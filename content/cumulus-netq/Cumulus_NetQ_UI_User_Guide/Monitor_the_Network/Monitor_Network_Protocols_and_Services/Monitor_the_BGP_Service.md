---
title: Monitor the BGP Service
author: Cumulus Networks
weight: 145
aliases:
 - /display/NETQ/Monitor+the+BGP+Service
 - /pages/viewpage.action?pageId=10456618
pageID: 10456618
product: Cumulus NetQ
version: '2.1'
imgData: cumulus-netq
siteSlug: cumulus-netq
---
The Cumulus NetQ UI enables operators to view the health of the BGP
service on a network-wide and a per session basis, giving greater
insight into all aspects of the service. This is accomplished through
two card workflows, one for the service and one for the session. They
are described separately here.

## <span>Monitor the BGP Service (All Sessions)</span>

With NetQ, you can monitor the number of nodes running the BGP service,
view switches with the most established and unestablished BGP sessions,
and view alarms triggered by the BGP service. For an overview and how to
configure BGP to run in your data center network, refer to [Border
Gateway Protocol - BGP](/display/NETQ/Border+Gateway+Protocol+-+BGP).

### <span>BGP Service Card Workflow</span>

The small BGP Service card displays:

{{% imgOld 0 %}}

{{% imgOld 1 %}}

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
<p>{{% imgOld 2 %}}</p></td>
<td><p>Indicates data is for all sessions of a Network Service or Protocol</p></td>
</tr>
<tr class="even">
<td><p>Title</p></td>
<td><p><strong>BGP</strong>: All BGP Sessions, or the BGP Service</p></td>
</tr>
<tr class="odd">
<td><p>{{% imgOld 3 %}}</p></td>
<td><p>Total number of switches and hosts with the BGP service enabled during the designated time period</p></td>
</tr>
<tr class="even">
<td><p>{{% imgOld 4 %}}</p></td>
<td><p>Total number of BGP-related alarms received during the designated time period</p></td>
</tr>
<tr class="odd">
<td><p>Chart</p></td>
<td><p>Distribution of BGP-related alarms received during the designated time period</p></td>
</tr>
</tbody>
</table>

The medium BGP Service card displays:

<span style="color: #ff0000;"> </span>

{{% imgOld 5 %}}

{{% imgOld 6 %}}

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
<p>{{% imgOld 7 %}}</p></td>
<td><p>Indicates data is for all sessions of a Network Service or Protocol</p></td>
</tr>
<tr class="odd">
<td><p>Title</p></td>
<td><p>Network Services | All BGP Sessions</p></td>
</tr>
<tr class="even">
<td><p>{{% imgOld 8 %}}</p></td>
<td><p>Total number of switches and hosts with the BGP service enabled during the designated time period</p></td>
</tr>
<tr class="odd">
<td><p>{{% imgOld 9 %}}</p></td>
<td><p>Total number of BGP-related alarms received during the designated time period</p></td>
</tr>
<tr class="even">
<td><p>Total Nodes Running chart</p></td>
<td><p>Total number and distribution of switches and hosts with the BGP service enabled during the designated time period</p></td>
</tr>
<tr class="odd">
<td><p>Total Alarms chart</p></td>
<td><p>Total number and distribution of BGP-related alarms received during the designated time period</p></td>
</tr>
<tr class="even">
<td><p>Total Nodes Not Est. chart</p></td>
<td><p>Total number and distribution of switches and hosts with unestablished BGP sessions during the designated time period</p></td>
</tr>
</tbody>
</table>

<span style="color: #000000;"> The large BGP service card contains two
tabs. </span>

<span style="color: #000000;"> The *Sessions Summary* tab displays:  
</span>

{{% imgOld 10 %}}

