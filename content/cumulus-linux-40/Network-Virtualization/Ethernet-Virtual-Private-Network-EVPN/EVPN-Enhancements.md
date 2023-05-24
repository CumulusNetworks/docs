---
title: EVPN Enhancements
author: NVIDIA
weight: 550
toc: 4
---
This section describes EVPN enhancements.

## Define RDs and RTs

When FRR learns about a local VNI and there is no explicit configuration for that VNI in FRR, the route distinguisher (RD), and import and export route targets (RTs) for this VNI are automatically derived. The RD uses *RouterId:VNI-Index* and the import and export RTs use *AS:VNI*. For routes that come from a layer 2 VNI (type-2 and type-3), the RD uses the `vxlan-local-tunnelip` from the layer 2 VNI interface instead of the RouterId (`vxlan-local-tunnelip:VNI`). The RD and RTs are used in the EVPN route exchange.

The RD disambiguates EVPN routes in different VNIs (as they may have the same MAC and/or IP address) while the RTs describe the VPN membership for the route. The *VNI-Index* used for the RD is a unique, internally-generated number for a VNI. It only has local significance; on remote switches, its only role is for route disambiguation. This number is used instead of the VNI value itself because this number has to be less than or equal to 65535. In the RT, the AS is always encoded as a 2-byte value to allow room for a large VNI. If the router has a 4-byte AS, only the lower 2 bytes are used. This ensures a unique RT for different VNIs while having the same RT for the same VNI across routers in the same AS.

For eBGP EVPN peering, the peers are in a different AS so using an automatic RT of *AS:VNI* does not work for route import. Therefore, the import RT is treated as *\*:VNI* to determine which received routes are applicable to a particular VNI. This only applies when the import RT is auto-derived and not configured.

If you do *not* want RDs and RTs to be derived automatically, you can define them manually. The following example commands are per VNI. You must specify these commands under `address-family l2vpn evpn` in BGP.

{{< tabs "TabID4" >}}

{{< tab "NCLU Commands" >}}

```
cumulus@switch:~$ net add bgp l2vpn evpn vni 10200 rd 172.16.100.1:20
cumulus@switch:~$ net add bgp l2vpn evpn vni 10200 route-target import 65100:20
cumulus@switch:~$ net add bgp l2vpn evpn advertise-all-vni
cumulus@switch:~$ net pending
cumulus@switch:~$ net commit
```

{{< /tab >}}

{{< tab "vtysh Commands" >}}

```
cumulus@switch:~$ sudo vtysh

switch# configure terminal
switch(config)# router bgp 65011
switch(config-router)# address-family l2vpn evpn
switch(config-router-af)# vni 10200
switch(config-router-af-vni)# rd 172.16.100.1:20
switch(config-router-af-vni)# route-target import 65100:20
switch(config-router-af-vni)# exit
switch(config-router-af)# advertise-all-vni
switch(config-router-af)# end
switch)# write memory
switch)# exit
cumulus@switch:~$
```

{{< /tab >}}

{{< /tabs >}}

These commands create the following configuration snippet in the `/etc/frr/frr.conf` file.

``` 
...
address-family l2vpn evpn
  advertise-all-vni
  vni 10200
   rd 172.16.100.1:20
   route-target import 65100:20
...
```

{{%notice note%}}
- If you delete the RD or RT later, it reverts back to its corresponding default value.
- Route target auto derivation does not support 4-byte AS numbers; If the router has a 4-byte AS, you must define the RTs manually.
{{%/notice%}}

You can configure multiple RT values. In addition, you can configure both the import and export route targets with a single command by using `route-target both`:

{{< tabs "TabID6" >}}

{{< tab "NCLU Commands" >}}

```
cumulus@switch:~$ net add bgp l2vpn evpn vni 10400 route-target import 100:400
cumulus@switch:~$ net add bgp l2vpn evpn vni 10400 route-target import 100:500
cumulus@switch:~$ net add bgp l2vpn evpn vni 10500 route-target both 65000:500
cumulus@switch:~$ net pending
cumulus@switch:~$ net commit
```

{{< /tab >}}

{{< tab "vtysh Commands" >}}

```
cumulus@switch:~$ sudo vtysh

switch# configure terminal
switch(config)# router bgp 65011
switch(config-router)# address-family l2vpn evpn
switch(config-router-af)# vni 10400
switch(config-router-af-vni)# route-target import 100:400
switch(config-router-af-vni)# route-target import 100:500
switch(config-router-af-vni)# exit
switch(config-router-af)# vni 10500
switch(config-router-af-vni)# route-target both 65000:500
switch(config-router-af)# end
switch)# write memory
switch)# exit
cumulus@switch:~$
```

{{< /tab >}}

