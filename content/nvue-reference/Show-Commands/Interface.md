---
title: Interface
author: Cumulus Networks
weight: 190

type: nojsscroll
---
<style>
h { color: RGB(118,185,0)}
</style>
<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show interface</h>

Shows information about all the interfaces on the switch, such as the name, type (swp, bond, vrf, and so on), state (up or down), speed, MTU, remote host and remote port, and IP address.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show interface
Interface   State  Speed  MTU    Type      Remote Host      Remote Port      Summary         
----------  -----  -----  -----  --------  ---------------  --------------…  ---------------…
BLUE        up            65575  vrf                                         IP Address:     
                                                                             127.0.0.1/8     
                                                                             IP Address:     
                                                                             ::1/128         
RED         up            65575  vrf                                         IP Address:     
                                                                             127.0.0.1/8     
                                                                             IP Address:     
                                                                             ::1/128         
bond1       up     1G     9000   bond                                                        
bond2       up     1G     9000   bond                                                        
bond3       up     1G     9000   bond                                                        
br_default  up            9216   bridge                                                      
br_l3vni    up            9216   bridge                                                      
eth0        up     1G     1500   eth       oob-mgmt-switch  swp10            IP Address:     
                                                                             192.168.200.11/…
lo          up            65536  loopback                                    IP Address:     
                                                                             10.10.10.1/32   
                                                                             IP Address:     
                                                                             127.0.0.1/8     
                                                                             IP Address:     
                                                                             ::1/128         
mgmt        up            65575  vrf                                         IP Address:     
                                                                             127.0.0.1/8     
                                                                             IP Address:     
                                                                             ::1/128         
swp1        up     1G     9000   swp       server01         48:b0:2d:bc:2e…                  
swp2        up     1G     9000   swp       server02         48:b0:2d:36:9e…                  
swp3        up     1G     9000   swp       server03         48:b0:2d:09:b9…                  
swp4        down          1500   swp                                                         
swp5        down          1500   swp                                                         
swp6        up     1G     9216   swp                                                        
...
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show interface \<interface-id\></h>

Shows the configuration information for the specified interface.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<interface-id>` | The interface name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show interface swp1
                          operational        applied  pending
------------------------  -----------------  -------  -------
type                      swp                swp      swp    
[acl]                                                        
evpn                                                         
  multihoming                                                
    uplink                                   off      off    
lldp                                                         
  dcbx-ets-config-tlv     off                                
  dcbx-ets-recomm-tlv     off                                
  dcbx-pfc-tlv            off                                
  [neighbor]              server01                           
ptp                                                          
  enable                                     off      off    
router                                                       
  adaptive-routing                                           
    enable                                   off      off    
  ospf                                                       
    enable                                   off      off    
  ospf6                                                      
    enable                                   off      off    
  pbr                                                        
    [map]                                                    
  pim                                                        
    enable                                   off      off    
synce                                                        
  enable                                     off      off
...
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show interface \<interface-id\> bond</h>

Shows the bond member configuration for the specified interface.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<interface-id>` | The interface name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show interface swp1 bond
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show interface \<interface-id\> bond member</h>

Shows the bond members for the specified interface.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<interface-id>` | The interface name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show interface swp1 bond member
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show interface \<interface-id\> bond member \<member-id\></h>

Shows specific bond member configuration for the specified interface.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<interface-id>` | The interface name. |
| `<member-id>` | The bond name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show interface swp1 bond member bond1
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show interface \<interface\> counters</h>

Shows all counters for a specific interface, such as packet drop, error, and distribution counts.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<interface-id>` | The interface name. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv show interface swp1 counters
                     operational  applied  pending
-------------------  -----------  -------  -------
carrier-transitions  6                            

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

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show interface \<interface\> counters drops</h>

Shows packet drop counters for a specific interface.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<interface-id>` | The interface name. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv show interface swp1 counters drops
Counter          Receive  Transmit
---------------  -------  --------
ACL Drops        0        n/a     
Buffer Drops     0        n/a
Non-Queue Drops  n/a      0       
Queue Drops      n/a      0       
Total Drops      0        0
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show interface \<interface\> counters errors</h>

