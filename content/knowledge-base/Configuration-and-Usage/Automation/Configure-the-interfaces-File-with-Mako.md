---
title: Configure the interfaces File with Mako
author: NVIDIA
weight: 326
toc: 4
---

## Issue

The `/etc/network/interfaces` file gets very long and cumbersome. What if multiple ports have similar configurations? Is there a way automate this without having to use something like Ansible or Puppet, or without making a custom Python/bash script?

## Solution

`ifupdown2` supports {{<exlink url="http://www.makotemplates.org/" text="Mako templates">}} on Cumulus Linux. Template engines are usually used for generating HTML content, but they work great for large network configurations. Read the {{<exlink url="http://docs.makotemplates.org/en/latest/" text="Mako documentation">}} for more information.

## Examples

| Mako | Output |
| ---- | ------ |
| <pre>## Note that the &quot;range&quot; ends with &#39;4&#39;<br/>## But will iterate only from 1 to 3<br/>## See Python range() for more details<br/>% for i in range(1, 4):<br/>auto swp${i}<br/>iface swp${i}<br/>% endfor</pre> | <pre>auto swp1<br/>iface swp1<br/><br/>auto swp2<br/>iface swp2<br/><br/>auto swp3<br/>iface swp3</pre> |
| <pre>## Mako code when commented out, should be<br/>## done using two comments, not one.<br/>## Otherwise incorrect processing may occur<br/>## &lt;%def name=&quot;other_defaults()&quot;&gt;<br/>##   mtu 3000<br/>## &lt;/%def&gt;<br/>###<br/>&lt;%def name=&quot;interface_defaults()&quot;&gt;<br/>   mtu 9000<br/>   link-speed 10000<br/>   link-duplex full<br/>   link-autoneg off<br/>&lt;/%def&gt;<br/><br/>% for i in range(3,7):<br/>auto swp${i}<br/>iface swp${i}<br/>${interface_defaults()}<br/>% endfor<br/><br/>auto default_bridge<br/>iface default_bridge<br/>        bridge_ports glob swp3-6<br/>        bridge-stp on</pre> | <pre>auto swp3<br/>iface swp3<br/><br/>   mtu 9000<br/>   link-speed 10000<br/>   link-duplex full<br/>   link-autoneg off<br/><br/>auto swp4<br/>iface swp4<br/>   mtu 9000<br/>   link-speed 10000<br/>   link-duplex full<br/>   link-autoneg off<br/><br/>auto swp5<br/>iface swp5<br/><br/>   mtu 9000<br/>   link-speed 10000<br/>   link-duplex full<br/>   link-autoneg off<br/><br/>auto swp6<br/>iface swp6<br/><br/>   mtu 9000<br/>   link-speed 10000<br/>   link-duplex full<br/>   link-autoneg off<br/><br/>auto default_bridge<br/>iface default_bridge<br/>    bridge_ports glob swp3-6<br/>    bridge-stp on</pre> |
| <pre>&lt;%<br/>    vlan_range_1 = [200,220,260]<br/>    vlan_range_2 = range(300,305)<br/>    full_vlan_list = vlan_range_1 + vlan_range_2<br/>%&gt;<br/><br/>% for v in full_vlan_list:<br/>auto vlan${v}<br/>iface vlan${v}<br/>        bridge-ports glob swp1-6.${v}<br/>        bridge-stp on<br/>% endfor</pre> | <pre>auto vlan200<br/>iface vlan200<br/>    bridge-ports glob swp1-6.200<br/>    bridge-stp on<br/>auto vlan220<br/>iface vlan220<br/>    bridge-ports glob swp1-6.220<br/>    bridge-stp on<br/>auto vlan260<br/>iface vlan260<br/>    bridge-ports glob swp1-6.260<br/>    bridge-stp on<br/>auto vlan300<br/>iface vlan300<br/>    bridge-ports glob swp1-6.300<br/>    bridge-stp on<br/>auto vlan301<br/>iface vlan301<br/>    bridge-ports glob swp1-6.301<br/>    bridge-stp on<br/>auto vlan302<br/>iface vlan302<br/>    bridge-ports glob swp1-6.302<br/>    bridge-stp on<br/>auto vlan303<br/>iface vlan303<br/>    bridge-ports glob swp1-6.303<br/>    bridge-stp on<br/>auto vlan304<br/>iface vlan304<br/>    bridge-ports glob swp1-6.304<br/>    bridge-stp on</pre> |

