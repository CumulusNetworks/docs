---
title: Networkwide Inventory
author: NVIDIA
weight: 730
toc: 4
---

With the NetQ UI and CLI, a user can monitor the inventory on a networkwide basis for all switches, hosts, and DPUs. Inventory includes such items as the number of each device and its operating system. Additional details are available about the hardware and software components on individual switches, such as the motherboard, ASIC, microprocessor, disk, memory, fan and power supply information.
The commands and cards available to obtain this type of information help you to answer questions such as:

<!-- vale off -->
- Which switches are being monitored in the network?
- What is the distribution of ASICs, CPUs, agents, and so forth across my network?
- Are NetQ Agents running on all of my switches?
- What hardware is installed on my switches?
- What software is installed on my switches?
<!-- vale on -->

To monitor the inventory of a given switch or DPU, refer to {{<link title="Switch Inventory">}} or {{<link title="DPU Inventory">}}.

## Access Networkwide Inventory Data

The Inventory/Devices card displays networkwide inventory information for all switches, hosts, and DPUs.

{{<img src="/images/netq/inventory-devices-l2-42.png" width="200">}}

The NetQ CLI provides detailed network inventory information through its `netq show inventory` command.

## View Networkwide Inventory Summary

{{<tabs "View worldwide inventory summary">}}

{{<tab "NetQ UI">}}

### View the Number of Each Device Type in Your Network

To view the quantity of devices in your network, open the Inventory/Devices card. The medium-sized card displays operating system distribution across the network in addition to the device count. Hover over items in the chart’s outer circle to view operating system distribution, and hover over items in the chart’s inner circle to view device counts.

{{<figure src="/images/netq/inventory-devices-l1-42.png" alt="small inventory card displaying 13 switches and 10 hosts" width="200">}}
{{<figure src="/images/netq/inventory-devices-l2-42.png" alt="medium inventory card displaying 15 switches and 10 hosts as a chart" width="200">}}

### View All Switches

You can view all stored attributes for all switches in your network from either the Inventory/Devices card:
- Open the full-screen Inventory/Devices card and select **Ethernet switches**:

    {{<figure src="/images/netq/inventory-devices-switches.png" alt="full-screen inventory/devices card displaying a list of switches" width="900">}}

### View Hosts

You can view all stored attributes for all hosts in your network. To view all host details, open the full screen Inventory/Devices card and select **Hosts**.

{{<figure src="/images/netq/inventory-devices-hosts.png" alt="full-screen inventory/devices card displaying a list of hosts" width="900" >}}

{{</tab>}}

{{<tab "NetQ CLI">}}

To view a list of devices in your network, run:

```
netq show inventory brief [json]
```

This example shows that there are four spine switches, three leaf switches, two border switches, two firewall switches, seven hosts (servers), and an out-of-band management server in this network. Each entry displays the type of switch, operating system, CPU, and ASIC.

```
cumulus@switch:~$ netq show inventory brief
Matching inventory records:
Hostname          Switch               OS              CPU      ASIC            Ports
----------------- -------------------- --------------- -------- --------------- -----------------------------------
border01          VX                   CL              x86_64   VX              N/A
border02          VX                   CL              x86_64   VX              N/A
fw1               VX                   CL              x86_64   VX              N/A
fw2               VX                   CL              x86_64   VX              N/A
leaf01            VX                   CL              x86_64   VX              N/A
leaf02            VX                   CL              x86_64   VX              N/A
leaf03            VX                   CL              x86_64   VX              N/A
oob-mgmt-server   N/A                  Ubuntu          x86_64   N/A             N/A
server01          N/A                  Ubuntu          x86_64   N/A             N/A
server02          N/A                  Ubuntu          x86_64   N/A             N/A
server03          N/A                  Ubuntu          x86_64   N/A             N/A
server04          N/A                  Ubuntu          x86_64   N/A             N/A
server05          N/A                  Ubuntu          x86_64   N/A             N/A
server06          N/A                  Ubuntu          x86_64   N/A             N/A
server07          N/A                  Ubuntu          x86_64   N/A             N/A
spine01           VX                   CL              x86_64   VX              N/A
spine02           VX                   CL              x86_64   VX              N/A
spine03           VX                   CL              x86_64   VX              N/A
spine04           VX                   CL              x86_64   VX              N/A
```

{{</tab>}}

{{</tabs>}}

## View Networkwide Hardware Inventory

You can view hardware components deployed on all switches and hosts, or on all switches in your network.

### View Components Summary

It can be useful to know the quantity and ratio of many components deployed in your network to determine the scope of upgrade tasks, balance vendor reliance, or for detailed troubleshooting.

{{<tabs "View component summary">}}

{{<tab "Inventory/Devices">}}

1. Locate the Inventory/Devices card on your workbench.

2. Hover over the card, and change to the large size card using the size picker.

   By default, the Switches tab shows the total number of switches, ASIC vendors, OS versions, NetQ Agent versions, and specific platforms deployed across all your switches.

   You can hover over any of the segments in a component distribution chart to highlight a specific type of the given component. When you *hover*, a tooltip appears displaying:

   - Name or value of the component type, such as the version number or status
   - Total number of switches with that type of component deployed compared to the total number of switches
   - Percentage of this type as compared to all component types

   {{<figure src="/images/netq/large-switches-inventory-devices.png" width="650">}}

{{</tab>}}

{{<tab "netq show inventory">}}

To view switch components, run:

```
netq show inventory brief [json]
```

This example shows the operating systems (Cumulus Linux and Ubuntu), CPU architecture (all x86_64), ASIC (virtual), and ports (N/A because Cumulus VX is virtual) for each device in the network.

```
cumulus@switch:~$ netq show inventory brief
Matching inventory records:
Hostname          Switch               OS              CPU      ASIC            Ports
----------------- -------------------- --------------- -------- --------------- -----------------------------------
border01          VX                   CL              x86_64   VX              N/A
border02          VX                   CL              x86_64   VX              N/A
fw1               VX                   CL              x86_64   VX              N/A
fw2               VX                   CL              x86_64   VX              N/A
leaf01            VX                   CL              x86_64   VX              N/A
leaf02            VX                   CL              x86_64   VX              N/A
leaf03            VX                   CL              x86_64   VX              N/A
oob-mgmt-server   N/A                  Ubuntu          x86_64   N/A             N/A
server01          N/A                  Ubuntu          x86_64   N/A             N/A
server02          N/A                  Ubuntu          x86_64   N/A             N/A
server03          N/A                  Ubuntu          x86_64   N/A             N/A
server04          N/A                  Ubuntu          x86_64   N/A             N/A
server05          N/A                  Ubuntu          x86_64   N/A             N/A
server06          N/A                  Ubuntu          x86_64   N/A             N/A
server07          N/A                  Ubuntu          x86_64   N/A             N/A
spine01           VX                   CL              x86_64   VX              N/A
spine02           VX                   CL              x86_64   VX              N/A
spine03           VX                   CL              x86_64   VX              N/A
spine04           VX                   CL              x86_64   VX              N/A
```

{{</tab>}}

{{</tabs>}}

### View ASIC Information

{{<tabs "TabID158" >}}

{{<tab "Inventory/Devices">}}

1. Locate the medium Inventory/Devices card on your workbench.

2. Hover over the card, and change to the large size card using the size picker.

3. Click a segment of the ASIC graph in the component distribution charts. Select **Filter ASIC**:

    {{<figure src="/images/netq/filter-asic-large.png" width="500">}}

4. Alternately, expand the card to full screen to view ASIC information as a column in a table.

{{</tab>}}

{{<tab "netq show inventory" >}}

To view information about the ASIC installed on your devices, run:

```
netq show inventory asic [vendor <asic-vendor>|model <asic-model>|model-id <asic-model-id>] [json]
```

{{<notice tip>}}

If you are running NetQ on a CumulusVX setup, there is no physical hardware to query and thus no ASIC information to display.

{{</notice>}}

This example shows the ASIC information for all devices in your network:

```
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
st1-l1            Broadcom             Trident2                       BCM56854                  720G           48 x 10G-SFP+ & 6 x 40G-QSFP+
st1-l2            Broadcom             Trident2                       BCM56854                  720G           48 x 10G-SFP+ & 6 x 40G-QSFP+
st1-l3            Broadcom             Trident2                       BCM56854                  720G           48 x 10G-SFP+ & 6 x 40G-QSFP+
st1-s1            Broadcom             Trident2                       BCM56850                  960G           32 x 40G-QSFP+
st1-s2            Broadcom             Trident2                       BCM56850                  960G           32 x 40G-QSFP+
```

You can filter the results of the command to view devices with a particular vendor, model, or modelID. This example shows ASIC information for all devices with a vendor of *NVIDIA*.

```
cumulus@switch:~$ netq show inventory asic vendor NVIDIA
Matching inventory records:
Hostname          Vendor               Model                          Model ID                  Core BW        Ports
----------------- -------------------- ------------------------------ ------------------------- -------------- -----------------------------------
mlx-2100-05       NVIDIA               Spectrum                       MT52132                   N/A            16 x 100G-QSFP28
mlx-2410a1-05     NVIDIA               Spectrum                       MT52132                   N/A            48 x 25G-SFP28 & 8 x 100G-QSFP28
mlx-2700-11       NVIDIA               Spectrum                       MT52132                   N/A            32 x 100G-QSFP28
```

