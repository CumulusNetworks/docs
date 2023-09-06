---
title: Bonding - Link Aggregation
author: NVIDIA
weight: 480
toc: 3
---
Linux bonding provides a method for aggregating multiple network interfaces (*slaves*) into a single logical bonded interface (*bond*). Link aggregation is useful for linear scaling of bandwidth, load balancing, and failover protection.

Cumulus Linux supports two bonding modes:

- IEEE 802.3ad link aggregation mode that allows you to combine one or more links to form a *link aggregation group* (LAG) so that a media access control (MAC) client can treat the group as a single link. IEEE 802.3ad link aggregation is the default mode.
- Balance-xor mode, where the bonding of slave interfaces are static and all slave interfaces are active for load balancing and fault tolerance purposes. This is useful for {{<link url="Multi-Chassis-Link-Aggregation-MLAG" text="MLAG">}} deployments.

Cumulus Linux uses version 1 of the LAG control protocol (LACP).

To temporarily bring up a bond even when there is no LACP partner, use {{<link title="LACP Bypass">}}.

## Hash Distribution

The switch distributes egress traffic through a bond to a slave based on a packet hash calculation, providing load balancing over the slaves; the switch distributes conversation flows over all available slaves to load balance the total traffic. Traffic for a single conversation flow always hashes to the same slave.

The hash calculation uses packet header data to choose to which slave to transmit the packet:

- For IP traffic, the switch uses IP header source and destination fields in the calculation.
- For IP + TCP/UDP traffic, the switch  includes source and destination ports in the hash calculation.

{{%notice note%}}
In a failover event, the switch adjusts the hash calculation to steer traffic over available slaves.
{{%/notice%}}

### LAG Custom Hashing

You can configure the fields you want to use in the LAG hash calculation. For example, if you do not want to use source or destination port numbers in the hash calculation, you can disable the source port and destination port fields.

You can configure the following fields:  

- Source MAC
- Destination
- Source IP
- Destination IP
- Ether type
- VLAN ID
- Source port
- Destination port
- Layer 3 protocol

To configure custom hash, edit the `/etc/cumulus/datapath/traffic.conf` file:

1. To enable custom hashing, uncomment the `lag_hash_config.enable = true` line.
2. To enable a field, set the field to `true`. To disable a field, set the field to `false`.
3. Run the `echo 1 > /cumulus/switchd/ctrl/hash_config_reload` command. This command does not cause any traffic interruptions.

The following shows an example `/etc/cumulus/datapath/traffic.conf` file:

```
cumulus@switch:~$ sudo nano /etc/cumulus/datapath/traffic.conf
...
#LAG HASH config
#HASH config for LACP to enable custom fields
#Fields will be applicable for LAG hash
#calculation
#Uncomment to enable custom fields configured below
lag_hash_config.enable = true

lag_hash_config.smac = true
lag_hash_config.dmac = true
lag_hash_config.sip  = true
lag_hash_config.dip  = true
lag_hash_config.ether_type = true
lag_hash_config.vlan_id = true
lag_hash_config.sport = false
lag_hash_config.dport = false
lag_hash_config.ip_prot = true
...
```

{{%notice note%}}
Cumulus Linux enables symmetric hashing by default. Make sure that the settings for the source IP (`lag_hash_config.sip`) and destination IP (`lag_hash_config.dip`) fields match, and that the settings for the source port (`lag_hash_config.sport`) and destination port (`lag_hash_config.dport`) fields match; otherwise symmetric hashing disables automatically. You can disable symmetric hashing manually in the `/etc/cumulus/datapath/traffic.conf` file by setting `symmetric_hash_enable = FALSE`.
{{%/notice%}}

You can set a unique hash seed for each switch to avoid hash polarization. See {{<link url="Equal-Cost-Multipath-Load-Sharing-Hardware-ECMP#configure-a-hash-seed-to-avoid-hash-polarization" text="Configure a Hash Seed to Avoid Hash Polarization">}}.

## Create a Bond

In the example below, the front panel port interfaces swp1 thru swp4 are slaves in bond0, while swp5 and swp6 are not part of bond0.

{{< img src = "/images/cumulus-linux/bonding-example.png" >}}

To create and configure a bond:

{{< tabs "TabID91 ">}}
{{< tab "NCLU Commands ">}}

```
cumulus@switch:~$ net add bond bond0 bond slaves swp1-4
cumulus@switch:~$ net pending
cumulus@switch:~$ net commit
```

{{< /tab >}}
{{< tab "NVUE Commands ">}}

```
cumulus@switch:~$ nv set interface bond0 bond member swp1-4
cumulus@switch:~$ nv config apply
```

{{< /tab >}}
{{< tab "Linux Commands ">}}

Edit the `/etc/network/interfaces` file to add a stanza for the bond, then run the `ifreload -a` command.

```
cumulus@switch:~$ sudo nano /etc/network/interfaces
...
auto bond0
iface bond0
    bond-slaves swp1 swp2 swp3 swp4
...
```

```
cumulus@switch:~$ ifreload -a
```

{{< /tab >}}
{{< /tabs >}}

{{%notice note%}}
- By default, the bond uses IEEE 802.3ad link aggregation mode. To configure the bond in balance-xor mode, see {{<link url="#configure-bond-options" text="Configuration Parameters">}} below.
- If the bond is *not* going to be part of a bridge, you must specify an IP address.
- Make sure the name of the bond adheres to Linux interface naming conventions and is unique within the switch.
- Do not use a dash (-) in the bond name.
- Cumulus Linux does not support bond members at 200G or greater.
- NVUE does not accept a bond name starting with an interface type ID, such as `sw`, `eth`, `vlan`, `lo`, `ib`, `fnm`, or `vrrp`. For example, you cannot name a bond `login123`, `eth2`, `sw1`, or `vlan10`.
{{%/notice%}}

