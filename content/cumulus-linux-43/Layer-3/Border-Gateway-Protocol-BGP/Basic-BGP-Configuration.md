---
title: Basic BGP Configuration
author: NVIDIA
weight: 850
toc: 3
---
This section describes how to configure BGP using either BGP numbered or {{<link title="Border Gateway Protocol - BGP#bgp-unnumbered" text="BGP unnumbered">}}. With BGP *unnumbered*, you can set up BGP peering between your Cumulus Linux switches and exchange IPv4 prefixes without having to configure an IPv4 address on each switch.

{{%notice note%}}
BGP *unnumbered* simplifies configuration and is recommended for data center deployments.
{{%/notice%}}

## BGP Numbered

To configure BGP numbered on a BGP node, you need to:
- Assign an ASN to identify this BGP node. In a two-tier leaf and spine configuration, you can use {{<link title="Border Gateway Protocol - BGP#auto-bgp" text="auto BGP">}}, where Cumulus Linux assigns an ASN automatically.
- Assign a router ID, which is a 32-bit value and is typically the address of the loopback interface on the switch.
- Specify where to distribute routing information by providing the IP address and ASN of the neighbor.
  - For BGP numbered, this is the IP address of the interface between the two peers; the interface must be a layer 3 access port.
  - The ASN can be a number, or `internal` for a neighbor in the same AS or `external` for a neighbor in a different AS.
- Specify which prefixes to originate from this BGP node.

{{< tabs "10 ">}}

{{< tab "NCLU Commands ">}}

{{%notice info%}}
When you commit a change that configures a new routing service such as BGP, the FRR daemon restarts and might interrupt network operations for other configured routing services.
{{%/notice%}}

{{< tabs "109 ">}}

{{< tab " leaf01 ">}}

1. Identify the BGP node by assigning an ASN.

    - To assign an ASN manually:

      ```
      cumulus@leaf01:~$ net add bgp autonomous-system 65101
      ```

    - To use auto BGP to assign an ASN automatically on the leaf:
    <!-- laclac: CUE-2562 auto BGP.  This is not implemented in CUE yet. -->

      ```
      cumulus@leaf01:~$ net add bgp auto leaf
      ```

      The auto BGP `leaf` keyword is only used to configure the ASN. The configuration files and `net show` commands display the AS number.

2. Assign the router ID.

    ```
    cumulus@leaf01:~$ net add bgp router-id 10.10.10.1
    ```

3. Specify the BGP neighbor to which you want to distribute routing information.

    ```
    cumulus@leaf01:~$ net add bgp neighbor 10.0.1.0 remote-as external
    ```

    For BGP to advertise IPv6 prefixes, you need to run an additional command to activate the BGP neighbor under the IPv6 address family. The IPv4 address family is enabled by default and the `activate` command is not required for IPv4 route exchange.

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

    - To use auto BGP to assign an ASN automatically on the spine:

      ```
      cumulus@spine01:~$ net add bgp auto spine
      ```

      The auto BGP `spine` keyword is only used to configure the ASN. The configuration files and `net show` commands display the AS number.

2. Assign the router ID.

    ```
    cumulus@spine01:~$ net add bgp router-id 10.10.10.101
    ```

