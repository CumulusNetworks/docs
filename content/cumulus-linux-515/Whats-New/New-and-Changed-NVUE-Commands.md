---
title: New and Changed NVUE Commands
author: Cumulus Networks
weight: -30
product: Cumulus Linux
version: "5.15"
toc: 1
---

## Changes to Command Syntax

The syntax for the following commands has changed in Cumulus Linux 5.15.

{{< tabs "12 ">}}
{{< tab "DHCP Server ">}}

| CL5.14.0 and Earlier | CL5.15 and Later |
| --- | --- |
| `nv show service dhcp-server <vrf-id>` | `nv show vrf <vrf-id> dhcp-server-v4` |
| `nv show service dhcp-server <vrf-id> interface` | `nv show vrf <vrf-id> dhcp-server-v4 interface` |
| `nv show service dhcp-server <vrf-id> interface <interface-id>` | `nv show vrf <vrf-id> dhcp-server-v4 interface <interface-id>` |
| `nv show service dhcp-server <vrf-id> pool` | `nv show vrf <vrf-id> dhcp-server-v4 subnet` |
| `nv show service dhcp-server <vrf-id> pool <pool-id>` | `nv show vrf <vrf-id> dhcp-server-v4 subnet <subnet-id>` |
| `nv show service dhcp-server <vrf-id> pool <pool-id> domain-name-server` | `nv show vrf <vrf-id> dhcp-server-v4 subnet <subnet-id> domain-name-server` |
| `nv show service dhcp-server <vrf-id> pool <pool-id> domain-name-server <server-id>` | `nv show vrf <vrf-id> dhcp-server-v4 subnet <subnet-id> domain-name-server <server-id>` |
| `nv show service dhcp-server <vrf-id> pool <pool-id> gateway` | `nv show vrf <vrf-id> dhcp-server-v4 subnet <subnet-id> gateway` |
| `nv show service dhcp-server <vrf-id> pool <pool-id> gateway <gateway-id>` | `nv show vrf <vrf-id> dhcp-server-v4 subnet <subnet-id> gateway <gateway-id>` |
| `nv show service dhcp-server <vrf-id> pool <pool-id> range` | `nv show vrf <vrf-id> dhcp-server-v4 subnet <subnet-id> range` |
| `nv show service dhcp-server <vrf-id> pool <pool-id> range <range-id>` | `nv show vrf <vrf-id> dhcp-server-v4 subnet <subnet-id> range <range-id>` |
| `nv show service dhcp-server <vrf-id> domain-name-server` | `nv show vrf <vrf-id> dhcp-server-v4 domain-name-server` |
| `nv show service dhcp-server <vrf-id> domain-name-server <server-id>` | `nv show vrf <vrf-id> dhcp-server-v4 domain-name-server <server-id>` |
| `nv show service dhcp-server <vrf-id> static` | `nv show vrf <vrf-id> dhcp-server-v4 static-host` |
| `nv show service dhcp-server <vrf-id> static <static-id>`| `nv show vrf <vrf-id> dhcp-server-v4 static-host <host-id>` |
| `nv set service dhcp-server <vrf-id>` | `nv set vrf <vrf-id> dhcp-server-v4` |
| `nv set service dhcp-server <vrf-id> interface <interface-id>` | `nv set vrf <vrf-id> dhcp-server-v4 interface <interface-id>` |
| `nv set service dhcp-server <vrf-id> pool <pool-id>` | `nv set vrf <vrf-id> dhcp-server-v4 subnet <subnet-id>` |
| `nv set service dhcp-server <vrf-id> pool <pool-id> domain-name-server <server-id>` | `nv set vrf <vrf-id> dhcp-server-v4 subnet <subnet-id> domain-name-server <server-id>` |
| `nv set service dhcp-server <vrf-id> pool <pool-id> gateway <gateway-id>` | `nv set vrf <vrf-id> dhcp-server-v4 subnet <subnet-id> gateway <gateway-id>` |
| `nv set service dhcp-server <vrf-id> pool <pool-id> range <range-id>` |`nv set vrf <vrf-id> dhcp-server-v4 subnet <subnet-id> range <range-id>` |
| `nv set service dhcp-server <vrf-id> pool <pool-id> range <range-id> to <ipv4>` | `nv set vrf <vrf-id> dhcp-server-v4 subnet <subnet-id> range <range-id> to <ipv4>` |
| `nv set service dhcp-server <vrf-id> pool <pool-id> lease-time (180-31536000)` | `nv set vrf <vrf-id> dhcp-server-v4 subnet <subnet-id> lease-time (180-31536000)` |
| `nv set service dhcp-server <vrf-id> pool <pool-id> ping-check (on\|off)` | `nv set vrf <vrf-id> dhcp-server-v4 subnet <subnet-id> ping-check (enabled\|disabled)` |
| `nv set service dhcp-server <vrf-id> pool <pool-id> default-url <value>` | `nv set vrf <vrf-id> dhcp-server-v4 subnet <subnet-id> default-url <value>` |
| `nv set service dhcp-server <vrf-id> pool <pool-id> cumulus-provision-url <value>` | `nv set vrf <vrf-id> dhcp-server-v4 subnet <subnet-id> provision-url <value>` |
| `nv set service dhcp-server <vrf-id> pool <pool-id> domain-name (none\|<idn-hostname>)` | `nv set vrf <vrf-id> dhcp-server-v4 subnet <subnet-id> domain-name (none\|<idn-hostname>)` |
| `nv set service dhcp-server <vrf-id> domain-name-server <server-id>` | `nv set vrf <vrf-id> dhcp-server-v4 domain-name-server <server-id>` |
| `nv set service dhcp-server <vrf-id> static <static-id>` | `nv set vrf <vrf-id> dhcp-server-v4 static-host <host-id>` |
| `nv set service dhcp-server <vrf-id> static <static-id> mac-address <mac>` |`nv set vrf <vrf-id> dhcp-server-v4 static-host <host-id> mac-address <mac>` |
| `nv set service dhcp-server <vrf-id> static <static-id> ip-address <ipv4>` | `nv set vrf <vrf-id> dhcp-server-v4 static-host <host-id> ip-address <ipv4>` |
| `nv set service dhcp-server <vrf-id> static <static-id> cumulus-provision-url <value>` | `nv set vrf <vrf-id> dhcp-server-v4 static-host <host-id> provision-url <value>` |
| `nv set service dhcp-server <vrf-id> static <static-id> host-id-circuit-id <value>` | `nv set vrf <vrf-id> dhcp-server-v4 static-host <host-id> agent-remoteid-circuitid <value>` |
| `nv set service dhcp-server <vrf-id> static <static-id> ifname <interface-name>` | `nv set vrf <vrf-id> dhcp-server-v4 static-host <host-id> ifname <interface-name>` |
| `nv set service dhcp-server <vrf-id> static <static-id> vendor-class <value>` | `nv set vrf <vrf-id> dhcp-server-v4 static-host <host-id> ifname <interface-name> vendor-class-id <value>` |
| `nv set service dhcp-server <vrf-id> domain-name (none\|<idn-hostname>)` | `nv set vrf <vrf-id> dhcp-server-v4 domain-name (none\|<idn-hostname>)` |
| `nv show service dhcp-server6 <vrf-id>` | `nv show vrf <vrf-id> dhcp-server-v6` |
| `nv show service dhcp-server6 <vrf-id> interface` | `nv show vrf <vrf-id> dhcp-server-v6 interface` |
| `nv show service dhcp-server6 <vrf-id> interface <interface-id>` | `nv show vrf <vrf-id> dhcp-server-v6 interface <interface-id>` |
| `nv show service dhcp-server6 <vrf-id> pool` | `nv show vrf <vrf-id> dhcp-server-v6 subnet` |
| `nv show service dhcp-server6 <vrf-id> pool <pool-id>` | `nv show vrf <vrf-id> dhcp-server-v6 subnet <subnet-id>` |
| `nv show service dhcp-server6 <vrf-id> pool <pool-id> domain-name-server` | `nv show vrf <vrf-id> dhcp-server-v6 subnet <subnet-id> domain-name-server` |
| `nv show service dhcp-server6 <vrf-id> pool <pool-id> domain-name-server <server-id>` | `nv show vrf <vrf-id> dhcp-server-v6 subnet <subnet-id> domain-name-server <server-id>` |
| `nv show service dhcp-server6 <vrf-id> pool <pool-id> range` | `nv show vrf <vrf-id> dhcp-server-v6 subnet <subnet-id> range` |
| `nv show service dhcp-server6 <vrf-id> pool <pool-id> range <range-id>` | `nv show vrf <vrf-id> dhcp-server-v6 subnet <subnet-id> range <range-id>` |
| `nv show service dhcp-server6 <vrf-id> domain-name-server` | `nv show vrf <vrf-id> dhcp-server-v6 domain-name-server` |
| `nv show service dhcp-server6 <vrf-id> domain-name-server <server-id>` | `nv show vrf <vrf-id> dhcp-server-v6 domain-name-server <server-id>` |
| `nv show service dhcp-server6 <vrf-id> static` | `nv show vrf <vrf-id> dhcp-server-v6 static-host` |
| `nv show service dhcp-server6 <vrf-id> static <static-id>` | `nv show vrf <vrf-id> dhcp-server-v6 static-host <host-id>` |
| `nv set service dhcp-server6 <vrf-id>` | `nv set vrf <vrf-id> dhcp-server-v6` |
| `nv set service dhcp-server6 <vrf-id> interface <interface-id>` | `nv set vrf <vrf-id> dhcp-server-v6 interface <interface-id>` |
| `nv set service dhcp-server6 <vrf-id> pool <pool-id>` | `nv set vrf <vrf-id> dhcp-server-v6 subnet <subnet-id> `|
| `nv set service dhcp-server6 <vrf-id> pool <pool-id> domain-name-server <server-id>` | `nv set vrf <vrf-id> dhcp-server-v6 subnet <subnet-id> domain-name-server <server-id>` |
| `nv set service dhcp-server6 <vrf-id> pool <pool-id> range <range-id>` | `nv set vrf <vrf-id> dhcp-server-v6 subnet <subnet-id> range <range-id>` |
| `nv set service dhcp-server6 <vrf-id> pool <pool-id> range <range-id> to <ipv6>` | `nv set vrf <vrf-id> dhcp-server-v6 subnet <subnet-id> range <range-id> to <ipv6>` |
| `nv set service dhcp-server6 <vrf-id> pool <pool-id> lease-time (180-31536000)` | `nv set vrf <vrf-id> dhcp-server-v6 subnet <subnet-id> lease-time (180-31536000)` |
| `nv set service dhcp-server6 <vrf-id> pool <pool-id> ping-check (on\|off)` | `nv set vrf <vrf-id> dhcp-server-v6 subnet <subnet-id> ping-check (enabled\|disabled)` |
| `nv set service dhcp-server6 <vrf-id> pool <pool-id> default-url <value>` | `nv set vrf <vrf-id> dhcp-server-v6 subnet <subnet-id> default-url <value>` |
| `nv set service dhcp-server6 <vrf-id> pool <pool-id> cumulus-provision-url <value>` | `nv set vrf <vrf-id> dhcp-server-v6 subnet <subnet-id> provision-url <value>` |
| `nv set service dhcp-server6 <vrf-id> pool <pool-id> domain-name (none\|<idn-hostname>)` | `nv set vrf <vrf-id> dhcp-server-v6 subnet <subnet-id> domain-name (none\|<idn-hostname>)` |
| `nv set service dhcp-server6 <vrf-id> domain-name-server <server-id>` | `nv set vrf <vrf-id> dhcp-server-v6 domain-name-server <server-id>` |
| `nv set service dhcp-server6 <vrf-id> static <static-id>` | `nv set vrf <vrf-id> dhcp-server-v6 static-host <host-id>` |
| `nv set service dhcp-server6 <vrf-id> static <static-id> mac-address <mac>` | `nv set vrf <vrf-id> dhcp-server-v6 static-host <host-id> mac-address <mac>` |
| `nv set service dhcp-server6 <vrf-id> static <static-id> ip-address <ipv6>` | `nv set vrf <vrf-id> dhcp-server-v6 static-host <host-id> ip-address <ipv6>` |
| `nv set service dhcp-server6 <vrf-id> static <static-id> cumulus-provision-url <value>` | `nv set vrf <vrf-id> dhcp-server-v6 static-host <host-id> provision-url <value>` |
| `nv set service dhcp-server6 <vrf-id> static <static-id> ifname <interface-name>` | `nv set vrf <vrf-id> dhcp-server-v6 static-host <host-id> ifname <interface-name>` |
| `nv set service dhcp-server6 <vrf-id> static <static-id> vendor-class <value>` | `nv set vrf <vrf-id> dhcp-server-v6 static-host <host-id> ifname <interface-name> vendor-class-id <value>` |
| `nv set service dhcp-server6 <vrf-id> domain-name (none\|<idn-hostname>)` | `nv set vrf <vrf-id> dhcp-server-v6 domain-name (none\|<idn-hostname>)` |

{{< /tab >}}
{{< tab "DNS Server">}}

| CL5.14.0 and Earlier | CL5.15 and Later |
| --- | --- |
| `nv set service dns <vrf-id> server <dns-server-id>` | `nv set system dns server <dns-server-id>` |
| `nv set service dns <vrf-id> search <domain-id>` | `nv set system dns search <dns-search-id>` |
| `nv show service dns` | `nv show system dns` |
| `nv show service dns <vrf-id> server` | `nv show system dns server` |
| `nv show service dns <vrf-id> server <dns-server-id>` | `nv show system dns server <dns-server-id>` |

