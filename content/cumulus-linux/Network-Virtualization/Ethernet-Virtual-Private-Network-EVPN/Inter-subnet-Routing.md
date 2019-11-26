---
title: Inter-subnet Routing
author: Cumulus Networks
weight: 354
aliases:
 - /pages/viewpage.action?pageId=12910740
product: Cumulus Linux
version: '4.0'
---
There are multiple models in EVPN for routing between different subnets (VLANs), also known as inter-VLAN routing. The model you choose depends if every VTEP acts as a layer 3 gateway and performs routing or if only specific VTEPs perform routing, and if routing is performed only at the ingress of the VXLAN tunnel or both the ingress and the egress of the VXLAN tunnel.

Cumulus Linux supports these models:

- [Centralized routing](#centralized-routing): Specific VTEPs act as designated layer 3 gateways and perform routing between subnets; other VTEPs just perform bridging.
- [Distributed asymmetric routing](#asymmetric-routing): Every VTEP participates in routing, but all routing is done at the ingress VTEP; the egress VTEP only performs bridging.
- [Distributed symmetric routing](#symmetric-routing): Every VTEP participates in routing and routing is done at both the ingress VTEP and the egress VTEP.

Distributed routing (asymmetric or symmetric) is commonly deployed with the VTEPs configured with an *anycast IP/MAC address* for each subnet; each VTEP that has a particular subnet is configured with the same IP/MAC for that subnet. Such a model facilitates easy host/VM mobility as there is no need to change the host/VM configuration when it moves from one VTEP to another.

All routing occurs in the context of a tenant VRF ([virtual routing and forwarding](../../../Layer-3/Virtual-Routing-and-Forwarding-VRF/)). A VRF instance is provisioned for each tenant and the subnets of the tenant are associated with that VRF (the corresponding SVI is attached to the VRF). Inter-subnet routing for each tenant occurs within the context of the VRF for that tenant and is separate from the routing for other tenants.

## Centralized Routing

In centralized routing, you configure a specific VTEP to act as the default gateway for all the hosts in a particular subnet throughout the EVPN fabric. It is common to provision a pair of VTEPs in active-active mode as the default gateway using an anycast IP/MAC address for each subnet. You need to configure all subnets on such a gateway VTEP. When a host in one subnet wants to communicate with a host in another subnet, it addresses the packets to the gateway VTEP. The ingress VTEP (to which the source host is attached) bridges the packets to the gateway VTEP over the corresponding VXLAN tunnel. The gateway VTEP performs the routing to the destination host and post-routing, the packet gets bridged to the egress VTEP (to which the destination host is attached). The egress VTEP then bridges the packet on to the destination host.

To enable centralized routing, you must configure the gateway VTEPs to advertise their IP/MAC address. Use the `advertise-default-gw` command:

<details>

<summary>NCLU Commands </summary>

```
cumulus@leaf01:~$ net add bgp autonomous-system 65000
cumulus@leaf01:~$ net add bgp l2vpn evpn advertise-default-gw
cumulus@leaf01:~$ net pending
cumulus@leaf01:~$ net commit
```

</details>

<details>

<summary>vtysh Commands </summary>

```
cumulus@switch:~$ sudo vtysh

switch# configure terminal
switch(config)# router bgp 65011
switch(config-router)# address-family l2vpn evpn 
switch(config-router-af)# advertise-default-gw
switch(config-router-af)# end
switch)# write memory
switch)# exit
cumulus@switch:~$ 
```

</details>

These commands create the following configuration snippet in the `/etc/frr/frr.conf` file.

```
...
router bgp 65000
...
  address-family l2vpn evpn
    advertise-default-gw
  exit-address-family
...
```

{{%notice note%}}

You can deploy centralized routing at the VNI level. Therefore, you can configure the `advertise-default-gw` command per VNI so that centralized routing is used for some VNIs while distributed routing (described below) is used for other VNIs. This type of configuration is not recommended unless the deployment requires it.

When centralized routing is in use, even if the source host and destination host are attached to the same VTEP, the packets travel to the gateway VTEP to get routed and then come back.

{{%/notice%}}

## Asymmetric Routing

In distributed asymmetric routing, each VTEP acts as a layer 3 gateway, performing routing for its attached hosts. The routing is called asymmetric because only the ingress VTEP performs routing, the egress VTEP only performs bridging. Asymmetric routing can be achieved with only host routing and does not involve any interconnecting VNIs. However, you must provision each VTEP with all VLANs/VNIs — the subnets between which communication can take place; this is required even if there are no locally-attached hosts for a particular VLAN.

{{%notice tip%}}

The only additional configuration required to implement asymmetric routing beyond the standard configuration for a layer 2 VTEP described earlier is to ensure that each VTEP has all VLANs (and corresponding VNIs) provisioned on it and the SVI for each such VLAN is configured with an anycast IP/MAC address.

{{%/notice%}}

## Symmetric Routing

In distributed symmetric routing, each VTEP acts as a layer 3 gateway, performing routing for its attached hosts. This is the same as in asymmetric routing. However, with symmetric routing, both the ingress VTEP and egress VTEP route the packets. Therefore, it can be compared to the traditional routing behavior of routing to a next hop router. In the VXLAN encapsulated packet, the inner destination MAC address is set to the router MAC address of the egress VTEP as an indication that the egress VTEP is the next hop and also needs to perform routing. All routing happens in the context of a tenant (VRF). For a packet received by the ingress VTEP from a locally attached host, the SVI interface corresponding to the VLAN determines the VRF. For a packet received by the egress VTEP over the VXLAN tunnel, the VNI in the packet has to specify the VRF. For symmetric routing, this is a VNI corresponding to the tenant and is different from either the source VNI or the destination VNI. This VNI is referred to as the layer 3 VNI or interconnecting VNI; it has to be provisioned by the operator and is exchanged through the EVPN control plane. To make the distinction clear, the regular VNI, which is used to map a VLAN, is referred to as the layer 2 VNI.

{{%notice note%}}

- There is a one-to-one mapping between a layer 3 VNI and a tenant (VRF).
- The VRF to layer 3 VNI mapping has to be consistent across all VTEPs. The layer 3 VNI has to be provisioned by the operator.
- The layer 3 VNI and layer 2 VNI cannot share the same number space; for example, you cannot have *vlan10* and *vxlan10*. Otherwise, the layer 2 VNI does not get created.
- In an MLAG configuration, the SVI used for the layer 3 VNI cannot be part of the bridge. This ensures that traffic tagged with that VLAN ID is not forwarded on the peer link or other trunks.

{{%/notice%}}

In an EVPN symmetric routing configuration, when a type-2 (MAC/IP) route is announced, in addition to containing two VNIs (the layer 2 VNI and the layer 3 VNI), the route also contains separate RTs for layer 2 and layer 3. The layer 3 RT associates the route with the tenant VRF. By default, this is auto-derived in a similar way to the layer 2 RT, using the layer 3 VNI instead of the layer 2 VNI; however you can also explicitly configure it.

For EVPN symmetric routing, additional configuration is required:

- [Configure a per-tenant VXLAN interface](#configure-a-per-tenant-vxlan-interface) that specifies the layer 3 VNI for the tenant. This VXLAN interface is part of the bridge and the router MAC address of the remote VTEP is installed over this interface.
- [Configure an SVI](#configure-an-svi-for-the-layer-3-vni) (layer 3 interface) corresponding to the per-tenant VXLAN interface. This is attached to the VRF of the tenant. Remote host routes for symmetric routing are installed over this SVI.
- [Specify the VRF to layer 3 VNI mapping](#configure-the-vrf-to-layer-3-vni-mapping). This configuration is for the BGP control plane.

Optional configuration includes [configuring RD and RTs for the tenant VRF](#configure-rd-and-rts-for-the-tenant-vrf) and [advertising the locally-attached subnets](#advertise-the-locally-attached-subnets).

### Configure a Per-tenant VXLAN Interface

<details>

<summary>NCLU Commands </summary>

```
cumulus@leaf01:~$ net add vxlan vni104001 vxlan id 104001
cumulus@leaf01:~$ net add vxlan vni104001 bridge access 4001
cumulus@leaf01:~$ net add vxlan vni104001 vxlan local-tunnelip 10.0.0.11
cumulus@leaf01:~$ net add bridge bridge ports vni104001
cumulus@leaf01:~$ net pending
cumulus@leaf01:~$ net commit
```

</details>

<details>

<summary>Linux Commands </summary>

Edit the `/etc/network/interfaces` file. For example:

```
cumulus@leaf01:~$ sudo nano /etc/network/interfaces
...
auto vni104001
iface vni104001
    bridge-access 4001
    vxlan-id 104001
    vxlan-local-tunnelip 10.0.0.11

auto bridge
  iface bridge
    bridge-ports vni104001
    bridge-vlan-aware yes
...
```

</details>

### Configure an SVI for the Layer 3 VNI

<details>

<summary>NCLU Commands </summary>

```
cumulus@leaf01:~$ net add vlan 4001 vrf turtle
cumulus@leaf01:~$ net pending
cumulus@leaf01:~$ net commit
```

</details>

<details>

<summary>Linux Commands </summary>

Edit the `/etc/network/interfaces` file. For example:

```
cumulus@leaf01:~$ sudo nano /etc/network/interfaces
...
auto vlan4001
iface vlan4001
    vlan-id 4001
    vlan-raw-device bridge
    vrf turtle
...
```

</details>

{{%notice note%}}

When two VTEPs are operating in **VXLAN active-active** mode and performing **symmetric** routing, you need to configure the router MAC corresponding to each layer 3 VNI to ensure both VTEPs use the same MAC address. Specify the `address-virtual` (MAC address) for the SVI corresponding to the layer 3 VNI. Use the same address on both switches in the MLAG pair. Cumulus Networks recommends you use the MLAG system MAC address. See [Advertise Primary IP Address](#advertise-primary-ip-address).

{{%/notice%}}

### Configure the VRF to Layer 3 VNI Mapping

<details>

<summary>NCLU Commands </summary>

```
cumulus@leaf01:~$ net add vrf turtle vni 104001
cumulus@leaf01:~$ net pending
cumulus@leaf01:~$ net commit
```

</details>

<details>

<summary>Linux Commands </summary>

Edit the `/etc/frr/frr.conf` file. For example:

```
cumulus@leaf01:~$ sudo nano /etc/frr/frr.conf
...
vrf turtle
  vni 104001
!
...
```

</details>

### Configure RD and RTs for the Tenant VRF

If you do not want the RD and RTs (layer 3 RTs) for the tenant VRF to be derived automatically, you can configure them manually by specifying them under the `l2vpn evpn` address family for that specific VRF.

<details>

<summary>NCLU Commands </summary>

```
cumulus@switch:~$ net add bgp vrf tenant1 l2vpn evpn rd 172.16.100.1:20
cumulus@switch:~$ net add bgp vrf tenant1 l2vpn evpn route-target import 65100:20
cumulus@switch:~$ net pending
cumulus@switch:~$ net commit
```

</details>

<details>

<summary>vtysh Commands </summary>

```
cumulus@switch:~$ sudo vtysh

switch# configure terminal
switch(config)# router bgp 65011 vrf tenant1
switch(config-router)# address-family l2vpn evpn
switch(config-router-af)# rd 172.16.100.1:20
switch(config-router-af)# route-target import 65100:20
switch(config-router-af)# end
switch# write memory
switch# exit
cumulus@switch:~$
```

</details>

These commands create the following configuration snippet in the `/etc/frr/frr.conf` file:

```
...
router bgp <as> vrf tenant1
  address-family l2vpn evpn
  rd 172.16.100.1:20
  route-target import 65100:20
...
```

{{%notice note%}}

The tenant VRF RD and RTs are different from the RD and RTs for the layer 2 VNI. See [Define RDs and RTs](../Basic-Configuration/#define-rds-and-rts).

{{%/notice%}}

### Advertise Locally-attached Subnets

Symmetric routing presents a problem in the presence of silent hosts. If the ingress VTEP does not have the destination subnet and the host route is not advertised for the destination host, the ingress VTEP cannot route the packet to its destination. You can overcome this problem by having VTEPs announce the subnet prefixes corresponding to their connected subnets in addition to announcing host routes. These routes are announced as EVPN prefix (type-5) routes.

To advertise locally attached subnets:

1. Enable advertisement of EVPN prefix (type-5) routes. Refer to [Prefix-based Routing — EVPN Type-5 Routes](#prefix-based-routing-evpn-type-5-routes), below.
2. Ensure that the routes corresponding to the connected subnets are known in the BGP VRF routing table by injecting them using the `network` command or redistributing them using the `redistribute connected` command.

{{%notice note%}}

This configuration is recommended only if the deployment is known to have silent hosts. It is also recommended that you enable on only one VTEP per subnet, or two for redundancy.

{{%/notice%}}

## Prefix-based Routing

EVPN in Cumulus Linux supports prefix-based routing using EVPN type-5 (prefix) routes. Type-5 routes (or prefix routes) are primarily used to route to destinations outside of the data center fabric.

EVPN prefix routes carry the layer 3 VNI and router MAC address and follow the symmetric routing model for routing to the destination prefix.

{{%notice note%}}

- When connecting to a WAN edge router to reach destinations outside the data center, Cumulus Networks recommends that you deploy specific border/exit leaf switches to originate the type-5 routes.
- On switches with Spectrum ASICs, centralized routing, symmetric routing, and prefix-based routing only work with the Spectrum A1 chip.
- If you are using a Broadcom Trident II+ switch as a border/exit leaf, see the [caveats](#caveats) below for a required workaround; the workaround only applies to Trident II+ switches, not Tomahawk or Spectrum.

{{%/notice%}}

### Install EVPN Type-5 Routes

For a switch to be able to install EVPN type-5 routes into the routing table, you must configure it with the layer 3 VNI related information. This configuration is the same as for symmetric routing. You need to:

1. Configure a per-tenant VXLAN interface that specifies the layer 3 VNI for the tenant. This VXLAN interface is part of the bridge; router MAC addresses of remote VTEPs are installed over this interface.
2. Configure an SVI (layer 3 interface) corresponding to the per-tenant VXLAN interface. This is attached to the VRF of the tenant. The remote prefix routes are installed over this SVI.
3. Specify the mapping of the VRF to layer 3 VNI. This configuration is for the BGP control plane.

### Announce EVPN Type-5 Routes

The following configuration is required in the tenant VRF to announce IP prefixes in the BGP RIB as EVPN type-5 routes.

<details>

<summary>NCLU Commands </summary>

```
cumulus@switch:~$ net add bgp vrf vrf1 l2vpn evpn advertise ipv4 unicast
cumulus@switch:~$ net pending
cumulus@switch:~$ net commit
```

</details>

<details>

<summary>vtysh Commands </summary>

```
cumulus@switch:~$ sudo vtysh

switch# configure terminal
switch(config)# router bgp 65011 vrf vrf1
switch(config-router)# address-family l2vpn evpn
switch(config-router-af)# advertise ipv4 unicast
switch(config-router-af)# end
switch# write memory
switch# exit
cumulus@switch:~$
```

</details>

These commands create the following snippet in the `/etc/frr/frr.conf` file:

```
...
router bgp 65005 vrf vrf1
  address-family l2vpn evpn
    advertise ipv4 unicast
  exit-address-family
end
...
```

### EVPN Type-5 Routing in Asymmetric Mode

Asymmetric routing is an ideal choice when all VLANs (subnets) are configured on all leaf switches. It simplifies the routing configuration and eliminates the potential need for advertising subnet routes to handle silent hosts. However, most deployments need access to external networks to reach the Internet or global destinations, or to do subnet-based routing between pods or data centers; this requires EVPN type-5 routes.

Cumulus Linux supports EVPN type-5 routes for prefix-based routing in asymmetric configurations within the pod or data center by providing an option to use the layer 3 VNI only for type-5 routes; type-2 routes (host routes) only use the layer 2 VNI.

The following example commands show how to use the layer 3 VNI for type-5 routes only:

<details>

<summary>NCLU Commands </summary>

```
cumulus@leaf01:~$ net add vrf turtle vni 104001 prefix-routes-only
cumulus@leaf01:~$ net pending
cumulus@leaf01:~$ net commit
```

{{%notice note%}}

There is no command to delete the `prefix-routes-only` option. The `net del vrf <vrf> vni <vni> prefix-routes-only` command deletes the VNI.

{{%/notice%}}

</details>

<details>

<summary>Linux Commands </summary>

Edit the `/etc/frr/frr.conf` file. For example:

```
cumulus@leaf01:~$ sudo nano /etc/frr/frr.conf
...
vrf turtle
  vni 104001 prefix-routes-only
...
```

</details>

### Control RIB Routes

By default, when announcing IP prefixes in the BGP RIB as EVPN type-5 routes, all routes in the BGP RIB are picked for advertisement as EVPN type-5 routes. You can use a route map to allow selective advertisement of routes from the BGP RIB as EVPN type-5 routes.

The following commands add a route map filter to IPv4 EVPN type-5 route advertisement:

<details>

<summary>NCLU Commands </summary>

```
cumulus@switch:~$ net add bgp vrf turtle l2vpn evpn advertise ipv4 unicast route-map map1
cumulus@switch:~$ net pending
cumulus@switch:~$ net commit
```

</details>

<details>

<summary>vtysh Commands </summary>

```
cumulus@switch:~$ sudo vtysh

switch# configure terminal
switch(config)# router bgp 65011 vrf turtle
switch(config-router)# address-family l2vpn evpn
switch(config-router-af)# advertise ipv4 unicast route-map map1
switch(config-router-af)# end
switch# write memory
switch# exit
cumulus@switch:~$
```

</details>

### Originate Default EVPN Type-5 Routes

Cumulus Linux supports originating EVPN default type-5 routes. The default type-5 route is originated from a border (exit) leaf and advertised to all the other leafs within the pod. Any leaf within the pod follows the default route towards the border leaf for all external traffic (towards the Internet or a different pod).

To originate a default type-5 route in EVPN, you need to execute FRRouting commands. The following shows an example:

```
cumulus@switch:~$ sudo vtysh

switch# configure terminal
switch(config)# router bgp 650030 vrf vrf1
switch(config-router)# address-family l2vpn evpn
switch(config-router-af)# default-originate ipv4
switch(config-router-af)# default-originate ipv6
switch(config-router-af)# end
switch# write memory
```

### Advertise Primary IP address

In EVPN symmetric routing configurations with MLAG in Cumulus Linux 3.7 and earlier, all EVPN routes are advertised with the anycast IP address (VXLAN interface tunnel IP address) as the next-hop IP address and the anycast MAC address as the router MAC address. In a failure scenario, this can lead to traffic being forwarded to a leaf switch that does not have the destination routes. Traffic has to traverse the peer link (with additional BGP sessions per VRF).

To prevent sub-optimal routing in Cumulus Linux 4.0 and later, the next hop IP address of the VTEP is conditionally handled depending on the route type: type-2 (MAC/IP advertisement) or type-5 (IP prefix route).

- For type-5 routes, the primary IP address of the VTEP is used as the next hop IP address and the system MAC address of the VTEP is used as the router MAC.
- For type-2 routes, the anycast IP address is used as the next hop IP address and the anycast MAC address is used as the router MAC address.

#### Configure Advertise Primary IP Address

Cumulus Linux automatically derives the system IP address from the router ID of the BGP default instance and uses the VXLAN interface tunnel IP address as the anycast IP address. However, you need to configure the switch to use two interfaces per layer 3 VNI; the SVI interface with a unique MAC address and the MAC VLAN (VRR interface) with the anycast MAC address.

{{%notice note%}}

Run these commands on both switches in the MLAG pair.

{{%/notice%}}

<details>

<summary> NCLU commands</summary>

Run the `address-virtual <anycast-mac>` command under the SVI:

```
cumulus@leaf01:~$ net add vlan 4001 address-virtual 44:38:39:FF:40:94
cumulus@leaf01:~$ net pending
cumulus@leaf01:~$ net commit
```

</details>

<details>

<summary> Linux commands</summary>

Edit the `/etc/network/interfaces` file and add `address-virtual <anycast-mac>` under the SVI. For example:

```
cumulus@leaf01:~$ sudo nano /etc/network/interfaces
...
auto vlan4001
iface vlan4001
    address-virtual 44:38:39:FF:40:94
    vlan-id 4001
    vlan-raw-device bridge
    vrf turtle
...
```

</details>

{{%notice note%}}

In Cumulus Linux 3.7 and earlier, the `hwaddress` command is used instead of the `address-virtual` command. If you upgraded from Cumulus Linux 3.7 to 4.0 and have a previous symmetric routing with VXLAN active-active mode configuration, you must change `hwaddress` to `address-virtual`. Either run the NCLU `address-virtual <anycast-mac>` command or edit the `/etc/network/interfaces` file.

{{%/notice%}}

If you do not want Cumulus Linux to derive the system IP address automatically, you can provide the system IP address and system MAC address under each tenant VRF BGP instance.

The following example commands add the system IP address 10.0.0.11 and the system MAC address 44:38:39:ff:00:00:

<details>

<summary> NCLU commands</summary>

```
cumulus@switch:~$ net add bgp vrf vrf1 l2vpn evpn advertise-pip ip 10.0.0.11 mac 44:38:39:ff:00:00  
cumulus@leaf01:~$ net pending
cumulus@leaf01:~$ net commit
```

</details>

<details>

<summary> vtysh commands</summary>

```
cumulus@switch:~$ sudo vtysh

switch# configure terminal
switch(config)# router bgp 65000 vrf vrf1
switch(config)# address-family l2vpn evpn
switch(config)# advertise-pip ip 10.0.0.11 mac 44:38:39:ff:00:00
switch(config-router-af)# end
switch# write memory
switch# exit
cumulus@switch:~$
```

</details>

The system IP address and system MAC address you provide take precedence over the addresses that Cumulus Linux derives automatically.

#### Disable Advertise Primary IP Address

Each switch in the MLAG pair advertises type-5 routes with its own system IP, which creates an additional next hop at the remote VTEPs. In a large multi-tenancy EVPN deployment, where additional resources are a concern, you might prefer to disable this feature.

To disable Advertise Primary IP Address under each tenant VRF BGP instance:

<details>

<summary> NCLU commands</summary>

```
cumulus@leaf01:~$ net del bgp vrf vrf1 l2vpn evpn advertise-pip
cumulus@leaf01:~$ net pending
cumulus@leaf01:~$ net commit
```

</details>

<details>

<summary> vtysh commands</summary>

cumulus@switch:~$ sudo vtysh

```
switch# configure terminal
switch(config)# router bgp 65000 vrf vrf1
switch(config)# address-family l2vpn evpn
switch(config)# no advertise-pip
switch(config-router-af)# end
switch# write memory
switch# exit
cumulus@switch:~$
```

</details>

#### Show Advertise Primary IP Address Information

To show Advertise Primary IP Address parameters, run the NCLU `net show bgp l2vpn evpn vni <vni>` command or the vtysh `show bgp l2vpn evpn vni <vni>` command. For example:

```
cumulus@switch:~$ sudo vtysh
switch# show bgp l2vpn evpn vni 4001
VNI: 4001 (known to the kernel)
 Type: L3
 Tenant VRF: vrf1
 RD: 10.0.0.11:2
 Originator IP: 10.0.0.112 🡨 Anycast IP
 Advertise-gw-macip : n/a
 Advertise-pip: Yes
 System-IP: 10.0.0.11
 System-MAC: 44:38:39:ff:00:00
 Router-MAC: 44:01:02:ff:ff:01
 Import Route Target:
  5586:4002
 Export Route Target:
  5586:4002
switch#
```

To show EVPN routes with Primary IP Advertisement, run the NCLU `net show bgp l2vpn evpn route` command or the vtysh `show bgp l2vpn evpn route` command. For example:

```
cumulus@switch:~$ sudo vtysh
switch# show bgp l2vpn evpn route
…
Route Distinguisher: 10.0.0.11:2
*> [5]:[0]:[24]:[81.6.1.0]
                    10.0.0.11                0             0 5541 i
                    ET:8 RT:5586:4002 Rmac:44:38:39:ff:00:00
…
Route Distinguisher: 10.0.0.11:3
*> [2]:[0]:[48]:[00:02:00:00:00:2e]:[32]:[45.0.4.2]
                    10.0.0.11                          32768 i
                    ET:8 RT:5586:1004 RT:5546:4002 Rmac:44:38:39:ff:00:00

```

To show the learned route from an external router injected as a type-5 route, run the NCLU `net show bgp vrf <vrf> ipv4 unicast` command or the vtysh `show bgp vrf <vrf> ipv4 unicast` command. For example:

```
cumulus@switch:~$ net show bgp vrf <vrf> ipv4 unicast
...
 Network          Next Hop            Metric LocPrf Weight Path
*> 10.0.0.0/8    10.0.0.42                0             0 5541 I
```

## Caveats

### VXLAN Decapsulation on Maverick, and Broadcom Trident II+ and Trident 3 Switches

On the Broadcom Trident II+, Trident 3, and Maverick-based switch, when a lookup is done after VXLAN decapsulation on the external-facing switch (the exit or border leaf), the switch does not rewrite the MAC addresses or TTL. For through traffic, packets are dropped by the next hop instead of correctly routing from a VXLAN overlay network into a non-VXLAN external network (such as the Internet). This applies to all forms of VXLAN routing (centralized, asymmetric, and symmetric) and affects all traffic from VXLAN overlay hosts that need to be routed after VXLAN decapsulation on an exit or border leaf. This includes traffic destined to external networks (through traffic) and traffic destined to the exit leaf SVI address. To work around this issue, modify the external-facing interface for each VLAN sub-interface on the exit leaf by creating a temporary VNI and associating it with the existing VLAN ID.

<details>

<summary>Example Workaround </summary>

For example, if the expected interface configuration is:

```
auto swp3.2001
iface swp3.2001
    vrf vrf1
    address 10.0.0.2/24
# where swp3 is the external facing port and swp3.2001 is the VLAN sub-interface

auto bridge
iface bridge
    bridge-vlan-aware yes
    bridge ports vx-4001
    bridge-vids 4001

auto vx-4001
iface vx-4001
    vxlan-id 4001
    <... usual vxlan config ...>
      bridge-access 4001
# where vnid 4001 represents the L3 VNI

auto vlan4001
iface vlan4001
    vlan-id 4001
    vlan-raw-device bridge
    vrf vrf1
```

Modify the configuration as follows:

```
auto swp3
iface swp3
    bridge-access 2001
# associate the port (swp3) with bridge 2001

auto bridge
iface bridge
    bridge-vlan-aware yes
    bridge ports swp3 vx-4001 vx-16000000
    bridge-vids 2001
# where vx-4001 is the existing VNI and vx-16000000 is a new temporary VNI
# this is now bridging the port (swp3), the VNI (vx-4001),
# and the new temporary VNI (vx-16000000)
# the bridge VLAN ID is now 2001

auto vlan2001
iface vlan2001
    vlan-id 2001
    vrf vrf1
    address 10.0.0.2/24
    vlan-raw-device bridge
# create a VLAN 2001 with the associated VRF and IP address

auto vx-16000000
iface vx-16000000
    vxlan-id 16000000
    bridge-access 2001
    <... usual vxlan config ...>
# associate the temporary VNI (vx-16000000) with bridge 2001

 auto vx-4001
iface vx-4001
    vxlan-id 4001
    <... usual vxlan config ...>
    bridge-access 4001
# where vnid 4001 represents the L3 VNI

auto vlan4001
iface vlan4001
    vlan-id 4001
    vlan-raw-device bridge
    vrf vrf1
```

If you use an MLAG pair instead of a single exit/border leaf, add the same temporary VNIs on both switches of the MLAG pair.

</details>

### Centralized Routing with ARP Suppression Enabled on the Gateway

In an EVPN centralized routing configuration, where the layer 2 network extends beyond VTEPs, (for example, a host with bridges), the gateway MAC address is not refreshed in the network when ARP suppression is enabled on the gateway. To work around this issue, disable ARP suppression on the centralized gateway.

### Type-5 Routes and ECMP

For VXLAN type-5 routes, ECMP does not work when the VTEP is directly connected to remote VTEPs.
To work around this issue, add an additional device in the VXLAN fabric between the local and remote VTEPs, so that local and remote VTEPs are not directly connected.
