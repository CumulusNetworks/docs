---
title: Voice VLAN
author: Cumulus Networks
weight: 339
aliases:
 - /display/CL36/Voice+VLAN
 - /pages/viewpage.action?pageId=8362146
pageID: 8362146
product: Cumulus Linux
version: '3.6'
imgData: cumulus-linux-36
siteSlug: cumulus-linux-36
---
In Cumulus Linux, a *voice VLAN* is a VLAN dedicated to voice traffic on
a switch port. However, the term can mean different things to different
vendors.

Voice VLAN is part of a trunk port with 2 VLANs that comprises either:

  - Native VLAN, which carries both data and voice traffic, or

  - Voice VLAN, which carries the voice traffic, and a data or native
    VLAN, which carries the data traffic in a trunk port.

The voice traffic is an 802.1q-tagged packet with a VLAN ID that has a
VLAN ID (which may or may not be 0) and an 802.1p (3-bit layer 2 COS)
with a specific value (typically 5 is assigned for voice traffic).

Data traffic is always
[untagged](/version/cumulus-linux-36/Layer_2/Ethernet_Bridging_-_VLANs/VLAN_Tagging).

## <span>Cumulus Linux Voice VLAN Example</span>

{{% imgOld 0 %}}

You can configure the topology above using the following
[NCLU](/version/cumulus-linux-36/System_Configuration/Network_Command_Line_Utility_-_NCLU/)
commands. In this configuration:

  - swp1 data traffic traverses the bridge's native VLAN and the voice
    traffic traverses VLAN 200

  - swp2 data traffic traverses VLAN 10 and the voice traffic traverses
    VLAN 100

  - swp3 data and voice traffic both traverse the bridge's native VLAN

<!-- end list -->

    cumulus@switch:~$ net add bridge bridge ports swp1-3
    cumulus@switch:~$ net add bridge bridge vids 1-1000
    cumulus@switch:~$ net add bridge bridge pvid 1
    cumulus@switch:~$ net add interface swp1 bridge voice-vlan 200
    cumulus@switch:~$ net add interface swp2 bridge voice-vlan 100 data-vlan 10
    cumulus@switch:~$ net add interface swp3 bridge voice-vlan
    cumulus@switch:~$ net add interface swp1-3 stp bpduguard
    cumulus@switch:~$ net add interface swp1-3 stp portadminedge
    cumulus@switch:~$ net pending
    cumulus@switch:~$ net commit

These commands create the following configuration snippet in the
`/etc/network/interfaces` file:

    auto swp1
    iface swp1
       bridge-vids 200
       mstpctl-bpduguard yes
       mstpctl-portadminedge yes
     
    auto swp2
    iface swp2
       bridge-pvid 10
       bridge-vids 100
       mstpctl-bpduguard yes
       mstpctl-portadminedge yes
     
    auto swp3
    iface swp3
       bridge-vids 300
       mstpctl-bpduguard yes
       mstpctl-portadminedge yes
     
    auto bridge
    iface bridge
      bridge-ports swp1 swp2 swp3
      bridge-pvid 1
      bridge-vids 1-1000
      bridge-vlan-aware yes

### <span>Configuring LLDP</span>

Configuring voice VLAN with NCLU does not configure `lldpd` in Cumulus
Linux, so LLDP-MED does not provide data and voice VLAN information. You
can configure LLDP-MED for each interface in a new file in
`/etc/lldp.d`. In the following example, the file is called
`/etc/lldpd.d/voice_vlan.conf`:

    cumulus@switch:~$ sudo nano /etc/lldpd.d/voice_vlan.conf
    configure ports swp1 med policy application voice tagged vlan 200 priority voice dscp 46
    configure ports swp2 med policy application voice tagged vlan 100 priority voice dscp 46
    configure ports swp3 med policy application voice tagged vlan 300 priority voice dscp 46

You can also use the `lldpcli` command to configure an LLDP-MED network
policy. However, `lldpcli` commands do not persist across reboots of the
switch.

## <span>Troubleshooting</span>

The `bridge-vids` can be reviewed with the `net show bridge vlan`
command:

    cumulus@switch:~$ net show bridge vlan
     
    Interface      VLAN  Flags
    -----------  ------  ---------------------
    swp1              1  PVID, Egress Untagged
                    200
     
    swp2             10  PVID, Egress Untagged
                    200
     
    swp3              1  PVID, Egress Untagged
                    300

<span style="color: #333333;"> You can get MAC address information using
the `net show bridge macs` command: </span>

``` 
cumulus@switch:~$ net show bridge macs
 
VLAN      Master    Interface    MAC                   TunnelDest  State      Flags    LastSeen
--------  --------  -----------  -----------------  -------------  ---------  -------  ----------
untagged  bridge    bridge       08:00:27:d5:00:93                 permanent           00:13:54   
untagged  bridge    swp1         08:00:27:6a:ad:da                 permanent           00:13:54   
untagged  bridge    swp2         08:00:27:e3:0c:a7                 permanent           00:13:54   
untagged  bridge    swp3         08:00:27:9e:98:86                 permanent           00:13:54   
```

You can capture LLDP information by checking `syslog` or using `tcpdump`
on an interface.

## <span>Caveats and Errata</span>

  - A static voice VLAN configuration overwrites a switch port's
    existing configuration.

  - Removing the `bridge-vids` or `bridge-pvid` configuration from a
    voice VLAN does not remove the VLAN from the bridge.
