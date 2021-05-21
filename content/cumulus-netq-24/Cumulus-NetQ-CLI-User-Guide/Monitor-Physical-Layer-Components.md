---
title: Monitor Physical Layer Components
author: Cumulus Networks
weight: 530
toc: 3
---
With NetQ, a network administrator can monitor OSI Layer 1 physical
components on network devices, including interfaces, ports, links, and
peers. NetQ provides the ability to:

- Manage physical inventory: view the performance and status of  various components of a switch or host server
- Validate configurations: verify the configuration of network peers  and ports

It helps answer questions such as:

- Are any individual or bonded links down?
- Are any links flapping?
- Is there a link mismatch anywhere in my network?
- Which interface ports are empty?
- Which transceivers are installed?
- What is the peer for a given port?

NetQ uses [LLDP]({{<ref "/cumulus-linux-43/Layer-2/Link-Layer-Discovery-Protocol" >}}) (Link Layer Discovery Protocol) to collect port information. NetQ can also identify peer ports connected to DACs (Direct Attached Cables) and AOCs (Active Optical Cables) without using LLDP, even if the link is not UP.

## Monitor Physical Layer Inventory

Keeping track of the various physical layer components in your switches
and servers ensures you have a fully functioning network and provides
inventory management and audit capabilities. You can monitor ports,
transceivers, and cabling deployed on a per port (interface), per
vendor, per part number and so forth. NetQ enables you to view the
current status and the status an earlier point in time. From this
information, you can, among other things:

- determine which ports are empty versus which ones have cables
  plugged in and thereby validate expected connectivity
- audit transceiver and cable components used by vendor, giving you
  insights for estimated replacement costs, repair costs, overall
  costs, and so forth to improve your maintenance and purchasing
  processes
- identify changes in your physical layer, and when they occurred

The `netq show interfaces physical` command is used to obtain the
information from the devices. Its syntax is:

    netq [<hostname>] show interfaces physical [<physical-port>] [empty|plugged] [peer] [vendor <module-vendor>|model <module-model>|module] [around <text-time>] [json]
    netq [<hostname>] show events [level info|level error|level warning|level critical|level debug] type interfaces-physical [between <text-time> and <text-endtime>] [json]

{{%notice note%}}
When entering a time value, you must include a numeric value *and* the unit of measure:

- **w**: week(s)
- **d**: day(s)
- **h**: hour(s)
- **m**: minute(s)
- **s**: second(s)
- **now**

For the `between` option, the start (`<text-time>`) and end time (`text-endtime>`) values can be entered as most recent first and least recent second, or vice versa. The values do not have to have the same unit of measure.
{{%/notice%}}

### View Detailed Cable Information for All Devices

