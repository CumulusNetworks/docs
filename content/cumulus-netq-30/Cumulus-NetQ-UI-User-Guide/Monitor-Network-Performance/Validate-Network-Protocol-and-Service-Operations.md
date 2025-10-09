---
title: Validate Network Protocol and Service Operations
author: Cumulus Networks
weight: 350
toc: 4
---
With the NetQ UI, you can validate the operation of the network protocols and services running in your network either on demand or on a scheduled basis. There are three card workflows to perform this validation: one for creating the validation request (either on-demand or scheduled) and two validation results (one for on-demand and one for scheduled).

This release supports validation of the following network protocols and services: Agents, BGP, CLAG, EVPN, Interfaces, License, MTU, NTP, OSPF, Sensors, VLAN, and VXLAN.

For a more general understanding of how well your network is operating, refer to the {{<link title="Monitor Network Health">}} topic.

## Create Validation Requests

The Validation Request card workflow is used to create on-demand validation requests to evaluate the health of your network protocols and services.

### Validation Request Card Workflow

The small Validation Request card displays:

{{< figure src="/images/netq/valid-request-small-230.png" width="200" >}}
<p> </p>
<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 85%" />
</colgroup>
<thead>
<tr class="header">
<th>Item</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><img src="https://icons.cumulusnetworks.com/22-Social-Medias-Rewards-Rating/05-Love-it/love-it-check.svg" height="18" width="18"/></td>
<td>Indicates a validation request</td>
</tr>
<tr class="even">
<td>Validation</td>
<td><p>Select a scheduled request to run that request on-demand. A default validation is provided for each supported network protocol and service, which runs a network-wide validation check. These validations run every 60 minutes, but you may run them on-demand at any time.</p>
<p><strong>Note</strong>: No new requests can be configured from this size card.</p></td>
</tr>
<tr class="odd">
<td>GO</td>
<td>Start the validation request. The corresponding On-demand Validation Result cards are opened on your workbench, one per protocol and service.</td>
</tr>
</tbody>
</table>

The medium Validation Request card displays:

{{< figure src="/images/netq/valid-request-medium-230.png" width="200" >}}
<p> </p>
<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 85%" />
</colgroup>
<thead>
<tr class="header">
<th>Item</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><img src="https://icons.cumulusnetworks.com/22-Social-Medias-Rewards-Rating/05-Love-it/love-it-check.svg" height="18" width="18"/></td>
<td>Indicates a validation request</td>
</tr>
<tr class="even">
<td>Title</td>
<td>Validation Request</td>
</tr>
<tr class="odd">
<td>Validation</td>
<td><p>Select a scheduled request to run that request on-demand. A default validation is provided for each supported network protocol and service, which runs a network-wide validation check. These validations run every 60 minutes, but you may run them on-demand at any time.</p>
<p><strong>Note</strong>: No new requests can be configured from this size card.</p></td>
</tr>
<tr class="even">
<td>Protocols</td>
<td>The protocols included in a selected validation request are listed here.</td>
</tr>
<tr class="odd">
<td>Schedule</td>
<td>For a selected scheduled validation, the schedule and the time of the last run are displayed.</td>
</tr>
<tr class="even">
<td>Start the validation request</td>
<td>Run Now</td>
</tr>
</tbody>
</table>

The large Validation Request card displays:

{{< figure src="/images/netq/valid-request-large-222.png" width="500" >}}

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 85%" />
</colgroup>
<thead>
<tr class="header">
<th>Item</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><img src="https://icons.cumulusnetworks.com/22-Social-Medias-Rewards-Rating/05-Love-it/love-it-check.svg" height="18" width="18"/></td>
<td>Indicates a validation request</td>
</tr>
<tr class="even">
<td>Title</td>
<td>Validation Request</td>
</tr>
<tr class="odd">
<td>Validation</td>
<td>Depending on user intent, this field is used to:
<ul>
<li>Select a scheduled request to run that request on-demand. A default validation is provided for each supported network protocol and service, which runs a network-wide validation check. These validations run every 60 minutes, but you may run them on-demand at any time.</li>
<li>Leave as is to create a new scheduled validation request</li>
<li>Select a scheduled request to modify</li>
</ul></td>
</tr>
<tr class="even">
<td>Protocols</td>
<td>For a selected scheduled validation, the protocols included in a validation request are listed here. For new on-demand or scheduled validations, click these to include them in the validation.</td>
</tr>
<tr class="odd">
<td>Schedule:</td>
<td>For a selected scheduled validation, the schedule and the time of the last run are displayed. For new scheduled validations, select the frequency and starting date and time.
<ul>
<li><strong>Run Every</strong>: Select how often to run the request. Choose from 30 minutes, 1, 3, 6, or 12 hours, or 1 day.</li>
<li><strong>Starting</strong>: Select the date and time to start the first request in the series</li>
<li><strong>Last Run</strong>: Timestamp of when the selected validation was started</li>
</ul></td>
</tr>
<tr class="even">
<td>Scheduled Validations</td>
<td>Count of scheduled validations that are currently scheduled compared to the maximum of 15 allowed</td>
</tr>
<tr class="odd">
<td>Run Now</td>
<td>Start the validation request</td>
</tr>
<tr class="even">
<td>Update</td>
<td>When changes are made to a selected validation request, <strong>Update</strong> becomes available so that you can save your changes.
<p>{{%notice info%}}</p>
<p>Be aware, that if you update a previously saved validation request, the historical data collected will no longer match the data results of future runs of the request. If your intention is to leave this request unchanged and create a new request, click <strong>Save As New</strong> instead.</p>
<p>{{%/notice%}}</p></td>
</tr>
<tr class="odd">
<td>Save As New</td>
<td>When changes are made to a previously saved validation request, <strong>Save As New</strong> becomes available so that you can save the modified request as a new request.</td>
</tr>
</tbody>
</table>

