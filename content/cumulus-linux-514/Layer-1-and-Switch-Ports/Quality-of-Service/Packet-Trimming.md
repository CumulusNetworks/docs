---
title: Packet Trimming
author: NVIDIA
weight: 321
right_toc_levels: 2
---

Spectrum ASICs implement shared buffers and enable flexible partitioning of the shared buffers for different flows and ports, as well as separation of lossy and lossless traffic. For lossy packets, if a packet in the headroom does not move into the switch shared buffers due to congestion in the lossy queue, it is dropped without any notification to the destination host. When a packet is lost, it can be recovered through fast retransmission or by using timeouts. Retransmission triggered by timeouts typically incurs significant latency.

With packet trimming, a switch can remove parts of the packet (such as the payload) instead of dropping it when the buffer is full. Packet trimming retains network forwarding and transport essential information, and resends the packet on a different traffic class to the destination. This allows congestion information to be communicated to the receiver even on congested networks.

{{%notice note%}}
- Cumulus Linux supports packet trimming on the Spectrum-4 and Spectrum-5 switch.
- You cannot enable packet trimming when the NetQ WJH agent is running or with WJH monitor buffer drops configured.
- When you enable packet trimming, you cannot configure SPAN session ID 0.
- Cumulus Linux supports packet trimming on physical ports only and for known unicast IPv4 and IPv6 traffic. Packet trimming does not support ISSU, bonds for egress eligibility, or the following packet types:
  - VXLAN packets
  - Adaptive Routing Notification Packets (ARN)
  - Congestion Notification Packets (CNP)
  - Flooding and MC packets
{{%/notice%}}

## Configure Packet Trimming

To enable and configure packet trimming on the switch:
- Set the packet trimming state to enabled.
- Configure the port eligibility by setting the egress port and traffic class from which to trim and recirculate dropped traffic. You can specify a traffic class value between 0 and 7. By default, port eligibility is disabled for all ports and traffic classes. You can only configure physical ports. If we want to trim packets egressing from bonds, specify the bond slave ports.
- Set the DSCP value to be marked on the trimmed packets. You can specify a value between 0 and 63. The default value is 11.
- Set the maximum size of the trimmed packet. You can specify a value between 256 and 1024; the value must be a multiple of 4.
- Set the egress switch priority on which to send the trimmed packet. You can specify a value between 0 and 7. The traffic class of the trimmed packet is internally derived from the switch priority.

```
cumulus@switch:~$ nv set system forwarding packet-trim state enabled
cumulus@switch:~$ nv set interface swp1-3 packet-trim egress-eligibility traffic-class 1
cumulus@switch:~$ nv set system forwarding packet-trim remark dscp 10
cumulus@switch:~$ nv set system forwarding packet-trim size 528
cumulus@switch:~$ nv set system forwarding packet-trim switch-priority 2
cumulus@switch:~$ nv config apply
```

{{%notice note%}}
On the NVIDIA SN5610 switch, you can run the `nv set system forwarding packet-trim service-port <interface>` command to set the service port, which is the recirculation port that loops the dropped packets internally to another traffic class. If you do not configure a service port, Cumulus Linux uses the last service port on the switch.
{{%/notice%}}

## Packet Trimming with Default Profile

Cumulus Linux provides a default packet trimming profile you can use instead of configuring all the settings above. The default packet trimming profile has the following settings:
- Enables packet trimming.
- Sets the DSCP remark value to 11 (global DSCP).
- Sets the truncation size to 256.
- Sets the switch priority to 4.
- Sets the eligibility to all ports on the switch with traffic class 1,2, and 3.

To use the default packet trimming profile:

```
cumulus@switch:~$ nv set system forwarding packet-trim profile packet-trim-default
cumulus@switch:~$ nv config apply
```

To disable packet trimming, run the `nv set system forwarding packet-trim state disabled` command.

To unset the default packet trimming profile, run the `nv unset system forwarding packet-trim profile packet-trim-default` command.

## Packet Trimming with RoCE

The RoCE `lossy-multi-tc` profile uses the {{<link url="#default-packet-trimming-profile" text="default packet trimming profile">}} settings:

To configure packet trimming with RoCE, run the `nv set qos roce mode lossy-multi-tc` command.

