---
title: Monitor Network Inventory
author: Cumulus Networks
weight: 610
toc: 4
---
With the NetQ UI and CLI, a user can monitor the network inventory of switches and hosts across the entire network, including such items as the number of each and what operating systems are installed. Additional details are available about the hardware and software components on individual switches, such as  the motherboard, ASIC, microprocessor, disk, memory, fan and power supply information. This is extremely useful for understanding the dependence on various vendors and versions, when planning upgrades or the scope of any other required changes.

The commands and cards available to obtain this type of information help you to answer questions such as:

- What switches do I have in the network?
- What is the distribution of ASICs across my network?
- Do all switches have valid licenses?
- Are NetQ agents running on all of my switches?
- What hardware is installed on my switches?
- What software is installed on my switches?
- What is the ACL and forwarding resources usage?
- Do all switches have NetQ Agents running?

To monitor individual switch inventory, refer to {{<link title="Monitor Switch Inventory">}}.

To view the network or device performance data, refer to {{<link title="Monitor Network and Device Performance">}}.

## Access Network Inventory Data

The Cumulus NetQ UI provides the Inventory|Devices card for monitoring network-wide inventory information. It provides varying degrees of information about hardware and software on all switches and hosts running NetQ. 

Access this card from the Cumulus Workbench, or add it to your own workbench by clicking <img src="https://icons.cumulusnetworks.com/44-Entertainment-Events-Hobbies/02-Card-Games/card-game-diamond.svg" height="18" width="18"/> (Add card) > **Inventory**  > Inventory|Devices card > **Open Cards**.

{{<figure src="/images/netq/inventory-devices-medium-240.png" width="200">}}

The CLI provides detailed network inventory information through its `netq show inventory` command.

## View Network Inventory Summary

All of the devices in your network can be viewed from either the NetQ UI or NetQ CLI.

{{< tabs "TabID13" >}}

{{< tab "NetQ UI" >}}

### View the Number of Each Device Type in Your Network

You can view the number of switches and hosts deployed in your network. As you grow your network this can be useful for validating that devices have been added as scheduled.

To view the quantity of devices in your network, locate or open the small or medium Inventory|Devices card.

{{<figure src="/images/netq/inventory-devices-small-240.png" width="200">}}
{{<figure src="/images/netq/inventory-devices-medium-230.png" width="200">}}

### View All Switches

You can view all stored attributes for all switches in your network. To view all switch details, open the full screen Inventory|Devices card and click the **All Switches** tab in the navigation panel.

{{<figure src="/images/netq/inventory-devices-fullscr-allswitches-tab-241.png" width="700">}}

To return to your workbench, click <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/close.svg" height="14" width="14"/> in the top right corner of the card.

### View All Hosts

You can view all stored attributes for all hosts in your network. To view all host details, open the full screen Inventory|Devices card and click the **All Hosts** tab in the navigation panel.

{{<figure src="/images/netq/inventory-devices-fullscr-allhosts-tab-241.png" width="700" >}}

To return to your workbench, click <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/close.svg" height="14" width="14"/> in the top right corner of the card.

{{< /tab >}}

{{< tab "NetQ CLI" >}}

To view a list of devices in your network, run:

```
netq show inventory brief [json]
```

This example shows that we have four spine switches, three leaf switches, two border switches, two firewall switches, seven hosts (servers), and an out-of-band management server in this network. For each of these we see the type of switch, operating system, CPU and ASIC.

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

{{< /tab >}}

{{< /tabs >}}

## View Hardware Inventory across the Network

You can view all hardware components or narrow your view to specific hardware components for all of the switches in your network.

### View Components Summary for All Switches

Switch component inventory can be viewed from either the NetQ UI or NetQ CLI.

{{< tabs "TabID87" >}}

{{< tab "NetQ UI" >}}

To view switch components:

1. Locate the Inventory|Devices card on your workbench.

2. Hover over the card, and change to the large size card using the size picker.

    By default the Switches tab is shown displaying the total number of switches, ASIC vendors, OS versions, license status, NetQ Agent versions, and specific platforms deployed across all of your switches.

    {{<figure src="/images/netq/inventory-devices-large-switches-tab-230.png" width="500">}}

<div style="padding-left: 18px;">You can hover over any of the segments in a component distribution chart to highlight a specific type of the given component. When you *hover*, a tooltip appears displaying:</div>

