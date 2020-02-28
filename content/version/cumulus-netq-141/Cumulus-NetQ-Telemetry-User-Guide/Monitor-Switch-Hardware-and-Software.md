---
title: Monitor Switch Hardware and Software
author: Cumulus Networks
weight: 57
aliases:
 - /display/NETQ141/Monitor+Switch+Hardware+and+Software
 - /pages/viewpage.action?pageId=10453523
pageID: 10453523
---
With NetQ, a network administrator can monitor both the switch hardware
and its operating system for misconfigurations or misbehaving services.
NetQ provides the ability to:

  - Validate configurations
  - Validate service operations
  - Identify inventory

It helps answer questions such as:

  - What switches do I have in the network?
  - Are all of my services running?
  - Are all switches licensed correctly?
  - Do all switches have NetQ agents running?

NetQ uses LLDP (Link
Layer Discovery Protocol) to collect port information. NetQ can also
identify peer ports connected to DACs ( Direct Attached Cables) and AOCs
(Active Optical Cables) without using LLDP, even if the link is not UP.

## Monitor Switch and Host Hardware Information

NetQ enables you to view either a summary or details about key
components on your switch or host, including the motherboard, ASIC,
microprocessor, disk and memory information. The `netq show inventory`
command is used to view the information for a single device or for all
of your devices at once, depending on what you want to see.

The syntax for this command is:

    netq [<hostname>] show inventory brief [json]
    netq [<hostname>] show inventory asic [vendor <asic-vendor>| model <asic-model>| model-id <asic-model-id>] [json]
    netq [<hostname>] show inventory board [vendor <board-vendor>|model <board-model>] [json]
    netq [<hostname>] show inventory cpu [arch <cpu-arch>] [json]
    netq [<hostname>] show inventory disk [name <disk-name>|transport <disk-transport>| vendor <disk-vendor>] [json]
    netq [<hostname>] show inventory memory [type <memory-type>|vendor <memory-vendor>] [json]

{{%notice note%}}

The keyword values for the `model`, `disk`, `arch`, `name`, `transport`,
and `type` keywords are specific to your deployment. For example, if you
have devices with CPU architectures of only one type, say Intel x86,
then that is the only option available for the `cpu-arch` keyword value.
If you have multiple CPU architectures, say you also have ARMv7, then
that would also be an option for you.

{{%/notice%}}

### View Information about the ASIC on a Switch

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

    cumulus@netq-ts:~$ netq show inventory asic vendor Broadcom
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

### View a Summary of All Hardware Information for a Switch

While the detail can be very helpful, sometimes a simple overview of the
hardware inventory is better. This example shows the basic hardware
information for all devices.

    cumulus@switch:~$ netq show inventory brief
     
    Matching inventory records:
    Hostname          Switch               OS              CPU      ASIC            Ports
    ----------------- -------------------- --------------- -------- --------------- -----------------------------------
    leaf01            VX                   Cumulus Linux   x86_64   N/A             N/A
    leaf02            VX                   Cumulus Linux   x86_64   N/A             N/A
    leaf03            VX                   Cumulus Linux   x86_64   N/A             N/A
    leaf04            VX                   Cumulus Linux   x86_64   N/A             N/A
    oob-mgmt-server   VX                   Cumulus Linux   x86_64   N/A             N/A
    server01          N/A                  Ubuntu          x86_64   N/A             N/A
    server02          N/A                  Ubuntu          x86_64   N/A             N/A
    server03          N/A                  Ubuntu          x86_64   N/A             N/A
    server04          N/A                  Ubuntu          x86_64   N/A             N/A
    spine01           VX                   Cumulus Linux   x86_64   N/A             N/A
    spine02           VX                   Cumulus Linux   x86_64   N/A             N/A

## Monitor Switch Software Information

