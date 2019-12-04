---
title: Basic Configuration
author: Cumulus Networks
weight: 350
aliases:
 - /pages/viewpage.action?pageId=12910740
product: Cumulus Linux
version: '4.0'
---
The following sections provide the basic configuration needed to use EVPN as the control plane for VXLAN. The steps provided assume you have already configured VXLAN interfaces, attached them to a bridge, and mapped VLANs to VNIs.

{{%notice note%}}

In Cumulus Linux 4.0, MAC learning is disabled and ARP/ND supression is enabled by default. This is a change from earlier Cumulus Linux releases, where MAC learning is *enabled* and ARP/ND suppression *disabled* by default. Be sure to update any configuration scripts, if necessary.

{{%/notice%}}

## Enable EVPN between BGP Neighbors

To enable EVPN between [BGP](../../../Layer-3/Border-Gateway-Protocol-BGP/) neighbors, add the address family *evpn* to the existing neighbor `address-family` activation command.

For a non-VTEP device that is merely participating in EVPN route exchange, such as a spine switch where the network deployment uses hop-by-hop eBGP or the switch is acting as an iBGP route reflector, activating the interface for the EVPN address family is the fundamental configuration needed in [FRRouting](../../../Layer-3/FRRouting-Overview/).

The other BGP neighbor address family specific configurations supported for EVPN are `allowas-in` and `route-reflector-client`.

To configure an EVPN route exchange with a BGP peer, activate the peer or peer group within the EVPN address family. For example:

<details>

<summary>NCLU Commands </summary>

```
cumulus@switch:~$ net add bgp autonomous-system 65000
cumulus@switch:~$ net add bgp neighbor swp1 interface remote-as external
cumulus@switch:~$ net add bgp l2vpn evpn neighbor swp1 activate
cumulus@switch:~$ net pending
cumulus@switch:~$ net commit
```

</details>

<details>

<summary>vtysh Commands </summary>

```
cumulus@switch:~$ sudo vtysh

switch# configure terminal
switch(config)# router bgp 65011
switch(config-router)# neighbor swp1 interface remote-as external
switch(config-router)# address-family l2vpn evpn
switch(config-router-af)# neighbor swp1 activate
switch(config-router-af)# end
switch)# write memory
switch)# exit
cumulus@switch:~$ 
```

</details>

{{%notice note%}}

Adjust the `remote-as` above to be appropriate for your environment.

{{%/notice%}}

The above commands create the following configuration snippet in the `/etc/frr/frr.conf` file.

```
...
router bgp 65000
  neighbor swp1 interface remote-as external
  address-family l2vpn evpn
  neighbor swp1 activate
...
```

