---
title: Optional BGP Configuration
author: NVIDIA
weight: 860
toc: 3
---
This section describes optional configuration. The steps provided in this section assume that you already configured basic BGP as described in {{<link url="Basic-BGP-Configuration" >}}.

## Peer Groups

Instead of specifying properties of each individual peer, you can define one or more peer groups and associate all the attributes common to that peer session to a peer group. You need to attach a peer to a peer group one time; it then inherits all address families activated for that peer group.

{{%notice note%}}
- If the peer you want to add to a group already exists in the BGP configuration, delete it first, than add it to the peer group.
- Configuring a peer group results in BGP session flaps, which might lead to traffic loss.
- When you delete a peer group associated with a BGP neighbor, Cumulus Linux also removes the corresponding neighbor configuration.
{{%/notice%}}

The following example commands create a peer group called SPINE that includes two external peers.

{{< tabs "19 ">}}
{{< tab "NVUE Commands ">}}

```
cumulus@leaf01:~$ nv set vrf default router bgp peer-group SPINE
cumulus@leaf01:~$ nv set vrf default router bgp peer-group SPINE remote-as external
cumulus@leaf01:~$ nv set vrf default router bgp neighbor 10.0.1.0 peer-group SPINE
cumulus@leaf01:~$ nv set vrf default router bgp neighbor 10.0.1.12 peer-group SPINE
cumulus@leaf01:~$ nv config apply
```

{{< /tab >}}
{{< tab "vtysh Commands ">}}

```
cumulus@leaf01:~$ sudo vtysh
leaf01# configure terminal
leaf01(config)# router bgp 65101
leaf01(config-router)# neighbor SPINE peer-group
leaf01(config-router)# neighbor SPINE remote-as external
leaf01(config-router)# neighbor 10.0.1.0 peer-group SPINE
leaf01(config-router)# neighbor 10.0.1.12 peer-group SPINE
leaf01(config-router)# end
leaf01# write memory
leaf01# exit
cumulus@leaf01:~$
```

{{< /tab >}}
{{< /tabs >}}

For an unnumbered configuration, you can use a single command to configure a neighbor and attach it to a peer group.

{{< tabs "52 ">}}
{{< tab "NVUE Commands ">}}

```
cumulus@leaf01:~$ nv set vrf default router bgp neighbor swp51 peer-group SPINE
```

{{< /tab >}}
{{< tab "vtysh Commands ">}}

```
leaf01(config-router)# neighbor swp51 interface peer-group SPINE
```

{{< /tab >}}
{{< /tabs >}}
<!-- vale off -->
{{%notice note%}}
If you unset a peer group, make sure that it is not applied to any neighbors. If the peer group is applied to neighbors, configure all parameters, such as the remote AS, directly on the neighbors before removing the peer group.
{{%/notice%}}
<!-- vale on -->

## IPv6-only Unnumbered Peering

To configure a BGP unnumbered peer for IPv6-only peering over a link-local address, you must configure an NVUE snippet. When you configure an NVUE snippet for a `v6only` peering, the `remote-as` and any `peer-group` configuration must be applied with the snippet instead of NVUE CLI commands. If a peer group is configured for the neighbor, the remote-as can be defined in the peer group configuration through NVUE commands.

The following example configures the BGP peer group CLIENT1 with soft reconfiguration and community advertisement enabled, and the remote AS set to external. The snippet configuration configures the `v6only` option and applies the peer group to the neighbor: 

```
cumulus@leaf01:~$ nv set vrf default router bgp peer-group CLIENT1 address-family ipv4-unicast community-advertise
cumulus@leaf01:~$ nv set vrf default router bgp peer-group CLIENT1 address-family ipv4-unicast soft-reconfiguration enabled
cumulus@leaf01:~$ nv set vrf default router bgp peer-group CLIENT1 remote-as external
cumulus@leaf01:~$ nv config apply
```

Create a .yaml file with the following content:

```
- set:
    system:
      config:
        snippet:
          frr.conf: |
            router bgp 65101
            neighbor swp1 interface v6only peer-group CLIENT1
```

Patch and apply the snippet:

```
cumulus@leaf01:~$ nv config patch bgp_snippet.yaml
cumulus@leaf01:~$ nv config apply
```

The following example configures a `v6only` peering with no peer group applied:

Create a .yaml file with the following content:

```
- set:
    system:
      config:
        snippet:
          frr.conf: |
            router bgp 65101
            neighbor swp1 interface v6only remote-as external
```

Patch and apply the snippet:

```
cumulus@leaf01:~$ nv config patch bgp_snippet.yaml
cumulus@leaf01:~$ nv config apply
```
## BGP Dynamic Neighbors

*BGP dynamic neighbors* provides BGP peering to remote neighbors within a specified range of IPv4 or IPv6 addresses for a BGP peer group. You can configure each range as a subnet IP address.

After you configure the dynamic neighbors, a BGP speaker can listen for, and form peer relationships with, any neighbor that is in the IP address range and maps to a peer group. You can also limit the number of dynamic peers. The default value is 100.

The following example commands configure BGP peering to remote neighbors within the address range 10.0.1.0/24 for the peer group SPINE and limit the number of dynamic peers to 5.

{{%notice note%}}
The peer group must already exist otherwise the configuration does not apply.
{{%/notice%}}

{{< tabs "85 ">}}
{{< tab "NVUE Commands ">}}

```
cumulus@leaf01:~$ nv set vrf default router bgp dynamic-neighbor listen-range 10.0.1.0/24 peer-group SPINE
cumulus@leaf01:~$ nv set vrf default router bgp dynamic-neighbor limit 5
cumulus@leaf01:~$ nv config apply
```

{{< /tab >}}
{{< tab "vtysh Commands ">}}

```
cumulus@leaf01:~$ sudo vtysh
leaf01# configure terminal
leaf01(config)# router bgp 65101
leaf01(config-router)# bgp listen range 10.0.1.0/24 peer-group SPINE
leaf01(config-router)# bgp listen limit 5
leaf01(config-router)# end
leaf01# write memory
leaf01# exit
cumulus@leaf01:~$
```

The vtysh commands save the configuration in the `/etc/frr/frr.conf` file. For example:

```
router bgp 65101
  neighbor SPINE peer-group
  neighbor SPINE remote-as external
  bgp listen limit 5
  bgp listen range 10.0.1.0/24 peer-group SPINE
```

{{< /tab >}}
{{< /tabs >}}

## eBGP Multihop

The eBGP multihop option lets you use BGP to exchange routes with an external peer that is more than one hop away.

{{%notice note%}}
Changing eBGP multihop configuration results in BGP session flaps, which might lead to traffic loss.
{{%/notice%}}

