---
title: Link Layer Discovery Protocol
author: Cumulus Networks
weight: 119
aliases:
 - /display/DOCS/Link+Layer+Discovery+Protocol
 - /pages/viewpage.action?pageId=8366373
product: Cumulus Linux
version: '4.0'
---
The `lldpd` daemon implements the IEEE802.1AB (Link Layer Discovery Protocol, or LLDP) standard. LLDP shows you which ports are neighbors of a given port. By default, `lldpd` runs as a daemon and starts at system boot. `lldpd` command line arguments are placed in `/etc/default/lldpd`. All `lldpd` configuration options are saved in `/etc/lldpd.conf` or under `/etc/lldpd.d/`.

For more details on the command line arguments and configuration options, see `man lldpd(8)`.

`lldpd` supports CDP (Cisco Discovery Protocol, v1 and v2) and logs by default into `/var/log/daemon.log` with an `lldpd` prefix.

You can use the `lldpcli` CLI tool to query the `lldpd` daemon for neighbors, statistics, and other running configuration information. See `man lldpcli(8)` for details.

## Configure LLDP

You configure `lldpd` settings in `/etc/lldpd.conf` or `/etc/lldpd.d/`.

Here is an example persistent configuration:

```
cumulus@switch:~$ sudo cat /etc/lldpd.conf
configure lldp tx-interval 40
configure lldp tx-hold 3
configure system interface pattern *,!eth0,swp*
```

The last line in the example above shows that LLDP is disabled on eth0. To disable LLDP on a single port, edit the `/etc/default/lldpd` file. This file specifies the default options to present to the `lldpd` service when it starts. The following example uses the `-I` option to disable LLDP on swp43:

```
cumulus@switch:~$ sudo nano /etc/default/lldpd

# Add "-x" to DAEMON_ARGS to start SNMP subagent
# Enable CDP by default
DAEMON_ARGS="-c -I *, !swp43"
```

`lldpd` has two timers defined by the `tx-interval` setting that affect each switch port:

- The first timer catches any port-related changes.
- The second is a system-based refresh timer on each port that looks for other changes like hostname. This timer uses the `tx-interval` value multiplied by 20.

`lldpd` logs to `/var/log/daemon.log` with the *lldpd* prefix:

```
cumulus@switch:~$ sudo tail -f /var/log/daemon.log  | grep lldp
Aug  7 17:26:17 switch lldpd[1712]: unable to get system name
Aug  7 17:26:17 switch lldpd[1712]: unable to get system name
Aug  7 17:26:17 switch lldpcli[1711]: lldpd should resume operations
Aug  7 17:26:32 switch lldpd[1805]: NET-SNMP version 5.4.3 AgentX subagent connected
```

## Example lldpcli Commands

To show all neighbors on all ports and interfaces:

```
cumulus@switch:~$ sudo lldpcli show neighbors
-------------------------------------------------------------------------------
LLDP neighbors:
-------------------------------------------------------------------------------
Interface:    eth0, via: LLDP, RID: 1, Time: 0 day, 17:38:08
  Chassis:
    ChassisID:    mac 08:9e:01:e9:66:5a
    SysName:      PIONEERMS22
    SysDescr:     Cumulus Linux version 4.0.0 running on quanta lb9
    MgmtIP:       192.168.0.22
    Capability:   Bridge, on
    Capability:   Router, on
  Port:
    PortID:       ifname swp47
    PortDescr:    swp47
-------------------------------------------------------------------------------
Interface:    swp1, via: LLDP, RID: 10, Time: 0 day, 17:08:27
  Chassis:
    ChassisID:    mac 00:01:00:00:09:00
    SysName:      MSP-1
    SysDescr:     Cumulus Linux version 4.0.0 running on QEMU Standard PC (i440FX + PIIX, 1996)
    MgmtIP:       192.0.2.9
    MgmtIP:       fe80::201:ff:fe00:900
    Capability:   Bridge, off
    Capability:   Router, on
  Port:
    PortID:       ifname swp1
    PortDescr:    swp1
-------------------------------------------------------------------------------
Interface:    swp2, via: LLDP, RID: 10, Time: 0 day, 17:08:27
  Chassis:
    ChassisID:    mac 00:01:00:00:09:00
    SysName:      MSP-1
    SysDescr:     Cumulus Linux version 4.0.0 running on QEMU Standard PC (i440FX + PIIX, 1996)
    MgmtIP:       192.0.2.9
    MgmtIP:       fe80::201:ff:fe00:900
    Capability:   Bridge, off
    Capability:   Router, on
  Port:
    PortID:       ifname swp2
    PortDescr:    swp2
-------------------------------------------------------------------------------
Interface:    swp3, via: LLDP, RID: 11, Time: 0 day, 17:08:27
  Chassis:
    ChassisID:    mac 00:01:00:00:0a:00
    SysName:      MSP-2
    SysDescr:     Cumulus Linux version 4.0.0 running on QEMU Standard PC (i440FX + PIIX, 1996)
    MgmtIP:       192.0.2.10
    MgmtIP:       fe80::201:ff:fe00:a00
    Capability:   Bridge, off
    Capability:   Router, on
  Port:
    PortID:       ifname swp1
    PortDescr:    swp1
-------------------------------------------------------------------------------
Interface:    swp4, via: LLDP, RID: 11, Time: 0 day, 17:08:27
  Chassis:
    ChassisID:    mac 00:01:00:00:0a:00
    SysName:      MSP-2
    SysDescr:     Cumulus Linux version 4.0.0 running on QEMU Standard PC (i440FX + PIIX, 1996)
    MgmtIP:       192.0.2.10
    MgmtIP:       fe80::201:ff:fe00:a00
    Capability:   Bridge, off
    Capability:   Router, on
  Port:
    PortID:       ifname swp2
    PortDescr:    swp2
-------------------------------------------------------------------------------
Interface:    swp49s1, via: LLDP, RID: 9, Time: 0 day, 16:55:00
  Chassis:
    ChassisID:    mac 00:01:00:00:0c:00
    SysName:      TORC-1-2
    SysDescr:     Cumulus Linux version 4.0.0 running on QEMU Standard PC (i440FX + PIIX, 1996)
    MgmtIP:       192.0.2.12
    MgmtIP:       fe80::201:ff:fe00:c00
    Capability:   Bridge, on
    Capability:   Router, on
  Port:
    PortID:       ifname swp6
    PortDescr:    swp6
-------------------------------------------------------------------------------
Interface:    swp49s0, via: LLDP, RID: 9, Time: 0 day, 16:55:00
  Chassis:
    ChassisID:    mac 00:01:00:00:0c:00
    SysName:      TORC-1-2
    SysDescr:     Cumulus Linux version 4.0.0 running on QEMU Standard PC (i440FX + PIIX, 1996)
    MgmtIP:       192.0.2.12
    MgmtIP:       fe80::201:ff:fe00:c00
    Capability:   Bridge, on
    Capability:   Router, on
  Port:
    PortID:       ifname swp5
    PortDescr:    swp5
-------------------------------------------------------------------------------
```

