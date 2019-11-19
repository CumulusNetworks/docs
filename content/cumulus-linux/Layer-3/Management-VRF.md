---
title: Management VRF
author: Cumulus Networks
weight: 195
aliases:
 - /display/DOCS/Management+VRF
 - /pages/viewpage.action?pageId=8366664
product: Cumulus Linux
version: '4.0'
---
{{%notice note%}}

In Cumulus Linux 4.0, management VRF is enabled by default. This is a change from earlier Cumulus Linux releases, where management VRF is *disabled* by default. Be sure to update any configuration scripts, if necessary.

{{%/notice%}}

*Management VRF* is a subset of [VRF](../Virtual-Routing-and-Forwarding-VRF/) (virtual routing tables and forwarding) and provides a separation between the out-of-band management network and the in-band data plane network. For all VRFs, the *main* routing table is the default table for all of the data plane switch ports. With management VRF, a second table, *mgmt*, is used for routing through the Ethernet ports of the switch. The *mgmt* name is special cased to identify the management VRF from a data plane VRF. FIB rules are installed for DNS servers because this is the typical deployment case.

Cumulus Linux only supports eth0 as the management interface, or eth1 depending on the switch platform. The Ethernet ports are software-only ports that are not hardware accelerated by `switchd`. VLAN subinterfaces, bonds, bridges, and the front panel switch ports are not supported as management interfaces.

Management VRF is enabled by default in Cumulus Linux so logins to the switch are set into the management VRF context. IPv4 and IPv6 networking applications (for example, Ansible, Chef, and `apt-get`) run by an administrator communicate out the management network by default. This default context does not impact services run through `systemd` and the `systemctl` command, and does not impact commands examining the state of the switch, such as the `ip` command to list links, neighbors, or routes.

{{%notice tip%}}

The management VRF configurations in this chapter contain a localhost loopback IPv4 address of 127.0.0.1/8 and IPv6 address of ::1/128. Management VRF must have an IPv6 address as well as an IPv4 address to work correctly. Adding the loopback address to the layer 3 domain of the management VRF prevents issues with applications that expect the loopback IP address to exist in the VRF, such as NTP.

{{%/notice%}}

To disable management VRF, either run the NCLU `net del vrf mgmt` command or remove the `auto mgmt` and `auto eth0` stanzas from the `/etc/network/interfaces` file, then reboot the switch:

## Bring Up the Management VRF

If you take down the management VRF using `ifdown`, to bring it back up you need to do one of two things:

- Run the `ifup --with-depends mgmt` command
- Run `ifreload -a` command

The following command example brings down the management VRF, then brings it back up with the `ifup --with-depends mgmt` command:

```
cumulus@switch:~$ sudo ifdown mgmt
cumulus@switch:~$ sudo ifup --with-depends mgmt
```

{{%notice note%}}

Running `ifreload -a` disconnects the session for any interface configured as *auto*.

{{%/notice%}}

## Run Services within the Management VRF

At installation, the only enabled service that runs in the management VRF is NTP (`ntp@mgmt.service`). However, you can run a variety of services within the management VRF instead of the default VRF. When you run a `systemd` service inside the management VRF, that service runs **only** on eth0. You cannot configure the same service to run successfully in both the management VRF and the default VRF; you must stop and disable the normal service with `systemctl`.

You must disable the following services in the default VRF if you want to run them in the management VRF:

- chef-client
- collectd
- dhcpd
- dhcrelay
- hsflowd
- netq-agent
- netq-notifier
- netqd
- puppet
- snmpd
- snmptrapd
- ssh
- zabbix-agent

You can configure certain services (such as `snmpd`) to use multiple routing tables, some in the management VRF, some in the default or additional VRFs. The kernel provides a `sysctl` that allows a single instance to accept connections over all VRFs.

{{%notice note%}}

For TCP, connected sockets are bound to the VRF on which the first packet is received.

{{%/notice%}}

The following steps show how to enable the SNMP service to run in the management VRF. You can enable any of the services listed above, except for `dhcrelay` (see [DHCP Relays](../../Layer-1-and-Switch-Ports/DHCP-Relays/)).

