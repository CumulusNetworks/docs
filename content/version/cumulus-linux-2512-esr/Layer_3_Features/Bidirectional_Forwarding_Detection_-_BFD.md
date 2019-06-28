---
title: Bidirectional Forwarding Detection - BFD
author: Cumulus Networks
weight: 137
aliases:
 - /display/CL25ESR/Bidirectional+Forwarding+Detection+-+BFD
 - /pages/viewpage.action?pageId=5116125
pageID: 5116125
product: Cumulus Linux
version: 2.5.12 ESR
imgData: cumulus-linux-2512-esr
siteSlug: cumulus-linux-2512-esr
---
*Bidirectional Forwarding Detection* (BFD) provides low overhead and
rapid detection of failures in the paths between two network devices. It
provides a unified mechanism for link detection over all media and
protocol layers. Use BFD to detect failures for IPv4 and IPv6 single or
multihop paths between any two network devices, including unidirectional
path failure detection.

{{%notice note%}}

Cumulus Linux does not support demand mode in BFD.

{{%/notice%}}

## <span>Using BFD Multihop Routed Paths</span>

BFD multihop sessions are built over arbitrary paths between two
systems, which results in some complexity that does not exist for single
hop sessions. Here are some best practices for using multihop paths:

  - **Spoofing:** To avoid spoofing with multihop paths, configure
    `max_hop_cnt` (maximum hop count*)* for each peer, which limits the
    number of hops for a BFD session. All BFD packets exceeding the max
    hop count will be dropped.

  - **Demultiplexing:** Since multihop BFD sessions can take arbitrary
    paths, demultiplex the initial BFD packet based on the
    source/destination IP address pair. Use Quagga, which monitors
    connectivity to the peer, to determine the source/destination IP
    address pairs.

Multihop BFD sessions are supported for both IPv4 and IPv6 peers. See
below for more details.

## <span>BFD Parameters</span>

You can configure the following BFD parameters for both IPv4 and IPv6
sessions:

  - The required minimum interval between the received BFD control
    packets.

  - The minimum interval for transmitting BFD control packets.

  - The detection time multiplier.

## <span>Configuring BFD</span>

You configure BFD one of two ways: by specifying the configuration in
the [PTM `topology.dot`
file](/version/cumulus-linux-2512-esr/Layer_1_and_Layer_2_Features/Prescriptive_Topology_Manager_-_PTM),
or using
[Quagga](/version/cumulus-linux-2512-esr/Layer_3_Features/Quagga_Overview).

