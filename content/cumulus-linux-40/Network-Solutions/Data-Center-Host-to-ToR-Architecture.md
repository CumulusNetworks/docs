---
title: Data Center Host to ToR Architecture
author: NVIDIA
weight: 1140
toc: 3
---
This chapter discusses the various architectures and strategies available from the top of rack (ToR) switches all the way down to the server hosts.

## Layer 2 - Traditional Spanning Tree - Single Attached

|<div style="width:300px">Example| Summary |
|--------------------------------|----------------|
| {{< img src = "/images/cumulus-linux/network-solutions-dc-host-to-tor.png">}}| {{<link url="Bonding-Link-Aggregation" text="Bond">}} and Etherchannel are not configured on host to multiple switches (bonds can still occur but only to one switch at a time), so leaf01 and leaf02 see two different MAC addresses.|

| <div style="width:300px">Benefits | Caveats |
|----------|---------|
|<ul><li>Established technology: Interoperability with other vendors, easy configuration, a lot of documentation from multiple vendors and the industry</li><li>Ability to use {{<link url="Spanning-Tree-and-Rapid-Spanning-Tree" text="spanning tree">}} commands: {{<link url="Spanning-Tree-and-Rapid-Spanning-Tree#portadminedge-portfast-mode" text="PortAdminEdge">}} and {{<link url="Spanning-Tree-and-Rapid-Spanning-Tree#bpdu-guard" text="BPDU guard">}}</li><li>Layer 2 reachability to all VMs</li></ul>|<ul><li>The load balancing mechanism on the host can cause problems. If there is only host pinning to each NIC, there are no problems, but if you have a bond, you need to look at an MLAG solution.</li><li>No active-active host links. Some operating systems allow HA (NIC failover), but this still does not utilize all the bandwidth. VMs use one NIC, not two.</li></ul>|

| <div style="width:130px">Active-Active Mode | <div style="width:130px">Active-Passive Mode | L2 to L3 Demarcation|
|---------------------|--------------------|---------------------|
| None (not possible with traditional spanning tree) | {{<link url="Virtual-Router-Redundancy-VRR-and-VRRP" text="VRR">}} | <ul><li>ToR layer (recommended)</li><li>Spine layer</li><li>Core/edge/exit</li></ul><br>You can configure VRR on a pair of switches at any level in the network. However, the higher up the network, the larger the layer 2 domain becomes. The benefit is layer 2 reachability. The drawback is that the layer 2 domain is more difficult to troubleshoot, does not scale as well, and the pair of switches running VRR needs to carry the entire MAC address table of everything below it in the network. Cumulus Professional Services recommends minimizing the layer 2 domain as much as possible. For more information, see {{<exlink url="https://docs.google.com/presentation/d/1l1d_6iUF7RTUHTSAmGuLwm3WCUXTNdFjndCLLxzBSOU/edit?usp=sharing" text="this presentation">}}.|

**Example Configuration**

{{< tabs "TabID0" >}}

{{< tab "leaf01" >}}

```
auto bridge
iface bridge
  bridge-vlan-aware yes
  bridge-ports swp1 peerlink
  bridge-vids 1-2000
  bridge-stp on

auto bridge.10
iface bridge.10
  address 10.1.10.2/24

auto peerlink
iface peerlink
    bond-slaves glob swp49-50

auto swp1
iface swp1
  mstpctl-portadminedge yes
  mstpctl-bpduguard yes
```

{{< /tab >}}

{{< tab "Ubuntu host" >}}

```
auto eth1
iface eth1 inet manual

auto eth1.10
iface eth1.10 inet manual

auto eth2
iface eth1 inet manual

auto eth2.20
iface eth2.20 inet manual

auto br-10
iface br-10 inet manual
  bridge-ports eth1.10 vnet0

auto br-20
iface br-20 inet manual
  bridge-ports eth2.20 vnet1
```

{{< /tab >}}

{{< /tabs >}}

## Layer 2 - MLAG

