---
title: VLAN-aware Bridge Mode for Large-scale Layer 2 Environments
author: Cumulus Networks
weight: 149
aliases:
 - /display/RMP25ESR/VLAN-aware+Bridge+Mode+for+Large-scale+Layer+2+Environments
 - /pages/viewpage.action?pageId=5116351
pageID: 5116351
product: Cumulus RMP
version: 2.5.12 ESR
imgData: cumulus-rmp-2512-esr
siteSlug: cumulus-rmp-2512-esr
---
The Cumulus RMP bridge driver supports two configuration modes, one that
is VLAN-aware, and one that follows a more traditional Linux bridge
model.

For traditional Linux bridges, the kernel supports VLANs in the form of
VLAN subinterfaces. Enabling bridging on multiple VLANs means
configuring a bridge for each VLAN and, for each member port on a
bridge, creating one or more VLAN subinterfaces out of that port. This
mode poses scalability challenges in terms of configuration size as well
as boot time and run time state management, when the number of ports
times the number of VLANs becomes large.

The VLAN-aware mode in Cumulus RMP implements a configuration model for
large-scale L2 environments, with **one single** **instance** of
[Spanning
Tree](/version/cumulus-rmp-2512-esr/Layer_1_and_Layer_2_Features/Spanning_Tree_and_Rapid_Spanning_Tree).
Each physical bridge member port is configured with the list of allowed
VLANs as well as its port VLAN ID (either PVID or native VLAN — see
below). MAC address learning, filtering and forwarding are *VLAN-aware*.
This significantly reduces the configuration size, and eliminates the
large overhead of managing the port/VLAN instances as subinterfaces,
replacing them with lightweight VLAN bitmaps and state updates.

{{%notice tip%}}

You can configure both VLAN-aware and traditional mode bridges on the
same network in Cumulus RMP; however you should not have more than one
VLAN-aware bridge on a given switch.

{{%/notice%}}

Contents

(Click to expand)

## <span>Creating the Bridge</span>

You need to configure only one VLAN-aware bridge, and you need to add
only physical ports or bonds to the bridge. Use ` ifupdown2  `to create
the configuration.

## <span>Defining VLAN Memberships</span>

With the VLAN-aware bridge mode, VLAN membership is defined for each
bridge member interface. This includes the allowed VLAN list and the
PVID of the interface (that is, native or default VLAN). In the code
below, bond0 and bond1 are trunk ports with native VLAN of 10 and
allowed VLAN list of 1-1000, 1010-1020. swp5 is an access port with
access VLAN of 10.

## <span>Configuring Router Interfaces</span>

In case L3 termination of any VLANs is required, you can configure a
router interface as a VLAN subinterface of the bridge device itself.

To continue with the previous example, say VLAN 10 and VLAN 1000 are
layer 3 routed. You can create the router interfaces by running:

    cumulus@switch:~$ sudo ip link add link br name br.10 type vlan id 10
    cumulus@switch:~$ sudo ip link add link br name br.1000 type vlan id 1000

Then you use the `ip addr add` command to assign an IP address to each
interface. Note that in order for the bridge to pass routed traffic on
these two VLANs, you need to assign the VLANs in the bridge's VLAN list.
To do this, run:

    cumulus@switch:~$ sudo bridge vlan add vid 10 dev br self
    cumulus@switch:~$ sudo bridge vlan add vid 1000 dev br self

## <span>Using the Show Commands</span>

To show all bridge VLANs:

    cumulus@switch:~$ bridge vlan show
    port    vlan ids
      
    bond0    10 PVID Egress Untagged
             1-9
             11-1000
             1010-1020
      
    bond1    10 PVID Egress Untagged
             1-9
             11-1000
             1010-1020
      
    swp5     10 PVID Egress Untagged
      
    br       10
             1000

To show membership of a particular VLAN:

    cumulus@switch:~$ sudo bridge vlan show vlan 10
    VLAN 10:
            bond0 bond1 swp5 br0

To show MAC addresses, do one of the following:

    cumulus@switch:~$ sudo brctl showmacs br | grep -v yes
    port name mac addr              vlan    is local? ageing timer
    bond0     00:e0:ec:25:2f:5b     10      no 39.47
      
    cumulus@switch:~$ sudo bridge fdb show | grep -v perm
    00:e0:ec:25:2f:5b dev bond0 vlan 10 port 0

## <span>Configuring a VLAN-aware Bridge</span>

To configure a VLAN-aware bridge, include the `bridge-vlan-aware`
attribute, setting it to *yes*. Name the bridge *bridge* to help ensure
it is the only VLAN-aware bridge on the switch. The following attributes
are useful for configuring VLAN-aware bridges:

  - `bridge-vlan-aware`: set to *yes* to indicate that the bridge is
    VLAN-aware.

  - `bridge-access`: declares the access port.

  - `bridge-pvid`: specifies native VLANs if the ID is other than 1.

  - `bridge-vids`: declares the VLANs associated with this bridge.

