---
title: What's New in Cumulus RMP 3.0.0
author: Cumulus Networks
weight: 11
aliases:
 - /display/RMP30/What's+New+in+Cumulus+RMP+3.0.0
 - /pages/viewpage.action?pageId=5118741
pageID: 5118741
product: Cumulus RMP
version: 3.0.1
imgData: cumulus-rmp-301
siteSlug: cumulus-rmp-301
---
Cumulus RMP 3.0.0 has a host of new features and capabilities. In
addition to this chapter, please read the [release
notes](https://support.cumulusnetworks.com/hc/en-us/articles/217040088)
to learn about known issues with this release.

Cumulus RMP 3.0.0 includes these new features and platforms:

  - [Debian Jessie](https://www.debian.org/releases/jessie/) (upgraded
    from [Debian Wheezy](https://www.debian.org/releases/wheezy/))

  - [4.1 kernel](http://kernelnewbies.org/Linux_4.1) (upgraded from 3.2)

  - Debian's [`systemctl` and
    `systemd`](https://wiki.archlinux.org/index.php/systemd) replace the
    `service` command for administering services; they also replace
    `jdoo` for monitoring

  - New installer

Read on to learn about more new functionality and new behaviors.

## <span>New Behavior and Functionality</span>

Cumulus RMP 3.0.0 marks a significant departure from earlier releases of
the operating system. As such, some new functionality and behaviors are
to be expected.

### <span>Cumulus RMP Now Based on Jessie</span>

Cumulus RMP is now based on Debian Jessie, instead of Debian Wheezy. For
a list of issues you need to be aware of, please read the [Debian
documentation](https://www.debian.org/releases/stable/amd64/release-notes/ch-information.en.html).

### <span>Default snmpd Port Binding</span>

In previous releases of Cumulus RMP, the default port binding
configuration in `/etc/snmp/snmpd.conf` was:

    # 2.5.x default agent IP address binding (bind to all interfaces on UDP port 161)
    agentAddress udp::161

This meant that the `snmpd` daemon listed and responded to all ports for
UDP port 161.

In Cumulus RMP 3.0, the default configuration has been updated to a more
secure setting:

    # 3.x default agent IP address binding (bind to only loopback interface on UDP port 161)
    agentAddress udp:127.0.0.1:161

This ensures that by default, the `snmpd` daemon will only listen on the
loopback interface on UDP port 161, and will only respond to SNMP
requests originating on the switch itself, rather than requests coming
into the box on an interface. Since this is really only useful for
testing purposes, most customers should change this to binding to a
specific IP address.

### <span>iquerySecName and Rouser</span>

In 2.5.x, default values for iquerySecName and rouser were configured in
`/etc/snmp/snpd.conf` as follows:

    iquerySecName internalUser
    rouser internalUser

In 3.x, the default configuration has been updated to a more secure
setting, by commenting out the default user:

    #iquerySecName internalUser
    #rouser internalUser

User accounts must now be created manually for SNMP traps to function
correctly.

### <span>New Bond Defaults</span>

In order to simplify configurations, many [bond
settings](/version/cumulus-rmp-301/Layer_1_and_Layer_2_Features/Bonding_-_Link_Aggregation)
have had their defaults changed:

| Setting          | 2.x Default | 3.x Default |
| ---------------- | ----------- | ----------- |
| lacp-rate        | none        | 1           |
| miimon           | 0           | 100         |
| min-links        | 0           | 1           |
| mode             | none        | 802.3ad     |
| use-carrier      | none        | 1           |
| xmit-hash-policy | none        | layer3+4    |

### <span>New bridge mdb Command Syntax</span>

The syntax of the `bridge mdb` command has changed slightly. Instead of
using `vlan <vid>` to specify the VLAN ID of a multicast group on a
VLAN-aware bridge, Cumulus RMP uses `vid <vid>`. Similarly, when dumping
the MDB with the `bridge mdb show` command, the VLAN ID, if any, is
displayed following the `vid` keyword.

### <span>Adding Static Bridge FDB Entries</span>

To add a static bridge FDB entry, make sure to specify *static* in the
`bridge fdb` command. For example:

    cumulus@switch:~$ sudo bridge fdb add 00:01:02:03:04:06 dev eth0 master static

### <span>Printing VLAN Ranges for a Bridge</span>

In order to print a range of [VLANs in a bridge](#src-5118741), use the
`-c` option with `bridge vlan show`:

    cumulus@switch:~$ bridge -c vlan show

### <span>List of Ports for a VLAN No Longer Displayed</span>

The `bridge vlan show vlan <vlanid>` command in the Linux 4.1 kernel no
longer displays the list of ports for a VLAN, unlike in the 3.2 kernel,
which did show list of ports for a VLAN.

In addition, the `/sys/class/net/<portname>/brport/pvid sysfs` node is
no longer present in Cumulus RMP.

### <span>virtio-net Driver Changes</span>

The default speed setting for the virtio-net driver is set to SPEED\_10.

In addition, VLAN Tx offload is enabled in the virtio-net driver by
default.

### <span>New ARP Refresh Rate</span>

For [ARP
timers](https://support.cumulusnetworks.com/hc/en-us/articles/202012933),
the default `base_reachable_time_ms` in Cumulus RMP 3.0 and later is
14400000 (4 hours); in Cumulus RMP 2.5.x it is 110000 (110 seconds).

### <span>switchd Doesn't Start if License Isn't Present</span>

If a license is not installed on a Cumulus RMP switch, the `switchd`
service will not start. If you install the license again, start
`switchd` with:

    cumulus@switch:~$ sudo systemctl start switchd.service

### <span>SSH to Switch as root User Disabled by Default</span>

To improve security, the ability to use SSH to connect to a switch as
the root user using a password has been disabled by default. To enable
it, read [User Accounts](/display/RMP30/User+Accounts).

### <span>SSH Output No Longer Truncated</span>

In Cumulus RMP 2.5.x, depending upon the number of peers on the network,
the output of `show ip bgp summary json` over an SSH session might get
truncated. This has been fixed in Cumulus RMP 3.0.

## <span>Removed Features</span>

  - `cl-img-install`. The
    [installer](/display/RMP30/Installing+a+New+Cumulus+Linux+Image) has
    been replaced.

  - Disk image slots and `/mnt/persist`: For information and strategies
    on how to preserve your network configuration across software
    upgrades, read the [Upgrading Cumulus
    Linux](/display/RMP30/Upgrading+Cumulus+Linux) chapter.

  - `cl-brctl`. This utility was simply a symlink to `brctl`, which is
    what you should use to [configure
    bridges](/display/RMP30/Ethernet+Bridging+-+VLANs), VLANs and the
    like.

  - `jdoo`. Use `systemd` and `systemctl` for
    [monitoring](/display/RMP30/Monitoring+and+Troubleshooting) your
    switches.
