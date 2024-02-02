---
title: Address Resolution Protocol - ARP
author: NVIDIA
weight: 179
pageID: 8362976
---
Address Resolution Protocol (ARP) is a communication protocol used for discovering the link layer  address, such as a MAC address, associated with a given network layer  address. ARP is defined by {{<exlink url="https://tools.ietf.org/html/rfc826" text="RFC 826">}}.

The  Cumulus Linux ARP implementation differs from standard Debian Linux ARP behavior in a few ways because Cumulus Linux is an operating system for routers/switches rather than servers. This chapter describes the differences in ARP behavior, why the changes were made, where the changes were implemented, and how to change port-specific values.

## Standard Debian ARP Behavior and the Tunable ARP Parameters

Debian has these five tunable ARP parameters:

- `arp_accept`
- `arp_announce`
- `arp_filter`
- `arp_ignore`
- `arp_notify`

These parameters are described in the {{<exlink url="https://www.kernel.org/doc/Documentation/networking/ip-sysctl.txt" text="Linux documentation">}}, but snippets for each parameter description are included in the table below and are highlighted in *italics*.

In a standard Debian installation, all of these ARP parameters are set to *0*, leaving the router as wide open and unrestricted as possible. These settings are based on the assertion made long ago that Linux IP addresses are a property of the device, not a property of an individual interface. Thus an ARP request or reply could be sent on one interface containing an address residing on a different interface. While this unrestricted behavior makes sense for a server, it is not the normal behavior of a router. Routers expect the MAC/IP address mappings supplied by ARP to match the physical topology, with the IP addresses matching the interfaces on which they reside. With these tunable ARP parameters, Cumulus Linux has been able to specify the behavior to match the expectations of a router.

## ARP Tunable Parameter Settings in Cumulus Linux

The ARP tunable parameters are set to the following values by default in Cumulus Linux.

