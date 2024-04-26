---
title: Equal Cost Multipath Load Sharing - Hardware ECMP
author: NVIDIA
weight: 191
pageID: 8362929
---
Cumulus Linux supports hardware-based {{<exlink url="http://en.wikipedia.org/wiki/Equal-cost_multi-path_routing" text="equal cost multipath">}} (ECMP) load sharing. ECMP is enabled by default in Cumulus Linux. Load sharing occurs automatically for all routes with multiple next hops installed. ECMP load sharing supports both IPv4 and IPv6 routes.

## Equal Cost Routing

ECMP operates only on equal cost routes in the Linux routing table.

In this example, the 10.1.1.0/24 route has two possible next hops that have been installed in the routing table:

```
$ ip route show 10.1.1.0/24
10.1.1.0/24  proto zebra  metric 20
  nexthop via 192.168.1.1 dev swp1 weight 1 onlink
  nexthop via 192.168.2.1 dev swp2 weight 1 onlink
```

For routes to be considered equal they must:

- Originate from the same routing protocol. Routes from different sources are not considered equal. For example, a static route and an OSPF route are not considered for ECMP load sharing.
- Have equal cost. If two routes from the same protocol are unequal, only the best route is installed in the routing table.

{{%notice info%}}

The BGP `maximum-paths` setting is enabled, so multiple routes are installed by default. See {{<link url="Border-Gateway-Protocol-BGP#ecmp-with-bgp" text="ECMP with BGP">}} for more information.

{{%/notice%}}

## ECMP Hashing

After multiple routes are installed in the routing table, a hash is used to determine which path a packet follows.

Cumulus Linux hashes on the following fields:

- IP protocol
- Source IPv4 or IPv6 address
- Destination IPv4 or IPv6 address

On switches with {{<exlink url="www.nvidia.com/en-us/networking/ethernet-switching/hardware-compatibility-list/" text="Spectrum ASICs">}}, Cumulus Linux hashes on these additional fields:

- Source MAC address
- Destination MAC address
- Ethertype
- VLAN ID

For TCP/UDP frames, Cumulus Linux also hashes on:

- Source port
- Destination port

{{< img src = "/images/cumulus-linux/ecmp-packet-hash.png" >}}

To prevent out of order packets, ECMP hashing is done on a per-flow basis, which means that all packets with the same source and destination IP addresses and the same source and destination ports always hash to the same next hop. ECMP hashing does not keep a record of flow states.

ECMP hashing does not keep a record of packets that have hashed to each next hop and does not guarantee that traffic sent to each next hop is equal.

### Use cl-ecmpcalc to Determine the Hash Result

Since the hash is deterministic and always provides the same result for the same input, you can query the hardware and determine the hash result of a given input. This is useful when determining exactly which path a flow takes through a network.

On Cumulus Linux, use the `cl-ecmpcalc` command to determine a hardware hash result.

To use `cl-ecmpcalc`, all fields that are used in the hash must be provided. This includes ingress interface, layer 3 source IP, layer 3 destination IP, layer 4 source port and layer 4 destination port.

```
$ sudo cl-ecmpcalc -i swp1 -s 10.0.0.1 -d 10.0.0.1 -p tcp --sport 20000 --dport 80
ecmpcalc: will query hardware
swp3
```

If any field is omitted, `cl-ecmpcalc` fails.

```
$ sudo cl-ecmpcalc -i swp1 -s 10.0.0.1 -d 10.0.0.1 -p tcp
ecmpcalc: will query hardware
usage: cl-ecmpcalc [-h] [-v] [-p PROTOCOL] [-s SRC] [--sport SPORT] [-d DST]
                   [--dport DPORT] [--vid VID] [-i IN_INTERFACE]
                   [--sportid SPORTID] [--smodid SMODID] [-o OUT_INTERFACE]
                   [--dportid DPORTID] [--dmodid DMODID] [--hardware]
                   [--nohardware] [-hs HASHSEED]
                   [-hf HASHFIELDS [HASHFIELDS ...]]
                   [--hashfunction {crc16-ccitt,crc16-bisync}] [-e EGRESS]
                   [-c MCOUNT]
cl-ecmpcalc: error: --sport and --dport required for TCP and UDP frames
```

