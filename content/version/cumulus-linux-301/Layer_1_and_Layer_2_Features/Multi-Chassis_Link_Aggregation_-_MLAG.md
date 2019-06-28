---
title: Multi-Chassis Link Aggregation - MLAG
author: Cumulus Networks
weight: 107
aliases:
 - /display/CL30/Multi-Chassis+Link+Aggregation+-+MLAG
 - /pages/viewpage.action?pageId=5118344
pageID: 5118344
product: Cumulus Linux
version: '3.0'
imgData: cumulus-linux-301
siteSlug: cumulus-linux-301
---
Multi-Chassis Link Aggregation, or MLAG, enables a server or switch with
a two-port bond (such as a link aggregation group/LAG, EtherChannel,
port group, or trunk) to connect those ports to different switches and
operate as if they are connected to a single, logical switch. This
provides greater redundancy and greater system throughput.

Dual-connected devices can create LACP bonds that contain links to each
physical switch. Thus, active-active links from the dual-connected
devices are supported even though they are connected to two different
physical switches.

A basic setup looks like this:

{{% imgOld 0 %}}

The two switches, S1 and S2, known as *peer switches*, cooperate so that
they appear as a single device to host H1's bond. H1 distributes traffic
between the two links to S1 and S2 in any manner that you configure on
the host. Similarly, traffic inbound to H1 can traverse S1 or S2 and
arrive at H1.

## <span id="src-5118344_Multi-ChassisLinkAggregation-MLAG-reqs" class="confluence-anchor-link"></span><span>MLAG Requirements</span>

MLAG has these requirements:

  - There must be a direct connection between the two peer switches
    implementing MLAG (S1 and S2). This is typically a bond for
    increased reliability and bandwidth.

  - There must be only two peer switches in one MLAG configuration, but
    you can have multiple configurations in a network for
    *switch-to-switch MLAG* (see below).

  - The peer switches implementing MLAG must be running Cumulus Linux
    version 2.5 or later.

  - You must specify a unique `clag-id` for every dual-connected bond on
    each peer switch; the value must be between 1 and 65535 and must be
    the same on both peer switches in order for the bond to be
    considered *dual-connected*.

  - The dual-connected devices (hosts or switches) must use LACP (IEEE
    802.3ad/802.1ax) to form the bond. The peer switches must also use
    LACP.

More elaborate configurations are also possible. The number of links
between the host and the switches can be greater than two, and does not
have to be symmetrical:

{{% imgOld 1 %}}

Additionally, since S1 and S2 appear as a single switch to other bonding
devices, pairs of MLAG switches can also be connected to each other in a
switch-to-switch MLAG setup:

{{% imgOld 2 %}}

In this case, L1 and L2 are also MLAG peer switches, and thus present a
two-port bond from a single logical system to S1 and S2. S1 and S2 do
the same as far as L1 and L2 are concerned. For a switch-to-switch MLAG
configuration, each switch pair must have a unique system MAC address.
In the above example, switches L1 and L2 each have the same system MAC
address configured. Switch pair S1 and S2 each have the same system MAC
address configured; however, it is a different system MAC address than
the one used by the switch pair L1 and L2.

## <span>LACP and Dual-Connectedness</span>

