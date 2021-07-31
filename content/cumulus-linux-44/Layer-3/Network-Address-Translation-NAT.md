---
title: Network Address Translation - NAT
author: NVIDIA
weight: 980
toc: 3
---
Network Address Translation (NAT) enables your network to use one set of IP addresses for internal traffic and a second set of addresses for external traffic.

NAT was designed to overcome addressing problems due to the explosive growth of the Internet. In addition to preventing the depletion of IPv4 addresses, NAT enables you to use the private address space internally and still have a way to access the Internet.

Cumulus Linux supports both static NAT and dynamic NAT. Static NAT provides a permanent mapping between one private IP address and a single public address. Dynamic NAT maps private IP addresses to public addresses; these public IP addresses come from a pool. The translations are created as needed  dynamically, so that a large number of private addresses can share a smaller pool of public addresses.

Static and dynamic NAT both support:

- Basic NAT, which only translates the IP address in the packet: the source IP address in the outbound direction and the destination IP address in the inbound direction.
- Port Address Translation (PAT), which translates both the IP address and layer 4 port: the source IP address and port in the outbound direction and the destination IP address and port in the inbound direction.

Static NAT supports double NAT (also known as twice NAT) where both the source and destination IP addresses are translated as a packet crosses address realms. Double NAT is used typically when address space in a private network overlaps with IP addresses in the public space.

The following illustration shows a basic NAT configuration.

{{< img src = "/images/cumulus-linux/nat-example.png" >}}

{{%notice note%}}
- NAT is supported on NVIDIA Spectrum-2 and Spectrum-3 switches only.
- NAT is supported on physical interfaces and bond interfaces and only in the default VRF.
- IPv6 to IPv4 translation is not supported.
- Multicast traffic is not supported.
- NAT is *not* supported in an EVPN configuration.
{{%/notice%}}

## Static NAT

Static NAT provides a one-to-one mapping between a private IP address inside your network and a public IP address. For example, if you have a web server with the private IP address 10.0.0.10 and you want a remote host to be able to make a request to the web server using the IP address 172.30.58.80, you must configure a static NAT mapping between the two IP addresses.

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

Then restart `switchd`.

{{<cl/restart-switchd>}}

{{%notice note%}}
Other options in the NAT configuration section of the `switchd.conf` file, such as `nat.age_poll_interval` and `nat.table_size` are dynamic NAT configuration options and are not supported with static NAT.
{{%/notice%}}

### Configure Static NAT

For static **NAT**, create a rule that matches a source or destination IP address and translates the IP address to a public IP address.

For static **PAT**, create a rule that matches a source or destination IP address together with the layer 4 port and translates the IP address and port to a public IP address and port.

For NVIDIA Spectrum-2 switches, you can include the outgoing or incoming interface.

To create rules, you can use either NCLU or `cl-acltool`.

{{< tabs "TabID68 ">}}
{{< tab "NCLU Commands ">}}

Use the following NCLU commands:

**NAT**

```
net add nat static snat|dnat <protocol> <ip-address> [out-interface|in-interface <interface>] translate <ip-address>
```

**PAT**

```
net add nat static snat|dnat <protocol> <ip-address> <port> [out-interface|in-interface <interface>] translate <ip-address> <port>
```

Where:

- `snat` is the source NAT
- `dnat` is the destination NAT
- `protocol` is TCP, ICMP, or UDP. The protocol is required.
- `out-interface` is the outbound interface for `snat` (NVIDIA Spectrum-2 switches only)
- `in-interface` is the inbound interface for `dnat` (NVIDIA Spectrum-2 switches only)

**Command Examples**

The following rule matches TCP packets with source IP address 10.0.0.1 and translates the IP address to 172.30.58.80:

```
cumulus@switch:~$ net add nat static snat tcp 10.0.0.1 translate 172.30.58.80
cumulus@switch:~$ net pending
cumulus@switch:~$ net commit
```

The following rule matches ICMP packets with destination IP address 172.30.58.80 on interface swp51 and translates the IP address to 10.0.0.1

```
cumulus@switch:~$ net add nat static dnat icmp 172.30.58.80 in-interface swp51 translate 10.0.0.1
cumulus@switch:~$ net pending
cumulus@switch:~$ net commit
```

The following rule matches UDP packets with source IP address 10.0.0.1 and source port 5000, and translates the IP address to 172.30.58.80 and the port to 6000.

```
cumulus@switch:~$ net add nat static snat udp 10.0.0.1 5000 translate 172.30.58.80 6000
cumulus@switch:~$ net pending
cumulus@switch:~$ net commit
```

