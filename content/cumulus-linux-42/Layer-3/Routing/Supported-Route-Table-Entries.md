---
title: Supported Route Table Entries
author: NVIDIA
weight: 740
toc: 3
---
Cumulus Linux advertises the maximum number of route table entries supported on a given platform, including:

- Layer 3 IPv4 LPM (longest prefix match) entries that have a mask less than /32
- Layer 3 IPv6 LPM entries that have a mask of /64 or less
- Layer 3 IPv6 LPM entries that have a mask greater than /64
- Layer 3 IPv4 neighbor (or host) entries that are the next hops seen in `ip neighbor`
- Layer 3 IPv6 neighbor entries that are the next hops seen in `ip -6 neighbor`
- ECMP next hops, which are IP address entries in a router's routing table that specify the next closest or most optimal router in its routing path
- MAC addresses

In addition, Tomahawk, Trident II, Trident II+, and Trident3 switches are configured to manage route table entries using Algorithm Longest Prefix Match (ALPM). In ALPM mode, the hardware can store significantly more route entries.

To determine the current table sizes on a switch, use either the NCLU `net show system asic` command or `{{<link url="Resource-Diagnostics-Using-cl-resource-query" text="cl-resource-query">}}`.

## Forwarding Table Profiles

On Mellanox Spectrum and some Broadcom ASICs, you can configure the allocation of forwarding table resources and mechanisms. Cumulus Linux provides a number of generalized profiles for the platforms described below. These profiles work only with layer 2 and layer 3 unicast forwarding.

Choose the profile that best suits your network architecture and specify the profile name for the `forwarding_table.profile` variable in the `/etc/cumulus/datapath/traffic.conf` file; for example:

```
cumulus@switch:~$ cat /etc/cumulus/datapath/traffic.conf | grep forwarding_table -B 4
# Manage shared forwarding table allocations
# Valid profiles -
# default, l2-heavy, v4-lpm-heavy, v6-lpm-heavy
#
forwarding_table.profile = default
```

After you specify a different profile, {{%link url="Configuring-switchd#restart-switchd" text="restart `switchd`"%}} for the change to take effect. You can see the forwarding table profile when you run `cl-resource-query`.

{{%notice note%}}

- Broadcom ASICs other than Maverick, Tomahawk/Tomahawk+, Trident II, Trident II+, and Trident3 support only the *default* profile.
- For Broadcom ASICs, the maximum number of IP multicast entries is 8k.

{{%/notice%}}

## Supported Route Entries

The following tables list the number of MAC addresses, layer 3 neighbors, and LPM routes validated for each forwarding table profile for supported platforms. If you do not specify any profiles as described above, the switch uses the *default* values.

{{%notice tip%}}

The values in the following tables reflect results from testing on supported platforms, which might differ from published manufacturer specifications.

{{%/notice%}}

### Mellanox Spectrum Switches

| <div style="width:100px">Profile| MAC Addresses | <div style="width:190px">L3 Neighbors| Longest Prefix Match (LPM)  |
| -------------- | ------------- | ------------------------- | ------------------------------ |
| default        | 40k           | 32k (IPv4) and 16k (IPv6) | 64k (IPv4) and 28k (IPv6-long) |
| l2-heavy       | 88k           | 48k (IPv4) and 40k (IPv6) | 8k (IPv4) and 8k (IPv6-long)   |
| l2-heavy-1     | 180K          | 8k (IPv4) and 8k (IPv6)   | 8k (IPv4) and 8k (IPv6-long)   |
| v4-lpm-heavy   | 8k            | 8k (IPv4) and 16k (IPv6)  | 80k (IPv4) and 16k (IPv6-long) |
| v4-lpm-heavy-1 | 8k            | 8k (IPv4) and 2k (IPv6)   | 176k (IPv4) and 2k (IPv6-long) |
| v6-lpm-heavy   | 40k           | 8k (IPv4) and 40k (IPv6)  | 8k (IPv4) and 32k (IPv6-long) and 32K (IPv6/64) |
| lpm-balanced   | 8k            | 8k (IPv4) and 8k (IPv6)   | 60k (IPv4) and 60k (IPv6-long) |

### Broadcom Tomahawk/Tomahawk+ Switches

