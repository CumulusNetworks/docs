---
title: Virtual Router Redundancy - VRR and VRRP
author: NVIDIA
weight: 510
toc: 3
---
Cumulus Linux provides the option of using Virtual Router Redundancy (VRR) or Virtual Router Redundancy Protocol (VRRP).

- **VRR** enables hosts to communicate with any redundant router without reconfiguration, by running dynamic router protocols or router redundancy protocols. Redundant routers respond to Address Resolution Protocol (ARP) requests from hosts. Routers respond in an identical manner, but if one fails, the other redundant routers continue to respond. You use VRR with MLAG

   Use VRR when you connect multiple devices to a single logical connection, such as an MLAG bond. A device that connects to an MLAG bond believes there is a single device on the other end of the bond and only forwards one copy of the transit frames. If the destination of this frame is the virtual MAC address and you are running VRRP, the frame can go to the link connected to the VRRP standby device, which does not forward the frame to the right destination. With the virtual MAC active on both MLAG devices, either MLAG device handles the frame it receives.

- **VRRP** allows two or more network devices in an active or standby configuration to share a single virtual default gateway. The physical VRRP router that forwards packets at any given time is the master. If this VRRP router fails, another VRRP standby router automatically takes over as master. You use VRRP without MLAG.

   Use VRRP when you have multiple distinct devices that connect to a layer 2 segment through multiple logical connections (not through a single bond). VRRP elects a single active forwarder that *owns* the virtual MAC address while it is active. This prevents the forwarding database of the layer 2 domain from continuously updating in response to MAC flaps because the switch receives frames sourced from the virtual MAC address from discrete logical connections.

{{%notice note%}}
You cannot configure both VRR and VRRP on the same switch.
{{%/notice%}}

## VRR

The diagram below illustrates a basic VRR-enabled network configuration.

{{< img src = "/images/cumulus-linux/mlag-dual-connect.png" >}}

The network includes three hosts and two routers running Cumulus Linux that use {{<link url="Multi-Chassis-Link-Aggregation-MLAG" text="multi-chassis link aggregation">}} (MLAG).
- As the bridges in each of the redundant routers connect, they each receive and reply to ARP requests for the virtual router IP address.
- Each ARP request by a host receives replies from each switch; these replies are identical, and the host receiving the replies either ignores replies after the first, or accepts them and overwrites the previous identical reply.
- VRR reserves a range of MAC addresses to prevent MAC address conflicts with other interfaces in the same bridged network. The reserved range is `00:00:5E:00:01:00` to `00:00:5E:00:01:ff`.

   Use MAC addresses from the reserved range when configuring VRR. The reserved MAC address range for VRR is the same as for the Virtual Router Redundancy Protocol (VRRP).

### Configure the Routers

The routers implement the layer 2 network interconnecting the hosts and the redundant routers. To configure the routers, add a bridge with the following interfaces to each router:

- One bond interface or switch port interface to each host. For networks using MLAG, use bond interfaces. Otherwise, use switch port interfaces.
- One or more interfaces to each peer router. To accommodate higher bandwidth between the routers and to offer link redundancy, multiple inter-peer links are typically bonded interfaces. The VLAN interface must have a unique IP address for both the physical and virtual interface; the switch uses the unique address when it initiates an ARP request.

{{%notice note%}}
Cumulus Linux only supports VRR on switched virtual interfaces (SVIs). You cannot configure VRR on physical interfaces or virtual subinterfaces.
{{%/notice%}}

The example commands below create a VLAN-aware bridge interface for a VRR-enabled network. The example assumes you have already configured a VLAN-aware bridge with VLAN 10 and that VLAN 10 has an IP address:

{{< tabs "TabID53 ">}}
{{< tab "NCLU Commands ">}}

```
cumulus@switch:~$ net add vlan 10 ip address-virtual 00:00:5E:00:01:01 10.1.10.1/24
cumulus@switch:~$ net add vlan 10 ipv6 address-virtual 00:00:5e:00:01:00 10.1.20.1/24
cumulus@switch:~$ net pending
cumulus@switch:~$ net commit
```

{{< /tab >}}
{{< tab "NVUE Commands ">}}

```
cumulus@switch:~$ nv set interface vlan10 ip vrr address 10.1.10.1/24
cumulus@switch:~$ nv set interface vlan10 ip vrr mac-address 00:00:5e:00:01:00
cumulus@switch:~$ nv set interface vlan10 ip vrr state up
cumulus@switch:~$ nv config apply
```

