---
title: Configuring DHCP Relays and Servers
author: Cumulus Networks
weight: 57
aliases:
 - /display/RMP31/Configuring+DHCP+Relays+and+Servers
 - /pages/viewpage.action?pageId=5122798
pageID: 5122798
product: Cumulus RMP
version: 3.1.2
imgData: cumulus-rmp-312
siteSlug: cumulus-rmp-312
---
You can configure an interface so it can make DHCP relay requests for
IPv4 and IPv6.

To run DHCP for both IPv4 and IPv6, you need to initiate the DHCP relay
and DHCP server twice: once for IPv4 and once for IPv6. Following are
the configurations on the host, DHCP relay and DHCP server using the
following topology:

{{% imgOld 0 %}}

For the configurations used in this chapter, both the DHCP server and
DHCP relay are switches running Cumulus RMP; however, the DHCP server
can also be located on a dedicated switch in your environment.

{{%notice note%}}

The `dhcpd` and `dhcrelay` services are disabled by default. After you
finish configuring the DHCP relays and servers, you need to start those
services.

{{%/notice%}}

## <span>Configuring the Host Interfaces</span>

You need to configure the host interfaces for DHCP for both IPv4 and
IPv6. On each host, edit `/etc/network/interfaces` and add the following
for the DHCP relay port on the server:

    auto eth1
    iface eth1 inet dhcp
     
    auto eth1
    iface eth1 inet6 dhcp

## <span>Configuring the DHCP Relays on Cumulus RMP Switches</span>

Configure the IPv4 and IPv6 DHCP relays on each leaf switch. You need to
run two independent instances of `dhcrelay`, one for IPv4 and one for
IPv6. The `dhcrelay` feature is part of the `isc-dhcp-relay` services.

Edit the `systemd` launch scripts so that the `dhcrelay` service starts
with the switch. The launch scripts for `systemd` are located in
`/lib/systemd/system`.

### <span>Configuring IPv4 DHCP Relays</span>

Edit `dhcrelay.service`, as described below. The IPv4 `dhcrelay.service`
*Unit* script calls `/etc/default/isc-dhcp-relay` to find launch
variables.

    cumulus@switch:~$ cat /lib/systemd/system/dhcrelay.service 
    [Unit]
    Description=DHCPv4 Relay Agent Daemon
    Documentation=man:dhcrelay(8)
    After=network-oneline.target networking.service syslog.service
     
    [Service]
    Type=simple
    EnvironmentFile=-/etc/default/isc-dhcp-relay
    # Here, we are expecting the INTF_CMD to contain
    # the -i for each interface specified,
    ExecStart=/usr/sbin/dhcrelay -d -q $INTF_CMD $SERVERS $OPTIONS
     
    [Install]
    WantedBy=multi-user.target

The `/etc/default/isc-dhcp-relay` variables file needs to reference both
interfaces participating in DHCP relay (facing the server and facing the
client) and the IP address of the server.

    cumulus@switch:~$ cat /etc/default/isc-dhcp-relay
    SERVERS="10.0.100.2"
     
    INTF_CMD="-i swp1 -i swp51"
     
    OPTIONS=""

After you've finished configuring the DHCP relay, enable the `dhcrelay`
service so the configuration persists between reloads:

    cumulus@switch:~$ sudo systemctl enable dhcrelay.service

### <span>Configuring IPv6 DHCP Relays</span>

If you're configuring IPv6, you need to create the `dhcrelay6.service`
file and populate its content, as described below. The
`dhcrelay6.service` *Unit* script calls `/etc/default/isc-dhcp-relay6`
to find launch variables.

    cumulus@switch:~$ cat /lib/systemd/system/dhcrelay6.service 
    [Unit]
    Description=DHCPv6 Relay Agent Daemon
    Documentation=man:dhcrelay(8)
    After=network-oneline.target networking.service syslog.service
     
    [Service]
    Type=simple
    EnvironmentFile=-/etc/default/isc-dhcp-relay6
    ExecStart=/usr/sbin/dhcrelay -6 -d -q $INTF_CMD $SERVERS $OPTIONS
     
    [Install]
    WantedBy=multi-user.target

The `/etc/default/isc-dhcp-relay6` variables file has a different format
than the `/etc/default/isc-dhcp-relay` file used for IPv4 DHCP relays.
Make sure to configure the variables appropriately:

    cumulus@switch:$ cat /etc/default/isc-dhcp-relay6 
    SERVERS=" -u 2001:db8:100::2%swp51"
     
    INTF_CMD="-l swp1"

After you've finished configuring the DHCP relay, enable the `dhcrelay6`
service so the configuration persists between reloads:

    cumulus@switch:~$ sudo systemctl enable dhcrelay6.service

## <span>Configuring DHCP Server on Cumulus RMP Switches</span>

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

After you've finished configuring the DHCP server, enable the`  dhcpd6
 `service immediately:

    cumulus@switch:~$ sudo systemctl enable dhcpd6.service

## <span>Troubleshooting the DHCP Relays</span>

If you are experiencing issues with the DHCP relay, you can run the
following commands to determine whether or not the issue is with
`systemd`. The following commands manually activate the DHCP relay
process, and they do not persist when you reboot the switch:

    cumulus@switch:~$ /usr/sbin/dhcrelay -4 -i <interface_facing_host> <ip_address_dhcp_server> -i <interface_facing_dhcp_server>
    cumulus@switch:~$ /usr/sbin/dhcrelay -6 -l <interface_facing_host> -u <ip_address_dhcp_server>%<interface_facing_dhcp_server>

For example:

    cumulus@switch:~$ /usr/sbin/dhcrelay -4 -i swp1 10.0.100.2 -i swp51
    cumulus@switch:~$ /usr/sbin/dhcrelay -6 -l swp1 -u 2001:db8:100::2%swp51

See the `man dhcrelay` for more information.