<div style="padding-left: 18px;"><ul>
<li>Name or value of the component type, such as the version number or status</li>
<li>Total number of switches with that type of component deployed compared to the total number of switches</li>
<li>Percentage of this type with respect to all component types</li></ul></div>

    {{<figure src="/images/netq/inventory-devices-large-switches-tab-component-highlight-230.png" width="650">}}

<div style="padding-left: 18px;">Additionally, sympathetic highlighting is used to show the related component types relevant to the highlighted segment and the number of unique component types associated with this type (shown in blue here).</div>

{{< /tab >}}

{{< tab "NetQ CLI" >}}

To view switch components, run:

```
netq show inventory brief [json]
```

This example shows the operating systems (Cumulus Linux and Ubuntu), CPU architecture (all x86_64), ASIC (virtual), and ports (none, since virtual) for each device in the network. You can manually count the number of each of these, or export to a spreadsheet tool to sort and filter the list.

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

{{< /tab >}}

{{< /tabs >}}

### View ASIC Information for all Switches

ASIC information can be viewed from either the NetQ UI or NetQ CLI.

{{< tabs "TabID158" >}}

{{< tab "NetQ UI" >}}

To dig deeper on a particular component type, you can filter the card data by that type. In this procedure, the result of filtering on the ASIC component is shown.

View ASIC data in a graphic or a table:

{{< tabs "TabID181" >}}

{{< tab "Graphic">}}

1. Locate the Inventory|Devices card on your workbench.

2. Hover over the card, and change to the large size card using the size picker.

3. Click a segment of the ASIC graph in the component distribution charts.

    {{<figure src="/images/netq/inventory-devices-large-switches-tab-asic-component-filter-320.png" width="500">}}

4. Select the first option from the popup, *Filter ASIC*. The card data is filtered to show only the components associated with selected component type. A filter tag appears next to the total number of switches indicating the filter criteria.

    {{<figure src="/images/netq/inventory-devices-large-switches-tab-component-filter-asic-320.png" width="500">}}

5. Hover over the segments to view the related components.

    {{<figure src="/images/netq/inventory-devices-large-switches-tab-component-highlight-agent-320.png" width="500">}}

6. To return to the full complement of components, click the <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/close.svg" height="14" width="14"/> in the filter tag.

While the Device Inventory cards provide a network-wide view, you may want to see more detail about your switch inventory. This can be found in the Switches Inventory card workflow. To open that workflow, click the **Switch Inventory** button at the top right of the Switches card.

{{<figure src="/images/netq/inventory-devices-large-switches-tab-switch-inv-button-230.png" width="500">}}

{{< /tab >}}

{{< tab "Table" >}}

You can view ASIC model, modelID, vendor, and ports for all switches using the full-screen card. ASIC information is not available for hosts.

1. Locate the Inventory|Devices card on your workbench.

2. Hover over the card, and change to the full-screen card using the size picker.

    {{<figure src="/images/netq/inventory-devices-fullscr-allswitches-tab-241.png" width="700">}}

3. Scroll to the right to view the above ASIC information.

To return to your workbench, click <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/close.svg" height="14" width="14"/> in the top right corner of the card.

{{< /tab >}}

{{< /tabs >}}

{{< /tab >}}

{{< tab "NetQ CLI" >}}

To view the vendor, model, model identifier, core bandwidth capability, and ports of the ASIC installed on your switch motherboard, run:

```
netq show inventory asic [vendor <asic-vendor>|model <asic-model>|model-id <asic-model-id>] [json]
```