### cl-ecmpcalc Limitations

`cl-ecmpcalc` can only take input interfaces that can be converted to a single physical port in the port tab file, like the physical switch ports (swp). Virtual interfaces like bridges, bonds, and subinterfaces are not supported.

`cl-ecmpcalc` is supported only on switches with the Mellanox Spectrum and the Broadcom Maverick, Tomahawk, Trident II, Trident II+ and Trident3 chipsets.

### ECMP Hash Buckets

When multiple routes are installed in the routing table, each route is assigned to an ECMP *bucket*. When the ECMP hash is executed the result of the hash determines which bucket gets used.

In the following example, 4 next hops exist. Three different flows are hashed to different hash buckets. Each next hop is assigned to a unique hash bucket.

{{< img src = "/images/cumulus-linux/ecmp-hash-bucket.png" >}}

#### Add a Next Hop

When a next hop is added, a new hash bucket is created. The assignment of next hops to hash buckets, as well as the hash result, may change when additional next hops are added.

{{< img src = "/images/cumulus-linux/ecmp-hash-bucket-added.png" >}}

A new next hop is added and a new hash bucket is created. As a result, the hash and hash bucket assignment changed, causing the existing flows to be sent to different next hops.

#### Remove a Next Hop

When a next hop is removed, the remaining hash bucket assignments may change, again, potentially changing the next hop selected for an existing flow.

{{< img src = "/images/cumulus-linux/ecmp-hash-failure.png" >}}

{{< img src = "/images/cumulus-linux/ecmp-hash-post-failure.png" >}}

A next hop fails and the next hop and hash bucket are removed. The remaining next hops may be reassigned.

In most cases, the modification of hash buckets has no impact on traffic flows as traffic is being forward to a single end host. In deployments where multiple end hosts are using the same IP address (anycast), *resilient hashing* must be used.

### Configure a Hash Seed to Avoid Hash Polarization

It is useful to have a unique hash seed for each switch. This helps avoid *hash polarization*, a type of network congestion that occurs when multiple data flows try to reach a switch using the same switch ports.

{{%notice info%}}

Starting in Cumulus Linux 3.5.4, if the `ecmp_hash_seed` value is not set in `/etc/cumulus/datapath/traffic.conf` (the default as shipped), switchd will use a randomly generated seed, which is stable across switchd restarts and reboots.

{{%/notice%}}

The hash seed is set by the `ecmp_hash_seed` parameter in the `/etc/cumulus/datapath/traffic.conf` file. It is an integer with a value from 0 to 4294967295. If you don't specify a value for it, `switchd` creates a randomly generated seed instead.

To set the hash seed to *50* for example, run the following commands:

```
cumulus@switch:~$ net add forwarding ecmp hash-seed 50
cumulus@switch:~$ net pending
cumulus@switch:~$ net commit
```

These commands create the following configuration in the `/etc/cumulus/datapath/traffic.conf` file:

```
cumulus@leaf01:~$ cat /etc/cumulus/datapath/traffic.conf
...

#Specify the hash seed for Equal cost multipath entries
ecmp_hash_seed = 50

...
cumulus@leaf01:~$
```

### ECMP Custom Hashing

{{%notice note%}}

Custom hashing is supported on Mellanox switches.

{{%/notice%}}

In Cumulus Linux 3.7.11 and later, you can configure the set of fields used to hash upon during ECMP load balancing. For example, if you do not want to use source or destination port numbers in the hash calculation, you can disable the source port and destination port fields.

You can enable/disable the following fields:

- IP Protocol
- Source IP
- Destination IP
- Source port
- Destination port
- IPv6 flow label
- Ingress interface

You can also enable/disable these Inner header fields:

- Inner IP protocol
- Inner source IP
- Inner destination IP
- Inner source port
- Inner destination port
- Inner IPv6 flow label

To configure custom hashing, edit the `/usr/lib/python2.7/dist-packages/cumulus/__chip_config/mlx/datapath.conf` file:

