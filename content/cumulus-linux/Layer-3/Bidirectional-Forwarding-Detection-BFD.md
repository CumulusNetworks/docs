---
title: Bidirectional Forwarding Detection - BFD
author: Cumulus Networks
weight: 187
aliases:
 - /display/DOCS/Bidirectional+Forwarding+Detection+++BFD
 - /display/DOCS/Bidirectional+Forwarding+Detection+-+BFD
 - /pages/viewpage.action?pageId=8366662
product: Cumulus Linux
version: '4.0'
---
*Bidirectional Forwarding Detection* (BFD) provides low overhead and rapid detection of failures in the paths between two network devices. It provides a unified mechanism for link detection over all media and protocol layers. Use BFD to detect failures for IPv4 and IPv6 single or multihop paths between any two network devices, including unidirectional path failure detection.

{{%notice note%}}

Cumulus Linux does not support demand mode in BFD.

{{%/notice%}}

## BFD Multihop Routed Paths

BFD multihop sessions are built over arbitrary paths between two systems, which results in some complexity that does not exist for single hop sessions. Here are some best practices for using multihop paths:

- To avoid **spoofing** with multihop paths, configure the maximum hop count (`max_hop_cnt`*)* for each peer, which limits the number of hops for a BFD session. All BFD packets exceeding the maximum hop count are dropped.
- Because multihop BFD sessions can take arbitrary paths, **demultiplex** the initial BFD packet based on the source/destination IP address pair. Use FRRouting, which monitors connectivity to the peer, to determine the source/destination IP address pairs.

  Cumulus Linux supports multihop BFD sessions for both IPv4 and IPv6 peers.

## Configure BFD

You can configure BFD by either using [FRRouting](../FRRouting-Overview/) (with NCLU or vtysh commands) or by specifying the configuration in the [PTM `topology.dot` file](../../Layer-1-and-Switch-Ports/Prescriptive-Topology-Manager-PTM/). However, the topology file has some limitations:

- The topology file supports BFD IPv4 and IPv6 *single* hop sessions only; you *cannot* specify IPv4 or IPv6 *multihop* sessions in the topology file.
- The topology file supports BFD sessions for only link-local IPv6 peers; BFD sessions for global IPv6 peers discovered on the link are not created.

Use FRRouting to register multihop peers with PTM and BFD as well as to monitor the connectivity to the remote BGP multihop peer. FRRouting can dynamically register and unregister both IPv4 and IPv6 peers with BFD when the BFD-enabled peer connectivity is established or de-established. Also, you can configure BFD parameters for each BGP or OSPF peer.

{{%notice note%}}

The BFD parameter configured in the topology file is given higher precedence over the client-configured BFD parameters for a BFD session that has been created by both the topology file and FRRouting.

{{%/notice%}}

{{%notice note%}}

BFD requires an IP address for any interface on which it is configured. The neighbor IP address for a single hop BFD session must be in the ARP table before BFD can start sending control packets.

{{%/notice%}}

When you configure BFD, you can set the following parameters for both IPv4 and IPv6 sessions. If you do not set these parameters, the default values are used.

- The required minimum interval between the received BFD control packets. The default value is 300ms.
- The minimum interval for transmitting BFD control packets. The default value is 300ms.
- The detection time multiplier. The default value is 3.

### BFD in BGP

When you configure BFD in BGP, neighbors are registered and deregistered with [PTM](../../Layer-1-and-Switch-Ports/Prescriptive-Topology-Manager-PTM/) dynamically.

To configure BFD in BGP, run the following commands.

{{%notice note%}}

You can configure BFD for a peer group or for an individual neighbor.

{{%/notice%}}

<details>

<summary>NCLU Commands </summary>

The following example configures BFD for swp1 and uses the default intervals.

```
cumulus@switch:~$ net add bgp neighbor swp1 bfd
cumulus@switch:~$ net pending
cumulus@switch:~$ net commit
```

The following example configures BFD for the peer group `fabric` and sets the interval multiplier to 4, the minimum interval between received BFD control packets to 400, and the minimum interval for sending BFD control packets to 400.

```
cumulus@switch:~$ net add bgp neighbor fabric bfd 4 400 400
cumulus@switch:~$ net pending
cumulus@switch:~$ net commit
```