3. Specify the BGP neighbor to which you want to distribute routing information.

    ```
    cumulus@spine01:~$ net add bgp neighbor 10.0.1.1 remote-as external
    ```

    For BGP to advertise IPv6 prefixes, you need to run an additional command to activate the BGP neighbor under the IPv6 address family. The IPv4 address family is enabled by default and the `activate` command is not required for IPv4 route exchange.

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
   leaf01(config-router)# neighbor 10.0.1.0 remote-as external
   ```

   For BGP to advertise IPv6 prefixes, you need to run an additional command to activate the BGP neighbor under the IPv6 address family. The IPv4 address family is enabled by default and the `activate` command is not required for IPv4 route exchange.

   ```
   leaf01(config-router)# neighbor 2001:db8:0002::0a00:1 remote-as external
   leaf01(config-router)# address-family ipv6 unicast
   leaf01(config-router-af)# neighbor 2001:db8:0002::0a00:1 activate
   ```

   For BGP to advertise *IPv4* prefixes with IPv6 next hops, see {{<link url="Optional-BGP-Configuration#advertise-ipv4-prefixes-with-ipv6-next-hops" text="Advertise IPv4 Prefixes with IPv6 Next Hops">}}.

4. Specify which prefixes to originate:

    ```
    leaf01(config-router)# address-family ipv4
    leaf01(config-router-af)# network 10.10.10.1/32
    leaf01(config-router-af)# network 10.1.10.0/24
    leaf01(config-router-af)# end
    leaf01# write memory
    leaf01# exit
    cumulus@leaf01:~$
    ```

    IPv6 prefix example:

    ```
    leaf01(config-router)# address-family ipv6
    leaf01(config-router-af)# network 2001:db8::1/128
    leaf01(config-router-af)# end
    leaf01# write memory
    leaf01# exit
    cumulus@leaf01:~$
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
    spine01(config-router)# neighbor 10.0.1.1 remote-as external
    ```

   For BGP to advertise IPv6 prefixes, you need to run an additional command to activate the BGP neighbor under the IPv6 address family. The IPv4 address family is enabled by default and the `activate` command is not required for IPv4 route exchange.

   ```
   spine01(config-router)# neighbor 2001:db8:0002::0a00:0002 remote-as external
   spine01(config-router)# address-family ipv6 unicast
   spine01(config-router-af)# neighbor 2001:db8:0002::0a00:0002 activate
   ```

   For BGP to advertise *IPv4* prefixes with IPv6 next hops, see {{<link url="Optional-BGP-Configuration#advertise-ipv4-prefixes-with-ipv6-next-hops" text="Advertise IPv4 Prefixes with IPv6 Next Hops">}}.

4. Specify which prefixes to originate:

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

{{< tab "CUE Commands ">}}

{{< tabs "267 ">}}

{{< tab " leaf01 ">}}

1. Identify the BGP node by assigning an ASN.
   <!-- laclac: We have 'global' commands for setting ASN and router-id.  Where/how do we expose the global and inherited stuff in CUE?
   $ cl set router bgp autonomous-system 651001
   $ cl set router bgp router-id 10.10.10.1
   -->
    - To assign an ASN manually:

      ```
      cumulus@leaf01:~$ cl set vrf default router bgp autonomous-system 65101
      ```

    - To use auto BGP to assign an ASN automatically on the leaf:

       ```
       cumulus@leaf01:~$ cl set vrf default router bgp autonomous-system NEED COMMAND
       ```

       The auto BGP `leaf` keyword is only used to configure the ASN. The configuration files and `net show` commands display the AS number.

2. Assign the router ID.

   ```
   cumulus@leaf01:~$ cl set vrf default router bgp router-id 10.10.10.1
   ```

3. Specify the BGP neighbor to which you want to distribute routing information.

    ```
    cumulus@leaf01:~$ cl set vrf default router bgp peer 10.0.1.0 remote-as external
    ```

    For BGP to advertise IPv6 prefixes, you need to run an additional command to activate the BGP neighbor under the IPv6 address family. The IPv4 address family is enabled by default and the `activate` command is not required for IPv4 route exchange.

    ```
    cumulus@leaf01:~$ cl set vrf default router bgp peer 2001:db8:0002::0a00:0002 remote-as external
    cumulus@leaf01:~$ cl set vrf default router bgp peer 2001:db8:0002::0a00:0002 address-family ipv6-unicast enable on
    ```

    For BGP to advertise *IPv4* prefixes with IPv6 next hops, see {{<link url="Optional-BGP-Configuration#advertise-ipv4-prefixes-with-ipv6-next-hops" text="Advertise IPv4 Prefixes with IPv6 Next Hops">}}.

4. Specify which prefixes to originate:

    ```
    cumulus@leaf01:~$ cl set vrf default router bgp address-family ipv4-unicast static-network 10.10.10.1/32
    cumulus@leaf01:~$ cl set vrf default router bgp address-family ipv4-unicast static-network 10.1.10.0/24
    cumulus@leaf01:~$ cl config apply
    ```

   IPv6 prefix example:

   ```
   cumulus@leaf01:~$ cl set vrf default router bgp address-family ipv6-unicast static-network 2001:db8::1/128
   cumulus@leaf01:~$ cl config apply
   ```

{{< /tab >}}

{{< tab "spine01 ">}}

1. Identify the BGP node by assigning an ASN.

    - To assign an ASN manually:

      ```
      cumulus@spine01:~$ cl set vrf default router bgp autonomous-system 65199
      ```

    - To use auto BGP to assign an ASN automatically on the spine:

      ```
      cumulus@spine01:~$ cl set vrf default router bgp autonomous-system NEED COMMAND
      ```

      The auto BGP `spine` keyword is only used to configure the ASN. The configuration files and `net show` commands display the AS number.

2. Assign the router ID.

    ```
    cumulus@spine01:~$ cl set vrf default router bgp router-id 10.10.10.101
    ```

3. Specify the BGP neighbor to which you want to distribute routing information.

    ```
    cumulus@spine01:~$ cl set vrf default router bgp peer remote-as external
    ```

    For BGP to advertise IPv6 prefixes, you need to run an additional command to activate the BGP neighbor under the IPv6 address family. The IPv4 address family is enabled by default and the `activate` command is not required for IPv4 route exchange.

    ```
    cumulus@spine01:~$ cl set vrf default router bgp peer 2001:db8:0002::0a00:1 remote-as external
    cumulus@spine01:~$ cl set vrf default router bgp peer address-family ipv6-unicast 2001:db8:0002::0a00:1 enable on
    ```

    For BGP to advertise *IPv4* prefixes with IPv6 next hops, see {{<link url="Optional-BGP-Configuration#advertise-ipv4-prefixes-with-ipv6-next-hops" text="Advertise IPv4 Prefixes with IPv6 Next Hops">}}.

4. Specify which prefixes to originate:

    ```
    cumulus@spine01:~$ cl set vrf default router bgp address-family ipv4-unicast static-network 10.10.10.101/32
    cumulus@spine01:~$ cl config diff
    cumulus@spine01:~$ cl config apply
    ```

   IPv6 prefix example:

   ```
   cumulus@spine01:~$ cl set vrf default router bgp address-family ipv6-unicast static-network 2001:db8::101/128
   cumulus@spine01:~$ cl config apply
   ```

{{< /tab >}}

{{< /tabs >}}

{{< /tab >}}

{{< /tabs >}}

The NCLU and `vtysh` commands save the configuration in the `/etc/frr/frr.conf` file. For example:

{{< tabs "2286 ">}}

{{< tab " leaf01 ">}}

```
cumulus@leaf01:~$  sudo cat /etc/frr/frr.conf
...
router bgp 65101
 bgp router-id 10.10.10.1
 neighbor 10.0.1.0 remote-as external
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
cumulus@spine01:~$  sudo cat /etc/frr/frr.conf
...
router bgp 65199
 bgp router-id 10.10.10.101
 neighbor 10.0.1.1 remote-as external
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

