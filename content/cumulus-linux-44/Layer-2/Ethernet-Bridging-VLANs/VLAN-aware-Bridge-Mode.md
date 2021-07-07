---
title: VLAN-aware Bridge Mode
author: NVIDIA
weight: 430
toc: 4
---
VLAN-aware bridge mode in Cumulus Linux implements a configuration model for large-scale layer 2 environments, with *one single instance* of {{<link url="Spanning-Tree-and-Rapid-Spanning-Tree-STP" text="spanning tree protocol">}}. Each physical bridge member port is configured with the list of allowed VLANs as well as its port VLAN ID, either primary VLAN Identifier (PVID) or native VLAN. MAC address learning, filtering and forwarding are *VLAN-aware*. This significantly reduces the configuration size, and eliminates the large overhead of managing the port and VLAN instances as subinterfaces, replacing them with lightweight VLAN bitmaps and state updates.

On NVIDIA Spectrum-2 and Spectrum-3 switches, Cumulus Linux supports multiple VLAN-aware bridges but with the following limitations:

- MLAG is not supported with multiple VLAN-aware bridges
- The same port cannot be part of multiple VLAN-aware bridges
- The same VNIs cannot appear in multiple VLAN-aware bridges
- VLAN translation is not supported with multiple VLAN-aware bridges
- Double tagged VLAN interfaces are not supported with multiple VLAN-aware bridges
- You cannot associate multiple single VXLAN devices (SVDs) with a single VLAN-aware bridge
- IGMPv3 is not supported

## Configure a VLAN-aware Bridge

The example below shows the commands required to create a VLAN-aware bridge configured for STP that contains two switch ports and includes 3 VLANs; tagged VLANs 10 and 20, and untagged (native) VLAN 1.

{{< img src = "/images/cumulus-linux/ethernet-bridging-basic-trunking1.png" >}}

{{< tabs "TabID25 ">}}
{{< tab "NCLU Commands ">}}

```
cumulus@switch:~$ net add bridge bridge ports swp1-2
cumulus@switch:~$ net add bridge bridge vids 10,20
cumulus@switch:~$ net add bridge bridge pvid 1
cumulus@switch:~$ net pending
cumulus@switch:~$ net commit
```

The above commands create the following code snippet in the `/etc/network/interfaces` file:

```
auto bridge
iface bridge
    bridge-ports swp1 swp2
    bridge-pvid 1
    bridge-vids 10 20
    bridge-vlan-aware yes
```

{{< /tab >}}
{{< tab "NVUE Commands ">}}

With NVUE, there is a default bridge called `br_default`, which has no ports assigned to it. The example below configures this default bridge.

```
cumulus@switch:~$ nv set interface swp1-2 bridge domain br_default
cumulus@switch:~$ nv set bridge domain br_default vlan 10,20
cumulus@switch:~$ nv set bridge domain br_default untagged 1
cumulus@switch:~$ nv config apply
```

{{< /tab >}}
{{< tab "Linux Commands ">}}

Edit the `/etc/network/interfaces` file and add the bridge. An example configuration is shown below.

```
cumulus@switch:~$ sudo nano /etc/network/interfaces
...
auto br_default
iface br_default
    bridge-ports swp1 swp2
    bridge-vids 10 20
    bridge-pvid 1
    bridge-vlan-aware yes
...
```

Run the `ifreload -a` command to load the new configuration:

```
cumulus@switch:~$ ifreload -a
```

{{< /tab >}}
{{< /tabs >}}

The Primary VLAN Identifer (PVID) of the bridge defaults to 1. You do *not* have to specify `bridge-pvid` for a bridge or a port. However, even though this does not affect the configuration, it helps other users for readability. The following configurations are identical to each other and the configuration above:

```
auto br_default
iface br_default
    bridge-ports swp1 swp2
    bridge-vids 1 10 20
    bridge-vlan-aware yes
```

```
auto br_default
iface br_default
    bridge-ports swp1 swp2
    bridge-pvid 1
    bridge-vids 1 10 20
    bridge-vlan-aware yes
```

```
auto br_default
iface br_default
    bridge-ports swp1 swp2
    bridge-vids 10 20
    bridge-vlan-aware yes
```

