---
title: Traditional Bridge Mode
author: Cumulus Networks
weight: 353
aliases:
 - /display/CL36/Traditional+Bridge+Mode
 - /pages/viewpage.action?pageId=8362161
pageID: 8362161
product: Cumulus Linux
version: '3.6'
imgData: cumulus-linux-36
siteSlug: cumulus-linux-36
---
Cumulus Networks recommends you use a [VLAN-aware
bridge](/version/cumulus-linux-36/Layer_2/Ethernet_Bridging_-_VLANs/VLAN-aware_Bridge_Mode_for_Large-scale_Layer_2_Environments)
on your switch. You use traditional mode bridges only if you need to run
more than one bridge on the switch or if you need to use PVSTP+.

## <span>Creating a Traditional Mode Bridge</span>

You can configure a traditional mode bridge either using
[NCLU](/version/cumulus-linux-36/System_Configuration/Network_Command_Line_Utility_-_NCLU/)
or manually editing the `/etc/network/interfaces` file.

### <span>Using NCLU to Configure a Traditional Bridge</span>

NCLU has limited support for configuring bridges in traditional mode.

{{%notice note%}}

The traditional bridge must be named something other than *bridge*, ****
as that name is reserved for the single [VLAN-aware
bridge](/version/cumulus-linux-36/Layer_2/Ethernet_Bridging_-_VLANs/VLAN-aware_Bridge_Mode_for_Large-scale_Layer_2_Environments)
that you can configure on the switch.

{{%/notice%}}

The following example shows how to create a simple traditional mode
bridge configuration on the switch, including adding the switch ports
that are members of the bridge. You can choose to add one or more of the
following elements to the configuration:

  - You can add an IP address to provide IP access to the bridge
    interface.

  - You can use glob syntax to specify a range of interfaces.

  - You can set two STP attributes on the bridge ports: *portautoedge*
    and *portrestrole*.
    
    {{%notice note%}}
    
    The **** *portautoedge* attribute defaults to *yes*; to use a
    setting other than the default, you must set this attribute to *no*.
    
    The *portrestrrole* attribute defaults to *no*, but to use a setting
    other than the default, you must specify this attribute **without**
    setting an option.
    
    The defaults for these attributes do not appear in the NCLU
    configuration.
    
    {{%/notice%}}

To configure a traditional mode bridge using NCLU, do the following:

    cumulus@switch:~$ net add bridge my_bridge_A ports swp1-4
    cumulus@switch:~$ net add bridge my_bridge_A ip address 10.10.10.10/24
    cumulus@switch:~$ net add interface swp1 stp portautoedge no
    cumulus@switch:~$ net add interface swp2 stp portrestrrole
    cumulus@switch:~$ net pending
    cumulus@switch:~$ net commit

These commands create the following configuration snippet in the
`/etc/network/interfaces` file:

    cumulus@switch:~$ cat /etc/network/interfaces
     
    ...
     
    auto swp1
    iface swp1
        mstpctl-portautoedge no
     
    auto swp2
    iface swp2
        mstpctl-portrestrrole yes
     
    auto swp3
    iface swp3
     
    auto swp4
    iface swp4
     
    ...
    auto my_bridge_A 
    iface my_bridge_A 
        address 10.10.10.10/24 
        bridge-ports swp1 swp2 swp3 swp4 
        bridge-vlan-aware no

Verify the configuration by running `net show config commands`:

    cumulus@switch:~$ net show config commands
    ...
    net add bridge my_bridge_A ip address 10.10.10.10/24
    net add bridge my_bridge_A ports swp1,swp2,swp3,swp4
    ...
    net add interface swp1 stp portautoedge no
    net add interface swp2 stp portrestrrole
    ...

### <span>Manually Configuring a Traditional Mode Bridge</span>

To create a traditional mode bridge manually, you need to hand edit the
`/etc/network/interfaces` file:

1.  Open the `/etc/network/interfaces` file in a text editor.

2.  Add a new stanza to create the bridge, and save the file. The
    example below creates a bridge with STP enabled and the MAC address
    ageing timer configured to a lower value than the default:
    
        auto my_bridge
        iface my_bridge
            bridge-ports bond0 swp5 swp6
            bridge-ageing 150
            bridge-stp on
    
    <table>
    <colgroup>
    <col style="width: 33%" />
    <col style="width: 33%" />
    <col style="width: 33%" />
    </colgroup>
    <thead>
    <tr class="header">
    <th><p>Configuration Option</p></th>
    <th><p>Description</p></th>
    <th><p>Default Value</p></th>
    </tr>
    </thead>
    <tbody>
    <tr class="odd">
    <td><p>bridge-ports</p></td>
    <td><p>List of logical and physical ports belonging to the logical bridge.</p></td>
    <td><p>N/A</p></td>
    </tr>
    <tr class="even">
    <td><p>bridge-ageing</p></td>
    <td><p>Maximum amount of time before a MAC addresses learned on the bridge expires from the bridge MAC cache.</p></td>
    <td><p>1800 seconds</p></td>
    </tr>
    <tr class="odd">
    <td><p>bridge-stp</p></td>
    <td><p>Enables spanning tree protocol on this bridge. The default spanning tree mode is Per VLAN Rapid Spanning Tree Protocol (PVRST).</p>
    <p>For more information on spanning-tree configurations see the configuration section: <a href="/version/cumulus-linux-36/Layer_2/Spanning_Tree_and_Rapid_Spanning_Tree">Spanning Tree and Rapid Spanning Tree</a>.</p></td>
    <td><p>off</p></td>
    </tr>
    </tbody>
    </table>
    
    {{%notice note%}}
    
    The name of the bridge must be:
    
      - Compliant with Linux interface naming conventions.
    
      - Unique within the switch.
    
    {{%/notice%}}
    
    {{%notice warning%}}
    
    Do not try to bridge the management port, eth0, with any switch
    ports (like swp0, swp1, and so forth). For example, if you created a
    bridge with eth0 and swp1, it will **not** work.
    
    {{%/notice%}}

