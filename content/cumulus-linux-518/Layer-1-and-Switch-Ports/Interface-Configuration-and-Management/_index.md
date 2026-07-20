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
- Interface descriptions can have a maximum of 255 characters.
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
cumulus@switch:~$ nv set interface swp1 link fast-linkup enabled
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
auto-negotiate           disabled           enabled     
duplex                   full               full   
speed                    1G                 auto   
mac-address              48:b0:2d:63:34:55         
fec                                         auto   
mtu                      9000               9216   
fast-linkup              disabled                       
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
- The duration in seconds during which a link must flap the number of times set in the link flap threshold before link flap protection triggers. You can specify a value between 0 (disabled) and 300. The default setting is 10.
- The number of times the link can flap within the link flap window before link flap protection triggers. You can specify a value between 0 (disabled) and 30. The default setting is 5.

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
cumulus@switch:~$ nv set interface swp1 link flap-protection state disabled
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
          operational  applied
---------  -----------  -------
threshold               5     
interval                10    
```

To show if link flap protection is on an interface, run the `nv show interface <interface-id> link flap-protection` command:

```
cumulus@switch:~$ nv show interface swp1 link flap-protection
        applied
------  -------
state   disabled
```

## Link Debounce Timers

A flapping port can cause network instability and disruption as layer 2 and layer 3 protocols are constantly forced to reconverge and rebuild the topology with every port status change. If flapping occurs at short intervals, it can also cause a spike in CPU utilization. To enhance the stability of Ethernet port link state transitions and mitigate network disruptions resulting from port flapping, Cumulus Linux provides link debounce hold timers for link state transitions. The switch waits until the port status is stable for a configured period before notifying layer 2 and layer 3 protocols about the status change (up or down).

When a link transitions up or down, the debounce timer starts. The switch reports the link change only after the timer expires, and the link remains in that state. If the link toggles back before the timer expires, the switch ignores the event and does not report any state change.

{{%notice note%}}
- You can configure link debounce timers on physical switch ports only.
- The maximum debounce timer values are limited by SDK capabilities (5000ms).
- NVIDIA recommends that you use identical or similar debounce timer values on both ends of the link.
- Link debounce and link flap protection are complementary features that work at different time scales. Link debounce filters transient noise and micro-interruptions whereas link flap protection detects excessive legitimate state transitions and protects the system by placing the interface into a protodown state. If you configure both features, set the link flap protection interval to be significantly larger than the debounce timers to ensure proper coordination.
{{%/notice%}}

To configure the link debounce timers, run the commands below. The hold timers allow a value between 0 and 5000. The default value is 10 milliseconds. A value of 0 disables the timer.

{{< tabs "TabID837 ">}}
{{< tab "NVUE Commands ">}}

Run the `nv set interface <interface> link debounce up` and `nv set interface <interface> link debounce down` commands.
If you configure one direction only, the other direction uses the default value of 10 milliseconds.

```
cumulus@switch:~$ nv set interface swp1 link debounce up 2000  
cumulus@switch:~$ nv set interface swp1 link debounce down 1000
cumulus@switch:~$ nv config apply
```

To unset the link debounce hold timers, run the `nv unset interface <interface> link debounce` command.

{{< /tab >}}
{{< tab "Linux Commands ">}}

Edit the `/etc/cumulus/switchd.d/link.conf` file to edit the `interface.swp61s0.link_debounce.up_delay` and `interface.swp61s0.link_debounce.down_delay` options, then reload `switchd`:

```
cumulus@switch:~$ sudo nano /etc/cumulus/switchd.d/link.conf
interface.swp1.link_debounce.up_delay = 2000 
interface.swp1.link_debounce.down_delay = 1000
```

```
cumulus@switch:~$ sudo systemctl reload switchd.service
```

{{< /tab >}}
{{< /tabs >}}

To show the link transitions for an interface, run the `nv show interface <interface-id> link debounce` command.

```
cumulus@switch:~$ nv show interface swp1 link debounce 
      operational  applied
----  -----------  -------
up    200          200    
down  150          150
```

To show link debounce statistics for an interface, run the `nv show interface <interface-id> counters link debounce` command.

```
cumulus@switch:~$ nv show interface swp1 counters link debounce 
                      operational
