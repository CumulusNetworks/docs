---
title: NCLU to NVUE Common Commands
weight: 300
---

Cumulus Linux version 4.4 introduces a new CLI called {{<kb_link latest="cl" url="System-Configuration/NVIDIA-User-Experience-NVUE.md" text="NVUE">}}. NVUE is a complete object model for Cumulus Linux, which makes translating configurations from one vendor to another much more reliable the first time you use Cumulus Linux and across Cumulus Linux versions.

This KB article describes how to translate common NCLU configurations to NVUE commands.

## Hostname and System

<table>
    <tr>
        <th>
        NCLU Command
        </th>
        <th>
        NVUE Command
        </th>
        <th>
        Comments
        </th>
    </tr>
    <tr>
        <td style="vertical-align : middle">
        <code>net add hostname &lt;hostname&gt;</code>
        </td>
        <td style="vertical-align : middle">
        <code>nv set platform hostname &lt;hostname&gt;</code>
        </td>
        <td>
        </td>       
    </tr>
    <tr>
        <td style="vertical-align : middle">
        <code>net add syslog host [ipv4|ipv6] &lt;ip&gt; port [tcp|udp] &lt;port&gt;</code>
        </td>
        <td style="vertical-align : middle">
        <code>nv set service syslog default server &lt;ip&gt;</code>
        </td>
        <td rowspan="2" style="vertical-align : middle">
        The value <code>default</code> is the VRF the server is in.
        </td>      
    </tr>
    <tr>
        <td style="vertical-align : middle">
        <code>net add time ntp server &lt;ip&gt;</code>
        </td>
        <td style="vertical-align : middle">
        <code>nv set service ntp default server &lt;ip&gt;</code>
        </td>   
    </tr>
    <tr>
        <td style="vertical-align : middle">
        <code>net pending</code>
        </td>
        <td style="vertical-align : middle">
        <code>nv config diff empty pending</code>
        </td>   
        <td>
        NVUE can compare between configuration types. </br> When any config type compared to <code>empty</code>, it shows only the type being compared.
        </td>   
    </tr>
    <tr>
        <td rowspan="2" style="vertical-align : middle">
        <code>net commit</code>
        </td>
        <td style="vertical-align : middle">
        <code>nv config apply</code>
        </td>   
        <td rowspan="2" style="vertical-align : middle">
        In NCLU, the running-config equals the startup-config. </br> NVUE separates running and startup configs: </br> <code>nv config apply</code> - apply configuration as running (without saving as startup) </br> <code>nv config save</code> - save configuration as startup (without applying as running)
        </td>
    </tr>
    <tr>
        <td style="vertical-align : middle">
        <code>nv config save</code>
        </td>
    </tr>
    <tr>
        <td rowspan="3" style="vertical-align : middle">
        <code>net show configuration</code>
        </td>
        <td style="vertical-align : middle">
        <code>cat /etc/nvue.d/startup.yaml</code>
        </td>   
        <td rowspan="3" style="vertical-align : middle">
        By using the <code>net show configuration commands</code>, you can view the configuration as actual NCLU commands.</br> NVUE is based on a single startup-config YAML file, you can view it using Linux <code>cat</code> command or using NVUE commands.
        </td>
    </tr>
    <tr>
        <td style="vertical-align : middle">
        <code>nv config diff empty startup</code>
        </td>   
    </tr>
    <tr>
        <td style="vertical-align : middle">
        <code>nv config diff empty applied</code>
        </td>   
    </tr>
</table>


## Interfaces