You can view what cables are connected to each interface port for all
devices, including the module type, vendor, part number and performance
characteristics. You can also view the cable information for a given
device by adding a hostname to the `show` command. This example shows
cable information and status for all interface ports on all devices.

    cumulus@switch:~$ netq show interfaces physical
    Matching cables records:
    Hostname          Interface                 State      Speed      AutoNeg Module    Vendor               Part No          Last Changed
    ----------------- ------------------------- ---------- ---------- ------- --------- -------------------- ---------------- -------------------------
    edge01            eth0                      up         1G         on      RJ45      n/a                  n/a              Fri Jun  7 00:42:52 2019
    edge01            eth1                      down       1G         off     RJ45      n/a                  n/a              Fri Jun  7 00:42:52 2019
    edge01            eth2                      down       1G         off     RJ45      n/a                  n/a              Fri Jun  7 00:42:52 2019
    edge01            vagrant                   down       1G         on      RJ45      n/a                  n/a              Fri Jun  7 00:42:52 2019
    exit01            eth0                      up         1G         off     RJ45      n/a                  n/a              Fri Jun  7 00:42:52 2019
    exit01            swp1                      down       Unknown    off     RJ45      n/a                  n/a              Fri Jun  7 00:43:03 2019
    exit01            swp44                     up         1G         off     RJ45      n/a                  n/a              Fri Jun  7 00:51:28 2019
    exit01            swp45                     down       Unknown    off     RJ45      n/a                  n/a              Fri Jun  7 00:43:03 2019
    exit01            swp46                     down       Unknown    off     RJ45      n/a                  n/a              Fri Jun  7 00:43:03 2019
    exit01            swp47                     down       Unknown    off     RJ45      n/a                  n/a              Fri Jun  7 00:43:03 2019
    exit01            swp48                     down       Unknown    off     RJ45      n/a                  n/a              Fri Jun  7 00:43:03 2019
    exit01            swp49                     down       Unknown    off     RJ45      n/a                  n/a              Fri Jun  7 00:43:03 2019
    exit01            swp50                     down       Unknown    off     RJ45      n/a                  n/a              Fri Jun  7 00:42:53 2019
    exit01            swp51                     up         1G         off     RJ45      n/a                  n/a              Fri Jun  7 00:51:28 2019
    exit01            swp52                     up         1G         off     RJ45      n/a                  n/a              Fri Jun  7 00:51:28 2019
    exit01            vagrant                   down       Unknown    off     RJ45      n/a                  n/a              Fri Jun  7 00:43:03 2019
    exit02            eth0                      up         1G         off     RJ45      n/a                  n/a              Fri Jun  7 00:42:51 2019
    exit02            swp1                      down       Unknown    off     RJ45      n/a                  n/a              Fri Jun  7 00:43:01 2019
    exit02            swp44                     up         1G         off     RJ45      n/a                  n/a              Fri Jun  7 00:51:28 2019
    exit02            swp45                     down       Unknown    off     RJ45      n/a                  n/a              Fri Jun  7 00:43:01 2019
    exit02            swp46                     down       Unknown    off     RJ45      n/a                  n/a              Fri Jun  7 00:43:01 2019
    exit02            swp47                     down       Unknown    off     RJ45      n/a                  n/a              Fri Jun  7 00:43:01 2019
    exit02            swp48                     down       Unknown    off     RJ45      n/a                  n/a              Fri Jun  7 00:43:01 2019
    exit02            swp49                     down       Unknown    off     RJ45      n/a                  n/a              Fri Jun  7 00:43:01 2019
    exit02            swp50                     down       Unknown    off     RJ45      n/a                  n/a              Fri Jun  7 00:43:01 2019
    exit02            swp51                     up         1G         off     RJ45      n/a                  n/a              Fri Jun  7 00:51:28 2019
    exit02            swp52                     up         1G         off     RJ45      n/a                  n/a              Fri Jun  7 00:51:28 2019
    exit02            vagrant                   down       Unknown    off     RJ45      n/a                  n/a              Fri Jun  7 00:43:01 2019
    leaf01            eth0                      up         1G         off     RJ45      n/a                  n/a              Fri Jun  7 00:43:02 2019
    leaf01            swp1                      up         1G         off     RJ45      n/a                  n/a              Fri Jun  7 00:52:03 2019
    leaf01            swp2                      up         1G         off     RJ45      n/a                  n/a              Fri Jun  7 00:52:03 2019
    ...

### View Detailed Module Information for a Given Device

You can view detailed information about the transceiver modules on each
interface port, including serial number, transceiver type, connector and
attached cable length. You can also view the module information for a
given device by adding a hostname to the `show` command. This example
shows the detailed module information for the interface ports on *leaf02*
switch.

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

### View Ports without Cables Connected for a Given Device

Checking for empty ports enables you to compare expected versus actual
deployment. This can be very helpful during deployment or during
upgrades. You can also view the cable information for a given device by
adding a hostname to the `show` command. This example shows the ports
that are empty on leaf01 switch.

    cumulus@switch:~$ netq leaf01 show interfaces physical empty
    Matching cables records are:
    Hostname         Interface State Speed      AutoNeg Module    Vendor           Part No          Last Changed
    ---------------- --------- ----- ---------- ------- --------- ---------------- ---------------- ------------------------
    leaf01           swp49     down  Unknown    on      empty     n/a              n/a              Thu Feb  7 22:49:37 2019
    leaf01           swp52     down  Unknown    on      empty     n/a              n/a              Thu Feb  7 22:49:37 2019