{{</tab>}}

{{</tabs>}}

### View Motherboard/Platform Information

{{<tabs "TabID266" >}}

{{<tab "Inventory/Devices">}}

1. Locate the Inventory/Devices card on your workbench.

2. Hover over the card, and change to the full-screen card using the size picker.

3. The **All Switches** tab is active by default. Scroll to the right to view the various Platform parameters for your switches. Optionally drag and drop the relevant columns next to each other.

    {{<figure src="/images/netq/inventory-devices-fullscr-allswitches-tab-320.png" width="700">}}

4. Click **All Hosts**.

5. Scroll to the right to view the various Platform parameters for your hosts. Optionally drag and drop the relevant columns next to each other.

    {{<figure src="/images/netq/inventory-devices-fullscr-allhosts-tab-320.png" width="700">}}

{{</tab>}}

{{<tab "netq show inventory" >}}

To view a list of motherboards installed in your switches and hosts, run:

```
netq show inventory board [vendor <board-vendor>|model <board-model>] [json]
```

This example shows all motherboard data for all devices.

```
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
```

You can filter the results of the command to capture only those devices with a particular motherboard vendor or model. This example shows only the devices with a *Celestica* motherboard.

```
cumulus@switch:~$ netq show inventory board vendor celestica
Matching inventory records:
Hostname          Vendor               Model                          Base MAC           Serial No                 Part No          Rev    Mfg Date
----------------- -------------------- ------------------------------ ------------------ ------------------------- ---------------- ------ ----------
st1-l1            CELESTICA            Arctica 4806xp                 00:E0:EC:27:71:37  D2060B2F044919GD000011    R0854-F1004-01   Redsto 09/20/2014
                                                                                                                                    ne-XP
st1-l2            CELESTICA            Arctica 4806xp                 00:E0:EC:27:6B:3A  D2060B2F044919GD000060    R0854-F1004-01   Redsto 09/20/2014
                                                                                                                                    ne-XP
```

{{</tab>}}

{{</tabs>}}

### View CPU Information

{{<tabs "TabID304" >}}

{{<tab "Inventory/Devices" >}}

1. Locate the Inventory/Devices card on your workbench.

2. Hover over the card, and change to the full-screen card using the size picker.

3. The **All Switches** tab is active by default. Scroll to the right to view the various CPU parameters. Optionally drag and drop relevant columns next to each other.

    {{<figure src="/images/netq/inventory-devices-fullscr-allswitches-tab-320.png" width="700">}}

4. Click **All Hosts** to view the CPU information for your host servers.

    {{<figure src="/images/netq/inventory-devices-fullscr-allhosts-tab-320.png" width="700" >}}

{{</tab>}}

{{<tab "netq show inventory" >}}

To view CPU information for all devices in your network, run:

```
netq show inventory cpu [arch <cpu-arch>] [json]
```

This example shows the CPU information for all devices.

```
cumulus@switch:~$ netq show inventory cpu
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
```

You can filter the results of the command to view which switches employ a particular CPU architecture using the *arch* keyword. This example shows how to determine all the currently deployed architectures in your network, and then shows all devices with an *x86\_64* architecture.

```
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
```

{{</tab>}}

{{</tabs>}}

### View Disk Information

{{<tabs "TabID591" >}}

{{<tab "Inventory/Devices" >}}

1. Locate the Inventory/Devices card on your workbench.

2. Hover over the card, and change to the full-screen card using the size picker.

    {{<figure src="/images/netq/inventory-devices-fullscr-allswitches-tab-241.png" width="700">}}

3. The **All Switches** tab is selected by default. Locate the **Disk Total Size** column.

4. Click **All Hosts** to view the total disk size of all host servers.

    {{<figure src="/images/netq/inventory-devices-fullscr-allhosts-tab-241.png" width="700" >}}

{{</tab>}}

{{<tab "netq show inventory" >}}

To view disk information for your switches, run:

```
netq show inventory disk [name <disk-name>|transport <disk-transport>|vendor <disk-vendor>] [json]
```

This example shows the disk information for all devices.

```
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
```

{{</tab>}}

{{</tabs>}}

### View Memory Information

{{<tabs "TabID480" >}}

{{<tab "Inventory/Devices" >}}

1. Locate the Inventory/Devices card on your workbench.

2. Hover over the card, and change to the full-screen card using the size picker.

    {{<figure src="/images/netq/inventory-devices-fullscr-allswitches-tab-241.png" width="700">}}

3. The **All Switches** tab is selected by default. Locate the **Memory Size** column.

4. Click **All Hosts** to view the memory size for all host servers.

    {{<figure src="/images/netq/inventory-devices-fullscr-allhosts-tab-241.png" width="700" >}}

{{</tab>}}

{{<tab "netq show inventory" >}}

To view memory information for your switches and host servers, run:

```
netq show inventory memory [type <memory-type>|vendor <memory-vendor>] [json]
```

This example shows all memory characteristics for all devices.

```
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
```

You can filter the results of the command to view devices with a particular memory type or vendor. This example shows all the devices with memory from *QEMU* .

```
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
```

{{</tab>}}

{{</tabs>}}

### View Sensor Information

Fan, power supply unit (PSU), and temperature sensors are available to provide additional data about the NetQ system operation.

{{<tabs "TabID758" >}}

{{<tab "NetQ UI" >}}

#### Power Supply Unit Information

1. Click <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/03-Menu/navigation-menu.svg" height="18" width="18"/> Menu, then click **Sensors**.

2. The PSU tab is displayed by default.

    {{<figure src="/images/netq/main-menu-ntwk-sensors-psu-310.png" width="700">}}

<div style="padding-left: 18px;">
<table>
<thead>
<tr>
<th>PSU Parameter</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>Hostname</td>
<td>Name of the switch or host where the power supply is installed</td>
</tr>
<tr>
<td>Timestamp</td>
<td>Date and time the data was captured</td>
</tr>
<tr>
<td>Message Type</td>
<td>Type of sensor message; always <em>PSU</em> in this table</td>
</tr>
<tr>
<td>PIn(W)</td>
<td>Input power (Watts) for the PSU on the switch or host</td>
</tr>
<tr>
<td>POut(W)</td>
<td>Output power (Watts) for the PSU on the switch or host</td>
</tr>
<tr>
<td>Sensor Name</td>
<td>User-defined name for the PSU</td>
</tr>
<tr>
<td>Previous State</td>
<td>State of the PSU when data was captured in previous window</td>
</tr>
<tr>
<td>State</td>
<td>State of the PSU when data was last captured</td>
</tr>
<tr>
<td>VIn(V)</td>
<td>Input voltage (Volts) for the PSU on the switch or host</td>
</tr>
<tr>
<td>VOut(V)</td>
<td>Output voltage (Volts) for the PSU on the switch or host</td>
</tr>
</tbody>
</table>
</div>

#### Fan Information

1. Click <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/03-Menu/navigation-menu.svg" height="18" width="18"/> Menu, then click **Sensors** in the **Network** heading.

2. Click **Fan**.

    {{<figure src="/images/netq/main-menu-ntwk-sensors-fan-320.png" width="700">}}

<div style="padding-left: 18px;">
<table>
<thead>
<tr>
<th>Fan Parameter</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>Hostname</td>
<td>Name of the switch or host where the fan is installed</td>
</tr>
<tr>
<td>Timestamp</td>
<td>Date and time the data was captured</td>
</tr>
<tr>
<td>Message Type</td>
<td>Type of sensor message; always <em>Fan</em> in this table</td>
</tr>
<tr>
<td>Description</td>
<td>User specified description of the fan</td>
</tr>
<tr>
<td>Speed (RPM)</td>
<td>Revolution rate of the fan (revolutions per minute)</td>
</tr>
<tr>
<td>Max</td>
<td>Maximum speed (RPM)</td>
</tr>
<tr>
<td>Min</td>
<td>Minimum speed (RPM)</td>
</tr>
<tr>
<td>Message</td>
<td>Message</td>
</tr>
<tr>
<td>Sensor Name</td>
<td>User-defined name for the fan</td>
</tr>
<tr>
<td>Previous State</td>
<td>State of the fan when data was captured in previous window</td>
</tr>
<tr>
<td>State</td>
<td>State of the fan when data was last captured</td>
</tr>
</tbody>
</table>
</div>

#### Temperature Information

1. Click <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/03-Menu/navigation-menu.svg" height="18" width="18"/> Menu, then click **Sensors** in the **Network** heading.

2. Click **Temperature**.

    {{<figure src="/images/netq/main-menu-ntwk-sensors-temp-320.png" width="700">}}

