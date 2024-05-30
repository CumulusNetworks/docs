---
title: VXLAN Devices
author: NVIDIA
weight: 600
toc: 3
---
Cumulus Linux supports both single and traditional <span class="a-tooltip">[VXLAN](## "Virtual Extensible LAN")</span> devices.

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

The following static VXLAN example configuration:
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

NVUE creates the following configuration snippet in the `/etc/nvue.d/startup.yaml` file:

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

## Automatic VLAN to VNI Mapping

In an EVPN VXLAN environment, you need to map individual VLANs to VNIs. For a single VXLAN device, you can do this with a separate NVUE command per VLAN; however, this can be cumbersome if you have to configure many VLANS or need to isolate tenants and reuse VLANs. To simplify the configuration, you can use these two commands instead:
- `nv set bridge domain <bridge> vlan <vlans> vni auto` configures the specified VLANs to use automatic mapping.
- `nv set bridge domain <bridge> vlan-vni-offset` configures the offset you want to use for the VNIs. For example, if you specify an offset of 10000, the VNI is the VLAN plus 10000.

The following commands automatically set the VNIs for VLAN 10, 20, 30, 40, and 50 on the default bridge (`br_default`) to 1000010, 1000020, 1000030, 1000040, and 1000050, and set the VNIs for VLAN 10, 20, 30, 40, and 50 on bridge `br_01` to 2000010, 2000020, 2000030, 2000040, and 2000050:

```
cumulus@switch:mgmt:~$ nv set bridge domain br_default vlan 10,20,30,40,50 vni auto
cumulus@switch:mgmt:~$ nv set bridge domain br_default vlan-vni-offset 10000
cumulus@switch:mgmt:~$ nv set bridge domain br_01 vlan 10,20,30,40,50 vni auto
cumulus@switch:mgmt:~$ nv set bridge domain br_01 vlan-vni-offset 20000
cumulus@switch:mgmt:~$ nv config apply
```

{{%notice note%}}
You cannot use automatic NVUE VLAN to VNI mapping commands to configure static VXLAN tunnels.
{{%/notice%}}

The following configuration example configures VLANS 10, 20, and 30. The VLANs map automatically to VNIs with an offset of 10000.

{{< tabs "TabID217 ">}}
{{< tab "NVUE Commands">}}

```
cumulus@switch:mgmt:~$ nv set interface lo ip address 10.10.10.1/32
cumulus@switch:mgmt:~$ nv set interface swp1-2 bridge domain br_default
cumulus@switch:mgmt:~$ nv set bridge domain br_default vlan 10,20,30
cumulus@switch:mgmt:~$ nv set interface vlan10
cumulus@switch:mgmt:~$ nv set interface vlan20
cumulus@switch:mgmt:~$ nv set interface vlan30
cumulus@switch:mgmt:~$ nv set bridge domain br_default vlan 10,20,30 vni auto
cumulus@switch:mgmt:~$ nv set bridge domain br_default vlan-vni-offset 10000
cumulus@switch:mgmt:~$ nv config apply
```

To unset the above configuration, run the `nv unset` commands in the reverse order. You must omit the bridge name from the `nv unset interface swp1-2 bridge domain br_default` command and `auto` from the `nv unset bridge domain br_default vlan 10,20,30 vni auto` commands.

```
cumulus@switch:mgmt:~$ nv unset bridge domain br_default vlan-vni-offset
cumulus@switch:mgmt:~$ nv unset bridge domain br_default vlan 10,20,30 vni
cumulus@switch:mgmt:~$ nv unset interface vlan30
cumulus@switch:mgmt:~$ nv unset interface vlan20
cumulus@switch:mgmt:~$ nv unset interface vlan10
cumulus@switch:mgmt:~$ nv unset bridge domain br_default vlan 10,20,30
cumulus@switch:mgmt:~$ nv unset interface swp1-2 bridge domain
cumulus@switch:mgmt:~$ nv unset interface lo ip address 10.10.10.1/32
cumulus@switch:mgmt:~$ nv config apply
```

{{< /tab >}}
{{< tab "/etc/nvue.d/startup.yaml ">}}

```
cumulus@switch:mgmt:~$ sudo cat /etc/nvue.d/startup.yaml
- set:
    bridge:
      domain:
        br_default:
          vlan:
            '10':
              vni:
                auto: {}
            '20':
              vni:
                auto: {}
            '30':
              vni:
                auto: {}
          vlan-vni-offset: 10000
    interface:
      lo:
        ip:
          address:
            10.10.10.1/32: {}
        type: loopback
      swp1:
        bridge:
          domain:
            br_default: {}
        type: swp
      swp2:
        bridge:
          domain:
            br_default: {}
        type: swp
      vlan10:
        type: svi
        vlan: 10
      vlan20:
        type: svi
        vlan: 20
      vlan30:
        type: svi
        vlan: 30
    nve:
      vxlan:
        enable: on
```

{{< /tab >}}
{{< tab "/etc/network/interfaces ">}}

```
cumulus@switch:mgmt:~$ sudo cat /etc/network/interfaces
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

auto swp2
iface swp2

auto vlan10
iface vlan10
    hwaddress 44:38:39:22:01:ab
    vlan-raw-device br_default
    vlan-id 10

auto vlan20
iface vlan20
    hwaddress 44:38:39:22:01:ab
    vlan-raw-device br_default
    vlan-id 20

auto vlan30
iface vlan30
    hwaddress 44:38:39:22:01:ab
    vlan-raw-device br_default
    vlan-id 30

auto vxlan48
iface vxlan48
    bridge-vlan-vni-map 10=10010 20=10020 30=10030
    bridge-learning off

auto br_default
iface br_default
    bridge-ports swp1 swp2 vxlan48
    hwaddress 44:38:39:22:01:ab
    bridge-vlan-aware yes
    bridge-vids 10 20 30
    bridge-pvid 1
```

{{< /tab >}}
{{< /tabs >}}

## VXLAN UDP Port

You can change the UDP port that Cumulus Linux uses for VXLAN encapsulation. The default port is 4879.

The following example changes the UDP port for VXLAN encapsulation to 1024:

```
cumulus@switch:mgmt:~$ nv set nve vxlan port 1024
```

## Related Information

- For information about VXLAN devices and static VXLAN tunnels, see {{<link url="Static-VXLAN-Tunnels" text="Static VXLAN Tunnels">}}.
- For information about VXLAN devices and EVPN, see {{<link url="Ethernet-Virtual-Private-Network-EVPN" text="EVPN">}}.
