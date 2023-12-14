---
title: NVIDIA User Experience (NVUE) Cheat Sheet
weight: 102
toc: 4
---

<span class="a-tooltip"> [NVUE](## "NVIDIA User Experience")</span> is an object-oriented, schema-driven model of a complete Cumulus Linux system providing a robust API that allows multiple interfaces to view and configure any element within a system.

You can use NVUE through its <span class="a-tooltip"> [CLI](## "Command Line Interface")</span> or <span class="a-tooltip"> [API](## "Application Programming Interface")</span>. Because NVUE is an object model, both CLI and REST API interfaces have equivalent functionality and can work in parallel while keeping all management operations consistent; for example, the CLI `show` commands reflect any `PATCH` operation you run through the REST API.  

NVUE follows a declarative model, removing context-specific commands and settings. It is structured as a big tree (like a filesystem path) representing the entire system state. At the base of the tree are high-level branches representing objects, such as router and interface. Under each branch, there are additional branches, and as you navigate through the tree, you gain a more specific context of the objects. The leaves of the tree are actual attributes, represented as key-value pairs.

This cheat sheet helps you get up to speed using [Cumulus Linux]({{<ref "/cumulus-linux-53">}}) and the [NVUE CLI]({{<ref "/cumulus-linux-53/System-Configuration/NVIDIA-User-Experience-NVUE/NVUE-CLI">}}).

{{%notice note%}}
This cheat sheet covers the most common and useful commands for certain Cumulus Linux elements, features, and protocols. Refer to the [Cumulus Linux User Guide]({{<ref "/cumulus-linux-53">}}) for more information, and additional and specific configurations.

For information about using the [NVUE REST API]({{<ref "/cumulus-linux-53/System-Configuration/NVIDIA-User-Experience-NVUE/NVUE-API">}}), refer to the [NVUE API documentation](https://docs.nvidia.com/networking-ethernet-software/cumulus-linux-53/api/index.html).
{{%/notice%}}

## NVUE CLI Command Syntax

All NVUE commands begin with `nv` and fall into one of four syntax categories:

- Configuration (`nv set` and `nv unset`)
- Monitoring (`nv show`)
- Configuration management (`nv config`)
- Action (`nv action`)

Like all industry-standard CLIs, the NVUE CLI includes command completion with the TAB key, use of the question mark (`?`) to display command information, and command abbreviation to speed up CLI interaction. In addition, you can get help with command syntax by using the `-h` or `--help` option, and list all commands by running `nv list-commands`.

## Getting Started

After you rack and power on your NVIDIA Spectrum switch with Cumulus Linux, connect a serial console cable so that you can begin configuration. All switches are manufactured with an RJ45 serial port for console connectivity and set to 115200 baud rate. If your switch does not have a pre-installed <span class="a-tooltip"> [NOS](## "Network Operating System")</span>, you can [install a new Cumulus Linux image]({{<ref "/cumulus-linux-53/Installation-Management/Installing-a-New-Cumulus-Linux-Image">}}).

## System Management and Services

Use the following commands to configure the management network and system services on the switch.

| <div style="width:220px">Command Syntax | Description and Example |
| -------------| ----------------------- |
| `nv set system hostname <name>` | Configures the system hostname. The default hostname is `cumulus`.<pre>$ nv set system hostname leaf01</pre>|
| `nv set interface eth0 ip address <ip-address/mask>`</br></br>`nv set interface eth0 ip gateway <ip-address>` |Configures a static IP address and default gateway on the <span class="a-tooltip">[OOB](## "Out of Band")</span> management interface (eth0). By default the OOB management interface is set to use DHCPv4 to obtain an IP address.<pre>$ nv set interface eth0 ip address 192.168.200.2/24</br>$ nv set interface eth0 ip gateway 192.168.200.1</pre> |
| `nv set service ntp <vrf-name> server <url> iburst on` | Adds an <span class="a-tooltip"><a><abbr title="Network Time Protocol">NTP</abbr></a></span> server. Cumulus Linux boots with the NTP service enabled and uses default servers. Refer to the <a href="/cumulus-linux-53/System-Configuration/Date-and-Time/Network-Time-Protocol-NTP">NTP</a> documentation for more information.</br>The <span class="a-tooltip"><a><abbr title="Virtual Routing and Forwarding">VRF</abbr></a></span> name in the example is `default`. You must specify a VRF.<pre>$ nv set service ntp default server 4.cumulusnetworks.pool.ntp.org iburst on</pre></br>If you do not use NTP, set the system time and date with the Linux `date` command. |
| `nv set system timezone <timezone>` | Configures the system time zone. By default, Cumulus Linux uses the <span class="a-tooltip">[UTC](## "Coordinated Universal Time")</span> time zone.<pre>$ nv set system timezone US/Eastern</pre> |
| `nv set service dns <vrf-name> server <ip-address)` | Configures the <span class="a-tooltip"><a><abbr title="Domain Name System">DNS</abbr></a></span> lookup server. The VRF name in the example is `mgmt`. You can use this command with or without the VRF.<pre>$ nv set service dns mgmt server 198.51.100.31</pre> |
| `nv set service syslog <vrf-name> server <ip-address> port <port>`</br></br>`nv set service syslog <vrf-name> server <ip-address> protocol <protocol>` | Configures a remote Syslog server for the switch to send syslog messages. The VRF name in the example is `default`. You must specify a VRF.</br>You can specify `udp` or `tcp` for the protocol.<pre>$ nv set service syslog default server 192.168.0.254 port 514</br>$ nv set service syslog default server 192.168.0.254 protocol udp</pre> |

## Working with Interfaces

Use the following commands to configure the physical, breakout, loopback, and logical layer 2 and layer 3 interfaces.

### Physical Interfaces

| <div style="width:250px">Command Syntax | Description and Example |
| -------------| ----------------------- |
| `nv set interface <interface>`</br>`nv set interface <interface-range>`| Administratively enables physical interfaces on the switch.</br>All physical interfaces except eth0 are disabled by default; you must enable them for them to become operational.</br>To disable an interface, use the `nv unset` command.</br>You can also enable or disable all or a range of interfaces at the same time. <pre>$ nv set interface swp1</br>$ nv set interface swp1,20-32</pre>|
| `nv set interface <interface> link state <state>` | Configures the interface link state: `up` or `down`. After you enable an interface, the link state is set automatically to `up`.</br><b>Note:</b> Setting the link state to `down` does not disable the interface from the system like the `nv unset interface <interface>` command. <pre>$ nv set interface swp1 link state down</br>$ nv set interface swp8-15 link state up</pre>|
| `nv set interface <interface> link speed <speed>` | Configures the interface speed. If auto-negotiation is enabled (the default setting), it takes precedence over the link speed setting.<pre>$ nv set interface swp1 link speed 50G</pre>|
| `nv set interface <interface> link mtu <mtu>` | Configures the interface <span class="a-tooltip"><a><abbr title="Maximum Transfer Unit">MTU</abbr></a></span>. All interfaces in Cumulus Linux are set to 9216B MTU by default.<pre>$ nv set interface swp1 link mtu 1500</pre>|

### Breakout Interfaces

To increase the number of ports on the NVIDIA Spectrum switch, you can break out physical interfaces into two or four lower speed ports.</br>Breakout configurations differ between platforms, refer to the <a href="/cumulus-linux-53/Layer-1-and-Switch-Ports/Interface-Configuration-and-Management/Switch-Port-Attributes#breakout-ports">breakout ports</a> section of the <a href="/cumulus-linux-53/Layer-1-and-Switch-Ports/Interface-Configuration-and-Management/Switch-Port-Attributes">switch port attributes</a> documentation for more information.</br>

| <div style="width:250px">Command Syntax | Description and Example |
| -------------| ----------------------- |
| `nv set interface <interface> link breakout <breakout-mode>`</br></br>`nv set interface <interface> link breakout disabled` | Configures the breakout mode on a physical interface.</br>Some platforms require you to disable the adjacent port to break out an interface. Refer to this <a href="/knowledge-base/Setup-and-Getting-Started/layer-1-Data-Center-Cheat-Sheet#breakout-ports-configuration">knowledge base article</a> for more information.<pre>$ nv set interface swp1 link breakout 4x25G</br>$ nv set interface swp2 link breakout disabled</pre> |
| `nv unset interface <breakout-interface>`</br></br>`nv unset interface <interface> link breakout` | Administratively disables the breakout port from the system. When you break out a physical port, Cumulus Linux creates new logical ports in the system; for example, when you break out interface swp1 into four new ports, Cumulus Linux creates swp1s0, swp1s1, swp1s2, and swp1s3. To remove the breakout configuration from an interface, you must administratively disable all the breakout ports and then `unset` the breakout configuration from the physical interface.<pre>$ nv unset interface swp1s0</br>$ nv unset interface swp1s1</br>$ nv unset interface swp1s2</br>$ nv unset interface swp1s3</br>$ nv unset interface swp1 link breakout</pre>|

### Loopback Interface

Cumulus Linux has a preconfigured loopback interface. When the switch boots up, the loopback interface, called `lo`, is `up` and assigned an IP address of `127.0.0.1`.

| <div style="width:250px">Command Syntax | Description and Example |
| -------------| ----------------------- |
| `nv set interface lo ip address <ip-address>` | Configures an IP address on the loopback interface (lo). The loopback interface <b>must</b> always exist and be `up`. `lo` does not require a subnet mask; it is automaticaly set with a `/32` prefix. You can configure multiple IP addresses for the loopback interface.<pre>$ nv set interface lo ip address 10.10.10.1</pre>|

### Layer 2 Interfaces

After you enable a physical interface in Cumulus Linux, the interface is routed (layer 3). To set an interface as a switch port (layer 2), you must add it to a bridge.

#### Bridge and VLANs

Cumulus Linux supports two bridge configuration modes:
- VLAN-aware bridge
- Traditional bridge

The default bridge `br_default` is a VLAN-aware bridge. Refer to the [Ethernet Bridging - VLANs]({{<ref "/cumulus-linux-53/Layer-2/Ethernet-Bridging-VLANs">}}) documentation for more information.

| <div style="width:200px">Command Syntax | Description and Example |
| -------------| ----------------------- |
| `nv set interface <interface> bridge domain br_default` | Adds a physical interface into the default `br_default` bridge. You can add a range of interfaces to a bridge.</br>When you add an interface to a bridge, Cumulus Linux sets the interface automatically to trunk mode (tagged-dot1Q) with all bridge VLANs allowed.<pre>$ nv set interface swp1 bridge domain br_default</br>$ nv set interface swp1-5,7-22 bridge domain br_default</pre>|
| `nv set interface <interface> bridge domain br_default untagged none` | Configures an interface (<b>not the bridge</b>) to drop all untagged traffic. The `untagged none` command removes the <span class="a-tooltip"><a><abbr title="Primary VLAN Identifier">PVID</abbr></a></span> from the interface.<pre>$ nv set interface swp2 bridge domain br_default untagged none</pre> |
| `nv set bridge domain br_default vlan <vlan-id>` | Configures VLANs on the default bridge (`br_default`). All new VLANs you add to the bridge are automatically added to all its trunk ports. You can also add VLANs in a range or a list.<pre>$ nv set bridge domain br_default vlan 10,20</pre>|
| `nv set interface <interface> bridge domain br_default access <vlan-id>` | Configures an interface as an access (untagged) port in a specific VLAN.<pre>$ nv set interface swp1 bridge domain br_default access 10</pre>|
| `nv set bridge domain br_default untagged <vlan-id>` | Configures the PVID of the default `br_default` bridge. The default PVID is 1. Use this command only to change (or reset) the default PVID.<pre>$ nv set bridge domain br_default untagged 100</pre>|

#### Spanning-Tree Protocol (STP)

The VLAN-aware bridge (`br_default`) operates only in <span class="a-tooltip"><a><abbr title="Rapid Spanning-Tree Protocol">RSTP</abbr></a></span> mode.
{{%notice note%}}
Traditional bridges operate in both <span class="a-tooltip"><a><abbr title="Per-VLAN Spanning-Tree">PVST</abbr></a></span> and <span class="a-tooltip"><a><abbr title="Rapid Per-VLAN Spanning-Tree">RPVST</abbr></a></span> mode. The default mode is PVRST. Each traditional bridge has its own separate STP instance.
{{%/notice%}}

| <div style="width:230px">Command Syntax | Description and Example |
| -------------| ----------------------- |
| `nv set bridge domain br_default stp priority <priority>` | Sets the spanning-tree priority of the default bridge (`br_default`). The default STP priority is 32768.<pre>$ nv set bridge domain br_default stp priority 8192</pre> |
| `nv set interface <interface> bridge domain br_default stp admin-edge on`</br></br>`nv set interface <interface> bridge domain br_default stp bpdu-guard on`</br></br>`nv set interface <interface> bridge domain br_default stp auto-edge on` | Sets an interface to Edge (PortFast) mode. NVIDIA recommends you set <span class="a-tooltip"><a><abbr title="Bridge Protocol Data Unit">BPDU</abbr></a></span>-guard on edge ports to eliminate loops.</br>Cumulus Linux enables automatic edge `auto-edge` port detection by default. You can disable `auto-edge` with the `off` option.<pre>$ nv set interface swp5 bridge domain br_default stp admin-edge on</br>$ nv set interface swp5 bridge domain br_default stp bpdu-guard on</br>$ nv set interface swp5 bridge domain br_default stp auto-edge off</pre>|

Refer to the [Spanning Tree and Rapid Spanning Tree - STP]({{<ref "/cumulus-linux-53/Layer-2/Spanning-Tree-and-Rapid-Spanning-Tree">}}) documentation for more information.

### Layer 3 Interfaces

After you enable a Cumulus Linux interface administratively, it is a routed port (layer 3).

| <div style="width:250px">Command Syntax | Description and Example |
| -------------| ----------------------- |
| `nv set interface <interface> ip address <ip-address>` | Configures an IPv4 or IPv6 address on the physical interface (swp).<pre>$ nv set interface swp10 ip address 10.1.0.5/24</br>$ nv set interface swp10 ip address 2001:db8::10/64</pre>|
| `nv set interface <svi> ip address <ip-address>` | Configures an IPv4 or IPv6 address on an <span class="a-tooltip"><a><abbr title="Switch Virtual Interface">SVI</abbr></a></span> (VLAN interface).</br>The SVI operates only if its VLAN exists and an interface is assigned to it (either tagged or untagged).<pre>$ nv set interface vlan100 ip address 100.1.0.2/24</br>$ nv set interface vlan100 ip address 2001:db8::1/32</pre>|

### Link Aggregation Interfaces

The Link Aggregation (LAG) interface in Cumulus Linux is called a bond. You can configure a bond as a layer 2 or layer 3 interface.

| <div style="width:250px">Command Syntax | Description and Example |
| -------------| ----------------------- |
| `nv set interface <bond-name> bond member <bonded-interface>`</br></br>`nv set interface <bond-name> type bond` | Configures a bond interface and sets the physical ports. If you use a bond name that starts with `bond`, the type is automatically set to `bond`. Otherwise, you have to manually set the interface type to `bond`.<pre>$ nv set interface bond1 bond members swp1-4</br>$ nv set interface lag1 bond members swp5-6</br>$ nv set interface lag1 type bond</pre>|
| `nv set interface <bond-name> bond mode <mode>`| Configures the bond interface operation mode.</br>By default, bonds in Cumulus Linux are set to <span class="a-tooltip"><a><abbr title="Link Aggregation Control Protocol">LACP</abbr></a></span> (802.3ad) mode.</br>You can change the mode to Balance-xor with the `static` option. To reset the bond mode to LACP, use the `lacp` option.<pre>$ nv set interface bond1 bond mode static</br>$ nv set interface bond1 bond mode lacp</pre>|
|`nv set interface <bond-name> bond lacp-rate <rate>` | Configures the bond interface LACP <span class="a-tooltip"><a><abbr title="Protocol Data Unit">PDU</abbr></a></span> transmit rate.</br>By default, bonds in Cumulus Linux are set to `fast` mode (transmitting every 3 seconds). To set the rate to 30 seconds, use `slow` mode.<pre>$ nv set interface bond1 bond lacp-rate slow</br>$ nv set interface bond1 bond lacp-rate fast</pre>|

## Working with Network Protocols

This cheat sheet includes some of the basic commands to configure the main data center protocols. To configure other protocols, see additional configuration commands, examples, and more detailed information, refer to the [Cumulus Linux User Guide]({{<ref "/cumulus-linux-53">}}).

### Layer 2 Protocols

#### Multi-Chassis Link Aggregation - MLAG

MLAG provides layer 2 redundancy and greater system throughput. To configure MLAG, you must fulfill these requirements:

- Only two switches can share MLAG configuration. However, you can have multiple (different) MLAG pairs in the network.
- Both MLAG peer switches must be directly connected. This is typically a bond for increased reliability and bandwidth.
- Both switches in the MLAG pair must be of the same Spectrum model and run the same Cumulus Linux version.
- The dual-connected devices (servers or switches) can use LACP or static bond modes. MLAG switches must be set accordingly.

This cheat sheet includes the basic MLAG configuration commands. Refer to the [Multi-Chassis Link Aggregation - MLAG]({{<ref "/cumulus-linux-53/Layer-2/Multi-Chassis-Link-Aggregation-MLAG">}}) documentation for more information.

| <div style="width:250px">Command Syntax | Description and Example |
| -------------| ----------------------- |
| `nv set interface <bond-name> bond member <bonded-interface>` | Configures a bond interface and sets its physical ports. You must create a bond interface so that it is set as an MLAG port.<pre>$ nv set interface bond1 bond members swp1</pre>|
| `nv set interface <bond-name> bond mlag id <mlag-id>` | Sets the MLAG ID of the bond interface. You must specify a unique MLAG ID for every dual-connected bond on each peer switch. The value must be identical on both MLAG peers.<pre>$ nv set interface bond1 bond mlag id 1</pre>|
| `nv set interface <bond-name> bridge domain br_default` | Sets the MLAG port into the default bridge `br_default`.<pre>$ nv set interface bond1 bridge domain br_default</pre>|
| `nv set interface peerlink bond member bonded-interface>` |Configures the inter-chassis bond for MLAG operation. `peerlink` is a reserved name for the inter-chassis link. When you create the peer link, Cumulus Linux creates a layer 3 sub-interface called `peerlink.4094` automatically to ensure VLAN-independent operation on this link.<pre>$ nv set interface peerlink bond member swp31-32</pre>|
| `nv set mlag mac-address <address>` | Configures the MLAG system MAC address, which is set in the PDU for all control protocols to represent the MLAG pair as a single switch. The MLAG MAC address must be identical on both MLAG peers but unique in the network and different between MLAG pairs (Cumulus Linux provides a special reserved range).<pre>$ nv set mlag mac-address 44:38:39:BE:EF:AA</pre>|
| `nv set mlag peer-ip linklocal` | Configures the MLAG peer IP address. The peer IP address is based on the `peerlink.4094` link-local addresses (point-to-point).<pre>$ nv set mlag peer-ip linklocal</pre>|
| `nv set mlag backup <ip-address>`| Configures the MLAG backup IP address, which is used to communicate between MLAG peers in case the peer link goes down.<pre>nv set mlag backup 10.10.10.2</pre>You can specify the backup IP in a specific VRF if needed.<pre>$ nv set mlag backup 10.10.10.2 vrf mgmt</pre>|

#### Virtual Router Redundancy - VRR

<span class="a-tooltip"> [VRR](## "Virtual Router Redundancy")</span> enables an active-active gateway for the layer 2 MLAG domain. Both MLAG peers must have an SVI with unique IP addresses for each VLAN. Then, you must set identical VRR instances (one instance per subnet) on both MLAG peers. The VRR instance is configured on the SVIs and holds the virtual IP and MAC addresses. Both peers respond to ARP requests from the host but if one fails, the second still serves as the gateway.

| <div style="width:250px">Command Syntax | Description and Example |
| -------------| ----------------------- |
| `nv set interface <svi> ip vrr address <ip-address>` | Configures the virtual IP address of the VRR instance. This address must be within the SVI subnet.<pre>$ nv set interface vlan10 ip vrr address 10.1.10.1/24</pre>|
| `nv set system global fabric-mac <mac-address>`</br></br>`nv set system global fabric-id <id>`| Configures the global fabric MAC address to ensure fabric-wide MAC consistency across VRR switches. The MAC address is used primarily for multi-fabric EVPN environments. Cumulus Linux uses the default VRR MAC address 00:00:5E:00:01:01; you can either change this MAC address globally or change the default fabric ID (`fabric_id=1`), which is added to the MAC address.<pre>$ nv set system global fabric-mac 00:00:5E:00:01:FF</br>$ nv set system global fabric-id 255</pre>|
| `nv set interface <svi> ip vrr mac-address <mac-address>` | Configures the VRR instance virtual MAC address for a specific VLAN (in case you want to override the global default settings).<pre>$ nv set interface vlan10 ip vrr mac-address 00:00:5E:00:01:00</pre>|

Refer to the [Virtual Router Redundancy - VRR and VRRP]({{<ref "/cumulus-linux-53/Layer-2/Virtual-Router-Redundancy-VRR-and-VRRP">}}) documentation for more information.

### Layer 3 Protocols

#### Virtual Routing and Forwarding - VRF

<span class="a-tooltip"> [VRF](## "Virtual Routing and Forwarding")</span> (also called VRF-Lite) enables you to use multiple independent routing tables that work simultaneously on the same switch. VRFs are useful in multi-tenant environments.

This cheat sheet includes basic VRF commands. For more information about using custom and `mgmt` VRFs with different protocols, refer to the [Virtual Routing and Forwarding - VRF]({{<ref "/cumulus-linux-53/Layer-3/VRFs/Virtual-Routing-and-Forwarding-VRF">}}) and [Management VRF]({{<ref "/cumulus-linux-53/Layer-3/VRFs/Management-VRF">}}) documentation.

| <div style="width:250px">Command Syntax | Description and Example |
| -------------| ----------------------- |
|`nv set vrf <vrf-name> table <id>` | Configures a new VRF and assigns a table ID. You can use the `auto` table assignment or set the ID manually (the ID must be between 1001-1255).<pre>$ nv set vrf BLUE table auto</br>$ nv set vrf RED table 1016</pre>|
| `nv set interface <interface> ip vrf <vrf-name>` |Adds a layer 3 interface into a VRF.<pre>$ nv set interface swp1 ip vrf BLUE</pre>|

#### Static Routing

You can use static routing if you do not require the complexity of a dynamic routing protocol (such as BGP or OSPF), if you have routes that do not change frequently and for which the destination is only one or two paths away.

| Command Syntax | Description and Example |
| -------------| ----------------------- |
| `nv set vrf <vrf-name> router static <ip-address> via <ip-address>` | Configures a static route to a destination network through a specified next hop within a VRF. You must have a local IP address within the next hop subnet.<pre>$ nv set vrf default router static 10.10.10.101/32 via 10.0.1.1</pre>|

#### Border Gateway Protocol - BGP

<span class="a-tooltip"> [BGP](## "Border Gateway Protocol")</span> is the routing protocol that runs the Internet. BGP manages how packets get routed from network to network by exchanging routing and reachability information.

Cumulus Linux makes BGP configuration in the data center easier with [Auto BGP]({{<ref "/cumulus-linux-53/Layer-3/Border-Gateway-Protocol-BGP#auto-bgp">}}) and
[BGP Unnumbered]({{<ref "/cumulus-linux-53/Layer-3/Border-Gateway-Protocol-BGP#bgp-unnumbered">}}). NVIDIA recommends using these features to eliminate the need for <span class="a-tooltip"> [ASN](## "Autonomous System Number")</span> and point-to-point IP addressing assignments, and to reduce human errors.

This cheat sheet includes basic BGP configuration commands. Refer to the [Border Gateway Protocol - BGP]({{<ref "/cumulus-linux-53/Layer-3/Border-Gateway-Protocol-BGP">}}) documentation for more information.

| <div style="width:250px">Command Syntax | Description and Example |
| -------------| ----------------------- |
| `nv set router bgp autonomous-system <asn>` | Configures BGP with an ASN. You can use the auto BGP `leaf` or `spine` keywords to let Cumulus Linux set the ASN automatically, or set a number manually.<pre>$ nv set router bgp autonomous-system 65101</br>$ nv set router bgp autonomous-system leaf</pre>|
| `nv set router bgp router-id <ip-address>`</br></br>`nv set vrf <vrf-name> router bgp router-id <ip-address>`| Configures the BGP router ID. By default, BGP assigns the loopback IP address as the router ID. If you do not have a loopback set or you want to override this setting, you need to set it manually. You can set the router ID globally or per VRF.<pre>$ nv set router bgp router-id 10.10.10.1</br>$ nv set vrf RED router bgp router-id 10.10.10.1</pre>|
| `nv set vrf <vrf-name> router bgp neighbor <neighbor> remote-as <remote-as>`| Configures BGP neighbor peering. You can set the neighbor as `internal` for iBGP or `external` for eBGP. The default VRF name is `default`. You must set the neighbors in this VRF.<pre>$ nv set vrf default router bgp neighbor 10.0.1.1 remote-as internal</br>$ nv set vrf default router bgp neighbor swp2 remote-as external</br>$ nv set vrf default router bgp neighbor 2001:db8:0002::0a00:0002 remote-as external</pre>|
| `nv set vrf <vrf-name> router bgp neighbor <neighbor> address-family ipv6-unicast enable on`|Enables IPv6 prefix advertisement. Cumulus Linux enables the IPv4 address family by default. To advertise IPv6 routes, you need to enable the IPv6 address family. To advertise IPv4 prefixes with IPv6 next hops, see <a href="/cumulus-linux-53/Layer-3/Border-Gateway-Protocol-BGP/Optional-BGP-Configuration#advertise-ipv4-prefixes-with-ipv6-next-hops">Advertise IPv4 Prefixes with IPv6 Next Hops</a>.<pre>$ nv set vrf default router bgp neighbor 2001:db8:0002::0a00:0002 address-family ipv6-unicast enable on</pre>|
| `nv set vrf <vrf-name> router bgp address-family <address-family> network <prefix>`|Specifies which prefixes to originate.<pre>$ nv set vrf default router bgp address-family ipv4-unicast network 10.1.10.0/24</br>$ nv set vrf default router bgp address-family ipv6-unicast network 2001:db8::1/128</pre>|
|`nv set vrf <vrf-name> router bgp address-family <address-family> redistribute <value> enable on` | Redistributes prefixes into the IPv4 or IPv6 address family. You can specify `connected`, `static`, or `ospf`. You can also use route redistribution with route maps and the BGP metric options. See <a href="/cumulus-linux-53/Layer-3/Routing/Route-Filtering-and-Redistribution">Route Filtering and Redistribution</a> for more information.<pre>$ nv set vrf default router bgp address-family ipv4-unicast redistribute static enable on</br>$ nv set vrf default router bgp address-family ipv6-unicast redistribute connected route-map routemap1</pre>|

### Network Virtualization

<span class="a-tooltip"> [VXLAN](## "Virtual Extensible LAN")</span> is a standard overlay protocol for logical virtual networks. It uses a VLAN-like encapsulation technique to encapsulate layer 2 Ethernet segments over layer 3 networks. The encapsulation happens on the  <span class="a-tooltip"> [VTEP](## "VXLAN Tunnel End Points")</span>, which establishes an overlay UDP tunnel to the remote VTEP device. Unlike VLANs, VXLAN scales to 16 million segments (a 24-bit VXLAN network identifier (VNI ID) in the VXLAN header) for multi-tenancy. Refer to the [Network Virtualization]({{<ref "/cumulus-linux-53/Network-Virtualization">}}) documentation for more information.

#### VXLAN Devices and Static Tunnels

Cumulus Linux supports single and traditional VXLAN devices. NVUE allows you to work only with a single VXLAN device (single VTEP) in a VLAN-aware bridge. With a single VXLAN device (<span class="a-tooltip">[NVE](## "Network Virtual Interface")</span> interface), you specify the VLAN to <span class="a-tooltip"> [VNI](## "Virtual Network Identifier")</span> mapping. 

{{%notice note %}}
Cumulus Linux supports multiple single VXLAN devices when set with multiple VLAN-aware bridges. Make sure not to duplicate VNIs across devices.
{{%/notice %}}

This cheat sheet includes some of the basic configuration commands for static VXLAN tunnels. For more information and for additional configuration, refer to the [Network Virtualization]({{<ref "/cumulus-linux-53/Network-Virtualization">}}) documentation.

| <div style="width:250px">Command Syntax | Description and Example |
| -------------| ----------------------- |
| `nv set bridge domain br_default vlan <vlan-id> vni <vni-id>`| Maps the VLAN to the VNI, and creates and adds the VXLAN device (NVE) to the bridge. The single VXLAN device name in Cumulus Linux is `vxlan48`.<pre>$ nv set bridge domain br_default vlan 10 vni 10</pre>|
| `nv set bridge domain br_default vlan <vlan-id> vni auto` |Automatically maps the VLAN to the VNI to simplify configuration. You can also configure auto VNI mapping on a VLAN range or list. Automatic VLAN to VNI mapping works only on EVPN fabrics.<pre>$ nv set bridge domain br_default vlan 10,20,30,40,50 vni auto</pre>|
| `nv set bridge domain br_default vlan-vni-offset <value>` | Automatically maps the VLAN to the VNI with a value offset.<pre>$ nv set bridge domain br_default vlan-vni-offset 10000</pre>|
| `nv set nve vxlan mac-learning on` | Enables MAC learning on the NVE device. You must set this command for non-EVPN fabrics. You can set MAC learning globally for all VNIs or per VNI (using the bridge command).<pre>$ nv set nve vxlan mac-learning on</br>$ nv set bridge domain br_default vlan 10 vni 10 mac-learning on</pre>|
| `nv set nve vxlan arp-nd-suppress on` | Enables the NVE to reply to local ARP requests if it has the remote MAC already. This prevents unnecessary broadcast traffic to all remote VTEPs.<pre>$ nv set nve vxlan arp-nd-suppress on</pre>|
| `nv set nve vxlan source address <ip-address>` | Configures the VTEP (NVE) source IP address to form the overlay tunnel. Cumulus Linux uses the loopback IP address for the tunnel source. <pre>$ nv set nve vxlan source address 10.10.10.1</pre>|
| `nv set nve vxlan mlag shared-address <ip-address>`| Configures the MLAG anycast virtual IP address as the VXLAN tunnel destination. Both MLAG peers must have the same address.<pre>$ nv set nve vxlan mlag shared-address 10.0.1.34</pre>|
| `nv set bridge domain br_default vlan <vlan-id> vni <vni-id> flooding head-end-replication <ip-address>`</br></br>`nv set nve vxlan flooding head-end-replication <ip-address>` | Configures the remote VTEPs for <span class="a-tooltip"><a><abbr title="Head End Replication">HER</abbr></a></span> to handle <span class="a-tooltip"><a><abbr title="Broadcast, Unknown-Unicast and Multicast">BUM</abbr></a></span> traffic. You must configure the remote VTEPs in non-EVPN fabrics. You can set the remote VTEP per VNI or globally for all VNIs.<pre>$ nv set bridge domain br_default vlan 10 vni 10 flooding head-end-replication 10.10.10.2</br>$ nv set nve vxlan flooding head-end-replication 10.10.10.2</pre>|
|`nv set bridge domain br_default vlan <vlan-id> vni <vni-id> flooding multicast-group <ip-address>`<br></br>`nv set nve vxlan flooding multicast-group <ip-address>` | Configures the multicast group for BUM traffic handling for EVPN fabrics (HER is the default). You can set the flooding group per VNI or globally. NVIDIA recommends setting a unique multicast group per VNI. This configuration requires using PIM-SM on the underlay network.</br>Refer to <a href="/cumulus-linux-53/Network-Virtualization/Ethernet-Virtual-Private-Network-EVPN/EVPN-PIM">EVPN BUM Traffic with PIM-SM</a> for more information.<pre>$ nv set bridge domain br_default vlan 10 vni 10 flooding multicast-group 239.1.1.110</br>$ nv set nve vxlan flooding multicast-group 224.0.0.10</pre>|

#### Ethernet Virtual Private Network - EVPN

<span class="a-tooltip"> [EVPN](## "Ethernet Virtual Private Network")</span> is a standards-based control plane that relies on multi-protocol BGP (MP-BGP) and allows for building and deploying VXLANs at scale. EVPN enables intra-subnet bridging and inter-subnet routing, including multi-tenancy support. 

This cheat sheet includes the basic EVPN configuration commands. For more information and additional configuration, refer to the [Ethernet Virtual Private Network - EVPN]({{<ref "/cumulus-linux-53/Network-Virtualization/Ethernet-Virtual-Private-Network-EVPN">}}) documentation.

| <div style="width:250px">Command Syntax | Description and Example |
| -------------| ----------------------- |
| `nv set evpn enable on` | Enables EVPN capabilities globally on the switch. You do not have to enable EVPN per VRF, it is set automatically.<pre>$ nv set evpn enable on</pre>|
| `nv set vrf <vrf-name> router bgp neighbor <neighbor> address-family l2vpn-evpn enable on` | Activates the EVPN address family between BGP neighbors. You need to set the EVPN neighbors in the `default` VRF.<pre>$ nv set vrf default router bgp neighbor swp51 address-family l2vpn-evpn enable on</pre>|
| `nv set evpn route-advertise default-gateway on` | Enables default gateway advertisement into EVPN when using EVPN <a href="/cumulus-linux-53/Network-Virtualization/Ethernet-Virtual-Private-Network-EVPN/Inter-subnet-Routing#centralized-routing">Centralized Routing</a>. You can set this per VNI, but NVIDIA recommends setting it globally.<pre>$ nv set evpn route-advertise default-gateway on</pre> |
| `nv set vrf <vrf-name> evpn vni <vni-id>` | Creates the layer 3 VNI for a tenant VRF when using EVPN <a href="/cumulus-linux-53/Network-Virtualization/Ethernet-Virtual-Private-Network-EVPN/Inter-subnet-Routing#symmetric-routing">Symmetric Routing</a>. First, make sure to create the tenant VRF and add an SVI to it.<pre>$ nv set vrf RED vni 4001</pre>|
| `nv set vrf <vrf-name> router bgp address-family ipv4-unicast route-export to-evpn enable on` | Enables the switch to install EVPN type-5 routes from the VRF BGP RIB. First, make sure to create the tenant VRF and set the layer 3 VNI to it.<pre>$ nv set vrf RED router bgp address-family ipv4-unicast route-export to-evpn enable on</pre>|
| `nv set evpn multihoming enable on`| Enables <a href="/cumulus-linux-53/Network-Virtualization/Ethernet-Virtual-Private-Network-EVPN/EVPN-Multihoming">EVPN Multihoming</a> (EVPN-MH) on the switch.<pre>$ nv set evpn multihoming enable on</pre>|
| `nv set interface <bond-name> evpn multihoming segment local-id <id>` | Configures the EVPN-MH <span class="a-tooltip"><a><abbr title="Ethernet Segment Identifier">ESI</abbr></a></span> on the bond interface. Each <span class="a-tooltip"><a><abbr title="Ethernet Segment">ES</abbr></a></span> must have the same ESI accross the fabric. You must set a unique ESI per bond interface on the switch.<pre>$ nv set interface bond2 evpn multihoming segment local-id 2</pre>|
| `nv set interface <bond-name> evpn multihoming segment mac-address <mac-address>` | Configures the EVPN-MH ES MAC address per bond interface. The ES MAC and the ESI generates a unique EVPN type-3 route. The ES MAC must be the same on all interfaces toward the same server.<pre>$ nv set interface bond1 evpn multihoming segment mac-address 44:38:39:BE:EF:AA</pre>|
| `nv set interface <bond-name> evpn multihoming segment df-preference <value>` | Configures the EVPN-MH ES <span class="a-tooltip"><a><abbr title="Designated Frowarder">DF</abbr></a></span>. The DF handles flooded traffic received through the VXLAN tunnels to the local ES. The default DF value is 32767. NVIDIA recommends setting the DF preference to avoid unpredictable failure scenarios.<pre>$ nv set interface bond1 evpn multihoming segment df-preference 50000</pre>|
| `nv set interface <interface> evpn multihoming uplink on` | Configures the EVPN-MH uplink ports. When all ES uplink ports go down, all bonds enter an error-disabled state to prevent active MH bonds without VXLAN overlay tunnels.<pre>$ nv set interface swp51-54 evpn multihoming uplink on</pre>|

The [Configuration Examples]({{<ref "/cumulus-linux-53/Network-Virtualization/Ethernet-Virtual-Private-Network-EVPN/Configuration-Examples">}}) section of the Cumulus Linux user guide provides examples of EVPN layer 2 routing, centralized routing, symmetric routing, and [EVPN-MH]({{<ref "/cumulus-linux-53/Network-Virtualization/Ethernet-Virtual-Private-Network-EVPN/EVPN-Multihoming#configuration-example">}}).

You can also examine and try the EVPN best practices using these pre-built simulations in [Air Marketplace](https://air.nvidia.com/marketplace):
- [EVPN L2 Extension](https://air.nvidia.com/marketplace?demo_id=18e96902-48a0-4bf9-9cf7-23852fbe72c5) 
- [EVPN Centralized Routing](https://air.nvidia.com/marketplace?demo_id=4a7f8342-9efa-446b-a58d-11c2c8bc94dc)
- [EVPN Symmetric Routing](https://air.nvidia.com/marketplace?demo_id=d2b854ae-12ed-4a9a-82b5-49863d3fb37c)
- [EVPN Multihoming](https://air.nvidia.com/marketplace?demo_id=f12bb2ac-55ef-4b61-a6fa-10613d9dbbd2)

## Access Control List - ACL

<span class="a-tooltip"> [ACLs](## "Access Control Lists")</span> in Cumulus Linux are based on Linux <em>iptables</em> and <em>ebtables</em> with the following default behaviors:

- There is no <em>implicit deny</em>. ACLs must end in a `match any` and `action deny` rule to drop all unmatched traffic.
- There is no support for wildcard masks. You must list subnets individually.

{{%notice note%}}
In addition to NVUE commands, you can configure ACLs by setting <em>ebtable</em> and <em>iptable</em> rules. You can also use the built-in ACL management tool `cl-acltool`. For more information, refer to the [Netfilter - ACLs]({{<ref "/cumulus-linux-53/System-Configuration/Netfilter-ACLs">}}) documentation.
{{%/notice%}}

| <div style="width:250px">Command Syntax | Description and Example |
| -------------| ----------------------- |
| `nv set acl <acl-name> type <type>`| Creates an IPv4, IPv6, or MAC access list. You must set the ACL type.<pre>$ nv set acl DENY_TCP_HTTP type ipv4</pre>|
| `nv set acl <cl-name> rule <rule-id> match <match>`| Sets the ACL rule to `match` certain parameters. You must set the parameters according to the ACL type. For example, you cannot set `match mac X:X:X:X:X:X` to an IPv4 ACL type.<pre>$ nv set acl DENY_TCP_HTTP rule 10 match ip protocol tcp</br>$ nv set acl DENY_TCP_HTTP rule 10 match ip source-ip ANY</br>$ nv set acl DENY_TCP_HTTP rule 10 match ip source-port ANY</br>$ nv set acl DENY_TCP_HTTP rule 10 match ip dest-ip 10.0.15.8/32</br>$ nv set acl DENY_TCP_HTTP rule 10 match ip dest-port 80</pre>|
| `nv set acl <acl-name> rule <rule-id> action <action>` | Sets the ACL rule action (`permit`, `deny`, `set`, `span`, `erspan`, `police`, or `log`) for the matched traffic. In addition to the basic `permit` and `deny` actions, you can modify and manipulate the matched traffic using the ACL.<pre>$ nv set acl DENY_TCP_HTTP rule 10 action drop</pre>|
| `nv set interface <interface> acl <acl-name> <direction>` | Applies the ACL on an interface. You need to choose the ACL bind direction, `inbound` for ingress traffic or `outbound` for egress.<pre>$ nv set interface swp1 acl DENY_TCP_HTTP inbound</pre>|
| `nv set interface <interface> acl <acl-name> <direction> control-plane` | Applies the ACL on the control plane and binds to an interface (in an `inbound` or `outbound` direction).<pre>$ nv set interface swp1 acl deny_icmp inbound control-plane</pre>|

## Monitoring Commands

The NVUE monitoring commands show how your network is configured. The monitoring commands are divided into categories (objects), which include subcommands. The general command syntax is `nv show <category> <subcommand> <subcommand> <...>`. You can use TAB completion to navigate through the commands.

| <div style="width:200px">Command Syntax | Description |
| -------------- | ----------------------- |
| `nv show acl <name>` | Shows an access list configuration.|
| `nv show action` |Shows information about the action commands that reset counters and remove conflicts.|
| `nv show bridge`| Shows bridge domain configuration.|
| `nv show evpn` | Shows EVPN configuration.|
| `nv show interface`|Shows interface configuration.|
| `nv show mlag`|Shows MLAG configuration.|
| `nv show nve` |Shows network virtualization configuration, such as VXLAN-specific MLAG configuration and VXLAN flooding.|
| `nv show platform`| Shows platform configuration, such as hardware and software components.|
| `nv show qos` | Shows QoS RoCE configuration.|
| `nv show router`| Shows router configuration, such as router policies, global BGP and OSPF configuration, PBR, PIM, IGMP, VRR, and VRRP configuration.|
| `nv show service` |Shows DHCP relays and server, NTP, PTP, LLDP, and Syslog configuration.|
| `nv show system` |Shows global system settings, such as the reserved routing table range for PBR and the reserved VLAN range for layer 3 VNIs. You can also see system login messages and switch reboot history.|
| `nv show vrf` |Shows VRF configuration.|

NVUE provides additional options for the `nv show` commands. These options are available using command flags.

| <div style="width:200px">Command Syntax | Description |
| -------------- | ----------------------- |
| `--applied`  | Shows the applied configuration for the shown object.|
| `--operational` |Shows the running configuration for the shown object. The `applied` and `operational` configuration must be identical.|
| `--color` | Shows the output with or without colors. |
| `--help` | Shows help for the command. This option also applies to `nv set` and `nv unset` commands.|
| `--output` | Shows the output in <code>json</code> or <code>yaml</code> format. |
| `--paginate` | Paginates the output. |
| `--pending` | Shows the pending configuration of the object. The configuration that is `set` and `unset` but not yet applied or saved.|
| `--rev <revision>` | Shows a detached pending configuration (with the `nv detach` command).|
| `--startup` | Shows the switch startup configuration (with the `nv config save` command).|
| `--view` | Shows these different views: `brief`, `lldp`, `mac`, `pluggables`, and `small`. This option is available for the `nv show interface` command only. For example, the `nv show interface --view=small` command shows a list of the interfaces on the switch and the `nv show interface --view=brief` command shows information about each interface on the switch, such as the interface type, speed, remote host, and port.|

Here are some useful show commands:

| <div style="width:250px">Command Syntax | Description |
| -------------- | ----------------------- |
| `nv show interface` | Shows the status of all interfaces. You can specify an interface to show its configuration and operational state. For each specific interface information, use the interface name in the command.|
| `nv show platform hardware` | Shows switch hardware-related information such as the ASIC model, CPU, memory, serial numbers, and so on. |
| `nv show platform environment` | Shows switch fans, LEDs, PSU and sensor information.|
| `nv show platform software` | Shows the installed system software packages and their versions.|
| `nv show system cpu` | Shows system CPU information and utilization.|
| `nv show system memory` | Shows system memory information and utilization.|
| `nv show service ntp` | Shows NTP service configuration and status. |
| `nv show system wjh packet-buffer` | Shows the <a href="/cumulus-linux-53/Monitoring-and-Troubleshooting/Network-Troubleshooting/Mellanox-WJH">What Just Happened (WJH)</a> configuration and drop events on the switch. |
| `nv show bridge domain br_default mac-table` | Shows the bridge MAC address table. |
| `nv show bridge domain br_default stp` | Shows the bridge spanning-tree status. |
| `nv show bridge domain br_default vlan` | Shows the bridge VLAN list and VNI mapping (if configured). |
| `nv show interface swp1 bridge domain br_default` | Shows the VLAN and spanning-tree status of an interface.|
| `nv show interface swp1 bridge domain br_default` | Shows the VLAN and spanning-tree status of an interface. |
| `nv show mlag` | Shows MLAG configuration and operational state.|
| `nv show mlag consistency-checker` | Shows configuration consistency and conflicts between MLAG peers. |
| `nv show mlag vni` | Shows VNI configuration on both MLAG peers. |
| `nv show nve` | Shows NVE interface (VTEP) configuration and operational state. |
| `nv show acl` | Shows access list configuration. |

## Action Commands

The NVUE action commands reset counters for interfaces and remove conflicts from protodown MLAG bonds.

| <div style="width:250px">Command Syntax | Description |
| -------------- | ----------------------- |
 `nv action clear interface <interface> qos roce counters` | Resets interface RoCE counters.<pre>$ nv action clear interface swp1 qos roce counters</pre> |
| `nv action clear interface <bond-name> bond mlag lacp-conflict` |  Removes duplicate partner MAC address or partner MAC address mismatch conflicts from protodown MLAG bonds.<pre>$ nv action clear interface bond1 bond mlag lacp-conflict</pre> |

## Configuration Management

NVUE leverages the Git engine to manage configuration so that you can treat your configuration as you would code.

| Command Syntax | Description |
| -------------- | ----------------------- |
| `nv config apply` | Applies the pending configuration. </br>The `-y` or `--assume-yes` flag automatically replies `yes` to all prompts (use the `--assume-no` flag for `no`).</br>Configuration `apply` does not save the configuration as the startup configuration, you need to run `nv config save`.</br>You can use the `--confirm` flag to leverage the `commit-confim` capability (`--confirm-status` shows the time left to confirm).|
| `nv config detach` | Deletes the current pending configuration. |
| `nv config diff <revision-a> <revision-b>`</br></br>`nv config diff <revision> <revision> -o commands` | Shows differences between two configuration revisions, such as the `pending` and `applied` configuration or the `detached` and `pending` configurations.</br> If you use `-o commands`, the show command presents the information in NVUE command syntax.|
| `nv config history <nvue-file>` | Shows the apply history for the configuration revision (file). |
| `nv config patch <nvue-file>` | Updates the pending configuration with the specified YAML configuration file. For more information, refer to <a href="/cumulus-linux-53/System-Configuration/NVIDIA-User-Experience-NVUE/NVUE-Snippets">NVUE Snippets</a>. |
| `nv config replace <nvue-file>` | Replaces the pending configuration with the specified YAML configuration file. |
| `nv config save` | Overwrites the startup configuration with the applied configuration (writes to `/etc/nvue.d/startup.yaml`). This configuration persists after a reboot.|
| `nv config show`</br>`nv config show -o commands` | Shows the currently applied configuration in `yaml` format.</br> If you use `-o commands`, the show command presents the information in NVUE command syntax.|