### View Ports with Cables Connected for a Given Device

In a similar manner as checking for empty ports, you can check for ports
that have cables connected, enabling you to compare expected versus
actual deployment. You can also view the cable information for a given
device by adding a hostname to the `show` command. If you add the around
keyword, you can view which interface ports had cables connected at a
previous time. This example shows the ports of *leaf01* switch that have
attached cables.

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

### View Components from a Given Vendor

By filtering for a specific cable vendor, you can collect information
such as how many ports use components from that vendor and when they
were last updated. This information may be useful when you run a cost
analysis of your network. This example shows all the ports that are
using components by an *OEM* vendor.

    cumulus@switch:~$ netq leaf01 show interfaces physical vendor OEM
    Matching cables records:
    Hostname          Interface                 State      Speed      AutoNeg Module    Vendor               Part No          Last Changed
    ----------------- ------------------------- ---------- ---------- ------- --------- -------------------- ---------------- -------------------------
    leaf01            swp33                     down       10G        off     SFP       OEM                  SFP-H10GB-CU1M   Thu Feb  7 22:49:37 2019
    leaf01            swp36                     down       10G        off     SFP       OEM                  SFP-H10GB-CU1M   Thu Feb  7 22:49:37 2019
    leaf01            swp37                     down       10G        off     SFP       OEM                  SFP-H10GB-CU1M   Thu Feb  7 22:49:37 2019
    leaf01            swp38                     down       10G        off     SFP       OEM                  SFP-H10GB-CU1M   Thu Feb  7 22:49:37 2019

### View All Devices Using a Given Component

You can view all of the devices with ports using a particular component.
This could be helpful when you need to change out a particular component
for possible failure issues, upgrades, or cost reasons. This example
first determines which models (part numbers) exist on all of the devices
and then those devices with a part number of QSFP-H40G-CU1M installed.

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

### View Changes to Physical Components

Because components are often changed, NetQ enables you to determine
what, if any, changes have been made to the physical components on your
devices. This can be helpful during deployments or upgrades.

You can select how far back in time you want to go, or select a time
range using the between keyword. Note that time values must include
units to be valid. If no changes are found, a "No matching cable records
found" message is displayed. This example illustrates each of these
scenarios for all devices in the network.

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

### View Interface Statistics

The `ethtool` command provides a wealth of statistics about network interfaces.
The `netq show ethtool-stats` command returns statistics about a given node and
interface, including frame errors, ACL drops, buffer drops and more.

You can use the `around` option to view the information for a particular time.
If no changes are found, a "No matching ethtool_stats records found" message is
displayed. This example illustrates the statistics for switch port swp1 on a
specific switch in the network.

