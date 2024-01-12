---
title: Address Resolution Protocol - ARP
author: NVIDIA
weight: 1000
toc: 3
---
Address Resolution Protocol (ARP) is a communication protocol used for discovering the link layer address, such as a MAC address, associated with a given network layer address. ARP is defined by {{<exlink url="https://tools.ietf.org/html/rfc826" text="RFC 826">}}. The Cumulus Linux ARP implementation differs from standard Debian Linux ARP behavior in a few ways because Cumulus Linux is an operating system for routers/switches rather than servers.

## Standard Debian ARP Behavior and the Tunable ARP Parameters

Debian has these five tunable ARP parameters:

- `arp_accept`
- `arp_announce`
- `arp_filter`
- `arp_ignore`
- `arp_notify`

These parameters are described in the {{<exlink url="https://www.kernel.org/doc/Documentation/networking/ip-sysctl.txt" text="Linux documentation">}}, but snippets for each parameter description are included in the table below and are highlighted in *italics*.

In a standard Debian installation, all of these ARP parameters are set to *0*, leaving the router as wide open and unrestricted as possible. These settings are based on the assertion made long ago that Linux IP addresses are a property of the device, not a property of an individual interface. Therefore, an ARP request or reply could be sent on one interface containing an address residing on a different interface. While this unrestricted behavior makes sense for a server, it is not the normal behavior of a router. Routers expect the MAC/IP address mappings supplied by ARP to match the physical topology, with the IP addresses matching the interfaces on which they reside. With these tunable ARP parameters, Cumulus Linux is able to specify the behavior to match the expectations of a router.

## ARP Tunable Parameter Settings in Cumulus Linux

The ARP tunable parameters are set to the following values by default in Cumulus Linux.

