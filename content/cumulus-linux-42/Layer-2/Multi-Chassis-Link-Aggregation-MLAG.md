---
title: Multi-Chassis Link Aggregation - MLAG
author: Cumulus Networks
weight: 480
toc: 3
---
{{%notice info%}}

**MLAG or CLAG**: The Cumulus Linux implementation of MLAG is referred to by other vendors as CLAG, MC-LAG or VPC. You will even see references to CLAG in Cumulus Linux, including the management daemon, named `clagd`, and other options in the code, such as `clag-id`, which exist for historical purposes. The Cumulus Linux implementation is truly a multi-chassis link aggregation protocol, so we call it MLAG.

{{%/notice%}}

Multi-Chassis Link Aggregation (MLAG) enables a server or switch with a two-port bond, such as a link aggregation group (LAG), EtherChannel, port group or trunk, to connect those ports to different switches and operate as if they are connected to a single, logical switch. This provides greater redundancy and greater system throughput.

Dual-connected devices can create LACP bonds that contain links to each physical switch. Therefore, active-active links from the dual-connected devices are supported even though they are connected to two different physical switches.

A basic MLAG configuration looks like this:

{{< img src = "/images/cumulus-linux/mlag-basic-setup.png" >}}

The two switches, leaf01 and leaf02, known as *peer switches*, appear as a single device to the bond on server01. server01 distributes traffic between the two links to leaf01 and leaf02 in the way you configure on the host. Traffic inbound to server01 can traverse leaf01 or leaf02 and arrive at server01.

More elaborate configurations are also possible. The number of links between the host and the switches can be greater than two and does not have to be symmetrical. Additionally, because the two peer switches appear as a single switch to other bonding devices, you can also connect pairs of MLAG switches to each other in a switch-to-switch MLAG configuration:

{{< img src = "/images/cumulus-linux/mlag-two-pair.png" >}}

In the above example, leaf01 and leaf02 are also MLAG peer switches and present a two-port bond from a single logical system to spine01 and spine02. spine01 and spine02 do the same as far as leaf01 and leaf02 are concerned. For a switch-to-switch MLAG configuration, each switch pair must have a unique system MAC address. In the example, leaf01 and leaf02 each have the same system MAC address. Switch pair spine01 and spine02 each have the same system MAC address; however, it is a different system MAC address than the one used by the switch pair leaf01 and leaf02.

## MLAG Requirements

MLAG has these requirements:

- There must be a direct connection between the two peer switches implementing MLAG. This is typically a bond for increased reliability and bandwidth.
- There must be only two peer switches in one MLAG configuration, but you can have multiple configurations in a network for *switch-to-switch MLAG*.
- You must specify a unique `clag-id` for every dual-connected bond on each peer switch; the value must be between 1 and 65535 and must be the same on both peer switches for the bond to be considered *dual-connected*.
- The dual-connected devices (servers or switches) can use LACP (IEEE 802.3ad/802.1ax) to form the {{<link url="Bonding-Link-Aggregation" text="bond">}}. In this case, the peer switches must also use LACP.
- Both switches in the MLAG pair must be running the same release of Cumulus Linux.

## LACP and Dual-connected Links

For MLAG to operate correctly, the peer switches must know which links are *dual-connected* or are connected to the same host or switch. You must specify a `clag-id` for every dual-connected bond on each peer switch; the `clag-id` must be the same for the corresponding bonds on both peer switches. Typically, {{<exlink url="http://en.wikipedia.org/wiki/Link_Aggregation_Control_Protocol#Link_Aggregation_Control_Protocol" text="Link Aggregation Control Protocol (LACP)">}}, the IEEE standard protocol for managing bonds, is used for verifying dual-connectedness. LACP runs on the dual-connected device and on each of the peer switches. On the dual-connected device, the only configuration requirement is to create a bond that is managed by LACP.

However, if you cannot use LACP in your environment, you can configure the bonds in {{<link url="Bonding-Link-Aggregation" text="balance-xor mode">}}. When using balance-xor mode to dual-connect host-facing bonds in an MLAG environment, you must configure the `clag-id` parameter on the MLAG bonds, which must be the same on both MLAG switches. Otherwise, the bonds are treated by the MLAG switch pair as if they are single-connected. Dual-connectedness is solely determined by matching `clag-id` and any misconnection is **not** detected.

On each of the peer switches, you must place the links that are connected to the dual-connected host or switch in the bond. This is true even if the links are a single port on each peer switch, where each port is placed into a bond, as shown below:

{{< img src = "/images/cumulus-linux/mlag-dual-connect.png" >}}

All of the dual-connected bonds on the peer switches have their system ID set to the MLAG system ID. Therefore, from the point of view of the hosts, each of the links in its bond is connected to the same system and so the host uses both links.

Each peer switch periodically makes a list of the LACP partner MAC addresses for all of their bonds and sends that list to its peer (using the `clagd` service; see below). The LACP partner MAC address is the MAC address of the system at the other end of a bond (hosts server01, server02, and server03 in the figure above). When a switch receives this list from its peer, it compares the list to the LACP partner MAC addresses on its switch. If any matches are found and the `clag-id` for those bonds match, then that bond is a dual-connected bond. You can find the LACP partner MAC address by the running `net show bridge macs` command or by examining the `/sys/class/net/<bondname>/bonding/ad_partner_mac sysfs` file for each bond.

## Configure MLAG

To configure MLAG:

1. On the dual-connected device, create a bond that uses LACP. The method you use varies with the type of device you are configuring.
2. On each peer switch, configure the interfaces, including bonds, VLANs, bridges, and peer links.
   - Place every interface that connects to the MLAG pair from a dual-connected device into a {{<link url="Bonding-Link-Aggregation" text="bond">}}, even if the bond contains only a single link on a single physical switch. Layer 2 data travels over this bond. In the examples throughout this chapter, *peerlink* is the name of the bond. Single-attached hosts, also known as *orphan ports*, can be just a member of the bridge.
   - Configure the fast mode of LACP on the bond to allow more timely updates of the LACP state. These bonds are then placed in a bridge, which must include the peer link between the switches.

   ```
   cumulus@switch:~$ net add bond bond1 bond slaves swp1
   cumulus@switch:~$ net add bond bond2 bond slaves swp2
   cumulus@switch:~$ net add bond bond3 bond slaves swp3
   cumulus@switch:~$ net add bond peerlink bond slaves swp49-swp50
   cumulus@switch:~$ net pending
   cumulus@switch:~$ net commit
   ```

   ```
   cumulus@switch:~$ net add bridge bridge ports bond1,bond2,bond3,peerlink
   cumulus@switch:~$ net add bridge bridge vids 10,20,30
   cumulus@switch:~$ net add bridge bridge pvid 1
   cumulus@switch:~$ net pending
   cumulus@switch:~$ net commit
   ```