| <div style="width:300px">Example | Summary |
|----|----|
|{{< img src = "/images/cumulus-linux/network-solutions-mlag.png" >}} | {{<link url="Multi-Chassis-Link-Aggregation-MLAG" text="MLAG (multi-chassis link aggregation)">}} uses both uplinks at the same time. VRR enables both spines to act as gateways simultaneously for HA (high availability) and {{<link url="VXLAN-Active-Active-Mode" text="active-active mode">}} (both are used at the same time). |

| <div style="width:300px">Benefits | Caveats |
|----------| --------|
| 100% of links utilized | <ul><li>More complicated (more moving parts) </li><li>More configuration</li><li>No interoperability between vendors</li><li>ISL (inter-switch link) required</li></ul> |

| Active-Active Mode | Active-Passive Mode | L2 to L3 Demarcation| More Information|
|---------------------|--------------------|---------------------|-----------------|
| {{<link url="Virtual-Router-Redundancy-VRR-and-VRRP" text="VRR">}}| None | <ul><li>ToR layer (recommended)</li><li>Spine layer</li><li>Core/edge/exit</li><ul>|<ul><li>Can be done with either the {{<link url="Traditional-Bridge-Mode" text="traditional">}} or {{<link url="VLAN-aware-Bridge-Mode" text="VLAN-aware">}} bridge driver depending on overall STP needs.</li><li>There are a few different solutions including Cisco VPC and Arista MLAG, but none of them interoperate and are very vendor specific.</li><li>{{<exlink url="https://resource.nvidia.com/en-us-ethernet-switching/bgp-evpn-for-vxlan-techincal-overview" text="Cumulus Networks Layer 2 HA validated design guide">}}.</li></ul>|

**Example Configuration**

{{< tabs "TabID2" >}}

{{< tab "leaf01" >}}

```
auto bridge
iface bridge
  bridge-vlan-aware yes
  bridge-ports host-01 peerlink
  bridge-vids 1-2000
  bridge-stp on

auto bridge.10
iface bridge.10
  address 172.16.1.2/24
  address-virtual 44:38:39:00:00:10 172.16.1.1/24

auto peerlink
iface peerlink
    bond-slaves glob swp49-50

auto peerlink.4094
iface peerlink.4094
    address 169.254.1.1/30
    clagd-enable yes
    clagd-peer-ip 169.254.1.2
    clagd-system-mac 44:38:39:FF:40:94

auto host-01
iface host-01
  bond-slaves swp1
  clag-id 1
  {bond-defaults removed for brevity}
```

{{< /tab >}}

{{< tab "Ubuntu host" >}}

```
auto bond0
iface bond0 inet manual
  bond-slaves eth0 eth1
  {bond-defaults removed for brevity}

auto bond0.10
iface bond0.10 inet manual

auto vm-br10
iface vm-br10 inet manual
  bridge-ports bond0.10 vnet0
```

{{< /tab >}}

{{< /tabs >}}

## Layer 3 - Single-attached Hosts

| <div style="width:300px">Example| Summary|
|----|----|
|{{< img src = "/images/cumulus-linux/network-solutions-single-attached.png" >}} | The server (physical host) has only has one link to one ToR switch. |

| <div style="width:300px">Benefits | Caveats |
|----------| --------|
| <ul><li>Relatively simple network configuration</li><li>No STP</li><li>No MLAG</li><li>No layer 2 loops</li><li>No crosslink between leafs</li><li>Greater route scaling and flexibility</li></ul>| <ul><li>No redundancy for ToR, upgrades can cause downtime</li><li>There is often no software to support application layer redundancy</li><ul>|

| <div style="width:300px">FHR (First Hop Redundancy) | More Information |
|----------| --------|
| No redundancy for ToR, uses single ToR as gateway.| For additional bandwidth, links between host and leaf can be bonded. |

**Example Configuration**

{{< tabs "TabID4" >}}

{{< tab "leaf01" >}}

`/etc/network/interfaces` file

```
auto swp1
iface swp1
  address 172.16.1.1/30
```

`/etc/frr/frr.conf` file

```
router ospf
  router-id 10.0.0.11
interface swp1
  ip ospf area 0
```

{{< /tab >}}

{{< tab "leaf02" >}}

`/etc/network/interfaces` file

