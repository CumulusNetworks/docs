---
title: Monitor the MLAG Service
author: Cumulus Networks
weight: 151
aliases:
 - /display/NETQ/Monitor+the+MLAG+Service
 - /pages/viewpage.action?pageId=10456746
pageID: 10456746
product: Cumulus NetQ
version: '2.1'
imgData: cumulus-netq
siteSlug: cumulus-netq
---
The Cumulus NetQ UI enables operators to view the health of the MLAG
service on a network-wide and a per session basis, giving greater
insight into all aspects of the service. This is accomplished through
two card workflows, one for the service and one for the session. They
are described separately here.

{{%notice info%}}

**MLAG or CLAG?**

The Cumulus Linux implementation of MLAG is referred to by other vendors
as CLAG, MC-LAG or VPC. The Cumulus NetQ UI uses the CLAG terminology.

{{%/notice%}}

## <span>Monitor the CLAG Service (All Sessions)</span>

With NetQ, you can monitor the number of nodes running the CLAG service,
view sessions running, and view alarms triggered by the CLAG service.
For an overview and how to configure CLAG in your data center network,
refer to [Multi-Chassis Link Aggregation -
MLAG](/display/NETQ/Multi-Chassis+Link+Aggregation+-+MLAG).

### <span>CLAG Service Card Workflow Summary</span>

The small CLAG Service card displays:

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
<td><p><strong>CLAG</strong>: All CLAG Sessions, or the CLAG Service</p></td>
</tr>
<tr class="odd">
<td><p>{{% imgOld 2 %}}</p></td>
<td><p>Total number of switches with the CLAG service enabled during the designated time period</p></td>
</tr>
<tr class="even">
<td><p>{{% imgOld 3 %}}</p></td>
<td><p>Total number of CLAG-related alarms received during the designated time period</p></td>
</tr>
<tr class="odd">
<td><p>Chart</p></td>
<td><p>Distribution of CLAG-related alarms received during the designated time period</p></td>
</tr>
</tbody>
</table>

The medium CLAG Service card displays:

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
<td><p>Network Services | <strong></strong> All CLAG Sessions</p></td>
</tr>
<tr class="even">
<td><p>{{% imgOld 6 %}}</p></td>
<td><p>Total number of switches with the CLAG service enabled during the designated time period</p></td>
</tr>
<tr class="odd">
<td><p>{{% imgOld 7 %}}</p></td>
<td><p>Total number of CLAG-related alarms received during the designated time period</p></td>
</tr>
<tr class="even">
<td><p><span style="color: #353744;"> </span></p>
<p>{{% imgOld 8 %}}</p></td>
<td><p>Total number of sessions with an inactive backup IP address</p></td>
</tr>
<tr class="odd">
<td><p><span style="color: #353744;"> </span></p>
<p>{{% imgOld 9 %}}</p></td>
<td><p>Total number of bonds with only a single connection</p></td>
</tr>
<tr class="even">
<td><p>Total Nodes Running chart</p></td>
<td><p>Total number and distribution of switches with CLAG service enabled during the designated time period</p></td>
</tr>
<tr class="odd">
<td><p>Total Alarms chart</p></td>
<td><p>Total number and distribution of CLAG-related alarms received during the designated time period</p></td>
</tr>
<tr class="even">
<td><p>Total Sessions chart</p></td>
<td><p>Total number and distribution of CLAG sessions network-wide during the designated time period</p></td>
</tr>
</tbody>
</table>

<span style="color: #000000;"> The large CLAG service card contains two
tabs. </span>

<span style="color: #000000;"> The *All CLAG Sessions Summary* tab which
displays: </span>

<span style="color: #000000;"> </span>

