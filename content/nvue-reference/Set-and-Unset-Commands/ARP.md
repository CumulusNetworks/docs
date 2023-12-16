---
title: ARP
author: Cumulus Networks
weight: 517

type: nojsscroll
---
<style>
h { color: RGB(118,185,0)}
</style>
{{%notice note%}}
The `nv unset` commands remove the configuration you set with the equivalent `nv set` commands. This guide only describes an `nv unset` command if it differs from the `nv set` command.
{{%/notice%}}

## <h>nv set system global arp base-reachable-time</h>

Configures how long a neighbor cache entry is valid. The entry is considered valid for at least the value between the base reachable time divided by two and three times the base reachable time divided by two. You can specify a value between 30 and 2147483 seconds. The default value is auto; NVUE derives the value for auto from the `/etc/sysctl.d/neigh.conf` file.

### Version History

Introduced in Cumulus Linux 5.6.0

### Example

```
cumulus@switch:~$ nv set system global arp base-reachable-time 50
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set interface \<interface-id\> neighbor ipv4 \<address\> lladdr \<lladdr-id\></h>

Configures a static ARP table entry for an interface with an IPv4 address associated with a MAC address for easy management or as a security measure to prevent spoofing and other nefarious activities.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<interface-id>` |  The interface you want to configure. |
| `<address>` |  The static IP address. |
| `<lladdr-id>` |  The MAC address you want to associate with IPv4 address. |

### Version History

Introduced in Cumulus Linux 5.7.0

### Example

```
cumulus@switch:~$ nv set interface swp51 neighbor ipv4 10.5.5.51 lladdr 00:00:5E:00:53:51
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set interface \<interface-id\> neighbor ipv4 \<address\> lladdr \<lladdr-id\> flag</h>

Configures a flag to indicate that the neighbor in the ARP table entry is a router (`is-router`) or learned externally (`ext_learn`)

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<interface-id>` |  The interface you want to configure. |
| `<address>` |   The static IP address. |
| `<lladdr-id>` |  The MAC address you want to associate with IPv4 address. |

### Version History

Introduced in Cumulus Linux 5.7.0

### Example

```
cumulus@switch:~$ nv set interface swp51 neighbor ipv4 10.5.5.51 lladdr 00:00:5E:00:53:51 flag is-router
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set interface \<interface-id\> neighbor ipv4 \<address\> lladdr \<lladdr-id\> state</h>

Configures the sate of the neighbor in the ARP table entry (`delay`, `failed`, `incomplete`, `noarp`, `permanent`, `probe`, `reachable`, or `stale`).

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<interface-id>` |  The interface you want to configure. |
| `<address>` |  The static IP address. |
| `<lladdr-id>` |  The MAC address you want to associate with IPv4 address. |

### Version History

Introduced in Cumulus Linux 5.7.0

### Example

```
cumulus@switch:~$ nv set interface swp51 neighbor ipv4 10.5.5.51 lladdr 00:00:5E:00:53:51 state permanent
```
