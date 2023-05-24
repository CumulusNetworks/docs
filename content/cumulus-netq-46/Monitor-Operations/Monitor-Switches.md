---
title: Switches
author: NVIDIA
weight: 960
toc: 3
---
With the NetQ UI and NetQ CLI, you can monitor the health of individual switches, including interface performance and resource utilization.

NetQ reports switch performance metrics for the following categories:

- **System configuration**: events, interfaces, IP and MAC addresses, VLANs, IP routes, IP neighbors, and installed software packages
- **Utilization statistics**: CPU, memory, disk, ACL and forwarding resources, SSD, and BTRFS
- **Physical sensing**: digital optics and switch sensors
- **RoCE** and **Precision Time Protocol**

For switch inventory information (ASIC, platform, CPU, memory, disk, and OS), refer to {{<link title="Switch Inventory">}}.

## View Switch Metrics and Attributes in the UI

To view events, metrics, and attributes per switch, open the Switch card:

1. In the header, select {{<img src="/images/netq/devices.svg" height="18" width="18">}} **Devices**, then click **Open a device card**.

2. Select a switch from the list:

    {{<figure src="/images/netq/open-device-dropdown-450.png" alt="dropdown displaying switches" width="300">}}

3. Click **Add**.

4. Adjust the card's size to view information at different levels of granularity. 

Attributes are displayed as the default tab on the large Switch card. You can view the static information about the switch, including its hostname, addresses, server and ASIC vendors and models, OS and NetQ software information. You can also view the state of the interfaces and NetQ Agent on the switch.

{{<figure src="/images/netq/switch-attributes-460.png" alt="large switch card displaying attributes" width="700">}}

Hover over the top of the card, then select the appropriate icon to view utilization info, interface statistics, digital optics info, RoCe metrics, and PTP clock graphs. This example displays utilization information, including CPU, memory, and disk utilization from the past 24 hours:

{{<figure src="/images/netq/device-utilization-460.png" alt="large switch card displaying attributes" width="700">}}

Expand the Switch card to full-screen to view, filter or export information about events, interfaces, MAC addresses, VLANs, IP routes, IP neighbors, IP addresses, BTRFS utilization, software packages, SSD utilization, forwarding resources, ACL resources, What Just Happened events, sensors, RoCE counters, digital optics, and PTP: 

{{<figure src="/images/netq/fullscreen-switch-460.png" width="1200">}}

## Switch Commands

The information available in the UI can also be displayed via the CLI with a corresponding {{<link title="show" text="netq show">}} command. Each command that begins with `netq show` includes the option `<hostname>`. When the `<hostname>` option is included in the command, the output displays results limited to the switch or host you specified.

For example, you can view all events across your network with the {{<link title="show/#netq-show-events" text="netq show events">}} command. To view all events on a particular switch, specify its name in the `<hostname>` field in `netq <hostname> show events`. The following example displays all events on the leaf01 switch:

```
cumulus@switch:~$ netq leaf01 show events

Matching events records:
Hostname          Message Type             Severity         Message                             Timestamp
----------------- ------------------------ ---------------- ----------------------------------- -------------------------
leaf01            btrfsinfo                error            data storage efficiency : space lef Wed Sep  2 20:34:31 2020
                                                            t after allocation greater than chu
                                                            nk size 0.57 GB
leaf01            btrfsinfo                error            data storage efficiency : space lef Wed Sep  2 20:04:30 2020
                                                            t after allocation greater than chu
                                                            nk size 0.57 GB
```

Refer to the command line reference for a comprehensive list of {{<link title="show" text="netq show commands">}}.




<!--the following are UI instructions that need to be incorporated into this page. This documentation was previously in Networkwide Inventory

### View Sensor Information

Fan, power supply unit (PSU), and temperature sensors are available to provide additional data about the NetQ system operation.

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

### View Digital Optics Information


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

-->

