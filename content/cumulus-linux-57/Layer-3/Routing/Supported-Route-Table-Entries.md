---
title: Supported Route Table Entries
author: NVIDIA
weight: 740
toc: 3
---
Cumulus Linux advertises the maximum number of route table entries supported on the switch, including:

- Layer 3 IPv4 <span style="background-color:#F5F5DC">[LPM](## "Longest Prefix Match")</span> entries that have a mask less than /32
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

### Spectrum 1
<!-- vale off -->
| <div style="width:100px">Profile| MAC Addresses | <div style="width:190px">Layer 3 Neighbors| LPM  |
| -------------- | ------------- | ------------------------- | ------------------------------ |
| default        | 40k           | 32k (IPv4) and 16k (IPv6) | 64k (IPv4) and 28k (IPv6-long) |
| l2-heavy       | 88k           | 48k (IPv4) and 40k (IPv6) | 8k (IPv4) and 8k (IPv6-long)   |
| l2-heavy-1     | 180K          | 8k (IPv4) and 8k (IPv6)   | 8k (IPv4) and 8k (IPv6-long)   |
| v4-lpm-heavy   | 8k            | 8k (IPv4) and 16k (IPv6)  | 80k (IPv4) and 16k (IPv6-long) |
| v4-lpm-heavy-1 | 8k            | 8k (IPv4) and 2k (IPv6)   | 176k (IPv4) and 2k (IPv6-long) |
| v6-lpm-heavy   | 40k           | 8k (IPv4) and 40k (IPv6)  | 8k (IPv4), 32k (IPv6-long) and 32K (IPv6/64) |
| lpm-balanced   | 8k            | 8k (IPv4) and 8k (IPv6)   | 60k (IPv4), 60k (IPv6-long) and 120k (IPv6/64) |

### Spectrum-2 and Spectrum-3

| <div style="width:100px">Profile| MAC Addresses | <div style="width:190px">Layer 3 Neighbors| LPM  |
| --------------  | ------------- | ------------------------- | ------------------------------ |
| default         | 50k           | 41k (IPv4) and 20k (IPv6) | 82k (IPv4), 74k (IPv6-long), 1K (IPv4-Mcast)|
| l2-heavy        | 115k          | 74k (IPv4) and 37k (IPv6) | 16k (IPv4), 24k (IPv6-long), 1K (IPv4-Mcast)|
| l2-heavy-1      | 239k          | 16k (IPv4) and 12k (IPv6) | 16k (IPv4), 16k (IPv6-long), 1K (IPv4-Mcast)|
| l2-heavy-v4-lpm | 125k          | 1k (IPv4) and 128 (IPv6) | 65k (IPv4), 512 (IPv6-long), 0 (IPv4-Mcast)|
| l2-heavy-3      | 107k          | 90k (IPv4) and 80k (IPv6) | 25k (IPv4), 10k (IPv6-long), 1K (IPv4-Mcast) |
| v4-lpm-heavy    | 16k           | 41k (IPv4) and 24k (IPv6) | 124k (IPv4), 24k (IPv6-long), 1K (IPv4-Mcast)|
| v4-lpm-heavy-1  | 16k           | 16k (IPv4) and 4k (IPv6)  | 256k (IPv4), 8k (IPv6-long), 1K (IPv4-Mcast)|
| v6-lpm-heavy    | 16k           | 16k (IPv4) and 62k (IPv6) | 16k (IPv4), 99k (IPv6-long), 1K (IPv4-Mcast)|
| v6-lpm-heavy-1  | 5k            | 4k (IPv4) and 4k (IPv6)   | 90k (IPv4), 235k (IPv6-long), 1K (IPv4-Mcast)|
| lpm-balanced    | 16k           | 16k (IPv4) and 12k (IPv6) | 124k (IPv4), 124k (IPv6-long), 1K (IPv4-Mcast)|
| ipmc-heavy      | 57k           | 41k (IPv4) and 20k (IPv6) | 82K (IPv4), 66K (IPv6-long), 8K (IPv4-Mcast) |
| ipmc-max        | 41K           | 41k (IPv4) and 20k (IPv6) | 74K (IPv4), 66K (IPv6-long), 15K (IPv4-Mcast)|

The IPv6 number corresponds to the /64 IPv6 prefix. The /128 IPv6 prefix number is half of the /64 IPv6 prefix number.

{{%notice note%}}
For the ipmc-max profile, the `cl-resource-query` command output displays 33K instead of 15K as the maximum number of IPv4 multicast routes in `switchd`. 15K is the supported and validated value. You can use the higher value of 33K to test higher multicast scale in non-production environments.
{{%/notice%}}

<!-- vale on -->
## Change Forwarding Resource Profiles

You can set the profile that best suits your network architecture.

{{< tabs "TabID64 ">}}
{{< tab "NVUE Commands ">}}

Run the `nv set system forwarding profile <profile-name>` command to specify the profile you want to use.

The following example command sets the `l2-heavy` profile:

```
cumulus@switch:~$ nv set system forwarding profile l2-heavy 
cumulus@switch:~$ nv config apply
```

To set the profile back to the default:

```
cumulus@switch:~$ nv unset system forwarding profile l2-heavy 
cumulus@switch:~$ nv config apply
```

Instead of the above command, you can run the `nv set system forwarding profile default` command to set the profile back to the default.

{{< /tab >}}
{{< tab "Linux Commands ">}}

Specify the profile you want to use with the `forwarding_table.profile` variable in the `/etc/cumulus/datapath/traffic.conf` file. The following example specifies `l2-heavy`:

```
cumulus@switch:~$ sudo cat /etc/cumulus/datapath/traffic.conf
...
forwarding_table.profile = l2-heavy
```

After you specify a different profile, restart `switchd` with the `sudo systemctl restart switchd.service` command.

{{< /tab >}}
{{< /tabs >}}

To show the different forwarding profiles that your switch supports and the MAC address, layer 3 neighbor, and LPM scale availability for each forwarding profile, run the `nv show system forwarding profile-option` command.

## TCAM Profiles - Spectrum 1

Specify the profile you want to use with the `tcam_resource.profile` variable in the `/etc/mlx/datapath/tcam_profile.conf` file. The following example specifies ipmc-max:

```
cumulus@switch:~$ cat /etc/mlx/datapath/tcam_profile.conf
...
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