<div style="padding-left: 18px;">
<table>
<thead>
<tr>
<th>Temperature Parameter</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>Hostname</td>
<td>Name of the switch or host where the temperature sensor is installed</td>
</tr>
<tr>
<td>Timestamp</td>
<td>Date and time the data was captured</td>
</tr>
<tr>
<td>Message Type</td>
<td>Type of sensor message; always <em>Temp</em> in this table</td>
</tr>
<tr>
<td>Critical</td>
<td>Current critical maximum temperature (&deg;C) threshold setting</td>
</tr>
<tr>
<td>Description</td>
<td>User specified description of the temperature sensor</td>
</tr>
<tr>
<td>Lower Critical</td>
<td>Current critical minimum temperature (&deg;C) threshold setting</td>
</tr>
<tr>
<td>Max</td>
<td>Maximum temperature threshold setting</td>
</tr>
<tr>
<td>Min</td>
<td>Minimum temperature threshold setting</td>
</tr>
<tr>
<td>Message</td>
<td>Message</td>
</tr>
<tr>
<td>Sensor Name</td>
<td>User-defined name for the temperature sensor</td>
</tr>
<tr>
<td>Previous State</td>
<td>State of the fan when data was captured in previous window</td>
</tr>
<tr>
<td>State</td>
<td>State of the fan when data was last captured</td>
</tr>
<tr>
<td>Temperature(Celsius)</td>
<td>Current temperature (&deg;C) measured by sensor</td>
</tr>
</tbody>
</table>
</div>

{{</tab>}}

{{<tab "NetQ CLI" >}}

#### View All Sensor Information

To view information for power supplies, fans, and temperature sensors on all switches and host servers, run:

```
netq show sensors all [around <text-time>] [json]
```

Use the `around` option to view sensor information for a time in the past.

This example shows all sensors on all devices.

```
cumulus@switch:~$ netq show sensors all
Matching sensors records:
Hostname          Name            Description                         State      Message                             Last Changed
----------------- --------------- ----------------------------------- ---------- ----------------------------------- -------------------------
border01          fan5            fan tray 3, fan 1                   ok                                             Fri Aug 21 18:51:11 2020
border01          fan6            fan tray 3, fan 2                   ok                                             Fri Aug 21 18:51:11 2020
border01          fan1            fan tray 1, fan 1                   ok                                             Fri Aug 21 18:51:11 2020
...
fw1               fan2            fan tray 1, fan 2                   ok                                             Thu Aug 20 19:16:12 2020
...
fw2               fan3            fan tray 2, fan 1                   ok                                             Thu Aug 20 19:14:47 2020
...
leaf01            psu2fan1        psu2 fan                            ok                                             Fri Aug 21 16:14:22 2020
...
leaf02            fan3            fan tray 2, fan 1                   ok                                             Fri Aug 21 16:14:14 2020
...
leaf03            fan2            fan tray 1, fan 2                   ok                                             Fri Aug 21 09:37:45 2020
...
leaf04            psu1fan1        psu1 fan                            ok                                             Fri Aug 21 09:17:02 2020
...
spine01           psu2fan1        psu2 fan                            ok                                             Fri Aug 21 05:54:14 2020
...
spine02           fan2            fan tray 1, fan 2                   ok                                             Fri Aug 21 05:54:39 2020
...
spine03           fan4            fan tray 2, fan 2                   ok                                             Fri Aug 21 06:00:52 2020
...
spine04           fan2            fan tray 1, fan 2                   ok                                             Fri Aug 21 05:54:09 2020
...
border01          psu1temp1       psu1 temp sensor                    ok                                             Fri Aug 21 18:51:11 2020
border01          temp2           board sensor near virtual switch    ok                                             Fri Aug 21 18:51:11 2020
border01          temp3           board sensor at front left corner   ok                                             Fri Aug 21 18:51:11 2020
...
border02          temp1           board sensor near cpu               ok                                             Fri Aug 21 18:46:05 2020
...
fw1               temp4           board sensor at front right corner  ok                                             Thu Aug 20 19:16:12 2020
...
fw2               temp5           board sensor near fan               ok                                             Thu Aug 20 19:14:47 2020
...
leaf01            psu1temp1       psu1 temp sensor                    ok                                             Fri Aug 21 16:14:22 2020
...
leaf02            temp5           board sensor near fan               ok                                             Fri Aug 21 16:14:14 2020
...
leaf03            psu2temp1       psu2 temp sensor                    ok                                             Fri Aug 21 09:37:45 2020
...
leaf04            temp4           board sensor at front right corner  ok                                             Fri Aug 21 09:17:02 2020
...
spine01           psu1temp1       psu1 temp sensor                    ok                                             Fri Aug 21 05:54:14 2020
...
spine02           temp3           board sensor at front left corner   ok                                             Fri Aug 21 05:54:39 2020
...
spine03           temp1           board sensor near cpu               ok                                             Fri Aug 21 06:00:52 2020
...
spine04           temp3           board sensor at front left corner   ok                                             Fri Aug 21 05:54:09 2020
...
border01          psu1            N/A                                 ok                                             Fri Aug 21 18:51:11 2020
border01          psu2            N/A                                 ok                                             Fri Aug 21 18:51:11 2020
border02          psu1            N/A                                 ok                                             Fri Aug 21 18:46:05 2020
border02          psu2            N/A                                 ok                                             Fri Aug 21 18:46:05 2020
fw1               psu1            N/A                                 ok                                             Thu Aug 20 19:16:12 2020
fw1               psu2            N/A                                 ok                                             Thu Aug 20 19:16:12 2020
fw2               psu1            N/A                                 ok                                             Thu Aug 20 19:14:47 2020
fw2               psu2            N/A                                 ok                                             Thu Aug 20 19:14:47 2020
leaf01            psu1            N/A                                 ok                                             Fri Aug 21 16:14:22 2020
leaf01            psu2            N/A                                 ok                                             Fri Aug 21 16:14:22 2020
leaf02            psu1            N/A                                 ok                                             Fri Aug 21 16:14:14 2020
leaf02            psu2            N/A                                 ok                                             Fri Aug 21 16:14:14 2020
leaf03            psu1            N/A                                 ok                                             Fri Aug 21 09:37:45 2020
leaf03            psu2            N/A                                 ok                                             Fri Aug 21 09:37:45 2020
leaf04            psu1            N/A                                 ok                                             Fri Aug 21 09:17:02 2020
leaf04            psu2            N/A                                 ok                                             Fri Aug 21 09:17:02 2020
spine01           psu1            N/A                                 ok                                             Fri Aug 21 05:54:14 2020
spine01           psu2            N/A                                 ok                                             Fri Aug 21 05:54:14 2020
spine02           psu1            N/A                                 ok                                             Fri Aug 21 05:54:39 2020
spine02           psu2            N/A                                 ok                                             Fri Aug 21 05:54:39 2020
spine03           psu1            N/A                                 ok                                             Fri Aug 21 06:00:52 2020
spine03           psu2            N/A                                 ok                                             Fri Aug 21 06:00:52 2020
spine04           psu1            N/A                                 ok                                             Fri Aug 21 05:54:09 2020
spine04           psu2            N/A                                 ok                                             Fri Aug 21 05:54:09 2020
```

### View Only Power Supply Sensors

To view information from all PSU sensors or PSU sensors with a given name on your switches and host servers, run:

```
netq show sensors psu [<psu-name>] [around <text-time>] [json]
```

Use the `psu-name` option to view all PSU sensors with a particular name. Use the `around` option to view sensor information for a time in the past.

{{<notice tip>}}

Use Tab completion to determine the names of the PSUs in your switches.

```
cumulus@switch:~$ netq show sensors psu <press tab>
around  :  Go back in time to around ...
json    :  Provide output in JSON
psu1    :  Power Supply
psu2    :  Power Supply
<ENTER>
```

{{</notice>}}

This example shows information from all PSU sensors on all switches and hosts.

```
cumulus@switch:~$ netq show sensor psu

Matching sensors records:
Hostname          Name            State      Pin(W)       Pout(W)        Vin(V)       Vout(V)        Message                             Last Changed
----------------- --------------- ---------- ------------ -------------- ------------ -------------- ----------------------------------- -------------------------
border01          psu1            ok                                                                                                     Tue Aug 25 21:45:21 2020
border01          psu2            ok                                                                                                     Tue Aug 25 21:45:21 2020
border02          psu1            ok                                                                                                     Tue Aug 25 21:39:36 2020
border02          psu2            ok                                                                                                     Tue Aug 25 21:39:36 2020
fw1               psu1            ok                                                                                                     Wed Aug 26 00:08:01 2020
fw1               psu2            ok                                                                                                     Wed Aug 26 00:08:01 2020
fw2               psu1            ok                                                                                                     Wed Aug 26 00:02:13 2020
fw2               psu2            ok                                                                                                     Wed Aug 26 00:02:13 2020
leaf01            psu1            ok                                                                                                     Wed Aug 26 16:14:41 2020
leaf01            psu2            ok                                                                                                     Wed Aug 26 16:14:41 2020
leaf02            psu1            ok                                                                                                     Wed Aug 26 16:14:08 2020
leaf02            psu2            ok                                                                                                     Wed Aug 26 16:14:08 2020
leaf03            psu1            ok                                                                                                     Wed Aug 26 14:41:57 2020
leaf03            psu2            ok                                                                                                     Wed Aug 26 14:41:57 2020
leaf04            psu1            ok                                                                                                     Wed Aug 26 14:20:22 2020
leaf04            psu2            ok                                                                                                     Wed Aug 26 14:20:22 2020
spine01           psu1            ok                                                                                                     Wed Aug 26 10:53:17 2020
spine01           psu2            ok                                                                                                     Wed Aug 26 10:53:17 2020
spine02           psu1            ok                                                                                                     Wed Aug 26 10:54:07 2020
spine02           psu2            ok                                                                                                     Wed Aug 26 10:54:07 2020
spine03           psu1            ok                                                                                                     Wed Aug 26 11:00:44 2020
spine03           psu2            ok                                                                                                     Wed Aug 26 11:00:44 2020
spine04           psu1            ok                                                                                                     Wed Aug 26 10:52:00 2020
spine04           psu2            ok                                                                                                     Wed Aug 26 10:52:00 2020
```