<table>
    <tr>
        <th>
        NCLU Command
        </th>
        <th>
        NVUE Command
        </th>
        <th>
        Comments
        </th>
    </tr>
    <tr>
        <td style="vertical-align : middle">
        <code>net add interface &lt;interface&gt; </code>
        </td>
        <td style="vertical-align : middle">
        <code>nv set interface &lt;interface&gt; type &lt;interface-type&gt;</code>
        </td>
        <td style="vertical-align : middle">
        NVUE allows to create any interface-type under the interface object. </br> NCLU is not an object model, so this command only allows to create &lt;swp&gt; interface-type. For other interface-types, you need to use different commands.
        </td>
    <tr>
        <td style="vertical-align : middle">
        <code>net add interface &lt;interface&gt; [ipv4|ipv6] address &lt;ip/mask&gt;</code>
        </td>
        <td style="vertical-align : middle">
        <code>nv set interface &lt;interface&gt; ip address &lt;ip/mask&gt;</code>
        </td>
        <td style="vertical-align : middle">
        In NVUE, you set IPv4 and IPv6 addresses with the same command. </br> To configure secondary IP address, use the same command.</br> To replace existing IP address, delete it first using: </br> NCLU - <code>net del interface &lt;interface&gt; [ipv4|ipv6] address &lt;ip/mask&gt;</code></br>NVUE - <code>nv unset interface &lt;interface&gt; ip address &lt;ip/mask&gt;</code>
        </td>      
    </tr>
    <tr>
        <td style="vertical-align : middle">
        <code>net add interface &lt;interface&gt; mtu &lt;mtu&gt;</code>
        </td>
        <td style="vertical-align : middle">
        <code>nv set interface &lt;interface&gt; link mtu &lt;mtu&gt;</code>
        </td>
        <td style="vertical-align : middle">
        The dafault MTU in Cumulus Linux is 9216B.
        </td>   
    </tr>
    <tr>
        <td style="vertical-align : middle">
        <code>net add interface &lt;interface&gt; link speed &lt;speed&gt;</code>
        </td>
        <td style="vertical-align : middle">
        <code>nv set interface &lt;interface&gt; link speed &lt;speed&gt;</code>
        </td>
        <td>
        </td>  
    </tr>
    <tr>
        <td style="vertical-align : middle">
        <code>net add interface &lt;interface&gt; link fec &lt;fec-mode&gt;</code>
        </td>
        <td style="vertical-align : middle">
        <code>nv set interface &lt;interface&gt; link fec &lt;fec-mode&gt;</code>
        </td>
        <td style="vertical-align : middle">
        </td>  
    </tr>
    <tr>
        <td style="vertical-align : middle">
        <code>net [add|del] interface &lt;interface&gt; link down &lt;fec-mode&gt;</code>
        </td>
        <td style="vertical-align : middle">
        <code>nv set interface &lt;interface&gt; link state [up|down]</code>
        </td>
        <td style="vertical-align : middle">
        The dafault state for interfaces is UP. 
        </td> 
    </tr>
    <tr>
        <td style="vertical-align : middle">
        <code>net add loopback lo</code>
        </td>
        <td style="vertical-align : middle">
        <code>nv set interface lo</code>
        </td>
        <td style="vertical-align : middle">
        The loopback interface in Cumulus Linux called "lo". 
        </td> 
    </tr>
    <tr>
        <td style="vertical-align : middle">
        <code>net add interface &lt;interface&gt; breakout &lt;breakout-option&gt;</code>
        </td>
        <td style="vertical-align : middle">
        <code>nv set interface &lt;interface&gt; link breakout &lt;breakout-option&gt;</code>
        </td>
        <td>
        Multiple breakout options exist. To veiw all options run:</br> NVUE - <code>nv set interface &lt;interface&gt; link breakout -h</code></br> NCLU - <code>net add interface &lt;interface&gt; breakout &lt;press TAB&gt;
        </td>   
    </tr>
    <tr>
        <td style="vertical-align : middle">
        <code>net add interface &lt;interface&gt; alias &lt;description-text&gt;</code>
        </td>
        <td style="vertical-align : middle">
        <code>nv set interface &lt;interface&gt; alias &lt;description-text&gt;</code>
        </td>
        <td style="vertical-align : middle">
        </td> 
    </tr>
</table>

## Bonds and Port Channels

Linux uses the term `bond` to represent `port-channels`.

<table>
    <tr>
        <th>
        NCLU Command
        </th>
        <th>
        NVUE Command
        </th>
        <th>
        Comments
        </th>
    </tr>
    <tr>
        <td rowspan="2" style="vertical-align : middle">
        <code>net add bond &lt;bond-name&gt; bond slaves &lt;interfaces&gt; </code>
        </td>
        <td style="vertical-align : middle">
        <code>nv set interface &lt;bond-name&gt; bond memeber &lt;interfaces&gt;</code>
        </td>
        <td rowspan="2" style="vertical-align : middle">
        In NCLU, bond is created by enslaving ports to it (or seetting <code>bond mode</code>). You create bond and add memebers in a sinble command.</br> In NVUE, you can create bond in the same way or without adding memebers by creating it using the <code>type bond</code> interface command. In addition, by naming bond interface as "bond...", its type will be defined automatically. e.g. <code>nv set interface bond1</code></br>NOTE: You define bonds with a name that must start with a letter. 
        </td>
    </tr>
    <tr>
        <td style="vertical-align : middle">
        <code>nv set interface &lt;bond-name&gt; type bond</code>
        </td>
    </tr>
    <tr>
        <td style="vertical-align : middle">
        <code>net add bond &lt;bond-name&gt; bond mode balance-xor</code>
        </td>
        <td style="vertical-align : middle">
        <code>nv set interface &lt;bond-name&gt; bond mode static</code>
        </td>
        <td style="vertical-align : middle">
        The default bond mode in Cumulus LInux is <code>lacp</code> (<code>802.3ad</code> in NCLU).
        </td>
    </tr>
    <tr>
        <td style="vertical-align : middle">
        <code>net add bond &lt;bond-name&gt; bond lacp-rate slow</code>
        </td>
        <td style="vertical-align : middle">
        <code>nv set interface &lt;bond-name&gt; bond lacp-rate slow</code>
        </td>
        <td style="vertical-align : middle">
        The default bond lacp-rate in Cumulus LInux is <code>fast</code>.
        </td>
    </tr>
