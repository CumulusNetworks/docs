---
title: NX-OS to NVUE Common Commands
weight: 300
---

Cumulus Linux version 4.4 introduces a new CLI called [NVUE]({{<ref "/cumulus-linux-51/System-Configuration/NVIDIA-User-Experience-NVUE/" >}}); a complete object model for Cumulus Linux. NVUE makes translating configurations from one vendor to another much more reliable the first time you use Cumulus Linux and across Cumulus Linux versions.

This KB article describes how to translate common NX-OS configurations to NVUE commands.

## Feature Enablement

{{<notice note >}}
Unlike NX-OS, Cumulus Linux does not require the enabling of specific features.
{{</notice >}}

## Hostname and System Commands

| NX-OS Command | NVUE Command | Comments |
| -----         | -----        | -----    |
| `hostname <hostname>` | `nv set system hostname <hostname>` ||
| `logging server <ip>` | `nv set service syslog default server <ip>` | The value `default` is the VRF the server is in. |
| `ntp server <ip>` | `nv set service ntp default server <ip>` | The value `default` is the VRF the server is in.
| `interface breakout module 1 port <port> map 10g-4x` | `nv set interface <interface> link breakout 4x10G`| Multiple breakout options exist. To see all commands, run `nv set interface <interface> link breakout -h`. |
| `copy running-config startup-config` | `nv config save` | To apply (commit) configuration as running-config in NVUE, use `nv config apply`. Saved configuration is not applied untill switch rebooted|
| `show startup-config` | `cat /etc/nvue.d/startup.yaml` | |
| `show running-config` | `nv config diff empty applied` | NVUE diff compares an `empty` configuration against the currently `applied` configuration. |
<!-- | `banner motd <banner>` | | | -->

## Interface Commands

You configure NX-OS interface commands under an individual interface; for example:

```
interface e1/1
   ip address 10.1.1.1/24
```

| NX-OS Command | NVUE Command | Comments |
| -----         | -----        | -----    |
| `ip address <ip>` | `nv set interface <interface> ip address <ip>` | In NVUE, you set IPv4 and IPv6 addresses with the same command. |
| `ip address <ip> secondary` | `nv set interface <interface> ip address <ip>` | Configuring a second IP address is additive. To replace an address, run `nv unset interface <interface> address <ip>`. |
| `ipv6 address <ip>` | `nv set interface <interface> ip address <ip>` | In NVUE, you set IPv4 and IPv6 addresses with the same command. |
| `mtu <mtu>` | `nv set interface <interface> link mtu <mtu>` | The default MTU in Cumulus Linux is 9216. |
| `speed <speed>` | `nv set interface <interface> link speed <speed>` | |
| `fec <mode>` | `nv set interface link fec <mode>` | |
| `no shutdown` | `nv set interface <interface> link state up` | The default state for interfaces is `up`. To shut down an interface, use `link state down`. |
| `interface loopback0` | `nv set interface lo` | `lo` is the name of the loopback interface on Cumulus Linux. |
| `description <text>` | `nv set interface <interface> description <text>` | | 

## Layer 2 and VLANs

Cumulus Linux interfaces are layer 3 routed interfaces by default. To make an interface a layer 2 switchport, you must add the interface to the default bridge called `br_default`:

```
cumulus@switch:~$ nv set interface <interface> bridge domain br_default
```

| NX-OS Command | NVUE Command | Comments |
| -----         | -----        | -----    |
| `switchport mode access` |  `nv set interface <interface> bridge domain br_default access <vlan>` | Use `<auto>` to inherit the defualt bridge switchport configuration. |
| `switchport access vlan <vlan>` |  `nv set interface <interface> bridge domain br_default access <vlan>` | |
| `switchport mode trunk` | `nv set interface <interface> bridge domain br_default` | Ports you add to a bridge are trunk ports by default. |
| `switchport trunk allowed vlan <vlan-list>` | `nv set interface <interface> bridge domain br_default vlan <vlan-list>` | |
| `spanning-tree port type edge` | `nv set interface <interface> bridge domain br_default stp admin-edge on` | |
| `spanning-tree port type network` | `nv set interface <interface> bridge domain br_default stp network on` | |
| `spanning-tree bpduguard enable` | `nv set interface <interface> bridge domain br_default stp bpdu-guard on` | |
| `spanning-tree bpdufilter enable` | `nv set interface <interface> bridge domain br_default stp bpdu-filter on` | |
| `spanning-tree vlan 1 priority <priority>` | `nv set bridge domain br_default stp priority <priority>` | Cumulus Linux only supports {{<kb_link latest="cl" url="Layer-2/Spanning-Tree-and-Rapid-Spanning-Tree.md" text="RSTP." >}} |

## Bonds and Port Channels

Linux uses the term `bond` whereas Cisco uses the term `port channels`.

| NX-OS Command | NVUE Command | Comments |
| -----         | -----        | -----    |
| `interface port-channel <number>` | `nv set interface <name> bond` | You define bonds with a name that must start with a letter. |
| `interface ethernet <mod/port>`<br />&nbsp;&nbsp;&nbsp;`channel-group <number>` | `nv set interface <bond-name> bond member <interface>` | You create the bond and apply the bond member in a single command. |
| `channel-group <number> mode on` | `nv set interface <bond-name> bond mode static` | The default mode is `lacp` |
| `lacp rate fast` | `nv set interface <bond-name> bond lacp-rate fast` | |

