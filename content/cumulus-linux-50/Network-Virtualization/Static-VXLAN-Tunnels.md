---
title: Static VXLAN Tunnels
author: NVIDIA
weight: 620
toc: 3
---
In VXLAN-based networks, there are a range of complexities and challenges in determining the destination *virtual tunnel endpoints* (VTEPs) for any given VXLAN. At scale, various solutions, including controller-based options, such as VMware NSX and even new standards like {{<link url="Ethernet-Virtual-Private-Network-EVPN" text="EVPN">}} try to address these complexities, however, they also have their own complexities.

*Static VXLAN tunnels* serve to connect two VTEPs in a given environment. Static VXLAN tunnels are the simplest deployment mechanism for small scale environments and are interoperable with other vendors that adhere to VXLAN standards. Because you simply map which VTEPs are in a particular VNI, you can avoid the tedious process of defining connections to every VLAN on every other VTEP on every other rack.

## Requirements

For a basic VXLAN configuration, make sure that:

- The VXLAN has a network identifier (VNI). Do not use VNI ID 0 or 16777215; these are reserved values under Cumulus Linux.
- Bridge learning must be enabled on the VNI (bridge learning is disabled by default).
- The VXLAN link and local interfaces are added to the bridge to create the association between the port, VLAN, and VXLAN instance.
- Each traditional mode bridge on the switch has only one VXLAN interface. Cumulus Linux does not support more than one VXLAN ID per traditional bridge.

  {{%notice note%}}
This limitation only affects a traditional mode bridge configuration. Cumulus Linux supports *more* than one VXLAN ID in VLAN-aware bridge mode.
{{%/notice%}}

## Example Topology

The following topology is used in this chapter. Each IP address corresponds to the loopback address of the switch.

{{< img src = "/images/cumulus-linux/static-vxlan-tunnel-example.png" >}}

## Configure Static VXLAN Tunnels

To configure static VXLAN tunnels, do the following on each leaf:

- Specify an IP address for the loopback.
- Create a VXLAN interface using the loopback address for the local tunnel IP address.
- Enable bridge learning on the VNI.
- Create the tunnels by configuring the remote IP address to be the loopback address of the other leafs.

For example, to configure static VXLAN tunnels on the four leafs in the topology shown above:

{{< tabs "TabID41 ">}}
{{< tab "CUE Commands ">}}

{{< tabs "TabID44 ">}}
{{< tab "leaf01 ">}}

```
cumulus@leaf01:~$ cl set interface lo ip address 10.10.10.1/32
cumulus@leaf01:~$ cl set bridge domain br_default vlan 10 vni 10
cumulus@leaf01:~$ cl set bridge domain br_default vlan 10 vni 10 mac-learning on
cumulus@leaf01:~$ cl set nve vxlan source address 10.10.10.1
cumulus@leaf01:~$ cl set bridge domain br_default vlan 10 vni 10 flooding head-end-replication 10.10.10.2
cumulus@leaf01:~$ cl set bridge domain br_default vlan 10 vni 10 flooding head-end-replication 10.10.10.3
cumulus@leaf01:~$ cl set bridge domain br_default vlan 10 vni 10 flooding head-end-replication 10.10.10.4
cumulus@leaf01:~$ cl set interface swp1 bridge domain br_default access 10
cumulus@leaf01:~$ cl config apply
```

{{< /tab >}}
{{< tab "leaf02 ">}}

```
cumulus@leaf01:~$ cl set interface lo ip address 10.10.10.2/32
cumulus@leaf01:~$ cl set bridge domain br_default vlan 10 vni 10
cumulus@leaf01:~$ cl set bridge domain br_default vlan 10 vni 10 mac-learning on
cumulus@leaf01:~$ cl set nve vxlan source address 10.10.10.2
cumulus@leaf01:~$ cl set bridge domain br_default vlan 10 vni 10 flooding head-end-replication 10.10.10.1
cumulus@leaf01:~$ cl set bridge domain br_default vlan 10 vni 10 flooding head-end-replication 10.10.10.3
cumulus@leaf01:~$ cl set bridge domain br_default vlan 10 vni 10 flooding head-end-replication 10.10.10.4
cumulus@leaf01:~$ cl set interface swp1 bridge domain br_default access 10
cumulus@leaf01:~$ cl config apply
```

