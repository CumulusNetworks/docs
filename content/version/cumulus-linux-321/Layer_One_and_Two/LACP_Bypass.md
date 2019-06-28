---
title: LACP Bypass
author: Cumulus Networks
weight: 113
aliases:
 - /display/CL321/LACP+Bypass
 - /pages/viewpage.action?pageId=5126871
pageID: 5126871
product: Cumulus Linux
version: 3.2.1
imgData: cumulus-linux-321
siteSlug: cumulus-linux-321
---
On Cumulus Linux, *LACP Bypass* is a feature that allows a
[bond](/version/cumulus-linux-321/Layer_One_and_Two/Bonding_-_Link_Aggregation)
configured in 802.3ad mode to become active and forward traffic even
when there is no LACP partner. A typical use case for this feature is to
enable a host, without the capability to run LACP, to PXE boot while
connected to a switch on a bond configured in 802.3ad mode. Once the
pre-boot process finishes and the host is capable of running LACP, the
normal 802.3ad link aggregation operation takes over.

## <span>Understanding the LACP Bypass All-active Mode</span>

When a bond has multiple slave interfaces, each bond slave interface
operates as an active link while the bond is in bypass mode. This is
known as *all-active mode*. This is useful during PXE boot of a server
with multiple NICs, when the user cannot determine beforehand which port
needs to be active.

Keep in the mind the following caveats with all-active mode:

  - All-active mode is not supported on bonds that are not specified as
    bridge ports on the switch.

  - Spanning tree protocol (STP) does not run on the individual bond
    slave interfaces when the LACP bond is in all-active mode.
    Therefore, only use all-active mode on host-facing LACP bonds.
    Cumulus Networks highly recommends you configure [STP BPDU
    guard](Spanning_Tree_and_Rapid_Spanning_Tree.html#src-5126866_SpanningTreeandRapidSpanningTree-bpdu)
    along with all-active mode.

{{%notice note%}}

The following features are not supported:

  - priority mode

  - bond-lacp-bypass-period

  - bond-lacp-bypass-priority

  - bond-lacp-bypass-all-active

{{%/notice%}}

### <span>LACP Bypass and MLAG Deployments</span>

In an [MLAG
deployment](/version/cumulus-linux-321/Layer_One_and_Two/Multi-Chassis_Link_Aggregation_-_MLAG)
where bond slaves of a host are connected to two switches and the bond
is in all-active mode, all the slaves of bond are active on both the
primary and secondary MLAG nodes.

## <span>Configuring LACP Bypass</span>

To enable LACP bypass on the host-facing bond, set
`bond-lacp-bypass-allow` to *yes*.

{{%notice info has%}}

**Example VLAN-aware Bridge Mode Configuration**

The following commands create a VLAN-aware bridge with LACP bypass
enabled:

    cumulus@switch:~$ net add bond bond1 bond slaves swp51s2,swp51s3
    cumulus@switch:~$ net add bond bond1 clag id 1
    cumulus@switch:~$ net add bond bond1 bond lacp-bypass-allow
    cumulus@switch:~$ net add bond bond1 stp bpduguard
    cumulus@switch:~$ net add bridge bridge ports bond1,bond2,bond3,bond4,peer5
    cumulus@switch:~$ net add bridge bridge vids 100-105
    cumulus@switch:~$ net pending
    cumulus@switch:~$ net commit

These commands create the following stanzas in
`/etc/network/interfaces`:

    auto bond1
    iface bond1
        bond-lacp-bypass-allow yes
        bond-slaves swp51s2 swp51s3
        clag-id 1
        mstpctl-bpduguard yes
     
    ...
     
    auto bridge
    iface bridge
        bridge-ports bond1 bond2 bond3 bond4 peer5
        bridge-vids 100-105
        bridge-vlan-aware yes

{{%/notice%}}

You can check the status of the configuration by running `net show
interface <bond>` on the bond and its slave interfaces:

    cumulus@switch:~$ net show interface bond1
     
       Name   MAC               Speed   MTU   Mode
    -- ------ ----------------- ------- ----- ----------
    UP bond1  44:38:39:00:00:5b 1G      1500  Bond/Trunk
     
     
    Bond Details
    ------------------ -------------------------
    Bond Mode:         LACP
    Load Balancing:    Layer3+4
    Minimum Links:     1
    In CLAG:           CLAG Active
    LACP Sys Priority:
    LACP Rate:         Fast Timeout
    LACP Bypass:       LACP Bypass Not Supported
     
     
       Port       Speed     TX   RX   Err   Link Failures
    -- --------   ------- ---- ---- ----- ---------------
    UP swp51s2(P) 1G         0    0     0               0
    UP swp51s3(P) 1G         0    0     0               0
     
     
    All VLANs on L2 Port
    ----------------------
    100-105
     
     
    Untagged
    ----------
    1
     
     
    Vlans in disabled State
    -------------------------
    100-105
     
     
    LLDP
    --------   ---- ------------------
    swp51s2(P) ==== swp1(spine01)
    swp51s3(P) ==== swp1(spine02)

Use the `cat` command to verify that LACP bypass is enabled on a bond
and its slave interfaces:

    cumulus@switch:~$ cat /sys/class/net/bond1/bonding/lacp_bypass 
    on 1
    cumulus@switch:~$ cat /sys/class/net/bond1/bonding/slaves
    swp51 swp52
    cumulus@switch:~$ cat /sys/class/net/swp52/bonding_slave/ad_rx_bypass 
    1
    cumulus@switch:~$ cat /sys/class/net/swp51/bonding_slave/ad_rx_bypass 
    1

### <span>Traditional Bridge Mode Configuration</span>

The following configuration shows LACP bypass enabled for multiple
active interfaces (all-active mode) with a bridge in [traditional bridge
mode](/version/cumulus-linux-321/Layer_One_and_Two/Ethernet_Bridging_-_VLANs/Traditional_Mode_Bridges):

    auto bond1
    iface bond1 
        bond-slaves swp3 swp4
        bond-lacp-bypass-allow 1
     
    auto br0
    iface br0
        bridge-ports bond1 bond2 bond3 bond4 peer5
        mstpctl-bpduguard bond1=yes
