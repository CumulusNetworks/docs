---
title: Policy-based Routing
author: NVIDIA
weight: 760
toc: 3
---
Typical routing systems and protocols forward traffic based on the destination address in the packet, which they look up in a routing table. However, sometimes the traffic on your network requires a more hands-on approach. Sometimes, you need to forward a packet based on the source address, the packet size, or other information in the packet header.

<span style="background-color:#F5F5DC">[PBR](## "Policy-based Routing")</span> lets you make routing decisions based on filters that change the routing behavior of specific traffic so that you can override the routing table and influence where the traffic goes. For example, you can use PBR to reach the best bandwidth utilization for business-critical applications, isolate traffic for inspection or analysis, or manually load balance outbound traffic.

Cumulus Linux applies PBR to incoming packets. All packets received on a PBR-enabled interface pass through enhanced packet filters that determine rules and specify where to forward the packets.

{{%notice note%}}
- You can create a *maximum* of 255 PBR match rules and 256 next hop groups (this is the <span style="background-color:#F5F5DC">[ECMP](## "Equal Cost Multi Path") limit)</span>.
- You can apply only one PBR policy per input interface.
- You can match on *source* and *destination* IP address, or match on <span style="background-color:#F5F5DC">[DSCP](## "Differentiated Services Code Point")</span> or <span style="background-color:#F5F5DC">[ECN](## "Explicit Congestion Notification")</span> values within a packet.
- PBR is not supported for VXLAN tunneling.
- PBR is not supported on management interfaces, such as eth0.
- A PBR rule cannot contain both IPv4 and IPv6 addresses.
{{%/notice%}}

## Configure PBR

A PBR policy contains one or more policy maps. Each policy map:

- Has a unique map name and sequence (rule) number. The rule number determines the relative order of the map within the policy.
- Contains a match source IP rule and (or) a match destination IP rule and a set rule, or a match DSCP or ECN rule and a set rule.
   - To match on a source and destination address, a policy map can contain both match source and match destination IP rules.
   - A set rule determines the PBR next hop for the policy. <!--The set rule can contain a single next hop IP address or it can contain a next hop group. A next hop group has more than one next hop IP address so that you can use multiple interfaces to forward traffic. To use ECMP, you configure a next hop group.-->

To use PBR in Cumulus linux, you define a PBR policy and apply it to the ingress interface (the interface must already have an IP address assigned). Cumulus Linux matches traffic against the match rules in sequential order and forwards the traffic according to the set rule in the first match. Traffic that does not match any rule passes on to the normal destination based routing mechanism.

To configure a PBR policy:

{{< tabs "TabID35 ">}}
{{< tab "NVUE Commands ">}}

{{%notice warning%}}
When you configure PBR with NVUE commands, NVUE enables the `pbrd` service and restarts the FRR service; An FRR service restart might impact traffic.
{{%/notice%}}

1. Configure the policy map.

    The example commands below configure a policy map called `map1` with rule number 1 that matches on destination address 10.1.2.0/24 and source address 10.1.4.1/24.

    If the IP address in the rule is `0.0.0.0/0 or ::/0`, any IP address is a match. You cannot mix IPv4 and IPv6 addresses in a rule.

    ```
    cumulus@switch:~$ nv set router pbr map map1 rule 1 match destination-ip 10.1.2.0/24
    cumulus@switch:~$ nv set router pbr map map1 rule 1 match source-ip 10.1.4.1/24 
    ```

    Instead of matching on IP address, you can match packets according to the DSCP or ECN field in the IP header. The DSCP value can be an integer between 0 and 63 or the DSCP codepoint name. The ECN value can be an integer between 0 and 3. The following example command configures a policy map called `map1` with rule number 1 that matches on packets with the DSCP value 10:

    ```
    cumulus@switch:~$ nv set router pbr map map1 rule 1 match dscp 10
    ```

    The following example command configures a policy map called `map1` with rule number 1 that matches on packets with the ECN value 2:

    ```
    cumulus@switch:~$ nv set router pbr map map1 rule 1 match ecn 2
    ```

2. Apply a next hop group to the policy map. First configure the next hop group, then apply the group to the policy map. The example commands below create a next hop group called `group1` that contains the next hop 192.168.0.21 on output interface swp1 and VRF `RED` and the next hop 192.168.0.22, then applies the next hop group `group1` to the `map1` policy map.

    The output interface and VRF are optional. However, you must specify the VRF if the next hop is not in the default VRF.

    ```
    cumulus@switch:~$ nv set router nexthop group group1 via 192.168.0.21 interface swp1
    cumulus@switch:~$ nv set router nexthop group group1 via 192.168.0.21 vrf RED
    cumulus@switch:~$ nv set router nexthop group group1 via 192.168.0.22
    cumulus@switch:~$ nv set router pbr map map1 rule 1 action nexthop-group group1
    ```

   If you want the rule to use a specific VRF table as its lookup, set the VRF. If you do not set a VRF, the rule uses the VRF table the interface is in as its lookup. The example command below sets the rule to use the `dmz` VRF table:

    ```
    cumulus@switch:~$ nv set router pbr map map1 rule 1 action vrf dmz
    ```

3. Assign the PBR policy to an ingress interface. The example command below assigns the PBR policy `map1` to interface swp51:

    ```
    cumulus@switch:~$ nv set interface swp51 router pbr map map1
    cumulus@switch:~$ nv config apply
    ```

{{< /tab >}}
{{< tab "vtysh Commands ">}}

1. Enable the `pbrd` service in the `/etc/frr/daemons` file:

    ```
    cumulus@switch:~$ sudo nano /etc/frr/daemons
    ...
    bgpd=yes
    ospfd=no
    ospf6d=no
    ripd=no
    ripngd=no
    isisd=no
    fabricd=no
    pimd=no
    ldpd=no
    nhrpd=no
    eigrpd=no
    babeld=no
    sharpd=no
    pbrd=yes
    ...
    ```
<!-- vale off -->
2. {{<cl/restart-frr>}}
<!-- vale on -->
3. Configure the policy map.

    The example commands below configure a policy map called `map1` with sequence number 1, that matches on destination address 10.1.2.0/24 and source address 10.1.4.1/24.

    ```
    cumulus@switch:~$ sudo vtysh

    switch# configure terminal
    switch(config)# pbr-map map1 seq 1
    switch(config-pbr-map)# match dst-ip 10.1.2.0/24
    switch(config-pbr-map)# match src-ip 10.1.4.1/24
    switch(config-pbr-map)# exit
    switch(config)# 
    ```

    If the IP address in the rule is `0.0.0.0/0 or ::/0`, any IP address is a match. You cannot mix IPv4 and IPv6 addresses in a rule.

    Instead of matching on IP address, you can match packets according to the DSCP or ECN field in the IP header. The DSCP value can be an integer between 0 and 63 or the DSCP codepoint name. The ECN value can be an integer between 0 and 3. The following example command configures a policy map called `map1` with sequence number 1 that matches on packets with the DSCP value 10:

    ```
    switch# configure terminal
    switch(config)# pbr-map map1 seq 1
    switch(config-pbr-map)# match dscp 10
    switch(config-pbr-map)# exit
    switch(config)# 
    ```

    The following example command configures a policy map called `map1` with sequence number 1 that matches on packets with the ECN value 2:

    ```
    switch# configure terminal
    switch(config)# pbr-map map1 seq 1
    switch(config-pbr-map)# match ecn 2
    switch(config-pbr-map)# exit
    switch(config)# 
    ```

4. Apply a *next hop* group to the policy map. First configure the next hop group, then apply the group to the policy map. The example commands below create a next hop group called `group1` that contains the next hop 192.168.0.21 on output interface swp1 and VRF `RED`, and the next hop 192.168.0.22, then applies the next hop group `group1` to the `map1` policy map.

    The output interface and VRF are optional. However, you must specify the VRF if the next hop is not in the default VRF.

    ```
    switch(config)# nexthop-group group1
    switch(config-nh-group)# nexthop 192.168.0.21 swp1 nexthop-vrf RED
    switch(config-nh-group)# nexthop 192.168.0.22
    switch(config-nh-group)# exit
    switch(config)# pbr-map map1 seq 1
    switch(config-pbr-map)# set nexthop-group group1
    switch(config-pbr-map)# exit
    switch(config)#
    ```

    If you want the rule to use a specific VRF table as its lookup, set the VRF. If you do not set a VRF, the rule uses the VRF table the interface is in as its lookup. The example command below sets the rule to use the `dmz` VRF table:

    ```
    switch(config)# pbr-map map1 seq 1
    switch(config-pbr-map)# set vrf dmz
    switch(config-pbr-map)# exit
    switch(config)#
    ```

   Instead of a next hop *group*, you can apply a next hop to the policy map. The example command below applies the next hop 192.168.0.31 on the output interface swp2 and VRF `RED` to the `map1` policy map. The next hop must be an IP address. The output interface and VRF are optional, however, you *must* specify the VRF you want to use for resolution if the next hop is *not* in the default VRF.

    ```
    switch(config-pbr-map)# set nexthop 192.168.0.31 swp2 nexthop-vrf RED
    switch(config-pbr-map)# exit
    switch(config)#
    ```

5. Assign the PBR policy to an ingress interface. The example command below assigns the PBR policy `map1` to interface swp51:

    ```
    switch(config)# interface swp51
    switch(config-if)# pbr-policy map1
    switch(config-if)# end
    switch# write memory
    switch# exit
    cumulus@switch:~$
    ```

The vtysh commands save the configuration in the `/etc/frr/frr.conf` file. For example:

```
...
nexthop-group group1
nexthop 192.168.0.21 nexthop-vrf RED swp1
nexthop 192.168.0.22
pbr-map map1 seq 1
match dst-ip 10.1.2.0/24
match src-ip 10.1.4.1/24
set nexthop-group group1
interface swp51
pbr-policy map1
...
```

{{< /tab >}}
{{< /tabs >}}

{{%notice note%}}
You can only set one policy per interface.
{{%/notice%}}

## Modify PBR Rules

When you want to change or extend an existing PBR rule, you must first delete the conditions in the rule, then add the rule back with the modification or addition.

{{< expand " Modify an existing match/set condition"  >}}

The example below shows an existing configuration.

```
cumulus@switch:~$ sudo vtysh
...
switch# show pbr map
Seq: 4 rule: 303 Installed: yes Reason: Valid
    SRC Match: 10.1.4.1/24
    DST Match: 10.1.2.0/24
 nexthop 192.168.0.21
    Installed: yes Tableid: 10009
```

The commands for the above configuration are:

```
cumulus@switch:~$ nv set router pbr map pbr-policy rule 4 match source-ip 10.1.4.1/24
cumulus@switch:~$ nv set router pbr map pbr-policy rule 4 match destination-ip 10.1.2.0/24
cumulus@switch:~$ nv set router nexthop group group1 via 192.168.0.21
cumulus@switch:~$ nv set router pbr map pbr-policy rule 4 action nexthop-group group1
```

To change the source IP match from 10.1.4.**1**/24 to 10.1.4.**2**/24, you must delete the existing sequence by explicitly specifying the match/set condition. For example:

```
cumulus@switch:~$ nv unset router pbr map pbr-policy rule 4 match source-ip
cumulus@switch:~$ nv unset router pbr map pbr-policy rule 4 match destination-ip
cumulus@switch:~$ nv unset router nexthop group group1 via 192.168.0.21
```

Add the new rule with the following commands:

```
cumulus@switch:~$ nv set router pbr map pbr-policy rule 4 match source-ip 10.1.4.2/24
cumulus@switch:~$ nv set router pbr map pbr-policy rule 4 match destination-ip 10.1.2.0/24
cumulus@switch:~$ nv set router nexthop group group1 via 192.168.0.21
cumulus@switch:~$ nv config apply
```

Run the vtysh `show pbr map` command to verify that the rule has the updated source IP match:

```
cumulus@switch:~$ sudo vtysh
...
switch# show pbr map
Seq: 4 rule: 303 Installed: yes Reason: Valid
     SRC Match: 10.1.4.2/24
     DST Match: 10.1.2.0/24
   nexthop 192.168.0.21
     Installed: yes Tableid: 10012
```

Run the Linux `ip rule show` command to verify the entry in the kernel:

```
cumulus@switch:~$ ip rule show

303: from 10.1.4.1/24 to 10.1.4.2 iif swp16 lookup 10012
```

Run the following command to verify `switchd`:

```
cumulus@switch:~$ sudo cat /cumulus/switchd/run/iprule/show | grep 303 -A 1
303: from 10.1.4.1/24 to 10.1.4.2 iif swp16 lookup 10012
     [hwstatus: unit: 0, installed: yes, route-present: yes, resolved: yes, nh-valid: yes, nh-type: nh, ecmp/rif: 0x1, action: route,  hitcount: 0]
```

{{< /expand >}}

{{< expand "Add a match condition to an existing rule"  >}}

The example below shows an existing configuration with only one source IP match:

```
Seq: 3 rule: 302 Installed: yes Reason: Valid
	SRC Match: 10.1.4.1/24
nexthop 192.168.0.21
	Installed: yes Tableid: 10008
```

The commands for the above configuration are:

```
cumulus@switch:~$ nv set router pbr map pbr-policy rule 3 match source-ip 10.1.4.1/24
cumulus@switch:~$ nv set router nexthop group group1 via 192.168.0.21
```

To add a destination IP match to the rule, you must delete the existing rule sequence:

```
cumulus@switch:~$ nv router pbr map pbr-policy rule 3 match source-ip
cumulus@switch:~$ nv unset router nexthop group group1 via 192.168.0.21
cumulus@switch:~$ nv config apply
```

Add back the source IP match and next hop condition, and add the new destination IP match (dst-ip 10.1.2.0/24):

```
cumulus@switch:~$ nv set router pbr map pbr-policy rule 3 match source-ip 10.1.4.1/24
cumulus@switch:~$ nv set router pbr map pbr-policy rule 3 match destination-ip 10.1.2.0/24
cumulus@switch:~$ nv set router nexthop group group1 via 192.168.0.21
cumulus@switch:~$ nv config apply
```

Run the vtysh `show pbr map` command to verify the update:

```
cumulus@switch:~$ sudo vtysh
...
switch# show pbr map
Seq: 3 rule: 302 Installed: 1(9) Reason: Valid
    SRC Match: 10.1.4.1/24
    DST Match: 10.1.2.0/24
   nexthop 192.168.0.21
    Installed: 1(1) Tableid: 10013
```

Run the  `ip rule show` command to verify the entry in the kernel:

```
cumulus@switch:~$ ip rule show
302:  from 10.1.4.1/24 to 10.1.2.0 iif swp16 lookup 10013
```

Run the following command to verify `switchd`:

```
cumulus@switch:~$ cat /cumulus/switchd/run/iprule/show | grep 302 -A 1
302: from 10.1.4.1/24 to 10.1.2.0 iif swp16 lookup 10013
     [hwstatus: unit: 0, installed: yes, route-present: yes, resolved: yes, nh-valid: yes, nh-type: nh, ecmp/rif: 0x1, action: route,  hitcount: 0]
```

{{< /expand >}}

## Delete PBR Rules and Policies

You can delete a PBR rule, a next hop group, or a policy. The following commands provide examples.

{{%notice note%}}
Use caution when deleting PBR rules and next hop groups. Do not create an incorrect configuration for the PBR policy.
{{%/notice%}}

{{< tabs "TabID451 ">}}
{{< tab "NVUE Commands ">}}

The following examples show how to delete a PBR rule match:

```
cumulus@switch:~$ nv unset router pbr map map1 rule 1 match destination-ip
cumulus@switch:~$ nv config apply
```

The following examples show how to delete a next hop from a group:

```
cumulus@switch:~$ nv unset router nexthop group group1 via 192.168.0.22
cumulus@switch:~$ nv config apply
```

The following examples show how to delete a next hop group:

```
cumulus@switch:~$ nv unset router nexthop group group1
cumulus@switch:~$ nv config apply
```

The following examples show how to delete a PBR policy so that the PBR interface is no longer receiving PBR traffic:

```
cumulus@switch:~$ nv unset interface swp51 router pbr map map1
cumulus@switch:~$ nv config apply
```

The following examples show how to delete a PBR rule:

```
cumulus@switch:~$ nv unset router pbr map map1
cumulus@switch:~$ nv config apply
```

{{< /tab >}}
{{< tab "vtysh Commands ">}}

The following examples show how to delete a PBR rule match:

```
cumulus@switch:~$ sudo vtysh
...
switch# configure terminal
switch(config)# pbr-map map1 seq 1
switch(config-pbr-map)# no match dst-ip 10.1.2.0/24
switch(config-pbr-map)# end
switch# write memory
switch# exit
```

The following examples show how to delete a next hop from a group:

```
cumulus@switch:~$ sudo vtysh
...
switch# configure terminal
switch(config)# nexthop-group group1
switch(config-nh-group)# no nexthop 192.168.0.32 swp1 nexthop-vrf RED
switch(config-nh-group)# end
switch# write memory
switch# exit
```

The following examples show how to delete a next hop group:

```
cumulus@switch:~$ sudo vtysh
...
switch# configure terminal
switch(config)# no nexthop-group group1
switch(config)# end
switch# write memory
switch# exit
```

The following examples show how to delete a PBR policy so that the PBR interface is no longer receiving PBR traffic:

```
cumulus@switch:~$ sudo vtysh
...
switch# configure terminal
switch(config)# interface swp51
switch(config-if)# no pbr-policy map1
switch(config-if)# end
switch# write memory
switch# exit
```

The following examples show how to delete a PBR rule:

```
cumulus@switch:~$ sudo vtysh
...
switch# configure terminal
switch(config)# no pbr-map map1 seq 1
switch(config)# end
switch# write memory
switch# exit
```

{{< /tab >}}
{{< /tabs >}}

If a PBR rule has multiple conditions (for example, a source IP match and a destination IP match), but you only want to delete one condition, you have to delete all conditions first, then re-add the ones you want to keep.

The example below shows an existing configuration that has a source IP match and a destination IP match.

```
Seq: 6 rule: 305 Installed: yes Reason: Valid
   SRC Match: 10.1.4.1/24
   DST Match: 10.1.2.0/24
nexthop 192.168.0.21
   Installed: yes Tableid: 10011
```

The commands for the above configuration are:

```
cumulus@switch:~$ nv set router pbr map pbr-policy rule 6 match source-ip 10.1.4.1/24
cumulus@switch:~$ nv set router pbr map pbr-policy rule 6 match destination-ip 10.1.2.0/24
cumulus@switch:~$ nv set router nexthop group group1 via 192.168.0.21
```

To remove the destination IP match, you must first delete all existing conditions defined under this sequence:

```
cumulus@switch:~$ nv unset router pbr map pbr-policy rule 6 match source-ip 
cumulus@switch:~$ nv unset router pbr map pbr-policy rule 6 match destination-ip
cumulus@switch:~$ nv unset router nexthop group group1 via 192.168.0.21
cumulus@switch:~$ nv config apply
```

Then, add back the conditions you want to keep:

```
cumulus@switch:~$ nv set router pbr map pbr-policy rule 6 match source-ip 10.1.4.1/24
cumulus@switch:~$ nv unset router nexthop group group1 via 192.168.0.21
cumulus@switch:~$ nv config apply
```

## Troubleshooting

To see the policies applied to all interfaces on the switch, run the NVUE `nv show router pbr -o json` command:

```
cumulus@switch:~$ nv show router pbr  -o json
{
  "map": {
    "map1": {
      "rule": {
        "1": {
          "action": {
            "nexthop-group": {
              "group1": {
                "installed": "off",
                "table-id": 10000
              }
            }
          },
          "installed": "off",
          "installed-reason": "Invalid NH-group",
          "ip-rule-id": 300,
          "match": {
            "destination-ip": "10.1.2.0/24",
            "dscp": 10,
            "source-ip": "10.1.4.1/24"
          }
        }
      }
    }
  }
}
```

To see the policies applied to a specific interface on the switch, run the NVUE `nv show interface <interface> router pbr` command or the vtysh `show pbr interface <interface>` command.

To see information about all policies, including mapped table and rule numbers, run the NVUE `nv show router pbr map` command or the vtysh `show pbr map` command. If the rule is not set, you see a reason why.

```
cumulus@switch:~$ sudo vtysh
switch# show pbr map
 pbr-map map1 valid: yes
  Seq: 700 rule: 999 Installed: yes Reason: Valid
      SRC Match: 10.0.0.1/32
  nexthop 192.168.0.32
      Installed: yes Tableid: 10003
  Seq: 701 rule: 1000 Installed: yes Reason: Valid
      SRC Match: 90.70.0.1/32
  nexthop 192.168.0.32
      Installed: yes Tableid: 10004
```

To see information about a policy, its matches, and associated interface, run the vtysh `show pbr map <map-name>` command.

To see information about all next hop groups, run the NVUE `nv show router pbr nexthop-group` command or the vtysh `show pbr nexthop-group` command.

```
cumulus@switch:~$ nv show router pbr nexthop-group
Nexthop-groups  installed  valid    Summary         
--------------  ---------  -----    ----------------
group1          yes         yes     Nexthop-index: 1
                                    Nexthop-index: 2
```

To see information about a specific next hop group, run the NVUE `nv show router pbr nexthop-group <nexthop-group>` command or the vtysh `show pbr nexthop-group <nexthop-group>` command.

{{%notice note%}}
Each next hop and next hop group uses a new Linux routing table ID.
{{%/notice%}}

To show the reserved routing table range, run the NVUE `nv show system global reserved routing-table pbr` command.

```
cumulus@switch:~$ nv show system global reserved routing-table pbr
       operational  applied   
-----  -----------  ----------
begin  10000        10000     
end    4294966272   4294966272
```

## Example Configuration

In the following example, the PBR-enabled switch has a PBR policy to route all traffic from the Internet to a server that performs anti-DDOS. After cleaning, the traffic returns to the PBR-enabled switch and then passes on to the regular destination-based routing mechanism.

{{< img src = "/images/cumulus-linux/pbr-example.png" >}}

{{< tabs "TabID197 ">}}
{{< tab "NVUE Commands ">}}

```
cumulus@switch:~$ nv set router pbr map map1 rule 1 match source-ip 0.0.0.0/0
cumulus@switch:~$ nv set router nexthop group group1 via 192.168.0.32
cumulus@switch:~$ nv set router pbr map map1 rule 1 action nexthop-group group1
cumulus@switch:~$ nv set interface swp51 router pbr map map1
cumulus@switch:~$ nv config apply
```

{{< /tab >}}
{{< tab "vtysh Commands ">}}

```
cumulus@switch:~$ sudo vtysh

switch# configure terminal
switch(config)# nexthop-group group1
switch(config-nh-group)#  nexthop 192.168.0.32
switch(config-nh-group)# exit
switch(config)# pbr-map map1 seq 1
switch(config-pbr-map)#  match src-ip 0.0.0.0/0
switch(config-pbr-map)#  set nexthop-group group1
switch(config-pbr-map)# exit
switch(config)# interface swp51
switch(config-if)#  pbr-policy map1
switch(config-if)# end
switch# write memory
switch# exit
cumulus@switch:mgmt:~$
```

The vtysh commands save the configuration in the `/etc/frr/frr.conf` file. For example:

```
interface swp51
pbr-policy map1
nexthop-group group1
nexthop 192.168.0.32
pbr-map map1 seq 1
match src-ip 0.0.0.0/0
set nexthop-group group1
...
```

{{< /tab >}}
{{< /tabs >}}
