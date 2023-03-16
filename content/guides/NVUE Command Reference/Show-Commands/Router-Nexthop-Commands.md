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

Shows the next hop groups in the RIB. Nexthop groups are a way to encapsulate ECMP information together.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show router nexthop groups
```

- - -

## nv show router nexthop group \<nexthop-group-id\>

Shows information about the specified next hop group in the RIB.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<nexthop-group-id>` | The next hop group ID. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show router nexthop 1
```

- - -

## nv show router nexthop group \<nexthop-group-id\> via

Shows information about the next hop addresses for the specified next hop group.

### Command Syntax

 Syntax |  Description   |
| --------- | -------------- |
| `<nexthop-group-id>` | The next hop group ID. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show router nexthop 1 via
```

- - -

## nv show router nexthop group \<nexthop-group-id\> via \<via-id\>

Shows details of a particular next hop group specified by the next hop address.

### Command Syntax

 Syntax |  Description   |
| --------- | -------------- |
| `<nexthop-group-id>` | The next hop group ID. |
| `<via-id>` | The IP address. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show router nexthop 10 via fe80::a00:27ff:fea6:b9fe
```

- - -

## nv show router nexthop rib

Shows information about the next hops in RIB, such as the IP address, VRF, interface, type, and so on.

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show router nexthop rib
```

- - -

## nv show router nexthop rib \<nhg-id\>

Shows information about the specified next hop in the RIB.

### Command Syntax

 Syntax |  Description   |
| --------- | -------------- |
| `<nhg-id>` | The next hop group ID. |

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show router next hop rib 10
```

- - -

## nv show router nexthop rib \<nhg-id\> resolved-via

Shows details the next-hop address for a particular next hop.

### Command Syntax

 Syntax |  Description   |
| --------- | -------------- |
| `<nhg-id>` | The next hop group ID. |

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show router next hop rib 10 resolved-via
```

- - -

## nv show router nexthop rib \<nhg-id\> resolved-via \<resolved-via-id\>

Shows details of a particular next hop specified by the next hop IP address.

### Command Syntax

 Syntax |  Description   |
| --------- | -------------- |
| `<nhg-id>` | The next hop group ID. |
| `<resolved-via-id>` | The next hop IP address. |

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show router nexthop rib 10 resolved-via fe80::a00:27ff:fea6:b9fe
```

- - -

## nv show router nexthop rib \<nhg-id\> resolved-via-backup

Shows information about the backup next hops for the specified next hop.

### Command Syntax

 Syntax |  Description   |
| --------- | -------------- |
| `<nhg-id>` | The next hop group ID. |

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show router next hop 10 resolved-via-backup
```

- - -

## nv show router nexthop rib \<nhg-id\> resolved-via-backup \<resolved-via-id\>

Shows information about a specific backup next hop.

### Command Syntax

 Syntax |  Description   |
| --------- | -------------- |
| `<nhg-id>` | The next hop group ID. |
| `<resolved-via-id>` | The IP address. |

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show router nexthop rib 20 resolved-via-backup 
```

- - -

## nv show router nexthop rib \<nhg-id\> depends

Shows information about the next hops on which a specific next hop relies on.

### Command Syntax

 Syntax |  Description   |
| --------- | -------------- |
| `<nhg-id>` | The next hop group ID. |

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show router nexthop rib 10 depends
```

- - -

## nv show router nexthop rib \<nhg-id\> dependents

Shows information about the next hop dependents on which a specific next hop relies on.

### Command Syntax

 Syntax |  Description   |
| --------- | -------------- |
| `<nhg-id>` | The next hop group ID. |

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show router nexthop rib 10 dependents
```

 - - -
