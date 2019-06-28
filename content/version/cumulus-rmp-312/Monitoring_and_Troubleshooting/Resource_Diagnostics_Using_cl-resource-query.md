---
title: Resource Diagnostics Using cl-resource-query
author: Cumulus Networks
weight: 105
aliases:
 - /display/RMP31/Resource+Diagnostics+Using+cl-resource-query
 - /pages/viewpage.action?pageId=5122750
pageID: 5122750
product: Cumulus RMP
version: 3.1.2
imgData: cumulus-rmp-312
siteSlug: cumulus-rmp-312
---
You can use `cl-resource-query` to retrieve information about host
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
    Host entries:               1,   0% of maximum value   8192 <<<< this is the default software-imposed limit, 50% of the hardware limit
    IPv4 neighbors:             1         <<<< these are counts of the number of valid entries in the table
    IPv6 neighbors:             0
    IPv4 entries:              13,   0% of maximum value  32668
    IPv6 entries:              18,   0% of maximum value  16384
    IPv4 Routes:               13
    IPv6 Routes:               18
    Total Routes:              31,   0% of maximum value  32768
    MAC entries:               12,   0% of maximum value  32768
