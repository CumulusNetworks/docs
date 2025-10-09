---
title: Monitor Events
author: NVIDIA
weight: 775
toc: 4
---
Use the UI or CLI to monitor events: you can view all events across the entire network or all events on a device, then filter events according to their type, severity, or time frame. Event querying is supported for a 72-hour window within the past 30 days.

Note that in the UI, it can take several minutes for NetQ to process and accurately display network events. The delay is caused by events with multiple network dependencies. It takes between 5 and 10 minutes for NetQ to consolidate and display these events.

Refer to {{<link title="Configure System Event Notifications">}} and {{<link title="Configure and Monitor Threshold-Crossing Events">}} for information about configuring third-party applications to broadcast NetQ events.
## Event Commands

Monitor events with the following command. See the {{<link title="show/#netq-show-events" text="command line reference">}} for additional options, definitions, and examples.

```
netq show events
```

## Monitor Events in the UI

Expand the {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/03-Menu/navigation-menu.svg" height="18" width="18">}} **Menu**, then select **Events**.

The dashboard presents a timeline of events alongside the devices that are causing the most events. 

  {{<figure src="/images/netq/events-full-460.png" width="1200" alt="Events dashboard with networkwide error and info events.">}}

Use the controls above the summary to filter events by time, device (hostname), type, severity, or state.

  {{<figure src="/images/netq/event-controls-460.png" width="500" alt="">}}

Select the tabs below the controls to display all events networkwide, interface events, network services events, system events, or threshold-crossing events. The charts and tables update according to the tab you've selected. In this example, the TCA tab is selected; the chart and tables update to reflect only threshold-crossing events:

  {{<figure src="/images/netq/tca-events-full-460.png" width="1200" alt="Events dashboard with networkwide error and info events.">}}

Events are also generated when streaming {{<link title="Validate Overall Network Health" text="validation checks">}} detect a failure. If an event is generated from a failed validation check, it will be marked resolved automatically the next time the check runs successfully.

  ## Suppress Events

 If you are receiving too many event notifications, you can create rules to suppress events. You can also create rules to suppress events attributable to known issues or false alarms. In addition to the rules you create to suppress events, NetQ suppresses some events by default. 

You can suppress events for the following types of messages:

- agent: NetQ Agent events
- bgp: BGP events
- btrfsinfo: Events related to the BTRFS file system in Cumulus Linux
- clsupport: Events generated when creating the `cl-support script`
- configdiff: Events generated when a configuration file has changed
- evpn: EVPN events
- lcm: Lifecycle management events
- license: Software license events
- link: Events related to links, including state and interface name
- lldp: LLDP events
- mlag: MLAG events
- ntp: NTP events
- ospf: OSPF events
- packageinfo:
- ptm: Prescriptive Topology Manager events
- ptp: PTP events
- roceconfig: RoCE configuration events
- runningconfigdiff: Events related to the difference between two configurations
- sensor: Sensor events
- services: Service-related events, including whether a service is active or inactive
- ssdutil: Events related to the storage on a switch

{{<notice info>}} 

NetQ suppresses BGP, EVPN, link, and sensor-related events with a severity level of 'info' by default in the UI. You can {{<link url="#delete-or-disable-an-event-suppression-rule" text="disable this rule">}} if you'd prefer to receive these notifications.

{{</notice>}}

### Create an Event Suppression Configuration

{{<tabs "TabID1689" >}}

{{<tab "NetQ UI" >}}

To suppress events using the NetQ UI:

1. Click {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/03-Menu/navigation-menu.svg" height="18" width="18">}} **Menu**, then **Events**.
2. In the top-right corner, select **Show suppression rules**.
3. Select **Add rule**. You can configure individual suppression rules or you can create a group rule that suppresses events for all message types.
    {{<figure src="/images/netq/create-suppression-rule-modal.png" width="600">}}
4. Enter the suppression rule parameters and click **Create**.

{{</tab>}}

{{<tab "NetQ CLI" >}}

When you add a new configuration using the CLI, you can specify a scope, which limits the suppression in the following order:

1. Hostname.
2. Severity.
3. Message type-specific filters. For example, the target VNI for EVPN messages, or the interface name for a link message.

NetQ has a predefined set of filter conditions. To see these conditions, run `netq show events-config show-filter-conditions`:

```
cumulus@switch:~$ netq show events-config show-filter-conditions
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

For example, to create a configuration called `mybtrfs` that suppresses OSPF-related events on leaf01 for the next 10 minutes, run:

```
netq add events-config events_config_name mybtrfs message_type ospf scope '[{"scope_name":"hostname","scope_value":"leaf01"},{"scope_name":"severity","scope_value":"*"}]' suppress_until 600
```
{{</tab>}}

{{</tabs>}}
### Delete or Disable an Event Suppression Rule

You can delete or disable suppression rules. After you delete a rule, event notifications will resume. Disabling suppression rules pauses those rules, allowing you to receive event notifications temporarily. 

{{<tabs "TabID1776" >}}

{{<tab "NetQ UI" >}}

To remove suppressed event configurations:

1. Click {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/03-Menu/navigation-menu.svg" height="18" width="18">}} **Menu**, then **Events**.
2. Select **Show suppression rules** at the top of the page.
3. Toggle between the **Single** and **All** tabs to view the suppression rules. Navigate to the rule you want to delete or disable.
4. Click the three-dot menu and select **Delete**. To pause the rule instead of deleting it, click **Disable**.

{{</tab>}}

{{<tab "NetQ CLI" >}}

To remove an event suppression configuration, run `netq del events-config events_config_id <text-events-config-id-anchor>`.

```
cumulus@switch:~$ netq del events-config events_config_id eventsconfig_10
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
3. Toggle between the **Single** and **All** tabs to view individual and group rules, respectively. 

{{</tab>}}

{{<tab "NetQ CLI" >}}

You can view all event suppression configurations, or you can filter by a specific configuration or message type.

```
cumulus@switch:~$ netq show events-config events_config_id eventsconfig_1
Matching config_events records:
Events Config ID     Events Config Name   Message Type         Scope                                                        Active Suppress Until
-------------------- -------------------- -------------------- ------------------------------------------------------------ ------ --------------------
eventsconfig_1       job_cl_upgrade_2d89c agent                {"db_state":"*","hostname":"spine02","severity":"*"}         True   Tue Jul  7 16:16:20
                     21b3effd79796e585c35                                                                                          2020
                     096d5fc6cef32b463e37
                     cca88d8ee862ae104d5_
                     spine02
eventsconfig_1       job_cl_upgrade_2d89c bgp                  {"vrf":"*","peer":"*","hostname":"spine04","severity":"*"}   True   Tue Jul  7 16:16:20
                     21b3effd79796e585c35                                                                                          2020
                     096d5fc6cef32b463e37
                     cca88d8ee862ae104d5_
                     spine04
eventsconfig_1       job_cl_upgrade_2d89c btrfsinfo            {"hostname":"spine04","info":"*","severity":"*"}             True   Tue Jul  7 16:16:20
                     21b3effd79796e585c35                                                                                          2020
                     096d5fc6cef32b463e37
                     cca88d8ee862ae104d5_
                     spine04
eventsconfig_1       job_cl_upgrade_2d89c clag                 {"hostname":"spine04","severity":"*"}                        True   Tue Jul  7 16:16:20
                     21b3effd79796e585c35                                                                                          2020
                     096d5fc6cef32b463e37
                     cca88d8ee862ae104d5_
                     spine04
eventsconfig_1       job_cl_upgrade_2d89c clsupport            {"fileAbsName":"*","hostname":"spine04","severity":"*"}      True   Tue Jul  7 16:16:20
                     21b3effd79796e585c35                                                                                          2020
                     096d5fc6cef32b463e37
                     cca88d8ee862ae104d5_
                     spine04
eventsconfig_1       job_cl_upgrade_2d89c configdiff           {"new_state":"*","old_state":"*","type":"*","hostname":"spin True   Tue Jul  7 16:16:20
                     21b3effd79796e585c35                      e04","severity":"*"}                                                2020
                     096d5fc6cef32b463e37
                     cca88d8ee862ae104d5_
                     spine04
eventsconfig_1       job_cl_upgrade_2d89c evpn                 {"hostname":"spine04","vni":"*","severity":"*"}              True   Tue Jul  7 16:16:20
                     21b3effd79796e585c35                                                                                          2020
                     096d5fc6cef32b463e37
                     cca88d8ee862ae104d5_
                     spine04
eventsconfig_1       job_cl_upgrade_2d89c link                 {"ifname":"*","new_state":"*","hostname":"spine04","severity True   Tue Jul  7 16:16:20
                     21b3effd79796e585c35                      ":"*"}                                                              2020
                     096d5fc6cef32b463e37
                     cca88d8ee862ae104d5_
                     spine04
eventsconfig_1       job_cl_upgrade_2d89c ntp                  {"new_state":"*","hostname":"spine04","severity":"*"}        True   Tue Jul  7 16:16:20
                     21b3effd79796e585c35                                                                                          2020
                     096d5fc6cef32b463e37
                     cca88d8ee862ae104d5_
                     spine04
eventsconfig_1       job_cl_upgrade_2d89c ospf                 {"ifname":"*","hostname":"spine04","severity":"*"}           True   Tue Jul  7 16:16:20
                     21b3effd79796e585c35                                                                                          2020
                     096d5fc6cef32b463e37
                     cca88d8ee862ae104d5_
                     spine04
eventsconfig_1       job_cl_upgrade_2d89c sensor               {"sensor":"*","new_s_state":"*","hostname":"spine04","severi True   Tue Jul  7 16:16:20
                     21b3effd79796e585c35                      ty":"*"}                                                            2020
                     096d5fc6cef32b463e37
                     cca88d8ee862ae104d5_
                     spine04
eventsconfig_1       job_cl_upgrade_2d89c services             {"new_status":"*","name":"*","hostname":"spine04","severity" True   Tue Jul  7 16:16:20
                     21b3effd79796e585c35                      :"*"}                                                               2020
                     096d5fc6cef32b463e37
                     cca88d8ee862ae104d5_
                     spine04
eventsconfig_1       job_cl_upgrade_2d89c ssdutil              {"hostname":"spine04","info":"*","severity":"*"}             True   Tue Jul  7 16:16:20
                     21b3effd79796e585c35                                                                                          2020
                     096d5fc6cef32b463e37
                     cca88d8ee862ae104d5_
                     spine04
eventsconfig_10      job_cl_upgrade_2d89c btrfsinfo            {"hostname":"fw2","info":"*","severity":"*"}                 True   Tue Jul  7 16:16:22
                     21b3effd79796e585c35                                                                                          2020
                     096d5fc6cef32b463e37
                     cca88d8ee862ae104d5_
                     fw2
eventsconfig_10      job_cl_upgrade_2d89c clag                 {"hostname":"fw2","severity":"*"}                            True   Tue Jul  7 16:16:22
                     21b3effd79796e585c35                                                                                          2020
                     096d5fc6cef32b463e37
                     cca88d8ee862ae104d5_
                     fw2
eventsconfig_10      job_cl_upgrade_2d89c clsupport            {"fileAbsName":"*","hostname":"fw2","severity":"*"}          True   Tue Jul  7 16:16:22
                     21b3effd79796e585c35                                                                                          2020
                     096d5fc6cef32b463e37
                     cca88d8ee862ae104d5_
                     fw2
eventsconfig_10      job_cl_upgrade_2d89c link                 {"ifname":"*","new_state":"*","hostname":"fw2","severity":"* True   Tue Jul  7 16:16:22
                     21b3effd79796e585c35                      "}                                                                  2020
                     096d5fc6cef32b463e37
                     cca88d8ee862ae104d5_
                     fw2
eventsconfig_10      job_cl_upgrade_2d89c ospf                 {"ifname":"*","hostname":"fw2","severity":"*"}               True   Tue Jul  7 16:16:22
                     21b3effd79796e585c35                                                                                          2020
                     096d5fc6cef32b463e37
                     cca88d8ee862ae104d5_
                     fw2
eventsconfig_10      job_cl_upgrade_2d89c sensor               {"sensor":"*","new_s_state":"*","hostname":"fw2","severity": True   Tue Jul  7 16:16:22
                     21b3effd79796e585c35                      "*"}                                                                2020
                     096d5fc6cef32b463e37
                     cca88d8ee862ae104d5_
                     fw2
```

When you filter for a message type, you must include the `show-filter-conditions` keyword to show the conditions associated with that message type and the hierarchy in which they get processed.

```
cumulus@switch:~$ netq show events-config message_type evpn show-filter-conditions
Matching config_events records:
Message Name             Filter Condition Name                      Filter Condition Hierarchy                           Filter Condition Description
------------------------ ------------------------------------------ ---------------------------------------------------- --------------------------------------------------------
evpn                     vni                                        3                                                    Target VNI
evpn                     severity                                   2                                                    Severity error/info
evpn                     hostname                                   1                                                    Target Hostname
```
{{</tab>}}

{{</tabs>}}