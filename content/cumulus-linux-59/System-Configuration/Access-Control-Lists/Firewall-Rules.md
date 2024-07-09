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

## Default Firewall Rule Files without NVUE

Cumulus Linux enables the default firewall rules on the switch even before you apply NVUE configuration for the first time. The default firewall rules are in the `01control_plane.rules` and `98control_plane_whitelist.rules` files in the `/etc/cumulus/acl/policy.d/` directory.

If you prefer to configure the switch by editing Linux files instead of running NVUE commands, you can make changes to these files to add additional rules.

## DoS Rules

DoS rules protect the switch control plane and CPU from DOS attacks. Cumulus Linux provides firewall DoS rules to:
- Allow only internal traffic to the loopback interfaces.
- Accept already established connections and outbound traffic.
- Set the `- allow` option to color the packets from a specific interface. Used when different policies need to be applied for different `eth` interfaces.
- Drop packets if the first TCP segment is not SYN.
- Drop fragmented IP packets.
- Drop Christmas tree packets; packets with all TCP flags set.
- Drop NULL packets.
- Drop invalid packets.
- Drop strange MSS values.
- Provide brute-force protection.
- Drop packets with routing Header Type 0.
- Drop packets with a hop limit greater than 1.
- Limit excessive TCP reset packets.
- Protect against SYN flood.
- Rate limit new TCP connections for each IP address.
- Log all remaining packets, then drop them.

## Whitelist Rules

Whitelist rules specify the services or application ports enabled on the switch. Cumulus Linux provides firewall whitelist rules to enable TCP ports and UDP ports.

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
|TCP/UDP| 389 | LDAP |
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
|UDP | 319,320 | PTP |
|TCP | 443 | HTTPS |
|TCP | 9339 | gNMI |
|TCP | 31980,31982 | NETQ Agent |
|OSPF | NA | NA |
|UDP | 53 (SPORT) | DNS response packets |
|TCP | 9999 | XMLRPC |
|ICMP | NA | Ping |
|PIM | NA | NA |
|IGMP | NA | NA |
|VRRP | NA | NA |
|TCP |639 | MSDP |

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

## Add Firewall Rules

You cannot modify the `acl-default-dos` and `acl-default-whitelist` rules. However, you can append or insert additional rules. Additionally, you can add your own ACLs and {{<link url="Access-Control-List-Configuration/#control-plane-acls" text="apply them on the control plane">}}; control plane ACLs take precedence over `acl-default-whitelist` rules when the default firewall rules are enabled.

If you use non-default ports for an application, NVIDIA recommends that you add a whitelist rule for the non-default port. For example, if you use ports 3020 and 3022 for radius server accounting and authentication instead of 1812 and 1813, you can add the following whitelist rules:

```
cumulus@switch:~$ nv set acl acl-default-whitelist rule 73 match ip udp source-port 3020
cumulus@switch:~$ nv set acl acl-default-whitelist rule 73 match ip connection-state new
cumulus@switch:~$ nv set acl acl-default-whitelist rule 73 match ip connection-state established
cumulus@switch:~$ nv set acl acl-default-whitelist rule 73 action permit
cumulus@switch:~$ nv set acl acl-default-whitelist rule 74 match ip udp source-port 3022
cumulus@switch:~$ nv set acl acl-default-whitelist rule 74 match ip connection-state new
cumulus@switch:~$ nv set acl acl-default-whitelist rule 74 match ip connection-state established
cumulus@switch:~$ nv set acl acl-default-whitelist rule 74 action permit
cumulus@switch:~$ nv config apply
```

## Hashlimit and Recent List Match

For firewall IPv4 type ACLs on the control plane, you can match on hashlimit and recent list. These matches are not supported for data plane ACLs, which get installed in hardware.

Cumulus Linux provides the following commands for matching on `hashlimit`.

|Command | Description |
| ------ | ----------- |
| `nv set acl <acl> rule <rule> match ip hashlimit name` | The hashlimit name. |
| `nv set acl <acl> rule <rule> match ip hashlimit mode` | The hashlimit mode. You can specify `src-ip` or `dst-ip`.  |
| `nv set acl <acl> rule <rule> match ip hashlimit burst` | The hashlimit burst rate; the maximum number of packets to match in a burst. You can specify a value between 1 and 4294967295. |
| `nv set acl <acl> rule <rule> match ip hashlimit rate-above` | The limit rate. You can specify `<integer/second>`, `<integer/min>`, or `<integer/hour>`. The maximum rate is 1000000/second. |
| `nv set acl <acl> rule <rule> match ip hashlimit expire` | The number of milliseconds after which hash entries expire. |
| `nv set acl <acl> rule <rule> match ip hashlimit source-mask` | The source address grouping prefix length. |
| `nv set acl <acl> rule <rule> match ip hashlimit destination-mask` | The destination address grouping prefix length. |

