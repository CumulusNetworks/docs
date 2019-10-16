---
title: Monitor the MLAG Service
author: Cumulus Networks
weight: 167
pageID: 12321372
product: Cumulus NetQ
version: 2.2
imgData: cumulus-netq-22
siteSlug: cumulus-netq-22
---
The Cumulus NetQ UI enables operators to view the health of the MLAG
service on a network-wide and a per session basis, giving greater
insight into all aspects of the service. This is accomplished through
two card workflows, one for the service and one for the session. They
are described separately here.

{{%notice note%}}

**MLAG or CLAG?**
The Cumulus Linux implementation of MLAG is referred to by other vendors
as CLAG, MC-LAG or VPC. The Cumulus NetQ UI uses the CLAG terminology.

{{%/notice%}}

## Monitor the CLAG Service (All Sessions)

With NetQ, you can monitor the number of nodes running the CLAG service,
view sessions running, and view alarms triggered by the CLAG service.
For an overview and how to configure CLAG in your data center network,
refer to [Multi-Chassis Link Aggregation - MLAG](/cumulus-linux/Layer-2/Multi-Chassis-Link-Aggregation-MLAG/).

### CLAG Service Card Workflow Summary

The small CLAG Service card displays:

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
<td><p><img src="https://icons.cumulusnetworks.com/05-Internet-Networks-Servers/01-Worldwide-Web/network-information.svg", height="18", width="18"/></p></td>
<td><p>Indicates data is for all sessions of a Network Service or Protocol</p></td>
</tr>
<tr class="even">
<td><p>Title</p></td>
<td><p>CLAG: All CLAG Sessions, or the CLAG Service</p></td>
</tr>
<tr class="odd">
<td><p><img src="https://icons.cumulusnetworks.com/04-Programing-Apps-Websites/10-Apps/monitor-play.svg", height="18", width="18"/></p></td>
<td><p>Total number of switches with the CLAG service enabled during the designated time period</p></td>
</tr>
<tr class="even">
<td><p><img src="https://icons.cumulusnetworks.com/01-Interface-Essential/20-Alert/alarm-bell.svg", height="18", width="18"/></p></td>
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
<td><p>Time period</p></td>
<td><p>Range of time in which the displayed data was collected; applies to all card sizes</p></td>
</tr>
<tr class="even">
<td><p><img src="https://icons.cumulusnetworks.com/05-Internet-Networks-Servers/01-Worldwide-Web/network-information.svg", height="18", width="18"/></p></td>
<td><p>Indicates data is for all sessions of a Network Service or Protocol</p></td>
</tr>
<tr class="odd">
<td><p>Title</p></td>
<td><p>Network Services | All CLAG Sessions</p></td>
</tr>
<tr class="even">
<td><p><img src="https://icons.cumulusnetworks.com/04-Programing-Apps-Websites/10-Apps/monitor-play.svg", height="18", width="18"/></p></td>
<td><p>Total number of switches with the CLAG service enabled during the designated time period</p></td>
</tr>
<tr class="odd">
<td><p><img src="https://icons.cumulusnetworks.com/01-Interface-Essential/20-Alert/alarm-bell.svg", height="18", width="18"/></p></td>
<td><p>Total number of CLAG-related alarms received during the designated time period</p></td>
</tr>
<tr class="even">
<td><p><img src="https://icons.cumulusnetworks.com/48-Maps-Navigation/11-Pins-Style%20Two/style-two-pin-off-map.svg", height="18", width="18"/></p></td>
<td><p>Total number of sessions with an inactive backup IP address during the designated time period</p></td>
</tr>
<tr class="odd">
<td><p><img src="https://icons.cumulusnetworks.com/01-Interface-Essential/27-Link-Unlink/link-broken-1.svg", height="18", width="18"/></p></td>
<td><p>Total number of bonds with only a single connection during the designated time period</p></td>
</tr>
<tr class="even">
<td><p>Total Nodes Running chart</p></td>
<td><p>Distribution of switches and hosts with the CLAG service enabled during the designated time period, and a total number of nodes running the service currently.
<p><strong>Note</strong>: The node count here may be different than the count in the summary bar. For example, the number of nodes running CLAG last week or last month might be more or less than the number of nodes running CLAG currently.</p></td>
</tr>
<tr class="odd">
<td><p>Total Open Alarms chart</p></td>
<td><p>Distribution of CLAG-related alarms received during the designated time period, and the total number of current CLAG-related alarms in the network.</p>
<p><strong>Note</strong>: The alarm count here may be different than the count in the summary bar. For example, the number of new alarms received in this time period does not take into account alarms that have already been received and are still active. You might have no new alarms, but still have a total number of alarms present on the network of 10.</p></td>
</tr>
<tr class="even">
<td><p>Total Sessions chart</p></td>
<td><p>Distribution of CLAG sessions running during the designated time period, and the total number of sessions running on the network currently</p></td>
</tr>
</tbody>
</table>