NetQ enables you to view either a summary or details about the operating
system and license, and whether NetQ Agents are running on your switch
or host. The `netq show inventory` command is used to view the OS and
license information for a single device or for all of your devices at
once, depending on what you want to see. The `netq show agents` command
is used to view the state of the NetQ Agents. You are also able to view
the historical state of these items for one or all devices to determine
if there have been any changes to their status.

The syntax for this command is:

    netq [<hostname>] show inventory brief [json]
    netq [<hostname>] show inventory license [cumulus] [around <text-time>] [json]
    netq [<hostname>] show inventory license [cumulus] changes [between <text-time> and <text-endtime>] [json]
    netq [<hostname>] show inventory os [version <os-version>|name <os-name>] [json]
    netq [<hostname>] show inventory os [version <os-version>|name <os-name>] changes [between <text-time> and <text-endtime>] [json]

{{%notice note%}}

The keyword values for the `name` keyword is specific to your
deployment. For example, if you have devices with only one type of OS,
say Cumulus Linux, then that is the only option available for the
`os-name` keyword value. If you have multiple OSs running, say you also
have Ubuntu, then that would also be an option for you.

{{%/notice%}}

{{%notice note%}}

When entering a time value, you must include a numeric value *and* the
unit of measure:

  - w: week(s)
  - d: day(s)
  - h: hour(s)
  - m: minute(s)
  - s: second(s)
  - now

For time ranges, the `<text-time>` is the most recent time and the
`<text-endtime>` is the oldest time. The values do not have to have the
same unit of measure.

{{%/notice%}}

### View OS Information for a Switch

You can view the name and version of the OS on a switch, and when it was
last modified. This example shows the OS information for all devices.

    cumulus@switch:~$ netq show inventory os
     
    Matching inventory records:
    Hostname          Name            Version                              Last Changed
    ----------------- --------------- ------------------------------------ -------------------------
    leaf01            Cumulus Linux   3.6.2.1~1533263732.39254ac           21d:23h:26m:3s
    leaf02            Cumulus Linux   3.6.2.1~1533263732.39254ac           21d:23h:26m:15s
    leaf03            Cumulus Linux   3.6.2.1~1533263732.39254ac           21d:23h:26m:10s
    leaf04            Cumulus Linux   3.6.1.0~1748339104.32814bc           21d:23h:26m:6s
    oob-mgmt-server   Cumulus Linux   3.7.0~1533263174.bce9472             19d:7h:46m:24s
    server04          Ubuntu          16.04                                21d:23h:26m:7s
    server04          Ubuntu          16.04                                21d:23h:26m:13s
    server04          Ubuntu          16.04                                21d:23h:26m:35s
    server04          Ubuntu          16.04                                21d:23h:26m:52s
    spine01           Cumulus Linux   3.6.2.1~1533263732.39254ac           21d:23h:26m:7s
    spine02           Cumulus Linux   3.6.2.1~1533263732.39254ac           21d:23h:26m:9s

You can filter the results of the command to view only devices with a
particular operating system or version. This can be especially helpful
when you suspect that a particular device has not been upgraded as
expected. This example shows all devices with the Cumulus Linux version
3.6.1 installed.

    cumulus@switch:~$ netq show inventory os version 3.6.1
     
    Matching inventory records:
    Hostname          Name            Version                              Last Changed
    ----------------- --------------- ------------------------------------ -------------------------
    leaf04            Cumulus Linux   3.6.1.0~1748339104.32814bc           21d:23h:26m:6s