{{% imgOld 10 %}}

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
<p>{{% imgOld 11 %}}</p></td>
<td><p>Indicates data is for all sessions of a Network Service or Protocol</p></td>
</tr>
<tr class="odd">
<td><p>Title</p></td>
<td><p>All CLAG Sessions Summary</p></td>
</tr>
<tr class="even">
<td><p>{{% imgOld 12 %}}</p></td>
<td><p>Total number of switches with the CLAG service enabled during the designated time period</p></td>
</tr>
<tr class="odd">
<td><p>{{% imgOld 13 %}}</p></td>
<td><p>Total number of CLAG-related alarms received during the designated time period</p></td>
</tr>
<tr class="even">
<td><p>Total Nodes Running chart</p></td>
<td><p>Total number and distribution of switches with CLAG service enabled during the designated time period</p></td>
</tr>
<tr class="odd">
<td><p>Total Sessions chart</p></td>
<td><p>Total number and distribution of CLAG sessions network-wide during the designated time period</p></td>
</tr>
<tr class="even">
<td><p>Total Sessions with Inactive-backup-ip chart</p></td>
<td><p>Total number and distribution of sessions without an active backup IP defined</p></td>
</tr>
<tr class="odd">
<td><p>Table/Filter options</p></td>
<td><p>When the <strong>SWITCHES WITH MOST SESSIONS</strong> filter is selected, the table displays switches running CLAG sessions in decreasing order of session count—devices with the largest number of sessions are listed first</p>
<p>When the <strong>SWITCHES WITH MOST UNESTABLISHED SESSIONS</strong> filter is selected, the table displays switches running CLAG sessions in decreasing order of unestablished session count—devices with the largest number of unestablished sessions are listed first</p></td>
</tr>
<tr class="even">
<td><p>Show All Sessions</p></td>
<td><p>Link to view all CLAG sessions in the full screen card</p></td>
</tr>
</tbody>
</table>

<span style="color: #000000;"> The full screen CLAG Service card
provides tabs for all switches, all sessions, and all alarms. </span>

{{% imgOld 14 %}}

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
<td><p>Network Services | CLAG</p></td>
</tr>
<tr class="even">
<td><p>{{% imgOld 15 %}}</p></td>
<td><p>Closes full screen card and returns to workbench</p></td>
</tr>
<tr class="odd">
<td><p>Time period</p></td>
<td><p>Range of time in which the displayed data was collected; applies to all card sizes; select an alternate time period by clicking <span style="color: #353744;"> </span></p>
<p>{{% imgOld 16 %}}</p></td>
</tr>
<tr class="even">
<td><p>Results</p></td>
<td><p>Number of results found for the selected tab</p></td>
</tr>
<tr class="odd">
<td><p>All Switches tab</p></td>
<td><p>Displays all switches and hosts running the CLAG service. By default, the device list is sorted by <strong>hostname</strong>. This tab provides the following additional data about each device:</p>
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
<td><p>Displays all CLAG sessions network-wide. By default, the session list is sorted by hostname. This tab provides the following additional data about each session:</p>
<ul>
<li><p><strong>Backup Ip</strong>: IP address of the interface to use if the peerlink (or bond) goes down</p></li>
<li><p><strong>Backup Ip Active</strong>: Indicates whether the backup IP address has been specified and is active (true) or not (false)</p></li>
<li><p><strong>Bonds</strong></p>
<ul>
<li><p>Conflicted: Identifies the set of interfaces in a bond that do not match on each end of the bond</p></li>
<li><p>Single: Identifies a set of interfaces connecting to only one of the two switches</p></li>
<li><p>Dual: Identifies a set of interfaces connecting to both switches</p></li>
<li><p>Proto Down: Interface on the switch brought down by the <code>clagd</code> service. Value is blank if no interfaces are down due to <code>clagd</code> service.</p></li>
</ul></li>
<li><p><strong>Clag Sysmac</strong>: Unique MAC address for each bond interface pair. <strong>Note</strong>: Must be a value between 44:38:39:ff:00:00 and 44:38:39:ff:ff:ff.</p></li>
<li><p><strong>DB State</strong>: Session state of the DB.</p></li>
<li><p><strong>OPID</strong>: CLAG service identifier</p></li>
<li><p><strong>Peer</strong>:</p>
<ul>
<li><p>If: Name of the peer interface</p></li>
<li><p>Role: Role of the peer device. Values include primary and secondary.</p></li>
<li><p>State: Indicates if peer device is up (true) or down (false)</p></li>
</ul></li>
<li><p><strong>Role</strong>: Role of the host device. Values include primary and secondary.</p></li>
<li><p><strong>Timestamp</strong>: Date and time the CLAG session was started, deleted, updated, or marked dead (device went down)</p></li>
<li><p><strong>Vxlan Anycast</strong>: Anycast IP address used for VXLAN termination</p></li>
</ul></td>
</tr>
<tr class="odd">
<td><p>All Alarms tab</p></td>
<td><p>Displays all CLAG events network-wide. By default, the event list is sorted by time, with the most recent events listed first. The tab provides the following additional data about each event:</p>
<ul>
<li><p><strong>Message</strong>: Text description of a BGP-related event. Example: Clag conflicted bond changed from swp7 swp8 to @swp9 swp10</p></li>
<li><p><strong>Source</strong>: Hostname of network device that generated the event</p></li>
<li><p><strong>Severity</strong>: Importance of the event. Values include critical, warning, info, and debug.</p></li>
<li><p><strong>Type</strong>: Network protocol or service generating the event. This always has a value of <em>clag</em> in this card workflow.</p></li>
</ul></td>
</tr>
<tr class="even">
<td><p>Export</p></td>
<td><p>Enables export of all or selected items in a CSV or JSON formatted file</p></td>
</tr>
<tr class="odd">
<td><p><span style="color: #353744;"> </span></p>
<p>{{% imgOld 17 %}}</p></td>
<td><p>Enables manipulation of table display; choose columns to display and reorder columns</p></td>
</tr>
</tbody>
</table>