Use the same commands for IPV6 addresses; for example:

```
cumulus@switch:~$ nv set interface vlan10 ip vrr address 2001:db8::1/32
cumulus@switch:~$ nv set interface vlan10 ip vrr mac-address 00:00:5e:00:01:00
cumulus@switch:~$ nv set interface vlan10 ip vrr state up
```

{{< /tab >}}
{{< tab "Linux Commands ">}}

Edit the `/etc/network/interfaces` file, then run the `ifreload -a` command.

```
cumulus@switch:~$ sudo nano /etc/network/interfaces
...
auto vlan10
iface vlan10
    address 10.1.10.2/24
    address-virtual 00:00:5e:00:01:00 10.1.10.1/24
    vlan-raw-device br_default
    vlan-id 10
...
```

```
cumulus@switch:~$ sudo ifreload -a
```

{{< /tab >}}
{{< /tabs >}}

### Configure the Hosts

Each host must have two network interfaces. The routers configure the interfaces as bonds running LACP; the hosts must also configure the two interfaces using teaming, port aggregation, port group, or EtherChannel running LACP. Configure the hosts either statically or with DHCP, with a gateway address that is the IP address of the virtual router; this default gateway address never changes.

Configure the links between the hosts and the routers in *active-active* mode for First Hop Redundancy Protocol.

### Example VRR Configuration with MLAG

To create an {{<link url="Multi-Chassis-Link-Aggregation-MLAG" text="MLAG">}} configuration that incorporates VRR, use a configuration similar to the following.

{{%notice note%}}
The following examples uses a single virtual MAC address for VLANs. You can add a unique MAC address for each VLAN, but this is not necessary.
{{%/notice%}}

{{< tabs "TabID116 ">}}
{{< tab "leaf01 ">}}

{{< tabs "TabID119 ">}}
{{< tab "NCLU Commands ">}}

```
cumulus@leaf01:~$ net add interface eth0 ip address 192.168.200.11/24
cumulus@leaf01:~$ net add bond bond1 bond slaves swp1
cumulus@leaf01:~$ net add bond bond2 bond slaves swp2
cumulus@leaf01:~$ net add bond bond1 clag id 1
cumulus@leaf01:~$ net add bond bond2 clag id 2
cumulus@leaf01:~$ net add bridge bridge ports bond1,bond2
cumulus@leaf01:~$ net add clag peer sys-mac 44:38:39:BE:EF:AA interface swp49-50 primary backup-ip 10.10.10.2
cumulus@leaf01:~$ net add vlan 10 ip address 10.1.10.2/24
cumulus@leaf01:~$ net add vlan 10 ip address-virtual 00:00:5E:00:01:01 10.1.10.1/24
cumulus@leaf01:~$ net add vlan 20 ip address 10.1.20.2/24
cumulus@leaf01:~$ net add vlan 20 ip address-virtual 00:00:5E:00:01:01 10.1.20.1/24
cumulus@leaf01:~$ net pending
cumulus@leaf01:~$ net commit
```

{{< /tab >}}
{{< tab "NVUE Commands ">}}

```
cumulus@leaf01:~$ nv set interface eth0 ip address 192.168.200.11/24
cumulus@leaf01:~$ nv set interface bond1 bond member swp1
cumulus@leaf01:~$ nv set interface bond2 bond member swp2
cumulus@leaf01:~$ nv set interface bond1 bond mlag id 1
cumulus@leaf01:~$ nv set interface bond2 bond mlag id 2
cumulus@leaf01:~$ nv set interface bond1-2 bridge domain br_default
cumulus@leaf01:~$ nv set interface peerlink bond member swp49-50
cumulus@leaf01:~$ nv set mlag mac-address 44:38:39:BE:EF:AA
cumulus@leaf01:~$ nv set mlag backup 10.10.10.2
cumulus@leaf01:~$ nv set mlag peer-ip linklocal
cumulus@leaf01:~$ nv set bridge domain br_default vlan 10,20
cumulus@leaf01:~$ nv set bridge domain br_default untagged 1
cumulus@leaf01:~$ nv set interface vlan10 ip address 10.1.10.2/24
cumulus@leaf01:~$ nv set interface vlan10 ip vrr address 10.1.10.1/24
cumulus@leaf01:~$ nv set interface vlan10 ip vrr mac-address 00:00:5e:00:01:00
cumulus@leaf01:~$ nv set interface vlan10 ip vrr state up
cumulus@leaf01:~$ nv set interface vlan20 ip address 10.1.20.2/24
cumulus@leaf01:~$ nv set interface vlan20 ip vrr address 10.1.20.1/24
cumulus@leaf01:~$ nv set interface vlan20 ip vrr mac-address 00:00:5e:00:01:00
cumulus@leaf01:~$ nv set interface vlan20 ip vrr state up
cumulus@leaf01:~$ nv config apply
```