## MLAG and vPC

Cumulus Linux uses `MLAG` (Multi-chassis Link Aggregation) to describe the feature Cisco calls `vPC`.

In MLAG configuration, Cumulus Linux also uses the concept of a vPC *peer link*. To keep MLAG pairs in sync when a direct connection fails, Cumulus Linux uses *mlag backup IP* instead of the vPC *peer-keepalive link*.

For more information about MLAG, refer to the s section of the Cumulus Linux User Guide.

| NX-OS Command | NVUE Command | Comments |
| -----         | -----        | -----    |
| `peer-keepalive destination <ip>` | `nv set mlag backup <ip>` | |
| `system-mac <mac>` | `nv set mlag mac-address <mac>` | NVUE also supports `auto` MAC address generation. |
| `interface port-channel <number>`<br />&nbsp;&nbsp;&nbsp;`vpc peer-link` | `nv set interface peerlink bond member <interface>`<br />`nv set mlag peer-ip linklocal` | Cumulus Linux requires a unique bond for the peerlink and an associated `peer-ip` definition. |
| `interface port-channel <number>`<br />&nbsp;&nbsp;&nbsp;`vpc <number>` | `nv set interface <bond-name> bond mlag id auto` | The `mlag id` must match the bond interface on both MLAG peers connected to the same host. Using `auto` determines the ID based on the MAC address of the end host. |

## Layer 3 Routing Protocols

Most BGP commands require the inclusion of the VRF in the command. This includes the `default` VRF.

| NX-OS Command | NVUE Command | Comments |
| -----         | -----        | -----    |
| `router bgp autonomous-system <ASN>` | `nv set vrf default router bgp autonomous-system <ASN>` | |
| `router-id <ID>` | `nv set vrf default router bgp router-id <id>` | |
| `neighbor <ip> remote-as <ASN>` | `nv set vrf default router bgp neighbor <ip> remote-as <ASN>` | You can use either `external` or `internal` instead of the ASN. |
| `address-family ipv4 unicast`<br />&nbsp;&nbsp;&nbsp;`network <network>` | `nv set vrf default router bgp address-family ipv4-unicast static-network <network>` | |
| `address-family ipv6 unicast`<br />&nbsp;&nbsp;&nbsp;`network <network>` | `nv set vrf default router bgp address-family ipv6-unicast static-network <network>` | |
| `address-family ipv6 unicast`<br />&nbsp;&nbsp;&nbsp;`redistribute direct` | `nv set vrf default router bgp address-family ipv4-unicast redistribute connected` | |
| `ip prefix-list <name> seq <seq> permit <prefix>` | `nv set router policy prefix-list <name> rule <seq> match <prefix>` | |
| `route-map <name> permit <seq>`<br />&nbsp;&nbsp;&nbsp;`match ip prefix-list <list>` | `nv set router policy route-map <name> rule <seq> match ip-prefix-list <name>` | |
| `neighbor <ip> remote-as <ASN>`<br />&nbsp;&nbsp;&nbsp;`address-family ipv4 unicast`<br />&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`route-map <name> in` | `nv set vrf default router bgp neighbor <ip> address-family ipv4-unicast policy inbound route-map <name>` | |
| `ip route <route> <next hop>` | `nv set vrf default router static <route> via <next hop>` | The `default` value is the VRF name (the default VRF in this example). |

## Access Control Lists (ACLs)

ACLs in Cumulus Linux derive from Linux `iptables` and behave differently from NX-OS in the following ways:

- No implicit deny. ACLs must end in a `match any` and `action deny` rule to drop all unmatched traffic.
- No support for wildcard masks. You must list subnets individually.

For more information, refer to the {{<kb_link latest="cl" url="System-Configuration/Access-Control-Lists/Access-Control-List-Configuration.md" text="ACLs" >}} section of the Cumulus Linux User Guide.

| NX-OS Command | NVUE Command | Comments |
| -----         | -----        | -----    |
|`ip access-list <name>`<br />&nbsp;&nbsp;&nbsp;`<seq> permit ip <source> <destination>` | `nv set acl <name> rule <seq> match ip source-ip <source>`<br />`nv set acl <name> rule <seq> match ip dest-ip <destination>`<br />`nv set acl <name> rule <seq> action permit` | NVUE links the source, destination, and actions with the `<seq>` value. |
|`interface <slot/port>`<br />&nbsp;&nbsp;&nbsp;`ip access-group <name> in` | `nv set interface <interface> acl <name> inbound` |
|`mac access-list <name>`<br />&nbsp;&nbsp;&nbsp;`<seq> permit <source mac> <destination mac> <protocol>` | `nv set acl <name> rule <seq> match mac source-mac <source mac>`<br />`nv set acl <name> rule <seq> match mac dest-mac <destination mac>`<br />`nv set acl <name> rule <seq> match <mac|ip> protocol <protocol number>`<br />`nv set acl <name> rule <seq> action permit` | NVUE links the source, destination, and actions with the `<seq>` value. |
|`interface <slot/port>`<br />&nbsp;&nbsp;&nbsp;`mac port access-group <name>` | `nv set interface <interface> acl <name> inbound` |
