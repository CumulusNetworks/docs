---
title: Monitor Switch Inventory
author: Cumulus Networks
weight: 620
toc: 4
---
With the NetQ UI and NetQ CLI, you can monitor the inventory of individual switches separately from the network. A user can monitor such items as operating system, motherboard, ASIC, microprocessor, disk, memory, fan and power supply information. Being able to monitor this inventory aids in upgrades, compliance, and other planning tasks.

The commands and cards available to obtain this type of information help you to answer questions such as:

- What hardware is installed on my switches?
- How many transmit and receive packets have been dropped?
- How healthy are the fans and power supply?
- What software is installed on my switch?
- What is the ACL and forwarding resources usage?

To monitor network-wide inventory, refer to {{<link title="Monitor Network Inventory">}}.

To view the network or device performance data, refer to {{<link title="Monitor Network and Device Performance">}}.

## Access Switch Inventory Data

The Cumulus NetQ UI provides the Inventory | Switches card for monitoring the hardware and software component inventory on switches running NetQ in your network. Access this card from the Cumulus Workbench, or add it to your own workbench by clicking <img src="https://icons.cumulusnetworks.com/44-Entertainment-Events-Hobbies/02-Card-Games/card-game-diamond.svg" height="18" width="18"/> (Add card) > **Inventory**  > Inventory|Switches card > **Open Cards**.

{{<figure src="/images/netq/inventory-switch-medium-320.png" width="200">}}

The CLI provides detailed switch inventory information through its `netq <hostname> show inventory` command.

## View Switch Inventory Summary

Component information for all of the switches in your network can be viewed from either the NetQ UI or NetQ CLI.

{{< tabs "TabID25" >}}

{{< tab "NetQ UI" >}}

{{< /tab >}}

{{< tab "NetQ CLI" >}}

To view the hardware and software components for a switch, run:

```
netq <hostname> show inventory brief
```

This example shows the type of switch (Cumulus VX), operating system (Cumulus Linux), CPU (x86_62), and ASIC (virtual) for the *spine01* switch.

```
cumulus@switch:~$ netq spine01 show inventory brief
Matching inventory records:
Hostname          Switch               OS              CPU      ASIC            Ports
----------------- -------------------- --------------- -------- --------------- -----------------------------------
spine01           VX                   CL              x86_64   VX              N/A
```

{{< /tab >}}

{{< /tabs >}}

## View Hardware Inventory on a Given Switch

You can view all hardware components or narrow your view to specific hardware components for a given switch.

Switch component inventory can be viewed from either the NetQ CLI or NetQ UI.

{{< tabs "TabID47" >}}

{{< tab "NetQ CLI" >}}

To view switch components, run:

```
netq <hostname> show inventory brief
```

This example shows

### View Information about the ASIC on all Switches

You can view the vendor, model, model identifier, core bandwidth
capability, and ports of the ASIC installed on your switch motherboard.
This example shows all of these for all devices.

    cumulus@switch:~$ netq show inventory asic
    Matching inventory records:
    Hostname          Vendor               Model                          Model ID                  Core BW        Ports
    ----------------- -------------------- ------------------------------ ------------------------- -------------- -----------------------------------
    dell-z9100-05     Broadcom             Tomahawk                       BCM56960                  2.0T           32 x 100G-QSFP28
    mlx-2100-05       Mellanox             Spectrum                       MT52132                   N/A            16 x 100G-QSFP28
    mlx-2410a1-05     Mellanox             Spectrum                       MT52132                   N/A            48 x 25G-SFP28 & 8 x 100G-QSFP28
    mlx-2700-11       Mellanox             Spectrum                       MT52132                   N/A            32 x 100G-QSFP28
    qct-ix1-08        Broadcom             Tomahawk                       BCM56960                  2.0T           32 x 100G-QSFP28
    qct-ix7-04        Broadcom             Trident3                       BCM56870                  N/A            32 x 100G-QSFP28
    qct-ix7-04        N/A                  N/A                            N/A                       N/A            N/A
    st1-l1            Broadcom             Trident2                       BCM56854                  720G           48 x 10G-SFP+ & 6 x 40G-QSFP+
    st1-l2            Broadcom             Trident2                       BCM56854                  720G           48 x 10G-SFP+ & 6 x 40G-QSFP+
    st1-l3            Broadcom             Trident2                       BCM56854                  720G           48 x 10G-SFP+ & 6 x 40G-QSFP+
    st1-s1            Broadcom             Trident2                       BCM56850                  960G           32 x 40G-QSFP+
    st1-s2            Broadcom             Trident2                       BCM56850                  960G           32 x 40G-QSFP+

You can filter the results of the command to view devices with a
particular characteristic. This example shows all devices that use a
Broadcom ASIC.

    cumulus@switch:~$ netq show inventory asic vendor Broadcom
    Matching inventory records:
    Hostname          Vendor               Model                          Model ID                  Core BW        Ports
    ----------------- -------------------- ------------------------------ ------------------------- -------------- -----------------------------------
    dell-z9100-05     Broadcom             Tomahawk                       BCM56960                  2.0T           32 x 100G-QSFP28
    qct-ix1-08        Broadcom             Tomahawk                       BCM56960                  2.0T           32 x 100G-QSFP28
    qct-ix7-04        Broadcom             Trident3                       BCM56870                  N/A            32 x 100G-QSFP28
    st1-l1            Broadcom             Trident2                       BCM56854                  720G           48 x 10G-SFP+ & 6 x 40G-QSFP+
    st1-l2            Broadcom             Trident2                       BCM56854                  720G           48 x 10G-SFP+ & 6 x 40G-QSFP+
    st1-l3            Broadcom             Trident2                       BCM56854                  720G           48 x 10G-SFP+ & 6 x 40G-QSFP+
    st1-s1            Broadcom             Trident2                       BCM56850                  960G           32 x 40G-QSFP+
    st1-s2            Broadcom             Trident2                       BCM56850                  960G           32 x 40G-QSFP+

You can filter the results of the command view the ASIC information for
a particular switch. This example shows the ASIC information for
*st1-11* switch.

    cumulus@switch:~$ netq leaf02 show inventory asic
    Matching inventory records:
    Hostname          Vendor               Model                          Model ID                  Core BW        Ports
    ----------------- -------------------- ------------------------------ ------------------------- -------------- -----------------------------------
    st1-l1            Broadcom             Trident2                       BCM56854                  720G           48 x 10G-SFP+ & 6 x 40G-QSFP+

### View Information about the Motherboard in a Switch

You can view the vendor, model, base MAC address, serial number, part
number, revision, and manufacturing date for a switch motherboard on a
single device or on all devices. This example shows all of the
motherboard data for all devices.

    cumulus@switch:~$ netq show inventory board
    Matching inventory records:
    Hostname          Vendor               Model                          Base MAC           Serial No                 Part No          Rev    Mfg Date
    ----------------- -------------------- ------------------------------ ------------------ ------------------------- ---------------- ------ ----------
    dell-z9100-05     DELL                 Z9100-ON                       4C:76:25:E7:42:C0  CN03GT5N779315C20001      03GT5N           A00    12/04/2015
    mlx-2100-05       Penguin              Arctica 1600cs                 7C:FE:90:F5:61:C0  MT1623X10078              MSN2100-CB2FO    N/A    06/09/2016
    mlx-2410a1-05     Mellanox             SN2410                         EC:0D:9A:4E:55:C0  MT1734X00067              MSN2410-CB2F_QP3 N/A    08/24/2017
    mlx-2700-11       Penguin              Arctica 3200cs                 44:38:39:00:AB:80  MT1604X21036              MSN2700-CS2FO    N/A    01/31/2016
    qct-ix1-08        QCT                  QuantaMesh BMS T7032-IX1       54:AB:3A:78:69:51  QTFCO7623002C             1IX1UZZ0ST6      H3B    05/30/2016
    qct-ix7-04        QCT                  IX7                            D8:C4:97:62:37:65  QTFCUW821000A             1IX7UZZ0ST5      B3D    05/07/2018
    qct-ix7-04        QCT                  T7032-IX7                      D8:C4:97:62:37:65  QTFCUW821000A             1IX7UZZ0ST5      B3D    05/07/2018
    st1-l1            CELESTICA            Arctica 4806xp                 00:E0:EC:27:71:37  D2060B2F044919GD000011    R0854-F1004-01   Redsto 09/20/2014
                                                                                                                                        ne-XP
    st1-l2            CELESTICA            Arctica 4806xp                 00:E0:EC:27:6B:3A  D2060B2F044919GD000060    R0854-F1004-01   Redsto 09/20/2014
                                                                                                                                        ne-XP
    st1-l3            Penguin              Arctica 4806xp                 44:38:39:00:70:49  N/A                       N/A              N/A    N/A
    st1-s1            Dell                 S6000-ON                       44:38:39:00:80:00  N/A                       N/A              N/A    N/A
    st1-s2            Dell                 S6000-ON                       44:38:39:00:80:81  N/A                       N/A              N/A    N/A

