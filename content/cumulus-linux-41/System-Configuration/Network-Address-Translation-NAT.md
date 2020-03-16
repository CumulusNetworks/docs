---
title: Network Address Translation - NAT
author: Cumulus Networks
weight: 225
toc: 3
---
Network Address Translation (NAT) enables your network to use one set of IP addresses for internal traffic and a second set of addresses for external traffic.

NAT was designed to overcome addressing problems due to the explosive growth of the Internet. In addition to preventing the depletion of IPv4 addresses, NAT enables you to use the private address space internally and still have a way to access the Internet, which increases security by hiding your internal network topology and private addresses.

Cumulus Linux supports both static NAT and dynamic NAT. Static NAT provides a permanent mapping between one private IP address and a single public address. Dynamic NAT maps private IP addresses to public addresses; these public IP addresses come from a pool. The dynamic translations are created as needed and dynamically, so that a large number of private addresses can share a smaller pool of public addresses.

Static and dynamic NAT both support:

- Basic NAT, which only translates the IP address in the packet: the source IP address in the outbound direction and the destination IP address in the inbound direction.
- PAT, which translates both the IP address and layer 4 port: the source IP address and port in the outbound direction and the destination IP address and port in the inbound direction.

The following illustratration shows a basic NAT configuration.

{{< img src = "/images/cumulus-linux/nat-example.png" >}}

{{%notice note%}}

- NAT is supported on physical interfaces and bond interfaces only.
- Dynamic NAT/PAT is supported on Broadcom Trident3 X7 and Mellanox Spectrum-2 switches only.
- IPv6 to IPv4 translation is not supported.
- Multicast traffic is not supported.
- NAT is *not* supported in an EVPN configuration.

{{%/notice%}}

## Static NAT

Static NAT provides a one-to-one mapping between a private IP address inside your network and a public IP address. For example, if you have a web server with the private IP address 10.0.0.10 and you want a remote host to be able to make a request to the web server using the IP address 192.168.1.3, you must configure a static NAT mapping between the two IP addresses.

Static NAT entries do not time out from the translation table.

### Enable Static NAT

To enable static NAT, edit the `/etc/cumulus/switchd.conf` file and uncomment the `nat.static_enable = TRUE` option:

```
cumulus@switch:~$ sudo nano /etc/cumulus/switchd.conf
...
# NAT configuration
# Enables NAT
nat.static_enable = TRUE
...
```

Restart `switchd` with the `sudo systemctl restart switchd.service` command.

{{%notice note%}}

Other options in the NAT configuration section of the switchd.conf file, such as nat.age_poll_interval and nat.table_size are dynamic NAT configuration options and are currently not supported.

{{%/notice%}}

### Configure Static NAT

To configure static NAT, create a rule that matches a source or destination IP address, protocol, layer 4 port (optional), and interface (optional) and translate for external use.

{{%notice note%}}

The protocol is required. Static NAT supports TCP, ICMP, and UDP packets.

{{%/notice%}}

To create rules, you can use either NCLU or cl-acltool.

<details>

<summary>NCLU Commands</summary>

Use the following NCLU commands:

**NAT**

```
net add nat static snat|dnat <protocol> <ip-address> [out-interface|in-interface <interface>] translate <ip-address>
```

**PAT**

```
net add nat static snat|dnat <protocol> <ip-address> <port>  [out-interface|in-interface <interface>] translate <ip-address> <port>
```

Where:

- `snat` is the source NAT
- `dnat` is the destination NAT
- `out-interface` is the outbound interface for `snat`
- `in-interface` is the inbound interface for `dnat`

**Command Examples**

The following rule matches TCP packets with source IP address 10.0.01 and translates the IP address to 192.168.1.3:

```
cumulus@switch:~$ net add nat static snat tcp 10.0.0.1 translate 192.168.1.3
cumulus@switch:~$ net pending
cumulus@switch:~$ net commit
```

The following rule matches ICMP packets with destination IP address 192.168.1.3 on interface swp51 and translates the IP address to 10.0.0.1

```
cumulus@switch:~$ net add nat static dnat icmp 192.168.1.3 in-interface swo51 translate 10.0.0.1
```

The following rule matches UDP packets with source IP address 10.0.0.1 and source port 5000, and translates the IP address to 192.168.1.3 and the port to 6000.

