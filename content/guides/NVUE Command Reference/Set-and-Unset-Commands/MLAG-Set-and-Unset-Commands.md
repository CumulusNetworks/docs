---
title: MLAG Set and Unset Commands
author: Cumulus Networks
weight: 600
product: Cumulus Linux
type: nojsscroll
---
- - -

## nv set mlag

Configures global Multi-chassis Link Aggregation (MLAG) properties.

### Usage

`nv [options] set mlag [backup ...]`

`nv [options] set mlag [debug ...]`

`nv [options] set mlag [enable ...]`

`nv [options] set mlag [init-delay ...]`

`nv [options] set mlag [mac-address ...]`

`nv [options] set mlag [peer-ip ...]`

`nv [options] set mlag [priority ...]`

### Version History

Introduced in Cumulus Linux 5.0.0

- - -

## nv set mlag backup \<backup-ip\>

Configures the IP address of the MLAG backup switch. The backup IP address is any layer 3 backup interface for the peer link, which the switch uses when the peer link goes down. You must add the backup IP address, which must be different than the peer link IP address.

### Usage

`nv [options] set mlag backup <backup-ip>`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<backup-ip>` |  The IP address of the MLAG backup switch. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set mlag backup 10.10.10.2
```

- - -

## nv set mlag backup \<backup-ip\> vrf \<vrf-name\>

Configures the VRF for MLAG backup IP address.

### Usage

`nv [options] set mlag backup <backup-ip> vrf <arg>`

### Default Setting

N/A

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<backup-ip>` |  The IP address of the MLAG backup switch.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set mlag backup 10.10.10.2 vrf RED
```

- - -

## nv set mlag enable

Turns MLAG on or off.

### Usage

`nv [options] set mlag enable [<arg> ...]`

### Default Setting

`off`

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set mlag enable on
```

- - -

## nv set mlag mac-address

Configures the MLAG system MAC address. NVIDIA provides a reserved range of MAC addresses for MLAG (between 44:38:39:ff:00:00 and 44:38:39:ff:ff:ff). Use a MAC address from this range to prevent conflicts with other interfaces in the same bridged network. Do not to use a multicast MAC address. Make sure you specify a different MAC address for each MLAG pair in the network.

### Usage

`nv [options] set mlag mac-address <arg>`

### Default Setting

N/A

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set mlag mac-address 44:38:39:BE:EF:AA
```

- - -

## nv set mlag peer-ip

Configures the IP address of the MLAG peer. You can specify an IPv4 address, an IPv6 address or `linklocal`.

### Usage

`nv [options] set mlag peer-ip <arg>`

### Default Setting

N/A

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set mlag peer-ip linklocal
```

- - -

## nv set mlag priority

Configures the MLAG priority. By default, the switch determines the role by comparing the MAC addresses of the two sides of the peering link; the switch with the lower MAC address assumes the primary role. You can override this by setting the priority option for the peer link. You can set a vlaue between 0-65535.

### Usage

`nv [options] set mlag priority <arg>`

### Default Setting

32768

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set mlag priority 2084
```

- - -

## nv set mlag init-delay

Configures the number of seconds `clagd` delays bringing up MLAG bonds and anycast IP addresses. You can set a value between 0 and 9000.

This timer sets to 0 automatically under the following conditions:
- When the peer is not alive and the backup link is not active after a reload timeout.
- When the peer sends a goodbye (through the peer link or the backup link).
- When both MLAG sessions come up at the same time.

### Usage

`nv [options] set mlag init-delay <arg>`

### Default Setting

180

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set mlag init-delay 100
```

- - -

## nv set mlag debug

Turns MLAG degugging on or off.

### Usage

`nv [options] set mlag debug <arg>`

### Default Setting

`off`

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set mlag debug on
```

- - -
