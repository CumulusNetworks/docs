---
title: Compare ifupdown2 Commands with ifupdown Commands
author: NVIDIA
weight: 415
toc: 4
---

`ifupdown2` is the network interface manager for Cumulus Linux. It is an updated version of the original `ifupdown` in both Cumulus Linux and Debian. This article demonstrates the differences between the two in how you configure interfaces.

## View All ifupdown2 Configuration Keywords and Options

To determine which options you can configure for the bridge settings or bond settings, run:

    ifquery --syntax-help

## Loopback Interfaces

`ifupdown2` lets you configure IP addresses on loopback interfaces:

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th>ifupdown</th>
<th>ifupdown2</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><pre><code>auto lo
iface lo inet loopback
auto lo:1
iface lo:1 inet static
    address 10.1.1.1/32
auto lo:2
iface lo:2 inet static
   address 10.2.2.2/32</code></pre></td>
<td><pre><code>auto lo
iface lo inet loopback
   address 10.1.1.1/32
   address 10.2.2.2/32</code></pre></td>
</tr>
</tbody>
</table>

## Layer 2 Interfaces - Physical

In the original `ifupdown`, when the method is `manual`, you had to
specify `up link set $IFACE up` and `down link set $IFACE down` in the
configuration. `ifupdown2` does this for you automatically.

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th>ifupdown</th>
<th>ifupdown2</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><pre><code>auto swp19
iface swp19 inet manual
  up link set $IFACE up
  down link set $IFACE down
  pre-up /sbin/ethtool -s $IFACE speed 1000</code></pre></td>
<td><pre><code>auto swp19
iface swp19
   link-speed 1000</code></pre></td>
</tr>
</tbody>
</table>

The following is some debug code:

    sudo ifup -d swp19
    DEBUG: args = Namespace(CLASS=None, all=False, debug=True, excludepats=None, force=False, iflist=['swp19'], jobs=-1, noact=False, nocache=False, perfmode=False, printdependency=None, quiet=False, verbose=False, withdepends=False)
    DEBUG: creating ifupdown object ..
    INFO: loading builtin modules from /usr/share/ifupdownaddons
    INFO: looking for user scripts under /etc/network
    INFO: loading scripts under /etc/network/if-pre-up.d ...
    INFO: loading scripts under /etc/network/if-up.d ...
    INFO: loading scripts under /etc/network/if-post-up.d ...
    INFO: loading scripts under /etc/network/if-pre-down.d ...
    INFO: loading scripts under /etc/network/if-down.d ...
    INFO: loading scripts under /etc/network/if-post-down.d ...
    DEBUG: reading interfaces file /etc/network/interfaces
    WARNING: template engine mako not found. skip template parsing ..
    DEBUG: populating dependency info for ['swp19']
    DEBUG: run_without_dependents for ops ['pre-up', 'up', 'post-up'] for ['swp19']
    DEBUG: swp19: pre-up : running module bridge
    DEBUG: swp19: pre-up : running module mstpctl
    DEBUG: swp19: pre-up : running module vlan
    DEBUG: swp19: pre-up : running module address
    DEBUG: swp19: pre-up : running module usercmds
    DEBUG: running cmd 'ethtool -s swp19 speed 1000'
    INFO: Executing ethtool -s swp19 speed 1000
    DEBUG: swp19: pre-up : running script /etc/network/if-pre-up.d/ethtool
    DEBUG: Executing /etc/network/if-pre-up.d/ethtool
    DEBUG: swp19: up : running module dhcp
    DEBUG: swp19: up : running module link
    INFO: Executing ip link set dev swp19 up <===== Run for you now!
    DEBUG: swp19: up : running script /etc/network/if-up.d/ethtool
    DEBUG: Executing /etc/network/if-up.d/ethtool
    DEBUG: swp19: up : running script /etc/network/if-up.d/ip
    DEBUG: Executing /etc/network/if-up.d/ip
    DEBUG: swp19: up : running script /etc/network/if-up.d/mountnfs
    DEBUG: Executing /etc/network/if-up.d/mountnfs
    DEBUG: swp19: up : running script /etc/network/if-up.d/openssh-server
    DEBUG: Executing /etc/network/if-up.d/openssh-server
    DEBUG: swp19: post-up : running module usercmds

## Layer 2 Interfaces - Trunk

With `ifupdown2`, you do not need to define subinterfaces to add to the trunk. Just add it under the bridge interface.

Notice that the example uses `bridge-ports` instead of `mstpctl-ports`.

By default, `bridge-stp` turns on Rapid Spanning Tree.

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th>ifupdown</th>
<th>ifupdown2</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><pre><code>auto swp19
iface swp19 inet manual
  up link set $IFACE up
  down link set $IFACE down
  pre-up /sbin/ethtool -s $IFACE speed 1000

auto swp19.100
iface swp19.100 inet manual
  up link set $IFACE up
  down link set $IFACE down

auto swp19.200
iface swp19.200 inet manual
  up link set $IFACE up
  down link set $IFACE down

