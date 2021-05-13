---
title: VXLAN Devices
author: NVIDIA
weight: 605
toc: 3
---
Cumulus Linux supports both single and traditional VXLAN devices. Single VXLAN devices are enabled by default.

{{%notice note%}}
- Single VXLAN devices are supported in VLAN-aware bridge mode only.
- A combination of single and traditional VXLAN devices in a VLAN-aware bridge is not supported.
{{%/notice%}}

## Single VXLAN Device

With a single VXLAN device, a set of VNIs are included in a single device model. The single VXLAN device has a set of attributes that belong to the VXLAN construct. Individual VNIs are represented as a VLAN to VNI mapping and you can specify which VLANs map to the associated VNIs. The single VXLAN device is similar to the VLAN-aware bridge model, where the bridge contains a set of VLANs and VNIs.

Cumulus Linux creates a unique name for the single VXLAN device in the format `vxlan<id>`, where the ID is generated using the bridge name as the hash key.

The following example configuration:
- Creates a single VXLAN device (vxlan0).
- Maps VLAN 10 to VNI 10, VLAN 20 to VNI 20, and VLAN 30 to VNI 30
- Adds the VXLAN device to the default bridge `br_default`

{{< tabs "TabID24 ">}}
{{< tab "CUE Commands ">}}

```
cumulus@leaf01:~$ cl set bridge domain br_default vlan 10 vni 10
cumulus@leaf01:~$ cl set bridge domain br_default vlan 20 vni 20
cumulus@leaf01:~$ cl set bridge domain br_default vlan 30 vni 30
cumulus@leaf01:~$ cl set nve vxlan source address 10.10.10.1
cumulus@leaf01:~$ cl set bridge domain br_default vlan 10 vni 10 flooding multicast-group 239.1.1.110
cumulus@leaf01:~$ cl set bridge domain br_default vlan 20 vni 20 flooding multicast-group 239.1.1.110
cumulus@leaf01:~$ cl set bridge domain br_default vlan 30 vni 30 flooding multicast-group 239.1.1.110
cumulus@leaf04:~$ cl set interface swp1 bridge domain br_default access 10
cumulus@leaf04:~$ cl set interface swp2 bridge domain br_default access 20
cumulus@leaf04:~$ cl set interface swp2 bridge domain br_default access 30
cumulus@leaf01:~$ cl config apply
```

The CUE commands create the following configuration snippet in the `/etc/cue.d/startup.yaml` file:

```
cumulus@spine01:~$ sudo cat /etc/cue.d/startup.yaml

```

{{< /tab >}}
{{< tab "Linux Commands ">}}

```
cumulus@leaf01:~$ sudo nano /etc/network/interfaces
...
auto br_default
iface br_default
    bridge-ports swp1 vxlan0
    bridge-vids 10 20
    bridge-vlan-aware yes
 
auto vxlan0
iface vxlan0
    vxlan-local-tunnelip 10.0.0.1
    bridge-vids 10 20
    bridge-vlan-vni-map 10=10
    bridge-vlan-vni-map 20=20
    vxlan-mcastgrp 239.1.1.110
```

{{< /tab >}}
{{< /tabs >}}

You can configure multiple single VXLAN devices in case you use different multicast groups for replication.

The following example configures:
- VXLAN device (vxlan0), which maps VLAN 10 to VNI 10, VLAN 20 to VNI 20, and VLAN 30 to VNI 30 and adds the VXLAN device to the bridge `bridge1`
- VXLAN device (vxlan1), which maps VLAN 40 to VNI 40, VLAN 50 to VNI 50, and VLAN 60 to VNI 60 and adds the VXLAN device to the bridge `bridge2`

{{< tabs "TabID74 ">}}
{{< tab "CUE Commands ">}}

```
cumulus@leaf01:~$ cl set bridge domain bridge1 vlan 10 vni 10 flooding multicast-group 239.1.1.110
cumulus@leaf01:~$ cl set bridge domain bridge1 vlan 20 vni 20 flooding multicast-group 239.1.1.110
cumulus@leaf01:~$ cl set bridge domain bridge1 vlan 30 vni 30 flooding multicast-group 239.1.1.110
cumulus@leaf04:~$ cl set interface swp1 bridge domain bridge1 access 10
cumulus@leaf04:~$ cl set interface swp2 bridge domain bridge1 access 20
cumulus@leaf04:~$ cl set interface swp3 bridge domain bridge1 access 30
cumulus@leaf01:~$ cl set bridge domain bridge2 vlan 40 vni 40 flooding multicast-group 239.1.1.112
cumulus@leaf01:~$ cl set bridge domain bridge2 vlan 50 vni 50 flooding multicast-group 239.1.1.112
cumulus@leaf01:~$ cl set bridge domain bridge2 vlan 60 vni 60 flooding multicast-group 239.1.1.112
cumulus@leaf04:~$ cl set interface swp4 bridge domain bridge2 access 40
cumulus@leaf04:~$ cl set interface swp5 bridge domain bridge2 access 50
cumulus@leaf04:~$ cl set interface swp6 bridge domain bridge2 access 60
cumulus@leaf01:~$ cl set nve vxlan source address 10.10.10.1
cumulus@leaf01:~$ cl config apply
```