{{< /tab >}}
{{< tab "/etc/network/interfaces">}}

```
auto lo
iface lo inet loopback

auto mgmt
iface mgmt
    address 127.0.0.1/8
    address ::1/128
    vrf-table auto

auto eth0
iface eth0 inet dhcp
    address 192.168.200.11/24
    ip-forward off
    ip6-forward off
    vrf mgmt

auto bond1
iface bond1
    bond-slaves swp1
    bond-mode 802.3ad
    bond-lacp-bypass-allow no
    clag-id 1

auto bond2
iface bond2
    bond-slaves swp2
    bond-mode 802.3ad
    bond-lacp-bypass-allow no
    clag-id 2

auto peerlink
iface peerlink
    bond-slaves swp49 swp50
    bond-mode 802.3ad
    bond-lacp-bypass-allow no

auto peerlink.4094
iface peerlink.4094
    clagd-peer-ip linklocal
    clagd-backup-ip 10.10.10.2
    clagd-sys-mac 44:38:39:BE:EF:AA
    clagd-args --initDelay 180

auto vlan10
iface vlan10
    address 10.1.10.2/24
    address-virtual 00:00:5e:00:01:00 10.1.10.1/24
    vlan-raw-device br_default
    vlan-id 10

auto vlan20
iface vlan20
    address 10.1.20.2/24
    address-virtual 00:00:5e:00:01:00 10.1.20.1/24
    vlan-raw-device br_default
    vlan-id 20

auto br_default
iface br_default
    bridge-ports peerlink bond1 bond2
    bridge-vlan-aware yes
    bridge-vids 10 20
    bridge-pvid 1
```

{{< /tab >}}
{{< /tabs >}}

{{< /tab >}}
{{< tab "leaf02 ">}}

{{< tabs "TabID246 ">}}
{{< tab "NVUE Commands ">}}

```
cumulus@leaf02:~$ nv set interface eth0 ip address 192.168.200.12/24
cumulus@leaf02:~$ nv set interface bond1 bond member swp1
cumulus@leaf02:~$ nv set interface bond2 bond member swp2
cumulus@leaf02:~$ nv set interface bond1 bond mlag id 1
cumulus@leaf02:~$ nv set interface bond2 bond mlag id 2
cumulus@leaf02:~$ nv set interface bond1-2 bridge domain br_default
cumulus@leaf02:~$ nv set interface peerlink bond member swp49-50
cumulus@leaf02:~$ nv set mlag mac-address 44:38:39:BE:EF:AA
cumulus@leaf02:~$ nv set mlag backup 10.10.10.1
cumulus@leaf02:~$ nv set mlag peer-ip linklocal
cumulus@leaf02:~$ nv set bridge domain br_default vlan 10,20
cumulus@leaf02:~$ nv set bridge domain br_default untagged 1
cumulus@leaf02:~$ nv set interface vlan10 ip address 10.1.10.3/24
cumulus@leaf02:~$ nv set interface vlan10 ip vrr address 10.1.10.1/24
cumulus@leaf02:~$ nv set interface vlan10 ip vrr mac-address 00:00:5e:00:01:00
cumulus@leaf02:~$ nv set interface vlan10 ip vrr state up
cumulus@leaf02:~$ nv set interface vlan20 ip address 10.1.20.3/24
cumulus@leaf02:~$ nv set interface vlan20 ip vrr address 10.1.20.1/24
cumulus@leaf02:~$ nv set interface vlan20 ip vrr mac-address 00:00:5e:00:01:00
cumulus@leaf02:~$ nv set interface vlan20 ip vrr state up
cumulus@leaf02:~$ nv config apply
```

{{< /tab >}}
{{< tab "/etc/network/interfaces ">}}

