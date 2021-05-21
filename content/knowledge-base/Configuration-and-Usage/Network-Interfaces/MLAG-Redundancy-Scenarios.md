---
title: MLAG Redundancy Scenarios
author: Cumulus Networks
weight: 416
toc: 4
---

## Issue

Cumulus Linux Multi-Chassis Link Aggregation (MLAG) enables two switches to operate at layer 2 as if they are a single logical L2 switch in order to provide greater throughput and redundancy. This article discusses expected LACP and STP behavior during common failure redundancy scenarios. It is assumed the reader has a working knowledge of Cumulus Linux MLAG, LACP bonding, and STP. MLAG capabilities and configuration instructions are provided in the [Cumulus Linux user guide]({{<ref "/cumulus-linux-43/Layer-2/Multi-Chassis-Link-Aggregation-MLAG" >}}).

## Environment

- Cumulus Linux, all versions

## MLAG Steady State Overview

Each MLAG peer switch considers bond interfaces as either single- or dual-attached. A single-attached bond is an LACP bond interface that is configured with a `clag-id` but is currently active on just one peer.

A dual-attached bond is an LACP bond that is configured with a `clag-id` and is currently active on both MLAG peers. A dual-attached bond can be identified by the *D* flag in the **LACP Information** field of `clagctl -v` output.

In the following example, Bond1 is dual-attached. Bond2 is currently down on sw28. Therefore, Bond2 is single-attached to sw27.

    cumulus@switch$ ip link show bond1
    root@sw27:~ # clagctl -v
    The peer is alive
      Our Priority, ID, and Role: 4096 70:72:cf:9d:48:06 primary
     Peer Priority, ID, and Role: 8192 70:72:cf:9d:4e:36 secondary
          Peer Interface and IP: peerlink.4094 1.1.1.2
                      Backup IP: (inactive)
                     System MAC: 44:39:39:ff:00:01
    
    CLAG Interfaces
    Our Interface    Peer Interface   CLAG Id Conflicts            Proto-Down Reason
    ---------------- ---------------- ------- -------------------- -----------------
               Bond1 Bond1            81      -                    - 
               Bond2 -                82      -                    -
    
    Our LACP Information
    Our Interface    Partner MAC CIST  PortId CLAG Id Oper St Flags
    ---------------- ----------------- ----------- ------- ------- -----
    Bond1            00:e0:ec:27:36:37 None        81      None    D 
    Bond2            00:e0:ec:27:43:51 None        82      None    -
    
    Peer LACP Information
    Peer Interface   Partner MAC       CIST PortId CLAG Id Oper St Flags
    ---------------- ----------------- ----------- ------- ------- -----
    Bond1            00:e0:ec:27:36:37 None        81      None     D 
    Bond2            00:00:00:00:00:00 None        82      None     -

In the steady state, the local LACP system ID used for MLAG bonds is the `clagd-sys-mac` address.

A peer switch may also have additional *orphan ports* &mdash; layer 2 interfaces or bonds not configured with a `clag-id`. The LACP system ID for these bonds is the bond MAC address. Orphan ports can participate in STP along with the MLAG bond members.

In the following example, the bridge *vlans* contains the two MLAG bonds, Bond1 and Bond2, and also two orphan ports, swp28 and bond3, which is not in the MLAG pair.

    root@sw27:~ # brctl show
    bridge name bridge id STP enabled interfaces
    vlans 8000.7072cf9d4806 yes peerlink
    swp28
    Bond1
    Bond2
    bond3

In steady state, the MLAG pair must appear to the connected layer 2 network as a single switch. Therefore both primary and secondary MLAG switches use the `clagd-sys-mac` address as the common STP bridge ID on all ports. Both primary and secondary switches transmit BPDUs on orphan and single-connected ports. Only the primary switch **sends** BPDUs on dual-connected bonds. Both the primary and secondary **receive** BPDUs on dual-connected bonds.

There is no requirement for MLAG peers to be the spanning tree root. However, as with all layer 2 topologies, the forwarding topology can be affected by the location of the root bridge. Therefore, it is useful to set the spanning tree priority using `mstpctl-treeprio` to aid in the selection of an optimal root. When configuring `mstpctl-treeprio`, both peers should be configured with the same priority.

`mstpctl showall` is used to show spanning tree status, including specific MLAG spanning tree state information. For dual-connected bonds, the MLAG dual-connected MAC address is the MAC address of the dual-connected LACP bond partner.

    clag ISL no clag ISL Oper UP no
     clag role primary clag dual conn mac 00:E0:EC:27:36:37
     clag remote portID F.FFF clag system mac 44:39:39:FF:00:01

