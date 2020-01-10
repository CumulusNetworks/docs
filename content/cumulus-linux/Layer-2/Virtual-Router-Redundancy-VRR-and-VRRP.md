---
title: Virtual Router Redundancy - VRR and VRRP
author: Cumulus Networks
weight: 129
aliases:
 - /display/DOCS/Virtual+Router+Redundancy+++VRR+and+VRRP
 - /pages/viewpage.action?pageId=8366414
 - /display/DOCS/Virtual+Router+Redundancy+VRR+and+VRRP
product: Cumulus Linux
version: '4.0'
---
Cumulus Linux provides the option of using Virtual Router Redundancy (VRR) or Virtual Router Redundancy Protocol (VRRP).

**VRR** enables hosts to communicate with any redundant router without reconfiguration, running dynamic router protocols, or running router redundancy protocols. This means that redundant routers respond to Address Resolution Protocol (ARP) requests from hosts. Routers are configured to respond in an identical manner, but if one fails, the other redundant routers continue to respond, leaving the hosts with the impression that nothing has changed. VRR is typically used in an MLAG configuration.

**VRRP** allows a single virtual default gateway to be shared between two or more network devices in an active/standby configuration. The physical VRRP router that forwards packets at any given time is called the master. If this VRRP router fails, another VRRP standby router automatically takes over as master. VRRP is used in a non-MLAG configuration.

{{%notice note%}}

You cannot configure both VRR and VRRP on the same switch.

{{%/notice%}}

## VRR

The diagram below illustrates a basic VRR-enabled network configuration. The network includes several hosts and two routers running Cumulus Linux configured with [Multi-chassis Link Aggregation](../Multi-Chassis-Link-Aggregation-MLAG/) (MLAG).

{{%notice note%}}

Cumulus Linux only supports VRR on switched virtual interfaces (SVIs). VRR is not supported on physical interfaces or virtual subinterfaces.

{{%/notice%}}

{{< img src = "/images/cumulus-linux/vrr-active-active.png" >}}

A production implementation has many more server hosts and network connections than are shown here. However, this basic configuration provides a complete description of the important aspects of the VRR setup.

As the bridges in each of the redundant routers are connected, they will each receive and reply to ARP requests for the virtual router IP address.

Each ARP request made by a host will receive replies from each router; these replies will be identical, and so the host receiving the replies will either ignore replies after the first, or accept them and overwrite the previous identical reply, rather than being confused over which response is correct.

A range of MAC addresses is reserved for use with VRR to prevent MAC address conflicts with other interfaces in the same bridged network. The reserved range is `00:00:5E:00:01:00` to `00:00:5E:00:01:ff`.

Cumulus Networks recommends using MAC addresses from the reserved range when configuring VRR.

The reserved MAC address range for VRR is the same as for the Virtual Router Redundancy Protocol (VRRP), as they serve similar purposes.

### Configure the Routers

The routers implement the layer 2 network interconnecting the hosts and the redundant routers. To configure the routers, add a bridge with the following interfaces to each router:

- One bond interface or switch port interface to each host. For networks using MLAG, use bond interfaces. Otherwise, use switch port interfaces.
- One or more interfaces to each peer router. To accommodate higher bandwidth between the routers and to offer link redundancy, multiple inter-peer links are typically bonded interfaces. The VLAN interface must have unique IP addresses for both the physical (the `address` option below) and virtual (the `address-virtual` option below) interfaces; the unique address is used when the switch initiates an ARP request.

<details>

<summary>NCLU Commands </summary>

The example NCLU commands below create a VLAN-aware bridge interface for a VRR-enabled network:

```
cumulus@switch:~$ net add bridge
cumulus@switch:~$ net add vlan 500 ip address 192.0.2.252/24
cumulus@switch:~$ net add vlan 500 ip address-virtual 00:00:5e:00:01:00 192.0.2.254/24
cumulus@switch:~$ net add vlan 500 ipv6 address 2001:db8::1/32
cumulus@switch:~$ net add vlan 500 ipv6 address-virtual 00:00:5e:00:01:00 2001:db8::f/32
cumulus@switch:~$ net pending
cumulus@switch:~$ net commit
```

</details>

<details>

<summary>Linux Commands </summary>

Edit the `/etc/network/interfaces` file. The example file configuration below create a VLAN-aware bridge interface for a VRR-enabled network:

