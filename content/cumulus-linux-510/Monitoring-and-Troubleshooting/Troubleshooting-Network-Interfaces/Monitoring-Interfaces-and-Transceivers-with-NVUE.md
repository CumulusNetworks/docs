---
title: Monitoring Interfaces and Transceivers with NVUE
author: NVIDIA
weight: 1100
toc: 4
---
NVUE enables you to check the status of an interface, and view and clear interface counters. Interface counters provide information about an interface, such as the number of packets dropped, the number of inbound and outbound packets not transmitted because of errors, and so on.

## Monitor Interface Status

To check the configuration and statistics for an interface, run the `nv show interface <interface>` command:

```
cumulus@switch:~$ nv show interface swp1
                          operational        applied  pending
------------------------  -----------------  -------  -------
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
    out-bytes              9.73 MB
    out-drops              0                           
    out-errors             0                           
    out-pkts               140188                      
  mac                      48:b0:2d:ef:52:b8           
ifindex                    3
```

## Show Interface Counters

NVUE provides the following commands to show counters (statistics) for the interfaces on the switch.

| <div style="width:430px">NVUE Command | Description |
| ----------- | ------------ |
| `nv show interface --view counters` |  Shows all statistics for all the interfaces configured on the switch, such as the total number of received and transmitted packets, and the number of received and transmitted dropped packets and error packets.
| `nv show interface <interface> counters` | Shows all statistics for a specific interface, such as the number of received and transmitted unicast, multicast and broadcast packets, the number of received and transmitted dropped packets and error packets, and the number of received and transmitted packets of a certain size.|
| `nv show interface <interface> counters errors`| Shows the number of error packets for a specific interface, such as the number of received and transmitted packet alignment, oversize, undersize, and jabber errors. |
| `nv show interface <interface> counters drops` | Shows the number of received and transmitted packet drops for a specific interface, such as ACL drops, buffer drops, queue drops, and non-queue drops.|
| `nv show interface <interface> counters pktdist` | Shows the number of received and transmitted packets of a certain size for a specific interface. |
| `nv show interface <interface> counters qos` | Shows QoS statistics for the specified interface. See {{<link url="Quality-of-Service/#show-qos-counters" text="Show Qos Counters">}}.|
| `nv show interface <interface> counters ptp` | Shows PTP statistics for a specific interface. See {{<link url="Precision-Time-Protocol-PTP/#show-ptp-counters" text="Show PTP Counters">}}.|

The following example shows all statistics for all the interfaces configured on the switch:

```
cumulus@switch$ nv show interface --view counters
Interface       MTU    RX_OK  RX_ERR  RX_DRP  RX_OVR  TX_OK  TX_ERR  TX_DRP  TX_OVR  Flg  
--------------  -----  -----  ------  ------  ------  -----  ------  ------  ------  -----
BLUE            65575  1      0       0       0       0      0       4       0       OmRU 
RED             65575  1      0       0       0       0      0       4       0       OmRU 
bond1           9000   718    0       0       0       1091   0       0       0       BMmRU
bond2           9000   727    0       0       0       1088   0       0       0       BMmRU
bond3           9000   722    0       0       0       1089   0       0       0       BMmRU
br_default      9216   360    0       10      0       475    0       0       0       BMRU 
eth0            1500   946    0       0       0       299    0       0       0       BMRU 
lo              65536  651    0       0       0       651    0       0       0       LRU  
mgmt            65575  283    0       0       0       0      0       4       0       OmRU 
peerlink        9216   4972   0       0       0       5028   0       0       0       BMmRU
peerlink.4094   9216   3263   0       0       0       3224   0       0       0       BMRU 
swp1            9000   721    0       0       0       1091   0       0       0       BMsRU
swp2            9000   730    0       0       0       1088   0       0       0       BMsRU
swp3            9000   725    0       0       0       1089   0       0       0       BMsRU
swp49           9216   2807   0       0       0       2691   0       0       0       BMsRU
swp50           9216   2165   0       0       0       2337   0       0       0       BMsRU
swp51           9216   685    0       0       0       690    0       0       0       BMRU 
swp52           9216   703    0       0       0       722    0       0       0       BMRU 
swp53           9216   738    0       0       0       710    0       0       0       BMRU 
swp54           9216   682    0       0       0       730    0       0       0       BMRU 
vlan10          9216   108    0       20      0       91     0       0       0       BMRU 
vlan10-v0       9216   63     0       20      0       45     0       0       0       BMRU 
vlan20          9216   104    0       20      0       88     0       0       0       BMRU 
vlan20-v0       9216   58     0       20      0       44     0       0       0       BMRU 
vlan30          9216   112    0       20      0       94     0       0       0       BMRU 
vlan30-v0       9216   61     0       20      0       44     0       0       0       BMRU 
vlan4024_l3     9216   1      0       0       0       82     0       0       0       BMRU 
vlan4024_l3-v0  9216   0      0       0       0       36     0       0       0       BMRU 
vlan4036_l3     9216   1      0       0       0       85     0       0       0       BMRU 
vlan4036_l3-v0  9216   0      0       0       0       37     0       0       0       BMRU 
vxlan48         9216   45     0       0       0       21     0       0       0       BMRU
```