This example shows changes that have been made to the OS on all devices
between 16 and 21 days ago. Remember to use measurement units on the
time values.

    cumulus@switch:~$ netq show inventory os changes between 16d and 21d
    Matching inventory records:
    Hostname          Name            Version                              DB State   Last Changed
    ----------------- --------------- ------------------------------------ ---------- -------------------------
    mlx-2410a1-05     Cumulus Linux   3.7.0                                Add        16d:1h:39m:30s
    mlx-2700-11       Cumulus Linux   3.7.0                                Add        16d:1h:39m:32s
    mlx-2100-05       Cumulus Linux   3.7.0                                Add        16d:1h:39m:32s
    mlx-2100-05       Cumulus Linux   3.7.0~1533263174.bce9472             Add        20d:0h:52m:4s
    mlx-2700-11       Cumulus Linux   3.7.0~1533263174.bce9472             Add        20d:0h:52m:22s
    mlx-2100-05       Cumulus Linux   3.7.0~1533263174.bce9472             Add        20d:18h:49m:31s
    mlx-2700-11       Cumulus Linux   3.7.0~1533263174.bce9472             Add        20d:18h:49m:32s

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
    leaf01            Cumulus Linux   ok         21d:23h:43m:4s
    leaf02            Cumulus Linux   ok         21d:23h:43m:16s
    leaf03            Cumulus Linux   ok         21d:23h:43m:12s
    leaf04            Cumulus Linux   ok         21d:23h:43m:7s
    oob-mgmt-server   Cumulus Linux   ok         19d:8h:3m:34s
    server01          Cumulus Linux   N/A        21d:23h:43m:8s
    server02          Cumulus Linux   N/A        21d:23h:43m:17s
    server03          Cumulus Linux   N/A        21d:23h:43m:25s
    server04          Cumulus Linux   N/A        21d:23h:43m:31s
    spine01           Cumulus Linux   ok         21d:23h:43m:8s
    spine02           Cumulus Linux   ok         21d:23h:43m:11s

You can view the historical state of licenses using the around and
changes keywords. This example shows the license state for all devices
about 7 days ago. Remember to use measurement units on the time values.

    cumulus@switch:~$ netq show inventory license around 7d
     
    Matching inventory records:
    Hostname          Name            State      Last Changed
    ----------------- --------------- ---------- -------------------------
    leaf01            Cumulus Linux   ok         14d:23h:43m:4s
    leaf02            Cumulus Linux   ok         14d:23h:43m:16s
    leaf03            Cumulus Linux   ok         14d:23h:43m:12s
    leaf04            Cumulus Linux   ok         14d:23h:43m:7s
    oob-mgmt-server   Cumulus Linux   ok         13d:8h:3m:34s
    server01          Cumulus Linux   N/A        14d:23h:43m:8s
    server02          Cumulus Linux   N/A        14d:23h:43m:17s
    server03          Cumulus Linux   N/A        14d:23h:43m:25s
    server04          Cumulus Linux   N/A        14d:23h:43m:31s
    spine01           Cumulus Linux   ok         14d:23h:43m:8s
    spine02           Cumulus Linux   ok         14d:23h:43m:11s

You can filter the results to show license changes during a particular
timeframe for a particular device. This example shows that there have
been no changes to the license state on spine01 between now and two
weeks ago.

    cumulus@switch:~$ netq spine01 show inventory license changes between now and 2w
    No matching inventory records found

### View Summary of Operating System on a Switch

As with the hardware information, you can view a summary of the software
information using the *brief* keyword. Specify a hostname to view the
summary for a specific device.

    cumulus@switch:~$ netq show inventory brief
     
    Matching inventory records:
    Hostname          Switch               OS              CPU      ASIC            Ports
    ----------------- -------------------- --------------- -------- --------------- -----------------------------------
    leaf01            VX                   Cumulus Linux   x86_64   N/A             N/A
    leaf02            VX                   Cumulus Linux   x86_64   N/A             N/A
    leaf03            VX                   Cumulus Linux   x86_64   N/A             N/A
    leaf04            VX                   Cumulus Linux   x86_64   N/A             N/A
    oob-mgmt-server   VX                   Cumulus Linux   x86_64   N/A             N/A
    server01          N/A                  Ubuntu          x86_64   N/A             N/A
    server02          N/A                  Ubuntu          x86_64   N/A             N/A
    server03          N/A                  Ubuntu          x86_64   N/A             N/A
    server04          N/A                  Ubuntu          x86_64   N/A             N/A
    spine01           VX                   Cumulus Linux   x86_64   N/A             N/A
    spine02           VX                   Cumulus Linux   x86_64   N/A             N/A