1. If SNMP is running, stop the service:

```
cumulus@switch:~$ sudo systemctl stop snmpd.service
```

2. Disable SNMP from starting automatically in the default VRF:

```
cumulus@switch:~$ sudo systemctl disable snmpd.service
```

3. Start SNMP in the management VRF:

```
cumulus@switch:~$ sudo systemctl start snmpd@mgmt.service
```

4. Enable `snmpd@mgmt` so that it starts when the switch boots:

```
cumulus@switch:~$ sudo systemctl enable snmpd@mgmt.service
```

5. Verify that the SNMP service is running in the management VRF:

```
cumulus@switch:~$ ps aux | grep snmpd
snmp      3083  0.1  1.9  35916 13292 ?        Ss   21:07   0:00 /usr/sbin/snmpd -y -LS 0-4 d -Lf /dev/null -u snmp -g snmp -I -smux -p /run/snmpd.pid -f
cumulus   3225  0.0  0.1   6076   884 pts/0    S+   21:07   0:00 grep snmpd
```

Run the following command to show the process IDs associated with the management VRF:

```
cumulus@switch:~$ ip vrf pids mgmt
1149  ntpd
 1159  login
 1227  bash
16178  vi
  948  dhclient
20934  sshd
20975  bash
21343  sshd
21384  bash
21477  ip
```

Run the following command to show the VRF association of the specified process:

```
cumulus@switch:~$ ip vrf identify 2055
mgmt
```

Run `ip vrf help` for additional `ip vfr` commands.

{{%notice note%}}

You might see a warning, similar to the one below from `systemctl` for any management VRF service. You can ignore this warning. This is a problem in `systemd` in Debian 10 (buster).

Warning: The unit file, source configuration file or drop-ins of ntp@mgmt.service changed on disk. Run 'systemctl daemon-reload' to reload unit

{{%/notice%}}

### Enable Polling with snmpd in a Management VRF

When you enable `snmpd` to run in the management VRF, you need to specify that VRF so that `snmpd` listens on eth0 in the management VRF; you can also configure `snmpd` to listen on other ports. In Cumulus Linux, SNMP configuration is VRF aware so `snmpd` can bind to multiple IP addresses each configured with a particular VRF (routing table). The `snmpd` daemon responds to polling requests on the interfaces of the VRF on which the request comes in. For information about configuring SNMP version 1, 2c, and 3 Traps and (v3) Inform messages, refer to [Simple Network Management Protocol - SNMP](../../Monitoring-and-Troubleshooting/Simple-Network-Management-Protocol-SNMP/).

{{%notice note%}}

The message `Duplicate IPv4 address detected, some interfaces may not be visible in IP-MIB` displays after starting `snmpd` in the management VRF. This is because the IP-MIB assumes that the same IP address cannot be used twice on the same device; the IP-MIB is not VRF aware. This message is a warning that the SNMP IP-MIB detects overlapping IP addresses on the system; it does *not* indicate a problem and is non-impacting to the operation of the switch.

{{%/notice%}}

### ping or traceroute on the Management VRF

By default, when you issue a `ping` or `traceroute`, the packet is sent to the dataplane network (the main routing table). To use `ping` or `traceroute` on the management network, use `ping -I mgmt` or `traceroute -i mgmt`. To select a source address within the management VRF, use the `-s` flag for `traceroute`.

```
cumulus@switch:~$ ping -I <destination-ip>
```

Or:

```
cumulus@switch:~$ traceroute -s <source-ip> <destination-ip>
```

For additional information on using `ping` and `traceroute`, see [Network Troubleshooting](../../Monitoring-and-Troubleshooting/Network-Troubleshooting/).

### Run Services as a Non-root User

To run services in the management VRF as a non-root user, you need to create a custom service based on the original service file. The following example commands configure the SSH service to run in the management VRF as a non-root user.

1. Run the following command to create a custom service file in the `/etc/systemd/system` direcotry.

```
cumulus@switch:~$ sudo -E systemctl edit --full ssh.service
```

2. If a *User* directive exists under *\[Service\]*, comment it out.

