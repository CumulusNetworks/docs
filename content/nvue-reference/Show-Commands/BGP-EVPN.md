---
title: BGP EVPN
author: Cumulus Networks
weight: 134
type: nojsscroll

---
<style>
h { color: RGB(118,185,0)}
</style>

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show evpn</h>

Shows EVPN configuration.

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@switch:~$ nv show evpn
                       operational   applied
---------------------  ------------  -------------
enable                               on
route-advertise
  nexthop-setting                    system-ip-mac
  svi-ip               off           off
  default-gateway      off           off
dad
  enable               on            on
  mac-move-threshold   5             5
  move-window          180           180
  duplicate-action     warning-only  warning-only
[vni]
multihoming
  enable                             off
  mac-holdtime         1080
  neighbor-holdtime    1080
  startup-delay        180
  startup-delay-timer  --:--:--
  uplink-count         0
  uplink-active        0
l2vni-count            3
l3vni-count            2
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show evpn access-vlan-info vlan</h>

Shows EVPN access VLAN information.

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@switch:~$ nv show evpn access-vlan-info vlan
Id    MemberCnt  Vni  VniCnt  VxlanIntf  MemberIntf
----  ---------  ---  ------  ---------  ----------
1     1                                  peerlink
10    2          10   1       vxlan48    bond1
                                         peerlink
20    2          20   1       vxlan48    bond2
                                         peerlink
30    2          30   1       vxlan48    bond3
                                         peerlink
4006                  1       vxlan48
4063                  1       vxlan48
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show evpn access-vlan-info vlan \<vlan-id\></h>

Shows EVPN access information for a specific VLAN.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vni-id>` |   The VNI name.|

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@switch:~$ nv show evpn access-vlan-info vlan 10
                        operational
----------------------  -----------
vxlan-interface         vxlan48
vni                     10
member-interface-count  2
vni-count               1

member-interface
===================

    --------
    bond1
    peerlink
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show evpn access-vlan-info vlan \<vlan-id\> member-interface</h>

Shows EVPN access VLAN member interface information.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vni-id>` |   The VNI name.|

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@switch:~$ nv show evpn access-vlan-info vlan 10 member-interface
--------
bond1
peerlink
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show evpn dad</h>

Shows duplicate address detection configuration information.

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@switch:~$ nv show evpn dad
                    operational   applied
------------------  ------------  ------------
enable              on            on
mac-move-threshold  5             5
move-window         180           180
duplicate-action    warning-only  warning-only
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show evpn dad duplicate-action</h>

Shows duplicate address detection action configuration.

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@switch:~$ nv show evpn dad duplicate-action
operational   applied
------------  ------------
warning-only  warning-only
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show evpn dad duplicate-action freeze</h>

Shows duplicate address detection freeze option information.

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@switch:~$ nv show evpn dad duplicate-action freeze
No Data
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show evpn l2-nhg</h>

Shows EVPN next hop group information.

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@switch:~$ nv show evpn l2-nhg
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show evpn l2-nhg vtep-ip</h>

Shows EVPN next hop group VTEP IP address information.

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@switch:~$ nv show evpn l2-nhg vtep-ip
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show evpn l2-nhg vtep-ip \<ip-address\></h>

Shows EVPN next hop group VTEP IP address information.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<ip-address>` |   The IP address of the VTEP.|

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@switch:~$ nv show evpn l2-nhg vtep-ip 10.10.10.3
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show evpn multihoming</h>

Shows global EVPN-MH information, such as the uplink count, startup delay timer, neighbor hold time, and MAC entry hold time.

### Version History

Introduced in Cumulus Linux 5.8.0

### Example

```
cumulus@switch:~$ nv show evpn multihoming
                     operational  applied
-------------------  -----------  -------
enable                            off
mac-holdtime         1080
neighbor-holdtime    1080
startup-delay        180
startup-delay-timer  --:--:--
uplink-count         0
uplink-active        0
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show evpn multihoming bgp-info</h>

Shows EVPN multihoming BGP information.

### Version History

Introduced in Cumulus Linux 5.8.0

### Example

