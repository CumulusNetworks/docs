---
title: Firewall Rules
author: NVIDIA
weight: 200
toc: 3
---

The Cumulus Linux default firewall rules protect the switch control plane and CPU from DOS and other potentially malicious network attacks.

In Cumulus Linu x 5.8 and earlier, the set of default firewall rules are more open; Cumulus Linux accepts packets from all addresses and protocols. Cumulus Linux 5.9 and later provides a set of default firewall rules that allows only specific addresses and ports, and drops packets from the disallowed addresses and ports.

{{%notice note%}}
The default set of firewall rules consist of IP and transport level rules. To block specific layer 2 packets such as ARP, LLDP, or STP or any packets sent to the CPU as part of generic traps, you must configure separate rules using control plane ACLs in the INPUT or OUTPUT chain of ebtables. See {{<link url="Netfilter-ACLs" text="Netfilter ACLs">}}.
{{%/notice%}}

## DoS Rules

DoS rules protect the switch control plane and CPU from DOS attacks.

Cumulus Linux provides the following firewall policies for DoS rules.

| Policy ID | Description |
| --------- | ---- |
| `FW_RULE_DEFAULT_01` | Rules to allow internal loopback traffic only. |
| `FW_RULE_DEFAULT_02` | Rules to accept already established connections and outbound traffic. |
| `FW_RULE_DEFAULT_03` | Rules to set the `- allow` option to color the packets from a specific interface. Used when different policies need to be applied for different `eth` interfaces. |
| `FW_RULE_DOS_01` | Rules to drop packets if the first TCP segment is not SYN. |
| `FW_RULE_DOS_02` | Rules to drop fragmented IP packets. |
| `FW_RULE_DOS_03` | Rules to drop XMAS tree packets. |
| `FW_RULE_DOS_04` | Rules to drop NULL packets.|
| `FW_RULE_DOS_06` | Rules to drop invalid packets. |
| `FW_RULE_DOS_08` | Rules to drop strange MSS values. |
| `FW_RULE_DOS_10` | Rules for service brute-force protection. |
| `FW_RULE_DOS_14` | Rules to drop packets with routing Header Type 0. |
| `FW_RULE_DOS_15` | Rules to drop packets with a hop limit greater than 1. |
| `FW_LIMIT_DOS_01` | Rules to limit excessive TCP reset packets. |
| `FW_LIMIT_DOS_02` | Rules to protect against SYN flood.|
| `FW_LIMIT_DOS_03` | Rules to limit TCP connections for each IP address. |
| `FW_RULE_DOS_13` | Rules to log all remaining packets, then drop them. |

## Whitelist Rules

Whitelist rules specify the services or application ports enabled on the switch.

Cumulus Linux provides the following firewall policies for whitelist rules.

| Policy ID | Description |
| --------- | ---- |
| `FW_RULE_WHITELIST_00` | Rules to enable TCP ports.|
| `FW_RULE_WHITELIST_01` | Rules to enable UDP ports.|

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

The `/etc/cumulus/acl/policy.d/00control_plane.rules` file stores the DoS rules.

{{< expand "/etc/cumulus/acl/policy.d/00control_plane.rules" >}}

```
cumulus@switch:~$ sudo cat /etc/cumulus/acl/policy.d/00control_plane.rules
...
[iptables] 
## ACL acl-default-dos in dir inbound control-plane ## 
# rule-id #30:  # 
-A INPUT -m comment --comment rule_id:30,acl_name:acl-default-dos,dir:inbound,interface_id:control-plane -p tcp -m conntrack --ctstate ESTABLISHED,RELATED -j ACCEPT 
# rule-id #40:  # 
-A INPUT -m comment --comment rule_id:40,acl_name:acl-default-dos,dir:inbound,interface_id:control-plane -p tcp --tcp-flags SYN,RST,ACK,FIN RST -m conntrack --ctstate NEW -j DROP 
# rule-id #41:  # 
-A INPUT -m comment --comment rule_id:41,acl_name:acl-default-dos,dir:inbound,interface_id:control-plane -p tcp --tcp-flags SYN,RST,ACK,FIN ACK -m conntrack --ctstate NEW -j DROP 
# rule-id #42:  # 
-A INPUT -m comment --comment rule_id:42,acl_name:acl-default-dos,dir:inbound,interface_id:control-plane -p tcp --tcp-flags SYN,RST,ACK,FIN FIN -m conntrack --ctstate NEW -j DROP 
# rule-id #50:  # 
-A INPUT -m comment --comment rule_id:50,acl_name:acl-default-dos,dir:inbound,interface_id:control-plane -f  -j DROP 
# rule-id #60:  # 
-A INPUT -m comment --comment rule_id:60,acl_name:acl-default-dos,dir:inbound,interface_id:control-plane -p tcp --tcp-flags ALL ALL -j DROP 
# rule-id #70:  # 
-A INPUT -m comment --comment rule_id:70,acl_name:acl-default-dos,dir:inbound,interface_id:control-plane -p tcp --tcp-flags ALL NONE -j DROP 
# rule-id #80:  # 
-A INPUT -m comment --comment rule_id:80,acl_name:acl-default-dos,dir:inbound,interface_id:control-plane -p tcp -m conntrack --ctstate INVALID -j DROP 
# rule-id #90:  # 
-A INPUT -m comment --comment rule_id:90,acl_name:acl-default-dos,dir:inbound,interface_id:control-plane -p tcp -m tcpmss ! --mss 536:65535 -m conntrack --ctstate NEW -j DROP 
# rule-id #100:  # 
-A INPUT -m comment --comment rule_id:100,acl_name:acl-default-dos,dir:inbound,interface_id:control-plane -p tcp --dport 22 -m conntrack --ctstate NEW -m recent --set 
# rule-id #110:  # 
-A INPUT -m comment --comment rule_id:110,acl_name:acl-default-dos,dir:inbound,interface_id:control-plane -p tcp --dport 22 -m conntrack --ctstate NEW -m recent --hitcount 10 --seconds 60 --update  -j DROP 
# rule-id #120:  # 
-A INPUT -m comment --comment rule_id:120,acl_name:acl-default-dos,dir:inbound,interface_id:control-plane -p tcp --tcp-flags RST RST -m hashlimit --hashlimit-burst 2 --hashlimit-srcmask 32 --hashlimit-htable-expire 30000 --hashlimit-mode srcip --hashlimit-name TCPRST --hashlimit-above 5/min -j DROP 
# rule-id #130:  # 
-A INPUT -m comment --comment rule_id:130,acl_name:acl-default-dos,dir:inbound,interface_id:control-plane -p tcp -m conntrack --ctstate NEW -m hashlimit --hashlimit-burst 30 --hashlimit-srcmask 32 --hashlimit-htable-expire 30000 --hashlimit-mode srcip --hashlimit-name TCPGENERAL --hashlimit-above 50/second -j DROP 
```
{{< /expand >}}

