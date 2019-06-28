---
title: TACACS Plus
author: Cumulus Networks
weight: 271
aliases:
 - /display/CL34/TACACS+Plus
 - /pages/viewpage.action?pageId=7112316
pageID: 7112316
product: Cumulus Linux
version: 3.4.3
imgData: cumulus-linux-343
siteSlug: cumulus-linux-343
---
Cumulus Linux implements TACACS+ client AAA (Accounting, Authentication,
and Authorization) in a transparent way with minimal configuration.
There is no need to create accounts or directories on the switch.
Authentication is handled via PAM, and includes `login`, `ssh`, `sudo`,
and `su`. Accounting records are sent to all configuredTACACS+ servers
by default. Use of per-command authorization requires additional setup
on the switch.

By default, TACACS+ privilege 15 users are allowed to run any command
with sudo via the `/etc/sudoers.d/tacplus` file that is installed by the
`libtacplus-map1` package.

## <span>Installing the TACACS+ Client Packages</span>

TACACS+ requires the following packages to be installed on Cumulus
Linux. They are not part of the base Cumulus Linux image installation.
All required packages can be installed easily with these commands:

    cumulus@switch:~$ sudo -E apt-get update
    cumulus@switch:~$ sudo -E apt-get install tacplus-client

## <span>Configuring the TACACS+ Client</span>

Post-installation TACACS+ configuration requires (at minimum) editting
only one file, /etc/tacplus\_servers. It is necessary add at least one
server, and usually one shared secret (key). The `server` and secret
parameters can be given in any order, and must not include any
whitespace (spaces or tabs), and can be added anywhere in the file. For
example, if your TACACS+ server IP address is `192.168.0.30`, and your
shared secret is ` tacacskey  `then you would add these parameters to` 
/etc/tacplus_servers: `

    secret=tacacskey
    server=192.168.0.30

Up to 7 TACACS+ servers are supported. Connections are made in the order
in which they are listed in this file. In most cases, no other
parameters need to be changed. All parameters used by any of the
packages can be added to this file, and will affect all the TACACS+
client software. It is also possible to configure some of the packages
through individual configuration files. For example, the timeout value
(see description below) is set to 5 seconds by default for NSS lookups
in `/etc/tacplus_nss.conf`, while other packages use a value of 10
seconds, set in /`etc/tacplus_servers.`

When TACACS+ servers or secrets are added or removed, `auditd` must be
restarted (with `systemctl restart auditd`) or a signal must be sent
(with `killall -HUP audisp-tacplus`) before `audisp-tacplus` will reread
the configuration to see the changed server list. Usually this is an
issue only at first change to the configuration.

At this point, the Cumulus Linux switch should be able to query the
TACACS server.

This is the complete list of the TACACS+ client configuration files, and
their use. The full list of TACACS+ parameters is below at **TACACS
Parameters** below.

| Filename                                | Description                                                                                                                                                                                                                                                                                                                                                                                           |
| --------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| /etc/tacplus\_servers                   | This is the primary file that requires configuration post-installation, and is used by all packages via ` include=/etc/tacplus_servers parameters in the other configuration files,  `when installed. Since this is usually the file with the shared secrets, it should not be world readable (should be Linux file mode 600).                                                                        |
| /etc/nsswitch.conf                      | When the `libnss_tacplus` package is installed, this file is configured to enable tacplus lookups via `libnss_tacplus`. If this file is replaced by automation or other means, you will need to add tacplus as the first lookup method for the *passwd* database line.                                                                                                                                |
| /etc/tacplus\_nss.conf                  | This file sets the basic parameters for `libnss_tacplus`. It includes a debug variable for debugging NSS lookups separately from other client packages.                                                                                                                                                                                                                                               |
| /usr/share/pam-configs/tacplus          | Configuration file for `pam-auth-update` to generate the files in the next row. These configurations are used at `login`, by `su`, and by `ssh`.                                                                                                                                                                                                                                                      |
| /etc/pam.d/common-\*                    | The `/etc/pam.d/common-*` files are updated for `tacplus` authentication. The files are updated with `pam-auth-update`, when `libpam-tacplus` is installed or removed.                                                                                                                                                                                                                                |
| /etc/sudoers.d/tacplus                  | This file allows TACACS+ privilege level 15 users to run commands with `sudo`. It also includes an example (commented out) showing how to enable privilege level 15 TACACS users to use `sudo` without having to enter a password, and an example of how to enable all TACACS users to run specific commands via sudo. It should only be editted with the command: *visudo -f /etc/sudoers.d/tacplus* |
| audisp-tacplus.conf                     | `audisp` plugin configuration file. In general, no modifications are required.                                                                                                                                                                                                                                                                                                                        |
| /etc/audisp/audisp-tac\_plus.conf       | TACACS+ server configuration file for accounting. In general, no modifications are required. It may be useful to use this configuration file when you only want to debug TACACS+ accounting issues, not all TACACS+ users.                                                                                                                                                                            |
| /etc/audit/rules.d/audisp-tacplus.rules | The `auditd` rules for TACACS+ accounting. The `augenrules` command uses all rules files to generate the file rules file (below)                                                                                                                                                                                                                                                                      |
| /etc/audit/audit.rules                  | Audit rules file generated during `auditd` installation.                                                                                                                                                                                                                                                                                                                                              |