```
cumulus@switch:~$ nv show evpn multihoming bgp-info
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show evpn multihoming bgp-info esi</h>

Shows the Ethernet segments across all VNIs learned through type-1 and type-4 routes.

### Version History

Introduced in Cumulus Linux 5.8.0

### Example

```
cumulus@switch:~$ nv show evpn multihoming bgp-info esi
SrcIP - Originator IP, VNICnt - VNI Count, VRFCnt - VRF Count, MACIPCnt - MAC IP
path count, MacGlblCnt - Mac global count, VTEP - Remote VTEP ID, FragID -
Fragments ID
ESI                            RD            SrcIP       VNICnt  VRFCnt  MACIPCnt  MacGlblCnt  Local  Remote  VTEP        FragID
-----------------------------  ------------  ----------  ------  ------  --------  ----------  -----  ------  ----------  ------------
03:44:38:39:FF:00:aa:00:00:01  10.10.10.1:3  10.10.10.1  1       1       3   6           yes    yes     10.10.10.2  10.10.10.1:3
03:44:38:39:FF:00:aa:00:00:02  10.10.10.1:4  10.10.10.1  1       1       2   4           yes    yes     10.10.10.2  10.10.10.1:4
03:44:38:39:FF:00:aa:00:00:03  10.10.10.1:5  10.10.10.1  1       1       2   4           yes    yes     10.10.10.2  10.10.10.1:5
03:44:38:39:FF:00:bb:00:00:01                0.0.0.0     1       1       0   12                 yes     10.10.10.3
                              10.10.10.4
03:44:38:39:FF:00:bb:00:00:02                0.0.0.0     1       1       0   0                  yes
03:44:38:39:FF:00:bb:00:00:03                0.0.0.0     1       1       0   0
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show evpn multihoming ead-evi-route</h>

Shows EVPN multihoming ead-evi-route information.

### Version History

Introduced in Cumulus Linux 5.8.0

### Example

```
cumulus@switch:~$ nv show evpn multihoming ead-evi-route
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show evpn multihoming segment</h>

Shows EVPN multihoming segment information.

### Version History

Introduced in Cumulus Linux 5.8.0

### Example

```
cumulus@switch:~$ nv show evpn multihoming segment
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show evpn vni</h>

Shows EVPN VNI information.

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@switch:~$ nv show evpn vni
NumMacs - Number of MACs (local and remote) known for this VNI, NumArps - Number
of ARPs (IPv4 and IPv6, local and remote) known for this VNI
, NumRemVteps - Number of Remote Vteps, Bridge - Bridge to which the vni
belongs, Vlan - VLAN assoicated to MAC

VNI  NumMacs  NumArps  NumRemVteps  TenantVrf  Bridge      Vlan
---  -------  -------  -----------  ---------  ----------  ----
10   7        2        1            RED        br_default  10
20   7        2        1            RED        br_default  20
30   7        2        1            BLUE       br_default  30
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show evpn vni \<vni-id\></h>

Shows configuration information for a specific VNI.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vni-id>` |   The VNI name.|

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@switch:~$ v show evpn vni 10
                   operational  applied
-----------------  -----------  -------
route-advertise
  svi-ip           off
  default-gateway  off
[remote-vtep]      10.0.1.34
vlan               10
bridge-domain      br_default
tenant-vrf         RED
vxlan-interface    vxlan48
mac-count          7
host-count         2
remote-vtep-count  1
local-vtep         10.0.1.12
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show evpn vni \<vni-id\> bgp-info</h>

Shows BGP information for the specified EVPN VNI.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vni-id>` |   The VNI name.|

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@switch:~$ nv show evpn vni 10 bgp-info
                           operational 
-------------------------  ------------
rd                         10.10.10.1:6
local-vtep                 10.0.1.12   
advertise-svi-ip           off         
advertise-default-gateway  off         
in-kernel                  on          
type                       L2          
mac-vrf-soo                            
[import-route-target]      65101:10    
[export-route-target]      65101:10
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show evpn vni \<vni-id\> host</h>

