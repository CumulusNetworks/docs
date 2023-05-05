---
title: ACL
author: Cumulus Networks
weight: 110
product: Cumulus Linux
type: nojsscroll
---
## nv show acl

Shows the configured ACL rules on the switch.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show acl
```

<hr style="border: dashed rgb(118,185,0) 1.0px;background-color: rgb(118,185,0);height: 6.0px;"/>

## nv show acl \<acl-id\>

Shows the specified ACL rule.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<acl-id>` | The ACL name.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show acl EXAMPLE1
```

<hr style="border: dashed rgb(118,185,0) 1.0px;background-color: rgb(118,185,0);height: 6.0px;"/>

## nv show acl \<acl-id\> rule

Shows the rules for the specified ACL.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<acl-id>` | The ACL name.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show acl EXAMPLE1 rule
```

<hr style="border: dashed rgb(118,185,0) 1.0px;background-color: rgb(118,185,0);height: 6.0px;"/>

## nv show acl \<acl-id\> rule \<rule-id\>

Shows configuration information about the ACL with the specified rule number.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<acl-id>` | The ACL name.|
| `<rule-id>` | The rule number.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show acl EXAMPLE1 rule 10
```

<hr style="border: dashed rgb(118,185,0) 1.0px;background-color: rgb(118,185,0);height: 6.0px;"/>

## nv show acl \<acl-id\> rule \<rule-id\> action

Shows the action for the specified ACL rule.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<acl-id>` | The ACL name.|
| `<rule-id>` | The rule number.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show acl EXAMPLE1 rule 10 action
```

<hr style="border: dashed rgb(118,185,0) 1.0px;background-color: rgb(118,185,0);height: 6.0px;"/>

## nv show acl \<acl-id\> rule \<rule-id\> action deny

Shows the deny action for the specified ACL rule.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<acl-id>` | The ACL name.|
| `<rule-id>` | The rule number.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show acl EXAMPLE1 rule 10 action deny
```

<hr style="border: dashed rgb(118,185,0) 1.0px;background-color: rgb(118,185,0);height: 6.0px;"/>

## nv show acl \<acl-id\> rule \<rule-id\> action erspan

Shows the ERSPAN session for the specified ACL rule.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<acl-id>` | The ACL name.|
| `<rule-id>` | The rule number.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show acl EXAMPLE1 rule 10 action erspan
```

<hr style="border: dashed rgb(118,185,0) 1.0px;background-color: rgb(118,185,0);height: 6.0px;"/>

## nv show acl \<acl-id\> rule \<rule-id\> action log

Shows logs for the specified ACL rule.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<acl-id>` | The ACL name.|
| `<rule-id>` | The rule number.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show acl EXAMPLE1 rule 10 action log
```

<hr style="border: dashed rgb(118,185,0) 1.0px;background-color: rgb(118,185,0);height: 6.0px;"/>

## nv show acl \<acl-id\> rule \<rule-id\> action permit

Shows the permit action for the specified ACL rule.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<acl-id>` | The ACL name.|
| `<rule-id>` | The rule number.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show acl EXAMPLE1 rule 10 action permit
```

<hr style="border: dashed rgb(118,185,0) 1.0px;background-color: rgb(118,185,0);height: 6.0px;"/>

## nv show acl \<acl-id\> rule \<rule-id\> action police

Shows policing of matched packets and bytes for the specified ACL rule.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<acl-id>` | The ACL name.|
| `<rule-id>` | The ACL rule number. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show acl EXAMPLE1 rule 10 action police
```

<hr style="border: dashed rgb(118,185,0) 1.0px;background-color: rgb(118,185,0);height: 6.0px;"/>

## nv show acl \<acl-id\> rule \<rule-id\> action set

Shows the set action for the specified ACL rule.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<acl-id>` | The ACL name.|
| `<rule-id>` | The rule number.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show acl EXAMPLE1 rule 10 action set
```

<hr style="border: dashed rgb(118,185,0) 1.0px;background-color: rgb(118,185,0);height: 6.0px;"/>

## nv show acl \<acl-id\> rule \<rule-id\> match

Shows the ACL match criteria for the specified ACL rule.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<acl-id>` | The ACL name.|
| `<rule-id>` | The rule number.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show acl EXAMPLE1 rule 10 match
```

<hr style="border: dashed rgb(118,185,0) 1.0px;background-color: rgb(118,185,0);height: 6.0px;"/>

## nv show acl \<acl-id\> rule \<rule-id\> match ip

Shows an IPv4 or IPv6 match criteria for the specified ACL rule.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<acl-id>` | The ACL name.|
| `<rule-id>` | The rule number.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show acl EXAMPLE1 rule 10 match ip
```

<hr style="border: dashed rgb(118,185,0) 1.0px;background-color: rgb(118,185,0);height: 6.0px;"/>

## nv show acl \<acl-id\> rule \<rule-id\> match ip dest-port

Shows destination port match criteria for the specified ACL rule.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<acl-id>` | The ACL name.|
| `<rule-id>` | The rule number.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show acl EXAMPLE1 rule 10 match ip dest-port
```

<hr style="border: dashed rgb(118,185,0) 1.0px;background-color: rgb(118,185,0);height: 6.0px;"/>

## nv show acl \<acl-id\> rule \<rule-id\> match ip dest-port \<ip-port-id\>

Shows destination port match criteria for the specified ACL rule.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<acl-id>` | The ACL name.|
| `<rule-id>` | The rule number.|
| `<ip-port-id>` |  The IP port number or protocol. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show acl EXAMPLE1 rule 10 match ip dest-port http
```

<hr style="border: dashed rgb(118,185,0) 1.0px;background-color: rgb(118,185,0);height: 6.0px;"/>

## nv show acl \<acl-id\> rule \<rule-id\> match ip ecn

Shows ECN match criteria for the specified ACL rule.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<acl-id>` | The ACL name.|
| `<rule-id>` | The rule number.|

