---
title: Ethernet Virtual Private Network - EVPN
author: Cumulus Networks
weight: 293
aliases:
 - /display/CL31/Ethernet+Virtual+Private+Network+-+EVPN
 - /pages/viewpage.action?pageId=5122076
pageID: 5122076
product: Cumulus Linux
version: 3.1.2
imgData: cumulus-linux-312
siteSlug: cumulus-linux-312
---
{{%notice warning%}}

**Early Access Feature**

EVPN is an [early access
feature](https://support.cumulusnetworks.com/hc/en-us/articles/202933878)
in Cumulus Linux 3.1.1. Before you can install EVPN, you must enable the
Early Access repository. For more information about the Cumulus Linux
repository, read [this knowledge base
article](https://support.cumulusnetworks.com/hc/en-us/articles/217422127).

{{%/notice%}}

Ethernet Virtual Private Network (EVPN) is an early access feature in
Cumulus Linux 3.1.x. EVPN acts as a control plane for
[VXLAN](/version/cumulus-linux-312/Layer_1_and_Layer_2_Features/Network_Virtualization/)
in Cumulus Linux, rather than acting as a generic layer 2 VPN solution.
The early access release implements VNI membership exchange on VTEPs
using the EVPN type-3, or Inclusive Multicast Ethernet Tag (IMET),
route. The available functionality includes the following
characteristics:

  - Auto-derivation of
    [BGP](/version/cumulus-linux-312/Layer_3_Features/Border_Gateway_Protocol_-_BGP)
    route distinguishers (RD) and route targets (RT) for the EVPN route,
    while allowing for manual configuration/override.

  - Either eBGP or iBGP may be used to exchange EVPN routes; peering
    sessions can be either numbered or unnumbered.

  - Either eBGP or OSPF can be used as the underlay routing protocol.

  - VXLANs can be configured using either VLAN-aware bridge mode, or
    per-VXLAN-bridge mode.

  - MAC learning over the VXLAN tunnels still occurs in the data plane.

  - Head end replication is used for handling BUM traffic.

## <span>Installing the EVPN Package</span>

To install EVPN on a switch:

1.  Open the `/etc/apt/sources.list` file in a text editor.

2.  Uncomment the early access repo lines and save the file:
    
        #deb        http://repo3.cumulusnetworks.com/repo CumulusLinux-3-early-access cumulus
        #deb-src    http://repo3.cumulusnetworks.com/repo CumulusLinuz-3-early-access cumulus

3.  Run the following commands to install the EVPN package in Cumulus
    Linux:
    
        cumulus@switch:~$ apt-get update
        cumulus@switch:~$ apt-get install cumulus-evpn
        cumulus@switch:~$ apt-get upgrade

4.  Check your Quagga version using the `dpkg -l quagga` command. Please
    make sure you are running `0.99.24+cl3eau5` or newer
    
        cumulus@leaf01:~$ dpkg -l quagga
        Desired=Unknown/Install/Remove/Purge/Hold
        | Status=Not/Inst/Conf-files/Unpacked/halF-conf/Half-inst/trig-aWait/Trig-pend
        |/ Err?=(none)/Reinst-required (Status,Err: uppercase=bad)
        ||/ Name                     Version           Architecture      Description
        +++-========================-=================-=================-=====================================================
        ii  quagga                   0.99.24+cl3eau5   amd64             BGP/OSPF/RIP routing daemon

## <span>Enabling Quagga</span>

Quagga needs to be enabled prior to using EVPN.

1.  Open `/etc/quagga/daemons` file in a text editor:
    
        cumulus@switch:~$ sudo nano /etc/quagga/daemons

2.  Change the *no* to *yes* for `zebra` and `bgpd`, then save the file:
    
        zebra=yes
        bgpd=yes

3.  Enable and start Quagga using the `systemctl` commands:
    
        cumulus@switch:~$ sudo systemctl enable quagga.service
        cumulus@switch:~$ sudo systemctl start quagga.service

## <span>Example Configuration</span>

The following configurations are used throughout this chapter. You can
find the flat-file configurations for the network devices in the Cumulus
Networks [GitHub
repository](https://github.com/CumulusNetworks/cldemo-evpn/tree/master/config).
Only a subset is shown here for brevity (not shown are configurations
for leaf03, leaf04, server03, server04). Here is the topology diagram:

{{% imgOld 0 %}}

### <span>leaf01 and leaf02 Configurations</span>

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="odd">
<td>leaf01 /etc/network/interfaces
<pre><code>auto lo
iface lo inet loopback
    address 10.0.0.11/32
 
auto eth0
iface eth0 inet dhcp
 
# uplinks
auto swp51
iface swp51
 
auto swp52
iface swp52
 
auto br0
iface br0
    bridge-ports swp1 vxlan10001 vxlan10100 vxlan10200
    bridge-vlan-aware yes
    bridge-vids 1 100 200
    bridge-pvid 1
 
auto vxlan10001
iface vxlan10001
    vxlan-id 10001
    vxlan-local-tunnelip 10.0.0.11
    bridge-access 1
 
auto vxlan10100
iface vxlan10100
     vxlan-id 10100
     vxlan-local-tunnelip 10.0.0.11
     bridge-access 100
 
auto vxlan10200
iface vxlan10200
     vxlan-id 10200
     vxlan-local-tunnelip 10.0.0.11
     bridge-access 200</code></pre></td>
<td>leaf02 /etc/network/interfaces
<pre><code>auto lo
iface lo inet loopback
    address 10.0.0.12/32
auto eth0
iface eth0 inet dhcp
 
# uplinks
auto swp51
iface swp51
 
auto swp52
iface swp52
 
auto br0
iface br0
    bridge-ports swp2 vxlan10001 vxlan10100 vxlan10200
    bridge-vlan-aware yes
    bridge-vids 1 100 200
    bridge-pvid 1
 
auto vxlan10001
iface vxlan10001
    vxlan-id 10001
    vxlan-local-tunnelip 10.0.0.12
    bridge-access 1
 
auto vxlan10100
iface vxlan10100
     vxlan-id 10100
     vxlan-local-tunnelip 10.0.0.12
     bridge-access 100
 
auto vxlan10200
iface vxlan10200
     vxlan-id 10200
     vxlan-local-tunnelip 10.0.0.12
     bridge-access 200</code></pre></td>
</tr>
<tr class="even">
<td>leaf01 /etc/quagga/Quagga.conf
<pre><code>!
interface swp51
 ipv6 nd ra-interval 10
 no ipv6 nd suppress-ra
!
interface swp52
 ipv6 nd ra-interval 10
 no ipv6 nd suppress-ra
!
router bgp 65011
 bgp router-id 10.0.0.11
 bgp bestpath as-path multipath-relax
 neighbor fabric peer-group
 neighbor fabric remote-as external
 neighbor fabric description Internal Fabric Network
 neighbor fabric capability extended-nexthop
 neighbor swp51 interface peer-group fabric
 neighbor swp52 interface peer-group fabric
 !
 address-family ipv4 unicast
  network 10.0.0.11/32
  neighbor fabric prefix-list dc-leaf-in in
  neighbor fabric prefix-list dc-leaf-out out
 exit-address-family
 !
!
 address-family ipv6 unicast
  neighbor fabric activate
 exit-address-family
 !
 address-family evpn
  neighbor fabric activate
  advertise-vni
 exit-address-family
 exit
!
ip prefix-list dc-leaf-in seq 10 permit 0.0.0.0/0
ip prefix-list dc-leaf-in seq 20 permit 10.0.0.0/24 le 32
ip prefix-list dc-leaf-in seq 500 deny any
ip prefix-list dc-leaf-out seq 20 permit 10.0.0.0/24 le 32
ip prefix-list dc-leaf-out seq 500 deny any
!
line vty
!
end</code></pre></td>
<td>leaf02 /etc/quagga/Quagga.conf
<pre><code>!
interface swp51
 ipv6 nd ra-interval 10
 no ipv6 nd suppress-ra
!
interface swp52
 ipv6 nd ra-interval 10
 no ipv6 nd suppress-ra
!
router bgp 65012
 bgp router-id 10.0.0.12
 bgp bestpath as-path multipath-relax
 neighbor fabric peer-group
 neighbor fabric remote-as external
 neighbor fabric description Internal Fabric Network
 neighbor fabric capability extended-nexthop
 neighbor swp51 interface peer-group fabric
 neighbor swp52 interface peer-group fabric
 !
 address-family ipv4 unicast
  network 10.0.0.12/32
  neighbor fabric prefix-list dc-leaf-in in
  neighbor fabric prefix-list dc-leaf-out out
 exit-address-family
 !
!
 address-family ipv6 unicast
  neighbor fabric activate
 exit-address-family
 !
 address-family evpn
  neighbor fabric activate
  advertise-vni
 exit-address-family
 exit
!
ip prefix-list dc-leaf-in seq 10 permit 0.0.0.0/0
ip prefix-list dc-leaf-in seq 20 permit 10.0.0.0/24 le 32
ip prefix-list dc-leaf-in seq 500 deny any
ip prefix-list dc-leaf-out seq 20 permit 10.0.0.0/24 le 32
ip prefix-list dc-leaf-out seq 500 deny any
!
line vty
!
end</code></pre></td>
</tr>
</tbody>
</table>

### <span>spine01 and spine02 Configurations</span>

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="odd">
<td>spine01 /etc/network/interfaces
<pre><code>auto lo
iface lo inet loopback
    address 10.0.0.21/32
 
auto eth0
iface eth0 inet dhcp
 
# downlinks
auto swp1
iface swp1
 
auto swp2
iface swp2
 
auto swp3
iface swp3
 
auto swp4
iface swp4</code></pre></td>
<td>spine02 /etc/network/interfaces
<pre><code>auto lo
iface lo inet loopback
    address 10.0.0.22/32
 
auto eth0
iface eth0 inet dhcp
 
# downlinks
auto swp1
iface swp1
 
auto swp2
iface swp2
 
auto swp3
iface swp3
 
auto swp4
iface swp4</code></pre></td>
</tr>
<tr class="even">
<td>spine01 /etc/quagga/Quagga.conf
<pre><code>!
interface swp1
 ipv6 nd ra-interval 10
 no ipv6 nd suppress-ra
!
interface swp2
 ipv6 nd ra-interval 10
 no ipv6 nd suppress-ra
!
interface swp3
 ipv6 nd ra-interval 10
 no ipv6 nd suppress-ra
!
interface swp4
 ipv6 nd ra-interval 10
 no ipv6 nd suppress-ra
!
router bgp 65020
 bgp router-id 10.0.0.21
 bgp bestpath as-path multipath-relax
 neighbor fabric peer-group
 neighbor fabric remote-as external
 neighbor fabric description Internal Fabric Network
 neighbor fabric capability extended-nexthop
 neighbor swp1 interface peer-group fabric
 neighbor swp2 interface peer-group fabric
 neighbor swp3 interface peer-group fabric
 neighbor swp4 interface peer-group fabric
 !
 address-family ipv4 unicast
  network 10.0.0.21/32
  neighbor fabric prefix-list dc-spine in
  neighbor fabric prefix-list dc-spine out
 exit-address-family
 !
!
 address-family ipv6 unicast
  neighbor fabric activate
 exit-address-family
 !
 address-family evpn
  neighbor fabric activate
 exit-address-family
 exit
!
ip prefix-list dc-spine seq 10 permit 0.0.0.0/0
ip prefix-list dc-spine seq 20 permit 10.0.0.0/24 le 32
ip prefix-list dc-spine seq 500 deny any
!
line vty
!
end</code></pre></td>
<td>spine02 /etc/quagga/Quagga.conf
<pre><code>!
interface swp1
 ipv6 nd ra-interval 10
 no ipv6 nd suppress-ra
!
interface swp2
 ipv6 nd ra-interval 10
 no ipv6 nd suppress-ra
!
interface swp3
 ipv6 nd ra-interval 10
 no ipv6 nd suppress-ra
!
interface swp4
 ipv6 nd ra-interval 10
 no ipv6 nd suppress-ra
!
router bgp 65020
 bgp router-id 10.0.0.22
 bgp bestpath as-path multipath-relax
 neighbor fabric peer-group
 neighbor fabric remote-as external
 neighbor fabric description Internal Fabric Network
 neighbor fabric capability extended-nexthop
 neighbor swp1 interface peer-group fabric
 neighbor swp2 interface peer-group fabric
 neighbor swp3 interface peer-group fabric
 neighbor swp4 interface peer-group fabric
 !
 address-family ipv4 unicast
  network 10.0.0.22/32
  neighbor fabric prefix-list dc-spine in
  neighbor fabric prefix-list dc-spine out
 exit-address-family
 !
!
 address-family ipv6 unicast
  neighbor fabric activate
 exit-address-family
 !
 address-family evpn
  neighbor fabric activate
 exit-address-family
 exit
!
ip prefix-list dc-spine seq 10 permit 0.0.0.0/0
ip prefix-list dc-spine seq 20 permit 10.0.0.0/24 le 32
ip prefix-list dc-spine seq 500 deny any
!
line vty
!
end</code></pre></td>
</tr>
</tbody>
</table>

### <span>server01 and server02 Configurations</span>

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="odd">
<td>server01 /etc/network/interfaces
<pre><code>#configuration is for Cumulus VX
#in real life this is a server OS
 
auto eth0
iface eth0 inet dhcp
 
auto eth1
iface eth1
    address 172.16.1.101/24
 
auto eth1.100
iface eth1.100
    address 172.16.100.101/24
 
auto eth1.200
iface eth1.200
    address 172.16.200.101/24</code></pre></td>
<td>server02 /etc/network/interfaces
<pre><code>#configuration is for Cumulus VX
#in real life this is a server OS
 
auto eth0
iface eth0 inet dhcp
 
auto eth2
iface eth2
    address 172.16.1.102/24
 
auto eth2.100
iface eth2.100
    address 172.16.100.102/24
 
auto eth2.200
iface eth2.200
    address 172.16.200.102/24</code></pre></td>
</tr>
</tbody>
</table>

## <span>EVPN Provisioning</span>

EVPN can be provisioned with either RDs and RTs automatically
configured, or by manually defining them. The output below shows example
[Quagga
configuration](/version/cumulus-linux-312/Layer_3_Features/Configuring_Quagga/)
for these two provisioning options:

### <span>Enable EVPN with Automatic RDs and RTs</span>

    router bgp 65011
     bgp router-id 10.0.0.11
     
     
    ... #code removed for brevity
     
     
     !
     address-family evpn
      neighbor fabric activate
      advertise-vni
     exit-address-family
     exit

### <span>Enable EVPN with User-defined RDs and RTs for Some VNIs</span>

    router bgp 65100
     address-family evpn
      neighbor swp1 activate
      advertise-vni
      vni 10200
         rd 172.16.10.1:20
         route-target both 65100:20

## <span>Testing Connectivity between Servers</span>

SSH to server01 and ping the VLAN1 IP address on server02:

    user@server01:~$ ping 172.16.1.102
    PING 172.16.1.102 (172.16.1.102) 56(84) bytes of data.
    64 bytes from 172.16.1.102: icmp_seq=1 ttl=64 time=2.52 ms
    64 bytes from 172.16.1.102: icmp_seq=2 ttl=64 time=2.74 ms
    ^C
    --- 172.16.1.102 ping statistics ---
    2 packets transmitted, 2 received, 0% packet loss, time 1001ms
    rtt min/avg/max/mdev = 2.528/2.638/2.749/0.121 ms

The following table lists all the servers IP addresses to test
connectivity across the L3 fabric:

|         | server01       | server02       | server03       | server04       |
| ------- | -------------- | -------------- | -------------- | -------------- |
| VLAN1   | 172.16.1.101   | 172.16.1.102   | 172.16.1.103   | 172.16.1.104   |
| VLAN100 | 172.16.100.101 | 172.16.100.102 | 172.16.100.103 | 172.16.100.104 |
| VLAN200 | 172.16.200.101 | 172.16.200.102 | 172.16.200.103 | 172.16.200.104 |

## <span>BGP Output Commands</span>

The following commands are not unique to EVPN but help troubleshoot
connectivity and route propagation. You can display the L3 fabric by
running the Quagga `show ip bgp summary` command on one of the spines:

    cumulus@spine01:~$ sudo vtysh
    spine01# show ip bgp sum
    BGP router identifier 10.0.0.21, local AS number 65020 vrf-id 0
    BGP table version 7
    RIB entries 9, using 1152 bytes of memory
    Peers 4, using 83 KiB of memory
    Peer groups 1, using 72 bytes of memory
    Neighbor        V         AS MsgRcvd MsgSent   TblVer  InQ OutQ Up/Down  State/PfxRcd
    leaf01(swp1)    4 65011    1038    1012        0    0    0 00:49:11        1
    leaf02(swp2)    4 65012    1042    1018        0    0    0 00:49:30        1
    leaf03(swp3)    4 65013    1013     995        0    0    0 00:41:20        1
    leaf04(swp4)    4 65014    1026    1012        0    0    0 00:49:10        1
    Total number of neighbors 4

You can see the loopback addresses for all the network devices
participating in BGP by running the `show ip bgp` command:

    cumulus@spine01:~$ sudo vtysh
    spine01# show ip bgp
    BGP table version is 7, local router ID is 10.0.0.21
    Status codes: s suppressed, d damped, h history, * valid, > best, = multipath,
                  i internal, r RIB-failure, S Stale, R Removed
    Origin codes: i - IGP, e - EGP, ? - incomplete
       Network          Next Hop            Metric LocPrf Weight Path
    *> 10.0.0.11/32     swp1            0              0 65011 i
    *> 10.0.0.12/32     swp2            0              0 65012 i
    *> 10.0.0.13/32     swp3            0              0 65013 i
    *> 10.0.0.14/32     swp4            0              0 65014 i
    *> 10.0.0.21/32     0.0.0.0                  0          32768 i
    Displayed  5 out of 5 total prefixes

## <span>EVPN BGP Output Commands</span>

The following commands are unique to EVPN address-families and VXLAN.
Note that just because two network nodes are BGP peers does not mean
they are EVPN address-family peers or are exchanging VXLAN information.

### <span>Displaying EVPN address-family Peers</span>

The network device participating in BGP EVPN address-family can be shown
using the ` show bgp evpn summary  `command

    cumulus@spine01:~$ sudo vtysh
    spine01# show bgp evpn summary
    BGP router identifier 10.0.0.21, local AS number 65020 vrf-id 0
    BGP table version 0
    RIB entries 23, using 2944 bytes of memory
    Peers 4, using 83 KiB of memory
    Peer groups 1, using 72 bytes of memory
    Neighbor        V         AS MsgRcvd MsgSent   TblVer  InQ OutQ Up/Down  State/PfxRcd
    leaf01(swp1)    4 65011    1103    1077        0    0    0 00:52:24        3
    leaf02(swp2)    4 65012    1106    1082        0    0    0 00:52:43        3
    leaf03(swp3)    4 65013    1078    1060        0    0    0 00:44:33        3
    leaf04(swp4)    4 65014    1090    1076        0    0    0 00:52:23        3
    Total number of neighbors 4

### <span>Displaying VNIs</span>

You can display the configured VNIs on a network device participating in
BGP EVPN by running the `show bgp evpn vni` command. The following
example examines leaf01, where 3 VXLANs are configured:

    cumulus@leaf01:~$ sudo vtysh
    leaf01# show bgp evpn vni
    BGP EVPN INFORMATION
    Advertise VNI flag: Enabled
    VNI: 10200
      RD: 10.0.0.11:10200
      Originator IP: 10.0.0.11
      Import Route Target:
         65011:10200
      Export Route Target:
         65011:10200
    VNI: 10001
      RD: 10.0.0.11:10001
      Originator IP: 10.0.0.11
      Import Route Target:
         65011:10001
      Export Route Target:
         65011:10001
    VNI: 10100
      RD: 10.0.0.11:10100
      Originator IP: 10.0.0.11
      Import Route Target:
         65011:10100
      Export Route Target:
         65011:10100

Notice that the spine01 switch is sharing VNI information but does not
have any VNIs configured on itself:

    cumulus@spine01:~$ sudo vtysh
    spine01# show bgp evpn vni
    BGP EVPN INFORMATION
    Advertise VNI flag: Enabled

### <span>Displaying EVPN VXLANs</span>

Run the `show evpn vni` command to list all local configured VXLANs and
remote VTEPs:

    cumulus@leaf01:~$ sudo vtysh
    leaf01# show evpn vni
    VNI: 10200
     VxLAN interface: vxlan10200 ifIndex: 15 VTEP IP: 10.0.0.11
     Remote VTEPs for this VNI:
      10.0.0.13
      10.0.0.12
      10.0.0.14
    VNI: 10001
     VxLAN interface: vxlan10001 ifIndex: 16 VTEP IP: 10.0.0.11
     Remote VTEPs for this VNI:
      10.0.0.13
      10.0.0.12
      10.0.0.14
    VNI: 10100
     VxLAN interface: vxlan10100 ifIndex: 14 VTEP IP: 10.0.0.11
     Remote VTEPs for this VNI:
      10.0.0.13
      10.0.0.12
      10.0.0.14

### <span>Displaying BGP EVPN Routes</span>

Run the `show bgp evpn route` command to display all EVPN routes at the
same time:

    cumulus@leaf01:~$ sudo vtysh
    leaf01# show bgp evpn route
    BGP table version is 0, local router ID is 10.0.0.11
    Status codes: s suppressed, d damped, h history, * valid, > best, i - internal
    Origin codes: i - IGP, e - EGP, ? - incomplete
     
       Network          Next Hop            Metric LocPrf Weight Path
    Route Distinguisher: 10.0.0.11:10001
    *> [3]:[0]:[4]:[10.0.0.11]
                                           32768 i
    Route Distinguisher: 10.0.0.11:10100
    *> [3]:[0]:[4]:[10.0.0.11]
                                           32768 i
    Route Distinguisher: 10.0.0.11:10200
    *> [3]:[0]:[4]:[10.0.0.11]
                                           32768 i
    Route Distinguisher: 10.0.0.12:10001
    *  [3]:[0]:[4]:[10.0.0.12]
                                               0 65020 65012 i
    *> [3]:[0]:[4]:[10.0.0.12]
                                               0 65020 65012 i
    Route Distinguisher: 10.0.0.12:10100
    *  [3]:[0]:[4]:[10.0.0.12]
                                               0 65020 65012 i
    *> [3]:[0]:[4]:[10.0.0.12]
                                               0 65020 65012 i
    Route Distinguisher: 10.0.0.12:10200
    *  [3]:[0]:[4]:[10.0.0.12]
                                               0 65020 65012 i
    *> [3]:[0]:[4]:[10.0.0.12]
                                               0 65020 65012 i
    Route Distinguisher: 10.0.0.13:10001
    *  [3]:[0]:[4]:[10.0.0.13]
                                               0 65020 65013 i
    *> [3]:[0]:[4]:[10.0.0.13]
                                               0 65020 65013 i
    Route Distinguisher: 10.0.0.13:10100
    *  [3]:[0]:[4]:[10.0.0.13]
                                               0 65020 65013 i
    *> [3]:[0]:[4]:[10.0.0.13]
                                               0 65020 65013 i
    Route Distinguisher: 10.0.0.13:10200
    *  [3]:[0]:[4]:[10.0.0.13]
                                               0 65020 65013 i
    *> [3]:[0]:[4]:[10.0.0.13]
                                               0 65020 65013 i
    Route Distinguisher: 10.0.0.14:10001
    *  [3]:[0]:[4]:[10.0.0.14]
                                               0 65020 65014 i
    *> [3]:[0]:[4]:[10.0.0.14]
                                               0 65020 65014 i
    Route Distinguisher: 10.0.0.14:10100
    *  [3]:[0]:[4]:[10.0.0.14]
                                               0 65020 65014 i
    *> [3]:[0]:[4]:[10.0.0.14]
                                               0 65020 65014 i
    Route Distinguisher: 10.0.0.14:10200
    *  [3]:[0]:[4]:[10.0.0.14]
                                               0 65020 65014 i
    *> [3]:[0]:[4]:[10.0.0.14]
                                               0 65020 65014 i
     
    Displayed 21 out of 21 total prefixes

#### <span>Output Explained</span>

  - The output ` *> [3]:[0]:[4]:[10.0.0.14]  `is explained as follows:
    
    | Output    | Explanation                         |
    | --------- | ----------------------------------- |
    | \[3\]     | Type 3 EVPN route                   |
    | \[0\]     | Ethernet tag                        |
    | \[4\]     | IP address length of 4 bytes        |
    | 10.0.0.14 | IPv4 address originating this route |
    

<!-- end list -->

  - The output `Displayed 21 out of 21 total prefixes` is derived as
    follows: 4 VTEPs (leaf01, leaf02, leaf03, leaf04) x 3 VXLANs each =
    12 VXLANs. There are two spine switches (for
    [ECMP](/version/cumulus-linux-312/Layer_3_Features/Equal_Cost_Multipath_Load_Sharing_-_Hardware_ECMP)),
    giving us 24 total prefixes. However, three of them are originating,
    so 24-3 = 21 prefixes.

### <span>Displaying a Specific EVPN Route</span>

To drill down on a specific route for more information, run the `show
bgp evpn route rd <VTEP:VXLAN>` command:

    cumulus@leaf01:~$ sudo vtysh
    leaf01# show bgp evpn route rd 10.0.0.14:10100
    BGP routing table entry for 10.0.0.14:10100
    Paths: (2 available, best #2)
      Advertised to non peer-group peers:
      spine01(swp51) spine02(swp52)
    Route [3]:[0]:[4]:[10.0.0.14]
      65020 65014
        10.0.0.14 from spine02(swp52) (10.0.0.22)
          Origin IGP, localpref 100, valid, external
          Extended Community: RT:65014:10100
          AddPath ID: RX 0, TX 54
          Last update: Thu Nov  3 16:01:43 2016
    Route [3]:[0]:[4]:[10.0.0.14]
      65020 65014
        10.0.0.14 from spine01(swp51) (10.0.0.21)
          Origin IGP, localpref 100, valid, external, bestpath-from-AS 65020, best
          Extended Community: RT:65014:10100
          AddPath ID: RX 0, TX 26
          Last update: Thu Nov  3 15:33:48 2016

## <span>Caveats</span>

The following caveats are in place for the early access release:

  - EVPN is only supported on platforms with Broadcom chipsets — same as
    for VXLAN itself.

  - [VXLAN active-active
    mode](/version/cumulus-linux-312/Layer_1_and_Layer_2_Features/Network_Virtualization/Lightweight_Network_Virtualization_-_LNV/LNV_VXLAN_Active-Active_Mode)
    is not supported.

  - Only VNI values less than 65535 are supported.

  - There is no support for route reflection of EVPN routes.

  - When iBGP is used to exchange EVPN routes between VTEPs, OSPF (or
    static routing) has to be used as the underlay routing protocol.

  - Cannot interoperate with other vendors' EVPN implementations. While
    the type-3 route exchanged adheres to the RFC/draft, there is
    insufficient functionality for a successful interop.