{{< /tabs >}}

The above commands create the following configuration snippet in the `/etc/frr/frr.conf` file:

```
...
address-family l2vpn evpn
  vni 10400
    route-target import 100:400
    route-target import 100:500
  vni 10500
    route-target import 65000:500
    route-target export 65000:500
...
```

## Enable EVPN in an iBGP Environment with an OSPF Underlay

You can use EVPN with an {{<link url="Open-Shortest-Path-First-OSPF" text="OSPF">}} or static route underlay. This is a more complex configuration than using eBGP. In this case, iBGP advertises EVPN routes directly between VTEPs and the spines are unaware of EVPN or BGP.

The leaf switches peer with each other in a full mesh within the EVPN address family without using route reflectors. The leafs generally peer to their loopback addresses, which are advertised in OSPF. The receiving VTEP imports routes into a specific VNI with a matching route target community.

{{< tabs "TabID8" >}}

{{< tab "NCLU Commands" >}}

```
cumulus@switch:~$ net add bgp autonomous-system 65020
cumulus@switch:~$ net add bgp l2vpn evpn neighbor 10.1.1.2 remote-as internal
cumulus@switch:~$ net add bgp l2vpn evpn neighbor 10.1.1.3 remote-as internal
cumulus@switch:~$ net add bgp l2vpn evpn neighbor 10.1.1.4 remote-as internal
cumulus@switch:~$ net add bgp l2vpn evpn neighbor 10.1.1.2 activate
cumulus@switch:~$ net add bgp l2vpn evpn neighbor 10.1.1.3 activate
cumulus@switch:~$ net add bgp l2vpn evpn neighbor 10.1.1.4 activate
cumulus@switch:~$ net add bgp l2vpn evpn advertise-all-vni
cumulus@switch:~$ net add ospf router-id 10.1.1.1
cumulus@switch:~$ net add loopback lo ospf area 0.0.0.0
cumulus@switch:~$ net add ospf passive-interface lo
cumulus@switch:~$ net add interface swp50 ospf area 0.0.0.0
cumulus@switch:~$ net add interface swp51 ospf area 0.0.0.0
cumulus@switch:~$ net add interface swp50 ospf network point-to-point
cumulus@switch:~$ net add interface swp51 ospf network point-to-point
cumulus@switch:~$ net pending
cumulus@switch:~$ net commit
```

{{< /tab >}}

{{< tab "vtysh Commands" >}}

```
cumulus@switch:~$ sudo vtysh

switch# configure terminal
switch(config)# router bgp 65020
switch(config-router)# neighbor 10.1.1.2 remote-as internal
switch(config-router)# neighbor 10.1.1.3 remote-as internal
switch(config-router)# neighbor 10.1.1.4 remote-as internal
switch(config-router)# address-family l2vpn evpn
switch(config-router-af)# neighbor 10.1.1.2 activate
switch(config-router-af)# neighbor 10.1.1.3 activate
switch(config-router-af)# neighbor 10.1.1.4 activate
switch(config-router-af)# advertise-all-vni
switch(config-router-af)# exit
switch(config-router)# exit
switch(config)# router ospf
switch(config-router)# router-id 10.1.1.1
switch(config-router)# passive-interface lo
switch(config-router)# exit
switch(config)# interface lo
switch(config-if)# ip ospf area 0.0.0.0
switch(config-if)# exit
switch(config)# interface swp50
switch(config-if)# ip ospf area 0.0.0.0
switch(config-if)# ospf network point-to-point
switch(config-if)# exit
switch(config)# interface swp51
switch(config-if)# ip ospf area 0.0.0.0
switch(config-if)# ospf network point-to-point
switch(config-if)# end
switch)# write memory
switch)# exit
cumulus@switch:~$
```

{{< /tab >}}

{{< /tabs >}}

These commands create the following configuration snippet in the `/etc/frr/frr.conf` file.

```
...
interface lo
  ip ospf area 0.0.0.0
!
interface swp50
  ip ospf area 0.0.0.0
  ip ospf network point-to-point

interface swp51
  ip ospf area 0.0.0.0
  ip ospf network point-to-point
!
router bgp 65020
  neighbor 10.1.1.2 remote-as internal
  neighbor 10.1.1.3 remote-as internal
  neighbor 10.1.1.4 remote-as internal
  !
  address-family l2vpn evpn
  neighbor 10.1.1.2 activate
  neighbor 10.1.1.3 activate
  neighbor 10.1.1.4 activate
  advertise-all-vni
  exit-address-family
  !
Router ospf
  Ospf router-id 10.1.1.1
  Passive-interface lo
...
```

## ARP and ND Suppression

