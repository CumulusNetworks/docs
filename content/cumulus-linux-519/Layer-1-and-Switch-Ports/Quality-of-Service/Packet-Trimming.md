---
title: Packet Trimming
author: NVIDIA
weight: 321
right_toc_levels: 2
---
The Spectrum switch implements a packet trimming mechanism, with which the switch trims and forwards packets that are about to be discarded due to unavailable buffer space. A trimmed packet (with a supplemented mechanism on the host) allows for quick retransmission of the discarded packet.

You can apply DSCP remarking on trimmed packets:
- At the global level, where all trimmed packets have the same DSCP value.
- At the port level, where the switch remarks the DSCP value of the trimmed packets based on the port level switch priority to DSCP mapping.

{{%notice note%}}
- Cumulus Linux supports packet trimming on Spectrum-4 and later.
- Cumulus Linux supports packet trimming for known unicast IPv4 and IPv6 traffic. Packet trimming does not support ISSU, VXLAN packets or flooding and multicast packets.
{{%/notice%}}
<!-- REMOVED FROM 5.18 - WJH NO LONGER IN DOCKER CONTAINER
Do not enable packet trimming when the NetQ WJH agent is running or with WJH monitor buffer drops configured.
-->
## Global Level Packet Trimming

Global level packet trimming enables you to use the same DSCP value on all trimmed packets.

To enable and configure global packet trimming on the switch:
- Set the packet trimming state to enabled.
- Configure the port eligibility by setting the egress port and traffic class from which to trim and recirculate dropped traffic. You can only configure physical ports; if you want to trim packets egressing bonds, specify the bond slave ports. You can specify a traffic class value between 0 and 7.
- Set the DSCP value you want to mark on trimmed packets. You can specify a value between 0 and 63.
- Set the maximum size of the trimmed packet in bytes. You can specify a value between 256 and 1024; the value must be a multiple of 4. If the packet is smaller than the trimming size, the switch does not trim the packet but forwards the packet based on the configured switch priority for trim-eligible packets.
- Set the switch priority of the trimmed packet. You can specify a value between 0 and 7. The traffic class of the trimmed packet is internally derived from the switch priority.

```
cumulus@switch:~$ nv set system forwarding packet-trim state enabled
cumulus@switch:~$ nv set interface swp1-3 packet-trim egress-eligibility traffic-class 1
cumulus@switch:~$ nv set system forwarding packet-trim remark dscp 10
cumulus@switch:~$ nv set system forwarding packet-trim size 528
cumulus@switch:~$ nv set system forwarding packet-trim switch-priority 2
cumulus@switch:~$ nv config apply
```

{{%notice note%}}
- On Spectrum-4 and Spectrum-5 switches, when you enable packet trimming, one service port is used. By default, this is the last service port on the switch. To change the service port, run the `nv set system forwarding packet-trim service-port <interface-id>` command. For information about service ports on Spectrum-4 switches, refer to {{<link url="Switch-Port-Attributes/#breakout-ports" text="Switch Port Attributes">}}.
- On a switch that supports two service ports, you can configure a bond on the service ports, then use the bond for the packet trimming service port; for example: `nv set system forwarding packet-trim service-port bond1`.
- When you enable packet trimming, do not configure packet trimming port eligibility, port security, adaptive routing, QoS, ACLs, PTP, VRR, PBR, telemetry, or histograms on the service port.

<!-- REVIEW: this notice used to describe the service port unconditionally, for every ASIC. Spectrum-6
     switches trim packets with an on-chip trim agent instead of port recirculation and do not use a
     service port for packet trimming or back-to-sender on congestion tail drop; the functional
     specification for BTS on congestion tail drop (FR 4373590, approved 22-09-2026) records this as a
     release-note withdrawal: "On Spectrum-6, nv set system forwarding packet-trim service-port is no
     longer offered. The leaf was exposed by accident, did nothing there, and a configuration that set
     it was never supported." Back-to-sender notification on link down is the exception -- it uses a
     recirculation session and its own service port on Spectrum-6 too; see that section below.
     Delete this comment before publishing. -->

{{%/notice%}}

### Global Level Packet Trimming with Default Profile

Cumulus Linux provides a default packet trimming profile you can use instead of configuring all the settings above. The default packet trimming profile has the following settings:
- Enables packet trimming.
- Sets the DSCP remark value to 11.
- Sets the truncation size to 256 bytes.
- Sets the switch priority to 4.
- Sets the eligibility to all ports on the switch with traffic class 1, 2, and 3.

