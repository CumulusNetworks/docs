---
title: Spanning Tree and Rapid Spanning Tree
author: Cumulus Networks
weight: 71
aliases:
 - /display/RMP31/Spanning+Tree+and+Rapid+Spanning+Tree
 - /pages/viewpage.action?pageId=5122792
pageID: 5122792
product: Cumulus RMP
version: 3.1.2
imgData: cumulus-rmp-312
siteSlug: cumulus-rmp-312
---
Spanning tree protocol (STP) is always recommended in layer 2
topologies, as it prevents bridge loops and broadcast radiation on a
bridged network.

The `mstpd` daemon is an open source project used by Cumulus RMP to
implement IEEE802.1D 2004 and IEEE802.1Q 2011. STP is disabled by
default on bridges in Cumulus RMP.

To enable STP, configure `brctl stp <bridge> on`.

## <span>Commands</span>

  - brctl

  - mstpctl

`mstpctl` is a utility to configure STP. `mstpd` is started by default
on bootup. `mstpd` logs and errors are located in `/var/log/daemon.log`.

## <span>Supported Modes</span>

The STP modes Cumulus RMP supports vary depending upon whether the
[traditional or VLAN-aware bridge driver
mode](/version/cumulus-rmp-312/Layer_1_and_Layer_2_Features/Ethernet_Bridging_-_VLANs/)
is in use.

For a bridge configured in *traditional* mode, PVST and PVRST are
supported, with the default set to PVRST. Each traditional mode bridge
has its own separate STP instance.

Bridges configured in
*[VLAN-aware](/version/cumulus-rmp-312/Layer_1_and_Layer_2_Features/Ethernet_Bridging_-_VLANs/VLAN-aware_Bridge_Mode_for_Large-scale_Layer_2_Environments)*
mode operate **only** in RSTP mode.

## <span>Configuring STP within a Traditional Mode Bridge</span>

### <span>Creating a Bridge and Configuring PVRST</span>

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

To create a traditional model bridge, configure the bridge stanza under
`/etc/network/interfaces`. More information on configuring bridges [can
be found
here](/version/cumulus-rmp-312/Layer_1_and_Layer_2_Features/Ethernet_Bridging_-_VLANs/).
To enable STP on the bridge, include the keyword `bridge-stp on`. swp1
and swp5 are configured for tagging VLAN 100, while swp4 is configured
to not tag a VLAN across the link.

    auto br100iface br100
      bridge-ports swp1.100 swp5.100
      bridge-stp on
     
    auto br1
    iface br1
      bridge-ports swp1 swp4 swp5
      bridge-stp on

To enable the bridge and load the new configuration from
`/etc/network/interfaces`, run `ifreload -a`:

    cumulus@switch:~$ sudo ifreload -a

Runtime Configuration (Advanced)

{{%notice warning%}}

A runtime configuration is non-persistent, which means the configuration
you create here does not persist after you reboot the switch.

{{%/notice%}}

`You use brctl` to create the bridge, add bridge ports in the bridge and
configure STP on the bridge. `mstpctl` is used only when an admin needs
to change the default configuration parameters for STP:

    cumulus@switch:~$ sudo brctl addbr br100
     
    cumulus@switch:~$ sudo brctl addif br100 swp1.100 swp4.100 swp5.100
     
    cumulus@switch:~$ sudo brctl stp br100 on
     
    cumulus@switch:~$ sudo ifconfig br100 up

## <span>Configuring STP within a VLAN-aware Bridge</span>

[VLAN-aware](/version/cumulus-rmp-312/Layer_1_and_Layer_2_Features/Ethernet_Bridging_-_VLANs/VLAN-aware_Bridge_Mode_for_Large-scale_Layer_2_Environments)
bridges only operate in RSTP mode. STP BPDUs are transmitted on the
native VLAN.

If a bridge running RSTP (802.1w) receives a common STP (802.1D) BPDU,
it will automatically fall back to 802.1D operation.

### <span>Creating a VLAN-aware Bridge and Configuring RSTP</span>

