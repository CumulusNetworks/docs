---
title: Static VXLAN Tunnels
author: Cumulus Networks
weight: 149
aliases:
 - /display/DOCS/Static+VXLAN+Tunnels
 - /pages/viewpage.action?pageId=8366517
product: Cumulus Linux
version: '4.0'
---
In VXLAN-based networks, there are a range of complexities and challenges in determining the destination *virtual tunnel endpoints* (VTEPs) for any given VXLAN. At scale, various solutions, including controller-based options like [Midokura MidoNet](../Virtualization-Integrations/Integrating-Hardware-VTEPs-with-Midokura-MidoNet-and-OpenStack/) or [VMware NSX](../Virtualization-Integrations/Integrating-Hardware-VTEPs-with-VMware-NSX-MH/) and even new standards like [EVPN](../Ethernet-Virtual-Private-Network-EVPN/) try to address these complexities, however, they also have their own complexities.

S*tatic VXLAN tunnels* serve to connect two VTEPs in a given environment. Static VXLAN tunnels are the simplest deployment mechanism for small scale environments and are interoperable with other vendors that adhere to VXLAN standards. Because you simply map which VTEPs are in a particular VNI, you can avoid the tedious process of defining connections to every VLAN on every other VTEP on every other rack.

## Requirements

Cumulus Networks supports static VXLAN tunnels only on switches in the [Cumulus Linux HCL](http://cumulusnetworks.com/hcl/) that use the Broadcom Tomahawk, Trident II+, Trident II, Trident3, and Maverick and Mellanox Spectrum ASICs.

For a basic VXLAN configuration, make sure that:

- The VXLAN has a network identifier (VNI). Do not use VNI ID 0 or 16777215; these are reserved values under Cumulus Linux.
- The VXLAN link and local interfaces are added to the bridge to create the association between the port, VLAN, and VXLAN instance.
- Each traditional bridge on the switch has only one VXLAN interface. Cumulus Linux does not support more than one VXLAN ID per traditional bridge.

    {{%notice note%}}

This limitation only affects a traditional bridge configuration. Cumulus Linux supports *more* than one VXLAN ID per VLAN-aware bridge.

    {{%/notice%}}

## Example Configuration

The following topology is used in this chapter. Each IP address corresponds to the loopback address of the switch.

{{< img src = "/images/cumulus-linux/static-vxlan-tunnels.png" >}}

## Configure Static VXLAN Tunnels

To configure static VXLAN tunnels, do the following on each leaf:

- Specify an IP address for the loopback
- Create a VXLAN interface using the loopback address for the local tunnel IP address
- Create the tunnels by configuring the remote IP address to each other leaf switch's loopback address

For example, to configure static VXLAN tunnels on the four leafs in the topology shown above:

<details>

<summary>NCLU Commands </summary>

Run the following commands on **leaf01**:

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

Run these commands on leaf02, leaf03, and leaf04:

**leaf02**

```
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

**leaf03**

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

**leaf04**

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

</details>

<details>

<summary>Linux Commands </summary>

Configure **leaf01** by editing the `/etc/network/interfaces` file as follows:

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

Configure leaf02, leaf03, and leaf04 as follows:

**leaf02**

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

**leaf03**

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

**leaf04**

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

After you configure all the leaf switches, run the following command to check for replication entries:

```
cumulus@leaf01:~$ sudo bridge fdb show | grep 00:00:00:00:00:00
00:00:00:00:00:00 dev vni-10 dst 10.0.0.14 self permanent
00:00:00:00:00:00 dev vni-10 dst 10.0.0.12 self permanent
00:00:00:00:00:00 dev vni-10 dst 10.0.0.13 self permanent
```

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