The following example commands show a basic {{<link title="Border Gateway Protocol - BGP#bgp-unnumbered" text="BGP unnumbered">}} configuration for two switches, leaf01 and spine01, which are eBGP peers.

The only difference between a BGP unnumbered configuration and the BGP numbered configuration shown above is that the BGP neighbor is specified as an interface (insead of an IP address). The interface between the two peers does **not** need to have an IP address configured on each side.

{{< tabs "354 ">}}

{{< tab "NCLU Commands ">}}

{{%notice info%}}
When you commit a change that configures a new routing service such as BGP, the FRR daemon restarts and might interrupt network operations for other configured routing services.
{{%/notice%}}

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

For BGP to advertise IPv6 prefixes, you need to run an additional command to activate the BGP neighbor under the IPv6 address family. The IPv4 address family is enabled by default and the `activate` command is not required for IPv4 route exchange.

```
cumulus@leaf01:~$ net add bgp autonomous-system 65101
cumulus@leaf01:~$ net add bgp router-id 10.10.10.1
cumulus@leaf01:~$ net add bgp neighbor swp51 remote-as external
cumulus@leaf01:~$ net add bgp ipv6 unicast neighbor swp51 activate
cumulus@leaf01:~$ net add bgp ipv6 unicast network 2001:db8::1/128
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

For BGP to advertise IPv6 prefixes, you need to run an additional command to activate the BGP neighbor under the IPv6 address family. The IPv4 address family is enabled by default and the `activate` command is not required for IPv4 route exchange.

```
cumulus@spine01:~$ net add bgp autonomous-system 65199
cumulus@spine01:~$ net add bgp router-id 10.10.10.101
cumulus@spine01:~$ net add bgp neighbor swp1 remote-as external
cumulus@spine01:~$ net add bgp ipv6 unicast neighbor swp1 activate
cumulus@spine01:~$ net add bgp ipv6 unicast network 2001:db8::101/128
cumulus@spine01:~$ net pending
cumulus@spine01:~$ net commit
```

{{< /tab >}}

{{< /tabs >}}

{{< /tab >}}

{{< tab "vtysh Commands ">}}

{{< tabs "407 ">}}

{{< tab "leaf01 ">}}

```
cumulus@leaf01:~$ sudo vtysh

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

For BGP to advertise IPv6 prefixes, you need to run an additional command to activate the BGP neighbor under the IPv6 address family. The IPv4 address family is enabled by default and the `activate` command is not required for IPv4 route exchange.

