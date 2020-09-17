---
title: Monitor Switch Performance
author: Cumulus Networks
weight: 830
toc: 4
---
With the NetQ UI and NetQ CLI, you can monitor the health of individual switches, including interface performance and resource utilization.

Three categories of performance metrics are available for switches:

- **System configuration**: alarms, interfaces, IP and MAC addresses, VLANs, IP routes, IP neighbors, and installed software packages
- **Utilization statistics**: CPU, memory, disk, ACL and forwarding resources, SSD, and BTRFS
- **Physical sensing**: digital optics, chassis sensors, and WJH

For information about the health of network services and protocols (BGP, EVPN, NTP, and so forth) running on switches, refer to the relevant layer monitoring topic.

For switch inventory information for all switches (ASIC, platform, CPU, memory, disk, and OS), refer to {{<link title="Monitor Switch Inventory">}}.

## View Overall Health

The NetQ UI provides several views that enable users to easily track the overall health of switch, some high-level metrics, and attributes of the switch.

### View the Overall Health

When you want to view an overview of the current or past health of a particular switch, open the NetQ UI small Switch card. It is unlikely that you would have this card open for every switch in your network at the same time, but it is useful for tracking selected switches that may have been problematic in the recent past or that you have recently installed. The card shows you alarm status, a summary health score, and health trend.

To view the summary:

1. Click {{<img src="https://icons.cumulusnetworks.com/03-Computers-Devices-Electronics/09-Hard-Drives/hard-drive-1.svg" height="18" width="18">}} (Switches), then click **Open a switch card**.

    {{<figure src="/images/netq/add-switch-card-modal-310.png" width="250">}}

2. Begin typing the hostname of the switch you are interested in. Select it from the suggested matches when it appears.

    {{<figure src="/images/netq/add-switch-card-auto-suggest-310.png" width="250">}}

3. Select *Small* from the card size dropdown.

    {{<figure src="/images/netq/add-switch-card-choose-size-320.png" width="250">}}

4. Click **Add**.

    {{<figure src="/images/netq/dev-switch-small-card-230.png" width="200">}}

    This example shows the *leaf01* switch has had very few alarms overall, but the number is trending upward, with a total count of 24 alarms currently.

### View High-Level Health Metrics

When you are monitoring switches that have been problematic or are newly installed, you might want to view more than a summary. Instead, seeing key performance metrics can help you determine where issues might be occurring or how new devices are functioning in the network.

To view the key metrics, use the NetQ UI to open the medium Switch card. The card shows you the overall switch health score and the scores for the key metrics that comprise that score. The key metric scores are based on the number of alarms attributed to the following activities on the switch:

- Network services, such as BGP, EVPN, MLAG, NTP, and so forth
- Interface performance
- System performance

Locate or open the relevant Switch card:

1. Click {{<img src="https://icons.cumulusnetworks.com/03-Computers-Devices-Electronics/09-Hard-Drives/hard-drive-1.svg" height="18" width="18">}} (Switches), then click **Open a switch card**.

2. Begin typing the hostname of the device you are interested in. Select it from the suggested matches when it appears.

3. Click **Add**.

{{<figure src="/images/netq/dev-switch-medium-alarms-charts-231.png" width="420">}}

Also included on the card is the total alarm count for all of these metrics. You can view the key performance metrics as numerical scores or as line charts over time, by clicking **Alarms** or **Charts** at the top of the card.

### View Attributes

For a quick look at the key attributes of a particular switch, open the large Switch card.

Locate or open the relevant Switch card:

- Hover over the card, then change to the large card using the card size picker.

OR

1. Click {{<img src="https://icons.cumulusnetworks.com/03-Computers-Devices-Electronics/09-Hard-Drives/hard-drive-1.svg" height="18" width="18">}} (Switches), then click **Open a switch card**.

2. Begin typing the hostname of the device you are interested in. Select it from the suggested matches when it appears.

3. Select *Large* from the card size dropdown.

4. Click **Add**.

