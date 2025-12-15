---
title: Syslog
author: Cumulus Networks
weight: 750

type: nojsscroll
---
<style>
h { color: RGB(118,185,0)}
</style>
{{%notice note%}}
The `nv unset` commands remove the configuration you set with the equivalent `nv set` commands. This guide only describes an `nv unset` command if it differs from the `nv set` command.
{{%/notice%}}

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set service syslog \<vrf-id\> server \<server-id\></h>

Configures the remote `syslog` server.

{{%notice note%}}
Cumulus 5.13 and later does not provide this command. Use the `nv set system syslog server <server-id>` command instead.
{{%/notice%}}

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<server-id>` |  The hostname or IP address of the `syslog` server. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set service syslog default server 192.168.0.254
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set service syslog \<vrf-id\> server \<server-id\> port</h>

Configures the port number of the remote `syslog` server.

{{%notice note%}}
Cumulus 5.13 and later does not provide this command. Use the `nv set system syslog server <server-id> port` command instead.
{{%/notice%}}

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<server-id>` |  The hostname or IP address of the `syslog` server. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set service syslog default server 192.168.0.254 port 601
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set service syslog \<vrf-id\> server \<server-id\> protocol</h>

Configures the protocol you want to use to transmit syslog data. You can specify either UDP or TCP.

{{%notice note%}}
Cumulus 5.13 and later does not provide this command. Use the `nv set system syslog server <server-id> protocol` command instead.
{{%/notice%}}

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<server-id>` |  The hostname or IP address of the `syslog` server. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set service syslog default server 192.168.0.254 protocol tcp
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system syslog format</h>

Sets the log format.
You can set the log format to:
- Standard (the default syslog format with a standard template).
- WELF (WebTrends Enhanced Log Format) and provide an optional firewall name.

### Version History

Introduced in Cumulus Linux 5.13.0

### Example

```
cumulus@switch:~$ nv set system syslog format welf firewall-name security-gateway
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system syslog selector \<selector-id\> facility</h>

Sets a syslog filtering rule to group logs based on their source, such as `auth` or `cron`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<selector-id>` |   The name of the filter selector. |

### Version History

Introduced in Cumulus Linux 5.13.0

### Example

```
cumulus@switch:~$ nv set system syslog selector SELECTOR1 facility cron
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system syslog selector \<selector-id\> filter \<filter-id\> action</h>

Sets a syslog filtering rule action to filter logs that match a certain regular expression. You can specify `include` or `exclude`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<selector-id>` |   The name of the filter selector. |
| `<filter-id>` |   The filter ID. |

### Version History

Introduced in Cumulus Linux 5.13.0

### Example

```
cumulus@switch:~$ nv set system syslog selector SELECTOR2 filter 10 action exclude
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system syslog selector \<selector-id\> filter \<filter-id\> match</h>

Sets a syslog filtering rule to filter logs that match a certain regular expression.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<selector-id>` |   The name of the filter selector. |
| `<filter-id>` |   The filter ID. |

### Version History

Introduced in Cumulus Linux 5.13.0

### Example

```
cumulus@switch:~$ nv set system syslog selector SELECTOR2 filter 10 match .*Flush Journal.+$
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system syslog selector \<selector-id\> program-name</h>

Sets a syslog filtering rule to filter logs based on the application that generates them.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<selector-id>` |   The name of the filter selector. |

### Version History

Introduced in Cumulus Linux 5.13.0

### Example

```
cumulus@switch:~$ nv set system syslog selector SELECTOR2 program-name switchd
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system syslog selector \<selector-id\> rate-limit burst</h>

Sets the burst limit to control log message processing or forwarding within a defined time period. The burst limit specifies the maximum number of log messages that the switch can process instantly before rate limiting takes effect. You can specify a value between 1 and 65535.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<selector-id>` | The name of the filter selector. |

### Version History

Introduced in Cumulus Linux 5.13.0

### Example

```
cumulus@switch:~$ nv set system syslog selector SELECTOR1 rate-limit burst 2
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system syslog selector \<selector-id\> rate-limit interval</h>