The full screen Validation Request card displays all scheduled
validation requests.

{{< figure src="/images/netq/valid-request-fullscr-300.png" width="700" >}}

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 85%" />
</colgroup>
<thead>
<tr class="header">
<th>Item</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Title</td>
<td>Validation Request</td>
</tr>
<tr class="even">
<td><img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/close.svg" height="14" width="14"/></td>
<td>Closes full screen card and returns to workbench</td>
</tr>
<tr class="odd">
<td>Default Time</td>
<td>No time period is displayed for this card as each validation request has its own time relationship.</td>
</tr>
<tr class="odd">
<td><img src="https://icons.cumulusnetworks.com/01-Interface-Essential/42-Multimedia-Controls/button-pause.svg" height="18" width="18"/></td>
<td>Displays data refresh status. Click <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/42-Multimedia-Controls/button-pause.svg" height="18" width="18"/> to pause data refresh. Click <img src="https://icons.cumulusnetworks.com/52-Arrows-Diagrams/01-Arrows/arrow-button-circle-right.svg" height="18" width="18"/> to resume data refresh. Current refresh rate is visible by hovering over icon. </td>
</tr>
<tr class="even">
<td>Results</td>
<td>Number of results found for the selected tab</td>
</tr>
<tr class="odd">
<td>Validation Requests</td>
<td>Displays all <em>scheduled</em> validation requests. By default, the requests list is sorted by the date and time that it was originally created (<strong>Created At</strong>). This tab provides the following additional data about each request:
<ul>
<li><strong>Name</strong>: Text identifier of the validation</li>
<li><strong>Type</strong>: Name of network protocols and/or services included in the validation</li>
<li><strong>Start Time</strong>: Data and time that the validation request was run</li>
<li><strong>Last Modified</strong>: Date and time of the most recent change made to the validation request</li>
<li><strong>Cadence (Min)</strong>: How often, in minutes, the validation is scheduled to run. This is empty for new on-demand requests.</li>
<li><strong>Is Active</strong>: Indicates whether the request is currently running according to its schedule (<em>true</em>) or it is not running (<em>false</em>)</li>
</ul></td>
</tr>
<tr class="even">
<td>Table Actions</td>
<td>Select, export, or filter the list. Refer to {{<link url="Access-Data-with-Cards#table-settings" text="Table Settings">}}.</td>
</tr>
</tbody>
</table>

### Create On-demand and Scheduled Validation Requests

There are several types of validation requests that a user can make. Each has a slightly different flow through the Validation Request card,
and is therefore described separately. The types are based on the intent of the request:

- {{<link url="#run-an-existing-scheduled-validation-request-on-demand" text="Run an Existing Scheduled Validation Request On Demand">}}
- {{<link url="#create-a-new-on-demand-validation-request" text="Create a New On-demand Validation Request">}}
- {{<link url="#create-a-new-scheduled-validation-request" text="Create a New Scheduled Validation Request">}}
- {{<link url="#modify-an-existing-scheduled-validation-request" text="Modify an Existing Scheduled Validation Request">}}

### Run an Existing Scheduled Validation Request On Demand

You may find that although you have a validation scheduled to run at a later time, you would like to run it now.

To run a scheduled validation now:

1. Open either the small, medium, or large Validation Request card.
2. Select the validation from the **Validation** dropdown list.  

    {{< figure src="/images/netq/valid-request-small-plus-medium-selection-230.png" width="420" >}}
    {{< figure src="/images/netq/valid-request-large-valid-selection-222.png" width="500" >}}

3. Click **Go** or **Run Now**.  
    The associated Validation Result card is opened on your workbench. Refer to {{<link url="#view-on-demand-validation-results" text="View On-demand Validation Results">}}.

    {{< figure src="/images/netq/valid-request-medium-default-bgp-running-230.png" width="200" >}}

### Create a New On-demand Validation Request

When you want to validate the operation of one or more network protocols and services right now, you can create and run an on-demand validation
request using the large Validation Request card.

To create and run a request for *a single* protocol or service:

1. Open the small, medium or large Validation Request card.
2. Select the validation from the **Validation** dropdown list.

    {{< figure src="/images/netq/valid-request-selection.png" width="300" >}}

3. Click **Go** or **Run Now**.  
    The associated Validation Result card is opened on your workbench. Refer to {{<link url="#view-on-demand-validation-results" text="View On-demand Validation Results">}}.

To create and run a request for *more than one* protocol and/or service:

1. Open the large Validation Request card.

2. Click the names of the protocols and services you want to validate.
    We selected BGP and EVPN in this example.

    {{< figure src="/images/netq/valid-request-bgp-evpn-222.png" width="500" >}}

3. Click **Run Now** to start the validation.  
    The associated on-demand validation result cards (one per protocol or service selected) are opened on your current workbench. Refer to {{<link url="#view-on-demand-validation-results" text="View On-demand Validation Results">}}.

    {{< figure src="/images/netq/valid-request-medium-bgpevpn-running-230.png" width="420" >}}

### Create a New Scheduled Validation Request

When you want to see validation results on a regular basis, it is useful to configure a scheduled validation request to avoid re-creating the
request each time.

To create and run a new scheduled validation:

1. Open the large Validation Request card.
2. Select the protocols and/or services you want to include in the validation. In this example we have chosen the Agents and NTP services.

      {{< figure src="/images/netq/valid-request-agents-ntp-222.png" width="500" >}}

3. Enter the schedule frequency (30 min, 1 hour, 3 hours, 6 hours, 12 hours, or 1 day) by selecting it from the **Run every** list. Default is hourly.

    {{< figure src="/images/netq/schedule-frequency-selection-222.png" width="300" >}}

