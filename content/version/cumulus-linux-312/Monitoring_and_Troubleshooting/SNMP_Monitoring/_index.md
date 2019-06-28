---
title: SNMP Monitoring
author: Cumulus Networks
weight: 181
aliases:
 - /display/CL31/SNMP+Monitoring
 - /pages/viewpage.action?pageId=5121965
pageID: 5121965
product: Cumulus Linux
version: 3.1.2
imgData: cumulus-linux-312
siteSlug: cumulus-linux-312
---
Cumulus Linux utilizes the open source Net-SNMP agent `snmpd`, v5.7.3,
which provides support for most of the common industry-wide MIBs,
including interface counters and TCP/UDP IP stack data.

{{%notice note%}}

Cumulus Linux does not prevent customers from extending SNMP features.
However, Cumulus Networks encourages the use of higher performance
monitoring environments, rather than SNMP.

{{%/notice%}}

## <span>Introduction to SNMP (Simple Network Management Protocol)</span>

SNMP is an IETF standards-based network management architecture and
protocol that traces its roots back to Carnegie-Mellon University in
1982. Since then, it's been modified by programmers at the University of
California. In 1995, this code was also made publicly available as the
UCD project. After that, `ucd-snmp` was extended by work done at the
University of Liverpool as well as later in Denmark. In late 2000, the
project name changed to net-snmp and became a fully-fledged
collaborative open source project. The version used by Cumulus Networks
is base on the latest `net-snmp` 5.7.3 branch with added custom MIBs and
pass through and pass persist scripts.

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
included. This section covers a few basic configuration options in
`snmpd.conf`. For more information regarding further configuring this
file, refer to the `snmpd.conf` man page.

{{%notice warning%}}

The default `snmpd.conf` file does not include all supported MIBs or
OIDs that can be exposed.

{{%/notice%}}

{{%notice note%}}

Customers must at least change the default community string for v1 or
v2c environments or the `snmpd` daemon will not respond to any requests.

{{%/notice%}}

### <span>Setting up the Custom Cumulus Networks MIBs</span>

{{%notice note%}}

No changes are required in the `/etc/snmp/snmpd.conf` file on the
switch, in order to support the custom Cumulus Networks MIBs. The
following lines are already included by default:

    view systemonly included .1.3.6.1.4.1.40310.1
    view systemonly included .1.3.6.1.4.1.40310.2
    sysObjectID 1.3.6.1.4.1.40310
    pass_persist .1.3.6.1.4.1.40310.1 /usr/share/snmp/resq_pp.py
    pass_persist .1.3.6.1.4.1.40310.2 /usr/share/snmp/cl_drop_cntrs_pp.py

{{%/notice%}}

However, several files need to be copied to the server, in order for the
custom Cumulus MIB to be recognized on the destination NMS server.

  - `/usr/share/snmp/mibs/Cumulus-Snmp-MIB.txt`

  - `/usr/share/snmp/mibs/Cumulus-Counters-MIB.txt`

  - `/usr/share/snmp/mibs/Cumulus-Resource-Query-MIB.txt`

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
        # quagga ospf6
        view   systemonly  included   .1.3.6.1.3.102
        # lldpd (Note: lldpd must be restarted with the -x option
        #     configured in order to send info to snmpd via Agent X
        view   systemonly  included   .1.0.8802.1.1.2
        # Cumulus specific
        view   systemonly  included   .1.3.6.1.4.1.40310.1
        view   systemonly  included   .1.3.6.1.4.1.40310.2

3.  Restart `snmpd`:
    
        cumulus@switch:~$ sudo systemctl start snmpd.service

### <span>Enabling Public Community</span>

The `snmpd` authentication for versions 1 and 2 is disabled by default
in Cumulus Linux. This password (called a community string) can be
enabled by setting **rocommunity** (for read-only access) or
**rwcommunity** (for read-write acces). To enable read-only querying by
a client:

1.  Open `/etc/snmp/snmpd.conf` in a text editor.

