---
title: Unequal Cost Multipath with BGP Link Bandwidth
author: NVIDIA
weight: 780
toc: 3
---
You use Unequal Cost Multipath (UCMP) in data center networks that rely on anycast routing to provide network-based load balancing. Cumulus Linux supports UCMP by using the BGP link bandwidth extended community to load balance traffic towards anycast services for IPv4 and IPv6 routes in a layer 3 deployment and for prefix (type-5) routes in an EVPN deployment.

## UCMP Routing

In ECMP, the route to a destination has multiple next hops and traffic distributes across them equally. Flow-based hashing ensures that all traffic associated with a particular flow uses the same next hop and the same path across the network.

In UCMP, along with the ECMP flow-based hash, Cumulus Linux associates a weight with each next hop and distributes traffic across the next hops in proportion to their weight. The BGP link bandwidth extended community carries information about the anycast server distribution through the network, which maps to the weight of the corresponding next hop. The mapping factors the bandwidth value of a particular path against the total bandwidth values of all possible paths, mapped to the range 1 to 100. The BGP best path selection algorithm and the multipath computation algorithm that determines which paths you can use for load balancing does not change.

## UCMP Example

{{< img src = "/images/cumulus-linux/ucmp-example.png" >}}

The above example shows how traffic towards 192.168.10.1/32 is load balanced when you use UCMP routing:

- Leaf01 has two ECMP paths to 192.168.10.1/32 (via Server01 and Server03) whereas Leaf03 and Leaf04 have a single path to Server04.
- Leaf01, Leaf02, Leaf03, and Leaf04 generate a BGP link bandwidth based on the number of BGP multipaths for a prefix.
- When announcing the prefix to the spines, Leaf01 and Leaf02 generate a link bandwidth of two while Leaf03 and Leaf04 generate a link bandwidth of one.
- Each spine advertises the 192.168.10.1/32 prefix to the border leafs with an accumulated bandwidth of 6. This combines the value of 2 from Leaf01, 2 from Leaf02, 1 from Leaf03 and 1 from Leaf04.

Now, each spine has four UCMP routes:

- through Leaf01 with weight 2
- through Leaf02 with weight 2
- through Leaf03 with weight 1
- through Leaf04 with weight 1

The border leafs also have four UCMP routes:

- through Spine01 with weight 6
- through Spine02 with weight 6
- through Spine03 with weight 6
- through Spine04 with weight 6

The border leafs balance traffic equally; all weights are equal to the spines. Only the spines have unequal load sharing based on the weight values.

## Configure UCMP

Use the `set extcommunity bandwidth num-multipaths` command in a route map to set the extended community against all prefixes, or against a specific or set of prefixes using the match clause of the route map. Apply the route map at the first device to receive the prefix; against the BGP neighbor that generated this prefix.

The BGP link bandwidth extended community uses bytes-per-second. To convert the number of ECMP paths, Cumulus Linux uses a reference bandwidth of 1024Kbps. For example, if there are four ECMP paths to an anycast IP, the encoded bandwidth in the extended community is 512,000. The actual value is not important, as long as all routers originating the link bandwidth convert the number of ECMP paths in the same way.

Cumulus Linux accepts the bandwidth extended community by default. You do not need to configure transit devices where UCMP routes are not originated.

{{%notice note%}}
- NVUE commands are not supported.
- The bandwidth used in the extended community has no impact on or relation to port bandwidth.
- You can only apply the route weight information on the outbound direction to a peer; you cannot apply route weight information on the inbound direction from peers advertising routes to the switch.
{{%/notice%}}

### Set the BGP Link Bandwidth Extended Community Against All Prefixes

The following command examples show how you can set the BGP link bandwidth extended community against **all** prefixes.

{{< tabs "TabID61 ">}}
{{< tab "NCLU Commands ">}}

```
cumulus@leaf01:~$ net add routing route-map ucmp-route-map permit 10 set extcommunity bandwidth num-multipaths
cumulus@leaf01:~$ net add bgp neighbor 10.1.1.1 route-map ucmp-route-map out
cumulus@leaf01:~$ net pending
cumulus@leaf01:~$ net commit
```

The NCLU commands save the configuration in the `/etc/frr/frr.conf` file. For example:

```
...
address-family ipv4 unicast
 neighbor 10.1.1.1 route-map ucmp-route-map out
!
route-map ucmp-route-map permit 10
 set extcommunity bandwidth num-multipaths
...
```

