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

You can associate different [SVIs](#vlan-layer-3-addressing) with each bridge by changing the `base-interface` value. The following example creates SVIs for VLAN 10 in both bridge1 and bridge2:


{{< tabs "TabID154 ">}}
{{< tab "NVUE Commands ">}}

```
cumulus@switch:~$ nv set interface bridge2_vlan10 type svi
cumulus@switch:~$ nv set interface bridge2_vlan10 vlan 10
cumulus@switch:~$ nv set interface bridge2_vlan10 base-interface bridge2
cumulus@switch:~$ nv set interface bridge2_vlan10 ip address 10.1.10.2/24
cumulus@switch:~$ nv set interface bridge1_vlan10 type svi
cumulus@switch:~$ nv set interface bridge1_vlan10 vlan 10
cumulus@switch:~$ nv set interface bridge1_vlan10 base-interface bridge1
cumulus@switch:~$ nv set interface bridge1_vlan10 ip address 192.168.10.2/24
cumulus@switch:~$ nv config apply
```

{{< /tab >}}
{{< tab "Linux Commands ">}}

Edit the `/etc/network/interfaces` file and add the bridge:

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
    address 192.168.10.2/24
    hwaddress 1c:34:da:1d:e6:fd
    vlan-raw-device bridge1
    vlan-id 10
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

The first time you configure a switch, all southbound bridge ports are down; therefore, by default, the SVI is also down. You can force the SVI to always be up by disabling interface state tracking so that the SVI is always in the UP state, even if all member ports are down. Other implementations describe this feature as *no autostate*. This is beneficial if you want to perform connectivity testing.

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

- STP runs on a per-bridge basis.
- `mstpd` remains the user space protocol daemon.
- Cumulus Linux supports {{<link url="Spanning-Tree-and-Rapid-Spanning-Tree-STP" text="Rapid Spanning Tree Protocol (RSTP)">}}.

### VLAN Translation

You cannot enable VLAN translation on a bridge in VLAN-aware mode. Only traditional mode bridges support VLAN translation.

### Bridge Conversion

You cannot convert traditional mode bridges automatically to and from a VLAN-aware bridge. You must delete the original configuration and bring down all member switch ports before creating a new bridge.
