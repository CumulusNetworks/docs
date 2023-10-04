---
title: Cumulus Linux vs Cisco IOS - Spanning Tree Protocol
author: NVIDIA
weight: 514
toc: 4
---

## Issue

User already knows Cisco IOS format and wants translation to `mstpd` (the spanning tree protocol daemon for Linux).

Refer to the [STP parameter list]({{<ref "/cumulus-linux-43/Layer-2/Spanning-Tree-and-Rapid-Spanning-Tree#spanning-tree-parameter-list" >}}) for more information.

You can find the Cisco Configuration Guide used to interpret their commands {{<exlink url="http://www.cisco.com/c/en/us/td/docs/switches/lan/catalyst3750x_3560x/software/release/12-2_55_se/configuration/guide/3750xscg/swstp.html" text="here">}}.

## Spanning Tree Translation Table

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<tbody>
<tr>
<th>Cumulus Linux</th>
<th>Cisco Systems IOS</th>
<th>Description</th>
</tr>
<tr>
<td><pre><code>net add bridge stp maxage 20</code></pre>
Configured under the bridge</td>
<td><pre><code>spanning-tree vlan vlan-id max-age 20</code></pre>
Global configuration command</td>
<td>Sets the bridge/VLAN <em>maximum age</em> to <code>&lt;max_age&gt;</code> seconds. The default is 20 for both Operating Systems.</td>
</tr>
<tr>
<td><pre><code>net add bridge stp fdelay 15</code></pre>
Configured under the bridge</td>
<td><pre><code>spanning-tree vlan vlan-id forward-time seconds</code></pre>
Global configuration command</td>
<td>Sets the bridge/VLAN <em>forward delay</em> to <code>&lt;time&gt;</code> seconds. The default is 15 for both Operating Systems.</td>
</tr>
<tr>
<td><pre><code>net add bridge stp maxhops 20</code></pre>
Configured under the bridge</td>
<td><pre><code>spanning-tree vlan vlan-id root primary [ diameter net-diameter [ hello-time seconds ]]</code></pre>
Global configuration command</td>
<td>Sets the bridge's <em>maximum hops</em> to <code>&lt;max_hops&gt;</code>. The default on Cumulus Linux is <em>20</em>. On Cisco the range is 2 to 7 with the default being 7.</td>
</tr>
<tr>
<td><pre><code>net add bridge stp txholdcount 6</code></pre>
Configured under the bridge</td>
<td><pre><code>spanning-tree transmit hold-count value</code></pre>
<p>Global configuration command</p></td>
<!-- vale off --><td>Sets the bridge/VLAN <em>transmit hold count</em> to <code>&lt;tx_hold_count&gt;</code>. The default is 6 for both Operating Systems. Cisco describes this as "the number of BPDUs that can be sent before pausing for 1 second."</td><!-- vale on -->
</tr>
<tr>
<td><pre><code>net add bridge stp forcevers rstp</code></pre>
Configured under the bridge</td>
<td><pre><code>spanning-tree mode{ pvst | mst | rapid-pvst }</code></pre>
Global configuration command</td>
<td>Sets the bridge/VLAN to a particular spanning-tree mode (MST, RSTP, etc)</td>
</tr>
<tr>
<td><pre><code>net add bridge stp treeprio 32768</code></pre>
Configured under the bridge</td>
<td><pre><code>spanning-tree vlan vlan-id priority priority</code></pre>
Global configuration command</td>
<td>Configure the switch's priority of a bridge/VLAN. The default for both operating systems is 32768. The range is a number between 0 and 65535</td>
</tr>
<tr>
<td><pre><code>net add bridge stp hello 2</code></pre>
Configured under the bridge</td>
<td><pre><code>spanning-tree vlan vlan-id hello-time seconds</code></pre>
Global configuration command</td>
<td>Sets the bridge/VLAN hello time to &lt;time&gt; seconds. The default is 2 for both operating systems.</td>
</tr>
<tr>
<td><pre><code>net add interface swp10 stp portpathcost 10</code></pre>
Configured under an interface stanza</td>
<td><pre><code>spanning-tree vlan vlan-id cost cost</code></pre>
<p>-interface configuration command</p></td>
<td>Configure the cost for a bridge/VLAN. The range is 1 to 200000000. Cisco derives the cost from the media speed of the interface. On Cumulus Linux the default is 0.</td>
</tr>
<tr>
<td><pre><code>net add interface swp1 stp portadminedge yes</code></pre>
<p>Configured under the interface</p></td>
<td><pre><code>spanning-tree portfast default</code></pre>
<p>Global configuration command</p>
<pre><code>spanning-tree portfast</code></pre>
<p>-interface configuration command</p></td>
<td>Immediately brings an interface configured as an access or trunk port to the forwarding state from a blocking state, bypassing the listening and learning states.</td>
</tr>
<tr>
<td><pre><code>net add interface swp2 stp portautoedge yes</code></pre>
Configured under interface</td>
<td><pre><code>No Comparable Command</code></pre></td>
<td>Reception of BPDUs on a port determines whether port is an edge port or not. When the port is receiving no BPDUs it becomes an edge port.</td>
</tr>
<tr>
<td><pre><code>net add interface swp3 stp portp2p yes</code></pre>
<p>Configured under the interface</p></td>
<td><pre><code>spanning-tree link-type { point-to-point | shared }</code></pre>
<p>-interface configuration command</p></td>
<td>Enables/disables the point-to-point detection mode of the port &lt;port&gt; in bridge &lt;bridge&gt;. The default is <em>auto</em> on Cumulus Linux. Cisco determines the link-type by the duplex settings (p2p for full and shared for half).</td>
</tr>
<tr>
<td><pre><code>net add interface swp4 stp portrestrrole yes</code></pre>
Configured under the interface</td>
<td><pre><code>spanning-tree guard root</code></pre>
<p>-interface configuration command</p></td>
<td>Enables/disables the ability of the port &lt;port&gt; in bridge &lt;bridge&gt; to take the root role. The default is no.</td>
</tr>
<tr>
<td><pre><code>net add interface swp5 stp bpduguard yes</code></pre>
Configured under the interface</td>
<td><pre><code>spanning-tree portfast bpduguard default</code></pre>
Global configuration command, however only affects ports configured with
<pre><code>spanning-tree portfast</code></pre></td>
<td>Enables/disables the BPDU guard configuration</td>
</tr>
<tr>
<td><pre><code>net add interface swp6 stp portbpdufilter yes</code></pre>
Configured under the interface</td>
<td><pre><code>spanning-tree portfast bpdufilter default</code></pre>
Global configuration command, however only affects ports configured with
<pre><code>spanning-tree portfast</code></pre></td>
<td>Enables bpdufilter on a switch port, which filters BPDUs in both directions.</td>
</tr>
<tr>
<td><pre><code>net add interface swp7 stp portrestrtcn yes</code></pre>
Configured under the interface</td>
<td>no equivalent</td>
<td>Enables/disables the ability of the port &lt;port&gt; in bridge &lt;bridge&gt; to propagate received topology change notifications. The default is no.</td>
</tr>
<tr>
<td><pre><code>net add interface swp8 stp portnetwork yes</code></pre>
Configured under the interface</td>
<td><pre><code>spanning-tree bridge assurance</code></pre>
Global configuration command</td>
<td>Enables/disables the bridge assurance capability</td>
</tr>
<tr>
<td><pre><code>net add interface swp9 stp treeportprio 128</code></pre>
Configured under the interface</td>
<td><pre><code>spanning-tree port-priority priority</code></pre>
Configured under the interface</td>
<td>Configure the port priority for an interface. The default for both operating systems is 128.</td>
</tr>
</tbody>
</table>

## Full Configuration Example

    cumulus@switch:~$ cat /etc/network/interfaces
    
    auto bridge
    iface bridge
        bridge-ports glob swp1-10
        bridge-vlan-aware yes
        bridge-vids 1-2000
        bridge-pvid 1
        bridge-stp on
        mstpctl-maxhops 20
        mstpctl-maxage 20
    
    auto swp1
    iface swp1
        mstpctl-portadminedge yes
    
    auto swp2
    iface swp2
        mstpctl-portautoedge yes
    
    auto swp3
    iface swp3
        mstpctl-portp2p yes
    
    auto swp4
    iface swp4
        mstpctl-portrestrrole yes
    
    auto swp5
    iface swp5
        mstpctl-bpduguard yes
    
    auto swp6
    iface swp6
        mstpctl-portbpdufilter yes
    
    auto swp7
    iface swp7
        mstpctl-portrestrtcn yes
    
    auto swp8
    iface swp8
        mstpctl-portnetwork yes
    
    auto swp9
    iface swp9
        mstpctl-treeportprio 128
    
    auto swp10
    iface swp10
        mstpctl-portpathcost 10