This example shows all PSUs with the name *psu2*.

```
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
```

#### View Only Fan Sensors

To view information from all fan sensors or fan sensors with a given name on your switches and host servers, run:

```
netq show sensors fan [<fan-name>] [around <text-time>] [json]
```

Use the `around` option to view sensor information for a time in the past.

{{<notice tip>}}

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

{{</notice>}}

This example shows the state of all fans.

```
cumulus@switch:~$ netq show sensor fan

Matching sensors records:
Hostname          Name            Description                         State      Speed      Max      Min      Message                             Last Changed
----------------- --------------- ----------------------------------- ---------- ---------- -------- -------- ----------------------------------- -------------------------
border01          fan5            fan tray 3, fan 1                   ok         2500       29000    2500                                         Tue Aug 25 21:45:21 2020
border01          fan6            fan tray 3, fan 2                   ok         2500       29000    2500                                         Tue Aug 25 21:45:21 2020
border01          fan1            fan tray 1, fan 1                   ok         2500       29000    2500                                         Tue Aug 25 21:45:21 2020
border01          fan4            fan tray 2, fan 2                   ok         2500       29000    2500                                         Tue Aug 25 21:45:21 2020
border01          psu1fan1        psu1 fan                            ok         2500       29000    2500                                         Tue Aug 25 21:45:21 2020
border01          fan3            fan tray 2, fan 1                   ok         2500       29000    2500                                         Tue Aug 25 21:45:21 2020
border01          fan2            fan tray 1, fan 2                   ok         2500       29000    2500                                         Tue Aug 25 21:45:21 2020
border01          psu2fan1        psu2 fan                            ok         2500       29000    2500                                         Tue Aug 25 21:45:21 2020
border02          fan2            fan tray 1, fan 2                   ok         2500       29000    2500                                         Tue Aug 25 21:39:36 2020
border02          psu2fan1        psu2 fan                            ok         2500       29000    2500                                         Tue Aug 25 21:39:36 2020
border02          psu1fan1        psu1 fan                            ok         2500       29000    2500                                         Tue Aug 25 21:39:36 2020
border02          fan4            fan tray 2, fan 2                   ok         2500       29000    2500                                         Tue Aug 25 21:39:36 2020
border02          fan1            fan tray 1, fan 1                   ok         2500       29000    2500                                         Tue Aug 25 21:39:36 2020
border02          fan6            fan tray 3, fan 2                   ok         2500       29000    2500                                         Tue Aug 25 21:39:36 2020
border02          fan5            fan tray 3, fan 1                   ok         2500       29000    2500                                         Tue Aug 25 21:39:36 2020
border02          fan3            fan tray 2, fan 1                   ok         2500       29000    2500                                         Tue Aug 25 21:39:36 2020
fw1               fan2            fan tray 1, fan 2                   ok         2500       29000    2500                                         Wed Aug 26 00:08:01 2020
fw1               fan5            fan tray 3, fan 1                   ok         2500       29000    2500                                         Wed Aug 26 00:08:01 2020
fw1               psu1fan1        psu1 fan                            ok         2500       29000    2500                                         Wed Aug 26 00:08:01 2020
fw1               fan4            fan tray 2, fan 2                   ok         2500       29000    2500                                         Wed Aug 26 00:08:01 2020
fw1               fan3            fan tray 2, fan 1                   ok         2500       29000    2500                                         Wed Aug 26 00:08:01 2020
fw1               psu2fan1        psu2 fan                            ok         2500       29000    2500                                         Wed Aug 26 00:08:01 2020
fw1               fan6            fan tray 3, fan 2                   ok         2500       29000    2500                                         Wed Aug 26 00:08:01 2020
fw1               fan1            fan tray 1, fan 1                   ok         2500       29000    2500                                         Wed Aug 26 00:08:01 2020
fw2               fan3            fan tray 2, fan 1                   ok         2500       29000    2500                                         Wed Aug 26 00:02:13 2020
fw2               psu2fan1        psu2 fan                            ok         2500       29000    2500                                         Wed Aug 26 00:02:13 2020
fw2               fan2            fan tray 1, fan 2                   ok         2500       29000    2500                                         Wed Aug 26 00:02:13 2020
fw2               fan6            fan tray 3, fan 2                   ok         2500       29000    2500                                         Wed Aug 26 00:02:13 2020
fw2               fan1            fan tray 1, fan 1                   ok         2500       29000    2500                                         Wed Aug 26 00:02:13 2020
fw2               fan4            fan tray 2, fan 2                   ok         2500       29000    2500                                         Wed Aug 26 00:02:13 2020
fw2               fan5            fan tray 3, fan 1                   ok         2500       29000    2500                                         Wed Aug 26 00:02:13 2020
fw2               psu1fan1        psu1 fan                            ok         2500       29000    2500                                         Wed Aug 26 00:02:13 2020
leaf01            psu2fan1        psu2 fan                            ok         2500       29000    2500                                         Wed Aug 26 16:14:41 2020
leaf01            fan5            fan tray 3, fan 1                   ok         2500       29000    2500                                         Wed Aug 26 16:14:41 2020
leaf01            fan3            fan tray 2, fan 1                   ok         2500       29000    2500                                         Wed Aug 26 16:14:41 2020
leaf01            fan1            fan tray 1, fan 1                   ok         2500       29000    2500                                         Wed Aug 26 16:14:41 2020
leaf01            fan6            fan tray 3, fan 2                   ok         2500       29000    2500                                         Wed Aug 26 16:14:41 2020
leaf01            fan2            fan tray 1, fan 2                   ok         2500       29000    2500                                         Wed Aug 26 16:14:41 2020
leaf01            psu1fan1        psu1 fan                            ok         2500       29000    2500                                         Wed Aug 26 16:14:41 2020
leaf01            fan4            fan tray 2, fan 2                   ok         2500       29000    2500                                         Wed Aug 26 16:14:41 2020
leaf02            fan3            fan tray 2, fan 1                   ok         2500       29000    2500                                         Wed Aug 26 16:14:08 2020
...
spine04           fan4            fan tray 2, fan 2                   ok         2500       29000    2500                                         Wed Aug 26 10:52:00 2020
spine04           psu1fan1        psu1 fan                            ok         2500       29000    2500                                         Wed Aug 26 10:52:00 2020
```

This example shows the state of all fans with the name *fan1*.

```
cumulus@switch~$ netq show sensors fan fan1
Matching sensors records:
Hostname          Name            Description                         State      Speed      Max      Min      Message                             Last Changed
----------------- --------------- ----------------------------------- ---------- ---------- -------- -------- ----------------------------------- -------------------------
border01          fan1            fan tray 1, fan 1                   ok         2500       29000    2500                                         Tue Aug 25 21:45:21 2020
border02          fan1            fan tray 1, fan 1                   ok         2500       29000    2500                                         Tue Aug 25 21:39:36 2020
fw1               fan1            fan tray 1, fan 1                   ok         2500       29000    2500                                         Wed Aug 26 00:08:01 2020
fw2               fan1            fan tray 1, fan 1                   ok         2500       29000    2500                                         Wed Aug 26 00:02:13 2020
leaf01            fan1            fan tray 1, fan 1                   ok         2500       29000    2500                                         Tue Aug 25 18:30:07 2020
leaf02            fan1            fan tray 1, fan 1                   ok         2500       29000    2500                                         Tue Aug 25 18:08:38 2020
leaf03            fan1            fan tray 1, fan 1                   ok         2500       29000    2500                                         Tue Aug 25 21:20:34 2020
leaf04            fan1            fan tray 1, fan 1                   ok         2500       29000    2500                                         Wed Aug 26 14:20:22 2020
spine01           fan1            fan tray 1, fan 1                   ok         2500       29000    2500                                         Wed Aug 26 10:53:17 2020
spine02           fan1            fan tray 1, fan 1                   ok         2500       29000    2500                                         Wed Aug 26 10:54:07 2020
spine03           fan1            fan tray 1, fan 1                   ok         2500       29000    2500                                         Wed Aug 26 11:00:44 2020
spine04           fan1            fan tray 1, fan 1                   ok         2500       29000    2500                                         Wed Aug 26 10:52:00 2020

```

