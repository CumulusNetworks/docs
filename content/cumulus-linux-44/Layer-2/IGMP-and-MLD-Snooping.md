---
title: IGMP and MLD Snooping
author: NVIDIA
weight: 520
toc: 3
---
Internet Group Management Protocol (IGMP) snooping and Multicast Listener Discovery (MLD) snooping prevent hosts on a local network from receiving traffic for a multicast group they have not explicitly joined. IGMP snooping is for IPv4 environments and MLD snooping is for IPv6 environments.

The bridge driver in Cumulus Linux kernel includes IGMP and MLD snooping. If you disable IGMP or MLD snooping, multicast traffic floods to all the bridge ports in the bridge. Similarly, in the absence of receivers in a VLAN, multicast traffic floods to all ports in the VLAN.

{{< img src = "/images/cumulus-linux/igmp_snoop_diagram.png" >}}

<!--BROADCOM ONLY## Configure IGMP/MLD Snooping over VXLAN

Cumulus Linux supports IGMP/MLD snooping over VXLAN bridges, where VXLAN ports are set as router ports, on Broadcom switches.

To enable IGMP/MLD snooping over VXLAN:

{{< tabs "TabID31 ">}}

{{< tab "NCLU Commands ">}}

```
cumulus@switch:~$ net add bridge mybridge mcsnoop yes
cumulus@switch:~$ net pending
cumulus@switch:~$ net commit
```

{{< /tab >}}

{{< tab "Linux Commands ">}}

```
cumulus@switch:~$ sudo nano /etc/network/interfaces
...
auto bridge
iface bridge
  bridge-ports swp1 swp2 swp3
  bridge-vlan-aware yes
  bridge-vids 100 200
  bridge-pvid 1
  bridge-mcsnoop yes
...
```

Run the `ifreload -a` command to reload the configuration:

```
cumulus@switch:~$ sudo ifreload -a
```

{{< /tab >}}

{{< /tabs >}}

Consider also configuring IGMP/MLD querier. See {{<link url="#configure-igmpmld-querier" text="Configure IGMP/MLD Querier">}}, below.

To disable IGMP/MLD snooping over VXLAN, run the `net add bridge <bridge> mcsnoop no` command.-->

## Configure the IGMP and MLD Querier

Without a multicast router, a single switch in an IP subnet can coordinate multicast traffic flows. This switch is the querier or the designated router. The querier generates query messages to check group membership, and processes membership reports and leave messages.

To configure the querier on the switch for a {{<link url="VLAN-aware-Bridge-Mode" text="VLAN-aware bridge">}}, enable the multicast querier on the bridge and add the source IP address of the queries to the VLAN.

The following configuration example enables the multicast querier and sets source IP address of the queries to 10.10.10.1 (the loopback address of the switch).

{{< tabs "TabID68 ">}}
{{< tab "NCLU Commands ">}}

NCLU commands are not supported.

{{< /tab >}}
{{< tab "NVUE Commands ">}}

```
cumulus@switch:~$ nv set bridge domain br_default multicast snooping querier enable on
cumulus@switch:~$ nv set bridge domain br_default vlan vlan10 multicast snooping querier source-ip 10.10.10.1
cumulus@switch:~$ nv config apply
```

NVUE commands for a bridge in {{<link url="Traditional-Bridge-Mode" text="traditional mode">}} are not supported.

{{< /tab >}}
{{< tab "Linux Commands ">}}

Edit the `/etc/network/interfaces` file to add `bridge-mcquerier 1` to the bridge stanza (this enables the multicast querier on the bridge) and add `bridge-igmp-querier-src <ip-address>` to the VLAN stanza (the is the source IP address of the queries).

```
cumulus@switch:~$ sudo nano /etc/network/interfaces
...
auto vlan10
iface vlan10
  address 10.1.10.2/24
  vlan-id 10
  vlan-raw-device bridge
  bridge-igmp-querier-src 10.10.10.1

auto br_default
iface br_default
  bridge-ports swp1 swp2 swp3
  bridge-vlan-aware yes
  bridge-vids 10 20
  bridge-pvid 1
  bridge-mcquerier 1
...
```

