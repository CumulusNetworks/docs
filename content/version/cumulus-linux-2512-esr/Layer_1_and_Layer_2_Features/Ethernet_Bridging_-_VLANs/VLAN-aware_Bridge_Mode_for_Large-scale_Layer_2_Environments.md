---
title: VLAN-aware Bridge Mode for Large-scale Layer 2 Environments
author: Cumulus Networks
weight: 235
aliases:
 - /display/CL25ESR/VLAN-aware+Bridge+Mode+for+Large-scale+Layer+2+Environments
 - /pages/viewpage.action?pageId=5116019
pageID: 5116019
product: Cumulus Linux
version: 2.5.12 ESR
imgData: cumulus-linux-2512-esr
siteSlug: cumulus-linux-2512-esr
---
Cumulus Linux bridge driver supports two configuration modes, one that
is VLAN-aware, and one that follows a more traditional Linux bridge
model.

For traditional Linux bridges, the kernel supports VLANs in the form of
VLAN subinterfaces. Enabling bridging on multiple VLANs means
configuring a bridge for each VLAN and, for each member port on a
bridge, creating one or more VLAN subinterfaces out of that port. This
mode poses scalability challenges in terms of configuration size as well
as boot time and run time state management, when the number of ports
times the number of VLANs becomes large.

The VLAN-aware mode in Cumulus Linux implements a configuration model
for large-scale L2 environments, with **one single** **instance** of
[Spanning
Tree](/version/cumulus-linux-2512-esr/Layer_1_and_Layer_2_Features/Spanning_Tree_and_Rapid_Spanning_Tree).
Each physical bridge member port is configured with the list of allowed
VLANs as well as its port VLAN ID (either PVID or native VLAN — see
below). MAC address learning, filtering and forwarding are *VLAN-aware*.
This significantly reduces the configuration size, and eliminates the
large overhead of managing the port/VLAN instances as subinterfaces,
replacing them with lightweight VLAN bitmaps and state updates.

{{%notice tip%}}

You can configure both VLAN-aware and traditional mode bridges on the
same network in Cumulus Linux; however you should not have more than one
VLAN-aware bridge on a given switch. If you are implementing
[VXLANs](/version/cumulus-linux-2512-esr/Layer_1_and_Layer_2_Features/Network_Virtualization/Static_MAC_Bindings_with_VXLAN),
you **must** use non-aware bridges.

{{%/notice%}}

## <span>Defining VLAN-aware Bridge Attributes</span>

To configure a VLAN-aware bridge, include the `bridge-vlan-aware`
attribute, setting it to *yes*. Name the bridge *bridge* to help ensure
it is the only VLAN-aware bridge on the switch. The following attributes
are useful for configuring VLAN-aware bridges:

  - `bridge-vlan-aware`: Set to *yes* to indicate that the bridge is in
    VLAN-aware mode.

  - `bridge-pvid`: A PVID is the bridge's *Primary VLAN Identifer*. The
    PVID defaults to 1; specifying the PVID identifies that VLAN as the
    native VLAN.

  - `bridge-vids`: A VID is the *VLAN Identifier*, which declares the
    VLANs associated with this bridge.

  - `bridge-access`: Declares the physical switch port as an *access
    port*. Access ports ignore all tagged packets; put all untagged
    packets into the `bridge-pvid`.

  - `bridge-allow-untagged`: When set to *no*, it drops any untagged
    frames for a given switch port.

For a definitive list of bridge attributes, run `ifquery --syntax-help`
and look for the entries under **bridge**, **bridgevlan** and
**mstpctl**.

## <span>Basic Trunking</span>

A basic configuration for a VLAN-aware bridge configured for STP that
contains two switch ports looks like this:

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>{{% imgOld 0 %}}</p></td>
<td><pre><code>auto bridge
iface bridge
    bridge-vlan-aware yes
    bridge-ports swp1 swp2
    bridge-vids 100 200
    bridge-pvid 1
    bridge-stp on</code></pre></td>
</tr>
</tbody>
</table>

The above configuration actually includes 3 VLANs: the tagged VLANs 100
and 200 and the untagged (native) VLAN of 1.

{{%notice note%}}

The `bridge-pvid 1` is implied by default. You do not have to specify
`bridge-pvid`. And while it does not hurt the configuration, it helps
other users for readability.

The following configurations are identical to each other and the
configuration above:

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<tbody>
<tr class="odd">
<td><pre><code>auto bridge
iface bridge
    bridge-vlan-aware yes
    bridge-ports swp1 swp2
    bridge-vids 1 100 200
    bridge-stp on</code></pre></td>