### <span>View Service Status Summary</span>

A summary of the CLAG service is available from the CLAG Service card
workflow, including the number of nodes running the service, the number
of CLAG-related alarms, and a distribution of those alarms.

To view the summary, open the small CLAG Service card.

{{% imgOld 18 %}}

For more detail, select a different size CLAG Service card.

### <span>View the Distribution of Sessions and Alarms</span>

It is useful to know the number of network nodes running the CLAG
protocol over a period of time, as it gives you insight into the amount
of traffic associated with and breadth of use of the protocol. It is
also useful to compare the number of nodes running CLAG with the alarms
present at the same time to determine if there is any correlation
between the issues and the ability to establish an CLAG session.

To view these distributions, open the medium CLAG Service card.

{{% imgOld 19 %}}

If a visual correlation is apparent, you can dig a little deeper with
the large CLAG Service card tabs.

### <span>View Devices with the Most CLAG Sessions</span>

You can view the load from CLAG on your switches using the large CLAG
Service card. This data enables you to see which switches are handling
the most CLAG traffic currently, validate that is what is expected based
on your network design, and compare that with data from an earlier time
to look for any differences.

To view switches and hosts with the most CLAG sessions:

1.  Open the large CLAG Service card.

2.  Select **SWITCHES WITH MOST SESSIONS** from the filter above the
    table.  
    The table content is sorted by this characteristic, listing nodes
    running the most CLAG sessions at the top. Scroll down to view those
    with the fewest sessions.
    
    {{% imgOld 20 %}}

To compare this data with the same data at a previous time:

1.  Open another large CLAG Service card.

2.  Move the new card next to the original card if needed.

3.  Change the time period for the data on the new card by hovering over
    the card and clicking <span style="color: #353744;"> </span>
    
    {{% imgOld 21 %}}
    
    .