The following rule matches UDP packets with destination IP address 172.30.58.80 and destination port 6000 on interface swp51, and translates the IP address to 10.0.0.1 and the port to 5000:

```
cumulus@switch:~$ net add nat static dnat udp 172.30.58.80 6000 in-interface swp51 translate 10.0.0.1 5000
cumulus@switch:~$ net pending
cumulus@switch:~$ net commit
```

The following *double NAT* rule matches both the source and destination IP addresses of incoming and outgoing ICMP packets:  
- For outgoing messages, NAT changes the inside local IP address 172.16.10.2 to the inside global IP address 130.1.100.10 and the outside local IP address 26.26.26.26 to the outside global IP address 140.1.1.2.
- For incoming messages, NAT changes the inside global IP address 130.1.100.10 to the inside local IP address 172.16.10.2 and the outside global IP address 140.1.1.2 to the outside local IP address 26.26.26.26.

```
cumulus@switch:~$ net add nat static snat icmp 172.16.10.2 translate 130.1.100.100
cumulus@switch:~$ net add nat static dnat icmp 26.26.26.26 translate 140.1.1.2
cumulus@switch:~$ net add nat static snat icmp 140.1.1.2 translate 26.26.26.26
cumulus@switch:~$ net add nat static dnat icmp 130.1.100.100 translate 172.16.10.2 
cumulus@switch:~$ net pending
cumulus@switch:~$ net commit 
```

To delete a static rule, run the `net del` command. For example:

```
cumulus@switch:~$ net del nat static snat tcp 10.0.0.1 translate 172.30.58.80
cumulus@switch:~$ net pending
cumulus@switch:~$ net commit
```

{{< /tab >}}
{{< tab "cl-acltool Commands ">}}

To add NAT rules using `cl-acltool`, either edit an existing file in the `/etc/cumulus/acl/policy.d` directory and add rules under `[iptables]` or create a new file in the `/etc/cumulus/acl/policy.d` directory and add rules under an `[iptables]` section. For example:

```
cumulus@switch:~$ sudo nano /etc/cumulus/acl/policy.d/60_nat.rules
[iptables]

 #Add rule
 ```

**Example Rules**

The following rule matches TCP packets with source IP address 10.0.01 and translates the IP address to 172.30.58.80:

```
-t nat -A POSTROUTING -s 10.0.0.1 -p tcp -j SNAT --to-source 172.30.58.80
```

The following rule matches ICMP packets with destination IP address 172.30.58.80 on interface swp51 and translates the IP address to 10.0.0.1

```
-t nat -A PREROUTING -d 172.30.58.80 -p icmp --in-interface swp51 -j DNAT --to-destination 10.0.0.1
```

The following rule matches UDP packets with source IP address 10.0.0.1 and source port 5000, and translates the IP address to 172.30.58.80 and the port to 6000.

```
-t nat -A POSTROUTING -s 10.0.0.1 -p udp --sport 5000 -j SNAT --to-source 172.30.58.80:6000
```

The following rule matches UDP packets with destination IP address 172.30.58.80 and destination port 6000 on interface swp51, and translates the IP address to 10.0.0.1 and the port to 5000.

```
-t nat -A PREROUTING -d 172.30.58.80 -p udp --dport 6000 --in-interface swp51  -j DNAT --to-destination 10.0.0.1:5000
```

The following *double NAT* rule translates both the source and destination IP addresses of incoming and outgoing ICMP packets:  
- For outgoing messages, NAT changes the inside local IP address 172.16.10.2 to the inside global IP address 130.1.100.10 and the outside local IP address 26.26.26.26 to the outside global IP address 140.1.1.2.
- For incoming messages, NAT changes the inside global IP address 130.1.100.10 to the inside local IP address 172.16.10.2 and the outside global IP address 140.1.1.2 to the outside local IP address 26.26.26.26.

```
-t nat -A POSTROUTING -s 172.16.10.2 -p icmp -j SNAT --to-source 130.1.100.100 
-t nat -A PREROUTING -d 26.26.26.26 -p icmp -j DNAT --to-destination 140.1.1.2 
-t nat -A POSTROUTING -s 140.1.1.2 -p icmp -j SNAT --to-source 26.26.26.26 
-t nat -A PREROUTING -d 130.1.100.100 -p icmp -j DNAT --to-destination 172.16.10.2 
```

To delete a static NAT rule, remove the rule from the policy file in the  `/etc/cumulus/acl/policy.d` directory, then run the `sudo cl-acltool -i command`.