ARP suppression with EVPN allows a VTEP to suppress ARP flooding over VXLAN tunnels as much as possible. A local proxy handles ARP requests received from locally attached hosts for remote hosts. ARP suppression is the implementation for IPv4; ND suppression is the implementation for IPv6.

ARP/ND suppression is enabled by default on all VNIs in Cumulus Linux to reduce flooding of ARP/ND packets over VXLAN tunnels.

In a centralized routing deployment, you must configure layer 3 interfaces even if the switch is configured only for layer 2 (you are not using VXLAN routing). To avoid unnecessary layer 3 information from being installed, configure the `ip forward off` or `ip6 forward off` options as appropriate on the VLANs. See the example configuration below.

The following examples show a configuration using two VXLANs (10100 and 10200) and two VLANs (100 and 200).

{{< tabs "TabID10" >}}

{{< tab "NCLU Commands" >}}

```
cumulus@switch:~$ net add bridge bridge ports vni100,vni200
cumulus@switch:~$ net add bridge bridge vids 100,200
cumulus@switch:~$ net add vxlan vni100 vxlan id 10100
cumulus@switch:~$ net add vxlan vni200 vxlan id 10200
cumulus@switch:~$ net add vxlan vni100 bridge access 100
cumulus@switch:~$ net add vxlan vni200 bridge access 200
cumulus@switch:~$ net add vxlan vni100 vxlan local-tunnelip 10.0.0.1
cumulus@switch:~$ net add vxlan vni200 vxlan local-tunnelip 10.0.0.1
cumulus@switch:~$ net add vlan 100 ip forward off
cumulus@switch:~$ net add vlan 100 ipv6 forward off
cumulus@switch:~$ net add vlan 200 ip forward off
cumulus@switch:~$ net add vlan 200 ipv6 forward off
cumulus@switch:~$ net pending
cumulus@switch:~$ net commit
```

{{< /tab >}}

{{< tab "Linux Commands" >}}

Edit the `/etc/network/interfaces` file.

```
cumulus@switch:~$ sudo nano /etc/network/interfaces
...
auto bridge
iface bridge
    bridge-ports vni100 vni200
    bridge-stp on
    bridge-vids 100 200
    bridge-vlan-aware yes

auto vlan100
iface vlan100
    ip6-forward off
    ip-forward off
    vlan-id 100
    vlan-raw-device bridge

auto vlan200
iface vlan200
    ip6-forward off
    ip-forward off
    vlan-id 200
    vlan-raw-device bridge

auto vni100
iface vni100
    bridge-access 100
    vxlan-id 10100
    vxlan-local-tunnelip 10.0.0.1

auto vni200
iface vni200
      bridge-access 200
      vxlan-id 10200
      vxlan-local-tunnelip 10.0.0.1
...
```

{{< /tab >}}

{{< /tabs >}}

For a bridge in {{<link url="Traditional-Bridge-Mode" text="traditional mode">}}, you must edit the bridge configuration in the `/etc/network/interfaces` file using a text editor:

```
cumulus@switch:~$ sudo nano /etc/network/interfaces
...
auto bridge1
iface bridge1
    bridge-ports swp3.100 swp4.100 vni100
    ip6-forward off
    ip-forward off
...
```

When deploying EVPN and VXLAN using a hardware profile *other* than the default {{<link url="Routing#forwarding-table-profiles" text="Forwarding Table Profile">}}, ensure that the Linux kernel ARP `sysctl` settings `gc_thresh2` and `gc_thresh3` are both set to a value larger than the number of neighbor (ARP/ND) entries anticipated in the deployment. To configure these settings, edit the `/etc/sysctl.d/neigh.conf` file, then reboot the switch. If your network has more hosts than the values used in the example below, change the `sysctl` entries accordingly.

{{< expand " Example /etc/sysctl.d/neigh.conf file" >}}

```
cumulus@switch:~$ sudo nano /etc/sysctl.d/neigh.conf
...
net.ipv4.neigh.default.gc_thresh3=14336
net.ipv6.neigh.default.gc_thresh3=16384
net.ipv4.neigh.default.gc_thresh2=7168
net.ipv6.neigh.default.gc_thresh2=8192
...
```

{{< /expand >}}

Keep ARP and ND suppression enabled to reduce flooding of ARP and ND packets over VXLAN tunnels. However, if you need to disable ARP and ND suppression, edit the `/etc/network/interfaces` file to set `bridge-arp-nd-suppress off` on the VNI, then run the `ifreload -a` command:

```
cumulus@switch:~$ sudo nano /etc/network/interfaces
...

auto vni100
iface vni100
    bridge-access 100
    vxlan-id 10100
    vxlan-local-tunnelip 10.0.0.1
    bridge-arp-nd-suppress off

auto vni200
iface vni200
      bridge-access 200
      vxlan-id 10200
      vxlan-local-tunnelip 10.0.0.1
      bridge-arp-nd-suppress off
...
```

