---
title: Bidirectional Forwarding Detection - BFD
author: NVIDIA
weight: 990
toc: 3
---
<span class="a-tooltip">[BFD](## "Bidirectional Forwarding Detection")</span> provides low overhead and rapid detection of failures in the paths between two network devices. It provides a unified mechanism for link detection over all media and protocol layers. Use BFD to detect failures for IPv4 and IPv6 single or multihop paths between any two network devices, including unidirectional path failure detection.

Cumulus Linux supports BFD with BGP, OSPF, PIM, and static routes and on interfaces, subinterfaces, and bonds.


{{%notice note%}}
Cumulus Linux does not support BFD demand mode, BFD echo mode, or BGP BFD strict mode.
{{%/notice%}}

## Enable BFD

To enable BFD:

{{< tabs "TabID33 ">}}
{{< tab "NVUE Commands ">}}

Run the `nv set router bfd state enabled` command:

```
cumulus@switch:~$ nv set router bfd state enabled
cumulus@switch:~$ nv config apply
```

To disable BFD, run the `nv set router bfd state disabled` command.

{{%notice note%}}
When you change the BFD state, the FRR service will restart, affecting all configured routing protocols.
{{%/notice%}}

{{< /tab >}}
{{< tab "Linux Commands ">}}

1. Enable the `bfdd` daemon as described in {{<link title="FRRouting">}}.

2. Restart the FRR service with the `sudo systemctl restart frr.service` command

{{< /tab >}}
{{< /tabs >}}



## Configure BFD

You can configure BFD with NVUE or vtysh commands.

To configure BFD, you configure a BFD profile, then attach the profile to the client, such as a BGP neighbor or peer group, OSPF interface, PIM interface, or static route. The BFD profile includes configuration parameters such as detect multiplier, transmit interval, receive interval, passive mode, admin state, and minimum expected TTL.

### Configure a BFD Profile

To configure BFD, you must create a BFD profile that includes the following options:
- The detection time multiplier to determine packet loss. The detection timeout is calculated based on multiplying the detection multiplier with the greater value between the local switch's receive interval and the peer's transmit interval. The default value is 3.
- The minimum interval for transmitting BFD control packets. You can set a value between 10 and 4294967 milliseconds. The default value is 300.
- The minimum interval between the received BFD control packets. You can set a value between 10 and 4294967 milliseconds. The default value is 300.
- Shutdown, which enables or disables the peer. When the peer is disabled the switch sends an `administrative down` message to the remote peer. The default value is `disabled`.
- Passive mode, which marks the session as passive. A passive session does not attempt to start the connection and waits for control packets from the peer before it begins replying. Passive mode is useful when you have a router that acts as the central node of a star network and you want to avoid sending BFD control packets you don’t need to. You can set passive mode to `enable` or `disabled`. The default is `disabled`.
- The minimum expected TTL for an incoming BFD control packet (for multi hop sessions only). This feature tightens the packet validation requirements to avoid receiving BFD control packets from other sessions. You can set a value between 1 and 254. The default value is 254 (only expect one hop between this system and the peer).

The following example configures a BFD profile called BFD1. The profile sets the detection time multiplier to 10, the minimum interval for transmitting BFD control packets and minimum interval between the received BFD control packets to 100, and the minimum expected TTL for an incoming BFD control packet to 1. The profile also enables shutdown and passive mode.

{{< tabs "TabID67 ">}}
{{< tab "NVUE Commands ">}}

```
cumulus@switch:~$ nv set router bfd profile BFD1 detect-multiplier 10
cumulus@switch:~$ nv set router bfd profile BFD1 min-tx-interval 100
cumulus@switch:~$ nv set router bfd profile BFD1 min-rx-interval 100
cumulus@switch:~$ nv set router bfd profile BFD1 minimum-ttl 1
cumulus@switch:~$ nv set router bfd profile BFD1 shutdown enabled
cumulus@switch:~$ nv set router bfd profile BFD1 passive-mode enabled
cumulus@switch:~$ nv config apply
```

{{< /tab >}}
{{< tab "vtysh Commands ">}}

```
cumulus@switch:~$ sudo vtysh
...
switch# configure terminal
switch(config)# bfd
switch(config-bfd)# profile BFD1
switch(config-bfd)# detect-multiplier 10 transmit-interval 100 receive-interval 100 shutdown passive-mode minimum-ttl 1
switch(config-bfd)# end
switch# write memory
switch# exit
```

{{< /tab >}}
{{< /tabs >}}

### BFD with BGP

BFD with BGP enables you to decrease BGP convergence time. When you configure BFD with BGP, the switch registers and de-registers neighbors dynamically.

You can configure BFD for a peer group or for an individual neighbor by attaching a BFD profile.

{{< tabs "TabID102 ">}}
{{< tab "NVUE Commands ">}}

The following example configures BFD for the neighbor swp51 using the BFD profile BFD1.

```
cumulus@switch:~$ nv set vrf default router bgp neighbor swp51 bfd profile BFD1
cumulus@switch:~$ nv config apply
```

The following example configures BFD for the peer group `fabric` using the BFD profile BFD1:

```
cumulus@switch:~$ nv set vrf default router bgp peer-group fabric bfd profile BFD1
cumulus@switch:~$ nv config apply
```

{{< /tab >}}
{{< tab "vtysh Commands ">}}

The following example configures BFD for the neighbor swp51 using the BFD profile BFD1.

```
cumulus@switch:~$ sudo vtysh
...
switch# configure terminal
switch(config)# router bgp 65000
switch(config-router)# neighbor swp1 bfd profile BFD1
switch(config-router)# end
switch# write memory
switch# exit
```

The following example configures BFD for the peer group `fabric` using the BFD profile BFD1:

```
cumulus@switch:~$ sudo vtysh
...
switch# configure terminal
switch(config)# router bgp 65000
switch(config-router)# neighbor fabric bfd profile BFD1
switch(config-router)# end
switch# write memory
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
neighbor fabric bfd profile BFD1
...
```

{{< /tab >}}
{{< /tabs >}}

### BFD with OSPF

When you enable BFD on an OSPF interface, a neighbor registers with BFD when two-way adjacency starts and de-registers when adjacency goes down. The BFD configuration is per interface and any IPv4 neighbors discovered on that interface inherit the configuration.

The following example configures BFD in OSPF for interface swp1 using the BFD profile BFD1.

{{< tabs "TabID182 ">}}
{{< tab "NVUE Commands ">}}

```
cumulus@switch:~$ nv set interface swp1 router ospf bfd profile BFD1
cumulus@switch:~$ nv config apply
```

{{< /tab >}}
{{< tab "vtysh Commands ">}}

```
cumulus@switch:~$ sudo vtysh
...
switch# configure terminal
switch(config)# interface swp1
switch(config-if)# ip ospf bfd profile BFD1
switch(config-if)# end
switch# write memory
switch# exit
```

The vtysh commands save the configuration in the `/etc/frr/frr.conf` file. For example:

```
...
interface swp1
  ip ospf bfd 
  ip ospf bfd profile BFD1 
  ...
```

{{< /tab >}}
{{< /tabs >}}

### BFD with PIM

To configure BFD with PIM, you attach a BFD profile to a PIM interface.

{{< tabs "TabID275 ">}}
{{< tab "NVUE Commands ">}}

```
cumulus@switch:~$ nv set interface vlan10 router pim bfd profile BFD1
cumulus@switch:~$ nv config apply
```

{{< /tab >}}
{{< tab "vtysh Commands ">}}

```
cumulus@switch:~$ sudo vtysh
...
switch# configure terminal
switch(config)# interface vlan10
switch(config-if)# ip pim bfd profile BFD1
switch(config-if)# end
switch# write memory
switch# exit
```

The vtysh commands save the configuration in the `/etc/frr/frr.conf` file. For example:

```
...
interface vlan10
  ip pim 
  ip pim bfd 
  ip pim bfd profile BFD1 
  ...
```

{{< /tab >}}
{{< /tabs >}}

### BFD with Static Routes

You can associate static routes with BFD to monitor static route reachability. Depending on status of the BFD session, the switch either adds or removes static routes from the Routing Information Base (RIB).

{{< tabs "TabID315 ">}}
{{< tab "NVUE Commands ">}}

```
cumulus@switch:~$ nv set vrf default router static 10.10.10.101/32 via 10.0.1.0 bfd profile BFD1 
cumulus@switch:~$ nv set vrf default router static 10.10.10.101/32 via 10.0.1.0 bfd multi-hop enabled
cumulus@switch:~$ nv set vrf default router static 10.10.10.101/32 via 10.0.1.0 bfd source 10.10.10.3
cumulus@switch:~$ nv config apply
```

```
cumulus@switch:~$ nv set vrf default router static 10.10.10.101/32 distance 2 via 10.0.1.0 bfd profile BFD2
cumulus@switch:~$ nv set vrf default router static 10.10.10.101/32 distance 2 via 10.0.1.0 bfd multi-hop enabled
cumulus@switch:~$ nv set vrf default router static 10.10.10.101/32 distance 2 via 10.0.1.0 bfd source 10.10.10.3
cumulus@switch:~$ nv config apply
```

{{< /tab >}}
{{< tab "vtysh Commands ">}}

```
cumulus@switch:~$ sudo vtysh
...
switch# configure terminal
switch(config)# ip route 10.10.10.101/32 10.0.1.0 bfd multi-hop source 10.10.10.3 profile BFD1
switch(config)# end
switch# write memory
switch# exit
```

To view BFD static route status, use the `show bfd static route` vtysh command:

```
switch# show bfd static route
Showing BFD monitored static routes:

  Next hops:
    VRF default IPv4 Unicast:
        10.10.10.101/32 peer 10.0.1.0 (status: uninstalled)
```

{{< /tab >}}
{{< /tabs >}}

{{%notice note%}}
- BFD with static routes is supported only when a next-hop IP address is specified.
- BFD operates in single hop mode by default. You must configure `multi-hop enabled` to use BFD for multihop next-hop tracking through static routes.
{{%/notice%}}
<!--
## Echo Function

Cumulus Linux supports the *echo function* for IPv4 single hops only, and with the asynchronous operating mode only (Cumulus Linux does not support demand mode).

Use the echo function to test the forwarding path on a remote system. To enable the echo function, set `echoSupport` to *1* in the topology file.

After the remote system loops the echo packets, the BFD control packets can send at a much lower rate. You configure this lower rate by setting the `slowMinTx` parameter in the topology file to a non-zero value in milliseconds.

You can use more aggressive detection times for echo packets because the round-trip time is less; echo packets access the forwarding path. You can configure the detection interval by setting the `echoMinRx` parameter in the topology file. The minimum setting is 50 milliseconds. After you configure this setting, BFD control packets send at this required minimum echo Rx interval. This indicates to the peer that the local system can loop back the echo packets. Echo packets transmit if the peer supports receiving echo packets.

Cumulus Linux encapsulates BFD echo packets into UDP packets over destination and source UDP port number 3785. The BFD echo packet format is vendor-specific. BFD echo packets that originate from Cumulus Linux are eight bytes long and have the following format:

|0|1|2|3|
|---|---|---|---|
|Version|Length|Reserved|Reserved|
|My Discriminator|

- **Version** is the version of the BFD echo packet.
- **Length** is the length of the BFD echo packet.
- **My Discriminator**is a non-zero value that uniquely identifies a BFD session on the transmitting side. When the originating node receives the packet after being looped back by the receiving system, this value uniquely identifies the BFD session.

### Transmit and Receive Echo Packets

Cumulus Linux transmits BFD echo packets for a BFD session only when the peer advertises a non-zero value for the required minimum echo receive interval (the `echoMinRx` setting) in the BFD control packet when the BFD session starts. The switch bases the transmit rate of the echo packets on the peer advertised echo receive value in the control packet.

Cumulus Linux loops BFD echo packets back to the originating node for a BFD session only if you configure the `echoMinRx` and `echoSupport` locally to a non-zero value.

### Echo Function Parameters

You configure the echo function by setting the following parameters in the topology file at the global, template and port level:

- **echoSupport** enables and disables echo mode. Set to 1 to enable the echo function. It defaults to 0 (disable).
- **echoMinRx** is the minimum interval between echo packets the local system is capable of receiving. The BFD control packet advertises this value. When you enable the echo function, it defaults to 50. If you disable the echo function, this parameter is automatically 0, which indicates the port or the node cannot process or receive echo packets.
- **slowMinTx** is the minimum interval between transmitting BFD control packets when the switch exchanges echo packets.
-->

### Considerations

- A BFP profile applied to an interface can be changed, but you can not unset a profile while BFD is still enabled on the interface. To remove BFD completely from an interface, use the `nv unset interface <if-name> router <protocol> bfd` command. To change the profile, set a new profile with the `nv set interface <if-name> router <protocol> bfd profile <profile>` command.
- BFD is supported in the `default` VRF and non-default VRFs.
- A single BFD session is established per interface, regardless of how many protocols use BFD on that interface. If you configure different BFD profiles for multiple protocols on the same interface, the most recently applied profile takes precedence for the BFD session on that interface.

## Show BFD Information

You can show BFD configuration and operational data with NVUE or vtysh show commands.

To show BFD profile configuration details, run the `nv show router bfd profile <profile-name>` command:

```
cumulus@switch:~$ nv show router bfd profile BFD1
                   applied 
-----------------  -------- 
detect-multiplier  10 
min-rx-interval    100 
min-tx-interval    100 
shutdown           enabled 
passive-mode       enabled 
minimum-ttl        1 
```

To show information about BFD connected devices, run the following commands:
- `nv show vrf <vrf-id> router bfd peers` shows
- `nv show vrf <vrf-id> router bfd peers --view brief` shows
- `nv show vrf <vrf-id> router bfd peers --view standard` shows
- `nv show vrf <vrf-id> router bfd peers --view detail` shows
- `nv show vrf <vrf-id> router bfd peers --view counters` shows
- `nv show vrf <vrf-id> router bfd peers <session-id>` shows

```
cumulus@switch:~$ nv show vrf default router bfd peers --view brief
MHop - Multihop, Local - Local, Peer - Peer, Interface - Interface, State - 
State, Passive - Passive Mode, Time - Up/Down Time, Type - Config Type 
LocalId     MHop   Local       Peer        Interface  State  Passive  Time        Type 
----------  -----  ----------  ----------  ---------  -----  -------  ----------  ------- 
20162981    True   6.0.0.24    6.0.0.26               up     False    1:00:08:20  dynamic 
1002134429  True   6000::24    6000::26               up     False    1:00:08:20  dynamic 
1987835266  False  fe80::a288  fe80::9e05  p0_if.100  up     False    1:00:08:20  dynamic 
2124581159  False  fe80::a288  fe80::9e05  p0_if.101  up     False    1:00:08:20  dynamic 
2323511220  True   6000::24    6000::23               up     False    1:00:08:20  dynamic 
4089962224  True   6.0.0.24    6.0.0.23               up     False    0:19:07:20  dynamic 
```

```
cumulus@switch:~$ nv show vrf default router bfd peers --view counters
Local - Local, Peer - Peer, Interface - Interface, State - State, CtrlIn - 
Control Packet Input, CtrlOut - Control Packet Output, EchoIn - Echo Packet 
Input, EchoOut - Echo Packet Output, Up - Session Up, Down - Session Down, Zebra 
- Zebra Notification 
LocalId    Local      Peer       Interface State CtrlIn CtrlOut EchoIn EchoOut Up Down Zebra 
---------- ---------- ---------- --------- ----- ------ ------- ------ ------- -- ---- ----- 
20162981   6.0.0.24   6.0.0.26             up    248913 248920  0      0       1  0    5 
1002134429 6000::24   6000::26             up    248882 248829  0      0       1  0    5 
1987835266 fe80::a288 fe80::9e05 p0_if.100 up    473059 497655  0      0       1  0    9 
2124581159 fe80::a288 fe80::9e05 p0_if.101 up    472823 497637  0      0       1  0    5 
2323511220 6000::24   6000::23             up    320763 331701  0      0       1  0    5 
4089962224 6.0.0.24   6.0.0.23             up    254206 262960  0      0       1  0    14 
```

### Show BFD with BGP

To show the BFD profile associated with a BGP neighbor or peer group, run the NVUE `nv show vrf <vrf-id> router bgp neighbor <neighbor-id> bfd` command or the `nv show vrf <vrf-id> router bgp peer-group <peer-group-id> bfd` command.

```
cumulus@switch:~$ nv show vrf default router bgp neighbor swp51 bfd
         operational  applied
-------  -----------  -------

profile               BFD1
```

To see neighbor information in BGP, including BFD status, run the vtysh `show ip bgp neighbor <interface-id>` command:

```
cumulus@switch:~$ sudo vtysh 
switch# show ip bgp neighbor swp51
...
BFD: Type: single hop
  Detect Mul: 4, Min Rx interval: 400, Min Tx interval: 400
  Status: Down, Last update: 0:00:00:08
...
```

### Show BFD with OSPF

To show the BFD profile associated with an OSPF interface, run the NVUE `nv show interface <interface-id> router ospf bfd` command:

```
cumulus@switch:~$ nv show interface swp1 router ospf bfd
         operational  applied
-------  -----------  -------

profile               BFD1
```

You can run vtysh commands to show neighbor information in OSPF, including BFD status. To show IPv4 OSPF interface information, run the vtysh `show ip ospf interface <interface-id>` command.
### Show BFD with PIM

To show the BFD profile associated with a PIM session, run the NVUE `nv show interface <interface-id> router pim bfd` command:

```
cumulus@switch:~$ nv show interface vlan10 router pim bfd
         operational  applied
-------  -----------  -------

profile               BFD1
```

### Show BFD with Static Routes

To show the BFD profile associated with static routes, run the NVUE `nv show vrf <vrf-id> router static <ipv4-prefix> via <ipv4> bfd` command or the `nv show vrf <vrf-id> router static <ipv4-prefix> distance <integer> via <ipv4> bfd` command:

```
cumulus@switch:~$ nv show vrf default router static 10.10.10.101/32 via 10.0.1.0 bfd
         operational  applied
-------  -----------  -------

profile               BFD1
```

## Related Information

- {{<exlink url="https://tools.ietf.org/html/rfc5880" text="RFC 5880 - Bidirectional Forwarding Detection">}}
- {{<exlink url="https://tools.ietf.org/html/rfc5881" text="RFC 5881 - BFD for IPv4 and IPv6 (Single Hop)">}}
- {{<exlink url="https://tools.ietf.org/html/rfc5882" text="RFC 5882 - Generic Application of BFD">}}
- {{<exlink url="https://tools.ietf.org/html/rfc5883" text="RFC 5883 - Bidirectional Forwarding Detection (BFD) for Multihop Paths">}}

<!--
## BFD Multihop Routed Paths

BFD multihop sessions build over arbitrary paths between two systems, which results in some complexity that does not exist for single hop sessions. To avoid **spoofing** with multihop paths, configure the maximum hop count (`max_hop_cnt`) for each peer, which limits the number of hops for a BFD session. The switch drops all BFD packets exceeding the maximum hop count.

Cumulus Linux supports multihop BFD sessions for both IPv4 and IPv6 peers.
-->