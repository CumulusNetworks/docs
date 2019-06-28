---
title: Static VXLAN Tunnels
author: Cumulus Networks
weight: 141
aliases:
 - /display/CL321/Static+VXLAN+Tunnels
 - /pages/viewpage.action?pageId=5126991
pageID: 5126991
product: Cumulus Linux
version: 3.2.1
imgData: cumulus-linux-321
siteSlug: cumulus-linux-321
---
In VXLAN-based networks, there are a range of complexities and
challenges in determining the destination *virtual tunnel endpoints*
(VTEPs) for any given VXLAN. At scale, various solutions, including
[Lightweight Network
Virtualization](/version/cumulus-linux-321/Network_Virtualization/Lightweight_Network_Virtualization_-_LNV_Overview/)
(LNV), controller-based options like [Midokura
MidoNet](/version/cumulus-linux-321/Network_Virtualization/Integrating_Hardware_VTEPs_with_Midokura_MidoNet_and_OpenStack)
or [VMware
NSX](/version/cumulus-linux-321/Network_Virtualization/Integrating_with_VMware_NSX)
and even new standards like
[EVPN](/version/cumulus-linux-321/Network_Virtualization/Ethernet_Virtual_Private_Network_-_EVPN)
are attempts to address these complexities, however do retain their own
complexities.

Enter *static VXLAN tunnels*, which simply serve to connect two VTEPs in
a given environment. Static VXLAN tunnels are the simplest deployment
mechanism for small scale environments, and they should be interoperable
with other vendors that adhere to VXLAN standards. It's an easy
configuration, since you are simply mapping which VTEPs are in a
particular VNI, so you can avoid the tedious process of defining
connections to every VLAN on every other VTEP on every other rack.

## <span>Requirements</span>

