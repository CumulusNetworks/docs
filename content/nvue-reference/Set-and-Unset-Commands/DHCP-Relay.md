---
title: DHCP Relay
author: Cumulus Networks
weight: 540

type: nojsscroll
---
<style>
h { color: RGB(118,185,0)}
</style>
{{%notice note%}}
The `nv unset` commands remove the configuration you set with the equivalent `nv set` commands. This guide only describes an `nv unset` command if it differs from the `nv set` command.
{{%/notice%}}

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set service dhcp-relay \<vrf-id\> agent state</h>

Enables DHCP Agent Information Option 82, which allows a DHCP relay to insert circuit or relay specific information into a request that the switch forwards to a DHCP server. You can specify `enabled` or `disabled`.

{{%notice note%}}
In Cumulus Linux 5.14 and earlier, you specify `enable on` or `enable off` instead of `state enabled` or `state disabled`.
{{%/notice%}}

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.7.0

### Example

```
cumulus@switch:~$ nv set service dhcp-relay default agent state enabled
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set service dhcp-relay \<vrf-id\> agent remote-id \<remote-id\></h>

Sets the remote ID DHCP Agent Information Option 82, which includes information that identifies the relay agent, such as the MAC address. By default, this is the system MAC address of the device on which DHCP relay is running.

{{%notice note%}}
Cumulus Linux 5.14 no longer provides this command.
{{%/notice%}}

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<remote-id>` | The remote ID, which includes information that identifies the relay agent, such as the MAC address.|

### Version History

Introduced in Cumulus Linux 5.7.0

### Example

```
cumulus@switch:~$ nv set service dhcp-relay default agent remote-id 44:38:39:BE:EF:AA
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set service dhcp-relay \<vrf-id\> agent use-pif-circuit-id state</h>

Enables Circuit ID DHCP Agent Information Option 82, which includes information about the circuit on which the request comes in, such as the SVI or physical port. By default, this is the printable name of the interface that receives the client request. You can specify `enabled` or `disabled`.

{{%notice note%}}
In Cumulus Linux 5.14 and earlier, you specify `enable on` or `enable off` instead of `state enabled` or `state disabled`.
{{%/notice%}}

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.7.0

### Example

```
cumulus@switch:~$ nv set service dhcp-relay default agent use-pif-circuit-id state enabled
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set service dhcp-relay \<vrf-id\> downstream-interface \<downstream-interface-id\> server-group-name</h>

Configures the server group associated with the DHCP relay host facing (downstream) interface.

{{%notice note%}}
In Cumulus Linux 5.13 and earlier, DHCP relay does not use server groups.
{{%/notice%}}

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<downstream-interface-id>` | The downstream interface name. |

### Version History

Introduced in Cumulus Linux 5.14.0

### Example

```
cumulus@switch:~$ nv set service dhcp-relay default downstream-interface vlan10 server-group-name type1-server-group
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set service dhcp-relay \<vrf-id\> gateway-interface \<interface-id\></h>

Configures the gateway IPv4 address on an interface.

{{%notice note%}}
In Cumulus Linux 5.4 and earlier, this command is `nv set service dhcp-relay <vrf-id> giaddress-interface <interface-id>`
{{%/notice%}}

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<interface-id>` | The gateway interface.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set service dhcp-relay default gateway-interface lo
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set service dhcp-relay \<vrf-id\> gateway-interface \<interface-id\> address</h>

Configures the IPv4 address on the gateway interface.

{{%notice note%}}
In Cumulus Linux 5.4 and earlier, this command is `nv set service dhcp-relay <vrf-id> giaddress-interface <interface-id> address <ipv4-address>`.
{{%/notice%}}

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<interface-id>` | The gateway IP address. |
| `<ipv4-address>` | The IPv4 address on the gateway interface. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set service dhcp-relay default gateway-address-interface address lo 10.10.10.1
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set service dhcp-relay \<vrf-id\> interface \<interface-id\></h>

Configures the interfaces on which to configure DHCP relay.

{{%notice note%}}
Cumulus Linux 5.14 no longer provides this command.
{{%/notice%}}

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<interface-id>` |  The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set service dhcp-relay default interface swp51
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set service dhcp-relay \<vrf-id\> server \<server-id\></h>

Configures the DHCP server.

{{%notice note%}}
Cumulus Linux 5.14 no longer provides the `nv show service dhcp-relay <vrf> server` command. You must configure server groups with the `nv set service dhcp-relay <vrf-id> server-group <server-group-id\>` command.
{{%/notice%}}

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<server-id>` |  The IPv4 address of the DHCP server. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set service dhcp-relay default server 172.16.1.102
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set service dhcp-relay \<vrf-id\> server-group \<server-group-id\> </h>

Configures the server group for DHCP relay.

Cumulus Linux uses server groups to receive different DHCP requests on separate interfaces from different end hosts and to relay the requests to specific DHCP servers in a VRF. Server groups provide load balancing and HA, ensuring more resilient DHCP service delivery in case of server failure or maintenance and prevents broadcasting requests to all servers.