2.  To allow read-only access using a password *public* from any client
    IP address (*default*) for the view you defined before with
    *systemonly*, add the following line to the end of the file, then
    save it:
    
        rocommunity public default -V systemonly
    
    | Syntax      | Meaning                                                                                                                                                                                                                                                                                                |
    | ----------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
    | rocommunity | Read-only community; (*rwcommunity* is for read-write access).                                                                                                                                                                                                                                         |
    | public      | Plain text password.                                                                                                                                                                                                                                                                                   |
    | default     | "default" allows connections from any system. "localhost" allows requests only from the local host. A restricted source can either be a specific hostname (or address), or a subnet, represented as IP/MASK (like 10.10.10.0/255.255.255.0), or IP/BITS (like 10.10.10.0/24), or the IPv6 equivalents. |
    | systemonly  | The name of this particular SNMP view. This is a user-defined value.                                                                                                                                                                                                                                   |
    

3.  Restart `snmpd`:
    
        cumulus@switch:~$ sudo systemctl restart snmpd.service

### <span>Configuring SNMPv3</span>

Since community strings in versions 1 and 2c are sent in the clear,
SNMPv3 is often used to enable authentication and encryption. SNMPv3 was
first release around 2000. A minimal example is shown here for
`/etc/snmp/snmpd.conf` that defines three users, each with a different
combination of authentication and encryption. Please change these
usernames and passwords before using this in a network:

{{%notice note%}}

Make sure you change the usernames and passwords in the sample code
below, as the ones used here are for explanatory purposes only.

{{%/notice%}}

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
    rouser user1 noauth 1.3.6.1.2.1.1
    rouser user2 auth 1.3.6.1.2.1
    rwuser user3 priv 1.3.6.1.2.1
    rwuser user666
    rwuser user999

Once you make this configuration and restart the `snmpd` daemon, the
user access can be checked with a client — the Debian package called
`snmp` contains `snmpget` and `snmpwalk`, as well as other programs that
are useful for checking daemon functionality from the switch itself or
from another workstation. The following commands check the access for
each user defined above from the localhost (the switch itself):

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
    
        cumulus@switch:~$ sudo apt-get update
        cumulus@switch:~$ sudo apt-get install libsnmp-dev

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
switch. For this demonstration, another switch running Cumulus Linux
within the network is used.

1.  Open `/etc/apt/sources.list` in an editor.

2.  Add the following line, and save the file:
    
        deb http://ftp.us.debian.org/debian/ jessie main non-free

3.  Update the switch:
    
        cumulus@switch:~$ sudo apt-get update

4.  Install the `snmp` and `snmp-mibs-downloader` packages:
    
        cumulus@switch:~$ sudo apt-get install snmp snmp-mibs-downloader

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
    
        cumulus@switch:~$ snmpwalk -c public -v2c 192.168.0.111
    
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
<td><p><strong>Nutanix Prism CLI</strong> (SSH to the cluster IP address)</p></td>
<td><p><code>snmpd</code> is serving information correctly and network reachability works between <strong>switch</strong> and the <strong>Nutanix Appliance</strong>.</p>
<p>The problem resides somewhere else. For example, the GUI might be misconfigured.</p></td>
<td><p>Is the right community name being used in the GUI? Is <code>snmp v2c</code> being used?</p></td>
</tr>
</tbody>
</table>

## <span>SNMP Traps</span>

### <span>snmptrapd.conf</span>

The Net-SNMP trap daemon configuration file, `/etc/snmptrapd.conf`, is
used to configure how incoming traps should be processed. For more
information about specific configuration options within the file, run
the following command:

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
    snmpTrapdAddr localhost
    forward default {{global['snmp_server']}}

### <span>Generating Event Notification Traps</span>

The Net-SNMP agent provides a method to generate SNMP trap events, via
the Distributed Management (DisMan) Event MIB, for various system
events, including linkup/down, exceeding the temperature sensor
threshold, CPU load, or memory threshold, or other SNMP MIBs.

#### <span>Monitoring Fans, Power Supplies, or Transformers</span>

