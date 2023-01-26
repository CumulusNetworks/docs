---
title: DNS Set and Unset Commands
author: Cumulus Networks
weight: 540
product: Cumulus Linux
type: nojsscroll
---
{{%notice note%}}
The `nv unset` commands remove the configuration you set with the equivlent `nv set` commands. This guide only describes an `nv unset` command if there is a difference between the `nv set` and `nv unset` command.
{{%/notice%}}

## nv set service dns \<vrf-id\>

Provides commands to configure the Domain Name Server (DNS) service.

- - -

## nv set service dns \<vrf-id\> server \<dns-server-id\>

Configures a remote DNS server.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>`         | The VRF you want to configure. |
| `<dns-server-id>`  | The IPv4 or IPv6 address of the remote DNS server.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set service dns default server 192.0.2.44
```