```
auto swp1
iface swp1
  address 172.16.2.1/30
```

`/etc/frr/frr.conf` file

```
router ospf
  router-id 10.0.0.12
interface swp1
  ip ospf area 0
```

{{< /tab >}}

{{< tab "Ubuntu host1" >}}

```
auto eth1
iface eth1 inet static
  address 172.16.1.2/30
  up ip route add 0.0.0.0/0 nexthop via 172.16.1.1
```

{{< /tab >}}

{{< tab "Ubuntu host2" >}}

```
auto eth1
iface eth1 inet static
  address 172.16.2.2/30
  up ip route add 0.0.0.0/0 nexthop via 172.16.2.1
```

{{< /tab >}}

{{< /tabs >}}

## Layer 3 - Redistribute Neighbor

|<div style="width:300px">Example| Summary |
|----|----|
|{{< img src = "/images/cumulus-linux/network-solutions-redis-neighbor.png" >}} | The {{<link url="Redistribute-Neighbor" text="Redistribute neighbor">}} daemon grabs ARP entries dynamically and uses the redistribute table for FRRouting to take these dynamic entries and redistribute them into the fabric. |

| <div style="width:300px">Benefits | Caveats |
|-----------------------------------| --------|
| Configuration in FRRouting is simple (route map plus redistribute table) | <ul><li>Silent hosts do not receive traffic (depending on ARP) </li><li>IPv4 only</li><li>If two VMs are on the same layer 2 domain, they can learn about each other directly instead of using the gateway, which causes problems (such as VM migration or getting the network routed). Put hosts on /32 (no other layer 2 adjacency).</li><li>VM moves do not trigger a route withdrawal from the original leaf (four hour timeout).</li><li>Clearing ARP impacts routing.</li><li>No layer 2 adjacency between servers without VXLAN.</li></ul> |

| FHR (First Hop Redundancy) | More Information |
| ---------------------------|------------------|
|<ul><li>Equal cost route installed on server, host, or hypervisor to both ToRs to load balance evenly.</li><li>For host/VM/container mobility, use the same default route on all hosts (such as x.x.x.1) but do not distribute or advertise the .1 on the ToR into the fabric. This allows the VM to use the same gateway no matter to which pair of leafs it is cabled.| |

## Layer 3 - Routing on the Host

