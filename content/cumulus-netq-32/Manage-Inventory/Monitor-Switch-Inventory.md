---
title: Monitor Switch Inventory
author: Cumulus Networks
weight: 620
toc: 4
---
With the NetQ UI and NetQ CLI, you can monitor your inventory of switches across the network or individually. A user can monitor such items as operating system, motherboard, ASIC, microprocessor, disk, memory, fan and power supply information. Being able to monitor this inventory aids in upgrades, compliance, and other planning tasks.

The commands and cards available to obtain this type of information help you to answer questions such as:

- What hardware is installed on my switch?
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

Component information for all of the switches in your network can be viewed from both the NetQ UI and NetQ CLI.

- Inventory|Switches card:
    - Small: view count of switches and distribution of switch status
    - Medium: view count of OS, license, ASIC, platform, CPU model, Disk, and memory types or versions across all switches
- `netq show inventory` command:
    -View ASIC, CPU, disk, OS, and ports on all switches

{{< tabs "TabID25" >}}

{{< tab "NetQ UI" >}}

1. Locate the Inventory|Switches card on your workbench.

2. From the medium sized card, view the distribution of hardware and software components across the network.

3. Hover over any of the segments in the distribution chart to highlight a specific component.

    {{<figure src="/images/netq/inventory-switch-medium-hover-license-230.png" width="200">}}

<div style="padding-left: 18px;">When you <em>hover</em>, a tooltip appears displaying:

<ul>
<li>Name or value of the component type, such as the version number or status</li>
<li>Total number of switches with that type of component deployed compared to the total number of switches</li>
<li>Percentage of this type with respect to all component types</li></ul></div>

4. Choose *Rotten Switches* from the dropdown to see which, if any, switches are currently not communicating with NetQ.

    {{<figure src="/images/netq/switch-status-dropdown-320.png" width="180">}}

5. Return to your fresh switches, then hover over the card header and change to the small size card using the size picker.

    {{<figure src="/images/netq/inventory-switch-small-230.png" width="150">}}

<div style="padding-left: 18px;">Here you can see the total switch count and the distribution of those that are communicating well and those that are not.</div>

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

This example show the components on the NetQ On-premises or Cloud Appliance.

```
cumulus@switch:~$ netq show inventory brief opta
Matching inventory records:
Hostname          Switch               OS              CPU      ASIC            Ports
----------------- -------------------- --------------- -------- --------------- -----------------------------------
netq-ts           N/A                  Ubuntu          x86_64   N/A             N/A
```

{{< /tab >}}

{{< /tabs >}}

## View Switch Hardware Inventory

You can view hardware components deployed on each switch in your network.

### View ASIC Information for a Switch

ASIC information for a switch can be viewed from either the NetQ CLI or NetQ UI.

{{< tabs "TabID96" >}}

{{< tab "NetQ UI" >}}

1. Locate the medium Inventory|Switches card on your workbench.

2. Hover over a segment of the ASIC graph in the distribution chart.

    The same information is available on the summary tab of the large size card.

    {{<figure src="/images/netq/inventory-switch-large-summary-tab-230.png" width="700">}}

3. Hover over the card header and click <img src="https://icons.cumulusnetworks.com/03-Computers-Devices-Electronics/08-Microprocessor-Chips/computer-chip-core.svg" height="14" width="14"/> to view the ASIC vendor and model distribution.

4. Hover over charts to view the name of the ASIC vendors or models, how many switches have that vendor or model deployed, and the percentage of this number compared to the total number of switches.

    {{<figure src="/images/netq/inventory-switch-large-asic-tab-230.png" width="700">}}

5. Change to the full-screen card and click **ASIC**.

    {{<figure src="/images/netq/inventory-switch-fullscr-asic-tab-320.png" width="700">}}

<div style="padding-left: 18px;">Note that if you are running CumulusVX switches, no detailed ASIC information is available because the hardware is virtualized.</div>

