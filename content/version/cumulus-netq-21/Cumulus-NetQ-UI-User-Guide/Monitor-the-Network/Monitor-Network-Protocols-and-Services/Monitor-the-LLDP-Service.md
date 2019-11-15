---
title: Monitor the LLDP Service
author: Cumulus Networks
weight: 151
aliases:
 - /display/NETQ21/Monitor+the+LLDP+Service
 - /pages/viewpage.action?pageId=10464735
pageID: 10464735
product: Cumulus NetQ
version: '2.1'
imgData: cumulus-netq-21
siteSlug: cumulus-netq-21
---
The Cumulus NetQ UI enables operators to view the health of the LLDP
service on a network-wide and a per session basis, giving greater
insight into all aspects of the service. This is accomplished through
two card workflows, one for the service and one for the session. They
are described separately here.

## Monitor the LLDP Service (All Sessions)

With NetQ, you can monitor the number of nodes running the LLDP service,
view nodes with the most LLDP neighbor nodes, those nodes with the least
neighbor nodes, and view alarms triggered by the LLDP service. For an
overview and how to configure LLDP in your data center network, refer to [Link Layer Discovery Protocol](https://docs.cumulusnetworks.com/cumulus-linux/Layer-2/Link-Layer-Discovery-Protocol/).

### LLDP Service Card Workflow Summary

The small LLDP Service card displays:

{{% imgOld 0 %}}

<table>
<colgroup>
<col style="width: 20%" />
<col style="width: 80%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Item</p></th>
<th><p>Description</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>{{% imgOld 1 %}}</p></td>
<td><p>Indicates data is for all sessions of a Network Service or Protocol</p></td>
</tr>
<tr class="even">
<td><p>Title</p></td>
<td><p><strong>LLDP</strong>: All LLDP Sessions, or the LLDP Service</p></td>
</tr>
<tr class="odd">
<td><p>{{% imgOld 2 %}}</p></td>
<td><p>Total number of switches with the LLDP service enabled during the designated time period</p></td>
</tr>
<tr class="even">
<td><p>{{% imgOld 3 %}}</p></td>
<td><p>Total number of LLDP-related alarms received during the designated time period</p></td>
</tr>
<tr class="odd">
<td><p>Chart</p></td>
<td><p>Distribution of LLDP-related alarms received during the designated time period</p></td>
</tr>
</tbody>
</table>

The medium LLDP Service card displays:

{{% imgOld 4 %}}

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 75%" />
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
<td><p>{{% imgOld 5 %}}</p></td>
<td><p>Indicates data is for all sessions of a Network Service or Protocol</p></td>
</tr>
<tr class="odd">
<td><p>Title</p></td>
<td><p><strong>LLDP</strong>: All LLDP Sessions, or the LLDP Service</p></td>
</tr>
<tr class="even">
<td><p>{{% imgOld 6 %}}</p></td>
<td><p>Total number of switches with the LLDP service enabled during the designated time period</p></td>
</tr>
<tr class="odd">
<td><p>{{% imgOld 7 %}}</p></td>
<td><p>Total number of LLDP-related alarms received during the designated time period</p></td>
</tr>
<tr class="even">
<td><p>Total Nodes Running chart</p></td>
<td><p>Total number and distribution of switches and hosts with LLDP enabled during the designated time period</p></td>
</tr>
<tr class="odd">
<td><p>Total Alarms chart</p></td>
<td><p>Total number and distribution of LLDP-related alarms received during the designated time period</p></td>
</tr>
<tr class="even">
<td><p>Total Sessions chart</p></td>
<td><p>Total number and distribution of LLDP sessions running during the designated time period</p></td>
</tr>
</tbody>
</table>

The large LLDP service card contains two tabs.

The *Sessions Summary* tab which displays:

{{% imgOld 8 %}}

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 75%" />
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
<td><p>{{% imgOld 9 %}}</p></td>
<td><p>Indicates data is for all sessions of a Network Service or Protocol</p></td>
</tr>
<tr class="odd">
<td><p>Title</p></td>
<td><p>Sessions Summary (Network Services | All LLDP Sessions)</p></td>
</tr>
<tr class="even">
<td><p>{{% imgOld 10 %}}</p></td>
<td><p>Total number of switches with the LLDP service enabled during the designated time period</p></td>
</tr>
<tr class="odd">
<td><p>{{% imgOld 11 %}}</p></td>
<td><p>Total number of LLDP-related alarms received during the designated time period</p></td>
</tr>
<tr class="even">
<td><p>Total Nodes Running chart</p></td>
<td><p>Total number and distribution of switches and hosts with LLDP enabled during the designated time period</p></td>
</tr>
<tr class="odd">
<td><p>Total Sessions chart</p></td>
<td><p>Total number and distribution of LLDP sessions running during the designated time period</p></td>
</tr>
<tr class="even">
<td><p>Total Sessions with No Nbr chart</p></td>
<td><p>Total number and distribution of LLDP sessions missing neighbor information during the designated time period</p></td>
</tr>
<tr class="odd">
<td><p>Table/Filter options</p></td>
<td><p>When the <strong>SWITCHES WITH MOST SESSIONS</strong> filter is selected, the table displays switches running LLDP sessions in decreasing order of session count—devices with the largest number of sessions are listed first</p>
<p>When the <strong>SWITCHES WITH MOST UNESTABLISHED SESSIONS</strong> filter is selected, the table displays switches running LLDP sessions in decreasing order of unestablished session count—devices with the largest number of unestablished sessions are listed first</p></td>
</tr>
<tr class="even">
<td><p>Show All Sessions</p></td>
<td><p>Link to view all LLDP sessions in the full screen card</p></td>
</tr>
</tbody>
</table>

The *Alarms* tab which displays:

{{% imgOld 12 %}}

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 75%" />
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
<td><p>{{% imgOld 13 %}}</p></td>
<td><p>Indicates data is for all sessions of a Network Service or Protocol</p></td>
</tr>
<tr class="odd">
<td><p>Title</p></td>
<td><p><strong>Alarms</strong> (visible when you hover over card)</p></td>
</tr>
<tr class="even">
<td><p>{{% imgOld 14 %}}</p></td>
<td><p>Total number of switches with the LLDP service enabled during the designated time period</p></td>
</tr>
<tr class="odd">
<td><p>{{% imgOld 15 %}}</p></td>
<td><p>Total number of LLDP-related alarms received during the designated time period</p></td>
</tr>
<tr class="even">
<td><p>Total Alarms chart</p></td>
<td><p>Total number and distribution of LLDP-related alarms received during the designated time period</p></td>
</tr>
<tr class="odd">
<td><p>Table/Filter options</p></td>
<td><p>When the <strong>EVENTS BY MOST ACTIVE DEVICE</strong> filter is selected, the table displays switches running LLDP sessions in decreasing order of alarm count—devices with the largest number of sessions are listed first</p></td>
</tr>
<tr class="even">
<td><p>Show All Sessions</p></td>
<td><p>Link to view all LLDP sessions in the full screen card</p></td>
</tr>
</tbody>
</table>

The full screen LLDP Service card provides tabs for all switches, all
sessions, and all alarms.

{{% imgOld 16 %}}

<table>
<colgroup>
<col style="width: 20%" />
<col style="width: 80%" />
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
<td><p>Network Services | LLDP</p></td>
</tr>
<tr class="even">
<td><p><img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/close.svg", height="18", width="18"/></p></td>
<td><p>Closes full screen card and returns to workbench</p></td>
</tr>
<tr class="odd">
<td><p>Time period</p></td>
<td><p>Range of time in which the displayed data was collected; applies to all card sizes; select an alternate time period by clicking {{% imgOld 18 %}}</p></td>
</tr>
<tr class="even">
<td><p>Results</p></td>
<td><p>Number of results found for the selected tab</p></td>
</tr>
<tr class="odd">
<td><p>All Switches tab</p></td>
<td><p>Displays all switches and hosts running the LLDP service. By default, the device list is sorted by <strong>hostname</strong>. This tab provides the following additional data about each device:</p>
<ul>
<li><p><strong>Agent</strong></p>
<ul>
<li><p>State: Indicates communication state of the NetQ Agent on a given device. Values include Fresh (heard from recently) and Rotten (not heard from recently).</p></li>
<li><p>Version: Software version number of the NetQ Agent on a given device. This should match the version number of the NetQ software loaded on your server or appliance; for example, 2.1.0.</p></li></ul>
<li><p><strong>ASIC</strong></p></li>
<ul>
<li><p>Core BW: Maximum sustained/rated bandwidth. Example values include 2.0 T and 720 G.</p></li>
<li><p>Model: Chip family. Example values include Tomahawk, Trident, and Spectrum.</p></li>
<li><p>Model Id: Identifier of networking ASIC model. Example values include BCM56960 and BCM56854. </span></p></li>
<li><p>Ports: Indicates port configuration of the switch. Example values include 32 x 100G-QSFP28, 48 x 10G-SFP+, and 6 x 40G-QSFP+. </span></p></li>
<li><p>Vendor: Manufacturer of the chip. Example values include Broadcom and Mellanox.</p></li>
</ul>
<p><strong>CPU</strong></p>
<ul>
<li><p>Arch: Microprocessor architecture type. Values include x86_64 (Intel), ARMv7 (AMD), and PowerPC.</p></li>
<li><p>Max Freq: Highest rated frequency for CPU. Example values include 2.40 GHz and 1.74 GHz. </span></p></li>
<li><p>Model: Chip family. Example values include Intel Atom C2538 and Intel Atom C2338. </span></p></li>
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
<li><p>MAC: System MAC address. Example value: 17:01:AB:EE:C3:F5.</p></li>
<li><p>Model: Manufacturer's model name. Examples values include AS7712-32X and S4048-ON. </span></p></li>
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
<td><p>Displays all LLDP sessions network-wide. By default, the session list is sorted by <strong>hostname</strong>. This tab provides the following additional data about each session:</p>
<ul>
<li><p><strong>DB State</strong>: Session state of the DB.</p></li>
<li><p><strong>Ifname</strong>: Name of the host interface where LLDP session is running</p></li>
<li><p><strong>LLDP Peer</strong>:</p>
<ul>
<li><p>Os: Operating system (OS) used by peer device. Values include Cumulus Linux, RedHat, Ubuntu, and CentOS.</p></li>
<li><p>Osv: Version of the OS used by peer device. Example values include 3.7.3, 2.5.x, 16.04, 7.1.</p></li>
<li><p>Bridge: Indicates whether the peer device is a bridge (true) or not (false)</p></li>
<li><p>Router: Indicates whether the peer device is a router (true) or not (false)</p></li>
<li><p>Station: Indicates whether the peer device is a station (true) or not (false)</p></li>
</ul></li>
<li><p><strong>OPID</strong>: LLDP service identifier</p></li>
<li><p><strong>Peer</strong>:</p>
<ul>
<li><p>Hostname: User-defined name for the peer device</p></li>
<li><p>Ifname: Name of the peer interface where the session is running</p></li>
</ul></li>
<li><p><strong>Timestamp</strong>: Date and time that the session was started, deleted, updated, or marked dead (device is down)</p></li>
</ul></td>
</tr>
<tr class="odd">
<td><p>All Alarms tab</p></td>
<td><p>Displays all LLDP events network-wide. By default, the event list is sorted by time, with the most recent events listed first. The tab provides the following additional data about each event:</p>
<ul>
<li><p><strong>Message</strong>: Text description of a LLDP-related event. Example: LLDP Session with host leaf02 swp6 modified fields leaf06 swp21</p></li>
<li><p><strong>Source</strong>: Hostname of network device that generated the event</p></li>
<li><p><strong>Severity</strong>: Importance of the event. Values include critical, warning, info, and debug.</p></li>
<li><p><strong>Type</strong>: Network protocol or service generating the event. This always has a value of <em>lldp</em> in this card workflow.</p></li>
</ul></td>
</tr>
<tr class="even">
<td><p>Export</p></td>
<td><p>Enables export of all or selected items in a CSV or JSON formatted file</p></td>
</tr>
<tr class="odd">
<td><p></p>
<p>{{% imgOld 19 %}}</p></td>
<td><p>Enables manipulation of table display; choose columns to display and reorder columns</p></td>
</tr>
</tbody>
</table>

### View Service Status Summary

A summary of the LLDP service is available from the Network Services
card workflow, including the number of nodes running the service, the
number of LLDP-related alarms, and a distribution of those alarms.

To view the summary, open the small LLDP Service card.

{{% imgOld 20 %}}

In this example, there are no LLDP alarms present on the network of
twelve devices.

For more detail, select a different size LLDP Network Services card.

### View the Distribution of Nodes, Alarms, and Sessions

It is useful to know the number of network nodes running the LLDP
protocol over a period of time, as it gives you insight into nodes that
might be misconfigured or experiencing communication issues.
Additionally, if there are a large number of alarms, it is worth
investigating either the service or particular devices.

To view the distribution, open the medium LLDP Service card.

{{% imgOld 21 %}}

In this example, we see that twelve nodes are running the LLDP protocol,
that there are 70 sessions established, and that no LLDP-related alarms
have occurred in the last 24 hours.

### View the Distribution of Missing Neighbors

You can view the number of missing neighbors in any given time period
and how that number has changed over time. This is a good indicator of
link communication issues.

To view the distribution, open the large LLDP Service card and view the
bottom chart on the left, **Total Sessions with No Nbr**.

{{% imgOld 22 %}}

In this example, we see that 18 of the 52 sessions are missing the
neighbor (peer) device.

### View Devices with the Most LLDP Sessions

You can view the load from LLDP on your switches using the large LLDP
Service card. This data enables you to see which switches are handling
the most LLDP traffic currently, validate that is what is expected based
on your network design, and compare that with data from an earlier time
to look for any differences.

To view switches and hosts with the most LLDP sessions:

1.  Open the large LLDP Service card.

2.  Select **SWITCHES WITH MOST SESSIONS** from the filter above the
    table.  
    The table content is sorted by this characteristic, listing nodes
    running the most LLDP sessions at the top. Scroll down to view those
    with the fewest sessions.
    
    {{% imgOld 23 %}}

To compare this data with the same data at a previous time:

1.  Open another large LLDP Service card.

2.  Move the new card next to the original card if needed.

3.  Change the time period for the data on the new card by hovering over
    the card and clicking {{% imgOld 24 %}}.

4.  Select the time period that you want to compare with the current
    time.  
    You can now see whether there are significant differences between
    this time period and the previous time period.  
    
    {{% imgOld 25 %}}
    
    {{% imgOld 26 %}}
    
      
    In this case, notice that the alarms have reduced significantly in
    the last week. If the changes are unexpected, you can investigate
    further by looking at another time frame, determining if more nodes
    are now running LLDP than previously, looking for changes in the
    topology, and so forth.

### View Devices with the Most Unestablished LLDP Sessions

You can identify switches that are experiencing difficulties
establishing LLDP sessions; both currently and in the past.

To view switches with the most unestablished LLDP sessions:

1.  Open the large LLDP Service card.

2.  Select **SWITCHES WITH MOST UNESTABLISHED SESSIONS** from the filter
    above the table.  
    The table content is sorted by this characteristic, listing nodes
    with the most unestablished CLAG sessions at the top. Scroll down to
    view those with the fewest unestablished sessions.
    
    {{% imgOld 27 %}}

Where to go next depends on what data you see, but a few options
include:

- Hover over any of the charts to focus on the number of switches or
  sessions with the chart characteristic during that smaller time
  slice. The table content changes to match the hovered content. Click on the
  chart to persist the table changes.
  
  {{% imgOld 28 %}}

- Change the time period for the data to compare with a prior time.  
  
  {{% imgOld 29 %}}
  
  {{% imgOld 30 %}}
  
  If the same switches are consistently indicating the most
  unestablished sessions, you might want to look more carefully at
  those switches using the Switches card workflow to determine
  probable causes. Refer to [Monitor Switches](../../../Monitor-Switches).

- Click **Show All Sessions** to investigate all LLDP sessions with
  events in the full screen card.

### View Switches with the Most LLDP-related Alarms

Switches experiencing a large number of LLDP alarms may indicate a
configuration or performance issue that needs further investigation. You
can view the switches sorted by the number of LLDP alarms and then use
the Switches card workflow or the Alarms card workflow to gather more
information about possible causes for the alarms.

To view switches with most LLDP alarms:

1.  Open the large LLDP Service card.

2.  Hover over the header and click <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/20-Alert/alarm-bell.svg", height="18", width="18"/>.

3.  Select **EVENTS BY MOST ACTIVE DEVICE** from the filter above the
    table.  
    The table content is sorted by this characteristic, listing nodes
    with the most BGP alarms at the top. Scroll down to view those with
    the fewest alarms.
    
    {{% imgOld 32 %}}

Where to go next depends on what data you see, but a few options
include:

- Hover over the Total Alarms chart to focus on the switches
  exhibiting alarms during that smaller time slice. The table content changes to match the hovered content. Click on the chart to persist the table changes.
- Change the time period for the data to compare with a prior time. If
  the same switches are consistently indicating the most alarms, you
  might want to look more carefully at those switches using the
  Switches card workflow.
- Click **Show All Sessions** to investigate all switches running LLDP
  sessions in the full screen card.

### View All LLDP Events

The LLDP Network Services card workflow enables you to view all of the
LLDP events in the designated time period.

To view all LLDP events:

1.  Open the full screen LLDP Service card.

2.  Click the **All Alarms** tab.
    
    {{% imgOld 33 %}}

Where to go next depends on what data you see, but a few options
include:

- Open the **All Switches** or **All Sessions** tabs to look more closely at the alarms from the switch or session perspective.
- Sort on other parameters:
  - by **Message** to determine the frequency of particular events
  - by **Severity** to determine the most critical events
  - by **Time** to find events that may have occurred at a
    particular time to try to correlate them with other system
    events
- Export data to a file
- Return to your workbench by clicking {{% imgOld 34 %}} in the top right corner

### View Detailed Information About All Switches Running LLDP

You can view all stored attributes of all switches running LLDP in your
network in the full screen card.

To view all switch details, open the LLDP Service card, and click the
**All Switches** tab.

{{% imgOld 35 %}}

Return to your workbench by clicking {{% imgOld 36 %}} in the top right corner.

### View Detailed Information About All LLDP Sessions

You can view all stored attributes of all LLDP sessions in your network
in the full screen card.

To view all session details, open the LLDP Service card, and click the
**All Sessions** tab.

{{% imgOld 37 %}}

Return to your workbench by clicking {{% imgOld 38 %}} in the top right corner.

### Take Actions on Data Displayed in Results List

In the full screen LLDP Service card, you can determine which results
are displayed in the results list, and which are exported.

To take actions on the data, click in the blank column at the very left
of a row. A checkbox appears, selecting that switch, session, or alarm,
and an edit menu is shown at the bottom of the card (shown enlarged
here).

{{% imgOld 39 %}}

{{% imgOld 40 %}}

You can perform the following actions on the results list:

| Option             | Action or Behavior on Click                                                                                      |
| ------------------ | ---------------------------------------------------------------------------------------------------------------- |
| Select All         | Selects all items in the results list                                                                            |
| Clear All          | Clears all existing selections of items in the results list. This also hides the edit menu.                      |
| Open Cards         | Open the corresponding validation or trace result card.                                                          |
| Hide Selected      | Hide selected items (switches, sessions, alarms, and so forth) from the results list.                            |
| Show Only Selected | Hide unselected items (switches, sessions, alarms, and so forth) from the results list.                          |
| Export Selected    | Exports selected data into a .csv file. If you want to export to a .json file format, use the **Export** button. |

To return to original display of results, click the associated tab.

## Monitor a Single LLDP Session

With NetQ, you can monitor the number of nodes running the LLDP service,
view neighbor state changes, and compare with events occurring at the
same time, as well as monitor the running LLDP configuration and changes
to the configuration file. For an overview and how to configure LLDP in
your data center network, refer to [Link Layer Discovery Protocol](https://docs.cumulusnetworks.com/cumulus-linux/Layer-2/Link-Layer-Discovery-Protocol/).

{{%notice info%}}

To access the single session cards, you must open the full screen LLDP
Service (all sessions) card and click on a session. Close the full
screen card to view the medium single session card.

{{%/notice%}}

### Granularity of Data Shown Based on Time Period

On the medium and large single LLDP session cards, the status of the
neighboring peers is represented in heat maps stacked vertically; one
for peers that are reachable (neighbor detected), and one for peers that
are unreachable (neighbor not detected). Depending on the time period of
data on the card, the number of smaller time blocks used to indicate the
status varies. A vertical stack of time blocks, one from each map,
includes the results from all checks during that time. The results are
shown by how saturated the color is for each block. If all peers during
that time period were detected for the entire time block, then the top
block is 100% saturated (white) and the neighbor not detected block is
zero percent saturated (gray). As peers become reachable, the neighbor
detected block increases in saturation, the peers that are unreachable
(neighbor not detected) block is proportionally reduced in saturation.
An example heat map for a time period of 24 hours is shown here with the
most common time periods in the table showing the resulting time blocks.

{{% imgOld 41 %}}

| Time Period | Number of Runs | Number Time Blocks | Amount of Time in Each Block |
| ----------- | -------------- | ------------------ | ---------------------------- |
| 6 hours     | 18             | 6                  | 1 hour                       |
| 12 hours    | 36             | 12                 | 1 hour                       |
| 24 hours    | 72             | 24                 | 1 hour                       |
| 1 week      | 504            | 7                  | 1 day                        |
| 1 month     | 2,086          | 30                 | 1 day                        |
| 1 quarter   | 7,000          | 13                 | 1 week                       |

### LLDP Session Card Workflow Summary

The small LLDP Session card displays:

{{% imgOld 42 %}}

<table>
<colgroup>
<col style="width: 20%" />
<col style="width: 80%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Item</p></th>
<th><p>Description</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>{{% imgOld 43 %}}</p></td>
<td><p>Indicates data is for a single session of a Network Service or Protocol</p></td>
</tr>
<tr class="even">
<td><p>Title</p></td>
<td><p>LLDP Session</p></td>
</tr>
<tr class="odd">
<td><p> </p></td>
<td><p>Host and peer devices in session. Arrow points from host to peer.</p></td>
</tr>
<tr class="even">
<td><p></p>
<p>{{% imgOld 44 %}}</p>
, 
<p>{{% imgOld 45 %}}</p>
</span></td>
<td><p>Indicates whether the host sees the peer or not;</p>
<p>{{% imgOld 46 %}}</p>
has a peer,
<p>{{% imgOld 47 %}}</p>
no peer</td>
</tr>
</tbody>
</table>

The medium LLDP Session card displays:

{{% imgOld 48 %}}

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 75%" />
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
<td><p>Range of time in which the displayed data was collected</p></td>
</tr>
<tr class="even">
<td><p>{{% imgOld 49 %}}</p></td>
<td><p>Indicates data is for a single session of a Network Service or Protocol</p></td>
</tr>
<tr class="odd">
<td><p>Title</p></td>
<td><p>LLDP Session</p></td>
</tr>
<tr class="even">
<td><p> </p></td>
<td><p>Host and peer devices in session. Arrow points from host to peer.</p></td>
</tr>
<tr class="odd">
<td><p></p>
<p>{{% imgOld 50 %}}</p>
,
<p>{{% imgOld 51 %}}</p></td>
<td><p>Indicates whether the host sees the peer or not;</p>
<p>{{% imgOld 52 %}}</p>
has a peer,
<p>{{% imgOld 53 %}}</p>
no peer</td>
</tr>
<tr class="even">
<td><p>Time period</p></td>
<td><p>Range of time for the distribution chart</p></td>
</tr>
<tr class="odd">
<td><p>Heat map</p></td>
<td><p>Distribution of neighbor availability (detected or undetected) during this given time period</p></td>
</tr>
<tr class="even">
<td><p>Hostname</p></td>
<td><p>User-defined name of the host device</p></td>
</tr>
<tr class="odd">
<td><p>Interface Name</p></td>
<td><p>Software interface on the host device where the session is running</p></td>
</tr>
<tr class="even">
<td><p>Peer Hostname</p></td>
<td><p>User-defined name of the peer device</p></td>
</tr>
<tr class="odd">
<td><p>Peer Interface Name</p></td>
<td><p>Software interface on the peer where the session is running</p></td>
</tr>
</tbody>
</table>

The large LLDP Session card contains two tabs.

The *Session Summary* tab displays:

{{% imgOld 54 %}}

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 75%" />
</colgroup>
<thead>
<tr class="header">
<th><p> </p></th>
<th><p>Description</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Time period</p></td>
<td><p>Range of time in which the displayed data was collected</p></td>
</tr>
<tr class="even">
<td><p>{{% imgOld 55 %}}</p></td>
<td><p>Indicates data is for a single session of a Network Service or Protocol</p></td>
</tr>
<tr class="odd">
<td><p>Title</p></td>
<td><p><strong>Summary Session</strong> (Network Services | LLDP Session)</p></td>
</tr>
<tr class="even">
<td><p> </p></td>
<td><p>Host and peer devices in session. Arrow points from host to peer.</p></td>
</tr>
<tr class="odd">
<td><p></p>
<p>{{% imgOld 56 %}}</p>
,
<p>{{% imgOld 57 %}}</p></td>
<td><p>Indicates whether the host sees the peer or not;</p>
<p>{{% imgOld 58 %}}</p>
has a peer,
<p>{{% imgOld 59 %}}</p>
no peer</td>
</tr>
<tr class="even">
<td><p>Heat map</p></td>
<td><p>Distribution of neighbor state (detected or undetected) during this given time period</p></td>
</tr>
<tr class="odd">
<td><p>Alarm Count chart</p></td>
<td><p>Distribution and count of LLDP alarm events during the given time period</p></td>
</tr>
<tr class="even">
<td><p>Info Count chart</p></td>
<td><p>Distribution and count of LLDP info events during the given time period</p></td>
</tr>
<tr class="odd">
<td><p>Host Interface Name</p></td>
<td><p>Software interface on the host where the session is running</p></td>
</tr>
<tr class="even">
<td><p>Peer Hostname</p></td>
<td><p>User-defined name of the peer device</p></td>
</tr>
<tr class="odd">
<td><p>Peer Interface Name</p></td>
<td><p>Software interface on the peer where the session is running</p></td>
</tr>
</tbody>
</table>

The *Configuration File Evolution* tab displays:

{{% imgOld 60 %}}

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 75%" />
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
<td><p>{{% imgOld 61 %}}</p></td>
<td><p>Indicates data is for a single session of a Network Service or Protocol</p></td>
</tr>
<tr class="odd">
<td><p>Title</p></td>
<td><p>(Network Services | LLDP Session) <strong>Configuration File Evolution</strong></p></td>
</tr>
<tr class="even">
<td><p></p>
<p>{{% imgOld 62 %}}</p></td>
<td><p>Device identifiers (hostname, IP address, or MAC address) for host and peer in session. Click on </p>
<p>{{% imgOld 63 %}}</p>
to open associated device card.</td>
</tr>
<tr class="odd">
<td><p></p>
<p>{{% imgOld 64 %}}</p>
,
<p>{{% imgOld 65 %}}</p></td>
<td><p>Indication of host role, primary</p>
<p>{{% imgOld 66 %}}</p>
or secondary
<p>{{% imgOld 67 %}}</p></td>
</tr>
<tr class="even">
<td><p>Timestamps</p></td>
<td><p>When changes to the configuration file have occurred, the date and time are indicated. Click the time to see the changed file.</p></td>
</tr>
<tr class="odd">
<td><p>Configuration File</p></td>
<td><p>When <strong>File</strong> is selected, the configuration file as it was at the selected time is shown. When <strong>Diff</strong> is selected, the configuration file at the selected time is shown on the left and the configuration file at the previous timestamp is shown on the right. Differences are highlighted.</p>
<p><strong>Note</strong>: If no configuration file changes have been made, the card shows no results.</p></td>
</tr>
</tbody>
</table>

The full screen LLDP Session card provides tabs for all LLDP sessions
and all events.

{{% imgOld 68 %}}

<table>
<colgroup>
<col style="width: 20%" />
<col style="width: 80%" />
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
<td><p>Network Services | LLDP</p></td>
</tr>
<tr class="even">
<td><p><img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/close.svg", height="18", width="18"/></p></td>
<td><p>Closes full screen card and returns to workbench</p></td>
</tr>
<tr class="odd">
<td><p>Time period</p></td>
<td><p>Range of time in which the displayed data was collected; applies to all card sizes; select an alternate time period by clicking </p>
<p>{{% imgOld 70 %}}</p></td>
</tr>
<tr class="even">
<td><p>Results</p></td>
<td><p>Number of results found for the selected tab</p></td>
</tr>
<tr class="odd">
<td><p>All LLDP Sessions tab</p></td>
<td><p>Displays all LLDP sessions on the host device. By default, the session list is sorted by <strong>hostname</strong>. This tab provides the following additional data about each session:</p>
<ul>
<li><p><strong>DB State</strong>: Session state of the DB.</p></li>
<li><p><strong>Ifname</strong>: Name of the host interface where LLDP session is running</p></li>
<li><p><strong>LLDP</strong> <strong>Peer</strong>:</p>
<ul>
<li><p>Os: Operating system (OS) used by peer device. Values include Cumulus Linux, RedHat, Ubuntu, and CentOS.</p></li>
<li><p>Osv: Version of the OS used by peer device. Example values include 3.7.3, 2.5.x, 16.04, 7.1.</p></li>
<li><p>Bridge: Indicates whether the peer device is a bridge (true) or not (false)</p></li>
<li><p>Router: Indicates whether the peer device is a router (true) or not (false)</p></li>
<li><p>Station: Indicates whether the peer device is a station (true) or not (false)</p></li>
</ul></li>
<li><p><strong>OPID</strong>: LLDP service identifier</p></li>
<li><p><strong>Peer</strong>:</p>
<ul>
<li><p>Hostname: User-defined name for the peer device</p></li>
<li><p>Ifname: Name of the peer interface where the session is running</p></li>
</ul></li>
<li><p><strong>Timestamp</strong>: Date and time that the session was started, deleted, updated, or marked dead (device is down)</p></li>
</ul></td>
</tr>
<tr class="even">
<td><p>All Events tab</p></td>
<td><p>Displays all events network-wide. By default, the event list is sorted by <strong>time</strong>, with the most recent events listed first. The tab provides the following additional data about each event:</p>
<ul>
<li><p><strong>Message</strong>: Text description of an event. Example: LLDP Session with host leaf02 swp6 modified fields leaf06 swp21</p></li>
<li><p><strong>Source</strong>: Hostname of network device that generated the event</p></li>
<li><p><strong>Severity</strong>: Importance of the event. Values include critical, warning, info, and debug.</p></li>
<li><p><strong>Type</strong>: Network protocol or service generating the event. This always has a value of <em>lldp</em> in this card workflow.</p></li>
</ul></td>
</tr>
<tr class="odd">
<td><p>Export</p></td>
<td><p>Enables export of all or selected items in a CSV or JSON formatted file</p></td>
</tr>
<tr class="even">
<td><p></p>
<p>{{% imgOld 71 %}}</p></td>
<td><p>Enables manipulation of table display; choose columns to display and reorder columns</p></td>
</tr>
</tbody>
</table>

### View Session Status Summary

A summary of the LLDP session is available from the LLDP Session card
workflow, showing the node and its peer and current status.

To view the summary:

1.  Open the full screen LLDP Service card

2.  Double-click on a session. The full screen card closes
    automatically.

3.  Locate the medium LLDP Session card.

4.  Optionally, open the small LLDP Session card.  
    
    {{% imgOld 72 %}}
    
    {{% imgOld 73 %}}

### View LLDP Session Neighbor State Changes

You can view the neighbor state for a given LLDP session from the medium
and large LLDP Session cards. For a given time period, you can determine
the stability of the LLDP session between two devices. If you
experienced connectivity issues at a particular time, you can use these
cards to help verify the state of the neighbor. If the neighbor was not
alive more than it was alive, you can then investigate further into
possible causes.

To view the neighbor availability for a given LLDP session on the medium
card:

1.  Open the full screen LLDP Service card.

2.  Double-click on a session. The full screen card closes
    automatically.

3.  Locate the medium LLDP Session card.
    
    {{% imgOld 74 %}}

In this example, the heat map tells us that this LLDP session has been
able to detect a neighbor for the entire time period.

From this card, you can also view the hostname and interface name for both the host and peer.

To view the neighbor availability for a given LLDP session on the large
LLDP Session card, open that card.

{{% imgOld 75 %}}

From this card, you can also view the alarm and info event counts, host
interface name, peer hostname, and peer interface identifying the
session in more detail.

### View Changes to the LLDP Service Configuration File

Each time a change is made to the configuration file for the LLDP
service, NetQ logs the change and enables you to compare it with the
last version. This can be useful when you are troubleshooting potential
causes for alarms or sessions losing their connections.

To view the configuration file changes:

1.  Open the large LLDP Session card.

2.  Hover over the card and click {{% imgOld 76 %}} to open the **LLDP Configuration File Evolution** tab.

3.  Select the time of interest on the left; when a change may have
    impacted the performance. Scroll down if needed.

### View All LLDP Session Details

You can view all stored attributes of all of the LLDP sessions
associated with the two devices on this card.

To view all session details, open the full screen LLDP Session card, and
click the **All LLDP Sessions** tab.

{{% imgOld 77 %}}

To return to your workbench, click {{% imgOld 78 %}} in the top right of the card.

### View All Events

You can view all of the alarm and info events in the network.

To view all events, open the full screen LLDP Session card, and click
the **All Events** tab.

{{% imgOld 79 %}}

Where to go next depends on what data you see, but a few options
include:

- Open the **All LLDP Sessions** tabs to look more closely at the
  details of the sessions between these two devices.
- Sort on other parameters:
  - by **Message** to determine the frequency of particular events
  - by **Severity** to determine the most critical events
  - by **Time** to find events that may have occurred at a particular time to try to correlate them with other system
events
- Export data to a file
- Return to your workbench by clicking {{% imgOld 80 %}} in the top right corner
