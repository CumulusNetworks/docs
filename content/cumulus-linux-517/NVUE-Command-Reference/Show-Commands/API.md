---
title: API
author: Cumulus Networks
weight: 125

type: nojsscroll
---
<style>
h { color: RGB(118,185,0)}
</style>
<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system api</h>

Shows the NVUE REST API port configuration, state (enabled or disabled), and connection information.

### Version History

Introduced in Cumulus Linux 5.6.0

### Example

```
cumulus@switch:~$ nv show system api
                     operational  applied  
-------------------  -----------  ---------
port                 8888         8888     
state                enabled      enabled  
[listening-address]  localhost    localhost
connections                                
  accepted           1                     
  active             1                     
  handled            1                     
  reading            0                     
  requests           1                     
  waiting            0                     
  writing            1
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system api listening-address</h>

Shows the NVUE REST API listening address.

### Version History

Introduced in Cumulus Linux 5.6.0

### Example

```
cumulus@switch:~$ nv show system api listening-address

---------
localhost
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system api listening-address \<listening-address-id\></h>

Shows information about a specific NVUE REST API listening address.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<listening-address-id>` | The listening address. |

### Version History

Introduced in Cumulus Linux 5.6.0

### Example

```
cumulus@switch:~$ nv show system api listening-address localhost
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system api connections</h>

Shows NVUE REST API connection information.

### Version History

Introduced in Cumulus Linux 5.6.0

### Example

```
cumulus@switch:~$ nv show system api connections
          operational  applied
--------  -----------  -------
accepted  5                   
active    1                   
handled   5                   
reading   0                   
requests  5                   
waiting   0                   
writing   1
```
