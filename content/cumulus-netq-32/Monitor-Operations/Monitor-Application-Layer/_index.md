---
title: Monitor Application Layer Protocols
author: Cumulus Networks
weight: 995
toc: 3
---
The only application layer protocol monitored by NetQ is NTP, the Network Time Protocol.

It is important that the switches and hosts remain in time synchronization with the NetQ appliance or Virtual Machine to ensure collected data is properly captured and processed. You can use the `netq show ntp` command to view the time synchronization status for all devices or filter for devices that are either in synchronization or out of synchronization, currently or at a time in the past.

The syntax for the show commands is:

```
netq [<hostname>] show ntp [out-of-sync|in-sync] [around <text-time>] [json]
netq [<hostname>] show events [level info|level error|level warning|level critical|level debug] type ntp [between <text-time> and <text-endtime>] [json]
```

## View Current Time Synchronization Status

You can view the current status of all devices with respect to their time synchronization with a given NTP server, stratum, and application.

This example shows the time synchronization status for all devices in the Cumulus Networks reference architecture. You can see that all border, leaf, and spine switches rely on the out-of-band management server running *ntpq* to provide their time and that they are all in time synchronization. The out-of-band management server uses the *titan.crash-ove* server running *ntpq* to obtain and maintain time synchronization. And the NetQ server uses the *eterna.binary.net* server running *chronyc* to obtain and maintain time synchronization. The firewall switches are not time synchronized, which is appropriate. The *Stratum* value indicates the number of hierarchical levels the switch or host is from reference clock.

```
cumulus@switch:~$ netq show ntp
Matching ntp records:
Hostname          NTP Sync Current Server    Stratum NTP App
----------------- -------- ----------------- ------- ---------------------
border01          yes      oob-mgmt-server   3       ntpq
border02          yes      oob-mgmt-server   3       ntpq
fw1               no       -                 16      ntpq
fw2               no       -                 16      ntpq
leaf01            yes      oob-mgmt-server   3       ntpq
leaf02            yes      oob-mgmt-server   3       ntpq
leaf03            yes      oob-mgmt-server   3       ntpq
leaf04            yes      oob-mgmt-server   3       ntpq
netq-ts           yes      eterna.binary.net 2       chronyc
oob-mgmt-server   yes      titan.crash-ove   2       ntpq
server01          yes      oob-mgmt-server   3       ntpq
server02          yes      oob-mgmt-server   3       ntpq
server03          yes      oob-mgmt-server   3       ntpq
server04          yes      oob-mgmt-server   3       ntpq
server05          yes      oob-mgmt-server   3       ntpq
server06          yes      oob-mgmt-server   3       ntpq
server07          yes      oob-mgmt-server   3       ntpq
server08          yes      oob-mgmt-server   3       ntpq
spine01           yes      oob-mgmt-server   3       ntpq
spine02           yes      oob-mgmt-server   3       ntpq
spine03           yes      oob-mgmt-server   3       ntpq
spine04           yes      oob-mgmt-server   3       ntpq
```

## View Devices that are Out of Time Synchronization

When a device is out of time synchronization with the NetQ server, the collected data may be improperly processed. For example, the wrong timestamp could be applied to a piece of data, or that data might be included in an aggregated metric when is should have been included in the next bucket of the aggregated metric. This would make the presented data be slightly off or give an incorrect impression.

This example shows all devices in the network that are out of time synchronization, and consequently need to be investigated.

```
cumulus@switch:~$ netq show ntp out-of-sync
Matching ntp records:
Hostname          NTP Sync Current Server    Stratum NTP App
----------------- -------- ----------------- ------- ---------------------
internet          no       -                 16      ntpq
```

## View Time Synchronization for a Given Device

You may only be concerned with the behavior of a particular device. Checking for time synchronization is a common troubleshooting step to take.

This example shows the time synchronization status for the *leaf01* switch.

```
cumulus@switch:~$ netq leaf01 show ntp
Matching ntp records:
Hostname          NTP Sync Current Server    Stratum NTP App
----------------- -------- ----------------- ------- ---------------------
leaf01            yes      kilimanjaro       2       ntpq
```

## View NTP Status for a Time in the Past

If you find a device that is out of time synchronization, you can use the `around` option to get an idea when the synchronization was broken.

This example shows the time synchronization status for all devices one week ago. Note that there are no errant devices in this example. You might try looking at the data for a few days ago. If there was an errant device a week ago, you might try looking farther back in time.

```
cumulus@switch:~$ netq show ntp 7d
Matching ntp records:
Hostname          NTP Sync Current Server    Stratum NTP App
----------------- -------- ----------------- ------- ---------------------
border01          yes      oob-mgmt-server   3       ntpq
border02          yes      oob-mgmt-server   3       ntpq
fw1               no       -                 16      ntpq
fw2               no       -                 16      ntpq
leaf01            yes      oob-mgmt-server   3       ntpq
leaf02            yes      oob-mgmt-server   3       ntpq
leaf03            yes      oob-mgmt-server   3       ntpq
leaf04            yes      oob-mgmt-server   3       ntpq
netq-ts           yes      eterna.binary.net 2       chronyc
oob-mgmt-server   yes      titan.crash-ove   2       ntpq
server01          yes      oob-mgmt-server   3       ntpq
server02          yes      oob-mgmt-server   3       ntpq
server03          yes      oob-mgmt-server   3       ntpq
server04          yes      oob-mgmt-server   3       ntpq
server05          yes      oob-mgmt-server   3       ntpq
server06          yes      oob-mgmt-server   3       ntpq
server07          yes      oob-mgmt-server   3       ntpq
server08          yes      oob-mgmt-server   3       ntpq
spine01           yes      oob-mgmt-server   3       ntpq
spine02           yes      oob-mgmt-server   3       ntpq
spine03           yes      oob-mgmt-server   3       ntpq
spine04           yes      oob-mgmt-server   3       ntpq
```

## View NTP Events

If a device has difficulty remaining in time synchronization, you might want to look to see if there are any related events.

This example shows there have been no events in the last 24 hours.

```
cumulus@switch:~$ netq show events type ntp
No matching event records found
```

This example shows there have been no critical NTP events in the last seven days.

```
cumulus@switch:~$ netq show events type ntp between now and 7d
No matching event records found
```
