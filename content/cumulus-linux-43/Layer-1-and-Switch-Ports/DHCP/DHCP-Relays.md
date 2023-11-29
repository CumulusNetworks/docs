---
title: DHCP Relays
author: NVIDIA
weight: 340
toc: 3
---
DHCP is a client server protocol that automatically provides IP hosts with IP addresses and other related configuration information. A DHCP relay (agent) is a host that forwards DHCP packets between clients and servers that are not on the same physical subnet.

This topic describes how to configure DHCP relays for IPv4 and IPv6 using the following topology:

{{< img src = "/images/cumulus-linux/dhcp-relay-topology-basic.png" >}}

{{%notice note%}}

If you intend to run the `dhcrelay` service within a {{<link url="Virtual-Routing-and-Forwarding-VRF" text="VRF">}}, follow {{<link url="Virtual-Routing-and-Forwarding-VRF/#dhcp-with-vrf" text="these steps">}}.

{{%/notice%}}

## Basic Configuration

To set up DHCP relay, you need to provide the IP address of the DHCP server and the interfaces participating in DHCP relay (facing the server and facing the client). You can specify as many server IP addresses that can fit in 255 octets.

{{< tabs "TabID25 ">}}

{{< tab "NCLU Commands ">}}

{{< tabs "TabID27 ">}}

{{< tab "IPv4 ">}}

In the example commands below, the DHCP server IP address is 172.16.1.102, vlan10 is the SVI for VLAN 10 and the uplinks are swp51 and swp52.

```
cumulus@leaf01:~$ net add dhcp relay interface swp51
cumulus@leaf01:~$ net add dhcp relay interface swp52
cumulus@leaf01:~$ net add dhcp relay interface vlan10
cumulus@leaf01:~$ net add dhcp relay server 172.16.1.102
cumulus@leaf01:~$ net pending
cumulus@leaf01:~$ net commit
```

{{< /tab >}}

{{< tab "IPv6 ">}}

NCLU commands are not currently available to configure IPv6 relays. Use the Linux Commands.

{{< /tab >}}

{{< /tabs >}}

{{< /tab >}}

{{< tab "Linux Commands ">}}

{{< tabs "TabID55 ">}}

{{< tab "IPv4 ">}}

1. Edit the `/etc/default/isc-dhcp-relay` file to add the IP address of the DHCP server and the interfaces participating in DHCP relay. In the example below, the DHCP server IP address is 172.16.1.102, vlan10 is the SVI for VLAN 10, and the uplinks are swp51 and swp52.

   ```
   cumulus@leaf01:~$ sudo nano /etc/default/isc-dhcp-relay
   SERVERS="172.16.1.102"
   INTF_CMD="-i vlan10 -i swp51 -i swp52"
   OPTIONS=""
   ```

2. Enable, then restart the `dhcrelay` service so that the configuration persists between reboots:

   ```
   cumulus@leaf01:~$ sudo systemctl enable dhcrelay.service
   cumulus@leaf01:~$ sudo systemctl restart dhcrelay.service
   ```

{{< /tab >}}

{{< tab "IPv6 ">}}

1. Edit the `/etc/default/isc-dhcp-relay6` file to add the IP address of the DHCP server and the interfaces participating in DHCP relay. In the example below, the DHCP server IP address is 2001:db8:100::2, vlan10 is the SVI for VLAN 10, and the uplinks are swp51 and swp52.

   ```
   cumulus@leaf01:$ sudo nano /etc/default/isc-dhcp-relay6
   SERVERS=" -u 2001:db8:100::2%swp51 -u 2001:db8:100::2%swp52"
   INTF_CMD="-l vlan10"
   ```

2. Enable, then restart the `dhcrelay6` service so that the configuration persists between reboots:

   ```
   cumulus@switch:~$ sudo systemctl enable dhcrelay6.service
   cumulus@switch:~$ sudo systemctl restart dhcrelay6.service
   ```

{{< /tab >}}

{{< /tabs >}}

{{< /tab >}}

{{< /tabs >}}

{{%notice note%}}

- You configure a DHCP relay on a per-VLAN basis, specifying the SVI, not the parent bridge. In the example above, you specify *vlan10* as the SVI for VLAN 10 but you do not specify the bridge named *bridge*.
- When you configure DHCP relay with VRR, the DHCP relay client must run on the SVI; not on the -v0 interface.