{{%notice note%}}
- If you specify `bridge-vids` or `bridge-pvid` at the bridge level, these configurations are inherited by all ports in the bridge. However, specifying any of these settings for a specific port overrides the setting in the bridge.
- Do not bridge the management port eth0 with any switch ports. For example, if you create a bridge with eth0 and swp1, the bridge does not work correctly and might disrupt access to the management interface.
{{%/notice%}}

## Configure Multiple VLAN-aware Bridges

This example shows the commands required to create two VLAN-aware bridges on the switch.

{{< img src = "/images/cumulus-linux/ethernet-bridging-vmvab.png" >}}

- bridge1 bridges swp1 and swp2, and includes 2 VLANs; vlan 10 and vlan 20
- bridge2 bridges swp3 and contains one VLAN; vlan 10

Bridges are independent so you can reuse VLANs between bridges. Each VLAN-aware bridge maintains its own MAC address and VLAN tag table; MAC and VLAN tags in one bridge are not visibile to the other table.

{{< tabs "TabID128 ">}}
{{< tab "NCLU Commands ">}}

```
cumulus@switch:~$ net add bridge bridge1 ports swp1-2
cumulus@switch:~$ net add bridge bridge1 vids 10,20
cumulus@switch:~$ net add bridge bridge1 pvid 1
cumulus@switch:~$ net add bridge bridge2 ports swp3
cumulus@switch:~$ net add bridge bridge2 vids 10
cumulus@switch:~$ net add bridge bridge2 pvid 1
cumulus@switch:~$ net pending
cumulus@switch:~$ net commit
```

{{< /tab >}}
{{< tab "NVUE Commands ">}}

```
cumulus@switch:~$ nv set interface swp1-2 bridge domain bridge1
cumulus@switch:~$ nv set bridge domain bridge1 vlan 10,20
cumulus@switch:~$ nv set bridge domain bridge1 untagged 1
cumulus@switch:~$ nv set interface swp3 bridge domain bridge2
cumulus@switch:~$ nv set bridge domain bridge2 vlan 10
cumulus@switch:~$ nv set bridge domain bridge2 untagged 1
cumulus@switch:~$ nv config apply
```

{{< /tab >}}
{{< tab "Linux Commands ">}}

Edit the `/etc/network/interfaces` file and add the bridge. An example configuration is shown below.

```
cumulus@switch:~$ sudo nano /etc/network/interfaces
...
auto bridge1
iface bridge1
    bridge-ports swp1 swp2
    bridge-vlan-aware yes
    bridge-vids 10 20
    bridge-pvid 1

auto bridge2
iface bridge2
    bridge-ports swp3
    bridge-vlan-aware yes
    bridge-vids 10
    bridge-pvid 1
...
```

Run the `ifreload -a` command to load the new configuration:

```
cumulus@switch:~$ ifreload -a
```

{{< /tab >}}
{{< /tabs >}}

{{%notice note%}}
NVIDIA Spectrum switches currently support a maximum of 6000 VLAN elements. The total number of VLAN elements is calculated as the number of VLANs times the number of bridges configured. For example, 6 bridges, each containing 1000 VLANS totals 6000 VLAN elements.
{{%/notice%}}

## Reserved VLAN Range

For hardware data plane internal operations, the switching silicon requires VLANs for every physical port, Linux bridge, and layer 3 subinterface. Cumulus Linux reserves a range of VLANs by default; the reserved range is 3725-3999.

{{%notice tip%}}
If the reserved VLAN range conflicts with any user-defined VLANs, you can modify the range. The new range must be a contiguous set of VLANs with IDs between 32 and 4094. For a single VLAN-aware bridge, the minimum size of the range is 32 VLANs.
{{%/notice%}}

To configure the reserved range, edit the `/etc/cumulus/switchd.conf` file to uncomment the `resv_vlan_range` line and specify a new range. After you save the file, you must restart `switchd`.

## VLAN Pruning

By default, the bridge port inherits the bridge VIDs, however, you can configure a port to override the bridge VIDs.

{{< img src = "/images/cumulus-linux/ethernet-bridging-vlan-pruned1.png" >}}

This example commands configure swp3 to override the bridge VIDs:

{{< tabs "TabID157 ">}}
{{< tab "NCLU Commands ">}}

