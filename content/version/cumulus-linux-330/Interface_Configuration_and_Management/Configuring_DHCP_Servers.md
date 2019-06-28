---
title: Configuring DHCP Servers
author: Cumulus Networks
weight: 95
aliases:
 - /display/CL330/Configuring+DHCP+Servers
 - /pages/viewpage.action?pageId=5866406
pageID: 5866406
product: Cumulus Linux
version: 3.3.0
imgData: cumulus-linux-330
siteSlug: cumulus-linux-330
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
services.

{{%/notice%}}

## <span>Configuring DHCP Server on Cumulus Linux Switches</span>

You can use the following sample configurations for `dhcp.conf` and
`dhcpd6.conf` to start both an IPv4 and an IPv6 DHCP server. The
configuration files for the two DHCP server instances need to have two
pools:

  - Pool 1: Subnet overlaps interfaces

  - Pool 2: Subnet that includes the addresses

### <span>Configuring the IPv4 DHCP Server</span>

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

After you've finished configuring the DHCP server, enable the ` dhcpd
 `service immediately:

    cumulus@switch:~$ sudo systemctl enable dhcpd.service

### <span>Configuring the IPv6 DHCP Server</span>

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

After you've finished configuring the DHCP server, enable the`  dhcpd6
 `service immediately:

    cumulus@switch:~$ sudo systemctl enable dhcpd6.service

## <span>Troubleshooting the Log from a DHCP Server</span>

The DHCP server knows whether a DHCP request is a relay or a non-relay
DHCP request. On isc-dhcp-server, for example, it is possible to tail
the log and look at the behavior firsthand:

    cumulus@server02:~$ sudo tail /var/log/syslog | grep dhcpd
    2016-12-05T19:03:35.379633+00:00 server02 dhcpd: Relay-forward message from 2001:db8:101::1 port 547, link address 2001:db8:101::1, peer address fe80::4638:39ff:fe00:3
    2016-12-05T19:03:35.380081+00:00 server02 dhcpd: Advertise NA: address 2001:db8:1::110 to client with duid 00:01:00:01:1f:d8:75:3a:44:38:39:00:00:03 iaid = 956301315 valid for 600 seconds
    2016-12-05T19:03:35.380470+00:00 server02 dhcpd: Sending Relay-reply to 2001:db8:101::1 port 547