auto vlan100
iface vlan100 inet manual
bridge_ports swp19.100
mstpctl_stp on

auto vlan200
iface vlan200 inet manual
mstpctl_ports swp19.200
mstpctl_stp on</code></pre></td>
<td><pre><code>auto swp19
iface swp19
  link-speed 1000

auto vlan100
iface vlan100
  bridge-ports swp19.100
  bridge-stp on

auto vlan200
iface vlan200
  bridge-ports swp19.200
  bridge-stp on</code></pre></td>
</tr>
</tbody>
</table>

## Layer 2 Bond Interface - with Trunking

The following shows you how to configure bonds with trunking under `ifupdown2`.

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th>ifupdown</th>
<th>ifupdown2</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><pre><code>auto swp3
iface swp3 inet manual
  up link set $IFACE up
  down link set $IFACE down
  
auto swp4
iface swp4 inet manual
  up link set $IFACE up
  down link set $IFACE down
  
auto bond0
iface bond0 inet manual
  up link set $IFACE up
  down link set $IFACE down
  bond-slaves swp3 swp4
  bond-miimon 100
  bond-min-links 1
  bond-mode 802.3ad
  bond-xmit-hash-policy layer3+4
  bond-lacp-rate

auto bond0.100
iface bond0.100 inet manual
  up link set $IFACE up
  down link set $IFACE down
  
auto bond0.200
iface bond0.200 inet manual
  up link set $IFACE up
  down link set $IFACE down
  
auto vlan100
iface vlan100 inet manual
  up link set $IFACE up
  down link set $IFACE down
  mstpctl_ports bond0.100
  mstpctl_stp on
  
auto vlan200
iface vlan200 inet manual
  up link set $IFACE up
  down link set $IFACE down
  mstpctl_ports bond0.200
  mstpctl_stp on</code></pre></td>
<td><pre><code>auto swp3
iface swp3

auto swp4
iface swp4

auto bond0
iface bond0
  bond-slaves swp3 swp4
  bond-miimon 100
  bond-min-links 1
  bond-mode 802.3ad
  bond-xmit-hash-policy layer3+4
  bond-lacp-rate 1

auto vlan100
iface vlan100 
  bridge-ports bond0.100
  bridge-stp on

auto vlan200
iface vlan200
  bridge-ports bond0.200
  bridge-stp on</code></pre></td>
</tr>
</tbody>
</table>

## Layer 2 Trunk - Port Ranges

The *glob* keyword replaces regular expressions for creating port ranges, because it does not require mentioning the interfaces in `/etc/network/interfaces`. You can mention multiple glob statements in the stanza so you can configure a discontiguous port range.

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th>ifupdown</th>
<th>ifupdown2</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><pre><code>auto swp3
iface swp3 inet manual
  up link set $IFACE up
  down link set $IFACE down
  
auto swp3.100
iface swp3.100 inet manual
  up link set $IFACE up
  down link set $IFACE down
  
auto swp4
iface swp4 inet manual
  up link set $IFACE up
   down link set $IFACE down
   
auto swp4.100
iface swp4.100 inet manual
  up link set $IFACE up
  down link set $IFACE down

auto swp12
iface swp12 inet manual
  up link set $IFACE up
  down link set $IFACE down
  
auto swp12.100
iface swp12.100 inet manual
  up link set $IFACE up
  down link set $IFACE down
  
auto swp21
iface swp21 inet manual
  up link set $IFACE up
  down link set $IFACE down
  
auto swp21.100
iface swp21.100 inet manual
  up link set $IFACE up
  down link set $IFACE down
  
auto swp22
iface swp22 inet manual
  up link set $IFACE up
  down link set $IFACE down
  
auto swp22
iface swp22.100 inet manual
  up link set $IFACE up
  down link set $IFACE down
  
auto vlan100
iface vlan100 inet manual
  up link set $IFACE up
  down link set $IFACE down
  mstpctl_ports swp3.100 swp4.100 swp12.100 swp21.100 swp22.100
  mstpctl_stp on</code></pre></td>
<td><pre><code>auto swp3
iface swp3

auto swp4
iface swp4

auto swp12
iface swp12

auto swp21
iface swp21

auto swp22
iface swp22

auto vlan100
iface vlan100
  bridge-ports glob swp3-4.100 swp12.100 swp21-22.100
  bridge-stp on</code></pre></td>
</tr>
</tbody>
</table>

## IPv6 Address Assignment

ifupdown2 does not require configuring IPv6 addresses under an independent **inet6** section. You do all interface configuration under the same section. The same is true for the loopback configuration as well.

### Single IPv6 Address

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th>ifupdown</th>
<th>ifupdown2</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><pre><code>auto swp1
iface swp1 inet6 manual
  address 2001:db8::1/64
</code></pre></td>
<td><pre><code>auto swp1
iface swp1
  address 2001:db8::1/64</code></pre></td>
</tr>
</tbody>
</table>

### Multiple IPv6 Addresses

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th>ifupdown</th>
<th>ifupdown2</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><pre><code>auto swp1:1
iface swp1:1 inet6 manual
  address 2001:db8::1:1/64
