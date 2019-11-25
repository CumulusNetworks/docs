---
title: Multi-Chassis Link Aggregation - MLAG
author: Cumulus Networks
weight: 125
aliases:
 - /display/DOCS/Multi+Chassis+Link+Aggregation+++MLAG
 - /pages/viewpage.action?pageId=8366400
 - /display/DOCS/Multi+Chassis+Link+Aggregation+MLAG
 - /display/DOCS/Multi+Chassis+Link+Aggregation+-+MLAG
product: Cumulus Linux
version: '4.0'
---
Multi-Chassis Link Aggregation (MLAG) enables a server or switch with a two-port bond, such as a link aggregation group/LAG, EtherChannel, port group or trunk, to connect those ports to different switches and operate as if they are connected to a single, logical switch. This provides greater redundancy and greater system throughput.

{{%notice info%}}

**MLAG or CLAG**: The Cumulus Linux implementation of MLAG is referred to by other vendors as CLAG, MC-LAG or VPC. You will even see references to CLAG in CumulusLinux, including the management daemon, named `clagd`, and other options in the code, such as `clag-id`, which exist for historical purposes. The Cumulus Linux implementation is truly a multi-chassis link aggregation protocol, so we call it MLAG.

{{%/notice%}}

Dual-connected devices can create LACP bonds that contain links to each physical switch. Therefore, active-active links from the dual-connected devices are supported even though they are connected to two different physical switches.

A basic setup looks like this:

{{< img src = "/images/cumulus-linux/mlag-basic-setup.png" >}}

{{%notice tip%}}

You can see an example of how to set up this configuration by running:

```
cumulus@switch:~$ net example clag basic-clag
```

{{%/notice%}}

The two switches, S1 and S2, known as *peer switches*, appear as a single device to the bond on host H1. H1 distributes traffic between the two links to S1 and S2 in any way that you configure on the host. Similarly, traffic inbound to H1 can traverse S1 or S2 and arrive at H1.

## MLAG Requirements

MLAG has these requirements:

- There must be a direct connection between the two peer switches implementing MLAG (S1 and S2). This is typically a bond for increased reliability and bandwidth.
- There must be only two peer switches in one MLAG configuration, but you can have multiple configurations in a network for *switch-to-switch MLAG* (see below).
- You must specify a unique `clag-id` for every dual-connected bond on each peer switch; the value must be between 1 and 65535 and must be the same on both peer switches for the bond to be considered *dual-connected*.
- The dual-connected devices (servers or switches) can use LACP (IEEE 802.3ad/802.1ax) to form the [bond](../Bonding-Link-Aggregation/). In this case, the peer switches must also use LACP.

    {{%notice tip%}}

If you cannot use LACP, you can also use [balance-xor mode](../Bonding-Link-Aggregation/) to dual-connect host-facing bonds in an MLAG environment. You must still configure the same `clag-id` parameter on the MLAG bonds and it must be the same on both MLAG switches. Otherwise, the MLAG switch pair treats the bonds as if they are single-connected.

{{%/notice%}}

More elaborate configurations are also possible. The number of links between the host and the switches can be greater than two and does not have to be symmetrical:

{{< img src = "/images/cumulus-linux/mlag-multiple-links.png" >}}

Additionally, because S1 and S2 appear as a single switch to other bonding devices, you can also connect pairs of MLAG switches to each other in a switch-to-switch MLAG configuration:

{{< img src = "/images/cumulus-linux/mlag-two-pair.png" >}}

In the above example, L1 and L2 are also MLAG peer switches and present a two-port bond from a single logical system to S1 and S2. S1 and S2 do the same as far as L1 and L2 are concerned. For a switch-to-switch MLAG configuration, each switch pair must have a unique system MAC address. In the example, switch L1 and L2 each have the same system MAC address. Switch pair S1 and S2 each have the same system MAC address; however, it is a different system MAC address than the one used by the switch pair L1 and L2.

## LACP and Dual-Connectedness

