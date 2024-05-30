---
title: Bonding - Link Aggregation
author: NVIDIA
weight: 480
toc: 3
---
Linux bonding provides a way to aggregate multiple network interfaces (*slaves*) into a single logical bonded interface (bond). Link aggregation is useful for linear scaling of bandwidth, load balancing, and failover protection.

Cumulus Linux supports two bonding modes:

- IEEE 802.3ad link aggregation mode combines one or more links to form a *link aggregation group* (LAG) so that a media access control (MAC) client can treat the group as a single link. IEEE 802.3ad link aggregation is the default mode.
- Balance-xor mode balances outgoing traffic across active ports according to the hashed protocol header information and accepts incoming traffic from any active port. All slave interfaces are active for load balancing and fault tolerance. This is useful for {{<link url="Multi-Chassis-Link-Aggregation-MLAG" text="MLAG">}} deployments.

Cumulus Linux uses version 1 of the LAG control protocol (LACP).

{{%notice note%}}
- NVUE does not accept a bond name starting with an interface type ID, such as `sw`, `eth`, `vlan`, `lo`, `ib`, `fnm`, or `vrrp`. For example, you cannot name a bond `login123`, `eth2`, `sw1`, or `vlan10`.
- An interface cannot belong to multiple bonds.
- A bond can have subinterfaces, but subinterfaces cannot have a bond.
- A bond cannot enslave VLAN subinterfaces.
- All slave ports within a bond must have the same speed or duplex and match the slave ports of the link partner.
{{%/notice%}}

## Create a Bond

To create a bond, specify the bond members. In the example below, the front panel port interfaces swp1 thru swp4 are members of bond1 but swp5 and swp6 are not part of bond1.

{{< figure src = "/images/cumulus-linux/bonding-example1.png" >}}

{{< tabs "TabID91 ">}}
{{< tab "NVUE Commands ">}}

```
cumulus@switch:~$ nv set interface bond1 bond member swp1-4
cumulus@switch:~$ nv config apply
```

{{%notice note%}}
In NVUE, if you create the bond interface with a name that starts with `bond`, NVUE automatically sets the interface type to `bond`. If you create a bond interface with a name that does *not* start with `bond`, you must set the interface type to `bond` with the `nv set interface <interface-name> type bond` command.
{{%/notice%}}

{{< /tab >}}
{{< tab "Linux Commands ">}}

Edit the `/etc/network/interfaces` file to add a stanza for the bond, then run the `ifreload -a` command.

```
cumulus@switch:~$ sudo nano /etc/network/interfaces
...
auto bond1
iface bond1
    bond-slaves swp1 swp2 swp3 swp4
...
```

```
cumulus@switch:~$ ifreload -a
```

{{< /tab >}}
{{< /tabs >}}

{{%notice note%}}
- By default, the bond uses IEEE 802.3ad link aggregation mode. To configure the bond in balance-xor mode, see {{<link url="#optional-configuration" text="Optional Configuration">}} below.
- If the bond is *not* going to be part of a bridge, you must specify an IP address.
- Make sure the name of the bond adheres to Linux interface naming conventions and is unique within the switch.
- To temporarily bring up a bond even when there is no LACP partner, use {{<link title="LACP Bypass">}}.

{{%/notice%}}

When you start networking, the switch creates bond1 as MASTER and interfaces swp1 thru swp4 come up in SLAVE mode:

```
cumulus@switch:~$ ip link show
...

3: swp1: <BROADCAST,MULTICAST,SLAVE,UP,LOWER_UP> mtu 1500 qdisc pfifo_fast master bond1 state UP mode DEFAULT qlen 500
    link/ether 44:38:39:00:03:c1 brd ff:ff:ff:ff:ff:ff
4: swp2: <BROADCAST,MULTICAST,SLAVE,UP,LOWER_UP> mtu 1500 qdisc pfifo_fast master bond1 state UP mode DEFAULT qlen 500
    link/ether 44:38:39:00:03:c1 brd ff:ff:ff:ff:ff:ff
5: swp3: <BROADCAST,MULTICAST,SLAVE,UP,LOWER_UP> mtu 1500 qdisc pfifo_fast master bond1 state UP mode DEFAULT qlen 500
    link/ether 44:38:39:00:03:c1 brd ff:ff:ff:ff:ff:ff
6: swp4: <BROADCAST,MULTICAST,SLAVE,UP,LOWER_UP> mtu 1500 qdisc pfifo_fast master bond1 state UP mode DEFAULT qlen 500
    link/ether 44:38:39:00:03:c1 brd ff:ff:ff:ff:ff:ff
...

55: bond1: <BROADCAST,MULTICAST,MASTER,UP,LOWER_UP> mtu 1500 qdisc noqueue state UP mode DEFAULT
    link/ether 44:38:39:00:03:c1 brd ff:ff:ff:ff:ff:ff
```

All slave interfaces within a bond have the same MAC address as the bond. Typically, the first slave you add to the bond donates its MAC address as the bond MAC address. The bond MAC address is the source MAC address for all traffic leaving the bond and provides a single destination MAC address to address traffic to the bond.

Removing a bond slave interface from which a bond derives its MAC address affects traffic when the bond interface flaps to update the MAC address.

## Optional Configuration

You can set these configuration options for a bond.

| <div style="width:200px">Option  | Description |
|---------|------------ |
|Link aggregation mode |Cumulus Linux supports IEEE 802.3ad link aggregation mode (802.3ad) and balance-xor mode. The default mode is 802.3ad. <br>Set balance-xor mode only if you cannot use LACP; LACP can detect mismatched link attributes between bond members and can even detect misconnections.{{%notice note%}}When you use balance-xor mode to dual-connect host-facing bonds in an MLAG environment, you must configure the MLAG ID with the same value on both MLAG switches. Otherwise, the MLAG switch pair treats the bonds as single-connected.{{%/notice%}} |
|MII link monitoring frequency|How often (in milliseconds) you want to inspect the link state of each slave for failures. <br>You can specify a value between 0 and 255. The default value is 100. |
|miimon link status mode| The miimon link status mode. You can set the mode to either netif_carrier_ok(), or MII or ethtool ioctls. The default setting is netif_carrier_ok(). |
|LACP bypass| Set LACP bypass on a bond in 802.3ad mode so that it becomes active and forwards traffic even when there is no LACP partner. You can specify on or off. The default setting is off. See {{<link url="LACP-Bypass" text="LACP Bypass">}}.|
|Transmit rate| The rate at which the link partner transmits LACP control packets. You can specify slow or fast. The default setting is fast.|
|Minimum number of links| The minimum number of links that must be active before the bond goes into service. You can set a value between 0 and 255. The default value is 1, which indicates that the bond must have at least one active member.<br><br>Use a value greater than 1 if you need higher level services to ensure a minimum aggregate bandwidth level before activating a bond.<br><br>If the number of active members drops below this setting, the bond appears to upper-level protocols as link-down. When the number of active links returns to greater than or equal to this value, the bond becomes link-up.|

{{%notice note%}}
Cumulus Linux sets the bond configuration options to the recommended values by default; use caution when changing settings.
{{%/notice%}}

To set the link aggregation mode on bond1 to balance-xor mode:

{{< tabs "TabID107 ">}}
{{< tab "NVUE Commands ">}}

```
cumulus@switch:~$ nv set interface bond1 bond mode static 
cumulus@switch:~$ nv config apply
```

To reset the link aggregation mode for bond1 to the default value of 802.3ad, run the `nv set interface bond1 bond mode lacp` command.

{{< /tab >}}
{{< tab "Linux Commands ">}}

Edit the `/etc/network/interfaces` file and add the `balance-xor` parameter to the bond stanza, then run the `ifreload -a` command:

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

To reset the bond mode for bond1 to the default value of 802.3ad, use the `bond-mode 802.3ad` parameter:

```
cumulus@switch:~$ sudo nano /etc/network/interfaces
...
auto bond1
iface bond1
    bond-mode 802.3ad
    bond-slaves swp1 swp2 swp3 swp4
...
```

{{< /tab >}}
{{< /tabs >}}

