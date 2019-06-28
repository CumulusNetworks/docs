---
title: Link Layer Discovery Protocol
author: Cumulus Networks
weight: 73
aliases:
 - /display/RMP30/Link+Layer+Discovery+Protocol
 - /pages/viewpage.action?pageId=5118711
pageID: 5118711
product: Cumulus RMP
version: 3.0.1
imgData: cumulus-rmp-301
siteSlug: cumulus-rmp-301
---
The ` lldpd  `daemon implements the IEEE802.1AB (Link Layer Discovery
Protocol, or LLDP) standard. LLDP allows you to know which ports are
neighbors of a given port. By default, `lldpd` runs as a daemon and is
started at system boot. `lldpd` command line arguments are placed in
`/etc/default/lldpd`. `lldpd` configuration options are placed in
`/etc/lldpd.conf` or under `/etc/lldpd.d/`.

For more details on the command line arguments and config options,
please see `man lldpd(8)`.

`lldpd` supports CDP (Cisco Discovery Protocol, v1 and v2). `lldpd` logs
by default into `/var/log/daemon.log` with an `lldpd` prefix.

`lldpcli` is the CLI tool to query the `lldpd` daemon for neighbors,
statistics and other running configuration information. See `man
lldpcli(8)` for details.

## <span>Commands</span>

  - lldpd (daemon)

  - lldpcli (interactive CLI)

## <span>Man Pages</span>

  - man lldpd

  - man lldpcli

## <span>Configuring LLDP</span>

You configure `lldpd` settings in `/etc/lldpd.conf` or `/etc/lldpd.d/`.

Here is an example persistent configuration:

    cumulus@switch:~$ sudo cat /etc/lldpd.conf
    configure lldp tx-interval 40
    configure lldp tx-hold 3
    configure system interface pattern-blacklist "eth0"

`lldpd` logs to `/var/log/daemon.log` with the *lldpd* prefix:

    cumulus@switch:~$ sudo tail -f /var/log/daemon.log  | grep lldp
    Aug  7 17:26:17 switch lldpd[1712]: unable to get system name
    Aug  7 17:26:17 switch lldpd[1712]: unable to get system name
    Aug  7 17:26:17 switch lldpcli[1711]: lldpd should resume operations
    Aug  7 17:26:32 switch lldpd[1805]: NET-SNMP version 5.4.3 AgentX subagent connected

## <span>Example lldpcli Commands</span>

To see all neighbors on all ports/interfaces:

    cumulus@switch:~$ sudo lldpcli show neighbors
    ---------------------------------------------------------------------
    LLDP neighbors:
    ---------------------------------------------------------------------
    Interface:    eth0, via: CDPv1, RID: 72, Time: 0 day, 00:33:40
    Chassis:
       ChassisID:    local test-server-1
       SysName:      test-server-1
       SysDescr:     Linux running on
    Linux 3.2.2+ #1 SMP Mon Jun 10 16:21:22 PDT 2013 ppc
       MgmtIP:       192.0.2.72
       Capability:   Router, on
    Port:
       PortID:       ifname eth1
    ---------------------------------------------------------------------
    Interface:    swp1, via: CDPv1, RID: 87, Time: 0 day, 00:36:27
    nChassis:
       ChassisID:    local T1
       SysName:      T1
       SysDescr:     Linux running on
    Cumulus RMP
       MgmtIP:       192.0.2.15
       Capability:   Router, on
    Port:
       PortID:       ifname swp1
       PortDescr:    swp1
    ---------------------------------------------------------------------
    ... and more (output truncated to fit this doc)

To see neighbors on specific ports:

    cumulus@switch:~$ sudo lldpcli show neighbors ports swp1,swp2
     ---------------------------------------------------------------------
     Interface:    swp1, via: CDPv1, RID: 87, Time: 0 day, 00:36:27
     Chassis:
        ChassisID:    local T1
        SysName:      T1
        SysDescr:     Linux running on
     Cumulus RMP
        MgmtIP:       192.0.2.15
        Capability:   Router, on
     Port:
        PortID:       ifname swp1
        PortDescr:    swp1
     ---------------------------------------------------------------------
     Interface:    swp2, via: CDPv1, RID: 123, Time: 0 day, 00:36:27
     Chassis:
        ChassisID:    local T2
        SysName:      T2
        SysDescr:     Linux running on
     Cumulus RMP
        MgmtIP:       192.0.2.15
        Capability:   Router, on
     Port:
        PortID:       ifname swp1
        PortDescr:    swp1

To see `lldpd` statistics for all ports:

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
    ... and more (output truncated to fit this document)

To see lldpd statistics summary for all ports:

    cumulus@switch:~$ sudo lldpcli show statistics  summary
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

To see the `lldpd` running configuration:

    cumulus@switch:~$ sudo lldpcli show running-configuration
    --------------------------------------------------------------------
    Global configuration:
    --------------------------------------------------------------------
    Configuration:
      Transmit delay: 1
      Transmit hold: 4
      Receive mode: no
      Pattern for management addresses: (none)
      Interface pattern: (none)
      Interface pattern for chassis ID: (none)
      Override description with: (none)
      Override platform with: (none)
      Advertise version: yes
      Disable LLDP-MED inventory: yes
      LLDP-MED fast start mechanism: yes
      LLDP-MED fast start interval: 1
    --------------------------------------------------------------------

Runtime Configuration (Advanced)

{{%notice warning%}}

A runtime configuration does not persist when you reboot the switch —
all changes are lost.

{{%/notice%}}

To configure active interfaces:

    lldpcli configure system interface pattern "swp*"

To configure inactive interfaces:

    lldpcli configure system interface pattern-blacklist "eth0"

{{%notice note%}}

The active interface list always overrides the inactive interface list.

{{%/notice%}}

To reset any interface list to none:

    lldpcli configure system interface pattern-blacklist ""

## <span>Enabling the SNMP Subagent in LLDP</span>

LLDP does not enable the SNMP subagent by default. You need to edit
`/etc/default/lldpd` and enable the `-x` option.

    cumulus@switch:~$ sudo nano /etc/default/lldpd 
    # Uncomment to start SNMP subagent and enable CD
    P, SONMP and EDP protocol 
    #DAEMON_ARGS="-x -c -s -e"
    
    # Enable CDP by default 
    DAEMON_ARGS="-c"
    DAEMON_ARGS="-x"

## <span>Configuration Files</span>

  - /etc/lldpd.conf

  - /etc/lldpd.d

  - /etc/default/lldpd

## <span>Useful Links</span>

  - <http://vincentbernat.github.io/lldpd/>

  - <http://en.wikipedia.org/wiki/Link_Layer_Discovery_Protocol>

## <span>Caveats and Errata</span>

  - Annex E (and hence Annex D) of IEEE802.1AB (lldp) is not supported.