3. Enable communication between the `clagd` services on the peer switches:
   - Choose an unused VLAN (also known as a *switched virtual interface* or *SVI*).
   - Assign the SVI an unrouteable link-local address to give the peer switches layer 3 connectivity between each other.
   - Configure the VLAN as a {{<link url="Interface-Configuration-and-Management" text="VLAN subinterface">}} on the peer link bond instead of the VLAN-aware bridge, called *peerlink*. If you configure the subinterface with {{<link url="Network-Command-Line-Utility-NCLU" text="NCLU">}}, the VLAN subinterface is named 4094 by default. If you are configuring the peer link without NCLU, Cumulus Networks recommends you use 4094 to ensures that the VLAN is completely independent of the bridge and spanning tree forwarding decisions.
   - To avoid issues with STP, include untagged traffic on the peer link.
   - Specify a backup interface, which is any layer 3 backup interface for your peer links in case the peer link goes down. See {{<link url="#specify-a-backup-link" text="backup link">}} and {{<link url="#failover-redundancy-scenarios" text="redundancy scenarios">}} below.

   ```
   example
   ```

4. DO WHAT HERE 

   The following example configures *peerlink.4094*, where *peerlink* is the inter-chassis bond and VLAN 4094 is the peer link VLAN:

   {{< tabs "TabID155 ">}}

{{< tab "NCLU Commands ">}}

```
cumulus@switch:~$ net add clag peer sys-mac 44:38:39:FF:40:94 interface swp49-50 primary backup-ip 10.10.10.2
cumulus@switch:~$ net pending
cumulus@switch:~$ net commit
```

   {{< /tab >}}

{{< tab "Linux Commands ">}}

Edit the `/etc/network/interfaces` file to add the peer link.

```
cumulus@switch:~$ sudo nano /etc/network/interfaces
...
auto peerlink
iface peerlink
    bond-slaves swp49 swp50

auto peerlink.4094
iface peerlink.4094
    clagd-backup-ip 10.10.10.2
    clagd-peer-ip linklocal
    clagd-sys-mac 44:38:39:BE:EF:AA
...
```

To enable MLAG, add *peerlink* to a traditional or VLAN-aware bridge, then run the `ifreload -a` command. The configuration below adds *peerlink* to a VLAN-aware bridge:

```
cumulus@switch:~$ sudo nano /etc/network/interfaces
...
auto bridge
iface bridge
    bridge-ports peerlink
    bridge-vlan-aware yes
...
```

```
cumulus@switch:~$ sudo ifreload -a
```

{{< /tab >}}

{{< /tabs >}}

  {{%notice note%}}

To prevent MAC address conflicts with other interfaces in the same bridged network, Cumulus Networks has reserved a range of MAC addresses specifically to use with MLAG. This range of MAC addresses is 44:38:39:ff:00:00 to 44:38:39:ff:ff:ff. Cumulus Networks recommends you use this range of MAC addresses when configuring MLAG.

- You *cannot* use the same MAC address for different MLAG pairs. Make sure you specify a different `clagd-sys-mac` setting for each MLAG pair in the network.
- You cannot use multicast MAC addresses as the `clagd-sys-mac`.
- If you configure MLAG with NCLU commands, Cumulus Linux does not check against a possible collision with VLANs outside the default reserved range when creating the peer link interfaces.

{{%/notice%}}

{{%notice note%}}

Do *not* add VLAN 4094 to the bridge VLAN list; VLAN 4094 for the peer link subinterface must **not** be also configured as a bridged VLAN with bridge VIDs under the bridge.

{{%/notice%}}

5. Enable MLAG by add *peerlink* to the bridge. The commands below add *peerlink* to a VLAN-aware bridge:

   ```
   cumulus@switch:~$ net add bridge bridge ports peerlink
   cumulus@switch:~$ net pending
   cumulus@switch:~$ net commit
   ```

{{%notice note%}}

- When you change the MLAG configuration in the `/etc/network/interfaces` file, the changes take effect when you bring the peer link interface up with `ifup` or `ifreload -a`. Do **not** use `systemctl restart clagd.service` to apply the new configuration.
- Do not use 169.254.0.1 as the MLAG peer link IP address; Cumulus Linux uses this address exclusively for {{<link url="Border-Gateway-Protocol-BGP" text="BGP unnumbered">}} interfaces.

{{%/notice%}}

MLAG synchronizes the dynamic state between the two peer switches but it does not synchronize the switch configurations. After modifying the configuration of one peer switch, you must make the same changes to the configuration on the other peer switch. This applies to all configuration changes, including:
- Port configuration, such as VLAN membership, {{<link url="#mtu-in-an-mlag-configuration" text="MTU">}} and bonding parameters.
- Bridge configuration, such as spanning tree parameters or bridge properties.
- Static address entries, such as static FDB entries and static IGMP entries.
- QoS configuration, such as ACL entries.

To verify VLAN membership configuration, run the NCLU `net show clag verify-vlans verbose` command or the Linux `clagctl -v verifyvlans` command. For example:

```
cumulus@switch:mgmt:~$ net show clag verify-vlans verbose
Vlan Database
Our Bond Interface   VlanId   Peer Bond Interface
------------------   ------   -------------------
bond1                    10   bond1
bond2                    20   bond2
bond3                    30   bond3
```

### Set Roles and Priority

Each MLAG-enabled switch in the pair has a *role*. When the peering relationship is established between the two switches, one switch is put into the *primary* role, and the other into the *secondary* role. When an MLAG-enabled switch is in the secondary role, it does not send STP BPDUs on dual-connected links; it only sends BPDUs on single-connected links. The switch in the primary role sends STP BPDUs on all single- and dual-connected links.

| Sends BPDUs Via        | Primary | Secondary |
| ---------------------- | ------- | --------- |
| Single-connected links | Yes     | Yes       |
| Dual-connected links   | Yes     | No        |

By default, the role is determined by comparing the MAC addresses of the two sides of the peering link; the switch with the lower MAC address assumes the primary role. You can override this by setting the `clagd-priority` option for the peer link:

{{< tabs "TabID243 ">}}

{{< tab "NCLU Commands ">}}

The following command example sets the `clagd-priority` option for the peer link.

```
cumulus@switch:~$ net add interface peerlink.4094 clag priority 2048
cumulus@switch:~$ net pending
cumulus@switch:~$ net commit
```

{{< /tab >}}

{{< tab "Linux Commands ">}}

Edit the `/etc/network/interfaces` file and add the `clagd-priority` option, then run the `ifreload -a` command. The following example sets the `clagd-priority` option for the peer link:

```
cumulus@switch:~$ sudo nano /etc/network/interfaces
...
auto peerlink.4094
iface peerlink.4094
    clagd-peer-ip linklocal
    clagd-backup-ip 10.10.10.2
    clagd-sys-mac 44:38:39:BE:EF:AA
    clagd-priority 2048
...
```

```
cumulus@switch:~$ sudo ifreload -a
```

{{< /tab >}}

{{< /tabs >}}

The switch with the lower priority value is given the primary role; the default value is 32768 and the range is 0 to 65535. Read the `clagd(8)` and `clagctl(8)` man pages for more information.

When the `clagd` service exits during switch reboot or if you stop the service on the primary switch, the peer switch that is in the secondary role becomes the primary.

However, if the primary switch goes down without stopping the `clagd` service for any reason, or if the peer link goes down, the secondary switch does **not** change its role. In case the peer switch is determined to be not alive, the switch in the secondary role rolls back the LACP system ID to be the bond interface MAC address instead of the `clagd-sys-mac` and the switch in primary role uses the `clagd-sys-mac` as the LACP system ID on the bonds.

### Set clagctl Timers

The `clagd` service has a number of timers that you can tune for enhanced performance:

| <div style="width:250px">Timer | Description |
| ----- | ----------- |
| `--reloadTimer <SECONDS>` | The number of seconds to wait for the peer switch to become active. If the peer switch does not become active after the timer expires, the MLAG bonds leave the initialization ({{<link url="#peer-link-interfaces-and-the-protodown-state" text="protodown">}}) state and become active. This provides `clagd` with sufficient time to determine whether the peer switch is coming up or if it is permanently unreachable. <br>The default is *300* seconds.|
| `--peerTimeout <SECONDS>` | The number of seconds `clagd` waits without receiving any data from the peer switch before it determines that the peer is no longer active. If this parameter is not specified, `clagd` uses ten times the local `lacpPoll` value. |
| `--initDelay <SECONDS>` | The number of seconds `clagd` delays bringing up MLAG bonds and anycast IP addresses. <br>The default is *180* seconds. |
| `--sendTimeout <SECONDS>` | The number of seconds `clagd` waits until the sending socket times out. If it takes longer than the `sendTimeout` value to send data to the peer, `clagd` generates an exception. <br>The default is *30* seconds. |

To set a timer, use NCLU. For example, to set the `peerTimeout` to 900 seconds:

```
cumulus@switch:~$ net add interface peerlink.4094 clag args --peerTimeout 900
cumulus@switch:~$ net pending
cumulus@switch:~$ net commit
```

You can run `clagctl params` to see the settings for all of the `clagd` parameters.

```
cumulus@leaf01:~$ clagctl params
clagVersion = 1.4.0
clagDataVersion = 1.4.0
clagCmdVersion = 1.1.0
peerIp = linklocal
peerIf = peerlink.4094
sysMac = 44:38:39:be:ef:aa
lacpPoll = 2
currLacpPoll = 2
peerConnect = 1
cmdConnect = 1
peerLinkPoll = 1
switchdReadyTimeout = 120
reloadTimer = 300
periodicRun = 4
priority = 1000
quiet = False
debug = 0x0
verbose = False
log = syslog
vm = True
peerPort = 5342
peerTimeout = 20
initDelay = 180
sendTimeout = 30
sendBufSize = 65536
forceDynamic = False
dormantDisable = False
redirectEnable = False
backupIp = 10.10.10.2
backupVrf = None
backupPort = 5342
vxlanAnycast = None
neighSync = True
permanentMacSync = True
cmdLine = /usr/sbin/clagd --daemon linklocal peerlink.4094 44:38:39:BE:EF:AA --priority 1000 --backupIp 10.10.10.2
peerlinkLearnEnable = False
```

## Disable MLAG on an Interface

The `clagd-peer-ip` and `clagd-sys-mac` parameters are mandatory for MLAG configuration; however, the rest are optional. When mandatory `clagd` commands are present under a peer link subinterface, the `clagd-enable` option is not present but is enabled by default. To disable `clagd` on the subinterface, set `clagd-enable` to *no*:

{{< tabs "TabID878 ">}}

{{< tab "NCLU Commands ">}}

```
cumulus@switch:~$ net add interface peerlink.4094 clag enable no
cumulus@switch:~$ net pending
cumulus@switch:~$ net commit
```

{{< /tab >}}

{{< tab "Linux Commands ">}}

Edit the `/etc/network/interfaces` file to add `clagd-enable no` to the interface stanza, then run the `ifreload -a` command:

```
cumulus@switch:~$ sudo nano /etc/network/interfaces
...
auto peerlink.4094
iface peerlink.4094
    clagd-backup-ip 10.10.10.2
    clagd-enable no
    clagd-peer-ip linklocal
    clagd-priority 1000
    clagd-sys-mac 44:38:39:BE:EF:AA
...
```

```
cumulus@switch:~$ sudo ifreload -a
```

{{< /tab >}}

{{< /tabs >}}

Use `clagd-priority` to set the role of the MLAG peer switch to primary or secondary. Each peer switch in an MLAG pair must have the same `clagd-sys-mac` setting. Each `clagd-sys-mac` setting must be unique to each MLAG pair in the network. For more details, refer to `man clagd`.

## Configure MLAG with a Traditional Mode Bridge

To configure MLAG with a traditional mode bridge instead of a {{<link url="VLAN-aware-Bridge-Mode" text="VLAN-aware mode bridge">}}, configure the peer link and all dual-connected links as {{<link url="Traditional-Bridge-Mode" text="untagged/native">}} ports on a bridge (note the absence of any VLANs in the bridge-ports line and the lack of the bridge-vlan-aware parameter below):

```
...
auto br0
iface br0
    bridge-ports peerlink leaf01 leaf02 server01 server02
...
```

The following example shows you how to allow VLAN 10 across the peer link:

```
...
auto br0.10
iface br0.10
    bridge-ports peerlink.10 bond1.10
    bridge-stp on
...
```

For a deeper comparison of traditional versus VLAN-aware bridge modes, read this {{<exlink url="https://docs.cumulusnetworks.com/knowledge-base/Configuration-and-Usage/Network-Interfaces/Compare-Traditional-Bridge-Mode-to-VLAN-aware-Bridge-Mode/" text="knowledge base article">}}.

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

You must specify a backup link for your peer links in case the peer link goes down. When this happens, the `clagd` service uses the backup link to check the health of the peer switch. The backup link is specified in the `clagd-backup-ip` parameter.

In an anycast VTEP environment, if you do not specify the `clagd-backup-ip` parameter, large convergence times (around 5 minutes) can result when the primary MLAG switch is powered off. Then the secondary switch must wait until the reload delay timer expires (which defaults to 300 seconds, or 5 minutes) before bringing up a VNI with its unique loopback IP.