--------------------  -----------
ignored-down-events   0          
ignored-up-events     0          
received-up-events    2          
received-down-events  1          
timer-cancellations   0          
timer-expirations     3
```

To show the link debounce statistics for all interfaces, run the `nv show interface debounce-counters` command:

```
cumulus@switch:~$ nv show interface debounce-counters
Interface ignored-up ignored-down received-up received-down timer-cancel timer-expire 
--------- ---------- ------------ ----------- ------------- ------------ ------------ 
swp1      10         8            23          22            18           45 
swp2      5          3            15          14            8            22 
swp3      0          0            2           2             0            4 
```

To clear link debounce statistics for an interface, run the `nv action clear interface <interface-id> counters link debounce` command:

```
cumulus@switch:~$ nv action clear interface swp1 counters link debounce
```

To clear link debounce statistics for all interfaces, run the `nv action clear interface debounce-counters` command:

```
cumulus@switch:~$ nv action clear interface debounce-counters 
```
<!-- NOT YET SUPPORTED IN 5.18
## APSU and Link Precoding Control

Cumulus Linux supports Autonomous Path Start-Up (APSU) for link initialization and precoding control for negotiation between connected devices on a Spectrum-6 switch while preserving the default firmware-managed behavior for standard deployments.

{{%notice note%}}
- APSU and link precoding control are supported on NVIDIA Spectrum-6 and later, and with firmware that has APSU and precoding support enabled.
- APSU and link precoding control are advanced features. Do not overwrite the default firmware-managed behavior unless you are an advanced user.
{{%/notice%}}

To enable APSU, run the `nv set interface <interface-id> link apsu-mode enabled` command: 

```
cumulus@switch:~$ nv set interface swp1 link apsu-mode enabled
cumulus@switch:~$ nv config apply
```

To disable APSU, run the `nv set interface <interface-id> link apsu-mode disabled` command.

To enable link precoding, run the `nv set interface <interface-id> link module-precoding enabled` command:

```
cumulus@switch:~$ nv set interface swp1 link module-precoding enabled
cumulus@switch:~$ nv config apply
```

To disable link precoding, run the `nv set interface <interface-id> link module-precoding disabled` command.

The default for both APSU and link precoding is `auto`, which maps to the firmware default.

To show APSU and link precoding information, run the `nv show interface <interface-id>` command:

```
cumulus@switch:~$ nv show interface swp1
```
-->
## Tx Squelch Control

{{%notice note%}}
Tx squelch control is a Beta feature.
{{%/notice%}}

Tx squelch control is a PHY‑level feature that controls if the local port continues transmitting when the remote side is logically down (for example, when the remote side is in a fault state or needs to restart auto-negotiation).

{{%notice note%}}
- Switches with Spectrum-4 and later support Tx squelch control.
- Cumulus Linux supports Tx squelch control on physical ports only (including breakout ports).
- Enabling or disabling Tx squelch control is disruptive on admin UP ports. The switch performs a port admin‑status down, then port admin‑status up for the changes to take effect.
- Enabling or disabling Tx squelch control is not disruptive on admin DOWN ports. When you enable or disable Tx squelch control on an admin DOWN port, the new setting becomes effective the next time the port is admin UP.
{{%/notice%}}

{{< tabs "TabID773 ">}}
{{< tab "NVUE Commands ">}}

To enable Tx squelch control, run the `nv set interface <interface> link tx-squelch enabled` command. The default setting is `auto`, which enables the switch to decide the correct configuration.

```
cumulus@switch:~$ nv set interface swp1 link tx-squelch enabled 
cumulus@switch:~$ nv config apply
```

To disable Tx squelch control, run the `nv set interface <interface> link tx-squelch disabled` command.

To show if Tx squelch control is enabled, run the `nv show interface <interface> link` command:

```
cumulus@switch:~$ nv show interface swp1 link
                         operational              applied