The [Quagga
CLI](#src-5116125_BidirectionalForwardingDetection-BFD-quagga) can track
IPv4 and IPv6 peer connectivity — both single hop and multihop, and both
link-local IPv6 peers and global IPv6 peers — using BFD sessions without
needing the `topology.dot` file. Use Quagga to register multihop peers
with PTM and BFD as well as for monitoring the connectivity to the
remote BGP multihop peer. Quagga can dynamically register and unregister
both IPv4 and IPv6 peers with BFD when the BFD-enabled peer connectivity
is established or de-established, respectively. Also, you can configure
BFD parameters for each BGP or OSPF peer using Quagga.

{{%notice note%}}

The BFD parameter configured in the topology file is given higher
precedence over the client-configured BFD parameters for a BFD session
that has been created by both topology file and client (Quagga).

{{%/notice%}}

### <span>BFD in BGP</span>

For Quagga when using **BGP**, neighbors are registered and
de-registered with
[PTM](/version/cumulus-linux-2512-esr/Layer_1_and_Layer_2_Features/Prescriptive_Topology_Manager_-_PTM)
dynamically when you enable BFD in BGP:

    quagga(config)# router bgp X
    quagga(config-router)# neighbor <neighbor ip> bfd

You can configure BFD parameters for each BGP neighbor. For example:

    null

To see neighbor information in BGP, including BFD status, run `show bgp
neighbors <IP address>`.

    quagga# show bgp neighbors 12.12.12.1
    BGP neighbor is 12.12.12.1, remote AS 65001, local AS 65000, external link
    Hostname: r1
      BGP version 4, remote router ID 0.0.0.1
      BGP state = Established, up for 00:01:39
      Last read 00:00:39, Last write 00:01:09
      Hold time is 180, keepalive interval is 60 seconds
      Neighbor capabilities:
        4 Byte AS: advertised and received
        AddPath:
          IPv4 Unicast: RX advertised and received
        Route refresh: advertised and received(old & new)
        Address family IPv4 Unicast: advertised and received
        Hostname Capability: advertised and received
        Graceful Restart Capabilty: advertised and received
          Remote Restart timer is 120 seconds
          Address families by peer:
            none
      Graceful restart informations:
        End-of-RIB send: IPv4 Unicast
        End-of-RIB received: IPv4 Unicast
      Message statistics:
        Inq depth is 0
        Outq depth is 0
                             Sent       Rcvd
        Opens:                  1          1
        Notifications:          0          0
        Updates:                2          2
        Keepalives:             2          1
        Route Refresh:          0          0
        Capability:             0          0
        Total:                  5          4
      Minimum time between advertisement runs is 30 seconds
      Update source is 12.12.12.7
     
     For address family: IPv4 Unicast
      Update group 1, subgroup 1
      Packet Queue length 0
      NEXT_HOP is always this router
      Community attribute sent to this neighbor(both)
      1 accepted prefixes
      Connections established 1; dropped 0
      Last reset never
      External BGP neighbor may be up to 2 hops away.
    Local host: 12.12.12.7, Local port: 34274
    Foreign host: 12.12.12.1, Foreign port: 179
    Nexthop: 12.12.12.7
    Nexthop global: ::
    Nexthop local: ::
    BGP connection: non shared network
    Read thread: on  Write thread: off
      BFD: Type: multi hop
        Detect Mul: 3, Min Rx interval: 300, Min Tx interval: 300
        Status: Down, Last update: 0:00:00:13

### <span>BFD in OSPF</span>

For Quagga using **OSFP**, neighbors are registered and de-registered
dynamically with
[PTM](/version/cumulus-linux-2512-esr/Layer_1_and_Layer_2_Features/Prescriptive_Topology_Manager_-_PTM)
when you enable or disable BFD in OSPF. A neighbor is registered with
BFD when two-way adjacency is established and deregistered when
adjacency goes down if the BFD is enabled on the interface. The BFD
configuration is per interface and any IPv4 and IPv6 neighbors
discovered on that interface inherit the configuration.

    quagga(config)# interface X
    quagga(config-if)# ipv6 ospf6 bfd
        <2-255> Detect Multiplier
        <cr>
    quagga(config-if)# ipv6 ospf6 bfd 5
        <50-60000> Required min receive interval
    quagga(config-if)# ipv6 ospf6 bfd 5 500
        <50-60000> Desired min transmit interval
    quagga(config-if)# ipv6 ospf6 bfd 5 500 500
        <cr>
    quagga(config-if)# ipv6 ospf6 bfd 5 500 500

### <span>OSPF Show Commands</span>

The BFD lines at the end of each code block shows the corresponding IPv6
or IPv4 OSPF interface or neighbor information.

    quagga# show ipv6 ospf6 interface swp2s0
    swp2s0 is up, type BROADCAST
      Interface ID: 4
      Internet Address:
        inet : 11.0.0.21/30
        inet6: fe80::4638:39ff:fe00:6c8e/64
      Instance ID 0, Interface MTU 1500 (autodetect: 1500)
      MTU mismatch detection: enabled
      Area ID 0.0.0.0, Cost 10
      State PointToPoint, Transmit Delay 1 sec, Priority 1
      Timer intervals configured:
       Hello 10, Dead 40, Retransmit 5
      DR: 0.0.0.0 BDR: 0.0.0.0
      Number of I/F scoped LSAs is 2
        0 Pending LSAs for LSUpdate in Time 00:00:00 [thread off]
        0 Pending LSAs for LSAck in Time 00:00:00 [thread off]
      BFD: Detect Mul: 3, Min Rx interval: 300, Min Tx interval: 300

    quagga# show ipv6 ospf6 neighbor detail
     Neighbor 0.0.0.4%swp2s0
        Area 0.0.0.0 via interface swp2s0 (ifindex 4)
        His IfIndex: 3 Link-local address: fe80::202:ff:fe00:a
        State Full for a duration of 02:32:33
        His choice of DR/BDR 0.0.0.0/0.0.0.0, Priority 1
        DbDesc status: Slave SeqNum: 0x76000000
        Summary-List: 0 LSAs
        Request-List: 0 LSAs
        Retrans-List: 0 LSAs
        0 Pending LSAs for DbDesc in Time 00:00:00 [thread off]
        0 Pending LSAs for LSReq in Time 00:00:00 [thread off]
        0 Pending LSAs for LSUpdate in Time 00:00:00 [thread off]
        0 Pending LSAs for LSAck in Time 00:00:00 [thread off]
        BFD: Type: single hop
          Detect Mul: 3, Min Rx interval: 300, Min Tx interval: 300
          Status: Up, Last update: 0:00:00:20

    quagga# show ip ospf interface swp2s0
    swp2s0 is up
      ifindex 4, MTU 1500 bytes, BW 0 Kbit <UP,BROADCAST,RUNNING,MULTICAST>
      Internet Address 11.0.0.21/30, Area 0.0.0.0
      MTU mismatch detection:enabled
      Router ID 0.0.0.3, Network Type POINTOPOINT, Cost: 10
      Transmit Delay is 1 sec, State Point-To-Point, Priority 1
      No designated router on this network
      No backup designated router on this network
      Multicast group memberships: OSPFAllRouters
      Timer intervals configured, Hello 10s, Dead 40s, Wait 40s, Retransmit 5
        Hello due in 7.056s
      Neighbor Count is 1, Adjacent neighbor count is 1
      BFD: Detect Mul: 5, Min Rx interval: 500, Min Tx interval: 500

    quagga# show ip ospf neighbor detail
     Neighbor 0.0.0.4, interface address 11.0.0.22
        In the area 0.0.0.0 via interface swp2s0
        Neighbor priority is 1, State is Full, 5 state changes
        Most recent state change statistics:
          Progressive change 3h59m04s ago
        DR is 0.0.0.0, BDR is 0.0.0.0
        Options 2 *|-|-|-|-|-|E|*
        Dead timer due in 38.501s
        Database Summary List 0
        Link State Request List 0
        Link State Retransmission List 0
        Thread Inactivity Timer on
        Thread Database Description Retransmision off
        Thread Link State Request Retransmission on
        Thread Link State Update Retransmission on
        BFD: Type: single hop
          Detect Mul: 5, Min Rx interval: 500, Min Tx interval: 500
          Status: Down, Last update: 0:00:01:29

## <span>Troubleshooting BFD</span>

To troubleshoot BFD, use `ptmctl -b`. For more information, see
[Prescriptive Topology Manager -
PTM](/version/cumulus-linux-2512-esr/Layer_1_and_Layer_2_Features/Prescriptive_Topology_Manager_-_PTM).