{{% imgOld 11 %}}

  

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
<p>{{% imgOld 12 %}}</p></td>
<td><p>Indicates data is for all sessions of a Network Service or Protocol</p></td>
</tr>
<tr class="odd">
<td><p>Title</p></td>
<td><p>Sessions Summary (visible when you hover over card)</p></td>
</tr>
<tr class="even">
<td><p>{{% imgOld 13 %}}</p></td>
<td><p>Total number of switches and hosts with the BGP service enabled during the designated time period</p></td>
</tr>
<tr class="odd">
<td><p>{{% imgOld 14 %}}</p></td>
<td><p>Total number of BGP-related alarms received during the designated time period</p></td>
</tr>
<tr class="even">
<td><p>Total Nodes Running chart</p></td>
<td><p>Total number and distribution of switches and hosts with the BGP service enabled</p></td>
</tr>
<tr class="odd">
<td><p>Total Nodes Not Est. chart</p></td>
<td><p>Total number and distribution of switches and hosts with unestablished BGP sessions during the designated time period</p></td>
</tr>
<tr class="even">
<td><p>Table/Filter options</p></td>
<td><p>When the <strong>Switches with Most Sessions</strong> filter option is selected, the table displays the switches and hosts running BGP sessions in decreasing order of session count—devices with the largest number of sessions are listed first</p>
<p>When the <strong>Switches with Most Unestablished Sessions</strong> filter option is selected, the table switches and hosts running BGP sessions in decreasing order of unestablished sessions—devices with the largest number of unestablished sessions are listed first</p></td>
</tr>
<tr class="odd">
<td><p>Show All Sessions</p></td>
<td><p>Link to view data for all BGP sessions in the full screen card</p></td>
</tr>
</tbody>
</table>

The *Alarms* tab displays:

{{% imgOld 15 %}}

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
<p>{{% imgOld 16 %}}</p></td>
<td><p>Indicates data is for all sessions of a Network Service or Protocol</p></td>
</tr>
<tr class="odd">
<td><p>Title</p></td>
<td><p>Alarms (visible when you hover over card)</p></td>
</tr>
<tr class="even">
<td><p>{{% imgOld 17 %}}</p></td>
<td><p>Total number of switches and hosts with the BGP service enabled during the designated time period</p></td>
</tr>
<tr class="odd">
<td><p>{{% imgOld 18 %}}</p></td>
<td><p>Total number of BGP-related alarms received during the designated time period</p></td>
</tr>
<tr class="even">
<td><p>Total Alarms chart</p></td>
<td><p>Total number and distribution of BGP-related alarms received during the designated time period</p></td>
</tr>
<tr class="odd">
<td><p>Table/Filter options</p></td>
<td><p>When the selected filter option is <strong>Switches with Most Alarms</strong>, the table displays <strong></strong> switches and hosts running BGP in decreasing order of the count of alarms—devices with the largest number of BGP alarms are listed first</p></td>
</tr>
<tr class="even">
<td><p>Show All Sessions</p></td>
<td><p>Link to view data for all BGP sessions in the full screen card</p></td>
</tr>
</tbody>
</table>

The full screen BGP Service card provides tabs for all switches, all
sessions, and all alarms.

