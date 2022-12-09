---
title: MLAG Commands
author: Cumulus Networks
weight: 170
product: Cumulus Linux
type: nojsscroll
---
## nv show interface \<interface-id\> bond mlag

Shows MLAG configuration on the bond interface.

### Usage

`nv show interface <interface-id> bond mlag [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<interface-id>`    | The interface name. |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `lacp-conflict`         | Configure the mlag lacp-conflict parameters |
| `consistency-checker`   | Consistency-checker parameters for mlag interfaces |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ nv show interface swp1 bond mlag
```

- - -

## nv show interface \<interface-id\> bond mlag consistency-checker

Shows inconsistencies on the interface that the MLAG consistency checker finds.

### Usage

`nv show interface <interface-id> bond mlag consistency-checker [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<interface-id>`    | The interface name. |

### Version History

Introduced in Cumulus Linux 5.1.0

### Example

```
cumulus@leaf04:mgmt:~$ nv show interface swp1 bond mlag consistency-checker
```

- - -

## nv show mlag

Shows global MLAG configuration on the switch.

### Usage

`nv show mlag [options] [<attribute> ...]`

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `lacp-conflict`         | Shows LACP conflicts. |
| `consistency-checker`   | Shows MLAG settings for each peer and indicates if there are any inconsistencies.|
| `backup`                | Shows the backup IP address configured for the peer link. |
| `fdb`                   | Shows the MAC addresses, VLANs, and VLAN IDs in the forwarding database (FDB). |
| `mdb`                   | Shows the multicast database on the peer switch. |
| `multicast-router-port`  | Shows the multicast router ports. |
| `vni`                   | Shows the local VNIs. |
| `lacpdb`                | Shows the MLAG local LACP information. |
| `neighbor`              | Shows the local and peer neighbour entries.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ nv show mlag
```

- - -

## nv show mlag consistency-checker

Shows any MLAG inconsistencies on the MLAG peers.

### Usage

`nv show mlag consistency-checker [options] [<attribute> ...]`

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `global`    | Shows global MLAG settings for each MLAG peer and indicates if there are any inconsistencies. |

### Version History

Introduced in Cumulus Linux 5.1.0

### Example

```
cumulus@leaf04:mgmt:~$ nv show mlag consistency-checker
```

- - -

## nv show mlag consistency-checker global

Shows global MLAG settings for each MLAG peer and indicates if there are any inconsistencies.

### Usage

`nv show mlag consistency-checker global [options]`

### Version History

Introduced in Cumulus Linux 5.1.0

### Example

```
cumulus@leaf04:mgmt:~$ nv show mlag consistency-checker global
```

- - -

## nv show mlag backup

Shows the backup IP address configured for the peer link. The switch uses this backup IP address if the peer link goes down.

### Usage

`nv show mlag backup [options] [<backup-ip> ...]`

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ nv show mlag backup
```

- - -

## nv show mlag backup \<backup-ip\>

Shows information about the backup IP address specified.

### Usage

`nv show mlag backup <backup-ip> [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<backup-ip>` | The backup IP address for the MLAG peer. |

### Version History

Introduced in Cumulus Linux 5.1.0

### Example

```
cumulus@leaf04:mgmt:~$ nv show mlag backup 10.10.10.2
```

- - -

## nv show mlag fdb

Shows the MAC addresses, VLANs, and VLAN IDs in the forwarding database (FDB).

### Usage

`nv show mlag fdb [options] [<attribute> ...]`

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `local`      | Shows the locally learned MAC addresses. |
| `peer`       | Shows the MAC addresses synchronized between MLAG peers. |
| `permanent`  | Shows the permanent MAC addresses installed on the MLAG peer. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ nv show mlag fdb
```

- - -

## nv show mlag fdb local

Shows the locally learned MAC addresses in the FDB.

### Usage

`nv show mlag fdb local [options]`

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ nv show mlag fdb local
```

- - -

## nv show mlag fdb peer

Shows the MAC addresses synchronized between MLAG peers in the FDB.

### Usage

`nv show mlag fdb peer [options]`

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ nv show mlag fdb peer
```

- - -

## nv show mlag fdb permanent

Shows the permanent MAC addresses installed in the FDB on the MLAG peer.

### Usage

`nv show mlag fdb permanent [options]`

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ nv show mlag fdb permanent
```

- - -

## nv show mlag mdb

Shows the multicast database on both MLAG peers.

### Usage

`nv show mlag mdb [options] [<attribute> ...]`

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `local`    | Shows the local multicast database on the local switch. |
| `peer `    | Shows the multicast database on the peer switch. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ nv show mlag mdb
```

- - -

## nv show mlag mdb local

Multicast Groups Info

### Usage

`nv show mlag mdb local [options]`

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ nv show mlag mdb local
```

- - -

## nv show mlag mdb peer

Shows the multicast database on the peer switch.

### Usage

`nv show mlag mdb peer [options]`

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ nv show mlag mdb peer
```

- - -

## nv show mlag multicast-router-port

Shows the MLAG multicast router ports on both MLAG peers.

### Usage

`nv show mlag multicast-router-port [options] [<attribute> ...]`

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `local`   | Shows the MLAG multicast router ports on the local switch. |
| `peer`    | Shows the MLAG multicast router ports on the peer switch. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ nv show mlag multicast-router-port
```

- - -

## nv show mlag multicast-router-port local

Shows the MLAG multicast router ports on the local switch.

### Usage

`nv show mlag multicast-router-port local [options]`

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ nv show mlag multicast-router-port local
```

- - -

## nv show mlag multicast-router-port peer

Shows the MLAG multicast router ports on the peer switch.

### Usage

`nv show mlag multicast-router-port peer [options]`

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ nv show mlag multicast-router-port peer
```

- - -

## nv show mlag vni

Shows the MLAG VNIs on both MLAG peers.

### Usage

`nv show mlag vni [options] [<attribute> ...]`

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `local`  | Shows the MLAG VNIs configured on the local switch. |
| `peer`   | Shows the MLAG VNIs configured on the peer switch.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ nv show mlag vni
```

- - -

## nv show mlag vni local

Shows the MLAG VNIs configured on the local switch.

### Usage

`nv show mlag vni local [options]`

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ nv show mlag vni local
```

- - -

## nv show mlag vni peer

Shows the MLAG VNIs configured on the peer switch.

### Usage

`nv show mlag vni peer [options]`

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ nv show mlag vni peer
```

- - -

## nv show mlag lacpdb

Shows the LACP database on the both MLAG peers.

### Usage

`nv show mlag lacpdb [options] [<attribute> ...]`

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `local` | Shows the LACP database on the local switch.|
| `peer`  | Shows the LACP database on the peer switch. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ nv show mlag lacpdb
```

- - -

## nv show mlag lacpdb local

Shows the LACP database on the local switch.

### Usage

`nv show mlag lacpdb local [options]`

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ nv show mlag lacpdb local
```

- - -

## nv show mlag lacpdb peer

Shows the LACP database on the peer switch.

### Usage

`nv show mlag lacpdb peer [options]`

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ nv show mlag lacpdb peer
```

- - -

## nv show mlag neighbor

Shows information about MLAG neighbors.

### Usage

`nv show mlag neighbor [options] [<attribute> ...]`

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `dynamic`     | Shows information about MLAG dynamic neighbors. |
| `permanent`   | Shows information about MLAG permanent neighbors. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ nv show mlag neighbor
```

- - -

## nv show mlag neighbor dynamic

Shows information about MLAG dynamic neighbors.

### Usage

`nv show mlag neighbor dynamic [options]`

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ nv show mlag neighbor dynamic
```

- - -

## nv show mlag neighbor permanent

Shows information about MLAG permanent neighbors.

### Usage

`nv show mlag neighbor permanent [options]`

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ nv show mlag neighbor permanent
```
