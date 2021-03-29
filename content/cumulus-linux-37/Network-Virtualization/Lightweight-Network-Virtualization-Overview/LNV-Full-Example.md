---
title: LNV Full Example
author: NVIDIA
weight: 377
pageID: 8362715
---
{{%notice warning%}}

As of Cumulus Linux 3.7.4, the lightweight network virtualization feature (LNV) has been deprecated. The feature will be removed in Cumulus Linux 4.0. Use {{<link url="Ethernet-Virtual-Private-Network-EVPN" text="Ethernet virtual private network (EVPN)">}} for network virtualization.

{{%/notice%}}

Lightweight Network Virtualization (LNV) is a technique for deploying
{{<link url="Network-Virtualization" text="VXLANs">}} without a central
controller on bare metal switches. This a full example complete with
diagram. Refer to the {{<link url="Lightweight-Network-Virtualization-Overview" text="LNV chapter">}}
for more detailed information. This full example uses the **recommended
way** of deploying LNV, which is to use anycast to load balance the
service nodes.

## Example LNV Configuration

The following images illustrate the configuration:

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Physical Cabling Diagram</p>
<p>{{% imgOld 0 %}}</p></td>
<td><p>Network Virtualization Diagram</p>
<p>{{% imgOld 1 %}}</p></td>
</tr>
</tbody>
</table>

{{%notice tip%}}

Want to try out configuring LNV and do not have a Cumulus Linux switch?
Check out {{<exlink url="https://cumulusnetworks.com/cumulus-vx/" text="Cumulus VX">}} .

{{%/notice%}}

{{%notice tip%}}

{{< img src="/images/old_doc_images/turtle_training.png" width="40">}}

Feeling overwhelmed? Come join a {{<exlink url="https://education.cumulusnetworks.com/series/bootcamps/" text="Cumulus Boot Camp">}} and get instructor-led training\!

{{%/notice%}}

### Layer 3 IP Addressing

Here is the configuration for the IP addressing information used in this
example:

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p><strong>spine1:</strong> <code>/etc/network/interfaces</code></p>
<pre><code>auto lo
iface lo inet loopback
  address 10.2.1.3/32
  address 10.10.10.10/32
 
auto eth0
iface eth0 inet dhcp
 
auto swp49
iface swp49
  address 10.1.1.2/30

auto swp50
iface swp50
  address 10.1.1.6/30

auto swp51
iface swp51
  address 10.1.1.50/30

auto swp52
iface swp52
  address 10.1.1.54/30</code></pre></td>
<td><p><strong>spine2:</strong> <code>/etc/network/interfaces</code></p>
<pre><code>auto lo
iface lo inet loopback
  address 10.2.1.4/32
  address 10.10.10.10/32

auto eth0
iface eth0 inet dhcp
 
auto swp49
iface swp49
 address 10.1.1.18/30

auto swp50
iface swp50
 address 10.1.1.22/30

auto swp51
iface swp51
address 10.1.1.34/30

auto swp52
iface swp52
address 10.1.1.38/30</code></pre></td>
</tr>
<tr class="even">
<td><p><strong>leaf1:</strong> <code>/etc/network/interfaces</code></p>
<pre><code>auto lo
iface lo inet loopback
  address 10.2.1.1/32
  vxrd-src-ip 10.2.1.1
  vxrd-svcnode-ip 10.10.10.10
 
auto eth0
iface eth0 inet dhcp
 
auto swp1s0
iface swp1s0
  address 10.1.1.1/30
 
auto swp1s1
iface swp1s1
  address 10.1.1.5/30
 
auto swp1s2
iface swp1s2
  address 10.1.1.33/30
 
auto swp1s3
iface swp1s3
  address 10.1.1.37/30
 
auto vni-10
iface vni-10
  vxlan-id 10
  vxlan-local-tunnelip 10.2.1.1
  mstpctl-bpduguard yes
  mstpctl-portbpdufilter yes
 
auto vni-2000
iface vni-2000
  vxlan-id 2000
  vxlan-local-tunnelip 10.2.1.1
  mstpctl-bpduguard yes
  mstpctl-portbpdufilter yes
 
auto vni-30
iface vni-30
  vxlan-id 30
  vxlan-local-tunnelip 10.2.1.1
  mstpctl-bpduguard yes
  mstpctl-portbpdufilter yes
 
auto br-10
iface br-10
  bridge-ports swp32s0.10 vni-10
 
auto br-20
iface br-20
  bridge-ports swp32s0.20 vni-2000
 
auto br-30
iface br-30
  bridge-ports swp32s0.30 vni-30</code></pre></td>
<td><p><strong>leaf2:</strong> <code>/etc/network/interfaces</code></p>
<pre><code>auto lo
iface lo inet loopback
  address 10.2.1.2/32
  vxrd-src-ip 10.2.1.2
  vxrd-svcnode-ip 10.10.10.10
 