{{% imgOld 19 %}}

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
<td><p>Network Services | BGP</p></td>
</tr>
<tr class="even">
<td><p>{{% imgOld 20 %}}</p></td>
<td><p>Closes full screen card and returns to workbench</p></td>
</tr>
<tr class="odd">
<td><p>Time period</p></td>
<td><p>Range of time in which the displayed data was collected; applies to all card sizes; select an alternate time period by clicking <span style="color: #353744;"> </span></p>
<p>{{% imgOld 21 %}}</p></td>
</tr>
<tr class="even">
<td><p>Results</p></td>
<td><p>Number of results found for the selected tab</p></td>
</tr>
<tr class="odd">
<td><p>All Switches tab</p></td>
<td><p>Displays all switches and hosts running the BGP service. By default, the device list is sorted by <strong>hostname</strong>. This tab provides the following additional data about each device:</p>
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
<li><p><strong>OS</strong></p></li>
<li><ul>
<li><p>Vendor: Operating System manufacturer. Values include Cumulus Networks, RedHat, Ubuntu, and CentOS.</p></li>
<li><p>Version: Software version number of the OS. Example values include 3.7.3, 2.5.x, 16.04, 7.1.</p></li>
<li><p>Version Id: Identifier of the OS version. For Cumulus, this is the same as the <em>Version</em> (3.7.x).</p></li>
</ul></li>
<li><p><strong>Platform</strong></p>
<ul>
<li><p>Date: Date and time the platform was manufactured. Example values include 7/12/18 and 10/29/2015.</p></li>
<li><p>MAC: System MAC address. Example value: <span style="color: #545454;"> 17:01:AB:EE:C3:F5. </span></p></li>
<li><p>Model: <span style="color: #222222;"> Manufacturer's model name. Examples values include AS7712-32X and S4048-ON. </span></p></li>
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
<td><p>Displays all BGP sessions network-wide. By default, the session list is sorted by <strong>hostname</strong>. This tab provides the following additional data about each session:</p>
<ul>
<li><p><strong>ASN</strong>: Autonomous System Number, identifier for a collection of IP networks and routers. Example values include 633284,655435.</p></li>
<li><p><strong>Conn Dropped</strong>: Number of dropped connections for a given session</p></li>
<li><p><strong>Conn Estd</strong>: Number of connections established for a given session</p></li>
<li><p><strong>DB State</strong>: Session state of DB</p></li>
<li><p><strong>Evpn Pfx Rcvd</strong>: Address prefix received for EVPN traffic. Examples include 115, 35.</p></li>
<li><p><strong>Ipv4, and Ipv6 Pfx Rcvd</strong>: Address prefix received for IPv4 or IPv6 traffic. Examples include 31, 14, 12.</p></li>
<li><p><strong>Last Reset Time</strong>: Date and time at which the session was last established or reset</p></li>
<li><p><strong>Objid</strong>: Object identifier for service</p></li>
<li><p><strong>OPID</strong>: Customer identifier. This is always zero.</p></li>
<li><p><strong>Peer</strong></p>
<ul>
<li><p>ASN: Autonomous System Number for peer device</p></li>
<li><p>Hostname: User-defined name for peer device</p></li>
<li><p>Name: Interface name or hostname of peer device</p></li>
<li><p>Router Id: IP address of router with access to the peer device</p></li>
</ul></li>
<li><p><strong>Reason</strong>: Text describing the cause of, or trigger for, an event</p></li>
<li><p><strong>Rx and Tx Families</strong>: Address families supported for the receive and transmit session channels. Values include ipv4, ipv6, and evpn.</p></li>
<li><p><strong>State</strong>: Current state of the session. Values include Established and NotEstd (not established).</p></li>
<li><p><strong>Timestamp</strong>: Date and time session was started, deleted, updated or marked dead (device is down)</p></li>
<li><p><strong>Upd8 Rx:</strong> Count of protocol messages received</p></li>
<li><p><strong>Upd8 Tx</strong>: Count of protocol messages transmitted</p></li>
<li><p><strong>Up Time</strong>: Number of seconds the session has been established, in EPOCH notation. Example: 1550147910000</p></li>
<li><p><strong>Vrf</strong>: Name of the Virtual Route Forwarding interface. Examples: default, mgmt, DataVrf1081</p></li>
<li><p><strong>Vrfid</strong>: Integer identifier of the VRF interface when used. Examples: 14, 25, 37</p></li>
</ul></td>
</tr>
<tr class="odd">
<td><p>All Alarms tab</p></td>
<td><p>Displays all BGP events network-wide. By default, the event list is sorted by <strong>time</strong>, with the most recent events listed first. The tab provides the following additional data about each event:</p>
<ul>
<li><p><strong>Message</strong>: Text description of a BGP-related event. Example: BGP session with peer tor-1 swp7 vrf default state changed from failed to Established</p></li>
<li><p><strong>Source</strong>: Hostname of network device that generated the event</p></li>
<li><p><strong>Severity</strong>: Importance of the event. Values include critical, warning, info, and debug.</p></li>
<li><p><strong>Type</strong>: Network protocol or service generating the event. This always has a value of <em>bgp</em> in this card workflow.</p></li>
</ul></td>
</tr>
<tr class="even">
<td><p>Export</p></td>
<td><p>Enables export of all or selected items in a CSV or JSON formatted file</p></td>
</tr>
<tr class="odd">
<td><p><span style="color: #353744;"> </span></p>
<p>{{% imgOld 22 %}}</p></td>
<td><p>Enables manipulation of table display; choose columns to display and reorder columns</p></td>
</tr>
</tbody>
</table>

