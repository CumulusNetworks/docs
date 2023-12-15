---
title: ACL
author: Cumulus Networks
weight: 110

type: nojsscroll
---
<style>
h { color: RGB(118,185,0)}
</style>
<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show acl</h>

Shows the configured ACL rules on the switch.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show acl
          type  Summary 
--------  ----  --------
EXAMPLE1  ipv4  rule: 10
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show acl \<acl-id\></h>

Shows the specified ACL configuration.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<acl-id>` | The ACL name.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show acl EXAMPLE1
      operational  applied
----  -----------  -------
type               ipv4

rule
=======
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show acl \<acl-id\> rule</h>

Shows the rules for the specified ACL.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<acl-id>` | The ACL name.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show acl EXAMPLE1 rule
Number  Summary                         
------  --------------------------------
10      match.ip.dest-ip:   10.0.15.8/32
        match.ip.dest-port:          ANY
        match.ip.protocol:           tcp
        match.ip.source-ip: 10.0.14.2/32
        match.ip.source-port:        ANY
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show acl \<acl-id\> rule \<rule-id\></h>

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
cumulus@switch:~$ nv show acl EXAMPLE1 rule 10
                   operational   applied     
-----------------  ------------  ------------
match                                        
  ip                                         
    dest-ip        10.0.15.8/32  10.0.15.8/32
    protocol       tcp           tcp         
    source-ip      10.0.14.2/32  10.0.14.2/32
    [dest-port]    ANY           ANY         
    [source-port]  ANY           ANY
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show acl \<acl-id\> rule \<rule-id\> action</h>

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
cumulus@switch:~$ nv show acl EXAMPLE1 rule 10 action
  operational  applied
  -----------  -------
               permit
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show acl \<acl-id\> rule \<rule-id\> action dest-nat</h>

Shows NAT destination rules.

### Version History

Introduced in Cumulus Linux 5.7.0

### Example

```
cumulus@switch:~$ nv show acl EXAMPLE1 rule 10 action dest-nat
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show acl \<acl-id\> rule \<rule-id\> action dest-nat translate-ip</h>

Shows NAT destination translate IP address rules.

### Version History

Introduced in Cumulus Linux 5.7.0

### Example

```
cumulus@switch:~$ nv show acl EXAMPLE1 rule 10 action dest-nat translate-ip
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show acl \<acl-id\> rule \<rule-id\> action dest-nat translate-ip <range-id></h>

Shows NAT destination translate IP address range rules.

### Version History

Introduced in Cumulus Linux 5.7.0

### Example

```
cumulus@switch:~$ nv show acl EXAMPLE1 rule 10 action dest-nat translate-ip 172.30.58.0
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show acl \<acl-id\> rule \<rule-id\> action dest-nat translate-port</h>

Shows the NAT destination translate port rules.

### Version History

Introduced in Cumulus Linux 5.7.0

### Example

```
cumulus@switch:~$ nv show acl EXAMPLE1 rule 10 action dest-nat translate-port
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show acl \<acl-id\> rule \<rule-id\> action dest-nat translate-port <translate-port-id></h>

Shows NAT destination translate rule for a specific port.

### Version History

Introduced in Cumulus Linux 5.7.0

### Example

```
cumulus@switch:~$ nv show acl EXAMPLE1 rule 10 action dest-nat translate-port 6000
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show acl \<acl-id\> rule \<rule-id\> action erspan</h></h>

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
cumulus@switch:~$ nv show acl EXAMPLE1 rule 10 action erspan
     operational  applied  pending
---  -----------  -------  -------
ttl                        200
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show acl \<acl-id\> rule \<rule-id\> action police</h>

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
cumulus@switch:~$ nv show acl EXAMPLE1 rule 10 action police
       operational  applied
-----  -----------  -------
burst               200    
mode                packet 
rate                400
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show acl \<acl-id\> rule \<rule-id\> match</h>

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
cumulus@switch:~$ nv show acl EXAMPLE1 rule 10 match
            operational  applied
----------  -----------  -------
ip                              
  protocol               tcp 
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show acl \<acl-id\> rule \<rule-id\> match ip</h>

Shows the IPv4 or IPv6 match criteria for the specified ACL rule.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<acl-id>` | The ACL name.|
| `<rule-id>` | The rule number.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show acl EXAMPLE1 rule 10 match ip
             operational  applied
-----------  -----------  -------
protocol                  tcp    
[dest-port]               200
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show acl \<acl-id\> rule \<rule-id\> match ip dest-port</h>

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
cumulus@switch:~$ nv show acl EXAMPLE1 rule 10 match ip dest-port
Ports
-----
200
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show acl \<acl-id\> rule \<rule-id\> match ip dest-port \<port-id\></h>