Shows host information for the specified EVPN VNI.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vni-id>` |   The VNI name.|

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@switch:~$ nv show evpn vni 10 host

LocMobSeq - local mobility sequence, RemMobSeq - remote mobility sequence, Esi -
Remote Esi

IP address                 Type    State   LocMobSeq  RemMobSeq  Mac                Esi
-------------------------  ------  ------  ---------  ---------  -----------------  ---
fe80::4ab0:2dff:fe65:d4af  remote  active  0          0          48:b0:2d:65:d4:af
fe80::4ab0:2dff:fed9:2d2d  local   active  0          0          48:b0:2d:d9:2d:2d
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show evpn vni \<vni-id\> mac</h>

Shows MAC address information for the specified EVPN VNI.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vni-id>` |   The VNI name.|

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@switch:~$ nv show evpn vni 10 mac
LocMobSeq - local mobility sequence, RemMobSeq - remote mobility sequence,
RemoteVtep - Remote Vtep address, Esi - Remote Esi

MAC address        Type    LocMobSeq  RemMobSeq  Interface  RemoteVtep  Esi
-----------------  ------  ---------  ---------  ---------  ----------  ---
44:38:39:22:01:7a  local   0          0          peerlink
44:38:39:22:01:8a  remote  0          0                     10.0.1.34
44:38:39:22:01:84  remote  0          0                     10.0.1.34
48:b0:2d:65:d4:af  remote  1          0                     10.0.1.34
48:b0:2d:72:90:d7  local   0          0          bond1
48:b0:2d:a0:8d:de  remote  0          0                     10.0.1.34
48:b0:2d:d9:2d:2d  local   0          0          bond1
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show evpn vni \<vni-id\> multihoming</h>

Shows multihoming information for the specified EVPN VNI.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vni-id>` |   The VNI name.|

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@switch:~$ nv show evpn vni 10 multihoming
No Data
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show evpn vni \<vni-id\> remote-vtep</h>

Shows EVPN VNI remote virtual tunnel endpoint information.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vni-id>` |   The VNI name.|

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@switch:~$ nv show evpn vni 20 remote-vtep
Flood - Remote-vtep flood type

RemoteVtep  Flood
----------  -----
10.0.1.34   HER
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show evpn vni \<vni-id\> route-advertise</h>

Shows EVPN VNI route advertise configuration.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vni-id>` |   The VNI name.|

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@switch:~$ nv show evpn vni 20 route-advertise
                 operational  applied
---------------  -----------  -------
svi-ip           off
default-gateway  off
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show evpn vni \<vni-id\> route-target</h>

Shows EVPN VNI route target information.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vni-id>` |   The VNI name.|

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@switch:~$ nv show evpn vni 20 route-target
No Data
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp address-family l2vpn-evpn</h>

Shows EVPN BGP configuration for the specified VRF.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` |  The VRF name.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp address-family l2vpn-evpn
        operational  applied
------  -----------  -------
enable               off
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp address-family l2vpn-evpn loc-rib</h>

Shows the EVPN local RIB for the specified VRF.

{{%notice note%}}
Cumulus Linux 5.11 and later no longer provides this command. Use the `nv show vrf <vrf-id> router bgp address-family l2vpn-evpn route` command instead.
{{%/notice%}}

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` |  The VRF name.|

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp address-family l2vpn-evpn loc-rib
rd
=====
              Summary      
------------  -------------
10.10.10.1:2  route-type: 1
              route-type: 2
              route-type: 3
10.10.10.1:3  route-type: 1
              route-type: 4
10.10.10.1:4  route-type: 1
              route-type: 2
              route-type: 3
10.10.10.1:5  route-type: 1
              route-type: 2
              route-type: 3
10.10.10.1:6  route-type: 5
10.10.10.1:7  route-type: 5
10.10.10.1:8  route-type: 1
...
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp address-family l2vpn-evpn loc-rib rd</h>

