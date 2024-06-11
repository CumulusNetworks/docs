---
title: VLAN-aware Bridge Mode
author: NVIDIA
weight: 430
toc: 4
---
VLAN-aware bridge mode in Cumulus Linux implements a configuration model for large-scale layer 2 environments, with *one single instance* of {{<link url="Spanning-Tree-and-Rapid-Spanning-Tree-STP" text="spanning tree protocol">}}. Each physical bridge member port includes the list of allowed VLANs as well as the port VLAN ID, either the primary VLAN Identifier (PVID) or native VLAN. MAC address learning, filtering and forwarding are *VLAN-aware*. This reduces the configuration size, and eliminates the large overhead of managing the port and VLAN instances as subinterfaces, replacing them with lightweight VLAN bitmaps and state updates.

Cumulus Linux supports multiple VLAN-aware bridges but with the following limitations:

- You cannot use MLAG with multiple VLAN-aware bridges.
- You cannot use the same port with multiple VLAN-aware bridges.
- You cannot use the same VNIs in multiple VLAN-aware bridges.
- You cannot use VLAN translation with multiple VLAN-aware bridges.
- You cannot use double tagged VLAN interfaces with multiple VLAN-aware bridges.
- You cannot associate multiple single VXLAN devices (SVDs) with a single VLAN-aware bridge
<!-- vale off -->
## Configure a VLAN-aware Bridge
<!-- vale on -->
The example commands below create a VLAN-aware bridge for STP that contains two switch ports and includes 3 VLANs; tagged VLANs 10 and 20, and untagged (native) VLAN 1.

{{< img src = "/images/cumulus-linux/ethernet-bridging-basic-trunking1.png" >}}

{{< tabs "TabID25 ">}}
{{< tab "NVUE Commands ">}}

With NVUE, there is a default bridge called `br_default`, which has no ports assigned. The example below configures this default bridge.

```
cumulus@switch:~$ nv set interface swp1-2 bridge domain br_default
cumulus@switch:~$ nv set bridge domain br_default vlan 10,20
cumulus@switch:~$ nv set bridge domain br_default untagged 1
cumulus@switch:~$ nv config apply
```

{{< /tab >}}
{{< tab "Linux Commands ">}}

Edit the `/etc/network/interfaces` file and add the bridge:

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

The Primary VLAN Identifier (PVID) of the bridge defaults to 1. You do *not* have to specify `bridge-pvid` for a bridge or a port. However, even though this does not affect the configuration, it helps other users for readability. The following configurations are identical to each other and the configuration above:

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
- If you specify `bridge-vids` or `bridge-pvid` at the bridge level, all ports in the bridge inherit these configurations. However, specifying any of these settings for a specific port overrides the setting in the bridge.
- Do not bridge the management port eth0 with any switch ports. For example, if you create a bridge with eth0 and swp1, the bridge does not work correctly and disrupts access to the management interface.
{{%/notice%}}
<!-- vale off -->
## Configure Multiple VLAN-aware Bridges
<!-- vale on -->
This example shows the commands required to create two VLAN-aware bridges on the switch.

{{< img src = "/images/cumulus-linux/ethernet-bridging-vmvab.png" >}}

- bridge1 bridges swp1 and swp2, and includes 2 VLANs; `vlan 10` and `vlan 20`
- bridge2 bridges swp3 and contains one VLAN; `vlan 10`

Bridges are independent so you can reuse VLANs between bridges. Each VLAN-aware bridge maintains its own MAC address and VLAN tag table; MAC and VLAN tags in one bridge are not visible to the other table.

{{< tabs "TabID128 ">}}
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

Edit the `/etc/network/interfaces` file and add the bridge:

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
NVIDIA Spectrum 1 switches support a maximum of 10000 VLAN elements. NVIDIA Spectrum-2 switches and later support a maximum of 15996 VLAN elements when {{<link url="In-Service-System-Upgrade-ISSU/#restart-mode" text="warm restart mode ">}} is `off` or 7934 VLAN elements when warm restart mode is `on`.
Cumulus Linux calculates the total number of VLAN elements as the number of VLANs times the number of configured bridges. For example, 6 bridges, each containing 2600 VLANs totals 15600 VLAN elements.

