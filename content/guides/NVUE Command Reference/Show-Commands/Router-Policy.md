---
title: Router Policy
author: Cumulus Networks
weight: 350
product: Cumulus Linux
type: nojsscroll
---
## nv show router policy

Shows route filtering and distribution configuration information. You can see configuration settings for prefix lists, community lists, AS path lists, and route maps.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show router policy
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show router policy as-path-list

Shows the AS path list policy configuration. You use an AS path list to match BGP AS paths.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show router policy as-path-list
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show router policy as-path-list \<list-id\>

Shows the specified AS path list policy configuration.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
|`<list-id>` | The AS path list name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show router policy as-path-list mylist 
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show router policy as-path-list \<list-id>\ rule

Shows the specified AS path list policy rules.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<list-id>` | The AS path list name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show router policy as-path-list mylist rule
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show router policy as-path-list \<list-id>\ rule \<rule-id\>

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
cumulus@leaf01:mgmt:~$ nv show router policy as-path-list mylist rule 10
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show router policy community-list

Shows the configured community lists. A community list is used for matching BGP community policies.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show router policy community-list
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show router policy community-list \<list-id\>

Shows the specified community list configuration.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<list-id>` |  The community list name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show router policy community-list COMMUNITY1
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show router policy community-list \<list-id\> rule

Shows the specified community list rules.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<list-id>` |  The community list name. |
| `<rule-id>` |  The rule number. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show router policy community-list COMMUNITY1 rule
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show router policy community-list \<list-id\> rule \<rule-id\>

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
cumulus@leaf01:mgmt:~$ nv show router policy community-list COMMUNITY1 rule 10
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show router policy community-list \<list-id\> rule \<rule-id\> community

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
cumulus@leaf01:mgmt:~$ nv show router policy community-list COMMUNITY1 rule 10 community
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show router policy community-list \<list-id\> rule \<rule-id\> community \<community-id\>

Shows the configuration for the specified community name for the specified community-list.

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
cumulus@leaf01:mgmt:~$ nv show router policy community-list COMMUNITY1 rule 10 community 64980:0
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show router policy ext-community-list

Shows the extended community list configuration.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show router policy ext-community-list
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show router policy ext-community-list \<list-id\>

Shows configuration for the specified extended community list used for matching BGP communities.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<list-id>` |  The extended community list name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show router policy ext-community-list EXTCOMMUNITY1
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show router policy ext-community-list \<list-id\> rule

Shows the specified extended community list rules.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<list-id>` | The extended community list name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show router policy ext-community-list EXTCOMMUNITY1 rule
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show router policy ext-community-list \<list-id\> rule \<rule-id\>

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
cumulus@leaf01:mgmt:~$ nv show router policy ext-community-list EXTCOMMUNITY1 rule 10
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show router policy ext-community-list \<list-id\> rule \<rule-id\> ext-community

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
cumulus@leaf01:mgmt:~$ nv show router policy ext-community-list MYEXTENDEDCOMMUNITYLIST rule 10 ext-community
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show router policy ext-community-list \<list-id\> rule \<rule-id\> ext-community rt

Shows the specified extended community rule Route Target Extended Community configuration.

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
cumulus@leaf01:mgmt:~$ nv show router policy ext-community-list MYEXTENDEDCOMMUNITYLIST rule 10 ext-community rt
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show router policy ext-community-list \<list-id\> rule \<rule-id\> ext-community rt \<ext-community-id\>

Shows the extended community Route Target Extended Community configuration for the specified rextended community list rule.

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
cumulus@leaf01:mgmt:~$ nv show router policy ext-community-list MYEXTENDEDCOMMUNITYLIST rule 10 ext-community rt 64510:1111
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show router policy ext-community-list \<list-id\> rule \<rule-id\> ext-community soo

Shows the site-of-origin (SoO) Extended Community rules.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<list-id>` |  The extended community list name. |
| `<rule-id>` |   The rule number. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show router policy ext-community-list MYEXTENDEDCOMMUNITYLIST rule 10 ext-community soo
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show router policy ext-community-list \<list-id\> rule \<rule-id\> ext-community soo \<ext-community-id\>

Shows the configuration for the specified site-of-origin (SoO) Extended Community rule.

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
cumulus@leaf01:mgmt:~$ nv show router policy ext-community-list MYEXTENDEDCOMMUNITYLIST rule 10 ext-community soo 45000:3soo
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show router policy large-community-list

Shows the large community lists used configured on the switch to match community based BGP policies.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show router policy large-community-list
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show router policy large-community-list \<list-id\>

