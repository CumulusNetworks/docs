---
title: NX-OS to NVUE Common Commands
weight: 300
Draft: true
---

Cumulus Linux version 4.4 introduces a new CLI called {{<kb_link url="cumulus-linux-44/System-Configuration/NVIDIA-User-Experience-NVUE/" text="NVUE">}}.

NVUE introduces a complete object model for Cumulus Linux. This makes translating configurations from one vendor to another much more reliable both the first time, but also across Cumulus Linux versions.

This KB article describes how to translate common NX-OS configurations to NVUE commands. 


## Feature Enablement
{{<notice note >}}
Cumulus Linux does not require specific features to be enabled like NX-OS does.
{{</notice >}}

## Hostname and System Commands
| NX-OS Command | NVUE Command | Comments |
| -----         | -----        | -----    |
| `hostname <hostname>` | `nv set platform hostname <hostname>` || 
| `logging server <ip>` | `nv set service syslog default server <ip>` | The value `default` is the VRF the server is in. | 
| `ntp server <ip>` | `nv set service ntp default server <ip>` | The value `default` is the VRF the server is in.
| `interface breakout module 1 port <port> map 10g-4x` | `nv set interface <interface> link breakout 4x10G`| Multiple breakout options exist. Use `nv set interface <interface> link breakout -h` to see all commands. |
| ` copy running-config startup-config` | `nv config apply` | |
| `show startup-config` | `cat /etc/nvue.d/startup.yaml` | |
| `show running-config` | `nv config diff empty applied` | NVUE diff compares an `empty` config against the currently `applied` config. | 
<!-- | `banner motd <banner>` | | | -->

## Interface Commands
NX-OS interface commands are configured under an individual interface, for example:
```
interface e1/1
   ip address 10.1.1.1/24
```

| NX-OS Command | NVUE Command | Comments |
| -----         | -----        | -----    |
| `ip address <IP>` | `nv set interface <interface> address <IP>` | NVUE supports setting either IPv4 or IPv6 addresses with the same command. |
| `ip address <IP> secondary` | `nv set interface <interface> address <IP>` | Configuring a second IP address is additive. To replace an address use `nv unset interface <interface> address <IP>`. |
| `ipv6 address <IP>` | `nv set interface <interface> address <IP>` | NVUE supports setting either IPv4 or IPv6 addresses with the same command. |
| `mtu <mtu>` | `nv set interface <interface> link mtu <mtu>` | The default MTU in Cumulus Linux is 9216. |
| `speed <speed>` | `nv set interface <interface> link speed <speed>` | | 
| `fec <mode>` | `nv set interface link fec <mode>` | |
| `no shutdown` | `nv set interface <interface> link state up` | The default state for interfaces is `up`. Use `link state down` to shutdown an interface. |
| `interface loopback0` | `nv set interface lo` | The loopback interface on Cumulus Linux is called `lo`. |
<!-- | `description <text>` | `nv set interface <interface> alias <text>` | | -->


## Layer 2 and VLANs
Cumulus Linux interfaces are layer 3 routed interfaces by default. To make an interface a layer 2 switchport the interface must be added to the default bridge named `br_default`.  
`nv set interface <interface> bridge domain br_default`

| NX-OS Command | NVUE Command | Comments |
| -----         | -----        | -----    |
| `switchport mode access` |  `nv set interface <interface> bridge domain br_default access` | |
| `switchport access vlan <vlan>` |  `nv set interface <interface> bridge domain br_default access <vlan>` | |
| `switchport mode trunk` | `nv set interface <interface> bridge domain br_default` | Ports added to a bridge are trunk ports by default. | 
| `switchport trunk allowed vlan <vlan-list>` | `nv set interface <interface> bridge domain br_default vlan <vlan-list>` | | 
| `spanning-tree port type edge` | `nv set interface <interface> bridge domain br_default stp admin-edge on` | |
| `spanning-tree port type network` | `nv set interface <interface> bridge domain br_default stp network on` | | 
| `spanning-tree bpduguard enable` | `nv set interface <interface> bridge domain br_default stp bpdu-guard on` | | 
| `spanning-tree bpdufilter enable` | `nv set interface <interface> bridge domain br_default stp bpdu-filter on` | | 
| `spanning-tree vlan 1 priority <priority>` | `nv set bridge domain br_default stp priority <priority>` | Cumulus Linux only supports {{<kb_link url="cumulus-linux-44/Layer-2/Spanning-Tree-and-Rapid-Spanning-Tree/#stp-for-a-vlan-aware-bridge" text="RSTP" >}}. |

## Bonds / Port Channels
Linux uses the term `bond` for what Cisco calls `port channels`.

| NX-OS Command | NVUE Command | Comments |
| -----         | -----        | -----    |
| `interface port-channel <number>` | `nv set interface <name> bond` | Bonds are defined with a name that must start with a letter. | 
| `interface ethernet <mod/port>`<br />&nbsp;&nbsp;&nbsp;`channel-group <number>` | `nv set interface <name> bond member <name>` | Cumulus Linux can create the bond and apply the member in a single command. | 
| `channel-group <number> mode on` | `nv set interface <name> bond mode static` | The default mode is `lacp` | 
| `lacp rate fast` | `nv set interface <name> bond lacp-rate fast` | | 