- Server groups do not support IPv6.
- A server group must contain at least one server and one upstream interface.
- You must associate a downstream interface with the server group.

{{%notice note%}}
In Cumulus Linux 5.13 and earlier, DHCP relay does not use server groups, but instead, forwards all DHCP client requests to every DHCP server within the same VRF. Cumulus Linux 5.14 and later no longer provides the `nv show service dhcp-relay <vrf> server` commands.
{{%/notice%}}

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.14.0

### Example

```
cumulus@switch:~$ nv set service dhcp-relay default server-group type1-server-group
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set service dhcp-relay \<vrf-id\> server-group \<server-group-id\> server <server-id></h>

Configures the DHCP servers in the server group. A server group must contain at least one DHCP server for a specific VRF.

{{%notice note%}}
In Cumulus Linux 5.13 and earlier, DHCP relay does not use server groups, but instead, forwards all DHCP client requests to every DHCP server within the same VRF. Cumulus Linux 5.14 and later no longer provides the `nv show service dhcp-relay <vrf> server` commands.
{{%/notice%}}

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.14.0

### Example

```
cumulus@switch:~$ 
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set service dhcp-relay \<vrf-id\> server-group \<server-group-id\> upstream-interface <interface-id></h>

Configures the DHCP relay server facing (upstream) interface for the server group. You can specify multiple interfaces.

{{%notice note%}}
In Cumulus Linux 5.13 and earlier, DHCP relay does not use server groups, but instead, forwards all DHCP client requests to every DHCP server within the same VRF. Cumulus Linux 5.14 and later no longer provides the `nv show service dhcp-relay <vrf> server` commands.
{{%/notice%}}

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<server-group-id>` | The name of the server group. |

### Version History

Introduced in Cumulus Linux 5.14.0

### Example

```
cumulus@switch:~$ nv set service dhcp-relay default server-group type1-server-group upstream-interface swp51-52
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set service dhcp-relay \<vrf-id\> source-ip</h>

Configures the source IP address to use on the relayed packet. You can specify `gateway` to use the gateway IP address as the source IP address or `auto`, where the source IP address of the relayed packet is taken from a layer 3 interface on the switch using normal routing methods. The default setting is `auto`.

{{%notice note%}}
- This option impacts all relayed IPv4 packets globally.
- In Cumulus Linux 5.5 and earlier, you specify `giaddress` instead of `gateway`.
{{%/notice%}}

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set service dhcp-relay default source-ip gateway
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set service dhcp-relay6 \<vrf-id\> interface downstream \<interface-id\></h>

Configures the DHCP relay downstream interface.

{{%notice note%}}
In Cumulus Linux 5.14 and earlier, you must associate the downstream interface with a server group using the `nv set service dhcp-relay <vrf> downstream-interface <interface> server-group-name` command.
{{%/notice%}}

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
|`<interface-id>` |  The DHCP relay interface. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set service dhcp-relay6 default interface downstream swp1
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set service dhcp-relay6 \<vrf-id\> interface downstream \<interface-id\> link-address \<ipv6\></h>

Configures the IPv6 address on DHCP relay downstream interface.

{{%notice note%}}
In Cumulus Linux 5.4 and earlier, the command is `nv set service dhcp-relay6 <vrf-id> interface downstream <interface-id> address <ipv6>`.
{{%/notice%}}

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
|`<interface-id>` |  The DHCP relay downstream interface. |
|`<ipv6>` |  The IPv6 address. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set service dhcp-relay6 default interface downstream swp1 address 2001:db8::1
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set service dhcp-relay6 \<vrf-id\> interface upstream \<interface-id\></h>

Configures the upstream interface for DHCP relay for IPv6.

{{%notice note%}}
Cumulus Linux 5.14 no longer provides the `nv show service dhcp-relay <vrf-id> interface upstream <interface-id>` command. You must configure server groups with the `nv set service dhcp-relay <vrf-id> server-group <server-group-id> upstream-interface <interface-id>` command.
{{%/notice%}}

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
|`<interface-id>` |  The DHCP relay upstream interface. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set service dhcp-relay6 default interface upstream swp51
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set service dhcp-relay6 \<vrf-id\> interface upstream \<interface-id\> server-address \<ipv6\></h>

Configures the IPv6 address on the DHCP relay upstream interface.

{{%notice note%}}
- In Cumulus Linux 5.4 and earlier, the command is `nv set service dhcp-relay6 <vrf-id> interface upstream <interface-id> address <ipv6>`.
- Cumulus Linux 5.14 no longer provides this command.
{{%/notice%}}

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
|`<interface-id>` |  The DHCP relay interface. |
|`<ipv6>` |  The IPv6 address. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set service dhcp-relay6 default interface upstream swp51 server-address 2001:db8:0002::0a00:0002
```