To use the default packet trimming profile:

```
cumulus@switch:~$ nv set system forwarding packet-trim profile packet-trim-default
cumulus@switch:~$ nv config apply
```

After setting the default packet trimming profile, you can also modify any of the {{<link url="#configure-packet-trimming" text="individual settings">}}.

To disable packet trimming, run the `nv set system forwarding packet-trim state disabled` command.

To unset the default packet trimming profile, run the `nv unset system forwarding packet-trim profile packet-trim-default` command.

### Global Level Packet Trimming with RoCE

The RoCE `lossy-multi-tc` profile uses the {{<link url="#global-level-packet-trimming-with-default-profile" text="default packet trimming profile">}} settings. To configure global level packet trimming with RoCE, refer to {{<link url="RDMA-over-Converged-Ethernet-RoCE/#lossy-multi-tc-profile" text="Lossy Multi TC Profile">}}.

## Port Level Packet Trimming

By default, you remark all trimmed packets with the same DSCP value; however, you can use a different DSCP value for trimmed packets sent out through different ports. For example, you can use DSCP 20 to send trimmed packets to hosts but DSCP 10 to send trimmed packets to the uplink. This allows the destination to know where congestion occurs; on downlinks to servers or in the fabric.

To enable and configure port level packet trimming:
- Enable packet trimming.
- Configure the port eligibility by setting the egress port and traffic class from which to trim and recirculate dropped traffic. You can only configure physical ports; if we want to trim packets egressing bonds, specify the bond slave ports. You can specify a traffic class value between 0 and 7.
- Set the DSCP remark to be at the port level.
- Create port profiles and assign the switch priority and DSCP values for each profile. Do not configure the rewrite type for the remark profile.
- Set the maximum size of the trimmed packet in bytes. You can specify a value between 256 and 1024; the value must be a multiple of 4.
- Set the switch priority of the trimmed packet. You can specify a value between 0 and 7.

The following example uses DSCP 20 on ports swp17 through swp32 to hosts but DSCP 10 on ports swp1 through swp17 to the uplink (spine):

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
cumulus@spine01:~$ nv set system forwarding packet-trim state enabled
cumulus@spine01:~$ nv set interface swp1-3 packet-trim egress-eligibility traffic-class 1
cumulus@spine01:~$ nv set system forwarding packet-trim remark dscp 10
cumulus@spine01:~$ nv set system forwarding packet-trim size 528
cumulus@spine01:~$ nv set system forwarding packet-trim switch-priority 4
cumulus@spine01:~$ nv config apply
```

### Port Level Packet Trimming with Default Profile

If you want to use the {{<link url="#global-level-packet-trimming-with-default-profile" text="default packet trimming profile">}} instead of configuring all the settings above, run the following commands to:
- Set the default packet trimming profile `packet-trim-default`.
- Set the DSCP remark to be at the port level.
- Apply the port profiles. The default packet trimming profile uses the following port profiles:
  - `lossy-multi-tc-host-group` sets the DSCP remark value to 21 for switch priority 4 on the downlink to hosts.
  - `lossy-multi-tc-network-group` sets the DSCP remark value to 11 for switch priority 4 on the uplink to the network.

```
cumulus@switch:~$ nv set system forwarding packet-trim packet-trim-default
cumulus@leaf01:~$ nv set system forwarding packet-trim remark dscp port-level
cumulus@leaf01:~$ nv set interface swp1-16 qos remark profile lossy-multi-tc-host-group
cumulus@leaf01:~$ nv set interface swp17-32 qos remark profile lossy-multi-tc-network-group 
cumulus@switch:~$ nv config apply
```

### Port Level Packet Trimming with RoCE

The RoCE `lossy-multi-tc` profile uses the {{<link url="#global-level-packet-trimming-with-default-profile" text="default packet trimming profile">}} settings. To configure port level packet trimming with RoCE, refer to {{<link url="RDMA-over-Converged-Ethernet-RoCE/#lossy-multi-tc-profile" text="Lossy Multi TC Profile">}}.

## Show Packet Trimming Configuration

To show packet trimming configuration, run the `nv show system forwarding packet-trim` command. The `trimmed-packet-counters` field shows the number of trimmed packets.

The following example shows the `nv show system forwarding packet-trim` command output for global level packet trimming.

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
trimmed-packet-counters  166788                              

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

The following example shows the `nv show system forwarding packet-trim` command output for port level packet trimming with the default profile `packet-trim-default`:

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
 trimmed-packet-counters  166788                               

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

To show packet trimming remark information, run the `nv show system forwarding packet-trim remark` command. For port level packet trimming, the default remark value is `port-level`.

```
cumulus@switch:~$ nv show system forwarding packet-trim remark 
      operational  applied
