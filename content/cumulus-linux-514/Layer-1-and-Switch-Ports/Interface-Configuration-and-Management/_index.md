---
title: Interface Configuration and Management
author: NVIDIA
weight: 290
toc: 3
---

This section discusses how to configure the interfaces on the switch.

Cumulus Linux (including NVUE) uses ifupdown2 to manage network interfaces, which is a new implementation of the Debian network interface manager ifupdown.

## Bring an Interface Up or Down

An interface status can be in an:
- Administrative state, where you configure the interface to be up or down. The administrative state reflects the intended configuration set by an administrator or management system. It indicates whether the interface is meant to be enabled or disabled. 
- Operational state, which reflects the current operational status of an interface. The operational state reflects the actual current status of the interface, taking into account physical and logical conditions.

The carrier state is the lower layer state of an interface. For a switch port, the carrier state represents if the switch port is enabled at the ASIC level and a cable connects successfully. For a virtual interface, the carrier state involves the operational state of lower-level interfaces. For example, for a VLAN interface, the carrier state depends on the underlying bridge device operational state.

The operational state always depends on administrative state and carrier state; the operational state is a function of the administrative state, carrier state and other link states.

{{< tabs "TabID17 ">}}
{{< tab "NVUE Commands ">}}

To configure and bring an interface up administratively, use the `nv set interface` command:

```
cumulus@switch:~$ nv set interface swp1
cumulus@switch:~$ nv config apply
```

After you bring up an interface, you can bring it down administratively by changing the link state to `down`:

```
cumulus@switch:~$ nv set interface swp1 link state down
cumulus@switch:~$ nv config apply
```

To bring the interface back up, change the link state back to `up`:

```
cumulus@switch:~$ nv set interface swp1 link state up
cumulus@switch:~$ nv config apply
```

To remove an interface from the configuration entirely, use the `nv unset interface` command:

```
cumulus@switch:~$ nv unset interface swp1
cumulus@switch:~$ nv config apply
```

{{%notice note%}}
NVUE applies only current configuration changes instead of processing the entire `/etc/network/interfaces` file.
{{%/notice%}}

{{< /tab >}}
{{< tab "Linux Commands ">}}

To configure and bring an interface up administratively, edit the `/etc/network/interfaces` file to add the interface stanza, then run the `ifreload -a` command:

```
cumulus@switch:~$ sudo nano /etc/network/interfaces
auto lo
iface lo inet loopback
    address 10.10.10.1/32
auto mgmt
iface mgmt
    address 127.0.0.1/8
    address ::1/128
    vrf-table auto
auto eth0
iface eth0 inet dhcp
    ip-forward off
    ip6-forward off
    vrf mgmt
auto swp1
iface swp1
...
```

To bring an interface down administratively after you configure it, add `link-down yes` to the interface stanza in the `/etc/network/interfaces` file, then run `ifreload -a`:

```
auto swp1
iface swp1
 link-down yes
```

If you configure an interface in the `/etc/network/interfaces` file, you can bring it down administratively with the `ifdown swp1` command, then bring the interface back up with the `ifup swp1` command. These changes do not persist after a reboot. After a reboot, the configuration present in `/etc/network/interfaces` takes effect.

{{%notice note%}}
- By default, the `ifupdown` and `ifup` commands are quiet. Use the verbose option (`-v`) to show commands as they execute when you bring an interface down or up.
- For configurations at scale, you can run the `ifreload -a --diff` command to apply only current configuration changes instead of processing the entire `/etc/network/interfaces` file.
{{%/notice%}}

To remove an interface from the configuration entirely, remove the interface stanza from the `/etc/network/interfaces` file, then run the `ifreload -a` command.

{{< /tab >}}
{{< /tabs >}}

For additional information on interface administrative state and physical state, refer to [this knowledge base article]({{<ref "/knowledge-base/Configuration-and-Usage/Monitoring/Monitor-Interface-Administrative-State-and-Physical-State-on-Cumulus-Linux" >}}).

## Loopback Interface

Cumulus Linux has a preconfigured loopback interface. When the switch boots up, the loopback interface called *lo* is up and assigned an IP address of 127.0.0.1.

{{%notice note%}}
The loopback interface *lo* must always exist on the switch and must always be up.
{{%/notice%}}

To configure an IP address for the loopback interface:

{{< tabs "TabID196 ">}}
{{< tab "NVUE Commands ">}}

```
cumulus@switch:~$ nv set interface lo ip address 10.10.10.1/32
cumulus@switch:~$ nv config apply
```

{{< /tab >}}
{{< tab "Linux Commands ">}}

Edit the `/etc/network/interfaces` file to add an `address` line:

```
auto lo
iface lo inet loopback
    address 10.10.10.1/32
```