The following example shows all statistics for swp1:

```
cumulus@switch$ nv show interface swp1 counters
                     operational  applied
-------------------  -----------  -------
carrier-transitions  4                   

Detailed Counters
====================
    Counter            Receive  Transmit
    -----------------  -------  --------
    Broadcast Packets  0        0       
    Multicast Packets  0        0       
    Total Octets       0        0       
    Total Packets      0        0       
    Unicast Packets    0        0       

Drop Counters
================
    Counter          Receive  Transmit
    ---------------  -------  --------
    ACL Drops        0        n/a     
    Buffer Drops     0        n/a     
    Non-Queue Drops  n/a      0       
    Queue Drops      n/a      0       
    Total Drops      0        0       

Error Counters
=================
    Counter           Receive  Transmit
    ----------------  -------  --------
    Alignment Errors  0        n/a     
    FCS Errors        0        n/a     
    Jabber Errors     0        n/a     
    Length Errors     0        n/a     
    Oversize Errors   0        n/a     
    Symbol Errors     0        n/a     
    Total Errors      0        0       
    Undersize Errors  0        n/a     

Packet Size Statistics
=========================
    Counter     Receive  Transmit
    ----------  -------  --------
    64          0        0       
    65-127      0        0       
    128-255     0        0       
    256-511     0        0       
    512-1023    0        0       
    1024-1518   0        0       
    1519-2047   0        0       
    2048-4095   0        0       
    4096-16383  0        0

Ingress Buffer Statistics
============================
    priority-group  rx-frames  rx-buffer-discards  rx-shared-buffer-discards
    --------------  ---------  ------------------  -------------------------
    0               0          0 Bytes             0 Bytes                  
    1               0          0 Bytes             0 Bytes                  
    2               0          0 Bytes             0 Bytes                  
    3               0          0 Bytes             0 Bytes                  
    4               0          0 Bytes             0 Bytes                  
    5               0          0 Bytes             0 Bytes                  
    6               0          0 Bytes             0 Bytes                  
    7               0          0 Bytes             0 Bytes 
...
```

The following example shows error counters for swp1:

```
cumulus@switch$ nv show interface swp1 counters errors
Counter           Receive  Transmit
----------------  -------  --------
Alignment Errors  0        n/a     
FCS Errors        0        n/a     
Jabber Errors     0        n/a     
Length Errors     0        n/a     
Oversize Errors   0        n/a     
Symbol Errors     0        n/a     
Total Errors      0        0       
Undersize Errors  0        n/a   
```

{{%notice note%}}
- NVUE does not show detailed statistics for logical interfaces, such as bonds, VLAN interfaces or subinterfaces. To see basic statistics for logical interfaces, run the `nv show interface <interface> link stats` command.
- On NVIDIA Spectrum switches, Cumulus Linux updates physical counters to the kernel every two seconds and virtual interfaces (such as VLAN interfaces) every ten seconds. You cannot change these values. Because the update process takes a lower priority than other `switchd` processes, the interval might be longer when the system is under a heavy load.
{{%/notice%}}

## PHY Health Management

To show PHY details:

```
cumulus@switch$ nv show interface swp1 link phy-detail 
                           operational 

-------------------------  ---------------- 
time-since-last-clear-min  395 
phy-received-bits          2373169010065408 
symbol-errors              0 
effective-errors           0 
phy-raw-errors-lane0       0 
phy-raw-errors-lane1       0 
phy-raw-errors-lane2       0 
phy-raw-errors-lane3       0 
phy-raw-errors-lane4       0 
phy-raw-errors-lane5       0 
phy-raw-errors-lane6       0 
phy-raw-errors-lane7       0 
raw-ber                    15E-255 
symbol-ber                 15E-255 
effective-ber              15E-255 
raw-ber-lane0              0 
raw-ber-lane1              0 
raw-ber-lane2              0 
raw-ber-lane3              0 
raw-ber-lane4              0 
raw-ber-lane5              0 
raw-ber-lane6              0 
raw-ber-lane7              0 
rs-num-corr-err-bin0       463548146626 
rs-num-corr-err-bin1       0 
rs-num-corr-err-bin2       0 
rs-num-corr-err-bin3       0 
rs-num-corr-err-bin4       0 
rs-num-corr-err-bin5       0 
rs-num-corr-err-bin6       0 
rs-num-corr-err-bin7       0 
rs-num-corr-err-bin8       0 
rs-num-corr-err-bin9       0 
rs-num-corr-err-bin10      0 
rs-num-corr-err-bin11      0 
rs-num-corr-err-bin12      0 
rs-num-corr-err-bin13      0 
rs-num-corr-err-bin14      0 
rs-num-corr-err-bin15      0 
```

To show PHY diagnostics:

```
cumulus@switch$ nv show interface swp20 link phy-diag 
                                  operational 
--------------------------------  ----------- 
pd-fsm-state                      0x8 
eth-an-fsm-state                  0x6 
phy-hst-fsm-state                 0x0 
psi-fsm-state                     0x0 
phy-manager-link-enabled          0x97f2 
core-to-phy-link-enabled          0x2f2 
cable-proto-cap-ext               0x0 
loopback-mode                     0x0 
retran-mode-request               0x0 
retran-mode-active                0x0 
fec-mode-request                  0x4 
profile-fec-in-use                0x4 
pd-link-enabled                   0xff8005 
phy-hst-link-enabled              0x0 
eth-an-link-enabled               0x5cf0002 
phy-manager-state                 0x3 
eth-proto-admin                   0x0 
ext-eth-proto-admin               0x0 
eth-proto-capability              0x0 
ext-eth-proto-capability          0x0 
data-rate-oper                    0x0 
an-status                         0x0 
an-disable-admin                  0x0 
proto-mask                        0x2 
module-info-ext                   0x0 
ethernet-compliance-code          0x80 
ext-ethernet-compliance-code      0x18 
memory-map-rev                    0x7 
linear-direct-drive               0x0 
cable-breakout                    0x10 
cable-rx-amp                      0x0 
cable-rx-pre-emphasis             0x0 
cable-rx-post-emphasis            0x0 
cable-tx-equalization             0x0 
cable-attenuation-53g             0x0 
cable-attenuation-25g             0x0 
cable-attenuation-12g             0x0 
cable-attenuation-7g              0x0 
cable-attenuation-5g              0x0 
tx-input-freq-sync                0x0 
tx-cdr-state                      0xf 
rx-cdr-state                      0xf 
module-fw-version                 0x201e010a 
module-st                         0x0 
dp-st-lane0                       0x0 
dp-st-lane1                       0x0 
dp-st-lane2                       0x0 
dp-st-lane3                       0x0 
dp-st-lane4                       0x0 
dp-st-lane5                       0x0 
dp-st-lane6                       0x0 
dp-st-lane7                       0x0 
rx-output-valid                   0x0 
rx-power-type                     0x1 
active-set-host-compliance-code   0x0 
active-set-media-compliance-code  0x0 
error-code-response               0x0 
temp-flags                        0x0 
vcc-flags                         0x0 
mod-fw-fault                      0x0 
dp-fw-fault                       0x0 
rx-los-cap                        0x0 
tx-fault                          0x0 
tx-los                            0x0 
tx-cdr-lol                        0x0 
tx-ad-eq-fault                    0x0 
rx-los                            0x0 
rx-cdr-lol                        0x0 
rx-output-valid-change            0x0 
flag-in-use                       0x0 
```

## Clear Interface Counters

To clear counters (statistics) for all interfaces, run the `nv action clear interface counters` command:

```
cumulus@switch$ nv action clear interface counters
all interface counters cleared
Action succeeded
```

To clear the counters for an interface, run the `nv action clear interface <interface> counters` command:

```
cumulus@switch$ nv action clear interface swp1 counters
swp1 counters cleared
Action succeeded
```

{{%notice note%}}
The `nv action clear interface <interface> counters` command does not clear counters in the hardware.
{{%/notice%}}