When a bond is single-connected, the MLAG dual-connected MAC address is null.

    clag ISL yes clag ISL Oper UP yes
     clag role primary clag dual conn mac 00:00:00:00:00:00
     clag remote portID F.FFF clag system mac 44:39:39:FF:00:01

## Redundancy Failure Scenarios

### Scenario 1: Peer Link Failure, clagd-backup-ip Is Active

Cumulus Networks recommends specifying a backup link to check the health of the peer switch in the event that the peer link goes down. The backup link serves to distinguish between a peer-link failure and a peer switch failure.

You configure the backup link using `clagd-backup-ip`. If `clagd-backup-ip` is active (that is, the backup IP address is reachable) when a peer link failure occurs, the secondary switch uses it to determine whether the primary peer is still active (or alive — the switch is up; however, the peer link could be down). Since the primary is still active, the primary peer will continue to use pre-existing LACP system IDs for all bonds. The primary will also continue to use `clagd-sys-mac` as the STP bridge ID for all ports.

In this scenario, the secondary switch cannot continue to operate as single switch with its peer. Accordingly, the secondary peer shuts down the member links for the dual-connected bonds. Since the primary peer is indeed up in this scenario, the primary switch continues to maintain its LACP sessions with the remote systems. As a result, traffic flow to and from the dual-attached bonds transitions to the primary peer.

Orphan ports attached to the secondary switch remain up. However, the secondary switch starts to use its local interface MAC address instead of the `clagd-sys-mac` for the STP bridge ID on all ports.

The following `tcpdump` output shows the bridge ID changing from the `clagd-sys-mac` (44:39:39:ff:00:01) to the local MAC (70:72:cf:9d:4e:36):

    root@sw20:~ # tcpdump -i swp26s1 stp 
    tcpdump: WARNING: swp26s1: no IPv4 address assigned
    tcpdump: verbose output suppressed, use -v or -vv for full protocol decode
    listening on swp26s1, link-type EN10MB (Ethernet), capture size 65535 bytes
    16:30:59.550638 STP 802.1w, Rapid STP, Flags [Learn, Forward, Agreement], bridge-id 0000.44:39:39:ff:00:01.8005, length 43
    16:31:01.550954 STP 802.1w, Rapid STP, Flags [Learn, Forward, Agreement], bridge-id 0000.44:39:39:ff:00:01.8005, length 43
    16:31:02.590928 STP 802.1w, Rapid STP, Flags [Proposal], bridge-id 0000.70:72:cf:9d:4e:36.8005, length 43
    16:31:02.590968 STP 802.1w, Rapid STP, Flags [Proposal, Agreement], bridge-id 0000.70:72:cf:9d:4e:36.8005, length 43
    16:31:04.550856 STP 802.1w, Rapid STP, Flags [Proposal, Agreement], bridge-id 0000.70:72:cf:9d:4e:36.8005, length 43
    16:31:06.550882 STP 802.1w, Rapid STP, Flags [Proposal, Learn, Forward, Agreement], bridge-id 0000.70:72:cf:9d:4e:36.8005, length 43
    16:31:07.376348 STP 802.1w, Rapid STP, Flags [Proposal, Agreement], bridge-id 8000.00:e0:ec:27:43:51.8002, length 36
    16:31:07.377232 STP 802.1w, Rapid STP, Flags [Topology change, Learn, Forward], bridge-id 0000.70:72:cf:9d:4e:36.8005, length 43
    16:31:07.377268 STP 802.1w, Rapid STP, Flags [Topology change, Learn, Forward, Agreement], bridge-id 0000.70:72:cf:9d:4e:36.8005, length 43

{{%notice note%}}

The change in the STP bridge ID on the secondary switch results in a layer 2 bridge topology change.

{{%/notice%}}

### Scenario 2: Peer Link Failure, clagd-backup-ip Is not Active

If `clagd-backup-ip` is not active when the peer link failure occurs, the secondary must assume that the primary may still be active. Since the primary peer is still active in this scenario, the primary peer continues to use pre-existing LACP system IDs for all bonds. The primary also continues to use the `clagd-sys-mac` as the STP bridge ID for all ports.

However, the secondary peer cannot continue to use the common `clagd-sys-mac` address as its LACP system ID. The secondary peer begins to use the bond interface MAC address as the LACP system ID.

