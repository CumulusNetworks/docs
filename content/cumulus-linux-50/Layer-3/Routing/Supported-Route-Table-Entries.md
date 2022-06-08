---
title: Supported Route Table Entries
author: NVIDIA
weight: 740
toc: 3
---
Cumulus Linux advertises the maximum number of route table entries supported on the switch, including:

- Layer 3 IPv4 LPM (longest prefix match) entries that have a mask less than /32
- Layer 3 IPv6 LPM entries that have a mask of /64 or less
- Layer 3 IPv6 LPM entries that have a mask greater than /64
- Layer 3 IPv4 neighbor (or host) entries that are the next hops seen in `ip neighbor`
- Layer 3 IPv6 neighbor entries that are the next hops seen in `ip -6 neighbor`
- ECMP next hops, which are IP address entries in the routing table that specify the next closest or most optimal router in its routing path
- MAC addresses

To determine the current table sizes on a switch, use `{{<link url="Resource-Diagnostics-Using-cl-resource-query" text="cl-resource-query">}}`.

## Supported Route Entries

Cumulus Linux provides several generalized profiles, described below. These profiles work only with layer 2 and layer 3 unicast forwarding.

The following tables list the number of MAC addresses, layer 3 neighbors, and LPM routes validated for each forwarding table profile. If you do not specify any profiles as described below, the switch uses the *default* values.

{{%notice note%}}
The values in the following tables reflect results from testing, which can differ from published manufacturer specifications.
{{%/notice%}}
<!-- vale off -->
### Spectrum
<!-- vale off -->
| <div style="width:100px">Profile| MAC Addresses | <div style="width:190px">Layer 3 Neighbors| Longest Prefix Match (LPM)  |
| -------------- | ------------- | ------------------------- | ------------------------------ |
| default        | 40k           | 32k (IPv4) and 16k (IPv6) | 64k (IPv4) and 28k (IPv6-long) |
| l2-heavy       | 88k           | 48k (IPv4) and 40k (IPv6) | 8k (IPv4) and 8k (IPv6-long)   |
| l2-heavy-1     | 180K          | 8k (IPv4) and 8k (IPv6)   | 8k (IPv4) and 8k (IPv6-long)   |
| v4-lpm-heavy   | 8k            | 8k (IPv4) and 16k (IPv6)  | 80k (IPv4) and 16k (IPv6-long) |
| v4-lpm-heavy-1 | 8k            | 8k (IPv4) and 2k (IPv6)   | 176k (IPv4) and 2k (IPv6-long) |
| v6-lpm-heavy   | 40k           | 8k (IPv4) and 40k (IPv6)  | 8k (IPv4), 32k (IPv6-long) and 32K (IPv6/64) |
| lpm-balanced   | 8k            | 8k (IPv4) and 8k (IPv6)   | 60k (IPv4), 60k (IPv6-long) and 120k (IPv6/64) |
<!-- vale on -->

### Spectrum-2 and Spectrum-3

| <div style="width:100px">Profile| MAC Addresses | <div style="width:190px">Layer 3 Neighbors| Longest Prefix Match (LPM)  |
| -------------- | ------------- | ------------------------- | ------------------------------ |
| default        | 50k           | 41k (IPv4) and 20k (IPv6) | 82k (IPv4), 74k (IPv6-long), 10K (IPv4-Mcast)|
| l2-heavy       | 115k          | 74k (IPv4) and 37k (IPv6) | 16k (IPv4), 24k (IPv6-long), 10K (IPv4-Mcast)|
| l2-heavy-1     | 239K          | 16k (IPv4) and 12k (IPv6) | 16k (IPv4), 16k (IPv6-long), 10K (IPv4-Mcast)|
| v4-lpm-heavy   | 16k           | 41k (IPv4) and 24k (IPv6) | 124k (IPv4), 24k (IPv6-long), 10K (IPv4-Mcast)|
| v4-lpm-heavy-1 | 16k           | 16k (IPv4) and 4k (IPv6)  | 256k (IPv4), 8k (IPv6-long), 10K (IPv4-Mcast)|
| v6-lpm-heavy   | 16k           | 16k (IPv4) and 62k (IPv6) | 16k (IPv4), 99k (IPv6-long), 10K (IPv4-Mcast)|
| lpm-balanced   | 16k           | 16k (IPv4) and 12k (IPv6) | 124k (IPv4), 124k (IPv6-long), 10K (IPv4-Mcast)|
| ipmc-heavy     | 57k           | 41k (IPv4) and 20k (IPv6) | 82K (IPv4), 66K (IPv6), 8K (IPv4-Mcast)     |
| ipmc-max       | 41K           | 41k (IPv4) and 20k (IPv6) | 74K (IPv4), 66K (IPv6), 15K (IPv4-Mcast)    |
<!--
| v6-lpm-heavy-1 | 5K            | 4K (IPv4) and 4K (IPv6)   | 120K (IPv4), 105K (IPv6-long), 1K (IPv4-Mcast)   |
| l2-heavy-3     | 105K          | 84K (IPv4) and 75K (IPv6) | 30K (IPv4), 1K (IPv6-long), 1K (IPv4-Mcast)      |
-->
<!-- vale on -->
The IPv6 number corresponds to the /64 IPv6 prefix. The /128 IPv6 prefix number is half of the /64 IPv6 prefix number.