{{< /tab >}}
{{< /tabs >}}

## Dynamic NAT

Dynamic NAT maps private IP addresses and ports to a public IP address and port range or a public IP address range and port range. IP addresses are assigned from a pool of addresses dynamically. When entries are released after a period of inactivity, new incoming connections are dynamically mapped to the freed up addresses and ports.

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

Then restart `switchd`.

{{<cl/restart-switchd>}}

#### Optional Dynamic NAT Settings

The `/etc/cumulus/switchd.conf` file includes the following configuration options for dynamic NAT. Only change these options if dynamic NAT is enabled.
<!-- vale off -->
| Option | Description |
| ------ | ----------- |
| nat.age_poll_interval | The period of inactivity before `switchd` releases a NAT entry from the translation table.<br>The default value is 5 minutes. The minimum value is 1 minute. The maximum value is 24 hours.|
| nat.table_size | The maximum number of dynamic `snat` and `dnat` entries in the translation table. The default value is 1024.<br>NVIDIA Spectrum-2 switches support a maximum of 8192 entries. |
| nat.config_table_size | The maximum number of rules allowed (NCLU or cl-acltool).<br>The default value is 64. The minimum value is 64. The maximum value is 1024. |
<!-- vale on --> 
After you change any of the dynamic NAT configuration options, restart `switchd`.

{{<cl/restart-switchd>}}

### Configure Dynamic NAT

For dynamic **NAT**, create a rule that matches a IP address in CIDR notation and translates the address to a public IP address or IP address range.

For dynamic **PAT**, create a rule that matches an IP address in CIDR notation and translates the address to a public IP address and port range or an IP address range and port range. You can also match on an IP address in CIDR notation and port.

For NVIDIA Spectrum-2 switches, you can include the outgoing or incoming interface in the rule. See the examples below.

{{< tabs "TabID226 ">}}
{{< tab "NCLU Commands ">}}

Use the following NCLU commands:

**NAT**

```
net add nat dynamic snat|dnat <protocol> source-ip <ipv4-address/prefixlen>|destination-ip <ip-address/prefixlen> out-interface|in-interface translate <ipv4-address>|<ip-address-range>
```

**PAT**

```
net add nat dynamic snat|dnat <protocol> source-ip <ipv4-address/prefixlen>|destination-ip <ipv4-address/prefixlen> source-port <port>|destination-port <port> out-interface|in-interface translate <ipv4-address> <port-range>|<ipv4-address-range> <port-range>
```

Where:

- `snat` is the source NAT
- `dnat` is the destination NAT
- `protocol` is TCP, ICMP, or UDP. The protocol is required.
- `out-interface` is the outbound interface for `snat` (NVIDIA Spectrum-2 switches only)
- `in-interface` is the inbound interface for `dnat` (NVIDIA Spectrum-2 switches only)

**Example Commands**

The following rule matches TCP packets with source IP address in the range 10.0.0.0/24 on outbound interface swp5 and translates the address dynamically to an IP address in the range 172.30.58.0-172.30.58.80:

```
cumulus@switch:~$ net add nat dynamic snat tcp source-ip 10.0.0.0/24 out-interface swp5 translate 172.30.58.0-172.30.58.80
cumulus@switch:~$ net pending
cumulus@switch:~$ net commit
```

The following rule matches UDP packets with source IP address in the range 10.0.0.0/24 and translates the addresses dynamically to IP address 172.30.58.80 with layer 4 ports in the range 1024-1200:

```
cumulus@switch:~$ net add nat dynamic snat udp source-ip 10.0.0.0/24 translate 172.30.58.80 1024-1200
cumulus@switch:~$ net pending
cumulus@switch:~$ net commit
```

The following rule matches UDP packets with source IP address in the range 10.0.0.0/24 on source port 5000 and translates the addresses dynamically to IP address 172.30.58.80 with layer 4 ports in the range 1024-1200:

```
cumulus@switch:~$ net add nat dynamic snat udp source-ip 10.0.0.0/24 source-port 5000 translate 172.30.58.80 1024-1200
cumulus@switch:~$ net pending
cumulus@switch:~$ net commit
```

The following rule matches TCP packets with destination IP address in the range 10.1.0.0/24 and translates the address dynamically to IP address range 172.30.58.0-172.30.58.80 with layer 4 ports in the range 1024-1200:

```
cumulus@switch:~$ net add nat dynamic dnat tcp destination-ip 10.1.0.0/24 translate 172.30.58.0-172.30.58.80 1024-1200
cumulus@switch:~$ net pending
cumulus@switch:~$ net commit
```

