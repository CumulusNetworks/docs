---
title: Protocol Independent Multicast - PIM
author: NVIDIA
weight: 960
toc: 3
---
<span class="a-tooltip">[PIM](## "Protocol Independent Multicast")</span> is a multicast control plane protocol that advertises multicast sources and receivers over a routed layer 3 network. Layer 3 multicast relies on PIM to advertise information about multicast capable routers, and the location of multicast senders and receivers. Multicast does not go through a routed network without PIM.

PIM operates in <span class="a-tooltip">[PIM-SM](## "Sparse Mode")</span> or <span class="a-tooltip">[PIM-DM](## "Dense Mode")</span> mode. Cumulus Linux supports PIM-SM only.

PIM-SM is a *pull* multicast distribution method; multicast traffic only goes through the network if receivers explicitly ask for it. When a receiver *pulls* multicast traffic, it must notify the network periodically that it wants to continue the multicast stream.

PIM-SM has three configuration options:
- <span class="a-tooltip">[ASM](## "Any-source Mulitcast")</span> relies on a multicast rendezvous point (RP) to connect multicast senders and receivers that dynamically determine the shortest path through the network.
- <span class="a-tooltip">[SSM](## "Source Specific Multicast")</span> requires multicast receivers to know from which source they want to receive multicast traffic instead of relying on an RP.
- <span class="a-tooltip">[BiDir](## "Bidirectional PIM")</span> forwards all traffic through the RP instead of tracking multicast source IPs, allowing for greater scale but can cause inefficient traffic forwarding.

Cumulus Linux supports ASM and SSM only.

For additional information on PIM-SM, refer to {{<exlink url="https://tools.ietf.org/html/rfc7761" text="RFC 7761 - Protocol Independent Multicast - Sparse Mode">}}. For a brief description of how PIM works, refer to [PIM Overview]({{<ref "/knowledge-base/Configuration-and-Usage/Network-Configuration/PIM-Overview" >}}).

## Example PIM Topology

The following illustration shows a basic PIM <span class="a-tooltip">[ASM](## "Any-source Mulitcast")</span> configuration:
- leaf01 is the <span class="a-tooltip">[FHR](## "First Hop Router")</span>, which controls the PIM register process. The FHR is the device to which the multicast sources connect.
- leaf02 is the <span class="a-tooltip">[LHR](## "Last Hop Router")</span>, which is the last router in the path and attaches to an interested multicast receiver.
- spine01 is the <span class="a-tooltip">[RP](## "Rendezvous Point")</span>, which receives multicast data from sources and forwards traffic down a shared distribution tree to the receivers.

{{< figure src = "/images/cumulus-linux/pim-basic-example.png" >}}

## Basic PIM Configuration

To configure PIM:
- Enable PIM on all interfaces that connect to a multicast source or receiver, and on the interface with the RP address.

  With NVUE, you must also run the `nv set router pim enable on` command to enable and start the PIM service. This is not required for vtysh configuration.

- Enable <span class="a-tooltip">[IGMP](## "Internet Group Management Protocol")</span> on all interfaces that attach to a host and all interfaces that attach to a multicast receiver. IGMP version 3 is the default. Only specify the version if you want to use IGMP version 2. For <span class="a-tooltip">[SSM](## "Source Specific Multicast")</span>, you must use IGMP version 3.
- For <span class="a-tooltip">[ASM](## "Any-source Mulitcast")</span>, on each PIM enabled switch, specify the IP address of the RP for the multicast group. You can also configure PIM to send traffic from specific multicast groups to specific RPs.

  <span class="a-tooltip">[SSM](## "Source Specific Multicast")</span> uses prefix lists to configure a receiver to only allow traffic to a multicast address from a single source. This removes the need for an RP because the receiver must know the source before accepting traffic. To enable SSM, you only need to enable PIM and IGMPv3 on the interfaces.

These example commands configure leaf01, leaf02 and spine01 as shown in the topology example above.

{{< tabs "TabID44 ">}}
{{< tab "NVUE Commands ">}}

{{< tabs "TabID86 ">}}
{{< tab "leaf01 ">}}

```
cumulus@leaf01:~$ nv set router pim enable on
cumulus@leaf01:~$ nv set interface vlan10 router pim
cumulus@leaf01:~$ nv set interface vlan10 ip igmp
cumulus@leaf01:~$ nv set interface swp51 router pim
cumulus@leaf01:~$ nv set vrf default router pim address-family ipv4-unicast rp 10.10.10.101
cumulus@leaf01:~$ nv config apply
```

{{< /tab >}}
{{< tab "leaf02 ">}}

```
cumulus@leaf02:~$ nv set router pim enable on
cumulus@leaf02:~$ nv set interface vlan20 router pim
cumulus@leaf02:~$ nv set interface vlan20 ip igmp
cumulus@leaf02:~$ nv set interface swp51 router pim
cumulus@leaf02:~$ nv set vrf default router pim address-family ipv4-unicast rp 10.10.10.101
cumulus@leaf02:~$ nv config apply
```

{{< /tab >}}
{{< tab "spine01 ">}}

```
cumulus@spine01:~$ nv set router pim enable on
cumulus@spine01:~$ nv set interface swp1 router pim
cumulus@spine01:~$ nv set interface swp2 router pim
cumulus@spine01:~$ nv set vrf default router pim address-family ipv4-unicast rp 10.10.10.101 
cumulus@spine01:~$ nv config apply
```

{{< /tab >}}
{{< /tabs >}}

{{< /tab >}}
{{< tab "vtysh Commands ">}}

{{< tabs "TabID91 ">}}
{{< tab "leaf01 ">}}

The <span class="a-tooltip">[FRR](## "FRRouting")</span> package includes PIM. For proper PIM operation, PIM depends on Zebra. You must configure unicast routing and a routing protocol or static routes.

1. Edit the `/etc/frr/daemons` file and add `pimd=yes` to the end of the file:

   ```
   cumulus@leaf01:~$ sudo nano /etc/frr/daemons
   ...
   pimd=yes
   ...
   ```
<!-- vale off -->
2. {{<cl/restart-frr>}}
<!-- vale on -->
3. In the vtysh shell, run the following commands to configure the PIM interfaces. PIM must be on all interfaces facing multicast sources or multicast receivers, as well as on the interface with the RP address.

   ```
   cumulus@leaf01:~$ sudo vtysh
   ...
   leaf01# configure terminal
   leaf01(config)# interface vlan10
   leaf01(config-if)# ip pim
   leaf01(config-if)# exit
   leaf01(config)# interface swp51
   leaf01(config-if)# ip pim
   leaf01(config-if)# exit
   ```

4. Enable IGMP on all interfaces that have attached hosts.

   ```
   leaf01(config)# interface vlan10
   leaf01(config-if)# ip igmp
   leaf01(config-if)# exit
   ```

5. **For ASM**, configure a group mapping for a static RP:

   ```
   leaf01(config)# ip pim rp 10.10.10.101
   leaf01(config)# exit
   leaf01# write memory
   leaf01#  exit
   ```

{{< /tab >}}
{{< tab "leaf02 ">}}

1. Edit the `/etc/frr/daemons` file and add `pimd=yes` to the end of the file:

   ```
   cumulus@leaf02:~$ sudo nano /etc/frr/daemons
   ...
   pimd=yes
   ...
   ```
<!-- vale off -->
2. {{<cl/restart-frr>}}
<!-- vale on -->
3. In the vtysh shell, run the following commands to configure the PIM interfaces. PIM must be on all interfaces facing multicast sources or multicast receivers, as well as on the interface with the RP address.

   ```
   cumulus@leaf02:~$ sudo vtysh
   ...
   leaf02# configure terminal
   leaf02(config)# interface vlan20
   leaf02(config-if)# ip pim
   leaf02(config-if)# exit
   leaf02(config)# interface swp51
   leaf02(config-if)# ip pim
   leaf02(config-if)# exit
   ```

4. Enable IGMP on all interfaces that have attached hosts.

   ```
   leaf02(config)# interface vlan20
   leaf02(config-if)# ip igmp
   leaf02(config-if)# exit
   ```

5. **For ASM**, configure a group mapping for a static RP:

   ```
   leaf02(config)# ip pim rp 10.10.10.101
   leaf02(config)# exit
   leaf02# write memory
   leaf02# exit
   ```

{{< /tab >}}
{{< tab "spine01 ">}}

1. Edit the `/etc/frr/daemons` file and add `pimd=yes` to the end of the file:

   ```
   cumulus@spine01:~$ sudo nano /etc/frr/daemons
   ...
   pimd=yes
   ...
   ```
<!-- vale off -->
2. {{<cl/restart-frr>}}
<!-- vale on -->
3. In the vtysh shell, run the following commands to configure the PIM interfaces. PIM must be on all interfaces facing multicast sources or multicast receivers, as well as on the interface with the RP address.

   ```
   cumulus@spine01:~$ sudo vtysh
   ...
   spine01# configure terminal
   spine01(config)# interface swp1
   spine01(config-if)# ip pim
   spine01(config-if)# exit
   spine01(config)# interface swp2
   spine01(config-if)# ip pim
   spine01(config-if)# exit
   ```

4. **For ASM**, configure a group mapping for a static RP:

   ```
   spine01(config)# ip pim rp 10.10.10.101
   spine01(config-if)# end
   spine01# write memory
   spine01# exit
   ```

{{< /tab >}}
{{< /tabs >}}

{{< /tab >}}
{{< /tabs >}}

The above commands configure the switch to send all multicast traffic to RP 10.10.10.101. The following commands configure PIM to send traffic from multicast group 224.10.0.0/16 to RP 10.10.10.101 and traffic from multicast group 224.10.2.0/24 to RP 10.10.10.102:

{{< tabs "TabID240 ">}}
{{< tab "NVUE Commands ">}}

```
cumulus@leaf01:~$ nv set vrf default router pim address-family ipv4-unicast rp 10.10.10.101 group-range 224.10.0.0/16
cumulus@leaf01:~$ nv set vrf default router pim address-family ipv4-unicast rp 10.10.10.102 group-range 224.10.2.0/24
```

{{< /tab >}}
{{< tab "vtysh Commands ">}}

```
cumulus@leaf01:~$ sudo vtysh
...
spine01# configure terminal
spine01(config)# ip pim rp 10.10.10.101 224.10.0.0/16
spine01(config)# ip pim rp 10.10.10.102 224.10.2.0/16
spine01(config)# end
spine01# exit
```

{{< /tab >}}
{{< /tabs >}}

The following commands use a prefix list to configure PIM to send traffic from multicast group 224.10.0.0/16 to RP 10.10.10.101 and traffic from multicast group 224.10.2.0/24 to RP 10.10.10.102:

{{< tabs "TabID252 ">}}
{{< tab "NVUE Commands ">}}

```
cumulus@leaf01:~$ nv set router policy prefix-list MCAST1 rule 1 action permit
cumulus@leaf01:~$ nv set router policy prefix-list MCAST1 rule 1 match 224.10.0.0/16
cumulus@leaf01:~$ nv set router policy prefix-list MCAST2 rule 1 action permit
cumulus@leaf01:~$ nv set router policy prefix-list MCAST2 rule 1 match 224.10.2.0/24
cumulus@leaf01:~$ nv config apply
cumulus@leaf01:~$ nv set vrf default router pim address-family ipv4-unicast rp 10.10.10.101 prefix-list MCAST1
cumulus@leaf01:~$ nv set vrf default router pim address-family ipv4-unicast rp 10.10.10.102 prefix-list MCAST2
cumulus@leaf01:~$ nv config apply
```

{{< /tab >}}
{{< tab "vtysh Commands ">}}

```
cumulus@leaf01:~$ sudo vtysh
...
spine01# configure terminal
switch(config)# ip prefix-list MCAST1 seq 1 permit 224.10.0.0/16
switch(config)# ip prefix-list MCAST2 seq 1 permit 224.10.2.0/24
spine01(config)# ip pim rp 10.10.10.101 prefix-list MCAST1
spine01(config)# ip pim rp 10.10.10.102 prefix-list MCAST2
spine01(config)# end
spine01# exit
```

{{< /tab >}}
{{< /tabs >}}

{{%notice note%}}
- You can either configure RP mappings for different multicast groups or use a prefix list to specify the RP to group mapping. You cannot use both methods at the same time.
- NVIDIA recommends that you do not use a spine switch as an RP when using eBGP in a Clos network. See the [PIM Overview knowledge-base article]({{<ref "/knowledge-base/Configuration-and-Usage/Network-Configuration/PIM-Overview" >}}).
- zebra does not resolve the next hop for the RP through the default route. To prevent multicast forwarding from failing, either provide a specific route to the RP or run the vtysh `ip nht resolve-via-default` configuration command to resolve the next hop for the RP through the default route.
{{%/notice%}}

## Optional PIM Configuration

This section describes optional configuration procedures.

### ASM SPT Infinity

When the LHR receives the first multicast packet, it sends a <span class="a-tooltip">[PIM (S,G) join](## "a single PIM message with a list of groups to join. ")</span> towards the FHR to forward traffic through the network. This builds the <span class="a-tooltip">[SPT](## "shortest path tree ")</span>, or the tree that is the shortest path to the source. When the traffic arrives over the SPT, a PIM (S,G) RPT prune goes up the shared tree towards the RP. This removes multicast traffic from the shared tree; multicast data only goes over the SPT.

You can configure SPT switchover per group (SPT infinity), which allows for some groups to never switch to a shortest path tree. The LHR now sends both (*,G) joins and (S,G) RPT prune messages towards the RP.

{{%notice note%}}
When you use a prefix list in Cumulus Linux to match a multicast group destination address (GDA) range, you must include the /32 operator. In the NVUE command example below, `max-prefix-len 32` after the group match range specifies the /32 operator. In the vtysh command example, `ge 32` after the group permit range specifies the /32 operator.
{{%/notice%}}
  
To configure a group to never follow the SPT, create the necessary prefix lists, then configure SPT switchover for the prefix list:

{{< tabs "TabID307 ">}}
{{< tab "NVUE Commands ">}}

```
cumulus@switch:~$ nv set router policy prefix-list SPTrange rule 1 match 235.0.0.0/8 max-prefix-len 32
cumulus@switch:~$ nv set router policy prefix-list SPTrange rule 1 action permit
cumulus@switch:~$ nv set router policy prefix-list SPTrange rule 2 match 238.0.0.0/8 max-prefix-len 32
cumulus@switch:~$ nv set router policy prefix-list SPTrange rule 2 action permit
cumulus@switch:~$ nv set vrf default router pim address-family ipv4-unicast spt-switchover prefix-list SPTrange
cumulus@switch:~$ nv set vrf default router pim address-family ipv4-unicast spt-switchover action infinity
cumulus@switch:~$ nv config apply
```

{{< /tab >}}
{{< tab "vtysh Commands ">}}

```
cumulus@switch:~$ sudo vtysh
...
switch# configure terminal
switch(config)# ip prefix-list spt-range permit 235.0.0.0/8 ge 32
switch(config)# ip prefix-list spt-range permit 238.0.0.0/8 ge 32
switch(config)# ip pim spt-switchover infinity prefix-list spt-range
switch(config)# end
switch# exit
```

{{< /tab >}}
{{< /tabs >}}

To view the configured prefix list, run the vtysh `show ip mroute` command. The following command shows that SPT switchover (`pimreg`) is on 235.0.0.0.

```
cumulus@switch:~$ sudo vtysh
...
switch# show ip mroute
Source          Group           Proto   Input     Output     TTL  Uptime
*               235.0.0.0       IGMP     swp1     pimreg     1    00:03:3
                                IGMP              vlan10     1    00:03:38
*               238.0.0.0       IGMP     swp1     vlan10     1    00:02:08
```

### SSM Multicast Group Ranges

232.0.0.0/8 is the default multicast group range reserved for <span class="a-tooltip">[SSM](## "Source Specific Multicast")</span>. To modify the SSM multicast group range, define a prefix list and apply it. You can change (expand) the default group or add additional groups to this range.

{{%notice note%}}
You must include 232.0.0.0/8 in the prefix list as this is the reserved SSM range. Using a prefix-list, you can expand the SSM range but all devices in the source tree must agree on the SSM range. When you use a prefix list in Cumulus Linux to match a multicast group destination address (GDA) range, you must include the /32 operator. In the NVUE command example below, `max-prefix-len 32` after the group match range specifies the /32 operator. In the vtysh command example, `ge 32` after the group permit range specifies the /32 operator.
{{%/notice%}}

{{< tabs "TabID825 ">}}
{{< tab "NVUE Commands ">}}

Create a prefix list with the `permit` keyword to match address ranges that you want to treat as multicast groups and the `deny` keyword for the address ranges you do not want to treat as multicast groups:

```
cumulus@switch:~$ nv set router policy prefix-list MyCustomSSMrange rule 5 match 232.0.0.0/8 max-prefix-len 32
cumulus@switch:~$ nv set router policy prefix-list MyCustomSSMrange rule 5 action permit
cumulus@switch:~$ nv set router policy prefix-list MyCustomSSMrange rule 10 match 238.0.0.0/8 max-prefix-len 32
cumulus@switch:~$ nv set router policy prefix-list MyCustomSSMrange rule 10 action permit
```

Apply the custom prefix list:

```
cumulus@switch:~$ nv set vrf default router pim address-family ipv4-unicast ssm-prefix-list MyCustomSSMrange
cumulus@switch:~$ nv config apply
```

{{< /tab >}}
{{< tab "vtysh Commands ">}}

Create a prefix list with the `permit` keyword to match address ranges that you want to treat as multicast groups and the `deny` keyword for the address ranges you do not want to treat as multicast groups:

```
cumulus@switch:~$ sudo vtysh
...
switch# configure terminal
switch(config)# ip prefix-list ssm-range seq 5 permit 232.0.0.0/8 ge 32
switch(config)# ip prefix-list ssm-range seq 10 permit 238.0.0.0/8 ge 32
```

Apply the custom prefix list as an `ssm-range`:

```
switch(config)# ip pim ssm prefix-list ssm-range
switch(config)# exit
switch# write memory
switch# exit
```

To view the configured prefix lists, run the vtysh `show ip prefix-list my-custom-ssm-range` command:

```
switch#  show ip prefix-list my-custom-ssm-range
ZEBRA: ip prefix-list my-custom-ssm-range: 1 entries
   seq 5 permit 232.0.0.0/8 ge 32
PIM: ip prefix-list my-custom-ssm-range: 1 entries
   seq 10 permit 232.0.0.0/8 ge 32
```

{{< /tab >}}
{{< /tabs >}}

### PIM and ECMP

PIM uses <span class="a-tooltip">[RPF](## "Reverse Path Forwarding")</span> to choose an upstream interface to build a forwarding state. If you configure <span class="a-tooltip">[ECMP](## "Equal Cost Multipaths")</span>, PIM chooses the RPF based on the ECMP hash algorithm.

You can configure PIM to use all the available next hops when installing mroutes. For example, if you have four-way ECMP, PIM spreads the <span class="a-tooltip">[S,G](## "Represents the source entry. S is the multicast source IP. G is the multicast group.")</span> and <span class="a-tooltip">[\*,G](## "Represents the RP Tree. \* is a wildcard indicating any multicast source. G is the multicast group.")</span> mroutes across the four different paths.

You can also configure PIM to recalculate all stream paths over one of the ECMP paths if the switch loses a path. Otherwise, only the streams that are using the lost path move to alternate ECMP paths. This recalculation does not affect existing groups.

{{%notice warning%}}
Recalculating all stream paths over one of the ECMP paths can cause some packet loss.
{{%/notice%}}

{{< tabs "TabID895 ">}}
{{< tab "NVUE Commands ">}}

To configure PIM to use all the available next hops when installing mroutes:

```
cumulus@switch:~$ nv set vrf default router pim ecmp enable on
cumulus@switch:~$ nv config apply
```

To recalculate all stream paths over one of the ECMP paths if the switch loses a path:

```
cumulus@switch:~$ nv set vrf default router pim ecmp rebalance on
cumulus@switch:~$ nv config apply
```

{{< /tab >}}
{{< tab "vtysh Commands ">}}

To configure PIM to use all the available next hops when installing mroutes:

```
cumulus@switch:~$ sudo vtysh
...
switch# configure terminal
switch(config)# ip pim ecmp
switch(config)# exit
switch# write memory
switch# exit
```

To recalculate all stream paths over one of the ECMP paths if the switch loses a path:

```
cumulus@switch:~$ sudo vtysh
...
switch# configure terminal
switch(config)# ip pim ecmp rebalance
switch(config)# exit
switch# write memory
switch# exit
```

{{< /tab >}}
{{< /tabs >}}

To show the next hop for a specific source or group, run the vtysh `show ip pim nexthop` command:

```
cumulus@switch:~$ sudo vtysh
...
switch# show ip pim nexthop
Number of registered addresses: 3
Address         Interface      Nexthop
-------------------------------------------
6.0.0.9         swp31s0        169.254.0.9
6.0.0.9         swp31s1        169.254.0.25
6.0.0.11        lo             0.0.0.0
6.0.0.10        swp31s0        169.254.0.9
6.0.0.10        swp31s1        169.254.0.25
```

### IP Multicast Boundaries

Use multicast boundaries to limit the distribution of multicast traffic and push multicast to a subset of the network. With boundaries in place, the switch drops or accepts incoming IGMP or PIM joins according to a prefix list. To configure the boundary, apply an IP multicast boundary OIL (outgoing interface list) on an interface.

First create a prefix list, then run the following commands:

{{< tabs "TabID983 ">}}
{{< tab "NVUE Commands ">}}

```
cumulus@switch:~$ nv set interface swp1 router pim address-family ipv4-unicast multicast-boundary-oil MyPrefixList
cumulus@switch:~$ nv config apply
```

{{< /tab >}}
{{< tab "vtysh Commands ">}}

```
cumulus@switch:~$ sudo vtysh
...
switch# configure terminal
switch(config)# interface swp1
switch(config-if)# ip multicast boundary oil my-prefix-list
switch(config-if)# end
switch# write memory
switch# exit
```

{{< /tab >}}
{{< /tabs >}}

### MSDP

You can use <span class="a-tooltip">[MSDP](## "Multicast Source Discovery Protocol")</span> to connect multiple PIM-SM multicast domains using the PIM-SM RPs. If you configure anycast RPs with the same IP address on multiple multicast switches (on the loopback interface), you can use more than one RP per multicast group.

When an RP discovers a new source (a PIM-SM register message), it sends an <span class="a-tooltip">[SA](## "source-active")</span> message to each MSDP peer. The peer then determines if there are any interested receivers.

{{%notice note%}}
- Cumulus Linux supports MSDP for anycast RP, not multiple multicast domains. You must configure each MSDP peer in a full mesh. The switch does not forward received SA messages.
- Cumulus Linux only supports one MSDP mesh group.
{{%/notice%}}

The following steps configure a Cumulus switch to use MSDP:

{{< tabs "TabID579 ">}}
{{< tab "NVUE Commands ">}}

1. Add an anycast IP address to the loopback interface for each RP in the domain:

   ```
   cumulus@rp01:~$ nv set interface lo ip address 10.10.10.101/32
   cumulus@rp01:~$ nv set interface lo ip address 10.100.100.100/32
   ```

2. On every multicast switch, configure the group to RP mapping using the anycast address:

   ```
   cumulus@switch:$ nv set vrf default router pim address-family ipv4-unicast rp 10.100.100.100 group-range 224.0.0.0/4
   cumulus@switch:$ nv config apply
   ```

3. Configure the MSDP mesh group for all active RPs. The following example uses three RPs:

   The mesh group must include all RPs in the domain as members, with a unique address as the source. This configuration results in MSDP peerings between all RPs.

   ```
   cumulus@rp01:$ nv set vrf default router pim msdp-mesh-group cumulus member-address 100.1.1.2
   cumulus@rp01:$ nv set vrf default router pim msdp-mesh-group cumulus member-address 100.1.1.3

   cumulus@rp02:$ nv set vrf default router pim msdp-mesh-group cumulus member-address 100.1.1.1
   cumulus@rp02:$ nv set vrf default router pim msdp-mesh-group cumulus member-address 100.1.1.3

   cumulus@rp03:$ nv set vrf default router pim msdp-mesh-group cumulus member-address 100.1.1.1
   cumulus@rp03:$ nv set vrf default router pim msdp-mesh-group cumulus member-address 100.1.1.2
   ```

4. Pick the local loopback address as the source of the MSDP control packets:

   ```
   cumulus@rp01:$ nv set vrf default router pim msdp-mesh-group cumulus source-address 10.10.10.101

   cumulus@rp02:$ nv set vrf default router pim msdp-mesh-group cumulus source-address 10.10.10.102

   cumulus@rp03:$ nv set vrf default router pim msdp-mesh-group cumulus source-address 10.10.10.103
   ```

5. Inject the anycast IP address into the IGP of the domain. If the network uses unnumbered BGP as the IGP, avoid using the anycast IP address to establish unicast or multicast peerings. For PIM-SM, ensure that you use the unique address as the PIM hello source by setting the source:

   ```
   cumulus@rp01:$ nv set interface lo router pim address-family ipv4-unicast use-source 10.100.100.100
   cumulus@rp01:$ nv config apply
   ```

{{< /tab >}}
{{< tab "vtysh Commands ">}}

1. Edit the `/etc/network/interfaces` file to add an anycast IP address to the loopback interface for each RP in the domain. For example:

   ```
   cumulus@rp01:~$ sudo nano /etc/network/interfaces
   auto lo
   iface lo inet loopback
      address 10.10.10.101/32
      address 10.100.100.100/32
   ...
   ```

2. Run the `ifreload -a` command to load the new configuration:

   ```
   cumulus@switch:~$ ifreload -a
   ```

3. On every multicast switch, configure the group to RP mapping using the anycast address:

   ```
   cumulus@rp01:~$ sudo vtysh
   ...
   rp01# configure terminal
   rp01(config)# ip pim rp 10.100.100.100 224.0.0.0/4
   ```

4. Configure the MSDP mesh group for all active RPs (the following example uses three RPs):

   The mesh group must include all RPs in the domain as members, with a unique address as the source. This configuration results in MSDP peerings between all RPs.

   ```
   rp01(config)# ip msdp mesh-group cumulus member 100.1.1.2
   rp01(config)# ip msdp mesh-group cumulus member 100.1.1.3

   rp02(config)# ip msdp mesh-group cumulus member 100.1.1.1
   rp02(config)# ip msdp mesh-group cumulus member 100.1.1.3

   rp03(config)# ip msdp mesh-group cumulus member 100.1.1.1
   rp03(config)# ip msdp mesh-group cumulus member 100.1.1.2
   ```

5. Pick the local loopback address as the source of the MSDP control packets

   ```
   rp01(config)# ip msdp mesh-group cumulus source 10.10.10.101
   rp02(config)# ip msdp mesh-group cumulus source 10.10.10.102
   rp03(config)# ip msdp mesh-group cumulus source 10.10.10.103
   ```

6. Inject the anycast IP address into the IGP of the domain. If the network uses unnumbered BGP as the IGP, avoid using the anycast IP address to establish unicast or multicast peerings. For PIM-SM, ensure that you use the unique address as the PIM hello source by setting the source:

   ```
   rp01# interface lo
   rp01(config-if)# ip pim use-source 100.100.100.100
   rp01(config-if)# end
   rp01# write memory
   rp01# exit
   ```

{{< /tab >}}
{{< /tabs >}}

### PIM in a VRF

{{<link url="Virtual-Routing-and-Forwarding-VRF" text="VRFs">}} divide the routing table on a per-tenant basis to provide separate layer 3 networks over a single layer 3 infrastructure. With a VRF, each tenant has its own virtualized layer 3 network so IP addresses can overlap between tenants.

PIM in a VRF enables PIM trees and multicast data traffic to run inside a layer 3 virtualized network, with a separate tree per domain or tenant. Each VRF has its own multicast tree with its own RPs, sources, and so on. Therefore, you can have one tenant per corporate division, client, or product.

If you do not enable <span class="a-tooltip">[MP-BGP](## "Multi Protocol BGP ")</span> <span class="a-tooltip">[MPLS VPN](## "Multiprotocol Label Switching virtual private network")</span>, VRFs on different switches typically connect or peer over subinterfaces, where each subinterface is in its own VRF.

To configure PIM in a VRF:

{{< tabs "TabID1170 ">}}
{{< tab "NVUE Commands ">}}

Add the VRFs and associate them with switch ports:

```
cumulus@switch:~$ nv set vrf RED
cumulus@switch:~$ nv set vrf BLUE
cumulus@switch:~$ nv set interface swp1 ip vrf RED
cumulus@switch:~$ nv set interface swp2 ip vrf BLUE
```

Add PIM configuration:

```
cumulus@switch:~$ nv set interface swp1 router pim
cumulus@switch:~$ nv set interface swp2 router pim
cumulus@switch:~$ nv set vrf RED router bgp autonomous-system 65001
cumulus@switch:~$ nv set vrf BLUE router bgp autonomous-system 65000
cumulus@switch:~$ nv set vrf RED router bgp router-id 10.1.1.1
cumulus@switch:~$ nv set vrf BLUE router bgp router-id 10.1.1.2
cumulus@switch:~$ nv set vrf RED router bgp neighbor swp1 remote-as external
cumulus@switch:~$ nv set vrf BLUE router bgp neighbor swp2 remote-as external
cumulus@switch:~$ nv config apply
```

{{< /tab >}}
{{< tab "vtysh Commands ">}}

Edit the `/etc/network/interfaces` file and to the VRFs and associate them with switch ports, then run `ifreload -a` to reload the configuration.

```
cumulus@switch:~$ sudo nano /etc/network/interfaces
...
auto swp1
iface swp1
    vrf RED

auto swp2
iface swp2
    vrf BLUE

auto RED
iface RED
    vrf-table auto

auto BLUE
iface BLUE
    vrf-table auto
...
```

Add the PIM configuration:

```
cumulus@switch:~$ sudo vtysh
...
switch# configure terminal
switch(config)# interface swp1
switch(config-if)# ip pim
switch(config-if)# exit
switch(config)# interface swp2
switch(config-if)# ip pim
switch(config-if)# exit
switch(config)# router bgp 65001 vrf RED
switch(config-router)# bgp router-id 10.1.1.2
switch(config-router)# neighbor swp1 interface remote-as external
switch(config-router)# exit
switch(config)# router bgp 65000 vrf BLUE
switch(config-router)# bgp router-id 10.1.1.1
switch(config-router)# neighbor swp2 interface remote-as external
switch(config-router)# end
switch# write memory
switch# exit
```

{{< /tab >}}
{{< /tabs >}}

### BFD for PIM Neighbors

You can use {{<link url="Bidirectional-Forwarding-Detection-BFD" text="BFD">}} for PIM neighbors to detect link failures. When you configure an interface, include the `pim bfd` option. The following example commands configure BFD between leaf01 and spine01:

{{< tabs "TabID709 ">}}
{{< tab "NVUE Commands ">}}

{{< tabs "TabID886 ">}}
{{< tab "leaf01 ">}}

```
cumulus@leaf01:~$ nv set interface swp51 router pim bfd enable on
cumulus@leaf01:~$ nv config apply
```

{{< /tab >}}
{{< tab "spine01 ">}}

```
cumulus@spine01:~$ nv set interface swp1 router pim bfd enable on
cumulus@spine01:~$ nv config apply
```

{{< /tab >}}
{{< /tabs >}}

{{< /tab >}}
{{< tab "vtysh Commands ">}}

{{< tabs "TabID736 ">}}
{{< tab "leaf01 ">}}

```
cumulus@leaf01:~$ sudo vtysh
...
leaf01# configure terminal
leaf01(config)# interface swp51
leaf01(config-if)# ip pim bfd
leaf01(config-if)# end
leaf01# write memory
leaf01# exit
```

{{< /tab >}}
{{< tab "spine01 ">}}

```
cumulus@spine01:~$ sudo vtysh
...
spine01# configure terminal
spine01(config)# interface swp1
spine01(config-if)# ip pim bfd
spine01(config-if)# end
spine01# write memory
spine01# exit
```

{{< /tab >}}
{{< /tabs >}}

{{< /tab >}}
{{< /tabs >}}

### Allow RP

To begin receiving multicast traffic for a group, a receiver expresses its interest in the group by sending an IGMP membership report on its connected LAN. The LHR receives this report and begins to build a multicast routing tree back towards the source. To build this tree, another router known both to the LHR and to the multicast source needs to exist to act as an RP for senders and receivers. The LHR looks up the RP for the group specified by the receiver and sends a PIM Join message towards the RP. Per RFC 7761, intermediary routers between the LHR and the RP must check that the RP for the group matches the one in the PIM Join, and if not, to drop the Join.

In some configurations, it is desirable to configure the LHR with an RP address that does not match the actual RP address for the group. In this case, you must configure the upstream routers to accept the Join and propagate it towards the appropriate RP for the group, ignoring the mismatched RP address in the PIM Join and replacing it with its own RP for the group.

You can configure the switch to allow joins from all upstream neighbors or you can provide a prefix list so that the switch only accepts joins with an upstream neighbor address.

{{< tabs "TabID997 ">}}
{{< tab "NVUE Commands ">}}

The following example command configures PIM to ignore the RP check for all upstream neighbors:

```
cumulus@switch:~$ nv set interface swp50 router pim address-family ipv4-unicast allow-rp enable on
cumulus@switch:~$ nv config apply
```

The following example command configures PIM to only ignore the RP check for the upstream neighbors in the prefix list called allowRP:

```
cumulus@switch:~$ nv set interface swp50 router pim address-family ipv4-unicast allow-rp rp-list allowRP
cumulus@switch:~$ nv config apply
```

{{< /tab >}}
{{< tab "vtysh Commands ">}}

The following example command configures PIM to ignore the RP check for all upstream neighbors:

```
cumulus@switch:~$ sudo vtysh
...
switch# configure terminal
switch(config)# interface swp50
switch(config-if)# ip pim allow-rp
switch(config-if)# end
switch# write memory
switch# exit
```

The following example command configures PIM to only ignore the RP check for the upstream neighbors in the prefix list called allowRP:

```
cumulus@switch:~$ sudo vtysh
...
switch# configure terminal
switch(config)# interface swp50
switch(config-if)# ip pim allow-rp rp-list allowRP
switch(config-if)# end
switch# write memory
switch# exit
```

{{< /tab >}}
{{< /tabs >}}

### PIM Timers

Cumulus Linux provides the following PIM timers:

| Timer | Description |
|------ | ----------- |
| `hello-interval` | The interval in seconds at which the PIM router sends hello messages to discover PIM neighbors and maintain PIM neighbor relationships. You can specify a value between 1 and 180. The default setting is 30 seconds. With vtysh, you set the hello interval for a specific PIM enabled interface. With NVUE, you can set the hello interval globally for all PIM enabled interfaces or for a specific PIM enabled interface.  |
| `holdtime`  | The number of seconds during which the neighbor must be in a reachable state. `auto` (the default setting) uses three and half times the `hello-interval`. You can specify a value between 1 and 180. With vtysh, you set the holdtime for a specific PIM enabled interface. With NVUE, you can set the holdtime globally for all PIM enabled interfaces or for a specific PIM enabled interface.|
| `join-prune-interval` | The interval in seconds at which a PIM router sends join/prune messages to its upstream neighbors for a state update. You can specify a value between 60 and 600. The default setting is 60 seconds. You set the `join-prune-interval` globally for all PIM enabled interfaces. NVUE also provides the option of setting the `join-prune-interval` for a specific VRF.|
| `keep-alive` | The timeout value for the S,G stream in seconds. You can specify a value between 31 and 60000. The default setting is 210 seconds. You can set the `keep-alive` timer globally or all PIM enabled interfaces or for a specific VRF.|
| `register-suppress` | The number of seconds during which to stop sending register messages to the RP. You can specify a value between 5 and 60000. The default setting is 60 seconds. You can set the `keep-alive` timer globally for all PIM enabled interfaces or for a specific VRF. |
| `rp-keep-alive` | NVUE only. The timeout value for the RP in seconds. You can specify a value between 31 and 60000. The default setting is 185 seconds. You set the `register-suppress-time` timer globally for all PIM enabled interfacesor for a specific VRF.|

{{< tabs "TabID1037 ">}}
{{< tab "NVUE Commands ">}}

The following example commands set the `join-prune-interval` to 100 seconds, the `keep-alive` timer to 10000 seconds, and the `register-suppress` time to 20000 seconds globally for all PIM enabled interfaces:

```
cumulus@switch:~$ nv set router pim timers join-prune-interval 100
cumulus@switch:~$ nv set router pim timers keep-alive 10000
cumulus@switch:~$ nv set router pim timers register-suppress 20000
cumulus@switch:~$ nv config apply
```

The following example commands set the `hello-interval` to 60 seconds for swp51:

```
cumulus@switch:~$ nv set interface swp51 router pim timers hello-interval 60
cumulus@switch:~$ nv config apply
```

The following example commands set the `rp-keep-alive` to 10000 for VRF RED:

```
cumulus@switch:~$ nv set vrf RED router pim timers rp-keep-alive 10000
cumulus@switch:~$ nv config apply
```

{{< /tab >}}
{{< tab "vtysh Commands ">}}

The following example commands set the `join-prune-interval` to 100 seconds, the `keep-alive` timer to 10000 seconds, and the `register-suppress` time to 20000 seconds globally for all PIM enabled interfaces:

```
cumulus@switch:~$ sudo vtysh
...
switch# configure terminal
switch(config)# ip pim join-prune-interval 100
switch(config)# ip pim keep-alive-timer 10000
switch(config)# ip pim register-suppress-time 20000
switch(config)# end
switch# write memory
switch# exit
```

The following example command sets the `hello-interval` to 60 seconds and the `holdtime` to 120 for swp51:

```
cumulus@switch:~$ sudo vtysh
...
switch# configure terminal
switch(config)# interface swp51
switch(config-if)# ip pim hello 60 120
switch(config-if)# end
switch# write memory
switch# exit
```

The following example command sets the `keep-alive-timer` to 10000 seconds for VRF RED:

```
cumulus@switch:~$ sudo vtysh
...
switch# configure terminal
switch(config)# vrf RED
switch(config-vrf)# ip pim keep-alive-timer 10000
switch(config-if)# end
switch# write memory
switch# exit
```

{{< /tab >}}
{{< /tabs >}}

### Improve Multicast Convergence

For large multicast environments, the default <span class="a-tooltip">[CoPP](## "Control Plane Policing")</span> policer might be too restrictive. You can adjust the policer to improve multicast convergence.

- The default PIM forwarding rate and burst rate is set to 2000 packets per second.
- The default IGMP forwarding rate and burst rate is set to 1000 packets per second.

To adjust the policer:

{{< tabs "991 ">}}
{{< tab "NVUE Commands ">}}

The following example commands set the PIM forwarding and burst rate to 400 packets per second:

```
cumulus@switch:~$ nv set system control-plane policer pim-ospf-rip rate 400
cumulus@switch:~$ nv set system control-plane policer pim-ospf-rip burst 400
cumulus@switch:~$ nv config apply 
```

The following example commands set the IGMP forwarding rate to 400 and the IGMP burst rate to 200 packets per second:

```
cumulus@switch:~$ nv set system control-plane policer igmp rate 400
cumulus@switch:~$ nv set system control-plane policer igmp burst 200
cumulus@switch:~$ nv config apply 
```

{{< /tab >}}
{{< tab "Edit /etc/cumulus/control-plane/policers.conf ">}}

1. Edit the `/etc/cumulus/control-plane/policers.conf` file:

   - To tune the PIM forwarding and burst rate, change the `copp.pim_ospf_rip.rate` and `copp.pim_ospf_rip.burst` parameters.
   - To tune the IGMP forwarding and burst rate, change the `copp.igmp.rate` and `copp.igmp.burst` parameters.

      The following example changes the PIM forwarding rate and the PIM burst rate to 400 packets per second, the IGMP forwarding rate to 400 packets per second and the IGMP burst rate to 200 packets per second:

      ```
      cumulus@switch:~$ sudo nano /etc/cumulus/control-plane/policers.conf
      ...
      copp.pim_ospf_rip.enable = TRUE
      copp.pim_ospf_rip.rate = 400
      copp.pim_ospf_rip.burst = 400
      ...
      copp.igmp.enable = TRUE
      copp.igmp.rate = 400
      copp.igmp.burst = 200
      ...
      ```

2. Run the following command:

   ```
   cumulus@switch:~$ /usr/lib/cumulus/switchdctl --load /etc/cumulus/control-plane/policers.conf
   ```

{{< /tab >}}
{{< /tabs >}}

### IGMP Settings

You can set the following optional IGMP settings on a PIM interface:
- The last member query interval, which is the maximum response time advertised in IGMP group-specific queries. You can specify a value between 1 and 6553 seconds. The default setting is 10.
- The maximum response time for IGMP general queries. You can specify a value between 1 and 6553 seconds. The default setting is 100.
- The last member query count, which is the number of group-specific queries that a querier can send after receiving a leave message on the interface. You can specify a value between 1 and 255. The default setting is 2.
- How often IGMP sends query-host messages to discover which multicast groups have members on the attached networks. You can specify a value between 1 and 65535 seconds. The default setting is 125.
- Fast leave processing, where the switch immediately removes a port from the forwarding entry for a multicast group when the port receives a leave message. The default setting is off.

{{< tabs "TabID356 ">}}
{{< tab "NVUE Commands ">}}

The following example sets the last member query interval to 80, the maximum response time for IGMP general queries to 120 seconds, the number of group-specific queries that a querier can send to 5, and configures IGMP to send query-host messages every 180 seconds:

```
cumulus@switch:~$ nv set interface swp1 ip igmp last-member-query-interval 80
cumulus@switch:~$ nv set interface swp1 ip igmp query-max-response-time 120
cumulus@switch:~$ nv set interface swp1 ip igmp last-member-query-count 5
cumulus@switch:~$ nv set interface swp1 ip igmp query-interval 180
cumulus@switch:~$ nv config apply
```

The following example enables fast leave processing:

```
cumulus@switch:~$ nv set interface swp1 ip igmp fast-leave on
cumulus@switch:~$ nv config apply
```

To disable fast leave processing, run the `nv set interface <interface> ip igmp fast-leave off` command.

{{< /tab >}}
{{< tab "Linux and vtysh Commands ">}}

The following example sets the last member query interval to 80, the maximum response time for IGMP general queries to 120 seconds, the number of group-specific queries that a querier sends to 5, and configures IGMP to send query-host messages every 180 seconds:

```
cumulus@switch:~$ sudo vtysh
...
switch# configure terminal
switch(config)# 
switch(config)# interface vlan10
leaf02(config-if)# ip igmp last-member-query-interval 80
leaf02(config-if)# ip igmp query-max-response-time 120
leaf02(config-if)# ip igmp last-member-query-count 5
leaf02(config-if)# ip igmp query-interval 180
leaf02(config-if)# end
switch# write memory
switch# exit
```

The vtysh `ip igmp last-member-query-count` command adds the configuration to the `/etc/frr/frr.conf file`:

```
cumulus@switch:~$ sudo nano /etc/frr/frr.conf
...
ip igmp
ip igmp version 3
ip igmp query-interval 180
ip igmp last-member-query-interval 80
ip igmp last-member-query-count 5
ip igmp query-max-response-time 120
...
```

To enable fast leave processing, edit the `/etc/network/interfaces` file and add the `bridge-portmcfl yes` parameter under the interface stanza:

```
cumulus@switch:~$ sudo nano /etc/network/interfaces
...
auto vlan10
iface vlan10
    address 10.1.10.1/24
    hwaddress 44:38:39:22:01:b1
    bridge-portmcfl yes
    vlan-raw-device br_default
    vlan-id 10
...
```

To disable fast leave processing, edit the `/etc/network/interfaces` file and set the `bridge-portmcfl no` parameter under the interface stanza.

{{< /tab >}}
{{< /tabs >}}

<!-- vale off -->
<!-- vale.ai Issue #253 -->
## PIM Active-active with MLAG
<!-- vale on -->

When a **multicast sender** attaches to an MLAG bond, the sender hashes the outbound multicast traffic over a single member of the bond. Traffic arrives on one of the MLAG enabled switches. Regardless of which switch receives the traffic, it goes over the MLAG peer link to the other MLAG-enabled switch, because the peerlink is always the multicast router port and always receives the multicast stream.

{{%notice note%}}
Traffic from multicast sources attached to an MLAG bond always goes over the MLAG peerlink. Be sure to
{{<link url="Multi-Chassis-Link-Aggregation-MLAG#peer-link-sizing" text="size the peerlink appropriately">}} to accommodate this traffic.
{{%/notice%}}

The <span class="a-tooltip">[PIM DR](## "PIM Designated Router")</span> for the VLAN where the source resides sends the PIM register towards the RP. The PIM DR is the PIM speaker with the highest IP address on the segment. After the PIM register process is complete and traffic is flowing along the <span class="a-tooltip">[SPT](## "Shortest Path Tree ")<span>, either MLAG switch forwards traffic towards the receivers.

PIM joins sent towards the source can be ECMP load shared by upstream PIM neighbors. Either MLAG member can receive the PIM join and forward traffic, regardless of DR status.

A dual-attached **multicast receiver** sends an IGMP join on the attached VLAN. One of the MLAG switches receives the IGMP join, then adds the IGMP join to the IGMP Join table and layer 2 MDB table. The layer 2 MDB table, like the unicast MAC address table, synchronizes through MLAG control messages over the peerlink. This allows both MLAG switches to program IGMP and MDB table forwarding information. Both switches send *,G PIM Join messages towards the RP. If the source is already sending, both MLAG switches receive the multicast stream.

{{%notice note%}}
Traditionally, the PIM DR is the only node to send the PIM *,G Join. To provide resiliency in case of failure, both MLAG switches send PIM *,G Joins towards the RP to receive the multicast stream.
{{%/notice%}}

To prevent duplicate multicast packets, PIM elects a <span class="a-tooltip">[DF](## "PIM Designated Forwarder")</span>, which is the `primary` member of the MLAG pair. The MLAG secondary switch puts the VLAN in the <span class="a-tooltip">[OIL](## "Outgoing Interface List")</span>, preventing duplicate multicast traffic.

### Example Traffic Flow

The examples below show the flow of traffic between server02 and server03:

| Step 1 |  |
|--------|--------|
|{{< figure src = "/images/cumulus-linux/pim-mlag-citc-topology1.png" >}}| **1**. server02 sends traffic to leaf02.<br><br>**2**. leaf02 forwards traffic to leaf01 because the peerlink is a multicast router port.<br><br>**3**. spine01 receives a PIM register from leaf01, the DR.<br><br>**4**. leaf02 syncs the *,G table from leaf01 as an MLAG active-active peer. |

| Step 2 |  |
|--------|--------|
| {{< figure src = "/images/cumulus-linux/pim-mlag-citc-topology2.png" >}} | **1**. leaf02 has the *,G route indicating that it must forward traffic towards spine01.<br><br>**2**. Either leaf02 or leaf01 sends this traffic directly based on which MLAG switch receives it from the attached source.<br><br>**3**. In this case, leaf02 receives the traffic on the MLAG bond and forwards it directly upstream.|

### Configure PIM with MLAG

You can use a multicast sender or receiver over a dual-attached MLAG bond. On the VLAN interface where multicast sources or receivers exist, configure PIM active-active and IGMP. Enabling PIM active-active automatically enables PIM on that interface.

{{< tabs "TabID363 ">}}
{{< tab "NVUE Commands ">}}

```
cumulus@leaf01:~$ nv set interface vlan10 router pim active-active on
cumulus@leaf01:~$ nv set interface vlan10 ip igmp
cumulus@leaf01:~$ nv config apply
```

{{< /tab >}}
{{< tab "vtysh Commands ">}}

```
cumulus@leaf01:~$ sudo vtysh
...
leaf01# configure terminal
leaf01(config)# interface vlan10
leaf01(config-if)# ip pim active-active
leaf01(config-if)# ip igmp
leaf01(config-if)# end
leaf01# write memory
leaf01# exit
```

{{< /tab >}}
{{< /tabs >}}

To verify PIM active-active configuration, run the vtysh `show ip pim mlag summary` command or the `net show pim mlag summary` command:

```
cumulus@leaf01:mgmt:~$ sudo vtysh
...
leaf01# show ip pim mlag summary
MLAG daemon connection: up
MLAG peer state: up
Zebra peer state: up
MLAG role: PRIMARY
Local VTEP IP: 0.0.0.0
Anycast VTEP IP: 0.0.0.0
Peerlink: peerlink.4094
Session flaps: mlagd: 0 mlag-peer: 0 zebra-peer: 0
Message Statistics:
mroute adds: rx: 5, tx: 5
mroute dels: rx: 0, tx: 0
peer zebra status updates: 1
PIM status updates: 0
VxLAN updates: 0
```

## Troubleshooting

This section provides commands to examine your PIM configuration and provides troubleshooting tips.

### PIM Show Commands

To show the contents of the IP multicast routing table, run the vtysh `show ip mroute` command or the `net show mroute` command. You can verify the (S,G) and (*,G) state entries from the flags and check that the incoming and outgoing interfaces are correct:

```
cumulus@fhr:~$ sudo vtysh
...
fhr# show ip mroute
IP Multicast Routing Table
Flags: S - Sparse, C - Connected, P - Pruned
       R - RP-bit set, F - Register flag, T - SPT-bit set

Source          Group           Flags    Proto  Input            Output           TTL  Uptime
10.1.10.101     239.1.1.1       SFP      none   vlan10           none             0    --:--:-- 
```

To see the active source on the switch, run the vtysh `show ip pim upstream` command or the `net show pim upstream` command.

```
cumulus@fhr:~$ sudo vtysh
...
fhr# show ip pim upstream
Iif    Source        Group     State   Uptime    JoinTimer  RSTimer   KATimer   RefCnt
vlan10 10.1.10.101   239.1.1.1 Prune   00:07:40  --:--:--   00:00:36  00:02:50  1
```

To show upstream information for S,Gs and the desire to join the multicast tree, run the vtysh `show ip pim upstream-join-desired` command or the `net show pim upstream-join-desired` command.

```
cumulus@fhr:~$ sudo vtysh
...
fhr# show ip pim upstream-join-desired
Source          Group           EvalJD
10.1.10.101     239.1.1.1       yes 
```

To show the PIM interfaces on the switch, run the vtysh `show ip pim interface` command or the `net show pim interface` command.

```
cumulus@fhr:mgmt:~$ sudo vtysh
...
fhr# show ip pim interface
Interface         State          Address  PIM Nbrs           PIM DR  FHR IfChannels
lo                   up       10.10.10.1         0            local    0          0
swp51                up       10.10.10.1         1     10.10.10.101    0          0
vlan10               up        10.1.10.1         0            local    1          0
```

The vtysh `show ip pim interface detail` command and the `net show pim interface detail` command shows more detail about the PIM interfaces on the switch:

```
cumulus@fhr:~$ sudo vtysh
...
fhr# show ip pim interface detail
...
Interface  : vlan10
State      : up
Address    : 10.1.10.1 (primary)
             fe80::4638:39ff:fe00:31/64

Designated Router
-----------------
Address   : 10.1.10.1
Priority  : 1(0)
Uptime    : --:--:--
Elections : 1
Changes   : 0

FHR - First Hop Router
----------------------
239.1.1.1 : 10.1.10.101 is a source, uptime is 00:03:08
...
```

To show local membership information for a PIM interface, run the vtysh `show ip pim local-membership` command or the  `net show pim local-membership`.

```
cumulus@lhr:~$ sudo vtysh
...
lhr# show ip pim local-membership
Interface         Address          Source           Group            Membership
vlan20            10.2.10.1        *                239.1.1.1        INCLUDE 
```

To show information about known S,Gs, the <span class="a-tooltip">[IIF](## "Incoming Interface")</span> and the <span class="a-tooltip">[OIL](## "Outgoing Interface")</span>, run the vtysh `show ip pim state` command or the `net show pim state` command.

```
cumulus@fhr:~$ sudo vtysh
...
fhr# show ip pim state
Codes: J -> Pim Join, I -> IGMP Report, S -> Source, * -> Inherited from (*,G), V -> VxLAN, M -> Muted
Active Source           Group            RPT  IIF               OIL
1      10.1.10.101      239.1.1.1        n    vlan10 
```

To show the IGMP configuration settings for an interface, run the `nv show interface <interface> ip igmp` command

```
cumulus@lhr:~$ nv show interface swp3 ip igmp
                            operational  applied
--------------------------  -----------  -------
enable                                   on     
fast-leave                               off    
last-member-query-count                  2      
last-member-query-interval               10     
query-interval                           125    
query-max-response-time                  100    
version                                  3      
[static-group]                                  
[group]           
```

To show IGMP operational data for an interface, run the NVUE `nv show interface <interface> ip igmp -o json` command or the vtysh `show ip igmp statistics` command.

To verify that the receiver is sending IGMP reports (joins) for the group, run the NVUE `nv show interface <interface> ip igmp group` command or the vtysh `show ip igmp groups` command.

```
cumulus@lhr:~$ nv show interface swp3 ip igmp group
StaticGroupID  filter-mode  source-count  timer     uptime    version  Summary
-------------  -----------  ------------  --------  --------  -------  -------------------------
225.1.101.1    exclude      1             00:02:43  00:02:56  3        source-address:         *
225.1.101.2    exclude      1             00:02:43  00:02:56  3        source-address:         *
225.1.101.3    exclude      1             00:02:43  00:02:56  3        source-address:         *
225.1.101.4    exclude      1             00:02:43  00:02:56  3        source-address:         *
225.1.101.5    exclude      1             00:02:43  00:02:56  3        source-address:         *
232.1.1.99     include      1             --:--:--  00:00:02  3        source-address: 10.1.10.1
```

To show IGMP source information, run the vtysh `show ip igmp sources` command or the `net show igmp sources` command.

```
cumulus@lhr:~$ sudo vtysh
...
lhr# show ip igmp sources
Interface        Address         Group           Source          Timer Fwd Uptime  
vlan20           10.2.10.1       239.1.1.1       *               03:13   Y 05:28:42 
```

### FHR Stuck in the Registering Process

When a multicast source starts, the FHR sends unicast PIM register messages from the <span class="a-tooltip">[RPF](## "Reverse Path Forwarding")</span> interface towards the source. After the RP receives the PIM register, it sends a `PIM register stop` message to the FHR to end the register process. If an issue occurs with this communication, the FHR becomes stuck in the registering process, which can result in high CPU (the FHR CPU generates and sends PIM register packets to the RP CPU).

To assess this issue, review the FHR. You can see the output interface of `pimreg` here. If this does not change to an interface within a couple of seconds, it is possible that the FHR remains in the registering process.

```
cumulus@fhr:~$ sudo vtysh
...
fhr# show ip mroute
Source          Group           Proto  Input      Output     TTL  Uptime
10.1.10.101     239.2.2.3       PIM    vlan10     pimreg     1    00:03:59
```

To troubleshoot the issue:

1. Validate that the FHR can reach the RP. If the RP and FHR can not communicate, the registration process fails:

   ```
   cumulus@fhr:~$ ping 10.10.10.101
   PING 10.10.10.101 (10.10.10.101) from 10.1.10.1: 56(84) bytes of data.
   ^C
   --- 10.0.0.21 ping statistics ---
   4 packets transmitted, 0 received, 100% packet loss, time 3000ms
   ```

2. On the RP, use `tcpdump` to see if the PIM register packets arrive:

   ```
   cumulus@rp01:~$ sudo tcpdump -i swp1
   tcpdump: verbose output suppressed, use -v or -vv for full protocol decode
   listening on swp1, link-type EN10MB (Ethernet), capture size 262144 bytes
   23:33:17.524982 IP 10.1.10.101 > 10.10.10.101: PIMv2, Register, length 66
   ```

3. If the switch is receiving PIM registration packets, verify that PIM sees them by running the vtysh `debug pim packets` command:

   ```
   cumulus@fhr:~$ sudo vtysh -c "debug pim packets"
   PIM Packet debugging is on

   cumulus@rp01:~$ sudo tail /var/log/frr/frr.log
   2016/10/19 23:46:51 PIM: Recv PIM REGISTER packet from 172.16.5.1 to 10.0.0.21 on swp30: ttl=255 pim_version=2 pim_msg_size=64 checksum=a681
   ```

4. Repeat the process on the FHR to see that it receives PIM register stop messages and passes them to the PIM process:

   ```
   cumulus@fhr:~$ sudo tcpdump -i swp51
   23:58:59.841625 IP 172.16.5.1 > 10.0.0.21: PIMv2, Register, length 28
   23:58:59.842466 IP 10.0.0.21 > 172.16.5.1: PIMv2, Register Stop, length 18

   cumulus@fhr:~$ sudo vtysh -c "debug pim packets"
   PIM Packet debugging is on

   cumulus@fhr:~$ sudo tail -f /var/log/frr/frr.log
   2016/10/19 23:59:38 PIM: Recv PIM REGSTOP packet from 10.10.10.101 to 10.10.10.1 on swp51: ttl=255 pim_version=2 pim_msg_size=18 checksum=5a39
   ```

### LHR Does Not Build \*,G

If you do not enable both PIM **and** IGMP on an interface facing a receiver, the LHR does not build <span class="a-tooltip">[\*,G](## "Represents the RP Tree. \* is a wildcard indicating any multicast source. G is the multicast group.")</span>.

```
cumulus@lhr:~$ sudo vtysh
...
lhr# show run
!
interface vlan20
 ip igmp
 ip pim
```

To troubleshoot this issue, ensure that the receiver sends IGMPv3 joins when you enable both PIM and IGMP:

```
cumulus@lhr:~$ sudo tcpdump -i vlan20 igmp
tcpdump: verbose output suppressed, use -v or -vv for full protocol decode
listening on vlan20, link-type EN10MB (Ethernet), capture size 262144 bytes
00:03:55.789744 IP 10.2.10.1 > igmp.mcast.net: igmp v3 report, 1 group record(s)
```

### No mroute Created on the FHR

To troubleshoot this issue:

1. Verify that the FHR is receiving multicast traffic:

   ```
   cumulus@fhr:~$ sudo tcpdump -i vlan10
   tcpdump: verbose output suppressed, use -v or -vv for full protocol decode
   listening on vlan10, link-type EN10MB (Ethernet), capture size 262144 bytes
   19:57:58.429632 IP 10.1.10.101.42420 > 239.1.1.1.1000: UDP, length 8
   19:57:59.431250 IP 10.1.10.101.42420 > 239.1.1.1.1000: UDP, length 8
   ```

2. Verify PIM configuration on the interface facing the source:

   ```
   cumulus@fhr:~$ sudo vtysh
   ...
   fhr# show run
   !
   interface vlan10
    ip igmp
    ip pim
   !
   ```

3. Verify that the <span class="a-tooltip">[RPF](## "Reverse Path Forwarding")</span> interface for the source matches the interface that receives multicast traffic:

   ```
   fhr# show ip rpf 10.1.10.1
   Routing entry for 10.1.10.0/24 using Unicast RIB
   Known via "connected", distance 0, metric 0, best
   Last update 1d00h26m ago
   * directly connected, vlan10
   ```

4. Verify RP configuration for the multicast group:

   ```
   fhr# show ip pim rp-info
   RP address       group/prefix-list   OIF               I am RP    Source
   10.10.10.101     224.0.0.0/4         swp51             no         Static
   ```

### No S,G on the RP for an Active Group

An RP does not build an mroute when there are no active receivers for a multicast group even though the FR creates the mroute.

```
cumulus@rp01:~$ sudo vtysh
...
rp01# show ip mroute
Source          Group           Flags    Proto  Input            Output           TTL  Uptime
```

You can see the active source on the RP with either the vtysh `show ip pim upstream` command or the `net show pim upstream` command.

```
cumulus@rp01:~$ sudo vtysh
...
rp01# show ip pim upstream
Iif             Source          Group           State       Uptime   JoinTimer RSTimer   KATimer   RefCnt
vlan10          10.1.10.101     239.1.1.1       Prune       00:08:03 --:--:--  --:--:--  00:02:20       1
```

### No mroute Entry in Hardware

To verify that the hardware IP multicast entry is the maximum value, run the `cl-resource-query | grep Mcast` command or the `net show system asic | grep Mcast` command.

```
cumulus@switch:~$ cl-resource-query  | grep Mcast
Total Mcast Routes:         450,   0% of maximum value    450
```

Refer to {{<link url="Supported-Route-Table-Entries#tcam-resource-profiles-for-spectrum-switches" text="TCAM Resource Profiles for Spectrum Switches">}}.

### Verify the MSDP Session State

To verify the state of MSDP sessions, run the vtysh `show ip msdp mesh-group` command or the `net show msdp mesh-group` command.

```
cumulus@switch:~$ sudo vtysh
...
switch# show ip msdp mesh-group
Mesh group : pod1
  Source : 10.1.10.101
  Member                 State
  10.1.10.102        established
  10.1.10.103        established

cumulus@switch:~$ sudo vtysh
switch# show ip msdp peer
Peer                    Local         State     Uptime    SaCnt
10.1.10.102       10.1.10.101   established    00:07:21       0
10.1.10.103       10.1.10.101   established    00:07:21       0
```

### View the Active Sources

To review the active sources that the switch learns locally (through PIM registers) and from MSDP peers, run the vtysh `show ip msdp sa` command or the `net show msdp sa` command.

```
cumulus@switch:~$ sudo vtysh
...
switch# show ip msdp sa
Source                Group               RP   Local    SPT      Uptime
10.1.10.101       239.1.1.1     10.10.10.101       n      n    00:00:40
10.1.10.101       239.1.1.2    100.10.10.101       n      n    00:00:25
```

### Clear PIM State and Statistics

If you are troubleshooting or making changes to your multicast environment, you can:
- Clear PIM neighbors for all PIM interfaces in a VRF.
- Clear traffic statistics for all PIM interfaces in a VRF.
- Clear the IGMP interface state.

{{< tabs "TabID1404 ">}}
{{< tab "NVUE Commands ">}}

To clear PIM neighbors for all PIM interfaces in a VRF:

```
cumulus@switch:~$ nv action clear vrf default router pim interfaces
Action succeeded
```

To clear traffic statistics for all PIM interfaces in a VRF:

```
cumulus@switch:~$ nv action clear vrf default router pim interface-traffic
Action succeeded
```

To clear the IGMP interface state:

```
cumulus@switch:~$ nv action clear router igmp interfaces
Action succeeded
```

{{< /tab >}}
{{< tab "vtysh Commands ">}}

To clear PIM neighbors for all PIM interfaces in a VRF:

```
cumulus@switch:~$ sudo vtysh
...
switch# clear ip pim vrf default interfaces
switch# exit
```

To clear traffic statistics for all PIM interfaces in a VRF:

```
cumulus@switch:~$ sudo vtysh
...
switch# clear ip pim vrf default interface traffic
switch# exit
```

To rescan the PIM OIL to update the output interface list in a VRF:

```
cumulus@switch:~$ sudo vtysh
...
switch# clear ip pim vrf default oil
switch# exit
```

To clear all PIM process statistics in a VRF:

```
cumulus@switch:~$ sudo vtysh
...
switch# clear ip pim statistics vrf default
switch# exit
```

To clear all PIM process statistics:

```
cumulus@switch:~$ sudo vtysh
...
switch# clear ip pim statistics
switch# exit
```

To clear the IGMP interface state:

```
cumulus@switch:~$ sudo vtysh
...
switch# clear ip igmp interfaces
switch# exit
```

{{< /tab >}}
{{< /tabs >}}

## Configuration Example

The following example configures PIM and BGP on leaf01, leaf02, and spine01.

- server01 (the source) connects to leaf01 (the FHR) through a VLAN-aware bridge (VLAN 10).
- leaf01 connects to spine01 (the RP) through swp51.
- spine01 connects to leaf02 (the LHR) through swp2.
- leaf02 connects to server02 (the receiver) through a VLAN-aware bridge (VLAN 20).

| Traffic Flow along the Shared Tree |     |
| ------------- | --- |
| {{< figure src = "/images/cumulus-linux/pim-config-example.png" >}} | <br><br><br><br>**1**. The FHR receives a multicast data packet from the source, encapsulates the packet in a unicast PIM register message, then sends it to the RP.<br><br>**2**. The RP builds an (S,G) mroute, decapsulates the multicast packet, then forwards it along the (*,G) tree towards the receiver.<br><br>**3**. The LHR receives multicast traffic and sees that it has a shorter path to the source. It requests the multicast stream from leaf01 and simultaneously sends the multicast stream to the receiver.|

| Traffic Flow for the Shortest Path Tree |     |
| ------------- | --- |
| {{< figure src = "/images/cumulus-linux/pim-config-example2.png" >}} | <br><br><br><br>**1**. The FHR hears a PIM join directly from the LHR and forwards multicast traffic directly to it.<br><br>**2**. The LHR receives the multicast packet both from the FHR and the RP. The LHR discards the packet from the RP and prunes itself from the RP.<br><br>**3**. The RP receives a prune message from the LHR and instructs the FHR to stop sending PIM register messages<br><br>**4**. Traffic continues directly between the FHR and the LHR. |

<!-- vale off -->
{{< tabs "TabID1395 ">}}
{{< tab "NVUE Commands">}}

{{< tabs "TabID1468 ">}}
{{< tab "leaf01 ">}}

```
cumulus@leaf01:~$ nv set router pim enable on
cumulus@leaf01:~$ nv set interface lo ip address 10.10.10.1/32
cumulus@leaf01:~$ nv set interface swp1,swp49,swp51
cumulus@leaf01:~$ nv set interface swp1 bridge domain br_default
cumulus@leaf01:~$ nv set interface swp1 bridge domain br_default access 10
cumulus@leaf01:~$ nv set bridge domain br_default vlan 10
cumulus@leaf01:~$ nv set interface vlan10 ip address 10.1.10.1/24
cumulus@leaf01:~$ nv set router bgp autonomous-system 65101
cumulus@leaf01:~$ nv set router bgp router-id 10.10.10.1
cumulus@leaf01:~$ nv set vrf default router bgp neighbor swp51 remote-as external
cumulus@leaf01:~$ nv set vrf default router bgp address-family ipv4-unicast network 10.10.10.1/32
cumulus@leaf01:~$ nv set vrf default router bgp address-family ipv4-unicast network 10.1.10.0/24
cumulus@leaf01:~$ nv set interface lo router pim
cumulus@leaf01:~$ nv set interface swp51 router pim
cumulus@leaf01:~$ nv set interface vlan10 router pim
cumulus@leaf01:~$ nv set interface vlan10 ip igmp
cumulus@leaf01:~$ nv set vrf default router pim address-family ipv4-unicast rp 10.10.10.101
cumulus@leaf01:~$ nv config apply
```

{{< /tab >}}
{{< tab "leaf02 ">}}

```
cumulus@leaf02:~$ nv set router pim enable on
cumulus@leaf02:~$ nv set interface lo ip address 10.10.10.2/32
cumulus@leaf02:~$ nv set interface swp2,swp49,swp51
cumulus@leaf02:~$ nv set interface swp2 bridge domain br_default
cumulus@leaf02:~$ nv set interface swp2 bridge domain br_default access 20
cumulus@leaf02:~$ nv set bridge domain br_default vlan 20
cumulus@leaf02:~$ nv set interface vlan20 ip address 10.2.10.1/24
cumulus@leaf02:~$ nv set router bgp autonomous-system 65102
cumulus@leaf02:~$ nv set router bgp router-id 10.10.10.2
cumulus@leaf02:~$ nv set vrf default router bgp neighbor swp51 remote-as external
cumulus@leaf02:~$ nv set vrf default router bgp address-family ipv4-unicast network 10.10.10.2/32
cumulus@leaf02:~$ nv set vrf default router bgp address-family ipv4-unicast network 10.2.10.0/24
cumulus@leaf02:~$ nv set interface lo router pim
cumulus@leaf02:~$ nv set interface swp51 router pim
cumulus@leaf02:~$ nv set interface vlan20 router pim
cumulus@leaf02:~$ nv set interface vlan20 ip igmp
cumulus@leaf02:~$ nv set vrf default router pim address-family ipv4-unicast rp 10.10.10.101
cumulus@leaf02:~$ nv config apply
```

{{< /tab >}}
{{< tab "spine01 ">}}

```
cumulus@spine01:~$ nv set router pim enable on
cumulus@spine01:~$ nv set interface lo ip address 10.10.10.101/32
cumulus@spine01:~$ nv set router bgp autonomous-system 65199
cumulus@spine01:~$ nv set router bgp router-id 10.10.10.101
cumulus@spine01:~$ nv set vrf default router bgp neighbor swp1 remote-as external
cumulus@spine01:~$ nv set vrf default router bgp neighbor swp2 remote-as external
cumulus@spine01:~$ nv set vrf default router bgp address-family ipv4-unicast network 10.10.10.101/32
cumulus@spine01:~$ nv set interface lo router pim
cumulus@spine01:~$ nv set interface swp1 router pim
cumulus@spine01:~$ nv set interface swp2 router pim
cumulus@spine01:~$ nv set vrf default router pim address-family ipv4-unicast rp 10.10.10.101 
cumulus@spine01:~$ nv config apply
```

{{< /tab >}}
{{< /tabs >}}

{{< /tab >}}
{{< tab "/etc/nvue.d/startup.yaml ">}}

{{< tabs "TabID1455 ">}}
{{< tab "leaf01 ">}}

```
cumulus@leaf01:mgmt:~$ sudo cat /etc/nvue.d/startup.yaml
- set:
    bridge:
      domain:
        br_default:
          vlan:
            '10': {}
    interface:
      lo:
        ip:
          address:
            10.10.10.1/32: {}
        router:
          pim:
            enable: on
        type: loopback
      swp1:
        bridge:
          domain:
            br_default: {}
        type: swp
      swp49:
        type: swp
      swp51:
        router:
          pim:
            enable: on
        type: swp
      vlan10:
        ip:
          address:
            10.1.10.1/24: {}
          igmp:
            enable: on
        router:
          pim:
            enable: on
        type: svi
        vlan: 10
    router:
      bgp:
        autonomous-system: 65101
        enable: on
        router-id: 10.10.10.1
      pim:
        enable: on
    system:
      hostname: leaf01
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
          pim:
            address-family:
              ipv4-unicast:
                rp:
                  10.10.10.101: {}
            enable: on
```

{{< /tab >}}
{{< tab "leaf02 ">}}

```
cumulus@leaf02:mgmt:~$ sudo cat /etc/nvue.d/startup.yaml
- set:
    bridge:
      domain:
        br_default:
          vlan:
            '20': {}
    interface:
      lo:
        ip:
          address:
            10.10.10.2/32: {}
        router:
          pim:
            enable: on
        type: loopback
      swp2:
        bridge:
          domain:
            br_default: {}
        type: swp
      swp49:
        type: swp
      swp51:
        router:
          pim:
            enable: on
        type: swp
      vlan20:
        ip:
          address:
            10.2.10.1/24: {}
          igmp:
            enable: on
        router:
          pim:
            enable: on
        type: svi
        vlan: 20
    router:
      bgp:
        autonomous-system: 65102
        enable: on
        router-id: 10.10.10.2
      pim:
        enable: on
    system:
      hostname: leaf02
    vrf:
      default:
        router:
          bgp:
            address-family:
              ipv4-unicast:
                enable: on
                network:
                  10.2.10.0/24: {}
                  10.10.10.2/32: {}
            enable: on
            neighbor:
              swp51:
                remote-as: external
                type: unnumbered
          pim:
            address-family:
              ipv4-unicast:
                rp:
                  10.10.10.101: {}
            enable: on
```

{{< /tab >}}
{{< tab "spine01 ">}}

```
cumulus@spine01:mgmt:~$ sudo cat /etc/nvue.d/startup.yaml
- set:
    interface:
      lo:
        ip:
          address:
            10.10.10.101/32: {}
        router:
          pim:
            enable: on
        type: loopback
      swp1:
        router:
          pim:
            enable: on
        type: swp
      swp2:
        router:
          pim:
            enable: on
        type: swp
    router:
      bgp:
        autonomous-system: 65199
        enable: on
        router-id: 10.10.10.101
      pim:
        enable: on
    system:
      hostname: spine01
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
              swp2:
                remote-as: external
                type: unnumbered
          pim:
            address-family:
              ipv4-unicast:
                rp:
                  10.10.10.101: {}
            enable: on
```

{{< /tab >}}
{{< /tabs >}}

{{< /tab >}}
{{< tab "/etc/network/interfaces ">}}

{{< tabs "TabID1458 ">}}
{{< tab "leaf01 ">}}

```
cumulus@leaf01:mgmt:~$ sudo cat /etc/network/interfaces
...
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
    bridge-access 10
auto swp49
iface swp49
auto swp51
iface swp51
auto vlan10
iface vlan10
    address 10.1.10.1/24
    hwaddress 44:38:39:22:01:b1
    vlan-raw-device br_default
    vlan-id 10
auto br_default
iface br_default
    bridge-ports swp1
    hwaddress 44:38:39:22:01:b1
    bridge-vlan-aware yes
    bridge-vids 10
    bridge-pvid 1
```

{{< /tab >}}
{{< tab "leaf02 ">}}

```
cumulus@leaf02:mgmt:~$ sudo cat /etc/network/interfaces
...
auto lo
iface lo inet loopback
    address 10.10.10.2/32
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
auto swp2
iface swp2
    bridge-access 20
auto swp49
iface swp49
auto swp51
iface swp51
auto vlan20
iface vlan20
    address 10.2.10.1/24
    hwaddress 44:38:39:22:01:af
    vlan-raw-device br_default
    vlan-id 20
auto br_default
iface br_default
    bridge-ports swp2
    hwaddress 44:38:39:22:01:af
    bridge-vlan-aware yes
    bridge-vids 20
    bridge-pvid 1
```

{{< /tab >}}
{{< tab "spine01 ">}}

```
cumulus@spine01:mgmt:~$ sudo cat /etc/network/interfaces
...
auto lo
iface lo inet loopback
    address 10.10.10.101/32
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
auto swp2
iface swp2
```

{{< /tab >}}
{{< tab "server01 ">}}

```
cumulus@server01:~$ sudo cat /etc/network/interfaces
# The loopback network interface
auto lo
iface lo inet loopback
# The OOB network interface
auto eth0
iface eth0 inet dhcp
# The data plane network interfaces
auto eth1
iface eth1 inet manual
  address 10.1.10.101
  netmask 255.255.255.0
  mtu 9000
  post-up ip route add 10.0.0.0/8 via 10.1.10.1
```

{{< /tab >}}
{{< tab "server02 ">}}

```
cumulus@server02:~$ sudo cat /etc/network/interfaces
auto lo
iface lo inet loopback
# The OOB network interface
auto eth0
iface eth0 inet dhcp
# The data plane network interfaces
auto eth2
iface eth2 inet manual
  address 10.2.10.102
  netmask 255.255.255.0
  mtu 9000
  post-up ip route add 10.0.0.0/8 via 10.2.10.1
```

{{< /tab >}}
{{< /tabs >}}

{{< /tab >}}
{{< tab "/etc/frr/frr.conf ">}}

{{< tabs "TabID1608 ">}}
{{< tab "leaf01 ">}}

```
cumulus@leaf01:mgmt:~$ sudo cat /etc/frr/frr.conf
...
interface lo
ip pim
interface swp51
ip pim
interface vlan10
ip igmp
ip igmp version 3
ip igmp query-interval 125
ip igmp last-member-query-interval 10
ip igmp query-max-response-time 100
ip pim
vrf default
ip pim rp 10.10.10.101 224.0.0.0/4
exit-vrf
vrf mgmt
exit-vrf
router bgp 65101 vrf default
bgp router-id 10.10.10.1
timers bgp 3 9
bgp deterministic-med
! Neighbors
neighbor swp51 interface remote-as external
neighbor swp51 timers 3 9
neighbor swp51 timers connect 10
neighbor swp51 advertisement-interval 0
neighbor swp51 capability extended-nexthop
! Address families
address-family ipv4 unicast
network 10.1.10.0/24
network 10.10.10.1/32
maximum-paths ibgp 64
maximum-paths 64
distance bgp 20 200 200
neighbor swp51 activate
exit-address-family
```

{{< /tab >}}
{{< tab "leaf02 ">}}

```
cumulus@leaf02:mgmt:~$ sudo cat /etc/frr/frr.conf
...
interface lo
ip pim
interface swp51
ip pim
interface vlan20
ip igmp
ip igmp version 3
ip igmp query-interval 125
ip igmp last-member-query-interval 10
ip igmp query-max-response-time 100
ip pim
vrf default
ip pim rp 10.10.10.101 224.0.0.0/4
exit-vrf
vrf mgmt
exit-vrf
router bgp 65102 vrf default
bgp router-id 10.10.10.2
timers bgp 3 9
bgp deterministic-med
! Neighbors
neighbor swp51 interface remote-as external
neighbor swp51 timers 3 9
neighbor swp51 timers connect 10
neighbor swp51 advertisement-interval 0
neighbor swp51 capability extended-nexthop
! Address families
address-family ipv4 unicast
network 10.10.10.2/32
network 10.2.10.0/24
maximum-paths ibgp 64
maximum-paths 64
distance bgp 20 200 200
neighbor swp51 activate
exit-address-family
```

{{< /tab >}}
{{< tab "spine01 ">}}

```
cumulus@spine01:mgmt:~$ sudo cat /etc/frr/frr.conf
...
interface lo
ip pim
interface swp1
ip pim
interface swp2
ip pim
vrf default
ip pim rp 10.10.10.101 224.0.0.0/4
exit-vrf
vrf mgmt
exit-vrf
router bgp 65199 vrf default
bgp router-id 10.10.10.101
timers bgp 3 9
bgp deterministic-med
! Neighbors
neighbor swp1 interface remote-as external
neighbor swp1 timers 3 9
neighbor swp1 timers connect 10
neighbor swp1 advertisement-interval 0
neighbor swp1 capability extended-nexthop
neighbor swp2 interface remote-as external
neighbor swp2 timers 3 9
neighbor swp2 timers connect 10
neighbor swp2 advertisement-interval 0
neighbor swp2 capability extended-nexthop
! Address families
address-family ipv4 unicast
network 10.10.10.101/32
maximum-paths ibgp 64
maximum-paths 64
distance bgp 20 200 200
neighbor swp1 activate
neighbor swp2 activate
exit-address-family
```

{{< /tab >}}
{{< /tabs >}}

{{< /tab >}}
{{< tab "Try It " >}}
    {{< simulation name="Try It CL56 - PIM" showNodes="leaf01,leaf02,spine01,server01,server02" >}}

This simulation starts with the example PIM configuration. To simplify the example, only one spine and two leafs are in the topology. The demo is pre-configured using NVUE commands.

- To show the multicast routing table, run the NCLU `net show mroute` command on the FHR (leaf01), RP (spine01), or LHR (leaf02).
- To see the active source on the RP, run the `net show pim upstream` command on spine01.
- To show information about known S,Gs, the <span class="a-tooltip">[IIF](## "Incoming Interface")</span> and the <span class="a-tooltip">[OIL](## "Outgoing Interface")</span>, run the `net show pim state` command on the FHR (leaf01), RP (spine01), or LHR (leaf02).

To further validate the configuration, run the PIM show commands listed in the troubleshooting section above.

{{< /tab >}}
{{< /tabs >}}
<!-- vale on -->

## Considerations

- Cumulus Linux does not support non-native forwarding (register decapsulation). Expect initial packet loss while the PIM \*,G tree is building from the RP to the FHR to trigger native forwarding.
- Cumulus Linux does not build an S,G mroute when forwarding over an \*,G tree.
