---
title: Equal Cost Multipath Load Sharing - Hardware ECMP
author: Cumulus Networks
weight: 840
aliases:
 - /display/DOCS/Equal+Cost+Multipath+Load+Sharing+++Hardware+ECMP
 - /display/DOCS/Equal+Cost+Multipath+Load+Sharing+Hardware+ECMP
 - /display/DOCS/Equal+Cost+Multipath+Load+Sharing+-+Hardware+ECMP
 - /pages/viewpage.action?pageId=8366653
---
Cumulus Linux supports hardware-based {{<exlink url="http://en.wikipedia.org/wiki/Equal-cost_multi-path_routing" text="equal cost multipath">}} (ECMP) load sharing. ECMP is enabled by default in Cumulus Linux. Load sharing occurs automatically for all routes with multiple next hops installed. ECMP load sharing supports both IPv4 and IPv6 routes.

## Equal Cost Routing

ECMP operates only on equal cost routes in the Linux routing table.

In this example, the 10.1.1.0/24 route has two possible next hops that have been installed in the routing table:

```
cumulus@switch:~$ ip route show 10.1.1.0/24
10.1.1.0/24  proto zebra  metric 20
  nexthop via 192.168.1.1 dev swp1 weight 1 onlink
  nexthop via 192.168.2.1 dev swp2 weight 1 onlink
```

For routes to be considered equal they must:

- Originate from the same routing protocol. Routes from different sources are not considered equal. For example, a static route and an OSPF route are not considered for ECMP load sharing.
- Have equal cost. If two routes from the same protocol are unequal, only the best route is installed in the routing table.

{{%notice info%}}

In Cumulus Linux, the BGP `maximum-paths` setting is enabled, so multiple routes are installed by default. See the {{<link url="Border-Gateway-Protocol-BGP#ecmp-with-bgp" text="ECMP section">}} of the BGP chapter for more information.

{{%/notice%}}

## ECMP Hashing

When multiple routes are installed in the routing table, a hash is used to determine which path a packet follows.

Cumulus Linux hashes on the following fields:

- IP protocol
- Ingress interface
- Source IPv4 or IPv6 address
- Destination IPv4 or IPv6 address

Further, on switches with {{<exlink url="https://cumulusnetworks.com/products/hardware-compatibility-list/?asic%5B0%5D=Mellanox%20Spectrum&asic%5B1%5D=Mellanox%20Spectrum_A1" text="Spectrum ASICs">}}, Cumulus Linux hashes on these additional fields:

- Source MAC address
- Destination MAC address
- Ethertype
- VLAN ID

For TCP/UDP frames, Cumulus Linux also hashes on:

- Source port
- Destination port

{{< img src = "/images/cumulus-linux/ecmp-packet-hash.png" >}}

To prevent out of order packets, ECMP hashing is done on a per-flow basis; all packets with the same source and destination IP addresses and the same source and destination ports always hash to the same next hop. ECMP hashing does not keep a record of flow states.

ECMP hashing does not keep a record of packets that have hashed to each next hop and does not guarantee that traffic sent to each next hop is equal.

### Use cl-ecmpcalc to Determine the Hash Result

Because the hash is deterministic and always provides the same result for the same input, you can query the hardware and determine the hash result of a given input. This is useful when determining exactly which path a flow takes through a network.

On Cumulus Linux, use the `cl-ecmpcalc` command to determine a hardware hash result.

To use `cl-ecmpcalc`, all fields that are used in the hash must be provided. This includes ingress interface, layer 3 source IP, layer 3 destination IP, layer 4 source port, and layer 4 destination port.

```
cumulus@switch:~$ sudo cl-ecmpcalc -i swp1 -s 10.0.0.1 -d 10.0.0.1 -p tcp --sport 20000 --dport 80
ecmpcalc: will query hardware
swp3
```

If any field is omitted, `cl-ecmpcalc` fails.

