---
title: DHCP Servers
author: Cumulus Networks
weight: 97
aliases:
 - /display/DOCS/DHCP+Servers
 - /pages/viewpage.action?pageId=8363042
pageID: 8363042
product: Cumulus Linux
version: 3.7
imgData: cumulus-linux
siteSlug: cumulus-linux
---
To run DHCP for both IPv4 and IPv6, you need to initiate the DHCP server
twice: once for IPv4 and once for IPv6. The following configuration uses
the following topology for the host, DHCP relay and DHCP server:

{{% imgOld 0 %}}

For the configurations used in this chapter, the DHCP server is a switch
running Cumulus Linux; however, the DHCP server can also be located on a
dedicated server in your environment.

{{%notice note%}}

The `dhcpd` and `dhcrelay` services are disabled by default. After you
finish configuring the DHCP relays and servers, you need to start those
services. If you intend to run these services within a
[VRF](../../Layer-3/Virtual-Routing-and-Forwarding-VRF),
including the [management VRF](../../Layer-3/Management-VRF),
follow [these steps](../../Layer-3/Management-VRF/#run-services-within-the-management-vrf) for
configuring them. See also the [VRF chapter](../../Layer-3/Virtual-Routing-and-Forwarding-VRF/#dhcp-with-vrf).

{{%/notice%}}

## Configure the DHCP Server on Cumulus Linux Switches

You can use the following sample configurations for `dhcp.conf` and
`dhcpd6.conf` to start both an IPv4 and an IPv6 DHCP server. The
configuration files for the two DHCP server instances need to have two
pools:

  - Pool 1: Subnet overlaps interfaces

  - Pool 2: Subnet that includes the addresses

### Configure the IPv4 DHCP Server

In a text editor, edit the `dhcpd.conf` file with a configuration
similar to the following:

    cumulus@switch:~$ cat /etc/dhcp/dhcpd.conf
    ddns-update-style none;
     
    default-lease-time 600;
    max-lease-time 7200;
     
    subnet 10.0.100.0 netmask 255.255.255.0 {
    }
    subnet 10.0.1.0 netmask 255.255.255.0 {
            range 10.0.1.50 10.0.1.60;
    }

Just as you did with the DHCP relay scripts, edit the DHCP server
configuration file so it can launch the DHCP server when the system
boots. Here is a sample configuration:

    cumulus@switch:~$ cat /etc/default/isc-dhcp-server
    DHCPD_CONF="-cf /etc/dhcp/dhcpd.conf"
     
    INTERFACES="swp1"

After you finish configuring the DHCP server, enable and start the
`dhcpd` service immediately:

    cumulus@switch:~$ sudo systemctl enable dhcpd.service
    cumulus@switch:~$ sudo systemctl start dhcpd.service

### Configure the IPv6 DHCP Server

In a text editor, edit the `dhcpd6.conf` file with a configuration
similar to the following:

    cumulus@switch:~$ cat /etc/dhcp/dhcpd6.conf
    ddns-update-style none;
     
    default-lease-time 600;
    max-lease-time 7200;
     
    subnet6 2001:db8:100::/64 {
    }
    subnet6 2001:db8:1::/64 {
            range6 2001:db8:1::100 2001:db8:1::200;
    }

Just as you did with the DHCP relay scripts, edit the DHCP server
configuration file so it can launch the DHCP server when the system
boots. Here is a sample configuration:

    cumulus@switch:~$ cat /etc/default/isc-dhcp-server6
    DHCPD_CONF="-cf /etc/dhcp/dhcpd6.conf"
     
    INTERFACES="swp1"

{{%notice note%}}

You cannot use NCLU to configure IPv6 DHCP servers.

{{%/notice%}}

After you finish configuring the DHCP server, enable and start the
`dhcpd6` service immediately:

    cumulus@switch:~$ sudo systemctl enable dhcpd6.service
    cumulus@switch:~$ sudo systemctl start dhcpd6.service

## Assign Port-Based IP Addresses

You can assign an IP address and other DHCP options based on physical
location or port regardless of MAC address to clients that are attached
directly to the Cumulus Linux switch through a switch port. This is
helpful when swapping out switches and servers; you can avoid the
inconvenience of collecting the MAC address and sending it to the
network administrator to modify the DHCP server configuration.

Edit the `/etc/dhcp/dhcpd.conf` file and add the interface name `ifname`
to assign an IP address through DHCP. The following provides an example:

    host myhost {
         ifname = "swp1" ;
         fixed_address = 10.10.10.10 ;
    }

## Troubleshooting

The DHCP server knows whether a DHCP request is a relay or a non-relay
DHCP request. On isc-dhcp-server, for example, it is possible to tail
the log and look at the behavior firsthand:

    cumulus@server02:~$ sudo tail /var/log/syslog | grep dhcpd
    2016-12-05T19:03:35.379633+00:00 server02 dhcpd: Relay-forward message from 2001:db8:101::1 port 547, link address 2001:db8:101::1, peer address fe80::4638:39ff:fe00:3
    2016-12-05T19:03:35.380081+00:00 server02 dhcpd: Advertise NA: address 2001:db8:1::110 to client with duid 00:01:00:01:1f:d8:75:3a:44:38:39:00:00:03 iaid = 956301315 valid for 600 seconds
    2016-12-05T19:03:35.380470+00:00 server02 dhcpd: Sending Relay-reply to 2001:db8:101::1 port 547