The `/etc/cumulus/acl/policy.d/98control_plane_whitelist.rules` file stores the whitelist rules and the FW_RULE_DOS_13, which drops packets that don't match any whitelist rule.

{{< expand "/etc/cumulus/acl/policy.d/98control_plane_whitelist.rules" >}}

```
cumulus@switch:~$ sudo cat /etc/cumulus/acl/policy.d/98control_plane_whitelist.rules
...
[iptables] 
## ACL acl-default-whitelist in dir inbound control-plane ## 
# rule-id #1:  # 
-A INPUT -m comment --comment rule_id:1,acl_name:acl-default-whitelist,dir:inbound,interface_id:control-plane -p tcp --dport 22 -m conntrack --ctstate ESTABLISHED,NEW -j ACCEPT 
# rule-id #6:  # 
-A INPUT -m comment --comment rule_id:6,acl_name:acl-default-whitelist,dir:inbound,interface_id:control-plane -p tcp --dport 179 -m conntrack --ctstate ESTABLISHED,NEW -j ACCEPT 
# rule-id #11:  # 
-A INPUT -m comment --comment rule_id:11,acl_name:acl-default-whitelist,dir:inbound,interface_id:control-plane -p tcp --dport 389 -m conntrack --ctstate ESTABLISHED,NEW -j ACCEPT 
# rule-id #16:  # 
-A INPUT -m comment --comment rule_id:16,acl_name:acl-default-whitelist,dir:inbound,interface_id:control-plane -p tcp --dport 8765 -m conntrack --ctstate ESTABLISHED,NEW -j ACCEPT 
# rule-id #21:  # 
-A INPUT -m comment --comment rule_id:21,acl_name:acl-default-whitelist,dir:inbound,interface_id:control-plane -p tcp --dport 443 -m conntrack --ctstate ESTABLISHED,NEW -j ACCEPT 
# rule-id #26:  # 
-A INPUT -m comment --comment rule_id:26,acl_name:acl-default-whitelist,dir:inbound,interface_id:control-plane -p tcp --dport 5342 -m conntrack --ctstate ESTABLISHED,NEW -j ACCEPT 
# rule-id #31:  # 
-A INPUT -m comment --comment rule_id:31,acl_name:acl-default-whitelist,dir:inbound,interface_id:control-plane -p tcp --dport 49 -m conntrack --ctstate ESTABLISHED,NEW -j ACCEPT 
# rule-id #36:  # 
-A INPUT -m comment --comment rule_id:36,acl_name:acl-default-whitelist,dir:inbound,interface_id:control-plane -p udp --dport 68 -m conntrack --ctstate ESTABLISHED,NEW -j ACCEPT 
# rule-id #41:  # 
-A INPUT -m comment --comment rule_id:41,acl_name:acl-default-whitelist,dir:inbound,interface_id:control-plane -p udp --dport 67 -m conntrack --ctstate ESTABLISHED,NEW -j ACCEPT 
# rule-id #46:  # 
-A INPUT -m comment --comment rule_id:46,acl_name:acl-default-whitelist,dir:inbound,interface_id:control-plane -p udp --dport 123 -m conntrack --ctstate ESTABLISHED,NEW -j ACCEPT 
# rule-id #51:  # 
-A INPUT -m comment --comment rule_id:51,acl_name:acl-default-whitelist,dir:inbound,interface_id:control-plane -p udp --dport 323 -m conntrack --ctstate ESTABLISHED,NEW -j ACCEPT 
# rule-id #56:  # 
-A INPUT -m comment --comment rule_id:56,acl_name:acl-default-whitelist,dir:inbound,interface_id:control-plane -p udp --dport 161 -m conntrack --ctstate ESTABLISHED,NEW -j ACCEPT 
# rule-id #61:  # 
-A INPUT -m comment --comment rule_id:61,acl_name:acl-default-whitelist,dir:inbound,interface_id:control-plane -p udp --dport 69 -m conntrack --ctstate ESTABLISHED,NEW -j ACCEPT 
# rule-id #66:  # 
-A INPUT -m comment --comment rule_id:66,acl_name:acl-default-whitelist,dir:inbound,interface_id:control-plane -p udp --dport 389 -m conntrack --ctstate ESTABLISHED,NEW -j ACCEPT 
# rule-id #71:  # 
-A INPUT -m comment --comment rule_id:71,acl_name:acl-default-whitelist,dir:inbound,interface_id:control-plane -p udp --dport 1812 -m conntrack --ctstate ESTABLISHED,NEW -j ACCEPT 
# rule-id #76:  # 
-A INPUT -m comment --comment rule_id:76,acl_name:acl-default-whitelist,dir:inbound,interface_id:control-plane -p udp --dport 1813 -m conntrack --ctstate ESTABLISHED,NEW -j ACCEPT 
# rule-id #81:  # 
-A INPUT -m comment --comment rule_id:81,acl_name:acl-default-whitelist,dir:inbound,interface_id:control-plane -p udp --dport 6343 -m conntrack --ctstate ESTABLISHED,NEW -j ACCEPT 
# rule-id #86:  # 
-A INPUT -m comment --comment rule_id:86,acl_name:acl-default-whitelist,dir:inbound,interface_id:control-plane -p udp --dport 6344 -m conntrack --ctstate ESTABLISHED,NEW -j ACCEPT 
# rule-id #91:  # 
-A INPUT -m comment --comment rule_id:91,acl_name:acl-default-whitelist,dir:inbound,interface_id:control-plane -p udp --dport 514 -m conntrack --ctstate ESTABLISHED,NEW -j ACCEPT 
# rule-id #96:  # 
-A INPUT -m comment --comment rule_id:96,acl_name:acl-default-whitelist,dir:inbound,interface_id:control-plane -p udp --dport 3784 -m conntrack --ctstate ESTABLISHED,NEW -j ACCEPT 
# rule-id #101:  # 
-A INPUT -m comment --comment rule_id:101,acl_name:acl-default-whitelist,dir:inbound,interface_id:control-plane -p udp --dport 4784 -m conntrack --ctstate ESTABLISHED,NEW -j ACCEPT 
# rule-id #106:  # 
-A INPUT -m comment --comment rule_id:106,acl_name:acl-default-whitelist,dir:inbound,interface_id:control-plane -p udp --dport 4789 -m conntrack --ctstate ESTABLISHED,NEW -j ACCEPT 
# rule-id #111:  # 
-A INPUT -m comment --comment rule_id:111,acl_name:acl-default-whitelist,dir:inbound,interface_id:control-plane -p udp --dport 319 -m conntrack --ctstate ESTABLISHED,NEW -j ACCEPT 
# rule-id #116:  # 
-A INPUT -m comment --comment rule_id:116,acl_name:acl-default-whitelist,dir:inbound,interface_id:control-plane -p udp --dport 320 -m conntrack --ctstate ESTABLISHED,NEW -j ACCEPT 
# rule-id #121:  # 
-A INPUT -m comment --comment rule_id:121,acl_name:acl-default-whitelist,dir:inbound,interface_id:control-plane -p tcp --dport 9339 -m conntrack --ctstate ESTABLISHED,NEW -j ACCEPT 
# rule-id #126:  # 
-A INPUT -m comment --comment rule_id:126,acl_name:acl-default-whitelist,dir:inbound,interface_id:control-plane -p tcp -m multiport --dports 31980,31982 -m conntrack --ctstate ESTABLISHED,NEW -j ACCEPT 
# rule-id #131:  # 
-A INPUT -m comment --comment rule_id:131,acl_name:acl-default-whitelist,dir:inbound,interface_id:control-plane -p ospf -j ACCEPT 
# rule-id #999:  # 
-A INPUT -m comment --comment rule_id:999,acl_name:acl-default-whitelist,dir:inbound,interface_id:control-plane  -m limit --limit 1/min -j LOG --log-prefix IPTables-Dropped-<Domain>: --log-level 3 
# rule-id #999:  # 
-A INPUT -m comment --comment rule_id:999,acl_name:acl-default-whitelist,dir:inbound,interface_id:control-plane  -m limit --limit 1/min -j DROP
```
{{< /expand >}}

To add additional firewall rules, refer to {{<link url="Netfilter-ACLs" text="Netfilter ACLs">}}.
