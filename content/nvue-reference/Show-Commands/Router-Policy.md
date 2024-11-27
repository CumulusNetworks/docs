---
title: Router Policy
author: Cumulus Networks
weight: 350

type: nojsscroll
---
<style>
h { color: RGB(118,185,0)}
</style>
<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show router policy</h>

Shows route filtering and distribution configuration information. You can see configuration settings for prefix lists, community lists, AS path lists, and route maps.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show router policy
                      applied  pending   
--------------------  -------  ----------
[as-path-list]                 mylist    
[community-list]               COMMUNITY1
[ext-community-list]           mylist
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show router policy as-path-list \<list-id\></h>

Shows the specified AS path list policy configuration.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
|`<list-id>` | The AS path list name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show router policy as-path-list mylist
        applied  pending
------  -------  -------
[rule]           10 
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show router policy as-path-list \<list-id\> rule</h>

Shows the specified AS path list policy rules.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<list-id>` | The AS path list name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show router policy as-path-list mylist rule
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show router policy as-path-list \<list-id\> rule \<rule-id\></h>

Shows the specified AS path list policy rule configuration.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<list-id>` | The AS path list name. |
| `<rule-id>` | The rule number. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show router policy as-path-list mylist rule 10
            applied  pending
----------  -------  -------
action               permit 
aspath-exp           ^100_
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show router policy community-list</h>

Shows the configured community lists. You use a community list for matching BGP community policies.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show router policy community-list
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show router policy community-list \<list-id\></h>

Shows the specified community list configuration.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<list-id>` |  The community list name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show router policy community-list COMMUNITY1
        applied  pending
------  -------  -------
[rule]           10
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show router policy community-list \<list-id\> rule</h>

Shows the specified community list rules.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<list-id>` |  The community list name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show router policy community-list COMMUNITY1 rule
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show router policy community-list \<list-id\> rule \<rule-id\></h>

Shows the configuration for the specified community list rule.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<list-id>` |  The community list name. |
| `<rule-id>` |  The rule number. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show router policy community-list COMMUNITY1 rule 10
             applied  pending
-----------  -------  -------
action                permit 
[community]           100:100
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show router policy community-list \<list-id\> rule \<rule-id\> community</h>

Shows the community names for the specified community list rule.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<list-id>` | The community list name. |
| `<rule-id>` |  The rule number. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show router policy community-list COMMUNITY1 rule 10 community
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show router policy community-list \<list-id\> rule \<rule-id\> community \<community-id\></h>

Shows the configuration for a specific community name for the specified community-list.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<list-id>` | The community list name. |
| `<rule-id>` |  The rule number. |
| `<community-id>` | The community number in AA:NN format or well known name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show router policy community-list COMMUNITY1 rule 10 community 64980:0
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show router policy ext-community-list</h>

Shows the extended community list configuration.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show router policy ext-community-list
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show router policy ext-community-list \<list-id\></h>

Shows configuration for the specified extended community list used for matching BGP communities.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<list-id>` |  The extended community list name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show router policy ext-community-list EXTCOMMUNITY1
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show router policy ext-community-list \<list-id\> rule</h>

Shows the specified extended community list rules.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<list-id>` | The extended community list name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show router policy ext-community-list EXTCOMMUNITY1 rule
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show router policy ext-community-list \<list-id\> rule \<rule-id\></h>

Shows the matching criteria for the specified extended community list rule.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<list-id>` |  The extended community list name. |
| `<rule-id>` |  The extended community list rule number. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show router policy ext-community-list EXTCOMMUNITY1 rule 10
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show router policy ext-community-list \<list-id\> rule \<rule-id\> ext-community</h>

Shows the matching criteria for a specific extended community for the specified extended community list rule.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<list-id>` |  The extended community list name. |
| `<rule-id>` |  The rule number. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show router policy ext-community-list MYEXTENDEDCOMMUNITYLIST rule 10 ext-community
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show router policy ext-community-list \<list-id\> rule \<rule-id\> ext-community rt</h>

Shows the Route Target Extended Community configuration for the specified extended community rule.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<list-id>` |  The extended community list name. |
| `<rule-id>` |   The rule number. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show router policy ext-community-list MYEXTENDEDCOMMUNITYLIST rule 10 ext-community rt
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show router policy ext-community-list \<list-id\> rule \<rule-id\> ext-community rt \<ext-community-id\></h>

