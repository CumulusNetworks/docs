---
title: LNV VXLAN Active-Active Mode
author: Cumulus Networks
weight: 281
aliases:
 - /display/CL25ESR/LNV+VXLAN+Active-Active+Mode
 - /pages/viewpage.action?pageId=5116066
pageID: 5116066
product: Cumulus Linux
version: 2.5.12 ESR
imgData: cumulus-linux-2512-esr
siteSlug: cumulus-linux-2512-esr
---
*VXLAN active-active mode* allows a pair of
[MLAG](/version/cumulus-linux-2512-esr/Layer_1_and_Layer_2_Features/Multi-Chassis_Link_Aggregation_-_MLAG)
switches to act as a single VTEP, providing active-active VXLAN
termination for bare metal as well as virtualized workloads.

## <span>Requirements</span>

  - Each MLAG switch should be provisioned with a virtual IP address in
    the form of an anycast IP address for VXLAN datapath termination.

  - All [MLAG
    requirements](Multi-Chassis_Link_Aggregation_-_MLAG.html#src-5116071_Multi-ChassisLinkAggregation-MLAG-reqs)
    apply for VXLAN Active-Active mode.

  - [LNV](/version/cumulus-linux-2512-esr/Layer_1_and_Layer_2_Features/Network_Virtualization/Lightweight_Network_Virtualization_-_LNV/)
    is the only supported control plane option for VXLAN active-active
    mode in this release. LNV can be configured for either service node
    replication or head-end replication.

  - If
    [STP](/version/cumulus-linux-2512-esr/Layer_1_and_Layer_2_Features/Spanning_Tree_and_Rapid_Spanning_Tree)
    is enabled on the bridge that is connected to VXLAN, then [BPDU
    filter and BPDU
    guard](Spanning_Tree_and_Rapid_Spanning_Tree.html#src-5116082_SpanningTreeandRapidSpanningTree-bpdu)
    should be enabled in the VXLAN interface.

## <span>Anycast IP Addresses</span>

The VXLAN termination address is an anycast IP address that you
configure as a `clagd` parameter (`clagd-vxlan-anycast-ip`) under the
loopback interface. `clagd` dynamically adds and removes this address as
the loopback interface address as follows:

  - When the switches come up, ` ifupdown2  `places all VXLAN interfaces
    in a [PROTO\_DOWN
    state](#src-5116066_LNVVXLANActive-ActiveMode-proto_down).

  - Upon MLAG peering and a successful VXLAN interface consistency check
    between the switches, `clagd` adds the anycast address as the
    interface address to the loopback interface. It then changes the
    local IP address of the VXLAN interface from a unique non-virtual IP
    address to an anycast virtual IP address and puts the interface in
    an UP state.

  - If after establishing MLAG peering, the peer link goes down, then
    the primary switch continues to keep all VXLAN interfaces up with
    the anycast IP address while the secondary switch brings down all
    VXLAN interfaces and places them in a PROTO\_DOWN state. It also
    removes the anycast IP address from the loopback interface and
    changes the local IP address of the VXLAN interface to a unique
    non-virtual IP address.

  - If after establishing MLAG peering, one of the switches goes down,
    then the other running switch continues to use the anycast IP
    address.

  - If after establishing MLAG peering, `clagd` is stopped, all VXLAN
    interfaces are put in a PROTO\_DOWN state. The anycast IP address is
    removed from the loopback interface and the local IP addresses of
    the VXLAN interfaces are changed from the anycast IP address to
    unique non-virtual IP addresses.

  - If MLAG peering could not be established between the switches,
    `clagd` brings up all the VXLAN interfaces after the reload timer
    expires with unique non-virtual IP addresses. This allows the VXLAN
    interface to be up and running on both switches even though peering
    is not established.

## <span>Checking VXLAN Interface Configuration Consistency</span>

The VXLAN active-active configuration for a given VNI has to be
consistent between the MLAG switches for correct traffic behavior.
`clagd` ensures that the configuration consistency is met before
bringing the VXLAN interfaces operationally up. The consistency checks
include:

  - The anycast virtual IP address for VXLAN termination must be the
    same on both switches

  - A VXLAN interface with the same VNI must be configured and
    administratively up on both switches

## <span>Configuring VXLAN Active-Active Mode</span>

### <span>Configuring the Anycast IP Address</span>

With MLAG peering, both switches use an anycast IP address for VXLAN
encapsulation and decapsulation. This allows remote VTEPs to learn the
host MAC addresses attached to the MLAG switches against one logical
VTEP even though the switches independently encapsulate and decapsulate
layer 2 traffic originating from the host. You configure this anycast
address under the loopback interface as shown below.

    auto lo
    iface lo
        address 27.0.0.11/32
        clagd-vxlan-anycast-ip 36.0.0.11

{{%notice note%}}

This is not a loopback interface address configuration. It's a `clagd`
parameter configuration under the loopback interface. Only `clagd` can
add or remove an anycast virtual IP address as an interface address to
the loopback interface.

{{%/notice%}}

### <span>Configuring MLAG</span>

Refer to the [MLAG
chapter](Multi-Chassis_Link_Aggregation_-_MLAG.html#src-5116071_Multi-ChassisLinkAggregation-MLAG-configuring)
for configuration information.

### <span>Configuration LNV</span>

Refer to the [LNV
chapter](/version/cumulus-linux-2512-esr/Layer_1_and_Layer_2_Features/Network_Virtualization/Lightweight_Network_Virtualization_-_LNV/)
for configuration information.

### <span>Configuring STP</span>

You should enable [BPDU filter and BPDU
guard](Spanning_Tree_and_Rapid_Spanning_Tree.html#src-5116082_SpanningTreeandRapidSpanningTree-bpdu)
in the VXLAN interfaces if
[STP](/version/cumulus-linux-2512-esr/Layer_1_and_Layer_2_Features/Spanning_Tree_and_Rapid_Spanning_Tree)
is enabled in the bridge that is connected to the VXLAN.

## <span>Example VXLAN Active-Active Configuration</span>

The following example configures two bonds for MLAG, each with a single
port, a peer link that is a bond with two member ports, and two
traditional Linux bridges. It is a Clos network with spine nodes
(spine1-4), 2 MLAG switches (leaf1, leaf2), 2 hosts connected to those
switches and 2 standalone switches (leaf3 and leaf4) with hosts
connected to them. The configuration is stored in
`/etc/network/interfaces` on each peer switch.

{{% imgOld 0 %}}

Note the configuration of the local IP address in the VXLAN interfaces
below. They are configured with individual IP addresses, which `clagd`
changes to anycast upon MLAG peering.

### <span>leaf1 Configuration</span>

leaf1 configuration; click here to expand...

    auto eth0
        address 10.0.0.1
        netmask 255.255.255.0
     
    auto lo
    iface lo
        address 27.0.0.11/32
        clagd-vxlan-anycast-ip 36.0.0.11
     
    auto swp1
    iface swp1
        address 10.1.1.1/30
        mtu  9050
     
    auto swp2
    iface swp2
        address 10.1.1.5/30
        mtu  9050
     
    auto swp3
    iface swp3
        address 10.1.1.33/30
        mtu  9050
     
    auto swp4
    iface swp4
        address 10.1.1.37/30
        mtu  9050
     
    auto peerlink
    iface peerlink
        bond-slaves swp31 swp32
        mtu  9050
     
    auto peerlink.4094
    iface peerlink.4094
        address 27.0.0.11/32
        address 169.254.1.1/30
        mtu 9050
        clagd-priority 4096
        clagd-sys-mac 44:38:39:ff:ff:01
        clagd-peer-ip 169.254.0.2
        clagd-backup-ip 10.0.0.2
     
    auto host1
    iface host1
            bond-slaves swp5
            mtu  9050
            clag-id 1
     
    auto host2
    iface host2
            bond-slaves swp6
            mtu  9050
            clag-id 2
     
    auto vxlan-1000
    iface vxlan-1000
        vxlan-id 1000
        vxlan-local-tunnelip 27.0.0.11
        mtu 9000
     
    auto vxlan-2000
    iface vxlan-2000
        vxlan-id 2000
        vxlan-local-tunnelip 27.0.0.11
        mtu 9000
     
    auto br1000
    iface br1000
        bridge-ports host1 host2.1000 peerlink.1000 vxlan-1000
        bridge-stp on
        mstpctl-portbpdufilter vxlan-1000=yes
        mstpctl-bpduguard vxlan-1000=yes
        mstpctl-portautoedge host1=yes host2.1000=yes peerlink.1000=yes
     
    auto br2000
    iface br2000
        bridge-ports host1.2000 host2 peerlink.2000 vxlan-2000
        bridge-stp on
        mstpctl-portbpdufilter vxlan-2000=yes
        mstpctl-bpduguard vxlan-2000=yes
        mstpctl-portautoedge host1.2000=yes host2=yes peerlink.2000=yes

### <span>leaf2 Configuration</span>

leaf2 configuration; click here to expand...

    auto eth0
        address 10.0.0.2
        netmask 255.255.255.0
     
    auto lo
    iface lo
        address 27.0.0.12/32
        clagd-vxlan-anycast-ip 36.0.0.11
     
    auto swp1
    iface swp1
        address 10.1.1.17/30
        mtu  9050
     
    auto swp2
    iface swp2
        address 10.1.1.21/30
        mtu  9050
     
    auto swp3
    iface swp1
        address 10.1.1.49/30
        mtu  9050
     
    auto swp4
    iface swp2
        address 10.1.1.53/30
        mtu  9050
     
    auto peerlink
    iface peerlink
        bond-slaves swp31 swp32
        mtu  9050
           
    auto peerlink.4094
    iface peerlink.4094
        address 27.0.0.12/32
        address 169.254.0.2/30
        mtu 9050
        clagd-priority 4096
        clagd-sys-mac 44:38:39:ff:ff:01
        clagd-peer-ip 169.254.1.1
        clagd-backup-ip 10.0.0.1
     
    auto host1
    iface host1
        bond-slaves swp5
        mtu  9050
        clag-id 1
     
    auto host2
    iface host2
        bond-slaves swp6
        mtu  9050
        clag-id 2
     
    auto vxlan-1000
    iface vxlan-1000
        vxlan-id 1000
        vxlan-local-tunnelip 27.0.0.12
        mtu 9000
     
    auto vxlan-2000
    iface vxlan-2000
        vxlan-id 2000
        vxlan-local-tunnelip 27.0.0.12
        mtu 9000
     
    auto br1000
    iface br1000
        bridge-ports host1 host2.1000 peerlink.1000 vxlan-1000
        bridge-stp on
        mstpctl-portbpdufilter vxlan-1000=yes
        mstpctl-bpduguard vxlan-1000=yes
        mstpctl-portautoedge host1=yes host2.1000=yes peerlink.1000=yes
     
    auto br2000
    iface br2000
        bridge-ports host1.2000 host2 peerlink.2000 vxlan-2000
        bridge-stp on
        mstpctl-portbpdufilter vxlan-2000=yes
        mstpctl-bpduguard vxlan-2000=yes
        mstpctl-portautoedge host1.2000=yes host2=yes peerlink.2000=yes

### <span>Quagga Configuration</span>

The layer 3 fabric can be configured using
[BGP](/version/cumulus-linux-2512-esr/Layer_3_Features/Configuring_Border_Gateway_Protocol_-_BGP)
or
[OSPF](/version/cumulus-linux-2512-esr/Layer_3_Features/Open_Shortest_Path_First_-_OSPF_-_Protocol).
The following example uses OSPF; the configuration needed in the MLAG
switches in the above specified topology is as follows:

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p><strong>leaf1:</strong> /etc/quagga/Quagga.conf</p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><pre><code>interface lo
 ip ospf area 0.0.0.0
interface swp1
 ip ospf network point-to-point
 ip ospf area 0.0.0.0
!
interface swp2
 ip ospf network point-to-point
 ip ospf area 0.0.0.0
!
interface swp3
 ip ospf network point-to-point
 ip ospf area 0.0.0.0
!
interface swp4
 ip ospf network point-to-point
 ip ospf area 0.0.0.0
!
!
!
!
!
router-id 10.2.1.1
router ospf
 ospf router-id 10.2.1.1</code></pre></td>
</tr>
</tbody>
</table></td>
<td><p><strong>leaf2:</strong> /etc/quagga/Quagga.conf</p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><pre><code>interface lo
 ip ospf area 0.0.0.0
interface swp1
 ip ospf network point-to-point
 ip ospf area 0.0.0.0
!
interface swp2
 ip ospf network point-to-point
 ip ospf area 0.0.0.0
!
interface swp3
 ip ospf network point-to-point
 ip ospf area 0.0.0.0
!
interface swp4
 ip ospf network point-to-point
 ip ospf area 0.0.0.0
!
!
!
!
!
router-id 10.2.1.2
router ospf
 ospf router-id 10.2.1.2</code></pre></td>
</tr>
</tbody>
</table></td>
</tr>
</tbody>
</table>

### <span>LNV Configuration</span>

The following configuration variables should be set in leaf1 and leaf2
in `/etc/vxrd.conf`. This configuration assumes head-end replication is
used to replicate BUM traffic. If service node based replication is
used, then `svcnode_ip` variable has to be set with service node
address. Please refer to [Configuring the Registration
Node](Lightweight_Network_Virtualization_-_LNV.html#src-5116051_LightweightNetworkVirtualization-LNV-regnode)
for setting that variable.

#### <span>leaf1 Configuration</span>

    # Local IP address to bind to for receiving control traffic from the snd
    src_ip = 27.0.0.11
    
    # Enable self replication
    # Note: Use true, or on, for True and 0, no, false, or off,
    # for False
    head_rep = true

#### <span>leaf2 Configuration</span>

    # Local IP address to bind to for receiving control traffic from the snd
    src_ip = 27.0.0.12
    
    # Enable self replication
    # Note: Use true, or on, for True and 0, no, false, or off,
    # for False
    head_rep = true

## <span id="src-5116066_LNVVXLANActive-ActiveMode-proto_down" class="confluence-anchor-link"></span><span>VXLAN PROTO\_DOWN State</span>

Similar to a bond interface, if MLAG detects a problem that could result
in connectivity issues such as traffic black-holing or a network
meltdown if the link carrier was left in an UP state, it can put VXLAN
interface into a [PROTO\_DOWN
state](Multi-Chassis_Link_Aggregation_-_MLAG.html#src-5116071_Multi-ChassisLinkAggregation-MLAG-proto_down).
Such connectivity issues include:

  - When the peer link goes down but the peer switch is up (that is, the
    backup link is active).

  - When an MLAG-enabled node is booted or rebooted, VXLAN interfaces
    are placed in a PROTO\_DOWN state until the node establishes a
    connection to its peer switch, detects existence of corresponding
    VXLAN interfaces in the peer switch, or five minutes have elapsed.

  - If the anycast address is not configured or if it is not the same in
    both MLAG switches, the VXLAN interfaces are placed into a
    PROTO\_DOWN state.

  - A configuration mismatch between the MLAG switches, such as the
    VXLAN interface is configured on just one of the switches or if the
    interface is shut down on one of the switches, then the VXLAN
    interface is placed into a PROTO\_DOWN state on the secondary
    switch.

You can use the `clagctl` command to check if any VXLAN devices are in a
PROTO\_DOWN state. As shown below, VXLAN devices are kept in a
PROTO\_DOWN state due to the missing anycast configuration.

    cumulus@switch$ clagctl
    The peer is alive
         Our Priority, ID, and Role: 4096 c4:54:44:bd:01:71 primary
        Peer Priority, ID, and Role: 8192 00:02:00:00:00:36 secondary
              Peer Interface and IP: peerlink.4094 169.254.0.2
                          Backup IP: 10.0.0.2 (active)
                         System MAC: 44:38:39:ff:ff:01
    
    CLAG Interfaces
    Our Interface      Peer Interface     CLAG Id   Conflicts              Proto-Down Reason
    ----------------   ----------------   -------   --------------------   -----------------
             host1     host2              1         -                      -              
             host1     host2              2         -                      -              
         vxlan-1000    -                  -         -                      vxlan-single,no-anycast-ip
         vxlan-2000    -                  -         -                      vxlan-single,no-anycast-ip

## <span>Caveats and Errata</span>

  - [VLAN-aware bridge
    mode](/version/cumulus-linux-2512-esr/Layer_1_and_Layer_2_Features/Ethernet_Bridging_-_VLANs/VLAN-aware_Bridge_Mode_for_Large-scale_Layer_2_Environments)
    is not supported for VXLAN active-active mode in this release.

  - The VLAN used for the peer link layer 3 subinterface should not be
    reused for any other interface in the system. It is recommended to
    use a high VLAN ID value. Read more about the [range of VLAN IDs you
    can
    use](VLAN-aware_Bridge_Mode_for_Large-scale_Layer_2_Environments.html#src-5116019_VLAN-awareBridgeModeforLarge-scaleLayer2Environments-range).

  - Active-active mode works only with LNV in this release. Integration
    with controller-based VXLANs such as VMware NSX and Midokura MidoNet
    will be supported in the future.