```
cumulus@switch:~$ net add bridge bridge ports swp1-3
cumulus@switch:~$ net add bridge bridge vids 10,20
cumulus@switch:~$ net add bridge bridge pvid 1
cumulus@switch:~$ net add interface swp3 bridge vids 20
cumulus@switch:~$ net pending
cumulus@switch:~$ net commit
```

{{< /tab >}}
{{< tab "NVUE Commands ">}}

```
cumulus@switch:~$ nv set interface swp1-3 bridge domain br_default
cumulus@switch:~$ nv set bridge domain br_default vlan 10,20
cumulus@switch:~$ nv set bridge domain br_default untagged 1
cumulus@switch:~$ nv set interface swp3 bridge domain br_default vlan 20
cumulus@switch:~$ nv config apply
```

{{< /tab >}}
{{< tab "Linux Commands ">}}

Edit the `/etc/network/interfaces` file, then run the `ifreload -a` command. The following example commands configure swp3 to override the bridge VIDs:

```
cumulus@switch:~$ sudo nano /etc/network/interfaces
...
auto br_default
iface br_default
    bridge-ports swp1 swp2 swp3
    bridge-pvid 1
    bridge-vids 10 20
    bridge-vlan-aware yes

auto swp3
iface swp3
  bridge-vids 20
...
```

```
cumulus@switch:~$ ifreload -a
```

{{< /tab >}}
{{< /tabs >}}

## Access Ports and Tagged Packets

Access ports ignore all tagged packets. In the configuration below, swp1 and swp2 are configured as access ports, while all untagged traffic goes to VLAN 10:

{{< img src = "/images/cumulus-linux/ethernet-bridging-vlan_untagged_access_ports1.png" >}}

{{< tabs "TabID223 ">}}
{{< tab "NCLU Commands ">}}

```
cumulus@switch:~$ net add bridge bridge ports swp1-2
cumulus@switch:~$ net add bridge bridge vids 10,20
cumulus@switch:~$ net add bridge bridge pvid 1
cumulus@switch:~$ net add interface swp1 bridge access 10
cumulus@switch:~$ net add interface swp2 bridge access 10
cumulus@switch:~$ net pending
cumulus@switch:~$ net commit
```

{{< /tab >}}
{{< tab "NVUE Commands ">}}

```
cumulus@switch:~$ nv set interface swp1-2 bridge domain br_default
cumulus@switch:~$ nv set bridge domain br_default vlan 10,20
cumulus@switch:~$ nv set bridge domain br_default untagged 1
cumulus@switch:~$ nv set interface swp1 bridge domain br_default access 10
cumulus@switch:~$ nv set interface swp2 bridge domain br_default access 10
cumulus@switch:~$ nv config apply
```

{{< /tab >}}
{{< tab "Linux Commands ">}}

Edit the `/etc/network/interfaces` file, then run the `ifreload -a` command.

```
cumulus@switch:~$ sudo nano /etc/network/interfaces
...
auto br_default
iface br_default
    bridge-ports swp1 swp2
    bridge-pvid 1
    bridge-vids 10 20
    bridge-vlan-aware yes

auto swp1
iface swp1
    bridge-access 10

auto swp2
iface swp2
    bridge-access 10
...
```

```
cumulus@switch:~$ ifreload -a
```

{{< /tab >}}
{{< /tabs >}}

## Drop Untagged Frames

With VLAN-aware bridge mode, you can configure a switch port to drop any untagged frames. To do this, add `bridge-allow-untagged no` to the **switch port** (not to the bridge). This leaves the bridge port without a PVID and drops untagged packets.

The following example command configures swp2 to drop untagged frames:

{{< tabs "TabID294 ">}}
{{< tab "NCLU Commands ">}}

```
cumulus@switch:~$ net add interface swp2 bridge allow-untagged no
cumulus@switch:~$ net pending
cumulus@switch:~$ net commit 
```

{{< /tab >}}
{{< tab "NVUE Commands ">}}

```
cumulus@switch:~$ nv set interface swp2 bridge domain br_default untagged none
cumulus@switch:~$ nv config apply
```

{{< /tab >}}
{{< tab "Linux Commands ">}}

Edit the `/etc/network/interfaces` file to add the `bridge-allow-untagged no` line under the switch port interface stanza, then run the `ifreload -a` command.