```
cumulus@switch:~$ netq myswitch show ethtool-stats swp1
Matching ethtool_stats records:
Hostname          Interface                 HwIfInOctets         HwIfInUcastPkts      HwIfInBcastPkts      HwIfInMcastPkts      HwIfInDiscards       HwIfInL3Drops        HwIfInBufferDrops    HwIfInAclDrops       HwIfInDot3LengthErro HwIfInErrors         SoftInErrors         SoftInDrops          SoftInFrameErrors    HwIfInDot3FrameError HwIfInPausePkt       HwIfInPfc0Pkt        HwIfInPfc1Pkt        HwIfInPfc2Pkt        HwIfInPfc3Pkt        HwIfInPfc4Pkt        HwIfInPfc5Pkt        HwIfInPfc6Pkt        HwIfInPfc7Pkt        HwIfOutOctets        HwIfOutUcastPkts     HwIfOutMcastPkts     HwIfOutBcastPkts     HwIfOutDiscards      HwIfOutErrors        HwIfOutQDrops        HwIfOutNonQDrops     SoftOutErrors        SoftOutDrops         SoftOutTxFifoFull    HwIfOutQLen          HwIfOutPausePkt      HwIfOutPfc0Pkt       HwIfOutPfc1Pkt       HwIfOutPfc2Pkt       HwIfOutPfc3Pkt       HwIfOutPfc4Pkt       HwIfOutPfc5Pkt       HwIfOutPfc6Pkt       HwIfOutPfc7Pkt       HwIfOutWredDrops     HwIfOutQ0WredDrops   HwIfOutQ1WredDrops   HwIfOutQ2WredDrops   HwIfOutQ3WredDrops   HwIfOutQ4WredDrops   HwIfOutQ5WredDrops   HwIfOutQ6WredDrops   HwIfOutQ7WredDrops   HwIfOutQ8WredDrops   HwIfOutQ9WredDrops   Last Updated
                                                                                                                                                                                                                    rs                                                                                                       s
----------------- ------------------------- -------------------- -------------------- -------------------- -------------------- -------------------- -------------------- -------------------- -------------------- -------------------- -------------------- -------------------- -------------------- -------------------- -------------------- -------------------- -------------------- -------------------- -------------------- -------------------- -------------------- -------------------- -------------------- -------------------- -------------------- -------------------- -------------------- -------------------- -------------------- -------------------- -------------------- -------------------- -------------------- -------------------- -------------------- -------------------- -------------------- -------------------- -------------------- -------------------- -------------------- -------------------- -------------------- -------------------- -------------------- -------------------- -------------------- -------------------- -------------------- -------------------- -------------------- -------------------- -------------------- -------------------- -------------------- -------------------- ------------------------
myswitch          swp1                      779659596            6679291              0                    1883805              4                    0                    0                    0                    0                    0                    0                    0                    0                    0                    0                    0                    0                    0                    0                    0                    0                    0                    0                    733672563            6650334              1268403              0                    0                    0                    0                    0                    0                    0                    0                    0                    0                    0                    0                    0                    0                    0                    0                    0                    0                    0                    0                    0                    0                    0                    0                    0                    0                    0                    0                    0                    Wed Feb 12 00:50:12 2020
```

You can generate the output in JSON format:

```
cumulus@switch:~$ netq myswitch show ethtool-stats swp1 json
{
    "ethtool_stats":[
        {
            "hwifoutpfc4pkt":0,
            "hwifoutq7wreddrops":0,
            "softinerrors":0,
            "hwifoutpfc6pkt":0,
            "hwifoutmcastpkts":1268403,
            "hwifoutpfc5pkt":0,
            "interface":"swp1",
            "hwifinpausepkt":0,
            "hwifoutq9wreddrops":0,
            "hwifinucastpkts":6679291,
            "hwifoutq0wreddrops":0,
            "hwifindot3lengtherrors":0,
            "hwifinbcastpkts":0,
            "hwifinpfc2pkt":0,
            "hwifinpfc0pkt":0,
            "softindrops":0,
            "hwifoutpfc3pkt":0,
            "hwifoutq4wreddrops":0,
            "hostname":"act-4610-54t-08",
            "hwifoutq3wreddrops":0,
            "hwifinpfc5pkt":0,
            "hwifoutdiscards":0,
            "hwifouterrors":0,
            "hwifoutqdrops":0,
            "hwifoutucastpkts":6650334,
            "hwifinpfc7pkt":0,
            "hwifinbufferdrops":0,
            "hwifoutbcastpkts":0,
            "hwifoutpfc2pkt":0,
            "hwifinl3drops":0,
            "hwifinpfc4pkt":0,
            "hwifoutpausepkt":0,
            "hwifoutq6wreddrops":0,
            "hwifoutnonqdrops":0,
            "hwifoutpfc1pkt":0,
            "hwifoutpfc0pkt":0,
            "lastUpdated":1581468612.0,
            "hwifoutoctets":733672563,
            "softinframeerrors":0,
            "hwifoutq5wreddrops":0,
            "hwifinerrors":0,
            "hwifoutpfc7pkt":0,
            "hwifoutq1wreddrops":0,
            "hwifinpfc6pkt":0,
            "hwifinpfc1pkt":0,
            "softouterrors":0,
            "softoutdrops":0,
            "hwifoutwreddrops":0,
            "hwifinacldrops":0,
            "softouttxfifofull":0,
            "hwifinmcastpkts":1883805,
            "hwifoutqlen":0,
            "hwifoutq8wreddrops":0,
            "hwifinpfc3pkt":0,
            "hwifoutq2wreddrops":0,
            "hwifindiscards":4,
            "hwifinoctets":779659596,
            "hwifindot3frameerrors":0
	}
    ],
    "truncatedResult":false
}
```

