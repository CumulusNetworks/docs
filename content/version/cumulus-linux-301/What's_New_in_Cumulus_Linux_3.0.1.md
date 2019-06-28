---
title: What's New in Cumulus Linux 3.0.1
author: Cumulus Networks
weight: 11
aliases:
 - /display/CL30/What's+New+in+Cumulus+Linux+3.0.1
 - /pages/viewpage.action?pageId=5118422
pageID: 5118422
product: Cumulus Linux
version: '3.0'
imgData: cumulus-linux-301
siteSlug: cumulus-linux-301
---
Cumulus Linux 3.0.1 includes bug fixes only.

Cumulus Linux 3.0 has a host of new features and capabilities. In
addition to this chapter, please read the [release
notes](https://support.cumulusnetworks.com/hc/en-us/articles/222822047)
to learn about known issues with this release.

Cumulus Linux 3.0 includes these new features and platforms:

  - [Debian Jessie](https://www.debian.org/releases/jessie/) (upgraded
    from [Debian Wheezy](https://www.debian.org/releases/wheezy/))

  - [4.1 kernel](http://kernelnewbies.org/Linux_4.1) (upgraded from 3.2)

  - Debian's [`systemctl` and
    `systemd`](https://wiki.archlinux.org/index.php/systemd) replace the
    `service` command for administering services; they also replace
    `jdoo` for monitoring

  - New installer

  - [Quagga
    reload](/version/cumulus-linux-301/Layer_3_Features/Quagga_Overview)

  - [VRF: virtual routing and
    forwarding](/version/cumulus-linux-301/Layer_3_Features/Virtual_Routing_and_Forwarding_-_VRF)

  - [BGP
    add-path](Border_Gateway_Protocol_-_BGP.html#src-5118393_BorderGatewayProtocol-BGP-add-path)
    (TX and RX)

  - [Redistribute
    neighbor](/version/cumulus-linux-301/Layer_3_Features/Redistribute_Neighbor)

  - New ASICs and platforms
    
      - New switching silicon (Broadcom Tomahawk and Trident II+,
        Mellanox Spectrum)
    
      - 100G platforms: Dell Z9100, Mellanox SN2700
    
      - 10GT switches: Dell S4048T

Read on to learn about more new functionality and new behaviors.

## <span>New Behavior and Functionality</span>

Cumulus Linux 3.0 marks a significant departure from earlier releases of
the operating system. As such, some new functionality and behaviors are
to be expected.

### <span>Cumulus Linux Now Based on Jessie</span>

Cumulus Linux is now based on Debian Jessie, instead of Debian Wheezy.
For a list of issues you need to be aware of, please read the [Debian
documentation](https://www.debian.org/releases/stable/amd64/release-notes/ch-information.en.html).

### <span>Quagga Default Configuration Changes</span>

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
</colgroup>
<thead>
<tr class="header">
<th><p> </p></th>
<th><p><strong>Description</strong></p></th>
<th><p><strong>2.5.x Default Configuration</strong></p></th>
<th><p><strong>3.x Default Configuration</strong></p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>ospf log-adjacency-changes</p></td>
<td><p>Logs a single message when a peer transitions to/from FULL state</p></td>
<td><p> </p></td>
<td><p>On</p></td>
</tr>
<tr class="even">
<td><p>ospf spf timers</p></td>
<td><p>OSPF uses three timers (A, B, C) as an exponential backoff, to prevent consecutive SPFs from hammering the CPU.</p>
<ul>
<li><p>A: ms from initial event until SPF runs</p></li>
<li><p>B: ms between consecutive SPF runs (the number doubles with each SPF, until it reaches the value of C)</p></li>
<li><p>C: Maximum ms between SPFs</p></li>
</ul></td>
<td><ul>
<li><p>A: 200</p></li>
<li><p>B: 1000</p></li>
<li><p>C: 10000</p></li>
</ul></td>
<td><ul>
<li><p>A: 0</p></li>
<li><p>B: 50</p></li>
<li><p>C: 5000</p></li>
</ul></td>
</tr>
<tr class="odd">
<td><p>bgp log-neighbor-changes</p></td>
<td><p>Logs a single message when a peer transitions to/from Established state</p></td>
<td><p> </p></td>
<td><p>On</p></td>
</tr>
<tr class="even">
<td><p>bgp deterministic-med</p></td>
<td><p>Ensures path ordering no longer impactrs bestpath selection</p></td>
<td><p> </p></td>
<td><p>Enabled</p></td>
</tr>
<tr class="odd">
<td><p>bgp default show-hostname</p></td>
<td><p>Displays the hostname in show command output.</p></td>
<td><p> </p></td>
<td><p>Enabled</p></td>
</tr>
<tr class="even">
<td><p>bgp network import-check</p></td>
<td><p> </p></td>
<td><p> </p></td>
<td><p>Enabled</p></td>
</tr>
<tr class="odd">
<td><p>bgp keepalive timers</p></td>
<td><p> </p></td>
<td><p>60s</p></td>
<td><p>3s</p></td>
</tr>
<tr class="even">
<td><p>bgp hold timers</p></td>
<td><p> </p></td>
<td><p>180s</p></td>
<td><p>9s</p></td>
</tr>
<tr class="odd">
<td><p>bgp timers-connect</p></td>
<td><p>Controls how long Cumulus Linux waits between attempts to bring up a peer</p></td>
<td><p>120s</p></td>
<td><p>10s</p></td>
</tr>
</tbody>
</table>

Additional configuration changes:

  - BGP peer-groups restrictions have been replaced with update-groups,
    which dynamically examine all peers, and group them if they have the
    same outbound policy.

  - BGP Min Route Advertisement Interval timers for eBGP and iBGP were
    set to 0 seconds, rather than 30 seconds for eBGP and 5 seconds for
    iBGP.

  - IPv6 Route Advertisements are automatically enabled on an interface
    with IPv6 addresses, so the step `no ipv6 nd suppress-ra` is no
    longer needed for BGP unnumbered. The timer interval for RAs remains
    600s, which may need to be adjusted to bring up peers quickly.

  - A peer needs to be attached to a peer-group only once, when it then
    inherits all address-families activated for that peer-group.

  - The default configuration for `bgp best path as-path
    multipath-relax` has been changed to `no-as-set`, as the Quagga
    implementation produced strange routing scenarios when allowed to
    create an AS\_SET in some situations. An as-set configuration option
    has been added.

  - BGP multipath is enabled by default; the number of maximum paths
    defaults to 64.

  - Simplified BGP unnumbered configuration — a single command can
    configure a neighbor and attach to peer-group:  
    `neighbor <swpX> interface peer-group <group name>`

### <span>PowerPC Switches Not Supported</span>

PowerPC switches are **not** supported under Cumulus Linux 3.0. They are
supported under Cumulus Linux 2.5 Extended Service Release (ESR). To see
if your switch uses a PowerPC processor, you can either:

  - Check the [hardware compatibility list
    (HCL)](http://cumulusnetworks.com/hcl).

  - Run `uname -m` in the console on the switch. If it returns *ppc*,
    it's a PowerPC switch.

### <span>Default snmpd Port Binding</span>

In previous releases of Cumulus Linux, the default port binding
configuration in `/etc/snmp/snmpd.conf` was:

    # 2.5.x default agent IP address binding (bind to all interfaces on UDP port 161)
    agentAddress udp::161

This meant that the `snmpd` daemon listed and responded to all ports for
UDP port 161.

In Cumulus Linux 3.0, the default configuration has been updated to a
more secure setting:

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
`/etc/snmp/snmpd.conf` as follows:

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
settings](/version/cumulus-linux-301/Layer_1_and_Layer_2_Features/Bonding_-_Link_Aggregation)
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
VLAN-aware bridge, Cumulus Linux uses `vid <vid>`. Similarly, when
dumping the MDB with the `bridge mdb show` command, the VLAN ID, if any,
is displayed following the `vid` keyword.

### <span>Adding Static Bridge FDB Entries</span>

To add a static bridge FDB entry, make sure to specify *static* in the
`bridge fdb` command. For example:

    cumulus@switch:~$ sudo bridge fdb add 00:01:02:03:04:06 dev eth0 master static

### <span>Printing VLAN Ranges for a Bridge</span>

In order to print a range of [VLANs in a
bridge](/version/cumulus-linux-301/Layer_1_and_Layer_2_Features/Ethernet_Bridging_-_VLANs/VLAN-aware_Bridge_Mode_for_Large-scale_Layer_2_Environments),
use the `-c` option with `bridge vlan show`:

    cumulus@switch:~$ bridge -c vlan show

### <span>List of Ports for a VLAN No Longer Displayed</span>

The `bridge vlan show vlan <vlanid>` command in the Linux 4.1 kernel no
longer displays the list of ports for a VLAN, unlike in the 3.2 kernel,
which did show list of ports for a VLAN.

In addition, the `/sys/class/net/<portname>/brport/pvid sysfs` node is
no longer present in Cumulus Linux.

### <span>Expanded Reserved VLAN Range</span>

Cumulus Linux now [reserves a
range](VLAN-aware_Bridge_Mode_for_Large-scale_Layer_2_Environments.html#src-5118287_VLAN-awareBridgeModeforLarge-scaleLayer2Environments-range)
of 1000 VLAN IDs, from 3000 to 3999. Previously, the range was 700
VLANs, numbered 3300 to 3999.

### <span>virtio-net Driver Changes</span>

The default speed setting for the virtio-net driver is set to SPEED\_10.

In addition, VLAN Tx offload is enabled in the virtio-net driver by
default.

### <span>MLAG ad\_actor\_key Setting Change</span>

In Cumulus Linux 3.0, the `ad_actor_key` parameter for a 10G full-duplex
port is set to 13; in Cumulus Linux 2.5.x, the `ad_actor_key` for the
same 10G speed and full-duplex port was set to 33.

### <span>New ARP Refresh Rate</span>

<span style="color: #000000;"> For [ARP
timers](https://support.cumulusnetworks.com/hc/en-us/articles/202012933),
the default </span> `base_reachable_time_ms`
<span style="color: #000000;"> in Cumulus Linux 3.0 and later is
14400000 (4 hours); in Cumulus Linux 2.5.x it is 110000 (110 seconds).
</span>

### <span>switchd Doesn't Start if License Isn't Present</span>

If a license is not installed on a Cumulus Linux switch, the `switchd`
service will not start. If you install the license again, start
`switchd` with:

    cumulus@switch:~$ sudo systemctl start switchd.service

### <span>SSH to Switch as root User Disabled by Default</span>

To improve security, the ability to use SSH to connect to a switch as
the root user using a password has been disabled by default. To enable
it, read [User
Accounts](/version/cumulus-linux-301/System_Management/Authentication_Authorization_and_Accounting/User_Accounts).

### <span>SSH Output No Longer Truncated</span>

In Cumulus Linux 2.5.x, depending upon the number of peers on the
network, the output of `show ip bgp summary json` over an SSH session
might get truncated. This has been fixed in Cumulus Linux 3.0.

## <span>Not All Features Available on Mellanox Platforms</span>

A number of features are not available or are limited on [Mellanox
switches](http://cumulusnetworks.com/hcl/) at this time. These include:

  - ACLs

  - CDP

  - SPAN (however, ERSPAN is supported)

  - VRF

  - VXLAN

  - Resilient hashing

  - 64 MACs (breakout to 25G is limited)

  - sFlow

  - Specific cables supported

### <span>Supported Cables for Mellanox Switches</span>

Cumulus Networks has tested and suggests using the following cables and
transceivers with Mellanox switches at this time:

Speed: 10G (QSA Adapter Used)

Manufacturer

Label (or internal EEPROM)

Type

Form Factor

Supported Lengths

Supported Speeds

Known Issues?

Mellanox

MFM1T02A-SR

SR

SFP

X

10G

 

Mellanox

MFM1T02A-LR

LR

SFP

X

10G

 

Mellanox

MC3309130

DAC

SFP

2M, 3M, 5M, 7M

10G

 

 

 

 

 

 

 

 

Speed: 40G

Manufacturer

Label (or internal EEPROM)

Type

Form Factor

Supported Lengths

Supported Speeds

Known Issues?

Finisar

FTL410QE2C

SR

QSFP

X

40G

 

Mellanox

MC2210411-SR4

SR

QSFP

X

40G

 

Mellanox

MC2210411-LR4

LR

QSFP

X

40G

 

Mellanox

MC2210130

DAC

QSFP

1M, 3M, 5M

40G

 

Mellanox

MC2210310

AoC

QSFP

10M

40G

 

Ampehnol

APF14190032M3A

DAC

QSFP

3M

40G

 

JDSU

JQP—04SWAA1

SR

QSFP

X

40G

 

 

 

 

 

 

 

 

Speed: 100G

Manufacturer

Label (or internal EEPROM)

Type

Form Factor

Supported Lengths

Supported Speeds

Known Issues?

Mellanox

MCP1600

DAC

QSFP

2M, 3M

40G/100G

 

Mellanox

MMA1B00

SR

QSFP

X

40G/100G

 

TE Connectivity

2231368-1

DAC

QSFP

1M, 3M

40G/100G

 

Ampehnol

NDAAFF

DAC

QSFP

1M

40G/100G

 

 

 

 

 

 

 

 

Speed: 40G to 4x10G

Manufacturer

Label (or internal EEPROM)

Type

Form Factor

Supported Lengths

Supported Speeds

Known Issues?

Mellanox

MC2609130

DAC

QSFP to 4xSFP

1M

40G to 4x10G

 

Ampehnol

NDAQGF-0002 (internal)

DAC

QSFP to 4xSFP

1M, 3M

40G to 4x10G

 

 

 

 

 

 

 

 

Speed: 100G to 4x25G

Manufacturer

Label (or internal EEPROM)

Type

Form Factor

Supported Lengths

Supported Speeds

Known Issues?

Mellanox

MCP7F00-A02A

DAC

QSFP to 4xSFP

3M

100G to 4x25G

 

10Gtek

CAB-ZQP/4ZSP-P1M

DAC

QSFP to 4xSFP

1M

100G to 4x25G

 

 

 

 

 

 

 

 

Speed: 40G to 1x10G

Manufacturer

Label (or internal EEPROM)

Type

Form Factor

Supported Lengths

Supported Speeds

Known Issues?

Mellanox

MC2309130

DAC

QSFP to 1xSFP

3M, 5M

40G to 1x10G

 

 

 

 

 

 

 

 

Speed: 100G to 2x50G

Manufacturer

Label (or internal EEPROM)

Type

Form Factor

Supported Lengths

Supported Speeds

Known Issues?

Mellanox

MCP7H00

DAC

QSFP to 2xQSFP

1M, 3M, 5M

100G to 2x50G

Yes (with ConnectX4)

## <span>Early Access Features</span>

The following [early access
features](https://support.cumulusnetworks.com/hc/en-us/articles/202933878)
are included in Cumulus Linux 3.0:

  - [Quagga automation
    optimization](https://support.cumulusnetworks.com/hc/en-us/articles/203735078)
    (applies configuration modifications only)

## <span>Removed Features</span>

  - `cl-img-install`. The
    [installer](/version/cumulus-linux-301/Installation_Upgrading_and_Package_Management/Managing_Cumulus_Linux_Disk_Images/Installing_a_New_Cumulus_Linux_Image)
    has been replaced.

  - Disk image slots and `/mnt/persist`: For information and strategies
    on how to preserve your network configuration across software
    upgrades, read the [Upgrading Cumulus
    Linux](/version/cumulus-linux-301/Installation_Upgrading_and_Package_Management/Managing_Cumulus_Linux_Disk_Images/Upgrading_Cumulus_Linux)
    chapter.

  - `cl-ns-mgmt`: This experimental feature was introduced in Cumulus
    Linux 2.1.1 to help users separate their management network from the
    in-band network. You should use [management
    VRF](/version/cumulus-linux-301/Layer_3_Features/Management_VRF)
    instead.

  - The following [LACP
    bypass](/version/cumulus-linux-301/Layer_1_and_Layer_2_Features/LACP_Bypass)
    settings are no longer supported: priority mode,
    <span style="color: #000000;"> bond-lacp-bypass-period,
    bond-lap-bypass-priority and </span> <span style="color: #000000;">
    bond-lap-bypass-all-active </span> .

  - The `clag_enable` and `ad_sys_mac_addr`
    [bonding](/version/cumulus-linux-301/Layer_1_and_Layer_2_Features/Bonding_-_Link_Aggregation)
    parameters.

  - `cl-brctl`. This utility was simply a symlink to `brctl`, which is
    what you should use to [configure
    bridges](/version/cumulus-linux-301/Layer_1_and_Layer_2_Features/Ethernet_Bridging_-_VLANs/),
    VLANs and the like.

  - `jdoo`. Use `systemd` and `systemctl` for
    [monitoring](/version/cumulus-linux-301/Monitoring_and_Troubleshooting/)
    your switches.