For a definitive list of bridge attributes, run `ifquery --syntax-help`
and look for the entries under **bridge**, **bridgevlan** and
**mstpctl**.

A basic configuration for a VLAN-aware bridge configured for STP that
contains two switch ports looks like this:

    auto bridge
    iface bridge
        bridge-vlan-aware yes
        bridge-ports swp1 swp2
        bridge-stp on

By default, the bridge port inherits the bridge VIDs. You can have a
port override the bridge VIDs by specifying port-specific VIDs, using
the `bridge-ports` attribute.

As with traditional bridges, the bridge port membership and bridge
attributes remain under bridge configuration. But bridge port attributes
reside under the ports themselves.

When configuring the VLAN attributes for the bridge, put the layer 2
attributes in a separate stanza using this special VLAN interface:
\<bridge\>.\<vlanid/range\>. You can specify a range of VLANs as well.
For example:

    auto bridge.4094
    vlan bridge.4094
        address 172.16.101.100
        hwaddress 44:38:39:ff:00:00
        bridge-igmp-querier-src 172.16.101.1

Or:

    auto bridge.[4094-4096]
    vlan bridge.[4094-4096]
        ATTRIBUTE VALUE

For switched virtual interface configurations, specify a regular
bridge.vlanid device with the `address` attribute:

    auto bridge.4094
    iface bridge.4094
        address <ipaddr>
        hwaddress <mac>

VLAN-aware bridges are backwards compatible with traditional bridge
configurations.

### <span>Example Basic Configuration</span>

The following is a basic example illustrating how to configure a
VLAN-aware bridge using
[ifupdown2](/version/cumulus-rmp-2512-esr/Configuring_and_Managing_Network_Interfaces/).
Add this persistent configuration to `/etc/network/interfaces`.

Note the attributes used in the stanza:

  - The `bridge-vlan-aware` is set to yes, indicating the bridge is
    VLAN-aware.

  - The `glob` keyword referenced in the `bridge-ports` attribute
    indicates that swp1 through swp52 are part of the bridge, instead of
    enumerating them one by one.

  - [STP](/version/cumulus-rmp-2512-esr/Layer_1_and_Layer_2_Features/Spanning_Tree_and_Rapid_Spanning_Tree)
    is enabled on the bridge.

  - The `bridge-vids` attribute declares the VLANs associated with the
    bridge.

<!-- end list -->

    #
    # vlan-aware bridge simple example
    #
    # 'bridge' is a vlan aware bridge with all ports (swp1-52).
    # native vlan is by default 1
    #
    # 'bridge-vids' attribute is used to declare vlans.
    # 'bridge-pvid' attribute is used to specify native vlans if other than 1
    # 'bridge-access' attribute is used to declare access port
    # 
    
    #
    # ports swp1-swp52 are trunk ports which inherit vlans from 'bridge'
    # ie vlans 310 700 707 712 850 910
          
    #
    # the following is a vlan aware bridge with ports swp1-swp52
    # It has stp on
    #
    auto bridge
    iface bridge
          bridge-vlan-aware yes
          bridge-ports glob swp1-52
          bridge-stp on
          bridge-vids 310 700 707 712 850 910

### <span>Example Configuration with Access Ports and Pruned VLANs</span>

The following example contains an access port and a switch port that is
*pruned*; that is, it only sends and receives traffic tagged to and from
a specific set of VLANs declared by the `bridge-vids` attribute. It also
contains other switch ports that send and receive traffic from all the
defined VLANs.

    #
    # vlan-aware bridge access ports and pruned vlan example
    #
    # 'bridge' is a vlan aware bridge with all ports (swp1-52).
    # native vlan is by default 1
    #
    # 'bridge-vids' attribute is used to declare vlans.
    # 'bridge-pvid' attribute is used to specify native vlans if other than 1
    # 'bridge-access' attribute is used to declare access port
    #
    # 
    
    # The following is an access port to vlan 310, no trunking
    auto swp1
    iface swp1
          bridge-access 310
          mstpctl-portadminedge yes
          mstpctl-bpduguard yes
    
    # The following is a trunk port that is "pruned".
    # native vlan is 1, but only .1q tags of 707, 712, 850 are
    # sent and received
    #
    auto swp2
    iface swp2
          bridge-vids 707 712 850
          mstpctl-portadminedge yes
          mstpctl-bpduguard yes
         
    # The following port is the trunk uplink and inherits all vlans
    # from 'bridge'; bridge assurance is enabled using 'portnetwork' attribute
    auto swp49
    iface swp49
          mstpctl-portpathcost 10
          mstpctl-portnetwork yes
    
    # The following port is the trunk uplink and inherits all vlans
    # from 'bridge'; bridge assurance is enabled using 'portnetwork' attribute
    auto swp50
    iface swp50
          mstpctl-portpathcost 0
          mstpctl-portnetwork yes
    
    #
    # ports swp3-swp48 are trunk ports which inherit vlans from the 'bridge'
    # ie vlans 310,700,707,712,850,910
          
    #
    # the following is a vlan aware bridge with ports swp1-swp52
    # It has stp on
    #
    auto bridge
    iface bridge
          bridge-vlan-aware yes
          bridge-ports glob swp1-52
          bridge-stp on
          bridge-vids 310 700 707 712 850 910