For MLAG to operate correctly, the peer switches must know which links are *dual-connected* or are connected to the same host or switch. You must specify a `clag-id` for every dual-connected bond on each peer switch; the `clag-id` must be the same for the corresponding bonds on both peer switches. Typically, [Link Aggregation Control Protocol (LACP)](http://en.wikipedia.org/wiki/Link_Aggregation_Control_Protocol#Link_Aggregation_Control_Protocol), the IEEE standard protocol for managing bonds, is used for verifying dual-connectedness. LACP runs on the dual-connected device and on each of the peer switches. On the dual-connected device, the only configuration requirement is to create a bond that is managed by LACP.

However, if you cannot use LACP in your environment, you can configure the bonds in [balance-xor mode](../Bonding-Link-Aggregation). When using balance-xor mode to dual-connect host-facing bonds in an MLAG environment, you must configure the `clag-id` parameter on the MLAG bonds, which must be the same on both MLAG switches. Otherwise, the bonds are treated by the MLAG switch pair as if they are single-connected. Dual-connectedness is solely determined by matching `clag-id` and any misconnection is **not** detected.

On each of the peer switches, you must place the links that are connected to the dual-connected host or switch in the bond. This is true even if the links are a single port on each peer switch, where each port is placed into a bond, as shown below:

{{< img src = "/images/cumulus-linux/mlag-dual-connect.png" >}}

All of the dual-connected bonds on the peer switches have their system ID set to the MLAG system ID. Therefore, from the point of view of the hosts, each of the links in its bond is connected to the same system and so the host uses both links.

Each peer switch periodically makes a list of the LACP partner MAC addresses for all of their bonds and sends that list to its peer (using the `clagd` service; see below). The LACP partner MAC address is the MAC address of the system at the other end of a bond (hosts H1, H2, and H3 in the figure above). When a switch receives this list from its peer, it compares the list to the LACP partner MAC addresses on its switch. If any matches are found and the `clag-id` for those bonds match, then that bond is a dual-connected bond. You can find the LACP partner MAC address by the running `net show bridge macs` command or by examining the `/sys/class/net/<bondname>/bonding/ad_partner_mac sysfs` file for each bond.

## Configure MLAG

To configure MLAG, you need to:

- Create a bond that uses LACP on the dual-connected devices.
- Configure the interfaces, including bonds, VLANs, bridges, and peer links on each peer switch.

MLAG synchronizes the dynamic state between the two peer switches but it does not synchronize the switch configurations. After modifying the configuration of one peer switch, you must make the same changes to the configuration on the other peer switch. This applies to all configuration changes, including:

- Port configuration; for example, VLAN membership, [MTU](#mtu-in-an-mlag-configuration), and bonding parameters.
- Bridge configuration; for example, spanning tree parameters or bridge properties.
- Static address entries; for example, static FDB entries and static IGMP entries.
- QoS configuration; for example, ACL entries.

To verify VLAN membership configuration, run the NCLU `net show clag verify-vlans verbose` command or the Linux `clagctl -v verifyvlans` command. For example:

```
cumulus@switch:~$ net show clag verify-vlans verbose
Our Bond Interface   VlanId   Peer Bond Interface
------------------   ------   -------------------
server01                  1   server01
server01                 10   server01
server01                 20   server01
server01                 30   server01
server01                 40   server01
server01                 50   server01
uplink                    1   uplink
uplink                   10   uplink
uplink                   20   uplink
uplink                   30   uplink
uplink                   40   uplink
uplink                   50   uplink
uplink                  100   uplink
uplink                  101   uplink
uplink                  102   uplink
uplink                  103   uplink
uplink                  104   uplink
uplink                  105   uplink
...
```

### Reserved MAC Address Range

To prevent MAC address conflicts with other interfaces in the same bridged network, Cumulus Networks has [reserved a range of MAC addresses](https://support.cumulusnetworks.com/hc/en-us/articles/203837076) specifically to use with MLAG. This range of MAC addresses is 44:38:39:ff:00:00 to 44:38:39:ff:ff:ff.

Cumulus Networks recommends you use this range of MAC addresses when configuring MLAG.

{{%notice note%}}

- You *cannot* use the same MAC address for different MLAG pairs. Make sure you specify a different `clag sys-mac` setting for each MLAG pair in the network.
- If you configure MLAG with NCLU commands, Cumulus Linux does not check against a possible collision with VLANs outside the default reserved range when creating the peer link interfaces, in case the reserved VLAN range has been modified.

{{%/notice%}}

### Configure the Host or Switch

On your dual-connected device, create a bond that uses LACP. The method you use varies with the type of device you are configuring. The following image is a basic MLAG configuration, showing all the essential elements; a more detailed two-leaf/two-spine configuration is shown [below](#example-mlag-configuration).

{{< img src = "/images/cumulus-linux/mlag_config-host-switch.png" >}}

### Configure the Interfaces

Place every interface that connects to the MLAG pair from a dual-connected device into a [bond](../Bonding-Link-Aggregation/), even if the bond contains only a single link on a single physical switch (even though the MLAG pair contains two or more links). Layer 2 data travels over this bond. In the examples throughout this chapter, *peerlink* is the name of the bond.

Single-attached hosts, also known as *orphan ports*, can be just a member of the bridge.

Additionally, configure the fast mode of LACP on the bond to allow more timely updates of the LACP state. These bonds are then placed in a bridge, which must include the peer link between the switches.

To enable communication between the `clagd` services on the peer switches, do the following:

- Choose an unused VLAN (also known as a *switched virtual interface* or *SVI* here).
- Assign the SVI an unrouteable link-local address to give the peer switches layer 3 connectivity between each other.
- Configure the VLAN as a [VLAN subinterface](../../Layer-1-and-Switch-Ports/Interface-Configuration-and-Management/) on the peer link bond instead of the VLAN-aware bridge, called *peerlink*. If you configure the subinterface with [NCLU](../../System-Configuration/Network-Command-Line-Utility-NCLU/), the VLAN subinterface is named 4094 by default (the subinterface named *peerlink.4094* below). If you are configuring the peer link  without NCLU, Cumulus Networks still recommends you use 4094 for the peer link VLAN if possible. This ensures that the VLAN is completely independent of the bridge and spanning tree forwarding decisions.
- Include untagged traffic on the peer link, as this avoids issues with STP.
- Specify a backup interface, which is any layer 3 backup interface for your peer links in case the peer link goes down. While a backup interface is optional, Cumulus Networks recommends you configure one. More information about configuring the [backup link](#specify-a-backup-link) and understanding various [redundancy scenarios](#failover-redundancy-scenarios) is available below.

For example, if *peerlink* is the inter-chassis bond, and VLAN 4094 is the peer link VLAN, configure *peerlink.4094* as follows:

<details>

<summary>NCLU Commands </summary>

```
cumulus@switch:~$ net add clag peer sys-mac 44:38:39:FF:40:94 interface swp49-50 linklocal backup-ip 192.0.2.50
cumulus@switch:~$ net pending
cumulus@switch:~$ net commit
```

{{%notice note%}}

Do *not* add VLAN 4094 to the bridge VLAN list; VLAN 4094 for the peer link subinterface cannot also be configured as a bridged VLAN with bridge VIDs under the bridge.

{{%/notice%}}

To enable MLAG, you must add *peerlink* to a traditional or VLAN-aware bridge. The commands below add *peerlink* to a VLAN-aware bridge:

```
cumulus@switch:~$ net add bridge bridge ports peerlink
cumulus@switch:~$ net pending
cumulus@switch:~$ net commit
```

</details>

<details>

<summary>Linux Commands </summary>

Edit the `/etc/network/interfaces` file to add the peer link.

```
cumulus@switch:~$ sudo nano /etc/network/interfaces
...
auto peerlink
iface peerlink
    bond-slaves swp49 swp50

auto peerlink.4094
iface peerlink.4094
    clagd-backup-ip 192.0.2.50
    clagd-peer-ip linklocal
    clagd-sys-mac 44:38:39:FF:40:94
...
```

To enable MLAG, you must add *peerlink* to a traditional or VLAN-aware bridge. The configuration below adds *peerlink* to a VLAN-aware bridge:

```
cumulus@switch:~$ sudo nano /etc/network/interfaces
...
auto bridge
iface bridge
    bridge-ports peerlink
    bridge-vlan-aware yes
...
```

Run the `ifreload -a` command to reload the configuration:

```
cumulus@switch:~$ sudo ifreload -a
```

</details>

{{%notice note%}}

When you change the MLAG configuration in the `interfaces` file, thechanges take effect when you bring the peer link interface up with `ifup` or `ifreload -a`. Do **not** use `systemctl restart clagd.service` to apply the new configuration.

{{%/notice%}}

{{%notice warning%}}

Do not use 169.254.0.1 as the MLAG peer link IP address; Cumulus Linux uses this address exclusively for [BGP unnumbered](../../Layer-3/Border-Gateway-Protocol-BGP/) interfaces.

{{%/notice%}}

### Switch Roles and Priority Setting

Each MLAG-enabled switch in the pair has a *role*. When the peering relationship is established between the two switches, one switch is put into the *primary* role, and the other into the *secondary* role. When an MLAG-enabled switch is in the secondary role, it does not send STP BPDUs on dual-connected links; it only sends BPDUs on single-connected links. The switch in the primary role sends STP BPDUs on all single- and dual-connected links.

| Sends BPDUs Via        | Primary | Secondary |
| ---------------------- | ------- | --------- |
| Single-connected links | Yes     | Yes       |
| Dual-connected links   | Yes     | No        |

By default, the role is determined by comparing the MAC addresses of the two sides of the peering link; the switch with the lower MAC address assumes the primary role. You can override this by setting the `clagd-priority` option for the peer link:

<details>

<summary>NCLU Commands </summary>

The following command example sets the `clagd-priority` option for the peer link.

```
cumulus@switch:~$ net add interface peerlink.4094 clag priority 2048
cumulus@switch:~$ net pending
cumulus@switch:~$ net commit
```

</details>

<details>

<summary>Linux Commands </summary>

Edit the `/etc/network/interfaces` file and add the `clagd-priority` option. The following example sets the `clagd-priority` option for the peer link:

```
cumulus@switch:~$ sudo nano /etc/network/interfaces
...
auto peerlink.4094
iface peerlink.4094
    clagd-peer-ip linklocal
    clagd-backup-ip 192.0.2.50
    clagd-sys-mac 44:38:39:FF:40:94
    clagd-priority 2048
...
```

Run the `ifreload -a` command to reload the configuration:

```
cumulus@switch:~$ sudo ifreload -a
```

</details>

The switch with the lower priority value is given the primary role; the default value is 32768 and the range is 0 to 65535. Read the `clagd(8)` and `clagctl(8)` man pages for more information.

When the `clagd` service exits during switch reboot or if you stop the service on the primary switch, the peer switch that is in the secondary role becomes the primary.

However, if the primary switch goes down without stopping the `clagd` service for any reason, or if the peer link goes down, the secondary switch does **not** change its role. In case the peer switch is determined to be not alive, the switch in the secondary role rolls back the LACP system ID to be the bond interface MAC address instead of the `clagd-sys-mac` and the switch in primary role uses the `clagd-sys-mac` as the LACP system ID on the bonds.

## Example MLAG Configuration

The example configuration below configures two bonds for MLAG, each with a single port, a peer link that is a bond with two member ports, and three VLANs on each port.

{{%notice tip%}}

You can see a more traditional layer 2 example configuration in NCLU; run `net example clag l2-with-server-vlan-trunks`. For a very basic configuration with just one pair of switches and a single host, run `net example clag l2-with-server-vlan-trunks`.

{{%/notice%}}

{{< img src = "/images/cumulus-linux/mlag-config-example.png" >}}

You configure these interfaces using [NCLU](../../System-Configuration/Network-Command-Line-Utility-NCLU/), so the bridges are in [VLAN-aware mode](../Ethernet-Bridging-VLANs/VLAN-aware-Bridge-Mode/). The bridges use these Cumulus Linux-specific keywords:

- `bridge-vids` defines the allowed list of tagged 802.1q VLAN IDs for all bridge member interfaces. You can specify non-contiguous ranges with a space-separated list; for example, `bridge-vids 100-200 300 400-500`.
- `bridge-pvid` defines the untagged VLAN ID for each port. This is commonly referred to as the *native VLAN*.

The bridge configurations below indicate that each bond carries tagged frames on VLANs 10, 20, 30, 40, 50, and 100 to 200 (as specified by `bridge-vids`), but untagged frames on VLAN 1 (as specified by `bridge-pvid`). Also, take note on how you configure the VLAN subinterfaces used for `clagd` communication (*peerlink.4094* in the sample configuration below). Finally, the host configurations for server01 through server04 are not shown here. The configurations for each corresponding node are almost identical, except for the IP addresses used for managing the `clagd` service.

{{%notice note%}}

Make sure that the VLAN subinterface is not in your layer 2 domain and does not have a very high VLAN ID (up to 4094). Read more about the [range of VLAN IDs you can use](../Ethernet-Bridging-VLANs/VLAN-aware-Bridge-Mode).

{{%/notice%}}

The commands to create the configurations for both spines look like the following. Note that the `clag-id` and `clagd-sys-mac` must be the same for the corresponding bonds on spine01 and spine02:

<details>

<summary>**spine01** </summary>

```
cumulus@spine01:~$ net show configuration commands
net add interface swp1-4
net add loopback lo ip address 10.0.0.21/32
net add interface eth0 ip address dhcp
```

These commands create the following configuration in the `/etc/network/interfaces` file:

```
cumulus@spine01:~$ cat /etc/network/interfaces
auto lo
iface lo inet loopback
    address 10.0.0.21/32

auto eth0
iface eth0 inet dhcp

# downlinks
auto swp1
iface swp1

auto swp2
iface swp2

auto swp3
iface swp3

auto swp4
iface swp4
```

</details>

<details>

<summary>**spine02** </summary>

```
cumulus@spine02:~$ net show configuration commands
net add interface swp1-4
net add loopback lo ip address 10.0.0.22/32
net add interface eth0 ip address dhcp
```

These commands create the following configuration in the `/etc/network/interfaces` file:

```
cumulus@spine02:~$ cat /etc/network/interfaces
auto lo
iface lo inet loopback
    address 10.0.0.22/32

auto eth0
iface eth0 inet dhcp

# downlinks
auto swp1
iface swp1

auto swp2
iface swp2

auto swp3
iface swp3

auto swp4
iface swp4
```

</details>

Here is an example configuration for the switches leaf01 through leaf04. Note that the `clag-id` and `clagd-sys-mac` must be the same for the corresponding bonds on leaf01 and leaf02 as well as leaf03 and leaf04:

<details>

<summary>**leaf01** </summary>

```
cumulus@leaf01:~$ net show configuration commands
net add loopback lo ip address 10.0.0.11/32
net add bgp autonomous-system 65011
net add bgp router-id 10.0.0.11
net add bgp ipv4 unicast network 10.0.0.11/32
net add routing prefix-list ipv4 dc-leaf-in seq 10 permit 0.0.0.0/0
net add routing prefix-list ipv4 dc-leaf-in seq 20 permit 10.0.0.0/24 le 32
net add routing prefix-list ipv4 dc-leaf-in seq 30 permit 172.16.2.0/24
net add routing prefix-list ipv4 dc-leaf-out seq 10 permit 172.16.1.0/24
net add bgp neighbor fabric peer-group
net add bgp neighbor fabric remote-as external
net add bgp ipv4 unicast neighbor fabric prefix-list dc-leaf-in in
net add bgp ipv4 unicast neighbor fabric prefix-list dc-leaf-out out
net add bgp neighbor swp51-52 interface peer-group fabric
net add vlan 100 ip address 172.16.1.1/24
net add bgp ipv4 unicast network 172.16.1.1/24
net add clag peer sys-mac 44:38:39:FF:00:01 interface swp49-50 primary backup-ip 192.168.1.12
net add clag port bond server1 interface swp1 clag-id 1
net add clag port bond server2 interface swp2 clag-id 2
net add bond server1-2 bridge access 100
net add bond server1-2 stp portadminedge
net add bond server1-2 stp bpduguard
```

These commands create the following configuration in the `/etc/network/interfaces` file:

```
cumulus@leaf01:~$ cat /etc/network/interfaces
auto lo
iface lo inet loopback
    address 10.0.0.11/32

auto eth0
iface eth0 inet dhcp

auto swp1
iface swp1

auto swp2
iface swp2

# peerlink
auto swp49
iface swp49
    post-up ip link set $IFACE promisc on     # Only required on VX

auto swp50
iface swp50
    post-up ip link set $IFACE promisc on     # Only required on VX

# uplinks
auto swp51
iface swp51

auto swp52
iface swp52

# bridge to hosts
auto bridge
iface bridge
    bridge-ports peerlink server1 server2
    bridge-vids 100
    bridge-vlan-aware yes

auto peerlink
iface peerlink
    bond-slaves swp49 swp50

auto peerlink.4094
iface peerlink.4094
    clagd-backup-ip 192.168.1.12
    clagd-peer-ip linklocal
    clagd-priority 1000
    clagd-sys-mac 44:38:39:FF:00:01

auto server1
iface server1
    bond-slaves swp1
    bridge-access 100
    clag-id 1
    mstpctl-bpduguard yes
    mstpctl-portadminedge yes

auto server2
iface server2
    bond-slaves swp2
    bridge-access 100
    clag-id 2
    mstpctl-bpduguard yes
    mstpctl-portadminedge yes

auto vlan100
iface vlan100
    address 172.16.1.1/24
    vlan-id 100
    vlan-raw-device bridge
```

</details>

<details>

<summary>**leaf02** </summary>

```
cumulus@leaf02:~$ net show conf commands
net add loopback lo ip address 10.0.0.12/32
net add bgp autonomous-system 65012
net add bgp router-id 10.0.0.12
net add bgp ipv4 unicast network 10.0.0.12/32
net add routing prefix-list ipv4 dc-leaf-in seq 10 permit 0.0.0.0/0
net add routing prefix-list ipv4 dc-leaf-in seq 20 permit 10.0.0.0/24 le 32
net add routing prefix-list ipv4 dc-leaf-in seq 30 permit 172.16.2.0/24
net add routing prefix-list ipv4 dc-leaf-out seq 10 permit 172.16.1.0/24
net add bgp neighbor fabric peer-group
net add bgp neighbor fabric remote-as external
net add bgp ipv4 unicast neighbor fabric prefix-list dc-leaf-in in
net add bgp ipv4 unicast neighbor fabric prefix-list dc-leaf-out out
net add bgp neighbor swp51-52 interface peer-group fabric
net add vlan 100 ip address 172.16.1.2/24
net add bgp ipv4 unicast network 172.16.1.2/24
net add clag peer sys-mac 44:38:39:FF:00:01 interface swp49-50 secondary backup-ip 192.168.1.11
net add clag port bond server1 interface swp1 clag-id 1
net add clag port bond server2 interface swp2 clag-id 2
net add bond server1-2 bridge access 100
net add bond server1-2 stp portadminedge
net add bond server1-2 stp bpduguard
```

These commands create the following configuration in the `/etc/network/interfaces` file:

```
cumulus@leaf02:~$ cat /etc/network/interfaces
auto lo
iface lo inet loopback
    address 10.0.0.12/32

auto eth0
iface eth0 inet dhcp

auto swp1
iface swp1

auto swp2
iface swp2

# peerlink
auto swp49
iface swp49
    post-up ip link set $IFACE promisc on     # Only required on VX

auto swp50
iface swp50
    post-up ip link set $IFACE promisc on     # Only required on VX

# uplinks
auto swp51
iface swp51

auto swp52
iface swp52

# bridge to hosts
auto bridge
iface bridge
    bridge-ports peerlink server1 server2
    bridge-vids 100
    bridge-vlan-aware yes

auto peerlink
iface peerlink
    bond-slaves swp49 swp50

auto peerlink.4094
iface peerlink.4094
    clagd-backup-ip 192.168.1.11
    clagd-peer-ip linklocal
    clagd-sys-mac 44:38:39:FF:00:01

auto server1
iface server1
    bond-slaves swp1
    bridge-access 100
    clag-id 1
    mstpctl-bpduguard yes
    mstpctl-portadminedge yes

auto server2
iface server2
    bond-slaves swp2
    bridge-access 100
    clag-id 2
    mstpctl-bpduguard yes
    mstpctl-portadminedge yes
 
auto vlan100
iface vlan100
    address 172.16.1.2/24
    vlan-id 100
    vlan-raw-device bridge
```

</details>

<details>

<summary>**leaf03**</summary>

```
cumulus@leaf03:~$ net show conf commands
net add loopback lo ip address 10.0.0.13/32
net add bgp autonomous-system 65013
net add bgp router-id 10.0.0.13
net add bgp ipv4 unicast network 10.0.0.13/32
net add routing prefix-list ipv4 dc-leaf-in seq 10 permit 0.0.0.0/0
net add routing prefix-list ipv4 dc-leaf-in seq 20 permit 10.0.0.0/24 le 32
net add routing prefix-list ipv4 dc-leaf-in seq 30 permit 172.16.2.0/24
net add routing prefix-list ipv4 dc-leaf-out seq 10 permit 172.16.1.0/24
net add bgp neighbor fabric peer-group
net add bgp neighbor fabric remote-as external
net add bgp ipv4 unicast neighbor fabric prefix-list dc-leaf-in in
net add bgp ipv4 unicast neighbor fabric prefix-list dc-leaf-out out
net add bgp neighbor swp51-52 interface peer-group fabric
net add vlan 100 ip address 172.16.1.3/24
net add bgp ipv4 unicast network 172.16.1.3/24
net add clag peer sys-mac 44:38:39:FF:00:02 interface swp49-50 primary backup-ip 192.168.1.14
net add clag port bond server3 interface swp1 clag-id 3
net add clag port bond server4 interface swp2 clag-id 4
net add bond server3-4 bridge access 100
net add bond server3-4 stp portadminedge
net add bond server3-4 stp bpduguard
```

These commands create the following configuration in the `/etc/network/interfaces` file:

```
cumulus@leaf03:~$ cat /etc/network/interfaces
auto lo
iface lo inet loopback
    address 10.0.0.13/32

auto eth0
iface eth0 inet dhcp

auto swp1
iface swp1

auto swp2
iface swp2

# peerlink
auto swp49
iface swp49
    post-up ip link set $IFACE promisc on     # Only required on VX

auto swp50
iface swp50
    post-up ip link set $IFACE promisc on     # Only required on VX

# uplinks
auto swp51
iface swp51

auto swp52
iface swp52

# bridge to hosts
auto bridge
iface bridge
    bridge-ports peerlink server3 server4
    bridge-vids 100
    bridge-vlan-aware yes

auto peerlink
iface peerlink
    bond-slaves swp49 swp50

auto peerlink.4094
iface peerlink.4094
    clagd-backup-ip 192.168.1.14
    clagd-peer-ip linklocal
    clagd-priority 1000
    clagd-sys-mac 44:38:39:FF:00:02

auto server3
iface server3
    bond-slaves swp1
    bridge-access 100
    clag-id 3
    mstpctl-bpduguard yes
    mstpctl-portadminedge yes

auto server4
iface server4
    bond-slaves swp2
    bridge-access 100
    clag-id 4
    mstpctl-bpduguard yes
    mstpctl-portadminedge yes

auto vlan100
iface vlan100
    address 172.16.1.3/24
    vlan-id 100
    vlan-raw-device bridge
```

</details>

<details>

<summary>**leaf04** </summary>

```
cumulus@leaf04:~$ net show configuration commands
net add loopback lo ip address 10.0.0.14/32
net add bgp autonomous-system 65014
net add bgp router-id 10.0.0.14
net add bgp ipv4 unicast network 10.0.0.14/32
net add routing prefix-list ipv4 dc-leaf-in seq 10 permit 0.0.0.0/0
net add routing prefix-list ipv4 dc-leaf-in seq 20 permit 10.0.0.0/24 le 32
net add routing prefix-list ipv4 dc-leaf-in seq 30 permit 172.16.2.0/24
net add routing prefix-list ipv4 dc-leaf-out seq 10 permit 172.16.1.0/24
net add bgp neighbor fabric peer-group
net add bgp neighbor fabric remote-as external
net add bgp ipv4 unicast neighbor fabric prefix-list dc-leaf-in in
net add bgp ipv4 unicast neighbor fabric prefix-list dc-leaf-out out
net add bgp neighbor swp51-52 interface peer-group fabric
net add vlan 100 ip address 172.16.1.4/24
net add bgp ipv4 unicast network 172.16.1.4/24
net add clag peer sys-mac 44:38:39:FF:00:02 interface swp49-50 secondary backup-ip 192.168.1.13
net add clag port bond server3 interface swp1 clag-id 3
net add clag port bond server4 interface swp2 clag-id 4
net add bond server3-4 bridge access 100
net add bond server3-4 stp portadminedge
net add bond server3-4 stp bpduguard
```

These commands create the following configuration in the `/etc/network/interfaces` file:

```
cumulus@leaf04:~$ cat /etc/network/interfaces
auto lo
iface lo inet loopback
    address 10.0.0.14/32

auto eth0
iface eth0 inet dhcp

auto swp1
iface swp1

auto swp2
iface swp2

# peerlink
auto swp49
iface swp49
    post-up ip link set $IFACE promisc on     # Only required on VX

auto swp50
iface swp50
    post-up ip link set $IFACE promisc on     # Only required on VX

# uplinks
auto swp51
iface swp51

auto swp52
iface swp52

# bridge to hosts
auto bridge
iface bridge
    bridge-ports peerlink server3 server4
    bridge-vids 100
    bridge-vlan-aware yes

auto peerlink
iface peerlink
    bond-slaves swp49 swp50

auto peerlink.4094
iface peerlink.4094
    clagd-backup-ip 192.168.1.13
    clagd-peer-ip linklocal
    clagd-sys-mac 44:38:39:FF:00:02

auto server3
iface server3
    bond-slaves swp1
    bridge-access 100
    clag-id 3
    mstpctl-bpduguard yes
    mstpctl-portadminedge yes

auto server4
iface server4
    bond-slaves swp2
    bridge-access 100
    clag-id 4
    mstpctl-bpduguard yes
    mstpctl-portadminedge yes

auto vlan100
iface vlan100
    address 172.16.1.4/24
    vlan-id 100
    vlan-raw-device bridge
```

</details>

## Disable clagd on an Interface

In the configurations above, the `clagd-peer-ip` and `clagd-sys-mac` parameters are mandatory, while the rest are optional. When mandatory `clagd` commands are present under a peer link subinterface, the `clagd-enable` option is not present but is enabled by default. To disable `clagd` on the subinterface, set `clagd-enable` to *no*:

<details>

<summary>NCLU Commands </summary>

```
cumulus@switch:~$ net add interface peerlink.4094 clag enable no
cumulus@switch:~$ net pending
cumulus@switch:~$ net commit
```

</details>

<details>

<summary>Linux Commands </summary>

Edit the `/etc/network/interfaces` file and add `clagd-enable no` to the interface stanza:

```
cumulus@switch:~$ sudo nano /etc/network/interfaces 
...
auto peerlink.4094
iface peerlink.4094
    clagd-backup-ip 192.168.1.12
    clagd-enable no
    clagd-peer-ip linklocal
    clagd-priority 1000
    clagd-sys-mac 44:38:39:FF:00:01
...
```

Run the `ifreload` -a command to reload the configuration.

```
cumulus@switch:~$ sudo ifreload -a
```

</details>

Use `clagd-priority` to set the role of the MLAG peer switch to primary or secondary. Each peer switch in an MLAG pair must have the same `clagd-sys-mac` setting. Each `clagd-sys-mac` setting must be unique to each MLAG pair in the network. For more details, refer to `man clagd`.

## Check the MLAG Configuration Status

To check the status of your MLAG configuration, run the NCLU `net show clag` command or the Linux `clagctl` command. For example:

``` 
cumulus@switch:~$ net show clag 
The peer is alive
    Peer Priority, ID, and Role: 4096 44:38:39:FF:00:01 primary
     Our Priority, ID, and Role: 8192 44:38:39:FF:00:02 secondary
          Peer Interface and IP: peerlink.4094 linklocal
                      Backup IP: 192.168.1.12 (inactive)
                     System MAC: 44:38:39:FF:00:01

CLAG Interfaces
Our Interface      Peer Interface     CLAG Id   Conflicts              Proto-Down Reason
----------------   ----------------   -------   --------------------   -----------------
         server1   server1            1         -                      -
         server2   server2            2         -                      -
```

## Configure MLAG with a Bridge in Traditional Mode

To configure MLAG with a traditional mode bridge instead of [VLAN-aware mode](../Ethernet-Bridging-VLANs/VLAN-aware-Bridge-Mode/), the peer link and all dual-connected links must be configured as [untagged/native](../Ethernet-Bridging-VLANs/Traditional-Bridge-Mode/) ports on a bridge (note the absence of any VLANs in the bridge-ports line and the lack of the bridge-vlan-aware parameter below):

```
...
auto br0
iface br0
    bridge-ports peerlink spine1-2 host1 host2
...
```

The following example shows you how to allow VLAN 100 across the peer link:

```
...
auto br0.100
iface br0.100
    bridge-ports peerlink.100 bond1.100
    bridge-stp on
...
```

For a deeper comparison of traditional versus VLAN-aware bridge modes, read this [knowledge base article](https://support.cumulusnetworks.com/hc/en-us/articles/204909397).

## Peer Link Interfaces and the protodown State

In addition to the standard UP and DOWN administrative states, an interface that is a member of an MLAG bond can also be in a `protodown` state. When MLAG detects a problem that might result in connectivity issues, it can put that interface into `protodown` state. Such connectivity issues include:

- When the peer link goes down but the peer switch is up (the backup link is active).
- When the bond is configured with an MLAG ID, but the `clagd` service is not running (whether it was deliberately stopped or simply dies).
- When an MLAG-enabled node is booted or rebooted, the MLAG bonds are placed in a `protodown` state until the node establishes a connection to its peer switch, or five minutes have elapsed.

When an interface goes into a `protodown` state, it results in a local OPER DOWN (carrier down) on the interface.

To show an interface in `protodown` state, run the NCLU `net show bridge link` command or the Linux `ip link show` command. For example:

```
cumulus@switch:~$ net show bridge link
3: swp1 state DOWN: <NO-CARRIER,BROADCAST,MULTICAST,MASTER,UP> mtu 9216 master pfifo_fast master host-bond1 state DOWN mode DEFAULT qlen 500 protodown on
    link/ether 44:38:39:00:69:84 brd ff:ff:ff:ff:ff:ff
```

### Specify a Backup Link

You can specify a backup link for your peer links in case the peer link goes down. When this happens, the `clagd` service uses the backup link to check the health of the peer switch.

The backup IP address **must** be different than the peer link IP address (`clagd-peer-ip`). It must be reachable by a route that does not use the peer link and it must be in the same network namespace as the peer link IP address.

Cumulus Networks recommends you use the switch's loopback or management IP address for this purpose. Which one should you choose?

- If your MLAG configuration has **routed uplinks** (a modern approach to the data center fabric network), then configure `clagd` to use the peer switch **loopback** address for the health check. When the peer link is down, the secondary switch must route towards the loopback address using uplinks (towards spine layer). If the primary switch is also suffering a more significant problem (for example, `switchd` is unresponsive /or stopped), then the secondary switch eventually promotes itself to primary and traffic now flows normally.

    To ensure IP connectivity between the loopbacks, you must carefully
    consider what implications this has on the BGP ASN configured:

    - The two MLAG member switches must use unique BGP ASNs, **or**,
    - If the two MLAG member switches use the same BGP ASN, then you must bypass the BGP loop prevention check on AS\_PATH attribute.

- If your MLAG configuration has **bridged uplinks** (such as a campus network or a large, flat layer 2 network), then configure `clagd` to use the peer switch **eth0** address for the health check. When the peer link is down, the secondary switch must route towards the eth0 address using the OOB network (provided you have implemented an OOB network).

To configure a backup link:

<details>

<summary>NCLU Commands </summary>

```
cumulus@switch:~$ net add interface peerlink.4094 clag backup-ip 192.0.2.50
cumulus@switch:~$ net pending
cumulus@switch:~$ net commit
```

You can also specify the backup UDP port. The port defaults to 5342, but you can configure it with the `clagd args` `--backupPort <PORT>` option. For example:

```
cumulus@switch:~$ net add interface peerlink.4094 clag args --backupPort 5400
cumulus@switch:~$ net pending
cumulus@switch:~$ net commit
```

</details>

<details>

<summary>Linux Commands </summary>

Edit the `/etc/network/interfaces` file and add `clag-backup-ip <ip-address>` to the peer link configuration. For example:

```
cumulus@switch:~$ sudo nano /etc/network/interfaces
...
auto peerlink.4094
iface peerlink.4094
    netmask 255.255.255.0
    clagd-priority 8192
    clagd-peer-ip linklocal
    clagd-backup-ip 192.0.2.50
    clagd-sys-mac 44:38:39:ff:00:01
    clagd-args --priority 1000
...
```

You can also specify the backup UDP port. The port defaults to 5342, but you can change the port with `clagd-args` `--backupPort <port>` . For example:

```
cumulus@switch:~$ sudo nano /etc/network/interfaces
...
auto peerlink.4094
iface peerlink.4094
    netmask 255.255.255.0
    clagd-priority 8192
    clagd-peer-ip linklocal
    clagd-backup-ip 192.0.2.50
    clagd-args --backupPort 5400
    clagd-sys-mac 44:38:39:ff:00:01
    clagd-args --priority 1000
...
```

Run `ifreload -a` to reload the configuration:

```
cumulus@switch:~$ sudo ifreload -a
```

</details>

To show the backup IP address, run the NCLU `net show clag` command or the Linux `clagctl` command. For example:

```
cumulus@switch:~$ net show clag 
The peer is alive
        Our Priority, ID, and Role: 32768 44:38:39:00:00:41 primary
    Peer Priority, ID, and Role: 32768 44:38:39:00:00:42 secondary
            Peer Interface and IP: peerlink.4094 linklocal
                        Backup IP: 192.168.0.22 (active)
                        System MAC: 44:38:39:FF:40:90

CLAG Interfaces
Our Interface      Peer Interface     CLAG Id   Conflicts              Proto-Down Reason
----------------   ----------------   -------   --------------------   -----------------
        leaf03-04   leaf03-04          1034      -                      -
        exit01-02   -                  2930      -                      -
        leaf01-02   leaf01-02          1012      -                      -
```

### Specify a Backup Link to a VRF

You can configure the backup link to a [VRF](../../Layer-3/Virtual-Routing-and-Forwarding-VRF/) or [management VRF](../../Layer-3/Management-VRF/). Include the name of the VRF or management VRF with the `clagd-backup-ip` command.

{{%notice note%}}

You cannot use the VRF on a peer link subinterface.

{{%/notice%}}

<details>

<summary>NCLU Commands </summary>

```
cumulus@switch:~$ net add interface peerlink.4094 clag backup-ip 192.168.0.22 vrf green
cumulus@switch:~$ net pending
cumulus@switch:~$ net commit
```

</details>

<details>

<summary>Linux Commands </summary>

Edit the `/etc/network/interfaces` file to include the name of the VRF or management VRF with the `clag-backup-ip` option. The following configuration links to the management VRF.

```
cumulus@switch:~$ sudo nano /etc/network/interfaces
...
auto eth0
iface eth0 inet dhcp
        vrf mgmt

auto mgmt
iface mgmt
        vrf-table auto

auto peer-bond.4000
iface peer-bond.4000
        clagd-priority 8192
        clagd-peer-ip linklocal
        clagd-backup-ip 192.0.2.174 vrf mgmt
        clagd-sys-mac 44:38:39:ff:00:01
...
```

R un `ifreload -a` to reload the configuration :

```
cumulus@switch:~$ sudo ifreload -a
```

</details>

To verify the backup link, run the NCLU `net show clag` command or the Linux `clagctl` command. For example:

```
cumulus@switch:~$ net show clag 
The peer is alive
        Our Priority, ID, and Role: 32768 44:38:39:00:00:41 primary
    Peer Priority, ID, and Role: 32768 44:38:39:00:00:42 secondary
            Peer Interface and IP: peerlink.4094 linklocal
                        Backup IP: 192.168.0.22 vrf green (active)
                        System MAC: 44:38:39:FF:40:90

CLAG Interfaces
Our Interface      Peer Interface     CLAG Id   Conflicts              Proto-Down Reason
----------------   ----------------   -------   --------------------   -----------------
        leaf03-04   leaf03-04          1034      -                      -
        exit01-02   -                  2930      -                      -
        leaf01-02   leaf01-02          1012      -                      -
```

## Monitor Dual-Connected Peers

When the switch receives a valid message from its peer, it knows that `clagd` is alive and executing on that peer. This causes `clagd` to change the system ID of each bond that is assigned a `clag-id` from the default value (the MAC address of the bond) to the system ID assigned to both peer switches. This makes the hosts connected to each switch act as if they are connected to the same system so that they use all ports within their bond. Additionally, `clagd` determines which bonds are dual-connected and modifies the forwarding and learning behavior to accommodate these dual-connected bonds.

If the peer does not receive any messages for three update intervals, that peer switch is assumed to no longer be acting as an MLAG peer. In this case, the switch reverts all configuration changes so that it operates as a standard non-MLAG switch. This includes removing all statically assigned MAC addresses, clearing the egress forwarding mask, and allowing addresses to move from any port to the peer port. After a message is again received from the peer, MLAG operation starts again as described earlier. You can configure a custom timeout setting by adding `--peerTimeout <value>` to `clagd-args`:

<details>

<summary>NCLU Commands </summary>

The following example commands set the timeout to 900:

```
cumulus@switch:~$ net add interface peerlink.4094 clag args --peerTimeout 900
cumulus@switch:~$ net pending
cumulus@switch:~$ net commit
```

</details>

<details>

<summary>Linux Commands </summary>

Edit the `/etc/network/interfaces` file and add the timeout to the *peerlink* stanza. The following example sets the timeout to 900:

```
cumulus@switch:~$ sudo nano /etc/network/interfaces
...
auto peerlink.4094
iface peerlink.4094
    clagd-args --backupPort 5400
    clagd-args --peerTimeout 900
    clagd-peer-ip linklocal
    clagd-backup-ip 192.0.2.50
    clagd-priority 8192
    clagd-sys-mac 44:38:39:ff:00:01
...
```

Run `ifreload -a` to reload the configuration:

```
cumulus@switch:~$ sudo ifreload -a
```

</details>

After bonds are identified as dual-connected, `clagd` sends more information to the peer switch for those bonds. The MAC addresses (and VLANs) that are dynamically learned on those ports are sent along with the LACP partner MAC address for each bond. When a switch receives MAC address information from its peer, it adds MAC address entries on the corresponding ports. As the switch learns and ages out MAC addresses, it informs the peer switch of these changes to its MAC address table so that the peer can keep its table synchronized. Periodically, at 45% of the bridge ageing time, a switch sends its entire MAC address table to the peer, so that peer switch can verify that its MAC address table is properly synchronized.

The switch sends an update frequency value in the messages to its peer, which tells `clagd` how often the peer will send these messages. You can configure a different frequency by adding `--lacpPoll <seconds>` to `clagd-args`:

<details>

<summary>NCLU Commands </summary>

The following example command sets the frequency to 900 seconds:

```
cumulus@switch:~$ net add interface peerlink.4094 clag args --lacpPoll 900
cumulus@switch:~$ net pending
cumulus@switch:~$ net commit
```

</details>

<details>

<summary>Linux Commands </summary>

Edit the `/etc/network/interfaces` file. The following example sets the frequency to 900 seconds:

```
cumulus@switch:~$ sudo nano /etc/network/interfaces
...
auto peerlink.4094
 iface peerlink.4094
    clagd-args --backupPort 5400
    clagd-args --lacpPoll 900
    clagd-peer-ip linklocal
    clagd-backup-ip 192.0.2.50
    clagd-priority 8192
    clagd-sys-mac 44:38:39:ff:00:01
...
```

Run `ifreload -a` to reload the configuration:

```
cumulus@switch:~$ sudo ifreload -a
```

</details>

## Configure Layer 3 Routed Uplinks

In this scenario, the spine switches connect at layer 3, as shown in the image below. Alternatively, the spine switches can be singly connected to each core switch at layer 3 (not shown below).

{{< img src = "/images/cumulus-linux/mlag-layer3-routed.png" >}}

In this design, the spine switches route traffic between the server hosts in the layer 2 domains and the core. The servers (host1 thru host4) each have a layer 2 connection up to the spine layer where the default gateway for the host subnets resides. However, since the spine switches as gateway devices communicate at layer 3, you need to configure a protocol such as [VRR](../Virtual-Router-Redundancy-VRR-and-VRRP/) (virtual router redundancy) between the spine switch pair to support active/active forwarding.

Then, to connect the spine switches to the core switches, you need to determine whether the routing is static or dynamic. If it is dynamic, you must choose which protocol to use ([OSPF](../../Layer-3/Open-Shortest-Path-First-OSPF/) or [BGP](../../Layer-3/Border-Gateway-Protocol-BGP/)). When enabling a routing protocol in an MLAG environment, it is also necessary to manage the uplinks, because by default MLAG is not aware of layer 3 uplink interfaces. If there is a peer link failure, MLAG does not remove static routes or bring down a BGP or OSPF adjacency unless you use a separate link state daemon such as `ifplugd`.

### MLAG and Peer Link Peering

When using MLAG with VRR, Cumulus Networks recommends you set up a routed adjacency across the peerlink.4094 interface. If a routed connection is not built across the peer link, then during uplink failure on one of the switches in the MLAG pair, egress traffic can be blackholed if it hashes to the leaf whose uplinks are down.

To set up the adjacency, configure a [BGP](../../Layer-3/Border-Gateway-Protocol-BGP#unnumbered)
or [OSPF](../../Layer-3/Open-Shortest-Path-First-OSPF/) unnumbered peering, as appropriate for your network.

For example, if you are using BGP, use a configuration like this:

```
cumulus@switch:~$ net add bgp neighbor peerlink.4094 interface remote-as internal
cumulus@switch:~$ net commit
```

If you are using OSPF, use a configuration like this:

```
cumulus@switch:~$ net add interface peerlink.4094 ospf area 0.0.0.1
cumulus@switch:~$ net commit
```

If you are using [EVPN](../../Network-Virtualization/Ethernet-Virtual-Private-Network-EVPN/) and MLAG, you need to enable the EVPN address family across the peerlink.4094 interface as well:

```
cumulus@switch:~$ net add bgp neighbor peerlink.4094 interface remote-as internal
cumulus@switch:~$ net add bgp l2vpn evpn neighbor peerlink.4094 activate
cumulus@switch:~$ net commit
```

{{%notice tip%}}

Be aware of an existing issue when you use NCLU to create an iBGP peering, it creates an eBGP peering instead. For more information, see [release note 1222](https://support.cumulusnetworks.com/hc/en-us/articles/360007793174-Cumulus-Linux-3-7-Release-Notes#RN1222).

{{%/notice%}}

## IGMP Snooping with MLAG

[IGMP snooping](../IGMP-and-MLD-Snooping/) processes IGMP reports received on a bridge port in a bridge to identify hosts that are configured to receive multicast traffic destined to that group. An IGMP query message received on a port is used to identify the port that is connected to a router and configured to receive multicast traffic.

IGMP snooping is enabled by default on the bridge. IGMP snooping multicast database entries and router port entries are synced to the peer MLAG switch. If there is no multicast router in the VLAN, you can configure the IGMP querier on the switch to generate IGMP query messages. For more information, read the [IGMP and MLD Snooping](../IGMP-and-MLD-Snooping/) chapter.

{{%notice note%}}

 In an MLAG configuration, the switch in the secondary role does not
 send IGMP queries, even though the configuration is identical to the
 switch in the primary role. This is expected behavior, as there can be
 only one querier on each VLAN. Once the querier on the primary switch
 stops transmitting, the secondary switch starts transmitting.

{{%/notice%}}

## Monitor the Status of the clagd Service

Due to the critical nature of the `clagd` service, `systemd` continuously monitors the status of `clagd`. `systemd` monitors the `clagd` service through the use of notify messages every 30 seconds. If the `clagd` service dies or becomes unresponsive for any reason and `systemd` receives no messages after 60 seconds `systemd` restarts `clagd`. `systemd` logs these failures in `/var/log/syslog`, and, on the first failure, generates a `cl-support`file as well.

This monitoring is configured and enabled automatically as long as `clagd` is enabled (`clagd-peer-ip` and `clagd-sys-mac` are configured for an interface) and the `clagd` service is running. If you stop `clagd`, for example with the `systemctl stop clagd.service` command, `clagd` monitoring also stops.

You can check the status of `clagd` monitoring by using the `cl-service-summary` command:

```
cumulus@switch:~$ sudo cl-service-summary
The systemctl daemon 5.4 uptime: 15m
...
Service clagd        enabled    active 
...
```

Or the `systemctl status` command:

```
cumulus@switch:~$ sudo systemctl status clagd.service
 ● clagd.service - Cumulus Linux Multi-Chassis LACP Bonding Daemon
    Loaded: loaded (/lib/systemd/system/clagd.service; enabled)
    Active: active (running) since Mon 2016-10-03 20:31:50 UTC; 4 days ago
        Docs: man:clagd(8)
    Main PID: 1235 (clagd)
    CGroup: /system.slice/clagd.service
            ├─1235 /usr/bin/python /usr/sbin/clagd --daemon 169.254.255.2 peerlink.4094 44:38:39:FF:40:90 --prior...
            └─1307 /sbin/bridge monitor fdb

Feb 01 23:19:30 leaf01 clagd[1717]: Cleanup is executing.
Feb 01 23:19:31 leaf01 clagd[1717]: Cleanup is finished
Feb 01 23:19:31 leaf01 clagd[1717]: Beginning execution of clagd version 1.3.0
Feb 01 23:19:31 leaf01 clagd[1717]: Invoked with: /usr/sbin/clagd --daemon 169.254.255.2 peerlink.4094 44:38:39:FF:40:94 --pri...168.0.12
Feb 01 23:19:31 leaf01 clagd[1717]: Role is now secondary
Feb 01 23:19:31 leaf01 clagd[1717]: Initial config loaded
Feb 01 23:19:31 leaf01 systemd[1]: Started Cumulus Linux Multi-Chassis LACP Bonding Daemon.
Feb 01 23:24:31 leaf01 clagd[1717]: HealthCheck: reload timeout.
Feb 01 23:24:31 leaf01 clagd[1717]: Role is now primary; Reload timeout
Hint: Some lines were ellipsized, use -l to show in full.
```

## MLAG Best Practices

For MLAG to function properly, you must configure the dual-connected host interfaces identically on the pair of peering switches. See the note above in the [Configuring MLAG](#configure-mlag) section.

### MTU in an MLAG Configuration

The [MTU](../../Layer-1-and-Switch-Ports/Interface-Configuration-and-Management/Switch-Port-Attributes/) in MLAG traffic is determined by the bridge MTU. Bridge MTU is determined by the lowest MTU setting of an interface that is a member of the bridge. If you want to set an MTU other than the default (1500 bytes on a Broadcom switch or 9248 bytes on a Mellanox switch), you must configure the MTU on each physical interface and bond interface that are members of the MLAG bridges in the entire bridged domain.

For example, if an MTU of 9216 is desired through the MLAG domain in the example shown above, **on all four leaf switches**, [configure `mtu 9216`](../../Layer-1-and-Switch-Ports/Interface-Configuration-and-Management/Switch-Port-Attributes/) for each of the following bond interfaces, as they are members of bridge *bridge*: peerlink, uplink, server01.

<details>

<summary>NCLU Commands </summary>

```
cumulus@switch:~$ net add bond peerlink mtu 9216
cumulus@switch:~$ net add bond uplink mtu 9216
cumulus@switch:~$ net add bond server01 mtu 9216
cumulus@switch:~$ net pending
cumulus@switch:~$ net commit
```

</details>

<details>

<summary>Linux Commands </summary>

Edit the `/etc/network/interfaces` file. This is an example configuration:

```
cumulus@switch:~$ sudo nano /etc/network/interfaces
...
auto bridge
iface bridge
    bridge-ports peerlink uplink server01

auto peerlink
iface peerlink
    mtu 9216

auto server01
iface server01
    mtu 9216

auto uplink
iface uplink
    mtu 9216
...
```

Run `ifreload -a` to reload the configuration:

```
cumulus@switch:~$ sudo ifreload -a
```

</details>

### Peer Link Sizing

The peer link carries very little traffic when compared to the bandwidth consumed by dataplane traffic. In a typical MLAG configuration, most every connection between the two switches in the MLAG pair is dual-connected  so the only traffic going across the peer link is traffic from the `clagd` process and some LLDP or LACP traffic; the traffic received on the peer link is not forwarded out of the dual-connected bonds.

However, there are some instances where a host is connected to only one switch in the MLAG pair; for example:

- You have a hardware limitation on the host where there is only one PCIE slot, and therefore, one NIC on the system, so the host is only single-connected across that interface.
- The host does not support 802.3ad and you cannot create a bond on it.
- You are accounting for a link failure, where the host becomes single connected until the failure is resolved.

Cumulus Networks recommends you determine how much bandwidth is traveling across the single-connected interfaces and allocate half of that bandwidth to the peer link. On average, one half of the traffic destined to the single-connected host arrives on the switch directly connected to the single-connected host and the other half arrives on the switch that is not directly connected to the single-connected host. When this happens, only the traffic that arrives on the switch that is not directly connected to the single-connected host needs to traverse the peer link.

In addition, you might want to add extra links to the peer link bond to handle link failures in the peer link bond itself.

In the illustration below, each host has two 10G links, with each 10G link going to each switch in the MLAG pair. Each host has 20G of dual-connected bandwidth, so all three hosts have a total of 60G of dual-connected bandwidth. Cumulus Networks recommend you allocate at least 15G of bandwidth to each peer link bond, which represents half of the single-connected bandwidth.

{{< img src = "/images/cumulus-linux/mlag-peerlink-sizing.png" >}}

Scaling this example out to a full rack, when planning for link failures, you need only allocate enough bandwidth to meet your site's strategy for handling failure scenarios. Imagine a full rack with 40 servers and two switches. You might plan for four to six servers to lose connectivity to a single switch and become single connected before you respond to the event. So expanding upon our previous example, if you have 40 hosts each with 20G of bandwidth dual-connected to the MLAG pair, you might allocate 20G to 30G of bandwidth to the peer link — which accounts for half of the single-connected bandwidth for four to six hosts.

### Failover Redundancy Scenarios

To get a better understanding of how STP and LACP behave in response to various failover redundancy scenarios, read [this knowledge base article](https://support.cumulusnetworks.com/hc/en-us/articles 217942577-Understanding-MLAG-Redundancy-Scenarios).

## STP Interoperability with MLAG

Cumulus Networks recommends that you always enable STP in your layer 2 network.

With MLAG, Cumulus Networks recommends you enable BPDU guard on the host-facing bond interfaces. For more information about BPDU guard, see [BPDU Guard and Bridge Assurance](../Spanning-Tree-and-Rapid-Spanning-Tree#bpdu-guard).

To show useful troubleshooting information:

<details>

<summary>NCLU Commands </summary>

Run the `net show bridge spanning-tree` command:

```
cumulus@switch:~$ net show bridge spanning-tree
Bridge info
    enabled         yes
    bridge id       8.000.44:39:39:FF:40:94
    Priority:   32768
    Address:    44:39:39:FF:40:94
    This bridge is root.

designated root 8.000.44:39:39:FF:40:94
Priority:   32768
Address:    44:39:39:FF:40:94

root port       none
path cost     0          internal path cost   0
max age       20         bridge max age       20
forward delay 15         bridge forward delay 15
tx hold count 6          max hops             20
hello time    2          ageing time          300
force protocol version     rstp

E bond01 8.001 forw 8.000.44:39:39:FF:40:94 8.000.44:39:39:FF:40:94 8.001 Desg
E bond02 8.002 forw 8.000.44:39:39:FF:40:94 8.000.44:39:39:FF:40:94 8.002 DesgE peerlink F.003 forw 8.000.44:39:39:FF:40:94 8.000.44:39:39:FF:40:94 F.003 Desg
E vni13 8.004 forw 8.000.44:39:39:FF:40:94 8.000.44:39:39:FF:40:94 8.004 Desg
E vni24 8.005 forw 8.000.44:39:39:FF:40:94 8.000.44:39:39:FF:40:94 8.005 Desg
E vxlan4001 8.006 forw 8.000.44:39:39:FF:40:94 8.000.44:39:39:FF:40:94 8.006 Desg
```

</details>

<details>

<summary>Linux Commands </summary>

Run the `mstpctl showportdetail` command:

```
cumulus@switch:~$ sudo mstpctl showportdetail bridge peerlink

bridge:peerlink CIST info
    enabled            yes                     role                 Designated
    port id            F.003                   state                forwarding
    external port cost 10000                   admin external cost  0
    internal port cost 10000                   admin internal cost  0
    designated root    8.000.44:39:39:FF:40:94 dsgn external cost   0
    dsgn regional root 8.000.44:39:39:FF:40:94 dsgn internal cost   0
    designated bridge  8.000.44:39:39:FF:40:94 designated port      F.003
    admin edge port    no                      auto edge port       yes
    oper edge port     yes                     topology change ack  no
    point-to-point     yes                     admin point-to-point auto
    restricted role    no                      restricted TCN       no
    port hello time    2                       disputed             no
    bpdu guard port    no                      bpdu guard error     no
    network port       no                      BA inconsistent      no
    Num TX BPDU        6                       Num TX TCN           0
    Num RX BPDU        0                       Num RX TCN           0
    Num Transition FWD 2                       Num Transition BLK   1
    bpdufilter port    no
    clag ISL           yes                     clag ISL Oper UP     yes
    clag role          primary                 clag dual conn mac   00:00:00:00:00:00
    clag remote portID F.FFF                   clag system mac      44:39:39:FF:40:94
```

</details>

{{%notice note%}}

**Best Practices for STP with MLAG**

- The STP global configuration must be the same on both peer switches.
- The STP configuration for dual-connected ports must be the same on both peer switches.
- The STP priority must be the same on both peer switches.

For additional information on STP, see [Spanning Tree Priority](../Spanning-Tree-and-Rapid-Spanning-Tree/).

{{%/notice%}}

## Troubleshooting

### Viewing the MLAG Log File

By default, when `clagd` is running, it logs its status to the `/var/log/clagd.log` file and `syslog`. Example log file output is below:

```
cumulus@spine01:~$ sudo tail /var/log/clagd.log 
2016-10-03T20:31:50.471400+00:00 spine01 clagd[1235]: Initial config loaded
2016-10-03T20:31:52.479769+00:00 spine01 clagd[1235]: The peer switch is active.
2016-10-03T20:31:52.496490+00:00 spine01 clagd[1235]: Initial data sync to peer done.
2016-10-03T20:31:52.540186+00:00 spine01 clagd[1235]: Role is now primary; elected
2016-10-03T20:31:54.250572+00:00 spine01 clagd[1235]: HealthCheck: role via backup is primary
2016-10-03T20:31:54.252642+00:00 spine01 clagd[1235]: HealthCheck: backup active
2016-10-03T20:31:54.537967+00:00 spine01 clagd[1235]: Initial data sync from peer done.
2016-10-03T20:31:54.538435+00:00 spine01 clagd[1235]: Initial handshake done.
2016-10-03T20:31:58.527464+00:00 spine01 clagd[1235]: leaf03-04 is now dual connected.
2016-10-03T22:47:35.255317+00:00 spine01 clagd[1235]: leaf01-02 is now dual connected.
```

### Large Packet Drops on the Peer Link Interface

A large volume of packet drops across one of the peer link interfaces can be expected. These drops serve to prevent looping of BUM (broadcast, unknown unicast, multicast) packets. When a packet is received across the peer link, if the destination lookup results in an egress interface that is a dual-connected bond, the switch does not forward the packet to prevent loops. This results in a drop being recorded on the peer link.

You can detect this issue by running the the following commands:

<details>

<summary>NCLU Commands </summary>

Run the `net show counters` command. The number of dropped packets is displayed in the `RX_DRP` column.

```
cumulus@switch:~$ net show counters

Kernel Interface table
Iface              MTU    Met    RX_OK    RX_ERR    RX_DRP    RX_OVR    TX_OK    TX_ERR    TX_DRP    TX_OVR  Flg
---------------  -----  -----    -------  --------  --------  --------  -------  --------  --------  ------  -----
peerlink        1500       0      19226721     0      2952460  0       55115330     0       364      0       BMmRU
peerlink.4094   1500       0      0            0      0        0       5379243      0       0        0       BMRU
swp51           1500       0      6587220      0      2129676  0       38957769     0       202      0       BMsRU
swp52           1500       0      12639501     0      822784   0       16157561     0       162      0       BMsRU
```

</details>

<details>

<summary>Linux Commands </summary>

Run the `ethtool -S <interface>` command. The number of dropped packets are indicated by the `HwIfInDiscards` counter.

```
cumulus@switch:~$ sudo ethtool -S swp51
NIC statistics:
HwIfInOctets: 669507330
HwIfInUcastPkts: 658871
HwIfInBcastPkts: 2231559
HwIfInMcastPkts: 3696790
HwIfOutOctets: 2752224343
HwIfOutUcastPkts: 1001632
HwIfOutMcastPkts: 3743199
HwIfOutBcastPkts: 34212938
HwIfInDiscards: 2129675
```

</details>

### Duplicate LACP Partner MAC Warning

When you run `clagctl`, you may see output like this:

```
bond01 bond01 52 duplicate lacp - partner mac
```

This occurs when you have multiple LACP bonds between the same two LACP endpoints; for example, an MLAG switch pair is one endpoint and an ESXi host is another. These bonds have duplicate LACP identifiers, which are MAC addresses. This same warning might trigger when you have a cabling or configuration error.

## Caveats and Errata

- If both the backup and peer connectivity are lost within a 30-second window, the switch in the secondary role misinterprets the event sequence, sees the peer switch as down and takes over as the primary.