To show `lldpd` statistics for all ports:

```
cumulus@switch:~$ sudo lldpcli show statistics
----------------------------------------------------------------------
LLDP statistics:
----------------------------------------------------------------------
Interface:    eth0
  Transmitted:  9423
  Received:     17634
  Discarded:    0
  Unrecognized: 0
  Ageout:       10
  Inserted:     20
  Deleted:      10
--------------------------------------------------------------------
Interface:    swp1
  Transmitted:  9423
  Received:     6264
  Discarded:    0
  Unrecognized: 0
  Ageout:       0
  Inserted:     2
  Deleted:      0
---------------------------------------------------------------------
Interface:    swp2
  Transmitted:  9423
  Received:     6264
  Discarded:    0
  Unrecognized: 0
  Ageout:       0
  Inserted:     2
  Deleted:      0
---------------------------------------------------------------------
Interface:    swp3
  Transmitted:  9423
  Received:     6265
  Discarded:    0
  Unrecognized: 0
  Ageout:       0
  Inserted:     2
  Deleted:      0
----------------------------------------------------------------------
...
```

To show `lldpd` statistics summary for all ports:

```
cumulus@switch:~$ sudo lldpcli show statistics summary
---------------------------------------------------------------------
LLDP Global statistics:
---------------------------------------------------------------------
Summary of stats:
  Transmitted:  648186
  Received:     437557
  Discarded:    0
  Unrecognized: 0
  Ageout:       10
  Inserted:     38
  Deleted:      10
```

To show the `lldpd` running configuration:

```
cumulus@switch:~$ sudo lldpcli show running-configuration
--------------------------------------------------------------------
Global configuration:
--------------------------------------------------------------------
Configuration:
  Transmit delay: 30
  Transmit hold: 4
  Receive mode: no
  Pattern for management addresses: (none)
  Interface pattern: (none)
  Interface pattern blacklist: (none)
  Interface pattern for chassis ID: (none)
  Override description with: (none)
  Override platform with: Linux
  Override system name with: (none)
  Advertise version: yes
  Update interface descriptions: no
  Promiscuous mode on managed interfaces: no
  Disable LLDP-MED inventory: yes
  LLDP-MED fast start mechanism: yes
  LLDP-MED fast start interval: 1
  Source MAC for LLDP frames on bond slaves: local
  Portid TLV Subtype for lldp frames: ifname
--------------------------------------------------------------------
```

<details>

<summary>Runtime Configuration (Advanced) </summary>

{{%notice warning%}}

A runtime configuration does not persist when you reboot the switch; all changes are lost.

{{%/notice%}}

To configure active interfaces:

```
cumulus@switch:~$ sudo lldpcli configure system interface pattern "swp*"
```

To configure inactive interfaces:

```
cumulus@switch:~$ sudo lldpcli configure system interface pattern *,!eth0,swp*
```

{{%notice note%}}

The active interface list always overrides the inactive interface list.

{{%/notice%}}

To reset any interface list to none:

```
cumulus@switch:~$ sudo lldpcli configure system interface pattern ""
```

</details>

## Enable the SNMP Subagent in LLDP

LLDP does not enable the SNMP subagent by default. You need to edit `/etc/default/lldpd` and enable the `-x` option.

```
cumulus@switch:~$ sudo nano /etc/default/lldpd

# Add "-x" to DAEMON_ARGS to start SNMP subagent

# Enable CDP by default
DAEMON_ARGS="-c"
```

## Caveats and Errata

Annex E (and hence Annex D) of IEEE802.1AB (lldp) is not supported.

## Related Information

- [GitHub - lldpd project](http://vincentbernat.github.io/lldpd/)
- [Wikipedia - Link Layer Discovery Protocol](http://en.wikipedia.org/wiki/Link_Layer_Discovery_Protocol)
