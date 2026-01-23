---
title: Extended Traceroute
author: Cumulus Networks
weight: 563

type: nojsscroll
---
<style>
h { color: RGB(118,185,0)}
</style>
{{%notice note%}}
The `nv unset` commands remove the configuration you set with the equivalent `nv set` commands. This guide only describes an `nv unset` command if it differs from the `nv set` command.
{{%/notice%}}

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system global icmp ipv4 errors-extension ingress-interface</h>

Configures extended traceroute for IPv4.

Cumulus Linux supports RFC 5837, which extends ICMP error messages with interface information, enabling more meaningful traceroute results in unnumbered networks where router interfaces use link-local addresses.

In unnumbered networks, router interfaces are assigned IPv6 link-local addresses (such as fe80::1/64) while only the loopback interface has globally unique addresses. When parallel links exist between routers, traditional traceroute cannot identify which physical interface a packet traverses because ICMP error messages use the loopback address as the source. With extended traceroute, you can see the name, index, MTU, and IP address (if present) of the interface that received the packet, enabling accurate path tracing.

{{%notice note%}}
- You can enable or disable RFC 5837 globally.
- Cumulus Linux supports incoming interface information only.
- ICMP rate limiting applies (1000 messages per second by default).
- If you add multiple IP addresses to the ingress interface, the first address you add is considered the primary and the switch only reports that address in the ICMP extended error information. For example, if swp1 is the ingress interface and you add 10.0.0.1 to swp1, then add 10.0.1.1, the switch only reports 11.0.0.1.
- If the source of the traceroute is not a Cumulus Linux switch, it must have the Traceroute 2.1.5 package installed.
{{%/notice%}}

To send extended traceroute packets to a destination, run the `nv action traceroute system <destination> errors-extension` command.

### Version History

Introduced in Cumulus Linux 5.16.0

### Example

```
cumulus@switch:~$ nv set system global icmp ipv4 errors-extension ingress-interface
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system global icmp ipv6 errors-extension ingress-interface</h>

Configures extended traceroute for IPv6.

To send extended traceroute packets to a destination, run the `nv action traceroute system <destination> errors-extension` command.

### Version History

Introduced in Cumulus Linux 5.16.0

### Example

```
cumulus@switch:~$ nv set system global icmp ipv6 errors-extension ingress-interface
```
