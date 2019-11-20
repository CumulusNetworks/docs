---
title: Voice VLAN
author: Cumulus Networks
weight: 333
aliases:
 - /display/DOCS/Voice+VLAN
 - /pages/viewpage.action?pageId=8366374
product: Cumulus Linux
version: '4.0'
---
In Cumulus Linux, a *voice VLAN* is a VLAN dedicated to voice traffic on a switch port. However, the term can mean different things to different vendors.

Voice VLAN is part of a trunk port with two VLANs that comprises either of the following:

- Native VLAN, which carries both data and voice traffic
- Voice VLAN, which carries the voice traffic, and a data or native VLAN, which carries the data traffic in a trunk port.

The voice traffic is an 802.1q-tagged packet with a VLAN ID (that might or might not be 0) and an 802.1p (3-bit layer 2 COS) with a specific value (typically 5 is assigned for voice traffic).

Data traffic is always [untagged](../../Ethernet-Bridging-VLANs/VLAN-Tagging/).

## Voice VLAN Configuration Example

{{< img src = "/images/cumulus-linux/voice-vlan.png" >}}

In this example configuration:

- swp1 data traffic traverses the native VLAN of the bridge and the voice traffic traverses VLAN 200
- swp2 data traffic traverses VLAN 10 and the voice traffic traverses VLAN 100
- swp3 data and voice traffic both traverse the native VLAN of the bridge

To configure the topology shown above:

<details>

<summary>NCLU Commands </summary>

```
cumulus@switch:~$ net add bridge bridge ports swp1-3
cumulus@switch:~$ net add bridge bridge vids 1-1000
cumulus@switch:~$ net add bridge bridge pvid 1
cumulus@switch:~$ net add interface swp1 bridge voice-vlan 200
cumulus@switch:~$ net add interface swp2 bridge voice-vlan 100 data-vlan 10
cumulus@switch:~$ net add interface swp3 bridge voice-vlan 300
cumulus@switch:~$ net pending
cumulus@switch:~$ net commit
```

</details>

<details>

<summary>Linux Commands </summary>

Edit the `/etc/network/interfaces` file and add the following configuration:

```
cumulus@switch:~$ sudo nano /etc/network/interfaces

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
```

</details>

## Configure LLDP

Configuring voice VLAN with NCLU does not configure `lldpd` in Cumulus Linux; therefore, LLDP-MED does not provide data and voice VLAN information. You can configure LLDP-MED for each interface in a new file in `/etc/lldp.d`. In the following example, the file is called `/etc/lldpd.d/voice_vlan.conf`:

```
cumulus@switch:~$ sudo nano /etc/lldpd.d/voice_vlan.conf
configure ports swp1 med policy application voice tagged vlan 200 priority voice dscp 46
configure ports swp2 med policy application voice tagged vlan 100 priority voice dscp 46
configure ports swp3 med policy application voice tagged vlan 300 priority voice dscp 46
```

You can also use the `lldpcli` command to configure an LLDP-MED network policy. However, `lldpcli` commands do not persist across switch reboots.

## Troubleshooting

To show the `bridge-vids:`

<details>

<summary>NCLU Commands </summary>

Run the `net show bridge vlan` command:

```
cumulus@switch:~$ net show bridge vlan

Interface      VLAN  Flags
-----------  ------  ---------------------
swp1            1  PVID, Egress Untagged
              200

swp2           10  PVID, Egress Untagged
              200

swp3            1  PVID, Egress Untagged
              300
```

</details>

<details>

<summary>Linux Commands </summary>

Run the `bridge fdb` `show` command:

```
cumulus@switch:~$ bridge fdb show
44:38:39:00:12:9c dev swp2 VLAN 0 master bridge-A permanent
44:38:39:00:12:9b dev swp1 VLAN 0 master bridge-A permanent
44:38:39:00:12:9e dev swp4 VLAN 0 master bridge-B permanent
44:38:39:00:12:9d dev swp3 VLAN 0 master bridge-B permanent
```

</details>

To obtain MAC address information:

<details>

<summary>NCLU Commands </summary>

Run the `net show bridge macs` command:

``` 
cumulus@switch:~$ net show bridge macs

VLAN      Master    Interface    MAC                   TunnelDest  State      Flags    LastSeen
--------  --------  -----------  -----------------  -------------  ---------  -------  ----------
untagged  bridge    bridge       08:00:27:d5:00:93                 permanent           00:13:54
untagged  bridge    swp1         08:00:27:6a:ad:da                 permanent           00:13:54
untagged  bridge    swp2         08:00:27:e3:0c:a7                 permanent           00:13:54
untagged  bridge    swp3         08:00:27:9e:98:86                 permanent           00:13:54
```

</details>

<details>

<summary>Linux Commands </summary>

Run the `sudo brctl showmacs <bridge>` command:

```
cumulus@switch:~$ sudo brctl showmacs my_bridge
  port name mac addr              is local?       ageing timer
  swp4      06:90:70:22:a6:2e     no                19.47
  swp1      12:12:36:43:6f:9d     no                40.50
  bond0     2a:95:22:94:d1:f0     no                 1.98
  swp1      44:38:39:00:12:9b     yes                0.00
  swp2      44:38:39:00:12:9c     yes                0.00
  swp3      44:38:39:00:12:9d     yes                0.00
  swp4      44:38:39:00:12:9e     yes                0.00
  bond0     44:38:39:00:12:9f     yes                0.00
  swp2      90:e2:ba:2c:b1:94     no                12.84
  swp2      a2:84:fe:fc:bf:cd     no                 9.43
```

</details>

To capture LLDP information, check `syslog` or use `tcpdump` on an interface.

## Caveats and Errata

- A static voice VLAN configuration overwrites the existing configuration for the switch port.
- Removing the `bridge-vids` or `bridge-pvid` configuration from a voice VLAN does not remove the VLAN from the bridge.
