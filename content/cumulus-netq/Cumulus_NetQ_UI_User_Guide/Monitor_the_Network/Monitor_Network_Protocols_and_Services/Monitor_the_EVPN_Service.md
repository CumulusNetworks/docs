---
title: Monitor the EVPN Service
author: Cumulus Networks
weight: 147
aliases:
 - /display/NETQ/Monitor+the+EVPN+Service
 - /pages/viewpage.action?pageId=10456678
pageID: 10456678
product: Cumulus NetQ
version: '2.1'
imgData: cumulus-netq
siteSlug: cumulus-netq
---
The Cumulus NetQ UI enables operators to view the health of the EVPN
service on a network-wide and a per session basis, giving greater
insight into all aspects of the service. This is accomplished through
two card workflows, one for the service and one for the session. They
are described separately here.

## <span>Monitor the EVPN Service (All Sessions)</span>

With NetQ, you can monitor the number of nodes running the EVPN service,
view switches with the sessions, total number of VNIs, and alarms
triggered by the EVPN service. For an overview and how to configure EVPN
in your data center network, refer to [Ethernet Virtual Private Network
- EVPN](/display/NETQ/Ethernet+Virtual+Private+Network+-+EVPN).

### <span>EVPN Service Card Workflow Summary</span>

The small EVPN Service card displays:

{{% imgOld 0 %}}

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Item</p></th>
<th><p>Description</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><span style="color: #333c4e;"> </span></p>
<p>{{% imgOld 1 %}}</p></td>
<td><p>Indicates data is for all sessions of a Network Service or Protocol</p></td>
</tr>
<tr class="even">
<td><p>Title</p></td>
<td><p><strong>EVPN</strong>: All EVPN Sessions, or the EVPN Service</p></td>
</tr>
<tr class="odd">
<td><p>{{% imgOld 2 %}}</p></td>
<td><p>Total number of switches and hosts with the EVPN service enabled during the designated time period</p></td>
</tr>
<tr class="even">
<td><p>{{% imgOld 3 %}}</p></td>
<td><p>Total number of EVPN-related alarms received during the designated time period</p></td>
</tr>
<tr class="odd">
<td><p>Chart</p></td>
<td><p>Distribution of EVPN-related alarms received during the designated time period</p></td>
</tr>
</tbody>
</table>

The medium EVPN Service card displays:

{{% imgOld 4 %}}

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Item</p></th>
<th><p>Description</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Time period</p></td>
<td><p>Range of time in which the displayed data was collected; applies to all card sizes</p></td>
</tr>
<tr class="even">
<td><p><span style="color: #333c4e;"> </span></p>
<p>{{% imgOld 5 %}}</p></td>
<td><p>Indicates data is for all sessions of a Network Service or Protocol</p></td>
</tr>
<tr class="odd">
<td><p>Title</p></td>
<td><p>Network Services | All EVPN Sessions</p></td>
</tr>
<tr class="even">
<td><p>{{% imgOld 6 %}}</p></td>
<td><p>Total number of switches and hosts with the EVPN service enabled during the designated time period</p></td>
</tr>
<tr class="odd">
<td><p>{{% imgOld 7 %}}</p></td>
<td><p>Total number of EVPN-related alarms received during the designated time period</p></td>
</tr>
<tr class="even">
<td><p>Total Nodes Running chart</p></td>
<td><p>Total number and distribution of switches and hosts with the EVPN service enabled during the designated time period</p></td>
</tr>
<tr class="odd">
<td><p>Total Alarms chart</p></td>
<td><p>Total number and distribution of EVPN-related alarms received during the designated time period</p></td>
</tr>
<tr class="even">
<td><p>Total Sessions chart</p></td>
<td><p>Total number and distribution of EVPN sessions network-wide during the designated time period</p></td>
</tr>
</tbody>
</table>

<span style="color: #000000;"> The large EVPN service card contains two
tabs. </span>

<span style="color: #000000;"> </span> <span style="color: #000000;">
The *Sessions Summary* tab which displays: </span>

<span style="color: #000000;"> </span>