```
cumulus@switch:~$ sudo nano /etc/network/interfaces
...
auto bridge
iface bridge
    bridge-vids 500
    bridge-vlan-aware yes

auto vlan500
iface vlan500
    address 192.0.2.252/24
    address 2001:db8::1/32
    address-virtual 00:00:5e:00:01:00 2001:db8::f/32 192.0.2.254/24
    vlan-id 500
    vlan-raw-device bridge
...
```

Run the `ifreload -a` command to reload the configuration:

```
cumulus@switch:~$ sudo ifreload -a
```

</details>

### Configure the Hosts

Each host must have two network interfaces. The routers configure the interfaces as bonds running LACP; the hosts must also configure its two interfaces using teaming, port aggregation, port group, or EtherChannel running LACP. Configure the hosts either statically or with DHCP, with a gateway address that is the IP address of the virtual router; this default gateway address never changes.

Configure the links between the hosts and the routers in *active-active* mode for First Hop Redundancy Protocol.

### Example VRR Configuration with MLAG

To create an [MLAG](../Multi-Chassis-Link-Aggregation-MLAG/) configuration that incorporates VRR, use a configuration like the following:

<details>

<summary>**leaf01 Configuration**</summary>

```
cumulus@leaf01:~$ net add interface eth0 ip address 192.168.0.21
cumulus@leaf01:~$ net add bond server01 bond slaves swp1-2
cumulus@leaf01:~$ net add bond server01 clag id 1
cumulus@leaf01:~$ net add bond server01 mtu 9216
cumulus@leaf01:~$ net add bond server01 alias LACP etherchannel to uplink on server01
cumulus@leaf01:~$ net add bond peerlink bond slaves swp49-50
cumulus@leaf01:~$ net add interface peerlink.4094 peerlink.4094
cumulus@leaf01:~$ net add interface peerlink.4094 ip address 169.254.255.1/30
cumulus@leaf01:~$ net add interface peerlink.4094 clag peer-ip 169.254.255.2
cumulus@leaf01:~$ net add interface peerlink.4094 clag backup-ip 192.168.0.22
cumulus@leaf01:~$ net add interface peerlink.4094 clag sys-mac 44:38:39:FF:40:90
cumulus@leaf01:~$ net add bridge bridge ports server01,peerlink
cumulus@leaf01:~$ net add bridge stp treeprio 4096
cumulus@leaf01:~$ net add vlan 100 ip address 10.0.1.2/24
cumulus@leaf01:~$ net add vlan 100 ip address-virtual 00:00:5E:00:01:01 10.0.1.1/24
cumulus@leaf01:~$ net add vlan 200 ip address 10.0.2.2/24
cumulus@leaf01:~$ net add vlan 200 ip address-virtual 00:00:5E:00:01:02 10.0.2.1/24
cumulus@leaf01:~$ net add vlan 300 ip address 10.0.3.2/24
cumulus@leaf01:~$ net add vlan 300 ip address-virtual 00:00:5E:00:01:03 10.0.3.1/24
cumulus@leaf01:~$ net add vlan 400 ip address 10.0.4.2/24
cumulus@leaf01:~$ net add vlan 400 ip address-virtual 00:00:5E:00:01:04 10.0.4.1/24
cumulus@leaf01:~$ net pending
cumulus@leaf01:~$ net commit
```

These commands create the following configuration in the `/etc/network/interfaces` file:

```
auto eth0
iface eth0
    address 192.168.0.21

auto bridge
iface bridge
    bridge-ports server01 peerlink
    bridge-vids 100 200 300 400
    bridge-vlan-aware yes
    mstpctl-treeprio 4096

auto server01
iface server01
    alias LACP etherchannel to uplink on server01
    bond-slaves swp1 swp2
    clag-id 1
    mtu 9216

auto peerlink
iface peerlink
    bond-slaves swp49 swp50

auto peerlink.4094
iface peerlink.4094
    address 169.254.255.1/30
    clagd-backup-ip 192.168.0.22
    clagd-peer-ip 169.254.255.2
    clagd-sys-mac 44:38:39:FF:40:90

auto vlan100
iface vlan100
    address 10.0.1.2/24
    address-virtual 00:00:5E:00:01:01 10.0.1.1/24
    vlan-id 100
    vlan-raw-device bridge

auto vlan200
iface vlan200
    address 10.0.2.2/24
    address-virtual 00:00:5E:00:01:02 10.0.2.1/24
    vlan-id 200
    vlan-raw-device bridge

auto vlan300
iface vlan300
    address 10.0.3.2/24
    address-virtual 00:00:5E:00:01:03 10.0.3.1/24
    vlan-id 300
    vlan-raw-device bridge

auto vlan400
iface vlan400
    address 10.0.4.2/24
    address-virtual 00:00:5E:00:01:04 10.0.4.1/24
    vlan-id 400
    vlan-raw-device bridge
```

