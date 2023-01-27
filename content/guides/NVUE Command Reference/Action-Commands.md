---
title: Action Commands
author: Cumulus Networks
weight: 55
product: Cumulus Linux
---
## nv action

Resets counters for interfaces, removes conflicts from protodown MLAG bonds, and disconnects system users.

- - -

## nv action clear interface \<interface\> bond mlag lacp-conflict

Clears the MLAG LACP conflict on the specified interface bond. A conflict can be an LACP partner MAC address mismatch or a duplicate LACP partner MAC address.

### Command Syntax

| <div style="width:250px">Syntax   |  Description  |
| ----------    | ------------  |
| `<interface>` | The interface that has an LACP conflict. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv action clear interface swp1 bond mlag lacp-conflict 
```

- - -

## nv action clear mlag lacp-conflict

Clears the MLAG LACP conflict. A conflict can be an LACP partner MAC address mismatch or a duplicate LACP partner MAC address.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv action clear mlag lacp-conflict 
```

- - -

## nv action clear qos buffer multicast-switch-priority

Clears the QoS multicast switch priority buffers.

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@leaf01:mgmt:~$ nv action clear qos buffer multicast-switch-priority 
```

- - -

## nv action clear qos buffer pool

Clears the QoS pool buffers.

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@leaf01:mgmt:~$ nv action clear qos buffer pool 
```

- - -

## nv action disconnect system aaa user \<user\>

Disconnects authenticated and authorized users.

### Command Syntax

| <div style="width:250px">Syntax   |  Description  |
| ----------    | ------------  |
| `<user>` | The user you want to disconnect. |

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@leaf01:mgmt:~$ nv action disconnect system aaa user admin2
```
