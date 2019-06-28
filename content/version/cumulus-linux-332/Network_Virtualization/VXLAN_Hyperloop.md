---
title: VXLAN Hyperloop
author: Cumulus Networks
weight: 151
aliases:
 - /display/CL332/VXLAN+Hyperloop
 - /pages/viewpage.action?pageId=5869109
pageID: 5869109
product: Cumulus Linux
version: 3.3.2
imgData: cumulus-linux-332
siteSlug: cumulus-linux-332
---
This chapter covers configuring VXLAN gateways using a loopback cable
(which we call a *hyperloop*) on non-RIOT (VXLAN routing) capable ASICs
running Cumulus Linux.

The Broadcom Trident II and Tomahawk ASICs have a limitation where a
layer 2 bridge that contains a VXLAN interface can not also have an IP
address assigned to it. This is an expected limitation with this ASIC,
because of the ordering of the decapsulation. A packet that is
decapsulated will already have passed the portion of the ASIC capable of
reading the IP address lookup (for example, VXLAN lookup happens before
IP address lookup). As of Cumulus Linux 3.2.1 even ASICs that are
capable of VXLAN routing (such as the Broadcom Trident II+ or Mellanox
Spectrum) also require a hyperloop. Please contact your [sales
team](mailto:sales@cumulusnetworks.com) if there is any confusion. Refer
to the [Cumulus Networks Hardware Compatibility
List](https://cumulusnetworks.com/hcl) to determine which ASIC is
running on the switch.

**This limitation will not exist in future ASICs.** For example, the
Trident II+ has the [RIOT (Routing In/Out of
Tunnels)](https://www.broadcom.com/press/release.php?id=s907324)
feature.

{{%notice warning%}}

RIOT and VXLAN routing are not supported in Cumulus Linux; use a
hyperloop instead.

{{%/notice%}}

## <span id="src-5869109_VXLANHyperloop-reqs" class="confluence-anchor-link"></span><span>Requirements</span>

  - VXLAN hyperloop only works on an ASIC capable of encapsulating and
    decapsulating VXLAN traffic, which includes:
    
      - Broadcom Tomahawk
    
      - Broadcom Trident II
    
      - Broadcom Trident II+
    
      - Mellanox Spectrum

  - VXLAN hyperloop is supported on Cumulus Linux 3.2.1 and later. Make
    sure to [upgrade to the latest
    version](/version/cumulus-linux-332/Installation_Management/Upgrading_Cumulus_Linux)
    of Cumulus Linux.

  - If you are using
    [EVPN](/version/cumulus-linux-332/Network_Virtualization/Ethernet_Virtual_Private_Network_-_EVPN),
    you must be running Quagga version eau8. Use a `dpkg -l` to check
    the Quagga version:
    
        cumulus@leaf01:mgmt-vrf:~$ dpkg -l quagga
        Desired=Unknown/Install/Remove/Purge/Hold
        | Status=Not/Inst/Conf-files/Unpacked/halF-conf/Half-inst/trig-aWait/Trig-pend
        |/ Err?=(none)/Reinst-required (Status,Err: uppercase=bad)
        ||/ Name                     Version           Architecture      Description
        +++-========================-=================-=================-=====================================================
        ii  quagga                   1.0.0+cl3eau8     amd64             BGP/OSPF/RIP routing daemon
    
    If you are not running the right version of Quagga for EVPN, [follow
    these
    directions](/version/cumulus-linux-332/Network_Virtualization/Ethernet_Virtual_Private_Network_-_EVPN)
    to upgrade.

## <span>Hyperloop Use Cases</span>

Without native VXLAN routing support, external gateways, firewalls or
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

  - You can avoid having to use external gateways/routers. A hyperloop
    gives you the ability to do integrated VXLAN routing on a non-RIOT
    (VXLAN routing) ASIC.

  - If applications are hosted on the switch and need layer 3
    connectivity, then a hyperloop can be used to provide reachability
    for this application as well.

You should **not** use a hyperloop under these circumstances:

  - If the external firewall is used for routing and security (as shown
    above), then there is no need for an external loopback as the
    firewall takes care of routing across subnets.

  - If bandwidth for the traffic to be routed is so large that you
    cannot provision such high bandwidth using a hyperloop, then you
    should have dedicated gateways connected to exit leafs instead.

  - If north-south routing involves edge router functionality, then that
    functionality cannot be provided by leaf switches; rather, it
    requires dedicated edge gateways to achieve the same result, like
    NAT.

### <span id="src-5869109_VXLANHyperloop-hyperloop" class="confluence-anchor-link"></span><span>Exiting a VXLAN with a Hyperloop</span>

### <span></span>

This limitation means a physical cable must be attached from one port on
leaf1 to another port on leaf1. One port is a layer 3 port while the
other is a member of the bridge. The native VLAN (VLAN ID 1) must be
tagged for all traffic going to the hyperloop ports.

For example, following the configuration above, in order for a layer 3
address to be used as the gateway for vni-10, you could configure the
following on exit01:

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

In order for the Broadcom Trident II and Tomahawk ASICs to be able to
have a hyperloop work correctly, you must configure the following
`switchd` flag. This change is not needed on any other hardware ASIC.

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
II switch to a configurable 512 local IP addresses (SVIs and so forth),
so you should use this only as a last resort. This is only a limitation
on this specific ASIC type.

{{%/notice%}}

## <span>VXLAN Hyperloop Troubleshooting Matrix</span>

Before you follow these troubleshooting steps, make sure your switch
meets the [requirements specified
above](#src-5869109_VXLANHyperloop-reqs).

### <span>Are HER (Head End Replication) entries being programmed into the bridge fdb table?</span>

Check for 00:00:00:00:00:00 entries for each VXLAN using `bridge fdb
show`:

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
[NCLU](/version/cumulus-linux-332/Layer_Three/Configuring_Quagga/Comparing_NCLU_and_vtysh_Commands):

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

If you are not getting HER entries, there are some steps you can try:

  - Make sure you are using
    [LNV](/version/cumulus-linux-332/Network_Virtualization/Lightweight_Network_Virtualization_-_LNV_Overview/)
    **OR** EVPN. You cannot use both at the same time.

  - Make sure you are not trying to use any VNI/VXLAN values over 65535.
    For example, VXLAN 70000 is not supported in Cumulus Linux 3.3.

  - Make sure you are not using the reserved VLAN range; by default it
    is 3000-3999. This range is stored in the `resv_vlan_range` variable
    in the `/etc/cumulus/switchd.conf` file.

### <span>If you are using an MLAG VTEP (dual attached), is it set up correctly?</span>

Check the outputs. Often, when VXLAN is considered to be non-working,
it's actually due to an incorrect setup on the server OS, whether it's
Ubuntu, Microsoft Windows or RHEL.  
  

{{% imgOld 2 %}}

### <span>Can you ping from host to host on the same VXLAN?</span>

For example, in the following network diagram, can server01 ping to
server03 on any of the VLANs (VLAN1, VLAN100, VLAN200)?  

{{% imgOld 3 %}}

  
If you can't even ping from server to server this is not a VXLAN gateway
problem, but a problem with the network itself. This must be fixed prior
to making a VXLAN gateway, with or without a hyperloop.

{{%notice warning%}}

Only proceed past this point if you can get server to server
connectivity on the same VXLAN.

{{%/notice%}}

### <span>Is the SVI on a physical interface or on a traditional bridge? </span>

{{%notice warning%}}

The SVI (switch virtual interface) IP address for a hyperloop MUST be on
a traditional bridge. Please follow the configuration guidelines above.

{{%/notice%}}

### <span>Is the port plugged in where it is supposed to be plugged in?</span>

Use `lldpctl` or `net show lldp` to see what ports are hooked up:

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
correctly](/version/cumulus-linux-332/Layer_One_and_Two/Virtual_Router_Redundancy_-_VRR/)
and that each MAC address is unique per VLAN.