The following example command configures Cumulus Linux to establish a connection between two <span class="a-tooltip">[eBGP](## "external BGP")</span> peers that are not directly connected and sets the maximum number of hops used to reach a eBGP peer to 1.

{{< tabs "128 ">}}
{{< tab "NVUE Commands ">}}

```
cumulus@leaf01:~$ nv set vrf default router bgp neighbor 10.10.10.101 remote-as external
cumulus@leaf01:~$ nv set vrf default router bgp neighbor 10.10.10.101 multihop-ttl 1
cumulus@leaf01:~$ nv config apply
```

{{< /tab >}}
{{< tab "vtysh Commands ">}}

```
cumulus@leaf01:~$ sudo vtysh
...
leaf01# configure terminal
leaf01(config)# router bgp 65101
leaf01(config-router)# neighbor 10.10.10.101 remote-as external
leaf01(config-router)# neighbor 10.10.10.101 ebgp-multihop
leaf01(config-router)# end
leaf01# write memory
leaf01# exit
```

{{< /tab >}}
{{< /tabs >}}

## BGP TTL Security Hop Count

You can use the TTL security hop count option to prevent attacks against eBGP, such as denial of service (DoS) attacks.
By default, BGP messages to eBGP neighbors have an IP time-to-live (TTL) of 1, which requires the peer to be directly connected, otherwise, the packets expire along the way. You can adjust the TTL with the {{<link url="#ebgp-multihop" text="eBGP multihop">}} option. An attacker can adjust the TTL of packets so that they look like they originate from a directly connected peer.

The BGP TTL security hops option inverts the direction in which BGP counts the TTL. Instead of accepting only packets with a TTL of 1, Cumulus Linux accepts BGP messages with a TTL greater than or equal to 255 minus the specified hop count.

When you use TTL security, you do not need eBGP multihop.

The following command example sets the TTL security hop count value to 200:

{{< tabs "166 ">}}
{{< tab "NVUE Commands ">}}

```
cumulus@leaf01:~$ nv set vrf default router bgp neighbor swp51 ttl-security hops 200
cumulus@leaf01:~$ nv config apply
```

{{< /tab >}}
{{< tab "vtysh Commands ">}}

```
cumulus@leaf01:~$ sudo vtysh
...
leaf01# configure terminal
leaf01(config)# router bgp 65101
leaf01(config-router)# neighbor swp51 ttl-security hops 200
leaf01(config-router)# end
leaf01# write memory
leaf01# exit
```

The vtysh commands save the configuration in the `/etc/frr/frr.conf` file. For example:

```
...
router bgp 65101
  ...
  neighbor swp51 ttl-security hops 200
...
```

{{%notice note%}}
- When you configure `ttl-security hops` on a peer group instead of a specific neighbor, FRR does not add it to either the running configuration or to the `/etc/frr/frr.conf` file. To work around this issue, add `ttl-security hops` to individual neighbors instead of the peer group.
- Enabling `ttl-security hops` does not program the hardware with relevant information. Cumulus Linux forwards frames to the CPU and then drops them. Use the NVUE Command to explicitly add the relevant entry to hardware. For more information about ACLs, see {{<link title="Access Control Lists">}}.
{{%/notice%}}

{{< /tab >}}
{{< /tabs >}}

<!-- vale off -->
## MD5-enabled BGP Neighbors
<!-- vale on -->
You can authenticate your BGP peer connection to prevent interference with your routing tables.

To enable MD5 authentication for BGP peers, set the same password on each peer.

{{%notice note%}}
Changing the password results in BGP session flaps, which might lead to traffic loss.
{{%/notice%}}

The following example commands set the password *mypassword* on BGP peers leaf01 and spine01:

{{< tabs "215 ">}}
{{< tab "NVUE Commands ">}}

{{< tabs "218 ">}}
{{< tab "leaf01 ">}}

```
cumulus@leaf01:~$ nv set vrf default router bgp neighbor swp51 password mypassword
cumulus@leaf01:~$ nv config apply
```

{{< /tab >}}
{{< tab "spine01 ">}}

```
cumulus@spine01:~$ nv set vrf default router bgp neighbor swp1 password mypassword
cumulus@spine01:~$ nv config apply
```

{{< /tab >}}
{{< /tabs >}}

{{< /tab >}}
{{< tab "vtysh Commands ">}}

{{< tabs "240 ">}}
{{< tab "leaf01 ">}}

```
cumulus@leaf01:~$ sudo vtysh
...
leaf01# configure terminal
leaf01(config)# router bgp 65101
leaf01(config-router)# neighbor swp51 password mypassword
leaf01(config-router)# end
leaf01# write memory
leaf01# exit
```

{{< /tab >}}
{{< tab "spine01 ">}}

```
cumulus@spine01:~$ sudo vtysh
...
spine01# configure terminal
spine01(config)# router bgp 65199
spine01(config-router)# neighbor swp1 password mypassword
spine01(config-router)# end
spine01# write memory
spine01# exit
```

{{< /tab >}}
{{< /tabs >}}

{{< /tab >}}
{{< /tabs >}}

You can confirm the configuration with the  NVUE `nv show vrf default router bgp neighbor <neighbor>` command or the vtysh `show ip bgp neighbor <neighbor>` command.

<!-- vale off -->
{{< expand "example" >}}

The following example shows that Cumulus Linux establishes a session with the peer. The output shows `Peer Authentication Enabled` towards the end.

```
cumulus@spine01:~$ sudo vtysh
...
spine01# show ip bgp neighbor swp1
BGP neighbor on swp1: fe80::2294:15ff:fe02:7bbf, remote AS 65101, local AS 65199, external link
Hostname: leaf01
  BGP version 4, remote router ID 10.10.10.1, local router ID 10.10.10.101
  BGP state = Established, up for 00:00:39
  Last read 00:00:00, Last write 00:00:00
  Hold time is 9, keepalive interval is 3 seconds
  Neighbor capabilities:
    4 Byte AS: advertised and received
    AddPath:
      IPv4 Unicast: RX advertised IPv4 Unicast and received
    Route refresh: advertised and received(old & new)
    Address Family IPv4 Unicast: advertised and received
    Hostname Capability: advertised (name: spine01,domain name: n/a) received (name: leaf01,domain name: n/a)
    Graceful Restart Capability: advertised and received
      Remote Restart timer is 120 seconds
      Address families by peer:
        none
  Graceful restart information:
    End-of-RIB send: IPv4 Unicast
    End-of-RIB received: IPv4 Unicast
  Message statistics:
    Inq depth is 0
    Outq depth is 0
                         Sent       Rcvd
    Opens:                  2          2
    Notifications:          0          2
    Updates:              424        369
    Keepalives:           633        633
    Route Refresh:          0          0
    Capability:             0          0
    Total:               1059       1006
  Minimum time between advertisement runs is 0 seconds
  For address family: IPv4 Unicast
  Update group 1, subgroup 1
  Packet Queue length 0
  Community attribute sent to this neighbor(all)
  3 accepted prefixes
  Connections established 2; dropped 1
  Last reset 00:02:37,   Notification received (Cease/Other Configuration Change)
Local host: fe80::7c41:fff:fe93:b711, Local port: 45586
Foreign host: fe80::2294:15ff:fe02:7bbf, Foreign port: 179
Nexthop: 10.10.10.101
Nexthop global: fe80::7c41:fff:fe93:b711
Nexthop local: fe80::7c41:fff:fe93:b711
BGP connection: shared network
BGP Connect Retry Timer in Seconds: 10
Peer Authentication Enabled
Read thread: on  Write thread: on  FD used: 27
```

{{< /expand >}}

{{%notice note%}}
Cumulus Linux does not enforce the MD5 password configured against a BGP listen-range peer group (used to accept and create dynamic BGP neighbors) and accepts connections from peers that do not specify a password.
{{%/notice%}}
<!-- asked not to document in 5.6
### Password Obfuscation

By default, when you set MD5 authentication for BGP peers, Cumulus Linux shows the passwords in clear text in the NVUE `nv config show` command output, vtysh `show running-config output`, and in the `/etc/frr/frr.conf` file. To configure BGP to obfuscate the passwords instead of showing them in clear text:

{{< tabs "340 ">}}
{{< tab "NVUE Commands ">}}

To enable password obfuscation (show encrypted passwords):

```
cumulus@leaf01:~$ nv set router password-obfuscation enabled
cumulus@leaf01:~$ nv config apply
```

To disable password obfuscation (show clear text passwords):

```
cumulus@leaf01:~$ nv set router password-obfuscation disabled
cumulus@leaf01:~$ nv config apply
```

{{< /tab >}}
{{< tab "vtysh Commands ">}}

To enable password obfuscation (show encrypted passwords):

```
cumulus@switch:~$ sudo vtysh
...
switch# configure terminal
switch(config)# service password-obfuscation
switch(config)# end
switch# write memory
switch# exit
```

To disable password obfuscation (show clear text passwords):

```
cumulus@switch:~$ sudo vtysh
...
switch# configure terminal
switch(config)# no service password-obfuscation
switch(config)# end
switch# write memory
switch# exit
```

{{< /tab >}}
{{< /tabs >}}
-->
## Remove Private BGP ASNs

If you use private ASNs in the data center, routes advertised to neighbors contain your private ASNs. The examples below show how to remove the private ASNs from routes and how to replace the private ASNs with your public ASN.

The following example command removes private ASNs from routes advertised to the neighbor on swp51 (an unnumbered interface):

{{< tabs "398 ">}}
{{< tab "NVUE Commands ">}}

```
cumulus@leaf01:~$ nv set vrf default router bgp neighbor swp51 address-family ipv4-unicast aspath private-as remove
cumulus@leaf01:~$ nv config apply
```

You can replace the private ASNs with your public ASN with the following command:

```
cumulus@leaf01:~$ nv set vrf default router bgp neighbor swp51 address-family ipv4-unicast aspath replace-peer-as on
cumulus@leaf01:~$ nv config apply
```

To unset the above configuration:

```
cumulus@leaf01:~$ nv unset vrf default router bgp neighbor swp51 address-family ipv4-unicast aspath private-as remove
cumulus@leaf01:~$ nv config apply
```

```
cumulus@leaf01:~$ nv unset vrf default router bgp neighbor swp51 address-family ipv4-unicast aspath replace-peer-as on
cumulus@leaf01:~$ nv config apply
```

{{< /tab >}}
{{< tab "Linux Commands ">}}

Add the line `neighbor swp51 remove-private-AS` to the address-family ipv4 unicast stanza:

```
cumulus@leaf01:~$ sudo nano /etc/frr/frr.conf
...
router bgp 65101
 bgp router-id 10.10.10.1
 neighbor underlay peer-group
 neighbor underlay remote-as external
 neighbor swp51 interface peer-group underlay
 neighbor swp52 interface peer-group underlay
 neighbor swp53 interface peer-group underlay
 neighbor swp54 interface peer-group underlay
 !
 address-family ipv4 unicast
  redistribute connected
  neighbor swp51 remove-private-AS
 exit-address-family
 !
...
```

{{< /tab >}}
{{< /tabs >}}

## Multiple BGP ASNs

Cumulus Linux supports the use of distinct ASNs for different VRF instances.

The following example configures VRF RED and VRF BLUE on border01 to use ASN 65532 towards fw1 and 65533 towards fw2:

{{< img src = "/images/cumulus-linux/asn-vrf-config.png" >}}

{{< tabs "461 ">}}
{{< tab "NVUE Commands ">}}

```
cumulus@border01:~$ nv set vrf RED router bgp autonomous-system 65532        
cumulus@border01:~$ nv set vrf RED router bgp router-id 10.10.10.63
cumulus@border01:~$ nv set vrf RED router bgp neighbor swp3 remote-as external
cumulus@border01:~$ nv set vrf BLUE router bgp autonomous-system 65533 
cumulus@border01:~$ nv set vrf BLUE router bgp router-id 10.10.10.63
cumulus@border01:~$ nv set vrf BLUE router bgp neighbor swp4 remote-as external
cumulus@border01:~$ nv config apply
```

{{< /tab >}}
{{< tab "vtysh Commands ">}}

```
cumulus@border01:~$ sudo vtysh
...
border01# configure terminal
border01(config)# router bgp 65532 vrf RED
border01(config-router)# bgp router-id 10.10.10.63
border01(config-router)# neighbor swp3 interface remote-as external
border01(config-router)# exit
border01(config)# router bgp 65533 vrf BLUE
border01(config-router)# bgp router-id 10.10.10.63
border01(config-router)# neighbor swp4 interface remote-as external
border01(config-router)# end
border01# write memory
border01# exit
```

The vtysh commands save the configuration in the `/etc/frr/frr.conf` file:

```
cumulus@border01:~$ cat /etc/frr/frr.conf
...
log syslog informational
!
vrf RED
  vni 4001
vrf BLUE
  vni 4002
!
router bgp 65132
 bgp router-id 10.10.10.63
 bgp bestpath as-path multipath-relax
 neighbor underlay peer-group
 neighbor underlay remote-as external
 neighbor peerlink.4094 interface remote-as internal
 neighbor swp51 interface peer-group underlay
 neighbor swp52 interface peer-group underlay
 !
 address-family ipv4 unicast
  redistribute connected
 exit-address-family
 !
 address-family l2vpn evpn
  neighbor underlay activate
  advertise-all-vni
 exit-address-family
!
router bgp 65532 vrf RED
 bgp router-id 10.10.10.63
 neighbor swp3 remote-as external
 !
 address-family ipv4 unicast
  redistribute static
 exit-address-family
 !
 address-family l2vpn evpn
  neighbor underlay activate
  advertise-all-vni
 exit-address-family
!
router bgp 65533 vrf BLUE
 bgp router-id 10.10.10.63
 neighbor swp4 remote-as external
 !
 address-family ipv4 unicast
  redistribute static
 exit-address-family
 !
 address-family l2vpn evpn
  neighbor underlay activate
  advertise-all-vni
 exit-address-family
!
line vty
```

{{< /tab >}}
{{< /tabs >}}

With the above configuration, the vtysh `show ip bgp vrf RED summary` command output shows the local ASN as 65532.

```
cumulus@border01:mgmt:~$ sudo vtysh
...
border01# show ip bgp vrf RED summary
ipv4 unicast summary

BGP router identifier 10.10.10.63, local AS number 65532 vrf-id 35
BGP table version 1
RIB entries 1, using 192 bytes of memory
Peers 1, using 21 KiB of memory

Neighbor      V      AS   MsgRcvd   MsgSent   TblVer  InQ OutQ  Up/Down State/PfxRcd   PfxSnt
fw1(swp3)     4   65199      2015      2015        0    0    0 01:40:36            1        1

Total number of neighbors 1
...
```

The vtysh `show ip bgp summary` command displays the global table, where the local ASN 65132 peers with spine01.

```
cumulus@border01:mgmt:~$ sudo vtysh
...
leaf01# show ip bgp summary
ipv4 unicast summary

BGP router identifier 10.10.10.63, local AS number 65132 vrf-id 0
BGP table version 3
RIB entries 5, using 960 bytes of memory
Peers 1, using 43 KiB of memory
Peer groups 1, using 64 bytes of memory

Neighbor        V         AS   MsgRcvd   MsgSent   TblVer  InQ OutQ  Up/Down State/PfxRcd   PfxSnt
spine01(swp51)  4      65199      2223      2223        0    0    0 01:50:18            1        3

Total number of neighbors 1
...
```

## BGP allowas-in

To prevent loops, the switch automatically discards BGP network prefixes if it sees its own ASN in the AS path. However, you can configure Cumulus Linux to receive and process routes even if it detects its own ASN in the AS path (allowas-in).

To enable allowas-in:

{{< tabs "602 ">}}
{{< tab "NVUE Commands ">}}

```
cumulus@switch:~$ nv set vrf default router bgp neighbor swp51 address-family ipv4-unicast aspath allow-my-asn state enabled
cumulus@switch:~$ nv config apply
```

To disable allowas-in:

```
cumulus@switch:~$ nv set vrf default router bgp neighbor swp51 address-family ipv4-unicast aspath allow-my-asn state disabled
cumulus@switch:~$ nv config apply
```

{{< /tab >}}
{{< tab "vtysh Commands ">}}

```
cumulus@switch:~$ sudo vtysh
...
switch# configure terminal
switch(config)# router bgp 65101
switch(config-router)# address-family ipv4 unicast
switch(config-router-af)# neighbor swp51 allowas-in
switch(config-router-af)# end
switch# write memory
switch# exit
```

The vtysh commands save the configuration in the `address-family` stanza of the `/etc/frr/frr.conf` file. For example:

```
...
address-family ipv4 unicast
  network 10.10.10.1/32
  redistribute connected
  neighbor swp51 allowas-in
...
```

{{< /tab >}}
{{< /tabs >}}

You can configure additional options:
- You can set the maximum number of occurrences of the local system's AS number in the received AS path
- You can allow a received AS path containing the ASN of the local system but only if it is the originating AS

The following example sets the maximum number of occurrences of the local system's AS number in the received AS path to 4:

{{< tabs "652 ">}}
{{< tab "NVUE Commands ">}}

```
cumulus@switch:~$ nv set vrf default router bgp neighbor swp51 address-family ipv4-unicast aspath allow-my-asn occurrences 4
cumulus@switch:~$ nv config apply
```

To unset the above configuration, run the `nv unset` command:

```
cumulus@switch:~$ nv unset vrf default router bgp neighbor swp51 address-family ipv4-unicast aspath allow-my-asn occurrences 4
cumulus@switch:~$ nv config apply
```

{{< /tab >}}
{{< tab "vtysh Commands ">}}

```
cumulus@switch:~$ sudo vtysh
...
switch# configure terminal
switch(config)# router bgp 65101
switch(config-router)# address-family ipv4 unicast
switch(config-router-af)# neighbor swp51 allowas-in 4
switch(config-router-af)# end
switch# write memory
switch# exit
```

The vtysh commands save the configuration in the `address-family` stanza of the `/etc/frr/frr.conf` file. For example:

```
...
address-family ipv4 unicast
  network 10.10.10.1/32
  redistribute connected
  neighbor swp51 allowas-in 4
...
```

{{< /tab >}}
{{< /tabs >}}

The following example allows a received AS path containing the ASN of the local system but only if it is the originating AS:  

{{< tabs "698 ">}}
{{< tab "NVUE Commands ">}}

```
cumulus@switch:~$ nv set vrf default router bgp neighbor swp51 address-family ipv4-unicast aspath allow-my-asn origin enabled
cumulus@switch:~$ nv config apply
```

To unset the above configuration, run the `nv unset` command:

```
cumulus@switch:~$ nv unset vrf default router bgp neighbor swp51 address-family ipv4-unicast aspath allow-my-asn origin on
cumulus@switch:~$ nv config apply
```

{{< /tab >}}
{{< tab "vtysh Commands ">}}

```
cumulus@switch:~$ sudo vtysh
...
switch# configure terminal
switch(config)# router bgp 65101
switch(config-router)# address-family ipv4 unicast
switch(config-router-af)# neighbor swp51 allowas-in origin
switch(config-router-af)# end
switch# write memory
switch# exit
```

The vtysh commands save the configuration in the `address-family` stanza of the `/etc/frr/frr.conf` file. For example:

```
...
address-family ipv4 unicast
  network 10.10.10.1/32
  redistribute connected
  neighbor swp51 allowas-in origin
...
```

{{< /tab >}}
{{< /tabs >}}

## Enforce First AS

By default, the switch denies an update received from an eBGP neighbor that does not list its ASN at the beginning of the AS_PATH in the incoming update. You can disable this setting with the `nv set vrf <vrf-id> router bgp neighbor <neighbor> enforce-first-as off` command.

{{%notice note%}}
In Cumulus Linux 5.13 and earlier the default setting for enforce first AS is OFF.
{{%/notice%}}

{{< tabs "757 ">}}
{{< tab "NVUE Commands ">}}

```
cumulus@switch:~$ nv set vrf default router bgp neighbor swp51 enforce-first-as off
cumulus@switch:~$ nv config apply
```

To disable the enforce first AS setting for a peer group, run the `nv set vrf <vrf-id> router bgp peer-group <peer-group> enforce-first-as off` command.

```
cumulus@switch:~$ nv set vrf default router bgp peer-group underlay enforce-first-as off
cumulus@switch:~$ nv config apply
```

To reenable enforce first AS, run the `nv set vrf <vrf-id> router bgp neighbor <neighbor> enforce-first-as on` command or the `nv set vrf <vrf-id> router bgp peer-group <peer-group> enforce-first-as on` command.

{{< /tab >}}
{{< tab "vtysh Commands ">}}

To disable the enforce first AS setting for a neighbor or a peer group:

```
cumulus@switch:~$ sudo vtysh
...
switch# configure terminal
switch(config)# router bgp 65101
switch(config-router)# no neighbor swp51 enforce-first-as
switch(config-router-af)# end
switch# write memory
switch# exit
```

To reenable the enforce first AS setting for a neighbor or a peer group:

```
cumulus@switch:~$ sudo vtysh
...
switch# configure terminal
switch(config)# router bgp 65101
switch(config-router)# neighbor swp51 enforce-first-as
switch(config-router-af)# end
switch# write memory
switch# exit
```

{{< /tab >}}
{{< /tabs >}}

## Update Source

You can configure BGP to use a specific IP address when exchanging BGP updates with a neighbor. For example, in a numbered BGP configuration, you can set the source IP address to be the loopback address of the switch.

{{%notice note%}}
Update source configuration results in BGP session flaps, which might lead to traffic loss.
{{%/notice%}}

{{< tabs "746 ">}}
{{< tab "NVUE Commands ">}}

```
cumulus@leaf01:~$ nv set vrf default router bgp neighbor 10.10.10.10 update-source 10.10.10.1
cumulus@leaf01:~$ nv config apply
```

{{< /tab >}}
{{< tab "vtysh Commands ">}}

```
cumulus@leaf01:~$ sudo vtysh
...
leaf01# configure terminal
leaf01(config)# router bgp 65101
leaf01(config-router)# neighbor 10.10.10.10 update-source 10.10.10.1
leaf01(config-router-af)# end
leaf01# write memory
leaf01# exit
```

The vtysh commands save the configuration in the `/etc/frr/frr.conf` file. For example:

```
...
router bgp 65101
 bgp router-id 10.10.10.1
 neighbor 10.10.10.10 remote-as 65000
 neighbor 10.10.10.10 update-source 10.10.10.1
 ...
```

{{< /tab >}}
{{< /tabs >}}

## ECMP

BGP supports equal-cost multipathing ({{<link url="Equal-Cost-Multipath-Load-Sharing" text="ECMP">}}). If a BGP node hears a certain prefix from multiple peers, it has the information necessary to program the routing table and forward traffic for that prefix through all these peers. BGP typically chooses one best path for each prefix and installs that route in the forwarding table.

Cumulus Linux enables the *BGP multipath* option by default and sets the maximum number of paths to 64 so that the switch can install multiple equal-cost BGP paths to the forwarding table and load balance traffic across multiple links. You can change the number of paths allowed, according to your needs.

The example commands change the maximum number of paths to 128. On Spectrum-1 switches, you can set a value between 1 and 64. On Spectrum-2 and later, you can set a value between 1 and 128. 1 disables the BGP multipath option.

{{< tabs "790 ">}}
{{< tab "NVUE Commands ">}}

```
cumulus@switch:~$ nv set vrf default router bgp address-family ipv4-unicast multipaths ibgp 128 
cumulus@switch:~$ nv config apply
```

{{< /tab >}}
{{< tab "vtysh Commands ">}}

```
cumulus@switch:~$ sudo vtysh
...
switch# configure terminal
switch(config)# router bgp 65101
switch(config-router)# address-family ipv4
switch(config-router-af)# maximum-paths 128
switch(config-router-af)# end
switch# write memory
switch# exit
```

The vtysh commands save the configuration in the `address-family` stanza of the `/etc/frr/frr.conf` file. For example:

```
...
address-family ipv4 unicast
 network 10.1.10.0/24
 network 10.10.10.1/32
 maximum-paths 128
exit-address-family
...
```

{{< /tab >}}
{{< /tabs >}}

When you enable *BGP multipath*, Cumulus Linux load balances BGP routes from the same AS. If the routes go across several different AS neighbors, even if the AS path length is the same, they are not load balanced. To load balance between multiple paths received from different AS neighbors.

{{< tabs "830 ">}}
{{< tab "NVUE Commands ">}}

```
cumulus@switch:~$ nv set vrf default router bgp path-selection multipath aspath-ignore on
cumulus@switch:~$ nv config apply
```

{{< /tab >}}
{{< tab "vtysh Commands ">}}

```
cumulus@switch:~$ sudo vtysh
...
switch# configure terminal
switch(config)# router bgp 65101
switch(config-router)# bgp bestpath as-path multipath-relax
switch(config-router)# end
switch# write memory
switch# exit
```

The vtysh commands save the configuration in the `/etc/frr/frr.conf` file. For example:

```
...
router bgp 65101
  bgp router-id 10.0.0.1
  bgp bestpath as-path multipath-relax
...
```

{{< /tab >}}
{{< /tabs >}}

{{%notice note%}}
When you disable the *bestpath as-path multipath-relax* option, EVPN type-5 routes do not use the updated configuration. Type-5 routes continue to use all available ECMP paths in the underlay fabric, regardless of ASN.
{{%/notice%}}

## Advertise IPv4 Prefixes with IPv6 Next Hops

{{<exlink url="https://tools.ietf.org/html/rfc5549" text="RFC 5549">}} defines how BGP advertises IPv4 prefixes with IPv6 next hops. The RFC does not make a distinction between whether the IPv6 peering and next hop values must be global unicast addresses (GUA) or link-local addresses. Cumulus Linux supports advertising IPv4 prefixes with IPv6 global unicast and link-local next hop addresses, with either *unnumbered* or *numbered* BGP.

When BGP peering uses IPv6 global addresses, and BGP advertises and installs IPv4 prefixes, Cumulus Linux uses IPv6 route advertisements to derive the MAC address of the peer so that FRR can create an IPv4 route with a link-local IPv4 next hop address (defined by RFC 3927). FRR configures these route advertisement settings automatically upon receiving an update from a BGP peer that uses IPv6 global addresses with an IPv4 prefix and an IPv6 next hop, and after it negotiates the enhanced-next hop capability.

To enable advertisement of IPv4 prefixes with IPv6 next hops over global IPv6 peerings, add the `extended-nexthop` capability to the global IPv6 neighbor statements on each end of the BGP sessions.

{{%notice note%}}
Changing the `extended-nexthop` capability results in BGP session flaps, which might lead to packet drops.
{{%/notice%}}

{{< tabs "877 ">}}
{{< tab "NVUE Commands ">}}

```
cumulus@switch:~$ nv set vrf default router bgp neighbor 2001:db8:0002::0a00:0002 capabilities extended-nexthop on
cumulus@switch:~$ nv config apply
```

{{< /tab >}}
{{< tab "vtysh Commands ">}}

```
cumulus@switch:~$ sudo vtysh
...
switch# configure terminal
switch(config)# router bgp 65101
switch(config-router)# neighbor 2001:db8:0002::0a00:0002 capability extended-nexthop
switch(config-router)# end
switch# write memory
switch# exit
```

The vtysh commands save the configuration in the `/etc/frr/frr.conf` file. For example:

```
...
router bgp 65101
  ...
  neighbor 2001:db8:0002::0a00:0002 capability extended-nexthop
...
```

{{< /tab >}}
{{< /tabs >}}

Ensure that you have activated the IPv6 peers under the IPv4 unicast address family; otherwise, all peers activate in the IPv4 unicast address family by default. If you configure `no bgp default ipv4-unicast`, you need to activate the IPv6 neighbor under the IPv4 unicast address family as shown below:

{{< tabs "914 ">}}
{{< tab "NVUE Commands ">}}

```
cumulus@switch:~$ nv set vrf default router bgp neighbor 2001:db8:0002::0a00:0002 capabilities extended-nexthop on
cumulus@switch:~$ nv set vrf default router bgp neighbor 2001:db8:0002::0a00:0002 address-family ipv4-unicast state enabled
cumulus@switch:~$ nv config apply
```

{{< /tab >}}
{{< tab "vtysh Commands ">}}

```
cumulus@switch:~$ sudo vtysh
...
switch# configure terminal
switch(config)# router bgp 65101
switch(config-router)# neighbor 2001:db8:0002::0a00:0002 capability extended-nexthop
switch(config-router)# address-family ipv4 unicast
switch(config-router-af)# neighbor 2001:db8:0002::0a00:0002 activate
switch(config-router-af)# end
switch# write memory
switch# exit
```

The vtysh commands save the configuration in the `/etc/frr/frr.conf` file. For example:

```
...
router bgp 65101
router-id 10.10.10.1
no bgp default ipv4-unicast
neighbor 2001:db8:0002::0a00:0002 remote-as external
neighbor 2001:db8:0002::0a00:0002 capability extended-nexthop
!
address-family ipv4 unicast
  neighbor 2001:db8:0002::0a00:0002 activate
exit-address-family
...
```

{{< /tab >}}
{{< /tabs >}}

## Neighbor Maximum Prefixes

To protect against an internal network connectivity disruption caused by BGP, you can control the number of route announcements (prefixes) you want to receive from a BGP neighbor.

The following example commands set the maximum number of prefixes allowed from the BGP neighbor on swp51 to 3000:

{{< tabs "964 ">}}
{{< tab "NVUE Commands ">}}

```
cumulus@leaf01:~$ nv set vrf default router bgp neighbor swp51 address-family ipv4-unicast prefix-limits inbound maximum 3000
cumulus@leaf01:~$ nv config apply
```

{{< /tab >}}
{{< tab "vtysh Commands ">}}

```
cumulus@leaf01:~$ sudo vtysh
...
leaf01# configure terminal
leaf01(config)# router bgp 65001
leaf01(config-router)# neighbor swp51 maximum-prefix 3000
leaf01(config-router)# end
leaf01# write memory
leaf01# exit
```

{{< /tab >}}
{{< /tabs >}}

## Aggregate Addresses

To minimize the size of the routing table and save bandwidth, you can aggregate a range of networks in your routing table into a single prefix.

The following example command aggregates a range of addresses, such as 10.1.1.0/24, 10.1.2.0/24, 10.1.3.0/24 into the single prefix 10.1.0.0/16:

```
cumulus@leaf01:~$ nv set vrf default router bgp address-family ipv4-unicast aggregate-route 10.1.0.0/16 
cumulus@leaf01:~$ nv config apply
```

The `summary-only` option ensures that BGP suppresses longer-prefixes inside the aggregate address before sending updates:

```
cumulus@leaf01:~$ nv set vrf default router bgp address-family ipv4-unicast aggregate-route 10.1.0.0/16 summary-only on
cumulus@leaf01:~$ nv config apply
```

## Suppress Route Advertisement

You can configure BGP to wait for a response from the RIB indicating that the routes installed in the RIB are also installed in the ASIC before sending updates to peers.

{{< tabs "TabID1011 ">}}
{{< tab "NVUE Commands ">}}

```
cumulus@leaf01:~$ nv set router bgp wait-for-install on
cumulus@leaf01:~$ nv config apply
```

When you configure suppress route advertisement, NVUE restarts `switchd`.

{{< /tab >}}
{{< tab "vtysh Commands ">}}

1. Run the following vtysh commands:

   ```
   cumulus@leaf01:~$ sudo vtysh
   ...
   leaf01# configure terminal
   leaf01(config)# router bgp 65101
   leaf01(config-router)# bgp suppress-fib-pending
   leaf01(config-router)# end
   leaf01# write memory
   leaf01# exit
   ```

   The vtysh commands save the configuration in the `/etc/frr/frr.conf` file. For example:

   ```
   ...
   router bgp 65199
   bgp router-id 10.10.10.101
   neighbor swp51 remote-as external
   bgp suppress-fib-pending
   ...
   ```

2. Edit the `/etc/cumulus/switchd.d/kernel_route_offload_flags.conf` file to set the `kernel_route_offload_flags` parameter to 2:

   ```
   cumulus@leaf01:~$ sudo nano /etc/cumulus/switchd.d/kernel_route_offload_flags.conf  
   # Set routing-forwarding-sync mode for routes.
   #  0: No notification on HW install success or failure (default mode)
   #  1: Notify HW install failure
   #  2: Notify HW install success/failure
   kernel_route_offload_flags = 2
   ```

3. Restart switchd:

   ```
   cumulus@leaf01:~$ sudo systemctl restart switchd.service
   ```

{{< /tab >}}
{{< /tabs >}}

{{<link url="Upgrading-Cumulus-Linux/#issu" text="ISSU">}} suppresses route advertisement automatically when upgrading or troubleshooting an active switch so that there is minimal disruption to the network.
<!-- vale off -->
## BGP add-path

Cumulus Linux supports both BGP add-path RX and BGP add-path TX.

### BGP add-path RX
<!-- vale on -->
BGP add-path RX enables BGP to receive multiple paths for the same prefix. A path identifier ensures that additional paths do not override previously advertised paths. Cumulus Linux enables BGP add-path RX by default; you do not need to perform additional configuration.

To view the existing capabilities, run the vtysh `show ip bgp neighbors` command. You can see the existing capabilities in the subsection *Add Path*, below *Neighbor capabilities.*

The following example output shows that BGP can send and receive additional BGP paths, and that the BGP neighbor on swp51 supports both.

```
cumulus@leaf01:~$ sudo vtysh
...
leaf01# show ip bgp neighbors
BGP neighbor on swp51: fe80::7c41:fff:fe93:b711, remote AS 65199, local AS 65101, external link
Hostname: spine01
  BGP version 4, remote router ID 10.10.10.101, local router ID 10.10.10.1
  BGP state = Established, up for 1d12h39m
  Last read 00:00:03, Last write 00:00:01
  Hold time is 9, keepalive interval is 3 seconds
  Neighbor capabilities:
    4 Byte AS: advertised and received
    AddPath:
      IPv4 Unicast: RX advertised IPv4 Unicast and received
    Extended nexthop: advertised and received
      Address families by peer:
                   IPv4 Unicast
    Route refresh: advertised and received(old & new)
    Address Family IPv4 Unicast: advertised and received
    Hostname Capability: advertised (name: leaf01,domain name: n/a) received (name: spine01,domain name: n/a)
    Graceful Restart Capability: advertised and received
...
```

To view the current additional paths, run the vtysh `show ip bgp <prefix>` command. The example output shows that the TX node adds an additional path for receiving. Each path has a unique AddPath ID.

```
cumulus@leaf01:mgmt:~$ sudo vtysh
...
leaf01# show ip bgp 10.10.10.9
BGP routing table entry for 10.10.10.9/32
Paths: (2 available, best #1, table Default-IP-Routing-Table)
  Advertised to non peer-group peers:
  spine01(swp51) spine02(swp52)
  65020 65012
    fe80::4638:39ff:fe00:5c from spine01(swp51) (10.10.10.12)
    (fe80::4638:39ff:fe00:5c) (used)
      Origin incomplete, localpref 100, valid, external, multipath, bestpath-from-AS 65020, best (Older Path)
      AddPath ID: RX 0, TX 6
      Last update: Wed Nov 16 22:47:00 2016
  65020 65012
    fe80::4638:39ff:fe00:2b from spine02(swp52) (10.10.10.12)
    (fe80::4638:39ff:fe00:2b) (used)
      Origin incomplete, localpref 100, valid, external, multipath
      AddPath ID: RX 0, TX 3
      Last update: Fri Oct  2 03:56:33 2020
```
<!-- vale off -->
### BGP add-path TX

BGP add-path TX enables BGP to advertise more than just the best path for a prefix. Cumulus Linux includes two options:
- `addpath-tx-all-paths` advertises all known paths to a neighbor.
- `addpath-tx-bestpath-per-AS` advertises only the best path learned from each AS to a neighbor.

The following example commands configure leaf01 to advertise the best path learned from each AS to the BGP neighbor on swp50:
<!-- vale on -->
{{< tabs "1138 ">}}
{{< tab "NVUE Commands ">}}

```
cumulus@leaf01:~$ nv set vrf default router bgp autonomous-system 65101
cumulus@leaf01:~$ nv set vrf default router bgp neighbor swp50 address-family ipv4-unicast add-path-tx best-per-as
cumulus@leaf01:~$ nv config apply
```

{{< /tab >}}
{{< tab "vtysh Commands ">}}

```
cumulus@leaf01:~$ sudo vtysh
...
leaf01# configure terminal
leaf01(config)# router bgp 65101
leaf01(config-router)# neighbor swp50 addpath-tx-bestpath-per-AS
leaf01(config-router)# end
leaf01# write memory
leaf01# exit
```

{{< /tab >}}
{{< /tabs >}}
<!-- vale off -->
The following example commands configure leaf01 to advertise all paths learned from each AS to the BGP neighbor on swp50:
<!-- vale on -->
{{< tabs "928 ">}}
{{< tab "NVUE Commands ">}}

```
cumulus@leaf01:~$ nv set vrf default router bgp autonomous-system 65101
cumulus@leaf01:~$ nv set vrf default router bgp neighbor swp50 address-family ipv4-unicast add-path-tx all-paths
cumulus@leaf01:~$ nv config apply
```

{{< /tab >}}
{{< tab "vtysh Commands ">}}

```
cumulus@leaf01:~$ sudo vtysh
...
leaf01# configure terminal
leaf01(config)# router bgp 65101
leaf01(config-router)# neighbor swp50 addpath-tx-all-paths
leaf01(config-router)# end
leaf01# write memory
leaf01# exit
```

{{< /tab >}}
{{< /tabs >}}

The following example configuration shows how BGP add-path TX advertises the best path learned from each AS.
<!-- vale off -->
| <div style="width:500px">   |    |
| -- | -- |
| {{< img src = "/images/cumulus-linux/bgp-add-path-tx.png" >}} | In this configuration:<ul><li>Every leaf and every spine has a different ASN</li><li>eBGP is configured between:<ul><li>leaf01 and spine01, spine02</li><li>leaf03 and spine01, spine02</li><li>leaf01 and leaf02 (leaf02 only has a single peer, which is leaf01)</li></ul><li>leaf01 is configured to advertise the best path learned from each AS to BGP neighbor leaf02</li><li>leaf03 generates a loopback IP address (10.10.10.3/32) into BGP with a network statement</li></ul>|
<!-- vale on -->
When you run the `show ip bgp 10.10.10.3/32` command on leaf02, the command output shows the leaf03 loopback IP address and two BGP paths, both from leaf01:

```
cumulus@leaf02:mgmt:~$ sudo vtysh
...
leaf02# show ip bgp 10.10.10.3/32
BGP routing table entry for 10.10.10.3/32
Paths: (2 available, best #2, table default)
       Advertised to non peer-group peers:
       leaf01(swp50)
  65101 65199 65103
    fe80::4638:39ff:fe00:13 from leaf01(swp50) (10.10.10.1)
    (fe80::4638:39ff:fe00:13) (used)
      Origin IGP, valid, external
      AddPath ID: RX 4, TX-All 0 TX-Best-Per-AS 0
      Last update: Thu Oct 15 18:31:46 2020
  65101 65198 65103
    fe80::4638:39ff:fe00:13 from leaf01(swp50) (10.10.10.1)
    (fe80::4638:39ff:fe00:13) (used)
      Origin IGP, valid, external, bestpath-from-AS 65101, best (Nothing left to compare)
      AddPath ID: RX 3, TX-All 0 TX-Best-Per-AS 0
      Last update: Thu Oct 15 18:31:46 2020
```

## Conditional Advertisement

Routes are typically propagated even if a different path exists. The BGP conditional advertisement feature lets you advertise certain routes only if other routes either do or do not exist.

This feature is typically used in multihomed networks where BGP advertises some prefixes to one of the providers only if information from the other provider is not present. For example, a multihomed router can use conditional advertisement to choose which upstream provider learns about the routes it provides so that it can influence which provider handles traffic destined for the downstream router. This is useful for cost of service, latency, or other policy requirements that are not natively accounted for in BGP.

Conditional advertisement uses the `non-exist-map` or the `exist-map` and the `advertise-map` keywords to track routes by route prefix.
You configure the BGP neighbors to use the route maps.

{{%notice info%}}
Use caution when configuring conditional advertisement on a large number of BGP neighbors. Cumulus Linux scans the entire RIB table every 60 seconds by default; depending on the number of routes in the RIB, this can result in longer processing times. NVIDIA does not recommend that you configure conditional advertisement on more than 50 neighbors.
{{%/notice%}}

The following example commands configure the switch to send a 10.0.0.0/8 summary route only if the 10.0.0.0/24 route exists in the routing table. The commands perform the following configuration:
- Enable the conditional advertisement option.
- Create a prefix list called EXIST with the route 10.0.0.0/24.
- Create a route map called EXISTMAP that uses the prefix list EXIST. You must provide the route map match type (`ipv4` or `ipv6`).
- Create a prefix list called ADVERTISE with the route to advertise (10.0.0.0/8).
- Create a route map called ADVERTISEMAP that uses the prefix list ADVERTISE. You must provide the route map match type (`ipv4` or `ipv6`).
- Configure BGP neighbor swp51 to use the route maps.

{{< tabs "1243 ">}}
{{< tab "NVUE Commands ">}}

```
cumulus@leaf01:~$ nv set vrf default router bgp neighbor swp51 address-family ipv4-unicast conditional-advertise state enabled 
cumulus@leaf01:~$ nv set router policy prefix-list EXIST rule 10 match 10.0.0.0/24
cumulus@leaf01:~$ nv set router policy prefix-list EXIST rule 10 action permit
cumulus@leaf01:~$ nv set router policy route-map EXISTMAP rule 10 match type ipv4
cumulus@leaf01:~$ nv set router policy route-map EXISTMAP rule 10 action permit
cumulus@leaf01:~$ nv set router policy route-map EXISTMAP rule 10 match ip-prefix-list EXIST
cumulus@leaf01:~$ nv set router policy prefix-list ADVERTISE rule 10 action permit
cumulus@leaf01:~$ nv set router policy prefix-list ADVERTISE rule 10 match 10.0.0.0/8
cumulus@leaf01:~$ nv set router policy route-map ADVERTISEMAP rule 10 match type ipv4
cumulus@leaf01:~$ nv set router policy route-map ADVERTISEMAP rule 10 action permit
cumulus@leaf01:~$ nv set router policy route-map ADVERTISEMAP rule 10 match ip-prefix-list ADVERTISE
cumulus@leaf01:~$ nv set vrf default router bgp neighbor swp51 address-family ipv4-unicast conditional-advertise advertise-map ADVERTISEMAP
cumulus@leaf01:~$ nv set vrf default router bgp neighbor swp51 address-family ipv4-unicast conditional-advertise exist-map EXIST
cumulus@leaf01:~$ nv config apply
```

{{< /tab >}}
{{< tab "vtysh Commands ">}}

```
cumulus@leaf01:~$ sudo vtysh
...
leaf01# configure terminal
leaf01(config)# ip prefix-list EXIST seq 10 permit 10.0.0.0/24
leaf01(config)# route-map EXISTMAP permit 10
leaf01(config-route-map)# match ip address prefix-list EXIST
leaf01(config-route-map)# exit
leaf01(config)# ip prefix-list ADVERTISE seq 10 permit 10.0.0.0/8
leaf01(config)# route-map ADVERTISEMAP permit 10
leaf01(config-route-map)# match ip address prefix-list ADVERTISE
leaf01(config-route-map)# exit
leaf01(config)# router bgp
leaf01(config-router)# neighbor swp51 advertise-map ADVERTISEMAP exist-map EXISTMAP
leaf01(config-router)# end
leaf01# write memory
leaf01# exit
```

The commands save the configuration in the `/etc/frr/frr.conf` file. For example:

```
cumulus@leaf01:~$ sudo cat /etc/frr/frr.conf
...
neighbor swp51 activate
neighbor swp51 advertise-map ADVERTISEMAP exist-map EXIST
...
ip prefix-list ADVERTISE seq 10 permit 10.0.0.0/8
ip prefix-list EXIST seq 10 permit 10.0.0.0/24
route-map ADVERTISEMAP permit 10
match ip address prefix-list ADVERTISE
route-map EXISTMAP permit 10
match ip address prefix-list EXIST
```

{{< /tab >}}
{{< /tabs >}}

Cumulus Linux scans the entire <span class="a-tooltip">[RIB](## "BGP Routing Information Base")</span> table every 60 seconds. You can set the conditional advertisement timer to increase or decrease how often you want Cumulus Linux to scan the RIB table. You can set a value between 5 and 240 seconds.

{{%notice note%}}
A lower value (such as 5) increases the amount of processing needed. Use caution when configuring conditional advertisement on a large number of BGP neighbors.
{{%/notice%}}

{{< tabs "1310 ">}}
{{< tab "NVUE Commands ">}}

```
cumulus@leaf01:~$ nv set vrf default router bgp timers conditional-advertise 100
cumulus@leaf01:~$ nv config apply
```

{{< /tab >}}
{{< tab "vtysh Commands ">}}

```
cumulus@leaf01:~$ sudo vtysh
...
leaf01# configure terminal
leaf01(config)# router bgp
leaf01(config-router)# bgp conditional-advertisement timer 100
leaf01(config-router)# end
leaf01# write memory
leaf01# exit
```

The commands save the configuration in the `/etc/frr/frr.conf` file. For example:

```
cumulus@leaf01:~$ sudo cat /etc/frr/frr.conf
...
router bgp 65101
 bgp router-id 10.10.10.1
 bgp conditional-advertisement timer 100
 neighbor swp51 interface remote-as external
 neighbor swp51 advertisement-interval 0
 neighbor swp51 timers 3 9
 neighbor swp51 timers connect 10
 neighbor swp52 interface remote-as external
 neighbor swp52 advertisement-interval 0
 neighbor swp52 timers 3 9
 neighbor swp52 timers connect 10
...
```

{{< /tab >}}
{{< /tabs >}}

## Next Hop Tracking

By default, next hop tracking does not resolve next hops through the default route. If you want BGP to peer across the default route, run the vtysh `ip nht resolve-via-default` command.

The following example command configures BGP to peer across the default route from the default VRF.

```
cumulus@leaf01:~$ sudo vtysh
...
leaf01# configure terminal
leaf01(config)# ip nht resolve-via-default
leaf01(config)# exit
leaf01# write memory
leaf01# exit
```

The following example command configures BGP to peer across the default route from VRF BLUE:

```
cumulus@leaf01:~$ sudo vtysh
leaf01# configure terminal
leaf01(config)# vrf BLUE
leaf01(config-vrf)# ip nht resolve-via-default
leaf01(config-vrf)# end
leaf01# write memory
leaf01# exit
cumulus@leaf01:~$
```

## BGP Prefix Independent Convergence

BGP prefix independent convergence (PIC) reduces convergence times and improves unicast traffic convergence for remote link and node failures (when the BGP next hop fails), regardless of route scale. A remote link is a link between a spine and a remote leaf, or a spine and the super spine layer.

When you configure BGP PIC, Cumulus Linux assigns one next hop group for each source and the remote leaf advertises a route with a prefix derived from the router ID. The remote leaf tags prefix routes with a route-origin extended community (SOO) so that the local leaf recognizes the routes. When the network topology changes, the local leaf obtains the router ID route with the updated ECMP, allowing a O (1) next hop group replace operation for all prefixes from the remote leaf without waiting for individual BGP updates.

{{%notice note%}}
- Cumulus Linux supports BGP PIC on Spectrum-4 switches.
- Cumulus Linux does not support BGP PIC with EVPN, MLAG, or VRF route leaking.
- Do not configure PIC if you have configured EVPN.
- You can configure PIC on the default VRF only.
- NVIDIA recommends that you do not redistribute interface addresses into BGP when you enable PIC.
- Do not configure the router ID and network address with the same value.
- The BGP router ID and the aggregate address must not be in the same subnet.
- Do not use martian addresses as the BGP router ID when you enable PIC.
- You need additional ECMP hardware resources for PIC. Refer to {{<link url="Equal-Cost-Multipath-Load-Sharing/#ecmp-resource-sharing-during-next-hop-group-updates" text="Additional ECMP resource optimization for next hop groups">}}
{{%/notice%}}

To configure PIC:
- **On a leaf only**, enable the BGP advertise origin option so that BGP can attach the SOO extended community to all routes advertised to its peers from the source where the routes originate.
- **On all switches**, enable the BGP next hop group per source option so that when BGP receives routes with the SOO extended community, it allocates a next hop group for each source.
- **On a spine and super spine**, set the {{<link url="#enable-read-only-mode" text="read-only mode">}} BGP convergence wait time to 30 and the convergence wait establish wait time to 15. These are the minimum recommended timer settings to ensure optimal convergence when using PIC.

{{%notice note%}}
Changing the BGP advertise origin option or the BGP next hop group per source option can cause traffic disruption.
{{%/notice%}}

{{< tabs "1398 ">}}
{{< tab "NVUE Commands ">}}

1. **On a leaf switch**, enable the BGP advertise origin option. The following example enables BGP advertise origin for IPv4:

   ```
   cumulus@leaf01:~$ nv set vrf default router bgp address-family ipv4-unicast advertise-origin
   cumulus@leaf01:~$ nv config apply
   ```

   For IPv6, run the `nv set vrf <vrf-id> router bgp address-family ipv6-unicast advertise-origin` command.

2. **On all switches** (leaf, spine and super spine), enable the next hop group per source option. The following example enables the next hop group per source option for IPv4:

   ```
   cumulus@spine01:~$ nv set vrf default router bgp address-family ipv4-unicast nhg-per-origin
   cumulus@spine01:~$ nv config apply
   ```

   For IPv6, run the `nv set vrf <vrf-id> router bgp address-family ipv6-unicast nhg-per-origin` command.

3. **On a spine and super spine**, set the BGP convergence wait time to 30 and the convergence wait establish wait time to 15.

   ```
   cumulus@leaf01:~$ nv set router bgp convergence-wait time 30
   cumulus@leaf01:~$ nv set router bgp convergence-wait establish-wait-time 15
   cumulus@leaf01:~$ nv config apply
   ```

To disable BGP PIC, run the `nv unset vrf <vrf-id> router bgp address-family <address-family> advertise-origin` command on the leaf switch and the `nv unset vrf <vrf-id> router bgp address-family <address-family> nhg-per-origin` command on all switches.

{{< /tab >}}
{{< tab "vtysh Commands ">}}

1. **On a leaf switch**, enable the BGP advertise origin option. The following example enables BGP advertise origin for IPv4:

   ```
   cumulus@leaf01:~$ sudo vtysh
   ...
   leaf01# configure terminal
   leaf01(config)# router bgp 65101
   leaf01(config-router)# address-family ipv4
   leaf01(config-router-af)# bgp advertise-origin
   leaf01(config-router-af)# end
   leaf01# write memory
   leaf01# exit
   ```

2. **On all switches** (leaf, spine and super spine), enable the next hop group per source option. The following example enables BGP next hop group per source for IPv4:

   ```
   cumulus@spine01:~$ sudo vtysh
   ...
   spine01# configure terminal
   spine01(config)# router bgp 65101
   spine01(config-router)# address-family ipv4
   spine01(config-router-af)# bgp nhg-per-origin
   spine01(config-router-af)# end
   spine01# write memory
   spine01# exit
   ```

3. **On a spine and super spine**, set the BGP convergence wait time to 30 and the convergence wait establish wait time to 15.

  ```
  cumulus@leaf01:~$ sudo vtysh
  ...
  leaf01# configure terminal
  leaf01(config)# router bgp
  leaf01(config-router)# update-delay 30 15
  leaf01(config-router)# end
  leaf01# write memory
  leaf01# exit
  ```

The vtysh commands save the configuration in the `/etc/frr/frr.conf` file. For example:

```
...
bgp update-delay 30 15
router bgp 65101
  ...
  address-family ipv4 unicast
  ...
   bgp advertise-origin
   bgp nhg-per-origin
...
```

To disable BGP PIC, use the `no bgp advertise-origin` command on the leaf switch and the `no bgp nhg-per-origin` on all switches. For example:

```
cumulus@spine02:~$ sudo vtysh
...
spine01# configure terminal
spine01(config)# router bgp 65101
spine01(config-router)# address-family ipv4
spine01(config-router-af)# no bgp nhg-per-origin
spine01(config-router-af)# end
spine01# write memory
spine01# exit
```

{{< /tab >}}
{{< /tabs >}}

### BGP PIC in a Multiplane Topology

Fast route convergence in case of remote link failures between leaf and spine, and spine and superspine layers in a multiplane topology requires you to configure the SOO source IP address on leaf switches to advertise the SOO route in addition to configuring PIC as described in {{<link url="#bgp-prefix-independent-convergence" text="BGP Prefix Independent Convergence">}} above. The switch uses the SOO source IP address instead of the router ID.

{{%notice note%}}
The SOO source IP address must be unique in the topology so that it does not conflict with the router ID or loopback IP address of any other switch.
{{%/notice%}}

To configure PIC in a multiplane topology, set the SOO source IP address on a leaf. Configuring the same SOO source IP address on multiple leaf switches puts them in the same anycast group.

{{< tabs "1654 ">}}
{{< tab "NVUE Commands ">}}

```
cumulus@leaf01:~$ nv set vrf default router bgp soo-source 10.1.1.1
cumulus@leaf01:~$ nv config apply
```

To unset the SOO source IP address, run the `nv set vrf default router bgp soo-source` command.

{{< /tab >}}
{{< tab "vtysh Commands ">}}

   ```
   cumulus@leaf01:~$ sudo vtysh
   ...
   leaf01# configure terminal
   leaf01(config)# router bgp 65101
   leaf01(config-router)# bgp soo-source 10.1.1.1
   leaf01(config-router)# end
   leaf01# write memory
   leaf01# exit
   ```

{{< /tab >}}
{{< /tabs >}}

If you set the SOO source IP address on a leaf switch before you enable the BGP advertise origin option, the switch starts advertising SOO routes using the configured SOO source IP address.

If you set the SOO source IP address on a leaf switch after enable the BGP advertise origin option:
- The leaf withdraws the old SOO route (the one with the router ID).
- The leaf announces a new SOO route using the SOO-source IP address.  
- All prefix routes are readvertised with the new SOO tag.  
- All network switches detect this change, remove references to the old SOO route, and install the new SOO route in their routing tables.

### Show BGP PIC Information

Cumulus Linux provides several show commands to help you troubleshoot BGP PIC. Refer to {{<link url="Troubleshooting-BGP/#show-prefix-independent-convergence-information" text="Show Prefix Independent Convergence Information">}}.

## BGP Timers

BGP includes several timers that you can configure.

### Keepalive Interval and Hold Time

By default, BGP exchanges periodic keepalive messages to measure and ensure that a peer is still alive and functioning. If BGP does not receive a keepalive or update message from the peer within the hold time, it declares the peer down and withdraws all routes received by this peer from the local BGP table. By default, the keepalive interval is 3 seconds and the hold time is 9 seconds. To decrease CPU load when there are a lot of neighbors, you can increase the values of these timers or disable the exchange of keepalives. When manually configuring new values, the keepalive interval can be less than or equal to one third of the hold time, but cannot be less than 1 second. Setting the keepalive and hold time values to 0 disables the exchange of keepalives.

The following example commands set the keepalive interval to 10 seconds and the hold time to 30 seconds.

{{< tabs "1482 ">}}
{{< tab "NVUE Commands ">}}

```
cumulus@leaf01:~$ nv set vrf default router bgp neighbor swp51 timers keepalive 10
cumulus@leaf01:~$ nv set vrf default router bgp neighbor swp51 timers hold 30
cumulus@leaf01:~$ nv config apply
```

To set the timers back to the default values, run the `nv unset vrf <vrf-id> router bgp neighbor <interface-id> timers keepalive` and the `nv unset vrf <vrf-id> router bgp neighbor <interface-id> timers hold` commands.

{{< /tab >}}
{{< tab "vtysh Commands ">}}

```
cumulus@leaf01:~$ sudo vtysh
...
leaf01# configure terminal
leaf01(config)# router bgp
leaf01(config-router)# neighbor swp51 timers 10 30
leaf01(config-router)# end
leaf01# write memory
leaf01# exit
```

The vtysh commands save the configuration in the `/etc/frr/frr.conf` file. For example:

```
...
router bgp 65101
  ...
  neighbor swp51 timers 10 30
...
```

{{< /tab >}}
{{< /tabs >}}

### Reconnect Interval

By default, the BGP process attempts to connect to a peer after a failure (or on startup) every 10 seconds. You can change this value to suit your needs.

The following example commands set the reconnect value to 30 seconds:

{{< tabs "1526 ">}}
{{< tab "NVUE Commands ">}}

```
cumulus@leaf01:~$ nv set vrf default router bgp neighbor swp51 timers connection-retry 30
cumulus@leaf01:~$ nv config apply
```

{{< /tab >}}
{{< tab "vtysh Commands ">}}

```
cumulus@leaf01:~$ sudo vtysh
...
leaf01# configure terminal
leaf01(config)# router bgp
leaf01(config-router)# neighbor swp51 timers connect 30
leaf01(config-router)# end
leaf01# write memory
leaf01# exit
```

The vtysh commands save the configuration in the `/etc/frr/frr.conf` file. For example:

```
...
router bgp 65101
  ...
  neighbor swp51 timers connect 30
...
```

{{< /tab >}}
{{< /tabs >}}

### Advertisement Interval

After making a new best path decision for a prefix, BGP can insert a delay before advertising the new results to a peer. This delay rate limits the amount of changes advertised to downstream peers and lowers processing requirements by slowing down convergence. By default, this interval is 0 seconds for both eBGP and iBGP sessions, which allows for fast convergence. For more information about the advertisement interval, see {{<exlink url="http://tools.ietf.org/html/draft-jakma-mrai-02" text="this IETF draft">}}.

The following example commands set the advertisement interval to 5 seconds:

{{< tabs "1567 ">}}
{{< tab "NVUE Commands ">}}

```
cumulus@leaf01:~$ nv set vrf default router bgp neighbor swp51 timers route-advertisement 5
cumulus@leaf01:~$ nv config apply
```

{{< /tab >}}
{{< tab "vtysh Commands ">}}

```
cumulus@leaf01:~$ sudo vtysh
...
leaf01# configure terminal
leaf01(config)# router bgp
leaf01(config-router)# neighbor swp51 advertisement-interval 5
leaf01(config-router)# end
leaf01# write memory
leaf01# exit
```

The vtysh commands save the configuration in the `/etc/frr/frr.conf` file. For example:

```
...
router bgp 65101
  ...
  neighbor swp51 advertisement-interval 5
...
```

{{< /tab >}}
{{< /tabs >}}

## BGP Input and Ouput Message Queue Limit

You can configure the input and the output message queue limit for all peers. For both the input and output queue limit, you can set a value between 1 and 4294967295 messages. The default setting is 10000.

{{%notice note%}}
Only increase the input or output queue if you have enough memory to handle large queues of messages at the same time.
{{%/notice%}}

{{< tabs "1610 ">}}
{{< tab "NVUE Commands ">}}

The following example sets the input queue limit to 2048 messages and the output queue limit to 2048 messages:

```
cumulus@leaf01:~$ nv set router bgp queue-limit input 2048
cumulus@leaf01:~$ nv set router bgp queue-limit output 2048
cumulus@leaf01:~$ nv config apply
```

{{< /tab >}}
{{< tab "vtysh Commands ">}}

The following example sets the input queue limit to 2048 messages and the output queue limit to 2048 messages:

```
cumulus@leaf01:~$ sudo vtysh
...
leaf01# configure terminal
leaf01(config)# bgp input-queue-limit 2048
leaf01(config)# bgp output-queue-limit 2048
leaf01(config)# end
leaf01# write memory
leaf01# exit
```

{{< /tab >}}
{{< /tabs >}}

To show the input and output message queue configuration, run the `nv show router bgp queue-limit` command.

## Route Reflectors

<span class="a-tooltip">[iBGP](## "internal BGP")</span> rules state that BGP cannot send a route learned from an iBGP peer to another iBGP peer. In a data center spine and leaf network using iBGP, this prevents a spine from sending a route learned from a leaf to any other leaf. As a workaround, you can use a *route reflector*. When an iBGP speaker is a route reflector, it *can* send iBGP learned routes to other iBGP peers.

In the following example, spine01 is acting as a route reflector. The leaf switches, leaf01, leaf02 and leaf03 are *route reflector clients*. BGP sends any route that spine01 learns from a route reflector client to other route reflector clients.

{{< img src = "/images/cumulus-linux/bgp-route-reflectors-example.png" >}}

To configure the BGP node as a route reflector for a BGP peer, set the neighbor `route-reflector-client` option. The following example sets spine01 shown in the illustration above to be a route reflector for leaf01 (on swp1), which is a route reflector client. You do not have to configure the client.

{{< tabs "1652 ">}}
{{< tab "NVUE Commands ">}}

```
cumulus@spine01:~$ nv set vrf default router bgp neighbor swp1 address-family ipv4-unicast route-reflector-client enabled
cumulus@spine01:~$ nv config apply
```

{{< /tab >}}
{{< tab "vtysh Commands ">}}

```
cumulus@spine01:~$ sudo vtysh
...
spine01# configure terminal
spine01(config)# router bgp 65199
spine01(config-router)# address-family ipv4
spine01(config-router-af)# neighbor swp1 route-reflector-client
spine01(config-router-af)# end
spine01# write memory
spine01# exit
```

The vtysh commands save the configuration in the `/etc/frr/frr.conf` file. For example:

```
...
router bgp 65199
 bgp router-id 10.10.10.101
 neighbor swp51 remote-as external
 !
 address-family ipv4 unicast
  network 10.10.10.101/32
  neighbor swp51 route-reflector-client
 exit-address-family
...
```

{{< /tab >}}
{{< /tabs >}}

When you configure BGP route reflectors, they reflect routes announced by the peers configured as clients. BGP client-to-client reflection is enabled by default. You can disable client-to-client reflection if required.

{{< tabs "1819 ">}}
{{< tab "NVUE Commands ">}}

The following example configures a BGP route reflector with cluster-id 10.10.10.5. BGP client-to-client reflection is enabled by default.

```
cumulus@leaf01:~$ nv set vrf blue router bgp route-reflection state enabled
cumulus@leaf01:~$ nv set vrf blue router bgp route-reflection cluster-id 10.10.10.5
cumulus@leaf01:~$ nv config apply
```

The following example configures a BGP route reflector with cluster-id 10.10.10.5 and disables client-to-client reflection:

```
cumulus@leaf01:~$ nv set vrf blue router bgp route-reflection state enabled
cumulus@leaf01:~$ nv set vrf blue router bgp route-reflection cluster-id 10.10.10.5
cumulus@leaf01:~$ nv set vrf blue router bgp route-reflection reflect-between-clients disabled
cumulus@leaf01:~$ nv config apply
```

{{< /tab >}}
{{< tab "vtysh Commands ">}}

The following example configures a BGP route reflector with cluster-id 10.10.10.5. BGP client-to-client reflection is enabled by default.

```
cumulus@leaf01:~$ sudo vtysh
...
leaf01# configure terminal
leaf01(config)# router bgp 65011 vrf blue
leaf01(config-router)# bgp cluster-id 10.10.10.5
leaf01(config-router)# end
leaf01# write memory
leaf01# exit
```

The vtysh commands save the configuration in the `/etc/frr/frr.conf` file. For example:

```
cumulus@leaf01:~$ sudo cat /etc/frr/frr.conf
...
router bgp 65011 vrf blue
bgp router-id 6.0.0.10
bgp cluster-id 10.10.10.5
!
address-family ipv4 unicast
  maximum-paths 64
  maximum-paths ibgp 64
exit-address-family
exit
!
...
```

The following example configures a BGP route reflector with cluster-id 10.10.10.5 and disables client-to-client reflection:

```
cumulus@leaf01:~$ sudo vtysh
...
leaf01# configure terminal
leaf01(config)# router bgp 65011 vrf blue
leaf01(config-router)# bgp cluster-id 10.10.10.5
leaf01(config-router)# no bgp client-to-client reflection
leaf01(config-router)# end
leaf01# write memory
leaf01# exit
```

The vtysh commands save the configuration in the `/etc/frr/frr.conf` file. For example:

```
cumulus@leaf01:~$ sudo cat /etc/frr/frr.conf
...
!
router bgp 65011 vrf blue
bgp router-id 6.0.0.10
no bgp client-to-client reflection
bgp cluster-id 10.10.10.5
!
address-family ipv4 unicast
  maximum-paths 64
  maximum-paths ibgp 64
exit-address-family
exit
!
...
```

{{< /tab >}}
{{< /tabs >}}

{{%notice info%}}
- When you configure BGP for IPv6, you must run the `route-reflector-client` command **after** the `activate` command.
- You can only configure a BGP node as a route reflector for an iBGP peer.
{{%/notice%}}

## BGP Confederations

To reduce the number of iBGP peerings, configure a confederation to divide an <span class="a-tooltip">[AS](## "autonomous system")</span> into smaller <span class="a-tooltip">[sub-ASs](## "sub-autonomous systems")</span>.

To configure a BGP confederation:
- Provide the configuration ID you want to use.
- Provide the ASNs of the peers you want to add to the confederation.

{{%notice note%}}
Changing BGP confederation configuration results in BGP session flaps, which might lead to traffic loss.
{{%/notice%}}

The following example configures confederation ID 2 with sub-ASs 65101, 65102, 65103, and 65104.

{{< tabs "1708 ">}}
{{< tab "NVUE Commands ">}}

```
cumulus@spine01:~$ nv set vrf default router bgp confederation id 2
cumulus@spine01:~$ nv set vrf default router bgp confederation member-as 65101-65104
cumulus@spine01:~$ nv config apply
```

{{< /tab >}}
{{< tab "vtysh Commands ">}}

```
cumulus@leaf01:~$ sudo vtysh
...
spine01# configure terminal
spine01(config)# router bgp 65199
spine01(config-router)# bgp confederation identifier 2
spine01(config-router)# bgp confederation peers 65101
spine01(config-router)# bgp confederation peers 65102
spine01(config-router)# bgp confederation peers 65103
spine01(config-router)# bgp confederation peers 65104
spine01(config-router)# end
spine01# write memory
spine01# exit
```

The vtysh commands save the configuration in the `/etc/frr/frr.conf` file. For example:

```
cumulus@spine01:~$ sudo cat /etc/frr/frr.conf
...
router bgp 65199
 bgp router-id 10.10.10.101
 bgp confederation identifier 2
 bgp confederation peers 65101 65102 65103 65104
...
```

{{< /tab >}}
{{< /tabs >}}

## Administrative Distance

Cumulus Linux uses the administrative distance to choose which routing protocol to use when two different protocols provide route information for the same destination. The smaller the distance, the more reliable the protocol. For example, if the switch receives a route from OSPF with an administrative distance of 110 and the same route from BGP with an administrative distance of 100, the switch chooses BGP.

The following example commands set the administrative distance for external routes to 150 and internal routes to 110:

{{< tabs "1756 ">}}
{{< tab "NVUE Commands ">}}

```
cumulus@spine01:~$ nv set vrf default router bgp address-family ipv4-unicast admin-distance external 150
cumulus@spine01:~$ nv set vrf default router bgp address-family ipv4-unicast admin-distance internal 110
cumulus@spine01:~$ nv config apply
```

{{< /tab >}}
{{< tab "vtysh Commands ">}}

```
cumulus@spine01:~$ sudo vtysh
...
spine01# configure terminal
spine01(config)# router bgp 65101
spine01(config-router)# distance bgp 150 110
spine01(config-router)# end
spine01# write memory
spine01# exit
```

{{< /tab >}}
{{< /tabs >}}

## BGP Neighbor Shutdown

You can shut down all active BGP sessions with a neighbor and remove all associated routing information without removing its associated configuration. When shut down, the neighbor goes into an administratively idle state.

{{< tabs "1786 ">}}
{{< tab "NVUE Commands ">}}

```
cumulus@leaf01:~$ nv set vrf default router bgp neighbor swp51 shutdown on
cumulus@leaf01:~$ nv config apply
```

To bring BGP sessions with the neighbor back up, run the `nv set vrf default router bgp neighbor swp51 shutdown off` command.

{{< /tab >}}
{{< tab "vtysh Commands ">}}

```
cumulus@spine01:~$ sudo vtysh
...
spine01# configure terminal
spine01(config)# router bgp 65101
spine01(config-router)# neighbor swp51 shutdown
spine01(config-router)# end
spine01# write memory
spine01# exit
```

The vtysh commands save the configuration in the `/etc/frr/frr.conf` file. For example:

```
...
router bgp 65199
  ...
  neighbor swp51 shutdown
...
```

To bring BGP sessions with the neighbor back up, run the `no neighbor swp51 shutdown` command.

{{< /tab >}}
{{< /tabs >}}

## Graceful BGP Shutdown

To reduce packet loss during planned switch or link maintenance, you can configure graceful BGP shutdown globally, on a peer group, or on a specific peer.

{{%notice note%}}
Graceful shutdown is active for a peer if you enable it at any level; globally, on the peer group, **or** on the specific peer.
Graceful shutdown is **not** active for a peer if you disable it on all levels; globally, on the peer group **and** on the specific peer.
{{%/notice%}}

### Global Graceful BGP Shutdown

When you enable graceful shutdown globally on the switch, Cumulus Linux adds the `graceful-shutdown` community to all inbound and outbound routes from all eBGP peers and sets the `local-pref` for the routes to `0` (refer to {{<exlink url="https://datatracker.ietf.org/doc/html/rfc8326" text="RFC8326">}}).

{{< tabs "1837 ">}}
{{< tab "NVUE Commands ">}}

To enable graceful shutdown globally on the switch:

```
cumulus@leaf01:~$ nv set router bgp graceful-shutdown on
cumulus@leaf01:~$ nv config apply
```

To disable graceful shutdown globally on the switch:

```
cumulus@leaf01:~$ nv set router bgp graceful-shutdown off
cumulus@leaf01:~$ nv config apply
```

{{< /tab >}}
{{< tab "vtysh Commands ">}}

To enable graceful shutdown globally:

```
cumulus@leaf01:~$ sudo vtysh
...
leaf01# configure terminal
leaf01(config)# router bgp 65101
leaf01(config-router)# bgp graceful-shutdown
leaf01(config-router)# end
leaf01# write memory
leaf01# exit
```

To disable graceful shutdown globally on the switch:

```
cumulus@leaf01:~$ sudo vtysh
...
leaf01# configure terminal
leaf01(config)# router bgp 65101
leaf01(config-router)# no bgp graceful-shutdown
leaf01(config-router)# end
leaf01# write memory
leaf01# exit
```

{{< /tab >}}
{{< /tabs >}}

To show the configuration, run the vtysh `show ip bgp <route>` command. For example:

```
cumulus@leaf01:~$ sudo vtysh
leaf01# show ip bgp 10.10.10.0/24
BGP routing table entry for 10.10.10.0/24
Paths: (2 available, best #1, table Default-IP-Routing-Table)
  Advertised to non peer-group peers:
  bottom0(10.10.10.2)
  30 20
    10.10.10.2 (metric 10) from top1(10.10.10.2) (10.10.10.2)
      Origin IGP, localpref 100, valid, internal, bestpath-from-AS 30, best
      Community: 99:1
      AddPath ID: RX 0, TX 52
      Last update: Mon Sep 18 17:01:18 2017

  20
    10.10.10.3 from bottom0(10.10.10.32) (10.10.10.10)
      Origin IGP, metric 0, localpref 0, valid, external, bestpath-from-AS 20
      Community: 99:1 graceful-shutdown
      AddPath ID: RX 0, TX 2
      Last update: Mon Sep 18 17:01:18 2017
```

As optional configuration, you can create a route map to prepend the AS so that reduced preference using a longer AS path propagates to other parts of network.

{{< expand "Example Configuration Using a Route Map" >}}

```
router bgp 65101
 bgp router-id 10.10.10.1
 bgp graceful-restart
 bgp bestpath as-path multipath-relax
 neighbor fabric peer-group
 neighbor swp51 interface remote-as external

 address-family ipv4 unicast
  redistribute connected
  neighbor swp51 route-map prependas out
 exit-address-family

bgp community-list standard gshut seq 5 permit graceful-shutdown

route-map prependas permit 10
 match community gshut exact-match
 set as-path prepend 65101

route-map prependas permit 20
```

With the above configuration, the peer sees:

```
cumulus@spine01:~$ sudo vtysh
...
spine01# show ip bgp 10.10.10.1/32
BGP routing table entry for 10.10.10.1/32
Paths: (1 available, best #1, table default)
Advertised to non peer-group peers:
65101 65101
10.10.10.1 from leaf01(10.10.10.1) (10.10.10.1)
Origin incomplete, metric 0, localpref 0, valid, external, bestpath-from-AS 65101, best (First path received)
Community: graceful-shutdown
Last update: Sun Dec 20 03:04:53 2020
```

{{< /expand >}}

### Graceful BGP Shutdown on a Peer

When you enable BGP graceful shutdown on a peer, Cumulus Linux attaches a `graceful-shutdown` community to the relevant routes. Neighbors receiving the `graceful-shutdown` community mark these routes as less preferred if alternative routes exist. If no other routes are available, neighbors continue to use the routes with the `graceful-shutdown` community. If you enable graceful shutdown (maintenance) in multiple parts of the network or where there are no additional routes, traffic does not stop on the routes that have the attached `graceful-shutdown` community.

{{< tabs "1962 ">}}
{{< tab "NVUE Commands ">}}

To enable graceful shutdown on a peer, run the `nv set vrf <vrf-id> router bgp neighbor <neighbor> graceful-shutdown on` command:

```
cumulus@leaf01:~$ nv set vrf default router bgp neighbor swp51 graceful-shutdown on
cumulus@leaf01:~$ nv config apply
```

To disable graceful shutdown on a peer, run the `nv unset vrf <vrf-id> router bgp neighbor <neighbor> graceful-shutdown` command:

```
cumulus@leaf01:~$ nv unset vrf default router bgp neighbor swp51 graceful-shutdown
cumulus@leaf01:~$ nv config apply
```

{{< /tab >}}
{{< tab "vtysh Commands ">}}

To enable graceful shutdown on a peer:

```
cumulus@leaf01:~$ sudo vtysh
...
leaf01# configure terminal
leaf01(config)# router bgp 65101
leaf01(config-router)# neighbor swp51 graceful-shutdown
leaf01(config-router)# end
leaf01# write memory
leaf01# exit
```

To disable graceful shutdown on a peer:

```
cumulus@leaf01:~$ sudo vtysh
...
leaf01# configure terminal
leaf01(config)# router bgp 65101
leaf01(config-router)# neighbor swp51 no graceful-shutdown
leaf01(config-router)# end
leaf01# write memory
leaf01# exit
```

{{< /tab >}}
{{< /tabs >}}

To show if graceful shutdown is enabled on a peer, run the `nv show vrf <vrf-id> router bgp neighbor <neighbor>` command:

```
cumulus@leaf01:~$ nv show vrf default router bgp neighbor swp51
                               operational                applied                                
-----------------------------  -------------------------  ---------------------------------------
password                                                  $nvsec$d1a028e8c7f97db92876c2a30fcc403f
enforce-first-as                                          enabled                                
passive-mode                                              disabled                               
nexthop-connected-check                                   enabled                                
description                                               none                                   
graceful-shutdown                                         disabled                               
...
```

### Graceful BGP Shutdown on a Peer Group

When you enable BGP graceful shutdown on a peer group, Cumulus Linux attaches a `graceful-shutdown` community to the relevant routes. Neighbors receiving the `graceful-shutdown` community mark these routes as less preferred if alternative routes exist. If no other routes are available, neighbors continue to use the routes with the `graceful-shutdown` community. If you enable graceful shutdown (maintenance) in multiple parts of the network or where there are no additional routes, traffic does not stop on the routes that have the attached `graceful-shutdown` community.

{{< tabs "2037 ">}}
{{< tab "NVUE Commands ">}}

To enable graceful shutdown on a peer group, run the `nv set vrf <vrf-id> router bgp peer-group <peer-group-id> graceful-shutdown on` command:

```
cumulus@leaf01:~$ nv set vrf default router bgp peer-group underlay graceful-shutdown on
cumulus@leaf01:~$ nv config apply
```

To disable graceful shutdown on a peer group, run the `nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> graceful-shutdown` command:

```
cumulus@leaf01:~$ nv unset vrf default router bgp peer-group underlay graceful-shutdown
cumulus@leaf01:~$ nv config apply
```

{{< /tab >}}
{{< tab "vtysh Commands ">}}

To enable graceful shutdown on a peer group:

```
cumulus@leaf01:~$ sudo vtysh
...
leaf01# configure terminal
leaf01(config)# router bgp 65101
leaf01(config-router)# neighbor underlay graceful-shutdown
leaf01(config-router)# end
leaf01# write memory
leaf01# exit
```

To disable graceful shutdown on a peer group:

```
cumulus@leaf01:~$ sudo vtysh
...
leaf01# configure terminal
leaf01(config)# router bgp 65101
leaf01(config-router)# neighbor underlay no graceful-shutdown
leaf01(config-router)# end
leaf01# write memory
leaf01# exit
```

{{< /tab >}}
{{< /tabs >}}

To show if graceful shutdown is `on` a peer group, run the `nv show vrf <vrf-id> router bgp peer-group <peer-group-id>` command:

```
cumulus@leaf01:~$ nv show vrf default router bgp peer-group underlay
                               operational  applied                                                                  
-----------------------------  -----------  ---------------------------------------
password                                    $nvsec$d1a028e8c7f97db92876c2a30fcc403f
enforce-first-as                            enabled                               
passive-mode                                disabled                             
nexthop-connected-check                     enabled                              
description                                 none                                 
graceful-shutdown                           disabled                             
ttl-security                                                                     
  state                                     disabled                             
local-as                                                                         
  state                                     disabled                             
timers                                                                           
  keepalive                                 auto                                 
  hold                                      auto                                 
  connection-retry                          auto                                 
  route-advertisement                       auto                                 
address-family                                                                   
  ipv4-unicast                                                                   
    state                                   enabled                              
    route-reflector-client                  disabled                             
    soft-reconfiguration                    disabled                             
    nexthop-setting                         auto                                 
    add-path-tx                             off                                  
    attribute-mod                                                                
      aspath                                disabled                             
      med                                   disabled                             
      nexthop                               disabled                             
    aspath                                                                       
      replace-peer-as                       disabled                             
      private-as                            none                                 
      allow-my-asn                                                                                                          
        state      
...
```

## Graceful BGP Restart

When BGP restarts on a switch, all BGP peers detect that the session goes down and comes back up. This session transition results in a routing flap on BGP peers that causes BGP to recompute routes, generate route updates, and add unnecessary churn to the forwarding tables. The routing flaps can create transient forwarding blackholes and loops, and also consume resources on the switches affected by the flap, which can affect overall network performance.

To minimize the negative effects that occur when BGP restarts, Cumulus Linux enables graceful BGP restart by default, which lets a BGP speaker signal to its peers that it can preserve its forwarding state and continue data forwarding during a restart. BGP graceful restart also enables a BGP speaker to continue to use routes announced by a peer even after the peer has gone down.

When BGP establishes a session, BGP peers use the BGP OPEN message to negotiate a graceful restart. If the BGP peer also supports graceful restart, it activates for that neighbor session. If the BGP session stops, the BGP peer (the restart helper) flags all routes associated with the device as stale but continues to forward packets to these routes for a certain period of time. The restarting device also continues to forward packets during the graceful restart. After the device comes back up and establishes BGP sessions again with its peers (restart helpers), it waits to learn all routes that these peers announce before selecting a cumulative path; after which, it updates its forwarding tables and re-announces the appropriate routes to its peers. These procedures ensure that if there are any routing changes while the BGP speaker is restarting, the network converges.

{{%notice note%}}
- For warm boot to restart the switch with no interruption to traffic for existing route entries, you must enable BGP graceful restart in all BGP VRFs.
- BGP graceful restart only supports eBGP direct and multihop peering. VRF leaking is not gracefully handled and traffic to destinations through these routes might drop while graceful restart is in progress.
{{%/notice%}}

### Restart Modes

Cumulus Linux supports graceful BGP restart full mode and helper-only mode for IPv4, IPv6 and EVPN. The default setting is helper-only mode.
- In full mode, the switch is in both a helper and restarter role.
- In helper-only mode, the switch is in a helper role only, where routes originated and advertised from a BGP peer are not deleted.

You can configure graceful BGP restart globally, where all BGP peers inherit the graceful restart capability, or for a BGP peer or peer group (useful for misbehaving peers or when working with third party devices).

{{%notice note%}}
- BGP goes through a graceful restart (as a restarting router) with a planned switch restart event that ISSU initiates. Any other time BGP restarts, such as when the BGP daemon restarts due to a software exception, or you restart the FRR service, BGP goes through a regular restart where the BGP session with peers terminates and Cumulus Linux removes the learned routes from the forwarding plane.
- Changing graceful restart mode results in BGP session flaps, which might lead to traffic loss.
{{%/notice%}}

{{< tabs "TabID2130 ">}}
{{< tab "NVUE Commands ">}}

The switch has graceful restart enabled in helper-only mode by default. To set graceful BGP restart to full mode globally on the switch:

```
cumulus@leaf01:~$ nv set router bgp graceful-restart mode full
cumulus@leaf01:~$ nv config apply
```

To set graceful BGP restart to full mode on the BGP peer connected on swp51:

```
cumulus@leaf01:~$ nv set vrf default router bgp neighbor swp51 graceful-restart mode full
cumulus@leaf01:~$ nv config apply
```

To set graceful BGP restart back to the default setting (helper-only mode), run the `nv unset router bgp graceful-restart` command or the `nv set router bgp graceful-restart mode helper-only` command.

{{< /tab >}}
{{< tab "vtysh Commands ">}}

The switch has graceful restart enabled in helper-only mode by default. To set graceful BGP restart to full mode globally on the switch:

```
cumulus@leaf01:~$ sudo vtysh
...
leaf01# configure terminal
leaf01(config)# router bgp 65101
leaf01(config-router)# bgp graceful-restart
leaf01(config-router)# end
leaf01# write memory
leaf01# exit
```

To set graceful BGP restart to full mode on the BGP peer connected on swp51:

```
cumulus@leaf01:~$ sudo vtysh
...
leaf01# configure terminal
leaf01(config)# router bgp 65101
leaf01(config-router)# neighbor swp51 graceful-restart
leaf01(config-router)# end
leaf01# write memory
leaf01# exit
```

To set graceful BGP restart back to the default setting (helper-only mode), run the `no bgp graceful-restart` command or the `no neighbor <interface-id> graceful-restart` command

{{< /tab >}}
{{< /tabs >}}

### Disable Graceful Restart

{{%notice info%}}
If you disable graceful BGP restart, you cannot achieve a switch restart or switch software upgrade with minimal traffic loss in a BGP configuration. Refer to {{<link url="Upgrading-Cumulus-Linux/#issu" text="ISSU">}} for more information.
{{%/notice%}}

{{< tabs "TabID2189 ">}}
{{< tab "NVUE Commands ">}}

To disable graceful BGP restart globally on the switch:

```
cumulus@leaf01:~$ nv set router bgp graceful-restart mode off
cumulus@leaf01:~$ nv config apply
```

To disable graceful BGP restart on a BGP peer:

```
cumulus@leaf01:~$ nv unset vrf default router bgp neighbor swp51 graceful-restart
cumulus@leaf01:~$ nv config apply
```

{{< /tab >}}
{{< tab "vtysh Commands ">}}

To disable graceful BGP restart globally on the switch:

```
cumulus@leaf01:~$ sudo vtysh
...
leaf01# configure terminal
leaf01(config)# router bgp 65101
leaf01(config-router)# bgp graceful-restart-disable
leaf01(config-router)# end
leaf01# write memory
leaf01# exit
```

To disable graceful BGP restart on a BGP peer:

```
cumulus@leaf01:~$ sudo vtysh
...
leaf01# configure terminal
leaf01(config)# router bgp 65101
leaf01(config-router)# neighbor swp51 graceful-restart-disable
leaf01(config-router)# end
leaf01# write memory
leaf01# exit
```

{{< /tab >}}
{{< /tabs >}}

### Restart Timers

You can configure the following graceful BGP restart timers.

{{< tabs "TabID2242 ">}}
{{< tab "NVUE Commands ">}}

|<div style="width:250px">Timer | Description |
| ---- | ----------- |
| `restart-time` | The number of seconds to wait for a graceful restart capable peer to re-establish BGP peering. You can set a value between 0 and 4095. The default is 120 seconds.|
| `pathselect-defer-time` | The number of seconds a restarting peer defers path-selection when waiting for the EOR marker from peers. You can set a value between 0 and 120. The default is 120 seconds. |
| `stalepath-time` | The number of seconds to hold stale routes for a restarting peer. You can set a value between 1 and 4095. The default is 360 seconds.|

{{%notice note%}}
To avoid traffic loss during warm boot in an EVPN multihoming configuration with multihop BGP sessions, increase the `restart-time` timer to more than 180 seconds on all multihoming configured switches.
{{%/notice%}}

The following example commands set the `restart-time` to 400 seconds, `pathselect-defer-time` to 300 seconds, and `stalepath-time` to 400 seconds:

```
cumulus@leaf01:~$ nv set router bgp graceful-restart restart-time 400
cumulus@leaf01:~$ nv set router bgp graceful-restart path-selection-deferral-time 300
cumulus@leaf01:~$ nv set router bgp graceful-restart stale-routes-time 400
cumulus@leaf01:~$ nv config apply
```

{{< /tab >}}
{{< tab "vtysh Commands ">}}

|<div style="width:250px">Timer | Description |
| ---- | ----------- |
| `notification` | Enables graceful BGP restart support for BGP NOTIFICATION messages.|
| `preserve-fw-state` | Sets the F-bit indication to preserve the FIB during a graceful BPG restart. |
| `restart-time` | The number of seconds to wait for a graceful restart capable peer to re-establish BGP peering. You can set a value between 1 and 4095. The default is 120 seconds. |
|  `rib-stale-time` |  The stale route removal time in the RIB (in seconds). You can set a value between 1 and 3600. |
| `select-defer-time` | The number of seconds a restarting peer defers path-selection when waiting for the EOR marker from peers. You can set a value between 0 and 3600. The default is 360 seconds. |
| `stalepath-time` | The number of seconds to hold stale routes for a restarting peer. You can set a value between 1 and 4095. The default is 360 seconds.|

The following example commands set the `restart-time` to 400 seconds, `pathselect-defer-time` to 300 seconds, and `stalepath-time` to 400 seconds:

```
cumulus@leaf01:~$ sudo vtysh
...
leaf01# configure terminal
leaf01(config)# router bgp 65101
leaf01(config-router)# bgp graceful-restart restart-time 400
leaf01(config-router)# bgp graceful-restart select-defer-time 300
leaf01(config-router)# bgp graceful-restart stalepath-time 400
leaf01(config-router)# end
leaf01# write memory
leaf01# exit
```

The vtysh commands save the configuration in the `/etc/frr/frr.conf` file. For example:

```
...
router bgp 65199
 bgp router-id 10.10.10.101
 neighbor swp51 remote-as external
 bgp graceful-restart restart-time 400
 bgp graceful-restart select-defer-time 300
 bgp graceful-restart stalepath-time 400
...
```

{{< /tab >}}
{{< /tabs >}}

### Show Graceful Restart Information

To show global graceful BGP restart configuration settings, run the NVUE `nv show router bgp graceful-restart` command:

```
cumulus@leaf01:mgmt:~$ nv show router bgp graceful-restart 
                              applied      pending    
----------------------------  -----------  -----------
mode                          helper-only  helper-only
restart-time                  120          120        
path-selection-deferral-time  360          360        
stale-routes-time             360          360
```

To show graceful BGP restart information on a specific BGP peer, run the vtysh `show ip bgp neighbor <neighbor> graceful-restart` command.

```
cumulus@leaf01:mgmt:~$ sudo vtysh
...
leaf01# show ip bgp neighbor swp51 graceful-restart
Codes: GR - Graceful Restart, * -  Inheriting Global GR Config,
       Restart - GR Mode-Restarting, Helper - GR Mode-Helper,
       Disable - GR Mode-Disable.

BGP neighbor on swp51: fe80::4638:39ff:fe00:2, remote AS 65199, local AS 65101, external link
  BGP state = Established, up for 00:15:54
  Neighbor GR capabilities:
    Graceful Restart Capability: advertised and received
      Remote Restart timer is 120 seconds
      Address families by peer:
        none
  Graceful restart information:
    End-of-RIB send: IPv4 Unicast
    End-of-RIB received: IPv4 Unicast
    Local GR Mode: Helper*
    Remote GR Mode: Helper
    R bit: False
    Timers:
      Configured Restart Time(sec): 120
      Received Restart Time(sec): 120
    IPv4 Unicast:
      F bit: False
      End-of-RIB sent: Yes
      End-of-RIB sent after update: Yes
      End-of-RIB received: Yes
      Timers:
        Configured Stale Path Time(sec): 360
```
<!-- vale off -->
## Enable Read-only Mode
<!-- vale on -->
Sometimes, as Cumulus Linux establishes BGP peers and receives updates, it installs prefixes in the RIB and advertises them to BGP peers before receiving and processing information from all the peers. Also, depending on the timing of the updates, Cumulus Linux sometimes installs prefixes, then withdraws and replaces them with new routing information. Read-only mode minimizes this BGP route churn in both the local RIB and with BGP peers.

Enable read-only mode to reduce CPU and network usage when restarting the BGP process. Because intermediate best paths are possible for the same prefix as peers establish and start receiving updates at different times, read-only mode is useful in topologies where BGP learns a prefix from a large number of peers and the network has a high number of prefixes.

{{%notice note%}}
While in read-only mode, BGP does not run best-path or generate any updates to its peers.
{{%/notice%}}

The following example commands enable read-only mode:

{{< tabs "2368 ">}}
{{< tab "NVUE Commands ">}}

```
cumulus@leaf01:~$ nv set router bgp convergence-wait time 300
cumulus@leaf01:~$ nv set router bgp convergence-wait establish-wait-time 200
cumulus@leaf01:~$ nv config apply
```

{{< /tab >}}
{{< tab "vtysh Commands ">}}

```
cumulus@leaf01:~$ sudo vtysh
...
leaf01# configure terminal
leaf01(config)# router bgp
leaf01(config-router)# update-delay 300 90
leaf01(config-router)# end
leaf01# write memory
leaf01# exit
```

The vtysh commands save the configuration in the `/etc/frr/frr.conf` file. For example:

```
...
router bgp 65199
 bgp router-id 10.10.10.101
 neighbor swp51 remote-as external
 bgp update-delay 300 200
...
```

{{< /tab >}}
{{< /tabs >}}

To show the configured timers and information about the transitions when a convergence event occurs, run the vtysh `show ip bgp summary` command.

```
cumulus@leaf01:mgmt:~$ sudo vtysh
...
leaf01# show ip bgp summary
ipv4 Unicast Summary

BGP router identifier 10.10.10.1, local AS number 65101 vrf-id 0
Read-only mode update-delay limit: 300 seconds
                   Establish wait: 200 seconds
BGP table version 0
RIB entries 3, using 576 bytes of memory
Peers 1, using 21 KiB of memory

Neighbor        V         AS   MsgRcvd   MsgSent   TblVer  InQ OutQ  Up/Down State/PfxRcd   PfxSnt
spine01(swp51)  4      65199     30798     30802        0    0    0 1d01h09m            0        0

Total number of neighbors 1
...
```

The vtysh `show ip bgp summary json` command shows the last convergence event.

## BGP Community Lists
<!-- vale off -->
You can use *{{<exlink url="http://docs.frrouting.org/en/latest/bgp.html#community-lists" text="community lists">}}* to define a BGP community to tag one or more routes. You can then use the communities to apply a route policy on either egress or ingress.
<!-- vale on -->
The BGP community list can be either *standard*, *extended*, or *large*. The standard BGP community list is a pair of values (such as *100:100*) that you can tag on a specific prefix and advertise to other neighbors, or you can apply them on route ingress. The standard BGP community list can be one of four BGP default communities:

- *0:0*: a BGP community that matches all routes. This value replaces `internet` used in Cumulus Linux 5.13 and earlier.
- *local-AS*: a BGP community that restricts routes to your confederation's sub-AS.
- *no-advertise*: a BGP community that is not advertised to anyone.
- *no-export*: a BGP community that is not advertised to the eBGP peer.

An extended BGP community list takes a regular expression of communities and matches the listed communities.

A large community-list accommodates more identification information, including 4-byte AS numbers. BGP enables large communities by default. To disable large communities, run the `nv set vrf <vrf-id> router bgp neighbor <neighbor> address-family <address-family> community-advertise large off` command or the `nv set vrf <vrf-id> router bgp peer-group <peer-group> address-family <address-family> community-advertise large off` command.

When the neighbor receives the prefix, it examines the community value and takes action accordingly, such as permitting or denying the community member in the routing policy.

{{%notice note%}}
If you include a comma in the BGP community list, extended community list, or large community list regex expression of a routing policy, you see error messages and FRR reload fails. Make sure the regex expression does not contain a comma.
{{%/notice%}}

The following example configures a standard community list filter:

{{< tabs "2448 ">}}
{{< tab "NVUE Commands ">}}

```
cumulus@leaf01:~$ nv set router policy community-list COMMUNITY1 rule 10 action permit
cumulus@leaf01:~$ nv set router policy community-list COMMUNITY1 rule 10 community 100:100
cumulus@leaf01:~$ nv config apply
```

{{< /tab >}}
{{< tab "vtysh Commands ">}}

```
cumulus@leaf01:~$ sudo vtysh
...
leaf01# configure terminal
leaf01(config)# bgp community-list standard COMMUNITY1 permit 100:100
leaf01(config)# exit
leaf01# write memory
leaf01# exit
```

{{< /tab >}}
{{< /tabs >}}

To apply the community list to a route map to define the routing policy:

{{< tabs "2475">}}
{{< tab "NVUE Commands ">}}

```
cumulus@leaf01:~$ nv set router policy route-map ROUTEMAP1 rule 10 match community-list COMMUNITY1
cumulus@leaf01:~$ nv set router policy route-map ROUTEMAP1 rule 10 action permit
cumulus@leaf01:~$ nv config apply
```

{{< /tab >}}
{{< tab "vtysh Commands ">}}

```
cumulus@leaf01:~$ sudo vtysh
...
leaf01# configure terminal
leaf01(config)# route-map ROUTEMAP1 
leaf01(config-route-map)# match community COMMUNITY1
leaf01(config-route-map)# end
leaf01# write memory
leaf01# exit
```

{{< /tab >}}
{{< /tabs >}}

The following example configures a BGP extended community <span class="a-tooltip">[RT](## "route target")</span> filter and applies the extended community list to a route map.

{{< tabs "2503">}}
{{< tab "NVUE Commands ">}}

```
cumulus@leaf01:~$ nv set router policy ext-community-list EXTCOMM1 rule 10 ext-community rt 11:11,22:22
cumulus@leaf01:~$ nv set router policy ext-community-list EXTCOMM1 rule 10 action permit
cumulus@leaf01:~$ nv set router policy route-map ROUTEMAP1 rule 10 match ext-community-list EXTCOMM1
cumulus@leaf01:~$ nv set router policy route-map ROUTEMAP1 rule 10 action permit
cumulus@leaf01:~$ nv config apply
```

{{< /tab >}}
{{< tab "vtysh Commands ">}}

```
cumulus@leaf01:~$ sudo vtysh
...
leaf01# configure terminal
leaf01(config)# bgp extcommunity standard EXTCOMM1 permit rt 11:11 rt 22:22
leaf01(config)# route-map ROUTEMAP1 permit 10
leaf01(config-route-map)# match extcommunity EXTCOMM1
leaf01(config-route-map)# end
leaf01# write memory
leaf01# exit
```

{{< /tab >}}
{{< /tabs >}}

The following example configures a BGP extended community <span class="a-tooltip">[RT](## "route target")</span> filter with a regex match and applies the extended community list to a route map.

{{< tabs "2534">}}
{{< tab "NVUE Commands ">}}

```
cumulus@leaf01:~$ nv set router policy ext-community-list EXTCOMM2 rule 10 ext-community rt "\.*_65000:2002_.*","\.*_89000:2002_.*"
cumulus@leaf01:~$ nv set router policy ext-community-list EXTCOMM2 rule 10 action permit
cumulus@leaf01:~$ nv set router policy  ROUTEMAP3 rule 10 match ext-community-list EXTCOMM2
cumulus@leaf01:~$ nv set router policy route-map ROUTEMAP3 rule 10 action permit
cumulus@leaf01:~$ nv config apply
```

{{< /tab >}}
{{< tab "vtysh Commands ">}}

```
cumulus@leaf01:~$ sudo vtysh
...
leaf01# configure terminal
leaf01(config)# bgp extcommunity expanded EXTCOMM2 permit rt "\.*_65000:2002_.*","\.*_89000:2002_.*"
leaf01(config)# route-map ROUTEMAP3 permit 10
leaf01(config-route-map)# match extcommunity EXTCOMM2
leaf01(config-route-map)# end
leaf01# write memory
leaf01# exit
```

{{< /tab >}}
{{< /tabs >}}

The following example configures a BGP extended community <span class="a-tooltip">[SOO](## "Site of Origin")</span> filter and applies the extended community list to a route map.

{{< tabs "2565">}}
{{< tab "NVUE Commands ">}}

```
cumulus@leaf01:~$ nv set router policy ext-community-list EXTCOMM1 rule 10 ext-community soo 66:66,77:77
cumulus@leaf01:~$ nv set router policy ext-community-list EXTCOMM1 rule 10 action permit
cumulus@leaf01:~$ nv set router policy route-map ROUTEMAP1 rule 10 match ext-community-list EXTCOMM1
cumulus@leaf01:~$ nv set router policy route-map ROUTEMAP1 rule 10 action permit
cumulus@leaf01:~$ nv config apply
```

{{< /tab >}}
{{< tab "vtysh Commands ">}}

```
cumulus@leaf01:~$ sudo vtysh
...
leaf01# configure terminal
leaf01(config)# bgp extcommunity standard EXTCOMM2 permit soo 66:66 soo 77:77
leaf01(config)# route-map ROUTEMAP1 permit 10
leaf01(config-route-map)# match extcommunity EXTCOMM2
leaf01(config)# end
leaf01# write memory
leaf01# exit
```

{{< /tab >}}
{{< /tabs >}}

The following example configures a BGP extended community <span class="a-tooltip">[SOO](## "Site of Origin")</span> filter with a regex match and applies the extended community list to a route map.

{{< tabs "2596">}}
{{< tab "NVUE Commands ">}}

```
cumulus@leaf01:~$ nv set router policy ext-community-list EXTCOMM2 rule 10 ext-community soo "\.*_65000:2002_.*","\.*_89000:2002_.*"
cumulus@leaf01:~$ nv set router policy ext-community-list EXTCOMM2 rule 10 action permit
cumulus@leaf01:~$ nv set router policy route-map ROUTEMAP20 rule 10 match ext-community-list EXTCOMM2
cumulus@leaf01:~$ nv set router policy route-map ROUTEMAP20 rule 10 action permit
cumulus@leaf01:~$ nv config apply
```

{{< /tab >}}
{{< tab "vtysh Commands ">}}

```
cumulus@leaf01:~$ sudo vtysh
...
leaf01# configure terminal
leaf01(config)# bgp extcommunity expanded EXTCOMM2 permit soo "\.*_65000:2002_.*","\.*_89000:2002_.*"
leaf01(config)# route-map ROUTEMAP20 permit 10
leaf01(config-route-map)# match extcommunity EXTCOMM2
leaf01(config)# exit
leaf01# write memory
leaf01# exit
```

{{< /tab >}}
{{< /tabs >}}

{{%notice note%}}
To use a special character, such as a period (.) in the regular expression for an extended BGP community list, you must escape the character with a backslash (`\`). For example, `nv set router policy community-list COMMUNITY1 rule 10 community "\.*_65000:2002_.*"`.
{{%/notice%}}

The following example configures a BGP large community list and applies the large community list to a route map.

{{< tabs "TabID2631 ">}}
{{< tab "NVUE Commands">}}

```
cumulus@leaf01:~$ nv set router policy large-community-list 11 rule 10 action permit
cumulus@leaf01:~$ nv set router policy large-community-list 11 rule 10 large-community 4200857911:011:011
cumulus@leaf01:~$ nv set router policy route-map MAP1 rule 10 match large-community-list mylist
cumulus@leaf01:~$ nv set router policy route-map MAP1 rule 10 action permit
cumulus@leaf01:~$ nv config apply
```

{{< /tab >}}
{{< tab "vtysh Commands ">}}

```
cumulus@leaf01:~$ sudo vtysh
...
leaf01# configure terminal
leaf01(config)# bgp large-community-list 11 seq 10 permit 4200857911:011:011
leaf01(config)# route-map MAP1 permit 10
leaf01(config-route-map)# match large-community 11
leaf01(config-route-map)# end
leaf01# write memory
leaf01# exit
cumulus@leaf01:~$
```

{{< /tab >}}
{{< /tabs >}}

{{%notice note%}}
Cumulus Linux considers the full list of communities on a BGP route as a single string to evaluate. If you try to match `$` (ends with), Cumulus Linux matches the last community value in the list of communities, not the individual community values within the list.

For example, if you use the regular expression `".*:(20)$"`, Cumulus Linux matches all the BGP routes with a list of communities ending in 20.
- Routes with communities 45000:10 55000:40 65000:15000 123:20 match.
- Routes with communities 45000:10 55000:20 65000:15000 do **not** match.
{{%/notice%}}

## Related Information

- {{<exlink url="https://tools.ietf.org/html/rfc4360" text="RFC 4360, BGP Extended Communities Attribute">}}
- {{<exlink url="https://tools.ietf.org/html/rfc4456" text="RFC 4456, BGP Route Reflection - An Alternative to Full Mesh Internal BGP (iBGP)">}}
