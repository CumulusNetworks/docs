---
title: Spanning Tree and Rapid Spanning Tree - STP
author: NVIDIA
weight: 460
toc: 3
---
<span class="a-tooltip">[STP](## "Spanning Tree Protocol")</span> identifies links in the network and shuts down redundant links, preventing possible network loops and broadcast radiation on a bridged network. STP also provides redundant links for automatic failover when an active link fails. Cumulus Linux enables STP by default for both VLAN-aware and traditional bridges.

{{%notice note%}}
Exercise caution when changing the STP settings below to prevent STP loop avoidance issues.
{{%/notice%}}

## STP Modes

Cumulus Linux supports STP for VLAN-aware and traditional bridges.
<!-- vale off -->
### STP Modes for a VLAN-aware Bridge
<!-- vale on -->
{{<link url="VLAN-aware-Bridge-Mode" text="VLAN-aware bridges">}} operate in:
- <span class="a-tooltip">[RSTP](## "Rapid Spanning Tree Protocol")</span> mode, which creates a single instance of spanning tree across all VLANs. RSTP is the default mode.
- <span class="a-tooltip">[PVRST](## "Per-VLAN Rapid Spanning Tree")</span> mode, which creates a single instance of spanning tree for every VLAN and provides improved link bandwidth utilization.
<!-- vale off -->
### Configure the Mode for a VLAN-aware Bridge
<!-- vale on -->
RSTP is the default mode for a VLAN-aware bridge. You can change the mode to PVRST.

{{%notice note%}}
You cannot configure PVRST mode for multiple VLAN-aware bridges.
{{%/notice%}}

{{< tabs "TabID492 ">}}
{{< tab "NVUE Commands ">}}

The following example sets PVRST mode on the br_default bridge:

```
cumulus@switch:~$ nv set bridge domain br_default stp mode pvrst
cumulus@switch:~$ nv config apply
```

To revert the mode to the default setting (RSTP), run the `nv unset bridge domain <bridge> stp mode` command.

{{< /tab >}}
{{< tab "Linux Commands ">}}

Add `mstpctl-pvrst-mode yes` under the bridge stanza in the `/etc/network/interfaces` file, then run the `ifreload -a` command.

```
cumulus@switch:~$ sudo nano /etc/network/interfaces
...
auto br_default
iface br_default
    bridge-ports swp1 swp2
    hwaddress 44:38:39:22:01:b1
    bridge-vlan-aware yes
    bridge-vids 10 20
    bridge-pvid 1
    bridge-stp yes
    mstpctl-pvrst-mode yes
...
```

```
cumulus@switch:~$ ifreload -a
```

**Runtime Configuration (Advanced)**

{{%notice warning%}}
A runtime configuration is non-persistent, which means the configuration you create here does not persist after you reboot the switch.
{{%/notice%}}

To set STP mode to PVRST at runtime:

```
cumulus@switch:~$ sudo mstpctl setmodepvrst
```

To revert the mode to the default setting (RSTP), run the `sudo mstpctl clearmodepvrst` command.

{{< /tab >}}
{{< /tabs >}}

### PVRST Scale

The maximum number of PVRST instances you can configure is 300 VLANs with 24 ports. The default forwarding rate and burst rate for the `rpvst` trap group is 2000 pps, as shown with the `nv show system control-plane policer rpvst` command ouput below:

```
cumulus@switch:~$ nv show system control-plane policer rpvst
                 operational  applied
---------------  -----------  -------
burst            2000         2000
rate             2000         2000
state            on           on
statistics
  policer-cbs    11
  policer-cir    2000
  policer-id     22
  to-cpu-bytes   0
  to-cpu-pkts    0
  trap-group-id  4
  violated-pkts  0
```

If you enable PVRST mode, you must modify the `rpvst` trap group settings to scale to the maximum number of PVRST instances by setting the forwarding rate and the burst rate to 7200 pps:

{{< tabs "107 ">}}
{{< tab "NVUE Commands ">}}

```
cumulus@switch:~$ nv set system control-plane policer rpvst rate 7200
cumulus@switch:~$ nv set system control-plane policer rpvst burst 7200
cumulus@switch:~$ nv config apply
```

{{< /tab >}}
{{< tab "Linux Commands ">}}

1. Edit the `/etc/cumulus/control-plane/policers.conf` file to change the `copp.rpvst.rate` and `copp.rpvst.burst` parameters to 7200:

   ```
   cumulus@switch:~$ sudo nano /etc/cumulus/control-plane/policers.conf
   ...
   copp.rpvst.enable = TRUE
   copp.rpvst.rate = 7200
   copp.rpvst.burst = 7200
   ...
   ```

2. Run the following command to apply the change:

   ```
   cumulus@switch:~$ /usr/lib/cumulus/switchdctl --load /etc/cumulus/control-plane/policers.conf
   ```

{{< /tab >}}
{{< /tabs >}}

### STP Modes for a Traditional Bridge

{{<link url="Traditional-Bridge-Mode" text="Traditional bridges">}} operate in:
- <span class="a-tooltip">[PVST](## "Per-VLAN Spanning Tree")</span> mode, which creates a spanning tree instance for a bridge.
- <span class="a-tooltip">[PVRST](## "Per-VLAN Rapid Spanning Tree")</span> mode, which supports <span class="a-tooltip">[RSTP](## "Rapid Spanning Tree Protocol")</span> enhancements for each spanning tree instance. To use PVRST with a traditional bridge, you must create a bridge corresponding to the untagged native VLAN and all the physical switch ports must be part of the same VLAN.

{{%notice note%}}
- For maximum interoperability, when connected to a switch that has a native VLAN configuration, you **must** configure the native VLAN to VLAN 1.
- NVUE does not provide commands to configure a traditional mode bridge.
{{%/notice%}}

## STP Interoperability

This section discusses STP interoperability.

### RSTP and STP Interoperability

If a bridge running RSTP (802.1w) receives a common STP (802.1D) BPDU, it falls back to 802.1D automatically.

### RSTP and PVRST Interoperability

The RSTP domain sends <span class="a-tooltip">[BPDUs](## "Bridge Protocol Data Units")</span> on the native VLAN, whereas PVRST sends BPDUs on each VLAN along with IEEE BPDUS. For both protocols to work together, you need to enable the native VLAN on the link between the RSTP to PVRST domain; the spanning tree builds according to the native VLAN parameters.

The RSTP protocol does not send or parse BPDUs on other VLANs, but floods BPDUs across the network, enabling the PVRST domain to maintain its spanning-tree topology and provide a loop-free network.
- To enable proper BPDU exchange across the network, be sure to allow all VLANs participating in the PVRST domain on the link between the RSTP and PVRST domains.
- When using RSTP together with an existing PVRST network, you need to define the root bridge on the PVRST domain. Either lower the priority on the PVRST domain or change the priority of the RSTP switches to a higher number.
- When connecting a VLAN-aware bridge to a proprietary PVST+ switch using RSTP mode, you must allow VLAN 1 on all 802.1Q trunks that interconnect them, regardless of the configured *native* VLAN. Only VLAN 1 enables the switches to address the BPDU frames to the IEEE multicast MAC address.

### RSTP and MST Interoperability

RSTP works with <span class="a-tooltip">[MST](## "Multiple Spanning Tree")</span> seamlessly, creating a single instance of spanning tree that transmits BPDUs on the native VLAN.

RSTP treats the MST domain as one giant switch, whereas MST treats the RSTP domain as a different region. To ensure proper communication between the regions, MST creates a <span class="a-tooltip">[CST](## "Common Spanning Tree")</span> that connects all the boundary switches and forms the overall view of the MST domain. Because changes in the CST must reflect in all regions, the RSTP tree exists is in the CST to ensure that changes on the RSTP domain are in the CST domain. Topology changes on the RSTP domain impact the rest of the network but inform the MST domain of every change occurring in the RSTP domain, ensuring a loop-free network.

Configure the root bridge within the MST domain by changing the priority on the relevant MST switch. When MST detects an RSTP link, it falls back into RSTP mode. The MST domain chooses the switch with the lowest cost to the CST root bridge as the CIST root bridge.

### RSTP with MLAG

More than one spanning tree instance enables switches to load balance and use different links for different VLANs. With RSTP, there is only one instance of spanning tree. To better utilize the links, you can configure <span class="a-tooltip">[MLAG](## "Multi-chassis Link Aggregation")</span> on the switches connected to the <span class="a-tooltip">[MST](## "Multiple Spanning Tree")</span> domain and set up these interfaces as an MLAG port. The MST domain thinks it connects to a single switch and utilizes all the links connected to it. Load balancing depends on the port channel hashing mechanism instead of different spanning tree instances and uses all the links between the RSTP to MST domains. For information about configuring MLAG, see {{<link url="Multi-Chassis-Link-Aggregation-MLAG" text="Multi-Chassis Link Aggregation - MLAG">}}.

## Optional Configuration

The following section provides optional configuration commands.

### Spanning Tree Priority

If you are running STP for a VLAN-aware bridge in the default mode (RSTP) and you have a multiple spanning tree instance (MSTI 0, also known as a common spanning tree, or CST), you can set the tree priority for a bridge. The bridge with the lowest priority is the *root bridge*. The priority must be a number between *0* and *61440,* and must be a multiple of 4096. The default value is *32768*.

{{%notice note%}}
If you are running MLAG and have multiple bridges, the STP priority must be the same on all bridges on both peer switches.
{{%/notice%}}

The following example sets the tree priority to 8192:

{{< tabs "TabID288 ">}}
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

**Runtime Configuration (Advanced)**

{{%notice warning%}}
A runtime configuration is non-persistent, which means the configuration you create here does not persist after you reboot the switch.
{{%/notice%}}

Run the `sudo mstpctl settreeprio <bridge> <MSTI> <priority>` command:

```
cumulus@switch:~$ sudo mstpctl settreeprio br_default 0 8192
```

{{< /tab >}}
{{< /tabs >}}

{{%notice note%}}
Cumulus Linux supports MSTI 0 only. It does not support MSTI 1 through 15.
{{%/notice%}}

### Port Path Cost

You can configure the path cost for an interface in the bridge to influence the spanning tree forwarding path. You can specify a value between 1 and 200000000.

For PVRST mode, the port cost for a VLAN takes precedence over the cost for a port. If you do not configure the port cost for a VLAN, Cumulus Linux applies the port cost to all the interfaces in the VLAN. If you do not configure either the port cost for a VLAN or the cost for a port, Cumulus Linux bases the port cost on the link speed.

The following example sets the path cost to 4000.

{{< tabs "TabID356 ">}}
{{< tab "NVUE Commands ">}}

```
cumulus@switch:~$ nv set interface swp1 bridge domain br_default stp path-cost 4000
cumulus@switch:~$ nv config apply
```

{{< /tab >}}
{{< tab "Linux Commands ">}}

Add the `mstpctl-portpathcost` parameter under the interface stanza of the `/etc/network/interfaces` file.

```
cumulus@switch:~$ sudo nano /etc/network/interfaces
...
auto swp1
iface swp1
    mstpctl-bpduguard yes
    mstpctl-portadminedge yes
    mstpctl-portpathcost 4000
...
```

**Runtime Configuration (Advanced)**

{{%notice warning%}}
A runtime configuration is non-persistent, which means the configuration you create here does not persist after you reboot the switch.
{{%/notice%}}

To set path cost to 4000 at runtime:

```
cumulus@switch:~$ sudo mstpctl setportpathcost br_default swp1 4000
```

{{< /tab >}}
{{< /tabs >}}

### PVRST Bridge Priority

You can set the spanning tree bridge priority for a VLAN. The priority must be a number between 4096 and 61440 and must be a multiple of 4096. The default value is 32768.

{{< tabs "TabID520 ">}}
{{< tab "NVUE Commands ">}}

The following example sets the bridge priority to 4096 for VLAN 10 and to 61440 for VLAN 20:

```
cumulus@switch:~$ nv set bridge domain br_default stp vlan 10 bridge-priority 4096
cumulus@switch:~$ nv set bridge domain br_default stp vlan 20 bridge-priority 61440
cumulus@switch:~$ nv config apply
```

The following example sets the bridge priority to 61440 for VLAN 10, 20, and 30:

```
cumulus@switch:~$ nv set bridge domain br_default stp vlan 10,20,30 bridge-priority 61440
cumulus@switch:~$ nv config apply
```

To set the bridge priority for a range of VLANs, use a hyphen (-). For example, to set the bridge priority to 61440 for VLAN 10 through VLAN 30:

```
cumulus@switch:~$ nv set bridge domain br_default stp vlan 10-30 bridge-priority 61440
cumulus@switch:~$ nv config apply
```

{{< /tab >}}
{{< tab "Linux Commands ">}}

Add the `bridge-stp-vlan-priority` parameter under the bridge stanza of the `/etc/network/interfaces` file, then run the `ifreload -a` command.

The following example sets the bridge priority to 4096 for VLAN 10 and to 61440 for VLAN 20:

```
cumulus@switch:~$ sudo nano /etc/network/interfaces
...
auto br_default
iface br_default
    bridge-ports swp1 swp2
    hwaddress 44:38:39:22:01:b1
    bridge-vlan-aware yes
    bridge-vids 10 20
    bridge-pvid 1
    bridge-stp yes
    mstpctl-pvrst-mode yes
    bridge-stp-vlan-priority 10=4096 20=61440
...
```

```
cumulus@switch:~$ ifreload -a
```

The following example sets the bridge priority to 61440 for VLAN 10, 20, and 30:

```
cumulus@switch:~$ sudo nano /etc/network/interfaces
...
auto br_default
iface br_default
    bridge-ports swp1 swp2
    hwaddress 44:38:39:22:01:b1
    bridge-vlan-aware yes
    bridge-vids 10 20
    bridge-pvid 1
    bridge-stp yes
    mstpctl-pvrst-mode yes
    bridge-stp-vlan-priority 10=61440 20=61440 30=61440
...
```

```
cumulus@switch:~$ ifreload -a
```

To set the bridge priority for a range of VLANs, use a hyphen (-). For example, to set the bridge priority to 61440 for VLAN 10 through VLAN 30:

```
cumulus@switch:~$ sudo nano /etc/network/interfaces
...
auto br_default
iface br_default
    bridge-ports swp1 swp2
    hwaddress 44:38:39:22:01:b1
    bridge-vlan-aware yes
    bridge-vids 10 20
    bridge-pvid 1
    bridge-stp yes
    mstpctl-pvrst-mode yes
    bridge-stp-vlan-priority 10-30=61440
...
```

```
cumulus@switch:~$ ifreload -a
```
<!--
**Runtime Configuration (Advanced)**

{{%notice warning%}}
A runtime configuration is non-persistent, which means the configuration you create here does not persist after you reboot the switch.
{{%/notice%}}

To set the bridge priority to 4096 for VLAN 10 and  to 61440 for VLAN 20 at runtime:

```
cumulus@switch:~$ sudo mstpctl setvlan-priority br_default 10 4096
cumulus@switch:~$ sudo mstpctl setvlan-priority br_default 20 61440
```

To set the bridge priority to 61440 for VLAN 10, 20, and 30 at runtime:

```
cumulus@switch:~$ sudo mstpctl setvlan-priority br_default 10,20,30 61440
```

To set the bridge priority for a range of VLANs, use a hyphen (-). For example, to set the bridge priority to 61440 for VLAN 10 through VLAN 30 at runtime:

```
cumulus@switch:~$ sudo mstpctl setvlan-priority br_default 10-30 61440
```
-->
{{< /tab >}}
{{< /tabs >}}

### PVRST Timers

You can set the following PVRST timers:
- *Max age*, which is the maximum amount of time the switch retains STP information before discarding it. You can set a value between 6 and 40 seconds. The default value is 20 seconds.
- *Hello time*, which is how often to broadcast hello messages to other switches. You can set a value between 1 and 10 seconds. The default value is 2 seconds.
- *Forward delay*, which is the delay before changing the spanning tree state from blocking to forwarding. You can set a value between 4 and 30 seconds. The default value is 15 seconds.

{{%notice note%}}
The max age timer must be equal to or less than two times the forward delay minus one second (`bridge max age <= 2 * bridge foward delay - 1 second`).
{{%/notice%}}

{{< tabs "TabID549 ">}}
{{< tab "NVUE Commands ">}}

The following example sets the max age to 6 seconds, the hello time to 4 seconds, and the forward delay to 4 seconds for VLAN 10, 20, and 30.

```
cumulus@switch:~$ nv set bridge domain br_default stp vlan 10,20,30 max-age 6
cumulus@switch:~$ nv set bridge domain br_default stp vlan 10,20,30 hello-time 4 
cumulus@switch:~$ nv set bridge domain br_default stp vlan 10,20,30 forward-delay 4
cumulus@switch:~$ nv config apply
```

To set the PVRST timers for a range of VLANs, use a hyphen (-). For example `nv set bridge domain br_default stp vlan 10-30 max-age 6`.

{{< /tab >}}
{{< tab "Linux Commands ">}}

Add the `bridge-stp-vlan-maxage`, `bridge-stp-vlan-hello`, and `bridge-stp-vlan-fdelay` parameters under the bridge stanza in the `/etc/network/interfaces` file, then run the `ifreload -a` command.

The following example sets the max age to 6 seconds, the hello time to 4 seconds, and the forward delay to 4 seconds for VLAN 10, 20, and 30.

```
cumulus@switch:~$ sudo nano /etc/network/interfaces
...
auto br_default
iface br_default
    bridge-ports swp1 swp2
    hwaddress 44:38:39:22:01:b1
    bridge-vlan-aware yes
    bridge-vids 10 20
    bridge-pvid 1
    bridge-stp yes
    mstpctl-pvrst-mode yes
    bridge-stp-vlan-priority 10=4096
    bridge-stp-vlan-hello 10=4 20=4 30=4
    bridge-stp-vlan-fdelay 10=4 20=4 30=4
    bridge-stp-vlan-maxage 10=6 20=6 30=6
...
```

```
cumulus@switch:~$ ifreload -a
```

To set the PVRST timers for a range of VLANs, use a hyphen (-). For example `bridge-stp-vlan-hello 10-30=4`.
<!--
**Runtime Configuration (Advanced)**

{{%notice warning%}}
A runtime configuration is non-persistent, which means the configuration you create here does not persist after you reboot the switch.
{{%/notice%}}

To set the max age to 6 seconds, the hello time to 4 seconds, and the forward delay to 4 seconds for VLAN 10, 20, and 30 at runtime:

```
cumulus@switch:~$ sudo mstpctl setvlan-maxage br_default 10,20,30 6
cumulus@switch:~$ sudo mstpctl setvlan-hello br_default 10,20,30 4
cumulus@switch:~$ sudo mstpctl setvlan-fdelay br_default 10,20,30 4
```

To set the PVRST timers for a range of VLANs, use a hyphen (-). For example `sudo mstpctl setvlan-maxage br_default 10-30 6`.
-->
{{< /tab >}}
{{< /tabs >}}

### PVRST Port Settings

You can configure an interface port priority and path cost for each VLAN to influence the spanning tree forwarding path. You can specify a path cost between 1 and 200000000. You can specify a priority between 0 and 240; the value must be a multiple of 16.

The following examples set the path cost to 4000 and the priority to 240 for VLAN 10.

{{< tabs "TabID256 ">}}
{{< tab "NVUE Commands ">}}

```
cumulus@switch:~$ nv set interface swp1 bridge domain br_default stp vlan 10 path-cost 4000
cumulus@switch:~$ nv set interface swp1 bridge domain br_default stp vlan 10 priority 240
cumulus@switch:~$ nv config apply
```

{{< /tab >}}
{{< tab "Linux Commands ">}}

Add the `mstpctl-port-vlan-path-cost` and `mstpctl-port-vlan-priority` parameters under the interface stanza of the `/etc/network/interfaces` file:

```
cumulus@switch:~$ sudo nano /etc/network/interfaces
...
auto swp1
iface swp1
    bridge-access 10
    mstpctl-bpduguard yes
    mstpctl-portadminedge yes
    mstpctl-port-vlan-path-cost 10=4000
    mstpctl-port-vlan-priority 10=240
...
```
<!--
**Runtime Configuration (Advanced)**

{{%notice warning%}}
A runtime configuration is non-persistent, which means the configuration you create here does not persist after you reboot the switch.
{{%/notice%}}

To set path cost to 4000 and the priority to 240 for VLAN 10 at runtime:

```
cumulus@switch:~$ sudo mstpctl setvlantreeportcost br_default swp1 10 4000
cumulus@switch:~$ sudo mstpctl setvlantreeportprio br_default swp1 10 240
```
-->
{{< /tab >}}
{{< /tabs >}}

### PortAdminEdge (PortFast Mode)

*PortAdminEdge* is equivalent to the PortFast feature offered by other vendors. It enables or disables the *initial edge state* of a port in a bridge. All ports with PortAdminEdge bypass the listening and learning states and go straight to forwarding.

{{%notice warning%}}
PortAdminEdge mode causes loops if you do not use it with {{<link url="#bpdu-guard" text="BPDU guard">}}.
{{%/notice%}}

You typically configure edge ports as access ports for a simple end host. In the data center, edge ports connect to servers, which pass both tagged and untagged traffic.

The following example commands configure PortAdminEdge and BPDU guard for swp5:

{{< tabs "TabID122 ">}}
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
cumulus@switch:~$ sudo nano /etc/network/interfaces
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

{{< tabs "TabID180 ">}}
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

{{< tabs "TabID213 ">}}
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

{{< tabs "TabID235 ">}}
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

{{< tabs "TabID266 ">}}
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

To recover from the `protodown` state, remove the protodown reason and protodown from the interface with the NVUE `nv action clear interface <interface> bridge domain <domain> stp bpduguardviolation` command or the Linux `mstpctl clearbpduguardviolation <bridge> <interface>` command.

{{%notice note%}}
- Bringing up the disabled port does not correct the problem if the configuration on the connected end station does not resolve.
- If you remove the interface from the bridge while the interface is in a `protodown` state, you must use the `ip link set <interface> protodown off protodown_reason stp off` command to recover from the `protodown` state.
{{%/notice%}}

### Bridge Assurance

On a point-to-point link where RSTP is running, if you want to detect unidirectional links and put the port in a discarding state, you can enable bridge assurance on the port by enabling a port type network. The port is then in a bridge assurance inconsistent state until it receives a BPDU from the peer. You need to configure the port type network on both ends of the link for bridge assurance.

Cumulus Linux disables bridge assurance by default.

The following example commands enable bridge assurance on swp1:

{{< tabs "TabID331 ">}}
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

{{< tabs "TabID392 ">}}
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

{{< tabs "TabID437 ">}}
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

### Force Version Setting

By default, the switch sends RSTP type 2 BPDUs. You can configure the switch to send BPDU type 0 STP configuration BPDUs when you need to interoperate with other systems.

{{< tabs "TabID904 ">}}
{{< tab "NVUE Commands ">}}

```
cumulus@switch:~$ nv set bridge domain br_default stp force-protocol-version stp
cumulus@switch:~$ nv config apply
```

To change the setting back to the default, run the `nv set bridge domain <domain> stp force-protocol-version rstp` command.

{{< /tab >}}
{{< tab "Linux Commands ">}}

Edit the bridge stanza in the `/etc/network/interfaces` file to add the `mstpctl-forcevers stp` line, then run the `ifreload -a` command.

```
cumulus@switch:~$ sudo nano /etc/network/interfaces
...
auto br_default
iface br_default
    hwaddress 08:00:27:60:36:0b
    bridge-vlan-aware yes
    bridge-vids 10
    bridge-pvid 1
    bridge-stp yes
    bridge-mcsnoop no
    mstpctl-forcevers stp
    mstpctl-pvrst-mode yes
...
```

```
cumulus@switch:~$ sudo ifreload -a
```

To change the setting back to the default, change the line in the bridge stanza to `mstpctl-forcevers rstp`, then run the `ifreload -a` command.

{{< /tab >}}
{{< /tabs >}}

### Additional STP Settings

The table below describes additional STP configuration parameters available in Cumulus Linux. You can set these optional parameters manually by editing the `/etc/network/interfaces` file. Cumulus Linux does not provide NVUE commands for these parameters.

The IEEE {{<exlink url="https://standards.ieee.org/standard/802_1D-2004.html" text="802.1D">}} and {{<exlink url="https://standards.ieee.org/standard/802_1Q-2018.html" text="802.1Q">}} specifications describe STP parameters. For a comparison of STP parameter configuration between `mstpctl` and other vendors, [read this knowledge base article]({{<ref "/knowledge-base/Demos-and-Training/Interoperability/Cumulus-Linux-vs-Cisco-IOS-Spanning-Tree-Protocol" >}}).

| Parameter | Description |
|-----------|----------|
| `mstpctl-maxage` | Sets the maximum age of the bridge in seconds. The default is 20. The maximum age timer must be equal to, or less than, two times the forward delay minus one second (bridge max age <= 2 * bridge foward delay - 1 second).<br>Add this parameter to the bridge stanza of the `/etc/network/interfaces` file.<br>If you are running STP in PVRST mode, see {{<link title="Spanning Tree and Rapid Spanning Tree - STP/#pvrst-mode-for-a-vlan-aware-bridge" text="PVRST Mode for a VLAN-aware Bridge">}}.|
| `mstpctl-fdelay` | Sets the bridge forward delay time in seconds. The default value is 15. Two times the forward delay minus one second must be more than or equal to the maximum age (2 * bridge foward delay - 1 second  >= bridge max age).<br>Add this parameter to the bridge stanza of the `/etc/network/interfaces` file.<br>If you are running STP in PVRST mode, see {{<link title="Spanning Tree and Rapid Spanning Tree - STP/#pvrst-mode-for-a-vlan-aware-bridge" text="PVRST Mode for a VLAN-aware Bridge">}}.|
| `mstpctl-maxhops` | Sets the maximum hops for the bridge. The default is 20.<br>Add this parameter to the bridge stanza of the `/etc/network/interfaces` file.<br>This parameter does not apply to PVRST mode.|
| `mstpctl-txholdcount` | Sets the bridge transmit hold count. The default value is 6 seconds.<br>Add this parameter to the bridge stanza of the `/etc/network/interfaces` file.<br>In PVRST mode, the transmit hold count applies to each interface in the VLAN.  |
| `mstpctl-hello` | Sets the bridge hello time in seconds. The default is 2.<br>Add this parameter to the bridge stanza of the `/etc/network/interfaces` file.<br>If you are running STP in PVRST mode, see {{<link title="Spanning Tree and Rapid Spanning Tree - STP/#pvrst-mode-for-a-vlan-aware-bridge" text="PVRST Mode for a VLAN-aware Bridge">}}. |
| `mstpctl-portp2p` | Enables or disables point-to-point detection mode for the interface in the bridge.<br>Add this parameter to the interface stanza of the `/etc/network/interfaces` file.|
| `mstpctl-portrestrtcn` | Enables or disables the interface in the bridge to propagate received topology change notifications. The default is no.<br>Add this parameter to the interface stanza of the `/etc/network/interfaces` file.|
| `mstpctl-treeportcost` | Sets the spanning tree port cost to a value from 0 to 255. The default is 0.<br>Add this parameter to the interface stanza of the `/etc/network/interfaces` file.<br>This parameter applies to RSTP mode only.|

Be sure to run the `sudo ifreload -a` command after you set the STP parameter in the `/etc/network/interfaces` file.

## Troubleshooting

{{< tabs "TabID584 ">}}
{{< tab "NVUE Commands ">}}

To show the STP state for a bridge:

```
cumulus@switch:~$ nv show bridge domain br_default stp state
   operational  applied
   -----------  -------
   up           up
```

To show configuration information for a bridge interface:

```
cumulus@switch:~$ nv show interface swp1 bridge domain br_default
               operational  applied
-------------  -----------  -------
access         10           10     
learning       on           on     
stp                                
  admin-edge   on           on     
  auto-edge    on           on     
  bpdu-filter  off          off    
  bpdu-guard   on           on     
  network      off          off    
  path-cost    20000               
  restrrole    off          off    
  [vlan]                           
  state        forwarding 
```

To show STP configuration information for a bridge interface:

```
cumulus@switch:~$  nv show interface swp1 bridge domain br_default stp
             operational  applied
-----------  -----------  -------
admin-edge   on           on     
auto-edge    on           on     
bpdu-filter  off          off    
bpdu-guard   on           on     
network      off          off    
path-cost    20000               
restrrole    off          off    
[vlan]                           
state        forwarding
```

To show the STP information for a bridge, run the `nv show bridge domain br_default stp` command.

The following example shows the output in PVRST mode:

```
cumulus@switch:~$ nv show bridge domain br_default stp
Bridge
    mode    : pvrst
Vlan              Bridge ID               HelloTime   MaxAge      FwdDly   
        Priority         MAC-addr        (seconds)    (seconds)   (seconds)  
-----  ------------------------------    ----------  ----------  ----------
1      32769   44:38:39:22:01:7A            2           20          15     
10     4106    44:38:39:22:01:7A            4           6           4      
20     61460   44:38:39:22:01:7A            2           20          15     
30     32798   44:38:39:22:01:7A            2           20          15 
```

The following example shows the output in RSTP mode:

```
cumulus@switch:~$ nv show bridge domain br_default stp
Bridge
    mode    : rstp
    priority: 32768
    state   : up
Bridge ID                priority    : 32768   mac-address       : 44:38:39:22:01:8A   
Designated Root ID       priority    : 32768   mac-address       : 44:38:39:22:01:8A   root-port  : -
Timers                   hello-time  : 2s      forward-delay     : 15s                 max-age    : 20s
Max Hops                 max-hops    : 20      
Topology Change Network  count       : 1       time since change : 838s
                         change port : swp3    last change port  : swp2

Interface info: swp1
---------------------------------
port-id            : 128.1(priority: 128, num: 1)
role               : Designated
state              : forwarding
port-path-cost     : 20000
fdb-flush          : no
disputed           : no
...
```

To show PVRST information for the VLANs in a bridge:

```
cumulus@switch:~$ nv show bridge domain br_default stp vlan
Bridge Vlan: 1
--------------------------------------------------------------------------
Bridge ID                priority    : 32769   mac-address       : 44:38:39:22:01:B1   
Designated Root ID       priority    : 32769   mac-address       : 44:38:39:22:01:B1   root-port  : -
Timers                   hello-time  : 2s      forward-delay     : 15s                 max-age    : 20s
Topology Change Network  count       : 0       time since change : 1152s
                         change port : None    last change port  : None

Bridge Vlan: 10
--------------------------------------------------------------------------
Bridge ID                priority    : 4106    mac-address       : 44:38:39:22:01:B1   
Designated Root ID       priority    : 4106    mac-address       : 44:38:39:22:01:B1   root-port  : -
Timers                   hello-time  : 4s      forward-delay     : 4s                  max-age    : 6s
Topology Change Network  count       : 1       time since change : 1147s
                         change port : swp2    last change port  : swp1

Bridge Vlan: 20
--------------------------------------------------------------------------
Bridge ID                priority    : 32788   mac-address       : 44:38:39:22:01:B1   
Designated Root ID       priority    : 32788   mac-address       : 44:38:39:22:01:B1   root-port  : -
Timers                   hello-time  : 2s      forward-delay     : 15s                 max-age    : 20s
Topology Change Network  count       : 1       time since change : 1147s
                         change port : swp2    last change port  : swp1
```

To show PVRST information for a specific bridge VLAN:

```
cumulus@switch:~$ nv show bridge domain br_default stp vlan 10
Bridge ID                priority    : 4106    mac-address       : 44:38:39:22:01:B1   
Designated Root ID       priority    : 4106    mac-address       : 44:38:39:22:01:B1   root-port  : -
Timers                   hello-time  : 4s      forward-delay     : 4s                  max-age    : 6s
Topology Change Network  count       : 1       time since change : 1174s
                         change port : swp2    last change port  : swp1

Interface info: swp1
---------------------------------
port-id            : 8.001
role               : Designated
state              : forwarding
port-path-cost     : 20000
tx-hold-count      : 6
port-hello-time    : 4s
fdb-flush          : no
disputed           : no

Interface info: swp2
---------------------------------
port-id            : 8.002
role               : Designated
state              : forwarding
port-path-cost     : 20000
tx-hold-count      : 6
port-hello-time    : 4s
fdb-flush          : no
disputed           : no
```

To show STP information for the ports in a bridge:

```
cumulus@switch:~$ nv show bridge domain br_default stp port
Interface Info: bond1
--------------------------------------------------------------------------
enabled              : yes         mcheck            : no
admin-edge-port      : no          bpdu-guard-port   : no
auto-edge-port       : yes         bpdu-filter-port  : no
oper-edge-port       : yes         bpdu-guard-error  : no
admin-port-path-cost : 0           restricted-tcn    : no
port-path-cost       : 20000       restricted-role   : no
network-port         : no          ba-inconsistent   : no
clag-role            : primary     clag-system-mac   : 44:38:39:BE:EF:AA
clag-isl             : no          clag-isl-oper-up  : no
clag-dual-conn-mac   : 00:00:00:00:00:00

Interface Info: bond2
--------------------------------------------------------------------------
enabled              : yes         mcheck            : no
admin-edge-port      : no          bpdu-guard-port   : no
auto-edge-port       : yes         bpdu-filter-port  : no
oper-edge-port       : yes         bpdu-guard-error  : no
admin-port-path-cost : 0           restricted-tcn    : no
port-path-cost       : 20000       restricted-role   : no
network-port         : no          ba-inconsistent   : no
clag-role            : primary     clag-system-mac   : 44:38:39:BE:EF:AA
clag-isl             : no          clag-isl-oper-up  : no
clag-dual-conn-mac   : 00:00:00:00:00:00

Interface Info: bond3
--------------------------------------------------------------------------
enabled              : yes         mcheck            : no
admin-edge-port      : no          bpdu-guard-port   : no
auto-edge-port       : yes         bpdu-filter-port  : no
oper-edge-port       : yes         bpdu-guard-error  : no
admin-port-path-cost : 0           restricted-tcn    : no
port-path-cost       : 20000       restricted-role   : no
network-port         : no          ba-inconsistent   : no
clag-role            : primary     clag-system-mac   : 44:38:39:BE:EF:AA
clag-isl             : no          clag-isl-oper-up  : no
clag-dual-conn-mac   : 00:00:00:00:00:00
...
```

To show STP information for a specific bridge port:

```
cumulus@switch:~$ nv show bridge domain br_default stp port swp1
enabled              : yes         mcheck            : no
admin-edge-port      : no          bpdu-guard-port   : no
auto-edge-port       : yes         bpdu-filter-port  : no
oper-edge-port       : yes         bpdu-guard-error  : no
admin-port-path-cost : 0           restricted-tcn    : no
port-path-cost       : 20000       restricted-role   : no
network-port         : no          ba-inconsistent   : no
clag-role            : primary     clag-system-mac   : 44:38:39:BE:EF:AA
clag-isl             : no          clag-isl-oper-up  : no
clag-dual-conn-mac   : 00:00:00:00:00:00
```

To show the root ID and root cost for the bridge, run the `nv show bridge domain <bridge> stp root` command.

The following command shows the output in PVRST mode:

```
cumulus@switch:~$ nv show bridge domain br_default stp root
instance             root-id                root-cost  hello-time  fwd-dly     max-age      root-port
           Priority        MAC-addr                     (seconds)   (seconds)   (seconds)  
-------- --------------------------------  ----------  ----------  ----------  ----------  ----------
1        32769   44:38:39:22:01:7A            0           2           15          20          -      
10       4106    44:38:39:22:01:7A            0           4           4           6           -      
20       61460   44:38:39:22:01:7A            0           2           15          20          -      
30       32798   44:38:39:22:01:7A            0           2           15          20          -    
```

The following command shows the output in RSTP mode:

```
cumulus@switch:~$ nv show bridge domain br_default stp root
instance             root-id                root-cost  hello-time  fwd-dly     max-age      root-port
          Priority        MAC-addr                     (seconds)   (seconds)   (seconds)  
-------- --------------------------------  ----------  ----------  ----------  ----------  ----------
CIST     32768      44:38:39:22:01:8A            0           2           15          20          -      
```

To show STP counters for a bridge:

```
cumulus@switch:~$ nv show bridge domain br_default stp counters
port  tx-bpdu  rx-bpdu  tx-tcn  rx-tcn  fwd-trans  blk-trans  tx-pvst-tnl-bpdu  rx-pvst-tnl-bpdu
----  -------  -------  ------  ------  ---------  ---------  ----------------  ----------------
swp1  182      0        0       0       1          0          91                0               
swp2  296      0        2       0       2          1          297               0               
swp3  296      0        7       0       4          7          539               0
```

To show all blocked ports in the bridge:

```
cumulus@switch:~$ nv show bridge domain br_default stp blocked-ports
```

{{< /tab >}}
{{< tab "Linux Commands ">}}

To show the `mstpd` bridge port state, run the `mstpctl showstpport <bridge>` command.

The following command shows the output in RSTP mode:

```
cumulus@switch:~$ sudo mstpctl showstpport br_default
 E swp1  8.001 forw 8.000.44:38:39:22:01:8A 8.000.44:38:39:22:01:8A 8.001 Desg
 E swp2  8.002 forw 8.000.44:38:39:22:01:8A 8.000.44:38:39:22:01:8A 8.002 Desg
 E swp3  8.003 forw 8.000.44:38:39:22:01:8A 8.000.44:38:39:22:01:8A 8.003 Desg
```

The following command shows the output in PVRST mode:

```
cumulus@switch:~$ sudo mstpctl showstpport br_default
 E swp1 
  ---PTP Info---
Port: swp1 vid: 1
8.001  8.001.44:38:39:22:01:8A 8.001.44:38:39:22:01:8A 8.001 Desg
state: forw
  ---PTP Info---
Port: swp1 vid: 10
8.001  1.00A.44:38:39:22:01:8A 1.00A.44:38:39:22:01:8A 8.001 Desg
state: forw
  ---PTP Info---
Port: swp1 vid: 20
8.001  F.014.44:38:39:22:01:8A F.014.44:38:39:22:01:8A 8.001 Desg
state: forw
  ---PTP Info---
Port: swp1 vid: 30
8.001  8.01E.44:38:39:22:01:8A 8.01E.44:38:39:22:01:8A 8.001 Desg
state: forw
 E swp2 
...
```

To show STP information for a bridge domain, including STP counters, run the `sudo mstpctl showstpall` command.

The following command shows the output in RSTP mode:

```
cumulus@switch:~$ sudo mstpctl showstpall 

Global info 
  debug level       2

BRIDGE: br_default, Br_index: 58

Spanning-tree enabled protocol rstp
Bridge Parameters for br_default
  enabled                    yes
  force protocol version     rstp
  tx hold count              6
  hello time                 2s
  bridge forward delay       15s
  bridge max age             20s
  max hops                   20
  migrate_time               3s
  ageing time                300s
  if_index: 58, name: br_default, up: yes, vlan_filter: yes uptime: 1244
---CIST info---
  bridge id       8.000.44:38:39:22:01:8A
  designated root 8.000.44:38:39:22:01:8A
  regional root   8.000.44:38:39:22:01:8A
  path cost     0          internal path cost   0

  root port         none
  root max age       20        s
  root forward delay 15        s
  time since topology change 1239s
  topology change count      1
  topology change            no
  topology change port       swp3
  last topology change port  swp2
  PRSSM_state: role_selection
...
```

The following command shows the output in PVRST mode:

```
cumulus@switch:~$ sudo mstpctl showstpall 

Global info 
  debug level       2

BRIDGE: br_default, Br_index: 58

Spanning-tree enabled protocol rapid-pvst
Bridge Parameters for br_default
  enabled                    yes
  force protocol version     rstp
  tx hold count              6
  migrate_time               3s
  ageing time                300s
  if_index: 58, name: br_default, up: yes, vlan_filter: yes uptime: 141
---Bridge Vlan 1---
  bridge id       8.001.44:38:39:22:01:8A
  priority      32769      
  forward delay       15         
  Max_Age       20         
  Hello_Time       2          
  designated root 8.001.44:38:39:22:01:8A
  root path cost     0          
  root port         none
  root max age       20        s
  root forward delay 15        s
  time since topology change 141s
  topology change count      0
  topology change            no
  topology change port       None
  last topology change port  None
  PRSSM_state: role_selection
---Bridge Vlan 10---
  bridge id       1.00A.44:38:39:22:01:8A
  priority      4106       
  forward delay       4          
  Max_Age       6          
  Hello_Time       4          
  designated root 1.00A.44:38:39:22:01:8A
  root path cost     0          
  root port         none
  root max age       6         s
  root forward delay 4         s
  time since topology change 136s
  topology change count      1
  topology change            no
  topology change port       swp3
  last topology change port  swp2
  PRSSM_state: role_selection
  ...
```

To show the bridge state, run the `brctl show` command:

```
cumulus@switch:~$ sudo brctl show
  bridge name     bridge id               STP enabled     interfaces
  br_default      8000.001401010100       yes             swp1
                                                          swp2
                                                          swp3
```

{{%notice note%}}
`mstpd` is the preferred utility for interacting with STP on Cumulus Linux. `brctl` also provides certain tools for STP; however, they are not as complete and output from `brctl` is sometimes misleading.
{{%/notice%}}

{{< /tab >}}
{{< /tabs >}}

## Considerations

You must remove PVRST VLAN configuration before you remove the VLANs on the interface or bridge.

The following example removes PVRST VLAN 10 configuration, then removes VLAN 10 from the bridge:

```
cumulus@switch:~$ nv unset bridge domain br_default stp vlan 10
cumulus@switch:~$ nv unset bridge domain br_default vlan 10
```

The following example removes PVRST VLAN 10 configuration, then removes VLAN 10 from swp1:

```
cumulus@switch:~$ nv unset interface swp1 bridge domain br_default stp vlan 10
cumulus@switch:~$ nv unset interface swp1 bridge domain br_default vlan 10
```
