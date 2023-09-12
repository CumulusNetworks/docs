---
title: VXLAN Devices
author: NVIDIA
weight: 600
toc: 3
---
Cumulus Linux supports both single and traditional [VXLAN](## "Virtual Extensible LAN") devices.

{{%notice note%}}
- You can configure single VXLAN devices in VLAN-aware bridge mode only.
- You cannot use a combination of single and traditional VXLAN devices.
- A traditional VXLAN device configuration supports up to 2000 VNIs and a single VXLAN device configuration supports up to 4000 VNIs.
{{%/notice%}}

## Traditional VXLAN Device

With a traditional VXLAN device, each VNI is a separate device (for example, vni10, vni20, vni30).
You can configure traditional VXLAN devices by manually editing the `/etc/network/interfaces` file.

The following example configuration:
- Creates two unique VXLAN devices (vni10 and vni20)
- Adds each VXLAN device (vni10 and vni20) to the bridge `bridge`
- Configures the local tunnel IP address to be the loopback address of the switch

{{< tabs "TabID25 ">}}
{{< tab "NVUE Commands ">}}

You cannot use NVUE commands to configure traditional VXLAN devices.

{{< /tab >}}
{{< tab "Linux Commands ">}}

Edit the `/etc/network/interfaces` file, then run the `ifreload -a` command.

```
cumulus@leaf01:~$ sudo nano /etc/network/interfaces
...
auto lo
iface lo inet loopback
    address 10.10.10.1/32
    vxlan-local-tunnelip 10.10.10.1

auto mgmt
iface mgmt
    address 127.0.0.1/8
    vrf-table auto

auto swp1
iface swp1
    bridge-access 10

auto swp2
iface swp2
    bridge-access 20

auto vni10
iface vni10
    bridge-access 10
    mstpctl-bpduguard yes
    mstpctl-portbpdufilter yes
    vxlan-id 10

auto vni20
iface vni20
    bridge-access 20
    mstpctl-bpduguard yes
    mstpctl-portbpdufilter yes
    vxlan-id 20

auto bridge
iface bridge
    bridge-ports swp1 swp2 vni10 vni20
    bridge-vlan-aware yes
    bridge-vids 10 20
    bridge-pvid 1
```

```
cumulus@leaf01:~$ ifreload -a
```

{{< /tab >}}
{{< /tabs >}}

## Single VXLAN Device

With a single VXLAN device, a set of VNIs represent a single device model. The single VXLAN device has a set of attributes that belong to the VXLAN construct. Individual VNIs include a VLAN to VNI mapping and you can specify which VLANs map to the associated VNIs. Single VXLAN device simplifies the configuration and reduces the overhead by replacing multiple traditional VXLAN devices with a single VXLAN device.

{{%notice note%}}
Cumulus Linux supports multiple single VXLAN devices when configured with multiple VLAN-aware bridges. You configure multiple single VXLAN devices in the same way you configure a single VXLAN device. Make sure *not* to duplicate VNIs across single VXLAN device configurations.

The limitations listed for {{<link url="VLAN-aware-Bridge-Mode" text="multiple VLAN-aware bridges">}} also apply to multiple single VXLAN devices.
{{%/notice%}}

You can configure a single VXLAN device with NVUE or by manually editing the `/etc/network/interfaces` file.
When you configure a single VXLAN device with NVUE, Cumulus Linux creates a unique name for the device in the format `vxlan<id>`. Cumulus Linux generates the ID using the bridge name as the hash key.

The following example configuration:
- Creates a single VXLAN device (vxlan48)
- Maps VLAN 10 to VNI 10 and VLAN 20 to VNI 20
- Adds the VXLAN device to the default bridge `br_default`
- Sets the flooding multicast group for VNI 10 to 239.1.1.110 and the multicast group for VNI 20 to 239.1.1.120

{{< tabs "TabID106 ">}}
{{< tab "NVUE Commands ">}}

```
cumulus@leaf01:~$ nv set bridge domain br_default vlan 10 vni 10
cumulus@leaf01:~$ nv set bridge domain br_default vlan 20 vni 20
cumulus@leaf01:~$ nv set nve vxlan source address 10.10.10.1
cumulus@leaf01:~$ nv set bridge domain br_default vlan 10 vni 10 flooding multicast-group 239.1.1.110
cumulus@leaf01:~$ nv set bridge domain br_default vlan 20 vni 20 flooding multicast-group 239.1.1.120
cumulus@leaf01:~$ nv set interface swp1 bridge domain br_default access 10
cumulus@leaf01:~$ nv set interface swp2 bridge domain br_default access 20
cumulus@leaf01:~$ nv config apply
```

The `nv config save` command creates the following configuration snippet in the `/etc/nvue.d/startup.yaml` file:

```
cumulus@leaf01:~$ sudo cat /etc/nvue.d/startup.yaml
- set:
    bridge:
      domain:
        br_default:
          vlan:
            '10':
              vni:
                '10':
                  flooding:
                    multicast-group: 239.1.1.110
                    enable: on
            '20':
              vni:
                '20':
                  flooding:
                    multicast-group: 239.1.1.120
                    enable: on
    nve:
      vxlan:
        enable: on
        source:
          address: 10.10.10.1
    interface:
      swp1:
        bridge:
          domain:
            br_default:
              access: 10
        type: swp
      swp2:
        bridge:
          domain:
            br_default:
              access: 20
        type: swp
```

{{< /tab >}}
{{< tab "Linux Commands ">}}

Edit the `/etc/network/interfaces` file then run the `ifreload -a` command.

```
cumulus@leaf01:~$ sudo nano /etc/network/interfaces
...
auto swp1
iface swp1
    bridge-access 10

auto swp2
iface swp2
    bridge-access 20

auto vxlan48
iface vxlan48
    vxlan-mcastgrp-map 10=239.1.1.110 20=239.1.1.120
    bridge-vlan-vni-map 10=10 20=20
    bridge-vids 10 20
    bridge-learning off

auto br_default
iface br_default
    bridge-ports swp1 swp2 vxlan48
    hwaddress 44:38:39:22:01:ab
    bridge-vlan-aware yes
    bridge-vids 10 20
    bridge-pvid 1
```

```
cumulus@leaf01:~$ ifreload -a
```

{{< /tab >}}
{{< /tabs >}}

## VXLAN UDP Port

You can change the UDP port that Cumulus Linux uses for VXLAN encapsulation. The default port is 4879.

The following example changes the UDP port for VXLAN encapsulation to 1024:

```
cumulus@switch:mgmt:~$ nv set nve vxlan port 1024
```

## TC Filters

NVIDIA recommends you run TC filter commands on each VLAN interface on the VTEP to install rules to protect the UDP port that Cumulus Linux uses for VXLAN encapsulation against VXLAN hopping vulnerabilities. If you have VRR configured on the VLAN, add a similar rule for the VRR device.

The following example installs an IPv4 and an IPv6 filter on vlan10 to protect the default port 4879:

```
cumulus@switch:mgmt:~$ tc filter add dev vlan10 prio 1 protocol ip ingress flower ip_proto udp dst_port 4879 action drop
cumulus@switch:mgmt:~$ tc filter add dev vlan10 prio 2 protocol ipv6 ingress flower ip_proto udp dst_port 4879 action drop
```

The following example installs an IPv4 and an IPv6 filter on VRR device vlan10-v0 to protect port 4879:

```
cumulus@switch:mgmt:~$ tc filter add dev vlan10-v0 prio 1 protocol ip ingress flower ip_proto udp dst_port 4879 action drop
cumulus@switch:mgmt:~$ tc filter add dev vlan10-v0 prio 2 protocol ipv6 ingress flower ip_proto udp dst_port 4879 action drop
```

## Related Information

- For information about VXLAN devices and static VXLAN tunnels, see {{<link url="Static-VXLAN-Tunnels" text="Static VXLAN Tunnels">}}.
- For information about VXLAN devices and EVPN, see {{<link url="Ethernet-Virtual-Private-Network-EVPN" text="EVPN">}}.