### <span>View Service Status Summary</span>

A summary of the BGP service is available from the Network Services card
workflow, including the number of nodes running the service, the number
of BGP-related alarms, and a distribution of those alarms.

To view the summary, open the small BGP Service card.

{{% imgOld 23 %}}

For more detail, select a different size BGP Service card.

### <span>View the Distribution of Sessions and Alarms</span>

It is useful to know the number of network nodes running the BGP
protocol over a period of time, as it gives you insight into the amount
of traffic associated with and breadth of use of the protocol. It is
also useful to compare the number of nodes running BGP with
unestablished sessions with the alarms present at the same time to
determine if there is any correlation between the issues and the ability
to establish a BGP session.

To view these distributions, open the medium BGP Service card.

{{% imgOld 24 %}}

If a visual correlation is apparent, you can dig a little deeper with
the large BGP Service card tabs.

### <span>View Devices with the Most BGP Sessions</span>

You can view the load from BGP on your switches and hosts using the
large Network Services card. This data enables you to see which switches
are handling the most BGP traffic currently, validate that is what is
expected based on your network design, and compare that with data from
an earlier time to look for any differences.

To view switches and hosts with the most BGP sessions:

1.  Open the large BGP Service card.

2.  Select **SWITCHES WITH MOST SESSIONS** from the filter above the
    table.  
    The table content is sorted by this characteristic, listing nodes
    running the most BGP sessions at the top. Scroll down to view those
    with the fewest sessions.
    
    {{% imgOld 25 %}}

To compare this data with the same data at a previous time:

1.  Open another large BGP Service card.

2.  Move the new card next to the original card if needed.

3.  Change the time period for the data on the new card by hovering over
    the card and clicking <span style="color: #353744;"> </span>
    
    {{% imgOld 26 %}}
    
    .

4.  Select the time period that you want to compare with the original
    time. We chose *Past Week* for this example.  
    
    {{% imgOld 27 %}}
    
    {{% imgOld 28 %}}
    
      
    You can now see whether there are significant differences between
    this time and the original time. If the changes are unexpected, you
    can investigate further by looking at another time frame,
    determining if more nodes are now running BGP than previously,
    looking for changes in the topology, and so forth.

### <span>View Devices with the Most Unestablished BGP Sessions</span>

You can identify switches and hosts that are experiencing difficulties
establishing BGP sessions; both currently and in the past.

To view switches with the most unestablished BGP sessions:

1.  Open the large BGP Service card.

2.  Select **SWITCHES WITH MOST UNESTABLISHED SESSIONS** from the filter
    above the table.  
    The table content is sorted by this characteristic, listing nodes
    with the most unestablished BGP sessions at the top. Scroll down to
    view those with the fewest unestablished sessions.
    
    {{% imgOld 29 %}}

Where to go next depends on what data you see, but a couple of options
include:

  - Hover over the **Total Nodes Not Est.** chart to focus on the
    switches and hosts with the most unestablished sessions during that
    smaller time slice.  
    The table content changes to match the hovered content. Click on the
    chart to persist the table changes.
    
    {{% imgOld 30 %}}

  - Change the time period for the data to compare with a prior time.
    
    {{% imgOld 31 %}}
    
    If the same switches are consistently indicating the most
    unestablished sessions, you might want to look more carefully at
    those switches using the Switches card workflow to determine
    probable causes. Refer to [Monitor
    Switches](/cumulus-netq/Cumulus_NetQ_UI_User_Guide/Monitor_Switches).

  - Click **Show All Sessions** to investigate all BGP sessions with
    events in the full screen card.

### <span id="src-10456618_MonitortheBGPService-DevsMostAlarmsBGP" class="confluence-anchor-link"></span><span>View Devices with the Most BGP-related Alarms</span>