4. Select the time to start the validation runs, by clicking in the Starting field. Select a day and click **Next**, then select the starting time and click **OK**.  

    {{< figure src="/images/netq/date-selection-222.png" width="150">}}
    <p> </p>
    {{< figure src="/images/netq/time-selection-222.png" width="150">}}

5. Verify the selections were made correctly.
6. Click **Save As New**.

      {{< figure src="/images/netq/valid-request-agents-ntp-save-as-new-222.png" width="500" >}}

7. Enter a name for the validation.

      {{%notice note%}}
Spaces and special characters are *not* allowed in validation request names.
      {{%/notice%}}

      {{< figure src="/images/netq/save-valid-name-example.png" width="250" >}}

8. Click **Save**.

The validation can now be selected from the Validation listing (on the small, medium or large size card) and run immediately using **Run Now**, or you can wait for it to run the first time according to the schedule you specified. Refer to {{<link url="#view-scheduled-validation-results" text="View Scheduled Validation Results">}}. Note that the number of scheduled validations is now two (2).

{{< figure src="/images/netq/valid-request-select-sched-222.png" width="500">}}

### Modify an Existing Scheduled Validation Request

At some point you might want to change the schedule or validation types that are specified in a scheduled validation request.

{{%notice info%}}
When you update a scheduled request, the results for all future runs of the validation will be different than the results of previous runs of the validation.
{{%/notice%}}

To modify a scheduled validation:

1. Open the large Validation Request card.
2. Select the validation from the **Validation** dropdown list.
3. Edit the schedule or validation types.
4. Click **Update**.

The validation can now be selected from the Validation listing (on the small, medium or large size card) and run immediately using **Run Now**, or you can wait for it to run the first time according to the schedule you specified. Refer to {{<link url="#view-scheduled-validation-results" text="View Scheduled Validation Results">}}.

## View On-demand Validation Results

The On-demand Validation Result card workflow enables you to view the results of on-demand validation requests. When a request has started processing, the associated medium Validation Result card is displayed on your workbench. When multiple network protocols or services are included in a validation, a validation result card is opened for each protocol and service.

### On-Demand Validation Result Card Workflow

The small Validation Result card displays:

{{<figure src="/images/netq/valid-result-on-demand-bgp-small-222.png" width="200">}}
<p> </p>
<table>
<colgroup>
<col style="width: 20%" />
<col style="width: 80%" />
</colgroup>
<thead>
<tr class="header">
<th>Item</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><img src="https://icons.cumulusnetworks.com/35-Health-Beauty/07-Monitoring/monitor-heart-beat-search.svg" height="18" width="18"/></td>
<td>Indicates an on-demand validation result</td>
</tr>
<tr class="even">
<td>Title</td>
<td>On-demand Result &lt;Network Protocol or Service Name&gt; Validation</td>
</tr>
<tr class="odd">
<td>Timestamp</td>
<td>Date and time the validation was completed</td>
</tr>
<tr class="even">
<td><img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/check-circle-1.svg" height="18" width="18"/>, <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/remove-shield.svg" height="18" width="18"/></td>
<td>Status of the validation job, where:
<ul>
<li><strong>Good</strong>: Job ran successfully. One or more warnings may have occurred during the run.</li>
<li><strong>Failed</strong>: Job encountered errors which prevented the job from completing, or job ran successfully, but errors occurred during the run.</li>
</ul></td>
</tr>
</tbody>
</table>

The medium Validation Result card displays:

{{<figure src="/images/netq/valid-result-on-demand-bgp-medium-222.png" width="200">}}

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 85%" />
</colgroup>
<thead>
<tr class="header">
<th>Item</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><img src="https://icons.cumulusnetworks.com/35-Health-Beauty/07-Monitoring/monitor-heart-beat-search.svg" height="18" width="18"/></td>
<td>Indicates an on-demand validation result</td>
</tr>
<tr class="even">
<td>Title</td>
<td>On-demand Validation Result | &lt;Network Protocol or Service Name&gt;</td>
</tr>
<tr class="odd">
<td>Timestamp</td>
<td>Date and time the validation was completed</td>
</tr>
<tr class="even">
<td><img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/check-circle-1.svg" height="18" width="18"/>, <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/14-Alerts/alert-triangle.svg" height="18" width="18"/>, <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/remove-shield.svg" height="18" width="18"/></td>
<td>Status of the validation job, where:
<ul>
<li><strong>Good</strong>: Job ran successfully.</li>
<li><strong>Warning</strong>: Job encountered issues, but it did complete its run.</li>
<li><strong>Failed</strong>: Job encountered errors which prevented the job from completing.</li>
</ul></td>
</tr>
<tr class="odd">
<td>Devices Tested</td>
<td>Chart with the total number of devices included in the validation and the distribution of the results.
<ul>
<li><strong>Pass</strong>: Number of devices tested that had successful results</li>
<li><strong>Warn</strong>: Number of devices tested that had successful results, but also had at least one warning event</li>
<li><strong>Fail</strong>: Number of devices tested that had one or more protocol or service failures</li>
</ul>
<p>Hover over chart to view the number of devices and the percentage of all tested devices for each result category.</p></td>
</tr>
<tr class="even">
<td>Sessions Tested</td>
<td><p>For BGP, chart with total number of BGP sessions included in the validation and the distribution of the overall results.</p>
<p>For EVPN, chart with total number of BGP sessions included in the validation and the distribution of the overall results.</p>
<p>For Interfaces, chart with total number of ports included in the validation and the distribution of the overall results.</p>
<p>In each of these charts:</p>
<ul>
<li><strong>Pass</strong>: Number of sessions or ports tested that had successful results</li>
<li><strong>Warn</strong>: Number of sessions or ports tested that had successful results, but also had at least one warning event</li>
<li><strong>Fail</strong>: Number of sessions or ports tested that had one or more failure events</li>
</ul>
<p>Hover over chart to view the number of devices, sessions, or ports and the percentage of all tested devices, sessions, or ports for each result category.</p>
<p>This chart does not apply to other Network Protocols and Services, and thus is not displayed for those cards.</p></td>
</tr>
<tr class="odd">
<td>Open &lt;Service&gt;  Card</td>
<td>Click to open the corresponding medium Network Services card, where available. Refer to {{<link title="Monitor Network Performance">}} for details about these cards and workflows.</td>
</tr>
</tbody>
</table>

