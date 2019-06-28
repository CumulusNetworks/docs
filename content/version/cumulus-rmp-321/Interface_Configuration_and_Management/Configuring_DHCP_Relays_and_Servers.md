---
title: Configuring DHCP Relays and Servers
author: Cumulus Networks
weight: 59
aliases:
 - /display/RMP321/Configuring+DHCP+Relays+and+Servers
 - /pages/viewpage.action?pageId=5127620
pageID: 5127620
product: Cumulus RMP
version: 3.2.1
imgData: cumulus-rmp-321
siteSlug: cumulus-rmp-321
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

Another way to configure this would be to connect the host to the DHCP
relay via a layer 2 bridge instead of a switch port over layer 3:

{{% imgOld 1 %}}

{{%notice note%}}

The `dhcpd` and `dhcrelay` services are disabled by default. After you
finish configuring the DHCP relays and servers, you need to start those
services.

{{%/notice%}}

## <span>Configuring the Host Interfaces</span>

Configure the host interfaces for both IPv4 and IPv6 for DHCP by adding
the DHCP port relay to the IPv4 and IPv6 host interfaces.

{{%notice info%}}

**Example IPv4 Host Interface DHCP Configuration**

The example NCLU commands below configure the IPv4 host interface `eth1`
for DHCP:

    cumulus@switch:~$ net add interface eth1 ip address dhcp
    cumulus@switch:~$ net pending
    cumulus@switch:~$ net commit

The NCLU commands above produce the following `/etc/network/interfaces`
snippet:

    auto eth1
    iface eth1 inet dhcp

{{%/notice%}}

{{%notice info%}}

**Example IPv6 Host Interface DHCP Configuration**

The example NCLU commands below configure the IPv6 host interface `eth1`
for DHCP:

    cumulus@switch:~$ net add interface eth1 ipv6 address dhcp
    cumulus@switch:~$ net pending
    cumulus@switch:~$ net commit

The NCLU commands above produce the following `/etc/network/interfaces`
snippet:

    auto eth1
    iface eth1 inet6 dhcp

{{%/notice%}}

## <span>Configuring the DHCP Relays on Cumulus RMP Switches</span>

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
(the Cumulus Linux or Cumulus RMP switch) a number of ways, either as
layer 3 or as a layer 2 bridge.

{{%notice info%}}

**Example Layer 3 Configuration**

The following NCLU commands create a layer 3 connected client
configuration:

    cumulus@switch:~$ net add interface swp1 ip address 10.0.1.1/30
    cumulus@switch:~$ net add interface swp51 ip address 10.0.100.1/30
    cumulus@switch:~$ net pending
    cumulus@switch:~$ net commit

These commands create the following code snippet in
`/etc/network/interfaces`:

    auto swp1
    iface swp1
      address 10.0.1.1/30
     
    auto swp51
    iface swp51
      address 10.0.100.1/30

{{%/notice%}}

A layer 2 bridge can be configured in either
[VLAN-aware](/version/cumulus-rmp-321/Layer_1_and_Layer_2_Features/Ethernet_Bridging_-_VLANs/VLAN-aware_Bridge_Mode_for_Large-scale_Layer_2_Environments)
or
[traditional](/version/cumulus-rmp-321/Layer_1_and_Layer_2_Features/Ethernet_Bridging_-_VLANs/Traditional_Mode_Bridges)
mode.

{{%notice info%}}

**Example Layer 2 VLAN-aware Bridge**

The following commands create a VLAN-aware bridge:

    cumulus@switch:~$ net add interface swp1 bridge access 100
    cumulus@switch:~$ net add interface swp51 ip address 10.0.100.1/30
    cumulus@switch:~$ net add bridge bridge ports swp1
    cumulus@switch:~$ net add vlan 100 ip address 10.0.1.1/24
    cumulus@switch:~$ net pending
    cumulus@switch:~$ net commit

These commands create the following code snippet in
`/etc/network/interfaces`:

    auto swp1
    iface swp1
      bridge-access 100
     
    auto swp51
    iface swp51
      address 10.0.100.1/30
     
    auto bridge
    iface bridge
      bridge-ports swp1
      bridge-vlan-aware yes
     
    auto vlan100
    iface vlan100
      address 10.0.1.1/24

{{%/notice%}}

{{%notice info%}}

**Example Traditional Bridge Configuration**

To create a traditional bridge configuration, edit
`/etc/network/interfaces` and create a code snippet similar to the one
below:

    auto swp51
    iface swp51
      address 10.0.100.1/30
     
    auto br100
    iface br100
      address 10.0.1.1/24
      bridge-ports swp1

{{%/notice%}}

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
bridge](https://docs.cumulusnetworks.com/pages/viewpage.action?pageId=5120547)
(for example, bridge.100), or the bridge name if using traditional
bridging (for example, br100).

    cumulus@switch:~$ net add dhcp relay interface swp1
    cumulus@switch:~$ net add dhcp relay interface swp51
    cumulus@switch:~$ net add dhcp relay server 10.0.100.2
    cumulus@switch:~$ net pending
    cumulus@switch:~$ net commit

These commands create the following configuration in the
`/etc/default/isc-dhcp-relay` file:

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
Make sure to configure the variables appropriately by editing this file:

    cumulus@switch:$ cat /etc/default/isc-dhcp-relay6 
    SERVERS=" -u 2001:db8:100::2%swp51"
     
    INTF_CMD="-l swp1"

{{%notice note%}}

You cannot use NCLU to configure IPv6 relays.

{{%/notice%}}

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

{{%notice note%}}

You cannot use NCLU to configure IPv6 DHCP servers.

{{%/notice%}}

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
