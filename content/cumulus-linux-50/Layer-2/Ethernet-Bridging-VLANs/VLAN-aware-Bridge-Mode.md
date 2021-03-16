---
title: VLAN-aware Bridge Mode
author: NVIDIA
weight: 430
toc: 4
---
VLAN-aware mode in Cumulus Linux implements a configuration model for large-scale layer 2 environments, with **one single instance** of {{<link url="Spanning-Tree-and-Rapid-Spanning-Tree-STP" text="spanning tree protocol">}}. Each physical bridge member port is configured with the list of allowed VLANs as well as its port VLAN ID, either primary VLAN Identifier (PVID) or native VLAN. MAC address learning, filtering and forwarding are *VLAN-aware*. This significantly reduces the configuration size, and eliminates the large overhead of managing the port/VLAN instances as subinterfaces, replacing them with lightweight VLAN bitmaps and state updates.

{{%notice note%}}

You cannot have more than one VLAN-aware bridge on a switch.

{{%/notice%}}

## Configure a VLAN-aware Bridge

The example below shows the commands required to create a VLAN-aware bridge that contains two switch ports and includes 3 VLANs; VLANs 10 and 20 (tagged), and native VLAN 1 (untagged).

{{< img src = "/images/cumulus-linux/ethernet-bridging-basic-trunking1.png" >}}

{{< tabs "TabID27 ">}}
{{< tab "CUE Commands ">}}

With CUE, there is a default bridge called `br_default`, which has no ports assigned to it. The example below configures this default bridge.

```
cumulus@switch:~$ cl set interface swp1-2 bridge domain br_default
cumulus@switch:~$ cl set bridge domain br_default vlan 10,20
cumulus@switch:~$ cl set bridge domain br_default untagged 1
cumulus@switch:~$ cl config apply
```

{{< /tab >}}
{{< tab "NCLU Commands ">}}

```
cumulus@switch:~$ net add bridge bridge ports swp1-2
cumulus@switch:~$ net add bridge bridge vids 10,20
cumulus@switch:~$ net add bridge bridge pvid 1
cumulus@switch:~$ net pending
cumulus@switch:~$ net commit
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

The Primary VLAN Identifer (PVID) of the bridge defaults to 1. You do *not* have to specify `bridge-pvid` for a bridge or port. However, even though this does not affect the configuration, it helps other users for readability. The following configurations are identical to each other and the configuration above:

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
If you specify `bridge-vids` or `bridge-pvid` at the bridge level, these configurations are inherited by all ports in the bridge. However, specifying any of these settings for a specific port overrides the setting in the bridge.
{{%/notice%}}

{{%notice warning%}}
Do not try to bridge the management port eth0 with any switch ports (swp0, swp1 and so on). For example, if you create a bridge with eth0 and swp1, it will not work properly and might disrupt access to the management interface.
{{%/notice%}}

## Reserved VLAN Range

For hardware data plane internal operations, the switching silicon requires VLANs for every physical port, Linux bridge, and layer 3 subinterface. Cumulus Linux reserves a range of  VLANs by default; the reserved range is between 3600 and 3999.

You can modify the reserved range if it conflicts with any user-defined VLANs, as long the new range is a contiguous set of VLANs with IDs anywhere between 2 and 4094, and the minimum size of the range is 150 VLANs.

To configure the reserved range:

Edit the `/etc/cumulus/switchd.conf` file to uncomment the `resv_vlan_range` line and specify a new range, then restart `switchd`:

```
cumulus@switch:~$ sudo nano /etc/cumulus/switchd.conf
...
resv_vlan_range
```

{{<cl/restart-switchd>}}

## VLAN Pruning

By default, the bridge port inherits the bridge VIDs; however, you can configure a port to override the bridge VIDs.

The following example shows you how to configure swp3 to override the bridge VIDs.

{{< img src = "/images/cumulus-linux/ethernet-bridging-vlan-pruned1.png" >}}

{{< tabs "TabID157 ">}}
{{< tab "CUE Commands ">}}

```
cumulus@switch:~$ cl set interface swp1-3 bridge domain br_default
cumulus@switch:~$ cl set bridge domain br_default vlan 10,20
cumulus@switch:~$ cl set bridge domain br_default untagged 1
cumulus@switch:~$ cl set interface swp3 bridge domain br_default vlan 20
cumulus@switch:~$ cl config apply
```

{{< /tab >}}
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
{{< tab "Linux Commands ">}}

Edit the `/etc/network/interfaces` file, then run the `ifreload -a` command.

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

## Access Ports

Access ports ignore all tagged packets. In the configuration below, swp1 and swp2 are configured as access ports, while all untagged traffic goes to VLAN 10.

{{< img src = "/images/cumulus-linux/ethernet-bridging-vlan_untagged_access_ports1.png" >}}

{{< tabs "TabID223 ">}}
{{< tab "CUE Commands ">}}

```
cumulus@switch:~$ cl set interface swp1-2 bridge domain br_default
cumulus@switch:~$ cl set bridge domain br_default vlan 10,20
cumulus@switch:~$ cl set bridge domain br_default untagged 1
cumulus@switch:~$ cl set interface swp1 bridge domain br_default access 10
cumulus@switch:~$ cl set interface swp2 bridge domain br_default access 10
cumulus@switch:~$ cl config apply
```

{{< /tab >}}
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

With VLAN-aware bridge mode, you can configure a switch port (not the bridge) to drop any untagged frames. This leaves the bridge port without a PVID and drops untagged packets.

The following example command configures swp2 to drop untagged frames:

{{< tabs "TabID294 ">}}
{{< tab "CUE Commands ">}}

```
cumulus@switch:~$ cl set interface swp2 bridge domain br_default untagged none
cumulus@switch:~$ cl config apply
```

{{< /tab >}}
{{< tab "NCLU Commands ">}}

```
cumulus@switch:~$ net add interface swp2 bridge allow-untagged no
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

