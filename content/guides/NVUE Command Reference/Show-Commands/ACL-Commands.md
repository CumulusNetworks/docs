---
title: ACL Commands
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

- - -

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

- - -

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

- - -

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

- - -

## nv show acl \<acl-id\> rule \<rule-id\> action

Shows the action for the ACL rule specified.

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

- - -

## nv show acl \<acl-id\> rule \<rule-id\> action deny

Shows a deny action for the ACL rule specified.

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

- - -

## nv show acl \<acl-id\> rule \<rule-id\> action erspan

Shows the ERSPAN session for the ACL rule specified.

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

- - -

## nv show acl \<acl-id\> rule \<rule-id\> action log

Shows logs for the ACL rule specified.

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

- - -

## nv show acl \<acl-id\> rule \<rule-id\> action permit

Shows a permit action for the ACL rule specified.

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

- - -

## nv show acl \<acl-id\> rule \<rule-id\> action police

Shows policing of matched packets and bytes for the ACL rule specified.

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

- - -

## nv show acl \<acl-id\> rule \<rule-id\> action set

Shows the set action for the ACL rule specified.

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

- - -

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

- - -

## nv show acl \<acl-id\> rule \<rule-id\> match ip

Shows an IPv4 or IPv6 match for the ACL rule specified.

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

- - -

## nv show acl \<acl-id\> rule \<rule-id\> match ip dest-port

Shows destination port match configuration for the ACL rule specified.

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

- - -

## nv show acl \<acl-id\> rule \<rule-id\> match ip dest-port \<ip-port-id\>

Shows destination port matches for the ACL rule specified.

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

- - -

## nv show acl \<acl-id\> rule \<rule-id\> match ip ecn

Shows ECN matches for the ACL rule specified.

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

- - -

## nv show acl \<acl-id\> rule \<rule-id\> match ip ecn flags

Shows the ECN protocol flag matches for the ACL rule specified.

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

- - -

## nv show acl \<acl-id\> rule \<rule-id\> match ip fragment

Shows ip fragment packet matches for the ACL rule specified.

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

- - -

## nv show acl \<acl-id\> rule \<rule-id\> match ip source-port

Shows the source port match configuration for the ACL rule specified.

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

- - -

## nv show acl \<acl-id\> rule \<rule-id\> match ip source-port \<ip-port-id\>

Shows source port matches for the ACL rule specified.

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

- - -

## nv show acl \<acl-id\> rule \<rule-id\> match ip tcp

Shows TCP matches for the ACL rule specified.

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

- - -

## nv show acl \<acl-id\> rule \<rule-id\> match ip tcp flags

Shows TCP flag matches for the ACL rule specified.

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

- - -

## nv show acl \<acl-id\> rule \<rule-id\> match ip tcp mask

Shows TCP protocol flag mask matches for the ACL rule specified.

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

- - -

## nv show acl \<acl-id\> rule \<rule-id\> match mac

Shows MAC address matches for the ACL rule specified.

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

- - -

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

- - -

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

- - -

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

- - -

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

- - -

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

- - -

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

- - -

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

- - -

## nv show interface \<interface-id\> acl \<acl-id\> statistics \<rule-id\>

Shows statistics for the specified ACL rule on the specified interface.

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

- - -

## nv show system acl

Shows the ACL mode setting; atomic or non-atomic

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show system acl
```

- - -

## nv show system control-plane

Shows the control plane configuration.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show system control-plane
```

- - -

## nv show system control-plane policer

Shows control plane policer configuration.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show system control-plane policer
```

- - -

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

- - -

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

- - -

## nv show system control-plane trap

Shows the control plane trap configuration.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show system control-plane trap
```

- - -

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

- - -