</details>

<details>

<summary>vtysh Commands </summary>

The following example configures BFD for swp1 and uses the default intervals:

```
cumulus@switch:~$ sudo vtysh

switch# configure terminal
switch(config)# router bgp 65000
switch(config-router)# neighbor swp1 bfd
switch(config-router)# exit
switch(config)# exit
switch# write mem
switch# exit
cumulus@switch:~$
```

The following example configures BFD for the peer group `fabric` and sets the interval multiplier to 4, the minimum interval between *received* BFD control packets to 400, and the minimum interval for *sending* BFD control packets to 400.

```
cumulus@switch:~$ sudo vtysh

switch# configure terminal
switch(config)# router bgp 65000
switch(config-router)# neighbor fabric bfd 4 400 400
switch(config-router)# exit
switch(config)# exit
switch# write mem
switch# exit
cumulus@switch:~$
```

</details>

The NCLU and vtysh commands save the configuration in the `/etc/frr/frr.conf` file. For example:

```
...
router bgp 65000
neighbor fabric bfd 4 400 400
...
```

To see neighbor information in BGP, including BFD status, run the NCLU `net show bgp neighbor <interface>` command or the vtysh `show ip bgp neighbor <interface>` command. For example:

```
cumulus@switch:~$ net show bgp neighbor swp1
...
BFD: Type: single hop
  Detect Mul: 3, Min Rx interval: 300, Min Tx interval: 300
  Status: Down, Last update: 0:00:00:08
...
```

### BFD in OSPF

When you enable or disable BFD in OSPF, neighbors are registered and de-registered dynamically with [PTM](../../Layer-1-and-Switch-Ports/Prescriptive-Topology-Manager-PTM/). When BFD is enabled on the interface, a neighbor is registered with BFD when two-way adjacency is established and deregistered when adjacency goes down. The BFD configuration is per interface and any IPv4 and IPv6 neighbors discovered on that interface inherit the configuration.

To configure BFD in OSPF, run the following commands.

<details>

<summary>NCLU Commands </summary>

The following example configures BFD in OSPFv3 for interface swp1 and sets the the interval multiplier to 4, the minimum interval between *received* BFD control packets to 400, and the minimum interval for *sending* BFD control packets to 400.

```
cumulus@switch:~$ net add interface swp1 ospf6 bfd 4 400 400
cumulus@switch:~$ net pending
cumulus@switch:~$ net commit
```

</details>

<details>

<summary>vtysh Commands </summary>

The following example configures BFD in OSPFv3 for interface swp1 and sets the the interval multiplier to 4, the minimum interval between *received* BFD control packets to 400, and the minimum interval for *sending* BFD control packets to 400.

```
cumulus@switch:~$ sudo vtysh

switch# configure terminal
switch(config)# interface swp1
switch(config-if)# ipv6 ospf6 bfd 4 400 400
switch(config-if)# exit
switch(config)# exit
switch# write mem
switch# exit
cumulus@switch:~$
```

</details>

The NCLU and vtysh commands save the configuration in the `/etc/frr/frr.conf` file. For example:

```
...
interface swp1
  ipv6 ospf6 bfd 4 400 400
  ...
```

You can run different commands to show neighbor information in OSPF, including BFD status.

- To show IPv6 OSPF interface information, run the NCLU `net show ospf6 interface <interface>` command or the vtysh `show ip ospf6 interface <interface>` command.
- To show IPv4 OSPF interface information, run the NCLU `net show ospf interface <interface>` command or the vtysh `show ip ospf interface <interface>` command.

   The following example shows IPv6 OSPF interface information.

```
cumulus@switch:~$ net show ospf6 interface swp2s0
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
```

- To show IPv6 OSPF neighbor details, run the NCLU `net show ospf6 neighbor detail` command or the vtysh `show ip ospf6 neighbor detail` command.
- To show IPv4 OSPF interface information, run the NCLU `net show ospf neighbor detail` command or the vtysh `show ip ospf neighbor detail` command.

  The following example shows IPv6 OSPF neighbor details.

```
cumulus@switch:~$ net show ospf6 neighbor detail
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
```

## Scripts

