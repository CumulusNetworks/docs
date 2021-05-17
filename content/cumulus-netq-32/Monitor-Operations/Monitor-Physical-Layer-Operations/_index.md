---
title: Monitor Physical Layer Operations
author: Cumulus Networks
weight: 850
toc: 3
---
With NetQ, a network administrator can monitor OSI Layer 1 physical
components on network devices, including interfaces, ports, links, and
peers. Keeping track of the various physical layer components in your switches
and servers ensures you have a fully functioning network and provides
inventory management and audit capabilities. You can monitor ports,
transceivers, and cabling deployed on a per port (interface), per
vendor, per part number and so forth. NetQ enables you to view the
current status and the status an earlier point in time. From this
information, you can, among other things:

- Determine which ports are empty versus which ones have cables
  plugged in and thereby validate expected connectivity
- Audit transceiver and cable components used by vendor, giving you
  insights for estimated replacement costs, repair costs, overall
  costs, and so forth to improve your maintenance and purchasing
  processes
- Identify mismatched links
- Identify changes in your physical layer, and when they occurred, indicating such items as bonds and links going down or flapping

NetQ uses [LLDP]({{<ref "/cumulus-linux-43/Layer-2/Link-Layer-Discovery-Protocol" >}}) (Link Layer Discovery Protocol) to collect port information. NetQ can also identify peer ports connected to DACs (Direct Attached Cables) and AOCs (Active Optical Cables) without using LLDP, even if the link is not UP.

## View Component Information

You can view performance and status information about cables, transceiver modules, and interfaces using the `netq show interfaces physical` command. Its syntax is:

```
netq [<hostname>] show interfaces physical [<physical-port>] [empty|plugged] [peer] [vendor <module-vendor>|model <module-model>|module] [around <text-time>] [json]
```

{{<notice note>}}

When entering a time value, you must include a numeric value <em>and</em> the unit of measure:
<ul>
<li><strong>d</strong>: day(s)</li>
<li><strong>w</strong>: week(s)</li>
<li><strong>h</strong>: hour(s)</li>
<li><strong>m</strong>: minute(s)</li>
<li><strong>s</strong>: second(s)</li>
<li><strong>now</strong></li>
</ul>
For the <code>between</code> option, the start (<code>text-time</code>) and end time (<code>text-endtime</code>) values can be entered as most recent first and least recent second, or vice versa. The values do not have to have the same unit of measure.

{{</notice>}}

### View Detailed Cable Information for All Devices

You can view what cables are connected to each interface port for all devices, including the module type, vendor, part number and performance characteristics. You can also view the cable information for a given device by adding a hostname to the `show` command.

This example shows cable information and status for all interface ports on all devices.

```
cumulus@switch:~$ netq show interfaces physical
Matching cables records:
Hostname          Interface                 State      Speed      AutoNeg Module    Vendor               Part No          Last Changed
----------------- ------------------------- ---------- ---------- ------- --------- -------------------- ---------------- -------------------------
border01          vagrant                   down       Unknown    off     RJ45      n/a                  n/a              Fri Sep 18 20:08:05 2020
border01          swp54                     up         1G         off     RJ45      n/a                  n/a              Fri Sep 18 20:08:05 2020
border01          swp49                     up         1G         off     RJ45      n/a                  n/a              Fri Sep 18 20:08:05 2020
border01          swp2                      down       Unknown    off     RJ45      n/a                  n/a              Fri Sep 18 20:08:05 2020
border01          swp3                      up         1G         off     RJ45      n/a                  n/a              Fri Sep 18 20:08:05 2020
border01          swp52                     up         1G         off     RJ45      n/a                  n/a              Fri Sep 18 20:08:05 2020
border01          swp1                      down       Unknown    off     RJ45      n/a                  n/a              Fri Sep 18 20:08:05 2020
border01          swp53                     up         1G         off     RJ45      n/a                  n/a              Fri Sep 18 20:08:05 2020
border01          swp4                      down       Unknown    off     RJ45      n/a                  n/a              Fri Sep 18 20:08:05 2020
border01          swp50                     up         1G         off     RJ45      n/a                  n/a              Fri Sep 18 20:08:05 2020
border01          eth0                      up         1G         off     RJ45      n/a                  n/a              Fri Sep 18 20:08:05 2020
border01          swp51                     up         1G         off     RJ45      n/a                  n/a              Fri Sep 18 20:08:05 2020
border02          swp49                     up         1G         off     RJ45      n/a                  n/a              Thu Sep 17 21:07:54 2020
border02          swp54                     up         1G         off     RJ45      n/a                  n/a              Thu Sep 17 21:07:54 2020
border02          swp52                     up         1G         off     RJ45      n/a                  n/a              Thu Sep 17 21:07:54 2020
border02          swp53                     up         1G         off     RJ45      n/a                  n/a              Thu Sep 17 21:07:54 2020
border02          swp4                      down       Unknown    off     RJ45      n/a                  n/a              Thu Sep 17 21:07:54 2020
border02          swp3                      up         1G         off     RJ45      n/a                  n/a              Thu Sep 17 21:07:54 2020
border02          vagrant                   down       Unknown    off     RJ45      n/a                  n/a              Thu Sep 17 21:07:54 2020
border02          swp1                      down       Unknown    off     RJ45      n/a                  n/a              Thu Sep 17 21:07:54 2020
border02          swp2                      down       Unknown    off     RJ45      n/a                  n/a              Thu Sep 17 21:07:54 2020
border02          swp51                     up         1G         off     RJ45      n/a                  n/a              Thu Sep 17 21:07:54 2020
border02          swp50                     up         1G         off     RJ45      n/a                  n/a              Thu Sep 17 21:07:54 2020
border02          eth0                      up         1G         off     RJ45      n/a                  n/a              Thu Sep 17 21:07:54 2020
fw1               swp49                     down       Unknown    off     RJ45      n/a                  n/a              Thu Sep 17 21:07:37 2020
fw1               eth0                      up         1G         off     RJ45      n/a                  n/a              Thu Sep 17 21:07:37 2020
fw1               swp1                      up         1G         off     RJ45      n/a                  n/a              Thu Sep 17 21:07:37 2020
fw1               swp2                      up         1G         off     RJ45      n/a                  n/a              Thu Sep 17 21:07:37 2020
fw1               vagrant                   down       Unknown    off     RJ45      n/a                  n/a              Thu Sep 17 21:07:37 2020
fw2               vagrant                   down       Unknown    off     RJ45      n/a                  n/a              Thu Sep 17 21:07:38 2020
fw2               eth0                      up         1G         off     RJ45      n/a                  n/a              Thu Sep 17 21:07:38 2020
fw2               swp49                     down       Unknown    off     RJ45      n/a                  n/a              Thu Sep 17 21:07:38 2020
fw2               swp2                      down       Unknown    off     RJ45      n/a                  n/a              Thu Sep 17 21:07:38 2020
fw2               swp1                      down       Unknown    off     RJ45      n/a                  n/a              Thu Sep 17 21:07:38 2020
...
```

### View Detailed Module Information for a Given Device

You can view detailed information about the transceiver modules on each interface port, including serial number, transceiver type, connector and attached cable length. You can also view the module information for a given device by adding a hostname to the `show` command.

This example shows the detailed module information for the interface ports on *leaf02* switch.

```
cumulus@switch:~$ netq leaf02 show interfaces physical module
Matching cables records are:
Hostname          Interface                 Module    Vendor               Part No          Serial No                 Transceiver      Connector        Length Last Changed
----------------- ------------------------- --------- -------------------- ---------------- ------------------------- ---------------- ---------------- ------ -------------------------
leaf02            swp1                      RJ45      n/a                  n/a              n/a                       n/a              n/a              n/a    Thu Feb  7 22:49:37 2019
leaf02            swp2                      SFP       Mellanox             MC2609130-003    MT1507VS05177             1000Base-CX,Copp Copper pigtail   3m     Thu Feb  7 22:49:37 2019
                                                                                                                        er Passive,Twin
                                                                                                                        Axial Pair (TW)
leaf02            swp47                     QSFP+     CISCO                AFBR-7IER05Z-CS1 AVE1823402U               n/a              n/a              5m     Thu Feb  7 22:49:37 2019
leaf02            swp48                     QSFP28    TE Connectivity      2231368-1        15250052                  100G Base-CR4 or n/a              3m     Thu Feb  7 22:49:37 2019
                                                                                                                        25G Base-CR CA-L
                                                                                                                        ,40G Base-CR4               
leaf02            swp49                     SFP       OEM                  SFP-10GB-LR      ACSLR130408               10G Base-LR      LC               10km,  Thu Feb  7 22:49:37 2019
                                                                                                                                                        10000m
leaf02            swp50                     SFP       JDSU                 PLRXPLSCS4322N   CG03UF45M                 10G Base-SR,Mult LC               80m,   Thu Feb  7 22:49:37 2019
                                                                                                                        imode,                            30m,  
                                                                                                                        50um (M5),Multim                  300m  
                                                                                                                        ode,            
                                                                                                                        62.5um (M6),Shor
                                                                                                                        twave laser w/o
                                                                                                                        OFC (SN),interme
                                                                                                                        diate distance (
                                                                                                                        I)              
leaf02            swp51                     SFP       Mellanox             MC2609130-003    MT1507VS05177             1000Base-CX,Copp Copper pigtail   3m     Thu Feb  7 22:49:37 2019
                                                                                                                        er Passive,Twin
                                                                                                                        Axial Pair (TW)
leaf02            swp52                     SFP       FINISAR CORP.        FCLF8522P2BTL    PTN1VH2                   1000Base-T       RJ45             100m   Thu Feb  7 22:49:37 2019
```

### View Ports without Cables Connected for a Given Device

Checking for empty ports enables you to compare expected versus actual deployment. This can be very helpful during deployment or during upgrades. You can also view the cable information for a given device by adding a hostname to the `show` command.

