---
title: DHCP Servers
author: NVIDIA
weight: 350
toc: 3
---
A DHCP Server automatically provides and assigns IP addresses and other network parameters to client devices. It relies on the Dynamic Host Configuration Protocol to respond to broadcast requests from clients.

{{%notice note%}}
If you intend to run the `dhcpd` service within a {{<link url="Virtual-Routing-and-Forwarding-VRF" text="VRF">}}, including the {{<link url="Management-VRF" text="management VRF">}}, follow {{<link url="Management-VRF/#run-services-within-the-management-vrf" text="these steps">}}.
{{%/notice%}}

For information about DHCP relays, refer to {{<link title="DHCP Relays">}}.

## Basic Configuration

This section shows you how to configure a DHCP server using the following topology, where the DHCP server is a switch running Cumulus Linux.

{{< img src = "/images/cumulus-linux/dhcp-server-topology.png" >}}

To configure the DHCP server on a Cumulus Linux switch:
- Create a DHCP pool by providing a pool ID. The ID is an IPv4 or IPv6 prefix.
- Provide a name for the pool (optional).
- Provide the IP address of the DNS Server you want to use in this pool. You can assign multiple DNS servers.
- Provide the domain name you want to use for this pool so that name resolution is provided (optional).
- Define the range of all IP addresses available for assignment.
- Provide the default gateway IP address (optional).

In addition, you can configure a static IP address for a resource, such as a server or printer:
- Create an ID for the static assignment. This is typically the name of the resource.
- Provide the static IP address you want to assign to this resource.
- Provide the MAC address of the resource to which you want to assign the IP address.

{{%notice note%}}
- To configure static IP address assignements, you must first configure a pool.
- You can set the DNS server IP address and domain name globally or specify different DNS server IP addresses and domain names for different pools. The following example commands configure a DNS server IP address and domain name for a pool.
{{%/notice%}}

{{< tabs "TabID27 ">}}
{{< tab "CUE Commands ">}}

{{< tabs "TabI32 ">}}
{{< tab "IPv4 ">}}

```
cumulus@switch:~$ cl set system dhcp-server pool 10.1.10.0/24
cumulus@switch:~$ cl set system dhcp-server pool 10.1.10.0/24 pool-name storage-servers
cumulus@switch:~$ cl set system dhcp-server pool 10.1.10.0/24 domain-name-server 192.168.200.53
cumulus@switch:~$ cl set system dhcp-server pool 10.1.10.0/24 domain-name example.com
cumulus@switch:~$ cl set system dhcp-server pool 10.1.10.0/24 range 10.1.10.100 to 10.1.10.199
cumulus@switch:~$ cl set system dhcp-server pool 10.1.10.0/24 gateway 10.1.10.1
cumulus@switch:~$ cl set system dhcp-server static server1
cumulus@switch:~$ cl set system dhcp-server static server1 ip-address 10.0.0.2
cumulus@switch:~$ cl set system dhcp-server static server1 mac-address 44:38:39:00:01:7e
cumulus@switch:~$ cl config apply
```

{{< /tab >}}
{{< tab "IPv6 ">}}

```
cumulus@switch:~$ cl set system dhcp-server6 pool 2001:db8::1/128 
cumulus@switch:~$ cl set system dhcp-server6 pool 2001:db8::1/128 pool-name storage-servers
cumulus@switch:~$ cl set system dhcp-server6 pool 2001:db8::1/128 domain-name-server 2001:db8:100::64
cumulus@switch:~$ cl set system dhcp-server6 pool 2001:db8::1/128 domain-name example.com
cumulus@switch:~$ cl set system dhcp-server6 pool 2001:db8::1/128 range 2001:db8:1::100 to 2001:db8:1::199 
cumulus@switch:~$ cl set system dhcp-server6 pool 2001:db8::1/128 gateway 2001:db8::a0a:0a01
cumulus@switch:~$ cl set system dhcp-server6 static server1
cumulus@switch:~$ cl set system dhcp-server6 static server1 ip-address 2001:db8:1::100
cumulus@switch:~$ cl set system dhcp-server6 static server1 mac-address 44:38:39:00:01:7e
cumulus@switch:~$ cl config apply
```

{{< /tab >}}
{{< /tabs >}}

{{< /tab >}}
{{< tab "Linux Commands ">}}

{{< tabs "TabID53 ">}}
{{< tab "IPv4 ">}}