On NVIDIA Spectrum-2 switches and later, if you enable multiple VLAN-aware bridges and want to use more VLAN elements than the default, you must update the number of VLAN elements in the `/etc/mlx/datapath/broadcast_domains.conf` file.
  - To specify the total number of bridge domains you want to use, uncomment and edit the `broadcast_domain.max_vlans` parameter. The default value is 6143 when warm restart mode is `off` or 4096 when warm restart mode is `on`.
  - To specify the total number of subinterfaces you want to use, uncomment and edit the `broadcast_domain.max_subinterfaces` parameter. The default value is 3872 when warm restart mode is `off` or 1872 when warm restart mode is `on`.

  You must restart `switchd` with the `systemctl restart switchd` command to apply the configuration.

  The number of `broadcast_domain.max_vlans` plus `broadcast_domain.max_subinterfaces` cannot exceed 15996.

  Increasing the `broadcast_domain.max_vlans` parameter can affect layer 2 multicast scale support.
{{%/notice%}}

## Reserved VLAN Range

For hardware data plane internal operations, the switching silicon requires VLANs for every physical port, Linux bridge, and layer 3 subinterface. Cumulus Linux reserves a range of VLANs by default; the reserved range is 3725-3999.

If the reserved VLAN range conflicts with any user-defined VLANs, you can modify the range. The new range must be a contiguous set of VLANs with IDs between 2 and 4094. For a single VLAN-aware bridge, the minimum size of the range is 2 VLANs. For multiple VLAN-aware bridges, the minimum size of the range is the number of VLAN-aware bridges on the system plus one.

The following example changes the reserved VLAN range to be between 4064 and 4094:

{{< tabs "TabID177 ">}}
{{< tab "NVUE Commands ">}}

```
cumulus@switch:~$ nv set system global reserved vlan internal range 4064-4094
cumulus@switch:~$ nv config apply
```

{{< /tab >}}
{{< tab "Linux Commands ">}}

1. Edit the `/etc/cumulus/switchd.conf` file to uncomment the `resv_vlan_range` line and specify a new range.

   ```
   cumulus@switch:~$ sudo nano /etc/cumulus/switchd.conf
   ...
   # global reserved vlan internal range
   resv_vlan_range = 4064-4094
   ```

2. After you save the file, you must restart `switchd`:

   ```
   cumulus@switch:~$ sudo systemctl restart switchd.service
   ```

{{< /tab >}}
{{< /tabs >}}

### Reserved Layer 3 VNI VLANs

In addition to the internal reserved VLAN range, Cumulus Linux allocates a reserved VLAN range for layer 3 VNIs in EVPN symmetric routing deployments. Use this reserved VLAN range when you configure layer 3 VNIs in MLAG environments with NVUE commands. The default range is 4000-4064. You can display the range with the `nv show system global reserved vlan l3-vni-vlan` command:

```
cumulus@switch:~$ nv show system global reserved vlan l3-vni-vlan
operational  applied
-----  -----------  -------
begin  4000         4000
end    4064         4064
```

Do not use this range of VLANs in the same bridge as your MLAG interfaces and layer 3 VNIs. You can configure the range with the `nv set system global reserved vlan l3-vni-vlan begin <vlan>` and `nv set system global reserved vlan l3-vni-vlan end <vlan>` commands. For more information, see {{<link url="Inter-subnet-Routing/#symmetric-routing" text="symmetric routing">}}.

{{%notice note%}}
The global reserved layer 3 VNI VLAN range does not apply to switches that you configure manually with Linux commands instead of NVUE or for symmetric routing deployments without MLAG.
{{%/notice%}}

## VLAN Pruning

By default, the bridge port inherits the bridge VIDs, however, you can configure a port to override the bridge VIDs.
<!-- vale off -->
{{< img src = "/images/cumulus-linux/ethernet-bridging-vlan-pruned1.png" >}}
<!-- vale on -->
This example commands configure swp3 to override the bridge VIDs:

{{< tabs "TabID157 ">}}
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

Access ports ignore all tagged packets. In the configuration below, swp1 and swp2 are access ports, while all untagged traffic goes to VLAN 10:
<!-- vale off -->
{{< img src = "/images/cumulus-linux/ethernet-bridging-vlan_untagged_access_ports1.png" >}}
<!-- vale on -->
{{< tabs "TabID223 ">}}
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

With VLAN-aware bridge mode, you can configure a switch port to drop any untagged frames. To do this, add `bridge-allow-untagged no` to the **switch port** (not to the bridge). The bridge port is without a PVID and drops untagged packets.

The following example command configures swp2 to drop untagged frames:

{{< tabs "TabID294 ">}}
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

## Keep SVIs Perpetually UP

The first time you configure a switch, all southbound bridge ports are down; therefore, by default, SVIs are also down. You can force SVIs to always be up by disabling interface state tracking so that the SVIs are always in the UP state even when all member ports are down. Other implementations describe this feature as *no autostate*. This is beneficial if you want to perform connectivity testing.

{{< tabs "TabID483 ">}}
{{< tab "NVUE Commands ">}}

To configure all SVIs on the switch to be perpetually UP, run the `nv set system global svi-force-up enable on` command.

```
cumulus@switch:~$ nv set system global svi-force-up enable on
cumulus@switch:~$ nv config apply
```

To configure SVIs in a specific bridge to be perpetually UP, run the `nv set bridge domain <bridge> svi-force-up enable on` command:

```
cumulus@switch:~$ nv set bridge domain br_default svi-force-up enable on
cumulus@switch:~$ nv config apply
```

- To configure all SVIs on the switch to be perpetually DOWN, run the `nv set system global svi-force-up enable off` command.
- To configure the SVIs in a specific bridge to be perpetually DOWN, run the `nv set bridge domain <bridge> svi-force-up enable off` command.

{{< /tab >}}
{{< tab "Linux Commands ">}}

To configure the SVIs in a bridge to be perpetually UP, edit the `/etc/network/interfaces` file and add the `bridge-always-up on` option to the bridge stanza, then reload the configuration with the `sudo ifreload -a` command:

```
cumulus@switch:~$ sudo nano /etc/network/interfaces
auto br_default
iface br_default
    bridge-ports bond1 bond2 bond3 peerlink
    hwaddress 48:b0:2d:4e:ad:89
    bridge-vlan-aware yes
    bridge-vids 10 20 30
    bridge-pvid 1
    bridge-stp yes
    bridge-mcsnoop no
    bridge-always-up on
    mstpctl-forcevers rstp
```

```
cumulus@switch:~$ sudo ifreload -a
```

To configure all SVIs on the switch to be perpetually UP, add the `bridge-always-up on` option to all bridge stanzas with SVIs.

- To configure the SVIs in a bridge to be perpetually DOWN, remove the `bridge-always-up on` option from the bridge stanza, then reload the configuration with the `sudo ifreload -a` command.
- To configure all SVIs on the switch to be perpetually DOWN, remove the `bridge-always-up on` option from all bridge stanzas, then reload the configuration with the `sudo ifreload -a` command.

{{< /tab >}}
{{< /tabs >}}

With the `svi-force-up` (`bridge-always-up`) option set to `on`, even when an interface is down, the bridge remains UP:

```
cumulus@switch:~$ ip link show bond1
7: bond1: <BROADCAST,MULTICAST,MASTER> mtu 9216 qdisc noqueue master br_default state DOWN mode DEFAULT group default qlen 1000
    link/ether 48:b0:2d:cf:e4:3e brd ff:ff:ff:ff:ff:ff
cumulus@switch:~$ ip link show br_default
18: br_default: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue state UP mode DEFAULT group default qlen 1000
    link/ether 8:b0:2d:4e:ad:89 brd ff:ff:ff:ff:ff:ff
```

To show if the `svi-force-up` option is set to `on` for all SVIs on the switch, run the `nv show system global svi-force-up` command:

```
cumulus@switch:~$ nv show system global svi-force-up
       operational  applied
------  -----------  -------
enable  on           on
```

To show if the `svi-force-up` option is set to `on` for SVIs in a specific bridge, run the `nv show bridge domain <domain-id> svi-force-up` command:

```
cumulus@switch:~$ nv show bridge domain br_default svi-force-up
        applied
------  -------
enable  on
```

<!-- vale off -->
## IPv6 Link-local Address Generation
<!-- vale on -->
By default, Cumulus Linux automatically generates IPv6 *link-local* addresses on VLAN interfaces. If you want to use a different mechanism to assign link-local addresses, you can disable this feature. You can disable link-local automatic address generation for both regular IPv6 addresses and address-virtual (macvlan) addresses.

To disable automatic address generation for a regular IPv6 address on a VLAN, run the following command. The following example command disables automatic address generation for a regular IPv6 address on VLAN 10.

{{< tabs "TabID248 ">}}
{{< tab "NVUE Commands ">}}

Cumulus Linux does not provide NVUE commands for this setting.

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

To reenable automatic link-local address generation for a VLAN:

{{< tabs "TabID287 ">}}
{{< tab "NVUE Commands ">}}

Cumulus Linux does not provide NVUE commands for this setting.

{{< /tab >}}
{{< tab "Linux Commands ">}}

Edit the `/etc/network/interfaces` file to **remove** the line `ipv6-addrgen off` from the VLAN stanza, then run the `ifreload -a` command.

{{< /tab >}}
{{< /tabs >}}

## MAC Address for a Bridge

To configure a MAC address for a bridge, run the `nv set bridge domain <bridge> mac-address <mac-address>` command.

The following example configures the bridge `br_default` with MAC address `00:00:5E:00:53:00`:

{{< tabs "TabID609 ">}}
{{< tab "NVUE Commands ">}}

```
cumulus@switch:~$ nv set bridge domain br_default mac-address 00:00:5E:00:53:00
cumulus@switch:~$ nv config apply
```

To unset the MAC address for a bridge, run the `nv unset bridge domain <bridge> mac-address <mac-address>` command.

```
cumulus@switch:~$ nv unset bridge domain br_default mac-address
cumulus@switch:~$ nv config apply
```

{{< /tab >}}
{{< tab "Linux Commands ">}}

Edit the `/etc/network/interfaces` file to add the MAC address (`hwaddress`) to the bridge stanza, then run the `sudo ifreload -a` command.

```
cumulus@switch:~$ sudo nano /etc/network/interfaces
...
auto br_default
iface br_default
    bridge-ports bond1 bond2 bond3 peerlink vxlan48
    hwaddress 00:00:5E:00:53:00
    bridge-vlan-aware yes
    bridge-vids 10 20 30
```

```
cumulus@switch:~$ sudo ifreload -a
```

To unset the MAC address for a bridge, remove the MAC address from the bridge stanza and run the `sudo ifreload -a` command.

{{< /tab >}}
{{< /tabs >}}

## MAC Address Ageing

By default, Cumulus Linux stores MAC addresses in the Ethernet switching table for 1800 seconds (30 minutes). You can change this setting to a value between 0 and 65535. A value of 0 disables MAC learning and frames flood out of all ports in a VLAN.

The following command example changes the MAC ageing setting to 600 seconds:

{{< tabs "TabID588 ">}}
{{< tab "NVUE Commands ">}}

```
cumulus@switch:~$ nv set bridge domain br_default ageing 600 
cumulus@switch:~$ nv config apply
```

{{< /tab >}}
{{< tab "Linux Commands ">}}

Edit the `/etc/network/interfaces` file to add the `bridge-ageing` parameter to the bridge interface:

```
cumulus@switch:~$ sudo nano /etc/network/interfaces
...
auto br_default
iface br_default
    bridge-ageing 600
...
```

{{< /tab >}}
{{< /tabs >}}

To show the bridge ageing configuration setting, run the `nv show bridge domain <domain>` command or the Linux `sudo ip -d link show <bridge-domain>` command.