| Parameter |Default Setting | Type | Description |
|---------- |-------- |----- |------------ |
| `arp_accept` | 0 | BOOL | Defines the behavior for gratuitous ARP frames when the IP address is not already in the ARP table:<ul><li>0: Do not create new entries in the ARP table.</li><li>1: Create new entries in the ARP table.</li></ul><br>You can set `arp_accept` on an individual interface which differs from the rest of the switch (see below). |
| `arp_announce` | 2 | INT | Defines different restriction levels for announcing the local source IP address from IP packets in ARP requests that send on an interface:<ul><li>0: Use any local address configured on any interface.</li><li>1: Avoid local addresses that are not in the target subnet for this interface. You can use this mode when target hosts reachable through this interface require the source IP address in ARP requests to be part of their logical network configured on the receiving interface. When Cumulus Linux generates the request, it checks all subnets that include the target IP address and preserves the source address if it is from such a subnet. If there is no such subnet, Cumulus Linux selects the source address according to the rules for level 2.</li><li>2: Always use the best local address for this target. In this mode, Cumulus Linux ignores the source address in the IP packet and tries to select the local address preferred for talks with the target host. To select the local address, Cumulus Linux looks for primary IP addresses on all the subnets on the outgoing interface that include the target IP address. If there is no suitable local address, Cumulus Linux selects the first local address on the outgoing interface or on all other interfaces, so that it receives a reply for the request regardless of the announced source IP address.</li></ul>The default Debian behavior (`arp_announce` is 0) sends gratuitous ARPs or ARP requests using any local source IP address and does not limit the IP source of the ARP packet to an address residing on the interface that sends the packet.<br><br>Routers expect a different relationship between the IP address and the physical network. Adjoining routers look for MAC and IP addresses to reach a next hop residing on a connecting interface for transiting traffic. By setting the `arp_announce` parameter to 2, Cumulus Linux uses the best local address for each ARP request, preferring the primary addresses on the interface that sends the ARP. |
| `arp_filter` | 0 | BOOL | <ul><li>0: The kernel can respond to ARP requests with addresses from other interfaces to increase the chance of successful communication. The complete host on Linux (not specific interfaces) owns the IP addresses. For more complex configurations, such as load balancing, this behavior can cause problems.</li><li>1: Allows you to have multiple network interfaces on the same subnet and to answer the ARPs for each interface based on whether the kernel routes a packet from the ARPd IP address out of that interface (you must use source based routing).</li></ul>`arp_filter` for the interface is on if at least one of `conf/{all,interface}/arp_filter` is TRUE, it is off otherwise.<br><br>Cumulus Linux uses the default Debian Linux `arp_filter` setting of 0.<br>The switch uses `arp_filter` when multiple interfaces reside in the same subnet and allows certain interfaces to respond to ARP requests. For OSPF with IP unnumbered interfaces, multiple interfaces appear in the same subnet and contain the same address. If you use multiple interfaces between a pair of routers and set `arp_filter` to 1, forwarding can fail. <br><br>The `arp_filter` parameter allows a response on any interface in the subnet, where the `arp_ignore` setting (below) limits cross-interface ARP behavior. |
| `arp_ignore` | 1 | INT | Defines different modes for sending replies in response to received ARP requests that resolve local target IP addresses:<ul><li>0: Reply for any local target IP address on any interface.</li><li>1: Reply only if the target IP address is the local address on the incoming interface.</li><li>2: Reply only if the target IP address is the local address on the incoming interface and the sender IP address is part of same subnet on this interface.</li><li>3: Do not reply for local addresses with scope host; the switch replies only for global and link addresses.</li><li>4-7: Reserved.</li><li>8: Do not reply for all local addresses.</li></ul>The switch uses the maximum value from `conf/{all,interface}/arp_ignore` when the {interface} receives the ARP request.<br><br>The default `arp_ignore` setting of 1 allows the device to reply to an ARP request for any IP address on any interface. While this matches the expectation that an IP address belongs to the device, not an interface, it can cause some unexpected behavior on a router.<br><br>For example, if `arp_ignore` is 0 and the switch receives an ARP request on one interface for the IP address residing on a different interface, the switch responds with an ARP reply even if the interface of the target address is down. This can cause traffic loss because the switch does not know if it can reach the next hops and results in troubleshooting challenges for failure conditions.<br><br>If you set `arp_ignore` to 2, the switch only replies to ARP requests if the target IP address is a local address and both the sender and target IP addresses are part of the same subnet on the incoming interface. The router does not create stale neighbor entries when a peer device sends an ARP request from a source IP address that is not on the connected subnet. Eventually, the switch sends ARP requests to the host to try to keep the entry fresh. If the host responds, the switch now has reachable neighbor entries for hosts that are not on the connected subnet. |
| `arp_notify` | 1 | BOOL | Defines the mode to notify address and device changes.<ul><li>0: Do nothing.</li><li>1: Generate gratuitous ARP requests when the device comes up or the hardware address changes.</li></ul>The default Debian `arp_notify` setting is to remain silent when an interface comes up or the hardware address changes. Because Cumulus Linux often acts as a next hop for several end hosts, it notifies attached devices when an interface comes up or the address changes, which speeds up new information convergence and provides the most rapid support for changes. |

## Change Tunable ARP Parameters

You can change the ARP parameter settings in several places, including:

- `/proc/sys/net/ipv4/conf/all/arp*` (all interfaces)
- `/proc/sys/net/ipv4/conf/default/arp*` (default for future interfaces)
- `/proc/sys/net/ipv4/conf/swp*/arp*` (individual interfaces)

The ARP parameter changes in Cumulus Linux use the *default* file locations.

The *all* and *default* locations sound similar, with the exception of which interfaces are impacted, but they operate in significantly different ways. The all location can **potentially** change the value for **all** interfaces running IP, both now and in the future. The reason for this uncertainty is that the *all* value is applied to each parameter using either *MAX* or *OR* logic between the *all* and any *port-specific* settings, as the following table shows:

| ARP Parameter | Condition |
| ------------- | --------- |
| `arp_accept`  | OR        |
| `arp_announce`| MAX       |
| `arp_filter`  | OR        |
| `arp_ignore`  | MAX       |
| `arp_notify`  | MAX       |