This example shows the ports that are empty on *leaf01* switch:

```
cumulus@switch:~$ netq leaf01 show interfaces physical empty
Matching cables records are:
Hostname         Interface State Speed      AutoNeg Module    Vendor           Part No          Last Changed
---------------- --------- ----- ---------- ------- --------- ---------------- ---------------- ------------------------
leaf01           swp49     down  Unknown    on      empty     n/a              n/a              Thu Feb  7 22:49:37 2019
leaf01           swp52     down  Unknown    on      empty     n/a              n/a              Thu Feb  7 22:49:37 2019
```

### View Ports with Cables Connected for a Given Device

In a similar manner as checking for empty ports, you can check for ports that have cables connected, enabling you to compare expected versus actual deployment. You can also view the cable information for a given device by adding a hostname to the `show` command. If you add the around keyword, you can view which interface ports had cables connected at a previous time.

This example shows the ports of *leaf01* switch that have attached cables.

```
cumulus@switch:~$ netq leaf01 show interfaces physical plugged
Matching cables records:
Hostname          Interface                 State      Speed      AutoNeg Module    Vendor               Part No          Last Changed
----------------- ------------------------- ---------- ---------- ------- --------- -------------------- ---------------- -------------------------
leaf01            eth0                      up         1G         on      RJ45      n/a                  n/a              Thu Feb  7 22:49:37 2019
leaf01            swp1                      up         10G        off     SFP       Amphenol             610640005        Thu Feb  7 22:49:37 2019
leaf01            swp2                      up         10G        off     SFP       Amphenol             610640005        Thu Feb  7 22:49:37 2019
leaf01            swp3                      down       10G        off     SFP       Mellanox             MC3309130-001    Thu Feb  7 22:49:37 2019
leaf01            swp33                     down       10G        off     SFP       OEM                  SFP-H10GB-CU1M   Thu Feb  7 22:49:37 2019
leaf01            swp34                     down       10G        off     SFP       Amphenol             571540007        Thu Feb  7 22:49:37 2019
leaf01            swp35                     down       10G        off     SFP       Amphenol             571540007        Thu Feb  7 22:49:37 2019
leaf01            swp36                     down       10G        off     SFP       OEM                  SFP-H10GB-CU1M   Thu Feb  7 22:49:37 2019
leaf01            swp37                     down       10G        off     SFP       OEM                  SFP-H10GB-CU1M   Thu Feb  7 22:49:37 2019
leaf01            swp38                     down       10G        off     SFP       OEM                  SFP-H10GB-CU1M   Thu Feb  7 22:49:37 2019
leaf01            swp39                     down       10G        off     SFP       Amphenol             571540007        Thu Feb  7 22:49:37 2019
leaf01            swp40                     down       10G        off     SFP       Amphenol             571540007        Thu Feb  7 22:49:37 2019
leaf01            swp49                     up         40G        off     QSFP+     Amphenol             624410001        Thu Feb  7 22:49:37 2019
leaf01            swp5                      down       10G        off     SFP       Amphenol             571540007        Thu Feb  7 22:49:37 2019
leaf01            swp50                     down       40G        off     QSFP+     Amphenol             624410001        Thu Feb  7 22:49:37 2019
leaf01            swp51                     down       40G        off     QSFP+     Amphenol             603020003        Thu Feb  7 22:49:37 2019
leaf01            swp52                     up         40G        off     QSFP+     Amphenol             603020003        Thu Feb  7 22:49:37 2019
leaf01            swp54                     down       40G        off     QSFP+     Amphenol             624410002        Thu Feb  7 22:49:37 2019
```

### View Components from a Given Vendor

By filtering for a specific cable vendor, you can collect information such as how many ports use components from that vendor and when they were last updated. This information may be useful when you run a cost analysis of your network. 

This example shows all the ports that are using components by an *OEM* vendor.

```
cumulus@switch:~$ netq leaf01 show interfaces physical vendor OEM
Matching cables records:
Hostname          Interface                 State      Speed      AutoNeg Module    Vendor               Part No          Last Changed
----------------- ------------------------- ---------- ---------- ------- --------- -------------------- ---------------- -------------------------
leaf01            swp33                     down       10G        off     SFP       OEM                  SFP-H10GB-CU1M   Thu Feb  7 22:49:37 2019
leaf01            swp36                     down       10G        off     SFP       OEM                  SFP-H10GB-CU1M   Thu Feb  7 22:49:37 2019
leaf01            swp37                     down       10G        off     SFP       OEM                  SFP-H10GB-CU1M   Thu Feb  7 22:49:37 2019
leaf01            swp38                     down       10G        off     SFP       OEM                  SFP-H10GB-CU1M   Thu Feb  7 22:49:37 2019
```

### View All Devices Using a Given Component

You can view all of the devices with ports using a particular component. This could be helpful when you need to change out a particular component for possible failure issues, upgrades, or cost reasons.

This example first determines which models (part numbers) exist on all of the devices
and then those devices with a part number of QSFP-H40G-CU1M installed.

```
cumulus@switch:~$ netq show interfaces physical model
    2231368-1         :  2231368-1
    624400001         :  624400001
    QSFP-H40G-CU1M    :  QSFP-H40G-CU1M
    QSFP-H40G-CU1MUS  :  QSFP-H40G-CU1MUS
    n/a               :  n/a

cumulus@switch:~$ netq show interfaces physical model QSFP-H40G-CU1M
Matching cables records:
Hostname          Interface                 State      Speed      AutoNeg Module    Vendor               Part No          Last Changed
----------------- ------------------------- ---------- ---------- ------- --------- -------------------- ---------------- -------------------------
leaf01            swp50                     up         1G         off     QSFP+     OEM                  QSFP-H40G-CU1M   Thu Feb  7 18:31:20 2019
leaf02            swp52                     up         1G         off     QSFP+     OEM                  QSFP-H40G-CU1M   Thu Feb  7 18:31:20 2019
```

### View Changes to Physical Components

Because components are often changed, NetQ enables you to determine what, if any, changes have been made to the physical components on your devices. This can be helpful during deployments or upgrades.

You can select how far back in time you want to go, or select a time range using the between keyword. Note that time values must include units to be valid. If no changes are found, a "No matching cable records found" message is displayed.

This example illustrates each of these scenarios for all devices in the network.

```
cumulus@switch:~$ netq show events type interfaces-physical between now and 30d
Matching cables records:
Hostname          Interface                 State      Speed      AutoNeg Module    Vendor               Part No          Last Changed
----------------- ------------------------- ---------- ---------- ------- --------- -------------------- ---------------- -------------------------
leaf01            swp1                      up         1G         off     SFP       AVAGO                AFBR-5715PZ-JU1  Thu Feb  7 18:34:20 2019
leaf01            swp2                      up         10G        off     SFP       OEM                  SFP-10GB-LR      Thu Feb  7 18:34:20 2019
leaf01            swp47                     up         10G        off     SFP       JDSU                 PLRXPLSCS4322N   Thu Feb  7 18:34:20 2019
leaf01            swp48                     up         40G        off     QSFP+     Mellanox             MC2210130-002    Thu Feb  7 18:34:20 2019
leaf01            swp49                     down       10G        off     empty     n/a                  n/a              Thu Feb  7 18:34:20 2019
leaf01            swp50                     up         1G         off     SFP       FINISAR CORP.        FCLF8522P2BTL    Thu Feb  7 18:34:20 2019
leaf01            swp51                     up         1G         off     SFP       FINISAR CORP.        FTLF1318P3BTL    Thu Feb  7 18:34:20 2019
leaf01            swp52                     down       1G         off     SFP       CISCO-AGILENT        QFBR-5766LP      Thu Feb  7 18:34:20 2019
leaf02            swp1                      up         1G         on      RJ45      n/a                  n/a              Thu Feb  7 18:34:20 2019
leaf02            swp2                      up         10G        off     SFP       Mellanox             MC2609130-003    Thu Feb  7 18:34:20 2019
leaf02            swp47                     up         10G        off     QSFP+     CISCO                AFBR-7IER05Z-CS1 Thu Feb  7 18:34:20 2019
leaf02            swp48                     up         10G        off     QSFP+     Mellanox             MC2609130-003    Thu Feb  7 18:34:20 2019
leaf02            swp49                     up         10G        off     SFP       FIBERSTORE           SFP-10GLR-31     Thu Feb  7 18:34:20 2019
leaf02            swp50                     up         1G         off     SFP       OEM                  SFP-GLC-T        Thu Feb  7 18:34:20 2019
leaf02            swp51                     up         10G        off     SFP       Mellanox             MC2609130-003    Thu Feb  7 18:34:20 2019
leaf02            swp52                     up         1G         off     SFP       FINISAR CORP.        FCLF8522P2BTL    Thu Feb  7 18:34:20 2019
leaf03            swp1                      up         10G        off     SFP       Mellanox             MC2609130-003    Thu Feb  7 18:34:20 2019
leaf03            swp2                      up         10G        off     SFP       Mellanox             MC3309130-001    Thu Feb  7 18:34:20 2019
leaf03            swp47                     up         10G        off     SFP       CISCO-AVAGO          AFBR-7IER05Z-CS1 Thu Feb  7 18:34:20 2019
leaf03            swp48                     up         10G        off     SFP       Mellanox             MC3309130-001    Thu Feb  7 18:34:20 2019
leaf03            swp49                     down       1G         off     SFP       FINISAR CORP.        FCLF8520P2BTL    Thu Feb  7 18:34:20 2019
leaf03            swp50                     up         1G         off     SFP       FINISAR CORP.        FCLF8522P2BTL    Thu Feb  7 18:34:20 2019
leaf03            swp51                     up         10G        off     QSFP+     Mellanox             MC2609130-003    Thu Feb  7 18:34:20 2019
...
oob-mgmt-server   swp1                      up         1G         off     RJ45      n/a                  n/a              Thu Feb  7 18:34:20 2019
oob-mgmt-server   swp2                      up         1G         off     RJ45      n/a                  n/a              Thu Feb  7 18:34:20 2019

cumulus@switch:~$ netq show events interfaces-physical between 6d and 16d
Matching cables records:
Hostname          Interface                 State      Speed      AutoNeg Module    Vendor               Part No          Last Changed
----------------- ------------------------- ---------- ---------- ------- --------- -------------------- ---------------- -------------------------
leaf01            swp1                      up         1G         off     SFP       AVAGO                AFBR-5715PZ-JU1  Thu Feb  7 18:34:20 2019
leaf01            swp2                      up         10G        off     SFP       OEM                  SFP-10GB-LR      Thu Feb  7 18:34:20 2019
leaf01            swp47                     up         10G        off     SFP       JDSU                 PLRXPLSCS4322N   Thu Feb  7 18:34:20 2019
leaf01            swp48                     up         40G        off     QSFP+     Mellanox             MC2210130-002    Thu Feb  7 18:34:20 2019
leaf01            swp49                     down       10G        off     empty     n/a                  n/a              Thu Feb  7 18:34:20 2019
leaf01            swp50                     up         1G         off     SFP       FINISAR CORP.        FCLF8522P2BTL    Thu Feb  7 18:34:20 2019
leaf01            swp51                     up         1G         off     SFP       FINISAR CORP.        FTLF1318P3BTL    Thu Feb  7 18:34:20 2019
leaf01            swp52                     down       1G         off     SFP       CISCO-AGILENT        QFBR-5766LP      Thu Feb  7 18:34:20 2019
...

cumulus@switch:~$ netq show events type interfaces-physical between 0s and 5h
No matching cables records found
```