### Version History

Introduced in Cumulus Linux 5.2.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show acl EXAMPLE1 rule 10 match ip ecn
```

<hr style="border: dashed rgb(118,185,0) 1.0px;background-color: rgb(118,185,0);height: 6.0px;"/>

## nv show acl \<acl-id\> rule \<rule-id\> match ip ecn flags

Shows the ECN protocol flag match criteria for the specified ACL rule.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<acl-id>` | The ACL name.|
| `<rule-id>` | The rule number.|

### Version History

Introduced in Cumulus Linux 5.2.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show acl EXAMPLE1 rule 10 match ip ecn flags
```

<hr style="border: dashed rgb(118,185,0) 1.0px;background-color: rgb(118,185,0);height: 6.0px;"/>

## nv show acl \<acl-id\> rule \<rule-id\> match ip fragment

Shows ip fragment packet match criteria for the specified ACL rule.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<acl-id>` | The ACL name.|
| `<rule-id>` | The rule number.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show acl EXAMPLE1 rule 10 match ip fragment
```

<hr style="border: dashed rgb(118,185,0) 1.0px;background-color: rgb(118,185,0);height: 6.0px;"/>

## nv show acl \<acl-id\> rule \<rule-id\> match ip source-port

Shows the source port match criteria for the specified ACL rule.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<acl-id>` | The ACL name.|
| `<rule-id>` | The rule number.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show acl EXAMPLE1 rule 10 match ip source-port ANY
```

<hr style="border: dashed rgb(118,185,0) 1.0px;background-color: rgb(118,185,0);height: 6.0px;"/>

## nv show acl \<acl-id\> rule \<rule-id\> match ip source-port \<ip-port-id\>

Shows the match criteria for a specific port for the specified ACL rule.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<acl-id>` | The ACL name.|
| `<rule-id>` | The rule number.|
| `<ip-port-id>` | The IP port number or protocol. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show acl EXAMPLE1 rule 10 match ip source-port ANY
```

<hr style="border: dashed rgb(118,185,0) 1.0px;background-color: rgb(118,185,0);height: 6.0px;"/>

## nv show acl \<acl-id\> rule \<rule-id\> match ip tcp

Shows TCP match criteria for the specified ACL rule.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<acl-id>` | The ACL name.|
| `<rule-id>` | The rule number.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show acl EXAMPLE1 rule 10 match ip tcp
```

<hr style="border: dashed rgb(118,185,0) 1.0px;background-color: rgb(118,185,0);height: 6.0px;"/>

## nv show acl \<acl-id\> rule \<rule-id\> match ip tcp flags

Shows TCP flag match criteria for the specified ACL rule.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<acl-id>` | The ACL name.|
| `<rule-id>` | The rule number.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show acl EXAMPLE1 rule 10 match ip tcp flags
```

<hr style="border: dashed rgb(118,185,0) 1.0px;background-color: rgb(118,185,0);height: 6.0px;"/>

## nv show acl \<acl-id\> rule \<rule-id\> match ip tcp mask

Shows TCP protocol flag mask match criteria for the specified ACL rule.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<acl-id>` | The ACL name.|
| `<rule-id>` | The rule number.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show acl EXAMPLE1 rule 10 match ip tcp mask
```

<hr style="border: dashed rgb(118,185,0) 1.0px;background-color: rgb(118,185,0);height: 6.0px;"/>

## nv show acl \<acl-id\> rule \<rule-id\> match mac

Shows MAC address match criteria for the specified ACL rule.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<acl-id>` | The ACL name.|
| `<rule-id>` | The rule number.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show acl EXAMPLE1 rule 10 match mac
```

<hr style="border: dashed rgb(118,185,0) 1.0px;background-color: rgb(118,185,0);height: 6.0px;"/>

## nv show interface \<interface-id\> acl

Shows the <span style="background-color:#F5F5DC">[ACLs](## "Access Control Lists")</span> on the specified interface. You use ACLs to match packets and take actions.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<interface-id>` | The interface on which the ACL operates. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show interface swp1 acl
```

<hr style="border: dashed rgb(118,185,0) 1.0px;background-color: rgb(118,185,0);height: 6.0px;"/>

## nv show interface \<interface-id\> acl \<acl-id\>

Shows information about the specified ACL on the specified interface. You use ACLs to match packets and take actions.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<interface-id>` | The interface on which the ACL operates. |
| `<acl-id>` | The ACL name.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show interface swp1 acl EXAMPLE1
```

<hr style="border: dashed rgb(118,185,0) 1.0px;background-color: rgb(118,185,0);height: 6.0px;"/>

## nv show interface \<interface-id\> acl \<acl-id\> inbound

Shows information about the ACL applied for inbound traffic on the specified interface.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<interface-id>` | The interface on which the ACL operates. |
| `<acl-id>` | The ACL name.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show interface swp1 acl EXAMPLE1 inbound
```

<hr style="border: dashed rgb(118,185,0) 1.0px;background-color: rgb(118,185,0);height: 6.0px;"/>

## nv show interface \<interface-id\> acl \<acl-id\> inbound control-plane

Shows information about the ACL applied for the control plane on the specified interface.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<interface-id>` | The interface on which the ACL operates. |
| `<acl-id>` | The ACL name.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show interface swp1 acl EXAMPLE1 inbound control-plane
```

<hr style="border: dashed rgb(118,185,0) 1.0px;background-color: rgb(118,185,0);height: 6.0px;"/>

## nv show interface \<interface-id\> acl \<acl-id\> outbound

Shows information about the ACL applied for outbound traffic on the specified interface.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<interface-id>` | The interface on which the ACL operates. |
| `<acl-id>` | The ACL name.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show interface swp1 acl EXAMPLE1 outbound
```

<hr style="border: dashed rgb(118,185,0) 1.0px;background-color: rgb(118,185,0);height: 6.0px;"/>

## nv show interface \<interface-id\> acl \<acl-id\> outbound control-plane

Shows information about the ACL applied to the control plane for outbound traffic on the specified interface.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<interface-id>` | The interface on which the ACL operates. |
| `<acl-id>` | The ACL name.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show interface swp1 acl EXAMPLE1 outbound control-plane
```

<hr style="border: dashed rgb(118,185,0) 1.0px;background-color: rgb(118,185,0);height: 6.0px;"/>

## nv show interface \<interface-id\> acl \<acl-id\> statistics

Shows statistics for a specific ACL on the specified interface.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<interface-id>` | The interface on which the ACL operates. |
| `<acl-id>` | The ACL name.|

