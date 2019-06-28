---
title: Lightweight Network Virtualization - LNV
author: Cumulus Networks
weight: 289
aliases:
 - /display/CL31/Lightweight+Network+Virtualization+-+LNV
 - /pages/viewpage.action?pageId=5122049
pageID: 5122049
product: Cumulus Linux
version: 3.1.2
imgData: cumulus-linux-312
siteSlug: cumulus-linux-312
---
Lightweight Network Virtualization (LNV) is a technique for deploying
[VXLANs](/version/cumulus-linux-312/Layer_1_and_Layer_2_Features/Network_Virtualization/)
without a central controller on bare metal switches. This solution
requires no external controller or software suite; it runs the VXLAN
service and registration daemons on Cumulus Linux itself. The data path
between bridge entities is established on top of a layer 3 fabric by
means of a simple service node coupled with traditional MAC address
learning.

To see an example of a full solution before reading the following
background information, [please read this
chapter](/version/cumulus-linux-312/Layer_1_and_Layer_2_Features/Network_Virtualization/Lightweight_Network_Virtualization_-_LNV/LNV_Full_Example).

{{%notice note%}}

LNV is a lightweight controller option. Please [contact Cumulus
Networks](https://support.cumulusnetworks.com/hc/en-us/requests/new)
with your scale requirements so we can make sure this is the right fit
for you. There are also other controller options that can work on
Cumulus Linux.

{{%/notice%}}

## <span>Understanding LNV Concepts</span>

To best describe this feature, consider the following example
deployment:

{{% imgOld 0 %}}

The two switches running Cumulus Linux, called leaf1 and leaf2, each
have a bridge configured. These two bridges contain the physical switch
port interfaces connecting to the servers as well as the logical VXLAN
interface associated with the bridge. By creating a logical VXLAN
interface on both leaf switches, the switches become *VTEPs* (virtual
tunnel end points). The IP address associated with this VTEP is most
commonly configured as its loopback address — in the image above, the
loopback address is 10.2.1.1 for leaf1 and 10.2.1.2 for leaf2.

### <span>Acquiring the Forwarding Database at the Service Node</span>

In order to connect these two VXLANs together and forward BUM
(Broadcast, Unknown-unicast, Multicast) packets to members of a VXLAN,
the service node needs to acquire the addresses of all the VTEPs for
every VXLAN it serves. The service node daemon does this through a
registration daemon running on each leaf switch that contains a VTEP
participating in LNV. The registration process informs the service node
of all the VXLANs to which the switch belongs.

### <span>MAC Learning and Flooding</span>

With LNV, as with traditional bridging of physical LANs or VLANs, a
bridge automatically learns the location of hosts as a side effect of
receiving packets on a port.

For example, when server1 sends an L2 packet to server3, leaf2 learns
that server1's MAC address is located on that particular VXLAN, and the
VXLAN interface learns that the IP address of the VTEP for server1 is
10.2.1.1. So when server3 sends a packet to server1, the bridge on leaf2
forwards the packet out of the port to the VXLAN interface and the VXLAN
interface sends it, encapsulated in a UDP packet, to the address
10.2.1.1.

But what if server3 sends a packet to some address that has yet to send
it a packet (server2, for example)? In this case, the VXLAN interface
sends the packet to the service node, which sends a copy to every other
VTEP that belongs to the same VXLAN.

### <span>Handling BUM Traffic</span>

Cumulus Linux has two ways of handling BUM (Broadcast Unknown-unicast
and Multicast) traffic:

  - Head end replication

  - Service node replication

Head end replication is enabled by default in Cumulus Linux.

{{%notice warning%}}

You cannot have both service node and head end replication configured
simultaneously, as this causes the BUM traffic to be duplicated — both
the source VTEP and the service node sending their own copy of each
packet to every remote VTEP.

{{%/notice%}}

#### <span id="src-5122049_LightweightNetworkVirtualization-LNV-head-end" class="confluence-anchor-link"></span><span>Head End Replication</span>

The Tomahawk, Trident II+ and Trident II chipsets are capable of head
end replication — the ability to generate all the BUM traffic in
hardware. The most scalable solution available with LNV is to have each
VTEP (top of rack switch) generate all of its own BUM traffic rather
than relying on an external service node.

Cumulus Linux verified support for up to 128 VTEPs with head end
replication.

To disable head end replication, edit `/etc/vxrd.conf` and set
`head_rep` to *False*.

#### <span>Service Node Replication</span>

Cumulus Linux also supports service node replication for VXLAN BUM
packets. This is useful with LNV if you have more than 128 VTEPs.
However, it is not recommended because it forces the spine switches
running the `vxsnd` (service node daemon) to replicate the packets in
software instead of in hardware, unlike head end replication. If you're
not using a controller but have more than 128 VTEPs, contact [Cumulus
Networks](mailto:support@cumulusnetworks.com).

To enable service node replication:

1.  Disable head end replication; set `head_rep` to *False* in
    `/etc/vxrd.conf`.

2.  Edit `/etc/network/interfaces` and configure a service node IP
    address for VXLAN interfaces using `vxrd-svcnode-ip <>`.

3.  Edit `/etc/vxsnd.conf`, and configure the following:
    
      - Set the same service node IP address that you did in the
        previous step:
        
            svcnode_ip = <>
    
      - To forward VXLAN data traffic, set the following variable to
        *True*:
        
            enable_vxlan_listen = true

## <span>Requirements</span>

### <span>Hardware Requirements</span>

  - Switches with a Tomahawk, Trident II+ or Trident II chipset running
    Cumulus Linux 2.5.4 or later. Please refer to the Cumulus Networks
    [hardware compatibility
    list](http://cumulusnetworks.com/support/linux-hardware-compatibility-list/)
    for a list of supported switch models.

### <span>Configuration Requirements</span>

  - The VXLAN has an associated **V**XLAN **N**etwork **I**dentifier
    (VNI), also interchangeably called a VXLAN ID.

  - The VNI should not be 0 or 16777215, as these two numbers are
    reserved values under Cumulus Linux.

  - The VXLAN link and physical interfaces are added to the bridge to
    create the association between the port, VLAN and VXLAN instance.

  - Each bridge on the switch has only one VXLAN interface. Cumulus
    Linux does not support more than one VXLAN link in a bridge;
    however, a switch can have multiple bridges.

  - An SVI (Switch VLAN Interface) or L3 address on the bridge is not
    supported. For example, you can't ping from the leaf1 SVI to the
    leaf2 SVI via the VXLAN tunnel; you would need to use server1 and
    server2 to verify. See [Creating a Layer 3
    Gateway](#src-5122049_LightweightNetworkVirtualization-LNV-l3gateway)
    below for more information.

### <span>Installing the LNV Packages</span>

`vxfld` is installed by default on all new installations of Cumulus
Linux 3.x. If you are upgrading from an earlier version, run `sudo
apt-get install python-vxfld` to install the LNV package.

## <span>Sample LNV Configuration</span>

The following images illustrate the configuration that is referenced
throughout this chapter.

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Physical Cabling Diagram</p>
<p>{{% imgOld 1 %}}</p></td>
<td><p>Network Virtualization Diagram</p>
<p>{{% imgOld 2 %}}</p></td>
</tr>
</tbody>
</table>

{{%notice tip%}}

Want to try out configuring LNV and don't have a Cumulus Linux switch?
Check out [Cumulus VX](https://cumulusnetworks.com/cumulus-vx/).

{{%/notice%}}

### <span>Network Connectivity</span>

There must be full network connectivity before you can configure LNV.
The layer 3 IP addressing information as well as the OSPF configuration
(`/etc/quagga/Quagga.conf`) below is provided to make the LNV example
easier to understand.

{{%notice info%}}

OSPF is not a requirement for LNV, LNV just requires L3 connectivity.
With Cumulus Linux this can be achieved with static routes, OSPF or BGP.

{{%/notice%}}

### <span>Layer 3 IP Addressing</span>

Here is the configuration for the IP addressing information used in this
example.

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
  address 10.1.1.37/30</code></pre></td>
<td><p><strong>leaf2:</strong> <code>/etc/network/interfaces</code></p>
<pre><code>auto lo
iface lo inet loopback
  address 10.2.1.2/32
 
auto eth0
iface eth0 inet dhcp
 
auto swp1s0
iface swp1s0
 address 10.1.1.17/30
              
auto swp1s1
iface swp1s1
 address 10.1.1.21/30
              
auto swp1s2
iface swp1s2
 address 10.1.1.49/30
              
auto swp1s3
iface swp1s3
 address 10.1.1.53/30</code></pre></td>
</tr>
</tbody>
</table>

### <span>Layer 3 Fabric</span>

The service nodes and registration nodes must all be routable between
each other. The L3 fabric on Cumulus Linux can either be
[BGP](/version/cumulus-linux-312/Layer_3_Features/Border_Gateway_Protocol_-_BGP)
or
[OSPF](/version/cumulus-linux-312/Layer_3_Features/Open_Shortest_Path_First_-_OSPF_-_Protocol).
In this example, OSPF is used to demonstrate full reachability. Expand
the Quagga configurations below.

Quagga configuration using OSPF:

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p><strong>spine1</strong></p>
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
<td><p><strong>spine2</strong></p>
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
<td><p><strong>leaf1</strong></p>
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
<td><p><strong>leaf2</strong></p>
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

### <span>Host Configuration</span>

In this example, the servers are running Ubuntu 14.04. There needs to be
a trunk mapped from server1 and server2 to the respective switch. In
Ubuntu this is done with subinterfaces. You can expand the
configurations below.

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

On Ubuntu it is more reliable to use `ifup` and `if down` to bring the
interfaces up and down individually, rather than restarting networking
entirely (that is, there is no equivalent to `if reload` like there is
in Cumulus Linux):

    cumulus@server1:~$ sudo ifup eth3.10
    Set name-type for VLAN subsystem. Should be visible in /proc/net/vlan/config
    Added VLAN with VID == 10 to IF -:eth3:-
    cumulus@server1:~$ sudo ifup eth3.20
    Set name-type for VLAN subsystem. Should be visible in /proc/net/vlan/config
    Added VLAN with VID == 20 to IF -:eth3:-
    cumulus@server1:~$ sudo ifup eth3.30
    Set name-type for VLAN subsystem. Should be visible in /proc/net/vlan/config
    Added VLAN with VID == 30 to IF -:eth3:-

## <span id="src-5122049_LightweightNetworkVirtualization-LNV-mapping" class="confluence-anchor-link"></span><span>Configuring the VLAN to VXLAN Mapping</span>

Configure the VLANS and associated VXLANs. In this example, there are 3
VLANs and 3 VXLAN IDs (VNIs). VLANs 10, 20 and 30 are used and
associated with VNIs 10, 2000 and 30 respectively. The loopback address,
used as the `vxlan-local-tunnelip`, is the only difference between leaf1
and leaf2 for this demonstration.

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>For leaf1:</p>
<pre><code>cumulus@leaf1$ sudo nano /etc/network/interfaces</code></pre>
<p>Add the following to the loopback stanza</p>
<pre><code>auto lo
iface lo 
  vxrd-src-ip 10.2.1.1
  vxrd-svcnode-ip 10.2.1.3</code></pre>
<p>Now append the following for the VXLAN configuration itself:</p>
<pre><code>auto vni-10
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
  bridge-ports swp32s0.30 vni-30</code></pre>
<p>To bring up the bridges and VNIs, use the <code>ifreload</code> command:</p>
<pre><code>cumulus@leaf1$ sudo ifreload -a</code></pre></td>
<td><p>For leaf2:</p>
<pre><code>cumulus@leaf2$ sudo nano /etc/network/interfaces</code></pre>
<p>Add the following to the loopback stanza</p>
<pre><code>auto lo
iface lo 
  vxrd-src-ip 10.2.1.2
  vxrd-svcnode-ip 10.2.1.3</code></pre>
<p>Now append the following for the VXLAN configuration itself:</p>
<pre><code>auto vni-10
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
  bridge-ports swp32s0.30 vni-30</code></pre>
<p>To bring up the bridges and VNIs, use the <code>ifreload</code> command:</p>
<pre><code>cumulus@leaf2$ sudo ifreload -a</code></pre></td>
</tr>
</tbody>
</table>

{{%notice info%}}

Why is br-20 not vni-20? For example, why not tie VLAN 20 to VNI 20, or
why was 2000 used? VXLANs and VLANs do not need to be the same number.
This was done on purpose to highlight this fact. However if you are
using fewer than 4096 VLANs, there is no reason not to make it easy and
correlate VLANs to VXLANs. It is completely up to you.

{{%/notice%}}

## <span>Verifying the VLAN to VXLAN Mapping</span>

Use the `brctl show` command to see the physical and logical interfaces
associated with that bridge:

    cumulus@leaf1:~$ brctl show
    bridge name bridge id           STP enabled     interfaces
    br-10       8000.443839008404   no              swp32s0.10
                                                    vni-10
    br-20       8000.443839008404   no              swp32s0.20
                                                    vni-2000
    br-30       8000.443839008404   no              swp32s0.30
                                                    vni-30

As with any logical interfaces on Linux, the name does not matter (other
than a 15-character limit). To verify the associated VNI for the logical
name, use the `ip -d link show` command:

    cumulus@leaf1$ ip -d link show vni-10
    43: vni-10: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue master br-10 state UNKNOWN mode DEFAULT
        link/ether 02:ec:ec:bd:7f:c6 brd ff:ff:ff:ff:ff:ff
        vxlan id 10 srcport 32768 61000 dstport 4789 ageing 300
        bridge_slave

The *vxlan id 10* indicates the VXLAN ID/VNI is indeed 10 as the logical
name suggests.

## <span>Enabling and Managing Service Node and Registration Daemons</span>

Every VTEP must run the registration daemon (`vxrd`). Typically, every
leaf switch acts as a VTEP. A minimum of 1 switch (a switch not already
acting as a VTEP) must run the service node daemon (`vxsnd`). The
instructions for enabling these daemons follows.

### <span>Enabling the Service Node Daemon</span>

The service node daemon (`vxsnd)` is included in the Cumulus Linux
repository as `vxfld-vxsnd`. The service node daemon can run on any
switch running Cumulus Linux as long as that switch is not also a VXLAN
VTEP. In this example, enable the service node only on the spine1
switch, then reboot it.

    cumulus@spine1$ sudo systemctl enable vxsnd.service
    cumulus@spine1$ sudo systemctl restart vxsnd.service

{{%notice warning%}}

Do not run `vxsnd` on a switch that is already acting as a VTEP.

{{%/notice%}}

### <span>Enabling the Registration Daemon</span>

The registration daemon (`vxrd`) is included in the Cumulus Linux
package as `vxfld-vxrd`. The registration daemon must run on each VTEP
participating in LNV, so you must enable it on every TOR (leaf) switch
acting as a VTEP, then reboot the `vxrd` daemon. For example, on leaf1:

    cumulus@leaf1$ sudo systemctl enable vxrd.service
    cumulus@leaf1$ sudo systemctl restart vxrd.service

Then enable and reboot the `vxrd` daemon on leaf2:

    cumulus@leaf2$ sudo systemctl enable vxrd.service
    cumulus@leaf2$ sudo systemctl restart vxrd.service

### <span>Checking the Daemon Status</span>

To determine if the daemon is running, use the `systemctl status <daemon
name>.service` command.

For the service node daemon:

    cumulus@spine1$ sudo systemctl status vxsnd.service
    ● vxsnd.service - Lightweight Network Virt Discovery Svc and Replicator
       Loaded: loaded (/lib/systemd/system/vxsnd.service; enabled)
       Active: active (running) since Wed 2016-05-11 11:42:55 UTC; 10min ago
     Main PID: 774 (vxsnd)
       CGroup: /system.slice/vxsnd.service
               └─774 /usr/bin/python /usr/bin/vxsnd
     
    May 11 11:42:55 cumulus vxsnd[774]: INFO: Starting (pid 774) ...

For the registration daemon:

    cumulus@leaf1$ sudo systemctl status vxrd.service 
    ● vxrd.service - Lightweight Network Virtualization Peer Discovery Daemon
       Loaded: loaded (/lib/systemd/system/vxrd.service; enabled)
       Active: active (running) since Wed 2016-05-11 11:42:55 UTC; 10min ago
     Main PID: 929 (vxrd)
       CGroup: /system.slice/vxrd.service
               └─929 /usr/bin/python /usr/bin/vxrd
     
    May 11 11:42:55 cumulus vxrd[929]: INFO: Starting (pid 929) ...

## <span id="src-5122049_LightweightNetworkVirtualization-LNV-regnode" class="confluence-anchor-link"></span><span>Configuring the Registration Node</span>

The registration node was configured earlier in
`/etc/network/interfaces` in the [VXLAN
mapping](#src-5122049_LightweightNetworkVirtualization-LNV-mapping)
section above; no additional configuration is typically needed. However,
if you need to modify the registration node configuration, edit
`/etc/vxrd.conf`.

Alternate location for configuration and additional knobs for the
registration node are found in /etc/vxrd.conf

    cumulus@leaf1$ sudo nano /etc/vxrd.conf

Then edit the `svcnode_ip` variable:

    svcnode_ip = 10.2.1.3

Then perform the same on leaf2:

    cumulus@leaf2$ sudo nano /etc/vxrd.conf

And again edit the `svcnode_ip` variable:

    svcnode_ip = 10.2.1.3

Enable, then restart the registration node daemon for the change to take
effect:

    cumulus@leaf1$ sudo systemctl enable vxrd.service
    cumulus@leaf1$ sudo systemctl restart vxrd.service

Restart the daemon on leaf2:

    cumulus@leaf2$ sudo systemctl enable vxrd.service
    cumulus@leaf2$ sudo systemctl restart vxrd.service

The complete list of options you can configure is listed below:

| Name                | Description                                                                                                                                                                                                          | Default            |
| ------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------ |
| loglevel            | The log level, which can be DEBUG, INFO, WARNING, ERROR, CRITICAL.                                                                                                                                                   | INFO               |
| logdest             | The destination for log messages. It can be a file name, `stdout` or `syslog`.                                                                                                                                       | syslog             |
| logfilesize         | Log file size in bytes. Used when `logdest` is a file name.                                                                                                                                                          | 512000             |
| logbackupcount      | Maximum number of log files stored on the disk. Used when `logdest` is a file name.                                                                                                                                  | 14                 |
| pidfile             | The PIF file location for the `vxrd` daemon.                                                                                                                                                                         | /var/run/vxrd.pid  |
| udsfile             | The file name for the Unix domain socket used for management.                                                                                                                                                        | /var/run/vxrd.sock |
| vxfld\_port         | The UDP port used for VXLAN control messages.                                                                                                                                                                        | 10001              |
| svcnode\_ip         | The address to which registration daemons send control messages for registration and/or BUM packets for replication. This can also be configured under `/etc/network/interfaces` with the `vxrd-svcnode-ip` keyword. |                    |
| holdtime            | Hold time (in seconds) for soft state, which is how long the service node waits before ageing out an IP address for a VNI. The `vxrd` includes this in the register messages it sends to a `vxsnd`.                  | 90 seconds         |
| src\_ip             | Local IP address to bind to for receiving control traffic from the service node daemon.                                                                                                                              |                    |
| refresh\_rate       | Number of times to refresh within the hold time. The higher this number, the more lost UDP refresh messages can be tolerated.                                                                                        | 3 seconds          |
| config\_check\_rate | The number of seconds to poll the system for current VXLAN membership.                                                                                                                                               | 5 seconds          |
| head\_rep           | Enables self replication. Instead of using the service node to replicate BUM packets, it will be done in hardware on the VTEP switch.                                                                                | true               |

{{%notice note%}}

Use *1*, *yes*, *true* or *on* for True for each relevant option. Use
*0*, *no*, *false* or *off* for False.

{{%/notice%}}

## <span>Configuring the Service Node</span>

To configure the service node daemon, edit the `/etc/vxsnd.conf`
configuration file.

{{%notice note%}}

For the example configuration, default values are used, except for the
`svcnode_ip` field.

{{%/notice%}}

    cumulus@spine1$ sudo nano /etc/vxsnd.conf

The address field is set to the loopback address of the switch running
the `vxsnd` dameon.

    svcnode_ip = 10.2.1.3

Enable, then restart the service node daemon for the change to take
effect:

    cumulus@spine1$ sudo systemctl enable vxsnd.service
    cumulus@spine1$ sudo systemctl restart vxsnd.service

The complete list of options you can configure is listed below:

| Name                  | Description                                                                                                                                                                                                             | Default            |
| --------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------ |
| loglevel              | The log level, which can be DEBUG, INFO, WARNING, ERROR, CRITICAL.                                                                                                                                                      | INFO               |
| logdest               | Destination for log messages. It can be a file name, `stdout` or `syslog`.                                                                                                                                              | syslog             |
| logfilesize           | The log file size in bytes. Used when `logdest` is a file name.                                                                                                                                                         | 512000             |
| logbackupcount        | Maximum number of log files stored on disk. Used when `logdest` is a file name.                                                                                                                                         | 14                 |
| pidfile               | The PID file location for the `vxrd` daemon.                                                                                                                                                                            | /var/run/vxrd.pid  |
| udsfile               | The file name for the Unix domain socket used for management.                                                                                                                                                           | /var/run/vxrd.sock |
| vxfld\_port           | The UDP port used for VXLAN control messages.                                                                                                                                                                           | 10001              |
| svcnode\_ip           | This is the address to which registration daemons send control messages for registration and/or BUM packets for replication.                                                                                            | 0.0.0.0            |
| holdtime              | Holdtime (in seconds) for soft state. It is used when sending a register message to peers in response to learning a \<vni, addr\> from a VXLAN data packet.                                                             | 90                 |
| src\_ip               | Local IP address to bind to for receiving inter-vxsnd control traffic.                                                                                                                                                  | 0.0.0.0            |
| svcnode\_peers        | Space-separated list of IP addresses with which the `vxsnd` shares its state.                                                                                                                                           |                    |
| enable\_vxlan\_listen | When set to true, the service node listens for VXLAN data traffic.                                                                                                                                                      | true               |
| install\_svcnode\_ip  | When set to true, the `snd_peer_address` gets installed on the loopback interface. It gets withdrawn when the `vxsnd` is not in service. If set to true, you must define the `snd_peer_address` configuration variable. | false              |
| age\_check            | Number of seconds to wait before checking the database to age out stale entries.                                                                                                                                        | 90 seconds         |

{{%notice note%}}

Use *1*, *yes*, *true* or *on* for True for each relevant option. Use
*0*, *no*, *false* or *off* for False.

{{%/notice%}}

## <span>Verification and Troubleshooting</span>

### <span>Verifying the Registration Node Daemon </span>

Use the `vxrdctl vxlans` ****command to see the configured VNIs, the
local address being used to source the VXLAN tunnel and the service node
being used.

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><pre><code>cumulus@leaf1$ vxrdctl vxlans
VNI     Local Addr       Svc Node
===     ==========       ========
 10      10.2.1.1        10.2.1.3
 30      10.2.1.1        10.2.1.3
2000      10.2.1.1        10.2.1.3</code></pre></td>
<td><pre><code>cumulus@leaf2$ vxrdctl vxlans
VNI     Local Addr       Svc Node
===     ==========       ========
 10      10.2.1.2        10.2.1.3
 30      10.2.1.2        10.2.1.3
2000      10.2.1.2        10.2.1.3</code></pre></td>
</tr>
</tbody>
</table>

Use the `vxrdctl peers` command to see configured VNIs and all VTEPs
(leaf switches) within the network that have them configured.

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><pre><code>cumulus@leaf1$ vxrdctl peers
VNI         Peer Addrs
===         ==========
10          10.2.1.1, 10.2.1.2
30          10.2.1.1, 10.2.1.2
2000        10.2.1.1, 10.2.1.2</code></pre></td>
<td><pre><code>cumulus@leaf2$ vxrdctl peers
VNI         Peer Addrs
===         ==========
10          10.2.1.1, 10.2.1.2
30          10.2.1.1, 10.2.1.2
2000        10.2.1.1, 10.2.1.2</code></pre></td>
</tr>
</tbody>
</table>

{{%notice note%}}

When head end replication mode is disabled, the command won't work.

Use the ` vxrdctl peers  `command to see the other VTEPs (leaf switches)
and what VNIs are associated with them. This does not show anything
unless you enabled head end replication mode by setting the `head_rep`
option to *True*. Otherwise, replication is done by the service node.

    cumulus@leaf2$ vxrdctl peers
    Head-end replication is turned off on this device.
    This command will not provide any output

{{%/notice%}}

### <span>Verifying the Service Node Daemon</span>

Use the `vxsndctl fdb` command to verify which VNIs belong to which VTEP
(leaf switches).

    cumulus@spine1$ vxsndctl fdb
    VNI    Address     Ageout
    ===    =======     ======
     10    10.2.1.1        82
     10    10.2.1.2        77
     30    10.2.1.1        82
     30    10.2.1.2        77
    2000    10.2.1.1        82
    2000    10.2.1.2        77

### <span>Verifying Traffic Flow and Checking Counters</span>

VXLAN transit traffic information is stored in a flat file located at
`/cumulus/switchd/run/stats/vxlan/all`.

    cumulus@leaf1$ cat /cumulus/switchd/run/stats/vxlan/all
    VNI                             : 10
    Network In Octets               : 1090
    Network In Packets              : 8
    Network Out Octets              : 1798
    Network Out Packets             : 13
    Total In Octets                 : 2818
    Total In Packets                : 27
    Total Out Octets                : 3144
    Total Out Packets               : 39
    VN Interface                    : vni: 10, swp32s0.10
    Total In Octets                 : 1728
    Total In Packets                : 19
    Total Out Octets                : 552
    Total Out Packets               : 18
    VNI                             : 30
    Network In Octets               : 828
    Network In Packets              : 6
    Network Out Octets              : 1224
    Network Out Packets             : 9
    Total In Octets                 : 2374
    Total In Packets                : 23
    Total Out Octets                : 2300
    Total Out Packets               : 32
    VN Interface                    : vni: 30, swp32s0.30
    Total In Octets                 : 1546
    Total In Packets                : 17
    Total Out Octets                : 552
    Total Out Packets               : 17
    VNI                             : 2000
    Network In Octets               : 676
    Network In Packets              : 5
    Network Out Octets              : 1072
    Network Out Packets             : 8
    Total In Octets                 : 2030
    Total In Packets                : 20
    Total Out Octets                : 2042
    Total Out Packets               : 30
    VN Interface                    : vni: 2000, swp32s0.20
    Total In Octets                 : 1354
    Total In Packets                : 15
    Total Out Octets                : 446

### <span>Pinging to Test Connectivity</span>

To test the connectivity across the VXLAN tunnel with an ICMP echo
request (ping), make sure to ping from the server rather than the switch
itself.

{{%notice note%}}

As mentioned above, SVIs (switch VLAN interfaces) are not supported when
using VXLAN. That is, there cannot be an IP address on the bridge that
also contains a VXLAN.

{{%/notice%}}

Following is the IP address information used in this example
configuration.

| VNI  | server1    | server2    |
| ---- | ---------- | ---------- |
| 10   | 10.10.10.1 | 10.10.10.2 |
| 2000 | 10.10.20.1 | 10.10.20.2 |
| 30   | 10.10.30.1 | 10.10.30.2 |

To test connectivity between VNI 10 connected servers by pinging from
server1:

    cumulus@server1:~$ ping 10.10.10.2
    PING 10.10.10.2 (10.10.10.2) 56(84) bytes of data.
    64 bytes from 10.10.10.2: icmp_seq=1 ttl=64 time=3.90 ms
    64 bytes from 10.10.10.2: icmp_seq=2 ttl=64 time=0.202 ms
    64 bytes from 10.10.10.2: icmp_seq=3 ttl=64 time=0.195 ms
    ^C
    --- 10.10.10.2 ping statistics ---
    3 packets transmitted, 3 received, 0% packet loss, time 2002ms
    rtt min/avg/max/mdev = 0.195/1.432/3.900/1.745 ms
    cumulus@server1:~$

The other VNIs were also tested and can be viewed in the expanded output
below.

Test connectivity between VNI-2000 connected servers by pinging from
server1:

    cumulus@server1:~$ ping 10.10.20.2
    PING 10.10.20.2 (10.10.20.2) 56(84) bytes of data.
    64 bytes from 10.10.20.2: icmp_seq=1 ttl=64 time=1.81 ms
    64 bytes from 10.10.20.2: icmp_seq=2 ttl=64 time=0.194 ms
    64 bytes from 10.10.20.2: icmp_seq=3 ttl=64 time=0.206 ms
    ^C
    --- 10.10.20.2 ping statistics ---
    3 packets transmitted, 3 received, 0% packet loss, time 2000ms
    rtt min/avg/max/mdev = 0.194/0.739/1.819/0.763 ms

Test connectivity between VNI-30 connected servers by pinging from
server1:

    cumulus@server1:~$ ping 10.10.30.2
    PING 10.10.30.2 (10.10.30.2) 56(84) bytes of data.
    64 bytes from 10.10.30.2: icmp_seq=1 ttl=64 time=1.85 ms
    64 bytes from 10.10.30.2: icmp_seq=2 ttl=64 time=0.239 ms
    64 bytes from 10.10.30.2: icmp_seq=3 ttl=64 time=0.185 ms
    64 bytes from 10.10.30.2: icmp_seq=4 ttl=64 time=0.212 ms
    ^C
    --- 10.10.30.2 ping statistics ---
    4 packets transmitted, 4 received, 0% packet loss, time 3000ms
    rtt min/avg/max/mdev = 0.185/0.622/1.853/0.711 ms

### <span>Troubleshooting with MAC Addresses</span>

Since there is no SVI, there is no way to ping from the server to the
directly attached leaf (top of rack) switch without cabling the switch
to itself (see [Creating a Layer 3
Gateway](#src-5122049_LightweightNetworkVirtualization-LNV-l3gateway)
below). The easiest way to see if the server can reach the leaf switch
is to check the MAC address table of the leaf switch.

First, get the MAC address of the server:

    cumulus@server1:~$ ip addr show eth3.10 | grep ether
        link/ether 90:e2:ba:55:f0:85 brd ff:ff:ff:ff:ff:ff

Next, check the MAC address table of the leaf switch:

    cumulus@leaf1$ brctl showmacs br-10
    port name mac addr      vlan    is local?   ageing timer
    vni-10    46:c6:57:fc:1f:54 0   yes        0.00
    swp32s0.10 90:e2:ba:55:f0:85    0   no        75.87
    vni-10    90:e2:ba:7e:a9:c1 0   no        75.87
    swp32s0.10 ec:f4:bb:fc:67:a1    0   yes        0.00

*90:e2:ba:55:f0:85* appears in the MAC address table, which indicates
that connectivity is occurring between leaf1 and server1.

### <span>Checking the Service Node Configuration</span>

Use `ip -d link show` to verify the service node, VNI and administrative
state of a particular logical VNI interface:

    cumulus@leaf1$ ip -d link show vni-10
    35: vni-10: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue master br-10 state UNKNOWN mode DEFAULT
        link/ether 46:c6:57:fc:1f:54 brd ff:ff:ff:ff:ff:ff
        vxlan id 10 remote 10.2.1.3 local 10.2.1.1 srcport 32768 61000 dstport 4789 ageing 300 svcnode 10.2.1.3
        bridge_slave

## <span id="src-5122049_LightweightNetworkVirtualization-LNV-l3gateway" class="confluence-anchor-link"></span><span>Creating a Layer 3 Gateway</span>

The Trident II ASIC has a limitation because of a restriction in the
hardware, where an IP address cannot be configured on the same bridge of
which a VXLAN is also a part. This limitation will not exist in future
ASICs. For example, the Trident II+ has the [RIOT (Routing In/Out of
Tunnels)](https://www.broadcom.com/press/release.php?id=s907324)
feature.

For the Trident II, this limitation means a physical cable must be
attached from one port on leaf1 to another port on leaf1. One port is an
L3 port while the other is a member of the bridge. For example,
following the configuration above, in order for a layer 3 address to be
used as the gateway for vni-10, you could configure the following on
leaf1:

    auto swp47
    iface swp47
    alias l2 port connected to swp48
     
    auto swp48
    iface swp48
    alias gateway
    address 10.10.10.3/24
     
    auto vni-10
    iface vni-10
      vxlan-id 10    
      vxlan-local-tunnelip 10.2.1.1
      mstpctl-bpduguard yes
      mstpctl-portbpdufilter yes
     
    auto br-10
    iface br-10
      bridge-ports swp47 swp32s0.10 vni-10

A loopback cable must be connected between swp47 and swp48 for this to
work. This will be addressed in a future version of Cumulus Linux so a
physical port does not need to be used for this purpose.

## <span id="src-5122049_LightweightNetworkVirtualization-LNV-loadbalancing" class="confluence-anchor-link"></span><span>Advanced LNV Usage</span>

### <span>Scaling LNV by Load Balancing with Anycast</span>

The above configuration assumes a single service node. A single service
node can quickly be overwhelmed by BUM traffic. To load balance BUM
traffic across multiple service nodes, use
[Anycast](http://en.wikipedia.org/wiki/Anycast). Anycast enables BUM
traffic to reach the topologically nearest service node rather than
overwhelming a single service node.

#### <span></span>

#### <span>Enabling the Service Node Daemon on Additional Spine Switches</span>

In this example, spine1 already has the service node daemon enabled.
Enable it on the spine2 switch, then reboot the `vxsnd` daemon:

    cumulus@spine2$ sudo systemctl enable vxsnd.service
    cumulus@spine2$ sudo systemctl restart vxsnd.service

#### <span>Configuring the AnyCast Address on All Participating Service Nodes</span>

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p><strong>spine1</strong></p>
<p>Use a text editor to edit the network configuration:</p>
<pre><code>cumulus@spine1$ sudo nano /etc/network/interfaces</code></pre>
<p>Add the 10.10.10.10/32 address to the loopback address:</p>
<pre><code>auto lo
iface lo inet loopback
  address 10.2.1.3/32
  address 10.10.10.10/32</code></pre>
<p>Run <code>ifreload -a</code>:</p>
<pre><code>cumulus@spine1$ sudo ifreload -a</code></pre>
<p>Verify the IP address is configured:</p>
<pre><code>cumulus@spine1$ ip addr show lo
1: lo: &lt;LOOPBACK,UP,LOWER_UP&gt; mtu 16436 qdisc noqueue state UNKNOWN
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
    inet 10.2.1.3/32 scope global lo
    inet 10.10.10.10/32 scope global lo
    inet6 ::1/128 scope host
       valid_lft forever preferred_lft forever</code></pre></td>
<td><p><strong>spine2</strong></p>
<p>Use a text editor to edit the network configuration:</p>
<pre><code>cumulus@spine2$ sudo nano /etc/network/interfaces</code></pre>
<p>Add the 10.10.10.10/32 address to the loopback address:</p>
<pre><code>auto lo
iface lo inet loopback
  address 10.2.1.4/32
  address 10.10.10.10/32</code></pre>
<p>Run <code>ifreload -a</code>:</p>
<pre><code>cumulus@spine2$ sudo ifreload -a</code></pre>
<p>Verify the IP address is configured:</p>
<pre><code>cumulus@spine2$ ip addr show lo
1: lo: &lt;LOOPBACK,UP,LOWER_UP&gt; mtu 16436 qdisc noqueue state UNKNOWN
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
    inet 10.2.1.4/32 scope global lo
    inet 10.10.10.10/32 scope global lo
    inet6 ::1/128 scope host
       valid_lft forever preferred_lft forever</code></pre></td>
</tr>
</tbody>
</table>

#### <span>Configuring the Service Node vxsnd.conf File</span>

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p><strong>spine1</strong></p>
<p>Use a text editor to edit the network configuration:</p>
<pre><code>cumulus@spine1$ sudo nano /etc/vxsnd.conf</code></pre>
<p>Change the following values:</p>
<pre><code>svcnode_ip = 10.10.10.10
 
svcnode_peers = 10.2.1.4
 
src_ip = 10.2.1.3</code></pre>
<p>{{%notice info%}}</p>
<p>This sets the address on which the service node listens to VXLAN messages to the configured Anycast address and sets it to sync with spine2.</p>
<p>{{%/notice%}}</p>
<p>Enable, then restart the <code>vxsnd</code> daemon:</p>
<pre><code>cumulus@spine1$ sudo systemctl enable vxsnd.service
cumulus@spine1$ sudo systemctl restart vxsnd.service</code></pre></td>
<td><p><strong>spine2</strong></p>
<p>Use a text editor to edit the network configuration:</p>
<pre><code>cumulus@spine2$ sudo nano /etc/vxsnd.conf</code></pre>
<p>Change the following values:</p>
<pre><code>svcnode_ip = 10.10.10.10
 
svcnode_peers = 10.2.1.3
 
src_ip = 10.2.1.4</code></pre>
<p>{{%notice info%}}</p>
<p>This sets the address on which the service node listens to VXLAN messages to the configured Anycast address and sets it to sync with spine1.</p>
<p>{{%/notice%}}</p>
<p>Enable, then restart the <code>vxsnd</code> daemon:</p>
<pre><code>cumulus@spine1$ sudo systemctl enable vxsnd.service
cumulus@spine1$ sudo systemctl restart vxsnd.service</code></pre></td>
</tr>
</tbody>
</table>

#### <span>Reconfiguring the VTEPs (Leafs) to Use the Anycast Address</span>

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p><strong>leaf1</strong></p>
<p>Use a text editor to edit the network configuration:</p>
<pre><code>cumulus@leaf1$ sudo nano /etc/network/interfaces</code></pre>
<p>Change the <code>vxrd-svcnode-ip</code> field to the Anycast address:</p>
<pre><code>auto lo
iface lo inet loopback
  address 10.2.1.1
  vxrd-svcnode-ip 10.10.10.10</code></pre>
<p>Run <code>ifreload -a</code>:</p>
<pre><code>cumulus@leaf1$ sudo ifreload -a</code></pre>
<p>Verify the new service node is configured:</p>
<pre><code>cumulus@leaf1$ ip -d link show vni-10
35: vni-10: &lt;BROADCAST,MULTICAST,UP,LOWER_UP&gt; mtu 1500 qdisc noqueue master br-10 state UNKNOWN mode DEFAULT
    link/ether 46:c6:57:fc:1f:54 brd ff:ff:ff:ff:ff:ff
    vxlan id 10 remote 10.10.10.10 local 10.2.1.1 srcport 32768 61000 dstport 4789 ageing 300 svcnode 10.10.10.10
    bridge_slave
 
 
cumulus@leaf1$ ip -d link show vni-2000
39: vni-2000: &lt;BROADCAST,MULTICAST,UP,LOWER_UP&gt; mtu 1500 qdisc noqueue master br-20 state UNKNOWN mode DEFAULT
    link/ether 4a:fd:88:c3:fa:df brd ff:ff:ff:ff:ff:ff
    vxlan id 2000 remote 10.10.10.10 local 10.2.1.1 srcport 32768 61000 dstport 4789 ageing 300 svcnode 10.10.10.10
    bridge_slave
 
cumulus@leaf1$ ip -d link show vni-30
37: vni-30: &lt;BROADCAST,MULTICAST,UP,LOWER_UP&gt; mtu 1500 qdisc noqueue master br-30 state UNKNOWN mode DEFAULT
    link/ether 3e:b3:dc:f3:bd:2b brd ff:ff:ff:ff:ff:ff
    vxlan id 30 remote 10.10.10.10 local 10.2.1.1 srcport 32768 61000 dstport 4789 ageing 300 svcnode 10.10.10.10
    bridge_slave</code></pre>
<p>{{%notice note%}}</p>
<p>The <code>svcnode</code> 10.10.10.10 means the interface has the correct service node configured.</p>
<p>{{%/notice%}}</p>
<p>Use the <code>vxrdctl vxlans</code> command to check the service node:</p>
<pre><code>cumulus@leaf1$ vxrdctl vxlans
VNI     Local Addr       Svc Node
===     ==========       ========
 10      10.2.1.1        10.2.1.3
 30      10.2.1.1        10.2.1.3
2000      10.2.1.1        10.2.1.3</code></pre></td>
<td><p><strong>leaf2</strong></p>
<p>Use a text editor to edit the network configuration:</p>
<pre><code>cumulus@leaf2$ sudo nano /etc/network/interfaces</code></pre>
<p>Change the <code>vxrd-svcnode-ip</code> field to the Anycast address:</p>
<pre><code>auto lo
iface lo inet loopback
  address 10.2.1.2
  vxrd-svcnode-ip 10.10.10.10</code></pre>
<p>Run <code>ifreload -a</code>:</p>
<pre><code>cumulus@leaf2$ sudo ifreload -a</code></pre>
<p>Verify the new service node is configured:</p>
<pre><code>cumulus@leaf2$ ip -d link show vni-10
35: vni-10: &lt;BROADCAST,MULTICAST,UP,LOWER_UP&gt; mtu 1500 qdisc noqueue master br-10 state UNKNOWN mode DEFAULT
    link/ether 4e:03:a7:47:a7:9d brd ff:ff:ff:ff:ff:ff
    vxlan id 10 remote 10.10.10.10 local 10.2.1.2 srcport 32768 61000 dstport 4789 ageing 300 svcnode 10.10.10.10
    bridge_slave
 
cumulus@leaf2$ ip -d link show vni-2000
39: vni-2000: &lt;BROADCAST,MULTICAST,UP,LOWER_UP&gt; mtu 1500 qdisc noqueue master br-20 state UNKNOWN mode DEFAULT
    link/ether 72:3a:bd:06:00:b7 brd ff:ff:ff:ff:ff:ff
    vxlan id 2000 remote 10.10.10.10 local 10.2.1.2 srcport 32768 61000 dstport 4789 ageing 300 svcnode 10.10.10.10
    bridge_slave
 
 
cumulus@leaf2$ ip -d link show vni-30
37: vni-30: &lt;BROADCAST,MULTICAST,UP,LOWER_UP&gt; mtu 1500 qdisc noqueue master br-30 state UNKNOWN mode DEFAULT
    link/ether 22:65:3f:63:08:bd brd ff:ff:ff:ff:ff:ff
    vxlan id 30 remote 10.10.10.10 local 10.2.1.2 srcport 32768 61000 dstport 4789 ageing 300 svcnode 10.10.10.10
    bridge_slave</code></pre>
<p>{{%notice note%}}</p>
<p>The <code>svcnode</code> 10.10.10.10 means the interface has the correct service node configured.</p>
<p>{{%/notice%}}</p>
<p>Use the <code>vxrdctl vxlans</code> command to check the service node:</p>
<pre><code>cumulus@leaf2$ vxrdctl vxlans
VNI     Local Addr       Svc Node
===     ==========       ========
 10      10.2.1.2        10.2.1.3
 30      10.2.1.2        10.2.1.3
2000      10.2.1.2        10.2.1.3</code></pre></td>
</tr>
</tbody>
</table>

#### <span>Testing Connectivity</span>

Repeat the ping tests from the previous section. Here is the table again
for reference:

| VNI  | server1    | server2    |
| ---- | ---------- | ---------- |
| 10   | 10.10.10.1 | 10.10.10.2 |
| 2000 | 10.10.20.1 | 10.10.20.2 |
| 30   | 10.10.30.1 | 10.10.30.2 |

    cumulus@server1:~$ ping 10.10.10.2
    PING 10.10.10.2 (10.10.10.2) 56(84) bytes of data.
    64 bytes from 10.10.10.2: icmp_seq=1 ttl=64 time=5.32 ms
    64 bytes from 10.10.10.2: icmp_seq=2 ttl=64 time=0.206 ms
    ^C
    --- 10.10.10.2 ping statistics ---
    2 packets transmitted, 2 received, 0% packet loss, time 1001ms
    rtt min/avg/max/mdev = 0.206/2.767/5.329/2.562 ms
     
    PING 10.10.20.2 (10.10.20.2) 56(84) bytes of data.
    64 bytes from 10.10.20.2: icmp_seq=1 ttl=64 time=1.64 ms
    64 bytes from 10.10.20.2: icmp_seq=2 ttl=64 time=0.187 ms
    ^C
    --- 10.10.20.2 ping statistics ---
    2 packets transmitted, 2 received, 0% packet loss, time 1001ms
    rtt min/avg/max/mdev = 0.187/0.914/1.642/0.728 ms
     
    cumulus@server1:~$ ping 10.10.30.2
    PING 10.10.30.2 (10.10.30.2) 56(84) bytes of data.
    64 bytes from 10.10.30.2: icmp_seq=1 ttl=64 time=1.63 ms
    64 bytes from 10.10.30.2: icmp_seq=2 ttl=64 time=0.191 ms
    ^C
    --- 10.10.30.2 ping statistics ---
    2 packets transmitted, 2 received, 0% packet loss, time 1001ms
    rtt min/avg/max/mdev = 0.191/0.913/1.635/0.722 ms

### <span>Restarting Network Removes vxsnd Anycast IP Address from Loopback Interface</span>

If you have not configured a loopback anycast IP address in
/etc/network/interfaces, but you have enabled the `vxsnd` (service node
daemon) log to automatically add anycast IP addresses, when you restart
networking (with `systemctl restart networking`), the anycast IP address
gets removed from the loopback interface.

To prevent this issue from occurring, you should specify an anycast IP
address for the loopback interface in both `/etc/network/interfaces` and
`vxsnd.conf`. This way, in case `vxsnd` fails, you can withdraw the IP
address.

## <span>Additional Resources</span>

Both `vxsnd` and `vxrd` have man pages in Cumulus Linux.

For `vxsnd`:

    cumulus@spine1$ man vxsnd

For `vxrd`:

    cumulus@leaf1$ man vxrd

## <span>See Also</span>

  - [tools.ietf.org/html/rfc7348](https://tools.ietf.org/html/rfc7348)

  - [en.wikipedia.org/wiki/Anycast](http://en.wikipedia.org/wiki/Anycast)