## View Utilization Statistics Networkwide

Utilization statistics provide a view into the operation of the devices in your network. They indicate whether resources are becoming dangerously close to their maximum capacity or a user-defined threshold. Depending on the function of the switch, the acceptable thresholds can vary.

### View Compute Resources Utilization

You can quickly determine how many compute resources &mdash; CPU, disk and memory &mdash; are being consumed by the switches on your network.

To obtain this information, run the relevant command:

```
netq <hostname> show resource-util [cpu | memory] [around <text-time>] [json]
netq <hostname> show resource-util disk [<text-diskname>] [around <text-time>] [json]
```

When no options are included the output shows the percentage of CPU and memory being consumed as well as the amount and percentage of disk space being consumed. You can use the `around` option to view the information for a particular time.

This example shows the CPU, memory, and disk utilization for all devices.

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

This example shows only the CPU utilization for all devices.

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

This example shows only the memory utilization for all devices.

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

This example shows only the disk utilization for all devices.

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

### View Port Statistics

The `ethtool` command provides a wealth of statistics about network interfaces. It returns statistics about a given node and interface, including frame errors, ACL drops, buffer drops and more. The syntax is:

```
netq [<hostname>] show ethtool-stats port <physical-port> (rx | tx) [extended] [around <text-time>] [json]
```

You can use the `around` option to view the information for a particular time. If no changes are found, a "No matching ethtool_stats records found" message is displayed.

This example shows the *transmit* statistics for switch port *swp50* on a the *leaf01* switch in the network.

```
cumulus@switch:~$ netq leaf01 show ethtool-stats port swp50 tx
Matching ethtool_stats records:
Hostname          Interface                 HwIfOutOctets        HwIfOutUcastPkts     HwIfOutMcastPkts     HwIfOutBcastPkts     HwIfOutDiscards      HwIfOutErrors        HwIfOutQDrops        HwIfOutNonQDrops     HwIfOutQLen          HwIfOutPausePkt      SoftOutErrors        SoftOutDrops         SoftOutTxFifoFull    Last Updated
----------------- ------------------------- -------------------- -------------------- -------------------- -------------------- -------------------- -------------------- -------------------- -------------------- -------------------- -------------------- -------------------- -------------------- -------------------- ------------------------
leaf01            swp50                     8749                 0                    44                   0                    0                    0                    0                    0                    0                    0                    0                    0                    0                    Tue Apr 28 22:09:57 2020
```

This example shows the *receive* statistics for switch port *swp50* on a the *leaf01* switch in the network.

```
cumulus@switch:~$ netq leaf01 show ethtool-stats port swp50 rx

Matching ethtool_stats records:
Hostname          Interface                 HwIfInOctets         HwIfInUcastPkts      HwIfInBcastPkts      HwIfInMcastPkts      HwIfInDiscards       HwIfInL3Drops        HwIfInBufferDrops    HwIfInAclDrops       HwIfInDot3LengthErro HwIfInErrors         HwIfInDot3FrameError HwIfInPausePkt       SoftInErrors         SoftInDrops          SoftInFrameErrors    Last Updated
                                                                                                                                                                                                                    rs                                        s
----------------- ------------------------- -------------------- -------------------- -------------------- -------------------- -------------------- -------------------- -------------------- -------------------- -------------------- -------------------- -------------------- -------------------- -------------------- -------------------- -------------------- ------------------------
leaf01            swp50                     9131                 0                    0                    23                   0                    0                    0                    0                    0                    0                    0                    0                    0                    0                    0                    Tue Apr 28 22:09:25 2020
```

Use the `extended` keyword to view additional statistics:

```
cumulus@switch:~$ netq leaf01 show ethtool-stats port swp50 tx extended

Matching ethtool_stats records:
Hostname          Interface                 HwIfOutPfc0Pkt       HwIfOutPfc1Pkt       HwIfOutPfc2Pkt       HwIfOutPfc3Pkt       HwIfOutPfc4Pkt       HwIfOutPfc5Pkt       HwIfOutPfc6Pkt       HwIfOutPfc7Pkt       HwIfOutWredDrops     HwIfOutQ0WredDrops   HwIfOutQ1WredDrops   HwIfOutQ2WredDrops   HwIfOutQ3WredDrops   HwIfOutQ4WredDrops   HwIfOutQ5WredDrops   HwIfOutQ6WredDrops   HwIfOutQ7WredDrops   HwIfOutQ8WredDrops   HwIfOutQ9WredDrops   Last Updated
----------------- ------------------------- -------------------- -------------------- -------------------- -------------------- -------------------- -------------------- -------------------- -------------------- -------------------- -------------------- -------------------- -------------------- -------------------- -------------------- -------------------- -------------------- -------------------- -------------------- -------------------- ------------------------
leaf01            swp50                      0                    0                    0                    0                    0                    0                    0                    0                    0                    0                    0                    0                    0                    0                    0                    0                    0                    0                    0                    Tue Apr 28 22:09:57 2020
```

```
cumulus@switch:~$ netq leaf01 show ethtool-stats port swp50 rx extended

Matching ethtool_stats records:
Hostname          Interface                 HwIfInPfc0Pkt        HwIfInPfc1Pkt        HwIfInPfc2Pkt        HwIfInPfc3Pkt        HwIfInPfc4Pkt        HwIfInPfc5Pkt        HwIfInPfc6Pkt        HwIfInPfc7Pkt        Last Updated
----------------- ------------------------- -------------------- -------------------- -------------------- -------------------- -------------------- -------------------- -------------------- -------------------- ------------------------
leaf01            swp50                     0                    0                    0                    0                    0                    0                    0                    0                    Tue Apr 28 22:09:25 2020
```

JSON output is also available for these commands:

```
cumulus@leaf01:~$ netq leaf01 show ethtool-stats port swp50 tx json
{
    "ethtool_stats":[
        {
            "hwifoutoctets":12571,
            "hwifoutucastpkts":0,
            "hwifoutpausepkt":0,
            "softouttxfifofull":0,
            "hwifoutmcastpkts":58,
            "hwifoutbcastpkts":0,
            "softouterrors":0,
            "interface":"swp50",
            "lastUpdated":1588112216.0,
            "softoutdrops":0,
            "hwifoutdiscards":0,
            "hwifoutqlen":0,
            "hwifoutnonqdrops":0,
            "hostname":"leaf01",
            "hwifouterrors":0,
            "hwifoutqdrops":0
	}
    ],
    "truncatedResult":false
}
```

```
cumulus@leaf01:~$ netq leaf01 show ethtool-stats port swp50 rx json
{
    "ethtool_stats":[
        {
            "hwifindot3frameerrors":0,
            "hwifinpausepkt":0,
            "hwifinbufferdrops":0,
            "interface":"swp50",
            "hwifinucastpkts":0,
            "hwifinbcastpkts":0,
            "hwifindiscards":0,
            "softinframeerrors":0,
            "softinerrors":0,
            "hwifinoctets":15086,
            "hwifinacldrops":0,
            "hwifinl3drops":0,
            "hostname":"leaf01",
            "hwifinerrors":0,
            "softindrops":0,
            "hwifinmcastpkts":38,
            "lastUpdated":1588112216.0,
            "hwifindot3lengtherrors":0
	}
    ],
    "truncatedResult":false
}
```

```
cumulus@leaf01:~$ netq leaf01 show ethtool-stats port swp50 tx extended json
{
    "ethtool_stats":[
        {
            "hostname":"leaf01",
            "hwifoutq5wreddrops":0,
            "hwifoutq3wreddrops":0,
            "hwifoutpfc3pkt":0,
            "hwifoutq6wreddrops":0,
            "hwifoutq9wreddrops":0,
            "hwifoutq2wreddrops":0,
            "hwifoutq8wreddrops":0,
            "hwifoutpfc7pkt":0,
            "hwifoutpfc4pkt":0,
            "hwifoutpfc6pkt":0,
            "hwifoutq7wreddrops":0,
            "hwifoutpfc0pkt":0,
            "hwifoutpfc1pkt":0,
            "interface":"swp50",
            "hwifoutq0wreddrops":0,
            "hwifoutq4wreddrops":0,
            "hwifoutpfc2pkt":0,
            "lastUpdated":1588112216.0,
            "hwifoutwreddrops":0,
            "hwifoutpfc5pkt":0,
            "hwifoutq1wreddrops":0
	}
    ],
    "truncatedResult":false
}
```