```
cumulus@switch:~$ sudo nano /etc/network/interfaces
...
auto swp1
iface swp1

auto swp2
iface swp2
    bridge-allow-untagged no

auto br_default
iface br_default
    bridge-ports swp1 swp2
    bridge-pvid 1
    bridge-vids 10 20
    bridge-vlan-aware yes
...
```

```
cumulus@switch:~$ sudo ifreload -a
```

{{< /tab >}}
{{< /tabs >}}

When you check VLAN membership for that port, it shows that there is **no** untagged VLAN.

```
cumulus@switch:~$ bridge -c vlan show
portvlan ids
swp1 1 PVID Egress Untagged
  10 20

swp2 10 20

bridge 1
```

## VLAN Layer 3 Addressing

When configuring the VLAN attributes for the bridge, specify the attributes for each VLAN interface. If you are configuring the switch virtual interface (SVI) for the native VLAN, you must declare the native VLAN and specify its IP address. Specifying the IP address in the bridge stanza itself returns an error.

The following example commands declare native VLAN 10 with IPv4 address 10.1.10.2/24 and IPv6 address 2001:db8::1/32.

The NVUE and Linux commands also show an example with multiple VLAN-aware bridges.

{{< tabs "TabID370 ">}}
{{< tab "NCLU Commands ">}}

```
cumulus@switch:~$ net add vlan 10 ip address 10.1.10.2/24
cumulus@switch:~$ net add vlan 10 ipv6 address 2001:db8::1/32
cumulus@switch:~$ net pending
cumulus@switch:~$ net commit
```

{{< /tab >}}
{{< tab "NVUE Commands ">}}

{{< tabs "TabID419 ">}}
{{< tab "Single Bridge ">}}

```
cumulus@switch:~$ nv set interface vlan10 ip address 10.1.10.2/24
cumulus@switch:~$ nv set interface vlan10 ip address 2001:db8::1/32
cumulus@switch:~$ nv config apply
```

{{< /tab >}}
{{< tab "Multiple Bridges ">}}

```
cumulus@switch:~$ nv set interface bridge2_vlan10 type svi
cumulus@switch:~$ nv set interface bridge2_vlan10 vlan 10
cumulus@switch:~$ nv set interface bridge2_vlan10 base-interface bridge2
cumulus@switch:~$ nv set interface bridge2_vlan10 ip address 10.1.10.2/24
cumulus@switch:~$ nv set interface bridge1_vlan10 type svi
cumulus@switch:~$ nv set interface bridge1_vlan10 vlan 10
cumulus@switch:~$ nv set interface bridge1_vlan10 base-interface bridge1
cumulus@switch:~$ nv set interface bridge1_vlan10 ip address 12.1.10.2/24
cumulus@switch:~$ nv config apply
```

{{< /tab >}}
{{< /tabs >}}

{{< /tab >}}
{{< tab "Linux Commands ">}}

{{< tabs "TabID431 ">}}
{{< tab "Single Bridge ">}}

Edit the `/etc/network/interfaces` file, then run the `ifreload -a` command.

```
cumulus@switch:~$ sudo nano /etc/network/interfaces
...
auto bridge
iface bridge
    bridge-ports swp1 swp2
    bridge-pvid 1
    bridge-vids 10 20
    bridge-vlan-aware yes

auto vlan10
iface vlan10
    address 10.1.10.2/24
    address 2001:db8::1/32
    vlan-id 10
    vlan-raw-device br_default
```

```
cumulus@switch:~$ ifreload -a
```

{{< /tab >}}
{{< tab "Multiple Bridges ">}}

```
cumulus@switch:~$ sudo nano /etc/network/interfaces
...
auto bridge2_vlan10
iface bridge2_vlan10
    address 10.1.10.2/24
    hwaddress 1c:34:da:1d:e6:fd
    vlan-raw-device bridge2
    vlan-id 10

auto bridge1_vlan10
iface bridge1_vlan10
    address 12.1.10.2/24
    hwaddress 1c:34:da:1d:e6:fd
    vlan-raw-device bridge1
    vlan-id 10
```

{{< /tab >}}
{{< /tabs >}}

{{< /tab >}}
{{< /tabs >}}

