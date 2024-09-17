---
title: VLAN-aware Bridge Mode
author: NVIDIA
weight: 450
toc: 4
---
The Cumulus Linux bridge driver supports two configuration modes, one that is VLAN-aware, and one that follows a more traditional Linux bridge model.

For {{<link url="Traditional-Bridge-Mode" text="traditional Linux bridges">}}, the kernel supports VLANs in the form of VLAN subinterfaces. Enabling bridging on multiple VLANs means configuring a bridge for each VLAN and, for each member port on a bridge, creating one or more VLAN subinterfaces out of that port. This mode poses scalability challenges in terms of configuration size as well as boot time and run time state management, when the number of ports times the number of VLANs becomes large.

The VLAN-aware mode in Cumulus Linux implements a configuration model for large-scale layer 2 environments, with **one single instance** of {{<link url="Spanning-Tree-and-Rapid-Spanning-Tree" text="spanning tree protocol">}}. Each physical bridge member port is configured with the list of allowed VLANs as well as its port VLAN ID, either primary VLAN Identifier (PVID) or native VLAN. MAC address learning, filtering and forwarding are *VLAN-aware*. This significantly reduces the configuration size, and eliminates the large overhead of managing the port/VLAN instances as subinterfaces, replacing them with lightweight VLAN bitmaps and state updates.

{{%notice tip%}}

You can configure both VLAN-aware and traditional mode bridges on thesame network in Cumulus Linux; however do not have more than one VLAN-aware bridge on a given switch.

{{%/notice%}}

## Configure a VLAN-aware Bridge

The example below shows the commands required to create a VLAN-aware bridge configured for STP that contains two switch ports and includes 3 VLANs; the tagged VLANs 100 and 200 and the untagged (native) VLAN of 1.

{{< img src = "/images/cumulus-linux/ethernet-bridging-basic-trunking.png" >}}

{{< tabs "TabID0" >}}

{{< tab "NCLU Commands" >}}

```
cumulus@switch:~$ net add bridge bridge ports swp1-2
cumulus@switch:~$ net add bridge bridge vids 100,200
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
    bridge-vids 100 200
    bridge-vlan-aware yes
```

{{< /tab >}}

{{< tab "Linux Commands" >}}

Edit the `/etc/network/interfaces` file and add the bridge. An example configuration is shown below.

```
cumulus@switch:~$ sudo nano /etc/network/interfaces
...
auto bridge
iface bridge
    bridge-ports swp1 swp2
    bridge-vids 100 200
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
auto bridge
iface bridge
    bridge-ports swp1 swp2
    bridge-vids 1 100 200
    bridge-vlan-aware yes
```

```
auto bridge
iface bridge
    bridge-ports swp1 swp2
    bridge-pvid 1
    bridge-vids 1 100 200
    bridge-vlan-aware yes
```

```
auto bridge
iface bridge
    bridge-ports swp1 swp2
    bridge-vids 100 200
    bridge-vlan-aware yes
```

{{%notice tip%}}

If you specify `bridge-vids` or `bridge-pvid` at the bridge level, these configurations are inherited by all ports in the bridge. However, specifying any of these settings for a specific port overrides the setting in the bridge.

{{%/notice%}}

{{%notice warning%}}

Do not try to bridge the management port, eth0, with any switch ports (swp0, swp1 and so on). For example, if you create a bridge with eth0 and swp1, it will not work properly and might disrupt access to the management interface.

{{%/notice%}}

### Reserved VLAN Range

For hardware data plane internal operations, the switching silicon requires VLANs for every physical port, Linux bridge, and layer 3 subinterface. Cumulus Linux reserves a range of 1000 VLANs by default; the reserved range is 3000-3999.

{{%notice tip%}}

You can modify the reserved range if it conflicts with any user-defined VLANs, as long the new range is a contiguous set of VLANs with IDs anywhere between 2 and 4094, and the minimum size of the range is 300 VLANs.

{{%/notice%}}

To configure the reserved range:

1. Open `/etc/cumulus/switchd.conf` in a text editor.
2. Uncomment the following line, specify a new range, and save the file:

    ```
    resv_vlan_range
    ```

3. Restart `switchd` to implement the change:

    ```
    cumulus@switch:~$ sudo systemctl restart switchd.service
    ```

   {{%notice note%}}

While restarting `switchd`, all running ports will flap, and forwarding will be interrupted.

    {{%/notice%}}