{{% imgOld 8 %}}

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Item</p></th>
<th><p>Description</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Time period</p></td>
<td><p>Range of time in which the displayed data was collected; applies to all card sizes</p></td>
</tr>
<tr class="even">
<td><p><span style="color: #333c4e;"> </span></p>
<p>{{% imgOld 9 %}}</p></td>
<td><p>Indicates data is for all sessions of a Network Service or Protocol</p></td>
</tr>
<tr class="odd">
<td><p>Title</p></td>
<td><p>Sessions Summary (visible when you hover over card)</p></td>
</tr>
<tr class="even">
<td><p>{{% imgOld 10 %}}</p></td>
<td><p>Total number of switches and hosts with the EVPN service enabled during the designated time period</p></td>
</tr>
<tr class="odd">
<td><p>{{% imgOld 11 %}}</p></td>
<td><p>Total number of EVPN-related alarms received during the designated time period</p></td>
</tr>
<tr class="even">
<td><p>Total Nodes Running chart</p></td>
<td><p>Total number and distribution of switches and hosts with the EVPN service enabled during the designated time period</p></td>
</tr>
<tr class="odd">
<td><p>Total Sessions chart</p></td>
<td><p>Total number and distribution of EVPN sessions network-wide during the designated time period</p></td>
</tr>
<tr class="even">
<td><p>Total L3 VNIs chart</p></td>
<td><p>Total number and distribution of layer 3 VXLAN Network Identifiers network-wide</p></td>
</tr>
<tr class="odd">
<td><p>Table/Filter options</p></td>
<td><p>When the <strong>Top Switches with Most Sessions</strong> filter is selected, the table displays devices running EVPN sessions in decreasing order of session count—devices with the largest number of sessions are listed first.</p>
<p>When the <strong>Switches with Most L2 EVPN</strong> filter is selected, the table displays devices running layer 2 EVPN sessions in decreasing order of session count—devices with the largest number of sessions are listed first.</p>
<p>When the <strong>Switches with</strong> <strong>Most L3 EVPN</strong> filter is selected, the table displays devices running layer 3 EVPN sessions in decreasing order of session count—devices with the largest number of sessions are listed first.</p></td>
</tr>
<tr class="even">
<td><p>Show All Sessions</p></td>
<td><p>Link to view data for all EVPN sessions network-wide in the full screen card</p></td>
</tr>
</tbody>
</table>

The *Alarms* tab which displays:

{{% imgOld 12 %}}

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Item</p></th>
<th><p>Description</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Time period</p></td>
<td><p>Range of time in which the displayed data was collected; applies to all card sizes</p></td>
</tr>
<tr class="even">
<td><p><span style="color: #333c4e;"> </span></p>
<p>{{% imgOld 13 %}}</p></td>
<td><p>Indicates data is for all sessions of a Network Service or Protocol</p></td>
</tr>
<tr class="odd">
<td><p>Title</p></td>
<td><p>Alarms (visible when you hover over card)</p></td>
</tr>
<tr class="even">
<td><p>{{% imgOld 14 %}}</p></td>
<td><p>Total number of switches and hosts with the EVPN service enabled during the designated time period</p></td>
</tr>
<tr class="odd">
<td><p>{{% imgOld 15 %}}</p></td>
<td><p>Total number of EVPN-related alarms received during the designated time period</p></td>
</tr>
<tr class="even">
<td><p>Total Alarms chart</p></td>
<td><p>Total number and distribution of EVPN-related alarms received during the designated time period</p></td>
</tr>
<tr class="odd">
<td><p>Table/Filter options</p></td>
<td><p>When the <strong>Events by Most Active Device</strong> filter is selected, the table displays devices running EVPN sessions in decreasing order of alarm count—devices with the largest number of alarms are listed first</p></td>
</tr>
<tr class="even">
<td><p>Show All Sessions</p></td>
<td><p>Link to view data for all EVPN sessions in the full screen card</p></td>
</tr>
</tbody>
</table>

<span style="color: #000000;">  
The full screen EVPN Service card provides tabs for all switches, all
sessions, all alarms. </span> <span style="color: #000000;"> </span>

