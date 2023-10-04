---
title: DHCP Relays
author: NVIDIA
weight: 340
toc: 3
---
DHCP is a client/server protocol that automatically provides IP hosts with IP addresses and other related  configuration information. A DHCP relay (agent) is a host that forwards DHCP packets between clients and servers. DHCP relays forward requests and replies between clients and servers that are not on the same physical subnet.

This topic describes how to configure DHCP relays for IPv4 and IPv6. Configurations on the server hosts, DHCP relays, and DHCP server are provided using the following topology:

{{< img src = "/images/cumulus-linux/dhcp-relay-topology.png" >}}

{{%notice note%}}

The `dhcpd` and `dhcrelay` services are disabled by default. After you finish configuring the DHCP relays and servers, you need to start those services. If you intend to run these services within a {{<link url="Virtual-Routing-and-Forwarding-VRF" text="VRF">}}, follow {{<link url="Virtual-Routing-and-Forwarding-VRF/#dhcp-with-vrf" text="these steps">}}.

{{%/notice%}}

## Configure IPv4 DHCP Relays

To configure IPv4 DHCP relays, run the following commands.

{{< tabs "TabID25 ">}}

{{< tab "NCLU Commands ">}}

{{%notice warning%}}

You configure a DHCP relay on a per-VLAN basis, specifying the SVI, not the parent bridge. In the example below, you specify v*lan1* as the SVI for VLAN 1 but you do not specify the bridge named *bridge* in this case.

{{%/notice%}}

Specify the IP address of each DHCP server and the interfaces that are used as the uplinks. In the example commands below, the DHCP server IP address is 172.16.1.102, VLAN 1 (the SVI is vlan1) and the uplinks are swp51 and swp52. As per {{<exlink url="https://tools.ietf.org/html/rfc3046" text="RFC 3046">}}, you can specify as many server IP addresses that can fit in 255 octets. You can specify each address only once.

```
cumulus@switch:~$ net add dhcp relay interface swp51
cumulus@switch:~$ net add dhcp relay interface swp52
cumulus@switch:~$ net add dhcp relay interface vlan1
cumulus@switch:~$ net add dhcp relay server 172.16.1.102
cumulus@switch:~$ net pending
cumulus@switch:~$ net commit
```

These commands create the following configuration in the `/etc/default/isc-dhcp-relay` file:

```
SERVERS="172.16.1.102"
INTF_CMD="-i vlan1 -i swp51 -i swp52"
OPTIONS=""
```

Enable, then restart the `dhcrelay` service so the configuration persists between reboots:

```
cumulus@switch:~$ sudo systemctl enable dhcrelay.service
cumulus@switch:~$ sudo systemctl restart dhcrelay.service
```

{{< /tab >}}

{{< tab "Linux Commands ">}}

1. Edit the `/etc/default/isc-dhcp-relay` file to add the IP address of the DHCP server and both interfaces participating in DHCP relay (facing the server and facing the client). In the example below, the DHCP server IP address is 172.16.1.102, VLAN 1 (the SVI is vlan1) and the uplinks are swp51 and swp52. If the client-facing interface is a bridge port, specify the switch virtual interface (SVI) name if using a {{<link url="VLAN-aware-Bridge-Mode" text="VLAN-aware bridge">}} (for example, bridge.100), or the bridge name if using traditional bridging (for example, br100).

   ```
   cumulus@switch:~$ sudo nano /etc/default/isc-dhcp-relay
   SERVERS="172.16.1.102"
   INTF_CMD="-i vlan1 -i swp51 -i swp52"
   OPTIONS=""
   ```

2. Enable then restart the `dhcrelay` service so that the configuration persists between reboots:

   ```
   cumulus@switch:~$ sudo systemctl enable dhcrelay.service
   cumulus@switch:~$ sudo systemctl restart dhcrelay.service
   ```

{{< /tab >}}

{{< /tabs >}}

To see the DHCP relay status, use the `systemctl status dhcrelay.service` command:

```
cumulus@switch:~$ sudo systemctl status dhcrelay.service
● dhcrelay.service - DHCPv4 Relay Agent Daemon
    Loaded: loaded (/lib/systemd/system/dhcrelay.service; enabled)
    Active: active (running) since Fri 2016-12-02 17:09:10 UTC; 2min 16s ago
      Docs: man:dhcrelay(8)
Main PID: 1997 (dhcrelay)
    CGroup: /system.slice/dhcrelay.service
            └─1997 /usr/sbin/dhcrelay --nl -d -q -i vlan1 -i swp51 -i swp52 172.16.1.102
```

### DHCP Agent Information Option (Option 82)

Cumulus Linux supports DHCP Agent Information Option 82, which allows a DHCP relay to insert circuit or relay specific information into a request that is being forwarded to a DHCP server. Two sub-options are provided:

- The Circuit ID sub-option includes information about the circuit on which the request comes in, such as the SVI or physical port.
- The Remote ID sub-option includes information that identifies the relay agent, such as the MAC address.

To enable the DHCP Agent Information Option, you configure the `-a` option. By default, when you enable this option, the Circuit ID is the printable name of the interface on which the client request is received, typically an SVI. The Remote ID is the System MAC of the device on which DHCP relay is running.

{{%notice note%}}

NCLU commands are not currently available for this feature. Use the following Linux commands.

{{%/notice%}}

- To configure the DHCP relay to inject the ingress *SVI interface* against which the relayed DHCP discover packet is processed, edit `/etc/default/isc-dhcp-relay` file and add `-a` to the `OPTIONS` line. For example:

   ```
   cumulus@switch:~$ sudo nano /etc/default/isc-dhcp-relay
   ...
   # Additional options that are passed to the DHCP relay daemon?
   OPTIONS="-a"
   ```

- To configure the DHCP relay to inject the *physical switch port* on which the relayed DHCP discover packet arrives instead of the SVI, edit the `/etc/default/isc-dhcp-relay` file and add `-a --use-pif-circuit-id` to the `OPTIONS` line. For example:

   ```
   cumulus@switch:~$ sudo nano /etc/default/isc-dhcp-relay
   ...
   # Additional options that are passed to the DHCP relay daemon?
   OPTIONS="-a --use-pif-circuit-id"
   ```