You can filter the results of the command to capture only those devices
with a particular motherboard vendor. This example shows only the
devices with *Celestica* motherboards.

    cumulus@switch:~$ netq show inventory board vendor celestica
    Matching inventory records:
    Hostname          Vendor               Model                          Base MAC           Serial No                 Part No          Rev    Mfg Date
    ----------------- -------------------- ------------------------------ ------------------ ------------------------- ---------------- ------ ----------
    st1-l1            CELESTICA            Arctica 4806xp                 00:E0:EC:27:71:37  D2060B2F044919GD000011    R0854-F1004-01   Redsto 09/20/2014
                                                                                                                                        ne-XP
    st1-l2            CELESTICA            Arctica 4806xp                 00:E0:EC:27:6B:3A  D2060B2F044919GD000060    R0854-F1004-01   Redsto 09/20/2014
                                                                                                                                        ne-XP

You can filter the results of the command to view the model for a
particular switch. This example shows the motherboard vendor for the
*st1-s1* switch.

    cumulus@switch:~$ netq st1-s1 show inventory board
    Matching inventory records:
    Hostname          Vendor               Model                          Base MAC           Serial No                 Part No          Rev    Mfg Date
    ----------------- -------------------- ------------------------------ ------------------ ------------------------- ---------------- ------ ----------
    st1-s1            Dell                 S6000-ON                       44:38:39:00:80:00  N/A                       N/A              N/A    N/A

### View Information about the CPU on a Switch

You can view the architecture, model, operating frequency, and the
number of cores for the CPU on a single device or for all devices. This
example shows these CPU characteristics for all devices.

    cumulus@nswitch:~$ netq show inventory cpu
    Matching inventory records:
    Hostname          Arch     Model                          Freq       Cores
    ----------------- -------- ------------------------------ ---------- -----
    dell-z9100-05     x86_64   Intel(R) Atom(TM) C2538        2.40GHz    4
    mlx-2100-05       x86_64   Intel(R) Atom(TM) C2558        2.40GHz    4
    mlx-2410a1-05     x86_64   Intel(R) Celeron(R)  1047UE    1.40GHz    2
    mlx-2700-11       x86_64   Intel(R) Celeron(R)  1047UE    1.40GHz    2
    qct-ix1-08        x86_64   Intel(R) Atom(TM) C2558        2.40GHz    4
    qct-ix7-04        x86_64   Intel(R) Atom(TM) C2558        2.40GHz    4
    st1-l1            x86_64   Intel(R) Atom(TM) C2538        2.41GHz    4
    st1-l2            x86_64   Intel(R) Atom(TM) C2538        2.41GHz    4
    st1-l3            x86_64   Intel(R) Atom(TM) C2538        2.40GHz    4
    st1-s1            x86_64   Intel(R) Atom(TM)  S1220       1.60GHz    4
    st1-s2            x86_64   Intel(R) Atom(TM)  S1220       1.60GHz    4

You can filter the results of the command to view which switches employ
a particular CPU architecture using the *arch* keyword. This example
shows how to determine which architectures are deployed in your network,
and then shows all devices with an *x86\_64* architecture.

    cumulus@switch:~$ netq show inventory cpu arch
        x86_64  :  CPU Architecture
     
    cumulus@switch:~$ netq show inventory cpu arch x86_64
    Matching inventory records:
    Hostname          Arch     Model                          Freq       Cores
    ----------------- -------- ------------------------------ ---------- -----
    leaf01            x86_64   Intel Core i7 9xx (Nehalem Cla N/A        1
                               ss Core i7)
    leaf02            x86_64   Intel Core i7 9xx (Nehalem Cla N/A        1
                               ss Core i7)
    leaf03            x86_64   Intel Core i7 9xx (Nehalem Cla N/A        1
                               ss Core i7)
    leaf04            x86_64   Intel Core i7 9xx (Nehalem Cla N/A        1
                               ss Core i7)
    oob-mgmt-server   x86_64   Intel Core i7 9xx (Nehalem Cla N/A        1
                               ss Core i7)
    server01          x86_64   Intel Core i7 9xx (Nehalem Cla N/A        1
                               ss Core i7)
    server02          x86_64   Intel Core i7 9xx (Nehalem Cla N/A        1
                               ss Core i7)
    server03          x86_64   Intel Core i7 9xx (Nehalem Cla N/A        1
                               ss Core i7)
    server04          x86_64   Intel Core i7 9xx (Nehalem Cla N/A        1
                               ss Core i7)
    spine01           x86_64   Intel Core i7 9xx (Nehalem Cla N/A        1
                               ss Core i7)
    spine02           x86_64   Intel Core i7 9xx (Nehalem Cla N/A        1
                               ss Core i7)

You can filter the results to view CPU information for a single switch,
as shown here for *server02*.

    cumulus@switch:~$ netq server02 show inventory cpu
     
    Matching inventory records:
    Hostname          Arch     Model                          Freq       Cores
    ----------------- -------- ------------------------------ ---------- -----
    server02          x86_64   Intel Core i7 9xx (Nehalem Cla N/A        1
                               ss Core i7)

### View Information about the Disk on a Switch

You can view the name or operating system, type, transport, size,
vendor, and model of the disk on a single device or all devices. This
example shows all of these disk characteristics for all devices.

    cumulus@switch:~$ netq show inventory disk
    Matching inventory records:
    Hostname          Name            Type             Transport          Size       Vendor               Model
    ----------------- --------------- ---------------- ------------------ ---------- -------------------- ------------------------------
    leaf01            vda             disk             N/A                6G         0x1af4               N/A
    leaf02            vda             disk             N/A                6G         0x1af4               N/A
    leaf03            vda             disk             N/A                6G         0x1af4               N/A
    leaf04            vda             disk             N/A                6G         0x1af4               N/A
    oob-mgmt-server   vda             disk             N/A                256G       0x1af4               N/A
    server01          vda             disk             N/A                301G       0x1af4               N/A
    server02          vda             disk             N/A                301G       0x1af4               N/A
    server03          vda             disk             N/A                301G       0x1af4               N/A
    server04          vda             disk             N/A                301G       0x1af4               N/A
    spine01           vda             disk             N/A                6G         0x1af4               N/A
    spine02           vda             disk             N/A                6G         0x1af4               N/A

You can filter the results of the command to view the disk information
for a particular device. This example shows disk information for
*leaf03* switch.

    cumulus@switch:~$ netq leaf03 show inventory disk
    Matching inventory records:
    Hostname          Name            Type             Transport          Size       Vendor               Model
    ----------------- --------------- ---------------- ------------------ ---------- -------------------- ------------------------------
    leaf03            vda             disk             N/A                6G         0x1af4               N/A

### View Memory Information for a Switch

You can view the name, type, size, speed, vendor, and serial number for
the memory installed in a single device or all devices. This example
shows all of these characteristics for all devices.

    cumulus@switch:~$ netq show inventory memory
    Matching inventory records:
    Hostname          Name            Type             Size       Speed      Vendor               Serial No
    ----------------- --------------- ---------------- ---------- ---------- -------------------- -------------------------
    dell-z9100-05     DIMM0 BANK 0    DDR3             8192 MB    1600 MHz   Hynix                14391421
    mlx-2100-05       DIMM0 BANK 0    DDR3             8192 MB    1600 MHz   InnoDisk Corporation 00000000
    mlx-2410a1-05     ChannelA-DIMM0  DDR3             8192 MB    1600 MHz   017A                 87416232
                      BANK 0
    mlx-2700-11       ChannelA-DIMM0  DDR3             8192 MB    1600 MHz   017A                 73215444
                      BANK 0
    mlx-2700-11       ChannelB-DIMM0  DDR3             8192 MB    1600 MHz   017A                 73215444
                      BANK 2
    qct-ix1-08        N/A             N/A              7907.45MB  N/A        N/A                  N/A
    qct-ix7-04        DIMM0 BANK 0    DDR3             8192 MB    1600 MHz   Transcend            00211415
    st1-l1            DIMM0 BANK 0    DDR3             4096 MB    1333 MHz   N/A                  N/A
    st1-l2            DIMM0 BANK 0    DDR3             4096 MB    1333 MHz   N/A                  N/A
    st1-l3            DIMM0 BANK 0    DDR3             4096 MB    1600 MHz   N/A                  N/A
    st1-s1            A1_DIMM0 A1_BAN DDR3             8192 MB    1333 MHz   A1_Manufacturer0     A1_SerNum0
                      K0
    st1-s2            A1_DIMM0 A1_BAN DDR3             8192 MB    1333 MHz   A1_Manufacturer0     A1_SerNum0
                      K0