```
cumulus@switch:~$ sudo ifreload -a
```

{{%notice note%}}
NVIDIA recommends that you keep ARP and ND suppression enabled on all VXLAN interfaces on the switch. If you must disable suppression for a special use case, you can not disable ARP and ND suppression on some VXLAN interfaces but not others.
{{%/notice%}}

## Configure Static MAC Addresses

MAC addresses that are intended to be pinned to a particular VTEP can be provisioned on the VTEP as a static bridge FDB entry. EVPN picks up these MAC addresses and advertises them to peers as remote static MACs. You configure static bridge FDB entries for MACs under the bridge configuration:

{{< tabs "TabID38" >}}

{{< tab "NCLU Commands" >}}

```
cumulus@switch:~$ net add bridge post-up bridge fdb add 00:11:22:33:44:55 dev swp1 vlan 101 master static
cumulus@switch:~$ net pending
cumulus@switch:~$ net commit
```

For a bridge in {{<link url="Traditional-Bridge-Mode" text="traditional mode">}}, you must edit the bridge configuration in the `/etc/network/interfaces` file using a text editor:

```
cumulus@leaf01:~$ sudo nano /etc/network/interfaces
...
auto br101
iface br101
    bridge-ports swp1.101 vni10101
    post-up bridge fdb add 00:11:22:33:44:55 dev swp1.101 master static
...
```

{{< /tab >}}

{{< tab "Linux Commands" >}}

Edit the `/etc/network/interfaces` file. For example:

```
cumulus@leaf01:~$ sudo nano /etc/network/interfaces
...
auto bridge
iface bridge
    bridge-ports swp1 vni10101
    bridge-vids 101
    bridge-vlan-aware yes
    post-up bridge fdb add 00:11:22:33:44:55 dev swp1 vlan 101 master static
...
```

{{< /tab >}}

{{< /tabs >}}

## Filter EVPN Routes

It is common to subdivide the data center into multiple pods with full host mobility within a pod but only do prefix-based routing across pods. You can achieve this by only exchanging EVPN type-5 routes across pods.

The following example commands configure EVPN to advertise type-5 routes:

{{< tabs "TabID438 ">}}
{{< tab "NCLU Commands ">}}

```
cumulus@leaf01:~$ net add routing route-map map1 permit 1 match evpn route-type prefix
cumulus@leaf01:~$ net pending
cumulus@leaf01:~$ net commit
```

{{< /tab >}}
{{< tab "vtysh Commands ">}}

```
cumulus@leaf01:~$ sudo vtysh

leaf01# configure terminal
leaf01(config)# route-map map1 permit 1
leaf01(config)# match evpn route-type prefix
leaf01(config)# end
leaf01# write memory
leaf01# exit
cumulus@leaf01:~$
```

{{< /tab >}}
{{< /tabs >}}

In many situations, it is also desirable to only exchange EVPN routes carrying a particular VXLAN ID.
For example, if data centers or pods within a data center only share certain tenants, you can use a route map to control the EVPN routes exchanged based on the VNI.

The following example configures a route map that only advertises EVPN routes from VNI 1000:

{{< tabs "TabID474" >}}
{{< tab "NCLU Commands" >}}

```
cumulus@switch:~$ net add routing route-map map1 permit 1 match evpn vni 1000
cumulus@switch:~$ net pending
cumulus@switch:~$ net commit
```

{{< /tab >}}
{{< tab "vtysh Commands" >}}

```
cumulus@switch:~$ sudo vtysh

switch# configure terminal
switch(config)# route-map map1 permit 1
switch(config)# match evpn vni 1000
switch(config)# end
switch# write memory
switch# exit
cumulus@switch:~$
```

{{< /tab >}}
{{< /tabs >}}

{{%notice note%}}
You can only match type-2 and type-5 routes based on VNI.
{{%/notice%}}

## Advertise SVI IP Addresses

In a typical EVPN deployment, you *reuse* SVI IP addresses on VTEPs across multiple racks. However, if you use *unique* SVI IP addresses across multiple racks and you want the local SVI IP address to be reachable via remote VTEPs, you can enable the `advertise-svi-ip` option. This option advertises the SVI IP/MAC address as a type-2 route and eliminates the need for any flooding over VXLAN to reach the IP from a remote VTEP/rack.

{{%notice note%}}