## VLAN Filtering (VLAN Pruning)

By default, the bridge port inherits the bridge VIDs. To configure a port to override the bridge VIDs:

{{< img src = "/images/cumulus-linux/ethernet-bridging-vlan-pruned.png" >}}

{{< tabs "TabID2" >}}

{{< tab "NCLU Commands" >}}

The following example commands configure swp3 to override the bridge VIDs:

```
cumulus@switch:~$ net add bridge bridge ports swp1-3
cumulus@switch:~$ net add bridge bridge vids 100,200
cumulus@switch:~$ net add bridge bridge pvid 1
cumulus@switch:~$ net add interface swp3 bridge vids 200
cumulus@switch:~$ net pending
cumulus@switch:~$ net commit
```

The above commands create the following code snippets in the `/etc/network/interfaces` file:

```
auto bridge
iface bridge
    bridge-ports swp1 swp2 swp3
    bridge-pvid 1
    bridge-vids 100 200
    bridge-vlan-aware yes

auto swp3
iface swp3
  bridge-vids 200
```

{{< /tab >}}

{{< tab "Linux Commands" >}}

Edit the `/etc/network/interfaces` file. The following example commands configure swp3 to override the bridge VIDs:

```
cumulus@switch:~$ sudo nano /etc/network/interfaces
...
auto bridge
iface bridge
    bridge-ports swp1 swp2 swp3
    bridge-pvid 1
    bridge-vids 100 200
    bridge-vlan-aware yes

auto swp3
iface swp3
  bridge-vids 200
...
```

Run the `ifreload -a` command to load the new configuration:

```
cumulus@switch:~$ ifreload -a
```

{{< /tab >}}

{{< /tabs >}}

## Untagged/Access Ports

Access ports ignore all tagged packets. In the configuration below, swp1 and swp2 are configured as access ports, while all untagged traffic goes to VLAN 100:

{{< img src = "/images/cumulus-linux/ethernet-bridging-vlan_untagged_access_ports.png" >}}

{{< tabs "TabID4" >}}

{{< tab "NCLU Commands" >}}

```
cumulus@switch:~$ net add bridge bridge ports swp1-2
cumulus@switch:~$ net add bridge bridge vids 100,200
cumulus@switch:~$ net add bridge bridge pvid 1
cumulus@switch:~$ net add interface swp1 bridge access 100
cumulus@switch:~$ net add interface swp2 bridge access 100
cumulus@switch:~$ net pending
cumulus@switch:~$ net commit
```

The above commands create the following code snippets in the `/etc/network/interfaces` file:

```
auto bridge
iface bridge
    bridge-ports swp1 swp2
    bridge-pvid 1
    bridge-vids 100 200
    bridge-vlan-aware yes

auto swp1
iface swp1
    bridge-access 100

auto swp2
iface swp2
    bridge-access 100
```

{{< /tab >}}

{{< tab "Linux Commands" >}}

Edit the `/etc/network/interfaces` file.

```
cumulus@switch:~$ sudo nano /etc/network/interfaces
...
auto bridge
iface bridge
    bridge-ports swp1 swp2
    bridge-pvid 1
    bridge-vids 100 200
    bridge-vlan-aware yes

auto swp1
iface swp1
    bridge-access 100

auto swp2
iface swp2
    bridge-access 100
...
```

Run the `ifreload -a` command to load the new configuration:

```
cumulus@switch:~$ ifreload -a
```

{{< /tab >}}

{{< /tabs >}}

## Drop Untagged Frames

With VLAN-aware bridge mode, you can configure a switch port to drop any untagged frames. To do this, add `bridge-allow-untagged no` to the **switch port** (not to the bridge). This leaves the bridge port without a PVID and drops untagged packets.

{{< tabs "TabID6" >}}

{{< tab "NCLU Commands" >}}

To configure a switch port to drop untagged frames, run the `net add interface swp2 bridge allow-untagged no` command. The following example command configures swp2 to drop untagged frames:

```
cumulus@switch:~$ net add interface swp2 bridge allow-untagged no
```

When you check VLAN membership for that port, it shows that there is **no** untagged VLAN.

```
cumulus@switch:~$ net show bridge vlan

Interface      VLAN   Flags
-----------  ------   ---------------------
swp1              1   PVID, Egress Untagged
                 10
                100
                200
swp2             10
                100
                200
```

{{< /tab >}}

{{< tab "Linux Commands" >}}