This example shows all of the ASIC attributes for all devices.

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
qct-ix7-04        N/A                  N/A                            N/A                       N/A            N/A
st1-l1            Broadcom             Trident2                       BCM56854                  720G           48 x 10G-SFP+ & 6 x 40G-QSFP+
st1-l2            Broadcom             Trident2                       BCM56854                  720G           48 x 10G-SFP+ & 6 x 40G-QSFP+
st1-l3            Broadcom             Trident2                       BCM56854                  720G           48 x 10G-SFP+ & 6 x 40G-QSFP+
st1-s1            Broadcom             Trident2                       BCM56850                  960G           32 x 40G-QSFP+
st1-s2            Broadcom             Trident2                       BCM56850                  960G           32 x 40G-QSFP+
```

You can filter the results of the command to view devices with a particular vendor, model, or modelID. This example shows all devices with a vendor of *Broadcom*.

```
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
```

{{< /tab >}}

{{< /tabs >}}

### View Motherboard Information for all Switches

You can view motherboard information from the NetQ UI or NetQ CLI, including the vendor, model, base MAC address, serial number, part number, revision, and manufacturing date for a switch motherboard on all devices.

{{< tabs "TabID266" >}}

{{< tab "NetQ UI">}}

1. Locate the Inventory|Devices card on your workbench.

2. Hover over the card, and change to the full-screen card using the size picker.

3. Scroll to the right to view the various parameters. Optionally drag and drop them to be next to each other.

    {{<figure src="/images/netq/inventory-devices-fullscr-allswitches-tab-241.png" width="700">}}

To return to your workbench, click <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/close.svg" height="14" width="14"/> in the top right corner of the card.

{{< /tab>}}

{{< tab "NetQ CLI">}}

To view a list of motherboards installed in your switches, run:

```
netq show inventory board [vendor <board-vendor>|model <board-model>] [json]
```

This example shows all of the motherboard data for all devices.

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

{{< /tab>}}

{{< /tabs >}}

### View CPU Information for all Switches and Hosts

You can view the architecture, model, operating frequency, and the number of cores for the CPU on all devices using the NetQ UI or NetQ CLI.

{{< tabs "TabID304" >}}

{{< tab "NetQ UI" >}}

1. Locate the Inventory|Devices card on your workbench.

2. Hover over the card, and change to the full-screen card using the size picker.

3. The **All Switches** tab is selected by default. Scroll to the right to view the various parameters. Optionally drag and drop them to be next to each other.

    {{<figure src="/images/netq/inventory-devices-fullscr-allswitches-tab-241.png" width="700">}}

4. Click **All Hosts** to view the same information for your host servers.

    {{<figure src="/images/netq/inventory-devices-fullscr-allhosts-tab-241.png" width="700" >}}

To return to your workbench, click <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/close.svg" height="14" width="14"/> in the top right corner of the card.

{{< /tab >}}

{{< tab "NetQ CLI" >}}

To view cpu information for your network, run:

```
netq show inventory cpu [arch <cpu-arch>] [json]
```

This example show the CPU for all devices.

```
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
```

You can filter the results of the command to view which switches employ a particular CPU architecture using the *arch* keyword. This example shows how to determine which architectures are deployed in your network, and then shows all devices with an *x86\_64* architecture.

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

{{< /tab >}}

{{< /tabs >}}

### View Disk Information for all Switches and Hosts

With NetQ UI you can view the size of the disk on all devices. With the NetQ CLI you can view the name or operating system, type, transport, size, vendor, and model of the disk on all devices. You can filter this list by name, transport, or vendor.

{{< tabs "TabID406" >}}

{{< tab "NetQ UI" >}}

1. Locate the Inventory|Devices card on your workbench.

2. Hover over the card, and change to the full-screen card using the size picker.

    {{<figure src="/images/netq/inventory-devices-fullscr-allswitches-tab-241.png" width="700">}}

3. Locate the **Disk Total Size** column.

4. Click **All Hosts** to view the total disk size of all host servers.

    {{<figure src="/images/netq/inventory-devices-fullscr-allhosts-tab-241.png" width="700" >}}

To return to your workbench, click <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/close.svg" height="14" width="14"/> in the top right corner of the card.

{{< /tab >}}

{{< tab "NetQ CLI" >}}

To view disk information for your switches, run:

```
netq show inventory disk [name <disk-name>|transport <disk-transport>|vendor <disk-vendor>] [json]
```

This example show the CPU for all devices.

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

{{< /tab >}}

{{< /tabs >}}

### View Memory Information for all Switches and Hosts

You can view the size of the memory on all devices with the NetQ CLI. You can view the name, type, size, speed, vendor, and serial number for the memory installed on all devices with the NetQ CLI.

{{< tabs "TabID480" >}}

{{< tab "NetQ UI" >}}

1. Locate the Inventory|Devices card on your workbench.

2. Hover over the card, and change to the full-screen card using the size picker.

    {{<figure src="/images/netq/inventory-devices-fullscr-allswitches-tab-241.png" width="700">}}

3. Locate the **Memory Size** column.

4. Click **All Hosts** to view the memory size for all host servers.

    {{<figure src="/images/netq/inventory-devices-fullscr-allhosts-tab-241.png" width="700" >}}

To return to your workbench, click <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/close.svg" height="14" width="14"/> in the top right corner of the card.
{{< /tab >}}

{{< tab "NetQ CLI" >}}

To view memory information for your switches and host servers, run:

```
netq show inventory memory [type <memory-type>|vendor <memory-vendor>] [json]
```

This example shows all of the memory characteristics for all devices.

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

You can filter the results of the command to view devices with a particular memory type or vendor. This example shows all of the devices with memory from *QEMU* .

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

{{< /tab >}}

{{< /tabs >}}



<!-- Move these topics to performance topic

### View Fan Health for All Switches

Fan, power supply unit, and temperature sensors are available to provide additional data about the NetQ system operation. To view the health of fans in your switches, use the `netq show sensors fan` command. If you name the fans in all of your switches consistently, you can view more information at once.

In this example, we look at the state of all fans with the name *fan1*.

```
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
```

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

To view the status for a particular switch, use the optional `hostname` parameter.

```
cumulus@switch:~$ netq leaf01 show sensors fan fan1
Hostname          Name            Description                         State      Speed      Max      Min      Message                             Last Changed
----------------- --------------- ----------------------------------- ---------- ---------- -------- -------- ----------------------------------- -------------------------
leaf01            fan1            fan tray 1, fan 1                   ok         2500       29000    2500                                         Sun Apr 21 20:07:12 2019
```

### View PSU Health for All Switches

Fan, power supply unit, and temperature sensors are available to provide additional data about the NetQ Platform operation. To view the health of PSUs in your switches, use the `netq show sensors psu` command. If you name the PSUs in all of your switches consistently, you can view more information at once.

In this example, we look at the state of all PSUs with the name *psu2*.

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

{{<notice tip>}}

Use Tab completion to determine the names of the PSUs in your switches. Use the optional <code>hostname</code> parameter to view the PSU state for a given switch.

{{</notice>}}

### View the Temperature in All Switches

Fan, power supply unit, and temperature sensors are available to provide additional data about the NetQ Platform operation. To view the temperature sensor status, current temperature, and configured threshold values, use the `netq show sensors temp` command. If you name the temperature sensors in all of your switches consistently, you can view more information at once.

In this example, we look at the state of all temperature sensors with the name *psu1temp1*.

```
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
```

{{<notice tip>}}

Use Tab completion to determine the names of the temperature sensors in
your switches. Use the optional <code>hostname</code> parameter to view the
temperature state, current temperature, and threshold values for a given
switch.

{{</notice>}}

### View All Sensor Data

To view all fan data, all PSU data, or all temperature data from the sensors in a chassis, you must view all of the sensor data. The more consistently you name your sensors, the easier it will be to view the full sensor data.

```
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
```

#### View All Sensor-related Events

You can view the events that are triggered by the chassis sensors using the
`netq show events` command. You can narrow the focus to only critical
events using the severity `level` option.

```
cumulus@switch:~$ netq show events type sensors
No matching events records found
```

```
cumulus@switch:~$ netq show events level critical type sensors
No matching events records found
```

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
-->

## View Software Inventory across the Network

You can view all software components or narrow your view to specific software components for all of the devices in your network.

### View the Operating Systems Running on All Switches and Hosts

With both the NetQ UI and NetQ CLI, you can view the vendor name and version of the OS on all devices, and when it was last modified. With the NetQ UI you can also view the OS ID and view the distribution of operating systems running on your switches and hosts. This is useful for verifying which versions of the OS are deployed and for upgrade planning. It also provides a view into the relative dependence on a given OS in your network.

{{< tabs "TabID1079" >}}

{{< tab "NetQ UI" >}}

1. Locate the medium Inventory|Devices card on your workbench.

    {{<figure src="/images/netq/inventory-devices-medium-230.png" width="200">}}

2. Hover over the pie charts to view the total number of devices with a given operating system installed.

3. Change to the full-screen card using the size picker.

    {{<figure src="/images/netq/inventory-devices-fullscr-allswitches-tab-241.png" width="700">}}

4. Scroll to the right to locate all of the OS parameter data.

5. Click **All Hosts** to view the OS parameters for all host servers.

    {{<figure src="/images/netq/inventory-devices-fullscr-allhosts-tab-241.png" width="700" >}}

To return to your workbench, click <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/close.svg" height="14" width="14"/> in the top right corner of the card.

{{< /tab >}}

{{< tab "NetQ CLI" >}}

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
edge01            Ubuntu          16.04                                Fri Aug 14 16:01:18 2020
exit01            CL              3.7.5                                Fri Aug 14 16:01:18 2020
exit02            CL              3.7.5                                Fri Aug 14 16:01:18 2020
leaf01            CL              3.7.5                                Sun Aug 14 16:01:18 2020
leaf02            CL              3.7.5                                Fri Aug 14 16:01:18 2020
leaf03            CL              3.7.5                                Fri Aug 14 16:01:18 2020
leaf04            CL              3.7.5                                Fri Aug 14 16:01:18 2020
server01          Ubuntu          16.04                                Fri Aug 14 16:01:18 2020
server02          Ubuntu          16.04                                Fri Aug 14 16:01:18 2020
server03          Ubuntu          16.04                                Fri Aug 14 16:01:18 2020
server04          Ubuntu          16.04                                Fri Aug 14 16:01:18 2020
spine01           CL              3.7.5                                Fri Aug 14 16:01:18 2020
spine02           CL              3.7.5                                Fri Aug 14 16:01:18 2020
```

