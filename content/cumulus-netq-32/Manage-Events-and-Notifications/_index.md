---
title: Manage Events and Notifications
author: Cumulus Networks
weight: 660
toc: 3
---
Events provide information about how the network and its devices are operating. NetQ allows you to view current events and compare that with events at an earlier time. Event notifications are available through Slack, PagerDuty, syslog, and Email channels and aid troubleshooting and resolution of problems in the network before they become critical.

The NetQ UI provides two event workflows and a summary list of all system events. The Alarms card workflow tracks critical severity events, whereas the Info card workflow tracks all warning, info, and debug severity events. These cards allow you to view events for a time in the past. The All Events table lists all events in the last 24 hours.

The NetQ CLI provides the `netq show events` command to view events from network protocols and services, license, sensors and more. The command allow you to filter by severity and view events from a time frame in the past.

NetQ also provides What Just Happened (WJH) event information from Mellanox switches through the NetQ UI and NetQ CLI.

To take advantage of these events, use the instructions contained in this topic to configure one or more notification channels for system and threshold-based events and setup WJH for selected switches.

<!-- monitor system events
monitor tca events
monitor wjh -->