---
title: Policy-based Routing
author: Cumulus Networks
weight: 18791
aliases:
 - /display/CL3740/Policy-based-Routing
 - /pages/viewpage.action?pageId=83629746698
pageID: 83629746698
product: Cumulus Linux
version: 3.7.7'4.0'
imgData: cumulus-linux-37740
siteSlug: cumulus-linux-37740
---
<details>

Typical routing systems and protocols forward traffic based on the
destination address in the packet, which is used to look up an entry in
a routing table. However, sometimes the traffic on your network requires
a more hands-on approach. You might need to forward a packet based on
the source address, the packet size, or other information in the packet
header.

Policy-based routing (PBR) lets you make routing decisions based on
filters that change the routing behavior of specific traffic so that you
can override the routing table and influence where the traffic goes. For
example, you can use PBR to help you reach the best bandwidth
utilization for business-critical applications, isolate traffic for
inspection or analysis, or manually load balance outbound traffic.

Policy-based routing is applied to incoming packets. All packets
received on a PBR-enabled interface pass through enhanced packet filters
that determine rules and specify where to forward the packets.

{{%notice note%}}

  - You can create a *maximum* of 255 PBR match rules and 256 next hop
    groups (this is the ECMP limit).

  - You can apply only one PBR policy per input interface.

  - You can match on *source* and *destination* IP address only.

  - PBR is not supported for GRE or VXLAN tunneling.

  - PBR is not supported on ethernet interfaces.

  - A PBR rule cannot contain both IPv4 and IPv6 addresses.

{{%/notice%}}

## <span>Configure PBR</span>

A PBR policy contains one or more policy maps. Each policy map:

  - Is identified with a unique map name and sequence number. The
    sequence number is used to determine the relative order of the map
    within the policy.

  - Contains a match source IP rule or a match destination IP rule, and
    a set rule.
    
      - To match on a source and destination address, a policy map can
        contain both match source and match destination IP rules.
    
      - A set rule determines the PBR next hop for the policy. The set
        rule can contain a single next hop IP address or it can contain a
        a next hop group. A next hop group has more than one next hop IP
        address so that you can use multiple interfaces to forward
        traffic. To use ECMP, you configure a next hop group.

To use PBR in Cumulus linux, you define a PBR policy and apply it to the
ingress interface (the interface must already have an IP address
assigned). Traffic is matched against the match rules in sequential
order and forwarded according to the set rule in the first match.
Traffic that does not match any rule is passed onto the normal
destination based routing mechanism.

{{%notice note%}}