You can filter the results of the command to view only devices with a
particular operating system or version. This can be especially helpful
when you suspect that a particular device has not been upgraded as
expected. This example shows all devices with the Cumulus Linux version
3.7.5 installed.

```
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
```

This example shows changes that have been made to the OS on all devices
between 16 and 21 days ago. Remember to use measurement units on the
time values.

```
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
```

{{< /tab >}}

{{< /tabs >}}

### View License Information for all Switches

In both the NetQ UI and NetQ CLI you can view the name and current state
of the license (whether it is valid or invalid/missing).  The date at which the license was last updated is also shown.

{{<notice note>}}

If a license is no longer valid or missing, the associated switch does not operate properly. Hosts do not have Cumulus Linux or NetQ licenses.</ul>

{{</notice>}}

{{< tabs "TabID1187" >}}

{{< tab "NetQUI" >}}

1. Locate the medium Inventory|Devices card on your workbench.

    {{<figure src="/images/netq/inventory-devices-medium-230.png" width="200">}}

2. Hover over the distribution chart for license to view the total number of devices with a given operating system installed.

3. Alternately, change to the full-screen card using the size picker.

    {{<figure src="/images/netq/inventory-devices-fullscr-allswitches-tab-241.png" width="700">}}

4. Scroll to the right to locate the **License State** column.