{{% imgOld 16 %}}

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Item</p></th>
<th><p>Description</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Title</p></td>
<td><p>Network Services | EVPN</p></td>
</tr>
<tr class="even">
<td><p>{{% imgOld 17 %}}</p></td>
<td><p>Closes full screen card and returns to workbench</p></td>
</tr>
<tr class="odd">
<td><p>Time period</p></td>
<td><p>Range of time in which the displayed data was collected; applies to all card sizes; select an alternate time period by clicking <span style="color: #353744;"> </span></p>
<p>{{% imgOld 18 %}}</p></td>
</tr>
<tr class="even">
<td><p>Results</p></td>
<td><p>Number of results found for the selected tab</p></td>
</tr>
<tr class="odd">
<td><p>All Switches tab</p></td>
<td><p>Displays all switches and hosts running the EVPN service. By default, the device list is sorted by <strong>hostname</strong>. This tab provides the following additional data about each device:</p>
<ul>
<li><p><strong>Agent</strong></p>
<ul>
<li><p>State: Indicates communication state of the NetQ Agent on a given device. Values include Fresh (heard from recently) and Rotten (not heard from recently).</p></li>
<li><p>Version: Software version number of the NetQ Agent on a given device. This should match the version number of the NetQ software loaded on your server or appliance; for example, 2.1.0.</p></li>
</ul></li>
<li><p><strong>ASIC</strong></p>
<ul>
<li><p>Core BW: Maximum sustained/rated bandwidth. Example values include 2.0 T and 720 G.</p></li>
<li><p>Model: Chip family. Example values include Tomahawk, Trident, and Spectrum.</p></li>
<li><p>Model Id: Identifier of networking ASIC model. Example values include <span style="color: #222222;"> BCM56960 and BCM56854. </span></p></li>
<li><p>Ports: Indicates port configuration of the switch. Example values include <span style="color: #222222;"> 32 x 100G-QSFP28, 48 x 10G-SFP+, and 6 x 40G-QSFP+. </span></p></li>
<li><p>Vendor: Manufacturer of the chip. Example values include Broadcom and Mellanox.</p></li>
</ul></li>
<li><p><strong>CPU</strong></p>
<ul>
<li><p>Arch: Microprocessor architecture type. Values include x86_64 (Intel), ARMv7 (AMD), and PowerPC.</p></li>
<li><p>Max Freq: Highest rated frequency for CPU. Example values include <span style="color: #222222;"> 2.40 GHz and 1.74 GHz. </span></p></li>
<li><p>Model: Chip family. Example values include <span style="color: #222222;"> Intel Atom C2538 and Intel Atom C2338. </span></p></li>
<li><p>Nos: Number of cores. Example values include 2, 4, and 8.</p></li>
</ul></li>
<li><p><strong>Disk Total Size</strong>: Total amount of storage space in physical disks (not total available). Example values: 10 GB, 20 GB, 30 GB.</p></li>
<li><p><strong>License State</strong>: Indicator of validity. Values include ok and bad.</p></li>
<li><p><strong>Memory Size</strong>: Total amount of local RAM. Example values include 8192 MB and 2048 MB.</p></li>
<li><p><strong>OS</strong></p>
<ul>
<li><p>Vendor: Operating System manufacturer. Values include Cumulus Networks, RedHat, Ubuntu, and CentOS.</p></li>
<li><p>Version: Software version number of the OS. Example values include 3.7.3, 2.5.x, 16.04, 7.1.</p></li>
<li><p>Version Id: Identifier of the OS version. For Cumulus, this is the same as the <em>Version</em> (3.7.x).</p></li>
</ul></li>
<li><p><strong>Platform</strong></p>
<ul>
<li><p>Date: Date and time the platform was manufactured. Example values include 7/12/18 and 10/29/2015.</p></li>
<li><p>MAC: System MAC address. Example value: <span style="color: #545454;"> 17:01:AB:EE:C3:F5. </span></p></li>
<li><p>Model: <span style="color: #222222;"> Manufacturer's model name. Examples include AS7712-32X and S4048-ON. </span></p></li>
<li><p>Number: Manufacturer part number. Examples values include FP3ZZ7632014A, 0J09D3.</p></li>
<li><p>Revision: Release version of the platform</p></li>
<li><p>Series: Manufacturer serial number. Example values include D2060B2F044919GD000060, CN046MRJCES0085E0004.</p></li>
<li><p>Vendor: Manufacturer of the platform. Example values include Cumulus Express, Dell, EdgeCore, Lenovo, Mellanox.</p></li>
</ul></li>
<li><p><strong>Time:</strong> Date and time the data was collected from device.</p></li>
</ul></td>
</tr>
<tr class="even">
<td><p>All Sessions tab</p></td>
<td><p>Displays all EVPN sessions network-wide. By default, the session list is sorted by <strong>hostname</strong>. This tab provides the following additional data about each session:</p>
<ul>
<li><p><strong>Adv All Vni</strong>: Indicates whether the VNI state is advertising all VNIs (true) or not (false)</p></li>
<li><p><strong>Adv Gw Ip</strong>: Indicates whether the host device is advertising the gateway IP address (true) or not (false)</p></li>
<li><p><strong>DB State</strong>: Session state of the DB</p></li>
<li><p><strong>Export RT</strong>: IP address and port of the export route target used in the filtering mechanism for BGP route exchange</p></li>
<li><p><strong>Import RT</strong>: IP address and port of the import route target used in the filtering mechanism for BGP route exchange</p></li>
<li><p><strong>In Kernel</strong>: Indicates whether the associated VNI is in the kernel (in kernel) or not (not in kernel)</p></li>
<li><p><strong>Is L3</strong>: Indicates whether the session is part of a layer 3 configuration (true) or not (false)</p></li>
<li><p><strong>Origin Ip</strong>: Host device's local VXLAN tunnel IP address for the EVPN instance</p></li>
<li><p><strong>OPID</strong>: LLDP service identifier</p></li>
<li><p><strong>Rd</strong>: Route distinguisher used in the filtering mechanism for BGP route exchange</p></li>
<li><p><strong>Timestamp</strong>: Date and time the session was started, deleted, updated or marked as dead (device is down)</p></li>
<li><p><strong>Vni</strong>: Name of the VNI where session is running</p></li>
</ul></td>
</tr>
<tr class="odd">
<td><p>All Alarms tab</p></td>
<td><p>Displays all EVPN events network-wide. By default, the event list is sorted by <strong>time</strong>, with the most recent events listed first. The tab provides the following additional data about each event:</p>
<ul>
<li><p><strong>Message</strong>: Text description of a EVPN-related event. Example: VNI 3 kernel state changed from down to up</p></li>
<li><p><strong>Source</strong>: Hostname of network device that generated the event</p></li>
<li><p><strong>Severity</strong>: Importance of the event. Values include critical, warning, info, and debug.</p></li>
<li><p><strong>Type</strong>: Network protocol or service generating the event. This always has a value of <em>evpn</em> in this card workflow.</p></li>
</ul></td>
</tr>
<tr class="even">
<td><p>Export</p></td>
<td><p>Enables export of all or selected items in a CSV or JSON formatted file</p></td>
</tr>
<tr class="odd">
<td><p><span style="color: #353744;"> </span></p>
<p>{{% imgOld 19 %}}</p></td>
<td><p>Enables manipulation of table display; choose columns to display and reorder columns</p></td>
</tr>
</tbody>
</table>