Shows information about a specific destination port match criteria for the specified ACL rule.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<acl-id>` | The ACL name.|
| `<rule-id>` | The rule number.|
| `<port-id>` | The port match, which be ANY, bgp, dhcp-client, http, ldaps, smtp, telnet, bfd, bootpc, dhcp-server, https, msdp, snmp, tftp, bfd-echo bootps,  domain, imap2, ntp, snmp-trap, bfd-multihop, clag, ftp, ldap, pop3, or ssh.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show acl EXAMPLE1 rule 10 match ip dest-port bgp
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show acl \<acl-id\> rule \<rule-id\> match ip ecn flags</h>

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
cumulus@switch:~$ nv show acl EXAMPLE1 rule 10 match ip ecn flags
 operational  applied
  -----------  -------
               tcp-cwr
               tcp-ece
               tcp-cwr
               tcp-ece
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show acl \<acl-id\> rule \<rule-id\> match ip source-port</h>

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
cumulus@switch:~$ nv show acl EXAMPLE1 rule 10 match ip source-port
Ports
-----
200
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show acl \<acl-id\> rule \<rule-id\> match ip tcp flags</h>

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
cumulus@switch:~$ nv show acl EXAMPLE1 rule 10 match ip tcp flags
   operational  applied
   -----------  -------
                syn
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show acl \<acl-id\> rule \<rule-id\> match ip tcp mask</h>

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
cumulus@switch:~$ nv show acl EXAMPLE1 rule 10 match ip tcp mask
   operational  applied
   -----------  -------
                syn
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show acl \<acl-id\> rule \<rule-id\> match mac</h>

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
cumulus@switch:~$ nv show acl EXAMPLE1 rule 10 match mac
                 operational  applied          
---------------  -----------  -----------------
dest-mac                      08:9e:01:ce:e2:04
dest-mac-mask                 ff:ff:ff:ff:ff:ff
source-mac                    00:00:00:00:00:12
source-mac-mask               ff:ff:ff:ff:ff:ff
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show interface \<interface-id\> acl</h>

Shows the <span class="a-tooltip">[ACLs](## "Access Control Lists")</span> on the specified interface. You use ACLs to match packets and take actions.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<interface-id>` | The interface on which the ACL operates. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show interface swp1 acl
ACL Name  Rule ID  In Packets  In Bytes  Out Packets  Out Bytes
--------  -------  ----------  --------  -----------  ---------
EXAMPLE1  10                             0            0 

```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show interface \<interface-id\> acl \<acl-id\></h>

Shows information about a specific ACL on the specified interface. You use ACLs to match packets and take actions.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<interface-id>` | The interface on which the ACL operates. |
| `<acl-id>` | The ACL name.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show interface swp1 acl EXAMPLE1
Statistics
=============
    Rule  In Packet  In Byte  Out Packet  Out Byte  Summary                
    ----  ---------  -------  ----------  --------  -----------------------
    10                        0           0 Bytes   match.ip.dest-port: 200
                                                    match.ip.protocol:  tcp
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show interface \<interface-id\> acl \<acl-id\> inbound</h>

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
cumulus@switch:~$ nv show interface swp1 acl EXAMPLE1 inbound
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show interface \<interface-id\> acl \<acl-id\> inbound control-plane</h>

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
cumulus@switch:~$ nv show interface swp1 acl EXAMPLE1 inbound control-plane
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show interface \<interface-id\> acl \<acl-id\> outbound</h>

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
cumulus@switch:~$ nv show interface swp2 acl EXAMPLE1 outbound
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show interface \<interface-id\> acl \<acl-id\> outbound control-plane</h>

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
cumulus@switch:~$ nv show interface swp1 acl EXAMPLE1 outbound control-plane
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show interface \<interface-id\> acl \<acl-id\> statistics</h>

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
cumulus@switch:~$ nv show interface swp1 acl EXAMPLE1 statistics
Rule  In Packet  In Byte  Out Packet  Out Byte  Summary                
----  ---------  -------  ----------  --------  -----------------------
10                        0           0 Bytes   match.ip.dest-port: 200
                                                match.ip.protocol:  tcp
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show interface \<interface-id\> acl \<acl-id\> statistics \<rule-id\></h>

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
cumulus@switch:~$ nv show interface swp1 acl EXAMPLE1 statistics 10
                 operational  applied
---------------  -----------  -------
match                                
  ip                                 
    protocol     tcp                 
    [dest-port]  200                 
outbound                             
  byte           0 Bytes             
  packet         0
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system acl</h>

Shows the ACL mode setting; atomic or non-atomic

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv show system acl
      applied
----  -------
mode  atomic 
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system control-plane</h>

Shows the control plane configuration.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show system control-plane
trap
=======
policer
==========
    Policer        State  Policer Rate  Policer Burst  Summary            
    -------------  -----  ------------  -------------  -------------------
    acl-log        on     100           100            Policer CBS:      7
                                                       Policer CIR:    100
                                                       Policer Id:       6
                                                       To CPU Bytes:     0
                                                       To CPU Pkts:      0
                                                       Trap Group:      18
                                                       Violated Packets: 0
    arp            on     800           800            Policer CBS:     10
                                                       Policer CIR:    800
                                                       Policer Id:       9
                                                       To CPU Bytes:     0
                                                       To CPU Pkts:      0
                                                       Trap Group:      13
                                                       Violated Packets: 0
    bfd            on     2000          2000           Policer CBS:     11
                                                       Policer CIR:   2000
                                                       Policer Id:      10
                                                       To CPU Bytes:     0
                                                       To CPU Pkts:      0
                                                       Trap Group:      17
                                                       Violated Packets: 0
    bgp            on     2000          2000           Policer CBS:     11