Run the `ifreload -a` command to reload the configuration:

```
cumulus@switch:~$ sudo ifreload -a
```

To configure the querier on the switch for a bridge in {{<link url="Traditional-Bridge-Mode" text="traditional mode">}}, edit the bridge stanza in the `/etc/network/interfaces` file to add `bridge-mcquerier 1` (this enables the multicast querier on the bridge) and `bridge-mcqifaddr` to 1 (this configures the source IP address of the queries to be the bridge IP address).

```
...
auto br0
iface br0
  address 10.10.10.10/24
  bridge-ports swp1 swp2 swp3
  bridge-vlan-aware no
  bridge-mcquerier 1
  bridge-mcqifaddr 1
...
```

Run the `ifreload -a` command to reload the configuration:

```
cumulus@switch:~$ sudo ifreload -a
```

{{< /tab >}}
{{< /tabs >}}

## Optimized Multicast Flooding (OMF)

IGMP snooping restricts multicast forwarding only to the ports that receive IGMP report messages. If the ports do not receive IGMP reports, multicast traffic floods to all ports in the bridge domain (also know as unregistered multicast (URMC) traffic). To restrict this flooding to only mrouter ports, you can enable OMF.

To enable OMF:

1. Configure an IGMP querier. See {{<link url="#configure-the-igmp-and-mld-querier" text="Configure the IGMP and MLD Querier">}} above.
2. In the `IGMP snooping unregistered L2 multicast flood control` section of the `/etc/cumulus/switchd.conf` file, uncomment and change these settings to TRUE, then restart `switchd`.

   - `bridge.unreg_mcast_init`
   - `bridge.unreg_v4_mcast_prune`
   - `bridge.unreg_v6_mcast_prune`

   ```
   cumulus@switch:~$ sudo nano /etc/cumulus/switchd.conf
   ...
   #IGMP snooping unregistered L2 multicast flood control
   #
   #Initialize prune module:
   bridge.unreg_mcast_init = TRUE
   #
   #Note:
   #Below configuration allowed only when bridge.unreg_mcast_init is set to TRUE
   #
   #Set below to TRUE to enable unregistered L2 multicast prune to mrouter ports.
   #Default is to flood the unregistered L2 multicast
   #
   bridge.unreg_v4_mcast_prune = TRUE
   bridge.unreg_v6_mcast_prune = TRUE
   ```
<!-- vale off -->
   {{<cl/restart-switchd>}}
<!-- vale on -->
When IGMP reports go to a multicast group, OMF has no effect; normal IGMP snooping occurs.

When you enable OMF, you can configure a bridge port as an mrouter port to forward unregistered multicast traffic to that port.

{{< tabs "TabID175 ">}}
{{< tab "NCLU Commands ">}}

```
cumulus@switch:mgmt:~$ net add interface swp1 bridge portmcrouter enabled
cumulus@switch:mgmt:~$ net commit
```

{{< /tab >}}
{{< tab "NVUE Commands ">}}

NVUE commands are not supported.

{{< /tab >}}
{{< tab "Linux Commands ">}}

Edit the `/etc/network/interfaces` file to add `bridge-portmcrouter enabled` to the swp1 stanza.

```
cumulus@switch:~$ sudo nano /etc/network/interfaces
...
auto swp1
iface swp1
   bridge-portmcrouter enabled
...
```

Run the `ifreload -a` command to reload the configuration:

```
cumulus@switch:~$ sudo ifreload -a
```

{{< /tab >}}
{{< /tabs >}}

{{%notice note%}}
OMF increases memory usage, which can impact scaling on Spectrum 1 switches.
{{%/notice%}}

## Improve Multicast Convergence

