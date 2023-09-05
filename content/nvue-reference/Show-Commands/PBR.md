---
title: PBR
author: Cumulus Networks
weight: 250

type: nojsscroll
---
<style>
h { color: RGB(118,185,0)}
</style>
<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show interface \<interface-id\> router pbr</h>

Shows PBR configuration settings for the specified interface.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<interface-id>` | The interface name.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show interface swp51 router pbr
       operational  applied
-----  -----------  -------
[map]  MAP1         MAP1
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show interface \<interface-id\> router pbr map</h>

Shows the PBR route maps configured for the specified interface.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<interface-id>`    | The interface name. |

### Version History

Introduced in Cumulus Linux 5.1.0

### Example

```
cumulus@switch:~$ nv show interface swp51 router pbr map
      valid
----  -----
MAP1  on
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show interface \<interface-id\> router pbr map \<pbr-map-id\></h>

Shows configuration settings for a specific PBR route map on the specified interface.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<interface-id>`    | The interface name. |
| `<pbr-map-id>`   |  The route map name.|

### Version History

Introduced in Cumulus Linux 5.1.0

### Example

```
cumulus@switch:~$ nv show interface swp51 router pbr map map1
       operational  applied
-----  -----------  -------
valid  on
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show router pbr</h>

Shows global PBR configuration settings.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show router pbr
       operational  applied
------  -----------  -------
enable               on     
[map]   map1         map1
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show router pbr map</h>

Shows settings for PBR route maps. If you do not provide a specific route map name, this command shows configuration settings for all configured PBR route maps.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show router pbr map
        operational  applied
------  -----------  -------
enable               on     
[map]   map1         map1
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show router pbr map \<pbr-map-id\></h>

Shows the configuration settings for a PBR route map used for policy configuration.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<pbr-map-id>` | The name of the route map. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show router pbr map map1
        operational  applied
------  -----------  -------
[rule]  1            1      
[rule]  10           10
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show router pbr map \<pbr-map-id\> rule</h>

Shows the rules for the specified PBR route map.

{{%notice note%}}
Add `-o json` at the end of the command to see the output in a more readable format.
{{%/notice%}}

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
|`<pbr-map-id>` | The name of the route map. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show router pbr map map1 rule -o json
{
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
      "source-ip": "0.0.0.0/0"
    }
  }
}
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show router pbr map \<pbr-map-id\> rule \<rule-id\></h>

Shows the match and set criteria, and the rule action for a PBR route map.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
|`<pbr-map-id>` | The name of the route map. |
|`<rule-id>`  |  The PBR rule number. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show router pbr map map1 rule 1
                   operational       applied  
-----------------  ----------------  ---------
action                                        
  [nexthop-group]  group1            group1   
match                                         
  source-ip        0.0.0.0/0         0.0.0.0/0
installed          off                        
installed-reason   Invalid NH-group           
ip-rule-id         300
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show router pbr map \<pbr-map-id\> rule \<rule-id\> action</h>

Shows the rule action for a PBR route map.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<pbr-map-id>` | The route map name. |
| `<rule-id>` | The PBR rule number. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show router pbr map map1 rule 1 action
                operational  applied
---------------  -----------  -------
[nexthop-group]  group1       group1
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show router pbr map \<pbr-map-id\> rule \<rule-id\> action nexthop-group</h>

Shows the next hop groups in the PBR route map rule action.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<pbr-map-id>` |  The route map name. |
| `<rule-id>` | The PBR rule number. |

### Version History

Introduced in Cumulus Linux 5.1.0

### Example

```
cumulus@switch:~$ nv show router pbr map map1 rule 1 action nexthop-group
       installed  table-id
------  ---------  --------
group1  off        5000
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show router pbr map \<pbr-map-id\> rule \<rule-id\> action nexthop-group \<nexthop-group-id\></h>

Shows configuration settings for the specified next hop group including the IP route table number of the default route.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<pbr-map-id>` |  The route map name. |
| `<rule-id>` | The PBR rule number. |
| `<nexthop-group-id>` | The next hop group name. |

### Version History

Introduced in Cumulus Linux 5.1.0

### Example

```
cumulus@switch:~$ nv show router pbr map map1 rule 1 action nexthop-group group1
           operational  applied
---------  -----------  -------
installed  off                 
table-id   5000
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show router pbr map \<pbr-map-id\> rule \<rule-id\> match</h>

Shows the rule match criteria for a PBR route map.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<pbr-map-id>` | The route map name. |
| `<rule-id>` | The PBR rule number. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show router pbr map map1 rule 1 match
           operational  applied  
---------  -----------  ---------
source-ip  0.0.0.0/0    0.0.0.0/0
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show router pbr nexthop-group </h>

Shows the PBR next hop groups configured on the switch.

### Version History

Introduced in Cumulus Linux 5.6.0

### Example

```
cumulus@switch:~$ nv show router pbr nexthop-group
Nexthop-groups  installed  valid    Summary         
--------------  ---------  -----    ----------------
group1          yes         yes     Nexthop-index: 1
                                    Nexthop-index: 2
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show router pbr nexthop-group \<nexthop-group-id\></h>

Shows information about a specific PBR next hop group.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<nexthop-group-id>` | The next hop group ID. |

### Version History

Introduced in Cumulus Linux 5.6.0

### Example

```
cumulus@switch:~$ nv show router pbr nexthop-group group1
           operational  applied
---------  -----------  -------
installed  no                  
valid      no                  

nexthop
==========
    Nexthop-index  label  nexthop       target-vrf  valid  vrf   weight
    -------------  -----  ------------  ----------  -----  ----  ------
    1                     192.168.0.22              no                 
    2                     192.168.0.21              no     swp1 
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system global reserved routing-table pbr</h>

Shows the PBR reserved routing table ranges.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show system global reserved routing-table pbr
       operational  applied   
-----  -----------  ----------
begin  10000        10000     
end    4294966272   4294966272
```