The backup IP address **must** be different than the peer link IP address (`clagd-peer-ip`). It must be reachable by a route that does not use the peer link and it must be in the same network namespace as the peer link IP address.

{{%notice note%}}

The `clagd-backup-ip` is required.

{{%/notice%}}

Cumulus Networks recommends you use the loopback or management IP address of the switch for this purpose. Which one should you choose?

- If your MLAG configuration has **routed uplinks** (a modern approach to the data center fabric network), configure `clagd` to use the peer switch **loopback** address for the health check. When the peer link is down, the secondary switch must route towards the loopback address using uplinks (towards the spine layer). If the primary switch is also suffering a more significant problem (for example, `switchd` is unresponsive or stopped), then the secondary switch eventually promotes itself to primary and traffic now flows normally.

    To ensure IP connectivity between the loopbacks, you must carefully consider what implications this has on the BGP ASN configured:
    - The two MLAG member switches must use unique BGP ASNs.
    - If the two MLAG member switches use the same BGP ASN, you must bypass the BGP loop prevention check on AS_PATH attribute.

- If your MLAG configuration has **bridged uplinks** (such as a campus network or a large, flat layer 2 network), configure `clagd` to use the peer switch **eth0** address for the health check. When the peer link is down, the secondary switch must route towards the eth0 address using the OOB network (provided you have implemented an OOB network).

To configure a backup link:

{{< tabs "TabID1002 ">}}

{{< tab "NCLU Commands ">}}

```
cumulus@switch:~$ net add interface peerlink.4094 clag backup-ip 10.10.10.2
cumulus@switch:~$ net pending
cumulus@switch:~$ net commit
```

You can also specify the backup UDP port. The port defaults to 5342, but you can configure it with the `clagd args` `--backupPort <PORT>` option. For example:

```
cumulus@switch:~$ net add interface peerlink.4094 clag args --backupPort 5400
cumulus@switch:~$ net pending
cumulus@switch:~$ net commit
```

{{< /tab >}}

{{< tab "Linux Commands ">}}

Edit the `/etc/network/interfaces` file to add `clag-backup-ip <ip-address>` to the peer link configuration, then run the `ifreload -a` command. For example:

```
cumulus@switch:~$ sudo nano /etc/network/interfaces
...
auto peerlink.4094
iface peerlink.4094
    netmask 255.255.255.0
    clagd-priority 8192
    clagd-peer-ip linklocal
    clagd-backup-ip 10.10.10.2
    clagd-sys-mac 44:38:39:ff:00:01
    clagd-args --priority 1000
...
```

```
cumulus@switch:~$ sudo ifreload -a
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
    clagd-backup-ip 10.10.10.2
    clagd-args --backupPort 5400
    clagd-sys-mac 44:38:39:ff:00:01
    clagd-args --priority 1000
...
```

{{< /tab >}}

{{< /tabs >}}

To show the backup IP address, run the NCLU `net show clag` command or the Linux `clagctl` command. For example:

```
cumulus@switch:~$ net show clag
The peer is alive
        Our Priority, ID, and Role: 32768 44:38:39:00:00:41 primary
    Peer Priority, ID, and Role: 32768 44:38:39:00:00:42 secondary
            Peer Interface and IP: peerlink.4094 linklocal
                        Backup IP: 10.10.10.2 (active)
                        System MAC: 44:38:39:ff:00:01

CLAG Interfaces
Our Interface      Peer Interface     CLAG Id   Conflicts              Proto-Down Reason
----------------   ----------------   -------   --------------------   -----------------
        leaf03-04   leaf03-04          1034      -                      -
        exit01-02   -                  2930      -                      -
        leaf01-02   leaf01-02          1012      -                      -
```

### Specify a Backup Link to a VRF

You can configure the backup link to a {{<link url="Virtual-Routing-and-Forwarding-VRF" text="VRF">}} or {{<link url="Management-VRF" text="management VRF">}}. Include the name of the VRF or management VRF with the `clagd-backup-ip` command.

{{%notice note%}}

You cannot use the VRF on a peer link subinterface.

{{%/notice%}}

{{< tabs "TabID1094 ">}}

{{< tab "NCLU Commands ">}}

```
cumulus@switch:~$ net add interface peerlink.4094 clag backup-ip 10.10.10.2 vrf RED
cumulus@switch:~$ net pending
cumulus@switch:~$ net commit
```

{{< /tab >}}

{{< tab "Linux Commands ">}}

Edit the `/etc/network/interfaces` file to include the name of the VRF or management VRF with the `clag-backup-ip` option, then run the `ifreload -a` command. The following configuration links to the management VRF.

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
        clagd-backup-ip 10.10.10.2 vrf mgmt
        clagd-sys-mac 44:38:39:ff:00:01
...
```

```
cumulus@switch:~$ sudo ifreload -a
```

{{< /tab >}}

{{< /tabs >}}

To verify the backup link, run the NCLU `net show clag` command or the Linux `clagctl` command. For example:

```
cumulus@switch:~$ net show clag
The peer is alive
        Our Priority, ID, and Role: 32768 44:38:39:00:00:41 primary
    Peer Priority, ID, and Role: 32768 44:38:39:00:00:42 secondary
            Peer Interface and IP: peerlink.4094 linklocal
                        Backup IP: 10.10.10.2 vrf RED (active)
                        System MAC: 44:38:39:FF:40:90

CLAG Interfaces
Our Interface      Peer Interface     CLAG Id   Conflicts              Proto-Down Reason
----------------   ----------------   -------   --------------------   -----------------
        leaf03-04   leaf03-04          1034      -                      -
        exit01-02   -                  2930      -                      -
        leaf01-02   leaf01-02          1012      -                      -
```

## Monitor Dual-connected Peers

When the switch receives a valid message from its peer, it knows that `clagd` is alive and executing on that peer. This causes `clagd` to change the system ID of each bond that is assigned a `clag-id` from the default value (the MAC address of the bond) to the system ID assigned to both peer switches. This makes the hosts connected to each switch act as if they are connected to the same system so that they use all ports within their bond. Additionally, `clagd` determines which bonds are dual-connected and modifies the forwarding and learning behavior to accommodate these dual-connected bonds.

If the peer does not receive any messages for three update intervals, that peer switch is assumed to no longer be acting as an MLAG peer. In this case, the switch reverts all configuration changes so that it operates as a standard non-MLAG switch. This includes removing all statically assigned MAC addresses, clearing the egress forwarding mask, and allowing addresses to move from any port to the peer port. After a message is again received from the peer, MLAG operation starts again as described earlier. You can configure a custom timeout setting by adding `--peerTimeout <value>` to `clagd-args`:

{{< tabs "TabID1163 ">}}

{{< tab "NCLU Commands ">}}

The following example commands set the timeout to 900:

```
cumulus@switch:~$ net add interface peerlink.4094 clag args --peerTimeout 900
cumulus@switch:~$ net pending
cumulus@switch:~$ net commit
```

{{< /tab >}}

{{< tab "Linux Commands ">}}

Edit the `/etc/network/interfaces` file and add the timeout to the *peerlink* stanza, then run the `ifreload -a` command. The following example sets the timeout to 900:

```
cumulus@switch:~$ sudo nano /etc/network/interfaces
...
auto peerlink.4094
iface peerlink.4094
    clagd-args --backupPort 5400
    clagd-args --peerTimeout 900
    clagd-peer-ip linklocal
    clagd-backup-ip 10.10.10.2
    clagd-priority 8192
    clagd-sys-mac 44:38:39:ff:00:01
