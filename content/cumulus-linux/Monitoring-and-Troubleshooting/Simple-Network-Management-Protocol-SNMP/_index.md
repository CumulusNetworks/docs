---
title: Simple Network Management Protocol - SNMP
author: Cumulus Networks
weight: 231
aliases:
 - /display/DOCS/Simple+Network+Management+Protocol+(SNMP)+Monitoring
 - /display/DOCS/SNMP+Monitoring
 - /pages/viewpage.action?pageId=8362608
pageID: 8362608
product: Cumulus Linux
version: 3.7
imgData: cumulus-linux
siteSlug: cumulus-linux
---
Cumulus Linux uses the open source Net-SNMP agent `snmpd`, version 5.7,
which provides support for most of the common industry+wide MIBs,
including interface counters and TCP/UDP IP stack data.

## History

SNMP is an IETF standards-based network management architecture and
protocol that traces its roots back to Carnegie-Mellon University in
1982. Since then, it has been modified by programmers at the University
of California. In 1995, this code was also made publicly available as
the UCD project. After that, `ucd-snmp` was extended by work done at the
University of Liverpool as well as later in Denmark. In late 2000, the
project name changed to `net-snmp` and became a fully-fledged
collaborative open source project. The version used by Cumulus Networks
is based on the latest `net-snmp` 5.7 branch with added custom MIBs and
pass-through and pass-persist scripts ([see below](#pass-persist-scripts)
for more information on pass persist scripts).

## Introduction to Simple Network Management Protocol

SNMP Management servers gather information from different systems in a
consistent manner and the paths to the relevant information are
standardized in IETF RFCs. SNMPs longevity is due to the fact that it
standardizes the objects collected from devices, the protocol used for
transport, and architecture of the management systems. The most widely
used, and most insecure, versions of SNMP are versions 1 and 2c and
their popularity is largely due to implementations that have been in use
for decades. SNMP version 3 is the recommended version because of its
advanced security features. In general, a network being profiled by SNMP
Management Stations mainly consist of devices containing SNMP agents.
The agent running on Cumulus Linux switches and routers is the `snmpd`
daemon.

### SNMP Managers

An SNMP Network Management System (NMS) is a computer that is configured
to poll SNMP agents (in this case, Cumulus Linux switches and routers)
to gather information and present it. This manager can be any machine
that can send query requests to SNMP agents with the correct
credentials. This NMS can be a large set of monitoring suite or as
simple as some scripts that collect and display data. The managers
generally poll the agents and the agents respond with the data. There
are a variety of polling command-line tools (snmpget, snmpgetnext,
snmpwalk, snmpbulkget, snmpbulkwalk, and so on). SNMP agents can also
send unsolicited Traps/Inform messages to the SNMP Manager based on
predefined criteria (like link changes).

### SNMP Agents

The SNMP agents (`snmpd`) running on the switches do the bulk of the
work and are responsible for gathering information about the local
system and storing data in a format that can be queried updating an
internal database called the *management information base*, or MIB. The
MIB is a standardized, hierarchical structure that stores information
that can be queried. Parts of the MIB tree are available and provided to
incoming requests originating from an NMS host that has authenticated
with the correct credentials. You can configure the Cumulus Linux switch
with usernames and credentials to provide authenticated and encrypted
responses to NMS requests. The `snmpd` agent can also proxy requests and
act as a *master agent* to sub-agents running on other daemons (FRR,
LLDP).

### Management Information Base (MIB)

The MIB is a database that is implemented on the daemon (or agent) and
follows IETF RFC standards to which the manager and agents adhere. It is
a hierarchical structure that, in many areas, is globally standardized,
but also flexible enough to allow vendor-specific additions. Cumulus
Networks implements a number of custom enterprise MIB tables and these
are defined in text files located on the switch and in files named
`/usr/share/snmp/mibs/Cumulus*`. The MIB structure is best understood as
a top-down hierarchical tree. Each branch that forks off is labeled with
both an identifying number (starting with 1) and an identifying string
that is unique for that level of the hierarchy. These strings and
numbers can be used interchangeably. A specific node of the tree can be
traced from the unnamed root of the tree to the node in question. The
parent IDs (numbers or strings) are strung together, starting with the
most general to form an address for the MIB Object. Each junction in the
hierarchy is represented by a dot in this notation so that the address
ends up being a series of ID strings or numbers separated by dots. This
entire address is known as an object identifier (OID).

Hardware vendors that embed SNMP agents in their devices sometimes
implement custom branches with their own fields and data points.
However, there are standard MIB branches that are well defined and can
be used by any device. The standard branches discussed here are all
under the same parent branch structure. This branch defines information
that adheres to the MIB-2 specification, which is a revised standard for
compliant devices. You can use various online and command-line tools to
translate between numbers and string and to also provide definitions for
the various MIB Objects. For example, you can view the `sysLocation`
object in the system table with either a string of numbers
**1.3.6.1.2.1.1.6** or the string representation
**iso.org.dod.internet.mgmt.mib-2.system.sysLocation.** You can view the
definition with the snmptranslate (1) command (found in the `snmp`
Debian package).

    /home/cumulus# snmptranslate -Td -On SNMPv2-MIB::sysLocation                                                                                                                                                                                                                                                                                      
    .1.3.6.1.2.1.1.6
    sysLocation OBJECT-TYPE
      -- FROM       SNMPv2-MIB
      -- TEXTUAL CONVENTION DisplayString
      SYNTAX        OCTET STRING (0..255)
      DISPLAY-HINT  "255a"
      MAX-ACCESS    read-write
      STATUS        current
      DESCRIPTION   "The physical location of this node (e.g., 'telephone
                closet, 3rd floor').  If the location is unknown, the
                value is the zero-length string."
    ::= { iso(1) org(3) dod(6) internet(1) mgmt(2) mib-2(1) system(1) 6 }
     
    /home/cumulus# snmptranslate  -Tp -IR   system
    +--system(1)
       |
       +-- -R-- String    sysDescr(1)
       |        Textual Convention: DisplayString
       |        Size: 0..255
       +-- -R-- ObjID     sysObjectID(2)
       +-- -R-- TimeTicks sysUpTime(3)
       |  |
       |  +--sysUpTimeInstance(0)
       |
       +-- -RW- String    sysContact(4)
       |        Textual Convention: DisplayString
       |        Size: 0..255
       +-- -RW- String    sysName(5)
       |        Textual Convention: DisplayString
       |        Size: 0..255
       +-- -RW- String    sysLocation(6)
       |        Textual Convention: DisplayString
       |        Size: 0..255
       +-- -R-- INTEGER   sysServices(7)
       |        Range: 0..127
       +-- -R-- TimeTicks sysORLastChange(8)
       |        Textual Convention: TimeStamp

The section ` 1.3.6.1  `or `iso.org.dod.internet` is the OID that
defines internet resources. The`  2  `or`  mgmt  `that follows is for a
management subcategory. The `1` or `mib-2` under that defines the MIB-2
specification. And finally, the 1 or system is the parent for a number
of child objects (sysDescr, sysObjectID, sysUpTime, sysContact, sysName,
sysLocation, sysServices, and so on).

## Getting Started

The simplest use case for using SNMP consists of creating a readonly
community password and enabling a listening address for the loopback
address (this is the default listening-address provided). This allows
for testing functionality of `snmpd` before extending the listening
addresses to IP addresses reachable from outside the switch or router.
This first sample configuration adds a listening address on the loopback
interface (this is not a change from the default so we get a message
stating that the configuration has not changed), sets a simple community
password (SNMPv2) for testing, changes the system-name object in the
system table, commits the change, checks the status of `snmpd`, and gets
the first MIB object in the system table:

    cumulus@router1:~$ net add snmp-server listening-address localhost
    Configuration has not changed
    cumulus@router1:~$ net add snmp-server readonly-community mynotsosecretpassword access any
    cumulus@router1:~$ net add snmp-server system-name my little router
    cumulus@router1:~$ net commit

    cumulus@router1:~$ net show snmp-server status

    Simple Network Management Protocol (SNMP) Daemon.
    ---------------------------------  ----------------
    Current Status                     active (running)
    Reload Status                      enabled
    Listening IP Addresses             localhost
    Main snmpd PID                     13669
    Version 1 and 2c Community String  Configured
    Version 3 Usernames                Not Configured
    ---------------------------------  ----------------

    cumulus@router1:~$ snmpgetnext -v 2c -c mynotsosecretpassword localhost SNMPv2-MIB::sysName
    SNMPv2-MIB::sysName.0 = STRING: my little router

## Configure SNMP

For external SNMP NMS systems to poll Cumulus Linux switches and
routers, you must configure the SNMP agent (snmpd) running on the switch
with one or more IP addresses (with `net add snmp-server
listening-address <ip>`) on which the agent listens. You must configure
these IP addresses on interfaces that have link state UP. By default,
the SNMP configuration has a listening address of localhost (or
127.0.0.1), which allows the daemon to respond to SNMP requests
originating on the switch itself. This is a useful method of checking
the configuration for SNMP without exposing the switch to attacks from
the outside. The only other required configuration is a readonly
community password (configured with `net add snmp-server
readonly-community <password> access <ip | any>``)`, that allows polling
of the various MIB objects on the device itself. SNMPv3 is recommended
since SNMPv2c (with a community string) exposes the password in the
`GetRequest` and `GetResponse` packets. SNMPv3 does not expose the
username passwords and has the option of encrypting the packet contents.

{{%notice note%}}

If you intend to run this service within a
[VRF](../../Layer-3/Virtual-Routing-and-Forwarding-VRF/),
including the [management VRF](../../Layer-3/Management-VRF/), follow
[these steps](../../Layer-3/Management-VRF/#run-services-within-the-management-vrf)
for configuring the service.

{{%/notice%}}

{{%notice info%}}

Cumulus Linux 3.4 and later releases support configuring SNMP with NCLU.
While NCLU does not provide functionality to configure every single
`snmpd` feature, it is the recommended method of configuring `snmpd`.
You are not restricted to using NCLU for configuration and can edit the
`/etc/snmp/snmpd.conf` file and control `snmpd` with `systemctl`
commands. For Cumulus Linux versions earlier than 3.0, `snmpd` has a
default configuration that listens to incoming requests on all
interfaces.

{{%/notice%}}

{{%notice info%}}

Cumulus Linux 3.6 and later releases support configuring VRFs for
listening-addresses as well as Trap/Inform support. If management VRF is
enabled on the switch, this places the eth0 interface in the management
VRF. When configuring the listening-address for snmp-server, you must
specify an additional parameter to enable listening on the eth0
interface with the following command:

`cumulus@router1:~$ net add snmp-server listening-address 10.10.10.10
vrf mgmt`

These additional parameters are described in detail below.

{{%/notice%}}

{{%notice note%}}

You must add a default community string for v1 or v2c environments or
the `snmpd` daemon does not respond to any requests. For security
reasons, the default configuration configures `snmpd` to listen to SNMP
requests on the loopback interface so access to the switch is restricted
to requests originating from the switch itself. The only required
commands for `snmpd` to function are a `listening-address` and either a
`username` or a`  readonly-community ` string.

{{%/notice%}}

### Configure SNMP with NCLU

The table below highlights the structure of NCLU commands available for
configuring SNMP. An example command set is provided below the table.
NCLU restarts the `snmpd` daemon after configuration changes are made
and committed.

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Command</p></th>
<th><p>Summary</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><code>net del all</code> or <code>net del snmp-server all</code></p></td>
<td><p>Removes all entries in the <code>/etc/snmp/snmpd.conf</code> file and replaces them with defaults. The defaults remove all SNMPv3 usernames, readonly-communities, and a listening-address of localhost is configured.</p></td>
</tr>
<tr class="even">
<td><p><code>net add snmp-server listening-address (localhost|localhost-v6)</code></p></td>
<td><p>For security reasons, the localhost is set to a listening address 127.0.0.1 by default so that the SNMP agent only responds to requests originating on the switch itself. You can also configure listening only on the IPv6 localhost address with localhost-v6. When using IPv6 addresses or localhost, you can use a <code>readonly-community-v6</code> for v1 and v2c requests. For v3 requests, you can use the <code>username</code> command to restrict access.</p>
<pre><code>net add snmp-server listening-address localhost
net add snmp-server listening-address localhost-v6</code></pre></td>
</tr>
<tr class="odd">
<td><p><code>net add snmp-server listening-address (all|all-v6)</code></p></td>
<td><p>Configures the <code>snmpd</code> agent to listen on all interfaces for either IPv4 or IPv6 UDP port 161 SNMP requests. This command removes all other individual IP addresses configured.</p>
<p>Note: This command does not allow <code>snmpd</code> to cross VRF table boundaries. To listen on IP addresses in different VRF tables, use multiple listening-address commands each with a VRF name, as shown below.</p>
<pre><code>net add snmp-server listening-address all
net add snmp-server listening-address all-v6</code></pre></td>
</tr>
<tr class="even">
<td><p><code>net add snmp-server listening-address IP_ADDRESS IP_ADDRESS ...</code></p></td>
<td><p>Sets <code>snmpd</code> to listen to a specific IPv4 or IPv6 address, or a group of addresses with space separated values, for incoming SNMP queries. If VRF tables are used, be sure to specify an IP address with an associated VRF name, as shown below. If you omit a VRF name, the default VRF is used.</p>
<pre><code>net add snmp-server listening-address 10.10.10.10</code></pre>
<pre><code>net add snmp-server listening-address 10.10.10.10 44.44.44.44</code></pre></td>
</tr>
<tr class="odd">
<td><p><code>net add snmp-server listening-address IP_ADDRESS vrf VRF_NAME</code></p></td>
<td><p>Sets <code>snmpd</code> to listen to a specific IPv4 or IPv6 address on an interface within a particular VRF. With VRFs, identical IP addresses can exist in different VRF tables. This command restricts listening to a particular IP address within a particular VRF. If the VRF name is not given, the default VRF is used.</p>
<pre><code>net add snmp-server listening-address 10.10.10.10 vrf mgmt</code></pre></td>
</tr>
<tr class="even">
<td><p><code>net add snmp-server username [user name] (auth-none|auth-md5|auth-sha) &lt;authentication password&gt; [(encrypt-des|encrypt-aes) &lt;encryption password&gt;] (oid &lt;OID&gt;|view &lt;view name&gt;)</code></p></td>
<td><p>Creates an SNMPv3 username and the necessary credentials for access. You can restrict a user to a particular OID tree or predefined view name if these are specified. If you specify auth-none, no authentication password is required. Otherwise, an MD5 or SHA password is required for access to the MIB objects. If specified, an encryption password is used to hide the contents of the request and response packets.</p>
<pre><code>net add snmp-server username testusernoauth  auth-none
net add snmp-server username testuserauth    auth-md5  myauthmd5password
net add snmp-server username testuserboth    auth-md5  mynewmd5password   encrypt-aes  myencryptsecret
net add snmp-server username limiteduser1    auth-md5  md5password1       encrypt-aes  myaessecret       oid 1.3.6.1.2.1.1</code></pre></td>
</tr>
<tr class="odd">
<td><p><code>net add snmp-server viewname [view name] (included | excluded) [OID or name]</code></p></td>
<td><p>Creates a view name that is used in readonly-community to restrict MIB tree exposure. By itself, this view definition has no effect; however, when linked to an SNMPv3 username or community password, and a host from a restricted subnet, any SNMP request with that username and password must have a source IP address within the configured subnet.</p>
<p>Note: OID can be either a string of period separated decimal numbers or a unique text string that identifies an SNMP MIB object. Some MIBs are not installed by default; you must install them either by hand or with the latest Debian package called snmp-mibs-downloader. You can remove specific view name entries with the delete command or with just a view name to remove all entries matching that view name. You can define a specific view name multiple times and fine tune to provide or restrict access using the included or excluded command to specify branches of certain MIB trees.</p>
<pre><code>net add snmp-server viewname cumulusOnly included .1.3.6.1.4.1.40310
net add snmp-server viewname cumulusCounters included .1.3.6.1.4.1.40310.2
 
net add snmp-server readonly-community simplepassword access any view cumulusOnly
net add snmp-server username testusernoauth  auth-none view cumulusOnly
net add snmp-server username limiteduser1    auth-md5  md5password1 encrypt-aes  myaessecret  view cumulusCounters</code></pre></td>
</tr>
<tr class="even">
<td><p><code>net add snmp-server (readonly-community | readonly-community-v6) [password] access (any | localhost | [network]) [(view [view name]) or [oid [oid or name])</code></p></td>
<td><p>This command defines the password required for SNMP version 1 or 2c requests for GET or GETNEXT. By default, this provides access to the full OID tree for such requests, regardless of from where they were sent. There is no default password set, so <code>snmpd</code> does not respond to any requests that arrive. Users often specify a source IP address token to restrict access to only that host or network given. You can specify a view name to restrict the subset of the OID tree.</p>
<p>Examples of <code>readonly-community </code>commands are shown below. The first command sets the read only community string to <code>simplepassword</code> for SNMP requests and this restricts requests to those sourced from hosts in the 10.10.10.0/24 subnet and restricts viewing to the <em>mysystem</em> view name defined with the <code>viewname</code> command. The second example creates a read-only community password <em>showitall</em> that allows access to the entire OID tree for requests originating from any source IP address.</p>
<pre><code>net add snmp-server viewname mysystem included 1.3.6.1.2.1.1
net add snmp-server readonly-community simplepassword access 10.10.10.0/24 view mysystem
 
net add snmp-server readonly-community showitall access any</code></pre></td>
</tr>
<tr class="odd">
<td><p><code>net add snmp-server trap-destination (localhost | [ipaddress]) [vrf vrf name] community-password [password] [version [1 | 2c]]</code></p></td>
<td><p>For SNMP versions 1 and 2C, this command sets the SNMP Trap destination IP address. Multiple destinations can exist, but you must set up at least one to enable SNMP Traps to be sent. Removing all settings disables SNMP traps. The default version is 2c, unless otherwise configured. You must include a VRF name with the IP address to force Traps to be sent in a non-default VRF table.</p>
<pre><code>net add snmp-server trap-destination 10.10.10.10 community-password mynotsosecretpassword version 1
net add snmp-server trap-destination 20.20.20.20 vrf mgmt community-password mymanagementvrfpassword version 2c
 </code></pre></td>
</tr>
<tr class="even">
<td><p><code>net add snmp-server trap-destination (localhost | [ipaddress]) [vrf vrf name] username &lt;v3 username&gt; (auth-md5|auth-sha) &lt;authentication password&gt; [(encrypt-des|encrypt-aes) &lt;encryption password&gt;] engine-id &lt;text&gt; [inform]</code></p></td>
<td><p>For SNMPv3 Trap and Inform messages, this command configures the trap destination IP address (with an optional VRF name). You must define the authentication type and password. The encryption type and password are optional. You must specify the engine ID/user name pair. The <code>inform </code>keyword is used to specify an Inform message where the SNMP agent waits for an acknowledgement.</p>
<p>For Traps, the engine ID/user name is for the CL switch <strong>sending</strong> the traps. This can be found at the end of the <code>/var/lib/snmp/snmpd.conf</code> file labelled <code>oldEngineID</code>. Configure this same engine ID/user name (with authentication and encryption passwords) for the Trap daemon receiving the trap to validate the received Trap.</p>
<pre><code>net add snmp-server trap-destination 10.10.10.10 username myv3userrsion auth-md5 md5password1 encrypt-aes myaessecret engine-id  0x80001f888070939b14a514da5a00000000
net add snmp-server trap-destination 20.20.20.20 vrf mgmt username mymgmtvrfusername auth-md5 md5password2 encrypt-aes myaessecret2 engine-id  0x80001f888070939b14a514da5a00000000</code></pre>
<p>For Inform messages (Informs are acknowledged version 3 Traps), the engine ID/user name is the one used to create the username on the <strong>receiving Trap daemon server</strong>. The Trap receiver sends the response for the Trap message using its own engine ID/user name. In practice, the trap daemon generates the usernames with its own engine ID and after these are created, the SNMP server (or agent) needs to use these engine ID/user names when configuring the Inform messages so that they are correctly authenticated and the correct response is sent to the <code>snmpd</code> agent that sent it.</p>
<pre><code>net add snmp-server trap-destination 10.10.10.10 username myv3userrsion auth-md5 md5password1 encrypt-aes myaessecret engine-id  0x80001f888070939b14a514da5a00000000 inform
net add snmp-server trap-destination 20.20.20.20 vrf mgmt username mymgmtvrfusername auth-md5 md5password2 encrypt-aes myaessecret2 engine-id  0x80001f888070939b14a514da5a00000000 inform</code></pre></td>
</tr>
<tr class="odd">
<td><p><code>net add snmp-server trap-link-up [check-frequency [seconds]]</code></p></td>
<td><p>Enables notifications for interface link-up to be sent to SNMP Trap destinations.</p>
<pre><code>net add snmp-server trap-link-up check-frequency 15</code></pre></td>
</tr>
<tr class="even">
<td><p><code>net add snmp-server trap-link-down [check-frequency [seconds]]</code></p></td>
<td><p>Enables notifications for interface link-down to be sent to SNMP Trap destinations.</p>
<pre><code>net add snmp-server trap-link-down check-frequency 10</code></pre></td>
</tr>
<tr class="odd">
<td><p><code>net add snmp-server trap-snmp-auth-failures</code></p></td>
<td><p>Enables SNMP Trap notifications to be sent for every SNMP authentication failure.</p>
<pre><code>net add snmp-server trap-snmp-auth-failures</code></pre></td>
</tr>
<tr class="even">
<td><p><code>net add snmp-server trap-cpu-load-average one-minute [threshold] five-minute [5-min-threshold]</code></p>
<p><code>fifteen-minute [15-min-threshold]</code></p></td>
<td><p>Enables a trap when the cpu-load-average exceeds the configured threshold. You can only use integers or floating point numbers.</p>
<pre><code>net add snmp-server trap-cpu-load-average one-minute 4.34 five-minute 2.32 fifteen-minute 6.5</code></pre></td>
</tr>
</tbody>
</table>

This table describes system setting configuration commands for
SNMPv2-MIB.

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Command</p></th>
<th><p>Summary</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><code>net add snmp-server system-location [string]</code></p></td>
<td><p>Sets the system physical location for the node in the SNMPv2-MIB system table.</p>
<pre><code>net add snmp-server system-location  My private bunker</code></pre></td>
</tr>
<tr class="even">
<td><p><code>net add snmp-server system-contact [string]</code></p></td>
<td><p>Sets the identification of the contact person for this managed node, together with information on how to contact this person.</p>
<pre><code>net add snmp-server system-contact user X at myemail@example.com</code></pre></td>
</tr>
<tr class="odd">
<td><p><code>net add snmp-server system-name [string]</code></p></td>
<td><p>Sets an administratively-assigned name for the managed node. By convention, this is the fully-qualified domain name of the node.</p>
<pre><code>net add snmp-server system-name CumulusBox number 1,543,567</code></pre></td>
</tr>
</tbody>
</table>

The example commands below enable an SNMP agent to listen on all IPv4
addresses with a community string password, set the trap destination
host IP address, and create four types of SNMP traps.

    cumulus@switch:~$ net add snmp-server listening-address all
    cumulus@switch:~$ net add snmp-server readonly-community tempPassword access any
    cumulus@switch:~$ net add snmp-server trap-destination 1.1.1.1 community-password mypass version 2c
    cumulus@switch:~$ net add snmp-server trap-link-up check-frequency 15
    cumulus@switch:~$ net add snmp-server trap-link-down check-frequency 10
    cumulus@switch:~$ net add snmp-server trap-cpu-load-average one-minute 7.45 five-minute 5.14
    cumulus@switch:~$ net add snmp-server trap-snmp-auth-failures

## Configure SNMP Manually

If you need to manually edit the SNMP configuration; for example, if the
necessary option has not been implemented in NCLU, you need to edit the
configuration directly, which is stored in the `/etc/snmp/snmpd.conf`
file.

Use caution when editing this file. The next time you use NCLU to update
your SNMP configuration, if NCLU is unable to correctly parse the
syntax, some of the options might be overwritten.

Make sure you do not delete the `snmpd.conf` file; this can cause issues
with the package manager the next time you update Cumulus Linux.

The SNMP daemon, `snmpd`, uses the `/etc/snmp/snmpd.conf` configuration
file for most of its configuration. The syntax of the most important
keywords are defined in the following table.

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Syntax</p></th>
<th><p>Meaning</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><strong>agentaddress</strong></p></td>
<td><p><strong>Required.</strong> This command sets the protocol, IP address, and the port for <code>snmpd</code> to listen for <strong>incoming</strong> requests. The IP address must exist on an interface that has link UP on the switch where <code>snmpd</code> is being used. By default, this is set to <em>udp:127.0.0.1:161</em>, which means <code>snmpd</code> listens on the loopback interface and only responds to requests (<code>snmpwalk</code>, <code>snmpget</code>, <code>snmpgetnext</code>) originating from the switch. A wildcard setting of <em>udp:161,udp6:161</em> forces <code>snmpd</code> to listen on all IPv4 and IPv6 interfaces for incoming SNMP requests. You can configure multiple IP addresses as comma-separated values; for example, <em>udp:66.66.66.66:161,udp:77.77.77.77:161,udp6:[2001::1]:161.</em> You can use multiple lines to define listening addresses. To bind to a particular IP address within a particular VRF table, follow the IP address with a <code>@</code> and the name of the VRF table (for example, <code>10.10.10.10@mgmt</code>).</p></td>
</tr>
<tr class="even">
<td><p><strong>rocommunity</strong></p></td>
<td><p><strong>Required.</strong> This command defines the password that is required for SNMP version 1 or 2c requests for GET or GETNEXT. By default, this provides access to the full OID tree for such requests, regardless of from where they were sent. There is no default password set, so <code>snmpd</code> does not respond to any requests that arrive. Specify a source IP address token to restrict access to only that host or network given. Specify a view name (as defined above) to restrict the subset of the OID tree.</p>
<p>Examples of <code>rocommunity</code> commands are shown below. The first command sets the read only community string to <code>simplepassword</code> for SNMP requests sourced from the 10.10.10.0/24 subnet and restricts viewing to the <em>systemonly</em> view name defined previously with the <code>view</code> command. The second example creates a read-only community password that allows access to the entire OID tree from any source IP address.</p>
<pre><code>rocommunity simplepassword 10.10.10.0/24 -V systemonly
 
rocommunity cumulustestpassword</code></pre></td>
</tr>
<tr class="odd">
<td><p><strong>view</strong></p></td>
<td><p>This command defines a view name that specifies a subset of the overall OID tree. You can reference this restricted view by name in the <code>rocommunity</code> command to link the view to a password that is used to see this restricted OID subset. By default, the <code>snmpd.conf</code> file contains numerous views with the <em>systemonly</em> view name.</p>
<pre><code>view   systemonly  included   .1.3.6.1.2.1.1
 
view   systemonly  included   .1.3.6.1.2.1.2
 
view   systemonly  included   .1.3.6.1.2.1.3 </code></pre>
<p>The <em>systemonly</em> view is used by <code>rocommunity</code> to create a password for access to only these branches of the OID tree.</p></td>
</tr>
<tr class="even">
<td><p><strong>trapsink</strong></p>
<p><strong>trap2sink</strong></p></td>
<td><p>This command defines the IP address of the notification (or trap) receiver for either SNMPv1 traps or SNMPv2 traps. If you specify several sink directives, multiple copies of each notification (in the appropriate formats) are generated. You must configure a trap server to receive and decode these trap messages (for example, <code>snmptrapd</code>). You can configure the address of the trap receiver with a different protocol and port but this is most often left out. The defaults are to use the well-known UDP packets and port 162.</p></td>
</tr>
<tr class="odd">
<td><p><strong>createuser</strong></p>
<p><strong>iquerysecName</strong></p>
<p><strong>rouser</strong></p></td>
<td><p>These three commands define an internal SNMPv3 username that is required for <code>snmpd</code> to send traps. This username is required to authorize the DisMan service even though SNMPv3 is not being configured for use. The example <code>snmpd.conf</code> configuration shown below creates <em>snmptrapusernameX</em> as the username (this is just an example username) using the <code>createUser</code> command. <code>iquerysecname</code> defines the default SNMPv3 username to be used when making internal queries to retrieve monitored expressions. <code>rouser</code> specifies the username for these SNMPv3 queries. All three are required for <code>snmpd</code> to retrieve information and send built-in traps or for those configured with the <code>monitor</code> command shown below in the examples.</p>
<pre><code>createuser snmptrapusernameX
 
iquerysecname snmptrapusernameX
 
rouser snmptrapusernameX</code></pre></td>
</tr>
<tr class="even">
<td><p><strong>linkUpDownNotifications yes</strong></p></td>
<td><p>This command enables link up and link down trap notifications, assuming the other trap configurations settings are set. This command configures the Event MIB tables to monitor the ifTable for network interfaces being taken up or down, and triggering a <em>linkUp</em> or <em>linkDown</em> notification as appropriate. This is equivalent to the following configuration:</p>
<pre><code>notificationEvent  linkUpTrap    linkUp   ifIndex ifAdminStatus ifOperStatus
 
notificationEvent  linkDownTrap  linkDown ifIndex ifAdminStatus ifOperStatus
 
monitor  -r 60 -e linkUpTrap   &quot;Generate linkUp&quot; ifOperStatus != 2
 
monitor  -r 60 -e linkDownTrap &quot;Generate linkDown&quot; ifOperStatus == 2</code></pre></td>
</tr>
<tr class="odd">
<td><p><strong>defaultMonitors yes</strong></p></td>
<td><p>This command configures the Event MIB tables to monitor the various UCD-SNMP-MIB tables for problems (as indicated by the appropriate xxErrFlag column objects) and send a trap. This assumes you have downloaded the <code>snmp-mibs-downloader</code> Debian package and commented out <code>mibs</code> from the <code>/etc/snmp/snmp.conf</code> file (#mibs). This command is exactly equivalent to the following configuration:</p>
<pre><code>monitor   -o prNames -o prErrMessage &quot;process table&quot; prErrorFlag != 0
 
monitor   -o memErrorName -o memSwapErrorMsg &quot;memory&quot; memSwapError != 0
 
monitor   -o extNames -o extOutput &quot;extTable&quot; extResult != 0
 
monitor   -o dskPath -o dskErrorMsg &quot;dskTable&quot; dskErrorFlag != 0
 
monitor   -o laNames -o laErrMessage  &quot;laTable&quot; laErrorFlag != 0
 
monitor   -o fileName -o fileErrorMsg  &quot;fileTable&quot; fileErrorFlag != 0</code></pre></td>
</tr>
</tbody>
</table>

### Start the SNMP Daemon

Use the recommended process described below to start `snmpd` and monitor
it using `systemctl`.

{{%notice note%}}

As mentioned above, if you intend to run this service within a
[VRF](../../Layer-3/Virtual-Routing-and-Forwarding-VRF/),
including the [management VRF](../../Layer-3/Management-VRF/), follow
[these steps](../../Layer-3/Management-VRF/#run-services-within-the-management-vrf)
for configuring the service.

{{%/notice%}}

To start the SNMP daemon:

1.  Start the `snmpd` daemon:

        cumulus@switch:~$ sudo systemctl start snmpd.service

2.  Configure the `snmpd` daemon to start automatically after reboot:

        cumulus@switch:~$ sudo systemctl enable snmpd.service

3.  To enable `snmpd` to restart automatically after failure:

    1.  Create a file called
        `/etc/systemd/system/snmpd.service.d/restart.conf`.

    2.  Add the following lines:

            [Service]
            Restart=always
            RestartSec=60

    3.  Run `sudo systemctl daemon-reload`.

After the service starts, you can use SNMP to manage various components
on the switch.

### Configure SNMP with Management VRF (used prior to Cumulus Linux 3.6)

When you configure [Management
VRF](../../Layer-3/Management-VRF/), you need to be aware of the
interface IP addresses on which SNMP is listening. If you set
listening-address to all, the `snmpd` daemon responds to incoming
requests on all interfaces that are in the default VRF. If you prefer to
listen on a limited number of IP addresses, Cumulus Networks recommends
that you run only one instance of the `snmpd` daemon and specify the VRF
name along with the listening-address. You can configure IP addresses in
different VRFs and a single SNMP daemon listens on multiple IP addresses
each with its own VRF. Because SNMP has native VRF awareness, using
systemctl commands to manage snmpd in different VRFs is no longer
necessary.

SNMP configuration in NCLU is VRF aware so you can configure the `snmpd`
daemon to listen to incoming SNMP requests on a particular IP address
within particular VRFs. Because interfaces in a particular VRF (routing
table) are not aware of interfaces in a different VRF, the `snmpd`
daemon only responds to polling requests and sends traps on the
interfaces of the VRF on which it is configured.

When management VRF is configured, configure the listening-address with
a VRF name as shown above. This allows snmpd to receive and respond to
SNMP polling requests on eth0.

Prior to Cumulus Linux 3.6, you could not configure a VRF name in the
listening-address or the trap-destination commands. To manually handle
VRF functionality, you had to do the following:

1.  Configure all the required SNMP settings with NCLU. Pay particular
    attention to the listening-address configuration setting, which
    should contain one or more IP addresses that belong to interfaces
    within a single VRF (if management VRF is configured, this is
    typically the IP address of eth0 ). You can use IP addresses other
    than eth0, but the interfaces for these IP addresses must be in the
    same VRF (typically the management VRF).

2.  Commit the changes to start the `snmpd` daemon in the default VRF.

3.  Manually stop the `snmpd` daemon from running in the default VRF.

4.  Manually restart the `snmpd` daemon in the management VRF.

{{%notice info%}}

**Running Multiple Instances of snmpd**

Prior to Cumulus Linux 3.6, more complex configurations may have been
needed; for example, you can run more than one `snmpd` daemon (one in
each VRF designed to receive SNMP polling requests). Cumulus Networks
does not recommend this for memory and CPU resource reasons. However, if
this is required, you must use a separate configuration file with each
instance of the `snmpd` daemon. You can use a copy of the
`/etc/snmp/snmpd.conf` file. When you use this file, start an `snmpd`
daemon with the following command:

    cumulus@switch:~$ sudo /usr/sbin/snmpd -y -LS 0-4 d -Lf /dev/null -u snmp -g snmp -I -smux -p /run/snmpd.pid -C -c <new snmp config filename> (edited)

{{%/notice%}}

To use management VRF, you need to configure the IP address of eth0 as
the listening-address. In the example below, eth0 IP address is
10.10.10.10. You can also add other `snmp-server` configurations, then
commit the changes.

    cumulus@switch:~$ net add snmp-server listening-address 10.10.10.10
    cumulus@switch:~$ net add snmp-server readonly-community tempPassword access any
    cumulus@switch:~$ net pending
    cumulus@switch:~$ net commit

This restarts the `snmpd` daemon in the default VRF. Then, to run
`snmpd` in the correct VRF, stop the daemon in the default VRF (or stop
any other `snmpd` daemons that happen to be running), then restart
`snmpd` in the management VRF so that it can respond to requests on
interfaces only in that VRF. Make sure that only one instance of the
`snmpd` daemon is running and that it is running in the desired VRF.
Assuming the Management VRF has been enabled, the following example
shows how to stop `snmpd` and restart it in the management VRF.

    cumulus@switch:mgmt-vrf:~$ systemctl stop snmpd.service
    cumulus@switch:mgmt-vrf:~$ systemctl disable snmpd.service
    cumulus@switch:mgmt-vrf:~$ ps aux | grep snmpd
    cumulus@switch:mgmt-vrf:~$
    cumulus@switch:mgmt-vrf:~$ systemctl start snmpd@mgmt.service
    cumulus@switch:mgmt-vrf:~$ systemctl enable snmpd.service
    cumulus@switch:mgmt-vrf:~$ systemctl status snmpd@mgmt.service
    root@switch:mgmt-vrf:/home/cumulus# systemctl status snmpd@mgmt.service                                                                                                                                                                                                                                                                               ● snmpd@mgmt.service - Simple Network Management Protocol (SNMP) Daemon.                                                                                                                                                                                                                                                                                       Loaded: loaded (/lib/systemd/system/snmpd.service; disabled)                                                                                                                                                                                                                                                                                               Drop-In: /run/systemd/generator/snmpd@.service.d                                                                                                                                                                                                                                                                                                                     └─vrf.conf
       Active: active (running) since Thu 2017-12-07 20:05:41 UTC; 2min 22s ago                                                                                                                                                                                                                                                                                  Main PID: 30880 (snmpd)
       CGroup: /system.slice/system-snmpd.slice/snmpd@mgmt.service                                                                                                                                                                                                                                                                                                         └─30880 /usr/sbin/snmpd -y -LS 0-4 d -Lf /dev/null -u snmp -g snmp -I -smux -p /run/snmpd.pid -f
                                                                                                                                                                                                                                                                                                                                                                Dec 07 20:05:41 cel-redxp-01 systemd[1]: Started Simple Network Management Protocol (SNMP) Daemon..
     
    cumulus@switch:mgmt-vrf:~$ ps aux | grep snmpd
    snmp     30880  0.4  0.3  57176 12276 ?        Ss   20:05   0:00 /usr/sbin/snmpd -y -LS 0-4 d -Lf /dev/null -u snmp -g snmp -I -smux -p /run/snmpd.pid -f

### Set up the Custom Cumulus Networks MIBs

No changes are required in the `/etc/snmp/snmpd.conf` file on the switch
to support the custom Cumulus Networks MIBs. The following lines are
already included by default and provide support for both the Cumulus
Counters and the Cumulus Resource Query MIBs.

    sysObjectID 1.3.6.1.4.1.40310
    pass_persist .1.3.6.1.4.1.40310.1 /usr/share/snmp/resq_pp.py
    pass_persist .1.3.6.1.4.1.40310.2 /usr/share/snmp/cl_drop_cntrs_pp.py

However, you need to copy several files to the NMS server for the custom
Cumulus MIB to be recognized on NMS server.

  - `/usr/share/snmp/mibs/Cumulus-Snmp-MIB.txt`

  - `/usr/share/snmp/mibs/Cumulus-Counters-MIB.txt`

  - `/usr/share/snmp/mibs/Cumulus-Resource-Query-MIB.txt`

### Set the Community String

The `snmpd` authentication for versions 1 and 2 is disabled by default
in Cumulus Linux. You can enable this password (called a community
string) by setting **rocommunity** (for read-only access) or
**rwcommunity** (for read-write access). Setting a community string is
required.

To enable read-only querying by a client:

1.  Open the `/etc/snmp/snmpd.conf` file in a text editor.

2.  To allow read-only access, uncomment the following line, then save
    the file:

        rocommunity public default -V systemonly

    <table>
    <colgroup>
    <col style="width: 50%" />
    <col style="width: 50%" />
    </colgroup>
    <thead>
    <tr class="header">
    <th><p>Keyword</p></th>
    <th><p>Meaning</p></th>
    </tr>
    </thead>
    <tbody>
    <tr class="odd">
    <td><p>rocommunity</p></td>
    <td><p>Read-only community; <em>rwcommunity</em> is for read-write access.</p></td>
    </tr>
    <tr class="even">
    <td><p>public</p></td>
    <td><p>Plain text password/community string.</p>
    <p>{{%notice warning%}}</p>
    <p>Cumulus Networks strongly recommends you change this password to something else.</p>
    <p>{{%/notice%}}</p></td>
    </tr>
    <tr class="odd">
    <td><p>default</p></td>
    <td><p>The <em>default</em> keyword allows connections from any system. The <em>localhost</em> keyword allows requests only from the local host. A restricted source can either be a specific hostname (or address), or a subnet, represented as IP/MASK (like 10.10.10.0/255.255.255.0), or IP/BITS (like 10.10.10.0/24), or the IPv6 equivalents.</p></td>
    </tr>
    <tr class="even">
    <td><p>systemonly</p></td>
    <td><p>The name of this particular SNMP view. This is a user-defined value.</p></td>
    </tr>
    </tbody>
    </table>

3.  Restart `snmpd`:

        cumulus@switch:~$ sudo systemctl restart snmpd.service

## Enable SNMP Support for FRRouting

SNMP supports Routing MIBs in
[FRRouting](../../Layer-3/FRRouting-Overview/). To enable SNMP
support for FRRouting, you need to:

  - Configure [AgentX](http://www.net-snmp.org/docs/README.agentx.html)
    (ASX) access in FRRouting

  - The default `/etc/snmp/snmpd.conf` configuration already enables
    agentx and sets the correct permissions

Enabling FRRouting includes support for BGP. However, if you plan on
using the BGP4 MIB, be sure to provide access to the MIB tree
1.3.6.1.2.1.15.

{{%notice note%}}

At this time, SNMP does not support monitoring BGP unnumbered neighbors.

{{%/notice%}}

If you plan on using the OSPFv2 MIB, provide access to 1.3.6.1.2.1.14
and to 1.3.6.1.2.1.191 for the OSPv3 MIB.

To enable SNMP support for FRRouting:

1.  Configure AgentX access in FRRouting:

        cumulus@switch:~$ net add routing agentx
        cumulus@switch:~$ net pending
        cumulus@switch:~$ net commit

2.  Update the SNMP configuration to enable FRRouting to respond to SNMP
    requests. Open the `/etc/snmp/snmpd.conf` file in a text editor and
    verify that the following configuration exists:

        agentxsocket /var/agentx/master
        agentxperms 777 777 snmp snmp
        master agentx

    {{%notice note%}}

Make sure that the `/var/agentx` directory is world-readable and
    world-searchable (octal mode 755).

    {{%/notice%}}

3.  Optionally, you might need to expose various MIBs:

      - For the BGP4 MIB, allow access to `1.3.6.1.2.1.15`

      - For the OSPF MIB, allow access to `1.3.6.1.2.1.14`

      - For the OSPFV3 MIB, allow access to `1.3.6.1.2.1.191`

To verify the configuration, run `snmpwalk`. For example, if you have a
running OSPF configuration with routes, you can check this OSPF-MIB
first from the switch itself with:

    cumulus@switch:~$ sudo snmpwalk -v2c -cpublic localhost 1.3.6.1.2.1.14

### Enable the .1.3.6.1.2.1 Range

Some MIBs, including storage information, are not included by default in
`snmpd.conf` in Cumulus Linux. This results in some default views on
common network tools (like `librenms`) to return less than optimal data.
You can include more MIBs by enabling all the .1.3.6.1.2.1 range. This
simplifies the configuration file, removing concern that any required
MIBs will be missed by the monitoring system. Various MIBs were added to
version 3.0 and include the following: ENTITY and ENTITY-SENSOR MIB and
parts of the BRIDGE-MIB and Q-BRIDGE-MIBs. These are included in the
default configuration.

{{%notice warning%}}

This configuration grants access to a large number of MIBs, including
all SNMPv2-MIB, which might reveal more data than expected. In addition
to being a security vulnerability, it might consume more CPU resources.

{{%/notice%}}

To enable the .1.3.6.1.2.1 range, make sure the view name commands
include the required MIB objects.

### Configure SNMPv3

SNMPv3 is often used to enable authentication and encryption, as
community strings in versions 1 and 2c are sent in plaintext. SNMPv3
usernames are added to the `/etc/snmp/snmpd.conf` file, along with
plaintext authentication and encryption pass phrases.

{{%notice note%}}

Cumulus Networks recommends that you configure SNMPv3 usernames and
passwords with NCLU. However, if you prefer to edit the
`/etc/snmp/snmpd.conf` manually instead, be aware that `snmpd` caches
SNMPv3 usernames and passwords in the /`var/lib/snmp/snmpd.conf` file.
Make sure you stop `snmpd` and remove the old entries when making
changes. Otherwise, Cumulus Linux uses the old usernames and passwords
in the `/var/lib/snmp/snmpd.conf` file instead of the ones in the
`/etc/snmp/snmpd.conf` file.

{{%/notice%}}

The NCLU command structures for configuring SNMP user passwords are:

    cumulus@switch:~$ net add snmp-server username <username> [auth-none] | [(auth-md5 | auth-sha) <auth-password>]
    cumulus@switch:~$ net add snmp-server username <username> auth-(none | sha | md5)  (oid <OID> | view <view>)

The example below defines five users, each with a different combination
of authentication and encryption:

    cumulus@switch:~$ net add snmp-server username user1 auth-none
    cumulus@switch:~$ net add snmp-server username user2 auth-md5 user2password
    cumulus@switch:~$ net add snmp-server username user3 auth-md5 user3password encrypt-des user3encryption
    cumulus@switch:~$ net add snmp-server username user666 auth-sha user666password encrypt-aes user666encryption
    cumulus@switch:~$ net add snmp-server username user999 auth-md5 user999password encrypt-des user999encryption
    cumulus@switch:~$ net add snmp-server username user1 auth-none oid 1.3.6.1.2.1
    cumulus@switch:~$ net add snmp-server username user1 auth-none oid system 
    cumulus@switch:~$ net add snmp-server username user2 auth-md5 test1234 view testview  oid 1.3.6.1.2.1
    cumulus@switch:~$ net add snmp-server username user3 auth-sha testshax encrypt-aes testaesx oid 1.3.6.1.2.1
    cumulus@switch:~$ net pending
    cumulus@switch:~$ net commit

    # simple no auth user
    #createuser user1
     
    # user with MD5 authentication
    #createuser user2 MD5 user2password
     
    # user with MD5 for auth and DES for encryption
    #createuser user3 MD5 user3password DES user3encryption
     
    # user666 with SHA for authentication and AES for encryption
    createuser user666 SHA user666password AES user666encryption
     
    # user999 with MD5 for authentication and DES for encryption
    createuser user999 MD5 user999password DES user999encryption
     
    # restrict users to certain OIDs
    # (Note: creating rouser or rwuser will give
    # access regardless of the createUser command above. However,
    # createUser without rouser or rwuser will not provide any access).
    rouser user1 noauth 1.3.6.1.2.1
    rouser user2 auth 1.3.6.1.2.1
    rwuser user3 priv 1.3.6.1.2.1
    rwuser user666
    rwuser user999

After configuring user passwords and restarting the `snmpd` daemon, you
can check user access with a client.

{{%notice note%}}

The `snmp` Debian package contains `snmpget`, `snmpwalk`, and other
programs that are useful for checking daemon functionality from the
switch itself or from another workstation.

{{%/notice%}}

The following commands check the access for each user defined above from
the localhost:

    # check user1 which has no authentication or encryption (NoauthNoPriv)
    snmpget -v 3 -u user1 -l NoauthNoPriv localhost 1.3.6.1.2.1.1.1.0
    snmpwalk -v 3 -u user1 -l NoauthNoPriv localhost 1.3.6.1.2.1.1
     
    # check user2 which has authentication but no encryption (authNoPriv)
    snmpget -v 3 -u user2 -l authNoPriv -a MD5 -A user2password localhost 1.3.6.1.2.1.1.1.0
    snmpget -v 3 -u user2 -l authNoPriv -a MD5 -A user2password localhost 1.3.6.1.2.1.2.1.0
    snmpwalk -v 3 -u user2 -l authNoPriv -a MD5 -A user2password localhost 1.3.6.1.2.1

    # check user3 which has both authentication and encryption (authPriv)
    snmpget -v 3 -u user3 -l authPriv -a MD5 -A user3password -x DES -X user3encryption localhost .1.3.6.1.2.1.1.1.0
    snmpwalk -v 3 -u user3 -l authPriv -a MD5 -A user3password -x DES -X user3encryption localhost .1.3.6.1.2.1
    snmpwalk -v 3 -u user666 -l authPriv -a SHA -x AES -A user666password -X user666encryption localhost 1.3.6.1.2.1.1
    snmpwalk -v 3 -u user999 -l authPriv -a MD5 -x DES -A user999password -X user999encryption localhost 1.3.6.1.2.1.1

The following procedure shows a slightly more secure method of
configuring SNMPv3 users without creating cleartext passwords:

1.  Install the `net-snmp-config` script that is in `libsnmp-dev`
    package:

        cumulus@switch:~$ sudo -E apt-get update
        cumulus@switch:~$ sudo -E apt-get install libsnmp-dev

2.  Stop the daemon:

        cumulus@switch:~$ sudo systemctl stop snmpd.service

3.  Use the `net-snmp-config` command to create two users, one with MD5
    and DES, and the next with SHA and AES.

    {{%notice note%}}

The minimum password length is eight characters and the arguments
    `-a` and `-x` have different meanings in `net-snmp-config` than
    `snmpwalk`.

    {{%/notice%}}

        cumulus@switch:~$ sudo net-snmp-config --create-snmpv3-user -a md5authpass -x desprivpass -A MD5 -X DES userMD5withDES
        cumulus@switch:~$ sudo net-snmp-config --create-snmpv3-user -a shaauthpass -x aesprivpass -A SHA -X AES userSHAwithAES
        cumulus@switch:~$ sudo systemctl start snmpd.service

This adds a `createUser` command in `/var/lib/snmp/snmpd.conf`. Do
**not** edit this file by hand unless you are removing usernames. You
can edit this file and restrict access to certain parts of the MIB by
adding *noauth*, *auth* or *priv* to allow unauthenticated access,
require authentication, or to enforce use of encryption.

The `snmpd` daemon reads the information from the
`/var/lib/snmp/snpmd.conf` file and then the line is removed
(eliminating the storage of the master password for that user) and
replaced with the key that is derived from it (using the EngineID). This
key is a localized key, so that if it is stolen, it cannot be used to
access other agents. To remove the two users `userMD5withDES` and
`userSHAwithAES`, stop the `snmpd` daemon and edit the
`/var/lib/snmp/snmpd.conf` file. Remove the lines containing the
username, then restart the `snmpd` daemon as in step 3 above.

From a client, you access the MIB with the correct credentials. (The
roles of `-x`, `-a` and `-X` and `-A` are reversed on the client side as
compared with the `net-snmp-config` command used above.)

    snmpwalk -v 3 -u userMD5withDES -l authPriv -a MD5 -x DES -A md5authpass -X desprivpass localhost 1.3.6.1.2.1.1.1
    snmpwalk -v 3 -u userSHAwithAES -l authPriv -a SHA -x AES -A shaauthpass -X aesprivpass localhost 1.3.6.1.2.1.1.1

## Manually Configure SNMP Traps (Non-NCLU)

### Generate Event Notification Traps

The Net-SNMP agent provides a method to generate SNMP trap events using
the Distributed Management (DisMan) Event MIB for various system events,
including:

  - Link up/down.

  - Exceeding the temperature sensor threshold, CPU load, or memory
    threshold.

  - Other SNMP MIBs.

To enable specific types of traps, you need to create the following
configurations in `/etc/snmp/snmpd.conf`.

#### Define Access Credentials

An SNMPv3 username is required to authorize the DisMan service even
though you are not configuring SNMPv3 here. The example `snmpd.conf`
configuration shown below creates *trapusername* as the username using
the `createUser` command. `iquerySecName` defines the default SNMPv3
username to be used when making internal queries to retrieve monitored
expressions. `rouser` specifies which username to use for these SNMPv3
queries. All three are required for `snmpd` to retrieve information and
send traps (even with the `monitor` command shown below in the
examples). Add the following lines to your `/etc/snmp/snmpd.conf`
configuration file:

    createuser trapusername
    iquerysecname trapusername
    rouser trapusername

{{%notice note%}}

`iquerysecname` specifies the default SNMPv3 username to be used when
making internal queries to retrieve any necessary information — either
for evaluating the monitored expression or building a notification
payload. These internal queries always use SNMPv3, even if normal
querying of the agent is done using SNMPv1 or SNMPv2c. Note that this
user must also be explicitly created via `createUser` and given
appropriate access rights, for `rouser`, for example. The
`iquerysecname` directive is purely concerned with defining which user
should be used, not with actually setting this user up.

{{%/notice%}}

#### Define Trap Receivers

The following configuration defines the trap receiver IP address where
SNMPv2 traps are sent:

    trap2sink 192.168.1.1 public
    # For SNMPv1 Traps, use
    # trapsink  192.168.1.1  public

{{%notice note%}}

Although the traps are sent to an SNMPV2 receiver, the SNMPv3 user is
still required. Starting with Net-SNMP 5.3, `snmptrapd` no longer
accepts all traps by default. `snmptrapd` must be configured with
authorized SNMPv1/v2c community strings and/or SNMPv3 users.
Non-authorized traps/informs are dropped. Refer to the
[snmptrapd.conf(5) manual
page](http://www.net-snmp.org/docs/man/snmptrapd.conf.html) for details.

{{%/notice%}}

{{%notice note%}}

It is possible to define multiple trap receivers and to use the domain
name instead of an IP address in the `trap2sink` directive.

{{%/notice%}}

Restart the `snmpd` service to apply the changes.

    cumulus@switch:~$ sudo systemctl restart snmpd.service

#### SNMP Version 3 Trap and Inform Messages

You can configure SNMPv3 trap and inform messages with the ` trapsess
 `configuration command. Inform messages are traps that are acknowledged
by the receiving trap daemon. You configure inform messages with the`
-Ci  `parameter. You must specify the EngineID of the receiving trap
server with the `-e` field.

    trapsess -Ci -e 0x80ccff112233445566778899 -v3 -l authPriv  -u trapuser1 -a MD5 -A trapuser1password -x DES -X trapuser1encryption 192.168.1.1

The SNMP trap receiving daemon must have usernames, authentication
passwords, and encryption passwords created with its own EngineID. You
must configure this trap server EngineID in the switch `snmpd` daemon
sending the trap and inform messages. You specify the level of
authentication and encryption for SNMPv3 trap and inform messages with
`-l` (`NoauthNoPriv, authNoPriv,` or `authPriv`).

{{%notice note%}}

You can define multiple trap receivers and use the domain name instead
of an IP address in the `trap2sink` directive.

{{%/notice%}}

After you complete the configuration, restart the `snmpd` service to
apply the changes:

    cumulus@switch:~$ sudo systemctl restart snmpd.service

#### Source Traps from a Different Source IP Address

When client SNMP programs (such as `snmpget`, `snmpwalk`, or `snmptrap`)
are run from the command line, or when `snmpd` is configured to send a
trap (based on `snmpd.conf`), you can configure a *clientaddr* in
`snmp.conf` that allows the SNMP client programs or `snmpd` (for traps)
to source requests from a different source IP address.

{{%notice note%}}

`snmptrap`, `snmpget`, `snmpwalk` and `snmpd` itself must be able to
bind to this address.

{{%/notice%}}

For more information, read the the `snmp.conf` man page:

    clientaddr [<transport-specifier>:]<transport-address>
                  specifies the source address to be used by command-line applica‐
                  tions when sending SNMP requests. See snmpcmd(1) for more infor‐
                  mation about the format of addresses.
                  This value is also used by snmpd when generating notifications.

#### Monitor Fans, Power Supplies, and Transformers

An SNMP agent (`snmpd`) waits for incoming SNMP requests and responds to
them. If no requests are received, an agent does not initiate any
actions. However, various commands can configure `snmpd` to send traps
based on preconfigured settings (`load`, `file`, `proc`, `disk`, or
`swap` commands), or customized `monitor` commands.

From the `snmpd.conf` man page, the `monitor` command is defined this
way:

    monitor [OPTIONS] NAME EXPRESSION
     
                  defines  a  MIB  object to monitor.  If the EXPRESSION condition holds then
                  this will trigger the corresponding event, and either send a notification or
                  apply a SET assignment (or both).  Note that the event will only be triggered once,
                  when the expression first matches.  This monitor entry will not fire again until the
                  monitored condition first becomes false, and then matches again.  NAME is an administrative
                  name for this expression, and is used for indexing the mteTriggerTable (and related tables).
                  Note also that such monitors use an internal SNMPv3 request to retrieve the values
                  being monitored (even  if  normal  agent  queries  typically  use SNMPv1 or SNMPv2c).
                  See the iquerySecName token described above.
     
           EXPRESSION
                  There are three types of monitor expression supported by the Event MIB - existence, boolean and threshold tests.
     
                  OID | ! OID | != OID
     
                         defines  an  existence(0)  monitor  test.  A bare OID specifies a present(0) test,
                         which will fire when (an instance of) the monitored OID is created.  An expression
                         of the form ! OID specifies an absent(1) test, which will fire when the monitored
                         OID is delected.  An expression of the form != OID specifies a changed(2) test,
                         which will fire whenever the monitored value(s) change.  Note that there must be
                         whitespace before the OID token.
     
                  OID OP VALUE
     
                         defines a boolean(1) monitor test.  OP should be one of the defined comparison operators
                         (!=, ==, <, <=, >, >=) and VALUE should be an integer value to compare against.  Note that
                         there must be whitespace around the OP token.  A comparison such as OID !=0 will not be
                         handled correctly.
     
                  OID MIN MAX [DMIN DMAX]
     
                         defines a threshold(2) monitor test.  MIN and MAX are integer values, specifying
                         lower and upper thresholds.  If the value of the monitored OID falls below the lower
                         threshold (MIN) or rises above the upper threshold (MAX), then the monitor entry will
                         trigger the corresponding event.
     
                         Note that the rising threshold event will only be re-armed when the monitored value
                         falls below the lower threshold (MIN).  Similarly, the falling threshold event will
                         be re-armed by the upper threshold (MAX).
     
                         The optional parameters DMIN and DMAX configure a pair of similar threshold tests,
                         but working with the delta differences between successive sample values.
     
           OPTIONS
     
                  There are various options to control the behaviour of the monitored expression.  These include:
                  -D     indicates that the expression should be evaluated using delta differences between sample
                         values (rather than the values themselves).
                  -d OID  or  -di OID
                         specifies a discontinuity marker for validating delta differences.  A -di object instance
                         will be used exactly as given.  A -d object will have the instance subidentifiers from
                         the corresponding (wildcarded) expression object appended.  If the -I flag is specified,
                         then there is no difference between these two options. This option also implies -D.
                  -e EVENT
                         specifies the event to be invoked when this monitor entry is triggered.  If this option
                         is not given, the monitor entry will generate one of the standard notifications defined
                         in the DISMAN-EVENT-MIB.
                  -I     indicates that the monitored expression should be applied to the specified OID as a
                         single instance.  By default, the OID will be treated as a wildcarded object, and the
                         monitor expanded to cover all matching instances.
                  -i OID or -o OID
                         define additional varbinds to be added to the notification payload when this monitor
                         trigger fires.  For a wildcarded expression, the suffix of the matched instance will be
                         added to any OIDs specified using -o, while OIDs specified using -i will be treated
                         as exact instances.  If the -I flag is specified,  then  there  is  no difference between
                         these two options.
                         See strictDisman for details of the ordering of notification payloads.
                  -r FREQUENCY
                         monitors the given expression every FREQUENCY, where FREQUENCY is in seconds or optionally
                         suffixed by one of s (for seconds), m (for minutes), h (for hours), d (for days),
                         or w (for weeks).  By default, the expression will be evaluated every 600s (10 minutes).
                  -S     indicates that the monitor expression should not be evaluated when the agent first starts up.
                         The first evaluation will be done once the first repeat interval has expired.
                  -s     indicates that the monitor expression should be evaluated when the agent first starts up.
                         This is the default behaviour.
                         Note:  Notifications triggered by this initial evaluation will be sent before the coldStart trap.
                  -u SECNAME
                         specifies a security name to use for scanning the local host, instead of the default
                         iquerySecName.  Once again, this user must be explicitly created and given suitable access rights.

You can configure`  snmpd  `to monitor the operational status of an
Entity MIB or Entity-Sensor MIB. You can determine the operational
status, given as a value of *ok(1)*, *unavailable(2)* or
*nonoperational(3)*, by adding the following example configuration to
`/etc/snmp/snmpd.conf` and adjusting the values:

  - Using the `entPhySensorOperStatus` integer:

        # without installing extra MIBS we can check the check Fan1 status
        # if the Fan1 index is 100011001, monitor this specific OID (-I) every 10 seconds (-r), and defines additional information to be included in the trap (-o).
        monitor -I -r 10  -o 1.3.6.1.2.1.47.1.1.1.1.7.100011001 "Fan1 Not OK"  1.3.6.1.2.1.99.1.1.1.5.100011001 > 1
        # Any Entity Status non OK (greater than 1)
        monitor  -r 10  -o 1.3.6.1.2.1.47.1.1.1.1.7  "Sensor Status Failure"  1.3.6.1.2.1.99.1.1.1.5 > 1

  - Using the OID name:

        # for a specific fan called Fan1 with an index 100011001
        monitor -I -r 10  -o entPhysicalName.100011001 "Fan1 Not OK"  entPhySensorOperStatus.100011001 > 1
        # for any Entity Status not OK ( greater than 1)
        monitor  -r 10  -o entPhysicalName  "Sensor Status Failure"  entPhySensorOperStatus > 1

    {{%notice note%}}

You can use the OID name if the `snmp-mibs-downloader` package is
    installed.

    {{%/notice%}}

    {{%notice note%}}

The `entPhySensorOperStatus` integer can be found by walking the
    `entPhysicalName` table.

    {{%/notice%}}

  - To get all sensor information, run `snmpwalk` on the
    `entPhysicalName` table. For example:

        cumulus@leaf01:~$ snmpwalk -v 2c -cpublic localhost .1.3.6.1.2.1.47.1.1.1.1.7
        iso.3.6.1.2.1.47.1.1.1.1.7.100000001 = STRING: "PSU1Temp1"
        iso.3.6.1.2.1.47.1.1.1.1.7.100000002 = STRING: "PSU2Temp1"
        iso.3.6.1.2.1.47.1.1.1.1.7.100000003 = STRING: "Temp1"
        iso.3.6.1.2.1.47.1.1.1.1.7.100000004 = STRING: "Temp2"
        iso.3.6.1.2.1.47.1.1.1.1.7.100000005 = STRING: "Temp3"
        iso.3.6.1.2.1.47.1.1.1.1.7.100000006 = STRING: "Temp4"
        iso.3.6.1.2.1.47.1.1.1.1.7.100000007 = STRING: "Temp5"
        iso.3.6.1.2.1.47.1.1.1.1.7.100011001 = STRING: "Fan1"
        iso.3.6.1.2.1.47.1.1.1.1.7.100011002 = STRING: "Fan2"
        iso.3.6.1.2.1.47.1.1.1.1.7.100011003 = STRING: "Fan3"
        iso.3.6.1.2.1.47.1.1.1.1.7.100011004 = STRING: "Fan4"
        iso.3.6.1.2.1.47.1.1.1.1.7.100011005 = STRING: "Fan5"
        iso.3.6.1.2.1.47.1.1.1.1.7.100011006 = STRING: "Fan6"
        iso.3.6.1.2.1.47.1.1.1.1.7.100011007 = STRING: "PSU1Fan1"
        iso.3.6.1.2.1.47.1.1.1.1.7.100011008 = STRING: "PSU2Fan1"
        iso.3.6.1.2.1.47.1.1.1.1.7.110000001 = STRING: "PSU1"
        iso.3.6.1.2.1.47.1.1.1.1.7.110000002 = STRING: "PSU2"

#### Enable MIB to OID Translation

MIB names can be used instead of OIDs, by installing the
`snmp-mibs-downloader`, to download SNMP MIBs to the switch prior to
enabling traps. This greatly improves the readability of the
`snmpd.conf` file.

1.  Open `/etc/apt/sources.list` in a text editor.

2.  Add the `non-free` repository, then save the file:

        cumulus@switch:~$ sudo deb http://ftp.us.debian.org/debian/ jessie main non-free

3.  Update the switch:

        cumulus@switch:~$ sudo -E apt-get update

4.  Install the `snmp-mibs-downloader`:

        cumulus@switch:~$ sudo -E apt-get install snmp-mibs-downloader

5.  Open the `/etc/snmp/snmp.conf` file to verify that the `mibs :` line
    is commented out:

        #
        # As the snmp packages come without MIB files due to license reasons, loading
        # of MIBs is disabled by default. If you added the MIBs you can reenable
        # loading them by commenting out the following line.
        #mibs :

6.  Open the `/etc/default/snmpd` file to verify that the `export MIBS=`
    line is commented out:

        # This file controls the activity of snmpd and snmptrapd
         
        # Don't load any MIBs by default.
        # You might comment this lines once you have the MIBs Downloaded.
        #export MIBS=

7.  After you confirm the configuration, remove or comment out the
    `non-free` repository in `/etc/apt/sources.list`.

        #deb http://ftp.us.debian.org/debian/ jessie main non-free

#### Configure Link Up/Down Notifications

The `linkUpDownNotifications` directive is used to configure link
up/down notifications when the operational status of the link changes.

    linkUpDownNotifications yes

{{%notice note%}}

The default frequency for checking link up/down is 60 seconds. You can
change the default frequency using the `monitor` directive directly
instead of the `linkUpDownNotifications` directive. See `man snmpd.conf`
for details.

{{%/notice%}}

#### Configure Temperature Notifications

Temperature sensor information for each available sensor is maintained
in the the lmSensors MIB. Each platform can contain a different number
of temperature sensors. The example below generates a trap event when
any temperature sensor exceeds a threshold of 68 degrees (centigrade).
It monitors each `lmTempSensorsValue`. When the threshold value is
checked and exceeds the `lmTempSensorsValue`, a trap is generated. The
`-o lmTempSenesorsDevice` option is used to instruct SNMP to also
include the lmTempSensorsDevice MIB in the generated trap. The default
frequency for the `monitor` directive is 600 seconds. You can change the
default frequency with the `-r` option.:

    monitor lmTemSensor -o lmTempSensorsDevice lmTempSensorsValue > 68000

To monitor the sensors individually, first use the `sensors` command to
determine which sensors are available to be monitored on the platform.

    cumulus@switch:~$ sudo sensors

    CY8C3245-i2c-4-2e
    Adapter: i2c-0-mux (chan_id 2)
    fan5: 7006 RPM (min = 2500 RPM, max = 23000 RPM)
    fan6: 6955 RPM (min = 2500 RPM, max = 23000 RPM)
    fan7: 6799 RPM (min = 2500 RPM, max = 23000 RPM)
    fan8: 6750 RPM (min = 2500 RPM, max = 23000 RPM)
    temp1: +34.0 C (high = +68.0 C)
    temp2: +28.0 C (high = +68.0 C)
    temp3: +33.0 C (high = +68.0 C)
    temp4: +31.0 C (high = +68.0 C)
    temp5: +23.0 C (high = +68.0 C)

Configure a `monitor` command for the specific sensor using the `-I`
option. The `-I` option indicates that the monitored expression is
applied to a single instance. In this example, there are five
temperature sensors available. Use the following directive to monitor
only temperature sensor 3 at 5 minute intervals.

    monitor -I -r 300 lmTemSensor3 -o lmTempSensorsDevice.3 lmTempSensorsValue.3 > 68000

#### Configure Free Memory Notifications

You can monitor free memory using the following directives. The example
below generates a trap when free memory drops below 1,000,000KB. The
free memory trap also includes the amount of total real memory:

    monitor MemFreeTotal -o memTotalReal memTotalFree <  1000000

#### Configure Processor Load Notifications

To monitor CPU load for 1, 5, or 15 minute intervals, use the `load`
directive with the `monitor` directive. The following example generates
a trap when the 1 minute interval reaches 12%, the 5 minute interval
reaches 10%, or the 15 minute interval reaches 5%.

    load 12 10 5

#### Configure Disk Utilization Notifications

To monitor disk utilization for all disks, use the `includeAllDisks`
directive together with the `monitor` directive. The example code below
generates a trap when a disk is 99% full:

    includeAllDisks 1%
    monitor -r 60 -o dskPath -o DiskErrMsg "dskTable" diskErrorFlag !=0

#### Configure Authentication Notifications

To generate authentication failure traps, use the `authtrapenable`
directive:

    authtrapenable 1

### snmptrapd.conf

Use the Net-SNMP trap daemon to **receive** SNMP traps. The
`/etc/snmp/snmptrapd.conf` file is used to configure how **incoming**
traps are processed. Starting with Net-SNMP release 5.3, you must
specify who is authorized to send traps and informs to the notification
receiver (and what types of processing these are allowed to trigger).
You can specify three processing types:

  - *log* logs the details of the notification in a specified file to
    standard output (or stderr), or through syslog (or similar).

  - *execute* passes the details of the trap to a specified handler
    program, including embedded Perl.

  - *net* forwards the trap to another notification receiver.

Typically, this configuration is *log,execute,net* to cover any style of
processing for a particular category of notification. But it is possible
(even desirable) to limit certain notification sources to selected
processing only.

`authCommunity TYPES COMMUNITY [SOURCE [OID | -v VIEW ]]` authorizes
traps and SNMPv2c INFORM requests with the specified community to
trigger the types of processing listed. By default, this allows any
notification using this community to be processed. You can use the
SOURCE field to specify that the configuration only applies to
notifications received from particular sources. For more information
about specific configuration options within the file, look at the
`snmpd.conf(5)` man page with the following command:

    cumulus@switch:~$ man 5 snmptrapd.conf

    ###############################################################################
    #
    # EXAMPLE-trap.conf:
    #   An example configuration file for configuring the Net-SNMP snmptrapd agent.
    #
    ###############################################################################
    #
    # This file is intended to only be an example.  If, however, you want
    # to use it, it should be placed in /etc/snmp/snmptrapd.conf.
    # When the snmptrapd agent starts up, this is where it will look for it.
    #
    # All lines beginning with a '#' are comments and are intended for you
    # to read.  All other lines are configuration commands for the agent.
     
    #
    # PLEASE: read the snmptrapd.conf(5) manual page as well!
    #
    # this is the default (port 162) and defines the listening
    # protocol and address  (e.g.  udp:10.10.10.10)
    snmpTrapdAddr localhost
    #
    # defines the actions and the community string
    authCommunity log,execute,net public

## Supported MIBs

Below are the MIBs supported by Cumulus Linux, as well as suggested uses
for them. The overall Cumulus Linux MIB is defined in the
`/usr/share/snmp/mibs/Cumulus-Snmp-MIB.txt` file.

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th><p>MIB Name</p></th>
<th><p>Suggested Uses</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><a href="https://cumulusnetworks.com/static/mibs/BGP4-MIB.txt" class="external-link">BGP4-MIB</a>,</p>
<p><a href="https://cumulusnetworks.com/static/mibs/OSPFv2-MIB.txt" class="external-link">OSPFv2-MIB</a>,</p>
<p><a href="https://cumulusnetworks.com/static/mibs/OSPFv3-MIB.txt" class="external-link">OSPFv3-MIB</a>,</p>
<p><a href="https://cumulusnetworks.com/static/mibs/RIPv2-MIB.txt" class="external-link">RIPv2-MIB</a></p></td>
<td><p>You can enable FRRouting SNMP support to provide support for OSPF-MIB (RFC-1850), OSPFV3-MIB (RFC-5643), and BGP4-MIB (RFC-1657). See the <a href="#enable-snmp-support-for-frrouting">FRRouting section</a> above.</p></td>
</tr>
<tr class="even">
<td><p><a href="https://cumulusnetworks.com/static/mibs/CUMULUS-COUNTERS-MIB.txt" class="external-link">CUMULUS-COUNTERS-MIB</a></p></td>
<td><p>Discard counters: Cumulus Linux also includes its own counters MIB, defined in <code>/usr/share/snmp/mibs/Cumulus-Counters-MIB.txt</code>. It has the OID <code>.1.3.6.1.4.1.40310.2</code></p></td>
</tr>
<tr class="odd">
<td><p><a href="https://cumulusnetworks.com/static/mibs/CUMULUS-POE-MIB.txt" class="external-link">CUMULUS-POE-MIB</a></p></td>
<td><p>The Cumulus Networks custom <a href="../../System-Configuration/Power-over-Ethernet-PoE">Power over Ethernet</a> PoE MIB defined in the <code>/usr/share/snmp/mibs/Cumulus-POE-MIB.txt</code> file. For devices that provide PoE, this provides users with the system wide power information in <code>poeSystemValues</code> as well as per interface <code>PoeObjectsEntry</code> values for the <code>poeObjectsTable</code>. Most of this information comes from the <code>poectl</code> command. To enable this MIB, uncomment the following line in <code>/etc/snmp/snmpd.conf</code>:</p>
<pre><code>#pass_persist .1.3.6.1.4.1.40310.3 /usr/share/snmp/cl_poe_pp.py</code></pre></td>
</tr>
<tr class="even">
<td><p><a href="https://cumulusnetworks.com/static/mibs/CUMULUS-RESOURCE-QUERY-MIB.txt" class="external-link">CUMULUS-RESOURCE-QUERY-MIB</a></p></td>
<td><p>Cumulus Linux includes its own resource utilization MIB, which is similar to using<code> cl-resource-query</code>. This MIB monitors layer 3 entries by host, route, nexthops, ECMP groups, and layer 2 MAC/BDPU entries.The MIB is defined in <code>/usr/share/snmp/mibs/Cumulus-Resource-Query-MIB.txt</code> and has the OID <code>.1.3.6.1.4.1.40310.1.</code></p></td>
</tr>
<tr class="odd">
<td><p><a href="https://cumulusnetworks.com/static/mibs/CUMULUS-SNMP-MIB.txt" class="external-link">CUMULUS-SNMP-MIB</a></p></td>
<td><p>SNMP counters. For information on exposing CPU and memory information with SNMP, see this <a href="https://support.cumulusnetworks.com/hc/en-us/articles/203922988" class="external-link">knowledge base article</a>.</p></td>
</tr>
<tr class="even">
<td><p><a href="https://cumulusnetworks.com/static/mibs/DISMAN-EVENT-MIB.txt" class="external-link">DISMAN-EVENT-MIB</a></p></td>
<td><p>Trap monitoring</p></td>
</tr>
<tr class="odd">
<td><p><a href="https://cumulusnetworks.com/static/mibs/ENTITY-MIB.txt" class="external-link">ENTITY-MIB</a></p></td>
<td><p>From RFC 4133, the temperature sensors, fan sensors, power sensors, and ports are covered.</p></td>
</tr>
<tr class="even">
<td><p><a href="https://cumulusnetworks.com/static/mibs/ENTITY-SENSOR-MIB.txt" class="external-link">ENTITY-SENSOR-MIB</a></p></td>
<td><p>Physical sensor information (temperature, fan, and power supply) from RFC 3433.</p></td>
</tr>
<tr class="odd">
<td><p><a href="https://cumulusnetworks.com/static/mibs/HOST-RESOURCES-MIB.txt" class="external-link">HOST-RESOURCES-MIB</a></p></td>
<td><p>Users, storage, interfaces, process info, run parameters</p></td>
</tr>
<tr class="even">
<td><p><a href="https://cumulusnetworks.com/static/mibs/IEEE8021-BRIDGE-MIB.txt" class="external-link">IEEE8021-BRIDGE-MIB</a></p>
<p><a href="https://cumulusnetworks.com/static/mibs/IEEE8021-Q-BRIDGE-MIB.txt" class="external-link">IEEE8021-Q-BRIDGE-MIB</a></p></td>
<td><p>The <code>dot1dBasePortEntry</code> and <code>dot1dBasePortIfIndex</code> tables in the BRIDGE-MIB and <code>dot1qBase</code>, <code>dot1qFdbEntry</code>, <code>dot1qTpFdbEntry</code>, <code>dot1qTpFdbStatus</code>, and <code>dot1qVlanStaticName</code> tables in the Q-BRIDGE-MIB tables. You must uncomment the <code>bridge_pp.py pass_persist</code> script in <code>/etc/snmp/snmpd.conf</code>.</p></td>
</tr>
<tr class="odd">
<td><p><a href="https://cumulusnetworks.com/static/mibs/IEEE8023-LAG-MIB.txt" class="external-link">IEEE8023-LAG-MIB</a></p></td>
<td><p>Implementation of the IEEE 8023-LAG-MIB includes the <code>dot3adAggTable</code> and <code>dot3adAggPortListTable</code> tables. To enable this, edit <code>/etc/snmp/snmpd.conf</code> and uncomment or add the following lines:</p>
<pre><code>view systemonly included .1.2.840.10006.300.43
pass_persist .1.2.840.10006.300.43 /usr/share/snmp/ieee8023_lag_pp.py</code></pre></td>
</tr>
<tr class="even">
<td><p><a href="https://cumulusnetworks.com/static/mibs/IF-MIB.txt" class="external-link">IF-MIB</a></p></td>
<td><p>Interface description, type, MTU, speed, MAC, admin, operation status, counters</p>
<p>{{%notice note%}}</p>
<p>The IF-MIB cache is disabled by default. The non-caching code path in the IF-MIB treats 64-bit counters like 32-bit counters (a 64-bit counter rolls over after the value increments to a value that extends beyond 32 bits). To enable the counter to reflect traffic statistics using 64-bit counters, remove the <code>-y</code> option from the <code>SNMPDOPTS</code> line in the <code>/etc/default/snmpd</code> file. The example below first shows the original line, commented out, then the modified line without the <code>-y</code> option:</p>
<pre><code>cumulus@switch:~$ cat /etc/default/snmpd
SNMPDOPTS=&#39;-LS 0-4 d -Lf /dev/null -u snmp -g snmp -I -smux -p /run/snmpd.pid&#39;</code></pre>
<p>{{%/notice%}}</p></td>
</tr>
<tr class="odd">
<td><p><a href="https://cumulusnetworks.com/static/mibs/IP-FORWARD-MIB.txt" class="external-link">IP-FORWARD-MIB</a></p></td>
<td><p>IP routing table</p></td>
</tr>
<tr class="even">
<td><p><a href="https://cumulusnetworks.com/static/mibs/IP-MIB.txt" class="external-link">IP-MIB (includes ICMP)</a></p></td>
<td><p>IPv4, IPv4 addresses, counters, netmasks</p></td>
</tr>
<tr class="odd">
<td><p><a href="https://cumulusnetworks.com/static/mibs/IPV6-MIB.txt" class="external-link">IPv6-MIB</a></p></td>
<td><p>IPv6 counters</p></td>
</tr>
<tr class="even">
<td><p><a href="https://cumulusnetworks.com/static/mibs/LLDP-MIB.txt" class="external-link">LLDP-MIB</a></p></td>
<td><p>Layer 2 neighbor information from <code>lldpd</code> (you need to <a href="../../Layer-2/Link-Layer-Discovery-Protocol/#enable-the-snmp-subagent-in-lldp">enable the SNMP subagent</a> in LLDP). You need to start <code>lldpd</code> with the <code>-x</code> option to enable connectivity to <code>snmpd</code> (AgentX).</p></td>
</tr>
<tr class="odd">
<td><p><a href="https://cumulusnetworks.com/static/mibs/LM-SENSORS-MIB.txt" class="external-link">LM-SENSORS MIB</a></p></td>
<td><p>Fan speed, temperature sensor values, voltages. This is deprecated since the ENTITY-SENSOR MIB has been added.</p></td>
</tr>
<tr class="even">
<td><p><a href="https://cumulusnetworks.com/static/mibs/NET-SNMP-AGENT-MIB.txt" class="external-link">NET-SNMP-AGENT-MIB</a></p></td>
<td><p>Agent timers, user, group config</p></td>
</tr>
<tr class="odd">
<td><p><a href="https://cumulusnetworks.com/static/mibs/NET-SNMP-EXTEND-MIB.txt" class="external-link">NET-SNMP-EXTEND-MIB</a></p></td>
<td><p>See <a href="https://support.cumulusnetworks.com/hc/en-us/articles/204507848" class="external-link">this knowledge base article</a> on extending NET-SNMP in Cumulus Linux to include data from power supplies, fans, and temperature sensors.</p></td>
</tr>
<tr class="even">
<td><p><a href="https://cumulusnetworks.com/static/mibs/NET-SNMP-VACM-MIB.txt" class="external-link">NET-SNMP-VACM-MIB</a></p></td>
<td><p>Agent timers, user, group config</p></td>
</tr>
<tr class="odd">
<td><p><a href="https://cumulusnetworks.com/static/mibs/NOTIFICATION-LOG-MIB.txt" class="external-link">NOTIFICATION-LOG-MIB</a></p></td>
<td><p>Local logging</p></td>
</tr>
<tr class="even">
<td><p><a href="https://cumulusnetworks.com/static/mibs/SNMP-FRAMEWORK-MIB.txt" class="external-link">SNMP-FRAMEWORK-MIB</a></p></td>
<td><p>Users, access</p></td>
</tr>
<tr class="odd">
<td><p><a href="https://cumulusnetworks.com/static/mibs/SNMP-MPD.txt" class="external-link">SNMP-MPD-MIB</a></p></td>
<td><p>Users, access</p></td>
</tr>
<tr class="even">
<td><p><a href="https://cumulusnetworks.com/static/mibs/SNMP-TARGET.txt" class="external-link">SNMP-TARGET-MIB</a></p></td>
<td><p> </p></td>
</tr>
<tr class="odd">
<td><p><a href="https://cumulusnetworks.com/static/mibs/SNMP-USER-BASED-SM.txt" class="external-link">SNMP-USER-BASED-SM-MIB</a></p></td>
<td><p>Users, access</p></td>
</tr>
<tr class="even">
<td><p><a href="https://cumulusnetworks.com/static/mibs/SNMP-VIEW-BASED-ACM.txt" class="external-link">SNMP-VIEW-BASED-ACM-MIB</a></p></td>
<td><p>Users, access</p></td>
</tr>
<tr class="odd">
<td><p><a href="https://cumulusnetworks.com/static/mibs/TCP-MIB.txt" class="external-link">TCP-MIB</a></p></td>
<td><p>TCP-related information</p></td>
</tr>
<tr class="even">
<td><p><a href="https://cumulusnetworks.com/static/mibs/UCD-SNMP-MIB.txt" class="external-link">UCD-SNMP-MIB</a></p></td>
<td><p>System memory, load, CPU, disk IO</p></td>
</tr>
<tr class="odd">
<td><p><a href="https://cumulusnetworks.com/static/mibs/UDP-MIB.txt" class="external-link">UDP-MIB</a></p></td>
<td><p>UDP-related information</p></td>
</tr>
</tbody>
</table>

{{%notice note%}}

The ENTITY MIB does not show the chassis information in Cumulus Linux.

{{%/notice%}}

## Pass Persist Scripts

The pass persist scripts in Cumulus Linux use the [pass\_persist
extension](http://net-snmp.sourceforge.net/wiki/index.php/Tut:Extending_snmpd_using_shell_scripts#Pass_persist)
to Net-SNMP. The scripts are stored in `/usr/share/snmp` and include:

  - bgp4\_pp.py
  - bridge\_pp.py
  - cl\_drop\_cntrs\_pp.py
  - cl\_poe\_pp.py
  - entity\_pp.py
  - entity\_sensor\_pp.py
  - ieee8023\_lag\_pp.py
  - resq\_pp.py
  - snmpifAlias\_pp.py
  - sysDescr\_pass.py

All the scripts are enabled by default in Cumulus Linux, except for:

  - `bgp4_pp.py`, which is now handled by
    [FRRouting](../../Layer-3/FRRouting-Overview/) instead of
    Quagga, so monitoring has changed accordingly.
  - `cl_poe_pp.py`, which is disabled by default as only certain
    platforms that Cumulus Linux supports are capable of doing [Power over Ethernet](../../System-Configuration/Power-over-Ethernet-PoE/).

## Troubleshooting

Use the following commands to troubleshoot potential SNMP issues:

    cumulus@switch:~$ net show snmp-server status                               
    Simple Network Management Protocol (SNMP) Daemon.
    ---------------------------------  ------------------------------------------------------------------------------------
    Current Status                     failed (failed)
    Reload Status                      enabled
    Listening IP Addresses             localhost 9.9.9.9
    Main snmpd PID                     0
    Version 1 and 2c Community String  Configured
    Version 3 Usernames                Not Configured
    Last Logs (with Errors)            -- Logs begin at Thu 2017-08-03 16:23:05 UTC, end at Fri 2017-08-04 18:17:24 UTC. --
                                       Aug 04 18:17:19 cel-redxp-01 snmpd[8389]: Error opening specified endpoint "9.9.9.9"
                                       Aug 04 18:17:19 cel-redxp-01 snmpd[8389]: Server Exiting with code 1
    ---------------------------------  ------------------------------------------------------------------------------------

    cumulus@switch:~$ net show configuration snmp-server                                                            
    snmp-server                                         
      listening-address 127.0.0.1                
      readonly-community public access default
      readonly-community allpass access any
      readonly-community temp2 access 1.1.1.1
      readonly-community temp2 access 2.2.2.2
      trap-destination 1.1.1.1 community-password public version 2c
      trap-link-up check-frequency 10
      trap-snmp-auth-failures

    cumulus@switch:~$ net show configuration commands
    ...
    net add snmp-server listening-address all
    net add snmp-server readonly-community allpass access any
    net add snmp-server readonly-community temp2 access 1.1.1.1
    net add snmp-server readonly-community temp2 access 2.2.2.2
    net add snmp-server trap-destination 1.1.1.1 community-password public version 2c
    net add snmp-server trap-link-up check-frequency 10
    net add snmp-server trap-snmp-auth-failures
    ...
