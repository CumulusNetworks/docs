---
title: Resource Diagnostics Using cl-resource-query
author: NVIDIA
weight: 1210
toc: 3
---
You can use the `cl-resource-query` command to retrieve information about host entries, MAC entries, layer 2 and layer 3 routes, and {{<link url="Equal-Cost-Multipath-Load-Sharing" text="ECMP">}} routes that are in use. Because Cumulus Linux synchronizes routes between the kernel and the switching silicon, if the required resource pools in hardware fill up, new kernel routes can cause existing routes to move from being fully allocated to being partially allocated. To avoid this, monitor the routes in the hardware to keep them below the ASIC limits.

To monitor the routes in Cumulus Linux hardware, use the `cl-resource-query` command.

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

Ingress ACL and Egress ACL entries show the counts in single wide (*not* double-wide). For information about ACL entries, see {{<link url="Netfilter-ACLs#estimate-the-number-of-rules" text="Estimate the Number of ACL Rules">}}.