You can filter the results of the command to view devices with a
particular memory type or vendor. This example shows all of the devices
with memory from *QEMU* .

    cumulus@switch:~$ netq show inventory memory vendor QEMU
    Matching inventory records:
    Hostname          Name            Type             Size       Speed      Vendor               Serial No
    ----------------- --------------- ---------------- ---------- ---------- -------------------- -------------------------
    leaf01            DIMM 0          RAM              1024 MB    Unknown    QEMU                 Not Specified
    leaf02            DIMM 0          RAM              1024 MB    Unknown    QEMU                 Not Specified
    leaf03            DIMM 0          RAM              1024 MB    Unknown    QEMU                 Not Specified
    leaf04            DIMM 0          RAM              1024 MB    Unknown    QEMU                 Not Specified
    oob-mgmt-server   DIMM 0          RAM              4096 MB    Unknown    QEMU                 Not Specified
    server01          DIMM 0          RAM              512 MB     Unknown    QEMU                 Not Specified
    server02          DIMM 0          RAM              512 MB     Unknown    QEMU                 Not Specified
    server03          DIMM 0          RAM              512 MB     Unknown    QEMU                 Not Specified
    server04          DIMM 0          RAM              512 MB     Unknown    QEMU                 Not Specified
    spine01           DIMM 0          RAM              1024 MB    Unknown    QEMU                 Not Specified
    spine02           DIMM 0          RAM              1024 MB    Unknown    QEMU                 Not Specified

You can filter the results to view memory information for a single
switch, as shown here for leaf01.

    cumulus@switch:~$ netq leaf01 show inventory memory
     
    Matching inventory records:
    Hostname          Name            Type             Size       Speed      Vendor               Serial No
    ----------------- --------------- ---------------- ---------- ---------- -------------------- -------------------------
    leaf01            DIMM 0          RAM              1024 MB    Unknown    QEMU                 Not Specified

### View a Summary of Physical Inventory for the NetQ or NetQ Cloud Appliance

Using the `opta` option lets you view inventory information for the NetQ or NetQ Cloud Appliance(s) rather than all network nodes. This example give you a summary of the inventory on the device.

```
cumulus@spine-1:mgmt-vrf:~$ netq show inventory brief opta

Matching inventory records:
Hostname          Switch               OS              CPU      ASIC            Ports
----------------- -------------------- --------------- -------- --------------- -----------------------------------
10-20-14-158      VX                   CL              x86_64   VX              N/A

```

### View Memory for the NetQ or NetQ Cloud Appliance

You can be specific about which inventory item you want to view for an appliance. This example shows the memory information for a NetQ Appliance, letting you verify you have sufficient memory.

```
cumulus@netq-appliance:~$ netq show inventory memory opta
Matching inventory records:
Hostname          Name            Type             Size       Speed      Vendor               Serial No
----------------- --------------- ---------------- ---------- ---------- -------------------- -------------------------
netq-app          DIMM 0          RAM              64 GB      Unknown    QEMU                 Not Specified

```

## View Fan Health for All Switches

Fan, power supply unit, and temperature sensors are available to provide
additional data about the NetQ Platform operation. To view the health of
fans in your switches, use the `netq show sensors fan` command. If you
name the fans in all of your switches consistently, you can view more
information at once.

In this example, we look at the state of all fans with the name *fan1*.

    cumulus@switch:~$ netq show sensors fan fan1
    Hostname          Name            Description                         State      Speed      Max      Min      Message                             Last Changed
    ----------------- --------------- ----------------------------------- ---------- ---------- -------- -------- ----------------------------------- -------------------------
    exit01            fan1            fan tray 1, fan 1                   ok         2500       29000    2500                                         Fri Apr 19 16:01:17 2019
    exit02            fan1            fan tray 1, fan 1                   ok         2500       29000    2500                                         Fri Apr 19 16:01:33 2019
    leaf01            fan1            fan tray 1, fan 1                   ok         2500       29000    2500                                         Sun Apr 21 20:07:12 2019
    leaf02            fan1            fan tray 1, fan 1                   ok         2500       29000    2500                                         Fri Apr 19 16:01:41 2019
    leaf03            fan1            fan tray 1, fan 1                   ok         2500       29000    2500                                         Fri Apr 19 16:01:44 2019
    leaf04            fan1            fan tray 1, fan 1                   ok         2500       29000    2500                                         Fri Apr 19 16:01:36 2019
    spine01           fan1            fan tray 1, fan 1                   ok         2500       29000    2500                                         Fri Apr 19 16:01:52 2019
    spine02           fan1            fan tray 1, fan 1                   ok         2500       29000    2500                                         Fri Apr 19 16:01:08 2019

{{%notice tip%}}

Use tab completion to determine the names of the fans in your switches:

```
cumulus@switch:~$ netq show sensors fan <<press tab>>
   around : Go back in time to around ...
   fan1 : Fan Name
   fan2 : Fan Name
   fan3 : Fan Name
   fan4 : Fan Name
   fan5 : Fan Name
   fan6 : Fan Name
   json : Provide output in JSON
   psu1fan1 : Fan Name
   psu2fan1 : Fan Name
   <ENTER>
```
{{%/notice%}}

To view the status for a particular switch, use the optional `hostname`
parameter.

    cumulus@switch:~$ netq leaf01 show sensors fan fan1
    Hostname          Name            Description                         State      Speed      Max      Min      Message                             Last Changed
    ----------------- --------------- ----------------------------------- ---------- ---------- -------- -------- ----------------------------------- -------------------------
    leaf01            fan1            fan tray 1, fan 1                   ok         2500       29000    2500                                         Sun Apr 21 20:07:12 2019

## View PSU Health for All Switches

Fan, power supply unit, and temperature sensors are available to provide
additional data about the NetQ Platform operation. To view the health of
PSUs in your switches, use the `netq show sensors psu` command. If you
name the PSUs in all of your switches consistently, you can view more
information at once.

In this example, we look at the state of all PSUs with the name *psu2*.

    cumulus@switch:~$ netq show sensors psu psu2
    Matching sensors records:
    Hostname          Name            State      Message                             Last Changed
    ----------------- --------------- ---------- ----------------------------------- -------------------------
    exit01            psu2            ok                                             Fri Apr 19 16:01:17 2019
    exit02            psu2            ok                                             Fri Apr 19 16:01:33 2019
    leaf01            psu2            ok                                             Sun Apr 21 20:07:12 2019
    leaf02            psu2            ok                                             Fri Apr 19 16:01:41 2019
    leaf03            psu2            ok                                             Fri Apr 19 16:01:44 2019
    leaf04            psu2            ok                                             Fri Apr 19 16:01:36 2019
    spine01           psu2            ok                                             Fri Apr 19 16:01:52 2019
    spine02           psu2            ok                                             Fri Apr 19 16:01:08 2019

{{%notice tip%}}

Use Tab completion to determine the names of the PSUs in your switches.
Use the optional `hostname` parameter to view the PSU state for a given
switch.

{{%/notice%}}

## View the Temperature in All Switches

Fan, power supply unit, and temperature sensors are available to provide
additional data about the NetQ Platform operation. To view the
temperature sensor status, current temperature, and configured threshold
values, use the `netq show sensors temp` command. If you name the
temperature sensors in all of your switches consistently, you can view
more information at once.

In this example, we look at the state of all temperature sensors with
the name *psu1temp1*.

    cumulus@switch:~$ netq show sensors temp psu2temp1 
    Matching sensors records:
    Hostname          Name            Description                         State      Temp     Critical Max      Min      Message                             Last Changed
     
    ----------------- --------------- ----------------------------------- ---------- -------- -------- -------- -------- ----------------------------------- -------------------------
     
    exit01            psu2temp1       psu2 temp sensor                    ok         25       85       80       5                                            Fri Apr 19 16:01:17 2019

    exit02            psu2temp1       psu2 temp sensor                    ok         25       85       80       5                                            Fri Apr 19 16:01:33 2019
     
    leaf01            psu2temp1       psu2 temp sensor                    ok         25       85       80       5                                            Sun Apr 21 20:07:12 2019
     
    leaf02            psu2temp1       psu2 temp sensor                    ok         25       85       80       5                                            Fri Apr 19 16:01:41 2019
     
    leaf03            psu2temp1       psu2 temp sensor                    ok         25       85       80       5                                            Fri Apr 19 16:01:44 2019
     
    leaf04            psu2temp1       psu2 temp sensor                    ok         25       85       80       5                                            Fri Apr 19 16:01:36 2019
     
    spine01           psu2temp1       psu2 temp sensor                    ok         25       85       80       5                                            Fri Apr 19 16:01:52 2019
     
    spine02           psu2temp1       psu2 temp sensor                    ok         25       85       80       5                                            Fri Apr 19 16:01:08 2019

{{%notice tip%}}

Use Tab completion to determine the names of the temperature sensors in
your switches. Use the optional `hostname` parameter to view the
temperature state, current temperature, and threshold values for a given
switch.

{{%/notice%}}

## View All Sensor Data