{{< /tab >}}
{{< tab "NTP ">}}

| CL5.14.0 and Earlier | CL5.15 and Later |
| --- | --- |
| `nv set service ntp <vrf-id> server <server-id>` | `nv set system ntp server <server-id>` |
| `nv set service ntp <vrf-id> server <server-id> iburst (on\|off)` | `nv set system ntp server <server-id> iburst (enabled\|disabled)` |
| `nv set service ntp <vrf-id> listen <interface-name>` | `nv set system ntp listen <interface-id>` |
| `nv show service ntp` | `nv show system ntp` |
| `nv show service ntp <vrf-id> server`| `nv show system ntp server` |
| `nv show service ntp <vrf-id> server <server-id>` | `nv show system ntp server <server-id>` |

{{< /tab >}}
{{< tab "System ">}}

| CL5.14.0 and Earlier | CL5.15 and Later |
| --- | --- |
| `nv show system time` | `nv show system date-time` |
| `nv show platform asic` | `nv show platform asic <asic-id>` |

{{< /tab >}}
{{< tab "LLDP ">}}

| CL5.14.0 and Earlier | CL5.15 and Later |
| --- | --- |
| `nv show service lldp` | `nv show system lldp` |
| `nv set service lldp` | `nv set system lldp` |
| `nv show service lldp application-tlv` | `nv show system lldp application-tlv` |
| `nv set service lldp application-tlv` | `nv set system lldp application-tlv` |
| `nv set service lldp dot1-tlv` | `nv set system lldp dot1-tlv` |
| `nv set service lldp lldp-med-inventory-tlv` | `nv set system lldp lldp-med-inventory-tlv` |
| `nv set service lldp mode` | `nv set system lldp mode` |
| `nv set service lldp tx-interval` | `nv set system lldp tx-interval` |
| `nv set service lldp tx-hold-multiplier` | `nv set system lldp tx-hold-multiplier` |
| `nv set service lldp state` | `nv set system lldp state` |

{{< /tab >}}
{{< tab "IP Interface">}}

| CL5.14.0 and Earlier | CL5.15 and Later |
| --- | --- |
| `nv set interface <interface-id> ip vrrp state (enabled\|disabled)` | `nv set interface <interface-id> ipv4 vrrp state (enabled\|disabled)` |
| `nv set interface <interface-id> ip vrrp virtual-router <virtual-router-id>` | `nv set interface <interface-id> ipv4 vrrp virtual-router <virtual-router-id>` |
| `nv set interface <interface-id> ip vrrp virtual-router <virtual-router-id> address <ip-address-id>` | `nv set interface <interface-id> ipv4 vrrp virtual-router <virtual-router-id> address <ip-address-id>` |
| `nv set interface <interface-id> ip vrrp virtual-router <virtual-router-id> version (2\|3)` | `nv set interface <interface-id> ipv4 vrrp virtual-router <virtual-router-id> version (2\|3)` |
| `nv set interface <interface-id> ip vrrp virtual-router <virtual-router-id> priority (1-254\|auto)` | `nv set interface <interface-id> ipv4 vrrp virtual-router <virtual-router-id> priority (1-254\|auto)` |
| `nv set interface <interface-id> ip vrrp virtual-router <virtual-router-id> preempt (enabled\|disabled\|auto)` | `nv set interface <interface-id> ipv4 vrrp virtual-router <virtual-router-id> preempt (enabled\|disabled\|auto)` |
| `nv set interface <interface-id> ip vrrp virtual-router <virtual-router-id> advertisement-interval (10-40950\|auto)` | `nv set interface <interface-id> ipv4 vrrp virtual-router <virtual-router-id> advertisement-interval (10-40950\|auto)` |
| `nv set interface <interface-id> ip vrrp state (enabled\|disabled)` | `nv set interface <interface-id> ipv6 vrrp state (enabled\|disabled)` |
| `nv set interface <interface-id> ip vrrp virtual-router <virtual-router-id>` | `nv set interface <interface-id> ipv6 vrrp virtual-router <virtual-router-id>` |
| `nv set interface <interface-id> ip vrrp virtual-router <virtual-router-id> address <ip-address-id>` | `nv set interface <interface-id> ipv6 vrrp virtual-router <virtual-router-id> address <ip-address-id>` |
| `nv set interface <interface-id> ip vrrp virtual-router <virtual-router-id> version (2\|3)` | `nv set interface <interface-id> ipv6 vrrp virtual-router <virtual-router-id> version (2\|3)` |
| `nv set interface <interface-id> ip vrrp virtual-router <virtual-router-id> priority (1-254\|auto)` | `nv set interface <interface-id> ipv6 vrrp virtual-router <virtual-router-id> priority (1-254\|auto)` |
| `nv set interface <interface-id> ip vrrp virtual-router <virtual-router-id> preempt (enabled\|disabled\|auto)` | `nv set interface <interface-id> ipv6 vrrp virtual-router <virtual-router-id> preempt (enabled\|disabled\|auto)` |
| `nv set interface <interface-id> ip vrrp virtual-router <virtual-router-id> advertisement-interval (10-40950\|auto)` | `nv set interface <interface-id> ipv6 vrrp virtual-router <virtual-router-id> advertisement-interval (10-40950\|auto)` |
| `nv show interface <interface-id> ip vrrp` | `nv show interface <interface-id> ipv4 vrrp` |
| `nv show interface <interface-id> ip vrrp virtual-router` | `nv show interface <interface-id> ipv4 vrrp virtual-router` |
| `nv show interface <interface-id> ip vrrp virtual-router <virtual-router-id>` | `nv show interface <interface-id> ipv4 vrrp virtual-router <virtual-router-id>` |
| `nv show interface <interface-id> ip vrrp virtual-router <virtual-router-id> address` | `nv show interface <interface-id> ipv4 vrrp virtual-router <virtual-router-id> address` |
| `nv show interface <interface-id> ip vrrp virtual-router <virtual-router-id> address <ip-address-id>` | `nv show interface <interface-id> ipv4 vrrp virtual-router <virtual-router-id> address <ip-address-id>` |
| `nv show interface <interface-id> ip vrrp` | `nv show interface <interface-id> ipv6 vrrp` |
| `nv show interface <interface-id> ip vrrp virtual-router` | `nv show interface <interface-id> ipv6 vrrp virtual-router` |
| `nv show interface <interface-id> ip vrrp virtual-router <virtual-router-id>` | `nv show interface <interface-id> ipv6 vrrp virtual-router <virtual-router-id>` |
| `nv show interface <interface-id> ip vrrp virtual-router <virtual-router-id> address` | `nv show interface <interface-id> ipv6 vrrp virtual-router <virtual-router-id> address` |
| `nv show interface <interface-id> ip vrrp virtual-router <virtual-router-id> address <ip-address-id>` | `nv show interface <interface-id> ipv6 vrrp virtual-router <virtual-router-id> address <ip-address-id>` |
| `nv set interface <interface-id> ip neighbor-discovery rdnss <ipv6-address-id>` |`nv set interface <interface-id> ipv6 neighbor-discovery rdnss <ipv6-address-id>` |
| `nv set interface <interface-id> ip neighbor-discovery rdnss <ipv6-address-id> lifetime (0-4294967295\|infinite\|auto)` | `nv set interface <interface-id> ipv6 neighbor-discovery rdnss <ipv6-address-id> lifetime (0-4294967295\|infinite\|auto)` |
| `nv set interface <interface-id> ip neighbor-discovery prefix <ipv6-prefix-id>` | `nv set interface <interface-id> ipv6 neighbor-discovery prefix <ipv6-prefix-id>` |
| `nv set interface <interface-id> ip neighbor-discovery prefix <ipv6-prefix-id> valid-lifetime (0-4294967295\|infinite)` | `nv set interface <interface-id> ipv6 neighbor-discovery prefix <ipv6-prefix-id> valid-lifetime (0-4294967295\|infinite)` |
| `nv set interface <interface-id> ip neighbor-discovery prefix <ipv6-prefix-id> preferred-lifetime (0-4294967295\|infinite)` | `nv set interface <interface-id> ipv6 neighbor-discovery prefix <ipv6-prefix-id> preferred-lifetime (0-4294967295\|infinite)` |
| `nv set interface <interface-id> ip neighbor-discovery prefix <ipv6-prefix-id> off-link (enabled\|disabled)` | `nv set interface <interface-id> ipv6 neighbor-discovery prefix <ipv6-prefix-id> off-link (enabled\|disabled)` |
| `nv set interface <interface-id> ip neighbor-discovery prefix <ipv6-prefix-id> autoconfig (enabled\|disabled)` | `nv set interface <interface-id> ipv6 neighbor-discovery prefix <ipv6-prefix-id> autoconfig (enabled\|disabled)` |
| `nv set interface <interface-id> ip neighbor-discovery prefix <ipv6-prefix-id> router-address enabled\|disabled` | `nv set interface <interface-id> ipv6 neighbor-discovery prefix <ipv6-prefix-id> router-address enabled\|disabled` |
| `nv set interface <interface-id> ip neighbor-discovery dnssl <domain-name-id>` | `nv set interface <interface-id> ipv6 neighbor-discovery dnssl <domain-name-id>` |
| `nv set interface <interface-id> ip neighbor-discovery dnssl <domain-name-id> lifetime (0-4294967295\|infinite\|auto)` | `nv set interface <interface-id> ipv6 neighbor-discovery dnssl <domain-name-id> lifetime (0-4294967295\|infinite\|auto)` |
| `nv set interface <interface-id> ip neighbor-discovery router-advertisement state enabled\|disabled` | `nv set interface <interface-id> ipv6 neighbor-discovery router-advertisement state enabled\|disabled` |
| `nv set interface <interface-id> ip neighbor-discovery router-advertisement interval (70-1800000)` | `nv set interface <interface-id> ipv6 neighbor-discovery router-advertisement interval (70-1800000)` |
| `nv set interface <interface-id> ip neighbor-discovery router-advertisement interval-option enabled\|disabled` | `nv set interface <interface-id> ipv6 neighbor-discovery router-advertisement interval-option enabled\|disabled` |
| `nv set interface <interface-id> ip neighbor-discovery router-advertisement fast-retransmit enabled\|disabled` | `nv set interface <interface-id> ipv6 neighbor-discovery router-advertisement fast-retransmit enabled\|disabled` |
| `nv set interface <interface-id> ip neighbor-discovery router-advertisement lifetime (0-9000)` | `nv set interface <interface-id> ipv6 neighbor-discovery router-advertisement lifetime (0-9000)` |
| `nv set interface <interface-id> ip neighbor-discovery router-advertisement reachable-time (0-3600000)` | `nv set interface <interface-id> ipv6 neighbor-discovery router-advertisement reachable-time (0-3600000)` |
| `nv set interface <interface-id> ip neighbor-discovery router-advertisement retransmit-time (0-4294967295)` | `nv set interface <interface-id> ipv6 neighbor-discovery router-advertisement retransmit-time (0-4294967295)` |
| `nv set interface <interface-id> ip neighbor-discovery router-advertisement managed-config enabled\|disabled` | `nv set interface <interface-id> ipv6 neighbor-discovery router-advertisement managed-config enabled\|disabled` |
| `nv set interface <interface-id> ip neighbor-discovery router-advertisement other-config enabled\|disabled` | `nv set interface <interface-id> ipv6 neighbor-discovery router-advertisement other-config enabled\|disabled` |
| `nv set interface <interface-id> ip neighbor-discovery router-advertisement hop-limit (0-255)` | `nv set interface <interface-id> ipv6 neighbor-discovery router-advertisement hop-limit (0-255)` |
| `nv set interface <interface-id> ip neighbor-discovery router-advertisement router-preference (high\|medium\|low)` | `nv set interface <interface-id> ipv6 neighbor-discovery router-advertisement router-preference (high\|medium\|low)` |
| `nv set interface <interface-id> ip neighbor-discovery home-agent state enabled\|disabled` | `nv set interface <interface-id> ipv6 neighbor-discovery home-agent state enabled\|disabled` |
| `nv set interface <interface-id> ip neighbor-discovery home-agent lifetime (0-65520)` | `nv set interface <interface-id> ipv6 neighbor-discovery home-agent lifetime (0-65520)` |
| `nv set interface <interface-id> ip neighbor-discovery home-agent preference (0-65535)` | `nv set interface <interface-id> ipv6 neighbor-discovery home-agent preference (0-65535)` |
| `nv set interface <interface-id> ip neighbor-discovery state enabled\|disabled` | `nv set interface <interface-id> ipv6 neighbor-discovery state enabled\|disabled` |
| `nv set interface <interface-id> ip neighbor-discovery mtu (1-65535)` |`nv set interface <interface-id> ipv6 neighbor-discovery mtu (1-65535)` |
| `nv show interface <interface-id> ip neighbor-discovery` | `nv show interface <interface-id> ipv6 neighbor-discovery` |
| `nv show interface <interface-id> ip neighbor-discovery rdnss` | `nv show interface <interface-id> ipv6 neighbor-discovery rdnss` |
| `nv show interface <interface-id> ip neighbor-discovery rdnss <ipv6-address-id>` | `nv show interface <interface-id> ipv6 neighbor-discovery rdnss <ipv6-address-id>` |
| `nv show interface <interface-id> ip neighbor-discovery prefix` | `nv show interface <interface-id> ipv6 neighbor-discovery prefix` |
| `nv show interface <interface-id> ip neighbor-discovery prefix <ipv6-prefix-id>` | `nv show interface <interface-id> ipv6 neighbor-discovery prefix <ipv6-prefix-id>` |
| `nv show interface <interface-id> ip neighbor-discovery dnssl` | `nv show interface <interface-id> ipv6 neighbor-discovery dnssl` |
| `nv show interface <interface-id> ip neighbor-discovery dnssl <domain-name-id>` | `nv show interface <interface-id> ipv6 neighbor-discovery dnssl <domain-name-id>` |
| `nv show interface <interface-id> ip neighbor-discovery router-advertisement` | `nv show interface <interface-id> ipv6 neighbor-discovery router-advertisement` |
| `nv show interface <interface-id> ip neighbor-discovery home-agent` | `nv show interface <interface-id> ipv6 neighbor-discovery home-agent` |
| `nv set interface <interface-id> ip igmp state enabled\|disabled` | `nv set interface <interface-id> ipv4 igmp state enabled\|disabled` |
| `nv set interface <interface-id> ip igmp static-group <static-group-id>` | `nv set interface <interface-id> ipv4 igmp static-group <static-group-id>` |
| `nv set interface <interface-id> ip igmp static-group <static-group-id> source-address <source-addresses-id>` | `nv set interface <interface-id> ipv4 igmp static-group <static-group-id> source-address <source-addresses-id>` |
| `nv set interface <interface-id> ip igmp version (2\|3)` | `nv set interface <interface-id> ipv4 igmp version (2\|3)` |
| `nv set interface <interface-id> ip igmp fast-leave enabled\|disabled` | `nv set interface <interface-id> ipv4 igmp fast-leave enabled\|disabled` |
| `nv set interface <interface-id> ip igmp query-interval (1-65535)` | `nv set interface <interface-id> ipv4 igmp query-interval (1-65535)` |
| `nv set interface <interface-id> ip igmp query-max-response-time (1-6553)` | `nv set interface <interface-id> ipv4 igmp query-max-response-time (1-6553)` |
| `nv set interface <interface-id> ip igmp last-member-query-interval (1-6553)` | `nv set interface <interface-id> ipv4 igmp last-member-query-interval (1-6553)` |
| `nv set interface <interface-id> ip igmp last-member-query-count (1-255)` | `nv set interface <interface-id> ipv4 igmp last-member-query-count (1-255)` |
| `nv show interface <interface-id> ip igmp` | `nv show interface <interface-id> ipv4 igmp` |
| `nv show interface <interface-id> ip igmp static-group` | `nv show interface <interface-id> ipv4 igmp static-group` |
| `nv show interface <interface-id> ip igmp static-group <static-group-id>` | `nv show interface <interface-id> ipv4 igmp static-group <static-group-id>` |
| `nv show interface <interface-id> ip igmp static-group <static-group-id> source-address` | `nv show interface <interface-id> ipv4 igmp static-group <static-group-id> source-address` |
| `nv show interface <interface-id> ip igmp static-group <static-group-id> source-address <source-addresses-id>` | `nv show interface <interface-id> ipv4 igmp static-group <static-group-id> source-address <source-addresses-id>` |
| `nv show interface <interface-id> ip igmp group` | `nv show interface <interface-id> ipv4 igmp group` |
| `nv show interface <interface-id> ip igmp group <group-id>` | `nv show interface <interface-id> ipv4 igmp group <group-id>` |
| `nv set interface <interface-id> ip vrr vrr-state (up\|down)` | `nv set interface <interface-id> ipv4 vrr vrr-state (up\|down)` |
| `nv set interface <interface-id> ip vrr address <ip-prefix-id>` | `nv set interface <interface-id> ipv4 vrr address <ipv4-prefix-id>` |
| `nv set interface <interface-id> ip vrr state enabled\|disabled` | `nv set interface <interface-id> ipv4 vrr state enabled\|disabled` |
| `nv set interface <interface-id> ip vrr mac-id (1-255\|none)` | `nv set interface <interface-id> ipv4 vrr mac-id (1-255\|none)`|
| `nv set interface <interface-id> ip vrr mac-address (auto\|<mac>)` | `nv set interface <interface-id> ipv4 vrr mac-address (auto\|<mac>)` |
| `nv set interface <interface-id> ip vrr vrr-state (up\|down)` | `nv set interface <interface-id> ipv6 vrr vrr-state (up\|down)` |
| `nv set interface <interface-id> ip vrr address <ip-prefix-id>` | `nv set interface <interface-id> ipv6 vrr address <ipv6-prefix-id>` |
| `nv set interface <interface-id> ip vrr state enabled\|disabled` | `nv set interface <interface-id> ipv6 vrr state enabled\|disabled` |
| `nv set interface <interface-id> ip vrr mac-id (1-255\|none)` | `nv set interface <interface-id> ipv6 vrr mac-id (1-255\|none)` |
| `nv set interface <interface-id> ip vrr mac-address (auto\|<mac>)` | `nv set interface <interface-id> ipv6 vrr mac-address (auto\|<mac>)` |
| `nv show interface <interface-id> ip vrr` | `nv show interface <interface-id> ipv4 vrr` |
| `nv show interface <interface-id> ip vrr vrr-state` | `nv show interface <interface-id> ipv4 vrr vrr-state` |
| `nv show interface <interface-id> ip vrr address` | `nv show interface <interface-id> ipv4 vrr address` |
| `nv show interface <interface-id> ip vrr address <ip-prefix-id>` | `nv show interface <interface-id> ipv4 vrr address <ipv4-prefix-id>` |
| `nv show interface <interface-id> ip vrr` | `nv show interface <interface-id> ipv6 vrr` |
| `nv show interface <interface-id> ip vrr vrr-state` | `nv show interface <interface-id> ipv6 vrr vrr-state` |
| `nv show interface <interface-id> ip vrr address` | `nv show interface <interface-id> ipv6 vrr address` |
| `nv show interface <interface-id> ip vrr address <ip-prefix-id>` | `nv show interface <interface-id> ipv6 vrr address <ipv6-prefix-id>` |
| `nv set interface <interface-id> ip address <ip-prefix-id>` | `nv set interface <interface-id> ipv4 address <ipv4-prefix-id>` |
| `nv set interface <interface-id> ip gateway <ip-address-id>` | `nv set interface <interface-id> ipv4 gateway <ipv4-address-id>` |
| `nv set interface <interface-id> ip ipv4 forward enabled\|disabled` | `nv set interface <interface-id> ipv4 forward enabled\|disabled` |
| `nv set interface <interface-id> ip address <ip-prefix-id>` | `nv set interface <interface-id> ipv6 address <ipv6-prefix-id>` |
| `nv set interface <interface-id> ip gateway <ip-address-id>` | `nv set interface <interface-id> ipv6 gateway <ipv6-address-id>` |
| `nv set interface <interface-id> ip ipv6 state enabled\|disabled` | `nv set interface <interface-id> ipv6 state enabled\|disabled` |
| `nv set interface <interface-id> ip ipv6 forward enabled\|disabled` | `nv set interface <interface-id> ipv6 forward enabled\|disabled` |
| `nv show interface <interface-id> ip` | `nv show interface <interface-id> ipv4` |
| `nv show interface <interface-id> ip` | `nv show interface <interface-id> ipv6` |
| `nv show interface <interface-id> ip address` | `nv show interface <interface-id> ipv4 address` |
| `nv show interface <interface-id> ip address <ip-prefix-id>` | `nv show interface <interface-id> ipv4 address <ipv4-prefix-id>` |
| `nv show interface <interface-id> ip gateway` | `nv show interface <interface-id> ipv4 gateway` |
| `nv show interface <interface-id> ip gateway <ip-address-id>` | `nv show interface <interface-id> ipv4 gateway <ipv4-address-id>` |
| `nv show interface <interface-id> ip address` | `nv show interface <interface-id> ipv6 address` |
| `nv show interface <interface-id> ip address <ip-prefix-id>` | `nv show interface <interface-id> ipv6 address <ipv6-prefix-id>` |
| `nv show interface <interface-id> ip gateway` | `nv show interface <interface-id> ipv6 gateway` |
| `nv show interface <interface-id> ip gateway <ip-address-id>` | `nv show interface <interface-id> ipv6 gateway <ipv6-address-id>` |
| `nv show interface <interface-id> ip neighbor ipv4` | `nv show interface <interface-id> ipv4 neighbor` |
| `nv show interface <interface-id> ip neighbor ipv4 <neighbor-id>` | `nv show interface <interface-id> ipv4 neighbor <ipv4-neighbor-id>` |
| `nv show interface <interface-id> ip neighbor ipv6` | `nv show interface <interface-id> ipv6 neighbor` |
| `nv show interface <interface-id> ip neighbor ipv6 <neighbor-id>` | `nv show interface <interface-id> ipv6 neighbor <ipv6-neighbor-id>` |
| `nv set interface <interface-id> ip vrf <vrf-name>` | `nv set interface <interface-id> vrf <vrf-name>` |
| `nv set interface <interface-id> ip address dhcp` | `nv set interface <interface-id> ipv4 dhcp-client state enabled\|disabled` |
| `nv set interface <interface-id> ip address dhcp6` | `nv set interface <interface-id> ipv6 dhcp-client state enabled\|disabled` |

