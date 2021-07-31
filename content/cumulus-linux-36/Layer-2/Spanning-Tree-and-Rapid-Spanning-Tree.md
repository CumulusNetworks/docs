---
title: Spanning Tree and Rapid Spanning Tree
author: Cumulus Networks
weight: 115
pageID: 8362181
---
Spanning tree protocol (STP) is always recommended in layer 2
topologies, as it prevents bridge loops and broadcast radiation on a
bridged network. STP also provides redundant links for automatic
failover when an active link fails. STP is disabled by default on
bridges in Cumulus Linux.

## Supported Modes

The STP modes Cumulus Linux supports vary depending upon whether the
[traditional or VLAN-aware bridge driver mode](/cumulus-linux-36/Layer-2/Ethernet-Bridging-VLANs/) 
is in use.

  - Bridges configured in
    *[VLAN-aware](/cumulus-linux-36/Layer-2/Ethernet-Bridging-VLANs/VLAN-aware-Bridge-Mode)*
    mode operate **only** in RSTP mode.
  - Bridges configured in 
    *[traditional mode](/cumulus-linux-36/Layer-2/Ethernet-Bridging-VLANs/Traditional-Bridge-Mode/)* 
    operate in PVST and PVRST mode. The default is set to PVRST. Each 
    traditional bridge has its own separate STP instance.

{{%notice note%}}

NCLU commands are not supported for traditional-mode bridges in Cumulus
Linux 3.6.1 and earlier.

{{%/notice%}}

### STP for a VLAN-aware Bridge

*[VLAN-aware](/cumulus-linux-36/Layer-2/Ethernet-Bridging-VLANs/VLAN-aware-Bridge-Mode)*
bridges only operate in RSTP mode. STP bridge protocol data units
(BPDUs) are transmitted on the native VLAN.

If a bridge running RSTP (802.1w) receives a common STP (802.1D) BPDU,
it will automatically fall back to 802.1D operation. RSTP interoperates
with MST seamlessly, creating a single instance of spanning tree, which
transmits BPDUs on the native VLAN. RSTP treats the MST domain as if it
were one giant switch.

{{%notice tip%}}

As of version 3.2.1, STP is enabled by default in Cumulus Linux. There
is no need to specify `bridge-stp on` for the bridge any more.

{{%/notice%}}

{{%notice note%}}

When connecting a 
[VLAN-aware bridge](../Ethernet-Bridging-VLANs/VLAN-aware-Bridge-Mode)
to a proprietary PVST+ switch using STP, VLAN 1 must be allowed on all
802.1Q trunks that interconnect them, regardless of the configured
"native" VLAN. This is because only VLAN 1 enables the switches to address
the BPDU frames to the IEEE multicast MAC address. The proprietary
switch might be configured like this: 

    switchport trunk allowed vlan 1-100

{{%/notice%}}

### STP within a Traditional Mode Bridge

Per VLAN Spanning Tree (PVST) creates a spanning tree instance for a
bridge. Rapid PVST (PVRST) supports RSTP enhancements for each spanning
tree instance. In order to use PVRST with a traditional bridge, a bridge
corresponding to the untagged native VLAN must be created, and all the
physical switch ports must be part of the same VLAN.

{{%notice note%}}

When connected to a switch that has a native VLAN configuration, the
native VLAN **must** be configured to be VLAN 1 only for maximum
interoperability.

{{%/notice%}}

## Viewing Bridge and STP Status/Logs

To check STP status for a bridge, run `net show bridge spanning-tree`:

<details>
<summary>Click to reveal the output ... </summary>

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
</details>

### Using Linux to Check Spanning Tree Status (Advanced)

<details>
<summary>Using Linux to check STP status ... </summary>

`mstpctl` is the utility provided by the `mstpd` service to configure
STP. The `mstpd` daemon is an open source project used by Cumulus Linux
to implement IEEE802.1D 2004 and IEEE802.1Q 2011.

`mstpd` is started by default when the switch boots. `mstpd` logs and
errors are located in `/var/log/syslog`.