To view all fan data, all PSU data, or
all temperature data from the sensors, you must view all of the sensor
data. The more consistently you name your sensors, the easier it will be
to view the full sensor data.

    cumulus@switch:~$ netq show sensors all
    Matching sensors records:
    Hostname          Name            Description                         State      Message                             Last Changed
    ----------------- --------------- ----------------------------------- ---------- ----------------------------------- -------------------------
    border01          fan3            fan tray 2, fan 1                   ok                                             Wed Apr 22 17:07:56 2020
    border01          fan1            fan tray 1, fan 1                   ok                                             Wed Apr 22 17:07:56 2020
    border01          fan6            fan tray 3, fan 2                   ok                                             Wed Apr 22 17:07:56 2020
    border01          fan5            fan tray 3, fan 1                   ok                                             Wed Apr 22 17:07:56 2020
    border01          psu2fan1        psu2 fan                            ok                                             Wed Apr 22 17:07:56 2020
    border01          fan2            fan tray 1, fan 2                   ok                                             Wed Apr 22 17:07:56 2020
    border01          fan4            fan tray 2, fan 2                   ok                                             Wed Apr 22 17:07:56 2020
    border01          psu1fan1        psu1 fan                            ok                                             Wed Apr 22 17:07:56 2020
    border02          fan1            fan tray 1, fan 1                   ok                                             Wed Apr 22 17:07:54 2020
    border02          fan2            fan tray 1, fan 2                   ok                                             Wed Apr 22 17:07:54 2020
    border02          psu1fan1        psu1 fan                            ok                                             Wed Apr 22 17:07:54 2020
    border02          fan5            fan tray 3, fan 1                   ok                                             Wed Apr 22 17:07:54 2020
    border02          fan3            fan tray 2, fan 1                   ok                                             Wed Apr 22 17:07:54 2020
    border02          fan6            fan tray 3, fan 2                   ok                                             Wed Apr 22 17:07:54 2020
    border02          fan4            fan tray 2, fan 2                   ok                                             Wed Apr 22 17:07:54 2020
    border02          psu2fan1        psu2 fan                            ok                                             Wed Apr 22 17:07:54 2020
    fw1               psu2fan1        psu2 fan                            ok                                             Wed Apr 22 17:08:45 2020
    fw1               fan3            fan tray 2, fan 1                   ok                                             Wed Apr 22 17:08:45 2020
    fw1               psu1fan1        psu1 fan                            ok                                             Wed Apr 22 17:08:45 2020
    fw1               fan1            fan tray 1, fan 1                   ok                                             Wed Apr 22 17:08:45 2020
    fw1               fan6            fan tray 3, fan 2                   ok                                             Wed Apr 22 17:08:45 2020
    fw1               fan5            fan tray 3, fan 1                   ok                                             Wed Apr 22 17:08:45 2020
    fw1               fan4            fan tray 2, fan 2                   ok                                             Wed Apr 22 17:08:45 2020
    fw1               fan2            fan tray 1, fan 2                   ok                                             Wed Apr 22 17:08:45 2020
    fw2               fan3            fan tray 2, fan 1                   ok                                             Wed Apr 22 17:07:53 2020
    ...
{{< /tab >}}

{{< /tabs >}}

## View Switch Software Inventory

### View OS Information for a Switch

You can view the name and version of the OS on a switch, and when it was
last modified. This example shows the OS information for all devices.

    cumulus@switch:~$ netq show inventory os
    Matching inventory records:
    Hostname          Name            Version                              Last Changed
    ----------------- --------------- ------------------------------------ -------------------------
    edge01            Ubuntu          16.04                                Fri Apr 19 16:01:18 2019
    exit01            CL              3.7.5                                Fri Apr 19 16:01:13 2019
    exit02            CL              3.7.5                                Fri Apr 19 16:01:38 2019
    leaf01            CL              3.7.5                                Sun Apr 21 20:07:09 2019
    leaf02            CL              3.7.5                                Fri Apr 19 16:01:46 2019
    leaf03            CL              3.7.5                                Fri Apr 19 16:01:41 2019
    leaf04            CL              3.7.5                                Fri Apr 19 16:01:32 2019
    server01          Ubuntu          16.04                                Fri Apr 19 16:01:55 2019
    server02          Ubuntu          16.04                                Fri Apr 19 16:01:55 2019
    server03          Ubuntu          16.04                                Fri Apr 19 16:01:55 2019
    server04          Ubuntu          16.04                                Fri Apr 19 16:01:55 2019
    spine01           CL              3.7.5                                Fri Apr 19 16:01:49 2019
    spine02           CL              3.7.5                                Fri Apr 19 16:01:05 2019

You can filter the results of the command to view only devices with a
particular operating system or version. This can be especially helpful
when you suspect that a particular device has not been upgraded as
expected. This example shows all devices with the Cumulus Linux version
3.7.5 installed.

    cumulus@switch:~$ netq show inventory os version 3.7.5
    Matching inventory records:
    Hostname          Name            Version                              Last Changed
    ----------------- --------------- ------------------------------------ -------------------------
    exit01            CL              3.7.5                                Fri Apr 19 16:01:13 2019
    exit02            CL              3.7.5                                Fri Apr 19 16:01:38 2019
    leaf01            CL              3.7.5                                Sun Apr 21 20:07:09 2019
    leaf02            CL              3.7.5                                Fri Apr 19 16:01:46 2019
    leaf03            CL              3.7.5                                Fri Apr 19 16:01:41 2019
    leaf04            CL              3.7.5                                Fri Apr 19 16:01:32 2019
    spine01           CL              3.7.5                                Fri Apr 19 16:01:49 2019
    spine02           CL              3.7.5                                Fri Apr 19 16:01:05 2019

This example shows changes that have been made to the OS on all devices
between 16 and 21 days ago. Remember to use measurement units on the
time values.

    cumulus@switch:~$ netq show events type os between 16d and 21d
    Matching inventory records:
    Hostname          Name            Version                              DB State   Last Changed
    ----------------- --------------- ------------------------------------ ---------- -------------------------
    mlx-2410a1-05     Cumulus Linux   3.7.3                                Add        Tue Feb 12 18:30:53 2019
    mlx-2700-11       Cumulus Linux   3.7.3                                Add        Tue Feb 12 18:30:45 2019
    mlx-2100-05       Cumulus Linux   3.7.3                                Add        Tue Feb 12 18:30:26 2019
    mlx-2100-05       Cumulus Linux   3.7.3~1533263174.bce9472             Add        Wed Feb 13 11:10:47 2019
    mlx-2700-11       Cumulus Linux   3.7.3~1533263174.bce9472             Add        Wed Feb 13 11:10:38 2019
    mlx-2100-05       Cumulus Linux   3.7.3~1533263174.bce9472             Add        Wed Feb 13 11:10:42 2019
    mlx-2700-11       Cumulus Linux   3.7.3~1533263174.bce9472             Add        Wed Feb 13 11:10:51 2019

### View License Information for a Switch

You can view the name and current state
of the license (whether it valid or not), and when it was last updated
for one or more devices. If a license is no longer valid on a switch, it
does not operate correctly. This example shows the license information
for all devices.

    cumulus@switch:~$ netq show inventory license
     
    Matching inventory records:
    Hostname          Name            State      Last Changed
    ----------------- --------------- ---------- -------------------------
    edge01            Cumulus Linux   N/A        Fri Apr 19 16:01:18 2019
    exit01            Cumulus Linux   ok         Fri Apr 19 16:01:13 2019
    exit02            Cumulus Linux   ok         Fri Apr 19 16:01:38 2019
    leaf01            Cumulus Linux   ok         Sun Apr 21 20:07:09 2019
    leaf02            Cumulus Linux   ok         Fri Apr 19 16:01:46 2019
    leaf03            Cumulus Linux   ok         Fri Apr 19 16:01:41 2019
    leaf04            Cumulus Linux   ok         Fri Apr 19 16:01:32 2019
    server01          Cumulus Linux   N/A        Fri Apr 19 16:01:55 2019
    server02          Cumulus Linux   N/A        Fri Apr 19 16:01:55 2019
    server03          Cumulus Linux   N/A        Fri Apr 19 16:01:55 2019
    server04          Cumulus Linux   N/A        Fri Apr 19 16:01:55 2019
    spine01           Cumulus Linux   ok         Fri Apr 19 16:01:49 2019
    spine02           Cumulus Linux   ok         Fri Apr 19 16:01:05 2019

