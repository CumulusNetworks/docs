---
title: Router Policy
author: Cumulus Networks
weight: 720

type: nojsscroll
---
<style>
h { color: RGB(118,185,0)}
</style>
{{%notice note%}}
The `nv unset` commands remove the configuration you set with the equivalent `nv set` commands. This guide only describes an `nv unset` command if it differs from the `nv set` command.
{{%/notice%}}

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set router policy</h>

Configures a router policy.

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set router policy as-path-list \<list-id\></h>

Sets the name of the AS path access list you want to use to match AS paths.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<list-id>` | The AS path list name.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set router policy as-path-list mylist
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set router policy as-path-list \<list-id\> rule \<rule-id\></h>

Configures the AS path list rule number.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<list-id>` |  The AS Path list name. |
| `<rule-id>` |  The prefix list rule number. |

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set router policy as-path-list mylist rule 10
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set router policy as-path-list \<list-id\> rule \<rule-id\> action</h>

Sets the action you want to take for a match. You can set `permit` or `deny`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<list-id>` |  The AS path list name. |
| `<rule-id>` |  The AS path list rule number. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set router policy as-path-list mylist rule 10 action permit
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set router policy as-path-list \<list-id\> rule \<rule-id\> aspath-exp \<bgp-regex\></h>

Configures the regular expression you want to use to match BGP AS paths.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<list-id>` | The AS path list name. |
| `<rule-id>` | The AS path list rule number. |
| `bgp-regex` | The regular expression you want to use to match BGP AS paths.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set router policy as-path-list mylist rule 10 aspath-exp ^100_
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set router policy community-list \<list-id\></h>

Configures the name of the community list you want to use to match BGP community policies.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<list-id>` |  The community list name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set router policy community-list COMMUNITY1
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set router policy community-list \<list-id\> rule</h>

Configures the community list rule.

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set router policy community-list \<list-id\> rule \<rule-id\> action</h>

Sets the action you want to take when you meet the match criteria. You can set `permit` or `deny`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<list-id>`  | The community list name. |
| `<rule-id>`  | The community list rule number. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set router policy community-list COMMUNITY1 rule 10 action permit
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set router policy community-list \<list-id\> rule \<rule-id\> community \<community-id\></h>

Sets the name of the community you want to match.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<list-id>` | The community list name. |
| `<rule-id>` | The community list rule number. |
| `<community-id>` | The community number in AA:NN format or the well-known name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set router policy community-list COMMUNITY1 rule 10 community 100:100
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set router policy ext-community-list \<list-id\></h>

Sets the name of the extended community list you want to use to match BGP communities.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<list-id>` | The extended community list name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set router policy ext-community-list mylist
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set router policy ext-community-list \<list-id\> rule \<rule-id\></h>

Sets the extended community list rule number.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<list-id>` |  The extended community list name. |
| `<rule-id>` |  The extended community list rule number. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set router policy ext-community-list mylist rule 10
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set router policy ext-community-list \<list-id\> rule \<rule-id\> action</h>

Configures the action to take on a match. You can set `permit` or `deny`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<list-id>` |  The extended community list name. |
| `<rule-id>` |  The extended community list rule number. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set router policy ext-community-list mylist rule 10 action permit
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set router policy ext-community-list \<list-id\> rule \<rule-id\> ext-community</h>

Configures the extended community.

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set router policy ext-community-list \<list-id\> rule \<rule-id\> ext-community rt \<ext-community-id\></h>

Configures the extended community number.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<list-id>` |  The extended community list name. |
| `<rule-id>` |  The extended community list rule number. |
| `<ext-community-id>` | The extended community number in AA:NN or IP:NN format. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set router policy ext-community-list mylist rule 10 ext-community rt 64510:1111
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set router policy ext-community-list \<list-id\> rule \<rule-id\> ext-community soo \<ext-community-id\></h>

Configures the site-of-origin (SoO) extended community to identify routes that originate from a certain site so that you can prevent readvertising that prefix back to the source site.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<list-id>` | The extended community list name. |
| `<rule-id>` |  The extended community list rule number. |
| `<ext-community-id>` | The extended community number in AA:NN or IP:NN format. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set router policy ext-community-list mylist rule 10 ext-community soo 45000:3
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set router policy large-community-list \<list-id\></h>

