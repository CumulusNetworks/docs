---
title: Sample Configurations
weight: 50
cascade:
    product: Technical Guides
    author: NVIDIA
---
## Access to Common Services and Internet Connectivity

Consider a scenario with two tenants in different VRFs - one needs access to the Internet and the other needs access to common services like DHCP.
There is a traditional method of route leaking into the VRF that can be leveraged. However, due to its scaling implications, the Downstream VNI (D-VNI) model can be used to access common services like DHCP, DNS, and so on.

Consider the network topology below:

{{< img src = "/images/guides/VXLAN-EVPN-design-guide/sample1.png" >}}

The topology shows three different tenants represented by VRFs RED, BLUE and PURPLE with corresponding hosts connected over an EVPN network. The network also hosts DNS (DN1 and DN2) and Storage (ST1 and ST2) servers in separate VRFs, and these services must be offered to the 3 tenants. The service leaf switches (SL1 and SL2) only have the shared services VRFs configured while the server leaf switches (L11, L12, L21, L22, L31 and L32) only have the tenant VRFs configured.

With D-VNI support, access to the shared services works as follows:
1. The VRFs (RED, BLUE and PURPLE) on the server leaf switches (L11 and so on) are configured to import the RTs with which the service leaf switches (SL1 and SL2) export routes from their shared services VRFs. For example, if they export with auto-derived RTs, the server leaf switches are configured to import RTs `*:20001` and `*:20002`; the ‘*’ refers to the ASN of SL1 and SL2 (65201 and 65202). You can specify the ASNs instead of specifying a wildcard.
2. The VRFs (DNS and STORAGE) on SL1 and SL2 are configured to import RTs announced by the server leaf switches for the tenant VRFs. For example, `*:10001`, `*:10002` and so on.
3. When routes to the DNS servers or the storage servers are received by the server leaf switches and installed into their VRF routing tables, they are set up to use the D-VNI; `20001` and `20002` respectively.
4. Similar behavior occurs on the service leaf switches for the routes they import.
5. When a server like H11 (`192.168.51.11`) tries to communicate with DNS server DN1 (`200.11.3.1`), the corresponding leaf switch (L11 or L12) encapsulates the packet with VNI 20001 and tunnel over to SL1 (`10.150.3.1`) or SL2 (`10.150.3.2`). Based on the received VNI (`20001`), SL1 and SL2 know to route the packet in the DNS VRF after VXLAN decapsulation. The reverse traffic from DN1 to H11 is encapsulated by SL1 or SL2 with VNI `10001` and tunneled over to L11 or L12, where routing occurs in the RED VRF.

Below is the snippet to show the import of multiple wildcard RTs.

```
nv set vrf RED router bgp autonomous-system 65001
nv set vrf RED router bgp address-family ipv4-unicast redistribute connected enable on
nv set vrf RED router bgp route-import from-evpn route-target *:20001 
nv set vrf RED router bgp route-import from-evpn route-target *:20002
```

## Communication between tenants in different VRFs

Consider a scenario with two tenants in different VRFs that need access to each other and access to common services like DHCP. Route leaking can be leveraged, where for example, VRF BLUE can be imported inside VRF RED. However, the better approach is through the HUB and SPOKE method using D-VNI as explained below.

Consider the network topology below:

{{< img src = "/images/guides/VXLAN-EVPN-design-guide/sample2.png" >}}

Communication between the tenant represented by VRF RED and the one represented by VRF BLUE is expected to happen through the service leaf switches, SL1 and SL2. This works with D-VNI as follows:
1. A VRF HUB01 is provisioned on the service leaf switches SL1 and SL2 and is configured to import routes originated in the tenant VRFs RED and BLUE by the server leaf switches. For example, VRF HUB01 is configured to import RTs `*:10001` and `*:10002`.
2. Additionally, the service leaf switches are configured to aggregate the VRF RED and VRF BLUE routes that they import into VRF HUB01 and then to originate the aggregate for VRF RED routes with the export RT `65201:10002` (or `65202:10002`); likewise, they also originate the aggregate for VRF BLUE routes with RT `65201:10001` (or `65201:10001`).
3. The server leaf switches L11, L12, L21 and L22 use their auto-derived RTs for route export and import. This means that they import the aggregate routes for inter-vrf routing through the service leaf switches.
4. When a server in VRF RED like H11 (`192.168.51.11`) tries to communicate with a server in VRF BLUE like H24 (`192.168.62.24`), the corresponding leaf switch (L11 or L12) route using the aggregate route for `192.168.62.0/24` from SL1 or SL2; the packet is encapsulated with VNI `20001` and tunneled over to SL1 or SL2. SL1 or SL2 decapsulate the packet and route in VRF HUB01, which now use the host route for `192.168.62.24/32` that originated from L21 and L22; the packet is encapsulated with VNI `10002` and tunneled back over VXLAN to L21 or L22, where the packet will be routed in the BLUE VRF. Note that a similar forwarding behavior occurs even if the communication is between servers H11 and H13, which are connected to the same server leaf switches because these hosts are in different VRFs.