For example, if the `/proc/sys/net/conf/all/arp_ignore` value is set to *1* and the `/proc/sys/net/conf/swp1/arp_ignore` value is set to *0*, to try to disable it on a per-port basis, interface swp1 still uses the value of *1* in its operation. While it may appear that the port-specific setting should override the global *all* setting, it does not actually work that way. Instead, the MAX value between the *all* value and port-specific value defines the actual behavior.

The *default* location `/proc/sys/net/ipv4/conf/default/arp*` defines the values for all future IP interfaces. Changing the *default* setting of an ARP parameter does not impact interfaces that already contain an IP address. If changes are being made to a running system that already has IP addresses assigned to it, port-specific settings should be used instead.

{{%notice note%}}

The way the *default* setting is implemented in Linux, the value of the *default* parameter is copied to every port-specific location, excluding those that already have an IP address assigned, as previously mentioned. Therefore there is not any complicated logic between the *default* setting and the *port-specific* setting like there is when using the *all* location. This makes the application of particular port-specific policies much simpler and more deterministic.

{{%/notice%}}

To determine the current ARP parameter settings for each of the the locations, use the following mechanism; other methods are available but this one is quite simple:

```
cumulus@switch:~$ sudo grep . /proc/sys/net/ipv4/conf/all/arp*
/proc/sys/net/ipv4/conf/all/arp_accept:0
/proc/sys/net/ipv4/conf/all/arp_announce:0
/proc/sys/net/ipv4/conf/all/arp_filter:0
/proc/sys/net/ipv4/conf/all/arp_ignore:0
/proc/sys/net/ipv4/conf/all/arp_notify:0

cumulus@switch:~$ sudo grep . /proc/sys/net/ipv4/conf/default/arp*
/proc/sys/net/ipv4/conf/default/arp_accept:0
/proc/sys/net/ipv4/conf/default/arp_announce:2
/proc/sys/net/ipv4/conf/default/arp_filter:0
/proc/sys/net/ipv4/conf/default/arp_ignore:1
/proc/sys/net/ipv4/conf/default/arp_notify:1

cumulus@switch:~$ sudo grep . /proc/sys/net/ipv4/conf/swp1/arp*
/proc/sys/net/ipv4/conf/swp1/arp_accept:0
/proc/sys/net/ipv4/conf/swp1/arp_announce:2
/proc/sys/net/ipv4/conf/swp1/arp_filter:0
/proc/sys/net/ipv4/conf/swp1/arp_ignore:1
/proc/sys/net/ipv4/conf/swp1/arp_notify:1
cumulus@switch:~$
```

Note that Cumulus Linux implements this change at boot time using the `arp.conf` file at the following location:

```
cumulus@switch:~$ cat /etc/sysctl.d/arp.conf
net.ipv4.conf.default.arp_announce = 2
net.ipv4.conf.default.arp_notify = 1
net.ipv4.conf.default.arp_ignore=1
cumulus@switch:~$
```

## Change Port-specific ARP Parameters

The simplest way to configure port-specific ARP parameters in a running device is with the following command:

```
cumulus@switch:~$ sudo sh -c "echo 0 > /proc/sys/net/ipv4/conf/swp1/arp_ignore"
cumulus@switch:~$ sudo grep . /proc/sys/net/ipv4/conf/swp1/arp*
/proc/sys/net/ipv4/conf/swp1/arp_accept:0
/proc/sys/net/ipv4/conf/swp1/arp_announce:2
/proc/sys/net/ipv4/conf/swp1/arp_filter:0
/proc/sys/net/ipv4/conf/swp1/arp_ignore:0
/proc/sys/net/ipv4/conf/swp1/arp_notify:1
cumulus@switch:~$
```

To make the change persist through reboots, edit the `/etc/sysctl.d/arp.conf` file and add your port-specific ARP setting.

## Configure Proxy ARP

The proxy ARP setting is a kernel setting that you can manipulate using `sysctl` or `sysfs`. Proxy ARP works with IPv4 only, since ARP is an IPv4-only protocol.

You need to set `/proc/sys/net/ipv4/conf/<INTERFACE>/proxy_arp` to *1*:

```
cumulus@switch:~$ net add interface swp1 post-up "echo 1 > /proc/sys/net/ipv4/conf/swp1/proxy_arp"
cumulus@switch:~$ net pending
cumulus@switch:~$ net commit
```

