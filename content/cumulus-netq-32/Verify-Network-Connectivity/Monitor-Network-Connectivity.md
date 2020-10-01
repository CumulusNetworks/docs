---
title: Verify Network Connectivity
author: Cumulus Networks
weight: 0
toc: 4
---
It is helpful to verify that communications are freely flowing between the various devices in your network. You can verify the connectivity between two devices in both an adhoc fashion and by defining connectivity checks to occur on a scheduled basis. There are three card workflows which enable you to view connectivity, the Trace Request, On-demand Trace Results, and Scheduled Trace Results.

## Create a Trace Request

Two types of connectivity checks can be run-an immediate (on-demand) trace and a scheduled trace. The Trace Request card workflow is used to configure and run both of these trace types.

### Create a Layer 3 On-demand Trace Request

It is helpful to verify the connectivity between two devices when you suspect an issue is preventing proper communication between them. It you cannot find a path through a layer 3 path, you might also try checking connectivity through a layer 2 path.

To create a layer 3 trace request:

1. Open the medium Trace Request card.

    {{<figure src="/images/netq/trace-request-medium-222.png" width="200">}}

2. In the **Source** field, enter the hostname or IP address of the device where you want to start the trace.

3. In the **Destination** field, enter the IP address of the device where you want to end the trace.  

    {{<figure src="/images/netq/trace-request-medium-l3-example-222.png" width="200">}}

    In this example, we are starting our trace at *server02* and ending it at *10.1.3.103*.

    {{%notice tip%}}
 If you mistype an address, you must double-click it, or backspace over the error, and retype the address. You cannot select the address by dragging over it as this action attempts to move the card to another location.
    {{%/notice%}}

4. Click **Run Now**. A corresponding Trace Results card is opened on your workbench. Refer to {{<link title="#View Layer 3 Trace Results" text="View Layer 3 Trace Results">}} for details.

### Create a Layer 3 Trace Through a Given VRF

If you want to guide a trace through a particular VRF interface, you can do so using the large New Trace Request card.

To create the trace request:

1. Open the large Trace Request card.

2. In the **Source** field, enter the hostname or IP address of the device where you want to start the trace.

3. In the **Destination** field, enter the IP address of the device where you want to end the trace.

4. In the **VRF** field, enter the identifier for the VRF interface you want to use.

    {{< figure src="/images/netq/trace-request-large-l3wVRF-example-222.png" width="500" >}}

    In this example, we are starting our trace at *leaf01* and ending it at *10.1.3.103* using VRF *vrf1.*

5. Click **Run Now**. A corresponding Trace Results card is opened on your workbench. Refer to {{<link title="#View Layer 3 Trace Results" text="View Layer 3 Trace Results">}} for details.

### Create a Layer 2 Trace

It is helpful to verify the connectivity between two devices when you suspect an issue is preventing proper communication between them. It you cannot find a path through a layer 2 path, you might also try checking connectivity through a layer 3 path.

To create a layer 2 trace request:

1. Open the large Trace Request card.

2. In the **Source** field, enter the hostname or IP address of the device where you want to start the trace.

3. In the **Destination** field, enter the MAC address for where you want to end the trace.

4. In the **VLAN ID** field, enter the identifier for the VLAN you want to use.

    {{< figure src="/images/netq/trace-request-large-l2vlan-example-222.png" width="500" >}}

    In this example, we are starting our trace at *leaf01* and ending it at *00:03:00:33:33:01* using VLAN *13.*

5. Click **Run Now**. A corresponding Trace Results card is opened on your workbench. Refer to {{<link title="#View Layer 2 Trace Results" text="View Layer 2 Trace Results">}} for details.

### Create a Trace to Run on a Regular Basis (Scheduled Trace)

There may be paths through your network that you consider critical to your everyday or particularly important operations. In that case, it might be useful to create one or more traces to periodically confirm that at least one path is available between the relevant two devices. Scheduling a trace request can be performed from the large Trace Request card.

To schedule a trace:

1. Open the large Trace Request card.

2. In the **Source** field, enter the hostname or IP address of the device where you want to start the trace.

3. In the **Destination** field, enter the MAC address (layer 2) or IP address (layer 3) of the device where you want to end the trace.

4. Optionally, enter a VLAN ID (layer 2) or VRF interface (layer 3).

    {{< figure src="/images/netq/trace-request-large-l2vlan-ex.png" width="500" >}}