...
```

```
cumulus@switch:~$ sudo ifreload -a
```

{{< /tab >}}

{{< /tabs >}}

After bonds are identified as dual-connected, `clagd` sends more information to the peer switch for those bonds. The MAC addresses (and VLANs) that are dynamically learned on those ports are sent along with the LACP partner MAC address for each bond. When a switch receives MAC address information from its peer, it adds MAC address entries on the corresponding ports. As the switch learns and ages out MAC addresses, it informs the peer switch of these changes to its MAC address table so that the peer can keep its table synchronized. Periodically, at 45% of the bridge ageing time, a switch sends its entire MAC address table to the peer, so that peer switch can verify that its MAC address table is properly synchronized.

The switch sends an update frequency value in the messages to its peer, which tells `clagd` how often the peer will send these messages. You can configure a different frequency by adding `--lacpPoll <seconds>` to `clagd-args`:

{{< tabs "TabID1207 ">}}

{{< tab "NCLU Commands ">}}

The following example command sets the frequency to 900 seconds:

```
cumulus@switch:~$ net add interface peerlink.4094 clag args --lacpPoll 900
cumulus@switch:~$ net pending
cumulus@switch:~$ net commit
```

{{< /tab >}}

{{< tab "Linux Commands ">}}

Edit the `/etc/network/interfaces` file, then run the `ifreload -a` command. The following example sets the frequency to 900 seconds:

```
cumulus@switch:~$ sudo nano /etc/network/interfaces
...
auto peerlink.4094
 iface peerlink.4094
    clagd-args --backupPort 5400
    clagd-args --lacpPoll 900
    clagd-peer-ip linklocal
    clagd-backup-ip 10.10.10.2
    clagd-priority 8192
    clagd-sys-mac 44:38:39:ff:00:01
...
```

```
cumulus@switch:~$ sudo ifreload -a
```

{{< /tab >}}

{{< /tabs >}}

<!-- ## Configure Layer 3 Routed Uplinks

In this scenario, the spine switches connect at layer 3, as shown in the image below. Alternatively, the spine switches can be singly connected to each core switch at layer 3 (not shown below).

{{< img src = "/images/cumulus-linux/mlag-layer3-routed.png" >}}

In this design, the spine switches route traffic between the server hosts in the layer 2 domains and the core. The servers (host1 thru host4) each have a layer 2 connection up to the spine layer where the default gateway for the host subnets resides. However, since the spine switches as gateway devices communicate at layer 3, you need to configure a protocol such as {{<link url="Virtual-Router-Redundancy-VRR-and-VRRP" text="VRR">}} (virtual router redundancy) between the spine switch pair to support active/active forwarding.

Then, to connect the spine switches to the core switches, you need to determine whether the routing is static or dynamic. If it is dynamic, you must choose which protocol to use ({{<link url="Open-Shortest-Path-First-OSPF" text="OSPF">}} or {{<link url="Border-Gateway-Protocol-BGP" text="BGP">}}). When enabling a routing protocol in an MLAG environment, it is also necessary to manage the uplinks, because by default MLAG is not aware of layer 3 uplink interfaces. If there is a peer link failure, MLAG does not remove static routes or bring down a BGP or OSPF adjacency unless you use a separate link state daemon such as `ifplugd`. -->

### MLAG and Peer Link Peering

When using MLAG with VRR, Cumulus Networks recommends you set up a routed adjacency across the peerlink.4094 interface. If a routed connection is not built across the peer link, then during uplink failure on one of the switches in the MLAG pair, egress traffic can be blackholed if it hashes to the leaf whose uplinks are down.

To set up the adjacency, configure a {{<link url="Border-Gateway-Protocol-BGP#unnumbered" text="BGP">}} or {{<link url="Open-Shortest-Path-First-OSPF" text="OSPF">}} unnumbered peering, as appropriate for your network.

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

If you are using {{<link url="Ethernet-Virtual-Private-Network-EVPN" text="EVPN">}} and MLAG, you need to enable the EVPN address family across the peerlink.4094 interface as well:

```
cumulus@switch:~$ net add bgp neighbor peerlink.4094 interface remote-as internal
cumulus@switch:~$ net add bgp l2vpn evpn neighbor peerlink.4094 activate
cumulus@switch:~$ net commit
```

{{%notice tip%}}

Be aware of an existing issue when you use NCLU to create an iBGP peering, it creates an eBGP peering instead. For more information, see {{<exlink url="https://docs.cumulusnetworks.com/cumulus-linux-37/Whats-New/rn/#CM-23417" text="this release note">}}.

{{%/notice%}}

## IGMP Snooping with MLAG

{{<link url="IGMP-and-MLD-Snooping" text="IGMP snooping">}} processes IGMP reports received on a bridge port in a bridge to identify hosts that are configured to receive multicast traffic destined to that group. An IGMP query message received on a port is used to identify the port that is connected to a router and configured to receive multicast traffic.

IGMP snooping is enabled by default on the bridge. IGMP snooping multicast database entries and router port entries are synced to the peer MLAG switch. If there is no multicast router in the VLAN, you can configure the IGMP querier on the switch to generate IGMP query messages. For more information, read the {{<link url="IGMP-and-MLD-Snooping" text="IGMP snooping">}}  chapter.

{{%notice note%}}

 In an MLAG configuration, the switch in the secondary role does not send IGMP queries, even though the configuration is identical to the switch in the primary role. This is expected behavior, as there can be only one querier on each VLAN. Once the querier on the primary switch stops transmitting, the secondary switch starts transmitting.

{{%/notice%}}

## MLAG Best Practices

### MTU in an MLAG Configuration

The {{<link url="Switch-Port-Attributes#mtu" text="MTU">}} in MLAG traffic is determined by the bridge MTU. Bridge MTU is determined by the lowest MTU setting of an interface that is a member of the bridge. If you want to set an MTU other than the default of 9216 bytes, you must configure the MTU on each physical interface and bond interface that are members of the MLAG bridges in the entire bridged domain.

For example, if an MTU of 1500 is desired through the MLAG domain in the example shown above, **on all four leaf switches**, {{%link url="Switch-Port-Attributes#mtu" text="configure `mtu 1500`"%}} for each of the following bond interfaces, as they are members of bridge *bridge*: peerlink, uplink, server01.

{{< tabs "TabID1358 ">}}

{{< tab "NCLU Commands ">}}

```
cumulus@switch:~$ net add bond peerlink mtu 1500
cumulus@switch:~$ net add bond uplink mtu 1500
cumulus@switch:~$ net add bond server01 mtu 1500
cumulus@switch:~$ net pending
cumulus@switch:~$ net commit
```

{{< /tab >}}

{{< tab "Linux Commands ">}}

Edit the `/etc/network/interfaces` file, then run the `ifreload -a` command. This is an example configuration:

```
cumulus@switch:~$ sudo nano /etc/network/interfaces
...
auto bridge
iface bridge
    bridge-ports peerlink uplink server01