Switches or hosts experiencing a large number of BGP alarms may indicate
a configuration or performance issue that needs further investigation.
You can view the devices sorted by the number of BGP alarms and then use
the Switches card workflow or the Alarms card workflow to gather more
information about possible causes for the alarms.

To view switches with the most BGP alarms:

1.  Open the large BGP Service card.

2.  Hover over the header and click
    
    {{% imgOld 32 %}}
    
    .

3.  Select **SWITCHES WITH MOST ALARMS** from the filter above the
    table.  
    The table content is sorted by this characteristic, listing nodes
    with the most BGP alarms at the top. Scroll down to view those with
    the fewest alarms.
    
    {{% imgOld 33 %}}

Where to go next depends on what data you see, but a few options
include:

  - Hover over the Total Alarms chart to focus on the switches
    exhibiting alarms during that smaller time slice.  
    The table content changes to match the hovered content. Click on the
    chart to persist the table changes.
    
    {{% imgOld 34 %}}

  - Change the time period for the data to compare with a prior time. If
    the same switches are consistently indicating the most alarms, you
    might want to look more carefully at those switches using the
    Switches card workflow.  
    
    {{% imgOld 35 %}}
    
    {{% imgOld 36 %}}
    
      
    In this example, the total alarm count has reduced significantly
    from one week ago.

  - Click **Show All Sessions** to investigate all BGP sessions with
    events in the full screen card.

### <span>View All BGP Events</span>

The BGP Network Services card workflow enables you to view all of the
BGP events in the designated time period.

To view all BGP events:

1.  Open the full screen BGP Service card.

2.  Click **All Alarms** tab in the navigation panel.  
    By default, events are listed in most recent to least recent order.
    
    {{% imgOld 37 %}}

Where to go next depends on what data you see, but a couple of options
include:

  - Open one of the other full screen tabs in this flow to focus on
    devices or sessions.

  - Export the data for use in another analytics tool, by clicking
    **Export** and providing a name for the data file.

### <span>View Details for All Devices Running BGP</span>

You can view all stored attributes of all switches and hosts running BGP
in your network in the full screen card.

To view all device details, open the full screen BGP Service card and
click the **All Switches** tab.

{{% imgOld 38 %}}

To return to your workbench, click

{{% imgOld 39 %}}

in the top right corner.

### <span>View Details for All BGP Sessions</span>

You can view all stored attributes of all BGP sessions in your network
in the full-screen card.

To view all session details, open the full screen BGP Service card and
click the **All Sessions** tab.

{{% imgOld 40 %}}

To return to your workbench, click

{{% imgOld 41 %}}

in the top right corner.

### <span>Take Actions on Data Displayed in Results List</span>

In the full screen BGP Service card, you can determine which results are
displayed in the results list, and which are exported.

To take actions on the data, click in the blank column at the very left
of a row. A checkbox appears, selecting that switch, session, or alarm,
and an edit menu is shown at the bottom of the card (shown enlarged
here).

{{% imgOld 42 %}}

{{% imgOld 43 %}}

You can perform the following actions on the results list:

| Option             | Action or Behavior on Click                                                                                         |
| ------------------ | ------------------------------------------------------------------------------------------------------------------- |
| Select All         | Selects all switches, sessions, or alarms in the results list                                                       |
| Clear All          | Clears all existing selections of switches, sessions, or alarms in the results list. This also hides the edit menu. |
| Export Selected    | Opens export options dialog. Exported data includes only the selected data.                                         |
| Show Only Selected | Hide unselected switches, sessions, or alarms.                                                                      |
| Remove Selected    | Remove selected switches, sessions, or alarms from the results list.                                                |

To return to original display of results, refresh the browser.

## <span>Monitor a Single BGP Session</span>

With NetQ, you can monitor a single session of the BGP service, view
session state changes, and compare with alarms occurring at the same
time, as well as monitor the running BGP configuration and changes to
the configuration file. For an overview and how to configure BGP to run
in your data center network, refer to [Border Gateway Protocol -
BGP](/display/NETQ/Border+Gateway+Protocol+-+BGP).

