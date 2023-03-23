---
title: NTP
author: Cumulus Networks
weight: 610
product: Cumulus Linux
type: nojsscroll
---
{{%notice note%}}
The `nv unset` commands remove the configuration you set with the equivalent `nv set` commands. This guide only describes an `nv unset` command if it differs from the `nv set` command.
{{%/notice%}}

## nv set service ntp \<vrf-id\>

Configures the Network Time Protocol (NTP) in a specific VRF.

The default VRF is `default`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |  The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set service ntp default
```

- - -

## nv set service ntp \<vrf-id\> server \<server-id\>

Configures the remote NTP server.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |  The VRF you want to configure. |
| `<server-id>` | The hostname or IP address of the NTP server. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set service ntp default server time.nist.gov
```

- - -

## nv set service ntp \<vrf-id\> server \<server-id\> iburst

Configures NTP to send a burst of eight packets instead of the usual one packet when the server is unreachable. You can specify `on` or `off`.

The default setting is `off`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |  The VRF you want to configure. |
| `<server-id>` | The hostname or IP address of the NTP server. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set service ntp default server 192.168.0.254 iburst on
```

- - -

## nv set service ntp \<vrf-id\> pool \<server-id\>

Configures the remote NTP server pool.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<server-id>` |  The hostname or IP address of the NTP server. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set service ntp default pool 4.cumulusnetworks.pool.ntp.org
```

- - -

## nv set service ntp \<vrf-id\> pool \<server-id\> iburst

Configures NTP to send a burst of eight packets instead of the usual one packet when the server pool is unreachable. You can specify `on` or `off`.

The default setting is `off`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |  The VRF you want to configure. |
| `<server-id>` | The NTP server pool. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set service ntp default pool 4.cumulusnetworks.pool.ntp.org iburst on
```

- - -

## nv set service ntp \<vrf-id\> listen \<interface-name\>

Configures the NTP interface on which to listen.

The default setting is `eth0`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<interface-name>` |  The NTP interface on which to listen. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set service ntp default listen swp10
```