```
cumulus@switch:~$ nv set qos roce mode lossy-multi-tc
cumulus@switch:~$ nv config apply
```

## Asymmetric Packet Trimming

Use asymmetric packet trimming to mark trimmed packets differently based on the outgoing port. By default, you remark all trimmed packets with the same DSCP value; however, you can use a different DSCP value for trimmed packets sent out through different ports. For example, you can use DSCP 20 to send trimmed packets to hosts but DSCP 10 to send trimmed packets to the uplink (spine). This allows the destination NIC to know where congestion occurs; on downlinks to servers or in the fabric.

## Configure Asymmetric Packet Trimming

To achieve asymmetric DSCP for trimmed packets, you set a dedicated switch priority value for trimmed packets and define a switch priority to DSCP rewrite mapping for each egress interface.

To enable and configure asymmetric packet trimming:
- Set the packet trimming state to enabled.
- Set the egress port and traffic-class from which the dropped traffic is trimmed. You can specify a value between 0 and 7.
- Set the DSCP remark to be at the port level.
- Set the DSCP value for the host facing and network facing ports by creating remark profiles and assigning the switch priority and DSCP values for each remark profile. The default value for the downlink (host facing interface) is 21. The default value for the uplink (network facing interface) is 11.
- Set the maximum size of the trimmed packet. You can specify a value between 256 and 1024; the value must be a multiple of 4.
- Set the egress switch priority on which to send the trimmed packet. You can specify a value between 0 and 7.

The following example configures asymmetric packet trimming on the downlink to hosts (leaf01) to use DSCP 20 to send trimmed packets on ports swp17 through swp32 to hosts but DSCP 10 on ports swp1 through swp17 to the uplink (spine):

```
cumulus@leaf01:~$ nv set system forwarding packet-trim state enabled
cumulus@leaf01:~$ nv set interface swp1-32 packet-trim egress-eligibility traffic-class 1
cumulus@leaf01:~$ nv set system forwarding packet-trim remark dscp port-level
cumulus@leaf01:~$ nv set interface swp1-16 qos remark profile network-port-group
cumulus@leaf01:~$ nv set qos remark network-port-group switch-priority 4 dscp 10
cumulus@leaf01:~$ nv set interface swp17-32 qos remark profile host-port-group 
cumulus@leaf01:~$ nv set qos remark host-port-group switch-priority 4 dscp 20
cumulus@leaf01:~$ nv set system forwarding packet-trim switch-priority 4 
cumulus@leaf01:~$ nv config apply
```

The following example configures the uplink (spine01) and remarks all trimmed packets with 10.

```
cumulus@switch:~$ nv set system forwarding packet-trim state enabled
cumulus@switch:~$ nv set interface swp1-3 packet-trim egress-eligibility traffic-class 1
cumulus@switch:~$ nv set system forwarding packet-trim remark dscp 10
cumulus@switch:~$ nv set system forwarding packet-trim size 528
cumulus@switch:~$ nv set system forwarding packet-trim switch-priority 4
cumulus@switch:~$ nv config apply
```

## Asymmetric Packet Trimming with Default Profile

If you want to use the {{<link url="#default-packet-trimming-profile" text="default packet trimming profile">}} instead of configuring all the settings above, run the following commands:

```
cumulus@switch:~$ nv set system forwarding packet-trim packet-trim-default
cumulus@leaf01:~$ nv set system forwarding packet-trim remark dscp port-level
cumulus@switch:~$ nv config apply
```

The default packet trimming profile uses the following port profiles:
- `lossy-multi-tc-host-group` sets the DSCP remark value to 21 for switch priority 4 on the downlink to hosts.
- `lossy-multi-tc-network-group` sets the DSCP remark value to 11 for switch priority 4 on the uplink to the network.

## Asymmetric Packet Trimming with RoCE

The RoCE `lossy-multi-tc` profile uses the {{<link url="#default-packet-trimming-profile" text="default packet trimming profile">}} settings.

To configure asymmetric packet trimming with RoCE:
- Set the `lossy-multi-tc` QoS profile.
- Set DSCP remark to be at the port level.

The following example configures packet trimming on the downlink to hosts (leaf01) to use DSCP 21 to send trimmed packets on ports swp17 through swp32 to hosts but DSCP 11 on ports swp1 through swp17 to the uplink (spine):

