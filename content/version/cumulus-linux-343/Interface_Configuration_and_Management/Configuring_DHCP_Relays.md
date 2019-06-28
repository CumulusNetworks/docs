---
title: Configuring DHCP Relays
author: Cumulus Networks
weight: 95
aliases:
 - /display/CL34/Configuring+DHCP+Relays
 - /pages/viewpage.action?pageId=7112627
pageID: 7112627
product: Cumulus Linux
version: 3.4.3
imgData: cumulus-linux-343
siteSlug: cumulus-linux-343
---
You can configure DHCP relays for IPv4 and IPv6.

To run DHCP for both IPv4 and IPv6, initiate the DHCP relay once for
IPv4 and once for IPv6. Following are the configurations on the server
hosts, DHCP relay and DHCP server using the following topology:

{{% imgOld 0 %}}

{{%notice warning%}}

The `dhcpd` and `dhcrelay` services are disabled by default. After you
finish configuring the DHCP relays and servers, you need to start those
services.

{{%/notice%}}

## <span>Configuring IPv4 DHCP Relays</span>

Configure `isc-dhcp-relay` using
[NCLU](/version/cumulus-linux-343/System_Configuration/Network_Command_Line_Utility_-_NCLU),
specifying the IP addresses to each DHCP server and the interfaces that
are used as the uplinks.

In the examples below, the DHCP server IP address is 172.16.1.102, VLAN
1 (the SVI is vlan1) and the uplinks are swp51 and swp52.

{{%notice warning%}}

You configure a DHCP relay on a per-VLAN basis, specifying the SVI, not
the parent bridge — in our example, you would specify v*lan1* as the SVI
for VLAN 1; do not specify the bridge named *bridge* in this case.