1. To enable custom hashing, uncomment the `hash_config.enable = true` line.
2. To enable a field, set the field to `true`. To disable a field, set the field to `false`.
3. Restart the `switchd` service:

   {{<cl/restart-switchd>}}

The following shows an example `datapath.conf` file:

```
cumulus@switch:~$ sudo nano /usr/lib/python2.7/dist-packages/cumulus/__chip_config/mlx/datapath.conf
...
# HASH config for ECMP to enable custom fields
# Fields will be applicable for ECMP hash
# calculation
#Note: Hash seed can be configured in traffic.conf
#/etc/cumulus/datapath/traffic.conf
#
# Uncomment to enable custom fields configured below
hash_config.enable = true

#symmetric hash will get disabled
#if sip/dip or sport/dport are not enabled in pair
#hash Fields available ( assign true to enable)
#ip protocol
hash_config.ip_prot = true
#source ip
hash_config.sip = true
#destination ip
hash_config.dip = true
#source port
hash_config.sport = false
#destination port
hash_config.dport = false
#ipv6 flow label
hash_config.ip6_label = true
#ingress interface
hash_config.ing_intf = false

#inner fields for  IPv4-over-IPv6 and IPv6-over-IPv6
hash_config.inner_ip_prot = false
hash_config.inner_sip = false
hash_config.inner_dip = false
hash_config.inner_sport = false
hash_config.inner_dport = false
hash_config.inner_ip6_label = false
# Hash config end #
...
```

{{%notice note%}}

Symmetric hashing is enabled by default on Mellanox switches running Cumulus Linux 3.7.11 and later. Make sure that the settings for the source IP (`hash_config.sip`) and destination IP (`hash_config.dip`) fields match, and that the settings for the source port (`hash_config.sport`) and destination port (`hash_config.dport`) fields match; otherwise symmetric hashing is disabled automatically. You can disable symmetric hashing manually in the `/etc/cumulus/datapath/traffic.conf` file by setting `symmetric_hash_enable = FALSE`.

{{%/notice%}}

## Resilient Hashing

In Cumulus Linux, when a next hop fails or is removed from an ECMP pool, the hashing or hash bucket assignment can change. For deployments where there is a need for flows to always use the same next hop, like TCP anycast deployments, this can create session failures.

*Resilient hashing* is an alternate mechanism for managing ECMP groups. The ECMP hash performed with resilient hashing is exactly the same as the default hashing mode. Only the method in which next hops are assigned to hash buckets differs &mdash; they're assigned to buckets by hashing their header fields and using the resulting hash to index into the table of 2^n hash buckets. Since all packets in a given flow have the same header hash value, they all use the same flow bucket.

Resilient hashing supports both IPv4 and IPv6 routes.

Resilient hashing behaves slightly differently depending upon whether you are running Cumulus Linux on a switch with a {{<link url="#resilient-hashing-on-broadcom-switches" text="Broadcom ASIC">}} or {{<link url="#resilient-hashing-on-mellanox-switches" text="Mellanox ASIC">}}. The differences are described below.

Resilient hashing is not enabled by default. See below for {{<link url="#configure-resilient-hashing" text="steps on configuring it">}}.

### Resilient Hashing on Broadcom Switches

Resilient hashing is supported only on switches with the Broadcom Tomahawk, Trident II, Trident II+, and Trident3 ASICs. You can run `net show system` to determine the ASIC.

The Broadcom ASIC assigns packets to hash buckets and assigns hash buckets to next hops as follows:

- When a next hop is removed, the assigned buckets are distributed to the remaining next hops.
- When a next hop is added, **some** buckets assigned to other next hops are migrated to the new next hop.
- The algorithm assigns buckets to next hops so as to make the number of buckets per next hop as close to equal as possible.
- The assignment of buckets to next hops is not changed in any other case. In particular, this assignment is not changed due to traffic loading or imbalance.
- Next hops are assigned to buckets randomly, to minimize the chance of systemic imbalance.

### Resilient Hashing on Mellanox Switches

