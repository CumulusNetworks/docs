---
title: Comparing Common Layer 2 Configurations to Arista and Cisco
author: NVIDIA
weight: 511
toc: 4
---

The configuration of layer 2 networking in Cumulus Linux (or any Linux distribution for that matter) is different from the incumbent network operating systems like Cisco\'s NX-OS or Arista\'s EOS. This article details some of the syntax differences using common layer 2 examples.
<!-- vale off -->
## Configuring Trunks
<!-- vale on -->
Configuring trunks with two VLANs on ports 1 and 2:

{{<img src="/images/knowledge-base/Compare-Common-L2-config-trunks.png" width="400">}}

| Cumulus Linux | Cisco NX-OS | Arista EOS |
| ------------- | ----------- | ---------- |
| <pre>auto bridge<br>iface bridge<br>  bridge-vlan-aware yes<br>  bridge-ports glob swp1-2<br>  bridge-vids 100 200</pre> | <pre>vlan 100,200<br><br>interface ethernet 1/1<br>    switchport mode trunk<br><br>interface ethernet 1/2<br>    switchport mode trunk</pre>      |     <pre>!<br>vlan 100,200<br>!<br>interface Ethernet1<br>    switchport mode trunk<br>!<br>interface Ethernet2<br>    switchport mode trunk</pre> |

## Pruning a Trunk

Pruning VLAN 100 from the trunk on port 1:

{{<img src="/images/knowledge-base/Compare-Common-L2-prune-trunks.png" width="400">}}

| Cumulus Linux | Cisco NX-OS | Arista EOS |
| ------------- | ----------- | ---------- |
| <pre>auto bridge<br>iface bridge<br>  bridge-vlan-aware yes<br>  bridge-ports glob swp1-2<br>  bridge-vids 100 200<br><br>auto swp1<br>iface swp1<br>  bridge-vids 200</pre> | <pre>vlan 100,200<br><br>interface ethernet 1/1<br>    switchport mode trunk<br>    switchport trunk allowed vlan 200<br><br>interface ethernet 1/2<br>    switchport mode trunk</pre>      |     <pre>!<br>vlan 100,200<br>!<br>interface Ethernet1<br>    switchport mode trunk<br>!<br>interface Ethernet2<br>    switchport mode trunk<br>    switchport trunk allowed vlan 200</pre> |
<!-- vale off -->
## Configuring Access Ports
<!-- vale on -->
Configuring two VLANs in access mode: port 1 VLAN 100 and port 2 VLAN 200:

{{<img src="/images/knowledge-base/Compare-Common-L2-config-access-ports.png" width="300">}}

| Cumulus Linux | Cisco NX-OS | Arista EOS |
| ------------- | ----------- | ---------- |
| <pre>auto bridge<br>iface bridge<br>  bridge-vlan-aware yes<br>  bridge-ports glob swp1-2<br>  bridge-vids 100 200<br><br>auto swp1<br>iface swp1<br>  bridge-access 100<br><br>auto swp2<br>iface swp2<br>  bridge-access 200</pre> | <pre>vlan 100,200<br><br>interface ethernet 1/1<br>    switchport mode access<br>    switchport access vlan 100<br><br>interface ethernet 1/2<br>    switchport mode access<br>    switchport access vlan 200</pre>      |     <pre>!<br>vlan 100,200<br>!<br>interface Ethernet1<br>    switchport access vlan 100<br>!<br>interface Ethernet2<br>    switchport access vlan 200</pre> |

## Changing the Native (Untagged) VLAN for a Single Trunk

Setting the native VLAN to 100 on port 1 and 200 on port 2 when both ports are trunks allowing VLAN 1-200:

{{<img src="/images/knowledge-base/Compare-Common-L2-change-native-VLAN.png" width="400">}}

| Cumulus Linux | Cisco NX-OS | Arista EOS |
| ------------- | ----------- | ---------- |
| <pre>auto bridge<br>iface bridge<br>  bridge-vlan-aware yes<br>  bridge-ports glob swp1-2<br>  bridge-vids 1-200<br><br>auto swp1<br>iface swp1<br>  bridge-pvid 100<br><br>auto swp2<br>iface swp2<br>  bridge-pvid 200</pre> | <pre>vlan 1-200<br><br>interface ethernet 1/1-2<br>    switchport mode trunk<br>    switchport trunk allowed vlan 1-200<br><br>interface ethernet 1/1<br>    switchport trunk native vlan 100<br><br>interface ethernet 1/2<br>    switchport trunk native vlan 200</pre>      |     <pre>!<br>vlan 1-200<br>!<br>interface Ethernet1<br>    switchport mode trunk<br>    switchport trunk native vlan 100<br>!<br>interface Ethernet2<br>    switchport mode trunk<br>    switchport trunk native vlan 200</pre> |

## See Also

- {{<link title="Bond Interoperability with Cisco and Arista Switches">}}
- {{<link url="Cumulus-Linux-Conversion-Guide-for-NX-OS-or-IOS-Users">}}
