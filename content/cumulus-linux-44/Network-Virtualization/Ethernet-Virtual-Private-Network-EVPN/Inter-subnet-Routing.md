---
title: Inter-subnet Routing
author: NVIDIA
weight: 565
toc: 4
---
There are multiple models in EVPN for routing between different subnets (VLANs), also known as inter-VLAN routing. The model you choose depends if every VTEP acts as a layer 3 gateway and performs routing or if only specific VTEPs perform routing, and if routing is performed only at the ingress of the VXLAN tunnel or both the ingress and the egress of the VXLAN tunnel.

Cumulus Linux supports these models:

- {{<link url="#centralized-routing" text="Centralized routing">}}: Specific VTEPs act as designated layer 3 gateways and perform routing between subnets; other VTEPs just perform bridging.
<!--- {{<link url="#asymmetric-routing" text="Distributed asymmetric routing">}}: Every VTEP participates in routing, but all routing is done at the ingress VTEP; the egress VTEP only performs bridging.-->
- {{<link url="#symmetric-routing" text="Distributed symmetric routing">}}: Every VTEP participates in routing and routing is done at both the ingress VTEP and the egress VTEP.

   Distributed routing is commonly deployed with the VTEPs configured with an *anycast IP and MAC address* for each subnet; each VTEP that has a particular subnet is configured with the same IP/MAC for that subnet. Such a model facilitates easy host and VM mobility as there is no need to change the host or VM configuration when it moves from one VTEP to another.

   All routing occurs in the context of a tenant VRF ({{<link url="Virtual-Routing-and-Forwarding-VRF" text="virtual routing and forwarding">}}). A VRF instance is provisioned for each tenant and the subnets of the tenant are associated with that VRF (the corresponding SVI is attached to the VRF). Inter-subnet routing for each tenant occurs within the context of the VRF for that tenant and is separate from the routing for other tenants.

## Centralized Routing

In centralized routing, you configure a specific VTEP to act as the default gateway for all the hosts in a particular subnet throughout the EVPN fabric. It is common to provision a pair of VTEPs in active-active mode as the default gateway using an anycast IP and MAC address for each subnet. You need to configure all subnets on such a gateway VTEP. When a host in one subnet wants to communicate with a host in another subnet, it addresses the packets to the gateway VTEP. The ingress VTEP (to which the source host is attached) bridges the packets to the gateway VTEP over the corresponding VXLAN tunnel. The gateway VTEP performs the routing to the destination host and, post-routing, the packet gets bridged to the egress VTEP (to which the destination host is attached). The egress VTEP then bridges the packet on to the destination host.

To enable centralized routing, you must configure the gateway VTEPs to advertise their IP and MAC address.

{{< tabs "TabID26 ">}}
{{< tab "NCLU Commands ">}}

```
cumulus@leaf01:~$ net add bgp autonomous-system 65101
cumulus@leaf01:~$ net add bgp l2vpn evpn advertise-default-gw
cumulus@leaf01:~$ net pending
cumulus@leaf01:~$ net commit
```

The NCLU commands create the following configuration snippet in the `/etc/frr/frr.conf` file.

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
{{< tab "NVUE Commands ">}}

```
cumulus@leaf01:~$ nv set evpn route-advertise default-gateway on
cumulus@leaf01:~$ nv config apply
```

The NVUE Commands create the following configuration snippet in the `/etc/nvue.d/startup.yaml` file:

```
cumulus@leaf01:~$ sudo cat /etc/nvue.d/startup.yaml
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
You can deploy centralized routing at the VNI level, where you can configure the `advertise-default-gw` command per VNI so that centralized routing is used for certain VNIs while distributed symmetric routing (described below) is used for other VNIs. This type of configuration is not recommended.

When centralized routing is in use, even if the source host and destination host are attached to the same VTEP, the packets travel to the gateway VTEP to get routed and then come back.
{{%/notice%}}

<!--## Asymmetric Routing

In distributed asymmetric routing, each VTEP acts as a layer 3 gateway, performing routing for its attached hosts. The routing is called asymmetric because only the ingress VTEP performs routing, the egress VTEP only performs bridging. Asymmetric routing can be achieved with only host routing and does not involve any interconnecting VNIs. However, you must provision each VTEP with all VLANs/VNIs - the subnets between which communication can take place; this is required even if there are no locally-attached hosts for a particular VLAN.

{{%notice note%}}
The only additional configuration required to implement asymmetric routing beyond the standard configuration for a layer 2 VTEP described earlier is to ensure that each VTEP has all VLANs (and corresponding VNIs) provisioned on it and the SVI for each such VLAN is configured with an anycast IP/MAC address.
{{%/notice%}}-->

## Symmetric Routing

In distributed symmetric routing, each VTEP acts as a layer 3 gateway, performing routing for its attached hosts; however, both the ingress VTEP and egress VTEP route the packets (similar to the traditional routing behavior of routing to a next hop router). In the VXLAN encapsulated packet, the inner destination MAC address is set to the router MAC address of the egress VTEP as an indication that the egress VTEP is the next hop and also needs to perform routing. All routing happens in the context of a tenant (VRF). For a packet received by the ingress VTEP from a locally attached host, the SVI interface corresponding to the VLAN determines the VRF. For a packet received by the egress VTEP over the VXLAN tunnel, the VNI in the packet has to specify the VRF. For symmetric routing, this is a VNI corresponding to the tenant and is different from either the source VNI or the destination VNI. This VNI is referred to as the layer 3 VNI or interconnecting VNI. The regular VNI, which is used to map a VLAN, is referred to as the layer 2 VNI.

{{%notice note%}}
- There is a one-to-one mapping between a layer 3 VNI and a tenant (VRF).
- The VRF to layer 3 VNI mapping has to be consistent across all VTEPs. The layer 3 VNI has to be provisioned by the operator.
- A layer 3 VNI and a layer 2 VNI cannot have the same ID. If the VNI IDs are the same, the layer 2 VNI does not get created.
- In an MLAG configuration, the SVI used for the layer 3 VNI cannot be part of the bridge. This ensures that traffic tagged with that VLAN ID is not forwarded on the peer link or other trunks.
{{%/notice%}}

In an EVPN symmetric routing configuration, when a type-2 (MAC/IP) route is announced, in addition to containing two VNIs (the layer 2 VNI and the layer 3 VNI), the route also contains separate RTs for layer 2 and layer 3. The layer 3 RT associates the route with the tenant VRF. By default, this is auto-derived in a similar way to the layer 2 RT, using the layer 3 VNI instead of the layer 2 VNI; however you can also explicitly configure it.

For EVPN symmetric routing, additional configuration is required:

- {{<link url="#configure-a-per-tenant-vxlan-interface" text="Configure a per-tenant VXLAN interface">}} that specifies the layer 3 VNI for the tenant. This VXLAN interface is part of the bridge and the router MAC address of the remote VTEP is installed over this interface.
- {{<link url="#configure-an-svi-for-the-layer-3-vni" text="Configure an SVI">}} (layer 3 interface) corresponding to the per-tenant VXLAN interface. This is attached to the VRF of the tenant. Remote host routes for symmetric routing are installed over this SVI.
- {{<link url="#configure-the-vrf-to-layer-3-vni-mapping" text="Specify the VRF to layer 3 VNI mapping">}}. This configuration is for the BGP control plane.

Optional configuration includes {{<link url="#configure-rd-and-rts-for-the-tenant-vrf" text="configuring RD and RTs for the tenant VRF">}} and {{<link url="#advertise-locally-attached-subnets" text="advertising the locally-attached subnets">}}.

### Configure a Per-tenant VXLAN Interface

{{< tabs "TabID113 ">}}
{{< tab "NCLU Commands ">}}

```
cumulus@leaf01:~$ net add vxlan vni10 vxlan id 10
cumulus@leaf01:~$ net add vxlan vni10 bridge access 10
cumulus@leaf01:~$ net add vxlan vni10 vxlan local-tunnelip 10.10.10.1
cumulus@leaf01:~$ net add bridge bridge ports vni10
cumulus@leaf01:~$ net pending
cumulus@leaf01:~$ net commit
```

{{< /tab >}}
{{< tab "NVUE Commands ">}}

```
cumulus@leaf01:~$ nv set bridge domain br_default vlan 10 vni 10 
cumulus@leaf01:~$ nv set nve vxlan source address 10.10.10.10
cumulus@leaf01:~$ nv config apply
```

{{< /tab >}}
{{< tab "Linux Commands ">}}

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

{{< /tab >}}
{{< /tabs >}}

### Configure an SVI for the Layer 3 VNI

{{< tabs "TabID154 ">}}
{{< tab "NCLU Commands ">}}

```
cumulus@leaf01:~$ net add vlan10 vrf RED
cumulus@leaf01:~$ net pending
cumulus@leaf01:~$ net commit
```

{{< /tab >}}
{{< tab "NVUE Commands ">}}

```
cumulus@leaf01:~$ nv set vrf RED
cumulus@leaf01:~$ nv set interface vlan10 ip vrf RED
cumulus@leaf01:~$ nv config apply
```

{{< /tab >}}
{{< tab "Linux Commands ">}}

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

{{< /tab >}}
{{< /tabs >}}

{{%notice note%}}
When two VTEPs are operating in **VXLAN active-active** mode and performing **symmetric** routing, you need to configure the router MAC corresponding to each layer 3 VNI to ensure both VTEPs use the same MAC address. Specify the `address-virtual` (MAC address) for the SVI corresponding to the layer 3 VNI. Use the same address on both switches in the MLAG pair. Use the MLAG system MAC address. See {{<link url="#advertise-primary-ip-address-vxlan-active-active-mode" text="Advertise Primary IP Address">}}.
{{%/notice%}}

### Configure the VRF to Layer 3 VNI Mapping

{{< tabs "TabID206 ">}}
{{< tab "NCLU Commands ">}}

```
cumulus@leaf01:~$ net add vrf RED vni 4001
cumulus@leaf01:~$ net pending
cumulus@leaf01:~$ net commit
```

{{< /tab >}}
{{< tab "NVUE Commands ">}}

```
cumulus@leaf01:~$ nv set vrf RED evpn vni 4001
cumulus@leaf01:~$ nv config apply
```

{{%notice note%}}
When you run the `nv set vrf RED evpn vni 4001` command, NVUE:
- Creates a layer 3 VNI called vni4001
- Assigns the vni4001 a VLAN automatically from the reserved VLAN range and adds `_l3` (layer 3) at the end (for example vlan220_l3)
- Creates a layer 3 bridge called br_l3vni
- Adds vni4001 to the br_l3vni bridge
- Assigns vlan4024 to vrf RED

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

### Configure RD and RTs for the Tenant VRF

If you do not want the RD and RTs (layer 3 RTs) for the tenant VRF to be derived automatically, you can configure them manually by specifying them under the `l2vpn evpn` address family for that specific VRF.

{{< tabs "TabID226 ">}}
{{< tab "NCLU Commands ">}}

```
cumulus@leaf01:~$ net add bgp vrf RED l2vpn evpn rd 10.1.20.2:5
cumulus@leaf01:~$ net add bgp vrf RED l2vpn evpn route-target import 65102:4001
cumulus@leaf01:~$ net pending
cumulus@leaf01:~$ net commit
```

The NCLU commands create the following configuration snippet in the `/etc/frr/frr.conf` file:

```
...
router bgp 65101 vrf RED
  address-family l2vpn evpn
  rd 10.1.20.2:5
  route-target import 65102:4001
