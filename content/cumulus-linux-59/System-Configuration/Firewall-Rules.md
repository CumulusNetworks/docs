---
title: Firewall Rules
author: NVIDIA
weight: 280
toc: 3
---

The Cumulus Linux default firewall rules protect the switch control plane and CPU from DOS and other potentially malicious network attacks.

In Cumulus Linux 5.8 and earlier, the set of default firewall rules are more open; Cumulus Linux accepts packets from all addresses and protocols, which can make the switch more vulnerable to network attacks. Cumulus Linux 5.9 and later provides a set of default firewall rules that allow only specific addresses and ports and drops packets from the addresses or ports that are not allowed.

{{%notice note%}}
The default set of firewall rules consist of IP and transport level rules. To block specific layer 2 packets such as ARP, LLDP, or STP or any packets sent to the CPU as part of generic traps, you must configure separate COPP rules using control plane ACLs in the INPUT or OUTPUT chain of ebtables.
{{%/notice%}}

## DoS Rules

DoS rules protect the switch control plane and CPU from DOS attacks.

Cumulus Linux provides the following DoS rules:

| Rule Name | Description |
| --------- | ---- |
| FW_RULE_DEFAULT_01 | Allows internal loopback traffic only. |
| FW_RULE_DEFAULT_02 | Accepts already established connections and outbound traffic. |
| FW_RULE_DEFAULT_03 | Sets the `- allow` option to color the packets from a specific interface. Used when different policies need to be applied for different `eth` interfaces. |
| FW_RULE_DOS_01 | Drops packets if the first TCP segment is not SYN. |
| FW_RULE_DOS_02 | Drops fragmented IP packets. |
| FW_RULE_DOS_03 | Drops XMAS tree packets. |
| FW_RULE_DOS_04 | Drops NULL packets.|
| FW_RULE_DOS_06 | Drops invalid packets. |
| FW_RULE_DOS_08 | Drops strange MSS values. |
| FW_RULE_DOS_10 | Provides service brute-force protection. |
| FW_RULE_DOS_14 | Drops packets with routing Header Type 0. |
| FW_RULE_DOS_15 | Drops packets with a hop limit greater than 1. |
| FW_LIMIT_DOS_01 | Limits excessive TCP reset packets. |
| FW_LIMIT_DOS_02 | Protects against SYN flood.|
| FW_LIMIT_DOS_03 | Limits TCP connections for each IP address. |
| FW_RULE_DOS_13 | Logs all remaining packets and drops them in the end. |

## Whitelist Rules

Whitelist rules specify the services or application ports enabled on the switch.

Cumulus Linux provides the following Whitelist rules:

| Rule Name | Description |
| --------- | ----------- |
| W_RULE_WHITELIST_00 | |
| W_RULE_WHITELIST_01 | |

The following table lists the ports that Cumulus Linux enables by default.

| Protocol | Port | Application |
| -------- | ---- | ----------- |
|TCP| 22 | SSH |
|TCP| 179 |BGP |
|UDP| 68 |DHCP Client |
|UDP| 67 |DHCP Server |
|Nv sUDP | 123 | NTP |
|UDP| 323 |Chrony |
|UDP | 161 | SNMP |
|UDP | 6306 | A multicast socket used internally. |
|UDP | 69 | TFTP |
|CP/UDP| 389 | LDAP |
|UDP |1812,1813 | RADIUS |
|TCP/UDP | 49 | TACACS |
|TCP/UDP | 53 | DNS |
|TCP | 8765 | NVUE NGINX |
|UDP | 6343 | 6344 sFlow |
|UDP | 514  |remote syslog |
|UDP | 3786 | BFD |
|UDP | 4784 | Multi-Hop BFD |
|TCP | 5342 | MLAG |
|UDP | 4789 | VXLAN |
|UDP | 319/320 | PTP |
|TCP | 443 | HTTPS |
|TCP | 9339 | gNMI |
|TCP | 31980,31982 | NETQ Agent |
|OSPF | NA | NA |

## Unset the Default Firewall Rules

To unset the default firewall rules and use the setting in Cumulus Linux 5.8 and earlier that accepts packets from all addresses and protocols:

```
cumulus@switch:~$ nv unset system control-plane acl acl-default-dos 
cumulus@switch:~$ nv unset system control-plane acl acl-default-whitelist
cumulus@switch:~$ nv config apply
```

To set the firewall rules back to the default Cumulus Linux 5.9 setting:

```
cumulus@switch:~$ nv set system control-plane acl acl-default-dos inbound
cumulus@switch:~$ nv set system control-plane acl acl-default-whitelist inbound
cumulus@switch:~$ nv config apply
```
