---
title: Monitor Events
author: NVIDIA
weight: 800
toc: 4
---
NetQ offers multiple ways to view your event status. The NetQ UI provides a graphical and tabular view and the NetQ CLI provides a tabular view of system and threshold-based (TCA) events. System events include events associated with network protocols and services operation, hardware and software status, and system services. TCA events include events associated with digital optics, ACL and forwarding resources, interface statistics, resource utilization, and sensors. You can view all events across the entire network or all events on a device. For each of these, you can filter your view of events based on event type, severity, and timeframe.

Refer to {{<link title="Configure System Event Notifications">}} and {{<link title="Configure Threshold-Based Event Notifications">}} for information about configuring and managing these events.

## Monitor All System and TCA Events Networkwide

You can monitor all system and TCA events across the network with the NetQ UI and the NetQ CLI.

{{<tabs "TabID29" >}}

{{<tab "NetQ UI" >}}

1. Click {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/03-Menu/navigation-menu.svg" height="18" width="18">}} (main menu).

2. In the side navigation under **Network**, click **Events**.

    The dashboard presents a timeline of events alongside the devices that are causing the most events. You can filter events by type, including interface, network services, system, and threshold crossing events. The filter controls are located at the top of the screen.

    {{<figure src="/images/netq/events-card-l4-42.png" width="700" alt="Events dashboard with networkwide error and info events.">}}

  If you are receiving too many event notifications, you can acknowledge events or create rules to suppress events from the dashboard. Refer to {{<link title="Configure System Event Notifications#suppress-events" text="Configure System Event Notifications">}} for information about event suppression.

  Events are also generated when streaming {{<link title="Validate Overall Network Health" text="validation checks">}} detect a failure. If an event is generated from a failed validation check, it will be marked resolved automatically the next time the check runs successfully.


{{</tab>}}

{{<tab "NetQ CLI" >}}

To view all system and all TCA events, run:

```
netq show events [between <text-time> and <text-endtime>] [json]
```

This example shows all system and TCA events between now and an hour ago.

```
netq show events
cumulus@switch:~$ netq show events
Matching events records:
Hostname          Message Type             Severity         Message                             Timestamp
----------------- ------------------------ ---------------- ----------------------------------- -------------------------
leaf01            btrfsinfo                error            data storage efficiency : space lef Wed Sep  2 20:04:30 2020
                                                            t after allocation greater than chu
                                                            nk size 0.57 GB
leaf02            btrfsinfo                error            data storage efficiency : space lef Wed Sep  2 19:55:26 2020
                                                            t after allocation greater than chu
                                                            nk size 0.57 GB
leaf01            btrfsinfo                error            data storage efficiency : space lef Wed Sep  2 19:34:29 2020
                                                            t after allocation greater than chu
                                                            nk size 0.57 GB
leaf02            btrfsinfo                error            data storage efficiency : space lef Wed Sep  2 19:25:24 2020
                                                            t after allocation greater than chu
                                                            nk size 0.57 GB
```

This example shows all events between now and 24 hours ago.

```
netq show events between now and 24hr
cumulus@switch:~$ netq show events between now and 24hr
Matching events records:
Hostname          Message Type             Severity         Message                             Timestamp
----------------- ------------------------ ---------------- ----------------------------------- -------------------------
leaf01            btrfsinfo                error            data storage efficiency : space lef Wed Sep  2 20:04:30 2020
                                                            t after allocation greater than chu
                                                            nk size 0.57 GB
leaf02            btrfsinfo                error            data storage efficiency : space lef Wed Sep  2 19:55:26 2020
                                                            t after allocation greater than chu
                                                            nk size 0.57 GB
leaf01            btrfsinfo                error            data storage efficiency : space lef Wed Sep  2 19:34:29 2020
                                                            t after allocation greater than chu
                                                            nk size 0.57 GB
leaf02            btrfsinfo                error            data storage efficiency : space lef Wed Sep  2 19:25:24 2020
                                                            t after allocation greater than chu
                                                            nk size 0.57 GB
leaf01            btrfsinfo                error            data storage efficiency : space lef Wed Sep  2 19:04:22 2020
                                                            t after allocation greater than chu
                                                            nk size 0.57 GB
leaf02            btrfsinfo                error            data storage efficiency : space lef Wed Sep  2 18:55:17 2020
                                                            t after allocation greater than chu
                                                            nk size 0.57 GB
leaf01            btrfsinfo                error            data storage efficiency : space lef Wed Sep  2 18:34:21 2020
                                                            t after allocation greater than chu
                                                            nk size 0.57 GB
leaf02            btrfsinfo                error            data storage efficiency : space lef Wed Sep  2 18:25:16 2020
                                                            t after allocation greater than chu
                                                            nk size 0.57 GB
leaf01            btrfsinfo                error            data storage efficiency : space lef Wed Sep  2 18:04:19 2020
                                                            t after allocation greater than chu
                                                            nk size 0.57 GB
leaf02            btrfsinfo                error            data storage efficiency : space lef Wed Sep  2 17:55:15 2020
                                                            t after allocation greater than chu
                                                            nk size 0.57 GB
leaf01            btrfsinfo                error            data storage efficiency : space lef Wed Sep  2 17:34:18 2020
                                                            t after allocation greater than chu
                                                            nk size 0.57 GB
...
```

{{</tab>}}

{{</tabs>}}

## Monitor All System and TCA Events on a Device

You can monitor all system and TCA events on a given device with the NetQ UI and the NetQ CLI.

{{<tabs "TabID126" >}}

{{<tab "NetQ UI" >}}

1. Click {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/03-Menu/navigation-menu.svg" height="18" width="18">}} (main menu).

2. In the side navigation under **Network**, click **Events**.

3. At the top of the screen, click the **Hostname** field and select a device.

4. Click **Apply**.

{{</tab>}}

{{<tab "NetQ CLI" >}}

To view all system and TCA events on a switch, run:

```
netq <hostname> show events [between <text-time> and <text-endtime>] [json]
```

This example shows all system and TCA events that have occurred on the *leaf01* switch between now and an hour ago.

```
cumulus@switch:~$ netq leaf01 show events

Matching events records:
Hostname          Message Type             Severity         Message                             Timestamp
----------------- ------------------------ ---------------- ----------------------------------- -------------------------
leaf01            btrfsinfo                error            data storage efficiency : space lef Wed Sep  2 20:34:31 2020
                                                            t after allocation greater than chu
                                                            nk size 0.57 GB
leaf01            btrfsinfo                error            data storage efficiency : space lef Wed Sep  2 20:04:30 2020
                                                            t after allocation greater than chu
                                                            nk size 0.57 GB
```

This example shows that no events have occurred on the spine01 switch in the last hour.

```
cumulus@switch:~$ netq spine01 show events
No matching event records found
```

{{</tab>}}

{{</tabs>}}

## Monitor System and TCA Events Networkwide by Type

You can view all system  and TCA events of a given type on a networkwide basis using the NetQ UI and the NetQ CLI.

{{<tabs "TabID187" >}}

{{<tab "NetQ UI" >}}

1. Click {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/03-Menu/navigation-menu.svg" height="18" width="18">}} (main menu).

2. In the side navigation under **Network**, click **Events**.

3. At the top of the screen, click the **Type** field and select a network protocol or service.

4. Click **Apply**.

{{</tab>}}

{{<tab "NetQ CLI" >}}

To view all system events for a given network protocol or service, run:

```
netq show events (type agents|bgp|btrfsinfo|clag|clsupport|configdiff|evpn|interfaces|interfaces-physical|lcm|lldp|macs|mtu|ntp|os|ospf|roceconfig|sensors|services|tca_roce|trace|vlan|vxlan) [between <text-time> and <text-endtime>] [json]
```

This example shows all services events between now and 30 days ago.

```
cumulus@switch:~$ netq show events type services between now and 30d
Matching events records:
Hostname          Message Type             Severity         Message                             Timestamp
----------------- ------------------------ ---------------- ----------------------------------- -------------------------
spine03           services                 error            Service netqd status changed from a Mon Aug 10 19:55:52 2020
                                                            ctive to inactive
spine04           services                 error            Service netqd status changed from a Mon Aug 10 19:55:51 2020
                                                            ctive to inactive
spine02           services                 error            Service netqd status changed from a Mon Aug 10 19:55:50 2020
                                                            ctive to inactive
spine03           services                 info             Service netqd status changed from i Mon Aug 10 19:55:38 2020
                                                            nactive to active
spine04           services                 info             Service netqd status changed from i Mon Aug 10 19:55:37 2020
                                                            nactive to active
spine02           services                 info             Service netqd status changed from i Mon Aug 10 19:55:35 2020

```

{{<notice tip>}}
You can enter a severity using the <code>level</code> option to further narrow the output.
{{</notice>}}

{{</tab>}}

{{</tabs>}}

## Monitor System and TCA Events on a Device by Type

You can view all system and TCA events of a given type on a given device using the NetQ UI and the NetQ CLI.

{{<tabs "TabID250" >}}

{{<tab "NetQ UI" >}}

1. Click {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/03-Menu/navigation-menu.svg" height="18" width="18">}} (main menu).

2. In the side navigation under **Network**, click **Events**.

3. At the top of the screen, click the **Hostname** field and select a device.

4. In the same row, click the **Type** field and select a network protocol or service.

5. Click **Apply**.

{{</tab>}}

{{<tab "NetQ CLI" >}}

To view all system events for a given network protocol or service, run:

```
netq <hostname> show events (type agents|bgp|btrfsinfo|clag|clsupport|configdiff|evpn|interfaces|interfaces-physical|lcm|lldp|macs|mtu|ntp|os|ospf|roceconfig|sensors|services|tca_roce|trace|vlan|vxlan) [between <text-time> and <text-endtime>] [json]
```


This example shows all *services* events on the *spine03* switch between now and 30 days ago.

```
cumulus@switch:~$ netq spine03 show events type services between now and 30d
Matching events records:
Hostname          Message Type             Severity         Message                             Timestamp
----------------- ------------------------ ---------------- ----------------------------------- -------------------------
spine03           services                 error            Service netqd status changed from a Mon Aug 10 19:55:52 2020
                                                            ctive to inactive
spine03           services                 info             Service netqd status changed from i Mon Aug 10 19:55:38 2020
                                                            nactive to active
```

{{<notice tip>}}
You can enter a severity using the <code>level</code> option to further narrow the output.
{{</notice>}}

{{</tab>}}

{{</tabs>}}

## Monitor System and TCA Events Networkwide by Severity

You can view system and TCA events by their severity on a networkwide basis with the NetQ UI and the NetQ CLI.

{{<notice tip>}}
System event severities include info, error, warning, or debug. TCA event severities include info or error.
{{</notice>}}

{{<tabs "TabID312" >}}

{{<tab "NetQ UI" >}}

1. Click {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/03-Menu/navigation-menu.svg" height="18" width="18">}} (main menu).

2. In the side navigation under **Network**, click **Events**.

3. At the top of the screen, click the **Severity** field and select a level.

4. Click **Apply**.

{{</tab>}}

{{<tab "NetQ CLI" >}}

To view all system events of a given severity, run:

```
netq show events (level info | level error | level warning | level debug) [between <text-time> and <text-endtime>] [json]
```

This example shows all events with error severity between now and 24 hours ago.

```
cumulus@switch:~$ netq show events level error
Matching events records:
Hostname          Message Type             Severity         Message                             Timestamp
----------------- ------------------------ ---------------- ----------------------------------- -------------------------
Matching events records:
Hostname          Message Type             Severity         Message                             Timestamp
----------------- ------------------------ ---------------- ----------------------------------- -------------------------
leaf02            btrfsinfo                error         data storage efficiency : space lef Tue Sep  8 21:32:32 2020
                                                            t after allocation greater than chu
                                                            nk size 0.57 GB
leaf01            btrfsinfo                error         data storage efficiency : space lef Tue Sep  8 21:13:28 2020
                                                            t after allocation greater than chu
                                                            nk size 0.57 GB
leaf02            btrfsinfo                error         data storage efficiency : space lef Tue Sep  8 21:02:31 2020
                                                            t after allocation greater than chu
                                                            nk size 0.57 GB
leaf01            btrfsinfo                error         data storage efficiency : space lef Tue Sep  8 20:43:27 2020
                                                            t after allocation greater than chu
                                                            nk size 0.57 GB
```

{{<notice tip>}}
You can use the <code>type</code> and <code>between</code> options to further narrow the output.
{{</notice>}}

{{</tab>}}

{{</tabs>}}

## Monitor System and TCA Events on a Device by Severity

You can view system and TCA events by their severity on a given device with the NetQ UI and the NetQ CLI.

{{<tabs "TabID545" >}}

{{<tab "NetQ UI" >}}

1. Click {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/03-Menu/navigation-menu.svg" height="18" width="18">}} (main menu).

2. In the side navigation under **Network**, click **Events**.

3. At the top of the screen, click the **Hostname** field and select a device.

4. In the same row, click the **Severity** field and select a level.

5. Click **Apply**.

{{</tab>}}

{{<tab "NetQ CLI" >}}

To view all system events for a given severity on a device, run:

```
netq <hostname> show events (level info | level error | level warning | level debug)  [between <text-time> and <text-endtime>] [json]
```

This example shows all *error* severity events on the *leaf01* switch between now and 24 hours ago.

```
cumulus@switch:~$ netq leaf01 show events level error
Matching events records:
Hostname          Message Type             Severity         Message                             Timestamp
----------------- ------------------------ ---------------- ----------------------------------- -------------------------
leaf01            btrfsinfo                error            data storage efficiency : space lef Wed Sep  9 18:44:49 2020
                                                            t after allocation greater than chu
                                                            nk size 0.57 GB
leaf01            btrfsinfo                error            data storage efficiency : space lef Wed Sep  9 18:14:48 2020
                                                            t after allocation greater than chu
                                                            nk size 0.57 GB

```

{{<notice tip>}}
You can use the <code>type</code> or <code>between</code> options to further narrow the output.
{{</notice>}}

{{</tab>}}

{{</tabs>}}

## Monitor System and TCA Events Networkwide by Time

You can monitor all system and TCA events across the network currently or for a time in the past with the NetQ UI and the NetQ CLI.

{{<tabs "TabID706" >}}

{{<tab "NetQ UI" >}}

1. Click {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/03-Menu/navigation-menu.svg" height="18" width="18">}} (main menu).

2. In the side navigation under **Network**, click **Events**.

3. At the top of the screen, use the first two fields to filter either over a time range or by recent events. 

4. Click **Apply**.

{{</tab>}}
{{<tab "NetQ CLI" >}}

The NetQ CLI uses a default of one hour unless otherwise specified. To view all system and all TCA events for a time beyond an hour in the past, run:

```
netq show events [between <text-time> and <text-endtime>] [json]
```

This example shows all system and TCA events between now and 24 hours ago.

```
netq show events between now and 24hr
cumulus@switch:~$ netq show events between now and 24hr
Matching events records:
Hostname          Message Type             Severity         Message                             Timestamp
----------------- ------------------------ ---------------- ----------------------------------- -------------------------
leaf01            btrfsinfo                error            data storage efficiency : space lef Wed Sep  2 20:04:30 2020
                                                            t after allocation greater than chu
                                                            nk size 0.57 GB
leaf02            btrfsinfo                error            data storage efficiency : space lef Wed Sep  2 19:55:26 2020
                                                            t after allocation greater than chu
                                                            nk size 0.57 GB
leaf01            btrfsinfo                error            data storage efficiency : space lef Wed Sep  2 19:34:29 2020
                                                            t after allocation greater than chu
                                                            nk size 0.57 GB
leaf02            btrfsinfo                error            data storage efficiency : space lef Wed Sep  2 19:25:24 2020
                                                            t after allocation greater than chu
                                                            nk size 0.57 GB
leaf01            btrfsinfo                error            data storage efficiency : space lef Wed Sep  2 19:04:22 2020
                                                            t after allocation greater than chu
                                                            nk size 0.57 GB
leaf02            btrfsinfo                error            data storage efficiency : space lef Wed Sep  2 18:55:17 2020
                                                            t after allocation greater than chu
                                                            nk size 0.57 GB
leaf01            btrfsinfo                error            data storage efficiency : space lef Wed Sep  2 18:34:21 2020
                                                            t after allocation greater than chu
                                                            nk size 0.57 GB
leaf02            btrfsinfo                error            data storage efficiency : space lef Wed Sep  2 18:25:16 2020
                                                            t after allocation greater than chu
                                                            nk size 0.57 GB
leaf01            btrfsinfo                error            data storage efficiency : space lef Wed Sep  2 18:04:19 2020
                                                            t after allocation greater than chu
                                                            nk size 0.57 GB
leaf02            btrfsinfo                error            data storage efficiency : space lef Wed Sep  2 17:55:15 2020
                                                            t after allocation greater than chu
                                                            nk size 0.57 GB
leaf01            btrfsinfo                error            data storage efficiency : space lef Wed Sep  2 17:34:18 2020
                                                            t after allocation greater than chu
                                                            nk size 0.57 GB
...
```

This example shows all system and TCA events between one and three days ago.

```
cumulus@switch:~$ netq show events between 1d and 3d

Matching events records:
Hostname          Message Type             Severity         Message                             Timestamp
----------------- ------------------------ ---------------- ----------------------------------- -------------------------
leaf01            btrfsinfo                error            data storage efficiency : space lef Wed Sep  9 16:14:37 2020
                                                            t after allocation greater than chu
                                                            nk size 0.57 GB
leaf02            btrfsinfo                error            data storage efficiency : space lef Wed Sep  9 16:03:31 2020
                                                            t after allocation greater than chu
                                                            nk size 0.57 GB
leaf01            btrfsinfo                error            data storage efficiency : space lef Wed Sep  9 15:44:36 2020
                                                            t after allocation greater than chu
                                                            nk size 0.57 GB
leaf02            btrfsinfo                error            data storage efficiency : space lef Wed Sep  9 15:33:30 2020
                                                            t after allocation greater than chu
                                                            nk size 0.57 GB
leaf01            btrfsinfo                error            data storage efficiency : space lef Wed Sep  9 15:14:35 2020
                                                            t after allocation greater than chu
                                                            nk size 0.57 GB
leaf02            btrfsinfo                error            data storage efficiency : space lef Wed Sep  9 15:03:28 2020
                                                            t after allocation greater than chu
                                                            nk size 0.57 GB
leaf01            btrfsinfo                error            data storage efficiency : space lef Wed Sep  9 14:44:34 2020
                                                            t after allocation greater than chu
                                                            nk size 0.57 GB
leaf02            btrfsinfo                error            data storage efficiency : space lef Wed Sep  9 14:33:21 2020
                                                            t after allocation greater than chu
                                                            nk size 0.57 GB
...
```

{{</tab>}}

{{</tabs>}}