You can view the historical state of licenses using the around keyword.
This example shows the license state for all devices about 7 days ago.
Remember to use measurement units on the time values.

    cumulus@switch:~$ netq show inventory license around 7d
     
    Matching inventory records:
    Hostname          Name            State      Last Changed
    ----------------- --------------- ---------- -------------------------
    edge01            Cumulus Linux   N/A        Tue Apr 2 14:01:18 2019
    exit01            Cumulus Linux   ok         Tue Apr 2 14:01:13 2019
    exit02            Cumulus Linux   ok         Tue Apr 2 14:01:38 2019
    leaf01            Cumulus Linux   ok         Tue Apr 2 20:07:09 2019
    leaf02            Cumulus Linux   ok         Tue Apr 2 14:01:46 2019
    leaf03            Cumulus Linux   ok         Tue Apr 2 14:01:41 2019
    leaf04            Cumulus Linux   ok         Tue Apr 2 14:01:32 2019
    server01          Cumulus Linux   N/A        Tue Apr 2 14:01:55 2019
    server02          Cumulus Linux   N/A        Tue Apr 2 14:01:55 2019
    server03          Cumulus Linux   N/A        Tue Apr 2 14:01:55 2019
    server04          Cumulus Linux   N/A        Tue Apr 2 14:01:55 2019
    spine01           Cumulus Linux   ok         Tue Apr 2 14:01:49 2019
    spine02           Cumulus Linux   ok         Tue Apr 2 14:01:05 2019

You can filter the results to show license changes during a particular
time frame for a particular device. This example shows that there have
been no changes to the license state on spine01 between now and 24 hours
ago.

    cumulus@switch:~$ netq spine01 show events type license between now and 24h
    No matching events records found

### View Summary of Operating System on a Switch

As with the hardware information, you can view a summary of the software
information using the `brief` keyword. Specify a hostname to view the
summary for a specific device.

    cumulus@switch:~$ netq show inventory brief
     
    Matching inventory records:
    Hostname          Switch               OS              CPU      ASIC            Ports
    ----------------- -------------------- --------------- -------- --------------- -----------------------------------
    edge01            N/A                  Ubuntu          x86_64   N/A             N/A
    exit01            VX                   CL              x86_64   VX              N/A
    exit02            VX                   CL              x86_64   VX              N/A
    leaf01            VX                   CL              x86_64   VX              N/A
    leaf02            VX                   CL              x86_64   VX              N/A
    leaf03            VX                   CL              x86_64   VX              N/A
    leaf04            VX                   CL              x86_64   VX              N/A
    server01          N/A                  Ubuntu          x86_64   N/A             N/A
    server02          N/A                  Ubuntu          x86_64   N/A             N/A
    server03          N/A                  Ubuntu          x86_64   N/A             N/A
    server04          N/A                  Ubuntu          x86_64   N/A             N/A
    spine01           VX                   CL              x86_64   VX              N/A
    spine02           VX                   CL              x86_64   VX              N/A

### View the Cumulus Linux Package on a Switch

When you are troubleshooting an issue with a switch, you might want to know what versions of the Cumulus Linux operating system are supported on that switch and on a switch that is not having the same issue.

This example shows the Cumulus Linux OS versions supported for the *leaf01* switch, using the *vx* ASIC vendor (virtual, so simulated) and *x86_64* CPU architecture.

```
cumulus@switch:~$ netq leaf01 show cl-manifest

Matching manifest records:
Hostname          ASIC Vendor          CPU Arch             Manifest Version
----------------- -------------------- -------------------- --------------------
leaf01            vx                   x86_64               3.7.6.1
leaf01            vx                   x86_64               3.7.10
leaf01            vx                   x86_64               3.6.2.1
leaf01            vx                   x86_64               3.7.4
leaf01            vx                   x86_64               3.7.2.5
leaf01            vx                   x86_64               3.7.1
leaf01            vx                   x86_64               3.6.0
leaf01            vx                   x86_64               3.7.0
leaf01            vx                   x86_64               3.4.1
leaf01            vx                   x86_64               3.7.3
leaf01            vx                   x86_64               3.2.0
...
```

This example shows the installed Cumulus Linux OS version for all monitored switches.

```
cumulus@oob-mgmt-server:~$ netq show cl-manifest

Matching manifest records:
Hostname          ASIC Vendor          CPU Arch             Manifest Version
----------------- -------------------- -------------------- --------------------
exit01            vx                   x86_64               3.7.6.1
exit01            vx                   x86_64               3.7.10
exit01            vx                   x86_64               3.6.2.1
exit01            vx                   x86_64               3.7.4
...
exit02            vx                   x86_64               3.7.6.1
exit02            vx                   x86_64               3.7.10
exit02            vx                   x86_64               3.6.2.1
exit02            vx                   x86_64               3.7.4
...
leaf01            vx                   x86_64               3.7.6.1
leaf01            vx                   x86_64               3.7.10
leaf01            vx                   x86_64               3.6.2.1
leaf01            vx                   x86_64               3.7.4
...
```

### View All Software Packages Installed on Switches

If you are having an issue with a particular switch, you may want to verify what software is installed and whether it needs updating. Use the `netq show cl-pkg-info` command to view the current package information.

This example shows all installed software packages for *spine01*.

```
cumulus@switch:~$ netq spine01 show cl-pkg-info 

Matching package_info records:
Hostname          Package Name             Version              CL Version           Package Status       Last Changed
----------------- ------------------------ -------------------- -------------------- -------------------- -------------------------
spine01           adduser                  3.113+nmu3           Cumulus Linux 3.7.8  installed            Wed Oct 30 18:21:05 2019
spine01           apt                      1.0.9.8.2-cl3u3      Cumulus Linux 3.7.8  installed            Wed Oct 30 18:21:05 2019
spine01           arping                   2.14-1               Cumulus Linux 3.7.8  installed            Wed Oct 30 18:21:05 2019
spine01           base-files               8+deb8u11            Cumulus Linux 3.7.8  installed            Wed Oct 30 18:21:05 2019
spine01           busybox                  1:1.22.0-9+deb8u4    Cumulus Linux 3.7.8  installed            Wed Oct 30 18:21:05 2019
spine01           clag                     1.3.0-cl3u23         Cumulus Linux 3.7.8  installed            Wed Oct 30 18:21:05 2019
spine01           cumulus-chassis          0.1-cl3u4            Cumulus Linux 3.7.8  installed            Wed Oct 30 18:21:05 2019
spine01           cumulus-platform         3.0-cl3u28           Cumulus Linux 3.7.8  installed            Wed Oct 30 18:21:05 2019
spine01           dh-python                1.20141111-2         Cumulus Linux 3.7.8  installed            Wed Oct 30 18:21:05 2019
spine01           dialog                   1.2-20140911-1       Cumulus Linux 3.7.8  installed            Wed Oct 30 18:21:05 2019
spine01           discover                 2.1.2-7              Cumulus Linux 3.7.8  installed            Wed Oct 30 18:21:05 2019
spine01           discover-data            2.2013.01.11         Cumulus Linux 3.7.8  installed            Wed Oct 30 18:21:05 2019
spine01           dmidecode                2.12-3               Cumulus Linux 3.7.8  installed            Wed Oct 30 18:21:05 2019
spine01           dnsutils                 1:9.9.5.dfsg-9+deb8u Cumulus Linux 3.7.8  installed            Wed Oct 30 18:21:05 2019
                                           18
spine01           e2fslibs                 1.42.12-2+b1         Cumulus Linux 3.7.8  installed            Wed Oct 30 18:21:05 2019
spine01           e2fsprogs                1.42.12-2+b1         Cumulus Linux 3.7.8  installed            Wed Oct 30 18:21:05 2019
spine01           eject                    2.1.5+deb1+cvs200811 Cumulus Linux 3.7.8  installed            Wed Oct 30 18:21:05 2019
                                           04-13.1+deb8u1
spine01           ethtool                  1:4.6-1-cl3u7        Cumulus Linux 3.7.8  installed            Wed Oct 30 18:21:05 2019
spine01           gcc-4.9-base             4.9.2-10+deb8u2      Cumulus Linux 3.7.8  installed            Wed Oct 30 18:21:05 2019
spine01           gnupg                    1.4.18-7+deb8u5      Cumulus Linux 3.7.8  installed            Wed Oct 30 18:21:05 2019
...
```

Remove the `hostname` option to view the information for all switches. Use the `text-package-name` option to narrow the results to a particular package or the `around` option to narrow the output to a particular time range.

### View Recommended Software Packages

You can determine whether any of your switches are using a software package other than the default package associated with the Cumulus Linux release that is running on the switches. Additionally, you can determine if a software package is missing. Use the `netq show recommended-pkg-version` command to display a list of recommended packages to install/upgrade on one or all devices.

This example shows that the *leaf12* switch which is running Cumulus Linux *3.7.1* needs to update the *switchd* software.