auto peerlink
iface peerlink
    mtu 1500

auto server01
iface server01
    mtu 1500

auto uplink
iface uplink
    mtu 1500
...
```

```
cumulus@switch:~$ sudo ifreload -a
```

{{< /tab >}}

{{< /tabs >}}

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

Scaling this example out to a full rack, when planning for link failures, you need only allocate enough bandwidth to meet your site's strategy for handling failure scenarios. Imagine a full rack with 40 servers and two switches. You might plan for four to six servers to lose connectivity to a single switch and become single connected before you respond to the event. So expanding upon our previous example, if you have 40 hosts each with 20G of bandwidth dual-connected to the MLAG pair, you might allocate 20G to 30G of bandwidth to the peer link - which accounts for half of the single-connected bandwidth for four to six hosts.

### Failover Redundancy Scenarios

To get a better understanding of how STP and LACP behave in response to various failover redundancy scenarios, read
{{<exlink url="https://docs.cumulusnetworks.com/knowledge-base/Configuration-and-Usage/Network-Interfaces/MLAG-Redundancy-Scenarios/" text="this knowledge base article">}}.

### STP and MLAG

Cumulus Networks recommends that you always enable STP in your layer 2 network.

With MLAG, Cumulus Networks recommends you enable BPDU guard on the host-facing bond interfaces. For more information about BPDU guard, see {{<link url="Spanning-Tree-and-Rapid-Spanning-Tree-STP#bpdu-guard" text="BPDU Guard and Bridge Assurance">}}.

To show useful STP troubleshooting information:

{{< tabs "TabID1438 ">}}

{{< tab "NCLU Commands ">}}

Run the `net show bridge spanning-tree` command:

```
cumulus@switch:~$ net show bridge spanning-tree
Bridge info
    enabled         yes
    bridge id       8.000.44:38:39:BE:EF:AA
    Priority:   32768
    Address:    44:38:39:BE:EF:AA
    This bridge is root.

designated root 8.000.44:38:39:BE:EF:AA
Priority:   32768
Address:    44:44:38:39:BE:EF:AA

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

{{< /tab >}}

{{< tab "Linux Commands ">}}

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

{{< /tab >}}

{{< /tabs >}}

{{%notice note%}}xs

- The STP global configuration must be the same on both peer switches.
- The STP configuration for dual-connected ports must be the same on both peer switches.
- The STP priority must be the same on both peer switches.

For additional information on STP, see {{<link url="Spanning-Tree-and-Rapid-Spanning-Tree-STP" text="Spanning Tree Priority">}}.

{{%/notice%}}

## Example MLAG Configuration

The example below shows an MLAG configuration.

{{< img src = "/images/cumulus-linux/mlag-config.png" >}}

{{< tabs "TabID2970 ">}}

{{< tab "leaf01 ">}}

```
cumulus@leaf01:~$ cat /etc/network/interfaces

auto lo
iface lo inet loopback
    address 10.10.10.1/32

auto mgmt
iface mgmt
    vrf-table auto
    address 127.0.0.1/8
    address ::1/128

auto eth0
iface eth0 inet dhcp
    vrf mgmt

auto bridge
iface bridge
    bridge-ports peerlink
    bridge-ports bond1 bond2 bond3
    bridge-vids 10 20 30  
    bridge-vlan-aware yes

auto vlan10
iface vlan10
    address 10.1.10.2/24
    vlan-raw-device bridge
    vlan-id 10

auto vlan20
iface vlan20
    address 10.1.20.2/24
    vlan-raw-device bridge
    vlan-id 20

auto vlan30
iface vlan30
    address 10.1.30.2/24
    vlan-raw-device bridge
    vlan-id 30

auto swp51
iface swp51
    alias leaf to spine

auto swp52
iface swp52
    alias leaf to spine

auto swp49
iface swp49
    alias peerlink

auto swp50
iface swp50
    alias peerlink

auto peerlink
iface peerlink
    bond-slaves swp49 swp50

auto peerlink.4094
iface peerlink.4094
    clagd-backup-ip 10.10.10.2
    clagd-peer-ip linklocal
    clagd-priority 1000
    clagd-sys-mac 44:38:39:BE:EF:AA

auto swp1
iface swp1
    alias bond member of bond1
    mtu 9000

auto bond1
iface bond1
    alias bond1 on swp1
    mtu 9000
    clag-id 1
    bridge-access 10
    bond-slaves swp1
    bond-lacp-bypass-allow yes
    mstpctl-bpduguard yes
    mstpctl-portadminedge yes

auto swp2
iface swp2
    alias bond member of bond2
    mtu 9000

auto bond2
iface bond2
    alias bond2 on swp2
    mtu 9000
    clag-id 2
    bridge-access 20
    bond-slaves swp2
    bond-lacp-bypass-allow yes
    mstpctl-bpduguard yes
    mstpctl-portadminedge yes

auto swp3
iface swp3
    alias bond member of bond3
    mtu 9000

auto bond3
iface bond3
    alias bond3 on swp3
    mtu 9000
    clag-id 3
    bridge-access 30
    bond-slaves swp3
    bond-lacp-bypass-allow yes
    mstpctl-bpduguard yes
    mstpctl-portadminedge yes
```

{{< /tab >}}

{{< tab "leaf02 ">}}

