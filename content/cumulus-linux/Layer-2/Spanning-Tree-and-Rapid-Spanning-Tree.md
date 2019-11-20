---
title: Spanning Tree and Rapid Spanning Tree
author: Cumulus Networks
weight: 117
aliases:
 - /display/DOCS/Spanning+Tree+and+Rapid+Spanning+Tree
 - /pages/viewpage.action?pageId=8366412
product: Cumulus Linux
version: '4.0'
---
Spanning tree protocol (STP) is always recommended in layer 2 topologies as it prevents bridge loops and broadcast radiation on a bridged network. STP also provides redundant links for automatic failover when an active link fails. STP is enabled by default for both VLAN-aware and traditional bridges.

## Supported Modes

Cumulus Linux supports RSTP, PVST, and PVRST modes:

- Bridges configured in *[VLAN-aware](../../Layer-2/Ethernet-Bridging-VLANs/VLAN-aware-Bridge-Mode/)* mode operate **only** in RSTP mode.
- Bridges configured in [*traditional* mode](../../Layer-2/Ethernet-Bridging-VLANs/Traditional-Bridge-Mode/) operate in both PVST and PVRST. The default is set to PVRST. Each traditional bridge has its own separate STP instance.

### STP for a VLAN-aware Bridge

VLAN-aware bridges only operate in RSTP mode. STP bridge protocol data units (BPDUs) are transmitted on the native VLAN.

If a bridge running RSTP (802.1w) receives a common STP (802.1D) BPDU, it falls back to 802.1D operation automatically. RSTP interoperates with MST seamlessly, creating a single instance of spanning tree, which transmits BPDUs on the native VLAN. RSTP treats the MST domain as one giant switch.

{{%notice note%}}

When connecting a VLAN-aware bridge to a proprietary PVST+ switch using STP, VLAN 1 must be allowed on all 802.1Q trunks that interconnect them, regardless of the configured *native* VLAN. Only VLAN 1 enables the
switches to address the BPDU frames to the IEEE multicast MAC address. The proprietary switch might be configured like this:

```
switchport trunk allowed vlan 1-100
```

{{%/notice%}}

### STP for a Traditional Mode Bridge

Per VLAN Spanning Tree (PVST) creates a spanning tree instance for a bridge. Rapid PVST (PVRST) supports RSTP enhancements for each spanning tree instance. To use PVRST with a traditional bridge, you must create a bridge corresponding to the untagged native VLAN and all the physical switch ports must be part of the same VLAN.

{{%notice note%}}

For maximum interoperability, when connected to a switch that has a native VLAN configuration, the native VLAN **must** be configured to be VLAN 1 only.

{{%/notice%}}

## Show Bridge and STP Status and Logs

To check STP status for a bridge:

<details>

<summary>NCLU Commands </summary>

Run the `net show bridge spanning-tree` command:

```
cumulus@switch:~$ net show bridge spanning-tree
bridge CIST info
  enabled         yes
  bridge id       1.000.44:38:39:FF:40:90
  designated root 1.000.44:38:39:FF:40:90
  regional root   1.000.44:38:39:FF:40:90
  root port       none
  path cost     0          internal path cost   0
  max age       20         bridge max age       20
  forward delay 15         bridge forward delay 15
  tx hold count 6          max hops             20
  hello time    2          ageing time          300
  force protocol version     rstp
  time since topology change 253343s
  topology change count      4
  topology change            no
  topology change port       peerlink
  last topology change port  leaf03-04

bridge:exit01-02 CIST info
  enabled            no                      role                 Disabled
  port id            8.004                   state                discarding
  external port cost 305                     admin external cost  0
  internal port cost 305                     admin internal cost  0
  designated root    1.000.44:38:39:00:00:27 dsgn external cost   0
  dsgn regional root 1.000.44:38:39:00:00:27 dsgn internal cost   0
  designated bridge  1.000.44:38:39:00:00:27 designated port      8.004
  admin edge port    no                      auto edge port       yes
  oper edge port     no                      topology change ack  no
  point-to-point     yes                     admin point-to-point auto
  restricted role    no                      restricted TCN       no
  port hello time    2                       disputed             no
  bpdu guard port    no                      bpdu guard error     no
  network port       no                      BA inconsistent      no
  Num TX BPDU        2                       Num TX TCN           0
  Num RX BPDU        0                       Num RX TCN           0
  Num Transition FWD 0                       Num Transition BLK   2
  bpdufilter port    no
  clag ISL           no                      clag ISL Oper UP     no
  clag role          primary                 clag dual conn mac   00:00:00:00:00:00
  clag remote portID F.FFF                   clag system mac      44:38:39:FF:40:90
bridge:leaf01-02 CIST info
  enabled            yes                     role                 Designated
  port id            8.003                   state                forwarding
  external port cost 10000                   admin external cost  0
  internal port cost 10000                   admin internal cost  0
  designated root    1.000.44:38:39:FF:40:90 dsgn external cost   0
  dsgn regional root 1.000.44:38:39:FF:40:90 dsgn internal cost   0
  designated bridge  1.000.44:38:39:FF:40:90 designated port      8.003
  admin edge port    no                      auto edge port       yes
  oper edge port     no                      topology change ack  no
  point-to-point     yes                     admin point-to-point auto
  restricted role    no                      restricted TCN       no
  port hello time    2                       disputed             no
  bpdu guard port    no                      bpdu guard error     no
  network port       no                      BA inconsistent      no
  Num TX BPDU        253558                  Num TX TCN           2
  Num RX BPDU        253373                  Num RX TCN           4
  Num Transition FWD 126675                  Num Transition BLK   126694
  bpdufilter port    no
  clag ISL           no                      clag ISL Oper UP     no
  clag role          primary                 clag dual conn mac   44:38:39:FF:40:94
  clag remote portID F.FFF                   clag system mac      44:38:39:FF:40:90
bridge:leaf03-04 CIST info
  enabled            yes                     role                 Designated
  port id            8.001                   state                forwarding
  external port cost 10000                   admin external cost  0
  internal port cost 10000                   admin internal cost  0
  designated root    1.000.44:38:39:FF:40:90 dsgn external cost   0
  dsgn regional root 1.000.44:38:39:FF:40:90 dsgn internal cost   0
  designated bridge  1.000.44:38:39:FF:40:90 designated port      8.001
  admin edge port    no                      auto edge port       yes
  oper edge port     no                      topology change ack  no
  point-to-point     yes                     admin point-to-point auto
  restricted role    no                      restricted TCN       no
  port hello time    2                       disputed             no
  bpdu guard port    no                      bpdu guard error     no
  network port       no                      BA inconsistent      no
  Num TX BPDU        130960                  Num TX TCN           6
  Num RX BPDU        4                       Num RX TCN           1
  Num Transition FWD 2                       Num Transition BLK   1
  bpdufilter port    no
  clag ISL           no                      clag ISL Oper UP     no
  clag role          primary                 clag dual conn mac   44:38:39:FF:40:93
  clag remote portID F.FFF                   clag system mac      44:38:39:FF:40:90
bridge:peerlink CIST info
  enabled            yes                     role                 Designated
  port id            F.002                   state                forwarding
  external port cost 10000                   admin external cost  0
  internal port cost 10000                   admin internal cost  0
  designated root    1.000.44:38:39:FF:40:90 dsgn external cost   0
  dsgn regional root 1.000.44:38:39:FF:40:90 dsgn internal cost   0
  designated bridge  1.000.44:38:39:FF:40:90 designated port      F.002
  admin edge port    no                      auto edge port       yes
  oper edge port     no                      topology change ack  no
  point-to-point     yes                     admin point-to-point auto
  restricted role    no                      restricted TCN       no
  port hello time    2                       disputed             no
  bpdu guard port    no                      bpdu guard error     no
  network port       no                      BA inconsistent      no
  Num TX BPDU        126700                  Num TX TCN           2
  Num RX BPDU        6                       Num RX TCN           3
  Num Transition FWD 2                       Num Transition BLK   1
  bpdufilter port    no
  clag ISL           yes                     clag ISL Oper UP     yes
  clag role          primary                 clag dual conn mac   00:00:00:00:00:00
  clag remote portID F.FFF                   clag system mac      44:38:39:FF:40:90
```

</details>

<details>

<summary>Linux Commands </summary>

The `mstpctl` utility provided by the `mstpd` service configures STP. The `mstpd` daemon is an open source project used by Cumulus Linux to implement IEEE802.1D 2004 and IEEE802.1Q 2011.

