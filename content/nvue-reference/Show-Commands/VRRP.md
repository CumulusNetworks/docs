---
title: VRRP
author: Cumulus Networkss
weight: 445

type: nojsscroll
---
<style>
h { color: RGB(118,185,0)}
</style>
<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show interface \<interface-id\> ipv4 vrrp</h>

Shows VRRP configuration for the specified interface. For IPv6, run the `nv show interface <interface-id> ipv6 vrrp` command.

{{%notice note%}}
In Cumulus Linux 5.14 and earlier, the command is `nv show interface <interface-id> ip vrrp`.
{{%/notice%}}

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<interface-id>`    |   The interface name.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show interface swp1 ipv4 vrrp
                  operational  applied
----------------  -----------  -------
enable                         on     
[virtual-router]  44           44
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show interface \<interface-id\> ipv4 vrrp virtual-router</h>

Shows the virtual gateways implemented with VRRP for the specified interface. For IPv6, run the `nv show interface <interface-id> ipv6 vrrp virtual-router` command.

{{%notice note%}}
In Cumulus Linux 5.14 and earlier, the command is `nv show interface <interface-id> ip vrrp virtual-router`.
{{%/notice%}}


{{%notice note%}}
Add `-o json` at the end of the command to see the output in a more readable format.
{{%/notice%}}

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<interface-id>`    | The interface name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show interface swp1 ipv4 vrrp virtual-router -o json
{
  "44": {
    "accept-mode": "off",
    "address-family": {
      "ipv4": {
        "counters": {
          "adv-rx": 0,
          "adv-tx": 0,
          "garp-tx": 0,
          "state-transitions": 0
        },
        "down-interval": 0,
        "master-adv-interval": 0,
        "priority": 254,
        "skew-time": 0,
        "status": "Initialize",
        "virtual-addresses": {
          "10.0.0.1": {}
        },
        "vmac": "00:00:5e:00:01:2c"
      },
      "ipv6": {
        "counters": {
          "adv-rx": 0,
          "adv-tx": 0,
          "neigh-adv-tx": 0,
          "state-transitions": 0
        },
        "down-interval": 0,
        "master-adv-interval": 0,
        "primary-addr": "::",
        "priority": 254,
        "skew-time": 0,
        "status": "Initialize",
        "virtual-addresses": {
          "2001:db8::1": {}
        },
        "vmac": "00:00:5e:00:02:2c"
      }
    }, 
    "advertisement-interval": 1000, 
    "auto-config": "off", 
    "interface": "vlan101", 
    "is-shutdown": "off", 
    "preempt": "on", 
    "priority": 110, 
    "version": 3 
  } 
}
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show interface \<interface-id\> ipv4 vrrp virtual-router \<virtual-router-id\></h>

Shows information about a specific virtual gateway implemented with VRRP for the specified interface. For IPv6, run the `nv show interface <interface-id> ipv6 vrrp virtual-router <virtual-router-id>` command.

