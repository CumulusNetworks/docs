---
title: Utilization Stats
author: Cumulus Networks
weight: 
toc: 3
---


### View Interface Statistics and Utilization

NetQ Agents collect performance statistics every 30 seconds for the
physical interfaces on switches and hosts in your network. The NetQ
Agent does not collect statistics for non-physical interfaces, such as
bonds, bridges, and VXLANs. The NetQ Agent collects the following statistics:

- Statistics
    - **Transmit**: tx\_bytes, tx\_carrier, tx\_colls, tx\_drop, tx\_errs, tx\_packets
    - **Receive**: rx\_bytes, rx\_drop, rx\_errs, rx\_frame, rx\_multicast, rx\_packets
- Utilization
    - rx\_util, tx\_util
    - port speed

These can be viewed using the following NetQ CLI commands:

```
netq [<hostname>] show interface-stats [errors | all] [<physical-port>] [around <text-time>] [json]
netq [<hostname>] show interface-utilization [<text-port>] [tx|rx] [around <text-time>] [json]
```

Where the various options are:

- `hostname` limits the output to a particular switch
- `errors` limits the output to only the transmit and receive errors found on the designated interfaces
- `physical-port` limits the output to a particular port
- `around` enables viewing of the data at a time in the past
- `json` outputs results in JSON format
- `text-port` limits output to a particular host and port; `hostname` is required with this option
- `tx`, `rx` limits output to the transmit or receive values, respectively

In this example, we view the interface statistics for all switches and
all of their physical interfaces.

```
cumulus@switch:~$ netq show interface-stats
Matching proc_dev_stats records:
Hostname          Interface                 RX Packets           RX Drop              RX Errors            TX Packets           TX Drop              TX Errors            Last Updated
----------------- ------------------------- -------------------- -------------------- -------------------- -------------------- -------------------- -------------------- ------------------------
border01          swp1                      0                    0                    0                    0                    0                    0                    Wed Apr 22 23:56:48 2020
border01          swp54                     82660                0                    0                    81630                0                    0                    Wed Apr 22 23:56:48 2020
border01          swp52                     83115                0                    0                    81491                0                    0                    Wed Apr 22 23:56:48 2020
border01          swp4                      0                    0                    0                    0                    0                    0                    Wed Apr 22 23:56:48 2020
border01          swp53                     77128                0                    0                    70080                0                    0                    Wed Apr 22 23:56:48 2020
border01          swp3                      183252               0                    0                    168795               0                    0                    Wed Apr 22 23:56:48 2020
border01          swp49                     396524               0                    0                    324746               0                    0                    Wed Apr 22 23:56:48 2020
border01          swp51                     80054                1                    0                    82420                0                    0                    Wed Apr 22 23:56:48 2020
border01          swp2                      0                    0                    0                    0                    0                    0                    Wed Apr 22 23:56:48 2020
border01          swp50                     179866               0                    0                    178564               0                    0                    Wed Apr 22 23:56:48 2020
border02          swp1                      0                    0                    0                    0                    0                    0                    Wed Apr 22 23:57:12 2020
border02          swp54                     75295                0                    0                    69453                0                    0                    Wed Apr 22 23:57:12 2020
border02          swp52                     83255                0                    0                    82895                0                    0                    Wed Apr 22 23:57:12 2020
border02          swp4                      0                    0                    0                    0                    0                    0                    Wed Apr 22 23:57:12 2020
...
```

In this example, we view the interface statistics for switch port 1.

```
cumulus@switch:~$ netq show interface-stats swp1

Matching proc_dev_stats records:
Hostname          Interface                 RX Packets           RX Drop              RX Errors            TX Packets           TX Drop              TX Errors            Last Updated
----------------- ------------------------- -------------------- -------------------- -------------------- -------------------- -------------------- -------------------- ------------------------
border01          swp1                      0                    0                    0                    0                    0                    0                    Wed Apr 22 23:56:18 2020
border02          swp1                      0                    0                    0                    0                    0                    0                    Wed Apr 22 23:56:11 2020
fw1               swp1                      163602               11                   0                    106430               0                    0                    Wed Apr 22 23:56:22 2020
fw2               swp1                      0                    0                    0                    0                    0                    0                    Wed Apr 22 23:56:07 2020
leaf01            swp1                      104053               1                    0                    160584               0                    0                    Wed Apr 22 23:56:18 2020
leaf02            swp1                      104271               1                    0                    109072               0                    0                    Wed Apr 22 23:56:28 2020
leaf03            swp1                      177346               3                    0                    106817               0                    0                    Wed Apr 22 23:56:25 2020
leaf04            swp1                      183301               9                    0                    107134               0                    0                    Wed Apr 22 23:56:26 2020
spine01           swp1                      83887                0                    0                    83131                0                    0                    Wed Apr 22 23:56:03 2020
spine02           swp1                      99007                0                    0                    85146                0                    0                    Wed Apr 22 23:56:31 2020
spine03           swp1                      88968                0                    0                    81558                0                    0                    Wed Apr 22 23:56:13 2020
spine04           swp1                      88795                0                    0                    75526                0                    0                    Wed Apr 22 23:56:27 2020
```