### Validate NetQ Agents are Running

You can confirm that NetQ Agents are running on switches and hosts (if
installed) using the `netq show agents` command. Viewing the **Status**
column of the output indicates whether the agent is up and current,
labelled *Fresh*, or down and stale, labelled *Rotten*. Additional
information is provided about the agent status, including whether it is
time synchronized, how long it has been up, and the last time its state
changed.

This example shows NetQ Agent state on all devices. You can view the
state for a single device using the *hostname* keyword.

    cumulus@switch:~$ netq show agents
     
    Matching agents records:
    Hostname          Status           NTP Sync Version                              Sys Uptime                Agent Uptime              Reinitialize Time          Last Changed
    ----------------- ---------------- -------- ------------------------------------ ------------------------- ------------------------- -------------------------- -------------------------
    leaf01            Fresh            no       1.3.0-cl3u9~1522970647.b08ca60       22d:4h:39m:26s            22d:4h:19m:6s             22d:0h:8m:20s              18.417234s
    leaf02            Fresh            no       1.3.0-cl3u9~1522970647.b08ca60       22d:4h:33m:0s             22d:4h:18m:26s            22d:0h:8m:33s              15.413085s
    leaf03            Fresh            no       1.3.0-cl3u9~1522970647.b08ca60       22d:4h:35m:14s            22d:4h:18m:56s            22d:0h:8m:28s              31.478846s
    leaf04            Fresh            no       1.3.0-cl3u9~1522970647.b08ca60       22d:4h:35m:48s            22d:4h:19m:5s             22d:0h:8m:23s              17.819782s
    oob-mgmt-server   Fresh            yes      1.4.0-cl3u10~1534306219.882a7e7      22d:0h:10m:32s            19d:8h:28m:38s            19d:8h:28m:38s             12.330358s
    server01          Fresh            yes      1.3.0-ub16.04u9~1522971904.b08ca60   22d:4h:25m:58s            11m:46.982s               11m:46.982s                11.973292s
    server02          Fresh            yes      1.3.0-ub16.04u9~1522971904.b08ca60   22d:4h:25m:57s            10m:11.888s               10m:11.888s                7.469695s
    server03          Fresh            yes      1.3.0-ub16.04u9~1522971904.b08ca60   22d:4h:26m:9s             9m:49.763s                9m:49.763s                 15.437087s
    server04          Fresh            yes      1.3.0-ub16.04u9~1522971904.b08ca60   22d:4h:26m:36s            22d:4h:21m:6s             22d:0h:8m:23s              13.428345s
    spine01           Fresh            no       1.3.0-cl3u9~1522970647.b08ca60       22d:4h:40m:8s             22d:4h:18m:53s            22d:0h:8m:24s              32.40132s
    spine02           Fresh            no       1.3.0-cl3u9~1522970647.b08ca60       22d:4h:33m:13s            22d:4h:19m:7s             22d:0h:8m:27s              23.748967s

You can view the state of NetQ Agents at an earlier time using the
*around* and *changes* keywords.

## Monitor Software Services