While they should be interoperable with other vendors, Cumulus Networks
supports static VXLAN tunnels only on switches in the [Cumulus Linux
HCL](http://cumulusnetworks.com/hcl/) using the Broadcom Tomahawk,
Trident II+ and Trident II chipsets as well as the Mellanox Spectrum
chipset.

For a basic VXLAN configuration, you should ensure that:

  - The VXLAN has a network identifier (VNI); do not use 0 or 16777215
    as the VNI ID, as they are reserved values under Cumulus Linux.

  - The VXLAN link and local interfaces are added to bridge to create
    the association between port, VLAN and VXLAN instance.

  - Each bridge on the switch has only one VXLAN interface. Cumulus
    Linux does not support more than one VXLAN link in a bridge.

  - The VXLAN registration daemon (`vxrd`) is not running. Static VXLAN
    tunnels do not interoperate with LNV or EVPN. If vxrd is running,
    stop it with:
    
        cumulus@switch:~ sudo systemctl stop vxrd.service

## <span>Example Configuration</span>

The following topology is used in this chapter. Each IP address
corresponds to the switch's loopback address:

{{% imgOld 0 %}}

## <span>Configuring Static VXLAN Tunnels</span>

To configure static VXLAN tunnels, for each leaf you need to do the
following:

  - Specify an IP address for the loopback

  - Create a VXLAN interface, using the loopback address for the local
    tunnel IP address

  - Create the tunnels by configuring the remote IP address to each
    other leaf switch's loopback address

To configure leaf01, run the following commands:

    cumulus@leaf01:~$ net add loopback lo ip address 10.0.0.11/32
    cumulus@leaf01:~$ net add vxlan vni-10 vxlan id 10
    cumulus@leaf01:~$ net add vxlan vni-10 vxlan local-tunnelip 10.0.0.11
    cumulus@leaf01:~$ net add vxlan vni-10 vxlan remoteip 10.0.0.12
    cumulus@leaf01:~$ net add vxlan vni-10 vxlan remoteip 10.0.0.13
    cumulus@leaf01:~$ net add vxlan vni-10 vxlan remoteip 10.0.0.14
    cumulus@leaf01:~$ net add vxlan vni-10 bridge access 10
    cumulus@leaf01:~$ net pending
    cumulus@leaf01:~$ net commit

These commands create the following configuration in the
/etc/network/interfaces file:

    # The loopback network interface
    auto lo
    iface lo inet loopback
        address 10.0.0.11/32
     
    # The primary network interface
    auto eth0
    iface eth0 inet dhcp
     
    auto swp1
    iface swp1
     
    auto swp2
    iface swp2
     
    auto bridge
    iface bridge
        bridge-ports vni-10
        bridge-vids 10
        bridge-vlan-aware yes
     
    auto vni-10
    iface vni-10
        bridge-access 10
        mstpctl-bpduguard yes
        mstpctl-portbpdufilter yes
        vxlan-id 10
        vxlan-local-tunnelip 10.0.0.11
        vxlan-remoteip 10.0.0.12
        vxlan-remoteip 10.0.0.13
        vxlan-remoteip 10.0.0.14

Repeat these steps for leaf02, leaf03 and leaf04:

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Node</p></th>
<th><p>NCLU Commands</p></th>
<th><p>/etc/network/interfaces Configuration</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>leaf02</p></td>
<td><pre><code>cumulus@leaf02:~$ net add loopback lo ip address 10.0.0.12/32
cumulus@leaf02:~$ net add vxlan vni-10 vxlan id 10
cumulus@leaf02:~$ net add vxlan vni-10 vxlan local-tunnelip 10.0.0.12
cumulus@leaf02:~$ net add vxlan vni-10 vxlan remoteip 10.0.0.11
cumulus@leaf02:~$ net add vxlan vni-10 vxlan remoteip 10.0.0.13
cumulus@leaf02:~$ net add vxlan vni-10 vxlan remoteip 10.0.0.14
cumulus@leaf02:~$ net add vxlan vni-10 bridge access 10
cumulus@leaf02:~$ net pending
cumulus@leaf02:~$ net commit</code></pre></td>
<td><pre><code># The loopback network interface
auto lo
iface lo inet loopback
    address 10.0.0.12/32
 
# The primary network interface
auto eth0
iface eth0 inet dhcp
 
auto swp1
iface swp1
 
auto swp2
iface swp2
 
auto bridge
iface bridge
    bridge-ports vni-10
    bridge-vids 10
    bridge-vlan-aware yes
 
auto vni-10
iface vni-10
    bridge-access 10
    mstpctl-bpduguard yes
    mstpctl-portbpdufilter yes
    vxlan-id 10
    vxlan-local-tunnelip 10.0.0.12
    vxlan-remoteip 10.0.0.11
    vxlan-remoteip 10.0.0.13
    vxlan-remoteip 10.0.0.14</code></pre></td>
</tr>
<tr class="even">
<td><p>leaf03</p></td>
<td><pre><code>cumulus@leaf03:~$ net add loopback lo ip address 10.0.0.13/32
cumulus@leaf03:~$ net add vxlan vni-10 vxlan id 10
cumulus@leaf03:~$ net add vxlan vni-10 vxlan local-tunnelip 10.0.0.13
cumulus@leaf03:~$ net add vxlan vni-10 vxlan remoteip 10.0.0.11
cumulus@leaf03:~$ net add vxlan vni-10 vxlan remoteip 10.0.0.12
cumulus@leaf03:~$ net add vxlan vni-10 vxlan remoteip 10.0.0.14
cumulus@leaf03:~$ net add vxlan vni-10 bridge access 10
cumulus@leaf03:~$ net pending
cumulus@leaf03:~$ net commit</code></pre></td>
<td><pre><code># The loopback network interface
auto lo
iface lo inet loopback
    address 10.0.0.13/32
 
# The primary network interface
auto eth0
iface eth0 inet dhcp
 
auto swp1
iface swp1
 
auto swp2
iface swp2
 
auto bridge
iface bridge
    bridge-ports vni-10
    bridge-vids 10
    bridge-vlan-aware yes
 
auto vni-10
iface vni-10
    bridge-access 10
    mstpctl-bpduguard yes
    mstpctl-portbpdufilter yes
    vxlan-id 10
    vxlan-local-tunnelip 10.0.0.13
    vxlan-remoteip 10.0.0.11
    vxlan-remoteip 10.0.0.12
    vxlan-remoteip 10.0.0.14</code></pre></td>
</tr>
<tr class="odd">
<td><p>leaf04</p></td>
<td><pre><code>cumulus@leaf04:~$ net add loopback lo ip address 10.0.0.14/32
cumulus@leaf04:~$ net add vxlan vni-10 vxlan id 10
cumulus@leaf04:~$ net add vxlan vni-10 vxlan local-tunnelip 10.0.0.14
cumulus@leaf04:~$ net add vxlan vni-10 vxlan remoteip 10.0.0.11
cumulus@leaf04:~$ net add vxlan vni-10 vxlan remoteip 10.0.0.12
cumulus@leaf04:~$ net add vxlan vni-10 vxlan remoteip 10.0.0.13
cumulus@leaf04:~$ net add vxlan vni-10 bridge access 10
cumulus@leaf04:~$ net pending
cumulus@leaf04:~$ net commit</code></pre></td>
<td><pre><code># The loopback network interface
auto lo
iface lo inet loopback
    address 10.0.0.14/32
 
# The primary network interface
auto eth0
iface eth0 inet dhcp
 
auto swp1
iface swp1
 
auto swp2
iface swp2
 
auto bridge
iface bridge
    bridge-ports vni-10
    bridge-vids 10
    bridge-vlan-aware yes
 
auto vni-10
iface vni-10
    bridge-access 10
    mstpctl-bpduguard yes
    mstpctl-portbpdufilter yes
    vxlan-id 10
    vxlan-local-tunnelip 10.0.0.14
    vxlan-remoteip 10.0.0.11
    vxlan-remoteip 10.0.0.12
    vxlan-remoteip 10.0.0.13</code></pre></td>
</tr>
</tbody>
</table>

## <span>Verifying the Configuration</span>

Once you configure all the leaf switches, check for replication entries:

    cumulus@leaf01:~$ sudo bridge fdb show | grep 00:00:00:00:00:00
    00:00:00:00:00:00 dev vni-10 dst 10.0.0.14 self permanent
    00:00:00:00:00:00 dev vni-10 dst 10.0.0.12 self permanent
    00:00:00:00:00:00 dev vni-10 dst 10.0.0.13 self permanent