{{< /tab >}}
{{< tab "leaf03 ">}}

```
cumulus@leaf01:~$ cl set interface lo ip address 10.10.10.3/32
cumulus@leaf01:~$ cl set bridge domain br_default vlan 10 vni 10
cumulus@leaf01:~$ cl set bridge domain br_default vlan 10 vni 10 mac-learning on
cumulus@leaf01:~$ cl set nve vxlan source address 10.10.10.3
cumulus@leaf01:~$ cl set bridge domain br_default vlan 10 vni 10 flooding head-end-replication 10.10.10.1
cumulus@leaf01:~$ cl set bridge domain br_default vlan 10 vni 10 flooding head-end-replication 10.10.10.2
cumulus@leaf01:~$ cl set bridge domain br_default vlan 10 vni 10 flooding head-end-replication 10.10.10.4
cumulus@leaf01:~$ cl set interface swp1 bridge domain br_default access 10
cumulus@leaf01:~$ cl config apply
```

{{< /tab >}}
{{< tab "leaf04 ">}}

```
cumulus@leaf01:~$ cl set interface lo ip address 10.10.10.4/32
cumulus@leaf01:~$ cl set bridge domain br_default vlan 10 vni 10
cumulus@leaf01:~$ cl set bridge domain br_default vlan 10 vni 10 mac-learning on
cumulus@leaf01:~$ cl set nve vxlan source address 10.10.10.4
cumulus@leaf01:~$ cl set bridge domain br_default vlan 10 vni 10 flooding head-end-replication 10.10.10.1
cumulus@leaf01:~$ cl set bridge domain br_default vlan 10 vni 10 flooding head-end-replication 10.10.10.2
cumulus@leaf01:~$ cl set bridge domain br_default vlan 10 vni 10 flooding head-end-replication 10.10.10.3
cumulus@leaf01:~$ cl set interface swp1 bridge domain br_default access 10
cumulus@leaf01:~$ cl config apply
```

{{< /tab >}}
{{< /tabs >}}

{{< /tab >}}
{{< tab "Linux Commands ">}}

Editing the `/etc/network/interfaces` file as follows:

{{< tabs "TabID134 ">}}
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

auto vni10
iface vni10
    bridge-access 10
    vxlan-remoteip 10.10.10.2
    vxlan-remoteip 10.10.10.3
    vxlan-remoteip 10.10.10.4
    vxlan-id 10

auto br_default
iface br_default
    bridge-ports swp1 vni10
    bridge-vlan-aware yes
    bridge-vids 10
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

auto vni10
iface vni10
    bridge-access 10
    vxlan-remoteip 10.10.10.1
    vxlan-remoteip 10.10.10.3
    vxlan-remoteip 10.10.10.4
    vxlan-id 10

auto br_default
iface br_default
    bridge-ports swp1 vni10
    bridge-vlan-aware yes
    bridge-vids 10
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

auto vni10
iface vni10
    bridge-access 10
    vxlan-remoteip 10.10.10.1
    vxlan-remoteip 10.10.10.2
    vxlan-remoteip 10.10.10.4
    vxlan-id 10

auto br_default
iface br_default
    bridge-ports swp1 vni10
    bridge-vlan-aware yes
    bridge-vids 10
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

auto vni10
iface vni10
    bridge-access 10
    vxlan-remoteip 10.10.10.1
    vxlan-remoteip 10.10.10.2
    vxlan-remoteip 10.10.10.3
    vxlan-id 10

auto br_default
iface br_default
    bridge-ports swp1 vni10
    bridge-vlan-aware yes
    bridge-vids 10
    bridge-pvid 1
```

{{< /tab >}}
{{< /tabs >}}

{{< /tab >}}
{{< /tabs >}}

## Verify the Configuration

After you configure all the leaf switches, run the following command to check for replication entries:

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