{{%notice warning%}}

The `/etc/pam.d/common-*` files can be edited manually. However, if
`pam-auth-update` is run again after the changes are made, the update
will fail. Configuration should be done in
`/usr/share/pam-configs/tacplus` instead, followed by running
`pam-auth-update`.

{{%/notice%}}

## <span>TACACS+ Authentication (login)</span>

The initial authentication configuration is done through the PAM
modules, and an updated version of the `libpam-tacplus` package. When
the package is installed, the PAM configuration is updated in
`/etc/pam.d` with the `pam-auth-update` command. If you have made
changes to your PAM configuration, you may need to integrate these
changes yourself. If you are also using LDAP with the ` libpam-ldap
 `package, you will need to edit the PAM configuration to ensure the
LDAP and TACACS ordering that you prefer. The `libpam-tacplus` are
configured to skip over rules, and the values in the ` success=2  `may
require adjustments to skip over LDAP rules.

{{%notice note%}}

TACACS+ users at privilege levels other than 15 are not allowed to run
`sudo` commands by default, and are limited to commands that can be run
with standard Linux user permissions.

{{%/notice%}}

## <span>TACACS+ Accounting</span>

TACACS+ accounting is implemented with the `audisp` module, with an
additional plugin for `auditd`/`audisp`. The plugin maps the auid in the
accounting record to a TACACS login, based on the auid and sessionid.
The `audisp` module requires `libnss_tacplus`, and uses the
`libtacplus_map.so` library interfaces as part of the modified
`libpam_tacplus` package.

Communication with the TACACS+ servers is done via the
`libsimple-tacact1` library, through `dlopen()`. A maximum of 240 bytes
of command name and arguments are sent in the accounting record, due to
the TACACS+ field length limitation of 255 bytes.

{{%notice note%}}

All Linux commands result in an accounting record, including commands
run as part of the login process or as a sub-processes of other
commands. This can sometimes generate a large number of accounting
records.

{{%/notice%}}

The IP address and encryption key of the server should be configured in
the `/etc/tacplus_servers` file. Minimal configuration to `auditd` and
`audisp` is necessary to enable the audit records necessary for
accounting. These records are installed as part of the package.

`audisp-tacplus` installs the audit rules for command accounting.
Modifying the configuration files is not usually necessary. However,
when a [management
VRF](/version/cumulus-linux-343/Layer_Three/Management_VRF) is
configured, the accounting configuration does need special modification,
because the `auditd` service starts prior to networking. It is necessary
add the *vrf* parameter, and to signal the `audisp-tacplus` process to
reread the configuration. The example below shows that the management
VRF is named *mgmt*. The *vrf* parameter can be placed in either
`/etc/tacplus_servers` or in `/etc/audisp/audisp-tac_plus.conf`.

    vrf=mgmt

After editing the configuration file, notify the accounting process to
reread it by sending the **HUP** signal: `killall -HUP audisp-tacplus`.

{{%notice note%}}

All `sudo` commands run by TACACS+ users generate accounting records
against the original TACACS+ login name.

{{%/notice%}}

For more information, refer to the `audisp.8` and `auditd.8` man pages.

## <span id="src-7112316_TACACSPlus-nclu" class="confluence-anchor-link"></span><span>Configuring NCLU for TACACS+ Users</span>

[NCLU](/version/cumulus-linux-343/System_Configuration/Network_Command_Line_Utility_-_NCLU)
has its own configuration file to enable TACACS+ privilege level 0 users
to run the `net` command. Edit the `/etc/netd.conf` file, then:

  - To give a TACACS+ user access to the show commands, add that user to
    the `users_with_show` line, then add the *tacacs* group to the
    `groups_with_show` line.

  - To give a TACACS+ user access to the edit commands (for all the NCLU
    write commands and to restart services with NCLU), add that user to
    the `users_with_edit` line.

