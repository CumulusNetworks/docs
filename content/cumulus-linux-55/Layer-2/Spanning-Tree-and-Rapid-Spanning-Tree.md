---
title: Spanning Tree and Rapid Spanning Tree - STP
author: NVIDIA
weight: 460
toc: 3
---
<span class="a-tooltip">[STP](## "Spanning Tree Protocol")</span> identifies links in the network and shuts down redundant links, preventing possible network loops and broadcast radiation on a bridged network. STP also provides redundant links for automatic failover when an active link fails. Cumulus Linux enables STP by default for both VLAN-aware and traditional bridges.

Cumulus Linux supports <span class="a-tooltip">[RSTP](## "Rapid Spanning Tree Protocol")</span>, <span class="a-tooltip">[PVST](## "Per-VLAN Spanning Tree")</span>, and <span class="a-tooltip">[PVRST](## "Per-VLAN Rapid Spanning Tree")</span> modes:

- *{{<link url="Traditional-Bridge-Mode" text="Traditional bridges">}}* operate in both PVST and PVRST mode. The default is PVRST. Each traditional bridge has its own separate STP instance.
- *{{<link url="VLAN-aware-Bridge-Mode" text="VLAN-aware bridges">}}* operate **only** in RSTP mode.

## STP for a Traditional Mode Bridge

<span class="a-tooltip">[PVST](## "Per-VLAN Spanning Tree")</span> creates a spanning tree instance for a bridge. <span class="a-tooltip">[PVRST](## "Per-VLAN Rapid Spanning Tree")</span> supports <span class="a-tooltip">[RSTP](## "Rapid Spanning Tree Protocol")</span> enhancements for each spanning tree instance. To use PVRST with a traditional bridge, you must create a bridge corresponding to the untagged native VLAN and all the physical switch ports must be part of the same VLAN.

{{%notice note%}}
For maximum interoperability, when connected to a switch that has a native VLAN configuration, you **must** configure the native VLAN to VLAN 1.
{{%/notice%}}
<!-- vale off -->
## STP for a VLAN-aware Bridge
<!-- vale on -->
VLAN-aware bridges operate in RSTP mode only. RSTP on VLAN-aware bridges works with other modes in the following ways:

### RSTP and STP

If a bridge running RSTP (802.1w) receives a common STP (802.1D) BPDU, it falls back to 802.1D automatically.

### RSTP and PVST

The RSTP domain sends <span class="a-tooltip">[BPDUs](## "Bridge Protocol Data Units")</span> on the native VLAN, whereas PVST sends BPDUs on a per VLAN basis. For both protocols to work together, you need to enable the native VLAN on the link between the RSTP to PVST domain; the spanning tree builds according to the native VLAN parameters.

The RSTP protocol does not send or parse BPDUs on other VLANs, but floods BPDUs across the network, enabling the PVST domain to maintain its spanning-tree topology and provide a loop-free network.
- To enable proper BPDU exchange across the network, be sure to allow all VLANs participating in the PVST domain on the link between the RSTP and PVST domains.
- When using RSTP together with an existing PVST network, you need to define the root bridge on the PVST domain. Either lower the priority on the PVST domain or change the priority of the RSTP switches to a higher number.
- When connecting a VLAN-aware bridge to a proprietary PVST+ switch using STP, you must allow VLAN 1 on all 802.1Q trunks that interconnect them, regardless of the configured *native* VLAN. Only VLAN 1 enables the switches to address the BPDU frames to the IEEE multicast MAC address.

### RSTP and MST

RSTP works with <span class="a-tooltip">[MST](## "Multiple Spanning Tree")</span> seamlessly, creating a single instance of spanning tree that transmits BPDUs on the native VLAN.

RSTP treats the MST domain as one giant switch, whereas MST treats the RSTP domain as a different region. To ensure proper communication between the regions, MST creates a <span class="a-tooltip">[CST](## "Common Spanning Tree")</span> that connects all the boundary switches and forms the overall view of the MST domain. Because changes in the CST must reflect in all regions, the RSTP tree exists is in the CST to ensure that changes on the RSTP domain are in the CST domain. Topology changes on the RSTP domain impact the rest of the network but inform the MST domain of every change occurring in the RSTP domain, ensuring a loop-free network.

Configure the root bridge within the MST domain by changing the priority on the relevant MST switch. When MST detects an RSTP link, it falls back into RSTP mode. The MST domain chooses the switch with the lowest cost to the CST root bridge as the CIST root bridge.

### RSTP with MLAG

More than one spanning tree instance enables switches to load balance and use different links for different VLANs. With RSTP, there is only one instance of spanning tree. To better utilize the links, you can configure <span class="a-tooltip">[MLAG](## "Multi-chassis Link Aggregation")</span> on the switches connected to the <span class="a-tooltip">[MST](## "Multiple Spanning Tree")</span> or <span class="a-tooltip">[PVST](## "Per-VLAN Spanning Tree")</span> domain and set up these interfaces as an MLAG port. The PVST or MST domain thinks it connects to a single switch and utilizes all the links connected to it. Load balancing depends on the port channel hashing mechanism instead of different spanning tree instances and uses all the links between the RSTP to the PVST or MST domains. For information about configuring MLAG, see {{<link url="Multi-Chassis-Link-Aggregation-MLAG" text="Multi-Chassis Link Aggregation - MLAG">}}.

## Configure STP

There several ways to customize STP in Cumulus Linux. Exercise caution when changing the settings below to prevent malfunctions in STP loop avoidance.

### Spanning Tree Priority

If you have a multiple spanning tree instance (MSTI 0, also known as a common spanning tree, or CST), you can set the *tree priority* for a bridge. The bridge with the lowest priority is the *root bridge*. The priority must be a number between *0* and *61440,* and must be a multiple of 4096. The default is *32768*.

{{%notice note%}}
If you are running MLAG and have multiple bridges, the STP priority must be the same on all bridges on both peer switches.
{{%/notice%}}

The following example command sets the tree priority to 8192:

{{< tabs "TabID213 ">}}
{{< tab "NVUE Commands ">}}

```
cumulus@switch:~$ nv set bridge domain br_default stp priority 8192
cumulus@switch:~$ nv config apply
```

{{< /tab >}}
{{< tab "Linux Commands ">}}

Configure the tree priority (`mstpctl-treeprio`) under the *bridge* stanza in the `/etc/network/interfaces` file, then run the `ifreload -a` command.

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

```
cumulus@switch:~$ ifreload -a
```

{{< /tab >}}
{{< /tabs >}}

{{%notice note%}}
Cumulus Linux supports MSTI 0 only. It does not support MSTI 1 through 15.
{{%/notice%}}

### PortAdminEdge (PortFast Mode)

*PortAdminEdge* is equivalent to the PortFast feature offered by other vendors. It enables or disables the *initial edge state* of a port in a bridge. All ports with PortAdminEdge bypass the listening and learning states and go straight to forwarding.

{{%notice warning%}}
PortAdminEdge mode causes loops if you do not use it with {{<link url="#bpdu-guard" text="BPDU guard">}}.
{{%/notice%}}

You typically configure edge ports as access ports for a simple end host. In the data center, edge ports connect to servers, which pass both tagged and untagged traffic.

The following example commands configure PortAdminEdge and BPDU guard for swp5:

{{< tabs "TabID276 ">}}
{{< tab "NVUE Commands ">}}

```
cumulus@switch:~$ nv set interface swp5 bridge domain br_default stp admin-edge on
cumulus@switch:~$ nv set interface swp5 bridge domain br_default stp bpdu-guard on
cumulus@switch:~$ nv config apply
```

{{< /tab >}}
{{< tab "Linux Commands ">}}

Configure PortAdminEdge and BPDU guard under the switch port interface stanza in the `/etc/network/interfaces` file, then run the `ifreload -a` command.

```
cumulus@switch:~$ sudo nano /etc/netowrk/interfaces
...
auto swp5
iface swp5
    mstpctl-bpduguard yes
    mstpctl-portadminedge yes
...
```

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

{{< /tab >}}
{{< /tabs >}}

### PortAutoEdge

*PortAutoEdge* is an enhancement to the standard PortAdminEdge (PortFast) mode, which allows for the automatic detection of edge ports. PortAutoEdge enables and disables the *auto transition* to and from the edge state of a port in a bridge.

{{%notice note%}}
Edge ports and access ports are not the same. Edge ports transition directly to the forwarding state and skip the listening and learning stages. Upstream topology change notifications are not generated when an edge port link changes state. Access ports only forward untagged traffic; however, there is no such restriction on edge ports, which can forward both tagged and untagged traffic.
{{%/notice%}}

When a port with PortAutoEdge receives a BPDU, the port stops being in the edge port state and transitions into a normal STP port. When the interface no longer receives BPDUs, the port becomes an edge port, and transitions through the discarding and learning states before it resumes forwarding.

Cumulus Linux enables PortAutoEdge by default.

The following example commands disable PortAutoEdge on swp1:

{{< tabs "TabID344 ">}}
{{< tab "NVUE Commands ">}}

```
cumulus@switch:~$ nv set interface swp1 bridge domain br_default stp auto-edge off
cumulus@switch:~$ nv config apply
```

{{< /tab >}}
{{< tab "Linux Commands ">}}

Edit the switch port interface stanza in the `/etc/network/interfaces` file to add the `mstpctl-portautoedge no` line, then run the `ifreload -a` command.

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

```
cumulus@switch:~$ sudo ifreload -a
```

{{< /tab >}}
{{< /tabs >}}

The following example commands reenable PortAutoEdge on swp1:

{{< tabs "TabID383 ">}}
{{< tab "NVUE Commands ">}}

```
cumulus@switch:~$ nv set interface swp1 bridge domain br_default stp auto-edge on
cumulus@switch:~$ nv config apply
```

{{< /tab >}}
{{< tab "Linux Commands ">}}

Edit the switch port interface stanza in the `/etc/network/interfaces` file to remove `mstpctl-portautoedge no`, then run the `ifreload -a` command.

{{< /tab >}}
{{< /tabs >}}

### BPDU Guard

You can configure *BPDU guard* to protect the spanning tree topology from an unauthorized device affecting the forwarding path. For example, if you add a new host to an access port off a leaf switch and the host sends an STP <span class="a-tooltip">[BPDU](## "Bridge Protocol Data Unit")</span>, BPDU guard protects against undesirable topology changes in the environment.

The following example commands set BPDU guard for swp5:

{{< tabs "TabID411 ">}}
{{< tab "NVUE Commands ">}}

```
cumulus@switch:~$ nv set interface swp5 bridge domain br_default stp bpdu-guard on
cumulus@switch:~$ nv config apply
```

{{< /tab >}}
{{< tab "Linux Commands ">}}

Edit the switch port interface stanza in the `/etc/network/interfaces` file to add the `mstpctl-bpduguard yes` line, then run the `ifreload -a` command.

```
cumulus@switch:~$ sudo nano /etc/network/interfaces
...
auto swp5
iface swp5
    mstpctl-bpduguard yes
...
```

```
cumulus@switch:~$ sudo ifreload -a
```

{{< /tab >}}
{{< /tabs >}}

To see if a port has BPDU guard on or if the port receives a BPDU:

{{< tabs "TabID454 ">}}
{{< tab "NVUE Commands ">}}

```
cumulus@switch:~$ nv show bridge domain br_default stp
```

{{< /tab >}}
{{< tab "Linux Commands ">}}

```
cumulus@switch:~$ mstpctl showportdetail br_default
bridge:swp5 CIST info
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
  bpdu guard port    yes                     bpdu guard error     yes
  network port       no                      BA inconsistent      no
  Num TX BPDU        3                       Num TX TCN           2
  Num RX BPDU        488                     Num RX TCN           2
  Num Transition FWD 1                       Num Transition BLK   2
  bpdufilter port    no
  clag ISL           no                      clag ISL Oper UP     no
  clag role          unknown                 clag dual conn mac   0:0:0:0:0:0
  clag remote portID F.FFF                   clag system mac      0:0:0:0:0:0
```

{{< /tab >}}
{{< /tabs >}}

If a port receives a BPDU, it goes into a `protodown` state, which results in a local OPER DOWN (carrier down) on the interface. Cumulus Linux also sets the protodown reason as `bpduguard` and records a log message in `/var/log/syslog`.

To show the reason for the port protodown, run the `ip -p -j link show <interface>` command.

```
cumulus@switch:~$ ip -p -j link show swp5
```

To recover from the `protodown` state, remove the protodown reason and protodown from the interface with the `mstpctl clearbpduguardviolation <bridge> <interface>` command.

```
cumulus@switch:~$ mstpctl clearbpduguardviolation bridge swp5
```

{{%notice note%}}
Bringing up the disabled port does not correct the problem if the configuration on the connected end station does not resolve.
{{%/notice%}}

### Bridge Assurance

On a point-to-point link where RSTP is running, if you want to detect unidirectional links and put the port in a discarding state, you can enable bridge assurance on the port by enabling a port type network. The port is then in a bridge assurance inconsistent state until it receives a BPDU from the peer. You need to configure the port type network on both ends of the link for bridge assurance.

Cumulus Linux disables bridge assurance by default.

The following example commands enable bridge assurance on swp1:

{{< tabs "TabID513 ">}}
{{< tab "NVUE Commands ">}}

```
cumulus@switch:~$ nv set interface swp5 bridge domain br_default stp network on
cumulus@switch:~$ nv config apply
```

{{< /tab >}}
{{< tab "Linux Commands ">}}

Edit the switch port interface stanza in the `/etc/network/interfaces` file to add the `mstpctl-portnetwork yes` line, then run the `ifreload -a` command.

```
cumulus@switch:~$ sudo nano /etc/network/interfaces
...
auto swp5
iface swp5
    mstpctl-portnetwork yes
...
```

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

{{< /tab >}}
{{< /tabs >}}

To monitor logs for bridge assurance messages, run the following command:

```
cumulus@switch:~$ sudo grep -in assurance /var/log/syslog | grep mstp
  1365:Jun 25 18:03:17 mstpd: br1007:swp1.1007 Bridge assurance inconsistent
```

### BPDU Filter

You can enable `bpdufilter` on a switch port, which filters BPDUs in both directions. This disables STP on the port as no BPDUs are transiting.

{{%notice warning%}}
Using BDPU filter sometimes causes layer 2 loops. Use this feature with caution.
{{%/notice%}}

The following example commands configure the BPDU filter on swp6:

{{< tabs "TabID584 ">}}
{{< tab "NVUE Commands ">}}

```
cumulus@switch:~$ nv set interface swp6 bridge domain br_default stp bpdu-filter on
cumulus@switch:~$ nv config apply
```

{{< /tab >}}
{{< tab "Linux Commands ">}}

Edit the switch port interface stanza in the `/etc/network/interfaces` file to add the `mstpctl-portbpdufilter yes` line, then run the `ifreload -a` command.

```
cumulus@switch:~$ sudo nano /etc/network/interfaces
...
auto swp6
iface swp6
    mstpctl-portbpdufilter yes
...
```

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

{{< /tab >}}
{{< /tabs >}}

### Restricted Role

To enable the interface in the bridge to take the restricted role:

{{< tabs "TabID427 ">}}
{{< tab "NVUE Commands ">}}

```
cumulus@switch:~$ nv set interface swp1 bridge domain br_default stp restrrole on
cumulus@switch:~$ nv config apply
```

{{< /tab >}}
{{< tab "Linux Commands ">}}

Edit the switch port interface stanza in the `/etc/network/interfaces` file to add the `mstpctl-portrestrrole yes` line, then run the `ifreload -a` command.

```
cumulus@switch:~$ sudo nano /etc/network/interfaces
...
auto swp6
iface swp6
    mstpctl-portrestrrole yes
...
```

```
cumulus@switch:~$ sudo ifreload -a
```

{{< /tab >}}
{{< /tabs >}}

## Additional STP Parameters

The table below describes additional STP configuration parameters available in Cumulus Linux. You can set these optional parameters manually by editing the `/etc/network/interfaces` file. Cumulus Linux does not provide NVUE commands for these parameters.

The IEEE {{<exlink url="https://standards.ieee.org/standard/802_1D-2004.html" text="802.1D">}} and {{<exlink url="https://standards.ieee.org/standard/802_1Q-2018.html" text="802.1Q">}} specifications describe STP parameters. For a comparison of STP parameter configuration between `mstpctl` and other vendors, [read this knowledge base article]({{<ref "/knowledge-base/Demos-and-Training/Interoperability/Cumulus-Linux-vs-Cisco-IOS-Spanning-Tree-Protocol" >}}).

| Parameter | Description |
|-----------|----------|
| `mstpctl-maxage` | Sets the maximum age of the bridge in seconds. The default is 20. The maximum age must meet the condition 2 * (Bridge Forward Delay - 1 second) >= Bridge Max Age.<br>Add this parameter to the bridge stanza of the `/etc/network/interfaces` file. |
| `mstpctl-ageing` | Sets the MAC address ageing time for the bridge in seconds when the running version is STP, but not RSTP or MSTP. The default is 1800.<br>Add this parameter to the bridge stanza of the `/etc/network/interfaces` file.  |
| `mstpctl-fdelay` | Sets the bridge forward delay time in seconds. The default value is 15. The bridge forward delay must meet the condition 2 * (Bridge Forward Delay - 1 second) >= Bridge Max Age.<br>Add this parameter to the bridge stanza of the `/etc/network/interfaces` file. |
| `mstpctl-maxhops` | Sets the maximum hops for the bridge. The default is 20.<br>Add this parameter to the bridge stanza of the `/etc/network/interfaces` file.  |
| `mstpctl-txholdcount` | Sets the bridge transmit hold count. The default value is 6 seconds.<br>Add this parameter to the bridge stanza of the `/etc/network/interfaces` file.  |
| `mstpctl-forcevers` | Sets the force STP version of the bridge to either RSTP/STP. The default is RSTP.<br>Add this parameter to the bridge stanza of the `/etc/network/interfaces` file. |
| `mstpctl-hello` | Sets the bridge hello time in seconds. The default is 2.<br>Add this parameter to the bridge stanza of the `/etc/network/interfaces` file. |
| `mstpctl-portpathcost` | Sets the port cost of the interface in the bridge. The default is 0.<br>`mstpd` supports only long mode; 32 bits for the path cost.<br>Add this parameter to the interface stanza of the `/etc/network/interfaces` file. |
| `mstpctl-portp2p` | Enables or disables point-to-point detection mode of the interface in the bridge.<br>Add this parameter to the interface stanza of the `/etc/network/interfaces` file.|
| `mstpctl-portrestrtcn` | Enables or disables the interface in the bridge to propagate received topology change notifications. The default is no.<br>Add this parameter to the interface stanza of the `/etc/network/interfaces` file.|
| `mstpctl-treeportcost` | Sets the spanning tree port cost to a value from 0 to 255. The default is 0.<br>Add this parameter to the interface stanza of the `/etc/network/interfaces` file.|

Be sure to run the `sudo ifreload -a` command after you set the STP parameter in the `/etc/network/interfaces` file.

## Troubleshooting

To check STP status for a bridge:

{{< tabs "TabID50 ">}}
{{< tab "NVUE Commands ">}}

```
cumulus@switch:~$ nv show bridge domain br_default stp
          operational  applied  description
--------  -----------  -------  ---------------------------------------------------------------------
priority  32768        32768    stp priority. The priority value must be a number between 4096 and...
state     up           up       The state of STP on the bridge
```

{{< /tab >}}
{{< tab "Linux Commands ">}}

The `mstpctl` utility provided by the `mstpd` service configures STP. The `mstpd` daemon is an open source project used by Cumulus Linux to implement IEEE802.1D 2004 and IEEE802.1Q 2011.

The `mstpd` daemon starts by default when the switch boots and logs errors to `/var/log/syslog`.

{{%notice warning%}}
`mstpd` is the preferred utility for interacting with STP on Cumulus Linux. `brctl` also provides certain tools for configuring STP; however, they are not as complete and output from `brctl` is sometimes misleading.
{{%/notice%}}

To show the bridge state, run the `brctl show` command:

```
cumulus@switch:~$ sudo brctl show
  bridge name     bridge id               STP enabled     interfaces
  bridge          8000.001401010100       yes             swp1
                                                          swp4
                                                          swp5
```

To show the `mstpd` bridge port state, run the `mstpctl showport bridge` command:

```
cumulus@switch:~$ sudo mstpctl showport bridge
  E swp1 8.001 forw F.000.00:14:01:01:01:00 F.000.00:14:01:01:01:00 8.001 Desg
    swp4 8.002 forw F.000.00:14:01:01:01:00 F.000.00:14:01:01:01:00 8.002 Desg
  E swp5 8.003 forw F.000.00:14:01:01:01:00 F.000.00:14:01:01:01:00 8.003 Desg
```

{{< /tab >}}
{{< /tabs >}}

## Related Information

- {{<exlink url="https://github.com/mstpd/mstpd" text="GitHub - mstpd project">}}
- brctl(8)
- bridge-utils-interfaces(5)
- ifupdown-addons-interfaces(5)
- mstpctl(8)
- mstpctl-utils-interfaces(5)