</table>

## Layer 2 and VLANs

Cumulus Linux interfaces are layer 3 routed interfaces by default. To make an interface a layer 2 switchport, you must add the interface to the default bridge called `bridge` when using NCLU or `br_default` in NVUE:

{{< tabs "bridge commands ">}}
{{< tab "NCLU">}}
```
cumulus@switch:~$ net add bridge bridge ports <interface>
```
{{</ tab >}}
{{< tab "NVUE">}}
```
cumulus@switch:~$ nv set interface <interface> bridge domain br_default
```
{{</ tab >}}
{{</ tabs >}}

<table>
    <tr>
        <th>
        NCLU Command
        </th>
        <th>
        NVUE Command
        </th>
        <th>
        Comments
        </th>
    </tr>
    <tr>
        <td style="vertical-align : middle">
        <code>net add interface &lt;interface&gt; bridge access &lt;vlan-id&gt;</code>
        </td>
        <td style="vertical-align : middle">
        <code>nv set interface &lt;interface&gt; bridge domain br_default access &lt;vlan-id&gt;</code>
        </td>
        <td style="vertical-align : middle">
        </td>
    </tr>
    <tr>
        <td style="vertical-align : middle">
        <code>net add bridge bridge ports &lt;interface&gt;</code>
        </td>
        <td style="vertical-align : middle">
        <code>nv set interface &lt;interface&gt; bridge domain br_default</code>
        </td>
        <td style="vertical-align : middle">
        Ports you add to a bridge are trunk ports by default (all vlans allowed).
        </td>
    </tr>
    <tr>
        <td style="vertical-align : middle">
        <code>net add inerface &lt;interface&gt; bridge trunk vlans &lt;vlan-id|vlan-list&gt;</code>
        </td>
        <td style="vertical-align : middle">
        <code>nv set interface &lt;interface&gt; bridge domain br_default vlan &lt;vlan-id|vlan-list|all&gt;</code>
        </td>
        <td style="vertical-align : middle">
        To allow all vlans on the trunk port: </br> NCLU - <code>net add inerface &lt;interface&gt; bridge trunk</code> </br> NVUE - <code>nv set interface &lt;interface&gt; bridge domain br_default</code>  
        </td>
    </tr>
        <td style="vertical-align : middle">
        <code>net add inerface &lt;interface&gt; stp portadminedge</code>
        </td>
        <td style="vertical-align : middle">
        <code>nv set interface &lt;interface&gt; bridge domain br_default stp admin-edge on</code>
        </td>
        <td style="vertical-align : middle">
        </td>
    </tr>
    </tr>
        <td style="vertical-align : middle">
        <code>net add inerface &lt;interface&gt; stp portnetwork</code>
        </td>
        <td style="vertical-align : middle">
        <code>nv set interface &lt;interface&gt; bridge domain br_default stp network on</code>
        </td>
        <td style="vertical-align : middle">
        </td>
    </tr>
    </tr>
        <td style="vertical-align : middle">
        <code>net add inerface &lt;interface&gt; stp bpduguard</code>
        </td>
        <td style="vertical-align : middle">
        <code>nv set interface &lt;interface&gt; bridge domain br_default stp bpdu-guard on</code>
        </td>
        <td style="vertical-align : middle">
        </td>
    </tr>
    </tr>
        <td style="vertical-align : middle">
        <code>net add inerface &lt;interface&gt; stp portbpdufilter</code>
        </td>
        <td style="vertical-align : middle">
        <code>nv set interface &lt;interface&gt; bridge domain br_default stp bpdu-filter on</code>
        </td>
        <td style="vertical-align : middle">
        </td>
    </tr>
    </tr>
        <td style="vertical-align : middle">
        <code>net add bridge stp treeprio &lt;stp-priority&gt;</code>
        </td>
        <td style="vertical-align : middle">
        <code>nv set bridge domain br_default stp priority &lt;stp-priority&gt;</code>
        </td>
        <td style="vertical-align : middle">
        Cumulus Linux only supports {{<kb_link latest="cl" url="Layer-2/Spanning-Tree-and-Rapid-Spanning-Tree.md" text="RSTP." >}}
        </td>
    </tr>
</table>

## MLAG and vPC

