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

## <h>nv show acl acl-default-dos</h>

Shows the firewall DoS rules on the switch.

### Version History

Introduced in Cumulus Linux 5.9.0

### Example

```
cumulus@switch:~$ nv show acl acl-default-dos 
      applied  pending
----  -------  -------
type  ipv4     ipv4   
rule
=======
    Number  Summary                                 
    ------  ----------------------------------------
    30      match.ip.protocol:                   tcp
    40      match.ip.protocol:                   tcp
    41      match.ip.protocol:                   tcp
    42      match.ip.protocol:                   tcp
    50                                              
    60      match.ip.protocol:                   tcp
    70      match.ip.protocol:                   tcp
    80      match.ip.protocol:                   tcp
    90      match.ip.protocol:                   tcp
            match.ip.tcp.all-mss-except:   536-65535
    100     match.ip.recent-list.action:         set
            match.ip.tcp.dest-port:               22
    110     match.ip.recent-list.action:      update
            match.ip.recent-list.hit-count:      100
            match.ip.recent-list.update-interval: 60
            match.ip.tcp.dest-port:               22
    120     match.ip.hashlimit.burst:              2
            match.ip.hashlimit.expire:         30000
            match.ip.hashlimit.mode:          src-ip
            match.ip.hashlimit.name:          TCPRST
            match.ip.hashlimit.rate-above:     5/min
            match.ip.hashlimit.source-mask:       32
            match.ip.protocol:                   tcp
    130     match.ip.hashlimit.burst:             30
            match.ip.hashlimit.expire:         30000
            match.ip.hashlimit.mode:          src-ip
            match.ip.hashlimit.name:      TCPGENERAL
            match.ip.hashlimit.rate-above: 50/second
            match.ip.hashlimit.source-mask:       32
            match.ip.protocol:                   tcp
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show acl acl-default-dos rule \<rule-id\></h>

Shows information about the specified firewall DoS rule on the switch.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<rule-id>` | The rule number.|

### Version History

Introduced in Cumulus Linux 5.9.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show acl acl-default-dos rule 120
                   applied  pending
-----------------  -------  -------
match                              
  ip                               
    protocol       tcp      tcp    
    hashlimit                      
      name         TCPRST   TCPRST 
      rate-above   5/min    5/min  
      burst        2        2      
      source-mask  32       32     
      expire       30000    30000  
      mode         src-ip   src-ip
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show acl acl-default-whitelist</h>

Shows the firewall whitelist rules on the switch.

### Version History

Introduced in Cumulus Linux 5.9.0

### Example

```
cumulus@switch:~$ nv show acl acl-default-whitelist
      applied  pending
----  -------  -------
type  ipv4     ipv4   
rule
=======
    Number  Summary                                          
    ------  -------------------------------------------------
    5       match.ip.protocol:                            tcp
            match.ip.tcp.dest-port:                       ssh
    10      match.ip.protocol:                            tcp
            match.ip.tcp.dest-port:                       bgp
    15      match.ip.protocol:                            tcp
            match.ip.tcp.dest-port:                      ldap
    20      match.ip.protocol:                            tcp
            match.ip.tcp.dest-port:                      8765
    25      match.ip.protocol:                            tcp
            match.ip.tcp.dest-port:                     https
    30      match.ip.protocol:                            tcp
            match.ip.tcp.dest-port:                      clag
    35      match.ip.protocol:                            tcp
            match.ip.tcp.source-port:                      49
    40      match.ip.protocol:                            udp
            match.ip.udp.dest-port:               dhcp-client
    45      match.ip.protocol:                            udp
            match.ip.udp.dest-port:               dhcp-server
    50      match.ip.protocol:                            udp
            match.ip.udp.dest-port:                       ntp
    55      match.ip.protocol:                            udp
            match.ip.udp.dest-port:                       323
    60      match.ip.protocol:                            udp
            match.ip.udp.dest-port:                      snmp
    65      match.ip.protocol:                            udp
            match.ip.udp.dest-port:                      tftp
    70      match.ip.protocol:                            udp
            match.ip.udp.dest-port:                      ldap
    73      match.ip.udp.source-port:                    3020
    74      match.ip.udp.source-port:                    3022
    75      match.ip.protocol:                            udp
            match.ip.udp.source-port:                    1812
    80      match.ip.protocol:                            udp
            match.ip.udp.source-port:                    1813
    85      match.ip.protocol:                            udp
            match.ip.udp.dest-port:                      6343
    90      match.ip.protocol:                            udp
            match.ip.udp.dest-port:                      6344
    95      match.ip.protocol:                            udp
            match.ip.udp.dest-port:                       514
    100     match.ip.protocol:                            udp
            match.ip.udp.dest-port:                       bfd
    105     match.ip.protocol:                            udp
            match.ip.udp.dest-port:              bfd-multihop
    110     match.ip.protocol:                            udp
            match.ip.udp.dest-port:                      4789
    115     match.ip.protocol:                            udp
            match.ip.udp.dest-port:                       319
    120     match.ip.protocol:                            udp
            match.ip.udp.dest-port:                       320
    125     match.ip.protocol:                            tcp
            match.ip.tcp.dest-port:                      9339
    130     match.ip.protocol:                            tcp
            match.ip.tcp.dest-port:                     31980
            match.ip.tcp.dest-port:                     31982
    135     match.ip.protocol:                            tcp
            match.ip.tcp.dest-port:                       639
    140     match.ip.protocol:                            udp
            match.ip.udp.source-port:                      53
    145     match.ip.protocol:                            tcp
            match.ip.tcp.dest-port:                      9999
    150     match.ip.protocol:                           ospf
    155     match.ip.protocol:                            pim
    160     match.ip.protocol:                           vrrp
    165     match.ip.protocol:                           igmp
    170     match.ip.protocol:                           icmp
    175     match.ip.protocol:                            udp
            match.ip.udp.dest-port:                      clag
    9999    Log Level:                                      5
            action.log.log-prefix: IPTables-Dropped:
            Log Rate:                                       1
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show acl acl-default-whitelist rule \<rule-id\></h>

Shows information about the specified firewall whitelist rule on the switch.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<rule-id>` | The rule number.|