{{%notice info%}}

To access the single session cards, you must open the full screen BGP
Service (all sessions) card and double-click on a session. The full
screen card automatically closes so you can view the medium single
session card.

{{%/notice%}}

### <span id="src-10456618_safe-id-TW9uaXRvcnRoZUJHUFNlcnZpY2UtI1RpbWVQZXJHcmFu" class="confluence-anchor-link"></span><span>Granularity of Data Shown Based on Time Period</span>

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

{{% imgOld 44 %}}

| Time Period | Number of Runs | Number Time Blocks | Amount of Time in Each Block | Region Size | Number Blocks per Region | Total Number of Regions |
| ----------- | -------------- | ------------------ | ---------------------------- | ----------- | ------------------------ | ----------------------- |
| 15 minutes  | 5              | 15                 | 1 minute                     | 3 minutes   | 3                        | 5                       |
| 1 hour      | 15             | 12                 | 5 minutes                    | 15 minutes  | 3                        | 4                       |
| 6 hours     | 18             | 12                 | 30 minutes                   | 1 hour      | 2                        | 6                       |
| 24 hours    | 72             | 24                 | 1 hour                       | 6 hours     | 6                        | 4                       |
| 1 week      | 504            | 14                 | 12 hours                     | 1 day       | 2                        | 7                       |
| 1 month     | 2,086          | 28                 | 1 day                        | 1 week      | 7                        | 4                       |
| 1 quarter   | 7,000          | 13                 | 1 week                       | 1 week      | 1                        | 13                      |
| 1 year      | 26,000         | 52                 | 1 week                       | 4 weeks     | 4                        | 13                      |

### <span>BGP Session Card Workflow Summary</span>

The small BGP Session card displays:

{{% imgOld 45 %}}

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
<p>{{% imgOld 46 %}}</p></td>
<td><p>Indicates data is for a single session of a Network Service or Protocol</p></td>
</tr>
<tr class="even">
<td><p>Title</p></td>
<td><p><strong>BGP Session</strong></p></td>
</tr>
<tr class="odd">
<td><p> </p></td>
<td><p>Hostnames of the two devices in a session. Arrow points from the host to the peer.</p></td>
</tr>
<tr class="even">
<td><p><span style="color: #353744;"> </span></p>
<p>{{% imgOld 47 %}}</p>
, <span style="color: #353744;"> </span>
<p>{{% imgOld 48 %}}</p></td>
<td><p>Current status of the session, either established or not established</p></td>
</tr>
</tbody>
</table>

The medium BGP Session card displays:

{{% imgOld 49 %}}

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
<td><p>{{% imgOld 50 %}}</p></td>
<td><p>Indicates data is for all sessions of a Network Service or Protocol</p></td>
</tr>
<tr class="odd">
<td><p>Title</p></td>
<td><p>Network Services | BGP Session</p></td>
</tr>
<tr class="even">
<td><p> </p></td>
<td><p>Hostnames of the two devices in a session. Arrow points in the direction of the session.</p></td>
</tr>
<tr class="odd">
<td><p><span style="color: #353744;"> </span></p>
<p>{{% imgOld 51 %}}</p>
,
<p>{{% imgOld 52 %}}</p></td>
<td><p>Current status of the session, either established or not established</p></td>
</tr>
<tr class="even">
<td><p>Time period for chart</p></td>
<td><p>Time period for the chart data</p></td>
</tr>
<tr class="odd">
<td><p>Session State Changes Chart</p></td>
<td><p>Heat map of the state of the given session over the given time period. The status is sampled at a rate consistent with the time period. For example, for a 24 hour period, a status is collected every hour. Refer to <a href="#src-10456618_MonitortheBGPService-TimePerGran">Granularity of Data Shown Based on Time Period</a>.</p></td>
</tr>
<tr class="even">
<td><p>Peer Name</p></td>
<td><p>Interface name on or hostname for peer device</p></td>
</tr>
<tr class="odd">
<td><p>Peer ASN</p></td>
<td><p>Autonomous System Number for peer device</p></td>
</tr>
<tr class="even">
<td><p>Peer Router ID</p></td>
<td><p>IP address of router with access to the peer device</p></td>
</tr>
<tr class="odd">
<td><p>Peer Hostname</p></td>
<td><p>User-defined name for peer device</p></td>
</tr>
</tbody>
</table>