{{< /tab >}}
{{< tab "vtysh Commands ">}}

```
cumulus@leaf01:~$ sudo vtysh
leaf01# configure terminal
leaf01(config)# route-map ucmp-route-map permit 10
leaf01(config-route-map)# set extcommunity bandwidth num-multipaths
leaf01(config-route-map)# exit
leaf01(config)# router bgp 65011
leaf01(config-router)# address-family ipv4 unicast
leaf01(config-router)# neighbor 10.1.1.1 route-map ucmp-route-map out
leaf01(config-router)# end
leaf01# write memory
leaf01# exit
cumulus@leaf01:~$
```

The vtysh commands save the configuration in the `/etc/frr/frr.conf` file. For example:

```
...
address-family ipv4 unicast
 neighbor 10.1.1.1 route-map ucmp-route-map out
!
route-map ucmp-route-map permit 10
 set extcommunity bandwidth num-multipaths
...
```

{{< /tab >}}
{{< /tabs >}}

### Set the BGP Link Bandwidth Extended Community Against Certain Prefixes

The following command examples show how you can set the BGP link bandwidth extended community for anycast servers in the 192.168/16 IP address range.

{{< tabs "TabID111 ">}}
{{< tab "NCLU Commands ">}}

```
cumulus@leaf01:~$ net add routing prefix-list ipv4 anycast-ip permit 192.168.0.0/16 le 32
cumulus@leaf01:~$ net add routing route-map ucmp-route-map permit 10 match ip address prefix-list anycast-ip
cumulus@leaf01:~$ net add routing route-map ucmp-route-map permit 10 set extcommunity bandwidth num-multipaths
cumulus@leaf01:~$ net add bgp neighbor 10.1.1.1 route-map ucmp-route-map out
cumulus@leaf01:~$ net pending
cumulus@leaf01:~$ net commit
```

The NCLU commands save the configuration in the `/etc/frr/frr.conf` file. For example:

```
...
address-family ipv4 unicast
 neighbor 10.1.1.1 route-map ucmp-route-map out
!
ip prefix-list anycast-ip permit 192.168.0.0/16 le 32
route-map ucmp-route-map permit 10
 match ip address prefix-list anycast-ip
 set extcommunity bandwidth num-multipaths
...
```

{{< /tab >}}
{{< tab "vtysh Commands ">}}

```
cumulus@leaf01:~$ sudo vtysh
leaf01# configure terminal
leaf01(config)# ip prefix-list anycast_ip seq 10 permit 192.168.0.0/16 le 32
leaf01(config)# route-map ucmp-route-map permit 10
leaf01(config-route-map)# match ip address prefix-list anycast_ip
leaf01(config-route-map)# set extcommunity bandwidth num-multipaths
leaf01(config-route-map)# router bgp 65011
leaf01(config-router)# address-family ipv4 unicast
leaf01(config-router-af)# neighbor swp51 prefix-list anycast_ip out
leaf01(config-router-af)# end
leaf01# write memory
leaf01# exit
cumulus@leaf01:~$
```

The vtysh commands save the configuration in the `/etc/frr/frr.conf` file. For example:

```
...
address-family ipv4 unicast
 neighbor 10.1.1.1 route-map ucmp-route-map out
!
ip prefix-list anycast-ip permit 192.168.0.0/16 le 32
route-map ucmp-route-map permit 10
 match ip address prefix-list anycast-ip
 set extcommunity bandwidth num-multipaths
...
```

{{< /tab >}}
{{< /tabs >}}

### EVPN Configuration

For EVPN configuration, make sure that you activate the commands under the EVPN address family. The following shows an example EVPN configuration that sets the BGP link bandwidth extended community against **all** prefixes.

{{< tabs "TabID166 ">}}
{{< tab "NCLU Commands ">}}

```
cumulus@leaf01:~$ net add routing route-map ucmp-route-map permit 10 set extcommunity bandwidth num-multipaths
cumulus@leaf01:~$ net add bgp vrf turtle l2vpn evpn advertise ipv4 unicast route-map ucmp-route-map
cumulus@leaf01:~$ net pending
cumulus@leaf01:~$ net commit
```

The NCLU commands save the configuration in the `/etc/frr/frr.conf` file. For example:

```
...
 address-family l2vpn evpn
  advertise ipv4 unicast route-map ucmp-route-map
 exit-address-family
!
ip prefix-list anycast-ip permit 192.168.0.0/16 le 32
route-map ucmp-route-map permit 10
 match ip address prefix-list anycast-ip
 set extcommunity bandwidth num-multipaths
...
```

{{< /tab >}}
{{< tab "vtysh Commands ">}}

```
cumulus@leaf01:~$ sudo vtysh
leaf01# configure terminal
leaf01(config)# route-map ucmp-route-map permit 10
leaf01(config-route-map)# set extcommunity bandwidth num-multipaths
leaf01(config-route-map)# router bgp 65011 vrf turtle
leaf01(config-router)# address-family l2vpn evpn
leaf01(config-router-af)# advertise ipv4 unicast route-map ucmp-route-map
leaf01(config-router-af)# end
leaf01# write memory
leaf01# exit
cumulus@leaf01:~$
```

The vtysh commands save the configuration in the `/etc/frr/frr.conf` file. For example:

```
...
 address-family l2vpn evpn
  advertise ipv4 unicast route-map ucmp-route-map
 exit-address-family
!
ip prefix-list anycast-ip permit 192.168.0.0/16 le 32
route-map ucmp-route-map permit 10
 match ip address prefix-list anycast-ip
 set extcommunity bandwidth num-multipaths
...
```

{{< /tab >}}
{{< /tabs >}}

## Control UCMP on the Receiving Switch

To control UCMP on the receiving switch, you can:

- Set default values for UCMP routes.
- Disable the advertisement of all BGP extended communities on specific peerings.

### Set Default Values for UCMP Routes

By default, if some of the multipaths do not have link bandwidth, Cumulus Linux ignores the bestpath bandwidth value in any of the multipaths and performs ECMP. However, you can set one of the following options instead:

- Ignore link bandwidth and perform ECMP.
- Skip paths without link bandwidth and perform UCMP among the others (if at least some paths have link bandwidth).
- Assign a low default weight (value 1) to paths that do not have link bandwidth.

Change this setting per BGP instance for both IPv4 and IPv6 unicast routes in the BGP instance. For EVPN, set the options on the tenant VRF.

Either run the NCLU `net add bestpath bandwidth ignore|skip-missing|default-weight-for-missing` command or the vtysh `bgp bestpath bandwidth ignore|skip-missing|default-weight-for-missing` command.

The following commands set link bandwidth processing to skip paths without link bandwidth and perform UCMP among the other paths:

{{< tabs "TabID235 ">}}
{{< tab "NCLU Commands ">}}

```
cumulus@switch:~$ net add bgp bestpath bandwidth skip-missing
cumulus@switch:~$ net pending
cumulus@switch:~$ net commit
```

The NCLU commands save the configuration in the `/etc/frr/frr.conf` file. For example:

```
router bgp 65011
  bgp bestpath as-path multipath-relax
  neighbor LEAF peer-group
  neighbor LEAF remote-as external
  neighbor swp1 interface peer-group LEAF
  neighbor swp2 interface peer-group LEAF
  neighbor swp3 interface peer-group LEAF
  neighbor swp4 interface peer-group LEAF
  bgp bestpath bandwidth skip-missing
!
  address-family ipv4 unicast
    network 10.0.0.1/32
  exit-address-family
 ...
 ```

{{< /tab >}}
{{< tab "vtysh Commands ">}}

```
cumulus@switch:~$ sudo vtysh
switch# configure terminal
switch(config)# router bgp 65011
switch(config-router)# bgp bestpath bandwidth skip-missing
switch(config-router)# end
switch# write memory
switch# exit
cumulus@switch:~$
```

The vtysh commands save the configuration in the `/etc/frr/frr.conf` file. For example:

```
router bgp 65011
  bgp bestpath as-path multipath-relax
  neighbor LEAF peer-group
  neighbor LEAF remote-as external
  neighbor swp1 interface peer-group LEAF
  neighbor swp2 interface peer-group LEAF
  neighbor swp3 interface peer-group LEAF
  neighbor swp4 interface peer-group LEAF
  bgp bestpath bandwidth skip-missing
!
  address-family ipv4 unicast
    network 10.0.0.1/32
  exit-address-family
 ...
 ```

{{< /tab >}}
{{< /tabs >}}

### BGP Link Bandwidth Outside a Domain

The BGP link bandwidth extended community is automatically passed on with the prefix to eBGP peers. If you do not want to pass on the BGP link bandwidth extended community outside of a particular domain, you can disable the advertisement of all BGP extended communities on specific peerings.

