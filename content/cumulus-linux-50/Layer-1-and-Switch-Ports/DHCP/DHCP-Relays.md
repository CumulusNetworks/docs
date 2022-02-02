---
title: DHCP Relays
author: NVIDIA
weight: 340
toc: 3
---
[DHCP](## "Dynamic Host Configuration Protocol") is a client server protocol that automatically provides IP hosts with IP addresses and other related configuration information. A DHCP relay (agent) is a host that forwards DHCP packets between clients and servers that are not on the same physical subnet.

This topic describes how to configure DHCP relays for IPv4 and IPv6 using the following topology:

{{< img src = "/images/cumulus-linux/dhcp-relay-topology-basic.png" >}}

## Basic Configuration

To set up DHCP relay, you need to provide the IP address of the DHCP server and the interfaces participating in DHCP relay (facing the server and facing the client). In an MLAG configuration, you must also specify the peerlink interface in case the local uplink interfaces fail.

In the example commands below:
- The DHCP server IPv4 address is 172.16.1.102
- The DHCP server IPv6 address is 2001:db8:100::2
- vlan10 is the SVI for VLAN 10 and the uplinks are swp51 and swp52
- `peerlink.4094` is the MLAG interface

{{< tabs "TabID21 ">}}
{{< tab "NVUE Commands ">}}

{{< tabs "TabID49 ">}}
{{< tab "IPv4 ">}}

```
cumulus@leaf01:~$ nv set service dhcp-relay default interface swp51
cumulus@leaf01:~$ nv set service dhcp-relay default interface swp52
cumulus@leaf01:~$ nv set service dhcp-relay default interface vlan10
cumulus@leaf01:~$ nv set service dhcp-relay default interface peerlink.4094
cumulus@leaf01:~$ nv set service dhcp-relay default server 172.16.1.102
cumulus@leaf01:~$ nv config apply
```

{{< /tab >}}
{{< tab "IPv6 ">}}

```
cumulus@leaf01:~$ nv set service dhcp-relay6 default interface upstream swp51 address 2001:db8:100::2
cumulus@leaf01:~$ nv set service dhcp-relay6 default interface upstream swp52 address 2001:db8:100::2
cumulus@leaf01:~$ nv set service dhcp-relay6 default interface downstream vlan10
cumulus@leaf01:~$ nv set service dhcp-relay6 default interface downstream peerlink.4094
cumulus@leaf01:~$ nv config apply
```

{{< /tab >}}
{{< /tabs >}}

{{< /tab >}}
{{< tab "Linux Commands ">}}

{{< tabs "TabID89 ">}}
{{< tab "IPv4 ">}}

1. Edit the `/etc/default/isc-dhcp-relay` file to add the IP address of the DHCP server and the interfaces participating in DHCP relay.

   ```
   cumulus@leaf01:~$ sudo nano /etc/default/isc-dhcp-relay
   SERVERS="172.16.1.102"
   INTF_CMD="-i vlan10 -i swp51 -i swp52 -i peerlink.4094"
   OPTIONS=""
   ```

2. Enable, then restart the `dhcrelay` service so that the configuration persists between reboots:

   ```
   cumulus@leaf01:~$ sudo systemctl enable dhcrelay.service
   cumulus@leaf01:~$ sudo systemctl restart dhcrelay.service
   ```

{{< /tab >}}
{{< tab "IPv6 ">}}

1. Edit the `/etc/default/isc-dhcp-relay6` file to add the IP address of the DHCP server and the interfaces participating in DHCP relay.

   ```
   cumulus@leaf01:$ sudo nano /etc/default/isc-dhcp-relay6
   SERVERS=" -u 2001:db8:100::2%swp51 -u 2001:db8:100::2%swp52"
   INTF_CMD="-l vlan10 -l peerlink.4094"
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
- If you intend to run the `dhcrelay` service within a {{<link url="Virtual-Routing-and-Forwarding-VRF" text="VRF">}}, including the {{<link url="Management-VRF" text="management VRF">}}, follow {{<link url="Management-VRF/#run-services-within-the-management-vrf" text="these steps">}}.
- For every instance of a DHCP relay in a non-default VRF, you need to create a separate default file in the `/etc/default` directory. See {{<link url="Virtual-Routing-and-Forwarding-VRF/#dhcp-with-vrf" text="DHCP with VRF">}}.
{{%/notice%}}

## Optional Configuration

This section describes optional DHCP relay configuration. The steps provided in this section assume that you already done basic DHCP relay configuration, described above.

### DHCP Agent Information Option (Option 82)

Cumulus Linux supports DHCP Agent Information Option 82, which allows a DHCP relay to insert circuit or relay specific information into a request that the switch forwards to a DHCP server. You can use the following options:

- *Circuit ID* includes information about the circuit on which the request comes in, such as the SVI or physical port. By default, this is the printable name of the interface that receives the client request.
- *Remote ID* includes information that identifies the relay agent, such as the MAC address. By default, this is the system MAC address of the device on which DHCP relay is running.

To configure DHCP Agent Information Option 82:

1. Edit the `/etc/default/isc-dhcp-relay` file and add one of the following options:

   To inject the ingress *SVI interface* against which DHCP processes the relayed DHCP discover packet, add `-a` to the `OPTIONS` line:

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

When you need DHCP relay in an environment that relies on an anycast gateway (such as EVPN), a unique IP address is necessary on each device for return traffic. By default, in a BGP unnumbered environment with DHCP relay, the source IP address is the loopback IP address and the gateway IP address (giaddr) is the SVI IP address. However with anycast traffic, the SVI IP address is not unique to each rack; it is typically shared between racks. Most EVPN ToR deployments only use a single unique IP address, which is the loopback IP address.

{{<exlink url="https://tools.ietf.org/html/rfc3527" text="RFC 3527">}} enables the DHCP server to react to these environments by introducing a new parameter to the DHCP header called the link selection sub-option, which the DHCP relay agent builds. The link selection sub-option takes on the normal role of the giaddr in relaying to the DHCP server which subnet correlates to the DHCP request. When using this sub-option, the giaddr continues to be present but only relays the return IP address that the DHCP server uses; the giaddr becomes the unique loopback IP address.

When enabling RFC 3527 support, you can specify an interface, such as the loopback interface or a switch port interface to use as the giaddr. The relay picks the first IP address on that interface. If the interface has multiple IP addresses, you can specify a specific IP address for the interface.

{{%notice note%}}
RFC 3527 supports IPv4 DHCP relays only.
{{%/notice%}}

<!--The following illustration demonstrates how you can control the giaddr with RFC 3527.

{{< img src = "/images/cumulus-linux/dhcp-relay-RFC3527.png" >}}-->

To enable RFC 3527 support and control the giaddr:

{{< tabs "TabID203 ">}}
{{< tab "NVUE Commands ">}}

Run the `nv set service dhcp-relay default giaddress-interface` command with the interface/IP address you want to use. The following example uses the first IP address on the loopback interface as the gateway IP address:

```
cumulus@leaf01:~$ nv set service dhcp-relay default giaddress-interface lo
```

The first IP address on the loopback interface is typically the 127.0.0.1 address. This example uses IP address 10.10.10.1 on the loopback interface as the giaddr:

```
cumulus@leaf01:~$ nv set service dhcp-relay default giaddress-interface lo address 10.10.10.1
```

This example uses the first IP address on swp2 as the giaddr:

```
cumulus@leaf01:~$ nv set service dhcp-relay default giaddr-interface swp2
```

This example uses IP address 10.0.0.4 on swp2 as the giaddr:

```
cumulus@leaf01:~$ nv set service dhcp-relay default giaddr-interface swp2 address 10.0.0.4
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
{{< /tabs >}}

### Gateway IP Address as Source IP for Relayed DHCP Packets (Advanced)

You can configure the `dhcrelay` service to forward IPv4 (only) DHCP packets to a DHCP server and ensure that the source IP address of the relayed packet is the same as the gateway IP address.

{{%notice note%}}
This option impacts all relayed IPv4 packets globally.
{{%/notice%}}

To use the gateway IP address as the source IP address:

{{< tabs "TabID319 ">}}
{{< tab "NVUE Commands ">}}

```
cumulus@leaf01:~$ nv set service dhcp-relay default source-ip giaddress
cumulus@leaf01:~$ nv config apply
```

{{< /tab >}}
{{< tab "Linux Commands ">}}

1. Edit the `/etc/default/isc-dhcp-relay` file to add `--giaddr-src` to the `OPTIONS` line.

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

1. In the `/etc/default` directory, create a configuration file for each DHCP relay daemon. Use the naming scheme `isc-dhcp-relay-<dhcp-name>` for IPv4 or `isc-dhcp-relay6-<dhcp-name>` for IPv6. This is an example configuration file for IPv4:

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

{{< tabs "TabID405 ">}}
{{< tab "NVUE Commands ">}}

Run the `nv show service dhcp-relay` command for IPv4 or the `nv show service dhcp-relay6` command for IPv6:

```
cumulus@leaf01:~$ nv show service dhcp-relay
           source-ip  Summary
---------  ---------  -----------------------
+ default  auto       giaddress-interface: lo
  default             interface:        swp51
  default             interface:        swp52
  default             interface:        vlan10
  default             server:    172.16.1.102
```

{{< /tab >}}
{{< tab "Linux Commands ">}}

Run the Linux `systemctl status dhcrelay.service` command for IPv4 or the `systemctl status dhcrelay6.service` command for IPv6:

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
{{< /tabs >}}

### Check systemd

If you are experiencing issues with DHCP relay, check if there is a problem with `systemd:`

- For IPv4, run the `/usr/sbin/dhcrelay -4 -i <interface-facing-host> <ip-address-dhcp-server> -i <interface-facing-dhcp-server>` command. For example:

   ```
   cumulus@leaf01:~$ /usr/sbin/dhcrelay -4 -i vlan10 172.16.1.102 -i swp51
   ```

- For IPv6, run the `/usr/sbin/dhcrelay -6 -l <interface-facing-host> -u <ip-address-dhcp-server>%<interface-facing-dhcp-server>` command. For example:

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

If you configure DHCP relays by editing the `/etc/default/isc-dhcp-relay` file manually, you can introduce configuration errors that cause the switch to crash.

For example, if you see an error similar to the following, check that there is no space between the DHCP server address and the interface you use as the uplink.

```
Core was generated by /usr/sbin/dhcrelay --nl -d -i vx-40 -i vlan10 10.0.0.4 -U 10.0.1.2  %vlan20.
Program terminated with signal SIGSEGV, Segmentation fault.
```

To resolve the issue, manually edit the `/etc/default/isc-dhcp-relay` file to remove the space, then run the `systemctl restart dhcrelay.service` command to restart the `dhcrelay` service and apply the configuration change.

## Considerations

The `dhcrelay` command does not bind to an interface if the interface name is longer than 14 characters. This is a known limitation in `dhcrelay`.