```
cumulus@noc-pr:~$ netq show recommended-pkg-version release-id 3.7.1 package-name switchd
Matching manifest records:
Hostname          Release ID           ASIC Vendor          CPU Arch             Package Name         Version              Last Changed
----------------- -------------------- -------------------- -------------------- -------------------- -------------------- -------------------------
noc-pr            3.7.1                vx                   x86_64               switchd              1.0-cl3u30           Wed Feb  5 04:36:30 2020
cumulus@noc-pr:~$
cumulus@noc-pr:~$
cumulus@noc-pr:~$ netq show recommended-pkg-version release-id 3.7.1 package-name ptmd
Matching manifest records:
Hostname          Release ID           ASIC Vendor          CPU Arch             Package Name         Version              Last Changed
----------------- -------------------- -------------------- -------------------- -------------------- -------------------- -------------------------
noc-pr            3.7.1                vx                   x86_64               ptmd                 3.0-2-cl3u8          Wed Feb  5 04:36:30 2020
cumulus@noc-pr:~$ netq show recommended-pkg-version release-id 3.7.1 package-name lldpd
Matching manifest records:
Hostname          Release ID           ASIC Vendor          CPU Arch             Package Name         Version              Last Changed
----------------- -------------------- -------------------- -------------------- -------------------- -------------------- -------------------------
noc-pr            3.7.1                vx                   x86_64               lldpd                0.9.8-0-cl3u11       Wed Feb  5 04:36:30 2020
cumulus@noc-pr:~$ netq show recommended-pkg-version release-id 3.6.2 package-name switchd
Matching manifest records:
Hostname          Release ID           ASIC Vendor          CPU Arch             Package Name         Version              Last Changed
----------------- -------------------- -------------------- -------------------- -------------------- -------------------- -------------------------
noc-pr            3.6.2                vx                   x86_64               switchd              1.0-cl3u27           Wed Feb  5 04:36:30 2020
cumulus@noc-pr:~$
2:57
from the hardware switch (real)
2:57
cumulus@noc-pr:~$ netq show recommended-pkg-version release-id 3.7.1 package-name switchd
Matching manifest records:
Hostname          Release ID           ASIC Vendor          CPU Arch             Package Name         Version              Last Changed
----------------- -------------------- -------------------- -------------------- -------------------- -------------------- -------------------------
noc-pr            3.7.1                vx                   x86_64               switchd              1.0-cl3u30           Wed Feb  5 04:36:30 2020
cumulus@noc-pr:~$
cumulus@noc-pr:~$
cumulus@noc-pr:~$ netq show recommended-pkg-version release-id 3.7.1 package-name ptmd
Matching manifest records:
Hostname          Release ID           ASIC Vendor          CPU Arch             Package Name         Version              Last Changed
----------------- -------------------- -------------------- -------------------- -------------------- -------------------- -------------------------
noc-pr            3.7.1                vx                   x86_64               ptmd                 3.0-2-cl3u8          Wed Feb  5 04:36:30 2020
cumulus@noc-pr:~$ netq show recommended-pkg-version release-id 3.7.1 package-name lldpd
Matching manifest records:
Hostname          Release ID           ASIC Vendor          CPU Arch             Package Name         Version              Last Changed
----------------- -------------------- -------------------- -------------------- -------------------- -------------------- -------------------------
noc-pr            3.7.1                vx                   x86_64               lldpd                0.9.8-0-cl3u11       Wed Feb  5 04:36:30 2020
cumulus@noc-pr:~$ netq show recommended-pkg-version release-id 3.6.2 package-name switchd
Matching manifest records:
Hostname          Release ID           ASIC Vendor          CPU Arch             Package Name         Version              Last Changed
----------------- -------------------- -------------------- -------------------- -------------------- -------------------- -------------------------
noc-pr            3.6.2                vx                   x86_64               switchd              1.0-cl3u27           Wed Feb  5 04:36:30 2020
cumulus@noc-pr:~$
2:58
from the switch
2:58
cumulus@noc-pr:~$ netq act-5712-09 show recommended-pkg-version release-id 3.6.2 package-name switchd
Matching manifest records:
Hostname          Release ID           ASIC Vendor          CPU Arch             Package Name         Version              Last Changed
----------------- -------------------- -------------------- -------------------- -------------------- -------------------- -------------------------
act-5712-09       3.6.2                bcm                  x86_64               switchd              1.0-cl3u27           Wed Feb  5 04:36:30 2020
cumulus@noc-pr:~$ netq act-5712-09 show recommended-pkg-version release-id 3.7.2 package-name switchd
Matching manifest records:
Hostname          Release ID           ASIC Vendor          CPU Arch             Package Name         Version              Last Changed
----------------- -------------------- -------------------- -------------------- -------------------- -------------------- -------------------------
act-5712-09       3.7.2                bcm                  x86_64               switchd              1.0-cl3u31           Wed Feb  5 04:36:30 2020
cumulus@noc-pr:~$
cumulus@noc-pr:~$
3:02
very old one too
3:02
cumulus@noc-pr:~$ netq act-5712-09 show recommended-pkg-version release-id 3.6.2 package-name switchd
Matching manifest records:
Hostname          Release ID           ASIC Vendor          CPU Arch             Package Name         Version              Last Changed
----------------- -------------------- -------------------- -------------------- -------------------- -------------------- -------------------------
act-5712-09       3.6.2                bcm                  x86_64               switchd              1.0-cl3u27           Wed Feb  5 04:36:30 2020
cumulus@noc-pr:~$ netq act-5712-09 show recommended-pkg-version release-id 3.7.2 package-name switchd
Matching manifest records:
Hostname          Release ID           ASIC Vendor          CPU Arch             Package Name         Version              Last Changed
----------------- -------------------- -------------------- -------------------- -------------------- -------------------- -------------------------
act-5712-09       3.7.2                bcm                  x86_64               switchd              1.0-cl3u31           Wed Feb  5 04:36:30 2020
cumulus@noc-pr:~$
cumulus@noc-pr:~$
3:02
cumulus@noc-pr:~$ netq act-5712-09 show recommended-pkg-version release-id 3.1.0 package-name switchd
Matching manifest records:
Hostname          Release ID           ASIC Vendor          CPU Arch             Package Name         Version              Last Changed
----------------- -------------------- -------------------- -------------------- -------------------- -------------------- -------------------------
act-5712-09       3.1.0                bcm                  x86_64               switchd              1.0-cl3u4            Wed Feb  5 04:36:30 2020
cumulus@noc-pr:~$
```

### View ACL Resources

You can monitor the incoming and outgoing access control lists (ACLs) configured on one or all devices, currently or at a time in the past. Use the `netq show cl-resource acl` command to view this information. Use the `egress` or `ingress` options to show only the outgoing or incoming ACLs. Use the `around` option to show this information for a time in the past.

This example shows the ACL resources by the *leaf01* switch.

```
cumulus@switch:~$ netq leaf01 show cl-resource acl
Matching cl_resource records:
Hostname          In IPv4 filter       In IPv4 Mangle       In IPv6 filter       In IPv6 Mangle       In 8021x filter      In Mirror            In PBR IPv4 filter   In PBR IPv6 filter   Eg IPv4 filter       Eg IPv4 Mangle       Eg IPv6 filter       Eg IPv6 Mangle       ACL Regions          18B Rules Key        32B Rules Key        54B Rules Key        L4 Port range Checke Last Updated
                                                                                                                                                                                                                                                                                                                                                                  rs
----------------- -------------------- -------------------- -------------------- -------------------- -------------------- -------------------- -------------------- -------------------- -------------------- -------------------- -------------------- -------------------- -------------------- -------------------- -------------------- -------------------- -------------------- ------------------------
leaf01            36,512(7%)           0,0(0%)              30,768(3%)           0,0(0%)              0,0(0%)              0,0(0%)              0,0(0%)              0,0(0%)              29,256(11%)          0,0(0%)              0,0(0%)              0,0(0%)              0,0(0%)              0,0(0%)              0,0(0%)              0,0(0%)              2,24(8%)             Mon Jan 13 03:34:11 2020
```

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

### View Forwarding Resources

You can monitor the amount of forwarding resources used by one or all devices, currently or at a time in the past. Use the `netq show cl-resource forwarding` command to view this information. Use the `around` option to show this information for a time in the past.

This example shows the forwarding resources used by the *spine02* switch.

```
cumulus@switch:~$ netq spine02 show cl-resource forwarding
Matching cl_resource records:
Hostname          IPv4 host entries    IPv6 host entries    IPv4 route entries   IPv6 route entries   ECMP nexthops        MAC entries          Total Mcast Routes   Last Updated
----------------- -------------------- -------------------- -------------------- -------------------- -------------------- -------------------- -------------------- ------------------------
spine02           9,16384(0%)          0,0(0%)              290,131072(0%)       173,20480(0%)        54,16330(0%)         26,32768(0%)         0,8192(0%)           Mon Jan 13 03:34:11 2020
```

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

### Validate NetQ Agents are Running

You can confirm that NetQ Agents are running on switches and hosts (if
installed) using the `netq show agents` command. Viewing the **Status**
column of the output indicates whether the agent is up and current,
labelled *Fresh*, or down and stale, labelled *Rotten*. Additional
information is provided about the agent status, including whether it is
time synchronized, how long it has been up, and the last time its state
changed.