6. Click {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/15-Filter/filter-1.svg" height="18" width="18">}} to quickly locate a switch that does not appear on the first page of the switch list.

7. Select *hostname* from the **Field** dropdown.

8. Enter the hostname of the switch you want to view, and click **Apply**.

   {{<figure src="/images/netq/inventory-switch-fullscr-filterbyhostname-320.png" width="300">}}

   {{<figure src="/images/netq/inventory-switch-asic-single-switch-filter-320.png" width="700">}}

9. To return to your workbench, click {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/close.svg" height="14" width="14">}} in the top right corner of the card.

{{< /tab >}}

{{< tab "NetQ CLI" >}}

To view information about the ASIC on a switch, run:

```
netq [<hostname>] show inventory asic [opta] [json]
```

This example shows the ASIC information for the *leaf02* switch.

```
cumulus@switch:~$ netq leaf02 show inventory asic
Matching inventory records:
Hostname          Vendor               Model                          Model ID                  Core BW        Ports
----------------- -------------------- ------------------------------ ------------------------- -------------- -----------------------------------
leaf02            Mellanox             Spectrum                       MT52132                   N/A            32 x 100G-QSFP28
```

This example shows the ASIC information for the NetQ On-premises or Cloud Appliance.

```
cumulus@switch:~$ netq show inventory asic opta
Matching inventory records:
Hostname          Vendor               Model                          Model ID                  Core BW        Ports
----------------- -------------------- ------------------------------ ------------------------- -------------- -----------------------------------
netq-ts            Mellanox             Spectrum                       MT52132                   N/A            32 x 100G-QSFP28
```

{{< /tab >}}

{{< /tabs >}}

### View Motherboard Information for a Switch

Motherboard/platform information is available from the NetQ UI and NetQ CLI.

- Inventory|Switches card
    - Medium/Large: view platform distribution across on all switches (graphic)
    - Full-screen: view platform vendor, model, manufacturing date, revision, serial number, MAC address, series for a switch (table)
- `netq show inventory board` command
    - View motherboard vendor, model, base MAC address, serial number, part number, revision, and manufacturing date on a switch

{{< tabs "TabID164" >}}

{{< tab "NetQ UI">}}

1. Locate the medium Inventory|Switches card on your workbench.

2. Hover over the card, and change to the large card using the size picker.

3. Hover over the header and click {{<img src="/images/netq/platform-icon.png" height="14" width="14">}}.

    {{<figure src="/images/netq/inventory-switch-large-platform-tab.png" width="500">}}

4. Hover over a segment in the Vendor or Platform graphic to view how many switches deploy the specified vendor or platform.

    Context sensitive highlighting is also employed here, such that when you select a vendor, the corresponding platforms are also highlighted; and vice versa. Note that you can also see the status of the Cumulus Linux license for each switch.

5. Click either **Show All** link to open the full-screen card.

6. Click **Platform**.

    {{<figure src="/images/netq/inventory-switch-fullscr-platform-tab-320.png" width="700">}}

<div style="padding-left: 18px;">Note that if you are running CumulusVX switches, no detailed platform information is available because the hardware is virtualized.</div>

7. Click {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/15-Filter/filter-1.svg" height="18" width="18">}} to quickly locate a switch that does not appear on the first page of the switch list.

8. Select *hostname* from the **Field** dropdown.

9. Enter the hostname of the switch you want to view, and click **Apply**.

   {{<figure src="/images/netq/inventory-switch-fullscr-filterbyhostname-320.png" width="300">}}

   {{<figure src="/images/netq/inventory-switch-platform-single-switch-filter-320.png" width="700">}}

10. To return to your workbench, click {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/close.svg" height="14" width="14">}} in the top right corner of the card.

{{< /tab >}}

{{< tab "NetQ CLI" >}}

To view a list of motherboards installed in a switch, run:

```
netq [<hostname>] show inventory board [opta] [json]
```

This example shows all of the motherboard data for the *spine01* switch.

```
cumulus@switch:~$ netq spine01 show inventory board
Matching inventory records:
Hostname          Vendor               Model                          Base MAC           Serial No                 Part No          Rev    Mfg Date
----------------- -------------------- ------------------------------ ------------------ ------------------------- ---------------- ------ ----------
spine01           Dell                 S6000-ON                       44:38:39:00:80:00  N/A                       N/A              N/A    N/A
```

Use the `opta` option without the `hostname` option to view the motherboard data for the NetQ On-premises or Cloud Appliance.

{{< /tab >}}

{{< /tabs >}}

### View CPU Information for a Switch

CPU information is available from the NetQ UI and NetQ CLI.

- Inventory|Switches card
    - Medium/Large: view CPU distribution across on all switches (graphic)
    - Full-screen: view CPU architecture, model, maximum operating frequency, the number of cores, and data on a switch (table)
- `netq show inventory cpu` command
    - View CPU architecture, model, maximum operating frequency, and the number of cores on a switch

{{< tabs "TabID232" >}}

{{< tab "NetQ UI" >}}

1. Locate the Inventory|Switches card on your workbench.

2. Hover over a segment of the CPU graph in the distribution chart.

    The same information is available on the summary tab of the large size card.

    {{<figure src="/images/netq/inventory-switch-large-summary-tab-230.png" width="700">}}

3. Hover over the card, and change to the full-screen card using the size picker.

4. Click **CPU**.

    {{<figure src="/images/netq/inventory-switch-fullscr-cpu-tab-320.png" width="700" >}}

5. Click {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/15-Filter/filter-1.svg" height="18" width="18">}} to quickly locate a switch that does not appear on the first page of the switch list.

6. Select *hostname* from the **Field** dropdown. Then enter the hostname of the switch you want to view.

   {{<figure src="/images/netq/inventory-switch-fullscr-cpu-filterbyhostname-320.png" width="300">}}

   {{<figure src="/images/netq/inventory-switch-cpu-single-switch-filter-320.png" width="700">}}

7. To return to your workbench, click {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/close.svg" height="14" width="14">}} in the top right corner of the card.

{{< /tab >}}

{{< tab "NetQ CLI" >}}

To view CPU information for a switch in your network, run:

```
netq [<hostname>] show inventory cpu [arch <cpu-arch>] [opta] [json]
```

This example shows CPU information for the *server02* switch.

```
cumulus@switch:~$ netq server02 show inventory cpu
Matching inventory records:
Hostname          Arch     Model                          Freq       Cores
----------------- -------- ------------------------------ ---------- -----
server02          x86_64   Intel Core i7 9xx (Nehalem Cla N/A        1
                            ss Core i7)
```

This example shows the CPU information for the NetQ On-premises or Cloud Appliance.

```
cumulus@switch:~$ netq show inventory cpu opta
Matching inventory records:
Hostname          Arch     Model                          Freq       Cores
----------------- -------- ------------------------------ ---------- -----
netq-ts           x86_64   Intel Xeon Processor (Skylake, N/A        8
                           IBRS)
```

{{< /tab >}}

{{< /tabs >}}

### View Disk Information for a Switch

Disk information is available from the NetQ UI and NetQ CLI.

- Inventory|Switches card
    - Medium/Large: view Disk distribution across on all switches (graphic)
    - Full-screen: view disk vendor, size, revision, model, name, transport, and type on a switch (table)
- `netq show inventory disk` command
    - View disk name, type, transport, size, vendor, and model on all devices

{{< tabs "TabID336" >}}

{{< tab "NetQ UI" >}}

1. Locate the Inventory|Switches card on your workbench.

2. Hover over a segment of the disk graph in the distribution chart.

    The same information is available on the summary tab of the large size card.

    {{<figure src="/images/netq/inventory-switch-large-summary-tab-230.png" width="700">}}

3. Hover over the card, and change to the full-screen card using the size picker.

4. Click **Disk**.

    {{<figure src="/images/netq/inventory-switch-fullscr-disk-tab-320.png" width="700">}}

<div style="padding-left: 18px;">Note that if you are running CumulusVX switches, no detailed disk information is available because the hardware is virtualized.</div>

5. Click {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/15-Filter/filter-1.svg" height="18" width="18">}} to quickly locate a switch that does not appear on the first page of the switch list.

6. Select *hostname* from the **Field** dropdown. Then enter the hostname of the switch you want to view.

   {{<figure src="/images/netq/inventory-switch-fullscr-filterbyhostname-320.png" width="300">}}

   {{<figure src="/images/netq/inventory-switch-disk-single-switch-filter-320.png" width="700">}}

7. To return to your workbench, click <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/close.svg" height="14" width="14"/> in the top right corner of the card.

{{< /tab >}}

{{< tab "NetQ CLI" >}}

To view disk information for a switch in your network, run:

```
netq [<hostname>] show inventory disk [opta] [json]
```

This example shows the disk information for the *leaf03* switch.

```
cumulus@switch:~$ netq leaf03 show inventory disk
Matching inventory records:
Hostname          Name            Type             Transport          Size       Vendor               Model
----------------- --------------- ---------------- ------------------ ---------- -------------------- ------------------------------
leaf03            vda             disk             N/A                6G         0x1af4               N/A
```

This example show the disk information for the NetQ On-premises or Cloud Appliance.

```
cumulus@switch:~$ netq show inventory disk opta

Matching inventory records:
Hostname          Name            Type             Transport          Size       Vendor               Model
----------------- --------------- ---------------- ------------------ ---------- -------------------- ------------------------------
netq-ts           vda             disk             N/A                265G       0x1af4               N/A
```

{{< /tab >}}

{{< /tabs >}}

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
