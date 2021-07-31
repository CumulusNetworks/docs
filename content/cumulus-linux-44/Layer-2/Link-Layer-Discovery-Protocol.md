---
title: Link Layer Discovery Protocol
author: NVIDIA
weight: 400
toc: 3
---
The `lldpd` daemon implements the IEEE802.1AB Link Layer Discovery Protocol  (LLDP) standard. LLDP shows which ports are neighbors of a given port.

By default, `lldpd` runs as a daemon and starts at system boot. `lldpd` command line arguments are in the `/etc/default/lldpd` file. All `lldpd` configuration options are saved in the `/etc/lldpd.conf` file or under `/etc/lldpd.d/`.

`lldpd` supports CDP (Cisco Discovery Protocol, v1 and v2) and logs by default into `/var/log/daemon.log` with an `lldpd` prefix.

You can use the `lldpcli` CLI tool to query the `lldpd` daemon for neighbors, statistics, and other running configuration information. See `man lldpcli(8)` for details.

## Configure LLDP Timers

You can configure the frequency of LLDP updates (between 10 and 300 seconds) and the amount of time to hold the information before discarding it. The hold time interval is a multiple of the `tx-interval`.

The following example commands configure the frequency of LLDP updates to 100 and the hold time to 3.

{{< tabs "TabID67 ">}}
{{< tab "NVUE Commands ">}}

```
cumulus@switch:~$ nv set system lldp tx-interval 100
cumulus@switch:~$ nv set system lldp tx-hold-multiplier 3
cumulus@switch:~$ nv config apply
```

{{< /tab >}}
{{< tab "Linux Commands ">}}

Add the timers to the `/etc/lldpd.conf` file or to your `.conf` file in the `/etc/lldpd.d/` directory.

{{%notice note%}}
Cumulus Linux does not ship with a `/etc/lldpd.conf` file. You must create the `/etc/lldpd.conf` file or create a `.conf` file in the `/etc/lldpd.d/` directory.
{{%/notice%}}

```
cumulus@switch:~$ sudo nano /etc/lldpd.conf
configure lldp tx-interval 40
configure lldp tx-hold 3
...
```

{{< /tab >}}
{{< /tabs >}}

## Disable LLDP on an Interface

To disable LLDP on a single interface, edit the `/etc/default/lldpd` file. This file specifies the default options to present to the `lldpd` service when it starts. The following example uses the `-I` option to disable LLDP on swp43:

```
cumulus@switch:~$ sudo nano /etc/default/lldpd

# Add "-x" to DAEMON_ARGS to start SNMP subagent
# Enable CDP by default
DAEMON_ARGS="-c -I *,!swp43"
```

{{< expand "Runtime Configuration (Advanced) "  >}}

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

{{< /expand >}}

## Enable the SNMP Subagent

LLDP does not enable the SNMP subagent by default. To enable the SNMP subagent, edit the `/etc/default/lldpd` file and add the `-x` option:

```
cumulus@switch:~$ sudo nano /etc/default/lldpd

# Add "-x" to DAEMON_ARGS to start SNMP subagent

# Enable CDP by default
DAEMON_ARGS="-c -x -M 4"
```

{{%notice note%}}
The `-c` option enables backwards compatibility with CDP and the `-M 4` option sends a field in discovery packets to indicate that the switch is a network device.
{{%/notice%}}

## Troubleshooting

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
    SysDescr:     Cumulus Linux version 4.1.0 running on quanta lb9
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
    SysDescr:     Cumulus Linux version 4.1.0 running on QEMU Standard PC (i440FX + PIIX, 1996)
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
    SysDescr:     Cumulus Linux version 4.1.0 running on QEMU Standard PC (i440FX + PIIX, 1996)
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
    SysDescr:     Cumulus Linux version 4.1.0 running on QEMU Standard PC (i440FX + PIIX, 1996)
    MgmtIP:       192.0.2.10
    MgmtIP:       fe80::201:ff:fe00:a00
    Capability:   Bridge, off
    Capability:   Router, on
  Port:
    PortID:       ifname swp1
    PortDescr:    swp1
...
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

To show a summary of `lldpd` statistics for all ports:

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

To show the running LLDP configuration:

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

You can also run the NVUE `nv show system lldp` command to show the running LLDP configuration.

## Considerations

Annex E (and hence Annex D) of IEEE802.1AB (lldp) is not supported.

## Related Information

- {{<exlink url="http://vincentbernat.github.io/lldpd/" text="GitHub - lldpd project">}}
- {{<exlink url="http://en.wikipedia.org/wiki/Link_Layer_Discovery_Protocol" text="Wikipedia - Link Layer Discovery Protocol">}}