-----------------------  -----------------------  -------
admin-status             up                              
oper-status              up                              
oper-status-last-change  2024/10/11 19:12:16.339         
protodown                disabled                        
auto-negotiate           disabled                 enabled
duplex                   full                     full   
speed                    1G                       auto   
mac-address              48:b0:2d:fa:a1:14               
fec                                               auto   
mtu                      9000                     9216   
fast-linkup              disabled
tx-squelch               enabled                  auto  
```

{{< /tab >}}
{{< tab "Linux Commands ">}}

To enable Tx squelch control, edit the `/etc/cumulus/switchd.conf` file to set the `interface.<interface-id>.tx_squelch` parameter to `enabled`, then reload `switchd`.

```
cumulus@switch:~$ sudo nano /etc/cumulus/switchd.conf
...
interface.swp1.tx_squelch = enabled 
```

```
cumulus@switch:~$ sudo systemctl reload switchd.service
```

To disable Tx squelch control, set the `interface.<interface-id>.tx_squelch` parameter to `disabled`.

{{< /tab >}}
{{< /tabs >}}

## Link Tracking

Link tracking enables you to monitor interfaces automatically and ensure traffic is steered through available redundant paths. This feature prevents traffic blackholing by dynamically managing downlink behavior based on the health of uplinks, ensuring predictable network operations, and improving overall resiliency.

### Configure and Enable Link Tracking

To configure and enable link tracking:
- Set link tracking to `enabled`.
- Create a link tracking group with the set of links (watch interfaces) that you want to monitor.
  - You can only configure switch port (swp) interfaces that already exist.
  - A group name must be between 1 and 16 characters long. You can use alphanumeric characters, hyphens (-), and underscores (_).
- Set the minimum number of watch interfaces for each group that must be operationally up to keep the associated target interfaces active. 
  - The minimum number of links must not exceed the number of interfaces configured in the group.
  - The default value is 1 when the group has at least one watch interface.
- Associate target interfaces with the link tracking group. These are the interfaces that depend on the health of the watch interfaces in the group. 
  - The interface must be a switch port (swp).
  - You cannot configure an interface as both a watch interface and a target interface.
- Specify the action each group takes when the number of operationally up watch interfaces drops below the minimum threshold. When the number of operationally up watch interfaces meets or exceeds the threshold again, the switch clears the action and restores the target interfaces. You can set the following actions:
  -  `protodown-target-interface` marks the target interfaces as protodown so that the switch does not forward traffic to downstream devices over those links. This is the default action.
  - `control-plane-action` notifies the control plane to reroute traffic away from the affected plane.

When you configure and enable link tracking, the `ifplugd` service starts. The `ifplugd-resync-config-change` service restarts and synchronizes the protodown state of the target interfaces based on their link tracking group configuration. When you disable link tracking, the `ifplugd` service stops.

The following example configures two groups: 
- GROUP1 sets the watch interfaces to swp17, swp19, and swp21, and the minimum number of watch interfaces that must be operationally up to 1. The target interfaces are swp7 and swp15, and the action is `control-plane-action`.
- GROUP2 sets the watch interfaces to swp17, swp24, swp25, and swp31 and the minimum number of watch interfaces that must be operationally up to 2. The target interface is swp8 and the action is `protodown-target-interface`.

{{< tabs "TabID895 ">}}
{{< tab "NVUE Commands ">}}

```
cumulus@switch:~$ nv set system link-tracking state enabled
cumulus@switch:~$ nv set system link-tracking group GROUP1 watch-interface swp17,19,21
cumulus@switch:~$ nv set system link-tracking group GROUP1 min-links 1
cumulus@switch:~$ nv set interface swp7,15 link-tracking group GROUP1
cumulus@switch:~$ nv set system link-tracking group GROUP1 state-change-action control-plane-action
cumulus@switch:~$ nv set system link-tracking group GROUP2 watch-interface swp17,24-25,31
cumulus@switch:~$ nv set system link-tracking group GROUP2 min-links 2
cumulus@switch:~$ nv set interface swp8 link-tracking group GROUP2
cumulus@switch:~$ nv set system link-tracking group GROUP2 state-change-action protodown-target-interface
cumulus@switch:~$ nv config apply
```

{{< /tab >}}
{{< tab "Linux Commands ">}}

Edit the following configuration files:

- `/etc/default/ifplugd` sets the watch interfaces to monitor for link state changes.
- `/etc/ifplugd/link-tracking.conf` configures link tracking groups and actions.

The example configuration below configures `ifplugd` to bring down all uplinks when the peer bond goes down in an MLAG environment.

1. Edit `/etc/default/ifplugd` in a text editor to configure the watch interfaces to monitor for link state changes. The example below configures interface swp17, swp19, swp21, swp24, swp25, and swp31.
    
```
    # ifplugd Configuration for Link Tracking