When you configure a switch initially, all southbound bridge ports might be down; therefore, by default, the SVI is also down. You can force the SVI to always be up by disabling interface state tracking, which leaves the SVI in the UP state always, even if all member ports are down. Other implementations describe this feature as *no autostate*. This is beneficial if you want to perform connectivity testing.

To keep the SVI perpetually UP, create a dummy interface, then make the dummy interface a member of the bridge.

{{< expand "Example Configuration"  >}}

Consider the following configuration, without a dummy interface in the bridge:

```
cumulus@switch:~$ sudo cat /etc/network/interfaces
...
auto br_default
iface br_default
    bridge-vlan-aware yes
    bridge-ports swp3
    bridge-vids 10
    bridge-pvid 1
...
```

With this configuration, when swp3 is down, the SVI is also down:

```
cumulus@switch:~$ ip link show swp3
5: swp3: <BROADCAST,MULTICAST> mtu 1500 qdisc pfifo_fast master br_default state DOWN mode DEFAULT group default qlen 1000
    link/ether 2c:60:0c:66:b1:7f brd ff:ff:ff:ff:ff:ff
cumulus@switch:~$ ip link show br_default
35: br_default: <NO-CARRIER,BROADCAST,MULTICAST,UP> mtu 1500 qdisc noqueue state DOWN mode DEFAULT group default
    link/ether 2c:60:0c:66:b1:7f brd ff:ff:ff:ff:ff:ff
```

Now add the dummy interface to your network configuration:

1. Edit the `/etc/network/interfaces` file and add the dummy interface stanza before the bridge stanza:

    ```
    cumulus@switch:~$ sudo nano /etc/network/interfaces
    ...
    auto dummy
    iface dummy
        link-type dummy

    auto br_default
    iface br_default
    ...
    ```

2. Add the dummy interface to the `bridge-ports` line in the bridge configuration:

    ```
    auto br_default
    iface br_default
        bridge-vlan-aware yes
        bridge-ports swp3 dummy
        bridge-vids 10
        bridge-pvid 1
    ```

3. Save and exit the file, then reload the configuration:

    ```
    cumulus@switch:~$ sudo ifreload -a
    ```

    Now, even when swp3 is down, both the dummy interface and the bridge remain up:

    ```
    cumulus@switch:~$ ip link show swp3
    5: swp3: <BROADCAST,MULTICAST> mtu 1500 qdisc pfifo_fast master br_default state DOWN mode DEFAULT group default qlen 1000
        link/ether 2c:60:0c:66:b1:7f brd ff:ff:ff:ff:ff:ff
    cumulus@switch:~$ ip link show dummy
    37: dummy: <BROADCAST,NOARP,UP,LOWER_UP> mtu 1500 qdisc noqueue master br_default state UNKNOWN mode DEFAULT group default
        link/ether 66:dc:92:d4:f3:68 brd ff:ff:ff:ff:ff:ff
    cumulus@switch:~$ ip link show br_default
    35: br_default: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue state UP mode DEFAULT group default
        link/ether 2c:60:0c:66:b1:7f brd ff:ff:ff:ff:ff:ff
    ```

{{< /expand >}}

## IPv6 Linklocal Address Generation

By default, Cumulus Linux automatically generates IPv6 *linklocal* addresses on VLAN interfaces. If you want to use a different mechanism to assign linklocal addresses, you can disable this feature. You can disable linklocal automatic address generation for both regular IPv6 addresses and address-virtual (macvlan) addresses.

To disable automatic address generation for a regular IPv6 address on a VLAN, run the following command. The following example command disables automatic address generation for a regular IPv6 address on VLAN 10.

{{< tabs "TabID248 ">}}
{{< tab "NCLU Commands ">}}

```
cumulus@switch:~$ net add vlan 10 ipv6-addrgen off
cumulus@switch:~$ net pending
cumulus@switch:~$ net commit
```

{{< /tab >}}
{{< tab "NVUE Commands ">}}

NVUE commands are not supported.

{{< /tab >}}
{{< tab "Linux Commands ">}}

Edit the `/etc/network/interfaces` file to add the line `ipv6-addrgen off` to the VLAN stanza, then run the `ifreload -a` command.