## Validate Physical Layer Configuration

Beyond knowing what physical components are deployed, it is valuable to
know that they are configured and operating correctly. NetQ enables you
to confirm that peer connections are present, discover any misconfigured
ports, peers, or unsupported modules, and monitor for link flaps.

NetQ checks peer connections using LLDP. For DACs and AOCs, NetQ
determines the peers using their serial numbers in the port EEPROMs,
even if the link is not UP.

### Confirm Peer Connections

You can validate peer connections for all devices in your network or for
a specific device or port. This example shows the peer hosts and their
status for leaf03 switch.

```
cumulus@switch:~$ netq leaf03 show interfaces physical peer
Matching cables records:
Hostname          Interface                 Peer Hostname     Peer Interface            State      Message
----------------- ------------------------- ----------------- ------------------------- ---------- -----------------------------------
leaf03            swp1                      oob-mgmt-switch   swp7                      up                                
leaf03            swp2                                                                  down       Peer port unknown                             
leaf03            swp47                     leaf04            swp47                     up                                
leaf03            swp48                     leaf04            swp48                     up              
leaf03            swp49                     leaf04            swp49                     up                                
leaf03            swp50                     leaf04            swp50                     up                                
leaf03            swp51                     exit01            swp51                     up                                
leaf03            swp52                                                                 down       Port cage empty                                
```

This example shows the peer data for a specific interface port.

```
cumulus@switch:~$ netq leaf01 show interfaces physical swp47
Matching cables records:
Hostname          Interface                 Peer Hostname     Peer Interface            State      Message
----------------- ------------------------- ----------------- ------------------------- ---------- -----------------------------------
leaf01            swp47                     leaf02            swp47                     up   
```

### Discover Misconfigurations

You can verify that the following configurations are the same on both
sides of a peer interface:

  - Admin state
  - Operational state
  - Link speed
  - Auto-negotiation setting

The `netq check interfaces` command is used to determine if any of the
interfaces have any continuity errors. This command only checks the
physical interfaces; it does not check bridges, bonds or other software
constructs. You can check all interfaces at once. It enables you to
compare the current status of the interfaces, as well as their status at
an earlier point in time. The command syntax is:

```
netq check interfaces [around <text-time>] [json]
```

{{%notice tip%}}

If NetQ cannot determine a peer for a given device, the port is marked
as *unverified*.

{{%/notice%}}

If you find a misconfiguration, use the `netq show interfaces physical`
command for clues about the cause.

**Example: Find Mismatched Operational States**

In this example, we check all of the interfaces for misconfigurations
and we find that one interface port has an error. We look for clues
about the cause and see that the Operational states do not match on the
connection between leaf 03 and leaf04: leaf03 is up, but leaf04 is down.
If the misconfiguration was due to a mismatch in the administrative
state, the message would have been *Admin state mismatch (up, down)* or
*Admin state mismatch (down, up)*.

```
cumulus@switch:~$ netq check interfaces
Checked Nodes: 18, Failed Nodes: 8
Checked Ports: 741, Failed Ports: 1, Unverified Ports: 414
 
cumulus@switch:~$ netq show interfaces physical peer
Matching cables records:
Hostname          Interface                 Peer Hostname     Peer Interface            Message
----------------- ------------------------- ----------------- ------------------------- -----------------------------------
...
leaf03            swp1                      oob-mgmt-switch   swp7                                                      
leaf03            swp2                                                                  Peer port unknown                             
leaf03            swp47                     leaf04            swp47                                                     
leaf03            swp48                     leaf04            swp48                     State mismatch (up, down)     
leaf03            swp49                     leaf04            swp49                                                     
leaf03            swp50                     leaf04            swp50                                                     
leaf03            swp52                                                                 Port cage empty                                    
...   
```