```
cumulus@leaf02:~$ cat /etc/network/interfaces

auto lo
iface lo inet loopback
    address 10.10.10.2/32

auto mgmt
iface mgmt
    vrf-table auto
    address 127.0.0.1/8
    address ::1/128

auto eth0
iface eth0 inet dhcp
    vrf mgmt

auto bridge
iface bridge
    bridge-ports peerlink
    bridge-ports bond1 bond2 bond3
    bridge-vids 10 20 30  
    bridge-vlan-aware yes

auto vlan10
iface vlan10
    address 10.1.10.3/24
    vlan-raw-device bridge
    vlan-id 10

auto vlan20
iface vlan20
    address 10.1.20.3/24
    vlan-raw-device bridge
    vlan-id 20

auto vlan30
iface vlan30
    address 10.1.30.3/24
    vlan-raw-device bridge
    vlan-id 30

auto swp51
iface swp51
    alias leaf to spine

auto swp52
iface swp52
    alias leaf to spine

auto swp49
iface swp49
    alias peerlink

auto swp50
iface swp50
    alias peerlink

auto peerlink
iface peerlink
    bond-slaves swp49 swp50

auto peerlink.4094
iface peerlink.4094
    clagd-backup-ip 10.10.10.1
    clagd-peer-ip linklocal
    clagd-priority 32768
    clagd-sys-mac 44:38:39:BE:EF:AA

auto swp1
iface swp1
    alias bond member of bond1
    mtu 9000

auto bond1
iface bond1
    alias bond1 on swp1
    mtu 9000
    clag-id 1
    bridge-access 10
    bond-slaves swp1
    bond-lacp-bypass-allow yes
    mstpctl-bpduguard yes
    mstpctl-portadminedge yes

auto swp2
iface swp2
    alias bond member of bond2
    mtu 9000

auto bond2
iface bond2
    alias bond2 on swp2
    mtu 9000
    clag-id 2
    bridge-access 20
    bond-slaves swp2
    bond-lacp-bypass-allow yes
    mstpctl-bpduguard yes
    mstpctl-portadminedge yes

auto swp3
iface swp3
    alias bond member of bond3
    mtu 9000

auto bond3
iface bond3
    alias bond3 on swp3
    mtu 9000
    clag-id 3
    bridge-access 30
    bond-slaves swp3
    bond-lacp-bypass-allow yes
    mstpctl-bpduguard yes
    mstpctl-portadminedge yes
```

{{< /tab >}}

{{< tab "leaf03 ">}}

```
cumulus@leaf03:~$ cat /etc/network/interfaces

auto lo
iface lo inet loopback
    address 10.10.10.3/32

auto mgmt
iface mgmt
    vrf-table auto
    address 127.0.0.1/8
    address ::1/128

auto eth0
iface eth0 inet dhcp
    vrf mgmt

auto bridge
iface bridge
    bridge-ports peerlink
    bridge-ports bond1 bond2 bond3
    bridge-vids 10 20 30  
    bridge-vlan-aware yes

auto vlan10
iface vlan10
    address 10.1.10.2/24
    vlan-raw-device bridge
    vlan-id 10

auto vlan20
iface vlan20
    address 10.1.20.2/24
    vlan-raw-device bridge
    vlan-id 20

auto vlan30
iface vlan30
    address 10.1.30.2/24
    vlan-raw-device bridge
    vlan-id 30

auto swp51
iface swp51
    alias leaf to spine

auto swp52
iface swp52
    alias leaf to spine

auto swp49
iface swp49
    alias peerlink

auto swp50
iface swp50
    alias peerlink

auto peerlink
iface peerlink
    bond-slaves swp49 swp50

auto peerlink.4094
iface peerlink.4094
    clagd-backup-ip 10.10.10.4
    clagd-peer-ip linklocal
    clagd-priority 1000
    clagd-sys-mac 44:38:39:BE:EF:BB

auto swp1
iface swp1
    alias bond member of bond1
    mtu 9000

auto bond1
iface bond1
    alias bond1 on swp1
    mtu 9000
    clag-id 1
    bridge-access 10
    bond-slaves swp1
    bond-lacp-bypass-allow yes
    mstpctl-bpduguard yes
    mstpctl-portadminedge yes

auto swp2
iface swp2
    alias bond member of bond2
    mtu 9000

auto bond2
iface bond2
    alias bond2 on swp2
    mtu 9000
    clag-id 2
    bridge-access 20
    bond-slaves swp2
    bond-lacp-bypass-allow yes
    mstpctl-bpduguard yes
    mstpctl-portadminedge yes

auto swp3
iface swp3
    alias bond member of bond3
    mtu 9000

auto bond3
iface bond3
    alias bond3 on swp3
    mtu 9000
    clag-id 3
    bridge-access 30
    bond-slaves swp3
    bond-lacp-bypass-allow yes
    mstpctl-bpduguard yes
    mstpctl-portadminedge yes
```

{{< /tab >}}

{{< tab "leaf04 ">}}

```
cumulus@leaf04:~$ cat /etc/network/interfaces

auto lo
iface lo inet loopback
    address 10.10.10.4/32

auto mgmt
iface mgmt
    vrf-table auto
    address 127.0.0.1/8
    address ::1/128

auto eth0
iface eth0 inet dhcp

auto bridge
iface bridge
    bridge-ports peerlink
    bridge-ports bond1 bond2 bond3
    bridge-vids 10 20 30
    bridge-vlan-aware yes

auto vlan10
iface vlan10
    address 10.1.10.3/24
    vlan-raw-device bridge
    vlan-id 10

auto vlan20
iface vlan20
    address 10.1.20.3/24
    vlan-raw-device bridge
    vlan-id 20

auto vlan30
iface vlan30
    address 10.1.30.3/24
    vlan-raw-device bridge
    vlan-id 30

auto swp51
iface swp51
    alias leaf to spine

auto swp52
iface swp52
    alias leaf to spine

auto swp49
iface swp49
    alias peerlink

auto swp50
iface swp50
    alias peerlink

auto peerlink
iface peerlink
    bond-slaves swp49 swp50

auto peerlink.4094
iface peerlink.4094
    clagd-backup-ip 10.10.10.3
    clagd-peer-ip linklocal
    clagd-priority 32768
    clagd-sys-mac 44:38:39:BE:EF:BB

auto swp1
iface swp1
    alias bond member of bond1
    mtu 9000

auto bond1
iface bond1
    alias bond1 on swp1
    mtu 9000
    clag-id 1
    bridge-access 10
    bond-slaves swp1
    bond-lacp-bypass-allow yes
    mstpctl-bpduguard yes
    mstpctl-portadminedge yes

auto swp2
iface swp2
    alias bond member of bond2
    mtu 9000

auto bond2
iface bond2
    alias bond2 on swp2
    mtu 9000
    clag-id 2
    bridge-access 20
    bond-slaves swp2
    bond-lacp-bypass-allow yes
    mstpctl-bpduguard yes
    mstpctl-portadminedge yes

auto swp3
iface swp3
    alias bond member of bond3
    mtu 9000

auto bond3
iface bond3
    alias bond3 on swp3
    mtu 9000
    clag-id 3
    bridge-access 30
    bond-slaves swp3
    bond-lacp-bypass-allow yes
    mstpctl-bpduguard yes
    mstpctl-portadminedge yes
```