To create a VLAN-aware mode bridge, configure the bridge stanza under
`/etc/network/interfaces`.

    auto br2
    iface br2
      bridge-vlan-aware yes
      bridge-vids 100
      bridge-pvid  1
      bridge-ports swp1 swp4 swp5
      bridge-stp on

To enable the bridge and load the new configuration from
`/etc/network/interfaces`, run `ifreload -a`:

    cumulus@switch:~$ sudo ifreload -a

### <span>RSTP Interoperation with MST (802.1s)</span>

RSTP interoperates with MST seamlessly, creating a single instance of
spanning tree which transmitts BPDUs on the native VLAN. RSTP treats the
MST domain as if it were one giant switch.

## <span>Viewing Bridge and STP Status/Logs</span>

`mstpd` is started by default when the switch boots. `mstpd` logs and
errors are located in `/var/log/syslog`.

{{%notice warning%}}

`mstpd` is the preferred utility for interacting with STP on Cumulus
RMP. `brctl` also provides certain methods for configuring STP; however,
they are not as complete as the tools offered in `mstpd` and [output
from brctl can be
misleading](https://support.cumulusnetworks.com/hc/en-us/articles/212153658-brctl-showstp-Shows-Carrier-Down-Ports-as-Blocking)
in some cases.

{{%/notice%}}

To get the bridge state, use:

    cumulus@switch:~$ sudo brctl show
     bridge name     bridge id               STP enabled     interfaces
     br2             8000.001401010100       yes             swp1
                                                             swp4
                                                             swp5

To get the `mstpd` bridge state, use:

    cumulus@switch:~$ sudo mstpctl showbridge br2
     br2 CIST info
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

    cumulus@switch:~$ sudo mstpctl showport br2
     E swp1 8.001 forw F.000.00:14:01:01:01:00 F.000.00:14:01:01:01:00 8.001 Desg
       swp4 8.002 forw F.000.00:14:01:01:01:00 F.000.00:14:01:01:01:00 8.002 Desg
     E swp5 8.003 forw F.000.00:14:01:01:01:00 F.000.00:14:01:01:01:00 8.003 Desg
     
    cumulus@switch:~$ sudo mstpctl showportdetail br2 swp1
     br2:swp1 CIST info
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

## <span>Configuring Spanning Tree Protocol</span>

There are a number of ways you can customize STP in Cumulus RMP. You
should exercise extreme caution with many of the settings below to
prevent malfunctions in STP's loop avoidance.

### <span>PortAdminEdge/PortFast Mode</span>

`PortAdminEdge` is equivalent to the PortFast feature offered by other
vendors.

All ports configured with `PortAdminEdge` bypass the listening and
learning states to move immediately to forwarding.

{{%notice warning%}}

Using PortAdminEdge mode has the potential to cause loops if it is not
accompanied by the BPDU guard feature. All examples below include BPDU
guard.

{{%/notice%}}

While it is common for edge ports to be configured as access ports for a
simple end host, this is not mandatory. In the data center, edge ports
typically connect to servers, which may pass both tagged and untagged
traffic.

For the bridge, configure `PortAdminEdge` under the bridge stanza in
`/etc/network/interfaces`:

    auto br2
    iface br2 inet static
      bridge-ports swp1 swp2 swp3 swp4
      bridge-stp on
      mstpctl-bpduguard swp1=yes swp2=yes swp3=yes swp4=yes
      mstpctl-portadminedge swp1=yes swp2=yes swp3=yes swp4=yes

For each interface, configure `PortAdminEdge` under a switch port
interface stanza in `/etc/network/interfaces`:

    auto swp5
    iface swp5
        mstpctl-bpduguard yes
        mstpctl-portadminedge yes

To load the new configuration, run `ifreload -a`:

    cumulus@switch:~$ sudo ifreload -a

Runtime Configuration (Advanced)

{{%notice warning%}}

A runtime configuration is non-persistent, which means the configuration
you create here does not persist after you reboot the switch.

{{%/notice%}}

    cumulus@switch:~$ sudo mstpctl setportadminedge br2 swp1 yes
    cumulus@switch:~$ sudo mstpctl setbpduguard br2 swp1 yes

### <span id="src-5122792_SpanningTreeandRapidSpanningTree-bpdu" class="confluence-anchor-link"></span><span> BPDU Guard</span>

To protect the spanning tree topology from unauthorized switches
affecting the forwarding path, you can configure *BPDU guard* (Bridge
Protocol Data Unit). One very common example is when someone hooks up a
new switch to an access port off of a leaf switch. If this new switch is
configured with a low priority, it could become the new root switch and
affect the forwarding path for the entire layer 2 topology.

#### <span>Configuring BPDU Guard</span>

For the bridge, configure BPDU guard under the bridge stanza in
`/etc/network/interfaces`:

    auto br2
    iface br2 inet static
      bridge-ports swp1 swp2 swp3 swp4 swp5 swp6
      bridge-stp on
      mstpctl-bpduguard swp1=yes swp2=yes swp3=yes swp4=yes

For each interface, configure BPDU guard under an interface stanza in
`/etc/network/interfaces`:

    auto swp5
    iface swp5
        mstpctl-bpduguard yes

To load the new configuration, run `ifreload -a`:

    cumulus@switch:~$ sudo ifreload -a

Runtime Configuration (Advanced)

{{%notice warning%}}

A runtime configuration is non-persistent, which means the configuration
you create here does not persist after you reboot the switch.

{{%/notice%}}

    cumulus@switch:~$ sudo mstpctl setbpduguard br2 swp1 yes
    cumulus@switch:~$ sudo mstpctl setbpduguard br2 swp2 yes
    cumulus@switch:~$ sudo mstpctl setbpduguard br2 swp3 yes
    cumulus@switch:~$ sudo mstpctl setbpduguard br2 swp4 yes

#### <span>Recovering a Port Disabled by BPDU Guard</span>

If a BPDU is received on the port, STP will bring down the port and log
an error in `/var/log/syslog`. The following is a sample error:

    mstpd: error, MSTP_IN_rx_bpdu: bridge:bond0 Recvd BPDU on BPDU Guard Port - Port Down

To determine whether BPDU guard is configured, or if a BPDU has been
received, run `mstpctl showportdetail <bridge name>`:

    cumulus@switch:~$ sudo mstpctl showportdetail br2 swp1 | grep guard
     bpdu guard port    yes                     bpdu guard error     yes

The only way to recover a port that has been placed in the disabled
state is to manually un-shut or bring up the port with ` sudo ifup
 ``[port]`, as shown in the example below:

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

### <span>Bridge Assurance</span>

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

To enable bridge assurance on an interface, edit
`/etc/network/interfaces` and add a line similar to the example below to
the bridge configuration:

    mstpctl-portnetwork swp1=no

You can monitor logs for bridge assurance messages by doing the
following:

    cumulus@switch:~$ sudo grep -in assurance /var/log/syslog | grep mstp
     1365:Jun 25 18:03:17 mstpd: br1007:swp1.1007 Bridge assurance inconsistent

To load the new configuration from `/etc/network/interfaces`, run
`ifreload -a`:

    cumulus@switch:~$ sudo ifreload -a

Runtime Configuration (Advanced)

{{%notice warning%}}

A runtime configuration is non-persistent, which means the configuration
you create here does not persist after you reboot the switch.

{{%/notice%}}

To enable bridge assurance at runtime, run `mstpctl`:

    cumulus@switch:~$ sudo mstpctl setportnetwork br1007 swp1.1007 yes
     
    cumulus@switch:~$ sudo mstpctl showportdetail br1007 swp1.1007 | grep network
      network port       yes                     BA inconsistent      yes

### <span>BPDU Filter</span>

You can enable `bpdufilter` on a switch port, which filters BPDUs in
both directions. This effectively disables STP on the port as no BPDUs
are transiting.

{{%notice warning%}}

Using BDPU filter inappropriately can cause layer 2 loops. Use this
feature deliberately and with extreme caution.

{{%/notice%}}

For the bridge, enable BPDU filter persistently by adding the following
to `/etc/network/interfaces` under the `bridge port iface` section
example:

    auto br100
    iface br100
         bridge-ports swp1.100 swp2.100
         mstpctl-portbpdufilter swp1=yes swp2=yes

For each interface, it is also possible to enable BPDU filter
persistently for a specific port with the following configuration:

    auto swp6
    iface swp6
        mstpctl-portbpdufilter yes

To load the new configuration from `/etc/network/interfaces`, run
`ifreload -a`:

    cumulus@switch:~$ sudo ifreload -a

For more information, see `man(5) ifupdown-addons-interfaces`.

Runtime Configuration (Advanced)

{{%notice warning%}}

A runtime configuration is non-persistent, which means the configuration
you create here does not persist after you reboot the switch.

{{%/notice%}}

To enable BPDU filter at runtime, run `mstpctl`:

    cumulus@switch:~$ sudo mstpctl setportbpdufilter br100 swp1.100=yes swp2.100=yes

### <span>Storm Control</span>

*Storm control* provides protection against excessive inbound BUM
(broadcast, unknown unicast, multicast) traffic on layer 2 switch port
interfaces, which can cause poor network performance.

You configure storm control for each physical port in one of three ways:

  - By editing `/etc/cumulus/switchd.conf`. The configuration persists
    across reboots and restarting `switchd`. If you change the storm
    control configuration in this file after rebooting the switch, you
    must [restart
    `switchd`](https://docs.cumulusnetworks.com/pages/viewpage.action?pageId=5117004)
    to activate the new configuration.

  - By editing `/etc/network/interfaces`, which requires you to reload
    the interface configuration for the change to take effect.

  - By writing directly to the [`switchd` file
    system](https://docs.cumulusnetworks.com/pages/viewpage.action?pageId=5117004).

For example, to enable broadcast and multicast storm control at 400
packets per second (pps) and 3000 pps, respectively, for swp1 editing
`/etc/cumulus/switchd.conf`, configure it as follows:

    # Storm Control setting on a port, in pps, 0 means disable
    interface.swp1.storm_control.broadcast = 400
    interface.swp1.storm_control.multicast = 3000

To configure these settings in `/etc/network/interfaces`:

    auto swp1
    iface swp1
      post-up echo 400 > /cumulus/switchd/config/interface/$IFACE/storm_control/broadcast
      post-up echo 3000 > /cumulus/switchd/config/interface/$IFACE/storm_control/multicast
      post-down echo 0 > /cumulus/switchd/config/interface/$IFACE/storm_control/broadcast
      post-down echo 0 > /cumulus/switchd/config/interface/$IFACE/storm_control/multicast

Then, reload the configuration:

    cumulus@switch:$ sudo ifreload -a

Runtime Configuration (Advanced)

{{%notice warning%}}

A runtime configuration is non-persistent, which means the configuration
you create here does not persist after you reboot the switch.

{{%/notice%}}

Finally, if you are not in a position to restart `switchd`, you can
change your storm control settings at runtime, which take effect
immediately. For example, to set the pps on swp1 to 400 pps for
broadcast traffic and 3000 for multicast traffic:

    cumulus@switch:$ sudo cl-cfg -w switchd interface.swp1.storm_control.broadcast=400
    cumulus@switch:$ sudo cl-cfg -w switchd interface.swp1.storm_control.multicast=3000

### <span>Example Configuration with All Possible Parameters</span>

The persistent configuration for a bridge is set in
`/etc/network/interfaces`. The configuration below shows every possible
option configured. There is no requirement to configure any of these
options:

    auto br2
    iface br2 inet static
      bridge-ports swp1 swp2 swp3 swp4
      bridge-stp on
      mstpctl-maxage 20
      mstpctl-ageing 300
      mstpctl-fdelay 15
      mstpctl-maxhops 20
      mstpctl-txholdcount 6
      mstpctl-forcevers rstp
      mstpctl-treeprio 32768
      mstpctl-treeportprio swp3=128
      mstpctl-hello 2
      mstpctl-portpathcost swp1=0 swp2=0
      mstpctl-portadminedge swp1=no swp2=no
      mstpctl-portautoedge swp1=yes swp2=yes
      mstpctl-portp2p swp1=no swp2=no
      mstpctl-portrestrrole swp1=no swp2=no
      mstpctl-portrestrtcn swp1=no swp2=no
      mstpctl-portnetwork swp1=no
      mstpctl-bpduguard swp1=no swp2=no
      mstpctl-portbpdufilter swp4=yes

### <span id="src-5122792_SpanningTreeandRapidSpanningTree-params" class="confluence-anchor-link"></span><span>Configuring Other Spanning Tree Parameters</span>

Spanning tree parameters are defined in the IEEE
[802.1D](http://standards.ieee.org/getieee802/download/802.1D-2004.pdf),
[802.1Q](http://standards.ieee.org/getieee802/download/802.1Q-2005.pdf)
specifications and in the table below.

While configuring spanning tree in a persistent configuration, as
described above, is the preferred method, you can also use `mstpctl(8)`
to configure spanning tree protocol parameters at runtime.

{{%notice warning%}}

A runtime configuration is non-persistent, which means the configuration
you create here does not persist after you reboot the switch.

{{%/notice%}}

For a comparison of STP parameter configuration between `mstpctl` and
other vendors, [please read this knowledge base
article](https://support.cumulusnetworks.com/hc/en-us/articles/206908397).

Examples are included below:

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Parameter</p></th>
<th><p>Description</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><strong>maxage</strong></p></td>
<td><p>Sets the bridge's <em>maximum age</em> to <code>&lt;max_age&gt;</code> seconds. The default is <em>20</em>.</p>
<p>The maximum age must meet the condition 2 * (Bridge Forward Delay - 1 second) &gt;= Bridge Max Age.</p>
<p>To set this parameter persistently, configure it under the bridge stanza:</p>
<pre><code>mstpctl-maxage 24</code></pre>
<p>To set this parameter at runtime, use:</p>
<p><code>mstpctl setmaxage &lt;bridge&gt; &lt;max_age&gt;</code></p>
<pre><code>cumulus@switch:~$ sudo mstpctl setmaxage br2 24</code></pre></td>
</tr>
<tr class="even">
<td><p><strong>ageing</strong></p></td>
<td><p>Sets the Ethernet (MAC) address <em>ageing time</em> in <code>&lt;time&gt;</code> seconds for the bridge when the running version is STP, but not RSTP/MSTP. The default is <em>300</em>.</p>
<p>To set this parameter persistently, configure it under the bridge stanza:</p>
<pre><code>mstpctl-ageing 240</code></pre>
<p>To set this parameter at runtime, use:</p>
<pre><code>mstpctl setageing &lt;bridge&gt; &lt;time&gt;</code></pre>
<pre><code>cumulus@switch:~$ sudo mstpctl setageing br2 240</code></pre></td>
</tr>
<tr class="odd">
<td><p><strong>fdelay</strong></p></td>
<td><p>Sets the bridge's <em>bridge forward delay</em> to <code>&lt;time&gt;</code> seconds. The default is <em>15</em>.</p>
<p>The bridge forward delay must meet the condition 2 * (Bridge Forward Delay - 1 second) &gt;= Bridge Max Age.</p>
<p>To set this parameter persistently, configure it under the bridge stanza:</p>
<pre><code>mstpctl-fdelay 15</code></pre>
<p>To set this parameter at runtime, use:</p>
<pre><code>mstpctl setfdelay &lt;bridge&gt; &lt;time&gt;</code></pre>
<pre><code>cumulus@switch:~$ sudo mstpctl setfdelay br2 15</code></pre></td>
</tr>
<tr class="even">
<td><p><strong>maxhops</strong></p></td>
<td><p>Sets the bridge's <em>maximum hops</em> to <code>&lt;max_hops&gt;</code>. The default is <em>20</em>.</p>
<p>To set this parameter persistently, configure it under the bridge stanza:</p>
<pre><code>mstpctl-maxhops 24</code></pre>
<p>To set this parameter at runtime, use:</p>
<pre><code>mstpctl setmaxhops &lt;bridge&gt; &lt;max_hops&gt;</code></pre>
<pre><code>cumulus@switch:~$ sudo mstpctl setmaxhops br2 24</code></pre></td>
</tr>
<tr class="odd">
<td><p><strong>txholdcount</strong></p></td>
<td><p>Sets the bridge's <em>bridge transmit hold count</em> to <code>&lt;tx_hold_count&gt;</code>. The default is <em>6</em>.</p>
<p>To set this parameter persistently, configure it under the bridge stanza:</p>
<pre><code>mstpctl-txholdcount 6</code></pre>
<p>To set this parameter at runtime, use:</p>
<p><code>mstpctl settxholdcount &lt;bridge&gt; &lt;tx_hold_count&gt;</code></p>
<pre><code>cumulus@switch:~$ sudo mstpctl settxholdcount br2 5</code></pre></td>
</tr>
<tr class="even">
<td><p><strong>forcevers</strong></p></td>
<td><p>Sets the bridge's <em>force STP version</em> to either RSTP/STP. MSTP is not supported currently. The default is <em>RSTP</em>.</p>
<p>To set this parameter persistently, configure it under the bridge stanza:</p>
<pre><code>mstpctl-forcevers rstp</code></pre>
<p>To set this parameter at runtime, use:</p>
<pre><code>mstpctl setforcevers &lt;bridge&gt; {mstp|rstp|stp}</code></pre>
<pre><code>cumulus@switch:~$ sudo mstpctl setforcevers br2 rstp</code></pre></td>
</tr>
<tr class="odd">
<td><p><strong>treeprio</strong></p></td>
<td><p>Sets the bridge's <em>tree priority</em> to <code>&lt;priority&gt;</code> for an MSTI instance. The priority value is a number between 0 and 65535 and must be a multiple of 4096. The bridge with the lowest priority is elected the <em>root bridge</em>. The default is <em>32768</em>.</p>
<p>{{%notice warning%}}</p>
<p>For <code>msti</code>, only 0 is supported currently.</p>
<p>{{%/notice%}}</p>
<p>To set this parameter persistently, configure it under the bridge stanza:</p>
<pre><code>mstpctl-treeprio 8192</code></pre>
<p>To set this parameter at runtime, use:</p>
<pre><code>mstpctl settreeprio &lt;bridge&gt; &lt;mstid&gt; &lt;priority&gt;</code></pre>
<pre><code>cumulus@switch:~$ sudo mstpctl settreeprio br2 0 8192</code></pre></td>
</tr>
<tr class="even">
<td><p><strong>treeportprio</strong></p></td>
<td><p>Sets the <em>priority</em> of port <code>&lt;port&gt;</code> to <code>&lt;priority&gt;</code> for the MSTI instance. The priority value is a number between 0 and 240 and must be a multiple of 16. The default is <em>128</em>.</p>
<p>{{%notice warning%}}</p>
<p>For <code>msti</code>, only <em>0</em> is supported currently.</p>
<p>{{%/notice%}}</p>
<p>To set this parameter persistently, configure it under the bridge stanza:</p>
<pre><code>mstpctl-treeportprio swp4.101 64</code></pre>
<p>To set this parameter at runtime, use:</p>
<pre><code>mstpctl settreeportprio &lt;bridge&gt; &lt;port&gt; &lt;mstid&gt; &lt;priority&gt;</code></pre>
<pre><code>cumulus@switch:~$ sudo mstpctl settreeportprio br2 swp4.101 0 64</code></pre></td>
</tr>
<tr class="odd">
<td><p><strong>hello</strong></p></td>
<td><p>Sets the bridge's <em>bridge hello time</em> to <code>&lt;time&gt;</code> seconds. The default is <em>2</em>.</p>
<p>To set this parameter persistently, configure it under the bridge stanza:</p>
<pre><code>mstpctl-hello 20</code></pre>
<p>To set this parameter at runtime, use:</p>
<pre><code>mstpctl sethello &lt;bridge&gt; &lt;time&gt;</code></pre>
<pre><code>cumulus@switch:~$ sudo mstpctl sethello br2 20</code></pre></td>
</tr>
<tr class="even">
<td><p><strong>portpathcost</strong></p></td>
<td><p>Sets the <em>port cost</em> of the port <code>&lt;port&gt;</code> in bridge <code>&lt;bridge&gt;</code> to <code>&lt;cost&gt;</code>. The default is <em>0</em>.</p>
<p><code>mstpd</code> supports only long mode; that is, 32 bits for the path cost.</p>
<p>To set this parameter persistently, configure it under the bridge stanza:</p>
<pre><code>mstpctl-portpathcost swp1.101=10</code></pre>
<p>To set this parameter at runtime, use:</p>
<pre><code>mstpctl setportpathcost &lt;bridge&gt; &lt;port&gt; &lt;cost&gt;</code></pre>
<pre><code>cumulus@switch:~$ sudo mstpctl setportpathcost br2 swp1.101 10</code></pre></td>
</tr>
<tr class="odd">
<td><p><strong>portadminedge</strong></p></td>
<td><p>Enables/disables the <em>initial edge state</em> of the port <code>&lt;port&gt;</code> in bridge <code>&lt;bridge&gt;</code>. The default is <em>no</em>.</p>
<p>To set this parameter persistently, configure it under the bridge stanza:</p>
<pre><code>mstpctl-portadminedge swp1.101=yes</code></pre>
<p>To set this parameter at runtime, use:</p>
<pre><code>mstpctl setportadminedge &lt;bridge&gt; &lt;port&gt; {yes|no}</code></pre>
<pre><code>cumulus@switch:~$ sudo mstpctl setportadminedge br2 swp1.101 yes</code></pre></td>
</tr>
<tr class="even">
<td><p><strong>portautoedge</strong></p></td>
<td><p>Enables/disables the <em>auto transition</em> to/from the edge state of the port <code>&lt;port&gt;</code> in bridge <code>&lt;bridge&gt;</code>. The default is <em>yes</em>.</p>
<p>To set this parameter persistently, configure it under the bridge stanza:</p>
<pre><code>mstpctl-portautoedge swp1.101=no</code></pre>
<p>To set this parameter at runtime, use:</p>
<pre><code>mstpctl setportautoedge &lt;bridge&gt; &lt;port&gt; {yes|no}</code></pre>
<pre><code>cumulus@switch:~$ sudo mstpctl setportautoedge br2 swp1.101 no</code></pre></td>
</tr>
<tr class="odd">
<td><p><strong>portp2p</strong></p></td>
<td><p>Enables/disables the <em>point-to-point detection mode</em> of the port <code>&lt;port&gt;</code> in bridge <code>&lt;bridge&gt;</code>. The default is <em>auto</em>.</p>
<p>To set this parameter persistently, configure it under the bridge stanza:</p>
<pre><code>mstpctl-portp2p swp1.101=no</code></pre>
<p>To set this parameter at runtime, use:</p>
<pre><code>mstpctl setportp2p &lt;bridge&gt; &lt;port&gt; {yes|no|auto}</code></pre>
<pre><code>cumulus@switch:~$ sudo mstpctl setportp2p br2 swp1.101 no</code></pre></td>
</tr>
<tr class="even">
<td><p><strong>portrestrrole</strong></p></td>
<td><p>Enables/disables the ability of the port <code>&lt;port&gt;</code> in bridge <code>&lt;bridge&gt;</code> to take the <em>root role</em>. The default is <em>no</em>.</p>
<p>To set this parameter persistently, configure it under the bridge stanza:</p>
<pre><code>mstpctl-portrestrrole swp1.101=no</code></pre>
<p>To set this parameter at runtime, use:</p>
<pre><code>mstpctl setportrestrrole &lt;bridge&gt; &lt;port&gt; {yes|no}</code></pre>
<pre><code>cumulus@switch:~$ sudo mstpctl setportrestrrole br2 swp1.101 yes</code></pre></td>
</tr>
<tr class="odd">
<td><p><strong>portrestrtcn</strong></p></td>
<td><p>Enables/disables the ability of the port <code>&lt;port&gt;</code> in bridge <code>&lt;bridge&gt;</code> to propagate <em>received topology change notifications</em>. The default is <em>no</em>.</p>
<p>To set this parameter persistently, configure it under the bridge stanza:</p>
<pre><code>mstpctl-portrestrtcn swp1.101=yes</code></pre>
<p>To set this parameter at runtime, use:</p>
<pre><code>mstpctl setportrestrtcn &lt;bridge&gt; &lt;port&gt; {yes|no}</code></pre>
<pre><code>cumulus@switch:~$ sudo mstpctl setportrestrtcn br2 swp1.101 yes</code></pre></td>
</tr>
<tr class="even">
<td><p><strong>portnetwork</strong></p></td>
<td><p>Enables/disables the <em>bridge assurance capability</em> for a network port <code>&lt;port&gt;</code> in bridge <code>&lt;bridge&gt;</code>. The default is <em>no</em>.</p>
<p>To set this parameter persistently, configure it under the bridge stanza:</p>
<pre><code>mstpctl-portnetwork swp4.101=yes</code></pre>
<p>To set this parameter at runtime, use:</p>
<pre><code>mstpctl setportnetwork &lt;bridge&gt; &lt;port&gt; {yes|no}</code></pre>
<pre><code>cumulus@switch:~$ sudo mstpctl setportnetwork br2 swp4.101 yes</code></pre></td>
</tr>
<tr class="odd">
<td><p><strong>bpduguard</strong></p></td>
<td><p>Enables/disables the <em>BPDU guard configuration</em> of the port <code>&lt;port&gt;</code> in bridge <code>&lt;bridge&gt;</code>. The default is <em>no</em>.</p>
<p>To set this parameter persistently, configure it under the bridge stanza:</p>
<pre><code>mstpctl-bpduguard swp1=no</code></pre>
<p>To set this parameter at runtime, use:</p>
<pre><code>mstpctl setbpduguard &lt;bridge&gt; &lt;port&gt; {yes|no}</code></pre>
<pre><code>cumulus@switch:~$ sudo mstpctl setbpduguard br2 swp1.101 yes</code></pre></td>
</tr>
<tr class="even">
<td><p><strong>portbpdufilter</strong></p></td>
<td><p>Enables/disables the <em>BPDU filter</em> functionality for a port <code>&lt;port&gt;</code> in bridge <code>&lt;bridge&gt;</code>. The default is <em>no</em>.</p>
<p>To set this parameter persistently, configure it under the bridge stanza:</p>
<pre><code>mstpctl-portbpdufilter swp4.101=yes</code></pre>
<p>To set this parameter at runtime, use:</p>
<pre><code>mstpctl setportbpdufilter &lt;bridge&gt; &lt;port&gt; {yes|no}</code></pre>
<pre><code>cumulus@switch:~$ sudo mstpctl setportbpdufilter br2 swp4.101 yes</code></pre></td>
</tr>
</tbody>
</table>

## <span>Configuration Files</span>

  - /etc/network/interfaces

## <span>Man Pages</span>

  - brctl(8)

  - bridge-utils-interfaces(5)

  - ifupdown-addons-interfaces(5)

  - mstpctl(8)

  - mstpctl-utils-interfaces(5)

## <span>Useful Links</span>

The source code for `mstpd/mstpctl` was written by [Vitalii
Demianets](mailto:vitas%40nppfactor.kiev.ua) and is hosted at the
sourceforge URL below.

  - [sourceforge.net/projects/mstpd/](https://sourceforge.net/projects/mstpd/)

  - [en.wikipedia.org/wiki/Spanning\_Tree\_Protocol](http://en.wikipedia.org/wiki/Spanning_Tree_Protocol)

## <span>Caveats and Errata</span>

  - MSTP is not supported currently. However, interoperability with MSTP
    networks can be accomplished using PVRSTP or PVSTP.