### Version History

Introduced in Cumulus Linux 5.2.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show interface swp1 acl EXAMPLE1 statistics
```

<hr style="border: dashed rgb(118,185,0) 1.0px;background-color: rgb(118,185,0);height: 6.0px;"/>

## nv show interface \<interface-id\> acl \<acl-id\> statistics \<rule-id\>

Shows statistics for a specific ACL rule on the specified interface.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<interface-id>` | The interface on which the ACL operates. |
| `<acl-id>` | The ACL name.|

### Version History

Introduced in Cumulus Linux 5.2.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show interface swp1 acl EXAMPLE1 statistics 10
```

<hr style="border: dashed rgb(118,185,0) 1.0px;background-color: rgb(118,185,0);height: 6.0px;"/>

## nv show system acl

Shows the ACL mode setting; atomic or non-atomic

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show system acl
```

<hr style="border: dashed rgb(118,185,0) 1.0px;background-color: rgb(118,185,0);height: 6.0px;"/>

## nv show system control-plane

Shows the control plane configuration.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show system control-plane
```

<hr style="border: dashed rgb(118,185,0) 1.0px;background-color: rgb(118,185,0);height: 6.0px;"/>

## nv show system control-plane acl

Shows the control plane ACLs configured on the switch. You use control plane ACLs to apply a single rule for all packets forwarded to the CPU regardless of the source interface or destination interface on the switch. Control plane ACLs allow you to regulate traffic forwarded to applications on the switch with more granularity than traps and to configure ACLs to block SSH from specific addresses or subnets.

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show system control-plane acl
```