</details>

<details>

<summary>**leaf02 Configuration** </summary>

```
cumulus@leaf02:~$ net add interface eth0 ip address 192.168.0.22
cumulus@leaf02:~$ net add bond server01 bond slaves swp1-2
cumulus@leaf02:~$ net add bond server01 clag id 1
cumulus@leaf02:~$ net add bond server01 mtu 9216
cumulus@leaf02:~$ net add bond server01 alias LACP etherchannel to uplink on server01
cumulus@leaf02:~$ net add bond peerlink bond slaves swp49-50
cumulus@leaf02:~$ net add interface peerlink.4094 peerlink.4094
cumulus@leaf02:~$ net add interface peerlink.4094 ip address 169.254.255.2/30
cumulus@leaf02:~$ net add interface peerlink.4094 clag peer-ip 169.254.255.1
cumulus@leaf02:~$ net add interface peerlink.4094 clag backup-ip 192.168.0.21
cumulus@leaf02:~$ net add interface peerlink.4094 clag sys-mac 44:38:39:FF:40:90
cumulus@leaf02:~$ net add bridge bridge ports server01,peerlink
cumulus@leaf02:~$ net add bridge stp treeprio 4096
cumulus@leaf02:~$ net add vlan 100 ip address 10.0.1.3/24
cumulus@leaf02:~$ net add vlan 100 ip address-virtual 00:00:5E:00:01:01 10.0.1.1/24
cumulus@leaf02:~$ net add vlan 200 ip address 10.0.2.3/24
cumulus@leaf02:~$ net add vlan 200 ip address-virtual 00:00:5E:00:01:02 10.0.2.1/24
cumulus@leaf02:~$ net add vlan 300 ip address 10.0.3.3/24
cumulus@leaf02:~$ net add vlan 300 ip address-virtual 00:00:5E:00:01:03 10.0.3.1/24
cumulus@leaf02:~$ net add vlan 400 ip address 10.0.4.3/24
cumulus@leaf02:~$ net add vlan 400 ip address-virtual 00:00:5E:00:01:04 10.0.4.1/24
cumulus@leaf02:~$ net pending
cumulus@leaf02:~$ net commit
```

These commands create the following configuration in the `/etc/network/interfaces` file:

```
auto eth0
iface eth0
    address 192.168.0.22

auto bridge
iface bridge
    bridge-ports server01 peerlink
    bridge-vids 100 200 300 400
    bridge-vlan-aware yes
    mstpctl-treeprio 4096

auto server01
iface server01
    alias LACP etherchannel to uplink on server01
    bond-slaves swp1 swp2
    clag-id 1
    mtu 9216

auto peerlink
iface peerlink
    bond-slaves swp49 swp50

auto peerlink.4094
iface peerlink.4094
    address 169.254.255.1/30
    clagd-backup-ip 192.168.0.22
    clagd-peer-ip 169.254.255.2
    clagd-sys-mac 44:38:39:FF:40:90

auto vlan100
iface vlan100
    address 10.0.1.3/24
    address-virtual 00:00:5E:00:01:01 10.0.1.1/24
    vlan-id 100
    vlan-raw-device bridge

auto vlan200
iface vlan200
    address 10.0.2.3/24
    address-virtual 00:00:5E:00:01:02 10.0.2.1/24
    vlan-id 200
    vlan-raw-device bridge

auto vlan300
iface vlan300
    address 10.0.3.3/24
    address-virtual 00:00:5E:00:01:03 10.0.3.1/24
    vlan-id 300
    vlan-raw-device bridge

auto vlan400
iface vlan400
    address 10.0.4.3/24
    address-virtual 00:00:5E:00:01:04 10.0.4.1/24
    vlan-id 400
    vlan-raw-device bridge
```

</details>

<details>

<summary>**server01 Configuration** </summary>

Create a configuration like the following on an Ubuntu host:

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

</details>

<details>

<summary>**server02 Configuration** </summary>

Create a configuration like the following on an Ubuntu host:

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

</details>

## VRRP