Shows the EVPN local RIB <span class="a-tooltip">[RDs](## "Route Distinguisher")</span> for the specified VRF.

{{%notice note%}}
Cumulus Linux 5.11 and later no longer provides this command.
{{%/notice%}}

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` |  The VRF name.|

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp address-family l2vpn-evpn loc-rib rd
              Summary      
------------  -------------
10.10.10.1:2  route-type: 1
              route-type: 2
              route-type: 3
10.10.10.1:3  route-type: 1
              route-type: 4
10.10.10.1:4  route-type: 1
              route-type: 2
              route-type: 3
10.10.10.1:5  route-type: 1
              route-type: 2
              route-type: 3
10.10.10.1:6  route-type: 5
10.10.10.1:7  route-type: 5
10.10.10.1:8  route-type: 1
              route-type: 4
...
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp address-family l2vpn-evpn loc-rib rd \<rd-id\></h>

Shows a specific EVPN local RIB <span class="a-tooltip">[RD](## "Route Distinguisher")</span> for the specified VRF.

{{%notice note%}}
Cumulus Linux 5.11 and later no longer provides this command.
{{%/notice%}}

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` |  The VRF name.|
| `<rd-id>` |  The route distinguisher ID.|

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp address-family l2vpn-evpn loc-rib rd 10.10.10.1:9
              operational  applied
------------  -----------  -------
[route-type]  1                   
[route-type]  4
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp address-family l2vpn-evpn loc-rib rd \<rd-id\> route-type</h>

Shows the EVPN local RIB <span class="a-tooltip">[RD](## "Route Distinguisher")</span> route distinguisher route types for the specified VRF.

{{%notice note%}}
Cumulus Linux 5.11 and later no longer provides this command.
{{%/notice%}}

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` |  The VRF name.|
| `<rd-id>` |  The route distinguisher ID: `ead`, `macip`, `multicast`, `ethernet-segment`, `prefix`, or an integer between 1 and 5. |

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp address-family l2vpn-evpn loc-rib rd 10.10.10.1:9 route-type
  Summary                                                                          
-  ---------------------------------------------------------------------------------
1  route: 03:44:38:39:be:ef:aa:00:00:03+::]/352+03:44:38:39:be:ef:aa:00:00:03+::/352
4  route:                               03:44:38:39:be:ef:aa:00:00:03+10.10.10.1/352
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp address-family l2vpn-evpn loc-rib rd \<rd-id\> route-type \<route-type-id\></h>

Shows information about a specific EVPN local RIB <span class="a-tooltip">[RD](## "Route Distinguisher")</span> route distinguisher route type for the specified VRF.

{{%notice note%}}
Cumulus Linux 5.11 and later no longer provides this command.
{{%/notice%}}

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` |  The VRF name.|
| `<rd-id>` |  The route distinguisher ID.|
| `<route-type-id>` |  The route type: `ead`, `macip`, `multicast`, `ethernet-segment`, `prefix`, or an integer between 1 and 5.|

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp address-family l2vpn-evpn loc-rib rd 10.10.10.1:20 route-type multicast
route 

======== 

      Advto - peers the prefix is advertised to, EVPNPrefixStr - EVPN prefix string    

    (Mac + IP), MAC - MAC Address, Peer - neighbor router-id, PathCnt - number of    

    L2VPN EVPN per (RD, route-type) paths                                         

    Route      Advto  EVPNPrefixStr           MAC  Peer                PathCnt  VNI  Weight 

    ---------  -----  ----------------------  ---  ------------------  -------  ---  ------ 

    0+1.1.1.1  swp1   [3]:[0]:[32]:[1.1.1.1]       id: 0.0.0.0         1        101  32768  

                                                   router-id: 1.1.1.1
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp address-family l2vpn-evpn loc-rib rd \<rd-id\> route-type \<route-type-id\> route</h>

Shows the routes in the EVPN local RIB for the specified VRF with a specific <span class="a-tooltip">[RD](## "Route Distinguisher")</span> and route type.

{{%notice note%}}
Cumulus Linux 5.11 and later no longer provides this command.
{{%/notice%}}

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` |  The VRF name.|
| `<rd-id>` |  The route distinguisher ID.|
| `<route-type-id>` |  The route type: `ead`, `macip`, `multicast`, `ethernet-segment`, `prefix`, or an integer between 1 and 5.|

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp address-family l2vpn-evpn loc-rib rd 10.10.10.1:20 route-type multicast route
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp address-family l2vpn-evpn loc-rib rd \<rd-id\> route-type \<route-type-id\> route \<evpn-route-id\></h>

Shows the routes in the EVPN local RIB for the specified VRF with a specific <span class="a-tooltip">[RD](## "Route Distinguisher")</span> route type and EVPN route type.

{{%notice note%}}
Cumulus Linux 5.11 and later no longer provides this command.
{{%/notice%}}

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` |  The VRF name.|
| `<rd-id>` |  The route distinguisher ID.|
| `<route-type-id>` |  The route type: `ead`, `macip`, `multicast`, `ethernet-segment`, `prefix`, or an integer between 1 and 5.|
| `<evpn-route-id>` |  The EVPN route type.|

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp address-family l2vpn-evpn loc-rib rd 10.10.10.1:20 route-type multicast route
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp address-family l2vpn-evpn route</h>

Shows BGP EVPN routing table.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` |  The VRF name.|

### Version History

Introduced in Cumulus Linux 5.11.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp address-family l2vpn-evpn route
PathCnt - number of L2VPN EVPN per (RD, route-type) paths

Route                                                                   rd             route-type  PathCnt
----------------------------------------------------------------------  -------------  ----------  -------
[10.10.10.1:2]:[5]:[0]:[10.1.30.0/24]                                   10.10.10.1:2   5           5
[10.10.10.1:3]:[5]:[0]:[10.1.10.0/24]                                   10.10.10.1:3   5           5
[10.10.10.1:3]:[5]:[0]:[10.1.20.0/24]                                   10.10.10.1:3   5           5
[10.10.10.2:2]:[5]:[0]:[10.1.30.0/24]                                   10.10.10.2:2   5           1
[10.10.10.2:3]:[5]:[0]:[10.1.10.0/24]                                   10.10.10.2:3   5           1
[10.10.10.2:3]:[5]:[0]:[10.1.20.0/24]                                   10.10.10.2:3   5           1
[10.10.10.2:4]:[2]:[0]:[44:38:39:22:01:7a]                              10.10.10.2:4   2           1
[10.10.10.2:4]:[2]:[0]:[48:b0:2d:a4:0d:7a]                              10.10.10.2:4   2           1
[10.10.10.2:4]:[2]:[0]:[48:b0:2d:a4:0d:7a]:[fe80::4ab0:2dff:fea4:d7a]   10.10.10.2:4   2           1
[10.10.10.2:4]:[2]:[0]:[48:b0:2d:bc:36:08]                              10.10.10.2:4   2           1
[10.10.10.2:4]:[3]:[0]:[10.0.1.12]                                      10.10.10.2:4   3           1
[10.10.10.2:5]:[2]:[0]:[44:38:39:22:01:7a]                              10.10.10.2:5   2           1
[10.10.10.2:5]:[2]:[0]:[48:b0:2d:7b:a7:e9]                              10.10.10.2:5   2           1
[10.10.10.2:5]:[2]:[0]:[48:b0:2d:9a:8d:47]                              10.10.10.2:5   2           1
[10.10.10.2:5]:[2]:[0]:[48:b0:2d:9a:8d:47]:[fe80::4ab0:2dff:fe9a:8d47]  10.10.10.2:5   2           1
[10.10.10.2:5]:[3]:[0]:[10.0.1.12]                                      10.10.10.2:5   3           1
[10.10.10.2:6]:[2]:[0]:[44:38:39:22:01:7a]                              10.10.10.2:6   2           1
[10.10.10.2:6]:[2]:[0]:[48:b0:2d:72:90:d7]                              10.10.10.2:6   2           1
...
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp address-family l2vpn-evpn route \<route-id\></h>

Shows information about the BGP EVPN route.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` |  The VRF name.|

### Version History

Introduced in Cumulus Linux 5.11.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp address-family l2vpn-evpn route 10.10.10.1:3
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp address-family l2vpn-evpn route-count</h>

Shows the BGP EVPN route and path count.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` |  The VRF name.|

### Version History

Introduced in Cumulus Linux 5.11.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp address-family l2vpn-evpn route-count
              operational
------------  -----------
total-routes  63
total-paths   243
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp address-family l2vpn-evpn update-group</h>

Shows information about BGP EVPN update group events.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` |  The VRF name.|

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp address-family l2vpn-evpn update-group
RouteMap - Outbound route map, MinAdvInterval - Minimum route advertisement     
interval, CreationTime - Time when the update group was created, LocalAsChange -
LocalAs changes for inbound route, Flags - r - replace-as, x - no-prepend       
                                                                                
UpdateGrp  RouteMap  MinAdvInterval  CreationTime          LocalAsChange  Flags
---------  --------  --------------  --------------------  -------------  -----
2                    0               2024-11-14T08:58:25Z
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp address-family l2vpn-evpn update-group \<group-id\></h>

Shows information about a specific BGP EVPN update group.

{{%notice note%}}
In Cumulus Linux 5.10 and earlier, add `-o json` at the end of the command to see the output in a more readable format.
{{%/notice%}}

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` |  The VRF name.|
| `<group-id>` |  The BGP group ID.|

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp address-family l2vpn-evpn update-group 2
                                  operational         
--------------------------------  --------------------
update-group-id                   2                   
min-route-advertisement-interval  0                   
create-time                       2024-11-15T10:01:47Z

sub-group
============
                                                                                
    CreateTime - Time when the sub group was created, AdvRouteCnt - Number of routes
    advertised to peer, Refresh - Indicates if subgroup requires refresh,           
    TotalQueuePkt - Total packets in queue, TotalEnqueuePkt - Total packets         
    enqueued, PktQueueLength - Packet queue length, Neighbor - Sub group peer info  
                                                                                
    GrpID  CreateTime            AdvRouteCnt  Refresh  TotalQueuePkt  TotalEnqueuePkt  PktQueueLength  Neighbor     
    -----  --------------------  -----------  -------  -------------  ---------------  --------------  -------------
    2      2024-11-15T10:01:47Z  72           off      104            104              0               peerlink.4094
                                                                                                       swp52        
                                                                                                       swp53        
                                                                                                       swp54
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp address-family l2vpn-evpn update-group \<group-id\> sub-group</h>

Shows the subgroup information for a specific BGP EVPN update group.

{{%notice note%}}
In Cumulus Linux 5.10 and earlier, add `-o json` at the end of the command to see the output in a more readable format.
{{%/notice%}}

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` |  The VRF name.|
| `<group-id>` |  The BGP group ID.|

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp address-family l2vpn-evpn update-group 2 sub-group 
                                                                                
CreateTime - Time when the sub group was created, AdvRouteCnt - Number of routes
advertised to peer, Refresh - Indicates if subgroup requires refresh,           
TotalQueuePkt - Total packets in queue, TotalEnqueuePkt - Total packets         
enqueued, PktQueueLength - Packet queue length, Neighbor - Sub group peer info  
                                                                                
GrpID  CreateTime            AdvRouteCnt  Refresh  TotalQueuePkt  TotalEnqueuePkt  PktQueueLength  Neighbor     
-----  --------------------  -----------  -------  -------------  ---------------  --------------  -------------
2      2024-11-15T10:01:47Z  72           off      104            104              0               peerlink.4094
                                                                                                   swp52        
                                                                                                   swp53        
                                                                                                   swp54
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> evpn bgp-info</h>

Shows layer 3 VNI information from BGP for the specified VRF.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@switch:~$ nv show vrf RED evpn bgp-info
                       operational      
---------------------  -----------------
rd                     10.10.10.1:3     
local-vtep             10.0.1.12        
router-mac             44:38:39:be:ef:aa
system-mac             44:38:39:22:01:7a
system-ip              10.10.10.1       
[import-route-target]  65101:4001       
[export-route-target]  65101:4001 
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family l2vpn-evpn</h>

Shows EVPN configuration for the specified BGP neighbor.

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |
| `<neighbor-id>`  |  The BGP neighbor name or interface (for BGP unnumbered).  |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp neighbor swp51 address-family l2vpn-evpn
                       operational  applied
---------------------  -----------  -------
enable                              on     
attribute-mod                              
  aspath               off                 
  med                  off                 
  nexthop              on                  
graceful-restart                           
  rx-eof-rib           off                 
  tx-eof-rib           off                 
prefix-limits                              
  inbound                                  
    maximum            1                   
    warning-threshold  75                  
    warning-only       off
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family l2vpn-evpn attribute-mod</h>

Shows the attribute modification configuration settings for the specified neighbor for EVPN.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |
| `<neighbor-id>`  |  The BGP neighbor name or interface (for BGP unnumbered).  |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp neighbor swp51 address-family l2vpn-evpn attribute-mod
         operational  applied
-------  -----------  -------
aspath   off                 
med      off                 
nexthop  on
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family l2vpn-evpn aspath</h>

Shows the configuration options for handling the AS path for prefixes to and from the specified BGP neighbor for EVPN.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |
| `<neighbor-id>`  |  The BGP neighbor name or interface (for BGP unnumbered).  |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp neighbor swp51 address-family l2vpn-evpn aspath
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family l2vpn-evpn aspath allow-my-asn</h>

Shows if it is acceptable for a received AS path to contain the ASN of the local system for EVPN.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |
| `<neighbor-id>`  |  The BGP neighbor name or interface (for BGP unnumbered).  |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp neighbor swp51 address-family l2vpn-evpn aspath allow-my-asn
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family l2vpn-evpn graceful-restart</h>

Shows graceful restart configuration for the specified BGP peer for EVPN.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |
| `<neighbor-id>`  |  The BGP neighbor name or interface (for BGP unnumbered).  |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp neighbor swp51 address-family l2vpn-evpn graceful-restart
            operational
----------  -----------
rx-eof-rib  on                           
tx-eof-rib  on
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family l2vpn-evpn graceful-restart timers</h>

Shows the BGP graceful restart selection deferral and stale path timer settings for the specified neighbor for EVPN.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |
| `<neighbor-id>`  |  The BGP neighbor name or interface (for BGP unnumbered).  |

### Version History

Introduced in Cumulus Linux 5.9.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp neighbor swp51 address-family l2vpn-evpn graceful-restart timers
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family l2vpn-evpn graceful-restart timers stale-path</h>

Shows the BGP graceful restart stale path timer settings for the specified neighbor for EVPN.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |
| `<neighbor-id>`  |  The BGP neighbor name or interface (for BGP unnumbered).  |

### Version History

Introduced in Cumulus Linux 5.9.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp neighbor swp51 address-family l2vpn-evpn graceful-restart timers stale-path
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family l2vpn-evpn graceful-restart timers selection-deferral</h>

Shows the BGP graceful restart selection deferral timer for the specified neighbor for EVPN.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |
| `<neighbor-id>`  |  The BGP neighbor name or interface (for BGP unnumbered).  |

### Version History

Introduced in Cumulus Linux 5.9.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp neighbor swp51 address-family l2vpn-evpn graceful-restart timers selection-deferral
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family l2vpn-evpn policy</h>

Shows EVPN policies for the specified neighbor.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |
| `<neighbor-id>`  |  The BGP neighbor name or interface (for BGP unnumbered).  |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp neighbor swp51 address-family l2vpn-evpn policy
                  operational  applied
----------------  -----------  -------
inbound                               
  route-map       MAP1         MAP1   
outbound                              
  route-map                    none   
  unsuppress-map               none
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family l2vpn-evpn policy inbound</h>

Shows the inbound EVPN policy for the specified BGP neighbor.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |
| `<neighbor-id>`  |  The BGP neighbor name or interface (for BGP unnumbered).  |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp neighbor swp51 address-family l2vpn-evpn policy inbound
           operational  applied
---------  -----------  -------
route-map  MAP1         MAP1  
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family l2vpn-evpn policy outbound</h>

Shows the outbound EVPN policy for the specified BGP neighbor.


### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |
| `<neighbor-id>`  |  The BGP neighbor name or interface (for BGP unnumbered).  |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp neighbor swp51 address-family l2vpn-evpn policy outbound
                operational  applied
--------------  -----------  -------
route-map                    none   
unsuppress-map               none
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family l2vpn-evpn capabilities</h>

Shows all advertised and received EVPN capabilities for the specified BGP neighbor.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |
| `<neighbor-id>`  |  The BGP neighbor name or interface (for BGP unnumbered).  |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp neighbor swp51 address-family l2vpn-evpn capabilities
                     operational
-------------------  -----------
rx-addpath           on                           
rx-graceful-restart  on                           
rx-mpbgp             on                           
tx-addpath           off                          
tx-mpbgp             on
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family l2vpn-evpn prefix-limits inbound</h>

Shows the configured prefix limits from the specified peer for EVPN.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |
| `<neighbor-id>`  |  The BGP neighbor name or interface (for BGP unnumbered).  |

### Version History

Introduced in Cumulus Linux 5.10.0

### Example

```
cumulus@switch:~$ nv show  vrf default router bgp neighbor swp51 address-family l2vpn-evpn prefix-limits inbound 
                   operational  applied  
-----------------  -----------  -------
maximum                         none   
warning-threshold               75     
warning-only       off
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family l2vpn-evpn</h>

Shows configuration information for the specified BGP peer group for EVPN.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |
| `<peer-group-id>` | The peer group name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp peer-group SPINES address-family l2vpn-evpn
        applied
------  -------
enable  off
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family l2vpn-evpn attribute-mod</h>

Shows the attribute modification configuration settings for the specified BGP peer group for EVPN.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |
| `<peer-group-id>`  |   The peer group name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp peer-group SPINES address-family l2vpn-evpn attribute-mod
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family l2vpn-evpn aspath</h>

Shows the configuration settings for handling the AS path for prefixes to and from the specified BGP peer group for EVPN.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |
| `<peer-group-id>`  |  The peer group name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp peer-group SPINES address-family l2vpn-evpn aspath
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family l2vpn-evpn aspath allow-my-asn</h>

Shows if it is acceptable for a received AS path from the specified BGP peer group to contain the ASN of the local system for EVPN.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |
| `<peer-group-id>`  |   The peer group name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp peer-group SPINES address-family l2vpn-evpn aspath allow-my-asn
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family l2vpn-evpn policy</h>

Shows the EVPN policies for the specified BGP peer group.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |
| `<peer-group-id>`  |   The peer group name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp peer-group SPINES address-family l2vpn-evpn policy
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family l2vpn-evpn policy inbound</h>

Shows the inbound EVPN policy for the specified BGP peer group.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |
| `<peer-group-id>`  |   The peer group name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp peer-group SPINES address-family l2vpn-evpn policy inbound
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family l2vpn-evpn policy outbound</h>

Shows the outbound EVPN policy for the specified BGP peer group.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |
| `<peer-group-id>`  |  The peer group name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp peer-group SPINES address-family l2vpn-evpn policy outbound
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp route-export</h>

Shows BGP route export configuration for the specified VRF.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp route-export
                  operational  applied  pending
----------------  -----------  -------  -------
to-evpn                                        
  [route-target]               auto     auto
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp route-export to-evpn</h>

Shows BGP route export to EVPN configuration for the specified VRF.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp route-export to-evpn route-target 
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp route-export to-evpn route-target</h>

Shows the RTs configured for BGP route export for the specified VRF.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp route-export to-evpn route-target
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp route-export to-evpn route-target \<rt-id\></h>

Shows BGP route export configuration for a specific RT in the specified VRF.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |
| `<rt-id>` |  The route target. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp route-export to-evpn route-target 10.10.10.1:20
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp route-import from-evpn</h>

Shows BGP route import from EVPN configuration for the specified VRF.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp route-import from-evpn route-target
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp route-import from-evpn route-target</h>

Shows the RTs configured for BGP route import from EVPN for the specified VRF.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp route-import from-evpn route-target
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp route-import from-evpn route-target \<rt-id\></h>

Shows configuration for a specific RD and layer 3 RT for the specified VRF.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name.|
| `<rt-id>` | The route target. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp route-import from-evpn route-target 10.10.10.1:20
```
