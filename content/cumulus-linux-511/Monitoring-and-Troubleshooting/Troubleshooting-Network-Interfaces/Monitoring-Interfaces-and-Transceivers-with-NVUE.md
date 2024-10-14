---
title: Monitoring Interfaces and Transceivers with NVUE
author: NVIDIA
weight: 1100
toc: 4
---
NVUE enables you to check the status of an interface, and view and clear interface counters. Interface counters provide information about an interface, such as the number of packets dropped, the number of inbound and outbound packets not transmitted because of errors, and so on.

## Show Interface Configuration and Statistics

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

## AmBER PHY Health Management

To show physical layer information, such as the error counters for each lane on a port, run the `nv show interface <interface> link phy-detail` command. This command highlights link integrity issues.

```
cumulus@switch$ nv show interface swp1 link phy-detail 
                          operational
-------------------------  -----------------
time-since-last-clear-min  324
phy-received-bits          15561574400000000
symbol-errors              0
effective-errors           0
phy-raw-errors-lane0       747567424
phy-raw-errors-lane1       215603747
phy-raw-errors-lane2       158456437
phy-raw-errors-lane3       30578923
phy-raw-errors-lane4       121708834
phy-raw-errors-lane5       29244642
phy-raw-errors-lane6       79102523
phy-raw-errors-lane7       96656135
raw-ber                    1E-7
symbol-ber                 15E-255
effective-ber              15E-255
raw-ber-lane0              3E-6
raw-ber-lane1              9E-7
raw-ber-lane2              6E-7
raw-ber-lane3              1E-7
raw-ber-lane4              5E-7
raw-ber-lane5              1E-7
raw-ber-lane6              3E-7
raw-ber-lane7              4E-7
rs-num-corr-err-bin0       757956054591
rs-num-corr-err-bin1       598244758
rs-num-corr-err-bin2       807002
rs-num-corr-err-bin3       3371
rs-num-corr-err-bin4       180
rs-num-corr-err-bin5       1
rs-num-corr-err-bin6       0
rs-num-corr-err-bin7       0
rs-num-corr-err-bin8       1
rs-num-corr-err-bin9       0
rs-num-corr-err-bin10      0
rs-num-corr-err-bin11      0
rs-num-corr-err-bin12      0
rs-num-corr-err-bin13      0
rs-num-corr-err-bin14      0
rs-num-corr-err-bin15      0
```

To show physical layer diagnostic information for a port, run the `nv show interface <interface> link phy-diag` command:

```
cumulus@switch$ nv show interface swp20 link phy-diag 
                                  operational
--------------------------------  -----------
pd-fsm-state                      0x7
eth-an-fsm-state                  0x6
phy-hst-fsm-state                 0x8
psi-fsm-state                     0x0
phy-manager-link-enabled          0x9bff0
core-to-phy-link-enabled          0x9b800
cable-proto-cap-ext               0x0
loopback-mode                     0x0
retran-mode-request               0x0
retran-mode-active                0x0
fec-mode-request                  0x1
profile-fec-in-use                0x4
pd-link-enabled                   0x80000
phy-hst-link-enabled              0x80000
eth-an-link-enabled               0x0
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
ethernet-compliance-code          0x1c
ext-ethernet-compliance-code      0x32
memory-map-rev                    0x40
linear-direct-drive               0x0
cable-breakout                    0x0
cable-rx-amp                      0x1
cable-rx-pre-emphasis             0x0
cable-rx-post-emphasis            0x0
cable-tx-equalization             0x0
cable-attenuation-53g             0x0
cable-attenuation-25g             0x0
cable-attenuation-12g             0x0
cable-attenuation-7g              0x0
cable-attenuation-5g              0x0
tx-input-freq-sync                0x0
tx-cdr-state                      0xff
rx-cdr-state                      0xff
module-fw-version                 0x2e820043
module-st                         0x3
dp-st-lane0                       0x4
dp-st-lane1                       0x4
dp-st-lane2                       0x4
dp-st-lane3                       0x4
dp-st-lane4                       0x4
dp-st-lane5                       0x4
dp-st-lane6                       0x4
dp-st-lane7                       0x4
rx-output-valid                   0x0
rx-power-type                     0x1
active-set-host-compliance-code   0x52
active-set-media-compliance-code  0x1c
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

{{%notice note%}}
Switches with the Spectrum 1 ASIC do not support the `nv show interface <interface> link phy-detail` command or the `nv show interface <interface> link phy-diag` command.
{{%/notice%}}

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

## Show Transceiver Information

To show the identifier, vendor name, part number, serial number, and revision for all SFP or QSFP modules, run the `nv show platform transceiver` command:

```
cumulus@switch:~$ nv show platform transceiver 
Transceiver  Identifier                     Vendor Name  Vendor PN         Vendor SN      Vendor Rev 
---------  -------------------------------  -----------  ----------------  -------------  ---------- 
swp1       QSFP28                           Mellanox     MCP1600-C001E30N  MT2039VB01185  A3 
swp10      QSFP28                           Mellanox     MCP1600-C001E30N  MT2211VS01792  A3 
swp11      QSFP28                           Mellanox     MCP1600-C001E30N  MT2211VS01792  A3 
swp12      QSFP28                           Mellanox     MCP1650-V00AE30   MT2122VB02220  A2 
swp13      QSFP28                           Mellanox     MCP1650-V00AE30   MT2122VB02220  A2 
swp14      QSFP-DD                          Mellanox     MCP1660-W00AE30   MT2121VS01645  A3 
swp15      QSFP-DD                          Mellanox     MCP1660-W00AE30   MT2121VS01645  A3 
swp18      QSFP28                           Mellanox     MCP1600-C001E30N  MT2211VS01967  A3 
swp20s0    QSFP28                           Mellanox     MFA1A00-C003      MT2108FT02204  B2 
swp20s1    QSFP28                           Mellanox     MFA1A00-C003      MT2108FT02204  B2 
swp21s0    QSFP28                           Mellanox     MFA1A00-C003      MT2108FT02204  B2 
swp21s1    QSFP28                           Mellanox     MFA1A00-C003      MT2108FT02204  B2 
swp22      QSFP28                           Mellanox     MFA1A00-C003      MT2108FT02194  B2 
swp23      QSFP28                           Mellanox     MFA1A00-C003      MT2108FT02194  B2 
swp31      QSFP28                           Mellanox     MCP1600-C001E30N  MT2039VB01191  A3 
```

To show a detailed view of SFP or QSFP module information for all ports that includes cable length, type, and diagnostics, current status and error status, run the `nv show platform transceiver details` command.

To show hardware capabilities and measurement information on the SFP or QSFP module in a particular port, run the `nv show platform transceiver <interface>` command:

```
cumulus@switch:~$ nv show platform transceiver swp2
cable-type             : Active cable 
cable-length           : 3m 
supported-cable-length : 0 om1, 0 om2, 0 om3, 3 om4, 0 om5 
diagnostics-status     : Diagnostic Data Available 
status                 : plugged_enabled 
error-status           : Power_Budget_Exceeded 
vendor-data-code       : 210215__ 
identifier             : QSFP28 
vendor-rev             : B2 
vendor-name            : Mellanox 
vendor-pn              : MFA1A00-C003 
vendor-sn              : MT2108FT02204 
temperature: 
  temperature         : 48.74 C 
  high-alarm-threshold: 80.00 C 
  low-alarm-threshold : -10.00 C 
  alarm               : Off 
voltage: 
  voltage             : 3.2692 V 
  high-alarm-threshold: 3.5000 V 
  low-alarm-threshold : 3.1000 V 
  alarm               : Off 
channel: 
  channel-1: 
    rx-power: 
        power            : 0.0000 mW / -inf dBm 
        high-alarm-thresh: 5.40 dBm 
        low-alarm-thresh : -13.31 dBm 
        alarm            : low 
    tx-power: 
        power            : 0.0000 mW / -inf dBm 
        high-alarm-thresh: 5.40 dBm 
        low-alarm-thresh : -11.40 dBm 
        alarm            : Off 
    tx-bias-current: 
        current          : 0.000 mA 
        high-alarm-thresh: 8.500 mA 
        low-alarm-thresh : 5.492 mA 
        alarm            : low 
  channel-2: 
    rx-power: 
        power            : 0.0000 mW / -inf dBm 
        high-alarm-thresh: 5.40 dBm 
        low-alarm-thresh : -13.31 dBm 
        alarm            : low 
    tx-power: 
        power            : 0.0000 mW / -inf dBm 
        high-alarm-thresh: 5.40 dBm 
        low-alarm-thresh : -11.40 dBm 
        alarm            : low 
    tx-bias-current: 
        current          : 0.000 mA 
        high-alarm-thresh: 8.500 mA 
        low-alarm-thresh : 5.492 mA 
        alarm            : low 
  channel-3: 
    rx-power: 
        power            : 0.0000 mW / -inf dBm 
        high-alarm-thresh: 5.40 dBm 
        low-alarm-thresh : -13.31 dBm 
        alarm            : low 
    tx-power: 
        power            : 0.0000 mW / -inf dBm 
        high-alarm-thresh: 5.40 dBm 
        low-alarm-thresh : -11.40 dBm 
        alarm            : low 
    tx-bias-current: 
        current          : 0.000 mA 
        high-alarm-thresh: 8.500 mA 
        low-alarm-thresh : 5.492 mA 
        alarm            : low 
  channel-4: 
    rx-power: 
        power            : 0.0000 mW / -inf dBm 
        high-alarm-thresh: 5.40 dBm 
       low-alarm-thresh : -13.31 dBm 
        alarm            : low 
    tx-power: 
        power            : 0.0000 mW / -inf dBm 
        high-alarm-thresh: 5.40 dBm 
        low-alarm-thresh : -11.40 dBm 
        alarm            : low 
    tx-bias-current: 
        current          : 0.000 mA 
        high-alarm-thresh: 8.500 mA 
        low-alarm-thresh : 5.492 mA 
        alarm            : low 