The large CLAG service card contains two tabs.

The *All CLAG Sessions Summary* tab which displays:

{{% imgOld 10 %}}

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
<td><p>Time period</p></td>
<td><p>Range of time in which the displayed data was collected; applies to all card sizes</p></td>
</tr>
<tr class="even">
<td><p><img src="https://icons.cumulusnetworks.com/05-Internet-Networks-Servers/01-Worldwide-Web/network-information.svg", height="18", width="18"/></p></td>
<td><p>Indicates data is for all sessions of a Network Service or Protocol</p></td>
</tr>
<tr class="odd">
<td><p>Title</p></td>
<td><p>All CLAG Sessions Summary</p></td>
</tr>
<tr class="even">
<td><p><img src="https://icons.cumulusnetworks.com/04-Programing-Apps-Websites/10-Apps/monitor-play.svg", height="18", width="18"/></p></td>
<td><p>Total number of switches with the CLAG service enabled during the designated time period</p></td>
</tr>
<tr class="odd">
<td><p><img src="https://icons.cumulusnetworks.com/01-Interface-Essential/20-Alert/alarm-bell.svg", height="18", width="18"/></p></td>
<td><p>Total number of CLAG-related alarms received during the designated time period</p></td>
</tr>
<tr class="even">
<td><p>Total Nodes Running chart</p></td>
<td><p>Distribution of switches and hosts with the CLAG service enabled during the designated time period, and a total number of nodes running the service currently.
<p><strong>Note</strong>: The node count here may be different than the count in the summary bar. For example, the number of nodes running CLAG last week or last month might be more or less than the number of nodes running CLAG currently.</p></td>
</tr>
<tr class="odd">
<td><p>Total Sessions chart</p></td>
<td><p>Distribution of CLAG sessions running during the designated time period, and the total number of sessions running on the network currently</p></td>
</tr>
<tr class="even">
<td><p>Total Sessions with Inactive-backup-ip chart</p></td>
<td><p>Distribution of sessions without an active backup IP defined during the designated time period, and the total number of these sessions running on the network currently</p></td>
</tr>
<tr class="odd">
<td><p>Table/Filter options</p></td>
<td><p>When the <strong>Switches with Most Sessions</strong> filter is selected, the table displays switches running CLAG sessions in decreasing order of session count—devices with the largest number of sessions are listed first</p>
<p>When the <strong>Switches with Most Unestablished Sessions</strong> filter is selected, the table displays switches running CLAG sessions in decreasing order of unestablished session count—devices with the largest number of unestablished sessions are listed first</p></td>
</tr>
<tr class="even">
<td><p>Show All Sessions</p></td>
<td><p>Link to view all CLAG sessions in the full screen card</p></td>
</tr>
</tbody>
</table>

The *All CLAG Alarms* tab which displays:

{{< figure src="https://dkahegywkrw3e.cloudfront.net/images/netq/ntwk-svcs-all-clag-large-alarms-tab.png" width="500" >}}

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
<td><p>Time period</p></td>
<td><p>Range of time in which the displayed data was collected; applies to all card sizes</p></td>
</tr>
<tr class="even">
<td><p><img src="https://icons.cumulusnetworks.com/01-Interface-Essential/20-Alert/alarm-bell.svg", height="18", width="18"/> (in header)</p></td>
<td><p>Indicates alarm data for all CLAG sessions</p></td>
</tr>
<tr class="odd">
<td><p>Title</p></td>
<td><p>Network Services | All CLAG Alarms (visible when you hover over card)</p></td>
</tr>
<tr class="even">
<td><p><img src="https://icons.cumulusnetworks.com/04-Programing-Apps-Websites/10-Apps/monitor-play.svg", height="18", width="18"/></p></td>
<td><p>Total number of switches with the CLAG service enabled during the designated time period</p></td>
</tr>
<tr class="odd">
<td><p><img src="https://icons.cumulusnetworks.com/01-Interface-Essential/20-Alert/alarm-bell.svg", height="18", width="18"/> (in summary bar)</p></td>
<td><p>Total number of CLAG-related alarms received during the designated time period</p></td>
</tr>
<tr class="even">
<td><p>Total Alarms chart</p></td>
<td><p>Distribution of CLAG-related alarms received during the designated time period, and the total number of current CLAG-related alarms in the network.</p>
<p><strong>Note</strong>: The alarm count here may be different than the count in the summary bar. For example, the number of new alarms received in this time period does not take into account alarms that have already been received and are still active. You might have no new alarms, but still have a total number of alarms present on the network of 10.</p></td>
</tr>
<tr class="odd">
<td><p>Table/Filter options</p></td>
<td><p>When the <strong>Events by Most Active Device</strong> filter is selected, the table displays switches running CLAG sessions in decreasing order of alarm count—devices with the largest number of sessions are listed first</p></td>
</tr>
<tr class="even">
<td><p>Show All Sessions</p></td>
<td><p>Link to view all CLAG sessions in the full screen card</p></td>
</tr>
</tbody>
</table>

The full screen CLAG Service card provides tabs for all switches, all
sessions, and all alarms.

{{<figure src="https://dkahegywkrw3e.cloudfront.net/images/netq/ntwk-svcs-all-clag-fullscr-222.png" width="700">}}

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
<td><p>Network Services | CLAG</p></td>
</tr>
<tr class="even">
<td><p><img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/close.svg", height="14", width="14"/></p></td>
<td><p>Closes full screen card and returns to workbench</p></td>
</tr>
<tr class="odd">
<td><p>Time period</p></td>
<td><p>Range of time in which the displayed data was collected; applies to all card sizes; select an alternate time period by clicking <img src="https://icons.cumulusnetworks.com/52-Arrows-Diagrams/01-Arrows/arrow-button-down-2.svg", height="14", width="14"/></p></td>
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
<li><p>Model Id: Identifier of networking ASIC model. Example values include BCM56960 and BCM56854.</p></li>
<li><p>Ports: Indicates port configuration of the switch. Example values include 32 x 100G-QSFP28, 48 x 10G-SFP+, and 6 x 40G-QSFP+.</p></li>
<li><p>Vendor: Manufacturer of the chip. Example values include Broadcom and Mellanox.</p></li>
</ul></li>
<li><p><strong>CPU</strong></p>
<ul>
<li><p>Arch: Microprocessor architecture type. Values include x86_64 (Intel), ARMv7 (AMD), and PowerPC.</p></li>
<li><p>Max Freq: Highest rated frequency for CPU. Example values include 2.40 GHz and 1.74 GHz.</p></li>
<li><p>Model: Chip family. Example values include Intel Atom C2538 and Intel Atom C2338.</p></li>
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
<li><p>Model: Manufacturer's model name. Examples values include AS7712-32X and S4048-ON.</p></li>
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
<li><p><strong>Message</strong>: Text description of a BGP-related event. Example: Clag conflicted bond changed from swp7 swp8 to swp9 swp10</p></li>
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
<td><p><img src="https://icons.cumulusnetworks.com/01-Interface-Essential/12-Settings/cog-1.svg", height="18", width="18"/></p></td>
<td><p>Enables manipulation of table display; choose columns to display and reorder columns</p></td>
</tr>
</tbody>
</table>

### View Service Status Summary

A summary of the CLAG service is available from the CLAG Service card
workflow, including the number of nodes running the service, the number
of CLAG-related alarms, and a distribution of those alarms.

To view the summary, open the small CLAG Service card.

{{% imgOld 18 %}}

For more detail, select a different size CLAG Service card.

### View the Distribution of Sessions and Alarms

It is useful to know the number of network nodes running the CLAG
protocol over a period of time, as it gives you insight into the amount
of traffic associated with and breadth of use of the protocol. It is
also useful to compare the number of nodes running CLAG with the alarms
present at the same time to determine if there is any correlation
between the issues and the ability to establish a CLAG session.