4.  Select the time period that you want to compare with the current
    time.  
    You can now see whether there are significant differences between
    this time period and the previous time period.  
    
    {{% imgOld 22 %}}
    
    {{% imgOld 23 %}}
    
      
    If the changes are unexpected, you can investigate further by
    looking at another time frame, determining if more nodes are now
    running CLAG than previously, looking for changes in the topology,
    and so forth.

### <span>View Devices with the Most Unestablished CLAG Sessions</span>

You can identify switches that are experiencing difficulties
establishing CLAG sessions; both currently and in the past.

To view switches with the most unestablished CLAG sessions:

1.  Open the large CLAG Service card.

2.  Select **SWITCHES WITH MOST UNESTABLISHED SESSIONS** from the filter
    above the table.  
    The table content is sorted by this characteristic, listing nodes
    with the most unestablished CLAG sessions at the top. Scroll down to
    view those with the fewest unestablished sessions.
    
    {{% imgOld 24 %}}

Where to go next depends on what data you see, but a few options
include:

  - Hover over the any of the charts to focus on the number of switches
    or sessions with the chart characteristic during that smaller time
    slice.  
    The table content changes to match the hovered content. Click on the
    chart to persist the table changes.
    
    {{% imgOld 25 %}}

  - Change the time period for the data to compare with a prior time.  
    
    {{% imgOld 26 %}}
    
    {{% imgOld 27 %}}
    
      
    If the same switches are consistently indicating the most
    unestablished sessions, you might want to look more carefully at
    those switches using the Switches card workflow to determine
    probable causes. Refer to [Monitor
    Switches](/cumulus-netq/Cumulus_NetQ_UI_User_Guide/Monitor_Switches).

  - Click **Show All Sessions** to investigate all CLAG sessions with
    events in the full screen card.

### <span>View Switches with the Most CLAG-related Alarms</span>

Switches experiencing a large number of CLAG alarms may indicate a
configuration or performance issue that needs further investigation. You
can view the switches sorted by the number of CLAG alarms and then use
the Switches card workflow or the Alarms card workflow to gather more
information about possible causes for the alarms.

To view switches with most CLAG alarms:

1.  Open the large CLAG Service card.

2.  Hover over the header and click
    
    {{% imgOld 28 %}}
    
    .

3.  Select **EVENTS BY MOST ACTIVE DEVICE** from the filter above the
    table.  
    The table content is sorted by this characteristic, listing nodes
    with the most CLAG alarms at the top. Scroll down to view those with
    the fewest alarms.
    
    {{% imgOld 29 %}}

Where to go next depends on what data you see, but a few options
include:

  - Hover over the Total Alarms chart to focus on the switches
    exhibiting alarms during that smaller time slice.  
    The table content changes to match the hovered content. Click on the
    chart to persist the table changes.
    
    {{% imgOld 30 %}}

  - Change the time period for the data to compare with a prior time. If
    the same switches are consistently indicating the most alarms, you
    might want to look more carefully at those switches using the
    Switches card workflow.  
    
    {{% imgOld 31 %}}
    
    {{% imgOld 32 %}}

  - Click **Show All Sessions** to investigate all CLAG sessions with
    alarms in the full screen card.

### <span>View All CLAG Events</span>

The CLAG Service card workflow enables you to view all of the CLAG
events in the designated time period.

To view all CLAG events:

1.  Open the full screen CLAG Service card.

2.  Click **All Alarms** tab.
    
    {{% imgOld 33 %}}

Where to go next depends on what data you see, but a few options
include:

  - Open the **All Switches** or **All Sessions** tabs to look more
    closely at the alarms from the switch or session perspective.

  - Sort on other parameters:
    
      - by **Message** to determine the frequency of particular events
    
      - by **Severity** to determine the most critical events
    
      - by **Time** to find events that may have occurred at a
        particular time to try to correlate them with other system
        events

  - Export the data to a file by clicking **Export** or selecting a
    subset and clicking **Export Selected** in edit menu

  - Return to your workbench by clicking
    
    {{% imgOld 34 %}}
    
    in the top right corner