...
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system control-plane acl</h>

Shows the control plane ACLs configured on the switch. You use control plane ACLs to apply a single rule for all packets forwarded to the CPU regardless of the source interface or destination interface on the switch. Control plane ACLs allow you to regulate traffic forwarded to applications on the switch with more granularity than traps and to configure ACLs to block SSH from specific addresses or subnets.

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv show system control-plane acl
ACL Name   Rule ID  In Packets  In Bytes  Out Packets  Out Bytes
---------  -------  ----------  --------  -----------  ---------
ACL1       1        0           0         0            0
           65535    0           0         0            0
ACL2       1        0           0         0            0
           65535    0           0         0            0
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system control-plane acl \<acl-id\></h>

Shows information about the specified control plane ACL.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<acl-id>` | The ACL name.|

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv show system control-plane acl ACL1
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system control-plane acl \<acl-id\> statistics</h>

Shows statistics for the specified control plane ACL.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<acl-id>` | The ACL name.|

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv show system control-plane acl ACL1 statistics
Rule  In Packet  In Byte  Out Packet  Out Byte  Summary 

----  ---------  -------  ----------  --------  --------------------------- 

1     0          0 Bytes  0           0 Bytes   match.ip.dest-ip:   9.1.2.3 

2     0          0 Bytes  0           0 Bytes   match.ip.source-ip: 7.8.2.3
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system control-plane acl \<acl-id\> statistics \<rule-id\></h>

Shows statistics for the specified control plane ACL rule.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<acl-id>` | The ACL name.|
| `<rule-id>` | The rule number.|

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv show system control-plane acl ACL1 statistics 2
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system control-plane policer</h>

Shows control plane policer configuration.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show system control-plane policer
Policer        State  Policer Rate  Policer Burst  Summary            
-------------  -----  ------------  -------------  -------------------
acl-log        on     100           100            Policer CBS:      7
                                                   Policer CIR:    100
                                                   Policer Id:       6
                                                   To CPU Bytes:     0
                                                   To CPU Pkts:      0
                                                   Trap Group:      18
                                                   Violated Packets: 0
arp            on     800           800            Policer CBS:     10
                                                   Policer CIR:    800
                                                   Policer Id:       9
                                                   To CPU Bytes:     0
                                                   To CPU Pkts:      0
                                                   Trap Group:      13
                                                   Violated Packets: 0
bfd            on     2000          2000           Policer CBS:     11
...
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system control-plane policer \<policer-id\></h>

Shows configuration information for a specific control plane policer.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<policer-id>` | The policer ID: `arp`, `bfd`, `pim-ospf-rip`, `bgp`, `clag`, `icmp-def`, `dhcp-ptp`, `igmp`, `ssh`, `icmp6-neigh`, `icmp6-def-mld`, `lacp`, `lldp`, `rpvst`, `eapol`, `ip2me`, `acl-log`, `nat`, `stp`, `l3-local`, `span-cpu`, `unknown-ipmc`, `catch-all`. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show system control-plane policer bfd
                 operational  applied
---------------  -----------  -------
burst            2000                
rate             2000                
state            on                  
statistics                           
  policer-cbs    11                  
  policer-cir    2000                
  policer-id     10                  
  to-cpu-bytes   0                   
  to-cpu-pkts    0                   
  trap-group-id  17                  
  violated-pkts  0
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system control-plane policer \<policer-id\> statistics</h>

Shows statistics for a specific control plane policer.

### Command Syntax

| Syntax |  Description |
| --------- | -------------- |
| `<policer-id>` | The policer ID: `arp`, `bfd`, `pim-ospf-rip`, `bgp`, `clag`, `icmp-def`, `dhcp-ptp`, `igmp`, `ssh`, `icmp6-neigh`, `icmp6-def-mld`, `lacp`, `lldp`, `rpvst`, `eapol`, `ip2me`, `acl-log`, `nat`, `stp`, `l3-local`, `span-cpu`, `unknown-ipmc`, `catch-all`. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show system control-plane policer bfd statistics
               operational  applied
-------------  -----------  -------
policer-cbs    11                  
policer-cir    2000                
policer-id     10                  
to-cpu-bytes   0                   
to-cpu-pkts    0                   
trap-group-id  17                  
violated-pkts  0
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system control-plane trap</h>

Shows the control plane trap configuration.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show system control-plane trap
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system control-plane trap \<trap-id\></h>

Shows specific control plane trap configuration.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<trap-id>` | The trap ID. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show system control-plane trap l3-mtu-err
       operational  applied
-----  -----------  -------
state  off          off
```