{{< /tab >}}
{{< /tabs >}}

{{%notice note%}}
You can configure multiple IP addresses for the loopback interface.
{{%/notice%}}

## Subinterfaces

On Linux, an *interface* is a network device that can be either physical, (for example, swp1) or virtual (for example, vlan100). A *VLAN subinterface* is a VLAN device on an interface, and the VLAN ID appends to the parent interface using dot (.) VLAN notation. For example, a VLAN with ID 100 that is a subinterface of swp1 is swp1.100. The dot VLAN notation for a VLAN device name is a standard way to specify a VLAN device on Linux.

A VLAN subinterface only receives traffic tagged for that VLAN; therefore, swp1.100 only receives packets that have a VLAN 100 tag on switch port swp1. Any packets that transmit from swp1.100 have a VLAN 100 tag.

The following example configures a routed subinterface on swp1 in VLAN 100:

{{< tabs "TabID316 ">}}
{{< tab "NVUE Commands ">}}

```
cumulus@switch:~$ nv set interface swp1.100 ip address 192.168.100.1/24
cumulus@switch:~$ nv config apply
```

{{< /tab >}}
{{< tab "Linux Commands ">}}

Edit the `/etc/network/interfaces` file, then run `ifreload -a`:

```
cumulus@switch:~$ sudo nano /etc/network/interfaces
...
auto swp1.100
iface swp1.100
 address 192.168.100.1/24
```

```
cumulus@switch:~$ sudo ifreload -a
```

{{< /tab >}}
{{< /tabs >}}

{{%notice note%}}
- If you are using a VLAN subinterface, do not add that VLAN under the bridge stanza.
- You cannot use NVUE commands to create a routed subinterface for VLAN 1.
{{%/notice%}}

## Interface IP Addresses

You can specify both IPv4 and IPv6 addresses for the same interface.

For IPv6 addresses:
- You can create or modify the IP address for an interface using either `::` or `0:0:0` notation. For example, both 2620:149:43:c109:0:0:0:5 and 2001:DB8::1/126 are valid.
- Cumulus Linux assigns the IPv6 address with all zeroes in the interface identifier (2001:DB8::/126) for each subnet; connected hosts cannot use this address.
- You can use Stateless Address Auto-Configuration (SLAAC) to configure an IPv6 address for an interface automatically.

The following example commands configure three IP addresses for swp1; two IPv4 addresses and one IPv6 address.

{{< tabs "TabID464 ">}}
{{< tab "NVUE Commands ">}}

```
cumulus@switch:~$ nv set interface swp1 ip address 10.0.0.1/30
cumulus@switch:~$ nv set interface swp1 ip address 10.0.0.2/30
cumulus@switch:~$ nv set interface swp1 ip address 2001:DB8::1/126
cumulus@switch:~$ nv config apply
```

To show the MAC address for an interface, run the `nv show interface <interface-id> link` command.

{{< /tab >}}
{{< tab "Linux Commands ">}}

In the `/etc/network/interfaces` file, list all IP addresses under the `iface` section.

```
auto swp1
iface swp1
    address 10.0.0.1/30
    address 10.0.0.2/30
    address 2001:DB8::1/126
```

The address method and address family are not mandatory; they default to `inet/inet6` and `static`. However, you must specify `inet/inet6` when you are creating DHCP or loopback interfaces.

```
auto lo
iface lo inet loopback
```

To make non-persistent changes to interfaces at runtime, use `ip addr add`:

```
cumulus@switch:~$ sudo ip addr add 10.0.0.1/30 dev swp1
cumulus@switch:~$ sudo ip addr add 2001:DB8::1/126 dev swp1
```

To remove an address from an interface, use `ip addr del`:

```
cumulus@switch:~$ sudo ip addr del 10.0.0.1/30 dev swp1
cumulus@switch:~$ sudo ip addr del 2001:DB8::1/126 dev swp1
```

{{< /tab >}}
{{< /tabs >}}

## Interface MAC Addresses

You can configure a MAC address for an interface with the `nv set interface <interface-id> link mac-address <mac-address>` command.

{{< tabs "TabID410 ">}}
{{< tab "NVUE Commands ">}}

The following command configures swp1 with MAC address 00:02:00:00:00:05:

```
cumulus@switch:~$ nv set interface swp1 link mac-address 00:02:00:00:00:05
cumulus@switch:~$ nv config apply
```

The following command configures vlan10 with MAC address 00:00:5E:00:01:00:

```
cumulus@switch:~$ nv set interface vlan10 link mac-address 00:00:5E:00:01:00
cumulus@switch:~$ nv config apply
```

To unset the MAC address for an interface, run the `nv unset interface <interface-id> link mac-address` command. This command resets the MAC address to the system assigned address.

