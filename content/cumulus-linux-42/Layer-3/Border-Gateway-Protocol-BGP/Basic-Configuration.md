---
title: Basic Configuration
author: Cumulus Networks
weight: 812
toc: 3
---
This section describes basic configuration for BGP *numbered* and BGP *unnumbered*.

## BGP Numbered

To configure numbered BGP on a switch, you need to:

- Assign an ASN to identify this BGP node. In a two-tier leaf and spine configuration, you can use {{<link title="Border Gateway Protocol - BGP#auto-bgp" text="auto BGP">}}, where Cumulus Linux assigns an ASN automatically.
- Assign a router ID, which is a 32-bit value and is typically the address of the loopback interface on the switch.
- Specify where to distribute routing information by providing the IP address and ASN of the neighbor. The ASN can be a number, or `internal` for a neighbor in the same AS or `external` for a neighbor in a different AS. For an iBGP session, the `remote-as` is the same as the local AS.

- Specify which prefixes to originate from this BGP node.

{{< tabs "10 ">}}

{{< tab "NCLU Commands ">}}

{{< tabs "109 ">}}

{{< tab " leaf01 ">}}

1. Identify the BGP node by assigning an ASN.

    - To assign an ASN manually:

      ```
      cumulus@switch:~$ net add bgp autonomous-system 65101
      ```

    - To use auto BGP to assign an ASN automatically on the leaf:

      ```
      cumulus@switch:~$ net add bgp auto leaf
      ```

      The auto BGP `leaf` keyword is only used to configure the ASN. The configuration files and `net show` commands display the ASN number only.

2. Assign the router ID.

    ```
    cumulus@switch:~$ net add bgp router-id 10.10.10.1
    ```

3. Specify the BGP neighbor to which you want to distribute routing information.

    ```
    cumulus@switch:~$ net add bgp neighbor 10.10.10.101 remote-as external
    ```

4. Specify which prefixes to originate:

    ```
    cumulus@switch:~$ net add bgp ipv4 unicast network 10.10.10.1/32
    cumulus@switch:~$ net add bgp ipv4 unicast network 10.1.10.0/24
    cumulus@switch:~$ net pending
    cumulus@switch:~$ net commit

   ```

{{< /tab >}}

{{< tab "spine01 ">}}

1. Identify the BGP node by assigning an ASN.

    - To assign an ASN manually:

      ```
      cumulus@switch:~$ net add bgp autonomous-system 65199
      ```

      To use auto BGP to assign an ASN automatically on the spine:

      ```
      cumulus@switch:~$ net add bgp auto spine
      ```

      The auto BGP `spine` keyword is only used to configure the ASN. The configuration files and `net show` commands display the ASN number only.

2. Assign the router ID.

    ```
    cumulus@switch:~$ net add bgp router-id 10.10.10.101
    ```

3. Specify the BGP neighbor to which you want to distribute routing information.

    ```
    cumulus@switch:~$ net add bgp neighbor 10.10.10.1 remote-as external
    ```

4. Specify which prefixes to originate:

    ```
    cumulus@switch:~$ net add bgp ipv4 unicast network 10.10.10.101/32
    cumulus@switch:~$ net pending
    cumulus@switch:~$ net commit

   ```

{{< /tab >}}

{{< /tabs >}}

{{< /tab >}}

{{< tab "vtysh Commands ">}}

{{< tabs "205 ">}}

{{< tab " leaf01 ">}}

1. Enable the `bgpd` daemon as described in {{<link title="Configure FRRouting">}}.

2. Identify the BGP node by assigning an ASN and the router ID:

    ```
    cumulus@switch:~$ sudo vtysh

    switch# configure terminal
    switch(config)# router bgp 65101
    switch(config-router)# bgp router-id 10.10.10.1
    ```

3. Specify where to distribute routing information:

    ```
    switch(config-router)# neighbor 10.10.10.101 remote-as external
    ```

    For an iBGP session, the `remote-as` is the same as the local AS.

5. Specify which prefixes to originate:

    ```
    switch(config-router)# address-family ipv4
    switch(config-router-af)# network 10.10.10.1/32
    switch(config-router-af)# network 10.1.10.0/24
    switch(config-router-af)# end
    switch# write memory
    switch# exit
    cumulus@switch:~$
    ```