In MLAG configuration, Cumulus Linux uses *peer link* (bond between peers) to sync the MLAG pair. To keep MLAG pairs in sync when a direct connection fails, Cumulus Linux uses *mlag backup IP*.

For more information about MLAG, refer to the {{<kb_link latest="cl" url="Layer-2/Multi-Chassis-Link-Aggregation-MLAG.md" text="Multi-Chassis Link Aggregation - MLAG" >}} page on the Cumulus Linux User Guide.

<table>
    </tr>
        <td style="vertical-align : middle">
        <code>net add bond &lt;bond-name&gt; clag id &lt;number&gt;</code>
        </td>
        <td style="vertical-align : middle">
        <code>nv set interface &lt;bond-name&gt; bond mlag id &lt;number|auto&gt;</code>
        </td>
        <td style="vertical-align : middle">
        You should create bond interfaces prior setting mlag id. The <code>mlag id</code> must match the bond interface on both MLAG peers connected to the same host. Using <code>&lt;auto&gt;</code> determines the ID based on the the MAC address of the end host.
        </td>
    </tr>
    </tr>
        <td rowspan="4" style="vertical-align : middle">
        <code>net add clag peer sys-mac &lt;mac&gt; interface &lt;peerlink-members&gt; [primary|secondary] backup-ip &lt;ip&gt;</code>
        </td>
        <td style="vertical-align : middle">
        <code>nv set mlag mac-address &lt;mac|auto&gt;</code>
        </td>
        <td rowspan="4" style="vertical-align : middle">
        NCLU MLAG configuration requires to set all paramaters in a single command where the <code>backup-ip &lt;ip&gt;</code> is optional.</br>NVUE MLAG configurat6ion separated into several commands, it allows easier changes to MLAG global parameters. It also supports <code>&lt;auto&gt;</code> MAC address generation.</br>Cumulus Linux requires a unique bond for the peerlink and an associated <code>peer-ip</code> definition.   
        </td>
    </tr>
        <td style="vertical-align : middle">
        <code>nv set interface peerlink bond member &lt;interfaces&gt;</code>
        </td>
    </tr>
    </tr>
        <td style="vertical-align : middle">
        <code>nv set mlag peer-ip linklocal</code>
        </td>
    </tr>
    </tr>
        <td style="vertical-align : middle">
        <code>nv set mlag backup &lt;ip&gt;</code>
        </td>
    </tr>
</table>

## Layer 3 Routing Protocols

Most NVUE BGP commands require the VRF to be included in the command. The examples below include the `default` VRF name since it is pre-defined in the system, but any VRF name can be used. You can still configure some of the global BGP parameters (enable/disable BGP, set the ASN and the router ID, configure BGP graceful restart, and shutdown the router) without specifying a VRF. Then all VRFs enherit these settings automatically unless you set specific settings on the VRF.</br> In NCLU, by default, all configuration is done globally on the system's default VRF, unless other VRF specified (NCLU doesn't have pre-defined VRF named `default`). Custom VRFs don't enherit the global BGP settings and must be configured separately.