#
# Usage:
#   Sourced by /etc/init.d/ifplugd and /lib/udev/ifplugd.agent
#   to set default values.
#
# Interface Lists:
#   - INTERFACES: Interfaces to be monitored by ifplugd
#   - HOTPLUG_INTERFACES: Interfaces monitored on hotplug (typically empty)

# Watch interfaces to monitor for link state changes
INTERFACES="swp17 swp19 swp21 swp24 swp25 swp31"

HOTPLUG_INTERFACES=""

# ifplugd Arguments:
# -p: Don't run action script on daemon startup (we run sync once after config
#     apply. ifplugd then only runs the script on link state changes)
# -q: Don't run script on daemon shutdown
# -f: Ignore detection failures (continue running if detection fails)
# -u0: Delay after link up = 0 seconds (immediate action)
# -d1: Delay after link down = 1 second (brief delay to avoid flaps)
# -w: Wait until daemon forks (synchronous startup)
# -I: Don't exit on nonzero return values from action script
#
# Note: These values balance responsiveness with flap protection.
#       Adjust delays if needed for your environment.
ARGS="-p -q -f -u0 -d1 -w -I"

SUSPEND_ACTION="stop"
```

2. Edit the `/etc/ifplugd/link-tracking.conf` file in a text editor to configure link tracking groups. The following example configures GROUP1 and GROUP2.

```
# Link Tracking Group Configuration
#
# Purpose:
#   Map watch interfaces to target interfaces for tracking.
#   Read by /etc/ifplugd/ifplugd.action to manage target interfaces when
#   watch interfaces fail.
#
# Format:
#   GROUP_ID|WATCH_INTERFACES|TARGET_INTERFACES|MIN_LINKS|state-change-action
#   GROUP_ID:            Unique identifier for the tracking group
#   WATCH_INTERFACES:    comma-separated interfaces to monitor
#   TARGET_INTERFACES:   comma-separated interfaces to manage
#   MIN_LINKS:           minimum watch interfaces that must be up (default 1)
#   state-change-action: protodown-target-interface or control-plane-action
#
# Example:
#   group-1|swp1,swp2|swp10,swp11|1|protodown-target-interface
#
GROUP1|swp17,swp19,swp21|swp15,swp7|1|control-plane-action
GROUP2|swp17,swp24,swp25,swp31|swp8|2|protodown-target-interface

$ cat /etc/ifplugd/ifplugd-link-tracking.conf
# Auto-generated by NVUE!
# Any local modifications will prevent NVUE from re-generating this file.
# md5sum: 79d87d9a2553351580a38b16e1878267
# ifplugd Link Tracking Maintenance
#
# Sourced by ifplugd-resync-config-change.service on restart (triggered by NVUE).
#
# CLEAR_TARGET_INTERFACES:
#   Space-separated list of target interfaces from which to clear the
#   link-tracking protodown reason. Other protodown reasons are unchanged.
#
# SYNC_GROUPS:
#   When "yes", sync protodown state for all link tracking groups by
#   invoking /etc/ifplugd/action.d/99_link_tracking --all-groups after clear.
#   When "no", skip group sync.

CLEAR_TARGET_INTERFACES=""
SYNC_GROUPS="yes"
```

3. Restart the `ifplugd` daemon to implement the changes:

```
cumulus@switch:~$ sudo systemctl restart ifplugd.service
```

{{< /tab >}}
{{< /tabs >}}

### Upgrade Notes

If you installed and configured {{<link url="ifplugd" text="ifplugd">}} manually in Cumulus Linux 5.17 or earlier, Cumulus Linux 5.18 or later preserves the existing `ifplugd` configuration and behavior after optimized image upgrade. The configuration includes manual configuration in `/etc/default/ifplugd` and custom action scripts under `/etc/ifplugd/action.d/`. If the `ifplugd` service is running before upgrade, the service continues to run and actively manage interfaces. No additional action is required while link tracking remains disabled. Link tracking in Cumulus Linux 5.18 or later is disabled by default.

After you enable and apply link tracking in Cumulus Linux 5.18 or later, feature-managed configuration takes precedence and might overwrite existing *manual* configuration. 

To retain custom interface lists or action logic not supported by link tracking, you can configure traditional snippets.

{{< expand "link tracking snippet" >}}

Configure watch interfaces with a traditional `ifplugd` snippet. The snippet adds the configured interfaces to the `INTERFACES` list in the `/etc/default/ifplugd` file and the switch monitors `ifplugd` for link state changes.

```
cumulus@switch:~$ sudo nano link-track-snippet.yaml
- set:
    system:
      config:
        snippet:
          ifplugd:
            watch-interface:
              swp14: {}
              swp20: {}
              swp5: {}