The following rule matches ICMP packets with source IP address in the range 10.0.0.0/24 and destination IP address in the range 10.1.0.0/24, and translates the address dynamically to IP address range 172.30.58.0-172.30.58.80 with layer 4 ports in the range 1024-1200:

```
cumulus@switch:~$ net add nat dynamic snat icmp source-ip 10.0.0.0/24 destination-ip 10.1.0.0/24 translate 172.30.58.0-172.30.58.80 1024-1200
cumulus@switch:~$ net pending
cumulus@switch:~$ net commit
```

To delete a dynamic rule, run the `net del` command. For example:

```
cumulus@switch:~$ net del nat dynamic snat tcp source-ip 10.0.0.0/24 translate 172.30.58.0-172.30.58.80 1024-1200
cumulus@switch:~$ net pending
cumulus@switch:~$ net commit
```

{{< /tab >}}
{{< tab "cl-acltool Commands ">}}

To add NAT rules using `cl-acltool`, either edit an existing file in the `/etc/cumulus/acl/policy.d` directory and add rules under `[iptables]` or create a new file in the `/etc/cumulus/acl/policy.d` directory and add rules under an `[iptables]` section. For example:

```
cumulus@switch:~$ sudo nano /etc/cumulus/acl/policy.d/60_nat.rules
[iptables]

 #Add rule
```

**Example Rules**

The following rule matches TCP packets with source IP address in the range 10.0.0.0/24 on outbound interface swp5 and translates the address dynamically to an IP address in the range 172.30.58.0-172.30.58.80.

```
-t nat -A POSTROUTING -s 10.0.0.0/24 --out-interface swp5 -p tcp -j SNAT --to-source 172.30.58.0-172.30.58.80
```

The following rule matches UDP packets with source IP address in the range 10.0.0.0/24 and translates the addresses dynamically to IP address 172.30.58.80 with layer 4 ports in the range 1024-1200:

```
-t nat -A POSTROUTING -s 10.0.0.0/24 -p udp -j SNAT --to-source 172.30.58.80:1024-1200
```

The following rule matches UDP packets with source IP address in the range 10.0.0.0/24 on source port 5000 and translates the addresses dynamically to IP address 172.30.58.80 with layer 4 ports in the range 1024-1200:

```
-t nat -A POSTROUTING -s 10.0.0.0/24 -p udp --sport 5000 -j SNAT --to-source 172.30.58.80:1024-1200
```

The following rule matches TCP packets with destination IP address in the range 10.1.0.0/24 and translates the address dynamically to IP address range 172.30.58.0-172.30.58.80 with layer 4 ports in the range 1024-1200:

```
-t nat -A PREROUTING -d 10.1.0.0/24 -p tcp -j DNAT --to-destination 172.30.58.0-172.30.58.80:1024-1200
```

The following rule matches ICMP packets with source IP address in the range 10.0.0.0/24 and destination IP address in the range 10.1.0.0/24, and translates the address dynamically to IP address range 172.30.58.0-172.30.58.80 with layer 4 ports in the range 1024-1200:

```
-t nat -A POSTROUTING -s 10.0.0.0/24 -d 10.1.0.0/24 -p icmp -j SNAT --to-source 172.30.58.0-172.30.58.80:1024-1200
```

To delete a dynamic NAT rule, remove the rule from the policy file in the  `/etc/cumulus/acl/policy.d` directory, then run the `sudo cl-acltool -i` command.

{{< /tab >}}
{{< /tabs >}}

## Show Configured NAT Rules

To see the NAT rules configured on the switch, run the `sudo iptables -t nat -v -L` or the
`sudo cl-acltool -L ip -v` command. For example:

```
cumulus@switch:~$ sudo iptables -t nat -v -L -n
...
Chain POSTROUTING (policy ACCEPT 27 packets, 3249 bytes)
 pkts bytes target   prot opt in   out   source      destination
    0     0 SNAT     tcp --  any  any   10.0.0.1    anywhere     to:172.30.58.80
```

## Show Conntrack Flows

To see the currently active connection tracking (conntrack) flows, run the `sudo cat /proc/net/nf_conntrack` command. The hardware offloaded flows contain `[OFFLOAD]` in the output.

```
cumulus@switch:~$ sudo cat /proc/net/nf_conntrack
ipv4     2 udp      17 src=172.30.10.5 dst=10.0.0.2 sport=5001 dport=5000 src=10.0.0.2 dst=10.1.0.10 sport=6000 dport=1026 [OFFLOAD] mark=0 zone=0 use=2
```