This example shows NetQ Agent state on all devices.

    cumulus@switch:~$ netq show agents
    Matching agents records:
    Hostname          Status           NTP Sync Version                              Sys Uptime                Agent Uptime              Reinitialize Time          Last Changed
    ----------------- ---------------- -------- ------------------------------------ ------------------------- ------------------------- -------------------------- -------------------------
    edge01            Fresh            yes      2.1.0-ub16.04u15~1555612152.6e34b56  2d:7h:2m:12s              2d:7h:2m:5s               2d:7h:2m:5s                Sun Apr 21 16:00:50 2019
    exit01            Fresh            yes      2.1.0-cl3u15~1555612272.6e34b56      2d:7h:1m:30s              2d:7h:1m:22s              2d:7h:1m:22s               Sun Apr 21 16:00:52 2019
    exit02            Fresh            yes      2.1.0-cl3u15~1555612272.6e34b56      2d:7h:1m:36s              2d:7h:1m:27s              2d:7h:1m:27s               Sun Apr 21 16:01:19 2019
    leaf01            Fresh            yes      2.1.0-cl3u15~1555612272.6e34b56      2d:7h:1m:28s              2h:54m:12s                2h:54m:12s                 Sun Apr 21 20:05:45 2019
    leaf02            Fresh            yes      2.1.0-cl3u15~1555612272.6e34b56      2d:7h:1m:38s              2d:7h:1m:29s              2d:7h:1m:29s               Sun Apr 21 16:01:43 2019
    leaf03            Fresh            yes      2.1.0-cl3u15~1555612272.6e34b56      2d:7h:1m:37s              2d:7h:1m:28s              2d:7h:1m:28s               Sun Apr 21 16:01:23 2019
    leaf04            Fresh            yes      2.1.0-cl3u15~1555612272.6e34b56      2d:7h:1m:39s              2d:7h:1m:31s              2d:7h:1m:31s               Sun Apr 21 16:01:27 2019
    server01          Fresh            yes      2.1.0-ub16.04u15~1555612152.6e34b56  2d:6h:59m:35s             2d:6h:59m:27s             2d:6h:59m:27s              Sun Apr 21 16:00:43 2019
    server02          Fresh            yes      2.1.0-ub16.04u15~1555612152.6e34b56  2d:6h:59m:34s             2d:6h:59m:26s             2d:6h:59m:26s              Sun Apr 21 16:00:46 2019
    server03          Fresh            yes      2.1.0-ub16.04u15~1555612152.6e34b56  2d:6h:59m:34s             2d:6h:59m:26s             2d:6h:59m:26s              Sun Apr 21 16:00:52 2019
    server04          Fresh            yes      2.1.0-ub16.04u15~1555612152.6e34b56  2d:6h:59m:34s             2d:6h:59m:26s             2d:6h:59m:26s              Sun Apr 21 16:00:43 2019
    spine01           Fresh            yes      2.1.0-cl3u15~1555612272.6e34b56      2d:7h:1m:40s              2d:7h:1m:32s              2d:7h:1m:32s               Sun Apr 21 16:01:33 2019
    spine02           Fresh            yes      2.1.0-cl3u15~1555612272.6e34b56      2d:7h:1m:34s              2d:7h:1m:26s              2d:7h:1m:26s               Sun Apr 21 16:01:12 2019

You can narrow your focus in several ways:

  - View the state of the NetQ Agent on a given device using the
    *hostname* keyword.
  - View only the NetQ Agents that are fresh or rotten using the *fresh* or *rotten* keyword.
  - View the state of NetQ Agents at an earlier time using the *around*
    keyword.

## Monitor Software Services

Cumulus Linux and NetQ run a number of services to deliver the various
features of these products. You can monitor their status using the `netq
show services` command. The services related to system-level operation
are described here. Monitoring of other services, such as those related
to routing, are described with those topics. NetQ automatically monitors
the following services:

  - **bgpd**: BGP (Border Gateway Protocol) daemon
  - **clagd**: MLAG (Multi-chassis Link Aggregation) daemon
  - **helpledmgrd**: Switch LED manager daemon
  - **lldpd**: LLDP (Link Layer Discovery Protocol) daemon
  - **mstpd**: MSTP (Multiple Spanning Tree Protocol) daemon
  - **neighmgrd**: Neighbor Manager daemon for BGP and OSPF
  - **netq-agent**: NetQ Agent service
  - **netqd**: NetQ application daemon
  - **ntp**: NTP service
  - **ntpd**: NTP daemon
  - **ptmd**: PTM (Prescriptive Topology Manager) daemon
  - **pwmd**: PWM (Password Manager)
    daemon
  - **rsyslog**: Rocket-fast system event logging processing service
  - **smond**: System monitor daemon
  - **ssh**: Secure Shell service for switches and servers
  - **status**: License validation service
  - **syslog**: System event logging service
  - **vrf**: VRF (Virtual Route Forwarding) service
  - **zebra**: GNU Zebra routing daemon

The CLI syntax for viewing the status of services is:

    netq [<hostname>] show services [<service-name>] [vrf <vrf>] [active|monitored] [around <text-time>] [json]
    netq [<hostname>] show services [<service-name>] [vrf <vrf>] status (ok|warning|error|fail) [around <text-time>] [json]
    netq [<hostname>] show events [level info | level error | level warning | level critical | level debug] type services [between <text-time> and <text-endtime>] [json]

### View All Services on All Devices

This example shows all of the available services on each device and
whether each is enabled, active, and monitored, along with how long the
service has been running and the last time it was changed.

{{%notice tip%}}

It is useful to have colored output for this show command. To configure
colored output, run the `netq config add color` command.

{{%/notice%}}

    cumulus@switch:~$ netq show services
    Hostname          Service              PID   VRF             Enabled Active Monitored Status           Uptime                    Last Changed
    ----------------- -------------------- ----- --------------- ------- ------ --------- ---------------- ------------------------- -------------------------
    leaf01            bgpd                 2872  default         yes     yes    yes       ok               1d:6h:43m:59s             Fri Feb 15 17:28:24 2019
    leaf01            clagd                n/a   default         yes     no     yes       n/a              1d:6h:43m:35s             Fri Feb 15 17:28:48 2019
    leaf01            ledmgrd              1850  default         yes     yes    no        ok               1d:6h:43m:59s             Fri Feb 15 17:28:24 2019
    leaf01            lldpd                2651  default         yes     yes    yes       ok               1d:6h:43m:27s             Fri Feb 15 17:28:56 2019
    leaf01            mstpd                1746  default         yes     yes    yes       ok               1d:6h:43m:35s             Fri Feb 15 17:28:48 2019
    leaf01            neighmgrd            1986  default         yes     yes    no        ok               1d:6h:43m:59s             Fri Feb 15 17:28:24 2019
    leaf01            netq-agent           8654  mgmt            yes     yes    yes       ok               1d:6h:43m:29s             Fri Feb 15 17:28:54 2019
    leaf01            netqd                8848  mgmt            yes     yes    yes       ok               1d:6h:43m:29s             Fri Feb 15 17:28:54 2019
    leaf01            ntp                  8478  mgmt            yes     yes    yes       ok               1d:6h:43m:29s             Fri Feb 15 17:28:54 2019
    leaf01            ptmd                 2743  default         yes     yes    no        ok               1d:6h:43m:59s             Fri Feb 15 17:28:24 2019
    leaf01            pwmd                 1852  default         yes     yes    no        ok               1d:6h:43m:59s             Fri Feb 15 17:28:24 2019
    leaf01            smond                1826  default         yes     yes    yes       ok               1d:6h:43m:27s             Fri Feb 15 17:28:56 2019
    leaf01            ssh                  2106  default         yes     yes    no        ok               1d:6h:43m:59s             Fri Feb 15 17:28:24 2019
    leaf01            syslog               8254  default         yes     yes    no        ok               1d:6h:43m:59s             Fri Feb 15 17:28:24 2019
    leaf01            zebra                2856  default         yes     yes    yes       ok               1d:6h:43m:59s             Fri Feb 15 17:28:24 2019
    leaf02            bgpd                 2867  default         yes     yes    yes       ok               1d:6h:43m:55s             Fri Feb 15 17:28:28 2019
    leaf02            clagd                n/a   default         yes     no     yes       n/a              1d:6h:43m:31s             Fri Feb 15 17:28:53 2019
    leaf02            ledmgrd              1856  default         yes     yes    no        ok               1d:6h:43m:55s             Fri Feb 15 17:28:28 2019
    leaf02            lldpd                2646  default         yes     yes    yes       ok               1d:6h:43m:30s             Fri Feb 15 17:28:53 2019
    ...