{{< /tab >}}
{{< tab "Link ">}}

| CL5.14.0 and Earlier | CL5.15 and Later |
| --- | --- |
| `nv show interface <interface-id> link phy-detail` | `nv show interface <interface-id> link phy health` |
| `nv show interface <interface-id> link phy-diag` | `nv show interface <interface-id> link phy detail` |
| `nv action clear interface <interface-id> link phy-detail` | `nv action clear interface <interface-id> link phy health` |

{{< /tab >}}
{{< tab "Telemetry ">}}

| CL5.14.0 and Earlier | CL5.15 and Later |
| --- | --- |
| `nv set system telemetry export otlp grpc cert-id <value>` | `nv set system telemetry export otlp grpc certificate <cert-id>` |
| `nv set system telemetry export otlp grpc destination <destination-id> cert-id <value>` | `nv set system telemetry export otlp grpc destination <destination-id> certificate <cert-id>` |

{{< /tab >}}
{{< tab "On/Off ">}}

| CL5.14.0 and Earlier | CL5.15 and Later |
| --- | --- |
| `nv set interface <interface-id> ip igmp fast-leave (on\|off)` | `nv set interface <interface-id> ip igmp fast-leave (enabled\|disabled)` |
| `nv set interface <interface-id> ptp forced-master on\|off` | `nv set interface <interface-id> ptp forced-master enabled\|disabled` |
| `nv set interface <interface-id> synce enable on\|off` | `nv set interface <interface-id> synce state enabled\|disabled` |
| `nv set interface <interface-id> ip ipv4 forward on\|off` | `nv set interface <interface-id> ip ipv4 forward enabled\|disabled` |
| `nv set interface <interface-id> link fast-linkup on\|off` | `nv set interface <interface-id> link fast-linkup enabled\|disabled` |
| `nv set interface <interface-id> ptp enable on\|off` | `nv set interface <interface-id> ptp state enabled\|disabled` |
| `nv set interface <interface-id> link auto-negotiate on\|off` | `nv set interface <interface-id> link auto-negotiate enabled\|disabled` |
| `nv set interface <interface-id> ptp shaper enable on\|off` | `nv set interface <interface-id> ptp shaper state enabled\|disabled` |
| `nv set interface <interface-id> ip ipv6 enable on\|off` | `nv set interface <interface-id> ip ipv6 state enabled\|disabled` |
| `nv set interface <interface-id> ip ipv6 forward on\|off` | `nv set interface <interface-id> ip ipv6 forward enabled\|disabled` |
| `nv set interface <interface-id> ptp mixed-multicast-unicast on\|off` | `nv set interface <interface-id> ptp mixed-multicast-unicast enabled\|disabled` |
| `nv set interface <interface-id> ptp acceptable-master (on/off)` | `nv set interface <interface-id> ptp acceptable-master enabled\|disabled` |
| `nv set system global svi-force-up enable on\|off` | `nv set system global svi-force-up state enabled\|disabled` |
| `nv set system snmp-server trap-destination <trap-destination-id> username <username-id> auth-md5 <auth-id> encrypt-des <encrypt-id> engine-id <engine-id> inform on\|off` | `nv set system snmp-server trap-destination <trap-destination-id> username <username-id> auth-md5 <auth-id> encrypt-des <encrypt-id> engine-id <engine-id> inform enabled\|disabled` |
| `nv set system snmp-server trap-destination <trap-destination-id> username <username-id> auth-md5 <auth-id> encrypt-aes <encrypt-id> engine-id <engine-id> inform on\|off` | `nv set system snmp-server trap-destination <trap-destination-id> username <username-id> auth-md5 <auth-id> encrypt-aes <encrypt-id> engine-id <engine-id> inform enabled\|disabled` |
| `nv set system snmp-server trap-destination <trap-destination-id> username <username-id> auth-md5 <auth-id> engine-id <engine-id> inform on\|off` | `nv set system snmp-server trap-destination <trap-destination-id> username <username-id> auth-md5 <auth-id> engine-id <engine-id> inform enabled\|disabled` |
| `nv set system aaa tacacs authentication per-user-homedir on\|off` | `nv set system aaa tacacs authentication per-user-homedir enabled\|disabled` |
| `nv set system snmp-server trap-destination <trap-destination-id> vrf <vrf-name> username <username-id> auth-sha <auth-id> encrypt-des <encrypt-id> engine-id <engine-id> inform on\|off` | `nv set system snmp-server trap-destination <trap-destination-id> vrf <vrf-name> username <username-id> auth-sha <auth-id> encrypt-des <encrypt-id> engine-id <engine-id> inform enabled\|disabled` |
| `nv set system snmp-server trap-destination <trap-destination-id> username <username-id> auth-sha <auth-id> encrypt-aes <encrypt-id> engine-id <engine-id> inform on\|off` | `nv set system snmp-server trap-destination <trap-destination-id> username <username-id> auth-sha <auth-id> encrypt-aes <encrypt-id> engine-id <engine-id> inform enabled\|disabled` |
| `nv set system snmp-server trap-destination <trap-destination-id> vrf <vrf-name> username <username-id> auth-md5 <auth-id> engine-id <engine-id> inform on\|off` | `nv set system snmp-server trap-destination <trap-destination-id> vrf <vrf-name> username <username-id> auth-md5 <auth-id> engine-id <engine-id> inform enabled\|disabled` |
| `nv set system snmp-server trap-destination <trap-destination-id> username <username-id> auth-sha <auth-id> encrypt-aes <encrypt-id> engine-id <engine-id> inform on\|off` | `nv set system snmp-server trap-destination <trap-destination-id> username <username-id> auth-sha <auth-id> encrypt-aes <encrypt-id> engine-id <engine-id> inform enabled\|disabled` |
| `nv set system snmp-server trap-destination <trap-destination-id> vrf <vrf-name> username <username-id> auth-sha <auth-id> encrypt-aes <encrypt-id> engine-id <engine-id> inform on\|off` | `nv set system snmp-server trap-destination <trap-destination-id> vrf <vrf-name> username <username-id> auth-sha <auth-id> encrypt-aes <encrypt-id> engine-id <engine-id> inform enabled\|disabled` |
| `nv set system snmp-server trap-destination <trap-destination-id> username <username-id> auth-sha <auth-id> engine-id <engine-id> inform on\|off` | `nv set system snmp-server trap-destination <trap-destination-id> username <username-id> auth-sha <auth-id> engine-id <engine-id> inform enabled\|disabled` |
| `nv set system snmp-server trap-destination <trap-destination-id> vrf <vrf-name> username <username-id> auth-sha <auth-id> engine-id <engine-id> inform on\|off` | `nv set system snmp-server trap-destination <trap-destination-id> vrf <vrf-name> username <username-id> auth-sha <auth-id> engine-id <engine-id> inform enabled\|disabled` |
| `nv set system snmp-server trap-destination <trap-destination-id> vrf <vrf-name> username <username-id> auth-md5 <auth-id> encrypt-des <encrypt-id> engine-id <engine-id> inform on\|off` | `nv set system snmp-server trap-destination <trap-destination-id> vrf <vrf-name> username <username-id> auth-md5 <auth-id> encrypt-des <encrypt-id> engine-id <engine-id> inform enabled\|disabled` |
| `nv set system snmp-server trap-destination <trap-destination-id> username <username-id> auth-md5 <auth-id> encrypt-aes <encrypt-id> engine-id <engine-id> inform on\|off` | `nv set system snmp-server trap-destination <trap-destination-id> username <username-id> auth-md5 <auth-id> encrypt-aes <encrypt-id> engine-id <engine-id> inform enabled\|disabled` |
| `nv set system telemetry enable on\|off` | `nv set system telemetry state enabled\|disabled` |
| `nv set system wjh enable on\|off` | `nv set system wjh state enabled\|disabled` |
| `nv set service ptp <instance-id> ignore-source-id on\|off` | `nv set service ptp <instance-id> ignore-source-id enabled\|disabled` |
| `nv set service ptp <instance-id> profile <profile-id> two-step on\|off` | `nv set service ptp <instance-id> profile <profile-id> two-step enabled\|disabled` |
| `nv set service ptp <instance-id> enable on\|off` | `nv set service ptp <instance-id> state enabled\|disabled` |
| `nv set service ptp <instance-id> two-step on\|off` | `nv set service ptp <instance-id> two-step enabled\|disabled` |
| `nv set vrf <vrf-id> ptp enable on\|off` | `nv set vrf <vrf-id> ptp state enabled\|disabled` |
| `nv set nve vxlan flooding enable on\|off` | `nv set nve vxlan flooding state enabled\|disabled` |
| `nv set bridge domain <domain-id> multicast snooping enable on\|off` | `nv set bridge domain <domain-id> multicast snooping state enabled\|disabled` |
| `nv set bridge domain <domain-id> multicast snooping querier enable on\|off` | `nv set bridge domain <domain-id> multicast snooping querier state enabled\|disabled` |
| `nv set bridge domain <domain-id> vlan <vid> ptp enable on\|off` | `nv set bridge domain <domain-id> vlan <vid> ptp state enabled\|disabled` |
| `nv set bridge domain <domain-id> vlan <vid> vni <vni-id> flooding enable on\|off` | `nv set bridge domain <domain-id> vlan <vid> vni <vni-id> flooding state enabled\|disabled` |
| `nv set bridge domain <domain-id> svi-force-up enable on\|off` | `nv set bridge domain <domain-id> svi-force-up state enabled\|disabled` |
| `nv set system snmp-server trap-destination <trap-destination-id> username <username-id> auth-sha <auth-id> encrypt-des <encrypt-id> engine-id <engine-id> inform on\|off` | `nv set system snmp-server trap-destination <trap-destination-id> username <username-id> auth-sha <auth-id> encrypt-des <encrypt-id> engine-id <engine-id> inform (enabled/enabled)` |
| `nv set system synce enable on\|off` | `nv set system synce state enabled\|disabled` |
| `nv set interface <interface-id> lldp dcbx-ets-recomm-tlv on\|off` | `nv set interface <interface-id> lldp dcbx-ets-recomm-tlv enabled\|disabled` |
| `nv set interface <interface-id> bond mlag enable on\|off` | `nv set interface <interface-id> bond mlag state enabled\|disabled` |
| `nv set interface <interface-id> lldp dcbx-pfc-tlv on\|off` | `nv set interface <interface-id> lldp dcbx-pfc-tlv enabled\|disabled` |
| `nv set interface <interface-id> port-security enable on\|off` | `nv set interface <interface-id> port-security state enabled\|disabled` |
| `nv set interface <interface-id> bond lacp-bypass on\|off` | `nv set interface <interface-id> bond lacp-bypass enabled\|disabled` |
| `nv set interface <interface-id> link flap-protection enable on\|off` | `nv set interface <interface-id> link flap-protection state enabled\|disabled` |
| `nv set interface <interface-id> telemetry bw-gauge enable on\|off` | `nv set interface <interface-id> telemetry bw-gauge state enabled\|disabled` |
| `nv set interface <interface-id> lldp dcbx-ets-config-tlv on\|off` | `nv set interface <interface-id> lldp dcbx-ets-config-tlv enabled\|disabled` |
| `nv set interface <interface-id> bridge domain <domain-id> stp network on\|off` | `nv set interface <interface-id> bridge domain <domain-id> stp network enabled\|disabled` |
| `nv show interface <interface-id> bridge domain <domain-id> stp` | `nv show interface <interface-id> bridge domain <domain-id> stp` |
| `nv set interface <interface-id> bridge domain <domain-id> stp bpdu-guard on\|off` | `nv set interface <interface-id> bridge domain <domain-id> stp bpdu-guard enabled\|disabled` |
| `nv set interface <interface-id> bridge domain <domain-id> stp restrrole on\|off` | `nv set interface <interface-id> bridge domain <domain-id> stp restrrole enabled\|disabled` |
| `nv set interface <interface-id> bridge domain <domain-id> stp admin-edge on\|off` | `nv set interface <interface-id> bridge domain <domain-id> stp admin-edge enabled\|disabled` |
| `nv set interface <interface-id> bridge domain <domain-id> stp auto-edge on\|off` | `nv set interface <interface-id> bridge domain <domain-id> stp auto-edge enabled\|disabled` |
| `nv set interface <interface-id> bridge domain <domain-id> stp bpdu-filter on\|off` | `nv set interface <interface-id> bridge domain <domain-id> stp bpdu-filter enabled\|disabled` |
| `nv set interface <interface-id> bridge domain <domain-id> learning on\|off` | `nv set interface <interface-id> bridge domain <domain-id> learning enabled\|disabled` |
| `nv set system control-plane trap <trap-id> enable on\|off` | `nv set system control-plane trap <trap-id> state enabled\|disabled` |
| `nv set system port-mirror session <session-id> erspan enable on\|off` | `nv set system port-mirror session <session-id> erspan state enabled\|disabled` |
| `nv set system port-mirror session <session-id> erspan truncate enable on\|off` | `nv set system port-mirror session <session-id> erspan truncate state enabled\|disabled` |
| `nv set system port-mirror session <session-id> span enable on\|off` | `nv set system port-mirror session <session-id> span state enabled\|disabled` |
| `nv set system port-mirror session <session-id> span truncate enable on\|off` | `nv set system port-mirror session <session-id> span truncate state enabled\|disabled` |
| `nv set system forwarding ecmp-hash source-port on\|off` | `nv set system forwarding ecmp-hash source-port enabled\|disabled` |
| `nv set system forwarding ecmp-hash ip-protocol on\|off` | `nv set system forwarding ecmp-hash ip-protocol enabled\|disabled` |
| `nv set system forwarding ecmp-hash destination-port on\|off` | `nv set system forwarding ecmp-hash destination-port enabled\|disabled` |
| `nv set system forwarding ecmp-hash ipv6-label on\|off` | `nv set system forwarding ecmp-hash ipv6-label enabled\|disabled` |
| `nv set system forwarding ecmp-hash source-ip on\|off` | `nv set system forwarding ecmp-hash source-ip enabled\|disabled` |
| `nv set system forwarding ecmp-hash ingress-interface on\|off` | `nv set system forwarding ecmp-hash ingress-interface enabled\|disabled` |
| `nv set system forwarding ecmp-hash inner-source-ip on\|off` | `nv set system forwarding ecmp-hash inner-source-ip enabled\|disabled` |
| `nv set system forwarding ecmp-hash inner-ipv6-label on\|off` | `nv set system forwarding ecmp-hash inner-ipv6-label enabled\|disabled` |
| `nv set system forwarding ecmp-hash inner-destination-ip on\|off` | `nv set system forwarding ecmp-hash inner-destination-ip enabled\|disabled` |
| `nv set system forwarding ecmp-hash inner-ip-protocol on\|off` | `nv set system forwarding ecmp-hash inner-ip-protocol enabled\|disabled` |
| `nv set system forwarding ecmp-hash inner-destination-port on\|off` | `nv set system forwarding ecmp-hash inner-destination-port enabled\|disabled` |
| `nv set system forwarding ecmp-hash inner-source-port on\|off` | `nv set system forwarding ecmp-hash inner-source-port enabled\|disabled` |
| `nv set system forwarding ecmp-hash destination-ip on\|off` | `nv set system forwarding ecmp-hash destination-ip enabled\|disabled` |
| `nv set system forwarding ecmp-hash gtp-teid on\|off` | `nv set system forwarding ecmp-hash gtp-teid enabled\|disabled` |
| `nv set system forwarding lag-hash destination-port on\|off` | `nv set system forwarding lag-hash destination-port enabled\|disabled` |
| `nv set system forwarding lag-hash source-port on\|off` | `nv set system forwarding lag-hash source-port enabled\|disabled` |
| `nv set system forwarding lag-hash source-mac on\|off` | `nv set system forwarding lag-hash source-mac enabled\|disabled` |
| `nv set system forwarding lag-hash destination-mac on\|off` | `nv set system forwarding lag-hash destination-mac enabled\|disabled` |
| `nv set system forwarding lag-hash vlan on\|off` | `nv set system forwarding lag-hash vlan enabled\|disabled` |
| `nv set system forwarding lag-hash gtp-teid on\|off` | `nv set system forwarding lag-hash gtp-teid enabled\|disabled` |
| `nv set system forwarding lag-hash ether-type on\|off` | `nv set system forwarding lag-hash ether-type enabled\|disabled` |
| `nv set system forwarding lag-hash ip-protocol on\|off` | `nv set system forwarding lag-hash ip-protocol enabled\|disabled` |
| `nv set system forwarding lag-hash destination-ip on\|off` | `nv set system forwarding lag-hash destination-ip (enabled\|enabled)` |
| `nv set system forwarding lag-hash source-ip on\|off` | `nv set system forwarding lag-hash source-ip enabled\|disabled` |
| `nv set system lldp lldp-med-inventory-tlv on\|off` | `nv set system lldp lldp-med-inventory-tlv enabled\|disabled` |
| `nv set system lldp dot1-tlv on\|off` | `nv set system lldp dot1-tlv enabled\|disabled` |
| `nv set system control-plane policer lacp state on\|off` | `nv set system control-plane policer lacp state enabled\|disabled` |
| `nv set service dhcp-server6 <vrf-id> pool <pool-id> ping-check on\|off` | `nv set service dhcp-server6 <vrf-id> pool <pool-id> ping-check enabled\|disabled` |
| `nv set service dhcp-relay <vrf-id> agent enable on\|off` | `nv set service dhcp-relay <vrf-id> agent state enabled\|disabled` |
| `nv set service dhcp-server <vrf-id> pool <pool-id> ping-check on\|off` | `nv set service dhcp-server <vrf-id> pool <pool-id> ping-check enabled\|disabled` |
| `nv set service dhcp-relay <vrf-id> agent use-pif-circuit-id enable on\|off` | `nv set service dhcp-relay <vrf-id> agent use-pif-circuit-id state enabled\|disabled` |
| `nv set router adaptive-routing enable on\|off` | `nv set router adaptive-routing state enabled\|disabled` |
| `nv set router adaptive-routing link-utilization-threshold on\|off` | `nv set router adaptive-routing link-utilization-threshold enabled\|disabled` |
| `nv set nve vxlan mac-learning on\|off` | `nv set nve vxlan mac-learning enabled\|disabled` |
| `nv set nve vxlan arp-nd-suppress on\|off` | `nv set nve vxlan arp-nd-suppress enabled\|disabled` |
| `nv set bridge domain <domain-id> vlan <vid> vni <vni-id> mac-learning on\|off` | `nv set bridge domain <domain-id> vlan <vid> vni <vni-id> mac-learning enabled\|disabled` |
| `nv set qos roce enable on\|off` | `nv set qos roce state enabled\|disabled` |
| `nv set mlag enable on\|off` | `nv set mlag state enabled\|disabled` |
| `nv set mlag debug on\|off` | `nv set mlag debug enabled\|disabled` |
| `nv set evpn enable on\|off` | `nv set evpn state enabled\|disabled` |
| `nv set evpn multihoming enable on\|off` | `nv set evpn multihoming state enabled\|disabled` |
| `nv set evpn dad enable on\|off` | `nv set evpn dad state enabled\|disabled` |
| `nv set evpn vni <vni-id> route-advertise svi-ip (on\|off\|auto)` | `nv set evpn vni <vni-id> route-advertise svi-ip (enabled\|disabled\|auto)` |
| `nv set evpn vni <vni-id> route-advertise default-gateway (on\|off\|auto)` | `nv set evpn vni <vni-id> route-advertise default-gateway (enabled\|disabled\|auto)` |
| `nv set evpn multihoming ead-evi-route rx on\|off` | `nv set evpn multihoming ead-evi-route rx enabled\|disabled` |
| `nv set evpn multihoming ead-evi-route tx on\|off` | `nv set evpn multihoming ead-evi-route tx enabled\|disabled` |
| `nv set evpn route-advertise default-gateway on\|off` | `nv set evpn route-advertise default-gateway enabled\|disabled` |
| `nv set evpn route-advertise svi-ip on\|off` | `nv set evpn route-advertise svi-ip enabled\|disabled` |
| `nv set router ptm enable on\|off` | `nv set router ptm state enabled\|disabled` |
| `nv set router pbr enable on\|off` | `nv set router pbr state enabled\|disabled` |
| `nv set router policy route-map <route-map-id> rule <rule-id> match evpn-default-route on\|off` | `nv set router policy route-map <route-map-id> rule <rule-id> match evpn-default-route enabled\|disabled` |
| `nv set router policy route-map <route-map-id> rule <rule-id> set atomic-aggregate on\|off` | `nv set router policy route-map <route-map-id> rule <rule-id> set atomic-aggregate enabled\|disabled` |
| `nv set router policy route-map <route-map-id> rule <rule-id> set ipv6-nexthop-prefer-global on\|off` | `nv set router policy route-map <route-map-id> rule <rule-id> set ipv6-nexthop-prefer-global enabled\|disabled` |
| `nv set router bgp enable on\|off` | `nv set router bgp state enabled\|disabled` |
| `nv set router bgp graceful-shutdown on\|off` | `nv set router bgp graceful-shutdown enabled\|disabled` |
| `nv set router bgp wait-for-install on\|off` | `nv set router bgp wait-for-install enabled\|disabled` |
| `nv set router ospf enable on\|off` | `nv set router ospf state enabled\|disabled` |
| `nv set router igmp enable on\|off` | `nv set router igmp state enabled\|disabled` |
| `nv set router vrrp enable on\|off` | `nv set router vrrp state enabled\|disabled` |
| `nv set router vrrp preempt on\|off` | `nv set router vrrp preempt enabled\|disabled` |
| `nv set router vrr enable on\|off` | `nv set router vrr state enabled\|disabled` |
| `nv set router pim enable on\|off` | `nv set router pim state enabled\|disabled` |
| `nv set vrf <vrf-id> router pim ecmp enable on\|off` | `nv set vrf <vrf-id> router pim ecmp state enabled\|disabled` |
| `nv set vrf <vrf-id> router pim ecmp rebalance on\|off` | `nv set vrf <vrf-id> router pim ecmp rebalance enabled\|disabled` |
| `nv set vrf <vrf-id> router pim address-family ipv4 send-v6-secondary on\|off` | `nv set vrf <vrf-id> router pim address-family ipv4 send-v6-secondary enabled\|disabled` |
| `nv set vrf <vrf-id> router pim enable on\|off` | `nv set vrf <vrf-id> router pim state enabled\|disabled` |
| `nv set interface <interface-id> router pim enable on\|off` | `nv set interface <interface-id> router pim state enabled\|disabled` |
| `nv set vrf <vrf-id> router nexthop-tracking <afi> resolved-via-default on\|off` | `nv set vrf <vrf-id> router nexthop-tracking <afi> resolved-via-default enabled\|disabled` |
| `nv set vrf <vrf-id> router ospf area <area-id> range <range-id> suppress on\|off` | `nv set vrf <vrf-id> router ospf area <area-id> range <range-id> suppress enabled\|disabled` |
| `nv set vrf <vrf-id> router ospf default-originate enable on\|off` | `nv set vrf <vrf-id> router ospf default-originate state enabled\|disabled` |
| `nv set vrf <vrf-id> router ospf default-originate always on\|off` | `nv set vrf <vrf-id> router ospf default-originate always enabled\|disabled` |
| `nv set vrf <vrf-id> router ospf max-metric administrative on\|off` | `nv set vrf <vrf-id> router ospf max-metric administrative enabled\|disabled` |
| `nv set vrf <vrf-id> router ospf log adjacency-changes (on\|off\|detail)` | `nv set vrf <vrf-id> router ospf log adjacency-changes (enabled\|disabled\|detail)` |
| `nv set vrf <vrf-id> router ospf redistribute static enable on\|off` | `nv set vrf <vrf-id> router ospf redistribute static state enabled\|disabled` |
| `nv set vrf <vrf-id> router ospf redistribute connected enable on\|off` | `nv set vrf <vrf-id> router ospf redistribute connected state enabled\|disabled` |
| `nv set vrf <vrf-id> router ospf redistribute kernel enable on\|off` | `nv set vrf <vrf-id> router ospf redistribute kernel state enabled\|disabled` |
| `nv set vrf <vrf-id> router ospf redistribute bgp enable on\|off` | `nv set vrf <vrf-id> router ospf redistribute bgp state enabled\|disabled` |
| `nv set vrf <vrf-id> router ospf enable on\|off` | `nv set vrf <vrf-id> router ospf state enabled\|disabled` |
| `nv set vrf <vrf-id> router ospf rfc1583-compatible on\|off` | `nv set vrf <vrf-id> router ospf rfc1583-compatible enabled\|disabled` |
| `nv set vrf <vrf-id> router bgp enable on\|off` | `nv set vrf <vrf-id> router bgp state enabled\|disabled` |
| `nv set interface <interface-id> router ospf authentication enable on\|off` | `nv set interface <interface-id> router ospf authentication state enabled\|disabled` |
| `nv set interface <interface-id> router ospf bfd enable on\|off` | `nv set interface <interface-id> router ospf bfd state enabled\|disabled` |
| `nv set interface <interface-id> router ospf enable on\|off` | `nv set interface <interface-id> router ospf state enabled\|disabled` |
| `nv set interface <interface-id> router ospf mtu-ignore on\|off` | `nv set interface <interface-id> router ospf mtu-ignore enabled\|disabled` |
| `nv set interface <interface-id> router ospf passive on\|off` | `nv set interface <interface-id> router ospf passive enabled\|disabled` |
| `nv set interface <interface-id> router pim bfd enable on\|off` | `nv set interface <interface-id> router pim bfd state enabled\|disabled` |
| `nv set interface <interface-id> router pim address-family ipv4-unicast allow-rp enable on\|off` | `nv set interface <interface-id> router pim address-family ipv4-unicast allow-rp state enabled\|disabled` |
| `nv set interface <interface-id> router pim active-active on\|off` | `nv set interface <interface-id> router pim active-active enabled\|disabled` |
| `nv set vrf <vrf-id> router bgp address-family ipv4-unicast redistribute static enable on\|off` | `nv set vrf <vrf-id> router bgp address-family ipv4-unicast redistribute static state enabled\|disabled` |
| `nv set vrf <vrf-id> router bgp address-family ipv4-unicast redistribute connected enable on\|off` | `nv set vrf <vrf-id> router bgp address-family ipv4-unicast redistribute connected state enabled\|disabled` |
| `nv set vrf <vrf-id> router bgp address-family ipv4-unicast redistribute kernel enable on\|off` | `nv set vrf <vrf-id> router bgp address-family ipv4-unicast redistribute kernel state enabled\|disabled` |
| `nv set vrf <vrf-id> router bgp address-family ipv4-unicast redistribute ospf enable on\|off` | `nv set vrf <vrf-id> router bgp address-family ipv4-unicast redistribute ospf state enabled\|disabled` |
| `nv set vrf <vrf-id> router bgp address-family ipv4-unicast aggregate-route <aggregate-route-id> summary-only on\|off` | `nv set vrf <vrf-id> router bgp address-family ipv4-unicast aggregate-route <aggregate-route-id> summary-only enabled\|disabled` |
| `nv set vrf <vrf-id> router bgp address-family ipv4-unicast aggregate-route <aggregate-route-id> as-set on\|off` | `nv set vrf <vrf-id> router bgp address-family ipv4-unicast aggregate-route <aggregate-route-id> as-set enabled\|disabled` |
| `nv set vrf <vrf-id> router bgp address-family ipv4-unicast route-import from-vrf enable on\|off` | `nv set vrf <vrf-id> router bgp address-family ipv4-unicast route-import from-vrf state enabled\|disabled` |
| `nv set vrf <vrf-id> router bgp address-family ipv4-unicast multipaths compare-cluster-length on\|off` | `nv set vrf <vrf-id> router bgp address-family ipv4-unicast multipaths compare-cluster-length enabled\|disabled` |
| `nv set vrf <vrf-id> router bgp address-family ipv4-unicast route-export to-evpn enable on\|off` | `nv set vrf <vrf-id> router bgp address-family ipv4-unicast route-export to-evpn state enabled\|disabled` |
| `nv set vrf <vrf-id> router bgp address-family ipv4-unicast route-export to-evpn default-route-origination on\|off` | `nv set vrf <vrf-id> router bgp address-family ipv4-unicast route-export to-evpn default-route-origination enabled\|disabled` |
| `nv set vrf <vrf-id> router bgp address-family ipv4-unicast enable on\|off` | `nv set vrf <vrf-id> router bgp address-family ipv4-unicast state enabled\|disabled` |
| `nv set vrf <vrf-id> router bgp address-family ipv6-unicast redistribute static enable on\|off` | `nv set vrf <vrf-id> router bgp address-family ipv6-unicast redistribute static state enabled\|disabled` |
| `nv set vrf <vrf-id> router bgp address-family ipv6-unicast redistribute connected enable on\|off` | `nv set vrf <vrf-id> router bgp address-family ipv6-unicast redistribute connected state enabled\|disabled` |
| `nv set vrf <vrf-id> router bgp address-family ipv6-unicast redistribute kernel enable on\|off` | `nv set vrf <vrf-id> router bgp address-family ipv6-unicast redistribute kernel state enabled\|disabled` |
| `nv set vrf <vrf-id> router bgp address-family ipv6-unicast redistribute ospf6 enable on\|off` | `nv set vrf <vrf-id> router bgp address-family ipv6-unicast redistribute ospf6 state enabled\|disabled` |
| `nv set vrf <vrf-id> router bgp address-family ipv6-unicast aggregate-route <aggregate-route-id> summary-only on\|off` | `nv set vrf <vrf-id> router bgp address-family ipv6-unicast aggregate-route <aggregate-route-id> summary-only enabled\|disabled` |
| `nv set vrf <vrf-id> router bgp address-family ipv6-unicast aggregate-route <aggregate-route-id> as-set on\|off` | `nv set vrf <vrf-id> router bgp address-family ipv6-unicast aggregate-route <aggregate-route-id> as-set enabled\|disabled` |
| `nv set vrf <vrf-id> router bgp address-family ipv6-unicast route-import from-vrf enable on\|off` | `nv set vrf <vrf-id> router bgp address-family ipv6-unicast route-import from-vrf state enabled\|disabled` |
| `nv set vrf <vrf-id> router bgp address-family ipv6-unicast multipaths compare-cluster-length on\|off` | `nv set vrf <vrf-id> router bgp address-family ipv6-unicast multipaths compare-cluster-length enabled\|disabled` |
| `nv set vrf <vrf-id> router bgp address-family ipv6-unicast route-export to-evpn enable on\|off` | `nv set vrf <vrf-id> router bgp address-family ipv6-unicast route-export to-evpn state enabled\|disabled` |
| `nv set vrf <vrf-id> router bgp address-family ipv6-unicast route-export to-evpn default-route-origination on\|off` | `nv set vrf <vrf-id> router bgp address-family ipv6-unicast route-export to-evpn default-route-origination enabled\|disabled` |
| `nv set vrf <vrf-id> router bgp address-family ipv6-unicast enable on\|off` | `nv set vrf <vrf-id> router bgp address-family ipv6-unicast state enabled\|disabled` |
| `nv set vrf <vrf-id> router bgp address-family l2vpn-evpn enable on\|off` | `nv set vrf <vrf-id> router bgp address-family l2vpn-evpn state enabled\|disabled` |
| `nv set vrf <vrf-id> router bgp path-selection aspath compare-lengths on\|off` | `nv set vrf <vrf-id> router bgp path-selection aspath compare-lengths enabled\|disabled` |
| `nv set vrf <vrf-id> router bgp path-selection aspath compare-confed on\|off` | `nv set vrf <vrf-id> router bgp path-selection aspath compare-confed enabled\|disabled` |
| `nv set vrf <vrf-id> router bgp path-selection med compare-always on\|off` | `nv set vrf <vrf-id> router bgp path-selection med compare-always enabled\|disabled` |
| `nv set vrf <vrf-id> router bgp path-selection med compare-deterministic on\|off` | `nv set vrf <vrf-id> router bgp path-selection med compare-deterministic enabled\|disabled` |
| `nv set vrf <vrf-id> router bgp path-selection med compare-confed on\|off` | `nv set vrf <vrf-id> router bgp path-selection med compare-confed enabled\|disabled` |
| `nv set vrf <vrf-id> router bgp path-selection med missing-as-max on\|off` | `nv set vrf <vrf-id> router bgp path-selection med missing-as-max enabled\|disabled` |
| `nv set vrf <vrf-id> router bgp path-selection multipath aspath-ignore on\|off` | `nv set vrf <vrf-id> router bgp path-selection multipath aspath-ignore enabled\|disabled` |
| `nv set vrf <vrf-id> router bgp path-selection multipath generate-asset on\|off` | `nv set vrf <vrf-id> router bgp path-selection multipath generate-asset enabled\|disabled` |
| `nv set vrf <vrf-id> router bgp path-selection routerid-compare on\|off` | `nv set vrf <vrf-id> router bgp path-selection routerid-compare enabled\|disabled` |
| `nv set vrf <vrf-id> router bgp route-reflection enable on\|off` | `nv set vrf <vrf-id> router bgp route-reflection state enabled\|disabled` |
| `nv set vrf <vrf-id> router bgp route-reflection reflect-between-clients on\|off` | `nv set vrf <vrf-id> router bgp route-reflection reflect-between-clients enabled\|disabled` |
| `nv set vrf <vrf-id> router bgp route-reflection outbound-policy on\|off` | `nv set vrf <vrf-id> router bgp route-reflection outbound-policy enabled\|disabled` |
| `nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast route-reflector-client on\|off` | `nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast route-reflector-client enabled\|disabled` |
| `nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast soft-reconfiguration on\|off` | `nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast soft-reconfiguration enabled\|disabled` |
| `nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast route-reflector-client on\|off` | `nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast route-reflector-client enabled\|disabled` |
| `nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast soft-reconfiguration on\|off` | `nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast soft-reconfiguration enabled\|disabled` |
| `nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family l2vpn-evpn route-reflector-client on\|off` | `nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family l2vpn-evpn route-reflector-client enabled\|disabled` |
| `nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family l2vpn-evpn soft-reconfiguration on\|off` | `nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family l2vpn-evpn soft-reconfiguration enabled\|disabled` |
| `nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast route-reflector-client on\|off` | `nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast route-reflector-client enabled\|disabled` |
| `nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast soft-reconfiguration on\|off` | `nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast soft-reconfiguration enabled\|disabled` |
| `nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast route-reflector-client on\|off` | `nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast route-reflector-client enabled\|disabled` |
| `nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast soft-reconfiguration on\|off` | `nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast soft-reconfiguration enabled\|disabled` |
| `nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family l2vpn-evpn route-reflector-client on\|off` | `nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family l2vpn-evpn route-reflector-client enabled\|disabled` |
| `nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family l2vpn-evpn soft-reconfiguration on\|off` | `nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family l2vpn-evpn soft-reconfiguration enabled\|disabled` |
| `nv set vrf <vrf-id> router bgp neighbor <neighbor-id> local-as enable on\|off` | `nv set vrf <vrf-id> router bgp neighbor <neighbor-id> local-as state enabled\|disabled` |
| `nv set vrf <vrf-id> router bgp neighbor <neighbor-id> local-as prepend on\|off` | `nv set vrf <vrf-id> router bgp neighbor <neighbor-id> local-as prepend enabled\|disabled` |
| `nv set vrf <vrf-id> router bgp neighbor <neighbor-id> local-as replace on\|off` | `nv set vrf <vrf-id> router bgp neighbor <neighbor-id> local-as replace enabled\|disabled` |
| `nv set vrf <vrf-id> router bgp neighbor <neighbor-id> bfd enable on\|off` | `nv set vrf <vrf-id> router bgp neighbor <neighbor-id> bfd state enabled\|disabled` |
| `nv set vrf <vrf-id> router bgp neighbor <neighbor-id> ttl-security enable on\|off` | `nv set vrf <vrf-id> router bgp neighbor <neighbor-id> ttl-security state enabled\|disabled` |
| `nv set vrf <vrf-id> router bgp peer-group <peer-group-id> bfd enable on\|off` | `nv set vrf <vrf-id> router bgp peer-group <peer-group-id> bfd state enabled\|disabled` |
| `nv set vrf <vrf-id> router bgp peer-group <peer-group-id> ttl-security enable on\|off` | `nv set vrf <vrf-id> router bgp peer-group <peer-group-id> ttl-security state enabled\|disabled` |
| `nv set vrf <vrf-id> router bgp peer-group <peer-group-id> local-as enable on\|off` | `nv set vrf <vrf-id> router bgp peer-group <peer-group-id> local-as state enabled\|disabled` |
| `nv set vrf <vrf-id> router bgp peer-group <peer-group-id> local-as prepend on\|off` | `nv set vrf <vrf-id> router bgp peer-group <peer-group-id> local-as prepend enabled\|disabled` |
| `nv set vrf <vrf-id> router bgp peer-group <peer-group-id> local-as replace on\|off` | `nv set vrf <vrf-id> router bgp peer-group <peer-group-id> local-as replace enabled\|disabled` |
| `nv set vrf <vrf-id> router bgp peer-group <peer-group-id> enforce-first-as on\|off` | `nv set vrf <vrf-id> router bgp peer-group <peer-group-id> enforce-first-as enabled\|disabled` |
| `nv set vrf <vrf-id> router bgp peer-group <peer-group-id> passive-mode on\|off` | `nv set vrf <vrf-id> router bgp peer-group <peer-group-id> passive-mode enabled\|disabled` |
| `nv set vrf <vrf-id> router bgp peer-group <peer-group-id> nexthop-connected-check on\|off` | `nv set vrf <vrf-id> router bgp peer-group <peer-group-id> nexthop-connected-check enabled\|disabled` |
| `nv set vrf <vrf-id> router bgp peer-group <peer-group-id> shutdown on\|off` | `nv set vrf <vrf-id> router bgp peer-group <peer-group-id> shutdown enabled\|disabled` |
| `nv set vrf <vrf-id> router bgp neighbor <neighbor-id> enforce-first-as on\|off` | `nv set vrf <vrf-id> router bgp neighbor <neighbor-id> enforce-first-as enabled\|disabled` |
| `nv set vrf <vrf-id> router bgp neighbor <neighbor-id> passive-mode on\|off` | `nv set vrf <vrf-id> router bgp neighbor <neighbor-id> passive-mode enabled\|disabled` |
| `nv set vrf <vrf-id> router bgp neighbor <neighbor-id> nexthop-connected-check on\|off` | `nv set vrf <vrf-id> router bgp neighbor <neighbor-id> nexthop-connected-check enabled\|disabled` |
| `nv set vrf <vrf-id> router bgp neighbor <neighbor-id> shutdown on\|off` | `nv set vrf <vrf-id> router bgp neighbor <neighbor-id> shutdown enabled\|disabled` |
| `nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast conditional-advertise enable on\|off` | `nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast conditional-advertise state enabled\|disabled` |
| `nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast conditional-advertise enable on\|off` | `nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast conditional-advertise state enabled\|disabled` |
| `nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast conditional-advertise enable on\|off` | `nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast conditional-advertise state enabled\|disabled` |
| `nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast conditional-advertise enable on\|off` | `nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast conditional-advertise state enabled\|disabled` |
| `nv set vrf <vrf-id> evpn prefix-routes-only on\|off` | `nv set vrf <vrf-id> evpn prefix-routes-only enabled\|disabled` |
| `nv set interface <interface-id> evpn multihoming segment enable on\|off` | `nv set interface <interface-id> evpn multihoming segment state enabled\|disabled` |
| `nv set interface <interface-id> evpn multihoming uplink on\|off` | `nv set interface <interface-id> evpn multihoming uplink enabled\|disabled` |
| `nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast community-advertise regular on\|off` | `nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast community-advertise regular enabled\|disabled` |
| `nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast community-advertise extended on\|off` | `nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast community-advertise extended enabled\|disabled` |
| `nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast community-advertise large on\|off` | `nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast community-advertise large enabled\|disabled` |
| `nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast attribute-mod aspath on\|off` | `nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast attribute-mod aspath enabled\|disabled` |
| `nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast attribute-mod med on\|off` | `nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast attribute-mod med enabled\|disabled` |
| `nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast attribute-mod nexthop on\|off` | `nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast attribute-mod nexthop enabled\|disabled` |
| `nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast aspath allow-my-asn enable on\|off` | `nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast aspath allow-my-asn stateenabled\|disabled` |
| `nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast aspath allow-my-asn origin on\|off` | `nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast aspath allow-my-asn origin enabled\|disabled` |
| `nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast aspath replace-peer-as on\|off` | `nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast aspath replace-peer-as enabled\|disabled` |
| `nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast prefix-limits inbound warning-only on\|off` | `nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast prefix-limits inbound warning-only enabled\|disabled` |
| `nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast default-route-origination enable on\|off` | `nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast default-route-origination state enabled\|disabled` |
| `nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast aspath allow-my-asn enable on\|off` | `nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast aspath allow-my-asn state enabled\|disabled` |
| `nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast aspath allow-my-asn origin on\|off` | `nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast aspath allow-my-asn origin enabled\|disabled` |
| `nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast aspath replace-peer-as on\|off` | `nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast aspath replace-peer-as enabled\|disabled` |
| `nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast prefix-limits inbound warning-only on\|off` | `nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast prefix-limits inbound warning-only enabled\|disabled` |
| `nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast default-route-origination enable on\|off` | `nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast default-route-origination stateenabled\|disabled` |
| `nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast community-advertise regular on\|off` | `nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast community-advertise regular enabled\|disabled` |
| `nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast community-advertise extended on\|off` | `nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast community-advertise extended enabled\|disabled` |
| `nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast community-advertise large on\|off` | `nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast community-advertise large enabled\|disabled` |
| `nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast attribute-mod aspath on\|off` | `nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast attribute-mod aspath enabled\|disabled` |
| `nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast attribute-mod med on\|off` | `nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast attribute-mod med enabled\|disabled` |
| `nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast attribute-mod nexthop on\|off` | `nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast attribute-mod nexthop enabled\|disabled` |
| `nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family l2vpn-evpn attribute-mod aspath on\|off` | `nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family l2vpn-evpn attribute-mod aspath enabled\|disabled` |
| `nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family l2vpn-evpn attribute-mod med on\|off` | `nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family l2vpn-evpn attribute-mod med enabled\|disabled` |
| `nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family l2vpn-evpn attribute-mod nexthop on\|off` | `nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family l2vpn-evpn attribute-mod nexthop enabled\|disabled` |
| `nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family l2vpn-evpn aspath allow-my-asn enable on\|off` | `nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family l2vpn-evpn aspath allow-my-asn stateenabled\|disabled` |
| `nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family l2vpn-evpn aspath allow-my-asn origin on\|off` | `nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family l2vpn-evpn aspath allow-my-asn origin enabled\|disabled` |
| `nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family l2vpn-evpn aspath replace-peer-as on\|off` | `nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family l2vpn-evpn aspath replace-peer-as enabled\|disabled` |
| `nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast attribute-mod aspath on\|off` | `nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast attribute-mod aspath enabled\|disabled` |
| `nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast attribute-mod med on\|off` | `nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast attribute-mod med enabled\|disabled` |
| `nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast attribute-mod nexthop on\|off` | `nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast attribute-mod nexthop enabled\|disabled` |
| `nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast aspath allow-my-asn enable on\|off` | `nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast aspath allow-my-asn stateenabled\|disabled` |
| `nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast aspath allow-my-asn origin on\|off` | `nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast aspath allow-my-asn origin enabled\|disabled` |
| `nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast aspath replace-peer-as on\|off` | `nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast aspath replace-peer-as enabled\|disabled` |
| `nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast prefix-limits inbound warning-only on\|off` | `nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast prefix-limits inbound warning-only enabled\|disabled` |
| `nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast default-route-origination enable on\|off` | `nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast default-route-origination stateenabled\|disabled` |
| `nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast community-advertise regular on\|off` | `nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast community-advertise regular enabled\|disabled` |
| `nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast community-advertise extended on\|off` | `nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast community-advertise extended enabled\|disabled` |
| `nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast community-advertise large on\|off` | `nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast community-advertise large enabled\|disabled` |
| `nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast enable on\|off` | `nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast stateenabled\|disabled` |
| `nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast attribute-mod aspath on\|off` | `nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast attribute-mod aspath enabled\|disabled` |
| `nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast attribute-mod med on\|off` | `nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast attribute-mod med enabled\|disabled` |
| `nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast attribute-mod nexthop on\|off` | `nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast attribute-mod nexthop enabled\|disabled` |
| `nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast aspath allow-my-asn enable on\|off` | `nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast aspath allow-my-asn stateenabled\|disabled` |
| `nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast aspath allow-my-asn origin on\|off` | `nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast aspath allow-my-asn origin enabled\|disabled` |
| `nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast aspath replace-peer-as on\|off` | `nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast aspath replace-peer-as enabled\|disabled` |
| `nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast prefix-limits inbound warning-only on\|off` | `nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast prefix-limits inbound warning-only enabled\|disabled` |
| `nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast default-route-origination enable on\|off` | `nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast default-route-origination stateenabled\|disabled` |
| `nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast community-advertise regular on\|off` | `nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast community-advertise regular enabled\|disabled` |
| `nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast community-advertise extended on\|off` | `nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast community-advertise extended enabled\|disabled` |
| `nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast community-advertise large on\|off` | `nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast community-advertise large enabled\|disabled` |
| `nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast enable on\|off` | `nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast stateenabled\|disabled` |
| `nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family l2vpn-evpn attribute-mod aspath on\|off` | `nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family l2vpn-evpn attribute-mod aspath enabled\|disabled` |
| `nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family l2vpn-evpn attribute-mod med on\|off` | `nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family l2vpn-evpn attribute-mod med enabled\|disabled` |
| `nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family l2vpn-evpn attribute-mod nexthop on\|off` | `nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family l2vpn-evpn attribute-mod nexthop enabled\|disabled` |
| `nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family l2vpn-evpn aspath allow-my-asn enable on\|off` | `nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family l2vpn-evpn aspath allow-my-asn stateenabled\|disabled` |
| `nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family l2vpn-evpn aspath allow-my-asn origin on\|off` | `nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family l2vpn-evpn aspath allow-my-asn origin enabled\|disabled` |
| `nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family l2vpn-evpn aspath replace-peer-as on\|off` | `nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family l2vpn-evpn aspath replace-peer-as enabled\|disabled` |
| `nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family l2vpn-evpn prefix-limits inbound warning-only on\|off` | `nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family l2vpn-evpn prefix-limits inbound warning-only enabled\|disabled` |
| `nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family l2vpn-evpn enable on\|off` | `nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family l2vpn-evpn state enabled\|disabled` |
| `nv set interface <interface-id> router adaptive-routing enable on\|off` | `nv set interface <interface-id> router adaptive-routing state enabled\|disabled` |
| `nv set router adaptive-routing enable on\|off` | `nv set router adaptive-routing state enabled\|disabled` |
| `nv set nve vxlan enable on\|off` | `nv set nve vxlan state enabled\|disabled` |
| `nv set vrf <vrf-id> router bgp peer-group <peer-group-id> capabilities extended-nexthop (on\|off\|auto)` | `nv set vrf <vrf-id> router bgp peer-group <peer-group-id> capabilities extended-nexthop (enabled\|disabled\|auto)` |
| `nv set vrf <vrf-id> router bgp neighbor <neighbor-id> capabilities extended-nexthop (on\|off\|auto)` | `nv set vrf <vrf-id> router bgp neighbor <neighbor-id> capabilities extended-nexthop (enabled\|disabled\|auto)` |
| `nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast enable on\|off` | `nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast state enabled\|disabled` |
| `nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast enable on\|off` | `nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast  state enabled\|disabled` |
| `nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family l2vpn-evpn prefix-limits inbound warning-only on\|off` | `nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family l2vpn-evpn prefix-limits inbound warning-only enabled\|disabled` |
| `nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family l2vpn-evpn enable on\|off` | `nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family l2vpn-evpn  state enabled\|disabled` |
| `nv set vrf <vrf-id> evpn enable on\|off` | `nv set vrf <vrf-id> evpn  state enabled\|disabled` |
| `nv set vrf <vrf-id> router bgp neighbor <neighbor-id> enable on\|off` | `nv set vrf <vrf-id> router bgp neighbor <neighbor-id>  state enabled\|disabled` |
| `nv set vrf <vrf-id> router bgp neighbor <neighbor-id> graceful-shutdown on\|off` | `nv set vrf <vrf-id> router bgp neighbor <neighbor-id> graceful-shutdown  enabled\|disabled` |
| `nv set vrf <vrf-id> router bgp peer-group <peer-group-id> graceful-shutdown on\|off` | `nv set vrf <vrf-id> router bgp peer-group <peer-group-id> graceful-shutdown  enabled\|disabled` |
| `nv set interface <interface-id> ip vrrp virtual-router <virtual-router-id> preempt (on\|off\|auto)` | `nv set interface <interface-id> ip vrrp virtual-router <virtual-router-id> preempt (enabled\|disabled\|auto)` |
| `nv set interface <interface-id> ip neighbor-discovery prefix <ipv6-prefix-id> off-link on\|off` | `nv set interface <interface-id> ip neighbor-discovery prefix <ipv6-prefix-id> off-link enabled\|disabled` |
| `nv set interface <interface-id> ip neighbor-discovery router-advertisement interval-option on\|off` | `nv set interface <interface-id> ip neighbor-discovery router-advertisement interval-option enabled\|disabled` |
| `nv set interface <interface-id> ip neighbor-discovery router-advertisement fast-retransmit on\|off` | `nv set interface <interface-id> ip neighbor-discovery router-advertisement fast-retransmitenabled\|disabled` |
| `nv set interface <interface-id> ip neighbor-discovery home-agent enable on\|off` | `nv set interface <interface-id> ip neighbor-discovery home-agent state enabled\|disabled` |
| `nv set interface <interface-id> ip neighbor-discovery prefix <ipv6-prefix-id> router-address on\|off` | `nv set interface <interface-id> ip neighbor-discovery prefix <ipv6-prefix-id> router-address enabled\|disabled` |
| `nv set interface <interface-id> ip neighbor-discovery prefix <ipv6-prefix-id> autoconfig on\|off` | `nv set interface <interface-id> ip neighbor-discovery prefix <ipv6-prefix-id> autoconfigenabled\|disabled` |
| `nv set interface <interface-id> ip vrrp enable on\|off` | `nv set interface <interface-id> ip vrrp  state enabled\|disabled` |
| `nv set interface <interface-id> ip neighbor-discovery enable on\|off` | `nv set interface <interface-id> ip neighbor-discovery state enabled\|disabled` |
| `nv set interface <interface-id> ip vrr enable on\|off` | `nv set interface <interface-id> ip vrr  state enabled\|disabled` |
| `nv set interface <interface-id> ip neighbor-discovery router-advertisement enable on\|off` | `nv set interface <interface-id> ip neighbor-discovery router-advertisement  state enabled\|disabled` |
| `nv set interface <interface-id> ip neighbor-discovery router-advertisement other-config on\|off` | `nv set interface <interface-id> ip neighbor-discovery router-advertisement other-config enabled\|disabled` |
| `nv set interface <interface-id> ip neighbor-discovery router-advertisement managed-config on\|off` | `nv set interface <interface-id> ip neighbor-discovery router-advertisement managed-config enabled\|disabled` |
| `nv set interface <interface-id> ip igmp enable on\|off` | `nv set interface <interface-id> ip igmp state enabled\|disabled` |
| `nv set interface <interface-id> ip vrr enable on\|off` | `nv set interface <interface-id> ip vrr state enabled\|disabled` |
| `nv set interface <interface-id> ip vrr state (down\|up)` | `nv set interface <interface-id> ip vrr vrr-state (down\|up)` |

