---
title: Basic BGP Configuration
author: Cumulus Networks
weight: 812
toc: 3
---
This section describes how to configure BGP using either BGP *numbered* or BGP *unnumbered*. With BGP *unnumbered*, you can set up BGP peering between your Cumulus Linux switches and exchange IPv4 prefixes without having to configure an IPv4 address on each switch.

## BGP Numbered

To configure BGP numbered on a BGP node, you need to:

- Assign an ASN to identify this BGP node. In a two-tier leaf and spine configuration, you can use {{<link title="Border Gateway Protocol - BGP#auto-bgp" text="auto BGP">}}, where Cumulus Linux assigns an ASN automatically.
- Assign a router ID, which is a 32-bit value and is typically the address of the loopback interface on the switch.
- Specify where to distribute routing information by providing the IP address and ASN of the neighbor.
  - For BGP numbered, this is the IP address of the the interface between the two peers; the interface must be a layer 3 access port.
  - The ASN can be a number, or `internal` for a neighbor in the same AS or `external` for a neighbor in a different AS.
- Specify which prefixes to originate from this BGP node.

{{< tabs "10 ">}}

{{< tab "NCLU Commands ">}}

{{< tabs "109 ">}}

{{< tab " leaf01 ">}}

1. Identify the BGP node by assigning an ASN.

    - To assign an ASN manually:

      ```
      cumulus@leaf01:~$ net add bgp autonomous-system 65101
      ```

    - To use auto BGP to assign an ASN automatically on the leaf:

      ```
      cumulus@leaf01:~$ net add bgp auto leaf
      ```

      The auto BGP `leaf` keyword is only used to configure the ASN. The configuration files and `net show` commands display the ASN number only.

2. Assign the router ID.

    ```
    cumulus@leaf01:~$ net add bgp router-id 10.10.10.1
    ```

3. Specify the BGP neighbor to which you want to distribute routing information.

    ```
    cumulus@leaf01:~$ net add bgp neighbor 169.254.10.101 remote-as external
    ```

    For BGP to advertise IPv6 prefixes, you need to an additional command to activate the BGP neighbor under the IPv6 address family:

    ```
    cumulus@leaf01:~$ net add bgp neighbor 2001:db8:0002::0a00:0002 remote-as external
    cumulus@leaf01:~$ net add bgp ipv6 unicast neighbor 2001:db8:0002::0a00:0002 activate
    ```

    For BGP to advertise *IPv4* prefixes with IPv6 next hops, see {{<link url="Optional-BGP-Configuration#advertise-ipv4-prefixes-with-ipv6-next-hops" text="Advertise IPv4 Prefixes with IPv6 Next Hops">}}.

4. Specify which prefixes to originate:

    ```
    cumulus@leaf01:~$ net add bgp ipv4 unicast network 10.10.10.1/32
    cumulus@leaf01:~$ net add bgp ipv4 unicast network 10.1.10.0/24
    cumulus@leaf01:~$ net pending
    cumulus@leaf01:~$ net commit
   ```

   IPv6 prefix example:

   ```
   cumulus@leaf01:~$ net add bgp ipv6 unicast network 2001:db8::1/128
   cumulus@leaf01:~$ net pending
   cumulus@leaf01:~$ net commit
   ```

{{< /tab >}}

{{< tab "spine01 ">}}

1. Identify the BGP node by assigning an ASN.

    - To assign an ASN manually:

      ```
      cumulus@spine01:~$ net add bgp autonomous-system 65199
      ```

      To use auto BGP to assign an ASN automatically on the spine:

      ```
      cumulus@spine01:~$ net add bgp auto spine
      ```

      The auto BGP `spine` keyword is only used to configure the ASN. The configuration files and `net show` commands display the ASN number only.

2. Assign the router ID.

    ```
    cumulus@spine01:~$ net add bgp router-id 10.10.10.101
    ```

3. Specify the BGP neighbor to which you want to distribute routing information.

    ```
    cumulus@spine01:~$ net add bgp neighbor 169.254.10.1 remote-as external
    ```

    For BGP to advertise IPv6 prefixes, you need to an additional command to activate the BGP neighbor under the IPv6 address family:

    ```
    cumulus@spine01:~$ net add bgp neighbor 2001:db8:0002::0a00:1 remote-as external
    cumulus@spine01:~$ net add bgp ipv6 unicast neighbor 2001:db8:0002::0a00:1 activate
    ```

    For BGP to advertise *IPv4* prefixes with IPv6 next hops, see {{<link url="Optional-BGP-Configuration#advertise-ipv4-prefixes-with-ipv6-next-hops" text="Advertise IPv4 Prefixes with IPv6 Next Hops">}}.

4. Specify which prefixes to originate:

    ```
    cumulus@spine01:~$ net add bgp ipv4 unicast network 10.10.10.101/32
    cumulus@spine01:~$ net pending
    cumulus@spine01:~$ net commit
   ```

   IPv6 prefix example:

   ```
   cumulus@spine01:~$ net add bgp ipv6 unicast network 2001:db8::101/128
   cumulus@spine01:~$ net pending
   cumulus@spine01:~$ net commit
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
    cumulus@leaf01:~$ sudo vtysh

    leaf01# configure terminal
    leaf01(config)# router bgp 65101
    leaf01(config-router)# bgp router-id 10.10.10.1
    ```

3. Specify where to distribute routing information:

   ```
   leaf01(config-router)# neighbor 169.254.10.101 remote-as external
   ```

   For BGP to advertise IPv6 prefixes, you need to an additional command to activate the BGP neighbor under the IPv6 address family:

   ```
   leaf01(config-router)# neighbor 2001:db8:0002::0a00:1 remote-as external
   leaf01(config-router)# address-family ipv6 unicast
   leaf01(config-router-af)# neighbor 2001:db8:0002::0a00:1 activate
   ```

   For BGP to advertise *IPv4* prefixes with IPv6 next hops, see {{<link url="Optional-BGP-Configuration#rfc-5549-support-with-global-ipv6-peers" text="RFC 5549 Support with Global IPv6 Peers">}}.

