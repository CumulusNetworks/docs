---
title: DHCP Relays
author: NVIDIA
weight: 95
pageID: 8363036
---
You can configure DHCP relays for IPv4 and IPv6.

To run DHCP for both IPv4 and IPv6, initiate the DHCP relay once for
IPv4 and once for IPv6. Following are the configurations on the server
hosts, DHCP relay, and DHCP server using the following topology:

{{< img src = "/images/cumulus-linux/dhcp-relay-topology.png" >}}

{{%notice note%}}

The `dhcpd` and `dhcrelay` services are disabled by default. After you
finish configuring the DHCP relays and servers, you need to start those
services. If you intend to run these services within a
{{<link url="Virtual-Routing-and-Forwarding-VRF" text="VRF">}},
follow {{<link url=Virtual-Routing-and-Forwarding-VRF/#dhcp-with-vrf text="these steps">}} for
configuring them.

{{%/notice%}}

## Configure IPv4 DHCP Relays

Configure `isc-dhcp-relay` using {{<link url="Network-Command-Line-Utility-NCLU" text="NCLU">}},
specifying the IP addresses to each DHCP server and the interfaces that are used as the uplinks.

In the examples below, the DHCP server IP address is 172.16.1.102, VLAN 1 (the SVI is vlan1) and the uplinks are swp51 and swp52.

{{%notice warning%}}

You configure a DHCP relay on a per-VLAN basis, specifying the SVI, not
the parent bridge; in our example, you would specify v*lan1* as the SVI
for VLAN 1; do not specify the bridge named *bridge* in this case.

As per {{<exlink url="https://tools.ietf.org/html/rfc3046" text="RFC 3046">}}, you can specify
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

After you finish configuring DHCP relay, restart then enable the
`dhcrelay` service so the configuration persists between reboots:

    cumulus@leaf01:~$ sudo systemctl restart dhcrelay.service
    cumulus@leaf01:~$ sudo systemctl enable dhcrelay.service

To see the DHCP relay status, use the `systemctl status
dhcrelay.service` command:

    cumulus@leaf01:~$ sudo systemctl status dhcrelay.service
    ● dhcrelay.service - DHCPv4 Relay Agent Daemon
       Loaded: loaded (/lib/systemd/system/dhcrelay.service; enabled)
       Active: active (running) since Fri 2016-12-02 17:09:10 UTC; 2min 16s ago
         Docs: man:dhcrelay(8)
     Main PID: 1997 (dhcrelay)
       CGroup: /system.slice/dhcrelay.service
               └─1997 /usr/sbin/dhcrelay --nl -d -q -i vlan1 -i swp51 -i swp52 172.16.1.102

### DHCP Option 8

You can configure DHCP relays to inject the `circuit-id` field with the
`-a` option, which you add to the `OPTIONS` line in the
`/etc/default/isc-dhcp-relay` file. By default, the ingress SVI
interface against which the relayed DHCP discover packet is processed is
injected into this field. You can change this behavior by adding the
`--use-pif-circuit-id` option. With this option, the physical switch
port (swp) on which the discover packet arrives is placed in the
`circuit-id` field.

### Control the Gateway IP Address with RFC 3527

When DHCP relay is required in an environment that relies on an anycast
gateway (such as EVPN), a unique IP address is necessary on each device
for return traffic. By default, in a BGP unnumbered environment with
DHCP relay, the source IP address is set to the loopback IP address and
the gateway IP address (giaddr) is set as the SVI IP address. However
with anycast traffic, the SVI IP address is not unique to each rack; it
is typically shared amongst all racks. Most EVPN ToR deployments only
possess a single unique IP address, which is the loopback IP address.

{{<exlink url="https://tools.ietf.org/html/rfc3527" text="RFC 3527">}} enables the DHCP server
to react to these environments by introducing a new parameter to the
DHCP header called the *link selection sub-option*, which is built by
the DHCP relay agent. The link selection sub-option takes on the normal
role of the giaddr in relaying to the DHCP server which subnet is
correlated to the DHCP request. When using this sub-option, the giaddr
continues to be present but only relays the return IP address that is to
be used by the DHCP server; the giaddr becomes the unique loopback IP address.

When enabling RFC 3527 support, you can specify an interface, such as
the loopback interface or a switchport interface to be used as the
giaddr. The relay picks the first IP address on that interface. If the
interface has multiple IP addresses, you can specify a specific IP
address for the interface.

{{%notice note%}}

RFC 3527 is supported for IPv4 DHCP relays only.

{{%/notice%}}

The following illustration demonstrates how you can control the giaddr
with RFC 3527.

{{< img src = "/images/cumulus-linux/dhcp-relay-RFC3527.png" >}}

To enable RFC 3527 support and control the giaddr, run the `net add dhcp
relay giaddr-interface` command with interface/IP address you want to
use.

The following example uses the first IP address on the loopback
interface as the giaddr:

    cumulus@leaf01:~$ net add dhcp relay giaddr-interface lo

The above command creates the following configuration in the
`/etc/default/isc-dhcp-relay` file:

    cumulus@leaf01:~$ cat /etc/default/isc-dhcp-relay
    ...
    # Additional options that are passed to the DHCP relay daemon?
    OPTIONS="-U lo"

{{%notice note%}}

The first IP address on the loopback interface is typically the
127.0.0.1 address. Use more specific syntax, as shown in the next example.

{{%/notice%}}

The following example uses IP address 10.0.0.1 on the loopback interface
as the giaddr:

    cumulus@leaf01:~$ net add dhcp relay giaddr-interface lo 10.0.0.1

The above command creates the following configuration in the
`/etc/default/isc-dhcp-relay` file:

    cumulus@leaf01:~$ cat /etc/default/isc-dhcp-relay
    ...
    # Additional options that are passed to the DHCP relay daemon?
    OPTIONS="-U 10.0.0.1%lo"

The following example uses the first IP address on swp2 as the giaddr:

    cumulus@leaf01:~$ net add dhcp relay giaddr-interface swp2

The above command creates the following configuration in the
`/etc/default/isc-dhcp-relay` file:

    cumulus@leaf01:~$ cat /etc/default/isc-dhcp-relay
    ...
    # Additional options that are passed to the DHCP relay daemon?
    OPTIONS="-U swp2"

The following example uses IP address 10.0.0.3 on swp2 as the giaddr:

    cumulus@leaf01:~$ net add dhcp relay giaddr-interface swp2 10.0.0.3

The above command creates the following configuration in the
`/etc/default/isc-dhcp-relay` file:

    cumulus@leaf01:~$ cat /etc/default/isc-dhcp-relay
    ...
    # Additional options that are passed to the DHCP relay daemon?
    OPTIONS="-U 10.0.0.3%swp2"

{{%notice note%}}
When enabling RFC 3527 support, you can specify an interface such as the loopback interface or swp interface for the gateway address. The interface you use must be reachable in the tenant VRF that it is servicing and must be unique to the switch. In EVPN symmetric routing, fabrics running an anycast gateway that uses the same SVI IP address on multiple leaf switches, need a unique IP address for the VRF interface and must include the layer 3 VNI for this VRF in the DHCP Relay configuration.
{{%/notice%}}

## Configure IPv6 DHCP Relays

If you are configuring IPv6, the `/etc/default/isc-dhcp-relay6`
variables file has a different format than the
`/etc/default/isc-dhcp-relay` file for IPv4 DHCP relays. Make sure to
configure the variables appropriately by editing this file.

{{%notice note%}}

You cannot use NCLU to configure IPv6 relays.

{{%/notice%}}

    cumulus@leaf01:$ sudo nano /etc/default/isc-dhcp-relay6
    SERVERS=" -u 2001:db8:100::2%swp51 -u 2001:db8:100::2%swp52"
    INTF_CMD="-l vlan1"

After you finish configuring the DHCP relay, save your changes, restart
the `dhcrelay6` service, then enable the `dhcrelay6` service so the
configuration persists between reboots:

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

## Configure Multiple DHCP Relays

Cumulus Linux supports multiple DHCP relay daemons on a switch to enable
relaying of packets from different bridges to different upstreams.

To configure multiple DHCP relay daemons on a switch:

1.  Create a config file in `/etc/default` using the following format
    for each dhcrelay: `isc-dhcp-relay-<dhcp-name>`. An example file is
    shown below:

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

2.  Run the following command to start a dhcrelay instance. Replace
    `dhcp-name` with the instance name or number:

        cumulus@switch:~$ sudo systemctl start dhcrelay@<dhcp-name>

## Configure a DHCP Relay with VRR

The configuration procedure for DHCP relay with VRR is the same as
documented above. Note that DHCP relay
must run on the SVI and not on the -v0 interface.

## Configure the DHCP Relay Service Manually (Advanced)

<details>
<summary>Configuring the DHCP service manually ... </summary>

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
is a bridge port, specify the switch virtual interface (SVI) name if you
are using a {{<link url="VLAN-aware-Bridge-Mode" text="VLAN-aware bridge">}}
(for example, vlan100), or the bridge name if you are using traditional
bridging (for example, br100).
</details>

## Use the Gateway IP Address as the Source IP for Relayed DHCP Packets (Advanced)

<details>
<summary>Using the gateway IP address as the source IP for relayed DHCP
packets </summary>

You can configure the `dhcrelay` service to forward IPv4 (only) DHCP
packets to a server and ensure that the source IP address of the relayed
packet is the same as the gateway IP address. You do this by enabling
the `giaddr-src` option; when set, `dhcrelay` attempts to set the source
IP address of the packet to be the gateway IP address.

This option impacts all relayed packets globally.

To enable this feature:

    cumulus@leaf:~$ net add dhcp relay use-giaddr-as-src
    cumulus@leaf:~$ net pending
    cumulus@leaf:~$ net commit

These commands create the following configuration in the
`/etc/default/isc-dhcp-relay` file:

    cumulus@leaf01:~$ cat /etc/default/isc-dhcp-relay
    # Defaults for isc-dhcp-relay initscript
    # sourced by /etc/init.d/isc-dhcp-relay
    # installed at /etc/default/isc-dhcp-relay by the maintainer scripts

    #
    # This is a POSIX shell fragment
    #

    # What servers should the DHCP relay forward requests to?
    SERVERS=""

    # On what interfaces should the DHCP relay (dhrelay) serve DHCP requests?
    # Always include the interface towards the DHCP server.
    # This variable requires a -i for each interface configured above.
    # This will be used in the actual dhcrelay command
    # For example, "-i eth0 -i eth1"
    INTF_CMD=""

    # Additional options that are passed to the DHCP relay daemon?
    OPTIONS="--giaddr-src"
</details>

## Troubleshooting

If you are experiencing issues with the DHCP relay, run the following
commands to determine if the issue is with `systemd`. The following
commands manually activate the DHCP relay process and they do not
persist when you reboot the switch:

    cumulus@switch:~$ /usr/sbin/dhcrelay -4 -i <interface_facing_host> <ip_address_dhcp_server> -i <interface_facing_dhcp_server>
    cumulus@switch:~$ /usr/sbin/dhcrelay -6 -l <interface_facing_host> -u <ip_address_dhcp_server>%<interface_facing_dhcp_server>

For example:

    cumulus@leaf01:~$ /usr/sbin/dhcrelay -4 -i vlan1 172.16.1.102 -i swp51
    cumulus@leaf01:~$ /usr/sbin/dhcrelay -6 -l vlan1 -u 2001:db8:100::2%swp51

See `man dhcrelay` for more information.

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

You can run the `journalctl` command with the `--since` flag to specify
a time period:

    cumulus@leaf01:~$ sudo journalctl -l --since "2 minutes ago" | grep dhcrelay
    Dec 05 21:08:55 leaf01 dhcrelay[6152]: Relaying Renew from fe80::4638:39ff:fe00:3 port 546 going up.
    Dec 05 21:08:55 leaf01 dhcrelay[6152]: sending upstream swp52
    Dec 05 21:08:55 leaf01 dhcrelay[6152]: sending upstream swp51

### Configuration Errors

If you configure DHCP relays by editing the
`/etc/default/isc-dhcp-relay` file
manually instead of running NCLU commands, you might introduce
configuration errors that can cause the switch to crash.

For example, if you see an error similar to the following, there might
be a space between the DHCP server address and the interface used as the
uplink.

    Core was generated by `/usr/sbin/dhcrelay --nl -d -i vx-40 -i vlan100 10.0.0.4 -U 10.0.1.2  %vlan120'.
    Program terminated with signal SIGSEGV, Segmentation fault.

To resolve the issue, manually edit the `/etc/default/isc-dhcp-relay`
file to remove the space, then run the
`systemctl restart dhcrelay.service` command to restart the `dhcrelay`
service and apply the configuration change.

## Caveats and Errata

### Interface Names Cannot Be Longer than 14 Characters

The `dhcrelay` command does not bind to an interface if the interface's name is
longer than 14 characters. To work around this issue, change the interface name
to be 14 or fewer characters if `dhcrelay` is required to bind to it.

This is a known limitation in `dhcrelay`.