To view these distributions, open the medium CLAG Service card.

{{% imgOld 19 %}}

If a visual correlation is apparent, you can dig a little deeper with
the large CLAG Service card tabs.

### View Devices with the Most CLAG Sessions

You can view the load from CLAG on your switches using the large CLAG
Service card. This data enables you to see which switches are handling
the most CLAG traffic currently, validate that is what is expected based
on your network design, and compare that with data from an earlier time
to look for any differences.

To view switches and hosts with the most CLAG sessions:

1.  Open the large CLAG Service card.
2.  Select **Switches with Most Sessions** from the filter above the
    table.  
    The table content is sorted by this characteristic, listing nodes
    running the most CLAG sessions at the top. Scroll down to view those
    with the fewest sessions.

    {{% imgOld 20 %}}

To compare this data with the same data at a previous time:

1.  Open another large CLAG Service card.
2.  Move the new card next to the original card if needed.
3.  Change the time period for the data on the new card by hovering over
    the card and clicking <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/18-Time/time-stopwatch.svg", height="18", width="18"/>.
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

### View Devices with the Most Unestablished CLAG Sessions

You can identify switches that are experiencing difficulties
establishing CLAG sessions; both currently and in the past.

To view switches with the most unestablished CLAG sessions:

1.  Open the large CLAG Service card.
2.  Select **Switches with Most Unestablished Sessions** from the filter above the table.
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
    probable causes. Refer to [Monitor Switches](../../Monitor-Devices/Monitor-Switches/).

  - Click **Show All Sessions** to investigate all CLAG sessions with
    events in the full screen card.

### View Switches with the Most CLAG-related Alarms

Switches experiencing a large number of CLAG alarms may indicate a
configuration or performance issue that needs further investigation. You
can view the switches sorted by the number of CLAG alarms and then use
the Switches card workflow or the Alarms card workflow to gather more
information about possible causes for the alarms.

To view switches with most CLAG alarms:

1.  Open the large CLAG Service card.
2.  Hover over the header and click <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/20-Alert/alarm-bell.svg", height="18", width="18"/>.
3.  Select **Events by Most Active Device** from the filter above the
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

### View All CLAG Events

The CLAG Service card workflow enables you to view all of the CLAG
events in the designated time period.

To view all CLAG events:

1.  Open the full screen CLAG Service card.
2.  Click **All Alarms** tab.

    {{<figure src="https://dkahegywkrw3e.cloudfront.net/images/netq/ntwk-svcs-all-clag-fullscr-alarms-tab-222.png" width="700">}}

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
  - Return to your workbench by clicking {{% imgOld 34 %}} in the top right corner

### View Details About All Switches Running CLAG

You can view all stored attributes of all switches running CLAG in your
network in the full-screen card.

To view all switch details, open the full screen CLAG Service card, and
click the **All Switches** tab.

{{<figure src="https://dkahegywkrw3e.cloudfront.net/images/netq/ntwk-svcs-all-clag-fullscr-222.png" width="700">}}

To return to your workbench, click {{% imgOld 36 %}} in the top right corner.

### Take Actions on Data Displayed in Results List

In the full screen BGP Service card, you can determine which results are
displayed in the results list, and which are exported.

To take actions on the data, click in the blank column at the very left
of a row. A checkbox appears, selecting that switch, session, or alarm,
and an edit menu is shown at the bottom of the card (shown enlarged
here).

{{<figure src="https://dkahegywkrw3e.cloudfront.net/images/netq/ntwk-svcs-all-clag-fullscr-switches-tab-selected-hosts-222.png" width="700">}}

{{<figure src="https://dkahegywkrw3e.cloudfront.net/images/netq/ntwk-svcs-fullscr-edit-menu-4selected-222.png" width="700">}}

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

## Monitor a Single CLAG Session

With NetQ, you can monitor the number of nodes running the CLAG service,
view switches with the most peers alive and not alive, and view alarms
triggered by the CLAG service. For an overview and how to configure CLAG
in your data center network, refer to
[Multi-Chassis Link Aggregation - MLAG](/cumulus-linux/Layer-2/Multi-Chassis-Link-Aggregation-MLAG/).

{{%notice note%}}