```
cumulus@leaf01:~$ netq leaf01 show ethtool-stats port swp50 rx extended json
{
    "ethtool_stats":[
        {
            "hwifinpfc5pkt":0,
            "hwifinpfc0pkt":0,
            "hwifinpfc1pkt":0,
            "interface":"swp50",
            "hwifinpfc4pkt":0,
            "lastUpdated":1588112216.0,
            "hwifinpfc3pkt":0,
            "hwifinpfc6pkt":0,
            "hostname":"leaf01",
            "hwifinpfc7pkt":0,
            "hwifinpfc2pkt":0
	}
    ],
    "truncatedResult":false
}
```

### View Interface Statistics and Utilization

NetQ Agents collect performance statistics every 30 seconds for the physical interfaces on switches in your network. The NetQ Agent does not collect statistics for non-physical interfaces, such as bonds, bridges, and VXLANs. The NetQ Agent collects the following statistics:

- Statistics
    - **Transmit**: tx\_bytes, tx\_carrier, tx\_colls, tx\_drop, tx\_errs, tx\_packets
    - **Receive**: rx\_bytes, rx\_drop, rx\_errs, rx\_frame, rx\_multicast, rx\_packets
- Utilization
    - rx\_util, tx\_util
    - port speed

To view the interface statistics and utilization, run:

```
netq show interface-stats [errors | all] [<physical-port>] [around <text-time>] [json]
netq show interface-utilization [<text-port>] [tx|rx] [around <text-time>] [json]
```

Where the various options are:

- `errors` limits the output to only the transmit and receive errors found on the designated interfaces
- `physical-port` limits the output to a particular port
- `around` enables viewing of the data at a time in the past
- `json` outputs results in JSON format
- `text-port` limits output to a particular host and port; `hostname` is required with this option
- `tx`, `rx` limits output to the transmit or receive values, respectively

This example shows the statistics for all interfaces on all devices.

```
cumulus@switch:~$ netq show interface-stats
Matching proc_dev_stats records:
Hostname          Interface                 RX Packets           RX Drop              RX Errors            TX Packets           TX Drop              TX Errors            Last Updated
----------------- ------------------------- -------------------- -------------------- -------------------- -------------------- -------------------- -------------------- ------------------------
border01          swp1                      0                    0                    0                    0                    0                    0                    Fri Sep 18 21:06:28 2020
border01          swp54                     71086                1                    0                    71825                0                    0                    Fri Sep 18 21:06:28 2020
border01          swp52                     61281                1                    0                    69446                0                    0                    Fri Sep 18 21:06:28 2020
border01          swp4                      0                    0                    0                    0                    0                    0                    Fri Sep 18 21:06:28 2020
border01          swp53                     64844                1                    0                    70158                0                    0                    Fri Sep 18 21:06:28 2020
border01          swp3                      88276                0                    0                    132592               0                    0                    Fri Sep 18 21:06:28 2020
border01          swp49                     178927               0                    0                    210020               0                    0                    Fri Sep 18 21:06:28 2020
border01          swp51                     67381                1                    0                    71387                0                    0                    Fri Sep 18 21:06:28 2020
border01          swp2                      0                    0                    0                    0                    0                    0                    Fri Sep 18 21:06:28 2020
border01          swp50                     201356               0                    0                    166632               0                    0                    Fri Sep 18 21:06:28 2020
border02          swp1                      0                    0                    0                    0                    0                    0                    Fri Sep 18 21:06:09 2020
border02          swp54                     68408                1                    0                    70275                0                    0                    Fri Sep 18 21:06:09 2020
border02          swp52                     70053                1                    0                    70484                0                    0                    Fri Sep 18 21:06:09 2020
border02          swp4                      0                    0                    0                    0                    0                    0                    Fri Sep 18 21:06:09 2020
border02          swp53                     70464                1                    0                    70943                0                    0                    Fri Sep 18 21:06:09 2020
border02          swp3                      88256                0                    0                    88225                0                    0                    Fri Sep 18 21:06:09 2020
border02          swp49                     209976               0                    0                    178888               0                    0                    Fri Sep 18 21:06:09 2020
border02          swp51                     70474                1                    0                    70857                0                    0                    Fri Sep 18 21:06:09 2020
border02          swp2                      0                    0                    0                    0                    0                    0                    Fri Sep 18 21:06:09 2020
border02          swp50                     166597               0                    0                    201312               0                    0                    Fri Sep 18 21:06:09 2020
fw1               swp49                     0                    0                    0                    0                    0                    0                    Fri Sep 18 21:06:15 2020
fw1               swp1                      132573               0                    0                    88262                0                    0                    Fri Sep 18 21:06:15 2020
fw1               swp2                      88231                0                    0                    88261                0                    0                    Fri Sep 18 21:06:15 2020
fw2               swp1                      0                    0                    0                    0                    0                    0                    Fri Sep 18 21:06:22 2020
fw2               swp2                      0                    0                    0                    0                    0                    0                    Fri Sep 18 21:06:22 2020
fw2               swp49                     0                    0                    0                    0                    0                    0                    Fri Sep 18 21:06:22 2020
leaf01            swp1                      89608                0                    0                    134841               0                    0                    Fri Sep 18 21:06:38 2020
leaf01            swp54                     70629                1                    0                    71241                0                    0                    Fri Sep 18 21:06:38 2020
leaf01            swp52                     70826                1                    0                    71364                0                    0                    Fri Sep 18 21:06:38 2020
leaf01            swp53                     69725                1                    0                    71110                0                    0                    Fri Sep 18 21:06:38 2020
leaf01            swp3                      89252                0                    0                    134515               0                    0                    Fri Sep 18 21:06:38 2020
leaf01            swp49                     91105                0                    0                    100937               0                    0                    Fri Sep 18 21:06:38 2020
leaf01            swp51                     69790                1                    0                    71161                0                    0                    Fri Sep 18 21:06:38 2020
leaf01            swp2                      89569                0                    0                    134861               0                    0                    Fri Sep 18 21:06:38 2020
leaf01            swp50                     295441               0                    0                    273136               0                    0                    Fri Sep 18 21:06:38 2020
leaf02            swp1                      89568                0                    0                    90508                0                    0                    Fri Sep 18 21:06:32 2020
leaf02            swp54                     70549                1                    0                    71088                0                    0                    Fri Sep 18 21:06:32 2020
leaf02            swp52                     62238                1                    0                    70729                0                    0                    Fri Sep 18 21:06:32 2020
leaf02            swp53                     69963                1                    0                    71355                0                    0                    Fri Sep 18 21:06:32 2020
leaf02            swp3                      89266                0                    0                    90180                0                    0                    Fri Sep 18 21:06:32 2020
leaf02            swp49                     100931               0                    0                    91098                0                    0                    Fri Sep 18 21:06:32 2020
leaf02            swp51                     68573                1                    0                    69168                0                    0                    Fri Sep 18 21:06:32 2020
leaf02            swp2                      89591                0                    0                    90479                0                    0                    Fri Sep 18 21:06:32 2020
leaf02            swp50                     273115               0                    0                    295420               0                    0                    Fri Sep 18 21:06:32 2020
leaf03            swp1                      89590                0                    0                    134847               0                    0                    Fri Sep 18 21:06:25 2020
leaf03            swp54                     70515                1                    0                    71786                0                    0                    Fri Sep 18 21:06:25 2020
leaf03            swp52                     69922                1                    0                    71816                0                    0                    Fri Sep 18 21:06:25 2020
leaf03            swp53                     70397                1                    0                    71846                0                    0                    Fri Sep 18 21:06:25 2020
leaf03            swp3                      89264                0                    0                    134501               0                    0                    Fri Sep 18 21:06:25 2020
leaf03            swp49                     200394               0                    0                    220183               0                    0                    Fri Sep 18 21:06:25 2020
leaf03            swp51                     67063                0                    0                    71737                0                    0                    Fri Sep 18 21:06:25 2020
leaf03            swp2                      89564                0                    0                    134821               0                    0                    Fri Sep 18 21:06:25 2020
leaf03            swp50                     170186               0                    0                    158605               0                    0                    Fri Sep 18 21:06:25 2020
leaf04            swp1                      89558                0                    0                    90477                0                    0                    Fri Sep 18 21:06:27 2020
leaf04            swp54                     68027                1                    0                    70540                0                    0                    Fri Sep 18 21:06:27 2020
leaf04            swp52                     69422                1                    0                    71786                0                    0                    Fri Sep 18 21:06:27 2020
leaf04            swp53                     69663                1                    0                    71269                0                    0                    Fri Sep 18 21:06:27 2020
leaf04            swp3                      89244                0                    0                    90181                0                    0                    Fri Sep 18 21:06:27 2020
leaf04            swp49                     220187               0                    0                    200396               0                    0                    Fri Sep 18 21:06:27 2020
leaf04            swp51                     68990                1                    0                    71783                0                    0                    Fri Sep 18 21:06:27 2020
leaf04            swp2                      89588                0                    0                    90508                0                    0                    Fri Sep 18 21:06:27 2020
leaf04            swp50                     158609               0                    0                    170188               0                    0                    Fri Sep 18 21:06:27 2020
spine01           swp1                      71146                0                    0                    69788                0                    0                    Fri Sep 18 21:06:27 2020
spine01           swp4                      71776                0                    0                    68997                0                    0                    Fri Sep 18 21:06:27 2020
spine01           swp5                      71380                0                    0                    67387                0                    0                    Fri Sep 18 21:06:27 2020
spine01           swp3                      71733                0                    0                    67072                0                    0                    Fri Sep 18 21:06:27 2020
spine01           swp2                      69157                0                    0                    68575                0                    0                    Fri Sep 18 21:06:27 2020
spine01           swp6                      70865                0                    0                    70496                0                    0                    Fri Sep 18 21:06:27 2020
spine02           swp1                      71346                0                    0                    70821                0                    0                    Fri Sep 18 21:06:25 2020
spine02           swp4                      71777                0                    0                    69426                0                    0                    Fri Sep 18 21:06:25 2020
spine02           swp5                      69437                0                    0                    61286                0                    0                    Fri Sep 18 21:06:25 2020
spine02           swp3                      71809                0                    0                    69929                0                    0                    Fri Sep 18 21:06:25 2020
spine02           swp2                      70716                0                    0                    62238                0                    0                    Fri Sep 18 21:06:25 2020
spine02           swp6                      70490                0                    0                    70072                0                    0                    Fri Sep 18 21:06:25 2020
spine03           swp1                      71090                0                    0                    69718                0                    0                    Fri Sep 18 21:06:22 2020
spine03           swp4                      71258                0                    0                    69664                0                    0                    Fri Sep 18 21:06:22 2020
spine03           swp5                      70147                0                    0                    64846                0                    0                    Fri Sep 18 21:06:22 2020
spine03           swp3                      71837                0                    0                    70400                0                    0                    Fri Sep 18 21:06:22 2020
spine03           swp2                      71340                0                    0                    69961                0                    0                    Fri Sep 18 21:06:22 2020
spine03           swp6                      70947                0                    0                    70481                0                    0                    Fri Sep 18 21:06:22 2020
spine04           swp1                      71213                0                    0                    70614                0                    0                    Fri Sep 18 21:06:12 2020
spine04           swp4                      70521                0                    0                    68021                0                    0                    Fri Sep 18 21:06:12 2020
spine04           swp5                      71806                0                    0                    71079                0                    0                    Fri Sep 18 21:06:12 2020
spine04           swp3                      71770                0                    0                    70510                0                    0                    Fri Sep 18 21:06:12 2020
spine04           swp2                      71064                0                    0                    70538                0                    0                    Fri Sep 18 21:06:12 2020
spine04           swp6                      70271                0                    0                    68416                0                    0                    Fri Sep 18 21:06:12 2020
```