```
cumulus@switch:~$ nv show bridge domain br_default
                 operational  applied   
---------------  -----------  ----------
ageing                        600
encap                         802.1Q
mac-address                   auto
type                          vlan-aware
untagged                      1
vlan-vni-offset               0
...
```

To reset bridge ageing to the default value (1800 seconds), run the `nv unset bridge domain <domain> ageing` command.

## Static MAC Address Entries

You can add a static MAC address entry to the layer 2 table for an interface within the VLAN-aware bridge by running a command similar to the following:

```
cumulus@switch:~$ sudo bridge fdb add 12:34:56:12:34:56 dev swp1 vlan 150 master static sticky
cumulus@switch:~$ sudo bridge fdb show
44:38:39:00:00:7c dev swp1 master bridge permanent
12:34:56:12:34:56 dev swp1 vlan 150 sticky master bridge static
44:38:39:00:00:7c dev swp1 self permanent
12:12:12:12:12:12 dev swp1 self permanent
12:34:12:34:12:34 dev swp1 self permanent
12:34:56:12:34:56 dev swp1 self permanent
12:34:12:34:12:34 dev bridge master bridge permanent
44:38:39:00:00:7c dev bridge vlan 500 master bridge permanent
12:12:12:12:12:12 dev bridge master bridge permanent
```

## Troubleshooting

To show the ports mapped to each bridge, run the NVUE `nv show bridge port` command or the Linux `bridge link show` command:

```
cumulus@switch:~$ nv show bridge port
domain                       port             
--------        ------------------------------
br_default      swp1,swp2,swp3
```

To show port information for a specific bridge, run the NVUE `nv show bridge domain <domain-name> port` command:

```
cumulus@switch:~$ nv show bridge domain br_default port
port  flags                       state     
----  --------------------------  ----------
swp1  flood,learning,mcast_flood  forwarding
swp2  flood,learning,mcast_flood  forwarding
swp3  flood,learning,mcast_flood  forwarding
```

To show the VLANs mapped to each bridge port, run the NVUE `nv show bridge port-vlan` command or the Linux `bridge vlan show` command:

```
cumulus@switch:~$ nv show bridge port-vlan
domain        port            vlan   tag-state
-------    ---------     ---------   ---------
br_default    swp1              10    untagged
              swp2               1    untagged
                                10      tagged
                                20      tagged
                                30      tagged
              swp3               1    untagged
                                10      tagged
                                20      tagged
                                30      tagged
```

To show VLAN information for a specific bridge, run the NVUE `nv show bridge domain <domain-name> port vlan` command or the Linux `bridge -d vlan show` command:

```
cumulus@switch:~$ nv show bridge domain br_default port vlan
port  vlan  tag-state  fwd-state 
----  ----  ---------  ----------
swp1  10    untagged   forwarding
swp2  1     untagged   forwarding
      10    tagged     forwarding
      20    tagged     forwarding
      30    tagged     forwarding
swp3  1     untagged   forwarding
      10    tagged     forwarding
      20    tagged     forwarding
      30    tagged     forwarding
```

## Example Configuration

The following example configuration contains an access port (swp51), a trunk carrying all VLANs (swp3 thru swp48), and a trunk pruning some VLANs from a switch port (swp2).

{{< tabs "TabID576 ">}}
{{< tab "NVUE ">}}

