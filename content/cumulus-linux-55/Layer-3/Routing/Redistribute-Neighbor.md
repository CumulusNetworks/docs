---
title: Redistribute Neighbor
author: NVIDIA
weight: 790
toc: 3
---
*Redistribute neighbor* provides a way for IP subnets to span racks without forcing the end hosts to run a routing protocol by announcing individual host /32 routes in the routed fabric. Other hosts on the fabric can use this new path to access the hosts in the fabric. If <span class="a-tooltip">[ECMP](## "Equal Cost Multi Path")</span> is available, traffic can load balance across the available paths natively.

Hosts use {{<link title="Address Resolution Protocol - ARP" text="ARP">}} to resolve MAC addresses when sending to an IPv4 address. A host then builds an ARP cache table of known MAC addresses: IPv4 tuples as they receive or respond to ARP requests.

For a leaf switch, where hosts within the rack use the default gateway, the ARP cache table contains a list of all hosts that ARP for their default gateway. In most cases, this table contains all the layer 3 information necessary. Redistribute neighbor formats and synchronizes this table into the routing protocol.

{{%notice note%}}
The current implementation of redistribute neighbor:

- Supports IPv4 only.
- Does not support {{<link url="Virtual-Routing-and-Forwarding-VRF" text="VRFs">}}.
- Supports a maximum of 1024 interfaces.
- Is not supported with <span class="a-tooltip">[EVPN](## "Ethernet Virtual Private Network")</span>. Enabling both redistribute neighbor and EVPN leads to unreachable IPv4 ARP and IPv6 neighbor entries.
{{%/notice%}}

## Target Use Cases and Best Practices

You use redistribute neighbor in these configurations:

- Virtualized clusters
- Hosts with service IP addresses that migrate between racks
- Hosts that are dual connected to two leaf nodes without using proprietary protocols such as {{<link url="Multi-Chassis-Link-Aggregation-MLAG" text="MLAG">}}
- Anycast services that need dynamic advertisement from multiple hosts

Follow these guidelines:

- You can connect a host to one or more leafs. Each leaf advertises the /32 it sees in its neighbor table.
- Make sure that a host-bound bridge or VLAN is local to each switch.
- Connect the leafs with redistribute neighbor directly to the hosts.
- Make sure that IP addresses do not overlap, as the host IP addresses are directly advertised into the routed fabric.
- Run redistribute neighbor on Linux-based hosts. NVIDIA does not test other host operating systems.

## How Does Redistribute Neighbor Work?

Redistribute neighbor works as follows:

1. The leaf or <span class="a-tooltip">[ToR](## "Top of Rack")</span> switch learns about connected hosts when the host sends an ARP request or ARP reply.
2. The kernel neighbor table adds an entry for the host of each leaf.
3. The redistribute neighbor daemon (`rdnbrd`) monitors the kernel neighbor table and creates a  /32 route for each neighbor entry. This /32 route is in kernel table 10.
4. <span class="a-tooltip">[FRR](## "FRRouting")</span> imports routes from kernel table 10.
5. A route map controls which routes to import from table 10.
6. FRR imports these routes as *table* routes.
7. You configure <span class="a-tooltip">[BGP](## "Border Gateway Protocol")</span> or <span class="a-tooltip">[OSPF](## "Open Shortest Path First")</span> to redistribute the table 10 routes.

## Example Configuration

The following example configuration uses the following topology.

{{< img src = "/images/cumulus-linux/redistribute-neighbor-example.png" >}}

### Configure the Leafs

{{< tabs "TabID59 ">}}
{{< tab "NVUE Commands ">}}

Cumulus Linux does not provide NVUE commands redistribute neighbor configuration.

{{< /tab >}}
{{< tab "vtysh Commands ">}}

1. Edit the `/etc/network/interfaces` file to configure the same IP address with a /32 prefix on both interfaces that face the host. In this example, swp1 and swp2 face server01 and server02:

    ```
    cumulus@leaf01:~$ sudo nano /etc/network/interfaces

    auto lo
    iface lo inet loopback
        address 10.0.0.1/32

    auto swp1
    iface swp1
        address 10.0.0.1/32

    auto swp2
    iface swp2
        address 10.0.0.1/32
    ...
    ```

2. Enable the daemon to start at boot up, then start the daemon:

    ```
    cumulus@leaf01:~$ sudo systemctl enable rdnbrd.service
    cumulus@leaf01:~$ sudo systemctl restart rdnbrd.service
    ```

3. Configure routing:

    1. Add the table as routes into the local routing table:

        ```
        cumulus@leaf01:~$ sudo vtysh

        leaf01# configure terminal
        leaf01(config)# ip import-table 10
        ```

    2. Define a route map that matches on the host-facing interface:

        ```
        leaf01(config)# route-map REDIST_NEIGHBOR permit 10
        leaf01(config-route-map)# match interface swp1
        leaf01(config-route-map)# route-map REDIST_NEIGHBOR permit 20
        leaf01(config-route-map)# match interface swp2
        ```

    3. Apply that route map to routes imported into *table*:

        ```
        leaf01(config)# ip import-table 10 route-map REDIST_NEIGHBOR
        ```

        To set the administrative distance to use for the routes, add the `distance` option before the route map name:

        ```
        leaf01(config)# ip import-table 10 distance 20 route-map REDIST_NEIGHBOR
        ```

    4. Redistribute the imported *table* routes into the appropriate routing protocol.

        **BGP:**

        ```
        leaf01(config)# router bgp 65001
        leaf01(config-router)# address-family ipv4 unicast
        leaf01(config-router-af)# redistribute table 10
        leaf01(config-router-af)# exit
        leaf01(config-router)# exit
        leaf01(config)# exit
        leaf01# write memory
        leaf01# exit
        cumulus@leaf01:~$
        ```

        **OSPF:**

        ```
        leaf01(config)# router ospf
        leaf01(config-router)# redistribute table 10
        leaf01(config-router)# exit
        leaf01(config)# exit
        leaf01# write memory
        leaf01# exit
        cumulus@leaf01:~$
        ```

The commands save the configuration in the `/etc/frr/frr.conf` file.

```
frr defaults datacenter
ip import-table 10 route-map REDIST_NEIGHBOR
username cumulus nopassword
!
service integrated-vtysh-config
!
log syslog informational
!
router bgp 65001
 !
 address-family ipv4 unicast
  redistribute table 10
 exit-address-family
!
route-map REDIST_NEIGHBOR permit 10
 match interface swp1
!
route-map REDIST_NEIGHBOR permit 20
 match interface swp2
!
router ospf
 redistribute table 10
!
line vty
!
```

{{< /tab >}}
{{< /tabs >}}

### Configure the Hosts

This document describes dual-connected Linux hosts with static IP addresses.

Configure a host with the same /32 IP address on its loopback and uplinks so that both leafs advertise the same /32 regardless of the interface. Cumulus Linux relies on {{<link url="Equal-Cost-Multipath-Load-Sharing-Hardware-ECMP" text="ECMP">}} to load balance across the interfaces southbound, and an equal cost static route (see the configuration below) to load balance northbound.

The loopback hosts the primary service IP address to which you can bind services.

Configure the loopback and physical interfaces. In the example topology above:
- server01 connects to leaf01 through eth1 and to leaf02 through eth2.
- lo, eth1, and eth2 use the loopback IP address.
- The `post-up arping` command forces the host to ARP as soon as its interface comes up. This allows the leaf to learn about the host as soon as possible.
- The `post-up ip route` commands install a default route through one or both leafs if both swp1 and swp2 are up.

    {{< expand "Configuration"  >}}

```
# The loopback network interface
auto lo
iface lo inet loopback

auto lo:1
iface lo:1
    address 10.1.0.101/32

auto eth1
iface eth1
    address 10.1.0.101/32
    post-up for i in {1..3}; do arping -q -c 1 -w 0 -i eth1 10.0.0.11; sleep 1; done
    post-up ip route add 0.0.0.0/0 nexthop via 10.0.0.11 dev eth1 onlink nexthop via 10.0.0.12 dev eth2 onlink || true

auto eth2
iface eth2
    address 10.1.0.101/32
    post-up for i in {1..3}; do arping -q -c 1 -w 0 -i eth2 10.0.0.12; sleep 1; done
    post-up ip route add 0.0.0.0/0 nexthop via 10.0.0.11 dev eth1 onlink nexthop via 10.0.0.12 dev eth2 onlink || true
...
```

{{< /expand >}}

### Install ifplugd

Install and use `{{<link url="ifplugd">}}`, which modifies the behavior of the Linux routing table when an interface undergoes a link transition (carrier up/down). By default, the Linux kernel keeps routes up even when the physical interface is unavailable (NO-CARRIER).

After you install `ifplugd`, edit `/etc/default/ifplugd` as follows, where *eth1* and *eth2* are the interface names that your host uses to connect to the leafs.

```
user@server01:$ sudo nano /etc/default/ifplugd
INTERFACES="eth1 eth2"
HOTPLUG_INTERFACES=""
ARGS="-q -f -u10 -d10 -w -I"
SUSPEND_ACTION="stop"
```

For complete instructions to install `ifplugd` on Ubuntu, [follow this guide]({{<ref "/knowledge-base/Configuration-and-Usage/Network-Interfaces/Using-ifplugd-on-a-Server-Host" >}}).

## Troubleshooting

### Check if rdnbrd is Running

`rdnbrd` is the redistribute neighbor daemon. To check if the daemon is running, run the `systemctl status rdnbrd.service` command:

```
cumulus@leaf01:~$ systemctl status rdnbrd.service
* rdnbrd.service - Cumulus Linux Redistribute Neighbor Service
 Loaded: loaded (/lib/systemd/system/rdnbrd.service; enabled)
 Active: active (running) since Wed 2016-05-04 18:29:03 UTC; 1h 13min ago
 Main PID: 1501 (python)
 CGroup: /system.slice/rdnbrd.service
 `-1501 /usr/bin/python /usr/sbin/rdnbrd -d
```

### Change rdnbrd Configuration

To change the default configuration of `rdnbrd`, edit the `/etc/rdnbrd.conf` file, then run `systemctl restart rdnbrd.service`:

```
cumulus@leaf01:~$ sudo nano /etc/rdnbrd.conf
# syslog logging level CRITICAL, ERROR, WARNING, INFO, or DEBUG
loglevel = INFO

# TX an ARP request to known hosts every keepalive seconds
keepalive = 1

# If a host does not send an ARP reply for holdtime consider the host down
holdtime = 3

# Install /32 routes for each host into this table
route_table = 10

# Uncomment to enable ARP debugs on specific interfaces.
# Note that ARP debugs can be very chatty.
# debug_arp = swp1 swp2 swp3 br1
# If we already know the MAC for a host, unicast the ARP request. This is
# unusual for ARP (why ARP if you know the destination MAC) but we will be
# using ARP as a keepalive mechanism and do not want to broadcast so many ARPs
# if we do not have to. If a host cannot handle a unicasted ARP request, set
#
# Unicasting ARP requests is common practice (in some scenarios) for other
# networking operating systems so it is unlikely that you will need to set
# this to False.
unicast_arp_requests = True
cumulus@leaf01:~$ sudo systemctl restart rdnbrd.service
```

### Set the Routing Table ID

The Linux kernel supports multiple routing tables and can use 0 through 255 table IDs; however it reserves tables 0, 253, 254 and 255, and uses 1 first. Therefore, `rdnbrd` only allows you to specify between 2 and 252. Cumulus Linux uses table ID 10, however you can set the ID to any value between 2 and 252. You can see all the tables specified here:

```
cumulus@leaf01:~$ cat /etc/iproute2/rt_tables
#
# reserved values
#
255 local
254 main
253 default
0 unspec
#
# local
#
#1  inr.ruhep
```

For more information, refer to {{<exlink url="http://linux-ip.net/html/routing-tables.html" text="Linux route tables">}} or you can read the {{<exlink url="https://manpages.ubuntu.com/manpages/eoan/en/man8/ip-route.8.html" text="Ubuntu man pages for ip route">}}.

### Check /32 Redistribute Neighbor Advertised Routes

For BGP, run the vtysh `show ip bgp neighbor <interface> advertised-routes` command. For example:

```
cumulus@leaf01:~$ show ip bgp neighbor swp51 advertise-routes
BGP table version is 5, local router ID is 10.0.0.11
Status codes: s suppressed, d damped, h history, * valid, > best, = multipath,
              i internal, r RIB-failure, S Stale, R Removed
Origin codes: i - IGP, e - EGP, ? - incomplete

    Network         Next Hop            Metric LocPrf Weight Path
*> 10.0.0.11/32     0.0.0.0                  0         32768 i
*> 10.0.0.12/32     ::                                     0 65020 65012 i
*> 10.0.0.21/32     ::                                     0 65020 i
*> 10.0.0.22/32     ::                                     0 65020 i

Total number of prefixes 4
```

### Verify the Kernel Routing Table

Use the following workflow to verify that the kernel routing table populates correctly and that routes import and advertise correctly:

1. Verify that ARP neighbor entries populate into the Kernel routing table 10.

    ```
    cumulus@leaf01:~$ ip route show table 10
    10.0.1.101 dev swp1 scope link
    ```

    If these routes do not generate, verify that the `rdnbrd` daemon is running and check that the `/etc/rdnbrd.conf` file includes the correct table number.

2. Verify that routes import into FRR from the kernel routing table 10.

    ```
    cumulus@leaf01:~$ sudo vtysh
    leaf01# show ip route table
    Codes: K - kernel route, C - connected, S - static, R - RIP,
            O - OSPF, I - IS-IS, B - BGP, A - Babel, T - Table,
            > - selected route, * - FIB route
    T[10]>* 10.0.1.101/32 [19/0] is directly connected, swp1, 01:25:29
    ```

    Both the \> and \* must be present so that table 10 routes install as preferred into the routing table. If the routes do not install, verify the imported distance of the locally imported kernel routes with the `ip import 10 distance X` command (where X is **not** less than the administrative distance of the routing protocol). If the distance is too low, routes learned from the protocol can overwrite the locally imported routes. Also, verify that the routes are in the kernel routing table.

3. Confirm that routes are in the BGP/OSPF database and that they advertise.

    ```
    leaf01# show ip bgp
    ```

## Considerations

### Route Scale

This feature adds each ARP entry as a /32 host route into the routing table of all switches within a summarization domain. Make sure the number of hosts plus fabric routes is under the allocated hardware LPM table size of the switch per the forwaring resource profile in use. Review the {{<exlink url="https://www.nvidia.com/en-us/networking/ethernet-switching/hardware-compatibility-list/" text="Cumulus Networks datasheets">}} for up to date scalability limits of your hardware platform. If in doubt, contact your support representative.

### Uneven Traffic Distribution

Linux uses *source* layer 3 addresses only to load balance on most older distributions.

### Silent Hosts Never Receive Traffic

Sometimes, freshly provisioned hosts that have yet to send traffic do not ARP for their default gateways. The `post-up arping` command in the  `/etc/network/interfaces` file on the host takes care of this. If the host does not ARP, then `rdnbrd` on the leaf does not learn about the host.