```
auto lo
iface lo inet loopback

auto mgmt
iface mgmt
    address 127.0.0.1/8
    address ::1/128
    vrf-table auto

auto eth0
iface eth0
    address 192.168.200.12/24
    ip-forward off
    ip6-forward off
    vrf mgmt

auto bond1
iface bond1
    bond-slaves swp1
    bond-mode 802.3ad
    bond-lacp-bypass-allow no
    clag-id 1

auto bond2
iface bond2
    bond-slaves swp2
    bond-mode 802.3ad
    bond-lacp-bypass-allow no
    clag-id 2

auto peerlink
iface peerlink
    bond-slaves swp49 swp50
    bond-mode 802.3ad
    bond-lacp-bypass-allow no

auto peerlink.4094
iface peerlink.4094
    clagd-peer-ip linklocal
    clagd-backup-ip 10.10.10.1
    clagd-sys-mac 44:38:39:BE:EF:AA
    clagd-args --initDelay 180

auto vlan10
iface vlan10
    address 10.1.10.3/24
    address-virtual 00:00:5e:00:01:00 10.1.10.1/24
    vlan-raw-device br_default
    vlan-id 10

auto vlan20
iface vlan20
    address 10.1.20.3/24
    address-virtual 00:00:5e:00:01:00 10.1.20.1/24
    vlan-raw-device br_default
    vlan-id 20

auto br_default
iface br_default
    bridge-ports peerlink bond1 bond2
    bridge-vlan-aware yes
    bridge-vids 10 20
    bridge-pvid 1
```

{{< /tab >}}
{{< /tabs >}}

{{< /tab >}}
{{< tab "server01 ">}}

Create a configuration similar to the following on an Ubuntu host:

```
auto eth0
iface eth0 inet dhcp

auto eth1
iface eth1 inet manual
    bond-master uplink

auto eth2
iface eth2 inet manual
    bond-master uplink

auto uplink
iface uplink inet static
    bond-slaves eth1 eth2
    bond-mode 802.3ad
    bond-miimon 100
    bond-lacp-rate 1
    bond-min-links 1
    bond-xmit-hash-policy layer3+4
    address 172.16.1.101
    netmask 255.255.255.0
    post-up ip route add 172.16.0.0/16 via 172.16.1.1
    post-up ip route add 10.0.0.0/8 via 172.16.1.1

auto uplink:200
iface uplink:200 inet static
    address 10.0.2.101

auto uplink:300
iface uplink:300 inet static
    address 10.0.3.101

auto uplink:400
iface uplink:400 inet static
    address 10.0.4.101

# modprobe bonding
```

{{< /tab >}}
{{< tab "server02 ">}}

Create a configuration similar to the following on an Ubuntu host:

```
auto eth0
iface eth0 inet dhcp

auto eth1
iface eth1 inet manual
    bond-master uplink

auto eth2
iface eth2 inet manual
    bond-master uplink

auto uplink
iface uplink inet static
    bond-slaves eth1 eth2
    bond-mode 802.3ad
    bond-miimon 100
    bond-lacp-rate 1
    bond-min-links 1
    bond-xmit-hash-policy layer3+4
    address 172.16.1.101
    netmask 255.255.255.0
    post-up ip route add 172.16.0.0/16 via 172.16.1.1
    post-up ip route add 10.0.0.0/8 via 172.16.1.1

auto uplink:200
iface uplink:200 inet static
    address 10.0.2.101

auto uplink:300
iface uplink:300 inet static
    address 10.0.3.101

auto uplink:400
iface uplink:400 inet static
    address 10.0.4.101

# modprobe bonding
```

{{< /tab >}}
{{< /tabs >}}

## VRRP

VRRP allows two or more network devices in an active standby configuration to share a single virtual default gateway. The VRRP router that forwards packets at any given time is the master. If this VRRP router fails, another VRRP standby router automatically takes over as master. The master sends VRRP advertisements to other VRRP routers in the same virtual router group, which include the priority and state of the master. VRRP router priority determines the role that each virtual router plays and who becomes the new master if the master fails.

All virtual routers use 00:00:5E:00:01:XX for IPv4 gateways or 00:00:5E:00:02:XX for IPv6 gateways as their MAC address. The last byte of the address is the Virtual Router IDentifier (VRID), which is different for each virtual router in the network. Only one physical router uses this MAC address at a time. The router replies with this address when it receives ARP requests or neighbor solicitation packets for the IP addresses of the virtual router.

