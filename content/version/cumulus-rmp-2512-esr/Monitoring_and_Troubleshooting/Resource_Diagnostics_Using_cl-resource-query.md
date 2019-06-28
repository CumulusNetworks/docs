---
title: Resource Diagnostics Using cl-resource-query
author: Cumulus Networks
weight: 89
aliases:
 - /display/RMP25ESR/Resource+Diagnostics+Using+cl-resource-query
 - /pages/viewpage.action?pageId=5116325
pageID: 5116325
product: Cumulus RMP
version: 2.5.12 ESR
imgData: cumulus-rmp-2512-esr
siteSlug: cumulus-rmp-2512-esr
---
You can use ` cl-resource-query  `to retrieve information about host
entries, MAC entries, L2 and L3 routes, and ingress and degrees ACL
counters and entries that are in use. This is especially useful because
Cumulus RMP syncs routes between the kernel and the switching silicon.
If the required resource pools in hardware fill up, new kernel routes
can cause existing routes to move from being fully allocated to being
partially allocated.

In order to avoid this, routes in the hardware should be monitored and
kept below the ASIC limits. For example on a Cumulus RMP system, the
limits are as follows:

    routes: 8092 <<<< if all routes are IPv6, or 16384 if all routes are IPv4
    long mask routes 2048 <<<< these are routes with a mask longer than the route mask limit
    route mask limit 64
    host_routes: 8192
    ecmp_nhs: 16346
    ecmp_nhs_per_route: 52

You can monitor this in Cumulus RMP with the `cl-resource-query`
command.

    cumulus@switch:~$ sudo cl-resource-query
    Host entries:               5,   0% of maximum value   2048
    IPv4 neighbors:             1
    IPv6 neighbors:             2
    IPv4/IPv6 entries:         13,   3% of maximum value    412
    Long IPv6 entries:          3,   1% of maximum value    256
    IPv4 Routes:                9
    IPv6 Routes:                5
    Total Routes:              14,   0% of maximum value  32768
    ECMP nexthops:              0,   0% of maximum value      1
    MAC entries:                0,   0% of maximum value  16384
    Ingress ACL entries:      463,  22% of maximum value   2048
    Ingress ACL counters:      56,   2% of maximum value   2048
    Ingress ACL meters:        10,   0% of maximum value   2048
    Ingress ACL slices:         3,  37% of maximum value      8
    Egress ACL entries:        36,   7% of maximum value    512
    Egress ACL counters:       36,   7% of maximum value    512
    Egress ACL meters:         18,   3% of maximum value    512
    Egress ACL slices:          2,  50% of maximum value      4