<!-- end list -->

    cumulus@switch:~$ sudo nano /etc/netd.conf
     
    ...
     
    # Control which users/groups are allowed to run 'add', 'del',
    # 'clear', 'net abort', 'net commit' and restart services
    # to apply those changes
    users_with_edit = root, cumulus, TACACS_USER
    groups_with_edit = netedit
     
    # Control which users/groups are allowed to run 'show' commands
    users_with_show = root, cumulus, tacacs_user
    groups_with_show = netshow, TACACS_USER
     
    ...

{{%notice note%}}

TACACS\_USER in the above output is actually the username of the account
logged in via TACACS.

{{%/notice%}}

{{%notice warning%}}

Do not add the *tacacs* group to the `groups_with_edit` line, as this is
dangerous and can potentially enable any user to log into the switch as
the root user.

{{%/notice%}}

If the user/command combination is not authorized by the TACACS+ server,
a message similar to the following gets displayed:

    tacuser0@switch:~$ net show version
    net not authorized by TACACS+ with given arguments, not executing

## <span>TACACS+ Per-command Authorization</span>

Per-command authorization is handled with the `tacplus-auth` command. To
make this an enforced authorization, the TACACS+ login must be changed
to use a restricted shell, with a very limited executable search path.
Otherwise, the user can bypass the authorization. The `tacplus-restrict`
utility simplifies the setup of the restricted environment. The example
below initializes the environment for the *tacacs0* user account. This
is the account used for TACACS+ users at privilege level `0`.

    tacuser0@switch:~$ sudo tacplus-restrict -i -u tacacs0 -a command1 command2 ... commandN

### <span>Command Options</span>

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Option</p></th>
<th><p>Description</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>-i</p></td>
<td><p>Initializes the environment. It only needs to be issued once per username.</p></td>
</tr>
<tr class="even">
<td><p>-a</p></td>
<td><p>The utility can be invoked with the <code>-a</code> option as many times as desired. For each command in the <code>-a</code> list, a symbolic link is created from <code>tacplus-auth</code> to the relative portion of the command name in the local <code>bin</code> subdirectory. These commands also need to be enabled on the TACACS+ server. See the server documentation for how to do that. It is common to have the server allow some options to a command, but not others.</p></td>
</tr>
<tr class="odd">
<td><p>-f</p></td>
<td><p>Re-initializes the environment. If you need to start over, issue the <code>-f</code> option with the <code>-i</code> to force the re-initialization; otherwise, repeated use of <code>-i</code> is ignored. As part of the initialization:</p>
<ul>
<li><p>The user's shell is changed to <code>/bin/rbash</code>.</p></li>
<li><p>Any existing dot files are saved.</p></li>
<li><p>A limited environment is set up that does not allow general command execution, but instead allows only commands from the user's local <code>bin</code> subdirectory.</p></li>
</ul></td>
</tr>
</tbody>
</table>

As a full example, if you want to allow the user to be able to run the
`net` and `ip` commands (potentially, if the TACACS+ server authorizes),
use the command:

    cumulus@switch:~$ sudo tacplus-restrict -i -u tacacs0 -a ip net

After running this command, examining the `tacacs0` directory should
show something similar to the following:

    cumulus@switch:~$ sudo ls -lR ~tacacs0
    total 12
    lrwxrwxrwx 1 root root 22 Nov 21 22:07 ip -> /usr/sbin/tacplus-auth
    lrwxrwxrwx 1 root root 22 Nov 21 22:07 net -> /usr/sbin/tacplus-auth

Other than shell built-ins, the only two commands the privilege level 0
TACACS users can run are the `ip` and `net` commands.

If you mistakenly add potential commands with the `-a` option, you can
remove the commands that you don't want (the example below shows the
`net` command):

    cumulus@switch:~$ sudo rm ~tacacs0/bin/net