Configures the name of the large community list you want to use to match community based BGP policies.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<list-id>`  | The large community list name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set router policy large-community-list mylist
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set router policy large-community-list \<list-id\> rule \<rule-id\></h>

Configures the large community list rule number.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<list-id>` | The large community list name |
| `<rule-id>`  | The large community list rule number. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set router policy large-community-list mylist rule 10
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set router policy large-community-list \<list-id\> rule \<rule-id\> action</h>

Configures the action for the large community list policy match. You can specify `permit` or `deny`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<list-id>` |  The large community list name. |
| `<rule-id>` | The large community list rule number. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set router policy large-community-list mylist rule 10 action permit
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set router policy large-community-list \<list-id\> rule \<rule-id\> large-community \<large-community-id\></h>

Configures the community names for the large community list.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<list-id>` |  The large community list name. |
| `<rule-id>` | The large community list rule number. |
| `<large-community-id>` | The community number in AA:BB:CC format. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set router policy large-community-list mylist rule 10 large-community 2914:65400:38016
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set router policy prefix-list \<prefix-list-id\></h>

Configures the name of the prefix list you want to use to match IPv4 and IPv6 address prefixes.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<prefix-list-id>` |  The prefix list name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set router policy prefix-list mylist
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set router policy prefix-list \<prefix-list-id\> rule \<rule-id\></h>

Configures the prefix list rule number.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<prefix-list-id>`  | The prefix list name. |
| `<rule-id>`  | The prefix list rule number. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set router policy prefix-list mylist rule 10
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set router policy prefix-list \<list-id\> rule \<rule-id\> action</h>

Configures the action to take on a match; `permit` or `deny`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<list-id>` |  The prefix list name. |
| `<rule-id>` |  The prefix list rule number. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set router policy prefix-list mylist rule 10 action permit
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set router policy prefix-list \<prefix-list-id\> rule \<rule-id\> match \<match-id\></h>

Configures the prefix match criteria you want to use.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<prefix-list-id>` | The prefix list name. |
| `<rule-id>` | The prefix list rule number. |
| `<match-id>` | The IPv4 or IPv6 prefix you want to match.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set router policy prefix-list mylist rule 10 match 10.0.0.0/16
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set router policy prefix-list \<prefix-list-id\> rule \<rule-id\> match \<match-id\> max-prefix-len</h>

Configures the maximum prefix length you want to match. You can specify a value between 0 and 128.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<prefix-list-id>` | The prefix list name.  |
| `<rule-id>` |  The prefix list rule number. |
| `<match-id>` |  The IPv4 or IPv6 prefix. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set router policy prefix-list mylist rule 10 match 10.0.0.0/16 max-prefix-len 30
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set router policy prefix-list \<prefix-list-id\> rule \<rule-id\> match \<match-id\> min-prefix-len</h>

Configures the minimum prefix length you want to match.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<prefix-list-id>` | The prefix list name. |
| `<rule-id>`  | The prefix list rule number. |
| `<match-id>` | The IPv4 or IPv6 prefix. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set router policy prefix-list mylist rule 10 match 10.0.0.0/16 min-prefix-len 30
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set router policy prefix-list \<list-id\> type</h>

Configures the type of prefix list; IPv4 or IPv6. The default setting is `ipv4`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<list-id>` |  The prefix list name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set router policy prefix-list mylist type ipv4
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set router policy route-map \<route-map-id\></h>

Configures the name of the route map you want to use for policy configuration.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<route-map-id>` |  The route map name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set router policy route-map MAP1
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set router policy route-map \<route-map-id\> rule \<rule-id\></h>

Configures the route map rule number.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<route-map-id>` | The route map name. |
| `<rule-id>` | The route map rule number.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set router policy route-map MAP1 rule 10 
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set router policy route-map \<route-map-id\> rule \<rule-id\> action</h>

Configures the route map rule action; `permit` or `deny`.

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set router policy route-map \<route-map-id\> rule \<rule-id\> action deny</h>

Configures the route map rule action to `deny`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<route-map-id>` | The route map name. |
| `<rule-id>` | The route map rule number.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set router policy route-map MAP1 rule 10 action deny
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set router policy route-map \<route-map-id\> rule \<rule-id\> action permit</h>