Sets a rate-limiting rule with an interval to control log message processing or forwarding within a defined time period. The interval defines the time window within which the switch limits log messages after reaching the burst threshold. You can specify a value between 1 and 65535.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<selector-id>` | The name of the filter selector. |

### Version History

Introduced in Cumulus Linux 5.13.0

### Example

```
cumulus@switch:~$ nv set system syslog selector SELECTOR1 rate-limit interval 240
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system syslog selector \<selector-id\> severity</h>

Sets a syslog filtering rule to filter logs based on the severity level.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<selector-id>` |   The name of the filter selector. |

### Version History

Introduced in Cumulus Linux 5.13.0

### Example

```
cumulus@switch:~$ nv set system syslog selector SELECTOR2 severity debug
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system syslog server \<server-id\></h>

Configures the port of the remote `syslog` server.

{{%notice note%}}
Cumulus 5.12 and earlier does not provide this command. Use the `nv set service syslog <vrf-id> server <server-id>` command instead.
{{%/notice%}}

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<server-id>` |  The hostname or IP address of the `syslog` server. |

### Version History

Introduced in Cumulus Linux 5.13.0

### Example

```
cumulus@switch:~$ nv set system syslog server 192.168.0.254
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system syslog server \<server-id\> port</h>

Configures the port of the remote `syslog` server.

{{%notice note%}}
Cumulus 5.12 and earlier does not provide this command. Use the `nv set service syslog <vrf-id> server <server-id> port` command instead.
{{%/notice%}}

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<server-id>` |  The hostname or IP address of the `syslog` server. |

### Version History

Introduced in Cumulus Linux 5.13.0

### Example

```
cumulus@switch:~$ nv set system syslog server 192.168.0.254 port 601
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system syslog server \<server-id\> protocol</h>

Configures the protocol you want to use to transmit syslog data. You can specify either UDP or TCP.

{{%notice note%}}
Cumulus 5.12 and earlier does not provide this command. Use the `nv set service syslog <vrf-id> server <server-id> protocol` command instead.
{{%/notice%}}

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<server-id>` |  The hostname or IP address of the `syslog` server. |

### Version History

Introduced in Cumulus Linux 5.13.0

### Example

```
cumulus@switch:~$ nv set system syslog server 192.168.0.254 protocol tcp
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## nv set system syslog server \<server-id\> selector \<priority-id\> selector-id \<value\></h>

Sets a selector to use for a specific server.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<server-id>` |  The hostname or IP address of the `syslog` server. |
| `<priority-id>` |  The priority, where 1 is the highest priority. |
| `<selector-id>` |  The name of the filter selector. |

### Version History

Introduced in Cumulus Linux 5.13.0

### Example

```
cumulus@switch:~$ nv set system syslog server 192.168.0.254 selector 1 selector-id SELECTOR1
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system syslog server \<server-id\> vrf \<vrf-id\></h>

Sets the VRF in which the `syslog` server runs. By default, the `syslog` server runs in the default VRF.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<server-id>` |  The hostname or IP address of the `syslog` server. |
| `<vrf-id>` |   The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.13.0

### Example

```
cumulus@switch:~$ nv set system syslog server 192.168.0.254 vrf mgmt 
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system syslog selector ifreload program-name</h>

Configures the switch to filter logs based on the application or program generating them.

### Version History

Introduced in Cumulus Linux 5.15.0

### Example

```
cumulus@switch:~$ nv set system syslog selector ifreload program-name ifreload
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system syslog selector ifreload filter \<filter-id\>

Configures filters for syslog messages. You can specify `action` or `match` to filter on specific text.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<filter-id>` |  The filter name. |

### Version History

Introduced in Cumulus Linux 5.15.0

### Example

```
cumulus@switch:~$ nv set system syslog selector ifreload filter 1 match 'ip link set'
cumulus@switch:~$ nv set system syslog selector ifreload filter 1 action include
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system syslog severity</h>

Sets the global severity level of logs to `debug`, `info`, `notice`, `warn`, `error`, `critical`, or `none`. The default setting is `none`.

### Version History

Introduced in Cumulus Linux 5.13.0

### Example

```
cumulus@switch:~$ nv set system syslog severity notice
```