5. Select a timeframe under **Schedule** to specify how often you want to run the trace.

    {{< figure src="/images/netq/schedule-frequency-selection-222.png" width="300" >}}

6. Accept the default starting time, or click in the **Starting** field to specify the day you want the trace to run for the first time.

    {{< figure src="/images/netq/date-selection-222.png" width="200" >}}

7. Click **Next**.

8. Click the time you want the trace to run for the first time.

    {{< figure src="/images/netq/time-selection-222.png" width="200" >}}

9. Click **OK**.

10. Verify your entries are correct, then click **Save As New**.

11. Provide a name for the trace. **Note**: This name must be unique for a given user.

    {{< figure src="/images/netq/save-trace-name-modal.png" width="250" >}}

12. Click **Save**. You can now run this trace on demand by selecting it from the dropdown list, or wait for it to run on its defined schedule.

### Run a Scheduled Trace on Demand

You may find that, although you have a schedule for a particular trace, you want to have visibility into the connectivity data now. You can run a scheduled trace on demand from the small, medium and large Trace Request cards.

To run a scheduled trace now:

1. Open the small or medium or large Trace Request card.

    {{< figure src="/images/netq/trace-request-small-selection-230.png" width="200" >}}

    {{< figure src="/images/netq/trace-request-medium-selection-230.png" width="200" >}}

    {{< figure src="/images/netq/trace-request-large-selection-222.png" width="500" >}}

2. Select the scheduled trace from the **Select Trace** or **New Trace Request** list. **Note**: In the medium and large cards, the trace details are filled in on selection of the scheduled trace.

3. Click **Go** or **Run Now**. A corresponding Trace Results card is opened on your workbench.

## View On-demand Trace Results

Once you have started an on-demand trace, the results are displayed in the medium Trace Results card by default. You may view the results in more or less detail by switching to the large or small Trace Results card, respectively.

### View Layer 2 Trace Results

When you start the trace, the corresponding results card is opened on your workbench. While it is working on the trace, a notice is shown on the card indicating it is running.

{{< figure src="/images/netq/od-trace-result-medium-running-230.png" width="200" >}}

Once the job is completed, the results are displayed.

{{< figure src="/images/netq/od-trace-result-medium-good-230.png" width="200" >}}

{{< figure src="/images/netq/od-trace-result-medium-fail-230.png" width="200" >}}

In this example, we see that the trace was successful. Four paths were found between the devices, each with four hops and with an overall MTU of 1500. If there was a difference between the minimum and maximum number of hops or other failures, viewing the results on the large card would provide additional information.

{{< figure src="/images/netq/od-trace-result-large-summary-tab-230.png" width="500" >}}

{{< figure src="/images/netq/od-trace-result-large-summary-tab-fail-230.png" width="500" >}}

In our example, we can verify that every path option had four hops since the distribution chart only shows one hop count and the table indicates each path had a value of four hops. Similarly, you can view the MTU data. If there had been any warnings, the count would have been visible in the table.

### View Layer 3 Trace Results

When you start the trace, the corresponding results card is opened on your workbench. While it is working on the trace, a notice is shown on the card indicating it is running.

{{< figure src="/images/netq/od-trace-result-medium-l3-running-230.png" width="200" >}}

Once results are obtained, it displays them. Using our example from earlier, the following results are shown:

{{< figure src="/images/netq/od-trace-result-medium-230.png" width="200" >}}

In this example, we see that the trace was successful. Six paths were found between the devices, each with five hops and with an overall MTU of 1500. If there was a difference between the minimum and maximum number of hops or other failures, viewing the results on the large card would provide additional information.

{{< figure src="/images/netq/od-trace-result-large-summary-tab-230.png" width="500" >}}

In our example, we can verify that every path option had five hops since the distribution chart only shows one hop count and the table indicates each path had a value of five hops. Similarly, you can view the MTU data. If there had been any warnings, the count would have been visible in the table.

### View Detailed On-demand  Trace Results

After the trace request has completed, the results are available in the corresponding medium Trace Results card.

To view the more detail:

1. Open the full-screen Trace Results card for the trace of interest.

    {{< figure src="/images/netq/od-trace-result-fullscr-240.png" width="700" >}}

