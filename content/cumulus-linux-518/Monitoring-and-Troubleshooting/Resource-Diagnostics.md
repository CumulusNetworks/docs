---
title: Resource Diagnostics
author: NVIDIA
weight: 1210
toc: 3
---

Cumulus Linux synchronizes routes between the kernel and the switching silicon. If the required resource pools in hardware fill up, new kernel routes can cause existing routes to move from being fully allocated to being partially allocated. To avoid this issue, monitor the routes in the hardware to keep them below the ASIC limits.

## Monitor Routes in Cumulus Linux Hardware 

You can retrieve information about host entries, MAC entries, layer 2 and layer 3 routes, and {{<link url="Equal-Cost-Multipath-Load-Sharing" text="ECMP">}} routes that are in use.

To monitor the routes in Cumulus Linux hardware, you can use NVUE commands or the Linux `cl-resource-query` command.

{{< tabs "TabID14 ">}}
{{< tab "NVUE Commands ">}}

To show both global and ACL ASIC resources, run the `nv show platform asic <asic-id> resource` command.

```
cumulus@switch:~$ nv show platform asic ASIC1 resource
Global 
========= 
    Resource Name                Used  Percentage  Max     Free    High-Watermark  High-Watermark-Timestamp 
    ---------------------------  ----  ----------  ------  ------  --------------  ------------------------------ 
    ACL-18B-Rules-Key            2     0.0%        60069   60067   2               2026-06-07 17:01:10.135707 UTC 
    ACL-36B-Rules-Key            0     0.0%        60067   60067   0               2026-06-07 17:01:10.135707 UTC 
    ACL-54B-Rules-Key            0     0.0%        36040   36040   0               2026-06-07 17:01:10.135707 UTC 
    ACL-Regions                  2     0.5%        400     398     2               2026-06-07 17:01:10.135707 UTC 
    Downstream-VNI-FID-count     0 
    Dynamic-Config-DNAT-entries  0     0.0%        64      64 
    Dynamic-Config-SNAT-entries  0     0.0%        64      64 
    Dynamic-DNAT-entries         0     0.0%        1024    1024 
    Dynamic-SNAT-entries         0     0.0%        1024    1024 
    ECMP-entries                 0 
    ECMP-nexthops                0     0.0%        33077   33077   0               2026-06-07 17:01:10.135707 UTC 
    Egress-ACL-entries           0 
    Flow-Counters                4     0.0%        40800   40796   4               2026-06-07 17:02:10.005791 UTC 
    IPv4-Routes                  0 
    IPv4-host-entries            0     0.0%        41347   41347   0               2026-06-07 17:01:10.135707 UTC 
    IPv4-neighbors               0 
    IPv4-route-entries           2     0.0%        82693   82691   2               2026-06-07 17:02:10.005791 UTC 
    IPv6-Routes                  11 
    IPv6-host-entries            0     0.0%        20673   20673   0               2026-06-07 17:01:10.135707 UTC 
    IPv6-neighbors               0 
    IPv6-route-entries           12    0.0%        74424   74412   12              2026-06-07 17:03:10.006976 UTC 
    Ingress-ACL-entries          0 
    MAC-entries                  38    0.1%        57885   57847   38              2026-06-07 17:02:10.005791 UTC 
    RIF-Basic-Counters           38    0.9%        4000    3962    38              2026-06-07 17:02:10.005791 UTC 
    RIF-Enhanced-Counters        0     0.0%        2719    2719    0               2026-06-07 17:01:10.135707 UTC 
    Total-FID-count              1     0.0%        6143    6142 
    Total-Mcast-Routes           0     0.0%        1000    1000    0               2026-06-07 17:01:10.135707 UTC 
    Total-Routes                 14    0.0%        157117  157103 
    Vport-FID-count              1 

Acl 
====== 
    Resource Name                  18B Rule  36B Rule  54B Rule  Rule Count 
    -----------------------------  --------  --------  --------  ---------- 
    Egress-ACL-ipv4-filter-table   0         0         0         0 
    Egress-ACL-ipv4-mangle-table   0         0         0         0 
    Egress-ACL-ipv6-filter-table   0         0         0         0 
    Egress-ACL-ipv6-mangle-table   0         0         0         0 
    Egress-ACL-mac-filter-table    0         0         0         0 
    Ingress-ACL-ipv4-filter-table  0         0         0         0 
    Ingress-ACL-ipv4-mangle-table  0         0         0         0 
    Ingress-ACL-ipv6-filter-table  0         0         0         0 
    Ingress-ACL-ipv6-mangle-table  0         0         0         0 
    Ingress-ACL-mac-filter-table   0         0         0         0 
    Ingress-PBR-ipv4-filter-table  0         0         0         0 
    Ingress-PBR-ipv6-filter-table  0         0         0         0 
```
<!-- 5.17
```
cumulus@switch:~$ nv show platform asic ASIC1 resource
Global 
========= 
    Resource Name             Count         Max        Percentage 
    ------------------                      -----      ---------
    IPv4-host-entries             4         32768      0% 
    IPv6-host-entries             4         8192       0% 
    IPv4-neighbors                4                    0% 
    IPv6-neighbors                4                    0% 
    IPv4-route-entries            22        65536      0% 
    IPv6-route-entries            21        45056      0% 
        IPv4-Routes               22                   0% 
    IPv6-Routes                   13                   0% 
    MAC-entries                   36        40960      0% 
    Total-Mcast-Routes             0        1000       0% 
    Ingress-ACL-entries            0                   0% 
    Egress-ACL-entries             0                   0% 
      Total-Routes                 43       110592     0% 
    ACL-Regions                    2        400        0% 
    ACL-18B-Rules-Key              2        3792       0% 
    ACL-36B-Rules-Key              0        1536       0% 
    ACL-54B-Rules-Key              0        1024       0% 
    ECMP-entries                   5                   0% 
    ECMP-nexthops                  8        7808       0% 
    Flow-Counters                  10       16196      0% 
       RIF-Basic-Counters          36       1000       3% 
    RIF-Enhanced-Counters          0        964        0% 
    Downstream-VNI-FID-count       0                   0% 
    Total-FID-count                3        6143       0% 
    Vport-FID-count                3                   0%
Acl 
====== 
    Resource Name                         18B Rule     36B Rule     54B Rule      Rule Count 
    ----------------------------          ----------   -----------  ----------     ------ 
    Egress-ACL-ipv4-filter-table           0           0               0            0 
    Egress-ACL-mac-filter-table            0           0               0            0 
    Ingress-ACL-mac-filter-table           0           0               0            0 
    Ingress-ACL-ipv4-filter-table          0           0               0            0 
    Ingress-ACL-ipv6-filter-table          0           0               0            0 
    Ingress-ACL-ipv4-mangle-table          1           0               0            1 
    Ingress-ACL-ipv6-mangle-table          0           0               0            0 
    Egress ACL-ipv4-mangle-table           1           0               0            1 
    Egress-ACL-ipv6-mangle-table           0           0               0            0 
    Ingress-PBR-ipv4-filter-table          0           0               0            0 
    Ingress-PBR-ipv6-filter-tabl           0           0               0            0  
```
-->
To show global ASIC resources on the switch in tabular format, run the `nv show platform asic <asic-id> resource global` command.