```
cumulus@switch:~$ nv unset interface swp1 link mac-address
cumulus@switch:~$ nv config apply
```

{{< /tab >}}
{{< tab "Linux Commands ">}}

In the `/etc/network/interfaces` file, add a MAC address for the interface in the interface stanza, then run `ifreload -a`.

The following example configures swp1 with MAC address 00:02:00:00:00:05:

```
cumulus@switch:~$ sudo nano /etc/network/interfaces
...
auto swp1
iface swp1
    address 10.0.0.2/24
    hwaddress 00:02:00:00:00:05
...
```

```
cumulus@switch:~$ sudo ifreload -a
```

The following example configures vlan10 with MAC address 00:00:5E:00:01:00:

```
cumulus@switch:~$ sudo nano /etc/network/interfaces
...
auto vlan10
iface vlan10
    address 10.1.10.5/24
    hwaddress 00:00:5E:00:01:00
```

```
cumulus@switch:~$ sudo ifreload -a
```

To unset the MAC address for an interface, remove the mac address from the interface stanza, then run the `sudo ifreload -a` command.

{{< /tab >}}
{{< /tabs >}}

## Interface Descriptions

You can add a description (alias) to an interface.

Interface descriptions also appear in the {{<link url="Simple-Network-Management-Protocol-SNMP" text="SNMP">}} OID {{<mib_link text="IF-MIB::ifAlias" url="mibs/IF-MIB.txt" >}}

{{%notice note%}}
- Interface descriptions can have a maximum of 256 characters.
- Avoid using apostrophes or non-ASCII characters. Cumulus Linux does not parse these characters.
{{%/notice%}}

The following example commands create the description `hypervisor_port_1` for swp1:

{{< tabs "TabID838 ">}}
{{< tab "NVUE Commands ">}}

```
cumulus@switch:~$ nv set interface swp1 description hypervisor_port_1
cumulus@switch:~$ nv config apply
```

{{< /tab >}}
{{< tab "Linux Commands ">}}

In the `/etc/network/interfaces` file, add a description using the *alias* keyword:

```
cumulus@switch:~$ sudo nano /etc/network/interfaces

auto swp1
iface swp1
    alias swp1 hypervisor_port_1
```

{{< /tab >}}
{{< /tabs >}}

## Interface Commands

You can specify user commands for an interface that run at pre-up, up, post-up, pre-down, down, and post-down.

You can add any valid command in the sequence to bring an interface up or down; however, limit the scope to network-related commands associated with the particular interface. For example, it does not make sense to install a Debian package on `ifup` of swp1, even though it is technically possible. See `man interfaces` for more details.

The following examples adds a command to an interface to enable proxy ARP:

{{< tabs "TabID640 ">}}
{{< tab "NVUE Commands ">}}

NVUE does not provide commands to configure this feature.

{{< /tab >}}
{{< tab "Linux Commands ">}}

```
cumulus@switch:~$ sudo nano /etc/network/interfaces
auto swp1
iface swp1
    address 12.0.0.1/30
    post-up echo 1 > /proc/sys/net/ipv4/conf/swp1/proxy_arp
```

{{%notice warning%}}
If your `post-up` command also starts, restarts, or reloads any `systemd` service, you must use the `--no-block` option with `systemctl`. Otherwise, that service or even the switch itself might hang after starting or restarting. For example, to restart the `dhcrelay` service after bringing up a VLAN, the `/etc network/interfaces` configuration looks like this:

```
auto bridge.100
iface bridge.100
    post-up systemctl --no-block restart dhcrelay.service
```
{{%/notice%}}

{{< /tab >}}
{{< /tabs >}}

## Port Ranges

To specify port ranges in commands:

{{< tabs "TabID725 ">}}
{{< tab "NVUE Commands ">}}

Use commas to separate different port ranges.

The following example configures the default bridge `br_default` with swp1 through swp46 and swp10 through swp12:

```
cumulus@switch:~$ nv set interface swp1-4,6,10-12 bridge domain br_default
cumulus@switch:~$ nv config apply
```

The following example sets all subinterfaces of swp1s within the range 1-4:

```
cumulus@switch:~$ nv set interface swp1s1-4
cumulus@switch:~$ nv config apply
```

The following example sets all interfaces within the swp range 1 through 64 and their subinterface range 1 through 3:

```
cumulus@switch:~$ nv set interface swp1-64s1-3
cumulus@switch:~$ nv config apply
```

{{< /tab >}}
{{< tab "Linux Commands ">}}

Use the `glob` keyword to specify bridge ports and bond slaves:

```
auto br0
iface br0
    bridge-ports glob swp1-6.100

auto br1
iface br1
    bridge-ports glob swp7-9.100  swp11.100 glob swp15-18.100
```