The large Validation Result card contains two tabs.

The *Summary* tab displays:

{{< figure src="/images/netq/od-valid-result-bgp-large.png" width="500" >}}

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 85%" />
</colgroup>
<thead>
<tr class="header">
<th>Item</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><img src="https://icons.cumulusnetworks.com/35-Health-Beauty/07-Monitoring/monitor-heart-beat-search.svg" height="18" width="18"/></td>
<td>Indicates an on-demand validation result</td>
</tr>
<tr class="even">
<td>Title</td>
<td>On-demand Validation Result | Summary | &lt;Network Protocol or Service Name&gt;</td>
</tr>
<tr class="odd">
<td>Date</td>
<td>Day and time when the validation completed</td>
</tr>
<tr class="even">
<td><img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/check-circle-1.svg" height="18" width="18"/>, <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/14-Alerts/alert-triangle.svg" height="18" width="18"/>, <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/remove-shield.svg" height="18" width="18"/></td>
<td>Status of the validation job, where:
<ul>
<li><strong>Good</strong>: Job ran successfully.</li>
<li><strong>Warning</strong>: Job encountered issues, but it did complete its run.</li>
<li><strong>Failed</strong>: Job encountered errors which prevented the job from completing.</li>
</ul></td>
</tr>
<tr class="odd">
<td>Devices Tested</td>
<td>Chart with the total number of devices included in the validation and the distribution of the results.
<ul>
<li><strong>Pass</strong>: Number of devices tested that had successful results</li>
<li><strong>Warn</strong>: Number of devices tested that had successful results, but also had at least one warning event</li>
<li><strong>Fail</strong>: Number of devices tested that had one or more protocol or service failures</li>
</ul>
<p>Hover over chart to view the number of devices and the percentage of all tested devices for each result category.</p></td>
</tr>
<tr class="even">
<td>Sessions Tested</td>
<td><p>For BGP, chart with total number of BGP sessions included in the validation and the distribution of the overall results.</p>
<p>For EVPN, chart with total number of BGP sessions included in the validation and the distribution of the overall results.</p>
<p>For Interfaces, chart with total number of ports included in the validation and the distribution of the overall results.</p>
<p>For OSPF, chart with total number of OSPF sessions included in the validation and the distribution of the overall results.</p>
<p>In each of these charts:</p>
<ul>
<li><strong>Pass</strong>: Number of sessions or ports tested that had successful results</li>
<li><strong>Warn</strong>: Number of sessions or ports tested that had successful results, but also had at least one warning event</li>
<li><strong>Fail</strong>: Number of sessions or ports tested that had one or more failure events</li>
</ul>
<p>Hover over chart to view the number of devices, sessions, or ports and the percentage of all tested devices, sessions, or ports for each result category.</p>
<p>This chart does not apply to other Network Protocols and Services, and thus is not displayed for those cards.</p></td>
</tr>
<tr class="odd">
<td>Open &lt;Service&gt; Card</td>
<td>Click to open the corresponding medium Network Services card, when available. Refer to {{<link title="Monitor Network Performance">}} for details about these cards and workflows.</td>
</tr>
<tr class="even">
<td>Table/Filter options</td>
<td><p>When the <strong>Most Active</strong> filter option is selected, the table displays switches and hosts running the given service or protocol in decreasing order of alarm counts. Devices with the largest number of warnings and failures are listed first. You can click on the device name to open its switch card on your workbench.</p>
<p>When the <strong>Most Recent</strong> filter option is selected, the table displays switches and hosts running the given service or protocol sorted by <strong>timestamp</strong>, with the device with the most recent warning or failure listed first. The table provides the following additional information:</p>
<ul>
<li><strong>Hostname</strong>: User-defined name for switch or host</li>
<li><strong>Message Type</strong>: Network protocol or service which triggered the event</li>
<li><strong>Message</strong>: Short description of the event</li>
<li><strong>Severity</strong>: Indication of importance of event; values in decreasing severity include critical, warning, error, info, debug</li>
</ul></td>
</tr>
<tr class="odd">
<td>Show All Results</td>
<td>Click to open the full screen card with all on-demand validation results sorted by timestamp.</td>
</tr>
</tbody>
</table>

The *Configuration* tab displays:

{{< figure src="/images/netq/od-valid-result-bgp-large-config-tab-230.png" width="500" >}}
<p> </p>
<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 85%" />
</colgroup>
<thead>
<tr class="header">
<th>Item</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><img src="https://icons.cumulusnetworks.com/01-Interface-Essential/12-Settings/cog-1.svg" height="18" width="18"/></td>
<td>Indicates an on-demand validation request configuration</td>
</tr>
<tr class="even">
<td>Title</td>
<td>On-demand Validation Result | Configuration | &lt;Network Protocol or Service Name&gt;</td>
</tr>
<tr class="odd">
<td>Validations</td>
<td>List of network protocols or services included in the request that produced these results</td>
</tr>
<tr class="even">
<td>Schedule</td>
<td>Not relevant to on-demand validation results. Value is always N/A.</td>
</tr>
</tbody>
</table>

