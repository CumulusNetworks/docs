---
title: DHCP Relays
author: NVIDIA
weight: 340
toc: 3
---
<span class="a-tooltip">[DHCP](## "Dynamic Host Configuration Protocol")</span> is a client server protocol that automatically provides IP hosts with IP addresses and other related configuration information. A DHCP relay (agent) is a host that forwards DHCP packets between clients and servers that are not on the same physical subnet.

This topic describes how to configure DHCP relays for IPv4 and IPv6 using the following topology:

{{< img src = "/images/cumulus-linux/dhcp-relay-topology-basic.png" >}}

## Basic Configuration

To set up DHCP relay, you need to provide the IP address of the DHCP server and the interfaces participating in DHCP relay (facing the server and facing the client).

In the example commands below:
- The DHCP server IPv4 address is 172.16.1.102
- The DHCP server IPv6 address is 2001:db8:100::2
- vlan10 is the SVI for VLAN 10 and the uplinks are swp51 and swp52

{{< tabs "TabID21 ">}}
{{< tab "NVUE Commands ">}}

{{< tabs "TabID49 ">}}
{{< tab "IPv4 ">}}

```
cumulus@leaf01:~$ nv set service dhcp-relay default interface swp51
cumulus@leaf01:~$ nv set service dhcp-relay default interface swp52
cumulus@leaf01:~$ nv set service dhcp-relay default interface vlan10
cumulus@leaf01:~$ nv set service dhcp-relay default server 172.16.1.102
cumulus@leaf01:~$ nv config apply
```

{{< /tab >}}
{{< tab "IPv6 ">}}

```
cumulus@leaf01:~$ nv set service dhcp-relay6 default interface upstream swp51 server-address 2001:db8:100::2
cumulus@leaf01:~$ nv set service dhcp-relay6 default interface upstream swp52 server-address 2001:db8:100::2
cumulus@leaf01:~$ nv set service dhcp-relay6 default interface downstream vlan10
cumulus@leaf01:~$ nv config apply
```

{{< /tab >}}
{{< /tabs >}}

{{< /tab >}}
{{< tab "Linux Commands ">}}

{{< tabs "TabID89 ">}}
{{< tab "IPv4 ">}}

1. Edit the `/etc/default/isc-dhcp-relay-default` file to add the IP address of the DHCP server and the interfaces participating in DHCP relay.

   ```
   cumulus@leaf01:~$ sudo nano /etc/default/isc-dhcp-relay-default
   SERVERS="172.16.1.102"
   INTF_CMD="-i vlan10 -i swp51 -i swp52"
   OPTIONS=""
   ```

2. Enable, then restart the `dhcrelay` service so that the configuration persists between reboots:

   ```
   cumulus@leaf01:~$ sudo systemctl enable dhcrelay@default.service
   cumulus@leaf01:~$ sudo systemctl restart dhcrelay@default.service
   ```

{{< /tab >}}
{{< tab "IPv6 ">}}

1. Edit the `/etc/default/isc-dhcp-relay6-default` file to add the IP address of the DHCP server and the interfaces participating in DHCP relay.

   ```
   cumulus@leaf01:$ sudo nano /etc/default/isc-dhcp-relay6-default
   SERVERS=" -u 2001:db8:100::2%swp51 -u 2001:db8:100::2%swp52"
   INTF_CMD="-l vlan10"
   ```

2. Enable, then restart the `dhcrelay6` service so that the configuration persists between reboots:

   ```
   cumulus@switch:~$ sudo systemctl enable dhcrelay6@default.service
   cumulus@switch:~$ sudo systemctl restart dhcrelay6@default.service
   ```

{{< /tab >}}
{{< /tabs >}}

{{< /tab >}}
{{< /tabs >}}

{{%notice note%}}
- You configure a DHCP relay on a per-VLAN basis, specifying the SVI, not the parent bridge. In the example above, you specify *vlan10* as the SVI for VLAN 10 but you do not specify the bridge named *bridge*.
- When you configure DHCP relay with VRR, the DHCP relay client must run on the SVI; not on the -v0 interface.
- For every instance of a DHCP relay in a non-default VRF, you need to create a separate default file in the `/etc/default` directory. See {{<link url="Virtual-Routing-and-Forwarding-VRF/#dhcp-with-vrf" text="DHCP with VRF">}}.
{{%/notice%}}

## Optional Configuration

This section describes optional DHCP relay configurations. The steps provided in this section assume that you have already configured basic DHCP relay, as described above.

### DHCP Agent Information Option (Option 82)

Cumulus Linux supports DHCP Agent Information Option 82, which allows a DHCP relay to insert circuit or relay specific information into a request that the switch forwards to a DHCP server. You can use the following options:

- *Circuit ID* includes information about the circuit on which the request comes in, such as the SVI or physical port. By default, this is the printable name of the interface that receives the client request.
- *Remote ID* includes information that identifies the relay agent, such as the MAC address. By default, this is the system MAC address of the device on which DHCP relay is running.

To configure DHCP Agent Information Option 82:

{{< tabs "TabID117 ">}}
{{< tab "NVUE Commands ">}}

The following example enables Option 82 and enables circuit ID to inject the *physical switch port* on which the relayed DHCP discover packet arrives instead of the SVI:

```
cumulus@leaf01:~$ nv set service dhcp-relay default agent enable on
cumulus@leaf01:~$ nv set service dhcp-relay default agent use-pif-circuit-id enable on
cumulus@leaf01:~$ nv config apply
```

The following example enables Option 82 and sets the remote ID to be MAC address 44:38:39:BE:EF:AA. The remote ID is a custom string (up to 255 characters in length).

```
cumulus@leaf01:~$ nv set service dhcp-relay default agent enable on
cumulus@leaf01:~$ nv set service dhcp-relay default agent remote-id 44:38:39:BE:EF:AA
cumulus@leaf01:~$ nv config apply
```

{{< /tab >}}
{{< tab "Linux Commands ">}}

1. Edit the `/etc/default/isc-dhcp-relay-default` file and add one of the following options:

   To inject the ingress *SVI interface* against which DHCP processes the relayed DHCP discover packet, add `-a` to the `OPTIONS` line:

   ```
   cumulus@leaf01:~$ sudo nano /etc/default/isc-dhcp-relay-default
   ...
   # Additional options that are passed to the DHCP relay daemon?
   OPTIONS="-a"
   ```

   To inject the *physical switch port* on which the relayed DHCP discover packet arrives instead of the SVI, add `-a --use-pif-circuit-id` to the `OPTIONS` line:

   ```
   cumulus@leaf01:~$ sudo nano /etc/default/isc-dhcp-relay-default
   ...
   # Additional options that are passed to the DHCP relay daemon?
   OPTIONS="-a --use-pif-circuit-id"
   ```

   To customize the Remote ID sub-option, add `-a -r` to the `OPTIONS` line followed by a custom string (up to 255 characters). The following example adds the MAC address 44:38:39:BE:EF:AA:

   ```
   cumulus@leaf01:~$ sudo nano /etc/default/isc-dhcp-relay-default
   ...
   # Additional options that are passed to the DHCP relay daemon?
   OPTIONS="-a -r 44:38:39:BE:EF:AA"
   ```

2. Restart the `dhcrelay` service to apply the new configuration:

   ```
   cumulus@leaf01:~$ sudo systemctl restart dhcrelay@default.service
   ```

{{< /tab >}}
{{< /tabs >}}

### Control the Gateway IP Address with RFC 3527

When you need DHCP relay in an environment that relies on an anycast gateway (such as EVPN), a unique IP address is necessary on each device for return traffic. By default, in a BGP unnumbered environment with DHCP relay, the source IP address is the loopback IP address and the gateway IP address is the SVI IP address. However with anycast traffic, the SVI IP address is not unique to each rack; it is typically shared between racks. Most EVPN ToR deployments only use a single unique IP address, which is the loopback IP address.

{{<exlink url="https://tools.ietf.org/html/rfc3527" text="RFC 3527">}} enables the DHCP server to react to these environments by introducing a new parameter to the DHCP header called the link selection sub-option, which the DHCP relay agent builds. The link selection sub-option takes on the normal role of the gateway address in relaying to the DHCP server which subnet correlates to the DHCP request. When using this sub-option, the gateway address continues to be present but only relays the return IP address that the DHCP server uses; the gateway address becomes the unique loopback IP address.

When enabling RFC 3527 support, you can specify an interface, such as the loopback interface or a switch port interface to use as the gateway address. The relay picks the first IP address on that interface. If the interface has multiple IP addresses, you can specify a specific IP address for the interface.

{{%notice note%}}
RFC 3527 supports IPv4 DHCP relays only.
{{%/notice%}}

To enable RFC 3527 support and control the gateway address:

{{< tabs "TabID203 ">}}
{{< tab "NVUE Commands ">}}

Run the `nv set service dhcp-relay default gateway-interface` command with the interface or IP address you want to use. The following example uses the first IP address on the loopback interface as the gateway IP address:

```
cumulus@leaf01:~$ nv set service dhcp-relay default gateway-interface lo
```

The first IP address on the loopback interface is typically the 127.0.0.1 address. This example uses IP address 10.10.10.1 on the loopback interface as the gateway address:

```
cumulus@leaf01:~$ nv set service dhcp-relay default gateway-interface lo address 10.10.10.1
```

This example uses the first IP address on swp2 as the gateway address:

```
cumulus@leaf01:~$ nv set service dhcp-relay default gateway-interface swp2
```

This example uses IP address 10.0.0.4 on swp2 as the gateway address:

```
cumulus@leaf01:~$ nv set service dhcp-relay default gateway-interface swp2 address 10.0.0.4
```

{{< /tab >}}
{{< tab "Linux Commands ">}}

1. Edit the `/etc/default/isc-dhcp-relay-default` file and provide the `-U` option with the interface or IP address you want to use as the gateway address.

   This example uses the first IP address on the loopback interface as the gateway address:

   ```
   cumulus@leaf01:~$ sudo nano /etc/default/isc-dhcp-relay-default
   ...
   # Additional options that are passed to the DHCP relay daemon?
   OPTIONS="-U lo"
   ```

   The first IP address on the loopback interface is typically the 127.0.0.1 address. This example uses IP address 10.10.10.1 on the loopback interface as the gateway address:

   ```
   cumulus@leaf01:~$ sudo nano /etc/default/isc-dhcp-relay-default
   ...
   # Additional options that are passed to the DHCP relay daemon?
   OPTIONS="-U 10.10.10.1%lo"
   ```

   This example uses the first IP address on swp2 as the gateway address:

   ```
   cumulus@leaf01:~$ sudo nano /etc/default/isc-dhcp-relay-default
   ...
   # Additional options that are passed to the DHCP relay daemon?
   OPTIONS="-U swp2"
   ```

   This example uses IP address 10.0.0.4 on swp2 as the gateway address:

   ```
   cumulus@leaf01:~$ sudo nano /etc/default/isc-dhcp-relay-default
   ...
   # Additional options that are passed to the DHCP relay daemon?
   OPTIONS="-U 10.0.0.4%swp2"
   ```

2. Restart the `dhcrelay` service to apply the configuration change:

   ```
   cumulus@leaf01:~$ sudo systemctl restart dhcrelay@default.service
   ```

{{< /tab >}}
{{< /tabs >}}

### DHCP Relay for IPv4 in an EVPN Symmetric Environment with MLAG

In a multi-tenant EVPN symmetric routing environment with MLAG, you must enable RFC 3527 support. You can specify an interface, such as the loopback or VRF interface for the gateway address. The interface must be reachable in the tenant VRF that you configure for DHCP relay and must have a unique IPv4 address. For EVPN symmetric routing with an anycast gateway that reuses the same SVI IP address on multiple leaf switches, you must assign a unique IP address for the VRF interface and include the layer 3 VNI for this VRF in the DHCP relay configuration.

{{< img src = "/images/cumulus-linux/dhcp-relay-topology-mlag.png" >}}

The following example:
- Configures VRF RED with IPv4 address 20.20.20.1/32.
- Configures the SVIs vlan10 and vlan20, and the layer 3 VNI VLAN interface for VRF RED vlan4024_l3 to be part of the interface list to service DHCP packets. To obtain the layer 3 VNI VLAN interface, run the `nv show vrf <vrf-name> evpn` command.
- Sets the DHCP server to 10.1.10.104.
- Configures VRF RED to advertise connected routes as type-5 so that the VRF RED loopback IPv4 address is reachable.

{{%notice note%}}
You do not need to add physical uplinks in the relay configuration. Only layer 3 VNI VLAN interface configuration is required for uplinks.
{{%/notice%}}

{{< tabs "TabID366 ">}}
{{< tab "NVUE Commands ">}}

```
cumulus@leaf01:~$ nv set vrf RED loopback ip address 20.20.20.1/32
cumulus@leaf01:~$ nv set service dhcp-relay RED interface vlan10
cumulus@leaf01:~$ nv set service dhcp-relay RED interface vlan20
cumulus@leaf01:~$ nv set service dhcp-relay RED interface vlan4024_l3
cumulus@leaf01:~$ nv set service dhcp-relay RED server 10.1.10.104
cumulus@leaf01:~$ nv set vrf RED router bgp address-family ipv4-unicast redistribute connected enable on
cumulus@leaf01:~$ nv set vrf RED router bgp address-family ipv4-unicast route-export to-evpn enable on
cumulus@leaf01:~$ nv config apply
```

{{< /tab >}}
{{< tab "Linux Commands ">}}

1. Edit the `/etc/network/interfaces` file to configure VRF RED with IPv4 address 20.20.20.1/32

   ```
   cumulus@leaf01:mgmt:~$ sudo nano /etc/network/interfaces
   ...
   auto RED
   iface RED
           address 20.20.20.1/32
           vrf-table auto
   ```

2. Configure VRF RED to advertise the connected routes as type-5 so that the loopback IPv4 address is reachable:

   ```
   cumulus@leaf01:mgmt:~$ sudo vtysh 
   ...
   leaf01# configure terminal
   leaf01(config)# router bgp 65101 vrf RED
   leaf01(config-router)# address-family l2vpn evpn
   leaf01(config-router-af)# advertise ipv4 unicast 
   leaf01(config-router-af)# end
   leaf01# write memory
   ```

   The `/etc/frr/frr.conf` file now contains the following entries:

   ```
   ...
   router bgp 65101 vrf RED
    bgp router-id 10.10.10.1
   ..
    !
    address-family ipv4 unicast
     redistribute connected
     maximum-paths 64
     maximum-paths ibgp 64
    exit-address-family
    !
    address-family l2vpn evpn
     advertise ipv4 unicast
    exit-address-family
   exit
   ```

3. Edit the `/etc/default/isc-dhcp-relay-RED` file.

   ```
   cumulus@leaf01:mgmt:~$ sudo nano /etc/default/isc-dhcp-relay-RED
   SERVERS="10.1.10.104"
   INTF_CMD=" -i vlan10 -i vlan20 -i vlan4024_l3" 
   OPTIONS="-U RED"
   ```

4. Start and enable the DHCP service so that it starts automatically the next time the switch boots:

   ```
   sudo systemctl start dhcrelay@RED.service
   sudo systemctl enable dhcrelay@RED.service
   ```

{{< /tab >}}
{{< /tabs >}}

### DHCP Relay for IPv4 in an EVPN Symmetric Environment without MLAG

In a multi-tenant EVPN symmetric routing environment without MLAG, the VLAN interface (SVI) IPv4 address is typically unique on each leaf switch, which does not require RFC 3527 configuration.

The following example:
- Configures the SVIs vlan10 and vlan20, and the layer 3 VNI VLAN interface for VRF RED vlan4024_l3 to be part of INTF_CMD list to service DHCP packets. To obtain the layer 3 VNI VLAN interface, run the `nv show vrf <vrf-name> evpn` command.
- Sets the DHCP server IP address to 10.1.10.104.

{{%notice note%}}
You do not need to add physical uplinks in the relay configuration. Only layer 3 VNI VLAN interface configuration is required for uplinks.
{{%/notice%}}

{{< tabs "TabID369 ">}}
{{< tab "NVUE Commands ">}}

```
cumulus@leaf01:~$ nv set service dhcp-relay RED interface vlan10
cumulus@leaf01:~$ nv set service dhcp-relay RED interface vlan20
cumulus@leaf01:~$ nv set service dhcp-relay RED interface vlan4024_l3
cumulus@leaf01:~$ nv set service dhcp-relay RED server 10.1.10.104
cumulus@leaf01:~$ nv config apply
```

{{< /tab >}}
{{< tab "Linux Commands ">}}

1. Edit the `/etc/default/isc-dhcp-relay-RED` file.

   ```
   cumulus@leaf01:mgmt:~$ sudo nano /etc/default/isc-dhcp-relay-RED
   SERVERS="10.1.10.104"
   INTF_CMD=" -i vlan10 -i vlan20 -i vlan4024_l3" 
   OPTIONS=""
   ```

2. Start the DHCP service and enable it to start automatically when the switch boots:

   ```
   sudo systemctl start dhcrelay@RED.service
   sudo systemctl enable dhcrelay@RED.service
   ```

{{< /tab >}}
{{< /tabs >}}

### DHCP Relay for IPv6 in an EVPN Symmetric Environment

For IPv6 DHCP relay in a symmetric routing environment, you must assign a unique IPv6 address to the non-default VRF interfaces that participate in DHCP relay. Cumulus Linux uses this IPv6 address as the source address when sending packets to the DHCP server and the DHCP server replies to this address.

{{%notice note%}}
{{<link url="#control-the-gateway-ip-address-with-rfc-3527" text="RFC 3527">}} does not apply to IPv6. IPv6 has the functionality described in RFC 3527 as part of its normal operations.
{{%/notice%}}

The following example:
- Configures VRF RED with the unique IPv6 address 2001:db8:666::1/128.
- Configures VLAN 10 and 20 in VRF RED to service DHCP requests from downstream hosts.
- Sets the DHCP server to 2001:db8:199::2.
- Configures the layer 3 VNI interface for VRF RED vlan4024_l3 to process DHCP packets from the upstream server.
- Configures VRF RED to advertise the connected routes so that the loopback IPv6 address is reachable.

{{< tabs "TabID367 ">}}
{{< tab "NVUE Commands ">}}

```
cumulus@leaf01:~$ nv set vrf RED loopback ip address 2001:db8:666::1/128
cumulus@leaf01:~$ nv set service dhcp-relay6 RED interface downstream vlan10
cumulus@leaf01:~$ nv set service dhcp-relay6 RED interface downstream vlan20
cumulus@leaf01:~$ nv set service dhcp-relay6 RED interface upstream RED server-address 2001:db8:199::2
cumulus@leaf01:~$ nv set service dhcp-relay6 RED interface upstream vlan4024_l3
cumulus@leaf01:~$ nv set vrf RED router bgp address-family ipv6-unicast route-export to-evpn enable on
cumulus@leaf01:~$ nv config apply
```

{{< /tab >}}
{{< tab "Linux Commands ">}}

1. Edit the `/etc/network/interfaces` file to configure VRF RED with IPv6 address 2001:db8:666::1/128:

   ```
   cumulus@leaf01:mgmt:~$ sudo nano /etc/network/interfaces
   ...
   auto RED
   iface RED
           address 2001:db8:666::1/128
           vrf-table auto
   ```

2. Configure VRF RED to advertise the connected routes so that the loopback IPv6 address is reachable:

   ```
   cumulus@leaf01:mgmt:~$ sudo vtysh 
   ...
   leaf01# configure terminal
   leaf01(config)# router bgp 65101 vrf RED
   leaf01(config-router)# address-family l2vpn evpn
   leaf01(config-router-af)# advertise ipv6 unicast 
   leaf01(config-router-af)# end
   leaf01# write memory
   ```

   The `/etc/frr/frr.conf` file now contains the following entries:

   ```
   ...
   router bgp 65101 vrf RED
    bgp router-id 10.10.10.1
   ..
    !
    address-family ipv6 unicast
     redistribute connected
     maximum-paths 64
     maximum-paths ibgp 64
    exit-address-family
    !
    address-family l2vpn evpn
     advertise ipv6 unicast
    exit-address-family
   exit
   ```

3. Edit the `/etc/default/isc-dhcp-relay6-RED` file.

   - Set the `-l ` option to the VLANs that receive DHCP requests from hosts.
   - Set the `<ip-address-dhcp-server>%<interface-facing-dhcp-server>` option to associate the DHCP Server with VRF RED.
   - Set the `-u` option to indicate where the switch receives replies from the DHCP server (SVI vlan4024_l3).

   ```
   cumulus@leaf01:mgmt:~$ sudo nano /etc/default/isc-dhcp-relay6-RED
   INTF_CMD="-l vlan10 -l vlan20"
   SERVERS="-u 2001:db8:199::2%RED -u vlan4024_l3"
   ```

4. Start and enable the DHCP service so that it starts automatically the next time the switch boots:

   ```
   sudo systemctl start dhcrelay6@RED.service
   sudo systemctl enable dhcrelay6@RED.service
   ```

{{< /tab >}}
{{< /tabs >}}

### Gateway IP Address as Source IP for Relayed DHCP Packets (Advanced)

You can configure the `dhcrelay` service to forward IPv4 (only) DHCP packets to a DHCP server and ensure that the source IP address of the relayed packet is the same as the gateway IP address. By default, the source IP address of the relayed packet is from a layer 3 interface on the switch using normal routing methods.

{{%notice note%}}
This option impacts all relayed IPv4 packets globally.
{{%/notice%}}

To use the gateway IP address as the source IP address:

{{< tabs "TabID319 ">}}
{{< tab "NVUE Commands ">}}

```
cumulus@leaf01:~$ nv set service dhcp-relay default source-ip gateway
cumulus@leaf01:~$ nv config apply
```

To configure this setting back to the default (where the source IP address of the relayed packet is from a layer 3 interface), set the source IP address to `auto`:

```
cumulus@leaf01:~$ nv set service dhcp-relay default source-ip auto
cumulus@leaf01:~$ nv config apply
```

{{< /tab >}}
{{< tab "Linux Commands ">}}

1. Edit the `/etc/default/isc-dhcp-relay-default` file to add `--giaddr-src` to the `OPTIONS` line.

   ```
   cumulus@leaf01:~$ sudo nano /etc/default/isc-dhcp-relay-default
   SERVERS="172.16.1.102"
   INTF_CMD="-i vlan10 -i swp51 -i swp52 -U swp2"
   OPTIONS="--giaddr-src"
   ```

2. Restart the `dhcrelay` service to apply the configuration change:

   ```
   cumulus@leaf01:~$ sudo systemctl restart dhcrelay@default.service
   ```

To configure this setting back to the default (where the source IP address of the relayed packet is from a layer 3 interface), remove the `--giaddr-src` from the `OPTIONS` line.

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
+ default  auto       gateway-interface: lo
  default             interface:        swp51
  default             interface:        swp52
  default             interface:        vlan10
  default             server:    172.16.1.102
```

{{< /tab >}}
{{< tab "Linux Commands ">}}

Run the Linux `systemctl status dhcrelay@default.service` command for IPv4 or the `systemctl status dhcrelay6@default.service` command for IPv6:

```
cumulus@leaf01:~$ sudo systemctl status dhcrelay@default.service
● dhcrelay@default.service - DHCPv4 Relay Agent Daemon default in vrf default
   Loaded: loaded (/lib/systemd/system/dhcrelay@.service; enabled; vendor preset: enabled)
  Drop-In: /run/systemd/generator/dhcrelay@.service.d
           └─vrf.conf
   Active: active (running) since Tue 2023-04-18 18:23:55 UTC; 9min ago
     Docs: man:dhcrelay(8)
 Main PID: 30904 (dhcrelay)
    Tasks: 1 (limit: 2056)
   Memory: 2.3M
   CGroup: /system.slice/system-dhcrelay.slice/dhcrelay@default.service
           └─vrf
             └─30904 /usr/sbin/dhcrelay --nl -d -i swp51 -i swp52 -i vlan10 -i peerlink.4094 172.16.1.102
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

If you configure DHCP relays by editing the `/etc/default/isc-dhcp-relay-default` file manually, you can introduce configuration errors that cause the switch to crash.

For example, if you see an error similar to the following, check that there is no space between the DHCP server address and the interface you use as the uplink.

```
Core was generated by /usr/sbin/dhcrelay --nl -d -i vx-40 -i vlan10 10.0.0.4 -U 10.0.1.2  %vlan20.
Program terminated with signal SIGSEGV, Segmentation fault.
```

To resolve the issue, manually edit the `/etc/default/isc-dhcp-relay-default` file to remove the space, then run the `systemctl restart dhcrelay@default.service` command to restart the `dhcrelay` service and apply the configuration change.

## Considerations

- The `dhcrelay` command does not bind to an interface if the interface name is longer than 14 characters. This is a known limitation in `dhcrelay`.
- DHCP discover packets transiting the switch are also sent to the CPU for additional processing, then dropped after being switched by the hardware. This causes the `RX_DRP` and `HwIfInDiscards` counters to increment on the interface even though the hardware forwards the packet correctly.