Shows the Route Target Extended Community configuration for a specified extended community list rule.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<list-id>` |  The extended community list name. |
| `<rule-id>` |   The rule number. |
| `<ext-community-id>` | The community number in AA:NN or IP:NN format. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show router policy ext-community-list MYEXTENDEDCOMMUNITYLIST rule 10 ext-community rt 64510:1111
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show router policy ext-community-list \<list-id\> rule \<rule-id\> ext-community soo</h>

Shows the site-of-origin (SoO) extended community rules.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<list-id>` |  The extended community list name. |
| `<rule-id>` |   The rule number. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show router policy ext-community-list MYEXTENDEDCOMMUNITYLIST rule 10 ext-community soo
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show router policy ext-community-list \<list-id\> rule \<rule-id\> ext-community soo \<ext-community-id\></h>

Shows the configuration for the specified site-of-origin (SoO) extended community rule.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<list-id>` |  The extended community list name. |
| `<rule-id>` |   The rule number. |
| `<ext-community-id>` | The community number in AA:NN or IP:NN format. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show router policy ext-community-list MYEXTENDEDCOMMUNITYLIST rule 10 ext-community soo 45000:3soo
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show router policy large-community-list</h>

Shows the large community lists configured on the switch to match community based BGP policies.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show router policy large-community-list
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show router policy large-community-list \<list-id\></h>

Shows the specified large community list configuration.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<list-id>` |  The large community list name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show router policy large-community-list MYLARGECOMMUNITY
        applied
------  -------
[rule]  10
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show router policy large-community-list \<list-id\> rule</h>

Shows the rules for the specified large community list.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<list-id>` |  The large community list name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show router policy large-community-list MYLARGECOMMUNITY rule
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show router policy large-community-list \<list-id\> rule \<rule-id\></h>

Shows the configuration for the specified large community list rule.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<list-id>` |  The large community list name. |
| `<rule-id>` |  The rule number. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show router policy large-community-list MYLARGECOMMUNITY rule 10
                  applied         
-----------------  ----------------
action             permit          
[large-community]  2914:65400:38016
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show router policy large-community-list \<list-id\> rule \<rule-id\> large-community</h>

Shows the community names for the specified large community list rule.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<list-id>` |  The large community list name. |
| `<rule-id>` |  The rule number. |
| `<large-community-id>` | The large community number in AA:BB:CC format. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show router policy large-community-list MYLARGECOMMUNITY rule 10 large-community
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show router policy large-community-list \<list-id\> rule \<rule-id\> large-community \<large-community-id\></h>

Shows configuration for a specific large community list rule.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<list-id>` |  The large community list name. |
| `<rule-id>` |  The rule number. |
| `<large-community-id>` |  The large community number in AA:BB:CC format. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show router policy large-community-list MYCOMMUNITYLIST rule 10 large-community 2914:65400:38016
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show router policy prefix-list</h>

Shows the configured prefix lists.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ 
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show router policy prefix-list \<prefix-list-id\></h>

Shows the specified prefix list configuration. You use a prefix list for matching IPv4 and IPv6 address prefixes.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<prefix-list-id>` |  The prefix list name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show router policy prefix-list MYPREFIXLIST
      applied
----  -------
type  ipv4
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show router policy prefix-list \<prefix-list-id\> rule</h>

Shows the rules for the specified prefix list.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<prefix-list-id>` |  The prefix list name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show router policy prefix-list MYPREFIXLIST rule
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show router policy prefix-list \<prefix-list-id\> rule \<rule-id\></h>

Shows the specified prefix list rule configuration.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<prefix-list-id>` |  The prefix list name. |
| `<rule-id>` |   Prefix List rule number |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show router policy prefix-list MYPREFIXLIST rule 10
         applied    
-------  -----------
action   permit     
[match]  10.0.0.0/16
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show router policy prefix-list \<prefix-list-id\> rule \<rule-id\> match</h>

Shows the specified prefix list rule match configuration.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<prefix-list-id>` | The prefix list name.|
| `<rule-id>` |  The rule number. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show router policy prefix-list MYPREFIXLIST rule 10 match
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show router policy prefix-list \<prefix-list-id\> rule \<rule-id\> match \<match-id\></h>

Shows configuration for the specified prefix list rule match.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<prefix-list-id>` | The prefix list name.|
| `<rule-id>` |  The rule number. |
| `<match-id>` |  The IPv4 or IPv6 prefix. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show router policy prefix-list MYPREFIXLIST rule 10 match 2001:100::1/64
                applied
--------------  -------
max-prefix-len  30     
min-prefix-len  30
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show router policy route-map</h>

Shows the route maps configured on the switch. You use a route map for policy configuration.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show router policy route-map
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show router policy route-map \<route-map-id\></h>

Shows the specified route map configuration. You use a route map for policy configuration.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<route-map-id>` | The route map name.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show router policy route-map MYROUTEMAP
        applied
------  -------
[rule]  10
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show router policy route-map \<route-map-id\> rule \<rule-id\></h>