The CUE commands create the following configuration snippet in the `/etc/cue.d/startup.yaml` file:

```
cumulus@spine01:~$ sudo cat /etc/cue.d/startup.yaml
```

{{< /tab >}}
{{< tab "Linux Commands ">}}

```
cumulus@leaf01:~$ sudo nano /etc/network/interfaces
...

auto lo
iface lo inet loopback
    address 10.10.10.1/32
    vxlan-local-tunnelip 10.10.10.1 

auto bridge1
iface bridge1
    bridge-ports swp1 swp2 swp3 vxlan0
    bridge-vids 10 20 30
    bridge-vlan-aware yes
 
auto vxlan0
iface vxlan0
    bridge-vids 10 20 30
    bridge-vlan-vni-map 10=10
    bridge-vlan-vni-map 20=20
    bridge-vlan-vni-map 30=30
    vxlan-mcastgrp 239.1.1.110

auto bridge2
iface bridge2
    bridge-ports swp4 swp5 swp6 vxlan1
    bridge-vids 40 50 60
    bridge-vlan-aware yes
 
auto vxlan1
iface vxlan1
    bridge-vids 40 50 60
    bridge-vlan-vni-map 40=10
    bridge-vlan-vni-map 50=20
    bridge-vlan-vni-map 60=30
    vxlan-mcastgrp 239.1.1.112
```

{{< /tab >}}
{{< /tabs >}}

## Traditional VXLAN Device

With a traditional VXLAN device, each VNI is represented as a separate device (for example, vni10, vni20, vni30).

The following example configuration:
- Enables traditional VXLAN devices
- Creates three unique VXLAN devices (vni10, vni20, and vni30)
- Configures the local tunnel IP address to be the loopback address of the switch
- Adds each VXLAN device (vni10, vni20, and vni30) to the default bridge `br_default`

{{< tabs "TabID84 ">}}
{{< tab "CUE Commands ">}}

```
cumulus@leaf01:~$ NEED COMMAND
cumulus@leaf01:~$ cl set interface lo ip address 10.10.10.1/32
cumulus@leaf01:~$ cl set bridge domain br_default vlan 10 vni 10
cumulus@leaf01:~$ cl set bridge domain br_default vlan 20 vni 20
cumulus@leaf01:~$ cl set bridge domain br_default vlan 30 vni 30
cumulus@leaf01:~$ cl set nve vxlan source address 10.10.10.1
cumulus@leaf04:~$ cl set interface swp1 bridge domain br_default access 10
cumulus@leaf04:~$ cl set interface swp2 bridge domain br_default access 20
cumulus@leaf04:~$ cl set interface swp3 bridge domain br_default access 30
cumulus@leaf01:~$ cl config apply
```

{{< /tab >}}
{{< tab "Linux Commands ">}}

Edit the `/var/lib/ifupdown2/policy.d/vxlan.json` file and add "single-vxlan-device": "on":

```
{
      "vxlan": {
        "module_globals": {
         "vxlan-purge-remotes": "no",
         "single-vxlan-device": "on"
        },
        "defaults": {
         "vxlan-ageing": "1800",
         "vxlan-port": "4789",
         "vxlan-ttl": "64"
        }
      }
    }
  )
```

Edit the `/etc/network/interfaces` file as follows:

```
auto lo
iface lo inet loopback
    address 10.10.10.1/32
    vxlan-local-tunnelip 10.10.10.1

auto mgmt
iface mgmt
    address 127.0.0.1/8
    address ::1/128
    vrf-table auto

auto eth0
iface eth0 inet dhcp
    ip-forward off
    ip6-forward off
    vrf mgmt

auto swp1
iface swp1
    bridge-access 10

auto swp2
iface swp2
    bridge-access 20

auto swp3
iface swp3
    bridge-access 30

auto vni10
iface vni10
    bridge-access 10
    vxlan-id 10

auto vni20
iface vni20
    bridge-access 20
    vxlan-id 20

auto vni30
iface vni30
    bridge-access 30
    vxlan-id 20

auto br_default
iface br_default
    bridge-ports swp1 swp2 vni10 vni20 vni30
    bridge-vlan-aware yes
    bridge-vids 10 20 30
    bridge-pvid 1
```

{{< /tab >}}
{{< /tabs >}}

- For information about VXLAN devices and static VXLAN tunnels, see {{<link url="Static-VXLAN-Tunnels" text="Static VXLAN Tunnels">}}.
- For information about VXLAN devices and EVPN, see {{<link url="Ethernet-Virtual-Private-Network-EVPN" text="EVPN">}}.