Cumulus Linux and NetQ run a number of services to deliver the various
features of these products. You can monitor their status using the `netq
show services` command. The services related to system-level operation
are described here. Monitoring of other services, such as those related
to routing, are described with those topics. NetQ automatically monitors
t he following services:

  - bgpd: BGP (Border Gateway Protocol) daemon
  - clagd: MLAG (Multi-chassis Link Aggregation) daemon
  - cumulus-chassis-ssh: Secure Shell for hardware chassis
  - cumulus-chassisd: Chassis daemon
  - ledmgrd: Switch LED manager daemon
  - lldpd: LLDP (Link Layer Discovery Protocol) daemon
  - mstpd: MSTP (Multiple Spanning Tree Protocol) daemon
  - neighmgrd: Neighbor Manager daemon for BGP and OSPF
  - netq-agent: NetQ Agent service
  - netq-notifier: NetQ Notifier service
  - netqd: NetQ telemetry application daemon
  - ntp: NTP service
  - ospf6d : OSPFv6 (Open Shortest Path First) daemon
  - ospfd: OSPF daemon
  - ptmd: PTM (Prescriptive Topology Manager) daemon
  - pwmd : PWM (Password Manager) daemon
  - rsyslog: Rocket-fast system event logging processing service
  - smond: System monitor daemon
  - ssh: Secure Shell service for switches and servers
  - status: License validation service
  - syslog: System event logging service
  - vrf: VRF (Virtual Route Forwarding) service
  - vxrd: Registration daemon for VXLAN BUM (broadcast, unknown unicast, and
    multicast) Flooding (VXFLD)
  - vxsnd: Service node daemon for VXFLD
  - zebra: GNU Zebra routing daemon

The CLI syntax for viewing the status of services is:

    netq [<hostname>] show services [<service-name>] [vrf <vrf>] [active|monitored] [around <text-time>] [json]
    netq [<hostname>] show services [<service-name>] [vrf <vrf>] [active|monitored] changes [between <text-time> and <text-endtime>] [json]
    netq [<hostname>] show services [<service-name>] [vrf <vrf>] status (ok|warning|error|fail) [around <text-time>] [json]
    netq [<hostname>] show services [<service-name>] [vrf <vrf>] status (ok|warning|error|fail) changes [between <text-time> and <text-endtime>] [json]
    netq [<hostname>] show services [<service-name>] [vrf <vrf>] status (ok|warning|error|fail) changes [json]

{{%notice note%}}