SNMP can be configured to monitor the operational status of an Entity
MIB or Entity-Sensor MIB. The operational status, given as a value of
ok(1), unavailable(2), or nonoperational(3), can be determined by adding
the following example configuration to `/etc/snmp/snmpd.conf`, and
adjusting the values:

  - Using the `entPhySensorOperStatus` integer:
    
        # without installing extra MIBS we can check the check Fan1 status
        # if the Fan1 index is 100011001
        monitor -I -r 10  -o 1.3.6.1.2.1.47.1.1.1.1.7.100011001 "Fan1 Not OK"  1.3.6.1.2.1.99.1.1.1.5.100011001 > 1
        # Any Entity Status non OK (greater than 1)
        monitor  -r 10  -o 1.3.6.1.2.1.47.1.1.1.1.7  "Sensor Status Failure"  1.3.6.1.2.1.99.1.1.1.5 > 1
    
    {{%notice note%}}
    
    The `entPhySensorOperStatus` integer can be found by walking the
    `entPhysicalName` table.
    
    {{%/notice%}}
    
    To get all sensor information, run `snmpwalk` on the entPhysicalName
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

  - Using the OID name:
    
        # for a specific fan called Fan1 with an index 100011001
        monitor -I -r 10  -o entPhysicalName.100011001 "Fan1 Not OK"  entPhySensorOperStatus.100011001 > 1
        # for any Entity Status not OK ( greater than 1)
        monitor  -r 10  -o entPhysicalName  "Sensor Status Failure"  entPhySensorOperStatus > 1
    
    {{%notice note%}}
    
    The OID name can be used if the `snmp-mibs-download` package is
    installed.
    
    {{%/notice%}}

#### <span>Enabling MIB to OID Translation</span>

MIB names can be used instead of OIDs, by installing the
`snmp-mibs-downloader`, to download SNMP MIBs to the switch prior to
enabling traps. This greatly improves the readability of the
`snmpd.conf` file.

1.  Open `/etc/apt/sources.list` in a text editor.

2.  Add the `non-free` repository, and save the file:
    
        cumulus@switch:~$ sudo deb http://ftp.us.debian.org/debian/ jessie main non-free

3.  Update the switch:
    
        cumulus@switch:~$ sudo apt-get update

4.  Install the `snmp-mibs-downloader`:
    
        cumulus@switch:~$ sudo apt-get snmp-mibs-downloader

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

#### <span>Configuring Trap Events</span>

The following configurations should be made in `/etc/snmp/snmp.conf`, in
order to enable specific types of traps. Once configured, restart the
`snmpd` service to apply the changes.

    cumulus@switch:~$ sudo systemctl restart snmpd.service

#### <span>Defining Access Credentials</span>

An SNMPv3 username is required to authorize the DisMan service. The
example code below uses `cumulusUser` as the username.

    createUser cumulusUser
    iquerySecName cumulusUser
    rouser cumulusUser

#### <span>Defining Trap Receivers</span>

The example code below creates a trap receiver that is capable of
receiving SNMPv2 traps.

    trap2sink 192.168.1.1 public

{{%notice note%}}

Although the traps are sent to an SNMPV2 receiver, the SNMPv3 user is
still required.

{{%/notice%}}

{{%notice note%}}

It is possible to define multiple trap receivers, and to use the domain
name instead of IP address in the `trap2sink` directive.

{{%/notice%}}

#### <span>Configuring LinkUp/Down Notifications</span>

The `linkUpDownNotifications` directive is used to configure linkup/down
notifications when the operational status of the link changes.

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
    monitor -r 60 -o laNames -o laErrMessage "laTable" laErrorFlag !=0

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

