---
title: Monitoring Interfaces and Transceivers with NVUE
author: NVIDIA
weight: 1100
toc: 4
---
NVUE enables you to check the status of an interface, and view and clear interface counters. Interface counters provide information about an interface, such as the number of packets intentionally or intentionally dropped, the number of inbound and outbound packets discarded even though the switch detected no errors, the number of inbound and outbound packets not transmitted because of errors, and so on.

## Monitor Interface Status

To check the configuration and statistics for an interface, run the `nv show interface <interface>` command:

```
cumulus@switch:~$ nv show interface swp1
type                       swp                swp      
[acl]                                                  
evpn                                                   
  multihoming                                          
    uplink                                    off      
ptp                                                    
  enable                                      off      
router                                                 
  adaptive-routing                                     
    enable                                    off      
  ospf                                                 
    enable                                    on       
    area                                      none     
    cost                                      auto     
    mtu-ignore                                off      
    network-type                              broadcast
    passive                                   on       
    priority                                  1        
    authentication                                     
      enable                                  off      
    bfd                                                
      enable                                  off      
    timers                                             
      dead-interval                           40       
      hello-interval                          10       
      retransmit-interval                     5        
      transmit-delay                          1        
  ospf6                                                
    enable                                    off      
  pbr                                                  
    [map]                                              
  pim                                                  
    enable                                    off      
synce                                                  
  enable                                      off      
ip                                                     
  igmp                                                 
    enable                                    off      
  ipv4                                                 
    forward                                   on       
  ipv6                                                 
    enable                                    on       
    forward                                   on       
  neighbor-discovery                                   
    enable                                    on       
    [dnssl]                                            
    home-agent                                         
      enable                                  off      
    [prefix]                                           
    [rdnss]                                            
    router-advertisement                               
      enable                                  on       
      fast-retransmit                         on       
      hop-limit                               64       
      interval                                600000   
      interval-option                         off      
      lifetime                                1800     
      managed-config                          off      
      other-config                            off      
      reachable-time                          0        
      retransmit-time                         0        
      router-preference                       medium   
  vrrp                                                 
    enable                                    off      
  vrf                                         default  
  [gateway]                                            
link                                                   
  auto-negotiate           off                on       
  duplex                   full               full     
  speed                    1G                 auto     
  fec                                         auto     
  mtu                      9216               9216     
  [breakout]                                           
  state                    up                 up       
  stats                                                
    carrier-transitions    4                           
    in-bytes               300 Bytes                   
    in-drops               5                           
    in-errors              0                           
    in-pkts                5                           
    out-bytes              9.73 MB                     ß
    out-drops              0                           
    out-errors             0                           
    out-pkts               140188                      
  mac                      48:b0:2d:ef:52:b8           
ifindex                    3
```

## Show Interface Statistics

NVUE provides the following commands to show counters for the interfaces on the switch.

| NVUE Command | Description |
| ----------- | ------------ |
| `nv show interface --view counters` |  Shows all statistics for all the interfaces configured on the switch.
| `nv show interface <interface> counters` | Shows all statistics for a specific interface.|
| `nv show interface <interface> counters errors`| Shows error counters for a specific interface. |
| `nv show interface <interface> counters drops` | Shows packet drop counters for a specific interface.|
| `nv show interface <interface> counters pktdist` | Shows packet distribution counters for a specific interface. |

The following example shows all statistics for all the interfaces configured on the switch:

```
cumulus@switch$ nv show interface --view counters
```

The following example shows all statistics for swp1:

```
cumulus@switch$ nv show interface swp1 counters
```

The following example shows error counters for swp1:

```
cumulus@switch$ nv show interface swp1 counters errors
```

{{%notice note%}}
NVUE does not provide statistics for logical interfaces, such as bonds and breakout interfaces. To show VNI counters for a single VXLAN device, run the `nv show nve counters vni <vni>` command.
{{%/notice%}}

## Clear Interface Statistics

To clear counters for all interfaces, run the `nv action clear interface counters` command:

```
cumulus@switch$ nv action clear interface counters
```

To clear the counters for an interface, run the `nv action clear interface <interface> counters` command:

```
cumulus@switch$ nv action clear interface swp1 counters
```

The `nv action clear interface <interface> counters` command does not clear counters in the kernel or hardware.