### <span>View Service Status Summary</span>

A summary of the EVPN service is available from the Network Services
card workflow, including the number of nodes running the service, the
number of EVPN-related alarms, and a distribution of those alarms.

To view the summary, open the small EVPN Network Service card.

{{% imgOld 20 %}}

For more detail, select a different size EVPN Network Service card.

### <span>View the Distribution of Sessions and Alarms</span>

It is useful to know the number of network nodes running the EVPN
protocol over a period of time, as it gives you insight into the amount
of traffic associated with and breadth of use of the protocol. It is
also useful to compare the number of nodes running EVPN with the alarms
present at the same time to determine if there is any correlation
between the issues and the ability to establish an EVPN session.

To view these distributions, open the medium EVPN Service card.

{{% imgOld 21 %}}

If a visual correlation is apparent, you can dig a little deeper with
the large EVPN Service card tabs.

### <span>View the Distribution of Layer 3 VNIs </span>

It is useful to know the number of layer 3 VNIs, as it gives you insight
into the complexity of the VXLAN.

To view this distribution, open the large EVPN Service card and view the
bottom chart on the left.

{{% imgOld 22 %}}

### <span>View Devices with the Most EVPN Sessions</span>

You can view the load from EVPN on your switches and hosts using the
large EVPN Service card. This data enables you to see which switches are
handling the most EVPN traffic currently, validate that is what is
expected based on your network design, and compare that with data from
an earlier time to look for any differences.

To view switches and hosts with the most EVPN sessions:

1.  Open the large EVPN Service card.

2.  Select **TOP** **SWITCHES WITH MOST SESSIONS** from the filter above
    the table.  
    The table content is sorted by this characteristic, listing nodes
    running the most EVPN sessions at the top. Scroll down to view those
    with the fewest sessions.
    
    {{% imgOld 23 %}}

To compare this data with the same data at a previous time:
<span style="color: #000000;"> </span>

1.  Open another large EVPN Service card.

2.  Move the new card next to the original card if needed.

3.  Change the time period for the data on the new card by hovering over
    the card and clicking <span style="color: #353744;"> </span>
    
    {{% imgOld 24 %}}
    
    .

4.  Select the time period that you want to compare with the current
    time.  
    You can now see whether there are significant differences between
    this time period and the previous time period.  
    
    {{% imgOld 25 %}}
    
    {{% imgOld 26 %}}

If the changes are unexpected, you can investigate further by looking at
another time frame, determining if more nodes are now running EVPN than
previously, looking for changes in the topology, and so forth.

### <span>View Devices with the Most Layer 2 EVPN Sessions</span>

You can view the number layer 2 EVPN sessions on your switches and hosts
using the large EVPN Service card. This data enables you to see which
switches are handling the most EVPN traffic currently, validate that is
what is expected based on your network design, and compare that with
data from an earlier time to look for any differences.

