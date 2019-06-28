---
title: Filtering Learned MAC Addresses
author: Cumulus Networks
weight: 279
aliases:
 - /display/CL332/Filtering+Learned+MAC+Addresses
 - /pages/viewpage.action?pageId=5868895
pageID: 5868895
product: Cumulus Linux
version: 3.3.2
imgData: cumulus-linux-332
siteSlug: cumulus-linux-332
---
On Broadcom switches, a MAC address is learned on a bridge regardless of
whether or not a received packet is dropped by an
[ACL](/version/cumulus-linux-332/System_Configuration/Netfilter_-_ACLs/).
This is due to how the hardware learns MAC addresses and occurs before
the ACL lookup. This can be a security or resource problem as the MAC
address table has the potential to get filled with bogus MAC addresses,
so a malfunctioning host, network error, loop or malicious attack on a
shared L2 platform can create an outage for other hosts if the same MAC
address is learned on another port.

To prevent this from happening, Cumulus Linux filters frames before MAC
learning occurs. Since the MAC addresses and their port/VLAN
associations are known at configuration time, you can create static MAC
addresses, then create ingress ACLs to whitelist traffic from these MAC
addresses and drop traffic otherwise.

{{%notice note%}}

This feature is specific to switches on the Broadcom platform only; on
Mellanox Spectrum switches, the input port ACL does not have these
issues when learning MAC addresses.

{{%/notice%}}

Create a configuration similar to the following, where you associate a
port and VLAN with a given MAC address, adding each one to the bridge:

    cumulus@switch:~$ net add bridge bridge vids 100,200,300
    cumulus@switch:~$ net add bridge bridge pvid 1
    cumulus@switch:~$ net add bridge bridge ports swp1-3
    cumulus@switch:~$ net add bridge pre-up bridge fdb add 00:00:00:00:00:11 dev swp1 master static vlan 100
    cumulus@switch:~$ net add bridge pre-up bridge fdb add 00:00:00:00:00:22 dev swp2 master static vlan 200
    cumulus@switch:~$ net add bridge pre-up bridge fdb add 00:00:00:00:00:33 dev swp3 master static vlan 300
    cumulus@switch:~$ net pending
    cumulus@switch:~$ net commit

These commands create the following configuration in the
`/etc/network/interfaces` file:

    auto swp1
    iface swp1
     
    auto swp2
    iface swp2
     
    auto swp3
    iface swp3
     
    auto bridge
    iface bridge
        bridge-ports swp1 swp2 swp3
        bridge-pvid 1
        bridge-vids 100 200 300
        bridge-vlan-aware yes
        pre-up bridge fdb add 00:00:00:00:00:11 dev swp1 master static vlan 100
        pre-up bridge fdb add 00:00:00:00:00:22 dev swp2 master static vlan 200
        pre-up bridge fdb add 00:00:00:00:00:33 dev swp3 master static vlan 300

Alternately, if you need to list too many MAC addresses, you can run a
script to create the same configuration. For example, create a script
called `macs.txt` and put in the `bridge fdb add` commands for each MAC
address you need to configure:

    cumulus@switch:~$ cat /etc/networks/macs.txt
    #!/bin/bash
    bridge fdb add 00:00:00:00:00:11 dev swp1 master static vlan 100
    bridge fdb add 00:00:00:00:00:22 dev swp2 master static vlan 200
    bridge fdb add 00:00:00:00:00:33 dev swp3 master static vlan 300
    bridge fdb add 00:00:00:00:00:44 dev swp4 master static vlan 400
    bridge fdb add 00:00:00:00:00:55 dev swp5 master static vlan 500
    bridge fdb add 00:00:00:00:00:66 dev swp6 master static vlan 600
     

Then create the configuration using
[NCLU](/version/cumulus-linux-332/System_Configuration/Network_Command_Line_Utility):

    cumulus@switch:~$ net add bridge bridge vids 100,200,300
    cumulus@switch:~$ net add bridge bridge pvid 1
    cumulus@switch:~$ net add bridge bridge ports swp1-3
    cumulus@switch:~$ net add bridge pre-up /etc/networks/macs.txt
    cumulus@switch:~$ net pending
    cumulus@switch:~$ net commit

These commands create the following configuration in the
`/etc/network/interfaces` file:

    auto swp1
    iface swp1
     
    auto swp2
    iface swp2
     
    auto swp3
    iface swp3
     
    auto swp4
    iface swp4 
     
    auto swp5
    iface swp5
     
    auto swp6
    iface swp6
     
    auto bridge
    iface bridge
        bridge-ports swp1 swp2 swp3 swp4 swp5 swp6
        bridge-pvid 1
        bridge-vids 100 200 300
        bridge-vlan-aware yes
        pre-up bridge fdb add 00:00:00:00:00:11 dev swp1 master static vlan 100
        pre-up bridge fdb add 00:00:00:00:00:22 dev swp2 master static vlan 200
        pre-up bridge fdb add 00:00:00:00:00:33 dev swp3 master static vlan 300
        pre-up bridge fdb add 00:00:00:00:00:44 dev swp4 master static vlan 400
        pre-up bridge fdb add 00:00:00:00:00:55 dev swp5 master static vlan 500
        pre-up bridge fdb add 00:00:00:00:00:66 dev swp6 master static vlan 600

## <span>Interactions with EVPN</span>

If you are using
[EVPN](/version/cumulus-linux-332/Network_Virtualization/Ethernet_Virtual_Private_Network_-_EVPN),
local static MAC addresses added to the local FDB are exported as static
MAC addresses to remote switches. Remote MAC addresses are added as MAC
addresses to the remote FDB.