The full screen Validation Result card provides a tab for all on-demand validation results.

{{< figure src="/images/netq/od-valid-result-bgp-fullscr-300.png" width="700" >}}

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 85%" />
</colgroup>
<thead>
<tr class="header">
<th>Item</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Title</td>
<td>Validation Results | On-demand</td>
</tr>
<tr class="even">
<td><img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/close.svg" height="14" width="14"/></td>
<td>Closes full screen card and returns to workbench</td>
</tr>
<tr class="odd">
<td>Time period</td>
<td>Range of time in which the displayed data was collected; applies to all card sizes; select an alternate time period by clicking <img src="https://icons.cumulusnetworks.com/52-Arrows-Diagrams/01-Arrows/arrow-button-down-2.svg" height="14" width="14"/></td>
</tr>
<tr class="odd">
<td><img src="https://icons.cumulusnetworks.com/01-Interface-Essential/42-Multimedia-Controls/button-pause.svg" height="18" width="18"/></td>
<td>Displays data refresh status. Click <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/42-Multimedia-Controls/button-pause.svg" height="18" width="18"/> to pause data refresh. Click <img src="https://icons.cumulusnetworks.com/52-Arrows-Diagrams/01-Arrows/arrow-button-circle-right.svg" height="18" width="18"/> to resume data refresh. Current refresh rate is visible by hovering over icon. </td>
</tr>
<tr class="even">
<td>Results</td>
<td>Number of results found for the selected tab</td>
</tr>
<tr class="odd">
<td>On-demand Validation Result | &lt;network protocol or service&gt;</td>
<td>Displays all unscheduled validation results. By default, the results list is sorted by <strong>Timestamp</strong>. This tab provides the following additional data about each result:
<ul>
<li><strong>Job ID</strong>: Internal identifier of the validation job that produced the given results</li>
<li><strong>Timestamp</strong>: Date and time the validation completed</li>
<li><strong>Type</strong>: Network protocol or service type</li>
<li><strong>Total Node Count</strong>: Total number of nodes running the given network protocol or service</li>
<li><strong>Checked Node Count</strong>: Number of nodes on which the validation ran</li>
<li><strong>Failed Node Count</strong>: Number of checked nodes that had protocol or service failures</li>
<li><strong>Rotten Node Count</strong>: Number of nodes that could not be reached during the validation</li>
<li><strong>Unknown Node Count</strong>: Applies only to the Interfaces service. Number of nodes with unknown port states.</li>
<li><strong>Failed Adjacent Count</strong>: Number of adjacent nodes that had protocol or service failures</li>
<li><strong>Total Session Count</strong>: Total number of sessions running for the given network protocol or service</li>
<li><strong>Failed Session Count</strong>: Number of sessions that had session failures</li>
</ul></td>
</tr>
<tr class="even">
<td>Table Actions</td>
<td>Select, export, or filter the list. Refer to {{<link url="Access-Data-with-Cards#table-settings" text="Table Settings">}}.</td>
</tr>
</tbody>
</table>

### View On-demand Validation Results

Once an on-demand validation request has completed, the results are available in the corresponding Validation Result card.

{{<notice tip>}}
It may take a few minutes for all results to be presented if the load on the NetQ Platform is heavy at the time of the run.
{{</notice>}}

To view the results:

1. Locate the medium on-demand Validation Result card on your workbench for the protocol or service that was run.  

    You can identify it by the on-demand result icon, <img src="https://icons.cumulusnetworks.com/35-Health-Beauty/07-Monitoring/monitor-heart-beat-search.svg" height="18" width="18"/>, protocol or service name, and the date and time that it was run.  

    **Note:** You may have more than one card open for a given protocol or service, so be sure to use the date and time on the card to     ensure you are viewing the correct card.  

    {{< figure src="/images/netq/od-valid-result-bgp-medium-date-highlight-230.png" width="420" >}}

2. Note the total number and distribution of results for the tested devices and sessions (when appropriate). Are there many failures?

3. Hover over the charts to view the total number of warnings or failures and what percentage of the total results that represents for both devices and sessions.

4. Switch to the large on-demand Validation Result card.

    {{< figure src="/images/netq/od-valid-result-bgp-large-230.png" width="500" >}}

5. If there are a large number of device warnings or failures, view the devices with the most issues in the table on the right. By default, this table displays the **Most Active** devices. Click on a device name to open its switch card on your workbench.

6. To view the most recent issues, select **Most Recent** from the filter above the table.

7. If there are a large number of devices or sessions with warnings or failures, the protocol or service may be experiencing issues. View     the health of the protocol or service as a whole by clicking **Open** \<*network service*\> **Card** when available.

8. To view all data available for all on-demand validation results for a given protocol, switch to the full screen card.

    {{< figure src="/images/netq/od-valid-result-bgp-fullscr-300.png" width="700" >}}

9. Double-click in a given result row to open details about the validation.

    From this view you can:
    - See a summary of the validation results by clicking <img src="https://icons.cumulusnetworks.com/52-Arrows-Diagrams/01-Arrows/arrow-button-right-2.svg" width="14" height="14"/> in the banner under the title. Toggle the arrow to close the summary.

        {{< figure src="/images/netq/od-valid-result-bgp-details-summary-fullscr.png" width="300" >}}

    - See detailed results of each test run to validate the protocol or service. When errors or warnings are present, the nodes and relevant detail is provided.

        {{< figure src="/images/netq/od-valid-result-bgp-tests-fullscr.png" width="700" >}}
    
    - Export the data by clicking **Export**.

    - Return to the validation jobs list by clicking <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/close.svg" width="14" height="14"/>.

    You may find that comparing various results gives you a clue as to why certain devices are experiencing more warnings or failures. For     example, more failures occurred between certain times or on a particular device.

