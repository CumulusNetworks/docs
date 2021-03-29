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

To determine the current table sizes on a switch, use either the NCLU `net show system asic` command or `{{<link url="Resource-Diagnostics-Using-cl-resource-query" text="cl-resource-query">}}`.

## Forwarding Table Profiles

You can configure the allocation of forwarding table resources and mechanisms. Cumulus Linux provides a number of generalized profiles, described below. These profiles work only with layer 2 and layer 3 unicast forwarding.

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

## Supported Route Entries

The following tables list the number of MAC addresses, layer 3 neighbors, and LPM routes validated for each forwarding table profile. If you do not specify any profiles as described above, the switch uses the *default* values.

{{%notice tip%}}

The values in the following tables reflect results from testing, which might differ from published manufacturer specifications.

{{%/notice%}}

| <div style="width:100px">Profile| MAC Addresses | <div style="width:190px">Layer 3 Neighbors| Longest Prefix Match (LPM)  |
| -------------- | ------------- | ------------------------- | ------------------------------ |
| default        | 40k           | 32k (IPv4) and 16k (IPv6) | 64k (IPv4) and 28k (IPv6-long) |
| l2-heavy       | 88k           | 48k (IPv4) and 40k (IPv6) | 8k (IPv4) and 8k (IPv6-long)   |
| l2-heavy-1     | 180K          | 8k (IPv4) and 8k (IPv6)   | 8k (IPv4) and 8k (IPv6-long)   |
| v4-lpm-heavy   | 8k            | 8k (IPv4) and 16k (IPv6)  | 80k (IPv4) and 16k (IPv6-long) |
| v4-lpm-heavy-1 | 8k            | 8k (IPv4) and 2k (IPv6)   | 176k (IPv4) and 2k (IPv6-long) |
| v6-lpm-heavy   | 40k           | 8k (IPv4) and 40k (IPv6)  | 8k (IPv4), 32k (IPv6-long) and 32K (IPv6/64) |
| lpm-balanced   | 8k            | 8k (IPv4) and 8k (IPv6)   | Spectrum-2 and Spectrum-3:<br>120k (IPv4) and 120k (IPv6-long)<br>Spectrum:<br>60k (IPv4), 60k (IPv6-long) and 120k (IPv6/64) |

## TCAM Resource Profiles

You can configure TCAM resource allocation, which is shared between IP multicast forwarding entries and ACL tables. Cumulus Linux provides a number of general profiles. Choose the profile that best suits your network architecture and specify that profile name in the `tcam_resource.profile` variable in the `/usr/lib/python2.7/dist-packages/cumulus/__chip_config/mlx/datapath.conf` file; for example:

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