```
cumulus@switch:~$ nv show platform asic ASIC1 resource global
Resource Name                     Count   Max      Percentage 
    ------------------            -----   ----      ---------- 
    IPv4-host-entries             4       32768     0%
    IPv6-host-entries             4       8192      0% 
    IPv4-neighbors                4                 0% 
    IPv6-neighbors                4                 0% 
    IPv4-route-entries            22      65536     0% 
    IPv6-route-entries            21      45056     0% 
    IPv4-Routes                   22                0% 
    IPv6-Routes                   13                0% 
    MAC-entries                   36      40960     0% 
    Total-Mcast-Routes            0       1000      0% 
    Ingress-ACL-entries           0                 0% 
    Egress-ACL-entries            0                 0% 
    Total-Routes                  43      110592    0% 
    ACL-Regions                   2       400       0% 
    ACL-18B-Rules-Key             2       3792      0% 
    ACL-36B-Rules-Key             0       1536      0% 
    ACL-54B-Rules-Key             0       1024      0% 
    ECMP-entries                  5                 0% 
    ECMP-nexthops                 8       7808      0% 
    Flow-Counters                 10      16196     0% 
    Ingress-ACL-entries           0                 0% 
    RIF-Basic-Counters            36      1000      3% 
    RIF-Enhanced-Counters         0       964       0% 
    Downstream-VNI-FID-count      0                 0% 
    Total-FID-count               3       6143      0% 
    Vport-FID-count               3                 0%
    Dynamic-Config-DNAT-entries   0       64        0.0% 
    Dynamic-Config -SNAT-entries  0       64        0.0% 
    Dynamic-DNAT-entries          0       1024      0.0% 
    Dynamic-SNAT-entries          0       1024      0.0% 
```

To show only ACL ASIC resources in tabular format, run the `nv show platform asic <asic-id> resource acl` command.