## View Scheduled Validation Results

The Scheduled Validation Result card workflow enables you to view the results of scheduled validation requests. When a request has completed processing, you can access the Validation Result card from the full screen Validation Request card. Each protocol and service has its own validation result card, but the content is similar on each.

### Scheduled Validation Result Card Workflow Summary

The small Scheduled Validation Result card displays:

{{< figure src="/images/netq/sch-valid-result-small-4cards-230.png" width="700" >}}

<table>
<colgroup>
<col style="width: 20%" />
<col style="width: 80%" />
</colgroup>
<thead>
<tr class="header">
<th>Item</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><img src="https://icons.cumulusnetworks.com/03-Computers-Devices-Electronics/01-Smart-Watches/smart-watch-square-graph-line.svg" height="18" width="18"/></td>
<td>Indicates a scheduled validation result</td>
</tr>
<tr class="even">
<td>Title</td>
<td>Scheduled Result &lt;Network Protocol or Service Name&gt; Validation</td>
</tr>
<tr class="odd">
<td>Results</td>
<td>Summary of validation results:
<ul>
<li><img src="https://icons.cumulusnetworks.com/01-Interface-Essential/21-Date-Calendar/calendar-refresh.svg" height="18" width="18"/> Number of validation runs completed in the designated time period</li>
<li><img src="https://icons.cumulusnetworks.com/01-Interface-Essential/14-Alerts/alert-triangle.svg" height="18" width="18"/> Number of runs with warnings</li>
<li><img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/remove-shield.svg" height="18" width="18"/> Number of runs with errors</li>
</ul></td>
</tr>
<tr class="even">
<td><img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/check-circle-1.svg" height="18" width="18"/>, <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/remove-shield.svg" height="18" width="18"/></td>
<td>Status of the validation job, where:
<ul>
<li><strong>Pass</strong>: Job ran successfully. One or more warnings may have occurred during the run.</li>
<li><strong>Failed</strong>: Job encountered errors which prevented the job from completing, or job ran successfully, but errors occurred during the run.</li>
</ul></td>
</tr>
</tbody>
</table>

The medium Scheduled Validation Result card displays:

{{<figure src="/images/netq/sch-valid-result-medium-222.png" width="425">}}

<table>
<colgroup>
<col style="width: 20%" />
<col style="width: 80%" />
</colgroup>
<thead>
<tr class="header">
<th>Item</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Time period</td>
<td>Range of time in which the displayed data was collected; applies to all card sizes</td>
</tr>
<tr class="even">
<td><img src="https://icons.cumulusnetworks.com/03-Computers-Devices-Electronics/01-Smart-Watches/smart-watch-square-graph-line.svg" height="18" width="18"/></td>
<td>Indicates a scheduled validation result</td>
</tr>
<tr class="odd">
<td>Title</td>
<td>Scheduled Validation Result | &lt;Network Protocol or Service Name&gt;</td>
</tr>
<tr class="even">
<td>Summary</td>
<td>Summary of validation results:
<ul>
<li>Name of scheduled validation</li>
<li>Status of the validation job, where:
<ul>
<li><img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/check-circle-1.svg" height="18" width="18"/> <strong>Pass</strong>: Job ran successfully. One or more warnings may have occurred during the run.</li>
<li><img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/remove-shield.svg" height="18" width="18"/> <strong>Failed</strong>: Job encountered errors which prevented the job from completing, or job ran successfully, but errors occurred during the run.</li>
</ul></li>
</ul></td>
</tr>
<tr class="odd">
<td>Chart</td>
<td>Validation results, where:
<ul>
<li><strong>Time period</strong>: Range of time in which the data on the heat map was collected</li>
<li><strong>Heat map</strong>: A time segmented view of the results. For each time segment, the color represents the percentage of warning, passing, and failed results. Refer to {{<link title="#Granularity of Data Shown Based on Time Period">}} for details on how to interpret the results.</li>
</ul></td>
</tr>
<tr class="even">
<td>Open &lt;Service&gt; Card</td>
<td>Click to open the corresponding medium Network Services card, when available. Refer to {{<link title="Monitor Network Performance">}} for details about these cards and workflows.</td>
</tr>
</tbody>
</table>

The large Scheduled Validation Result card contains two tabs.

   The *Summary* tab displays:

   {{< figure src="/images/netq/sch-valid-result-large-sum-tab-222.png" width="500" >}}

