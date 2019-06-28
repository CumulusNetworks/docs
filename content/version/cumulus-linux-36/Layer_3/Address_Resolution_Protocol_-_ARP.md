---
title: Address Resolution Protocol - ARP
author: Cumulus Networks
weight: 175
aliases:
 - /display/CL36/Address+Resolution+Protocol+-+ARP
 - /pages/viewpage.action?pageId=8362442
pageID: 8362442
product: Cumulus Linux
version: '3.6'
imgData: cumulus-linux-36
siteSlug: cumulus-linux-36
---
Address Resolution Protocol <span style="color: #222222;"> ( </span> ARP
<span style="color: #222222;"> ) is a </span> communication protocol
<span style="color: #222222;"> used for discovering the </span> link
layer <span style="color: #222222;"> address, such as a </span> MAC
address <span style="color: #222222;"> , associated with a given </span>
network layer <span style="color: #222222;"> address </span>
<span style="color: #222222;"> . ARP is defined by </span>
[RFC 826](https://tools.ietf.org/html/rfc826).
<span style="color: #222222;"> The </span> Cumulus Linux ARP
implementation differs from standard Debian Linux ARP behavior in a few
ways because Cumulus Linux is an operating system for routers/switches
rather than servers. This chapter describes the differences in ARP
behavior, why the changes were made, where the changes were implemented,
and how to change port-specific values.

## <span>Standard Debian ARP Behavior and the Tunable ARP Parameters</span>

Debian has these five tunable ARP parameters:

  - arp\_accept

  - arp\_announce

  - arp\_filter

  - arp\_ignore

  - arp\_notify

These parameters are described in the [Linux
documentation](https://www.kernel.org/doc/Documentation/networking/ip-sysctl.txt),
but snippets for each parameter description are included in the table
below and are highlighted in *italics*.

In a standard Debian installation, all of these ARP parameters are set
to *0*, leaving the router as wide open and unrestricted as possible.
These settings are based on the assertion made long ago that Linux IP
addresses are a property of the device, not a property of an individual
interface. Thus an ARP request or reply could be sent on one interface
containing an address residing on a different interface. While this
unrestricted behavior makes sense for a server, it is not the normal
behavior of a router. Routers expect the MAC/IP address mappings
supplied by ARP to match the physical topology, with the IP addresses
matching the interfaces on which they reside. With these tunable ARP
parameters, Cumulus Linux has been able to specify the behavior to match
the expectations of a router.

### <span>ARP Tunable Parameter Settings in Cumulus Linux</span>

The ARP tunable parameters are set to the following values by default in
Cumulus Linux. Each parameter is described in detail, including why
Cumulus Networks chose the value used.

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Parameter</p></th>
<th><p>Setting</p></th>
<th><p>Type</p></th>
<th><p>Description</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>arp_accept</p></td>
<td><p>0</p></td>
<td><p>BOOL</p></td>
<td><p><em>Define behavior for gratuitous ARP frames whose IP is not already present in the ARP table:</em></p>
<p><em>0 - Don't create new entries in the ARP table.</em></p>
<p><em>1 - Create new entries in the ARP table.</em></p>
<p>Cumulus Linux uses the default <code>arp_accept</code> behavior of not creating new entries in the ARP table when a gratuitous ARP is seen on an interface or when an ARP reply packet is received. However, an individual interface can have the <code>arp_accept</code> behavior set differently than the remainder of the switch if needed. For information on how to apply this port-specific behavior, <a href="#src-8362442_AddressResolutionProtocol-ARP-po">see below</a>.</p></td>
</tr>
<tr class="even">
<td><p>arp_announce</p></td>
<td><p>2</p></td>
<td><p>INT</p></td>
<td><p><em>Define different restriction levels for announcing the local source IP address from IP packets in ARP requests sent on interface:</em></p>
<p><em>0 - (default) Use any local address, configured on any interface.</em></p>
<p><em>1 - Try to avoid local addresses that are not in the target's subnet for this interface. This mode is useful when target hosts reachable via this interface require the source IP address in ARP requests to be part of their logical network configured on the receiving interface. When we generate the request we will check all our subnets that include the target IP and will preserve the source address if it is from such subnet. If there is no such subnet we select source address according to the rules for level 2.</em></p>
<p><em>2 - Always use the best local address for this target. In this mode we ignore the source address in the IP packet and try to select local address that we prefer for talks with the target host. Such local address is selected by looking for primary IP addresses on all our subnets on the outgoing interface that include the target IP address. If no suitable local address is found we select the first local address we have on the outgoing interface or on all other interfaces, with the hope we will receive reply for our request and even sometimes no matter the source IP address we announce.</em></p>
<p>The default Debian behavior with <code>arp_announce</code> set to <em>0</em> is to send gratuitous ARPs or ARP requests using any local source IP address, not limiting the IP source of the ARP packet to an address residing on the interface used to send the packet. This reflects the historically held view in Linux that IP addresses reside <em>inside</em> the device and are not considered a property of a specific interface.</p>
<p>Routers expect a different relationship between the IP address and the physical network. Adjoining routers look for MAC/IP addresses to reach a next-hop residing on a connecting interface for transiting traffic. By setting the <code>arp_announce</code> parameter to <em>2</em>, Cumulus Linux uses the best local address for each ARP request, preferring primary addresses on the interface used to send the ARP. This most closely matches traditional router ARP request behavior.</p></td>
</tr>
<tr class="odd">
<td><p>arp_filter</p></td>
<td><p>0</p></td>
<td><p>BOOL</p></td>
<td><p><em>0 - (default) The kernel can respond to ARP requests with addresses from other interfaces. This may seem wrong but it usually makes sense, because it increases the chance of successful communication. IP addresses are owned by the complete host on Linux, not by particular interfaces. Only for more complex setups like load- balancing, does this behavior cause problems.</em></p>
<p><em>1 - Allows you to have multiple network interfaces on the same subnet, and have the ARPs for each interface be answered based on whether or not the kernel would route a packet from the ARP'd IP address out of that interface (therefore you must use source based routing for this to work). In other words, it allows control of which cards (usually 1) will respond to an ARP request.</em></p>
<p><em>arp_filter for the interface will be enabled if at least one of conf/{all,interface}/arp_filter is set to TRUE, it will be disabled otherwise.</em></p>
<p>Cumulus Linux uses the default Debian Linux arp_filter setting of <em>0</em>.</p>
<p>The <code>arp_filter</code> is primarily used when multiple interfaces reside in the same subnet and is used to allow/disallow which interfaces respond to ARP requests. In the case of <a href="/version/cumulus-linux-36/Layer_3/Open_Shortest_Path_First_-_OSPF_-_Protocol">OSPF</a> using IP unnumbered interfaces, many interfaces appear to be in the same subnet, and so actually contain the same address. If multiple interfaces are used between a pair of routers, having <code>arp_filter</code> set to 1 causes forwarding to fail.</p>
<p>The <code>arp_filter</code> parameter is set to allow a response on any interface in the subnet, where the <code>arp_ignore</code> setting (below) to limit cross-interface ARP behavior.</p></td>
</tr>
<tr class="even">
<td><p>arp_ignore</p></td>
<td><p>1</p></td>
<td><p>INT</p></td>
<td><p><em>Define different modes for sending replies in response to received ARP requests that resolve local target IP addresses:</em></p>
<p><em>0 - (default) Reply for any local target IP address, configured on any interface.</em></p>
<p><em>1 - Reply only if the target IP address is local address configured on the incoming interface.</em></p>
<p><em>2 - Reply only if the target IP address is local address configured on the incoming interface and both with the sender's IP address are part from same subnet on this interface.</em></p>
<p><em>3 - Do not reply for local addresses configured with scope host, only resolutions for global and link addresses are replied.</em></p>
<p><em>4-7 - Reserved</em></p>
<p><em>8 - Do not reply for all local addresses.</em></p>
<p>The maximum value from <em>conf/{all,interface}/arp_ignore</em> is used when the ARP request is received on the {interface}.</p>
<p>The default Debian <code>arp_ignore</code> parameter allows the device to reply to an ARP request for any IP address on any interface. While this matches the expectation that an IP address belongs to the device, not an interface, it can cause some unexpected and undesirable behavior on a router.</p>
<p>For example, if the <code>arp_ignore</code> parameter were set to <em>0</em> and an ARP request is received on one interface for the IP address residing on a different interface, the switch responds with an ARP reply even if the interface of the target address is down. This can cause a loss of traffic due to incorrect understanding about the reachability of next-hops, and also makes troubleshooting extremely challenging for some failure conditions.</p>
<p>In Cumulus Linux, the <code>arp_ignore</code> value is set to <em>1</em> so that it only replies to ARP requests on the interface that contains the target IP address. This acts much more like a traditional router and provides simplicity in troubleshooting and operation.</p></td>
</tr>
<tr class="odd">
<td><p>arp_notify</p></td>
<td><p>1</p></td>
<td><p>BOOL</p></td>
<td><p><em>Define mode for notification of address and device changes.</em></p>
<p><em>0 - (default) Do nothing.</em></p>
<p><em>1 - Generate gratuitous arp requests when device is brought up or hardware address changes.</em></p>
<p>The default Debian <code>arp_notify</code> setting is to remain silent when an interface is brought up or the hardware address is changed. Since Cumulus Linux often acts as a next-hop for many end hosts, it immediately notifies attached devices when an interface comes up or the address changes. This speeds up convergence on the new information and provides the most rapid support for changes.</p></td>
</tr>
</tbody>
</table>

## <span>Where Tunable ARP Parameter Changes Have Been Implemented in Cumulus Linux</span>

You can change the ARP parameter settings in several places, including:

  - `/proc/sys/net/ipv4/conf/all/arp*` (all interfaces)

  - `/proc/sys/net/ipv4/conf/default/arp*` (default for future
    interfaces)

  - `/proc/sys/net/ipv4/conf/swp*/arp*` (individual interfaces)

The ARP parameter changes in Cumulus Linux use the *default* file
locations.

The *all* and *default* locations sound similar, with the exception of
which interfaces are impacted, but they operate in significantly
different ways. The all location can **potentially** change the value
for **all** interfaces running IP, both now and in the future. The
reason for this uncertainty is that the *all* value is applied to each
parameter using either *MAX* or *OR* logic between the *all* and any
*port-specific* settings, as the following table shows:

| ARP Parameter | Condition |
| ------------- | --------- |
| arp\_accept   | OR        |
| arp\_announce | MAX       |
| arp\_filter   | OR        |
| arp\_ignore   | MAX       |
| arp\_notify   | MAX       |

For example, if the `/proc/sys/net/conf/all/arp_ignore` value is set to
*1* and the `/proc/sys/net/conf/swp1/arp_ignore` value is set to *0*, to
try to disable it on a per-port basis, interface swp1 still uses the
value of *1* in its operation. While it may appear that the
port-specific setting should override the global *all* setting, it does
not actually work that way. Instead, the MAX value between the *all*
value and port-specific value defines the actual behavior. This lack of
simplicity has led Cumulus Networks to implement the ARP parameter
changes using the *default* location instead.

The *default* location `/proc/sys/net/ipv4/conf/default/arp*` defines
the values for all future IP interfaces. Changing the *default* setting
of an ARP parameter does not impact interfaces that already contain an
IP address. If changes are being made to a running system that already
has IP addresses assigned to it, port-specific settings should be used
instead.

{{%notice note%}}

The way the *default* setting is implemented in Linux, the value of the
*default* parameter is copied to every port-specific location, excluding
those that already have an IP address assigned, as previously mentioned.
Therefore, there is not any complicated logic between the *default*
setting and the *port-specific* setting like there is when using the
*all* location. This makes the application of particular port-specific
policies much simpler and more deterministic.

{{%/notice%}}

To determine the current ARP parameter settings for each of the the
locations, use the following mechanism; other methods are available but
this one is quite simple:

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

Note that Cumulus Linux implements this change at boot time using the
`arp.conf` file at the following location:

    cumulus@switch:~$ cat /etc/sysctl.d/arp.conf
    net.ipv4.conf.default.arp_announce = 2
    net.ipv4.conf.default.arp_notify = 1
    net.ipv4.conf.default.arp_ignore=1
    cumulus@switch:~$

## <span id="src-8362442_AddressResolutionProtocol-ARP-port" class="confluence-anchor-link"></span><span>Changing Port-specific ARP Parameters</span>

The simplest way to configure port-specific ARP parameters in a running
device is with the following command:

    cumulus@switch:~$ sudo sh -c "echo 0 > /proc/sys/net/ipv4/conf/swp1/arp_ignore"
    cumulus@switch:~$ sudo grep . /proc/sys/net/ipv4/conf/swp1/arp* 
    /proc/sys/net/ipv4/conf/swp1/arp_accept:0
    /proc/sys/net/ipv4/conf/swp1/arp_announce:2
    /proc/sys/net/ipv4/conf/swp1/arp_filter:0
    /proc/sys/net/ipv4/conf/swp1/arp_ignore:0
    /proc/sys/net/ipv4/conf/swp1/arp_notify:1
    cumulus@switch:~$

To make the change persist through reboots, edit the
`/etc/sysctl.d/arp.conf` file and add your port-specific ARP setting.

## <span>Configuring Proxy ARP</span>

The proxy ARP setting is a kernel setting that you can manipulate using
`sysctl` or `sysfs`. Proxy ARP works with IPv4 only, since ARP is an
IPv4-only protocol.

You need to set `/proc/sys/net/ipv4/conf/<INTERFACE>/proxy_arp` to *1*:

    cumulus@switch:~$ net add interface swp1 post-up "echo 1 > /proc/sys/net/ipv4/conf/swp1/proxy_arp"
    cumulus@switch:~$ net pending
    cumulus@switch:~$ net commit

These commands create the following snippet in the
`/etc/network/interfaces` file:

    auto swp1
    iface swp1
        post-up echo 1 > /proc/sys/net/ipv4/conf/swp1/proxy_arp

If you're running two interfaces in the same broadcast domain, which is
typically seen when using
[VRR](/version/cumulus-linux-36/Layer_2/Virtual_Router_Redundancy_-_VRR/),
as it creates a "-v0" interface in the same broadcast domain, make sure
to use `sysctl` or `sysfs` to let the kernel know, so that both
interfaces do not respond with proxy ARP replies. To do so, set
`/proc/sys/net/ipv4/conf/<INTERFACE>/medium_id` to *2* on both the
interface and the -v0 interface. Continuing with the previous example:

    cumulus@switch:~$ net add interface swp1 post-up "echo 2 > /proc/sys/net/ipv4/conf/swp1/medium_id"
    cumulus@switch:~$ net add interface swp1-v0 post-up "echo 1 > /proc/sys/net/ipv4/conf/swp1-v0/proxy_arp"
    cumulus@switch:~$ net add interface swp1-v0 post-up "echo 2 > /proc/sys/net/ipv4/conf/swp1-v0/medium_id"
    cumulus@switch:~$ net pending
    cumulus@switch:~$ net commit

These commands create the following snippet in the
`/etc/network/interfaces` file:

    auto swp1
    iface swp1
        post-up echo 1 > /proc/sys/net/ipv4/conf/swp1/proxy_arp
        post-up echo 2 > /proc/sys/net/ipv4/conf/swp1/medium_id
     
    auto swp1-v0
    iface swp1-v0
        post-up echo 1 > /proc/sys/net/ipv4/conf/swp1-v0/proxy_arp
        post-up echo 2 > /proc/sys/net/ipv4/conf/swp1-v0/medium_id

If you're running proxy ARP on a VRR interface, add a post-up line to
the VRR interface stanza similar to the following. For example, if
vlan100 is the VRR interface for the configuration above:

    cumulus@switch:~$ net add vlan 100 post-up "echo 1 > /proc/sys/net/ipv4/conf/swp1/proxy_arp && echo 1 > /proc/sys/net/ipv4/conf/swp1-v0/proxy_arp && echo 2 > /proc/sys/net/ipv4/conf/swp1/medium_id && echo 2 > /proc/sys/net/ipv4/conf/swp1-v0/medium_id"
    cumulus@switch:~$ net pending
    cumulus@switch:~$ net commit