```

```
cumulus@switch:~$ nv config patch link-track-snippet.yaml
cumulus@switch:~$ nv config apply
```

{{%notice note%}}
- Custom modifications to `/etc/ifplugd/action.d/ifupdown` do not migrate or update automatically. You must implement the `/etc/ifplugd/action.d/ifupdown` script to manage the interface state as required.
- Cumulus Linux does not add the watch interfaces you configure through the snippet to the `/etc/ifplugd/link-tracking.conf` file unless you also configure them as watch interfaces for a link tracking group.
{{%/notice%}}

{{< /expand >}}

{{%notice note%}}
When you enable link tracking after upgrade, any existing `ifplugd` instances manually configured and started before enabling link tracking continue to run. Cumulus Linux does not stop or clean up the instances automatically. You must identify and terminate any manually configured `ifplugd` instances that are no longer required. Failure to do so might result in conflicts with link tracking managed interfaces.
{{%/notice%}}

### Manage Link Tracking

- To disable link tracking, run the `nv set system link-tracking state disabled` command.
- To remove a target interface from a group, run the `nv unset interface <interface-id> link-tracking group` command.
- To reset the action back to the default value, run the `nv unset system link-tracking group <group-id> state-change-action` command.
- To reset the minimum number of watch interfaces to the default value of 1, run the `nv unset system link-tracking group <group-id> min-links` command.
- To remove a link tracking group, run the `nv unset system link-tracking group <group-id>` command. If the group is associated with a target interface, remove the association with the `nv unset interface <interface-id> link-tracking group` command.

### Show Link Tracking Information

To show link tracking configuration, such as the feature state (enabled or disabled) and all configured link tracking groups with their watch interfaces, minimum threshold, and state-change action, run the `nv show system link-tracking` command.

```
cumulus@switch:~$ nv show system link-tracking
       operational  applied
-----  -----------  -------
state  enabled      enabled

group
========
    Link Tracking Group  Watch Interface  Min Links  State Change Action
    -------------------  ---------------  ---------  --------------------------
    GROUP1               swp17            1          control-plane-action
                         swp19
                         swp21
    GROUP2               swp17            2          protodown-target-interface
                         swp24
                         swp25
                         swp3
```

To show all the configured link tracking groups, run the `nv show system link-tracking group` command:

```
cumulus@switch:~$ nv show system link-tracking group
Link Tracking Group  Watch Interface  Min Links  State Change Action
-------------------  ---------------  ---------  --------------------------
GROUP1               swp17            1          control-plane-action
                     swp19
                     swp21
GROUP2               swp17            2          protodown-target-interface
                     swp24
                     swp25
                     swp31
```

To show details of a specific link tracking group, including its watch interfaces, minimum threshold, and state-change action, run the `nv show system link-tracking group <group-id>` command: 

```
cumulus@switch:~$ nv show system link-tracking group GROUP2
                     operational                 applied
