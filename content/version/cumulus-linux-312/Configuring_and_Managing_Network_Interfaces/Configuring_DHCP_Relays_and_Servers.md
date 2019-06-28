---
title: Configuring DHCP Relays and Servers
author: Cumulus Networks
weight: 85
aliases:
 - /display/CL31/Configuring+DHCP+Relays+and+Servers
 - /pages/viewpage.action?pageId=5122111
pageID: 5122111
product: Cumulus Linux
version: 3.1.2
imgData: cumulus-linux-312
siteSlug: cumulus-linux-312
---
You can configure an interface so it can make DHCP relay requests for
IPv4 and IPv6.

To run DHCP for both IPv4 and IPv6, you need to initiate the DHCP relay
and DHCP server twice: once for IPv4 and once for IPv6. Following are
the configurations on the host, DHCP relay and DHCP server using the
following topology:

{{% imgOld 0 %}}

For the configurations used in this chapter, both the DHCP server and
DHCP relay are switches running Cumulus Linux; however, the DHCP server
can also be located on a dedicated server in your environment.

Another way to configure this would be to connect the host to the DHCP
relay via a layer 2 bridge instead of a switch port over layer 3:

{{% imgOld 1 %}}

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

{{%notice warning%}}

There is currently an issue where `ifupdown2` only recognizes the first
configuration, but not the second; see this [release
note](https://support.cumulusnetworks.com/hc/en-us/articles/224473608#rn445).

{{%/notice%}}

## <span>Configuring the DHCP Relays on Cumulus Linux Switches</span>

Configure the IPv4 and IPv6 DHCP relays on each leaf switch. You need to
run two independent instances of `dhcrelay`, one for IPv4 and one for
IPv6. The `dhcrelay` feature is part of the `isc-dhcp-relay` services.

Edit the `systemd` launch scripts so that the `dhcrelay` service starts
with the switch. The launch scripts for `systemd` are located in
`/lib/systemd/system`.

{{%notice warning%}}

If your launch script also starts, restarts or reloads any `systemd`
service, including `dhcrelay.service`, you must use the `--no-block`
option with the `systemctl` command. Otherwise, that service or even the
switch itself may hang after starting or restarting.

{{%/notice%}}

### <span>Configuring the DHCP Relay Interfaces</span>

As described above, you can configure the interfaces on the DHCP relay
(the Cumulus Linux switch) a number of ways, either as layer 3 or as a
layer 2 bridge.

Here's the layer 3 connected client configuration:

    auto swp1
    iface swp1
      address 10.0.1.1/30
     
    auto swp51
    iface swp51
      address 10.0.100.1/30

If you prefer to use a layer 2 bridge, you can configure it in either
[VLAN-aware](/version/cumulus-linux-312/Layer_1_and_Layer_2_Features/Ethernet_Bridging_-_VLANs/VLAN-aware_Bridge_Mode_for_Large-scale_Layer_2_Environments)
or
[traditional](/version/cumulus-linux-312/Layer_1_and_Layer_2_Features/Ethernet_Bridging_-_VLANs/)
mode. Here is the configuration for the VLAN-aware bridge:

    auto swp1
    iface swp1
      bridge-access 100
     
    auto swp51
    iface swp51
      address 10.0.100.1/30
     
    auto bridge
    iface bridge
      bridge-vlan-aware yes
      bridge-ports swp1
     
    auto bridge.100
    iface bridge.100
      address 10.0.1.1/24

And here's the configuration for the bridge in traditional mode:

    auto swp51
    iface swp51
      address 10.0.100.1/30
     
    auto br100
    iface br100
      address 10.0.1.1/24
      bridge-ports swp1
      bridge-stp yes

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
client) and the IP address of the server. If the client-facing interface
is a bridge port, specify the switch virtual interface (SVI) name if
using a [VLAN-aware
bridge](/version/cumulus-linux-312/Layer_1_and_Layer_2_Features/Ethernet_Bridging_-_VLANs/VLAN-aware_Bridge_Mode_for_Large-scale_Layer_2_Environments)
(for example, bridge.100), or the bridge name if using traditional
bridging (for example, br100).

    cumulus@switch:~$ cat /etc/default/isc-dhcp-relay
    SERVERS="10.0.100.2"
     
    INTF_CMD="-i bridge.100 -i swp51"
     
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
     
    INTF_CMD="-l bridge.100"

After you've finished configuring the DHCP relay, enable the `dhcrelay6`
service so the configuration persists between reloads:

    cumulus@switch:~$ sudo systemctl enable dhcrelay6.service

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
     
    INTERFACES="bridge.100"

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

    cumulus@switch:~$ /usr/sbin/dhcrelay -4 -i bridge.100 10.0.100.2 -i swp51
    cumulus@switch:~$ /usr/sbin/dhcrelay -6 -l bridge.100 -u 2001:db8:100::2%swp51

See the `man dhcrelay` for more information.
