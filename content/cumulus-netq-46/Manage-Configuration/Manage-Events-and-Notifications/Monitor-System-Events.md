---
title: Monitor Events
author: NVIDIA
weight: 800
toc: 4
---
You can monitor both system and threshold-crossing events with the UI or CLI. You can view all events across the entire network or all events on a device, then filter your view of events based on event type, severity, and timeframe.

Refer to {{<link title="Configure System Event Notifications">}} and {{<link title="Configure Threshold-Crossing Event Notifications">}} for information about configuring and managing these events.

Note that in the UI, it can take several minutes for NetQ to process and accurately display network events. The delay is caused by events with multiple network dependencies. It takes between 5 and 10 minutes for NetQ to consolidate and display these events.

## Monitor All System and TCA Events Networkwide

{{<tabs "TabID29" >}}

{{<tab "NetQ UI" >}}

1. Click {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/03-Menu/navigation-menu.svg" height="18" width="18">}} Menu.

2. In the side navigation under **Network**, click **Events**.

    The dashboard presents a timeline of events alongside the devices that are causing the most events. You can filter events by type, including interface, network services, system, and threshold crossing events. The filter controls are located at the top of the screen.

    {{<figure src="/images/netq/events-card-l4-42.png" width="1200" alt="Events dashboard with networkwide error and info events.">}}

 If you are receiving too many event notifications, you can create rules to suppress events. Select **Show suppression rules** in the top-right corner to view rules that prevent NetQ from displaying an event message. Refer to {{<link title="Configure System Event Notifications#suppress-events" text="Configure System Event Notifications">}} for information about event suppression.

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

{{<tabs "TabID126" >}}

{{<tab "NetQ UI" >}}

1. Click {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/03-Menu/navigation-menu.svg" height="18" width="18">}} Menu.

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

{{<tabs "TabID187" >}}

{{<tab "NetQ UI" >}}

1. Click {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/03-Menu/navigation-menu.svg" height="18" width="18">}} Menu.

2. In the side navigation under **Network**, click **Events**.

3. At the top of the screen, click the **Type** field and select a network protocol or service.

4. Click **Apply**.

{{</tab>}}

{{<tab "NetQ CLI" >}}

To view all system events for a given network protocol or service, run:

```
netq [<hostname>] show events [severity info | severity error ] [message_type link | message_type interfaces | message_type evpn | message_type bgp | message_type vxlan | message_type vlan | message_type ntp | message_type ospf | message_type lldp | message_type roceconfig | message_type mlag | message_type agent | message_type node | message_type mtu | message_type license | message_type sensor | message_type port | message_type configdiff  | message_type services | message_type clsupport | message_type runningconfigdiff | message_type resource | message_type btrfsinfo  | message_type ssdutil | message_type lcm | message_type ptm | message_type trace | message_type cable | message_type tca_resource | message_type tca_sensors | message_type tca_procdevstats | message_type tca_dom | message_type tca_link | message_type tca_ethtool | message_type tca_wjh | message_type tca_roce | message_type tca_bgp | message_type tca_ecmp ] [between <text-time> and <text-endtime>] [json]
```
{{</tab>}}

{{</tabs>}}

## Monitor System and TCA Events on a Device by Type

{{<tabs "TabID250" >}}

{{<tab "NetQ UI" >}}

1. Click {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/03-Menu/navigation-menu.svg" height="18" width="18">}} Menu.

2. In the side navigation under **Network**, click **Events**.

3. At the top of the screen, click the **Hostname** field and select a device.

4. In the same row, click the **Type** field and select a network protocol or service.

5. Click **Apply**.

{{</tab>}}

{{<tab "NetQ CLI" >}}

To view all system events for a given network protocol or service, run:

```
netq [<hostname>] show events [severity info | severity error ] [message_type link | message_type interfaces | message_type evpn | message_type bgp | message_type vxlan | message_type vlan | message_type ntp | message_type ospf | message_type lldp | message_type roceconfig | message_type mlag | message_type agent | message_type node | message_type mtu | message_type license | message_type sensor | message_type port | message_type configdiff  | message_type services | message_type clsupport | message_type runningconfigdiff | message_type resource | message_type btrfsinfo  | message_type ssdutil | message_type lcm | message_type ptm | message_type trace | message_type cable | message_type tca_resource | message_type tca_sensors | message_type tca_procdevstats | message_type tca_dom | message_type tca_link | message_type tca_ethtool | message_type tca_wjh | message_type tca_roce | message_type tca_bgp | message_type tca_ecmp ] [between <text-time> and <text-endtime>] [json]
```

{{</tab>}}

{{</tabs>}}

## Monitor System and TCA Events Networkwide by Severity

{{<notice tip>}}
System event severities include info, error, warning, or debug. TCA event severities include info or error.
{{</notice>}}

{{<tabs "TabID312" >}}

{{<tab "NetQ UI" >}}

1. Click {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/03-Menu/navigation-menu.svg" height="18" width="18">}} Menu.

2. In the side navigation under **Network**, click **Events**.

3. At the top of the screen, click the **Severity** field and select a level.

4. Click **Apply**.

{{</tab>}}

{{<tab "NetQ CLI" >}}

To view all system events of a given severity, run:

```
netq show events [severity info | severity error ] [between <text-time> and <text-endtime>] [json]
```

{{</tab>}}

{{</tabs>}}

## Monitor System and TCA Events on a Device by Severity

{{<tabs "TabID545" >}}

{{<tab "NetQ UI" >}}

1. Click {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/03-Menu/navigation-menu.svg" height="18" width="18">}} Menu.

2. In the side navigation under **Network**, click **Events**.

3. At the top of the screen, click the **Hostname** field and select a device.

4. In the same row, click the **Severity** field and select a level.

5. Click **Apply**.

{{</tab>}}

{{<tab "NetQ CLI" >}}

To view all system events for a given severity on a device, run:

```
netq <hostname> show events [severity info | severity error ]  [between <text-time> and <text-endtime>] [json]
```

{{</tab>}}

{{</tabs>}}

## Monitor System and TCA Events Networkwide by Time

{{<tabs "TabID706" >}}

{{<tab "NetQ UI" >}}

1. Click {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/03-Menu/navigation-menu.svg" height="18" width="18">}} Menu.

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
