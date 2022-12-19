---
title: NVIDIA User Experience (NVUE) Cheat Sheet
weight: 102
toc: 4
---

<span style="background-color:#F5F5DC"> [NVUE](## "NVIDIA User Experience")</span> is an object-oriented, schema-driven model of a complete Cumulus Linux system providing a robust API that allows multiple interfaces to view and configure any element within a system.

You can use the NVUE through its <span style="background-color:#F5F5DC"> [CLI](## "Command Line Interface")</span> or the <span style="background-color:#F5F5DC"> [API](## "Application Programming Interface")</span>. As NVUE is an object model, both CLI and REST API interfaces have equivalent functionality and can work in parallel while keeping all management operations consistent; for example, the CLI `show` commands reflect any `PATCH` operation (create) you run through the REST API.  

NVUE follows a declarative model, removing context-specific commands and settings. It is structured as a big tree (like a filesystem path) representing the entire system state. At the tree’s base are high-level branches representing objects, such as router and interface. Under each branch, there are further branches, and as you navigate through the tree, you gain a more specific context of the objects. The tree’s leaves are actual attributes, represented as key-value pairs. 

This cheat sheet will help you get up to speed with using [Cumulus Linux]({{<ref "/cumulus-linux-53">}}) and [NVUE CLI]({{<ref "/cumulus-linux-53/System-Configuration/NVIDIA-User-Experience-NVUE/NVUE-CLI">}}). 

{{%notice note%}}
This cheat sheet covers the most common and useful commands for certain CL elements, features, and protocols. Check out the [Cumulus Linux User Guide]({{<ref "/cumulus-linux-53">}}) for more information and additional/specific configurations. 
{{%/notice%}}
{{%notice note%}}
For information about using the [NVUE REST API]({{<ref "/cumulus-linux-53/System-Configuration/NVIDIA-User-Experience-NVUE/NVUE-API">}}), refer to the [NVUE API documentation](https://docs.nvidia.com/networking-ethernet-software/cumulus-linux-53/api/index.html).
{{%/notice%}}

## NVUE CLI Command Syntax

NVUE commands all begin with `nv` and fall into one of four syntax categories:

- Configuration (`nv set` and `nv unset`)
- Monitoring (`nv show`)
- Configuration management (`nv config`)
- Action commands (`nv action`)

As all industry-standard CLIs, NVUE CLI has commands completion using the TAB key, question mark (`?`) to display required command information, and commands abbreviation to speed up CLI interaction. In addition, in NVUE CLI you can get help with command syntax by using the `-h` or `-`-help` flag and list all commands by using the `nv list-commands`.   

## Getting Started

Once you racked and powered on your NVIDIA Spectrum switch with Cumulus Linux (CL), connect a serial console cable to start configuring it. All switches are manufactured with an RJ45 serial port for console connectivity and set to *115200* boud rate. If your switch doesn't have a pre-installed  NOSNetwork Operating System")</span>, check out how to [install a new CL image]({{<ref "/cumulus-linux-53/Installation-Management/Installing-a-New-Cumulus-Linux-Image">}}).


## System Management and Services

Using the below commands, you can do the initial switch configuration of the management network and some system services.

<table style="width:100%">
    <tr >
        <th style="width:32%">
        Command Syntax
        </th>
        <th style="width:36%">
        Command Description
        </th>
        <th style="width:32%">
        Example
        </th>
    </tr>
    <tr>
        <td style="vertical-align : middle">
        <code>nv set system hostname &lt;name&gt;</code>
        </td>
        <td style="vertical-align : middle">
        Sets the system hostname.</br>CL default hostname is <code>cumulus</code>.
        </td>      
        <td style="vertical-align : middle">
        <pre>$ nv set system hostname leaf01</pre>
        </td>  
    </tr>
    <tr>
        <td style="vertical-align : middle">
        <code>nv set interface eth0 ip address &lt;ip/mask&gt;</code>
        </td>
        <td rowspan="2" style="vertical-align : middle">
        Configures static IP address and default gateway on the OOB management interface - <em>eth0</em>.</br>By default it is set to use DHCPv4 to obtain an IP address.
        </td>
        <td rowspan="2" style="vertical-align : middle">
        <pre>$ nv set interface eth0 ip address 192.168.200.2/24</br>$ nv set interface eth0 ip gateway 192.168.200.1</pre>
        </td>      
    </tr>
    <tr>
        <td style="vertical-align : middle">
        <code>nv set interface eth0 ip gateway &lt;ipk&gt;</code>
        </td>   
    </tr>
    <tr>    
    <tr>
        <td style="vertical-align : middle">
        <code>nv set service ntp default server &lt;url&gt; iburst on</code>
        </td>
        <td style="vertical-align : middle">
        Adds an <span style="background-color:#F5F5DC"><a><abbr title="Network Time Protocol">NTP</abbr></a></span> server. CL boots with NTP service enabled and default servers set. Check out <a href="/cumulus-linux-53/System-Configuration/Date-and-Time/Network-Time-Protocol-NTP">NTP</a> documentation for more information.</br><code>default</code> is <span style="background-color:#F5F5DC"><a><abbr title="Virtual Routing and Forwarding">VRF</abbr></a></span> name. You must specify a VRF. If you don't use NTP, set system time/date using Linux <code>date</code> command.
        </td>      
        <td style="vertical-align : middle">
        <pre>$ nv set service ntp default server 4.cumulusnetworks.pool.ntp.org iburst on</pre>
        </td>  
    </tr>
    <tr>
        <td style="vertical-align : middle">
        <code>nv set system timezone &lt;timezone&gt;</code>
        </td>
        <td style="vertical-align : middle">
        Configures the system time zone. Cumulus Linux is set with a default <em>UTC</em> (Coordinated Universal Time) time zone.
        </td>      
        <td style="vertical-align : middle">
        <pre>$ nv set system timezone US/Eastern</pre>
        </td>  
    </tr>
    <tr>
        <td style="vertical-align : middle">
        <code>nv set service dns mgmt server &lt;ip&gt;</code>
        </td>
        <td style="vertical-align : middle">
        Configures <span style="background-color:#F5F5DC"><a><abbr title="Domain Name System">DNS</abbr></a></span> lookup server.</br><code>mgmt</code> is the VRF name. You can use this command w/ or w/o VRF.
        </td>      
        <td style="vertical-align : middle">
        <pre>$ nv set service dns mgmt server 198.51.100.31</pre>
        </td>  
    </tr>
    <tr>
        <td style="vertical-align : middle">
        <code>nv set service syslog default server &lt;ip&gt; port &lt;port&gt;</code>
        </td>
        <td rowspan="2" style="vertical-align : middle">
        Configures a remote Syslog server for the switch to send its Syslog messages.</br><code>default</code> is the VRF name. You must specify a VRF.
        </td>
        <td rowspan="2" style="vertical-align : middle">
        <pre>$ nv set service syslog default server 192.168.0.254 port 514
$ nv set service syslog default server 192.168.0.254 protocol udp</pre>
        </td>      
    </tr>
    <tr>
        <td style="vertical-align : middle">
        <code>nv set service syslog default server &lt;ip&gt; protocol &lt;tcp|udp&gt;</code>
        </td>   
    </tr>
</table>

## Working with Interfaces

These commands allow you to configure the physical, breakout, loopback and logical layer 2 and layer 3 interfaces.

### Physical Interfaces

<table style="width:100%">
    <tr >
        <th style="width:32%">
        Command Syntax
        </th>
        <th style="width:36%">
        Command Description
        </th>
        <th style="width:32%">
        Example
        </th>
    </tr>
    <tr>
        <td style="vertical-align : middle" >
        <code>nv set interface &lt;interface&gt;</code>
        </td>
        <td rowspan="2" style="vertical-align : middle">
        Administratively enables physical interface in the system.</br>All physical interfaces are disabled by default (except <em>eth0</em>).</br>Therefore, you must enable them to become operational.</br>To disable an interface, use the <code>nv unset</code> command.</br>You can also enable/disable all (or a range) interfaces at once.
        </td>      
        <td  rowspan="2" style="vertical-align : middle">
        <pre>$ nv set interface swp1</br>$ nv set interface swp1,20-32</pre>
        </td>  
    </tr>
    <tr>
        <td style="vertical-align : middle">
        <code>nv set interface &lt;interfaces-range&gt;</code>
        </td>  
    </tr>
    <tr>
        <td style="vertical-align : middle">
        <code>nv set interface &lt;interface&gt; link state &lt;up|down&gt;</code>
        </td>
        <td style="vertical-align : middle">
        Configures interface link state. Once an interface(/s) is enabled, its link state is automatically set to <code>up</code>.</br><b>Note:</b> Setting the link state to <code>down</code> doesn't disable the interface from the system like the <code>nv unset interface &lt;interface&gt;</code> command.
        </td>      
        <td style="vertical-align : middle">
        <pre>$ nv set interface swp1 link state down</br>$ nv set interface swp8-15 link state up</pre>
        </td>  
    </tr>
     <tr>
        <td style="vertical-align : middle">
        <code>nv set interface &lt;interface&gt; link speed &lt;speed&gt;</code>
        </td>
        <td style="vertical-align : middle">
        Configures interface speed. If auto-negotiation is enabled (it is set by default), it takes precedence over the link speed setting.
        </td>      
        <td style="vertical-align : middle">
        <pre>$ nv set interface swp1 link speed 50G</pre>
        </td>  
    </tr>
    <tr>
        <td style="vertical-align : middle">
        <code>nv set interface &lt;interface&gt; link mtu &lt;mtu&gt;</code>
        </td>
        <td style="vertical-align : middle">
        Configures interfaecs <span style="background-color:#F5F5DC"><a><abbr title="Maximum Transfer Unit">MTU</abbr></a></span>. All ports on CL are set to 9216B MTU by default.
        </td>      
        <td style="vertical-align : middle">
        <pre>$ nv set interface swp1 link mtu 1500</pre>
        </td>  
    </tr>
</table>

### Breakout Interfaces

NVIDIA Spectrum switches allow you to breakout physical interfaces into 2/4 lower speeds ports. By that, you increase the number of ports on the switch.</br>Breakout configurations differ between platforms, check out the <a href="/cumulus-linux-53/Layer-1-and-Switch-Ports/Interface-Configuration-and-Management/Switch-Port-Attributes#breakout-ports">breakout ports</a> section of the <a href="/cumulus-linux-53/Layer-1-and-Switch-Ports/Interface-Configuration-and-Management/Switch-Port-Attributes">switch port attributes</a> documentation for more information.</br>

<table style="width:100%">
    <tr >
        <th style="width:32%">
        Command Syntax
        </th>
        <th style="width:36%">
        Command Description
        </th>
        <th style="width:32%">
        Example
        </th>
    </tr>
    <tr>
        <td style="vertical-align : middle">
        <code>nv set interface &lt;interface&gt; link breakout &lt;breakout-mode&gt;</code>
        </td>
        <td rowspan="2" style="vertical-align : middle">
        Configures the breakout mode on a physical interface.</br>Some platforms require disabling the adjacent port to breakout an interface. Check out this <a href="/knowledge-base/Setup-and-Getting-Started/layer-1-Data-Center-Cheat-Sheet#breakout-ports-configuration">KB</a> article for more information.  
        </td>      
        <td  rowspan="2" style="vertical-align : middle">
        <pre>$ nv set interface swp1 link breakout 4x25G</br>$ nv set interface swp2 link breakout disabled</pre>
        </td>  
    </tr>
    <tr>
        <td style="vertical-align : middle">
        <code>nv set interface &lt;interface&gt; link breakout &lt;disabled&gt;</code>
        </td>
    </tr>
    <tr>
        <td style="vertical-align : middle">
        <code>nv unset interface &lt;breakout-interface&gt;</code>
        </td>
        <td rowspan="2" style="vertical-align : middle">
        Administratively disables the breakout port from the system.</br>When you breakout a physical port, new logical ports are created in the system; for example, when you breakout interface <em>swp1</em> into 4, new ports <em>swp1s0</em>, <em>swp1s1</em>, <em>swp1s2</em>, and <em>swp1s3</em> are created. To remove the breakout configuration from an interface, you must administratively disable all the breakout ports and then &lt;unset&gt; the breakout configuration from the physical interface:
        </td>      
        <td rowspan="2" style="vertical-align : middle">
        <pre>$ nv unset interface swp1s0</br>$ nv unset interface swp1s1</br>$ nv unset interface swp1s2</br>$ nv unset interface swp1s3</br>$ nv unset interface swp1 link breakout</pre>
        </td>  
    </tr>
    <tr>
        <td style="vertical-align : middle">
        <code>nv unset interface &lt;interface&gt; link breakout</code>
        </td>
    </tr>
</table>

### Loopback Interface

Cumulus Linux has a preconfigured loopback interface. When the switch boots up, the loopback interface called <em>lo</em> is <code>up</code> and assigned an IP address of <em>127.0.0.1</em>.

<table style="width:100%">
    <tr >
        <th style="width:32%">
        Command Syntax
        </th>
        <th style="width:36%">
        Command Description
        </th>
        <th style="width:32%">
        Example
        </th>
    </tr>
    <tr>
        <td style="vertical-align : middle" >
        <code>nv set interface lo ip address &lt;ip&gt;</code>
        </td>
        <td style="vertical-align : middle">
        Configures an IP address on the loopback (<em>lo</em>) interface. The loopback interface <b>must</b> always exist and be <code>up</code>. <em>lo</em> doesn't require subnet mask, it automaticaly set wiht <code>/32</code> prefix. You can configure multiple IP addresses for the loopback interface.
        </td>      
        <td style="vertical-align : middle">
        <pre>$ nv set interface lo ip address 10.10.10.1</pre>
        </td>  
    </tr>
</table>

### Layer 2 Interfaces 

All physical interfaces in CL are routed (layer 3) once enabled. To set an interface as switch ports (layer 2), you must add it to a bridge.

#### Bridge and VLANs

CL supports two bridge configuration modes: 
- VLAN-aware bridge
- Traditional bridge 

The default bridge <code>br_default</code> is a VLAN-aware bridge. Check out the <a href="/cumulus-linux-53/Layer-2/Ethernet-Bridging-VLANs">Ethernet Bridging - VLANs documentation for more information.

<table style="width:100%">
    <tr >
        <th style="width:32%">
        Command Syntax
        </th>
        <th style="width:36%">
        Command Description
        </th>
        <th style="width:32%">
        Example
        </th>
    </tr>
    <tr>
        <td style="vertical-align : middle" >
        <code>nv set interface &lt;interface&gt; bridge domain br_default</code>
        </td>
        <td style="vertical-align : middle">
        Adds a physical interface into the default <code>br_default</code> bridge. You can add a range of interfaces to a bridge.</br>When an interface is added to a bridge, it's automatically set to trunk mode (tagged-dot1Q) with all bridge VLANs allowed. 
        </td>      
        <td style="vertical-align : middle">
        <pre>$ nv set interface swp1 bridge domain br_default</br>$ nv set interface swp1-5,7-22 bridge domain br_default</pre>
        </td>  
    </tr>
    <tr>
        <td style="vertical-align : middle" >
        <code>nv set interface &lt;interface&gt; bridge domain br_default untagged none</code>
        </td>
        <td style="vertical-align : middle">
        Configures an interface (<b>not the brdige</b>) to drop all untagged traffic. The <code>untagged none</code> command removes the <span style="background-color:#F5F5DC"><a><abbr title="Primary VLAN Identifier">PVID</abbr></a></span> from the interface.
        </td>      
        <td style="vertical-align : middle">
        <pre>$ nv set interface swp2 bridge domain br_default untagged none</pre>
        </td>  
    </tr>
    <tr>
        <td style="vertical-align : middle" >
        <code>nv set bridge domain br_default vlan &lt;vlan_id&gt;</code>
        </td>
        <td style="vertical-align : middle">
        Configures VLANs on the default <code>br_default</code> bridge. All new VLANs added to the bridge, will automatically be added to all its trunk ports. You can also add VLANs in range or list.
        </td>      
        <td style="vertical-align : middle">
        <pre>$ nv set bridge domain br_default vlan 10,20</pre>
        </td>  
    </tr>
    <tr>
        <td style="vertical-align : middle" >
        <code>nv set interface &lt;interface&gt; bridge domain br_default access &lt;vlan_id&gt;</code>
        </td>
        <td style="vertical-align : middle">
        Configures an interface as an access (untagged) port in a specific VLAN.
        </td>      
        <td style="vertical-align : middle">
        <pre>$ nv set interface swp1 bridge domain br_default access 10</pre>
        </td>  
    </tr>
    <tr>
        <td style="vertical-align : middle" >
        <code>nv set bridge domain br_default untagged &lt;vlan_id&gt;</code>
        </td>
        <td style="vertical-align : middle">
        Configures the PVID of the default <code>br_default</code> bridge. CL defualt PVID is <code>1</code>. You should use this command only to change (or reset) the default PVID. 
        </td>      
        <td style="vertical-align : middle">
        <pre>$ nv set bridge domain br_default untagged 100</pre>
        </td>  
    </tr>
</table>

#### Spanning-Tree Protocol (STP)

The VLAN-aware bridges (e.g. <code>br_default</code>) operate only in <span style="background-color:#F5F5DC"><a><abbr title="Rapid Spanning-Tree Protocol">RSTP</abbr></a></span> mode.
{{%notice note%}}
Traditional bridges operate in both <span style="background-color:#F5F5DC"><a><abbr title="Per-VLAN Spanning-Tree">PVST</abbr></a></span> and <span style="background-color:#F5F5DC"><a><abbr title="Rapid Per-VLAN Spanning-Tree">RPVST</abbr></a></span> modes. The default is PVRST. Each traditional bridge has its own separate STP instance.
{{%/notice%}}

<table style="width:100%">
    <tr >
        <th style="width:32%">
        Command Syntax
        </th>
        <th style="width:36%">
        Command Description
        </th>
        <th style="width:32%">
        Example
        </th>
    </tr>
    <tr>
        <td style="vertical-align : middle" >
        <code>nv set bridge domain br_default stp priority &lt;priority&gt;</code>
        </td>
        <td style="vertical-align : middle">
        Sets the spanning-tree priority of the default <code>br_default</code> bridge. The default STP priority is <em>32768</em>.
        </td>      
        <td style="vertical-align : middle">
        <pre>$ nv set bridge domain br_default stp priority 8192</pre>
        </td>  
    </tr>
    <tr>
        <td style="vertical-align : middle" >
        <code>nv set interface &lt;interface&gt; bridge domain br_default stp admin-edge &lt;on|off&gt;</code>
        </td>
        <td rowspan="3" style="vertical-align : middle">
        Sets an interface to Edge (PortFast) mode. It is recommended to set the <span style="background-color:#F5F5DC"><a><abbr title="Bridge Protocol Data Unit">BPDU</abbr></a></span>-guard on edge ports to eliminate loops.</br>CL enables automatic edge <code>auto-edge</code> port detection by default. You can disable it using the <code>off</code> option.    
        </td>      
        <td rowspan="3" style="vertical-align : middle">
        <pre>$ nv set interface swp5 bridge domain br_default stp admin-edge on</br>$ nv set interface swp5 bridge domain br_default stp bpdu-guard on</br>$ nv set interface swp5 bridge domain br_default stp auto-edge off</pre>
        </td>  
    </tr>
    <tr>
        <td style="vertical-align : middle" >
        <code>nv set interface &lt;interface&gt; bridge domain br_default stp bpdu-guard &lt;on|off&gt;</code>
        </td>
    </tr>
    <tr>
        <td style="vertical-align : middle" >
        <code>nv set interface &lt;interface&gt; bridge domain br_default stp auto-edge &lt;on|off&gt;</code>
        </td>
    </tr>
</table>

Check out the [Spanning Tree and Rapid Spanning Tree - STP]({{<ref "/cumulus-linux-53/Layer-2/Spanning-Tree-and-Rapid-Spanning-Tree">}}) documentation for more information.

### Layer 3 Interfaces

By default, all CL interfaces are routed ports (layer 3) once administratively enabled.

<table style="width:100%">
    <tr >
        <th style="width:32%">
        Command Syntax
        </th>
        <th style="width:36%">
        Command Description
        </th>
        <th style="width:32%">
        Example
        </th>
    </tr>
    <tr>
        <td style="vertical-align : middle" >
        <code>nv set interface &lt;interface&gt; ip address &lt;ipv4|ipv6/mask&gt;</code>
        </td>
        <td style="vertical-align : middle">
        Configures an IPv4/6 address on the physical (<em>swp</em>) interface. 
        </td>      
        <td style="vertical-align : middle">
        <pre>$ nv set interface swp10 ip address 10.1.0.5/24</br>$ nv set interface swp10 ip address 2001:db8::10/64</pre>
        </td>  
    </tr>
    <tr>
        <td style="vertical-align : middle" >
        <code>nv set interface &lt;svi&gt; ip address &lt;ipv4|ipv6/mask&gt;</code>
        </td>
        <td style="vertical-align : middle">
        Configures an IPv4/6 address on <span style="background-color:#F5F5DC"><a><abbr title="Switch Virtual Interface">SVI</abbr></a></span> (VLAN interface).</br>SVI will operate only if its VLAN exist and an interface is assigned to it (either tagged/untagged). 
        </td>      
        <td style="vertical-align : middle">
        <pre>$ nv set interface vlan100 ip address 100.1.0.2/24</br>$ nv set interface vlan100 ip address 2001:db8::1/32</pre>
        </td>  
    </tr>
</table>


### Link Aggregation (LAG) Interfaces

The LAG interface on CL is called a <em>bond</em>. Bonds can be set as layer 2 or layer 3 interfaces.

<table style="width:100%">
    <tr >
        <th style="width:32%">
        Command Syntax
        </th>
        <th style="width:36%">
        Command Description
        </th>
        <th style="width:32%">
        Example
        </th>
    </tr>
    <tr>
        <td style="vertical-align : middle" >
        <code>nv set interface &lt;bond-name&gt; bond member &lt;bonded-interfaces&gt;</code>
        </td>
        <td rowspan="2" style="vertical-align : middle">
        Configures bond interface and sets physical ports to it. If you use a bond name that starts with <code>bond</code> its type will automatically be set to <code>bond</code>. Otherwise, you will have to manually set the interface type to <code>bond</code>.  
        </td>      
        <td rowspan="2" style="vertical-align : middle">
        <pre>$ nv set interface bond1 bond members swp1-4</br>$ nv set interface lag1 bond members swp5-6</br>$ nv set interface lag1 type bond</pre>
        </td>  
    </tr>
    <tr>
        <td style="vertical-align : middle" >
        <code>nv set interface &lt;bond-name&gt; type bond</code>
        </td>
    </tr>
    <tr>
        <td style="vertical-align : middle" >
        <code>nv set interface &lt;bond-name&gt; bond mode &lt;static|lacp&gt;</code>
        </td>
        <td style="vertical-align : middle">
        Configures bond interface operation mode.</br>By default, bonds on CL are set to <span style="background-color:#F5F5DC"><a><abbr title="Link Aggregation Control Protocol">LACP</abbr></a></span> (802.3ad) mode.</br>You can change it to Balance-xor mode using the <code>static</code> mode. To reset the bond mode to LACP, use the <code>lcap</code> mode. 
        </td>      
        <td style="vertical-align : middle">
        <pre>$ nv set interface bond1 bond mode static</br>$ nv set interface bond1 bond mode lacp</pre>
        </td>  
    </tr>
    <tr>
        <td style="vertical-align : middle" >
        <code>nv set interface &lt;bond-name&gt; bond lacp-rate &lt;fast|slow&gt;</code>
        </td>
        <td style="vertical-align : middle">
        Configures bond interface LACP <span style="background-color:#F5F5DC"><a><abbr title="Protocl Data Unit">PDU</abbr></a></span> transmit rate.</br>By default, bonds on CL are set to <code>fast</code> mode (every 3s). To set the rate to 30s, use the <code>slow</code> mode. 
        </td>      
        <td style="vertical-align : middle">
        <pre>$ nv set interface bond1 bond lacp-rate slow</br>$ nv set interface bond1 bond lacp-rate fast</pre>
        </td>  
    </tr>
</table>

## Working with Network Protocols

This cheat sheet covers some of the basic configuration commands of the main data center protocols. You can check out the [Cumulus Linux User Guide]({{<ref "/cumulus-linux-53">}}) for other protocols, configuration commands, examples, and more detailed information.

### Layer 2 Protocols

#### Multi-Chassis Link Aggregation - MLAG

MLAG provides layer 2 redundancy and greater system throughput. To set MLAG on CL switches, you must fulfill these requirements:

 - Only two switches can share MLAG configuration. But you can have multiple (different) MLAG pairs in the network.
 - Both MLAG peer switches must be directly connected. This is typically a bond for increased reliability and bandwidth.
 - Both switches in the MLAG pair must be of the same Spectrum model and run the same CL version.
 - The dual-connected devices (servers or switches) can use LACP or static bond modes. MLAG switches must be set accordingly.

This cheat sheet covers the basic MLAG configuration commands. Check out the [Multi-Chassis Link Aggregation - MLAG]({{<ref "/cumulus-linux-53/Layer-2/Multi-Chassis-Link-Aggregation-MLAG">}}) documentation for more information.

<table style="width:100%">
    <tr >
        <th style="width:32%">
        Command Syntax
        </th>
        <th style="width:36%">
        Command Description
        </th>
        <th style="width:32%">
        Example
        </th>
    </tr>
    <tr>
        <td style="vertical-align : middle" >
        <code>nv set interface &lt;bond-name&gt; bond member &lt;bonded-interfaces&gt;</code>
        </td>
        <td style="vertical-align : middle">
        Configures bond interface and sets physical ports to it. You must create a bond interface so that it will be set as an MLAG port.
        </td>      
        <td style="vertical-align : middle">
        <pre>$ nv set interface bond1 bond members swp1</pre>
        </td>  
    </tr>
    <tr>
        <td style="vertical-align : middle" >
        <code>nv set interface &lt;bond-name&gt; bond mlag id &lt;mlag-id&gt;</code>
        </td>
        <td style="vertical-align : middle">
        Sets the MLAG ID of the bond interface. You must specify a unique MLAG ID for every dual-connected bond on each peer switch. The value must be identical on both MLAG peers.
        </td>      
        <td style="vertical-align : middle">
        <pre>$ nv set interface bond1 bond mlag id 1</pre>
        </td>  
    </tr>
    <tr>
        <td style="vertical-align : middle" >
        <code>nv set interface &lt;bond-name&gt; bridge domain br_default</code>
        </td>
        <td style="vertical-align : middle">
        Sets the MLAG port into the default bridge <code>br_default</code>.
        </td>      
        <td style="vertical-align : middle">
        <pre>$ nv set interface bond1 bridge domain br_default</pre>
        </td>  
    </tr>
    <tr>
        <td style="vertical-align : middle" >
        <code>nv set interface peerlink bond member &lt;bonded-interfaces&gt;</code>
        </td>
        <td style="vertical-align : middle">
        Configures the inter-chassis bond for MLAG operation. <code>peerlink</code> is a reserved name for the inter-chassis link. When <code>peerlink</code> is created, a layer 3 sub-interface <em>peerlink.4094</em> is created automatically to ensure VLAN-independent operation on this link. 
        </td>      
        <td style="vertical-align : middle">
        <pre>$ nv set interface peerlink bond member swp31-32</pre>
        </td>  
    </tr>
    <tr>
        <td style="vertical-align : middle" >
        <code>nv set mlag mac-address &lt;mac&gt;</code>
        </td>
        <td style="vertical-align : middle">
        Configures the MLAG system MAC address which will be set in all control protocols PDU to represent the MLAG pair as a single switch. MLAG MAC must be identical on both MLAG peers but unique in the network and different between MLAG pairs (CL provides a special reserved range).
        </td>      
        <td style="vertical-align : middle">
        <pre>$ nv set mlag mac-address 44:38:39:BE:EF:AA</pre>
        </td>  
    </tr>
    <tr>
        <td style="vertical-align : middle" >
        <code>nv set mlag peer-ip linklocal</code>
        </td>
        <td style="vertical-align : middle">
        Configures the MLAG peer address. The peer-IP is based on the <em>peerlink.4094</em> link-local addresses (point-to-point).
        </td>      
        <td style="vertical-align : middle">
        <pre>$ nv set mlag peer-ip linklocal</pre>
        </td>  
    </tr>
    <tr>
        <td style="vertical-align : middle" >
        <code>nv set mlag backup &lt;ip&gt; [&lt;vrf&gt;]</code>
        </td>
        <td style="vertical-align : middle">
        Configures the MLAG backup IP address which is used to communicate between MLAG peers in case the <em>peerlink</em> goes down. You can specify the backup IP in a specific VRF if needed.
        </td>      
        <td style="vertical-align : middle">
        <pre>$ nv set mlag backup 10.10.10.2 vrf mgmt</pre>
        </td>  
    </tr>
</table>

#### Virtual Router Redundancy - VRR

<span style="background-color:#F5F5DC"> [VRR](## "Virtual Router Redundancy")</span> enables an active-active gateway for the layer 2 MLAG domain. Both MLAG peers must have an SVI with unique IP addresses for each VLAN. Then, VRR instances (instance per subnet) must be identically set on both MLAG peers. VRR instance is configured on the SVIs and holds virtual IP and MAC addresses. Hence, both peers respond to ARP requests from the host; but if one fails, the second still serves as the gateway.

<table style="width:100%">
    <tr >
        <th style="width:32%">
        Command Syntax
        </th>
        <th style="width:36%">
        Command Description
        </th>
        <th style="width:32%">
        Example
        </th>
    </tr>
    <tr>
        <td style="vertical-align : middle" >
        <code>nv set interface &lt;svi&gt; ip vrr address &lt;ip&gt;</code>
        </td>
        <td style="vertical-align : middle">
        Configures the virtual IP address of the VRR instance. This address must be within the SVI subnet.
        </td>      
        <td style="vertical-align : middle">
        <pre>$ nv set interface vlan10 ip vrr address 10.1.10.1/24</pre>
        </td>  
    </tr>
    <tr>
        <td style="vertical-align : middle" >
        <code>nv set system global fabric-mac &lt;mac&gt;</code>
        </td>
        <td rowspan="2" style="vertical-align : middle">
        Configures the global fabric MAC address to ensure fabric-wide MAC consistency across VRR switches. It is primarily used for multi-fabric EVPN environments. CL has default VRR MAC address <code>00:00:5E:00:01:01</code>, so you can either change it globally or by changing the default fabric ID (<em>fabric_id=1</em>), which is added to the MAC address.
        </td>      
        <td rowspan="2" style="vertical-align : middle">
        <pre>$ nv set system global fabric-mac 00:00:5E:00:01:FF</br>$ nv set system global fabric-id 255</pre>
        </td>  
    </tr>
    <tr>
        <td style="vertical-align : middle" >
        <code>nv set system global fabric-id &lt;id&gt;</code>
        </td>
    </tr>
    <tr>
        <td style="vertical-align : middle" >
        <code>nv set interface &lt;svi&gt; ip vrr mac-address &lt;mac&gt;</code>
        </td>
        <td style="vertical-align : middle">
        Configures the VRR instance virtual MAC address for a specific VLAN (in case you want to override the global default settings).  
        </td>      
        <td style="vertical-align : middle">
        <pre>$ nv set interface vlan10 ip vrr mac-address 00:00:5E:00:01:00</pre>
        </td>  
    </tr>
</table>

Check out the [Virtual Router Redundancy - VRR and VRRP]({{<ref "/cumulus-linux-53/Layer-2/Virtual-Router-Redundancy-VRR-and-VRRP">}}) documentation for more information.

### Layer 3 Protocols

#### Virtual Routing and Forwarding - VRF

<span style="background-color:#F5F5DC"> [VRF](## "Virtual Routing and Forwarding")</span> (aka <em>VRF-Lite</em>) enables you to use multiple independent routing tables that work simultaneously on the same switch (e.g. in multi-tenant environments).

Here are the basic commands to use VRFs. Check out the [Virtual Routing and Forwarding - VRF]({{<ref "/cumulus-linux-53/Layer-3/VRFs/Virtual-Routing-and-Forwarding-VRF">}}) and [Management VRF]({{<ref "/cumulus-linux-53/Layer-3/VRFs/Management-VRF">}}) documentation for more information about the usage of custom and mgmt. VRFs with diffeernt protocols. 

<table style="width:100%">
    <tr >
        <th style="width:32%">
        Command Syntax
        </th>
        <th style="width:36%">
        Command Description
        </th>
        <th style="width:32%">
        Example
        </th>
    </tr>
    <tr>
        <td style="vertical-align : middle" >
        <code>nv set vrf &lt;name&gt; table &lt;auto|id&gt;</code>
        </td>
        <td style="vertical-align : middle">
        Configures a new VRF and assigns a table ID. You can use the <code>auto</code> table assignment or set the ID manually (<b>must</b> be between <em>1001-1255</em>.
        </td>      
        <td style="vertical-align : middle">
        <pre>$ nv set vrf BLUE table auto</br>$ nv set vrf RED table 1016</pre>
        </td>  
    </tr>
    <tr>
        <td style="vertical-align : middle" >
        <code>nv set interface &lt;interface&gt; ip vrf &lt;name&gt;</code>
        </td>
        <td style="vertical-align : middle">
        Adds a layer 3 interface into a VRF.
        </td>      
        <td style="vertical-align : middle">
        <pre>$ nv set interface swp1 ip vrf BLUE</pre>
        </td>  
    </tr>
</table>

#### Static Routing

add blablabla

<table style="width:100%">
    <tr >
        <th style="width:32%">
        Command Syntax
        </th>
        <th style="width:36%">
        Command Description
        </th>
        <th style="width:32%">
        Example
        </th>
    </tr>
    <tr>
        <td style="vertical-align : middle" >
        <code>nv set vrf &lt;name&gt; router static &lt;ip/mask&gt; via &lt;ip&gt;</code>
        </td>
        <td rowspan="2" style="vertical-align : middle">
        Configures a static route to a destination network via a specified next hop within a VRF. You must have a local IP address within the next-hop subnet.
        </td>      
        <td rowspan="2" style="vertical-align : middle">
        <pre>$ nv set vrf default router static 10.10.10.101/32 via 10.0.1.1</pre>
        </td>  
    </tr>
</table>

#### Border Gateway Protocol - BGP

<span style="background-color:#F5F5DC"> [BGP](## "Border Gateway Protocol")</span> is the routing protocol that runs the Internet. It manages how packets get routed from network to network by exchanging routing and reachability information.

CL brings simplicity into the data center BGP configuration using the [Auto BGP]({{<ref "/cumulus-linux-53/Layer-3/Border-Gateway-Protocol-BGP#auto-bgp">}}) and the 
[BGP Unnumbered]({{<ref "/cumulus-linux-53/Layer-3/Border-Gateway-Protocol-BGP#bgp-unnumbered">}}) capabilities. NVIDIA recommends using these features to eliminate the need for <span style="background-color:#F5F5DC"> [ASN](## "Autonomous System Number")</span> and point-to-point IP addressing assignments and reduce human errors.

This cheat sheet covers the basic BGP configuration. Check out the [Border Gateway Protocol - BGP]({{<ref "/cumulus-linux-53/Layer-3/Border-Gateway-Protocol-BGP">}}) documentation for more information.

<table style="width:100%">
    <tr >
        <th style="width:32%">
        Command Syntax
        </th>
        <th style="width:36%">
        Command Description
        </th>
        <th style="width:32%">
        Example
        </th>
    </tr>
    <tr>
        <td style="vertical-align : middle" >
        <code>nv set router bgp autonomous-system &lt;leaf|spine|asn&gt;</code>
        </td>
        <td style="vertical-align : middle">
        Configures router BGP with an ASN. You can use the auto BGP <code>leaf</code> or <code>spine</code> keywords to let CL set the ASN, or set a number.
        </td>      
        <td style="vertical-align : middle">
        <pre>$ nv set router bgp autonomous-system 65101</br>$ nv set router bgp autonomous-system leaf</pre>
        </td>  
    </tr>
    <tr>
        <td style="vertical-align : middle" >
        <code>nv set router bgp router-id &lt;ip&gt;</code>
        </td>
        <td  rowspan="2" style="vertical-align : middle">
        Configures the BGP router-id. By default, BGP assigns the loopback IP address as the router-id. But if you don't have a loopback set or you want to override this setting, you need to set it manually. You can set the router-id globally or per VRF.
        </td>      
        <td  rowspan="2" style="vertical-align : middle">
        <pre>$ nv set router bgp router-id 10.10.10.1</br>$ nv set vrf RED router bgp router-id 10.10.10.1</pre>
        </td>  
    </tr>
    <tr>
        <td style="vertical-align : middle" >
        <code>nv set vrf &lt;name&gt; router bgp router-id &lt;ip&gt;</code>
        </td>  
    </tr>
    <tr>
        <td style="vertical-align : middle" >
        <code>nv set vrf default router bgp neighbor &lt;ipv4|ipv6|interface&gt; remote-as &lt;internal|external&gt;</code>
        </td>
        <td style="vertical-align : middle">
        Configures BGP neighbor peering. You can set the neighbor as <code>internal</code> for iBGP or <code>external</code> eBGP. <code>default</code> is the VRF name. You must set the neighbors in this VRF.
        </td>      
        <td style="vertical-align : middle">
        <pre>$ nv set vrf default router bgp neighbor 10.0.1.1 remote-as internal</br>$ nv set vrf default router bgp neighbor swp2 remote-as external</br>$ nv set vrf default router bgp neighbor 2001:db8:0002::0a00:0002 remote-as external</pre>
        </td>  
    </tr>
    <tr>
        <td style="vertical-align : middle" >
        <code>nv set vrf default router bgp neighbor &lt;ipv4|ipv6|interface&gt; address-family ipv6-unicast enable on</code>
        </td>
        <td style="vertical-align : middle">
        Enables IPv6 prefixes advertisement. CL enables the IPv4 address-family by default. But to advertise IPv6 routes, you need to enable the IPv6 <span style="background-color:#F5F5DC"><a><abbr title="Address-Family">AF</abbr></a></span>. To advertise IPv4 prefixes with Ipv6 next hops, see <a href="/cumulus-linux-53/Layer-3/Border-Gateway-Protocol-BGP/Optional-BGP-Configuration#advertise-ipv4-prefixes-with-ipv6-next-hops">Advertise IPv4 Prefixes with IPv6 Next Hops</a>.
        </td>      
        <td style="vertical-align : middle">
        <pre>$ nv set vrf default router bgp neighbor 2001:db8:0002::0a00:0002 address-family ipv4-unicast enable on</pre>
        </td>  
    </tr>
    <tr>
        <td style="vertical-align : middle" >
        <code>nv set vrf default router bgp address-family &lt;ipv4-unicast|ipv6-unicast&gt; network &lt;ipv4|ipv6/mask&gt;</code>
        </td>
        <td style="vertical-align : middle">
        Specifies which prefixes to originate.
        </td>      
        <td style="vertical-align : middle">
        <pre>$ nv set vrf default router bgp address-family ipv4-unicast network 10.1.10.0/24</br>$ nv set vrf default router bgp address-family ipv6-unicast network 2001:db8::1/128</pre>
        </td>  
    </tr>
    <tr>
        <td style="vertical-align : middle" >
        <code>nv set vrf &lt;name&gt; router bgp address-family &lt;ipv4-unicast|ipv6-unicast&gt; redistribute &lt;connected|static|ospf(6)&gt; enable &lt;on|off&gt;</code>
        </td>
        <td style="vertical-align : middle">
        Redistributes prefixes into the IPv4/IPv6 AF. Route redistribution can also be used with route-map filtering using the <code>route-map &lt;name&gt;</code> and BGP metric setting <code>metric &lt;auto|value&gt;</code> options. See <a href="/cumulus-linux-53/Layer-3/Routing/Route-Filtering-and-Redistribution">Route Filtering and Redistribution</a> for more information.
        </td>      
        <td style="vertical-align : middle">
        <pre>$ nv set vrf default router bgp address-family ipv4-unicast redistribute static enable on</br>$ nv set vrf default router bgp address-family ipv6-unicast redistribute connected route-map routemap1</pre>
        </td>  
    </tr>
</table>

### Network Virtualization

<span style="background-color:#F5F5DC"> [VXLAN](## "Virtual Extensible LAN")</span> is a standard overlay protocol for logical virtual networks. It uses a VLAN-like encapsulation technique to encapsulate layer 2 Ethernet segments over the layer 3 networks. The encapsulation happens on the  <span style="background-color:#F5F5DC"> [VTEP](## "VXLAN Tunnel End Points")</span> which establish an overlay UDP tunnel to the remote VTEP device. Unlike VLANs, VXLAN scales to 16 million segments - a 24-bit VXLAN network identifier (VNI ID) in the VXLAN header - for multi-tenancy. Check out the [Network Virtualization]({{<ref "/cumulus-linux-53/Network-Virtualization">}}) documentation for more information.

#### VXLAN Devices and Static Tunnels

CL supports single and traditional VXLAN devices. NVUE allows you to work only with a single VXLAN device (single VTEP) and it must be set in a VLAN-aware bridge mode only.
With a single VXLAN device (<span style="background-color:#F5F5DC">[NVE](## "Network Virtual Interface")</span> interface), you specify a VLAN to <span style="background-color:#F5F5DC"> [VNI](## "Virtual Network Identifier")</span> mapping. 

{{%notice note %}}
CL supports multiple single VXLAN devices when set with multiple VLAN-aware bridges. But, make sure not to duplicate VNIs across devices.
{{%/notice %}}

This cheat sheet covers some of the basic configuration commands for static VXLAN tunnels. Check out the [Network Virtualization]({{<ref "/cumulus-linux-53/Network-Virtualization">}}) documentation for more information and extra configuration.

<table style="width:100%">
    <tr >
        <th style="width:32%">
        Command Syntax
        </th>
        <th style="width:36%">
        Command Description
        </th>
        <th style="width:32%">
        Example
        </th>
    </tr>
    <tr>
        <td style="vertical-align : middle" >
        <code>nv set bridge domain br_default vlan &lt;vlan_id&gt; vni &lt;vni_id&gt;</code>
        </td>
        <td style="vertical-align : middle">
        Maps the VLAN to VNI, creates and adds the VXLAN device (NVE) to the bridge. The single VXLAN device name in CL is <em>vxlan48</em>. 
        </td>      
        <td style="vertical-align : middle">
        <pre>$ nv set bridge domain br_default vlan 10 vni 10</pre>
        </td>  
    </tr>
    <tr>
        <td style="vertical-align : middle" >
        <code>nv set bridge domain br_default vlan &lt;vlan_id&gt; vni auto</code>
        </td>
        <td style="vertical-align : middle">
        Automatically maps VLAN to VNI to simplify configuration. You can configure auto VNI mapping also on a VLAN range or list. Automatic VLAN-VNI mapping works only on EVPN fabrics.
        </td>      
        <td style="vertical-align : middle">
        <pre>$ nv set bridge domain br_default vlan 10,20,30,40,50 vni auto</pre>
        </td>  
    </tr>
    <tr>
        <td style="vertical-align : middle" >
        <code>nv set bridge domain br_default vlan-vni-offset &lt;value&gt;</code>
        </td>
        <td style="vertical-align : middle">
        Automatically maps VLAN to VNI with a value offset.
        </td>      
        <td style="vertical-align : middle">
        <pre>$ nv set bridge domain br_default vlan-vni-offset 10000</pre>
        </td>  
    </tr>
    <tr>
        <td style="vertical-align : middle" >
        <code>nv set nve vxlan mac-learning &lt;on|off&gt;</code>
        </td>
        <td style="vertical-align : middle">
        Enables MAC learning on the NVE device. You must set this command for non-EVPN fabrics. MAC learning can be set globally for all VNIs or per VNI (using the bridge command).
        </td>      
        <td style="vertical-align : middle">
        <pre>$ nv set nve vxlan mac-learning on</br>nv set bridge domain br_default vlan 10 vni 10 mac-learning on</pre>
        </td>  
    </tr>
    <tr>
        <td style="vertical-align : middle" >
        <code>nv set nve vxlan arp-nd-suppress &lt;on|off&gt;</code>
        </td>
        <td style="vertical-align : middle">
        Enables the NVE to reply to local ARP requests if it has the remote MAC already. This prevents unnecessary broadcast traffic to all remote VTEPs.
        </td>      
        <td style="vertical-align : middle">
        <pre>$ nv set nve vxlan arp-nd-suppress on</pre>
        </td>  
    </tr>
    <tr>
        <td style="vertical-align : middle" >
        <code>nv set nve vxlan source address &lt;ip&gt;</code>
        </td>
        <td style="vertical-align : middle">
        Configures the VTEP (NVE) source IP address to form the overlay tunnel. A loopback IP address is used for the tunnel source. 
        </td>      
        <td style="vertical-align : middle">
        <pre>$ nv set nve vxlan source address 10.10.10.1</pre>
        </td>  
    </tr>
    <tr>
        <td style="vertical-align : middle" >
        <code>nv set nve vxlan mlag shared-address &lt;ip&gt;</code>
        </td>
        <td style="vertical-align : middle">
        Configures the MLAG anycast virtual IP address that will be used as the VXLAN tunnel destination. Both MLAG peers must have the same address
        </td>      
        <td style="vertical-align : middle">
        <pre>$ nv set nve vxlan mlag shared-address 10.0.1.34</pre>
        </td>  
    </tr>
    <tr>
        <td style="vertical-align : middle" >
        <code>nv set bridge domain br_default vlan &lt;vlan_id&gt; vni &lt;vni_id&gt; flooding head-end-replication &lt;ip&gt;</code>
        </td>
        <td rowspan="2" style="vertical-align : middle">
        Configures the remote VTEP/s for <span style="background-color:#F5F5DC"><a><abbr title="Head End Replication">HER</abbr></a></span> to handle <span style="background-color:#F5F5DC"><a><abbr title="Broadcast, Unknown-Unicast and Multicast">BUM</abbr></a></span> traffic. You must configure the remote VTEPs in non-EVPN fabrics. You can set the remote VTEP per VNI or globally for all VNIs.
        </td>      
        <td rowspan="2" style="vertical-align : middle">
        <pre>$ nv set bridge domain br_default vlan 10 vni 10 flooding head-end-replication 10.10.10.2</br>$ nv set nve vxlan flooding head-end-replication 10.10.10.2</pre>
        </td>  
    </tr>
    <tr>
        <td style="vertical-align : middle" >
        <code>nv set nve vxlan flooding head-end-replication &lt;ip&gt;</code>
        </td>
    </tr>
    <tr>
        <td style="vertical-align : middle" >
        <code>nv set bridge domain br_default vlan &lt;vlan_id&gt; vni &lt;vni_id&gt; flooding multicast-group &lt;ip&gt;</code>
        </td>
        <td rowspan="2" style="vertical-align : middle">
        Configures the multicast group for BUM traffic handling for EVPN fabrics (HER is the default). You can set the flooding group per VNI or globally. NVIDIA recommends setting a unique multicast group per VNI. This configuration requires using PIM-SM on the underlay network.</br>Check out <a href="/cumulus-linux-53/Network-Virtualization/Ethernet-Virtual-Private-Network-EVPN/EVPN-PIM">EVPN BUM Traffic with PIM-SM</a> for more information.
        </td>      
        <td rowspan="2" style="vertical-align : middle">
        <pre>$ nv set bridge domain br_default vlan 10 vni 10 flooding multicast-group 239.1.1.110</br>$ nv set nve vxlan flooding multicast-group 224.0.0.10</pre>
        </td>  
    </tr>
    <tr>
        <td style="vertical-align : middle" >
        <code>nv set nve vxlan flooding multicast-group &lt;ip&gt;</code>
        </td>
    </tr>
</table>

#### Ethernet Virtual Private Network - EVPN

<span style="background-color:#F5F5DC"> [EVPN](## "Ethernet Virtual Private Network")</span> is a standards-based control plane that relies on multi-protocol BGP (MP-BGP) and allows for building and deploying VXLANs at scale. EVPN enables intra-subnet bridging and inter-subnet routing including multi-tenancy support. 

This cheat sheet covers the basic EVPN configuration commands. Check out the [Ethernet Virtual Private Network - EVPN]({{<ref "/cumulus-linux-53/Network-Virtualization/Ethernet-Virtual-Private-Network-EVPN">}}) documentation for more information and extra configuration.

<table style="width:100%">
    <tr >
        <th style="width:32%">
        Command Syntax
        </th>
        <th style="width:36%">
        Command Description
        </th>
        <th style="width:32%">
        Example
        </th>
    </tr>
    <tr>
        <td style="vertical-align : middle" >
        <code>nv set evpn enable &lt;on|off&gt;</code>
        </td>
        <td style="vertical-align : middle">
        Enables the EVPN capabilities globally on the switch. You don't have to enable EVPN per VRF, it's automatically set.
        </td>      
        <td style="vertical-align : middle">
        <pre>$ nv set evpn enable on</pre>
        </td>  
    </tr>
    <tr>
        <td style="vertical-align : middle" >
        <code>nv set vrf default router bgp neighbor &lt;ip|interface&gt; address-family l2vpn-evpn enable &lt;on|off&gt;</code>
        </td>
        <td style="vertical-align : middle">
        Activates the EVPN AF between BGP neighbors. You need to set the EVPN neighbors in the <code>default</code> VRF.
        </td>      
        <td style="vertical-align : middle">
        <pre>$ nv set vrf default router bgp neighbor swp51 address-family l2vpn-evpn enable on</pre>
        </td>  
    </tr>
    <tr>
        <td style="vertical-align : middle" >
        <code>nv set evpn route-advertise default-gateway on &lt;on|off&gt;</code>
        </td>
        <td style="vertical-align : middle">
        Enables default-gateway advertisement into EVPN when using EVPN <a href="/cumulus-linux-53/Network-Virtualization/Ethernet-Virtual-Private-Network-EVPN/Inter-subnet-Routing#centralized-routing">Centralized Routing</a> mode. You can set this per VNI, but NVIDIA recommends setting it globally.
        </td>      
        <td style="vertical-align : middle">
        <pre>$ nv set evpn route-advertise default-gateway on</pre>
        </td>  
    </tr>
    <tr>
        <td style="vertical-align : middle" >
        <code>nv set vrf &lt;name&gt; evpn vni &lt;vni_id&gt;</code>
        </td>
        <td style="vertical-align : middle">
        Creates the L3VNI for a tenant VRF when using EVPN <a href="/cumulus-linux-53/Network-Virtualization/Ethernet-Virtual-Private-Network-EVPN/Inter-subnet-Routing#symmetric-routing">Symmetric Routing</a> mode. First, make sure to create the tenant VRF and add an SVI to it.
        </td>      
        <td style="vertical-align : middle">
        <pre>$ nv set vrf RED vni 4001</pre>
        </td> 
    </tr>
    <tr>
        <td style="vertical-align : middle" >
        <code>nv set vrf &lt;name&gt; router bgp address-family ipv4-unicast route-export to-evpn enable &lt;on|off&gt;</code>
        </td>
        <td style="vertical-align : middle">
        Enables the switch to install EVPN type-5 routes from the VRF BGP RIB. First, make sure to create the tenant VRF and set the L3VNI to it.
        </td>      
        <td style="vertical-align : middle">
        <pre>$ nv set vrf RED router bgp address-family ipv4-unicast route-export to-evpn enable on</pre>
        </td>  
    </tr>
    <tr>
        <td style="vertical-align : middle" >
        <code>nv set evpn multihoming enable &lt;on|off&gt;</code>
        </td>
        <td style="vertical-align : middle">
        Enables <a href="/cumulus-linux-53/Network-Virtualization/Ethernet-Virtual-Private-Network-EVPN/EVPN-Multihoming">EVPN Multihoming</a> (EVPN-MH) capability on the switch.
        </td>      
        <td style="vertical-align : middle">
        <pre>$ nv set evpn multihoming enable on</pre>
        </td>  
    </tr>
    <tr>
        <td style="vertical-align : middle" >
        <code>nv set interface &lt;bond-name&gt; evpn multihoming segment local-id &lt;id&gt;</code>
        </td>
        <td style="vertical-align : middle">
        Configures the EVPN-MH <span style="background-color:#F5F5DC"><a><abbr title="Ethernet Segment Identifier">ESI</abbr></a></span> on the bond interface. Each <span style="background-color:#F5F5DC"><a><abbr title="Ethernet Segment">ES</abbr></a></span> must have the same ESI accross fabric. You must set a unique ESI per bond interface on the switch. 
        </td>      
        <td style="vertical-align : middle">
        <pre>$ nv set interface bond2 evpn multihoming segment local-id 2</pre>
        </td>  
    </tr>
    <tr>
        <td style="vertical-align : middle" >
        <code>nv set interface &lt;bond-name&gt; evpn multihoming segment mac-address &lt;mac&gt;</code>
        </td>
        <td style="vertical-align : middle">
        Configures the EVPN-MH ES MAC address per bond interface. The ES MAC and the ESI generates a unique EVPN type 3 route. ES MAC must be the same on all interfaces toward the same server.
        </td>      
        <td style="vertical-align : middle">
        <pre>$ nv set interface bond1 evpn multihoming segment mac-address 44:38:39:BE:EF:AA</pre>
        </td>  
    </tr>
    <tr>
        <td style="vertical-align : middle" >
        <code>nv set interface &lt;bond-name&gt; evpn multihoming segment df-preference &lt;value&gt;</code>
        </td>
        <td style="vertical-align : middle">
        Configures the EVPN-MH ES <span style="background-color:#F5F5DC"><a><abbr title="Designated Frowarder">DF</abbr></a></span>. The DF handles the flooded traffic received through the VXLAN tunnels to the local ES. The default DF value is <em>32767</em>. NVIDIA recommends setting DF preference to avoid unpredictable failure scenarios.
        </td>      
        <td style="vertical-align : middle">
        <pre>$ nv set interface bond1 evpn multihoming segment df-preference 50000</pre>
        </td>  
    </tr> 
    <tr>
        <td style="vertical-align : middle" >
        <code>nv set interface &lt;interface&gt; evpn multihoming uplink &lt;on|off&gt;</code>
        </td>
        <td style="vertical-align : middle">
        Configures the EVPN-MH uplink ports. When all ES uplink ports go down, all bonds enter an error-disabled state to prevent active MH bonds without VXLAN overlay tunnels.
        </td>      
        <td style="vertical-align : middle">
        <pre>$ nv set interface swp51-54 evpn multihoming uplink on</pre>
        </td>  
    </tr>                
</table>

Check out these [Configuration Examples]({{<ref "/cumulus-linux-53/Network-Virtualization/Ethernet-Virtual-Private-Network-EVPN/Configuration-Examples">}}) of EVPN layer 2 extensions, centralized and symmetric routing use cases. Here you can check out the [EVPN-MH]({{<ref "/cumulus-linux-53/Network-Virtualization/Ethernet-Virtual-Private-Network-EVPN/EVPN-Multihoming#configuration-example">}}) configuration example.

You can also examine and try the EVPN best practices using our pre-built simulations in [Air Marketplace](https://air.nvidia.com/marketplace):
- [EVPN L2 Extension](https://air.nvidia.com/marketplace?demo_id=18e96902-48a0-4bf9-9cf7-23852fbe72c5) 
- [EVPN Centralized Routing](https://air.nvidia.com/marketplace?demo_id=4a7f8342-9efa-446b-a58d-11c2c8bc94dc)
- [EVPN Symmetric Routing](https://air.nvidia.com/marketplace?demo_id=d2b854ae-12ed-4a9a-82b5-49863d3fb37c)
- [EVPN Multihoming](https://air.nvidia.com/marketplace?demo_id=f12bb2ac-55ef-4b61-a6fa-10613d9dbbd2)

## Access Control List - ACL

<span style="background-color:#F5F5DC"> [ACLs](## "Access Control Lists")</span> in CL are based on Linux <em>iptables</em> and <em>ebtables</em> with the following default behaviors:

- There is no <em>implicit deny</em>. ACLs must end in a <em>match any</em> and <em>action deny</em> rule to drop all unmatched traffic.
- There is no support for wildcard masks. You must list subnets individually.

{{%notice note%}}
In addition to NVUE commands, you can configure ACLs straight by setting the <em>ebtables</em> and <em>iptables</em> rules. You can also use the built-in ACL management tool - <em>cl-acltool</em>.</br>For more information and details, refer to the [Netfilter - ACLs]({{<ref "/cumulus-linux-53/System-Configuration/Netfilter-ACLs">}}) documentation.
{{%/notice%}}

<table style="width:100%">
    <tr >
        <th style="width:32%">
        Command Syntax
        </th>
        <th style="width:36%">
        Command Description
        </th>
        <th style="width:32%">
        Example
        </th>
    </tr>
    <tr>
        <td style="vertical-align : middle" >
        <code>nv set acl &lt;name&gt; type &lt;ipv4|ipv6|mac&gt;</code>
        </td>
        <td style="vertical-align : middle">
        Creates an IPv4/IPv6/MAC access-list. The ACL <code>type</code> must be set to create it.
        </td>      
        <td style="vertical-align : middle">
        <pre>$ nv set acl DENY_TCP_HTTP type ipv4</pre>
        </td>  
    </tr>
    <tr>
        <td style="vertical-align : middle" >
        <code>nv set acl &lt;name&gt; rule &lt;rule_id&gt; match &lt;ip|mac&gt; [&lt;params&gt;]</code>
        </td>
        <td style="vertical-align : middle">
        Sets ACL rule to <code>match</code> parameters. The parameters must be set according to the ACL type. For example, you can't set <code>match mac X:X:X:X:X:X</code> to an IPv4 ACL type.
        </td>      
        <td style="vertical-align : middle">
        <pre>$ nv set acl DENY_TCP_HTTP rule 10 match ip protocol tcp</br>$ nv set acl DENY_TCP_HTTP rule 10 match ip source-ip ANY</br>$ nv set acl DENY_TCP_HTTP rule 10 match ip source-port ANY</br>$ nv set acl DENY_TCP_HTTP rule 10 match ip dest-ip 10.0.15.8/32</br>$ nv set acl DENY_TCP_HTTP rule 10 match ip dest-port 80</pre>
        </td>  
    </tr>
    <tr>
        <td style="vertical-align : middle" >
        <code>nv set acl &lt;name&gt; rule &lt;rule_id&gt; action &lt;permit|deny|set|span|erspan|police|log&gt;</code>
        </td>
        <td style="vertical-align : middle">
        Sets the ACL rule action for the matched traffic. Besides the basic <code>permit</code> and <code>deny</code> actions, you can modify and manipulate the matched traffic using the ACL.
        </td>      
        <td style="vertical-align : middle">
        <pre>$ nv set acl DENY_TCP_HTTP rule 10 action drop</pre>
        </td>  
    </tr>
    <tr>
        <td style="vertical-align : middle" >
        <code>nv set interface &lt;interface&gt; acl &lt;name&gt; &lt;inbound|outbound&gt;</code>
        </td>
        <td style="vertical-align : middle">
        Applies the ACL on an interface. You need to choose the ACL bind direction, <code>inbound</code> for ingress traffic or <code>outbound</code> for egress.
        </td>      
        <td style="vertical-align : middle">
        <pre>$ nv set interface swp1 acl DENY_TCP_HTTP inbound</pre>
        </td>  
    </tr>
    <tr>
        <td style="vertical-align : middle" >
        <code>nv set interface &lt;interface&gt; acl &lt;name&gt; &lt;inbound|outbound&gt; control-plane</code>
        </td>
        <td style="vertical-align : middle">
        Applies the ACL on the control plane and binds to an interface (<code>inbound</code> or <code>outbound</code> direction).
        </td>      
        <td style="vertical-align : middle">
        <pre>$ nv set interface swp1 acl deny_icmp inbound control-plane</pre>
        </td>  
    </tr>
</table>

## Monitoring Commands 

The NVUE monitoring commands show various parts of the network configuration. The monitoring commands are divided into categories (objects) which include subcommands.</br>The general commands syntax is <code>nv show &lt;category&gt; &lt;subcommand&gt; &lt;subcommand&gt; &lt;...&gt;</code>. You can use the TAB completion to navigate through the commands.

<table style="width:100%">
    <tr >
        <th style="width:32%">
        Command Syntax
        </th>
        <th style="width:68%">
        Command Description
        </th>
    </tr>
    <tr>
        <td style="vertical-align : middle" >
        <code>nv show acl [&lt;name&gt;]<</code>
        </td>
        <td style="vertical-align : middle">
        Shows an access-list configuration.
        </td>      
    </tr>
    <tr>
        <td style="vertical-align : middle" >
        <code>nv show action</code>
        </td>
        <td style="vertical-align : middle">
        Shows information about the action commands that reset counters and remove conflicts.
        </td>        
    </tr>
    <tr>
        <td style="vertical-align : middle" >
        <code>nv show bridge</code>
        </td>
        <td style="vertical-align : middle">
        Shows bridge domain configuration.
        </td>      
    </tr>
    <tr>
        <td style="vertical-align : middle" >
        <code>nv show evpn</code>
        </td>    
        <td style="vertical-align : middle">
        Shows EVPN configuration.
        </td>      
    </tr>
    <tr>
        <td style="vertical-align : middle" >
        <code>nv show interface</code>
        </td>
        <td style="vertical-align : middle">
        Shows interface configuration.
        </td>      
    </tr>
    <tr>
        <td style="vertical-align : middle" >
        <code>nv show mlag</code>
        </td>
        <td style="vertical-align : middle">
        Shows MLAG configuration.
        </td>      
    </tr>
    <tr>
        <td style="vertical-align : middle" >
        <code>nv show nve</code>
        </td>
        <td style="vertical-align : middle">
        Shows network virtualization configuration, such as VXLAN-specific MLAG configuration and VXLAN flooding.
        </td>      
    </tr>
    <tr>
        <td style="vertical-align : middle" >
        <code>nv show platform</code>
        </td>
        <td style="vertical-align : middle">
        Shows platform configuration, such as hardware and software components.
        </td>      
    </tr>
    <tr>
        <td style="vertical-align : middle" >
        <code>nv show qos</code>
        </td>
        <td style="vertical-align : middle">
        Shows QoS RoCE configuration.
        </td>      
    </tr>
    <tr>
        <td style="vertical-align : middle" >
        <code>nv show router</code>
        </td>
        <td style="vertical-align : middle">
        Shows router configuration, such as router policies, global BGP and OSPF configuration, PBR, PIM, IGMP, VRR, and VRRP configuration.
        </td>      
    </tr>
    <tr>
        <td style="vertical-align : middle" >
        <code>nv show service</code>
        </td>
        <td style="vertical-align : middle">
        Shows DHCP relays and server, NTP, PTP, LLDP, and Syslog configuration.
        </td>      
    </tr>
    <tr>
        <td style="vertical-align : middle" >
        <code>nv show system</code>
        </td>
        <td style="vertical-align : middle">
        Shows global system settings, such as the reserved routing table range for PBR and the reserved VLAN range for layer 3 VNIs. You can also see system login messages and switch reboot history.
        </td>      
    </tr>
    <tr>
        <td style="vertical-align : middle" >
        <code>nv show vrf</code>
        </td>
        <td style="vertical-align : middle">
        Shows VRF configuration.
        </td>      
    </tr>             
</table>

NVUE provides additional options to the <code>nv show</code> commands. These options are available using command flags.

<table style="width:100%">
    <tr >
        <th style="width:32%">
        Command Syntax
        </th>
        <th style="width:68%">
        Command Description
        </th>
    </tr>
    <tr>
        <td style="vertical-align : middle" >
        <code>--applied</code>
        </td>
        <td style="vertical-align : middle">
        Shows the applied configuration for the shown object.
        </td>      
    </tr>
    <tr>
        <td style="vertical-align : middle" >
        <code>--operational</code>
        </td>
        <td style="vertical-align : middle">
        Shows the running configuration for the shown object. <code>applied</code> and <code>operational</code> configuration must be identical.
        </td>      
    </tr>
    <tr>
        <td style="vertical-align : middle" >
        <code>--color</code>
        </td>
        <td style="vertical-align : middle">
        Shows the show output /w or w/o colors.
        </td>      
    </tr>
    <tr>
        <td style="vertical-align : middle" >
        <code>--help</code>
        </td>
        <td style="vertical-align : middle">
        Shows help for the command (can be used not only for <code>nv show</code> commands).
        </td>      
    </tr>
    <tr>
        <td style="vertical-align : middle" >
        <code>--output</code>
        </td>
        <td style="vertical-align : middle">
        Shows the output in <code>json</code> or <code>yaml</code> format. 
        </td>      
    </tr>
    <tr>
        <td style="vertical-align : middle" >
        <code>--paginate</code>
        </td>
        <td style="vertical-align : middle">
        Paginates the output. 
        </td>      
    </tr>
    <tr>
        <td style="vertical-align : middle" >
        <code>--pending</code>
        </td>
        <td style="vertical-align : middle">
        Shows the pending configuration of the object. The configuration that was <code>set</code> and <code>unset</code> but not yet applied or saved.
        </td>      
    </tr>
    <tr>
        <td style="vertical-align : middle" >
        <code>--rev &lt;revision&gt;</code>
        </td>
        <td style="vertical-align : middle">
        Shows a detached (using the <code>nv detach</code> command) pending configuration.
        </td>      
    </tr>
    <tr>
        <td style="vertical-align : middle" >
        <code>--startup</code>
        </td>
        <td style="vertical-align : middle">
        Shows the switch startup-configuration (using the <code>nv config save</code> command).
        </td>      
    </tr>
    <tr>
        <td style="vertical-align : middle" >
        <code>--view</code>
        </td>
        <td style="vertical-align : middle">
        Shows these different views: <code>brief</code>, <code>lldp</code>, <code>mac</code>, <code>pluggables</code>, and <code>small</code>. This option is available for the <code>nv show interface</code> command only. E.g. <code>nv show interface --view=small</code> command shows a list of the interfaces on the switch and the <code>nv show interface --view=brief</code> command shows information about each interface on the switch, such as the interface type, speed, remote host and port.
        </td>      
    </tr>
</table>

Here are some of the useful show commands

<table style="width:100%">
    <tr >
        <th style="width:32%">
        Command Syntax
        </th>
        <th style="width:68%">
        Command Description
        </th>
    </tr>
    <tr>
        <td style="vertical-align : middle" >
        <code>nv show interface</code>
        </td>
        <td style="vertical-align : middle">
        Shows all interfaces' status. You can specify an &lt;interface&gt; to show its configuration and operational state. For each specific interface information, use the interface name in the command.
        </td>      
    </tr>
    <tr>
        <td style="vertical-align : middle" >
        <code>nv show platform hardware</code>
        </td>
        <td style="vertical-align : middle">
        Shows switch hardware-related information such as ASIC model, CPU, Memory, serial and numbers, etc.
        </td>      
    </tr>
    <tr>
        <td style="vertical-align : middle" >
        <code>nv show platform environment</code>
        </td>
        <td style="vertical-align : middle">
        Shows switch fans, LEDs, PSU and sensors information.
        </td>      
    </tr>
    <tr>
        <td style="vertical-align : middle" >
        <code>nv show platform software</code>
        </td>
        <td style="vertical-align : middle">
        Shows the installed system software packages and their versions. 
        </td>      
    </tr>
    <tr>
        <td style="vertical-align : middle" >
        <code>nv show system cpu</code>
        </td>
        <td style="vertical-align : middle">
        Shows system CPU information and utilization.
        </td>      
    </tr>
    <tr>
        <td style="vertical-align : middle" >
        <code>nv show system memory</code>
        </td>
        <td style="vertical-align : middle">
        Shows system memory information and utilization.
        </td>      
    </tr>
    <tr>
        <td style="vertical-align : middle" >
        <code>nv show service ntp</code>
        </td>
        <td style="vertical-align : middle">
        Shows NTP service configuration and status.
        </td>      
    </tr>
    <tr>
        <td style="vertical-align : middle" >
        <code>nv show system wjh packet-buffer</code>
        </td>
        <td style="vertical-align : middle">
        Shows the <a href="/cumulus-linux-53/Monitoring-and-Troubleshooting/Network-Troubleshooting/Mellanox-WJH">What Just Happened (WJH)</a> configuration and drop events on the switch.
        </td>      
    </tr>
    <tr>
        <td style="vertical-align : middle" >
        <code>nv show bridge domain br_default mac-table</code>
        </td>
        <td style="vertical-align : middle">
        Shows the bridge MAC address table.
        </td>      
    </tr>
    <tr>
        <td style="vertical-align : middle" >
        <code>nv show bridge domain br_default stp</code>
        </td>
        <td style="vertical-align : middle">
        Shows the bridge spanning-tree status.
        </td>      
    </tr>
    <tr>
        <td style="vertical-align : middle" >
        <code>nv show bridge domain br_default vlan</code>
        </td>
        <td style="vertical-align : middle">
        Shows the bridge VLAN list and VNI mapping (if configured).
        </td>      
    </tr>
    <tr>
        <td style="vertical-align : middle" >
        <code>nv show interface swp1 bridge domain br_default</code>
        </td>
        <td style="vertical-align : middle">
        Shows VLAN and spanning-tree status of an interface.
        </td>      
    </tr>
    <tr>
        <td style="vertical-align : middle" >
        <code>nv show interface swp1 bridge domain br_default</code>
        </td>
        <td style="vertical-align : middle">
        Shows VLAN and spanning-tree status of an interface.
        </td>      
    </tr>
    <tr>
        <td style="vertical-align : middle" >
        <code>nv show mlag</code>
        </td>
        <td style="vertical-align : middle">
        Shows MLAG configuration and operational state.
        </td>      
    </tr>
    <tr>
        <td style="vertical-align : middle" >
        <code>nv show mlag consistency-checker</code>
        </td>
        <td style="vertical-align : middle">
        Shows configuration consistency and conflicts between MLAG peers.
        </td>      
    </tr>
    <tr>
        <td style="vertical-align : middle" >
        <code>nv show mlag vni</code>
        </td>
        <td style="vertical-align : middle">
        Shows VNI configuration on both MLAG peers.
        </td>      
    </tr>
    <tr>
        <td style="vertical-align : middle" >
        <code>nv show nve</code>
        </td>
        <td style="vertical-align : middle">
        Shows NVE interface (VTEP) configuartion and oprational state.
        </td>      
    </tr>
    <tr>
        <td style="vertical-align : middle" >
        <code>nv show acl</code>
        </td>
        <td style="vertical-align : middle">
        Shows access-lists configuration.
        </td>      
    </tr>
</table>

## Action Commands

The NVUE action commands reset counters for interfaces and remove conflicts from protodown MLAG bonds.

<table style="width:100%">
    <tr >
        <th style="width:32%">
        Command Syntax
        </th>
        <th style="width:36%">
        Command Description
        </th>
        <th style="width:32%">
        Example
        </th>
    </tr>
    <tr>
        <td style="vertical-align : middle" >
        <code>nv action clear interface &lt;interface&gt; qos roce counters</code>
        </td>
        <td style="vertical-align : middle">
        Resets interface RoCE counters.
        </td>
        <td style="vertical-align : middle">
        <pre>$ nv action clear interface swp1 qos roce counters</pre>
        </td>   
    </tr>   
    <tr>
        <td style="vertical-align : middle" >
        <code>nv action clear interface &lt;bond-name&gt; bond mlag lacp-conflict</code>
        </td>
        <td style="vertical-align : middle">
        Removes duplicate partner MAC address or partner MAC address mismatch conflicts from protodown MLAG bonds.
        </td>
        <td style="vertical-align : middle">
        <pre>$ nv action clear interface bond1 bond mlag lacp-conflict</pre>
        </td>   
    </tr>
</table> 

## Configuration Management

NVUE leverages the Git engine to manage configuration so that you can treat your configuration as you would code.

<table style="width:100%">
    <tr >
        <th style="width:32%">
        Command Syntax
        </th>
        <th style="width:68%">
        Command Description
        </th>
    </tr>
    <tr>
        <td style="vertical-align : middle" >
        <code>nv config apply</code>
        </td>
        <td style="vertical-align : middle">
        Applies the pending configuration. </br><code>-y</code> or <code>--assume-yes</code> flag automatically reply <em>yes</em> to all prompts (<code>--assume-no</code> flag for<em>no</em>).</br>Configuration <code>apply</code> doesn't save it as startup-config, you need <code>nv config save</code> to do so.</br>You can use <code>--confirm</code> flag to leverage the <em>commit-confim</em> capability (<code>--confirm-status</code> shows the time left to confirm).
        </td>      
    </tr>
    <tr>
        <td style="vertical-align : middle" >
        <code>nv config detach</code>
        </td>
        <td style="vertical-align : middle">
        Deletes the current pending configuration.
        </td>        
    </tr>
    <tr>
        <td style="vertical-align : middle" >
        <code>nv config diff &lt;revision_a&gt; &lt;revision_b&gt;</code>
        </td>
        <td rowspan="2" style="vertical-align : middle">
        Shows differences between two configuration revisions, such as the <code>pending</code> and the <code>applied</code> configuration or the <code>detached</code> and the <code>pending</code> configurations.</br> Using the <code>-o commands</code> output, the applied configuration will be presented in NVUE commands syntax.
        </td>      
    </tr>
    <tr>
        <td style="vertical-align : middle" >
        <code>nv config diff &lt;revision&gt; &lt;revision&gt; -o commands</code>
        </td>    
    </tr>
    <tr>
        <td style="vertical-align : middle" >
        <code>nv config history &lt;nvue-file&gt;</code>
        </td>
        <td style="vertical-align : middle">
        Shows the apply history for the configuration revision (file). 
        </td>      
    </tr>
    <tr>
        <td style="vertical-align : middle" >
        <code>nv config patch &lt;nvue-file&gt;</code>
        </td>
        <td style="vertical-align : middle">
        Updates the pending configuration with the specified YAML configuration file. For more information, check out the <a href="/cumulus-linux-53/System-Configuration/NVIDIA-User-Experience-NVUE/NVUE-Snippets">NVUE Snippets</a>.
        </td>      
    </tr>
    <tr>
        <td style="vertical-align : middle" >
        <code>nv config replace &lt;nvue-file&gt;</code>
        </td>
        <td style="vertical-align : middle">
        Replaces the pending configuration with the specified YAML configuration file.
        </td>      
    </tr>
    <tr>
        <td style="vertical-align : middle" >
        <code>nv config save</code>
        </td>
        <td style="vertical-align : middle">
        Overwrites startup configuration with the applied configuration (writes to <code>/etc/nvue.d/startup.yaml</code>). This configuration persists after reboot.
        </td>      
    </tr>
    <tr>
        <td style="vertical-align : middle" >
        <code>nv config show</code>
        </td>
        <td  rowspan="2" style="vertical-align : middle">
        Shows the currently applied configuration in <code>yaml</code> format.</br> Using the <code>-o commands</code> output, the applied configuration will be presented in NVUE commands syntax.
        </td>      
    </tr>
    <tr>
        <td style="vertical-align : middle" >
        <code>nv config show -o commands</code>
        </td>
    </tr>
</table>