```
cumulus@switch:~$ sudo cl-ecmpcalc -i swp1 -s 10.0.0.1 -d 10.0.0.1 -p tcp
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

`cl-ecmpcalc` can only take input interfaces that can be converted to a single physical port in the port tab file, such as the physical switch ports (swp). Virtual interfaces like bridges, bonds, and subinterfaces are not supported.

`cl-ecmpcalc` is supported only on switches with the {{<exlink url="https://cumulusnetworks.com/hcl/" text="Mellanox Spectrum and the Broadcom Maverick, Tomahawk, Trident II, Trident II+ and Trident3">}} chipsets.

### ECMP Hash Buckets

When multiple routes are installed in the routing table, each route is assigned to an ECMP *bucket*. When the ECMP hash is executed the result of the hash determines which bucket gets used.

In the following example, four next hops exist. Three different flows are hashed to different hash buckets. Each next hop is assigned to a unique hash bucket.

{{< img src = "/images/cumulus-linux/ecmp-hash-bucket.png" >}}

#### Add a Next Hop

When a next hop is added, a new hash bucket is created. The assignment of next hops to hash buckets, as well as the hash result, might change when additional next hops are added.

{{< img src = "/images/cumulus-linux/ecmp-hash-bucket-added.png" >}}

A new next hop is added and a new hash bucket is created. As a result, the hash and hash bucket assignment changes, causing the existing flows to be sent to different next hops.

#### Remove a Next Hop

When a next hop is removed, the remaining hash bucket assignments might change, again, potentially changing the next hop selected for an existing flow.

{{< img src = "/images/cumulus-linux/ecmp-hash-failure.png" >}}

{{< img src = "/images/cumulus-linux/ecmp-hash-post-failure.png" >}}

A next hop fails and the next hop and hash bucket are removed. The remaining next hops might be reassigned.

In most cases, the modification of hash buckets has no impact on traffic flows as traffic is being forwarded to a single end host. In deployments where multiple end hosts are using the same IP address (anycast), *resilient hashing* must be used.

### Configure a Hash Seed to Avoid Hash Polarization

It is useful to have a unique hash seed for each switch. This helps avoid *hash polarization*, a type of network congestion that occurs when multiple data flows try to reach a switch using the same switch ports.

The hash seed is set by the `ecmp_hash_seed` parameter in the `/etc/cumulus/datapath/traffic.conf` file. It is an integer with a value from 0 to 4294967295. If you do not specify a value, `switchd` creates a randomly generated seed instead.

For example, to set the hash seed to *50*, run the following commands:

<details>

<summary>NCLU Commands </summary>

```
cumulus@switch:~$ net add forwarding ecmp hash-seed 50
cumulus@switch:~$ net pending
cumulus@switch:~$ net commit
```

</details>

<details>

<summary>Linux Commands </summary>

Edit the the `/etc/cumulus/datapath/traffic.conf` file. For example:

```
cumulus@switch:~$ sudo nano /etc/cumulus/datapath/traffic.conf
...
#Specify the hash seed for Equal cost multipath entries
ecmp_hash_seed = 50
...
```

{{<link url="Configuring-switchd#restart-switchd" text="Restart">}} the `switchd` service:

```
cumulus@switch:~$ sudo systemctl restart switchd.service
```

</details>

## Resilient Hashing

In Cumulus Linux, when a next hop fails or is removed from an ECMP pool, the hashing or hash bucket assignment can change. For deployments where there is a need for flows to always use the same next hop, like TCP anycast deployments, this can create session failures.

The ECMP hash performed with resilient hashing is exactly the same as the default hashing mode. Only the method in which next hops are assigned to hash buckets differs.

Resilient hashing supports both IPv4 and IPv6 routes.

{{%notice note%}}

Resilient hashing prevents disruptions when next hops are removed. It does not prevent disruption when next hops are added.

{{%/notice%}}

{{%notice note%}}

Resilient hashing is supported only on switches with the {{<exlink url="https://cumulusnetworks.com/hcl/" text="Broadcom Tomahawk, Trident II, Trident II+, and Trident3 as well as Mellanox Spectrum">}} chipsets. You can run `net show system` to determine the chipset.

{{%/notice%}}

### Resilient Hash Buckets

When resilient hashing is configured, a fixed number of buckets are defined. Next hops are then assigned in round robin fashion to each of those buckets. In this example, 12 buckets are created and four next hops are assigned.

{{< img src = "/images/cumulus-linux/ecmp-reshash-bucket-assignment.png" >}}

### Remove Next Hops

Unlike default ECMP hashing, when a next hop needs to be removed, the number of hash buckets does not change.

{{< img src = "/images/cumulus-linux/ecmp-reshash-failure.png" >}}

With 12 buckets assigned and four next hops, instead of reducing the number of buckets - which would impact flows to known good hosts - the remaining next hops replace the failed next hop.

{{< img src = "/images/cumulus-linux/ecmp-reshash-restore.png" >}}

After the failed next hop is removed, the remaining next hops are installed as replacements. This prevents impact to any flows that hash to working next hops.

### Add Next Hops

Resilient hashing does not prevent possible impact to existing flows when new next hops are added. Due to the fact there are a fixed number of buckets, a new next hop requires reassigning next hops to buckets.

{{< img src = "/images/cumulus-linux/ecmp-reshash-add.png" >}}

As a result, some flows may hash to new next hops, which can impact anycast deployments.

### Configure Resilient Hashing

Resilient hashing is *not* enabled by default. When resilient hashing is enabled, 65,536 buckets are created to be shared among all ECMP groups. An ECMP group is a list of unique next hops that are referenced by multiple ECMP routes.

{{%notice info%}}

An ECMP route counts as a single route with multiple next hops. The following example is considered to be a single ECMP route:

```
cumulus@switch:~$ ip route show 10.1.1.0/24
10.1.1.0/24  proto zebra  metric 20
  nexthop via 192.168.1.1 dev swp1 weight 1 onlink
  nexthop via 192.168.2.1 dev swp2 weight 1 onlink