| Parameter | Setting | Type | Description |
|---------- |-------- |----- |------------ |
| `arp_accept` | 0 | BOOL | Define behavior for gratuitous ARP frames whose IP is not already present in the ARP table:<ul><li>0: Do not create new entries in the ARP table.</li><li>1: Create new entries in the ARP table.</li></ul><br>Cumulus Linux uses the default `arp_accept` behavior of not creating new entries in the ARP table when a gratuitous ARP is seen on an interface or when an ARP reply packet is received. However, an individual interface can have the arp_accept behavior set differently than the remainder of the switch if needed. For information on how to apply this port-specific behavior, see below. |
| `arp_announce` | 2 | INT | Define different restriction levels for announcing the local source IP address from IP packets in ARP requests sent on interface:<ul><li>0: (default) Use any local address, configured on any interface.</li><li>1: Try to avoid local addresses that are not in the target's subnet for this interface. This mode is useful when target hosts reachable via this interface require the source IP address in ARP requests to be part of their logical network configured on the receiving interface. When Cumulus Linux generates the request, it checks all subnets that include the target IP  and preserves the source address if it is from such a subnet. If there is no such subnet. Cumulus Linux selects the source address according to the rules for level 2.</li><li>2: Always use the best local address for this target. In this mode Cumulus Linux ignores the source address in the IP packet and tries to select local address preferred for talks with the target host. Such local address is selected by looking for primary IP addresses on all the subnets on the outgoing interface that include the target IP address. If no suitable local address is found, Cumulus Linux selects the first local address on the outgoing interface or on all other interfaces, so that a reply for the request is received no matter the source IP address announced.</li></ul>The default Debian behavior with `arp_announce` set to 0 is to send gratuitous ARPs or ARP requests using any local source IP address, not limiting the IP source of the ARP packet to an address residing on the interface used to send the packet. This reflects the historically held view in Linux that IP addresses reside inside the device and are not considered a property of a specific interface.<br><br>Routers expect a different relationship between the IP address and the physical network. Adjoining routers look for MAC/IP addresses to reach a next hop residing on a connecting interface for transiting traffic. By setting the `arp_announce` parameter to 2, Cumulus Linux uses the best local address for each ARP request, preferring primary addresses on the interface used to send the ARP. This most closely matches traditional router ARP request behavior. |
| `arp_filter` | 0 | BOOL | <ul><li>0: (default) The kernel can respond to ARP requests with addresses from other interfaces to increase the chance of successful communication. IP addresses are owned by the complete host on Linux, not by particular interfaces. Only for more complex setups like load balancing, does this behavior cause problems.</li><li>1: Allows you to have multiple network interfaces on the same subnet and to have the ARPs for each interface answered based on whether or not the kernel routes a packet from the ARPd IP address out of that interface (therefore you must use source based routing for this to work). In other words, it allows control of which cards (usually 1) will respond to an ARP request.</li></ul>`arp_filter` for the interface is enabled if at least one of `conf/{all,interface}/arp_filter` is set to TRUE, it is disabled otherwise.<br><br>Cumulus Linux uses the default Debian Linux `arp_filter` setting of 0.<br>The `arp_filter` is primarily used when multiple interfaces reside in the same subnet and is used to allow or disallow which interfaces respond to ARP requests. For OSPF using IP unnumbered interfaces, many interfaces appear to be in the same subnet, and so actually contain the same address. If multiple interfaces are used between a pair of routers, having `arp_filter` set to 1 causes forwarding to fail. <br><br>The `arp_filter` parameter is set to allow a response on any interface in the subnet, where the `arp_ignore` setting (below) to limit cross-interface ARP behavior. |
| `arp_ignore` | 2 | INT | Define different modes for sending replies in response to received ARP requests that resolve local target IP addresses:<ul><li>0: (default) Reply for any local target IP address, configured on any interface.</li><li>1: Reply only if the target IP address is local address configured on the incoming interface.</li><li>2: Reply only if the target IP address is local address configured on the incoming interface and both with the sender's IP address are part from same subnet on this interface.</li><li>3: Do not reply for local addresses configured with scope host, only resolutions for global and link addresses are replied.</li><li>4-7: Reserved.</li><li>8: Do not reply for all local addresses.</li></ul>The maximum value from `conf/{all,interface}/arp_ignore` is used when the ARP request is received on the {interface}.<br><br>The default Debian `arp_ignore` parameter allows the device to reply to an ARP request for any IP address on any interface. While this matches the expectation that an IP address belongs to the device, not an interface, it can cause some unexpected and undesirable behavior on a router.<br><br>For example, if the `arp_ignore` parameter is set to 0 and an ARP request is received on one interface for the IP address residing on a different interface, the switch responds with an ARP reply even if the interface of the target address is down. This can cause a loss of traffic due to incorrect understanding about the reachability of next hops, and also makes troubleshooting extremely challenging for some failure conditions.<br><br>In Cumulus Linux, the `arp_ignore` value is set to 2 so that it only replies to ARP requests if the target IP address is a local address and both the sender's and target's IP addresses are part of the same subnet on the incoming interface. This should prevent the creation of stale neighbor entries when a peer device sends an ARP request from a source IP address that is not on the connected subnet. Eventually, the switch sends ARP requests to the host in an attempt to keep the entry fresh. If the host responds, the switch now has reachable neighbor entries for hosts that are not on the connected subnet. |
| `arp_notify` | 1 | BOOL | Define mode for notification of address and device changes.<ul><li>0: (default) Do nothing.</li><li>1: Generate gratuitous arp requests when device is brought up or hardware address changes.</li></ul>The default Debian arp_notify setting is to remain silent when an interface is brought up or the hardware address is changed. Since Cumulus Linux often acts as a next-hop for many end hosts, it immediately notifies attached devices when an interface comes up or the address changes. This speeds up convergence on the new information and provides the most rapid support for changes. |

## Change Tunable ARP Parameters

You can change the ARP parameter settings in several places, including:

- `/proc/sys/net/ipv4/conf/all/arp*` (all interfaces)
- `/proc/sys/net/ipv4/conf/default/arp*` (default for future interfaces)
- `/proc/sys/net/ipv4/conf/swp*/arp*` (individual interfaces)

The ARP parameter changes in Cumulus Linux use the *default* file locations.

The *all* and *default* locations sound similar, with the exception of which interfaces are impacted, but they operate in significantly different ways. The all location can **potentially** change the value for **all** interfaces running IP, both now and in the future. The reason for this uncertainty is that the *all* value is applied to each parameter using either *MAX* or *OR* logic between the *all* and any *port-specific* settings, as the following table shows:

| ARP Parameter | Condition |
| ------------- | --------- |
| arp\_accept   | OR        |
| arp\_announce | MAX       |
| arp\_filter   | OR        |
| arp\_ignore   | MAX       |
| arp\_notify   | MAX       |