{{%notice note%}}
In Cumulus Linux 5.14 and earlier, the command is `nv show interface <interface-id> ip vrrp virtual-router <virtual-router-id>`.
{{%/notice%}}

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<interface-id>`    | The interface name. |
| `<virtual-router-id>` |  The <span class="a-tooltip">[VRID](## "Virtual Router Identifier")</span> that identifies the group of VRRP routers.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show interface swp1 ipv4 vrrp virtual-router 44
                        operational  applied     
----------------------  -----------  ------------
version                 3            3 
priority                110          110 
preempt                 on           auto 
advertisement-interval  1000         1000 
[address]                            50.0.0.1 
[address]                            2001:50::1 
auto-config             off 
is-shutdown             off 
accept-mode             on 
interface               vlan101 
[address-family]        ipv4 
[address-family]        ipv6
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show interface \<interface-id\> ipv4 vrrp virtual-router \<virtual-router-id\> address</h>

Shows the IP addresses of the virtual gateway implemented with VRRP for the specified interface. For IPv6, run the `nv show interface <interface-id> ipv6 vrrp virtual-router <virtual-router-id> address` command.

{{%notice note%}}
In Cumulus Linux 5.14 and earlier, the command is `nv show interface <interface-id> ip vrrp virtual-router <virtual-router-id> address`.
{{%/notice%}}

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<interface-id>`    | The interface name. |
| `<virtual-router-id>` |  The <span class="a-tooltip">[VRID](## "Virtual Router Identifier")</span> that identifies the group of VRRP routers.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show interface swp1 ipv4 vrrp virtual-router 44 address
IP address 
---------- 
10.0.0.1 
2001:50::1 
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show interface \<interface-id\> ipv4 vrrp virtual-router \<virtual-router-id\> address\<ip-address-id\></h>

Shows information about the IP address of the virtual gateway implemented with VRRP for the specified interface. For IPv6, run the `nv show interface <interface-id> ipv6 vrrp virtual-router <virtual-router-id> address <address-id>` command.

{{%notice note%}}
In Cumulus Linux 5.14 and earlier, the command is `nv show interface <interface-id> ip vrrp virtual-router <virtual-router-id> address <address-ip>`.
{{%/notice%}}

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<interface-id>` | The interface name. |
| `<virtual-router-id>` | The <span class="a-tooltip">[VRID](## "Virtual Router Identifier")</span> that identifies the group of VRRP routers.|
| `<ip-address-id>` | The IPv4 or IPv6 address. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show interface swp1 ipv4 vrrp virtual-router 44 address 10.0.0.1
No Data
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show interface \<interface-id\> ipv4 vrrp virtual-router \<virtual-router-id\> address-family</h>

Shows the IP addresses for all address families for the virtual gateway implemented with VRRP for the specified interface.

Add `-o json` at the end of the command to see the output in a more readable format.

{{%notice note%}}
Cumulus Linux 5.15 no longer supports this command.
{{%/notice%}}

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<interface-id>`    | The interface name. |
| `<virtual-router-id>` |  The <span class="a-tooltip">[VRID](## "Virtual Router Identifier")</span> that identifies the group of VRRP routers.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show interface swp1 ip vrrp virtual-router 44 address-family -o json
{
  "ipv4": {
    "counters": {
      "adv-rx": 0,
      "adv-tx": 0,
      "garp-tx": 0,
      "state-transitions": 0
    },
    "down-interval": 0,
    "master-adv-interval": 0,
    "priority": 254,
    "skew-time": 0,
    "status": "Initialize",
    "virtual-addresses": {
      "10.0.0.1": {}
    },
    "vmac": "00:00:5e:00:01:2c"
  },
  "ipv6": {
    "counters": {
      "adv-rx": 0,
      "adv-tx": 0,
      "neigh-adv-tx": 0,
      "state-transitions": 0
    },
    "down-interval": 0,
    "master-adv-interval": 0,
    "primary-addr": "::",
    "priority": 254,
    "skew-time": 0,
    "status": "Initialize",
    "virtual-addresses": {
      "2001:db8::1": {}
    },
    "vmac": "00:00:5e:00:02:2c"
    "vrrp-interface": "vrrp6-10-1"
  }
}
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show interface \<interface-id\> ip vrrp virtual-router \<virtual-router-id\> address-family \<afi\></h>

Shows the IP addresses for a specific address family (IPv4 or IPv6) for the virtual gateway implemented with VRRP for the specified interface.

{{%notice note%}}
Cumulus Linux 5.15 no longer supports this command.
{{%/notice%}}

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<interface-id>`    | The interface name. |
| `<virtual-router-id>` |  The <span class="a-tooltip">[VRID](## "Virtual Router Identifier")</span> that identifies the group of VRRP routers.|
| `<afi>` |  The address family; `ipv4` or `ipv6`.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show interface swp1 ip vrrp virtual-router 44 address-family ipv4
                     operational
-------------------  -----------------
vrrp-interface       vrrp4-10-1 
vmac                 00:00:5e:00:01:2c 
primary-addr         10.0.0.2
status               Master 
priority             110 
master-adv-interval  1000 
skew-time            570 
down-interval        3570 
counters 
  adv-tx             947 
  adv-rx             0 
  garp-tx            1 
  state-transitions  2 
[virtual-addresses]  10.0.0.1
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show router vrrp</h>

Shows global VRRP configuration on the switch.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show router vrrp
                        applied
----------------------  -------
enable                  on     
advertisement-interval  1000   
preempt                 on     
priority                100
```