The following `tcpdump` output shows the LACP system ID change when the peer link went down.

    root@sw20:~ # tcpdump -i swp26s0 ether proto 0x8809 -evx | grep "70:72:cf:9d:4e:4d" -A3
    tcpdump: WARNING: swp26s0: no IPv4 address assigned
    tcpdump: listening on swp26s0, link-type EN10MB (Ethernet), capture size 65535 bytes
    15:45:28.526237 70:72:cf:9d:4e:4d (oui Unknown) > 01:80:c2:00:00:02 (oui Unknown), ethertype Slow Protocols (0x8809), length 124: LACPv1, length 110
     Actor Information TLV (0x01), length 20
     System 44:39:39:ff:00:01 (oui Unknown), System Priority 65535, Key 33, Port 1, Port Priority 255
     State Flags [Activity, Timeout, Aggregation, Synchronization, Collecting, Distributing]
    --
    15:45:29.726281 70:72:cf:9d:4e:4d (oui Unknown) > 01:80:c2:00:00:02 (oui Unknown), ethertype Slow Protocols (0x8809), length 124: LACPv1, length 110
     Actor Information TLV (0x01), length 20
     System 70:72:cf:9d:4e:4d (oui Unknown), System Priority 65535, Key 33, Port 1, Port Priority 255
     State Flags [Activity, Timeout, Aggregation, Synchronization]

Since the primary peer is indeed up in this scenario, the primary switch maintains its LACP sessions with the remote systems. Accordingly, the remote systems cannot establish the LACP session with the secondary. Therefore, the dual-attached bonds on the secondary revert to the NO-CARRIER state.

The following shows that the underlying bond member link is up, but the bond is down:

    root@sw28:~ # ip link show swp25
    27: swp25: <BROADCAST,MULTICAST,SLAVE,UP,LOWER_UP> mtu 1500 qdisc pfifo_fast master Bond2 state UP mode DEFAULT qlen 500
     link/ether 70:72:cf:9d:4e:4d brd ff:ff:ff:ff:ff:ff
     
    root@sw28:~ # ip link show Bond2
    69: Bond2: <NO-CARRIER,BROADCAST,MULTICAST,MASTER,UP> mtu 1500 qdisc noqueue master vlans state DOWN mode DORMANT 
     link/ether 70:72:cf:9d:4e:4d brd ff:ff:ff:ff:ff:ff

Traffic flow to/from the dual-attached bonds transition to the active peer. Orphan ports remain up on the secondary switch. However, the secondary switch begins to use a local interface MAC address instead of the `clagd-sys-mac` for the STP bridge ID on all ports.

Note that the change in STP bridge ID on the secondary switch may result in STP convergence.

### Scenario 3: Primary Power Off, clagd-backup-ip Is Active

When the primary is powered off, secondary uses the `clagd-backup-ip` to determine that primary peer is no longer active. Since the primary is powered off, it is expected that links (bonds) must also be down between the remote system and primary.

Orphan ports attached to the primary peer are out of service until the primary is restored.

The secondary peer transitions to the primary role. Accordingly, it continues to use preexisting LACP system IDs for all bonds. It also begins transmitting BPDUs on the MLAG bonds.

When the original primary switch is powered back on, it is expected to re-assume primary role.

### Scenario 4: Primary Power Off, clagd-backup-ip Is not Active

If `clagd-backup-ip` is not active when a primary switch is powered off, the secondary must assume that the primary is still active. Since the primary is indeed not active, the bonds between the primary switch and the remote systems get down.

Orphan ports attached to the primary peer are out of service until the primary is restored.

Just as in the peer link failure scenario, when `clagd-backup-ip` is not active, the secondary peer cannot continue to use the common `clagd-sys-mac` address as its LACP system ID. Therefore the secondary switch now starts using the bond interface MAC address for the LACP system ID.

In this case, since primary is indeed down, the bonds from the secondary will come up. The secondary will also begin to use its local interface MAC instead of `clagd-sys-mac` form the STP bridge ID on all ports.

### Scenario 5: Primary Reboot via reboot Command

When the primary switch is rebooted via the `reboot` command, the primary switch sends a goodbye message to the secondary switch informing the secondary to assume the primary role. The primary also brings down bonds with `clag-id`s. As a result, traffic flow transitions to the other peer.

Orphan ports attached to the primary peer go out of service until the primary is restored.

The secondary peer transitions to the primary role. Accordingly, it continues to use preexisting LACP system IDs for all bonds. It also begins to transmit BPDUs on the MLAG bonds.

When the original primary switch is powered back on, it should resume the primary role.

### Scenario 6: Secondary Power Off or Reboot

The primary peer maintains the primary role and continues to use preexisting LACP system IDs and the `clag-sys-mac` address as the STP bridge ID. Traffic flow to and from the dual-attached bonds should transition from the secondary peer to the primary peer.

Orphan ports connected to the secondary peer are out of service until the secondary switch recovers.

When the secondary switch is powered back on. It is expected to re-assume secondary role.
