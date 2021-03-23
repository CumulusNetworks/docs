---
title: Basic Configuration
author: NVIDIA
weight: 550
toc: 4
---
The following sections provide the basic configuration needed to use EVPN as the control plane for VXLAN. For additional EVPN configuration, see {{<link url="EVPN-Enhancements" text="EVPN Enhancements">}}

The steps provided assume you have already {{<link url="Border-Gateway-Protocol-BGP" text="Configured BGP">}} and {{<link url="VLAN-aware-Bridge-Mode/#vxlans-with-vlan-aware-bridges" text="created VXLAN interfaces">}}, attached them to a bridge, mapped VLANs to VNIs, and configured the VXLAN local tunnel IP address.

{{< expand "Example BGP Configuration" >}}

{{< tabs "TabID14 ">}}
{{< tab "CUE Commands ">}}

```
cumulus@leaf01:~$ cl set router bgp autonomous-system 65101
cumulus@leaf01:~$ cl set router bgp router-id 10.10.10.1
cumulus@leaf01:~$ cl set vrf default router bgp peer swp51 remote-as external
cumulus@leaf01:~$ cl set vrf default router bgp address-family ipv4-unicast static-network 10.10.10.1/32
cumulus@leaf01:~$ cl config apply
```

{{< /tab >}}
{{< tab "vtysh Commands ">}}

```
cumulus@leaf01:~$ sudo vtysh
leaf01# configure terminal
leaf01(config)# router bgp 65101
leaf01(config-router)# bgp router-id 10.10.10.1
leaf01(config-router)# neighbor 10.0.1.0 remote-as external
leaf01(config-router)# address-family ipv4
leaf01(config-router-af)# network 10.10.10.1/32
leaf01(config-router-af)# end
leaf01# write memory
leaf01# exit
cumulus@leaf01:~$
```

{{< /tab >}}
{{< /tabs >}}

{{< /expand >}}

{{< expand "Example VXLAN Interface Configuration" >}}

{{< tabs "TabID41 ">}}
{{< tab "CUE Commands ">}}

```
cumulus@leaf01:~$ cl set bridge domain br_default vlan 10 vni 10
cumulus@leaf01:~$ cl set nve vxlan source address 10.10.10.10
cumulus@leaf01:~$ cl config apply
```

{{< /tab >}}
{{< tab "Linux Commands ">}}

```
cumulus@leaf01:~$ sudo nano /etc/network/interfaces
...
auto lo
iface lo inet loopback
        address 10.10.10.1/32
        vxlan-local-tunnelip 10.10.10.10

auto vni10
iface vni10
        bridge-access 10
        bridge-learning off
        vxlan-id 10

auto br_default
iface br_default
        bridge-ports vni10
        bridge-vlan-aware yes
        bridge-vids 10
        bridge-pvid 1
```

{{< /tab >}}
{{< /tabs >}}

{{< /expand >}}

## Configure EVPN
  
The following example commands show basic EVPN configuration.

To enable EVPN between {{<link url="Border-Gateway-Protocol-BGP" text="BGP">}} neighbors, add the address family *evpn* to the existing neighbor `address-family` activation command.

For a non-VTEP device that is only participating in EVPN route exchange, such as a spine switch where the network deployment uses hop-by-hop eBGP or the switch is acting as an iBGP route reflector, activating the interface for the EVPN address family is the fundamental configuration needed.

{{< tabs "TabID25 ">}}
{{< tab "CUE Commands ">}}

```
cumulus@leaf01:~$ cl set evpn enable on
cumulus@leaf01:~$ cl set vrf default router bgp address-family l2vpn-evpn enable on
cumulus@leaf01:~$ cl set vrf default router bgp peer swp51 address-family l2vpn-evpn enable on
cumulus@leaf01:~$ cl config apply
```

{{< /tab >}}
{{< tab "NCLU Commands ">}}

```
cumulus@leaf01:~$ net add bgp neighbor swp51 interface remote-as external
cumulus@leaf01:~$ net add bgp l2vpn evpn neighbor swp51 activate
cumulus@leaf01:~$ net add bgp l2vpn evpn advertise-all-vni
cumulus@leaf01:~$ net pending
cumulus@leaf01:~$ net commit
```

