---
title: Static MAC Bindings with VXLAN
author: Cumulus Networks
weight: 383
aliases:
 - /display/CL36/Static+MAC+Bindings+with+VXLAN
 - /pages/viewpage.action?pageId=8362282
pageID: 8362282
product: Cumulus Linux
version: '3.6'
imgData: cumulus-linux-36
siteSlug: cumulus-linux-36
---
Cumulus Linux includes native Linux VXLAN kernel support.

## <span>Requirements</span>

A VXLAN configuration requires a Broadcom switch with the Tomahawk,
Trident II+, or Trident II ASIC running Cumulus Linux 2.0 or later, or a
Mellanox switch with the Spectrum ASIC running Cumulus Linux 3.2.0 or
later.

For a basic VXLAN configuration, make sure that:

  - The VXLAN has a network identifier (VNI); do not use 0 or 16777215
    as the VNI ID, which are reserved values under Cumulus Linux.

  - The VXLAN link and local interfaces are added to bridge to create
    the association between port, VLAN, and VXLAN instance.

## <span>Example VXLAN Configuration</span>

Consider the following example:

{{% imgOld 0 %}}

{{%notice warning%}}

Preconfiguring remote MAC addresses does not scale. A better solution is
to use the Cumulus Networks [Lightweight Network
Virtualization](https://docs.cumulusnetworks.com/pages/viewpage.action?pageId=2722663)
feature, or a controller-based option like [Midokura MidoNet and
OpenStack](https://docs.cumulusnetworks.com/pages/viewpage.action?pageId=2722662)
or [VMware
NSX](https://docs.cumulusnetworks.com/pages/viewpage.action?pageId=2722660).

{{%/notice%}}

## <span>Configuring the Static MAC Bindings VXLAN</span>

To configure the example illustrated above, first create the following
configuration on switch1:

    cumulus@switch1:~$ net add loopback lo ip address 172.10.1.1
    cumulus@switch1:~$ net add loopback lo vxrd-src-ip 172.10.1.1
    cumulus@switch1:~$ net add bridge bridge ports swp1-2
    cumulus@switch1:~$ net add bridge post-up bridge fdb add 0:00:10:00:00:0C dev vtep1000 dst 172.20.1.1 vni 1000
    cumulus@switch1:~$ net add vxlan vtep1000 vxlan id 1000 
    cumulus@switch1:~$ net add vxlan vtep1000 vxlan local-tunnelip 172.10.1.1
    cumulus@switch1:~$ net add vxlan vtep1000 bridge access 10
    cumulus@switch1:~$ net pending 
    cumulus@switch1:~$ net commit 

These commands create the following configuration in the
`/etc/network/interfaces` file:

    auto vtep1000
    iface vtep1000
        vxlan-id 1000
        vxlan-local-tunnelip 172.10.1.1
     
    auto bridge
    iface bridge
        bridge-ports swp1 swp2 vtep1000
        bridge-vids 10
        bridge-vlan-aware yes
        post-up bridge fdb add 0:00:10:00:00:0C dev vtep1000 dst 172.20.1.1 vni 1000 

Then create the following configuration on switch2:

    cumulus@switch2:~$ net add loopback lo ip address 172.20.1.1
    cumulus@switch2:~$ net add loopback lo vxrd-src-ip 172.20.1.1
    cumulus@switch1:~$ net add bridge bridge ports swp1-2
    cumulus@switch2:~$ net add bridge post-up bridge fdb add 00:00:10:00:00:0A dev vtep1000 dst 172.10.1.1 vni 1000
    cumulus@switch2:~$ net add bridge post-up bridge fdb add 00:00:10:00:00:0B dev vtep1000 dst 172.10.1.1 vni 1000
    cumulus@switch2:~$ net add vxlan vtep1000 vxlan id 1000 
    cumulus@switch2:~$ net add vxlan vtep1000 vxlan local-tunnelip 172.10.1.1
    cumulus@switch2:~$ net add vxlan vtep1000 bridge access 10
    cumulus@switch2:~$ net pending 
    cumulus@switch2:~$ net commit

These commands create the following configuration in the
`/etc/network/interfaces` file:

    auto vtep1000
    iface vtep1000
        vxlan-id 1000
        vxlan-local-tunnelip 172.20.1.1
     
    auto bridge
    iface bridge
        bridge-ports swp1 swp2 vtep1000
        bridge-vlan-aware yes
        post-up bridge fdb add 00:00:10:00:00:0A dev vtep1000 dst 172.10.1.1 vni 1000
        post-up bridge fdb add 00:00:10:00:00:0B dev vtep1000 dst 172.10.1.1 vni 1000

## <span>Troubleshooting VXLANs in Cumulus Linux</span>

Use the following commands to troubleshoot issues on the switch:

  - `brctl show` verifies the VXLAN configuration in a bridge:
    
        cumulus@switch:~$ brctl show
        bridge name bridge id           STP enabled   interfaces
        bridge      8000.2a179a8cc471   yes           swp1
                                                      swp2
                                                      vni-10
                                                      vni-2000

  - `bridge fdb show` displays the list of MAC addresses in an FDB:
    
        cumulus@switch1:~$ bridge fdb show
        44:38:39:00:00:18 dev swp1 master bridge permanent
        44:38:39:00:00:1c dev swp2 master bridge permanent
        2a:17:9a:8c:c4:71 dev vni-2000 master bridge permanent
        9a:e8:ef:a1:9d:6f dev vni-10 master bridge permanent
        00:00:10:00:00:0c dev vni-10 dst 172.20.1.1 self permanent

  - `ip -d link show` displays information about the VXLAN link:
    
        cumulus@switch1:~$ ip –d link show vni-10
        15: vni-10: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue master bridge state UNKNOWN mode DEFAULT group default 
            link/ether 9a:e8:ef:a1:9d:6f brd ff:ff:ff:ff:ff:ff promiscuity 1 
            vxlan id 10 remote 10.2.1.3 local 10.2.1.1 srcport 0 0 dstport 4789 ageing 1800 
            bridge_slave state forwarding priority 8 cost 100 hairpin off guard off root_block off fastleave off learning on flood on port_id 0x8004 port_no 0x4 designated_port 32772 designated_cost 0 designated_bridge 8000.2a:17:9a:8c:c4:71 designated_root 8000.2a:17:9a:8c:c4:71 hold_timer    0.00 message_age_timer    0.00 forward_delay_timer    0.00 topology_change_ack 0 config_pending 0 proxy_arp off proxy_arp_wifi off mcast_router 1 mcast_fast_leave off mcast_flood on addrgenmode eui64