You can check VLAN membership for the port with the CUE `cl show bridge domain <domain-name> vlan` command or the Linux `bridge -c vlan show` command. The command output shows that there is **no** untagged VLAN. For example:

```
cumulus@switch:~$ bridge -c vlan show
portvlan ids
swp1 1 PVID Egress Untagged
  10 20

swp2 10 20

bridge 1
```

## VLAN Layer 3 Addressing

When you configure VLAN attributes for a bridge, you must specify the attributes for each VLAN interface. If you configure the switch virtual interface (SVI) for the native VLAN, you must declare the native VLAN and specify its IP address.

The following example commands declare native VLAN 10 with IPv4 address 10.1.10.2/24 and IPv6 address 2001:db8::1/32.

{{< tabs "TabID370 ">}}
{{< tab "CUE Commands ">}}

```
cumulus@switch:~$ cl set interface vlan10 ip address 10.1.10.2/24
cumulus@switch:~$ cl set interface vlan10 ip address 2001:db8::1/32
cumulus@switch:~$ cl config apply
```

{{< /tab >}}
{{< tab "NCLU Commands ">}}

```
cumulus@switch:~$ net add vlan 10 ip address 10.1.10.2/24
cumulus@switch:~$ net add vlan 10 ipv6 address 2001:db8::1/32
cumulus@switch:~$ net pending
cumulus@switch:~$ net commit
```

{{< /tab >}}
{{< tab "Linux Commands ">}}

Edit the `/etc/network/interfaces` file, then run the `ifreload -a` command.

{{%notice note%}}
Specifying the IP address in the bridge stanza itself returns an error.
{{%/notice%}}

```
cumulus@switch:~$ sudo nano /etc/network/interfaces
...
auto br_default
iface br_default
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
...
```

```
cumulus@switch:~$ ifreload -a
```

{{< /tab >}}
{{< /tabs >}}

{{%notice note%}}
If your switch is configured for multicast routing, there is no need for a static IGMP querier configuration on the switch. The static IGMP querier configuration helps to probe the hosts to refresh their IGMP reports.
{{%/notice%}}

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

## IPv6 Link-local Address Generation

By default, Cumulus Linux automatically generates IPv6 {{<exlink url="https://en.wikipedia.org/wiki/Link-local_address" text="link-local addresses">}} on VLAN interfaces. If you want to use a different mechanism to assign link-local addresses, you can disable this feature. You can disable link-local automatic address generation for both regular IPv6 addresses and address-virtual (macvlan) addresses.

