---
title: Resource Diagnostics
author: NVIDIA
weight: 1210
toc: 3
---

Cumulus Linux synchronizes routes between the kernel and the switching silicon. If the required resource pools in hardware fill up, new kernel routes can cause existing routes to move from being fully allocated to being partially allocated. To avoid this issue, monitor the routes in the hardware to keep them below the ASIC limits.

## Monitor Resources in Cumulus Linux Hardware

To monitor resources in Cumulus Linux, you can use either NVUE commands or the Linux `cl-resource-query` command.
- NVUE commands report resource utilization from hardware when available; otherwise, they report software-maintained values.
- `cl-resource-query` reports software-maintained resource utilization.

Because these commands retrieve information from different sources (hardware or software), the reported values might differ slightly under certain conditions. 

{{< tabs "TabID14 ">}}
{{< tab "NVUE Commands ">}}

To show both global and ACL ASIC resources, run the `nv show platform asic <asic-id> resource` command.

```
cumulus@switch:~$ nv show platform asic ASIC1 resource
Global
=========
    Resource Name                Used  Percentage  Max     Free    High-Watermark  High-Watermark-Timestamp
    ---------------------------  ----  ----------  ------  ------  --------------  ------------------------------
    ACL-18B-Rules-Key            3     0.0%        60044   60041   3               2026-07-27 11:42:07.433184 UTC
    ACL-36B-Rules-Key            0     0.0%        60041   60041   0               2026-07-27 11:41:07.675445 UTC
    ACL-54B-Rules-Key            0     0.0%        36025   36025   0               2026-07-27 11:41:07.675445 UTC
    ACL-Regions                  2     0.5%        400     398     2               2026-07-27 11:41:07.675445 UTC
    Downstream-VNI-FID-count     0
    Dynamic-Config-DNAT-entries  0     0.0%        64      64
    Dynamic-Config-SNAT-entries  0     0.0%        64      64
    Dynamic-DNAT-entries         0     0.0%        1024    1024
    Dynamic-SNAT-entries         0     0.0%        1024    1024
    ECMP-entries                 0
    ECMP-nexthops                0     0.0%        33077   33077   0               2026-07-27 11:41:07.675445 UTC
    Egress-ACL-entries           0
    Flow-Counters                4     0.0%        40620   40616   4               2026-07-27 11:42:07.433184 UTC
    IPv4-Routes                  2     0.0%        82693   82691   2               2026-07-27 11:42:07.433184 UTC
    IPv4-host-entries            0     0.0%        41347   41347   0               2026-07-27 11:41:07.675445 UTC
    IPv4-neighbors               0
    IPv4-route-entries           0     0.0%        82693   82693
    IPv6-Routes                  12    0.0%        74424   74412   12              2026-07-27 11:42:07.433184 UTC
    IPv6-host-entries            0     0.0%        20673   20673   0               2026-07-27 11:41:07.675445 UTC
    IPv6-neighbors               0
    IPv6-route-entries           20    0.0%        74424   74404
    Ingress-ACL-entries          0
    MAC-entries                  68    0.1%        57885   57817   68              2026-07-27 11:41:07.675445 UTC
    RIF-Basic-Counters           68    1.7%        4000    3932    68              2026-07-27 11:41:07.675445 UTC
    RIF-Enhanced-Counters        0     0.0%        2707    2707    0               2026-07-27 11:41:07.675445 UTC
    Total-FID-count              5     0.1%        6143    6138
    Total-Mcast-Routes           0     0.0%        1000    1000    0               2026-07-27 11:41:07.675445 UTC
    Total-Routes                 20    0.0%        157117  157097
    Vport-FID-count              5

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

To show global ASIC resources on the switch in tabular format, run the `nv show platform asic <asic-id> resource global` command.

```
cumulus@switch:~$ nv show platform asic ASIC1 resource global
Resource Name                Used  Percentage  Max     Free    High-Watermark  High-Watermark-Timestamp
---------------------------  ----  ----------  ------  ------  --------------  ------------------------------
ACL-18B-Rules-Key            3     0.0%        60044   60041   3               2026-07-27 11:42:07.433184 UTC
ACL-36B-Rules-Key            0     0.0%        60041   60041   0               2026-07-27 11:41:07.675445 UTC
ACL-54B-Rules-Key            0     0.0%        36025   36025   0               2026-07-27 11:41:07.675445 UTC
ACL-Regions                  2     0.5%        400     398     2               2026-07-27 11:41:07.675445 UTC
Downstream-VNI-FID-count     0
Dynamic-Config-DNAT-entries  0     0.0%        64      64
Dynamic-Config-SNAT-entries  0     0.0%        64      64
Dynamic-DNAT-entries         0     0.0%        1024    1024
Dynamic-SNAT-entries         0     0.0%        1024    1024
ECMP-entries                 0
ECMP-nexthops                0     0.0%        33077   33077   0               2026-07-27 11:41:07.675445 UTC
Egress-ACL-entries           0
Flow-Counters                4     0.0%        40620   40616   4               2026-07-27 11:42:07.433184 UTC
IPv4-Routes                  2     0.0%        82693   82691   2               2026-07-27 11:42:07.433184 UTC
IPv4-host-entries            0     0.0%        41347   41347   0               2026-07-27 11:41:07.675445 UTC
IPv4-neighbors               0
IPv4-route-entries           0     0.0%        82693   82693
IPv6-Routes                  12    0.0%        74424   74412   12              2026-07-27 11:42:07.433184 UTC
IPv6-host-entries            0     0.0%        20673   20673   0               2026-07-27 11:41:07.675445 UTC
IPv6-neighbors               0
IPv6-route-entries           20    0.0%        74424   74404
Ingress-ACL-entries          0
MAC-entries                  68    0.1%        57885   57817   68              2026-07-27 11:41:07.675445 UTC
RIF-Basic-Counters           68    1.7%        4000    3932    68              2026-07-27 11:41:07.675445 UTC
RIF-Enhanced-Counters        0     0.0%        2707    2707    0               2026-07-27 11:41:07.675445 UTC
Total-FID-count              5     0.1%        6143    6138
Total-Mcast-Routes           0     0.0%        1000    1000    0               2026-07-27 11:41:07.675445 UTC
Total-Routes                 20    0.0%        157117  157097
Vport-FID-count              5
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