### Version History

Introduced in Cumulus Linux 5.9.0

### Example

```
cumulus@switch:~$ nv show acl acl-default-whitelist rule 150
              applied  pending
------------  -------  -------
match                         
  ip                          
    protocol  ospf     ospf 
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

## <h>nv show acl \<acl-id\> rule \<rule-id\> action recent</h>

Shows the recent action for the ACL rule.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<acl-id>` | The ACL name.|
| `<rule-id>` | The rule number.|

### Version History

Introduced in Cumulus Linux 5.9.0

### Example

```
cumulus@switch:~$ nv show acl acl-default-whitelist rule 73 action recent
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

## <h>nv show acl \<acl-id\> rule \<rule-id\> match ip connection-state</h>

Shows the connection state for the match IP ACL rule.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<acl-id>` | The ACL name.|
| `<rule-id>` | The rule number.|

### Version History

Introduced in Cumulus Linux 5.9.0

### Example

```
cumulus@switch:~$ nv show acl acl-default-whitelist rule 73 match ip connection-state
applied    
-----------
new        
established
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

## <h>nv show acl \<acl-id\> rule \<rule-id\> match ip hashlimit</h>

Shows the hash limit for the match IP ACL rule.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<acl-id>` | The ACL name.|
| `<rule-id>` | The rule number.|

### Version History

Introduced in Cumulus Linux 5.9.0

### Example

```
cumulus@switch:~$ nv show acl acl-default-whitelist rule 73 match ip hashlimit
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show acl \<acl-id\> rule \<rule-id\> match ip recent-list</h>

Shows the recent list for the match IP ACL rule.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<acl-id>` | The ACL name.|
| `<rule-id>` | The rule number.|

### Version History

Introduced in Cumulus Linux 5.9.0

### Example

```
cumulus@switch:~$ nv show acl acl-default-whitelist rule 73 match ip recent-list
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

Shows configuration information for a specific control plane policer. The policer can be: `acl-log`, `arp`, `bfd`, `bgp`, `brief`, `catch-all`, `clag`, `dhcp`, `eapol`, `icmp6-def-mld`, `icmp6-neigh`, `icmp-def`, `igmp`, `ip2me`, `l3-local`, `lacp`, `lldp-ptp`, `nat`, `pim-ospf-rip`, `rpvst`, `span-cpu`, `ssh`, `stp`, or `unknown-ipmc`.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<policer-id>` | The policer ID. |

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

Shows statistics for a specific control plane policer. The policer can be: `acl-log`, `arp`, `bfd`, `bgp`, `brief`, `catch-all`, `clag`, `dhcp`, `eapol`, `icmp6-def-mld`, `icmp6-neigh`, `icmp-def`, `igmp`, `ip2me`, `l3-local`, `lacp`, `lldp-ptp`, `nat`, `pim-ospf-rip`, `rpvst`, `span-cpu`, `ssh`, `stp`, or `unknown-ipmc`.

### Command Syntax

| Syntax |  Description |
| --------- | -------------- |
| `<policer-id>` | The policer ID. |

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
