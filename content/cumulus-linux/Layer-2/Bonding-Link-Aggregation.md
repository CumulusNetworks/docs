---
title: Bonding - Link Aggregation
author: Cumulus Networks
weight: 121
aliases:
 - /display/DOCS/Bonding+++Link+Aggregation
 - /pages/viewpage.action?pageId=8366376
 - /display/DOCS/Bonding+Link+Aggregation
 - /display/DOCS/Bonding+-+Link+Aggregation
 - /pages/viewpage.action?pageId=8362653
product: Cumulus Linux
version: '4.0'
---
Linux bonding provides a method for aggregating multiple network interfaces (*slaves*) into a single logical bonded interface (*bond*). Link aggregation is useful for linear scaling of bandwidth, load balancing, and failover protection.

Cumulus Linux supports two bonding modes:

- IEEE 802.3ad link aggregation mode that allows one or more links to be aggregated together to form a *link aggregation group* (LAG) so that a media access control (MAC) client can treat the group as if it were a single link. IEEE 802.3ad link aggregation is the default mode.
- Balance-xor mode, where the bonding of slave interfaces are static and all slave interfaces are active for load balancing and fault tolerance purposes. This is useful for [MLAG](../Multi-Chassis-Link-Aggregation-MLAG/) deployments.

Cumulus Linux uses version 1 of the LAG control protocol (LACP).

To temporarily bring up a bond even when there is no LACP partner, use [LACP Bypass](../LACP-Bypass/).

## Hash Distribution

Egress traffic through a bond is distributed to a slave based on a packet hash calculation, providing load balancing over the slaves; many conversation flows are distributed over all available slaves to load balance the total traffic. Traffic for a single conversation flow always hashes to the same slave.

The hash calculation uses packet header data to choose to which slave to transmit the packet:

- For IP traffic, IP header source and destination fields are used in the calculation.
- For IP + TCP/UDP traffic, source and destination ports are included in the hash calculation.

{{%notice note%}}

In a failover event, the hash calculation is adjusted to steer traffic over available slaves.

{{%/notice%}}

## Create a Bond

In the example below, the front panel port interfaces swp1 thru swp4 are slaves in bond0, while swp5 and swp6 are not part of bond0.

{{< img src = "/images/cumulus-linux/bonding-example.png" >}}

To create and configure a bond:

<details>

<summary>NCLU Commands </summary>

Run the `net add bond` command. The example command below creates a bond called `bond0` with slaves swp1, swp2, swp3, and swp4:

```
cumulus@switch:~$ net add bond bond0 bond slaves swp1-4
cumulus@switch:~$ net pending
cumulus@switch:~$ net commit
```

</details>

<details>

<summary>Linux Commands </summary>

Edit the `/etc/network/interfaces` file and add a stanza for the bond. The example below creates a bond called `bond0` with slaves swp1, swp2, swp3, and swp4:

```
cumulus@switch:~$ sudo nanno /etc/network/interfaces
...
auto bond0
iface bond0
    bond-slaves swp1 swp2 swp3 swp4
...
```

Run the `ifreload -a` command to load the new configuration:

```
cumulus@switch:~$ ifreload -a
```

</details>

{{%notice note%}}

