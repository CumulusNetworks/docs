---
title: LLDP Set and Unset Commands
author: Cumulus Networks
weight: 610
product: Cumulus Linux
type: nojsscroll
---
{{%notice note%}}
The `nv unset` commands remove the configuration you set with the equivalent `nv set` commands. This guide only describes an `nv unset` command if there is a difference between the `nv set` and `nv unset` command.
{{%/notice%}}

nv set service lldp
nv set service lldp tx-interval 10-300
nv set service lldp tx-hold-multiplier 1-10
nv set service lldp dot1-tlv (on|off)
nv set acl <acl-id> rule <rule-id> match mac source-mac (ANY|bpdu|cdp|cisco-pvst|lacp|lldp|<mac>)
nv set acl <acl-id> rule <rule-id> match mac dest-mac (ANY|bpdu|cdp|cisco-pvst|lacp|lldp|<mac>)

## nv set interface \<interface-id\> lldp

Provides commands to configure Link Layer Discovery Protocol (LLDP) for an interface.

- - -

## nv set interface \<interface-id\> lldp dcbx-pfc-tlv

Configures PFC TLV transmission on the interface.

The default setting is `off`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
|`<interface-id>` |  The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set interface swp1 lldp dcbx-pfc-tlv on
```

- - -

## nv set interface \<interface-id\> lldp dcbx-ets-config-tlv

Configures ETS TLV transmission on the interface.

The default setting is `off`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
|`<interface-id>` |  The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set interface swp1 lldp dcbx-ets-config-tlv on
```

- - -

## nv set interface \<interface-id\> lldp dcbx-ets-recomm-tlv

Configures ETS Recommendation TLV transmission on the interface.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
|`<interface-id>` |  The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set interface swp1 lldp dcbx-ets-recomm-tlv on
```

- - -

## nv set service lldp

Provides commands to configure Link Layer Discovery Protocol LLDP globally on the switch.

- - -

## nv set service lldp tx-interval

Configures the frequency of LLDP updates. You can specify a value between 10 and 300.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set service lldp tx-interval 100
```

- - -

## nv set service lldp tx-hold-multiplier

Configures the amount of time to hold LLDP information before discarding it. The hold time interval is a multiple of the tx-interval.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set service lldp tx-hold-multiplier 3
```

- - -

## nv set service lldp dot1-tlv

Turns dot1 TLV advertisements on or off.

The default setting is `off`.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set service lldp dot1-tlv on
```