```
cumulus@switch:~$ sudo nano /etc/network/interfaces
...
auto vlan10
iface vlan 10
    ipv6-addrgen off
    vlan-id 10
    vlan-raw-device br_default
...
```

```
cumulus@switch:~$ ifreload -a
```

{{< /tab >}}
{{< /tabs >}}

To re-enable automatic linklocal address generation for a VLAN:

{{< tabs "TabID287 ">}}
{{< tab "NCLU Commands ">}}

```
cumulus@switch:~$ net del vlan 10 ipv6-addrgen off
cumulus@switch:~$ net pending
cumulus@switch:~$ net commit
```

{{< /tab >}}
{{< tab "NVUE Commands ">}}

NVUE commands are not supported.

{{< /tab >}}
{{< tab "Linux Commands ">}}

Edit the `/etc/network/interfaces` file to **remove** the line `ipv6-addrgen off` from the VLAN stanza, then run the `ifreload -a` command.

{{< /tab >}}
{{< /tabs >}}

## Static MAC Address Entries

You can add a static MAC address entry to the layer 2 table for an interface within the VLAN-aware bridge by running a command similar to the following:

```
cumulus@switch:~$ sudo bridge fdb add 12:34:56:12:34:56 dev swp1 vlan 150 master static
cumulus@switch:~$ sudo bridge fdb show
44:38:39:00:00:7c dev swp1 master bridge permanent
12:34:56:12:34:56 dev swp1 vlan 150 master bridge static
44:38:39:00:00:7c dev swp1 self permanent
12:12:12:12:12:12 dev swp1 self permanent
12:34:12:34:12:34 dev swp1 self permanent
12:34:56:12:34:56 dev swp1 self permanent
12:34:12:34:12:34 dev bridge master bridge permanent
44:38:39:00:00:7c dev bridge vlan 500 master bridge permanent
12:12:12:12:12:12 dev bridge master bridge permanent
```

## Example Configuration

The following example configuration contains an access port and switch port that are *pruned*; they only send and receive traffic tagged to and from a specific set of VLANs declared by the `bridge-vids` attribute. It also contains other switch ports that send and receive traffic from all the defined VLANs.

```
...
# ports swp3-swp48 are trunk ports which inherit vlans from the 'bridge'
# ie vlans 310,700,707,712,850,910
#
auto br_default
iface br_default
      bridge-ports swp1 swp2 swp3 ... swp51 swp52
      bridge-vids 310 700 707 712 850 910
      bridge-vlan-aware yes
auto swp1
iface swp1
      bridge-access 310
      mstpctl-bpduguard yes
      mstpctl-portadminedge yes
# The following is a trunk port that is "pruned".
# native vlan is 1, but only .1q tags of 707, 712, 850 are
# sent and received
#
auto swp2
iface swp2
      mstpctl-bpduguard yes
      mstpctl-portadminedge yes
      bridge-vids 707 712 850
# The following port is the trunk uplink and inherits all vlans
# from 'bridge'; bridge assurance is enabled using 'portnetwork' attribute
auto swp49
iface swp49
      mstpctl-portnetwork yes
      mstpctl-portpathcost 10
# The following port is the trunk uplink and inherits all vlans
# from 'br_default'; bridge assurance is enabled using 'portnetwork' attribute
 auto swp50
 iface swp50
      mstpctl-portnetwork yes
      mstpctl-portpathcost 0
...
```

## Considerations

### Spanning Tree Protocol (STP)

- STP is enabled on a per-bridge basis.
- `mstpd` remains the user space protocol daemon.
- Cumulus Linux supports {{<link url="Spanning-Tree-and-Rapid-Spanning-Tree-STP" text="Rapid Spanning Tree Protocol (RSTP)">}}.

<!--### IGMP Snooping

IGMP snooping and group membership are supported on a per-VLAN basis; however, the IGMP snooping configuration (including enable, disable, and mrouter ports) is defined on a per-bridge port basis.-->

### VLAN Translation

You cannot enable VLAN translation on a bridge in VLAN-aware mode. Only traditional mode bridges support VLAN translation.

### Bridge Conversion

You cannot convert traditional mode bridges automatically to and from a VLAN-aware bridge. You must delete the original configuration and bring down all member switch ports before creating a new bridge.