When you start networking, the switch creates bond0 as MASTER and interfaces swp1 thru swp4 come up in SLAVE mode:

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
All slave interfaces within a bond have the same MAC address as the bond. Typically, the first slave you add to the bond donates its MAC address as the bond MAC address, whereas the MAC addresses of the other slaves are the bond MAC address. The bond MAC address is the source MAC address for all traffic leaving the bond and provides a single destination MAC address to address traffic to the bond.

Removing a bond slave interface from which a bond derives its MAC address affects traffic when the bond interface flaps to update the MAC address.
{{%/notice%}}

## Configure Bond Options

The table below describes the configuration options for a bond. To configure a bond, run the commands shown or add the parameter to the bond stanza in the `/etc/network/interfaces` file.

The following example sets the bond mode for bond01 to balance-xor (static):

{{< tabs "TabID166 ">}}
{{< tab "NCLU Commands ">}}

```
cumulus@switch:~$ net add bond bond1 bond mode balance-xor
cumulus@switch:~$ net pending
cumulus@switch:~$ net commit
```

{{< /tab >}}
{{< tab "NVUE Commands ">}}

```
cumulus@switch:~$ nv set interface bond01 bond mode static 
cumulus@switch:~$ nv config apply
```

{{< /tab >}}
{{< tab "Linux Commands ">}}

Edit the `/etc/network/interfaces` file to add the `balance-xor` parameter to the bond stanza, then run the `ifreload -a` command:

```
cumulus@switch:~$ sudo nano /etc/network/interfaces
...
auto bond1
iface bond1
    bond-mode balance-xor
    bond-slaves swp1 swp2 swp3 swp4
...
```

```
cumulus@switch:~$ ifreload -a
```

{{< /tab >}}
{{< /tabs >}}

{{%notice note%}}
Each bond configuration option, except for `bond slaves,` has the recommended value by default in Cumulus Linux. Only configure an option if you need a different setting. For more information on configuration values, refer to the {{<link url="#related-information" text="Related Information">}}  section below.
{{%/notice%}}

| Parameter |  Description|
|---------- | ---------- |
| `bond-mode 802.3ad`<br><br>`bond-mode balance-xor` | Cumulus Linux supports IEEE 802.3ad link aggregation mode (802.3ad) and balance-xor mode.<br>The default mode is 802.3ad.<br><br>**Note:** When you enable balance-xor mode, the bonding of slave interfaces are static and all slave interfaces are active for load balancing and fault tolerance. The switch bases packet transmission on the bond on the hash policy in xmit-hash-policy.<br><br>When you use balance-xor mode to dual-connect host-facing bonds in an MLAG environment, you must configure the `clag-id` parameter with the same value on both MLAG switches. Otherwise, the MLAG switch pair treats the bonds as single-connected.<br><br>Use balance-xor mode only if you cannot use LACP; LACP can detect mismatched link attributes between bond members and can even detect misconnections. <br><br>NCLU command: `net add bond <bond-name> bond mode balance-xor` <br>NVUE command: `nv set interface <bond-name> bond mode static` |
| `bond miimon <value>` | Defines how often to inspect the link state of each slave for failures. You can specify a value between 0 and 255. The default value is 100. |
| `bond-use-carrier no` | Determines the link state. |
| `bond-lacp-bypass-allow`| Enables LACP bypass.<br><br>NCLU command: `net add bond <bond-name> bond lacp-bypass-allow` <br>NVUE command: `nv set interface <bond-name> bond lacp-bypass on` |
| `bond-lacp-rate slow` | Sets the rate to ask the link partner to transmit LACP control packets. `slow` is the only option. |
| `bond-min-links` | Defines the minimum number of links (between 0 and 255) that must be active before the bond goes into service. The default value is 1.<br><br>Use a value greater than 1 if you need higher level services to ensure a minimum aggregate bandwidth level before activating a bond. Keeping the `bond-min-links` value at 1 indicates the bond must have at least one active member. If the number of active members drops below the `bond-min-links` setting, the bond appears to upper-level protocols as link-down. When the number of active links returns to greater than or equal to `bond-min-links`, the bond becomes link-up. |

## Show Bond Information

To show information for a bond:

{{< tabs "TabID222 ">}}
{{< tab "NCLU Commands ">}}

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

{{< /tab >}}
{{< tab "Linux Commands ">}}

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

{{< /tab >}}
{{< /tabs >}}

{{%notice info%}}
The detailed output in `/proc/net/bonding/<filename>` includes the actor/partner LACP information. This information is not necessary and requires you to use `sudo` to view the file.
{{%/notice%}}

## Considerations

- An interface cannot belong to multiple bonds.
- A bond can have subinterfaces, but subinterfaces cannot have a bond.
- A bond cannot enslave VLAN subinterfaces.
- Set all slave ports within a bond to the same speed or duplex and make sure they match the slave ports of the link partner.

## Related Information

- {{<exlink url="http://www.ieee802.org/3/ad/" text="802.3ad">}} ({{<exlink url="http://cs.uccs.edu/%7Escold/doc/linkage%20aggregation.pdf" text="Accessible writeup">}})
- {{<exlink url="http://en.wikipedia.org/wiki/Link_aggregation" text="Wikipedia - Link aggregation">}}