{{%/notice%}}

## Optional Configuration

This section describes optional DHCP relay configurations. The steps provided in this section assume that you have already configured basic DHCP relay, as described above.

### DHCP Agent Information Option (Option 82)

Cumulus Linux supports DHCP Agent Information Option 82, which allows a DHCP relay to insert circuit or relay specific information into a request that is being forwarded to a DHCP server. The following options are provided:

- *Circuit ID* includes information about the circuit on which the request comes in, such as the SVI or physical port. By default, this is the printable name of the interface on which the client request is received.
- *Remote ID* includes information that identifies the relay agent, such as the MAC address. By default, this is the system MAC address of the device on which DHCP relay is running.

{{%notice note%}}

NCLU commands are not currently available for this feature. Use Linux commands.

{{%/notice%}}

To configure DHCP Agent Information Option 82:

1. Edit the `/etc/default/isc-dhcp-relay` file and add one of the following options:

   To inject the ingress *SVI interface* against which the relayed DHCP discover packet is processed, add `-a` to the `OPTIONS` line:

   ```
   cumulus@leaf01:~$ sudo nano /etc/default/isc-dhcp-relay
   ...
   # Additional options that are passed to the DHCP relay daemon?
   OPTIONS="-a"
   ```

   To inject the *physical switch port* on which the relayed DHCP discover packet arrives instead of the SVI, add `-a --use-pif-circuit-id` to the `OPTIONS` line:

   ```
   cumulus@leaf01:~$ sudo nano /etc/default/isc-dhcp-relay
   ...
   # Additional options that are passed to the DHCP relay daemon?
   OPTIONS="-a --use-pif-circuit-id"
   ```

   To customize the Remote ID sub-option, add `-a -r` to the `OPTIONS` line followed by a custom string (up to 255 characters):

   ```
   cumulus@leaf01:~$ sudo nano /etc/default/isc-dhcp-relay
   ...
   # Additional options that are passed to the DHCP relay daemon?
   OPTIONS="-a -r CUSTOMVALUE"
   ```

2. Restart the `dhcrelay` service to apply the new configuration:

   ```
   cumulus@leaf01:~$ sudo systemctl restart dhcrelay.service
   ```

### Control the Gateway IP Address with RFC 3527

When DHCP relay is required in an environment that relies on an anycast gateway (such as EVPN), a unique IP address is necessary on each device for return traffic. By default, in a BGP unnumbered environment with DHCP relay, the source IP address is set to the loopback IP address and the gateway IP address (giaddr) is set to the SVI IP address. However with anycast traffic, the SVI IP address is not unique to each rack; it is typically shared between racks. Most EVPN ToR deployments only possess a single unique IP address, which is the loopback IP address.

{{<exlink url="https://tools.ietf.org/html/rfc3527" text="RFC 3527">}} enables the DHCP server to react to these environments by introducing a new parameter to the DHCP header called the link selection sub-option, which is built by the DHCP relay agent. The link selection sub-option takes on the normal role of the giaddr in relaying to the DHCP server which subnet is correlated to the DHCP request. When using this sub-option, the giaddr continues to be present but only relays the return IP address that is to be used by the DHCP server; the giaddr becomes the unique loopback IP address.

When enabling RFC 3527 support, you can specify an interface, such as the loopback interface or a switch port interface to be used as the giaddr. The relay picks the first IP address on that interface. If the interface has multiple IP addresses, you can specify a specific IP address for the interface.

{{%notice note%}}

RFC 3527 is supported for IPv4 DHCP relays only.

{{%/notice%}}

To enable RFC 3527 support and control the giaddr:

{{< tabs "TabID166 ">}}

{{< tab "NCLU Commands ">}}

Run the `net add dhcp relay giaddr-interface` command with the interface or the interface and IP address you want to use.

This example uses the first IP address on the loopback interface as the giaddr:

```
cumulus@leaf01:~$ net add dhcp relay giaddr-interface lo
```

The first IP address on the loopback interface is typically the 127.0.0.1 address. This example uses IP address 10.10.10.1 on the loopback interface as the giaddr:

```
cumulus@leaf01:~$ net add dhcp relay giaddr-interface lo 10.10.10.1
```

This example uses the first IP address on swp2 as the giaddr:

```
cumulus@leaf01:~$ net add dhcp relay giaddr-interface swp2
```

This example uses IP address 10.0.0.4 on swp2 as the giaddr:

```
cumulus@leaf01:~$ net add dhcp relay giaddr-interface swp2 10.0.0.4
```

{{< /tab >}}

{{< tab "Linux Commands ">}}

1. Edit the `/etc/default/isc-dhcp-relay` file and provide the `-U` option with the interface or IP address you want to use as the giaddr.

   This example uses the first IP address on the loopback interface as the giaddr:

   ```
   cumulus@leaf01:~$ sudo nano /etc/default/isc-dhcp-relay
   ...
   # Additional options that are passed to the DHCP relay daemon?
   OPTIONS="-U lo"
   ```

   The first IP address on the loopback interface is typically the 127.0.0.1 address. This example uses IP address 10.10.10.1 on the loopback interface as the giaddr:

   ```
   cumulus@leaf01:~$ sudo nano /etc/default/isc-dhcp-relay
   ...
   # Additional options that are passed to the DHCP relay daemon?
   OPTIONS="-U 10.10.10.1%lo"
   ```

   This example uses the first IP address on swp2 as the giaddr:

   ```
   cumulus@leaf01:~$ sudo nano /etc/default/isc-dhcp-relay
   ...
   # Additional options that are passed to the DHCP relay daemon?
   OPTIONS="-U swp2"
   ```

   This example uses IP address 10.0.0.4 on swp2 as the giaddr:

   ```
   cumulus@leaf01:~$ sudo nano /etc/default/isc-dhcp-relay
   ...
   # Additional options that are passed to the DHCP relay daemon?
   OPTIONS="-U 10.0.0.4%swp2"
   ```

2. Restart the `dhcrelay` service to apply the configuration change:

   ```
   cumulus@leaf01:~$ sudo systemctl restart dhcrelay.service
   ```

{{< /tab >}}

{{< tab "CUE Commands ">}}

Run the `cl set service dhcp-relay default giaddress-interface` command with the interface/IP address you want to use. The  following example uses the first IP address on the loopback interface as the gateway IP address:

```
cumulus@leaf01:~$ cl set service dhcp-relay default giaddress-interface lo
```

The first IP address on the loopback interface is typically the 127.0.0.1 address. This example uses IP address 10.10.10.1 on the loopback interface as the giaddr:

```
cumulus@leaf01:~$ cl set service dhcp-relay default giaddress-interface lo 10.10.10.1
```

This example uses the first IP address on swp2 as the giaddr:

```
cumulus@leaf01:~$ cl set service dhcp-relay default giaddr-interface swp2
```

This example uses IP address 10.0.0.4 on swp2 as the giaddr:

```
cumulus@leaf01:~$ cl set service dhcp-relay default giaddr-interface swp2 10.0.0.4
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

Run the `net add dhcp relay use-giaddr-as-src` command:

```
cumulus@leaf:~$ net add dhcp relay use-giaddr-as-src
cumulus@leaf:~$ net pending
cumulus@leaf:~$ net commit
```

{{< /tab >}}

{{< tab "Linux Commands ">}}

1. Edit the `/etc/default/isc-dhcp-relay` file to add `--giaddr-src` to the `OPTIONS` line. An example is shown below.

   ```
   cumulus@leaf01:~$ sudo nano /etc/default/isc-dhcp-relay
   SERVERS="172.16.1.102"
   INTF_CMD="-i vlan10 -i swp51 -i swp52 -U swp2"
   OPTIONS="--giaddr-src"
   ```

2. Restart the `dhcrelay` service to apply the configuration change:

   ```
   cumulus@leaf01:~$ sudo systemctl restart dhcrelay.service
   ```

{{< /tab >}}

{{< /tabs >}}

### Configure Multiple DHCP Relays

Cumulus Linux supports multiple DHCP relay daemons on a switch to enable relaying of packets from different bridges to different upstream interfaces.

To configure multiple DHCP relay daemons on a switch:

1. In the `/etc/default` directory, create a configuration file for each DHCP relay daemon. Use the naming scheme `isc-dhcp-relay-<dhcp-name>` for IPv4 or `isc-dhcp-relay6-<dhcp-name>` for IPv6. An example configuration file for IPv4 is shown below:

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

2. Run the following command to start a `dhcrelay` instance, where `<dhcp-name>` is the instance name or number.

   ```
   cumulus@leaf01:~$ sudo systemctl start dhcrelay@<dhcp-name>
   ```

## Troubleshooting

This section provides troubleshooting tips.

### Show DHCP Relay Status

To show the DHCP relay status:

{{< tabs "TabID583 ">}}

{{< tab "Linux Commands ">}}

Run the Linux `systemctl status dhcrelay.service` command for IPv4 DHCP or the `systemctl status dhcrelay6.service` command for IPv6 DHCP. For example:

```
cumulus@leaf01:~$ sudo systemctl status dhcrelay.service
● dhcrelay.service - DHCPv4 Relay Agent Daemon
    Loaded: loaded (/lib/systemd/system/dhcrelay.service; enabled)
    Active: active (running) since Fri 2016-12-02 17:09:10 UTC; 2min 16s ago
      Docs: man:dhcrelay(8)