----  -----------  -------
dscp               11
```

- To show packet trimming interface eligibility information, run the `nv show interface <interface-id> packet-trim egress-eligibility` command.
- To show packet trimming interface eligibility traffic-class information, run the `nv show interface <interface-id> packet-trim egress-eligibility traffic-class` command.
- To show packet trimming interface eligibility information for a specific traffic class, run the `nv show interface <interface-id> packet-trim egress-eligibility traffic-class <tc-id>` command.

## Packet Trimming Counters

Use NVUE commands to show and clear packet trimming counters.  

### Show Packet Trimming Counters

You can show the number of trimmed packets at the global level and the number of trimmed packets for each interface. On Spectrum-6 switches, you can also show the number of trimmed packets the switch sent successfully and the number it dropped, at the global, port, and traffic class level.

{{%notice note%}}
- You can show packet trimming counters on switches with Spectrum-4 and later ASICs.
- Spectrum-4 switches show only the total number of trimmed packets at the global, port, and traffic class level; they do not provide separate sent or dropped counters.
- Spectrum-6 switches show the number of trimmed packets sent successfully and the number dropped, at the global, port, and traffic class level.
{{%/notice%}}

To display the number of trimmed packets at both the global and interface levels, run the `nv show system forwarding packet-trim counters` command:


```
cumulus@switch:~$ nv show system forwarding packet-trim counters
Global 
 trimmed-packets      20,000 
Port-Level 
------------- 
Interface  Trim Eligible Packets Trimmed TxPackets 
---------  ------------------  ---------------- 
swp1        1000                  N/A 
swp2        2000                  N/A 
swp3        4000                  N/A 
swp4        5000                  N/A 
```

On Spectrum-6 switches, the same command also shows the number of trimmed packets sent successfully and the number dropped, at the global and port level:

```
cumulus@switch:~$ nv show system forwarding packet-trim counters
Global
 trimmed-packets           322
 trimmed-tx-packets        322
 trimmed-drop-packets      0