```
cumulus@switch:~$ sudo nano /etc/systemd/system/ssh.service
...
[Service]
#User=username
ExecStart=/usr/local/bin/ssh agent -data-dir=/tmp/ssh -bind=192.168.0.11
...
```

3. Modify the *ExecStart* line to `/usr/bin/vrf exec mgmt /sbin/runuser -u USER -- ssh`:

```
...
[Service]
#User=username
ExecStart=/usr/bin/vrf task exec mgmt /sbin/runuser -u cumulus -- ssh
...
```

## OSPF and BGP

FRRouting is VRF-aware and sends packets based on the switch port routing table. This includes BGP peering via loopback interfaces. BGP does routing lookups in the default table. However, depending on how your routes are redistributed, you might want to perform the following modification.

Management VRF uses the mgmt table, including local routes. It does not affect how the routes are redistributed when using routing protocols such as OSPF and BGP.

To redistribute the routes in your network, use the `redistribute connected` command under BGP or OSPF. This enables the directly-connected network out of eth0 to be advertised to its neighbor.

{{%notice note%}}

This also creates a route on the neighbor device to the management network through the data plane, which might not be desired.

{{%/notice%}}

Cumulus Networks recommends you always use route maps to control the advertised networks redistributed by the `redistribute connected` command. For example, you can specify a route map to redistribute routes in this way (for both BGP and OSPF):

<details>

<summary>NCLU Commands </summary>

```
cumulus@switch:~$ net add routing route-map REDISTRIBUTE-CONNECTED deny 100 match interface eth0
cumulus@switch:~$ net add routing route-map REDISTRIBUTE-CONNECTED permit 1000
```

</details>

<details>

<summary>vtysh Commands </summary>

```
cumulus@switch:$ sudo vtysh

switch# configure terminal
switch(config)# route-map REDISTRIBUTE-CONNECTED deny 100 match interface eth0
switch(config)# route-map REDISTRIBUTE-CONNECTED permit 1000
switch(config)# redistribute connected route-map REDISTRIBUTE-CONNECTED
switch(config)# exit
switch# write memory
switch# exit
cumulus@switch:~$
```

</details>

The NCLU and vtysh commands save the configuration in the `/etc/frr/frr.conf` file. For example:

```
...
<routing-protocol>
redistribute connected route-map REDISTRIBUTE-CONNECTED

route-map REDISTRIBUTE-CONNECTED deny 100
match interface eth0
!
route-map REDISTRIBUTE-CONNECTED permit 1000
...
```

## SSH within a Management VRF Context

If you SSH to the switch through a switch port, SSH works as expected. If you need to SSH from the device out of a switch port, use the `ip vrf exec default ssh <switch-port-ip-address>` command. For example:

```
cumulus@switch:~$ sudo ip vrf exec default ssh 10.23.23.2 10.3.3.3
```

## View the Routing Tables

<details>

<summary>NCLU Commands </summary>

The `ip route show` command shows the switch port (*main*) table. You can see the dataplane routing table with the `net show route vrf main` command.

To show information for eth0 (the management routing table), run the `net show route vrf mgmt` command:

```
cumulus@switch:~$ net show route vrf mgmt
default via 192.168.0.1 dev eth0
```

```
cumulus@switch:~$ net show route
default via 10.23.23.3 dev swp17  proto zebra  metric 20
10.3.3.3 via 10.23.23.3 dev swp17
10.23.23.0/24 dev swp17  proto kernel  scope link  src 10.23.23.2
192.168.0.0/24 dev eth0  proto kernel  scope link  src 192.168.0.11
```

If you run the `ip route get` command to return information about a single route, the command resolves over the *mgmt* table by default. To obtain information about the route in the switching silicon, run this command:

```
cumulus@switch:~$ net show route <ip-address>
```

To show the route for any VRF, run the `net show route vrf <vrf-name> <ip-address>` command:

```
cumulus@switch:~$ net show route vrf mgmt <ip-address>
```

</details>

<details>

<summary>Linux Commands </summary>

When you use `ip route get` to return information about a single route, the command resolves over the *mgmt* table by default. To show information about the route in the switching silicon, run this command:

```
cumulus@switch:~$ ip route get <ip-address>
```

Alternatively, you can run this command:

```
cumulus@switch:~$ sudo cl-rctl ip route show <ip-address> 
```

To get the route for any VRF, run the `ip route get <ip-address> oif <vrf-name>` command. For example, to show the route for the management VRF, run:

```
cumulus@switch:~$ ip route get <ip-address> oif mgmt
```

</details>

## mgmt Interface Class

In `ifupdown2`, [interface classes](../../Layer-1-and-Switch-Ports/Interface-Configuration-and-Management/) are used to create a user-defined grouping for interfaces. The special class *mgmt* is available to separate the management interfaces of the switch from the data interfaces. This allows you to manage the data interfaces by default using `ifupdown2` commands. Performing operations on the *mgmt* interfaces requires specifying the `--allow-mgmt` option, which prevents inadvertent outages on the management interfaces. Cumulus Linux by default brings up all interfaces in both the *auto* (default) class and the *mgmt* interface class when the switch boots.

{{%notice warning%}}

The management VRF interface class is not supported if you are configuring Cumulus Linux using [NCLU](../../System-Configuration/Network-Command-Line-Utility-NCLU/).

{{%/notice%}}

You configure the management interface in the `/etc/network/interfaces` file. In the example below, the management interface eth0 and the management VRF stanzas are added to the *mgmt* interface class:

```
...
auto lo
iface lo inet loopback

allow-mgmt eth0
iface eth0 inet dhcp
    vrf mgmt

allow-mgmt mgmt
iface mgmt
    address 127.0.0.1/8
    address ::1/128
    vrf-table auto
...
```

When you run `ifupdown2` commands against the interfaces in the mgmt class, include `--allow=mgmt` with the commands. For example, to see which interfaces are in the mgmt interface class, run:

```
cumulus@switch:~$ ifquery l --allow=mgmt
eth0
mgmt
```

To reload the configurations for interfaces in the mgmt class, run:

```
cumulus@switch:~$ sudo ifreload --allow=mgmt
```

You can still bring the management interface up and down using `ifup eth0` and `ifdown eth0`.

## Management VRF and DNS

Cumulus Linux supports both DHCP and static DNS entries over management VRF through IP FIB rules. These rules are added to direct lookups to the DNS addresses out of the management VRF.

For DNS to use the management VRF, the static DNS entries must reference the management VRF in the `/etc/resolv.conf` file. You cannot specify the same DNS server address twice to associate it with different VRFs.

For example, to specify DNS servers and associate some of them with the management VRF, run the following commands:

<details>
<summary>NCLU Commands </summary>

```
cumulus@switch:~$ net add dns nameserver ipv4 192.0.2.1
cumulus@switch:~$ net add dns nameserver ipv4 198.51.100.31 vrf mgmt
cumulus@switch:~$ net add dns nameserver ipv4 203.0.113.13 vrf mgmt
cumulus@switch:~$ net pending
cumulus@switch:~$ net commit
```

</details>

<details>
<summary>Linux Commands </summary>

Edit the `/etc/resolv.conf` file to add the DNS servers and associate some of them with the management VRF. For example:

```
cumulus@switch:~$ sudo nano /etc/resolv.conf
nameserver 192.0.2.1
nameserver 198.51.100.31 # vrf mgmt
nameserver 203.0.113.13 # vrf mgmt
```

Run the `ifreload -a` command to load the new configuration:

``` 
cumulus@switch:~$ ifreload -a
```

</details>

{{%notice note%}}

Because DNS lookups are forced out of the management interface using FIB rules, this might affect data plane ports if you use overlapping addresses. For example, when the DNS server IP address is learned over the management VRF, a FIB rule is created for that IP address. When DHCP relay is configured for the same IP address, a DHCP discover packet received on the front panel port is forwarded out of the management interface (eth0) even though a route is present out the front-panel port.

{{%/notice%}}

{{%notice note%}}

If you do not specify a DNS server and you lose in band connectivity, DNS does not work through the management VRF. Cumulus Linux does not assume all DNS servers are reachable through the management VRF.

{{%/notice%}}