Shows error counters for a specific interface.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<interface-id>` | The interface name. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv show interface swp1 counters errors
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

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show interface \<interface\> counters pktdist</h>

Shows packet distribution counters for a specific interface.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<interface-id>` | The interface name. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv show interface swp1 counters pktdist
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
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show interface \<interface-id\> ip</h>

Shows the IP configuration for the specified interface.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<interface-id>` | The interface name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show interface swp1 ip
                        operational  applied  pending
----------------------  -----------  -------  -------
igmp                                                 
  enable                             off      off    
ipv4                                                 
  forward                            on       on     
ipv6                                                 
  enable                             on       on     
  forward                            on       on     
neighbor-discovery                                   
  enable                             on       on     
  [dnssl]                                            
  home-agent                                         
    enable                           off      off    
  [prefix]                                           
  [rdnss]                                            
  router-advertisement                               
    enable                           off      off    
vrrp                                                 
  enable                             off      off    
vrf                                  default  default
[gateway]
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show interface \<interface-id\> ip address</h>

Shows the IP addresses configured for the specified interface.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<interface-id>` | The interface name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show interface lo ip address

-------------
10.10.10.1/32
127.0.0.1/8  
::1/128  
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show interface \<interface-id\> ip address \<ip-prefix-id\></h>

Shows details about a specific IP address for the specified interface.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<interface-id>` | The interface name.|
| `<ip-prefix-id>`  | The IPv4 or IPv6 address and route prefix in CIDR notation.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show interface lo ip address 10.10.10.1/32
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show interface \<interface-id\> ip gateway</h>

Shows the gateway IP address for the specified interface.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<interface-id>` | The interface name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show interface swp1 ip gateway
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show interface \<interface-id\> ip gateway \<ip-address-id\></h>

Shows information about a specific gateway IP address for the specified interface

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<interface-id>` | The interface name. |
| `<ip-address-id>` | The gateway IP address. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show interface swp1 ip gateway 10.10.10.1
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show interface \<interface-id\> ip ipv4</h>

Shows IPv4 information for the specified interface.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<interface-id>` | The interface name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show interface swp1 ip ipv4
         operational  applied  pending
-------  -----------  -------  -------
forward               on       on
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show interface \<interface-id\> ip ipv6</h>

Shows IPv6 information for the specified interface.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<interface-id>` | The interface name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show interface swp1 ip ipv6
        operational  applied  pending
-------  -----------  -------  -------
enable                on       on     
forward               on       on
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show interface \<interface-id\> ip neighbor</h>

Shows information about the IP neighbors configured for the specified interface.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<interface-id>` | The interface name.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show interface swp51 ip neighbor
        operational                applied  pending
------  -------------------------  -------  -------
[ipv4]  169.254.0.1                                
[ipv6]  fe80::4ab0:2dff:fe08:9898
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show interface \<interface-id\> ip neighbor ipv4</h>

Shows the IPv4 neighbors for the specified interface.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<interface-id>` | The interface name.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show interface swp51 ip neighbor ipv4
             lladdr             state    
-----------  -----------------  ---------
169.254.0.1  48:b0:2d:08:98:98  permanent
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show interface \<interface-id\> ip neighbor ipv4 \<neighbor-id\></h>

Shows information about a specific IPv4 neighbor for the specified interface.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<interface-id>` | The interface name.|
| `<neighbor-id>`  | The IPv4 address of the neighbor.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show interface swp51 ip neighbor ipv4 169.254.0.1
        operational        applied  pending
------  -----------------  -------  -------
lladdr  48:b0:2d:08:98:98                  
state   permanent
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show interface \<interface-id\> ip neighbor ipv6</h>

Shows the IPv6 neighbors for the specified interface.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<interface-id>` | The interface name.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show interface swp51 ip neighbor ipv6
                           lladdr             state    
-------------------------  -----------------  ---------
fe80::4ab0:2dff:fe08:9898  48:b0:2d:08:98:98  reachable
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show interface \<interface-id\> ip neighbor ipv6 \<neighbor-id\></h>

Shows information about a specific IPv6 neighbor for the specified interface.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<interface-id>` | The interface name.|
| `<neighbor-id>`  | The IPv4 address of the neighbor.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show interface swp51 ip neighbor ipv6 fe80::4ab0:2dff:fe08:9898
        operational        applied  pending