To access the single session cards, you must open the full screen CLAG
Service, click the All Sessions tab, select the desired session, then click <img src="https://icons.cumulusnetworks.com/44-Entertainment-Event-Hobbies/02-Card-Games/card-game-diamond.svg",  height="18", width="18"/> (Open Cards).

{{%/notice%}}

### Granularity of Data Shown Based on Time Period

On the medium and large single CLAG session cards, the status of the
peers is represented in heat maps stacked vertically; one for peers that
are reachable (alive), and one for peers that are unreachable (not
alive). Depending on the time period of data on the card, the number of
smaller time blocks used to indicate the status varies. A vertical stack
of time blocks, one from each map, includes the results from all checks
during that time. The results are shown by how saturated the color is
for each block. If all peers during that time period were alive for the
entire time block, then the top block is 100% saturated (white) and the
not alive block is zero percent saturated (gray). As peers that are not
alive increase in saturation, the peers that are alive block is
proportionally reduced in saturation. An example heat map for a time
period of 24 hours is shown here with the most common time periods in
the table showing the resulting time blocks.

{{% imgOld 39 %}}

| Time Period | Number of Runs | Number Time Blocks | Amount of Time in Each Block |
| ----------- | -------------- | ------------------ | ---------------------------- |
| 6 hours     | 18             | 6                  | 1 hour                       |
| 12 hours    | 36             | 12                 | 1 hour                       |
| 24 hours    | 72             | 24                 | 1 hour                       |
| 1 week      | 504            | 7                  | 1 day                        |
| 1 month     | 2,086          | 30                 | 1 day                        |
| 1 quarter   | 7,000          | 13                 | 1 week                       |

### CLAG Session Card Workflow Summary

The small CLAG Session card displays:

{{% imgOld 40 %}}

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
<td><p><img src="https://icons.cumulusnetworks.com/05-Internet-Networks-Servers/05-Network/signal-loading.svg", height="22", width="22"/></p></td>
<td><p>Indicates data is for a single session of a Network Service or Protocol</p></td>
</tr>
<tr class="even">
<td><p>Title</p></td>
<td><p>CLAG Session</p></td>
</tr>
<tr class="odd">
<td><p> </p></td>
<td><p>Device identifiers (hostname, IP address, or MAC address) for host and peer in session.</p></td>
</tr>
<tr class="even">
<td><p><img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/check-circle-1.svg", height="18", width="18"/>, <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/remove-shield.svg", height="18", width="18"/></p></td>
<td><p>Indication of host role, primary <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/check-circle-1.svg", height="18", width="18"/> or secondary <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/remove-shield.svg", height="18", width="18"/></p></td>
</tr>
</tbody>
</table>

The medium CLAG Session card displays:

{{< figure src="https://dkahegywkrw3e.cloudfront.net/images/netq/ntwk-svcs-single-session-clag-medium.png" width="200" >}}

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
<td><p>Time period (in header)</p></td>
<td><p>Range of time in which the displayed data was collected; applies to all card sizes</p></td>
</tr>
<tr class="even">
<td><p><img src="https://icons.cumulusnetworks.com/05-Internet-Networks-Servers/05-Network/signal-loading.svg", height="22", width="22"/></p></td>
<td><p>Indicates data is for a single session of a Network Service or Protocol</p></td>
</tr>
<tr class="odd">
<td><p>Title</p></td>
<td><p>Network Services | CLAG Session</p></td>
</tr>
<tr class="even">
<td><p><img src="https://icons.cumulusnetworks.com/44-Entertainment-Event-Hobbies/02-Card-Games/card-game-diamond.svg", height="18", width="18"/></p></td>
<td><p>Device identifiers (hostname, IP address, or MAC address) for host and peer in session. Arrow points from the host to the peer. Click <img src="https://icons.cumulusnetworks.com/44-Entertainment-Event-Hobbies/02-Card-Games/card-game-diamond.svg", height="18", width="18"/> to open associated device card.</p></td>
</tr>
<tr class="odd">
<td><p><img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/check-circle-1.svg", height="18", width="18"/>, <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/remove-shield.svg", height="18", width="18"/></p></td>
<td><p>Indication of host role, primary <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/check-circle-1.svg", height="18", width="18"/> or secondary <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/remove-shield.svg", height="18", width="18"/></p></td>
</tr>
<tr class="even">
<td><p>Time period (above chart)</p></td>
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

The large CLAG Session card contains two tabs.

