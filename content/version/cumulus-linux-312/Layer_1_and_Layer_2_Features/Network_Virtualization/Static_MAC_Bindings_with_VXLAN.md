---
title: Static MAC Bindings with VXLAN
author: Cumulus Networks
weight: 291
aliases:
 - /display/CL31/Static+MAC+Bindings+with+VXLAN
 - /pages/viewpage.action?pageId=5122073
pageID: 5122073
product: Cumulus Linux
version: 3.1.2
imgData: cumulus-linux-312
siteSlug: cumulus-linux-312
---
Cumulus Linux includes native Linux VXLAN kernel support.

## <span>Requirements</span>

A VXLAN configuration requires a switch with a Tomahawk, Trident II+ or
Trident II chipset running Cumulus Linux 2.0 or later.

For a basic VXLAN configuration, you should ensure that:

  - The VXLAN has a network identifier (VNI); do not use 0 or 16777215
    as the VNI ID, as they are reserved values under Cumulus Linux.

  - The VXLAN link and local interfaces are added to bridge to create
    the association between port, VLAN and VXLAN instance.

  - Each bridge on the switch has only one VXLAN interface. Cumulus
    Linux does not support more than one VXLAN link in a bridge; however
    a switch can have multiple bridges.

{{%notice note%}}

VXLANs are not supported on switches with [Spectrum
ASICs](https://cumulusnetworks.com/hcl).

{{%/notice%}}

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

To configure the example illustrated above, edit
`/etc/network/interfaces` with a text editor like vi, nano or zile.

Add the following configuration to the `/etc/network/interfaces` file on
switch1:

    auto vtep1000
    iface vtep1000
        vxlan-id 1000
        vxlan-local-tunnelip 172.10.1.1
     
    auto br-100
    iface br-100
        bridge-ports swp1.100 swp2.100 vtep1000
        post-up bridge fdb add 0:00:10:00:00:0C dev vtep1000 dst 172.20.1.1 vni 1000 

Add the following configuration to the `/etc/network/interfaces` file on
switch2:

    auto vtep1000
    iface vtep1000
        vxlan-id 1000
        vxlan-local-tunnelip 172.20.1.1
     
    auto br-100
    iface br-100
        bridge-ports swp1.100 swp2.100 vtep1000
        post-up bridge fdb add 00:00:10:00:00:0A dev vtep1000 dst 172.10.1.1 vni 1000
        post-up bridge fdb add 00:00:10:00:00:0B dev vtep1000 dst 172.10.1.1 vni 1000

Runtime Configuration (Advanced)

{{%notice warning%}}

A runtime configuration is non-persistent, which means the configuration
you create here does not persist after you reboot the switch.

{{%/notice%}}

In general, to configure a VXLAN in Cumulus Linux without a controller,
run the following commands in a terminal connected to the switch:

1.  Create a VXLAN link:
    
        cumulus@switch1:~$ sudo ip link add <name> type vxlan id <vni> local <ip addr> [group <mcast group address>] [no] nolearning [ttl] [tos] [dev] [port MIN MAX] [ageing <value>] remote [replicator addr]
    
    {{%notice note%}}
    
    If you are specifying `ageing`, you **must** specify the replicator
    (`remote`) .
    
    {{%/notice%}}

2.  Add a VXLAN link to a bridge:
    
        cumulus@switch1:~$ sudo brctl addif br-vxlan <name>

3.  Install a static MAC binding to a remote tunnel IP:
    
        cumulus@switch1:~$ sudo bridge fdb add <mac addr> dev <device> dst <ip addr> vni <vni> port <port> via <device>

4.  Show VXLAN link and FDB:
    
        cumulus@switch1:~$ ip –d link show
        cumulus@switch1:~$ bridge fdb show

To create a runtime configuration that matches the image above, do the
following:

1.  Configure hosts A and B as part of the same tenant as C (VNI 10) on
    switch1. Hosts A and B are part of VLAN 100. To configure the VTEP
    interface with VNI 10, run the following commands in a terminal
    connected to switch1 running Cumulus Linux:
    
        cumulus@switch1:~$ sudo ip link add link swp1 name swp1.100 type vlan id 100
        cumulus@switch1:~$ sudo ip link add link swp2 name swp2.100 type vlan id 100
        cumulus@switch1:~$ sudo ip link add vtep1000 type vxlan id 10 local 172.10.1.1 nolearning
        cumulus@switch1:~$ sudo ip link set swp1 up
        cumulus@switch1:~$ sudo ip link set swp2 up
        cumulus@switch1:~$ sudo ip link set vtep1000 up

2.  Configure VLAN 100 and VTEP 1000 to be part of the same bridge
    br-100 on switch1:
    
        cumulus@switch1:~$ sudo brctl addbr br-100
        cumulus@switch1:~$ sudo ip link set br-100 up
        cumulus@switch1:~$ sudo brctl addif br-100 swp1.100 swp2.100
        cumulus@switch1:~$ sudo brctl addif br-100 vtep1000

3.  Install a static MAC binding to a remote tunnel IP, assuming the MAC
    address for host C is 00:00:10:00:00:0C:
    
        cumulus@switch1:~$ sudo bridge fdb add 00:00:10:00:00:0C dev vtep1000 dst 172.20.1.1

4.  Configure host C as part of the same tenant as hosts A and B on
    switch2:
    
        cumulus@switch2:~$ sudo ip link add link swp1 name swp1.100 type vlan id 100
        cumulus@switch2:~$ sudo ip link add name vtep1000 type vxlan id 10 local 172.20.1.1 nolearning
        cumulus@switch2:~$ sudo ip link set swp1 up
        cumulus@switch2:~$ sudo ip link set vtep1000 up

5.  Configure VLAN 100 and VTEP 1000 to be part of the same bridge
    br-100 on switch2:
    
        cumulus@switch2:~$ sudo brctl addbr br-100
        cumulus@switch2:~$ sudo ip link set br-100 up
        cumulus@switch2:~$ sudo brctl addif br-100 swp1.100
        cumulus@switch2:~$ sudo brctl addif br-100 vtep1000

6.  Install a static MAC binding to a remote tunnel IP on switch2,
    assuming the MAC address for host A is 00:00:10:00:00:0A and the MAC
    address for host B is 00:00:10:00:00:0B:
    
        cumulus@switch2:~$ sudo bridge fdb add 00:00:10:00:00:0A dev vtep1000 dst 172.10.1.1
        cumulus@switch2:~$ sudo bridge fdb add 00:00:10:00:00:0B dev vtep1000 dst 172.10.1.1

7.  Verify the configuration on switch1, then on switch2:
    
        cumulus@switch1:~$ ip –d link show
        cumulus@switch1:~$ bridge fdb show
         
        cumulus@switch2:~$ ip –d link show
        cumulus@switch2:~$ bridge fdb show

8.  Set the static `arp` for hosts B and C on host A:
    
        root@hostA:~# sudo arp –s 10.1.1.3 00:00:10:00:00:0C

9.  Set the static `arp` for hosts A and C on host B:
    
        root@hostB:~# sudo arp –s 10.1.1.3 00:00:10:00:00:0C

10. Set the static `arp` for hosts A and B on host C:
    
        root@hostC:~# arp –s 10.1.1.1 00:00:10:00:00:0A
        root@hostC:~# arp –s 10.1.1.2 00:00:10:00:00:0B

## <span>Troubleshooting VXLANs in Cumulus Linux</span>

Use the following commands to troubleshoot issues on the switch:

  - `brctl show`: Verifies the VXLAN configuration in a bridge:
    
        cumulus@switch:~$ brctl show
        bridge name     bridge id              STP enabled       interfaces
        br-vxln100      8000.44383900480d         no             swp2s0.100
                                                                 swp2s1.100
                                                                 vxln100

  - `bridge fdb show`: Displays the list of MAC addresses in an FDB:
    
        cumulus@switch1:~$ bridge fdb show
        52:54:00:ae:2a:e0 dev vxln100 dst 172.16.21.150 self permanent
        d2:ca:78:bb:7c:9b dev vxln100 permanent
        90:e2:ba:3f:ce:34 dev swp2s1.100
        90:e2:ba:3f:ce:35 dev swp2s0.100
        44:38:39:00:48:0e dev swp2s1.100 permanent
        44:38:39:00:48:0d dev swp2s0.100 permanent

  - `ip -d link show`: Displays information about the VXLAN link:
    
        cumulus@switch1:~$ ip –d link show vxln100
        71: vxln100: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue master br-vxln100 state UP 
            mode DEFAULT group default 
            link/ether d2:ca:78:bb:7c:9b brd ff:ff:ff:ff:ff:ff promiscuity 1 
            vxlan id 100 local 36.0.0.11 srcport 0 0 dstport 4789 ageing 300 
            bridge_slave state forwarding priority 32 cost 100 hairpin off guard off root_block off 
            fastleave off learning on flood on port_id 0x8001 port_no 0x1 designated_port 32769 
            designated_cost 0 designated_bridge 8000.c4:54:44:bd:1:71 designated_root 8000.c4:54:44:bd:1:71 
            hold_timer    0.00 message_age_timer    0.00 forward_delay_timer    0.00 
            topology_change_ack 0 config_pending 0 proxy_arp off proxy_arp_wifi off mcast_router 1 
            mcast_fast_leave off addrgenmode eui64