- The bond is configured by default in IEEE 802.3ad link aggregation mode. To configure the bond in balance-xor mode, see [Configuration Parameters](#configure-bond-options) below.
- If the bond is *not* going to become part of a bridge, you need to specify an IP address.
- The name of the bond must be compliant with Linux interface naming conventions and unique within the switch.

{{%/notice%}}

When networking is started on the switch, bond0 is created as MASTER and interfaces swp1 thru swp4 come up in SLAVE mode, as seen in the `ip link show` command:

```
cumulus@switch:~$ ip link show
...

3: swp1: <BROADCAST,MULTICAST,SLAVE,UP,LOWER_UP> mtu 1500 qdisc pfifo_fast master bond0 state UP mode DEFAULT qlen 500
    link/ether 44:38:39:00:03:c1 brd ff:ff:ff:ff:ff:ff
4: swp2: <BROADCAST,MULTICAST,SLAVE,UP,LOWER_UP> mtu 1500 qdisc pfifo_fast master bond0 state UP mode DEFAULT qlen 500
    link/ether 44:38:39:00:03:c1 brd ff:ff:ff:ff:ff:ff
5: swp3: <BROADCAST,MULTICAST,SLAVE,UP,LOWER_UP> mtu 1500 qdisc pfifo_fast master bond0 state UP mode DEFAULT qlen 500
    link/ether 44:38:39:00:03:c1 brd ff:ff:ff:ff:ff:ff
6: swp4: <BROADCAST,MULTICAST,SLAVE,UP,LOWER_UP> mtu 1500 qdisc pfifo_fast master bond0 state UP mode DEFAULT qlen 500
    link/ether 44:38:39:00:03:c1 brd ff:ff:ff:ff:ff:ff
...

55: bond0: <BROADCAST,MULTICAST,MASTER,UP,LOWER_UP> mtu 1500 qdisc noqueue state UP mode DEFAULT
    link/ether 44:38:39:00:03:c1 brd ff:ff:ff:ff:ff:ff
```

{{%notice note%}}

All slave interfaces within a bond have the same MAC address as the bond. Typically, the first slave added to the bond donates its MAC address as the bond MAC address, whereas the MAC addresses of the other slaves are set to the bond MAC address. The bond MAC address is used as the source MAC address for all traffic leaving the bond and provides a single destination MAC address to address traffic to the bond.

{{%/notice%}}

## Configure Bond Options

The configuration options for a bond are are described in the table below. To configure a bond:

<details>

<summary>NCLU Commands </summary>

Run `net add bond <bond-name> bond <option>`. The following example sets the bond mode for bond01 to `balance-xor`:

```
cumulus@switch:~$ net add bond bond1 bond mode balance-xor
cumulus@switch:~$ net pending
cumulus@switch:~$ net commit
```

</details>

<details>

<summary>Linux Commands </summary>

Edit the `/etc/network/interfaces` file and add the parameter to the bond stanza, then load the new configuration. The following example sets the bond mode for bond01 to `balance-xor`:

```
cumulus@switch:~$ sudo nanno /etc/network/interfaces
...
auto bond1
iface bond1
    bond-mode balance-xor
    bond-slaves swp1 swp2 swp3 swp4
...
```

Run the `ifreload -a` command to load the new configuration:

```
cumulus@switch:~$ ifreload -a
```

</details>

{{%notice note%}}

Each bond configuration option, except for `bond slaves,` is set to the recommended value by default in Cumulus Linux. Only configure an option if a different setting is needed. For more information on configuration values, refer to the [Related Information](#related-information) section below.

{{%/notice%}}

| Parameter| Description|
|---------- |---------- |
| `bond-mode 802.3ad`\|`balance-xor` | Cumulus Linux supports IEEE 802.3ad link aggregation mode (802.3ad) and balance-xor mode.<br>The default mode is 802.3ad.<br><br>**Note:** When you enable balance-xor mode, the bonding of slave interfaces are static and all slave interfaces are active for load balancing and fault tolerance purposes. Packet transmission on the bond is based on the hash policy specified by xmit-hash-policy.<br><br>When using balance-xor mode to dual-connect host-facing bonds in an MLAG environment, you must configure the clag-id parameter on the MLAG bonds and it must be the same on both MLAG switches. Otherwise, the bonds are treated by the MLAG switch pair as single-connected.<br><br>Use balance-xor mode only if you cannot use LACP; LACP can detect mismatched link attributes between bond members and can even detect misconnections. |
| `bond-slaves <interface-list>` | The list of slaves in the bond. |
| `bond miimon <value>` |Defines how often the link state of each slave is inspected for failures. You can specify a value between 0 and 255. The default value is 100. |
| `bond downdelay <milliseconds>` |Specifies the time, in milliseconds (between 0 and 65535), to wait before disabling a slave after a link failure is detected. The default value is 0.<br><br>This option is only valid for the miimon link monitor. The downdelay value must be a multiple of the miimon value; if not, it is rounded down to the nearest multiple. |
| `bond-updelay <milliseconds>` |Specifies the time, in milliseconds (between 0 and 65535), to wait before enabling a slave after a link recovery is detected. The default value is 0.<br><br>This option is only valid for the miimon link monitor. The updelay value must be a multiple of the miimon value; if not, it is rounded down to the nearest multiple. |
| `bond-use-carrier no` | Determines the link state. |
| `bond-lacp-bypass-allow`| Enables LACP bypass. |
| `bond-lacp-rate slow` | Sets the rate to ask the link partner to transmit LACP control packets. slow is the only option. |
| `bond-min-links` | Defines the minimum number of links (between 0 and 255) that must be active before the bond is put into service. The default value is 1.<br><br>A value greater than 1 is useful if higher level services need to ensure a minimum aggregate bandwidth level before activating a bond. Keeping bond-min-links set to 1 indicates the bond must have at least one active member. If the number of active members drops below the bond-min-links setting, the bond appears to upper-level protocols as link-down. When the number of active links returns to greater than or equal to bond-min-links, the bond becomes link-up. |

## Show Bond Information

To show information for a bond:

<details>

<summary>NCLU Commands </summary>

Run the `net show interface <bond>` command:

```
cumulus@switch:~$ net show interface bond1
    Name    MAC                Speed    MTU    Mode
--  ------  -----------------  -------  -----  ------
UP  bond1   00:02:00:00:00:12  20G      1500   Bond


Bond Details
---------------  -------------
Bond Mode:       Balance-XOR
Load Balancing:  Layer3+4
Minimum Links:   1
In CLAG:         CLAG Inactive


    Port     Speed      TX    RX    Err    Link Failures
--  -------  -------  ----  ----  -----  ---------------
UP  swp3(P)  10G         0     0      0                0
UP  swp4(P)  10G         0     0      0                0


LLDP
-------  ----  ------------
swp3(P)  ====  swp1(p1c1h1)
swp4(P)  ====  swp2(p1c1h1)Routing
-------
  Interface bond1 is up, line protocol is up
  Link ups:       3    last: 2017/04/26 21:00:38.26
  Link downs:     2    last: 2017/04/26 20:59:56.78
  PTM status: disabled
  vrf: Default-IP-Routing-Table
  index 31 metric 0 mtu 1500
  flags: <UP,BROADCAST,RUNNING,MULTICAST>
  Type: Ethernet
  HWaddr: 00:02:00:00:00:12
  inet6 fe80::202:ff:fe00:12/64
  Interface Type Other
```

</details>

<details>

<summary>Linux Commands </summary>

Run the `sudo cat /proc/net/bonding/<bond>` command:

```
cumulus@switch:~$ sudo cat /proc/net/bonding/bond01

Ethernet Channel Bonding Driver: v3.7.1 (April 27, 2011)
Bonding Mode: load balancing (xor)
Transmit Hash Policy: layer3+4 (1)
MII Status: up
MII Polling Interval (ms): 100
Up Delay (ms): 0
Down Delay (ms): 0


Slave Interface: swp1
MII Status: up
Speed: 1000 Mbps
Duplex: full
Link Failure Count: 0
Permanent HW addr: 44:38:39:00:00:03
Slave queue ID: 0
```

</details>

## Caveats and Errata

- An interface cannot belong to multiple bonds.
- A bond can have subinterfaces, but subinterfaces cannot have a bond.
- A bond cannot enslave VLAN subinterfaces.
- Set all slave ports within a bond to the same speed/duplex and make sure they match the link partner’s slave ports.
- On a [Cumulus RMP](/cumulus-rmp) switch, if you create a bond with multiple 10G member ports, traffic gets dropped when the bond uses members of the same *unit* listed in the `/var/lib/cumulus/porttab` file. For example, traffic gets dropped if both swp49 and swp52 are in the bond because they both are in xe0 (or if both swp50 and swp51 are in the same bond because they are both in xe1):

```
swp49 xe0 0 0 -1 0
swp50 xe1 0 0 -1 0
swp51 xe1 1 0 -1 0
swp52 xe0 1 0 -1 0
```

    Single port member bonds, bonds with different units (xe0 or xe1, as above), or layer 3 bonds do not have this issue.

    {{%notice note%}}

On Cumulus RMP switches, which are built with two Hurricane2 ASICs, you cannot form an LACP bond on links that terminate on different Hurricane2 ASICs.

    {{%/notice%}}

## Related Information

- [Linux Foundation - Bonding](http://www.linuxfoundation.org/collaborate/workgroups/networking/bonding)
- [802.3ad](http://www.ieee802.org/3/ad/) ([Accessible writeup](http://cs.uccs.edu/%7Escold/doc/linkage%20aggregation.pdf))
- [Wikipedia - Link aggregation](http://en.wikipedia.org/wiki/Link_aggregation)