#### View Only Temperature Sensors

To view information from all temperature sensors or temperature sensors with a given name on your switches and host servers, run:

```
netq show sensors temp [<temp-name>] [around <text-time>] [json]
```

Use the `around` option to view sensor information for a time in the past.

{{<notice tip>}}

Use tab completion to determine the names of the temperature sensors on your devices:

```
cumulus@switch:~$ netq show sensors temp <press tab>
    around     :  Go back in time to around ...
    json       :  Provide output in JSON
    psu1temp1  :  Temp Name
    psu2temp1  :  Temp Name
    temp1      :  Temp Name
    temp2      :  Temp Name
    temp3      :  Temp Name
    temp4      :  Temp Name
    temp5      :  Temp Name
    <ENTER>
```

{{</notice>}}

This example shows the state of all temperature sensors.

```
cumulus@switch:~$ netq show sensor temp

Matching sensors records:
Hostname          Name            Description                         State      Temp     Critical Max      Min      Message                             Last Changed
----------------- --------------- ----------------------------------- ---------- -------- -------- -------- -------- ----------------------------------- -------------------------
border01          psu1temp1       psu1 temp sensor                    ok         25       85       80       5                                            Tue Aug 25 21:45:21 2020
border01          temp2           board sensor near virtual switch    ok         25       85       80       5                                            Tue Aug 25 21:45:21 2020
border01          temp3           board sensor at front left corner   ok         25       85       80       5                                            Tue Aug 25 21:45:21 2020
border01          temp1           board sensor near cpu               ok         25       85       80       5                                            Tue Aug 25 21:45:21 2020
border01          temp4           board sensor at front right corner  ok         25       85       80       5                                            Tue Aug 25 21:45:21 2020
border01          psu2temp1       psu2 temp sensor                    ok         25       85       80       5                                            Tue Aug 25 21:45:21 2020
border01          temp5           board sensor near fan               ok         25       85       80       5                                            Tue Aug 25 21:45:21 2020
border02          temp1           board sensor near cpu               ok         25       85       80       5                                            Tue Aug 25 21:39:36 2020
border02          temp5           board sensor near fan               ok         25       85       80       5                                            Tue Aug 25 21:39:36 2020
border02          temp3           board sensor at front left corner   ok         25       85       80       5                                            Tue Aug 25 21:39:36 2020
border02          temp4           board sensor at front right corner  ok         25       85       80       5                                            Tue Aug 25 21:39:36 2020
border02          psu2temp1       psu2 temp sensor                    ok         25       85       80       5                                            Tue Aug 25 21:39:36 2020
border02          psu1temp1       psu1 temp sensor                    ok         25       85       80       5                                            Tue Aug 25 21:39:36 2020
border02          temp2           board sensor near virtual switch    ok         25       85       80       5                                            Tue Aug 25 21:39:36 2020
fw1               temp4           board sensor at front right corner  ok         25       85       80       5                                            Wed Aug 26 00:08:01 2020
fw1               temp3           board sensor at front left corner   ok         25       85       80       5                                            Wed Aug 26 00:08:01 2020
fw1               psu1temp1       psu1 temp sensor                    ok         25       85       80       5                                            Wed Aug 26 00:08:01 2020
fw1               temp1           board sensor near cpu               ok         25       85       80       5                                            Wed Aug 26 00:08:01 2020
fw1               temp2           board sensor near virtual switch    ok         25       85       80       5                                            Wed Aug 26 00:08:01 2020
fw1               temp5           board sensor near fan               ok         25       85       80       5                                            Wed Aug 26 00:08:01 2020
fw1               psu2temp1       psu2 temp sensor                    ok         25       85       80       5                                            Wed Aug 26 00:08:01 2020
fw2               temp5           board sensor near fan               ok         25       85       80       5                                            Wed Aug 26 00:02:13 2020
fw2               temp2           board sensor near virtual switch    ok         25       85       80       5                                            Wed Aug 26 00:02:13 2020
fw2               psu2temp1       psu2 temp sensor                    ok         25       85       80       5                                            Wed Aug 26 00:02:13 2020
fw2               temp3           board sensor at front left corner   ok         25       85       80       5                                            Wed Aug 26 00:02:13 2020
fw2               temp4           board sensor at front right corner  ok         25       85       80       5                                            Wed Aug 26 00:02:13 2020
fw2               temp1           board sensor near cpu               ok         25       85       80       5                                            Wed Aug 26 00:02:13 2020
fw2               psu1temp1       psu1 temp sensor                    ok         25       85       80       5                                            Wed Aug 26 00:02:13 2020
leaf01            psu1temp1       psu1 temp sensor                    ok         25       85       80       5                                            Wed Aug 26 16:14:41 2020
leaf01            temp5           board sensor near fan               ok         25       85       80       5                                            Wed Aug 26 16:14:41 2020
leaf01            temp4           board sensor at front right corner  ok         25       85       80       5                                            Wed Aug 26 16:14:41 2020
leaf01            temp1           board sensor near cpu               ok         25       85       80       5                                            Wed Aug 26 16:14:41 2020
leaf01            temp2           board sensor near virtual switch    ok         25       85       80       5                                            Wed Aug 26 16:14:41 2020
leaf01            temp3           board sensor at front left corner   ok         25       85       80       5                                            Wed Aug 26 16:14:41 2020
leaf01            psu2temp1       psu2 temp sensor                    ok         25       85       80       5                                            Wed Aug 26 16:14:41 2020
leaf02            temp5           board sensor near fan               ok         25       85       80       5                                            Wed Aug 26 16:14:08 2020
...
spine04           psu2temp1       psu2 temp sensor                    ok         25       85       80       5                                            Wed Aug 26 10:52:00 2020
spine04           temp5           board sensor near fan               ok         25       85       80       5                                            Wed Aug 26 10:52:00 2020
```

This example shows the state of all temperature sensors with the name *psu2temp1*.

```
cumulus@switch:~$ netq show sensors temp psu2temp1
Matching sensors records:
Hostname          Name            Description                         State      Temp     Critical Max      Min      Message                             Last Changed
----------------- --------------- ----------------------------------- ---------- -------- -------- -------- -------- ----------------------------------- -------------------------
border01          psu2temp1       psu2 temp sensor                    ok         25       85       80       5                                            Tue Aug 25 21:45:21 2020
border02          psu2temp1       psu2 temp sensor                    ok         25       85       80       5                                            Tue Aug 25 21:39:36 2020
fw1               psu2temp1       psu2 temp sensor                    ok         25       85       80       5                                            Wed Aug 26 00:08:01 2020
fw2               psu2temp1       psu2 temp sensor                    ok         25       85       80       5                                            Wed Aug 26 00:02:13 2020
leaf01            psu2temp1       psu2 temp sensor                    ok         25       85       80       5                                            Tue Aug 25 18:30:07 2020
leaf02            psu2temp1       psu2 temp sensor                    ok         25       85       80       5                                            Tue Aug 25 18:08:38 2020
leaf03            psu2temp1       psu2 temp sensor                    ok         25       85       80       5                                            Tue Aug 25 21:20:34 2020
leaf04            psu2temp1       psu2 temp sensor                    ok         25       85       80       5                                            Wed Aug 26 14:20:22 2020
spine01           psu2temp1       psu2 temp sensor                    ok         25       85       80       5                                            Wed Aug 26 10:53:17 2020
spine02           psu2temp1       psu2 temp sensor                    ok         25       85       80       5                                            Wed Aug 26 10:54:07 2020
spine03           psu2temp1       psu2 temp sensor                    ok         25       85       80       5                                            Wed Aug 26 11:00:44 2020
spine04           psu2temp1       psu2 temp sensor                    ok         25       85       80       5                                            Wed Aug 26 10:52:00 2020
```

{{</tab>}}

{{</tabs>}}

### View Digital Optics Information

{{<tabs "TabID1227" >}}

{{<tab "NetQ UI" >}}

Use the filter option to view laser power and bias current for a given interface and channel on a switch, and temperature and voltage for a given module. Select the relevant tab to view the data.

1. Click <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/03-Menu/navigation-menu.svg" height="18" width="18"/> Menu, then click **Digital Optics**.

2. The **Laser Rx Power** tab is displayed by default.

    {{<figure src="/images/netq/main-menu-ntwk-dom-laserrx-power-310.png" width="700">}}