These commands create the following snippet in the `/etc/network/interfaces` file:

```
auto swp1
iface swp1
    post-up echo 1 > /proc/sys/net/ipv4/conf/swp1/proxy_arp
```

If you are running two interfaces in the same broadcast domain (typically seen when using {{<link url="Virtual-Router-Redundancy-VRR-and-VRRP" text="VRR">}}, which creates a `-v0` interface in the same broadcast domain), set `/proc/sys/net/ipv4/conf/<INTERFACE>/medium_id` to *2* on both the base SVI interface and the -v0 interface so that only one of the two interfaces replies when getting an ARP request. This prevents the v0 interface from proxy replying on behalf of the SVI (and the SVI from proxy replying on behalf of the v0 interface). You can only prevent duplicate replies when the ARP request is for the SVI or the v0 interface directly.

```
cumulus@switch:~$ net add interface swp1 post-up "echo 2 > /proc/sys/net/ipv4/conf/swp1/medium_id"
cumulus@switch:~$ net add interface swp1-v0 post-up "echo 1 > /proc/sys/net/ipv4/conf/swp1-v0/proxy_arp"
cumulus@switch:~$ net add interface swp1-v0 post-up "echo 2 > /proc/sys/net/ipv4/conf/swp1-v0/medium_id"
cumulus@switch:~$ net pending
cumulus@switch:~$ net commit
```

These commands create the following snippet in the `/etc/network/interfaces` file:

```
auto swp1
iface swp1
    post-up echo 1 > /proc/sys/net/ipv4/conf/swp1/proxy_arp
    post-up echo 2 > /proc/sys/net/ipv4/conf/swp1/medium_id

auto swp1-v0
iface swp1-v0
    post-up echo 1 > /proc/sys/net/ipv4/conf/swp1-v0/proxy_arp
    post-up echo 2 > /proc/sys/net/ipv4/conf/swp1-v0/medium_id
```

If you are running proxy ARP on a VRR interface, add a post-up line to the VRR interface stanza similar to the following. For example, if vlan100 is the VRR interface for the configuration above:

```
cumulus@switch:~$ net add vlan 100 post-up "echo 1 > /proc/sys/net/ipv4/conf/swp1/proxy_arp && echo 1 > /proc/sys/net/ipv4/conf/swp1-v0/proxy_arp && echo 2 > /proc/sys/net/ipv4/conf/swp1/medium_id && echo 2 > /proc/sys/net/ipv4/conf/swp1-v0/medium_id"
cumulus@switch:~$ net pending
cumulus@switch:~$ net commit
```

## Duplicate Address Detection (Windows Hosts)

In centralized VXLAN environments, where ARP/ND suppression is enabled and SVIs exist on the leaf switches but are not assigned an address within the subnet, problems with the Duplicate Address Detection process on Microsoft Windows hosts can occur. For example, in a pure layer 2 scenario or with SVIs that have the `ip-forward` option set to off, the IP address is not assigned to the SVI. The `neighmgrd` service selects a source IP address for an ARP probe based on the subnet match on the neighbor IP address. Because the SVI on which this neighbor is learned does not contain an IP address, the subnet match fails. This results in `neighmgrd` using UNSPEC (0.0.0.0 for IPv4) as the source IP address in the ARP probe.

To work around this issue, run the `neighmgrctl setsrcipv4 <ipaddress>` command to specify a non-0.0.0.0 address for the source; for example:

```
cumulus@switch:~$ neighmgrctl setsrcipv4 10.1.0.2
```

The configuration above takes effect immediately but does not persist if you reboot the switch. To make the changes apply persistently:

1. Create a new file called `/etc/cumulus/neighmgr.conf` and add the `setsrcipv4 <ipaddress>` option; for example:

    ```
    cumulus@switch:~$  sudo nano /etc/cumulus/neighmgr.conf

    [main]
    setsrcipv4: 10.1.0.2
    ```

2. Restart the `neighmgrd` service:

    ```
    cumulus@switch:~$ sudo systemctl restart neighmgrd
    ```