Port-Level
-------------
Interface  Trim Eligible Packets  Trimmed TxPackets  Trimmed Dropped Packets
---------  ---------------------  -----------------  -----------------------
swp7s0     322                    322                 0
```

To show the number of trimmed packets for a specific interface by traffic class, run the `nv show interface <interface-id> packet-trim counters` command. You must specify a specific interface. The NVUE command does not support interface ranges.

```
cumulus@switch:~$ nv show interface swp1 packet-trim counters
Traffic Class  Trim Eligible Packets 
-------------  --------------- 
1                 1000                
2                 2000              
3                 3000 
```

On Spectrum-6 switches, the same command also shows the number of trimmed packets sent successfully and the number dropped, for each traffic class:

```
cumulus@switch:~$ nv show interface swp7s0 packet-trim counters
Traffic Class  Trim Eligible Packets  Trimmed TxPackets  Trimmed Dropped Packets
-------------  ---------------------  ------------------  -----------------------
1               109                    109                 0
2               106                    106                 0
3               107                    107                 0
```

### Clear Packet Trimming Counters

You can clear both the global and interface packet trimming counters with the `nv action clear system forwarding packet-trim counters` command. NVIDIA recommends clearing packet trimming counters when you initially enable the feature or configure a new interface for packet trimming.​

```
cumulus@switch:~$ nv action clear system forwarding packet-trim counters
```

To clear the packet trimming counters globally and for all interfaces, run the `nv action clear packet-trim counters` command:

```
cumulus@switch:~$ nv action clear packet-trim counters
```

To clear the packet trimming counters for a specific interface, run the `nv action clear interface <interface-id> packet-trim counters` command:

```
cumulus@switch:~$ nv action clear interface swp1 packet-trim counters
```

## Back-to-sender Notification on Congestion Tail Drop

{{%notice note%}}
- Cumulus Linux supports back-to-sender notification on congestion tail drop on Spectrum-6 switches only, for layer 3 unicast RoCEv2 traffic with IPv4 or IPv6 outer headers, in the default VRF. The outer header can be an SRv6 encapsulation, which is how MRC carries RoCEv2 traffic.
- Back-to-sender notification is disabled by default.
{{%/notice%}}

A congested Spectrum-6 switch can discard a RoCEv2 packet at an egress shared buffer; this is a congestion tail drop. Normally the switch discards the packet silently and the sender learns of the loss only from the receiver or from a timeout. With back-to-sender notification enabled, the switch instead keeps the discarded packet's headers, marks them, and returns them to the sender, so the sender learns of the loss and can retransmit within a fraction of a round trip. This feature brings congestion tail drop back-to-sender notification to Spectrum-6, matching the behavior Spectrum-4 XGS switches already provide.

Back-to-sender notification on congestion tail drop is a property of packet trimming: you select it, instead of the existing trim-and-forward behavior, for a specific combination of egress port and traffic class. A combination you do not select for back-to-sender continues to trim-and-forward as it does today, and no combination does both. Unlike Spectrum-4, where the whole switch chooses one behavior, a Spectrum-6 switch can run both at once, on different port and traffic class combinations.

This feature is designed for XGS `dci-custom` deployments, where long-haul, inter-datacenter traffic runs on its own lossy traffic class. Enable back-to-sender only on the traffic class and ports that carry that long-haul traffic; the commands below do not require the `dci-custom` profile, but nothing checks that you scoped back-to-sender correctly.

{{%notice note%}}
Back-to-sender notification on congestion tail drop has no counters or telemetry of its own. Notifications count as trimmed packets on the same {{<link url="#packet-trimming-counters" text="packet trimming counters">}} that already report trim-and-forward, using the same metric and gNMI path names.
{{%/notice%}}

### Configure Back-to-sender Notification on Congestion Tail Drop

Back-to-sender notification on congestion tail drop shares its enable state, truncation size, and switch priority with trim-and-forward, because both run on the same underlying trim session; a change to any of these affects both. Only the DSCP value the switch marks on the notification is independent between the two.

To enable and configure back-to-sender notification on congestion tail drop:
- Enable packet trimming and set its shared truncation size and switch priority, if you have not already. Refer to {{<link url="#global-level-packet-trimming" text="Global Level Packet Trimming">}}.
- Select the egress ports and traffic class you want back-to-sender notification on, instead of trim-and-forward. This setting is required; until you set it, every trim-eligible combination stays trim-and-forward.
- Optionally, set the DSCP value the switch marks on the notification. You can specify a value between 0 and 63, or `port-level` to use the port-level remark profile. If you do not set this, the switch uses the value from the XGS parameter template.
- Optionally, set a device-wide DSCP eligibility filter, and the ingress interfaces it applies to. This filter is shared between back-to-sender and trim-and-forward. If you do not set a filter, every DSCP is eligible.

```
cumulus@switch:~$ nv set system forwarding packet-trim state enabled
cumulus@switch:~$ nv set system forwarding packet-trim remark dscp 24
cumulus@switch:~$ nv set system forwarding packet-trim size 256
cumulus@switch:~$ nv set system forwarding packet-trim switch-priority 4
cumulus@switch:~$ nv set system forwarding packet-trim notify-sender tail-drop remark dscp 11
cumulus@switch:~$ nv set interface swp1-48 packet-trim notify-sender tail-drop egress-eligibility traffic-class 4
cumulus@switch:~$ nv set system forwarding packet-trim ingress-eligibility dscp 26,46
cumulus@switch:~$ nv set system forwarding packet-trim ingress-eligibility interface swp1-10
cumulus@switch:~$ nv config apply
```

To select a second, distinct traffic class for back-to-sender on a different set of ports:

```
cumulus@switch:~$ nv set interface swp33-48 packet-trim notify-sender tail-drop egress-eligibility traffic-class 5
cumulus@switch:~$ nv config apply
```

{{%notice note%}}
- Back-to-sender-enabled ports support at most three distinct sets of eligible traffic classes across the switch; ports with the same set of classes share one hardware resource. A fourth distinct set is refused, naming the ports and the sets involved.
- If a DSCP eligible for trimming resolves, through your QoS configuration, onto the traffic class the switch trims to, the switch accepts the configuration but reports a warning in the `nv show system forwarding packet-trim notify-sender` command output.
- Enable back-to-sender only on traffic classes carrying traffic that leaves the datacenter, and do not enable it on a lossless traffic class. The switch does not check either of these; get them wrong and the feature still applies, just not usefully.
- If you change QoS or class-of-service configuration after you configure back-to-sender, recheck that your eligible DSCP values still resolve to the traffic class you intend. The switch does not revalidate this automatically.
- Changing any back-to-sender or trim-and-forward parameter briefly interrupts trimming while the switch rebuilds the trim session. Forwarding is not affected.
- Cumulus Linux does not rate-limit back-to-sender notifications.
{{%/notice%}}

If the configuration is not valid, `nv config apply` fails and the switch logs the reason to the system log.

To turn off packet trimming, including back-to-sender notification, without discarding your eligibility configuration, run the `nv unset system forwarding packet-trim state` command:

```
cumulus@switch:~$ nv unset system forwarding packet-trim state
cumulus@switch:~$ nv config apply
```

### Show Back-to-sender Notification on Congestion Tail Drop Configuration

To show the requested and applied back-to-sender configuration for congestion tail drop, and the resolved eligible traffic classes with their interfaces, run the `nv show system forwarding packet-trim notify-sender` command. If you also configure back-to-sender notification on link down, the same command shows that configuration too; refer to {{<link url="#show-back-to-sender-notification-configuration" text="Show Back-to-sender Notification Configuration">}}.

- To show the configuration for a specific interface, run the `nv show interface <interface-id> packet-trim notify-sender tail-drop` command.
- To show only the eligible traffic classes for a specific interface, run the `nv show interface <interface-id> packet-trim notify-sender tail-drop egress-eligibility` command.

<!-- TODO: capture this output on a Spectrum-6 switch and paste it here. The block below is adapted
     from the specification's own draft output. -->

```
cumulus@switch:~$ nv show system forwarding packet-trim notify-sender
                  operational  applied  pending
