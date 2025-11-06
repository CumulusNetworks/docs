---
title: Monitor Events
author: NVIDIA
weight: 775
toc: 4
---
Use the UI or CLI to monitor events: you can view all events across the entire network or all events on a device, then filter events according to their type, severity, or time frame. Event querying is supported for a 72-hour window within the past 30 days.

{{<notice note>}}
It can take several minutes for the NetQ UI to process and accurately display network events. The delay is caused by events with multiple network dependencies. It takes between 5 and 10 minutes for NetQ to consolidate and display these events.
{{</notice>}}

Refer to {{<link title="Configure System Event Notifications">}} for information about configuring third-party applications to broadcast NetQ events.
## Event Commands

- {{<link title="show/#netq-show-events" text="netq show events">}}

## Monitor Events in the UI

Expand the {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/03-Menu/navigation-menu.svg" height="18" width="18">}} **Menu**, then select **Events**.

The dashboard presents a timeline of events alongside the devices that are causing the most events. You can select the controls above the summary to filter events by time, device (hostname), type, severity, or state. Select the tabs below the controls to display all events networkwide, interface events, network services events, system events, or threshold-crossing events. The charts and tables update according to the tab you've selected.

  {{<figure src="/images/netq/events-full-460.png" width="1200" alt="Events dashboard with networkwide error and info events.">}}

Events are also generated when streaming {{<link title="Validation Tests Reference" text="validation checks">}} detect a failure. If an event is generated from a failed validation check, it will be marked resolved automatically the next time the check runs successfully.

## Create Event Filters

You can create, save, and apply filters to show a subset of events. After you save the filters, navigate back to your workbench to view filtered and unfiltered data side-by-side. For example, the left-most card displays all network events from the past 24 hours alongside a filtered subset of BGP 'error' events from the past six hours:

{{<figure src="/images/netq/events-plus-filter-413.png" width="500" alt="">}}

{{<tabs "TabID38" >}}

{{<tab "NetQ UI">}}

To create a filter in the NetQ UI:

1. Expand the Events card to full-screen.

2. Use the controls above the events summary to create a filter according to time parameters, hostname, event type, or event severity.

3. Select **Save filters** and enter a descriptive name for the filter. Then select **Save**.

The events summary now displays the filtered data. Select the X in the top-right corner to return to your workbench. The events card displays a filter with a red dot, indicating that you are viewing filtered data. Hover your mouse over the filter to view its name. If you have not included a custom time filter, you can select the clock <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/18-Time/time-stopwatch.svg" height="18" width="18"/> to adjust the time period of the data reflected on the card.

To clear or delete the filter, expand the card to full-screen and select **Clear all filters** from above the table. When you remove cards from a workbench, the cards' respective filters are also deleted. Note that when you clone a workbench, you must recreate the filters on the new, cloned workbench. 

{{</tab>}}

{{</tabs>}}

## Suppress Events

 If you are receiving too many event notifications or do not want NetQ to display known issues or false alarms, you can suppress these events. NetQ does not display suppressed events in the event summary dashboard, which effectively allows you to ignore them. In addition to the rules you create to suppress events, NetQ suppresses some events by default. 

You can suppress events for the following types of messages:

- Adaptive routing
- BGP
- BTRFS information (events related to the BTRFS file system in Cumulus Linux)
- Cable
- CL support (events generated when creating the `cl-support script`)
- EVPN
- Installed packages
- Lifecycle management
- Link (events related to links, including state and interface name)
- LLDP
- MLAG
- MTU
- NetQ agent
- NTP
- PTM
- PTP
- RoCE configuration
- Running config diff (events related to the difference between two configurations)
- Sensor
- Services (including whether a service is active or inactive)
- SSD utilization (events related to the storage on a switch)
- Topology

{{<notice note>}} 

NetQ suppresses BGP, EVPN, link, cable, and sensor-related events with a severity level of 'info' by default in the UI. You can {{<link url="#delete-or-disable-an-event-suppression-rule" text="disable this rule">}} if you'd prefer to receive these notifications.

{{</notice>}}

### Create an Event Suppression Configuration

If you see a type of event displayed in the events dashboard that you'd like to suppress, navigate to the *Event suppression* column and select **Suppress events**. The wizard described below will be pre-filled with your suppression criteria.

{{<tabs "TabID1689" >}}

{{<tab "NetQ UI" >}}

To suppress events using the NetQ UI:

1. Click {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/03-Menu/navigation-menu.svg" height="18" width="18">}} **Menu**, then **Events**.

2. In the top-right corner, select **Show suppression rules**.

3. Select **Add rule**. You can configure individual suppression rules or you can create a group rule that suppresses events for all message types.
    {{<figure src="/images/netq/create-suppression-rule-modal.png" width="600">}}

4. Give your rule a name and fill out the fields. Then select **Create**.

{{</tab>}}

{{<tab "NetQ CLI" >}}

When you add a new configuration using the CLI, you can specify a scope, which limits the suppression in the following order:

1. Hostname.
2. Severity.
3. Message type-specific filters. For example, the target VNI for EVPN messages, or the interface name for a link message.

NetQ has a predefined set of filter conditions. To see these conditions, run `netq show events-config show-filter-conditions`:

```
nvidia@switch:~$ netq show events-config show-filter-conditions
Matching config_events records:
Message Name             Filter Condition Name                      Filter Condition Hierarchy                           Filter Condition Description
------------------------ ------------------------------------------ ---------------------------------------------------- --------------------------------------------------------
evpn                     vni                                        3                                                    Target VNI
evpn                     severity                                   2                                                    Severity error/info
evpn                     hostname                                   1                                                    Target Hostname
clsupport                fileAbsName                                3                                                    Target File Absolute Name
clsupport                severity                                   2                                                    Severity error/info
clsupport                hostname                                   1                                                    Target Hostname
link                     new_state                                  4                                                    up / down
link                     ifname                                     3                                                    Target Ifname
link                     severity                                   2                                                    Severity error/info
link                     hostname                                   1                                                    Target Hostname
ospf                     ifname                                     3                                                    Target Ifname
ospf                     severity                                   2                                                    Severity error/info
ospf                     hostname                                   1                                                    Target Hostname
sensor                   new_s_state                                4                                                    New Sensor State Eg. ok
sensor                   sensor                                     3                                                    Target Sensor Name Eg. Fan, Temp
sensor                   severity                                   2                                                    Severity error/info
sensor                   hostname                                   1                                                    Target Hostname
configdiff               old_state                                  5                                                    Old State
configdiff               new_state                                  4                                                    New State
configdiff               type                                       3                                                    File Name
configdiff               severity                                   2                                                    Severity error/info
configdiff               hostname                                   1                                                    Target Hostname
ssdutil                  info                                       3                                                    low health / significant health drop
ssdutil                  severity                                   2                                                    Severity error/info
ssdutil                  hostname                                   1                                                    Target Hostname
agent                    db_state                                   3                                                    Database State
agent                    severity                                   2                                                    Severity error/info
agent                    hostname                                   1                                                    Target Hostname
ntp                      new_state                                  3                                                    yes / no
ntp                      severity                                   2                                                    Severity error/info
ntp                      hostname                                   1                                                    Target Hostname
bgp                      vrf                                        4                                                    Target VRF
bgp                      peer                                       3                                                    Target Peer
bgp                      severity                                   2                                                    Severity error/info
bgp                      hostname                                   1                                                    Target Hostname
services                 new_status                                 4                                                    active / inactive
services                 name                                       3                                                    Target Service Name Eg.netqd, mstpd, zebra
services                 severity                                   2                                                    Severity error/info
services                 hostname                                   1                                                    Target Hostname
btrfsinfo                info                                       3                                                    high btrfs allocation space / data storage efficiency
btrfsinfo                severity                                   2                                                    Severity error/info
btrfsinfo                hostname                                   1                                                    Target Hostname
clag                     severity                                   2                                                    Severity error/info
clag                     hostname                                   1                                                    Target Hostname
```

For example, to create a configuration called `mybtrfs` that suppresses BTRFS-related events on leaf01 for the next 10 minutes, run:

```
netq add events-config events_config_name mybtrfs message_type btrfsinfo scope '[{"scope_name":"hostname","scope_value":"leaf01"},{"scope_name":"severity","scope_value":"*"}]' suppress_until 600
```
{{</tab>}}

{{</tabs>}}
### Delete or Disable a Suppression Rule

Delete a suppression rule to resume event notifications. Disable a suppression rule to temporarily resume event notifications. After you disabling a rule, you can choose to either re-enable or delete it. 

{{<tabs "TabID1776" >}}

{{<tab "NetQ UI" >}}

To remove suppressed event configurations:

1. Click {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/03-Menu/navigation-menu.svg" height="18" width="18">}} **Menu**, then **Events**.

2. Select **Show suppression rules** at the top of the page.

3. Toggle between the **Single** and **All** tabs to alternately view one suppression rule or a group of rules. Navigate to the rule you want to delete or disable.

4. For a single rule, click the three-dot menu and select **Delete**. To pause the rule instead of deleting it, click **Disable**. To delete a group of rules, click the three-dot menu and select **Delete**. To disable individual rules within the group, select **View all**, then **Disable**.

{{</tab>}}

{{<tab "NetQ CLI" >}}

To remove an event suppression configuration, run the {{<link title="del/#netq del events-config" text="netq del events-config">}} and include the identifier for the suppression configuration.

```
nvidia@switch:~$ netq del events-config events_config_id eventsconfig_10
Successfully deleted Events Config eventsconfig_10
```
{{</tab>}}

{{</tabs>}}
### Show Event Suppression Rules

{{<tabs "TabID1804" >}}

{{<tab "NetQ UI" >}}

To view suppressed events:

1. Click {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/03-Menu/navigation-menu.svg" height="18" width="18">}} **Menu**, then **Events**.

2. Select **Show suppression rules** at the top of the page.

3. Toggle between the **Single** and **All** tabs to view individual and groups of rules, respectively. 

{{</tab>}}

{{<tab "NetQ CLI" >}}

You can view all event suppression configurations, or you can filter by a specific configuration or message type using the {{<link title="show/#netq show events-config" text="netq show events-config">}} command.

```
nvidia@switch:~$ netq show events-config events_config_id eventsconfig_1
Matching config_events records:
Events Config ID     Events Config Name   Message Type         Scope                                                        Active Suppress Until
-------------------- -------------------- -------------------- ------------------------------------------------------------ ------ --------------------
eventsconfig_1       job_cl_upgrade_2d89c agent                {"db_state":"*","hostname":"spine02","severity":"*"}         True   Tue Jul  7 16:16:20
                     21b3effd79796e585c35                                                                                          2025
                     096d5fc6cef32b463e37
                     cca88d8ee862ae104d5_
                     spine02
eventsconfig_1       job_cl_upgrade_2d89c bgp                  {"vrf":"*","peer":"*","hostname":"spine04","severity":"*"}   True   Tue Jul  7 16:16:20
                     21b3effd79796e585c35                                                                                          2025
                     096d5fc6cef32b463e37
                     cca88d8ee862ae104d5_
                     spine04
eventsconfig_1       job_cl_upgrade_2d89c btrfsinfo            {"hostname":"spine04","info":"*","severity":"*"}             True   Tue Jul  7 16:16:20
                     21b3effd79796e585c35                                                                                          2025
                     096d5fc6cef32b463e37
                     cca88d8ee862ae104d5_
                     spine04
eventsconfig_1       job_cl_upgrade_2d89c clag                 {"hostname":"spine04","severity":"*"}                        True   Tue Jul  7 16:16:20
                     21b3effd79796e585c35                                                                                          2025
                     096d5fc6cef32b463e37
                     cca88d8ee862ae104d5_
                     spine04
eventsconfig_1       job_cl_upgrade_2d89c clsupport            {"fileAbsName":"*","hostname":"spine04","severity":"*"}      True   Tue Jul  7 16:16:20
                     21b3effd79796e585c35                                                                                          2025
                     096d5fc6cef32b463e37
                     cca88d8ee862ae104d5_
                     spine04
...
```

When you filter for a message type, you must include the `show-filter-conditions` keyword to show the conditions associated with that message type and the hierarchy in which they get processed.

```
nvidia@switch:~$ netq show events-config message_type evpn show-filter-conditions
Matching config_events records:
Message Name             Filter Condition Name                      Filter Condition Hierarchy                           Filter Condition Description
------------------------ ------------------------------------------ ---------------------------------------------------- --------------------------------------------------------
evpn                     vni                                        3                                                    Target VNI
evpn                     severity                                   2                                                    Severity error/info
evpn                     hostname                                   1                                                    Target Hostname
```
{{</tab>}}

{{</tabs>}}