### <span>View Detailed Information About All Switches Running CLAG</span>

You can view all stored attributes of all switches running CLAG in your
network in the full-screen card.

To view all switch details, open the full screen CLAG Service card, and
click the **All Switches** tab.

{{% imgOld 35 %}}

To return to your workbench, click

{{% imgOld 36 %}}

in the top right corner.

### <span>Take Actions on Data Displayed in Results List</span>

In the full screen BGP Service card, you can determine which results are
displayed in the results list, and which are exported.

To take actions on the data, click in the blank column at the very left
of a row. A checkbox appears, selecting that switch, session, or alarm,
and an edit menu is shown at the bottom of the card (shown enlarged
here).

{{% imgOld 37 %}}

{{% imgOld 38 %}}

You can perform the following actions on the results list:

| Option             | Action or Behavior on Click                                                                                         |
| ------------------ | ------------------------------------------------------------------------------------------------------------------- |
| Select All         | Selects all switches, sessions, or alarms in the results list                                                       |
| Clear All          | Clears all existing selections of switches, sessions, or alarms in the results list. This also hides the edit menu. |
| Export Selected    | Opens export options dialog. Exported data includes only the selected data.                                         |
| Show Only Selected | Hide unselected switches, sessions, or alarms.                                                                      |
| Remove Selected    | Remove selected switches, sessions, or alarms from the results list.                                                |

To return to original display of results, refresh the browser.

## <span>Monitor a Single CLAG Session</span>

With NetQ, you can monitor the number of nodes running the CLAG service,
view switches with the most peers alive and not alive, and view alarms
triggered by the CLAG service. For an overview and how to configure CLAG
in your data center network, refer to [Multi-Chassis Link Aggregation -
MLAG](/display/NETQ/Multi-Chassis+Link+Aggregation+-+MLAG).

{{%notice info%}}

To access the single session cards, you must open the full screen CLAG
Service (all sessions) card and double-click on a session.

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

{{% imgOld 39 %}}

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

### <span>CLAG Session Card Workflow Summary</span>

The small CLAG Session card displays:

{{% imgOld 40 %}}

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
<p>{{% imgOld 41 %}}</p></td>
<td><p>Indicates data is for a single session of a Network Service or Protocol</p></td>
</tr>
<tr class="even">
<td><p>Title</p></td>
<td><p><strong>CLAG Session</strong></p></td>
</tr>
<tr class="odd">
<td><p> </p></td>
<td><p>Device identifiers (hostname, IP address, or MAC address) for host and peer in session. Arrow points from the host to the peer.</p></td>
</tr>
<tr class="even">
<td><p><span style="color: #353744;"> </span></p>
<p>{{% imgOld 42 %}}</p>
, <span style="color: #353744;"> </span>
<p>{{% imgOld 43 %}}</p></td>
<td><p>Indication of host role, primary</p>
<p>{{% imgOld 44 %}}</p>
or secondary
<p>{{% imgOld 45 %}}</p></td>
</tr>
</tbody>
</table>

The medium CLAG Session card displays:

<span style="color: #000000;"> </span>

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
<td><p>Time period</p></td>
<td><p>Range of time in which the displayed data was collected; applies to all card sizes</p></td>
</tr>
<tr class="even">
<td><p><span style="color: #222222;"> </span></p>
<p>{{% imgOld 47 %}}</p></td>
<td><p>Indicates data is for a single session of a Network Service or Protocol</p></td>
</tr>
<tr class="odd">
<td><p>Title</p></td>
<td><p>Network Services | CLAG Session</p></td>
</tr>
<tr class="even">
<td><p><span style="color: #353744;"> </span></p>
<p>{{% imgOld 48 %}}</p></td>
<td><p>Device identifiers (hostname, IP address, or MAC address) for host and peer in session. Arrow points from the host to the peer. Click on <span style="color: #353744;"> </span></p>
<p>{{% imgOld 49 %}}</p>
to open associated device card.</td>
</tr>
<tr class="odd">
<td><p><span style="color: #353744;"> </span></p>
<p>{{% imgOld 50 %}}</p>
,
<p>{{% imgOld 51 %}}</p></td>
<td><p>Indication of host role, primary</p>
<p>{{% imgOld 52 %}}</p>
or secondary
<p>{{% imgOld 53 %}}</p></td>
</tr>
<tr class="even">
<td><p>Time period</p></td>
<td><p>Range of time for data displayed in peer status chart</p></td>
</tr>
<tr class="odd">
<td><p>Peer Status chart</p></td>
<td><p>Distribution of peer availability, alive or not alive, during the designated time period. The number of time segments in a time period varies according to the length of the time period.</p></td>
</tr>
<tr class="even">
<td><p>Role</p></td>
<td><p>Role that host device is playing. Values include primary and secondary.</p></td>
</tr>
<tr class="odd">
<td><p>CLAG sysmac</p></td>
<td><p>System MAC address of the CLAG session</p></td>
</tr>
<tr class="even">
<td><p>Peer Role</p></td>
<td><p>Role that peer device is playing. Values include primary and secondary.</p></td>
</tr>
<tr class="odd">
<td><p>Peer State</p></td>
<td><p>Operational state of the peer, up (true) or down (false)</p></td>
</tr>
</tbody>
</table>

<span style="color: #000000;"> The large CLAG Session card contains
</span> one <span style="color: #000000;"> tab. </span>

<span style="color: #000000;"> The *Session Summary* tab displays:
</span>

<span style="color: #000000;"> </span>

{{% imgOld 54 %}}

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
<p>{{% imgOld 55 %}}</p></td>
<td><p>Indicates data is for a single session of a Network Service or Protocol</p></td>
</tr>
<tr class="odd">
<td><p>Title</p></td>
<td><p>(Network Services | CLAG Session) <strong>Session Summary</strong></p></td>
</tr>
<tr class="even">
<td><p><span style="color: #353744;"> </span></p>
<p>{{% imgOld 56 %}}</p></td>
<td><p>Device identifiers (hostname, IP address, or MAC address) for host and peer in session. Arrow points from the host to the peer. Click on <span style="color: #353744;"> </span></p>
<p>{{% imgOld 57 %}}</p>
to open associated device card.</td>
</tr>
<tr class="odd">
<td><p><span style="color: #353744;"> </span></p>
<p>{{% imgOld 58 %}}</p>
,
<p>{{% imgOld 59 %}}</p></td>
<td><p>Indication of host role, primary</p>
<p>{{% imgOld 60 %}}</p>
or secondary
<p>{{% imgOld 61 %}}</p></td>
</tr>
<tr class="even">
<td><p>Peer Status chart</p></td>
<td><p>Distribution of peer availability, alive or not alive, during the designated time period. The number of time segments in a time period varies according to the length of the time period.</p></td>
</tr>
<tr class="odd">
<td><p>Backup IP</p></td>
<td><p>IP address of the interface to use if the peerlink (or bond) goes down</p></td>
</tr>
<tr class="even">
<td><p>Backup IP Active</p></td>
<td><p>Indicates whether the backup IP address is configured</p></td>
</tr>
<tr class="odd">
<td><p>CLAG SysMAC</p></td>
<td><p>System MAC address of the CLAG session</p></td>
</tr>
<tr class="even">
<td><p>Peer State</p></td>
<td><p>Operational state of the peer, up (true) or down (false)</p></td>
</tr>
<tr class="odd">
<td><p>Count of Dual Bonds</p></td>
<td><p>Number of bonds connecting to both switches.</p></td>
</tr>
<tr class="even">
<td><p>Count of Single Bonds</p></td>
<td><p>Number of bonds connecting to only one switch.</p></td>
</tr>
<tr class="odd">
<td><p>Count of Protocol Down Bonds</p></td>
<td><p>Number of bonds with interfaces that were brought down by the <code>clagd</code> service.</p></td>
</tr>
<tr class="even">
<td><p>Count of Conflicted Bonds</p></td>
<td><p>Number of bonds which have a set of interfaces that are not the same on both switches</p></td>
</tr>
</tbody>
</table>