Shows the specified large community list configuration.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<list-id>` |  The large community list name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show router policy large-community-list MYLARGECOMMUNITY 
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show router policy large-community-list \<list-id\> rule

Shows the rules for the specified large community list.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<list-id>` |  The large community list name. |
| `<rule-id>` |  The rule number. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show router policy large-community-list MYLARGECOMMUNITY rule
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show router policy large-community-list \<list-id\> rule \<rule-id\>

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
cumulus@leaf01:mgmt:~$ nv show router policy large-community-list MYLARGECOMMUNITY rule 10
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show router policy large-community-list \<list-id\> rule \<rule-id\> large-community

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
cumulus@leaf01:mgmt:~$ nv show router policy large-community-list MYLARGECOMMUNITY rule 10 large-community
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show router policy large-community-list \<list-id\> rule \<rule-id\> large-community \<large-community-id\>

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
cumulus@leaf01:mgmt:~$ nv show router policy large-community-list MYCOMMUNITYLIST rule 10 large-community 2914:65400:38016
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show router policy prefix-list

Shows the configured prefix lists.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ 
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show router policy prefix-list \<prefix-list-id\>

Shows the specified prefix list configuration. A prefix list is used for matching IPv4 and IPv6 address prefixes.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<prefix-list-id>` |  The prefix list name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show router policy prefix-list MYPREFIXLIST
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show router policy prefix-list \<prefix-list-id\> rule

Shows the rules for the specified prefix list.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<prefix-list-id>` |  The prefix list name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show router policy prefix-list MYPREFIXLIST rule
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show router policy prefix-list \<prefix-list-id\> rule \<rule-id\>

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
cumulus@leaf01:mgmt:~$ nv show router policy prefix-list MYPREFIXLIST rule 10
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show router policy prefix-list \<prefix-list-id\> rule \<rule-id\> match

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
cumulus@leaf01:mgmt:~$ nv show router policy prefix-list MYPREFIXLIST rule 10 match
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show router policy prefix-list \<prefix-list-id\> rule \<rule-id\> match \<match-id\>

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
cumulus@leaf01:mgmt:~$ nv show router policy prefix-list MYPREFIXLIST rule 10 match 2001:100::1/64
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show router policy route-map

Shows the route maps configured on the switch. A route map is used for policy configuration.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<route-map-id>` |  The route map name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ 
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show router policy route-map \<route-map-id\>

Shows the specified route map configuration. A route map is used for policy configuration.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<route-map-id>` | The route map name.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show router policy route-map MYROUTEMAP
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show router policy route-map \<route-map-id\> rule

Shows the rules for the specified route map.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<route-map-id>` | The route map name.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show router policy route-map MYROUTEMAP rule
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show router policy route-map \<route-map-id\> rule \<rule-id\>

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
cumulus@leaf01:mgmt:~$ nv show router policy route-map MYROUTEMAP rule 10 
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show router policy route-map \<route-map-id\> rule \<rule-id\> match

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
cumulus@leaf01:mgmt:~$ nv show router policy route-map MYROUTEMAP rule 10 match
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show router policy route-map \<route-map-id\> rule \<rule-id\> set

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
cumulus@leaf01:mgmt:~$ nv show router policy route-map MYROUTEMAP rule 10 set
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show router policy route-map \<route-map-id\> rule \<rule-id\> set as-path-prepend

Shows the set AS path prepend configuration for the specified route map rule.

AS Path prepend

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<route-map-id>` | The route map name.|
| `<rule-id>` |  The rule number. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show router policy route-map MYROUTEMAP rule 10 set as-path-prepend
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show router policy route-map \<route-map-id\> rule \<rule-id\> set community

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
cumulus@leaf01:mgmt:~$ nv show router policy route-map MYROUTEMAP rule 10 set community
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show router policy route-map \<route-map-id\> rule \<rule-id\> set community \<community-id\>

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
cumulus@leaf01:mgmt:~$ nv show router policy route-map MYROUTEMAP rule 10 set community 64980:0
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show router policy route-map \<route-map-id\> rule \<rule-id\> set large-community

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
cumulus@leaf01:mgmt:~$ nv show router policy route-map MYROUTEMAP rule 10 set large-community
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show router policy route-map \<route-map-id\> rule \<rule-id\> set large-community \<large-community-id\>

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
cumulus@leaf01:mgmt:~$ nv show router policy route-map MYROUTEMAP rule 10 set large-community 2914:65400:38016
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show router policy route-map \<route-map-id\> rule \<rule-id\> set aggregator-as

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
cumulus@leaf01:mgmt:~$ nv show router policy route-map MYROUTEMAP rule 10 set aggregator-as
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show router policy route-map \<route-map-id\> rule \<rule-id\> set aggregator-as \<asn-id\>

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
cumulus@leaf01:mgmt:~$ nv show router policy route-map MYROUTEMAP rule 10 set aggregator-as 65101
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show router policy route-map \<route-map-id\> rule \<rule-id\> set aggregator-as \<asn-id\> address

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
cumulus@leaf01:mgmt:~$ nv show router policy route-map MYROUTEMAP rule 10 set aggregator-as 65101 address
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show router policy route-map \<route-map-id\> rule \<rule-id\> set aggregator-as \<asn-id\> address \<ipv4-address-id\>

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
cumulus@leaf01:mgmt:~$ nv show router policy route-map MYROUTEMAP rule 10 set aggregator-as 65101 address 10.10.10.01
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show router policy route-map \<route-map-id\> rule \<rule-id\> action

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
cumulus@leaf01:mgmt:~$ nv show router policy route-map MYROUTEMAP rule 10 action
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show router policy route-map \<route-map-id\> rule \<rule-id\> action deny

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
cumulus@leaf01:mgmt:~$ nv show router policy route-map MYROUTEMAP rule 10 action deny
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show router policy route-map \<route-map-id\> rule \<rule-id\> action permit

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
cumulus@leaf01:mgmt:~$ nv show router policy route-map MYROUTEMAP rule 10 action permit
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show router policy route-map \<route-map-id\> rule \<rule-id\> action permit exit-policy