```

{{%/notice%}}

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

```
# Enable resilient hashing
resilient_hash_enable = TRUE
```

2. **(Optional)** Edit the number of hash buckets:

```
# Resilient hashing flowset entries per ECMP group
# Valid values - 64, 128, 256, 512, 1024
resilient_hash_entries_ecmp = 256
```

3. {{<link url="Configuring-switchd#restart-switchd" text="Restart">}} the `switchd` service:

```
cumulus@switch:~$ sudo systemctl restart switchd.service
```

## Caveats and Errata

### IPv6 Route Replacement

When the next hop information for an IPv6 prefix changes (for example, when ECMP paths are added or deleted, or when the next hop IP address, interface, or tunnel changes), FRR deletes the existing route to that prefix from the kernel and then adds a new route with all the relevant new information. Because of this process, resilient hashing might not be maintained for IPv6 flows in certain situations.

To work around this issue, you can enable the IPv6 route replacement option.

{{%notice info%}}

Be aware that for certain configurations, the IPv6 route replacement option can lead to incorrect forwarding decisions and lost traffic. For example, it is possible for a destination to have next hops with a gateway value with the outbound interface or just the outbound interface itself, without a gateway address defined. If both types of next hops for the same destination exist, route replacement does not operate correctly; Cumulus Linux adds an additional route entry and next hop but does not delete the previous route entry and next hop.

{{%/notice%}}

To enable the IPv6 route replacement option:

1. In the `/etc/frr/daemons` file, add the configuration option `--v6-rr-semantics` to the zebra daemon definition. For example:

```
cumulus@switch:~$ sudo nano /etc/frr/daemons
...
vtysh_enable=yes
zebra_options=" -M snmp -A 127.0.0.1 --v6-rr-semantics -s 90000000"
bgpd_options=" -M snmp  -A 127.0.0.1"
ospfd_options=" -M snmp -A 127.0.0.1"
...
```

2. Restart FRRouting:

```
cumulus@switch:~$ sudo systemctl restart frr.service
```

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
