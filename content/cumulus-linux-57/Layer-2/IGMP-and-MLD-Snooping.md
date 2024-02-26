---
title: IGMP and MLD Snooping
author: NVIDIA
weight: 520
toc: 3
---
<span class="a-tooltip">[IGMP](## "Internet Group Management Protocol")</span> and <span class="a-tooltip">[MLD](## "Multicast Listener Discovery")</span> snooping prevent hosts on a local network from receiving traffic for a multicast group they have not explicitly joined. IGMP snooping is for IPv4 environments and MLD snooping is for IPv6 environments.

The bridge driver in Cumulus Linux kernel includes IGMP and MLD snooping. If you disable IGMP or MLD snooping, multicast traffic floods to all the bridge ports in the bridge. Similarly, in the absence of receivers in a VLAN, multicast traffic floods to all ports in the VLAN.

{{< img src = "/images/cumulus-linux/igmp_snoop_diagram.png" >}}

## Configure the IGMP and MLD Querier

Without a multicast router, a single switch in an IP subnet can coordinate multicast traffic flows. This switch is the querier or the designated router. The querier generates query messages to check group membership, and processes membership reports and leave messages.

To configure the querier on the switch for a {{<link url="VLAN-aware-Bridge-Mode" text="VLAN-aware bridge">}}, enable the multicast querier on the bridge and add the source IP address of the queries to the VLAN.

The following configuration example enables the multicast querier and sets source IP address of the queries to 10.10.10.1 (the loopback address of the switch).

{{< tabs "TabID22 ">}}
{{< tab "NVUE Commands ">}}

```
cumulus@switch:~$ nv set bridge domain br_default multicast snooping querier enable on
cumulus@switch:~$ nv set bridge domain br_default vlan 10 multicast snooping querier source-ip 10.10.10.1
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

IGMP snooping restricts multicast forwarding only to the ports that receive IGMP report messages. If the ports do not receive IGMP reports, multicast traffic floods to all ports in the bridge domain (also known as unregistered multicast (URMC) traffic). To restrict this flooding to only mrouter ports, you can enable OMF.

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

{{< tabs "TabID127 ">}}
{{< tab "NVUE Commands ">}}

Cumulus Linux does not provide NVUE commands for this setting.

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

For large multicast environments, the default <span class="a-tooltip">[CoPP](## "Control Plane Policing")</span> policer might be too restrictive. You can adjust the policer to improve multicast convergence.

- For IGMP, both the default forwarding rate and the default burst rate are set to 1000 packets per second.
- For MLD, the default forwarding rate is set to 300 packets per second and the default burst rate is set to 100 packets per second.

To tune the IGMP and MLD forwarding and burst rates:

{{< tabs "174 ">}}
{{< tab "NVUE Commands ">}}

The following example commands set the IGMP forwarding rate to 400 and the IGMP burst rate to 200 packets per second:

```
cumulus@switch:~$ nv set system control-plane policer igmp rate 400
cumulus@switch:~$ nv set system control-plane policer igmp burst 200
cumulus@switch:~$ nv config apply
```

{{< /tab >}}
{{< tab "Edit /etc/cumulus/control-plane/policers.conf ">}}

1. Edit the `/etc/cumulus/control-plane/policers.conf` file. 

   - For IGMP, change the `copp.igmp.rate` and `copp.igmp.burst` parameters.
   - For MLD, change the `copp.icmp6_def_mld.rate` and `copp.icmp6_def_mld.burst` parameters.

   The following example changes the IGMP and MLD forwarding rate to 400 packets per second and the burst rate to 200 packets per second:

   ```
   cumulus@switch:~$ sudo nano /etc/cumulus/control-plane/policers.conf
   ...
   copp.igmp.enable = TRUE
   copp.igmp.rate = 400
   copp.igmp.burst = 200
   ...
   copp.icmp6_def_mld.enable = TRUE
   copp.icmp6_def_mld.rate = 400
   copp.icmp6_def_mld.burst = 200
   ...
   ```

2. Run the following command:

   ```
   cumulus@switch:~$ /usr/lib/cumulus/switchdctl --load /etc/cumulus/control-plane/policers.conf
   ```

{{< /tab >}}
{{< /tabs >}}

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

NVUE does not provide a command to change the bridge IGMP version.

## Disable IGMP and MLD Snooping

If you do not use mirroring functions or other types of multicast traffic, you can disable IGMP and MLD snooping.

{{< tabs "TabID209 ">}}
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

To show the IGMP and MLD snooping bridge state, run the `brctl showstp <bridge>` command:

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

Cumulus Linux tracks multicast group and port state in the <span class="a-tooltip">[MDB](## "multicast database")</span>. To show the groups and bridge port state, run the Linux `sudo bridge mdb show` command. To show detailed router ports and group information, run the `sudo bridge -d -s mdb show` command:

```
cumulus@switch:~$ sudo bridge -d -s mdb show
  dev bridge port swp2 grp 234.10.10.10 temp 241.67
  dev bridge port swp1 grp 238.39.20.86 permanent 0.00
  dev bridge port swp1 grp 234.1.1.1 temp 235.43
  dev bridge port swp2 grp ff1a::9 permanent 0.00
  router ports on bridge: swp3
```

## Scale Considerations

The number of unique multicast groups supported in the MDB is 4096 by default. To increase the maximum number of multicast groups in the MDB, edit the `/etc/network/interfaces` file to add a `bridge-hashmax` value to the bridge stanza:

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
* Spectrum 1 switches limit multicast groups to 16300 in the MDB with OMF disabled and 14800 multicast groups with OMF enabled.
* On Spectrum 1 switches, to support this uppper limit you must change the {{<link title="Forwarding Table Size and Profiles" text="forwarding resource profile">}} to `rash-custom-profile1`, then restart `switchd`.
{{%/notice%}}
<!-- vale off -->
## DIP-based Multicast Forwarding
<!-- vale on -->
Cumulus Linux does not support DIP-based multicast forwarding. Do not configure the 224.0.0.x through 239.0.0.x and 224.128.0.x through 239.128.0.x IP ranges as multicast groups, which map to link-local MAC addresses (01:00:5e:00:00:xx).

## Related Information

- {{<exlink url="http://en.wikipedia.org/wiki/IGMP_snooping" text="Wikipedia entry for IGMP snooping">}}
- {{<exlink url="http://tools.ietf.org/rfc/rfc2236.txt" text="RFC 2236">}}
- {{<exlink url="http://tools.ietf.org/html/rfc3376" text="RFC 3376">}}
- {{<exlink url="http://tools.ietf.org/html/rfc3810" text="RFC 3810">}}
- {{<exlink url="https://tools.ietf.org/html/rfc4541" text="RFC 4541">}}