{{< /tab >}}
{{< /tabs >}}

## Fast Linkup

Cumulus Linux supports fast linkup on interfaces on NVIDIA Spectrum1 switches. Fast linkup enables you to bring up ports with cards that require links to come up fast, such as certain 100G optical network interface cards.

{{%notice note%}}
You must configure both sides of the connection with the same speed and FEC settings.
{{%/notice%}}

{{< tabs "TabID607 ">}}
{{< tab "NVUE Commands">}}

```
cumulus@switch:~$ nv set interface swp1 link fast-linkup on
cumulus@switch:~$ nv config apply
```

{{< /tab >}}
{{< tab "Linux Commands ">}}

Edit the `/etc/cumulus/switchd.conf` file and add the `interface.<interface-id>.enable_media_depended_linkup_flow=TRUE` and `interface.<interface-id>.enable_port_short_tuning=TRUE` settings for the interfaces on which you want to enable fast linkup. The following example enables fast linkup on swp1:

```
cumulus@switch:~$ sudo nano /etc/cumulus/switchd.conf
...
interface.swp1.enable_media_depended_linkup_flow=TRUE
interface.swp1.enable_short_tuning=TRUE
```

Reload `switchd` with the `sudo systemctl reload switchd.service` command.

{{< /tab >}}
{{< /tabs >}}

## Link Flap Protection

Cumulus Linux enables link flap detection by default. Link flap detection triggers when there are five link flaps within ten seconds, at which point the interface goes into a protodown state and shows `linkflap` as the reason. The `switchd` service also shows a log message similar to the following:

```
2023-02-10T17:53:21.264621+00:00 cumulus switchd[10109]: sync_port.c:2263 ERR swp2 link flapped more than 3 times in the last 60 seconds, setting protodown
```

To show interfaces with the protodown flag, run the NVUE `nv show interface status` command or the Linux `ip link` command. To check a specific interface, run the `nv show interface <interface-id> link` command.

```
cumulus@switch:~$ nv show interface status
Interface       Admin Status  Oper Status  Protodown  Protodown Reason
--------------  ------------  -----------  ---------  ----------------
BLUE            up            up           disabled                   
RED             up            up           disabled                   
bond1           up            up           disabled                   
bond2           up            up           disabled                   
bond3           up            up           disabled                   
br_default      up            up           disabled                   
eth0            up            up           disabled                   
lo              up            unknown      disabled                   
mgmt            up            up           disabled                   
peerlink        up            up           disabled                   
peerlink.4094   up            up           disabled                   
swp1            up            up           disabled                   
swp2            up            up           disabled                   
swp3            up            down         enabled    linkflap                 
swp4            down          down         disabled                   
swp5            down          down         disabled                   
swp6            down          down         disabled                   
swp7            down          down         disabled                   
swp8            down          down         disabled                   
swp9            down          down         disabled                   
swp10           down          down         disabled                                                                            
...
```

```
cumulus@switch:~$ ip link
...
37: swp3: <NO-CARRIER,BROADCAST,MULTICAST,SLAVE,UP> mtu 9178 qdisc pfifo_fast master bond131 state DOWN mode DEFAULT group default qlen 1000
  link/ether 1c:34:da:ba:bb:2a brd ff:ff:ff:ff:ff:ff protodown on protodown_reason <linkflap>
...
```

```
cumulus@switch:~$ nv show interface swp3 link
                         operational        applied
-----------------------  -----------------  -------
admin-status             up                        
oper-status              up                        
oper-status-last-change  Unknown                   
protodown                enabled                  
auto-negotiate           off                on     
duplex                   full               full   
speed                    1G                 auto   
mac-address              48:b0:2d:63:34:55         
fec                                         auto   
mtu                      9000               9216   
fast-linkup              off                       
[breakout]                                         
state                    up                 up     
flap-protection                                    
  enable                                    on     
stats                                              
  in-bytes               52.86 MB                  
  in-pkts                440743                    
  in-drops               0                         
  in-errors              0                         
  out-bytes              53.00 MB                  
  out-pkts               444066                    
  out-drops              0                         
  out-errors             0                         
  carrier-transitions    4                         
  carrier-up-count       2                         
  carrier-down-count     2
```

```
cumulus@switch:~$ nv show interface swp3 link protodown-reason 
operational
-----------
linkflap 
```

### Clear the Interface Protodown State and Reason

To clear the protodown state and the reason:

{{< tabs "TabID654 ">}}
{{< tab "NVUE Commands">}}

```
cumulus@switch:~$ nv action clear interface swp1 link flap-protection violation 
```

After a few seconds the port state returns to `up`. Run the `nv show <interface-id> link state` command to verify that the interface is no longer in a protodown state and that the reason clears:

```
cumulus@switch:~$ nv show interface swp1 link state
operational    applied
  -----------    -------
  up             up
```

To clear all the interfaces from a protodown state, run the `nv action clear system link flap-protection violation`.

{{< /tab >}}
{{< tab "Linux Commands ">}}

The `ifdown` and `ifup` commands do not clear the protodown state. You must clear the protodown state and the reason manually using the `sudo ip link set <interface-id> protodown_reason linkflap off` and `sudo ip link set <interface-id> protodown off` commands.

```
cumulus@switch:~$ sudo ip link set swp2 protodown_reason linkflap off
cumulus@switch:~$ sudo ip link set swp2 protodown off
```

After a few seconds, the port state returns to UP. To verify that the interface is no longer in a protodown state and that the reason clears, run the `ip link show <interface-id>` command:

```
cumulus@switch:~$ ip link show swp2
37: swp2: <NO-CARRIER,BROADCAST,MULTICAST,SLAVE,UP> mtu 9178 qdisc pfifo_fast master bond131 state UP mode DEFAULT group default qlen 1000
  link/ether 1c:34:da:ba:bb:2a brd ff:ff:ff:ff:ff:ff
```

{{< /tab >}}
{{< /tabs >}}

### Change Link Flap Protection Settings

You can change the following link flap protection settings:
- The duration in seconds during which a link must flap the number of times set in the link flap threshold before link flap protection triggers. You can specify a value between 0 (off) and 300. The default setting is 10.
- The number of times the link can flap within the link flap window before link flap protection triggers. You can specify a value between 0 (off) and 30. The default setting is 5.

The following example configures the link flap duration to 30 and the number of times the link must flap to 8.

{{< tabs "TabID671 ">}}
{{< tab "NVUE Commands ">}}

```
cumulus@switch:~$ nv set system link flap-protection interval 30
cumulus@switch:~$ nv set system link flap-protection threshold 8 
cumulus@switch:~$ nv config apply
```

{{< /tab >}}
{{< tab "Linux Commands ">}}

Edit the `/etc/cumulus/switchd.conf` file to change the `link_flap_window` and `link_flap_threshold` settings.

```
cumulus@switch:~$ sudo nano /etc/cumulus/switchd.conf
...
link_flap_window = 30
link_flap_threshold = 8
...
```

After you change the link flap settings, you must restart `switchd` with the `sudo systemctl restart switchd.service` command.

{{< /tab >}}
{{< /tabs >}}

### Disable Link Flap Protection

To disable link flap protection:

{{< tabs "TabID682 ">}}
{{< tab "NVUE Commands ">}}

```
cumulus@switch:~$ nv set interface swp1 link flap-protection enable off
cumulus@switch:~$ nv config apply
```

{{< /tab >}}
{{< tab "Linux Commands ">}}

Edit the `/etc/cumulus/switchd.conf` file, and set the `link_flap_window` and `link_flap_threshold` parameters to 0 (zero).

```
cumulus@switch:~$ sudo nano /etc/cumulus/switchd.conf
...
link_flap_window = 0
link_flap_threshold = 0
```

{{< /tab >}}
{{< /tabs >}}

### Show Link Flap Protection Configuration

To show the link flap protection time interval and threshold settings:

```
cumulus@switch:~$ nv show system link flap-protection
           applied
---------  -------
threshold  8      
interval   30 
```

To show if link flap protection is on an interface, run the `nv show interface <interface-id> link flap-protection` command:

```
cumulus@switch:~$ nv show interface swp1 link flap-protection
        applied
------  -------
enable  off
```

## Source Interface File Snippets

Sourcing interface files helps organize and manage the `/etc/network/interfaces` file. For example:

```
cumulus@switch:~$ sudo cat /etc/network/interfaces
# The loopback network interface
auto lo
iface lo inet loopback

# The primary network interface
auto eth0
iface eth0 inet dhcp

source /etc/network/interfaces.d/bond0
```

The contents of the sourced file used above are:

```
cumulus@switch:~$ sudo cat /etc/network/interfaces.d/bond0
auto bond0
iface bond0
    address 14.0.0.9/30
    address 2001:ded:beef:2::1/64
    bond-slaves swp25 swp26
```

## Mako Templates

`ifupdown2` supports {{<exlink url="http://www.makotemplates.org/" text="Mako-style templates">}}. The Mako template engine processes the `interfaces` file before parsing.

Use the template to declare cookie-cutter bridges and to declare addresses in the `interfaces` file:

```
%for i in [1,12]:
auto swp${i}
iface swp${i}
    address 10.20.${i}.3/24
```