A Mellanox switch has two unique options for configuring resilient hashing, both of which you configure in the `/usr/lib/python2.7/dist-packages/cumulus/__chip_config/mlx/datapath.conf​` file. The recommended values for these options depend largely on the desired outcome for a specific network implementation &mdash; the number and duration of flows, and the importance of keeping these flows pinned without interruption.

- `resilient_hash_active_timer`: A timer that protects TCP sessions from being
  disrupted while attempting to populate new next hops. You specify the number of
  seconds when at least one hash bucket consistently sees no traffic before
  Cumulus Linux rebalances the flows; the default is 120 seconds. If any
  one bucket is idle; that is, it sees no traffic for the defined period, the next
  new flow utilizes that bucket and flows to the new link. Thus, if the network is
  experiencing a large number of flows or very consistent or persistent flows, there
  may not be any buckets remaining idle for a consistent 120 second period, and the
  imbalance remains until that timer has been met. If a new link is brought up and
  added back to a group during this time, traffic does not get allocated to utilize
  it until a bucket qualifies as *empty*, meaning it has been idle for 120 seconds.
  This is when a rebalance can occur.
- `resilient_hash_max_unbalanced_timer`: You can force a rebalance every N seconds
  with this option. However, while this could correct the persistent imbalance that
  is expected with resilient hashing, this rebalance would result in the movement of
  all flows and thus a break in any TCP sessions that are active at that time.

Note that when you configure these options, a new next hop may not get populated for a long time.

The Mellanox Spectrum ASIC assigns packets to hash buckets and assigns hash buckets to next hops as follows. It also runs a background thread that monitors and may migrate buckets between next hops to rebalance the load.

- When a next hop is removed, the assigned buckets are distributed to the remaining next hops.
- When a next hop is added, **no** buckets are assigned to the new next hop until the background thread rebalances the load.
- The load gets rebalanced when the active flow timer specified by the `resilient_hash_active_timer` setting expires if, and only if, there are inactive hash buckets available; the new next hop may remain unpopulated until the period set in `resilient_hash_active_timer` expires
- When the `resilient_hash_max_unbalanced_timer` setting expires and the load is not balanced, the thread migrates any bucket(s) to different next hops to rebalance the load.

As a result, any flow may be migrated to any next hop, depending on flow activity and load balance conditions; over time, the flow may get pinned, which is the default setting and behavior.

### Resilient Hash Buckets

When resilient hashing is configured, a fixed number of buckets are defined. Next hops are then assigned in round robin fashion to each of those buckets. In this example, 12 buckets are created and four next hops are assigned.

{{< img src = "/images/cumulus-linux/ecmp-reshash-bucket-assignment.png" >}}

### Remove Next Hops

Unlike default ECMP hashing, when a next hop needs to be removed, the number of hash buckets does not change.

{{< img src = "/images/cumulus-linux/ecmp-reshash-failure.png" >}}

With 12 buckets assigned and four next hops, instead of reducing the number of buckets &mdash; which would impact flows to known good hosts &mdash; the remaining next hops replace the failed next hop.

{{< img src = "/images/cumulus-linux/ecmp-reshash-restore.png" >}}

After the failed next hop is removed, the remaining next hops are installed as replacements. This prevents impact to any flows that hash to working next hops.

### Add Next Hops

Resilient hashing does not prevent possible impact to existing flows when new next hops are added. Due to the fact there are a fixed number of buckets, a new next hop requires reassigning next hops to buckets.

{{< img src = "/images/cumulus-linux/ecmp-reshash-add.png" >}}

As a result, some flows may hash to new next hops, which can impact anycast deployments.

### Configure Resilient Hashing

Resilient hashing is not enabled by default. When resilient hashing is enabled, 65,536 buckets are created to be shared among all ECMP groups. An ECMP group is a list of unique next hops that are referenced by multiple ECMP routes.

An ECMP route counts as a single route with multiple next hops. The following example is considered to be a single ECMP route:

```
$ ip route show 10.1.1.0/24
10.1.1.0/24  proto zebra  metric 20
    nexthop via 192.168.1.1 dev swp1 weight 1 onlink
    nexthop via 192.168.2.1 dev swp2 weight 1 onlink
```