```
cumulus@switch:~$ net add nat static snat udp 10.0.0.1 5000 translate 192.168.1.3 6000
cumulus@switch:~$ net pending
cumulus@switch:~$ net commit
```

The following rule matches UDP packets with destination IP address 192.168.1.3 and destination port 6000 on interface swp51, and translates the IP address to 10.0.0.1 and the port to 5000:
cumulus@switch:~$ net add nat static dnat udp 192.168.1.3 6000 in-interface swp51 translate 10.0.0.1 5000

```
cumulus@switch:~$ net pending
cumulus@switch:~$ net commit
```

To delete a static rule, run the `net del` command. For example:

```
cumulus@switch:~$ net del nat static snat tcp 10.0.0.1 translate 192.168.1.3
cumulus@switch:~$ net pending
cumulus@switch:~$ net commit
```

</details>

<details>

<summary>cl-acltool </summary>

To add NAT rules using `cl-acltool`, either edit an existing file in the `/etc/cumulus/acl/policy.d` directory and add rules under `[iptables]` or create a new file in the `/etc/cumulus/acl/policy.d` directory and add rules under an `[iptables]` section. For example:

```
cumulus@switch:~$ sudo nano /etc/cumulus/acl/policy.d/60_nat.rules
[iptables]

 #Add rule
 ```

**Example Rules**

The following rule matches TCP packets with source IP address 10.0.01 and translates the IP address to 192.168.1.3:

```
-t nat -A POSTROUTING -s 10.0.0.1 -p tcp -j SNAT --to-source 192.168.1.3
```

The following rule matches ICMP packets with destination IP address 192.168.1.3 on interface swp51 and translates the IP address to 10.0.0.1

```
-t nat -A PREROUTING -d 192.168.1.3 -p icmp --in-interface swp51 -j DNAT --to-destination 10.0.0.1
```

The following rule matches UDP packets with source IP address 10.0.0.1 and source port 5000, and translates the IP address to 192.168.1.3 and the port to 6000.

```
-t nat -A POSTROUTING -s 10.0.0.1 -p udp --sport 5000 -j SNAT --to-source 192.168.1.3:6000
```

The following rule matches UDP packets with destination IP address 192.168.1.3 and destination port 6000 on interface swp51, and translates the IP address to 10.0.0.1 and the port to 5000.

```
-t nat -A PREROUTING -d 192.168.1.3 -p udp --dport 6000 --in-interface swp51  -j DNAT --to-destination 10.0.0.1:5000
```

To delete a static NAT rule, remove the rule from the policy file in the  `/etc/cumulus/acl/policy.d` directory, then run the `sudo cl-acltool -i command`.

</details>

## Dynamic NAT

Dynamic NAT maps private IP addresses to multiple public IP addresses or to a single public IP address and a range of ports. IP addresses are assigned from a pool of addresses dynamically. When entries are released after a period of inactivity, new incoming connections are dynamically mapped to the freed up addresses and ports.

### Enable Dynamic NAT

To enable dynamic NAT, edit the `/etc/cumulus/switchd.conf` file and uncomment the `nat.dynamic_enable = TRUE` option:

```
cumulus@switch:~$ sudo nano /etc/cumulus/switchd.conf
...
# NAT configuration
# Enables NAT
nat.dynamic_enable = TRUE
...
```

Restart `switchd` with the `sudo systemctl restart switchd.service` command.

{{%notice note%}}

Other dynamic NAT options in the NAT configuration section of the `switchd.conf` file, such as `nat.age_poll_interval` and `nat.table_size` are currently not supported.

{{%/notice%}}

### Configure Dynamic NAT

To configure dynamic NAT, create a rule that matches an IP address in CIDR notation, a protocol, and interface (optional) and translates the address to a public IP address range, or to a public IP address and port range.

{{%notice note%}}

The protocol is required. Dynamic NAT supports TCP and UDP packets.

{{%/notice%}}

<details>

<summary>NCLU Commands</summary>

Use the following NCLU commands:

**NAT**

```
net add nat dynamic snat|dnat <protocol> source-ip <ipv4-address/prefixlen>|destination-ip <ip-address/prefixlen> out-interface|in-interface translate <ip-address-range>
```

**PAT**