2. Double-click on the trace of interest to open the detail view.

    {{< figure src="/images/netq/od-trace-result-fullscr-details-wjh-240.png" width="700" >}}

    The tabular view enables you to walk through the trace path, host by host, viewing the interfaces, ports, tunnels, VLANs, and so forth used to traverse the network from the source to the destination.

3. If the trace was run on a Mellanox switch *and* drops were detected by the What Just Happened feature, they are identified above the path. Click the down arrow to view the list of drops and their details. Click the up arrow to close the list.

## View Scheduled Trace Results

You can view the results of scheduled traces at any time. Results are displayed on the Scheduled Trace Results cards.

### Granularity of Data Shown Based on Time Period

On the medium and large Trace Result cards, the status of the runs is represented in heat maps stacked vertically; one for runs with warnings and one for runs with failures. Depending on the time period of data on the card, the number of smaller time blocks used to indicate the status varies. A vertical stack of time blocks, one from each map, includes the results from all checks during that time. The results are shown by how saturated the color is for each block. If all traces run during that time period pass, then both blocks are 100% gray. If there are only failures, the associated lower blocks are 100% saturated white and the warning blocks are 100% saturated gray. As warnings and failures increase, the blocks increase their white saturation. As warnings or failures decrease, the blocks increase their gray saturation. An example heat map for a time period of 24 hours is shown here with the most common time periods in the table showing the resulting time blocks.

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

Once a scheduled trace request has completed, the results are available in the corresponding Trace Result card.

To view the results:

1. Open the full screen Trace Request card to view all scheduled traces that have been run.

    {{< figure src="/images/netq/sch-trace-result-fullscr-230.png" width="700" >}}

2. Select the scheduled trace you want to view results for by clicking in the first column of the result and clicking the check box.

3. On the Edit Menu that appears at the bottom of the window, click <img src="https://icons.cumulusnetworks.com/44-Entertainment-Events-Hobbies/02-Card-Games/card-game-diamond.svg" height="18" width="18"/> (Open Cards). This opens the medium Scheduled Trace Results card(s) for the selected items.

    {{< figure src="/images/netq/sch-trace-result-medium.png" width="200" >}}

4. Note the distribution of results. Are there many failures? Are they concentrated together in time? Has the trace begun passing again?

5. Hover over the heat maps to view the status numbers and what percentage of the total results that represents for a given region.

6. Switch to the large Scheduled Trace Result card.

    {{< figure src="/images/netq/sch-trace-result-large-sum-tab.png" width="500" >}}

7. If there are a large number of warnings or failures, view the associated messages by selecting **Failures** or **Warning** in the filter above the table. This might help narrow the failures down to a particular device or small set of devices that you can investigate further.

8. Look for a consistent number of paths, MTU, hops in the small charts under the heat map. Changes over time here might correlate with the     messages and give you a clue to any specific issues. Note if the number of bad nodes changes over time. Devices that become unreachable are often the cause of trace failures.

9. View the available paths for each run, by selecting **Paths** in the filter above the table.

10. You can view the configuration of the request that produced the results shown on this card workflow, by hovering over the card and clicking <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/12-Settings/cog-1.svg" height="18" width="18"/>. If you want to change the configuration, click **Edit** to open the large Trace Request card, pre-populated with the current configuration. Follow the instructions in {{<link url="#create-a-trace-to-run-on-a-regular-basis-scheduled-trace" text="Create a Scheduled Trace Request">}} to make your changes in the same way you created a new scheduled trace.

11. To view a summary of all scheduled trace results, switch to the full screen card.

12. Look for changes and patterns in the results for additional clues to isolate root causes of trace failures. Select and view related traces using the Edit menu.

13. View the details of any specific trace result by clicking on the trace. A new window opens similar to the following:

    {{< figure src="/images/netq/sch-trace-result-fullscr-trace-detail-230.png" width="700" >}}

    Scroll to the right to view the information for a given hop. Scroll down to view additional paths. This display shows each of the hosts and detailed steps the trace takes to validate a given path between two devices. Using Path 1 as an example, each path can be interpreted as follows:

    - Hop 1 is from the source device, server02 in this case.
    - It exits this device at switch port bond0 with an MTU of 9000 and over the default VRF to get to leaf02.
    - The trace goes in to swp2 with an MTU of 9216 over the vrf1 interface.
    - It exits leaf02 through switch port 52 and so on.

14. Export this data by clicking **Export** or click <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/close.svg" height="14" width="14"/> to return to the results list to view another trace in detail.