<table>
    <tr>
        <th>
        NCLU Command
        </th>
        <th>
        NVUE Command
        </th>
        <th>
        Comments
        </th>
    </tr>
    <tr>
        <td style="vertical-align : middle">
        <code>net add bgp [vrf &lt;name&gt;] autonomous-system &lt;leaf|spine|ASN&gt;</code>
        </td>
        <td style="vertical-align : middle">
        <code>nv set [vrf &lt;default|name&gt;] router bgp autonomous-system &lt;leaf|spine|none|ASN&gt;</code>
        </td>
        <td style="vertical-align : middle">
        In NVUE, when a single AS is in use for all VRFs, the <code>[vrf &lt;name&gt;]</code> not required to create the instance. Its settings will be automatically applied to all VRFs including the <code>default</code> VRF.</br> If <code>&lt;none&gt;</code> ASN option used globally, then ASN must be set for every VRF.</br>For more information about the <code>&lt;leaf|spine&gt;</code> options, check out {{<kb_link latest="cl" url="layer-3/Border-Gateway-Protocol-BGP/#auto-bgp" text="Auto BGP" >}} section in the Cumulus Linux User Guide.
        </td>
    </tr>
    <tr>
        <td style="vertical-align : middle">
        <code>net add bgp [vrf &lt;name&gt;] router-id &lt;ipv4&gt;</code>
        </td>
        <td style="vertical-align : middle">
        <code>nv set [vrf &lt;default|name&gt;] router bgp router-id &lt;ipv4&gt;</code>
        </td>
        <td style="vertical-align : middle">
        In NVUE, when a single AS is in use for all VRFs, the <code>&lt;vrf &lt;name&gt;&gt;</code> not required in the command. It will be gloabally applied to all VRFs including the <code>default</code> VRF.
        </td>
    </tr>
    <tr>
        <td style="vertical-align : middle">
        <code>net add bgp [vrf &lt;name&gt;] neighbor &lt;ip|interface&gt; remote-as &lt;internal|external|ASN&gt; </code>
        </td>
        <td style="vertical-align : middle">
        <code> set vrf &lt;default|name&gt; router bgp peer &lt;ip|interface&gt; remote-as &lt;internal|external|ASN&gt;</code>
        </td>
        <td style="vertical-align : middle">
        NVUE requires to specify a VRF when adding BGP peer. Cumulus Linux supports {{<kb_link latest="cl" url="layer-3/Border-Gateway-Protocol-BGP/#bgp-unnumbered" text="BGP Unnambered" >}} peer configuration.</br>The ASN can be a number, or <code>internal</code> for a neighbor in the same AS or <code>external</code> for a neighbor in a different AS.
        </td>
    </tr>
    <tr>
        <td style="vertical-align : middle">
        <code>net add bgp [vrf &lt;name&gt;] neighbor &lt;name&gt; peer-group &lt;attributes&gt;</code>
        </td>
        <td style="vertical-align : middle">
        <code>nv set vrf &lt;default|name&gt; router bgp peer-group &lt;name&gt; &lt;attributes&gt;</code>
        </td>
        <td style="vertical-align : middle">
        NCLU requires to create peer-group with </br><code>net add bgp &lt;vrf &lt;name&gt;&gt; neighbor &lt;name&gt; peer-group</code> prior configuring its attributes.</br> NVUE allows you to create peer-group and set its attributes in a single command.
        </td>
    </tr>
    <tr>
        <td style="vertical-align : middle">
        <code>net add bgp [vrf &lt;name&gt;] [ipv4|ipv6] unicast network &lt;ipv4|ipv6/mask&gt;</code>
        </td>
        <td style="vertical-align : middle">
        <code>nv set vrf &lt;default|name&gt; router bgp address-family &lt;ipv4-unicast|ipv6-unicast&gt; static-network &lt;ipv4|ipv6/mask&gt;</code>
        </td>
        <td style="vertical-align : middle">
        In NCLU, address-family is optional and can be determined by the type of the ip-address advertised. In NVUE, you must specify the address-family to advertise network into it.
        </td>
    </tr>
    <tr>
        <td style="vertical-align : middle">
        <code>net add bgp [vrf &lt;name&gt;] &lt;ipv4|ipv6&gt; unicast redistribute &lt;connected|static|ospf|kernel&gt;</code>
        </td>
        <td style="vertical-align : middle">
        <code>nv set vrf &lt;default|name&gt; router bgp address-family &lt;ipv4-unicast|ipv6-unicast&gt; redistribute &lt;connected|static|ospf|kernel&gt;</code>
        </td>
        <td style="vertical-align : middle">
        </td>
    </tr>
    <tr>
        <td rowspan="2" style="vertical-align : middle">
        <code>net add routing prefix-list &lt;ipv4|ipv6&gt; &lt;name&gt; seq &lt;seq&gt; &lt;permit|deny&gt; &lt;ipv4|ipv6/lenght|any&gt;</code>
        </td>
        <td style="vertical-align : middle">
        <code>nv set router policy prefix-list &lt;name&gt; rule &lt;seq&gt; action &lt;permit|deny&gt;</code>
        </td>
        <td rowspan="2" style="vertical-align : middle">
        NCLU allows to configure prefix-list action and match in a single command. </br> NVUE does it in two commands. The default prefix-list type in NVUE is IPv4. But, you can set IPv6 prefix-list using the <code>nv set router policy prefix-list &lt;name&gt; type ipv6</code> command. 
        </td>
    </tr>
    <tr>
        <td style="vertical-align : middle">
        <code>nv set router policy prefix-list &lt;name&gt; rule &lt;seq&gt; match &lt;prefix/lenght&gt;</code>
        </td>
    </tr>
    <tr>
        <td style="vertical-align : middle">
        <code>net add bgp [vrf &lt;name&gt;] [ipv4|ipv6] neighbor &lt;ip|interface&gt; prefix-list &lt;name&gt; &lt;in|out&gt;</code>
        </td>
        <td style="vertical-align : middle">
        <code>nv set vrf &lt;default|name&gt; router bgp peer &lt;ip|interface&gt; address-family &lt;ipv4-unicast|ipv6-unicast&gt; policy &lt;inbound|outbound&gt; prefix-list &lt;name&gt;</code>
        </td>
        <td style="vertical-align : middle">
        In NCLU, when no address-family specified, the default is IPv4-unicast.
        </td>
    </tr>
    <tr>
        <td rowspan="2" style="vertical-align : middle">
        <code>net add routing route-map &lt;name&gt; &lt;permit|deny&gt; &lt;seq&gt; match ip address prefix-list &lt;name&gt;</code>
        </td>
        <td style="vertical-align : middle">
        <code>nv set router policy route-map &lt;name&gt; rule &lt;seq&gt; action &lt;permit|deny&gt;</code>
        </td>
        <td rowspan="2" style="vertical-align : middle">
        NCLU allows to configure route-map action and match in a single command. </br> NVUE does it with two commands for that. 
        </td>
    </tr>
    <tr>
        <td style="vertical-align : middle">
        <code>nv set router policy route-map &lt;name&gt; rule &lt;seq&gt; match ip-prefix-list &lt;name&gt;</code>
        </td>
    </tr>
    <tr>
        <td style="vertical-align : middle">
        <code>net add bgp [vrf &lt;name&gt;] [ipv4|ipv6|evpn] neighbor &lt;ip|interface&gt; route-map &lt;name&gt; &lt;in|out&gt;</code>
        </td>
        <td style="vertical-align : middle">
        <code>nv set vrf &lt;default|name&gt; router bgp peer &lt;ip|interface&gt; address-family &lt;ipv4-unicast|ipv6-unicast|l2vpn-evpn&gt; policy &lt;inbound|outbound&gt; route-map &lt;name&gt;</code>
        </td>
        <td style="vertical-align : middle">
        In NCLU, when no address-family specified, the default is IPv4-unicast.
        </td>
    </tr>
    <tr>
        <td style="vertical-align : middle">
        <code>net add routing route &lt;ipv4|ipv6/mask&gt; &lt;next-hop|interface&gt; [vrf &lt;name&gt;] </code>
        </td>
        <td style="vertical-align : middle">
        <code>nv set vrf &lt;default|name&gt; router static &lt;route&gt; via &lt;next-hop&gt;</code>
        </td>
        <td style="vertical-align : middle">
        </td>
    </tr>