`ptmd` executes scripts at `/etc/ptm.d/bfd-sess-down` when BFD sessions go down and `/etc/ptm.d/bfd-sess-up` when BFD sessions goes up. Modify these default scripts as needed.

## Echo Function

Cumulus Linux supports the *echo function* for IPv4 single hops only, and with the asynchronous operating mode only (Cumulus Linux does not support demand mode).

Use the echo function to test the forwarding path on a remote system. To enable the echo function, set `echoSupport` to *1* in the topology file.

After the echo packets are looped by the remote system, the BFD control packets can be sent at a much lower rate. You configure this lower rate by setting the `slowMinTx` parameter in the topology file to a non-zero value in milliseconds.

You can use more aggressive detection times for echo packets because the round-trip time is reduced; echo  packets access the forwarding path. You can configure the detection interval by setting the `echoMinRx` parameter in the topology file. The minimum setting is 50 milliseconds. After configured, BFD control packets are sent out at this required minimum echo Rx interval. This indicates to the peer that the local system can loop back the echo packets. Echo packets are transmitted if the peer supports receiving echo packets.

### About the Echo Packet

BFD echo packets are encapsulated into UDP packets over destination and source UDP port number 3785. The BFD echo packet format is vendor-specific and has not been defined in the RFC. BFD echo packets that originate from Cumulus Linux are 8 bytes long and have the following format:

|0|1|2|3|
|---|---|---|---|
|Version|Length|Reserved|Reserved|
|My Discriminator|

Where:

- **Version** is the version of the BFD echo packet.
- **Length** is the length of the BFD echo packet.
- **My Discriminator** is a non-zero value that uniquely identifies a BFD session on the transmitting side. When the originating node receives the packet after being looped back by the receiving system, this value uniquely identifies the BFD session.

### Transmit and Receive Echo Packets

BFD echo packets are transmitted for a BFD session only when the peer has advertised a non-zero value for the required minimum echo Rx interval (the `echoMinRx` setting) in the BFD control packet when the BFD session starts. The transmit rate of the echo packets is based on the peer advertised echo receive value in the control packet.

BFD echo packets are looped back to the originating node for a BFD session only if locally the `echoMinRx` and `echoSupport` are configured to a non-zero values.

### Echo Function Parameters

You configure the echo function by setting the following parameters in the topology file at the global, template and port level:

- **echoSupport** enables and disables echo mode. Set to 1 to enable the echo function. It defaults to 0 (disable).
- **echoMinRx** is the minimum interval between echo packets the local system is capable of receiving. This is advertised in the BFD control packet. When the echo function is enabled, it defaults to 50. If you disable the echo function, this parameter is automatically set to 0, which indicates the port or the node cannot process or receive echo packets.
- **slowMinTx** is the minimum interval between transmitting BFD control packets when the echo packets are being exchanged.

## Troubleshooting

To troubleshoot BFD, run the NCLU `net show bfd sessions` or `net show bfd sessions detail` command.

```
cumulus@switch:~$ net show bfd sessions detail

----------------------------------------------------------------------------------------
port  peer                 state  local  type       diag  det   tx_timeout  rx_timeout  
                                                          mult
----------------------------------------------------------------------------------------
swp1  fe80::202:ff:fe00:1  Up     N/A    singlehop  N/A   3     300         900
swp1  3101:abc:bcad::2     Up     N/A    singlehop  N/A   3     300         900

#continuation of output
---------------------------------------------------------------------
echo        echo        max      rx_ctrl  tx_ctrl  rx_echo  tx_echo
tx_timeout  rx_timeout  hop_cnt
---------------------------------------------------------------------
0           0           N/A      187172   185986   0        0
0           0           N/A      501      533      0        0
```

You can also run the Linux `ptmctl -b` command.

## Related Information

- [RFC 5880 - Bidirectional Forwarding Detection](https://tools.ietf.org/html/rfc5880)
- [RFC 5881 - BFD for IPv4 and IPv6 (Single Hop)](https://tools.ietf.org/html/rfc5881)
- [RFC 5882 - Generic Application of BFD](https://tools.ietf.org/html/rfc5882)
- [RFC 5883 - Bidirectional Forwarding Detection (BFD) for Multihop Paths](https://tools.ietf.org/html/rfc5883)