## VRF Configuration on Border Leafs

Configuring all tenant VRFs is not required on border leafs, you can create a different VRF on the border leaf (such as shared) and import the RT of shared on the tenant VRFs.

## Internet Route Distribution into the Fabric

You can use route maps to distribute any route into the EVPN fabric or you can enable the default originate option on the border leaf.

The following commands set up and add a route map filter to IPv4 EVPN `type-5` route advertisement:

```
nv set router policy prefix-list ext-routes-to-vrf1 rule 10 match 81.1.1.0/24
nv set router policy prefix-list ext-routes-to-vrf1 rule 10 action permit

nv set router policy prefix-list ext-routes-to-vrf2 rule 10 match 81.1.2.0/24
nv set router policy prefix-list ext-routes-to-vrf2 rule 10 action permit

nv set router policy prefix-list ext-routes-to-all-vrfs rule 10 match 120.0.0.1/32 
nv set router policy prefix-list ext-routes-to-all-vrfs rule 10 action permit

nv set router policy route-map IPV4-TO-EXT rule 10 action permit
nv set router policy route-map IPV4-TO-EXT rule 10 match type ipv4
nv set router policy route-map IPV4-TO-EXT rule 10 match ip-prefix-list IPV4-TO-EXT

nv set router policy route-map ext-routes-to-vrf rule 10 match type ipv4
nv set router policy route-map ext-routes-to-vrf rule 10 match ip-prefix-list ext-routes-to-vrf1
nv set router policy route-map ext-routes-to-vrf rule 10 set extcommunity rt 65050:104001
nv set router policy route-map ext-routes-to-vrf rule 10 action permit

nv set router policy route-map ext-routes-to-vrf rule 20 match type ipv4
nv set router policy route-map ext-routes-to-vrf rule 20 match type ipv4
nv set router policy route-map ext-routes-to-vrf rule 20 match ip-prefix-list ext-routes-to-vrf2
nv set router policy route-map ext-routes-to-vrf rule 20 set extcommunity rt 65050:104002
nv set router policy route-map ext-routes-to-vrf rule 20 action permit

nv set router policy route-map ext-routes-to-vrf rule 30 match type ipv4
nv set router policy route-map ext-routes-to-vrf rule 30 match ip-prefix-list ext-routes-to-all-vrfs
nv set router policy route-map ext-routes-to-vrf rule 30 set extcommunity rt 65050:104001 
nv set router policy route-map ext-routes-to-vrf rule 30 set extcommunity rt 65050:104002 
nv set router policy route-map ext-routes-to-vrf rule 30 set extcommunity rt 65050:104003
nv set router policy route-map ext-routes-to-vrf rule 30 action permit

nv set vrf shared router bgp router-id 144.1.1.2
nv set vrf shared router bgp autonomous-system 65201
nv set vrf shared router bgp neighbor 144.1.1.1 remote-as external
nv set vrf shared router bgp address-family ipv4-unicast redistribute connected enable on
nv set vrf shared router bgp address-family ipv4-unicast route-export to-evpn route-map ext-routes-to-vrf
```

To originate a default `type-5` route in EVPN:

```
nv set vrf shared router bgp router-id 144.1.1.2
nv set vrf shared router bgp autonomous-system 65201
nv set vrf shared router bgp neighbor 144.1.1.1 remote-as external
nv set vrf shared router bgp address-family ipv4-unicast redistribute connected enable on
nv set vrf shared router bgp address-family ipv4-unicast route-export to-evpn default-route-origination on
nv set vrf shared router bgp address-family ipv6-unicast route-export to-evpn default-route-origination on
```