</table>

## VXLAN and EVPN 

<table>
    <tr>
        <th>
        NCLU Command
        </th>
        <th>
        NVUE Command
        </th>
        <th>
        Comments
        </th>
    </tr>
    <tr>
        <td style="vertical-align : middle">
        <code>net add loopback lo clag vxlan-anycast-ip &lt;ip&gt;</code>
        </td>
        <td style="vertical-align : middle">
        <code>nv set nve vxlan mlag shared-address &lt;ip&gt;</code>
        </td>
        <td style="vertical-align : middle">
        </td>
    </tr>
    <tr>
        <td style="vertical-align : middle">
        <code>net add vxlan &lt;name&gt; vxlan id &lt;number&gt;</code>
        </td>
        <td style="vertical-align : middle">
        <code>nv set bridge domain br_default vlan &lt;number&gt; vni &lt;number&gt;</code>
        </td>
        <td style="vertical-align : middle">
        </td>
    </tr>
    <tr>
        <td style="vertical-align : middle">
        <code>net add vxlan &lt;name&gt; vxlan id &lt;number&gt;</code>
        </td>
        <td style="vertical-align : middle">
        <code>nv set bridge domain br_default vlan &lt;number&gt; vni &lt;number&gt;</code>
        </td>
        <td style="vertical-align : middle">
        </td>
    </tr>

| NX-OS Command | NVUE Command | Comments |
| -----         | -----        | -----    |