auto eth0
iface eth0 inet dhcp
 
auto swp1s0
iface swp1s0 inet static
 address 10.1.1.17/30
 
auto swp1s1
iface swp1s1 inet static
 address 10.1.1.21/30
 
auto swp1s2
iface swp1s2 inet static
 address 10.1.1.49/30
 
auto swp1s3
iface swp1s3 inet static
 address 10.1.1.53/30
 
auto vni-10
iface vni-10
  vxlan-id 10
  vxlan-local-tunnelip 10.2.1.2
  mstpctl-bpduguard yes
  mstpctl-portbpdufilter yes
 
auto vni-2000
iface vni-2000
  vxlan-id 2000
  vxlan-local-tunnelip 10.2.1.2
  mstpctl-bpduguard yes
  mstpctl-portbpdufilter yes
 
auto vni-30
iface vni-30
  vxlan-id 30
  vxlan-local-tunnelip 10.2.1.2
  mstpctl-bpduguard yes
  mstpctl-portbpdufilter yes
 
auto br-10
iface br-10
  bridge-ports swp32s0.10 vni-10
 
auto br-20
iface br-20
  bridge-ports swp32s0.20 vni-2000
 
auto br-30
iface br-30
  bridge-ports swp32s0.30 vni-30</code></pre></td>
</tr>
</tbody>
</table>

### FRRouting Configuration

The service nodes and registration nodes must all be routable between
each other. The layer 3 fabric on Cumulus Linux can either be
{{<link url="Border-Gateway-Protocol-BGP/" text="BGP">}} or
{{<link url="Open-Shortest-Path-First-OSPF" text="OSPF">}}. In this
example, OSPF is used to demonstrate full reachability.

Here is the FRRouting configuration using OSPF:

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p><strong>spine1:</strong>/etc/frr/frr.conf</p>
<pre><code>interface lo
 ip ospf area 0.0.0.0
interface swp49
 ip ospf network point-to-point
 ip ospf area 0.0.0.0
!
interface swp50
 ip ospf network point-to-point
 ip ospf area 0.0.0.0
!
interface swp51
 ip ospf network point-to-point
 ip ospf area 0.0.0.0
!
interface swp52
 ip ospf network point-to-point
 ip ospf area 0.0.0.0
!
!
!
!
!
router-id 10.2.1.3
router ospf
 ospf router-id 10.2.1.3</code></pre></td>
<td><p><strong>spine2:</strong> /etc/frr/frr.conf</p>
<pre><code>interface lo
 ip ospf area 0.0.0.0
interface swp49
 ip ospf network point-to-point
 ip ospf area 0.0.0.0
!
interface swp50
 ip ospf network point-to-point
 ip ospf area 0.0.0.0
!
interface swp51
 ip ospf network point-to-point
 ip ospf area 0.0.0.0
!
interface swp52
 ip ospf network point-to-point
 ip ospf area 0.0.0.0
!
!
!
!
!
router-id 10.2.1.4
router ospf
 ospf router-id 10.2.1.4</code></pre></td>
</tr>
<tr class="even">
<td><p><strong>leaf1:</strong> /etc/frr/frr.conf</p>
<pre><code>interface lo
 ip ospf area 0.0.0.0
interface swp1s0
 ip ospf network point-to-point
 ip ospf area 0.0.0.0
!
interface swp1s1
 ip ospf network point-to-point
 ip ospf area 0.0.0.0
!
interface swp1s2
 ip ospf network point-to-point
 ip ospf area 0.0.0.0
!
interface swp1s3
 ip ospf network point-to-point
 ip ospf area 0.0.0.0
!
!
!
!
!
router-id 10.2.1.1
router ospf
 ospf router-id 10.2.1.1</code></pre></td>
<td><p><strong>leaf2:</strong> /etc/frr/frr.conf</p>
<pre><code>interface lo
 ip ospf area 0.0.0.0
interface swp1s0
 ip ospf network point-to-point
 ip ospf area 0.0.0.0
!
interface swp1s1
 ip ospf network point-to-point
 ip ospf area 0.0.0.0
!
interface swp1s2
 ip ospf network point-to-point
 ip ospf area 0.0.0.0
!
interface swp1s3
 ip ospf network point-to-point
 ip ospf area 0.0.0.0
!
!
!
!
!
router-id 10.2.1.2
router ospf
 ospf router-id 10.2.1.2</code></pre></td>
</tr>
</tbody>
</table>

### Host Configuration

In this example, the servers are running Ubuntu 14.04. You must map a
trunk from server1 and server2 to the respective switch. In Ubuntu, this
is done with subinterfaces.

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p><strong>server1</strong></p>
<pre><code>auto eth3.10
iface eth3.10 inet static
  address 10.10.10.1/24
 
auto eth3.20
iface eth3.20 inet static
  address 10.10.20.1/24
 
auto eth3.30
iface eth3.30 inet static
  address 10.10.30.1/24</code></pre></td>
