---
title: Resource Diagnostics Using cl-resource-query
author: NVIDIA
weight: 217
pageID: 8362593
---
You can use the `cl-resource-query` command to retrieve information about host entries, MAC entries, layer 2 and layer 3 routes, and {{<link url="Equal-Cost-Multipath-Load-Sharing-Hardware-ECMP" text="ECMP">}} routes that are in use. Because Cumulus Linux synchronizes routes between the kernel and the switching silicon, if the required resource pools in hardware fill up, new kernel routes can cause existing routes to move from being fully allocated to being partially allocated. To avoid this, monitor the routes in the hardware to keep them below the ASIC limits. For example, on a Broadcom Tomahawk switch, the limits are as follows:

    routes: 8192 <<<< if all routes are IPv6, or 65536 if all routes are IPv4
    route mask limit 64
    host_routes: 73728
    ecmp_nhs: 16327
    ecmp_nhs_per_route: 52

This translates to approximately 314 routes with ECMP nexthops, if every route has the maximum ECMP nexthops.

To monitor the routes in Cumulus Linux hardware, use the `cl-resource-query` command. The results vary between switches running on different chipsets.

The example below shows `cl-resource-query` results for a Broadcom Tomahawk switch:

    cumulus@switch:~$ sudo cl-resource-query
    IPv4/IPv6 host entries:                 0,   0% of maximum value  40960
    IPv4 neighbors:                         0
    IPv6 neighbors:                         0
    IPv4 route entries:                     4,   0% of maximum value  65536
    IPv6 route entries:                     8,   0% of maximum value   8192
    IPv4 Routes:                            4
    IPv6 Routes:                            8
    Total Routes:                          12,   0% of maximum value  65536
    ECMP nexthops:                          0,   0% of maximum value  16327
    MAC entries:                            1,   0% of maximum value  40960
    Total Mcast Routes:                     0,   0% of maximum value  20480
    Ingress ACL entries:                  195,  12% of maximum value   1536
    Ingress ACL counters:                 195,  12% of maximum value   1536
    Ingress ACL meters:                    21,   1% of maximum value   2048
    Ingress ACL slices:                     6, 100% of maximum value      6
    Egress ACL entries:                    58,  11% of maximum value    512
    Egress ACL counters:                   58,   5% of maximum value   1024
    Egress ACL meters:                     29,   5% of maximum value    512
    Egress ACL slices:                      2, 100% of maximum value      2
    Ingress ACL ipv4_mac filter table:     36,  14% of maximum value    256 (allocated: 256)
    Ingress ACL ipv6 filter table:         29,  11% of maximum value    256 (allocated: 256)
    Ingress ACL mirror table:               0,   0% of maximum value      0 (allocated: 0)
    Ingress ACL 8021x filter table:         0,   0% of maximum value      0 (allocated: 0)
    Ingress PBR ipv4_mac filter table:      0,   0% of maximum value      0 (allocated: 0)
    Ingress PBR ipv6 filter table:          0,   0% of maximum value      0 (allocated: 0)
    Ingress ACL ipv4_mac mangle table:      0,   0% of maximum value      0 (allocated: 0)
    Ingress ACL ipv6 mangle table:          0,   0% of maximum value      0 (allocated: 0)
    Egress ACL ipv4_mac filter table:      29,  11% of maximum value    256 (allocated: 256)
    Egress ACL ipv6 filter table:           0,   0% of maximum value      0 (allocated: 0)
    ACL L4 port range checkers:             2,   6% of maximum value     32

The example below shows `cl-resource-query` results for a Broadcom Trident II switch:

```
cumulus@switch:~$ sudo cl-resource-query
IPv4/IPv6 host entries:                 0,   0% of maximum value  16384
IPv4 neighbors:                         0
IPv6 neighbors:                         0
IPv4 route entries:                     0,   0% of maximum value 131072
IPv6 route entries:                     1,   0% of maximum value  20480
IPv4 Routes:                            0
IPv6 Routes:                            1
Total Routes:                           1,   0% of maximum value 131072
ECMP nexthops:                          0,   0% of maximum value  16346
MAC entries:                            0,   0% of maximum value  32768
Total Mcast Routes:                     0,   0% of maximum value   8192
Ingress ACL entries:                  130,   6% of maximum value   2048
Ingress ACL counters:                  86,   4% of maximum value   2048
Ingress ACL meters:                    21,   0% of maximum value   4096
Ingress ACL slices:                     4,  66% of maximum value      6
Egress ACL entries:                    58,  11% of maximum value    512
Egress ACL counters:                   58,   5% of maximum value   1024
Egress ACL meters:                     29,   5% of maximum value    512
Egress ACL slices:                      2, 100% of maximum value      2
Ingress ACL ipv4_mac filter table:     36,   7% of maximum value    512 (allocated: 256)
Ingress ACL ipv6 filter table:         29,   3% of maximum value    768 (allocated: 512)
Ingress ACL mirror table:               0,   0% of maximum value      0 (allocated: 0)
Ingress ACL 8021x filter table:         0,   0% of maximum value      0 (allocated: 0)
Ingress PBR ipv4_mac filter table:      0,   0% of maximum value      0 (allocated: 0)
Ingress PBR ipv6 filter table:          0,   0% of maximum value      0 (allocated: 0)
Ingress ACL ipv4_mac mangle table:      0,   0% of maximum value      0 (allocated: 0)
Ingress ACL ipv6 mangle table:          0,   0% of maximum value      0 (allocated: 0)
Egress ACL ipv4_mac filter table:      29,  11% of maximum value    256 (allocated: 256)
Egress ACL ipv6 filter table:           0,   0% of maximum value      0 (allocated: 0)
ACL L4 port range checkers:             2,   8% of maximum value     24
```

{{%notice note%}}
- Ingress ACL and Egress ACL entries show the counts in single wide (*not* double-wide). For information about ACL entries, see
{{<link url="Netfilter-ACLs#estimate-the-number-of-rules" text="Estimate the Number of ACL Rules">}}.
- On a Spectrum switch in Cumulus Linux 3.7.4, the `cl-resource-query` command shows the number of TCAM entries used by the different types of ACL resources.
- Cumulus Linux 3.7.11 and later provides the `net show system asic` command, which is the NCLU command equivalent of `cl-resource-query`.
{{%/notice%}}

## ECMP nexthops on Mellanox Spectrum Switches

On Mellanox Spectrum switches, the maximum value of ECMP nexthops shown in `cl-resource-query` results differ according to the Cumulus Linux release:

- In Cumulus Linux 3.7.7 and earlier, the maximum value is 16384
- In Cumulus Linux 3.7.8 through 3.7.14.12, the maximum value is 4101
- In Cumulus Linux 3.7.15 and later, the maximum value is 262464

In Cumulus Linux 3.7.15, `cl-resource-query` results show the maximum value of ECMP nexthops as 262464. This is the theoretical maximum number of supported ECMP nexthops. However, the actual number of maximum ECMP nexthops depends on the number of nexthops in individual ECMP containers as allocated in the ASIC. The following calculation provides the maximum number of ECMP containers available on the switch:

- Single path ECMP containers: 7808
- 2-path ECMP containers: 3904
- 3-4 path ECMP containers: 976 (double size containers are allocated)
- 5-16 path ECMP containers: 488
- 17-32 path ECMP containers: 244
- 33-64 path ECMP containers: 122

In Cumulus Linux 3.7.x, the current value of ECMP nexthops counts only 2-path or more ECMP containers. For each programmed ECMP container, the ECMP nexthop value is incremented by a multiplication factor, which is retrieved from the `/cumulus/switchd/run/route_info/ecmp_nh/max_per_route` file and is derived internally as the minimum of the following two values:

- The number of ports present on the switch.
- The `ecmp_max_paths` parameter configured in the `/etc/cumulus/datapath/traffic.conf` file.

To retrieve all programmed ECMPs, you can issue the `/usr/lib/cumulus/mlxcmd l3 ecmp_table` command. The same information is populated in `cl-support`.