You can also view services information in JSON format:

    cumulus@switch:~$ netq show services json
    {
        "services":[
            {
                "status":"ok",
                "uptime":1550251734.0,
                "monitored":"yes",
                "service":"ntp",
                "lastChanged":1550251734.4790000916,
                "pid":"8478",
                "hostname":"leaf01",
                "enabled":"yes",
                "vrf":"mgmt",
                "active":"yes"
            },
            {
                "status":"ok",
                "uptime":1550251704.0,
                "monitored":"no",
                "service":"ssh",
                "lastChanged":1550251704.0929999352,
                "pid":"2106",
                "hostname":"leaf01",
                "enabled":"yes",
                "vrf":"default",
                "active":"yes"
            },
            {
                "status":"ok",
                "uptime":1550251736.0,
                "monitored":"yes",
                "service":"lldpd",
                "lastChanged":1550251736.5160000324,
                "pid":"2651",
                "hostname":"leaf01",
                "enabled":"yes",
                "vrf":"default",
                "active":"yes"
            },
            {
                "status":"ok",
                "uptime":1550251704.0,
                "monitored":"yes",
                "service":"bgpd",
                "lastChanged":1550251704.1040000916,
                "pid":"2872",
                "hostname":"leaf01",
                "enabled":"yes",
                "vrf":"default",
                "active":"yes"
            },
            {
                "status":"ok",
                "uptime":1550251704.0,
                "monitored":"no",
                "service":"neighmgrd",
                "lastChanged":1550251704.0969998837,
                "pid":"1986",
                "hostname":"leaf01",
                "enabled":"yes",
                "vrf":"default",
                "active":"yes"
            },
    ...

If you want to view the service information for a given device, simply
use the `hostname` option when running the command.

### View Information about a Given Service on All Devices

You can view the status of a given service at the current time, at a
prior point in time, or view the changes that have occurred for the
service during a specified timeframe.

This example shows how to view the status of the NTP service across the
network. In this case, VRF is configured so the NTP service runs on both
the default and management interface. You can perform the same command
with the other services, such as `bgpd`, `lldpd`, and `clagd`.

    cumulus@switch:~$ netq show services ntp
    Matching services records:
    Hostname          Service              PID   VRF             Enabled Active Monitored Status           Uptime                    Last Changed
    ----------------- -------------------- ----- --------------- ------- ------ --------- ---------------- ------------------------- -------------------------
    exit01            ntp                  8478  mgmt            yes     yes    yes       ok               1d:6h:52m:41s             Fri Feb 15 17:28:54 2019
    exit02            ntp                  8497  mgmt            yes     yes    yes       ok               1d:6h:52m:36s             Fri Feb 15 17:28:59 2019
    firewall01        ntp                  n/a   default         yes     yes    yes       ok               1d:6h:53m:4s              Fri Feb 15 17:28:31 2019
    hostd-11          ntp                  n/a   default         yes     yes    yes       ok               1d:6h:52m:46s             Fri Feb 15 17:28:49 2019
    hostd-21          ntp                  n/a   default         yes     yes    yes       ok               1d:6h:52m:37s             Fri Feb 15 17:28:58 2019
    hosts-11          ntp                  n/a   default         yes     yes    yes       ok               1d:6h:52m:28s             Fri Feb 15 17:29:07 2019
    hosts-13          ntp                  n/a   default         yes     yes    yes       ok               1d:6h:52m:19s             Fri Feb 15 17:29:16 2019
    hosts-21          ntp                  n/a   default         yes     yes    yes       ok               1d:6h:52m:14s             Fri Feb 15 17:29:21 2019
    hosts-23          ntp                  n/a   default         yes     yes    yes       ok               1d:6h:52m:4s              Fri Feb 15 17:29:31 2019
    noc-pr            ntp                  2148  default         yes     yes    yes       ok               1d:6h:53m:43s             Fri Feb 15 17:27:52 2019
    noc-se            ntp                  2148  default         yes     yes    yes       ok               1d:6h:53m:38s             Fri Feb 15 17:27:57 2019
    spine01           ntp                  8414  mgmt            yes     yes    yes       ok               1d:6h:53m:30s             Fri Feb 15 17:28:05 2019
    spine02           ntp                  8419  mgmt            yes     yes    yes       ok               1d:6h:53m:27s             Fri Feb 15 17:28:08 2019
    spine03           ntp                  8443  mgmt            yes     yes    yes       ok               1d:6h:53m:22s             Fri Feb 15 17:28:13 2019
    leaf01             ntp                  8765  mgmt            yes     yes    yes       ok               1d:6h:52m:52s             Fri Feb 15 17:28:43 2019
    leaf02             ntp                  8737  mgmt            yes     yes    yes       ok               1d:6h:52m:46s             Fri Feb 15 17:28:49 2019
    leaf11            ntp                  9305  mgmt            yes     yes    yes       ok               1d:6h:49m:22s             Fri Feb 15 17:32:13 2019
    leaf12            ntp                  9339  mgmt            yes     yes    yes       ok               1d:6h:49m:9s              Fri Feb 15 17:32:26 2019
    leaf21            ntp                  9367  mgmt            yes     yes    yes       ok               1d:6h:49m:5s              Fri Feb 15 17:32:30 2019
    leaf22            ntp                  9403  mgmt            yes     yes    yes       ok               1d:6h:52m:57s             Fri Feb 15 17:28:38 2019

This example shows the status of the BGP daemon.

    cumulus@switch:~$ netq show services bgpd
    Matching services records:
    Hostname          Service              PID   VRF             Enabled Active Monitored Status           Uptime                    Last Changed
    ----------------- -------------------- ----- --------------- ------- ------ --------- ---------------- ------------------------- -------------------------
    exit01            bgpd                 2872  default         yes     yes    yes       ok               1d:6h:54m:37s             Fri Feb 15 17:28:24 2019
    exit02            bgpd                 2867  default         yes     yes    yes       ok               1d:6h:54m:33s             Fri Feb 15 17:28:28 2019
    firewall01        bgpd                 21766 default         yes     yes    yes       ok               1d:6h:54m:54s             Fri Feb 15 17:28:07 2019
    spine01           bgpd                 2953  default         yes     yes    yes       ok               1d:6h:55m:27s             Fri Feb 15 17:27:34 2019
    spine02           bgpd                 2948  default         yes     yes    yes       ok               1d:6h:55m:23s             Fri Feb 15 17:27:38 2019
    spine03           bgpd                 2953  default         yes     yes    yes       ok               1d:6h:55m:18s             Fri Feb 15 17:27:43 2019
    leaf01            bgpd                 3221  default         yes     yes    yes       ok               1d:6h:54m:48s             Fri Feb 15 17:28:13 2019
    leaf02            bgpd                 3177  default         yes     yes    yes       ok               1d:6h:54m:42s             Fri Feb 15 17:28:19 2019
    leaf11            bgpd                 3521  default         yes     yes    yes       ok               1d:6h:51m:18s             Fri Feb 15 17:31:43 2019
    leaf12            bgpd                 3527  default         yes     yes    yes       ok               1d:6h:51m:6s              Fri Feb 15 17:31:55 2019
    leaf21            bgpd                 3512  default         yes     yes    yes       ok               1d:6h:51m:1s              Fri Feb 15 17:32:00 2019
    leaf22            bgpd                 3536  default         yes     yes    yes       ok               1d:6h:54m:54s             Fri Feb 15 17:28:07 2019

### View Events Related to a Given Service

To view changes over a given time period, use the `netq show events`
command. For more detailed information about events, refer to {{<link url="Monitor-Events">}}.

In this example, we want to view changes to the bgpd service in the last
48 hours.

    cumulus@switch:/$ netq show events type bgp between now and 48h
    Matching events records:
    Hostname          Message Type Severity Message                             Timestamp
    ----------------- ------------ -------- ----------------------------------- -------------------------
    leaf01            bgp          info     BGP session with peer spine-1 swp3. 1d:6h:55m:37s
                                            3 vrf DataVrf1081 state changed fro
                                            m failed to Established
    leaf01            bgp          info     BGP session with peer spine-2 swp4. 1d:6h:55m:37s
                                            3 vrf DataVrf1081 state changed fro
                                            m failed to Established
    leaf01            bgp          info     BGP session with peer spine-3 swp5. 1d:6h:55m:37s
                                            3 vrf DataVrf1081 state changed fro
                                            m failed to Established
    leaf01            bgp          info     BGP session with peer spine-1 swp3. 1d:6h:55m:37s
                                            2 vrf DataVrf1080 state changed fro
                                            m failed to Established
    leaf01            bgp          info     BGP session with peer spine-3 swp5. 1d:6h:55m:37s
                                            2 vrf DataVrf1080 state changed fro
                                            m failed to Established
    leaf01            bgp          info     BGP session with peer spine-2 swp4. 1d:6h:55m:37s
                                            2 vrf DataVrf1080 state changed fro
                                            m failed to Established
    leaf01            bgp          info     BGP session with peer spine-3 swp5. 1d:6h:55m:37s
                                            4 vrf DataVrf1082 state changed fro
                                            m failed to Established
