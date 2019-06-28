---
title: Configuring DHCP Relays
author: Cumulus Networks
weight: 85
aliases:
 - /display/CL30/Configuring+DHCP+Relays
 - /pages/viewpage.action?pageId=5118376
pageID: 5118376
product: Cumulus Linux
version: '3.0'
imgData: cumulus-linux-301
siteSlug: cumulus-linux-301
---
You can configure an interface so it can make DHCP relay requests for
IPv4 and IPv6.

To run DHCP for both IPv4 and IPv6, you need to initiate the DHCP relay
and DHCP server twice: once for IPv4 using the `-4` option, and once for
IPv6 using the `-6` option. Following are the configurations on the
host, leaf and DHCP server using the following topology:

{{% imgOld 0 %}}

Contents

## <span>Configuring the Relays </span>

Here is the host configuration:

    /etc/network/interfaces
    auto eth1
    iface eth1 inet dhcp
    
    auto eth1
    iface eth1 inet6 dhcp

Here is the leaf configuration:

    cumulus@switch:~$ /usr/sbin/dhcrelay -4 -i swp1 10.0.100.2 -i swp51
    cumulus@switch:~$ /usr/sbin/dhcrelay -6 -l swp1 -u 2001:db8:100::2%swp51

You have to run two independent instances of `dhcrelay`. The `dhcrelay`
feature is part of the `isc-dhcp-relay` services. The format of this
command is below:

    cumulus@switch:~$ /usr/sbin/dhcrelay -4 -i <interface_facing_host> <ip_address_dhcp_server> -i <interface_facing_dhcp_server>
    cumulus@switch:~$ /usr/sbin/dhcrelay -6 -l <interface_facing_host> -u <ip_address_dhcp_server>%<interface_facing_dhcp_server>

See the `man dhcrelay` for more information.

The `systemd` launch scripts can be edited so that the `dhcrelay`
service starts with the switch.

The launch scripts for systemd are located in ` /lib/systemd/system  `.
Edit or create two files as described below:

    cumulus@leaf01:/lib/systemd/system$ cat dhcrelay.service 
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

    cumulus@leaf01:/lib/systemd/system$ cat /etc/default/isc-dhcp-relay 
    SERVERS="10.0.100.2"
    
    INTF_CMD="-i swp1 -i swp51"

    cumulus@leaf01:/lib/systemd/system$ cat dhcrelay6.service 
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

    cumulus@leaf01:/lib/systemd/system$ cat /etc/default/isc-dhcp-relay6 
    SERVERS=" -u 2001:db8:100::2%swp51"
    
    INTF_CMD="-l swp1"

Here is the DHCP server configuration:

    /usr/sbin/dhcpd -6 -cf /etc/dhcp/dhcpd6.conf swp1
    /usr/sbin/dhcpd -4 -cf /etc/dhcp/dhcpd.conf swp1

The configuration files for the two DHCP servers need to have two pools:

  - Pool 1: Subnet overlaps interfaces

  - Pool 2: Subnet that includes the addresses

Here are the sample configurations:

    /etc/dhcp/dhcpd.conf
    subnet 10.0.100.0 netmask 255.255.255.0 {
    }
    subnet 10.0.1.0 netmask 255.255.255.0 {
            range 10.0.1.50 10.0.1.60;
    }

    /etc/dhcp/dhcpd6.conf
    subnet6 2001:db8:100::/64 {
    }
    subnet6 2001:db8:1::/64 {
            range6 2001:db8:1::100 2001:db8:1::200;
    }

Just as you did with the DHCP relay scripts, the `systemd`
initialization scripts can be used to launch the DHCP server at start.
Here are sample configurations:

    cumulus@spine01:/lib/systemd/system$ cat dhcpd.service 
    [Unit]
    Description=DHCPv4 Server Daemon
    Documentation=man:dhcpd(8) man:dhcpd.conf(5)
    After=network-oneline.target networking.service syslog.service
    
    [Service]
    Type=simple
    EnvironmentFile=-/etc/default/isc-dhcp-server
    ExecStart=/usr/sbin/dhcpd -f -q $DHCPD_CONF $DHCPD_PID $INTERFACES $OPTIONS
    
    [Install]
    WantedBy=multi-user.target

    cumulus@spine01:/lib/systemd/system$ cat /etc/default/isc-dhcp-server
    DHCPD_CONF="-cf /etc/dhcp/dhcpd.conf"
    
    INTERFACES="swp1"

    cumulus@spine01:/lib/systemd/system$ cat /etc/dhcp/dhcpd.conf
    ddns-update-style none;
    
    default-lease-time 600;
    max-lease-time 7200;
    
    subnet 10.0.100.0 netmask 255.255.255.0 {
    }
    subnet 10.0.1.0 netmask 255.255.255.0 {
            range 10.0.1.50 10.0.1.60;
    }

    cumulus@spine01:/lib/systemd/system$ cat dhcpd6.service 
    [Unit]
    Description=DHCPv6 Server Daemon
    Documentation=man:dhcpd(8) man:dhcpd.conf(5)
    After=network-oneline.target networking.service syslog.service
    
    [Service]
    Type=simple
    EnvironmentFile=-/etc/default/isc-dhcp-server6
    ExecStart=/usr/sbin/dhcpd -f -q -6 $DHCPD_CONF $DHCPD_PID $INTERFACES $OPTIONS
    
    [Install]
    WantedBy=multi-user.target

    cumulus@spine01:/lib/systemd/system$ cat /etc/default/isc-dhcp-server6
    DHCPD_CONF="-cf /etc/dhcp/dhcpd6.conf"
    
    INTERFACES="swp1"

    cumulus@spine01:/lib/systemd/system$ cat /etc/dhcp/dhcpd6.conf
    ddns-update-style none;
    
    default-lease-time 600;
    max-lease-time 7200;
    
    subnet6 2001:db8:100::/64 {
    }
    subnet6 2001:db8:1::/64 {
            range6 2001:db8:1::100 2001:db8:1::200;
    }