...
```

{{< /tab >}}
{{< tab "NVUE Commands ">}}

```
cumulus@leaf01:~$ nv set vrf RED router bgp rd 10.1.20.2:5
cumulus@leaf01:~$ nv set vrf RED router bgp route-import from-evpn route-target 65102:4001
```

The NVUE Commands create the following configuration snippet in the `/etc/nvue.d/startup.yaml` file:

```
cumulus@leaf01:~$ sudo cat /etc/nvue.d/startup.yaml

```

{{< /tab >}}
{{< tab "vtysh Commands ">}}

```
cumulus@leaf01:~$ sudo vtysh

leaf01# configure terminal
leaf01(config)# router bgp 65101 vrf RED
leaf01(config-router)# address-family l2vpn evpn
leaf01(config-router-af)# 10.1.20.2:5
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

### Advertise Locally-attached Subnets

Symmetric routing presents a problem in the presence of silent hosts. If the ingress VTEP does not have the destination subnet and the host route is not advertised for the destination host, the ingress VTEP cannot route the packet to its destination. You can overcome this problem by having VTEPs announce the subnet prefixes corresponding to their connected subnets in addition to announcing host routes. These routes are announced as EVPN prefix (type-5) routes.

To advertise locally attached subnets:

1. Enable advertisement of EVPN prefix (type-5) routes. Refer to {{<link url="#announce-evpn-type-5-routes" text="Prefix-based Routing - EVPN Type-5 Routes">}}, below.
2. Ensure that the routes corresponding to the connected subnets are known in the BGP VRF routing table by injecting them using the `network` command or redistributing them using the `redistribute connected` command.