1. In a text editor, edit the `/etc/dhcp/dhcpd.conf` file. Use following configuration as an example:

   ```
   cumulus@switch:~$ sudo nano /etc/dhcp/dhcpd.conf
   authoritative;
   subnet 10.1.10.0 netmask 255.255.255.0 {
      option domain-name-servers 192.168.200.53;
      option domain-name example.com;
      option routers 10.1.10.1;
      default-lease-time 3600;
      max-lease-time 3600;
      default-url ;
   pool {
          range 10.1.10.100 10.1.10.199;
          }
   }
   #Statics
   group {
      host server1 {
         hardware ethernet 44:38:39:00:01:7e;
         fixed-address 10.0.0.2;
      }
   }
   ```

2. Edit the `/etc/default/isc-dhcp-server` configuration file so that the DHCP server starts when the system boots. Here is an example configuration:

   ```
   cumulus@switch:~$ sudo nano /etc/default/isc-dhcp-server
   DHCPD_CONF="-cf /etc/dhcp/dhcpd.conf"

   INTERFACES="swp1"
   ```

3. Enable and start the `dhcpd` service:

   ```
   cumulus@switch:~$ sudo systemctl enable dhcpd.service
   cumulus@switch:~$ sudo systemctl start dhcpd.service
   ```

{{< /tab >}}
{{< tab "IPv6 ">}}

1. In a text editor, edit the `/etc/dhcp/dhcpd6.conf` file. Use following configuration as an example:

   ```
   cumulus@switch:~$ sudo nano /etc/dhcp/dhcpd6.conf
   authoritative;
   subnet6 2001:db8::1/128 {
      option domain-name-servers 2001:db8:100::64;
      option domain-name example.com;
      option routers 2001:db8::a0a:0a01;
      default-lease-time 3600;
      max-lease-time 3600;
      default-url ;
      pool {
          range6 2001:db8:1::100 2001:db8:1::199;
      }
   }
   #Statics
   group {
      host server1 {
          hardware ethernet 44:38:39:00:01:7e;
          fixed-address6 2001:db8:1::100;
      }
   }
   ```

2. Edit the `/etc/default/isc-dhcp-server6` file so that the DHCP server launches when the system boots. Here is an example configuration:

   ```
   cumulus@switch:~$ sudo nano /etc/default/isc-dhcp-server6
   DHCPD_CONF="-cf /etc/dhcp/dhcpd6.conf"

   INTERFACES="swp1"
   ```

3. Enable and start the `dhcpd6` service:

   ```
   cumulus@switch:~$ sudo systemctl enable dhcpd6.service
   cumulus@switch:~$ sudo systemctl start dhcpd6.service
   ```

{{< /tab >}}
{{< /tabs >}}

{{< /tab >}}
{{< /tabs >}}

## Optional Configuration

### Lease Time

You can set the network address lease time assigned to DHCP clients. You can specify a number between 180 and 31536000. The default lease time is 600 seconds.

{{< tabs "TabID274 ">}}
{{< tab "CUE Commands ">}}

{{< tabs "TabID277 ">}}
{{< tab "IPv4 ">}}

```
cumulus@switch:~$ cl set system dhcp-server pool 10.1.10.0/24 lease-time 200000
cumulus@switch:~$ cl config apply
```

{{< /tab >}}
{{< tab "IPv6 ">}}

```
cumulus@switch:~$ cl set system dhcp-server6 pool 10.1.10.0/24 lease-time 200000
cumulus@switch:~$ cl config apply
```

{{< /tab >}}
{{< /tabs >}}

{{< /tab >}}
{{< tab "Linux Commands ">}}

{{< tabs "TabID299 ">}}
{{< tab "IPv4 ">}}

1. Edit the `/etc/dhcp/dhcpd.conf` file to set the lease time (in seconds):

   ```
   cumulus@switch:~$ sudo nano /etc/dhcp/dhcpd.conf
   ddns-update-style none;

   default-lease-time 200000;
   max-lease-time 7200;

   subnet 10.0.0.0 netmask 255.255.255.0 {
   }
   subnet 10.0.0.0 netmask 255.255.255.0 {
      range 10.0.0.2 10.0.0.60;
   }
   ```

2. Restart the `dhcpd` service:

   ```
   cumulus@switch:~$ sudo systemctl restart dhcpd6.service
   ```

{{< /tab >}}
{{< tab "IPv6 ">}}

