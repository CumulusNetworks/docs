---
title: Resource Diagnostics Using cl-resource-query
author: Cumulus Networks
weight: 159
aliases:
 - /display/CL25ESR/Resource+Diagnostics+Using+cl-resource-query
 - /pages/viewpage.action?pageId=5115964
pageID: 5115964
product: Cumulus Linux
version: 2.5.12 ESR
imgData: cumulus-linux-2512-esr
siteSlug: cumulus-linux-2512-esr
---
You can use `cl-resource-query` to retrieve information about host
entries, MAC entries, L2 and L3 routes, and ECMPs (equal-cost multi-path
routes, see [Load
Balancing](Network_Topology.html#src-5116104_NetworkTopology-load_balancing))
that are in use. This is especially useful because Cumulus Linux syncs
routes between the kernel and the switching silicon. If the required
resource pools in hardware fill up, new kernel routes can cause existing
routes to move from being fully allocated to being partially allocated.

In order to avoid this, routes in the hardware should be monitored and
kept below the ASIC limits. For example, on systems with a Trident II
chipset, the limits are as follows:

    routes: 8092 <<<< if all routes are IPv6, or 16384 if all routes are IPv4
    long mask routes 2048 <<<< these are routes with a mask longer than the route mask limit
    route mask limit 64
    host_routes: 8192
    ecmp_nhs: 16346
    ecmp_nhs_per_route: 52

This translates to about 314 routes with ECMP next hops, if every route
has the maximum ECMP NHs.

For systems with a Trident+ chipset, the limits are as follows:

    routes: 16384 <<<< if all routes are IPv4
    long mask routes 256 <<<< these are routes with a mask longer than the route mask limit
    route mask limit 64
    host_routes: 8192
    ecmp_nhs: 4044
    ecmp_nhs_per_route: 52

This translates to about 77 routes with ECMP next hops, if every route
has the maximum ECMP NHs.

You can monitor this in Cumulus Linux with the `cl-resource-query`
command. Results vary between switches running on Trident+ and Trident
II chipsets.

`cl-resource-query` results for a Trident II switch:

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

`cl-resource-query` results for a Trident+ switch:

    cumulus@switch:~$ sudo cl-resource-query
    Host entries:               6,   0% of maximum value   4096 <<< same as above
    IPv4 neighbors:             6
    IPv6 neighbors:             0
    IPv4/IPv6 entries:         33,   0% of maximum value  16284
    Long IPv6 entries:          0,   0% of maximum value    256
    IPv4 Routes:               29
    IPv6 Routes:                2
    Total Routes:              31,   0% of maximum value  32768
    ECMP nexthops:              0,   0% of maximum value   4041
    MAC entries:                0,   0% of maximum value 131072