- When you enable the `advertise-svi-ip` option, the anycast IP/MAC address pair is not advertised. Be sure **not** to enable both the `advertise-svi-ip` option and the `advertise-default-gw` option at the same time. (The `advertise-default-gw` option configures the gateway VTEPs to advertise their IP/MAC address. See {{<link url="Inter-subnet-Routing#centralized-routing" text="Advertising the Default Gateway">}}.
- If your switch is in an MLAG configuration, refer to {{<link url="Inter-subnet-Routing#advertise-primary-ip-address" text="Advertise Primary IP Address">}}.

{{%/notice%}}

To advertise *all* SVI IP/MAC addresses on the switch, run these commands:

{{< tabs "TabID487" >}}

{{< tab "NCLU Commands" >}}

```
cumulus@switch:~$ net add bgp l2vpn evpn advertise-svi-ip
cumulus@switch:~$ net pending
cumulus@switch:~$ net commit
```

{{< /tab >}}

{{< tab "vtysh Commands" >}}

```
cumulus@switch:~$ sudo vtysh

switch# configure terminal
switch(config)# router bgp 65011
switch(config-router)# address-family l2vpn evpn 
switch(config-router-af)# advertise-svi-ip
switch(config-router-af)# end
switch)# write memory
switch)# exit
cumulus@switch:~$

cumulus@switch:~$ sudo cat /etc/frr/frr.conf
...
address-family l2vpn evpn
  advertise-svi-ip
exit-address-family
...
```

{{< /tab >}}

{{< /tabs >}}

To advertise a *specific* SVI IP/MAC address, run these commands:

{{< tabs "TabID527" >}}

{{< tab "NCLU Commands" >}}

```
cumulus@switch:~$ net add bgp l2vpn evpn vni 10 advertise-svi-ip
cumulus@switch:~$ net pending
cumulus@switch:~$ net commit
```

{{< /tab >}}

{{< tab "vtysh Commands" >}}

```
cumulus@switch:~$ sudo vtysh

switch# configure terminal
switch(config)# router bgp 65011
switch(config-router)# address-family l2vpn evpn 
switch(config-router-af)# vni 10
switch(config-router-af-vni)# advertise-svi-ip
switch(config-router-af-vni)# end
switch)# write memory
switch)# exit
cumulus@switch:~$
```

{{< /tab >}}

{{< /tabs >}}

The NCLU and vtysh commands save the configuration in the `/etc/frr/frr.conf` file. For example:

```
cumulus@switch:~$ sudo cat /etc/frr/frr.conf
...
address-family l2vpn evpn
  vni 10
  advertise-svi-ip
exit-address-family
...
```

## Extended Mobility

Cumulus Linux supports scenarios where the IP to MAC binding for a host or virtual machine changes across the move. In addition to the simple mobility scenario where a host or virtual machine with a binding of `IP1`, `MAC1` moves from one rack to another, Cumulus Linux supports additional scenarios where a host or virtual machine with a binding of `IP1`, `MAC1` moves and takes on a new binding of `IP2`, `MAC1` or `IP1`, `MAC2`. The EVPN protocol mechanism to handle extended mobility continues to use the MAC mobility extended community and is the same as the standard mobility procedures. Extended mobility defines how the sequence number in this attribute is computed when binding changes occur.

Extended mobility not only supports virtual machine *moves*, but also where one virtual machine shuts down and another is provisioned on a different rack that uses the IP address or the MAC address of the previous virtual machine. For example, in an EVPN deployment with OpenStack, where virtual machines for a tenant are provisioned and shut down very dynamically, a new virtual machine can use the same IP address as an earlier virtual machine but with a different MAC address.

{{%notice note%}}
During mobility events, EVPN neighbor management relies on ARP and GARP to learn the new location for hosts and VMs. MAC learning is independent of this and happens in the hardware.
{{%/notice%}}

The support for extended mobility is enabled by default and does not require any additional configuration.

You can examine the sequence numbers associated with a host or virtual machine MAC address and IP address with the NCLU `net show evpn mac vni <vni> mac <address>` command or the vtysh `show evpn mac vni <vni> mac <address>` command. For example:

```
cumulus@switch:~$ net show evpn mac vni 10100 mac 00:02:00:00:00:42
MAC: 00:02:00:00:00:42
  Remote VTEP: 10.0.0.2
  Local Seq: 0 Remote Seq: 3
  Neighbors:
    10.1.1.74 Active

cumulus@switch:~$ net show evpn arp vni 10100 ip 10.1.1.74
IP: 10.1.1.74
  Type: local
  State: active
  MAC: 44:39:39:ff:00:24
  Local Seq: 2 Remote Seq: 3
```

## Duplicate Address Detection

Cumulus Linux is able to detect duplicate MAC and IPv4/IPv6 addresses on hosts or virtual machines in a VXLAN-EVPN configuration. The Cumulus Linux switch (VTEP) considers a host MAC or IP address to be duplicate if the address moves across the network more than a certain number of times within a certain number of seconds (five moves within 180 seconds by default). In addition to legitimate host or VM mobility scenarios, address movement can occur when IP addresses are misconfigured on hosts or when packet looping occurs in the network due to faulty configuration or behavior.

Duplicate address detection is enabled by default and triggers when:

- Two hosts have the same MAC address (the host IP addresses might be the same or different)
- Two hosts have the same IP address but different MAC addresses

By default, when a duplicate address is detected, Cumulus Linux flags the address as a duplicate and generates an error in syslog so that you can troubleshoot the reason and address the fault, then clear the duplicate address flag. No functional action is taken on the address.

{{%notice note%}}

If a MAC address is flagged as a duplicate, all IP addresses associated with that MAC are flagged as duplicates.

{{%/notice%}}

{{%notice note%}}

In an MLAG configuration, MAC mobility detection runs independently on each switch in the MLAG pair. Based on the sequence in which local learning and/or route withdrawal from the remote VTEP occurs, a type-2 route might have its MAC mobility counter incremented only on one of the switches in the MLAG pair. In rare cases, it is possible for neither VTEP to increment the MAC mobility counter for the type-2 prefix.

{{%/notice%}}

### When Does Duplicate Address Detection Trigger?

The VTEP that sees an address move from remote to local begins the detection process by starting a timer. Each VTEP runs duplicate address detection independently. Detection always starts with the first mobility event from *remote* to *local*. If the address is initially remote, the detection count can start with the very first move for the address. If the address is initially local, the detection count starts only with the second or higher move for the address. If an address is undergoing a mobility event between remote VTEPs, duplicate detection is not started. 

The following illustration shows VTEP-A, VTEP-B, and VTEP-C in an EVPN configuration. Duplicate address detection triggers on VTEP-A when there is a duplicate MAC address for two hosts attached to VTEP-A and VTEP-B. However, duplicate detection does *not* trigger on VTEP-A when mobility events occur between two remote VTEPs (VTEP-B and VTEP-C).

{{< img src = "/images/cumulus-linux/evpn-dad-example.png" >}}

### Configure Duplicate Address Detection

To change the threshold for MAC and IP address moves, run the `net add bgp l2vpn evpn dup-addr-detection max-moves <number-of-events> time <duration>` command. You can specify `max-moves` to be between 2 and 1000 and `time` to be between 2 and 1800 seconds.

The following example command sets the maximum number of address moves allowed to 10 and the duplicate address detection time interval to 1200 seconds.

{{< tabs "TabID634" >}}

{{< tab "NCLU Commands" >}}

```
cumulus@switch:~$ net add bgp l2vpn evpn dup-addr-detection max-moves 10 time 1200 
```

{{< /tab >}}

{{< tab "vtysh Commands" >}}

```
cumulus@switch:~$ sudo vtysh

switch# configure terminal
switch(config)# router bgp 65011
switch(config-router)# address-family l2vpn evpn 
switch(config-router-af)# dup-addr-detection max-moves 10 time 1200
switch(config-router-af)# end
switch)# write memory
switch)# exit
cumulus@switch:~$ 
```

{{< /tab >}}

{{< /tabs >}}

To disable duplicate address detection, see {{<link url="#disable-duplicate-address-detection" text="Disable Duplicate Address Detection">}} below.

### Example syslog Messages

The following example shows the syslog message that is generated when Cumulus Linux detects a MAC address as a duplicate during a local update:

```
2018/11/06 18:55:29.463327 ZEBRA: [EC 4043309149] VNI 1001: MAC 00:01:02:03:04:11 detected as duplicate during local update, last VTEP 172.16.0.16
```

The following example shows the syslog message that is generated when Cumulus Linux detects an IP address as a duplicate during a remote update:

```
2018/11/09 22:47:15.071381 ZEBRA: [EC 4043309151] VNI 1002: MAC aa:22:aa:aa:aa:aa IP 10.0.0.9 detected as duplicate during remote update, from VTEP 172.16.0.16
```

### Freeze a Detected Duplicate Address

Cumulus Linux provides a *freeze* option that takes action on a detected duplicate address. You can freeze the address *permanently* (until you intervene) or for a *defined amount of time*, after which it is cleared automatically.

When you enable the freeze option and a duplicate address is detected:

- If the MAC or IP address is learned from a remote VTEP at the time it is frozen, the forwarding information in the kernel and hardware is not updated, leaving it in the prior state. Any future remote updates are processed but they are not reflected in the kernel entry. If the remote VTEP sends a MAC-IP route withdrawal, the local VTEP removes the frozen remote entry. Then, if the local VTEP has a locally-learned entry already present in its kernel, FRR will originate a corresponding MAC-IP route and advertise it to all remote VTEPs.
- If the MAC or IP address is locally learned on this VTEP at the time it is frozen, the address is not advertised to remote VTEPs. Future local updates are processed but are not advertised to remote VTEPs. If FRR receives a local entry delete event, the frozen entry is removed from the FRR database. Any remote updates (from other VTEPs) change the state of the entry to remote but the entry is not installed in the kernel (until cleared).

**To recover from a freeze**, shut down the faulty host or VM or fix any other misconfiguration in the network. If the address is frozen *permanently,* issue the {{<link url="#clear-duplicate-addresses" text="clear command">}} on the VTEP where the address is marked as duplicate. If the address is frozen for a defined period of time, it is cleared automatically after the timer expires (you can clear the duplicate address before the timer expires with the {{<link url="#clear-duplicate-addresses" text="clear command">}}).

{{%notice note%}}

If you issue the clear command or the timer expires before you address the fault, duplicate address detection might occur repeatedly.

{{%/notice%}}

After you clear a frozen address, if it is present behind a remote VTEP, the kernel and hardware forwarding tables are updated. If the address is locally learned on this VTEP, the address is advertised to remote VTEPs. All VTEPs get the correct address as soon as the host communicates . Silent hosts are learned only after the faulty entries age out, or you intervene and clear the faulty MAC and ARP table entries.

### Configure the Freeze Option

To enable Cumulus Linux to *freeze* detected duplicate addresses, run the `net add bgp l2vpn evpn dup-addr-detection freeze <duration>|permanent` command. The duration can be any number of seconds between 30 and 3600.

The following example command freezes duplicate addresses for a period of 1000 seconds, after which it is cleared automatically:

{{< tabs "TabID704" >}}

{{< tab "NCLU Commands" >}}

```
cumulus@switch:~$ net add bgp l2vpn evpn dup-addr-detection freeze 1000
```

{{< /tab >}}

{{< tab "vtysh Commands" >}}

```
cumulus@switch:~$ sudo vtysh

switch# configure terminal
switch(config)# router bgp 65011
switch(config-router)# address-family l2vpn evpn
switch(config-router-af)# dup-addr-detection freeze 1000
switch(config-router-af)# end
switch)# write memory
switch)# exit
cumulus@switch:~$
```

{{< /tab >}}

{{< /tabs >}}

{{%notice note%}}

Set the freeze timer to be three times the duplicate address detection window. For example, if the duplicate address detection window is set to the default of 180 seconds, set the freeze timer to 540 seconds.

{{%/notice%}}

The following example command freezes duplicate addresses permanently (until you issue the {{<link url="#clear-duplicate-addresses" text="clear command">}}):

{{< tabs "TabID741" >}}

{{< tab "NCLU Commands" >}}

```
cumulus@switch:~$ net add bgp l2vpn evpn dup-addr-detection freeze permanent
```

{{< /tab >}}

{{< tab "vtysh Commands" >}}

```
cumulus@switch:~$ sudo vtysh

switch# configure terminal
switch(config)# router bgp 65011
switch(config-router)# address-family l2vpn evpn 
switch(config-router-af)# dup-addr-detection freeze permanent
switch(config-router-af)# end
switch)# write memory
switch)# exit
cumulus@switch:~$
```

{{< /tab >}}

{{< /tabs >}}

### Clear Duplicate Addresses

You can clear a duplicate MAC or IP address (and unfreeze a frozen address). The following example command clears IP address 10.0.0.9 for VNI 101.

{{< tabs "TabID774" >}}

{{< tab "NCLU Commands" >}}

```
cumulus@switch:~$ net clear evpn dup-addr vni 101 ip 10.0.0.9
```

{{< /tab >}}

{{< tab "vtysh Commands" >}}

```
cumulus@switch:~$ sudo vtysh

switch# clear evpn dup-addr vni 101 ip 10.0.0.9
switch)# exit
cumulus@switch:~$
```

{{< /tab >}}

{{< /tabs >}}

To clear duplicate addresses for all VNIs, run the following command:

{{< tabs "TabID800" >}}

{{< tab "NCLU Commands" >}}

```
cumulus@switch:~$ net clear evpn dup-addr vni all
```

{{< /tab >}}

{{< tab "vtysh Commands" >}}

```
cumulus@switch:~$ sudo vtysh

switch# clear evpn dup-addr vni all
switch)# exit
cumulus@switch:~$
```

{{< /tab >}}

{{< /tabs >}}

{{%notice note%}}

In an MLAG configuration, you need to run the clear command on both the MLAG primary and secondary switch.

{{%/notice%}}

{{%notice note%}}

When you clear a duplicate MAC address, all its associated IP addresses are also cleared. However, you cannot clear an associated IP address if its MAC address is still in a duplicate state.

{{%/notice%}}

### Disable Duplicate Address Detection

By default, duplicate address detection is enabled and a syslog error is generated when a duplicate address is detected. To disable duplicate address detection, run the following command.

{{< tabs "TabID840" >}}

{{< tab "NCLU Commands" >}}

```
cumulus@switch:~$ net del bgp l2vpn evpn dup-addr-detection
```

{{< /tab >}}

{{< tab "vtysh Commands" >}}

```
cumulus@switch:~$ sudo vtysh

switch# configure terminal
switch(config)# router bgp 65011
switch(config-router)# address-family l2vpn evpn
switch(config-router-af)# no dup-addr-detection
switch(config-router-af)# end
switch)# write memory
switch)# exit
cumulus@switch:~$
```

{{< /tab >}}

{{< /tabs >}}

When you disable duplicate address detection, Cumulus Linux clears the configuration and all existing duplicate addresses.

### Show Detected Duplicate Address Information

During the duplicate address detection process, you can see the start time and current detection count with the NCLU `net show evpn mac vni <vni_id> mac <mac_addr>` command or the vtysh `show evpn mac vni <vni_id> mac <mac_addr>` command. The following command example shows that detection started for MAC address 00:01:02:03:04:11 for VNI 1001 on Tuesday, Nov 6 at 18:55:05 and the number of moves detected is 1.

```
cumulus@switch:~$ net show evpn mac vni 1001 mac 00:01:02:03:04:11
MAC: 00:01:02:03:04:11
  Intf: hostbond3(15) VLAN: 1001
  Local Seq: 1 Remote Seq: 0
  Duplicate detection started at Tue Nov  6 18:55:05 2018, detection count 1
  Neighbors:
    10.0.1.26 Active
```

After the duplicate MAC address is cleared, the NCLU `net show evpn mac vni <vni_id> mac <mac_addr>` command or the vtysh `show evpn mac vni <vni_id> mac <mac_addr>` command shows:

```
MAC: 00:01:02:03:04:11
  Remote VTEP: 172.16.0.16
  Local Seq: 13 Remote Seq: 14
  Duplicate, detected at Tue Nov  6 18:55:29 2018
  Neighbors:
    10.0.1.26 Active
```

To display information for a duplicate IP address, run the NCLU `net show evpn arp-cache vni <vni_id> ip <ip_addr>` command or the vtysh `show evpn arp-cache vni <vni_id> ip <ip_addr>` command. The following command example shows information for IP address 10.0.0.9 for VNI 1001.

```
cumulus@switch:~$ net show evpn arp-cache vni 1001 ip 10.0.0.9
IP: 10.0.0.9
  Type: remote
  State: inactive
  MAC: 00:01:02:03:04:11
  Remote VTEP: 10.0.0.34
  Local Seq: 0 Remote Seq: 14
  Duplicate, detected at Tue Nov  6 18:55:29 2018
```

To show a list of MAC addresses detected as duplicate for a specific VNI or for all VNIs, run the NCLU `net show evpn mac vni <vni-id|all> duplicate` command or the vtysh `show evpn mac vni <vni-id|all> duplicate` command. The following example command shows a list of duplicate MAC addresses for VNI 1001:

``` 
cumulus@switch:~$ net show evpn mac vni 1001 duplicate
Number of MACs (local and remote) known for this VNI: 16
MAC               Type   Intf/Remote VTEP      VLAN
aa:bb:cc:dd:ee:ff local  hostbond3             1001  
```

To show a list of IP addresses detected as duplicate for a specific VNI or for all VNIs, run the NCLU `net show evpn arp-cache vni <vni-id|all> duplicate` command or the vtysh `show evpn arp-cache vni <vni-id|all> duplicate` command. The following example command shows a list of duplicate IP addresses for VNI 1001:

```
cumulus@switch:~$ net show evpn arp-cache vni 1001 duplicate
Number of ARPs (local and remote) known for this VNI: 20
IP                Type   State    MAC                Remote VTEP
10.0.0.8          local  active   aa:11:aa:aa:aa:aa
10.0.0.9          local  active   aa:11:aa:aa:aa:aa
10.10.0.12        remote active   aa:22:aa:aa:aa:aa  172.16.0.16
```

To show configured duplicate address detection parameters, run the NCLU `net show evpn` command or the vtysh `show evpn` command:

```
cumulus@switch:~$ net show evpn
L2 VNIs: 4
L3 VNIs: 2
Advertise gateway mac-ip: No
Duplicate address detection: Enable
  Detection max-moves 7, time 300
  Detection freeze permanent
```