This example shows the statistics for the *swp1* interface on all devices.

```
cumulus@switch:~$ netq show interface-stats swp1
Matching proc_dev_stats records:
Hostname          Interface                 RX Packets           RX Drop              RX Errors            TX Packets           TX Drop              TX Errors            Last Updated
----------------- ------------------------- -------------------- -------------------- -------------------- -------------------- -------------------- -------------------- ------------------------
border01          swp1                      0                    0                    0                    0                    0                    0                    Fri Sep 18 21:23:17 2020
border02          swp1                      0                    0                    0                    0                    0                    0                    Fri Sep 18 21:23:21 2020
fw1               swp1                      134125               0                    0                    89296                0                    0                    Fri Sep 18 21:23:33 2020
fw2               swp1                      0                    0                    0                    0                    0                    0                    Fri Sep 18 21:23:36 2020
leaf01            swp1                      90625                0                    0                    136376               0                    0                    Fri Sep 18 21:23:27 2020
leaf02            swp1                      90580                0                    0                    91531                0                    0                    Fri Sep 18 21:23:16 2020
leaf03            swp1                      90607                0                    0                    136379               0                    0                    Fri Sep 18 21:23:15 2020
leaf04            swp1                      90574                0                    0                    91502                0                    0                    Fri Sep 18 21:23:16 2020
spine01           swp1                      71979                0                    0                    70622                0                    0                    Fri Sep 18 21:23:39 2020
spine02           swp1                      72179                0                    0                    71654                0                    0                    Fri Sep 18 21:23:35 2020
spine03           swp1                      71922                0                    0                    70550                0                    0                    Fri Sep 18 21:23:33 2020
spine04           swp1                      72047                0                    0                    71448                0                    0                    Fri Sep 18 21:23:23 2020
```

This example shows the utilization data for all devices.

