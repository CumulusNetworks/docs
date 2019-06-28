---
title: Hybrid Cloud Connectivity with QinQ and VXLANs
author: Cumulus Networks
weight: 155
aliases:
 - /display/CL332/Hybrid+Cloud+Connectivity+with+QinQ+and+VXLANs
 - /pages/viewpage.action?pageId=5869127
pageID: 5869127
product: Cumulus Linux
version: 3.3.2
imgData: cumulus-linux-332
siteSlug: cumulus-linux-332
---
{{%notice warning%}}

**Early Access Feature**

QinQ is an [early access
feature](https://support.cumulusnetworks.com/hc/en-us/articles/202933878)
in Cumulus Linux. Before you can install QinQ, you must enable the Early
Access repository. For more information about the Cumulus Linux
repository, read [this knowledge base
article](https://support.cumulusnetworks.com/hc/en-us/articles/217422127).

{{%/notice%}}

*QinQ* is an amendment to the [IEEE 802.1Q
specification](http://www.ieee802.org/1/pages/802.1Q.html) that provides
the capability for multiple [VLAN
tags](/version/cumulus-linux-332/Layer_One_and_Two/Ethernet_Bridging_-_VLANs/VLAN_Tagging)
to be inserted into a single Ethernet frame.

The primary use case for QinQ with VXLAN is where a service provider who
offers multi-tenant layer 2 connectivity between different customers’
data centers (private clouds) may also need to connect those data
centers to public cloud providers. Public clouds often has a mandatory
QinQ handoff interface, where the outer tag is for the customer and the
inner tag is for the service.

In Cumulus Linux, you map QinQ packets to VXLANs through:

  - *Single tag translation*, where you map a customer to a VNI and
    preserve the service as an inner VLAN inside a VXLAN packet.

  - *Double tag translation*, where you map a customer and service to a
    VNI.

## <span>Installing the QinQ Metapackage</span>

To install the QinQ metapackage on a switch:

1.  Open the `/etc/apt/sources.list` file in a text editor.

2.  Uncomment the early access repo lines and save the file:
    
        #deb        http://repo3.cumulusnetworks.com/repo CumulusLinux-3-early-access cumulus
        #deb-src    http://repo3.cumulusnetworks.com/repo CumulusLinuz-3-early-access cumulus

3.  Run the following commands to install the QinQ metapackage in
    Cumulus Linux:
    
        cumulus@switch:~$ sudo -E apt-get update
        cumulus@switch:~$ sudo -E apt-get install cumulus-vxlan-routing
        cumulus@switch:~$ sudo -E apt-get install cumulus-qinq
        cumulus@switch:~$ sudo -E apt-get upgrade
    
    {{%notice info%}}
    
    Installing one of the two packages pulls in the other package, but
    both packages are listed here for sake of completeness.
    
    {{%/notice%}}

If you need to remove the QinQ packages, read the [early access
feature](https://support.cumulusnetworks.com/hc/en-us/articles/202933878)
article.

## <span>Configuring Single Tag Translation</span>

Single tag translation adheres to traditional QinQ service model. The
customer-facing interface is a QinQ access port with the outer S-tag
being the PVID, representing the customer. The S-tag is translated to a
VXLAN VNI. The inner C-tag, which represents the service, is transparent
to the provider. The public cloud handoff interface is a QinQ trunk
where packets on the wire carry both the S-tag and the C-tag.

Single tag translation leverages [VLAN-aware Linux
bridge](/version/cumulus-linux-332/Layer_One_and_Two/Ethernet_Bridging_-_VLANs/VLAN-aware_Bridge_Mode_for_Large-scale_Layer_2_Environments)
mode with the use of the 802.1ad VLAN protocol (the only supported
protocol at the time of writing). Hence, it is more scalable.

An example configuration could look like the following:

{{% imgOld 0 %}}

You configure two switches: one at the service provider edge that faces
the customer (the switch on the left above), and one on the public cloud
handoff edge (the righthand switch above).

{{%notice note%}}

All edges need to support QinQ with VXLANs to correctly interoperate.

{{%/notice%}}

### <span>Configuring the Public Cloud-facing Switch</span>

For the switch facing the public cloud:

  - Configure the bridge with `vlan_protocol` set to *802.1ad*.

  - The VNI maps back to S-tag (customer).

  - A trunk port connected to the public cloud is the QinQ trunk, and
    packets are double tagged, where the S-tag is for the customer and
    the C-tag is for the service.

To configure the public cloud-facing switch, run the following
[NCLU](/version/cumulus-linux-332/System_Configuration/Network_Command_Line_Utility)
commands:

    cumulus@switch:~$ net add vxlan vni-1000 vxlan id 1000
    cumulus@switch:~$ net add vxlan vni-1000 vxlan local-tunnelip 10.0.0.1
    cumulus@switch:~$ net add vxlan vni-1000 bridge access 100
    cumulus@switch:~$ net add vxlan vni-3000 vxlan id 3000
    cumulus@switch:~$ net add vxlan vni-3000 vxlan local-tunnelip 10.0.0.3
    cumulus@switch:~$ net add vxlan vni-3000 bridge access 200
    cumulus@switch:~$ net add bridge bridge vlan-protocol 802.1ad
    cumulus@switch:~$ net add bridge bridge ports swp3,vni-1000,vni-3000
    cumulus@switch:~$ net pending
    cumulus@switch:~$ net commit

These commands create the following configuration in the
`/etc/network/interfaces` file:

    auto vni-1000
    iface vni-1000
        address 10.0.0.1/24
        bridge-access 100
        vxlan-id 1000
     
    auto vni-3000
    iface vni-3000
        address 10.0.0.3/24
        bridge-access 200
        vlan-id 3000
     
    auto bridge
    iface bridge
        bridge-ports swp3 vni-1000 vni-3000
        bridge-vids 100, 200
        bridge-vlan-aware yes
        bridge-vlan-protocol 802.1ad

### <span>Configuring the Customer-facing Edge Switch</span>

For the switch facing the customer:

  - Configure the bridge with `vlan_protocol` set to *802.1ad*.

  - The customer interface is the QinQ access port, the PVID is the
    S-tag (customer) and is mapped to a VNI.

  - The service VLAN tags (C-tags) are preserved during VXLAN
    encapsulation.

To configure the customer-facing switch, run the following
[NCLU](/version/cumulus-linux-332/System_Configuration/Network_Command_Line_Utility)
commands:

    cumulus@switch:~$ net add interface swp3 bridge access 100
    cumulus@switch:~$ net add interface swp4 bridge access 200
    cumulus@switch:~$ net add vxlan vni-1000 vxlan id 1000
    cumulus@switch:~$ net add vxlan vni-13000 vxlan local-tunnelip 10.0.0.1
    cumulus@switch:~$ net add vxlan vni-1000 bridge access 100
    cumulus@switch:~$ net add vxlan vni-3000 vxlan id 3000
    cumulus@switch:~$ net add vxlan vni-3000 vxlan local-tunnelip 10.0.0.3
    cumulus@switch:~$ net add vxlan vni-3000 bridge access 200
    cumulus@switch:~$ net add bridge bridge vlan-protocol 802.1ad
    cumulus@switch:~$ net pending
    cumulus@switch:~$ net commit

These commands create the following configuration in the
`/etc/network/interfaces` file:

    auto vni-1000
    iface vni-1000
        address 10.0.0.1
        bridge-access 100
        vxlan-id 1000
     
    auto vni-3000
    iface vni-3000
        address 10.0.0.3
        bridge-access 200
        vxlan-id 3000
    auto swp3
    iface swp3
        bridge-access 100
     
    auto swp4
    iface swp4
        bridge-access 200
     
    auto bridge
    iface bridge
        bridge-ports swp3 swp4 vni-1000 vni-3000
        bridge-vlan-aware yes
        bridge-vlan-protocol 802.1ad

### <span>Viewing the Configuration</span>

In the output below, customer A is on VLAN 100 (S-TAG) and customer B is
on VLAN 200 (S-TAG).

To check the public cloud-facing switch, use `net show bridge vlan`:

    cumulus@switch:~$ net show bridge vlan
     
    Interface      VLAN  Flags                  VNI
    -----------  ------  ---------------------  -----
    swp7            100  PVID Egress Untagged
    swp8            200  PVID Egress Untagged
    vni1000         100  PVID Egress Untagged
    vni3000         200  PVID Egress Untagged
    bridge         None

To check the customer-facing switch, use `net show bridge vlan`:

    cumulus@switch:~$ net show bridge vlan 
    Interface      VLAN  Flags                  VNI
    -----------  ------  ---------------------  -----
    swp49s2           1  PVID, Egress Untagged
                    100
                    200
    swp49s3           1  PVID, Egress Untagged
                    100
                    200
    bridge          100
                    200
    vni100         100  PVID, Egress Untagged  10100
    vni200         200  PVID, Egress Untagged  10200

To verify that the bridge is configured for QinQ, run `ip -d link show
bridge` and look for *vlan\_protocol 802.1ad* in the output:

    root@qct-ly8-02:~# ip -d link show bridge
    287: bridge: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue state UP mode DEFAULT group default 
        link/ether 06:a2:ae:de:e3:43 brd ff:ff:ff:ff:ff:ff promiscuity 0 
        bridge forward_delay 1500 hello_time 200 max_age 2000 ageing_time 30000 stp_state 2 priority 32768 vlan_filtering 1 vlan_protocol 802.1ad bridge_id 8000.6:a2:ae:de:e3:43 designated_root 8000.6:a2:ae:de:e3:43 root_port 0 root_path_cost 0 topology_change 0 topology_change_detected 0 hello_timer    0.00 tcn_timer    0.00 topology_change_timer    0.00 gc_timer   64.29 vlan_default_pvid 1 vlan_stats_enabled 1 group_fwd_mask 0 group_address 01:80:c2:00:00:08 mcast_snooping 0 mcast_router 1 mcast_query_use_ifaddr 0 mcast_querier 0 mcast_hash_elasticity 4096 mcast_hash_max 4096 mcast_last_member_count 2 mcast_startup_query_count 2 mcast_last_member_interval 100 mcast_membership_interval 26000 mcast_querier_interval 25500 mcast_query_interval 12500 mcast_query_response_interval 1000 mcast_startup_query_interval 3125 mcast_stats_enabled 1 mcast_igmp_version 2 mcast_mld_version 1 nf_call_iptables 0 nf_call_ip6tables 0 nf_call_arptables 0 addrgenmode eui64 

## <span>Configuring Double Tag Translation</span>

Double tag translation involves a bridge with double-tagged member
interfaces, where a combination of the C-tag and S-tag map to a VNI. You
create the configuration only at the edge facing the public cloud. The
VXLAN configuration at the customer-facing edge doesn't need to change.

The double tag is always a cloud connection. The customer-facing edge is
either single-tagged or untagged. At the public cloud handoff point, the
VNI maps to double VLAN tags, with the S-tag indicating the customer and
the C-tag indicating the service.

{{%notice note%}}

The configuration in Cumulus Linux uses the outer tag for the customer
and the inner tag for the service.

{{%/notice%}}

You configure a double-tagged interface by stacking the VLANs in the
following manner: \<port\>.\<outer tag\>.\<inner tag\>. For example,
consider swp1.100.10: the outer tag is VLAN 100, which represents the
customer, and the inner tag is VLAN 10, which represents the service.

The outer tag or *TPID* (tagged protocol identifier) needs the
`vlan_protocol` to be specified. It can be either *802.1Q* or *802.1ad*.
If 802.1ad is used, it must be specified on the lower VLAN device, such
as swp3.100 in the example below.

{{%notice note%}}

Double tag translation only works with bridges in [traditional
mode](/version/cumulus-linux-332/Layer_One_and_Two/Ethernet_Bridging_-_VLANs/Traditional_Mode_Bridges)
(not VLAN-aware). As such, you cannot use NCLU to configure it.

{{%/notice%}}

An example configuration could look like the following:

{{% imgOld 1 %}}

### <span>Configuring the Switch</span>

To configure the switch for double tag translation using the above
example, edit the `/etc/network/interfaces` file in a text editor and
add the following:

    auto swp3.100
    iface swp3.100
        vlan_protocol 802.1ad
     
    auto swp3.100.10
    iface swp3.100.10
        mstpctl-portbpdufilter yes
        mstpctl-bpduguard yes
     
    auto vni1000
    iface vni1000
        address 10.0.0.1
        mstpctl-portbpdufilter yes
        mstpctl-bpduguard yes
        vxlan-id 1000
     
    auto custA-10-azr
    iface custA-10-azr
        bridge-ports swp3.100.10, vni1000
        bridge-vlan-aware no

You can check the configuration with the `brctl show` command:

    cumulus@switch:~$ sudo brctl show
    bridge name     bridge id               STP enabled     interfaces
    custA-10-azr    8000.00020000004b       yes             swp3.100.10                                              
                                                            vni1000
    custB-20-azr    8000.00020000004b       yes             swp3.200.20                                                        
                                                            vni3000

{{%notice info%}}

You can try this out without the bridge being VXLAN-enabled. The
configuration would look something like this:

    auto swp5.100.10
    iface swp5.100.10
        mstpctl-portbpdufilter yes
        mstpctl-bpduguard yes
     
    auto br10
    iface br10
        bridge-ports swp3.10  swp4  swp5.100.10
        bridge-vlan-aware no

{{% imgOld 2 %}}

{{%/notice%}}

## <span>Caveats and Errata</span>

### <span>EA Feature Limitations</span>

  - QinQ is available only on Broadcom Tomahawk, Trident II+ and Trident
    II switches; support for Mellanox switches will be available in a
    future release.

  - `iptables` match on double-tagged interfaces is not supported.

  - Single-tagged translation supports only [VLAN-aware bridge
    mode](/version/cumulus-linux-332/Layer_One_and_Two/Ethernet_Bridging_-_VLANs/VLAN-aware_Bridge_Mode_for_Large-scale_Layer_2_Environments)
    with the bridge’s VLAN 802.1ad protocol.

  - No layer 2 protocol (STP BPDU, LLDP) tunneling support.

  - No
    [MLAG](/version/cumulus-linux-332/Layer_One_and_Two/Multi-Chassis_Link_Aggregation_-_MLAG)
    support for double-tagged translation.

  - MLAG support for single-tagged translation should work, but has not
    been tested for this EA release.

  - Mixing 802.1Q and 802.1ad subinterfaces on the same switch port is
    not supported.

### <span>Long Interface Names</span>

The Linux kernel limits interface names to 15 characters in length. For
QinQ interfaces, this limit can be reached fairly easily.

To work around this issue, you'll need to create two VLANs as nested
VLAN raw devices, one for the outer tag and one for the inner tag. For
example, you can't create an interface called swp50s0.1001.101, since it
has 16 characters in its name. Instead, you'll create VLANs with IDs
1001 and 101 as follows by editing /etc/network/interfaces and adding a
configuration like the following:

    auto vlan1001
    iface vlan1001
           vlan-id 1001
           vlan-raw-device swp50s0
           vlan-protocol 802.1ad
     
     
    auto vlan1001-101
    iface vlan1001-101
           vlan-id 101
           vlan-raw-device vlan1001
     
     
    auto bridge101
    iface bridge101
        bridge-ports vlan1001-101 vxlan1000101

{{%notice note%}}

There isn't a way to create this configuration using
[NCLU](/version/cumulus-linux-332/System_Configuration/Network_Command_Line_Utility)
at this time.

{{%/notice%}}