The above configuration does not result in BGP knowing about the local VNIs defined on the system and advertising them to peers. This requires additional configuration, described in [Advertise All VNIs](#advertise-all-vnis), below.

## Advertise All VNIs

FRR is not aware of any local VNIs and MACs, or hosts (neighbors) associated with those VNIs until you enable the BGP control plane for all VNIs configured on the switch by setting the `advertise-all-vni` option.

{{%notice note%}}

This configuration is only needed on leaf switches that are VTEPs. EVPN routes received from a BGP peer are accepted, even without this explicit EVPN configuration. These routes are maintained in the global EVPN routing table. However, they only become effective (imported into the per-VNI routing table and appropriate entries installed in the kernel) when the VNI corresponding to the received route is locally known.

{{%/notice%}}

<details>

<summary>NCLU Commands </summary>

```
cumulus@switch:~$ net add bgp l2vpn evpn advertise-all-vni
cumulus@switch:~$ net pending
cumulus@switch:~$ net commit
```

</details>

<details>

<summary>vtysh Commands </summary>

```
cumulus@switch:~$ sudo vtysh

switch# configure terminal
switch(config)# router bgp 65011
switch(config-router)# address-family l2vpn evpn 
switch(config-router-af)# advertise-all-vni
switch(config-router-af)# end
switch)# write memory
switch)# exit
cumulus@switch:~$
```

</details>

The above commands create the following configuration snippet in the `/etc/frr/frr.conf` file.

```
...
router bgp 65000
  neighbor swp1 interface remote-as external
  address-family l2vpn evpn
  neighbor swp1 activate
  advertise-all-vni
...
```

## Define RDs and RTs

When a local VNI is learned by FRR and there is no explicit configuration for that VNI in FRR, the route distinguisher (RD), and import and export route targets (RTs) for this VNI are automatically derived. The RD uses *RouterId:VNI-Index* and the import and export RTs use *AS:VNI*. The RD and RTs are used in the EVPN route exchange. The RD disambiguates EVPN routes in different VNIs (as they may have the same MAC and/or IP address) while the RTs describe the VPN membership for the route. The *VNI-Index* used for the RD is a unique, internally generated number for a VNI. It only has local significance; on remote switches, its only role is for route disambiguation. This number is used instead of the VNI value itself because this number has to be less than or equal to 65535. In the RT, the AS is always encoded as a 2-byte value to allow room for a large VNI. If the router has a 4-byte AS, only the lower 2 bytes are used. This ensures a unique RT for different VNIs while having the same RT for the same VNI across routers in the same AS.

For eBGP EVPN peering, the peers are in a different AS so using an automatic RT of *AS:VNI* does not work for route import. Therefore, the import RT is treated as *\*:VNI* to determine which received routes are applicable to a particular VNI. This only applies when the import RT is auto-derived and not configured.

If you do *not* want RDs and RTs to be derived automatically, you can define them manually. The following example commands are per VNI. You must specify these commands under `address-family l2vpn evpn` in BGP.

<details>

<summary>NCLU Commands </summary>

```
cumulus@switch:~$ net add bgp l2vpn evpn vni 10200 rd 172.16.100.1:20
cumulus@switch:~$ net add bgp l2vpn evpn vni 10200 route-target import 65100:20
cumulus@switch:~$ net add bgp l2vpn evpn advertise-all-vni
cumulus@switch:~$ net pending
cumulus@switch:~$ net commit
```

</details>

<details>

<summary>vtysh Commands </summary>

```
cumulus@switch:~$ sudo vtysh

switch# configure terminal
switch(config)# router bgp 65011
switch(config-router)# address-family l2vpn evpn
switch(config-router-af)# vni 10200
switch(config-router-af-vni)# rd 172.16.100.1:20
switch(config-router-af-vni)# route-target import 65100:20
switch(config-router-af-vni)# exit
switch(config-router-af)# advertise-all-vni
switch(config-router-af)# end
switch)# write memory
switch)# exit
cumulus@switch:~$
```

</details>

These commands create the following configuration snippet in the `/etc/frr/frr.conf` file.

``` 
...
address-family l2vpn evpn
  advertise-all-vni
  vni 10200
   rd 172.16.100.1:20
   route-target import 65100:20
...
```

{{%notice note%}}

If you delete the RD or RT later, it reverts back to its corresponding default value.

{{%/notice%}}

You can configure multiple RT values. In addition, you can configure both the import and export route targets with a single command by using `route-target both`:

<details>

<summary>NCLU Commands </summary>

```
cumulus@switch:~$ net add bgp l2vpn evpn vni 10400 route-target import 100:400
cumulus@switch:~$ net add bgp l2vpn evpn vni 10400 route-target import 100:500
cumulus@switch:~$ net add bgp l2vpn evpn vni 10500 route-target both 65000:500
cumulus@switch:~$ net pending
cumulus@switch:~$ net commit
```

</details>

<details>

<summary>vtysh Commands </summary>

```
cumulus@switch:~$ sudo vtysh

switch# configure terminal
switch(config)# router bgp 65011
switch(config-router)# address-family l2vpn evpn
switch(config-router-af)# vni 10400
switch(config-router-af-vni)# route-target import 100:400
switch(config-router-af-vni)# route-target import 100:500
switch(config-router-af-vni)# exit
switch(config-router-af)# vni 10500
switch(config-router-af-vni)# route-target both 65000:500
switch(config-router-af)# end
switch)# write memory
switch)# exit
cumulus@switch:~$
```

</details>

The above commands create the following configuration snippet in the `/etc/frr/frr.conf` file:

```
...
address-family l2vpn evpn
  vni 10400
    route-target import 100:400
    route-target import 100:500
  vni 10500
    route-target import 65000:500
    route-target export 65000:500
...
```

## Enable EVPN in an iBGP Environment with an OSPF Underlay

You can use EVPN with an [OSPF](../../../Layer-3/Open-Shortest-Path-First-OSPF/) or static route underlay. This is a more complex configuration than using eBGP. In this case, iBGP advertises EVPN routes directly between VTEPs and the spines are unaware of EVPN or BGP.

The leaf switches peer with each other in a full mesh within the EVPN address family without using route reflectors. The leafs generally peer to their loopback addresses, which are advertised in OSPF. The receiving VTEP imports routes into a specific VNI with a matching route target community.

<details>

<summary>NCLU Commands </summary>

```
cumulus@switch:~$ net add bgp autonomous-system 65020
cumulus@switch:~$ net add bgp l2vpn evpn neighbor 10.1.1.2 remote-as internal
cumulus@switch:~$ net add bgp l2vpn evpn neighbor 10.1.1.3 remote-as internal
cumulus@switch:~$ net add bgp l2vpn evpn neighbor 10.1.1.4 remote-as internal
cumulus@switch:~$ net add bgp l2vpn evpn neighbor 10.1.1.2 activate
cumulus@switch:~$ net add bgp l2vpn evpn neighbor 10.1.1.3 activate
cumulus@switch:~$ net add bgp l2vpn evpn neighbor 10.1.1.4 activate
cumulus@switch:~$ net add bgp l2vpn evpn advertise-all-vni
cumulus@switch:~$ net add ospf router-id 10.1.1.1
cumulus@switch:~$ net add loopback lo ospf area 0.0.0.0
cumulus@switch:~$ net add ospf passive-interface lo
cumulus@switch:~$ net add interface swp50 ospf area 0.0.0.0
cumulus@switch:~$ net add interface swp51 ospf area 0.0.0.0
cumulus@switch:~$ net add interface swp50 ospf network point-to-point
cumulus@switch:~$ net add interface swp51 ospf network point-to-point
cumulus@switch:~$ net pending
cumulus@switch:~$ net commit
```

</details>

<details>

<summary>vtysh Commands </summary>

```
cumulus@switch:~$ sudo vtysh

switch# configure terminal
switch(config)# router bgp 65011
switch(config-router)# neighbor 10.1.1.2 remote-as internal
switch(config-router)# neighbor 10.1.1.3 remote-as internal
switch(config-router)# neighbor 10.1.1.4 remote-as internal
switch(config-router)# address-family l2vpn evpn
switch(config-router-af)# neighbor 10.1.1.2 activate
switch(config-router-af)# neighbor 10.1.1.3 activate
switch(config-router-af)# neighbor 10.1.1.4 activate
switch(config-router-af)# advertise-all-vni
switch(config-router-af)# exit
switch(config-router)# exit
switch(config)# router ospf
switch(config-router)# router-id 10.1.1.1
switch(config-router)# passive-interface lo
switch(config-router)# exit
switch(config)# interface lo
switch(config-if)# ip ospf area 0.0.0.0
switch(config-if)# exit
switch(config)# interface swp50
switch(config-if)# ip ospf area 0.0.0.0
switch(config-if)# ospf network point-to-point
switch(config-if)# exit
switch(config)# interface swp51
switch(config-if)# ip ospf area 0.0.0.0
switch(config-if)# ospf network point-to-point
switch(config-if)# end
switch)# write memory
switch)# exit
cumulus@switch:~$
```

</details>

These commands create the following configuration snippet in the `/etc/frr/frr.conf` file.

```
...
interface lo
  ip ospf area 0.0.0.0
!
interface swp50
  ip ospf area 0.0.0.0
  ip ospf network point-to-point

interface swp51
  ip ospf area 0.0.0.0
  ip ospf network point-to-point
!
router bgp 65020
  neighbor 10.1.1.2 remote-as internal
  neighbor 10.1.1.3 remote-as internal
  neighbor 10.1.1.4 remote-as internal
  !
  address-family l2vpn evpn
  neighbor 10.1.1.2 activate
  neighbor 10.1.1.3 activate
  neighbor 10.1.1.4 activate
  advertise-all-vni
  exit-address-family
  !
Router ospf
  Ospf router-id 10.1.1.1
  Passive-interface lo
...
```

## ARP and ND Suppression

ARP suppression with EVPN allows a VTEP to suppress ARP flooding over VXLAN tunnels as much as possible. A local proxy handles ARP requests received from locally attached hosts for remote hosts. ARP suppression is the implementation for IPv4; ND suppression is the implementation for IPv6.

ARP/ND suppression is enabled by default on all VNIs in Cumulus Linux to reduce flooding of ARP/ND packets over VXLAN tunnels.

In a centralized routing deployment, you must configure layer 3 interfaces even if the switch is configured only for layer 2 (you are not using VXLAN routing). To avoid unnecessary layer 3 information from being installed, Cumulus Networks recommends you configure the `ip forward off` or `ip6 forward off` options as appropriate on the VLANs. See the example configuration below.

The following examples show a configuration using two VXLANs (10100 and 10200) and two VLANs (100 and 200).

<details>

<summary>NCLU Commands </summary>

```
cumulus@switch:~$ net add bridge bridge ports vni100,vni200
cumulus@switch:~$ net add bridge bridge vids 100,200
cumulus@switch:~$ net add vxlan vni100 vxlan id 10100
cumulus@switch:~$ net add vxlan vni200 vxlan id 10200
cumulus@switch:~$ net add vxlan vni100 bridge access 100
cumulus@switch:~$ net add vxlan vni200 bridge access 200
cumulus@switch:~$ net add vxlan vni100 vxlan local-tunnelip 10.0.0.1
cumulus@switch:~$ net add vxlan vni200 vxlan local-tunnelip 10.0.0.1
cumulus@switch:~$ net add vlan 100 ip forward off
cumulus@switch:~$ net add vlan 100 ipv6 forward off
cumulus@switch:~$ net add vlan 200 ip forward off
cumulus@switch:~$ net add vlan 200 ipv6 forward off
cumulus@switch:~$ net pending
cumulus@switch:~$ net commit
```

</details>

<details>

<summary>Linux Commands </summary>

Edit the `/etc/network/interfaces` file.

```
cumulus@switch:~$ sudo nano /etc/network/interfaces
...
auto bridge
iface bridge
    bridge-ports vni100 vni200
    bridge-stp on
    bridge-vids 100 200
    bridge-vlan-aware yes

auto vlan100
iface vlan100
    ip6-forward off
    ip-forward off
    vlan-id 100
    vlan-raw-device bridge

auto vlan200
iface vlan200
    ip6-forward off
    ip-forward off
    vlan-id 200
    vlan-raw-device bridge

auto vni100
iface vni100
    bridge-access 100
    vxlan-id 10100
    vxlan-local-tunnelip 10.0.0.1

auto vni200
iface vni200
      bridge-access 200
      vxlan-id 10200
      vxlan-local-tunnelip 10.0.0.1
...
```

</details>

For a bridge in [traditional mode](../../../Layer-2/Ethernet-Bridging-VLANs/Traditional-Bridge-Mode/), you must edit the bridge configuration in the `/etc/network/interfaces` file using a text editor:

```
cumulus@switch:~$ sudo nano /etc/network/interfaces
...
auto bridge1
iface bridge1
    bridge-ports swp3.100 swp4.100 vni100
    ip6-forward off
    ip-forward off
...
```

{{%notice note%}}

When deploying EVPN and VXLAN using a hardware profile *other* than the default [Forwarding Table Profile](../../../Layer-3/Routing#forwarding-table-profiles), ensure that the Linux kernel ARP `sysctl` settings `gc_thresh2` and `gc_thresh3` are both set to a value larger than the number of neighbor (ARP/ND) entries anticipated in the deployment. To configure these settings, edit the `/etc/sysctl.d/neigh.conf` file, then reboot the switch. If your network has more hosts than the values used in the example below, change the `sysctl` entries accordingly.

<details>

<summary> Example /etc/sysctl.d/neigh.conf file</summary>

```
cumulus@switch:~$ sudo nano /etc/sysctl.d/neigh.conf
...
net.ipv4.neigh.default.gc_thresh3=14336
net.ipv6.neigh.default.gc_thresh3=16384
net.ipv4.neigh.default.gc_thresh2=7168
net.ipv6.neigh.default.gc_thresh2=8192
...
```

</details>

{{%/notice%}}

Cumulus Networks recommends that you keep ARP and ND suppression enabled to reduce flooding of ARP/ND packets over VXLAN tunnels. However, if you need to disable ARP and ND suppression, follow the example commands below.

<details>

<summary>NCLU Commands </summary>

```
cumulus@switch:~$ net add vxlan vni100 bridge arp-nd-suppress off
cumulus@switch:~$ net add vxlan vni200 bridge arp-nd-suppress off
cumulus@switch:~$ net pending
cumulus@switch:~$ net commit

```

</details>

<details>

<summary>Linux Commands </summary>

Edit the /etc/network/interfaces file.

```
cumulus@switch:~$ sudo nano /etc/network/interfaces
...

auto vni100
iface vni100
    bridge-access 100
    bridge-arp-nd-suppress off
    vxlan-id 10100
    vxlan-local-tunnelip 10.0.0.1

auto vni200
iface vni200
      bridge-access 200
      bridge-arp-nd-suppress off
      vxlan-id 10200
      vxlan-local-tunnelip 10.0.0.1
...
```

</details>

## EVPN and VXLAN Active-active Mode

For EVPN in VXLAN active-active mode, both switches in the MLAG pair establish EVPN peering with other EVPN speakers (for example, with spine switches if using hop-by-hop eBGP) and inform about their locally known VNIs and MACs. When MLAG is active, both switches announce this information with the shared anycast IP address.

For active-active configuration, make sure that:

- The `clagd-vxlan-anycast-ip` and `vxlan-local-tunnelip` parameters are under the loopback stanza on both peers.
- The anycast address is advertised to the routed fabric from both peers.
- The VNIs are configured identically on both peers.
- The peerlink must belong to the bridge.

MLAG synchronizes information between the two switches in the MLAG pair; EVPN does not synchronize.

For type-5 routes in an EVPN *symmetric* configuration with VXLAN active-active mode, Cumulus Linux uses Primary IP Address Advertisement. For information on configuring Primary IP Address Advertisement, see [Advertise Primary IP Address](../Inter-subnet-Routing#advertise-primary-ip-address).

For information about active-active VTEPs and anycast IP behavior, and for failure scenarios, see [VXLAN Active-Active Mode](../../VXLAN-Active-Active-Mode).

## Caveats

- When EVPN is enabled on a VTEP, all locally defined VNIs on that switch and other information (such as MAC addresses) are advertised to EVPN peers. There is no provision to only announce certain VNIs.
- On switches with [Spectrum ASICs](https://cumulusnetworks.com/products/hardware-compatibility-list/?asic%5B0%5D=Mellanox%20Spectrum&asic%5B1%5D=Mellanox%20Spectrum_A1), ND suppression only works with the Spectrum-A1 chip.
- ARP suppression is enabled by default in Cumulus Linux. However, in a [VXLAN active-active](../../VXLAN-Active-Active-Mode/) configuration, ARPs are sometimes *not* suppressed. This is because the neighbor entries are not synchronized between the two switches operating in active-active mode by a control plane. This has no impact on forwarding.
- You must configure the overlay (tenants) in a specific VRF and separate from the underlay, which resides in the default VRF. Layer 3 VNI mapping for the default VRF is not supported.
- In an EVPN deployment, Cumulus Linux supports a single BGP ASN which represents the ASN of the core as well as the ASN for any tenant VRFs if they have BGP peerings. If you need to change the ASN, you must first remove the layer 3 VNI in the `/etc/frr/frr.conf` file, modify the BGP ASN, then add back the layer 3 VNI in the `/etc/frr/frr.conf` file.
