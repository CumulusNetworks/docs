---
title: Neighbor Discovery
author: Cumulus Networks
weight: 220
product: Cumulus Linux
type: nojsscroll
---
<style>
h { color: RGB(118,185,0)}
</style>
## <h>nv show interface \<interface-id\> ip neighbor-discovery</h>

Shows <span style="background-color:#F5F5DC">[ND](## "Neighbor Discovery")</span> settings for an interface.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<interface-id>` | The interface name.|

### Version History

Introduced in Cumulus Linux 5.1.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show interface swp1 ip neighbor-discovery
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show interface \<interface-id\> ip neighbor-discovery dnssl</h>

Shows the <span style="background-color:#F5F5DC">[DNSSL](## "DNS search list")</span>domain suffixes configured on the specified interface.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<interface-id>` | The interface name.|

### Version History

Introduced in Cumulus Linux 5.1.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show interface swp1 ip neighbor-discovery dnssl
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show interface \<interface-id\> ip neighbor-discovery dnssl \<domain-name-id\></h>

Shows configuration information for the specified <span style="background-color:#F5F5DC">[DNSSL](## "DNS search list")</span>domain suffix.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<interface-id>` | The interface name.|
| `<domain-name-id>`   |  The domain portion of a hostname (RFC 1123) or an internationalized hostname (RFC 5890).|

### Version History

Introduced in Cumulus Linux 5.1.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show interface swp1 ip neighbor-discovery dnssl accounting.nvidia.com
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show interface \<interface-id\> ip neighbor-discovery home-agent</h>

Shows Home Agent configuration for an interface, such as the maximum amount of time the router acts as a Home Agent and the router preference.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<interface-id>` | The interface name.|

### Version History

Introduced in Cumulus Linux 5.1.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show interface swp1 ip neighbor-discovery home-agent
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show interface \<interface-id\> ip neighbor-discovery prefix</h>

Shows the ND prefixes for the specified interface.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<interface-id>` | The interface name.|

### Version History

Introduced in Cumulus Linux 5.1.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show interface swp1 ip neighbor-discovery prefix
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show interface \<interface-id\> ip neighbor-discovery prefix \<ipv6-prefix-id\></h>

Shows ND prefix configuration for the specified interface, such as the amount of time the prefix is valid for on-link determination, the amount of time that addresses generated from a prefix remain preferred, and if the specified prefix is configured to use IPv6 autoconfiguration.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<interface-id>` | The interface name.|
| `<ipv6-address-id>`  | The IPv6 address of the RDNSS.|

### Version History

Introduced in Cumulus Linux 5.1.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show interface swp1 ip neighbor-discovery prefix 2001:db8:1::100/32
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show interface \<interface-id\> ip neighbor-discovery rdnss</h>

Shows the <span style="background-color:#F5F5DC">[RDNSS](## "recursive DNS servers")</span> configured on the specified interface.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<interface-id>` | The interface name.|

### Version History

Introduced in Cumulus Linux 5.1.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show interface swp1 ip neighbor-discovery rdnss
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show interface \<interface-id\> ip neighbor-discovery rdnss \<ipv6-address-id\></h>

Shows configuration for the specified <span style="background-color:#F5F5DC">[RDNSS](## "recursive DNS server")</span> configured on the specified interface.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<interface-id>` | The interface name.|
| `<ipv6-address-id>`  | The IPv6 address of the RDNSS.|

### Version History

Introduced in Cumulus Linux 5.1.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show interface swp1 ip neighbor-discovery rdnss 2001:db8:1::100
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show interface \<interface-id\> ip neighbor-discovery router-advertisement</h>

Shows router advertisement configuration for an interface, such as the hop limit value advertised in a Router Advertisement message, the maximum amount of time that Router Advertisement messages can exist on the route, the interval at which neighbor solicitation messages retransmit, and if fast transmit mode is on.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<interface-id>` | The interface name.|

### Version History

Introduced in Cumulus Linux 5.1.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show interface swp1 ip neighbor-discovery router-advertisement
```