------  -----------------  -------  -------
lladdr  48:b0:2d:08:98:98                  
state   reachable
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show interface \<interface-id\> link</h>

Shows configuration and statistics for the specified interface.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<interface-id>`  | The interface name.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show interface swp1 link
                       operational        applied  pending
---------------------  -----------------  -------  -------
auto-negotiate         off                on       on     
duplex                 full               full     full   
speed                  1G                 auto     auto   
fec                                       auto     auto   
mtu                    9000               9216     9216   
[breakout]                                                
state                  up                 up       up     
stats                                                     
  carrier-transitions  6                                  
  in-bytes             39.21 MB                           
  in-drops             0                                  
  in-errors            0                                  
  in-pkts              324461                             
  out-bytes            48.50 MB                           
  out-drops            0                                  
  out-errors           0                                  
  out-pkts             501807                             
mac                    48:b0:2d:6c:72:a0
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show interface \<interface-id\> link breakout</h>

Shows the port breakouts for the specified interface.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<interface-id>` | The interface name.|

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@switch:~$ nv show interface swp1 link breakout
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show interface \<interface-id\> link breakout \<mode-id\></h>

Shows information about a specific port breakout for the specified interface.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<interface-id>` | The interface name.|
| `<mode-id>` |  The breakout mode identifier: 1x, 2x, 4x, 8x, disabled, or loopback. |

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@switch:~$ nv show interface swp1 link breakout 2x
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show interface \<interface-id\> link flag</h>

Shows link flags for the specified interface.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<interface-id>` | The interface name.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show interface swp1 link flag
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set interface \<interface-id\> link phy-detail</h>

Shows physical layer information, such the error counters for each lane on a port.

{{%notice note%}}
Switches with the Spectrum 1 ASIC do not support the `nv show interface <interface> link phy-detail` command.
{{%/notice%}}

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
|`<interface-id>` |  The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.10.0

### Example

```
cumulus@switch:~$ nv show interface swp1 link phy-detail 
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

## <h>nv set interface \<interface-id\> link phy-diag</h>

Shows physical layer diagnostic information for a port.

{{%notice note%}}
Switches with the Spectrum 1 ASIC do not support the `nv show interface <interface> link phy-diag` command.
{{%/notice%}}

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
|`<interface-id>` |  The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.10.0

### Example

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

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show interface \<interface-id\> link protodown-reason</h>

Shows the link protodown reason details for an interface.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<interface-id>` | The interface name.|

### Version History

Introduced in Cumulus Linux 5.9.0

### Example

```
cumulus@switch:~$ nv show interface swp1 link protodown-reason
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show interface \<interface-id\> link state</h>

Shows the state of the specified interface; if the link is up or down.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<interface-id>` | The interface name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show interface swp1 link state
operational  applied  pending
  -----------  -------  -------
  up           up       up
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show interface \<interface-id\> link stats</h>

Shows statistics for the specified interface, such as packet size, packet drops, and packet errors.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<interface-id>` | The interface name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show interface swp1 link stats
                     operational  applied  pending
-------------------  -----------  -------  -------
carrier-transitions  6                            
in-bytes             39.22 MB                     
in-drops             0                            
in-errors            0                            
in-pkts              324557                       
out-bytes            48.51 MB                     
out-drops            0                            
out-errors           0                            
out-pkts             501951
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show interface \<interface-id\> link traffic-engineering</h>

Shows traffic engineering statistics for the specified interface.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<interface-id>` | The interface name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show interface swp1 link traffic-engineering
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show interface \<interface-id\> pluggable</h>