## Forwarding Resource Profiles

You can configure forwarding resource allocation. Choose the profile that best suits your network architecture.
<!-- vale off -->
### Spectrum, Spectrum-2 and Spectrum-3
<!-- vale on -->
Specify the profile you want to use with the `forwarding_table.profile` variable in the `/etc/cumulus/datapath/traffic.conf` file. The following example specifies ipmc-max:

```
cumulus@switch:~$ sudo cat /etc/cumulus/datapath/traffic.conf
# Specify the forwarding table resource allocation profile, applicable
# only on platforms that support universal forwarding resources.
#
# /usr/cumulus/sbin/cl-resource-query reports the allocated table sizes
# based on the profile setting.
#
#   Values: one of { *** Common ***
#                   'default', 'l2-heavy', 'l2-heavy-1', 'l2-heavy-2',
#                   'v4-lpm-heavy', 'v4-lpm-heavy-1', 'v6-lpm-heavy',
#                   'rash-v4-lpm-heavy', 'rash-custom-profile1',
#                   'rash-custom-profile2', 'lpm-balanced'
#
#                   *** Mellanox Spectrum2+ only platforms ***
#                   'ipmc-heavy', 'ipmc-max'
#
#                   }
#
#   Default value: 'default'
#   Notes: some devices may support more modes, please consult user
#          guide for more details
#
forwarding_table.profile = ipmc-max
```

After you specify a different profile, {{%link url="Configuring-switchd#restart-switchd" text="restart `switchd`"%}} for the change to take effect.

### TCAM Profiles - Spectrum Only

Specify the profile you want to use with the `tcam_resource.profile` variable in the `/etc/mlx/datapath/tcam_profile.conf` file. The following example specifies ipmc-max:

```
cumulus@switch:~$ cat /etc/mlx/datapath/tcam_profile.conf
#
# Default tcam_profile configuration for Mellanox Spectrum chip
# Copyright (C) 20xx-2021 NVIDIA Corporation. ALL RIGHTS RESERVED.
#

#TCAM resource forwarding profile
# Applicable for Spectrum-1 and Spectrum-A1 switches only
# Valid profiles -
#    default, ipmc-heavy, acl-heavy, ipmc-max, ip-acl-heavy
tcam_resource.profile = ipmc-max
```

After you specify a different profile, {{%link url="Configuring-switchd#restart-switchd" text="restart `switchd`"%}} for the change to take effect.

When you enable {{<link url="Netfilter-ACLs#nonatomic-update-mode-and-atomic-update-mode" text="nonatomic updates">}} (`acl.non_atomic_update_mode` is `TRUE` in the `/etc/cumulus/switchd.conf` file), the maximum number of mroute and ACL entries for each profile are:

| Profile    | Mroute Entries | ACL Entries                |
| ---------- | -------------- | -------------------------- |
| default    | 1000           | 500 (IPv6) or 1000 (IPv4)  |
| ipmc-heavy | 8500           | 1000 (IPv6) or 1500 (IPv4) |
| acl-heavy  | 450            | 2000 (IPv6) or 3500 (IPv4) |
| ipmc-max   | 13000          | 1000 (IPv6) or 2000 (IPv4) |

When you disable {{<link url="Netfilter-ACLs#nonatomic-update-mode-and-atomic-update-mode" text="nonatomic updates">}} (`acl.non_atomic_update_mode` is `FALSE` in the `/etc/cumulus/switchd.conf` file), the maximum number of mroute and ACL entries for each profile are:

| Profile    | Mroute Entries | ACL Entries                |
| ---------- | -------------- | -------------------------- |
| default    | 1000           | 250 (IPv6) or 500 (IPv4)   |
| ipmc-heavy | 8500           | 500 (IPv6) or 750 (IPv4)   |
| acl-heavy  | 450            | 1000 (IPv6) or 1750 (IPv4) |
| ipmc-max   | 13000          | 500 (IPv6) or 1000 (IPv4)  |
