---
title: CLI Early Access Features
author: Cumulus Networks
weight: 55
aliases:
 - /display/NETQ21/Early+Access+Features
 - /pages/viewpage.action?pageId=12321063
pageID: 12321063
product: Cumulus NetQ
version: 2.4
imgData: cumulus-netq
siteSlug: cumulus-netq
---

NetQ has [early access](https://support.cumulusnetworks.com/hc/en-us/articles/202933878-Early-Access-Features-Defined)
features that provide advanced access to new functionality before it becomes generally available. One feature is available as an early access feature in NetQ 2.4.0:  View MAC address history

This feature is bundled into the `netq-apps` package; there is no
specific EA package like there typically is with Cumulus Linux.

This feature is provided as is, and is subject to change before it becomes generally available.

## Enable/Disable Early Access Features

You enable early access features by running the `netq config add experimental` command on any node running NetQ.

    cumulus@switch:~$ netq config add experimental
    Experimental config added

You disable the early access features by running the `netq config del experimental` command on any node running NetQ.

    cumulus@switch:~$ netq config del experimental
    Experimental config deleted

## View the History of a MAC Address

It is useful when debugging to be able to see when  a MAC address is learned, when and where it moved in the network after that, if there was a duplicate at any time, and so forth. The `netq show mac-history` command makes this information available. It enables you to see:

- each change that was made chronologically
- changes made between two points in time, using the `between` option
- only the difference between to points in time using the `diff` option
- to order the output by selected output fields using the `listby` option
- each change that was made for the MAC address on a particular VLAN, using the `vlan` option

And as with many NetQ commands, the default time range used is now to one hour ago. You can view the output in JSON format as well.

The syntax of the command is:

```
netq [<hostname>] show mac-history <mac> [vlan <1-4096>] [diff] [between <text-time> and <text-endtime>] [listby <text-list-by>] [json]
```

{{%notice note%}}

When entering a time value, you must include a numeric value *and* the
unit of measure:

- d: day(s)
- h: hour(s)
- m: minute(s)
- s: second(s)
- now

For time ranges, the `<text-time>` is the most recent time and the
`<text-endtime>` is the oldest time. The values do not have to have the
same unit of measure.

{{%/notice%}}

This example shows how to view a full chronology of changes for a MAC Address. The carrot (^) notation indicates no change in this value from the row above.

```
cumulus@switch:~$ netq show mac-history 00:03:00:11:11:77 vlan 13

Matching mac-history records:
Last Changed              Hostname          VLAN   Origin Link             Destination            Remote Static
------------------------- ----------------- ------ ------ ---------------- ---------------------- ------ ------------
Mon Nov  4 20:21:13 2019  leaf01            13     no     bond01                                  no     no
Mon Nov  4 20:21:13 2019  leaf02            13     no     bond01                                  no     no
Mon Nov  4 20:21:13 2019  leaf04            13     no     vni13            10.0.0.112             yes    no
Mon Nov  4 20:21:13 2019  leaf03            13     no     vni13            10.0.0.112             yes    no
Mon Nov  4 20:22:40 2019  leaf03            ^      ^      bond03                                  no     ^
Mon Nov  4 20:22:40 2019  leaf04            13     no     vni13            10.0.0.112             yes    no
Mon Nov  4 20:22:40 2019  leaf02            13     no     vni13            10.0.0.134             yes    no
Mon Nov  4 20:22:40 2019  leaf01            13     no     vni13            10.0.0.134             yes    no

```

This example shows how to view the history of a MAC address by hostname. The carrot (^) notation indicates no change in this value from the row above.

```
cumulus@switch:~$ netq show mac-history 00:03:00:11:11:77 vlan 13 listby hostname

Matching mac-history records:
Last Changed              Hostname          VLAN   Origin Link             Destination            Remote Static
------------------------- ----------------- ------ ------ ---------------- ---------------------- ------ ------------
Mon Nov  4 20:21:13 2019  leaf03            13     no     vni13            10.0.0.112             yes    no
Mon Nov  4 20:22:40 2019  leaf03            ^      ^      bond03                                  no     ^
Mon Nov  4 20:21:13 2019  leaf02            13     no     bond01                                  no     no
Mon Nov  4 20:22:40 2019  leaf02            ^      ^      vni13            10.0.0.134             yes    ^
Mon Nov  4 20:21:13 2019  leaf01            13     no     bond01                                  no     no
Mon Nov  4 20:22:40 2019  leaf01            ^      ^      vni13            10.0.0.134             yes    ^
Mon Nov  4 20:21:13 2019  leaf04            13     no     vni13            10.0.0.112             yes    no
Mon Nov  4 20:22:40 2019  leaf04            ^      ^      bond03                                  no     ^
```

This example shows show to view the history of a MAC address between now and two hours ago. The carrot (^) notation indicates no change in this value from the row above.

```
cumulus@switch:~$ netq show mac-history 00:03:00:11:11:77 vlan 13 between now and 2h

Matching mac-history records:
Last Changed              Hostname          VLAN   Origin Link             Destination            Remote Static
------------------------- ----------------- ------ ------ ---------------- ---------------------- ------ ------------
Mon Nov  4 20:21:13 2019  leaf01            13     no     bond01                                  no     no
Mon Nov  4 20:21:13 2019  leaf02            13     no     bond01                                  no     no
Mon Nov  4 20:21:13 2019  leaf04            13     no     vni13            10.0.0.112             yes    no
Mon Nov  4 20:21:13 2019  leaf03            13     no     vni13            10.0.0.112             yes    no
Mon Nov  4 20:22:40 2019  leaf03            ^      ^      bond03                                  no     ^
Mon Nov  4 20:22:40 2019  leaf04            13     no     vni13            10.0.0.112             yes    no
Mon Nov  4 20:22:40 2019  leaf02            13     no     vni13            10.0.0.134             yes    no
Mon Nov  4 20:22:40 2019  leaf01            13     no     vni13            10.0.0.134             yes    no
```