All ECMP routes must use the same number of buckets (the number of buckets cannot be configured per ECMP route).

The number of buckets can be configured as 64, 128, 256, 512 or 1024; the default is 128:

| Number of Hash Buckets | Number of Supported ECMP Groups |
| ---------------------- | ------------------------------- |
| 64                     | 1024                            |
| **128**                | **512**                         |
| 256                    | 256                             |
| 512                    | 128                             |
| 1024                   | 64                              |

{{%notice note%}}

Mellanox switches with the Spectrum ASIC do not support 128 or 256 hash buckets. The default number of hash buckets is 64.

{{%/notice%}}

A larger number of ECMP buckets reduces the impact on adding new next hops to an ECMP route. However, the system supports fewer ECMP routes. If the maximum number of ECMP routes have been installed, new ECMP routes log an error and are not installed.

To enable resilient hashing, edit `/etc/cumulus/datapath/traffic.conf`:

1. Enable resilient hashing:

       # Enable resilient hashing
       resilient_hash_enable = TRUE

1. **(Optional)** Edit the number of hash buckets:

       # Resilient hashing flowset entries per ECMP group
       # Valid values - 64, 128, 256, 512, 1024
       resilient_hash_entries_ecmp = 256

1. **(Optional)** On {{<link url="#resilient-hashing-on-mellanox-switches" text="Mellanox switches">}},
  configure timers in `/usr/lib/python2.7/dist-packages/cumulus/__chip_config/mlx/datapath.conf​`
  file.

1. Restart the `switchd` service:

   {{<cl/restart-switchd>}}

## Caveats and Errata

### IPv6 Route Replacement

When the next hop information for an IPv6 prefix changes (for example, when ECMP paths are added or deleted, or when the next hop IP address, interface, or tunnel changes), FRR deletes the existing route to that prefix from the kernel and then adds a new route with all the relevant new information. Because of this process, resilient hashing might not be maintained for IPv6 flows in certain situations.

To work around this issue in Cumulus Linux 3.7.12 and later, you can enable the IPv6 route replacement option.

{{%notice info%}}

Be aware that for certain configurations, the IPv6 route replacement option can lead to incorrect forwarding decisions and lost traffic. For example, it is possible for a destination to have next hops with a gateway value with the outbound interface or just the outbound interface itself, without a gateway address defined. If both types of next hops for the same destination exist, route replacement does not operate correctly; Cumulus Linux adds an additional route entry and next hop but does not delete the previous route entry and next hop.

{{%/notice%}}

To enable the IPv6 route replacement option:

1. In the `/etc/frr/daemons.conf` file, add the configuration option `--v6-rr-semantics` to the zebra daemon definition. For example:

```
cumulus@switch:~$ sudo nano /etc/frr/daemons.conf
...
vtysh_enable=yes
zebra_options=" -M snmp -s 90000000 --v6-rr-semantics --daemon -A 127.0.0.1"
bgpd_options=" -M snmp --daemon -A 127.0.0.1"
ospfd_options=" -M snmp --daemon -A 127.0.0.1"
...
```

2. {{<cl/restart-frr>}}

To verify that the IPv6 route replacement option is enabled, run the `systemctl status frr` command:

```
cumulus@switch:~$ systemctl status frr

● frr.service - FRRouting
   Loaded: loaded (/lib/systemd/system/frr.service; enabled; vendor preset: enabled)
   Active: active (running) since Mon 2020-02-03 20:02:33 UTC; 3min 8s ago
     Docs: https://frrouting.readthedocs.io/en/latest/setup.html
  Process: 4675 ExecStart=/usr/lib/frr/frrinit.sh start (code=exited, status=0/SUCCESS)
   Memory: 14.4M
   CGroup: /system.slice/frr.service
           ├─4685 /usr/lib/frr/watchfrr -d zebra bgpd staticd
           ├─4701 /usr/lib/frr/zebra -d -M snmp -A 127.0.0.1 --v6-rr-semantics -s 90000000
           ├─4705 /usr/lib/frr/bgpd -d -M snmp -A 127.0.0.1
           └─4711 /usr/lib/frr/staticd -d -A 127.0.0.1
```