```
net add nat dynamic snat|dnat <protocol> source-ip <ip-address/prefixlen>|destination-ip <ip-address/prefixlen> out-interface|in-interface translate <ip-address> <port-range>
```

Where:

- `snat` is the source NAT
- `dnat` is the destination NAT
- `out-interface` is the outbound interface for `snat`
- `in-interface` is the inbound interface for `dnat`

**Example Commands**

The following rule matches TCP packets with source IP address 10.0.0.0/24 on outbound interface swp5 and translates the address dynamically to an IP address in the range 192.168.1.3-192.168.1.100

```
cumulus@switch:~$ net add nat dynamic snat tcp source-ip 10.0.0.0/24 out-interface swp5 translate 192.168.1.3-192.168.1.100
cumulus@switch:~$ net pending
cumulus@switch:~$ net commit
```

The following rule matches UDP packets with source IP address 10.0.0.0/24 and destination IP address 172.16.0.0/24, and translates the address dynamically to IP address 192.168.1.3 with layer 4 ports in the range 1024-1200.

```
cumulus@switch:~$ net add nat dynamic snat udp source-ip 10.0.0.0/24 destination-ip 172.16.0.0/24 translate 192.168.1.3 1024-1200
cumulus@switch:~$ net pending
cumulus@switch:~$ net commit
```

The following rule matches TCP packets with source IP address 10.0.0.0/24 and translates the address dynamically to IP address 192.168.1.3 with layer 4 ports in the range 1024-1200

```
cumulus@switch:~$ net add nat dynamic snat tcp source-ip 10.0.0.0/24  translate 192.168.1.3 1024-1200
cumulus@switch:~$ net pending
cumulus@switch:~$ net commit
```

To delete a dynamic rule, run the net del command. For example:

```
cumulus@switch:~$ net del nat dynamic snat tcp source-ip 10.0.0.0/24 translate 192.168.1.3-192.168.1.100
cumulus@switch:~$ net pending
cumulus@switch:~$ net commit
```

</details>

<details> 

<summary>cl-acltool Commands</summary>

To add NAT rules using `cl-acltool`, either edit an existing file in the `/etc/cumulus/acl/policy.d` directory and add rules under `[iptables]` or create a new file in the `/etc/cumulus/acl/policy.d` directory and add rules under an `[iptables]` section. For example:

```
cumulus@switch:~$ sudo nano /etc/cumulus/acl/policy.d/60_nat.rules
[iptables]

 #Add rule
```

**Example Rules**

The following rule matches TCP packets with source IP address 10.0.0.0/24 on outbound interface swp5 and translates the address dynamically to an IP address in the range 192.168.1.3-192.168.1.100.

```
-t nat -A POSTROUTING -s 10.0.0.0/24 --out-interface swp5 -p tcp -j SNAT --to-source 192.168.1.3-192.168.1.100
```

The following rule matches UDP packets with source IP address 10.0.0.0/24 and destination IP address 172.16.0.0/24, and translates the addresses dynamically to IP address 192.168.1.3 with layer 4 ports in the range 1024-1200.

```
-t nat -A POSTROUTING -s 10.0.0.0/24 -d 172.16.0.0/24 -p udp -j SNAT --to-source 192.168.1.3:1024-1200
```

The following rule matches TCP packets with source IP address 10.0.0.0/24 and translates the address dynamically to IP address 192.168.1.3 using layer 4 ports in the range 1024-1200.

```
-t nat -A POSTROUTING -s 10.0.0.0/24 -p tcp -j SNAT --to-source 192.168.1.3:1024-1200
```

To delete a dynamic NAT rule, remove the rule from the policy file in the  `/etc/cumulus/acl/policy.d` directory, then run the `sudo cl-acltool -i` command.

</details>

## Show Configured NAT Rules

To see the NAT rules configured on the switch, run the `sudo iptables -t nat -v -L` or the
`sudo ccl-acltool -L ip -v` command. For example:

```
cumulus@switch:~$ sudo iptables -t nat -v -L
...
Chain POSTROUTING (policy ACCEPT 27 packets, 3249 bytes)
 pkts bytes target   prot opt in   out   source      destination
    0     0 SNAT     tcp --  any  any   10.0.0.1    anywhere     to:192.168.1.3
```