Main PID: 1997 (dhcrelay)
    CGroup: /system.slice/dhcrelay.service
            └─1997 /usr/sbin/dhcrelay --nl -d -q -i vlan10 -i swp51 -i swp52 172.16.1.102
```

{{< /tab >}}

{{< tab "CUE Commands ">}}

Run the `cl show service dhcp-relay` command. For example:

```
cumulus@leaf01:~$ cl show service dhcp-relay
           source-ip  Summary
---------  ---------  -----------------------
+ default  auto       giaddress-interface: lo
  default             interface:        swp51
  default             interface:        swp52
  default             interface:        vlan10
  default             server:    172.16.1.102
```

{{< /tab >}}

{{< /tabs >}}

### Check systemd

If you are experiencing issues with DHCP relay, check if there is a problem with `systemd:`

- For IPv4, run the `/usr/sbin/dhcrelay -4 -i <interface-facing-host> <ip-address-dhcp-server> -i <interface-facing-dhcp-server>` command. For example:

   ```
   cumulus@leaf01:~$ /usr/sbin/dhcrelay -4 -i vlan10 172.16.1.102 -i swp51
   ```

- For IPv6,run the `/usr/sbin/dhcrelay -6 -l <interface-facing-host> -u <ip-address-hcp-server>%<interface-facing-dhcp-server>` command. For example:

   ```
   cumulus@leaf01:~$ /usr/sbin/dhcrelay -6 -l vlan10 -u 2001:db8:100::2%swp51
   ```

To see how DHCP relay is working on your switch, run the `journalctl` command:

```
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
```

To specify a time period with the `journalctl` command, use the `--since` flag:

```
cumulus@leaf01:~$ sudo journalctl -l --since "2 minutes ago" | grep dhcrelay
Dec 05 21:08:55 leaf01 dhcrelay[6152]: Relaying Renew from fe80::4638:39ff:fe00:3 port 546 going up.
Dec 05 21:08:55 leaf01 dhcrelay[6152]: sending upstream swp52
Dec 05 21:08:55 leaf01 dhcrelay[6152]: sending upstream swp51
```

### Configuration Errors

If you configure DHCP relays by editing the `/etc/default/isc-dhcp-relay` file manually, you might introduce configuration errors that can cause the switch to crash.

For example, if you see an error similar to the following, there might be a space between the DHCP server address and the interface used as the uplink.

```
Core was generated by /usr/sbin/dhcrelay --nl -d -i vx-40 -i vlan10 10.0.0.4 -U 10.0.1.2  %vlan20.
Program terminated with signal SIGSEGV, Segmentation fault.
```

To resolve the issue, manually edit the `/etc/default/isc-dhcp-relay` file to remove the space, then run the `systemctl restart dhcrelay.service` command to restart the `dhcrelay` service and apply the configuration change.

## Considerations

The `dhcrelay` command does not bind to an interface if the interface name is longer than 14 characters. This is a known limitation in `dhcrelay`.