{{< /tab >}}
{{< /tabs >}}

## Changes to Command Output

The output for the following commands has changed in Cumulus Linux 5.15.

{{< tabs "828 ">}}
{{< tab "Platform">}}

```
nv show platform asic
```

{{< /tab >}}
{{< tab "Power Supply ">}}

```
nv show system health
```

{{< /tab >}}
{{< tab "Timestamp Format">}}

```
nv show router nexthop rib
nv show router nexthop rib <nhg-id>
nv show vrf <vrf-id> router rib <afi>
nv show vrf <vrf-id> router rib <afi> route
nv show vrf <vrf-id> router rib <afi> route <route-id> route-entry <route-entry-id>
nv show vrf <vrf-id> router bgp nexthop <afi> ip-address <ip-address-id>
nv show vrf <vrf-id> router bgp address-family ipv4-unicast route <route-id>
nv show vrf <vrf-id> router bgp address-family ipv4-unicast route <route-id> path
nv show vrf <vrf-id> router bgp address-family ipv4-unicast route <route-id> path <path-id>
nv show vrf <vrf-id> router bgp address-family ipv6-unicast route <route-id>
nv show vrf <vrf-id> router bgp address-family ipv6-unicast route <route-id> path
nv show vrf <vrf-id> router bgp address-family ipv6-unicast route <route-id> path <path-id>
nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast advertised-routes <route-id>
nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast advertised-routes <route-id> path
nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast advertised-routes <route-id> path <path-id>
nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast advertised-routes <route-id>
nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast advertised-routes <route-id> path
nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast advertised-routes <route-id> path <path-id>
nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast received-routes <route-id>
nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast received-routes <route-id> path
nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast received-routes <route-id> path <path-id>
nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast received-routes <route-id>
nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast received-routes <route-id> path
nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast received-routes <route-id> path <path-id>
nv show vrf <vrf-id> router bgp address-family ipv4-unicast update-group
nv show vrf <vrf-id> router bgp address-family ipv4-unicast update-group <group-id>
nv show vrf <vrf-id> router bgp address-family ipv4-unicast update-group <group-id> sub-group
nv show vrf <vrf-id> router bgp address-family ipv6-unicast update-group
nv show vrf <vrf-id> router bgp address-family ipv6-unicast update-group <group-id>
nv show vrf <vrf-id> router bgp address-family ipv6-unicast update-group <group-id> sub-group
nv show vrf <vrf-id> router bgp address-family l2vpn-evpn update-group
nv show vrf <vrf-id> router bgp address-family l2vpn-evpn update-group <group-id>
nv show vrf <vrf-id> router bgp address-family l2vpn-evpn update-group <group-id> sub-group
nv show vrf <vrf-id> router ospf neighbor <nbr-id> interface <interface-id> local-ip
nv show vrf <vrf-id> router ospf neighbor <nbr-id> interface <interface-id> local-ip <address-id>
nv show interface <interface-id> ip igmp
nv show interface <interface-id> ip igmp group
nv show interface <interface-id> ip igmp group <group-id>
nv show router graceful-restart
```