VRRP allows for a single virtual default gateway to be shared among two or more network devices in an active standby configuration. The VRRP router that forwards packets at any given time is called the master. If this VRRP router fails, another VRRP standby router automatically takes over as master. The master sends VRRP advertisements to other VRRP routers in the same virtual router group, which include the priority and state of the master. VRRP router priority determines the role that each virtual router plays and who becomes the new master if the master fails.

All virtual routers use 00:00:5E:00:01:XX for IPv4 gateways or 00:00:5E:00:02:XX for IPv6 gateways as their MAC address. The last byte of the address is the Virtual Router IDentifier (VRID), which is different for each virtual router in the network. This MAC address is used by only one physical router at a time, which replies with this address when ARP requests or neighbor solicitation packets are sent for the IP addresses of the virtual router.

{{%notice note%}}

- Cumulus Linux supports both VRRPv2 and VRRPv3. The default protocol version is VRRPv3.

- 255 virtual routers are supported per switch.

- VRRP is not supported currently in an MLAG environment or with EVPN.

- To configure VRRP on an SVI, you need to edit the `/etc/frr/frr.conf` file; The NCLU commands are not supported for SVIs.

{{%/notice%}}

[RFC 5798](https://tools.ietf.org/html/rfc5798#section-4.1) describes VRRP in detail.

The following example illustrates a basic VRRP configuration.

{{< img src = "/images/cumulus-linux/vrrp-example.png" >}}

### Configure VRRP

To configure VRRP, you need to specify the following information on each switch:

- **A virtual router ID (VRID) that identifies the group of VRRP routers**. You must specify the same ID across all virtual routers in the group.
- **One or more virtual IP addresses that are assigned to the virtual router group**. These are IP addresses that do not directly connect to a specific interface. Inbound packets sent to a virtual IP address are redirected to a physical network interface.

You can also set these optional parameters. If you do not set these parameters, the defaults are used:

| Optional Parameter | Default Value | Description|
| -----------| -------------| ------------- |
| `priority` | 100 | The priority level of the virtual router within the virtual router group, which determines the role that each virtual router plays and what happens if the master fails. Virtual routers have a priority between 1 and 254; the router with the highest priority becomes the master. |
| `advertisement interval` | 1000 milliseconds | The advertisement interval is the interval between successive advertisements by the master in a virtual router group. You can specify a value between 10 and 40950.|
| `preempt` | enabled | Preempt mode lets the router take over as master for a virtual router group if it has a higher priority than the current master. Preempt mode is enabled by default. To disable preempt mode, you need to edit the `/etc/frr/frr.conf` file and add the line `no vrrp <VRID> preempt` to the interface stanza, then restart FRR service.|

The NCLU commands write VRRP configuration to the `/etc/network/interfaces` file and the `/etc/frr/frr.conf` file.

The following example commands configure two switches (spine01 and spine02) that form one virtual router group (VRID 44) with IPv4 address 10.0.0.1/24 and IPv6 address 2001:0db8::1/64. *spine01* is the master; it has a priority of 254. *spine02* is the backup VRRP router.

<details>

<summary>NCLU Commands </summary>

**spine01**

```
cumulus@spine01:~$ net add interface swp1 vrrp 44 10.0.0.1/24
cumulus@spine01:~$ net add interface swp1 vrrp 44 2001:0db8::1/64
cumulus@spine01:~$ net add interface swp1 vrrp 44 priority 254
cumulus@spine01:~$ net add interface swp1 vrrp 44 advertisement-interval 5000
cumulus@spine01:~$ net pending
cumulus@spine01:~$ net commit
```

**spine02**

```
cumulus@spine02:~$ net add interface swp1 vrrp 44 10.0.0.1/24
cumulus@spine02:~$ net add interface swp1 vrrp 44 2001:0db8::1/64
cumulus@spine02:~$ net pending
cumulus@spine02:~$ net commit
```

</details>

<details>

<summary>Linux and vtysh Commands </summary>

1. Enable the `vrrpd` daemon, then start the FRRouting service. See [Configuring FRRouting](../../Layer-3/Configuring-FRRouting/).
2. From the vtysh shell, configure VRRP.

    **spine01**

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

    **spine02**

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

</details>

The NCLU and vtysh commands save the configuration in the `/etc/frr/frr.conf` file. For example:

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
Primary IP (v4)
Primary IP (v6)                      fe80::54df:e543:5c12:7762
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