{{%notice note%}}
The `advertise-all-vni` option is only needed on leaf switches that are VTEPs. EVPN routes received from a BGP peer are accepted, even without this explicit EVPN configuration. These routes are maintained in the global EVPN routing table. However, they only become effective (imported into the per-VNI routing table and appropriate entries installed in the kernel) when the VNI corresponding to the received route is locally known.
{{%/notice%}}

{{< /tab >}}
{{< tab "vtysh Commands ">}}

```
cumulus@leaf01:~$ sudo vtysh

leaf01# configure terminal
leaf01(config)# router bgp 65101
leaf01(config-router)# bgp router-id 10.10.10.1
leaf01(config-router)# neighbor swp51 interface remote-as external
leaf01(config-router)# address-family l2vpn evpn
leaf01(config-router-af)# neighbor swp51 activate
leaf01(config-router-af)# advertise-all-vni
leaf01(config-router-af)# end
leaf01)# write memory
leaf01)# exit
cumulus@leaf01:~$
```

{{%notice note%}}
The `advertise-all-vni` option is only needed on leaf switches that are VTEPs. EVPN routes received from a BGP peer are accepted, even without this explicit EVPN configuration. These routes are maintained in the global EVPN routing table. However, they only become effective (imported into the per-VNI routing table and appropriate entries installed in the kernel) when the VNI corresponding to the received route is locally known.
{{%/notice%}}

{{< /tab >}}
{{< /tabs >}}

The above commands create the following configuration snippet in the `/etc/frr/frr.conf` file.

```
...
router bgp 65101
  bgp router-id 10.10.10.1
  neighbor swp51 interface remote-as external
  address-family l2vpn evpn
neighbor swp51 activate
  advertise-all-vni
...
```

## EVPN and VXLAN Active-active Mode

For EVPN in VXLAN active-active mode, both switches in the MLAG pair establish EVPN peering with other EVPN speakers (for example, with spine switches if using hop-by-hop eBGP) and inform about their locally known VNIs and MACs. When MLAG is active, both switches announce this information with the shared anycast IP address.

For active-active configuration, make sure that:

- The `clagd-vxlan-anycast-ip` and `vxlan-local-tunnelip` parameters are under the loopback stanza on both peers.
- The anycast address is advertised to the routed fabric from both peers.
- The VNIs are configured identically on both peers.
- The peerlink must belong to the bridge.

MLAG synchronizes information between the two switches in the MLAG pair; EVPN does not synchronize.

For type-5 routes in an EVPN *symmetric* configuration with VXLAN active-active mode, Cumulus Linux uses Primary IP Address Advertisement. For information on configuring Primary IP Address Advertisement, see {{<link url="Inter-subnet-Routing#advertise-primary-ip-address-vxlan-active-active-mode" text="Advertise Primary IP Address">}}.

For information about active-active VTEPs and anycast IP behavior, and for failure scenarios, see {{<link url="VXLAN-Active-active-Mode">}}.

## Considerations

- When EVPN is enabled on a VTEP, all locally defined VNIs on that switch and other information (such as MAC addresses) are advertised to EVPN peers. There is no provision to only announce certain VNIs.
- ND suppression only works with the Spectrum-A1 chip.
- ARP suppression is enabled by default in Cumulus Linux. However, in a {{<link url="VXLAN-Active-active-Mode" text="VXLAN active-active">}} configuration, ARPs are sometimes *not* suppressed. This is because the neighbor entries are not synchronized between the two switches operating in active-active mode by a control plane. This has no impact on forwarding.
- You must configure the overlay (tenants) in a specific VRF and separate from the underlay, which resides in the default VRF. Layer 3 VNI mapping for the default VRF is not supported.
- EVPN is not supported when {{<link title="Redistribute Neighbor" >}} is also configured. Enabling both features simultaneously causes instability in IPv4 and IPv6 neighbor entries.
- To conform to {{<exlink url="https://tools.ietf.org/html/rfc6514#section-5" text="RFC 6514">}}, Cumulus Linux implements a stricter check on a received type-3 route to ensure that it has the PMSI attribute with the replication type set to *ingress-replication*.
