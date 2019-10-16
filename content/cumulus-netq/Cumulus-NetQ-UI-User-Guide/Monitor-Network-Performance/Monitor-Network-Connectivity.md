---
title: Monitor Network Connectivity
author: Cumulus Networks
weight: 171
aliases:
 - /display/NETQ/Monitor+Network+Connectivity
 - /pages/viewpage.action?pageId=12321680
pageID: 12321680
product: Cumulus NetQ
version: 2.3
imgData: cumulus-netq
siteSlug: cumulus-netq
---
It is helpful to verify that communications are freely flowing between
the various devices in your network. You can verify the connectivity
between two devices in both an adhoc fashion and by defining
connectivity checks to occur on a scheduled basis. There are three card
workflows which enable you to view connectivity, the Trace Request,
On-demand Trace Results, and Scheduled Trace Results.

## Create a Trace Request

Two types of connectivity checks can be run–an immediate (on-demand)
trace and a scheduled trace. The Trace Request card workflow is used to
configure and run both of these trace types.

### Trace Request Card Workflow Summary

The small Trace Request card displays:

{{<figure src="/images/uploads/trace-request-small-card.png" width="200">}}

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 85%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Item</p></th>
<th><p>Description</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><img src="https://icons.cumulusnetworks.com/48-Maps-Navigation/06-Trip/trip-pins.svg", height="18", width="18"/></p></td>
<td><p>Indicates a trace request</p></td>
</tr>
<tr class="even">
<td><p>Select Trace list</p></td>
<td><p>Select a scheduled trace request from the list</p></td>
</tr>
<tr class="odd">
<td><p>Go</p></td>
<td><p>Click to start the trace now</p></td>
</tr>
</tbody>
</table>

The medium Trace Request card displays:

{{<figure src="/images/netq/trace-request-medium-222.png" width="200">}}

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 85%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Item</p></th>
<th><p>Description</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><img src="https://icons.cumulusnetworks.com/48-Maps-Navigation/06-Trip/trip-pins.svg", height="18", width="18"/></p></td>
<td><p>Indicates a trace request</p></td>
</tr>
<tr class="even">
<td><p>Title</p></td>
<td><p>New Trace Request</p></td>
</tr>
<tr class="odd">
<td><p>New Trace Request</p></td>
<td><p>Create a new layer 3 trace request. Use the large Trace Request card to create a new layer 2 or 3 request.</p></td>
</tr>
<tr class="even">
<td><p>Source</p></td>
<td><p>(Required) Hostname or IP address of device where to begin the trace</p></td>
</tr>
<tr class="odd">
<td><p>Destination</p></td>
<td><p>(Required) IP address of device where to end the trace</p></td>
</tr>
<tr class="even">
<td><p>Run Now</p></td>
<td><p>Start the trace now</p></td>
</tr>
</tbody>
</table>

The large Trace Request card displays:

{{< figure src="/images/netq/trace-request-large-222.png" width="500" >}}

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 85%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Item</p></th>
<th><p>Description</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><img src="https://icons.cumulusnetworks.com/48-Maps-Navigation/06-Trip/trip-pins.svg", height="18", width="18"/></p></td>
<td><p>Indicates a trace request</p></td>
</tr>
<tr class="even">
<td><p>Title</p></td>
<td><p>New Trace Request</p></td>
</tr>
<tr class="odd">
<td><p>Trace selection</p></td>
<td><p>Leave <em>New Trace Request</em> selected to create a new request, or choose a scheduled request from the list.</p></td>
</tr>
<tr class="even">
<td><p>Source</p></td>
<td><p>(Required) Hostname or IP address of device where to begin the trace.</p></td>
</tr>
<tr class="odd">
<td><p>Destination</p></td>
<td><p>(Required) Ending point for the trace. For layer 2 traces, value must be a MAC address. For layer 3 traces, value must be an IP address.</p></td>
</tr>
<tr class="even">
<td><p>VRF</p></td>
<td><p>Optional for layer 3 traces. Virtual Route Forwarding interface to be used as part of the trace path.</p></td>
</tr>
<tr class="odd">
<td><p>VLAN ID</p></td>
<td><p>Required for layer 2 traces. Virtual LAN to be used as part of the trace path.</p></td>
</tr>
<tr class="even">
<td><p>Schedule</p></td>
<td><p>Sets the frequency with which to run a new trace (<strong>Run every</strong>) and when to start the trace for the first time (<strong>Starting</strong>).</p></td>
</tr>
<tr class="odd">
<td><p>Run Now</p></td>
<td><p>Start the trace now</p></td>
</tr>
<tr class="even">
<td><p>Update</p></td>
<td><p><strong>Update</strong> is available when a scheduled trace request is selected from the dropdown list and you make a change to its configuration. Clicking <strong>Update</strong> saves the changes to the <em>existing</em> scheduled trace.</p></td>
</tr>
<tr class="odd">
<td><p>Save As New</p></td>
<td><p><strong>Save As New</strong> is available in two instances:</p>
<ul>
<li><p>When you enter a source, destination, and schedule for a new trace. Clicking <strong>Save As New</strong> in this instance saves the new scheduled trace.</p></li>
<li><p>When changes are made to a selected scheduled trace request. Clicking <strong>Save As New</strong> in this instance saves the modified scheduled trace <em>without</em> changing the original trace on which it was based.</p></li>
</ul></td>
</tr>
</tbody>
</table>

