---
title: Port Security
author: Cumulus Networks
weight: 292

type: nojsscroll
---
<style>
h { color: RGB(118,185,0)}
</style>
<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show interface \<interface-id\> port-security</h>

Shows port security configuration on the specified interface.

### Version History

Introduced in Cumulus Linux 5.7.0

### Example

```
cumulus@switch:~$ nv show interface swp1 port-security
                   operational  applied
-----------------  -----------  --------
enable             on           on
mac-limit          32           32
sticky-mac         disabled     disabled
sticky-timeout     1800         1800
sticky-ageing      disabled     disabled
violation-mode     restrict     restrict
violation-timeout  30           30

mac-addresses
================
    entry-id  MAC address        Type     Status
    --------  -----------------  -------  ---------
    1         00:01:02:03:04:05
    2         00:02:00:00:00:ab  Static
    3         00:02:00:00:00:05  Static
    4         00:02:00:00:01:05  Static
    5         00:02:00:00:01:06  Static
    6         00:02:01:00:01:06  Static
    7         01:02:01:00:01:06  Static
    8         00:02:00:00:00:11  Dynamic  Installed
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show interface \<interface-id\> port-security mac-addresses</h>

Shows port security MAC address information for the specified interface.

### Version History

Introduced in Cumulus Linux 5.7.0

### Example

```
cumulus@switch:~$ nv show interface swp1 port-security mac-addresses
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show interface \<interface-id\> port-security static-mac</h>

Shows port security static MAC address information for the specified interface.

### Version History

Introduced in Cumulus Linux 5.7.0

### Example

```
cumulus@switch:~$ nv show interface swp1 port-security static-mac
```