{{%notice note%}}
This configuration is recommended only if the deployment is known to have silent hosts. It is also recommended that you enable on only one VTEP per subnet, or two for redundancy.
{{%/notice%}}

## Prefix-based Routing

EVPN in Cumulus Linux supports prefix-based routing using EVPN type-5 (prefix) routes. Type-5 routes (or prefix routes) are primarily used to route to destinations outside of the data center fabric.

EVPN prefix routes carry the layer 3 VNI and router MAC address and follow the symmetric routing model for routing to the destination prefix.

{{%notice note%}}
When connecting to a WAN edge router to reach destinations outside the data center, deploy specific border/exit leaf switches to originate the type-5 routes.
{{%/notice%}}

### Install EVPN Type-5 Routes

For a switch to be able to install EVPN type-5 routes into the routing table, you must configure it with the layer 3 VNI related information. This configuration is the same as for symmetric routing. You need to:

1. Configure a per-tenant VXLAN interface that specifies the layer 3 VNI for the tenant. This VXLAN interface is part of the bridge; router MAC addresses of remote VTEPs are installed over this interface.
2. Configure an SVI (layer 3 interface) corresponding to the per-tenant VXLAN interface. This is attached to the VRF of the tenant. The remote prefix routes are installed over this SVI.
3. Specify the mapping of the VRF to layer 3 VNI. This configuration is for the BGP control plane.

### Announce EVPN Type-5 Routes

The following configuration is required in the tenant VRF to announce IP prefixes in the BGP RIB as EVPN type-5 routes.

{{< tabs "TabID317 ">}}
{{< tab "NCLU Commands ">}}

```
cumulus@leaf01:~$ net add bgp vrf RED l2vpn evpn advertise ipv4 unicast
cumulus@leaf01:~$ net pending
cumulus@leaf01:~$ net commit
```

The NCLU commands create the following snippet in the `/etc/frr/frr.conf` file:

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
{{< tab "NVUE Commands ">}}

```
cumulus@leaf01:~$ nv set vrf RED router bgp address-family ipv4-unicast route-export to-evpn enable on
cumulus@leaf01:~$ nv config apply
```

The NVUE Commands create the following configuration snippet in the `/etc/nvue.d/startup.yaml` file:

```
cumulus@leaf01:~$ sudo cat /etc/nvue.d/startup.yaml

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

<!--### EVPN Type-5 Routing in Asymmetric Mode

Asymmetric routing is an ideal choice when all VLANs (subnets) are configured on all leaf switches. It simplifies the routing configuration and eliminates the potential need for advertising subnet routes to handle silent hosts. However, most deployments need access to external networks to reach the Internet or global destinations, or to do subnet-based routing between pods or data centers; this requires EVPN type-5 routes.

Cumulus Linux supports EVPN type-5 routes for prefix-based routing in asymmetric configurations within the pod or data center by providing an option to use the layer 3 VNI only for type-5 routes; type-2 routes (host routes) only use the layer 2 VNI.

The following example commands show how to use the layer 3 VNI for type-5 routes only:

{{< tabs "TabID368 ">}}

{{< tab "NCLU Commands ">}}

```
cumulus@leaf01:~$ net add vrf RED vni 4001 prefix-routes-only
cumulus@leaf01:~$ net pending
cumulus@leaf01:~$ net commit
```

{{%notice note%}}

There is no command to delete the `prefix-routes-only` option. The `net del vrf <vrf> vni <vni> prefix-routes-only` command deletes the VNI.

{{%/notice%}}

{{< /tab >}}

{{< tab "Linux Commands ">}}

Edit the `/etc/frr/frr.conf` file. For example:

```
cumulus@leaf01:~$ sudo nano /etc/frr/frr.conf
...
vrf RED
  vni 4001 prefix-routes-only