{{< /tab >}}

{{< tab "spine01 ">}}

1. Enable the `bgpd` daemon as described in {{<link title="Configure FRRouting">}}.

2. Identify the BGP node by assigning an ASN and the router ID:

    ```
    cumulus@switch:~$ sudo vtysh

    switch# configure terminal
    switch(config)# router bgp 65199
    switch(config-router)# bgp router-id 10.10.10.101
    ```

3. Specify where to distribute routing information:

    ```
    switch(config-router)# neighbor 10.10.10.1 remote-as external
    ```

5. Specify which prefixes to originate:

    ```
    switch(config-router)# address-family ipv4
    switch(config-router-af)# network 10.10.10.101/32
    switch(config-router-af)# end
    switch# write memory
    switch# exit
    cumulus@switch:~$
    ```

{{< /tab >}}

{{< /tabs >}}

{{< /tab >}}

{{< /tabs >}}

The NCLU and `vtysh` commands save the configuration in the `/etc/frr/frr.conf` file. For example:

{{< tabs "2286 ">}}

{{< tab " leaf01 ">}}

```
...
router bgp 65101
 bgp router-id 10.10.10.1
 neighbor 10.10.10.101 remote-as external
 !
 address-family ipv4 unicast
  network 10.10.10.1/32
  network 10.1.10.0/24
 exit-address-family
...
```

{{< /tab >}}

{{< tab "spine01 ">}}

```
...
router bgp 65199
 bgp router-id 10.10.10.101
 neighbor 10.10.10.1 remote-as external
 !
 address-family ipv4 unicast
  network 10.10.10.101/32
 exit-address-family
...
```

{{< /tab >}}

{{< /tabs >}}

{{%notice note%}}

When using auto BGP, there are no references to `leaf` or `spine` in the configurations. Auto BGP determines the ASN for the system and configures it using standard vtysh commands.

{{%/notice%}}

## BGP Unnumbered

Historically, peers connect through IPv4 over TCP port 179 and after they establish a session, they exchange prefixes. When a BGP peer advertises an IPv4 prefix, it must include an IPv4 next hop address, which is usually the address of the advertising router. This requires that each BGP peer has an IPv4 address, which in a large network can consume a lot of address space, requiring a separate IP address for each peer-facing interface.

The BGP unnumbered standard, specified in {{<exlink url="https://tools.ietf.org/html/rfc5549" text="RFC 5549">}} uses *extended next hop encoding* (ENHE) and no longer requires an IPv4 prefix to be advertised along with an IPv4 next hop. This means that you can set up BGP peering between your Cumulus Linux switches and exchange IPv4 prefixes without having to configure an IPv4 address on each switch; the interfaces used by BGP are unnumbered.

The next hop address for each prefix is an IPv6 link-local address, which is assigned automatically to each interface. Using the IPv6 link-local address as a next hop instead of an IPv4 unicast address, BGP unnumbered saves you from having to configure IPv4 addresses on each interface.

When you use BGP unnumbered, BGP learns the prefixes, calculates the routes and installs them in IPv4 AFI to IPv6 AFI format. ENHE in Cumulus Linux does not install routes into the kernel in IPv4 prefix to IPv6 next hop format. For link-local peerings enabled by dynamically learning the other end's link-local address using IPv6 neighbor discovery router advertisements, an IPv6 next hop is converted into an IPv4 link-local address and a static neighbor entry is installed for this IPv4 link-local address with the MAC address derived from the link-local address of the other end.

{{%notice note%}}

- Interface-based peering with separate IPv4 and IPv6 sessions is not supported.
- If an IPv4 /30 or /31 IP address is assigned to the interface, IPv4 peering is used over IPv6 link-local peering.
- BGP unnumbered only works with two switches at a time, as it is designed to work with PTP (point-to-point protocol).
- The IPv6 implementation on the peering device uses the MAC address as the interface ID when assigning the IPv6 link-local address, as suggested by RFC 4291.

{{%/notice%}}

The following example commands show a basic BGP unnumbered configuration for two switches, leaf01 and spine01, which are eBPG peers.