{{%notice note%}}
- Cumulus Linux supports both VRRPv2 and VRRPv3. The default protocol version is VRRPv3.
- You can configure a maximum of 255 virtual routers on a switch.
- You cannot use VRRP with MLAG.
- To configure VRRP on an SVI or {{<link url="Traditional-Bridge-Mode" text="traditional mode bridge">}}, you need to edit the `etc/network/interfaces` and `/etc/frr/frr.conf` files. NCLU commands do not support SVIs or traditional mode bridges.
- You can use VRRP with layer 3 interfaces and subinterfaces that are part of a [VRF](## "Virtual Routing and Forwarding").
- You cannot use VRRP in an [EVPN](## "Ethernet Virtual Private Network") configuration; use MLAG and VRR instead.
{{%/notice%}}

{{<exlink url="https://tools.ietf.org/html/rfc5798#section-4.1" text="RFC 5798">}} describes VRRP in detail.

The following example illustrates a basic VRRP configuration.

{{< img src = "/images/cumulus-linux/vrrp-example.png" >}}

### Configure VRRP

To configure VRRP, specify the following information on each switch:

- **A virtual router ID (VRID) that identifies the group of VRRP routers**. You must specify the same ID across all virtual routers in the group.
- **One or more virtual IP addresses for the virtual router group**. These IP addresses do not directly connect to a specific interface. The switch redirects inbound packets to a virtual IP address to a physical network interface.

You can also set these optional parameters:

| Optional Parameter | Default Value | Description|
| -----------| -------------| ------------- |
| `priority` | 100 | The priority level of the virtual router within the virtual router group, which determines the role that each virtual router plays and what happens if the master fails. Virtual routers have a priority between 1 and 254; the router with the highest priority becomes the master. |
| `advertisement interval` | 1000 milliseconds | The advertisement interval is the interval between successive advertisements by the master in a virtual router group. You can specify a value between 10 and 40950.|
| `preempt` | enabled | Preempt mode lets the router take over as master for a virtual router group if it has a higher priority than the current master. Preempt mode is on by default. To disable preempt mode, edit the `/etc/frr/frr.conf` file to add the line `no vrrp <VRID> preempt` to the interface stanza, then restart the FRR service.|

The following example commands configure two switches (spine01 and spine02) that form one virtual router group (VRID 44) with IPv4 address 10.0.0.1/24 and IPv6 address 2001:0db8::1/64. *spine01* is the master; it has a priority of 254. *spine02* is the backup VRRP router.

{{%notice note%}}
The parent interface must use a primary address as the source address on VRRP advertisement packets.
{{%/notice%}}

{{< tabs "TabID448 ">}}
{{< tab "NCLU Commands ">}}

{{%notice info%}}
When you commit a change that configures a new routing service such as VRRP, the FRR daemon restarts and might interrupt network operations for other configured routing services.
{{%/notice%}}

{{< tabs "TabID526 ">}}
{{< tab "spine01 ">}}

```
cumulus@spine01:~$ net add interface swp1 ip address 10.0.0.2/24
cumulus@spine01:~$ net add interface swp1 ipv6 address 2001:0db8::2/64
cumulus@spine01:~$ net add interface swp1 vrrp 44 10.0.0.1/24
cumulus@spine01:~$ net add interface swp1 vrrp 44 2001:0db8::1/64
cumulus@spine01:~$ net add interface swp1 vrrp 44 priority 254
cumulus@spine01:~$ net add interface swp1 vrrp 44 advertisement-interval 5000
cumulus@spine01:~$ net pending
cumulus@spine01:~$ net commit
```

{{< /tab >}}
{{< tab "spine02 ">}}

```
cumulus@spine02:~$ net add interface swp1 ip address 10.0.0.3/24
cumulus@spine02:~$ net add interface swp1 ipv6 address 2001:0db8::3/64
cumulus@spine02:~$ net add interface swp1 vrrp 44 10.0.0.1/24
cumulus@spine02:~$ net add interface swp1 vrrp 44 2001:0db8::1/64
cumulus@spine02:~$ net pending
cumulus@spine02:~$ net commit
```

{{< /tab >}}
{{< /tabs >}}

{{< /tab >}}
{{< tab "NVUE Commands ">}}

{{< tabs "TabID504 ">}}
{{< tab "spine01 ">}}

NVUE commands are not supported.

{{< /tab >}}
{{< tab "spine02 ">}}

NVUE commands are not supported.

{{< /tab >}}
{{< /tabs >}}

{{< /tab >}}
{{< tab "Linux and vtysh Commands ">}}

{{< tabs "TabID557 ">}}
{{< tab "spine01 ">}}

1. Edit the `/etc/network/interface` file to assign an IP address to the parent interface; for example:

   ```
   cumulus@spine01:~$ sudo vi /etc/network/interfaces
   ...
   auto swp1
   iface swp1
       address 10.0.0.2/24
       address 2001:0db8::2/64
   ```

2. Enable the `vrrpd` daemon, then start the FRRouting service. See {{<link title="FRRouting">}}.

3. From the vtysh shell, configure VRRP.

    ```
    cumulus@spine01:~$ sudo vtysh

    spine01# configure terminal
    spine01(config)# interface swp1
    spine01(config-if)# vrrp 44 ip 10.0.0.1
    spine01(config-if)# vrrp 44 ipv6 2001:0db8::1
    spine01(config-if)# vrrp 44 priority 254
    spine01(config-if)# vrrp 44 advertisement-interval 5000
    spine01(config-if)# end
    spine01# write memory
    spine01# exit
    ```

{{< /tab >}}
{{< tab "spine02 ">}}

1. Edit the `/etc/network/interface` file to assign an IP address to the parent interface; for example:

   ```
   cumulus@spine02:~$ sudo vi /etc/network/interfaces
   ...
   auto swp1
   iface swp1
       address 10.0.0.3/24
       address 2001:0db8::3/64
   ```

2. Enable the `vrrpd` daemon, then start the FRRouting service. See {{<link title="FRRouting">}}.

3. From the vtysh shell, configure VRRP.

   ```
   cumulus@spine02:~$ sudo vtysh

   spine02# configure terminal
   spine02(config)# interface swp1
   spine02(config-if)# vrrp 44 ip 10.0.0.1
   spine02(config-if)# vrrp 44 ipv6 2001:0db8::1
   spine02(config-if)# end
   spine02# write memory
   spine02# exit
   ```

{{< /tab >}}
{{< /tabs >}}

{{< /tab >}}
{{< /tabs >}}

The NCLU and vtysh commands save the configuration in the `/etc/network/interfaces` file and the `/etc/frr/frr.conf` file. For example:

```
cumulus@spine01:~$ sudo cat /etc/network/interfaces
...
auto swp1
iface swp1
    address 10.0.0.2/24
    address 2001:0db8::2/64
    vrrp 44 10.0.0.1/24 2001:0db8::1/64
...
```

```
cumulus@spine01:~$ sudo cat /etc/frr/frr.conf
...
interface swp1
vrrp 44
vrrp 44 advertisement-interval 5000
vrrp 44 priority 254
vrrp 44 ip 10.0.0.1
vrrp 44 ipv6 2001:0db8::1
...
```

### Show VRRP Configuration

To show virtual router information on a switch, run the NCLU `net show vrrp <VRID>` command or the vtysh `show vrrp <VRID>` command. For example:

```
cumulus@spine01:~$ net show vrrp 44
Virtual Router ID                    44
Protocol Version                     3
Autoconfigured                       No
Shutdown                             No
Interface                            swp1
 VRRP interface (v4)                 vrrp4-3-1
VRRP interface (v6)                  vrrp6-3-1
Primary IP (v4)                      10.0.0.2
Primary IP (v6)                      2001:0db8::2
Virtual MAC (v4)                     00:00:5e:00:01:01
Virtual MAC (v6)                     00:00:5e:00:02:01
Status (v4)                          Master
Status (v6)                          Master
Priority                             254
Effective Priority (v4)              254
Effective Priority (v6)              254
Preempt Mode                         Yes
Accept Mode                          Yes
Advertisement Interval               5000 ms
Master Advertisement Interval (v4)   0 ms
Master Advertisement Interval (v6)   5000 ms
Advertisements Tx (v4)               17
Advertisements Tx (v6)               17
Advertisements Rx (v4)               0
Advertisements Rx (v6)               0
Gratuitous ARP Tx (v4)               1
Neigh. Adverts Tx (v6)               1
State transitions (v4)               2
State transitions (v6)               2
Skew Time (v4)                       0 ms
Skew Time (v6)                       0 ms
Master Down Interval (v4)            0 ms
Master Down Interval (v6)            0 ms
IPv4 Addresses                       1
. . . . . . . . . . . . . . . . . .  10.0.0.1
IPv6 Addresses                       1
. . . . . . . . . . . . . . . . . .  2001:0db8::1
```