The following example command disables automatic address generation for a regular IPv6 address on VLAN 10.

{{< tabs "TabID248 ">}}
{{< tab "CUE Commands ">}}

```
cumulus@switch:~$ NEED COMMAND
cumulus@switch:~$ cl config apply
```

{{< /tab >}}
{{< tab "NCLU Commands ">}}

```
cumulus@switch:~$ net add vlan 10 ipv6-addrgen off
cumulus@switch:~$ net pending
cumulus@switch:~$ net commit
```

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

To re-enable automatic link-local address generation for a VLAN:

{{< tabs "TabID287 ">}}
{{< tab "CUE Commands ">}}

```
cumulus@switch:~$ NEED COMMAND
cumulus@switch:~$ cl config apply
```

{{< /tab >}}
{{< tab "NCLU Commands ">}}

Run the `net del vlan <vlan> ipv6-addrgen off` command.

```
cumulus@switch:~$ net del vlan 10 ipv6-addrgen off
cumulus@switch:~$ net pending
cumulus@switch:~$ net commit
```

{{< /tab >}}
{{< tab "Linux Commands ">}}

Edit the `/etc/network/interfaces` file to **remove** the line `ipv6-addrgen off` from the VLAN stanza, then run the `ifreload -a` command.

{{< /tab >}}
{{< /tabs >}}

## Example Configurations

The following sections provide example VLAN-aware bridge configurations.

### Access Ports and Pruned VLANs

The following example configuration contains an access port and switch port that are *pruned*; they only send and receive traffic tagged to and from a specific set of VLANs declared by the `bridge-vids` attribute. It also contains other switch ports that send and receive traffic from all the defined VLANs.

```
...
# ports swp3-swp48 are trunk ports that inherit vlans from the 'bridge'
# vlans 310,700,707,712,850,910
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

### Large Bond Sets

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

Cumulus Linux supports VXLANs with VLAN-aware bridge configurations. This provides improved scalability as multiple VXLANs can be added to a single VLAN-aware bridge. A one to one association is used between the VXLAN VNI and the VLAN, with the bridge access VLAN definition on the VXLAN and the VLAN membership definition on the local bridge member interfaces.

The configuration example below shows the differences between a VXLAN configured for traditional bridge mode and one configured for VLAN-aware mode. The configurations use head end replication (HER) together with the VLAN-aware bridge to map VLANs to VNIs.

```
...
auto lo
iface lo inet loopback
    address 10.10.10.1/32

auto br_default
iface br_default
    bridge-ports uplink
    bridge-pvid 1
    bridge-vids 1-100
    bridge-vlan-aware yes

auto vni-10000
iface vni-10000
    alias CUSTOMER X VLAN 10
    bridge-access 10
    vxlan-id 10000
    vxlan-local-tunnelip 10.10.10.1
    vxlan-remoteip 10.10.10.34
...
```

### Static MAC Address Entries

You can add a static MAC address entry to the layer 2 table for an interface in a VLAN-aware bridge by running a command similar to the following:

```
cumulus@switch:~$ sudo bridge fdb add 12:34:56:12:34:56 dev swp1 vlan 10 master static
```

## Considerations

### Spanning Tree Protocol (STP)

- STP is enabled on a per-bridge basis; therefore, VLAN-aware mode supports a single instance of STP across all VLANs. A common practice when using a single STP instance for all VLANs is to define every VLAN on every switch in the spanning tree instance.
- `mstpd` remains the user space protocol daemon.
- Cumulus Linux supports {{<link url="Spanning-Tree-and-Rapid-Spanning-Tree-STP" text="Rapid Spanning Tree Protocol (RSTP)">}}.

<!--### IGMP Snooping

IGMP snooping and group membership are supported on a per-VLAN basis; however, the IGMP snooping configuration (including enable, disable, and mrouter ports) is defined on a per-bridge port basis.-->

### VLAN Translation

You cannot enable VLAN translation on a bridge in VLAN-aware mode. Only traditional mode bridges support VLAN translation.

### Convert Bridges between Supported Modes

You cannot convert traditional mode bridges automatically to and from a VLAN-aware bridge. You must delete the original configuration and bring down all member switch ports before creating a new bridge.
