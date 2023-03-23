---
title: MLAG
author: Cumulus Networks
weight: 210
product: Cumulus Linux
type: nojsscroll
---
## nv show interface \<interface-id\> bond mlag

Shows MLAG configuration on the bond interface.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<interface-id>`    | The interface name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show interface swp1 bond mlag
```

- - -

## nv show interface \<interface-id\> bond mlag consistency-checker

Shows MLAG consistency checker inconsistencies on the bond interface.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<interface-id>`    | The interface name. |

### Version History

Introduced in Cumulus Linux 5.1.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show interface swp1 bond mlag consistency-checker
```

- - -

## nv show mlag

Shows global MLAG configuration on the switch.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show mlag
```

- - -

## nv show mlag backup

Shows the backup IP address configured for the MLAG peer link. The switch uses this backup IP address if MLAG the peer link goes down.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show mlag backup
```

- - -

## nv show mlag backup \<backup-ip\>

Shows information about the MLAG backup IP address specified, such as the VRF.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<backup-ip>` | The backup IP address for the MLAG peer. |

### Version History

Introduced in Cumulus Linux 5.1.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show mlag backup 10.10.10.2
```

- - -

## nv show mlag consistency-checker

Shows any MLAG inconsistencies on the MLAG peers.

### Version History

Introduced in Cumulus Linux 5.1.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show mlag consistency-checker
```

- - -

## nv show mlag consistency-checker global

Shows global MLAG settings for each MLAG peer and indicates if there are any inconsistencies.

### Version History

Introduced in Cumulus Linux 5.1.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show mlag consistency-checker global
```

- - -

## nv show mlag fdb

Shows the MAC addresses, VLANs, and VLAN IDs in the forwarding database (FDB).

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show mlag fdb
```

- - -

## nv show mlag fdb local

Shows the locally learned MAC addresses in the FDB.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show mlag fdb local
```

- - -

## nv show mlag fdb peer

Shows the MAC addresses synchronized between MLAG peers in the FDB.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show mlag fdb peer
```

- - -

## nv show mlag fdb permanent

Shows the permanent MAC addresses installed in the FDB on the MLAG peer.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show mlag fdb permanent
```

- - -

## nv show mlag lacpdb

Shows the LACP database on the both MLAG peers.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show mlag lacpdb
```

- - -

## nv show mlag lacpdb local

Shows the LACP database on the local switch.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show mlag lacpdb local
```

- - -

## nv show mlag lacpdb peer

Shows the LACP database on the peer switch.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show mlag lacpdb peer
```

- - -

## nv show mlag mdb

Shows the multicast database on both MLAG peers.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show mlag mdb
```

- - -

## nv show mlag mdb local

Shows the multicast database on the local switch.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show mlag mdb local
```

- - -

## nv show mlag mdb peer

Shows the multicast database on the peer switch.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show mlag mdb peer
```

- - -

## nv show mlag multicast-router-port

Shows the MLAG multicast router ports on both MLAG peers.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show mlag multicast-router-port
```

- - -

## nv show mlag multicast-router-port local

Shows MLAG multicast router port information on the local switch.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show mlag multicast-router-port local
```

- - -

## nv show mlag multicast-router-port peer

Shows MLAG multicast router port information on the peer switch.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show mlag multicast-router-port peer
```

- - -

## nv show mlag neighbor

Shows information about permanent and dynamic MLAG neighbors.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show mlag neighbor
```

- - -

## nv show mlag neighbor dynamic

Shows information about MLAG dynamic neighbors.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show mlag neighbor dynamic
```

- - -

## nv show mlag neighbor permanent

Shows information about MLAG permanent neighbors.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show mlag neighbor permanent
```

- - -

## nv show mlag vni

Shows the MLAG VNIs on both MLAG peers.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show mlag vni
```

- - -

## nv show mlag vni local

Shows the MLAG VNIs configured on the local switch.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show mlag vni local
```

- - -

## nv show mlag vni peer

Shows the MLAG VNIs configured on the peer switch.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show mlag vni peer
```

- - -

## nv show nve vxlan mlag

Shows VXLAN source address information.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show nve vxlan mlag
```

- - -