|<div style="width:300px">Example| Summary |
|--------------------------------|-----------|
| {{< img src = "/images/cumulus-linux/network-solutions-routing-on-host.png" >}} | Routing on the host means there is a routing application (such as {{<link url="FRRouting-Overview" text="FRRouting">}}, either on the bare metal host (no VMs or containers) or the hypervisor (for example, Ubuntu with KVM). This is highly recommended by the our Professional Services team. |

| <div style="width:300px">Benefits | Caveats |
|-----------------------------------| --------|
| <ul><li>No requirement for MLAG</li><li>No spanning tree or layer 2 domain</li><li>No loops</li><li>You can use three or more ToRs instead of the usual two</li><li>Host and VM mobility</li><li>You can use traffic engineering to migrate traffic from one ToR to another when upgrading both hardware and software</li></ul>| <ul><li>The hypervisor or host OS might not support a routing application like FRRouting and requires a virtual router on the hypervisor</li><li>No layer 2 adjacnecy between servers without VXLAN</li></ul>|

| <div style="width:300px">FHR (First Hop Redundancy) | More Information |
| ---------------------------|------------------|
|<ul><li>The first hop is still the ToR, just like redistribute neighbor</li><li>A default route can be advertised by all leaf/ToRs for dynamic ECMP paths</li></ul>|<ul><li>{{<exlink url="http://docs.frrouting.org/en/latest/installation.html" text="Installing the FRRouting Package on an Ubuntu Server">}}</li><li>{{<link url="Configuring-FRRouting">}}</li></ul>|

## Layer 3 - Routing on the VM

|<div style="width:300px">Example|Summary|
|----|----|
| {{< img src = "/images/cumulus-linux/network-solutions-routing-vm.png" >}} | Instead of routing on the hypervisor, each virtual machine uses its own routing stack. |

| <div style="width:300px">Benefits | Caveats |
|-----------------------------------| --------|
| In addition to routing on host:<ul><li> The hypervisor/base OS does not need to be able to do routing.</li><li>VMs can be authenticated into routing fabric.</li></ul> |<ul><li>All VMs must be capable of routing</li><li>You need to take scale considerations into an account; instead of one routing process, there are as many as there are VMs</li><li>No layer 2 adjacency between servers without VXLAN</li></ul>|

| <div style="width:300px">FHR (First Hop Redundancy) | More Information |
| ---------------------------|------------------|
| <ul><li>The first hop is still the ToR, just like redistribute neighbor</li><li>You can use multiple ToRs (two or more)</li><ul>|<ul><li>{{<exlink url="http://docs.frrouting.org/en/latest/installation.html" text="Installing the FRRouting Package on an Ubuntu Server">}}</li><li>{{<link url="Configuring-FRRouting">}}</li><ul>|

## Layer 3 - Virtual Router

|<div style="width:300px">Example | Summary |
|----|----|
| {{< img src = "/images/cumulus-linux/network-solutions-vrouter.png" >}} | Virtual router (vRouter) runs as a VM on the hypervisor or host and sends routes to the ToR using {{<link url="Border-Gateway-Protocol-BGP" text="BGP">}} or {{<link url="Open-Shortest-Path-First-OSPF" text="OSPF">}}. |

| <div style="width:300px">Benefits | Caveats |
|-----------------------------------| --------|
|In addition to routing on a host:<ul><li>Multi-tenancy can work, where multiple customers share the same racks</li><li>The base OS does not need to be routing capable</li></ul>|<ul><li>{{<link url="Equal-Cost-Multipath-Load-Sharing-Hardware-ECMP" text="ECMP">}} might not work correctly (load balancing to multiple ToRs); the Linux kernel in older versions is not capable of ECMP per flow (it does it per packet)</li><li>No layer 2 adjacency between servers without VXLAN</li></ul>|

| <div style="width:300px">FHR (First Hop Redundancy) | More Information |
| ---------------------------|------------------|
|<ul><li>The gateway is the vRouter, which has two routes out (two ToRs)</li><li>You can use multiple vRouters</li></ul>|<ul><li>{{<exlink url="http://docs.frrouting.org/en/latest/installation.html" text="Installing the FRRouting Package on an Ubuntu Server">}}</li><li>{{<link url="Configuring-FRRouting">}}</li></ul>|

## Layer 3 - Anycast with Manual Redistribution

|<div style="width:300px">Example | Summary |
|----|----|
| {{< img src = "/images/cumulus-linux/network-solutions-anycast-router.png" >}} | In contrast to routing on the host (preferred), this method allows you to route **to** the host. The ToRs are the gateway, as with redistribute neighbor, except because there is no daemon running, you must manually configure the networks under the routing process. There is a potential to black hole unless you run a script to remove the routes when the host no longer responds. |

| <div style="width:300px">Benefits | Caveats |
|-----------------------------------| --------|
| <ul><li>Most benefits of routing **on** the host</li><li>No requirement for host to run routing</li><li>No requirement for redistribute neighbor</li></ul>|<ul><li>Removing a subnet from one ToR and re-adding it to another (network statements from your router process) is a manual process</li><li>Network team and server team have to be in sync, or the server team controls the ToR, or automation is used used whenever VM migration occurs</li><li>When using VMs or containers it is very easy to black hole traffic, as the leafs continue to advertise prefixes even when the VM is down</li><li>No layer 2 adjacency between servers without VXLAN</li></ul>|

| FHR (First Hop Redundancy) |
| ---------------------------|
|The gateways are the ToRs, exactly like redistribute neighbor with an equal cost route installed.|

**Example Configuration**

{{< tabs "TabID8" >}}

{{< tab "leaf01" >}}

`/etc/network/interfaces file`

```
auto swp1
iface swp1
  address 172.16.1.1/30
```

`/etc/frr/frr.conf` file

```
router ospf
  router-id 10.0.0.11
interface swp1
  ip ospf area 0
```

{{< /tab >}}

{{< tab "leaf02" >}}

`/etc/network/interfaces` file

```
auto swp2
iface swp2
  address 172.16.1.1/30
```

`/etc/frr/frr.conf` file

```
router ospf
  router-id 10.0.0.12
interface swp1
  ip ospf area 0
```

{{< /tab >}}

{{< tab "Ubuntu host" >}}

```
auto lo
iface lo inet loopback

auto lo:1
iface lo:1 inet static
  address 172.16.1.2/32
  up ip route add 0.0.0.0/0 nexthop via 172.16.1.1 dev eth0 onlink nexthop via 172.16.1.1 dev eth1 onlink

auto eth1
iface eth2 inet static
  address 172.16.1.2/32

auto eth2
iface eth2 inet static
  address 172.16.1.2/32
```

{{< /tab >}}

{{< /tabs >}}

## Layer 3 - EVPN with Symmetric VXLAN Routing

{{<link url="VXLAN-Routing" text="Symmetric VXLAN routing">}} is configured directly on the ToR, using {{<link url="Ethernet-Virtual-Private-Network-EVPN" text="EVPN">}} for both VLAN and VXLAN bridging as well as VXLAN and external routing.

{{< img src = "/images/cumulus-linux/network-solutions-evpn-symmetric.png" >}}

Each server is configured on a VLAN, with a total of two VLANs for the setup. MLAG is also set up between servers and the leafs. Each leaf is configured with an anycast gateway and the servers default gateways are pointing towards the corresponding leaf switch IP gateway address. Two tenant VNIs (corresponding to two VLANs/VXLANs) are bridged to corresponding VLANs.

| <div style="width:300px">Benefits | Caveats |
|-----------------------------------| --------|
| <ul><li>Layer 2 domain is reduced to the pair of ToRs</li><li>Aggregation layer is all layer 3 (VLANs do not have to exist on spine switches)</li><li>Greater route scaling and flexibility</li><li>High availability</li></ul>| Needs MLAG (with the same caveats as the {{<link url="#mlag" text="MLAG">}} section above)|

|Active-Active Mode|Active-Passive Mode|Demarcation| More Information|
|------------------|-------------------|------------|-------------|
| {{<link url="Virtual-Router-Redundancy-VRR-and-VRRP" text="VRR">}} |None|ToR layer|<ul><li>{{<exlink url="https://github.com/CumulusNetworks/cldemo-evpn-symmetric" text="Cumulus Networks EVPN with symmetric routing demo on GitHub">}}</li><li>{{<link url="Ethernet-Virtual-Private-Network-EVPN" text="Ethernet Virtual Private Network - EVPN">}}</li><li>{{<link url="VXLAN-Routing">}}</li></ul>|

**Example Configuration**

{{< tabs "TabID11" >}}

{{< tab "leaf01" >}}

```
# Loopback interface
auto lo
iface lo inet loopback
  address 10.0.0.11/32
  clagd-vxlan-anycast-ip 10.0.0.112
  alias loopback interface

# Management interface
 auto eth0
 iface eth0 inet dhcp
    vrf mgmt

auto mgmt
iface mgmt
    address 127.0.0.1/8
    address ::1/128
    vrf-table auto

# Port to Server01
auto swp1
iface swp1
  alias to Server01
  # This is required for Vagrant only
  post-up ip link set swp1 promisc on

# Port to Server02
auto swp2
iface swp2
  alias to Server02
  # This is required for Vagrant only
  post-up ip link set swp2 promisc on

# Port to Leaf02
auto swp49
iface swp49
  alias to Leaf02
  # This is required for Vagrant only
  post-up ip link set swp49 promisc on

# Port to Leaf02
auto swp50
iface swp50
  alias to Leaf02
  # This is required for Vagrant only
  post-up ip link set swp50 promisc on

# Port to Spine01
auto swp51
iface swp51
  mtu 9216
  alias to Spine01

# Port to Spine02
auto swp52
iface swp52
  mtu 9216
  alias to Spine02

# MLAG Peerlink bond
auto peerlink
iface peerlink
  mtu 9000
  bond-slaves swp49 swp50

# MLAG Peerlink L2 interface.
# This creates VLAN 4094 that only lives on the peerlink bond
# No other interface will be aware of VLAN 4094
auto peerlink.4094
iface peerlink.4094
  address 169.254.1.1/30
  clagd-peer-ip 169.254.1.2
  clagd-backup-ip 10.0.0.12
  clagd-sys-mac 44:39:39:ff:40:94
  clagd-priority 100

# Bond to Server01
auto bond01
iface bond01
  mtu 9000
  bond-slaves swp1
  bridge-access 13
  clag-id 1

# Bond to Server02
auto bond02
iface bond02
  mtu 9000
  bond-slaves swp2
  bridge-access 24
  clag-id 2

# Define the bridge for STP
auto bridge
iface bridge
  bridge-vlan-aware yes
  # bridge-ports includes all ports related to VxLAN and CLAG.
  # does not include the Peerlink.4094 subinterface
  bridge-ports bond01 bond02 peerlink vni13 vni24 vxlan4001
  bridge-vids 13 24
  bridge-pvid 1

# VXLAN Tunnel for Server1-Server3 (Vlan 13)
auto vni13
iface vni13
  mtu 9000
  vxlan-id 13
  vxlan-local-tunnelip 10.0.0.11
  bridge-access 13
  mstpctl-bpduguard yes
  mstpctl-portbpdufilter yes

#VXLAN Tunnel for Server2-Server4 (Vlan 24)
auto vni24
iface vni24
  mtu 9000
  vxlan-id 24
  vxlan-local-tunnelip 10.0.0.11
  bridge-access 24
  mstpctl-bpduguard yes
  mstpctl-portbpdufilter yes

auto vxlan4001
iface vxlan4001
    vxlan-id 104001
    vxlan-local-tunnelip 10.0.0.11
    bridge-access 4001

auto vrf1
iface vrf1
   vrf-table auto

#Tenant SVIs - anycast GW
auto vlan13
iface vlan13
    address 10.1.3.11/24
    address-virtual 44:39:39:ff:00:13 10.1.3.1/24
    vlan-id 13
    vlan-raw-device bridge
    vrf vrf1

auto vlan24
iface vlan24
    address 10.2.4.11/24
    address-virtual 44:39:39:ff:00:24 10.2.4.1/24
    vlan-id 24
    vlan-raw-device bridge
    vrf vrf1

#L3 VLAN interface per tenant (for L3 VNI)
auto vlan4001
iface vlan4001
    hwaddress 44:39:39:FF:40:94
    vlan-id 4001
    vlan-raw-device bridge
    vrf vrf1
```

{{< /tab >}}

{{< tab "Leaf02" >}}

```
# Loopback interface
auto lo
iface lo inet loopback
  address 10.0.0.12/32
  clagd-vxlan-anycast-ip 10.0.0.112
  alias loopback interface

# Management interface
auto eth0
iface eth0 inet dhcp
    vrf mgmt

auto mgmt
iface mgmt
    address 127.0.0.1/8
    address ::1/128
    vrf-table auto

# Port to Server01
auto swp1
iface swp1
  alias to Server01
  # This is required for Vagrant only
  post-up ip link set swp1 promisc on

# Port to Server02
auto swp2
iface swp2
  alias to Server02
  # This is required for Vagrant only
  post-up ip link set swp2 promisc on

# Port to Leaf01
auto swp49
iface swp49
  alias to Leaf01
  # This is required for Vagrant only
  post-up ip link set swp49 promisc on

# Port to Leaf01
auto swp50
iface swp50
  alias to Leaf01
  # This is required for Vagrant only
  post-up ip link set swp50 promisc on

# Port to Spine01
auto swp51
iface swp51
  mtu 9216
  alias to Spine01

# Port to Spine02
auto swp52
iface swp52
  mtu 9216
  alias to Spine02

# MLAG Peerlink bond
auto peerlink
iface peerlink
  mtu 9000
  bond-slaves swp49 swp50

# MLAG Peerlink L2 interface.
# This creates VLAN 4094 that only lives on the peerlink bond
# No other interface will be aware of VLAN 4094
auto peerlink.4094
iface peerlink.4094
  address 169.254.1.2/30
  clagd-peer-ip 169.254.1.1
  clagd-backup-ip 10.0.0.11
  clagd-sys-mac 44:39:39:ff:40:94
  clagd-priority 200

# Bond to Server01
auto bond01
iface bond01
  mtu 9000
  bond-slaves swp1
  bridge-access 13
  clag-id 1

# Bond to Server02
auto bond02
iface bond02
  mtu 9000
  bond-slaves swp2
  bridge-access 24
  clag-id 2

# Define the bridge for STP
auto bridge
iface bridge
  bridge-vlan-aware yes
  # bridge-ports includes all ports related to VxLAN and CLAG.
  # does not include the Peerlink.4094 subinterface
  bridge-ports bond01 bond02 peerlink vni13 vni24 vxlan4001
  bridge-vids 13 24
  bridge-pvid 1

auto vxlan4001
iface vxlan4001
     vxlan-id 104001
     vxlan-local-tunnelip 10.0.0.12
     bridge-access 4001

# VXLAN Tunnel for Server1-Server3 (Vlan 13)
auto vni13
iface vni13
  mtu 9000
  vxlan-id 13
  vxlan-local-tunnelip 10.0.0.12
  bridge-access 13
  mstpctl-bpduguard yes
  mstpctl-portbpdufilter yes

#VXLAN Tunnel for Server2-Server4 (Vlan 24)
auto vni24
iface vni24
  mtu 9000
  vxlan-id 24
  vxlan-local-tunnelip 10.0.0.12
  bridge-access 24
  mstpctl-bpduguard yes
  mstpctl-portbpdufilter yes

auto vrf1
iface vrf1
   vrf-table auto

auto vlan13
iface vlan13
    address 10.1.3.12/24
    address-virtual 44:39:39:ff:00:13 10.1.3.1/24
    vlan-id 13
    vlan-raw-device bridge
    vrf vrf1

auto vlan24
iface vlan24
    address 10.2.4.12/24
    address-virtual 44:39:39:ff:00:24 10.2.4.1/24
    vlan-id 24
    vlan-raw-device bridge
    vrf vrf1

#L3 VLAN interface per tenant (for L3 VNI)
auto vlan4001
iface vlan4001
    hwaddress 44:39:39:FF:40:94
    vlan-id 4001
    vlan-raw-device bridge
    vrf vrf1
```

{{< /tab >}}

{{< tab "Server01" >}}

```
auto lo
iface lo inet loopback

auto eth0
iface eth0 inet dhcp

auto eth1
iface eth1 inet manual
  bond-master uplink
  # Required for Vagrant
  post-up ip link set promisc on dev eth1

auto eth2
iface eth2 inet manual
  bond-master uplink
  # Required for Vagrant
  post-up ip link set promisc on dev eth2

auto uplink
iface uplink inet static
  mtu 9000
  bond-slaves none
  bond-mode 802.3ad
  bond-miimon 100
  bond-lacp-rate 1
  bond-min-links 1
  bond-xmit-hash-policy layer3+4
  address 10.1.3.101
  netmask 255.255.255.0
  post-up ip route add default via 10.1.3.1
```

{{< /tab >}}

{{< tab "Server02" >}}

```
auto lo
iface lo inet loopback

auto eth0
iface eth0 inet dhcp

auto eth1
iface eth1 inet manual
  bond-master uplink
  # Required for Vagrant
  post-up ip link set promisc on dev eth1

auto eth2
iface eth2 inet manual
  bond-master uplink
  # Required for Vagrant
  post-up ip link set promisc on dev eth2

auto uplink
iface uplink inet static
  mtu 9000
  bond-slaves none
  bond-mode 802.3ad
  bond-miimon 100
  bond-lacp-rate 1
  bond-min-links 1
  bond-xmit-hash-policy layer3+4
  address 10.2.4.102
  netmask 255.255.255.0
  post-up ip route add default via 10.2.4.1
```

{{< /tab >}}

{{< /tabs >}}