## Layer 3 Configuration Using Mako

The following is a layer 3 configuration created with Mako for `ifupdown2`:

This requires `apt-get install python-ipaddr` if not already installed.

| Mako | Output |
| ---- | ------ |
| <pre>iface lo inet loopback<br />auto eth0<br />iface eth0 inet dhcp<br /><br />&lt;%!<br />from ipaddr import IPAddress<br />ip = IPAddress(&#39;10.1.1.0&#39;)<br />%&gt;<br /><br />&lt;%def name=&quot;incr_ip(ip, count, incr)&quot;&gt;<br />&lt;% newip = ip + (count * incr) %&gt;<br />  address ${newip}/31<br />&lt;/%def&gt;<br /><br />% for i in range(1,10):<br />auto swp${i}<br />iface swp${i}<br />${incr_ip(ip, i, 2)}<br />% endfor</pre> | <pre>iface lo inet loopback<br />auto eth0<br />iface eth0 inet dhcp<br /><br />auto swp1<br />iface swp1<br />    address 10.1.1.2/31<br /><br />auto swp2<br />iface swp2<br />    address 10.1.1.4/31<br /><br />auto swp3<br />iface swp3<br />    address 10.1.1.6/31<br /><br />auto swp4<br />iface swp4<br />    address 10.1.1.8/31<br /><br />auto swp5<br />iface swp5<br />    address 10.1.1.10/31<br /><br />auto swp6<br />iface swp6<br />    address 10.1.1.12/31<br /><br />auto swp7<br />iface swp7<br />    address 10.1.1.14/31<br /><br />auto swp8<br />iface swp8<br />    address 10.1.1.16/31<br /><br />auto swp9<br />iface swp9<br />    address 10.1.1.18/31</pre> |
| <pre>&lt;%!<br /> from ipaddr import IPAddress<br /> ip = IPAddress(&#39;12.12.12.12&#39;)<br />%&gt;<br /><br />&lt;%def name=&quot;incr_ip(ip, count, incr)&quot;&gt;<br />&lt;% newip = ip + (count * incr) %&gt;<br /> address ${newip}/31<br />&lt;/%def&gt;<br /><br />% for i in range(1,4):<br />auto swp${i}<br />iface swp${i}<br />% endfor<br /><br />% for i in range(5,8):<br />auto vlan${i}<br />iface vlan${i}<br />bridge-ports swp1.${i} <br />swp2.${i} swp3.${i}<br />${incr_ip(ip, i, 2)}<br />% endfor</pre> | <pre>auto swp1<br />iface swp1<br /><br />auto swp2<br />iface swp2<br /><br />auto swp3<br />iface swp3<br /><br />auto vlan5<br />iface vlan5<br /> bridge-ports swp1.5 swp2.5 swp3.5<br /> address 12.12.12.22/31<br /><br />auto vlan6<br />iface vlan6<br /> bridge-ports swp1.6 swp2.6 swp3.6<br /> address 12.12.12.24/31<br /><br />auto vlan7<br />iface vlan7<br /> bridge-ports swp1.7 swp2.7 swp3.7<br /> address 12.12.12.26/31</pre> |

## Notes

To correctly comment Mako code, make sure to comment out the code twice (using two hash marks — \#\#). Otherwise, you might see the following error when running `ifquery` on an interface:

    cumulus@switch:~$ ifquery swp1
    error: /etc/network/interfaces: failed to render template (Undefined). Continue without template rendering ...
    auto swp1
    iface swp1 inet static
    address 10.1.2.2
    netmask 255.255.255.252
    down ip addr flush dev swp1

## See Also

{{<link title="Compare ifupdown2 Commands with ifupdown Commands">}}