<span style="color: #000000;"> The full screen CLAG Session card
provides tabs for all CLAG sessions and all events. </span>

<span style="color: #000000;"> </span>

{{% imgOld 62 %}}

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
<td><p>Network Services | CLAG</p></td>
</tr>
<tr class="even">
<td><p>{{% imgOld 63 %}}</p></td>
<td><p>Closes full screen card and returns to workbench</p></td>
</tr>
<tr class="odd">
<td><p>Time period</p></td>
<td><p>Range of time in which the displayed data was collected; applies to all card sizes; select an alternate time period by clicking <span style="color: #353744;"> </span></p>
<p>{{% imgOld 64 %}}</p></td>
</tr>
<tr class="even">
<td><p>Results</p></td>
<td><p>Number of results found for the selected tab</p></td>
</tr>
<tr class="odd">
<td><p>All CLAG Sessions tab</p></td>
<td><p>Displays all CLAG sessions for the given session. By default, the session list is sorted by <strong>hostname</strong>. This tab provides the following additional data about each session:</p>
<ul>
<li><p><strong>Backup Ip</strong>: IP address of the interface to use if the peerlink (or bond) goes down</p></li>
<li><p><strong>Backup Ip Active</strong>: Indicates whether the backup IP address has been specified and is active (true) or not (false)</p></li>
<li><p><strong>Bonds</strong></p>
<ul>
<li><p>Conflicted: Identifies the set of interfaces in a bond that do not match on each end of the bond</p></li>
<li><p>Single: Identifies a set of interfaces connecting to only one of the two switches</p></li>
<li><p>Dual: Identifies a set of interfaces connecting to both switches</p></li>
<li><p>Proto Down: Interface on the switch brought down by the <code>clagd</code> service. Value is blank if no interfaces are down due to <code>clagd</code> service.</p></li>
</ul></li>
<li><p><strong>Clag Sysmac</strong>: Unique MAC address for each bond interface pair. <strong>Note</strong>: Must be a value between 44:38:39:ff:00:00 and 44:38:39:ff:ff:ff.</p></li>
<li><p><strong>DB State</strong>: Session state of the DB.</p></li>
<li><p><strong>OPID</strong>: CLAG service identifier</p></li>
<li><p><strong>Peer</strong>:</p>
<ul>
<li><p>If: Name of the peer interface</p></li>
<li><p>Role: Role of the peer device. Values include primary and secondary.</p></li>
<li><p>State: Indicates if peer device is up (true) or down (false)</p></li>
</ul></li>
<li><p><strong>Role</strong>: Role of the host device. Values include primary and secondary.</p></li>
<li><p><strong>Timestamp</strong>: Date and time the CLAG session was started, deleted, updated, or marked dead (device went down)</p></li>
<li><p><strong>Vxlan Anycast</strong>: Anycast IP address used for VXLAN termination</p></li>
</ul></td>
</tr>
<tr class="even">
<td><p>All Events tab</p></td>
<td><p>Displays all events network-wide. By default, the event list is sorted by <strong>time</strong>, with the most recent events listed first. The tab provides the following additional data about each event:</p>
<ul>
<li><p><strong>Message</strong>: Text description of an event. Example: Clag conflicted bond changed from swp7 swp8 to @swp9 swp10</p></li>
<li><p><strong>Source</strong>: Hostname of network device that generated the event</p></li>
<li><p><strong>Severity</strong>: Importance of the event. Values include critical, warning, info, and debug.</p></li>
<li><p><strong>Type</strong>: Network protocol or service generating the event. This always has a value of <em>clag</em> in this card workflow.</p></li>
</ul></td>
</tr>
<tr class="odd">
<td><p>Export</p></td>
<td><p>Enables export of all or selected items in a CSV or JSON formatted file</p></td>
</tr>
<tr class="even">
<td><p><span style="color: #353744;"> </span></p>
<p>{{% imgOld 65 %}}</p></td>
<td><p>Enables manipulation of table display; choose columns to display and reorder columns</p></td>
</tr>
</tbody>
</table>

