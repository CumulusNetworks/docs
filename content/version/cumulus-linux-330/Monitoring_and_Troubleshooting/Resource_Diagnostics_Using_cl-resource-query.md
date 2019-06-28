---
title: Resource Diagnostics Using cl-resource-query
author: Cumulus Networks
weight: 201
aliases:
 - /display/CL330/Resource+Diagnostics+Using+cl-resource-query
 - /pages/viewpage.action?pageId=5866130
pageID: 5866130
product: Cumulus Linux
version: 3.3.0
imgData: cumulus-linux-330
siteSlug: cumulus-linux-330
---
You can use `cl-resource-query` to retrieve information about host
entries, MAC entries, L2 and L3 routes, and ECMPs (equal-cost multi-path
routes, see [Load
Balancing](Network_Topology.html#src-5866428_NetworkTopology-load_balancing))
that are in use. This is especially useful because Cumulus Linux syncs
routes between the kernel and the switching silicon. If the required
resource pools in hardware fill up, new kernel routes can cause existing
routes to move from being fully allocated to being partially allocated.

In order to avoid this, routes in the hardware should be monitored and
kept below the ASIC limits. For example, on systems with a Broadcom
Trident II chipset, the limits are as follows:

    routes: 8092 <<<< if all routes are IPv6, or 16384 if all routes are IPv4
    long mask routes 2048 <<<< these are routes with a mask longer than the route mask limit
    route mask limit 64
    host_routes: 8192
    ecmp_nhs: 16346
    ecmp_nhs_per_route: 52

This translates to about 314 routes with ECMP next hops, if every route
has the maximum ECMP NHs.

You can monitor this in Cumulus Linux with the `cl-resource-query`
command. Results vary between switches running on different chipsets.

`cl-resource-query` results for a Mellanox Spectrum switch:

    cumulus@switch:~$ sudo cl-resource-query
    Host entries:               2,   0% of maximum value   5120
    IPv4 neighbors:             2
    IPv6 neighbors:             0
    IPv4 entries:              33,   0% of maximum value  39936
    IPv6 entries:              13,   0% of maximum value  15360
    IPv4 Routes:               33
    IPv6 Routes:               13
    Total Routes:              46,   0% of maximum value  32768
    ECMP nexthops:              0,   0% of maximum value 209664
    MAC entries:               25,   0% of maximum value 409600

`cl-resource-query` results for a Broadcom Tomahawk switch:

    cumulus@switch:~$ sudo cl-resource-query
    Host entries:               1,   0% of maximum value  20480  <<< 2 IPv4 neighbors can use one entry
    IPv4 neighbors:             1
    IPv6 neighbors:             0
    IPv4 entries:               5,   0% of maximum value  32668  <<< switch overrides the SDK max limits
    IPv6 entries:               4,   0% of maximum value  16384  <<<
    IPv4 Routes:                5
    IPv6 Routes:                4
    Total Routes:               9,   0% of maximum value  32768
    ECMP nexthops:              0,   0% of maximum value  16350
    MAC entries:                2,   0% of maximum value  40960

`cl-resource-query` results for a Broadcom Trident II switch:

    cumulus@switch:~$ sudo cl-resource-query
    Host entries:               1,   0% of maximum value   8192 <<<< this is the default software-imposed limit, 50% of the hardware limit
    IPv4 neighbors:             1         <<<< these are counts of the number of valid entries in the table
    IPv6 neighbors:             0
    IPv4 entries:              13,   0% of maximum value  32668
    IPv6 entries:              18,   0% of maximum value  16384
    IPv4 Routes:               13
    IPv6 Routes:               18
    Total Routes:              31,   0% of maximum value  32768
    ECMP nexthops:              0,   0% of maximum value  16346
    MAC entries:               12,   0% of maximum value  32768