**Example: Find Mismatched Peers**

This example uses the *and* keyword to check the connections between two
peers. An error is seen, so we check the physical peer information and
discover that the incorrect peer has been specified. After fixing it, we
run the check again, and see that there are no longer any interface
errors.

    cumulus@switch:~$ netq check interfaces
    Checked Nodes: 1, Failed Nodes: 1
    Checked Ports: 1, Failed Ports: 1, Unverified Ports: 0
    cumulus@switch:~$ netq show interfaces physical peer
     
    Matching cables records:
    Hostname          Interface                 Peer Hostname     Peer Interface            Message
    ----------------- ------------------------- ----------------- ------------------------- -----------------------------------
    leaf01            swp50                     leaf04            swp49                     Incorrect peer specified. Real peer
                                                                                            is leaf04 swp50      
     
    cumulus@switch:~$ netq check interfaces
    Checked Nodes: 1, Failed Nodes: 0
    Checked Ports: 1, Failed Ports: 0, Unverified Ports: 0

**Example: Find Mismatched Link Speeds**

This example checks for for configuration mismatches and finds a link
speed mismatch on server03. The link speed on swp49 is *40G* and the
peer port swp50 is *unspecified*.

    cumulus@switch:~$ netq check interfaces
    Checked Nodes: 10, Failed Nodes: 1
    Checked Ports: 125, Failed Ports: 2, Unverified Ports: 35
    Hostname          Interface                 Peer Hostname     Peer Interface            Message
    ----------------- ------------------------- ----------------- ------------------------- -----------------------------------
    server03          swp49                     server03          swp50                     Speed mismatch (40G, Unknown)      
    server03          swp50                     server03          swp49                     Speed mismatch (Unknown, 40G)  

**Example: Find Mismatched Auto-negotiation Settings**

This example checks for configuration mismatches and finds
auto-negotation setting mismatches between the servers and leafs.
Auto-negotiation is *off* on the leafs, but *on* on the servers.

    cumulus@switch:~$ netq check interfaces
    Checked Nodes: 15, Failed Nodes: 8
    Checked Ports: 118, Failed Ports: 8, Unverified Ports: 94
    Hostname          Interface                 Peer Hostname     Peer Interface            Message
    ----------------- ------------------------- ----------------- ------------------------- -----------------------------------
    leaf01            swp1                      server01          eth1                      Autoneg mismatch (off, on)         
    leaf02            swp2                      server02          eth2                      Autoneg mismatch (off, on)         
    leaf03            swp1                      server03          eth1                      Autoneg mismatch (off, on)         
    leaf04            swp2                      server04          eth2                      Autoneg mismatch (off, on)         
    server01          eth1                      leaf01            swp1                      Autoneg mismatch (on, off)         
    server02          eth2                      leaf02            swp2                      Autoneg mismatch (on, off)         
    server03          eth1                      leaf03            swp1                      Autoneg mismatch (on, off)         
    server04          eth2                      leaf04            swp2                      Autoneg mismatch (on, off)         

### Identify Flapping Links

You can also determine whether a link is flapping using the `netq check
interfaces` command. If a link is flapping, NetQ indicates this in a
message:

```
cumulus@switch:~$ netq check interfaces
Checked Nodes: 18, Failed Nodes: 8
Checked Ports: 741, Failed Ports: 1, Unverified Ports: 414
 
Matching cables records:
Hostname          Interface                 Peer Hostname     Peer Interface            Message
----------------- ------------------------- ----------------- ------------------------- -----------------------------------
leaf02            -                         -                 -                         Link flapped 11 times in last 5
                                                                                        mins                    
```