```

To show channel information for the SFP or QSFP module in a particular port, run the `nv show platform transceiver <interface> channel` command. To show specific channel information for the SFP or QSFP module in a particular port, run the `nv show platform transceiver <interface> channel <channel>` command.

```
cumulus@switch:~$ nv show platform transceiver swp25 channel 
channel: 
  channel-1: 
    rx-power: 
        power            : 0.0000 mW / -inf dBm 
        high-alarm-thresh: 5.40 dBm 
        low-alarm-thresh : -13.31 dBm 
        alarm            : low 
    tx-power: 
        power            : 0.0000 mW / -inf dBm 
        high-alarm-thresh: 5.40 dBm 
        low-alarm-thresh : -11.40 dBm 
        alarm            : Off 
    tx-bias-current: 
        current          : 0.000 mA 
        high-alarm-thresh: 8.500 mA 
        low-alarm-thresh : 5.492 mA 
        alarm            : low 
  channel-2: 
    rx-power: 
        power            : 0.0000 mW / -inf dBm 
        high-alarm-thresh: 5.40 dBm 
        low-alarm-thresh : -13.31 dBm 
        alarm            : low 
    tx-power: 
        power            : 0.0000 mW / -inf dBm 
        high-alarm-thresh: 5.40 dBm 
        low-alarm-thresh : -11.40 dBm 
        alarm            : low 
    tx-bias-current:
        current          : 0.000 mA 
        high-alarm-thresh: 8.500 mA 
        low-alarm-thresh : 5.492 mA 
        alarm            : low 
  channel-3: 
    rx-power: 
        power            : 0.0000 mW / -inf dBm 
        high-alarm-thresh: 5.40 dBm 
        low-alarm-thresh : -13.31 dBm 
        alarm            : low 
    tx-power: 
        power            : 0.0000 mW / -inf dBm 
        high-alarm-thresh: 5.40 dBm 
        low-alarm-thresh : -11.40 dBm 
        alarm            : low 
    tx-bias-current: 
        current          : 0.000 mA 
        high-alarm-thresh: 8.500 mA 
        low-alarm-thresh : 5.492 mA 
        alarm            : low 
  channel-4: 
    rx-power: 
        power            : 0.0000 mW / -inf dBm 
        high-alarm-thresh: 5.40 dBm 
        low-alarm-thresh : -13.31 dBm 
        alarm            : low 
    tx-power: 
        power            : 0.0000 mW / -inf dBm 
        high-alarm-thresh: 5.40 dBm 
        low-alarm-thresh : -11.40 dBm 
        alarm            : low 
    tx-bias-current: 
        current          : 0.000 mA 
        high-alarm-thresh: 8.500 mA 
        low-alarm-thresh : 5.492 mA 
        alarm            : low 
```

To show the thresholds for the SFP or QSFP module in a particular port, run the `nv show interface <interface> transceiver thresholds` command:

```
cumulus@switch:~$ nv show interface swp3 transceiver thresholds
                                      High Alarm  High Warn   Low Warn   Low Alarm 
                     Ch   Value       Threshold   Threshold   Threshold  Threshold  Alt Value 
------------------   -------------------------------------------------------------------------- 
temperature          -    53.00 C      72.00       65.00        5.00      -2.00     127.4F 
voltage              -     3.28 V       3.50        3.47        3.14       3.10     
rx-power             1    -4.09 dBm     4.00        3.00       -4.00      -5.00       0.39 mW 
                     2    -6.58 dBm     4.00        3.00       -4.00      -5.00       0.22 mW 
tx-power             1     1.04 dBm     4.00        3.00       -4.00      -3.47       1.27 mW 
                     2     1.21 dBm     4.00        3.00       -4.00      -3.47       1.32 mW 
tx-bias-current      1     9.90 mA     11.00       10.00        8.00       7.00     
                     2     9.25 mA     11.00       10.00        8.00       7.00
```