To view switches and hosts with the most layer 2 EVPN sessions:

1.  Open the large EVPN Service card.

2.  Select **SWITCHES WITH MOST L2 EVPN** from the filter above the
    table.  
    The table content is sorted by this characteristic, listing nodes
    running the most layer 2 EVPN sessions at the top. Scroll down to
    view those with the fewest sessions.
    
    {{% imgOld 27 %}}

To compare this data with the same data at a previous time:

1.  Open another large EVPN Service card.

2.  Move the new card next to the original card if needed.

3.  Change the time period for the data on the new card by hovering over
    the card and clicking
    
    {{% imgOld 28 %}}
    
    .

4.  Select the time period that you want to compare with the current
    time.  
    You can now see whether there are significant differences between
    this time period and the previous time period.  
    
    {{% imgOld 29 %}}
    
    {{% imgOld 30 %}}

If the changes are unexpected, you can investigate further by looking at
another time frame, determining if more nodes are now running EVPN than
previously, looking for changes in the topology, and so forth.

### <span>View Devices with the Most Layer 3 EVPN Sessions</span>

You can view the number layer 3 EVPN sessions on your switches and hosts
using the large EVPN Service card. This data enables you to see which
switches are handling the most EVPN traffic currently, validate that is
what is expected based on your network design, and compare that with
data from an earlier time to look for any differences.

To view switches and hosts with the most layer 3 EVPN sessions:

1.  Open the large EVPN Service card.

2.  Select **SWITCHES WITH MOST L3 EVPN** from the filter above the
    table.  
    The table content is sorted by this characteristic, listing nodes
    running the most layer 3 EVPN sessions at the top. Scroll down to
    view those with the fewest sessions.
    
    {{% imgOld 31 %}}

To compare this data with the same data at a previous time:

1.  Open another large EVPN Service card.

2.  Move the new card next to the original card if needed.

3.  Change the time period for the data on the new card by hovering over
    the card and clicking
    
    {{% imgOld 32 %}}
    
    .

4.  Select the time period that you want to compare with the current
    time.  
    You can now see whether there are significant differences between
    this time period and the previous time period.  
    
    {{% imgOld 33 %}}
    
    {{% imgOld 34 %}}

If the changes are unexpected, you can investigate further by looking at
another time frame, determining if more nodes are now running EVPN than
previously, looking for changes in the topology, and so forth.

### <span id="src-10456678_MonitortheEVPNService-DevMostAlarmsEVPN" class="confluence-anchor-link"></span><span>View Devices with the Most EVPN-related Alarms</span>

Switches experiencing a large number of EVPN alarms may indicate a
configuration or performance issue that needs further investigation. You
can view the switches sorted by the number of BGP alarms and then use
the Switches card workflow or the Alarms card workflow to gather more
information about possible causes for the alarms.

To view switches with the most EVPN alarms:

1.  Open the large EVPN Service card.

2.  Hover over the header and click
    
    {{% imgOld 35 %}}
    
    .

3.  Select **EVENTS BY MOST ACTIVE DEVICE** from the filter above the
    table.  
    The table content is sorted by this characteristic, listing nodes
    with the most EVPN alarms at the top. Scroll down to view those with
    the fewest alarms.
    
    {{% imgOld 36 %}}

Where to go next depends on what data you see, but a few options
include:

  - Hover over the Total Alarms chart to focus on the switches
    exhibiting alarms during that smaller time slice.  
    The table content changes to match the hovered content. Click on the
    chart to persist the table changes.

  - Change the time period for the data to compare with a prior time. If
    the same switches are consistently indicating the most alarms, you
    might want to look more carefully at those switches using the
    Switches card workflow.

  - Click **Show All Sessions** to investigate all EVPN sessions
    network-wide in the full screen card.

### <span>View All EVPN Events</span>

The EVPN Service card workflow enables you to view all of the EVPN
events in the designated time period.

To view all EVPN events:

1.  Open the full screen EVPN Service card.

2.  Click **All Alarms** tab in the navigation panel. By default, events
    are sorted by Time, with most recent events listed first.
    
    {{% imgOld 37 %}}

Where to go next depends on what data you see, but a few options
include:

  - Open one of the other full screen tabs in this flow to focus on
    devices or sessions.

  - Sort by the **Message** or **Severity** to narrow your focus.

  - Export the data for use in another analytics tool, by selecting all
    or some of the events and clicking **Export**.

  - Click
    
    {{% imgOld 38 %}}
    
    at the top right to return to your workbench.

### <span>View Details for All Devices Running EVPN</span>