```
cumulus@leaf01:~$ sudo vtysh

leaf01# configure terminal
leaf01(config)# router bgp 65101
leaf01(config-router)# bgp router-id 10.10.10.1
leaf01(config-router)# neighbor swp51 remote-as external
leaf01(config-router)# address-family ipv6 unicast
leaf01(config-router-af)# neighbor swp51 activate
leaf01(config-router-af)# network 2001:db8::1/128
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

For BGP to advertise IPv6 prefixes, you need to run an additional command to activate the BGP neighbor under the IPv6 address family. The IPv4 address family is enabled by default and the `activate` command is not required for IPv4 route exchange.

```
cumulus@spine01:~$ sudo vtysh

spine01# configure terminal
spine01(config)# router bgp 65199
spine01(config-router)# bgp router-id 10.10.10.101
spine01(config-router)# neighbor swp1 remote-as external
spine01(config-router)# address-family ipv6 unicast
spine01(config-router-af)# neighbor swp1 activate
spine01(config-router-af)# network 2001:db8::101/128
spine01(config-router-af)# end
spine01# write memory
spine01# exit
cumulus@spine01:~$
```

{{< /tab >}}

{{< /tabs >}}

{{< /tab >}}

{{< tab "CUE Commands ">}}

{{< tabs "490 ">}}

{{< tab " leaf01 ">}}

```
cumulus@leaf01:~$ cl set vrf default router bgp autonomous-system 65101
cumulus@leaf01:~$ cl set vrf default router bgp router-id 10.10.10.1
cumulus@leaf01:~$ cl set vrf default router bgp peer swp51 remote-as external
cumulus@leaf01:~$ cl set vrf default router bgp address-family ipv4-unicast static-network 10.10.10.1/32
cumulus@leaf01:~$ cl set vrf default router bgp address-family ipv4-unicast static-network 10.1.10.0/24
cumulus@leaf01:~$ cl config apply
```

For BGP to advertise IPv6 prefixes, you need to run an additional command to activate the BGP neighbor under the IPv6 address family. The IPv4 address family is enabled by default and the `enable` command is not required for IPv4 route exchange.

```
cumulus@leaf01:~$ cl set vrf default router bgp autonomous-system 65101
cumulus@leaf01:~$ cl set vrf default router bgp router-id 10.10.10.1
cumulus@leaf01:~$ cl set vrf default router bgp peer swp51 remote-as external
cumulus@leaf01:~$ cl set vrf default router bgp address-family ipv6-unicast enable on
cumulus@leaf01:~$ cl set vrf default router bgp address-family ipv6-unicast static-network 2001:db8::1/128
cumulus@leaf01:~$ cl config apply
```

{{< /tab >}}

{{< tab "spine01 ">}}

```
cumulus@spine01:~$ cl set vrf default router bgp autonomous-system 65199
cumulus@spine01:~$ cl set vrf default router bgp router-id 10.10.10.101
cumulus@spine01:~$ cl set vrf default router bgp peer swp1 remote-as external
cumulus@spine01:~$ cl set vrf default router bgp address-family ipv4-unicast static-network 10.10.10.101/32
cumulus@spine01:~$ cl config apply
```

For BGP to advertise IPv6 prefixes, you need to run an additional command to activate the BGP neighbor under the IPv6 address family. The IPv4 address family is enabled by default and the `enable` command is not required for IPv4 route exchange.

```
cumulus@spine01:~$ cl set vrf default router bgp autonomous-system 65101
cumulus@spine01:~$ cl set vrf default router bgp router-id 10.10.10.1
cumulus@spine01:~$ cl set vrf default router bgp peer swp51 remote-as external
cumulus@spine01:~$ cl set vrf default router bgp address-family ipv6-unicast enable on
cumulus@spine01:~$ cl set vrf default router bgp address-family ipv6-unicast static-network 2001:db8::101/128
cumulus@spine01:~$ cl config apply
```

{{< /tab >}}

{{< /tabs >}}

{{< /tab >}}

{{< /tabs >}}

The NCLU and vtysh commands save the configuration in the `/etc/frr/frr.conf` file. For example:

{{< tabs "416 ">}}

{{< tab "leaf01 ">}}

```
cumulus@leaf01:~$  sudo cat /etc/frr/frr.conf
...
router bgp 65101
 bgp router-id 10.10.10.1
 neighbor swp51 interface
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
cumulus@spine01:~$  sudo cat /etc/frr/frr.conf
...
router bgp 65199
 bgp router-id 10.10.10.101
 neighbor swp1 interface
 neighbor swp1 remote-as external
 !
 address-family ipv4 unicast
  network 10.10.10.101/32
 exit-address-family
...
```

{{< /tab >}}

{{< /tabs >}}
