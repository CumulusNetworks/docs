---
title: System
author: Cumulus Networks
weight: 410
product: Cumulus Linux
type: nojsscroll
---
## nv show system

Shows information about the switch, such as the hostname, Cumulus Linux verison, the switch uptime, and the timezone.

### Version History

Introduced in Cumulus Linux 5.2.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show system
```

- - -

## nv show system counter polling-interval

Shows the polling interval for the switch counters for both the logical and physical interfaces.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show system counter polling-interval
```

- - -

## nv show system cpu

Shows information about the switch CPU, such as the core-count, the model, and the utilization percentage.

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show system cpu
```

- - -

## nv show system forwarding profile-option

Shows forwarding profile information.

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show system forwarding profile-option
```

- - -

## nv show system global

Shows global system configuration, such as the anycast ID, anycast MAC address, fabric ID, fabric MAC address, system MAC address, routing table, VLAN, and VNI information.

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show system global
```

- - -

## nv show system global reserved

Shows global reserved configuration information, such as the VLAN internal range.

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show system global reserved
```

- - -

## nv show system global reserved routing-table

Shows global reserved routing table information.

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show system global reserved routing-table
```

- - -

## nv show system global reserved vlan

Shows the reserved VLAN configuration settings.

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show system global reserved vlan
```

- - -

## nv show system global reserved vlan internal

Shows the reserved internal VLAN configuration settings.

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show system global reserved vlan internal
```

- - -

## nv show system global reserved vlan l3-vni-vlan

Shows the reserved VLAN layer 3 VNI to VLAN mapping settings.

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show system global reserved vlan l3-vni-vlan
```

- - -

## nv show system memory

Shows information about the switch memory, such as the total amount of memory, the amount of free and used memory,and the percent of memory utilized.

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show system memory
```

- - -

## nv show system message

Shows pre- and post-login messages.

### Version History

Introduced in Cumulus Linux 5.2.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show system message
```

- - -

## nv show system reboot

Shows system reboot information.

### Version History

Introduced in Cumulus Linux 5.2.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show system reboot
```

- - -

## nv show system reboot history

Shows the system reboot history.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show system reboot history
```

- - -

## nv show system reboot reason

Shows the reason why the switch was rebooted.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show system reboot reason
```

- - -
