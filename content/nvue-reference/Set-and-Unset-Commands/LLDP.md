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

## <h>nv set interface \<interface-id\> lldp</h>

Provides commands to configure <span class="a-tooltip">[LLDP](## "Link Layer Discovery Protocol")</span> on an interface.

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set interface \<interface-id\> lldp application-tlv app \<application\> </h>

Configures the interface on which LLDP sends application priority TLVs in LLDP PDUs.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
|`<interface-id>` |  The interface you want to configure. |
|`<application>` |  The application name. |

### Version History

Introduced in Cumulus Linux 5.9.0

### Example

```
cumulus@switch:~$ nv set interface swp1 lldp application-tlv app iSCSI
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set interface \<interface-id\> lldp application-tlv tcp-port \<port\></h>

Configures the interface on which LLDP sends application priority TLVs in LLDP PDUs for TCP traffic using the specified port.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
|`<interface-id>` |  The interface you want to configure. |
|`<port>` |  The port number. |

### Version History

Introduced in Cumulus Linux 5.9.0

### Example

```
cumulus@switch:~$ nv set interface swp1 lldp application-tlv tcp-port 4217
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set interface \<interface-id\> lldp application-tlv udp-port \<port\></h>

Configures the interface on which LLDP sends application priority TLVs in LLDP PDUs for UDP traffic using the specified port.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
|`<interface-id>` |  The interface you want to configure. |
|`<port>` |  The port number. |

### Version History

Introduced in Cumulus Linux 5.9.0

### Example

```
cumulus@switch:~$ nv set interface swp1 lldp application-tlv udp-port 4317
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set interface \<interface-id\> lldp dcbx-ets-config-tlv</h>

Configures ETS TLV transmission on the interface. The default setting is `off`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
|`<interface-id>` |  The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.1.0

### Example

```
cumulus@switch:~$ nv set interface swp1 lldp dcbx-ets-config-tlv on
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

Configures PFC TLV transmission on the interface. The default setting is `off`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
|`<interface-id>` |  The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.1.0

### Example

```
cumulus@switch:~$ nv set interface swp1 lldp dcbx-pfc-tlv on
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set service lldp</h>

Provides commands to configure LLDP globally on the switch.

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set service lldp dot1-tlv</h>

Turns dot1 TLV advertisements on or off. The default setting is `off`.

### Version History

Introduced in Cumulus Linux 5.1.0

### Example

```
cumulus@switch:~$ nv set service lldp dot1-tlv on
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set service lldp application-tlv app \<application\> priority \<priority\></h>

Configures the specified application TLV priority.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
|`<application-id>` |  The application name. |
|`<priority>` |  The priority ID. |

### Version History

Introduced in Cumulus Linux 5.9.0

### Example

```
cumulus@switch:~$ nv set service lldp application-tlv app iSCSI priority 3
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set service lldp application-tlv tcp-port \<port\> priority \<priority\></h>

Configures the application priority for TCP traffic for the specified port.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
|`<port>` |  The port number. |
|`<priority>` |  The priority ID. |

### Version History

Introduced in Cumulus Linux 5.9.0

### Example

```
cumulus@switch:~$ nv set service lldp application-tlv tcp-port 4217 priority 6
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set service lldp application-tlv udp-port \<port\> priority \<priority\></h>

Configures the application priority for UDP traffic for the specified port.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
|`<port>` |  The port number. |
|`<priority>` |  The priority ID. |

### Version History

Introduced in Cumulus Linux 5.9.0

### Example

```
cumulus@switch:~$ nv set service lldp application-tlv udp-port 4317 priority 4
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set service lldp lldp-med-inventory-tlv></h>

Configures the `lldpd` service to send <span class="a-tooltip">[LLDP-MED](## "LLDP for Media Endpoint Devices")</span> Inventory TLV advertisements. By default, Cumulus Linux transmits LLDP-MED Inventory TLV advertisements on enabled ports.

LLDP-MED is an extension to LLDP that operates between endpoint devices, such as IP phones and switches. Inventory management TLV enables an endpoint to transmit detailed inventory information about itself to the switch, such as the hardware revision, firmware version, software version, serial number, manufacturer name, and model name.

You can disable LLDP-MED inventory TLV transmission if you want LLDP to receive LLDP-MED inventory TLVs (and publish them using SNMP, if enabled) but not send them.

### Version History

Introduced in Cumulus Linux 5.7.0

### Example

```
cumulus@switch:~$ nv set service lldp lldp-med-inventory-tlv off
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set service lldp mode \<mode\></h>

Configures the `lldpd` service to send only CDP frames or only LLDP frames. By default, the `lldpd` service sends LLDP frames unless it detects a CDP peer, then it sends CDP frames. You can set the following options:
- `force-send-cdpv1` configures the `lldpd` service to send only CDPv1 frames.
- `force-send-cdpv2` configures the `lldpd` service to send only CDPv2 frames.
- `force-send-lldp` configures the `lldpd` service to send only LLDP frames.

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@switch:~$ nv set service lldp mode force-send-cdpv1
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set service lldp tx-hold-multiplier</h>

Configures the amount of time to hold LLDP information before discarding it. The hold time interval is a multiple of the tx-interval.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set service lldp tx-hold-multiplier 3
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set service lldp tx-interval</h>

Configures the frequency of LLDP updates. You can specify a value between 10 and 300.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set service lldp tx-interval 100
```