The only difference between this BGP unnumbered configuration and the basic BGP configuration shown above, is that the BGP neighbour is specified as an interface (insead of an IP address).

{{< tabs "354 ">}}

{{< tab "NCLU Commands ">}}

{{< tabs "358 ">}}

{{< tab "leaf01 ">}}

```
cumulus@switch:~$ net add bgp autonomous-system 65101
cumulus@switch:~$ net add bgp router-id 10.10.10.1
cumulus@switch:~$ net add bgp neighbor swp51 remote-as external
cumulus@switch:~$ net add bgp ipv4 unicast network 10.10.10.1/32
cumulus@switch:~$ net add bgp ipv4 unicast network 10.1.10.0/24
cumulus@switch:~$ net pending
cumulus@switch:~$ net commit
```

{{< /tab >}}

{{< tab "spine01 ">}}

```
cumulus@switch:~$ net add bgp autonomous-system 65199
cumulus@switch:~$ net add bgp router-id 10.10.10.101
cumulus@switch:~$ net add bgp neighbor swp1 remote-as external
cumulus@switch:~$ net add bgp ipv4 unicast network 10.10.10.101/32
cumulus@switch:~$ net pending
cumulus@switch:~$ net commit
```

{{< /tab >}}

{{< /tabs >}}

{{< /tab >}}

{{< tab "vtysh Commands ">}}

{{< tabs "390 ">}}

{{< tab "leaf01 ">}}

```
cumulus@switch:~$ sudo vtysh

switch# configure terminal
switch(config)# router bgp 65101
switch(config-router)# bgp router-id 10.10.10.1
switch(config-router)# neighbor swp1 remote-as external
switch(config-router)# address-family ipv4
switch(config-router-af)# network 10.10.10.1/32
switch(config-router-af)# network 10.1.10.0/24
switch(config-router-af)# end
switch# write memory
switch# exit
cumulus@switch:~$
```

{{< /tab >}}

{{< tab "spine01 ">}}

```
cumulus@switch:~$ sudo vtysh

switch# configure terminal
switch(config)# router bgp 65199
switch(config-router)# bgp router-id 10.10.10.101
switch(config-router)# neighbor swp1 remote-as external
switch(config-router)# address-family ipv4
switch(config-router-af)# network 10.10.10.101/32
switch(config-router-af)# end
switch# write memory
switch# exit
cumulus@switch:~$
```

{{< /tab >}}

{{< /tabs >}}

{{< /tab >}}

{{< /tabs >}}

The NCLU and vtysh commands save the configuration in the `/etc/frr/frr.conf` file. For example:

{{< tabs "416 ">}}

{{< tab "leaf01 ">}}

```
...
router bgp 65101
 bgp router-id 10.10.10.1
 neighbor swp51 remote-as external
 !
 address-family ipv4 unicast
  network 10.10.10.1/32
  network 10.1.10.0/24
 exit-address-family
...
```

{{< /tab >}}

{{< tab "spine01 ">}}

```
...
router bgp 65199
 bgp router-id 10.10.10.101
 neighbor swp1 remote-as external
 !
 address-family ipv4 unicast
  network 10.10.10.101/32
 exit-address-family
...
```

{{< /tab >}}

{{< /tabs >}}

{{%notice note%}}

Every router or end host must have an IPv4 address to complete a `traceroute` of IPv4 addresses. In this case, the IPv4 address used is that of the loopback device.

Even if extended next-hop encoding (ENHE) is not used in the data center, link addresses are not typically advertised because:

- Link addresses take up valuable FIB resources. In a large Clos environment, the number of such addresses can be quite large.
- Link addresses expose an additional attack vector for intruders to use to either break in or engage in DDOS attacks.

Assigning an IP address to the loopback device is essential.

{{%/notice%}}

{{< expand "Advanced: How Next Hop Fields Are Set "  >}}

This section describes how the IPv6 next hops are set in the MP\_REACH\_NLRI ({{<exlink url="https://www.ietf.org/rfc/rfc2858.txt" text="multiprotocol reachable NLRI">}}) initiated by the system, which applies whether IPv6 prefixes or IPv4 prefixes are exchanged with ENHE. There are two main aspects to determine: how many IPv6 next hops are included in the MP\_REACH\_NLRI (the RFC allows either one or two next hops) and the values of the next hops. This section also describes how a received MP\_REACH\_NLRI is handled as far as processing IPv6 next hops.

