---
title: DHCP Servers
author: NVIDIA
weight: 350
toc: 3
---
A DHCP server automatically provides and assigns IP addresses and other network parameters to client devices. It relies on <span class="a-tooltip">[DHCP](## "Dynamic Host Configuration Protocol")</span> to respond to broadcast requests from clients.

{{%notice note%}}
If you intend to run the `dhcpd` service within a {{<link url="Virtual-Routing-and-Forwarding-VRF" text="VRF">}}, including the {{<link url="Management-VRF" text="management VRF">}}, follow {{<link url="Management-VRF/#run-services-within-the-management-vrf" text="these steps">}}.
{{%/notice%}}

## Basic Configuration

This section shows you how to configure a DHCP server using the following topology, where the DHCP server is a switch running Cumulus Linux.

{{< img src = "/images/cumulus-linux/dhcp-server-topology.png" >}}

To configure the DHCP server on a Cumulus Linux switch:
- Create a DHCP pool by providing a pool ID. The ID is an IPv4 or IPv6 prefix.
- Provide a name for the pool (optional).
- Provide the IP address of the DNS Server you want to use in this pool. You can assign multiple DNS servers.
- Provide the domain name you want to use for this pool for name resolution (optional).
- Define the range of IP addresses available for assignment.
- Provide the default gateway IP address (optional).

In addition, you can configure a static IP address for a resource, such as a server or printer:
- Create an ID for the static assignment. This is typically the name of the resource.
- Provide the static IP address you want to assign to this resource.
- Provide the MAC address of the resource to which you want to assign the IP address. Instead of the MAC address, you can set the interface name for the static assignment (IPv4 only); for example swp1.

{{%notice note%}}
- To configure static IP address assignments, you must first configure a pool.
- You can set the DNS server IP address and domain name globally or specify different DNS server IP addresses and domain names for different pools.
{{%/notice%}}

The following example configures the `storage-servers` pool with DNS and static DHCP assignments for `server1` and `server2`.

{{< tabs "TabID27 ">}}
{{< tab "NVUE Commands ">}}

{{< tabs "TabI32 ">}}
{{< tab "IPv4 ">}}

```
cumulus@switch:~$ nv set service dhcp-server default pool 10.1.10.0/24 pool-name storage-servers
cumulus@switch:~$ nv set service dhcp-server default pool 10.1.10.0/24 domain-name example.com
cumulus@switch:~$ nv set service dhcp-server default pool 10.1.10.0/24 domain-name-server 192.168.200.53
cumulus@switch:~$ nv set service dhcp-server default pool 10.1.10.0/24 range 10.1.10.100 to 10.1.10.199
cumulus@switch:~$ nv set service dhcp-server default pool 10.1.10.0/24 gateway 10.1.10.1
cumulus@switch:~$ nv set service dhcp-server default static server1
cumulus@switch:~$ nv set service dhcp-server default static server1 ip-address 10.0.0.2
cumulus@switch:~$ nv set service dhcp-server default static server1 mac-address 44:38:39:00:01:7e
cumulus@switch:~$ nv set service dhcp-server default static server2
cumulus@switch:~$ nv set service dhcp-server default static server2 ip-address 10.0.0.3
cumulus@switch:~$ nv set service dhcp-server default static server2 ifname swp1
cumulus@switch:~$ nv config apply
```

To set the DNS server IP address and domain name globally, use the `nv set service dhcp-server <vrf> domain-name-server <address>` and `nv set service dhcp-server <vrf> domain-name <domain>` commands.

To set the interface name for the static assignment, run the `nv set service dhcp-server <vrf> static <server> ifname` command.

{{< /tab >}}
{{< tab "IPv6 ">}}

```
cumulus@switch:~$ nv set service dhcp-server6 default pool 2001:db8::1/128 
cumulus@switch:~$ nv set service dhcp-server6 default pool 2001:db8::1/128 pool-name storage-servers
cumulus@switch:~$ nv set service dhcp-server6 default pool 2001:db8::1/128 domain-name-server 2001:db8:100::64
cumulus@switch:~$ nv set service dhcp-server6 default pool 2001:db8::1/128 domain-name example.com
cumulus@switch:~$ nv set service dhcp-server6 default pool 2001:db8::1/128 range 2001:db8:1::100 to 2001:db8:1::199 
cumulus@switch:~$ nv set service dhcp-server6 default static server1
cumulus@switch:~$ nv set service dhcp-server6 default static server1 ip-address 2001:db8:1::100
cumulus@switch:~$ nv set service dhcp-server6 default static server1 mac-address 44:38:39:00:01:7e
cumulus@switch:~$ nv config apply
```

To set the DNS server IP address and domain name globally, use the `nv set service dhcp-server6 <vrf> domain-name-server <address>` and `nv set service dhcp-server6 <vrf> domain-name <domain>` commands.

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

To set the DNS server IP address and domain name globally, add the DNS server IP address and domain name before the pool information in the `/etc/dhcp/dhcpd.conf` file. For example:

```
cumulus@switch:~$ sudo nano /etc/dhcp/dhcpd.conf
authoritative;
option domain-name servers;
option domain-name-servers 192.168.200.51;
subnet 10.1.10.0 netmask 255.255.255.0 {
   option routers 10.10.10.1;
   default-lease-time 3600;
   max-lease-time 3600;
...
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

To set the DNS server IP address and domain name globally, add the DNS server IP address and domain name before the pool information in the `/etc/dhcp/dhcpd6.conf` file. For example:

```
cumulus@switch:~$ sudo nano /etc/dhcp/dhcpd6.conf
authoritative;
option domain-name servers;
option domain-name-servers 2001:db8:100::64;
subnet6 2001:db8::1/128 {
   option routers 2001:db8::a0a:0a01;
   default-lease-time 3600;
   max-lease-time 3600;
...
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

You can set the network address lease time assigned to DHCP clients. You can specify a number between 180 and 31536000. The default lease time is 3600 seconds.

{{< tabs "TabID206 ">}}
{{< tab "NVUE Commands ">}}

{{< tabs "TabID209 ">}}
{{< tab "IPv4 ">}}

```
cumulus@switch:~$ nv set service dhcp-server default pool 10.1.10.0/24 lease-time 200000
cumulus@switch:~$ nv config apply
```

{{< /tab >}}
{{< tab "IPv6 ">}}

```
cumulus@switch:~$ nv set service dhcp-server6 default pool 2001:db8::1/128 lease-time 200000
cumulus@switch:~$ nv config apply
```

{{< /tab >}}
{{< /tabs >}}

{{< /tab >}}
{{< tab "Linux Commands ">}}

{{< tabs "TabID231 ">}}
{{< tab "IPv4 ">}}

1. Edit the `/etc/dhcp/dhcpd.conf` file to set the lease time (in seconds):

   ```
   cumulus@switch:~$ sudo nano /etc/dhcp/dhcpd.conf
   authoritative;
   subnet 10.1.10.0 netmask 255.255.255.0 {
      option domain-name-servers 192.168.200.53;
      option domain-name example.com;
      option routers 10.1.10.1;
      default-lease-time 200000;
      max-lease-time 200000;
      default-url ;
   pool {
          range 10.1.10.100 10.1.10.199;
          }
   }
   ```

2. Restart the `dhcpd` service:

   ```
   cumulus@switch:~$ sudo systemctl restart dhcpd.service
   ```

{{< /tab >}}
{{< tab "IPv6 ">}}

1. Edit the `/etc/dhcp/dhcpd6.conf` file to set the lease time (in seconds):

   ```
   cumulus@switch:~$ sudo nano /etc/dhcp/dhcpd6.conf
   authoritative;
   subnet6 2001:db8::1/128 {
      option domain-name-servers 2001:db8:100::64;
      option domain-name example.com;
      option routers 2001:db8::a0a:0a01;
      default-lease-time 200000;
      max-lease-time 200000;
      default-url ;
      pool {
          range6 2001:db8:1::100 2001:db8:1::199;
      }
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

Configure the DHCP server to ping the address you want to assign to a client before issuing the IP address. If there is no response, DHCP delivers the IP address; otherwise, it attempts the next available address in the range.

{{< tabs "TabID295 ">}}
{{< tab "NVUE Commands ">}}

{{< tabs "TabID298 ">}}
{{< tab "IPv4 ">}}

```
cumulus@switch:~$ nv set service dhcp-server default pool 10.1.10.0/24 ping-check on
cumulus@switch:~$ nv config apply
```

{{< /tab >}}
{{< tab "IPv6 ">}}

```
cumulus@switch:~$ nv set service dhcp-server6 default pool 2001:db8::1/128 ping-check on
cumulus@switch:~$ nv config apply
```

{{< /tab >}}
{{< /tabs >}}

{{< /tab >}}
{{< tab "Linux Commands ">}}

{{< tabs "TabID318 ">}}
{{< tab "IPv4 ">}}

1. Edit the `/etc/dhcp/dhcpd.conf` file to add `ping-check true;`:

   ```
   cumulus@switch:~$ sudo nano /etc/dhcp/dhcpd.conf
   authoritative;
   subnet 10.1.10.0 netmask 255.255.255.0 {
      option domain-name-servers 192.168.200.53;
      option domain-name example.com;
      option routers 10.1.10.1;
      default-lease-time 200000;
      max-lease-time 200000;
      ping-check true;
      default-url ;
   pool {
          range 10.1.10.100 10.1.10.199;
          }
   }
   ```
   
2. Restart the `dhcpd` service:

   ```
   cumulus@switch:~$ sudo systemctl restart dhcpd.service
   ```

{{< /tab >}}
{{< tab "IPv6 ">}}

1. Edit the `/etc/dhcp/dhcpd6.conf` file to add `ping-check true;`:

   ```
   cumulus@switch:~$ sudo nano /etc/dhcp/dhcpd6.conf
   authoritative;
   subnet6 2001:db8::1/128 {
      option domain-name-servers 2001:db8:100::64;
      option domain-name example.com;
      option routers 2001:db8::a0a:0a01;
      default-lease-time 200000;
      max-lease-time 200000;
      ping-check true;
      default-url ;
      pool {
          range6 2001:db8:1::100 2001:db8:1::199;
      }
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

<!-- vale off -->
<!-- Vale issue #253 -->
### Assign Port-based IP Addresses
<!-- vale on -->

You can assign an IP address and other DHCP options based on physical location or port regardless of MAC address to clients that attach directly to the Cumulus Linux switch through a switch port. This is helpful when swapping out switches and servers; you can avoid the inconvenience of collecting the MAC address and sending it to the network administrator to modify the DHCP server configuration.

{{< tabs "TabID384 ">}}
{{< tab "NVUE Commands ">}}

{{< tabs "TabID387 ">}}
{{< tab "IPv4 ">}}

```
Cumulus Linux does not provide NVUE commands for this setting.
```

{{< /tab >}}
{{< tab "IPv6 ">}}

```
Cumulus Linux does not provide NVUE commands for this setting.
```

{{< /tab >}}
{{< /tabs >}}

{{< /tab >}}
{{< tab "Linux Commands ">}}

{{< tabs "TabID409 ">}}
{{< tab "IPv4 ">}}

1. Edit the `/etc/dhcp/dhcpd.conf` file to add the interface and IP address:

   ```
   cumulus@switch:~$ sudo nano /etc/dhcp/dhcpd.conf
   ...
   authoritative;
   option cumulus-provision-url code 239 = text;
   
   subnet 10.0.0.0 netmask 255.255.255.0 {
       option domain-name-servers 192.168.200.53;
       option domain-name "example.com";
       option routers 10.0.0.1;
       default-lease-time 3600;
       max-lease-time 3600;
       ping-check off;
   
       pool {
           range 10.0.0.2 10.0.0.254;
       }
   }
   group {
       host myhost {
           ifname "swp1" ;
           fixed-address 10.0.0.2 ;
       }
   }
   ...
   ```

2. Restart the `dhcpd` service:

   ```
   cumulus@switch:~$ sudo systemctl restart dhcpd.service
   ```

{{< /tab >}}
{{< tab "IPv6 ">}}

1. Edit the `/etc/dhcp/dhcpd6.conf` file to add the interface and IP address:

   ```
   cumulus@switch:~$ sudo nano /etc/dhcp/dhcpd6.conf
   ...
   host myhost {
       ifname "swp1" ;
       fixed-address 2001:db8:1::100 ;
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

To show the current DHCP server settings, run the `nv show service dhcp-server` command:

```
cumulus@leaf01:mgmt:~$ nv show service dhcp-server
           Summary
---------  ------------------
+ default  interface:   "swp1
  default  pool: 10.1.10.0/24
  default  static:    server1
```

The DHCP server determines if a DHCP request is a relay or a non-relay DHCP request. Run the following command to see the DHCP request:

```
cumulus@server02:~$ sudo tail /var/log/syslog | grep dhcpd
2016-12-05T19:03:35.379633+00:00 server02 dhcpd: Relay-forward message from 2001:db8:101::1 port 547, link address 2001:db8:101::1, peer address fe80::4638:39ff:fe00:3
2016-12-05T19:03:35.380081+00:00 server02 dhcpd: Advertise NA: address 2001:db8:1::110 to client with duid 00:01:00:01:1f:d8:75:3a:44:38:39:00:00:03 iaid = 956301315 valid for 600 seconds
2016-12-05T19:03:35.380470+00:00 server02 dhcpd: Sending Relay-reply to 2001:db8:101::1 port 547
```
## Considerations

DHCP packets received on bridge ports and sent to the CPU for processing cause the RX_DROP counter to increment on the interface.
