---
title: Basic BGP Configuration
author: NVIDIA
weight: 850
toc: 3
---
This section describes how to configure BGP using either BGP numbered or {{<link title="Border Gateway Protocol - BGP#bgp-unnumbered" text="BGP unnumbered">}}. With BGP *unnumbered*, you can set up BGP peering between your Cumulus Linux switches and exchange IPv4 prefixes without having to configure an IPv4 address on each switch.

{{%notice note%}}
BGP *unnumbered* simplifies configuration. NVIDIA recommends you use BGP unnumbered for data center deployments.
{{%/notice%}}

{{%notice warning%}}
When you enable BGP for the first time, the FRR service restarts, which might impact traffic. Any time you enable or disable BGP, or change the ASN, the FRR service also restarts.
{{%/notice%}}

## BGP Numbered

To configure BGP numbered on a BGP node, you need to:
- Assign an <span class="a-tooltip">[ASN](## "Autonomous System Number")</span> to identify this BGP node. In a two-tier leaf and spine configuration, you can use {{<link title="Border Gateway Protocol - BGP#auto-bgp" text="auto BGP">}}, where Cumulus Linux assigns an ASN automatically.
- If necessary, specify a router ID. NVUE automatically assigns the loopback address of the switch to be the router ID. FRR automatically assigns the router ID to be the loopback address or the highest IPv4 address for the interface. If you do not have a loopback address configured or want to use a specific router ID, set the router ID globally or per VRF.
- Specify where to distribute routing information by providing the IP address and ASN of the neighbor.
  - For BGP numbered, this is the IP address of the interface between the two peers; the interface must be a layer 3 access port.
  - The ASN can be a number, or `internal` for a neighbor in the same AS or `external` for a neighbor in a different AS.
- Specify which prefixes to originate from this BGP node.

{{< tabs "23 ">}}
{{< tab "NVUE Commands ">}}

{{< tabs "142 ">}}
{{< tab " leaf01 ">}}

1. Identify the BGP node by assigning an ASN.

    - To assign an ASN manually:

      ```
      cumulus@leaf01:~$ nv set router bgp autonomous-system 65101
      ```

    - To use auto BGP to assign an ASN automatically on the leaf:

       ```
       cumulus@leaf01:~$ nv set router bgp autonomous-system leaf
       ```

       The auto BGP `leaf` keyword is only used to configure the ASN. The configuration files and `nv show` commands display the AS number.

2. BGP automatically assigns the loopback address of the switch to be the router ID. If you do not have a loopback address configured or you do not want to use the loopback address as the router ID, you must assign the router ID either globally with the `nv set router bgp router-id` command or in a VRF with the `nv set vrf <vrf> router bgp router-id` command.

   ```
   cumulus@leaf01:~$ nv set router bgp router-id 10.10.10.1
   ```

3. Specify the BGP neighbor to which you want to distribute routing information.

    ```
    cumulus@leaf01:~$ nv set vrf default router bgp neighbor 10.0.1.0 remote-as external
    ```

    For BGP to advertise IPv6 prefixes, you need to run an additional command to activate the BGP neighbor under the IPv6 address family. Cumulus Linux enables the IPv4 address family by default; you do not need to run the `activate` command for IPv4 route exchange.

    ```
    cumulus@leaf01:~$ nv set vrf default router bgp neighbor 2001:db8:0002::0a00:0002 remote-as external
    cumulus@leaf01:~$ nv set vrf default router bgp neighbor 2001:db8:0002::0a00:0002 address-family ipv6-unicast enable on
    ```

    For BGP to advertise *IPv4* prefixes with IPv6 next hops, see {{<link url="Optional-BGP-Configuration#advertise-ipv4-prefixes-with-ipv6-next-hops" text="Advertise IPv4 Prefixes with IPv6 Next Hops">}}.

4. Specify which prefixes to originate:

    ```
    cumulus@leaf01:~$ nv set vrf default router bgp address-family ipv4-unicast network 10.10.10.1/32
    cumulus@leaf01:~$ nv set vrf default router bgp address-family ipv4-unicast network 10.1.10.0/24
    cumulus@leaf01:~$ nv config apply
    ```

   IPv6 prefix example:

   ```
   cumulus@leaf01:~$ nv set vrf default router bgp address-family ipv6-unicast network 2001:db8::1/128
   cumulus@leaf01:~$ nv config apply
   ```

After you run `nv config save`, the NVUE Commands create the following configuration snippet in the `/etc/nvue.d/startup.yaml` file:

```
cumulus@leaf01:~$ sudo cat /etc/nvue.d/startup.yaml
...
- set:
    router:
      bgp:
        autonomous-system: 65101
        enable: on
        router-id: 10.10.10.1
    vrf:
      default:
        router:
          bgp:
            address-family:
              ipv4-unicast:
                enable: on
                network:
                  10.1.10.0/24: {}
                  10.10.10.1/32: {}
            enable: on
            neighbor:
              10.0.1.0:
                remote-as: external
                type: numbered
```

{{< /tab >}}
{{< tab "spine01 ">}}

1. Identify the BGP node by assigning an ASN.

    - To assign an ASN manually:

      ```
      cumulus@spine01:~$ nv set router bgp autonomous-system 65199
      ```

    - To use auto BGP to assign an ASN automatically on the spine:

      ```
      cumulus@spine01:~$ nv set router bgp autonomous-system spine
      ```

      The auto BGP `spine` keyword is only used to configure the ASN. The configuration files and `nv show` commands display the AS number.

2. BGP automatically assigns the loopback address of the switch to be the router ID. If you do not have a loopback address configured or you do not want to use the loopback address as the router ID, you must assign the router ID either globally with the `nv set router bgp router-id` command or in a VRF with the `nv set vrf <vrf> router bgp router-id` command.

    ```
    cumulus@spine01:~$ nv set router bgp router-id 10.10.10.101
    ```

3. Specify the BGP neighbor to which you want to distribute routing information.

    ```
    cumulus@spine01:~$ nv set vrf default router bgp neighbor 10.0.1.0 remote-as external
    ```

    For BGP to advertise IPv6 prefixes, you need to run an additional command to activate the BGP neighbor under the IPv6 address family. Cumulus Linux enables the IPv4 address family by default; you do not need to run the `activate` command for IPv4 route exchange.

    ```
    cumulus@spine01:~$ nv set vrf default router bgp neighbor 2001:db8:0002::0a00:1 remote-as external
    cumulus@spine01:~$ nv set vrf default router bgp neighbor address-family ipv6-unicast 2001:db8:0002::0a00:1 enable on
    ```

    For BGP to advertise *IPv4* prefixes with IPv6 next hops, see {{<link url="Optional-BGP-Configuration#advertise-ipv4-prefixes-with-ipv6-next-hops" text="Advertise IPv4 Prefixes with IPv6 Next Hops">}}.

4. Specify which prefixes to originate:

    ```
    cumulus@spine01:~$ nv set vrf default router bgp address-family ipv4-unicast network 10.10.10.101/32
    cumulus@spine01:~$ nv config apply
    ```

   IPv6 prefix example:

   ```
   cumulus@spine01:~$ nv set vrf default router bgp address-family ipv6-unicast network 2001:db8::101/128
   cumulus@spine01:~$ nv config apply
   ```

After you run `nv config save`, the NVUE Commands create the following configuration snippet in the `/etc/nvue.d/startup.yaml` file:

```
cumulus@spine01:~$ sudo cat /etc/nvue.d/startup.yaml
...
- set:
    router:
      bgp:
        autonomous-system: 65199
        enable: on
        router-id: 10.10.10.101
    vrf:
      default:
        router:
          bgp:
            address-family:
              ipv4-unicast:
                enable: on
                network:
                  10.10.10.101/32: {}
            enable: on
            neighbor:
              10.0.1.0:
                remote-as: external
                type: numbered
```

{{< /tab >}}
{{< /tabs >}}

{{< /tab >}}
{{< tab "vtysh Commands ">}}

{{< tabs "311 ">}}
{{< tab " leaf01 ">}}

1. Enable the `bgpd` daemon as described in {{<link title="FRRouting">}}.

2. Identify the BGP node by assigning an ASN and, if necessary, the router ID.

   BGP automatically assigns the router ID using the loopback address or the highest IPv4 address for the interface. If you want to assign a specific IPv4 address for the router ID, add the router ID globally or per VRF.

    ```
    cumulus@leaf01:~$ sudo vtysh
    ...
    leaf01# configure terminal
    leaf01(config)# router bgp 65101
    leaf01(config-router)# bgp router-id 10.10.10.1
    ```

3. Specify where to distribute routing information:

   ```
   leaf01(config-router)# neighbor 10.0.1.0 remote-as external
   ```

   For BGP to advertise IPv6 prefixes, you need to run an additional command to activate the BGP neighbor under the IPv6 address family. Cumulus Linux enables the IPv4 address family by default; you do not need to run the `activate` command for IPv4 route exchange.

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
    ```

{{< /tab >}}
{{< tab "spine01 ">}}

1. Enable the `bgpd` daemon as described in {{<link title="FRRouting">}}.

2. Identify the BGP node by assigning an ASN and, if necessary, the router ID.

   BGP automatically assigns the router ID using the loopback address or the highest IPv4 address for the interface. If you want to assign a specific IPv4 address for the router ID, add the router ID globally or per VRF.

    ```
    cumulus@spine01:~$ sudo vtysh
    ...
    spine01# configure terminal
    spine01(config)# router bgp 65199
    spine01(config-router)# bgp router-id 10.10.10.101
    ```

3. Specify where to distribute routing information:

    ```
    spine01(config-router)# neighbor 10.0.1.1 remote-as external
    ```

   For BGP to advertise IPv6 prefixes, you need to run an additional command to activate the BGP neighbor under the IPv6 address family. Cumulus Linux enables the IPv4 address family by default; you do not need to run the `activate` command for IPv4 route exchange.

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
    ```

    IPv6 prefixes:

    ```
    spine01(config-router)# address-family ipv4
    spine01(config-router-af)# network 2001:db8::101/128
    spine01(config-router-af)# end
    spine01# write memory
    spine01# exit
    ```

{{%notice note%}}
When using auto BGP, there are no references to `leaf` or `spine` in the configurations. Auto BGP determines the ASN for the system and configures it using standard vtysh commands.
{{%/notice%}}

{{< /tab >}}
{{< /tabs >}}

The vtysh commands save the configuration in the `/etc/frr/frr.conf` file. For example:

```
cumulus@spine01:~$ sudo cat /etc/frr/frr.conf
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

## BGP Unnumbered

The following example commands show a basic {{<link title="Border Gateway Protocol - BGP#bgp-unnumbered" text="BGP unnumbered">}} configuration for two switches, leaf01 and spine01, which are eBGP peers.

The only difference between a BGP unnumbered configuration and the BGP numbered configuration shown above is that the BGP neighbor is as an interface (instead of an IP address). You do not need to configure an IP address on the interface between the two peers on each side.

{{< tabs "463 ">}}
{{< tab "NVUE Commands ">}}

{{< tabs "518 ">}}
{{< tab " leaf01 ">}}

```
cumulus@leaf01:~$ nv set router bgp autonomous-system 65101
cumulus@leaf01:~$ nv set router bgp router-id 10.10.10.1
cumulus@leaf01:~$ nv set vrf default router bgp neighbor swp51 remote-as external
cumulus@leaf01:~$ nv set vrf default router bgp address-family ipv4-unicast network 10.10.10.1/32
cumulus@leaf01:~$ nv set vrf default router bgp address-family ipv4-unicast network 10.1.10.0/24
cumulus@leaf01:~$ nv config apply
```

For BGP to advertise IPv6 prefixes, you need to run an additional command to activate the BGP neighbor under the IPv6 address family. Cumulus Linux enables the IPv4 address family by default; you do not need to run the `activate` command for IPv4 route exchange.

```
cumulus@leaf01:~$ nv set router bgp autonomous-system 65101
cumulus@leaf01:~$ nv set router bgp router-id 10.10.10.1
cumulus@leaf01:~$ nv set vrf default router bgp neighbor swp51 remote-as external
cumulus@leaf01:~$ nv set vrf default router bgp address-family ipv6-unicast enable on
cumulus@leaf01:~$ nv set vrf default router bgp address-family ipv6-unicast network 2001:db8::1/128
cumulus@leaf01:~$ nv config apply
```

After you run `nv config save`, the NVUE Commands create the following configuration snippet in the `/etc/nvue.d/startup.yaml` file:

```
cumulus@leaf01:~$ sudo cat /etc/nvue.d/startup.yaml
...
- set:
    router:
      bgp:
        autonomous-system: 65101
        enable: on
        router-id: 10.10.10.1
    vrf:
      default:
        router:
          bgp:
            address-family:
              ipv4-unicast:
                enable: on
                network:
                  10.1.10.0/24: {}
                  10.10.10.1/32: {}
            enable: on
            neighbor:
              swp51:
                remote-as: external
                type: unnumbered
```

{{< /tab >}}
{{< tab "spine01 ">}}

```
cumulus@spine01:~$ nv set router bgp autonomous-system 65199
cumulus@spine01:~$ nv set router bgp router-id 10.10.10.101
cumulus@spine01:~$ nv set vrf default router bgp neighbor swp1 remote-as external
cumulus@spine01:~$ nv set vrf default router bgp address-family ipv4-unicast network 10.10.10.101/32
cumulus@spine01:~$ nv config apply
```

For BGP to advertise IPv6 prefixes, you need to run an additional command to activate the BGP neighbor under the IPv6 address family. Cumulus Linux enables the IPv4 address family by default; you do not need to run the `activate` command for IPv4 route exchange.

```
cumulus@spine01:~$ nv set router bgp autonomous-system 65199
cumulus@spine01:~$ nv set router bgp router-id 10.10.10.101
cumulus@spine01:~$ nv set vrf default router bgp neighbor swp1 remote-as external
cumulus@spine01:~$ nv set vrf default router bgp address-family ipv6-unicast enable on
cumulus@spine01:~$ nv set vrf default router bgp address-family ipv6-unicast network 2001:db8::101/128
cumulus@spine01:~$ nv config apply
```

After you run `nv config save`, the NVUE Commands create the following configuration snippet in the `/etc/nvue.d/startup.yaml` file:

```
cumulus@spine01:~$ sudo cat /etc/nvue.d/startup.yaml
...
- set:
    router:
      bgp:
        autonomous-system: 65199
        enable: on
        router-id: 10.10.10.101
    vrf:
      default:
        router:
          bgp:
            address-family:
              ipv4-unicast:
                enable: on
                network:
                  10.10.10.101/32: {}
            enable: on
            neighbor:
              swp1:
                remote-as: external
                type: unnumbered
```

{{< /tab >}}
{{< /tabs >}}

{{< /tab >}}
{{< tab "vtysh Commands ">}}

{{< tabs "622 ">}}
{{< tab "leaf01 ">}}

```
cumulus@leaf01:~$ sudo vtysh
...
leaf01# configure terminal
leaf01(config)# router bgp 65101
leaf01(config-router)# bgp router-id 10.10.10.1
leaf01(config-router)# neighbor swp51 interface remote-as external
leaf01(config-router)# address-family ipv4
leaf01(config-router-af)# network 10.10.10.1/32
leaf01(config-router-af)# network 10.1.10.0/24
leaf01(config-router-af)# end
leaf01# write memory
leaf01# exit
```

For BGP to advertise IPv6 prefixes, you need to run an additional command to activate the BGP neighbor under the IPv6 address family. Cumulus Linux enables the IPv4 address family by default; you do not need to run the `activate` command for IPv4 route exchange.

```
cumulus@leaf01:~$ sudo vtysh
...
leaf01# configure terminal
leaf01(config)# router bgp 65101
leaf01(config-router)# bgp router-id 10.10.10.1
leaf01(config-router)# neighbor swp51 interface remote-as external
leaf01(config-router)# address-family ipv6 unicast
leaf01(config-router-af)# neighbor swp51 activate
leaf01(config-router-af)# network 2001:db8::1/128
leaf01(config-router-af)# end
leaf01# write memory
leaf01# exit
```

The vtysh commands save the configuration in the `/etc/frr/frr.conf` file. For example:

```
cumulus@leaf01:~$  sudo cat /etc/frr/frr.conf
...
router bgp 65101
 bgp router-id 10.10.10.1
 neighbor swp51 interface remote-as external
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
cumulus@spine01:~$ sudo vtysh
...
spine01# configure terminal
spine01(config)# router bgp 65199
spine01(config-router)# bgp router-id 10.10.10.101
spine01(config-router)# neighbor swp1 interface remote-as external
spine01(config-router)# address-family ipv4
spine01(config-router-af)# network 10.10.10.101/32
spine01(config-router-af)# end
spine01# write memory
spine01# exit
```

For BGP to advertise IPv6 prefixes, you need to run an additional command to activate the BGP neighbor under the IPv6 address family. Cumulus Linux enables the IPv4 address family by default; you do not need to run the `activate` command for IPv4 route exchange.

```
cumulus@spine01:~$ sudo vtysh
...
spine01# configure terminal
spine01(config)# router bgp 65199
spine01(config-router)# bgp router-id 10.10.10.101
spine01(config-router)# neighbor swp1 interface remote-as external
spine01(config-router)# address-family ipv6 unicast
spine01(config-router-af)# neighbor swp1 activate
spine01(config-router-af)# network 2001:db8::101/128
spine01(config-router-af)# end
spine01# write memory
spine01# exit
```

The vtysh commands save the configuration in the `/etc/frr/frr.conf` file. For example:

```
cumulus@spine01:~$  sudo cat /etc/frr/frr.conf
...
router bgp 65199
 bgp router-id 10.10.10.101
 neighbor swp1 interface remote-as external
 !
 address-family ipv4 unicast
  network 10.10.10.101/32
 exit-address-family
...
```

{{< /tab >}}
{{< /tabs >}}

{{< /tab >}}
{{< /tabs >}}

## Verify Configuration

To verify that the switch can see its BGP neighbors, run the vtysh `show ip bgp summary` command:

{{< tabs "550 ">}}
{{< tab "leaf01 ">}}

```
cumulus@leaf01:mgmt:~$ sudo vtysh
...
leaf01# show ip bgp summary
IPv4 Unicast Summary (VRF default):
BGP router identifier 10.10.10.1, local AS number 65101 vrf-id 0
BGP table version 16
RIB entries 15, using 2880 bytes of memory
Peers 2, using 40 KiB of memory

Neighbor        V         AS   MsgRcvd   MsgSent   TblVer  InQ OutQ  Up/Down State/PfxRcd   PfxSnt Desc
spine01(swp51)  4      65199       599       603        0    0    0 00:29:35            6        8 N/A
spine02(swp52)  4      65199       582       585        0    0    0 00:28:43            3        8 N/A

Total number of neighbors 2
```

{{< /tab >}}
{{< tab "spine01 ">}}

```
cumulus@spine01:mgmt:~$ sudo vtysh
...
spine01# show ip bgp summary
IPv4 Unicast Summary (VRF default):
BGP router identifier 10.10.10.101, local AS number 65199 vrf-id 0
BGP table version 7
RIB entries 13, using 2496 bytes of memory
Peers 4, using 79 KiB of memory

Neighbor        V         AS   MsgRcvd   MsgSent   TblVer  InQ OutQ  Up/Down State/PfxRcd   PfxSnt Desc
leaf01(swp1)    4      65101       637       634        0    0    0 00:31:20            4        7 N/A
leaf02(swp2)    4      65102       639       636        0    0    0 00:31:25            4        7 N/A
swp3            4          0         0         0        0    0    0    never         Idle        0 N/A
leaf04(swp4)    4      65104       636       635        0    0    0 00:31:23            1        7 N/A

Total number of neighbors 4
```

{{< /tab >}}
{{< /tabs >}}

To verify that you can see the prefixes of the other neighbor in the routing table, run the vtysh `show ip route` command.

{{< tabs "608 ">}}
{{< tab "leaf01 ">}}

```
cumulus@leaf01:mgmt:~$ sudo vtysh
...
leaf01# show ip route
Codes: K - kernel route, C - connected, S - static, R - RIP,
       O - OSPF, I - IS-IS, B - BGP, E - EIGRP, N - NHRP,
       T - Table, A - Babel, D - SHARP, F - PBR, f - OpenFabric,
       Z - FRR,
       > - selected route, * - FIB route, q - queued, r - rejected, b - backup
       t - trapped, o - offload failure

C>* 10.1.10.0/24 is directly connected, vlan10, 00:36:43
C>* 10.1.20.0/24 is directly connected, vlan20, 00:36:43
C>* 10.1.30.0/24 is directly connected, vlan30, 00:36:43
C>* 10.10.10.1/32 is directly connected, lo, 00:38:34
B>* 10.10.10.2/32 [20/0] via fe80::4ab0:2dff:fe51:3d2a, swp52, weight 1, 00:32:23
  *                      via fe80::4ab0:2dff:feb1:8706, swp51, weight 1, 00:32:23
B>* 10.10.10.4/32 [20/0] via fe80::4ab0:2dff:fe51:3d2a, swp52, weight 1, 00:32:19
  *                      via fe80::4ab0:2dff:feb1:8706, swp51, weight 1, 00:32:19
B>* 10.10.10.101/32 [20/0] via fe80::4ab0:2dff:feb1:8706, swp51, weight 1, 00:33:18
B>* 10.10.10.102/32 [20/0] via fe80::4ab0:2dff:fe51:3d2a, swp52, weight 1, 00:32:2
```

{{< /tab >}}
{{< tab "spine01 ">}}

```
cumulus@spine01:mgmt:~$ sudo vtysh
...
spine01# show ip route
Codes: K - kernel route, C - connected, S - static, R - RIP,
       O - OSPF, I - IS-IS, B - BGP, E - EIGRP, N - NHRP,
       T - Table, A - Babel, D - SHARP, F - PBR, f - OpenFabric,
       Z - FRR,
       > - selected route, * - FIB route, q - queued, r - rejected, b - backup
       t - trapped, o - offload failure

B>* 10.1.10.0/24 [20/0] via fe80::4ab0:2dff:fe90:b5c8, swp2, weight 1, 00:37:24
B>* 10.1.20.0/24 [20/0] via fe80::4ab0:2dff:fe90:b5c8, swp2, weight 1, 00:37:24
B>* 10.1.30.0/24 [20/0] via fe80::4ab0:2dff:fe90:b5c8, swp2, weight 1, 00:37:24
B>* 10.10.10.1/32 [20/0] via fe80::4ab0:2dff:feb5:d65e, swp1, weight 1, 00:37:20
B>* 10.10.10.2/32 [20/0] via fe80::4ab0:2dff:fe90:b5c8, swp2, weight 1, 00:37:24
B>* 10.10.10.4/32 [20/0] via fe80::4ab0:2dff:fea4:fab6, swp4, weight 1, 00:37:22
C>* 10.10.10.101/32 is directly connected, lo, 00:37:31
```

{{< /tab >}}
{{< /tabs >}}

## Related Information

- To configure optional BGP settings, see {{<link url="Optional-BGP-Configuration" >}}.
- To view and test a full BGP configuration example, see {{<link url="Configuration-Example" >}}.