-------------------  --------------------------  --------------------------
min-links            2                           2
state-change-action  protodown-target-interface  protodown-target-interface
[watch-interface]    swp17                       swp17
[watch-interface]    swp24                       swp24
[watch-interface]    swp25                       swp25
[watch-interface]    swp31                       swp31
```

To show all configured watch interfaces in a specific group, run the `nv show system link-tracking group <group-id> watch-interface` command:

```
cumulus@switch:~$ nv show system link-tracking group GROUP2 watch-interface
swp17
swp24
swp25
swp31
```

To show the link tracking group associated with each interface, run the `nv show interface link-tracking` command.

```
cumulus@switch:~$ nv show interface link-tracking
Interface  Link Tracking Group  Admin Status  Oper Status  Protodown  Protodown Reason
---------  -------------------  ------------  -----------  ---------  ----------------
eth0                            up            up           disabled
lo                              up            unknown      disabled
mgmt                            up            up           disabled
swp1                            up            down         disabled
swp2                            up            down         disabled
swp3                            up            down         disabled
swp4                            up            down         disabled
swp5                            up            down         disabled
swp6                            up            down         disabled
swp7       GROUP1               up            down         disabled
swp8       GROUP2               up            down         enabled    link-tracking
swp9                            up            down         disabled
swp10                           up            down         disabled
swp11                           up            down         disabled
swp12                           up            down         disabled
swp13                           up            down         disabled
swp14                           up            down         disabled
swp15      GROUP1               up            down         disabled
swp16                           up            down         disabled
swp17                           up            up           disabled
swp18                           up            up           disabled
swp19                           up            up           disabled
swp20                           up            up           disabled
swp21                           up            up           disabled
swp22                           up            up           disabled
swp23                           up            down         disabled
swp24                           up            down         disabled
swp25                           up            down         disabled
```

To show the link tracking group associated with a specific interface, run the `nv show interface <interface-id> link-tracking` command:

```
cumulus@switch:~$ nv show interface swp8 link-tracking
       operational  applied
-----  -----------  -------
group  GROUP2       GROUP2
```

To show only the interfaces associated with a specific group, run the `nv show interface link-tracking --filter "group=<group-name>"` command:

```
cumulus@switch:~$ nv show interface link-tracking --filter "group=GROUP1"
Interface  Link Tracking Group  Admin Status  Oper Status  Protodown  Protodown Reason
---------  -------------------  ------------  -----------  ---------  ----------------
swp7       GROUP1              up            down         disabled
swp15      GROUP1              up            down         disabled
```

### Troubleshooting

To verify the protodown state on a target interface, run the `sudo ip -d link show <interface-id>` command:

```
cumulus@switch:~$ sudo ip -d link show swp8
10: swp8: <NO-CARRIER,BROADCAST,MULTICAST,UP> mtu 9216 qdisc pfifo_fast state DOWN mode DEFAULT group default qlen 1000
    link/ether 1c:34:da:1b:cc:74 brd ff:ff:ff:ff:ff:ff protodown on protodown_reason <link-tracking> promiscuity 0  allmulti 0 minmtu 68 maxmtu 0
    sx_netdev addrgenmode eui64 numtxqueues 1 numrxqueues 1 gso_max_size 65536 gso_max_segs 65535 tso_max_size 65536 tso_max_segs 65535 gro_max_size 65536 switchid ffffffffff01 last_change 1784260523674 carrier_up_count 7 carrier_down_count 8 carrier_changes 15
```

The following example shows the interface state of a target interface after the action is cleared:

```
cumulus@switch:~$ sudo ip -d link show swp8
10: swp8: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 9216 qdisc pfifo_fast state UP mode DEFAULT group default qlen 1000
    link/ether 1c:34:da:1b:cc:74 brd ff:ff:ff:ff:ff:ff promiscuity 0  allmulti 0 minmtu 68 maxmtu 0
    sx_netdev addrgenmode eui64 numtxqueues 1 numrxqueues 1 gso_max_size 65536 gso_max_segs 65535 tso_max_size 65536 tso_max_segs 65535 gro_max_size 65536 switchid ffffffffff01 last_change 1784260564714 carrier_up_count 9 carrier_down_count 9 carrier_changes 18
