---
title: Static VXLAN Tunnels
author: NVIDIA
weight: 620
toc: 3
---
In VXLAN-based networks, there are a range of complexities and challenges in determining the destination *virtual tunnel endpoints* (VTEPs) for any given VXLAN. At scale, various solutions, including controller-based options, such as VMware NSX and new standards like {{<link url="Ethernet-Virtual-Private-Network-EVPN" text="EVPN">}} try to address these complexities, however, they also have their own complexities.

*Static VXLAN tunnels* serve to connect two VTEPs in a given environment. Static VXLAN tunnels are the simplest deployment mechanism for small scale environments and are interoperable with other vendors that adhere to VXLAN standards. Because you simply map which VTEPs are in a particular VNI, you can avoid the tedious process of defining connections to every VLAN on every other VTEP on every other rack.

{{%notice note%}}
Cumulus Linux supports *more* than one VXLAN ID per VLAN-aware bridge. However, more than one VXLAN ID per traditional bridge is not supported.
{{%/notice%}}

## Configure Static VXLAN Tunnels

To configure static VXLAN tunnels, you create VXLAN devices. Cumulus Linux supports:
- *Single VXLAN devices*, where all VXLAN tunnels with the same settings (local tunnel IP address and VXLAN remote IP addresses) can share the same VXLAN device and you only need to add the single VXLAN device to the bridge.
- *Traditional VXLAN devices*, where you configure unique VXLAN devices and add each device to the bridge.

The following topology is used in the configuration examples. Each IP address corresponds to the loopback address of the switch.

{{< img src = "/images/cumulus-linux/static-vxlan-tunnel-example.png" >}}

### Single VXLAN Device

The following single VXLAN device example configuration:
- Sets the loopback address on each leaf
- Creates a single VXLAN device (vxlan0)
- Configures the local tunnel IP address to be the loopback address of the switch
- Enables bridge learning on the single VXLAN device
- Creates the static VXLAN tunnels by specifying the loopback addresses of the other leafs
- Adds the VXLAN device to the default bridge br_default

{{< tabs "TabID35 ">}}
{{< tab "CUE Commands ">}}

{{< tabs "TabID38 ">}}
{{< tab "leaf01 ">}}

```
cumulus@leaf01:~$ NEED COMMAND
cumulus@leaf01:~$ cl config apply
```

{{< /tab >}}
{{< tab "leaf02 ">}}

```
cumulus@leaf02:~$ NEED COMMAND
cumulus@leaf02:~$ cl config apply
```

{{< /tab >}}
{{< tab "leaf03 ">}}

```
cumulus@leaf03:~$ NEED COMMAND
cumulus@leaf03:~$ cl config apply
```

{{< /tab >}}
{{< tab "leaf04 ">}}

```
cumulus@leaf04:~$ NEED COMMAND
cumulus@leaf04:~$ cl config apply
```

{{< /tab >}}
{{< /tabs >}}

{{< /tab >}}
{{< tab "Linux Commands ">}}

Editing the `/etc/network/interfaces` file as follows:

{{< tabs "TabID78 ">}}
{{< tab "leaf01 ">}}

```

```

{{< /tab >}}
{{< tab "leaf02 ">}}

```

```

{{< /tab >}}
{{< tab "leaf03 ">}}

```

```

{{< /tab >}}
{{< tab "leaf04 ">}}

```

```

{{< /tab >}}
{{< /tabs >}}

{{< /tab >}}
{{< /tabs >}}

### Traditional VXLAN Device

The following example traditional VXLAN device configuration:
- Sets the loopback address on each leaf
- Creates two unique VXLAN devices (vni10 and vni20)
- Configures the local tunnel IP address to be the loopback address of the switch
- Enables bridge learning on the each VXLAN device
- Creates the tunnels on each VXLAN device by specifying the loopback addresses of the other leafs
- Adds both VXLAN devices (vni10 and vni20) to the default bridge br_default

{{< tabs "TabID122 ">}}
{{< tab "CUE Commands ">}}

{{< tabs "TabID125 ">}}
{{< tab "leaf01 ">}}

```
cumulus@leaf01:~$ cl set interface lo ip address 10.10.10.1/32
cumulus@leaf01:~$ cl set bridge domain br_default vlan 10 vni 10
cumulus@leaf01:~$ cl set bridge domain br_default vlan 10 vni 10 mac-learning on
cumulus@leaf01:~$ cl set bridge domain br_default vlan 20 vni 20
cumulus@leaf01:~$ cl set bridge domain br_default vlan 20 vni 20 mac-learning on
cumulus@leaf01:~$ cl set nve vxlan source address 10.10.10.1
cumulus@leaf01:~$ cl set bridge domain br_default vlan 10 vni 10 flooding head-end-replication 10.10.10.2
cumulus@leaf01:~$ cl set bridge domain br_default vlan 10 vni 10 flooding head-end-replication 10.10.10.3
cumulus@leaf01:~$ cl set bridge domain br_default vlan 10 vni 10 flooding head-end-replication 10.10.10.4
cumulus@leaf01:~$ cl set bridge domain br_default vlan 20 vni 20 flooding head-end-replication 10.10.10.2
cumulus@leaf01:~$ cl set bridge domain br_default vlan 20 vni 20 flooding head-end-replication 10.10.10.3
cumulus@leaf01:~$ cl set bridge domain br_default vlan 20 vni 20 flooding head-end-replication 10.10.10.4
cumulus@leaf04:~$ cl set interface swp1 bridge domain br_default access 10
cumulus@leaf04:~$ cl set interface swp2 bridge domain br_default access 20
cumulus@leaf01:~$ cl config apply
```