{{< /tab >}}

{{< tab "spine01 ">}}

```
cumulus@spine01:~$ cat /etc/network/interfaces

auto lo
iface lo inet loopback
    address 10.10.10.101/32

auto mgmt
iface mgmt
    vrf-table auto
    address 127.0.0.1/8
    address ::1/128

auto eth0
iface eth0 inet dhcp
    vrf mgmt

auto swp1
iface swp1
    alias leaf to spine

auto swp2
iface swp2
    alias leaf to spine

auto swp3
iface swp3
    alias leaf to spine

auto swp4
iface swp4
    alias leaf to spine
```

{{< /tab >}}

{{< tab "spine02 ">}}

```
cumulus@spine02:~$ cat /etc/network/interfaces

auto lo
iface lo inet loopback
    address 10.10.10.102/32

auto mgmt
iface mgmt
    vrf-table auto
    address 127.0.0.1/8
    address ::1/128

auto eth0
iface eth0 inet dhcp
    vrf mgmt

auto swp1
iface swp1
    alias leaf to spine

auto swp2
iface swp2
    alias leaf to spine

auto swp3
iface swp3
    alias leaf to spine

auto swp4
iface swp4
    alias leaf to spine
```

{{< /tab >}}

{{< /tabs >}}

### /etc/frr/frr.conf

{{< tabs "TabID3535 ">}}

{{< tab "leaf01 ">}}

```
cumulus@leaf01:~$ cat /etc/frr/frr.conf
...
service integrated-vtysh-config
!
log syslog informational
!
router bgp 65101
 bgp router-id 10.10.10.1
 bgp bestpath as-path multipath-relax
 neighbor underlay peer-group
 neighbor underlay remote-as external
 neighbor peerlink.4094 interface remote-as internal
 neighbor swp51 interface peer-group underlay
 neighbor swp52 interface peer-group underlay
 !
 !
 address-family ipv4 unicast
  redistribute connected
 exit-address-family
 !

!
line vty
!
```

{{< /tab >}}

{{< tab "leaf02 ">}}

```
cumulus@leaf02:~$ cat /etc/frr/frr.conf
...
service integrated-vtysh-config
!
log syslog informational
!
router bgp 65101
 bgp router-id 10.10.10.2
 bgp bestpath as-path multipath-relax
 neighbor underlay peer-group
 neighbor underlay remote-as external
 neighbor peerlink.4094 interface remote-as internal
 neighbor swp51 interface peer-group underlay
 neighbor swp52 interface peer-group underlay
 !
 !
 address-family ipv4 unicast
  redistribute connected
 exit-address-family
!

!
line vty
!
```

{{< /tab >}}

{{< tab "leaf03 ">}}

```
cumulus@leaf03:~$ cat /etc/frr/frr.conf
...
service integrated-vtysh-config
!
log syslog informational
!
router bgp 65102
 bgp router-id 10.10.10.3
 bgp bestpath as-path multipath-relax
 neighbor underlay peer-group
 neighbor underlay remote-as external
 neighbor peerlink.4094 interface remote-as internal
 neighbor swp51 interface peer-group underlay
 neighbor swp52 interface peer-group underlay
 !
 !
 address-family ipv4 unicast
  redistribute connected
 exit-address-family
 !

!
line vty
!
```

{{< /tab >}}

{{< tab "leaf04 ">}}

```
cumulus@leaf04:~$ cat /etc/frr/frr.conf
...
service integrated-vtysh-config
!
log syslog informational
!
router bgp 65102
 bgp router-id 10.10.10.4
 bgp bestpath as-path multipath-relax
 neighbor underlay peer-group
 neighbor underlay remote-as external
 neighbor peerlink.4094 interface remote-as internal
 neighbor swp51 interface peer-group underlay
 neighbor swp52 interface peer-group underlay
 !
 !
 address-family ipv4 unicast
  redistribute connected
 exit-address-family
!

!
line vty
!
```

{{< /tab >}}

{{< tab "spine01 ">}}

```
cumulus@spine01:~$ cat /etc/frr/frr.conf
...
service integrated-vtysh-config
!
log syslog informational
!
!
router bgp 65199
 bgp router-id 10.10.10.101
 bgp bestpath as-path multipath-relax
 neighbor underlay peer-group
 neighbor underlay remote-as external
 neighbor swp1 interface peer-group underlay
 neighbor swp2 interface peer-group underlay
 neighbor swp3 interface peer-group underlay
 neighbor swp4 interface peer-group underlay
 !
 !
 address-family ipv4 unicast
  redistribute connected
 exit-address-family
!

!
line vty
!
```

{{< /tab >}}

{{< tab "spine02 ">}}

```
cumulus@spine02:~$ cat /etc/frr/frr.conf
...
service integrated-vtysh-config
!
log syslog informational
!
!
router bgp 65199
 bgp router-id 10.10.10.102
 bgp bestpath as-path multipath-relax
 neighbor underlay peer-group
 neighbor underlay remote-as external
 neighbor swp1 interface peer-group underlay
 neighbor swp2 interface peer-group underlay
 neighbor swp3 interface peer-group underlay
 neighbor swp4 interface peer-group underlay
 !
 !
 address-family ipv4 unicast
  redistribute connected
 exit-address-family
 !

!
line vty
!
```

{{< /tab >}}

{{< /tabs >}}

## Troubleshooting

### View the MLAG Log File

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

### Check the MLAG Configuration Status

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

### Monitor the Status of the clagd Service

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

### Large Packet Drops on the Peer Link Interface

A large volume of packet drops across one of the peer link interfaces can be expected. These drops serve to prevent looping of BUM (broadcast, unknown unicast, multicast) packets. When a packet is received across the peer link, if the destination lookup results in an egress interface that is a dual-connected bond, the switch does not forward the packet to prevent loops. This results in a drop being recorded on the peer link.

You can detect this issue by running the the following commands:

{{< tabs "TabID1547 ">}}

{{< tab "NCLU Commands ">}}

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

{{< /tab >}}

{{< tab "Linux Commands ">}}

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

{{< /tab >}}

{{< /tabs >}}

### Duplicate LACP Partner MAC Warning

When you run `clagctl`, you might see output similar to this:

```
bond1 bond1 52 duplicate lacp - partner mac
```

This occurs when you have multiple LACP bonds between the same two LACP endpoints; for example, an MLAG switch pair is one endpoint and an ESXi host is another. These bonds have duplicate LACP identifiers, which are MAC addresses. This same warning might trigger when you have a cabling or configuration error.

## Considerations

If both backup and peer connectivity are lost within a 30-second window, the switch in the secondary role misinterprets the event sequence, sees the peer switch as down and takes over as the primary.
