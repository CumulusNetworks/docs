---
title: SNMP Monitoring
author: Cumulus Networks
weight: 219
aliases:
 - /display/CL35/SNMP+Monitoring
 - /pages/viewpage.action?pageId=8357390
pageID: 8357390
product: Cumulus Linux
version: '3.5'
imgData: cumulus-linux-35
siteSlug: cumulus-linux-35
---
Cumulus Linux utilizes the open source Net-SNMP agent `snmpd`, v5.7.3,
which provides support for most of the common industry-wide MIBs,
including interface counters and TCP/UDP IP stack data.

## <span>Introduction to SNMP (Simple Network Management Protocol)</span>

SNMP is an IETF standards-based network management architecture and
protocol that traces its roots back to Carnegie-Mellon University in
1982. Since then, it's been modified by programmers at the University of
California. In 1995, this code was also made publicly available as the
UCD project. After that, `ucd-snmp` was extended by work done at the
University of Liverpool as well as later in Denmark. In late 2000, the
project name changed to `net-snmp` and became a fully-fledged
collaborative open source project. The version used by Cumulus Networks
is base on the latest `net-snmp` 5.7.3 branch with added custom MIBs and
pass through and pass persist scripts ([see
below](#src-8357390_SNMPMonitoring-passpersist) for more information on
pass persist scripts).

## <span>Configuring Ports for SNMP to Listen for Requests</span>

For security reasons, the default port binding for `snmpd` is the
loopback local address; consequently by default, the SNMP service does
not listen for SNMP requests from outside the switch. In order to listen
to requests from outside the switch, you need to change this binding to
a specific IP address (or all interfaces) after configuring security
access (community strings, users, and so forth). This is a change from
older versions of Cumulus Linux (before version 3.0), which listened to
incoming requests on all interfaces by default. The `snmpd`
configuration file is `/etc/snmp/snmpd.conf` and should be modified
before enabling and starting `snmpd`. The default configuration has no
access community strings defined so `snmpd` will not respond to any SNMP
requests until this is added.

## <span>Quick Start Guide</span>

The SNMP daemon, `snmpd`, uses the configuration file
`/etc/snmp/snmpd.conf` for almost all of its configuration. The syntax
of the most important keywords are defined in the following table.

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
<td><p><strong>agentAddress</strong></p></td>
<td><p><strong>Required.</strong> This command sets the protocol, IP address, and the port for <code>snmpd</code> to listen on for <strong>incoming</strong> requests. The IP address must exist on an interface that has link UP on the switch where <code>snmpd</code> is being used. By default, this is set to <em>udp:127.0.0.1:161</em>, which means <code>snmpd</code> listens on the loopback interface and so only responds to requests (<code>snmpwalk</code>, <code>snmpget</code>, <code>snmpgetnext</code>) originating from the switch. A wildcard setting of <em>udp:161,udp6:161</em> forces <code>snmpd</code> to listen on all IPv4 and IPv6 interfaces for incoming SNMP requests. Multiple IP address can be configured as comma-separated values, as in <em>udp:66.66.66.66:161,udp:77.77.77.77:161,udp6:[2001::1]:161.</em></p></td>
</tr>
<tr class="even">
<td><p><strong>rocommunity</strong></p></td>
<td><p><strong>Required.</strong> This command defines the password that is required for SNMP version 1 or 2c requests for GET or GETNEXT. By default, this provides access to the full OID tree for such requests, regardless of from where they were sent. There is no default password set, so that <code>snmpd</code> does not respond to any requests that arrive. Users often specify a source IP address token to restrict access to only that host or network given. Users also specify a view name (as defined above) to restrict the subset of the OID tree.</p>
<p>Some examples of <code>rocommunity</code> commands are shown below. The first command sets the read only community string to "simplepassword" for SNMP requests sourced from the 10.10.10.0/24 subnet and restricts viewing to the <em>systemonly</em> view name defined previously with the <code>view</code> command. The second example simply creates a read-only community password that allows access to the entire OID tree from any source IP address.</p>
<pre><code>rocommunity simplepassword 10.10.10.0/24 -V systemonly
 
rocommunity cumulustestpassword</code></pre></td>
</tr>
<tr class="odd">
<td><p><strong>view</strong></p></td>
<td><p>This commands defines a view name that specifies a subset of the overall OID tree. This restricted view can then be referenced by name in the <code>rocommunity</code> command to link the view to a password that is used to see this restricted OID subset. By default, the <code>snmpd.conf</code> file contains numerous views with the <em>systemonly</em> view name:</p>
<pre><code>view   systemonly  included   .1.3.6.1.2.1.1 
 
view   systemonly  included   .1.3.6.1.2.1.2
 
view   systemonly  included   .1.3.6.1.2.1.3 </code></pre>
<p>The <em>systemonly</em> view is used by <code>rocommunity</code> to create a password for access to only these branches of the OID tree.</p></td>
</tr>
<tr class="even">
<td><p><strong>trapsink</strong></p>
<p><strong>trap2sink</strong></p></td>
<td><p>This command defines the IP address of the notification (or trap) receiver for either SNMPv1 traps or SNMPv2 traps. If several sink directives are specified, multiple copies of each notification (in the appropriate formats) are generated. Note that a trap server must be configured to receive and decode these trap messages (for example, <code>snmptrapd</code>). The address of the trap receiver can be configured with a different protocol and port but this is most often left out. The defaults are to use the well-known UDP packets and port 162.</p></td>
</tr>
<tr class="odd">
<td><p><strong>createUser</strong></p>
<p><strong>iquerySecName</strong></p>
<p><strong>rouser</strong></p></td>
<td><p>These three commands define an internal SNMPv3 username that is required in order for <code>snmpd</code> to send traps. This username is required to authorize the DisMan service even though SNMPv3 is not being configured for use. The example <code>snmpd.conf</code> configuration shown below creates <em>snmptrapusernameX</em> as the username (this is just an example username) using the <code>createUser</code> command. <code>iquerySecName</code> defines the default SNMPv3 username to be used when making internal queries to retrieve monitored expressions. <code>rouser</code> specifies which username should be used for these SNMPv3 queries. All three are required for <code>snmpd</code> to retrieve information and send built-in traps or for those configured with the <code>monitor</code> command shown below in the examples.</p>
<pre><code>createUser snmptrapusernameX
 
iquerySecName snmptrapusernameX
 
rouser snmptrapusernameX</code></pre></td>
</tr>
<tr class="even">
<td><p><strong>linkUpDownNotifications yes</strong></p></td>
<td><p>This command enables link up and link down trap notifications, assuming the other trap configurations settings are set. This command configures the Event MIB tables to monitor the ifTable for network interfaces being taken up or down, and triggering a <em>linkUp</em> or <em>linkDown</em> notification as appropriate. This is exactly equivalent to the following configuration:</p>
<pre><code>notificationEvent  linkUpTrap    linkUp   ifIndex ifAdminStatus ifOperStatus
 
notificationEvent  linkDownTrap  linkDown ifIndex ifAdminStatus ifOperStatus 
 
monitor  -r 60 -e linkUpTrap   &quot;Generate linkUp&quot; ifOperStatus != 2
 
monitor  -r 60 -e linkDownTrap &quot;Generate linkDown&quot; ifOperStatus == 2</code></pre></td>
</tr>
<tr class="odd">
<td><p><strong>defaultMonitors yes</strong></p></td>
<td><p>This command configures the Event MIB tables to monitor the various UCD-SNMP-MIB tables for problems (as indicated by the appropriate xxErrFlag column objects) and send a trap. This assumes the user has downloaded the <code>snmp-mibs-downloader</code> Debian package and comments out "mibs" from <code>/etc/snmp/snmp.conf</code> (as in: "#mibs"). This command is exactly equivalent to the following configuration:</p>
<pre><code>monitor   -o prNames -o prErrMessage &quot;process table&quot; prErrorFlag != 0
 
monitor   -o memErrorName -o memSwapErrorMsg &quot;memory&quot; memSwapError != 0
 
monitor   -o extNames -o extOutput &quot;extTable&quot; extResult != 0
 
monitor   -o dskPath -o dskErrorMsg &quot;dskTable&quot; dskErrorFlag != 0
 
monitor   -o laNames -o laErrMessage  &quot;laTable&quot; laErrorFlag != 0
 
monitor   -o fileName -o fileErrorMsg  &quot;fileTable&quot; fileErrorFlag != 0</code></pre></td>
</tr>
</tbody>
</table>

## <span>Starting the SNMP Daemon</span>

The following procedure is the recommended process to start `snmpd` and
monitor it using `systemctl`.

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

Once the service is started, SNMP can be used to manage various
components on the Cumulus Linux switch.

## <span>Configuring SNMP</span>

Cumulus Linux ships with a production usable default `snmpd.conf` file
included.This section covers a few basic configuration options in
`snmpd.conf`. For more information regarding further configuring this
file, refer to the `snmpd.conf` man page.

{{%notice info%}}

Cumulus Linux 3.4 and later releases support configuring SNMP with NCLU.

{{%/notice%}}

{{%notice warning%}}

The default `snmpd.conf` file does not include all supported MIBs or
OIDs that can be exposed.

{{%/notice%}}

{{%notice note%}}

Customers must at least change the default community string for v1 or
v2c environments or the `snmpd` daemon will not respond to any requests.

{{%/notice%}}

### <span>Configuring SNMP with NCLU</span>

The table below highlights the structure of NCLU commands available for
configuring SNMP. An example command set can be found below the table.

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
<td><p>Removes all entries in the <code>/etc/snmp/snmpd.conf</code> file and replaces them with defaults. The defaults remove all SNMPv3 usernames, readonly-communities, and a listening-address of localhost will be configured.</p></td>
</tr>
<tr class="even">
<td><p><code>net add snmp-server listening-address localhost</code></p></td>
<td><p>For security reasons, the localhost is set to a listening address 127.0.0.1 by default. This means that the SNMP agent will only respond to requests originating on the switch itself. One or more IP addresses can be deleted.</p></td>
</tr>
<tr class="odd">
<td><p><code>net add snmp-server listening-address all</code></p></td>
<td><p>Configures the snmpd agent to listen on all interfaces for UDP port 161 SNMP requests.</p></td>
</tr>
<tr class="even">
<td><p><code>net add snmp-server listening-address IP_ADDRESS IP_ADDRESS ...</code></p></td>
<td><p>Sets the SNMP agent snmpd to listen to a specific IPv4 or IPv6 address, or a group of addresses with space separated values, for incoming SNMP queries.</p>
<pre><code>net add snmp-server listening-address 10.10.10.10</code></pre>
<pre><code>net add snmp-server listening-address 10.10.10.10 44.44.44.44</code></pre></td>
</tr>
<tr class="odd">
<td><p><code>net add snmp-server viewname [view name] (included | excluded) [OID or name]</code></p></td>
<td><p>Creates a view to restrict MIB tree exposure. By itself, this view definition has no effect; however, when linked to an SNMPv3 username or community password, and a host from a restricted subnet, any SNMP request with that username/password must have a source IP address within the configured subnet.</p>
<p>Note that OID can be either a string of period separated decimal numbers or a unique text string that identifies an SNMP MIB object. Some MIBs are not installed by default and must be installed either by hand or with the latest Debian package called snmp-mibs-downloader. Specific viewname entries can be removed with the delete command or with just a view name to remove all entries matching that view name. A specific view name can be defined multiple times and fine tuned to provide or restrict access using included or excluded command to specify branches of certain MIB trees</p>
<p>net add snmp-server viewname cumulusOnly included .1.3.6.1.4.1.40310</p></td>
</tr>
<tr class="even">
<td><p><code>net add snmp-server (readonly-community | readonly-community-v6) [password] access (any | localhost | [network]) [(view [view name]) or [oid [oid or name])</code></p></td>
<td><p>Defines the community password, and which parts of the OID tree to apply the password to for incoming SNMP requests.</p></td>
</tr>
<tr class="odd">
<td><p><code>net add snmp-server trap-destination (localhost | [ipaddress]) community-password [password] [version [1 | 2c]]</code></p></td>
<td><p>Sets the SNMP Trap destination IP address. Multiple destinations can exist, but at least one must be set to enable SNMP Traps to be sent. Removing all settings will disable SNMP traps.</p>
<p>The default version is 2c, unless otherwise configured.</p></td>
</tr>
<tr class="even">
<td><p><code>net add snmp-server trap-link-up [check-frequency [seconds]]</code></p></td>
<td><p>Enables notifications for interface link-up to be sent to SNMP Trap destinations.</p></td>
</tr>
<tr class="odd">
<td><p><code>net add snmp-server trap-link-down [check-frequency [seconds]]</code></p></td>
<td><p>Enables notifications for interface link-down to be sent to SNMP Trap destinations.</p></td>
</tr>
<tr class="even">
<td><p><code>net add snmp-server trap-snmp-auth-failures</code></p></td>
<td><p>Enables SNMP Trap notifications to be sent for every SNMP authentication failure.</p></td>
</tr>
<tr class="odd">
<td><p><code>net add snmp-server trap-cpu-load-average one-minute [threshold] five-minute [5-min-threshold] fifteen-minute [15-min-threshold]</code></p></td>
<td><p>Enables a trap when the cpu-load-average exceeds the configured threshold. Only integers or floating point numbers can be used.</p></td>
</tr>
</tbody>
</table>

This table covers system setting configuration commands for SNMPv2-MIB:

| Command                                        | Summary                                                                                                                       |
| ---------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------- |
| `net add snmp-server system-location [string]` | Sets the system physical location for the node in the SNMPv2-MIB system table.                                                |
| `net add snmp-server system-contact [string]`  | Sets the identification of the contact person for this managed node, together with information on how to contact this person. |
| `net add snmp-server system-name [string]`     | Sets an administratively-assigned name for the managed node. By convention, this is the node's fully-qualified domain name.   |

The example commands below enable an SNMP agent to listen on all IP
addresses with a community string password, set the trap destination
host IP address, and create four types of SNMP traps:

    cumulus@switch:~$ net add snmp-server listening-address all
    cumulus@switch:~$ net add snmp-server readonly-community tempPassword access any
    cumulus@switch:~$ net add snmp-server trap-destination 1.1.1.1 community-password mypass version 2c
    cumulus@switch:~$ net add snmp-server trap-link-up check-frequency 15
    cumulus@switch:~$ net add snmp-server trap-link-down check-frequency 10
    cumulus@switch:~$ net add snmp-server trap-cpu-load-average one-minute 7.45 five-minute 5.14
    cumulus@switch:~$ net add snmp-server trap-snmp-auth-failures

### <span>Configuring SNMP Manually</span>

There are times when you need to manually edit the SNMP configuration;
for example, there may not be the necessary option in NCLU. In cases
like this, you need to edit the configuration directly, which is stored
in the `/etc/snmp/snmpd.conf` file.

Use caution when making direct edits to the file, however, because the
next time you use NCLU to update your SNMP configuration, some of the
options you specified may get overwritten by NCLU as it may not be able
to correctly parse the syntax. However, if NCLU is not aware of a given
configuration option, it will not overwrite such an option.

Make sure you do not delete the `snmpd.conf` file as this can cause
issues with the package manager the next time you update Cumulus Linux.

### <span>Configuring SNMP with Management VRF</span>

When you configure [Management VRF](/display/CL35/Management+VRF), you
need to be aware of the interface IP addresses on which SNMP is
listening. If you set listening-address to all, the `snmpd` daemon
responds to incoming requests on all interfaces in the default VRF. If
you prefer to listen on a limited number of IP addresses, Cumulus
Networks recommends that you run only one instance of the `snmpd` daemon
and that all of the configured interfaces are in the same VRF.

SNMP configuration in NCLU is not VRF aware so the `snmpd` daemon is
always started in the default VRF. Because interfaces in a particular
VRF (routing table) are not aware of interfaces in a different VRF, the
`snmpd` daemon only responds to polling requests and sends traps on the
interfaces of the VRF on which it is running.

When management VRF is configured, most users will want to start the
`snmpd` daemon in the management VRF to receive and respond to SNMP
polling requests on eth0. Follow these guidelines:

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

More complex configurations are possible; for example, you can run more
than one `snmpd` daemon (one in each VRF designed to receive SNMP
polling requests). Cumulus Networks does not recommend this for memory
and cpu resource reasons. However, if this is required, you must use a
separate configuration file with each instance of the `snmpd` daemon.
You can use a copy of the `/etc/snmp/snmpd.conf` file. When you use this
file, start an `snmpd` daemon with the following command:

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

### <span id="src-8357390_SNMPMonitoring-agentAddress" class="confluence-anchor-link"></span><span>Configuring the agentAddress</span>

As mentioned earlier, you need to configure the transport protocol, IP
address and port where SNMP listens. In Cumulus Linux, the transport
defaults to UDP, the IP address defaults to the localhost (127.0.0.1)
and the port defaults to 161. If you want to change any of these
settings, do the following:

1.  Open the `/etc/snmp/snmpd.conf` file in a text editor, and edit the
    following line:
    
        agentAddress udp:127.0.0.1:161
    
    {{%notice note%}}
    
    You can only specify one agentAddress line. If you want to listen on
    multiple IP addresses, use comma-separated addresses, like this:
    
        agentAddress  10.10.10.10,44.44.44.44,127.0.0.1
    
    {{%/notice%}}

2.  Save the file, then restart the `snmpd` service:
    
        cumulus@switch:~$ sudo systemctl restart snmpd.service

### <span>Setting up the Custom Cumulus Networks MIBs</span>

No changes are required in the `/etc/snmp/snmpd.conf` file on the
switch, in order to support the custom Cumulus Networks MIBs. The
following lines are already included by default:

    view systemonly included .1.3.6.1.4.1.40310.1
    view systemonly included .1.3.6.1.4.1.40310.2
    sysObjectID 1.3.6.1.4.1.40310
    pass_persist .1.3.6.1.4.1.40310.1 /usr/share/snmp/resq_pp.py
    pass_persist .1.3.6.1.4.1.40310.2 /usr/share/snmp/cl_drop_cntrs_pp.py

However, several files need to be copied to the server, in order for the
custom Cumulus MIB to be recognized on the destination NMS server.

  - `/usr/share/snmp/mibs/Cumulus-Snmp-MIB.txt`

  - `/usr/share/snmp/mibs/Cumulus-Counters-MIB.txt`

  - `/usr/share/snmp/mibs/Cumulus-Resource-Query-MIB.txt`

### <span id="src-8357390_SNMPMonitoring-public_community" class="confluence-anchor-link"></span><span>Setting the Community String</span>

The `snmpd` authentication for versions 1 and 2 is disabled by default
in Cumulus Linux. This password (called a community string) can be
enabled by setting **rocommunity** (for read-only access) or
**rwcommunity** (for read-write access). Setting a community string is
required.

To enable read-only querying by a client:

1.  Open `/etc/snmp/snmpd.conf` in a text editor.

2.  To allow read-only access, uncomment the following line, then save
    the file:
    
        rocommunity public default -V systemonly
    
    The line can be broken down as follows:
    
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

### <span id="src-8357390_SNMPMonitoring-frr" class="confluence-anchor-link"></span><span>Enabling SNMP Support for FRRouting</span>

As of Cumulus Linux 3.3.1, SNMP is now supported for
[FRRouting](/version/cumulus-linux-35/Layer_3/FRRouting_Overview/). To
enable SNMP support for FRRouting, you need to:

  - Configure [AgentX](http://www.net-snmp.org/docs/README.agentx.html)
    (ASX) access in FRRouting

  - Create an SNMP-specific `frr.conf` file

  - Restart the SNMP and FRRouting services

Enabling FRRouting includes support for BGP. However, if you plan on
using the BGP4 MIB, you need to expose .1.3.6.1.2.1.15 in the
`/etc/snmp/snmpd.conf` file.

{{%notice note%}}

At this time, SNMP does not support monitoring BGP unnumbered neighbors.

{{%/notice%}}

Similarly, if you plan on using the OSPFv2 MIB, you need to expose
.1.3.6.1.2.1.14 in the `/etc/snmp/snmpd.conf` file, and expose
.1.3.6.1.2.1.191 for the OSPv3 MIB.

To enable SNMP support for FRRouting, do the following:

1.  Configure AgentX access in FRRouting:
    
        cumulus@switch:~$ net add routing agentx
        cumulus@switch:~$ net pending
        cumulus@switch:~$ net commit

2.  Update the SNMP configuration to enable FRRouting to respond to SNMP
    requests. Open the `/etc/snmp/snmpd.conf` file in a text editor, and
    add the following lines:
    
        agentAddress udp:161  
        rocommunity public default   
         
        # these next three lines configure agentx and allows FRRouting to respond to snmp requests.
        master  agentx 
        agentXSocket /run/agentx/master 
        agentXPerms 777 777 
    
    {{%notice note%}}
    
    The rocommunity password is defined
    [above](#src-8357390_SNMPMonitoring-public_community).
    
    {{%/notice%}}

3.  Optionally, you need to uncomment parts of `snmpd.conf` if you
    intend to use SNMP with the following MIBs:
    
      - For the BGP4 MIB, uncomment the `view systemonly included
        .1.3.6.1.2.1.15` line below.
    
      - For the OSPF MIB, uncomment the `view systemonly included
        .1.3.6.1.2.1.14` line below.
    
      - For the OSPFV3 MIB, uncomment the `view systemonly included
        .1.3.6.1.2.1.191` line below.
    
    <!-- end list -->
    
        # Note: FRRouting snmpd support has been reenabled.
        # Please see FRRouting documentation for instructions
        # on enabling AgentX functionality in FRRouting and
        # also set agentxsocket and agentxperms at the bottom
        # of this config file.
        #
        # Uncomment the following to enable OSPF, OSPFV3 and BGP4 MIBs
        # The following line exposes OSPF-MIB in this view
        # view   systemonly  included   .1.3.6.1.2.1.14
        # frrouting bgp
        # The following line exposes BGP4-MIB in this view
        # view   systemonly  included   .1.3.6.1.2.1.15
        # frrouting ospf6
        # The following line exposes OSPFV3-MIB in this view
        # view   systemonly  included   .1.3.6.1.3.191
        #
        # This pass persist script bgp4_pp.py is deprecated.  Please enable
        # AgentX support in FRRouting for BGP4-MIB support.

4.  After you save the `snmpd.conf` file, create a file called
    `/etc/snmp/frr.conf` that contains the following line:
    
        agentXSocket /run/agentx/master

5.  After you save this file, restart the `snmpd` and FRRouting services
    for these changes to take effect and to reload the FRRouting daemons
    with AgentX access:
    
        cumulus@switch:~$ sudo systemctl restart snmpd.service
        cumulus@switch:~$ sudo systemctl restart frr.service

To verify the configuration, run `snmpwalk`. For example, if you have a
running OSPF configuration with routes, you can check this OSPF-MIB
first from the switch itself with:

    cumulus@switch:~$ sudo snmpwalk -v2c -cpublic localhost .1.3.6.1.2.1.14

### <span>Enabling the .1.3.6.1.2.1 Range</span>

Some MIBs, including storage information, are not included by default in
`snmpd.conf` in Cumulus Linux. This results in some default views on
common network tools (like `librenms`) to return less than optimal data.
More MIBs can be included, by enabling all the .1.3.6.1.2.1 range. This
simplifies the configuration file, removing concern that any required
MIBs will be missed by the monitoring system. Various MIBs were added to
version 3.0 and include the following: ENTITY and ENTITY-SENSOR MIB and
parts of the BRIDGE-MIB and Q-BRIDGE-MIBs. These are included in the
default configuration.

{{%notice note%}}

The view of the BRIDGE-MIB and Q-BRIDGE-MIB are commented out.

{{%/notice%}}

{{%notice warning%}}

This configuration grants access to a large number of MIBs, including
all MIB2 MIBs, which could reveal more data than expected. In addition
to being a security vulnerability, it could consume more CPU resources.

{{%/notice%}}

To enable the .1.3.6.1.2.1 range:

1.  Open `/etc/snmp/snmpd.conf` in a text editor.

2.  Make sure the following lines are included in the configuration:
    
        ###############################################################################
        #
        #  ACCESS CONTROL 
        #
         
        # system
        view   systemonly  included   .1.3.6.1.2.1
        # frrouting ospf6
        view   systemonly  included   .1.3.6.1.3.102
        # lldpd (Note: lldpd must be restarted with the -x option
        #     configured in order to send info to snmpd via Agent X
        view   systemonly  included   .1.0.8802.1.1.2
        # Cumulus specific
        view   systemonly  included   .1.3.6.1.4.1.40310.1
        view   systemonly  included   .1.3.6.1.4.1.40310.2

3.  Restart `snmpd`:
    
        cumulus@switch:~$ sudo systemctl restart snmpd.service

### <span>Configuring SNMPv3</span>

SNMPv3 is often used to enable authentication and encryption, as
community strings in versions 1 and 2c are sent in plaintext. SNMPv3
usernames are added to the `/etc/snmp/snmpd.conf` file, along with
plaintext authentication and encryption pass phrases.

The NCLU command structures for configuring SNMP user passwords are:

    cumulus@switch:~$ net add snmp-server username <username> [auth-none] | [(auth-md5 | auth-sha) <auth-password>]
    cumulus@switch:~$ net add snmp-server username <username> auth-(none | sha | md5)  (oid <OID> | view <view>)

An example is shown below, defining five users, each with a different
combination of authentication and encryption:

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
    #createUser user1
     
    # user with MD5 authentication
    #createUser user2 MD5 user2password
     
    # user with MD5 for auth and DES for encryption
    #createUser user3 MD5 user3password DES user3encryption
     
    # user666 with SHA for authentication and AES for encryption
    createUser user666 SHA user666password AES user666encryption
     
    # user999 with MD5 for authentication and DES for encryption
    createUser user999 MD5 user999password DES user999encryption
     
    # restrict users to certain OIDs
    # (Note: creating rouser or rwuser will give
    # access regardless of the createUser command above. However,
    # createUser without rouser or rwuser will not provide any access).
    rouser user1 noauth 1.3.6.1.2.1
    rouser user2 auth 1.3.6.1.2.1
    rwuser user3 priv 1.3.6.1.2.1
    rwuser user666
    rwuser user999

After configuring user passwords and restarting the `snmpd` daemon, the
user access can be checked with a client.

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

A slightly more secure method of configuring SNMPv3 users without
creating cleartext passwords is the following:

1.  Install the `net-snmp-config` script that is in `libsnmp-dev`
    package:
    
        cumulus@switch:~$ sudo -E apt-get update
        cumulus@switch:~$ sudo -E apt-get install libsnmp-dev

2.  Stop the daemon:
    
        cumulus@switch:~$ sudo systemctl stop snmpd.service

3.  Use the `net-snmp-config` command to create two users, one with MD5
    and DES, and the next with SHA and AES.
    
    {{%notice note%}}
    
    The minimum password length is 8 characters and the arguments `-a`
    and `-x` to `net-snmp-config` have different meanings than they do
    for `snmpwalk`.
    
    {{%/notice%}}
    
        cumulus@switch:~$ sudo net-snmp-config --create-snmpv3-user -a md5authpass -x desprivpass -A MD5 -X DES userMD5withDES 
        cumulus@switch:~$ sudo net-snmp-config --create-snmpv3-user -a shaauthpass -x aesprivpass -A SHA -X AES userSHAwithAES
        cumulus@switch:~$ sudo systemctl start snmpd.service

This adds a `createUser` command in `/var/lib/snmp/snmpd.conf`. Do
**not** edit this file by hand, unless you are removing usernames. It
also adds the rwuser in `/usr/share/snmp/snmpd.conf`. You may want to
edit this file and restrict access to certain parts of the MIB by adding
*noauth*, *auth* or *priv* to allow unauthenticated access, require
authentication or to enforce use of encryption, respectively.

The `snmpd` daemon reads the information from the
`/var/lib/snmp/snpmd.conf` file and then the line is removed
(eliminating the storage of the master password for that user) and
replaced with the key that is derived from it (using the EngineID). This
key is a localized key, so that if it is stolen it cannot be used to
access other agents. To remove the two users userMD5withDES and
userSHAwithAES, you need simply stop the `snmpd` daemon and edit the
files `/var/lib/snmp/snmpd.conf` and `/usr/share/snmp/snmpd.conf`.
Simply remove the lines containing the username. Then restart the
`snmpd` daemon as in step 3 above.

From a client, you would access the MIB with the correct credentials.
(Again, note that the roles of `-x`, `-a` and `-X` and `-A` are reversed
on the client side as compared with the `net-snmp-config` command used
above.)

    snmpwalk -v 3 -u userMD5withDES -l authPriv -a MD5 -x DES -A md5authpass -X desprivpass localhost 1.3.6.1.2.1.1.1
    snmpwalk -v 3 -u userSHAwithAES -l authPriv -a SHA -x AES -A shaauthpass -X aesprivpass localhost 1.3.6.1.2.1.1.1

## <span>snmpwalk a Switch from Another Linux Device</span>

One of the most important ways to troubleshoot is to `snmpwalk` the
switch from another Linux device that can reach the Cumulus Linux
switch.

{{%notice note%}}

`snmpwalk` does not show enterprise MIBs by default (from the
1.3.6.1.4.1 tree); these need to be explicitly named.

{{%/notice%}}

For this demonstration, another switch running Cumulus Linux within the
network is used.

1.  Open `/etc/apt/sources.list` in an editor.

2.  Add the following line, and save the file:
    
        deb http://ftp.us.debian.org/debian/ jessie main non-free

3.  Update the switch:
    
        cumulus@switch:~$ sudo -E apt-get update

4.  Many SNMP clients (`snmpwalk`, `snmpget` and `snmpgetnext`) as well
    as the SNMP agent (`snmpd`) can benefit from having MIBs installed.
    
    {{%notice note%}}
    
    Enabling monitoring for traps with **defaultMonitors** and
    **monitor** (when referring to OIDs by name) require MIBs to be
    installed on the switch.
    
    {{%/notice%}}
    
    Install the `snmp` and `snmp-mibs-downloader` packages:
    
        cumulus@switch:~$ sudo -E apt-get install snmp snmp-mibs-downloader

5.  Verify that the "mibs :" line is commented out in
    `/etc/snmp/snmp.conf`:
    
        #
        # As the snmp packages come without MIB files due to license reasons, loading
        # of MIBs is disabled by default. If you added the MIBs you can reenable
        # loading them by commenting out the following line.
        #mibs :

6.  Perform an `snmpwalk` on the switch. The switch running `snmpd` in
    the demonstration is using IP address 192.168.0.111. It is possible
    to `snmpwalk` the switch from itself. Run the following command,
    which rules out an SNMP problem against a networking problem.
    
        cumulus@switch:~$ snmpwalk -c public -v2c 192.168.0.111  .1
    
    Here is some sample output:
    
        IF-MIB::ifPhysAddress.2 = STRING: 74:e6:e2:f5:a2:80
        IF-MIB::ifPhysAddress.3 = STRING: 0:e0:ec:25:b8:54
        IF-MIB::ifPhysAddress.4 = STRING: 74:e6:e2:f5:a2:81
        IF-MIB::ifPhysAddress.5 = STRING: 74:e6:e2:f5:a2:82
        IF-MIB::ifPhysAddress.6 = STRING: 74:e6:e2:f5:a2:83
        IF-MIB::ifPhysAddress.7 = STRING: 74:e6:e2:f5:a2:84
        IF-MIB::ifPhysAddress.8 = STRING: 74:e6:e2:f5:a2:85
        IF-MIB::ifPhysAddress.9 = STRING: 74:e6:e2:f5:a2:86
        IF-MIB::ifPhysAddress.10 = STRING: 74:e6:e2:f5:a2:87
        IF-MIB::ifPhysAddress.11 = STRING: 74:e6:e2:f5:a2:88
        IF-MIB::ifPhysAddress.12 = STRING: 74:e6:e2:f5:a2:89
        IF-MIB::ifPhysAddress.13 = STRING: 74:e6:e2:f5:a2:8a
        IF-MIB::ifPhysAddress.14 = STRING: 74:e6:e2:f5:a2:8b
        IF-MIB::ifPhysAddress.15 = STRING: 74:e6:e2:f5:a2:8c
        IF-MIB::ifPhysAddress.16 = STRING: 74:e6:e2:f5:a2:8d
        IF-MIB::ifPhysAddress.17 = STRING: 74:e6:e2:f5:a2:8e
        IF-MIB::ifPhysAddress.18 = STRING: 74:e6:e2:f5:a2:8f
        IF-MIB::ifPhysAddress.19 = STRING: 74:e6:e2:f5:a2:90

Any information gathered here should verify that `snmpd` is running
correctly on the Cumulus Linux side, reducing locations where a problem
may reside.

### <span>Troubleshooting Tips Table for snmpwalks</span>

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Run snmpwalk from</p></th>
<th><p>If it works</p></th>
<th><p>If it does not work</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><strong>switch</strong> (switch to monitor)</p></td>
<td><p><code>snmpd</code> is serving information correctly.</p>
<p>The problem resides somewhere else. For example, network connectivity, or Prism misconfiguration.</p></td>
<td><p>Is snmpd misconfigured or installed incorrectly?</p></td>
</tr>
<tr class="even">
<td><p><strong>switch2</strong> (another Cumulus Linux switch in the network)</p></td>
<td><p><code>snmpd</code> is serving information correctly and network reachability works between <strong>switch</strong> and <strong>switch2</strong>.</p>
<p>The problem resides somewhere else. For example, Prism cannot reach <strong>switch</strong>, or there is a Prism misconfiguration.</p></td>
<td><p>Network connectivity is not able to grab information?<br />
Is there an <code>iptables</code> rule blocking? Is the <code>snmpwalk</code> being run correctly?</p></td>
</tr>
<tr class="odd">
<td><p><strong><a href="/version/cumulus-linux-35/Monitoring_and_Troubleshooting/SNMP_Monitoring/Using_Nutanix_Prism_as_a_Monitoring_Tool">Nutanix Prism CLI</a></strong> (SSH to the cluster IP address)</p></td>
<td><p><code>snmpd</code> is serving information correctly and network reachability works between <strong>switch</strong> and the <strong>Nutanix Appliance</strong>.</p>
<p>The problem resides somewhere else. For example, the GUI might be misconfigured.</p></td>
<td><p>Is the right community name being used in the GUI? Is <code>snmp v2c</code> being used?</p></td>
</tr>
</tbody>
</table>

## <span>SNMP Traps</span>

### <span>Generating Event Notification Traps</span>

The Net-SNMP agent provides a method to generate SNMP trap events via
the Distributed Management (DisMan) Event MIB for various system events,
including:

  - Link up/down.

  - Exceeding the temperature sensor threshold, CPU load or memory
    threshold.

  - Other SNMP MIBs.

Iin order to enable specific types of traps, you need to create the
following configurations in `/etc/snmp/snmpd.conf`.

#### <span>Defining Access Credentials</span>

An SNMPv3 username is required to authorize the DisMan service even
though you are not configuring SNMPv3 here. The example `snmpd.conf`
configuration shown below creates *trapusername* as the username using
the `createUser` command. `iquerySecName` defines the default SNMPv3
username to be used when making internal queries to retrieve monitored
expressions. `rouser` specifies which username should be used for these
SNMPv3 queries. All three are required for `snmpd` to retrieve
information and send traps (even with the **monitor** command shown
below in the examples). Add the following lines to your
`/etc/snmp/snmpd.conf` configuration file:

    createUser trapusername
    iquerySecName trapusername
    rouser trapusername

{{%notice note%}}

`iquerySecName` specifies the default SNMPv3 username to be used when
making internal queries to retrieve any necessary information — either
for evaluating the monitored expression or building a notification
payload. These internal queries always use SNMPv3, even if normal
querying of the agent is done using SNMPv1 or SNMPv2c. Note that this
user must also be explicitly created via `createUser` and given
appropriate access rights, for `rouser`, for example. The
`iquerySecName` directive is purely concerned with defining which user
should be used, not with actually setting this user up.

{{%/notice%}}

#### <span>Defining Trap Receivers</span>

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
Non-authorized traps/informs will be dropped. Please refer to the
[snmptrapd.conf(5) manual
page](http://www.net-snmp.org/docs/man/snmptrapd.conf.html) for details.

{{%/notice%}}

{{%notice note%}}

It is possible to define multiple trap receivers and to use the domain
name instead of an IP address in the `trap2sink` directive.

{{%/notice%}}

Once configured, restart the `snmpd` service to apply the changes.

    cumulus@switch:~$ sudo systemctl restart snmpd.service

#### <span>SNMP Version 3 Trap and Inform Messages</span>

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

#### <span>Sourcing Traps from a Different Source IP Address</span>

When client SNMP programs (such as `snmpget`, `snmpwalk` or `snmptrap`)
are run from the command line, or when `snmpd` is configured to send a
trap (based on `snmpd.conf`), you can configure a *clientaddr* in
`snmp.conf` that allow the SNMP client programs or snmpd (for traps) to
source requests from a different source IP address.

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

#### <span>Monitoring Fans, Power Supplies and Transformers</span>

The usual behavior of an SNMP agent (`snmpd`) is to wait for incoming
SNMP requests and respond to them. If no requests are received, an agent
will typically not initiate any actions. However, various commands can
configure `snmpd` to send traps based on preconfigured settings (`load`,
`file`, `proc`, `disk` or `swap` commands) or customized `monitor`
commands.

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

`snmpd` can be configured to monitor the operational status of an Entity
MIB or Entity-Sensor MIB. The operational status, given as a value of
*ok(1)*, *unavailable(2)* or *nonoperational(3)*, can be determined by
adding the following example configuration to `/etc/snmp/snmpd.conf`,
and adjusting the values:

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
    
    The OID name can be used if the `snmp-mibs-downloader` package is
    installed.
    
    {{%/notice%}}
    
    {{%notice note%}}
    
    The `entPhySensorOperStatus` integer can be found by walking the
    `entPhysicalName` table.
    
    {{%/notice%}}

  - To get all sensor information, run `snmpwalk` on the entPhysicalName
    table. For example:
    
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

#### <span>Enabling MIB to OID Translation</span>

MIB names can be used instead of OIDs, by installing the
`snmp-mibs-downloader`, to download SNMP MIBs to the switch prior to
enabling traps. This greatly improves the readability of the
`snmpd.conf` file.

1.  Open `/etc/apt/sources.list` in a text editor.

2.  Add the `non-free` repository, and save the file:
    
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

7.  Once the configuration has been confirmed, remove or comment out the
    `non-free` repository in `/etc/apt/sources.list`.
    
        #deb http://ftp.us.debian.org/debian/ jessie main non-free

#### <span>Configuring Link Up/Down Notifications</span>

The `linkUpDownNotifications` directive is used to configure link
up/down notifications when the operational status of the link changes.

    linkUpDownNotifications yes

{{%notice note%}}

The default frequency for checking link up/down is 60 seconds. The
default frequency can be changed using the `monitor` directive directly
instead of the `linkUpDownNotifications` directive. See `man snmpd.conf`
for details.

{{%/notice%}}

#### <span>Configuring Temperature Notifications</span>

Temperature sensor information for each available sensor is maintained
in the the lmSensors MIB. Each platform may contain a different number
of temperature sensors. The example below generates a trap event when
any temperature sensors exceeds a threshold of 68 degrees (centigrade).
It monitors each `lmTempSensorsValue`. When the threshold value is
checked and exceeds the `lmTempSensorsValue`, a trap is generated. The
`-o lmTempSenesorsDevice` option is used to instruct SNMP to also
include the lmTempSensorsDevice MIB in the generated trap. The default
frequency for the `monitor` directive is 600 seconds. The default
frequency may be changed using the `-r` option.:

    monitor lmTemSensor -o lmTempSensorsDevice lmTempSensorsValue > 68000

Alternatively, temperature sensors may be monitored individually. To
monitor the sensors individually, first use the `sensors` command to
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
temperature sensors available. The following monitor directive can be
used to monitor only temperature sensor three at five minute intervals.

    monitor -I -r 300 lmTemSensor3 -o lmTempSensorsDevice.3 lmTempSensorsValue.3 > 68000

#### <span>Configuring Free Memory Notifications</span>

You can monitor free memory using the following directives. The example
below generates a trap when free memory drops below 1,000,000KB. The
free memory trap also includes the amount of total real memory:

    monitor MemFreeTotal -o memTotalReal memTotalFree <  1000000

#### <span>Configuring Processor Load Notifications</span>

To monitor CPU load for 1, 5 or 15 minute intervals, use the `load`
directive in conjunction with the `monitor` directive. The following
example will generate a trap when the 1 minute interval reaches 12%, the
5 minute interval reaches 10% or the 15 minute interval reaches 5%.

    load 12 10 5

#### <span>Configuring Disk Utilization Notifications</span>

To monitor disk utilization for all disks, use the `includeAllDisks`
directive in conjunction with the `monitor` directive. The example code
below generates a trap when a disk is 99% full:

    includeAllDisks 1%
    monitor -r 60 -o dskPath -o DiskErrMsg "dskTable" diskErrorFlag !=0

#### <span>Configuring Authentication Notifications</span>

To generate authentication failure traps, use the `authtrapenable`
directive:

    authtrapenable 1

### <span>snmptrapd.conf</span>

To **receive** SNMP traps, the Net-SNMP trap daemon can be used on the
switch. The configuration file, `/etc/snmp/snmptrapd.conf`, is used to
configure how **incoming** traps should be processed. Starting with
release 5.3, it is necessary to explicitly specify who is authorized to
send traps and informs to the notification receiver (and what types of
processing these are allowed to trigger). There are currently three
types of processing that can be specified:

  - *log*: Logs the details of the notification, in a specified file, to
    standard output (or stderr), or via syslog (or similar).

  - *execute*: Passes the details of the trap to a specified handler
    program, including embedded Perl.

  - *net*: Forwards the trap to another notification receiver.

Most commonly, this configuration typically is *log,execute,net* to
cover any style of processing for a particular category of notification.
But it is possible (even desirable) to limit certain notification
sources to selected processing only.

`authCommunity TYPES COMMUNITY [SOURCE [OID | -v VIEW ]]` authorizes
traps and SNMPv2c INFORM requests with the specified community to
trigger the types of processing listed. By default, this allows any
notification using this community to be processed. The SOURCE field can
be used to specify that the configuration should only apply to
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

## <span id="src-8357390_SNMPMonitoring-supported_mibs" class="confluence-anchor-link"></span><span>Supported MIBs</span>

Below are the MIBs supported by Cumulus Linux, as well as suggested uses
for them. The overall Cumulus Linux MIB is defined in
`/usr/share/snmp/mibs/Cumulus-Snmp-MIB.txt`.

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
<td><p>BRIDGE and Q-BRIDGE</p></td>
<td><p>The dot1dBasePortEntry and dot1dBasePortIfIndex tables in the BRIDGE-MIB and dot1qBase, dot1qFdbEntry, dot1qTpFdbEntry, dot1qTpFdbStatus, and the dot1qVlanStaticName tables in the Q-BRIDGE-MIB tables. You must uncomment the <code>bridge_pp.py pass_persist</code> script in <code>/etc/snmp/snmpd.conf</code>.</p></td>
</tr>
<tr class="even">
<td><p>BGP4, OSPF, OSPFV3, RIPv2</p>
<span id="src-8357390_SNMPMonitoring-bgp4"></span></td>
<td><p>FRRouting SNMP support may be enabled to provide support for OSPF-MIB (RFC-1850), OSPFV3-MIB (RFC-5643), and BGP4-MIB (RFC-4273). To enable this support, see the <a href="#src-8357390_SNMPMonitoring-frr">FRRouting section</a> above.</p></td>
</tr>
<tr class="odd">
<td><p>CUMULUS-COUNTERS-MIB</p></td>
<td><p>Discard counters: Cumulus Linux also includes its own counters MIB, defined in <code>/usr/share/snmp/mibs/Cumulus-Counters-MIB.txt</code>. It has the OID <code>.1.3.6.1.4.1.40310.2</code></p></td>
</tr>
<tr class="even">
<td><p>CUMULUS-RESOURCE-QUERY-MIB</p></td>
<td><p>Cumulus Linux includes its own resource utilization MIB, which is similar to using<code> cl-resource-query </code>. It monitors L3 entries by host, route, nexthops, ECMP groups and L2 MAC/BDPU entries. The MIB is defined in <code>/usr/share/snmp/mibs/Cumulus-Resource-Query-MIB.txt</code>, and has the OID <code>.1.3.6.1.4.1.40310.1.</code></p></td>
</tr>
<tr class="odd">
<td><p>CUMULUS-POE-MIB</p></td>
<td><p>The Cumulus Networks custom <a href="/version/cumulus-linux-35/System_Configuration/Power_over_Ethernet_-_PoE">Power over Ethernet</a> PoE MIB defined in <code>/usr/share/snmp/mibs/Cumulus-POE-MIB.txt</code>. For devices that provide PoE, this provides users with the system wide power information in poeSystemValues as well as per interface PoeObjectsEntry values for the poeObjectsTable. Most of this information comes from the <code>poectl</code> command. This MIB is enabled by uncommenting the following line in <code>/etc/snmp/snmpd.conf</code>:</p>
<pre><code>#pass_persist .1.3.6.1.4.1.40310.3 /usr/share/snmp/cl_poe_pp.py</code></pre></td>
</tr>
<tr class="even">
<td><p>DISMAN-EVENT</p></td>
<td><p>Trap monitoring</p></td>
</tr>
<tr class="odd">
<td><p>ENTITY</p></td>
<td><p>From RFC 4133, the temperature sensors, fan sensors, power sensors, and ports are covered.</p></td>
</tr>
<tr class="even">
<td><p>ENTITY-SENSOR</p></td>
<td><p>Physical sensor information (temperature, fan, and power supply) from RFC 3433.</p></td>
</tr>
<tr class="odd">
<td><p>HOST-RESOURCES</p></td>
<td><p>Users, storage, interfaces, process info, run parameters</p></td>
</tr>
<tr class="even">
<td><p>IEEE8023-LAG-MIB</p></td>
<td><p>Implementation of the IEEE 8023-LAG-MIB includes the dot3adAggTable and dot3adAggPortListTable tables. To enable this, edit <code>/etc/snmp/snmpd.conf</code> and uncomment or add the following lines:</p>
<pre><code>view systemonly included .1.2.840.10006.300.43
pass_persist .1.2.840.10006.300.43 /usr/share/snmp/ieee8023_lag_pp.py</code></pre></td>
</tr>
<tr class="odd">
<td><p><a href="http://net-snmp.sourceforge.net/docs/mibs/interfaces.html" class="external-link">IF-MIB</a></p></td>
<td><p>Interface description, type, MTU, speed, MAC, admin, operation status, counters</p>
<p>{{%notice note%}}</p>
<p>The IF-MIB cache is disabled by default. To enable the counter to reflect traffic statistics, remove the <code>-y</code> option from the <code>SNMPDOPTS</code> line in the <code>/etc/default/snmpd</code> file. The example below first shows the original line, commented out, then the modified line without the <code>-y</code> option:</p>
<pre><code>cumulus@switch:~$ cat /etc/default/snmpd
# SNMPDOPTS=&#39;-y -LS 0-4 d -Lf /dev/null -u snmp -g snmp -I -smux -p /run/snmpd.pid&#39;
SNMPDOPTS=&#39;-LS 0-4 d -Lf /dev/null -u snmp -g snmp -I -smux -p /run/snmpd.pid&#39;</code></pre>
<p>{{%/notice%}}</p></td>
</tr>
<tr class="even">
<td><p><a href="http://net-snmp.sourceforge.net/docs/mibs/ip.html" class="external-link">IP (includes ICMP)</a></p></td>
<td><p>IPv4, IPv4 addresses, counters, netmasks</p></td>
</tr>
<tr class="odd">
<td><p>IPv6</p></td>
<td><p>IPv6 counters</p></td>
</tr>
<tr class="even">
<td><p>IP-FORWARD</p></td>
<td><p>IP routing table</p></td>
</tr>
<tr class="odd">
<td><p><a href="http://www.mibdepot.com/cgi-bin/getmib3.cgi?i=1&amp;n=LLDP-MIB&amp;r=cisco&amp;f=LLDP-MIB-V1SMI.my&amp;v=v1&amp;t=tree" class="external-link">LLDP</a></p></td>
<td><p>L2 neighbor info from <code>lldpd</code> (note, you need to <a href="Link_Layer_Discovery_Protocol.html#src-8357430_LinkLayerDiscoveryProtocol-snmp">enable the SNMP subagent</a> in LLDP). <code>lldpd</code> needs to be started with the <code>-x</code> option to enable connectivity to <code>snmpd</code> (AgentX).</p></td>
</tr>
<tr class="even">
<td><p><a href="http://support.ipmonitor.com/mibs_byoidtree.aspx?oid=.1.3.6.1.4.1.2021.13.16" class="external-link">LM-SENSORS MIB</a></p></td>
<td><p>Fan speed, temperature sensor values, voltages. This is deprecated since the ENTITY-SENSOR MIB has been added.</p></td>
</tr>
<tr class="odd">
<td><p>NET-SNMP-AGENT</p></td>
<td><p>Agent timers, user, group config</p></td>
</tr>
<tr class="even">
<td><p>NET-SNMP-EXTEND</p></td>
<td><p>Agent timers, user, group config</p></td>
</tr>
<tr class="odd">
<td><p><a href="http://net-snmp.sourceforge.net/docs/mibs/netSnmpExtendMIB.html" class="external-link">NET-SNMP-EXTEND-MIB</a></p></td>
<td><p>See <a href="https://support.cumulusnetworks.com/hc/en-us/articles/204507848" class="external-link">this knowledge base article</a> on extending NET-SNMP in Cumulus Linux to include data from power supplies, fans and temperature sensors.</p></td>
</tr>
<tr class="even">
<td><p>NET-SNMP-VACM</p></td>
<td><p>Agent timers, user, group config</p></td>
</tr>
<tr class="odd">
<td><p><a href="http://www.net-snmp.org/docs/mibs/notificationLogMIB.html" class="external-link">NOTIFICATION-LOG</a></p></td>
<td><p>Local logging</p></td>
</tr>
<tr class="even">
<td><p><a href="http://net-snmp.sourceforge.net/docs/mibs/snmpFrameworkMIB.html" class="external-link">SNMP-FRAMEWORK</a></p></td>
<td><p>Users, access</p></td>
</tr>
<tr class="odd">
<td><p><a href="http://net-snmp.sourceforge.net/docs/mibs/snmpMPDMIB.html" class="external-link">SNMP-MPD</a></p></td>
<td><p>Users, access</p></td>
</tr>
<tr class="even">
<td><p><a href="http://www.net-snmp.org/docs/mibs/snmpTargetMIB.html" class="external-link">SNMP-TARGET</a></p></td>
<td><p> </p></td>
</tr>
<tr class="odd">
<td><p><a href="http://net-snmp.sourceforge.net/docs/mibs/snmpUsmMIB.html" class="external-link">SNMP-USER-BASED-SM</a></p></td>
<td><p>Users, access</p></td>
</tr>
<tr class="even">
<td><p><a href="http://net-snmp.sourceforge.net/docs/mibs/snmpVacmMIB.html" class="external-link">SNMP-VIEW-BASED-ACM</a></p></td>
<td><p>Users, access</p></td>
</tr>
<tr class="odd">
<td><p><a href="http://net-snmp.sourceforge.net/docs/mibs/snmpMIB.html" class="external-link">SNMPv2</a></p></td>
<td><p>SNMP counters. For information on exposing CPU and memory information via SNMP, see this <a href="https://support.cumulusnetworks.com/hc/en-us/articles/203922988" class="external-link">knowledge base article</a>.</p></td>
</tr>
<tr class="even">
<td><p><a href="http://net-snmp.sourceforge.net/docs/mibs/tcp.html" class="external-link">TCP</a></p></td>
<td><p>TCP related information</p></td>
</tr>
<tr class="odd">
<td><p><a href="http://www.net-snmp.org/docs/mibs/UCD-SNMP-MIB.txt" class="external-link">UCD-SNMP</a></p></td>
<td><p>System memory, load, CPU, disk IO</p></td>
</tr>
<tr class="even">
<td><p><a href="http://net-snmp.sourceforge.net/docs/mibs/udp.html" class="external-link">UDP</a></p></td>
<td><p>UDP related information</p></td>
</tr>
</tbody>
</table>

{{%notice note%}}

The ENTITY MIB does not currently show the chassis information in
Cumulus Linux.

{{%/notice%}}

## <span id="src-8357390_SNMPMonitoring-passpersist" class="confluence-anchor-link"></span><span>About Pass Persist Scripts</span>

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

All the scripts are enabled by default in Cumulus Linux, except for the
`bgp4_pp.py` and `cl_poe_pp.py` scripts:

  - `bgp4_pp.py` is now handled by
    [FRRouting](/version/cumulus-linux-35/Layer_3/FRRouting_Overview/)
    instead of Quagga, so monitoring has changed accordingly.

  - `cl_poe_pp.py` is disabled by default as only some platforms that
    Cumulus Linux supports are capable of doing [Power over
    Ethernet](/version/cumulus-linux-35/System_Configuration/Power_over_Ethernet_-_PoE).

## <span>Troubleshooting</span>

The following commands can be used to troubleshoot potential SNMP
issues:

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