To enable LACP bypass:

{{< tabs "TabID160 ">}}
{{< tab "NVUE Commands ">}}

```
cumulus@switch:~$ nv set interface bond1 bond lacp-bypass on 
cumulus@switch:~$ nv config apply
```

{{< /tab >}}
{{< tab "Linux Commands ">}}

Edit the `/etc/network/interfaces` file and add the `bond-lacp-bypass-allow` parameter to the bond stanza, then run the `ifreload -a` command:

```
cumulus@switch:~$ sudo nano /etc/network/interfaces
...
auto bond1
iface bond1
    bond-lacp-bypass-allow
    bond-slaves swp1 swp2 swp3 swp4
...
```

```
cumulus@switch:~$ ifreload -a
```

{{< /tab >}}
{{< /tabs >}}

To set the miimon link status mode to MII or ethtool ioctls:

{{< tabs "TabID192 ">}}
{{< tab "NVUE Commands ">}}

Cumulus Linux does not provide NVUE commands for this setting.

{{< /tab >}}
{{< tab "Linux Commands ">}}

Edit the `/etc/network/interfaces` file and add the `bond-use-carrier no` parameter to the bond stanza, then run the `ifreload -a` command:

```
cumulus@switch:~$ sudo nano /etc/network/interfaces
...
auto bond1
iface bond1
    bond-use-carrier no
    bond-slaves swp1 swp2 swp3 swp4
...
```

```
cumulus@switch:~$ ifreload -a
```

To reset the miimon link status mode to the default of netif_carrier_ok(), use the `bond-use-carrier yes` parameter.

{{< /tab >}}
{{< /tabs >}}

To set the rate at which the link partner transmits LACP control packets to slow:

{{< tabs "TabID216 ">}}
{{< tab "NVUE Commands ">}}

```
cumulus@switch:~$ nv set interface bond1 bond lacp-rate slow
cumulus@switch:~$ nv config apply
```

To reset the rate to the default value of fast, run the `nv set interface bond1 bond lacp-rate fast` command.

{{< /tab >}}
{{< tab "Linux Commands ">}}

Edit the `/etc/network/interfaces` file and add the `bond-lacp-rate slow` parameter to the bond stanza, then run the `ifreload -a` command:

```
cumulus@switch:~$ sudo nano /etc/network/interfaces
...
auto bond1
iface bond1
    bond-lacp-rate slow
    bond-slaves swp1 swp2 swp3 swp4
...
```

```
cumulus@switch:~$ ifreload -a
```

To reset the rate to the default (fast), use the `bond-lacp-rate fast` parameter:

{{< /tab >}}
{{< /tabs >}}

To set the minimum number of links that must be active before the bond goes into service to 50:

{{< tabs "TabID252 ">}}
{{< tab "NVUE Commands ">}}

Cumulus Linux does not provide NVUE commands for this setting.

{{< /tab >}}
{{< tab "Linux Commands ">}}

Edit the `/etc/network/interfaces` file and add the `bond-min-links 50` parameter to the bond stanza, then run the `ifreload -a` command:

```
cumulus@switch:~$ sudo nano /etc/network/interfaces
...
auto bond1
iface bond1
    bond-min-links 50
    bond-slaves swp1 swp2 swp3 swp4
...
```

```
cumulus@switch:~$ ifreload -a
```

{{< /tab >}}
{{< /tabs >}}

<!--## Load Balancing

The switch distributes egress traffic through a bond to a slave based on a packet hash calculation, providing load balancing over the slaves; the switch distributes conversation flows over all available slaves to load balance the total traffic. Traffic for a single conversation flow always hashes to the same slave. In a failover event, the switch adjusts the hash calculation to steer traffic over available slaves.

The hash calculation uses packet header data to choose to which slave to transmit the packet:

- For IP traffic, the switch uses IP header source and destination fields in the calculation.
- For IP and TCP or UDP traffic, the switch includes source and destination ports in the hash calculation.

For load balancing between multiple interfaces that are members of the same bond, you can hash on these fields:

| <div style="width:200px">Field  | Default Setting | `/etc/cumulus/datapath/traffic.conf` File Parameter |
| ------- | --------------- | ------------ |
| IP protocol | on |`lag_hash_config.ip_prot`|
| Source MAC address| on |`lag_hash_config.smac`|
| Destination MAC address| on |`lag_hash_config.dmac`|
| Source IP address | on |
| Destination IP address| on | `lag_hash_config.dip` |
| Source port | on |`lag_hash_config.sport` |
| Destination port | on | `lag_hash_config.dport` |
| Ethertype| on | `lag_hash_config.ether_type` |
| VLAN ID| on |`lag_hash_config.vlan_id` |

Cumulus Linux does not provide NVUE commands to configure load balancing.

To set the hash fields:

1. Edit the `/etc/cumulus/datapath/traffic.conf` file:
   - Uncomment the `lag_hash_config.enable` option.
   - Set the hash field to `true` to include it in the hash calculation or `false` to omit it from the hash calculation.

2. Run the `echo 1 > /cumulus/switchd/ctrl/hash_config_reload` command to reload the configuration. This command does not cause any traffic interruptions.

The following example commands omit the source MAC address and destination MAC address from the hash calculation:

```
cumulus@switch:~$ sudo nano /etc/cumulus/datapath/traffic.conf
...
#LAG HASH config
#HASH config for LACP to enable custom fields
#Fields will be applicable for LAG hash
#calculation
#Uncomment to enable custom fields configured below
lag_hash_config.enable = true

lag_hash_config.smac = false
lag_hash_config.dmac = false
lag_hash_config.sip  = true
lag_hash_config.dip  = true
lag_hash_config.ether_type = true
lag_hash_config.vlan_id = true
lag_hash_config.sport = true
lag_hash_config.dport = true
lag_hash_config.ip_prot = true
...
```

```
cumulus@switch:~$ echo 1 > /cumulus/switchd/ctrl/hash_config_reload
```

{{%notice note%}}
Cumulus Linux enables symmetric hashing by default. Make sure that the settings for the source IP and destination IP fields match, and that the settings for the source port and destination port fields match; otherwise Cumulus Linux disables symmetric hashing automatically. If necessary, you can disable symmetric hashing manually in the `/etc/cumulus/datapath/traffic.conf` file by setting `symmetric_hash_enable = FALSE`.
{{%/notice%}}

You can also set a unique hash seed for each switch to avoid hash polarization. See {{<link url="Equal-Cost-Multipath-Load-Sharing#unique-hash-seed" text="Unique Hash Seed">}}.

## GTP Hashing