Shows the specified route map rule configuration.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<route-map-id>` | The route map name.|
| `<rule-id>` |  The rule number. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show router policy route-map MYROUTEMAP rule 10
                   applied
-----------------  -------
match                     
  evpn-route-type  macip  
  evpn-vni         10
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show router policy route-map \<route-map-id\> rule \<rule-id\> match</h>

Shows the specified route map rule match configuration.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<route-map-id>` | The route map name.|
| `<rule-id>` |  The rule number. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show router policy route-map MAP2 rule 10 match
        applied
------  -------
origin  igp
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show router policy route-map \<route-map-id\> rule \<rule-id\> set</h>

Shows the specified route map rule set configuration.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<route-map-id>` | The route map name.|
| `<rule-id>` |  The rule number. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show router policy route-map MAP1 rule 10 set
        applied
------  -------
metric  50
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show router policy route-map \<route-map-id\> rule \<rule-id\> set as-path-prepend</h>

Shows the set AS path prepend configuration for the specified route map rule.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<route-map-id>` | The route map name.|
| `<rule-id>` |  The rule number. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show router policy route-map MYROUTEMAP rule 10 set as-path-prepend
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show router policy route-map \<route-map-id\> rule \<rule-id\> set community</h>

Shows the set BGP communities for the specified route map rule.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<route-map-id>` | The route map name. |
| `<rule-id>` |  The rule number. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show router policy route-map MYROUTEMAP rule 10 set community
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show router policy route-map \<route-map-id\> rule \<rule-id\> set community \<community-id\></h>

Shows the set configuration for a specific BGP community for the specified route map rule.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<route-map-id>` | The route map name. |
| `<rule-id>` |  The rule number. |
| `<community-id>` |  The BGP community ID. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show router policy route-map MYROUTEMAP rule 10 set community 64980:0
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show router policy route-map \<route-map-id\> rule \<rule-id\> set large-community</h>

Shows the set large BGP communities for the specified route map rule.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<route-map-id>` | The route map name. |
| `<rule-id>` |  The rule number. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show router policy route-map MYROUTEMAP rule 10 set large-community
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show router policy route-map \<route-map-id\> rule \<rule-id\> set large-community \<large-community-id\></h>

Shows the set configuration for a specific large BGP community for the specified route map rule.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<route-map-id>` | The route map name. |
| `<rule-id>` |  The rule number. |
| `<large-community-id>` |  The BGP large community ID. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show router policy route-map MYROUTEMAP rule 10 set large-community 2914:65400:38016
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show router policy route-map \<route-map-id\> rule \<rule-id\> set aggregator-as</h>

Shows the set aggregator ASNs for the specified route map rule.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<route-map-id>` | The route map name. |
| `<rule-id>` |  The rule number. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show router policy route-map MYROUTEMAP rule 10 set aggregator-as
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show router policy route-map \<route-map-id\> rule \<rule-id\> set aggregator-as \<asn-id\></h>

Shows the set configuration for a specific aggregator ASN for the specified route map rule.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<route-map-id>` | The route map name. |
| `<rule-id>` |  The rule number. |
| `<asn-id>` |   The autonomous number (ASN). |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show router policy route-map MYROUTEMAP rule 10 set aggregator-as 65101
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show router policy route-map \<route-map-id\> rule \<rule-id\> set aggregator-as \<asn-id\> address</h>

Shows the set ASN IPv4 addresses for the specified route map rule.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<route-map-id>` | The route map name. |
| `<rule-id>` |  The rule number. |
| `<asn-id>` |   The autonomous number (ASN). |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show router policy route-map MYROUTEMAP rule 10 set aggregator-as 65101 address
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show router policy route-map \<route-map-id\> rule \<rule-id\> set aggregator-as \<asn-id\> address \<ipv4-address-id\></h>

Shows the configuration for a specific ASN and IPv4 address for the specified route map rule.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<route-map-id>` | The route map name. |
| `<rule-id>` |  The rule number. |
| `<asn-id>` |   The autonomous number (ASN). |
| `<ipv4-address-id>`  | The IPv4 address. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show router policy route-map MYROUTEMAP rule 10 set aggregator-as 65101 address 10.10.10.01
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show router policy route-map \<route-map-id\> rule \<rule-id\> action</h>

Shows the route map rule action.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<route-map-id>` | The route map name. |
| `<rule-id>` |  The rule number. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show router policy route-map MYROUTEMAP rule 10 action
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show router policy route-map \<route-map-id\> rule \<rule-id\> action deny</h>

Shows the deny action for the specified route map rule.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<route-map-id>` | The route map name. |
| `<rule-id>` |  The rule number. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show router policy route-map MYROUTEMAP rule 10 action deny
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show router policy route-map \<route-map-id\> rule \<rule-id\> action permit</h>