{{%notice warning%}}

`mstpd` is the preferred utility for interacting with STP on Cumulus
Linux. `brctl` also provides certain methods for configuring STP;
however, they are not as complete as the tools offered in `mstpd` and
[output from brctl can be misleading]({{<ref "/knowledge-base/Configuration-and-Usage/Network-Interfaces/brctl-showstp-Shows-Carrier-Down-Ports-as-Blocking" >}})
in some cases.

{{%/notice%}}

To get the bridge state, use:

    cumulus@switch:~$ sudo brctl show
     bridge name     bridge id               STP enabled     interfaces
     bridge          8000.001401010100       yes             swp1
                                                             swp4
                                                             swp5

To get the `mstpd` bridge state, use:

    cumulus@switch:~$ net show bridge spanning-tree
     bridge CIST info
      enabled         yes
      bridge id       F.000.00:14:01:01:01:00
      designated root F.000.00:14:01:01:01:00
      regional root   F.000.00:14:01:01:01:00
      root port       none
      path cost     0          internal path cost   0
      max age       20         bridge max age       20
      forward delay 15         bridge forward delay 15
      tx hold count 6          max hops             20
      hello time    2          ageing time          200
      force protocol version     rstp
      time since topology change 90843s
      topology change count      4
      topology change            no
      topology change port       swp4
      last topology change port  swp5

To get the `mstpd` bridge port state, use:

    cumulus@switch:~$ sudo mstpctl showport bridge
     E swp1 8.001 forw F.000.00:14:01:01:01:00 F.000.00:14:01:01:01:00 8.001 Desg
       swp4 8.002 forw F.000.00:14:01:01:01:00 F.000.00:14:01:01:01:00 8.002 Desg
     E swp5 8.003 forw F.000.00:14:01:01:01:00 F.000.00:14:01:01:01:00 8.003 Desg
     
    cumulus@switch:~$ net show bridge spanning-tree
     
    ...
     bridge:swp1 CIST info
      enabled            yes                     role                 Designated
      port id            8.001                   state                forwarding
      external port cost 2000                    admin external cost  0
      internal port cost 2000                    admin internal cost  0
      designated root    F.000.00:14:01:01:01:00 dsgn external cost   0
      dsgn regional root F.000.00:14:01:01:01:00 dsgn internal cost   0
      designated bridge  F.000.00:14:01:01:01:00 designated port      8.001
      admin edge port    no                      auto edge port       yes
      oper edge port     yes                     topology change ack  no
      point-to-point     yes                     admin point-to-point auto
      restricted role    no                      restricted TCN       no
      port hello time    2                       disputed             no
      bpdu guard port    no                      bpdu guard error     no
      network port       no                      BA inconsistent      no
      Num TX BPDU        45772                   Num TX TCN           4
      Num RX BPDU        0                       Num RX TCN           0
      Num Transition FWD 2                       Num Transition BLK   2
</details>

## Customizing Spanning Tree Protocol

There are a number of ways you can customize STP in Cumulus Linux. You
should exercise extreme caution with many of the settings below to
prevent malfunctions in STP's loop avoidance.

### Spanning Tree Priority

If you have a multiple spanning tree instance (MSTI 0, also known as a
common spanning tree, or CST), you can set the *tree priority* for a
bridge. The bridge with the lowest priority is elected the *root
bridge*. The priority must be a number between *0* and *61440* and must
be a multiple of 4096; the default is *32768*.

To set the tree priority, run:

    cumulus@switch:~$ net add bridge stp treeprio 8192
    cumulus@switch:~$ net pending
    cumulus@switch:~$ net commit

{{%notice note%}}

Cumulus Linux supports MSTI 0 only. It does not support MSTI 1 through 15.

{{%/notice%}}

### PortAdminEdge/PortFast Mode

*PortAdminEdge* is equivalent to the PortFast feature offered by other
vendors. It enables or disables the *initial edge state* of a port in a
bridge.