```
cumulus@switch:~$ netq show interface-utilization
Matching port_stats records:
Hostname          Interface                 RX Bytes (30sec)     RX Drop (30sec)      RX Errors (30sec)    RX Util (%age)       TX Bytes (30sec)     TX Drop (30sec)      TX Errors (30sec)    TX Util (%age)       Port Speed           Last Changed
----------------- ------------------------- -------------------- -------------------- -------------------- -------------------- -------------------- -------------------- -------------------- -------------------- -------------------- --------------------
border01          swp1                      0                    0                    0                    0                    0                    0                    0                    0                    Unknown              Fri Sep 18 21:19:45
                                                                                                                                                                                                                                         2020
border01          swp54                     2459                 0                    0                    0                    2461                 0                    0                    0                    1G                   Fri Sep 18 21:19:45
                                                                                                                                                                                                                                         2020
border01          swp52                     2459                 0                    0                    0                    2461                 0                    0                    0                    1G                   Fri Sep 18 21:19:45
                                                                                                                                                                                                                                         2020
border01          swp4                      0                    0                    0                    0                    0                    0                    0                    0                    Unknown              Fri Sep 18 21:19:45
                                                                                                                                                                                                                                         2020
border01          swp53                     2545                 0                    0                    0                    2547                 0                    0                    0                    1G                   Fri Sep 18 21:19:45
                                                                                                                                                                                                                                         2020
border01          swp3                      3898                 0                    0                    0                    4714                 0                    0                    0                    1G                   Fri Sep 18 21:19:45
                                                                                                                                                                                                                                         2020
border01          swp49                     17816                0                    0                    0                    20015                0                    0                    0                    1G                   Fri Sep 18 21:19:45
                                                                                                                                                                                                                                         2020
border01          swp51                     2545                 0                    0                    0                    2547                 0                    0                    0                    1G                   Fri Sep 18 21:19:45
                                                                                                                                                                                                                                         2020
border01          swp2                      0                    0                    0                    0                    0                    0                    0                    0                    Unknown              Fri Sep 18 21:19:45
                                                                                                                                                                                                                                         2020
border01          swp50                     9982                 0                    0                    0                    7941                 0                    0                    0                    1G                   Fri Sep 18 21:19:45
                                                                                                                                                                                                                                         2020
border02          swp1                      0                    0                    0                    0                    0                    0                    0                    0                    Unknown              Fri Sep 18 21:19:19
                                                                                                                                                                                                                                         2020
border02          swp54                     2459                 0                    0                    0                    2461                 0                    0                    0                    1G                   Fri Sep 18 21:19:19
                                                                                                                                                                                                                                         2020
border02          swp52                     2459                 0                    0                    0                    2461                 0                    0                    0                    1G                   Fri Sep 18 21:19:19
                                                                                                                                                                                                                                         2020
border02          swp4                      0                    0                    0                    0                    0                    0                    0                    0                    Unknown              Fri Sep 18 21:19:19
                                                                                                                                                                                                                                         2020
border02          swp53                     2545                 0                    0                    0                    2547                 0                    0                    0                    1G                   Fri Sep 18 21:19:19
                                                                                                                                                                                                                                         2020
border02          swp3                      4022                 0                    0                    0                    4118                 0                    0                    0                    1G                   Fri Sep 18 21:19:19
                                                                                                                                                                                                                                         2020
border02          swp49                     19982                0                    0                    0                    16746                0                    0                    0                    1G                   Fri Sep 18 21:19:19
                                                                                                                                                                                                                                         2020
border02          swp51                     2545                 0                    0                    0                    2547                 0                    0                    0                    1G                   Fri Sep 18 21:19:19
                                                                                                                                                                                                                                         2020
border02          swp2                      0                    0                    0                    0                    0                    0                    0                    0                    Unknown              Fri Sep 18 21:19:19
                                                                                                                                                                                                                                         2020
border02          swp50                     8254                 0                    0                    0                    10672                0                    0                    0                    1G                   Fri Sep 18 21:19:19
                                                                                                                                                                                                                                         2020
fw1               swp49                     0                    0                    0                    0                    0                    0                    0                    0                    Unknown              Fri Sep 18 21:19:31
                                                                                                                                                                                                                                         2020
fw1               swp1                      4714                 0                    0                    0                    3898                 0                    0                    0                    1G                   Fri Sep 18 21:19:31
                                                                                                                                                                                                                                         2020
fw1               swp2                      3919                 0                    0                    0                    3898                 0                    0                    0                    1G                   Fri Sep 18 21:19:31
                                                                                                                                                                                                                                         2020
fw2               swp1                      0                    0                    0                    0                    0                    0                    0                    0                    Unknown              Fri Sep 18 21:19:33
                                                                                                                                                                                                                                         2020
fw2               swp2                      0                    0                    0                    0                    0                    0                    0                    0                    Unknown              Fri Sep 18 21:19:33
                                                                                                                                                                                                                                         2020
fw2               swp49                     0                    0                    0                    0                    0                    0                    0                    0                    Unknown              Fri Sep 18 21:19:33
                                                                                                                                                                                                                                         2020
leaf01            swp1                      3815                 0                    0                    0                    4712                 0                    0                    0                    1G                   Fri Sep 18 21:19:24
                                                                                                                                                                                                                                         2020
leaf01            swp54                     2459                 0                    0                    0                    2459                 0                    0                    0                    1G                   Fri Sep 18 21:19:24
                                                                                                                                                                                                                                         2020
leaf01            swp52                     2459                 0                    0                    0                    2459                 0                    0                    0                    1G                   Fri Sep 18 21:19:24
                                                                                                                                                                                                                                         2020
leaf01            swp53                     2459                 0                    0                    0                    2459                 0                    0                    0                    1G                   Fri Sep 18 21:19:24
                                                                                                                                                                                                                                         2020
leaf01            swp3                      3815                 0                    0                    0                    4754                 0                    0                    0                    1G                   Fri Sep 18 21:19:24
                                                                                                                                                                                                                                         2020
leaf01            swp49                     3996                 0                    0                    0                    4242                 0                    0                    0                    1G                   Fri Sep 18 21:19:24
                                                                                                                                                                                                                                         2020
leaf01            swp51                     2459                 0                    0                    0                    2459                 0                    0                    0                    1G                   Fri Sep 18 21:19:24
                                                                                                                                                                                                                                         2020
leaf01            swp2                      3815                 0                    0                    0                    4712                 0                    0                    0                    1G                   Fri Sep 18 21:19:24
                                                                                                                                                                                                                                         2020
leaf01            swp50                     31565                0                    0                    0                    29964                0                    0                    0                    1G                   Fri Sep 18 21:19:24
                                                                                                                                                                                                                                         2020
leaf02            swp1                      3987                 0                    0                    0                    4081                 0                    0                    0                    1G                   Fri Sep 18 21:19:43
                                                                                                                                                                                                                                         2020
leaf02            swp54                     2459                 0                    0                    0                    2459                 0                    0                    0                    1G                   Fri Sep 18 21:19:43
                                                                                                                                                                                                                                         2020
leaf02            swp52                     2459                 0                    0                    0                    2459                 0                    0                    0                    1G                   Fri Sep 18 21:19:43
                                                                                                                                                                                                                                         2020
leaf02            swp53                     2459                 0                    0                    0                    2459                 0                    0                    0                    1G                   Fri Sep 18 21:19:43
                                                                                                                                                                                                                                         2020
leaf02            swp3                      3815                 0                    0                    0                    3959                 0                    0                    0                    1G                   Fri Sep 18 21:19:43
                                                                                                                                                                                                                                         2020
leaf02            swp49                     4422                 0                    0                    0                    3996                 0                    0                    0                    1G                   Fri Sep 18 21:19:43
                                                                                                                                                                                                                                         2020
leaf02            swp51                     2459                 0                    0                    0                    2459                 0                    0                    0                    1G                   Fri Sep 18 21:19:43
                                                                                                                                                                                                                                         2020
leaf02            swp2                      3815                 0                    0                    0                    4003                 0                    0                    0                    1G                   Fri Sep 18 21:19:43
                                                                                                                                                                                                                                         2020
leaf02            swp50                     30769                0                    0                    0                    31457                0                    0                    0                    1G                   Fri Sep 18 21:19:43
                                                                                                                                                                                                                                         2020
leaf03            swp1                      3815                 0                    0                    0                    4876                 0                    0                    0                    1G                   Fri Sep 18 21:19:42
                                                                                                                                                                                                                                         2020
leaf03            swp54                     2623                 0                    0                    0                    2545                 0                    0                    0                    1G                   Fri Sep 18 21:19:42
                                                                                                                                                                                                                                         2020
leaf03            swp52                     2459                 0                    0                    0                    2459                 0                    0                    0                    1G                   Fri Sep 18 21:19:42
                                                                                                                                                                                                                                         2020
leaf03            swp53                     2537                 0                    0                    0                    2459                 0                    0                    0                    1G                   Fri Sep 18 21:19:42
                                                                                                                                                                                                                                         2020
leaf03            swp3                      3815                 0                    0                    0                    4754                 0                    0                    0                    1G                   Fri Sep 18 21:19:42
                                                                                                                                                                                                                                         2020
leaf03            swp49                     26514                0                    0                    0                    9830                 0                    0                    0                    1G                   Fri Sep 18 21:19:42
                                                                                                                                                                                                                                         2020
leaf03            swp51                     2537                 0                    0                    0                    2459                 0                    0                    0                    1G                   Fri Sep 18 21:19:42
                                                                                                                                                                                                                                         2020
leaf03            swp2                      3815                 0                    0                    0                    4712                 0                    0                    0                    1G                   Fri Sep 18 21:19:42
                                                                                                                                                                                                                                         2020
leaf03            swp50                     7938                 0                    0                    0                    25030                0                    0                    0                    1G                   Fri Sep 18 21:19:42
                                                                                                                                                                                                                                         2020
leaf04            swp1                      3815                 0                    0                    0                    4003                 0                    0                    0                    1G                   Fri Sep 18 21:19:43
                                                                                                                                                                                                                                         2020
leaf04            swp54                     2459                 0                    0                    0                    2459                 0                    0                    0                    1G                   Fri Sep 18 21:19:43
                                                                                                                                                                                                                                         2020
leaf04            swp52                     2459                 0                    0                    0                    2459                 0                    0                    0                    1G                   Fri Sep 18 21:19:43
                                                                                                                                                                                                                                         2020
leaf04            swp53                     2459                 0                    0                    0                    2459                 0                    0                    0                    1G                   Fri Sep 18 21:19:43
                                                                                                                                                                                                                                         2020
leaf04            swp3                      3815                 0                    0                    0                    4003                 0                    0                    0                    1G                   Fri Sep 18 21:19:43
                                                                                                                                                                                                                                         2020
leaf04            swp49                     9549                 0                    0                    0                    26604                0                    0                    0                    1G                   Fri Sep 18 21:19:43
                                                                                                                                                                                                                                         2020
leaf04            swp51                     2459                 0                    0                    0                    2459                 0                    0                    0                    1G                   Fri Sep 18 21:19:43
                                                                                                                                                                                                                                         2020
leaf04            swp2                      3815                 0                    0                    0                    3917                 0                    0                    0                    1G                   Fri Sep 18 21:19:43
                                                                                                                                                                                                                                         2020
leaf04            swp50                     25030                0                    0                    0                    7724                 0                    0                    0                    1G                   Fri Sep 18 21:19:43
                                                                                                                                                                                                                                         2020
spine01           swp1                      2459                 0                    0                    0                    2459                 0                    0                    0                    1G                   Fri Sep 18 21:19:36
                                                                                                                                                                                                                                         2020
spine01           swp4                      2459                 0                    0                    0                    2459                 0                    0                    0                    1G                   Fri Sep 18 21:19:36
                                                                                                                                                                                                                                         2020
spine01           swp5                      2547                 0                    0                    0                    2545                 0                    0                    0                    1G                   Fri Sep 18 21:19:36
                                                                                                                                                                                                                                         2020
spine01           swp3                      2459                 0                    0                    0                    2459                 0                    0                    0                    1G                   Fri Sep 18 21:19:36
                                                                                                                                                                                                                                         2020
spine01           swp2                      2459                 0                    0                    0                    2459                 0                    0                    0                    1G                   Fri Sep 18 21:19:36
                                                                                                                                                                                                                                         2020
spine01           swp6                      2461                 0                    0                    0                    2459                 0                    0                    0                    1G                   Fri Sep 18 21:19:36
                                                                                                                                                                                                                                         2020
spine02           swp1                      2459                 0                    0                    0                    2459                 0                    0                    0                    1G                   Fri Sep 18 21:19:32
                                                                                                                                                                                                                                         2020
spine02           swp4                      2459                 0                    0                    0                    2459                 0                    0                    0                    1G                   Fri Sep 18 21:19:32
                                                                                                                                                                                                                                         2020
spine02           swp5                      2461                 0                    0                    0                    2459                 0                    0                    0                    1G                   Fri Sep 18 21:19:32
                                                                                                                                                                                                                                         2020
spine02           swp3                      2459                 0                    0                    0                    2459                 0                    0                    0                    1G                   Fri Sep 18 21:19:32
                                                                                                                                                                                                                                         2020
spine02           swp2                      2459                 0                    0                    0                    2459                 0                    0                    0                    1G                   Fri Sep 18 21:19:32
                                                                                                                                                                                                                                         2020
spine02           swp6                      2461                 0                    0                    0                    2459                 0                    0                    0                    1G                   Fri Sep 18 21:19:32
                                                                                                                                                                                                                                         2020
spine03           swp1                      2459                 0                    0                    0                    2459                 0                    0                    0                    1G                   Fri Sep 18 21:19:30
                                                                                                                                                                                                                                         2020
spine03           swp4                      2459                 0                    0                    0                    2459                 0                    0                    0                    1G                   Fri Sep 18 21:19:30
                                                                                                                                                                                                                                         2020
spine03           swp5                      2547                 0                    0                    0                    2545                 0                    0                    0                    1G                   Fri Sep 18 21:19:30
                                                                                                                                                                                                                                         2020
spine03           swp3                      2459                 0                    0                    0                    2459                 0                    0                    0                    1G                   Fri Sep 18 21:19:30
                                                                                                                                                                                                                                         2020
spine03           swp2                      2459                 0                    0                    0                    2459                 0                    0                    0                    1G                   Fri Sep 18 21:19:30
                                                                                                                                                                                                                                         2020
spine03           swp6                      2461                 0                    0                    0                    2459                 0                    0                    0                    1G                   Fri Sep 18 21:19:30
                                                                                                                                                                                                                                         2020
spine04           swp1                      2459                 0                    0                    0                    2459                 0                    0                    0                    1G                   Fri Sep 18 21:19:19
                                                                                                                                                                                                                                         2020
spine04           swp4                      2545                 0                    0                    0                    2545                 0                    0                    0                    1G                   Fri Sep 18 21:19:19
                                                                                                                                                                                                                                         2020
spine04           swp5                      2652                 0                    0                    0                    2860                 0                    0                    0                    1G                   Fri Sep 18 21:19:19
                                                                                                                                                                                                                                         2020
spine04           swp3                      2459                 0                    0                    0                    2459                 0                    0                    0                    1G                   Fri Sep 18 21:19:19
                                                                                                                                                                                                                                         2020
spine04           swp2                      2459                 0                    0                    0                    2459                 0                    0                    0                    1G                   Fri Sep 18 21:19:19
                                                                                                                                                                                                                                         2020
spine04           swp6                      2566                 0                    0                    0                    2774                 0                    0                    0                    1G                   Fri Sep 18 21:19:19
                                                                                                                                                                                                                                         2020

```

