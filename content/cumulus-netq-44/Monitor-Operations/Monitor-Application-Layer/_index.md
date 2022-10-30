---
title: Application Layer Protocols
author: NVIDIA
weight: 995
toc: 3
---
The only application layer protocol monitored by NetQ is NTP, the Network Time Protocol.

You can use the `netq show ntp` command to view the time synchronization status for all devices or filter for devices that are either in synchronization or out of synchronization, currently or at a time in the past.

The syntax for the `show` commands is:

```
netq [<hostname>] show ntp [out-of-sync|in-sync] [around <text-time>] [json]
netq [<hostname>] show events [severity info | severity error ] message_type ntp [between <text-time> and <text-endtime>] [json]
```

## View Current Time Synchronization Status

You can view the current status of all devices regarding their time synchronization with a given NTP server, stratum, and application.

{{<expand "show ntp">}}

The following example shows the time synchronization status for all devices in the NVIDIA reference architecture. 

All border, leaf, and spine switches rely on the out-of-band management server running *ntpq* to provide their time; they are all synchronized. The out-of-band management server uses the *titan.crash-ove* server running *ntpq* to obtain and maintain time synchronization. Meanwhile, the NetQ server uses the *eterna.binary.net* server running *chronyc* to obtain and maintain time synchronization. The firewall switches are not time synchronized (which is expected). The *Stratum* value indicates the number of hierarchical levels the switch or host is from the reference clock.

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
{{</expand>}}
## View Devices that are Out of Time Synchronization

When a device is out of time synchronization with the NetQ server, the collected data might be improperly processed. For example, the incorrect timestamp could be applied to a piece of data, or that data might be included in an aggregated metric when it should have been included in the next bucket of the aggregated metric. This could make the presented data slightly off or give an incorrect impression.

{{<expand "show ntp out-of-sync">}}

The following example shows all devices in the network that are out of time synchronization, and therefore need further investigation:

```
cumulus@switch:~$ netq show ntp out-of-sync
Matching ntp records:
Hostname          NTP Sync Current Server    Stratum NTP App
----------------- -------- ----------------- ------- ---------------------
internet          no       -                 16      ntpq
```
{{</expand>}}
## View Time Synchronization for a Given Device

Include the hostname to view NTP status for a particular device.

{{<expand "leaf01 show ntp">}}

The following example shows the time synchronization status for the leaf01 switch:

```
cumulus@switch:~$ netq leaf01 show ntp
Matching ntp records:
Hostname          NTP Sync Current Server    Stratum NTP App
----------------- -------- ----------------- ------- ---------------------
leaf01            yes      kilimanjaro       2       ntpq
```
{{</expand>}}
## View NTP Status for a Time in the Past

If you find a device that is out of time synchronization, you can use the `around` option to get an idea when the synchronization broke.

{{<expand "show ntp 7d">}}

The following example shows the time synchronization status for all devices one week ago; all devices are synchronized as expected.

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
{{</expand>}}
## View NTP Events

If a device has difficulty remaining in time synchronization, you might want to look to see if there are any related events.

{{<expand "show events type ntp">}}

The following example displays no events in the last 24 hours:

```
cumulus@switch:~$ netq show events message_type ntp
No matching event records found
```
{{</expand>}}
{{<expand "show events type ntp between now and 7d">}}

The following example shows no error NTP events in the last seven days:

```
cumulus@switch:~$ netq show events message_type ntp between now and 7d
No matching event records found

```
{{</expand>}}