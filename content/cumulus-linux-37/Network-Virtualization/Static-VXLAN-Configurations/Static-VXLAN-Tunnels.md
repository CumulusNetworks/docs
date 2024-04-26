---
title: Static VXLAN Tunnels
author: NVIDIA
weight: 363
pageID: 8362793
---
In VXLAN-based networks, there are a range of complexities and challenges in determining the destination *virtual tunnel endpoints* (VTEPs) for any given VXLAN. At scale, solutions such as {{<link url="Ethernet-Virtual-Private-Network-EVPN" text="EVPN">}} are attempts to address these complexities, however do retain their own complexities.

Enter *static VXLAN tunnels*, which simply serve to connect two VTEPs in a given environment. Static VXLAN tunnels are the simplest deployment mechanism for small scale environments and are interoperable with other vendors that adhere to VXLAN standards. Because you are simply mapping which VTEPs are in a particular VNI, you can avoid the tedious process of defining connections to every VLAN on every other VTEP on every other rack.

## Requirements

Static VXLAN tunnels are supported only on switches using the Broadcom Tomahawk, Trident II+, Trident II, and Maverick ASICs, as well as the Mellanox Spectrum ASIC.

For a basic VXLAN configuration, make sure that:

- The VXLAN has a network identifier (VNI); do not use 0 or 16777215 as the VNI ID, which are reserved values under Cumulus Linux.
- The VXLAN link and local interfaces are added to bridge to create the association between port, VLAN, and VXLAN instance.
- Each traditional bridge on the switch has only one VXLAN interface. Cumulus Linux does not support more than one VXLAN ID per traditional bridge.

    {{%notice note%}}

When deploying VXLAN with a VLAN-aware bridge, there is no restriction on using a single VNI. This limitation is only present when using the traditional bridge configuration.

{{%/notice%}}

- The VXLAN registration daemon (`vxrd`) is not running. Static VXLAN tunnels do not interoperate with LNV or EVPN. If `vxrd` is running, stop it with the following command:

```
cumulus@switch:~ sudo systemctl stop vxrd.service
```

## Example Configuration

This chapter uses the following topology. Each IP address corresponds to the loopback address of the switch.

{{% img src="/images/old_doc_images/static-vxlan-tunnels.png" %}}

## Configure Static VXLAN Tunnels

To configure static VXLAN tunnels, do the following for each leaf:

- Specify an IP address for the loopback
- Create a VXLAN interface using the loopback address for the local tunnel IP address
- Create the tunnels by configuring the remote IP address to each other leaf switch's loopback address

To configure leaf01, run the following commands:

```
cumulus@leaf01:~$ net add loopback lo ip address 10.0.0.11/32
cumulus@leaf01:~$ net add vxlan vni-10 vxlan id 10
cumulus@leaf01:~$ net add vxlan vni-10 vxlan local-tunnelip 10.0.0.11
cumulus@leaf01:~$ net add vxlan vni-10 vxlan remoteip 10.0.0.12
cumulus@leaf01:~$ net add vxlan vni-10 vxlan remoteip 10.0.0.13
cumulus@leaf01:~$ net add vxlan vni-10 vxlan remoteip 10.0.0.14
cumulus@leaf01:~$ net add vxlan vni-10 bridge access 10
cumulus@leaf01:~$ net pending
cumulus@leaf01:~$ net commit
```

These commands create the following configuration in the `/etc/network/interfaces` file:

```
# The loopback network interface
auto lo
iface lo inet loopback
    address 10.0.0.11/32
 
# The primary network interface
auto eth0
iface eth0 inet dhcp

auto swp1
iface swp1

auto swp2
iface swp2

auto bridge
iface bridge
    bridge-ports vni-10
    bridge-vids 10
    bridge-vlan-aware yes

auto vni-10
iface vni-10
    bridge-access 10
    mstpctl-bpduguard yes
    mstpctl-portbpdufilter yes
    vxlan-id 10
    vxlan-local-tunnelip 10.0.0.11
    vxlan-remoteip 10.0.0.12
    vxlan-remoteip 10.0.0.13
    vxlan-remoteip 10.0.0.14
```

Repeat these steps for leaf02, leaf03, and leaf04:

<details>

<summary>leaf02 </summary>

NCLU Commands

```
/etc/network/interfaces Configuration
cumulus@leaf02:~$ net add loopback lo ip address 10.0.0.12/32
cumulus@leaf02:~$ net add vxlan vni-10 vxlan id 10
cumulus@leaf02:~$ net add vxlan vni-10 vxlan local-tunnelip 10.0.0.12
cumulus@leaf02:~$ net add vxlan vni-10 vxlan remoteip 10.0.0.11
cumulus@leaf02:~$ net add vxlan vni-10 vxlan remoteip 10.0.0.13
cumulus@leaf02:~$ net add vxlan vni-10 vxlan remoteip 10.0.0.14
cumulus@leaf02:~$ net add vxlan vni-10 bridge access 10
cumulus@leaf02:~$ net pending
cumulus@leaf02:~$ net commit
```

/etc/network/interfaces Configuration