In order for MLAG to operate correctly, the peer switches must know
which links are *dual-connected*, or are connected to the same host or
switch. To do this, specify a `clag-id` for every dual-connected bond on
each peer switch; the `clag-id` must be the same for the corresponding
bonds on both peer switches. [Link Aggregation Control Protocol
(LACP)](http://en.wikipedia.org/wiki/Link_Aggregation_Control_Protocol#Link_Aggregation_Control_Protocol),
the IEEE standard protocol for managing bonds, is used for verifying
dual-connectedness. LACP runs on the dual-connected device and on each
of the peer switches. On the dual-connected device, the only
configuration requirement is to create a bond that will be managed by
LACP.

On each of the peer switches the links connected to the dual-connected
host or switch must be placed in the bond. This is true even if the
links are a single port on each peer switch, where each port is placed
into a bond, as shown below:

{{% imgOld 3 %}}

All of the dual-connected bonds on the peer switches have their system
ID set to the MLAG system ID. Therefore, from the point of view of the
hosts, each of the links in its bond is connected to the same system,
and so the host will use both links.

Each peer switch periodically makes a list of the LACP partner MAC
addresses of all of their bonds and sends that list to its peer (using
the `clagd` service; see below). The LACP partner MAC address is the MAC
address of the system at the other end of a bond, which in the figure
above would be hosts H1, H2 and H3. When a switch receives this list
from its peer, it compares the list to the LACP partner MAC addresses on
its switch. If any matches are found and the `clag-id` for those bonds
match, then that bond is a dual-connected bond. You can also find the
LACP partner MAC address in the
`/sys/class/net/<bondname>/bonding/ad_partner_mac sysfs` file for each
bond.

## <span id="src-5118344_Multi-ChassisLinkAggregation-MLAG-roles" class="confluence-anchor-link"></span><span>Understanding Switch Roles</span>

Each MLAG-enabled switch in the pair has a role. When the peering
relationship is established between the two switches, one switch will be
in *primary* role, and the other one will be in *secondary* role. When
an MLAG-enabled switch is in the secondary role, it does not send STP
BPDUs on dual-connected links; it only sends BPDUs on single-connected
links. The switch in the primary role sends STP BPDUs on all single- and
dual-connected links.

| Send BPDUs             | Primary | Secondary |
| ---------------------- | ------- | --------- |
| Single-connected links | Yes     | Yes       |
| Dual-connected links   | Yes     | No        |

By default, the role is determined by comparing the MAC addresses of the
two sides of the peering link; the switch with the lower MAC address
assumes the primary role. You can override this by setting the priority
configuration, either by specifying the `clagd-priority` option in
`/etc/network/interfaces`, or by using `clagctl`. The switch with the
lower priority value is given the primary role; the default value is
32768, and the range is 0 to 65535. Read the `clagd(8)` and `clagctl(8)`
man pages for more information.

When the `clagd` service is exited during switch reboot or the service
is stopped in the primary switch, the peer switch that is in the
secondary role will become primary. If the primary switch goes down
without stopping the `clagd` service for any reason or the peer link
goes down, the secondary switch will **not** change its role. In case
the peer switch is determined to be not alive, the switch in the
secondary role will roll back the LACP system ID to be the bond
interface MAC address instead of the `clagd-sys-mac` and the switch in
primary role uses the `clagd-sys-mac` as the LACP system ID on the
bonds.

## <span id="src-5118344_Multi-ChassisLinkAggregation-MLAG-configuring" class="confluence-anchor-link"></span><span>Configuring MLAG</span>

Configuring MLAG involves:

  - On the dual-connected devices, create a bond that uses LACP.

  - On each peer switch, configure the interfaces, including bonds,
    VLANs, bridges and peer links.

{{%notice note%}}

MLAG synchronizes the dynamic state between the two peer switches, but
it does not synchronize the switch configurations. After modifying the
configuration of one peer switch, you must make the same changes to the
configuration on the other peer switch. This applies to all
configuration changes, including:

  - Port configuration: For example, VLAN membership,
    [MTU](#src-5118344_Multi-ChassisLinkAggregation-MLAG-mtu), and
    bonding parameters.

  - Bridge configuration: For example, spanning tree parameters or
    bridge properties.

  - Static address entries: For example, static FDB entries and static
    IGMP entries.

  - QoS configuration: For example, ACL entries.

You can verify the configuration of VLAN membership using the `clagctl
-v verifyvlans` command.

{{%/notice%}}

### <span>Reserved MAC Address Range</span>

In order to prevent MAC address conflicts with other interfaces in the
same bridged network, Cumulus Networks has [reserved a range of MAC
addresses](https://support.cumulusnetworks.com/hc/en-us/articles/203837076)
specifically to use with MLAG. This range of MAC addresses is
44:38:39:ff:00:00 to 44:38:39:ff:ff:ff.

Cumulus Networks recommends you use this range of MAC addresses when
configuring MLAG.

### <span>Configuring the Host or Switch</span>

On your dual-connected device, create a bond that uses LACP. The method
you use varies with the type of device you are configuring. The
following image is a basic MLAG configuration, showing all the essential
elements; a more detailed two-leaf/two-spine configuration is
[below](#src-5118344_Multi-ChassisLinkAggregation-MLAG-exampl).

{{% imgOld 4 %}}

### <span>Configuring the Interfaces</span>

Every interface that connects to the MLAG pair from a dual-connected
device should be placed into a
[bond](/version/cumulus-linux-301/Layer_1_and_Layer_2_Features/Bonding_-_Link_Aggregation),
even if the bond contains only a single link on a single physical switch
(since the MLAG pair contains two or more links). Layer 2 data travels
over this bond. In the examples throughout this chapter, *peerlink* is
the name of the bond.

Single-attached hosts, also known as *orphan ports*, can be just a
member of the bridge.

Additionally, the fast mode of LACP should be configured on the bond to
allow more timely updates of the LACP state. These bonds will then be
placed in a bridge, which will include the peer link between the
switches.

In order to enable communication between the `clagd` services on the
peer switches, you should choose an unused VLAN (also known as a
*switched virtual interface* or *SVI* here) and assign an unrouteable
link-local address to give the peer switches layer 3 connectivity
between each other. To ensure that the VLAN is completely independent of
the bridge and spanning tree forwarding decisions, configure the VLAN as
a VLAN subinterface on the peer link bond rather than the VLAN-aware
bridge. Cumulus Networks recommends you use 4094 for the peer link VLAN
(*peerlink.4094* below) if possible. In addition, to avoid issues with
STP, make sure you include untagged traffic on the peer link.

You can also specify a backup interface, which is any layer 3 backup
interface for your peer links in the event that the peer link goes down.
[See below](#src-5118344_Multi-ChassisLinkAggregation-MLAG-backup) for
more information about the backup link.

For example, if peerlink is the inter-chassis bond, and VLAN 4094 is the
peer link VLAN, configure peerlink.4094 using:

    auto peerlink.4094
    iface peerlink.4094
      address 169.254.1.1/30
      clagd-peer-ip 169.254.1.2
      clagd-backup-ip 192.0.2.50
      clagd-sys-mac 44:38:39:FF:40:94

Then run `ifup` on the peer link VLAN interface. In this example, the
command would be `sudo ifup peerlink.4094`.

There is no need to add VLAN 4094 to the bridge VLAN list, as it is
unnecessary there.

{{%notice note%}}

Keep in mind that when you change the MLAG configuration in the
`interfaces` file, the changes take effect when you bring the peer link
interface up with `ifup`. Do **not** use `systemctl restart
clagd.service` to apply the new configuration.

{{%/notice%}}

{{%notice warning%}}

Do not use 169.254.0.1 as the MLAG peerlink IP address, as Cumulus Linux
uses this address exclusively for [BGP
unnumbered](Border_Gateway_Protocol_-_BGP.html#src-5118393_BorderGatewayProtocol-BGP-unnumbered)
interfaces.

{{%/notice%}}

### <span id="src-5118344_Multi-ChassisLinkAggregation-MLAG-example" class="confluence-anchor-link"></span><span>Example MLAG Configuration</span>

An example configuration is included below. It configures two bonds for
MLAG, each with a single port, a peer link that is a bond with two
member ports, and three VLANs on each port. You store the configuration
in `/etc/network/interfaces` on each peer switch.

{{% imgOld 5 %}}

Configuring these interfaces uses syntax from ` ifupdown2  `and the
[VLAN-aware bridge driver
mode](/version/cumulus-linux-301/Layer_1_and_Layer_2_Features/Ethernet_Bridging_-_VLANs/VLAN-aware_Bridge_Mode_for_Large-scale_Layer_2_Environments).
The bridges use these Cumulus Linux-specific keywords:

  - `bridge-vids`, which defines the allowed list of tagged 802.1q VLAN
    IDs for all bridge member interfaces. You can specify non-contiguous
    ranges with a space-separated list, like  
    `bridge-vids 100-200 300 400-500`.

  - `bridge-pvid`, which defines the untagged VLAN ID for each port.
    This is commonly referred to as the *native VLAN*.

The bridge configurations below indicate that each bond carries tagged
frames on VLANs 1000 to 3000 but untagged frames on VLAN 1. Also, take
note on how you configure the VLAN subinterface used for `clagd`
communication (*peerlink.4094* in the sample configuration below).

{{%notice note%}}

At minimum, this VLAN subinterface should not be in your Layer 2 domain,
and you should give it a very high VLAN ID (up to 4094). Read more about
the [range of VLAN IDs you can
use](VLAN-aware_Bridge_Mode_for_Large-scale_Layer_2_Environments.html#src-5118287_VLAN-awareBridgeModeforLarge-scaleLayer2Environments-range).

{{%/notice%}}

The configuration for the spines should look like the following (note
that the `clag-id` and `clagd-sys-mac` must be the same for the
corresponding bonds on spine1 and spine2):

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>spine1</p>
<pre><code> 
# The loopback network interface auto lo
iface lo 
inet loopback
 
# The primary network interface 
auto eth0
iface eth0
    address 10.0.0.1 
    netmask 255.255.255.0
        
auto peerlink 
iface peerlink
    bond-slaves swp31 swp32 
        
auto peerlink.4094 
iface peerlink.4094
    address 169.254.255.1 
    netmask 255.255.255.0      
    clagd-priority 4096
    clagd-peer-ip 169.254.255.2
    clagd-backup-ip 10.0.0.2
    clagd-sys-mac 44:38:39:ff:00:01
 
  
# ToR pair #1 
auto downlink1 
iface downlink1
    bond-slaves swp29 swp30 
    clag-id 1
        
# ToR pair #2 
auto downlink2 
iface downlink2
    bond-slaves swp27 swp28 
    clag-id 2
        
auto br0
iface br0
    bridge-vlan-aware yes
    bridge-ports uplinkA peerlink downlink1 downlink2 
    bridge-stp on
    bridge-vids 1000-2999
    bridge-pvid 1
    mstpctl-treeprio 4096</code></pre></td>
<td><p>spine2</p>
<pre><code> 
# The loopback network interface auto lo
iface lo 
inet loopback
 
# The primary network interface 
auto eth0
iface eth0
    address 10.0.0.2 
    netmask 255.255.255.0
        
auto peerlink 
iface peerlink
    bond-slaves swp31 swp32 
        
auto peerlink.4094 
iface peerlink.4094
    address 169.254.255.2 
    netmask 255.255.255.0      
    clagd-priority 8192
    clagd-peer-ip 169.254.255.1
    clagd-backup-ip 10.0.0.1
    clagd-sys-mac 44:38:39:ff:00:01
 
  
# ToR pair #1 
auto downlink1 
iface downlink1
    bond-slaves swp29 swp30 
    clag-id 1
        
# ToR pair #2 
auto downlink2 
iface downlink2
    bond-slaves swp27 swp28 
    clag-id 2
        
auto br0
iface br0
    bridge-vlan-aware yes
    bridge-ports uplinkA peerlink downlink1 downlink2 
    bridge-stp on
    bridge-vids 1000-2999
    bridge-pvid 1
    mstpctl-treeprio 4096</code></pre></td>
</tr>
</tbody>
</table>

Here is an example configuration file for the switches leaf1 and leaf2.
Note that the `clag-id` and `clagd-sys-mac` must be the same for the
corresponding bonds on leaf1 and leaf2:

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>leaf1</p>
<pre><code>        
# The loopback network interface
auto lo
iface lo inet loopback
        
# The primary network interface
auto eth0
iface eth0
    address 10.0.0.3
    netmask 255.255.255.0
        
auto spine1-2
iface spine1-2
    bond-slaves swp49 swp50
    clag-id 1
        
auto peerlink
iface peerlink
    bond-slaves swp51 swp52
        
auto peerlink.4094
iface peerlink.4094
    address 169.254.255.3
    netmask 255.255.255.0
    clagd-priority 4096
    clagd-peer-ip 169.254.255.4
    clagd-backup-ip 10.0.0.4
    clagd-sys-mac 44:38:39:ff:01:02
  
auto host1
iface host1
    bond-slaves swp1
    clag-id 2
    mstpctl-portadminedge yes
    mstpctl-bpduguard yes
  
auto host2
iface host2
    bond-slaves swp2
    clag-id 3
    mstpctl-portadminedge yes
    mstpctl-bpduguard yes
 
 
auto br0
iface br0
    bridge-vlan-aware yes
    bridge-ports spine1-2 peerlink host1 host2
    bridge-stp on
    bridge-vids 1000-2999
    bridge-pvid 1
    mstpctl-treeprio 8192</code></pre></td>
<td><p>leaf2</p>
<pre><code>        
# The loopback network interface
auto lo
iface lo inet loopback
        
# The primary network interface
auto eth0
iface eth0
    address 10.0.0.4
    netmask 255.255.255.0
        
auto spine1-2
iface spine1-2
    bond-slaves swp49 swp50
    clag-id 1
        
auto peerlink
iface peerlink
    bond-slaves swp51 swp52
        
auto peerlink.4094
iface peerlink.4094
    address 169.254.255.4
    netmask 255.255.255.0
    clagd-priority 8192
    clagd-peer-ip 169.254.255.3
    clagd-backup-ip 10.0.0.3
    clagd-sys-mac 44:38:39:ff:01:02
  
auto host1
iface host1
    bond-slaves swp1
    clag-id 2
    mstpctl-portadminedge yes
    mstpctl-bpduguard yes
  
auto host2
iface host2
    bond-slaves swp2
    clag-id 3
    mstpctl-portadminedge yes
    mstpctl-bpduguard yes
 
 
auto br0
iface br0
    bridge-vlan-aware yes
    bridge-ports spine1-2 peerlink host1 host2
    bridge-stp on
    bridge-vids 1000-2999
    bridge-pvid 1
    mstpctl-treeprio 8192</code></pre></td>
</tr>
</tbody>
</table>

The configuration is almost identical, except for the IP addresses used
for managing the `clagd` service.

{{%notice note%}}

In the configurations above, the `clagd-peer-ip` and `clagd-sys-mac`
parameters are mandatory, while the rest are optional. When mandatory
`clagd` commands are present under a peer link subinterface, by default
`clagd-enable` is set to *yes* and doesn't need to be specified; to
disable `clagd` on the subinterface, set `clagd-enable` to *no*. Use
`clagd-priority` to set the role of the MLAG peer switch to primary or
secondary. Each peer switch in an MLAG pair must have the same
`clagd-sys-mac` setting. Each `clagd-sys-mac` setting should be unique
to each MLAG pair in the network. For more details refer to `man clagd`.

{{%/notice%}}

### <span>Configuring MLAG with a Traditional Mode Bridge</span>

It's possible to configure MLAG with a bridge in [traditional
mode](/version/cumulus-linux-301/Layer_1_and_Layer_2_Features/Ethernet_Bridging_-_VLANs/)
instead of [VLAN-aware
mode](/version/cumulus-linux-301/Layer_1_and_Layer_2_Features/Ethernet_Bridging_-_VLANs/VLAN-aware_Bridge_Mode_for_Large-scale_Layer_2_Environments).
In order to do so, the peer link and all dual-connected links must be
configured as
[untagged/native](Ethernet_Bridging_-_VLANs.html#src-5118277_EthernetBridging-VLANs-VLAN_tagging)
ports on a bridge (note the absence of any VLANs in the `bridge-ports`
line and the lack of the `bridge-vlan-aware` parameter below):

    auto br0
    iface br0
      bridge-ports peerlink spine1-2 host1 host2

{{%notice tip%}}

For a deeper comparison of traditional versus VLAN-aware bridge modes,
read this [knowledge base
article](https://support.cumulusnetworks.com/hc/en-us/articles/204909397).

{{%/notice%}}

### <span>Using the clagd Command Line Interface</span>

A command line utility called `clagctl` is available for interacting
with a running `clagd` service to get status or alter operational
behavior. For detailed explanation of the utility, please refer to the
`clagctl(8)`man page. The following is a sample output of the MLAG
operational status displayed by the utility:

    cumulus@switch$ clagctl
    The peer is alive
         Our Priority, ID, and Role: 8192 00:e0:ec:26:50:89 primary
        Peer Priority, ID, and Role: 8192 00:e0:ec:27:49:f6 secondary
              Peer Interface and IP: peerlink.4094 169.254.255.2
                         System MAC: 44:38:39:ff:00:01
     
                             Dual Attached Ports
          Our Interface      Peer Interface     CLAG Id
          ----------------   ----------------   -------
                 downlink1   downlink1          1
                 downlink2   downlink2          2

## <span id="src-5118344_Multi-ChassisLinkAggregation-MLAG-protodown" class="confluence-anchor-link"></span><span>Peer Link Interfaces and the protodown State</span>

In addition to the standard UP and DOWN administrative states, an
interface that is a member of an MLAG bond can also be in a `protodown`
state. When MLAG detects a problem that could result in connectivity
issues such as traffic black-holing or a network meltdown if the link
carrier was left in an UP state, it can put that interface into
`protodown` state. Such connectivity issues include:

  - When the peer link goes down but the peer switch is up (that is, the
    backup link is active).

  - When the bond is configured with an MLAG ID, but the `clagd` service
    is not running (whether it was deliberately stopped or simply died).

  - When an MLAG-enabled node is booted or rebooted, the MLAG bonds are
    placed in a `protodown` state until the node establishes a
    connection to its peer switch, or five minutes have elapsed.

When an interface goes into a `protodown` state, it results in a local
OPER DOWN (carrier down) on the interface. As of Cumulus Linux 2.5.5,
the `protodown` state can be manipulated with the `ip link set` command.
Given its use in preventing network meltdowns, manually manipulating
`protodown` is not recommended outside the scope of interaction with the
Cumulus Networks support team.

The following `ip link show` command output shows an interface in
`protodown` state. Notice that the link carrier is down (NO-CARRIER):

    cumulus@switch:~$ ip link show swp1
    3: swp1: <NO-CARRIER,BROADCAST,MULTICAST,SLAVE,UP> mtu 1500 qdisc pfifo_fast master host-bond1 state DOWN mode DEFAULT qlen 500 protodown on
       link/ether 44:38:39:00:69:84 brd ff:ff:ff:ff:ff:ff

### <span id="src-5118344_Multi-ChassisLinkAggregation-MLAG-backup" class="confluence-anchor-link"></span><span>Specifying a Backup Link</span>

You can specify a backup link for your peer links in the event that the
peer link goes down. When this happens, the `clagd` service uses the
backup link to check the health of the peer switch. To configure this,
edit `/etc/network/interfaces` and add ` clag-backup-ip <ADDRESS>  `to
the peer link configuration. Here's an example:

    auto peerlink.4094
    iface peerlink.4094
        address 169.254.255.1
        netmask 255.255.255.0
        clagd-priority 8192
        clagd-peer-ip 169.254.255.2
        clagd-backup-ip 192.0.2.50
        clagd-sys-mac 44:38:39:ff:00:01
        clagd-args --priority 1000

{{%notice tip%}}

The backup IP address must be different than the peer link IP address
(`clagd-peer-ip` above). It must be reachable by a route that doesn't
use the peer link and it must be in the same network namespace as the
peer link IP address.

Cumulus Networks recommends you use the switch's management IP address
for this purpose.

{{%/notice%}}

You can also specify the backup UDP port. The port defaults to 5342, but
you can configure it as an argument in `clagd-args` using `--backupPort
<PORT>`.

    auto peerlink.4094
    iface peerlink.4094
        address 169.254.255.1
        netmask 255.255.255.0
        clagd-priority 8192
        clagd-peer-ip 169.254.255.2
        clagd-backup-ip 192.0.2.50
        clagd-sys-mac 44:38:39:ff:00:01
        clagd-args --backupPort 5400

You can see the backup IP address if you run `clagctl`:

    cumulus@switch:~$ clagctl
    The peer is alive
         Our Priority, ID, and Role: 8192 00:e0:ec:26:50:89 primary
        Peer Priority, ID, and Role: 8192 00:e0:ec:27:49:f6 secondary
              Peer Interface and IP: peerlink.4094 169.254.255.2
                          Backup IP: 192.0.2.50
                         System MAC: 44:38:39:ff:00:01
     
                             Dual Attached Ports
          Our Interface      Peer Interface     CLAG Id
          ----------------   ----------------   -------
                 downlink1   downlink1          1
                 downlink2   downlink2          2 

## <span>Monitoring Dual-Connected Peers</span>

Upon receipt of a valid message from its peer, the switch knows that
`clagd` is alive and executing on that peer. This causes `clagd` to
change the system ID of each bond that was assigned a `clag-id` from the
default value (the MAC address of the bond) to the system ID assigned to
both peer switches. This makes the hosts connected to each switch act as
if they are connected to the same system so that they will use all ports
within their bond. Additionally, `clagd` determines which bonds are
dual-connected and modifies the forwarding and learning behavior to
accommodate these dual-connected bonds.

If the peer does not receive any messages for three update intervals,
then that peer switch is assumed to no longer be acting as an MLAG peer.
In this case, the switch reverts all configuration changes so that it
operates as a standard non-MLAG switch. This includes removing all
statically assigned MAC addresses, clearing the egress forwarding mask,
and allowing addresses to move from any port to the peer port. Once a
message is again received from the peer, MLAG operation starts again as
described earlier. You can configure a custom timeout setting by adding
`--peerTimeout <VALUE>` to `clagd-args` in `/etc/network/interfaces`.

Once bonds are identified as dual-connected, `clagd` sends more
information to the peer switch for those bonds. The MAC addresses (and
VLANs) that have been dynamically learned on those ports are sent along
with the LACP partner MAC address for each bond. When a switch receives
MAC address information from its peer, it adds MAC address entries on
the corresponding ports. As the switch learns and ages out MAC
addresses, it informs the peer switch of these changes to its MAC
address table so that the peer can keep its table synchronized.
Periodically, at 45% of the bridge ageing time, a switch will send its
entire MAC address table to the peer, so that peer switch can verify
that its MAC address table is properly synchronized.

The switch sends an update frequency value in the messages to its peer,
which tells `clagd` how often the peer will send these messages. You can
configure a different frequency by adding `--lacpPoll <SECONDS>` to
`clagd-args` in `/etc/network/interfaces`.

## <span>Configuring Layer 3 Routed Uplinks</span>

In this scenario, the spine switches connect at layer 3, as shown in the
image below. Alternatively, the spine switches can be singly connected
to each core switch at layer 3 (not shown below).

{{% imgOld 6 %}}

In this design, the spine switches route traffic between the server
hosts in the layer 2 domains and the core. The servers (host1 - host4)
each have a layer 2 connection up to the spine layer where the default
gateway for the host subnets resides. However, since the spine switches
as gateway devices communicate at layer 3, you need to configure a
protocol such as
[VRR](/version/cumulus-linux-301/Layer_1_and_Layer_2_Features/Virtual_Router_Redundancy_-_VRR)
(Virtual Router Redundancy) between the spine switch pair to support
active/active forwarding.

Then, to connect the spine switches to the core switches, you need to
determine whether the routing is static or dynamic. If it's dynamic, you
must choose which protocol —
[OSPF](/version/cumulus-linux-301/Layer_3_Features/Open_Shortest_Path_First_-_OSPF_-_Protocol)
or
[BGP](/version/cumulus-linux-301/Layer_3_Features/Border_Gateway_Protocol_-_BGP)
— to use. When enabling a routing protocol in an MLAG environment it is
also necessary to manage the uplinks, because by default MLAG is not
aware of layer 3 uplink interfaces. In the event of a peer link failure
MLAG does not remove static routes or bring down a BGP or OSPF adjacency
unless a separate link state daemon such as ` ifplugd  `is used.

## <span>IGMP Snooping with MLAG</span>

IGMP snooping processes IGMP reports received on a bridge port in a
bridge to identify hosts that are configured to receive multicast
traffic destined to that group. An IGMP query message received on a port
is used to identify the port that is connected to a router and
configured to receive multicast traffic.

IGMP snooping is enabled by default on the bridge. IGMP snooping
multicast database entries and router port entries are synced to the
peer MLAG switch. If there is no multicast router in the VLAN, the IGMP
querier can be configured on the switch to generate IGMP query messages
by adding a configuration like the following to
`/etc/network/interfaces`:

    auto br.100
    vlan br.100
        #igmp snooping is enabled by default, but is shown here for completeness
        bridge-mcsnoop 1
        # If you need to specify the querier IP address
        bridge-igmp-querier-source 123.1.1.1

To display multicast group and router port information, use the `bridge
-d mdb show` command:

    cumulus@switch:~# sudo bridge -d mdb show
    dev br port bond0 vlan 100 grp 234.1.1.1 temp
    router ports on br: bond0

Runtime Configuration (Advanced)

{{%notice warning%}}

A runtime configuration is non-persistent, which means the configuration
you create here does not persist after you reboot the switch.

{{%/notice%}}

    cumulus@switch:~# sudo brctl setmcqv4src br 100 192.0.2.1
    cumulus@switch:~# sudo brctl setmcquerier br 1
    cumulus@switch:~# sudo brctl showmcqv4src br
     
            
    vlan            querier address
    100             192.0.2.1

## <span>Monitoring the Status of the clagd Service</span>

Due to the critical nature of the `clagd` service, `systemd`
continuously monitors the status of `clagd`. `systemd` monitors the
`clagd` service through the use of notify messages every 30 seconds. If
the `clagd` service dies or becomes unresponsive for any reason and
`systemd` receives no messages after 60 seconds, `systemd` restarts
`clagd`. `systemd` logs these failures in `/var/log/syslog`, and, on the
first failure, generates a ` cl-support  `file as well.

This monitoring is automatically configured and enabled as long as
`clagd` is enabled (that is, `clagd-peer-ip` and `clagd-sys-mac` are
configured in `/etc/network/interfaces`) and `clagd` been started. When
`clagd` is explicitly stopped, for example with the `systemctl stop
clagd.service` command, monitoring of `clagd` is also stopped.

You can check the status of `clagd` monitoring by using the
`cl-service-summary` command:

    cumulus@switch:~$ sudo cl-service-summary summary
    The systemctl daemon 5.4 uptime: 15m
    ...
    Service clagd        enabled    active 
    ...

## <span>MLAG Best Practices</span>

For MLAG to function properly, the dual-connected hosts' interfaces
should be configured identically on the pair of peering switches. See
the note above in the [Configuring
MLAG](#src-5118344_Multi-ChassisLinkAggregation-MLAG-configuring)
section.

### <span id="src-5118344_Multi-ChassisLinkAggregation-MLAG-mtu" class="confluence-anchor-link"></span><span> Understanding MTU in an MLAG Configuration</span>

Note that the
[MTU](Layer_1_and_Switch_Port_Attributes.html#src-5118373_Layer1andSwitchPortAttributes-mtu)
in MLAG traffic is determined by the bridge MTU. Bridge MTU is
determined by the lowest MTU setting of an interface that is a member of
the bridge. If an MTU other than the default of 1500 bytes is desired,
you must configure the MTU on each physical interface and bond interface
that are members of the MLAG bridges in the entire bridged domain.

For example, if an MTU of 9216 is desired through the MLAG domain in the
example shown above:

On the the leaf switches, [configure
`mtu 9216`](Layer_1_and_Switch_Port_Attributes.html#src-5118373_Layer1andSwitchPortAttributes-mtu)
for each of following interfaces, since they are members of bridge
*br0*: spine1-2, peerlink, host1, host2.

    auto br0
    iface br0
       bridge-vlan-aware yes
       bridge-ports spine1-2 peerlink host1 host2   <- List of bridge member interfaces
       ...

Likewise, to ensure the MTU 9216 path is respected through the spine
switches above, also change the MTU setting for bridge *br* by
configuring `mtu 9216` for each of the following members of bridge *br*
on spine1 and spine2: uplinkA, peerlink, downlink1, downlink2.

    auto br
    iface br
        bridge-vlan-aware yes
        bridge-ports uplinkA peerlink downlink1 downlink2 
        ...

### <span>Sizing the Peerlink</span>

What's the best size for a peerlink? Before we answer that, let's talk a
little bit about the peerlink itself.

The peerlink tends to carry very little traffic when compared to the
bandwidth consumed by dataplane traffic. In a typical MLAG
configuration, most every connection between the two switches in the
MLAG pair is dual-connected, so the only traffic going across the
peerlink is traffic from the `clagd` process and some LLDP or LACP
traffic. However, there are some instances where a host is connected to
only one switch in the MLAG pair; these include:

  - You have a hardware limitation on the host where there is only one
    PCIE slot, and thus, one NIC on the system, so the host is only
    single-connected across that interface.

  - The host doesn't support 802.3ad and you can't create a bond on it.

  - You are accounting for a link failure, where the host may become
    single connected until the failure is rectified.

So, in terms of sizing the peerlink, in general, you need to determine
how much bandwidth is traveling across the single-connected interfaces,
and allocate half of that bandwidth to the peerlink. We recommend half
of the single-connected bandwidth because, on average, one half of the
traffic destined to the single-connected host will arrive on the switch
directly connected to the single-connected host and the other half will
arrive on the switch that is not directly connected to the
single-connected host. When this happens, only the traffic that arrives
on the switch that is not directly connected to the single-connected
host needs to traverse the peerlink, which is how you calculate 50% of
the traffic.

In addition, you may want to add extra links to the peerlink bond to
handle link failures in the peerlink bond itself.

In illustration below, each host has 2 10G links, with each 10G link
going to each switch in the MLAG pair. Each host has 20G of
dual-connected bandwidth, so all three hosts have a total of 60G of
dual-connected bandwidth. We recommend you allocate at least 15G of
bandwidth to each peerlink bond, which represents half of the
single-connected bandwidth.

{{% imgOld 7 %}}

Scaling this example out to a full rack, when planning for link
failures, you need only allocate enough bandwidth to meet your site's
strategy for handling failure scenarios. Imagine a full rack with 40
servers and two switches in it. You may plan for, say, 4 to 6 servers to
lose connectivity to a single switch and become single connected before
you respond to the event. So expanding upon our previous example, if you
have 40 hosts each with 20G of bandwidth dual-connected to the MLAG
pair, you might allocate 20G to 30G of bandwidth to the peerlink — which
accounts for half of the single-connected bandwidth for 4 to 6 hosts.

## <span>STP Interoperability with MLAG</span>

Cumulus Networks recommends that you always enable STP in your layer 2
network.

Further, with MLAG, Cumulus Networks recommends you enable BPDU guard on
the host-facing bond interfaces. (For more information about BPDU guard,
see [BPDU Guard and Bridge
Assurance](Spanning_Tree_and_Rapid_Spanning_Tree.html#src-5118355_SpanningTreeandRapidSpanningTree-bpdu).)

### <span>Debugging STP with MLAG</span>

`/var/log/daemon.log` has `mstpd` logs.

Run `mstpctl debuglevel 3` to see MLAG-related logs in
`/var/log/daemon.log`:

    cumulus@switch:~$ sudo mstpctl showportdetail br peer-bond
    br:peer-bond CIST info
      enabled            yes                     role                 Designated
      port id            8.008                   state                forwarding
      ...............
      bpdufilter port    no                     
      clag ISL           yes                     clag ISL Oper UP     yes
      clag role          primary                 clag dual conn mac   0:0:0:0:0:0
      clag remote portID F.FFF                   clag system mac      44:38:39:ff:0:1
    cumulus@switch:~$ 
     
    cumulus@switch:~$ sudo mstpctl showportdetail br downlink-1
    br:downlink-1 CIST info
      enabled            yes                     role                 Designated
      port id            8.006                   state                forwarding
      ..............
      bpdufilter port    no                     
      clag ISL           no                      clag ISL Oper UP     no
      clag role          primary                 clag dual conn mac   0:0:0:3:11:1
      clag remote portID F.FFF                   clag system mac      44:38:39:ff:0:1
    cumulus@switch:~$

### <span>Best Practices for STP with MLAG</span>

  - The STP global configuration must be the same on both the switches.

  - The STP configuration for dual-connected ports should be the same on
    both peer switches.

  - Use `mstpctl` commands for all spanning tree configurations,
    including bridge priority, path cost and so forth. Do not use
    `brctl` commands for spanning tree, except for `brctl stp on/off`,
    as changes are not reflected to `mstpd` and can create conflicts.

## <span>Troubleshooting MLAG</span>

By default, when `clagd` is running, it logs its status to the
`/var/log/clagd.log` file and syslog. Example log file output is below:

    Jan 14 23:45:10 switch clagd[3704]: Beginning execution of clagd version 1.0.0
    Jan 14 23:45:10 switch clagd[3704]: Invoked with: /usr/sbin/clagd --daemon 169.254.2.2 peer-bond.4000 44:38:39:ff:00:01 --priority 8192
    Jan 14 23:45:11 switch clagd[3995]: Role is now secondary
    Jan 14 23:45:31 switch clagd[3995]: Role is now primary
    Jan 14 23:45:32 switch clagd[3995]: The peer switch is active.
    Jan 14 23:45:35 switch clagd[3995]: downlink-1 is now dual connected.

## <span>Caveats and Errata</span>

If both the backup and peer connectivity are lost within a 30-second
window, the switch in the secondary role misinterprets the event
sequence, believing the peer switch is down, so it takes over as the
primary.

## <span>Configuration Files</span>

  - /etc/network/interfaces