<td><p><strong>server2</strong></p>
<pre><code>auto eth3.10
iface eth3.10 inet static
  address 10.10.10.2/24
 
auto eth3.20
iface eth3.20 inet static
  address 10.10.20.2/24
 
auto eth3.30
iface eth3.30 inet static
  address 10.10.30.2/24</code></pre></td>
</tr>
</tbody>
</table>

### Service Node Configuration

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p><strong>spine1</strong>:/etc/vxsnd.conf</p>
<pre><code>[common]
# Log level is one of DEBUG, INFO, WARNING, ERROR, CRITICAL
#loglevel = INFO
# Destination for log message.  Can be a file name, &#39;stdout&#39;, or &#39;syslog&#39;
#logdest = syslog
# log file size in bytes. Used when logdest is a file
#logfilesize = 512000
# maximum number of log files stored on disk. Used when logdest is a file
#logbackupcount = 14
# The file to write the pid. If using monit, this must match the one
# in the vxsnd.rc
#pidfile = /var/run/vxsnd.pid
# The file name for the unix domain socket used for mgmt.
#udsfile = /var/run/vxsnd.sock
# UDP port for vxfld control messages
#vxfld_port = 10001
# This is the address to which registration daemons send control messages for
# registration and/or BUM packets for replication
svcnode_ip = 10.10.10.10
# Holdtime (in seconds) for soft state. It is used when sending a
# register msg to peers in response to learning a &lt;vni, addr&gt; from a
# VXLAN data pkt
#holdtime = 90
# Local IP address to bind to for receiving inter-vxsnd control traffic
src_ip = 10.2.1.3
[vxsnd]
# Space separated list of IP addresses of vxsnd to share state with
svcnode_peers = 10.2.1.4
# When set to true, the service node will listen for vxlan data traffic
# Note: Use 1, yes, true, or on, for True and 0, no, false, or off,
# for False
#enable_vxlan_listen = true
# When set to true, the svcnode_ip will be installed on the loopback
# interface, and it will be withdrawn when the vxsnd is no longer in
# service.  If set to true, the svcnode_ip configuration
# variable must be defined.
# Note: Use 1, yes, true, or on, for True and 0, no, false, or off,
# for False
#install_svcnode_ip = false
# Seconds to wait before checking the database to age out stale entries
#age_check = 90</code></pre></td>
<td><p><strong>spine2</strong>:/etc/vxsnd.conf</p>
<pre><code>[common]
# Log level is one of DEBUG, INFO, WARNING, ERROR, CRITICAL
#loglevel = INFO
# Destination for log message.  Can be a file name, &#39;stdout&#39;, or &#39;syslog&#39;
#logdest = syslog
# log file size in bytes. Used when logdest is a file
#logfilesize = 512000
# maximum number of log files stored on disk. Used when logdest is a file
#logbackupcount = 14
# The file to write the pid. If using monit, this must match the one
# in the vxsnd.rc
#pidfile = /var/run/vxsnd.pid
# The file name for the unix domain socket used for mgmt.
#udsfile = /var/run/vxsnd.sock
# UDP port for vxfld control messages
#vxfld_port = 10001
# This is the address to which registration daemons send control messages for
# registration and/or BUM packets for replication
svcnode_ip = 10.10.10.10
# Holdtime (in seconds) for soft state. It is used when sending a
# register msg to peers in response to learning a &lt;vni, addr&gt; from a
# VXLAN data pkt
#holdtime = 90
# Local IP address to bind to for receiving inter-vxsnd control traffic
src_ip = 10.2.1.4
[vxsnd]
# Space separated list of IP addresses of vxsnd to share state with
svcnode_peers = 10.2.1.3
# When set to true, the service node will listen for vxlan data traffic
# Note: Use 1, yes, true, or on, for True and 0, no, false, or off,
# for False
#enable_vxlan_listen = true
# When set to true, the svcnode_ip will be installed on the loopback
# interface, and it will be withdrawn when the vxsnd is no longer in
# service.  If set to true, the svcnode_ip configuration
# variable must be defined.
# Note: Use 1, yes, true, or on, for True and 0, no, false, or off,
# for False
#install_svcnode_ip = false
# Seconds to wait before checking the database to age out stale entries
#age_check = 90</code></pre></td>
</tr>
</tbody>
</table>

## Related Information

  - {{<exlink url="https://tools.ietf.org/html/rfc7348" text="RFC 7348">}}
  - {{<exlink url="http://en.wikipedia.org/wiki/Anycast" text="Wikipedia - Anycast">}}
  - {{<link url="Lightweight-Network-Virtualization-Overview" text="Detailed LNV Configuration Guide">}}
  - {{<exlink url="http://cumulusnetworks.com/education/instructor-led-training/" text="Cumulus Linux Training">}}
  - {{<link url="Network-Virtualization" text="Network virtualization chapter, Cumulus Linux user guide">}}