...
```

{{< /tab >}}

{{< /tabs >}}-->

### Control RIB Routes

By default, when announcing IP prefixes in the BGP RIB as EVPN type-5 routes, all routes in the BGP RIB are picked for advertisement as EVPN type-5 routes. You can use a route map to allow selective route advertisement from the BGP RIB.

The following commands add a route map filter to IPv4 EVPN type-5 route advertisement:

{{< tabs "TabID408 ">}}
{{< tab "NCLU Commands ">}}

```
cumulus@leaf01:~$ net add bgp vrf RED l2vpn evpn advertise ipv4 unicast route-map map1
cumulus@leaf01:~$ net pending
cumulus@leaf01:~$ net commit
```

{{< /tab >}}
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

### Originate Default EVPN Type-5 Routes

Cumulus Linux supports originating EVPN default type-5 routes. The default type-5 route is originated from a border (exit) leaf and advertised to all the other leafs within the pod. Any leaf within the pod follows the default route towards the border leaf for all external traffic (towards the Internet or a different pod).

To originate a default type-5 route in EVPN, you need to execute FRRouting commands. The following shows an example:

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

### Advertise Primary IP address (VXLAN Active-Active Mode)

EVPN symmetric routing configurations with VXLAN active-active (MLAG), all EVPN routes are advertised with the anycast IP address ({{<link url="VXLAN-Active-active-Mode#terminology" text="clagd-vxlan-anycast-ip">}}) as the next hop IP address and the anycast MAC address as the router MAC address. In a failure scenario, this can lead to traffic being forwarded to a leaf switch that does not have the destination routes. Traffic has to traverse the peer link (with additional BGP sessions per VRF).

To prevent sub-optimal routing, the next hop IP address of the VTEP is conditionally handled depending on the route type: host type-2 (MAC/IP advertisement) or type-5 (IP prefix route).

- For host type-2 routes, the anycast IP address is used as the next hop IP address and the anycast MAC address is used as the router MAC address.
- For type-5 routes, the system IP address (the primary IP address of the VTEP) is used as the next hop IP address and the system MAC address of the VTEP is used as the router MAC address.

See {{<link url="Basic-Configuration#evpn-and-vxlan-active-active-mode" text="EVPN and VXLAN Active-Active mode">}} for information about EVPN and VXLAN active-active mode.

#### Configure Advertise Primary IP Address

Set the MLAG system MAC address on both switches in the MLAG pair.

{{< tabs "TabID472 ">}}
{{< tab "NCLU Commands ">}}

```
cumulus@leaf01:~$ net add vlan 4001 ip address-virtual 44:38:39:BE:EF:AA
cumulus@leaf01:~$ net pending
cumulus@leaf01:~$ net commit
```

{{< /tab >}}
{{< tab "NVUE Commands ">}}

```
cumulus@leaf01:~$ nv set system global anycast-mac 44:38:39:BE:EF:AA
cumulus@leaf01:~$ nv config apply
```

{{< /tab >}}
{{< tab "Linux Commands ">}}

Edit the `/etc/network/interfaces` file and add `address-virtual <anycast-mac>` under the SVI. For example:

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

{{%notice note%}}
- In Cumulus Linux 3.7 and earlier, the `hwaddress` command is used instead of the `address-virtual` command. If you upgrade from Cumulus Linux 3.7 to 4.0 or later and have a previous symmetric routing with VXLAN active-active configuration, you must change `hwaddress` to `address-virtual`. Either run the NCLU `address-virtual <anycast-mac>` command or edit the `/etc/network/interfaces` file.
- When configuring third party networking devices using MLAG and EVPN for interoperability, you must configure and announce a single shared router MAC value per advertised next hop IP address.
{{%/notice%}}

{{< /tab >}}
{{< /tabs >}}

#### Optional Configuration

To advertise type-5 routes and host type-2 routes using the system IP address and system MAC address:

{{< tabs "TabID520 ">}}
{{< tab "NVUE Commands ">}}

```
cumulus@leaf01:~$ nv set evpn route-advertise nexthop-setting system-ip-mac
cumulus@leaf01:~$ nv config apply
```

{{< /tab >}}
{{< tab "vtysh Commands ">}}

```
cumulus@leaf01:~$ sudo vtysh