<span style="color: #000000;"> The large BGP Session card contains one
tab. </span>

<span style="color: #000000;"> The *Session Summary* tab displays:
</span>

<span style="color: #000000;"> <span style="color: #000000;">
</span></span>

{{% imgOld 53 %}}

Item

Description

Time period

Range of time in which the displayed data was collected; applies to all
card sizes

{{% imgOld 54 %}}

Indicates data is for all sessions of a Network Service or Protocol

Title

Session Summary (Network Services | BGP Session)

Summary bar

Hostnames of the two devices in a session. Arrow points in the direction
of the session.

Current status of the session—either established

{{% imgOld 55 %}}

, or not established

{{% imgOld 56 %}}

Session State Changes Chart

Heat map of the state of the given session over the given time period.
The status is sampled at a rate consistent with the time period. For
example, for a 24 hour period, a status is collected every hour. Refer
to [Granularity of Data Shown Based on Time
Period](#src-10456618_MonitortheBGPService-TimePerGran) .

Connection Drop Count

Number of times the session entered the not established state during the
time period

ASN

Autonomous System Number for host device

RX/TX Families

Receive and Transmit address types supported. Values include IPv4, IPv6,
and EVPN.

Peer Hostname

User-defined name for peer device

Peer Interface

Interface on which the session is connected

Peer ASN

Autonomous System Number for peer device

Peer Router ID

IP address of router with access to the peer device

<span style="color: #000000;"> The full screen BGP Session card provides
tabs for all BGP sessions and all events. </span>

{{% imgOld 57 %}}

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
<td><p>Title</p></td>
<td><p>Network Services | BGP</p></td>
</tr>
<tr class="odd">
<td><p>All BGP Sessions tab</p></td>
<td><p>Displays all BGP sessions running on the host device. This tab provides the following additional data about each session:</p>
<ul>
<li><p><strong>ASN</strong>: Autonomous System Number, identifier for a collection of IP networks and routers. Example values include 633284,655435.</p></li>
<li><p><strong>Conn Dropped</strong>: Number of dropped connections for a given session</p></li>
<li><p><strong>Conn Estd</strong>: Number of connections established for a given session</p></li>
<li><p><strong>DB State</strong>: Session state of DB</p></li>
<li><p><strong>Evpn Pfx Rcvd</strong>: Address prefix for EVPN traffic. Examples include 115, 35.</p></li>
<li><p><strong>Ipv4, and Ipv6 Pfx Rcvd</strong>: Address prefix for IPv4 or IPv6 traffic. Examples include 31, 14, 12.</p></li>
<li><p><strong>Last Reset Time</strong>: Time at which the session was last established or reset</p></li>
<li><p><strong>Objid</strong>: Object identifier for service</p></li>
<li><p><strong>OPID</strong>: Customer identifier. This is always zero.</p></li>
<li><p><strong>Peer</strong></p>
<ul>
<li><p>ASN: Autonomous System Number for peer device</p></li>
<li><p>Hostname: User-defined name for peer device</p></li>
<li><p>Name: Interface name or hostname of peer device</p></li>
<li><p>Router Id: IP address of router with access to the peer device</p></li>
</ul></li>
<li><p><strong>Reason</strong>: Event or cause of failure</p></li>
<li><p><strong>Rx and Tx Families</strong>: Address families supported for the receive and transmit session channels. Values include ipv4, ipv6, and evpn.</p></li>
<li><p><strong>State</strong>: Current state of the session. Values include Established and NotEstd (not established).</p></li>
<li><p><strong>Timestamp</strong>: Date and time session was started, deleted, updated or marked dead (device is down)</p></li>
<li><p><strong>Upd8 Rx:</strong> Count of protocol messages received</p></li>
<li><p><strong>Upd8 Tx</strong>: Count of protocol messages transmitted</p></li>
<li><p><strong>Up Time</strong>: Number of seconds the session has be established, in EPOC notation. Example: 1550147910000</p></li>
<li><p><strong>Vrf</strong>: Name of the Virtual Route Forwarding interface. Examples: default, mgmt, DataVrf1081</p></li>
<li><p><strong>Vrfid</strong>: Integer identifier of the VRF interface when used. Examples: 14, 25, 37</p></li>
</ul></td>
</tr>
<tr class="even">
<td><p>All Events tab</p></td>
<td><p>Displays all events network-wide. By default, the event list is sorted by <strong>time</strong>, with the most recent events listed first. The tab provides the following additional data about each event:</p>
<ul>
<li><p><strong>Message</strong>: Text description of a BGP-related event. Example: BGP session with peer tor-1 swp7 vrf default state changed from failed to Established</p></li>
<li><p><strong>Source</strong>: Hostname of network device that generated the event</p></li>
<li><p><strong>Severity</strong>: Importance of the event. Values include critical, warning, info, and debug.</p></li>
<li><p><strong>Type</strong>: Network protocol or service generating the event. This always has a value of bgp in this card workflow.</p></li>
</ul></td>
</tr>
<tr class="odd">
<td><p>Export</p></td>
<td><p>Enables export of all or selected items in a CSV or JSON formatted file</p></td>
</tr>
<tr class="even">
<td><p><span style="color: #353744;"> </span></p>
<p>{{% imgOld 58 %}}</p></td>
<td><p>Enables manipulation of table display; choose columns to display and reorder columns</p></td>
</tr>
</tbody>
</table>

### <span>View Session Status Summary</span>

A summary of the BGP session is available from the BGP Session card
workflow, showing the node and its peer and current status.

To view the summary:

1.  Add the Network Services | All BGP Sessions card.

2.  Switch to the full screen card.

3.  Click the **All Sessions** tab.

4.  Double-click the session of interest. The full screen card closes
    automatically.

5.  Optionally, switch to the small BGP Session card.  
    
    {{% imgOld 59 %}}
    
    {{% imgOld 60 %}}

### <span>View BGP Session State Changes</span>

You can view the state of a given BGP session from the medium and large
BGP Session Network Service cards. For a given time period, you can
determine the stability of the BGP session between two devices. If you
experienced connectivity issues at a particular time, you can use these
cards to help verify the state of the session. If it was not established
more than it was established, you can then investigate further into
possible causes.

To view the state transitions for a given BGP session, on the *medium*
BGP Session card:

1.  Add the Network Services | All BGP Sessions card.

2.  Switch to the full screen card.

3.  Open the large BGP Service card.

4.  Click the **All Sessions** tab.

5.  Double-click the session of interest. The full screen card closes
    automatically.
    
    {{% imgOld 61 %}}

The heat map indicates the status of the session over the designated
time period. In this example, the session has been established for the
entire time period.

From this card, you can also view the Peer ASN, name, hostname and
router id identifying the session in more detail.

To view the state transitions for a given BGP session on the large BGP
Session card, follow the same steps to open the medium BGP Session card
and then switch to the large card.

{{% imgOld 62 %}}

From this card, you can view the Peer ASN, hostname, and router id, VRF,
and Tx/Rx families identifying the session in more detail. The
Connection Drop Count gives you a sense of the session performance.

### <span>View All BGP Session Details</span>

<span style="color: #000000;"> You can view all stored attributes of all
of the BGP sessions associated with the two devices on this card.
</span>

To view all session details, open the full screen BGP Session card, and
click the **All BGP Sessions** tab.

{{% imgOld 63 %}}

To return to your workbench, click

{{% imgOld 64 %}}

in the top right corner.

### <span>View All Events</span>

<span style="color: #000000;"> You can view all of the alarm and info
events for the two devices on this card. </span>

<span style="color: #000000;"> To view all events, o </span> pen the
full screen BGP Session card, and click the **All Events** tab.

{{% imgOld 65 %}}

To return to your workbench, click

{{% imgOld 66 %}}

in the top right corner.