## <span id="src-5121965_SNMPMonitoring-supported_mibs" class="confluence-anchor-link"></span><span>Supported MIBs</span>

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
<td><p>BGP4</p>
<span id="src-5121965_SNMPMonitoring-bgp4"></span></td>
<td><p>Implementation of the BGP4 MIB (RFC 4273) which includes bgpPeerTable and bgp4PathAttrTable. By default, the <code>bgp4_pp.py</code> script does not show the bgp4PathAttrTable since this can be very large and result in a periodic CPU spike. To enable this table, add <em>--include-paths</em> to the end of the line (as an option) after uncommenting it in the <code>/etc/snmp/snmpd.conf</code> configuration file.</p>
<pre><code>#pass_persist .1.3.6.1.2.1.15 /usr/share/snmp/bgp4_pp.py</code></pre></td>
</tr>
<tr class="odd">
<td><p>CUMULUS-COUNTERS-MIB</p></td>
<td><p>Discard counters: Cumulus Linux also includes its own counters MIB, defined in <code>/usr/share/snmp/mibs/Cumulus-Counters-MIB.txt</code>. It has the OID <code>.1.3.6.1.4.1.40310.2</code></p></td>
</tr>
<tr class="even">
<td><p>CUMULUS-RESOURCE-QUERY-MIB</p></td>
<td><p>Cumulus Linux includes its own resource utilization MIB, which is similar to using <code>cl-resource-query </code>. It monitors L3 entries by host, route, nexthops, ECMP groups and L2 MAC/BDPU entries. The MIB is defined in <code>/usr/share/snmp/mibs/Cumulus-Resource-Query-MIB.txt</code>, and has the OID <code>.1.3.6.1.4.1.40310.1.</code></p></td>
</tr>
<tr class="odd">
<td><p>CUMULUS-POE-MIB</p></td>
<td><p>The Cumulus Networks custom <a href="/version/cumulus-linux-312/System_Management/Power_over_Ethernet_-_PoE">Power over Ethernet</a> PoE MIB defined in <code>/usr/share/snmp/mibs/Cumulus-POE-MIB.txt</code>. For devices that provide PoE, this provides users with the system wide power information in poeSystemValues as well as per interface PoeObjectsEntry values for the poeObjectsTable. Most of this information comes from the <code>poectl</code> command. This MIB is enabled by uncommenting the following line in <code>/etc/snmp/snmpd.conf</code>:</p>
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
<td><p><a href="http://net-snmp.sourceforge.net/docs/mibs/interfaces.html" class="external-link">IF-MIB</a></p></td>
<td><p>Interface description, type, MTU, speed, MAC, admin, operation status, counters</p></td>
</tr>
<tr class="odd">
<td><p><a href="http://net-snmp.sourceforge.net/docs/mibs/ip.html" class="external-link">IP (includes ICMP)</a></p></td>
<td><p>IPv4, IPv4 addresses, counters, netmasks</p></td>
</tr>
<tr class="even">
<td><p>IPv6</p></td>
<td><p>IPv6 counters</p></td>
</tr>
<tr class="odd">
<td><p>IP-FORWARD</p></td>
<td><p>IP routing table</p></td>
</tr>
<tr class="even">
<td><p><a href="http://www.mibdepot.com/cgi-bin/getmib3.cgi?i=1&amp;n=LLDP-MIB&amp;r=cisco&amp;f=LLDP-MIB-V1SMI.my&amp;v=v1&amp;t=tree" class="external-link">LLDP</a></p></td>
<td><p>L2 neighbor info from <code>lldpd</code> (note, you need to <a href="Link_Layer_Discovery_Protocol.html#src-5122001_LinkLayerDiscoveryProtocol-snmp">enable the SNMP subagent</a> in LLDP). <code>lldpd</code> needs to be started with the <code>-x</code> option to enable connectivity to <code>snmpd</code> (AgentX).</p></td>
</tr>
<tr class="odd">
<td><p><a href="http://support.ipmonitor.com/mibs_byoidtree.aspx?oid=.1.3.6.1.4.1.2021.13.16" class="external-link">LM-SENSORS MIB</a></p></td>
<td><p>Fan speed, temperature sensor values, voltages. This is deprecated since the ENTITY-SENSOR MIB has been added.</p></td>
</tr>
<tr class="even">
<td><p>NET-SNMP-AGENT</p></td>
<td><p>Agent timers, user, group config</p></td>
</tr>
<tr class="odd">
<td><p>NET-SNMP-EXTEND</p></td>
<td><p>Agent timers, user, group config</p></td>
</tr>
<tr class="even">
<td><p><a href="http://net-snmp.sourceforge.net/docs/mibs/netSnmpExtendMIB.html" class="external-link">NET-SNMP-EXTEND-MIB</a></p></td>
<td><p>(See also <a href="https://support.cumulusnetworks.com/hc/en-us/articles/204507848" class="external-link">this knowledge base article</a> on extending NET-SNMP in Cumulus Linux to include data from power supplies, fans and temperature sensors.)</p></td>
</tr>
<tr class="odd">
<td><p>NET-SNMP-VACM</p></td>
<td><p>Agent timers, user, group config</p></td>
</tr>
<tr class="even">
<td><p><a href="http://www.net-snmp.org/docs/mibs/notificationLogMIB.html" class="external-link">NOTIFICATION-LOG</a></p></td>
<td><p>Local logging</p></td>
</tr>
<tr class="odd">
<td><p><a href="http://net-snmp.sourceforge.net/docs/mibs/snmpFrameworkMIB.html" class="external-link">SNMP-FRAMEWORK</a></p></td>
<td><p>Users, access</p></td>
</tr>
<tr class="even">
<td><p><a href="http://net-snmp.sourceforge.net/docs/mibs/snmpMPDMIB.html" class="external-link">SNMP-MPD</a></p></td>
<td><p>Users, access</p></td>
</tr>
<tr class="odd">
<td><p><a href="http://www.net-snmp.org/docs/mibs/snmpTargetMIB.html" class="external-link">SNMP-TARGET</a></p></td>
<td><p> </p></td>
</tr>
<tr class="even">
<td><p><a href="http://net-snmp.sourceforge.net/docs/mibs/snmpUsmMIB.html" class="external-link">SNMP-USER-BASED-SM</a></p></td>
<td><p>Users, access</p></td>
</tr>
<tr class="odd">
<td><p><a href="http://net-snmp.sourceforge.net/docs/mibs/snmpVacmMIB.html" class="external-link">SNMP-VIEW-BASED-ACM</a></p></td>
<td><p>Users, access</p></td>
</tr>
<tr class="even">
<td><p><a href="http://net-snmp.sourceforge.net/docs/mibs/snmpMIB.html" class="external-link">SNMPv2</a></p></td>
<td><p>SNMP counters (For information on exposing CPU and memory information via SNMP, see this <a href="https://support.cumulusnetworks.com/hc/en-us/articles/203922988" class="external-link">knowledge base article</a>.)</p></td>
</tr>
<tr class="odd">
<td><p><a href="http://net-snmp.sourceforge.net/docs/mibs/tcp.html" class="external-link">TCP</a></p></td>
<td><p>TCP related information</p></td>
</tr>
<tr class="even">
<td><p><a href="http://www.net-snmp.org/docs/mibs/UCD-SNMP-MIB.txt" class="external-link">UCD-SNMP</a></p></td>
<td><p>System memory, load, CPU, disk IO</p></td>
</tr>
<tr class="odd">
<td><p><a href="http://net-snmp.sourceforge.net/docs/mibs/udp.html" class="external-link">UDP</a></p></td>
<td><p>UDP related information</p></td>
</tr>
</tbody>
</table>

{{%notice note%}}

Due to licensing restrictions, SNMP support within Quagga has been
disabled and not included in Cumulus Linux.

However, Cumulus Linux does support the BGP4 MIB (RFC 4273), which
includes bgpPeerTable and bgp4PathAttrTable. By default, the pass
persist script `bgp4_pp.py` does not show the bgp4PathAttrTable since it
can be very large and result in a periodic CPU spike.

To enable this table, [see above](#src-5121965_SNMPMonitoring-bgp4).

{{%/notice%}}

{{%notice note%}}

The ENTITY MIB does not currently show the chassis information in
Cumulus Linux 3.1.

{{%/notice%}}
