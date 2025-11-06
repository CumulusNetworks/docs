---
title: LLDP
author: Cumulus Networks
weight: 590

type: nojsscroll
---
<style>
h { color: RGB(118,185,0)}
</style>
{{%notice note%}}
The `nv unset` commands remove the configuration you set with the equivalent `nv set` commands. This guide only describes an `nv unset` command if it differs from the `nv set` command.
{{%/notice%}}

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set interface \<interface-id\> lldp application-tlv app \<application-id\> </h>

Configures the interface on which <span class="a-tooltip">[LLDP](## "Link Layer Discovery Protocol")</span> sends application priority TLVs in LLDP PDUs.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
|`<interface-id>` |  The interface you want to configure. |
|`<application-id>` |  The application name. |

### Version History

Introduced in Cumulus Linux 5.9.0

### Example

```
cumulus@switch:~$ nv set interface swp1 lldp application-tlv app iSCSI
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set interface \<interface-id\> lldp application-tlv tcp-port \<port-id\></h>

Configures the interface on which LLDP sends application priority TLVs in LLDP PDUs for TCP traffic using the specified port.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
|`<interface-id>` |  The interface you want to configure. |
|`<port-id>` |  The port number. |

### Version History

Introduced in Cumulus Linux 5.9.0

### Example

```
cumulus@switch:~$ nv set interface swp1 lldp application-tlv tcp-port 4217
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set interface \<interface-id\> lldp application-tlv udp-port \<port-id\></h>

Configures the interface on which LLDP sends application priority TLVs in LLDP PDUs for UDP traffic.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
|`<interface-id>` |  The interface you want to configure. |
|`<port-id>` |  The port number. |

### Version History

Introduced in Cumulus Linux 5.9.0

### Example

```
cumulus@switch:~$ nv set interface swp1 lldp application-tlv udp-port 4317
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set interface \<interface-id\> lldp dcbx-ets-config-tlv</h>

Configures ETS TLV transmission on the interface. The default setting is `disabled`.

{{%notice note%}}
In Cumulus Linux 5.14 and earlier, you specify `on` or `off`.
{{%/notice%}}

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
|`<interface-id>` |  The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.1.0

### Example

```
cumulus@switch:~$ nv set interface swp1 lldp dcbx-ets-config-tlv enabled
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set interface \<interface-id\> lldp dcbx-ets-recomm-tlv</h>

Configures ETS Recommendation TLV transmission on the interface.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
|`<interface-id>` |  The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.1.0

### Example

```
cumulus@switch:~$ nv set interface swp1 lldp dcbx-ets-recomm-tlv on
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set interface \<interface-id\> lldp dcbx-pfc-tlv</h>

Configures PFC TLV transmission on the interface. The default setting is `disabled`.

{{%notice note%}}
In Cumulus Linux 5.14 and earlier, you specify `on` or `off`.
{{%/notice%}}

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
|`<interface-id>` |  The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.1.0

### Example

```
cumulus@switch:~$ nv set interface swp1 lldp dcbx-pfc-tlv disabled
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set interface \<interface-id\> lldp state</h>

Enables and disables LLDP on an interface.

When you disable LLDP on an interface, LLDP and CDP packet transmission stops on the interface.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
|`<interface-id>` |  The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.11.0

### Example

```
cumulus@switch:~$ nv set interface swp1 lldp state disabled
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system lldp application-tlv app \<application\> priority \<priority-id\></h>

Configures the specified application TLV priority.

{{%notice note%}}
In Cumulus Linux 5.14 and earlier, this command is `nv set service lldp application-tlv app <application> priority <priority-id>`.
{{%/notice%}}

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
|`<application-id>` |  The application name. |
|`<priority-id>` |  The priority ID. |

### Version History

Introduced in Cumulus Linux 5.9.0

### Example

```
cumulus@switch:~$ nv set system lldp application-tlv app iSCSI priority 3
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system lldp application-tlv tcp-port \<port-id\> priority \<priority-id\></h>

Configures the application priority for TCP traffic for the specified port.

{{%notice note%}}
In Cumulus Linux 5.14 and earlier, this command is `nv set service lldp application-tlv tcp-port <port-id> priority <priority-id>`.
{{%/notice%}}

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
|`<port-id>` |  The port number. |
|`<priority-id>` |  The priority ID. |

### Version History

Introduced in Cumulus Linux 5.9.0

### Example

```
cumulus@switch:~$ nv set system lldp application-tlv tcp-port 4217 priority 6
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system lldp application-tlv udp-port \<port-id\> priority \<priority-id\></h>

Configures the application priority for UDP traffic for the specified port.

{{%notice note%}}
In Cumulus Linux 5.14 and earlier, this command is `nv set service lldp application-tlv udp-port <port-id> priority <priority-id>`.
{{%/notice%}}

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
|`<portid>` |  The port number. |
|`<priority-id>` |  The priority ID. |

### Version History

Introduced in Cumulus Linux 5.9.0

### Example

```
cumulus@switch:~$ nv set system lldp application-tlv udp-port 4317 priority 4
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system lldp dot1-tlv</h>

Enables and disables dot1 TLV advertisements. The default setting is `disabled`.

{{%notice note%}}
In Cumulus Linux 5.14 and earlier, this command is `nv set service lldp dot1-tlv` and you specify `on` or `off` instead of `enabled` or `disabled`.
{{%/notice%}}

### Version History

Introduced in Cumulus Linux 5.1.0

### Example

```
cumulus@switch:~$ nv set system lldp dot1-tlv enabled
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system lldp lldp-med-inventory-tlv</h>

Configures the `lldpd` service to send <span class="a-tooltip">[LLDP-MED](## "LLDP for Media Endpoint Devices")</span> Inventory TLV advertisements. By default, Cumulus Linux transmits LLDP-MED Inventory TLV advertisements on enabled ports.

LLDP-MED is an extension to LLDP that operates between endpoint devices, such as IP phones and switches. Inventory management TLV enables an endpoint to transmit detailed inventory information about itself to the switch, such as the hardware revision, firmware version, software version, serial number, manufacturer name, and model name.

You can disable LLDP-MED inventory TLV transmission if you want LLDP to receive LLDP-MED inventory TLVs (and publish them using SNMP, if enabled) but not send them.

{{%notice note%}}
In Cumulus Linux 5.14 and earlier, this command is `nv set service lldp lldp-med-inventory-tlv`.
{{%/notice%}}

### Version History

Introduced in Cumulus Linux 5.7.0

### Example

```
cumulus@switch:~$ nv set system lldp lldp-med-inventory-tlv disabled
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system lldp mode \<mode\></h>

Configures the `lldpd` service to send only CDP frames or only LLDP frames. By default, the `lldpd` service sends LLDP frames unless it detects a CDP peer, then it sends CDP frames. You can set the following options:
- `force-send-cdpv1` configures the `lldpd` service to send only CDPv1 frames.
- `force-send-cdpv2` configures the `lldpd` service to send only CDPv2 frames.
- `force-send-lldp` configures the `lldpd` service to send only LLDP frames.

{{%notice note%}}
In Cumulus Linux 5.14 and earlier, this command is `nv set service lldp mode`.
{{%/notice%}}

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@switch:~$ nv set system lldp mode force-send-cdpv1
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system lldp state</h>

Enables and disables LLDP globally. Cumulus Linux enables the LLDP service by default. When you disable LLDP globally, the `lldp` service, and all LLDP and CDP packet transmission stops.

{{%notice note%}}
In Cumulus Linux 5.14 and earlier, this command is `nv set service lldp state`.
{{%/notice%}}

### Version History

Introduced in Cumulus Linux 5.11.0

### Example

```
cumulus@switch:~$ nv set system lldp state disabled
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system lldp tx-hold-multiplier</h>

Configures the amount of time to hold LLDP information before discarding it. The hold time interval is a multiple of the tx-interval.

{{%notice note%}}
In Cumulus Linux 5.14 and earlier, this command is `nv set service tx-hold-multiplier`.
{{%/notice%}}

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set service lldp tx-hold-multiplier 3
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system lldp tx-interval</h>

Configures the frequency of LLDP updates. You can specify a value between 10 and 300.

{{%notice note%}}
In Cumulus Linux 5.14 and earlier, this command is `nv set service lldp tx-interval`.
{{%/notice%}}

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set system lldp tx-interval 100
```
