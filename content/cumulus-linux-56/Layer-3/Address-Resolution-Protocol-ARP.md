---
title: Address Resolution Protocol - ARP
author: NVIDIA
weight: 1000
toc: 3
---
<span style="background-color:#F5F5DC">[ARP](## "Address Resolution Protocol")</span> is a communication protocol that discovers the link layer address, such as a MAC address, associated with a network layer address. The Cumulus Linux ARP implementation differs from standard Debian Linux ARP behavior because Cumulus Linux is an operating system for routers and switches, not servers.

For a definition of ARP, refer to {{<exlink url="https://tools.ietf.org/html/rfc826" text="RFC 826">}}.

## Standard Debian ARP Behavior and the Tunable ARP Parameters

Debian has these five tunable ARP parameters:

- `arp_accept`
- `arp_announce`
- `arp_filter`
- `arp_ignore`
- `arp_notify`

For a full description of these parameters, refer to the {{<exlink url="https://www.kernel.org/doc/Documentation/networking/ip-sysctl.txt" text="Linux documentation">}}.

The standard Debian installation sets these ARP parameters to *0*, leaving the router as wide open and unrestricted as possible. The Linux IP addresses are a property of the device, not an individual interface. Therefore, you can send an ARP request or reply on one interface with an address that resides on a different interface. While this unrestricted behavior makes sense for a server, it is not the normal behavior of a router. Routers expect the MAC and IP address mappings that ARP provides to match the physical topology, so that the IP addresses match the interfaces on which they reside. With these tunable ARP parameters, Cumulus Linux is able to specify the behavior to match the expectations of a router.

## ARP Tunable Parameter Settings in Cumulus Linux

| Parameter | Setting | Type | Description |
|---------- |-------- |----- |------------ |
| `arp_accept` | 0 | BOOL | Defines the behavior for gratuitous ARP frames when the IP address is not already in the ARP table:<ul><li>0: Do not create new entries in the ARP table (the default value).</li><li>1: Create new entries in the ARP table.</li></ul><br>You can set `arp_accept` on an individual interface which differs from the rest of the switch (see below). |
| `arp_announce` | 2 | INT | Defines different restriction levels for announcing the local source IP address from IP packets in ARP requests that send on an interface:<ul><li>0: Use any local address configured on any interface (the default value) .</li><li>1: Avoid local addresses that are not in the target subnet for this interface. You can use this mode when target hosts reachable through this interface require the source IP address in ARP requests to be part of their logical network configured on the receiving interface. When Cumulus Linux generates the request, it checks all subnets that include the target IP address and preserves the source address if it is from such a subnet. If there is no such subnet, Cumulus Linux selects the source address according to the rules for level 2.</li><li>2: Always use the best local address for this target. In this mode, Cumulus Linux ignores the source address in the IP packet and tries to select the local address preferred for talks with the target host. To select the local address, Cumulus Linux looks for primary IP addresses on all the subnets on the outgoing interface that include the target IP address. If there is no suitable local address, Cumulus Linux selects the first local address on the outgoing interface or on all other interfaces, so that it receives a reply for the request regardless of the announced source IP address.</li></ul>The default Debian behavior (`arp_announce` is 0) sends gratuitous ARPs or ARP requests using any local source IP address and does not limit the IP source of the ARP packet to an address residing on the interface that sends the packet.<br><br>Routers expect a different relationship between the IP address and the physical network. Adjoining routers look for MAC and IP addresses to reach a next hop residing on a connecting interface for transiting traffic. By setting the `arp_announce` parameter to 2, Cumulus Linux uses the best local address for each ARP request, preferring the primary addresses on the interface that sends the ARP. |
| `arp_filter` | 0 | BOOL | <ul><li>0: The kernel can respond to ARP requests with addresses from other interfaces to increase the chance of successful communication (the default value). The complete host on Linux (not specific interfaces) owns the IP addresses. For more complex configurations, such as load balancing, this behavior can cause problems.</li><li>1: Allows you to have multiple network interfaces on the same subnet and to answer the ARPs for each interface based on whether the kernel routes a packet from the ARPd IP address out of that interface (you must use source based routing).</li></ul>`arp_filter` for the interface is on if at least one of `conf/{all,interface}/arp_filter` is TRUE, it is off otherwise.<br><br>Cumulus Linux uses the default Debian Linux `arp_filter` setting of 0.<br>The switch uses `arp_filter` when multiple interfaces reside in the same subnet and allows certain interfaces to respond to ARP requests. For OSPF with IP unnumbered interfaces, multiple interfaces appear in the same subnet and contain the same address. If you use multiple interfaces between a pair of routers and set `arp_filter` to 1, forwarding can fail. <br><br>The `arp_filter` parameter allows a response on any interface in the subnet, where the `arp_ignore` setting (below) limits cross-interface ARP behavior. |
| `arp_ignore` | 2 | INT | Defines different modes for sending replies in response to received ARP requests that resolve local target IP addresses:<ul><li>0: Reply for any local target IP address on any interface (the default value).</li><li>1: Reply only if the target IP address is the local address on the incoming interface.</li><li>2: Reply only if the target IP address is the local address on the incoming interface and the sender IP address is part of same subnet on this interface.</li><li>3: Do not reply for local addresses with scope host; the switch replies only for global and link addresses.</li><li>4-7: Reserved.</li><li>8: Do not reply for all local addresses.</li></ul>The switch uses the maximum value from `conf/{all,interface}/arp_ignore` when the {interface} receives the ARP request.<br><br>The default Debian `arp_ignore` parameter allows the device to reply to an ARP request for any IP address on any interface. While this matches the expectation that an IP address belongs to the device, not an interface, it can cause some unexpected behavior on a router.<br><br>For example, if `arp_ignore` is 0 and the switch receives an ARP request on one interface for the IP address residing on a different interface, the switch responds with an ARP reply even if the interface of the target address is down. This can cause traffic loss because the switch does not know if it can reach the next hops and results in troubleshooting challenges for failure conditions.<br><br>In Cumulus Linux, the `arp_ignore` value is 2 so that the switch only replies to ARP requests if the target IP address is a local address and both the sender and target IP addresses are part of the same subnet on the incoming interface. The router does not create stale neighbor entries when a peer device sends an ARP request from a source IP address that is not on the connected subnet. Eventually, the switch sends ARP requests to the host to try to keep the entry fresh. If the host responds, the switch now has reachable neighbor entries for hosts that are not on the connected subnet. |
| `arp_notify` | 1 | BOOL | Defines the mode to notify address and device changes.<ul><li>0: Do nothing (the default value).</li><li>1: Generate gratuitous ARP requests when the device comes up or the hardware address changes.</li></ul>The default Debian `arp_notify` setting is to remain silent when an interface comes up or the hardware address changes. Because Cumulus Linux often acts as a next hop for several end hosts, it notifies attached devices when an interface comes up or the address changes, which speeds up new information convergence and provides the most rapid support for changes. |

## Change Tunable ARP Parameters

You can change the ARP parameter settings in several places, including:

- `/proc/sys/net/ipv4/conf/all/arp*` (all interfaces)
- `/proc/sys/net/ipv4/conf/default/arp*` (default for future interfaces)
- `/proc/sys/net/ipv4/conf/swp*/arp*` (individual interfaces)

The ARP parameter changes in Cumulus Linux use the *default* file locations.

The *all* and *default* locations sound similar but they operate in different ways. The all location can **potentially** change the value for **all** interfaces running IP, both now and in the future. The *all* value applies to each parameter using either *MAX* or *OR* logic between the *all* and any *port-specific* settings, as the following table shows:

| ARP Parameter | Condition |
| ------------- | --------- |
| arp\_accept   | OR        |
| arp\_announce | MAX       |
| arp\_filter   | OR        |
| arp\_ignore   | MAX       |
| arp\_notify   | MAX       |

For example, if you set the `/proc/sys/net/conf/all/arp_ignore` value to *1* and the `/proc/sys/net/conf/swp1/arp_ignore` value to *0* to try to disable it on a per-port basis, interface swp1 still uses the value of *1*; the port-specific setting does not override the global *all* setting. Instead, the MAX value between the *all* value and port-specific value defines the actual behavior.

The *default* location `/proc/sys/net/ipv4/conf/default/arp*` defines the values for all future IP interfaces. Changing the *default* setting of an ARP parameter does not impact interfaces that already have an IP address. If you make changes to a running system that already has assigned IP addresses, use port-specific settings instead.

{{%notice note%}}

Cumulus Linux copies the value of the *default* parameter to every port-specific location, excluding those that already have an IP address. There is no complicated logic between the *default* setting and the *port-specific* setting (unlike the *all* location).

{{%/notice%}}

To determine the current ARP parameter settings for each of the locations, run the following commands:

```
cumulus@switch:~$ sudo grep . /proc/sys/net/ipv4/conf/all/arp*
/proc/sys/net/ipv4/conf/all/arp_accept:0
/proc/sys/net/ipv4/conf/all/arp_announce:0
/proc/sys/net/ipv4/conf/all/arp_filter:0
/proc/sys/net/ipv4/conf/all/arp_ignore:0
/proc/sys/net/ipv4/conf/all/arp_notify:0
```

```
cumulus@switch:~$ sudo grep . /proc/sys/net/ipv4/conf/default/arp*
/proc/sys/net/ipv4/conf/default/arp_accept:0
/proc/sys/net/ipv4/conf/default/arp_announce:2
/proc/sys/net/ipv4/conf/default/arp_filter:0
/proc/sys/net/ipv4/conf/default/arp_ignore:2
/proc/sys/net/ipv4/conf/default/arp_notify:1
```

```
cumulus@switch:~$ sudo grep . /proc/sys/net/ipv4/conf/swp1/arp*
/proc/sys/net/ipv4/conf/swp1/arp_accept:0
/proc/sys/net/ipv4/conf/swp1/arp_announce:2
/proc/sys/net/ipv4/conf/swp1/arp_filter:0
/proc/sys/net/ipv4/conf/swp1/arp_ignore:2
/proc/sys/net/ipv4/conf/swp1/arp_notify:1
cumulus@switch:~$
```

Cumulus Linux implements this change at boot time using the `arp.conf` file in the following location:

```
cumulus@switch:~$ cat /etc/sysctl.d/arp.conf
net.ipv4.conf.default.arp_announce = 2
net.ipv4.conf.default.arp_notify = 1
net.ipv4.conf.default.arp_ignore=1
cumulus@switch:~$
```
<!-- vale off -->
## Change Port-specific ARP Parameters
<!-- vale on -->
To configure port-specific ARP parameters in a running device, run the following command:

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

When you enable proxy ARP, if the switch receives an ARP request for which it has a route to the destination IP address, the switch sends a proxy ARP reply that contains its own MAC address. The host that sent the ARP request then sends its packets to the switch and the switch forwards the packets to the intended host.

{{%notice note%}}
Proxy ARP works with IPv4 only; ARP is an IPv4-only protocol.
{{%/notice%}}

The following example commands enable proxy ARP on swp1.

{{< tabs "TabID137 ">}}
{{< tab "NVUE Commands ">}}

Cumulus Linux does not provide NVUE commands for this setting.

{{< /tab >}}
{{< tab "Linux Commands ">}}

Edit the `/etc/network/interfaces` file to set `/proc/sys/net/ipv4/conf/<interface>/proxy_arp` to `1` in the interface stanza, then run the `ifreload -a` command.

```
cumulus@switch:~$ sudo nano /etc/network/interfaces
...
auto swp1
iface swp1
    post-up echo 1 > /proc/sys/net/ipv4/conf/swp1/proxy_arp
...
```

```
cumulus@switch:~$ sudo ifreload -a
```

{{< /tab >}}
{{< /tabs >}}

If you are running two interfaces in the same broadcast domain (typically seen when using {{<link url="Virtual-Router-Redundancy-VRR" text="VRR">}}, which creates a `-v0` interface in the same broadcast domain), set `/proc/sys/net/ipv4/conf/<INTERFACE>/medium_id` to *2* on both the interface and the -v0 interface so that both interfaces do not respond with proxy ARP replies.

{{< tabs "TabID174 ">}}
{{< tab "NVUE Commands ">}}

Cumulus Linux does not provide NVUE commands for this setting.

{{< /tab >}}
{{< tab "Linux Commands ">}}

Edit the `/etc/network/interfaces` file, then run the `ifreload -a` command. For example:

```
cumulus@switch:~$ sudo nano /etc/network/interfaces
...
auto swp1
iface swp1
    post-up echo 1 > /proc/sys/net/ipv4/conf/swp1/proxy_arp
    post-up echo 2 > /proc/sys/net/ipv4/conf/swp1/medium_id

auto swp1-v0
iface swp1-v0
    post-up echo 1 > /proc/sys/net/ipv4/conf/swp1-v0/proxy_arp
    post-up echo 2 > /proc/sys/net/ipv4/conf/swp1-v0/medium_id
...
```

```
cumulus@switch:~$ sudo ifreload -a
```

{{< /tab >}}
{{< /tabs >}}

If you are running proxy ARP on a VRR interface, add a post-up line to the VRR interface stanza similar to the following. For example, if vlan100 is the VRR interface for the configuration above:

{{< tabs "TabID217 ">}}
{{< tab "NVUE Commands ">}}

Cumulus Linux does not provide NVUE commands for this setting.

{{< /tab >}}
{{< tab "Linux Commands ">}}

Edit the `/etc/network/interfaces` file, then run the `ifreload -a` command. For example:

```
cumulus@switch:~$ sudo nano /etc/networks/interfaces
...
auto vlan100
iface vlan100
    post-up echo 1 > /proc/sys/net/ipv4/conf/swp1-v0/proxy_arp
    post-up echo 1 > /proc/sys/net/ipv4/conf/swp1/proxy_arp
    post-up echo 2 > /proc/sys/net/ipv4/conf/swp1-v0/medium_id
    post-up echo 2 > /proc/sys/net/ipv4/conf/swp1/medium_id
    vlan-id 100
...
```

```
cumulus@switch:~$ sudo ifreload -a
```

{{< /tab >}}
{{< /tabs >}}

## Duplicate Address Detection (Windows Hosts)

In centralized VXLAN environments with ARP and ND suppression, if the SVIs on the leafs but do not have an IP address within the subnet, problems with the Duplicate Address Detection process on Microsoft Windows hosts occur. For example, in a pure layer 2 scenario or with SVIs that have the `ip-forward` option off, the SVI does not have an IP address. The `neighmgrd` service selects a source IP address for an ARP probe based on the subnet match on the neighbor IP address. Because the SVI that learns this neighbor does not have an IP address, the subnet match fails and `neighmgrd` uses UNSPEC (0.0.0.0 for IPv4) as the source IP address in the ARP probe.

To work around this issue, run the `neighmgrctl setsrcipv4 <ipaddress>` command to specify a non-0.0.0.0 address for the source; for example:

```
cumulus@switch:~$ neighmgrctl setsrcipv4 10.1.0.2
```

The configuration above does not persist if you reboot the switch. To make the changes apply persistently:

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

## Neighbor Base Reachable Timer

You can set how long a neighbor cache entry is valid with the NVUE `nv set system global arp base-reachable-time` command. The entry is considered valid for at least the value between the base reachable time divided by two and three times the base reachable time divided by two. You can specify a value between 30 and 2147483 seconds.

The following example configures the neighbor base reachable timer to 50 seconds.

```
cumulus@leaf01:~$ nv set system global arp base-reachable-time 50
cumulus@leaf01:~$ nv config apply
```

To reset the neighbor base reachable timer to the default setting, run the `nv unset system global arp base-reachable-time` command.

To show the neighbor base reachable timer setting, run the `nv show system global arp` command:

```
cumulus@leaf02:mgmt:~$ nv show system global arp
                              operational  applied
----------------------------  -----------  -------
base-reachable-time           50           50   
garbage-collection-threshold                      
  effective                   35840               
  maximum                     40960               
  minimum                     128            
```

## ARP Refresh

Cumulus Linux does not interact directly with end systems as much as end systems interact with each another. Therefore, after ARP places a neighbor into a reachable state, if Cumulus Linux does not interact with the client again for a long enough period of time, the neighbor can move into a stale state. To keep neighbors in the reachable state, Cumulus Linux includes a background process (`/usr/bin/neighmgrd`). The background process tracks neighbors that move into a stale, delay, or probe state, and attempts to refresh their state before removing them from the Linux kernel and from hardware forwarding. The `neighmgrd` process adds a neighbor if the sender IP in the ARP packet is in one of the SVI's subnets (you can disable this check by setting `subnet_checks` to *0* in the `/etc/cumulus/neighmgr.conf` file).

The ARP refresh timer defaults to 1080 seconds (18 minutes).