In this example, we view the utilization for the leaf03 switch.

```
cumulus@switch:~$ netq leaf03 show interface-utilization
Matching port_stats records:
Hostname          Interface                 RX Bytes (30sec)     RX Drop (30sec)      RX Errors (30sec)    RX Util (%age)       TX Bytes (30sec)     TX Drop (30sec)      TX Errors (30sec)    TX Util (%age)       Port Speed           Last Changed
----------------- ------------------------- -------------------- -------------------- -------------------- -------------------- -------------------- -------------------- -------------------- -------------------- -------------------- --------------------
leaf03            swp1                      3937                 0                    0                    0                    4933                 0                    0                    0                    1G                   Fri Apr 24 09:35:51
                                                                                                                                                                                                                                         2020
leaf03            swp54                     2459                 0                    0                    0                    2459                 0                    0                    0                    1G                   Fri Apr 24 09:35:51
                                                                                                                                                                                                                                         2020
leaf03            swp52                     2459                 0                    0                    0                    2459                 0                    0                    0                    1G                   Fri Apr 24 09:35:51
                                                                                                                                                                                                                                         2020
leaf03            swp53                     2545                 0                    0                    0                    2545                 0                    0                    0                    1G                   Fri Apr 24 09:35:51
                                                                                                                                                                                                                                         2020
leaf03            swp3                      3937                 0                    0                    0                    4962                 0                    0                    0                    1G                   Fri Apr 24 09:35:51
                                                                                                                                                                                                                                         2020
leaf03            swp49                     27858                0                    0                    0                    7732                 0                    0                    0                    1G                   Fri Apr 24 09:35:51
                                                                                                                                                                                                                                         2020
leaf03            swp51                     1599                 0                    0                    0                    2459                 0                    0                    0                    1G                   Fri Apr 24 09:35:51
                                                                                                                                                                                                                                         2020
leaf03            swp2                      3985                 0                    0                    0                    4924                 0                    0                    0                    1G                   Fri Apr 24 09:35:51
                                                                                                                                                                                                                                         2020
leaf03            swp50                     7575                 0                    0                    0                    28221                0                    0                    0                    1G                   Fri Apr 24 09:35:51
```

In this example, we view the transmit utilization only.

```
cumulus@switch:~$ netq show interface-utilization tx

Matching port_stats records:
Hostname          Interface                 TX Bytes (30sec)     TX Drop (30sec)      TX Errors (30sec)    TX Util (%age)       Port Speed           Last Changed
----------------- ------------------------- -------------------- -------------------- -------------------- -------------------- -------------------- --------------------
border01          swp1                      0                    0                    0                    0                    Unknown              Fri Apr 24 09:33:20
                                                                                                                                                     2020
border01          swp54                     2461                 0                    0                    0                    1G                   Fri Apr 24 09:33:20
                                                                                                                                                     2020
border02          swp1                      0                    0                    0                    0                    Unknown              Fri Apr 24 09:33:05
                                                                                                                                                     2020
border02          swp54                     2461                 0                    0                    0                    1G                   Fri Apr 24 09:33:05
                                                                                                                                                     2020
border02          swp52                     2461                 0                    0                    0                    1G                   Fri Apr 24 09:33:05
                                                                                                                                                     2020
border02          swp4                      0                    0                    0                    0                    Unknown              Fri Apr 24 09:33:05
                                                                                                                                                     2020
border02          swp53                     2566                 0                    0                    0                    1G                   Fri Apr 24 09:33:05
                                                                                                                                                     2020
leaf02            swp1                      4209                 0                    0                    0                    1G                   Fri Apr 24 09:33:08
                                                                                                                                                     2020
leaf02            swp54                     2459                 0                    0                    0                    1G                   Fri Apr 24 09:33:08
                                                                                                                                                     2020
```

### View Switch Resource Utilization

You can quickly determine how many compute resources &mdash; CPU, disk and
memory &mdash; are being consumed by the switches on your network. Run the
`netq show resource-util` command to see the percentage of CPU and memory
being consumed as well as the amount and percentage of disk space being
consumed.

You can use the `around` option to view the information for a particular time.