As per [RFC 3046](https://tools.ietf.org/html/rfc3046), you can specify
as many server IP addresses that can fit in 255 octets, specifying each
address only once.

{{%/notice%}}

    cumulus@leaf01:~$ net add dhcp relay interface swp51
    cumulus@leaf01:~$ net add dhcp relay interface swp52
    cumulus@leaf01:~$ net add dhcp relay interface vlan1
    cumulus@leaf01:~$ net add dhcp relay server 172.16.1.102
    cumulus@leaf01:~$ net pending
    cumulus@leaf01:~$ net commit

These commands create the following configuration in the
`/etc/default/isc-dhcp-relay` file:

    cumulus@leaf01:~$ cat /etc/default/isc-dhcp-relay
    SERVERS="172.16.1.102"
    INTF_CMD="-i vlan1 -i swp51 -i swp52"
    OPTIONS=""

After you've finished configuring the DHCP relay, restart then enable
the `dhcrelay` service so the configuration persists between reboots:

    cumulus@leaf01:~$ sudo systemctl restart dhcrelay.service
    cumulus@leaf01:~$ sudo systemctl enable dhcrelay.service

To see the status of the DHCP relay, use the `systemctl status
dhcrelay.service` command:

    cumulus@leaf01:~$ sudo systemctl status dhcrelay.service
    ● dhcrelay.service - DHCPv4 Relay Agent Daemon
       Loaded: loaded (/lib/systemd/system/dhcrelay.service; enabled)
       Active: active (running) since Fri 2016-12-02 17:09:10 UTC; 2min 16s ago
         Docs: man:dhcrelay(8)
     Main PID: 1997 (dhcrelay)
       CGroup: /system.slice/dhcrelay.service
               └─1997 /usr/sbin/dhcrelay --nl -d -q -i vlan1 -i swp51 -i swp52 172.16.1.102

### <span id="src-7112627_ConfiguringDHCPRelays-82" class="confluence-anchor-link"></span><span>Using DHCP Option 82</span>

DHCP relays can be configured to inject the `circuit-id` field with the
`-a` option, which you add to the `OPTIONS` line in
`/etc/default/isc-dhcp-relay`. By default, the ingress SVI interface
that the relayed DHCP discover packet is processed against is injected
into this field. You can change this behavior by adding the
`--use-pif-circuit-id` option. With this option, the physical switch
port (swp) that the discover packet arrives on is placed in the
`circuit-id` field.

## <span>Configuring IPv6 DHCP Relays</span>

If you're configuring IPv6, the `/etc/default/isc-dhcp-relay6` variables
file has a different format than the `/etc/default/isc-dhcp-relay` file
for IPv4 DHCP relays. Make sure to configure the variables appropriately
by editing this file.

{{%notice note%}}

You cannot use NCLU to configure IPv6 relays.

{{%/notice%}}

    cumulus@leaf01:$ sudo nano /etc/default/isc-dhcp-relay6 
    SERVERS=" -u 2001:db8:100::2%swp51 -u 2001:db8:100::2%swp52"
    INTF_CMD="-l vlan1"

After you've finished configuring the DHCP relay, save your changes,
restart the `dhcrelay6` service, then enable the `dhcrelay6` service so
the configuration persists between reboots:

    cumulus@leaf01:~$ sudo systemctl restart dhcrelay6.service
    cumulus@leaf01:~$ sudo systemctl enable dhcrelay6.service

To see the status of the IPv6 DHCP relay, use the `systemctl status
dhcrelay6.service` command:

    cumulus@leaf01:~$ sudo systemctl status dhcrelay6.service
    ● dhcrelay6.service - DHCPv6 Relay Agent Daemon
       Loaded: loaded (/lib/systemd/system/dhcrelay6.service; disabled)
       Active: active (running) since Fri 2016-12-02 21:00:26 UTC; 1s ago
         Docs: man:dhcrelay(8)
     Main PID: 6152 (dhcrelay)
       CGroup: /system.slice/dhcrelay6.service
               └─6152 /usr/sbin/dhcrelay -6 --nl -d -q -l vlan1 -u 2001:db8:100::2 swp51 -u 2001:db8:100::2 swp52

## <span id="src-7112627_ConfiguringDHCPRelays-multiple" class="confluence-anchor-link"></span><span>Configuring Multiple DHCP Relays</span>

Cumulus Linux supports configuring multiple DHCP relay daemons on a
switch, to enable relaying of packets from different bridges to
different upstreams.

1.  As the sudo user, open `/etc/vrf/systemd.conf` in a text editor, and
    remove `dhcrelay`.

2.  Run the following command to reload the systemd files:
    
        cumulus@switch:~$ sudo systemctl daemon-reload

3.  Create a config file in `/etc/default` using the following format
    for each dhcrelay: `isc-dhcp-relay-<dhcp-name>`. An example file can
    be seen below:
    
        # Defaults for isc-dhcp-relay initscript# sourced by /etc/init.d/isc-dhcp-relay
        # installed at /etc/default/isc-dhcp-relay by the maintainer scripts
        #
        # This is a POSIX shell fragment
        #
        # What servers should the DHCP relay forward requests to?
        SERVERS="102.0.0.2"
        # On what interfaces should the DHCP relay (dhrelay) serve DHCP requests?
        # Always include the interface towards the DHCP server.
        # This variable requires a -i for each interface configured above.
        # This will be used in the actual dhcrelay command
        # For example, "-i eth0 -i eth1"
        INTF_CMD="-i swp2s2 -i swp2s3"
        # Additional options that are passed to the DHCP relay daemon?
        OPTIONS=""

4.  Run the following command to start a dhcrelay instance, replacing
    `dhcp-name` with the instance name or number:
    
        cumulus@switch:~$ sudo systemctl start dhcrelay@<dhcp-name>

## <span>Configuring a DHCP Relay with VRR</span>

If a DHCP relay is configured and you want to enable [virtual router
redundancy
(VRR)](/version/cumulus-linux-343/Layer_One_and_Two/Virtual_Router_Redundancy_-_VRR/)
on the SVI, then you must include the VRR interface in the `INTF_CMD`
field in the `/etc/default/isc-dhcp-relay` file. For example:

    cumulus@switch:~$ net add bridge
    cumulus@switch:~$ net add vlan 500 ip address 192.0.2.252/24
    cumulus@switch:~$ net add vlan 500 ip address-virtual 00:00:5e:00:01:01 192.0.2.254/24
    cumulus@switch:~$ net add dhcp relay interface vlan500
    cumulus@switch:~$ net add dhcp relay interface vlan500-v0
    cumulus@switch:~$ net add dhcp relay server 172.16.1.102
    cumulus@switch:~$ net pending
    cumulus@switch:~$ net commit

These commands create the following configuration in the
`/etc/network/interfaces` file:

    cumulus@switch:~$ cat /etc/network/interfaces
     
     
    ...
     
    auto bridge
    iface bridge
        bridge-vids 500
        bridge-vlan-aware yes
     
     
    auto vlan500
    iface vlan500
        address 192.0.2.252/24
        address-virtual 00:00:5e:00:01:01 192.0.2.254/24
        vlan-id 500
        vlan-raw-device bridge
     
     
    auto vlan500-v0
    iface vlan500-v0

They also create the following configuration in the
`/etc/default/isc-dhcp-relay` file:

    cumulus@leaf02:mgmt-vrf:~$ cat /etc/default/isc-dhcp-relay
    # Defaults for isc-dhcp-relay initscript
    # sourced by /etc/init.d/isc-dhcp-relay
    # installed at /etc/default/isc-dhcp-relay by the maintainer scripts
    #
    # This is a POSIX shell fragment
    #
     
     
    # What servers should the DHCP relay forward requests to?
    SERVERS="172.16.1.102"
     
     
    # On what interfaces should the DHCP relay (dhrelay) serve DHCP requests?
    # Always include the interface towards the DHCP server.
    # This variable requires a -i for each interface configured above.
    # This will be used in the actual dhcrelay command
    # For example, "-i eth0 -i eth1"
    INTF_CMD="-i vlan500 -i vlan500-v0"
     
     
    # Additional options that are passed to the DHCP relay daemon?
    OPTIONS=""

## <span>Configuring the DHCP Relay Service Manually (Advanced)</span>

Configuring the DHCP service manually ...

By default, Cumulus Linux configures the DHCP relay service
automatically. However, in older versions of Cumulus Linux, you needed
to edit the `dhcrelay.service` file as described below. The IPv4
`dhcrelay.service` *Unit* script calls `/etc/default/isc-dhcp-relay` to
find launch variables.

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
    #     e.g. "-i eth0 -i swp1"
    ExecStart=/usr/sbin/dhcrelay -d -q $INTF_CMD $SERVERS $OPTIONS
     
    [Install]
    WantedBy=multi-user.target

The `/etc/default/isc-dhcp-relay` variables file needs to reference both
interfaces participating in DHCP relay (facing the server and facing the
client) and the IP address of the server. If the client-facing interface
is a bridge port, specify the switch virtual interface (SVI) name if
using a [VLAN-aware
bridge](/version/cumulus-linux-343/Layer_One_and_Two/Ethernet_Bridging_-_VLANs/VLAN-aware_Bridge_Mode_for_Large-scale_Layer_2_Environments)
(for example, vlan100), or the bridge name if using traditional bridging
(for example, br100).

## <span>Troubleshooting the DHCP Relays</span>

If you are experiencing issues with the DHCP relay, you can run the
following commands to determine whether or not the issue is with
`systemd`. The following commands manually activate the DHCP relay
process, and they do not persist when you reboot the switch:

    cumulus@switch:~$ /usr/sbin/dhcrelay -4 -i <interface_facing_host> <ip_address_dhcp_server> -i <interface_facing_dhcp_server>
    cumulus@switch:~$ /usr/sbin/dhcrelay -6 -l <interface_facing_host> -u <ip_address_dhcp_server>%<interface_facing_dhcp_server>

For example:

    cumulus@leaf01:~$ /usr/sbin/dhcrelay -4 -i vlan1 172.16.1.102 -i swp51
    cumulus@leaf01:~$ /usr/sbin/dhcrelay -6 -l vlan1 -u 2001:db8:100::2%swp51

See `man dhcrelay` for more information.

### <span>Looking at the Log on Switch where DHCP Relay Is Configured</span>

Use the `journalctl` command to look at the behavior on the Cumulus
Linux switch that is providing the DHCP relay functionality:

    cumulus@leaf01:~$ sudo journalctl -l -n 20 | grep dhcrelay
    Dec 05 20:58:55 leaf01 dhcrelay[6152]: sending upstream swp52
    Dec 05 20:58:55 leaf01 dhcrelay[6152]: sending upstream swp51
    Dec 05 20:58:55 leaf01 dhcrelay[6152]: Relaying Reply to fe80::4638:39ff:fe00:3 port 546 down.
    Dec 05 20:58:55 leaf01 dhcrelay[6152]: Relaying Reply to fe80::4638:39ff:fe00:3 port 546 down.
    Dec 05 21:03:55 leaf01 dhcrelay[6152]: Relaying Renew from fe80::4638:39ff:fe00:3 port 546 going up.
    Dec 05 21:03:55 leaf01 dhcrelay[6152]: sending upstream swp52
    Dec 05 21:03:55 leaf01 dhcrelay[6152]: sending upstream swp51
    Dec 05 21:03:55 leaf01 dhcrelay[6152]: Relaying Reply to fe80::4638:39ff:fe00:3 port 546 down.
    Dec 05 21:03:55 leaf01 dhcrelay[6152]: Relaying Reply to fe80::4638:39ff:fe00:3 port 546 down.

You can run the command `journalctl` command with the `--since` flag to
specify a time period:

    cumulus@leaf01:~$ sudo journalctl -l --since "2 minutes ago" | grep dhcrelay
    Dec 05 21:08:55 leaf01 dhcrelay[6152]: Relaying Renew from fe80::4638:39ff:fe00:3 port 546 going up.
    Dec 05 21:08:55 leaf01 dhcrelay[6152]: sending upstream swp52
    Dec 05 21:08:55 leaf01 dhcrelay[6152]: sending upstream swp51