```
cumulus@switch:~$ nv show platform asic ASIC1 resource acl
Resource Name                        18B Rule     36B Rule     54B Rule    Rule Count 
    ----------------------------     ----------   ----------   ----------  -------- 
    Egress-ACL-ipv4-filter-table       0          0             0          0 
    Egress-ACL-mac-filter-table        0          0             0          0 
    Ingress-ACL-mac-filter-table       0          0             0          0 
    Ingress-ACL-ipv4-filter-table      0          0             0          0 
    Ingress-ACL-ipv6-filter-table      0          0             0          0 
    Ingress-ACL-ipv4-mangle-table      1          0             0          1 
    Ingress-ACL-ipv6-mangle-table      0          0             0          0 
    Egress ACL-ipv4-mangle-table      1           0             0          1 
    Egress-ACL-ipv6-mangle-table      0           0             0          0 
    Ingress-PBR-ipv4-filter-table     0           0             0          0 
    Ingress-PBR-ipv6-filter-tabl      0           0             0          0 
    Egress-ACL-ipv6-filter-table      0           0             0          0 
```

{{< /tab >}}
{{< tab "Linux Commands ">}}

The example below shows `cl-resource-query` results for an NVIDIA Spectrum-2 switch:

```
cumulus@switch:~$ sudo cl-resource-query
IPv4 host entries:                      0,   0% of maximum value  41360
IPv6 host entries:                      0,   0% of maximum value  20680
IPv4 neighbors:                         0
IPv6 neighbors:                         0
IPv4 route entries:                     0,   0% of maximum value  82720
IPv6 route entries:                    22,   0% of maximum value  74446
IPv4 Routes:                            0
IPv6 Routes:                           12
Total Routes:                          22,   0% of maximum value 157166
Unicast Adjacency entries:              0,   0% of maximum value  33087
ECMP entries:                           0,   0% of maximum value   8571
MAC entries:                           38,   0% of maximum value  57903
Total Mcast Routes:                     0,   0% of maximum value   1000
Ingress ACL entries:                    0
Egress ACL entries:                     0
ACL Regions:                            4,   1% of maximum value    400
ACL 18B Rules Key:                      1,   0% of maximum value  57476
ACL 36B Rules Key:                      0,   0% of maximum value  57475
ACL 54B Rules Key:                      0,   0% of maximum value  34485
Ingress ACL mac filter table:           0    18B : 0 36B : 0 54B : 0 
Ingress ACL ipv4 filter table:          0    18B : 0 36B : 0 54B : 0 
Ingress ACL ipv6 filter table:          0    18B : 0 36B : 0 54B : 0 
Egress ACL mac filter table:            0    18B : 0 36B : 0 54B : 0 
Egress ACL ipv4 filter table:           0    18B : 0 36B : 0 54B : 0 
Egress ACL ipv6 filter table:           0    18B : 0 36B : 0 54B : 0 
Ingress ACL ipv4 mangle table:          0    18B : 0 36B : 0 54B : 0 
Ingress ACL ipv6 mangle table:          0    18B : 0 36B : 0 54B : 0 
Ingress PBR ipv4 filter table:          0    18B : 0 36B : 0 54B : 0 
Ingress PBR ipv6 filter table:          0    18B : 0 36B : 0 54B : 0 
Flow Counters:                          2,   0% of maximum value  39430
RIF Basic Counters:                     0,   0% of maximum value   7885
RIF Enhanced Counters:                 38,   1% of maximum value   2666
Dynamic SNAT entries:                   0,   0% of maximum value   1024
Dynamic DNAT entries:                   0,   0% of maximum value   1024
Dynamic Config SNAT entries:            0,   0% of maximum value     64
Dynamic Config DNAT entries:            0,   0% of maximum value     64
```

{{< /tab >}}
{{< /tabs >}}

Ingress ACL and Egress ACL entries show the counts in single wide (*not* double-wide). For information about ACL entries, see {{<link url="Access-Control-List-Configuration#estimate-the-number-of-rules" text="Estimate the Number of ACL Rules">}}.

## Clear Resource Metrics

To clear the high watermark related metrics for a specific ASIC, run the `nv action clear platform asic <asic-id> resource` command:

```
cumulus@switch:~$ nv action clear platform asic ASIC1 resource
```

{{%notice note%}}
The `nv action clear platform asic <asic-id> resource` command clears only High-Watermark and Last-High-Watermark resource metrics for the ASIC specified. All other metrics in the `nv show platform asic <asic-id> resource` command output are unaffected. 
{{%/notice%}}