<div style="padding-left: 18px;">
<table>
<thead>
<tr>
<th>Laser Parameter</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>Hostname</td>
<td>Name of the switch or host where the digital optics module resides</td>
</tr>
<tr>
<td>Timestamp</td>
<td>Date and time the data was captured</td>
</tr>
<tr>
<td>If Name</td>
<td>Name of interface where the digital optics module is installed</td>
</tr>
<tr>
<td>Units</td>
<td>Measurement unit for the power (mW) or current (mA)</td>
</tr>
<tr>
<td>Channel 1&ndash;8</td>
<td>Value of the power or current on each channel where the digital optics module is transmitting</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th>Module Parameter</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>Hostname</td>
<td>Name of the switch or host where the digital optics module resides</td>
</tr>
<tr>
<td>Timestamp</td>
<td>Date and time the data was captured</td>
</tr>
<tr>
<td>If Name</td>
<td>Name of interface where the digital optics module is installed</td>
</tr>
<tr>
<td>Degree C</td>
<td>Current module temperature, measured in degrees Celsius</td>
</tr>
<tr>
<td>Degree F</td>
<td>Current module temperature, measured in degrees Fahrenheit</td>
</tr>
<tr>
<td>Units</td>
<td>Measurement unit for module voltage; Volts</td>
</tr>
<tr>
<td>Value</td>
<td>Current module voltage</td>
</tr>
</tbody>
</table>
</div>

3. Click each of the other Laser or Module tabs to view that information for all devices.

{{</tab>}}

{{<tab "NetQ CLI" >}}

To view digital optics information for your switches and host servers, run one of the following:

```
netq show dom type (laser_rx_power|laser_output_power|laser_bias_current) [interface <text-dom-port-anchor>] [channel_id <text-channel-id>] [around <text-time>] [json]
netq show dom type (module_temperature|module_voltage) [interface <text-dom-port-anchor>] [around <text-time>] [json]
```

This example shows module temperature information for all devices.

```
cumulus@switch:~$ netq show dom type module_temperature
Matching dom records:
Hostname          Interface  type                 high_alarm_threshold low_alarm_threshold  high_warning_thresho low_warning_threshol value                Last Updated
                                                                                            ld                   d
----------------- ---------- -------------------- -------------------- -------------------- -------------------- -------------------- -------------------- ------------------------
...
spine01           swp53s0    module_temperature   {‘degree_c’: 85,     {‘degree_c’: -10,    {‘degree_c’: 70,     {‘degree_c’: 0,      {‘degree_c’: 32,     Wed Jul  1 15:25:56 2020
                                                  ‘degree_f’: 185}     ‘degree_f’: 14}      ‘degree_f’: 158}     ‘degree_f’: 32}      ‘degree_f’: 89.6}
spine01           swp35      module_temperature   {‘degree_c’: 75,     {‘degree_c’: -5,     {‘degree_c’: 70,     {‘degree_c’: 0,      {‘degree_c’: 27.82,  Wed Jul  1 15:25:56 2020
                                                  ‘degree_f’: 167}     ‘degree_f’: 23}      ‘degree_f’: 158}     ‘degree_f’: 32}      ‘degree_f’: 82.08}
spine01           swp55      module_temperature   {‘degree_c’: 75,     {‘degree_c’: -5,     {‘degree_c’: 70,     {‘degree_c’: 0,      {‘degree_c’: 26.29,  Wed Jul  1 15:25:56 2020
                                                  ‘degree_f’: 167}     ‘degree_f’: 23}      ‘degree_f’: 158}     ‘degree_f’: 32}      ‘degree_f’: 79.32}
spine01           swp9       module_temperature   {‘degree_c’: 78,     {‘degree_c’: -13,    {‘degree_c’: 73,     {‘degree_c’: -8,     {‘degree_c’: 25.57,  Wed Jul  1 15:25:56 2020
                                                  ‘degree_f’: 172.4}   ‘degree_f’: 8.6}     ‘degree_f’: 163.4}   ‘degree_f’: 17.6}    ‘degree_f’: 78.02}
spine01           swp56      module_temperature   {‘degree_c’: 78,     {‘degree_c’: -10,    {‘degree_c’: 75,     {‘degree_c’: -5,     {‘degree_c’: 29.43,  Wed Jul  1 15:25:56 2020
                                                  ‘degree_f’: 172.4}   ‘degree_f’: 14}      ‘degree_f’: 167}     ‘degree_f’: 23}      ‘degree_f’: 84.97}
...
```

{{</tab>}}

{{</tabs>}}

## View Software Inventory across the Network

You can view software components deployed on all switches and hosts, or on all the switches in your network.

### View the Operating Systems Information

{{<tabs "TabID1079" >}}

{{<tab "Inventory/Devices" >}}

1. Locate the medium Inventory/Devices card on your workbench.

    {{<figure src="/images/netq/inventory-devices-medium-320.png" width="200">}}

2. Hover over the pie charts to view the total number of devices with a given operating system installed.

    {{<figure src="/images/netq/inventory-devices-medium-hover-tip-320.png" width="200">}}

3. Change to the large card using the size picker.

4. Hover over a segment in the OS distribution chart to view the total number of devices with a given operating system installed.

    Note that sympathetic highlighting (in blue) is employed to show which versions of the other switch components are associated with this OS.

    {{<figure src="/images/netq/inventory-devices-large-switches-tab-component-highlight2-230.png" width="500">}}

5. Click on a segment in OS distribution chart.

6. Click *Filter OS* at the top of the popup.

    {{<figure src="/images/netq/inventory-devices-large-switches-tab-component-filter-os-320.png" width="350">}}

7. The card updates to show only the components associated with switches running the selected OS. To return to all OSs, click X in the OS tag to remove the filter.

    {{<figure src="/images/netq/inventory-devices-large-switches-tab-filter-results-320.png" width="500">}}

8. Change to the full-screen card using the size picker.

    {{<figure src="/images/netq/inventory-devices-fullscr-allswitches-tab-320.png" width="700">}}

9. The **All Switches** tab is selected by default. Scroll to the right to locate all of the OS parameter data.

10. Click **All Hosts** to view the OS parameters for all host servers.

    {{<figure src="/images/netq/inventory-devices-fullscr-allhosts-tab-320.png" width="700" >}}

{{</tab>}}

{{<tab "netq show inventory" >}}

To view OS information for your switches and host servers, run:

```
netq show inventory os [version <os-version>|name <os-name>] [json]
```

This example shows the OS information for all devices.

```
cumulus@switch:~$ netq show inventory os
Matching inventory records:
Hostname          Name            Version                              Last Changed
----------------- --------------- ------------------------------------ -------------------------
border01          CL              3.7.13                               Tue Jul 28 18:49:46 2020
border02          CL              3.7.13                               Tue Jul 28 18:44:42 2020
fw1               CL              3.7.13                               Tue Jul 28 19:14:27 2020
fw2               CL              3.7.13                               Tue Jul 28 19:12:50 2020
leaf01            CL              3.7.13                               Wed Jul 29 16:12:20 2020
leaf02            CL              3.7.13                               Wed Jul 29 16:12:21 2020
leaf03            CL              3.7.13                               Tue Jul 14 21:18:21 2020
leaf04            CL              3.7.13                               Tue Jul 14 20:58:47 2020
oob-mgmt-server   Ubuntu          18.04                                Mon Jul 13 21:01:35 2020
server01          Ubuntu          18.04                                Mon Jul 13 22:09:18 2020
server02          Ubuntu          18.04                                Mon Jul 13 22:09:18 2020
server03          Ubuntu          18.04                                Mon Jul 13 22:09:20 2020
server04          Ubuntu          18.04                                Mon Jul 13 22:09:20 2020
server05          Ubuntu          18.04                                Mon Jul 13 22:09:20 2020
server06          Ubuntu          18.04                                Mon Jul 13 22:09:21 2020
server07          Ubuntu          18.04                                Mon Jul 13 22:09:21 2020
server08          Ubuntu          18.04                                Mon Jul 13 22:09:22 2020
spine01           CL              3.7.12                               Mon Aug 10 19:55:06 2020
spine02           CL              3.7.12                               Mon Aug 10 19:55:07 2020
spine03           CL              3.7.12                               Mon Aug 10 19:55:09 2020
spine04           CL              3.7.12                               Mon Aug 10 19:55:08 2020
```

You can filter the results of the command to view only devices with a particular operating system or version. This can be especially helpful when you suspect that a particular device upgrade did not work as expected.

This example shows all devices with the Cumulus Linux version 3.7.12 installed.

```
cumulus@switch:~$ netq show inventory os version 3.7.12

Matching inventory records:
Hostname          Name            Version                              Last Changed
----------------- --------------- ------------------------------------ -------------------------
spine01           CL              3.7.12                               Mon Aug 10 19:55:06 2020
spine02           CL              3.7.12                               Mon Aug 10 19:55:07 2020
spine03           CL              3.7.12                               Mon Aug 10 19:55:09 2020
spine04           CL              3.7.12                               Mon Aug 10 19:55:08 2020
```

{{</tab>}}

{{</tabs>}}

### View the Supported Cumulus Linux Packages

When you are troubleshooting an issue with a switch, you might want to know all the supported versions of the Cumulus Linux operating system that are available for that switch and on a switch that is not having the same issue.

To view package information for your switches, run:

```
netq show cl-manifest [json]
```

This example shows the OS packages supported for all switches.