This example shows only the transmit utilization data for devices.

```
cumulus@switch:~$ netq show interface-utilization tx
Matching port_stats records:
Hostname          Interface                 TX Bytes (30sec)     TX Drop (30sec)      TX Errors (30sec)    TX Util (%age)       Port Speed           Last Changed
----------------- ------------------------- -------------------- -------------------- -------------------- -------------------- -------------------- --------------------
border01          swp1                      0                    0                    0                    0                    Unknown              Fri Sep 18 21:21:47
                                                                                                                                                     2020
border01          swp54                     2633                 0                    0                    0                    1G                   Fri Sep 18 21:21:47
                                                                                                                                                     2020
border01          swp52                     2738                 0                    0                    0                    1G                   Fri Sep 18 21:21:47
                                                                                                                                                     2020
border01          swp4                      0                    0                    0                    0                    Unknown              Fri Sep 18 21:21:47
                                                                                                                                                     2020
border01          swp53                     2652                 0                    0                    0                    1G                   Fri Sep 18 21:21:47
                                                                                                                                                     2020
border01          swp3                      4891                 0                    0                    0                    1G                   Fri Sep 18 21:21:47
                                                                                                                                                     2020
border01          swp49                     20072                0                    0                    0                    1G                   Fri Sep 18 21:21:47
                                                                                                                                                     2020
border01          swp51                     2547                 0                    0                    0                    1G                   Fri Sep 18 21:21:47
                                                                                                                                                     2020
border01          swp2                      0                    0                    0                    0                    Unknown              Fri Sep 18 21:21:47
                                                                                                                                                     2020
border01          swp50                     8468                 0                    0                    0                    1G                   Fri Sep 18 21:21:47
                                                                                                                                                     2020
border02          swp1                      0                    0                    0                    0                    Unknown              Fri Sep 18 21:21:50
                                                                                                                                                     2020
border02          swp54                     2461                 0                    0                    0                    1G                   Fri Sep 18 21:21:50
                                                                                                                                                     2020
border02          swp52                     2461                 0                    0                    0                    1G                   Fri Sep 18 21:21:50
                                                                                                                                                     2020
border02          swp4                      0                    0                    0                    0                    Unknown              Fri Sep 18 21:21:50
                                                                                                                                                     2020
border02          swp53                     2461                 0                    0                    0                    1G                   Fri Sep 18 21:21:50
                                                                                                                                                     2020
border02          swp3                      4043                 0                    0                    0                    1G                   Fri Sep 18 21:21:50
                                                                                                                                                     2020
border02          swp49                     17063                0                    0                    0                    1G                   Fri Sep 18 21:21:50
                                                                                                                                                     2020
border02          swp51                     2461                 0                    0                    0                    1G                   Fri Sep 18 21:21:50
                                                                                                                                                     2020
border02          swp2                      0                    0                    0                    0                    Unknown              Fri Sep 18 21:21:50
                                                                                                                                                     2020
border02          swp50                     10672                0                    0                    0                    1G                   Fri Sep 18 21:21:50
                                                                                                                                                     2020
fw1               swp49                     0                    0                    0                    0                    Unknown              Fri Sep 18 21:21:32
                                                                                                                                                     2020
fw1               swp1                      3898                 0                    0                    0                    1G                   Fri Sep 18 21:21:32
                                                                                                                                                     2020
fw1               swp2                      3898                 0                    0                    0                    1G                   Fri Sep 18 21:21:32
                                                                                                                                                     2020
fw2               swp1                      0                    0                    0                    0                    Unknown              Fri Sep 18 21:21:35
                                                                                                                                                     2020
fw2               swp2                      0                    0                    0                    0                    Unknown              Fri Sep 18 21:21:35
                                                                                                                                                     2020
fw2               swp49                     0                    0                    0                    0                    Unknown              Fri Sep 18 21:21:35
                                                                                                                                                     2020
leaf01            swp1                      4712                 0                    0                    0                    1G                   Fri Sep 18 21:21:56
                                                                                                                                                     2020
leaf01            swp54                     2459                 0                    0                    0                    1G                   Fri Sep 18 21:21:56
                                                                                                                                                     2020
leaf01            swp52                     2459                 0                    0                    0                    1G                   Fri Sep 18 21:21:56
                                                                                                                                                     2020
leaf01            swp53                     2564                 0                    0                    0                    1G                   Fri Sep 18 21:21:56
                                                                                                                                                     2020
leaf01            swp3                      4754                 0                    0                    0                    1G                   Fri Sep 18 21:21:56
                                                                                                                                                     2020
leaf01            swp49                     4332                 0                    0                    0                    1G                   Fri Sep 18 21:21:56
                                                                                                                                                     2020
leaf01            swp51                     2459                 0                    0                    0                    1G                   Fri Sep 18 21:21:56
                                                                                                                                                     2020
leaf01            swp2                      4712                 0                    0                    0                    1G                   Fri Sep 18 21:21:56
                                                                                                                                                     2020
leaf01            swp50                     30337                0                    0                    0                    1G                   Fri Sep 18 21:21:56
                                                                                                                                                     2020
leaf02            swp1                      4081                 0                    0                    0                    1G                   Fri Sep 18 21:21:45
                                                                                                                                                     2020
leaf02            swp54                     2459                 0                    0                    0                    1G                   Fri Sep 18 21:21:45
                                                                                                                                                     2020
leaf02            swp52                     2459                 0                    0                    0                    1G                   Fri Sep 18 21:21:45
                                                                                                                                                     2020
leaf02            swp53                     2459                 0                    0                    0                    1G                   Fri Sep 18 21:21:45
                                                                                                                                                     2020
leaf02            swp3                      3917                 0                    0                    0                    1G                   Fri Sep 18 21:21:45
                                                                                                                                                     2020
leaf02            swp49                     3996                 0                    0                    0                    1G                   Fri Sep 18 21:21:45
                                                                                                                                                     2020
leaf02            swp51                     2459                 0                    0                    0                    1G                   Fri Sep 18 21:21:45
                                                                                                                                                     2020
leaf02            swp2                      3917                 0                    0                    0                    1G                   Fri Sep 18 21:21:45
                                                                                                                                                     2020
leaf02            swp50                     31711                0                    0                    0                    1G                   Fri Sep 18 21:21:45
                                                                                                                                                     2020
leaf03            swp1                      4641                 0                    0                    0                    1G                   Fri Sep 18 21:21:43
                                                                                                                                                     2020
leaf03            swp54                     2459                 0                    0                    0                    1G                   Fri Sep 18 21:21:43
                                                                                                                                                     2020
leaf03            swp52                     2459                 0                    0                    0                    1G                   Fri Sep 18 21:21:43
                                                                                                                                                     2020
leaf03            swp53                     2459                 0                    0                    0                    1G                   Fri Sep 18 21:21:43
                                                                                                                                                     2020
leaf03            swp3                      4641                 0                    0                    0                    1G                   Fri Sep 18 21:21:43
                                                                                                                                                     2020
leaf03            swp49                     9740                 0                    0                    0                    1G                   Fri Sep 18 21:21:43
                                                                                                                                                     2020
leaf03            swp51                     2459                 0                    0                    0                    1G                   Fri Sep 18 21:21:43
                                                                                                                                                     2020
leaf03            swp2                      4813                 0                    0                    0                    1G                   Fri Sep 18 21:21:43
                                                                                                                                                     2020
leaf03            swp50                     25789                0                    0                    0                    1G                   Fri Sep 18 21:21:43
                                                                                                                                                     2020
leaf04            swp1                      3917                 0                    0                    0                    1G                   Fri Sep 18 21:21:45
                                                                                                                                                     2020
leaf04            swp54                     2459                 0                    0                    0                    1G                   Fri Sep 18 21:21:45
                                                                                                                                                     2020
leaf04            swp52                     2459                 0                    0                    0                    1G                   Fri Sep 18 21:21:45
                                                                                                                                                     2020
leaf04            swp53                     2545                 0                    0                    0                    1G                   Fri Sep 18 21:21:45
                                                                                                                                                     2020
leaf04            swp3                      3959                 0                    0                    0                    1G                   Fri Sep 18 21:21:45
                                                                                                                                                     2020
leaf04            swp49                     27061                0                    0                    0                    1G                   Fri Sep 18 21:21:45
                                                                                                                                                     2020
leaf04            swp51                     2459                 0                    0                    0                    1G                   Fri Sep 18 21:21:45
                                                                                                                                                     2020
leaf04            swp2                      4081                 0                    0                    0                    1G                   Fri Sep 18 21:21:45
                                                                                                                                                     2020
leaf04            swp50                     7702                 0                    0                    0                    1G                   Fri Sep 18 21:21:45
                                                                                                                                                     2020
spine01           swp1                      2459                 0                    0                    0                    1G                   Fri Sep 18 21:21:38
                                                                                                                                                     2020
spine01           swp4                      2545                 0                    0                    0                    1G                   Fri Sep 18 21:21:38
                                                                                                                                                     2020
spine01           swp5                      2459                 0                    0                    0                    1G                   Fri Sep 18 21:21:38
                                                                                                                                                     2020
spine01           swp3                      2459                 0                    0                    0                    1G                   Fri Sep 18 21:21:38
                                                                                                                                                     2020
spine01           swp2                      2459                 0                    0                    0                    1G                   Fri Sep 18 21:21:38
                                                                                                                                                     2020
spine01           swp6                      2459                 0                    0                    0                    1G                   Fri Sep 18 21:21:38
                                                                                                                                                     2020
spine02           swp1                      2459                 0                    0                    0                    1G                   Fri Sep 18 21:21:34
                                                                                                                                                     2020
spine02           swp4                      2459                 0                    0                    0                    1G                   Fri Sep 18 21:21:34
                                                                                                                                                     2020
spine02           swp5                      2459                 0                    0                    0                    1G                   Fri Sep 18 21:21:34
                                                                                                                                                     2020
spine02           swp3                      2459                 0                    0                    0                    1G                   Fri Sep 18 21:21:34
                                                                                                                                                     2020
spine02           swp2                      2459                 0                    0                    0                    1G                   Fri Sep 18 21:21:34
                                                                                                                                                     2020
spine02           swp6                      2459                 0                    0                    0                    1G                   Fri Sep 18 21:21:34
                                                                                                                                                     2020
spine03           swp1                      2564                 0                    0                    0                    1G                   Fri Sep 18 21:21:31
                                                                                                                                                     2020
spine03           swp4                      2459                 0                    0                    0                    1G                   Fri Sep 18 21:21:31
                                                                                                                                                     2020
spine03           swp5                      2459                 0                    0                    0                    1G                   Fri Sep 18 21:21:31
                                                                                                                                                     2020
spine03           swp3                      2459                 0                    0                    0                    1G                   Fri Sep 18 21:21:31
                                                                                                                                                     2020
spine03           swp2                      2459                 0                    0                    0                    1G                   Fri Sep 18 21:21:31
                                                                                                                                                     2020
spine03           swp6                      2459                 0                    0                    0                    1G                   Fri Sep 18 21:21:31
                                                                                                                                                     2020
spine04           swp1                      2564                 0                    0                    0                    1G                   Fri Sep 18 21:21:51
                                                                                                                                                     2020
spine04           swp4                      2459                 0                    0                    0                    1G                   Fri Sep 18 21:21:51
                                                                                                                                                     2020
spine04           swp5                      2545                 0                    0                    0                    1G                   Fri Sep 18 21:21:51
                                                                                                                                                     2020
spine04           swp3                      2459                 0                    0                    0                    1G                   Fri Sep 18 21:21:51
                                                                                                                                                     2020
spine04           swp2                      2459                 0                    0                    0                    1G                   Fri Sep 18 21:21:51
                                                                                                                                                     2020
spine04           swp6                      2459                 0                    0                    0                    1G                   Fri Sep 18 21:21:51
                                                                                                                                                     2020
```

