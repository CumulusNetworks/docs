---
title: Bidirectional Forwarding Detection - BFD
author: NVIDIA
weight: 990
toc: 3
---
<span class="a-tooltip">[BFD](## "Bidirectional Forwarding Detection")</span> provides low overhead and rapid detection of failures in the paths between two network devices. It provides a unified mechanism for link detection over all media and protocol layers. Use BFD to detect failures for IPv4 and IPv6 single or multihop paths between any two network devices, including unidirectional path failure detection.

{{%notice note%}}
Cumulus Linux does not support:
- BFD demand mode
- Dynamic BFD timer negotiation on an existing session. Any change to the timer values takes effect only when the session goes down and comes back up.
{{%/notice%}}

## BFD Multihop Routed Paths

BFD multihop sessions build over arbitrary paths between two systems, which results in some complexity that does not exist for single hop sessions. To avoid **spoofing** with multihop paths, configure the maximum hop count (`max_hop_cnt`) for each peer, which limits the number of hops for a BFD session. The switch drops all BFD packets exceeding the maximum hop count.

Cumulus Linux supports multihop BFD sessions for both IPv4 and IPv6 peers.

## Configure BFD

You can configure BFD with NVUE or vtysh commands or by specifying the configuration in the {{<link url="Prescriptive-Topology-Manager-PTM" text="PTM `topology.dot` file">}}. However, the topology file has some limitations:

- The topology file supports BFD IPv4 and IPv6 *single* hop sessions only; you *cannot* specify IPv4 or IPv6 *multihop* sessions in the topology file.
- The topology file supports BFD sessions for only link-local IPv6 peers; BFD sessions for global IPv6 peers discovered on the link are not created.

Use <span class="a-tooltip">[FRR](## "FRRouting")</span> to register multihop peers with {{<link url="Prescriptive-Topology-Manager-PTM" text="PTM">}} and BFD, and monitor the connectivity to the remote <span class="a-tooltip">[BGP](## "Border Gateway Protocol")</span> multihop peer. FRR can dynamically register and unregister both IPv4 and IPv6 peers with BFD when the BFD-enabled peer connectivity starts or stops. Also, you can configure BFD parameters for each BGP or <span class="a-tooltip">[OSPF](## "Open Shortest Path First")</span> peer.

{{%notice note%}}
The BFD parameter in the topology file takes precedence over the client-configured BFD parameters for a BFD session that both the topology file and FRR creates.
{{%/notice%}}

{{%notice note%}}
Every BFD interface requires an IP address. The neighbor IP address for a single hop BFD session must exist in the ARP table before BFD can start sending control packets.
{{%/notice%}}

When you configure BFD, you can set the following parameters for both IPv4 and IPv6 sessions. If you do not set these parameters, Cumulus Linux uses the default values.

- The required minimum interval between the received BFD control packets. The default value is 300ms.
- The minimum interval for transmitting BFD control packets. The default value is 300ms.
- The detection time multiplier. The default value is 3.

### BFD in BGP

When you configure BFD in BGP, {{<link url="Prescriptive-Topology-Manager-PTM" text="PTM">}} registers and de-registers neighbors dynamically.

To configure BFD in BGP, run the following commands.

{{%notice note%}}
You can configure BFD for a peer group or for an individual neighbor.
{{%/notice%}}

{{< tabs "TabID66 ">}}
{{< tab "NVUE Commands ">}}

The following example configures BFD for swp51 and uses the default intervals.

```
cumulus@switch:~$ nv set vrf default router bgp neighbor swp51 bfd enable on
cumulus@switch:~$ nv config apply
```

The following example configures BFD for the peer group `fabric` and sets the interval multiplier to 4, the minimum interval between received BFD control packets to 400, and the minimum interval for sending BFD control packets to 400.

```
cumulus@switch:~$ nv set vrf default router bgp neighbor fabric bfd enable on
cumulus@switch:~$ nv set vrf default router bgp neighbor fabric bfd detect-multiplier 4 
cumulus@switch:~$ nv set vrf default router bgp neighbor fabric bfd min-rx-interval 400 
cumulus@switch:~$ nv set vrf default router bgp neighbor fabric bfd min-tx-interval 400
cumulus@switch:~$ nv config apply
```

{{< /tab >}}
{{< tab "vtysh Commands ">}}

The following example configures BFD for swp1 and uses the default intervals:

```
cumulus@switch:~$ sudo vtysh
...
switch# configure terminal
switch(config)# router bgp 65000
switch(config-router)# neighbor swp1 bfd
switch(config-router)# exit
switch(config)# exit
switch# write mem
switch# exit
```

The following example configures BFD for the peer group `fabric` and sets the interval multiplier to 4, the minimum interval between *received* BFD control packets to 400, and the minimum interval for *sending* BFD control packets to 400.

```
cumulus@switch:~$ sudo vtysh
...
switch# configure terminal
switch(config)# router bgp 65000
switch(config-router)# neighbor fabric bfd 4 400 400
switch(config-router)# exit
switch(config)# exit
switch# write mem
switch# exit
```

The vtysh commands save the configuration in the `/etc/frr/frr.conf` file. For example:

```
...
router bgp 65101 vrf default
bgp router-id 10.10.10.1
! Neighbors
neighbor fabric peer-group
neighbor fabric remote-as external
neighbor fabric bfd 4 400 400
...
```

{{< /tab >}}
{{< /tabs >}}

To see neighbor information in BGP, including BFD status, run the vtysh `show ip bgp neighbor <interface>` command. For example:

```
cumulus@switch:~$ sudo vtysh 
switch# show ip bgp neighbor swp51
...
BFD: Type: single hop
  Detect Mul: 4, Min Rx interval: 400, Min Tx interval: 400
  Status: Down, Last update: 0:00:00:08
...
```

### BFD in OSPF

When you enable or disable BFD in OSPF, {{<link url="Prescriptive-Topology-Manager-PTM" text="PTM">}} registers and de-registers neighbors dynamically. When you enable BFD on the interface, a neighbor registers with BFD when two-way adjacency starts and de-registers when adjacency goes down. The BFD configuration is per interface and any IPv4 and IPv6 neighbors discovered on that interface inherit the configuration.

The following example configures BFD in OSPF for interface swp1 and sets interval multiplier to 4, the minimum interval between *received* BFD control packets to 400, and the minimum interval for *sending* BFD control packets to 400.

{{< tabs "TabID150 ">}}
{{< tab "NVUE Commands ">}}

```
cumulus@switch:~$ nv set interface swp1 router ospf bfd detect-multiplier 4
cumulus@switch:~$ nv set interface swp1 router ospf bfd min-receive-interval 400
cumulus@switch:~$ nv set interface swp1 router ospf bfd min-transmit-interval 400
cumulus@switch:~$ nv config apply
```

{{< /tab >}}
{{< tab "vtysh Commands ">}}

```
cumulus@switch:~$ sudo vtysh
...
switch# configure terminal
switch(config)# interface swp1
switch(config-if)# ipv6 ospf6 bfd 4 400 400
switch(config-if)# exit
switch(config)# exit
switch# write mem
switch# exit
```

The vtysh commands save the configuration in the `/etc/frr/frr.conf` file. For example:

```
...
interface swp1
  ipv6 ospf6 bfd 4 400 400
  ...
```

{{< /tab >}}
{{< /tabs >}}

You can run different commands to show neighbor information in OSPF, including BFD status.

- To show IPv6 OSPF interface information, run the vtysh `show ip ospf6 interface <interface>` command.
- To show IPv4 OSPF interface information, run the vtysh `show ip ospf interface <interface>` command.

   The following example shows IPv6 OSPF interface information.

    ```
    cumulus@switch:~$ sudo vtysh
    switch# show ip ospf6 interface swp2s0
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

- To show IPv6 OSPF neighbor details, run the vtysh `show ip ospf6 neighbor detail` command.
- To show IPv4 OSPF interface information, run the vtysh `show ip ospf neighbor detail` command.

  The following example shows IPv6 OSPF neighbor details.

  ```
  cumulus@switch:~$ sudo vtysh
  switch# show ip ospf6 neighbor detail
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

After the remote system loops the echo packets, the BFD control packets can send at a much lower rate. You configure this lower rate by setting the `slowMinTx` parameter in the topology file to a non-zero value in milliseconds.

You can use more aggressive detection times for echo packets because the round-trip time is less; echo packets access the forwarding path. You can configure the detection interval by setting the `echoMinRx` parameter in the topology file. The minimum setting is 50 milliseconds. After you configure this setting, BFD control packets send at this required minimum echo Rx interval. This indicates to the peer that the local system can loop back the echo packets. Echo packets transmit if the peer supports receiving echo packets.

### About the Echo Packet

Cumulus Linux encapsulates BFD echo packets into UDP packets over destination and source UDP port number 3785. The BFD echo packet format is vendor-specific. BFD echo packets that originate from Cumulus Linux are eight bytes long and have the following format:
<!-- vale off -->
|0|1|2|3|
|---|---|---|---|
|Version|Length|Reserved|Reserved|
|My Discriminator|

Where:

- **Version** is the version of the BFD echo packet.
- **Length** is the length of the BFD echo packet.
- **My Discriminator**is a non-zero value that uniquely identifies a BFD session on the transmitting side. When the originating node receives the packet after being looped back by the receiving system, this value uniquely identifies the BFD session.
<!-- vale on -->
### Transmit and Receive Echo Packets

Cumulus Linux transmits BFD echo packets for a BFD session only when the peer advertises a non-zero value for the required minimum echo receive interval (the `echoMinRx` setting) in the BFD control packet when the BFD session starts. The switch bases the transmit rate of the echo packets on the peer advertised echo receive value in the control packet.

Cumulus Linux loops BFD echo packets back to the originating node for a BFD session only if you configure the `echoMinRx` and `echoSupport` locally to a non-zero values.

### Echo Function Parameters

You configure the echo function by setting the following parameters in the topology file at the global, template and port level:

- **echoSupport** enables and disables echo mode. Set to 1 to enable the echo function. It defaults to 0 (disable).
- **echoMinRx** is the minimum interval between echo packets the local system is capable of receiving. The BFD control packet advertises this value. When you enable the echo function, it defaults to 50. If you disable the echo function, this parameter is automatically 0, which indicates the port or the node cannot process or receive echo packets.
- **slowMinTx** is the minimum interval between transmitting BFD control packets when the switch exchanges echo packets.

## Troubleshooting

To troubleshoot BFD, run the Linux `ptmctl -b` command.

```
cumulus@switch:~$ net show bfd detail

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

## Related Information

- {{<exlink url="https://tools.ietf.org/html/rfc5880" text="RFC 5880 - Bidirectional Forwarding Detection">}}
- {{<exlink url="https://tools.ietf.org/html/rfc5881" text="RFC 5881 - BFD for IPv4 and IPv6 (Single Hop)">}}
- {{<exlink url="https://tools.ietf.org/html/rfc5882" text="RFC 5882 - Generic Application of BFD">}}
- {{<exlink url="https://tools.ietf.org/html/rfc5883" text="RFC 5883 - Bidirectional Forwarding Detection (BFD) for Multihop Paths">}}