```
cumulus@switch:~$ netq show cl-manifest

Matching manifest records:
Hostname          ASIC Vendor          CPU Arch             Manifest Version
----------------- -------------------- -------------------- --------------------
border01          vx                   x86_64               3.7.6.1
border01          vx                   x86_64               3.7.10
border01          vx                   x86_64               3.7.11
border01          vx                   x86_64               3.6.2.1
...
fw1               vx                   x86_64               3.7.6.1
fw1               vx                   x86_64               3.7.10
fw1               vx                   x86_64               3.7.11
fw1               vx                   x86_64               3.6.2.1
...
leaf01            vx                   x86_64               4.1.0
leaf01            vx                   x86_64               4.0.0
leaf01            vx                   x86_64               3.6.2
leaf01            vx                   x86_64               3.7.2
...
leaf02            vx                   x86_64               3.7.6.1
leaf02            vx                   x86_64               3.7.10
leaf02            vx                   x86_64               3.7.11
leaf02            vx                   x86_64               3.6.2.1
...
```

### View All Software Packages Installed

If you are having an issue with several switches, you should verify all the packages installed on them and compare that to the recommended packages for a given Cumulus Linux release.

To view installed package information for your switches, run:

```
netq show cl-pkg-info [<text-package-name>] [around <text-time>] [json]
```

Use the `text-package-name` option to narrow the results to a particular package or the `around` option to narrow the output to a particular time range.

This example shows all installed software packages for all devices.

```
cumulus@switch:~$ netq show cl-pkg-info
Matching package_info records:
Hostname          Package Name             Version              CL Version           Package Status       Last Changed
----------------- ------------------------ -------------------- -------------------- -------------------- -------------------------
border01          libcryptsetup4           2:1.6.6-5            Cumulus Linux 3.7.13 installed            Mon Aug 17 18:53:50 2020
border01          libedit2                 3.1-20140620-2       Cumulus Linux 3.7.13 installed            Mon Aug 17 18:53:50 2020
border01          libffi6                  3.1-2+deb8u1         Cumulus Linux 3.7.13 installed            Mon Aug 17 18:53:50 2020
...
border02          libdb5.3                 9999-cl3u2           Cumulus Linux 3.7.13 installed            Mon Aug 17 18:48:53 2020
border02          libnl-cli-3-200          3.2.27-cl3u15+1      Cumulus Linux 3.7.13 installed            Mon Aug 17 18:48:53 2020
border02          pkg-config               0.28-1               Cumulus Linux 3.7.13 installed            Mon Aug 17 18:48:53 2020
border02          libjs-sphinxdoc          1.2.3+dfsg-1         Cumulus Linux 3.7.13 installed            Mon Aug 17 18:48:53 2020
...
fw1               libpcap0.8               1.8.1-3~bpo8+1       Cumulus Linux 3.7.13 installed            Mon Aug 17 19:18:57 2020
fw1               python-eventlet          0.13.0-2             Cumulus Linux 3.7.13 installed            Mon Aug 17 19:18:57 2020
fw1               libapt-pkg4.12           1.0.9.8.5-cl3u2      Cumulus Linux 3.7.13 installed            Mon Aug 17 19:18:57 2020
fw1               libopts25                1:5.18.4-3           Cumulus Linux 3.7.13 installed            Mon Aug 17 19:18:57 2020
...
```

This example shows the installed *switchd* package version.

```
cumulus@switch:~$ netq spine01 show cl-pkg-info switchd

Matching package_info records:
Hostname          Package Name             Version              CL Version           Package Status       Last Changed
----------------- ------------------------ -------------------- -------------------- -------------------- -------------------------
spine01           switchd                  1.0-cl3u40           Cumulus Linux 3.7.12 installed            Thu Aug 27 01:58:47 2020

```

### View Recommended Software Packages

You can determine whether any of your switches are using a software package other than the default package associated with the Cumulus Linux release that is running on the switches. Use this list to determine which packages to install/upgrade on all devices. Additionally, you can determine if a software package is missing.

To view recommended package information for your switches, run:

```
netq show recommended-pkg-version [release-id <text-release-id>] [package-name <text-package-name>] [json]
```

{{<notice tip>}}
The output can be rather lengthy if you run this command for all releases and packages. If desired, run the command using the <code>release-id</code> and/or <code>package-name</code> options to shorten the output.
{{</notice>}}

This example looks for switches running Cumulus Linux 3.7.1 and `switchd`. The result is a single switch, *leaf12*, that has older software and should get an update.

```
cumulus@switch:~$ netq show recommended-pkg-version release-id 3.7.1 package-name switchd
Matching manifest records:
Hostname          Release ID           ASIC Vendor          CPU Arch             Package Name         Version              Last Changed
----------------- -------------------- -------------------- -------------------- -------------------- -------------------- -------------------------
leaf12            3.7.1                vx                   x86_64               switchd              1.0-cl3u30           Wed Feb  5 04:36:30 2020
```

This example looks for switches running Cumulus Linux 3.7.1 and `ptmd`. The result is a single switch, *server01*, that has older software and should get an update.

```
cumulus@switch:~$ netq show recommended-pkg-version release-id 3.7.1 package-name ptmd
Matching manifest records:
Hostname          Release ID           ASIC Vendor          CPU Arch             Package Name         Version              Last Changed
----------------- -------------------- -------------------- -------------------- -------------------- -------------------- -------------------------
server01            3.7.1                vx                   x86_64               ptmd                 3.0-2-cl3u8          Wed Feb  5 04:36:30 2020
```

This example looks for switches running Cumulus Linux 3.7.1 and `lldpd`. The result is a single switch, *server01*, that has older software and should get an update.

```
cumulus@switch:~$ netq show recommended-pkg-version release-id 3.7.1 package-name lldpd
Matching manifest records:
Hostname          Release ID           ASIC Vendor          CPU Arch             Package Name         Version              Last Changed
----------------- -------------------- -------------------- -------------------- -------------------- -------------------- -------------------------
server01            3.7.1                vx                   x86_64               lldpd                0.9.8-0-cl3u11       Wed Feb  5 04:36:30 2020
```

This example looks for switches running Cumulus Linux 3.6.2 and `switchd`. The result is a single switch, *leaf04*, that has older software and should get an update.

```
cumulus@noc-pr:~$ netq show recommended-pkg-version release-id 3.6.2 package-name switchd
Matching manifest records:
Hostname          Release ID           ASIC Vendor          CPU Arch             Package Name         Version              Last Changed
----------------- -------------------- -------------------- -------------------- -------------------- -------------------- -------------------------
leaf04            3.6.2                vx                   x86_64               switchd              1.0-cl3u27           Wed Feb  5 04:36:30 2020
```


### View ACL Resources

Using the NetQ CLI, you can monitor the incoming and outgoing access control lists (ACLs) configured on all switches, currently or at a time in the past.

To view ACL resources for all your switches, run:

```
netq show cl-resource acl [ingress | egress] [around <text-time>] [json]
```

Use the `egress` or `ingress` options to show only the outgoing or incoming ACLs. Use the `around` option to show this information for a time in the past.

This example shows the ACL resources for all configured switches:

```
cumulus@switch:~$ netq show cl-resource acl
Matching cl_resource records:
Hostname          In IPv4 filter       In IPv4 Mangle       In IPv6 filter       In IPv6 Mangle       In 8021x filter      In Mirror            In PBR IPv4 filter   In PBR IPv6 filter   Eg IPv4 filter       Eg IPv4 Mangle       Eg IPv6 filter       Eg IPv6 Mangle       ACL Regions          18B Rules Key        32B Rules Key        54B Rules Key        L4 Port range Checke Last Updated
                                                                                                                                                                                                                                                                                                                                                                  rs
----------------- -------------------- -------------------- -------------------- -------------------- -------------------- -------------------- -------------------- -------------------- -------------------- -------------------- -------------------- -------------------- -------------------- -------------------- -------------------- -------------------- -------------------- ------------------------
act-5712-09       40,512(7%)           0,0(0%)              30,768(3%)           0,0(0%)              0,0(0%)              0,0(0%)              0,0(0%)              0,0(0%)              32,256(12%)          0,0(0%)              0,0(0%)              0,0(0%)              0,0(0%)              0,0(0%)              0,0(0%)              0,0(0%)              2,24(8%)             Tue Aug 18 20:20:39 2020
mlx-2700-04       0,0(0%)              0,0(0%)              0,0(0%)              0,0(0%)              0,0(0%)              0,0(0%)              0,0(0%)              0,0(0%)              0,0(0%)              0,0(0%)              0,0(0%)              0,0(0%)              4,400(1%)            2,2256(0%)           0,1024(0%)           2,1024(0%)           0,0(0%)              Tue Aug 18 20:19:08 2020
```

### View Forwarding Resources

With the NetQ CLI, you can monitor the amount of forwarding resources used by all devices, currently or at a time in the past.

To view forwarding resources for all your switches, run:

```
netq show cl-resource forwarding [around <text-time>] [json]
```

Use the `around` option to show this information for a time in the past.

This example shows forwarding resources for all configured switches:

