---
title: Early Access Features
author: Cumulus Networks
weight: 97
aliases:
 - /display/NETQ21/Early+Access+Features
 - /pages/viewpage.action?pageId=10464121
pageID: 10464121
product: Cumulus NetQ
version: '2.1'
imgData: cumulus-netq-21
siteSlug: cumulus-netq-21
---
NetQ has [early access](https://support.cumulusnetworks.com/hc/en-us/articles/202933878-Early-Access-Features-Defined)
features that provide advanced access to new functionality before it
becomes generally available. The ability to view physical interface
statistics collected by the NetQ Agent is the only early access feature
available in NetQ 2.1.2.

This feature is bundled into the `netq-apps` package; there is no
specific EA package like there typically is with Cumulus Linux.

## Enable Early Access Features

You enable early access features by running the `netq config add experimental` command on any node running NetQ.

    cumulus@switch:~$ netq config add experimental
    Experimental config added

## View Interface Statistics

NetQ Agents collect performance statistics every 30 seconds for the
physical interfaces on switches and hosts in your network. The NetQ
Agent does not collect statistics for non-physical interfaces, such as
bonds, bridges, and VXLANs. After enabling the feature, the NetQ Agent
collects the following statistics:

  - **Transmit**: tx_bytes, tx_carrier, tx_colls, tx_drop, tx_errs, tx_packets
  - **Receive**: rx_bytes, rx_drop, rx_errs, rx_frame, rx_multicast, rx_packets

These can be viewed using the following NetQ CLI command:

    netq [<hostname>] show interface-stats [errors | all] [<physical-port>] [around <text-time>] [json]

Use the `hostname` option to limit the output to a particular switch.
Use the `errors` option to view only the transmit and receive errors
found on the designated interfaces. Use the `physical-port` option to
limit the output to a particular port. Use the `around` option to view
the data at a time in the past.

In this example, we view the interface statistics for all switches and
all of their physical interfaces.

    cumulus@switch:~$ netq show interface-stats
    Matching proc_dev_stats records:
    Hostname          Interface                 Duration         RX Bytes             RX Drop              RX Errors            TX Bytes             TX Drop              TX Errors            Last Changed
    ----------------- ------------------------- ---------------- -------------------- -------------------- -------------------- -------------------- -------------------- -------------------- -------------------------
    edge01            eth0                      30               2278                 0                    16                   4007                 0                    0                    Mon Jun  3 23:03:14 2019
    edge01            lo                        30               864                  0                    0                    864                  0                    0                    Mon Jun  3 23:03:14 2019
    exit01            bridge                    60               336                  0                    0                    1176                 0                    0                    Mon Jun  3 23:02:27 2019
    exit01            eth0                      30               3424                 0                    0                    6965                 0                    0                    Mon Jun  3 23:02:58 2019
    exit01            mgmt                      30               2682                 0                    0                    7488                 0                    0                    Mon Jun  3 23:02:58 2019
    exit01            swp44                     30               2457                 0                    0                    2457                 0                    0                    Mon Jun  3 23:02:58 2019
    exit01            swp51                     30               2462                 0                    0                    1769                 0                    0                    Mon Jun  3 23:02:58 2019
    exit01            swp52                     30               2634                 0                    0                    2629                 0                    0                    Mon Jun  3 23:02:58 2019
    exit01            vlan4001                  50               336                  0                    0                    1176                 0                    0                    Mon Jun  3 23:02:27 2019
    exit01            vrf1                      60               1344                 0                    0                    0                    0                    0                    Mon Jun  3 23:02:27 2019
    exit01            vxlan4001                 50               336                  0                    0                    1368                 0                    0                    Mon Jun  3 23:02:27 2019
    exit02            bridge                    61               1008                 0                    0                    392                  0                    0                    Mon Jun  3 23:03:07 2019
    exit02            eth0                      20               2711                 0                    0                    4983                 0                    0                    Mon Jun  3 23:03:07 2019
    exit02            mgmt                      30               2162                 0                    0                    5506                 0                    0                    Mon Jun  3 23:03:07 2019
    exit02            swp44                     20               3040                 0                    0                    3824                 0                    0                    Mon Jun  3 23:03:07 2019
    ...

## Disable Early Access Features

You disable the early access features by running the `netq config del experimental` command on any node running NetQ.

    cumulus@switch:~$ netq config del experimental
    Experimental config deleted