<table>
<colgroup>
<col style="width: 20%" />
<col style="width: 80%" />
</colgroup>
<thead>
<tr class="header">
<th>Item</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><img src="https://icons.cumulusnetworks.com/03-Computers-Devices-Electronics/01-Smart-Watches/smart-watch-square-graph-line.svg" height="18" width="18"/></td>
<td>Indicates a scheduled validation result</td>
</tr>
<tr class="even">
<td>Title</td>
<td>Validation Summary (Scheduled Validation Result | &lt;Network Protocol or Service Name&gt;)</td>
</tr>
<tr class="odd">
<td>Summary</td>
<td>Summary of validation results:
<ul>
<li>Name of scheduled validation</li>
<li>Status of the validation job, where:
<ul>
<li><img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/check-circle-1.svg" height="18" width="18"/> <strong>Pass</strong>: Job ran successfully. One or more warnings may have occurred during the run.</li>
<li><img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/remove-shield.svg" height="18" width="18"/> <strong>Failed</strong>: Job encountered errors which prevented the job from completing, or job ran successfully, but errors occurred during the run.</li>
</ul></li>
<li><img src="https://icons.cumulusnetworks.com/01-Interface-Essential/53-Resize/expand-horizontal-3.svg" height="18" width="18"/> <strong>Expand/Collapse</strong>: Expand the heat map to full width of card, collapse the heat map to the left</li>
</ul></td>
</tr>
<tr class="even">
<td>Chart</td>
<td>Validation results, where:
<ul>
<li><strong>Time period</strong>: Range of time in which the data on the heat map was collected</li>
<li><strong>Heat map</strong>: A time segmented view of the results. For each time segment, the color represents the percentage of warning, passing, and failed results. Refer to {{<link title="#Granularity of Data Shown Based on Time Period">}} for details on how to interpret the results.</li>
</ul></td>
</tr>
<tr class="odd">
<td>Open &lt;Service&gt; Card</td>
<td>Click to open the corresponding medium Network Services card, when available. Refer to {{<link title="Monitor Network Performance">}} for details about these cards and workflows.</td>
</tr>
<tr class="even">
<td>Table/Filter options</td>
<td><p>When the <strong>Most Active</strong> filter option is selected, the table displays switches and hosts running the given service or protocol in decreasing order of alarm counts-devices with the largest number of warnings and failures are listed first.</p>
<p>When the <strong>Most Recent</strong> filter option is selected, the table displays switches and hosts running the given service or protocol sorted by <strong>timestamp</strong>, with the device with the most recent warning or failure listed first. The table provides the following additional information:</p>
<ul>
<li><strong>Hostname</strong>: User-defined name for switch or host</li>
<li><strong>Message Type</strong>: Network protocol or service which triggered the event</li>
<li><strong>Message</strong>: Short description of the event</li>
<li><strong>Severity</strong>: Indication of importance of event; values in decreasing severity include critical, warning, error, info, debug</li>
</ul></td>
</tr>
<tr class="odd">
<td>Show All Results</td>
<td>Click to open the full screen card with all scheduled validation results sorted by timestamp.</td>
</tr>
</tbody>
</table>

The *Configuration* tab displays:

{{< figure src="/images/netq/sch-valid-result-large-config-tab-222.png" width="500" >}}

<table>
<colgroup>
<col style="width: 20%" />
<col style="width: 80%" />
</colgroup>
<thead>
<tr class="header">
<th>Item</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><img src="https://icons.cumulusnetworks.com/01-Interface-Essential/12-Settings/cog-1.svg" height="18" width="18"/></td>
<td>Indicates a scheduled validation configuration</td>
</tr>
<tr class="even">
<td>Title</td>
<td>Configuration (Scheduled Validation Result | &lt;Network Protocol or Service Name&gt;)</td>
</tr>
<tr class="odd">
<td>Name</td>
<td>User-defined name for this scheduled validation</td>
</tr>
<tr class="even">
<td>Validations</td>
<td>List of validations included in the validation request that created this result</td>
</tr>
<tr class="odd">
<td>Schedule</td>
<td>User-defined schedule for the validation request that created this result</td>
</tr>
<tr class="even">
<td>Open Schedule Card</td>
<td>Opens the large Validation Request card for editing this configuration</td>
</tr>
</tbody>
</table>

The full screen Scheduled Validation Result card provides tabs for all scheduled
validation results for the service.

{{< figure src="/images/netq/sch-valid-result-fullscr-300.png" width="700" >}}

<table>
<colgroup>
<col style="width: 20%" />
<col style="width: 80%" />
</colgroup>
<thead>
<tr class="header">
<th>Item</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Title</td>
<td>Scheduled Validation Results | &lt;Network Protocol or Service&gt;</td>
</tr>
<tr class="even">
<td><img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/close.svg" height="14" width="14"/></td>
<td>Closes full screen card and returns to workbench</td>
</tr>
<tr class="odd">
<td>Time period</td>
<td>Range of time in which the displayed data was collected; applies to all card sizes; select an alternate time period by clicking <img src="https://icons.cumulusnetworks.com/52-Arrows-Diagrams/01-Arrows/arrow-button-down-2.svg" height="14" width="14"/></td>
</tr>
<tr class="odd">
<td><img src="https://icons.cumulusnetworks.com/01-Interface-Essential/42-Multimedia-Controls/button-pause.svg" height="18" width="18"/></td>
<td>Displays data refresh status. Click <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/42-Multimedia-Controls/button-pause.svg" height="18" width="18"/> to pause data refresh. Click <img src="https://icons.cumulusnetworks.com/52-Arrows-Diagrams/01-Arrows/arrow-button-circle-right.svg" height="18" width="18"/> to resume data refresh. Current refresh rate is visible by hovering over icon. </td>
</tr>
<tr class="even">
<td>Results</td>
<td>Number of results found for the selected tab</td>
</tr>
<tr class="odd">
<td>Scheduled Validation Result | &lt;network protocol or service&gt;</td>
<td>Displays all unscheduled validation results. By default, the results list is sorted by timestamp. This tab provides the following additional data about each result:
<ul>
<li><strong>Job ID</strong>: Internal identifier of the validation job that produced the given results</li>
<li><strong>Timestamp</strong>: Date and time the validation completed</li>
<li><strong>Type:</strong> Protocol of Service Name</li>
<li><strong>Total Node Count</strong>: Total number of nodes running the given network protocol or service</li>
<li><strong>Checked Node Count</strong>: Number of nodes on which the validation ran</li>
<li><strong>Failed Node Count</strong>: Number of checked nodes that had protocol or service failures</li>
<li><strong>Rotten Node Count</strong>: Number of nodes that could not be reached during the validation</li>
<li><strong>Unknown Node Count</strong>: Applies only to the Interfaces service. Number of nodes with unknown port states.</li>
<li><strong>Failed Adjacent Count</strong>: Number of adjacent nodes that had protocol or service failures</li>
<li><strong>Total Session Count</strong>: Total number of sessions running for the given network protocol or service</li>
<li><strong>Failed Session Count</strong>: Number of sessions that had session failures</li>
</ul></td>
</tr>
<tr class="even">
<td>Table Actions</td>
<td>Select, export, or filter the list. Refer to {{<link url="Access-Data-with-Cards#table-settings" text="Table Settings">}}.</td>
</tr>
</tbody>
</table>