Shows the permit action for the specified route map rule.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<route-map-id>` | The route map name. |
| `<rule-id>` |  The rule number. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show router policy route-map MYROUTEMAP rule 10 action permit
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show router policy route-map \<route-map-id\> rule \<rule-id\> action permit exit-policy</h>

Shows the permit action exit policy for the specified route map rule.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<route-map-id>` | The route map name. |
| `<rule-id>` |  The rule number. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show router policy route-map MYROUTEMAP rule 10 action permit exit-policy
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> ebgp-policy</h>

Shows the eBGP policy configuration on the switch.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |  The VRF name.|
| `<neighbor-id>`  | The IP address of the BGP peer or the interface if you are using unnumbered BGP. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp neighbor swp51 ebgp-policy
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family</h>

Shows the IPv4, IPv6, and EVPN configuration settings for the specified BGP neighbor.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |  The VRF name.|
| `<neighbor-id>`  | The IP address of the BGP peer or the interface if you are using unnumbered BGP. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp neighbor swp51 address-family address-family
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv4-unicast policy inbound</h>

Shows the IPv4 inbound policy configuration for the specified BGP neighbor.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |  The VRF name.|
| `<neighbor-id>`  | The IP address of the BGP peer or the interface if you are using unnumbered BGP. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp neighbor swp51 address-family ipv4-unicast policy inbound
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv4-unicast policy outbound</h>

Shows the IPv4 outbound policy configuration for a specific BGP neighbor.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |  The VRF name.|
| `<neighbor-id>`  | The IP address of the BGP peer or the interface if you are using unnumbered BGP. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp neighbor swp51 address-family ipv4-unicast policy outbound
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family l2vpn-evpn policy</h>

Shows the EVPN policy configuration for a specific BGP neighbor.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |  The VRF name.|
| `<neighbor-id>`  | The IP address of the BGP peer or the interface if you are using unnumbered BGP. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp neighbor swp51 address-family l2vpn-evpn policy
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family l2vpn-evpn policy inbound</h>

Shows the EVPN inbound policy configuration for a specific BGP neighbor.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |  The VRF name.|
| `<neighbor-id>`  | The IP address of the BGP peer or the interface if you are using unnumbered BGP. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp neighbor swp51 address-family l2vpn-evpn policy inbound
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family l2vpn-evpn policy outbound</h>

Shows the EVPN outbound policy configuration for a specific BGP neighbor.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |  The VRF name.|
| `<neighbor-id>`  | The IP address of the BGP peer or the interface if you are using unnumbered BGP. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp neighbor swp51 address-family l2vpn-evpn policy outbound
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv4-unicast policy</h>

Shows the IPv4 policy configuration for a specific BGP peer group.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |  The VRF name. |
| `<peer-group-id>`  | The BGP peer group name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp peer-group SPINES address-family ipv4-unicast policy
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv4-unicast policy inbound</h>

Shows the IPv4 inbound policy configuration for a specific BGP peer group.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |  The VRF name. |
| `<peer-group-id>`  | The BGP peer group name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp peer-group SPINES address-family ipv4-unicast policy inbound
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv4-unicast policy outbound</h>

Shows the IPv4 outbound policy configuration for a specific BGP peer group.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |  The VRF name. |
| `<peer-group-id>`  | The BGP peer group name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp peer-group SPINES address-family ipv4-unicast policy outbound
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv6-unicast policy</h>

Shows the IPv6 policy configuration for a specific BGP peer group.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |  The VRF name. |
| `<peer-group-id>`  | The BGP peer group name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp peer-group SPINES address-family ipv6-unicast policy
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv6-unicast policy inbound</h>

Shows the IPv6 inbound policy configuration for a specific BGP peer group.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |  The VRF name. |
| `<peer-group-id>`  | The BGP peer group name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp peer-group SPINES address-family ipv6-unicast policy inbound
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv6-unicast policy outbound</h>

Shows the IPv6 outbound policy configuration for a specific BGP peer group.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |  The VRF name. |
| `<peer-group-id>`  | The BGP peer group name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp peer-group SPINES address-family ipv6-unicast policy outbound
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family l2vpn-evpn policy</h>

Shows the EVPN policy configuration for a specific BGP peer group.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |  The VRF name. |
| `<peer-group-id>`  | The BGP peer group name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp peer-group SPINES address-family l2vpn-evpn policy
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family l2vpn-evpn policy inbound</h>

Shows the EVPN inbound policy configuration for a specific BGP peer group.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |  The VRF name. |
| `<peer-group-id>`  | The BGP peer group name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp peer-group SPINES address-family l2vpn-evpn policy inbound
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family l2vpn-evpn policy outbound</h>

Shows the EVPN outbound policy configuration for a specific BGP peer group.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |  The VRF name. |
| `<peer-group-id>`  | The BGP peer group name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show vrf default router bgp peer-group SPINES address-family l2vpn-evpn policy outbound
```