```
cumulus@noc-pr:~$ netq show cl-resource forwarding
Matching cl_resource records:
Hostname          IPv4 host entries    IPv6 host entries    IPv4 route entries   IPv6 route entries   ECMP nexthops        MAC entries          Total Mcast Routes   Last Updated
----------------- -------------------- -------------------- -------------------- -------------------- -------------------- -------------------- -------------------- ------------------------
act-5712-09       0,16384(0%)          0,0(0%)              0,131072(0%)         23,20480(0%)         0,16330(0%)          0,32768(0%)          0,8192(0%)           Tue Aug 18 20:20:39 2020
mlx-2700-04       0,32768(0%)          0,16384(0%)          0,65536(0%)          4,28672(0%)          0,4101(0%)           0,40960(0%)          0,1000(0%)           Tue Aug 18 20:19:08 2020
```

### View NetQ Agents

{{<tabs "TabID1549" >}}

{{<tab "Agents List" >}}

To view the NetQ Agents on all switches and hosts:

1. Click <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/03-Menu/navigation-menu.svg" height="18" width="18"/> to open the Main menu.

2. Select **Agents** from the **Network** column.

3. View the **Version** column to determine which release of the NetQ Agent is running on your devices. Ideally, this version should be the same as the NetQ release you are running, and is the same across all your devices.

    {{<figure src="/images/netq/main-menu-ntwk-agents-310.png" width="700">}}

<div style="padding-left: 18px;"><table>
<thead>
<tr>
<th>Parameter</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>Hostname</td>
<td>Name of the switch or host</td>
</tr>
<tr>
<td>Timestamp</td>
<td>Date and time the data was captured</td>
</tr>
<tr>
<td>Last Reinit</td>
<td>Date and time that the switch or host was reinitialized</td>
</tr>
<tr>
<td>Last Update Time</td>
<td>Date and time that the switch or host was updated</td>
</tr>
<tr>
<td>Lastboot</td>
<td>Date and time that the switch or host was last booted up</td>
</tr>
<tr>
<td>NTP State</td>
<td>Status of NTP synchronization on the switch or host; yes = in synchronization, no = out of synchronization</td>
</tr>
<tr>
<td>Sys Uptime</td>
<td>Amount of time the switch or host has been continuously up and running</td>
</tr>
<tr>
<td>Version</td>
<td>NetQ version running on the switch or host</td>
</tr>
</tbody>
</table>
</div>

{{</tab>}}

{{<tab "netq show agents" >}}

To view the NetQ Agents on all switches and hosts, run:

```
netq show agents [fresh | rotten ] [around <text-time>] [json]
```

Use the `fresh` keyword to view only the NetQ Agents that are in current communication with the NetQ Platform or NetQ Collector. Use the `rotten` keyword to view those that are not. Use the `around` keyword to view the state of NetQ Agents at an earlier time.

This example shows the current NetQ Agent state on all devices. The **Status** column indicates whether the agent is up and current, labelled *Fresh*, or down and stale, labelled *Rotten*. Additional information includes the agent status &mdash; whether it is time synchronized, how long it has been up, and the last time its state changed. You can also see the version running. Ideally, this version should be the same as the NetQ release you are running, and is the same across all your devices.

```
cumulus@switch:~$ netq show agents
Matching agents records:
Hostname          Status           NTP Sync Version                              Sys Uptime                Agent Uptime              Reinitialize Time          Last Changed
----------------- ---------------- -------- ------------------------------------ ------------------------- ------------------------- -------------------------- -------------------------
border01          Fresh            yes      3.1.0-cl3u28~1594095615.8f00ba1      Tue Jul 28 18:48:31 2020  Tue Jul 28 18:49:46 2020  Tue Jul 28 18:49:46 2020   Sun Aug 23 18:56:56 2020
border02          Fresh            yes      3.1.0-cl3u28~1594095615.8f00ba1      Tue Jul 28 18:43:29 2020  Tue Jul 28 18:44:42 2020  Tue Jul 28 18:44:42 2020   Sun Aug 23 18:49:57 2020
fw1               Fresh            yes      3.1.0-cl3u28~1594095615.8f00ba1      Tue Jul 28 19:13:26 2020  Tue Jul 28 19:14:28 2020  Tue Jul 28 19:14:28 2020   Sun Aug 23 19:24:01 2020
fw2               Fresh            yes      3.1.0-cl3u28~1594095615.8f00ba1      Tue Jul 28 19:11:27 2020  Tue Jul 28 19:12:51 2020  Tue Jul 28 19:12:51 2020   Sun Aug 23 19:21:13 2020
leaf01            Fresh            yes      3.1.0-cl3u28~1594095615.8f00ba1      Tue Jul 14 21:04:03 2020  Wed Jul 29 16:12:22 2020  Wed Jul 29 16:12:22 2020   Sun Aug 23 16:16:09 2020
leaf02            Fresh            yes      3.1.0-cl3u28~1594095615.8f00ba1      Tue Jul 14 20:59:10 2020  Wed Jul 29 16:12:23 2020  Wed Jul 29 16:12:23 2020   Sun Aug 23 16:16:48 2020
leaf03            Fresh            yes      3.1.0-cl3u28~1594095615.8f00ba1      Tue Jul 14 21:04:03 2020  Tue Jul 14 21:18:23 2020  Tue Jul 14 21:18:23 2020   Sun Aug 23 21:25:16 2020
leaf04            Fresh            yes      3.1.0-cl3u28~1594095615.8f00ba1      Tue Jul 14 20:57:30 2020  Tue Jul 14 20:58:48 2020  Tue Jul 14 20:58:48 2020   Sun Aug 23 21:09:06 2020
oob-mgmt-server   Fresh            yes      3.1.0-ub18.04u28~1594095612.8f00ba1  Mon Jul 13 17:07:59 2020  Mon Jul 13 21:01:35 2020  Tue Jul 14 19:36:19 2020   Sun Aug 23 15:45:05 2020
server01          Fresh            yes      3.1.0-ub18.04u28~1594095612.8f00ba1  Mon Jul 13 18:30:46 2020  Mon Jul 13 22:09:19 2020  Tue Jul 14 19:36:22 2020   Sun Aug 23 19:43:34 2020
server02          Fresh            yes      3.1.0-ub18.04u28~1594095612.8f00ba1  Mon Jul 13 18:30:46 2020  Mon Jul 13 22:09:19 2020  Tue Jul 14 19:35:59 2020   Sun Aug 23 19:48:07 2020
server03          Fresh            yes      3.1.0-ub18.04u28~1594095612.8f00ba1  Mon Jul 13 18:30:46 2020  Mon Jul 13 22:09:20 2020  Tue Jul 14 19:36:22 2020   Sun Aug 23 19:47:47 2020
server04          Fresh            yes      3.1.0-ub18.04u28~1594095612.8f00ba1  Mon Jul 13 18:30:46 2020  Mon Jul 13 22:09:20 2020  Tue Jul 14 19:35:59 2020   Sun Aug 23 19:47:52 2020
server05          Fresh            yes      3.1.0-ub18.04u28~1594095612.8f00ba1  Mon Jul 13 18:30:46 2020  Mon Jul 13 22:09:20 2020  Tue Jul 14 19:36:02 2020   Sun Aug 23 19:46:27 2020
server06          Fresh            yes      3.1.0-ub18.04u28~1594095612.8f00ba1  Mon Jul 13 18:30:46 2020  Mon Jul 13 22:09:21 2020  Tue Jul 14 19:36:37 2020   Sun Aug 23 19:47:37 2020
server07          Fresh            yes      3.1.0-ub18.04u28~1594095612.8f00ba1  Mon Jul 13 17:58:02 2020  Mon Jul 13 22:09:21 2020  Tue Jul 14 19:36:01 2020   Sun Aug 23 18:01:08 2020
server08          Fresh            yes      3.1.0-ub18.04u28~1594095612.8f00ba1  Mon Jul 13 17:58:18 2020  Mon Jul 13 22:09:23 2020  Tue Jul 14 19:36:03 2020   Mon Aug 24 09:10:38 2020
spine01           Fresh            yes      3.1.0-cl3u28~1594095615.8f00ba1      Mon Jul 13 17:48:43 2020  Mon Aug 10 19:55:07 2020  Mon Aug 10 19:55:07 2020   Sun Aug 23 19:57:05 2020
spine02           Fresh            yes      3.1.0-cl3u28~1594095615.8f00ba1      Mon Jul 13 17:47:39 2020  Mon Aug 10 19:55:09 2020  Mon Aug 10 19:55:09 2020   Sun Aug 23 19:56:39 2020
spine03           Fresh            yes      3.1.0-cl3u28~1594095615.8f00ba1      Mon Jul 13 17:47:40 2020  Mon Aug 10 19:55:12 2020  Mon Aug 10 19:55:12 2020   Sun Aug 23 19:57:29 2020
spine04           Fresh            yes      3.1.0-cl3u28~1594095615.8f00ba1      Mon Jul 13 17:47:56 2020  Mon Aug 10 19:55:11 2020  Mon Aug 10 19:55:11 2020   Sun Aug 23 19:58:23 2020
```

{{</tab>}}

{{</tabs>}}