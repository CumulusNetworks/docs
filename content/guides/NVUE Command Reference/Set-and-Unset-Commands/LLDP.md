---
title: LLDP
author: Cumulus Networks
weight: 580
product: Cumulus Linux
type: nojsscroll
---
{{%notice note%}}
The `nv unset` commands remove the configuration you set with the equivalent `nv set` commands. This guide only describes an `nv unset` command if it differs from the `nv set` command.
{{%/notice%}}

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

Introduced in Cumulus Linux 5.1.0

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

Introduced in Cumulus Linux 5.1.0

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

Introduced in Cumulus Linux 5.1.0

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

Introduced in Cumulus Linux 5.1.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set service lldp dot1-tlv on
```

- - -

## nv set service lldp mode \<mode\>

Configures the `lldpd` service to send only CDP frames or only LLDP frames. By default, the `lldpd` service sends LLDP frames unless it detects a CDP peer, then it sends CDP frames. You can set the following options:
- `force-send-cdpv1` configures the `lldpd` service to send only CDPv1 frames.
- `force-send-cdpv2` configures the `lldpd` service to send only CDPv2 frames.
- `force-send-lldp` configures the `lldpd` service to send only LLDP frames.

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set service lldp mode force-send-cdpv1
```

- - -