{{< /tab >}}
{{< tab "leaf02 ">}}

```
cumulus@leaf02:~$ cl set interface lo ip address 10.10.10.2/32
cumulus@leaf02:~$ cl set bridge domain br_default vlan 10 vni 10
cumulus@leaf02:~$ cl set bridge domain br_default vlan 10 vni 10 mac-learning on
cumulus@leaf02:~$ cl set bridge domain br_default vlan 20 vni 20
cumulus@leaf02:~$ cl set bridge domain br_default vlan 20 vni 20 mac-learning on
cumulus@leaf02:~$ cl set nve vxlan source address 10.10.10.2
cumulus@leaf02:~$ cl set bridge domain br_default vlan 10 vni 10 flooding head-end-replication 10.10.10.1
cumulus@leaf02:~$ cl set bridge domain br_default vlan 10 vni 10 flooding head-end-replication 10.10.10.3
cumulus@leaf02:~$ cl set bridge domain br_default vlan 10 vni 10 flooding head-end-replication 10.10.10.4
cumulus@leaf02:~$ cl set bridge domain br_default vlan 20 vni 20 flooding head-end-replication 10.10.10.1
cumulus@leaf02:~$ cl set bridge domain br_default vlan 20 vni 20 flooding head-end-replication 10.10.10.3
cumulus@leaf02:~$ cl set bridge domain br_default vlan 20 vni 20 flooding head-end-replication 10.10.10.4
cumulus@leaf04:~$ cl set interface swp1 bridge domain br_default access 10
cumulus@leaf04:~$ cl set interface swp2 bridge domain br_default access 20
cumulus@leaf02:~$ cl config apply
```

{{< /tab >}}
{{< tab "leaf03 ">}}

```
cumulus@leaf03:~$ cl set interface lo ip address 10.10.10.3/32
cumulus@leaf03:~$ cl set bridge domain br_default vlan 10 vni 10
cumulus@leaf03:~$ cl set bridge domain br_default vlan 10 vni 10 mac-learning on
cumulus@leaf03:~$ cl set bridge domain br_default vlan 20 vni 20
cumulus@leaf03:~$ cl set bridge domain br_default vlan 20 vni 20 mac-learning on
cumulus@leaf03:~$ cl set nve vxlan source address 10.10.10.3
cumulus@leaf03:~$ cl set bridge domain br_default vlan 10 vni 10 flooding head-end-replication 10.10.10.1
cumulus@leaf03:~$ cl set bridge domain br_default vlan 10 vni 10 flooding head-end-replication 10.10.10.2
cumulus@leaf03:~$ cl set bridge domain br_default vlan 10 vni 10 flooding head-end-replication 10.10.10.4
cumulus@leaf03:~$ cl set bridge domain br_default vlan 20 vni 20 flooding head-end-replication 10.10.10.1
cumulus@leaf03:~$ cl set bridge domain br_default vlan 20 vni 20 flooding head-end-replication 10.10.10.2
cumulus@leaf03:~$ cl set bridge domain br_default vlan 20 vni 20 flooding head-end-replication 10.10.10.4
cumulus@leaf04:~$ cl set interface swp1 bridge domain br_default access 10
cumulus@leaf04:~$ cl set interface swp2 bridge domain br_default access 20
cumulus@leaf03:~$ cl config apply
```

{{< /tab >}}
{{< tab "leaf04 ">}}

```
cumulus@leaf04:~$ cl set interface lo ip address 10.10.10.4/32
cumulus@leaf04:~$ cl set bridge domain br_default vlan 10 vni 10
cumulus@leaf04:~$ cl set bridge domain br_default vlan 10 vni 10 mac-learning on
cumulus@leaf04:~$ cl set bridge domain br_default vlan 20 vni 20
cumulus@leaf04:~$ cl set bridge domain br_default vlan 20 vni 20 mac-learning on
cumulus@leaf04:~$ cl set nve vxlan source address 10.10.10.4
cumulus@leaf04:~$ cl set bridge domain br_default vlan 10 vni 10 flooding head-end-replication 10.10.10.1
cumulus@leaf04:~$ cl set bridge domain br_default vlan 10 vni 10 flooding head-end-replication 10.10.10.2
cumulus@leaf04:~$ cl set bridge domain br_default vlan 10 vni 10 flooding head-end-replication 10.10.10.3
cumulus@leaf04:~$ cl set bridge domain br_default vlan 20 vni 20 flooding head-end-replication 10.10.10.1
cumulus@leaf04:~$ cl set bridge domain br_default vlan 20 vni 20 flooding head-end-replication 10.10.10.2
cumulus@leaf04:~$ cl set bridge domain br_default vlan 20 vni 20 flooding head-end-replication 10.10.10.3
cumulus@leaf04:~$ cl set interface swp1 bridge domain br_default access 10
cumulus@leaf04:~$ cl set interface swp2 bridge domain br_default access 20
cumulus@leaf04:~$ cl config apply
```