{{< /tab >}}
{{< tab "Message of the Day ">}}

```
nv show system message
```

{{< /tab >}}
{{< tab "CPU ">}}

```
nv show system cpu
```

{{< /tab >}}
{{< tab "Memory ">}}

```
nv show system memory
```

{{< /tab >}}
{{< tab "Reboot ">}}

```
nv show system reboot
nv show system forwarding
```

{{< /tab >}}
{{< tab "ACL ">}}

```
nv show interface <interface-id> acl <acl-id>
nv show interface <interface-id> acl <acl-id> inbound
nv show interface <interface-id> acl <acl-id> inbound control-plane
nv show interface <interface-id> acl <acl-id> outbound
nv show interface <interface-id> acl <acl-id> outbound control-plane
nv show interface <interface-id> acl <acl-id> statistics
nv show system control-plane acl <acl-id>
nv show system control-plane acl <acl-id> statistics
```

{{< /tab >}}
{{< tab "Tech Support ">}}

```
nv show system tech-support
nv show system tech-support files
```

{{< /tab >}}
{{< tab "Operation Support">}}

```
nv show interface <interface-id> link flap-protection
nv show interface <interface-id> storm-control
nv show system acl
nv show system link flap-protection
nv show system counter polling-interval
nv show system forwarding programming
nv show system forwarding ecmp-weight-normalisation
nv show vrf <vrf-id> router bgp neighbor <neighbor-id>
nv show vrf <vrf-id> evpn
```