leaf01# configure terminal
leaf01(config)# router bgp 65101 vrf RED
leaf01(config)# address-family l2vpn evpn
leaf01(config)# advertise-pip ip 10.10.10.1 mac 44:38:39:be:ef:aa
leaf01(config-router-af)# end
leaf01# write memory
leaf01# exit
cumulus@leaf01:~$
```

{{< /tab >}}
{{< /tabs >}}

#### Disable Advertise Primary IP Address

Each switch in the MLAG pair advertises type-5 routes with its own system IP, which creates an additional next hop at the remote VTEPs. In a large multi-tenancy EVPN deployment, where additional resources are a concern, you might prefer to disable this feature.

To disable Advertise Primary IP Address:

{{< tabs "TabID560 ">}}
{{< tab "NCLU Commands ">}}

```
cumulus@leaf01:~$ net del bgp vrf RED l2vpn evpn advertise-pip
cumulus@leaf01:~$ net pending
cumulus@leaf01:~$ net commit
```

{{< /tab >}}
{{< tab "NVUE Commands ">}}

```
cumulus@leaf01:~$ nv set evpn route-advertise nexthop-setting shared-ip-mac
cumulus@leaf01:~$ nv config apply
```

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

{{< /tab >}}
{{< /tabs >}}

#### Show Advertise Primary IP Address Information

To show Advertise Primary IP Address parameters, run the NCLU `net show bgp l2vpn evpn vni <vni>` command or the vtysh `show bgp l2vpn evpn vni <vni>` command. For example:

```
cumulus@leaf01:~$ net show bgp l2vpn evpn vni 4001
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
leaf01#
```

To show EVPN routes with Primary IP Advertisement, run the NCLU `net show bgp l2vpn evpn route` command or the vtysh `show bgp l2vpn evpn route` command. For example:

```
cumulus@leaf01:~$ net show bgp l2vpn evpn route
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

To show the learned route from an external router injected as a type-5 route, run the NCLU `net show bgp vrf <vrf> ipv4 unicast` command or the vtysh `show bgp vrf <vrf> ipv4 unicast` command.

## Downstream VNI

Downstream VNI (symmetric EVPN route leaking) enables you to assign a VNI from a downstream remote VTEP through EVPN routes instead of configuring layer 3 VNIs globally across the network.

To configure a downstream VNI, you configure tenant VRFs as usual; however, to configure the desired route leaking, you define a route target import and, or export statement.

### Configure Route Targets

The route target import or export statement is in the format `route-target import|export <asn>:<vni>`; for example, `route-target import 65101:6000`. As an alternative, you can use `route-target import|export *:<vni>`. The asterisk (*) uses any ASN as a wildcard.

To configure the downsteam VNI, you must manually edit the `/etc/frr/frr.conf` file; NCLU and NVUE commands are not supported.

{{%notice note%}}
- Downstream VNI is supported in EVPN symmetric mode with layer 3 VNIs and single VXLAN devices only.
- You can configure multiple import and export route targets in a VRF.
- You can configure selective route targets for individual prefixes with routing policies.
- You cannot leak (import) overlapping tenant prefixes into the same destination VRF.
{{%/notice%}}

The following example shows a configuration with downstream VNI on leaf01 thru leaf04, and border01.

|   Traffic Flow between VRF RED and VRF 10  |     |
| ----------------------------------------------| ----|
| <img width=1300/> {{< img src="/images/cumulus-linux/evpn-downstream-vni.png"  >}}| <br><ol><li>server01 forwards traffic to leaf01.</li><li>leaf01 encapsulates the packet with the VNI in its route-target import statement (6000) and tunnels the traffic over to border01.</li><li> border01 uses the VNI received from leaf01 to forward the packet.</li><li> The reverse traffic from border01 to server01 is encapsulated with the VNI in the route-target import statement on border01 (4001) and tunneled over to leaf01, where routing occurs in VRF RED.</li></ul> |

The configuration for the example is shown below.
- On leaf01, you can see the route target (`route-target import *:6000`) under the `router bgp 65101 vrf RED` and `router bgp 65101 vrf BLUE` stanza of the `/etc/frr/frr.conf` file.
- On border01, you can see the route targets (`route-target import *:4001` and `route-target import *:4002`) under the `router bgp 65163 vrf VRF10` stanza of the `/etc/frr/frr.conf` file.