The *active* and *monitored* keywords are not processed correctly in
this release. Refer to the [Release
Notes](https://support.cumulusnetworks.com/hc/en-us/articles/360005898274)
 for more detail.

{{%/notice%}}

### View All Services on All Devices

This example shows all of the available services on each device and
whether each is enabled, active, and monitored, along with how long the
service has been running and the last time it was changed.

    cumulus@switch:~$ netq show services
     
    Matching services records:
    Hostname          Service              PID   VRF             Enabled Active Monitored Status           Uptime                    Last Changed
    ----------------- -------------------- ----- --------------- ------- ------ --------- ---------------- ------------------------- -------------------------
    leaf02            bgpd                 2013  default         yes     yes    yes       ok               5h:1m:10s                 6m:41.781s
    leaf02            clagd                1169  default         yes     yes    yes       ok               5h:2m:0s                  6m:42.777s
    leaf02            cumulus-chassis-ssh  n/a   default         no      no     no        n/a              2d:4h:15m:58s             2d:4h:15m:58s
    leaf02            cumulus-chassisd     n/a   default         no      no     no        n/a              2d:4h:15m:58s             2d:4h:15m:58s
    leaf02            ledmgrd              612   default         yes     yes    no        ok               5h:2m:15s                 6m:50.946s
    leaf02            lldpd                1160  default         yes     yes    yes       ok               5h:2m:3s                  6m:28.313s
    leaf02            mstpd                448   default         yes     yes    yes       ok               5h:2m:19s                 6m:42.884s
    leaf02            neighmgrd            1094  default         yes     yes    no        ok               5h:2m:5s                  6m:50.940s
    leaf02            netq-agent           n/a   default         no      no     yes       n/a              6m:50.943s                6m:50.943s
    leaf02            netq-notifier        n/a   default         no      no     yes       n/a              2d:4h:15m:58s             2d:4h:15m:58s
    leaf02            netqd                n/a   default         no      no     yes       n/a              6m:50.944s                6m:50.944s
    leaf02            ntp                  n/a   default         no      no     yes       n/a              6m:50.936s                6m:50.936s
    leaf02            ospf6d               n/a   default         no      no     no        n/a              2d:4h:15m:58s             2d:4h:15m:58s
    leaf02            ospfd                n/a   default         no      no     yes       n/a              6m:41.922s                6m:41.922s
    leaf02            ptmd                 1162  default         yes     yes    no        ok               5h:2m:3s                  6m:51.441s
    leaf02            pwmd                 613   default         yes     yes    no        ok               5h:2m:15s                 6m:50.948s
    leaf02            smond                609   default         yes     yes    yes       ok               5h:2m:15s                 6m:28.279s
    leaf02            ssh                  1125  default         yes     yes    no        ok               5h:2m:5s                  6m:50.935s
    leaf02            syslog               393   default         yes     yes    no        ok               5h:2m:19s                 6m:50.934
    leaf02            vxrd                 n/a   default         no      no     yes       n/a              6m:9.742s                 6m:9.742s
    leaf02            vxsnd                n/a   default         no      no     yes       n/a              6m:9.756s                 6m:9.756s
    leaf02            zebra                2006  default         yes     yes    yes       ok               6m:28.244s                6m:28.244s
    server01          lldpd                1359  default         yes     yes    yes       ok               2h:0m:25s                 4h:59m:45s
    server01          netq-agent           1363  default         yes     yes    yes       ok               2h:0m:26s                 5h:0m:7s
    server01          netq-notifier        n/a   default         no      no     yes       n/a              2d:4h:16m:1s              2d:4h:16m:1s
    server01          netqd                1355  default         yes     yes    yes       ok               2h:0m:26s                 5h:0m:7s
    server01          ntp                  0     default         yes     yes    yes       ok               2h:0m:20s                 5h:0m:7s
    server01          ssh                  1358  default         yes     yes    no        ok               2h:0m:25s                 5h:0m:7s
    server01          syslog               967   default         yes     yes    no        ok               2h:0m:27s                 5h:0m:7s
    ...

You can also view services information in JSON format:

    cumulus@switch:~$ netq show services json
    {
        "services":[
            {
                "status":"ok",
                "uptime":1537904537.0,
                "monitored":"yes",
                "service":"netqd",
                "lastChanged":1537893777.617677927,
                "pid":"1047",
                "hostname":"edge01",
                "enabled":"yes",
                "vrf":"default",
                "active":"yes"
            },
            {
                "status":"ok",
                "uptime":1537904537.0,
                "monitored":"yes",
                "service":"netq-agent",
                "lastChanged":1537893777.6185410023,
                "pid":"1052",
                "hostname":"edge01",
                "enabled":"yes",
                "vrf":"default",
                "active":"yes"
            },
    ...

If you want to view the service information for a given device, simply
use the *hostname* variable to the command.

### View Information about a Given Service on All Devices

You can view the status of a given service at the current time, at a
prior point in time, or view the changes that have occurred for the
service during a specified timeframe.

This example shows how to view the status of the NTP service across the
network. In this case, VRF is configured so the NTP service runs on both
the default and management interface. You can perform the same command
with the other services, such as `netq-agent`, `netq-notifier`, and
`syslog`.

    cumulus@switch:~$ netq show services ntp
     
    Matching services records:
    Hostname          Service              PID   VRF             Enabled Active Monitored Status           Uptime                    Last Changed
    ----------------- -------------------- ----- --------------- ------- ------ --------- ---------------- ------------------------- -------------------------
    edge01            ntp                  0     default         yes     yes    yes       ok               2d:1h:24m:10s             2d:4h:23m:36s
    exit01            ntp                  1238  mgmt            yes     yes    yes       ok               5h:9m:8s                  8m:4.578s
    exit01            ntp                  n/a   default         no      no     yes       n/a              8m:4.583s                 8m:4.583s
    exit02            ntp                  1233  mgmt            yes     yes    yes       ok               5h:9m:8s                  7m:41.133s
    exit02            ntp                  n/a   default         no      no     yes       n/a              7m:41.137s                7m:41.137s
    internet          ntp                  n/a   default         no      no     yes       n/a              5h:9m:6s                  5h:9m:6s
    internet          ntp                  n/a   mgmt            yes     no     yes       n/a              5h:8m:51s                 5h:8m:51s
    leaf01            ntp                  1555  mgmt            yes     yes    yes       ok               5h:9m:10s                 1h:1m:5s
    leaf01            ntp                  n/a   default         no      no     yes       n/a              1h:1m:5s                  1h:1m:5s
    leaf02            ntp                  1565  mgmt            yes     yes    yes       ok               5h:9m:9s                  14m:25.774s
    leaf02            ntp                  n/a   default         no      no     yes       n/a              14m:25.778s               14m:25.778s
    leaf03            ntp                  1564  mgmt            yes     yes    yes       ok               5h:9m:9s                  13m:36.464s
    leaf03            ntp                  n/a   default         no      no     yes       n/a              13m:36.469s               13m:36.469s
    leaf04            ntp                  1551  mgmt            yes     yes    yes       ok               5h:9m:8s                  10m:15.960s
    leaf04            ntp                  n/a   default         no      no     yes       n/a              10m:15.964s               10m:15.964s
    oob-mgmt-server   ntp                  813   default         yes     yes    yes       ok               2d:4h:25m:35s             2d:4h:23m:9s
    server01          ntp                  0     default         yes     yes    yes       ok               2h:7m:55s                 5h:7m:42s
    server02          ntp                  0     default         yes     yes    yes       ok               2h:7m:55s                 5h:7m:42s
    server03          ntp                  0     default         yes     yes    yes       ok               2h:7m:55s                 5h:7m:42s
    server04          ntp                  0     default         yes     yes    yes       ok               2h:7m:55s                 5h:7m:42s
    spine01           ntp                  1188  mgmt            yes     yes    yes       ok               5h:9m:8s                  9m:32.856s
    spine01           ntp                  n/a   default         no      no     yes       n/a              9m:32.861s                9m:32.861s
    spine02           ntp                  1188  mgmt            yes     yes    yes       ok               5h:9m:7s                  9m:4.722s
    spine02           ntp                  n/a   default         no      no     yes       n/a              9m:4.726s                 9m:4.726s

This example shows the status of the BGP daemon.

    cumulus@switch:~$ netq show services bgpd
     
    Matching services records:
    Hostname          Service              PID   VRF             Enabled Active Monitored Status           Uptime                    Last Changed
    ----------------- -------------------- ----- --------------- ------- ------ --------- ---------------- ------------------------- -------------------------
    exit01            bgpd                 1627  default         yes     yes    yes       ok               5h:25m:43s                24m:55.103s
    exit02            bgpd                 1628  default         yes     yes    yes       ok               5h:25m:36s                24m:33.633s
    internet          bgpd                 1493  default         yes     yes    yes       ok               5h:25m:34s                5h:25m:20s
    leaf01            bgpd                 2009  default         yes     yes    yes       ok               5h:25m:44s                1h:17m:57s
    leaf02            bgpd                 2013  default         yes     yes    yes       ok               5h:25m:44s                31m:16.166s
    leaf03            bgpd                 2010  default         yes     yes    yes       ok               5h:25m:44s                30m:27.992s
    leaf04            bgpd                 1998  default         yes     yes    yes       ok               5h:25m:43s                27m:7.428s
    spine01           bgpd                 1559  default         yes     yes    yes       ok               5h:25m:35s                26m:24.326s
    spine02           bgpd                 1553  default         yes     yes    yes       ok               5h:25m:35s                25m:56.141s