{{< /tab >}}

{{< tab "NetQ CLI" >}}

To view license information for your switches, run:

```
netq show inventory license [cumulus] [status ok | status missing] [around <text-time>] [json]
```

This example shows the license information for all switches.

```
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
```

You can view the historical state of licenses using the around keyword.
This example shows the license state for all devices about 7 days ago.
Remember to use measurement units on the time values.

```
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
```

You can filter the results to show license changes during a particular
time frame for a particular device. This example shows that there have
been no changes to the license state on spine01 between now and 24 hours
ago.

```
cumulus@switch:~$ netq spine01 show events type license between now and 24h
No matching events records found
```

{{< /tab >}}

{{< /tabs >}}

### View the Supported Cumulus Linux Packages on all Switches

When you are troubleshooting an issue with a switch, you might want to know what versions of the Cumulus Linux operating system are supported on that switch and on a switch that is not having the same issue.

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

### View All Software Packages Installed on All Switches

If you are having an issue with a particular switch, you may want to verify what software is installed and whether it needs updating.

To view package information for your switches, run:

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

### View Recommended Software Packages on All Switches

You can determine whether any of your switches are using a software package other than the default package associated with the Cumulus Linux release that is running on the switches. Use this list  determine which packages to install/upgrade on all devices. Additionally, you can determine if a software package is missing.

To view recommended package information for your switches, run:

```
netq show recommended-pkg-version [release-id <text-release-id>] [package-name <text-package-name>] [json]
```

{{<notice tip>}}
The output may be rather lengthy if this command is run for all releases and packages. If desired, run the command using the <code>release-id</code> and/or <code>package-name</code> options to shorten the output.
{{</notice>}}

This example looks for switches running Cumulus Linux 3.7.1 and `switchd`. The result is a single switch, *leaf12*, that has older software and is recommended for update.

```
cumulus@switch:~$ netq show recommended-pkg-version release-id 3.7.1 package-name switchd
Matching manifest records:
Hostname          Release ID           ASIC Vendor          CPU Arch             Package Name         Version              Last Changed
----------------- -------------------- -------------------- -------------------- -------------------- -------------------- -------------------------
leaf12            3.7.1                vx                   x86_64               switchd              1.0-cl3u30           Wed Feb  5 04:36:30 2020
```