Edit the `/etc/network/interfaces` file to add the `bridge-allow-untagged no` line to the under the switch port interface stanza. The following example configures swp2 to drop untagged frames:

```
cumulus@switch:~$ sudo nano /etc/network/interfaces
...
auto swp1
iface swp1

auto swp2
iface swp2
    bridge-allow-untagged no 

auto bridge
iface bridge
    bridge-ports swp1 swp2
    bridge-pvid 1
    bridge-vids 10 100 200
    bridge-vlan-aware yes
...
```

Run the `ifreload -a` command to load the new configuration:

``` 
cumulus@switch:~$ sudo ifreload -a
```

When you check VLAN membership for that port, it shows that there is **no** untagged VLAN.

```
cumulus@switch:~$ bridge -c vlan show
portvlan ids
swp1 1 PVID Egress Untagged
  10 100 200

swp2 10 100 200

bridge 1
```

{{< /tab >}}

{{< /tabs >}}

## VLAN Layer 3 Addressing - Switch Virtual Interfaces and Other VLAN Attributes

When configuring the VLAN attributes for the bridge, specify the attributes for each VLAN interface. If you are configuring the SVI for the native VLAN, you must declare the native VLAN and specify its IP address. Specifying the IP address in the bridge stanza itself returns an error.

{{< tabs "TabID8" >}}

{{< tab "NCLU Commands" >}}

The following example commands declare native VLAN 100 with IPv4 address 192.168.10.1/24 and IPv6 address 2001:db8::1/32.

```
cumulus@switch:~$ net add vlan 100 ip address 192.168.10.1/24
cumulus@switch:~$ net add vlan 100 ipv6 address 2001:db8::1/32
cumulus@switch:~$ net pending
cumulus@switch:~$ net commit
```

{{< /tab >}}

{{< tab "Linux Commands" >}}

Edit the `/etc/network/interfaces` file, then reload the configuration with the `ifreload -a` command. The following example declares native VLAN 100 with IPv4 address 192.168.10.1/24 and IPv6 address 2001:db8::1/32.

```
cumulus@switch:~$ sudo nano /etc/network/interfaces
...
auto bridge
iface bridge
    bridge-ports swp1 swp2
    bridge-pvid 1
    bridge-vids 10 100 200
    bridge-vlan-aware yes

auto vlan100
iface vlan100
    address 192.168.10.1/24
    address 2001:db8::1/32
    vlan-id 100
    vlan-raw-device bridge
...
```

{{< /tab >}}

{{< /tabs >}}

{{%notice note%}}

In the above configuration, if your switch is configured for multicast routing, you do not need to specify `bridge-igmp-querier-src`, as there is no need for a static IGMP querier configuration on the switch. Otherwise, the static IGMP querier configuration helps to probe the hosts to refresh their IGMP reports.

{{%/notice%}}

## Configure Multiple Ports in a Range

To save time, you can specify a range of ports or VLANs instead of enumerating each one individually.

To specify a range:

{{< tabs "TabID10" >}}

{{< tab "NCLU Commands" >}}

In the example below, `swp1-52` indicates that swp1 through swp52 are part of the bridge.

```
cumulus@switch:~$ net add bridge bridge ports swp1-52
cumulus@switch:~$ net pending
cumulus@switch:~$ net commit
```

{{< /tab >}}

{{< tab "Linux Commands" >}}

The `glob` keyword referenced in the `bridge-ports` attribute indicates that swp1 through swp52 are part of the bridge:

```
...
auto bridge
iface bridge
        bridge-vlan-aware yes
        bridge-ports glob swp1-52
        bridge-stp on
        bridge-vids 310 700 707 712 850 910
...
```

{{< /tab >}}

{{< /tabs >}}

## Example Configurations

The following sections provide example VLAN-aware bridge configurations.

### Access Ports and Pruned VLANs

The following example configuration contains an access port and switch port that are *pruned*; they only sends and receive traffic tagged to and from a specific set of VLANs declared by the `bridge-vids` attribute. It also contains other switch ports that send and receive traffic from all the defined VLANs.

```
...
# ports swp3-swp48 are trunk ports which inherit vlans from the 'bridge'
# ie vlans 310,700,707,712,850,910
#
auto bridge
iface bridge
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
# from 'bridge'; bridge assurance is enabled using 'portnetwork' attribute
 auto swp50
 iface swp50
      mstpctl-portnetwork yes
      mstpctl-portpathcost 0
...
```