For large multicast environments, the default [CoPP](## "Control Plane Policing") policer might be too restrictive. You can adjust the policer to improve multicast convergence.

For both IGMP and MLD, the default forwarding rate is set to 300 packets per second and the default burst rate is set to 100 packets. To tune the IGMP and MLD forwarding and burst rates, edit the `/etc/cumulus/acl/policy.d/00control_plane.rules` file and change `--set-rate` and `--set-burst` in the IGMP and MLD policer lines.

The following command example changes the **IGMP** forwarding rate to 400 packets per second and the burst rate to 200 packets.

```
-A $INGRESS_CHAIN -p igmp -j POLICE --set-mode pkt --set-rate 400 --set-burst 200
```

For **MLD**, you need to change several lines in the `/etc/cumulus/acl/policy.d/00control_plane.rules` file.

{{%notice note%}}
All the MLD packet types use same policer internally; you must set all the lines with the same rates.
{{%/notice%}}

The following command examples change the MLD forwarding rate to 400 packets per second and the burst rate to 200 packets.

```
# link-local multicast receiver: Listener Query
-A $INGRESS_CHAIN --in-interface $INGRESS_INTF -p ipv6-icmp -m icmp6 --icmpv6-type 130 -j POLICE --set-mode pkt --set-rate 400 --set-burst 200 --set-class 6

# link-local multicast receiver: Listener Report
-A $INGRESS_CHAIN --in-interface $INGRESS_INTF -p ipv6-icmp -m icmp6 --icmpv6-type 131 -j POLICE --set-mode pkt --set-rate 400 --set-burst 200 --set-class 6

# link-local multicast receiver: Listener Done
-A $INGRESS_CHAIN --in-interface $INGRESS_INTF -p ipv6-icmp -m icmp6 --icmpv6-type 132 -j POLICE --set-mode pkt --set-rate 400 --set-burst 200 --set-class 6

# link-local multicast receiver: Listener Report v2
-A $INGRESS_CHAIN --in-interface $INGRESS_INTF -p ipv6-icmp -m icmp6 --icmpv6-type 143 -j POLICE --set-mode pkt --set-rate 400 --set-burst 200 --set-class 6
```

Apply the rules with the `sudo cl-acltool -i` command:

```
cumulus@switch:~$ sudo cl-acltool -i
```

## Change the Bridge IGMP Version

You can configure a bridge to use IGMPv2 or IGMPv3. IGMPv2 is the default version. To change the IGMP version, add the `bridge-igmp-version <version>` parameter to the bridge stanza in the `/etc/network/interfaces` file. For example, to change the IGMP version to IGMPv3:

```
cumulus@switch:~$ sudo nano /etc/network/interfaces
...
auto br_default
iface br_default
    bridge-ports swp3
    hwaddress 44:38:39:22:01:bb
    bridge-vlan-aware yes
    bridge-vids 1
    bridge-pvid 1
    bridge-igmp-version 3
```

## Disable IGMP and MLD Snooping

If you do not use mirroring functions or other types of multicast traffic, you can disable IGMP and MLD snooping.

{{< tabs "TabID114 ">}}
{{< tab "NCLU Commands ">}}

```
cumulus@switch:~$ net add bridge bridge mcsnoop no
cumulus@switch:~$ net pending
cumulus@switch:~$ net commit
```

{{< /tab >}}
{{< tab "NVUE Commands ">}}

```
cumulus@switch:~$ nv set bridge domain br_default multicast snooping enable off
cumulus@switch:~$ nv config apply
```

{{< /tab >}}
{{< tab "Linux Commands ">}}

Edit the `/etc/network/interfaces` file and set `bridge-mcsnoop to 0` in the bridge stanza:

```
cumulus@switch:~$ sudo nano /etc/network/interfaces
...
auto bridge
iface bridge
  bridge-mcquerier 1
  bridge-mcsnoop 0
  bridge-ports swp1 swp2 swp3
  bridge-pvid 1
  bridge-vids 100 200
  bridge-vlan-aware yes
...
```

Run the `ifreload -a` command to reload the configuration:

```
cumulus@switch:~$ sudo ifreload -a
```

{{< /tab >}}
{{< /tabs >}}

## Troubleshooting

To show the IGMP/MLD snooping bridge state, run the `brctl showstp <bridge>` command:

```
cumulus@switch:~$ sudo brctl showstp bridge
  bridge
  bridge id              8000.7072cf8c272c
  designated root        8000.7072cf8c272c
  root port                 0                    path cost                  0
  max age                  20.00                 bridge max age            20.00
  hello time                2.00                 bridge hello time          2.00
  forward delay            15.00                 bridge forward delay      15.00
  ageing time             300.00
  hello timer               0.00                 tcn timer                  0.00
  topology change timer     0.00                 gc timer                 263.70
  hash elasticity        4096                    hash max                4096
  mc last member count      2                    mc init query count        2
  mc router                 1                    mc snooping                1
  mc last member timer      1.00                 mc membership timer      260.00
  mc querier timer        255.00                 mc query interval        125.00
  mc response interval     10.00                 mc init query interval    31.25
  mc querier                0                    mc query ifaddr            0
  flags

swp1 (1)
  port id                8001                    state                forwarding
  designated root        8000.7072cf8c272c       path cost                  2
  designated bridge      8000.7072cf8c272c       message age timer          0.00
  designated port        8001                    forward delay timer        0.00
  designated cost           0                    hold timer                 0.00
  mc router                 1                    mc fast leave              0
  flags

swp2 (2)
  port id                8002                    state                forwarding
  designated root        8000.7072cf8c272c       path cost                  2
  designated bridge      8000.7072cf8c272c       message age timer          0.00
  designated port        8002                    forward delay timer        0.00
  designated cost           0                    hold timer                 0.00
  mc router                 1                    mc fast leave              0
  flags

swp3 (3)
  port id                8003                    state                forwarding
  designated root        8000.7072cf8c272c       path cost                  2
  designated bridge      8000.7072cf8c272c       message age timer          0.00
  designated port        8003                    forward delay timer        8.98
  designated cost           0                    hold timer                 0.00
  mc router                 1                    mc fast leave              0
  flags
```

Cumulus Linux tracks multicast group and port state in the multicast database (MDB). To show the groups and bridge port state, run the NCLU `net show bridge mdb` command or the Linux `sudo bridge mdb show` command. To show detailed router ports and group information, run the `sudo bridge -d -s mdb show` command:

```
cumulus@switch:~$ sudo bridge -d -s mdb show
  dev bridge port swp2 grp 234.10.10.10 temp 241.67
  dev bridge port swp1 grp 238.39.20.86 permanent 0.00
  dev bridge port swp1 grp 234.1.1.1 temp 235.43
  dev bridge port swp2 grp ff1a::9 permanent 0.00
  router ports on bridge: swp3
```

## Scale Considerations

The number of unique multicast groups supported in the mdb is 4096 by default. To increase the number of maximum number of multicast groups in the mdb, edit the `/etc/network/interfaces` file to add a `bridge-hashmax` value to the bridge stanza:

```
auto br_default
iface br_default
  bridge-hashmax 16384
  bridge-ports swp1 swp2 swp3
  bridge-vlan-aware yes
  bridge-vids 10 20
  bridge-pvid 1
  bridge-mcquerier 1
  bridge-mcsnoop 1
```

The supported values for `bridge-hashmax` are 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536.

{{%notice note%}}
- Spectrum 1 switches limit multicast groups to 16300 in the MDB with OMF disabled and 14800 multicast groups with OMF enabled.
- On Spectrum 1 switches, to support this uppper limit you must change the {{<link url="Supported-Route-Table-Entries/#forwarding-resource-profiles" text="forwarding resource profile">}} to `rash-custom-profile1`, then restart `switchd`.
{{%/notice%}}

## DIP-based Multicast Forwarding

Cumulus Linux does not support DIP-based multicast forwarding. Do not configure the 224.0.0.x through 239.0.0.x and 224.128.0.x through 239.128.0.x IP ranges as multicast groups, which map to link-local MAC addresses (01:00:5e:00:00:xx).

## Related Information

- {{<exlink url="http://en.wikipedia.org/wiki/IGMP_snooping" text="Wikipedia entry for IGMP snooping">}}
- {{<exlink url="http://tools.ietf.org/rfc/rfc2236.txt" text="RFC 2236">}}
- {{<exlink url="http://tools.ietf.org/html/rfc3376" text="RFC 3376">}}
- {{<exlink url="http://tools.ietf.org/html/rfc3810" text="RFC 3810">}}
- {{<exlink url="https://tools.ietf.org/html/rfc4541" text="RFC 4541">}}