Attributes are displayed as the default tab on the large Switch card. You can view the static information about the switch, including its hostname, addresses, server and ASIC vendors and models, OS and NetQ software information. You can also view the state of the interfaces, NetQ Agent, and license on the switch.

{{<figure src="/images/netq/dev-switch-large-attributes-tab-230.png" width="500">}}

From a performance perspective, this example shows that five interfaces are down, the NetQ Agent is communicating with the NetQ appliance or VM, and it is missing the Cumulus Linux license. It is important the license is valid, so you would want to fix this first (refer to {{<link url="https://docs.cumulusnetworks.com/cumulus-linux-42/Quick-Start-Guide/#install-the-license" text="Install the Cumulus Linux License">}}). Secondly, you would want to look more closely at the interfaces (refer to {{<link title="View Interface Statistics for a Switch" text="interface statistics">}}).

## System Configuration Metrics

At some point in the lifecycle of a switch, you are likely to want more detail about how the switch is configured and what software is running on it. The NetQ UI and the NetQ CLI can provide this information.

### View All Switch Alarms

### View Status of All Interfaces

You can view all of the configured interfaces on a switch in one place making it easier to see inconsistencies in the configuration, quickly see when changes were made, and the operational status.

To view all interfaces:

1. Open the full-screen Switch card and click **All Interfaces**.

    {{<figure src="/images/netq/dev-switch-fullscr-interfaces-tab-241.png" width="700">}}

2. Look for interfaces that are down, shown in the **State** column.

3. Look for recent changes to the interfaces, shown in the **Last Changed** column.

4. View details about each interface, shown in the **Details** column.

5. Verify they are of the correct kind for their intended function, shown in the **Type** column.

6. Verify the correct VRF interface is assigned to an interface, shown in the **VRF** column.

7. To return to the workbench, click <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/close.svg" height="14" width="14"/> in the top right corner.

### View Status of All MAC Addresses

### View Status of All VLANs

### View Status of All IP Routes

### View Status of All IP Neighbors

### View Status of All IP Addresses

### View All Software Packages

You can view all of the software installed on a given switch to quickly validate versions and total software installed.

To view all software packages:

1. Open the full-screen Switch card and click **Installed Packages**.

    {{<figure src="/images/netq/dev-switch-fullscr-pkgs-tab-241.png" width="700">}}

2. Look for packages of interest and their version and status. Sort by a particular parameter by clicking <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/15-Filter/filter-1.svg" height="18" width="18"/>.

    {{<figure src="/images/netq/dev-switch-fullscr-filter-by-pkgname-241.png" width="300">}}

3. Optionally, export the list by selecting all or specific packages, then clicking <img src="https://icons.cumulusnetworks.com/05-Internet-Networks-Servers/08-Upload-Download/upload-bottom.svg" height="18" width="18"/>.

## Utilization Statistics

Utilization statistics provide a view into the operation of a switch. They indicate whether resources are becoming dangerously close to their maximum capacity or a user-defined threshold. Depending on the function of the switch, the acceptable thresholds can vary. You can use the NetQ UI or the NetQ CLI to access the utilization statistics.

### View Compute Resources Utilization

You can view the current utilization of CPU, memory, and disk resources to determine whether a switch is reaching its maximum load and compare its performance with other switches.

{{< tabs "TabID155" >}}

{{< tab "NetQ UI" >}}

To view the compute resources utilization:

1. Open the large Switch card.

2. Hover over the card and click <img src="https://icons.cumulusnetworks.com/06-Business-Products/12-Analytics/analytics-bars.svg" height="18" width="18"/>.

3. The card is divided into two sections, displaying hardware-related performance through a series of charts.

    {{<figure src="/images/netq/dev-switch-large-utilization-tab-230.png" width="500">}}

4. Look at the hardware performance charts.

    Are there any that are reaching critical usage levels? Is usage high at a particular time of day?

5. Change the time period. Is the performance about the same? Better? Worse? The results can guide your decisions about upgrade options.

6. Open the large Switch card for a comparable switch. Is the performance similar?

{{< /tab >}}

{{< tab "NetQ CLI" >}}

