---
title: DHCP Servers
author: NVIDIA
weight: 350
toc: 3
---
A DHCP Server automatically provides and assigns IP addresses and other network parameters to client devices. It relies on the Dynamic Host Configuration Protocol to respond to broadcast requests from clients.

This topic describes how to configure a DHCP server for IPv4 and IPv6. Configurations on the hosts, DHCP relay and DHCP server are provided using the following topology. The DHCP server is a switch running Cumulus Linux; however, the DHCP server can also be located on a dedicated server in your environment.

{{< img src = "/images/cumulus-linux/dhcp-server-swp.png" >}}

{{%notice note%}}

The `dhcpd` and `dhcrelay` services are disabled by default. After you finish configuring the DHCP relays and servers, you need to start those services. If you intend to run these services within a {{<link url="Virtual-Routing-and-Forwarding-VRF" text="VRF">}}, including the {{<link url="Management-VRF" text="management VRF">}}, follow {{<link url="Management-VRF/#run-services-within-the-management-vrf" text="these steps">}}.

{{%/notice%}}

For information about DHCP relays, refer to {{<link title="DHCP Relays">}}.

## Configure the DHCP Server on Cumulus Linux Switches

To configure the DHCP server on a Cumulus Linux switch for IPv4 and IPv6, you need to edit the `/etc/dhcp/dhcp.conf` and `/etc/dhcp/dhcpd6.conf` configuration files. Sample configurations are provided as a starting point.

You must include two pools in the DHCP configuration files:

- Pool 1 is the subnet that includes the IP addresses of the interfaces on the DHCP server
- Pool 2 is the subnet that includes the IP addresses being assigned

### Configure the IPv4 DHCP Server

In a text editor, edit the `/etc/dhcp/dhcpd.conf` file. Use following configuration as an example:

```

cumulus@switch:~$ cat /etc/dhcp/dhcpd.conf
ddns-update-style none;

default-lease-time 600;
max-lease-time 7200;

subnet 10.0.100.0 netmask 255.255.255.0 {
}
subnet 10.0.1.0 netmask 255.255.255.0 {
      range 10.0.1.50 10.0.1.60;
}
```

Edit the `/etc/default/isc-dhcp-server` configuration file so that the DHCP server launches when the system boots. Here is an example configuration:

```
cumulus@switch:~$ cat /etc/default/isc-dhcp-server
DHCPD_CONF="-cf /etc/dhcp/dhcpd.conf"

INTERFACES="swp1"
```

Enable and start the `dhcpd` service:

```
cumulus@switch:~$ sudo systemctl enable dhcpd.service
cumulus@switch:~$ sudo systemctl start dhcpd.service
```

### Configure the IPv6 DHCP Server

In a text editor, edit the `/etc/dhcp/dhcpd6.conf` file. Use following configuration as an example:

```
cumulus@switch:~$ cat /etc/dhcp/dhcpd6.conf
ddns-update-style none;

default-lease-time 600;
max-lease-time 7200;

subnet6 2001:db8:100::/64 {
}
subnet6 2001:db8:1::/64 {
    range6 2001:db8:1::100 2001:db8:1::200;
}
```

Edit the `/etc/default/isc-dhcp-server6` file so that the DHCP server launches when the system boots. Here is an example configuration:

```
cumulus@switch:~$ cat /etc/default/isc-dhcp-server6
DHCPD_CONF="-cf /etc/dhcp/dhcpd6.conf"

INTERFACES="swp1"
```

Enable and start the `dhcpd6` service:

```
cumulus@switch:~$ sudo systemctl enable dhcpd6.service
cumulus@switch:~$ sudo systemctl start dhcpd6.service
```

## Assign Port-Based IP Addresses

You can assign an IP address and other DHCP options based on physical location or port regardless of MAC address to clients that are attached directly to the Cumulus Linux switch through a switch port. This is helpful when swapping out switches and servers; you can avoid the inconvenience of collecting the MAC address and sending it to the network administrator to modify the DHCP server configuration.

Edit the `/etc/dhcp/dhcpd.conf` file and add the interface name `ifname` to assign an IP address through DHCP. The following provides an example:

```
host myhost {
    ifname "swp1" ;
    fixed-address 10.10.10.10 ;
}
```

## Troubleshooting

The DHCP server determines if a DHCP request is a relay or a non-relay DHCP request. You can run the following command to see the DHCP request:

```
cumulus@server02:~$ sudo tail /var/log/syslog | grep dhcpd
2016-12-05T19:03:35.379633+00:00 server02 dhcpd: Relay-forward message from 2001:db8:101::1 port 547, link address 2001:db8:101::1, peer address fe80::4638:39ff:fe00:3
2016-12-05T19:03:35.380081+00:00 server02 dhcpd: Advertise NA: address 2001:db8:1::110 to client with duid 00:01:00:01:1f:d8:75:3a:44:38:39:00:00:03 iaid = 956301315 valid for 600 seconds
2016-12-05T19:03:35.380470+00:00 server02 dhcpd: Sending Relay-reply to 2001:db8:101::1 port 547
```