You can view all stored attributes of all switches running EVPN in your
network in the full screen card.

To view all switch and host details, open the full screen EVPN Service
card, and click the **All Switches** tab.

{{% imgOld 39 %}}

To return to your workbench, click

{{% imgOld 40 %}}

at the top right.

### <span>View Details for All EVPN Sessions</span>

You can view all stored attributes of all EVPN sessions in your network
in the full screen card.

To view all session details, open the full screen EVPN Service card, and
click the **All Sessions** tab.

{{% imgOld 41 %}}

To return to your workbench, click

{{% imgOld 42 %}}

at the top right.

### <span>Take Actions on Data Displayed in Results List</span>

In the full screen EVPN Service card, you can determine which results
are displayed in the results list, and which are exported.

To take actions on the data, click in the blank column at the very left
of a row. A checkbox appears, selecting that switch, session, or alarm,
and an edit menu is shown at the bottom of the card (shown enlarged
here).

{{% imgOld 43 %}}

{{% imgOld 44 %}}

You can perform the following actions on the results list:

| Option             | Action or Behavior on Click                                                                                         |
| ------------------ | ------------------------------------------------------------------------------------------------------------------- |
| Select All         | Selects all switches, sessions, or alarms in the results list                                                       |
| Clear All          | Clears all existing selections of switches, sessions, or alarms in the results list. This also hides the edit menu. |
| Export Selected    | Opens export options dialog. Exported data includes only the selected data.                                         |
| Show Only Selected | Hide unselected switches, sessions, or alarms.                                                                      |
| Remove Selected    | Remove selected switches, sessions, or alarms from the results list.                                                |

To return to original display of results, refresh the browser.

## <span>Monitor a Single EVPN Session</span>

With NetQ, you can monitor the performance of a single EVPN session,
including the number of associated VNI, VTEPs and type. For an overview
and how to configure EVPN in your data center network, refer to
[Ethernet Virtual Private Network -
EVPN](/display/NETQ/Ethernet+Virtual+Private+Network+-+EVPN).

{{%notice info%}}

To access the single session cards, you must open the full screen EVPN
Service (all sessions) card and click on a session. Close the full
screen card to view the medium single session card.

{{%/notice%}}

### <span>Granularity of Data Shown Based on Time Period</span>

On the medium and large Network Services cards, the status of the runs
is represented in heat maps stacked vertically; one for passing runs,
one for runs with warnings, and one for runs with failures. Depending on
the time period of data on the card, the number of smaller time blocks
used to indicate the status varies. A vertical stack of time blocks, one
from each map, includes the results from all checks during that time.
The results are shown by how saturated the color is for each block. If
all validations during that time period pass, then the top block is 100%
saturated and the warning and failure blocks are zero % saturated. As
warnings and errors increase in saturation, the passing block is
proportionally reduced in saturation. The maps are divided into regions.
The number of blocks in a region varies with the time period as well. An
example set of heat maps for a time period of 24 hours is shown here
with the most common time periods in the table along with the resulting
time blocks and regions.

{{% imgOld 45 %}}

| Time Period | Number of Runs | Number Time Blocks | Amount of Time in Each Block | Region Size | Number Blocks per Region | Total Number of Regions |
| ----------- | -------------- | ------------------ | ---------------------------- | ----------- | ------------------------ | ----------------------- |
| 15 minutes  | 5              | 15                 | 1 minute                     | 3 minutes   | 3                        | 5                       |
| 1 hour      | 15             | 12                 | 5 minutes                    | 15 minutes  | 3                        | 4                       |
| 6 hours     | 18             | 12                 | 30 minutes                   | 1 hour      | 2                        | 6                       |
| 24 hours    | 72             | 24                 | 1 hour                       | 6 hours     | 6                        | 4                       |
| 1 week      | 504            | 14                 | 12 hours                     | 1 day       | 2                        | 7                       |
| 1 month     | 2,086          | 28                 | 1 day                        | 1 week      | 7                        | 4                       |
| 1 quarter   | 7,000          | 13                 | 1 week                       | 1 week      | 1                        | 13                      |
| 1 year      | 26,000         | 52                 | 1 week                       | 4 weeks     | 4                        |                         |

### <span>EVPN Session Card Workflow Summary</span>

The small EVPN Session card displays:

{{% imgOld 46 %}}

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Item</p></th>
<th><p>Description</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><span style="color: #222222;"> </span></p>
<p>{{% imgOld 47 %}}</p></td>
<td><p>Indicates data is for an EVPN session</p></td>
</tr>
<tr class="even">
<td><p>Title</p></td>
<td><p>EVPN Session</p></td>
</tr>
<tr class="odd">
<td><p>VNI Name</p></td>
<td><p>Name of the VNI (virtual network instance) used for this EVPN session</p></td>
</tr>
<tr class="even">
<td><p>Current VNI Nodes</p></td>
<td><p>Total number of devices participating in the EVPN session during the designated time period</p></td>
</tr>
</tbody>
</table>