```
# The loopback network interface
auto lo
iface lo inet loopback
    address 10.0.0.12/32

# The primary network interface
auto eth0
iface eth0 inet dhcp

auto swp1
iface swp1

auto swp2
iface swp2

auto bridge
iface bridge
    bridge-ports vni-10
    bridge-vids 10
    bridge-vlan-aware yes

auto vni-10
iface vni-10
    bridge-access 10
    mstpctl-bpduguard yes
    mstpctl-portbpdufilter yes
    vxlan-id 10
    vxlan-local-tunnelip 10.0.0.12
    vxlan-remoteip 10.0.0.11
    vxlan-remoteip 10.0.0.13
    vxlan-remoteip 10.0.0.14
```

</details>

<details>

<Summary>leaf03 </summary>

NCLU Commands

```
cumulus@leaf03:~$ net add loopback lo ip address 10.0.0.13/32
cumulus@leaf03:~$ net add vxlan vni-10 vxlan id 10
cumulus@leaf03:~$ net add vxlan vni-10 vxlan local-tunnelip 10.0.0.13
cumulus@leaf03:~$ net add vxlan vni-10 vxlan remoteip 10.0.0.11
cumulus@leaf03:~$ net add vxlan vni-10 vxlan remoteip 10.0.0.12
cumulus@leaf03:~$ net add vxlan vni-10 vxlan remoteip 10.0.0.14
cumulus@leaf03:~$ net add vxlan vni-10 bridge access 10
cumulus@leaf03:~$ net pending
cumulus@leaf03:~$ net commit
```

/etc/network/interfaces Configuration

```
# The loopback network interface
auto lo
iface lo inet loopback
    address 10.0.0.13/32

# The primary network interface
auto eth0
iface eth0 inet dhcp

auto swp1
iface swp1

auto swp2
iface swp2

auto bridge
iface bridge
    bridge-ports vni-10
    bridge-vids 10
    bridge-vlan-aware yes

auto vni-10
iface vni-10
    bridge-access 10
    mstpctl-bpduguard yes
    mstpctl-portbpdufilter yes
    vxlan-id 10
    vxlan-local-tunnelip 10.0.0.13
    vxlan-remoteip 10.0.0.11
    vxlan-remoteip 10.0.0.12
    vxlan-remoteip 10.0.0.14
```

</details>

<details>

<summary>leaf04</summary>

NCLU Commands

```
cumulus@leaf04:~$ net add loopback lo ip address 10.0.0.14/32
cumulus@leaf04:~$ net add vxlan vni-10 vxlan id 10
cumulus@leaf04:~$ net add vxlan vni-10 vxlan local-tunnelip 10.0.0.14
cumulus@leaf04:~$ net add vxlan vni-10 vxlan remoteip 10.0.0.11
cumulus@leaf04:~$ net add vxlan vni-10 vxlan remoteip 10.0.0.12
cumulus@leaf04:~$ net add vxlan vni-10 vxlan remoteip 10.0.0.13
cumulus@leaf04:~$ net add vxlan vni-10 bridge access 10
cumulus@leaf04:~$ net pending
cumulus@leaf04:~$ net commit
```

/etc/network/interfaces Configuration

```
# The loopback network interface
auto lo
iface lo inet loopback
    address 10.0.0.14/32

# The primary network interface
auto eth0
iface eth0 inet dhcp

auto swp1
iface swp1

auto swp2
iface swp2

auto bridge
iface bridge
    bridge-ports vni-10
    bridge-vids 10
    bridge-vlan-aware yes

auto vni-10
iface vni-10
    bridge-access 10
    mstpctl-bpduguard yes
    mstpctl-portbpdufilter yes
    vxlan-id 10
    vxlan-local-tunnelip 10.0.0.14
    vxlan-remoteip 10.0.0.11
    vxlan-remoteip 10.0.0.12
    vxlan-remoteip 10.0.0.13
```

</details>

## Verify the Configuration

After you configure all the leaf switches, check for replication entries:

```
cumulus@leaf01:~$ sudo bridge fdb show | grep 00:00:00:00:00:00
00:00:00:00:00:00 dev vni-10 dst 10.0.0.14 self permanent
00:00:00:00:00:00 dev vni-10 dst 10.0.0.12 self permanent
00:00:00:00:00:00 dev vni-10 dst 10.0.0.13 self permanent
```

## Control Link-local Multicast across a Static VXLAN Tunnel

By default, when you configure static VXLAN tunnels, Cumulus Linux forwards link-local multicast packets to the CPU and floods the ASIC. Cumulus Linux 3.7.12 and later provides a configuration option on Broadcom switches to disable forwarding of link-local multicast packets to the CPU so that such packets only flood the ASIC, which reduces CPU usage.

To disable forwarding of link local multicast packets to the CPU on a Broadcom switch, run the following command:

```
cumulus@switch:~$ echo TRUE > /cumulus/switchd/config/hal/bcm/ll_mcast_punt_disable
```

The configuration above takes effect immediately, but does not persist if you reboot the switch. A persistent configuration will be available in a future release.

## Caveats and Errata

Cumulus Linux does not support different `bridge-learning` settings for different VNIs of VXLAN tunnels between 2 VTEPs. For example, the following configuration in the `/etc/network/interfaces` file is *not* supported.

```
...
auto vni300
iface vni300
vxlan-id 300
vxlan-local-tunnelip 10.252.255.58
vxlan-remoteip 10.250.255.161
mtu 9000

auto vni258
iface vni258
vxlan-id 258
vxlan-local-tunnelip 10.252.255.58
vxlan-remoteip 10.250.255.161
bridge-access 258
bridge-learning off
mtu 9000
```