3.  Reload the network configuration using the `ifreload` command:
    
        cumulus@switch:~$ sudo ifreload -a

{{%notice info%}}

You can configure multiple bridges, in order to logically divide a
switch into multiple layer 2 domains. This allows for hosts to
communicate with other hosts in the same domain, while separating them
fro hosts in other domains.

<span class="admonition-icon confluence-information-macro-icon"></span>

{{%notice info%}}

You can create only one VLAN-aware bridge on a switch.

{{%/notice%}}

The diagram below shows a multiple bridge configuration, where host-1
and host-2 are connected to bridge-A, while host-3 and host-4 are
connected to bridge-B. This means that:

  - host-1 and host-2 can communicate with each other.

  - host-3 and host-4 can communicate with each other.

  - host-1 and host-2 cannot communicate with host-3 and host-4.

{{% imgOld 0 %}}

This example configuration looks like this in the
`/etc/network/interfaces` file:

    auto bridge-A
    iface bridge-A
        bridge-ports swp1 swp2
        bridge-stp on
     
    auto bridge-B
    iface bridge-B
        bridge-ports swp3 swp4
        bridge-stp on

{{%/notice%}}

## <span id="src-8362161_TraditionalBridgeMode-VLAN_tagging" class="confluence-anchor-link"></span><span>Using Trunks in Traditional Bridge Mode</span>

The [IEEE standard](http://www.ieee802.org/1/pages/802.1Q.html) for
trunking is 802.1Q. The 802.1Q specification adds a 4 byte header within
the Ethernet frame that identifies the VLAN of which the frame is a
member.

802.1Q also identifies an *untagged* frame as belonging to the *native*
VLAN (most network devices default their native VLAN to 1). The concept
of native, non-native, tagged or untagged has generated confusion due to
mixed terminology and vendor-specific implementations. Some
clarification is in order:

  - A *trunk port* is a switch port configured to send and receive
    802.1Q tagged frames.

  - A switch sending an untagged (bare Ethernet) frame on a trunk port
    is sending from the native VLAN defined on the trunk port.

  - A switch sending a tagged frame on a trunk port is sending to the
    VLAN identified by the 802.1Q tag.

  - A switch receiving an untagged (bare Ethernet) frame on a trunk port
    places that frame in the native VLAN defined on the trunk port.

  - A switch receiving a tagged frame on a trunk port places that frame
    in the VLAN identified by the 802.1Q tag.

A bridge in traditional mode has no concept of trunks, just tagged or
untagged frames. With a trunk of 200 VLANs, there would need to be 199
bridges, each containing a tagged physical interface, and one bridge
containing the native untagged VLAN. See the examples below for more
information.

{{%notice note%}}

The interaction of tagged and un-tagged frames on the same trunk often
leads to undesired and unexpected behavior. A switch that uses VLAN 1
for the native VLAN may send frames to a switch that uses VLAN 2 for the
native VLAN, thus merging those two VLANs and their spanning tree state.

{{%/notice%}}

### <span>Trunk Example</span>

{{% imgOld 1 %}}

To create the above example, add the following configuration to the
`/etc/network/interfaces` file:

    auto br-VLAN100
    iface br-VLAN100
     bridge-ports swp1.100 swp2.100
     bridge-stp on
     
     
    auto br-VLAN200
    iface br-VLAN200
     bridge-ports swp1.200 swp2.200
     bridge-stp on

### <span>VLAN Tagging Examples</span>

You can find more examples of VLAN tagging in [this
chapter](/version/cumulus-linux-36/Layer_2/Ethernet_Bridging_-_VLANs/VLAN_Tagging).

### <span id="src-8362161_TraditionalBridgeMode-arp" class="confluence-anchor-link"></span><span>Configuring ARP Timers</span>

Cumulus Linux does not often interact directly with end systems as much
as end systems interact with one another. Thus, after a successful
[address resolution protocol](http://linux-ip.net/html/ether-arp.html)
(ARP) places a neighbor into a reachable state, Cumulus Linux may not
interact with the client again for a long enough period of time for the
neighbor to move into a stale state. To keep neighbors in the reachable
state, Cumulus Linux includes a background process
(`/usr/bin/neighmgrd`) that tracks neighbors that move into a stale,
delay or probe state, and attempts to refresh their state ahead of any
removal from the Linux kernel, and thus before it would be removed from
the hardware forwarding.

The ARP refresh timer defaults to 1080 seconds (18 minutes). You can
change this setting by following the procedures outlined in this
[knowledge base
article](https://support.cumulusnetworks.com/hc/en-us/articles/202012933).