You can quickly determine how many compute resources &mdash; CPU, disk and memory &mdash; are being consumed by the switches on your network.

To obtain this information, run the relevant command:

```
netq <hostname> show resource-util [cpu | memory] [around <text-time>] [json]
netq <hostname> show resource-util disk [<text-diskname>] [around <text-time>] [json]
```

When no options are included the output shows the percentage of CPU and memory being consumed as well as the amount and percentage of disk space being consumed. You can use the `around` option to view the information for a particular time.

This example shows the CPU, memory, and disk utilization for the *leaf01* switch.

```
cumulus@switch:~$ netq leaf01 show resource-util
Matching resource_util records:
Hostname          CPU Utilization      Memory Utilization   Disk Name            Total                Used                 Disk Utilization     Last Updated
----------------- -------------------- -------------------- -------------------- -------------------- -------------------- -------------------- ------------------------
leaf01            4.5                  72.1                 /dev/vda4            6170849280           1230303232           20.9                 Wed Sep 16 20:35:57 2020

```

This example shows only the CPU utilization for the *leaf01* switch.

```
cumulus@switch:~$ netq leaf01 show resource-util cpu
Matching resource_util records:
Hostname          CPU Utilization      Last Updated
----------------- -------------------- ------------------------
leaf01            4.2                  Wed Sep 16 20:52:12 2020
```

This example shows only the memory utilization for the *leaf01* switch.

```
cumulus@switch:~$ netq leaf01 show resource-util memory
Matching resource_util records:
Hostname          Memory Utilization   Last Updated
----------------- -------------------- ------------------------
leaf01            72.1                 Wed Sep 16 20:52:12 2020
```

This example shows only the disk utilization for the *leaf01* switch. If you have more than one disk in your switch, utilization data for all of the disks are displayed. If you want to view the data for only one of the disks, you must specify a disk name.

```
cumulus@switch:~$ netq leaf01 show resource-util disk
Matching resource_util records:
Hostname          Disk Name            Total                Used                 Disk Utilization     Last Updated
----------------- -------------------- -------------------- -------------------- -------------------- ------------------------
leaf01            /dev/vda4            6170849280           1230393344           20.9                 Wed Sep 16 20:54:14 2020
```

{{< /tab >}}

{{< /tabs >}}

### View Interface Statistics and Utilization

NetQ Agents collect performance statistics every 30 seconds for the physical interfaces on switches in your network. The NetQ Agent does not collect statistics for non-physical interfaces, such as bonds, bridges, and VXLANs. The NetQ Agent collects the following statistics:

- Statistics
    - **Transmit**: tx\_bytes, tx\_carrier, tx\_colls, tx\_drop, tx\_errs, tx\_packets
    - **Receive**: rx\_bytes, rx\_drop, rx\_errs, rx\_frame, rx\_multicast, rx\_packets
- Utilization
    - rx\_util, tx\_util
    - port speed

You can view these statistics and utilization data using the NetQ UI or the NetQ CLI.

{{< tabs "TabID89" >}}

{{< tab "NetQ UI" >}}

1. Locate the switch card of interest on your workbench and change to the large size card if needed. Otherwise, open the relevant switch card:

    1. Click {{<img src="https://icons.cumulusnetworks.com/03-Computers-Devices-Electronics/09-Hard-Drives/hard-drive-1.svg" width="18" height="18">}} (Switches), and then select **Open a switch card**.

    2. Begin typing the name of the switch of interest, and select when it appears in the suggestions list.

    3. Select the *Large* card size.

    4. Click **Add**.

2. Hover over the card and click {{<img src="https://icons.cumulusnetworks.com/05-Internet-Networks-Servers/07-Data-Transfer/data-transfer-square-diagonal.svg" width="18" height="18">}} to open the Interface Stats tab.

    {{<figure src="/images/netq/dev-switch-large-interfaces-tab-230.png" width="500">}}

3. Select an interface from the list, scrolling down until you find it. By default the interfaces are sorted by Name, but you may find it easier to sort by the highest transmit or receive utilization using the filter above the list.

    The charts update according to your selection. Scroll up and down to view the individual statistics. Look for high usage, a large number of drops or errors.

