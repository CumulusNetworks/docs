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
- Cumulus Linux supports packet trimming on the Spectrum-4 switch.
- Do not enable packet trimming when the NetQ WJH agent is running or with WJH monitor buffer drops configured.
- Cumulus Linux supports packet trimming for known unicast IPv4 and IPv6 traffic. Packet trimming does not support ISSU, VXLAN packets or flooding and multicast packets.
{{%/notice%}}

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
When you enable packet trimming, one service port is used. By default, this is the last service port on the switch. To change the service port, run the `nv set system forwarding packet-trim service-port <interface-id>` command.”

On a switch that supports two service ports, you can configure a bond on the service ports, then use the bond for the packet trimming service port; for example: `nv set system forwarding packet-trim service-port bond1`. For information about service ports on Spectrum-4 switches, refer to {{<link url="Switch-Port-Attributes/#breakout-ports" text="Switch Port Attributes">}}.

When you enable packet trimming, do not configure packet trimming port eligibility, port security, adaptive routing, QoS, ACLs, PTP, VRR, PBR, telemetry, or histograms on the service port.

{{%/notice%}}

### Global Level Packet Trimming with Default Profile

Cumulus Linux provides a default packet trimming profile you can use instead of configuring all the settings above. The default packet trimming profile has the following settings:
- Enables packet trimming.
- Sets the DSCP remark value to 11 (global DSCP).
- Sets the truncation size to 256 bytes.
- Sets the switch priority to 4.
- Sets the eligibility to all ports on the switch with traffic class 1,2, and 3.

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

By default, you remark all trimmed packets with the same DSCP value; however, you can use a different DSCP value for trimmed packets sent out through different ports. For example, you can use DSCP 20 to send trimmed packets to hosts but DSCP 10 to send trimmed packets to the uplink (spine). This allows the destination to know where congestion occurs; on downlinks to servers or in the fabric.

To enable and configure port level packet trimming:
- Enable packet trimming.
- Configure the port eligibility by setting the egress port and traffic class from which to trim and recirculate dropped traffic. You can only configure physical ports; if we want to trim packets egressing bonds, specify the bond slave ports. You can specify a traffic class value between 0 and 7.
- Set the DSCP remark to be at the port level.
- Create port profiles and assign the switch priority and DSCP values for each profile. Do not configure the rewrite type for the remark profile.
- Set the maximum size of the trimmed packet in bytes. You can specify a value between 256 and 1024; the value must be a multiple of 4.
- Set the switch priority of the trimmed packet. You can specify a value between 0 and 7.

The following example configures port level packet trimming on the downlink to hosts (leaf01) to use DSCP 20 to send trimmed packets on ports swp17 through swp32 to hosts but DSCP 10 on ports swp1 through swp17 to the uplink (spine):

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

The following example shows the `nv show system forwarding packet-trim` command output for packet trimming. 

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