Shows the <span class="a-tooltip">[SFP](## "Small Form-Factor Pluggable")</span> module information for the specified interface.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<interface-id>` | The interface name. |

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv show interface swp1 pluggable
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show interface \<interface-id\> storm-control</h>

Shows storm control configuration settings for the specified interface.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<interface-id>` | The interface name. |

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv show interface swp1 storm-control
                 applied
---------------  -------
broadcast        400    
multicast        3000   
unknown-unicast  2000
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show interface \<interface-id\> tunnel</h>

Shows tunnel information for the specified interface.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<interface-id>` | The interface name. |

### Version History

Introduced in Cumulus Linux 5.1.0

### Example

```
cumulus@switch:~$ nv show interface swp1 tunnel
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show interface --view=counters</h>

Shows all statistics for all the interfaces configured on the switch.

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv show interface --view=counters
Interface   MTU    RX_OK   RX_ERR  RX_DRP  RX_OVR  TX_OK   TX_ERR  TX_DRP  TX_OVR  Flg  
----------  -----  ------  ------  ------  ------  ------  ------  ------  ------  -----
BLUE        65575  0       0       0       0       0       0       1197    0       OmRU 
RED         65575  0       0       0       0       0       0       1197    0       OmRU 
bond1       9000   324612  0       0       0       502040  0       0       0       BMmRU
bond2       9000   330788  0       0       0       499929  0       0       0       BMmRU
bond3       9000   324604  0       0       0       499590  0       0       0       BMmRU
br_default  9216   44391   0       0       0       40362   0       0       0       BMRU 
br_l3vni    9216   0       0       0       0       7253    0       0       0       BMRU 
eth0        1500   214911  0       0       0       29286   0       0       0       BMRU 
lo          65536  227368  0       0       0       227368  0       0       0       LRU  
mgmt        65575  31690   0       0       0       0       0       1197    0       OmRU 
swp1        9000   324616  0       0       0       502040  0       0       0       BMsRU
swp2        9000   330792  0       0       0       499929  0       0       0       BMsRU
swp3        9000   324608  0       0       0       499590  0       0       0       BMsRU
swp6        9216   0       0       0       0       97832   0       0       0       BMRU 
swp7        9216   0       0       0       0       97832   0       0       0       BMRU 
swp51       9216   273647  0       10793   0       274422  0       0       0       BMRU 
swp52       9216   249220  0       10793   0       262843  0       0       0       BMRU 
vlan10      9216   13482   0       80      0       14416   0       0       0       BMRU 
vlan10-v0   9216   300     0       80      0       7090    0       0       0       BMRU 
vlan20      9216   20409   0       50      0       11355   0       0       0       BMRU 
vlan20-v0   9216   275     0       50      0       5894    0       0       0       BMRU 
vlan30      9216   11700   0       50      0       12033   0       0       0       BMRU 
vlan30-v0   9216   226     0       50      0       5894    0       0       0       BMRU 
vlan220_l3  9216   0       0       0       0       2420    0       0       0       BMRU 
vlan297_l3  9216   0       0       0       0       2420    0       0       0       BMRU 
vxlan48     9216   27342   0       0       0       25891   40829   51      0       BMRU 
vxlan99     9216   0       0       0       0       0       0       4800    0       BMRU
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system link</h>

Show global link configuration.

### Version History

Introduced in Cumulus Linux 5.7.0

### Example

```
cumulus@switch:~$ nv show system link
                 applied
---------------  -------
flap-protection         
  threshold      5      
  interval       10
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system link flap-protection</h>

Shows the link flap protection threshold and interval configuration settings.

### Version History

Introduced in Cumulus Linux 5.7.0

### Example

```
cumulus@switch:~$ nv show system link flap-protection
           applied
---------  -------
threshold  8      
interval   30
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> loopback</h>

Shows the loopback interfaces associated with this VRF.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show vrf default loopback
             operational    applied      pending    
-----------  -------------  -----------  -----------
ip                                                  
  [address]  10.10.10.1/32                          
  [address]  127.0.0.1/8    127.0.0.1/8  127.0.0.1/8
  [address]  ::1/128        ::1/128      ::1/128
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> loopback ip</h>

Shows the IP addresses associated with the loopback interface for the specified VRF.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show vrf default loopback ip
           operational    applied      pending    
---------  -------------  -----------  -----------
[address]  10.10.10.1/32                          
[address]  127.0.0.1/8    127.0.0.1/8  127.0.0.1/8
[address]  ::1/128        ::1/128      ::1/128
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> loopback ip address \<ip-prefix-id\></h>

Shows details about the specified loopback IP address for the specified VRF.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |
| `<ip-prefix-id>` | The IPv4 or IPv6 address and route prefix in CIDR notation. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show vrf default loopback ip address 10.10.10.1/32
```