```
cumulus@leaf01:~$ nv set qos roce mode lossy-multi-tc
cumulus@leaf01:~$ nv set system forwarding packet-trim remark dscp port-level
cumulus@leaf01:~$ nv config apply
```

The following example configures the uplink (spine01) with the QoS `lossy-multi-tc` profile. You do not need to configure additional settings; the switch expects the default global DSCP remark type and remarks all trimmed packets with 11.

```
cumulus@spine01:~$ nv set qos roce mode lossy-multi-tc
cumulus@spine01:~$ nv config apply
```

## Show Packet Trimming Configuration

To show packet trimming configuration, run the `nv show system forwarding packet-trim` command.

The following example shows `nv show system forwarding packet-trim` command output for packet trimming:

```
cumulus@switch:~$ nv show system forwarding packet-trim
                          operational  applied           
-------------------------  -----------  -------------------
state                      enabled      enabled           
profile                                 
service-port               swp65                          
size                       1024                             
traffic-class              4                              
switch-priority            4                              
remark                                                    
dscp                     11                             
session-info                                              
session-id               0x0                            
trimmed-packet-counters  0                              

Egress Eligibility TC-to-Interface Information
=================================================
   TC  interface                                                      
   --  ----------------------------------------------------------------
   1   swp2-16,18-32,34-48,50-64,swp1s0-1,swp17s0-1,swp33s0-1,swp49s0-1
   2   swp2-16,18-32,34-48,50-64,swp1s0-1,swp17s0-1,swp33s0-1,swp49s0-1
   3   swp2-16,18-32,34-48,50-64,swp1s0-1,swp17s0-1,swp33s0-1,swp49s0-1

Port-Level SP to DSCP Remark Information
===========================================
No Data
```

The following example shows `nv show system forwarding packet-trim` command output for asymmetric packet trimming:

```
cumulus@switch:~$ nv show system forwarding packet-trim 
                           operational  applied            
-------------------------  -----------  -------------------
state                      enabled      enabled            
profile                                 packet-trim-default
service-port               swp65                           
size                       256                             
traffic-class              4                               
switch-priority            4                               
remark                                                     
 dscp                     port-level   port-level         
session-info                                               
 session-id               0x0                             
 trimmed-packet-counters  0                               

Egress Eligibility TC-to-Interface Information
=================================================
    TC  interface                                                  
    --  -----------------------------------------------------------
    1   swp2,4-32,34-48,50-64,swp1s0-1,swp3s0-1,swp33s0-1,swp49s0-1
    2   swp2,4-32,34-48,50-64,swp1s0-1,swp3s0-1,swp33s0-1,swp49s0-1
    3   swp2,4-32,34-48,50-64,swp1s0-1,swp3s0-1,swp33s0-1,swp49s0-1

Port-Level SP to DSCP Remark Information
===========================================
    Profile                       Interface  SP  DSCP
    ----------------------------  ---------  --  ----
    lossy-multi-tc-host-group     swp1s0     4   21  
    lossy-multi-tc-network-group  swp33s0    4   11
```

To show packet trimming remark information, run the `nv show system forwarding packet-trim remark` command. The default global packet trimming remark value is 11. For asymmetric packet trimming, the default remark value is `port-level`.

```
cumulus@switch:~$ nv show system forwarding packet-trim remark 
                          operational   applied
----                      -----------   -------
state                      enabled      enabled
profile                                 packet-trim-default
service-port               swp65
size                       256
traffic-class              4
switch-priority            4
remark
  dscp                     11
session-info
  session-id               0x0
  trimmed-packet-counters  0

Egress Eligibility TC-to-Interface Information
=================================================
    TC  interface
    --  -----------------------
    1   swp1-60,63-64,swp61s0-7
    2   swp1-60,63-64,swp61s0-7
    3   swp1-60,63-64,swp61s0-7

Port-Level SP to DSCP Remark Information
===========================================
No Data
```

- To show interface packet-trim eligibility information, run the `nv show interface <interface-id> packet-trim` command.
- To show interface packet-trim eligibility traffic-class information, run the `nv show interface <interface-id> packet-trim egress-eligibility` command.
- To show interface packet-trim egress-interface traffic class information, run the `nv show interface <interface-id> packet-trim egress-eligibility traffic-class <tc-id>` command.