|`fabric forwarding anycast-gateway-mac 0001.0001.0001`| `nv set system global anycast-mac 44:38:39:BE:EF:AA` | |
|`ip pim rp-address 192.168.9.9 group-list 224.0.0.0/4`| _none_ | NVIDIA recommends you use Head End Replication for EVPN, removing the need for PIM. For scale-out deployments {{<kb_link latest="cl" url="Network-Virtualization/Ethernet-Virtual-Private-Network-EVPN/EVPN-PIM.md" text="PIM Replication" >}} is supported.|
|`ip pim ssm range 232.0.0.0/8`| _none_ |
|`vlan 1,10,20,30,40`| `nv set bridge domain br_default vlan 30,40` | {{<kb_link latest="cl" url="Layer-2/Ethernet-Bridging-VLANs/VLAN-aware-Bridge-Mode.md" text="Ethernet Bridging" >}}
|`vlan 10`| _none_ | The layer 3 VNI does not require a unique VLAN interface. |
|` name L3-VNI-VLAN-10`|  _none_ | |
|` vn-segment 10000010`|  _none_ | |
|`vlan 30`| `nv set bridge domain br_default vlan 30 vni 10000030` | |
|` vn-segment 10000030`| _none_ | The `vn-segment` and `vlan` are defined in a single command with NVUE. |
|`vlan 40`| `nv set bridge domain br_default vlan 40 vni 10000040` | |
|` vn-segment 10000040`| _none_ | |
|`vpc domain 2`| `nv set mlag backup 10.197.204.103` | Cumulus Linux {{<kb_link latest="cl" url="Layer-2/Multi-Chassis-Link-Aggregation-MLAG.md" text="Multi-Chassis Link Aggregation - MLAG" >}} uses remote and local peering to ensure uptime.|
|` peer-keepalive destination 10.197.204.103`| `nv set mlag peer-ip linklocal` | You can determine the local peer IP automatically with link-local addresses. |
|`interface Vlan10`| _none_ | The layer 3 VNI does not require a unique VLAN interface. |
|` no shutdown`| _none_ | |
|` vrf member EVPN-L3-VNI-VLAN-10`| _none_ | |
|` ip forward`| _none_ | |
|`interface Vlan30`| | |
|` no shutdown`| _none_ | Interfaces are `no shut` by default. |
|` vrf member EVPN-L3-VNI-VLAN-10`| `nv set interface vlan30 ip vrf EVPN-L3-VNI-VLAN-10` | |
|` ip address 172.16.30.1/24`| `nv set interface vlan30 ip address 172.16.30.1/24` | |
|` fabric forwarding mode anycast-gateway`| _none_ | No explicit command is required for this setting in NVUE. |
|`interface Vlan40 `| | |
|` no shutdown`| _none_ | |
|` vrf member EVPN-L3-VNI-VLAN-10`| `nv set interface vlan40 ip vrf EVPN-L3-VNI-VLAN-10` | |
|` ip address 172.16.40.1/24`| `nv set interface vlan40 ip address 172.16.40.1/24` | |
|`interface port-channel2 `| `nv set interface bond2 bond member swp1` | This example uses `swp1` instead of NX-OS port `e1/13`. | 
|` switchport mode trunk`| `nv set interface bond2 bridge domain br_default vlan all` | `br_default` is the name of the default bridge. |
|` vpc 2`| `nv set interface bond2 bond mlag id 2`| |
|`interface port-channel34`|`nv set interface peerlink bond member swp49` | This example uses `swp49` instead of NX-OS port `e1/1`. |
|`interface nve1`| _none_ | There is no explicit NVUE interface. |
|` source-interface loopback2`| `nv set nve vxlan source address 192.168.33.33` | You configure NVUE interface settings globally with `nv set nve vxlan` commands.|
|` member vni 10000010 associate-vrf`| `nv set vrf EVPN-L3-VNI-VLAN-10 evpn vni 10000010` | | 
|` member vni 10000030`| _none_ | You only need to associate the VRF VNI. | 
|` suppress-arp`| `nv set nve vxlan arp-nd-suppress on` | | 
|` mcast-group 239.1.1.10`| _none_ | NVIDIA recommends you use Head end Replication. |
|` switchport mode trunk`| _none_ | The interface was defined when the bond was created earlier. |
|` no switchport`| _none_ | Interfaces are layer 3 by default. |
|` ip address 192.168.39.3/24`| _none_ | NVIDIA recommends {{<kb_link latest="cl" url="Layer-3/Border-Gateway-Protocol-BGP/Basic-BGP-Configuration.md#bgp-unnumbered" text="BGP Unnumbered" >}} for the underlay, removing the need for an IP address. |
|` ip router ospf UNDERLAY area 0.0.0.0`| _none_ | NVIDIA recommends BGP Unnumbered. | 
|` ip pim sparse-mode`| _none_ | NVIDIA recommends Head End Replication. |
|` switchport mode trunk`| _none_ | Port configuration is part of the bond definition. | 
|`interface loopback2`| `nv set interface lo ip address 192.168.33.33/32` | Cumulus Linux uses a single loopback `lo`. |
|` ip address 192.168.33.33/32`| _none_ | Defined with the creation of the loopback interface. | 
|` ip address 192.168.33.34/32 secondary`| `nv set nve vxlan mlag shared-address 192.168.33.34` | | 
|` ip router ospf UNDERLAY area 0.0.0.0`| _none_ | NVIDIA recommends using BGP for both the underlay and overlay. |
|`router bgp 65000`| `nv set router bgp autonomous-system  65000` | | 
|` neighbor 192.168.9.9 remote-as 100`| `nv set vrf default router bgp peer swp51 remote-as external` | This command uses eBGP unnumbered instead of IP based peering. |
|` remote-as 65000`| _none_ | This command is combined with the peer command above. |
|` update-source loopback2`| _none_ | BGP unnumbered uses the interface instead of a loopback source. | 
|` address-family l2vpn evpn`| `nv set vrf default router bgp peer swp51 address-family l2vpn-evpn enable on` | | 
|` send-community extended`| _none_ | This is enabled by default. | 
|` vrf EVPN-L3-VNI-VLAN-10`| _none_ | This is managed through an earlier `nv set vrf` command. |