| Profile                    | MAC Addresses | L3 Neighbors | Longest Prefix Match (LPM)     |
| -------------------------- | ------------- | ------------ | ------------------------------ |
| default                    | 40k           | 40k          | 64k (IPv4) or 8k (IPv6-long)   |
| l2-heavy                   | 72k           | 72k          | 8k (IPv4) or 2k (IPv6-long)    |
| v4-lpm-heavy<br>v6-lpm-heavy | 8k            | 8k           | 128k (IPv4) or 20k (IPv6-long) |

### Broadcom Trident II/Trident II+/Trident3 Switches

| Profile                      | MAC Addresses | L3 Neighbors | Longest Prefix Match (LPM)     |
| --------------------------   | ------------- | ------------ | ------------------------------ |
| default                      | 32k           | 16k          | 128k (IPv4) or 20k (IPv6-long) |
| l2-heavy                     | 160k          | 96k          | 8k (IPv4) or 2k (IPv6-long)    |
| v4-lpm-heavy<br>v6-lpm-heavy | 32k           | 16k          | 128k (IPv4) or 20k (IPv6-long) |

### Broadcom Helix4 Switches

Helix4 switches do *not* have profiles.

| MAC Addresses | L3 Neighbors | Longest Prefix Match (LPM)    |
| ------------- | ------------ | ----------------------------- |
| 24k           | 12k          | 7.8k (IPv4) or 2k (IPv6-long) |

{{%notice note%}}

For Broadcom switches, IPv4 and IPv6 entries are not carved in separate spaces so it is not possible to define explicit numbers in the L3 Neighbors column of the tables above. An IPv6 entry takes up twice the space of an IPv4 entry.

{{%/notice%}}

## TCAM Resource Profiles for Spectrum Switches

On the Mellanox Spectrum ASIC, you can configure TCAM resource allocation, which is shared between IP multicast forwarding entries and ACL tables. Cumulus Linux provides a number of general profiles for this platform. Choose the profile that best suits your network architecture and specify that profile name in the `tcam_resource.profile` variable in the `/usr/lib/python2.7/dist-packages/cumulus/__chip_config/mlx/datapath.conf` file; for example:

```
cumulus@switch:~$ cat /usr/lib/python2.7/dist-packages/cumulus/__chip_config/mlx/datapath.conf | grep -B3 "tcam_resource"
#TCAM resource forwarding profile

    1. Valid profiles -
    2. default, ipmc-heavy, acl-heavy, ipmc-max
       tcam_resource.profile = default
```

After you specify a different profile, {{%link url="Configuring-switchd#restart-switchd" text="restart `switchd`"%}} for the change to take effect.

When {{<link url="Netfilter-ACLs#nonatomic-update-mode-and-atomic-update-mode" text="nonatomic updates">}} are enabled (`acl.non_atomic_update_mode` is set to `TRUE` in the `/etc/cumulus/switchd.conf` file), the maximum number of mroute and ACL entries for each profile are:

| Profile    | Mroute Entries | ACL Entries                |
| ---------- | -------------- | -------------------------- |
| default    | 1000           | 500 (IPv6) or 1000 (IPv4)  |
| ipmc-heavy | 8500           | 1000 (IPv6) or 1500 (IPv4) |
| acl-heavy  | 450            | 2000 (IPv6) or 3500 (IPv4) |
| ipmc-max   | 13000          | 1000 (IPv6) or 2000 (IPv4) |

When {{<link url="Netfilter-ACLs#nonatomic-update-mode-and-atomic-update-mode" text="nonatomic updates">}} are disabled (`acl.non_atomic_update_mode` is set to `FALSE` in the `/etc/cumulus/switchd.conf` file), the maximum number of mroute and ACL entries for each profile are:

| Profile    | Mroute Entries | ACL Entries                |
| ---------- | -------------- | -------------------------- |
| default    | 1000           | 250 (IPv6) or 500 (IPv4)   |
| ipmc-heavy | 8500           | 500 (IPv6) or 750 (IPv4)   |
| acl-heavy  | 450            | 1000 (IPv6) or 1750 (IPv4) |
| ipmc-max   | 13000          | 500 (IPv6) or 1000 (IPv4)  |

## Route Entry Takes Precedence Over Neighbor Entry

On Broadcom switches running Cumulus Linux 4.0 and later, when there is a /32 IPv4 or /128 IPv6 route and the same prefix is also a neighbor entry in the linux kernel, the route entry takes precedence over the neighbor entry in the forwarding lookup. To change this behavior, update the `route_preferred_over_neigh` variable to FALSE in the `/etc/cumulus/switchd.conf` file.