### Large Bond Set Configuration

The configuration below demonstrates a VLAN-aware bridge with a large set of bonds. The bond configurations are generated from a {{<exlink url="http://www.makotemplates.org/" text="Mako">}} template.

```
...
#
# vlan-aware bridge with bonds example
#
# uplink1, peerlink and downlink are bond interfaces.
# 'bridge' is a vlan aware bridge with ports uplink1, peerlink
# and downlink (swp2-20).
#
# native vlan is by default 1
#
# 'bridge-vids' attribute is used to declare vlans.
# 'bridge-pvid' attribute is used to specify native vlans if other than 1
# 'bridge-access' attribute is used to declare access port
#
auto lo
iface lo

auto eth0
iface eth0 inet dhcp

# bond interface
auto uplink1
iface uplink1
    bond-slaves swp32
    bridge-vids 2000-2079

# bond interface
auto peerlink
iface peerlink
    bond-slaves swp30 swp31
    bridge-vids 2000-2079 4094

# bond interface
auto downlink
iface downlink
    bond-slaves swp1
    bridge-vids 2000-2079

#
# Declare vlans for all swp ports
# swp2-20 get vlans from 2004 to 2022.
# The below uses mako templates to generate iface sections
# with vlans for swp ports
#
%for port, vlanid in zip(range(2, 20), range(2004, 2022)) :
    auto swp${port}
    iface swp${port}
      bridge-vids ${vlanid}

%endfor

# svi vlan 2000
auto bridge.2000
iface bridge.2000
    address 11.100.1.252/24

# l2 attributes for vlan 2000
auto bridge.2000
vlan bridge.2000
    bridge-igmp-querier-src 172.16.101.1

#
# vlan-aware bridge
#
auto bridge
iface bridge
    bridge-ports uplink1 peerlink downlink swp1 swp2 swp49 swp50
    bridge-vlan-aware yes

# svi peerlink vlan
auto peerlink.4094
iface peerlink.4094
    address 192.168.10.1/30
    broadcast 192.168.10.3
...
```

### VXLANs with VLAN-aware Bridges

Cumulus Linux supports using VXLANs with VLAN-aware bridge configuration. This provides improved scalability, as multiple VXLANs can be added to a single VLAN-aware bridge. A one to one association is used between the VXLAN VNI and the VLAN, with the bridge access VLAN definition on the VXLAN and the VLAN membership definition on the local bridge member interfaces.

The configuration example below shows the differences between a VXLAN configured for traditional bridge mode and one configured for VLAN-aware mode. The configurations use head end replication (HER) together with the VLAN-aware bridge to map VLANs to VNIs.

{{%notice note%}}

See {{<link title="VXLAN Scale">}} for information about the number of VXLANs you can configure simultaneously.

{{%/notice%}}

```
...
auto lo
iface lo inet loopback
    address 10.35.0.10/32

auto bridge
iface bridge
    bridge-ports uplink
    bridge-pvid 1
    bridge-vids 1-100
    bridge-vlan-aware yes
auto vni-10000
iface vni-10000
    alias CUSTOMER X VLAN 10
    bridge-access 10
    vxlan-id 10000
    vxlan-local-tunnelip 10.35.0.10
    vxlan-remoteip 10.35.0.34
...
```

### Configure a Static MAC Address Entry

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

## Caveats and Errata

### Spanning Tree Protocol (STP)

- Because STP is enabled on a per-bridge basis, VLAN-aware mode supports a single instance of STP across all VLANs. A common practice when using a single STP instance for all VLANs is to define every VLAN on every switch in the spanning tree instance.
- `mstpd` remains the user space protocol daemon.
- Cumulus Linux supports {{<link url="Spanning-Tree-and-Rapid-Spanning-Tree" text="Rapid Spanning Tree Protocol (RSTP)">}}.

### IGMP Snooping

IGMP snooping and group membership are supported on a per-VLAN basis; however, the IGMP snooping configuration (including enable, disable, and mrouter ports) is defined on a per-bridge port basis.

### VLAN Translation

A bridge in VLAN-aware mode cannot have VLAN translation enabled. Only traditional mode bridges can utilize VLAN translation.

### Convert Bridges between Supported Modes

You cannot convert traditional mode bridges automatically to and from a VLAN-aware bridge. You must delete the original configuration and bring down all member switch ports before creating a new bridge.