### Granularity of Data Shown Based on Time Period

On the medium and large Validation Result cards, the status of the runs is represented in heat maps stacked vertically; one for passing runs,  one for runs with warnings, and one for runs with failures. Depending on the time period of data on the card, the number of smaller time blocks used to indicate the status varies. A vertical stack of time blocks, one from each map, includes the results from all checks during that time. The results are shown by how saturated the color is for each block. If all validations during that time period pass, then the middle block is 100% saturated (white) and the warning and failure blocks are zero % saturated (gray). As warnings and errors increase in saturation, the passing block is proportionally reduced in saturation. An example heat map for a time period of 24 hours is shown here with the most common time periods in the table showing the resulting time blocks and regions.

{{<figure src="/images/netq/sch-valid-result-granularity-230.png" width="300">}}

| Time Period | Number of Runs | Number Time Blocks | Amount of Time in Each Block |
| ----------- | -------------- | ------------------ | ---------------------------- |
| 6 hours     | 18             | 6                  | 1 hour                       |
| 12 hours    | 36             | 12                 | 1 hour                       |
| 24 hours    | 72             | 24                 | 1 hour                       |
| 1 week      | 504            | 7                  | 1 day                        |
| 1 month     | 2,086          | 30                 | 1 day                        |
| 1 quarter   | 7,000          | 13                 | 1 week                       |

### View Scheduled Validation Results

Once a scheduled validation request has completed, the results are available in the corresponding Validation Result card.

To view the results:

1. Open the full size Validation Request card to view all scheduled validations.

    {{<figure src="/images/netq/valid-request-fullscr-300.png" width="700">}}

2. Select the validation results you want to view by clicking in the first column of the result and clicking the check box.

3. On the Edit Menu that appears at the bottom of the window, click <img src="https://icons.cumulusnetworks.com/44-Entertainment-Events-Hobbies/02-Card-Games/card-game-diamond.svg" height="18" width="18"/> (Open Cards). This opens the medium Scheduled Validation Results card(s) for the selected items.

    {{<figure src="/images/netq/sch-valid-result-medium-222.png" width="425">}}

4. Note the distribution of results. Are there many failures? Are they concentrated together in time? Has the protocol or service recovered     after the failures?

5. Hover over the heat maps to view the status numbers and what percentage of the total results that represents for a given region. The tooltip also shows the number of devices included in the validation and the number with warnings and/or failures. This is useful when you see the failures occurring on a small set of devices, as it might point to an issue with the devices rather than the network service.

    {{<figure src="/images/netq/sch-valid-result-medium-bgp-popup-222.png" width="200">}}

6. Optionally, click **Open** \<*network service*\> **Card** link to open the medium individual Network Services card. Your current card is not closed.

7. Switch to the large Scheduled Validation card.

8. Click <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/53-Resize/expand-horizontal-3.svg" height="18" width="18"/> to expand the chart.

    {{<figure src="/images/netq/sch-valid-result-large-bgp-expand-chart-230.png" width="500">}}

9. Collapse the heat map by clicking <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/53-Resize/expand-horizontal-3.svg" height="18" width="18"/>.

    {{<figure src="/images/netq/sch-valid-result-large-bgp-collapse-chart-230.png" width="500">}}

10. If there are a large number of warnings or failures, view the devices with the most issues by clicking **Most Active** in the filter above the table. This might help narrow the failures down to a particular device or small set of devices that you can investigate further.

11. Select the **Most Recent** filter above the table to see the events that have occurred in the near past at the top of the list.

12. Optionally, view the health of the protocol or service as a whole by clicking **Open** \<*network service*\> **Card** (when available).

13. You can view the configuration of the request that produced the results shown on this card workflow, by hovering over the card and     clicking <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/12-Settings/cog-1.svg" height="18" width="18"/>. If you want to change the configuration, click **Edit Config** to open the large Validation Request card, pre-populated with the current configuration. Follow the instructions in {{<link url="#modify-an-existing-scheduled-validation-request" text="Modify an Existing Scheduled Validation Request">}} to make your changes.

14. To view all data available for all scheduled validation results for the given protocol or service, click **Show All Results** or switch to the full screen card.

    {{< figure src="/images/netq/sch-valid-result-fullscr-bgp-241.png" width="700" >}}

15. Look for changes and patterns in the results. Scroll to the right. Are there more failed sessions or nodes during one or more validations?

16. Double-click in a given result row to open details about the validation.

    From this view you can:
    - See a summary of the validation results by clicking <img src="https://icons.cumulusnetworks.com/52-Arrows-Diagrams/01-Arrows/arrow-button-right-2.svg" width="14" height="14"/> in the banner under the title. Toggle the arrow to close the summary.

        {{< figure src="/images/netq/od-valid-result-bgp-details-summary-fullscr.png" width="300" >}}

    - See detailed results of each test run to validate the protocol or service. When errors or warnings are present, the nodes and relevant detail is provided.

        {{< figure src="/images/netq/od-valid-result-bgp-tests-fullscr.png" width="700" >}}

    - Export the data by clicking **Export**.

    - Return to the validation jobs list by clicking <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/close.svg" width="14" height="14"/>.

    You may find that comparing various results gives you a clue as to why certain devices are experiencing more warnings or failures. For  example, more failures occurred between certain times or on a particular device.