```
cumulus@switch:~$ netq show resource-util

Matching resource_util records:
Hostname          CPU Utilization      Memory Utilization   Disk Name            Total                Used                 Disk Utilization     Last Updated
----------------- -------------------- -------------------- -------------------- -------------------- -------------------- -------------------- ------------------------
exit01            9.2                  48                   /dev/vda4            6170849280           1524920320           26.8                 Wed Feb 12 03:54:10 2020
exit02            9.6                  47.6                 /dev/vda4            6170849280           1539346432           27.1                 Wed Feb 12 03:54:22 2020
leaf01            9.8                  50.5                 /dev/vda4            6170849280           1523818496           26.8                 Wed Feb 12 03:54:25 2020
leaf02            10.9                 49.4                 /dev/vda4            6170849280           1535246336           27                   Wed Feb 12 03:54:11 2020
leaf03            11.4                 49.4                 /dev/vda4            6170849280           1536798720           27                   Wed Feb 12 03:54:10 2020
leaf04            11.4                 49.4                 /dev/vda4            6170849280           1522495488           26.8                 Wed Feb 12 03:54:03 2020
spine01           8.4                  50.3                 /dev/vda4            6170849280           1522249728           26.8                 Wed Feb 12 03:54:19 2020
spine02           9.8                  49                   /dev/vda4            6170849280           1522003968           26.8                 Wed Feb 12 03:54:25 2020
```

You can focus on a specific switch by including the hostname in your query:

```
cumulus@switch:~$ netq leaf01 show resource-util

Matching resource_util records:
Hostname          CPU Utilization      Memory Utilization   Disk Name            Total                Used                 Disk Utilization     Last Updated
----------------- -------------------- -------------------- -------------------- -------------------- -------------------- -------------------- ------------------------
leaf01            9.8                  49.9                 /dev/vda4            6170849280           1524314112           26.8                 Wed Feb 12 04:35:05 2020
```

### View CPU Utilization

You can quickly determine what percentage of CPU resources are being consumed
by the switches on your network. Run the `netq show resource-util cpu` command.

You can use the `around` option to view the information for a particular time.

```
cumulus@switch:~$ netq show resource-util cpu

Matching resource_util records:
Hostname          CPU Utilization      Last Updated
----------------- -------------------- ------------------------
exit01            8.9                  Wed Feb 12 04:29:29 2020
exit02            8.3                  Wed Feb 12 04:29:22 2020
leaf01            10.9                 Wed Feb 12 04:29:24 2020
leaf02            11.6                 Wed Feb 12 04:29:10 2020
leaf03            9.8                  Wed Feb 12 04:29:33 2020
leaf04            11.7                 Wed Feb 12 04:29:29 2020
spine01           10.4                 Wed Feb 12 04:29:38 2020
spine02           9.7                  Wed Feb 12 04:29:15 2020
```

You can focus on a specific switch by including the hostname in your query:

```
cumulus@switch:~$ netq leaf01 show resource-util cpu

Matching resource_util records:
Hostname          CPU Utilization      Last Updated
----------------- -------------------- ------------------------
leaf01            11.1                 Wed Feb 12 04:16:18 2020
```

### View Disk Utilization

You can quickly determine how much storage, in bytes and in percentage of disk
space, is being consumed by the switches on your network. Run the
`netq show resource-util disk` command.

You can use the `around` option to view the information for a particular time.

```
cumulus@switch:~$ netq show resource-util disk

Matching resource_util records:
Hostname          Disk Name            Total                Used                 Disk Utilization     Last Updated
----------------- -------------------- -------------------- -------------------- -------------------- ------------------------
exit01            /dev/vda4            6170849280           1525309440           26.8                 Wed Feb 12 04:29:29 2020
exit02            /dev/vda4            6170849280           1539776512           27.1                 Wed Feb 12 04:29:22 2020
leaf01            /dev/vda4            6170849280           1524203520           26.8                 Wed Feb 12 04:29:24 2020
leaf02            /dev/vda4            6170849280           1535631360           27                   Wed Feb 12 04:29:41 2020
leaf03            /dev/vda4            6170849280           1537191936           27.1                 Wed Feb 12 04:29:33 2020
leaf04            /dev/vda4            6170849280           1522864128           26.8                 Wed Feb 12 04:29:29 2020
spine01           /dev/vda4            6170849280           1522688000           26.8                 Wed Feb 12 04:29:38 2020
spine02           /dev/vda4            6170849280           1522409472           26.8                 Wed Feb 12 04:29:46 2020
```

You can focus on a specific switch and disk drive by including the hostname
and device name in your query:

```
cumulus@switch:~$ netq leaf01 show resource-util disk /dev/vda4

Matching resource_util records:
Hostname          Disk Name            Total                Used                 Disk Utilization     Last Updated
----------------- -------------------- -------------------- -------------------- -------------------- ------------------------
leaf01            /dev/vda4            6170849280           1524064256           26.8                 Wed Feb 12 04:15:45 2020
```

### View Memory Utilization

You can quickly determine what percentage of memory resources are being consumed
by the switches on your network. Run the `netq show resource-util memory` command.

You can use the `around` option to view the information for a particular time.