- To customize the Remote ID sub-option, edit `/etc/default/isc-dhcp-relay` file and add `-a -r` to the `OPTIONS` line followed by a custom string (up to 255 characters that is used for the Remote ID. For example:

   ```
   cumulus@switch:~$ sudo nano /etc/default/isc-dhcp-relay
   ...
   # Additional options that are passed to the DHCP relay daemon?
   OPTIONS="-a -r CUSTOMVALUE"
   ```

Make sure to restart the `dhcrelay` service to apply the new configuration :

```
cumulus@switch:~$ sudo systemctl restart dhcrelay.service
```

### Control the Gateway IP Address with RFC 3527

When DHCP relay is required in an environment that relies on an anycast gateway (such as EVPN), a unique IP address is necessary on each device for return traffic. By default, in a BGP unnumbered environment with DHCP relay, the source IP address is set to the loopback IP address and the gateway IP address (giaddr) is set as the SVI IP address. However with anycast traffic, the SVI IP address is not unique to each rack; it is typically shared amongst all racks. Most EVPN ToR deployments only possess a single unique IP address, which is the loopback IP address.

{{<exlink url="https://tools.ietf.org/html/rfc3527" text="RFC 3527">}} enables the DHCP server to react to these environments by introducing a new parameter to the DHCP header called the link selection sub-option, which is built by the DHCP relay agent. The link selection sub-option takes on the normal role of the giaddr in relaying to the DHCP server which subnet is correlated to the DHCP request. When using this sub-option, the giaddr continues to be present but only relays the return IP address that is to be used by the DHCP server; the giaddr becomes the unique loopback IP address.

When enabling RFC 3527 support, you can specify an interface, such as the loopback interface or a switch port interface to be used as the giaddr. The relay picks the first IP address on that interface. If the interface has multiple IP addresses, you can specify a specific IP address for the interface.

{{%notice note%}}

RFC 3527 is supported for IPv4 DHCP relays only.

{{%/notice%}}

The following illustration demonstrates how you can control the giaddr with RFC 3527.

{{< img src = "/images/cumulus-linux/dhcp-relay-RFC3527.png" >}}

To enable RFC 3527 support and control the giaddr, run the following commands.

{{< tabs "TabID166 ">}}

{{< tab "NCLU Commands ">}}

1. Run the `net add dhcp relay giaddr-interface` command with the interface/IP address you want to use. The  following example uses the first IP address on the loopback interface as the giaddr:

   ```
   cumulus@switch:~$ net add dhcp relay giaddr-interface lo
   ```

   The above command creates the following configuration in the `/etc/default/isc-dhcp-relay` file:

   ```
   # Additional options that are passed to the DHCP relay daemon?
   OPTIONS="-U lo"
   ```

   The first IP address on the loopback interface is typically the 127.0.0.1 address; Use more specific syntax, as shown in the next example.

   The following example uses IP address 10.0.0.1 on the loopback interface as the giaddr:

   ```
   cumulus@switch:~$ net add dhcp relay giaddr-interface lo 10.0.0.1
   ```

   The above command creates the following configuration in the `/etc/default/isc-dhcp-relay` file:

   ```
   # Additional options that are passed to the DHCP relay daemon?
   OPTIONS="-U 10.0.0.1%lo"
   ```

   The following example uses the first IP address on swp2 as the giaddr:

   ```
   cumulus@switch:~$ net add dhcp relay giaddr-interface swp2
   ```

   The above command creates the following configuration in the `/etc/default/isc-dhcp-relay` file:

   ```
   # Additional options that are passed to the DHCP relay daemon?
   OPTIONS="-U swp2"
   ```

   The following example uses IP address 10.0.0.3 on swp2 as the giaddr:

   ```
   cumulus@switch:~$ net add dhcp relay giaddr-interface swp2 10.0.0.3
   ```

   The above command creates the following configuration in the `/etc/default/isc-dhcp-relay` file:

   ```
   # Additional options that are passed to the DHCP relay daemon?
   OPTIONS="-U 10.0.0.3%swp2"
   ```

2. Restart the `dhcrelay` service to apply the configuration change:

   ```
   cumulus@switch:~$ sudo systemctl restart dhcrelay.service
   ```

{{< /tab >}}

{{< tab "Linux Commands ">}}

1. Edit the `/etc/default/isc-dhcp-relay` file and provide the `-U` option with the interface or IP address you want to use as the giaddr. The following example uses the first IP address on the loopback interface as the giaddr:

   ```
   cumulus@switch:~$ sudo nano /etc/default/isc-dhcp-relay
   ...
   # Additional options that are passed to the DHCP relay daemon?
   OPTIONS="-U lo"
   ```

   The first IP address on the loopback interface is typically the 127.0.0.1 address. Use more specific syntax, as shown in the next example.

   The following example uses IP address 10.0.0.1 on the loopback interface as the giaddr:

   ```
   cumulus@switch:~$ sudo nano /etc/default/isc-dhcp-relay
   ...
   # Additional options that are passed to the DHCP relay daemon?
   OPTIONS="-U 10.0.0.1%lo"
   ```

   The following example uses the first IP address on swp2 as the giaddr:

   ```
   cumulus@switch:~$ sudo nano /etc/default/isc-dhcp-relay
   ...
   # Additional options that are passed to the DHCP relay daemon?
   OPTIONS="-U swp2"
   ```

   The following example uses IP address 10.0.0.3 on swp2 as the giaddr:

   ```
   cumulus@switch:~$ sudo nano /etc/default/isc-dhcp-relay
   ...
   # Additional options that are passed to the DHCP relay daemon?
   OPTIONS="-U 10.0.0.3%swp2"
   ```

2. Restart the `dhcrelay` service to apply the configuration change :

   ```
   cumulus@switch:~$ sudo systemctl restart dhcrelay.service
   ```

{{< /tab >}}

{{< /tabs >}}

{{%notice note%}}
When enabling RFC 3527 support, you can specify an interface such as the loopback interface or swp interface for the gateway address. The interface you use must be reachable in the tenant VRF that it is servicing and must be unique to the switch. In EVPN symmetric routing, fabrics running an anycast gateway that use the same SVI IP address on multiple leaf switches need a unique IP address for the VRF interface and must include the layer 3 VNI for this VRF in the DHCP Relay configuration. For example:

```
cumulus@leaf01:mgmt:~$ cat /etc/default/isc-dhcp-relay-RED
SERVERS="10.1.10.104"
INTF_CMD=" -i vlan10 -i vlan20 -i vlan4001"
OPTIONS="-U RED"
```

{{%/notice%}}

### Gateway IP Address as Source IP for Relayed DHCP Packets (Advanced)

You can configure the `dhcrelay` service to forward IPv4 (only) DHCP packets to a DHCP server and ensure that the source IP address of the relayed packet is the same as the gateway IP address.

{{%notice note%}}

This option impacts all relayed IPv4 packets globally.

{{%/notice%}}

To use the gateway IP address as the source IP address:

{{< tabs "TabID302 ">}}

{{< tab "NCLU Commands ">}}

Run these commands:

```
cumulus@leaf:~$ net add dhcp relay use-giaddr-as-src
cumulus@leaf:~$ net pending
cumulus@leaf:~$ net commit
```

{{< /tab >}}

{{< tab "Linux Commands ">}}

1. Edit the `/etc/default/isc-dhcp-relay` file to add `--giaddr-src` to the `OPTIONS` line. An example is shown below.

   ```
   cumulus@switch:~$ sudo nano /etc/default/isc-dhcp-relay
   SERVERS="172.16.1.102"
   INTF_CMD="-i vlan1 -i swp51 -i swp52 -U swp2"
   OPTIONS="--giaddr-src"
   ```

2. Restart the `dhcrelay` service to apply the configuration change :

   ```
   cumulus@switch:~$ sudo systemctl restart dhcrelay.service
   ```

{{< /tab >}}

{{< /tabs >}}

## Configure IPv6 DHCP Relays

{{%notice note%}}

NCLU commands are not currently available to configure IPv6 relays.

{{%/notice%}}

1. Edit the `/etc/default/isc-dhcp-relay6` file to add the upstream and downstream interfaces. In the example below, the SVI is vlan1, and the interfaces are swp51 and swp52.

   ```
   cumulus@switch:$ sudo nano /etc/default/isc-dhcp-relay6
   SERVERS=" -u 2001:db8:100::2%swp51 -u 2001:db8:100::2%swp52"
   INTF_CMD="-l vlan1"
   ```

2. Enable, then restart the `dhcrelay6` service so that the configuration persists between reboots:

   ```
   cumulus@switch:~$ sudo systemctl enable dhcrelay6.service
   cumulus@switch:~$ sudo systemctl restart dhcrelay6.service
   ```

   To see the status of the IPv6 DHCP relay, use the `systemctl status dhcrelay6.service` command:

   ```
   cumulus@switch:~$ sudo systemctl status dhcrelay6.service
   ● dhcrelay6.service - DHCPv6 Relay Agent Daemon
      Loaded: loaded (/lib/systemd/system/dhcrelay6.service; disabled)
      Active: active (running) since Fri 2016-12-02 21:00:26 UTC; 1s ago
         Docs: man:dhcrelay(8)
   Main PID: 6152 (dhcrelay)
      CGroup: /system.slice/dhcrelay6.service
               └─6152 /usr/sbin/dhcrelay -6 --nl -d -q -l vlan1 -u 2001:db8:100::2 swp51 -u 2001:db8:100::2 swp52
   ```

## Configure Multiple DHCP Relays

Cumulus Linux supports multiple DHCP relay daemons on a switch to enable relaying of packets from different bridges to different upstream interfaces.

To configure multiple DHCP relay daemons on a switch:

1. Create a configuration file in the `/etc/default` directory for each DHCP relay daemon. Use the naming scheme `isc-dhcp-relay-<dhcp-name>` for IPv4 or `isc-dhcp-relay6-<dhcp-name>` for IPv6. An example configuration file for IPv4 is shown below:

   ```
   # Defaults for isc-dhcp-relay initscript
   # sourced by /etc/init.d/isc-dhcp-relay
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
   ```

   An example configuration file for IPv6 is shown below:

   ```
   # Defaults for isc-dhcp-relay6 initscript
   # sourced by /etc/init.d/isc-dhcp-relay6
   # installed at /etc/default/isc-dhcp-relay6 by the maintainer scripts

   #
   # This is a POSIX shell fragment
   #

   # Specify upstream and downstream interfaces
   # For example, "-u eth0 -l swp1"
   INTF_CMD=""

   # Additional options that are passed to the DHCP relay daemon?
   OPTIONS=""
   ```

2. Run the following command to start a `dhcrelay` instance, where `<dhcp-name>` is the instance name or number.

   ```
   cumulus@switch:~$ sudo systemctl start dhcrelay@<dhcp-name>
   ```

## Configure a DHCP Relay with VRR

The configuration procedure for DHCP relay with VRR is the same as documented above.

{{%notice note%}}

The DHCP relay must run on the SVI and not on the -v0 interface.

{{%/notice%}}

## Troubleshooting

If you are experiencing issues with DHCP relay, you can check if there is a problem with `systemd:`

- For IPv4, run this command:

   ```
   cumulus@switch:~$  /usr/sbin/dhcrelay -4 -i <interface-facing-host> <ip-address-dhcp-server> -i <interface-facing-dhcp-server>
   ```

- For IPv6, run this command:

   ```
   cumulus@switch:~$  /usr/sbin/dhcrelay -6 -l <interface-facing-host> -u <ip-address-hcp-server>%<interface-facing-dhcp-server>
   ```

For example:

```
cumulus@switch:~$ /usr/sbin/dhcrelay -4 -i vlan1 172.16.1.102 -i swp51
cumulus@switch:~$ /usr/sbin/dhcrelay -6 -l vlan1 -u 2001:db8:100::2%swp51
```

The above commands manually activate the DHCP relay process and they do not persist when you reboot the switch.

To see how DHCP relay is working on your switch, run the `journalctl` command:

```
cumulus@switch:~$ sudo journalctl -l -n 20 | grep dhcrelay
Dec 05 20:58:55 leaf01 dhcrelay[6152]: sending upstream swp52
Dec 05 20:58:55 leaf01 dhcrelay[6152]: sending upstream swp51
Dec 05 20:58:55 leaf01 dhcrelay[6152]: Relaying Reply to fe80::4638:39ff:fe00:3 port 546 down.
Dec 05 20:58:55 leaf01 dhcrelay[6152]: Relaying Reply to fe80::4638:39ff:fe00:3 port 546 down.
Dec 05 21:03:55 leaf01 dhcrelay[6152]: Relaying Renew from fe80::4638:39ff:fe00:3 port 546 going up.
Dec 05 21:03:55 leaf01 dhcrelay[6152]: sending upstream swp52
Dec 05 21:03:55 leaf01 dhcrelay[6152]: sending upstream swp51
Dec 05 21:03:55 leaf01 dhcrelay[6152]: Relaying Reply to fe80::4638:39ff:fe00:3 port 546 down.
Dec 05 21:03:55 leaf01 dhcrelay[6152]: Relaying Reply to fe80::4638:39ff:fe00:3 port 546 down.
```

To specify a time period with the `journalctl` command, use the `--since` flag:

```
cumulus@switch:~$ sudo journalctl -l --since "2 minutes ago" | grep dhcrelay
Dec 05 21:08:55 leaf01 dhcrelay[6152]: Relaying Renew from fe80::4638:39ff:fe00:3 port 546 going up.
Dec 05 21:08:55 leaf01 dhcrelay[6152]: sending upstream swp52
Dec 05 21:08:55 leaf01 dhcrelay[6152]: sending upstream swp51
```

### Configuration Errors

If you configure DHCP relays by editing the `/etc/default/isc-dhcp-relay` file manually instead of running NCLU commands, you might introduce configuration errors that can cause the switch to crash.

For example, if you see an error similar to the following, there might be a space between the DHCP server address and the interface used as the uplink.

```
Core was generated by /usr/sbin/dhcrelay --nl -d -i vx-40 -i vlan100 10.0.0.4 -U 10.0.1.2  %vlan120.
Program terminated with signal SIGSEGV, Segmentation fault.
```

To resolve the issue, manually edit the `/etc/default/isc-dhcp-relay` file to remove the space, then run the `systemctl restart dhcrelay.service` command to restart the `dhcrelay` service and apply the configuration change.

## Caveats and Errata

### Interface Names Cannot Be Longer than 14 Characters

The `dhcrelay` command does not bind to an interface if the interface's name is longer than 14 characters. To work around this issue, change the interface name to be 14 or fewer characters if `dhcrelay` is required to bind to it.

This is a known limitation in `dhcrelay`.
