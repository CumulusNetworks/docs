---
title: Port Channels - Link Aggregation - LAG
author: NVIDIA
weight: 410
product: SONiC
version: 202012
siteSlug: sonic
---

Link aggregation is a way to increase bandwidth in an Ethernet network by aggregating multiple physical switch ports into a *link aggregation group* (LAG). A LAG &mdash; also known as a port channel or bond &mdash; also provides redundancy in the event that one of the link members fails.

In SONiC, link aggregation is managed in the `teamd` container, which provides the functionality for configuring port channels on SONiC switches. The `teamd` service is a Linux-based open source implementation of the Link Aggregation Control Protocol (LACP). The `teamsyncd` service manages the interaction between `teamd` and southbound subsystems.

## Prerequisites

- A port channel name must be in the format *PortChannelxxxx*, where *xxxx* is a 1 to 4 digit number. For example, *PortChannel0002*.
- Before you add a physical port to a port channel, bring the interface up, remove its IP address, remove it from a VLAN if it is a member of one.

## Configure a Port Channel

When you create a LAG, you give it a name and add some physical ports as members. In addition, you can specify either or both of these options:

- `min-links`: The minimum number of links required to bring up the port channel.
- `fallback`: When set to `true`, it enables LACP fallback. When enabled, only one member port is selected as the active port in a port channel during fallback mode. Read more about LACP fallback in the {{<exlink url="https://github.com/Azure/SONiC/blob/master/doc/lag/LACP%20Fallback%20Feature%20for%20SONiC_v0.5.md" text="Azure GitHub">}} documentation.

{{<tabs "PortChannel">}}

Configure a port channel named *PortChannel0002* and add interfaces Ethernet4 and Ethernet8 as its members.

{{<tab "SONiC CLI">}}

    admin@leaf01:~$ sudo config portchannel add PortChannel0002
    admin@leaf01:~$ sudo config portchannel member add PortChannel0002 Ethernet4
    admin@leaf01:~$ sudo config portchannel member add PortChannel0002 Ethernet8

{{</tab>}}

{{<tab "config_db.json">}}

Configure the port channel in the PORTCHANNEL table in `/etc/sonic/config_db.json`.

```
admin@switch:~$ sudo vi /etc/sonic/config_db.json

"PORTCHANNEL": {
    "PortChannel0002": {
        "admin_status": "up", 
        "members": [
            "Ethernet4",
            "Ethernet8"
        ], 
        "mtu": "9100"
    }
},
"PORTCHANNEL_INTERFACE": {
    "PortChannel0001|10.0.0.100/24": {}
}
```

{{</tab>}}

{{</tabs>}}

Save your changes to the configuration:

    admin@switch:~$ sudo config save -y

## Show Port Channels

You can see the port channel and its members with the `show interface portchannel` command:

    admin@switch:~$ show interface portchannel PortChannel0002
    Flags: A - active, I - inactive, Up - up, Dw - Down, N/A - not available, S - selected, D - deselected
    No.   Team Dev        Protocol    Ports
    ----- --------------- ----------- ---------------------------
    0002  PortChannel0002 LACP(A)(Up) Ethernet4(S) Ethernet8(S)

## Delete a Port Channel or Member

You can delete a port channel only if it has no members or if you already removed its members.

To remove a member port from a port channel, run:

    admin@leaf01:~$ sudo config portchannel member del PortChannel0002 Ethernet8

To delete a port channel, run:

    admin@leaf01:~$ sudo config portchannel del PortChannel0008

## Dump the Port Channel Configuration with teamdctl

You can use the `teamdctl` service to dump the configured port channel:

```
admin@switch:~$ teamdctl PortChannel0002 config dump
{
    "device": "PortChannel0002",
    "hwaddr": "e4:1d:2d:f7:d5:40",
    "link_watch": {
        "name": "ethtool"
    },
    "ports": {
        "Ethernet4": {},
        "Ethernet8": {}
    },
    "runner": {
        "active": true,
        "min_ports": 1,
        "name": "lacp",
        "tx_hash": [
            "eth",
            "ipv4",
            "ipv6"
         ]
     }

 }
```