For Tomahawk and Tomahawk+ platforms, you must configure the switch to
operate in non-atomic mode, which offers better scaling as all TCAM
resources are used to actively impact traffic. Add the line
`acl.non_atomic_update_mode = TRUE` to the `/etc/cumulus/switchd.conf`
file. For more information, see [Nonatomic Update Mode vs. Atomic Update
Mode](Netfilter---ACLs.html#src-83625636284_Netfilter-ACLs-nonatomic).

{{%/notice%}}

To configure a PBR policy:

1.  Configure the policy map with the `net add pbr-map <name> seq
    <1-700> match dst-ip|src-ip <ip/prefixlen>` command.  
   <summary>NCLU Commands </summary>

1.  Configure the policy map. The example commands below configure a
    policy map called `map1` with
    sequence number 1, that matches on
    destination address 10.1.2.0/24
    and source address 10.1.4.1/24.
    
        cumulus@switch:~$ net add pbr-map map1 seq 1 match dst-ip 10.1.2.0/24
        cumulus@switch:~$ net add pbr-map map1 seq 1 match src-ip 10.1.4.1/24
    
    {{%notice note%}}
    
    If the IP address in the rule is `0.0.0.0/0 or ::/0`, any IP address
    is a match. You cannot mix IPv4 and IPv6 addresses in a rule.
    
    {{%/notice%}}

2.  Either apply a *next hop* or a *next hop* group to the policy map:
  .  
      \- To apply a nexthop to the policy map, usehe example command below applies the ` next add pbr-map
        <name> seq <1-700> set nexthop <ipaddress> [<interface>]
        [nexthop-vrf <vrfname>]  `command.  
    hop 192.168.0.31 on
    the output interface swp2 and VRF `rocket` to the `map1` policy map.
    The output interface and VRF are optional, however, you *must*
        specify the VRF you want to use for resolution if the next hop is
        *not* in the default VRF.  
        The example command below applies the nexthop 192.168.0.31 on
        the output interface swp2 and VRF `rocket` to the `map1` policy
        map:
        
    
        cumulus@switch:~$ net add pbr-map map1 seq 1 set nexthop 192.168.0.31 swp2 nexthop-vrf rocket
    
      \- To apply a next hop group (for ECMP) to the policy map, first
        create the next hop group, then apply the group to the policy
        map:
        
        1.  C map.
    
    The example commands below create thea next hop group with the `net addcalled `group1`
    that contains the next hop-group
            <groupname> 192.168.0.21 on output interface swp1 and
    VRF `rocket`, and the next hop <ipaddress> [<interface>] [nexthop-vrf
            <vrfname>]` command.  
     192.168.0.22, then applies the next
    hop group `group1` to the `map1` policy map.
    
    {{%notice note%}}
    
    The output interface and VRF are optional. However, you must
            specify
    the VRF if the next hop is not in the default VRF.
    
            The example commands below create a nexthop group called
            `group1` that contains the nexthop 192.168.0.21 on outpu{{%/notice%}}
    
        cumulus@switch:~$ net add nexthop-group group1 nexthop 192.168.0.21 swp1 nexthop-vrf rocket
        cumulus@switch:~$ net add nexthop-group group1 nexthop 192.168.0.22
        cumulus@switch:~$ net add pbr-map map1 seq 1 set nexthop-group group1

3.  Assign the PBR policy to an ingress interface. The example command
    below assigns the PBR policy `map1` to interface swp51:
    
        cumulus@switch:~$ net add interface swp51 pbr-policy map1
        cumulus@switch:~$ net pending
        cumulus@switch:~$ net commit
    
        interface swp1 and VRF `rocket`, and the nexthop
            192.168.0.22.
            {{%notice note%}}
    
    You can only set one policy per interface.
    
    {{%/notice%}}

<summary>vtysh Commands </summary>

1.  Before you run the vtysh commands, you need to enable the `pbrd`
    service in the `/etc/frr/daemons` file, then restart FRR with the
    `systemctl restart frr.service` command.
    
        cumulus@leaf01:~$ sudo nano /etc/frr/daemons
        zebra=yes
        bgpd=yes
        ospfd=no
        ospf6d=no
        ripd=no
        ripngd=no
        isisd=no
        babeld=no
        pbrd=yes

2.  Configure the policy map. The example commands below configure a
    policy map called `map1` with sequence number 1, that matches on
    destination address 10.1.2.0/24 and source address 10.1.4.1/24.
    
        cumulus@switch:~$ sudo vtysh
         
       cumulus@switch:~$ net add  switch# configure terminal
        switch(config)# pbr-map map1 seq 1 
        switch(config-pbr-map)# match dst-ip 10.1.2.0/24
        switch(config-pbr-map)# match src-ip 10.1.4.1/24 
    
    {{%notice note%}}
    
    If the IP address in the rule is `0.0.0.0/0 or ::/0`, any IP address
    is a match. You cannot mix IPv4 and IPv6 addresses in a rule.
    
    {{%/notice%}}

3.  Either apply a *next hop-group group1* or a *next hop* group to the policy map.  
    \- The example command below applies the next hop 192.168.0.231 swp1 nexthop-vrf rocket
                cumulus@switch:~$ net addon
    the output interface swp2 and VRF `rocket` to the `map1` policy map.
    The output interface and VRF are optional, however, you *must*
    specify the VRF you want to use for resolution if the next hop-group group1 nexthop 192.168.0.22
        
        2.  A is
    *not* in the default VRF.
    
        switch(config-pbr-map)# set nexthop 192.168.0.31 swp2 nexthop-vrf rocket
        switch(config-pbr-map)# exit
        switch(config)# 
    
    \- To apply thea next hop group (for ECMP) to the policy map with, first
    create the `next add
      hop group, then apply the group to the policy map.  
    pbr-map <name> seq <1-700> setThe example commands below create a next hop- group <groupname>`
            command.  
            Tcalled `group1`
    that contains the next hop 192.168.0.21 on output interface swp1 and
    VRF `rocket`, and the nexample command belowt hop 192.168.0.22, then applies the next
    hop group `group1` to the `map1` policy map.
    
        to the `map1` policy map:
            {{%notice note%}}
    
    The output interface and VRF are optional. However, you must specify
    the VRF if the next hop is not in the default VRF.
    
            cumulus@switch:~$ net add pbr-map map1 seq 1 set nexthop-group group1

3.  Assign the PBR policy to an ingress interface with the `net add
    interface <interface> pbr-policy <name>` command.  
   {{%/notice%}}
    
        switch(config)# nexthop-group group1
        switch(config-nh-group)# nexthop 192.168.0.21 swp1 nexthop-vrf rocket
        switch(config-nh-group)# nexthop 192.168.0.22
        switch(config-nh-group)# exit
        switch(config)# pbr-map map1 seq 1 
        switch(config-pbr-map)# set nexthop-group group1
        switch(config-pbr-map)# exit
        switch(config)# 

4.  Assign the PBR policy to an ingress interface. The example command
    below assigns the PBR policy `map1` to interface
    swp51:
    
        cumulus@switch:~$ net add interface swp51 pbr-policy map1
        cumulus@switch:~$ net pendingswitch(config)# interface swp51
        switch(config-if)# pbr-policy map1
        switch(config-if)# end
        switch# write memory
        switch# exit
        cumulus@switch:~$ net commit
    
    {{%notice note%}}
    
    You can only set one policy per interface.
    
    {{%/notice%}}

The NCLU and vtysh commands save the configuration in the
`/etc/frr/frr.conf` file. For example:

    ...
    interface swp51
     pbr-policy map1
    ...
    nexthop-group group1
     nexthop 192.168.0.21 swp1 nexthop-vrf rocket
     nexthop 192.168.0.22
    ...
    pbr-map map1 seq 1
     match dst-ip 10.1.2.0/24
     match src-ip 0.0.0.0/0
     set nexthop nexthop-group group1
    ...

## <span>Configuration Example</span>

In the following example, the PBR-enabled switch has a PBR policy to
route all traffic from the Internet to a server that performs anti-DDOS.
The traffic returns to the PBR-enabled switch after being cleaned and is
then passed onto the regular destination based routing mechanism.

{{% imgOld 0 %}}

The configuration for the example above is:

<summary>NCLU Commands </summary>

    cumulus@switch:~$ net add pbr-map map1 seq 1 match src-ip 0.0.0.0/0
    cumulus@switch:~$ net add pbr-map map1 seq 1 set nexthop 192.168.0.32
    cumulus@switch:~$ net add interface swp51 pbr-policy map1
    cumulus@switch:~$ net pending
    cumulus@switch:~$ net commit

These commands produce the following snippet in the <summary>vtysh Commands </summary>

    cumulus@switch:~$ sudo vtysh
     
    switch# configure terminal
    switch(config)# pbr-map map1 seq 1 
    switch(config-pbr-map)# match src-ip 0.0.0.0/0
    switch(config-pbr-map)# set nexthop 192.168.0.32
    switch(config-pbr-map)# exit
    switch(config)# interface swp51
    switch(config-if)# pbr-policy map1
    switch(config-if)# end
    switch# write memory
    switch# exit
    cumulus@switch:~$ 

The NCLU and vtysh commands save the configuration in the
`/etc/frr/frr.conf`
 file.
 For example:

    ...
    interface swp51
     pbr-policy map1
    ...
    pbr-map map1 seq 1
     match src-ip 0.0.0.0/0
     set nexthop 192.168.0.32
    ...

## <span>Review Your Configuration</span>

Use the following commands to see the configured PBR policies.

To see the policies applied to all interfaces on the switch, userun the
NCLU `net show pbr interface` command or the vtysh `show pbr interface`
command. For example:

    cumulus@switch:~$ net show pbr interface
    swp55s3(67) with pbr-policy map1

To see the policies applied to a specific interface on the switch, add
the interface name at the end of the command; for example, `net show pbr
interface swp51` (or `show pbr interface swp51` in vtysh).

To see information about all policies, including mapped table and rule
numbers, userun the NCLU `net show pbr map` command or the vtysh `show pbr
map` command. If the rule is not set, you
 see a reason why.

    cumulus@switch:~$ net show pbr map
     pbr-map map1 valid: 1
      Seq: 700 rule: 999 Installed: 1(1) Reason: Valid
         SRC Match: 10.0.0.1/32
      nexthop 192.168.0.32
         Installed: 1(1) Tableid: 10003
      Seq: 701 rule: 1000 Installed: 1(2) Reason: Valid
         SRC Match: 90.70.0.1/32
      nexthop 192.168.0.32
         Installed: 1(1) Tableid: 10004

To see information about a specific policy, what it matches, and with
which interface it is associated, add the map name at the end of the
command; for example, `net show pbr map map1` (or `show pbr map map1` in
vtysh).

To see information about all next hop groups, run the NCLU `net show pbr
nexthop-group` command: or the vtysh `show pbr nexthop-group` command.

    cumulus@switch:~$ net show pbr nexthop-group
    Nexthop-Group: map1701 Table: 10004 Valid: 1 Installed: 1
    Valid: 1 nexthop 10.1.1.2
    Nexthop-Group: map1700 Table: 10003 Valid: 1 Installed: 1
    Valid: 1 nexthop 10.1.1.2
    Nexthop-Group: group1 Table: 10000 Valid: 1 Installed: 1
    Valid: 1 nexthop 192.168.10.0 bond1
    Valid: 1 nexthop 192.168.10.2
    Valid: 1 nexthop 192.168.10.3 vlan70
    Nexthop-Group: group2 Table: 10001 Valid: 1 Installed: 1
    Valid: 1 nexthop 192.168.8.1
    Valid: 1 nexthop 192.168.8.2
    Valid: 1 nexthop 192.168.8.3

To see information about a specific next hop group, add the group name 
at
 the end of the command; for example, `net show pbr nexthop-group
group1` (or `show pbr nexthop-group group1` in vtysh).

{{%notice note%}}

A new Linux routing table ID is used for each next hop and next hop 
group.

{{%/notice%}}

## <span>Delete PBR Rules and Policies</span>

You can delete a PBR rule, a next hop group, or a policy. with the `net
del` command.  
The following 
commands provide examples.

{{%notice note%}}

Use caution when deleting PBR rules and next hop groups, as you might
create an incorrect configuration for the PBR policy.

{{%/notice%}}

<summary>NCLU Commands </summary>

The following examples shows how to delete a PBR rule match:

    cumulus@switch:~$ net del pbr-map map1 seq 1 match dst-ip 10.1.2.0/24
    cumulus@switch:~$ net pending
    cumulus@switch:~$ net commit

The following examples shows how to delete a PBR rule matchnext hop from a group:

    cumulus@switch:~$ net del pbr-map map1 seq 1 match dst-ip 10.1.2.0/24nexthop-group group1 nexthop 192.168.0.32 swp1 nexthop-vrf rocket
    cumulus@switch:~$ net pending
    cumulus@switch:~$ net commit

The following examples shows how to delete a next hop group:

    cumulus@switch:~$ net del nexthop-group group1
    cumulus@switch:~$ net pending
    cumulus@switch:~$ net commit

The following examples shows how to delete a nexthop from a group:

    cumulus@switch:~$ net del nexthop-group group1 nexthop 192.168.0.32 swp1 nexthop-vrf rocket
    cumulus@switch:~$ net pending
    cumulus@switch:~$ net commit how to delete a PBR policy so that the PBR
interface is no longer receiving PBR traffic:

    cumulus@switch:~$ net del interface swp3 pbr-policy map1
    cumulus@switch:~$ net pending
    cumulus@switch:~$ net commit

The following examples show how to delete a PBR rule:

    cumulus@switch:~$ net del pbr-map map1 seq 1
    cumulus@switch:~$ net pending
    cumulus@switch:~$ net commit

<summary>vtysh Commands </summary>

The following examples show how to delete a PBR rule match:

    cumulus@switch:~$ sudo vtysh
    switch# configure terminal
    switch(config)# pbr-map map1 seq 1 
    switch(config-pbr-map)# no match dst-ip 10.1.2.0/24
    switch(config-pbr-map)# end
    switch# write memory
    switch# exit
    cumulus@switch:~$ 

The following examples show how to delete a next hop from a group:

    cumulus@switch:~$ sudo vtysh
    switch# configure terminal
    switch(config)# nexthop-group group1
    switch(config-nh-group)# no nexthop 192.168.0.32 swp1 nexthop-vrf rocket
    switch(config-nh-group)# end
    switch# write memory
    switch# exit
    cumulus@switch:~$ 

The following examples show how to delete a next hop group:

    cumulus@switch:~$ sudo vtysh
    switch# configure terminal
    switch(config)# no set nexthop-group group1 
    switch(config)# end
    switch# write memory
    switch# exit
    cumulus@switch:~$ 

The following examples shows how to delete a PBR policy so that the PBR
interface is no longer receiving PBR traffic:

    cumulus@switch:~$ net del interface swp3 pbr-policy map1
    cumulus@switch:~$ net pending
    cumulus@switch:~$ net commitsudo vtysh
    switch# configure terminal
    switch(config)# interface swp51
    switch(config-if)# no pbr-policy map1
    switch(config-if)# end
    switch# write memory
    switch# exit
    cumulus@switch:~$ 

The following examples show how to delete a PBR rule:

    cumulus@switch:~$ sudo vtysh
    switch# configure terminal
    switch(config)# no pbr-map map1 seq 1
    switch(config)# end
    switch# write memory
    switch# exit
    cumulus@switch:~$ 

<article id="html-search-results" class="ht-content" style="display: none;">

</article>

<footer id="ht-footer">

</footer>

</details>
<!--stackedit_data:
eyJoaXN0b3J5IjpbMjAzNDYxMTk2NF19
-->