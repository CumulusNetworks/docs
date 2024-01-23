---
title: Inter-subnet Routing
author: NVIDIA
weight: 565
toc: 4
---
EVPN includes multiple models for routing between different subnets (VLANs), also known as inter-VLAN routing. The model you choose depends if every <span class="a-tooltip">[VTEP](## "Virtual Tunnel End Point")</span> acts as a layer 3 gateway and performs routing or if only specific VTEPs perform routing, and if routing occurs only at the ingress of the VXLAN tunnel or both the ingress and the egress of the VXLAN tunnel.

Cumulus Linux supports these models:

- {{<link url="#centralized-routing" text="Centralized routing">}}: Specific VTEPs act as designated layer 3 gateways and perform routing between subnets; other VTEPs just perform bridging.
- {{<link url="#asymmetric-routing" text="Distributed asymmetric routing">}}: Every VTEP participates in routing, but all routing is done at the ingress VTEP; the egress VTEP only performs bridging.
- {{<link url="#symmetric-routing" text="Distributed symmetric routing">}}: Every VTEP participates in routing and performs routing at both the ingress VTEP and the egress VTEP.

   You typically deploy distributed routing with the VTEPs that have an *anycast IP and MAC address* for each subnet; each VTEP that has a particular subnet has the same IP/MAC for that subnet. Such a model facilitates easy host and VM mobility as there is no need to change the host or VM configuration when it moves from one VTEP to another.

   All routing occurs in the context of a tenant VRF ({{<link url="Virtual-Routing-and-Forwarding-VRF" text="virtual routing and forwarding">}}). Cumulus Linux provisions a VRF instance for each tenant and associates the subnets of the tenant with that VRF (the corresponding SVI attaches to the VRF). Inter-subnet routing for each tenant occurs within the context of the VRF for that tenant and is separate from the routing for other tenants.

## Centralized Routing

In centralized routing, you configure a specific VTEP to act as the default gateway for all the hosts in a particular subnet throughout the EVPN fabric. It is common to provision a pair of VTEPs in active-active mode as the default gateway using an anycast IP and MAC address for each subnet. You need to configure all subnets on such a gateway VTEP. When a host in one subnet wants to communicate with a host in another subnet, it addresses the packets to the gateway VTEP. The ingress VTEP (to which the source host attaches) bridges the packets to the gateway VTEP over the corresponding VXLAN tunnel. The gateway VTEP routes to the destination host and, post-routing, the packet bridges to the egress VTEP (to which the destination host attaches). The egress VTEP then bridges the packet on to the destination host.

To enable centralized routing, you must configure the gateway VTEPs to advertise their IP and MAC address.

{{< tabs "TabID26 ">}}
{{< tab "NVUE Commands ">}}

```
cumulus@leaf01:~$ nv set evpn route-advertise default-gateway on
cumulus@leaf01:~$ nv config apply
```

{{< /tab >}}
{{< tab "vtysh Commands ">}}

```
cumulus@leaf01:~$ sudo vtysh

leaf01# configure terminal
leaf01(config)# router bgp 65101
leaf01(config-router)# address-family l2vpn evpn
leaf01(config-router-af)# advertise-default-gw
leaf01(config-router-af)# end
leaf01)# write memory
leaf01)# exit
cumulus@leaf01:~$
```

The vtysh commands create the following configuration snippet in the `/etc/frr/frr.conf` file.

```
...
router bgp 65101
...
  address-family l2vpn evpn
    advertise-default-gw
  exit-address-family
...
```

{{< /tab >}}
{{< /tabs >}}

{{%notice note%}}
You can deploy centralized routing at the VNI level, where you can configure the `advertise-default-gw` command per VNI; you use centralized routing for certain VNIs and distributed symmetric routing (described below) other VNIs. NVIDIA does not recommend this type of configuration.

When you use centralized routing, even if the source host and destination host attach to the same VTEP, the packets travel to the gateway VTEP, the switch routes the packets, then the packets come back.
{{%/notice%}}

## Asymmetric Routing

In distributed asymmetric routing, each VTEP acts as a layer 3 gateway, performing routing for its attached hosts. The routing is called asymmetric because only the ingress VTEP performs routing, the egress VTEP only performs bridging. You can achieve asymmetric routing with only host routing, which does not involve any interconnecting VNIs. However, you must provision each VTEP with all VLANs and corresponding VNIs (the subnets between which communication takes place); this is required even if there are no locally-attached hosts for a particular VLAN.

The only additional configuration required to implement asymmetric routing beyond the standard configuration for a layer 2 VTEP described above is to ensure that each VTEP has all VLANs (and corresponding VNIs) provisioned and the SVI for each VLAN is configured with an anycast IP or MAC address.

{{%notice note%}}
- NVIDIA recommends you use symmetric or centralized routing instead of asymmetric routing.
- Asymmetric routing does not support EVPN multihoming.
{{%/notice%}}

## Symmetric Routing

In distributed symmetric routing, each VTEP acts as a layer 3 gateway, performing routing for its attached hosts; however, both the ingress VTEP and egress VTEP route the packets (similar to the traditional routing behavior of routing to a next hop router). In the VXLAN encapsulated packet, the inner destination MAC address is the router MAC address of the egress VTEP to indicate that the egress VTEP is the next hop and also needs to perform routing. All routing happens in the context of a tenant (VRF). For a packet that the ingress VTEP receives from a locally attached host, the SVI interface corresponding to the VLAN determines the VRF. For a packet that the egress VTEP receives over the VXLAN tunnel, the VNI in the packet has to specify the VRF. For symmetric routing, this is a VNI corresponding to the tenant and is different from either the source VNI or the destination VNI. This VNI is a layer 3 VNI or interconnecting VNI. The regular VNI, which maps a VLAN, is the layer 2 VNI.

{{%notice note%}}
- Cumulus Linux supports symmetric routing on NVIDIA Spectrum-A1 and later.
- Cumulus Linux uses a one-to-one mapping between a layer 3 VNI and a tenant (VRF).
- The VRF to layer 3 VNI mapping has to be consistent across all VTEPs.
- A layer 3 VNI and a layer 2 VNI cannot have the same ID. If the VNI IDs are the same, Cumulus Linux does not create the layer 2 VNI.
- In an MLAG configuration, the SVI for the layer 3 VNI cannot be part of the bridge. This ensures that the switch does not forward traffic tagged with that VLAN ID on the peer link or other trunks.
{{%/notice%}}

In an EVPN symmetric routing configuration, when the switch announces a type-2 (MAC/IP) route, in addition to containing two VNIs (the layer 2 VNI and the layer 3 VNI), the route also contains separate RTs for layer 2 and layer 3. The layer 3 RT associates the route with the tenant VRF. By default, this is auto-derived using the layer 3 VNI instead of the layer 2 VNI; however you can also configure it.

For EVPN symmetric routing, you need to perform the following additional configuration. Optional configuration includes {{<link url="#configure-rd-and-rts-for-the-tenant-vrf" text="configuring RD and RTs for the tenant VRF">}} and {{<link url="#advertise-locally-attached-subnets" text="advertising the locally-attached subnets">}}.

{{< tabs "TabID113 ">}}
{{< tab "NVUE Commands ">}}

Specify the VRF to layer 3 VNI mapping. This configuration is for the BGP control plane.

```
cumulus@leaf01:~$ nv set vrf RED evpn vni 4001
cumulus@leaf01:~$ nv config apply
```

{{%notice note%}}
When you run the `nv set vrf RED evpn vni 4001` command, NVUE:
- Creates a layer 3 VNI called vni4001
- Assigns the vni4001 a VLAN automatically from the reserved VLAN range and adds `_l3` (layer 3) at the end (for example vlan220_l3)
- Creates a layer 3 bridge called `br_l3vni`
- Adds vni4001 to the `br_l3vni` bridge
- Assigns vlan4024 to VRF RED

```
cumulus@leaf01:~$ sudo cat /etc/network/interfaces
...
auto vni4001
iface vni4001
    bridge-access 220
    bridge-learning off
    vxlan-id 4001
auto vlan220_l3
iface vlan220_l3
vrf RED
vlan-raw-device br_l3vni
address-virtual 44:38:39:BE:EF:AA
vlan-id 220
...
```
{{%/notice%}}

{{< /tab >}}
{{< tab "Linux Commands ">}}

1. Configure a per-tenant VXLAN interface that specifies the layer 3 VNI for the tenant. This VXLAN interface is part of the bridge and the router MAC address of the remote VTEP installs over this interface.

   Edit the `/etc/network/interfaces` file. For example:

   ```
   cumulus@leaf01:~$ sudo nano /etc/network/interfaces
   ...
   auto vni10
   iface vni10
       bridge-access 10
       vxlan-id 10
       vxlan-local-tunnelip 10.10.10.1
   
   auto bridge
     iface bridge
       bridge-ports vni10
       bridge-vlan-aware yes
   ...
   ```

2. Configure an SVI (layer 3 interface) corresponding to the per-tenant VXLAN interface. This attaches to the VRF of the tenant. Remote host routes for symmetric routing install over this SVI.

   Edit the `/etc/network/interfaces` file. For example:

   ```
   cumulus@leaf01:~$ sudo nano /etc/network/interfaces
   ...
   auto vlan10
   iface vlan10
       vlan-id 10
       vlan-raw-device bridge
       vrf RED
   ...
   ```

3. Specify the VRF to layer 3 VNI mapping. This configuration is for the BGP control plane.

   Edit the `/etc/frr/frr.conf` file. For example:

   ```
   cumulus@leaf01:~$ sudo nano /etc/frr/frr.conf
   ...
   vrf RED
     vni 4001
   !
   ...
   ```

{{< /tab >}}
{{< /tabs >}}

{{%notice info%}}
- Do not add the layer 3 VNI VLAN IDs to the bridge `vids` list in the layer 2 bridge configuration.
- When two VTEPs are operating in **VXLAN active-active** mode and performing **symmetric** routing, you need to configure the router MAC corresponding to each layer 3 VNI to ensure both VTEPs use the same MAC address. Specify the `address-virtual` (MAC address) for the SVI corresponding to the layer 3 VNI. Use the same address on both switches in the MLAG pair. Use the MLAG system MAC address. See {{<link url="#advertise-primary-ip-address-vxlan-active-active-mode" text="Advertise Primary IP    Address">}}.
{{%/notice%}}

### Configure RD and RTs for the Tenant VRF

If you do not want Cumulus Linux to derive the RD and RTs (layer 3 RTs) for the tenant VRF automatically, you can configure them manually by specifying them under the `l2vpn evpn` address family for that specific VRF.

{{< tabs "TabID226 ">}}
{{< tab "NVUE Commands ">}}

```
cumulus@leaf01:~$ nv set vrf RED router bgp rd 10.1.20.2:5
cumulus@leaf01:~$ nv set vrf RED router bgp route-import from-evpn route-target 65102:4001
```

{{< /tab >}}
{{< tab "vtysh Commands ">}}

```
cumulus@leaf01:~$ sudo vtysh

leaf01# configure terminal
leaf01(config)# router bgp 65101 vrf RED
leaf01(config-router)# address-family l2vpn evpn
leaf01(config-router-af)# rd 10.1.20.2:5
leaf01(config-router-af)# route-target import 65102:4001
leaf01(config-router-af)# end
leaf01# write memory
leaf01# exit
cumulus@leaf01:~$
```

The vtysh commands create the following configuration snippet in the `/etc/frr/frr.conf` file:

```
...
router bgp 65101 vrf RED
  address-family l2vpn evpn
  rd 10.1.20.2:5
  route-target import 65102:4001
...
```

{{< /tab >}}
{{< /tabs >}}

{{%notice note%}}
The tenant VRF RD and RTs are different from the RD and RTs for the layer 2 VNI. See {{<link url="EVPN-Enhancements#define-rds-and-rts" text="Define RDs and RTs">}}.
{{%/notice%}}

### Advertise Locally Attached Subnets

Symmetric routing presents a problem in the presence of silent hosts. If the ingress VTEP does not have the destination subnet and the host route does not advertise for the destination host, the ingress VTEP cannot route the packet to its destination. You can overcome this problem by having VTEPs announce the subnet prefixes corresponding to their connected subnets in addition to announcing host routes. Cumulus Linux announces these routes as EVPN prefix (type-5) routes.

To advertise locally attached subnets:
<!-- vale off -->
1. Enable advertisement of EVPN prefix (type-5) routes. Refer to {{<link url="#announce-evpn-type-5-routes" text="Prefix-based Routing - EVPN Type-5 Routes">}}, below.<!-- vale on -->
2. Ensure that the routes corresponding to the connected subnets are in the BGP VRF routing table by injecting them using the `network` command or redistributing them using the `redistribute connected` command.

{{%notice note%}}
Use this configuration only if you have silent hosts and only on one VTEP per subnet (or two for redundancy).
{{%/notice%}}
<!-- vale off -->
## Prefix-based Routing
<!-- vale on -->
EVPN in Cumulus Linux supports prefix-based routing using EVPN type-5 (prefix) routes. Type-5 routes (or prefix routes) primarily route to destinations outside of the data center fabric.

EVPN prefix routes carry the layer 3 VNI and router MAC address and follow the symmetric routing model to route to the destination prefix.

{{%notice note%}}
- When connecting to a WAN edge router to reach destinations outside the data center, deploy specific border or exit leaf switches to originate the type-5 routes.
- On switches with Spectrum ASICs, centralized routing, symmetric routing, and prefix-based routing only work with Spectrum-A1 and later.
{{%/notice%}}
<!-- vale off -->
### Install EVPN Type-5 Routes
<!-- vale on -->
For a switch to install EVPN type-5 routes into the routing table, you must configure layer 3 VNI related information. This configuration is the same as for symmetric routing. You need to:

1. Configure a per-tenant VXLAN interface that specifies the layer 3 VNI for the tenant. This VXLAN interface is part of the bridge; router MAC addresses of remote VTEPs install over this interface.
2. Configure an SVI (layer 3 interface) corresponding to the per-tenant VXLAN interface. This attaches to the VRF of the tenant. The remote prefix routes install over this SVI.
3. Specify the mapping of the VRF to layer 3 VNI. This configuration is for the BGP control plane.
<!-- vale off -->
### Announce EVPN Type-5 Routes
<!-- vale on -->
The tenant VRF requires the following configuration to announce IP prefixes in the BGP RIB as EVPN type-5 routes.

{{< tabs "TabID317 ">}}
{{< tab "NVUE Commands ">}}

```
cumulus@leaf01:~$ nv set vrf RED router bgp address-family ipv4-unicast route-export to-evpn enable on
cumulus@leaf01:~$ nv config apply
```

{{< /tab >}}
{{< tab "vtysh Commands ">}}

```
cumulus@leaf01:~$ sudo vtysh

leaf01# configure terminal
leaf01(config)# router bgp 65101 vrf RED
leaf01(config-router)# address-family l2vpn evpn
leaf01(config-router-af)# advertise ipv4 unicast
leaf01(config-router-af)# end
leaf01# write memory
leaf01# exit
cumulus@leaf01:~$
```

The vtysh commands create the following snippet in the `/etc/frr/frr.conf` file:

```
...
router bgp 65101 vrf RED
  address-family l2vpn evpn
    advertise ipv4 unicast
  exit-address-family
end
...
```

{{< /tab >}}
{{< /tabs >}}

### Control RIB Routes

By default, when announcing IP prefixes in the BGP RIB as EVPN type-5 routes, the switch selects all routes in the BGP RIB to advertise as EVPN type-5 routes. You can use a route map to allow selective route advertisement from the BGP RIB.

The following commands add a route map filter to IPv4 EVPN type-5 route advertisement:

{{< tabs "TabID408 ">}}
{{< tab "NVUE Commands ">}}

```
cumulus@leaf01:~$ nv set vrf RED router bgp address-family ipv4-unicast route-export to-evpn route-map map1
```

{{< /tab >}}
{{< tab "vtysh Commands ">}}

```
cumulus@leaf01:~$ sudo vtysh

leaf01# configure terminal
leaf01(config)# router bgp 65101 vrf RED
leaf01(config-router)# address-family l2vpn evpn
leaf01(config-router-af)# advertise ipv4 unicast route-map map1
leaf01(config-router-af)# end
leaf01# write memory
leaf01# exit
cumulus@leaf01:~$
```

{{< /tab >}}
{{< /tabs >}}

<!-- vale off -->
### Originate Default EVPN Type-5 Routes
<!-- vale on -->
Cumulus Linux supports originating EVPN default type-5 routes. The default type-5 route originates from a border (exit) leaf and advertises to all the other leafs within the pod. Any leaf within the pod follows the default route towards the border leaf for all external traffic (towards the Internet or a different pod).

To originate a default type-5 route in EVPN:

{{< tabs "TabID384 ">}}
{{< tab "NVUE Commands ">}}

```
cumulus@leaf01:~$ nv set vrf RED router bgp address-family ipv4-unicast route-export to-evpn default-route-origination on
cumulus@leaf01:~$ nv set vrf RED router bgp address-family ipv6-unicast route-export to-evpn default-route-origination on
```

{{< /tab >}}
{{< tab "vtysh Commands ">}}

```
cumulus@leaf01:~$ sudo vtysh

leaf01# configure terminal
leaf01(config)# router bgp 65101 vrf RED
leaf01(config-router)# address-family l2vpn evpn
leaf01(config-router-af)# default-originate ipv4
leaf01(config-router-af)# default-originate ipv6
leaf01(config-router-af)# end
leaf01# write memory
```

{{< /tab >}}
{{< /tabs >}}

<!-- vale off -->
### Advertise Primary IP address (VXLAN Active-Active Mode)
<!-- vale on -->
In EVPN symmetric routing configurations with VXLAN active-active (<span class="a-tooltip">[MLAG](## "Multi-chassis Link Aggregation")</span>), all EVPN routes advertise with the anycast IP address as the next hop IP address and the anycast MAC address as the router MAC address. In a failure scenario, the switch might forward traffic to a leaf switch that does not have the destination routes. To prevent dropped traffic in this failure scenario, Cumulus Linux enables the Advertise Primary IP address feature by default so that the switch handles the next hop IP address of the VTEP conditionally depending on the route type: host type-2 (MAC/IP advertisement) or type-5 (IP prefix route).

- For host type-2 routes, the anycast IP address is the next hop IP address and the anycast MAC address is the router MAC address.
- For type-5 routes, the system IP address (the unique primary loopback IP address of the VTEP) is the next hop IP address and the unique router MAC address of the VTEP is the router MAC address.

For more information about VXLAN active-active, see {{<link title="VXLAN Active-active Mode" text="VXLAN Active-active Mode">}}.

#### Set the Anycast MAC Address

You set the anycast MAC address on both switches in the MLAG pair.

NVUE provides two commands to set the anycast MAC address globally. You can either:

- Set the anycast MAC address to a value in the reserved range between 44:38:39:ff:00:00 and 44:38:39:ff:ff:ff. Be sure to use an address in this reserved range to prevent MAC address conflicts with other interfaces in the same bridged network.
- Set an anycast MAC ID, from which Cumulus Linux derives the MAC address. You can specify a number between 1 and 65535. Cumulus Linux adds the number to the MAC address 44:38:39:ff:00:00 in hex. For example, if you specify 225, the anycast MAC address is 44:38:39:ff:00:FF.

If you use Linux commands to configure the switch instead of NVUE, add the `address-virtual <anycast-mac>` option under every VLAN interface in the` /etc/network/interfaces` file. Cumulus Linux does not provide a global anycast MAC address or MAC ID option in the `/etc/network/interfaces` file.

{{< tabs "TabID472 ">}}
{{< tab "NVUE Commands ">}}

To set the anycast MAC address:

```
cumulus@leaf01:~$ nv set system global anycast-mac 44:38:39:ff:00:ff
cumulus@leaf01:~$ nv config apply
```

To set the anycast MAC ID:

```
cumulus@leaf01:~$ nv set system global anycast-id 255
cumulus@leaf01:~$ nv config apply
```

{{< /tab >}}
{{< tab "Linux Commands ">}}

Edit the `/etc/network/interfaces` file and add `address-virtual <anycast-mac>` under each VLAN interface. For example:

```
cumulus@leaf01:~$ sudo nano /etc/network/interfaces
...
auto vlan4001
iface vlan4001
    address-virtual 44:38:39:BE:EF:AA
    vrf RED
    vlan-raw-device bridge
    vlan-id 4001
...
```

{{< /tab >}}
{{< /tabs >}}

The anycast MAC address is different from the {{<link url="Virtual-Router-Redundancy-VRR-and-VRRP/#change-the-vrr-mac-address" text="fabric-wide VRR MAC address">}}, which distributes the same VRR gateway on VLAN interfaces across switches fabric-wide. The following diagram shows the relationship between the anycast MAC address or ID, which is unique for each active-active pair, and the fabric MAC address or ID, which is consistent across the entire fabric.

{{< img src = "/images/cumulus-linux/anycast-fabric-address.png" >}}

{{%notice note%}}
When configuring third party networking devices using MLAG and EVPN for interoperability, you must configure and announce a single shared router MAC value for each advertised next hop IP address.
{{%/notice%}}

#### Disable Advertise Primary IP Address

Each switch in the MLAG pair advertises type-5 routes with its own system IP, which creates an additional next hop at the remote VTEPs. In a large multi-tenancy EVPN deployment, where additional resources are a concern, you can disable this feature.

To disable Advertise Primary IP Address:

{{< tabs "TabID560 ">}}
{{< tab "NVUE Commands ">}}

```
cumulus@leaf01:~$ nv set evpn route-advertise nexthop-setting shared-ip-mac
cumulus@leaf01:~$ nv config apply
```

To reenable Advertise Primary IP Address, run the `nv set evpn route-advertise nexthop-setting system-ip-mac` command.

{{< /tab >}}
{{< tab "vtysh Commands ">}}

```
cumulus@leaf01:~$ sudo vtysh
leaf01# configure terminal
leaf01(config)# router bgp 65101 vrf RED
leaf01(config)# address-family l2vpn evpn
leaf01(config)# no advertise-pip
leaf01(config-router-af)# end
leaf01# write memory
leaf01# exit
cumulus@leaf01:~$
```

To reenable Advertise Primary IP Address:

```
cumulus@leaf01:~$ sudo vtysh

leaf01# configure terminal
leaf01(config)# router bgp 65101 vrf RED
leaf01(config)# address-family l2vpn evpn
leaf01(config)# advertise-pip
leaf01(config-router-af)# end
leaf01# write memory
leaf01# exit
cumulus@leaf01:~$
```

{{< /tab >}}
{{< /tabs >}}

#### Show Advertise Primary IP Address Information

To show Advertise Primary IP Address parameters, run the vtysh `show bgp l2vpn evpn vni <vni>` command or the `net show bgp l2vpn evpn vni <vni>` command. For example:

```
cumulus@leaf01:~$ sudo vtysh
...
leaf01# show bgp l2vpn evpn vni 4001
VNI: 4001 (known to the kernel)
  Type: L3
  Tenant VRF: RED
  RD: 10.1.20.2:5
  Originator IP: 10.0.1.1
  Advertise-gw-macip : n/a
  Advertise-svi-macip : n/a
  Advertise-pip: Yes
  System-IP: 10.10.10.1
  System-MAC: 44:38:39:be:ef:aa
  Router-MAC: 44:38:39:be:ef:aa
  Import Route Target:
    65101:4001
  Export Route Target:
    65101:4001
```

To show EVPN routes with Primary IP Advertisement, run the vtysh `show bgp l2vpn evpn route` command or the `net show bgp l2vpn evpn route` command. For example:

```
cumulus@leaf01:~$ sudo vtysh
leaf01# show bgp l2vpn evpn route
...
Route Distinguisher: 10.10.10.1:3
*> [2]:[0]:[48]:[00:60:08:69:97:ef]
                    10.0.1.1                           32768 i
                    ET:8 RT:65101:10 RT:65101:4001 Rmac:44:38:39:be:ef:aa
*> [2]:[0]:[48]:[26:76:e6:93:32:78]
                    10.0.1.1                           32768 i
                    ET:8 RT:65101:10 RT:65101:4001 Rmac:44:38:39:be:ef:aa
*> [2]:[0]:[48]:[26:76:e6:93:32:78]:[32]:[10.1.10.101]
                    10.0.1.1                           32768 i
                    ET:8 RT:65101:10 RT:65101:4001 Rmac:44:38:39:be:ef:aa
...
```

To show the learned route from an external router injected as a type-5 route, run the vtysh `show bgp vrf <vrf> ipv4 unicast` command or the `net show bgp vrf <vrf> ipv4 unicast` command.

## Downstream VNI

Downstream VNI (symmetric EVPN route leaking) enables you to assign a VNI from a downstream remote VTEP through EVPN routes instead of configuring layer 3 VNIs globally across the network.

To configure a downstream VNI, you configure tenant VRFs as usual; however, to configure the desired route leaking, you define a route target import and, or export statement.

### Configure Route Targets

The route target import or export statement is in the format `route-target import|export <asn>:<vni>`; for example, `route-target import 65101:6000`. For route target *import* statements, you can use `route-target import ANY:<vni>` for NVUE commands or `route-target import *:<vni>` in the `/etc/frr/frr.conf` file. `ANY` in NVUE commands or the asterisk (*) in the `/etc/frr/frr.conf` file uses any ASN as a wildcard.

The NVUE commands are as follows:
- To configure a route import statement: `nv set vrf <vrf> router bgp route-import from-evpn route-target <asn>:<vni>`
- To configure a route export statement: `nv set vrf <vrf> router bgp route-export from-evpn route-target <asn>:<vni>`

{{%notice note%}}
- EVPN symmetric mode supports downstream VNI with layer 3 VNIs and single VXLAN devices only.
- You can configure multiple import and export route targets in a VRF.
- You can configure selective route targets for individual prefixes with routing policies.
- You cannot leak (import) overlapping tenant prefixes into the same destination VRF.
{{%/notice%}}

The following example shows a configuration with downstream VNI on leaf01 thru leaf04, and border01.
<!-- vale off -->
|   Traffic Flow between VRF RED and VRF 10  |     |
| ----------------------------------------------| ----|
| <img width=1300/> {{< img src="/images/cumulus-linux/evpn-downstream-vni-new.png"  >}}| <br><ol><li>server01 forwards traffic to leaf01.</li><li>leaf01 encapsulates the packet with the VNI in its route-target import statement (6000) and tunnels the traffic over to border01.</li><li> border01 uses the VNI received from leaf01 to forward the packet.</li><li> The reverse traffic from border01 to server01 is encapsulated with the VNI in the route-target import statement on border01 (4001) and tunneled over to leaf01, where routing occurs in VRF RED.</li></ul> |
<!-- vale on -->
The configuration for the example is below.
- On leaf01, you can see the route target (`route-target import 65163:6000`) under the `router bgp 65101 vrf RED` and `router bgp 65101 vrf BLUE` stanza of the `/etc/frr/frr.conf` file.
- On border01, you can see the route targets (`route-target import 65101:4001` and `route-target import 65101:4002`) under the `router bgp 65163 vrf VRF10` stanza of the `/etc/frr/frr.conf` file.

Because the configuration is similar on all the leafs, the example only shows configuration files for leaf01 and border01. For brevity, the example do not show the spine configuration files.

{{< tabs "TabID749 ">}}
{{< tab "NVUE Commands ">}}

{{< tabs "TabID767 ">}}
{{< tab "leaf01 ">}}

```
cumulus@leaf01:~$ nv set interface lo ip address 10.10.10.1/32
cumulus@leaf01:~$ nv set interface swp1-3,swp51-52
cumulus@leaf01:~$ nv set interface bond1 bond member swp1
cumulus@leaf01:~$ nv set interface bond2 bond member swp2
cumulus@leaf01:~$ nv set interface bond3 bond member swp3
cumulus@leaf01:~$ nv set interface bond1 bond lacp-bypass on
cumulus@leaf01:~$ nv set interface bond2 bond lacp-bypass on
cumulus@leaf01:~$ nv set interface bond3 bond lacp-bypass on
cumulus@leaf01:~$ nv set interface bond1 link mtu 9000
cumulus@leaf01:~$ nv set interface bond2 link mtu 9000
cumulus@leaf01:~$ nv set interface bond3 link mtu 9000
cumulus@leaf01:~$ nv set interface bond1-3 bridge domain br_default
cumulus@leaf01:~$ nv set interface bond1 bridge domain br_default access 10
cumulus@leaf01:~$ nv set interface bond2 bridge domain br_default access 20
cumulus@leaf01:~$ nv set interface bond3 bridge domain br_default access 30
cumulus@leaf01:~$ nv set bridge domain br_default vlan 10,20,30
cumulus@leaf01:~$ nv set interface vlan10 ip address 10.1.10.2/24
cumulus@leaf01:~$ nv set interface vlan10 ip vrr address 10.1.10.1/24
cumulus@leaf01:~$ nv set interface vlan10 ip vrr mac-address 00:00:00:00:00:10
cumulus@leaf01:~$ nv set interface vlan10 ip vrr state up
cumulus@leaf01:~$ nv set interface vlan20 ip address 10.1.20.2/24
cumulus@leaf01:~$ nv set interface vlan20 ip vrr address 10.1.20.1/24
cumulus@leaf01:~$ nv set interface vlan20 ip vrr mac-address 00:00:00:00:00:20
cumulus@leaf01:~$ nv set interface vlan20 ip vrr state up
cumulus@leaf01:~$ nv set interface vlan30 ip address 10.1.30.2/24
cumulus@leaf01:~$ nv set interface vlan30 ip vrr address 10.1.30.1/24
cumulus@leaf01:~$ nv set interface vlan30 ip vrr mac-address 00:00:00:00:00:30
cumulus@leaf01:~$ nv set interface vlan30 ip vrr state up
cumulus@leaf01:~$ nv set vrf RED
cumulus@leaf01:~$ nv set vrf BLUE
cumulus@leaf01:~$ nv set bridge domain br_default vlan 10 vni 10
cumulus@leaf01:~$ nv set bridge domain br_default vlan 20 vni 20
cumulus@leaf01:~$ nv set bridge domain br_default vlan 30 vni 30
cumulus@leaf01:~$ nv set interface vlan10 ip vrf RED
cumulus@leaf01:~$ nv set interface vlan20 ip vrf RED
cumulus@leaf01:~$ nv set interface vlan30 ip vrf BLUE
cumulus@leaf01:~$ nv set nve vxlan source address 10.10.10.1
cumulus@leaf01:~$ nv set nve vxlan arp-nd-suppress on 
cumulus@leaf01:~$ nv set vrf RED evpn vni 4001
cumulus@leaf01:~$ nv set vrf BLUE evpn vni 4002
cumulus@leaf01:~$ nv set system global anycast-mac 44:38:39:BE:EF:AA
cumulus@leaf01:~$ nv set evpn enable on
cumulus@leaf01:~$ nv set router bgp autonomous-system 65101
cumulus@leaf01:~$ nv set router bgp router-id 10.10.10.1
cumulus@leaf01:~$ nv set vrf default router bgp peer-group underlay remote-as external
cumulus@leaf01:~$ nv set vrf default router bgp neighbor swp51 peer-group underlay
cumulus@leaf01:~$ nv set vrf default router bgp neighbor swp52 peer-group underlay
cumulus@leaf01:~$ nv set vrf default router bgp peer-group underlay address-family l2vpn-evpn enable on
cumulus@leaf01:~$ nv set vrf default router bgp address-family ipv4-unicast redistribute connected enable on
cumulus@leaf01:~$ nv set vrf RED router bgp autonomous-system 65101
cumulus@leaf01:~$ nv set vrf RED router bgp router-id 10.10.10.1
cumulus@leaf01:~$ nv set vrf RED router bgp address-family ipv4-unicast redistribute connected enable on
cumulus@leaf01:~$ nv set vrf RED router bgp address-family ipv4-unicast route-export to-evpn
cumulus@leaf01:~$ nv set vrf RED router bgp route-import from-evpn route-target 65163:6000
cumulus@leaf01:~$ nv set vrf BLUE router bgp autonomous-system 65101
cumulus@leaf01:~$ nv set vrf BLUE router bgp router-id 10.10.10.1
cumulus@leaf01:~$ nv set vrf BLUE router bgp address-family ipv4-unicast redistribute connected enable on
cumulus@leaf01:~$ nv set vrf BLUE router bgp address-family ipv4-unicast route-export to-evpn
cumulus@leaf01:~$ nv set vrf BLUE router bgp route-import from-evpn route-target 65163:6000
cumulus@leaf01:~$ nv set evpn multihoming enable on
cumulus@leaf01:~$ nv set interface bond1 evpn multihoming segment local-id 1
cumulus@leaf01:~$ nv set interface bond2 evpn multihoming segment local-id 2
cumulus@leaf01:~$ nv set interface bond3 evpn multihoming segment local-id 3
cumulus@leaf01:~$ nv set interface bond1-3 evpn multihoming segment mac-address 44:38:39:BE:EF:AA
cumulus@leaf01:~$ nv set interface bond1-3 evpn multihoming segment df-preference 50000
cumulus@leaf01:~$ nv set interface swp51-52 evpn multihoming uplink on
cumulus@leaf01:~$ nv config apply
```

{{< /tab >}}
{{< tab "border01 ">}}

```
cumulus@border01:~$ nv set interface lo ip address 10.10.10.63/32
cumulus@border01:~$ nv set interface swp1-3,swp51-52
cumulus@border01:~$ nv set interface bond1 bond member swp1
cumulus@border01:~$ nv set interface bond2 bond member swp2
cumulus@border01:~$ nv set interface bond3 bond member swp3
cumulus@border01:~$ nv set interface bond1 bond lacp-bypass on
cumulus@border01:~$ nv set interface bond2 bond lacp-bypass on
cumulus@border01:~$ nv set interface bond3 bond lacp-bypass on
cumulus@border01:~$ nv set interface bond1 link mtu 9000
cumulus@border01:~$ nv set interface bond2 link mtu 9000
cumulus@border01:~$ nv set interface bond3 link mtu 9000
cumulus@border01:~$ nv set interface bond1-3 bridge domain br_default
cumulus@border01:~$ nv set interface bond1 bridge domain br_default access 2001
cumulus@border01:~$ nv set interface bond2 bridge domain br_default access 2002
cumulus@border01:~$ nv set interface bond3 bridge domain br_default access 2010
cumulus@border01:~$ nv set interface vlan2001 ip address 10.1.201.1/24
cumulus@border01:~$ nv set interface vlan2002 ip address 10.1.202.1/24
cumulus@border01:~$ nv set interface vlan2010 ip address 10.1.210.1/24
cumulus@border01:~$ nv set bridge domain br_default vlan 2001,2002,2010
cumulus@border01:~$ nv set vrf VRF10
cumulus@border01:~$ nv set vrf EXTERNAL1
cumulus@border01:~$ nv set vrf EXTERNAL2
cumulus@border01:~$ nv set bridge domain br_default vlan 2001 vni 2001
cumulus@border01:~$ nv set bridge domain br_default vlan 2002 vni 2002
cumulus@border01:~$ nv set bridge domain br_default vlan 2010 vni 2010
cumulus@border01:~$ nv set interface vlan2001 ip vrf EXTERNAL1
cumulus@border01:~$ nv set interface vlan2002 ip vrf EXTERNAL2
cumulus@border01:~$ nv set interface vlan2010 ip vrf VRF10
cumulus@border01:~$ nv set nve vxlan source address 10.10.10.63
cumulus@border01:~$ nv set nve vxlan arp-nd-suppress on 
cumulus@border01:~$ nv set vrf VRF10 evpn vni 6000
cumulus@border01:~$ nv set system global anycast-mac 44:38:39:BE:EF:FF
cumulus@border01:~$ nv set evpn enable on
cumulus@border01:~$ nv set router bgp autonomous-system 65163
cumulus@border01:~$ nv set router bgp router-id 10.10.10.63
cumulus@border01:~$ nv set vrf default router bgp peer-group underlay remote-as external
cumulus@border01:~$ nv set vrf default router bgp neighbor swp51 peer-group underlay
cumulus@border01:~$ nv set vrf default router bgp neighbor swp52 peer-group underlay
cumulus@border01:~$ nv set vrf default router bgp peer-group underlay address-family l2vpn-evpn enable on
cumulus@border01:~$ nv set vrf default router bgp address-family ipv4-unicast redistribute connected enable on
cumulus@border01:~$ nv set vrf VRF10 router bgp autonomous-system 65163
cumulus@border01:~$ nv set vrf VRF10 router bgp router-id 10.10.10.63
cumulus@border01:~$ nv set vrf VRF10 router bgp address-family ipv4-unicast redistribute connected enable on
cumulus@border01:~$ nv set vrf VRF10 router bgp peer-group underlay address-family l2vpn-evpn enable on
cumulus@border01:~$ nv set vrf VRF10 router bgp address-family ipv4-unicast route-export to-evpn
cumulus@border01:~$ nv set vrf VRF10 router bgp route-import from-evpn route-target 65101:4001
cumulus@border01:~$ nv set vrf VRF10 router bgp route-import from-evpn route-target 65101:4002
cumulus@border01:~$ nv set vrf EXTERNAL1 router bgp autonomous-system 65163
cumulus@border01:~$ nv set vrf EXTERNAL1 router bgp router-id 10.10.10.63
cumulus@border01:~$ nv set vrf EXTERNAL1 router bgp address-family ipv4-unicast redistribute connected enable on
cumulus@border01:~$ nv set vrf EXTERNAL1 router bgp peer-group underlay address-family l2vpn-evpn enable on
cumulus@border01:~$ nv set vrf EXTERNAL1 router bgp address-family ipv4-unicast route-export to-evpn
cumulus@border01:~$ nv set vrf EXTERNAL2 router bgp autonomous-system 65163
cumulus@border01:~$ nv set vrf EXTERNAL2 router bgp router-id 10.10.10.63
cumulus@border01:~$ nv set vrf EXTERNAL2 router bgp address-family ipv4-unicast redistribute connected enable on
cumulus@border01:~$ nv set vrf EXTERNAL2 router bgp peer-group underlay address-family l2vpn-evpn enable on
cumulus@border01:~$ nv set vrf EXTERNAL2 router bgp address-family ipv4-unicast route-export to-evpn
cumulus@border01:~$ nv config apply
```

{{< /tab >}}
{{< /tabs >}}

{{< /tab >}}
{{< tab "/etc/nvue.d/startup.yaml ">}}

{{< tabs "TabID841 ">}}
{{< tab "leaf01 ">}}

```
cumulus@leaf01:~$ sudo cat /etc/nvue.d/startup.yaml
- set:
    bridge:
      domain:
        br_default:
          vlan:
            '10':
              vni:
                '10': {}
            '20':
              vni:
                '20': {}
            '30':
              vni:
                '30': {}
    evpn:
      enable: on
      multihoming:
        enable: on
    interface:
      bond1:
        bond:
          lacp-bypass: on
          member:
            swp1: {}
        bridge:
          domain:
            br_default:
              access: 10
        evpn:
          multihoming:
            segment:
              df-preference: 50000
              enable: on
              local-id: 1
              mac-address: 44:38:39:BE:EF:AA
        link:
          mtu: 9000
        type: bond
      bond2:
        bond:
          lacp-bypass: on
          member:
            swp2: {}
        bridge:
          domain:
            br_default:
              access: 20
        evpn:
          multihoming:
            segment:
              df-preference: 50000
              enable: on
              local-id: 2
              mac-address: 44:38:39:BE:EF:AA
        link:
          mtu: 9000
        type: bond
      bond3:
        bond:
          lacp-bypass: on
          member:
            swp3: {}
        bridge:
          domain:
            br_default:
              access: 30
        evpn:
          multihoming:
            segment:
              df-preference: 50000
              enable: on
              local-id: 3
              mac-address: 44:38:39:BE:EF:AA
        link:
          mtu: 9000
        type: bond
      lo:
        ip:
          address:
            10.10.10.1/32: {}
        type: loopback
      swp1:
        type: swp
      swp2:
        type: swp
      swp3:
        type: swp
      swp51:
        evpn:
          multihoming:
            uplink: on
        type: swp
      swp52:
        evpn:
          multihoming:
            uplink: on
        type: swp
      vlan10:
        ip:
          address:
            10.1.10.2/24: {}
          vrf: RED
          vrr:
            address:
              10.1.10.1/24: {}
            enable: on
            mac-address: 00:00:00:00:00:10
            state:
              up: {}
        type: svi
        vlan: 10
      vlan20:
        ip:
          address:
            10.1.20.2/24: {}
          vrf: RED
          vrr:
            address:
              10.1.20.1/24: {}
            enable: on
            mac-address: 00:00:00:00:00:20
            state:
              up: {}
        type: svi
        vlan: 20
      vlan30:
        ip:
          address:
            10.1.30.2/24: {}
          vrf: BLUE
          vrr:
            address:
              10.1.30.1/24: {}
            enable: on
            mac-address: 00:00:00:00:00:30
            state:
              up: {}
        type: svi
        vlan: 30
    nve:
      vxlan:
        arp-nd-suppress: on
        enable: on
        source:
          address: 10.10.10.1
    router:
      bgp:
        autonomous-system: 65101
        enable: on
        router-id: 10.10.10.1
      vrr:
        enable: on
    system:
      global:
        anycast-mac: 44:38:39:BE:EF:AA
    vrf:
      BLUE:
        evpn:
          enable: on
          vni:
            '4002': {}
        router:
          bgp:
            address-family:
              ipv4-unicast:
                enable: on
                redistribute:
                  connected:
                    enable: on
                route-export:
                  to-evpn:
                    enable: on
            autonomous-system: 65101
            enable: on
            route-import:
              from-evpn:
                route-target:
                  65163:6000: {}
            router-id: 10.10.10.1
      RED:
        evpn:
          enable: on
          vni:
            '4001': {}
        router:
          bgp:
            address-family:
              ipv4-unicast:
                enable: on
                redistribute:
                  connected:
                    enable: on
                route-export:
                  to-evpn:
                    enable: on
            autonomous-system: 65101
            enable: on
            route-import:
              from-evpn:
                route-target:
                  65163:6000: {}
            router-id: 10.10.10.1
      default:
        router:
          bgp:
            address-family:
              ipv4-unicast:
                enable: on
                redistribute:
                  connected:
                    enable: on
            enable: on
            neighbor:
              swp51:
                peer-group: underlay
                type: unnumbered
              swp52:
                peer-group: underlay
                type: unnumbered
            peer-group:
              underlay:
                address-family:
                  l2vpn-evpn:
                    enable: on
                remote-as: external
```

{{< /tab >}}
{{< tab "border01 ">}}

```
cumulus@border01:~$ sudo cat /etc/nvue.d/startup.yaml
- set:
    bridge:
      domain:
        br_default:
          vlan:
            '2001':
              vni:
                '2001': {}
            '2002':
              vni:
                '2002': {}
            '2010':
              vni:
                '2010': {}
    evpn:
      enable: on
      multihoming: {}
    interface:
      bond1:
        bond:
          lacp-bypass: on
          member:
            swp1: {}
        bridge:
          domain:
            br_default:
              access: 2001
        evpn:
          multihoming: {}
        link:
          mtu: 9000
        type: bond
      bond2:
        bond:
          lacp-bypass: on
          member:
            swp2: {}
        bridge:
          domain:
            br_default:
              access: 2002
        evpn:
          multihoming: {}
        link:
          mtu: 9000
        type: bond
      bond3:
        bond:
          lacp-bypass: on
          member:
            swp3: {}
        bridge:
          domain:
            br_default:
              access: 2010
        evpn:
          multihoming: {}
        link:
          mtu: 9000
        type: bond
      lo:
        ip:
          address:
            10.10.10.63/32: {}
        type: loopback
      swp1:
        type: swp
      swp2:
        type: swp
      swp3:
        type: swp
      swp51:
        evpn:
          multihoming: {}
        type: swp
      swp52:
        evpn:
          multihoming: {}
        type: swp
      vlan2001:
        ip:
          address:
            10.1.201.1/24: {}
          vrf: EXTERNAL1
        type: svi
        vlan: 2001
      vlan2002:
        ip:
          address:
            10.1.202.1/24: {}
          vrf: EXTERNAL2
        type: svi
        vlan: 2002
      vlan2010:
        ip:
          address:
            10.1.210.1/24: {}
          vrf: VRF10
        type: svi
        vlan: 2010
    nve:
      vxlan:
        arp-nd-suppress: on
        enable: on
        source:
          address: 10.10.10.63
    router:
      bgp:
        autonomous-system: 65163
        enable: on
        router-id: 10.10.10.63
    system:
      global:
        anycast-mac: 44:38:39:BE:EF:FF
        system-mac: 44:38:39:22:01:74
      hostname: border01
    vrf:
      EXTERNAL1:
        router:
          bgp:
            address-family:
              ipv4-unicast:
                enable: on
                redistribute:
                  connected:
                    enable: on
                route-export:
                  to-evpn:
                    enable: on
            autonomous-system: 65163
            enable: on
            peer-group:
              underlay:
                address-family:
                  l2vpn-evpn:
                    enable: on
            router-id: 10.10.10.63
      EXTERNAL2:
        router:
          bgp:
            address-family:
              ipv4-unicast:
                enable: on
                redistribute:
                  connected:
                    enable: on
                route-export:
                  to-evpn:
                    enable: on
            autonomous-system: 65163
            enable: on
            peer-group:
              underlay:
                address-family:
                  l2vpn-evpn:
                    enable: on
            router-id: 10.10.10.63
      VRF10:
        evpn:
          enable: on
          vni:
            '6000': {}
        router:
          bgp:
            address-family:
              ipv4-unicast:
                enable: on
                redistribute:
                  connected:
                    enable: on
                route-export:
                  to-evpn:
                    enable: on
            autonomous-system: 65163
            enable: on
            peer-group:
              underlay:
                address-family:
                  l2vpn-evpn:
                    enable: on
            route-import:
              from-evpn:
                route-target:
                  65101:4001: {}
                  65101:4002: {}
            router-id: 10.10.10.63
      default:
        router:
          bgp:
            address-family:
              ipv4-unicast:
                enable: on
                redistribute:
                  connected:
                    enable: on
            enable: on
            neighbor:
              swp51:
                peer-group: underlay
                type: unnumbered
              swp52:
                peer-group: underlay
                type: unnumbered
            peer-group:
              underlay:
                address-family:
                  l2vpn-evpn:
                    enable: on
                remote-as: external

```

{{< /tab >}}
{{< /tabs >}}

{{< /tab >}}
{{< tab "/etc/network/interfaces ">}}

{{< tabs "TabID752 ">}}
{{< tab "leaf01 ">}}

```
cumulus@leaf01:~$ sudo cat /etc/network/interfaces
...
auto lo
iface lo inet loopback
    address 10.10.10.1/32
    vxlan-local-tunnelip 10.10.10.1
auto mgmt
iface mgmt
    address 127.0.0.1/8
    address ::1/128
    vrf-table auto
auto RED
iface RED
    vrf-table auto
auto BLUE
iface BLUE
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
auto swp51
iface swp51
auto swp52
iface swp52
auto bond1
iface bond1
    mtu 9000
    es-sys-mac 44:38:39:BE:EF:AA
    bond-slaves swp1
    bond-mode 802.3ad
    bond-lacp-bypass-allow yes
    bridge-access 10
auto bond2
iface bond2
    mtu 9000
    es-sys-mac 44:38:39:BE:EF:AA
    bond-slaves swp2
    bond-mode 802.3ad
    bond-lacp-bypass-allow yes
    bridge-access 20
auto bond3
iface bond3
    mtu 9000
    es-sys-mac 44:38:39:BE:EF:AA
    bond-slaves swp3
    bond-mode 802.3ad
    bond-lacp-bypass-allow yes
    bridge-access 30
auto vlan10
iface vlan10
    address 10.1.10.2/24
    address-virtual 00:00:00:00:00:10 10.1.10.1/24
    hwaddress 44:38:39:22:01:b1
    vrf RED
    vlan-raw-device br_default
    vlan-id 10
auto vlan20
iface vlan20
    address 10.1.20.2/24
    address-virtual 00:00:00:00:00:20 10.1.20.1/24
    hwaddress 44:38:39:22:01:b1
    vrf RED
    vlan-raw-device br_default
    vlan-id 20
auto vlan30
iface vlan30
    address 10.1.30.2/24
    address-virtual 00:00:00:00:00:30 10.1.30.1/24
    hwaddress 44:38:39:22:01:b1
    vrf BLUE
    vlan-raw-device br_default
    vlan-id 30
auto vxlan48
iface vxlan48
    bridge-vlan-vni-map 10=10 20=20 30=30
    bridge-vids 10 20 30
    bridge-learning off
auto vlan220_l3
iface vlan220_l3
    vrf RED
    vlan-raw-device br_l3vni
    vlan-id 220
auto vlan297_l3
iface vlan297_l3
    vrf BLUE
    vlan-raw-device br_l3vni
    vlan-id 297
auto vxlan99
iface vxlan99
    bridge-vlan-vni-map 220=4001 297=4002
    bridge-vids 220 297
    bridge-learning off
auto br_default
iface br_default
    bridge-ports bond1 bond2 bond3 vxlan48
    hwaddress 44:38:39:22:01:b1
    bridge-vlan-aware yes
    bridge-vids 10 20 30
    bridge-pvid 1
auto br_l3vni
iface br_l3vni
    bridge-ports vxlan99
    hwaddress 44:38:39:22:01:b1
    bridge-vlan-aware yes
```

{{< /tab >}}
{{< tab "border01 ">}}

```
cumulus@border01:~$ sudo cat /etc/network/interfaces
...
auto lo
iface lo inet loopback
    address 10.10.10.63/32
    vxlan-local-tunnelip 10.10.10.63
auto mgmt
iface mgmt
    address 127.0.0.1/8
    address ::1/128
    vrf-table auto
auto EXTERNAL1
iface EXTERNAL1
    vrf-table auto
auto EXTERNAL2
iface EXTERNAL2
    vrf-table auto
auto VRF10
iface VRF10
    vrf-table auto
auto eth0
iface eth0 inet dhcp
    ip-forward off
    ip6-forward off
    vrf mgmt
auto bond1
iface bond1
    mtu 9000
    bond-slaves swp1
    bond-mode 802.3ad
    bond-lacp-bypass-allow yes
    bridge-access 2001
auto bond2
iface bond2
    mtu 9000
    bond-slaves swp2
    bond-mode 802.3ad
    bond-lacp-bypass-allow yes
    bridge-access 2002
auto bond3
iface bond3
    mtu 9000
    bond-slaves swp3
    bond-mode 802.3ad
    bond-lacp-bypass-allow yes
    bridge-access 2010
auto swp1
iface swp1
auto swp2
iface swp2
auto swp3
iface swp3
auto swp51
iface swp51
auto swp52
iface swp52
auto vlan2001
iface vlan2001
    address 10.1.201.1/24
    hwaddress 44:38:39:22:01:74
    vrf EXTERNAL1
    vlan-raw-device br_default
    vlan-id 2001
auto vlan2002
iface vlan2002
    address 10.1.202.1/24
    hwaddress 44:38:39:22:01:74
    vrf EXTERNAL2
    vlan-raw-device br_default
    vlan-id 2002
auto vlan2010
iface vlan2010
    address 10.1.210.1/24
    hwaddress 44:38:39:22:01:74
    vrf VRF10
    vlan-raw-device br_default
    vlan-id 2010
auto vxlan48
iface vxlan48
    bridge-vlan-vni-map 2001=2001 2002=2002 2010=2010
    bridge-learning off
auto vlan336_l3
iface vlan336_l3
    vrf VRF10
    vlan-raw-device br_l3vni
    vlan-id 336
auto vxlan99
iface vxlan99
    bridge-vlan-vni-map 336=6000
    bridge-learning off
auto br_default
iface br_default
    bridge-ports bond1 bond2 bond3 vxlan48
    hwaddress 44:38:39:22:01:74
    bridge-vlan-aware yes
    bridge-vids 2001 2002 2010
    bridge-pvid 1
auto br_l3vni
iface br_l3vni
    bridge-ports vxlan99
    hwaddress 44:38:39:22:01:74
    bridge-vlan-aware yes
```

{{< /tab >}}
{{< /tabs >}}

{{< /tab >}}
{{< tab "/etc/frr/frr.conf ">}}

{{< tabs "TabID1018 ">}}
{{< tab "leaf01 ">}}

```
cumulus@leaf01:~$ sudo cat /etc/frr/frr.conf
...
evpn mh mac-holdtime 1080
evpn mh neigh-holdtime 1080
evpn mh startup-delay 180
interface bond1
evpn mh es-df-pref 50000
evpn mh es-id 1
evpn mh es-sys-mac 44:38:39:BE:EF:AA
interface bond2
evpn mh es-df-pref 50000
evpn mh es-id 2
evpn mh es-sys-mac 44:38:39:BE:EF:AA
interface bond3
evpn mh es-df-pref 50000
evpn mh es-id 3
evpn mh es-sys-mac 44:38:39:BE:EF:AA
interface swp51
evpn mh uplink
interface swp52
evpn mh uplink
vrf BLUE
vni 4002
exit-vrf
vrf RED
vni 4001
exit-vrf
vrf default
exit-vrf
vrf mgmt
exit-vrf
router bgp 65101 vrf default
bgp router-id 10.10.10.1
timers bgp 3 9
bgp deterministic-med
! Neighbors
neighbor underlay peer-group
neighbor underlay remote-as external
neighbor underlay timers 3 9
neighbor underlay timers connect 10
neighbor underlay advertisement-interval 0
no neighbor underlay capability extended-nexthop
neighbor swp51 interface peer-group underlay
neighbor swp51 timers 3 9
neighbor swp51 timers connect 10
neighbor swp51 advertisement-interval 0
neighbor swp51 capability extended-nexthop
neighbor swp52 interface peer-group underlay
neighbor swp52 timers 3 9
neighbor swp52 timers connect 10
neighbor swp52 advertisement-interval 0
neighbor swp52 capability extended-nexthop
! Address families
address-family ipv4 unicast
redistribute connected
maximum-paths ibgp 64
maximum-paths 64
distance bgp 20 200 200
neighbor swp51 activate
neighbor swp52 activate
neighbor underlay activate
exit-address-family
address-family l2vpn evpn
advertise-all-vni
neighbor swp51 activate
neighbor swp52 activate
neighbor underlay activate
exit-address-family
! end of router bgp 65101 vrf default
router bgp 65101 vrf RED
bgp router-id 10.10.10.1
timers bgp 3 9
bgp deterministic-med
! Neighbors
! Address families
address-family ipv4 unicast
redistribute connected
maximum-paths ibgp 64
maximum-paths 64
distance bgp 20 200 200
exit-address-family
address-family l2vpn evpn
advertise ipv4 unicast
route-target import 65163:6000
exit-address-family
! end of router bgp 65101 vrf RED
router bgp 65101 vrf BLUE
bgp router-id 10.10.10.1
timers bgp 3 9
bgp deterministic-med
! Neighbors
! Address families
address-family ipv4 unicast
redistribute connected
maximum-paths ibgp 64
maximum-paths 64
distance bgp 20 200 200
exit-address-family
address-family l2vpn evpn
advertise ipv4 unicast
route-target import 65163:6000
exit-address-family
! end of router bgp 65101 vrf BLUE
```

{{< /tab >}}
{{< tab "border01 ">}}

```
cumulus@border01:~$ sudo cat /etc/frr/frr.conf
vrf EXTERNAL1
exit-vrf
vrf EXTERNAL2
exit-vrf
vrf VRF10
vni 6000
exit-vrf
vrf default
exit-vrf
vrf mgmt
exit-vrf
router bgp 65163 vrf default
bgp router-id 10.10.10.63
timers bgp 3 9
bgp deterministic-med
! Neighbors
neighbor underlay peer-group
neighbor underlay remote-as external
neighbor underlay timers 3 9
neighbor underlay timers connect 10
neighbor underlay advertisement-interval 0
no neighbor underlay capability extended-nexthop
neighbor swp51 interface peer-group underlay
neighbor swp51 timers 3 9
neighbor swp51 timers connect 10
neighbor swp51 advertisement-interval 0
neighbor swp51 capability extended-nexthop
neighbor swp52 interface peer-group underlay
neighbor swp52 timers 3 9
neighbor swp52 timers connect 10
neighbor swp52 advertisement-interval 0
neighbor swp52 capability extended-nexthop
! Address families
address-family ipv4 unicast
redistribute connected
maximum-paths ibgp 64
maximum-paths 64
distance bgp 20 200 200
neighbor swp51 activate
neighbor swp52 activate
neighbor underlay activate
exit-address-family
address-family l2vpn evpn
advertise-all-vni
neighbor swp51 activate
neighbor swp52 activate
neighbor underlay activate
exit-address-family
! end of router bgp 65163 vrf default
router bgp 65163 vrf EXTERNAL1
bgp router-id 10.10.10.63
timers bgp 3 9
bgp deterministic-med
! Neighbors
neighbor underlay peer-group
neighbor underlay timers 3 9
neighbor underlay timers connect 10
neighbor underlay advertisement-interval 0
no neighbor underlay capability extended-nexthop
! Address families
address-family ipv4 unicast
redistribute connected
maximum-paths ibgp 64
maximum-paths 64
distance bgp 20 200 200
neighbor underlay activate
exit-address-family
address-family l2vpn evpn
advertise ipv4 unicast
neighbor underlay activate
exit-address-family
! end of router bgp 65163 vrf EXTERNAL1
router bgp 65163 vrf EXTERNAL2
bgp router-id 10.10.10.63
timers bgp 3 9
bgp deterministic-med
! Neighbors
neighbor underlay peer-group
neighbor underlay timers 3 9
neighbor underlay timers connect 10
neighbor underlay advertisement-interval 0
no neighbor underlay capability extended-nexthop
! Address families
address-family ipv4 unicast
redistribute connected
maximum-paths ibgp 64
maximum-paths 64
distance bgp 20 200 200
neighbor underlay activate
exit-address-family
address-family l2vpn evpn
advertise ipv4 unicast
neighbor underlay activate
exit-address-family
! end of router bgp 65163 vrf EXTERNAL2
router bgp 65163 vrf VRF10
bgp router-id 10.10.10.63
timers bgp 3 9
bgp deterministic-med
! Neighbors
neighbor underlay peer-group
neighbor underlay timers 3 9
neighbor underlay timers connect 10
neighbor underlay advertisement-interval 0
no neighbor underlay capability extended-nexthop
! Address families
address-family ipv4 unicast
redistribute connected
maximum-paths ibgp 64
maximum-paths 64
distance bgp 20 200 200
neighbor underlay activate
exit-address-family
address-family l2vpn evpn
advertise ipv4 unicast
route-target import 65101:4001
route-target import 65101:4002
neighbor underlay activate
exit-address-family
! end of router bgp 65163 vrf VRF10
```

{{< /tab >}}
{{< /tabs >}}

{{< /tab >}}
{{< tab "Try It " >}}
    {{< simulation name="Try It CL55 - DVNI" showNodes="leaf01,spine01,border01,server01,fw1" >}}

This simulation starts with the example downstream VNI configuration. To simplify the example, only one spine is in the topology. The demo is pre-configured using {{<exlink url="https://docs.nvidia.com/networking-ethernet-software/cumulus-linux/System-Configuration/NVIDIA-User-Experience-NVUE/" text="NVUE">}} commands.

- **fw1** has IP address 10.1.210.254 configured beyond border01 in VRF10.
- **server01** has IP address 10.1.10.101 as in the example.

To validate the configuration, run the verification commands shown below.

{{< /tab >}}
{{< /tabs >}}

### Verify Configuration

To verify the configuration, check that the routes are properly received and tagged:

{{< tabs "TabID1187 ">}}
{{< tab "leaf01 ">}}

The following vtysh command on leaf01 shows the route from border01 tagged with route target 6000

```
cumulus@leaf01:~$ sudo vtysh
leaf01# show bgp l2vpn evpn route type prefix
...
Route Distinguisher: 10.10.10.63:3
*> [5]:[0]:[24]:[10.1.210.0]
                    10.10.10.63                            0 65222 65163 ?
                    RT:65163:6000 ET:8 Rmac:44:38:39:22:01:b3
...
```

The following Linux command on leaf01 shows the encapsulated ID (6000) on the routes:

```
cumulus@leaf01:mgmt:~$ ip route show vrf RED 10.1.210.0/24
10.1.210.0/24  encap ip id 6000 src 0.0.0.0 dst 10.10.10.63 ttl 0 tos 0 via 10.10.10.63 dev vxlan99 proto bgp metric 20 onlink
```

{{< /tab >}}
{{< tab "border01 ">}}

The following vtysh command on border01 shows the routes from leaf01 tagged with route targets 4001 and 4002:

```
cumulus@border01:~$ sudo vtysh
border01# show bgp l2vpn evpn route type prefix
...
Route Distinguisher: 10.10.10.1:2
*> [5]:[0]:[24]:[10.1.10.0]
                    10.10.10.1                             0 65222 65101 ?
                    RT:65101:4001 ET:8 Rmac:44:38:39:22:01:b1
*> [5]:[0]:[24]:[10.1.20.0]
                    10.10.10.1                             0 65222 65101 ?
                    RT:65101:4001 ET:8 Rmac:44:38:39:22:01:b1
Route Distinguisher: 10.10.10.1:3
*> [5]:[0]:[24]:[10.1.30.0]
                    10.10.10.1                             0 65222 65101 ?
                    RT:65101:4002 ET:8 Rmac:44:38:39:22:01:b1
...
```

The following Linux command on border01 shows the encapsulated IDs (4001 and 4002) on the routes:

```
cumulus@border01:mgmt:~$ ip route show vrf VRF10
10.1.10.0/24  encap ip id 4001 src 0.0.0.0 dst 10.10.10.1 ttl 0 tos 0 via 10.10.10.1 dev vxlan99 proto bgp metric 20 onlink 
10.1.20.0/24  encap ip id 4001 src 0.0.0.0 dst 10.10.10.1 ttl 0 tos 0 via 10.10.10.1 dev vxlan99 proto bgp metric 20 onlink 
10.1.30.0/24  encap ip id 4002 src 0.0.0.0 dst 10.10.10.1 ttl 0 tos 0 via 10.10.10.1 dev vxlan99 proto bgp metric 20 onlink 
...
```

{{< /tab >}}
{{< /tabs >}}

## Considerations

### Centralized Routing with ARP Suppression Enabled on the Gateway

In an EVPN centralized routing configuration, where the layer 2 network extends beyond VTEPs, (for example, a host with bridges), the gateway MAC address does not refresh in the network when ARP suppression exists on the gateway. To work around this issue, disable ARP suppression on the centralized gateway.
<!-- vale off -->

### Symmetric Routing and the Same SVI IP Address Across Racks

In EVPN symmetric routing, if you use the same SVI IP address across racks (for example, if the SVI IP address for a specific VLAN interface (such as vlan100) is the same on all VTEPs where this SVI is present):

- You cannot use ping between SVI IP addresses to verify connectivity between VTEPs because either the local rack itself uses the ping destination IP address or remote racks use the ping destination IP address.
- If you use ping from a host to the SVI IP address, sometimes, the local VTEP (gateway) does not reply if the host has an ARP entry from a remote gateway.

Host-to-host traffic does not have these issues.