----------------  -----------  -------  -------
tail-drop
  state           enabled      enabled  enabled
  remark
    dscp          11           11       11

BTS Egress Eligibility TC-to-Interface Information
====================================================
TC  Interfaces
--  ----------
4   swp1-swp48
5   swp33-swp48
```

If the configuration is refused, the command shows the same view with the columns disagreeing, and the reason in `session-down-reason`:

```
cumulus@switch:~$ nv show system forwarding packet-trim notify-sender
                       operational  applied  pending
---------------------  -----------  -------  -------
tail-drop
  state                disabled     enabled  enabled
  session-down-reason  packet-trim: swp5 TC4 is in both the trim-and-forward
                        and the BTS eligibility list; a port and traffic class
                        selects one direction
```

## Back-to-sender Notification on Link Down

{{%notice note%}}
- Cumulus Linux supports back-to-sender notification on link down on Spectrum-6 switches only, for layer 3 unicast RoCEv2 and MRC (Multipath Reliable Connection) traffic.
- Back-to-sender notification is disabled by default.
{{%/notice%}}

MRC uses a static SRv6 route. When the egress link fails, the sender keeps transmitting until FRR withdraws that route, and the switch drops those packets silently. Back-to-sender notification trims each affected packet and returns it to the sender, so the sender fails over without waiting for the control plane to converge. The switch sends notifications both while the withdrawn route is still in hardware and after FRR withdraws it.

Back-to-sender notification on link down runs alongside packet trimming. It uses its own recirculation session and its own service port.

### Configure Back-to-sender Notification

To enable and configure back-to-sender notification on link down:
- Set the state to enabled.
- Optionally, set the DSCP value the switch writes onto the notification. You can specify a value between 0 and 63; the default is 11. Port level remarking is not supported for notifications. The value cannot be one of the ingress eligibility DSCP values below.
- Optionally, set the ingress eligibility DSCP match list on the interfaces you want to cover, or on all interfaces. The switch sends a notification only for a packet that arrives with one of these DSCP values. If you do not set this while the feature is enabled, the switch programs a default of all DSCP values (0-63).
- Optionally, set the maximum size of the notification in bytes. You can specify a value between 256 and 1024; the value must be a multiple of 4. The default is 256.
- Optionally, set the switch priority of the notification. You can specify a value between 0 and 7. The default is 1.
- Optionally, set the service port. The service port must be a bonus port, and cannot be the same port trim-and-forward or back-to-sender on congestion tail drop uses. If you do not set one, the switch uses the platform bonus port.

```
cumulus@switch:~$ nv set system forwarding packet-trim notify-sender link-down state enabled
cumulus@switch:~$ nv set system forwarding packet-trim notify-sender link-down remark dscp 46
cumulus@switch:~$ nv set system forwarding packet-trim notify-sender link-down size 256
cumulus@switch:~$ nv set system forwarding packet-trim notify-sender link-down switch-priority 1
cumulus@switch:~$ nv set system forwarding packet-trim notify-sender link-down service-port swp66
cumulus@switch:~$ nv set interface all packet-trim spxm notify-sender link-down ingress-eligibility dscp 10
cumulus@switch:~$ nv config apply
```

To cover only certain ingress interfaces, specify an interface range instead of `all`:

```
cumulus@switch:~$ nv set interface swp1-4 packet-trim spxm notify-sender link-down ingress-eligibility dscp 10
cumulus@switch:~$ nv config apply
```

{{%notice note%}}
- The remark DSCP must not be one of the ingress eligibility DSCP values.
- Ingress eligibility is by ingress interface. You cannot scope notifications by egress interface.
- The switch returns notifications in the default VRF only.
- The switch does not configure buffer or scheduler QoS on the service port. Configure the service port QoS yourself.
- If a default route or super-net route with a valid next hop covers the traffic, the switch reroutes the traffic and sends no notification. If that route is a blackhole or reject route, the switch drops the traffic and sends no notification.
- After FRR withdraws the route, notifications require {{<link url="Segment-Routing" text="segment routing">}} to be enabled. With SRv6 disabled, the switch sends notifications only while the route is still installed.
{{%/notice%}}

If the configuration is not valid, `nv config apply` fails and the switch logs the reason to the system log.

To disable back-to-sender notification on link down, run the `nv unset system forwarding packet-trim notify-sender link-down` command.

### Show Back-to-sender Notification Configuration

To show the requested and applied back-to-sender configuration, the resolved service port, and the apply verdict, run the `nv show system forwarding packet-trim notify-sender` command:

<!-- TODO: capture this output on a Spectrum-6 switch and paste it here. The block below is adapted
     from the specification's own draft output. -->

```
cumulus@switch:~$ nv show system forwarding packet-trim notify-sender
                      operational  applied
