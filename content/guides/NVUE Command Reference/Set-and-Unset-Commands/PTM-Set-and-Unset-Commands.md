---
title: PTM Set and Unset Commands
author: Cumulus Networks
weight: 660
product: Cumulus Linux
type: nojsscroll
---
{{%notice note%}}
The `nv unset` commands remove the configuration you set with the equivalent `nv set` commands. This guide only describes an `nv unset` command if it differs from the `nv set` command.
{{%/notice%}}

## nv set router ptm

Provides commands to configure Prescriptive Topology Manager (PTM).

- - -

## nv set router ptm enable

Turns PTM on or off. When on, PTM perfoms additional checks to ensure that routing adjacencies form only on links that have connectivity and that conform to the specification that `ptmd` defines.

The default setting is `off`.

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set router ptm enable on
```