```
cumulus@switch:~$ netq show resource-util memory

Matching resource_util records:
Hostname          Memory Utilization   Last Updated
----------------- -------------------- ------------------------
exit01            48.8                 Wed Feb 12 04:29:29 2020
exit02            49.7                 Wed Feb 12 04:29:22 2020
leaf01            49.8                 Wed Feb 12 04:29:24 2020
leaf02            49.5                 Wed Feb 12 04:29:10 2020
leaf03            50.7                 Wed Feb 12 04:29:33 2020
leaf04            49.3                 Wed Feb 12 04:29:29 2020
spine01           47.5                 Wed Feb 12 04:29:07 2020
spine02           49.2                 Wed Feb 12 04:29:15 2020
```

You can focus on a specific switch by including the hostname in your query:

```
cumulus@switch:~$ netq leaf01 show resource-util memory

Matching resource_util records:
Hostname          Memory Utilization   Last Updated
----------------- -------------------- ------------------------
leaf01            49.8                 Wed Feb 12 04:16:18 2020
```

### View SSD Utilization

For NetQ servers and appliances that have 3ME3 solid state drives (SSDs) installed (primarily in on-premises deployments), you can view the utilization of the drive on-demand. An alarm is generated for drives that drop below 10% health, or have more than a two percent loss of health in 24 hours, indicating the need to rebalance the drive. Tracking SSD utilization over time enables you to see any downward trend or instability of the drive before you receive an alarm.

Use the `netq show cl-ssd-util` command to view the SSD information.

This example shows the utilization for spine02 which has this type of SSD.

```
cumulus@switch:~$ netq spine02 show cl-ssd-util
Hostname        Remaining PE Cycle (%)  Current PE Cycles executed      Total PE Cycles supported       SSD Model               Last Changed
spine02         80                      576                             2880                            M.2 (S42) 3ME3          Thu Oct 31 00:15:06 2019
```

This output indicates that this drive is in a good state overall with 80% of its PE cycles remaining. View this information for all devices with this type of SSD by removing the `hostname` option, or add the `around` option to view this information around a particular time.

### View Disk Storage Utilization After BTRFS Allocation

Customers running Cumulus Linux 3.x which uses the BTRFS (b-tree file system) might experience issues with disk space management. This is a known problem of BTRFS because it does not perform periodic garbage collection, or rebalancing. If left unattended, these errors can make it impossible to rebalance the partitions on the disk. To avoid this issue, Cumulus Networks recommends rebalancing the BTRFS partitions in a preemptive manner, but only when absolutely needed to avoid reduction in the lifetime of the disk. By tracking the state of the disk space usage, users can determine when rebalancing should be performed. Refer to {{<exlink url="https://support.cumulusnetworks.com/hc/en-us/articles/360037394933-When-to-Rebalance-BTRFS-Partitions" text="When to Rebalance BTRFS Partitions">}} for details about the rules used to recommend a rebalance operation.

To view the disk utilization and whether a rebalance is recommended, use the `netq show cl-btrfs-util` command as follows:

```
cumulus@switch:~$ netq show cl-btrfs-info
Matching btrfs_info records:
Hostname          Device Allocated     Unallocated Space    Largest Chunk Size   Unused Data Chunks S Rebalance Recommende Last Changed
                                                                                 pace                 d
----------------- -------------------- -------------------- -------------------- -------------------- -------------------- -------------------------
exit01            31.16 %              3.96 GB              588.5 MB             39.13 MB             no                   Wed Oct 30 18:51:35 2019
exit02            31.16 %              3.96 GB              588.5 MB             38.79 MB             no                   Wed Oct 30 19:20:41 2019
leaf01            31.16 %              3.96 GB              588.5 MB             38.75 MB             no                   Wed Oct 30 18:52:34 2019
leaf02            31.16 %              3.96 GB              588.5 MB             38.79 MB             no                   Wed Oct 30 18:51:22 2019
leaf03            31.16 %              3.96 GB              588.5 MB             35.44 MB             no                   Wed Oct 30 18:52:02 2019
leaf04            31.16 %              3.96 GB              588.5 MB             33.49 MB             no                   Wed Oct 30 19:21:15 2019
spine01           31.16 %              3.96 GB              588.5 MB             36.9 MB              no                   Wed Oct 30 19:21:13 2019
spine02           31.16 %              3.96 GB              588.5 MB             39.12 MB             no                   Wed Oct 30 18:52:44 2019
```

Look for the **Rebalance Recommended** column. If the value in that column says *Yes*, then you are strongly encouraged to rebalance the BTRFS partitions. If it says *No*, then you can review the other values in the output to determine if you are getting close to needing a rebalance, and come back to view this data at a later time.

Optionally, use the `hostname` option to view the information for a given device, or use the `around` option to view the information for a particular time.