The medium EVPN Session card displays:

{{% imgOld 48 %}}

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Item</p></th>
<th><p>Description</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Time period</p></td>
<td><p>Range of time in which the displayed data was collected; applies to all card sizes</p></td>
</tr>
<tr class="even">
<td><p><span style="color: #222222;"> </span></p>
<p>{{% imgOld 49 %}}</p></td>
<td><p>Indicates data is for an EVPN session</p></td>
</tr>
<tr class="odd">
<td><p>Title</p></td>
<td><p>Network Services | EVPN Session</p></td>
</tr>
<tr class="even">
<td><p>Summary bar</p></td>
<td><p>VTEP ( <span style="color: #353744;"> VXLAN Tunnel EndPoint) </span> Count: Total number of VNI devices participating in the EVPN session during the designated time period</p></td>
</tr>
<tr class="odd">
<td><p>VTEP Count Over Time chart</p></td>
<td><p>Distribution of VTEP counts during the designated time period</p></td>
</tr>
<tr class="even">
<td><p>VNI Name</p></td>
<td><p>Name of the VNI used for this EVPN session</p></td>
</tr>
<tr class="odd">
<td><p>Type</p></td>
<td><p>Indicates whether the session is established as part of a layer 2 or layer 3 overlay network</p></td>
</tr>
</tbody>
</table>

<span style="color: #000000;"> The large EVPN Session card contains one
tab. </span>

<span style="color: #000000;"> The *Session Summary* tab displays:
</span>

<span style="color: #000000;"> </span>

{{% imgOld 50 %}}

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Item</p></th>
<th><p>Description</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Time period</p></td>
<td><p>Range of time in which the displayed data was collected; applies to all card sizes</p></td>
</tr>
<tr class="even">
<td><p><span style="color: #222222;"> </span></p>
<p>{{% imgOld 51 %}}</p></td>
<td><p>Indicates data is for an EVPN session</p></td>
</tr>
<tr class="odd">
<td><p>Title</p></td>
<td><p>Session Summary (Network Services | EVPN Session)</p></td>
</tr>
<tr class="even">
<td><p>Summary bar</p></td>
<td><p>VTEP ( <span style="color: #353744;"> VXLAN Tunnel EndPoint) </span> Count: Total number of VNI devices participating in the EVPN session during the designated time period</p></td>
</tr>
<tr class="odd">
<td><p>VTEP Count Over Time chart</p></td>
<td><p>Distribution of VTEP counts during the designated time period</p></td>
</tr>
<tr class="even">
<td><p>Table</p></td>
<td><p>VRF (for layer 3) or VLAN (for layer 2) identifiers by device</p></td>
</tr>
</tbody>
</table>

<span style="color: #000000;"> The full screen EVPN Session card
provides tabs for all EVPN sessions and all events. </span>
<span style="color: #000000;"> </span>

<span style="color: #000000;"> </span>