<td><pre><code>auto bridge
iface bridge
    bridge-vlan-aware yes
    bridge-ports swp1 swp2
    bridge-vids 1 100 200
    bridge-pvid 1
    bridge-stp on</code></pre></td>
<td><pre><code>auto bridge
iface bridge
    bridge-vlan-aware yes
    bridge-ports swp1 swp2
    bridge-vids 100 200
    bridge-stp on</code></pre></td>
</tr>
</tbody>
</table>

{{%/notice%}}

## <span>VLAN Filtering/VLAN Pruning</span>

By default, the bridge port inherits the bridge VIDs. A port's
configuration can override the bridge VIDs. Do this by specifying
port-specific VIDs using the `bridge-vids` attribute.

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>{{% imgOld 1 %}}</p></td>
<td><pre><code>auto bridge
iface bridge
    bridge-vlan-aware yes
    bridge-ports swp1 swp2 swp3
    bridge-vids 100 200
    bridge-pvid 1
    bridge-stp on
 
auto swp3
iface swp3
  bridge-vids 200</code></pre></td>
</tr>
</tbody>
</table>

## <span>Untagged/Access Ports</span>

As described above, access ports ignore all tagged packets. In the
configuration below, swp1 and swp2 are configured as access ports. All
untagged traffic goes to the specified VLAN, which is VLAN 100 in the
example below.

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>{{% imgOld 2 %}}</p></td>
<td><pre><code>auto bridge
iface bridge
    bridge-vlan-aware yes
    bridge-ports swp1 swp2
    bridge-vids 100 200
    bridge-pvid 1
    bridge-stp on
 
auto swp1
iface swp1
    bridge-access 100
 
auto swp2
iface swp2
    bridge-access 100</code></pre></td>
</tr>
</tbody>
</table>

### <span>Dropping Untagged Frames</span>

With VLAN-aware bridge mode, it's possible to configure a switch port so
it drops any untagged frames. To do this, add `bridge-allow-untagged no`
under the switch port stanza in `/etc/network/interfaces`. This leaves
the bridge port without a PVID and drops untagged packets.

Consider the following example bridge:

    auto bridge
    iface bridge
      bridge-vlan-aware yes
      bridge-ports swp1 swp9
      bridge-vids 2-100
      bridge-pvid 101
      bridge-stp on

Here is the VLAN membership for that configuration:

    cumulus@switch$ bridge vlan show
    portvlan ids
    swp1 101 PVID Egress Untagged
     2-100
    
    swp9 101 PVID Egress Untagged
     2-100
    
    bridge 101

To configure swp9 to drop untagged frames, add `bridge-allow-untagged
no`:

    auto swp9
    iface swp9
      bridge-allow-untagged no

When you check VLAN membership for that port, it shows that there is
**no** untagged VLAN.

    cumulus@switch$ bridge vlan show
    portvlan ids
    swp1 101 PVID Egress Untagged
     2-100
    
    swp9 2-100
    
    bridge 101

## <span>VLAN Layer 3 Addressing/Switch Virtual Interfaces and other VLAN Attributes </span>

When configuring the VLAN attributes for the bridge, put the attributes
in a separate stanza for each VLAN interface: \<bridge\>.\<vlanid\>. If
you are configuring the SVI for the native VLAN, you must declare the
native VLAN in its own stanza and specify its IP address. Specifying the
IP address in the bridge stanza itself returns an error.

    auto bridge.100
    iface bridge.100
        address 192.168.10.1/24
        address 2001:db8::1/32
        hwaddress 44:38:39:ff:00:00
    
    # l2 attributes
    auto bridge.100
    vlan bridge.100
        bridge-igmp-querier-src 172.16.101.1

{{%notice note%}}

The *vlan* object type in the l2 attributes section above is used to
specify layer 2 VLAN attributes only. Currently, the only supported
layer 2 VLAN attribute is `bridge-igmp-querier-src`.

However, if your switch is configured for multicast routing, then you do
not need to specify `bridge-igmp-querier-src`, as there is no need for a
static IGMP querier configuration on the switch. Otherwise, the static
IGMP querier configuration helps to probe the hosts to refresh their
IGMP reports.

{{%/notice%}}

You can specify a range of VLANs as well. For example:

    auto bridge.[1-2000]
    vlan bridge.[1-2000]
        ATTRIBUTE VALUE

## <span>Using the glob Keyword to Configure Multiple Ports in a Range</span>

The `glob` keyword referenced in the `bridge-ports` attribute indicates
that swp1 through swp52 are part of the bridge, which is a short cut
that saves you from enumerating each port individually:

    auto bridge
    iface bridge
          bridge-vlan-aware yes
          bridge-ports glob swp1-52
          bridge-stp on
          bridge-vids 310 700 707 712 850 910

