---
title: MLAG Commands
author: Cumulus Networks
weight: 150
product: Cumulus Linux
type: nojsscroll
---
## nv show interface \<interface-id\> bond mlag

MLAG configuration on the bond interface

### Usage

`nv show interface <interface-id> bond mlag [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<interface-id>`    |    Interface |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `lacp-conflict`         | Configure the mlag lacp-conflict parameters |
| `consistency-checker`   | Consistency-checker parameters for mlag interfaces |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show interface \<interface-id\> bond mlag consistency-checker

Interface MLAG Consistency-checker

### Usage

`nv show interface <interface-id> bond mlag consistency-checker [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<interface-id>`    |    Interface |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show mlag

Global Multi-chassis Link Aggregation properties

### Usage

`nv show mlag [options] [<attribute> ...]`

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `lacp-conflict`         | Configure the mlag lacp-conflict parameters |
| `consistency-checker`   | Consistency-checker parameters for mlag nodes |
| `backup`                | Set of MLAG backups |
| `fdb`                   | Macs owned by local/peer mlag switch |
| `mdb`                   | Mdb owned by local/peer switch |
| `multicast-router-port`  | Multicast Router Ports owned by local/peer mlag switch |
| `vni`                   | Local VNIs |
| `lacpdb`                | Mlag Local Lacp Info |
| `neighbor`              | Local/peer Neighbour Entries|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show mlag lacp-conflict

Configure the mlag lacp-conflict parameters

### Usage

`nv show mlag lacp-conflict [options]`

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show mlag consistency-checker

Show the mlag consistency-checker parameters

### Usage

`nv show mlag consistency-checker [options] [<attribute> ...]`

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `global`    | mlag global consistency-checker |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show mlag consistency-checker global

Global Consistency-checker

### Usage

`nv show mlag consistency-checker global [options]`

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show mlag backup

Set of MLAG backups

### Usage

`nv show mlag backup [options] [<backup-ip> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<backup-ip>` | Backup IP of MLAG peer |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show mlag backup \<backup-ip\>

alternative ip address or interface for peer to reach us

### Usage

`nv show mlag backup <backup-ip> [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| <backup-ip> |  Backup IP of MLAG peer |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show mlag fdb

Set of all mlag macs

### Usage

`nv show mlag fdb [options] [<attribute> ...]`

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `local`      | Locally learnt macs |
| `peer`       | Peer Synced Macs |
| `permanent`  | Permanent Macs installed on local/peer |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show mlag fdb local

Set of MLAG Macs learnt/sync between mlag peers

### Usage

`nv show mlag fdb local [options]`

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show mlag fdb peer

Set of MLAG Macs learnt/sync between mlag peers

### Usage

`nv show mlag fdb peer [options]`

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show mlag fdb permanent

Permanent Mac Entry

### Usage

`nv show mlag fdb permanent [options]`

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show mlag mdb

Set of Mlag Multicast Database Entries

### Usage

`nv show mlag mdb [options] [<attribute> ...]`

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `local`    | Local Multicast Database |
| `peer `    | Peer Multicast Database |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show mlag mdb local

Multicast Groups Info

### Usage

`nv show mlag mdb local [options]`

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show mlag mdb peer

Multicast Groups Info

### Usage

`nv show mlag mdb peer [options]`

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show mlag multicast-router-port

Set of all Mlag Multicast Router Ports

### Usage

`nv show mlag multicast-router-port [options] [<attribute> ...]`

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `local`   | Local Multicast Router Ports |
| `peer`    | Peer Multicast Router Ports |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show mlag multicast-router-port local

Multicast Router Ports

### Usage

`nv show mlag multicast-router-port local [options]`

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show mlag multicast-router-port peer

### Usage

`nv show mlag multicast-router-port peer [options]`

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show mlag vni

Set of all vnis

### Usage

`nv show mlag vni [options] [<attribute> ...]`

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `local`  | Local Vnis |
| `peer`   | Peer Vnis |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show mlag vni local

Set of VNIs configured

### Usage

`nv show mlag vni local [options]`

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show mlag vni peer

Set of VNIs configured

### Usage

`nv show mlag vni peer [options]`

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show mlag lacpdb

Set of all mlag local/peer lacpdb

### Usage

`nv show mlag lacpdb [options] [<attribute> ...]`

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `local` | Local Lacp Database |
| `peer`  | Peer Lacp Database |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show mlag lacpdb local

Lacp DB

### Usage

`nv show mlag lacpdb local [options]`

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show mlag lacpdb peer

Lacp DB

### Usage

`nv show mlag lacpdb peer [options]`

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show mlag neighbor

Set of all mlag neigh entries

### Usage

`nv show mlag neighbor [options] [<attribute> ...]`

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `dynamic`     | Dynamic Neighbor |
| `permanent`   | Permanent Neighbor |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show mlag neighbor dynamic

Neighs

### Usage

`nv show mlag neighbor dynamic [options]`

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show mlag neighbor permanent

Permanent Neighbors 
### Usage

`nv show mlag neighbor permanent [options]`

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```