```
cumulus@switch:mgmt:~$ nv set interface swp3-48 bridge domain br_default
cumulus@switch:mgmt:~$ nv set bridge domain br_default vlan 310,700,707,712,850,910
cumulus@switch:mgmt:~$ nv set interface swp1 bridge domain br_default access 310
cumulus@switch:mgmt:~$ nv set interface swp1 bridge domain br_default stp bpdu-guard on
cumulus@switch:mgmt:~$ nv set interface swp1 bridge domain br_default stp admin-edge on
cumulus@switch:mgmt:~$ nv set interface swp2 bridge domain br_default vlan 707,712,850
cumulus@switch:mgmt:~$ nv set interface swp2 bridge domain br_default stp admin-edge on
cumulus@switch:mgmt:~$ nv set interface swp2 bridge domain br_default stp bpdu-guard on
cumulus@switch:mgmt:~$ nv set interface swp49 bridge domain br_default stp network on
cumulus@switch:mgmt:~$ nv set interface swp50 bridge domain br_default stp network on
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
            '310': {}
            '700': {}
            '707': {}
            '712': {}
            '850': {}
            '910': {}
    interface:
      swp1:
        bridge:
          domain:
            br_default:
              access: 310
              stp:
                admin-edge: on
                bpdu-guard: on
        type: swp
      swp2:
        bridge:
          domain:
            br_default:
              stp:
                admin-edge: on
                bpdu-guard: on
              vlan:
                '707': {}
                '712': {}
                '850': {}
        type: swp
      ...  
      swp49:
        bridge:
          domain:
            br_default:
              stp:
                network: on
        type: swp
      swp50:
        bridge:
          domain:
            br_default:
              stp:
                network: on
        type: swp
    system:
      hostname: switch
```

{{< /tab >}}
{{< tab "/etc/network/interfaces">}}

```
cumulus@switch:mgmt:~$ sudo cat /etc/network/interfaces
...
auto lo
iface lo inet loopback

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

# the following is an access port

auto swp1
iface swp1
    bridge-access 310
    mstpctl-bpduguard yes
    mstpctl-portadminedge yes

# the following is a trunk port that is pruned
# only .1q tags of 707, 712, 850 are sent and received

auto swp2
iface swp2
    bridge-vids 707 712 850
    mstpctl-bpduguard yes
    mstpctl-portadminedge yes
...
# the following port is the trunk uplink and inherits all vlans
# from br_default; bridge assurance is enabled using portnetwork

auto swp49
iface swp49
    mstpctl-portnetwork yes

# the following port is the trunk uplink and inherits all vlans
# from 'br_default'; bridge assurance is enabled using portnetwork

auto swp50
iface swp50
    mstpctl-portnetwork yes

# ports swp3-swp48 are trunk ports that inherit vlans 
# 310,700,707,712,850,910 from the bridge br_default

auto br_default
iface br_default
    bridge-ports swp1 swp2 swp3... swp49 swp50
    hwaddress 44:38:39:22:01:af
    bridge-vlan-aware yes
    bridge-vids 310 700 707 712 850 910
    bridge-pvid 1
```

{{< /tab >}}
{{< /tabs >}}

## Considerations

### Spanning Tree Protocol (STP)

- By default, STP runs in RSTP mode on a per-bridge basis. To configure STP to run in PVRST mode, where each VLAN runs its own instance of STP, see {{<link title="Spanning Tree and Rapid Spanning Tree - STP/#pvrst-mode-for-a-vlan-aware-bridge" text="PVRST Mode for a VLAN-aware Bridge">}}.
- `mstpd` remains the user space protocol daemon.

### VLAN Translation

You cannot enable VLAN translation on a bridge in VLAN-aware mode. Only traditional mode bridges support VLAN translation.

### Bridge Conversion

You cannot convert traditional mode bridges automatically to and from a VLAN-aware bridge. You must delete the original configuration and bring down all member switch ports before creating a new bridge.

### VLAN Memory Resource Limitations

On Spectrum-2 and later, Cumulus Linux uses internal debugging flow counters for each VLAN that require <span class="a-tooltip">[KVD](## "Key Value Database")</span> and <span class="a-tooltip">[ATCAM](## "Algorithmic TCAM")</span> memory space. When you configure more than 1000 VLAN interfaces, you might not be able to apply ACLs if flow counter resources deplete the ACL resource space. In addition, you might see error messages in the `/var/log/switchd.log` file similar to the following:

```
error: hw sync failed (sync_acl hardware installation failed) Rolling back .. failed.
error: hw sync failed (Bulk counter init failed with No More Resources). Rolling back ..
```

To troubleshoot this issue and manage netfilter resources with high VLAN and ACL scale, refer to {{<link url="Access-Control-List-Configuration/#troubleshooting-acl-rule-installation-failures" text="Troubleshooting ACL Rule Installation Failures">}}.