What you view next depends on what you see, but a couple of possibilities include:

- Open the full screen card to view details about all of the interfaces on the switch.
- Open another switch card to compare performance on a similar interface.

{{< /tab >}}

{{< tab "NetQ CLI" >}}

To view the interface statistics and utilization, run:

```
netq <hostname> show interface-stats [errors | all] [<physical-port>] [around <text-time>] [json]
netq <hostname> show interface-utilization [<text-port>] [tx|rx] [around <text-time>] [json]
```

Where the various options are:

- `hostname` limits the output to a particular switch
- `errors` limits the output to only the transmit and receive errors found on the designated interfaces
- `physical-port` limits the output to a particular port
- `around` enables viewing of the data at a time in the past
- `json` outputs results in JSON format
- `text-port` limits output to a particular host and port; `hostname` is required with this option
- `tx`, `rx` limits output to the transmit or receive values, respectively

This example shows the interface statistics for the *leaf01* switch for all of its physical interfaces.

```
cumulus@switch:~$ netq leaf01 show interface-stats
Matching proc_dev_stats records:
Hostname          Interface                 RX Packets           RX Drop              RX Errors            TX Packets           TX Drop              TX Errors            Last Updated
----------------- ------------------------- -------------------- -------------------- -------------------- -------------------- -------------------- -------------------- ------------------------
leaf01            swp1                      6147779              0                    0                    6504275              0                    0                    Tue Sep 15 19:01:56 2020
leaf01            swp54                     4325143              1                    0                    4366254              0                    0                    Tue Sep 15 19:01:56 2020
leaf01            swp52                     4415219              1                    0                    4321097              0                    0                    Tue Sep 15 19:01:56 2020
leaf01            swp53                     4298355              1                    0                    4707209              0                    0                    Tue Sep 15 19:01:56 2020
leaf01            swp3                      5489369              1                    0                    5753733              0                    0                    Tue Sep 15 19:01:56 2020
leaf01            swp49                     10325417             0                    0                    10251618             0                    0                    Tue Sep 15 19:01:56 2020
leaf01            swp51                     4498784              1                    0                    4360750              0                    0                    Tue Sep 15 19:01:56 2020
leaf01            swp2                      5697369              0                    0                    5942791              0                    0                    Tue Sep 15 19:01:56 2020
leaf01            swp50                     13885780             0                    0                    13944728             0                    0                    Tue Sep 15 19:01:56 2020
```

This example shows the utilization data for the *leaf03* switch.

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

This example shows only the transmit utilization data for the *border01* switch.

```
cumulus@switch:~$ netq border01 show interface-utilization tx

Matching port_stats records:
Hostname          Interface                 TX Bytes (30sec)     TX Drop (30sec)      TX Errors (30sec)    TX Util (%age)       Port Speed           Last Changed
----------------- ------------------------- -------------------- -------------------- -------------------- -------------------- -------------------- --------------------
border01          swp1                      0                    0                    0                    0                    Unknown              Fri Apr 24 09:33:20
                                                                                                                                                     2020
border01          swp54                     2461                 0                    0                    0                    1G                   Fri Apr 24 09:33:20
                                                                                                                                                     2020
```

{{< /tab >}}

{{< /tabs >}}

### View ACL Resource Utilization

### View Forwarding Resource Utilization

### View SSD Utilization

For NetQ Appliances that have 3ME3 solid state drives (SSDs) installed (primarily in on-premises deployments), you can view the utilization of the drive on-demand. An alarm is generated for drives that drop below 10% health, or have more than a two percent loss of health in 24 hours, indicating the need to rebalance the drive. Tracking SSD utilization over time enables you to see any downward trend or instability of the drive before you receive an alarm.

{{< tabs "TabID368" >}}

{{< tab "NetQ UI" >}}

To view SSD utilization:

1. Open the full screen Switch card and click **SSD Utilization**.

    {{<figure src="/images/netq/dev-switch-fullscr-ssd-tab-241.png" width="700">}}