<hr style="border: dashed rgb(118,185,0) 1.0px;background-color: rgb(118,185,0);height: 6.0px;"/>

## nv show system control-plane acl \<acl-id\>

Shows information about the specified control plane ACL.

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show system control-plane acl ACL1
```

<hr style="border: dashed rgb(118,185,0) 1.0px;background-color: rgb(118,185,0);height: 6.0px;"/>

## nv show system control-plane acl \<acl-id\> inbound

Shows configuration information for the specified inbound control plane ACL.

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show system control-plane acl ACL1 inbound
```

<hr style="border: dashed rgb(118,185,0) 1.0px;background-color: rgb(118,185,0);height: 6.0px;"/>

## nv show system control-plane acl \<acl-id\> outbound

Shows configuration information for the specified outbound control plane ACL.

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show system control-plane acl ACL1 outbound
```

<hr style="border: dashed rgb(118,185,0) 1.0px;background-color: rgb(118,185,0);height: 6.0px;"/>

## nv show system control-plane acl \<acl-id\> statistics

Shows statistics for the specified control plane ACL.

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show system control-plane acl ACL1 statistics
```

<hr style="border: dashed rgb(118,185,0) 1.0px;background-color: rgb(118,185,0);height: 6.0px;"/>

## nv show system control-plane acl \<acl-id\> statistics \<rule-id\>

Shows statistics for the specified control plane ACL rule.

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show system control-plane acl ACL1 statistics 10
```

<hr style="border: dashed rgb(118,185,0) 1.0px;background-color: rgb(118,185,0);height: 6.0px;"/>

## nv show system control-plane policer

Shows control plane policer configuration.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show system control-plane policer
```

<hr style="border: dashed rgb(118,185,0) 1.0px;background-color: rgb(118,185,0);height: 6.0px;"/>

## nv show system control-plane policer \<policer-id\>

Shows configuration information for a specific control plane policer.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<policer-id>` | The policer ID: `arp`, `bfd`, `pim-ospf-rip`, `bgp`, `clag`, `icmp-def`, `dhcp-ptp`, `igmp`, `ssh`, `icmp6-neigh`, `icmp6-def-mld`, `lacp`, `lldp`, `rpvst`, `eapol`, `ip2me`, `acl-log`, `nat`, `stp`, `l3-local`, `span-cpu`, `unknown-ipmc`, `catch-all`.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show system control-plane policer bfd
```

<hr style="border: dashed rgb(118,185,0) 1.0px;background-color: rgb(118,185,0);height: 6.0px;"/>

## nv show system control-plane policer \<policer-id\> statistics

Shows statistics for a specific control plane policer.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<policer-id>` | The policer ID: `arp`, `bfd`, `pim-ospf-rip`, `bgp`, `clag`, `icmp-def`, `dhcp-ptp`, `igmp`, `ssh`, `icmp6-neigh`, `icmp6-def-mld`, `lacp`, `lldp`, `rpvst`, `eapol`, `ip2me`, `acl-log`, `nat`, `stp`, `l3-local`, `span-cpu`, `unknown-ipmc`, `catch-all`.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show system control-plane policer bfd statistics
```

<hr style="border: dashed rgb(118,185,0) 1.0px;background-color: rgb(118,185,0);height: 6.0px;"/>

## nv show system control-plane trap

Shows the control plane trap configuration.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show system control-plane trap
```

<hr style="border: dashed rgb(118,185,0) 1.0px;background-color: rgb(118,185,0);height: 6.0px;"/>

## nv show system control-plane trap \<trap-id\>

Shows specific control plane trap configuration.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<trap-id>` | The trap ID.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show system control-plane trap l3-mtu-err
```