The following example shows an ACL that drops packets when matching on `hashlimit`.

{{%notice note%}}
To configure the hashlimit match, you must set the hashlimit name, mode, expiration, burst, and rate; the source mask and destination mask settings are optional.
{{%/notice%}}

```
cumulus@switch:~$ nv set acl EXAMPLE1 type ipv4
cumulus@switch:~$ nv set acl EXAMPLE1 rule 10 match ip protocol tcp
cumulus@switch:~$ nv set acl EXAMPLE1 rule 10 match ip source-ip 10.0.14.2/32
cumulus@switch:~$ nv set acl EXAMPLE1 rule 10 match ip hashlimit name ssh
cumulus@switch:~$ nv set acl EXAMPLE1 rule 10 match ip hashlimit mode src-ip 
cumulus@switch:~$ nv set acl EXAMPLE1 rule 10 match ip hashlimit expire 100
cumulus@switch:~$ nv set acl EXAMPLE1 rule 10 match ip hashlimit burst 100
cumulus@switch:~$ nv set acl EXAMPLE1 rule 10 match ip hashlimit rate-above 100/second
cumulus@switch:~$ nv set acl EXAMPLE1 rule 10 match ip hashlimit source-mask 32
cumulus@switch:~$ nv set acl EXAMPLE1 rule 10 action deny
cumulus@switch:~$ nv set interface swp1 acl EXAMPLE1 inbound control-plane
cumulus@switch:~$ nv config apply
```

NVUE writes this rule in the `/etc/cumulus/acl/policy.d/50_nvue.rules` file:

```
cumulus@switch:~$ sudo cat /etc/cumulus/acl/policy.d/50_nvue.rules
[iptables]
## ACL EXAMPLE1 in dir inbound on interface swp1 ##
# rule-id #10:  #
-A INPUT -i swp1 -m comment --comment rule_id:10,acl_name:EXAMPLE1,dir:inbound,interface_id:swp1 -s 10.0.14.2/32 -p tcp -m hashlimit --hashlimit-name ssh --hashlimit-mode srcip --hashlimit-htable-expire 100 --hashlimit-burst 100 --hashlimit-above 100/second --hashlimit-srcmask 32 -j DROP
```

You can also show the ACL settings with the `nv show acl <acl>` command:

```
cumulus@switch:~$ nv show acl EXAMPLE1
      applied
----  -------
type  ipv4
rule
=======
    Number  Summary                                   
    ------  ------------------------------------------
    10      match.ip.hashlimit.burst:              100
            match.ip.hashlimit.expire:             100
            match.ip.hashlimit.mode:            src-ip
            match.ip.hashlimit.name:            ssh
            match.ip.hashlimit.rate-above: 100/second
            match.ip.hashlimit.source-mask:         32
            match.ip.protocol:                     tcp
            match.ip.source-ip:           10.0.14.2/32
```

Cumulus Linux provides the following commands to match on `recent list`.

|Command | Description |
| ------ | ----------- |
| `nv set acl <acl> rule <rule> match ip recent-list name`| The recent module name.  |
| `nv set acl <acl> rule <rule> match ip recent-list action`| The recent action. You can specify `set` or `update`. |
| `nv set acl <acl> rule <rule> match ip recent-list hit-count`| The number of hits in an interval. You can specify a value between 1 and 4294967295. |
| `nv set acl <acl> rule <rule> match ip recent-list update-interval`| The update interval. You can specify a value between 1 and 4294967295. |

The following example shows an ACL that drops packets when matching on `recent-list`.

{{%notice note%}}
To configure the recent module match, you must set the recent list name and action; other `recent-list` settings are optional.
{{%/notice%}}