{{< /tab >}}
{{< tab "On/Off ">}}

```
nv show interface <interface-id> ip igmp
nv show interface <interface-id> synce
nv show interface <interface-id> ip ipv4
nv show interface <interface-id> link
nv show interface <interface-id> ptp
nv show interface <interface-id> ip
nv show system global svi-force-up
nv show system snmp-server trap-destination localhost username <username> auth-md5 <authmd5-id> encrypt-des encryptdes engine-id <engineid>
nv show system snmp-server trap-destination localhost username <username> auth-md5 <authmd5-id> encrypt-aes encryptdes engine-id <engineid>
nv show system snmp-server trap-destination localhost username <username> auth-md5 <authmd-5id> engine-id <engineid>
nv show system aaa tacacs authentication
nv show system snmp-server trap-destination localhost vrf mgmt username <username> auth-sha <authsha-id> encrypt-des encryptid engine-id <engine-id>
nv show system snmp-server trap-destination localhost username <username> auth-sha auth-idtest encrypt-aes <encrypt-id> engine-id <engine-id>
nv show system snmp-server trap-destination localhost vrf mgmt username <username> auth-md5 <auth-id> engine-id <engine-id>
nv show system snmp-server trap-destination localhost username <username> auth-sha <auth-id> encrypt-aes <encrypt-id> engine-id <engine-id>
nv show system snmp-server trap-destination localhost-v6 vrf mgmt username <username> auth-sha <authsha-id> encrypt-aes <encript-id> engine-id <engine-id>
nv show system snmp-server trap-destination localhost-v6 username <username> auth-sha <authsha-id> engine-id <engine-id>
nv show system snmp-server trap-destination localhost-v6 vrf mgmt username <username> auth-sha <auth-id> engine-id <engine-id>
nv show system snmp-server trap-destination localhost vrf <vrf-id> username <username> auth-md5 <auth-id> encrypt-des <encrypt-id> engine-id <engine-id>
nv show system snmp-server trap-destination localhost username <username> auth-md5 <auth-id> encrypt-aes <encrypt-id> engine-id <engine-id>
nv show system telemetry
nv show system wjh
nv show service ptp <id> profile
nv show service ptp <id>
nv show vrf <vrf-id> ptp
nv show nve vxlan flooding
nv show bridge domain <bridge-id> multicast
nv show bridge domain <bridge-id> multicast snooping querier
nv show bridge domain <bridge-id> vlan <vlan-id> ptp
nv show bridge domain <bridge-id> vlan <vlan-id> vni <vni-id> flooding
nv show bridge domain <bridge-id> svi-force-up
nv show interface <interface-id> lldp
nv show interface <bond-id> bond mlag
nv show interface <interface-id> port-security
nv show interface <bond-id> bond
nv show interface <interface-id> link flap-protection
nv show interface <interface-id> telemetry bw-gauge
nv show interface <interface-id> bridge domain <bridge-id> stp
nv show interface <interface-id> bridge domain <bridge-id>
nv show system control-plane trap
nv show system port-mirror session <session-id> erspan
nv show system port-mirror session <session-id> erspan truncate
nv show system port-mirror session <session-id> span
nv show system port-mirror session <session-id> span truncate
nv show system forwarding ecmp-hash
nv show system forwarding lag-hash
nv show system lldp
nv show system control-plane policer lacp
nv show service dhcp-server6 mgmt pool
nv show service dhcp-relay mgmt agent
nv show service dhcp-server mgmt pool <pool-id>
nv show service dhcp-relay mgmt agent use-pif-circuit-id
nv show router adaptive-routing
nv show nve vxlan
nv show bridge domain <domain-id> vlan <vlan-id> vni <vni-id>
nv show qos roce
nv show mlag
```