Configures the route map rule action to `permit`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<route-map-id>` | The route map name. |
| `<rule-id>` | The route map rule number.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set router policy route-map MAP1 rule 10 permit
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set router policy route-map \<route-map-id\> rule \<rule-id\> action permit exit-policy</h>

Configures the permit action exit policy. You can specify an alternative exit policy to take if the entry matches, instead of the normal policy of exiting the route map and permitting the route. You can configure the permit action exit policy to exit further rule processing, go to the next rule, or go to a specific rule.

### Version History

Introduced in Cumulus Linux 5.0.0

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set router policy route-map \<route-map-id\> rule \<rule-id\> action permit exit-policy exit \<value\></h>

Configures the permit action exit policy to exit further rule processing. You can specify a value between 1 and 65535.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<route-map-id>` | The route map name. |
| `<rule-id>` | The route map rule number.|

### Version History

Introduced in Cumulus Linux 5.7.0

### Example

```
cumulus@switch:~$ nv set router policy route-map MAP1 rule 10 action permit exit-policy exit 3
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set router policy route-map \<route-map-id\> rule \<rule-id\> action permit exit-policy next-rule \<value\></h>

Configures the route map to go to the next rule when the matching conditions are met.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<route-map-id>` | The route map name. |
| `<rule-id>` | The route map rule number.|

### Version History

Introduced in Cumulus Linux 5.7.0

### Example

```
cumulus@switch:~$ nv set router policy route-map MAP1 rule 10 action permit exit-policy next-rule
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set router policy route-map \<route-map-id\> rule \<rule-id\> action permit exit-policy rule \<value\></h>

Configures the route map to go to a specific rule when you meet the matching conditions.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<route-map-id>` | The route map name. |
| `<rule-id>` | The route map rule number.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set router policy route-map MAP1 rule 10 action permit exit-policy rule 20
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set router policy route-map \<route-map-id\> rule \<rule-id\> description</h>