auto swp1:2
iface swp1:2 inet6 manual
  address 2001:db8::2:2/64

</code></pre></td>
<td><pre><code>auto swp1
iface swp1
  address 2001:db8::1:1/64
  address 2001:db8::2:2/64</code></pre></td>
</tr>
</tbody>
</table>

<!-- vale off -->
## Setting Speed, Duplex and Auto-negotiation on a Port
<!-- vale on -->
`ifupdown2` now supports keywords to set the speed, duplex and auto-negotiation.

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th>ifupdown</th>
<th>ifupdown2</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><pre><code>auto swp1
iface swp1 inet static
  address 10.1.1.1/24
  mtu 9000
  pre-up /sbin/ethtool -s $IFACE speed 1000 duplex half autoneg off
  up ip link set $IFACE up
  down ip link set $IFACE down</code></pre></td>
<td><pre><code>auto swp1
iface swp1
  address 10.1.1.1/24
  mtu 9000
  link-speed 1000
  link-duplex half
  link-autoneg off</code></pre></td>
</tr>
</tbody>
</table>

## Setting the Port Description

`ifupdown2` lets you configure the IP address on loopback interfaces.

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th>ifupdown</th>
<th>ifupdown2</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><pre><code>auto swp1
iface swp1 inet static
  address 10.1.1.1/24
  post-up ip link set $IFACE alias customerA
  up ip link set $IFACE up
  down ip link set $IFACE down</code></pre></td>
<td><pre><code>auto swp1
iface swp1
  address 10.1.1.1/24
  alias customerA</code></pre></td>
</tr>
</tbody>
</table>

    # ip link show swp1
    3: swp1: <NO-CARRIER,BROADCAST,MULTICAST,UP> mtu 1500 qdisc pfifo_fast state DOWN mode DEFAULT qlen 500
        link/ether 08:9e:01:ce:dc:c2 brd ff:ff:ff:ff:ff:ff
        alias customerA

## Using the "source" Keyword to Place Interface Configuration in Files Other than /etc/network/interfaces

This is useful for automation. This example shows how Ansible writes individual port configs into the `/etc/network/ansible/` directory with `ifupdown2`.

To view all the configuration, run `ifquery -a`.

    auto lo
    iface lo inet loopback
    
    auto eth0
    iface eth0 inet dhcp
    
    source /etc/network/ansible/*

    # tree /etc/network/ansible
    /etc/network/ansible
    |-- swp1
    |-- swp2
    |-- swp3
    `-- swp4
    0 directories, 4 files
      
    # ifquery -a
    auto lo
    iface lo inet loopback
        address 10.3.3.3/32
        address 10:3:3::3/128
    auto eth0
    iface eth0 inet dhcp
    auto swp1
    iface swp1
        link-speed 1000
    auto swp2
    iface swp2
        link-speed 1000
    auto swp3
    iface swp3
        link-speed 10000
    auto swp4
    iface swp4
        address 10.200.1.1/24

## Creating the Default Configuration Using Mako

Mako is a templating engine that you can use to generate the `/etc/network/interfaces` configuration. Use it to generate a default configuration. The example below shows how to set defaults for bonds. By default, `ifupdown2` reads Mako files in the `/etc/network/ifupdown2/templates` directory. You can change this location in the `/etc/network/ifupdown2/ifupdown2.conf`. To view the expanded configuration, like a running config, run `ifquery bond0` or `ifquery -a`.

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th>ifupdown2 - /etc/network/interfaces</th>
<th>ifupdown2 - /etc/network/mako/bond_defaults</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><pre><code>iface lo inet loopback

auto eth0
iface eth0 inet dhcp

\#\#\# define name of default files and functions to use
&lt;%namespace file=&#39;bond_defaults&#39; import=&#39;bond_defaults&#39;/&gt;

auto swp1
iface swp1
   alias bond0-member

auto swp2
iface swp2
    alias bond0-member

auto bond0
iface bond0
     bond-slaves swp1 swp2
     ${bond_defaults()}</code></pre></td>
<td><pre><code>&lt;%def name=&quot;bond_defaults()&quot;&gt;
    bond-miimon 100 
    bond-min-links 1 
    bond-mode 802.3ad 
    bond-xmit-hash-policy layer3+4 
    bond-lacp-rate 1
&lt;/%def&gt;</code></pre></td>
</tr>
</tbody>
</table>

### ifquery Output

    #sudo ifquery -a
     
    auto lo
    iface lo inet loopback
     
    auto eth0
    iface eth0 inet dhcp
     
    auto swp1
    iface swp1
     
    auto swp2
    iface swp2
     
    auto bond0
    iface bond0
            bond-slaves swp1 swp2
            bond-miimon 100
            bond-min-links 1
            bond-mode 802.3ad
            bond-xmit-hash-policy layer3+4
            bond-lacp-rate 1

## See Also

{{<link url="Configure-the-interfaces-File-with-Mako">}}