Or you can remove all the commands with:

    cumulus@switch:~$ sudo rm ~tacacs0/bin/*

Use the `man` command on the switch for more information on
`tacplus-auth` and `tacplus-restrict`.

    cumulus@switch:~$ man tacplus-auth tacplus-restrict

## <span>NSS Plugin</span>

When used with `pam_tacplus`, TACACS+ authenticated users are able to
log in without a local account on the system via the NSS plugin that
comes with the `tacplus_nss` package. The plugin uses the mapped
`tacplus` information if the user is not found in the local password
file, provides the `getpwnam()` and `getpwuid()`entry point,s and uses
the TACACS+ authentication functions.

The plugin asks the TACACS+ server if the user is known, and then for
relevant attributes to determine the user’s privilege level. When the
`libnss_tacplus` package is installed, `nsswitch.conf` is be modified to
set `tacplus` as the first lookup method for `passwd`. If the order is
changed, lookups will return the local accounts such as `tacacs0`

If the user is not found, a mapped lookup is performed using the
`libtacplus_map.so` exported functions. The privilege level is appended
to “tacacs”, and the lookup searches for the name in the local password
file. For example, privilege level 15 will search for the tacacs15 user.
If the user is found, the password structure is filled in with the
user’s information.

If it is not found, the privilege level is decremented and checked
again, until privilege level 0 (user t`acacs0`) is reached. This allows
use of only the two local users `tacacs0` and `tacacs15`, if minimal
configuration is desired.

## <span>TACACS Configuration Parameters</span>

The recognized configuration options are the same as the
`libpam_tacplus` command line arguments; not all `pam_tacplus` options
are supported, however. These configuration parameters are documented in
the `tacplus_servers.5` man page, which is part of the `libpam-tacplus`
package.

The table below describes the configuration options available:

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Configuration Option</p></th>
<th><p>Description</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>debug</p></td>
<td><p>Output debugging information via <code>syslog(3)</code>.</p>
<p>{{%notice note%}}</p>
<p>Debugging is heavy, including passwords. Do not leave debugging enabled on a production switch once you have completed troubleshooting.</p>
<p>{{%/notice%}}</p></td>
</tr>
<tr class="even">
<td><p>secret=STRING</p></td>
<td><p>Secret key used to encrypt/decrypt packets sent to/received from the server. Can be specified more than once, and can be in any order with respect to the server= parameter. When fewer secret= parameters are specified, the last secret given is used for the remaining servers. This parameter should only be put into files such as /etc/tacplus_servers that are not world readable.</p></td>
</tr>
<tr class="odd">
<td><p>server=HOSTNAME</p>
<p>server=IP_ADDR</p></td>
<td><p>Adds a TACACS+ server to the servers list. Servers will be queried in turn until a match is found, or no servers remain in the list. Can be specified up to 7 times. When the IP_ADDR form is used, it can be optionally followed by a port number, preceded by a ":". The default port is 49.</p>
<p>{{%notice note%}}</p>
<p>When sending accounting records, the record is sent to all servers in the list if <code>acct_all=1,</code> which is the default.</p>
<p>{{%/notice%}}</p></td>
</tr>
<tr class="even">
<td><p>timeout=SECONDS</p></td>
<td><p>TACACS+ server(s) communication timeout. The default value is 5 seconds.</p></td>
</tr>
<tr class="odd">
<td><p>login=STRING</p></td>
<td><p>TACACS+ authentication service (pap, chap, or login). The default value is <em>pap</em>.</p></td>
</tr>
<tr class="even">
<td><p>user_homedir=1</p></td>
<td><p>This is not enabled by default. When enabled, a separate home directory for each TACACS+ user is created when the TACACS+ user first logs in. By default, the home directory in the mapping accounts in <code>/etc/passwd</code> (<code>/home/tacacs0</code> ... <code>/home/tacacs15</code>) is used. If the home directory does not exist, it is created with the <code>mkhomedir_helper</code> program, in the same manner as <code>pam_mkhomedir</code>.</p>
<p>This option is not honored for accounts with restricted shells when per-command authorization is enabled.</p></td>
</tr>
<tr class="odd">
<td><p>acct_all=1</p></td>
<td><p>Configuration option for <code>audisp_tacplus</code> and <code>pam_tacplus</code> sending accounting records to all supplied servers (1), or the first server to respond (0). The default value is <em>1</em>.</p></td>
</tr>
<tr class="even">
<td><p>timeout=<strong>SECS</strong></p></td>
<td><p>Sets the timeout in seconds for connections to each TACACS+ server. The default is 10 seconds for all lookups except that NSS lookups use a 5 second timeout.</p></td>
</tr>
<tr class="odd">
<td><p>vrf=<strong>VRFNAME</strong></p></td>
<td><p>If the management network is in a VRF, set this variable to the VRF name. This would usually be "mgmt". When this variable is set, the connection to the TACACS+ accounting servers is made through the named VRF.</p></td>
</tr>
<tr class="even">
<td><p>service</p></td>
<td><p>TACACS+ accounting and authorization service. Examples include shell, pap, raccess, ppp, and slip.</p>
<p>The default value is <em>shell</em>.</p></td>
</tr>
<tr class="odd">
<td><p>protocol</p></td>
<td><p>TACACS+ protocol field. This option is use dependent.</p>
<p>PAM uses the SSH protocol.</p></td>
</tr>
</tbody>
</table>

## <span>Removing the TACACS+ Client Packages</span>

To remove all of the TACACS+ client packages, use the following
commands:

    cumulus@switch:~$ sudo -E apt-get remove tacplus-client
    cumulus@switch:~$ sudo -E apt-get autoremove

To remove the TACACS+ client configuration files as well as the packages
(recommended), use this command:

    cumulus@switch:~$ sudo -E apt-get autoremove --purge

## <span>Troubleshooting TACACS+</span>

### <span>Debugging Basic Server Connectivity or NSS Issues</span>

The `getent` command can be used to determine whether TACACS+ is
configured correctly, and the local password is stored in the
configuration files. In the example commands below, the cumulus user
represents the local user, while cumulusTAC represents the TACACS user.

To look up the username within all NSS methods:

    cumulus@switch:~$ sudo getent passwd cumulusTAC
    cumulusTAC:x:1016:1001:TACACS+ mapped user at privilege level 15,,,:/home/tacacs15:/bin/bash

To look up the user within the local database only:

    cumulus@switch:~$ sudo getent -s compat passwd cumulus
    cumulus:x:1000:1000:cumulus,,,:/home/cumulus:/bin/bash

To look up the user within the TACACS+ database only:

    cumulus@switch:~$ sudo getent -s tacplus passwd cumulusTAC
    cumulusTAC:x:1016:1001:TACACS+ mapped user at privilege level 15,,,:/home/tacacs15:/bin/bash

If TACACS does not appear to be working correctly, the following
configuration files should be debugged by adding the *debug=1* parameter
to one or more of these files:

  - /etc/tacplus\_servers

  - /etc/tacplus\_nss.conf

{{%notice note%}}

*debug=1* can also be added to individual `pam_tacplus` lines in
`/etc/pam.d/common*`.

{{%/notice%}}

All log messages are stored in `/var/log/syslog`.

#### <span>Incorrect Shared Key</span>

The TACACS client on the switch and the TACACS server should have the
same shared secret key. If this key is incorrect, the following messages
is printed to `syslog`:

    2017-09-05T19:57:00.356520+00:00 leaf01 sshd[3176]: nss_tacplus: TACACS+ server 192.168.0.254:49 read failed with protocol error (incorrect shared secret?) user cumulus 

### <span>Debugging Issues with Per-command Authorization</span>

To debug TACACS user command authorization, have the TACACS+ user enter
the following command at a shell prompt, and then try the command again:

    tacuser0@switch:~$ export TACACSAUTHDEBUG=1 

When this debugging is enabled, additional information is shown for the
command authorization conversation with the TACACS+ server:

    tacuser0@switch:~$ net pending
    tacplus-auth: found matching command (/usr/bin/net) request authorization
    tacplus-auth: error connecting to 10.0.3.195:49 to request authorization for net: Transport endpoint is not connected
    tacplus-auth: cmd not authorized (16)
    tacplus-auth: net not authorized from 192.168.3.189:49
    net not authorized by TACACS+ with given arguments, not executing
     
    tacuser0@switch:~$ net show version
    tacplus-auth: found matching command (/usr/bin/net) request authorization
    tacplus-auth: error connecting to 10.0.3.195:49 to request authorization for net: Transport endpoint is not connected
    tacplus-auth: 192.168.3.189:49 authorized command net
    tacplus-auth: net authorized, executing
    DISTRIB_ID="Cumulus Linux"
    DISTRIB_RELEASE=3.4.0
    DISTRIB_DESCRIPTION="Cumulus Linux 3.4.0"

To disable debugging:

    tacuser0@switch:~$ export -n TACACSAUTHDEBUG

### <span>Debug Issues with Accounting Records</span>

If TACACS+ servers have been added or deleted from the configuration
files, make sure you notify the audisp plugin with this command:

    cumulus@switch:~$ sudo killall -HUP audisp-tacplus

If accounting records still are not being sent, add *debug=1* to the
file `/etc/audisp/audisp-tac_plus.conf`, and then issue the command
above to notify the plugin. Then have the TACACS+ user run a command,
and examine the end of `/var/log/syslog` for messages from the plugin.
You can also check the auditing log file `/var/log/audit/audit.log` to
be sure the auditing records are being written. If they are not, restart
the audit daemon with:

    cumulus@switch:~$ sudo systemctl restart auditd.service

### <span>TACACS Component Software Descriptions</span>

These different pieces of software are involved with delivering TACACS.
Provided below is a brief description of their functionalities.

| Package Name                    | Description                                                                                                                                                                                                                                                                                                                                                                      |
| ------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| audisp-tacplus\_1.0.0-1-cl3u3   | This package uses auditing data from `auditd` to send accounting records to the TACACS+ server and is started as part of `auditd`.                                                                                                                                                                                                                                               |
| libtac2\_1.4.0-cl3u2            | Basic TACACS+ server utility and communications routines.                                                                                                                                                                                                                                                                                                                        |
| libnss-tacplus\_1.0.1-cl3u3     | Provides an interface between `libc` username lookups, the mapping functions, and the TACACS+ server.                                                                                                                                                                                                                                                                            |
| tacplus-auth-1.0.0-cl3u1        | This package provides the ability to do per-command TACACS+ authorization, and a setup utility tacplus-restrict to enable that. Per-command authorization is not done by default.                                                                                                                                                                                                |
| libpam-tacplus\_1.4.0-1-cl3u2   | A modified version of the standard Debian package.                                                                                                                                                                                                                                                                                                                               |
| libtacplus-map1\_1.0.0-cl3u2    | The mapping functionality between local and TACACS+ users on the server. Sets the immutable `sessionid` and auditing UID to ensure the original user can be tracked through multiple processes and privilege changes. Sets the auditing `loginuid` as immutable if supported. Creates and maintains a status database in `/run/tacacs_client_map` to manage and lookup mappings. |
| libsimple-tacacct1\_1.0.0-cl3u2 | Provides an interface for programs to send accounting records to the TACACS+ server. Used by `audisp-tacplus`.                                                                                                                                                                                                                                                                   |
| libtac2-bin\_1.4.0-cl3u2        | Provides the “tacc” testing program and TACACS+ man page.                                                                                                                                                                                                                                                                                                                        |

## <span>Limitations</span>

### <span>TACACS+ Client Is only Supported through the Management Interface</span>

The TACACS+ client is only supported through the switch's management
interface, which could be eth0 or eth1, or even the VRF management
interface. The TACACS+ client is not supported through bonds, switch
virtual interfaces (SVIs) or switch port interfaces (swp).

### <span>Multiple TACACS+ Users</span>

If two or more TACACS+ users are logged in simultaneously, with the same
privilege level, while the accounting records are maintained correctly,
a lookup on either name will match both users, while a UID lookup will
only return the user that logged in first.

This means that any processes run by either user will be attributed to
both, and all files created by either user will be attributed to the
first name matched. This is similar to adding two local users to the
password file with the same UID and GID, and is an inherent limitation
of using the UID for the base user from the password file.

{{%notice note%}}

The current algorithm returns the first name matching the UID from the
mapping file; this could be the first or second user that logged in.

{{%/notice%}}

To work around this issue, the switch’s audit log or the TACACS server
accounting logs can be used to determine which processes and files were
created by each user.

  - For commands that do not execute other commands (for example,
    changes to configurations in an editor, or actions with tools like
    `clagctl` and `vtysh`), no additional accounting is done.

  - Per-command authorization is not implemented in this release except
    at the most basic level (commands are permitted or denied based on
    the standard Linux user permissions for the local TACACS users, and
    only privilege level 15 users can run `sudo` commands by default).

The Linux `auditd` system does not always generate audit events for
processes when terminated with a signal (via the `kill` system call or
internal errors such as SIGSEGV). As a result, processes that exit on a
signal that isn’t caught and handled may not generate a STOP accounting
record.

### <span>Issues with deluser Command</span>

TACACS+ and other non-local users that run the `deluser` command with
the `--remove-home` option will see an error about not finding the user
in `/etc/passwd`:

    tacuser0@switch: deluser --remove-home USERNAME
    userdel: cannot remove entry ‘USERNAME’ from /etc/passwd
    /usr/sbin/deluser: `/usr/sbin/userdel USERNAME' returned error code 1. Exiting

However, the command does remove the home directory. The user can still
log in on that account, but will not have a valid home directory. This
is a known upstream issue with the `deluser` command for all non-local
users.

The `--remove-home` option should only be used when the `user_homedir=1`
configuration command is in use.