{{< /tab >}}
{{< /tabs >}}

## Deprecated NVUE Commands

The following NVUE commands are deprecated in Cumulus Linux 5.15.

{{< tabs "TabID857 ">}}
{{< tab "nv set ">}}

```
nv set system message post-logout <value>
nv set system ssh-server strict
nv set system reboot mode
nv set interface <interface-id> router ospf bfd enable
nv set interface <interface-id> router ospf bfd detect-multiplier
nv set interface <interface-id> router ospf bfd min-receive-interval 
nv set interface <interface-id> router ospf bfd min-transmit-interval
nv set interface <interface-id> router pim bfd enable
nv set interface <interface-id> router pim bfd detect-multiplier
nv set interface <interface-id> router pim bfd min-receive-interval
nv set interface <interface-id> router pim bfd min-transmit-interval
nv set vrf <vrf-id> router bgp peer-group <peer-group-id> bfd enable
nv set vrf <vrf-id> router bgp peer-group <peer-group-id> bfd detect-multiplier
nv set vrf <vrf-id> router bgp peer-group <peer-group-id> bfd min-rx-interval
nv set vrf <vrf-id> router bgp peer-group <peer-group-id> bfd min-tx-interval
nv set vrf <vrf-id> router bgp neighbor <neighbor-id> bfd enable
nv set vrf <vrf-id> router bgp neighbor <neighbor-id> bfd detect-multiplier
nv set vrf <vrf-id> router bgp neighbor <neighbor-id> bfd min-rx-interval
nv set vrf <vrf-id> router bgp neighbor <neighbor-id> bfd min-tx-interval
```

