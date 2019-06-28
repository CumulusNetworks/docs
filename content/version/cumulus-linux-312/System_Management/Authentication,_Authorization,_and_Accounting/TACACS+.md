---
title: TACACS+
author: Cumulus Networks
weight: 235
aliases:
 - /display/CL31/TACACS+
 - /pages/viewpage.action?pageId=5121931
pageID: 5121931
product: Cumulus Linux
version: 3.1.2
imgData: cumulus-linux-312
siteSlug: cumulus-linux-312
---
{{%notice warning%}}

**Early Access Feature**

TACACS+ is an [early access
feature](https://support.cumulusnetworks.com/hc/en-us/articles/202933878)
in Cumulus Linux 3.1. Before you can install TACACS+, you must enable
the Early Access repository. For more information about the Cumulus
Linux repository, read [this knowledge base
article](https://support.cumulusnetworks.com/hc/en-us/articles/217422127).

{{%/notice%}}

Cumulus Linux 3.1 has implemented TACACS+ client authentication
(including login, su, sudo, and ssh) and command accounting. These
package enable TACACS+ users in a transparent manner, similar to LDAP or
local accounts.

Command accounting occurs in addition to session accounting, at the
start and stop of the server, via the exec() system call family.

By default, TACACS+ privilege 15 users are allowed to run any command
with sudo via the /etc/sudoers.d/tacplus file that is installed by the
libtacplus-map1 package.

{{%notice note%}}

All sudo commands generate accounting records against the original
login.

{{%/notice%}}

{{%notice note%}}

TACACS+ users at privilege levels other than 15 are not allowed to run
sudo commands by default, and are limited to commands that can be run
with standard Linux user permissions.

{{%/notice%}}

{{%notice note%}}

Cumulus Linux 3.x provides a new library to map TACACS+ users by their
privilege level to the tacacs\* users in the local password file, and
from those local users to the TACACS+ users. These users are created
with the `adduser` command after the `libtacplus-map1` package is
installed.

{{%/notice%}}

## <span>Package Dependencies</span>

TACACS+ requires the following packages to be installed on Cumulus
Linux:

| Package Name                           | Description                                                                                                                                                                                                                                                                                                                                                                      |
| -------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| audisp-tacplus\_1.0.0-1\_amd64.deb     | This package uses auditing data from `auditd` to send accounting records to the TACACS+ server.                                                                                                                                                                                                                                                                                  |
| libtac2\_1.3.9-1\_amd64.deb            | Basic TACACS+ server utility and communications routines.                                                                                                                                                                                                                                                                                                                        |
| libnss-tacplus\_1.0.1-1\_amd64.deb     | Provides an interface between `libc` username lookups, the mapping functions, and the TACACS+ server.                                                                                                                                                                                                                                                                            |
| libtac2-bin\_1.3.9-1\_amd64.deb        | Provides the “tacc” testing program and TACACS+ man page.                                                                                                                                                                                                                                                                                                                        |
| libpam-tacplus\_1.4.0-1\_amd64.deb     | A modified version of the standard Debian package.                                                                                                                                                                                                                                                                                                                               |
| libtacplus-map1\_1.0.0-1\_amd64.deb    | The mapping functionality between local and TACACS+ users on the server. Sets the immutable `sessionid` and auditing UID to ensure the original user can be tracked through multiple processes and privilege changes. Sets the auditing `loginuid` as immutable if supported. Creates and maintains a status database in `/run/tacacs_client_map` to manage and lookup mappings. |
| libsimple-tacacct1\_1.0.0-1\_amd64.deb | Provides an interface for programs to send accounting records to the TACACS+ server. Used by `audisp-tacplus`.                                                                                                                                                                                                                                                                   |
| sudo\_1.8.10p3-cl3u1\_amd64.deb        | A modified version of the standard Debian package, adding TACACS+ authenticated user/password lookup functionality. This package is installed by default.                                                                                                                                                                                                                        |

## <span>Installing and Removing the TACACS+ Client Packages</span>

To install the `tacplus-client` package, on a switch, follow the
instructions in the [Cumulus Linux 3.1 release
notes](https://support.cumulusnetworks.com/hc/en-us/articles/224473608#ea).

To remove all of the TACACS+ client packages, use the following
commands:

    cumulus@switch:~$ sudo apt-get remove tacplus-client
    cumulus@switch:~$ sudo apt-get autoremove

To remove the TACACS+ client configuration files as well as the packages
(recommended), use this command:

    cumulus@switch:~$ sudo apt-get autoremove --purge

## <span>TACACS+ Authentication</span>

The initial authentication configuration is done through the PAM
modules, and an updated version of the `libpam-tacplus` package. When
the package is installed, the PAM configuration is updated in
`/etc/pam.d` with the `pam-auth-update` command.

## <span>NSS Plugin</span>

When used with `pam_tacplus`, TACACS+ authenticated users can log in
without a local account on the system by using the NSS plugin that comes
with the `tacpluss_nss` package. The plugin uses the mapped `tacplus`
information if the user is not found in the local password file,
provides the `getpwnam()` entry point, and uses the TACACS+
authentication and accounting functions.

The plugin asks the TACACS+ server if the user is known, and then for
relevant attributes to determine the user’s privilege level. When the
`libnss_tacplus` package is installed, `nsswitch.conf` can be modified
to set `tacplus` as the first lookup method for `passwd`, though it
works in any position.

If the user is not found, a mapped lookup is performed using the
` libtacplus_map.so  `exported functions. The privilege level is
appended to “tacacs”, and the lookup searches for the name in the local
password file. For example, privilege level 15 will search for the
tacacs15 user. If the user is found, the password structure is filled in
with the user’s information.

If it is not found, the privilege level is decremented and checked
again, until tacacs0 is reached.

{{%notice note%}}

The `pw_name` attribute is not filled in with the user information;
rather, with the original login name.

{{%/notice%}}

{{%notice note%}}

This allows for a configuration setup containing only two tacacs users:
tacacs0 and tacacs15.

{{%/notice%}}

## <span>TACACS+ Accounting</span>

TACACS+ accounting is implemented with the `audisp` module, with an
additional plugin for auditd/audisp. The plugin maps the auid in the
accounting record to a tacacs login, based on the auid and sessionid.
The audisp module requires `libnss_tacplus`, and uses the
`libtacplus_map.so` library interfaces as part of the modified
`lipam_tacplus` package.

Communication with the TACACS+ servers is done via the
`libsimple-tacact1` library, via `dlopen()`. A maximum of 240 bytes of
command name and arguments will be sent in the accounting record, due to
the TACACS+ field length limitation of 255 bytes.

The IP address and encryption key of the server should be configured in
the `/etc/tacplus_servers` file. Minimal configuration to auditd and
audisp is necessary to enable the audit records necessary for
accounting. These records are installed as part of the package.

Audisp-tacplus installs the audit rules for command accounting.
Modifying the configuration files is not usually necessary.

Below are the configuration files for `auditd`/`audisp`:

| Filename                                  | Description                                                                    |
| ----------------------------------------- | ------------------------------------------------------------------------------ |
| /etc/audisp/plugins.d/audisp-tacplus.conf | `audisp` plugin configuration file. In general, no modifications are required. |
| /etc/audisp/audisp-tac\_plus.conf         | TACACS+ server configuration file. In general, no modifications are required.  |
| /etc/audit/rules.d/audisp-tacplus.rules   | The `auditd` rules file.                                                       |
| /etc/audit/audit.rules                    | Audit rules file generated during `auditd` installation.                       |

{{%notice note%}}

Filenames can be altered in the `/etc/audisp/audisp-tacplus.conf` file.

{{%/notice%}}

## <span>TACACS+ Configuration</span>

Post-installation TACACS+ configuration is done in the following
configuration files:

| Filename                       | Description                                                                                                                                                         |
| ------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| /etc/tacplus\_servers          | This is the primary file that requires configuration post-installation.                                                                                             |
| /etc/nsswitch.conf             | When the `libnss_tacplus` package is installed, this file is configured to enable tacplus lookups via `libnss_tacplus`.                                             |
| /etc/tacplus\_nss.conf         | This file sets the basic parameters for `libnss_tacplus`. It includes a debug variable for debugging NSS lookups.                                                   |
| /usr/share/pam-configs/tacplus | Configuration file for `pam-auth-update`.                                                                                                                           |
| /etc/pam.d/common-\*           | Most of the `/etc/pam.d/common-*` files are updated for `tacplus` authentication. The files are updated with `pam-auth-update`, when `libpam-tacplus` is installed. |
| /etc/sudoers.d/tacplus         | This file allows TACACS+ privilege level 15 users to run commands with `sudo`.                                                                                      |

The minimum required configuration involves setting the IP address of
the TACACS+ server and the shared encryption key, in the
`/etc/tacplus_servers` file. The TACACS shared encryption key is an
ASCII phrase that is used to encrypt TACACS messages between the client
and TACACS server. Below is an example of the configuration file:

    cumulus@switch:~$ sudo cat /etc/tacplus_servers 
    # This is a common file used by audisp-tacplus, libpam_tacplus, and
    # libtacplus_map config files as shipped.
    #
    # Any tac_plus client config can go here that is common to all users of this
    # file, but typically it's just the TACACS+ server IP address(es) and shared
    # secret(s)
    #
    # This file should normally be mode 600, if you care about the security 
    # of your secret key.   When set to mode 600 NSS lookups for TACACS users
    # will only work for tacacs users that are logged in, via the local mapping.
    # For root, lookups will work for any tacacs users, logged in or not.
    secret=tacacskey
    server=192.168.0.30

Additional TACACS servers can be configured in /etc/`tacplus_nss.conf`:

    cumulus@switch:~$ cat /etc/tacplus_nss.conf
    #%NSS_TACPLUS-1.0
    # Install this file as /etc/tacplus_nss.conf
    # Edit /etc/nsswitch.conf to add tacplus to the passwd lookup, similar to this
    # where tacplus precede compat (or files), and depending on local policy can
    # follow or precede ldap, nis, etc.
    #    passwd: tacplus compat 
    # The server keyword should follow the secret keyword, and may be
    # given fewer times than the server keyword, if all servers have the same
    # shared secret.
    # is matched up with first secret line, etc.  You can use any of the
    # following orders, or most other orders you can think of.  There must be at
    # least as many secret lines as there are server lines.  This file should be
    # kept as permisions 644, owned by root, since it must be readable by arbitrary
    # processes, even though the secret for the TACACS+ server is present as clear
    # text.
    #  Servers are tried in the order listed, and once a server
    #  replies, no other servers are attempted in a given process instantiation
    # 
    #  This configuration is similar to the libpam_tacplus configuration, but
    #  is maintained as a configuration file, since nsswitch.conf doesn't
    #  support passing parameters.  Parameters must start in the first
    #  column, and parsing stops at the first whitespace
    # if set, errors and other issues are logged with syslog
    # debug=1
    # The include keyword allows centralizing the tacacs+ server information
    # including the IP address and shared secret
    include=/etc/tacplus_servers
    #  The server IP address can be optionally followed by a ':' and a port
    #  number (server=1.1.1.1:49).
    secret=SECRET1
    server=192.168.0.60
    secret=SECRET2
    server=192.168.0.90

Once the `tacplus_client` package is installed, the `tacplus` option is
added the ` passwd  `function in the `nsswitch` config. Below is the
default example:

    cumulus@switch:~$ cat /etc/nsswitch.conf
    # /etc/nsswitch.conf
    #
    # Example configuration of GNU Name Service Switch functionality.
    # If you have the `glibc-doc-reference' and `info' packages installed, try:
    # `info libc "Name Service Switch"' for information about this file.
    passwd:         tacplus compat
    group:          compat
    shadow:         compat
    gshadow:        files
    hosts:          files dns
    networks:       files
    protocols:      db files
    services:       db files
    ethers:         db files
    rpc:            db files
    netgroup:       nis

At this point, the Cumulus Linux switch should be able to query the
TACACS server.

{{%notice note%}}

The `/etc/tacplus_servers` file permissions should be set to mode 600 to
keep the shared key secure. When editing this file, auditing must be
restarted before accounting will see the changes. To restart `auditd`:

    cumulus@switch:~$ sudo systemctl restart auditd

{{%/notice%}}

{{%notice warning%}}

If you overwrite the `/etc/nsswitch.conf` file, `tacplus` must be added
to the `passwd` line, preceding `compat`.

{{%/notice%}}

{{%notice warning%}}

The `/etc/pam.d/common-*` files can be edited manually. However, if
`pam-auth-update` is run again after the changes are made, the update
will fail. Configuration should be done in
`/usr/share/pam-configs/tacplus` instead, followed by running
`pam-auth-update`.

{{%/notice%}}

The recognized configuration options are the same as the
`libpam_tacplus` command line arguments; not all `pam_tacplus` options
are supported, however. The table below describes the configuration
options available:

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Configuration Option</p></th>
<th><p>Management Group</p></th>
<th><p>Description</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>debug</p></td>
<td><p>ALL</p></td>
<td><p>Output debugging information via <code>syslog(3)</code>.</p>
<p>{{%notice note%}}</p>
<p>Debugging is heavy, including passwords.</p>
<p>{{%/notice%}}</p></td>
</tr>
<tr class="even">
<td><p>secret=STRING</p></td>
<td><p>ALL</p></td>
<td><p>Secret key used to encrypt/decrypt packets sent to/received from the server. Can be specified more than once.</p></td>
</tr>
<tr class="odd">
<td><p>server=HOSTNAME</p>
<p>server=IP_ADDR</p></td>
<td><p>auth, session</p></td>
<td><p>Adds a TACACS+ server to the servers list. Servers will be queried in turn until a match is found, or no servers remain in the list. Can be specified more than once.</p>
<p>{{%notice note%}}</p>
<p>When sending accounting records, the record is sent to all servers in the list.</p>
<p>{{%/notice%}}</p></td>
</tr>
<tr class="even">
<td><p>timeout=SECONDS</p></td>
<td><p> </p></td>
<td><p>TACACS+ server(s) communication timeout. The default value is 5 seconds.</p></td>
</tr>
<tr class="odd">
<td><p>login=STRING</p></td>
<td><p> </p></td>
<td><p>TACACS+ authentication service (pap, chap, or login). The default value is <em>pap</em>.</p></td>
</tr>
<tr class="even">
<td><p>acct_all=1</p></td>
<td><p> </p></td>
<td><p>Configuration option for <code>audisp_tacplus</code> and <code>pam_tacplus</code> sending accounting records to all supplied servers (1), or the first server to respond (0). The default value is <em>1</em>.</p></td>
</tr>
<tr class="odd">
<td><p>service</p></td>
<td><p> </p></td>
<td><p>TACACS+ accounting and authorization service. Examples include shell, pap, raccess, ppp, and slip.</p>
<p>The default value is <em>shell</em>.</p></td>
</tr>
<tr class="even">
<td><p>protocol</p></td>
<td><p> </p></td>
<td><p>TACACS+ protocol field. This option is use dependent.</p>
<p>PAM uses the SSH protocol.</p></td>
</tr>
</tbody>
</table>

For more information, refer to the `audisp.8` and `auditd.8` man pages.

## <span>Troubleshooting TACACS+</span>

The `getent` command can be used to determine whether TACACS+ is
configured correctly, and the local password is stored in the
configuration files. In the example commands below, the cumulus user
represents the local user, while cumulusTAC represents the TACACS user.

To look up the username within all NSS methods:

    cumulus@switch:~# getent password cumulusTAC
    cumulusTAC:x:1016:1001:TACACS+ mapped user at privilege level 15,,,:/home/tacacs15:/bin/bash

To look up the user within the local database only:

    cumulus@switch:~# getent -s compat passwd cumulus
    cumulus:x:1000:1000:cumulus,,,:/home/cumulus:/bin/bash

{{%notice note%}}

Running this command with the cumulusTAC user should return nothing.

{{%/notice%}}

To look up the user within the TACACS+ database only:

    cumulus@switch:~# getent -s tacplus passwd cumulusTAC
    cumulusTAC:x:1016:1001:TACACS+ mapped user at privilege level 15,,,:/home/tacacs15:/bin/bash

{{%notice note%}}

Running this command with the cumulus user should return nothing.

{{%/notice%}}

If TACACS does not appear to be working correctly, the following
configuration files should be debugged with *debug=1*:

  - /etc/tacplus\_servers

  - /etc/tacplus\_nss.conf

{{%notice note%}}

*debug=1* can also be added to individual `pam_tacplus` lines in
`/etc/pam.d/common*`.

{{%/notice%}}

All logs are stored in `/var/log/syslog`.

## <span>Limitations</span>

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

To workaround this issue, the switch’s audit log or the TACACS server
accounting logs can be used to determine which processes and files were
created by each user.

  - For commands that do not execute other commands (for example,
    changes to configurations in an editor, or actions with tools like
    `clagctl` and `vtysh`), no additional accounting is done.

  - Per-command authorization is not implemented in this release except
    at the most basic level (commands are permitted or denied based on
    the standard Linux user permissions for the local TACACS users, and
    only privilege level 15 users can run `sudo` commands by default).

The Linux `auditd` system does not generate audit events for processes
when terminated with a signal (via the `kill` system call or internal
errors such as SIGSEGV). As a result, processes that exit on a signal
that isn’t caught and handled may not generate a STOP accounting record.