{{< /tab >}}
{{< /tabs >}}

{{< /tab >}}
{{< tab "Linux Commands ">}}

Editing the `/etc/network/interfaces` file as follows:

{{< tabs "TabID217 ">}}
{{< tab "leaf01 ">}}

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

auto br_default
iface br_default
    bridge-ports swp1 swp2 vni10 vni20
    bridge-vlan-aware yes
    bridge-vids 10 20
    bridge-pvid 1
```

{{< /tab >}}
{{< tab "leaf02 ">}}

```
auto lo
iface lo inet loopback
    address 10.10.10.2/32
    vxlan-local-tunnelip 10.10.10.2

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

auto vni10
iface vni10
    bridge-access 10
    vxlan-remoteip 10.10.10.1
    vxlan-remoteip 10.10.10.3
    vxlan-remoteip 10.10.10.4
    vxlan-id 10

auto vni20
iface vni20
    bridge-access 20
    vxlan-remoteip 10.10.10.1
    vxlan-remoteip 10.10.10.3
    vxlan-remoteip 10.10.10.4
    vxlan-id 20

auto br_default
iface br_default
    bridge-ports swp1 swp2 vni10 vn20
    bridge-vlan-aware yes
    bridge-vids 10 20
    bridge-pvid 1
```

{{< /tab >}}
{{< tab "leaf03 ">}}

```
auto lo
iface lo inet loopback
    address 10.10.10.3/32
    vxlan-local-tunnelip 10.10.10.3

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

auto vni10
iface vni10
    bridge-access 10
    vxlan-remoteip 10.10.10.1
    vxlan-remoteip 10.10.10.2
    vxlan-remoteip 10.10.10.4
    vxlan-id 10

auto vni20
iface vni20
    bridge-access 20
    vxlan-remoteip 10.10.10.1
    vxlan-remoteip 10.10.10.2
    vxlan-remoteip 10.10.10.4
    vxlan-id 20

auto br_default
iface br_default
    bridge-ports swp1 swp2 vni10 vni20
    bridge-vlan-aware yes
    bridge-vids 10 20
    bridge-pvid 1
```

{{< /tab >}}
{{< tab "leaf04 ">}}

```
auto lo
iface lo inet loopback
    address 10.10.10.4/32
    vxlan-local-tunnelip 10.10.10.3

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

auto vni10
iface vni10
    bridge-access 10
    vxlan-remoteip 10.10.10.1
    vxlan-remoteip 10.10.10.2
    vxlan-remoteip 10.10.10.3
    vxlan-id 10

auto vni20
iface vni20
    bridge-access 20
    vxlan-remoteip 10.10.10.1
    vxlan-remoteip 10.10.10.2
    vxlan-remoteip 10.10.10.3
    vxlan-id 20

auto br_default
iface br_default
    bridge-ports swp1 swp2 vni10 vn20
    bridge-vlan-aware yes
    bridge-vids 10 20
    bridge-pvid 1
```

{{< /tab >}}
{{< /tabs >}}

{{< /tab >}}
{{< /tabs >}}

## Verify the Configuration

After you configure all the leafs, run the following command to check for replication entries:

```
cumulus@leaf01:~$ sudo bridge fdb show | grep 00:00:00:00:00:00
00:00:00:00:00:00 dev vni-10 dst 10.10.10.4 self permanent
00:00:00:00:00:00 dev vni-10 dst 10.10.10.2 self permanent
00:00:00:00:00:00 dev vni-10 dst 10.10.10.3 self permanent
```

{{%notice note%}}
In Cumulus Linux, bridge learning is disabled and ARP suppression is enabled by default on VXLAN interfaces. You can change the default behavior to set bridge learning on and ARP suppression off for all VNIs by creating a policy file called `bridge.json` in the `/etc/network/ifupdown2/policy.d/` directory. For example:

```
cumulus@leaf01:~$ sudo cat /etc/network/ifupdown2/policy.d/bridge.json
{
    "bridge": {
        "module_globals": {
            "bridge_vxlan_port_learning" : "on",
            "bridge-vxlan-arp-nd-suppress" : "off"
        }
    }
}
```

After you create the file, run `ifreload -a` to load the new configuration.
{{%/notice%}}
