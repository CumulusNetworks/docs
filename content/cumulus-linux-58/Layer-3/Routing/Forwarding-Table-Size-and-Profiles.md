---
title: Forwarding Table Size and Profiles
author: NVIDIA
weight: 740
toc: 3
---
Cumulus Linux advertises the maximum number of forwarding table entries supported on the switch, including:

- Layer 3 IPv4 <span class="a-tooltip">[LPM](## "Longest Prefix Match")</span> entries that have a mask less than /32
- Layer 3 IPv6 LPM entries that have a mask of /64 or less
- Layer 3 IPv6 LPM entries that have a mask greater than /64
- Layer 3 IPv4 neighbor (or host) entries that are the next hops seen in `ip neighbor`
- Layer 3 IPv6 neighbor entries that are the next hops seen in `ip -6 neighbor`
- ECMP next hops, which are IP address entries in the routing table that specify the next closest or most optimal router in its routing path
- MAC addresses

To determine the current table sizes on a switch, run the `{{<link url="Resource-Diagnostics-Using-cl-resource-query" text="cl-resource-query">}}` command.

Each switching architecture has specific resources available for forwarding table entries. Cumulus Linux stores:
- Forwarding table resources in a <span class="a-tooltip">[KVD](## "Key Value Database")</span>.
- ACL table entries and other switching functions in a fast memory area called the <span class="a-tooltip">[TCAM](## "Ternary Content Addressable Memory")</span> on Spectrum 1, and the <span class="a-tooltip">[ATCAM](## "Algorithmic TCAM")</span> on Spectrum-2 and later.

Cumulus Linux provides various general profiles for forwarding table resources, and, based on your network design, you might need to adjust various switch parameters to allocate resources, as needed.

{{%notice note%}}
The values provided in the profiles below are the maximum values that Cumulus Linux software allocates; the theoretical hardware limits might be higher. These limits refer to values that NVIDIA checks as part of unidimensional scale validation. If you try to achieve maximum scalability with multiple features enabled, results might differ from the values listed in this guide.
{{%/notice%}}

### Spectrum 1

Forwarding resource profiles control unicast forwarding table entry allocations. On the Spectrum 1 switch, TCAM profiles control multicast forwarding table entry allocations. For more information about multicast route entry limitations, refer to {{<link url="Netfilter-ACLs/#hardware-limitations-for-acl-rules" text="Hardware Limitations for ACL Rules">}}.
<!-- vale off -->
| <div style="width:100px">Profile| MAC Addresses | <div style="width:190px">Layer 3 Neighbors| LPM  |
| -------------- | ------------- | ------------------------- | ------------------------------ |
| default        | 40k           | 32k (IPv4) and 8k (IPv6) | 64k (IPv4) and 22k (IPv6-long) |
| l2-heavy       | 88k           | 48k (IPv4) and 18k (IPv6) | 8k (IPv4) and 8k (IPv6-long)   |
| l2-heavy-1     | 176k          | 4k (IPv4) and 2k (IPv6)   | 4k (IPv4) and 2k (IPv6-long)   |
| l2-heavy-2     | 86k           | 86k (IPv4) and 4k (IPv6)  | 8k (IPv4), 4k (IPv6-long)|
| v4-lpm-heavy   | 8k            | 8k (IPv4) and 16k (IPv6)  | 80k (IPv4) and 16k (IPv6-long)|
| v4-lpm-heavy-1 | 6k            | 6k (IPv4) and 2k (IPv6)   | 176k (IPv4) and 2k (IPv6-long) |
| v6-lpm-heavy   | 27k           | 8k (IPv4) and 36k (IPv6)  | 8k (IPv4), 32k (IPv6-long) and 32k (IPv6/64) |
| lpm-balanced   | 6k            | 4k (IPv4) and 3k (IPv6)   | 60k (IPv4), 60k (IPv6-long) and 120k (IPv6/64) |

### Spectrum-2 and Later

On Spectrum-2 and later, forwarding resource profiles control both unicast and multicast forwarding table entry allocations.

| <div style="width:100px">Profile| MAC Addresses | <div style="width:190px">Layer 3 Neighbors| LPM  |
| --------------  | ------------- | ------------------------- | ------------------------------ |
| default         | 50k           | 41k (IPv4) and 20k (IPv6) | 82k (IPv4), 74k (IPv6-long), 1k (IPv4-Mcast)|
| l2-heavy        | 115k          | 74k (IPv4) and 37k (IPv6) | 16k (IPv4), 24k (IPv6-long), 1k (IPv4-Mcast)|
| l2-heavy-1      | 239k          | 16k (IPv4) and 12k (IPv6) | 16k (IPv4), 16k (IPv6-long), 1k (IPv4-Mcast)|
| l2-heavy-2      | 124k          | 132k (IPv4) and 12k (IPv6)| 16k (IPv4), 16k (IPv6-long), 1k (IPv4-Mcast)|
| l2-heavy-3      | 107k          | 90k (IPv4) and 80k (IPv6) | 25k (IPv4), 10k (IPv6-long), 1k (IPv4-Mcast) |
| v4-lpm-heavy    | 16k           | 41k (IPv4) and 24k (IPv6) | 124k (IPv4), 24k (IPv6-long), 1k (IPv4-Mcast)|
| v4-lpm-heavy-1  | 16k           | 16k (IPv4) and 4k (IPv6)  | 256k (IPv4), 8k (IPv6-long), 1k (IPv4-Mcast)|
| v6-lpm-heavy    | 16k           | 16k (IPv4) and 62k (IPv6) | 16k (IPv4), 99k (IPv6-long), 1k (IPv4-Mcast)|
| v6-lpm-heavy-1  | 5k            | 4k (IPv4) and 4k (IPv6)   | 90k (IPv4), 235k (IPv6-long), 1k (IPv4-Mcast)|
| lpm-balanced    | 16k           | 16k (IPv4) and 12k (IPv6) | 124k (IPv4), 124k (IPv6-long), 1k (IPv4-Mcast)|
| ipmc-heavy      | 57k           | 41k (IPv4) and 20k (IPv6) | 82k (IPv4), 66k (IPv6-long), 8k (IPv4-Mcast) |
| ipmc-max        | 41K           | 41k (IPv4) and 20k (IPv6) | 74k (IPv4), 66k (IPv6-long), 15k (IPv4-Mcast)|

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

## ACL and VLAN Memory Resources

In addition to forwarding table memory resources, there are limitations on other memory resources for ACLs and VLAN interfaces; refer to {{<link url="Netfilter-ACLs/#hardware-limitations-for-acl-rules" text="Hardware Limitations for ACL Rules">}}.
