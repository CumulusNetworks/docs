---
title: Router Nexthop Commands
author: Cumulus Networks
weight: 275
product: Cumulus Linux
type: nojsscroll
---
## nv show router nexthop

Shows information about the next hops in the RIB, such as the IP address, VRF, interface, type, and so on.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show router nexthop
```

- - -

## nv show router nexthop group

Shows information about nexthop groups in the RIB. Nexthop groups are a way to encapsulate ECMP information together.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show router nexthop groups
```

- - -

## nv show router nexthop group \<nexthop-group-id\>

Shows information about the specified nexthop group in the RIB.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<nexthop-group-id>` | The nexthop group ID. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show router nexthop 1
```

- - -

## nv show router nexthop group \<nexthop-group-id\> via

Shows information about the IP addresses for the specified nexthop group.

### Command Syntax

 Syntax |  Description   |
| --------- | -------------- |
| `<nexthop-group-id>` | The nexthop group ID. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show router nexthop 1 via
```

- - -

## nv show router nexthop group \<nexthop-group-id\> via \<via-id\>

Shows information about the specified IP address for a specific nexthop group.

### Command Syntax

 Syntax |  Description   |
| --------- | -------------- |
| `<nexthop-group-id>` | The nexthop group ID. |
| `<via-id>` | The IP address. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show router nexthop 1 via fe80::a00:27ff:fea6:b9fe
```

- - -

## nv show router nexthop rib

Shows information about the next hops in RIB, such as the IP address, VRF, interface, type, and so on.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show router nexthop rib
```

- - -

## nv show router nexthop rib \<nhg-id\>

Shows information about the specified nexthop group in the RIB.

### Command Syntax

 Syntax |  Description   |
| --------- | -------------- |
| `<nhg-id>` | The nexthop group ID. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show router nexthop rib 10
```

- - -

## nv show router nexthop rib \<nhg-id\> resolved-via

Shows the IP addresses for the specified nexthop in the RIB.

### Command Syntax

 Syntax |  Description   |
| --------- | -------------- |
| `<nhg-id>` | The nexthop group ID. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show router nexthop rib 10 resolved-via
```

- - -

## nv show router nexthop rib \<nhg-id\> resolved-via \<resolved-via-id\>

Shows information about the specified IP address for a specific nexthop group in the RIB.

### Command Syntax

 Syntax |  Description   |
| --------- | -------------- |
| `<nhg-id>` | The nexthop group ID. |
| `<resolved-via-id>` | The IP address. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show router nexthop
```

- - -

## nv show router nexthop rib \<nhg-id\> resolved-via-backup

Shows information about the nexthop group RIB backup nexthops.

### Command Syntax

 Syntax |  Description   |
| --------- | -------------- |
| `<nhg-id>` | The nexthop group ID. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show router nexthop 10 resolved-via-backup
```

- - -

## nv show router nexthop rib \<nhg-id\> resolved-via-backup \<resolved-via-id\>

Shows information about a specific nexthop group RIB backup nexthop.

### Command Syntax

 Syntax |  Description   |
| --------- | -------------- |
| `<nhg-id>` | The nexthop group ID. |
| `<resolved-via-id>` | The IP address. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show router nexthop rib 20 resolved-via-backup 
```

- - -

## nv show router nexthop rib \<nhg-id\> depends

Shows information about for nexthop group RIB depends

### Command Syntax

 Syntax |  Description   |
| --------- | -------------- |
| `<nhg-id>` | The nexthop group ID. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show router nexthop rib 10 depends
```

- - -

## nv show router nexthop rib \<nhg-id\> dependents

Shows information about for nexthop group RIB dependents.

### Command Syntax

 Syntax |  Description   |
| --------- | -------------- |
| `<nhg-id>` | The nexthop group ID. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show router nexthop rib 10 dependents
```

 - - -