The full screen Trace Request card displays:

{{< figure src="/images/netq/trace-request-fullscr-preview-tab-222.png" width="700" >}}

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 85%" />
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
<td><p>Trace Request</p></td>
</tr>
<tr class="even">
<td><p><img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/close.svg", height="14", width="14"/></p></td>
<td><p>Closes full screen card and returns to workbench</p></td>
</tr>
<tr class="odd">
<td><p>Time period</p></td>
<td><p>Range of time in which the displayed data was collected; applies to all card sizes; select an alternate time period by clicking <img src="https://icons.cumulusnetworks.com/52-Arrows-Diagrams/01-Arrows/arrow-button-down-2.svg", height="14", width="14"/></td>
</tr>
<tr class="even">
<td><p>Results</p></td>
<td><p>Number of results found for the selected tab</p></td>
</tr>
<tr class="odd">
<td><p>Schedule Preview tab</p></td>
<td><p>Displays all scheduled trace requests for the given user. By default, the listing is sorted by <strong>Start Time</strong>, with the most recently started traces listed at the top. The tab provides the following additional data about each event:</p>
<ul>
<li><p><strong>Action</strong>: Indicates latest action taken on the trace job. Values include Add, Deleted, Update.</p></li>
<li><p><strong>Frequency</strong>: How often the trace is scheduled to run</p></li>
<li><p><strong>Active</strong>: Indicates if trace is actively running (true), or stopped from running (false)</p></li>
<li><p><strong>ID</strong>: Internal system identifier for the trace job</p></li>
<li><p><strong>Trace Name</strong>: User-defined name for a trace</p></li>
<li><p><strong>Trace Params</strong>: Indicates source and destination, optional VLAN or VRF specified, and whether to alert on failure</p></li>
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

### Create a Layer 3 On-demand Trace Request

It is helpful to verify the connectivity between two devices when you
suspect an issue is preventing proper communication between them. It you
cannot find a path through a layer 3 path, you might also try checking
connectivity through a layer 2 path.

To create a layer 3 trace request:

1.  Open the medium Trace Request card.

    {{<figure src="/images/netq/trace-request-medium-222.png" width="200">}}

2.  In the **Source** field, enter the hostname or IP address of the
    device where you want to start the trace.
3.  In the **Destination** field, enter the IP address of the device
    where you want to end the trace.  

    {{<figure src="/images/netq/trace-request-medium-l3-example-222.png" width="200">}}

    In this example, we are starting our trace at *server02* and ending
    it at *10.1.3.103*.

    {{%notice tip%}}

 If you mistype an address, you must double-click it, or backspace
 over the error, and retype the address. You cannot select the
 address by dragging over it as this action attempts to move the card
 to another location.

    {{%/notice%}}