2. View the average PE Cycles value for a given drive. Is it higher than usual?

3. View the Health value for a given drive. Is it lower than  usual? Less than 10%?

Consider adding the switch cards that are suspect to a workbench for easy tracking.

{{< /tab >}}

{{< tab "NetQ CLI" >}}

To view SDD utilization, run:

```
netq show cl-ssd-util [around <text-time>] [json]
```

This example shows the utilization for *spine02* which has this type of SSD.

```
cumulus@switch:~$ netq spine02 show cl-ssd-util
Hostname        Remaining PE Cycle (%)  Current PE Cycles executed      Total PE Cycles supported       SSD Model               Last Changed
spine02         80                      576                             2880                            M.2 (S42) 3ME3          Thu Oct 31 00:15:06 2019
```

This output indicates that this drive is in a good state overall with 80% of its PE cycles remaining. Use the `around` option to view this information around a particular time in the past.

{{< /tab >}}

{{< /tabs >}}

### View Disk Storage After BTRFS Allocation

Customers running Cumulus Linux 3.x which uses the BTRFS (b-tree file system) might experience issues with disk space management. This is a known problem of BTRFS because it does not perform periodic garbage collection, or rebalancing. If left unattended, these errors can make it impossible to rebalance the partitions on the disk. To avoid this issue, Cumulus Networks recommends rebalancing the BTRFS partitions in a preemptive manner, but only when absolutely needed to avoid reduction in the lifetime of the disk. By tracking the state of the disk space usage, users can determine when rebalancing should be performed.

For details about when a rebalance is recommended, refer to {{<exlink url="https://support.cumulusnetworks.com/hc/en-us/articles/360037394933-When-to-Rebalance-BTRFS-Partitions" text="When to Rebalance BTRFS Partitions">}}.

{{< tabs "TabID414" >}}

{{< tab "NetQ UI" >}}

To view the disk state:

1. Open the full-screen Switch card for a switch of interest:

     - Type the switch name in the Global Search box, then use the card size picker to open the full-screen card, *or* 
     - Click {{<img src="https://icons.cumulusnetworks.com/03-Computers-Devices-Electronics/09-Hard-Drives/hard-drive-1.svg" height="24" width="24">}} (Switches), select **Open a switch card**, enter the switch name and select the full-screen card size.

2. Click **BTRFS Utilization**.

    {{<figure src="/images/netq/dev-switch-fullscr-btrfs-util-tab-241.png" width="700">}}

3. Look for the **Rebalance Recommended** column.

    If the value in that column says *Yes*, then you are strongly encouraged to rebalance the BTRFS partitions. If it says *No*, then you can review the other values in the table to determine if you are getting close to needing a rebalance, and come back to view this table at a later time.

{{< /tab >}}

{{< tab "NetQ CLI" >}}

To view the disk utilization and whether a rebalance is recommended, run:

```
netq show cl-btrfs-util [around <text-time>] [json]
```

This example shows the utilization on the *leaf01* switch:

```
cumulus@switch:~$ netq leaf01 show cl-btrfs-info
Matching btrfs_info records:
Hostname          Device Allocated     Unallocated Space    Largest Chunk Size   Unused Data Chunks S Rebalance Recommende Last Changed
                                                                                 pace                 d
----------------- -------------------- -------------------- -------------------- -------------------- -------------------- -------------------------
leaf01            37.79 %              3.58 GB              588.5 MB             771.91 MB            yes                  Wed Sep 16 21:25:17 2020

```

Look for the **Rebalance Recommended** column. If the value in that column says *Yes*, then you are strongly encouraged to rebalance the BTRFS partitions. If it says *No*, then you can review the other values in the output to determine if you are getting close to needing a rebalance, and come back to view this data at a later time.

Optionally, use the `around` option to view the information for a particular time in the past.

{{< /tab >}}

{{< /tabs >}}

## Physical Sensing

### DOM

### Chassis Sensors

Fan Health
To view the health of fans in your switches, use the `netq show sensors fan` command. If you name the fans in all of your switches consistently, you can view more information at once.

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
### WJH

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