## MLAG / vPC
Cumulus Linux uses `MLAG` (Multi-chassis Link Aggregation) or `CLAG` (Cumulus Link Aggregation) to describe the feature Cisco calls `vPC`.

The concept of a vPC "peer link" is also used in Cumulus Linux MLAG configuration. The vPC "peer-keepalive link" is not used in Cumulus Linux. Instead, a "mlag backup IP" is used to keep MLAG pairs in sync in the case of direct connection failure.

More information about MLAG can be found in the {{<kb_link url="cumulus-linux-44/Layer-2/Multi-Chassis-Link-Aggregation-MLAG/" text="MLAG user guide" >}}.

| NX-OS Command | NVUE Command | Comments |
| -----         | -----        | -----    |
| `peer-keepalive destination <IP>` | `nv set mlag backup <IP>` | |
| `system-mac <mac>` | `nv set mlag mac-address <mac>` | NVUE also supports an `auto` MAC address generation. | 
| `interface port-channel <number>`<br />&nbsp;&nbsp;&nbsp;`vpc peer-link` | `nv set interface peerlink bond member <interface>`<br />`nv set mlag peer-ip linklocal` | Cumulus Linux requires a unique bond for the peerlink and then an associated `peer-ip` definition. | 
| `interface port-channel <number>`<br />&nbsp;&nbsp;&nbsp;`vpc <number>` | `nv set interface <bond-name> bond mlag id auto` | The `mlag id` must match the bond interface on both MLAG peers connected to the same host. Using `auto` determines the ID based on the end-host's MAC address. | 


## Layer 3 Routing Protocols
Most BGP commands require the VRF to be included in the command. This includes the `default` VRF.

| NX-OS Command | NVUE Command | Comments |
| -----         | -----        | -----    |
| `router bgp autonomous-system <ASN>` | `nv set vrf default router bgp autonomous-system <ASN>` | | 
| `router-id <ID>` | `nv set router bgp router-id <ID>` | |
| `neighbor <IP> remote-as <ASN>` | `nv set vrf default router bgp peer <IP> remote-as <ASN>` | Either `external` or `internal` can be used in place of the ASN. |
| `address-family ipv4 unicast`<br />&nbsp;&nbsp;&nbsp;`network <network>` | `nv set vrf default router bgp address-family ipv4-unicast static-network <network>` | | 
| `address-family ipv6 unicast`<br />&nbsp;&nbsp;&nbsp;`network <network>` | `nv set vrf default router bgp address-family ipv6-unicast static-network <network>` | | 
| `address-family ipv6 unicast`<br />&nbsp;&nbsp;&nbsp;`redistribute direct` | `nv set vrf default router bgp address-family ipv4-unicast redistribute connected` | | 
| `ip prefix-list <name> seq <seq> permit <prefix>` | `nv set router policy prefix-list <name> rule <seq> match <prefix>` | |
| `route-map <name> permit <seq>`<br />&nbsp;&nbsp;&nbsp;`match ip prefix-list <list>` | `nv set router policy route-map <name> rule <seq> match ip-prefix-list <list>` | | 
| `neighbor <IP> remote-as <ASN>`<br />&nbsp;&nbsp;&nbsp;`address-family ipv4 unicast`<br />&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`route-map <name> in` | `nv set vrf default router bgp peer <IP> address-family ipv4-unicast policy inbound route-map <name>` | | 
| `ip route <route> <next hop>` | `nv set vrf default routing static <route> via <next hop>` | The `default` value is the VRF name, in this example, the default VRF. | 

## Access Control Lists (ACLs)
ACLs in Cumulus Linux are based on Linux iptables and have two major differences in behavior from NX-OS:
* No implicit deny. ACLs must end in a `match any` and `action deny` rule to drop all unmatched traffic.
* No support for wildcard masks. Subnets must be individually listed. 

Read the {{<kb_link url="cumulus-linux-44/System-Configuration/Netfilter-ACLs/" text="ACL user guide" >}} for more information. 

| NX-OS Command | NVUE Command | Comments |
| -----         | -----        | -----    |
|`ip access-list <name>`<br />&nbsp;&nbsp;&nbsp;`<seq> permit ip <source> <destination>` | `nv set acl <name> rule <seq> match source-ip <source>`<br />`nv set acl <name> rule <seq> match dest-ip <destination>`<br />`nv set acl <name> rule <seq> action permit` | NVUE links the source, destination and actions via the `<seq>` value. | 
|`interface <slot/port>`<br />&nbsp;&nbsp;&nbsp;`ip access-group <name> in` | `nv set interface <interface> acl <name> inbound` | 
|`mac access-list <name>`<br />&nbsp;&nbsp;&nbsp;`<seq> permit <source mac> <destination mac> <protocol>` | `nv set acl <name> rule <seq> match source-mac <source mac>`<br />`nv set acl <name> rule <seq> match dest-mac <destination mac>`<br />`nv set acl <name> rule <seq> match protocol <protocol number>`<br />`nv set acl <name> rule <seq> action permit` | NVUE links the source, destination and actions via the `<seq>` value. | 
|`interface <slot/port>`<br />&nbsp;&nbsp;&nbsp;`mac port access-group <name>` | `nv set interface <interface> acl <name> inbound` | 