```
cumulus@switch:~$ nv set acl EXAMPLE1 type ipv4
cumulus@switch:~$ nv set acl EXAMPLE1 rule 10 match ip protocol tcp
cumulus@switch:~$ nv set acl EXAMPLE1 rule 10 match ip source-ip 10.0.14.2/32
cumulus@switch:~$ nv set acl EXAMPLE1 rule 10 match ip recent-list name bruteforce
cumulus@switch:~$ nv set acl EXAMPLE1 rule 10 match ip recent-list action set
cumulus@switch:~$ nv set acl EXAMPLE1 rule 10 match ip recent-list hit-count 5
cumulus@switch:~$ nv set acl EXAMPLE1 rule 10 match ip recent-list update-interval 3600
cumulus@switch:~$ nv set acl EXAMPLE1 rule 10 action deny
cumulus@switch:~$ nv set interface swp1 acl EXAMPLE1 inbound control-plane
cumulus@switch:~$ nv config apply
```

NVUE writes this rule in the `/etc/cumulus/acl/policy.d/50_nvue.rules` file:

```
cumulus@switch:~$ sudo cat /etc/cumulus/acl/policy.d/50_nvue.rules
[iptables]

## ACL EXAMPLE1 in dir inbound on interface swp1 ##
# rule-id #10:  #
-A INPUT -i swp1 -m comment --comment rule_id:10,acl_name:EXAMPLE1,dir:inbound,interface_id:swp1 -s 10.0.14.2/32 -p tcp -m recent --name bruteforce --set  --hitcount 5 --seconds 360 -j DROP
```

You can also show the ACL settings with the NVUE `nv show acl <acl>` command.

## Show Firewall Rules

To show the DoS rules, run the `nv show acl acl-default-dos` command:

```
cumulus@switch:~$ nv show acl acl-default-dos
      applied  pending
----  -------  -------
type  ipv4     ipv4   
rule
=======
    Number  Summary                                 
    ------  ----------------------------------------
    30      match.ip.protocol:                   tcp
    40      match.ip.protocol:                   tcp
    41      match.ip.protocol:                   tcp
    42      match.ip.protocol:                   tcp
    50                                              
    60      match.ip.protocol:                   tcp
    70      match.ip.protocol:                   tcp
    80      match.ip.protocol:                   tcp
    90      match.ip.protocol:                   tcp
            match.ip.tcp.all-mss-except:   536-65535
    100     match.ip.recent-list.action:         set
            match.ip.tcp.dest-port:               22
    110     match.ip.recent-list.action:      update
            match.ip.recent-list.hit-count:       50
            match.ip.recent-list.update-interval: 60
            match.ip.tcp.dest-port:               22
    120     match.ip.hashlimit.burst:              2
            match.ip.hashlimit.expire:         30000
            match.ip.hashlimit.mode:          src-ip
            match.ip.hashlimit.name:          TCPRST
            match.ip.hashlimit.rate-above:     5/min
            match.ip.hashlimit.source-mask:       32
            match.ip.protocol:                   tcp
    130     match.ip.hashlimit.burst:             30
            match.ip.hashlimit.expire:         30000
            match.ip.hashlimit.mode:          src-ip
            match.ip.hashlimit.name:      TCPGENERAL
            match.ip.hashlimit.rate-above: 50/second
            match.ip.hashlimit.source-mask:       32
            match.ip.protocol:                   tcp
```

Run the `nv show acl acl-default-dos --rev=applied -o json` command to show additional information, such as the connection state, hit count and update interval:

```
cumulus@switch:~$ nv show acl acl-default-dos --rev=applied -o json
{
  "rule": {
    "100": {
      "action": {
        "recent": {}
      },
      "match": {
        "ip": {
          "connection-state": {
            "new": {}
          },
          "recent-list": {
            "action": "set"
          },
          "tcp": {
            "dest-port": {
              "22": {}
            }
          }
        }
      }
    },
    "110": {
      "action": {
        "deny": {}
      },
      "match": {
        "ip": {
          "connection-state": {
            "new": {}
          },
          "recent-list": {
            "action": "update",
            "hit-count": 50,
            "update-interval": 60
          },
          "tcp": {
            "dest-port": {
              "22": {}
            }
          }
        }
      }
    },
...
```

To show the whitelist rules, run the `nv show acl acl-default-whitelist` command:

```
cumulus@switch:~$ nv show acl acl-default-whitelist 
      applied  pending
----  -------  -------
type  ipv4     ipv4
rule
=======
    Number  Summary                                          
    ------  -------------------------------------------------
    5       match.ip.protocol:                            tcp
            match.ip.tcp.dest-port:                       ssh
    10      match.ip.protocol:                            tcp
            match.ip.tcp.dest-port:                       bgp
    15      match.ip.protocol:                            tcp
            match.ip.tcp.dest-port:                      ldap
    20      match.ip.protocol:                            tcp
            match.ip.tcp.dest-port:                      8765
    25      match.ip.protocol:                            tcp
            match.ip.tcp.dest-port:                     https
    30      match.ip.protocol:                            tcp
            match.ip.tcp.dest-port:                      clag
    35      match.ip.protocol:                            tcp
            match.ip.tcp.source-port:                      49
    40      match.ip.protocol:                            udp
            match.ip.udp.dest-port:               dhcp-client
    45      match.ip.protocol:                            udp
            match.ip.udp.dest-port:               dhcp-server
    50      match.ip.protocol:                            udp
            match.ip.udp.dest-port:                       ntp
    55      match.ip.protocol:                            udp
            match.ip.udp.dest-port:                       323
    60      match.ip.protocol:                            udp
            match.ip.udp.dest-port:                      snmp
    65      match.ip.protocol:                            udp
            match.ip.udp.dest-port:                      tftp
    70      match.ip.protocol:                            udp
            match.ip.udp.dest-port:                      ldap
    75      match.ip.protocol:                            udp
            match.ip.udp.source-port:                    1812
    80      match.ip.protocol:                            udp
            match.ip.udp.source-port:                    1813
    85      match.ip.protocol:                            udp
            match.ip.udp.dest-port:                      6343
    90      match.ip.protocol:                            udp
            match.ip.udp.dest-port:                      6344
    95      match.ip.protocol:                            udp
            match.ip.udp.dest-port:                       514
    100     match.ip.protocol:                            udp
            match.ip.udp.dest-port:                       bfd
    105     match.ip.protocol:                            udp
            match.ip.udp.dest-port:              bfd-multihop
    110     match.ip.protocol:                            udp
            match.ip.udp.dest-port:                      4789
    115     match.ip.protocol:                            udp
            match.ip.udp.dest-port:                       319
    120     match.ip.protocol:                            udp
            match.ip.udp.dest-port:                       320
    125     match.ip.protocol:                            tcp
            match.ip.tcp.dest-port:                      9339
    130     match.ip.protocol:                            tcp
            match.ip.tcp.dest-port:                     31980
            match.ip.tcp.dest-port:                     31982
    135     match.ip.protocol:                            tcp
            match.ip.tcp.dest-port:                       639
    140     match.ip.protocol:                            udp
            match.ip.udp.source-port:                      53
    145     match.ip.protocol:                            tcp
            match.ip.tcp.dest-port:                      9999
    150     match.ip.protocol:                           ospf
    155     match.ip.protocol:                            pim
    160     match.ip.protocol:                           vrrp
    165     match.ip.protocol:                           igmp
    170     match.ip.protocol:                           icmp
    9999    Log Level:                                      3
            action.log.log-prefix: IPTables-Dropped-<Domain>:
            Log Rate:                                       1
```

Run the `nv show acl acl-default-whitelist --rev=applied -o json` command to show additional information, such as the connection state:

```
cumulus@switch:~$ nv show acl acl-default-whitelist --rev=applied -o json
{
  "rule": {
    "10": {
      "action": {
        "permit": {}
      },
      "match": {
        "ip": {
          "connection-state": {
            "established": {},
            "new": {}
          },
          "protocol": "tcp",
          "tcp": {
            "dest-port": {
              "bgp": {}
            }
          }
        }
      }
    },
    "100": {
      "action": {
        "permit": {}
      },
      "match": {
        "ip": {
          "connection-state": {
            "established": {},
            "new": {}
          },
          "protocol": "udp",
          "udp": {
            "dest-port": {
              "bfd": {}
            }
          }
        }
      }
...
```

To show information about a specific rule, run the `nv show acl acl-default-dos rule <rule>` command:

```
cumulus@switch:~$ nv show acl acl-default-dos rule 30
              applied  pending
------------  -------  -------
match                         
  ip                          
    protocol  tcp      tcp
```

 Run the `nv show acl acl-default-dos rule <rule> --rev=applied -o json` command to see additional information, such as the connection state:

```
cumulus@switch:~$ nv show acl acl-default-dos rule 30 --rev=applied -o json
{
  "action": {
    "permit": {}
  },
  "match": {
    "ip": {
      "connection-state": {
        "established": {},
        "related": {}
      },
      "protocol": "tcp"
    }
  }
}
```

## Syslog Messages

Default firewall rules include a log rule for packets that arrive in the control plane and do not match user defined or default firewall rules. The switch generates a log message in `/var/log/syslog` for packets that match the log rule.
