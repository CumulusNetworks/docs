---
title: Voice VLAN
author: NVIDIA
weight: 410
toc: 4
---
In Cumulus Linux, a *voice VLAN* is a VLAN dedicated to voice traffic on a switch port. Voice VLAN is part of a trunk port with two VLANs that comprises either of the following:

- Native VLAN, which carries both data and voice traffic.
- Voice VLAN, which carries the voice traffic, and a data or native VLAN, which carries the data traffic in a trunk port.

The voice traffic is an 802.1q-tagged packet with a VLAN ID (that might or might not be 0) and an 802.1p (3-bit layer 2 COS) with a specific value (typically 5 is assigned for voice traffic).

Data traffic is always {{<link url="VLAN-Tagging" text="untagged">}}.

## Example Configuration

|      |      |
| ---- | ---- |
| <img width=300/> {{< img src = "/images/cumulus-linux/voice-vlan-example.png" >}} | <br><br><br><br>In this example configuration:<ul><li>swp1 data traffic traverses the native VLAN of the bridge and the voice traffic traverses VLAN 200</li><li>swp2 data traffic traverses VLAN 100 and the voice traffic traverses VLAN 200</li><li>swp3 data traffic traverses VLAN 100 and voice traffic traverses VLAN 300</li></ul> |

To configure the topology shown above:

{{< tabs "TabID32 ">}}

{{< tab "NCLU Commands ">}}

```
cumulus@switch:~$ net add bridge bridge ports swp1-3
cumulus@switch:~$ net add bridge bridge vids 10,100,200,300
cumulus@switch:~$ net add bridge bridge pvid 10
cumulus@switch:~$ net add interface swp1 bridge voice-vlan 200
cumulus@switch:~$ net add interface swp2 bridge voice-vlan 200 data-vlan 100
cumulus@switch:~$ net add interface swp3 bridge voice-vlan 300 data-vlan 100
cumulus@switch:~$ net pending
cumulus@switch:~$ net commit
```

{{< /tab >}}

{{< tab "Linux Commands ">}}

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
    bridge-pvid 100
    bridge-vids 200
    mstpctl-bpduguard yes
    mstpctl-portadminedge yes

auto swp3
iface swp3
    bridge-pvid 100
    bridge-vids 300
    mstpctl-bpduguard yes
    mstpctl-portadminedge yes

auto bridge
iface bridge
  bridge-ports swp1 swp2 swp3
  bridge-pvid 10
  bridge-vids 10 100 200 300
  bridge-vlan-aware yes
```

{{< /tab >}}

{{< tab "CUE Commands ">}}

```
cumulus@switch:~$ cl set interface swp1-3 bridge domain br_default
cumulus@switch:~$ cl set bridge domain br_default vlan 10,100,200,300
cumulus@switch:~$ cl set bridge domain br_default untagged 10
cumulus@switch:~$ cl set interface swp1 bridge domain br_default NEED COMMAND
cumulus@switch:~$ cl set interface swp2 bridge domain br_default NEED COMMAND
cumulus@switch:~$ cl set interface swp3 bridge domain br_default NEED COMMAND
cumulus@switch:~$ cl config apply
```

{{< /tab >}}

{{< /tabs >}}

## Troubleshooting

To show the bridge VIDs, run the `net show bridge vlan` command:

```
cumulus@switch:~$ net show bridge vlan

Interface      VLAN  Flags
-----------  ------  ---------------------
swp1             10  PVID, Egress Untagged
                200
swp2            100  PVID, Egress Untagged
                200
swp3            100  PVID, Egress Untagged
                300
```

To obtain MAC address information, run the NCLU `net show bridge macs` command or the Linux `sudo brctl showmacs <bridge>` command. For example:

```
cumulus@switch:~$ net show bridge macs

VLAN      Master    Interface    MAC                   TunnelDest  State      Flags    LastSeen
--------  --------  -----------  -----------------  -------------  ---------  -------  ----------
untagged  bridge    bridge       08:00:27:d5:00:93                 permanent           00:13:54
untagged  bridge    swp1         08:00:27:6a:ad:da                 permanent           00:13:54
untagged  bridge    swp2         08:00:27:e3:0c:a7                 permanent           00:13:54
untagged  bridge    swp3         08:00:27:9e:98:86                 permanent           00:13:54
```

To capture LLDP information, check `syslog` or use `tcpdump` on an interface.

## Considerations

- A static voice VLAN configuration overwrites the existing configuration for the switch port.
- Removing the `bridge-vids` or `bridge-pvid` configuration from a voice VLAN does not remove the VLAN from the bridge.
- Configuring voice VLAN with NCLU does not configure `lldpd` in Cumulus Linux; LLDP-MED does **not** provide data and voice VLAN information. You can configure LLDP-MED for each interface in a new file in `/etc/lldp.d`. In the following example, the file is called `/etc/lldpd.d/voice_vlan.conf`:

   ```
   cumulus@switch:~$ sudo nano /etc/lldpd.d/voice_vlan.conf
   configure ports swp1 med policy application voice tagged vlan 200 priority voice dscp 46
   configure ports swp2 med policy application voice tagged vlan 100 priority voice dscp 46
   configure ports swp3 med policy application voice tagged vlan 300 priority voice dscp 46
   ```

   You can also use the `lldpcli` command to configure an LLDP-MED network policy. However, `lldpcli` commands do not persist across switch reboots.