```

To view link tracking logs in journalctl, run the `sudo journalctl -t ifplugd-link-tracking -f` command:

```
cumulus@switch:~$ sudo journalctl -t ifplugd-link-tracking -f
Jul 17 03:34:21 cumulus ifplugd-link-tracking[859902]: Interface swp24 link state changed, checking link tracking groups
Jul 17 03:34:21 cumulus ifplugd-link-tracking[859907]: Group group-2: Watch interface swp24 is part of this group (min_links=2)
Jul 17 03:34:21 cumulus ifplugd-link-tracking[859917]: Group group-2: 1 watch interface(s) up (min_links=2), applying action to target interfaces: swp8
Jul 17 03:34:21 cumulus ifplugd-link-tracking[859926]: Group group-2: Protodown set ON for target interface swp8 (reason: link-tracking)
Jul 17 03:45:26 cumulus ifplugd-link-tracking[868112]: Interface swp24 link state changed, checking link tracking groups
Jul 17 03:45:26 cumulus ifplugd-link-tracking[868117]: Group group-2: Watch interface swp24 is part of this group (min_links=2)
Jul 17 03:45:26 cumulus ifplugd-link-tracking[868127]: Group group-2: 2 watch interface(s) up (min_links=2), clearing action on target interfaces: swp8
Jul 17 03:45:26 cumulus ifplugd-link-tracking[868131]: Group group-2: Watch interface restored, clearing link-tracking protodown reason for target interface swp8
Jul 17 03:45:26 cumulus ifplugd-link-tracking[868135]: Group group-2: link-tracking reason cleared for swp8
Jul 17 03:45:26 cumulus ifplugd-link-tracking[868140]: Group group-2: Protodown turned off for target interface swp8 (link-tracking cleared, no other reasons)
```

To view link tracking logs in syslog, run the `sudo grep "link-tracking" /var/log/syslog` command:

```
cumulus@switch:~$ sudo grep "link-tracking" /var/log/syslog
2026-07-17T03:20:03.549597+00:00 cumulus ifplugd-link-tracking: Interface swp24 link state changed, checking link tracking groups
2026-07-17T03:20:03.556205+00:00 cumulus ifplugd-link-tracking: Group group-2: Watch interface swp24 is part of this group (min_links=2)
2026-07-17T03:20:03.565774+00:00 cumulus ifplugd-link-tracking: Group group-2: 1 watch interface(s) up (min_links=2), applying action to target interfaces: swp8
2026-07-17T03:20:03.577761+00:00 cumulus ifplugd-link-tracking: Group group-2: Protodown set ON for target interface swp8 (reason: link-tracking)
2026-07-17T03:45:26.527768+00:00 cumulus ifplugd-link-tracking: Interface swp24 link state changed, checking link tracking groups
2026-07-17T03:45:26.534124+00:00 cumulus ifplugd-link-tracking: Group group-2: Watch interface swp24 is part of this group (min_links=2)
2026-07-17T03:45:26.543704+00:00 cumulus ifplugd-link-tracking: Group group-2: 2 watch interface(s) up (min_links=2), clearing action on target interfaces: swp8
2026-07-17T03:45:26.548576+00:00 cumulus ifplugd-link-tracking: Group group-2: Watch interface restored, clearing link-tracking protodown reason for target interface swp8
2026-07-17T03:45:26.555627+00:00 cumulus ifplugd-link-tracking: Group group-2: link-tracking reason cleared for swp8
2026-07-17T03:45:26.563410+00:00 cumulus ifplugd-link-tracking: Group group-2: Protodown turned off for target interface swp8 (link-tracking cleared, no other reasons)
```

To verify the ifplugd service:

```
cumulus@switch:~$ sudo systemctl status ifplugd.service
● ifplugd.service - LSB: Brings up/down network automatically
     Loaded: loaded (/etc/init.d/ifplugd; generated)
    Drop-In: /etc/systemd/system/ifplugd.service.d
             └─override.conf
     Active: active (running) since Fri 2026-07-17 01:56:33 UTC; 1h 54min ago
       Docs: man:systemd-sysv-generator(8)
      Tasks: 6 (limit: 18430)
     Memory: 1.2M
        CPU: 2.032s
     CGroup: /system.slice/ifplugd.service
             ├─788534 /usr/sbin/ifplugd -i swp17 -p -q -f -u0 -d1 -w -I
             ├─788542 /usr/sbin/ifplugd -i swp19 -p -q -f -u0 -d1 -w -I
             ├─788550 /usr/sbin/ifplugd -i swp21 -p -q -f -u0 -d1 -w -I
             ├─788559 /usr/sbin/ifplugd -i swp24 -p -q -f -u0 -d1 -w -I
             ├─788567 /usr/sbin/ifplugd -i swp25 -p -q -f -u0 -d1 -w -I
             └─788575 /usr/sbin/ifplugd -i swp31 -p -q -f -u0 -d1 -w -I