The `mstpd` daemon starts by default when the switch boots. The `mstpd` logs and errors are located in `/var/log/syslog`.

{{%notice warning%}}

`mstpd` is the preferred utility for interacting with STP on Cumulus Linux. `brctl` also provides certain methods for configuring STP; however, they are not as complete as the tools offered in `mstpd` and output from brctl can be misleading in some cases.

{{%/notice%}}

To show the bridge state, run the `brctl show` command:

```
cumulus@switch:~$ sudo brctl show
  bridge name     bridge id               STP enabled     interfaces
  bridge          8000.001401010100       yes             swp1
                                                          swp4
                                                          swp5
```

To show the `mstpd` bridge port state, run the `mstpctl showport bridge`command:

```
cumulus@switch:~$ sudo mstpctl showport bridge
  E swp1 8.001 forw F.000.00:14:01:01:01:00 F.000.00:14:01:01:01:00 8.001 Desg
    swp4 8.002 forw F.000.00:14:01:01:01:00 F.000.00:14:01:01:01:00 8.002 Desg
  E swp5 8.003 forw F.000.00:14:01:01:01:00 F.000.00:14:01:01:01:00 8.003 Desg
```

</details>

## Customize Spanning Tree Protocol

There are a number of ways to customize STP in Cumulus Linux. Exercise extreme caution with the settings below to prevent malfunctions in STP loop avoidance.

### Spanning Tree Priority

If you have a multiple spanning tree instance (MSTI 0, also known as a common spanning tree, or CST), you can set the *tree priority* for a bridge. The bridge with the lowest priority is elected the *root bridge*. The priority must be a number between *0* and *61440,* and must be a multiple of 4096. The default is *32768*.

To set the tree priority, run the following commands:

<details>

<summary>NCLU Commands </summary>

The following example command sets the tree priority to 8192:

```
cumulus@switch:~$ net add bridge stp treeprio 8192
cumulus@switch:~$ net pending
cumulus@switch:~$ net commit
```

</details>

<details>

<summary>Linux Commands </summary>

Configure the tree priority (`mstpctl-treeprio`) under the *bridge* stanza in the `/etc/network/interfaces` file. The following example command sets the tree priority to 8192:

```
cumulus@switch:~$ sudo nano /etc/network/interfaces
...
auto bridge
iface bridge
    # bridge-ports includes all ports related to VxLAN and CLAG.
    # does not include the Peerlink.4094 subinterface
    bridge-ports bond01 bond02 peerlink vni13 vni24 vxlan4001
    bridge-pvid 1
    bridge-vids 13 24
    bridge-vlan-aware yes
    mstpctl-treeprio 8192
...
```

Run the `ifreload -a` command to load the new configuration:

``` 
cumulus@switch:~$ ifreload -a
```

</details>

{{%notice note%}}

Cumulus Linux supports MSTI 0 only. It does not support MSTI 1 through 15.

{{%/notice%}}

### PortAdminEdge (PortFast Mode)

*PortAdminEdge* is equivalent to the PortFast feature offered by other vendors. It enables or disables the *initial edge state* of a port in a bridge.

All ports configured with PortAdminEdge bypass the listening and learning states to move immediately to forwarding.

{{%notice warning%}}