### <span>Example Configuration with Bonds</span>

This configuration demonstrates a VLAN-aware bridge with a large set of
bonds. The bond configurations are generated from a
[Mako](http://www.makotemplates.org/) template.

    #
    # vlan-aware bridge with bonds example
    #
    # uplink1, peerlink and downlink are bond interfaces.
    # 'bridge' is a vlan aware bridge with ports uplink1, peerlink
    # and downlink (swp2-20).
    # 
    # native vlan is by default 1
    #
    # 'bridge-vids' attribute is used to declare vlans.
    # 'bridge-pvid' attribute is used to specify native vlans if other than 1
    # 'bridge-access' attribute is used to declare access port
    # 
    auto lo
    iface lo
    
    auto eth0
    iface eth0 inet dhcp
    
    # bond interface
    auto uplink1
    iface uplink1
        bond-slaves swp32
        bond-mode 802.3ad
        bond-miimon 100
        bond-use-carrier 1
        bond-lacp-rate 1
        bond-min-links 1
        bond-xmit-hash-policy layer3+4
        bridge-vids 2000-2079
    
    # bond interface
    auto peerlink
    iface peerlink
        bond-slaves swp30 swp31
        bond-mode 802.3ad
        bond-miimon 100
        bond-use-carrier 1
        bond-lacp-rate 1
        bond-min-links 1
        bond-xmit-hash-policy layer3+4
        bridge-vids 2000-2079 4094
    
    # bond interface
    auto downlink
    iface downlink
        bond-slaves swp1
        bond-mode 802.3ad
        bond-miimon 100
        bond-use-carrier 1
        bond-lacp-rate 1
        bond-min-links 1
        bond-xmit-hash-policy layer3+4
        bridge-vids 2000-2079
    
    #
    # Declare vlans for all swp ports
    # swp2-20 get vlans from 2004 to 2022.
    # The below uses mako templates to generate iface sections
    # with vlans for swp ports
    #
    %for port, vlanid in zip(range(2, 20), range(2004, 2022)) :
        auto swp${port}
        iface swp${port}
            bridge-vids ${vlanid}
    
    %endfor
    
    # svi vlan 4094
    auto bridge.4094
    iface bridge.4094
        address 11.100.1.252/24
    
    # l2 attributes for vlan 4094
    auto bridge.4094
    vlan bridge.4094
        bridge-igmp-querier-src 172.16.101.1
    
    #
    # vlan-aware bridge
    #
    auto bridge
    iface bridge
        bridge-vlan-aware yes
        bridge-ports uplink1 peerlink downlink glob swp2-20
        bridge-stp on
    
    # svi peerlink vlan
    auto peerlink.4094
    iface peerlink.4094
        address 192.168.10.1/30
        broadcast 192.168.10.3

<span id="src-5116351_VLAN-awareBridgeModeforLarge-scaleLayer2Environments-iproute2"></span>

## <span>Caveats and Errata</span>

  - **STP:** Because [Spanning Tree and Rapid Spanning
    Tree](/version/cumulus-rmp-2512-esr/Layer_1_and_Layer_2_Features/Spanning_Tree_and_Rapid_Spanning_Tree)
    (STP) are enabled on a per-bridge basis, VLAN-aware mode essentially
    supports a single instance of STP across all VLANs. A common
    practice when using a single STP instance for all VLANs is to define
    all every VLAN on each switch in the spanning tree instance. `mstpd`
    continues to be the user space protocol daemon, and Cumulus RMP
    supports RSTP.

  - **<span id="src-5116351_VLAN-awareBridgeModeforLarge-scaleLayer2Environments-range"></span>Reserved
    VLAN range:** For hardware data plane internal operations, the
    switching silicon requires VLANs for every physical port, Linux
    bridge, and layer 3 subinterface. Cumulus RMP reserves a range of
    700 VLANs by default; this range is 3300-3999. In case any of your
    user-defined VLANs conflict with the default reserved range, you can
    modify the range, as long as the new range is a contiguous set of
    VLANs with IDs anywhere between 2 and 4094, and the minimum size of
    the range is 300 VLANs:
    
    1.  Edit `/etc/cumulus/switchd.conf`, uncomment `resv_vlan_range`
        and specify the new range.
    
    2.  Restart `switchd` (`sudo service switchd restart`) for the new
        range to take effect.
        
        {{%notice note%}}
        
        While restarting `switchd`, all running ports will flap and
        forwarding will be interrupted.
        
        {{%/notice%}}

  - **VLAN translation:** A bridge in VLAN-aware mode cannot have VLAN
    translation enabled for it; only bridges configured in [traditional
    mode](/version/cumulus-rmp-2512-esr/Layer_1_and_Layer_2_Features/Ethernet_Bridging_-_VLANs/)
    can utilize VLAN translation.
