---
title: Port Security
author: NVIDIA
weight: 380
toc: 3
---
Port security is a layer 2 traffic control feature that enables you to manage network access from end-users. Use port security to:

- Limit port access to specific MAC addresses so that the port does not forward ingress traffic from source addresses that are not defined.  
- Limit port access to only the first learned MAC address on the port (sticky MAC) so that the device with that MAC address has full bandwidth. You can provide a timeout so that the MAC address on that port no longer has access after a specified time.
- Limit port access to a specific number of MAC addresses.

You can specify what action to take when there is a port security violation (drop packets or put the port into ADMIN down state) and add a timeout for the action to take effect.

{{%notice note%}}

- Port security is supported on Broadcom switches only.
- Layer 2 interfaces in trunk or access mode are currently supported. However, interfaces in a bond are *not* supported.

{{%/notice%}}

## Configure MAC Address Options

**To limit port access to a specific MAC address**, run the following commands.

The example commands configure swp1 to allow access to MAC address 00:02:00:00:00:05:

```
cumulus@switch:~$ net add interface swp1 port-security allowed-mac 00:02:00:00:00:05
```

You can specify only one MAC address with the NCLU command. To specify multiple MAC addresses, set the `interface.<port>.port_security.static_mac` parameter in the `/etc/cumulus/switchd.d/port_security.conf` file. See {{<link title="#Configure Port Security Manually" text="Configure Port Security Manually">}} below.

**To enable sticky MAC on a port**, where the first learned MAC address on the port is the only MAC address allowed, run the following commands.

You can add a timeout value so that after the time specified, the MAC address ages out and no longer has access to the port. The default aging timeout value is 1800 seconds. You can specify a value between 0 and 3600 seconds.

The example commands enable sticky MAC on interface swp1, set the timeout value to 2000 seconds, and enable aging.

```
cumulus@switch:~$ net add interface swp1 port-security sticky-mac
cumulus@switch:~$ net add interface swp1 port-security sticky-mac timeout 2000
cumulus@switch:~$ net add interface swp1 port-security sticky-mac aging
cumulus@switch:~$ net pending
cumulus@switch:~$ net commit
```

**To limit the number of MAC addresses that are allowed to access a port**, run the following commands. You can specify a number between 0 and 512. The default is 32.

The example commands configure swp1 to limit access to 40 MAC addresses:

```
cumulus@switch:~$ net add interface swp1 port-security mac-limit 40
cumulus@switch:~$ net pending
cumulus@switch:~$ net commit
```

## Configure Security Violation Actions

You can configure the action you want to take when there is a security violation on a port:

- `shutdown` puts a port into ADMIN down state
- `restrict` drops packets. When packets are dropped, Cumulus Linux sends a log message.

You can also set a timeout value between 0 and 3600 seconds for the action to take effect. The default is 1800 seconds.

The following example commands put swp1 into ADMIN down state when there is a security violation and set the timeout value to 3600 seconds:

```
cumulus@switch:~$ net add interface swp1 port-security violation shutdown
cumulus@switch:~$ net add interface swp1 port-security violation timeout 3600
cumulus@switch:~$ net pending
cumulus@switch:~$ net commit
```

## Enable Port Security Settings

After you configure the port security settings to suit your needs, you can enable security on a port with the following commands:

```
cumulus@switch:~$ net add interface swp1 port-security
cumulus@switch:~$ net pending
cumulus@switch:~$ net commit
```

To disable port security on a port, run the `net del interface <interface> port-security` command.

## Configure Port Security Manually

You can edit the `/etc/cumulus/switchd.d/port_security.conf` file manually to configure port security instead of running the NCLU commands shown above. This procedure is useful if you use configuration scripts.

Add the configuration settings you want to use to the `/etc/cumulus/switchd.d/port_security.conf` file, then restart `switchd` to apply the changes.

| <div style="width:460px">Setting | Description|
| --------| -----------|
| `interface.<port>.port_security.enable` | 1 enables security on the port. 0 disables security on the port.|
| `interface.<port>.port_security.mac_limit` | The maximum number of MAC addresses allowed to access the port. You can specify a number between 0 and 512. The default is 32.|
| `interface.<port>.port_security.static_mac` | The specific MAC addresses allowed to access the port. You can specify multiple MAC addresses. Separate each MAC address with a space.|
| `interface.<port>.port_security.sticky_mac` | 1 enables sticky MAC, where the first learned MAC address on the port is the only MAC address allowed. 0 disables sticky MAC. |
| `interface.<port>.port_security.sticky_timeout` | The time period after which the first learned MAC address ages out and no longer has access to the port. The default aging timeout value is 30 minutes. You can specify a value between 0 and 60 minutes.|
| `interface.<port>.port_security.sticky_aging` | 1 enables sticky MAC aging. 0 disables sticky MAC aging.|
| `interface.<port>.port_security.violation_mode` | The violation mode: 0 (shutdown) puts a port into ADMIN down state. 1 (restrict) drops packets.|
| `interface.<port>.port_security.violation_timeout` | The number of seconds after which the violation mode times out. You can specify a value between 0 and 3600 seconds. The default value is 1800 seconds.|

An example `/etc/cumulus/switchd.d/port_security.conf` configuration file is shown here:

```
cumulus@switch:~$ sudo nano /etc/cumulus/switchd.d/port_security.conf
interface.swp1.port_security.enable = 1
interface.swp1.port_security.mac_limit = 32
interface.swp1.port_security.static_mac = 00:02:00:00:00:05 00:02:00:00:00:06
interface.swp1.port_security.sticky_mac = 1
interface.swp1.port_security.sticky_timeout = 2000
interface.swp1.port_security.sticky_aging = 1
interface.swp1.port_security.violation_mode = 0
interface.swp1.port_security.violation_timeout = 3600
...
```

## Show Port Security Configuration

To show port security settings for all ports:

```
cumulus@switch:~$ net show port-security
Interface  Port security  MAC limit  Sticky MAC  Sticky MAC aging  Sticky MAC timeout  Violation mode  Timeout
---------  -------------  ---------  ----------  ----------------  ------------------  --------------  -------
swp1       ENABLED        40         ENABLED     ENABLED           2000                Shutdown        3600
swp2       Disabled       NA         NA          NA                NA                  Restrict        1800
swp3       Disabled       NA         NA          NA                NA                  Restrict        1800
swp4       Disabled       NA         NA          NA                NA                  Restrict        1800
swp5       Disabled       NA         NA          NA                NA                  Restrict        1800
swp6       Disabled       NA         NA          NA                NA                  Restrict        1800
...
```

To show port security settings for a specific port:

```
cumulus@switch:~$ net show port-security swp1
Interface           swp1
Port security       Enabled
Mac limit           40
Sticky mac          ENABLED
Sticky MAC aging    Enabled
Sticky MAC timeout  1440
Violation mode      Shutdown
Violation timeout   3600
Mac addresses
00:02:00:00:00:05
00:02:00:00:00:06
```