- When peering to a global IPv6 address or link-local IPv6 address, whether to send one or two next hops is determined as follows:
    - If reflecting the route, two next hops are sent only if the peer has `nexthop-local unchanged` configured and the attribute of the received route has an IPv6 link-local next hop  otherwise, only one next hop is sent.
    - If not reflecting the route, two next hops are sent if explicitly configured (`nexthop-local unchanged`) or the peer is directly connected (either peering is on link-local address or the global IPv4 or IPv6 address is *directly connected*) and the route is either a local/self-originated route or the peer is an eBGP peer.
    - In all other cases, only one next hop is sent, unless an outbound route map adds another next hop.
- `route-map` can impose two next hops in scenarios where Cumulus Linux only sends one next hop - by specifying `set ipv6 nexthop link-local`.
- For all routes to eBGP peers and self-originated routes to iBGP peers, the global next hop (first value) is the peering address of the local system. If the peering is on the link-local address, this is the global IPv6 address on the peering interface, if present; otherwise, it is the link-local IPv6 address on the peering interface.
- For other routes to iBGP peers (eBGP to iBGP or reflected), the global next hop is the global next hop in the received attribute.

    {{%notice note%}}

If this address is a link-local IPv6 address, it is reset so that the link-local IPv6 address of the eBGP peer is not passed along to an iBGP peer, which is typically on a different link.

{{%/notice%}}

- `route-map` and/or the peer configuration can change the above behavior. For example, `route-map` can set the global IPv6 next hop or the peer configuration can set it to *self* - which is relevant for *iBGP* peers. The route map or peer configuration can also set the next hop to unchanged, which ensures the source IPv6 global next hop is passed around - which is relevant for *eBGP* peers.
- Whenever two next hops are being sent, the link-local next hop (the second value of the two) is the link-local IPv6 address on the peering interface unless it is due to `nh-local-unchanged` or `route-map` has set the link-local next hop.
- Network administrators cannot set {{<exlink url="http://en.wikipedia.org/wiki/Martian_packet" text="martian values">}} for IPv6 next hops in `route-map`. Also, global and link-local next hops are validated to ensure they match the respective address types.
- In a received update, a martian check is imposed for the IPv6 global next hop. If the check fails, it gets treated as an implicit withdraw.
- If two next hops are received in an update and the second next hop is not a link-local address, it gets ignored and the update is treated as if only one next hop was received.
- Whenever two next hops are received in an update, the second next hop is used to install the route into `zebra`. As per the previous point, it is already assured that this is a link-local IPv6 address. Currently, this is assumed to be reachable and is not registered with NHT.
- When `route-map` specifies the next hop as `peer-address`, the global IPv6 next hop as well as the link-local IPv6 next hop (if it's being sent) is set to the *peering address*. If the peering is on a link-local address, the former could be the link-local address on the peering interface, unless there is a global IPv6 address present on this interface.
- When using iBGP unnumbered with IPv6 Link Local Addresses (the default), FRR rewrites the BGP next hop to be the adjacent link. This is similar behavior to eBGP next hops. However, iBGP route advertisement rules do not change and a full mesh or route reflectors is still required.

The above rules imply that there are scenarios where a generated update has two IPv6 next hops, and both of them are the IPv6 link-local address of the peering interface on the local system. If you are peering with a switch or router that is not running Cumulus Linux and expects the first next hop to be a global IPv6 address, a route map can be used on the sender to specify a global IPv6 address. This conforms with the recommendations in the Internet draft {{<exlink url="https://tools.ietf.org/html/draft-kato-bgp-ipv6-link-local-00" text="draft-kato-bgp-ipv6-link-local-00.txt">}}, "BGP4+ Peering Using IPv6 Link-local Address."

{{< /expand >}}

{{%notice note%}}

The NCLU command to remove a BGP neighbor does not remove the BGP neighbor statement in the `/etc/network/interfaces` file when the BGP unnumbered interface belongs to a VRF. However, if the interface belongs to the default VRF, the BGP neighbor statement is removed.

{{%/notice%}}