### View ACL Resource Utilization Networkwide

You can monitor the incoming and outgoing access control lists (ACLs) configured on all switches and host.

To view ACL resource utilization across all devices, run:

```
netq show cl-resource acl [ingress | egress] [around <text-time>] [json]
```

Use the `egress` or `ingress` options to show only the outgoing or incoming ACLs. Use the `around` option to show this information for a time in the past.

This example shows the ACL resources available and currently used by all devices.

```
cumulus@switch:~$ netq show cl-resource acl
Matching cl_resource records:
Hostname          In IPv4 filter       In IPv4 Mangle       In IPv6 filter       In IPv6 Mangle       In 8021x filter      In Mirror            In PBR IPv4 filter   In PBR IPv6 filter   Eg IPv4 filter       Eg IPv4 Mangle       Eg IPv6 filter       Eg IPv6 Mangle       ACL Regions          18B Rules Key        32B Rules Key        54B Rules Key        L4 Port range Checke Last Updated
                                                                                                                                                                                                                                                                                                                                                                  rs
----------------- -------------------- -------------------- -------------------- -------------------- -------------------- -------------------- -------------------- -------------------- -------------------- -------------------- -------------------- -------------------- -------------------- -------------------- -------------------- -------------------- -------------------- ------------------------
leaf01            36,512(7%)           0,0(0%)              30,768(3%)           0,0(0%)              0,0(0%)              0,0(0%)              0,0(0%)              0,0(0%)              29,256(11%)          0,0(0%)              0,0(0%)              0,0(0%)              0,0(0%)              0,0(0%)              0,0(0%)              0,0(0%)              2,24(8%)             Mon Jan 13 03:34:11 2020
```
<!-- need output for all devs -->
You can also view this same information in JSON format.

```
cumulus@switch:~$ netq leaf01 show cl-resource acl json
{
    "cl_resource": [
        {
            "egIpv4Filter": "29,256(11%)",
            "egIpv4Mangle": "0,0(0%)",
            "inIpv6Filter": "30,768(3%)",
            "egIpv6Mangle": "0,0(0%)",
            "inIpv4Mangle": "0,0(0%)",
            "hostname": "leaf01",
            "inMirror": "0,0(0%)",
            "egIpv6Filter": "0,0(0%)",
            "lastUpdated": 1578886451.885,
            "54bRulesKey": "0,0(0%)",
            "aclRegions": "0,0(0%)",
            "in8021XFilter": "0,0(0%)",
            "inIpv4Filter": "36,512(7%)",
            "inPbrIpv6Filter": "0,0(0%)",
            "18bRulesKey": "0,0(0%)",
            "l4PortRangeCheckers": "2,24(8%)",
            "inIpv6Mangle": "0,0(0%)",
            "32bRulesKey": "0,0(0%)",
            "inPbrIpv4Filter": "0,0(0%)"
	}
    ],
    "truncatedResult":false
}
```

### View Forwarding Resources Utilization Networkwide

You can monitor the amount of forwarding resources used by a switch, currently or at a time in the past.

To view forwarding resources utilization on all devices, run:

```
netq show cl-resource forwarding [around <text-time>] [json]
```

Use the `around` option to show this information for a time in the past.

This example shows the forwarding resources used by all switches and hosts.

```
cumulus@switch:~$ netq show cl-resource forwarding
Matching cl_resource records:
Hostname          IPv4 host entries    IPv6 host entries    IPv4 route entries   IPv6 route entries   ECMP nexthops        MAC entries          Total Mcast Routes   Last Updated
----------------- -------------------- -------------------- -------------------- -------------------- -------------------- -------------------- -------------------- ------------------------
spine02           9,16384(0%)          0,0(0%)              290,131072(0%)       173,20480(0%)        54,16330(0%)         26,32768(0%)         0,8192(0%)           Mon Jan 13 03:34:11 2020
```
<!-- need output for all devs -->
You can also view this same information in JSON format.

```
cumulus@switch:~$ netq spine02 show cl-resource forwarding  json
{
    "cl_resource": [
        {
            "macEntries": "26,32768(0%)",
            "ecmpNexthops": "54,16330(0%)",
            "ipv4HostEntries": "9,16384(0%)",
            "hostname": "spine02",
            "lastUpdated": 1578886451.884,
            "ipv4RouteEntries": "290,131072(0%)",
            "ipv6HostEntries": "0,0(0%)",
            "ipv6RouteEntries": "173,20480(0%)",
            "totalMcastRoutes": "0,8192(0%)"
	}
    ],
    "truncatedResult":false
}
```

### View SSD Utilization Networkwide

For NetQ Appliances that have 3ME3 solid state drives (SSDs) installed (primarily in on-premises deployments), you can view the utilization of the drive on-demand. An alarm is generated for drives that drop below 10% health, or have more than a two percent loss of health in 24 hours, indicating the need to rebalance the drive. Tracking SSD utilization over time enables you to see any downward trend or instability of the drive before you receive an alarm.

To view SDD utilization, run:

```
netq show cl-ssd-util [around <text-time>] [json]
```

This example shows the utilization for all devices which have this type of SSD.

```
cumulus@switch:~$ netq show cl-ssd-util
Hostname        Remaining PE Cycle (%)  Current PE Cycles executed      Total PE Cycles supported       SSD Model               Last Changed
spine02         80                      576                             2880                            M.2 (S42) 3ME3          Thu Oct 31 00:15:06 2019
```

This output indicates that the one drive found of this type, on the *spine02* switch, is in a good state overall with 80% of its PE cycles remaining. Use the `around` option to view this information around a particular time in the past.

### View Disk Storage After BTRFS Allocation Networkwide

Customers running Cumulus Linux 3.x which uses the BTRFS (b-tree file system) might experience issues with disk space management. This is a known problem of BTRFS because it does not perform periodic garbage collection, or rebalancing. If left unattended, these errors can make it impossible to rebalance the partitions on the disk. To avoid this issue, Cumulus Networks recommends rebalancing the BTRFS partitions in a preemptive manner, but only when absolutely needed to avoid reduction in the lifetime of the disk. By tracking the state of the disk space usage, users can determine when rebalancing should be performed.

For details about when a rebalance is recommended, refer to [When to Rebalance BTRFS Partitions]({{<ref "/knowledge-base/Configuration-and-Usage/Storage/When-to-Rebalance-BTRFS-Partitions" >}}).

To view the disk utilization and whether a rebalance is recommended, run:

```
netq show cl-btrfs-util [around <text-time>] [json]
```

This example shows the utilization on all devices:
<!-- need example with more than one device -->
```
cumulus@switch:~$ netq show cl-btrfs-info
Matching btrfs_info records:
Hostname          Device Allocated     Unallocated Space    Largest Chunk Size   Unused Data Chunks S Rebalance Recommende Last Changed
                                                                                 pace                 d
----------------- -------------------- -------------------- -------------------- -------------------- -------------------- -------------------------
leaf01            37.79 %              3.58 GB              588.5 MB             771.91 MB            yes                  Wed Sep 16 21:25:17 2020
```

Look for the **Rebalance Recommended** column. If the value in that column says *Yes*, then you are strongly encouraged to rebalance the BTRFS partitions. If it says *No*, then you can review the other values in the output to determine if you are getting close to needing a rebalance, and come back to view this data at a later time.

Optionally, use the `around` option to view the information for a particular time in the past.