{{%notice note%}}
- In Mako syntax, use square brackets (`[1,12]`) to specify a list of individual numbers. Use `range(1,12)` to specify a range of interfaces.
- To test your template and confirm it evaluates correctly, run `mako-render /etc/network/interfaces`.
{{%/notice%}}

To comment out content in Mako templates, use double hash marks (##). For example:

```
## % for i in range(1, 4):
## auto swp${i}
## iface swp${i}
## % endfor
##
```

For more Mako template examples, refer to this [knowledge base article]({{<ref "/knowledge-base/Configuration-and-Usage/Automation/Configure-the-interfaces-File-with-Mako" >}}).

## ifupdown Scripts

Unlike the traditional `ifupdown` system, `ifupdown2` does not run scripts installed in `/etc/network/*/` automatically to configure network interfaces.

To enable or disable `ifupdown2` scripting, edit the `addon_scripts_support` line in the `/etc/network/ifupdown2/ifupdown2.conf` file. `1` enables scripting and `2` disables scripting. For example:

```
cumulus@switch:~$ sudo nano /etc/network/ifupdown2/ifupdown2.conf
# Support executing of ifupdown style scripts.
# Note that by default python addon modules override scripts with the same name
addon_scripts_support=1
```

`ifupdown2` sets the following environment variables when executing commands:

- `$IFACE` represents the physical name of the interface; for example, `br0` or vxlan42. The name comes from the `/etc/network/interfaces` file.
- `$LOGICAL` represents the logical name (configuration name) of the interface.
- `$METHOD` represents the address method; for example, loopback, DHCP, DHCP6, manual, static, and so on.
- `$ADDRFAM` represents the address families associated with the interface in a comma-separated list; for example, `"inet,inet6"`.

## Show Interface Information

To show the administrative and physical (operational) state of all interfaces on the switch:

```
cumulus@switch:~$ nv show interface
Interface  Admin Status  Oper Status  Speed  MTU    Type      Remote Host      Remote Port  Summary                                 
---------  ------------  -----------  -----  -----  --------  ---------------  -----------  ----------------------------------------
eth0       up            up           1G     1500   eth       oob-mgmt-switch  swp10        IP Address:            192.168.200.11/24
                                                                                            IP Address:  fe80::4638:39ff:fe22:17a/64
lo         up            unknown             65536  loopback                                IP Address:                  127.0.0.1/8
                                                                                            IP Address:                      ::1/128
mgmt       up            up                  65575  vrf                                     IP Address:                  127.0.0.1/8
                                                                                            IP Address:                      ::1/128
swp1       up            up           1G     9216   swp                                     IP Address: fe80::4ab0:2dff:fe50:fecf/64
swp2       down          down                1500   swp                                                                             
swp3       down          down                1500   swp                                                                             
swp4       down          down                1500   swp                                                                             
swp5       down          down                1500   swp                                                                             
swp6       down          down                1500   swp                                                                             
swp7       down          down                1500   swp
...
```

To show the administrative and physical (operational) state of an interface, and the date and time the physical state of the interface changed:

{{< tabs "TabID875 ">}}
{{< tab "NVUE Commands ">}}

```
cumulus@switch:~$ nv show interface swp1
                         operational        applied
-----------------------  -----------------  -------
...
  oper-status              up                                       
  admin-status             up                                       
  oper-status-last-change  2024/10/11 19:12:16.339
```

{{< /tab >}}
{{< tab "Linux Commands ">}}

Run the `ip link show dev <interface-id>` command.

In the following example, swp1 is administratively UP and the physical link is UP (LOWER_UP).

```
cumulus@switch:~$ ip link show dev swp1
3: swp1: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc pfifo_fast state UP mode DEFAULT qlen 500
    link/ether 44:38:39:00:03:c1 brd ff:ff:ff:ff:ff:ff
```

{{< /tab >}}
{{< /tabs >}}

To show the last time (date and time) the operational state of an interface changed and the number of carrier transitions for each interface (from the time of interface creation):

```
cumulus@switch:~$ nv show interface --view=carrier-stats
Interface       Oper Status  Up Count  Down Count  Total State Changes  Last State Change      
--------------  -----------  --------  ----------  -------------------  -----------------------
BLUE            up           0         0           0                    Never                  
RED             up           0         0           0                    Never                  
bond1           up           2         1           3                    2024/10/11 19:14:59.265
bond2           up           1         0           1                    2024/10/11 19:12:18.817
bond3           up           1         0           1                    2024/10/11 19:12:18.833
br_default      up           2         2           4                    2024/10/11 19:12:15.216
eth0            up           1         1           2                    2024/10/11 19:12:02.157
lo              unknown      0         0           0                    Never                  
mgmt            up           0         0           0                    Never                  
peerlink        up           1         0           1                    2024/10/11 19:12:06.913
peerlink.4094   up           1         0           1                    2024/10/11 19:12:06.915
swp1            up           2         2           4                    2024/10/11 19:12:16.339
swp2            up           2         2           4                    2024/10/11 19:12:16.345
swp3            up           2         2           4                    2024/10/11 19:12:16.351
swp4            down         1         1           2                    2024/10/11 19:11:28.936
swp5            down         1         1           2                    2024/10/11 19:11:28.936
swp6            down         1         1           2                    2024/10/11 19:11:28.936
swp7            down         1         1           2                    2024/10/11 19:11:28.936
...
```

In the example above:
- `Last State Change` shows the timestamp of the last operational state change.
- `Total State Changes` shows the total number of transitions in the carrier state.
- `Up Count`shows the number of times the carrier transitioned to an UP state.
- `Down Count` shows the number of times the carrier transitioned to a DOWN state.

To show the date and time the operational state of a specific interface changes (`oper-status-last-change`) and the number of carrier transitions (`carrier-transitions`, `carrier-up-count`, `carrier-down-count`):

```
cumulus@switch:~$ nv show interface swp1 link
                         operational              applied  pending
-----------------------  -----------------------  -------  -------
admin-status             up                                       
oper-status              up                                       
oper-status-last-change  2024/10/11 19:12:16.339                  
protodown                disabled                                 
auto-negotiate           off                      on       on     
duplex                   full                     full     full   
speed                    1G                       auto     auto   
mac-address              48:b0:2d:fa:a1:14                        
fec                                               auto     auto   
mtu                      9000                     9216     9216   
fast-linkup              off                                      
[breakout]                                                        
state                    up                       up       up     
flap-protection                                                   
  enable                                          on       on     
stats                                                             
  in-bytes               1.96 MB                                  
  in-pkts                16399                                    
  in-drops               0                                        
  in-errors              0                                        
  out-bytes              2.37 MB                                  
  out-pkts               24669                                    
  out-drops              0                                        
  out-errors             0                                        
  carrier-transitions    4                                        
  carrier-up-count       2                                        
  carrier-down-count     2 
```

To show the number of carrier transitions only (`carrier-transitions`, `carrier-up-count`, `carrier-down-count`) for a specific interface, run the `nv show interface <interface-id> link stats` command.

To show the assigned IP address on an interface:

{{< tabs "TabID898 ">}}
{{< tab "NVUE Commands ">}}

```
cumulus@switch:~$ nv show interface lo ip address
-------------
10.0.1.12/32 
10.10.10.1/32
127.0.0.1/8  
::1/128
```

{{< /tab >}}
{{< tab "Linux Commands ">}}

```
cumulus@switch:~$ ip addr show swp1
3: swp1: <BROADCAST,MULTICAST,SLAVE,UP,LOWER_UP> mtu 1500 qdisc pfifo_fast state UP qlen 500
    link/ether 44:38:39:00:03:c1 brd ff:ff:ff:ff:ff:ff
    inet 192.0.2.1/30 scope global swp1
    inet 192.0.2.2/30 scope global swp1
    inet6 2001:DB8::1/126 scope global tentative
        valid_lft forever preferred_lft forever
```

{{< /tab >}}
{{< /tabs >}}

To show the description (alias) for an interface:

{{< tabs "TabID923 ">}}
{{< tab "NVUE Commands ">}}

```
cumulus@switch$ nv show interface swp1
                         operational        applied
-----------------------  -----------------  -------
                          operational                   applied          
------------------------  ----------------------------  -----------------
...                                                            
description               hypervisor_port_1             hypervisor_port_1
ip                                                                       
  vrrp                                                                   
    enable                                              off              
  igmp                                                                   
    enable                                              off              
  neighbor-discovery                                                     
    enable                                              on               
    router-advertisement                                                 
      enable                                            off              
    home-agent                                                           
      enable                                            off              
    [rdnss]                                                              
    [dnssl]                                                              
    [prefix]                                                             
  ipv4                                                                   
    forward                                             on               
  ipv6                                                                   
    enable                                              on               
    forward                                             on               
  vrf                                                   default          
  [address]               fe80::4ab0:2dff:feeb:db72/64                   
  [gateway]                                                              
...
```

{{< /tab >}}
{{< tab "Linux Commands ">}}

```
cumulus@switch$ ip link show swp1
3: swp1: <NO-CARRIER,BROADCAST,MULTICAST,UP> mtu 1500 qdisc pfifo_fast state DOWN mode DEFAULT qlen 500
    link/ether aa:aa:aa:aa:aa:bc brd ff:ff:ff:ff:ff:ff
    alias hypervisor_port_1
```

{{< /tab >}}
{{< /tabs >}}

You can monitor the traffic rate and <span class="a-tooltip">[PPS](## "Packets per Second")</span> for an interface to ensure optimal network performance and reliability; refer to {{<link title="Troubleshooting Network Interfaces/#monitor-interface-traffic-rate-and-pps" text="Commands to monitor interface traffic rate and PPS">}}.

## Considerations

Even though `ifupdown2` supports the inclusion of multiple `iface` stanzas for the same interface, use a single `iface` stanza for each interface. If you must specify more than one `iface` stanza; for example, if the configuration for a single interface comes from many places, like a template or a sourced file, make sure the stanzas do not specify the same interface attributes. Otherwise, you see unexpected behavior.

In the following example, swp1 is in two files: `/etc/network/interfaces` and `/etc/network/interfaces.d/speed_settings`. `ifupdown2` parses this configuration because the same attributes are not in multiple `iface` stanzas.

```
cumulus@switch:~$ sudo cat /etc/network/interfaces

source /etc/network/interfaces.d/speed_settings

auto swp1
iface swp1
  address 10.0.14.2/24

cumulus@switch:~$ cat /etc/network/interfaces.d/speed_settings

auto swp1
iface swp1
  link-speed 1000
  link-duplex full
```

<!-- vale off -->
<!-- specific commands in title -->
### ifupdown2 and sysctl
<!-- vale on -->

For `sysctl` commands in the `pre-up`, `up`, `post-up`, `pre-down`, `down`, and `post-down` lines that use the
`$IFACE` variable, if the interface name contains a dot (.), `ifupdown2` does not change the name to work with `sysctl`. For example, the interface name `bridge.1` does not convert to `bridge/1`.

<!-- vale off -->
<!-- specific commands in title -->
### ifupdown2 and the gateway Parameter
<!-- vale on -->

The default route that the `gateway` parameter creates in ifupdown2 does not install in FRR, therefore does not redistribute into other routing protocols. Define a static default route instead, which installs in FRR and redistributes, if needed.

The following shows an example of the `/etc/network/interfaces` file when you use a static route instead of a gateway parameter:

```
auto swp2
iface swp2
address 172.16.3.3/24
up ip route add default via 172.16.3.2
```

### Interface Name Limitations

Interface names can be a maximum of 15 characters. You cannot use a number for the first character and you cannot include a dash (-) in the name. In addition, you cannot use any name that matches with the regular expression `.{0,13}\-v.*`.

If you encounter issues, remove the interface name from the `/etc/network/interfaces` file, then restart the `networking.service`.

```
cumulus@switch:~$ sudo nano /etc/network/interfaces
cumulus@switch:~$ sudo systemctl restart networking.service
```

### IP Address Scope

`ifupdown2` does not honor the configured IP address scope setting in the `/etc/network/interfaces` file and treats all addresses as global. It does not report an error. Consider this example configuration:

```
auto swp2
iface swp2
    address 35.21.30.5/30
    address 3101:21:20::31/80
    scope link
```

When you run `ifreload -a` on this configuration, `ifupdown2` considers all IP addresses as global.

```
cumulus@switch:~$ ip addr show swp2
5: swp2: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc pfifo_fast state UP group default qlen 1000
link/ether 74:e6:e2:f5:62:82 brd ff:ff:ff:ff:ff:ff
inet 35.21.30.5/30 scope global swp2
valid_lft forever preferred_lft forever
inet6 3101:21:20::31/80 scope global
valid_lft forever preferred_lft forever
inet6 fe80::76e6:e2ff:fef5:6282/64 scope link
valid_lft forever preferred_lft forever
```

To work around this issue, configure the IP address scope:

{{< tabs "TabID589 ">}}
{{< tab "NVUE Commands ">}}

The NVUE command is not supported.

{{< /tab >}}
{{< tab "Linux Commands ">}}

In the `/etc/network/interfaces` file, configure the IP address scope using `post-up ip address add <address> dev <interface-id> scope <scope>`. For example:

```
auto swp6
iface swp6
    post-up ip address add 71.21.21.20/32 dev swp6 scope site
```

Then run the `ifreload -a` command on this configuration.

{{< /tab >}}
{{< /tabs >}}

The following configuration shows the correct scope:

```
cumulus@switch:~$ ip addr show swp6
9: swp6: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc pfifo_fast state UP group default qlen 1000
link/ether 74:e6:e2:f5:62:86 brd ff:ff:ff:ff:ff:ff
inet 71.21.21.20/32 scope site swp6
valid_lft forever preferred_lft forever
inet6 fe80::76e6:e2ff:fef5:6286/64 scope link
valid_lft forever preferred_lft forever
```

## Related Information

- {{<link url="Troubleshoot-Layer-1">}}
- {{<exlink url="http://wiki.debian.org/NetworkConfiguration" text="Debian - Network Configuration">}}
