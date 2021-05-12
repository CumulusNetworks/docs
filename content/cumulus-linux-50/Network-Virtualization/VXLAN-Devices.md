title: VXLAN Devices
author: NVIDIA
weight: 602
toc: 3
---
Cumulus Linux supports both single and traditional VXLAN devices. Single VXLAN device is enabled by default.

{{%notice note%}}
- Single VXLAN device is supported with VLAN-aware bridge mode only.
- A combination of single and traditional VXLAN devices in a VLAN-aware bridge is not supported.
{{%/notice%}}

## Single VXLAN Device

With a single VXLAN device, a set of VNIs are encapsulated in a single device model. The single VXLAN device has a set of attributes that belong to the VXLAN construct. Individual VNIs are represented as a VLAN to VNI mapping and you can specify which VLANs map to the associated VNIs. The single VXLAN device is similar to the VLAN-aware bridge model, where the bridge encapsulates a set of VLANs and VNIs.

The following example configuration:
- Creates a single VXLAN device (vxlan0)
- Maps VLAN 10 to VNI 10, VLAN 20 to VNI 20, and VLAN 30 to VNI 30
- Enables bridge learning on the single VXLAN device
- Configures the local tunnel IP address to be the loopback address of the switch
- Adds the VXLAN device to the default bridge br_default

{{< tabs "TabID24 ">}}
{{< tab "CUE Commands ">}}

```
cumulus@leaf01:~$ cl set bridge domain br_default vlan 10 vni 10
cumulus@leaf01:~$ cl set bridge domain br_default vlan 20 vni 20
cumulus@leaf01:~$ cl set bridge domain br_default vlan 30 vni 30
cumulus@leaf01:~$ cl set nve vxlan mac-learning on
cumulus@leaf01:~$ cl set nve vxlan source address 10.10.10.1
cumulus@leaf01:~$ cl set nve vxlan flooding head-end-replication 10.10.10.2
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

Edit the `/etc/network/interfaces` file as follows:

```
cumulus@leaf01:~$ sudo nano /etc/network/interfaces
...
auto bridge
iface bridge
    bridge-ports swp1 vxlan0
    bridge-vids 10 20
    bridge-vlan-aware yes
 
auto vxlan0
iface vxlan0
    vxlan-local-tunnelip 10.0.0.11
    vxlan-remoteip 10.0.0.2
    bridge-vids 10 20
    bridge-vlan-vni-map 10=10
    bridge-vlan-vni-map 20=20
```

{{< /tab >}}
{{< /tabs >}}

## Traditional VXLAN Device

With a traditional VXLAN device, each VNI is represented as a separate device (for example, vni10, vni20, vni30).

The following example configuration:
- Creates three unique VXLAN devices (vni10, vni20, and vni30)
- Configures the local tunnel IP address to be the loopback address of the switch
- Enables bridge learning on the each VXLAN device
- Creates the tunnels on each VXLAN device by specifying the loopback addresses of the other leafs
- Adds all VXLAN devices (vni10, vni20, and vni30) to the default bridge br_default

{{< tabs "TabID84 ">}}
{{< tab "CUE Commands ">}}

```
cumulus@leaf01:~$ cl set interface lo ip address 10.10.10.1/32
cumulus@leaf01:~$ cl set bridge domain br_default vlan 10 vni 10
cumulus@leaf01:~$ cl set bridge domain br_default vlan 10 vni 10 mac-learning on
cumulus@leaf01:~$ cl set bridge domain br_default vlan 20 vni 20
cumulus@leaf01:~$ cl set bridge domain br_default vlan 20 vni 20 mac-learning on
cumulus@leaf01:~$ cl set bridge domain br_default vlan 30 vni 30
cumulus@leaf01:~$ cl set bridge domain br_default vlan 30 vni 30 mac-learning on
cumulus@leaf01:~$ cl set nve vxlan source address 10.10.10.1
cumulus@leaf01:~$ cl set bridge domain br_default vlan 10 vni 10 flooding head-end-replication 10.10.10.2
cumulus@leaf01:~$ cl set bridge domain br_default vlan 10 vni 10 flooding head-end-replication 10.10.10.3
cumulus@leaf01:~$ cl set bridge domain br_default vlan 10 vni 10 flooding head-end-replication 10.10.10.4
cumulus@leaf01:~$ cl set bridge domain br_default vlan 20 vni 20 flooding head-end-replication 10.10.10.2
cumulus@leaf01:~$ cl set bridge domain br_default vlan 20 vni 20 flooding head-end-replication 10.10.10.3
cumulus@leaf01:~$ cl set bridge domain br_default vlan 20 vni 20 flooding head-end-replication 10.10.10.4
cumulus@leaf01:~$ cl set bridge domain br_default vlan 20 vni 30 flooding head-end-replication 10.10.10.2
cumulus@leaf01:~$ cl set bridge domain br_default vlan 20 vni 30 flooding head-end-replication 10.10.10.3
cumulus@leaf01:~$ cl set bridge domain br_default vlan 20 vni 30 flooding head-end-replication 10.10.10.4
cumulus@leaf04:~$ cl set interface swp1 bridge domain br_default access 10
cumulus@leaf04:~$ cl set interface swp2 bridge domain br_default access 20
cumulus@leaf04:~$ cl set interface swp3 bridge domain br_default access 30
cumulus@leaf01:~$ cl config apply
```

{{< /tab >}}
{{< tab "Linux Commands ">}}

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
    vxlan-remoteip 10.10.10.2
    vxlan-remoteip 10.10.10.3
    vxlan-remoteip 10.10.10.4
    vxlan-id 10

auto vni20
iface vni20
    bridge-access 20
    vxlan-remoteip 10.10.10.2
    vxlan-remoteip 10.10.10.3
    vxlan-remoteip 10.10.10.4
    vxlan-id 20

auto vni30
iface vni30
    bridge-access 30
    vxlan-remoteip 10.10.10.2
    vxlan-remoteip 10.10.10.3
    vxlan-remoteip 10.10.10.4
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