The *Session Summary* tab displays:

{{% imgOld 54 %}}

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
<td><p>Time period</p></td>
<td><p>Range of time in which the displayed data was collected; applies to all card sizes</p></td>
</tr>
<tr class="even">
<td><p><img src="https://icons.cumulusnetworks.com/05-Internet-Networks-Servers/05-Network/signal-loading.svg", height="22", width="22"/></p></td>
<td><p>Indicates data is for a single session of a Network Service or Protocol</p></td>
</tr>
<tr class="odd">
<td><p>Title</p></td>
<td><p>(Network Services | CLAG Session) Session Summary</p></td>
</tr>
<tr class="even">
<td><p><img src="https://icons.cumulusnetworks.com/44-Entertainment-Event-Hobbies/02-Card-Games/card-game-diamond.svg", height="18", width="18"/></p></td>
<td><p>Device identifiers (hostname, IP address, or MAC address) for host and peer in session. Arrow points from the host to the peer. Click <img src="https://icons.cumulusnetworks.com/44-Entertainment-Event-Hobbies/02-Card-Games/card-game-diamond.svg", height="18", width="18"/> to open associated device card.</p></td>
</tr>
<tr class="odd">
<td><p><img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/check-circle-1.svg", height="18", width="18"/>, <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/remove-shield.svg", height="18", width="18"/></p></td>
<td><p>Indication of host role, primary <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/check-circle-1.svg", height="18", width="18"/> or secondary <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/remove-shield.svg", height="18", width="18"/></p></td>
</tr>
<tr class="even">
<td><p>Alarm Count Chart</p></td>
<td><p>Distribution and count of CLAG alarm events over the given time period.</p></td>
</tr>
<tr class="odd">
<td><p>Info Count Chart</p></td>
<td><p>Distribution and count of CLAG info events over the given time period.</p></td>
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

The *Configuration File Evolution* tab displays:

{{% imgOld 62 %}}

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
<td><p>Time period</p></td>
<td><p>Range of time in which the displayed data was collected; applies to all card sizes</p></td>
</tr>
<tr class="even">
<td><p><img src="https://icons.cumulusnetworks.com/16-Files-Folders/01-Common-Files/common-file-settings-1.svg", height="18", width="18"/></p></td>
<td><p>Indicates configuration file information for a single session of a Network Service or Protocol</p></td>
</tr>
<tr class="odd">
<td><p>Title</p></td>
<td><p>(Network Services | CLAG Session) Configuration File Evolution</p></td>
</tr>
<tr class="even">
<td><p>{{% imgOld 64 %}}</p></td>
<td><p>Device identifiers (hostname, IP address, or MAC address) for host and peer in session. Click on {{% imgOld 65 %}} to open associated device card.</td>
</tr>
<tr class="even">
<td><p><img src="https://icons.cumulusnetworks.com/44-Entertainment-Event-Hobbies/02-Card-Games/card-game-diamond.svg", height="18", width="18"/></p></td>
<td><p>Device identifiers (hostname, IP address, or MAC address) for host and peer in session. Arrow points from the host to the peer. Click <img src="https://icons.cumulusnetworks.com/44-Entertainment-Event-Hobbies/02-Card-Games/card-game-diamond.svg", height="18", width="18"/> to open associated device card.</p></td>
</tr>
<tr class="odd">
<td><p><img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/check-circle-1.svg", height="18", width="18"/>, <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/remove-shield.svg", height="18", width="18"/></p></td>
<td><p>Indication of host role, primary <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/check-circle-1.svg", height="18", width="18"/> or secondary <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/remove-shield.svg", height="18", width="18"/></p></td>
</tr>
<tr class="even">
<td><p>Timestamps</p></td>
<td><p>When changes to the configuration file have occurred, the date and time are indicated. Click the time to see the changed file.</p></td>
</tr>
<tr class="odd">
<td><p>Configuration File</p></td>
<td><p>When <strong>File</strong> is selected, the configuration file as it was at the selected time is shown.</p>
<p>When <strong>Diff</strong> is selected, the configuration file at the selected time is shown on the left and the configuration file at the previous timestamp is shown on the right. Differences are highlighted.</p>
</td>
</tr>
</tbody>
</table>

The full screen CLAG Session card provides tabs for all CLAG sessions
and all events.