5. Specify which prefixes to originate:

    ```
    leaf01(config-router)# address-family ipv4
    leaf01(config-router-af)# network 10.10.10.1/32
    leaf01(config-router-af)# network 10.1.10.0/24
    leaf01(config-router-af)# end
    leaf01# write memory
    leaf01# exit
    cumulus@switch:~$
    ```

    IPv6 prefix example:

    ```
    leaf01(config-router)# address-family ipv4
    leaf01(config-router-af)# network 2001:db8::1/128
    leaf01(config-router-af)# end
    leaf01# write memory
    leaf01# exit
    cumulus@switch:~$
    ```

{{< /tab >}}

{{< tab "spine01 ">}}

1. Enable the `bgpd` daemon as described in {{<link title="Configure FRRouting">}}.

2. Identify the BGP node by assigning an ASN and the router ID:

    ```
    cumulus@spine01:~$ sudo vtysh

    spine01# configure terminal
    spine01(config)# router bgp 65199
    spine01(config-router)# bgp router-id 10.10.10.101
    ```

3. Specify where to distribute routing information:

    ```
    spine01(config-router)# neighbor 169.254.10.1 remote-as external
    ```

   For BGP to advertise IPv6 prefixes, you need to an additional command to activate the BGP neighbor under the IPv6 address family:

   ```
   spine01(config-router)# neighbor 2001:db8:0002::0a00:0002 remote-as external
   spine01(config-router)# address-family ipv6 unicast
   spine01(config-router-af)# neighbor 2001:db8:0002::0a00:0002 activate
   ```

   For BGP to advertise *IPv4* prefixes with IPv6 next hops, see {{<link url="Optional-BGP-Configuration#rfc-5549-support-with-global-ipv6-peers" text="RFC 5549 Support with Global IPv6 Peers">}}.

5. Specify which prefixes to originate:

    ```
    spine01(config-router)# address-family ipv4
    spine01(config-router-af)# network 10.10.10.101/32
    spine01(config-router-af)# end
    spine01# write memory
    spine01# exit
    cumulus@spine01:~$
    ```

    IPv6 prefixes:

    ```
    spine01(config-router)# address-family ipv4
    spine01(config-router-af)# network 2001:db8::101/128
    spine01(config-router-af)# end
    spine01# write memory
    spine01# exit
    cumulus@spine01:~$
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
 neighbor 169.254.10.101 remote-as external
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
 neighbor 169.254.10.1 remote-as external
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

The following example commands show a basic BGP unnumbered configuration for two switches, leaf01 and spine01, which are eBPG peers.

The only difference between this BGP unnumbered configuration and the BGP numbered configuration shown above, is that the BGP neighbour is specified as an interface (insead of an IP address). The interface between the two peers does **not** need to have an IP address configured on each side.

{{< tabs "354 ">}}

{{< tab "NCLU Commands ">}}

{{< tabs "358 ">}}

{{< tab "leaf01 ">}}

```
cumulus@leaf01:~$ net add bgp autonomous-system 65101
cumulus@leaf01:~$ net add bgp router-id 10.10.10.1
cumulus@leaf01:~$ net add bgp neighbor swp51 remote-as external
cumulus@leaf01:~$ net add bgp ipv4 unicast network 10.10.10.1/32
cumulus@leaf01:~$ net add bgp ipv4 unicast network 10.1.10.0/24
cumulus@leaf01:~$ net pending
cumulus@leaf01:~$ net commit
```

{{< /tab >}}

{{< tab "spine01 ">}}

```
cumulus@spine01:~$ net add bgp autonomous-system 65199
cumulus@spine01:~$ net add bgp router-id 10.10.10.101
cumulus@spine01:~$ net add bgp neighbor swp1 remote-as external
cumulus@spine01:~$ net add bgp ipv4 unicast network 10.10.10.101/32
cumulus@spine01:~$ net pending
cumulus@spine01:~$ net commit
```

{{< /tab >}}

{{< /tabs >}}

{{< /tab >}}

{{< tab "vtysh Commands ">}}

{{< tabs "390 ">}}

{{< tab "leaf01 ">}}

```
cumulus@switch:~$ sudo vtysh

leaf01# configure terminal
leaf01(config)# router bgp 65101
leaf01(config-router)# bgp router-id 10.10.10.1
leaf01(config-router)# neighbor swp1 remote-as external
leaf01(config-router)# address-family ipv4
leaf01(config-router-af)# network 10.10.10.1/32
leaf01(config-router-af)# network 10.1.10.0/24
leaf01(config-router-af)# end
leaf01# write memory
leaf01# exit
cumulus@leaf01:~$
```

{{< /tab >}}

{{< tab "spine01 ">}}

```
cumulus@spine01:~$ sudo vtysh

spine01# configure terminal
spine01(config)# router bgp 65199
spine01(config-router)# bgp router-id 10.10.10.101
spine01(config-router)# neighbor swp1 remote-as external
spine01(config-router)# address-family ipv4
spine01(config-router-af)# network 10.10.10.101/32
spine01(config-router-af)# end
spine01# write memory
spine01# exit
cumulus@spine01:~$
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

{{%notice note%}}

The NCLU command to remove a BGP neighbor does not remove the BGP neighbor statement in the `/etc/network/interfaces` file when the BGP unnumbered interface belongs to a VRF. However, if the interface belongs to the default VRF, the BGP neighbor statement is removed.

{{%/notice%}}
