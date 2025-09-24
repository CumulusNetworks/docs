---
title: Syslog
author: Cumulus Networks
weight: 380

type: nojsscroll
---
<style>
h { color: RGB(118,185,0)}
</style>
<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show service syslog</h>

Shows the syslog configuration settings.

{{%notice note%}}
Cumulus 5.13 and later does not provide this command. Use the `nv show system syslog` command instead.
{{%/notice%}}

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show service syslog
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show service syslog \<vrf-id\></h>

Shows the syslog configuration settings for the specified VRF.

{{%notice note%}}
Cumulus 5.13 and later does not provide this command. Use the `nv show system syslog <vrf-id>` command instead.
{{%/notice%}}

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` | The VRF name.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show service syslog default
          operational  applied      
--------  -----------  -------------
[server]               192.168.0.254
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show service syslog \<vrf-id\> server</h>

Shows the remote DNS servers for the specified VRF.

{{%notice note%}}
Cumulus 5.13 and later does not provide this command. Use the `nv show system syslog <vrf-id> server` command instead.
{{%/notice%}}

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |  The VRF name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show service syslog default server
               port  protocol
-------------  ----  --------
192.168.0.254  514   tcp
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show service syslog \<vrf-id\> server \<server-id\></h>

Shows information about a specific remote DNS server for the specified VRF.

{{%notice note%}}
Cumulus 5.13 and later does not provide this command. Use the `nv show system syslog <vrf-id> server <server-id>` command instead.
{{%/notice%}}

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |  The VRF name. |
| `<server-id>` | The hostname or IP address of the syslog server. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show service syslog default server 192.168.0.254
          operational  applied
--------  -----------  -------
port      514          514    
protocol  tcp          tcp
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system syslog</h>

Shows the syslog configuration settings.

{{%notice note%}}
Cumulus 5.12 and earlier does not provide this command. Use the `nv show service syslog <vrf-id>` command instead.
{{%/notice%}}

### Version History

Introduced in Cumulus Linux 5.13.0

### Example

```
cumulus@switch:~$ nv show system syslog
                   operational  applied
-----------------  -----------  -------
format             welf         welf   
  welf                                 
    firewall-name  nvidia       nvidia 

server
=========
    Servers               Vrf      Protocol  Port  Priority  Selector-Id      
    --------------------  -------  --------  ----  --------  -----------------
    192.168.0.254         default  tcp       601   1         SELECTOR1        
                                                   2         SELECTOR2        
    fe80::202:ff:fe00:29  default  udp       514   1         selector-ifreload

selector
===========
    Selectors          Severity  Program-Name  Facility  Burst  Interval  Filter  Match               Action 
    -----------------  --------  ------------  --------  -----  --------  ------  ------------------  -------
    SELECTOR1          notice                  cron                                                          
    SELECTOR2          debug     switchd       daemon                     2       Running             exclude
                                                                          10      issu_start=true.+$  include
                                                                          15      smonctl                    
    selector-ifreload  info      ifreload      daemon
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system syslog format</h>

Shows the syslog format: standard or WELF.

### Version History

Introduced in Cumulus Linux 5.13.0

### Example

```
cumulus@switch:~$ nv show system syslog format
                 operational  applied
---------------  -----------  -------
welf                                 
  firewall-name  nvidia       nvidia
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system syslog selector <selector-id\></h>

Shows configuration information for a selector.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<selector-id>` |  The name of the selector. |

### Version History

Introduced in Cumulus Linux 5.13.0

### Example

```
cumulus@switch:~$ nv show system syslog selector SELECTOR2
              operational  applied
------------  -----------  -------
facility      daemon       daemon 
program-name  switchd      switchd
severity      debug        debug  

filter
=========
    Priority  Action   Match             
    --------  -------  ------------------
    2         exclude  Running           
    10        include  issu_start=true.+$
    15                 smonctl
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system syslog selector \<selector-id\> filter</h>

Shows all filters for a selector.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<selector-id>` |  The name of the selector. |

### Version History

Introduced in Cumulus Linux 5.13.0

### Example

```
cumulus@switch:~$ nv show system syslog selector SELECTOR2 filter
Priority  Action   Match             
--------  -------  ------------------
2         exclude  Running           
10        include  issu_start=true.+$
15                 smonctl
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system syslog selector \<selector-id\> filter \<filter-id\></h>

Shows information about a specific filter for a selector.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<selector-id>` |  The name of the selector. |
| `<filter-id>` |  The filtering ID. |

### Version History

Introduced in Cumulus Linux 5.13.0

### Example

```
cumulus@switch:~$ nv show system syslog selector SELECTOR2 filter 10
        operational         applied           
------  ------------------  ------------------
match   issu_start=true.+$  issu_start=true.+$
action  include             include
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system syslog selector \<selector-id\> rate-limit</h>

Shows the rate limit configuration for a selector.
- The interval defines the time window within which the switch limits log messages after reaching the burst threshold.
- The burst limit specifies the maximum number of log messages that the switch can process instantly before rate limiting takes effect.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<selector-id>` |  The name of the selector. |

### Version History

Introduced in Cumulus Linux 5.13.0

### Example

```
cumulus@switch:~$ nv show system syslog selector SELECTOR1 rate-limit
          operational  applied
--------  -----------  -------
burst     2            2      
interval  240          240
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system syslog server</h>

Shows the configured syslog servers.

{{%notice note%}}
Cumulus 5.12 and earlier does not provide this command. Use the `nv show service syslog <vrf-id> server` command instead.
{{%/notice%}}

### Version History

Introduced in Cumulus Linux 5.13.0

### Example

```
cumulus@switch:~$ nv show system syslog server
Servers               Vrf      Protocol  Port  Priority  Selector-Id      
--------------------  -------  --------  ----  --------  -----------------
192.168.0.254         default  tcp       601   1         SELECTOR1        
                                               2         SELECTOR2        
fe80::202:ff:fe00:29  default  udp       514   1         selector-ifreload
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system syslog server \<server-id\></h>

Shows information for a specific syslog server.

{{%notice note%}}
Cumulus 5.12 and earlier does not provide this command. Use the `nv show service syslog <vrf-id> server <server-id>` command instead.
{{%/notice%}}

### Version History

Introduced in Cumulus Linux 5.13.0

### Example

```
cumulus@switch:~$ nv show system syslog server 192.168.0.254
          operational  applied
--------  -----------  -------
port      601          601
protocol  tcp          tcp
vrf       mgmt         mgmt

selector
===========
    Priority  Selector-Id
    --------  -----------
    1         SELECTOR1
    2         SELECTOR2
```