{{<figure src="https://dkahegywkrw3e.cloudfront.net/images/netq/ntwk-svcs-single-clag-fullscr-222.png" width="700">}}

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
<td><p>Network Services | CLAG</p></td>
</tr>
<tr class="even">
<td><p><img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/close.svg", height="14", width="14"/></p></td>
<td><p>Closes full screen card and returns to workbench</p></td>
</tr>
<tr class="odd">
<td><p>Time period</p></td>
<td><p>Range of time in which the displayed data was collected; applies to all card sizes; select an alternate time period by clicking <img src="https://icons.cumulusnetworks.com/52-Arrows-Diagrams/01-Arrows/arrow-button-down-2.svg", height="14", width="14"/></p></td>
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
<li><p><strong>Message</strong>: Text description of an event. Example: Clag conflicted bond changed from swp7 swp8 to swp9 swp10</p></li>
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
<td><p><img src="https://icons.cumulusnetworks.com/01-Interface-Essential/12-Settings/cog-1.svg", height="18", width="18"/></p></td>
<td><p>Enables manipulation of table display; choose columns to display and reorder columns</p></td>
</tr>
</tbody>
</table>

### View Session Status Summary

A summary of the CLAG session is available from the CLAG Session card
workflow, showing the node and its peer and current status.

To view the summary:

1.  Open the full screen CLAG Service card.
2.  Select a session from the listing to view.
3.  Close the full screen card to view the medium CLAG Session card.  

    {{% imgOld 74 %}}

    {{% imgOld 75 %}}

    In the left example, we see that the tor1 switch plays the secondary
    role in this session with the switch at 44:38:39:ff:01:01. In the
    right example, we see that the leaf03 switch plays the primary role
    in this session with leaf04.

### View CLAG Session Peering State Changes

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

    {{% imgOld 76 %}}

    In this example, the peer switch has been alive for the entire
    24-hour period.

From this card, you can also view the node role, peer role and state,
and CLAG system MAC address which identify the session in more detail.

To view the peering state transitions for a given CLAG session on the
large CLAG Session card, open that card.

{{% imgOld 77 %}}

From this card, you can also view the alarm and info event counts, node
role, peer role, state, and interface, CLAG system MAC address, active
backup IP address, single, dual, conflicted, and protocol down bonds,
and the VXLAN anycast address identifying the session in more detail.

### View Changes to the CLAG Service Configuration File

Each time a change is made to the configuration file for the CLAG
service, NetQ logs the change and enables you to compare it with the
last version. This can be useful when you are troubleshooting potential
causes for alarms or sessions losing their connections.

To view the configuration file changes:

1.  Open the large CLAG Session card.
2.  Hover over the card and click <img src="https://icons.cumulusnetworks.com/16-Files-Folders/01-Common-Files/common-file-settings-1.svg", height="18", width="18"/> to open the **Configuration File Evolution** tab.
3.  Select the time of interest on the left; when a change may have
    impacted the performance. Scroll down if needed.

    {{% imgOld 79 %}}

4.  Choose between the **File** view and the **Diff** view (selected
    option is dark; File by default).  
    The File view displays the content of the file for you to review.

    {{% imgOld 80 %}}

    The Diff view displays the changes between this version (on left)
    and the most recent version (on right) side by side. The changes are
    highlighted in red and green. In this example, we don't have any
    changes after this first creation, so the same file is shown on both
    sides and no highlighting is present.

    {{% imgOld 81 %}}

### All CLAG Session Details

You can view all stored attributes of all of the CLAG sessions
associated with the two devices on this card.

To view all session details, open the full screen CLAG Session card, and
click the **All CLAG Sessions** tab.

{{<figure src="https://dkahegywkrw3e.cloudfront.net/images/netq/ntwk-svcs-single-clag-fullscr-222.png" width="700">}}

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
  - Return to your workbench by clicking {{% imgOld 83 %}} in the top right corner

### View All CLAG Session Events

You can view all of the alarm and info events for the two devices on
this card.

To view all events, open the full screen CLAG Session card, and click
the **All Events** tab.

{{<figure src="https://dkahegywkrw3e.cloudfront.net/images/netq/ntwk-svcs-single-clag-fullscr-events-222.png" width="700">}}

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
  - Return to your workbench by clicking {{% imgOld 85 %}} in the top right corner
