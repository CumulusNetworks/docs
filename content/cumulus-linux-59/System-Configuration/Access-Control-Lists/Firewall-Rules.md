---
title: Firewall Rules
author: NVIDIA
weight: 210
toc: 3
---

The Cumulus Linux default firewall rules protect the switch control plane and CPU from DOS and other potentially malicious network attacks.

In Cumulus Linux 5.8 and earlier, the set of default firewall rules are more open; Cumulus Linux accepts packets from all addresses and protocols. Cumulus Linux 5.9 and later provides a set of default firewall rules that allows only specific addresses and ports, and drops packets that are disallowed.

{{%notice note%}}
The default set of firewall rules consists of IP and transport level rules. To block specific layer 2 packets such as ARP, LLDP, or STP or any packets sent to the CPU as part of generic traps, you must configure separate rules using control plane ACLs in the INPUT or OUTPUT chain of ebtables. See {{<link url="Access-Control-List-Configuration" text="Access Control List Configuration">}}.
{{%/notice%}}

## DoS Rules

DoS rules protect the switch control plane and CPU from DOS attacks. Cumulus Linux provides the following firewall DoS rules to:
- Allow internal loopback traffic only.
- Accept already established connections and outbound traffic.
- Set the `- allow` option to color the packets from a specific interface. Used when different policies need to be applied for different `eth` interfaces.
- Drop packets if the first TCP segment is not SYN.
- Drop fragmented IP packets.
- Drop Christmas tree packets; packets with all TCP flags set.
- Drop NULL packets.
- Drop invalid packets.
- Drop strange MSS values.
- Service brute-force protection.
- Drop packets with routing Header Type 0.
- Drop packets with a hop limit greater than 1.
- Limit excessive TCP reset packets.
- Protect against SYN flood.
- Limit TCP connections for each IP address.
- Log all remaining packets, then drop them.

## Whitelist Rules

Whitelist rules specify the services or application ports enabled on the switch. Cumulus Linux provides the following firewall whitelist rules.
- Rules to enable TCP ports.
- Rules to enable UDP ports.

The following table lists the ports that Cumulus Linux enables by default.

| Protocol | Port | Application |
| -------- | ---- | ----------- |
|TCP| 22 | SSH |
|TCP| 179 |BGP |
|UDP| 68 |DHCP Client |
|UDP| 67 |DHCP Server |
|UDP | 123 | NTP |
|UDP| 323 |Chrony |
|UDP | 161 | SNMP |
|UDP | 6306 | A multicast socket used internally. |
|UDP | 69 | TFTP |
|CP/UDP| 389 | LDAP |
|UDP |1812,1813 | RADIUS |
|TCP/UDP | 49 | TACACS |
|TCP/UDP | 53 | DNS |
|TCP | 8765 | NVUE NGINX |
|UDP | 6343, 6344 | sFlow |
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

## Default Firewall Rule Files

Cumulus Linux stores:
- DoS policy rules in the `/etc/cumulus/acl/policy.d/01control_plane.rules` file. 
- Whitelist policy rules in the `/etc/cumulus/acl/policy.d/98control_plane_whitelist.rules` file.
- DoS policy rules to log all remaining packets, then drop them in the `/etc/cumulus/acl/policy.d/98control_plane_whitelist.rules` file.

To add additional rules with NVUE or manually in the `/etc/cumulus/acl/policy.conf` file, refer to {{<link url="Access-Control-List-Configuration" text="Access Control List Configuration">}}.

## Considerations

Default firewall rules include a log rule for packets that arrive in the control plane and do not match user defined or default firewall rules. The switch generates a log message for packets that match the log rule. To avoid console logs for these packets, add an `accept` or `deny` rule for the packets that cause the console logs.