PortAdminEdge mode might cause loops if it is not used with the [BPDU guard](#bpdu-guard) feature.

{{%/notice%}}

It is common for edge ports to be configured as access ports for a simple end host; however, this is not mandatory. In the data center, edge ports typically connect to servers, which might pass both tagged and untagged traffic.

To configure PortAdminEdge mode:

<details>

<summary>NCLU Commands </summary>

The following example commands configure PortAdminEdge and BPDU guard for swp5.

```
cumulus@switch:~$ net add interface swp5 stp bpduguard
cumulus@switch:~$ net add interface swp5 stp portadminedge
cumulus@switch:~$ net pending
cumulus@switch:~$ net commit
```

</details>

<details>

<summary>Linux Commands </summary>

Configure PortAdminEdge and BPDU guard under the switch port interface stanza in the `/etc/network/interfaces` file. The following example configures PortAdminEdge and BPD guard on swp5.

```
cumulus@switch:~$ sudo nano /etc/netowrk/interfaces
...
auto swp5
iface swp5
    mstpctl-bpduguard yes
    mstpctl-portadminedge yes
...
```

Run the `ifreload -a` command to load the new configuration:

```
cumulus@switch:~$ sudo ifreload -a
```

**Runtime Configuration (Advanced)**

{{%notice warning%}}

A runtime configuration is non-persistent, which means the configuration you create here does not persist after you reboot the switch.

{{%/notice%}}

To configure PortAdminEdge and BPDU guard at runtime, run the following commands:

```
cumulus@switch:~$ sudo mstpctl setportadminedge br2 swp1 yes
cumulus@switch:~$ sudo mstpctl setbpduguard br2 swp1 yes
```

</details>

### PortAutoEdge

*PortAutoEdge* is an enhancement to the standard PortAdminEdge (PortFast) mode, which allows for the automatic detection of edge ports. PortAutoEdge enables and disables the *auto transition* to and from the edge state of a port in a bridge.

{{%notice note%}}

Edge ports and access ports are not the same. Edge ports transition directly to the forwarding state and skip the listening and learning stages. Upstream topology change notifications are not generated when an edge port link changes state. Access ports only forward untagged traffic; however, there is no such restriction on edge ports, which can forward both tagged and untagged traffic.

{{%/notice%}}

When a BPDU is received on a port configured with PortAutoEdge, the port ceases to be in the edge port state and transitions into a normal STP port. When BPDUs are no longer received on the interface, the port becomes an edge port, and transitions through the discarding and learning states before resuming forwarding.

PortAutoEdge is enabled by default in Cumulus Linux.

To disable PortAutoEdge for an interface:

<details>

<summary>NCLU Commands </summary>

The following example commands disable PortAutoEdge on swp1:

```
cumulus@switch:~$ net add interface swp1 stp portautoedge no
cumulus@switch:~$ net pending
cumulus@switch:~$ net commit
```

</details>

<details>

<summary>Linux Commands </summary>

Edit the switch port interface stanza in the `/etc/network/interfaces` file to add the `mstpctl-portautoedge no` line. The following example disables PortAutoEdge on swp1:

```
cumulus@switch:~$ sudo nano /etc/network/interfaces
...
auto swp1
iface swp1
    alias to Server01
    # Port to Server02
    mstpctl-portautoedge no
...
```

Run `ifreload -a` to load the new configuration:

```
cumulus@switch:~$ sudo ifreload -a
```

</details>

To re-enable PortAutoEdge for an interface:

<details>

<summary>NCLU Commands </summary>

The following example commands re-enable PortAutoEdge on swp1:

```
cumulus@switch:~$ net del interface swp1 stp portautoedge no
cumulus@switch:~$ net pending
cumulus@switch:~$ net commit
```

</details>

<details>

<summary>Linux Commands </summary>

Edit the switch port interface stanza in the `/etc/network/interfaces` file to remove `mstpctl-portautoedge no`.

Run `ifreload -a` to load the new configuration:

```
cumulus@switch:~$ sudo ifreload -a
```

</details>

### BPDU Guard

You can configure *BPDU guard* (Bridge Protocol Data Unit) to protect the spanning tree topology from unauthorized switches affecting the forwarding path. For example, when someone adds a new switch to an access port off a leaf switch and this new switch is configured with a low priority, it might become the new root switch and affect the forwarding path for the entire layer 2 topology.

To configure BPDU guard:

<details>

<summary>NCLU Commands </summary>

The following example commands set BPDU guard for swp5:

```
cumulus@switch:~$ net add interface swp5 stp bpduguard
cumulus@switch:~$ net pending
cumulus@switch:~$ net commit
```

</details>

<details>

<summary>Linux Commands </summary>

Edit the switch port interface stanza in the `/etc/network/interfaces` file and add the `mstpctl-bpduguard yes` line. The following example sets BPDU guard for interface swp5:

```
cumulus@switch:~$ sudo nano /etc/network/interfaces
...
auto swp5
iface swp5
    mstpctl-bpduguard yes
...
```

Run `ifreload -a` to load the new configuration:

```
cumulus@switch:~$ sudo ifreload -a
```

</details>

If a BPDU is received on the port, STP brings down the port and logs an error in `/var/log/syslog`. The following is a sample error:

```
mstpd: error, MSTP_IN_rx_bpdu: bridge:bond0 Recvd BPDU on BPDU Guard Port - Port Down
```

To determine whether BPDU guard is configured, or if a BPDU has been received:

<details>

<summary>NCLU Commands </summary>

```
cumulus@switch:~$ net show bridge spanning-tree | grep bpdu
  bpdu guard port    yes                bpdu guard error     yes
```

</details>

<details>

<summary>Linux Commands </summary>

```
cumulus@switch:~$ mstpctl showportdetail bridge bond0
bridge:bond0 CIST info
  enabled            no                      role                 Disabled
  port id            8.001                   state                discarding
  external port cost 305                     admin external cost  0
  internal port cost 305                     admin internal cost  0
  designated root    8.000.6C:64:1A:00:4F:9C dsgn external cost   0
  dsgn regional root 8.000.6C:64:1A:00:4F:9C dsgn internal cost   0
  designated bridge  8.000.6C:64:1A:00:4F:9C designated port      8.001
  admin edge port    no                      auto edge port       yes
  oper edge port     no                      topology change ack  no
  point-to-point     yes                     admin point-to-point auto
  restricted role    no                      restricted TCN       no
  port hello time    10                      disputed             no
  bpdu guard port    yes                      bpdu guard error     yes
  network port       no                      BA inconsistent      no
  Num TX BPDU        3                       Num TX TCN           2
  Num RX BPDU        488                     Num RX TCN           2
  Num Transition FWD 1                       Num Transition BLK   2
  bpdufilter port    no
  clag ISL           no                      clag ISL Oper UP     no
  clag role          unknown                 clag dual conn mac   0:0:0:0:0:0
  clag remote portID F.FFF                   clag system mac      0:0:0:0:0:0
```

</details>

The only way to recover a port that has been placed in the disabled state is to manually bring up the port with the `sudo ifup <interface>` command. See [Interface Configuration and Management](../../Layer-1-and-Switch-Ports/Interface-Configuration-and-Management/) for more information about `ifupdown`.

{{%notice note%}}

Bringing up the disabled port does not correct the problem if the configuration on the connected end-station has not been resolved.

{{%/notice%}}

### Bridge Assurance

On a point-to-point link where RSTP is running, if you want to detect unidirectional links and put the port in a discarding state (in error), you can enable bridge assurance on the port by enabling a port type network. The port is then in a bridge assurance inconsistent state until a BPDU is received from the peer. You need to configure the port type network on both ends of the link for bridge assurance to operate properly.

Bridge assurance is disabled by default.

To enable bridge assurance on an interface:

<details>

<summary>NCLU Commands </summary>

The following example commands enable bridge assurance on swp1:

```
cumulus@switch:~$ net add interface swp1 stp portnetwork
cumulus@switch:~$ net pending
cumulus@switch:~$ net commit
```

</details>

<details>

<summary>Linux Commands </summary>

Edit the switch port interface stanza in the `/etc/network/interfaces` file and add the `mstpctl-portnetwork yes` line. The following example enables bridge assurance on swp5:

```
cumulus@switch:~$ sudo nano /etc/network/interfaces
...
auto swp5
iface swp5 
    mstpctl-portnetwork yes
...
```

Run `ifreload -a` to load the new configuration:

```
cumulus@switch:~$ sudo ifreload -a
```

**Runtime Configuration (Advanced)**

{{%notice warning%}}

A runtime configuration is non-persistent, which means the configuration you create here does not persist after you reboot the switch.

{{%/notice%}}

To enable bridge assurance at runtime, run `mstpctl`:

```
cumulus@switch:~$ sudo mstpctl setportnetwork br1007 swp1.1007 yes

cumulus@switch:~$ sudo mstpctl showportdetail br1007 swp1.1007 | grep network
  network port       yes                     BA inconsistent      yes
```

</details>

To monitor logs for bridge assurance messages, run the following command:

```
cumulus@switch:~$ sudo grep -in assurance /var/log/syslog | grep mstp
  1365:Jun 25 18:03:17 mstpd: br1007:swp1.1007 Bridge assurance inconsistent
```

### BPDU Filter

You can enable `bpdufilter` on a switch port, which filters BPDUs in both directions. This disables STP on the port as no BPDUs are transiting.

{{%notice warning%}}

Using BDPU filter might cause layer 2 loops. Use this feature deliberately and with extreme caution.

{{%/notice%}}

To configure the BPDU filter on an interface:

<details>

<summary>NCLU Commands </summary>

The following example commands configure the BPDU filter on swp6:

```
cumulus@switch:~$ net add interface swp6 stp portbpdufilter
cumulus@switch:~$ net pending
cumulus@switch:~$ net commit
```

</details>

<details>

<summary>Linux Commands </summary>

Edit the switch port interface stanza in the `/etc/network/interfaces` file and add the `mstpctl-portbpdufilter yes` line. The following example configures BPDU filter on swp6:

```
cumulus@switch:~$ sudo nano /etc/network/interfaces
...
auto swp6
iface swp6
    mstpctl-portbpdufilter yes
...
```

Run `ifreload -a` to load the new configuration:

```
cumulus@switch:~$ sudo ifreload -a
```

**Runtime Configuration (Advanced)**

{{%notice warning%}}

A runtime configuration is non-persistent, which means the configuration you create here does not persist after you reboot the switch.

{{%/notice%}}

To enable BPDU filter at runtime, run `mstpctl`. For example:

```
cumulus@switch:~$ sudo mstpctl setportbpdufilter br100 swp1.100=yes swp2.100=yes
```

</details>

### Storm Control

Storm control provides protection against excessive inbound BUM (broadcast, unknown unicast, multicast) traffic on layer 2 switch port interfaces, which can cause poor network performance.

You configure storm control for each physical port by [configuring `switchd`](../../System-Configuration/Configuring-switchd/). For example, to enable unicast and multicast storm control at 400 packets per second (pps) and 3000 pps for swp1, run the following commands:

```
cumulus@switch:~$ sudo sh -c 'echo 400 > /cumulus/switchd/config/interface/swp1/storm_control/unknown_unicast'
cumulus@switch:~$ sudo sh -c 'echo 3000 > /cumulus/switchd/config/interface/swp1/storm_control/multicast'
```

### Spanning Tree Parameter List

Spanning tree parameters are defined in the IEEE [802.1D](http://standards.ieee.org/findstds/standard/802.1D-2004.html), [802.1Q](http://standards.ieee.org/findstds/standard/802.1Q-2018.html) specifications.

The table below describes the STP configuration parameters available in Cumulus Linux. For a comparison of STP parameter configuration between `mstpctl` and other vendors, [read this knowledge base article](https://support.cumulusnetworks.com/hc/en-us/articles/206908397).

{{%notice note%}}

Most of these parameters are blacklisted in the `ifupdown_blacklist` section of the `/etc/netd.conf` file. Before you configure these parameters, you must [edit the file](../../System-Configuration/Network-Command-Line-Utility-NCLU/) to remove them from the blacklist.

{{%/notice%}}

| Parameter | <div style="width:250px">NCLU Command</div>| Description |
|-----------|----------|---------|
| `mstpctl-maxage` | `net add bridge stp maxage <seconds>`| Sets the maximum age of the bridge in seconds. The default is 20. The maximum age must meet the condition 2 * (Bridge Forward Delay - 1 second) >= Bridge Max Age. |
| `mstpctl-ageing` | `net add bridge stp ageing <seconds>` | Sets the Ethernet (MAC) address ageing time for the bridge in seconds when the running version is STP, but not RSTP/MSTP. The default is 1800. |
| `mstpctl-fdelay` | `net add bridge stp fdelay <seconds>` | Sets the bridge forward delay time in seconds. The default value is 15. The bridge forward delay must meet the condition 2 * (Bridge Forward Delay - 1 second) >= Bridge Max Age. |
| `mstpctl-maxhops` | `net add bridge stp maxhops <max-hops>` | Sets the maximum hops for the bridge. The default is 20. |
| `mstpctl-txholdcount` |`net add bridge stp txholdcount <hold-count>` | Sets the bridge transmit hold count. The default value is 6. |
| `mstpctl-forcevers` | `net add bridge stp forcevers RSTP`\|`STP` | Sets the force STP version of the bridge to either RSTP/STP. MSTP is not supported currently. The default is RSTP. |
| `mstpctl-treeprio` | `net add bridge stp treeprio <priority>` | Sets the tree priority of the bridge for an MSTI (multiple spanning tree instance). The priority value is a number between 0 and 61440 and must be a multiple of 4096. The bridge with the lowest priority is elected the root bridge. The default is 32768.<br>**Note**: Cumulus Linux supports MSTI 0 only. It does not support MSTI 1 through 15. |
| `mstpctl-hello` | `net add bridge stp hello <seconds>` | Sets the bridge hello time in seconds. The default is 2. |
| `mstpctl-portpathcost` | `net add interface <interface> stp portpathcost <cost>` | Sets the port cost of the interface. The default is 0.<br>mstpd supports only long mode; 32 bits for the path cost. |
|`mstpctl-treeportprio` | `net add interface <interface> stp treeportprio <priority>`| Sets the priority of the interface for the MSTI. The priority value is a number between 0 and 240 and must be a multiple of 16. The default is 128.<br>**Note**: Cumulus Linux supports MSTI 0 only. It does not support MSTI 1 through 15.|
| `mstpctl-portadminedge` | `net add interface <interface> stp portadminedge` | Enables or disables the initial edge state of the interface in the bridge. The default is no.<br>In NCLU, to use a setting other than the default, you must specify this attribute without setting an option. |
| `mstpctl-portautoedge` | `net add interface <interface> stp portautoedge` | Enables or disables the auto transition to and from the edge state of the interface in the bridge. PortAutoEdge is enabled by default.<br>portautoedge is an enhancement to the standard PortAdminEdge (PortFast) mode, which allows for the automatic detection of edge ports.<br>**Note**: Edge ports and access ports are not the same thing. Edge ports transition directly to the forwarding state and skip the listening and learning stages. Upstream topology change notifications are not generated when an edge port's link changes state. Access ports only forward untagged traffic; however, there is no such restriction on edge ports, which can forward both tagged and untagged traffic.<br>When a BPDU is received on a port configured with PortAutoEdge, the port ceases to be in the edge port state and transitions into a normal STP port.<br>When BPDUs are no longer received on the interface, the port becomes an edge port, and transitions through the discarding and learning states before resuming forwarding. |
| `mstpctl-portp2p` | `net add interface <interface> stp portp2p yes`\|`no` | Enables or disables the point-to-point detection mode of the interface in the bridge. |
| `mstpctl-portrestrrole` | `net add interface <interface> stp portrestrrole` | Enables or disables the ability of the interface in the bridge to take the root role. The default is no.<br>To enable this feature with the NCLU command, you specify this attribute without an option (portrestrrole). To enable this feature by editing the /etc/network/interfaces file, you specify this attribute with yes (mstpctl-portrestrrole yes). |
| `mstpctl-portrestrtcn` | `net add interface <interface> stp portrestrtcn` | Enables or disables the ability of the interface in the bridge to propagate received topology change notifications. The default is no. |
| `mstpctl-portnetwork` | `net add interface <interface> stp portnetwork` | Enables or disables the bridge assurance capability for a network interface. The default is no. |
| `mstpctl-bpduguard` | `net add interface <interface> stp bpduguard` | Enables or disables the BPDU guard configuration of the interface in the bridge. The default is no. See above. |
| `mstpctl-portbpdufilter` | `net add interface <interface> stp portbpdufilter`| Enables or disables the BPDU filter functionality for an interface in the bridge. The default is no. |
| `mstpctl-treeportcost` | `net add interface <interface> stp treeportcost <port-cost>` | Sets the spanning tree port cost to a value from 0 to 255. The default is 0. |

## Caveats and Errata

MSTP is not supported currently because Cumulus Linux only supports MSTI 0 (not MSTI 1 through 15). However, interoperability with MSTP networks can be accomplished using PVRSTP or PVSTP.

## Related Information

The source code for `mstpd` and `mstpctl` was written by [Vitalii Demianets](mailto:vitas%40nppfactor.kiev.ua) and is hosted at the URL below.

- [GitHub - mstpd project](https://github.com/mstpd/mstpd)
- [Wikipedia - Spanning Tree Protocol](http://en.wikipedia.org/wiki/Spanning_Tree_Protocol)
- brctl(8)
- bridge-utils-interfaces(5)
- ifupdown-addons-interfaces(5)
- mstpctl(8)
- mstpctl-utils-interfaces(5)