Shopws the permit action exit policy for the specified route map rule.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<route-map-id>` | The route map name. |
| `<rule-id>` |  The rule number. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show router policy route-map MYROUTEMAP rule 10 action permit exit-policy
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> ebgp-policy

Shows the EBGP policy configuration on the switch.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |  The VRF name.|
| `<neighbor-id>`  | The IP address of the BGP peer or the interface if you are using unnumbered BGP. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show vrf default router bgp neighbor swp51 ebgp-policy
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family

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
cumulus@leaf01:mgmt:~$ nv show vrf default router bgp neighbor swp51 address-family address-family
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv4-unicast policy inbound

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
cumulus@leaf01:mgmt:~$ nv show vrf default router bgp neighbor swp51 address-family ipv4-unicast policy inbound
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv4-unicast policy outbound

Shows the IPv4 outbound policy configuration for a specifc BGP neighbor.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |  The VRF name.|
| `<neighbor-id>`  | The IP address of the BGP peer or the interface if you are using unnumbered BGP. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show vrf default router bgp neighbor swp51 address-family ipv4-unicast policy outbound
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family l2vpn-evpn policy

Shows the EVPN policy configuration for a specifc BGP neighbor.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |  The VRF name.|
| `<neighbor-id>`  | The IP address of the BGP peer or the interface if you are using unnumbered BGP. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show vrf default router bgp neighbor swp51 address-family l2vpn-evpn policy
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family l2vpn-evpn policy inbound

Shows the EVPN inbound policy configuration for a specifc BGP neighbor.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |  The VRF name.|
| `<neighbor-id>`  | The IP address of the BGP peer or the interface if you are using unnumbered BGP. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show vrf default router bgp neighbor swp51 address-family l2vpn-evpn policy inbound
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family l2vpn-evpn policy outbound

Shows the EVPN outbound policy configuration for a specifc BGP neighbor.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |  The VRF name.|
| `<neighbor-id>`  | The IP address of the BGP peer or the interface if you are using unnumbered BGP. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show vrf default router bgp neighbor swp51 address-family l2vpn-evpn policy outbound
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv4-unicast policy

Shows the IPv4 policy configuration for a specifc BGP peer group.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |  The VRF name. |
| `<peer-group-id>`  | The BGP peer group name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show vrf default router bgp peer-group SPINES address-family ipv4-unicast policy
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv4-unicast policy inbound

Shows the IPv4 inbound policy configuration for a specifc BGP peer group.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |  The VRF name. |
| `<peer-group-id>`  | The BGP peer group name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show vrf default router bgp peer-group SPINES address-family ipv4-unicast policy inbound
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv4-unicast policy outbound

Shows the IPv4 outbound policy configuration for a specifc BGP peer group.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |  The VRF name. |
| `<peer-group-id>`  | The BGP peer group name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show vrf default router bgp peer-group SPINES address-family ipv4-unicast policy outbound
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv6-unicast policy

Shows the IPv6 policy configuration for a specifc BGP peer group.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |  The VRF name. |
| `<peer-group-id>`  | The BGP peer group name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show vrf default router bgp peer-group SPINES address-family ipv6-unicast policy
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv6-unicast policy inbound

Shows the IPv6 inbound policy configuration for a specifc BGP peer group.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |  The VRF name. |
| `<peer-group-id>`  | The BGP peer group name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show vrf default router bgp peer-group SPINES address-family ipv6-unicast policy inbound
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv6-unicast policy outbound

Shows the IPv6 outbound policy configuration for a specifc BGP peer group.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |  The VRF name. |
| `<peer-group-id>`  | The BGP peer group name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show vrf default router bgp peer-group SPINES address-family ipv6-unicast policy outbound
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family l2vpn-evpn policy

Shows the EVPN policy configuration for a specifc BGP peer group.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |  The VRF name. |
| `<peer-group-id>`  | The BGP peer group name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show vrf default router bgp peer-group SPINES address-family l2vpn-evpn policy
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family l2vpn-evpn policy inbound

Shows the EVPN inbound policy configuration for a specifc BGP peer group.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |  The VRF name. |
| `<peer-group-id>`  | The BGP peer group name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show vrf default router bgp peer-group SPINES address-family l2vpn-evpn policy inbound
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family l2vpn-evpn policy outbound

Shows the EVPN outbound policy configuration for a specifc BGP peer group.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |  The VRF name. |
| `<peer-group-id>`  | The BGP peer group name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show vrf default router bgp peer-group SPINES address-family l2vpn-evpn policy outbound
```