{{%notice note%}}
You cannot disable just the BGP link bandwidth extended community from advertising to a neighbor; you either send all BGP extended communities, or none.
{{%/notice%}}

To disable all BGP extended communities on a peer or peer group (per address family), either run the NCLU `net del bgp neighbor <neighbor> send-community extended` command or the vtysh `no neighbor <neighbor> send-community extended` command:

{{< tabs "TabID295 ">}}
{{< tab "NCLU Commands ">}}

```
cumulus@switch:~$ net del bgp neighbor 10.10.0.2 send-community extended
cumulus@switch:~$ net pending
cumulus@switch:~$ net commit
```

{{< /tab >}}
{{< tab "vtysh Commands ">}}

```
cumulus@switch:~$ sudo vtysh
switch# configure terminal
switch(config)# router bgp 65011
switch(config-router)# no neighbor 10.10.0.2 send-community extended
switch(config-router)# end
switch# write memory
switch# exit
cumulus@switch:~$
```

{{< /tab >}}
{{< /tabs >}}

## Troubleshooting

To show the extended community in a received or local route, run the NCLU `net show bgp` command or the vtysh `show bgp` command.

The following example shows that the switch receives an IPv4 unicast route with the BGP link bandwidth attribute from two peers. The link bandwidth extended community is in bytes-per-second and shows in Mbps per second: `Extended Community: LB:65002:131072000 (1000.000 Mbps) and Extended Community: LB:65001:65536000 (500.000 Mbps)`.

```
cumulus@switch:~$ net show bgp ipv4 unicast 192.168.10.1/32
BGP routing table entry for 192.168.10.1/32
Paths: (2 available, best #2, table default)
  Advertised to non peer-group peers:
  l1(swp1) l2(swp2) l3(swp3) l4(swp4)
  65002
    fe80::202:ff:fe00:1b from l2(swp2) (10.0.0.2)
    (fe80::202:ff:fe00:1b) (used)
      Origin IGP, metric 0, valid, external, multipath, bestpath-from-AS 65002
      Extended Community: LB:65002:131072000 (1000.000 Mbps)
      Last update: Thu Feb 20 18:34:16 2020

  65001
    fe80::202:ff:fe00:15 from l1(swp1) (110.0.0.1)
    (fe80::202:ff:fe00:15) (used)
      Origin IGP, metric 0, valid, external, multipath, bestpath-from-AS 65001, best (Older Path)
      Extended Community: LB:65001:65536000 (500.000 Mbps)
      Last update: Thu Feb 20 18:22:34 2020
```

{{%notice note%}}
The bandwidth value used by UCMP is only to determine the percentage of load to a given next hop and has no impact on actual link or flow bandwidth.
{{%/notice%}}

To show EVPN type-5 routes, run the NCLU `net show bgp l2vpn evpn route type prefix` command or the vtysh `show bgp l2vpn evpn route type prefix` command.

The bandwidth shows both as bytes-per-second (unsigned 32 bits) as well as in Gbps, Mbps, or Kbps. For example:

```
cumulus@switch:~$ net show bgp l2vpn evpn route type prefix
BGP table version is 1, local router ID is 10.0.0.11
Status codes: s suppressed, d damped, h history, * valid, > best, i - internal
Origin codes: i - IGP, e - EGP, ? - incomplete
...
*> [5]:[0]:[32]:[192.168.10.1]
            10.0.0.5                           0 65100 65050 65200 i
            RT:65050:104001 LB:65050:134217728 (1.000 Gbps) ET:8 Rmac:36:4f:15:ea:81:90
```

To see weights associated with next hops for a route with multiple paths, run the NCLU `net show route` command or the vtysh `show ip route` command. For example:

```
cumulus@switch:~$ net show route 192.168.10.1/32
Routing entry for 192.168.10.1/32
  Known via "bgp", distance 20, metric 0, best
  Last update 00:00:32 ago
  * fe80::202:ff:fe00:1b, via swp2, weight 66
  * fe80::202:ff:fe00:15, via swp1, weight 33
```

## Considerations

UCMP with BGP link bandwidth is only available for BGP-learned routes.

## Related Information

{{<exlink url="https://tools.ietf.org/html/draft-ietf-idr-link-bandwidth-07" text="IETF draft - BGP Link Bandwidth Extended Community">}}
