---
title: Monitoring Interfaces and Transceivers with NVUE
author: NVIDIA
weight: 1100
toc: 4
---
NVUE enables you to check the status of an interface, and view and clear interface counters. Interface counters provide information about an interface, such as the number of packets dropped, the number of inbound and outbound packets not transmitted because of errors, and so on.

## Show Interface Configuration and Statistics

To check the configuration and statistics for an interface, run the `nv show interface <interface-id>` command:

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
  auto-negotiate           disabled           enabled       
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
| `nv show interface <interface-id> counters` | Shows all statistics for a specific interface, such as the number of received and transmitted unicast, multicast and broadcast packets, the number of received and transmitted dropped packets and error packets, and the number of received and transmitted packets of a certain size.|
| `nv show interface <interface-id> counters errors`| Shows the number of error packets for a specific interface, such as the number of received and transmitted packet alignment, oversize, undersize, and jabber errors. |
| `nv show interface <interface-id> counters drops` | Shows the number of received and transmitted packet drops for a specific interface, such as ACL drops, buffer drops, queue drops, and non-queue drops.|
| `nv show interface <interface-id> counters pktdist` | Shows the number of received and transmitted packets of a certain size for a specific interface. |
| `nv show interface <interface-id> counters qos` | Shows QoS statistics for the specified interface. See {{<link url="Quality-of-Service/#show-qos-counters" text="Show Qos Counters">}}.|
| `nv show interface <interface-id> counters ptp` | Shows PTP statistics for a specific interface. See {{<link url="Precision-Time-Protocol-PTP/#show-ptp-counters" text="Show PTP Counters">}}.|

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
- NVUE does not show detailed statistics for logical interfaces, such as bonds, VLAN interfaces or subinterfaces. To see basic statistics for logical interfaces, run the `nv show interface <interface-id> link stats` command.
- On NVIDIA Spectrum switches, Cumulus Linux updates physical counters to the kernel every two seconds and virtual interfaces (such as VLAN interfaces) every ten seconds. You cannot change these values. Because the update process takes a lower priority than other `switchd` processes, the interval might be longer when the system is under a heavy load.
{{%/notice%}}

## AmBER PHY Health Management