<details>
<summary>Complete NVUE Configuration</summary>

``` 
nv set system global anycast-mac 44:38:39:BE:EF:AA
nv set bridge domain br_default vlan 30,40
nv set bridge domain br_default vlan 30 vni 10000030
nv set bridge domain br_default vlan 40 vni 10000040
nv set mlag backup 10.197.204.103
nv set mlag peer-ip linklocal
nv set interface vlan30 ip vrf EVPN-L3-VNI-VLAN-10
nv set interface vlan30 ip address 172.16.30.1/24
nv set interface vlan40 ip vrf EVPN-L3-VNI-VLAN-10
nv set interface vlan40 ip address 172.16.40.1/24
nv set interface bond2 bond member swp1
nv set interface bond2 bridge domain br_default vlan all
nv set interface bond2 bond mlag id 2
nv set interface peerlink bond member swp49
nv set nve vxlan source address 192.168.33.33
nv set vrf EVPN-L3-VNI-VLAN-10 evpn vni 10000010
nv set nve vxlan arp-nd-suppress on
nv set interface lo ip address 192.168.33.33/32
nv set nve vxlan mlag shared-address 192.168.33.34
nv set router bgp autonomous-system 65000
nv set vrf default router bgp peer swp51 remote-as external
nv set vrf default router bgp peer swp51 address-family l2vpn-evpn enable on
```

</details>

















































## Access Control Lists (ACLs)

ACLs in Cumulus Linux are based on Linux iptables so keep this in mind:
- There is no implicit deny. ACLs must end in a `match any` and `action deny` rule to drop all unmatched traffic.
- There is no support for wildcard masks. You must list subnets individually.
In addition to NCLU commands, you can configure ACLs stright by setting ebtables and iptables rules. To ease ACL management on the system, you can use a tool called `cl-acltool`.

For more information, refer to the {{<kb_link latest="cl" url="System-Configuration/Netfilter-ACLs/_index.md" text="Netfilter - ACLs" >}} section of the Cumulus Linux User Guide.

<table>
    <tr>
        <th>
        NCLU Command
        </th>
        <th>
        NVUE Command
        </th>
        <th>
        Comments
        </th>
    </tr>
    <tr>
        <td rowspan="3" style="vertical-align : middle">
        <code>net add acl &lt;ipv4|ipv6|mac&gt; &lt;name&gt; &lt;action&gt; &lt;protocol&gt; &lt;src_ip&gt; &lt;src_port&gt; &lt;dst_ip&gt; &lt;dst_port&gt;</code>
        </td>
        <td style="vertical-align : middle">
        <code>nv set acl &lt;name&gt; rule &lt;seq&gt; &lt;action&gt; </code>
        </td>
        <td rowspan="3" style="vertical-align : middle">
        NCLU allows ACL configuration in one line, but doesn't have sequance numbers. To change sequance numbers, you have to edit <code>nclu_acl.conf</code> file.</br>NVUE ACL configuration must be using separate commands and it links the source, destination, and actions with the &lt;seq&gt; value.
        </td>
    </tr>
    <tr>
        <td style="vertical-align : middle">
        <code>nv set acl &lt;name&gt; rule &lt;seq&gt; &lt;action&gt; </code>
        </td>
    </tr>

| NX-OS Command | NVUE Command | Comments |
| -----         | -----        | -----    |
|`ip access-list <name>`<br />&nbsp;&nbsp;&nbsp;`<seq> permit ip <source> <destination>` | `nv set acl <name> rule <seq> match source-ip <source>`<br />`nv set acl <name> rule <seq> match dest-ip <destination>`<br />`nv set acl <name> rule <seq> action permit` |  |
|`interface <slot/port>`<br />&nbsp;&nbsp;&nbsp;`ip access-group <name> in` | `nv set interface <interface> acl <name> inbound` |
|`mac access-list <name>`<br />&nbsp;&nbsp;&nbsp;`<seq> permit <source mac> <destination mac> <protocol>` | `nv set acl <name> rule <seq> match source-mac <source mac>`<br />`nv set acl <name> rule <seq> match dest-mac <destination mac>`<br />`nv set acl <name> rule <seq> match protocol <protocol number>`<br />`nv set acl <name> rule <seq> action permit` | NVUE links the source, destination, and actions with the `<seq>` value. |
|`interface <slot/port>`<br />&nbsp;&nbsp;&nbsp;`mac port access-group <name>` | `nv set interface <interface> acl <name> inbound` |
