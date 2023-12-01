---
title: Port Security
author: NVIDIA
weight: 380
toc: 3
---
Port security is a layer 2 traffic control feature that enables you to limit port access to:
- A specific number of MAC addresses.
- Specific MAC addresses so that the port does not forward ingress traffic from undefined source addresses.
- The first learned MAC address on the port (sticky MAC) so that the device with that MAC address has full bandwidth. You can provide a timeout so that the MAC address on that port no longer has access after a certain time.

You can configure what action to take when there is a port security violation (drop packets or put the port into ADMIN down state) and add a timeout for the action to take effect.

{{%notice note%}}
Port security supports layer 2 interfaces in trunk or access mode but **not** interfaces in a bond.
{{%/notice%}}

## Configure Port Security

To configure port security:

{{< tabs "TabID22 ">}}
{{< tab "NVUE Commands ">}}

To enable security on a port, run the `nv set interface <interface> port-security enable on` command:

```
cumulus@switch:~$ nv set interface swp1 port-security enable on
cumulus@switch:~$ nv config apply
```

You can disable port security on an interface with the `nv set interface <interface> port-security enable off` command

To configure the maximum number of MAC addresses allowed to access the port, run the `nv set interface <interface> port-security mac-limit` command. You can specify a value between 1 and 512. The default value is 32.

```
cumulus@switch:~$ nv set interface swp1 port-security mac-limit 100
cumulus@switch:~$ nv config apply 
```

To configure specific MAC addresses allowed to access the port, run the `nv set interface <interface> port-security static-mac` command.

```
cumulus@switch:~$ nv set interface swp1 port-security static-mac 00:02:00:00:00:05
cumulus@switch:~$ nv set interface swp1 port-security static-mac 00:02:00:00:00:06
cumulus@switch:~$ nv config apply
```

To enable sticky MAC, where the first learned MAC address on the port is the only MAC address allowed, run the `nv set interface <interface> port-security sticky-mac enabled` command.

```
cumulus@switch:~$ nv set interface swp1 port-security sticky-mac enabled
cumulus@switch:~$ nv config apply
```

To configure the time period after which the first learned MAC address ages out and no longer has access to the port, run the `nv set interface <interface> port-security sticky-timeout` command. You can specify a value between 0 and 3600 seconds. The default setting is 1800 seconds.

```
cumulus@switch:~$ nv set interface swp1 port-security sticky-timeout 2000 
cumulus@switch:~$ nv config apply
```

To enable sticky MAC aging, run the `nv set interface <interface> port-security sticky-aging enabled` command.

```
cumulus@switch:~$ nv set interface swp1 port-security sticky-ageing enable
cumulus@switch:~$ nv config apply
```

To configure violation mode, either run the `nv set interface <interface> port-security violation-mode protodown` command to put a port into ADMIN down state or run the `nv set interface <interface> port-security violation-mode restrict` command to drop packets.

```
cumulus@switch:~$ nv set interface swp1 port-security violation-mode protodown
cumulus@switch:~$ nv config apply
```

To configure the number of seconds after which the violation mode times out, run the `nv set interface <interface> port-security violation-timeout` command. You can specify a value between 0 and 60 minutes. The default value is 30 seconds.

```
cumulus@switch:~$ nv set interface swp1 port-security violation-timeout 60
cumulus@switch:~$ nv config apply
```

{{< /tab >}}
{{< tab "Linux Commands ">}}

Add the configuration settings you want to use to the `/etc/cumulus/switchd.d/port_security.conf` file, then reload `switchd` with the `sudo systemctl reload switchd.service` command to apply the changes.

| <div style="width:460px">Setting | Description|
| --------| -----------|
| `interface.<port>.port_security.enable` | Enables and disables port security. 1 enables security on the port. 0 disables security on the port. By default, port security is disabled.|
| `interface.<port>.port_security.mac_limit` | Configures the maximum number of MAC addresses allowed to access the port. You can specify a number between 0 and 512. The default value is 32.|
| `interface.<port>.port_security.static_mac` | Configures the specific MAC addresses allowed to access the port. To specify multiple MAC addresses, separate each MAC address with a space.|
| `interface.<port>.port_security.sticky_mac` | Enables and disables sticky MAC. 1 enables sticky MAC, where the first learned MAC address on the port is the only MAC address allowed. 0 disables sticky MAC. |
| `interface.<port>.port_security.sticky_timeout` | The time period after which the first learned MAC address ages out and no longer has access to the port. The default aging timeout value is 1800 seconds (30 minutes). You can specify a value between 0 and 3600 seconds (60 minutes).|
| `interface.<port>.port_security.sticky_aging` | Enables and disables sticky MAC aging. 1 enables sticky MAC aging. 0 disables sticky MAC aging.|
| `interface.<port>.port_security.violation_mode` | Configures the violation mode: 0 (protodown) puts a port into ADMIN down state. 1 (restrict) drops packets.|
| `interface.<port>.port_security.violation_timeout` | Configures the number of seconds after which the violation mode times out. You can specify a value between 0 and 3600 seconds. The default value is 1800 seconds.|

The following shows an example `/etc/cumulus/switchd.d/port_security.conf` configuration file:

```
cumulus@switch:~$ sudo nano /etc/cumulus/switchd.d/port_security.conf
...
## Interface Port security
interface.swp1.port_security.enable = 1
interface.swp1.port_security.mac_limit = 100
interface.swp1.port_security.sticky_mac = 1
interface.swp1.port_security.sticky_timeout = 2000
interface.swp1.port_security.sticky_aging = 1
interface.swp1.port_security.violation_mode = 0
interface.swp1.port_security.violation_timeout = 3600
interface.swp1.port_security.static_mac = 00:02:00:00:00:05 00:02:00:00:00:06
```

{{< /tab >}}
{{< /tabs >}}

## Troubleshooting

To show port security configuration, run the `nv show interface <interface-id> port-security` command:

```
cumulus@switch:~$ nv show interface swp1 port-security
                   operational  applied  
-----------------  -----------  ---------
enable             off          on       
mac-limit                       100      
sticky-mac                      enabled  
sticky-timeout                  2000     
sticky-ageing                   enabled  
violation-mode                  protodown
violation-timeout               60     

Static MAC
=============
00:02:00:00:00:05
00:02:00:00:00:06

mac-addresses
================
No Data
```

To show port security static MAC address information, run the `nv show interface <interface-id> port-security static-mac` command:

```
cumulus@switch:~$ nv show interface swp1 port-security static-mac
```

To show port security MAC address information, run the `nv show interface <interface-id> port-security mac-addresses` command:

```
cumulus@switch:~$ nv show interface swp1 port-security mac-addresses
```