Jul 17 03:20:03 cumulus ifplugd(swp24)[788559]: Program executed successfully.
Jul 17 03:33:57 cumulus ifplugd(swp24)[788559]: Link beat detected.
Jul 17 03:33:57 cumulus ifplugd(swp24)[788559]: Executing '/etc/ifplugd/ifplugd.action swp24 up'.
Jul 17 03:33:57 cumulus ifplugd(swp24)[788559]: Program executed successfully.
Jul 17 03:34:20 cumulus ifplugd(swp24)[788559]: Link beat lost.
Jul 17 03:34:21 cumulus ifplugd(swp24)[788559]: Executing '/etc/ifplugd/ifplugd.action swp24 down'.
Jul 17 03:34:21 cumulus ifplugd(swp24)[788559]: Program executed successfully.
Jul 17 03:45:26 cumulus ifplugd(swp24)[788559]: Link beat detected.
Jul 17 03:45:26 cumulus ifplugd(swp24)[788559]: Executing '/etc/ifplugd/ifplugd.action swp24 up'.
Jul 17 03:45:26 cumulus ifplugd(swp24)[788559]: Program executed successfully.
```

```
cumulus@switch:~$ sudo systemctl status ifplugd-resync-config-change.service
○ ifplugd-resync-config-change.service - ifplugd Resync on Config Change
     Loaded: loaded (/lib/systemd/system/ifplugd-resync-config-change.service; enabled; preset: enabled)
     Active: inactive (dead) since Fri 2026-07-17 03:05:21 UTC; 45min ago
       Docs: man:ifplugd(8)
    Process: 838723 ExecStart=/etc/ifplugd/ifplugd-resync-config-change.sh (code=exited, status=0/SUCCESS)
   Main PID: 838723 (code=exited, status=0/SUCCESS)
        CPU: 37ms

Jul 17 03:05:21 cumulus systemd[1]: Starting ifplugd-resync-config-change.service - ifplugd Resync on Config Change...
Jul 17 03:05:21 cumulus systemd[1]: ifplugd-resync-config-change.service: Deactivated successfully.
Jul 17 03:05:21 cumulus systemd[1]: Finished ifplugd-resync-config-change.service - ifplugd Resync on Config Change.
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
auto-negotiate           disabled                 enabled       
duplex                   full                     full     full   
speed                    1G                       auto     auto   
mac-address              48:b0:2d:fa:a1:14                        
fec                                               auto     auto   
mtu                      9000                     9216     9216   
fast-linkup              disabled                                      
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
cumulus@switch:~$ nv show interface lo ipv4 address
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
                          operational                   applied          
------------------------  ----------------------------  -----------------
...                                                            
description               hypervisor_port_1             hypervisor_port_1
ip                                                                       
  vrrp                                                                   
    state                                               disabled              
  igmp                                                                   
    state                                               disabled              
  neighbor-discovery                                                     
    state                                               enabled               
    router-advertisement                                                 
      state                                             disabled              
    home-agent                                                           
      state                                             disabled              
    [rdnss]                                                              
    [dnssl]                                                              
    [prefix]                                                             
  ipv4                                                                   
    forward                                             enabled               
  ipv6                                                                   
    state                                               enabled               
    forward                                             enabled               
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

### Interface Fault Detection

You can view interface status along with any detected local or remote fault with the `nv show interface status` command:

```
cumulus@switch:mgmt:~$ nv show interface status

Interface  Admin Status  Oper Status  Protodown  Protodown Reason  Fault  
---------  ------------  -----------  ---------  ----------------  --------
...
swp45      up            down         disabled                     Local Fault  
swp46      up            down         disabled                     Remote Fault
swp47      down          down         disabled                     No Fault   
swp48      down          down         disabled                     No Fault 
...
```

To view additional fault information for a specific interface, run the `nv show interface <interface> link phy detail` command:

```
cumulus@switch:mgmt:~$ nv show interface swp45 link phy detail
                                  operational       
--------------------------------  -------------------
...
linkdown-reason-code-local        23                
linkdown-reason-status-local      CABLE_WAS_UNPLUGGED
linkdown-reason-code-remote       1                 
linkdown-reason-status-remote     UNKNOWN_REASON
...
```

{{%notice note%}}
- Interface fault detection is supported on Spectrum-4 and later.
- Fault status reported by the `nv show interface status` command is only supported on physical switch ports and breakout interfaces. Fault state is not applicable to logical interfaces such as VLAN sub-interfaces, SVIs, loopback interfaces, VRF interfaces, and bonds.
- Fault detection data is not retained across reboots or when the `switchd` service is restarted.
{{%/notice%}}

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