Configures the route map rule description. If the description is more than one word, enclose it in double quotes (").

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<route-map-id>` | The route map name. |
| `<rule-id>` | The route map rule number.|

### Version History

Introduced in Cumulus Linux 5.2.0

### Example

```
cumulus@switch:~$ nv set router policy route-map MAP1 rule 10 description "this is my route map description"
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set router policy route-map \<route-map-id\> rule \<rule-id\> match</h>

Configures the match criteria you want to use for the route map rule.

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set router policy route-map \<route-map-id\> rule \<rule-id\> match as-path-list \<instance-name\></h>

Configures the name of the BGP AS path list you want use in the route map.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<route-map-id>` | The route map name. |
| `<rule-id>` | The route map rule number.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set router policy route-map MAP1 rule 10 match as-path-list MYLIST
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set router policy route-map \<route-map-id\> rule \<rule-id\> match community-list \<instance-name\></h>

Configures the name of the BGP community list you want to use in the route map.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<route-map-id>` | The route map name. |
| `<rule-id>` | The route map rule number.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set router policy route-map MAP1 rule 10 match community-list MYLIST
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set router policy route-map \<route-map-id\> rule \<rule-id\> match evpn-default-route</h>

Configures Cumulus Linux to match the EVPN default route in the route map. You can set the value to `on` or `off`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<route-map-id>` | The route map name. |
| `<rule-id>` | The route map rule number.|

### Version History

Introduced in Cumulus Linux 5.2.0

### Example

```
cumulus@switch:~$ nv set router policy route-map MAP1 rule 10 match evpn-default-route on
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set router policy route-map \<route-map-id\> rule \<rule-id\> match evpn-route-type</h>

Configures the EVPN route type you want to match in the route map. You can specify type 2 (MAC or IP advertisement routes), type 3 (Inclusive multicast Ethernet tag routes), or type 5 (IP prefix routes).

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<route-map-id>` | The route map name. |
| `<rule-id>` | The route map rule number.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set router policy route-map MAP1 rule 10 match evpn-route-type macip
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set router policy route-map \<route-map-id\> rule \<rule-id\> match evpn-vni \<value\></h>

Configures the VNI ID you want to use a match in the route map.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<route-map-id>` | The route map name. |
| `<rule-id>` | The route map rule number.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set router policy route-map MAP1 rule 10 match evpn-vni 10
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set router policy route-map \<route-map-id\> rule \<rule-id\> match interface \<interface-name\></h>

Configures the interface you want to use as a match in the route map.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<route-map-id>` | The route map name. |
| `<rule-id>` | The route map rule number.|
| `<interface-name>` | The interface or VRF name.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set router policy route-map MAP1 rule 10 match interface swp51
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set router policy route-map \<route-map-id\> rule \<rule-id\> match ip-nexthop \<address\></h>

Configures the route map to match the IP address of a next hop.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<route-map-id>` | The route map name. |
| `<rule-id>` | The route map rule number.|
| `<address>` | The IPv4 or IPv6 address of the next hop.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set router policy route-map MAP1 rule 10 match ip-nexthop 10.10.101
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set router policy route-map \<route-map-id\> rule \<rule-id\> match ip-nexthop-len</h>

Configures the route map to match an IP nexthop prefix length.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<route-map-id>` | The route map name. |
| `<rule-id>` | The route map rule number.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set router policy route-map MAP1 rule 10 match ip-nexthop-len 32
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set router policy route-map \<route-map-id\> rule \<rule-id\> match ip-nexthop-list</h>

Configures the IP next hop list you want to use as a match in the route map.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<route-map-id>` | The route map name. |
| `<rule-id>` | The route map rule number.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set router policy route-map MAP1 rule 10 match ip-nexthop-list prefixlist1
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set router policy route-map \<route-map-id\> rule \<rule-id\> match ip-nexthop-type blackhole</h>

Configures the route map to match a null route (blackhole).

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<route-map-id>` | The route map name. |
| `<rule-id>` | The route map rule number.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set router policy route-map MAP1 rule 10 match ip-nexthop-type blackhole
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set router policy route-map \<route-map-id\> rule \<rule-id\> match ip-prefix-list</h>

Configures the IP prefix list to use as a match in the route map.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<route-map-id>` | The route map name. |
| `<rule-id>`  |  The route map rule number. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set router policy route-map MAP1 rule 10 match ip-prefix-list prefixlist1
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set router policy route-map \<route-map-id\> rule \<rule-id\> match ip-prefix-len</h>

Configures the IP address prefix length you want to match. You can specify a value between 0 and 128.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<route-map-id>` | The route map name. |
| `<rule-id>` | The route map rule number.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set router policy route-map MAP1 rule 10 match ip-prefix-len 128
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set router policy route-map \<route-map-id\> rule \<rule-id\> match large-community-list \<instance-name\></h>

Configures the name of the BGP large community list you want to use in the route map.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<route-map-id>` | The route map name. |
| `<rule-id>` | The route map rule number.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set router policy route-map MAP1 rule 10 match large-community-list MYLIST
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set router policy route-map \<route-map-id\> rule \<rule-id\> match local-preference</h>

Configures the local preference of the route you want to match in the route map. You can specify a value between 0 and 4294967295.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<route-map-id>` | The route map name. |
| `<rule-id>` | The route map rule number.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set router policy route-map MAP1 rule 10 match local-preference 300
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set router policy route-map \<route-map-id\> rule \<rule-id\> match metric</h>

Configures the route metric (the cost values used by routers to determine the best path to a destination network) you want to use as a match in the route map.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<route-map-id>` | The route map name. |
| `<rule-id>` | The route map rule number.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set router policy route-map MAP1 rule 10 match metric 1
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set router policy route-map \<route-map-id\> rule \<rule-id\> match origin</h>

Configures the BGP origin you want to use as a match in the route map. You can specify `egp`, `igp`, or `incomplete`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<route-map-id>` | The route map name. |
| `<rule-id>` | The route map rule number.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set router policy route-map MAP1 rule 10 match origin igp
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set router policy route-map \<route-map-id\> rule \<rule-id\> match peer</h>

Configures the BGP peer you want to use as a match in the route map. You can specify `local`, the interface, or the IPv4 or IPv6 address.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<route-map-id>` | The route map name. |
| `<rule-id>` | The route map rule number.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set router policy route-map MAP1 rule 10 match peer swp51
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set router policy route-map \<route-map-id\> rule \<rule-id\> match source-protocol</h>

Configures the source protocol you want to use as a match in the route map. The source protocol is the protocol through which the switch learns the route. You can specify `bgp`, `connected`, `kernel`, `ospf`, `spf6`, `sharp` or `static`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<route-map-id>` | The route map name. |
| `<rule-id>` | The route map rule number.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set router policy route-map MAP1 rule 10 match source-protocol bgp
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set router policy route-map \<route-map-id\> rule \<rule-id\> match source-vrf \<vrf-name\></h>

Configures the source VRF you want to use as a match in the route map.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<route-map-id>` | The route map name. |
| `<rule-id>` | The route map rule number.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set router policy route-map MAP1 rule 10 match source-vrf RED
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set router policy route-map \<route-map-id\> rule \<rule-id\> match tag</h>

Configures the BGP tag you want to use as a match in the route map. You can specify a value between 1 and 4294967295.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<route-map-id>` | The route map name. |
| `<rule-id>` | The route map rule number.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set router policy route-map MAP1 rule 10 match tag 10
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set router policy route-map \<route-map-id\> rule \<rule-id\> match type</h>

Configures the route types you want to use as a match in the route map. You can specify IPv4 or IPv6 routes.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<route-map-id>` | The route map name. |
| `<rule-id>` | The route map rule number.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set router policy route-map MAP1 rule 10 match ipv4
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set router policy route-map \<route-map-id\> rule \<rule-id\> set</h>

Configures the route map rule set.

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set router policy route-map \<route-map-id\> rule \<rule-id\> set aggregator-as \<asn-id\></h>

Sets the aggregator ASN for a matched route.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<route-map-id>` | The route map name. |
| `<rule-id>` | The route map rule number.|
| `<asn-id>` | The ASN.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set router policy route-map MAP1 rule 10 set aggregator-as 65101
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set router policy route-map \<route-map-id\> rule \<rule-id\> set aggregator-as \<asn-id\> address \<ipv4-address\></h>

Sets the originating AS of an aggregated route if there is a match.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<route-map-id>` | The route map name. |
| `<rule-id>` | The route map rule number.|
| `<asn-id>` | The ASN number.|
| `<ipv4-address-id>` |  The IPv4 address. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set router policy route-map MAP1 rule 10 set aggregator-as 65101 address 10.10.10.01
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set router policy route-map \<route-map-id\> rule \<rule-id\> set as-path-exclude</h>

Configures a set clause in the route map to remove the ASN from the AS path attribute of the route. You can specify a value between 1 and 4294967295.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<route-map-id>` | The route map name. |
| `<rule-id>` | The route map rule number.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set router policy route-map MAP1 rule 10 set as-path-exclude 65101
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set router policy route-map \<route-map-id\> rule \<rule-id\> set as-path-prepend</h>

Sets the BGP AS path you want to prepend for a matched route.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<route-map-id>` | The route map name. |
| `<rule-id>` | The route map rule number.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set router policy route-map MAP1 rule 10 set as-path-prepend
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set router policy route-map \<route-map-id\> rule \<rule-id\> set as-path-prepend as</h>

Sets the BGP ASN to prepend for a matched route.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<route-map-id>` | The route map name. |
| `<rule-id>` | The route map rule number.|

### Version History

Introduced in Cumulus Linux 5.2.0

### Example

```
cumulus@switch:~$ nv set router policy route-map MAP1 rule 10 set as-path-prepend as 65101
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set router policy route-map \<route-map-id\> rule \<rule-id\> set as-path-prepend last-as</h>

Sets the last BGP AS path to prepend for a matched route. You can set a value between 1 and 10.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<route-map-id>` | The route map name. |
| `<rule-id>` | The route map rule number.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set router policy route-map MAP1 rule 10 set as-path-prepend as last-as 4
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set router policy route-map \<route-map-id\> rule \<rule-id\> set atomic-aggregate (on|off)</h>

Configures a set clause in the route map to inform BGP peers that the local router is using a less specific (aggregated) route to a destination. You can specify `on` or `off`. The default setting is `off`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<route-map-id>` | The route map name. |
| `<rule-id>` | The route map rule number.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set router policy route-map MAP1 rule 10 set atomic-aggregate on
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set router policy route-map \<route-map-id\> rule \<rule-id\> set community \<community-id\></h>

Sets the BGP community attribute for a matched route.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<route-map-id>` | The route map name. |
| `<rule-id>` | The route map rule number.|
| `<community-id>` | The community number in AA:NN format or the well-known name.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set router policy route-map MAP1 rule 10 set community 100:100
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set router policy route-map \<route-map-id\> rule \<rule-id\> set community-delete-list</h>

Configures a set clause in the route map to remove BGP communities from advertising to other BGP routes.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<route-map-id>` | The route map name. |
| `<rule-id>` | The route map rule number.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set router policy route-map MAP1 rule 10 set community-delete-list communitylist1
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set router policy route-map \<route-map-id\> rule \<rule-id\> set ip-nexthop</h>

Configures a set clause in the route map for the next hop address for a packet regardless of the explicit route for the packet. You can specify the IP address of the next hop. Alternatively, you can specify `peer-addr` to set the next hop as the IP address of the peer for incoming route maps or the local peering address on the switch for outgoing route maps.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<route-map-id>` | The route map name. |
| `<rule-id>` | The route map rule number.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set router policy route-map MAP1 rule 10 set ip-nexthop peer-addr
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set router policy route-map \<route-map-id\> rule \<rule-id\> set ipv6-nexthop-global</h>

Configures a set clause in the route map for IPv6 next hop global address.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<route-map-id>` | The route map name. |
| `<rule-id>` | The route map rule number.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set router policy route-map MAP1 rule 10 set ipv6-nexthop-global 2001:db8:0002::0a00:0002
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set router policy route-map \<route-map-id\> rule \<rule-id\> set ipv6-nexthop-local</h>

Configures a set clause in the route map for the IPv6 next hop local address.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<route-map-id>` | The route map name. |
| `<rule-id>` | The route map rule number.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set router policy route-map MAP1 rule 10 set ipv6-nexthop-local 2001:db8:0002::0a00:0002
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set router policy route-map \<route-map-id\> rule \<rule-id\> set ipv6-nexthop-prefer-global</h>

Configures a set clause in the route map to use the global address as the IPv6 next hop.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<route-map-id>` | The route map name. |
| `<rule-id>` | The route map rule number.|

### Version History

Introduced in Cumulus Linux 5.1.0

### Example

```
cumulus@switch:~$ nv set router policy route-map MAP1 rule 10 set ipv6-nexthop-prefer-global on
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set router policy route-map \<route-map-id\> rule \<rule-id\> set large-community \<large-community-id\></h>

Sets the large BGP community for a matched route.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<route-map-id>` | The route map name. |
| `<rule-id>` | The route map rule number.|
| `<large-community-id>` | The large community number in AA:BB:CC format.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set router policy route-map MAP1 rule 10 set large-community 2914:65400:38016
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set router policy route-map \<route-map-id\> rule \<rule-id\> set ext-community-bw</h>

Sets the BGP extended community for a matched route. You can specify `cumulative` `multipaths` `cumulative-non-transitive`, or `multipaths-non-transitive`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<route-map-id>` | The route map name. |
| `<rule-id>` | The route map rule number.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set router policy route-map MAP1 rule 10 set ext-community-bw multipaths.
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set router policy route-map \<route-map-id\> rule \<rule-id\> set ext-community-rt \<route-distinguisher\></h>

Sets the route target extended community for a matched route.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<route-map-id>` | The route map name. |
| `<rule-id>` | The route map rule number.|
|`<route-distinguisher>` | The route distinguisher. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set router policy route-map MAP1 rule 10 set ext-community-rt 64510:1111
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set router policy route-map \<route-map-id\> rule \<rule-id\> set ext-community-soo \<route-distinguisher\></h>

Sets the site-of-origin (SoO) extended community for a matched route.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<route-map-id>` | The route map name. |
| `<rule-id>` | The route map rule number.|
| `<route-distinguisher>` |The route distinguisher. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set router policy route-map MAP1 rule 10 set ext-community-soo 100:30
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set router policy route-map \<route-map-id\> rule \<rule-id\> set forwarding-address</h>

Configures the IPv6 forwarding address you want to set for the route in the route map.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<route-map-id>` | The route map name. |
| `<rule-id>` | The route map rule number.|

### Version History

Introduced in Cumulus Linux 5.2.0

### Example

```
cumulus@switch:~$ nv set router policy route-map MAP1 rule 10 set forwarding-address 2001:100::1/64
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set router policy route-map \<route-map-id\> rule \<rule-id\> set label-index</h>

Configures the label index value you want to set for the route in the route map. You can set a value between 0 and 1048560.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<route-map-id>` | The route map name. |
| `<rule-id>` | The route map rule number.|

### Version History

Introduced in Cumulus Linux 5.2.0

### Example

```
cumulus@switch:~$ nv set router policy route-map MAP1 rule 10 set label-index 1000
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set router policy route-map \<route-map-id\> rule \<rule-id\> set large-community-delete-list</h>

Configures a set clause in the route map to remove BGP large communities from advertising to other BGP routes.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<route-map-id>` | The route map name. |
| `<rule-id>` | The route map rule number.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set router policy route-map MAP1 rule 10 set large-community-delete-list largecommunitylist1
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set router policy route-map \<route-map-id\> rule \<rule-id\> set local-preference</h>

Sets the BGP local preference for a matched route. You can specify a value between 0 and 4294967295.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<route-map-id>` | The route map name. |
| `<rule-id>` | The route map rule number.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set router policy route-map MAP1 rule 10 set local-preference 300
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set router policy route-map \<route-map-id\> rule \<rule-id\> set metric</h>

Configures a set clause in the route map for the metric value for the destination routing protocol. You can set the value to `rtt`, `rtt-plus`, `rtt-minus`, or a value between 1 and 4294967295.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<route-map-id>` | The route map name. |
| `<rule-id>` | The route map rule number.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set router policy route-map MAP1 rule 10 set metric rtt
```

{{%notice note%}}
In Cumulus Linux 5.5 and earlier, you can also set the metric value to `metric-plus` or `metric-minus`. Cumulus 5.6 and later does not provide the `metric-plus` and `metric-minus` options.
{{%/notice%}}

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set router policy route-map \<route-map-id\> rule \<rule-id\> set metric type</h>

Configures a set clause in the route map for the metric type for routes that match the map. The OSPF protocol uses the metric type. You can set OSPF external type 1 metric or OSPF external type 2 metric.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<route-map-id>` | The route map name. |
| `<rule-id>` | The route map rule number.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set router policy route-map MAP1 rule 10 set metric type type-2
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set router policy route-map \<route-map-id\> rule \<rule-id\> set origin</h>

Configures a set clause in the route map for the BGP origin code for the matched route. You can specify `egp` (the switch learns the origin of the route from an exterior routing protocol with the given autonomous system number) `igp` (the switch learns the origin of the route from an interior routing protocol), or `incomplete` (the origin of the route is unknown).

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<route-map-id>` | The route map name. |
| `<rule-id>` | The route map rule number.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set router policy route-map MAP1 rule 10 set origin igp
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set router policy route-map \<route-map-id\> rule \<rule-id\> set originator-id</h>

Configures the BGP IPv4 address of originator you want to set for the route in the route map.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<route-map-id>` | The route map name. |
| `<rule-id>` | The route map rule number.|

### Version History

Introduced in Cumulus Linux 5.2.0

### Example

```
cumulus@switch:~$ nv set router policy route-map MAP1 rule 10 set originator-id 10.10.10.4
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set router policy route-map \<route-map-id\> rule \<rule-id\> set source-ip</h>

Configures a set clause in the route map for the source IP address. You can specify an IPv4 or IPv6 address.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<route-map-id>` | The route map name. |
| `<rule-id>` | The route map rule number.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set router policy route-map MAP1 rule 10 set source-ip 10.1.10.0
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set router policy route-map \<route-map-id\> rule \<rule-id\> set tag</h>

Configures a set clause in the route map for the tag value for the routing protocol.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<route-map-id>` | The route map name. |
| `<rule-id>` | The route map rule number.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set router policy route-map MAP1 rule 10 set tag 100
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set router policy route-map \<route-map-id\> rule \<rule-id\> set weight</h>

Sets the BGP weight value for a matched route. You can specify a value between 0 and 4294967295.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<route-map-id>` | The route map name. |
| `<rule-id>` | The route map rule number.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set router policy route-map MAP1 rule 10 set weight 300
```