<span class="a-tooltip">[GTP](## "GPRS Tunneling Protocol")</span> carries mobile data within the core of the mobile operator’s network. Traffic in the 5G Mobility core cluster, from cell sites to compute nodes, have the same source and destination IP address. The only way to identify individual flows is with the GTP <span class="a-tooltip">[TEID](## "Tunnel Endpoint Identifier")</span>. Enabling GTP hashing adds the TEID as a hash parameter and helps the Cumulus Linux switches in the network to distribute mobile data traffic evenly across ECMP routes.

Cumulus Linux supports TEID-based load balancing for traffic egressing a bond and is only applicable if the outer header egressing the port is GTP encapsulated and if the ingress packet is either a GTP-U packet or a VXLAN encapsulated GTP-U packet.

{{%notice note%}}
- GTP Hashing is an early access feature.
- Cumulus Linux supports GTP Hashing on NVIDIA Spectrum-2 and later.
- <span class="a-tooltip">[GTP-C](## "GPRS Tunnelling Protocol Control")</span> packets are not part of GTP hashing.
- Cumulus Linux does not provide NVUE commands to configure GTP hashing.
{{%/notice%}}

To enable TEID-based load balancing:

1. Edit the `/etc/cumulus/datapath/traffic.conf` file:
   - Uncomment the `hash_config.enable = true` line.
   - Change the `lag_hash_config.gtp_teid` parameter to `true`.

   ```
   cumulus@switch:~$ sudo nano /etc/cumulus/datapath/traffic.conf
   ...
   # Uncomment to enable custom fields configured below
   hash_config.enable = true
   ...
   #GTP-U teid
   lag_hash_config.gtp_teid = true
   ```

2. Run the `echo 1 > /cumulus/switchd/ctrl/hash_config_reload` command. This command does not cause any traffic interruptions.

   ```
   cumulus@switch:~$ echo 1 > /cumulus/switchd/ctrl/hash_config_reload
   ```

To disable TEID-based load balancing, set the `lag_hash_config.gtp_teid` parameter to `false`, then reload the configuration.

{{%notice note%}}
NVUE does not provide commands to enable TEID-based load balancing.
{{%/notice%}}
-->
## Custom Hashing

The switch distributes egress traffic through a bond to a slave based on a packet hash calculation, providing load balancing over the slaves; the switch distributes conversation flows over all available slaves to load balance the total traffic. Traffic for a single conversation flow always hashes to the same slave. In a failover event, the switch adjusts the hash calculation to steer traffic over available slaves.

The hash calculation uses packet header data to choose to which slave to transmit the packet:

- For IP traffic, the switch uses IP header source and destination fields in the calculation.
- For IP and TCP or UDP traffic, the switch includes source and destination ports in the hash calculation.

For load balancing between multiple interfaces that are members of the same bond, you can hash on these fields:

| <div style="width:200px">Field  | Default Setting | NVUE Command | `traffic.conf`|
| ------- | --------------- | ------------ | --------------------------------------------- |
| IP protocol | on |`nv set system forwarding lag-hash ip-protocol on`<br><br>`nv set system forwarding lag-hash ip-protocol off`|`lag_hash_config.ip_prot`|
| Source MAC address| on |`nv set system forwarding lag-hash source-mac on`<br><br>`nv set system forwarding lag-hash source-mac off`|`lag_hash_config.smac`|
| Destination MAC address| on | `nv set system forwarding lag-hash destination-mac on`<br><br>`nv set system forwarding lag-hash destination-mac off`|`lag_hash_config.dmac`|
| Source IP address | on | `nv set system forwarding lag-hash source-ip on`<br><br>`nv set system forwarding lag-hash source-ip off`|`lag_hash_config.sip` |
| Destination IP address| on | `nv set system forwarding lag-hash destination-ip on`<br><br>`nv set system forwarding lag-hash destination-ip off`| `lag_hash_config.dip` |
| Source port | on | `nv set system forwarding lag-hash source-port on`<br><br>`nv set system forwarding lag-hash source-port off`|`lag_hash_config.sport` |
| Destination port | on | `nv set system forwarding lag-hash destination-port on`<br><br>`nv set system forwarding lag-hash destination-port off`| `lag_hash_config.dport` |
| Ethertype| on | `nv set system forwarding lag-hash ether-type on`<br><br>`nv set system forwarding lag-hash ether-type off`|`lag_hash_config.ether_type` |
| VLAN ID| on | `nv set system forwarding lag-hash vlan on`<br><br>`nv set system forwarding lag-hash vlan off`|`lag_hash_config.vlan_id` |
| TEID (see {{<link url="#gtp-hashing" text="GTP Hashing" >}})| off | `nv set system forwarding lag-hash gtp-teid on`<br><br>`nv set system forwarding lag-hash gtp-teid off`| `lag_hash_config.gtp_teid`|

The following example commands omit the source MAC address and destination MAC address from the hash calculation:

{{< tabs "TabID149 ">}}
{{< tab "NVUE Commands">}}

```
cumulus@switch:~$ nv set system forwarding lag-hash source-mac off
cumulus@switch:~$ nv set system forwarding lag-hash destination-mac off
cumulus@switch:~$ nv config apply
```

{{< /tab >}}
{{< tab "Linux Commands ">}}

{{%notice note%}}
Use the instructions below when NVUE is not enabled. If you are using NVUE to configure your switch, the NVUE commands change the settings in `/etc/cumulus/datapath/nvue_traffic.conf` which takes precedence over the settings in `/etc/cumulus/datapath/traffic.conf`.
{{%/notice%}}

1. Edit the `/etc/cumulus/datapath/traffic.conf` file:
   - Uncomment the `lag_hash_config.enable` option.
   - Set the `lag_hash_config.smac` and `lag_hash_config.dmac` options to `false`.

```
cumulus@switch:~$ sudo nano /etc/cumulus/datapath/traffic.conf
...
#LAG HASH config
#HASH config for LACP to enable custom fields
#Fields will be applicable for LAG hash
#calculation
#Uncomment to enable custom fields configured below
lag_hash_config.enable = true

lag_hash_config.smac = false
lag_hash_config.dmac = false
lag_hash_config.sip  = true
lag_hash_config.dip  = true
lag_hash_config.ether_type = true
lag_hash_config.vlan_id = true
lag_hash_config.sport = true
lag_hash_config.dport = true
lag_hash_config.ip_prot = true
#GTP-U teid
lag_hash_config.gtp_teid = false
...
```

2. Run the `echo 1 > /cumulus/switchd/ctrl/hash_config_reload` command. This command does not cause any traffic interruptions.

   ```
   cumulus@switch:~$ echo 1 > /cumulus/switchd/ctrl/hash_config_reload
   ```

{{< /tab >}}
{{< /tabs >}}

{{%notice note%}}
Cumulus Linux enables symmetric hashing by default. Make sure that the settings for the source IP and destination IP fields match, and that the settings for the source port and destination port fields match; otherwise Cumulus Linux disables symmetric hashing automatically. If necessary, you can disable symmetric hashing manually in the `/etc/cumulus/datapath/traffic.conf` file by setting `symmetric_hash_enable = FALSE`.
{{%/notice%}}

You can also set a unique hash seed for each switch to avoid hash polarization. See {{<link url="Equal-Cost-Multipath-Load-Sharing#unique-hash-seed" text="Unique Hash Seed">}}.

## GTP Hashing

<span class="a-tooltip">[GTP](## "GPRS Tunneling Protocol")</span> carries mobile data within the core of the mobile operator’s network. Traffic in the 5G Mobility core cluster, from cell sites to compute nodes, have the same source and destination IP address. The only way to identify individual flows is with the GTP <span class="a-tooltip">[TEID](## "Tunnel Endpoint Identifier")</span>. Enabling GTP hashing adds the TEID as a hash parameter and helps the Cumulus Linux switches in the network to distribute mobile data traffic evenly across ECMP routes.

Cumulus Linux supports TEID-based *load balancing* for traffic egressing a bond and is only applicable if the outer header egressing the port is GTP encapsulated and if the ingress packet is either a GTP-U packet or a VXLAN encapsulated GTP-U packet.

{{%notice note%}}
- Cumulus Linux supports GTP Hashing on NVIDIA Spectrum-2 and later.
- [GTP-C](## "GPRS Tunnelling Protocol Control") packets are not part of GTP hashing.
{{%/notice%}}

To enable TEID-based load balancing:

{{< tabs "TabID256 ">}}
{{< tab "NVUE Commands">}}

```
cumulus@switch:~$ nv set system forwarding lag-hash gtp-teid on
cumulus@switch:~$ nv config apply
```

To disable TEID-based load balancing, run the `nv set system forwarding lag-hash gtp-teid off` command.

{{< /tab >}}
{{< tab "Linux Commands ">}}

{{%notice note%}}
Use the instructions below when NVUE is not enabled. If you are using NVUE to configure your switch, the NVUE commands change the settings in `/etc/cumulus/datapath/nvue_traffic.conf` which takes precedence over the settings in `/etc/cumulus/datapath/traffic.conf`.
{{%/notice%}}

1. Edit the `/etc/cumulus/datapath/traffic.conf` file:
   - Uncomment the `hash_config.enable = true` line.
   - Change the `lag_hash_config.gtp_teid` parameter to `true`.

   ```
   cumulus@switch:~$ sudo nano /etc/cumulus/datapath/traffic.conf
   ...
   # Uncomment to enable custom fields configured below
   hash_config.enable = true
   ...
   #GTP-U teid
   lag_hash_config.gtp_teid = true
   ```

2. Run the `echo 1 > /cumulus/switchd/ctrl/hash_config_reload` command. This command does not cause any traffic interruptions.

   ```
   cumulus@switch:~$ echo 1 > /cumulus/switchd/ctrl/hash_config_reload
   ```

To disable TEID-based load balancing, set the `lag_hash_config.gtp_teid` parameter to `false`, then reload the configuration.

{{< /tab >}}
{{< /tabs >}}

## Troubleshooting

To show information for a bond, run the NVUE `nv show interface <bond> bond` command:

```
cumulus@leaf01:mgmt:~$ nv show interface bond1 bond
             operational  applied  description
-----------  -----------  -------  ------------------------------------------------------
down-delay   0            0        bond down delay
lacp-bypass  on           on       lacp bypass
lacp-rate    fast         fast     lacp rate
mode                      lacp     bond mode
up-delay     0            0        bond up delay
[member]     swp1         swp1     Set of bond members
mlag
  enable                  on       Turn the feature 'on' or 'off'.  The default is 'off'.
  id         1            1        MLAG id
  status     single                Mlag Interface status
```

You can also run the Linux `sudo cat /proc/net/bonding/<bond>` command:

```
cumulus@leaf01:mgmt:~$ sudo cat /proc/net/bonding/bond1
...
Bonding Mode: IEEE 802.3ad Dynamic link aggregation
Transmit Hash Policy: layer3+4 (1)
MII Status: up
MII Polling Interval (ms): 100
Up Delay (ms): 0
Down Delay (ms): 0

802.3ad info
LACP rate: fast
Min links: 1
Aggregator selection policy (ad_select): stable
System priority: 65535
System MAC address: 44:38:39:be:ef:aa
Active Aggregator Info:
	Aggregator ID: 1
	Number of ports: 1
	Actor Key: 9
	Partner Key: 1
	Partner Mac Address: 00:00:00:00:00:00

Slave Interface: swp1
MII Status: up
Speed: 1000 Mbps
Duplex: full
Link Failure Count: 0
Permanent HW addr: 44:38:39:00:00:37
Slave queue ID: 0
Aggregator ID: 1
Actor Churn State: none
Partner Churn State: churned
Actor Churned Count: 1
Partner Churned Count: 2
...
```

To show specific bond information, use the `nv show interface <bond> <option>` commands:

```
cumulus@switch:~$ nv show interface bond1 TAB
acl        bridge     ip         lldp       ptp        router     
bond       evpn       link       pluggable  qos
cumulus@leaf02:mgmt:~$ nv show interface bond1 link
                       operational        applied  description
---------------------  -----------------  -------  ----------------------------------------------------------------------
auto-negotiate         off                on       Link speed and characteristic auto negotiation
duplex                 full               full     Link duplex
fec                                       auto     Link forward error correction mechanism
mtu                    9000               9000     interface mtu
speed                  1G                 auto     Link speed
dot1x
  mab                                     off      bypass MAC authentication
  parking-vlan                            off      VLAN for unauthorized MAC addresses
state                  up                 up       The state of the interface
stats
  carrier-transitions  1                           Number of times the interface state has transitioned between up and...
  in-bytes             0 Bytes                     total number of bytes received on the interface
  in-drops             0                           number of received packets dropped
  in-errors            0                           number of received packets with errors
  in-pkts              0                           total number of packets received on the interface
  out-bytes            3.65 MB                     total number of bytes transmitted out of the interface
  out-drops            0                           The number of outbound packets that were chosen to be discarded eve...
  out-errors           0                           The number of outbound packets that could not be transmitted becaus...
  out-pkts             51949                       total number of packets transmitted out of the interface
mac                    44:38:39:00:00:37           MAC Address on an interface
```

## Related Information

- {{<exlink url="http://www.ieee802.org/3/ad/" text="802.3ad">}} ({{<exlink url="http://cs.uccs.edu/%7Escold/doc/linkage%20aggregation.pdf" text="Accessible writeup">}})
- {{<exlink url="http://en.wikipedia.org/wiki/Link_aggregation" text="Wikipedia - Link aggregation">}}
