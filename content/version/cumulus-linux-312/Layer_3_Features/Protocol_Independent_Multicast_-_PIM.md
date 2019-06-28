---
title: Protocol Independent Multicast - PIM
author: Cumulus Networks
weight: 155
aliases:
 - /display/CL31/Protocol+Independent+Multicast+-+PIM
 - /pages/viewpage.action?pageId=5122116
pageID: 5122116
product: Cumulus Linux
version: 3.1.2
imgData: cumulus-linux-312
siteSlug: cumulus-linux-312
---
{{%notice warning%}}

**Early Access Feature**

PIM Sparse Mode is an [early access
feature](https://support.cumulusnetworks.com/hc/en-us/articles/202933878)
Cumulus Linux 3.1. Before you can install PIM, you must enable the Early
Access repository. For more information about the Cumulus Linux
repository, read [this knowledge base
article](https://support.cumulusnetworks.com/hc/en-us/articles/217422127).

{{%/notice%}}

Protocol Independent Multicast, or PIM, is a collection of multicast
routing protocols implemented to reduce network traffic. The two main
PIM modes are PIM Sparse Mode and PIM Dense Mode.

{{%notice note%}}

Cumulus Linux 3.1 supports PIM Sparse Mode.

{{%/notice%}}

## <span>Installing and Configuring PIM Sparse Mode</span>

PIM Sparse Mode builds explicit multicasts trees rooted at a Rendezvous
Point (RP) for each group. Each RP keeps track of all multicast sources
and receivers for a multicast group range within the PIM domain,
allowing PIM Sparse Mode configurations to scale effectively.

To install the `cumulus-pim` package, follow the instructions in the
[Cumulus Linux 3.1 release
notes](https://support.cumulusnetworks.com/hc/en-us/articles/224473608#ea).

To configure PIM on a switch:

1.  Open `/etc/quagga/daemons` in a text editor.

2.  Enable the PIM daemon and save the file:
    
        pimd=yes
    
    {{%notice note%}}
    
    As with other routing protocols, the `zebra` daemon must always be
    enabled, so set it to *yes* as well.
    
    {{%/notice%}}

3.  Run the `systemctl restart` command to restart Quagga:
    
        cumulus@switch:~$ sudo systemctl restart quagga

To enable IP Multicast on a switch:

1.  Open `/etc/cumulus/switchd.conf` in a text editor.

2.  Uncomment the `ipmulticast.enable` variable, set the value to
    `TRUE`, and save the file:
    
        ipmulticast.enable = TRUE

3.  Restart switchd to implement the changes:
    
        cumulus@switch:~$ sudo systemctl restart switchd

To enable PIM on an interface:

1.  In a terminal, run the `vtysh` command to start the Quagga CLI on
    the switch.
    
        cumulus@switch:~$ sudo vtysh
        cumulus# 

2.  Run the following command to enable multicast routing:
    
        cumulus# configure terminal
        cumulus(config)# ip multicast-routing

3.  Run the following commands to configure the PIM interfaces:
    
        cumulus# configure terminal
        cumulus(config)# int swp1
        cumulus(config-if)# ip pim sm

4.  Run the following command to enable IGMP on the interfaces with
    hosts attached:
    
        cumulus# configure terminal
        cumulus(config)# int swp1 
        cumulus(config-if)# ip igmp

5.  Run the following command to configure a group mapping for a static
    RP:
    
        cumulus# configure terminal 
        cumulus(config)# ip pim rp 192.168.0.1 224.0.0.0/4
    
    {{%notice note%}}
    
    Each PIM-SM enabled device must configure a static RP to a group
    mapping, and all PIM-SM enabled devices must have the same RP to
    group mapping configuration.
    
    {{%/notice%}}
    
    Two examples are shown below:
    
        cumulus# ip pim rp 192.168.0.1 224.0.0.0/4
        cumulus# ip pim rp 192.168.0.1 228.0.0.0/8
        cumulus# ip pim rp 192.168.0.2 229.0.0.0/8

## <span>Limitations</span>

  - Only PIM Sparse Mode is available in Cumulus Linux 3.1

  - ECMP with multicast traffic is not utilized

  - Interfaces must use IPv4 addresses. Unnumbered interfaces are not
    supported for PIM-SM

  - CLOS configuration is recommended when using PIM-SM

  - SPT switchover is not currently supported

  - Non-native forwarding (register decapsulation) is not currently
    supported
