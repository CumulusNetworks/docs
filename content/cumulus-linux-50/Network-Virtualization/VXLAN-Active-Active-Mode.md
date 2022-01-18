---
title: VXLAN Active-active Mode
author: NVIDIA
weight: 615
toc: 3
---
*VXLAN active-active mode* enables a pair of [MLAG](## "Multi Chassis Link Aggregation") switches to act as a single [VTEP](## "Virtual Tunnel End Point"), providing active-active VXLAN termination for bare metal as well as virtualized workloads.

To work correctly, VXLAN active-active mode requires the following underlying technologies:
- {{<link url="Multi-Chassis-Link-Aggregation-MLAG" text="MLAG">}}
- {{<link url="Open-Shortest-Path-First-OSPF" text="OSPF">}} or {{<link url="Border-Gateway-Protocol-BGP" text="BGP">}}
- {{<link url="VXLAN-Devices" text="VXLAN interfaces">}}

{{%notice note%}}
If the bridge that connects to the VXLAN uses [STP](## "Spanning Tree Protocol"), you must configure {{<link url="Spanning-Tree-and-Rapid-Spanning-Tree-STP#bpdu-filter" text="BPDU filter">}} and {{<link url="Spanning-Tree-and-Rapid-Spanning-Tree-STP#bpdu-guard" text="BPDU guard">}} on the VXLAN interfaces.
{{%/notice%}}
<!-- vale off -->
## Configure VXLAN Active-Active
<!-- vale on -->
To configure VXLAN active-active, you must provision each switch in an MLAG pair with a virtual IP address for VXLAN data-path termination. The VXLAN termination address is an anycast IP address that you configure under the loopback interface. With MLAG peering, both switches use the anycast IP address for VXLAN encapsulation and decapsulation. This enables remote VTEPs to learn the host MAC addresses attached to the MLAG switches against one logical VTEP, even though the switches independently encapsulate and decapsulate layer 2 traffic originating from the host.

MLAG dynamically adds and removes the anycast IP address as the loopback interface address as follows:

1. When the switches boot up, all VXLAN interfaces are in a PROTO_DOWN state. The anycast IP address is not in use.
2. MLAG peering takes place and a successful VXLAN interface consistency check between the switches occurs.
3. The `clagd` daemon adds the anycast address to the loopback interface as a second address. It then changes the local IP address of the VXLAN interface from a unique address to the anycast IP address and puts the interface in an UP state.

{{%notice note%}}
- The active-active configuration for a given VXLAN interface must be consistent between the MLAG switches; MLAG ensures that the configuration is consistent before bringing up the VXLAN interfaces.
  - The anycast virtual IP address for VXLAN termination must be the same on both switches in the MLAG pair.
  - You must configure a VXLAN interface with the same VXLAN ID, which must be administratively up on both switches in the MLAG pair. Run the `clagctl` command to check if any VXLAN switches are in a PROTO_DOWN state.
{{%/notice%}}

To configure the anycast IP address:

<!-- vale off -->
{{< img src = "/images/cumulus-linux/vxlan-active-active-config.png" >}}
<!-- vale on -->
{{< tabs "TabID67 ">}}
{{< tab "NVUE Commands ">}}

Run the `nv set nve vxlan mlag shared-address` command.

{{< tabs "TabID81 ">}}
{{< tab "leaf01 ">}}

```
cumulus@leaf01:~$ nv set nve vxlan mlag shared-address 10.0.1.12
cumulus@leaf01:~$ nv config apply
```

{{< /tab >}}
{{< tab "leaf02 ">}}

```
cumulus@leaf02:~$ nv set nve vxlan mlag shared-address 10.0.1.12
cumulus@leaf02:~$ nv config apply
```

{{< /tab >}}
{{< /tabs >}}

{{< /tab >}}
{{< tab "Linux Commands ">}}

Add the `clagd-vxlan-anycast-ip` parameter under the loopback interface in the `/etc/network/interfaces` file:

{{< tabs "TabID291 ">}}
{{< tab "leaf01 ">}}

```
cumulus@leaf01:~$ sudo nano /etc/network/interfaces
...
auto lo
iface lo inet loopback
  address 10.10.10.1/32
  clagd-vxlan-anycast-ip 10.0.1.12
```

{{< /tab >}}
{{< tab "leaf02 ">}}

```
cumulus@leaf02:~$ sudo nano /etc/network/interfaces
...
auto lo
iface lo inet loopback
  address 10.10.10.2/32
  clagd-vxlan-anycast-ip 10.0.1.12
```

{{< /tab >}}
{{< /tabs >}}

{{< /tab >}}
{{< /tabs >}}

## Troubleshooting

This section describes VXLAN active-active failure conditions and provides troubleshooting commands.

### Failure Conditions

| <div style="width:250px">Failure Condition | Behavior |
| --------------------------------- | ---------|
| The peer link goes down. | The primary MLAG switch continues to keep all VXLAN interfaces up with the anycast IP address while the secondary switch brings down all VXLAN interfaces and places them in a PROTO_DOWN state. The secondary MLAG switch removes the anycast IP address from the loopback interface and changes the local IP address of the VXLAN interface to the configured unique IP address. |
| One of the switches goes down. | The other operational switch continues to use the anycast IP address. |
| `clagd` stops. | All VXLAN interfaces go in a PROTO_DOWN state. The switch removes the anycast IP address from the loopback interface and the local IP addresses of the VXLAN interfaces change from the anycast IP address to unique non-virtual IP addresses. |
| MLAG peering does not establish between the switches. | `clagd` brings up all the VXLAN interfaces after the reload timer expires with the configured anycast IP address. This allows the VXLAN interface to be up and running on both switches even though peering is not established. |
| The peer link goes down but the peer switch is up (the backup link is active). | All VXLAN interfaces go into a PROTO_DOWN state on the secondary switch. |
| The anycast IP address is different on the MLAG peers. | The VXLAN interface goes into a PROTO_DOWN state on the secondary switch. |

### Troubleshooting Commands

To show the MLAG configuration on the switch, run the NVUE `nv show mlag` command:

```
cumulus@leaf01:mgmt:~$ nv show mlag
                operational              applied            description
--------------  -----------------------  -----------------  ------------------------------------------------------
enable                                   on                 Turn the feature 'on' or 'off'.  The default is 'off'.
debug                                    off                Enable MLAG debugging
init-delay                               180                The delay, in seconds, before bonds are brought up.
mac-address     44:38:39:be:ef:aa        44:38:39:BE:EF:AA  Override anycast-mac and anycast-id
peer-ip         fe80::4638:39ff:fe00:5a  linklocal          Peer Ip Address
priority        32768                    32768              Mlag Priority
[backup]        10.10.10.2               10.10.10.2         Set of MLAG backups
anycast-ip      10.0.1.12                                   Vxlan Anycast Ip address
backup-active   True                                        Mlag Backup Status
backup-reason                                               Mlag Backup Reason
local-id        44:38:39:00:00:59                           Mlag Local Unique Id
local-role      primary                                     Mlag Local Role
peer-alive      True                                        Mlag Peer Alive Status
peer-id         44:38:39:00:00:5a                           Mlag Peer Unique Id
peer-interface  peerlink.4094                               Mlag Peerlink Interface
peer-priority   32768                                       Mlag Peer Priority
peer-role       secondary                                   Mlag Peer Role
```

To show the MLAG neighbor information on the switch, run the NVUE `nv show mlag neighbor` command:

```
cumulus@leaf01:mgmt:~$ nv show mlag neighbor
    operational  applied  description
--  -----------  -------  -----------


dynamic
==========
        interface  ip-address  lladdr  vlan-id
    --  ---------  ----------  ------  -------


permanent
============
        address-family  interface  ip-address                lladdr             vlan-id
    --  --------------  ---------  ------------------------  -----------------  -------
    1   10              vlan10     fe80::4638:39ff:fe22:1b1  44:38:39:22:01:b1  10
    2   10              vlan20     fe80::4638:39ff:fe22:1b1  44:38:39:22:01:b1  20
    3   10              vlan10     fe80::4638:39ff:fe22:1af  44:38:39:22:01:af  10
    4   10              vlan20     fe80::4638:39ff:fe22:1af  44:38:39:22:01:af  20
```

To show MLAG behavior and any inconsistencies between an MLAG pair, run the `clagctl` command.

In the following example, no conflicts exist for this MLAG interface and the VXLAN is up and running (there is no Proto-Down). The VXLAN anycast IP address shared by the MLAG pair for VTEP termination is in use and is 10.0.1.12.

```
cumulus@leaf01$ clagctl
The peer is alive
     Our Priority, ID, and Role: 32768 44:38:39:00:00:59 primary
    Peer Priority, ID, and Role: 32768 44:38:39:00:00:5a secondary
          Peer Interface and IP: peerlink.4094 fe80::4638:39ff:fe00:5a (linklocal)
               VxLAN Anycast IP: 10.0.1.12
                      Backup IP: 10.10.10.2 (active)
                     System MAC: 44:38:39:be:ef:aa

CLAG Interfaces
Our Interface      Peer Interface     CLAG Id   Conflicts              Proto-Down Reason
----------------   ----------------   -------   --------------------   -----------------
           bond1   -                  1         -                      -              
         vxlan48   vxlan48            -         -                      -
```

In the following example, the primary switch has the wrong VXLAN anycast IP address configured. When you run the `clagctl` command on the secondary switch, the `Proto-Down Reason` shows `anycast-ip-mismatch` on bond01 and `vxlan-single,anycast-ip-mismatch` on vxlan48.

```
cumulus@leaf04:mgmt:~$ clagctl
The peer is alive
     Our Priority, ID, and Role: 32768 44:38:39:00:00:5e secondary
    Peer Priority, ID, and Role: 32768 44:38:39:00:00:5d primary
          Peer Interface and IP: peerlink.4094 fe80::4638:39ff:fe00:5d (linklocal)
               VxLAN Anycast IP: 10.0.1.34
                      Backup IP: 10.10.10.3 (active)
                     System MAC: 44:38:39:be:ef:bb

CLAG Interfaces
Our Interface      Peer Interface     CLAG Id   Conflicts              Proto-Down Reason
----------------   ----------------   -------   --------------------   -----------------
           bond1   -                  1         -                      anycast-ip-mismatch
         vxlan48   -                  -         -                      vxlan-single,anycast-ip-mismatch
```

<!-- vale off -->
## Example VXLAN Active-Active Configuration

{{< img src = "/images/cumulus-linux/vxlan-active-active-example.png" >}}
<!-- vale on -->
This commands in this example configure:
- MLAG between leaf01 and leaf02, and between leaf03 and leaf04.
- BGP unnumbered on all leafs and spines.
- A single VXLAN device (vxlan48) on each leaf. VLAN 10 maps to VNI 10 and VLAN 20 to VNI 20. The VXLAN device is part of the default bridge `br_default`.
- The anycast IP address 10.0.1.12 on leaf01 and leaf02, and 10.0.1.34 on leaf03 and leaf04.
- Layer 2 bonds that link server01 to leaf01 and leaf02, and server03 to leaf03 and leaf04.

{{< tabs "TabID113 ">}}
{{< tab "NVUE Commands ">}}

{{< tabs "TabID116 ">}}
{{< tab "leaf01 ">}}

```
cumulus@leaf01:~$ nv set interface lo ip address 10.10.10.1/32
cumulus@leaf01:~$ nv set interface swp1,swp49-52
cumulus@leaf01:~$ nv set interface bond1 bond member swp1
cumulus@leaf01:~$ nv set interface bond1 bond mlag id 1
cumulus@leaf01:~$ nv set interface bond1 bridge domain br_default 
cumulus@leaf01:~$ nv set interface peerlink bond member swp49-50
cumulus@leaf01:~$ nv set mlag mac-address 44:38:39:BE:EF:AA
cumulus@leaf01:~$ nv set mlag backup 10.10.10.2
cumulus@leaf01:~$ nv set mlag peer-ip linklocal
cumulus@leaf01:~$ nv set interface vlan10 
cumulus@leaf01:~$ nv set interface vlan20
cumulus@leaf01:~$ nv set bridge domain br_default vlan 10,20
cumulus@leaf01:~$ nv set bridge domain br_default vlan 10 vni 10
cumulus@leaf01:~$ nv set bridge domain br_default vlan 20 vni 20
cumulus@leaf01:~$ nv set nve vxlan mlag shared-address 10.0.1.12
cumulus@leaf01:~$ nv set router bgp autonomous-system 65101
cumulus@leaf01:~$ nv set router bgp router-id 10.10.10.1
cumulus@leaf01:~$ nv set vrf default router bgp neighbor swp51 remote-as external
cumulus@leaf01:~$ nv set vrf default router bgp neighbor swp52 remote-as external
cumulus@leaf01:~$ nv set vrf default router bgp address-family ipv4-unicast network 10.10.10.1/32
cumulus@leaf01:~$ nv set vrf default router bgp address-family ipv4-unicast redistribute connected
cumulus@leaf01:~$ nv config apply
```

{{< /tab >}}
{{< tab "leaf02 ">}}

```
cumulus@leaf02:~$ nv set interface lo ip address 10.10.10.2/32
cumulus@leaf02:~$ nv set interface swp1,swp49-52
cumulus@leaf02:~$ nv set interface bond1 bond member swp1
cumulus@leaf02:~$ nv set interface bond1 bond mlag id 1
cumulus@leaf02:~$ nv set interface bond1 bridge domain br_default 
cumulus@leaf02:~$ nv set interface peerlink bond member swp49-50
cumulus@leaf02:~$ nv set mlag mac-address 44:38:39:BE:EF:AA
cumulus@leaf02:~$ nv set mlag backup 10.10.10.1
cumulus@leaf02:~$ nv set mlag peer-ip linklocal
cumulus@leaf02:~$ nv set interface vlan10 
cumulus@leaf02:~$ nv set interface vlan20
cumulus@leaf02:~$ nv set bridge domain br_default vlan 10,20
cumulus@leaf02:~$ nv set bridge domain br_default vlan 10 vni 10
cumulus@leaf02:~$ nv set bridge domain br_default vlan 20 vni 20
cumulus@leaf02:~$ nv set nve vxlan mlag shared-address 10.0.1.12
cumulus@leaf02:~$ nv set router bgp autonomous-system 65102
cumulus@leaf02:~$ nv set router bgp router-id 10.10.10.2
cumulus@leaf02:~$ nv set vrf default router bgp neighbor swp51 remote-as external
cumulus@leaf02:~$ nv set vrf default router bgp neighbor swp52 remote-as external
cumulus@leaf02:~$ nv set vrf default router bgp address-family ipv4-unicast network 10.10.10.2/32
cumulus@leaf02:~$ nv set vrf default router bgp address-family ipv4-unicast redistribute connected
cumulus@leaf02:~$ nv config apply
```

{{< /tab >}}
{{< tab "leaf03 ">}}

```
cumulus@leaf03:~$ nv set interface lo ip address 10.10.10.3/32
cumulus@leaf03:~$ nv set interface swp1,swp49-52
cumulus@leaf03:~$ nv set interface bond1 bond member swp1
cumulus@leaf03:~$ nv set interface bond1 bond mlag id 1
cumulus@leaf03:~$ nv set interface bond1 bridge domain br_default 
cumulus@leaf03:~$ nv set interface peerlink bond member swp49-50
cumulus@leaf03:~$ nv set mlag mac-address 44:38:39:BE:EF:BB
cumulus@leaf03:~$ nv set mlag backup 10.10.10.4
cumulus@leaf03:~$ nv set mlag peer-ip linklocal
cumulus@leaf03:~$ nv set interface vlan10 
cumulus@leaf03:~$ nv set interface vlan20
cumulus@leaf03:~$ nv set bridge domain br_default vlan 10,20
cumulus@leaf03:~$ nv set bridge domain br_default vlan 10 vni 10
cumulus@leaf03:~$ nv set bridge domain br_default vlan 20 vni 20
cumulus@leaf03:~$ nv set nve vxlan mlag shared-address 10.0.1.34
cumulus@leaf03:~$ nv set router bgp autonomous-system 65103
cumulus@leaf03:~$ nv set router bgp router-id 10.10.10.3
cumulus@leaf03:~$ nv set vrf default router bgp neighbor swp51 remote-as external
cumulus@leaf03:~$ nv set vrf default router bgp neighbor swp52 remote-as external
cumulus@leaf03:~$ nv set vrf default router bgp address-family ipv4-unicast network 10.10.10.3/32
cumulus@leaf03:~$ nv set vrf default router bgp address-family ipv4-unicast redistribute connected
cumulus@leaf03:~$ nv config apply
```

{{< /tab >}}
{{< tab "leaf04 ">}}

```
cumulus@leaf04:~$ nv set interface lo ip address 10.10.10.4/32
cumulus@leaf04:~$ nv set interface swp1,swp49-52
cumulus@leaf04:~$ nv set interface bond1 bond member swp1
cumulus@leaf04:~$ nv set interface bond1 bond mlag id 1
cumulus@leaf04:~$ nv set interface bond1 bridge domain br_default 
cumulus@leaf04:~$ nv set interface peerlink bond member swp49-50
cumulus@leaf04:~$ nv set mlag mac-address 44:38:39:BE:EF:BB
cumulus@leaf04:~$ nv set mlag backup 10.10.10.3
cumulus@leaf04:~$ nv set mlag peer-ip linklocal
cumulus@leaf04:~$ nv set interface vlan10 
cumulus@leaf04:~$ nv set interface vlan20
cumulus@leaf04:~$ nv set bridge domain br_default vlan 10,20
cumulus@leaf04:~$ nv set bridge domain br_default vlan 10 vni 10
cumulus@leaf04:~$ nv set bridge domain br_default vlan 20 vni 20
cumulus@leaf04:~$ nv set nve vxlan mlag shared-address 10.0.1.34
cumulus@leaf04:~$ nv set router bgp autonomous-system 65104
cumulus@leaf04:~$ nv set router bgp router-id 10.10.10.4
cumulus@leaf04:~$ nv set vrf default router bgp neighbor swp51 remote-as external
cumulus@leaf04:~$ nv set vrf default router bgp neighbor swp52 remote-as external
cumulus@leaf04:~$ nv set vrf default router bgp address-family ipv4-unicast network 10.10.10.4/32
cumulus@leaf04:~$ nv set vrf default router bgp address-family ipv4-unicast redistribute connected
cumulus@leaf04:~$ nv config apply
```

{{< /tab >}}
{{< tab "spine01 ">}}

```
cumulus@spine01:~$ nv set interface lo ip address 10.10.10.101/32
cumulus@spine01:~$ nv set interface swp1-4
cumulus@spine01:~$ nv set router bgp autonomous-system 65199
cumulus@spine01:~$ nv set router bgp router-id 10.10.10.101
cumulus@spine01:~$ nv set vrf default router bgp peer-group underlay remote-as external
cumulus@spine01:~$ nv set vrf default router bgp neighbor swp1 remote-as external
cumulus@spine01:~$ nv set vrf default router bgp neighbor swp2 remote-as external
cumulus@spine01:~$ nv set vrf default router bgp neighbor swp3 remote-as external
cumulus@spine01:~$ nv set vrf default router bgp neighbor swp4 remote-as external
cumulus@spine01:~$ nv set vrf default router bgp address-family ipv4-unicast redistribute connected
cumulus@spine01:~$ nv config apply
```

{{< /tab >}}
{{< tab "spine02 ">}}

```
cumulus@spine02:~$ nv set interface lo ip address 10.10.10.102/32
cumulus@spine02:~$ nv set interface swp1-4
cumulus@spine02:~$ nv set router bgp autonomous-system 65199
cumulus@spine02:~$ nv set router bgp router-id 10.10.10.102
cumulus@spine02:~$ nv set vrf default router bgp peer-group underlay remote-as external
cumulus@spine02:~$ nv set vrf default router bgp neighbor swp1 remote-as external
cumulus@spine02:~$ nv set vrf default router bgp neighbor swp2 remote-as external
cumulus@spine02:~$ nv set vrf default router bgp neighbor swp3 remote-as external
cumulus@spine02:~$ nv set vrf default router bgp neighbor swp4 remote-as external
cumulus@spine02:~$ nv set vrf default router bgp address-family ipv4-unicast redistribute connected
cumulus@spine02:~$ nv config apply
```

{{< /tab >}}
{{< /tabs >}}

{{< /tab >}}
{{< tab "/etc/network/interfaces ">}}

{{< tabs "TabID122 ">}}
{{< tab "leaf01 ">}}

```
cumulus@leaf01:~$ sudo cat /etc/network/interfaces
...
auto lo
iface lo inet loopback
    address 10.10.10.1/32
    clagd-vxlan-anycast-ip 10.0.1.12
    vxlan-local-tunnelip 10.10.10.1
auto mgmt
iface mgmt
    address 127.0.0.1/8
    address ::1/128
    vrf-table auto
auto eth0
iface eth0 inet dhcp
    ip-forward off
    ip6-forward off
    vrf mgmt
auto swp1
iface swp1
auto swp49
iface swp49
auto swp50
iface swp50
auto swp51
iface swp51
auto swp52
iface swp52
auto bond1
iface bond1
    bond-slaves swp1
    bond-mode 802.3ad
    bond-lacp-bypass-allow no
    clag-id 1
auto peerlink
iface peerlink
    bond-slaves swp49 swp50
    bond-mode 802.3ad
    bond-lacp-bypass-allow no
auto peerlink.4094
iface peerlink.4094
    clagd-peer-ip linklocal
    clagd-backup-ip 10.10.10.2
    clagd-sys-mac 44:38:39:BE:EF:AA
    clagd-args --initDelay 180
auto vlan10
iface vlan10
    hwaddress 44:38:39:22:01:af
    vlan-raw-device br_default
    vlan-id 10
auto vlan20
iface vlan20
    hwaddress 44:38:39:22:01:af
    vlan-raw-device br_default
    vlan-id 20
auto vxlan48
iface vxlan48
    bridge-vlan-vni-map 10=10 20=20
    bridge-learning off
auto br_default
iface br_default
    bridge-ports bond1 peerlink vxlan48
    hwaddress 44:38:39:22:01:af
    bridge-vlan-aware yes
    bridge-vids 10 20
```

{{< /tab >}}
{{< tab "leaf02 ">}}

```
cumulus@leaf02:~$ sudo cat /etc/network/interfaces
...
auto lo
iface lo inet loopback
    address 10.10.10.2/32
    clagd-vxlan-anycast-ip 10.0.1.12
    vxlan-local-tunnelip 10.10.10.2
auto mgmt
iface mgmt
    address 127.0.0.1/8
    address ::1/128
    vrf-table auto
auto eth0
iface eth0 inet dhcp
    ip-forward off
    ip6-forward off
    vrf mgmt
auto swp1
iface swp1
auto swp49
iface swp49
auto swp50
iface swp50
auto swp51
iface swp51
auto swp52
iface swp52
auto bond1
iface bond1
    bond-slaves swp1
    bond-mode 802.3ad
    bond-lacp-bypass-allow no
    clag-id 1
auto peerlink
iface peerlink
    bond-slaves swp49 swp50
    bond-mode 802.3ad
    bond-lacp-bypass-allow no
auto peerlink.4094
iface peerlink.4094
    clagd-peer-ip linklocal
    clagd-backup-ip 10.10.10.1
    clagd-sys-mac 44:38:39:BE:EF:AA
    clagd-args --initDelay 180
auto vlan10
iface vlan10
    hwaddress 44:38:39:22:01:af
    vlan-raw-device br_default
    vlan-id 10
auto vlan20
iface vlan20
    hwaddress 44:38:39:22:01:af
    vlan-raw-device br_default
    vlan-id 20
auto vxlan48
iface vxlan48
    bridge-vlan-vni-map 10=10 20=20
    bridge-learning off
auto br_default
iface br_default
    bridge-ports bond1 peerlink vxlan48
    hwaddress 44:38:39:22:01:af
    bridge-vlan-aware yes
    bridge-vids 10 20
```

{{< /tab >}}
{{< tab "leaf03 ">}}

```
cumulus@leaf03:~$ sudo cat /etc/network/interfaces
...
auto lo
iface lo inet loopback
    address 10.10.10.3/32
    clagd-vxlan-anycast-ip 10.0.1.34
    vxlan-local-tunnelip 10.10.10.3
auto mgmt
iface mgmt
    address 127.0.0.1/8
    address ::1/128
    vrf-table auto
auto eth0
iface eth0 inet dhcp
    ip-forward off
    ip6-forward off
    vrf mgmt
auto swp1
iface swp1
auto swp49
iface swp49
auto swp50
iface swp50
auto swp51
iface swp51
auto swp52
iface swp52
auto bond1
iface bond1
    bond-slaves swp1
    bond-mode 802.3ad
    bond-lacp-bypass-allow no
    clag-id 1
auto peerlink
iface peerlink
    bond-slaves swp49 swp50
    bond-mode 802.3ad
    bond-lacp-bypass-allow no
auto peerlink.4094
iface peerlink.4094
    clagd-peer-ip linklocal
    clagd-backup-ip 10.10.10.4
    clagd-sys-mac 44:38:39:BE:EF:AA
    clagd-args --initDelay 180
auto vlan10
iface vlan10
    hwaddress 44:38:39:22:01:bb
    vlan-raw-device br_default
    vlan-id 10
auto vlan20
iface vlan20
    hwaddress 44:38:39:22:01:bb
    vlan-raw-device br_default
    vlan-id 20
auto vxlan48
iface vxlan48
    bridge-vlan-vni-map 10=10 20=20
    bridge-learning off
auto br_default
iface br_default
    bridge-ports bond1 peerlink vxlan48
    hwaddress 44:38:39:22:01:bb
    bridge-vlan-aware yes
    bridge-vids 10 20
```

{{< /tab >}}
{{< tab "leaf04 ">}}

```
cumulus@leaf04:~$ sudo cat /etc/network/interfaces
...
auto lo
iface lo inet loopback
    address 10.10.10.4/32
    clagd-vxlan-anycast-ip 10.0.1.34
    vxlan-local-tunnelip 10.10.10.4
auto mgmt
iface mgmt
    address 127.0.0.1/8
    address ::1/128
    vrf-table auto
auto eth0
iface eth0 inet dhcp
    ip-forward off
    ip6-forward off
    vrf mgmt
auto swp1
iface swp1
auto swp49
iface swp49
auto swp50
iface swp50
auto swp51
iface swp51
auto swp52
iface swp52
auto bond1
iface bond1
    bond-slaves swp1
    bond-mode 802.3ad
    bond-lacp-bypass-allow no
    clag-id 1
auto peerlink
iface peerlink
    bond-slaves swp49 swp50
    bond-mode 802.3ad
    bond-lacp-bypass-allow no
auto peerlink.4094
iface peerlink.4094
    clagd-peer-ip linklocal
    clagd-backup-ip 10.10.10.3
    clagd-sys-mac 44:38:39:BE:EF:BB
    clagd-args --initDelay 180
auto vlan10
iface vlan10
    hwaddress 44:38:39:22:01:c1
    vlan-raw-device br_default
    vlan-id 10
auto vlan20
iface vlan20
    hwaddress 44:38:39:22:01:c1
    vlan-raw-device br_default
    vlan-id 20
auto vxlan48
iface vxlan48
    bridge-vlan-vni-map 10=10 20=20
    bridge-learning off
auto br_default
iface br_default
    bridge-ports bond1 peerlink vxlan48
    hwaddress 44:38:39:22:01:c1
    bridge-vlan-aware yes
    bridge-vids 10 20
```

{{< /tab >}}
{{< tab "spine01 ">}}

```
cumulus@spine01:~$ sudo cat /etc/network/interfaces
...
auto lo
iface lo inet loopback
    address 10.10.10.101/32
auto mgmt
iface mgmt
    address 127.0.0.1/8
    address ::1/128
    vrf-table auto
auto eth0
iface eth0 inet dhcp
    ip-forward off
    ip6-forward off
    vrf mgmt
auto swp1
iface swp1
auto swp2
iface swp2
auto swp3
iface swp3
auto swp4
iface swp4
```

{{< /tab >}}
{{< tab "spine02 ">}}

```
cumulus@spine02:~$ sudo cat /etc/network/interfaces
...
auto lo
iface lo inet loopback
    address 10.10.10.102/32
auto mgmt
iface mgmt
    address 127.0.0.1/8
    address ::1/128
    vrf-table auto
auto eth0
iface eth0 inet dhcp
    ip-forward off
    ip6-forward off
    vrf mgmt
auto swp1
iface swp1
auto swp2
iface swp2
auto swp3
iface swp3
auto swp4
iface swp4
```

{{< /tab >}}
{{< tab "server01 ">}}

```
auto lo
iface lo inet loopback

auto lo
iface lo inet static
  address 10.0.0.31/32
  
auto eth0
iface eth0 inet dhcp

auto eth1
iface eth1 inet manual
    bond-master bond1

auto eth2
iface eth2 inet manual
    bond-master bond1

auto bond1
iface bond1 inet static
  bond-slaves none
  bond-miimon 100
  bond-min-links 1
  bond-mode 802.3ad
  bond-xmit-hash-policy layer3+4
  bond-lacp-rate 1
  address 172.16.1.101/24

auto bond1.10
iface bond1.10 inet static
  address 172.16.10.101/24
  
auto bond1.20
iface bond1.20 inet static
  address 172.16.20.101/24
```

{{< /tab >}}
{{< tab "server03 ">}}

```
auto lo
iface lo inet loopback

auto lo
iface lo inet static
  address 10.0.0.33/32
  
auto eth0
iface eth0 inet dhcp

auto eth1
iface eth1 inet manual
    bond-master bond0

auto eth2
iface eth2 inet manual
    bond-master bond0

auto bond1
iface bond1 inet static
  bond-slaves none
  bond-miimon 100
  bond-min-links 1
  bond-mode 802.3ad
  bond-xmit-hash-policy layer3+4
  bond-lacp-rate 1
  address 172.16.1.103/24

auto bond1.10
iface bond1.10 inet static
  address 172.16.10.103/24
  
auto bond1.20
iface bond1.20 inet static
  address 172.16.20.103/24
```

{{< /tab >}}
{{< /tabs >}}

{{< /tab >}}
{{< /tabs >}}