For example, if you set the `/proc/sys/net/conf/all/arp_ignore` value to *1* and the `/proc/sys/net/conf/swp1/arp_ignore` value to *0* to try to disable it on a per-port basis, interface swp1 still uses the value of *1*; the port-specific setting does not override the global *all* setting. Instead, the MAX value between the *all* value and port-specific value defines the actual behavior.

The *default* location `/proc/sys/net/ipv4/conf/default/arp*` defines the values for all future IP interfaces. Changing the *default* setting of an ARP parameter does not impact interfaces that already contain an IP address. If changes are being made to a running system that already has IP addresses assigned to it, port-specific settings should be used instead.

{{%notice note%}}

In Cumulus Linux, the value of the *default* parameter is copied to every port-specific location, excluding those that already have an IP address assigned. Therefore, there is no complicated logic between the *default* setting and the *port-specific* setting like there is when using the *all* location. This makes the application of particular port-specific policies much simpler and more deterministic.

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

## Change Port-specific ARP Parameters

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

To enable proxy ARP:

{{< tabs "TabID137 ">}}

{{< tab "NCLU Commands ">}}

The following example commands enable proxy ARP on swp1.

```
cumulus@switch:~$ net add interface swp1 post-up "echo 1 > /proc/sys/net/ipv4/conf/swp1/proxy_arp"
cumulus@switch:~$ net pending
cumulus@switch:~$ net commit
```

{{< /tab >}}

{{< tab "Linux Commands ">}}

Edit the `/etc/network/interfaces` file to set `/proc/sys/net/ipv4/conf/<interface>/proxy_arp` to `1` in the interface stanza, then run the `ifreload -a` command. The following example configuration enables proxy ARP on swp1.

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

If you are running two interfaces in the same broadcast domain (typically seen when using {{<link url="Virtual-Router-Redundancy-VRR-and-VRRP" text="VRR">}}, which creates a `-v0` interface in the same broadcast domain), set `/proc/sys/net/ipv4/conf/<INTERFACE>/medium_id` to *2* on both the base SVI interface and the -v0 interface so that only one of the two interfaces replies when getting an ARP request. This prevents the v0 interface from proxy replying on behalf of the SVI (and the SVI from proxy replying on behalf of the v0 interface). You can only prevent duplicate replies when the ARP request is for the SVI or the v0 interface directly.

{{< tabs "TabID174 ">}}

{{< tab "NCLU Commands ">}}

```
cumulus@switch:~$ net add interface swp1 post-up "echo 2 > /proc/sys/net/ipv4/conf/swp1/medium_id"
cumulus@switch:~$ net add interface swp1-v0 post-up "echo 1 > /proc/sys/net/ipv4/conf/swp1-v0/proxy_arp"
cumulus@switch:~$ net add interface swp1-v0 post-up "echo 2 > /proc/sys/net/ipv4/conf/swp1-v0/medium_id"
cumulus@switch:~$ net pending
cumulus@switch:~$ net commit
```

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

{{< tab "NCLU Commands ">}}

```
cumulus@switch:~$ net add vlan 100 post-up "echo 1 > /proc/sys/net/ipv4/conf/swp1/proxy_arp"
cumulus@switch:~$ net add vlan 100 post-up "echo 1 > /proc/sys/net/ipv4/conf/swp1-v0/proxy_arp"
cumulus@switch:~$ net add vlan 100 post-up "echo 2 > /proc/sys/net/ipv4/conf/swp1/medium_id"
cumulus@switch:~$ net add vlan 100 post-up "echo 2 > /proc/sys/net/ipv4/conf/swp1-v0/medium_id"
cumulus@switch:~$ net pending
cumulus@switch:~$ net commit
```

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

In centralized VXLAN environments, where ARP/ND suppression is enabled and SVIs exist on the leaf switches but are not assigned an address within the subnet, problems with the Duplicate Address Detection process on Microsoft Windows hosts can occur. For example, in a pure layer 2 scenario or with SVIs that have the `ip-forward` option set to off, the IP address is not assigned to the SVI. The `neighmgrd` service selects a source IP address for an ARP probe based on the subnet match on the neighbor IP address. Because the SVI on which this neighbor is learned does not contiain an IP address, the subnet match fails. This results in `neighmgrd` using UNSPEC (0.0.0.0 for IPv4) as the source IP address in the ARP probe.

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