Because the configuration is similar on all the leafs, only leaf01 and border01 configuration files are shown below. The spine configuration files are not shown for brevity.

{{< tabs "TabID749 ">}}
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
auto VRF10
iface VRF10
    vrf-table auto
auto EXTERNAL1
iface EXTERNAL1
    vrf-table auto
auto EXTERNAL2
iface EXTERNAL2
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
    es-sys-mac 44:38:39:BE:EF:FF
    bond-slaves swp1
    bond-mode 802.3ad
    bond-lacp-bypass-allow yes
    bridge-access 2001
auto bond2
iface bond2
    mtu 9000
    es-sys-mac 44:38:39:BE:EF:FF
    bond-slaves swp2
    bond-mode 802.3ad
    bond-lacp-bypass-allow yes
    bridge-access 2002
auto bond3
iface bond3
    mtu 9000
    es-sys-mac 44:38:39:BE:EF:FF
    bond-slaves swp3
    bond-mode 802.3ad
    bond-lacp-bypass-allow yes
    bridge-access 2010
auto vlan2001
iface vlan2001
    address 10.1.201.1/24
    hwaddress 44:38:39:22:01:b3
    vrf EXTERNAL1
    vlan-raw-device br_default
    vlan-id 2001
auto vlan2002
iface vlan2002
    address 10.1.202.1/24
    hwaddress 44:38:39:22:01:b3
    vrf EXTERNAL2
    vlan-raw-device br_default
    vlan-id 2002
auto vlan2010
iface vlan2010
    address 10.1.210.1/24
    hwaddress 44:38:39:22:01:b3
    vrf VRF10
    vlan-raw-device br_default
    vlan-id 2010
auto vxlan48
iface vxlan48
    bridge-vlan-vni-map 2001=2001 2002=2002 2010=2010
    bridge-vids 2001 2002 2010
    bridge-learning off
auto vlan336_l3
iface vlan336_l3
    vrf VRF10
    vlan-raw-device br_l3vni
    vlan-id 336
auto vxlan99
iface vxlan99
    bridge-vlan-vni-map 336=6000
    bridge-vids 336
    bridge-learning off
auto br_default
iface br_default
    bridge-ports bond1 bond2 bond3 vxlan48
    hwaddress 44:38:39:22:01:b3
    bridge-vlan-aware yes
    bridge-vids 2001 2002 2010
    bridge-pvid 1
auto br_l3vni
iface br_l3vni
    bridge-ports vxlan99
    hwaddress 44:38:39:22:01:b3
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
vrf BLUE
 vni 4002
 exit-vrf
!
vrf RED
 vni 4001
 exit-vrf
!
interface bond1
 evpn mh es-df-pref 50000
 evpn mh es-id 1
 evpn mh es-sys-mac 44:38:39:be:ef:aa
!
interface bond2
 evpn mh es-df-pref 50000
 evpn mh es-id 2
 evpn mh es-sys-mac 44:38:39:be:ef:aa
!
interface bond3
 evpn mh es-df-pref 50000
 evpn mh es-id 3
 evpn mh es-sys-mac 44:38:39:be:ef:aa
!
interface swp51
 evpn mh uplink
!
interface swp52
 evpn mh uplink
!
router bgp 65101
 bgp router-id 10.10.10.1
 bgp bestpath as-path multipath-relax
 neighbor underlay peer-group
 neighbor underlay remote-as external
 neighbor underlay advertisement-interval 0
 neighbor underlay timers 3 9
 neighbor underlay timers connect 10
 neighbor swp51 interface peer-group underlay
 neighbor swp51 advertisement-interval 0
 neighbor swp51 timers 3 9
 neighbor swp51 timers connect 10
 neighbor swp52 interface peer-group underlay
 neighbor swp52 advertisement-interval 0
 neighbor swp52 timers 3 9
 neighbor swp52 timers connect 10
 !
 address-family ipv4 unicast
  redistribute connected
  maximum-paths 64
 exit-address-family
 !
 address-family l2vpn evpn
  neighbor underlay activate
  advertise-all-vni
 exit-address-family
