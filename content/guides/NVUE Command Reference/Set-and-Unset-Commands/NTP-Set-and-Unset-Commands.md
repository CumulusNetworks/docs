---
title: NTP Set and Unset Commands
author: Cumulus Networks
weight: 670
product: Cumulus Linux
type: nojsscroll
---
## nv set service ntp \<vrf-id\>

Configures the Network Time Protocol (NTP).

### Default Setting

N/A

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

### Default Setting

N/A

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

### Default Setting

`off`

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

### Default Setting

N/A

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<server-id>` |  The hostname or IP address of the NTP server. |

### Version History

Introduced in Cumulus Linux 5.0.0

```
cumulus@leaf01:mgmt:~$ nv set service ntp default pool 4.cumulusnetworks.pool.ntp.org
```

- - -

## nv set service ntp \<vrf-id\> pool \<server-id\> iburst

Configures NTP to send a burst of eight packets instead of the usual one packet when the server pool is unreachable. You can specify `on` or `off`.

### Default Setting

`off`

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

### Default Setting

`eth0`

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