1. Edit the `/etc/dhcp/dhcpd6.conf` file to set the lease time (in seconds):

   ```
   cumulus@switch:~$ sudo nano /etc/dhcp/dhcpd6.conf
   ddns-update-style none;

   default-lease-time 200000;
   max-lease-time 7200;

   subnet6 2001:db8:100::/64 {
   }
   subnet6 2001:db8:1::/64 {
       range 2001:db8:1::100 2001:db8:1::200;
   }
   ```

2. Restart the `dhcpd6` service:

   ```
   cumulus@switch:~$ sudo systemctl restart dhcpd6.service
   ```

{{< /tab >}}
{{< /tabs >}}

{{< /tab >}}
{{< /tabs >}}

### Ping Check

Configure the DHCP server to ping the address to be assigned to a client before issuing the IP address. If no response is received, the IP address is delivered; otherwise the IP address is abandoned and no response is sent to the client.

{{< tabs "TabID359 ">}}
{{< tab "CUE Commands ">}}

{{< tabs "TabID362 ">}}
{{< tab "IPv4 ">}}

```
cumulus@switch:~$ cl set system dhcp-server pool 10.1.10.0/24 ping-check on
```

{{< /tab >}}
{{< tab "IPv6 ">}}

```
cumulus@switch:~$ cl set system dhcp-server6 pool 10.1.10.0/24 ping-check on
```

{{< /tab >}}
{{< /tabs >}}

{{< /tab >}}
{{< /tabs >}}

### Assign Port-based IP Addresses

You can assign an IP address and other DHCP options based on physical location or port regardless of MAC address to clients that are attached directly to the Cumulus Linux switch through a switch port. This is helpful when swapping out switches and servers; you can avoid the inconvenience of collecting the MAC address and sending it to the network administrator to modify the DHCP server configuration.

{{< tabs "TabID426 ">}}
{{< tab "CUE Commands ">}}

{{< tabs "TabID429 ">}}
{{< tab "IPv4 ">}}

```
cumulus@switch:~$ cl set system dhcp-server static server1 ip-address 10.0.0.2
cumulus@switch:~$ cl set system dhcp-server static server1 interface swp1
```

{{< /tab >}}
{{< tab "IPv6 ">}}

```
cumulus@switch:~$ cl set system dhcp-server6 static server1 ip-address 2001:db8:1::100
cumulus@switch:~$ cl set system dhcp-server6 static server1 interface swp1
```

{{< /tab >}}
{{< /tabs >}}

{{< /tab >}}
{{< tab "Linux Commands ">}}

{{< tabs "TabID449 ">}}
{{< tab "IPv4 ">}}

1. Edit the `/etc/dhcp/dhcpd.conf` file and add the interface name `ifname` to assign an IP address through DHCP. The following provides an example:

   ```
   cumulus@switch:~$ sudo nano /etc/dhcp/dhcpd.conf
   ...
   host myhost {
       ifname "swp1" ;
       fixed-address 10.0.0.10 ;
   }
   ...
   ```

2. Restart the `dhcpd` service:

   ```
   cumulus@switch:~$ sudo systemctl restart dhcpd.service
   ```

{{< /tab >}}
{{< tab "IPv6 ">}}

1. Edit the `/etc/dhcp/dhcpd6.conf` file and add the interface name `ifname` to assign an IP address through DHCP. The following provides an example:

   ```
   cumulus@switch:~$ sudo nano /etc/dhcp/dhcpd6.conf
   ...
   host myhost {
       ifname "swp1" ;
       fixed-address 10.0.0.10 ;
   }
   ...
   ```

2. Restart the `dhcpd6` service:

   ```
   cumulus@switch:~$ sudo systemctl restart dhcpd6.service
   ```

{{< /tab >}}
{{< /tabs >}}

{{< /tab >}}
{{< /tabs >}}

## Troubleshooting

To show the current DHCP server settings, run the `cl show system dhcp-server` command.

The DHCP server determines if a DHCP request is a relay or a non-relay DHCP request. Run the following command to see the DHCP request:

```
cumulus@server02:~$ sudo tail /var/log/syslog | grep dhcpd
2016-12-05T19:03:35.379633+00:00 server02 dhcpd: Relay-forward message from 2001:db8:101::1 port 547, link address 2001:db8:101::1, peer address fe80::4638:39ff:fe00:3
2016-12-05T19:03:35.380081+00:00 server02 dhcpd: Advertise NA: address 2001:db8:1::110 to client with duid 00:01:00:01:1f:d8:75:3a:44:38:39:00:00:03 iaid = 956301315 valid for 600 seconds
2016-12-05T19:03:35.380470+00:00 server02 dhcpd: Sending Relay-reply to 2001:db8:101::1 port 547
```