## <span>Example Configuration with Access Ports and Pruned VLANs</span>

The following example contains an access port and a switch port that is
*pruned*; that is, it only sends and receives traffic tagged to and from
a specific set of VLANs declared by the `bridge-vids` attribute. It also
contains other switch ports that send and receive traffic from all the
defined VLANs.

    # ports swp3-swp48 are trunk ports which inherit vlans from the 'bridge'
    # ie vlans 310,700,707,712,850,910
    #
    auto bridge
    iface bridge
          bridge-vlan-aware yes
          bridge-ports glob swp1-52
          bridge-stp on
          bridge-vids 310 700 707 712 850 910
     
    auto swp1
    iface swp1
          mstpctl-portadminedge yes
          mstpctl-bpduguard yes
          bridge-access 310
     
    # The following is a trunk port that is "pruned".
    # native vlan is 1, but only .1q tags of 707, 712, 850 are
    # sent and received
    #
    auto swp2
    iface swp2
          mstpctl-portadminedge yes
          mstpctl-bpduguard yes
          bridge-vids 707 712 850
         
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

## <span>Example Configuration with Bonds</span>

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
        bridge-vids 2000-2079
     
    # bond interface
    auto peerlink
    iface peerlink
        bond-slaves swp30 swp31
        bridge-vids 2000-2079 4094
     
    # bond interface
    auto downlink
    iface downlink
        bond-slaves swp1
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

## <span>Converting a Traditional Bridge to VLAN-aware or Vice Versa</span>

You cannot automatically convert a traditional bridge to/from a
VLAN-aware bridge simply by changing the configuration in the
`/etc/network/interfaces` file. If you need to change the mode for a
bridge, do the following:

1.  Delete the traditional mode bridge from the configuration and bring
    down all its member switch port interfaces.

2.  Create a new VLAN-aware bridge, as described above.

3.  Bring up the bridge.

These steps assume you are converting a traditional mode bridge to a
VLAN-aware one. To do the opposite, delete the VLAN-aware bridge in step
1, and create a new traditional mode bridge in step 2.

## <span>Caveats and Errata</span>

  - **STP:** Because [Spanning Tree and Rapid Spanning
    Tree](/version/cumulus-linux-2512-esr/Layer_1_and_Layer_2_Features/Spanning_Tree_and_Rapid_Spanning_Tree)
    (STP) are enabled on a per-bridge basis, VLAN-aware mode essentially
    supports a single instance of STP across all VLANs. A common
    practice when using a single STP instance for all VLANs is to define
    all every VLAN on each switch in the spanning tree instance. `mstpd`
    continues to be the user space protocol daemon, and Cumulus Linux
    supports RSTP.

  - **IGMP snooping:** IGMP snooping and group membership are supported
    on a per-VLAN basis, though the IGMP snooping configuration
    (including enable/disable, mrouter port and so forth) are defined on
    a per-bridge port basis.

  - **VXLANs:** Use the traditional configuration mode for [VXLAN
    configuration](/version/cumulus-linux-2512-esr/Layer_1_and_Layer_2_Features/Network_Virtualization/Static_MAC_Bindings_with_VXLAN).

  - **<span id="src-5116019_VLAN-awareBridgeModeforLarge-scaleLayer2Environments-range"></span>Reserved
    VLAN range:** For hardware data plane internal operations, the
    switching silicon requires VLANs for every physical port, Linux
    bridge, and layer 3 subinterface. Cumulus Linux reserves a range of
    700 VLANs by default; this range is 3300-3999. In case any of your
    user-defined VLANs conflict with the default reserved range, you can
    modify the range, as long as the new range is a contiguous set of
    VLANs with IDs anywhere between 2 and 4094, and the minimum size of
    the range is 300 VLANs:
    
    1.  Edit `/etc/cumulus/switchd.conf`, uncomment `resv_vlan_range`
        and specify the new range.
    
    2.  [Restart
        `switchd`](Configuring_switchd.html#src-5115907_Configuringswitchd-restartswitchd)
        (`sudo service switchd restart`) for the new range to take
        effect.
        
        {{%notice note%}}
        
        While restarting `switchd`, all running ports will flap and
        forwarding will be
        [interrupted](Configuring_switchd.html#src-5115907_Configuringswitchd-restartswitchd).
        
        {{%/notice%}}

  - **VLAN translation:** A bridge in VLAN-aware mode cannot have VLAN
    translation enabled for it; only bridges configured in [traditional
    mode](/version/cumulus-linux-2512-esr/Layer_1_and_Layer_2_Features/Ethernet_Bridging_-_VLANs/)
    can utilize VLAN translation.