This example looks for switches running Cumulus Linux 3.7.1 and `ptmd`. The result is a single switch, *server01*, that has older software and is recommended for update.

```
cumulus@switch:~$ netq show recommended-pkg-version release-id 3.7.1 package-name ptmd
Matching manifest records:
Hostname          Release ID           ASIC Vendor          CPU Arch             Package Name         Version              Last Changed
----------------- -------------------- -------------------- -------------------- -------------------- -------------------- -------------------------
server01            3.7.1                vx                   x86_64               ptmd                 3.0-2-cl3u8          Wed Feb  5 04:36:30 2020
```

This example looks for switches running Cumulus Linux 3.7.1 and `lldpd`. The result is a single switch, *server01*, that has older software and is recommended for update.

```
cumulus@switch:~$ netq show recommended-pkg-version release-id 3.7.1 package-name lldpd
Matching manifest records:
Hostname          Release ID           ASIC Vendor          CPU Arch             Package Name         Version              Last Changed
----------------- -------------------- -------------------- -------------------- -------------------- -------------------- -------------------------
server01            3.7.1                vx                   x86_64               lldpd                0.9.8-0-cl3u11       Wed Feb  5 04:36:30 2020
```

This example looks for switches running Cumulus Linux 3.6.2 and `switchd`. The result is a single switch, *leaf04*, that has older software and is recommended for update.

```
cumulus@noc-pr:~$ netq show recommended-pkg-version release-id 3.6.2 package-name switchd
Matching manifest records:
Hostname          Release ID           ASIC Vendor          CPU Arch             Package Name         Version              Last Changed
----------------- -------------------- -------------------- -------------------- -------------------- -------------------- -------------------------
leaf04            3.6.2                vx                   x86_64               switchd              1.0-cl3u27           Wed Feb  5 04:36:30 2020
```

<!-- Move to device inventory -->
<!-- from the switch
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
``` -->

### View ACL Resources on All Switches

Using the NetQ CLI, you can monitor the incoming and outgoing access control lists (ACLs) configured on all devices, currently or at a time in the past.

To view ACL resources for all of your switches, run:

```
netq show cl-resource acl [ingress | egress] [around <text-time>] [json]
```

Use the `egress` or `ingress` options to show only the outgoing or incoming ACLs. Use the `around` option to show this information for a time in the past.

<!-- Move to switch inventory
This example shows the ACL resources for the *leaf01* switch.

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
``` -->

### View Forwarding Resources on All Switches

With the NetQ CLI, you can monitor the amount of forwarding resources used by all devices, currently or at a time in the past.

To view forwarding resources for all of your switches, run:

```
netq show cl-resource forwarding [around <text-time>] [json]
```

Use the `around` option to show this information for a time in the past.

<!-- Move to switch inventory
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
``` -->

### Validate NetQ Agents are Running on All Switches and Hosts

With the NetQ UI and the NetQ CLI, you can confirm that NetQ Agents are running on switches and hosts (if installed). using the `netq show agents` command. Viewing the **Status** column of the output indicates whether the agent is up and current, labelled *Fresh*, or down and stale, labelled *Rotten*. Additional information is provided about the agent status, including whether it is time synchronized, how long it has been up, and the last time its state changed. You can also see the version running.

{{< tabs "TabID1549" >}}

{{< tab "NetQ UI" >}}

To view the NetQ Agents on all switches and hosts:

1. Open the Main menu (click ).

2. Select **Agents** from the **Network** column.

    {{<figure src="/images/netq/main-menu-ntwk-agents-241.png" width="700">}}

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

{{< /tab >}}

{{< tab "NetQ CLI" >}}

To view the NetQ Agents on all switches and hosts, run:

```
netq show agents [fresh | rotten ] [around <text-time>] [json]
```

Use the `fresh` keyword to view only the NetQ Agents that are in current communication with the NetQ Platform or NetQ Collector. Use the `rotten` keyword to view those that are not. Use the `around` keyword to view the state of NetQ Agents at an earlier time.

This example shows the current NetQ Agent state on all devices.

```

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
```

{{< /tab >}}

{{< /tabs >}}

<!-- Move to performance: new file "system services"

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
                                            m failed to Established -->