### <span>View Session Status Summary</span>

A summary of the CLAG session is available from the CLAG Session card
workflow, showing the node and its peer and current status.

To view the summary:

1.  Open the full screen CLAG Service card.

2.  Select a session from the listing to view.

3.  Close the full screen card to view the medium CLAG Session card.
    
    {{% imgOld 66 %}}
    
    In this example, we see that the tor1 switch plays the secondary
    role in this session with the switch at 44:38:39:ff:01:01.

### <span>View CLAG Session Peering State Changes </span>

You can view the peering state for a given CLAG session from the medium
and large CLAG Session cards. For a given time period, you can determine
the stability of the CLAG session between two devices. If you
experienced connectivity issues at a particular time, you can use these
cards to help verify the state of the peer. If the peer was not alive
more than it was alive, you can then investigate further into possible
causes.

To view the state transitions for a given CLAG session:

1.  Open the full screen CLAG Service card.

2.  Select a session from the listing to view.

3.  Close the full screen card to view the medium CLAG Session card.
    
    {{% imgOld 67 %}}
    
    In this example, the peer switch has been alive for the entire
    24-hour period.

From this card, you can also view the node role, peer role and state,
and CLAG system MAC address which identify the session in more detail.

To view the peering state transitions for a given CLAG session on the
large CLAG Session card, open that card.

{{% imgOld 68 %}}

From this card, you can also view the node role, peer role, state, and
interface, CLAG system MAC address, active backup IP address, single,
dual, conflicted, and protocol down bonds, and the VXLAN anycast address
identifying the session in more detail.

### <span>View All CLAG Session Details</span>

<span style="color: #000000;"> You can view all stored attributes of all
of the CLAG sessions associated with the two devices on this card.
</span>

<span style="color: #000000;"> To view all session details, open the
full screen CLAG Session card, and click the **All CLAG Sessions** tab.
</span>

<span style="color: #000000;"> </span>

{{% imgOld 69 %}}

Where to go next depends on what data you see, but a few options
include:

  - Open the **All Events** tabs to look more closely at the alarm and
    info events fin the network.

  - Sort on other parameters:
    
      - by **Single Bonds** to determine which interface sets are only
        connected to one of the switches
    
      - by **Backup IP and Backup IP Active** to determine if the
        correct backup IP address is specified for the service

  - Export the data to a file by clicking **Export** or selecting a
    subset and clicking **Export Selected** in edit menu

  - Return to your workbench by clicking
    
    {{% imgOld 70 %}}
    
    in the top right corner

### <span>View All Events</span>

<span style="color: #000000;"> You can view all of the alarm and info
events for the two devices on this card. </span>

<span style="color: #000000;"> To view all events, o </span> pen the
full screen CLAG Session card, and click the **All Events** tab.

{{% imgOld 71 %}}

Where to go next depends on what data you see, but a few options
include:

  - Open the **All CLAG Sessions** tabs to look more closely at the
    individual sessions.

  - Sort on other parameters:
    
      - by **Message** to determine the frequency of particular events
    
      - by **Severity** to determine the most critical events
    
      - by **Time** to find events that may have occurred at a
        particular time to try to correlate them with other system
        events

  - Export the data to a file by clicking **Export** or selecting a
    subset and clicking **Export Selected** in edit menu

  - Return to your workbench by clicking
    
    {{% imgOld 72 %}}
    
    in the top right corner