To show physical layer information, such as the error counters for each lane on a port and <span class="a-tooltip">[SNR](## "Signal-to-Noise Ratio")</span> information for media and host lanes (lane0 through lane7), run the `nv show interface <interface-id> link phy health` command.

This command highlights link integrity issues.

{{%notice note%}}
The `nv show interface <interface-id> link phy health` command shows SNR information for media and host lanes for OSFP 100G per lane capable transceivers on certain switches with the Spectrum-4 ASIC and later. The command does not show SNR information for SFP28 bonus ports.
  - For lanes not in use for the optical cable, the command output shows 0.
  - For copper ports, the command output shows n/a.
{{%/notice%}}

The `effective-ber` in the command output represents the uncorrectable bit error rate, which is the same as uncorrected FEC errors.

```
cumulus@switch$ nv show interface swp1 link phy health 
                           operational  
-------------------------  -------------
time-since-last-clear-min  1            
phy-received-bits          6214400000000
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
raw-ber                    15E-255      
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
rs-num-corr-err-bin0       1216554377   
rs-num-corr-err-bin1       598244758            
rs-num-corr-err-bin2       807002            
rs-num-corr-err-bin3       3371            
rs-num-corr-err-bin4       180            
rs-num-corr-err-bin5       1            
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
snr-host-lane0             25.12 dB              
snr-host-lane1             25.25 dB              
snr-host-lane2             25.37 dB              
snr-host-lane3             25.37 dB              
snr-host-lane4             26    dB              
snr-host-lane5             24.61 dB              
snr-host-lane6             24.12 dB              
snr-host-lane7             26    dB              
snr-media-lane0            25.05 dB              
snr-media-lane1            24.09 dB              
snr-media-lane2            25.34 dB              
snr-media-lane3            23.67 dB              
snr-media-lane4            26    dB              
snr-media-lane5            25.05 dB              
snr-media-lane6            23.12 dB              
snr-media-lane7            24.05 dB
```

To show physical layer diagnostic information for a port, run the `nv show interface <interface-id> link phy detail` command:

```
cumulus@switch$ nv show interface swp20 link phy detail 
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
Switches with the Spectrum 1 ASIC do not support the `nv show interface <interface-id> link phy health` command or the `nv show interface <interface-id> link phy detail` command.
{{%/notice%}}

## Clear Interface Counters

To clear counters (statistics) for all interfaces, run the `nv action clear interface counters` command.

```
cumulus@switch$ nv action clear interface counters
all interface counters cleared
Action succeeded
```

To clear the counters for an interface, run the `nv action clear interface <interface-id> counters` command:

```
cumulus@switch$ nv action clear interface swp1 counters
swp1 counters cleared
Action succeeded
```

{{%notice note%}}
The `nv action clear interface <interface-id> counters` command does not clear counters in the hardware.
{{%/notice%}}

## Clear Interface Physical Layer Error Counters

To clear interface physical layer error counters, run the `nv action clear interface <interface-id> link phy health` command. The command clears the counters at the software level, but not the hardware level.

```
cumulus@switch:~$ nv action clear interface swp1 link phy health
Action executing ... 
swp1 link phy health counters cleared. 
Action succeeded
```

To clear physical layer error counters for a range of interfaces:

```
cumulus@switch:~$ nv action clear interface swp1-3,swp5,swp7-10 link phy health 
Action executing ...
swp1 link phy health counters cleared.
Action executing ...
swp2 link phy health counters cleared.
swp3 link phy health counters cleared.
Action executing ...
swp5 link phy health counters cleared.
swp7 link phy health counters cleared.
Action executing ...
swp8 link phy health counters cleared.
swp9 link phy health counters cleared.
swp10 link phy health counters cleared.
```

If the specified interface is out of range; for example, if the switch supports up to 32 switch ports but you try to clear swp33, NVUE displays an error.

{{%notice note%}}
The `nv action clear interface <interface-id> link phy health` command does not clear counters in the hardware.
{{%/notice%}}

## Reset a Transceiver

NVUE provides a command to reset a specific transceiver to its initial, stable state without having to be present physically in the data center to pull the transceiver.

The following example resets the transceiver in swp1:

```
cumulus@switch:~$ nv action reset platform transceiver swp1 
Action executing ... 
Resetting module swp1 ... OK 
Action succeeded 
```

The following example resets a range of transceivers:

```
cumulus@switch:~$ nv action reset platform transceiver swp1-3 
Action executing ... 
Resetting module swp1 ... OK 
Action executing ... 
Resetting module swp2 ... OK 
Action executing ... 
Resetting module swp3 ... OK 
Action succeeded 
```

The following example resets the transceiver in swp5 and swp7:

```
cumulus@switch:~$ nv action reset platform transceiver swp5,swp7 
Action executing ... 
Resetting module swp5 ... OK 
Action executing ... 
Resetting module swp7 ... OK 
Action executing ... 
Action succeeded 
```

When the reset completes successfully, you see syslog messages similar to the following:

```
2024-12-06T07:12:37.996339+00:00 cumulus nvue-port-reset: The module reset was successfully completed on swp1
```

{{%notice note%}}
- To reset a transceiver on a split port, specify the parent port; for example, to reset swp1s0, run the `nv action reset platform transceiver swp1` command.
- If a cable is faulty, the `nv action reset platform transceiver <transceiver-id` command completes successfully, but the details of the transceiver do not show until you resolve the issue or reboot the system if necessary,
{{%/notice%}}

## Transceiver Thermal Control

To optimize transceiver thermal performance and maintain a cooler operating environment before reaching critical temperatures, you can set temperature thresholds for fan activation in the FAN algorithm,
ensuring that they are below the module's high warning threshold.

Lowering the thresholds leads to earlier and more frequent fan operation, increasing power usage and noise but protecting hardware performance and lifespan.

Setting the temperature thresholds does not change the module EEPROM-based alarm thresholds. The optical module continues reporting temperature alarms based on alarms or warning thresholds preprogrammed in the transceiver EEPROM.

{{%notice warning%}}
Setting the temperature thresholds without proper guidance can result in transceiver damage, and might void your warranty and support agreements. This is an advanced configuration task; NVIDIA recommends you use the default transceiver temperature settings. Only modify this setting with approval from NVIDIA Technical Support.
{{%/notice%}}

{{%notice note%}}
- You can set temperature thresholds on the SN5610 switch only.
- Always use the parent transceiver name for configuration; for example, use swp1 not swp1s0.
{{%/notice%}}

To set the temperature threshold for a single port, run the `nv set platform transceiver <transceiver-id> temperature setpoint` command. You can set a value between 30 and 80. The temperature threshold for an interface must be below the module advertised high warning threshold. If you configure the setpoint to be above the module advertised high temperature warning threshold, the FAN algorithm uses the module advertised threshold.

```
cumulus@switch:~$ nv set platform transceiver swp2 temperature setpoint 60 
cumulus@switch:~$ nv config apply
```

To set the temperature threshold for a group of ports:

```
cumulus@switch:~$ nv set platform transceiver swp2-10 temperature setpoint 60 
cumulus@switch:~$ nv config apply
```

To set the temperature threshold for a group of comma-separated ports:

```
cumulus@switch:~$ nv set platform transceiver swp1,4,5,30 temperature setpoint 65
cumulus@switch:~$ nv config apply
```

{{%notice note%}}
- When you set the temperature threshold, the hardware management service (`hw-managament-tc.service`) and `switchd` restart.
- If you try to set the temperature threshold above the module advertised high temperature warning or if the module is not DOM capable, Cumulus Linux reports an invalid configuration warning.
{{%/notice%}}

To unset the temperature threshold and return to the default value, run the `nv unset platform transceiver <transceiver-id> temperature setpoint` command.

{{%notice info%}}
If you run the `nv unset platform` command, the switch clears out the temperature setpoints for all ports.
{{%/notice%}}

To verify the temperature threshold configuration for a port, run the `nv show platform transceiver <transceiver-id> temperature` command:

```
cumulus@switch:~$ nv show platform transceiver swp1 temperature 
          operational  applied 
--------  -----------  ------- 
setpoint  60           60 
```

The `nv show platform transceiver <transceiver-id>` command also shows the temperature threshold for the specified port. See below.

## Show Transceiver Information

To show the identifier, vendor name, part number, serial number, and revision for all modules, run the `nv show platform transceiver` command:

```
cumulus@switch:~$ nv show platform transceiver 
Transceiver  Identifier  Vendor name  Vendor PN         Vendor SN      Vendor revision
-----------  ----------  -----------  ----------------  -------------  --------------- 
swp1         QSFP28      Mellanox     MCP1600-C001E30N  MT2039VB01185  A3 
swp10        QSFP28      Mellanox     MCP1600-C001E30N  MT2211VS01792  A3 
swp11        QSFP28      Mellanox     MCP1600-C001E30N  MT2211VS01792  A3 
swp12        QSFP28      Mellanox     MCP1650-V00AE30   MT2122VB02220  A2 
swp13        QSFP28      Mellanox     MCP1650-V00AE30   MT2122VB02220  A2 
swp14        QSFP-DD     Mellanox     MCP1660-W00AE30   MT2121VS01645  A3 
swp15        QSFP-DD     Mellanox     MCP1660-W00AE30   MT2121VS01645  A3 
swp18        QSFP28      Mellanox     MCP1600-C001E30N  MT2211VS01967  A3 
swp20        QSFP28      Mellanox     MFA1A00-C003      MT2108FT02204  B2 
swp21        QSFP28      Mellanox     MFA1A00-C003      MT2108FT02204  B2 
swp22        QSFP28      Mellanox     MFA1A00-C003      MT2108FT02194  B2 
swp23        QSFP28      Mellanox     MFA1A00-C003      MT2108FT02194  B2 
swp31        QSFP28      Mellanox     MCP1600-C001E30N  MT2039VB01191  A3 
```

To show a detailed view of module information for all ports that includes cable length, type, and diagnostics, current status and error status, run the `nv show platform transceiver details` command.

To show hardware capabilities and measurement information on the module in a particular port, run the `nv show platform transceiver <transceiver-id>` command:

```
cumulus@switch:~$ nv show platform transceiver swp2
cable-type             : Active cable 
cable-length           : 3m 
supported-cable-length : 0m om1, 0m om2, 0m om3, 3m om4, 0m om5 
diagnostics-status     : Diagnostic Data Available 
status                 : plugged_enabled 
error-status           : N/A 
vendor-date-code       : 210215__ 
identifier             : QSFP28 
vendor-rev             : B2 
vendor-name            : Mellanox 
vendor-pn              : MFA1A00-C003 
vendor-sn              : MT2108FT02204 
temperature: 
  temperature           : 42.56 C 
  high-alarm-threshold  : 80.00 C 
  low-alarm-threshold   : -10.00 C 
  high-warning-threshold: 70.00 C 
  low-warning-threshold : 0.00 C
  temperature-setpoint  : 60.00 C
  alarm                 : Off 
voltage: 
  voltage               : 3.2862 V 
  high-alarm-threshold  : 3.5000 V 
  low-alarm-threshold   : 3.1000 V 
  high-warning-threshold: 3.4650 V 
  low-warning-threshold : 3.1350 V
  alarm                 : Off 
channel: 
  channel-1: 
    rx-power: 
        power                 : 0.8625 mW / -0.64 dBm 
        high-alarm-threshold  : 5.40 dBm 
        low-alarm-threshold   : -13.31 dBm 
        high-warning-threshold: 2.40 dBm 
        low-warning-threshold : -10.30 dBm 
        alarm                 : Off 
    tx-power: 
        power                 : 0.8988 mW / -0.46 dBm 
        high-alarm-threshold  : 5.40 dBm 
        low-alarm-threshold   : -11.40 dBm 
        high-warning-threshold: 2.40 dBm 
        low-warning-threshold : -8.40 dBm 
        alarm                 : Off 
    tx-bias-current: 
        current               : 6.750 mA 
        high-alarm-threshold  : 8.500 mA 
        low-alarm-threshold   : 5.492 mA 
        high-warning-threshold: 8.000 mA 
        low-warning-threshold : 6.000 mA 
        alarm                 : Off
...  
```

{{%notice note%}}
- The `nv show platform transceiver` commands show information for front panel physical ports only (for example swp1). The commands do not show information for logical ports, such as SVIs, bonds, or eth0.
- To show information for subinterfaces; run the `nv show interface <subinterface> transceiver` commands.
{{%/notice%}}

You can also show transceiver data in a more condensed format with the `nv show interface <interface-id> transceiver` command:

```
cumulus@switch:~$ nv show interface swp1 transceiver
cable-type             : Active cable 
cable-length           : 3m 
supported-cable-length : 0m om1, 0m om2, 0m om3, 3m om4, 0m om5 
diagnostics-status     : Diagnostic Data Available 
status                 : plugged_enabled 
error-status           : N/A 
revision-compliance    : SFF-8636 Rev 2.5/2.6/2.7 
vendor-date-code       : 210215__ 
identifier             : QSFP28 
vendor-rev             : B2 
vendor-oui             : 00:02:c9 
vendor-name            : Mellanox 
vendor-pn              : MFA1A00-C003 
vendor-sn              : MT2108FT02204 
temperature            : 42.56 degrees C / 108.61 degrees F 
voltage                : 3.2888 V 
ch-1-rx-power          : 0.8625 mW / -0.64 dBm 
ch-1-tx-power          : 0.8988 mW / -0.46 dBm 
ch-1-tx-bias-current   : 6.750 mA 
ch-2-rx-power          : 0.8385 mW / -0.76 dBm 
ch-2-tx-power          : 0.9154 mW / -0.38 dBm 
ch-2-tx-bias-current   : 6.750 mA 
ch-3-rx-power          : 0.8556 mW / -0.68 dBm 
ch-3-tx-power          : 0.9537 mW / -0.21 dBm 
ch-3-tx-bias-current   : 6.750 mA 
ch-4-rx-power          : 0.8576 mW / -0.67 dBm 
ch-4-tx-power          : 0.9695 mW / -0.13 dBm 
ch-4-tx-bias-current   : 6.750 mA 
```

To show channel information for the module in a particular port, run the `nv show platform transceiver <transceiver-id> channel` command. To show specific channel information for the module in a particular port, run the `nv show platform transceiver <transceiver-id> channel <channel-id>` command.

```
cumulus@switch:~$ nv show platform transceiver swp25 channel 
channel: 
  channel-1: 
    rx-power: 
        power                 : 0.8625 mW / -0.64 dBm 
        high-alarm-threshold  : 5.40 dBm 
        low-alarm-threshold   : -13.31 dBm 
        high-warning-threshold: 2.40 dBm 
        low-warning-threshold : -10.30 dBm 
        alarm                 : Off 
    tx-power: 
        power                 : 0.8988 mW / -0.46 dBm 
        high-alarm-threshold  : 5.40 dBm 
        low-alarm-threshold   : -11.40 dBm 
        high-warning-threshold: 2.40 dBm 
        low-warning-threshold : -8.40 dBm 
        alarm                 : Off 
    tx-bias-current: 
        current               : 6.750 mA 
        high-alarm-threshold  : 8.500 mA 
        low-alarm-threshold   : 5.492 mA 
        high-warning-threshold: 8.000 mA 
        low-warning-threshold : 6.000 mA 
        alarm                 : Off 
  channel-2: 
    rx-power: 
        power                 : 0.8385 mW / -0.76 dBm 
        high-alarm-threshold  : 5.40 dBm 
        low-alarm-threshold   : -13.31 dBm 
        high-warning-threshold: 2.40 dBm 
        low-warning-threshold : -10.30 dBm 
        alarm                 : Off 
    tx-power: 
        power                 : 0.9154 mW / -0.38 dBm 
        high-alarm-threshold  : 5.40 dBm 
        low-alarm-threshold   : -11.40 dBm 
        high-warning-threshold: 2.40 dBm 
        low-warning-threshold : -8.40 dBm 
        alarm                 : Off
...
```

To show the thresholds for the module for a specific interface, run the `nv show interface <interface-id> transceiver thresholds` command:

```
cumulus@switch:~$ nv show interface swp3 transceiver thresholds
                     Ch    Value          High Alarm       High Warn        Low Warn       Low Alarm       Alt Value 
                                          Threshold        Threshold       Threshold       Threshold 
------------------------------------------------------------------------------------------------------------------------ 
temperature          -     42.74 C         80.00 C         70.00 C         0.00 C          -10.00 C        108.94F 
voltage              -     3.2862 V        3.5000 V        3.4650 V        3.1350 V        3.1000 V 
rx-power             1     -0.64 dBm       5.40 dBm        2.40 dBm        -10.30 dBm      -13.31 dBm      0.8625 mW 
                     2     -0.70 dBm       5.40 dBm        2.40 dBm        -10.30 dBm      -13.31 dBm      0.8514 mW 
                     3     -0.68 dBm       5.40 dBm        2.40 dBm        -10.30 dBm      -13.31 dBm      0.8556 mW 
                     4     -0.60 dBm       5.40 dBm        2.40 dBm        -10.30 dBm      -13.31 dBm      0.8704 mW 
tx-power             1     -0.48 dBm       5.40 dBm        2.40 dBm        -8.40 dBm       -11.40 dBm      0.8963 mW 
                     2     -0.38 dBm       5.40 dBm        2.40 dBm        -8.40 dBm       -11.40 dBm      0.9154 mW 
                     3     -0.19 dBm       5.40 dBm        2.40 dBm        -8.40 dBm       -11.40 dBm      0.9562 mW 
                     4     -0.13 dBm       5.40 dBm        2.40 dBm        -8.40 dBm       -11.40 dBm      0.9695 mW 
tx-bias-current      1     6.750 mA        8.500 mA        8.000 mA        6.000 mA        5.492 mA 
                     2     6.750 mA        8.500 mA        8.000 mA        6.000 mA        5.492 mA 
                     3     6.750 mA        8.500 mA        8.000 mA        6.000 mA        5.492 mA 
                     4     6.750 mA        8.500 mA        8.000 mA        6.000 mA        5.492 mA 
```