{{< /tab >}}
{{< tab "nv unset ">}}

```
nv unset system reboot
nv unset interface <interface-id> router ospf bfd enable 
nv unset interface <interface-id> router ospf bfd detect-multiplier 
nv unset interface <interface-id> router ospf bfd min-receive-interval 
nv unset interface <interface-id> router ospf bfd min-transmit-interval 
nv unset interface <interface-id> router pim bfd 
nv unset interface <interface-id> router pim bfd enable 
nv unset interface <interface-id> router pim bfd detect-multiplier 
nv unset interface <interface-id> router pim bfd min-receive-interval 
nv unset interface <interface-id> router pim bfd min-transmit-interval 
nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> bfd enable 
nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> bfd detect-multiplier 
nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> bfd min-rx-interval 
nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> bfd min-tx-interval 
nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> bfd enable 
nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> bfd detect-multiplier 
nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> bfd min-rx-interval 
nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> bfd min-tx-interval 
```

{{< /tab >}}
{{< tab "nv action ">}}

```
nv action power-cycle system
```

{{< /tab >}}
{{< /tabs >}}

## All New NVUE Commands

The following NVUE commands are new in Cumulus Linux 5.15.

For descriptions and examples of all NVUE commands, refer to the [NVUE Command Reference]({{<ref "/nvue-reference" >}}) for Cumulus Linux.

{{< tabs "TabID1083 ">}}
{{< tab "nv show ">}}

```
nv show interface <interface-id> latency-measurement
nv show interface <interface-id> latency-measurement traffic-class
nv show interface <interface-id> latency-measurement traffic-class <traffic-class>
nv show interface <interface-id> latency-measurement traffic-class <traffic-class> protocol <protocol>
nv show interface <interface-id> link phy health native 
nv show interface <interface-id> link phy health histogram 
nv show interface <interface-id> link phy health histogram native
nv show interface dot1x-summary
nv show interface dot1x-ipv6-summary
nv show interface dot1x-counters
nv show system aaa authentication restrictions
nv show system control-plane acl <acl-id> inbound 
nv show system control-plane acl <acl-id> outbound
nv show system dns search
nv show system dns search <dns-search-id>
nv show system docker
nv show system docker image
nv show system docker container
nv show system docker container stats
nv show system docker engine
nv show system forwarding packet-trim
nv show system forwarding packet-trim counters
nv show system gnmi-server status gnoi-rpc
nv show system health history 
nv show system health history files 
nv show system health history files <file-name>
nv show system ntp brief
nv show system ntp server 
nv show system ntp listen 
nv show system ntp listen <interface-id  
nv show system telemetry congestion-event
nv show system telemetry latency-measurement
nv show system telemetry latency-measurement export
nv show interface <interface> telemetry congestion-event
nv show system serial-console
nv show vrf <vrf-id> dhcp-server-v4 static-host <host-id> ifname
nv show vrf <vrf-id> dhcp-server-v4 static-host <host-id> ifname <interface-name>
nv show vrf <vrf-id> dhcp-server-v6 static-host <host-id> ifname
nv show vrf <vrf-id> dhcp-server-v6 static-host <host-id> ifname <interface-name>
nv show interface <interface-id> ipv4 dhcp-client 
nv show interface <interface-id> ipv4 dhcp-client lease
nv show interface <interface-id> ipv6 dhcp-client 
nv show interface <interface-id> ipv6 dhcp-client lease
nv show router bfd profile <profile-name>  
nv show vrf <vrf-id> router bgp peer-group <peer-group-id> bfd 
nv show vrf <vrf-id> router bgp neighbor <neighbor-id> bfd 
nv show vrf <vrf-id> router bfd peers 
nv show vrf <vrf-id> router bfd peers <session-id> 
nv show interface <interface-id> router ospf bfd  
nv show interface <interface-id> router pim bfd  
nv show vrf <vrf-id> router static <ipv4-prefix> via <ipv4> bfd 
nv show vrf <vrf-id> router static <ipv4-prefix> distance <integer> via <ipv4> bfd
```

{{< /tab >}}
{{< tab "nv set ">}}

```
nv set interface <interface-id> dot1x ipv6-profile <profile-name>
nv set interface <interface-id> dot1x ipv6-profile <profile-name>
nv set interface <interface-id> ipv4 dhcp-client set-hostname (enabled|disabled) 
nv set interface <interface-id> ipv6 dhcp-client set-hostname (enabled|disabled) 
nv set interface <interface-id> latency-measurement traffic-class <traffic-class> protocol <protocol-id> dscp <dscp>
nv set router bfd state
nv set router bfd profile <profile-name>
nv set router bfd profile <profile-name> detect-multiplier
nv set router bfd profile <profile-name> min-rx-interval 
nv set router bfd profile <profile-name> min-tx-interval
nv set router bfd profile <profile-name> shutdown
nv set router bfd profile <profile-name> passive-mode 
nv set router bfd profile <profile-name> minimum-ttl
nv set interface <interface-id> router ospf bfd profile <profile-name> 
nv set interface <interface-id> router pim bfd profile <profile-name>
nv set vrf <vrf-id> router bgp peer-group <peer-group-id> bfd profile <profile-name> 
nv set vrf <vrf-id> router bgp neighbor <neighbor-id> bfd profile <profile-name>
nv set vrf <vrf-id> router static <ipv4-prefix> distance <integer> via <ipv4> bfd profile <profile-name>
nv set vrf <vrf-id> router static <ipv4-prefix> distance <integer> via <ipv4> bfd multi-hop
nv set vrf <vrf-id> router static <ipv4-prefix> distance <integer> via <ipv4> bfd source
nv set vrf <vrf-id> router static <ipv4-prefix> via <ipv4> bfd profile <profile-name> 
nv set vrf <vrf-id> router static <ipv4-prefix> via <ipv4> bfd multi-hop
nv set vrf <vrf-id> router static <ipv4-prefix> via <ipv4> bfd source 
nv set system aaa authentication restrictions lockout-state
nv set system aaa authentication restrictions lockout-attempts
nv set system aaa authentication restrictions fail-delay
nv set system aaa authentication restrictions lockout-reattempt
nv set system dns server <dns-server-ip> vrf <vrf-id> 
nv set system dns server <dns-server-id> priority <integer> 
nv set system dns domain <dns-domain-def> 
nv set system docker state
nv set system docker vrf <vrf-name>
nv set system dot1x dynamic-ipv6-multi-tenant state
nv set system dot1x ipv6-profile <profile-id>
nv set system dot1x ipv6-profile <profile-id> property
nv set system dot1x ipv6-profile <profile-id> route-map
nv set system ntp server <server-id> state (enabled|disabled) 
nv set system ntp server <server-id> version (3|4) 
nv set system ntp server <server-id> association-type (server|pool) 
nv set system ntp state (enabled|disabled) 
nv set system ntp vrf <vrf-name> 
nv set system serial-console sysrq-capabilities <arg> 
nv set system security encryption folder-encrypt storage
nv set system security encryption folder-encrypt encrypted-folder
nv set system ssh-server ciphers
nv set system ssh-server macs
nv set system ssh-server kex-algorithms
nv set system ssh-server pubkey-accepted-algorithms 
nv set system ssh-server host-key-algorithms
nv set system syslog selector ifreload
nv set system syslog selector ifreload filter
nv set system syslog selector ifreload program-name
nv set system telemetry congestion-event export state
nv set system telemetry congestion-event throttle-duration
nv set interface <interface-id> telemetry congestion-event egress-buffer traffic-class <traffic-class> buffer-threshold
nv set system telemetry hft sample-interval-usec
nv set system telemetry hft counter
nv set system telemetry hft egress-buffer
nv set system telemetry hft duration
nv set interface <interface-id> telemetry hft state
nv set system telemetry hft export state
nv set system telemetry stats-group <name> hft export state
nv set system telemetry latency-measurement export state
nv set system telemetry stats-group <name> latency-measurement export state
nv set system telemetry latency-measurement state
nv set system telemetry latency-measurement sample-interval
nv set system forwarding resource-mode 
```

{{< /tab >}}
{{< tab "nv action ">}}

```
nv action clear system aaa authentication restrictions user <user-id>
nv action clear system aaa authentication restrictions
nv action enable system security encryption folder-encrypt password <passsword>
nv action enable system security encryption folder-encrypt force
nv action reboot system
nv action release interface <interface-id> ipv4 dhcp-client
nv action release interface <interface-id> ipv6 dhcp-client
nv action renew interface <interface-id> ipv4 dhcp-client
nv action renew interface <interface-id> ipv6 dhcp-client
nv action delete system health history files <file-name>
nv action upload system health history files <file-name> <remote-url> 
nv action pull system docker image
nv action remove system docker image
nv action remove system docker container <container-id>
nv action run system docker container <container-id> image <image>
nv action stop system docker container <container-id>
```

{{< /tab >}}
{{< /tabs >}}