All ports configured with PortAdminEdge bypass the listening and
learning states to move immediately to forwarding.

{{%notice warning%}}

Using PortAdminEdge mode has the potential to cause loops if it is not
accompanied by the [BPDU guard](#bpdu-guard) feature.

{{%/notice%}}

While it is common for edge ports to be configured as access ports for a
simple end host, this is not mandatory. In the data center, edge ports
typically connect to servers, which may pass both tagged and untagged
traffic.

{{%notice info has%}}

**Example VLAN-aware Bridge Configuration**

To configure PortAdminEdge mode, use the `bpduguard` and `portadminedge`
NCLU configuration commands:

    cumulus@switch:~$ net add interface swp5 stp bpduguard
    cumulus@switch:~$ net add interface swp5 stp portadminedge
    cumulus@switch:~$ net pending
    cumulus@switch:~$ net commit

The NCLU commands above create the following code snippet:

    auto swp5
    iface swp5
        mstpctl-bpduguard yes
        mstpctl-portadminedge yes

{{%/notice%}}

{{%notice info has%}}

**Example Traditional Bridge Configuration**

For a bridge in [traditional mode](/cumulus-linux-36/Layer-2/Ethernet-Bridging-VLANs/Traditional-Bridge-Mode/), configure `PortAdminEdge` under the bridge stanza in
`/etc/network/interfaces`:

    auto br2
    iface br2 inet static
      bridge-ports swp1 swp2 swp3 swp4
      mstpctl-bpduguard swp1=yes swp2=yes swp3=yes swp4=yes
      mstpctl-portadminedge swp1=yes swp2=yes swp3=yes swp4=yes

To load the new configuration, run `ifreload -a`:

    cumulus@switch:~$ sudo ifreload -a

{{%/notice%}}

### PortAutoEdge

*PortAutoEdge* is an enhancement to the standard PortAdminEdge
(PortFast) mode, which allows for the automatic detection of edge ports.
PortAutoEdge enables and disables the *auto transition* to/from the edge
state of a port in a bridge.

{{%notice note%}}

Edge ports and access ports are not the same thing. Edge ports
transition directly to the forwarding state and skip the listening and
learning stages. Upstream topology change notifications are not
generated when an edge port's link changes state. Access ports only
forward untagged traffic; however, there is no such restriction on edge
ports, which can forward both tagged and untagged traffic.

{{%/notice%}}

When a BPDU is received on a port configured with portautoedge, the port
ceases to be in the edge port state and transitions into a normal STP
port. When BPDUs are no longer received on the interface, the port
becomes an edge port, and transitions through the discarding and
learning states before resuming forwarding.

PortAutoEdge is enabled by default in Cumulus Linux.

To disable PortAutoEdge for an interface, run the 
`net add interface <port> stp portautoedge no` command. The following 
example disables PortAutoEdge on swp1:

    cumulus@switch:~$ net add interface swp1 stp portautoedge no
    cumulus@switch:~$ net pending
    cumulus@switch:~$ net commit

To reenable PortAutoEdge for an interface, run the the 
`net del interface <port> stp portautoedge no` command. The following example
reenables PortAutoEdge on swp1:

    cumulus@switch:~$ net del interface swp1 stp portautoedge no
    cumulus@switch:~$ net pending
    cumulus@switch:~$ net commit

### BPDU Guard

To protect the spanning tree topology from unauthorized switches
affecting the forwarding path, you can configure *BPDU guard* (Bridge
Protocol Data Unit). One very common example is when someone hooks up a
new switch to an access port off of a leaf switch. If this new switch is
configured with a low priority, it could become the new root switch and
affect the forwarding path for the entire layer 2 topology.

{{%notice info has%}}

**Example BPDU Guard Configuration**

To configure BPDU guard, set the `bpduguard` value for the interface:

    cumulus@switch:~$ net add interface swp5 stp bpduguard
    cumulus@switch:~$ net pending
    cumulus@switch:~$ net commit

This creates the following stanza in the `/etc/network/interfaces` file:

    auto swp5
    iface swp5
        mstpctl-bpduguard yes

{{%/notice%}}

#### Recovering a Port Disabled by BPDU Guard

If a BPDU is received on the port, STP will bring down the port and log
an error in `/var/log/syslog`. The following is a sample error:

    mstpd: error, MSTP_IN_rx_bpdu: bridge:bond0 Recvd BPDU on BPDU Guard Port - Port Down

To determine whether BPDU guard is configured, or if a BPDU has been
received, run:

    cumulus@switch:~$ net show bridge spanning-tree | grep bpdu
     bpdu guard port    yes                     bpdu guard error     yes

The only way to recover a port that has been placed in the disabled
state is to manually un-shut or bring up the port with 
`sudo ifup [port]`, as shown in the example below.

{{%notice note%}}

Bringing up the disabled port does not fix the problem if the
configuration on the connected end-station has not been rectified.

{{%/notice%}}

    cumulus@leaf2$ mstpctl showportdetail bridge bond0
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
     
    cumulus@leaf2$ sudo ifup bond0
     
    cumulus@leaf2$ mstpctl showportdetail bridge bond0
    bridge:bond0 CIST info
      enabled            yes                     role                 Root
      port id            8.001                   state                forwarding
      external port cost 305                     admin external cost  0
      internal port cost 305                     admin internal cost  0
      designated root    8.000.6C:64:1A:00:4F:9C dsgn external cost   0
      dsgn regional root 8.000.6C:64:1A:00:4F:9C dsgn internal cost   0
      designated bridge  8.000.6C:64:1A:00:4F:9C designated port      8.001
      admin edge port    no                      auto edge port       yes
      oper edge port     no                      topology change ack  no
      point-to-point     yes                     admin point-to-point auto
      restricted role    no                      restricted TCN       no
      port hello time    2                       disputed             no
      bpdu guard port    no                      bpdu guard error     no
      network port       no                      BA inconsistent      no
      Num TX BPDU        3                       Num TX TCN           2
      Num RX BPDU        43                      Num RX TCN           1
      Num Transition FWD 1                       Num Transition BLK   0
      bpdufilter port    no                     
      clag ISL           no                      clag ISL Oper UP     no
      clag role          unknown                 clag dual conn mac   0:0:0:0:0:0
      clag remote portID F.FFF                   clag system mac      0:0:0:0:0:0

### Bridge Assurance

On a point-to-point link where RSTP is running, if you want to detect
unidirectional links and put the port in a discarding state (in error),
you can enable bridge assurance on the port by enabling a port type
network. The port would be in a bridge assurance inconsistent state
until a BPDU is received from the peer. You need to configure the port
type network on both the ends of the link in order for bridge assurance
to operate properly.

The default setting for bridge assurance is off. This means that there
is no difference between disabling bridge assurance on an interface and
not configuring bridge assurance on an interface.

{{%notice info has%}}

**Example Bridge Assurance Configuration**

To enable bridge assurance on an interface, add the `portnetwork` option
to the interface:

    cumulus@switch:~$ net add interface swp1 stp portnetwork
    cumulus@switch:~$ net pending
    cumulus@switch:~$ net commit

This creates the following interface stanza:

    auto swp1
    iface swp1
        mstpctl-portnetwork yes

{{%/notice%}}

You can monitor logs for bridge assurance messages by doing the
following:

    cumulus@switch:~$ sudo grep -in assurance /var/log/syslog | grep mstp
     1365:Jun 25 18:03:17 mstpd: br1007:swp1.1007 Bridge assurance inconsistent

### BPDU Filter

You can enable `bpdufilter` on a switch port, which filters BPDUs in
both directions. This effectively disables STP on the port as no BPDUs
are transiting.

{{%notice warning%}}

Using BDPU filter inappropriately can cause layer 2 loops. Use this
feature deliberately and with extreme caution.

{{%/notice%}}

{{%notice info has%}}

**Example BPDU Filter Configuration**

To configure the BPDU filter, add the `portbpdufilter` option to the
interface:

    cumulus@switch:~$ net add interface swp6 stp portbpdufilter
    cumulus@switch:~$ net pending
    cumulus@switch:~$ net commit

These commands create the following stanza in the
`/etc/network/interfaces` file:

    auto swp6
    iface swp6
        mstpctl-portbpdufilter yes

{{%/notice%}}

### Storm Control

*Storm control* provides protection against excessive inbound BUM
(broadcast, unknown unicast, multicast) traffic on layer 2 switch port
interfaces, which can cause poor network performance.

You configure storm control for each physical port by 
[configuring `switchd` BUM parameters](/cumulus-linux-36/System-Configuration/Configuring-switchd).
For example, to enable unicast and multicast storm control at 400
packets per second (pps) and 3000 pps, respectively, for swp1, run the
following:

    cumulus@switch:~$ sudo sh -c 'echo 400 > /cumulus/switchd/config/interface/swp1/storm_control/unknown_unicast'
    cumulus@switch:~$ sudo sh -c 'echo 3000 > /cumulus/switchd/config/interface/swp1/storm_control/multicast'
     

### Configuring Other Spanning Tree Parameters

Spanning tree parameters are defined in the IEEE
[802.1D](https://standards.ieee.org/standard/802_1D-2004.html),
[802.1Q](https://standards.ieee.org/standard/802_1Q-2018.html)
specifications and in the table below.

For a comparison of STP parameter configuration between `mstpctl` and
other vendors, 
[read this knowledge base article]({{<ref "/knowledge-base/Demos-and-Training/Interoperability/Cumulus-Linux-vs-Cisco-IOS-Spanning-Tree-Protocol" >}}).

The table below describes the configuration parameters available.

{{%notice note%}}

You configure these parameters using NCLU on the interfaces, not the
bridge itself. Most of these parameters are blacklisted in `netd.conf`
in the ifupdown\_blacklist; blacklisted parameters are indicated with an
asterisk (\*). You can 
[edit the blacklist](/cumulus-linux-36/System-Configuration/Network-Command-Line-Utility-NCLU/#advanced-configuration)
to remove any of them.

{{%/notice%}}

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Parameter</p></th>
<th><p>NCLU Command<br />
net add interface &lt;interface&gt; stp ...</p></th>
<th><p>Description</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><code>mstpctl-maxage</code></p></td>
<td><p><code>maxage*</code></p></td>
<td><p>Sets the bridge's <em>maximum age</em> to <code>&lt;max_age&gt;</code> seconds. The default is <em>20</em>. The maximum age must meet the condition 2 * (Bridge Forward Delay - 1 second) &gt;= Bridge Max Age.</p></td>
</tr>
<tr class="even">
<td><p><code>mstpctl-ageing</code></p></td>
<td><p><code>ageing*</code></p></td>
<td><p>Sets the Ethernet (MAC) address <em>ageing time</em> in <code>&lt;time&gt;</code> seconds for the bridge when the running version is STP, but not RSTP/MSTP. The default is <em>1800 seconds</em>.</p></td>
</tr>
<tr class="odd">
<td><p><code>mstpctl-fdelay</code></p></td>
<td><p><code>fdelay*</code></p></td>
<td><p>Sets the bridge's <em>bridge forward delay</em> to <code>&lt;time&gt;</code> seconds. The default is <em>15</em>. The bridge forward delay must meet the condition 2 * (Bridge Forward Delay - 1 second) &gt;= Bridge Max Age.</p></td>
</tr>
<tr class="even">
<td><p><code>mstpctl-maxhops</code></p></td>
<td><p><code>maxhops*</code></p></td>
<td><p>Sets the bridge's <em>maximum hops</em> to <code>&lt;max_hops&gt;</code>. The default value is <em>20</em>.</p></td>
</tr>
<tr class="odd">
<td><p><code>mstpctl-txholdcount</code></p></td>
<td><p><code>txholdcount*</code></p></td>
<td><p>Sets the bridge's <em>bridge transmit hold count</em> to <code>&lt;tx_hold_count&gt;</code>. The default is <em>6</em>.</p></td>
</tr>
<tr class="even">
<td><p><code>mstpctl-forcevers</code></p></td>
<td><p><code>forcevers*</code></p></td>
<td><p>Sets the bridge's <em>force STP version</em> to either RSTP/STP. MSTP is not supported currently. The default is <em>RSTP</em>.</p></td>
</tr>
<tr class="odd">
<td><p><code>mstpctl-treeprio</code></p></td>
<td><p><code>treeprio*</code></p></td>
<td><p>Sets the bridge's <em>tree priority</em> to <code>&lt;priority&gt;</code> for an MSTI (multiple spanning tree instance). The priority value is a number between 0 and 61440 and must be a multiple of 4096. The bridge with the lowest priority is elected the <em>root bridge</em>. The default is <em>32768</em>.</p>
<p>{{%notice note%}}</p>
<p>Cumulus Linux supports MSTI 0 only. It does not support MSTI 1 through 15.</p>
<p>{{%/notice%}}</p></td>
</tr>
<tr class="even">
<td><p><code>mstpctl-treeportprio</code></p></td>
<td><p><code>treeportprio*</code></p></td>
<td><p>Sets the <em>priority</em> of port <code>&lt;port&gt;</code> to <code>&lt;priority&gt;</code> for the MSTI. The priority value is a number between 0 and 240 and must be a multiple of 16. The default is <em>128</em>.</p>
<p>{{%notice note%}}</p>
<p>Cumulus Linux supports MSTI 0 only. It does not support MSTI 1 through 15.</p>
<p>{{%/notice%}}</p></td>
</tr>
<tr class="odd">
<td><p><code>mstpctl-hello</code></p></td>
<td><p><code>hello*</code></p></td>
<td><p>Sets the bridge's <em>bridge hello time</em> to <code>&lt;time&gt;</code> seconds. The default is <em>2</em>.</p></td>
</tr>
<tr class="even">
<td><p><code>mstpctl-portpathcost</code></p></td>
<td><p><code>portpathcost*</code></p></td>
<td><p>Sets the <em>port cost</em> of the port <code>&lt;port&gt;</code> in bridge <code>&lt;bridge&gt;</code> to <code>&lt;cost&gt;</code>. The default is <em>0</em>.</p>
<p><code>mstpd</code> supports only long mode; that is, 32 bits for the path cost.</p></td>
</tr>
<tr class="odd">
<td><p><code>mstpctl-portadminedge</code></p></td>
<td><p><code>portadminedge</code></p></td>
<td><p>Enables/disables the <em>initial edge state</em> of the port <code>&lt;port&gt;</code> in bridge <code>&lt;bridge&gt;</code>. The default is <em>no</em>.</p>
<p>{{%notice note%}}</p>
<p>This setting only applies to a bridge in <a href="/cumulus-linux-36/Layer-2/Ethernet-Bridging-VLANs/Traditional-Bridge-Mode">traditional mode</a>; it does not apply to <a href="/cumulus-linux-36/Layer-2/Ethernet-Bridging-VLANs/VLAN-aware-Bridge-Mode">VLAN-aware bridges</a>.</p>
<p>{{%/notice%}}</p></td>
</tr>
<tr class="even">
<td><p><code>mstpctl-portautoedge</code></p></td>
<td><p><code>portautoedge</code></p></td>
<td><p>Enables/disables the <em>auto transition</em> to/from the edge state of the port <code>&lt;port&gt;</code> in bridge <code>&lt;bridge&gt;</code>. The default is <em>yes</em>.</p>
<p><em>portautoedge</em> is an enhancement to the standard PortAdminEdge (PortFast) mode, which allows for the automatic detection of edge ports.</p>
<p>{{%notice note%}}</p>
<p>Edge ports and access ports are not the same thing. Edge ports transition directly to the forwarding state and skip the listening and learning stages. Upstream topology change notifications are not generated when an edge port's link changes state. Access ports only forward untagged traffic; however, there is no such restriction on edge ports, which can forward both tagged and untagged traffic.</p>
<p>{{%/notice%}}</p>
<p>When a BPDU is received on a port configured with portautoedge, the port ceases to be in the edge port state and transitions into a normal STP port.</p>
<p>When BPDUs are no longer received on the interface, the port becomes an edge port, and transitions through the discarding and learning states before resuming forwarding.</p></td>
</tr>
<tr class="odd">
<td><p><code>mstpctl-portp2p</code></p></td>
<td><p><code>portp2p*</code></p></td>
<td><p>Enables/disables the <em>point-to-point detection mode</em> of the port <code>&lt;port&gt;</code> in bridge <code>&lt;bridge&gt;</code>. The default is <em>auto</em>.</p></td>
</tr>
<tr class="even">
<td><p><code>mstpctl-portrestrrole</code></p></td>
<td><p><code>portrestrrole*</code></p></td>
<td><p>Enables/disables the ability of the port <code>&lt;port&gt;</code> in bridge <code>&lt;bridge&gt;</code> to take the <em>root role</em>. The default is <em>no</em>.</p></td>
</tr>
<tr class="odd">
<td><p><code>mstpctl-portrestrtcn</code></p></td>
<td><p><code>portrestrtcn*</code></p></td>
<td><p>Enables/disables the ability of the port <code>&lt;port&gt;</code> in bridge <code>&lt;bridge&gt;</code> to propagate <em>received topology change notifications</em>. The default is <em>no</em>.</p></td>
</tr>
<tr class="even">
<td><p><code>mstpctl-portnetwork</code></p></td>
<td><p><code>portnetwork</code></p></td>
<td><p>Enables/disables the <em>bridge assurance capability</em> for a network port <code>&lt;port&gt;</code> in bridge <code>&lt;bridge&gt;</code>. The default is <em>no</em>.</p></td>
</tr>
<tr class="odd">
<td><p><code>mstpctl-bpduguard</code></p></td>
<td><p><code>bpduguard</code></p></td>
<td><p>Enables/disables the <em>BPDU guard configuration</em> of the port <code>&lt;port&gt;</code> in bridge <code>&lt;bridge&gt;</code>. The default is <em>no</em>.</p></td>
</tr>
<tr class="even">
<td><p><code>mstpctl-portbpdufilter</code></p></td>
<td><p><code>portbpdufilter</code></p></td>
<td><p>Enables/disables the <em>BPDU filter</em> functionality for a port <code>&lt;port&gt;</code> in bridge <code>&lt;bridge&gt;</code>. The default is <em>no</em>.</p></td>
</tr>
<tr class="odd">
<td><p><code>mstpctl-treeportcost</code></p></td>
<td><p><code>treeportcost*</code></p></td>
<td><p>Sets the spanning tree <em>port cost</em> to a value from 0 to 255. The default is <em>0</em>.</p></td>
</tr>
</tbody>
</table>

## Caveats and Errata

  - MSTP is not supported currently since Cumulus Linux only supports
    MSTI 0 (not MSTI 1 through 15). However, interoperability with MSTP
    networks can be accomplished using PVRSTP or PVSTP.

## Related Information

The source code for `mstpd`/`mstpctl` was written by 
[Vitalii Demianets](mailto:vitas%40nppfactor.kiev.ua) and is hosted at the URL
below.

  - [Sourceforge - mstpd project](https://github.com/mstpd/mstpd)
  - [Wikipedia - Spanning Tree Protocol](http://en.wikipedia.org/wiki/Spanning_Tree_Protocol)
  - [IEEE 802.1Q-2018 specification](https://standards.ieee.org/standard/802_1Q-2018.html)
  - brctl(8)
  - bridge-utils-interfaces(5)
  - ifupdown-addons-interfaces(5)
  - mstpctl(8)
  - mstpctl-utils-interfaces(5)
