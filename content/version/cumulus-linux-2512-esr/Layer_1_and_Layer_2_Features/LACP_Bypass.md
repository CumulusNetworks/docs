---
title: LACP Bypass
author: Cumulus Networks
weight: 103
aliases:
 - /display/CL25ESR/LACP+Bypass
 - /pages/viewpage.action?pageId=5116086
pageID: 5116086
product: Cumulus Linux
version: 2.5.12 ESR
imgData: cumulus-linux-2512-esr
siteSlug: cumulus-linux-2512-esr
---
On Cumulus Linux, *LACP Bypass* is a feature that allows a
[bond](/version/cumulus-linux-2512-esr/Layer_1_and_Layer_2_Features/Bonding_-_Link_Aggregation)
configured in 802.3ad mode to become active and forward traffic even
when there is no LACP partner. A typical use case for this feature is to
enable a host, without the capability to run LACP, to PXE boot while
connected to a switch on a bond configured in 802.3ad mode. Once the
pre-boot process finishes and the host is capable of running LACP, the
normal 802.3ad link aggregation operation takes over.

## <span>Understanding LACP Bypass Modes</span>

When a bond has multiple slave interfaces, you can control which of them
should go into LACP bypass using one of two modes:

  - *Priority mode*: This is the default mode. On a switch, if a bond
    has multiple slave interfaces, you can configure a bypass priority
    value (default is 0) for each interface in the bond; the one with
    higher numerical priority value wins. A string comparison of the
    interface names serves as a tiebreaker in case the priority values
    are equal; the string with the lower ASCII values wins. Note that
    the priority value is significant within a switch; there is no
    coordination between two switches in an
    [MLAG](/version/cumulus-linux-2512-esr/Layer_1_and_Layer_2_Features/Multi-Chassis_Link_Aggregation_-_MLAG)
    peering relationship.

  - *All-active mode*: In this mode, each bond slave interface operates
    as an active link while the bond is in bypass mode. This mode is
    useful during PXE boot of a server with multiple NICs, when the user
    cannot determine beforehand which port needs to be active. By
    default, all-active mode is disabled.
    
    {{%notice note%}}
    
    All-active mode is not supported on bonds that are not specified as
    bridge ports on the switch.
    
    {{%/notice%}}
    
    {{%notice note%}}
    
    STP does not run on the individual bond slave interfaces, when the
    LACP bond is in all-active mode. Therefore, only use all-active mode
    on host-facing LACP bonds. Cumulus Networks highly recommends you
    configure [STP BPDU
    guard](http://docs.cumulusnetworks.com/display/DOCS/Spanning+Tree+and+Rapid+Spanning+Tree#SpanningTreeandRapidSpanningTree-BPDUGuardandBridgeAssurance)
    along with all-active mode.
    
    {{%/notice%}}

### <span>LACP Bypass Timeout</span>

As a safeguard, you can configure a timeout period to limit the duration
in which bypass is enabled. The timeout period works with both modes.
The valid range of timeout period is 0 to 900 seconds; the default is 0
seconds, which indicates no timeout. If no LACP partner is detected
before the timeout period expires, the bond becomes inactive and stops
forwarding traffic. The timer is restarted when an slave interfaces are
enabled; which can be achieved by setting the interface down and then
up. At any point in time, receiving LACP PDU on any slave interface
aborts the bypass, and normal LACP protocol negotiation takes over.
Enabling or disabling bypass during LACP exchange does not affect link
aggregation.

## <span>LACP Bypass and MLAG Deployments</span>

In an [MLAG
deployment](/version/cumulus-linux-2512-esr/Layer_1_and_Layer_2_Features/Multi-Chassis_Link_Aggregation_-_MLAG)
where bond slaves of a host are connected to two switches and the bond
is in ***priority mode*** , the bypass priority is determined using the
MLAG switch role. The bond on the switch with the primary role has a
**higher** bypass priority than the bond on the switch with the
secondary role. When multiple slave interfaces of a bond are connected
to each switch, the slave with the highest priority on the primary MLAG
switch will be the active interface. All other slaves on the same device
will not be active during bypass mode.

When a dual-connected (MLAG) bond is in ***all-active mode*** , all the
slaves of bond are active on both the primary and secondary MLAG nodes.

## <span>Configuring LACP Bypass</span>

You configure LACP bypass in the `/etc/network/interfaces` file.

To enable LACP bypass on the host-facing bond, under the bond interface
stanza, set `bond-lacp-bypass-allow` to 1. Then optionally configure one
of the following:

  - To configure **priority mode**, which is the *default* mode, set
    `bond-lacp-bypass-priority` to a value, with the priority values for
    each slave interface. The default priority value is 0.

  - To configure **all-active mode** for multiple active interfaces, set
    `bond-lacp-bypass-all-active` to 1. This enables all interfaces to
    pass traffic (become active) until the server can form an LACP bond.

**(Optional):** To configure a timeout period for either mode, set
`bond-lacp-bypass-period` to a valid value (0-900); however, it is
recommended to not configure this, and use the default value of 0.

## <span>Configuration Examples</span>

### <span>Default Configuration with Priority Mode and Optional Timeout Period</span>

The following configuration shows LACP bypass enabled in the default
priority mode, with a timeout period set. Here there are two slave
interfaces, and swp2 will be preferred as the active bypass interface:

    auto bond0
    iface bond0
          bond-lacp-bypass-allow 1
          bond-slaves swp4 swp5
          bond-lacp-bypass-period 300
          bond-lacp-bypass-priority swp4=2 swp5=1

The following command shows that swp4 bypass timeout has expired and the
bond is operationally down:

    cumulus@switch$ ip link show bond0
    7: bond0: <NO-CARRIER,BROADCAST,MULTICAST,MASTER,UP> mtu 1500 qdisc noqueue state DOWN mode DEFAULT
      link/ether 00:02:00:00:00:02 brd ff:ff:ff:ff:ff:ff
    cumulus@switch$ cat /proc/net/bonding/bond0
    Ethernet Channel Bonding Driver: v3.7.1 (April 27, 2011)
    Bonding Mode: IEEE 802.3ad Dynamic link aggregation
    Transmit Hash Policy: layer2 (0)
    MII Status: up
    MII Polling Interval (ms): 0
    Up Delay (ms): 0
    Down Delay (ms): 0
    802.3ad info
    LACP rate: fast
    Min links: 1
    Aggregator selection policy (ad_select): stable
    System Identification: 65535 00:02:00:00:00:02
    Active Aggregator Info:
          Aggregator ID: 1
          Number of ports: 1
          Actor Key: 33
          Partner Key: 1
          Partner Mac Address: 00:00:00:00:00:00
    Fall back Info:
           Allowed: 1
           Timeout: 300
    Slave Interface: swp4
    MII Status: up
    Speed: 10000 Mbps
    Duplex: full
    Link Failure Count: 0
    Permanent HW addr: 00:02:00:00:00:02
    Aggregator ID: 1
    LACP bypass priority: 2
    LACP bypass: expired
    Slave queue ID: 0
    Slave Interface: swp5
    MII Status: up
    Speed: 10000 Mbps
    Duplex: full
    Link Failure Count: 0
    Permanent HW addr: 00:02:00:00:00:01
    Aggregator ID: 2
    Bypass priority: 1
    Slave queue ID: 0

### <span>All-active Mode Configuration with Multiple Simultaneous Active Interfaces</span>

The following configuration shows LACP bypass enabled for multiple
active interfaces (all-active mode) with a bridge in [VLAN-aware
mode](/version/cumulus-linux-2512-esr/Layer_1_and_Layer_2_Features/Ethernet_Bridging_-_VLANs/VLAN-aware_Bridge_Mode_for_Large-scale_Layer_2_Environments):

    auto bond1
    iface bond1 inet static
        bond-slaves swp3 swp4
        bond-lacp-bypass-allow 1
        bond-lacp-bypass-all-active 1
    
    auto br0
    iface br0 inet static
        bridge-vlan-aware yes
        bridge-ports bond1 bond2 bond3 bond4 peer5
        bridge-stp on
        bridge-vids 100-105
        mstpctl-bpduguard bond1=yes
    
    
    cumulus@switch:~$ ip link show bond1
    58: bond1: <BROADCAST,MULTICAST,MASTER,UP,LOWER_UP> mtu 1500 qdisc noqueue master br0 state UP mode DORMANT
        link/ether 44:38:39:00:38:44 brd ff:ff:ff:ff:ff:ff
    cumulus@switch:~$ ip link show swp3
    5: swp3: <BROADCAST,MULTICAST,SLAVE,UP,LOWER_UP> mtu 1500 qdisc pfifo_fast master bond1 state UP mode DEFAULT qlen 500
        link/ether 44:38:39:00:38:44 brd ff:ff:ff:ff:ff:ff
    cumulus@switch:~$ ip link show swp4
    6: swp4: <BROADCAST,MULTICAST,SLAVE,UP,LOWER_UP> mtu 1500 qdisc pfifo_fast master bond1 state UP mode DEFAULT qlen 500
        link/ether 44:38:39:00:38:44 brd ff:ff:ff:ff:ff:ff
    
      
    cumulus@switch:~$ cat /proc/net/bonding/bond1
    Ethernet Channel Bonding Driver: v3.7.1 (April 27, 2011)
    
    Bonding Mode: IEEE 802.3ad Dynamic link aggregation
    Transmit Hash Policy: layer3+4 (1)
    MII Status: up
    MII Polling Interval (ms): 100
    Up Delay (ms): 0
    Down Delay (ms): 0
    
    802.3ad info
    LACP rate: fast
    Min links: 1
    Aggregator selection policy (ad_select): stable
    System Identification: 65535 00:00:00:aa:bb:01
    Active Aggregator Info:
            Aggregator ID: 1
            Number of ports: 1
            Actor Key: 33
            Partner Key: 33
            Partner Mac Address: 00:02:00:00:00:05
    LACP Bypass Info:
            Allowed: 1
            Timeout: 0
            All-active: 1
    
    Slave Interface: swp3
    MII Status: up
    Speed: 10000 Mbps
    Duplex: full
    Link Failure Count: 1
    Permanent HW addr: 44:38:39:00:38:44
    Aggregator ID: 1
    LACP bypass priority: 0
    LACP bypass: on
    Slave queue ID: 0
    
    Slave Interface: swp4
    MII Status: up
    Speed: 10000 Mbps
    Duplex: full
    Link Failure Count: 1
    Permanent HW addr: 44:38:39:00:38:45
    Aggregator ID: 2
    LACP bypass priority: 0
    LACP bypass: on
    Slave queue ID: 0

The following configuration shows LACP bypass enabled for multiple
active interfaces (all-active mode) with a bridge in [traditional bridge
mode](/version/cumulus-linux-2512-esr/Layer_1_and_Layer_2_Features/Ethernet_Bridging_-_VLANs/):

    auto bond1
    iface bond1 inet static
        bond-slaves swp3 swp4
        bond-lacp-bypass-allow 1
        bond-lacp-bypass-all-active 1
    
    auto br0
    iface br0 inet static
        bridge-ports bond1 bond2 bond3 bond4 peer5
        bridge-stp on
        mstpctl-bpduguard bond1=yes
