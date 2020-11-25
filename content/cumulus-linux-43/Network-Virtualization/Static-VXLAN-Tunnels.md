---
title: Static VXLAN Tunnels
author: Cumulus Networks
weight: 620
toc: 3
---
In VXLAN-based networks, there are a range of complexities and challenges in determining the destination *virtual tunnel endpoints* (VTEPs) for any given VXLAN. At scale, various solutions, including controller-based options like {{<link url="Integrating-Hardware-VTEPs-with-Midokura-MidoNet-and-OpenStack" text="Midokura MidoNet">}} or {{<link url="Integrating-Hardware-VTEPs-with-VMware-NSX-MH" text="VMware NSX">}} and even new standards like {{<link url="Ethernet-Virtual-Private-Network-EVPN" text="EVPN">}} try to address these complexities, however, they also have their own complexities.

*Static VXLAN tunnels* serve to connect two VTEPs in a given environment. Static VXLAN tunnels are the simplest deployment mechanism for small scale environments and are interoperable with other vendors that adhere to VXLAN standards. Because you simply map which VTEPs are in a particular VNI, you can avoid the tedious process of defining connections to every VLAN on every other VTEP on every other rack.

## Requirements

Cumulus Networks supports static VXLAN tunnels only on switches in the {{<exlink url="https://cumulusnetworks.com/hcl/" text="Cumulus Linux HCL">}} that use the Mellanox Spectrum ASICs or the Broadcom Tomahawk, Trident II+, Trident II, Trident3, and Maverick ASICs.

For a basic VXLAN configuration, make sure that:

- The VXLAN has a network identifier (VNI). Do not use VNI ID 0 or 16777215; these are reserved values under Cumulus Linux.
- Bridge learning must be enabled on the VNI (bridge learning is disabled by default).
- The VXLAN link and local interfaces are added to the bridge to create the association between the port, VLAN and VXLAN instance.
- Each traditional mode bridge on the switch has only one VXLAN interface. Cumulus Linux does not support more than one VXLAN ID per traditional bridge.

  {{%notice note%}}

This limitation only affects a traditional mode bridge configuration. Cumulus Linux supports *more* than one VXLAN ID in VLAN-aware bridge mode.

{{%/notice%}}

## Example Topology

The following topology is used in this chapter. Each IP address corresponds to the loopback address of the switch.

{{< img src = "/images/cumulus-linux/static-vxlan-tunnels.png" >}}

## Configure Static VXLAN Tunnels

To configure static VXLAN tunnels, do the following on each leaf:

- Specify an IP address for the loopback.
- Create a VXLAN interface using the loopback address for the local tunnel IP address.
- Enable bridge learning on the VNI.
- Create the tunnels by configuring the remote IP address to each other leaf switch's loopback address.

For example, to configure static VXLAN tunnels on the four leafs in the topology shown above:

{{< tabs "TabID45 ">}}

{{< tab "NCLU Commands ">}}

Run the following commands on **leaf01**:

```
cumulus@leaf01:~$ net add loopback lo ip address 10.0.0.11/32
cumulus@leaf01:~$ net add vxlan vni-10 vxlan id 10
cumulus@leaf01:~$ net add vxlan vni-10 bridge learning on
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
cumulus@leaf02:~$ net add vxlan vni-10 bridge learning on
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
cumulus@leaf03:~$ net add vxlan vni-10 bridge learning on
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
cumulus@leaf04:~$ net add vxlan vni-10 bridge learning on
cumulus@leaf04:~$ net add vxlan vni-10 vxlan local-tunnelip 10.0.0.14
cumulus@leaf04:~$ net add vxlan vni-10 vxlan remoteip 10.0.0.11
cumulus@leaf04:~$ net add vxlan vni-10 vxlan remoteip 10.0.0.12
cumulus@leaf04:~$ net add vxlan vni-10 vxlan remoteip 10.0.0.13
cumulus@leaf04:~$ net add vxlan vni-10 bridge access 10
cumulus@leaf04:~$ net pending
cumulus@leaf04:~$ net commit
```

{{< /tab >}}

{{< tab "Linux Commands ">}}

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
    bridge-learning on
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
    bridge-learning on
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
   bridge-learning on
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
    bridge-learning on
```

{{< /tab >}}

{{< /tabs >}}

## Verify the Configuration

After you configure all the leaf switches, run the following command to check for replication entries:

```
cumulus@leaf01:~$ sudo bridge fdb show | grep 00:00:00:00:00:00
00:00:00:00:00:00 dev vni-10 dst 10.0.0.14 self permanent
00:00:00:00:00:00 dev vni-10 dst 10.0.0.12 self permanent
00:00:00:00:00:00 dev vni-10 dst 10.0.0.13 self permanent
```

{{%notice note%}}

In Cumulus Linux, bridge learning is disabled and ARP suppression is enabled by default. You can change the default behavior to set bridge learning on and ARP suppression off for all VNIs by creating a policy file called `bridge.json` in the `/etc/network/ifupdown2/policy.d/` directory. For example:

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

## Control Link-local Multicast across a Static VXLAN Tunnel

By default, when you configure static VXLAN tunnels, Cumulus Linux forwards link-local multicast packets to the CPU and floods the ASIC. Cumulus Linux 3.7.12 and later provides a configuration option on Broadcom switches to disable forwarding of link-local multicast packets to the CPU so that such packets only flood the ASIC, which reduces CPU usage.

To disable forwarding of link local multicast packets to the CPU on a Broadcom switch, run the following command:

```
cumulus@switch:~$ echo TRUE > /cumulus/switchd/config/hal/bcm/ll_mcast_punt_disable
```

The configuration above takes effect immediately, but does not persist if you reboot the switch.

To apply the configuration so that it is persistent, edit the `/etc/cumulus/switchd.conf` file and uncomment the `hal.bcm.ll_mcast_punt_disable = TRUE` option. For example:

```
cumulus@switch:~$ sudo nano /etc/cumulus/switchd.conf
#
# /etc/cumulus/switchd.conf - switchd configuration file
#
...
# Bridge L2MC Link-Local multicast punt disable
hal.bcm.ll_mcast_punt_disable = TRUE
...
```

A `switchd` restart is **not** required.