!
router bgp 65101 vrf RED
 bgp router-id 10.10.10.1
 !
 address-family ipv4 unicast
  redistribute connected
 exit-address-family
 !
 address-family l2vpn evpn
  advertise ipv4 unicast
  route-target import *:6000
 exit-address-family
!
router bgp 65101 vrf BLUE
 bgp router-id 10.10.10.1
 !
 address-family ipv4 unicast
  redistribute connected
 exit-address-family
 !
 address-family l2vpn evpn
  advertise ipv4 unicast
  route-target import *:6000
 exit-address-family
```

{{< /tab >}}
{{< tab "border01 ">}}

```
cumulus@border01:~$ sudo cat /etc/frr/frr.conf
...
vrf VRF10
 vni 6000
 exit-vrf
!
interface bond1
 evpn mh es-df-pref 50000
 evpn mh es-id 1
 evpn mh es-sys-mac 44:38:39:be:ef:ff
!
interface bond2
 evpn mh es-df-pref 50000
 evpn mh es-id 2
 evpn mh es-sys-mac 44:38:39:be:ef:ff
!
interface bond3
 evpn mh es-df-pref 50000
 evpn mh es-id 3
 evpn mh es-sys-mac 44:38:39:be:ef:ff
!
interface swp51
 evpn mh uplink
!
interface swp52
 evpn mh uplink
!
router bgp 65163
 bgp router-id 10.10.10.63
 bgp bestpath as-path multipath-relax
 neighbor underlay peer-group
 neighbor underlay remote-as external
 neighbor underlay advertisement-interval 0
 neighbor underlay timers 3 9
 neighbor underlay timers connect 10
 neighbor swp51 interface peer-group underlay
 neighbor swp51 advertisement-interval 0
 neighbor swp51 timers 3 9
 neighbor swp51 timers connect 10
 neighbor swp52 interface peer-group underlay
 neighbor swp52 advertisement-interval 0
 neighbor swp52 timers 3 9
 neighbor swp52 timers connect 10
 !
 address-family ipv4 unicast
  redistribute connected
  maximum-paths 64
  maximum-paths ibgp 64
 exit-address-family
 !
 address-family l2vpn evpn
  neighbor underlay activate
  advertise-all-vni
 exit-address-family
!
router bgp 65163 vrf VRF10
 bgp router-id 10.10.10.63
 !
 address-family ipv4 unicast
  redistribute connected
 exit-address-family
 !
 address-family l2vpn evpn
  advertise ipv4 unicast
  route-target import *:4001
  route-target import *:4002
 exit-address-family
!
router bgp 65163 vrf EXTERNAL1
 bgp router-id 10.10.10.63
 !
 address-family ipv4 unicast
  redistribute connected
 exit-address-family
 !
 address-family l2vpn evpn
  advertise ipv4 unicast
 exit-address-family
!
router bgp 65163 vrf EXTERNAL2
 bgp router-id 10.10.10.63
 !
 address-family ipv4 unicast
  redistribute connected
 exit-address-family
 !
 address-family l2vpn evpn
  advertise ipv4 unicast
 exit-address-family
 ...
```

{{< /tab >}}
{{< /tabs >}}

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

In an EVPN centralized routing configuration, where the layer 2 network extends beyond VTEPs, (for example, a host with bridges), the gateway MAC address is not refreshed in the network when ARP suppression is enabled on the gateway. To work around this issue, disable ARP suppression on the centralized gateway.

### Type-5 Routes and ECMP

For VXLAN type-5 routes, ECMP does not work when the VTEP is directly connected to remote VTEPs.
To work around this issue, add an additional device in the VXLAN fabric between the local and remote VTEPs, so that local and remote VTEPs are not directly connected.

### Symmetric Routing and the Same SVI IP Address Across Racks

In EVPN symmetric routing, if you use the same SVI IP address across racks (for example, if the SVI IP address for a specific VLAN interface (such as vlan100) is the same on all VTEPs where this SVI is present):

- You cannot use ping between SVI IP adresses to verify connectivity between VTEPs because either the local rack itself uses the ping destination IP address or many remote racks use the ping destination IP address.
- If you use ping from a host to the SVI IP address, the local VTEP (gateway) might not reply if the host has an ARP entry from a remote gateway.

There are no issues with host-to-host traffic.
