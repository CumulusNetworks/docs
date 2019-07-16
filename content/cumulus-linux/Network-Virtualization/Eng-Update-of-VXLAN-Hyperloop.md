---
title: Eng Update of VXLAN Hyperloop
author: Cumulus Networks
weight: 161
aliases:
 - /display/CL40/Eng-Update-of-VXLAN-Hyperloop
 - /pages/viewpage.action?pageId=8366606
pageID: 8366606
product: Cumulus Linux
version: '4.0'
imgData: cumulus-linux-40
siteSlug: cumulus-linux-40
---
This chapter describes how to configure VXLAN gateways using a loopback
cable (called a *hyperloop*) on non-RIOT (VXLAN routing) capable ASICs
running Cumulus Linux.

The Broadcom Trident II and Tomahawk ASICs have a limitation where a
layer 2 bridge that contains a VXLAN interface cannot also have an IP
address assigned to it. This is an expected limitation with this ASIC
because of the ordering of the decapsulation. A packet that is
decapsulated will already have passed the portion of the ASIC capable of
reading the IP address lookup (for example, VXLAN lookup occurs before
IP address lookup). Contact your [sales
team](mailto:sales@cumulusnetworks.com) if there is any confusion. Refer
to the [Cumulus Networks Hardware Compatibility
List](https://wiki.cumulusnetworks.com/cumulusnetworks.com/hcl) to
determine which ASIC is running on the switch.

**This limitation does not exist in some ASICs.** For example, the
Trident II+ provides the [RIOT (Routing In/Out of
Tunnels)](https://www.broadcom.com/press/release.php?id=s907324)
feature; see [VXLAN
Routing](/version/cumulus-linux-40/Network-Virtualization/VXLAN-Routing)
for more information.

## <span id="src-8366606_EngUpdateofVXLANHyperloop-reqs" class="confluence-anchor-link"></span><span>Requirements</span>

  - VXLAN hyperloop only works on an ASIC capable of encapsulating and
    decapsulating VXLAN traffic, which includes:
    
      - Broadcom Tomahawk
    
      - Broadcom Trident II
    
      - Broadcom Trident II+
    
      - Mellanox Spectrum

  - VXLAN hyperloop is supported on Cumulus Linux 3.2.1 and later. Make
    sure to [upgrade to the latest
    version](/version/cumulus-linux-40/Installation-Management/Upgrading-Cumulus-Linux)
    of Cumulus Linux.

  - If you are using
    [EVPN](/version/cumulus-linux-40/Network-Virtualization/Ethernet-Virtual-Private-Network---EVPN),
    you must be running FRRouting version eau8. Use the `dpkg -l`
    command to check the FRRouting version:
    
        cumulus@leaf01:mgmt-vrf:~$ dpkg -l frr
        Desired=Unknown/Install/Remove/Purge/Hold
        | Status=Not/Inst/Conf-files/Unpacked/halF-conf/Half-inst/trig-aWait/Trig-pend
        |/ Err?=(none)/Reinst-required (Status,Err: uppercase=bad)
        ||/ Name                     Version           Architecture      Description
        +++-========================-=================-=================-=====================================================
        ii  frr                      1.0.0+cl3eau8     amd64             BGP/OSPF/RIP routing daemon
    
    If you are not running the correct version of FRRouting for EVPN,
    [follow these
    directions](/version/cumulus-linux-40/Network-Virtualization/Ethernet-Virtual-Private-Network---EVPN)
    to upgrade.

{{%notice note%}}

EVPN inter-subnet routing (centralized, symmetric and asymmetric) are
not supported.

{{%/notice%}}

## <span>Hyperloop Use Cases</span>

Without native VXLAN routing support, external gateways, firewalls, or
routers are attached to a VTEP do the routing, as in the diagram below.

It is very common in network virtualization environments for firewalls
to sit on internal VXLAN-tied VLANs as well as external VLANs that are
routed out to the internet. Consider the following illustration. No
special configuration is needed on the switch because the firewall acts
as the gateway between the internal VLAN (VLAN20/VNI-20) and the
routable external VLAN 10. VLAN 10 could have an SVI (switch virtual
interface) configured to route out of the VLAN. This also has the
benefit in cases where a VXLAN represents a tenant (or a purposely
separated application) — you want to keep the firewall between VXLANs so
that traffic can be filtered and sanitized to the network operator's
specification.

{{% imgOld 0 %}}

With integrated VXLAN routing and bridging using a hyperloop:

  - You can avoid having to use external gateways or routers. A
    hyperloop provides the ability to do integrated VXLAN routing on a
    non-RIOT (VXLAN routing) ASIC.

  - If applications are hosted on the switch and require layer 3
    connectivity, you can use a hyperloop to provide reachability for
    this application as well.

Do **not** use a hyperloop under these circumstances:

  - If the external firewall is used for routing and security (as shown
    above), then there is no need for an external loopback as the
    firewall provides routing across subnets.

  - If bandwidth for the traffic to be routed is so large that you
    cannot provision such high bandwidth using a hyperloop, use
    dedicated gateways connected to exit leafs instead.

  - If north-south routing involves edge router functionality, then that
    functionality cannot be provided by leaf switches; it requires
    dedicated edge gateways to achieve the same result, like NAT.

### <span id="src-8366606_EngUpdateofVXLANHyperloop-hyperloop" class="confluence-anchor-link"></span><span>Exit a VXLAN with a Hyperloop</span>

### <span></span>

This limitation means a physical cable must be attached from one port on
leaf1 to another port on leaf1. One port is a layer 3 port while the
other is a member of the bridge. The native VLAN (VLAN ID 1) must be
tagged for all traffic going to the hyperloop ports.

For example, following the configuration above, for a layer 3 address to
be used as the gateway for vni-10, configure the following on exit01:

    cumulus@exit01:~$ sudo nano /etc/network/interfaces
     
    auto lo
    iface lo inet loopback
       address 10.0.0.11/32
     
    ## some output removed for brevity (such as peerlink and host-facing bonds) ##
     
    auto bridge
    iface bridge
        bridge-vlan-aware yes
        bridge-ports inside server01 server02 vni-10 vni-20 peerlink
        bridge-vids 100 200
        bridge-pvid 1             # sets native VLAN to 1, an unused VLAN
        mstpctl-treeprio 8192
     
    auto outside
    iface outside
        bond-slaves swp45 swp47
        alias hyperloop outside 
        mstpctl-bpduguard yes
        mstpctl-portbpdufilter yes
     
    auto inside
    iface inside
        bond-slaves swp46 swp48
        alias hyperloop inside 
        mstpctl-bpduguard yes
        mstpctl-portbpdufilter yes
     
    auto VLAN100GW
    iface VLAN100GW
        bridge_ports outside.100
        address 172.16.100.2/24
        alias VXLAN GW 100 Linux Bridge
        address-virtual 44:38:39:FF:01:90 172.16.100.1/24
     
    auto VLAN200GW
    iface VLAN200GW
       bridge_ports outside.200
       address 172.16.200.2/24
       alias VXLAN GW 200 Linux Bridge
       address-virtual 44:38:39:FF:02:90 172.16.200.1/24 
     
    auto vni-10
    iface vni-10
        vxlan-id 10
        vxlan-local-tunnelip 10.0.0.11
        bridge-access 100
     
    auto vni-20
    iface vni-20
        vxlan-id 20
        vxlan-local-tunnelip 10.0.0.11
        bridge-access 200

### <span>Packet Flow Diagram</span>

{{% imgOld 1 %}}

### <span>Trident II and Tomahawk switchd Flag</span>

For the Broadcom Trident II and Tomahawk ASICs to be able to have a
hyperloop work correctly, you must configure the following `switchd`
flag. This change is not needed on any other hardware ASIC.

    cumulus@exit01:mgmt-vrf:/root$ sudo nano /etc/cumulus/switchd.conf
    hal.bcm.per_vlan_router_mac_lookup = TRUE

Restart `switchd` for the change to take place:

    cumulus@exit01:mgmt-vrf:/root$ sudo systemctl restart switchd.service

{{%notice warning%}}

Restarting `switchd` is a disruptive change and affects data plane
network traffic.

{{%/notice%}}

{{%notice warning%}}

Setting `hal.bcm.per_vlan_router_mac_lookup = TRUE` limits the Trident
II switch to a configurable 512 local IP addresses (SVIs and so forth).
Use this only as a last resort. This is only a limitation on this
specific ASIC type.

{{%/notice%}}

## <span>VXLAN Hyperloop Troubleshooting Matrix</span>

Before you follow these troubleshooting steps, make sure your switch
meets the [requirements specified
above](#src-8366606_EngUpdateofVXLANHyperloop-reqs).

### <span>Are HER (Head End Replication) entries being programmed into the bridge fdb table?</span>

Check for 00:00:00:00:00:00 entries for each VXLAN using the `bridge fdb
show` command:

    cumulus@leaf03:mgmt-vrf:~$ bridge fdb show | grep 00:00:00:00:00:00
    00:00:00:00:00:00 dev vni-40 dst 10.10.10.30 self permanent
    00:00:00:00:00:00 dev vni-40 dst 10.10.10.40 self permanent
    00:00:00:00:00:00 dev vni-1 dst 10.10.10.30 self permanent
    00:00:00:00:00:00 dev vni-1 dst 10.10.10.40 self permanent
    00:00:00:00:00:00 dev vni-30 dst 10.10.10.30 self permanent
    00:00:00:00:00:00 dev vni-30 dst 10.10.10.40 self permanent
    00:00:00:00:00:00 dev vni-20 dst 10.10.10.30 self permanent
    00:00:00:00:00:00 dev vni-20 dst 10.10.10.40 self permanent
    00:00:00:00:00:00 dev vni-50 dst 10.10.10.30 self permanent
    00:00:00:00:00:00 dev vni-50 dst 10.10.10.40 self permanent
    00:00:00:00:00:00 dev vni-10 dst 10.10.10.30 self permanent
    00:00:00:00:00:00 dev vni-10 dst 10.10.10.40 self permanent

or use
[NCLU](/version/cumulus-linux-40/Layer-3/Configuring-FRRouting/Comparing-NCLU-and-vtysh-Commands):

    cumulus@leaf03:mgmt-vrf:~$ net show bridge macs
    VLAN      Master    Interface    MAC                TunnelDest    State      Flags    LastSeen
    --------  --------  -----------  -----------------  ------------  ---------  -------  ----------------
    1         bridge    server03     90:e2:ba:7e:96:d9                                    00:01:07
    untagged            vni-1        00:00:00:00:00:00  10.10.10.30   permanent  self     4 days, 22:25:42
    untagged            vni-1        00:00:00:00:00:00  10.10.10.40   permanent  self     4 days, 22:25:42
    untagged            vni-10       00:00:00:00:00:00  10.10.10.30   permanent  self     4 days, 22:25:42
    untagged            vni-10       00:00:00:00:00:00  10.10.10.40   permanent  self     4 days, 22:25:42
    untagged            vni-20       00:00:00:00:00:00  10.10.10.30   permanent  self     4 days, 22:25:42
    untagged            vni-20       00:00:00:00:00:00  10.10.10.40   permanent  self     4 days, 22:25:42
    untagged            vni-30       00:00:00:00:00:00  10.10.10.30   permanent  self     4 days, 22:25:42
    untagged            vni-30       00:00:00:00:00:00  10.10.10.40   permanent  self     4 days, 22:25:42
    untagged            vni-40       00:00:00:00:00:00  10.10.10.30   permanent  self     4 days, 22:25:42
    untagged            vni-40       00:00:00:00:00:00  10.10.10.40   permanent  self     4 days, 22:25:42
    untagged            vni-50       00:00:00:00:00:00  10.10.10.30   permanent  self     4 days, 22:25:42
    untagged            vni-50       00:00:00:00:00:00  10.10.10.40   permanent  self     4 days, 22:25:42
    untagged  bridge    peerlink     2c:60:0c:72:eb:a0                permanent           5 days, 00:53:13
    untagged  bridge    server03     2c:60:0c:72:eb:70                permanent           5 days, 00:53:13
    untagged  bridge    vni-1        86:c9:5c:cc:88:54                permanent           4 days, 22:28:23
    untagged  bridge    vni-10       32:d5:3a:99:36:f7                permanent           4 days, 22:28:23
    untagged  bridge    vni-20       9a:91:5a:7e:0f:e8                permanent           4 days, 22:28:23
    untagged  bridge    vni-30       6a:33:ff:fd:ca:34                permanent           4 days, 22:28:23
    untagged  bridge    vni-40       e2:1f:a4:7c:75:2b                permanent           4 days, 22:28:23
    untagged  bridge    vni-50       d6:df:b4:85:4d:55                permanent           4 days, 22:28:23

{{%notice tip%}}

If you are not seeing HER entries, make sure that you are not using the
reserved VLAN range; the default is 3000-3999. This range is stored in
the `resv_vlan_range` variable in the `/etc/cumulus/switchd.conf` file.

{{%/notice%}}

### <span>If you are using an MLAG VTEP (dual attached), is it set up correctly?</span>

Check the outputs. Often, when VXLAN is considered to be non-working, it
is actually due to an incorrect setup on the server OS, whether it is
Ubuntu, Microsoft Windows, or RHEL.  
  

{{% imgOld 2 %}}

### <span>Can you ping from host to host on the same VXLAN?</span>

In the following network diagram, can server01 ping to server03 on any
of the VLANs (VLAN1, VLAN100, VLAN200)?  

{{% imgOld 3 %}}

  
If you cannot even ping from server to server, this is not a VXLAN
gateway problem but a problem with the network itself. You must resolve
the network problem before you make a VXLAN gateway, with or without a
hyperloop.

{{%notice warning%}}

Only proceed past this point if you can get server to server
connectivity on the same VXLAN.

{{%/notice%}}

### <span>Is the SVI on a physical interface or on a traditional bridge? </span>

{{%notice warning%}}

The SVI (switch virtual interface) IP address for a hyperloop MUST be on
a traditional bridge. Follow the configuration guidelines above.

{{%/notice%}}

### <span>Is the port plugged in correctly?</span>

Use the `lldpctl` or `net show lldp` commands to see which ports are
hooked up:

    cumulus@leaf03:mgmt-vrf:~$ net show lldp
    Local Port    Speed    Mode                 Remote Port        Remote  Host     Summary
    ------------  -------  -------------  ----  -----------------  ---------------  -------------------------
    eth0          1G       Mgmt           ====  swp42              oob-mgmt-switch  IP: 10.50.100.53/24(DHCP)
    swp1          10G      BondMember     ====  90:e2:ba:7e:96:d8  server03         Master: server03(UP)
    swp49         40G      BondMember     ====  swp49              leaf04           Master: peerlink(UP)
    swp50         40G      BondMember     ====  swp50              leaf04           Master: peerlink(UP)
    swp51         40G      NotConfigured  ====  swp3               spine01
    swp52         40G      NotConfigured  ====  swp3               spine02
    swp53         40G      NotConfigured  ====  swp54              leaf03
    swp54         40G      NotConfigured  ====  swp53              leaf03

Notice above that swp53 and swp54 are a loopback cable (hyperloop) where
it is connected to itself.

### <span>Is the VRR MAC address unique per subnet?</span>

Make sure that [VRR is configured
correctly](/version/cumulus-linux-40/Layer-2/Virtual-Router-Redundancy---VRR-and-VRRP)
and that each MAC address is unique per VLAN.

<article id="html-search-results" class="ht-content" style="display: none;">

</article>

<footer id="ht-footer">

</footer>