--------------------  -----------  -------
link-down
  state               enabled      enabled
  remark
    dscp              46           46
  size                256          256
  switch-priority     1            1
  service-port        swp66        swp66
  ingress-eligibility
    ports             all          all
    dscp              10           10
  apply-verdict       ok           --
```

- To show only the link down configuration, run the `nv show system forwarding packet-trim notify-sender link-down` command.
- To show the link down configuration for an interface, run the `nv show interface <interface-id> packet-trim spxm notify-sender link-down` command.
- To show only the ingress eligibility DSCP configuration for an interface, run the `nv show interface <interface-id> packet-trim spxm notify-sender link-down ingress-eligibility` command.

### Show and Clear Back-to-sender Notification on Link Down Counters

To show the counters for back-to-sender notification on link down, run the `nv show system forwarding packet-trim notify-sender link-down counters` command:

<!-- TODO: capture this output on a Spectrum-6 switch and paste it here. The specification does not
     give a worked example of this output; the layout below follows the format of the other show
     commands on this page. Delete this comment before publishing. -->

```
cumulus@switch:~$ nv show system forwarding packet-trim notify-sender link-down counters
                      operational
--------------------  -----------
spxm-link-down-pkts   0
trim-link-down-pkts   0
last-clear-time       never
```

- `spxm-link-down-pkts` shows the number of packets that matched the back-to-sender classifier on link down, both while the route is still in hardware and after FRR withdraws it. This counts notifications the switch attempted, not notifications the switch confirmed the sender received.
- `trim-link-down-pkts` shows the number of those packets the switch actually trimmed and sent from the service port.
- `last-clear-time` shows when you last cleared these counters.

To clear the counters, run the `nv action clear system forwarding packet-trim notify-sender link-down counters` command:

```
cumulus@switch:~$ nv action clear system forwarding packet-trim notify-sender link-down counters
```

{{%notice note%}}
Clearing the counters resets only the values this command shows. The underlying hardware counters are not cleared, and continue counting from where they were; gNMI and OpenTelemetry report the uncleared hardware values.
{{%/notice%}}

## Troubleshooting

If packet trimming is not working, check the `session-down-reason` field in the `nv show system forwarding packet-trim` command output to examine the reason.

```
cumulus@switch:~$ nv show system forwarding packet-trim 
                           operational                           applied                         
-------------------------  ------------------------------------  -------------------  
state                      disabled                              enabled                       
profile                                                          packet-trim-default  
service-port               swp65                                                                         
size                       253                                                                           
traffic-class              4                                                                             
switch-priority            4                                                                             
remark                                                                                                   
  dscp                     11                                                                            
session-info                                                                                             
  session-id               0xffff                                                                        
  trimmed-packet-counters  0                                                                             
  session-down-reason      Failed to create/update span session                                          

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
