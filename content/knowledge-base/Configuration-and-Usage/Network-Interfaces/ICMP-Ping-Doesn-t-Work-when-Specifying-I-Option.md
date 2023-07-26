---
title: ICMP Ping Doesn't Work when Specifying the -I Option
author: NVIDIA
weight: 419
toc: 4
---

## Issue
<!-- vale off -->
When I run `ping -I` and specify an interface I don't get an echo-reply. However, when I run `ping` without the `-I` option everything works as expected. What is going on?
<!-- vale on -->
## Specific Example for Issue

This example does not work:

    cumulus@switch:default:~:# ping -I swp2 50.50.50.1
    PING 50.50.50.1 (50.50.50.1) from 5.5.5.10 swp1.5: 56(84) bytes of data.

Whereas this example does work:

    cumulus@switch:default:~:# ping 50.50.50.1
    PING 50.50.50.1 (50.50.50.1) 56(84) bytes of data.
    64 bytes from 50.50.50.1: icmp_req=1 ttl=63 time=4.00 ms
    64 bytes from 50.50.50.1: icmp_req=2 ttl=63 time=0.000 ms
    64 bytes from 50.50.50.1: icmp_req=3 ttl=63 time=0.000 ms
    64 bytes from 50.50.50.1: icmp_req=4 ttl=63 time=0.000 ms
    ^C
    --- 50.50.50.1 ping statistics ---
    4 packets transmitted, 4 received, 0% packet loss, time 3004ms
    rtt min/avg/max/mdev = 0.000/1.000/4.001/1.732 ms
    cumulus@switch:default:~:#

{{<figure src="/images/knowledge-base/icmp-ping-I-option.png" width="350">}}

The image above has these IP addresses:

| Device | VLAN 2 | VLAN 5 |
| ------ | ------ | ------ |
| Edge router | 2.2.2.1 | N/A |
| Cumulus Linux switch | 2.2.2.5 | 5.5.5.5 |
| Hypervisor | 2.2.2.10 | 5.5.5.10 |

## Configurations

### Hypervisor

    auto swp1
    iface swp1
        address 2.2.2.10/24
        up ip route add 0.0.0.0/0 via 2.2.2.1
    
    auto swp2
    iface swp2
        address 5.5.5.10/24

### Cumulus Linux Switch

    auto swp1
    iface swp1
    
    auto swp2
    iface swp2
    
    auto swp17
    iface swp17
    
    auto bridge_2
    iface bridge_2
        address 2.2.2.5/24
        bridge-ports swp1 swp17
        up ip route add 0.0.0.0/0 via 2.2.2.1
    
    auto bridge_5
    iface bridge_5
        address 5.5.5.5/24
        bridge-ports swp2

### Edge Router

    auto swp30
    iface swp30
        address 50.50.50.2/24
    
    auto swp17
    iface swp17
        address 2.2.2.1/24
        up ip route add 5.5.5.0/24 via 2.2.2.5

### Internet Router

    auto swp1
    iface swp1
        address 50.50.50.1/24
        up route add -net 5.5.5.0/24 gw 50.50.50.2
        up route add -net 2.2.2.0/24 gw 50.50.50.2

## Explanation

What is happening here? **This behavior is actually as expected.** You do not need to have an SVI (switch VLAN interface) on the Cumulus Linux switch (in this particular example) for a host on the hypervisor to reach the "internet" (simulated here by another Cumulus Linux switch). The host has one default route (0.0.0.0/0) to 2.2.2.5, so when you specify the `-I` (interface) option, Cumulus Linux forces traffic to ARP for the destination (50.50.50.1) on the swp2 link between the Cumulus Linux switch and the hypervisor. There is no route on that interface (for that subnet) which forces the ARP on that link.  

When you ping from the Internet router down to each SVI, both of them are reachable. If there are hosts on the hypervisor, both of them are reachable as well because they have a gateway configured on the Cumulus Linux switch. The `-I` option forces the ARP and there is no route. If the hypervisor utilized namespaces to split the route table (allowing for dual default routes), you could ping from the hypervisor using the `-I` option. There are also various ways not tested here to solve the dual routing issue, depending on what your hypervisor or host is doing in the situation (such as IP rules or containers).

## See Also

- [Routing on Cumulus Linux]({{<ref "/cumulus-linux-43/Layer-3/Routing" >}})
- [Network Troubleshooting]({{<ref "/cumulus-linux-43/Monitoring-and-Troubleshooting/Network-Troubleshooting" >}})
- {{<exlink url="https://www.kernel.org/doc/Documentation/networking/ip-sysctl.txt" text="ip-sysctl on kernel.org">}}, which covers `arp_announce`
