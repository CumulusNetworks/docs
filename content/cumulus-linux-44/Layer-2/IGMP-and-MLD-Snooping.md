---
title: IGMP and MLD Snooping
author: NVIDIA
weight: 520
toc: 3
---
Internet Group Management Protocol (IGMP) snooping and Multicast Listener Discovery (MLD) snooping prevent hosts on a local network from receiving traffic for a multicast group they have not explicitly joined. IGMP snooping is used for IPv4 environments and MLD snooping is used for IPv6 environments.

IGMP and MLD snooping are implemented in the bridge driver in the Cumulus Linux kernel and are enabled by default. If you disable IGMP or MLD snooping, multicast traffic is flooded to all the bridge ports in the bridge. Similarly, in the absence of receivers in a VLAN, multicast traffic is flooded to all ports in the VLAN.

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

In the absence of a multicast router, a single switch in an IP subnet can coordinate multicast traffic flows. This switch is called the querier or the designated router. The querier generates query messages to check group membership, and processes membership reports and leave messages.

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

IGMP Snooping restricts multicast forwarding only to the ports where IGMP report messages are received. If no IGMP reports are received, multicast traffic is flooded to all ports in the bridge domain (this traffic is known as unregistered multicast (URMC) traffic). To restrict this flooding to only mrouter ports, you can enable OMF.

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

   {{<cl/restart-switchd>}}

When IGMP reports are sent for a multicast group, OMF has no effect; normal IGMP Snooping behavior is followed.

{{%notice note%}}
OMF increases memory usage, which can impact scaling on Spectrum 1 switches.
{{%/notice%}}

## Disable IGMP and MLD Snooping

If you do not use mirroring functions or other types of multicast traffic, you can disable IGMP and MLD Snooping.

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

To show the groups and bridge port state, run the NCLU `net show bridge mdb` command or the Linux `sudo bridge mdb show` command. To show detailed router ports and group information, run the `sudo bridge -d -s mdb show` command:

```
cumulus@switch:~$ sudo bridge -d -s mdb show
  dev bridge port swp2 grp 234.10.10.10 temp 241.67
  dev bridge port swp1 grp 238.39.20.86 permanent 0.00
  dev bridge port swp1 grp 234.1.1.1 temp 235.43
  dev bridge port swp2 grp ff1a::9 permanent 0.00
  router ports on bridge: swp3
```

## Related Information

- {{<exlink url="http://en.wikipedia.org/wiki/IGMP_snooping" text="Wikipedia entry for IGMP snooping">}}
- {{<exlink url="http://tools.ietf.org/rfc/rfc2236.txt" text="RFC 2236">}}
- {{<exlink url="http://tools.ietf.org/search/rfc2710" text="RFC 2710">}}
- {{<exlink url="http://tools.ietf.org/html/rfc3376" text="RFC 3376">}}
- {{<exlink url="http://tools.ietf.org/html/rfc3810" text="RFC 3810">}}
- {{<exlink url="https://tools.ietf.org/html/rfc4541" text="RFC 4541">}}