4.  Click **Run Now**. A corresponding Trace Results card is opened on
    your workbench. Refer to [View Layer 3 Trace Results](#view-layer-3-trace-results) for
    details.

### Create a Layer 3 Trace Through a Given VRF

If you want to guide a trace through a particular VRF interface, you can
do so using the large New Trace Request card.

To create the trace request:

1.  Open the large Trace Request card.
2.  In the **Source** field, enter the hostname or IP address of the
    device where you want to start the trace.
3.  In the **Destination** field, enter the IP address of the device
    where you want to end the trace.
4.  In the **VRF** field, enter the identifier for the VRF interface you
    want to use.

    {{< figure src="/images/netq/trace-request-large-l3wVRF-example-222.png" width="500" >}}

    In this example, we are starting our trace at *leaf01* and ending it
    at *10.1.3.103* using VRF *vrf1.*

5.  Click **Run Now**. A corresponding Trace Results card is opened on
    your workbench. Refer to [View Layer 3 Trace Results](#view-layer-3-trace-results) for
    details.

### Create a Layer 2 Trace

It is helpful to verify the connectivity between two devices when you
suspect an issue is preventing proper communication between them. It you
cannot find a path through a layer 2 path, you might also try checking
connectivity through a layer 3 path.

To create a layer 2 trace request:

1.  Open the large Trace Request card.

2.  In the **Source** field, enter the hostname or IP address of the
    device where you want to start the trace.
3.  In the **Destination** field, enter the MAC address for where you
    want to end the trace.
4.  In the **VLAN ID** field, enter the identifier for the VLAN you want
    to use.

    {{< figure src="/images/netq/trace-request-large-l2vlan-example-222.png" width="500" >}}

    In this example, we are starting our trace at *leaf01* and ending it
    at *00:03:00:33:33:01* using VLAN *13.*

5.  Click **Run Now**. A corresponding Trace Results card is opened on
    your workbench. Refer to [View Layer 2 Trace Results](#view-layer-2-trace-results) for
    details.

### Create a Trace to Run on a Regular Basis (Scheduled Trace)

There may be paths through your network that you consider critical to
your everyday or particularly important operations. In that case, it
might be useful to create one or more traces to periodically confirm
that at least one path is available between the relevant two devices.
Scheduling a trace request can be performed from the large Trace Request
card.

To schedule a trace:

1.  Open the large Trace Request card.
2.  In the **Source** field, enter the hostname or IP address of the
    device where you want to start the trace.
3.  In the **Destination** field, enter the MAC address (layer 2) or IP
    address (layer 3) of the device where you want to end the trace.
4.  Optionally, enter a VLAN ID (layer 2) or VRF interface (layer 3).

    {{< figure src="/images/netq/trace-request-large-l2vlan-ex.png" width="500" >}}

5.  Select a timeframe under **Schedule** to specify how often you want
    to run the trace.

    {{< figure src="/images/netq/schedule-frequency-selection-222.png" width="300" >}}

6.  Accept the default starting time, or click in the **Starting** field to specify the day you want the trace to run for the first time.

    {{< figure src="/images/netq/date-selection-222.png" width="200" >}}

7.  Click **Next**.
8.  Click the time you want the trace to run for the first time.

    {{< figure src="/images/netq/time-selection-222.png" width="200" >}}

9.  Click **OK**.
10. Verify your entries are correct, then click **Save As New**.
11. Provide a name for the trace. **Note**: This name must be unique
    for a given user.

    {{< figure src="/images/netq/save-trace-name-modal.png" width="250" >}}

12. Click **Save**. You can now run this trace on demand by selecting it
    from the dropdown list, or wait for it to run on its defined
    schedule.

### Run a Scheduled Trace on Demand

You may find that, although you have a schedule for a particular trace,
you want to have visibility into the connectivity data now. You can run
a scheduled trace on demand from the small, medium and large Trace
Request cards.

To run a scheduled trace now:

1.  Open the small or medium or large Trace Request card.  

    {{< figure src="/images/netq/trace-request-small-selection-230.png" width="200" >}}

    {{< figure src="/images/netq/trace-request-medium-selection-230.png" width="200" >}}

    {{< figure src="/images/netq/trace-request-large-selection-222.png" width="500" >}}

2.  Select the scheduled trace from the **Select Trace** or **New Trace
    Request** list. **Note**: In the medium and large cards, the trace
    details are filled in on selection of the scheduled trace.
3.  Click **Go** or **Run Now**. A corresponding Trace Results card is
    opened on your workbench.

## View On-demand Trace Results

Once you have started an on-demand trace,
the results are displayed in the medium Trace Results card by default.
You may view the results in more or less detail by switching to the
large or small Trace Results card, respectively.

### On-demand Trace Results Card Workflow Summary

The small On-demand Trace Results card
displays:

{{< figure src="/images/netq/od-trace-result-small-230.png" width="200" >}}

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 85%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Item</p></th>
<th><p>Description</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><img src="https://icons.cumulusnetworks.com/06-Business-Products/13-Data-Files/data-file-bars-search.svg", height="18", width="18"/></p></td>
<td><p>Indicates an on-demand trace result</p></td>
</tr>
<tr class="even">
<td><p> </p></td>
<td><p>Source and destination of the trace, identified by their address or hostname. Source is listed on top with arrow pointing to destination.</p></td>
</tr>
<tr class="odd">
<td><p><img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/check-circle-1.svg", height="18", width="18"/>, <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/23-Delete/delete-2.svg", height="18", width="18"/></p></td>
<td><p>Indicates success or failure of the trace request. A successful result implies all paths were successful without any warnings or failures. A failure result implies there was at least one path with warnings or errors.</p></td>
</tr>
</tbody>
</table>

The medium On-demand Trace Results card displays:

{{< figure src="/images/netq/od-trace-result-medium-230.png" width="200" >}}

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 85%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Item</p></th>
<th><p>Description</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><img src="https://icons.cumulusnetworks.com/06-Business-Products/13-Data-Files/data-file-bars-search.svg", height="18", width="18"/></p></td>
<td><p>Indicates an on-demand trace result</p></td>
</tr>
<tr class="even">
<td><p>Title</p></td>
<td><p>On-demand Trace Result</p></td>
</tr>
<tr class="odd">
<td><p> </p></td>
<td><p>Source and destination of the trace, identified by their address or hostname. Source is listed on top with arrow pointing to destination.</p></td>
</tr>
<tr class="even">
<td><p><img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/check-circle-1.svg", height="18", width="18"/>, <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/23-Delete/delete-2.svg", height="18", width="18"/></p></td>
<td><p>Indicates success or failure of the trace request. A successful result implies all paths were successful without any warnings or failures. A failure result implies there was at least one path with warnings or errors.</p></td>
</tr>
<tr class="odd">
<td><p>Total Paths Found</p></td>
<td><p>Number of paths found between the two devices</p></td>
</tr>
<tr class="even">
<td><p>MTU Overall</p></td>
<td><p>Average size of the maximum transmission unit for all paths</p></td>
</tr>
<tr class="odd">
<td><p>Minimum Hops</p></td>
<td><p>Smallest number of hops along a path between the devices</p></td>
</tr>
<tr class="even">
<td><p>Maximum Hops</p></td>
<td><p>Largest number of hops along a path between the devices</p></td>
</tr>
</tbody>
</table>

The large On-demand Trace Results card contains two tabs.

The *On-demand Trace Result* tab displays:

{{< figure src="/images/netq/od-trace-result-large-summary-tab-230.png" width="500" >}}

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 85%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Item</p></th>
<th><p>Description</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><img src="https://icons.cumulusnetworks.com/06-Business-Products/13-Data-Files/data-file-bars-search.svg", height="18", width="18"/></p></td>
<td><p>Indicates an on-demand trace result</p></td>
</tr>
<tr class="even">
<td><p>Title</p></td>
<td><p>On-demand Trace Result</p></td>
</tr>
<tr class="odd">
<td><p><img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/check-circle-1.svg", height="18", width="18"/>, <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/23-Delete/delete-2.svg", height="18", width="18"/></p></td>
<td><p>Indicates success or failure of the trace request. A successful result implies all paths were successful without any warnings or failures. A failure result implies there was at least one path with warnings or errors.</p></td>
</tr>
<tr class="even">
<td><p> </p></td>
<td><p>Source and destination of the trace, identified by their address or hostname. Source is listed on top with arrow pointing to destination.</p></td>
</tr>
<tr class="odd">
<td><p>Distribution by Hops chart</p></td>
<td><p>Displays the distributions of various hop counts for the available paths</p></td>
</tr>
<tr class="even">
<td><p>Distribution by MTU chart</p></td>
<td><p>Displays the distribution of MTUs used on the interfaces used in the available paths</p></td>
</tr>
<tr class="odd">
<td><p>Table</p></td>
<td><p>Provides detailed path information, sorted by the route identifier, including:</p>
<ul>
<li><p><strong>Route ID</strong>: Identifier of each path</p></li>
<li><p><strong>MTU</strong>: Average speed of the interfaces used</p></li>
<li><p><strong>Hops</strong>: Number of hops to get from the source to the destination device</p></li>
<li><p><strong>Warnings</strong>: Number of warnings encountered during the trace on a given path</p></li>
<li><p><strong>Errors</strong>: Number of errors encountered during the trace on a given path</p></li>
</ul></td>
</tr>
<tr class="even">
<td><p>Total Paths Found</p></td>
<td><p>Number of paths found between the two devices</p></td>
</tr>
<tr class="odd">
<td><p>MTU Overall</p></td>
<td><p>Average size of the maximum transmission unit for all paths</p></td>
</tr>
<tr class="even">
<td><p>Minimum Hops</p></td>
<td><p>Smallest number of hops along a path between the devices</p></td>
</tr>
</tbody>
</table>

The *On-demand Trace Settings* tab displays:

{{< figure src="/images/netq/od-trace-result-large-config-tab-230.png" width="500" >}}

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 85%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Item</p></th>
<th><p>Description</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><img src="https://icons.cumulusnetworks.com/01-Interface-Essential/12-Settings/cog-1.svg", height="18", width="18"/></p></td>
<td><p>Indicates an on-demand trace setting</p></td>
</tr>
<tr class="even">
<td><p>Title</p></td>
<td><p>On-demand Trace Settings</p></td>
</tr>
<tr class="odd">
<td><p>Source</p></td>
<td><p>Starting point for the trace</p></td>
</tr>
<tr class="even">
<td><p>Destination</p></td>
<td><p>Ending point for the trace</p></td>
</tr>
<tr class="odd">
<td><p>Schedule</p></td>
<td><p>Does not apply to on-demand traces</p></td>
</tr>
<tr class="even">
<td><p>VRF</p></td>
<td><p>Associated virtual route forwarding interface, when used with layer 3 traces</p></td>
</tr>
<tr class="odd">
<td><p>VLAN</p></td>
<td><p>Associated virtual local area network, when used with layer 2 traces</p></td>
</tr>
<tr class="even">
<td><p>Job ID</p></td>
<td><p>Identifier of the job; used internally</p></td>
</tr>
<tr class="odd">
<td><p>Re-run Trace</p></td>
<td><p>Clicking this button runs the trace again</p></td>
</tr>
</tbody>
</table>

The full screen On-demand Trace Results card displays:

{{< figure src="/images/netq/od-trace-result-fullscr-230.png" width="700" >}}

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 85%" />
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
<td><p>On-demand Trace Results</p></td>
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
<tr class="even">
<td><p>Trace Results tab</p></td>
<td><p>Provides detailed path information, sorted by the <strong>Resolution Time</strong> (date and time results completed), including:</p>
<ul>
<li><p><strong>SCR.IP</strong>: Source IP address</p></li>
<li><p><strong>DST.IP</strong>: Destination IP address</p></li>
<li><p><strong>Max Hop Count</strong>: Largest number of hops along a path between the devices</p></li>
<li><p><strong>Min Hop Count</strong>: Smallest number of hops along a path between the devices</p></li>
<li><p><strong>Total Paths</strong>: Number of paths found between the two devices</p></li>
<li><p><strong>PMTU</strong>: Average size of the maximum transmission unit for all interfaces along the paths</p></li>
<li><p><strong>Errors</strong>: Message provided for analysis when a trace fails</p></li>
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

### View Layer 2 Trace Results

When you start the trace, the corresponding results card is opened on
your workbench. While it is working on the trace, a notice is shown on
the card indicating it is running.

{{< figure src="/images/netq/od-trace-result-medium-running-230.png" width="200" >}}

Once the job is completed, the results are displayed.

{{< figure src="/images/netq/od-trace-result-medium-good-230.png" width="200" >}}

{{< figure src="/images/netq/od-trace-result-medium-fail-230.png" width="200" >}}

In this example, we see that the trace was successful. Four paths were
found between the devices, each with four hops and with an overall MTU
of 1500. If there was a difference between the minimum and maximum
number of hops or other failures, viewing the results on the large card
would provide additional information.

{{< figure src="/images/netq/od-trace-result-large-summary-tab-230.png" width="500" >}}

{{< figure src="/images/netq/od-trace-result-large-summary-tab-fail-230.png" width="500" >}}

In our example, we can verify that every path option had four hops since
the distribution chart only shows one hop count and the table indicates
each path had a value of four hops. Similarly, you can view the MTU
data. If there had been any warnings, the count would have been visible
in the table.

### View Layer 3 Trace Results

When you start the trace, the corresponding results card is opened on
your workbench. While it is working on the trace, a notice is shown on
the card indicating it is running.

{{< figure src="/images/netq/od-trace-result-medium-l3-running-230.png" width="200" >}}

Once results are obtained, it displays them. Using our example from
earlier, the following results are shown:

{{< figure src="/images/netq/od-trace-result-medium-230.png" width="200" >}}

In this example, we see that the trace was successful. Six paths were
found between the devices, each with five hops and with an overall MTU
of 1500. If there was a difference between the minimum and maximum
number of hops or other failures, viewing the results on the large card
would provide additional information.

{{< figure src="/images/netq/od-trace-result-large-summary-tab-230.png" width="500" >}}

In our example, we can verify that every path option had five hops since
the distribution chart only shows one hop count and the table indicates
each path had a value of five hops. Similarly, you can view the MTU
data. If there had been any warnings, the count would have been visible
in the table.

## View Scheduled Trace Results

You can view the results of scheduled traces at any time. Results are
displayed on the Scheduled Trace Results cards.

### Scheduled Trace Results Card Workflow Summary

The small Scheduled Trace Results card displays:

{{< figure src="/images/netq/sch-trace-result-small.png" width="200" >}}

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 85%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Item</p></th>
<th><p>Description</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><img src="https://icons.cumulusnetworks.com/03-Computers-Devices-Electronics/01-Smart-Watches/smart-watch-square-graph.svg", height="18", width="18"/></p></td>
<td><p>Indicates a scheduled trace result</p></td>
</tr>
<tr class="even">
<td><p> </p></td>
<td><p>Source and destination of the trace, identified by their address or hostname. Source is listed on left with arrow pointing to destination.</p></td>
</tr>
<tr class="odd">
<td><p>Results</p></td>
<td><p>Summary of trace results: a successful result implies all paths were successful without any warnings or failures; a failure result implies there was at least one path with warnings or errors.</p>
<ul>
<li><p><img src="https://icons.cumulusnetworks.com/01-Interface-Essential/21-Date-Calendar/calendar-refresh.svg", height="18", width="18"/> Number of trace runs completed in the designated time period</p></li>
<li><p><img src="https://icons.cumulusnetworks.com/01-Interface-Essential/14-Alerts/alert-triangle.svg", height="18", width="18"/> Number of runs with warnings</p></li>
<li><p><img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/remove-shield.svg", height="18", width="18"/> Number of runs with errors</p></li>
</ul></td>
</tr>
</tbody>
</table>

The medium Scheduled Trace Results card displays:

{{< figure src="/images/netq/sch-trace-result-medium.png" width="200" >}}

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 85%" />
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
<td><p><img src="https://icons.cumulusnetworks.com/03-Computers-Devices-Electronics/01-Smart-Watches/smart-watch-square-graph.svg", height="18", width="18"/></p></td>
<td><p>Indicates a scheduled trace result</p></td>
</tr>
<tr class="odd">
<td><p>Title</p></td>
<td><p>Scheduled Trace Result</p></td>
</tr>
<tr class="even">
<td><p>Summary</p></td>
<td><p>Name of scheduled validation and summary of trace results: a successful result implies all paths were successful without any warnings or failures; a failure result implies there was at least one path with warnings or errors.</p>
<ul>
<li><p><img src="https://icons.cumulusnetworks.com/01-Interface-Essential/21-Date-Calendar/calendar-refresh.svg", height="18", width="18"/> Number of trace runs completed in the designated time period</p></li>
<li><p><img src="https://icons.cumulusnetworks.com/01-Interface-Essential/14-Alerts/alert-triangle.svg", height="18", width="18"/> Number of runs with warnings</p></li>
<li><p><img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/remove-shield.svg", height="18", width="18"/> Number of runs with errors</p></li>
</ul></td>
</tr>
<tr class="odd">
<td><p>Charts</p></td>
<td><p><strong>Heat map:</strong> A time segmented view of the results. For each time segment, the color represents the percentage of warning and failed results. Refer to <a href="#granularity-of-data-shown-based-on-time-period">Granularity of Data Shown Based on Time Period</a> for details on how to interpret the results.</p>
<p><strong>Unique Bad Nodes</strong>: Distribution of unique nodes that generated the indicated warnings and/or failures</p></td>
</tr>
</tbody>
</table>

The large Scheduled Trace Results card contains two tabs:

The *Results* tab displays:

{{< figure src="/images/netq/sch-trace-result-large-sum-tab.png" width="500" >}}

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 85%" />
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
<td><p><img src="https://icons.cumulusnetworks.com/03-Computers-Devices-Electronics/01-Smart-Watches/smart-watch-square-graph.svg", height="18", width="18"/></p></td>
<td><p>Indicates a scheduled trace result</p></td>
</tr>
<tr class="odd">
<td><p>Title</p></td>
<td><p>Scheduled Trace Result</p></td>
</tr>
<tr class="even">
<td><p>Summary</p></td>
<td><p>Name of scheduled validation and summary of trace results: a successful result implies all paths were successful without any warnings or failures; a failure result implies there was at least one path with warnings or errors.</p>
<ul>
<li><p><img src="https://icons.cumulusnetworks.com/01-Interface-Essential/21-Date-Calendar/calendar-refresh.svg", height="18", width="18"/> Number of trace runs completed in the designated time period</p></li>
<li><p><img src="https://icons.cumulusnetworks.com/01-Interface-Essential/14-Alerts/alert-triangle.svg", height="18", width="18"/> Number of runs with warnings</p></li>
<li><p><img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/remove-shield.svg", height="18", width="18"/> Number of runs with errors</p></li>
</ul></td>
</tr>
<tr class="odd">
<td><p>Charts</p></td>
<td><p><strong>Heat map:</strong> A time segmented view of the results. For each time segment, the color represents the percentage of warning and failed results. Refer to <a href="#granularity-of-data-shown-based-on-time-period">Granularity of Data Shown Based on Time Period</a> for details on how to interpret the results.</p>
<p><strong>Small charts</strong>: Display counts for each item during the same time period, for the purpose of correlating with the warnings and errors shown in the heat map.</p></td>
</tr>
<tr class="even">
<td><p>Table/Filter options</p></td>
<td><p>When the <strong>Failures</strong> filter option is selected, the table displays the failure messages received for each run.</p>
<p>When the <strong>Paths</strong> filter option is selected, the table displays all of the paths tried during each run.</p>
<p>When the <strong>Warning</strong> filter option is selected, the table displays the warning messages received for each run.</p></td>
</tr>
</tbody>
</table>

The *Configuration* tab displays:

{{< figure src="/images/netq/sch-trace-result-large-config-tab.png" width="500" >}}

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 85%" />
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
<td><p><img src="https://icons.cumulusnetworks.com/01-Interface-Essential/12-Settings/cog-1.svg", height="18", width="18"/></p></td>
<td><p>Indicates a scheduled trace configuration</p></td>
</tr>
<tr class="odd">
<td><p>Title</p></td>
<td><p>Scheduled Trace Configuration (Scheduled Trace Result)</p></td>
</tr>
<tr class="even">
<td><p>Source</p></td>
<td><p>Address or hostname of the device where the trace was started</p></td>
</tr>
<tr class="odd">
<td><p>Destination</p></td>
<td><p>Address of the device where the trace was stopped</p></td>
</tr>
<tr class="even">
<td><p>Schedule</p></td>
<td><p>The frequency and starting date and time to run the trace</p></td>
</tr>
<tr class="odd">
<td><p>VRF</p></td>
<td><p>Virtual Route Forwarding interface, when defined</p></td>
</tr>
<tr class="even">
<td><p>VLAN</p></td>
<td><p>Virtual LAN identifier, when defined</p></td>
</tr>
<tr class="odd">
<td><p>Name</p></td>
<td><p>User-defined name of the scheduled trace</p></td>
</tr>
<tr class="even">
<td><p>Run Now</p></td>
<td><p>Start the trace now</p></td>
</tr>
<tr class="odd">
<td><p>Edit</p></td>
<td><p>Modify the trace. Opens Trace Request card with this information pre-populated.</p></td>
</tr>
</tbody>
</table>

The full screen Scheduled Trace Results card displays:

{{< figure src="/images/netq/sch-trace-result-fullscr-230.png" width="700" >}}

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 85%" />
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
<td><p>Scheduled Trace Results</p></td>
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
<td><p>Scheduled Trace Results tab</p></td>
<td><p>Displays the basic information about the trace, including:</p>
<ul>
<li><p><strong>Resolution Time</strong>: Time that trace was run</p></li>
<li><p><strong>SRC.IP</strong>: IP address of the source device</p></li>
<li><p><strong>DST.IP</strong>: Address of the destination device</p></li>
<li><p><strong>Max Hop Count</strong>: Maximum number of hops across all paths between the devices</p></li>
<li><p><strong>Min Hop Count</strong>: Minimum number of hops across all paths between the devices</p></li>
<li><p><strong>Total Paths</strong>: Number of available paths found between the devices</p></li>
<li><p><strong>PMTU</strong>: Average of the maximum transmission units for all paths</p></li>
<li><p><strong>Errors</strong>: Message provided for analysis if trace fails</p></li>
</ul>
<p>Click on a result to open a detailed view of the results.</p></td>
</tr>
<tr class="even">
<td><p>Export</p></td>
<td><p>Enables export of all or selected items in a CSV or JSON formatted file</p></td>
</tr>
<tr class="odd">
<td><img src="https://icons.cumulusnetworks.com/01-Interface-Essential/12-Settings/cog-1.svg", height="18", width="18"/></p></td>
<td><p>Enables manipulation of table display; choose columns to display and reorder columns</p></td>
</tr>
</tbody>
</table>

### Granularity of Data Shown Based on Time Period

On the medium and large Trace Result cards, the status of the runs is
represented in heat maps stacked vertically; one for runs with warnings
and one for runs with failures. Depending on the time period of data on
the card, the number of smaller time blocks used to indicate the status
varies. A vertical stack of time blocks, one from each map, includes the
results from all checks during that time. The results are shown by how
saturated the color is for each block. If all traces run during that
time period pass, then both blocks are 100% gray. If there are only
failures, the associated lower blocks are 100% saturated white and the
warning blocks are 100% saturated gray. As warnings and failures
increase, the blocks increase their white saturation. As warnings or
failures decrease, the blocks increase their gray saturation. An example
heat map for a time period of 24 hours is shown here with the most
common time periods in the table showing the resulting time blocks.

{{< figure src="/images/netq/sch-trace-result-granularity-230.png" width="300" >}}

| Time Period | Number of Runs | Number Time Blocks | Amount of Time in Each Block |
| ----------- | -------------- | ------------------ | ---------------------------- |
| 6 hours     | 18             | 6                  | 1 hour                       |
| 12 hours    | 36             | 12                 | 1 hour                       |
| 24 hours    | 72             | 24                 | 1 hour                       |
| 1 week      | 504            | 7                  | 1 day                        |
| 1 month     | 2,086          | 30                 | 1 day                        |
| 1 quarter   | 7,000          | 13                 | 1 week                       |

### View Detailed Scheduled Trace Results

Once a scheduled trace request has completed, the results are available
in the corresponding Trace Result card.

To view the results:

1.  Open the full screen Trace Request card to view all scheduled traces
    that have been run.

    {{< figure src="/images/netq/sch-trace-result-fullscr-230.png" width="700" >}}

2.  Select the scheduled trace you want to view results for by clicking
    in the first column of the result and clicking the check box.

3.  On the Edit Menu that appears at the bottom of the window, click <img src="https://icons.cumulusnetworks.com/44-Entertainment-Event-Hobbies/02-Card-Games/card-game-diamond.svg", height="18", width="18"/> (Open Cards). This opens the medium Scheduled Trace Results card(s) for the selected items.

    {{< figure src="/images/netq/sch-trace-result-medium.png" width="200" >}}

4.  Note the distribution of results. Are there many failures? Are they
    concentrated together in time? Has the trace begun passing again?

5.  Hover over the heat maps to view the status numbers and what
    percentage of the total results that represents for a given region.

6.  Switch to the large Scheduled Trace Result card.

    {{< figure src="/images/netq/sch-trace-result-large-sum-tab.png" width="500" >}}

7.  If there are a large number of warnings or failures, view the
    associated messages by selecting **Failures** or **Warning** in the
    filter above the table. This might help narrow the failures down to
    a particular device or small set of devices that you can investigate
    further.
8.  Look for a consistent number of paths, MTU, hops in the small charts
    under the heat map. Changes over time here might correlate with the
    messages and give you a clue to any specific issues. Note if the
    number of bad nodes changes over time. Devices that become
    unreachable are often the cause of trace failures.
9.  View the available paths for each run, by selecting **Paths** in the
    filter above the table.
10. You can view the configuration of the request that produced the
    results shown on this card workflow, by hovering over the card and
    clicking <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/12-Settings/cog-1.svg", height="18", width="18"/>. If you want to change the configuration, click **Edit** to open
    the large Trace Request card, pre-populated with the current
    configuration. Follow the instructions in [Create a Scheduled Trace Request](#create-a-trace-to-run-on-a-regular-basis-scheduled-trace) to
    make your changes in the same way you created a new scheduled trace.

11. To view a summary of all scheduled trace results, switch to the full
    screen card.
12. Look for changes and patterns in the results for additional clues to
    isolate root causes of trace failures. Select and view related
    traces using the Edit menu.
13. View the details of any specific trace result by clicking on the
    trace. A new window opens similar to the following:

    {{< figure src="/images/netq/sch-trace-result-fullscr-trace-detail-230.png" width="700" >}}

    Scroll to the right to view the information for a given hop. Scroll
    down to view additional paths.  
    This display shows each of the hosts and detailed steps the trace
    takes to validate a given path between two devices. Using Path 1 as
    an example, each path can be interpreted as follows:  
    Hop 1 is from the source device, server02 in this case. It exits this
    device at switch port bond0 with an MTU of 9000 and over the default VRF
    too get to leaf02. The trace goes in to swp2 with an MTU of 9216
    over the vrf1 interface. It exits leaf02 through switch port 52
    and so on.

14. Export this data using the **Export** button or click <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/close.svg", height="14", width="14"/> to return to the results list to view another trace in detail.
