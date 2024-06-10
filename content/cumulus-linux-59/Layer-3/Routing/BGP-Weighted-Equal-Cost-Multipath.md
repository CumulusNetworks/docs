---
title: BGP Weighted Equal Cost Multipath
author: NVIDIA
weight: 780
toc: 3
---
You use <span class="a-tooltip">[W-ECMP](## "Weighted Equal Cost Multipath")</span> in data center networks that rely on anycast routing to provide network-based load balancing. Cumulus Linux supports BGP W-ECMP by using the <span class="a-tooltip">[BGP](## "Border Gateway Protocol")</span> link bandwidth extended community to load balance traffic towards anycast services for IPv4 and IPv6 routes in a layer 3 deployment and for prefix (type-5) routes in an EVPN deployment.
<!-- vale off -->
## W-ECMP Routing
<!-- vale on -->
In <span class="a-tooltip">[ECMP](## "Equal Cost Multi Path")</span>, the route to a destination has multiple next hops and traffic distributes across them equally. Flow-based hashing ensures that all traffic associated with a particular flow uses the same next hop and the same path across the network.

In W-ECMP, along with the ECMP flow-based hash, Cumulus Linux associates a weight with each next hop and distributes traffic across the next hops in proportion to their weight. The BGP link bandwidth extended community carries information about the anycast server distribution through the network, which maps to the weight of the corresponding next hop. The mapping factors the bandwidth value of a particular path against the total bandwidth values of all possible paths, mapped to the range 1 to 100. The BGP best path selection algorithm and the multipath computation algorithm that determines which paths you can use for load balancing does not change.
<!-- vale off -->
## W-ECMP Example
<!-- vale on -->
{{< img src = "/images/cumulus-linux/ucmp-example.png" >}}

The above example shows how traffic towards 192.168.10.1/32 is load balanced when you use W-ECMP routing:
- leaf01 has two ECMP paths to 192.168.10.1/32 (through server01 and server03) whereas leaf03 and leaf04 have a single path to server04.
- leaf01, leaf02, leaf03, and leaf04 generate a BGP link bandwidth based on the number of BGP multipaths for a prefix.
- When announcing the prefix to the spines, leaf01 and leaf02 generate a link bandwidth of two while leaf03 and leaf04 generate a link bandwidth of one.
- Each spine advertises the 192.168.10.1/32 prefix to the border leafs with an accumulated bandwidth of 6. This combines the value of 2 from leaf01, 2 from leaf02, 1 from leaf03 and 1 from leaf04.

Now, each spine has four W-ECMP routes:
- through leaf01 with weight 2
- through leaf02 with weight 2
- through leaf03 with weight 1
- through leaf04 with weight 1

The border leafs also have four W-ECMP routes:
- through spine01 with weight 6
- through spine02 with weight 6
- through spine03 with weight 6
- through spine04 with weight 6

The border leafs balance traffic equally; all weights are equal to the spines. Only the spines have unequal load sharing based on the weight values.
<!-- vale off -->
## Configure W-ECMP
<!-- vale on -->
Set the BGP link bandwidth extended community in a route map against all prefixes, a specific prefix, or set of prefixes using the match clause of the route map. Apply the route map on the first device to receive the prefix; against the BGP neighbor that generated this prefix.

The BGP link bandwidth extended community uses bytes-per-second. To convert the number of ECMP paths, Cumulus Linux uses a reference bandwidth of 1024Kbps. For example, if there are four ECMP paths to an anycast IP, the encoded bandwidth in the extended community is 512,000. The actual value is not important, as long as all routers originating the link bandwidth convert the number of ECMP paths in the same way.

Cumulus Linux accepts the bandwidth extended community by default. You do not need to configure transit devices where W-ECMP routes are not originated.

{{%notice note%}}
- The bandwidth used in the extended community has no impact on or relation to port bandwidth.
- You can only apply the route weight information on the outbound direction to a peer; you cannot apply route weight information on the inbound direction from peers advertising routes to the switch.
{{%/notice%}}

### Set the BGP Link Bandwidth Extended Community Against All Prefixes

The following example sets the BGP link bandwidth extended community against **all** prefixes.

{{< tabs "TabID59 ">}}
{{< tab "NVUE Commands">}}

```
cumulus@switch:~$ nv set router policy route-map ucmp-route-map rule 10 action permit 
cumulus@switch:~$ nv set router policy route-map ucmp-route-map rule 10 set ext-community-bw multipaths
cumulus@switch:~$ nv set vrf default router bgp neighbor swp51 address-family ipv4-unicast policy outbound route-map ucmp-route-map 
cumulus@switch:~$ nv config apply
```

{{< /tab >}}
{{< tab "vtysh Commands ">}}

```
cumulus@leaf01:~$ sudo vtysh
...
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

The following example sets the BGP link bandwidth extended community for anycast servers in the 192.168/16 IP address range.

{{< tabs "TabID102 ">}}
{{< tab "NVUE Commands">}}

```
cumulus@switch:~$ nv set router policy prefix-list anycast_ip type ipv4
cumulus@switch:~$ nv set router policy prefix-list anycast_ip rule 1 match 192.168.0.0/16 max-prefix-len 30
cumulus@switch:~$ nv set router policy prefix-list anycast_ip rule 1 action permit
cumulus@switch:~$ nv set router policy route-map ucmp-route-map rule 1 action permit 
cumulus@switch:~$ nv set router policy route-map ucmp-route-map rule 1 match ip-prefix-list anycast_ip
cumulus@switch:~$ nv set router policy route-map ucmp-route-map rule 1 set ext-community-bw multipaths
cumulus@switch:~$ nv set vrf default router bgp neighbor swp51 address-family ipv4-unicast policy outbound prefix-list anycast_ip 
cumulus@switch:~$ nv config apply
```

{{< /tab >}}
{{< tab "vtysh Commands ">}}

```
cumulus@leaf01:~$ sudo vtysh
...
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

For <span class="a-tooltip">[EVPN](## "Ethernet Virtual Private Network")</span> configuration, make sure that you activate the commands under the EVPN address family. The following shows an example EVPN configuration that sets the BGP link bandwidth extended community against **all** prefixes.

{{< tabs "TabID160 ">}}
{{< tab "NVUE Commands">}}

```
cumulus@switch:~$ nv set vrf turtle router bgp autonomous-system 65011
cumulus@switch:~$ nv set vrf turtle router bgp address-family ipv4-unicast route-export to-evpn route-map ucmp-route-map
cumulus@switch:~$ nv set router policy route-map ucmp-route-map rule 10 action permit
cumulus@switch:~$ nv set router policy route-map ucmp-route-map rule 10 set ext-community-bw cumulative
cumulus@switch:~$ nv config apply
```

{{< /tab >}}
{{< tab "vtysh Commands ">}}

```
cumulus@leaf01:~$ sudo vtysh
...
leaf01# configure terminal
leaf01(config)# route-map ucmp-route-map permit 10
leaf01(config-route-map)# set extcommunity bandwidth num-multipaths
leaf01(config-route-map)# router bgp 65011 vrf turtle
leaf01(config-router)# address-family l2vpn evpn
leaf01(config-router-af)# advertise ipv4 unicast route-map ucmp-route-map
leaf01(config-router-af)# end
leaf01# write memory
leaf01# exit
```

The vtysh commands save the configuration in the `/etc/frr/frr.conf` file. For example:

```
...
router bgp 65011 vrf turtle
 !
 address-family ipv4 unicast
  maximum-paths 64
  maximum-paths ibgp 64
 exit-address-family
 !
 address-family l2vpn evpn
  advertise ipv4 unicast route-map ucmp-route-map
 exit-address-family
...
```

{{< /tab >}}
{{< /tabs >}}
<!-- vale off -->
## Control W-ECMP on the Receiving Switch
<!-- vale on -->
To control W-ECMP on the receiving switch, you can:

- Set default values for W-ECMP routes.
- Disable the advertisement of all BGP extended communities on specific peerings.
<!-- vale off -->
### Set Default Values for W-ECMP Routes
<!-- vale on -->
By default, if some of the multipaths do not have link bandwidth, Cumulus Linux ignores the bestpath bandwidth value in any of the multipaths and performs ECMP. However, you can set one of the following options instead:

- Ignore link bandwidth and perform ECMP.
- Skip paths without link bandwidth and perform W-ECMP among the others (if at least some paths have link bandwidth).
- Assign a low default weight (value 1) to paths that do not have link bandwidth.

Change this setting per BGP instance for both IPv4 and IPv6 unicast routes in the BGP instance. For EVPN, set the options on the tenant VRF.

{{< tabs "TabID223 ">}}
{{< tab "NVUE Commands">}}

Run the NVUE `nv set vrf <vrf> router bgp path-selection multipath bandwidth ignore`, `nv set vrf <vrf> router bgp path-selection multipath bandwidth skip-missing`, or `nv set vrf <vrf> router bgp path-selection multipath bandwidth default-weight-for-missing` command.

The following example sets link bandwidth processing to skip paths without link bandwidth and perform W-ECMP among the other paths:

```
cumulus@switch:~$ nv set vrf default router bgp path-selection multipath bandwidth skip-missing
cumulus@switch:~$ nv config apply
```

{{< /tab >}}
{{< tab "vtysh Commands ">}}

Run the vtysh `bgp bestpath bandwidth ignore`, `bgp bestpath bandwidth skip-missing`, or `bgp bestpath bandwidth default-weight-for-missing` command.

The following example sets link bandwidth processing to skip paths without link bandwidth and perform UCMP among the other paths:

```
cumulus@switch:~$ sudo vtysh
...
switch# configure terminal
switch(config)# router bgp 65011
switch(config-router)# bgp bestpath bandwidth skip-missing
switch(config-router)# end
switch# write memory
switch# exit
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

The BGP link bandwidth extended community passes on automatically with the prefix to <span class="a-tooltip">[eBGP](## "external BGP")</span> peers. If you do not want to pass on the BGP link bandwidth extended community outside of a particular domain, you can disable the advertisement of all BGP extended communities on specific peerings.

{{%notice note%}}
You cannot disable just the BGP link bandwidth extended community from advertising to a neighbor; you either send all BGP extended communities, or none.
{{%/notice%}}

The following example disables all BGP extended communities on a peer:

{{< tabs "TabID284 ">}}
{{< tab "NVUE Commands">}}

```
cumulus@switch:~$ nv set vrf default router bgp neighbor swp51 address-family ipv4-unicast community-advertise extended off
cumulus@switch:~$ nv config apply
```

{{< /tab >}}
{{< tab "vtysh Commands ">}}

```
cumulus@switch:~$ sudo vtysh
...
switch# configure terminal
switch(config)# router bgp 65011
switch(config-router)# no neighbor 10.10.0.2 send-community extended
switch(config-router)# end
switch# write memory
switch# exit
```

{{< /tab >}}
{{< /tabs >}}

## Weight Normalization

The NVIDIA Spectrum switch supports weight programming for ECMP by repeating each individual path, which consumes resources. To reduce hardware utilization of ECMP resources, you can enable weight normalization.

To enable weight normalization:

```
cumulus@leaf01:mgmt:~$ nv set system forwarding ecmp-weight-normalisation mode enabled
cumulus@leaf01:mgmt:~$ nv config apply
```

To disable weight normalization, run the `nv set system forwarding ecmp-weight-normalisation mode disabled` command.

You can also adjust the maximum number of hardware entries for weighted ECMP by running the `nv set system forwarding ecmp-weight-normalisation max-hw-weight` command. You can specify a value between 10 and 255. The default value is 32.

```
cumulus@leaf01:mgmt:~$ nv set system forwarding ecmp-weight-normalisation max-hw-weight 100
cumulus@leaf01:mgmt:~$ nv config apply
```

{{%notice note%}}
Exercise caution when adjusting the maximum number of hardware entries. Configuring the setting too low consumes fewer resources but provides less weight granularity. Configuring the setting too high consumes more resources but provides more weight granularity.
{{%/notice%}}

<!-- vale off -->
## BGP W-ECMP with Adaptive Routing
<!-- vale on -->
Cumulus Linux supports BGP W-ECMP with {{<link title="#adaptive-routing" text="adaptive routing">}} for high-performance Ethernet topologies, where you use adaptive routing for optimal and efficient traffic distribution. You do not need to perform any additional configuration other than the configuration specified {{<link title="#configure-w-ecmp" text="above.">}}

- NVIDIA recommends using W-ECMP with adaptive routing on networks that have an equal number of links connecting the spine and leaf switches and where the port speed for the links is the same across all the switches.
- Both adaptive routing eligible traffic and non adaptive routing eligible traffic goes over the same ECMP group, which adjusts according to the W-ECMP weight. Non adaptive routing traffic continues to follow the hash-based traffic distribution between the updated list of next hops.

## Troubleshooting

To show the extended community in a received or local route, run the vtysh `show bgp` command.

The following example shows that the switch receives an IPv4 unicast route with the BGP link bandwidth attribute from two peers. The link bandwidth extended community is in bytes per second and shows in megabits per second: `Extended Community: LB:65002:131072000 (1000.000 Mbps) and Extended Community: LB:65001:65536000 (500.000 Mbps)`.

```
cumulus@switch:~$ sudo vtysh
...
switch# show ip bgp ipv4 unicast 192.168.10.1/32
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
The bandwidth value used by W-ECMP is only to determine the percentage of load to a given next hop and has no impact on actual link or flow bandwidth.
{{%/notice%}}

To show EVPN type-5 routes, run the vtysh `show bgp l2vpn evpn route type prefix` command.

The bandwidth shows both as bytes per second (unsigned 32 bits) as well as in Gbps, Mbps, or Kbps. For example:

```
cumulus@switch:~$ sudo vtysh
...
switch# show bgp l2vpn evpn route type prefix
BGP table version is 1, local router ID is 10.0.0.11
Status codes: s suppressed, d damped, h history, * valid, > best, i - internal
Origin codes: i - IGP, e - EGP, ? - incomplete
...
*> [5]:[0]:[32]:[192.168.10.1]
            10.0.0.5                           0 65100 65050 65200 i
            RT:65050:104001 LB:65050:134217728 (1.000 Gbps) ET:8 Rmac:36:4f:15:ea:81:90
```

To see weights associated with next hops for a route with multiple paths, run the vtysh `show ip route` command. For example:

```
cumulus@switch:~$ sudo vtysh
...
switch# show ip route 192.168.10.1/32
Routing entry for 192.168.10.1/32
  Known via "bgp", distance 20, metric 0, best
  Last update 00:00:32 ago
  * fe80::202:ff:fe00:1b, via swp2, weight 66
  * fe80::202:ff:fe00:15, via swp1, weight 33
```

## Considerations

W-ECMP with BGP link bandwidth is only available for BGP-learned routes.

## Related Information

{{<exlink url="https://tools.ietf.org/html/draft-ietf-idr-link-bandwidth-07" text="IETF draft - BGP Link Bandwidth Extended Community">}}