{{% imgOld 52 %}}

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Item</p></th>
<th><p>Description</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Title</p></td>
<td><p>Network Services | EVPN</p></td>
</tr>
<tr class="even">
<td><p>{{% imgOld 53 %}}</p></td>
<td><p>Closes full screen card and returns to workbench</p></td>
</tr>
<tr class="odd">
<td><p>Time period</p></td>
<td><p>Range of time in which the displayed data was collected; applies to all card sizes; select an alternate time period by clicking <span style="color: #353744;"> </span></p>
<p>{{% imgOld 54 %}}</p></td>
</tr>
<tr class="even">
<td><p>Results</p></td>
<td><p>Number of results found for the selected tab</p></td>
</tr>
<tr class="odd">
<td><p>All EVPN Sessions tab</p></td>
<td><p>Displays all EVPN sessions network-wide. By default, the session list is sorted by <strong>hostname</strong>. This tab provides the following additional data about each session:</p>
<ul>
<li><p><strong>Adv All Vni</strong>: Indicates whether the VNI state is advertising all VNIs (true) or not (false)</p></li>
<li><p><strong>Adv Gw Ip</strong>: Indicates whether the host device is advertising the gateway IP address (true) or not (false)</p></li>
<li><p><strong>DB State</strong>: Session state of the DB</p></li>
<li><p><strong>Export RT</strong>: IP address and port of the export route target used in the filtering mechanism for BGP route exchange</p></li>
<li><p><strong>Import RT</strong>: IP address and port of the import route target used in the filtering mechanism for BGP route exchange</p></li>
<li><p><strong>In Kernel</strong>: Indicates whether the associated VNI is in the kernel (in kernel) or not (not in kernel)</p></li>
<li><p><strong>Is L3</strong>: Indicates whether the session is part of a layer 3 configuration (true) or not (false)</p></li>
<li><p><strong>Origin Ip</strong>: Host device's local VXLAN tunnel IP address for the EVPN instance</p></li>
<li><p><strong>OPID</strong>: LLDP service identifier</p></li>
<li><p><strong>Rd</strong>: Route distinguisher used in the filtering mechanism for BGP route exchange</p></li>
<li><p><strong>Timestamp</strong>: Date and time the session was started, deleted, updated or marked as dead (device is down)</p></li>
<li><p><strong>Vni</strong>: Name of the VNI where session is running</p></li>
</ul></td>
</tr>
<tr class="even">
<td><p>All Events tab</p></td>
<td><p>Displays all events network-wide. By default, the event list is sorted by <strong>time</strong>, with the most recent events listed first. The tab provides the following additional data about each event:</p>
<ul>
<li><p><strong>Message</strong>: Text description of a EVPN-related event. Example: VNI 3 kernel state changed from down to up</p></li>
<li><p><strong>Source</strong>: Hostname of network device that generated the event</p></li>
<li><p><strong>Severity</strong>: Importance of the event. Values include critical, warning, info, and debug.</p></li>
<li><p><strong>Type</strong>: Network protocol or service generating the event. This always has a value of <em>evpn</em> in this card workflow.</p></li>
</ul></td>
</tr>
<tr class="odd">
<td><p>Export</p></td>
<td><p>Enables export of all or selected items in a CSV or JSON formatted file</p></td>
</tr>
<tr class="even">
<td><p><span style="color: #353744;"> </span></p>
<p>{{% imgOld 55 %}}</p></td>
<td><p>Enables manipulation of table display; choose columns to display and reorder columns</p></td>
</tr>
</tbody>
</table>

### <span>View Session Status Summary</span>

A summary of the <span style="color: #000000;"> EVPN </span> session is
available from the <span style="color: #000000;"> EVPN </span> Session
card workflow, showing the node and its peer and current status.

To view the summary:

1.  Add the Network Services | All EVPN Sessions card.

2.  Switch to the full screen card.

3.  Click the **All Sessions** tab.

4.  Double-click the session of interest. The full screen card closes
    automatically.

5.  Optionally, switch to the small EVPN Session card.  
    
    {{% imgOld 56 %}}
    
    {{% imgOld 57 %}}

For more detail, select a different size <span style="color: #000000;">
EVPN </span> Session card.

### <span>View VTEP Count </span>

You can view the count of VTEPs for a given
<span style="color: #000000;"> EVPN </span> session from the medium and
large <span style="color: #000000;"> EVPN </span> Session cards.

To view the count for a given EVPN session, on the *medium* EVPN Session
card:

1.  Add the Network Services | All EVPN Sessions card.

2.  Switch to the full screen card.

3.  Click the **All Sessions** tab.

4.  Double-click the session of interest. The full screen card closes
    automatically.
    
    {{% imgOld 58 %}}

To view the count for a given EVPN session on the *large* EVPN Session
card, follow the same steps as for the medium card and then switch to
the large card.

{{% imgOld 59 %}}

### <span>View All EVPN Session Details</span>

<span style="color: #000000;"> You can view all stored attributes of all
of the EVPN sessions running network-wide. </span>

To view all session details, open the full screen
<span style="color: #000000;"> EVPN </span> Session card and click the
**All <span style="color: #000000;"> EVPN </span> Sessions** tab.

{{% imgOld 60 %}}

To return to your workbench, click

{{% imgOld 61 %}}

in the top right of the card.

### <span>View All Events</span>

<span style="color: #000000;"> You can view all of the alarm and info
events occurring network wide. </span>

<span style="color: #000000;"> To view all events, o </span> pen the
full screen <span style="color: #000000;"> EVPN </span> Session card and
click the **All Events** tab.

{{% imgOld 62 %}}

Where to go next depends on what data you see, but a few options
include:

  - Open one of the other full screen tabs in this flow to focus on
    sessions.

  - Sort by the **Message** or **Severity** to narrow your focus.

  - Export the data for use in another analytics tool, by selecting all
    or some of the events and clicking **Export**.

  - Click
    
    {{% imgOld 63 %}}
    
    at the top right to return to your workbench.
