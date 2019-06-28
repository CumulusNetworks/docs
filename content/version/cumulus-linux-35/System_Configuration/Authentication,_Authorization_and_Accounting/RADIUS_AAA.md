---
title: RADIUS AAA
author: Cumulus Networks
weight: 277
aliases:
 - /display/CL35/RADIUS+AAA
 - /pages/viewpage.action?pageId=8357341
pageID: 8357341
product: Cumulus Linux
version: '3.5'
imgData: cumulus-linux-35
siteSlug: cumulus-linux-35
---
Cumulus Networks offers add-on packages that provide the ability for
[RADIUS](https://en.wikipedia.org/wiki/RADIUS) users to log in to
Cumulus Linux switches in a transparent way with minimal configuration.
There is no need to create accounts or directories on the switch.
Authentication is handled via PAM, and includes login, `ssh`, `sudo` and
`su`.

## <span>Installing and Configuring the RADIUS Packages</span>

The plugin is installed from two RADIUS packages, which are not in the
base Cumulus Linux image. There is no RADIUS metapackage.

To install the plugins, run these commands:

    cumulus@switch:~$ sudo apt-get update
    cumulus@switch:~$ sudo apt-get install libnss-mapuser libpam-radius-auth

To remove the plugins, [see below](#src-8357341_RADIUSAAA-remove).

During installation, the PAM configuration is modified automatically via
`pam-auth-update (8)`, and the NSS configuration file
`/etc/nsswitch.conf` is modified to add the *mapuser* and *mapuid*
plugins. If you remove or purge the packages, these files are modified
to remove the configuration for these plugins.

## <span>Configuring the RADIUS Client</span>

For common use cases, the only configuration file that needs to be
modified is `/etc/pam_radius_auth.conf`. You need to add the hostname or
IP address of at least one RADIUS server (such as a
[*freeradius*](http://freeradius.org) server on Linux), and the shared
secret used to authenticate and encrypt communication with the server.
If you specify multiple server configuration lines, they are verified in
the order listed. Other than memory, there is no limit to the number of
RADIUS servers that may be on a given switch. These fields are described
in the `pam_radius_auth (5)` man page and in comments in the
`/etc/pam_radius_auth.conf` file.

Consider the following example configuration in the
`/etc/pam_radius_auth.conf` file:

    # server[:port]     shared_secret       timeout (secs)      src_ip
    aaa-testing         radius321
    192.168.0.254       secretkey

The server port number or name is optional. The system looks up the port
in the `/etc/services` file. However, you can override the ports in the
`/etc/pam_radius_auth.conf` file.

The `timeout` defaults to 3 seconds; you only need to change this
setting if the server is slow or latencies are high.

The `src_ip` option only needs to be specified if you want to use a
specific interface to reach the server. It can be set to the hostname of
the interface, or an IPv4 or IPv6 address. If specified, the `timeout`
option must also be specified.

The other field that you may need to set is the `vrf-name` field. This
is normally set to *mgmt* if you are using a [management
VRF](/version/cumulus-linux-35/Layer_3/Management_VRF). If you are
specifying the `src_ip` field for a server entry, and that interface is
in a VRF, you may also need to set it. At this time, you cannot specify
more than one VRF. The example below shows the vrf setting in the
`/etc/pam_radius_auth.conf` file.

    # server[:port]     shared_secret       timeout (secs)      src_ip         vrf
    192.168.0.254       secretkey
    other-server        othersecret         3                   192.168.1.10   vrf-blue

When first configuring the RADIUS client, it is a good idea to enable
debugging. This can be done by uncommenting the `debug` line in the
configuration file. Debugging messages are written to `syslog`.

There are a number of PAM configuration keywords that you can set, but
these do not normally need to be configured. See the `pam_radius_auth
(8)` man page for the variables that can be used. You can add these
either by editing:

  - The `/etc/pam.d/common-auth` lines for ` pam_radius_auth.so  `.

  - The `/usr/share/pam-configs/radius` file, then running
    `pam-auth-update --package`.

The latter method is recommended, because it is less likely to introduce
errors.

The `libpam-radius-auth` package supplied with the Cumulus Linux RADIUS
client is a newer version than the one in [Debian
Jessie](https://packages.debian.org/jessie/libpam-radius-auth), and has
added support for IPv6, the `src_ip` field described above, as well as a
number of bug fixes and minor features. Cumulus Linux further added VRF
support, man pages describing the PAM and RADIUS configuration, and the
setting of the `SUDO_PROMPT` environment variable to the login name as
part of the mapping support described below.

## <span>Configuring NCLU for RADIUS Users</span>

[NCLU](/version/cumulus-linux-35/System_Configuration/Network_Command_Line_Utility_-_NCLU/)
has its own configuration file to enable RADIUS users to run the `net`
command. Edit the `/etc/netd.conf` file, then:

  - To give a RADIUS user access to the show commands, add that user to
    the `users_with_show` line, then add the *radius\_users* group to
    the `groups_with_show` line.

  - To give a RADIUS user access to the edit commands (for all the NCLU
    write commands and to restart services with NCLU), add that user to
    the `users_with_edit` line.

<!-- end list -->

    cumulus@switch:~$ sudo nano /etc/netd.conf
     
    ...
     
    # Control which users/groups are allowed to run 'add', 'del',
    # 'clear', 'net abort', 'net commit' and restart services (quagga, etc)
    # to apply those changes
    users_with_edit = root, cumulus, rad_user
    groups_with_edit = netedit
     
    # Control which users/groups are allowed to run 'show' commands
    users_with_show = root, cumulus, rad_user
    groups_with_show = netshow, radius_users
     
    ...

{{%notice warning%}}

Do not add the *radius\_users* group to the `groups_with_edit` line, as
this is dangerous and can potentially enable any user to log into the
switch as the root user.

{{%/notice%}}

If the user/command combination is not authorized by the RADIUS server,
a message similar to the following gets displayed:

    rad_user@switch:~$ net show version
    net not authorized by TACACS+ with given arguments, not executing

### <span>Enabling Login without Local Accounts</span>

The above description of the PAM interfaces is similar to the normal
Debian `libpam-radius-auth` package, which work without the
`libnss-mapuser` package, if local or LDAP accounts are available for
each desired RADIUS user. Since LDAP is not commonly used with switches,
and adding accounts locally is cumbersome, Cumulus Linux added a mapping
capability. This is enabled by the `libnss-mapuser` package, which is
specific to Cumulus Linux.

Mapping is done via two NSS (Name Service Switch) plugins, one for
account name lookup, and one for UID lookup. These are automatically
configured in `/etc/nsswitch.conf` at installation, and are removed when
the package is removed. See the `nss_mapuser (8)` man page for the full
description of this plugin.

Mapping is done on username at login to a fixed account specified in the
configuration file, with the fields of the fixed account used as a
template for the user that is logging in.

For example, if the name being looked up is *dave* and the fixed account
in the configuration file is *radius\_user*, and that entry in
`/etc/passwd` is:

    radius_user:x:1017:1002:radius user:/home/radius_user:/bin/bash

then the matching line returned by running `getent passwd dave` would
be:

    cumulus@switch:~$ getent passwd dave
    dave:x:1017:1002:dave mapped user:/home/dave:/bin/bash

and the home directory `/home/dave` would be created during the login
process if it does not already exist, and will be populated with the
standard skeleton files by the `mkhomedir_helper` command.

The configuration file `/etc/nss_mapuser.conf` is used to configure the
plugins. It does not normally need to be changed. The `nss_mapuser (5)`
man page fully describes the configuration file. Comments in the file
also describe the fields.

A flat file mapping is done based on the session number assigned during
login, and it persists across `su` and `sudo`. The mapping is removed at
logout.

## <span>Enabling sudo Access for RADIUS Users</span>

To allow RADIUS users to use `sudo`, you need to create a `sudoers` file
authorizing them. The simplest case is to give them full `sudo` access,
similar to the *cumulus* user account. To do this, edit or create the
`/etc/sudoers.d/radius` file, and add the users to the file with an
entry like this:

    cumulus@switch:~$ sudo vi /etc/sudoers.d/radius
    dave ALL=(ALL:ALL) ALL

where *dave* is the login account name of a RADIUS user. If you want all
RADIUS users to have this ability, you can enable `sudo` access for all
members of the *radius\_users* group:

    cumulus@switch:~$ sudo vi /etc/sudoers.d/radius
    %radius_users ALL=(ALL:ALL) ALL

## <span id="src-8357341_RADIUSAAA-remove" class="confluence-anchor-link"></span><span>Removing the RADIUS Client Packages</span>

You can remove the RADIUS packages with the following command:

    cumulus@switch:~$ sudo apt-get remove libnss-mapuser libpam-radius-auth

When the packages are removed, the plugins are removed from the
`/etc/nsswitch.conf` file and from the PAM files, respectively.

To remove all configuration files for these packages, run:

    cumulus@switch:~$ sudo apt-get purge libnss-mapuser libpam-radius-auth

{{%notice note%}}

The RADIUS fixed account is not removed from `/etc/passwd` or
`/etc/group`, and the home directories are not removed either. They are
left in case there are modifications to the account or files in the home
directories.

{{%/notice%}}

To remove the home directories of the RADIUS users, first get the list
by running:

    cumulus@switch:~$ sudo ls -l /home | grep radius

For all users listed other than the *radius\_user*, run this command to
remove the home directories:

    cumulus@switch:~$ sudo deluser --remove-home USERNAME

where USERNAME is the account name (the home directory relative
portion). This command gives the following warning:

    userdel: cannot remove entry 'USERNAME' from /etc/passwd
    /usr/sbin/deluser: `/usr/sbin/userdel USERNAME' returned error code 1. Exiting.

Because the user is not listed in the `/etc/passwd` file. After removing
all the RADIUS users, run the command to remove the fixed account (the
account may have been changed in `/etc/nss_mapuser.conf`; if so, use
that account name instead of *radius\_user*).

    cumulus@switch:~$ sudo deluser --remove-home radius_user
    cumulus@switch:~$ sudo delgroup radius_users

## <span>Limitations</span>

### <span>Multiple RADIUS Users</span>

If two or more RADIUS users are logged in simultaneously, a UID lookup
only returns the user that logged in first. This means that any
processes run by either user get attributed to both, and all files
created by either user get attributed to the first name matched. This is
similar to adding two local users to the password file with the same UID
and GID, and is an inherent limitation of using the UID for the fixed
user from the password file.

The current algorithm returns the first name matching the UID from the
mapping file; this could be the first or second user that logged in.

## <span>Related Information</span>

  - [TACACS+
    client](/version/cumulus-linux-35/System_Configuration/Authentication_Authorization_and_Accounting/TACACS_Plus)

  - [Cumulus Networks RADIUS demo on
    GitHub](https://github.com/CumulusNetworks/cldemo-radius)

  - [Cumulus Network TACACS demo on
    GitHub](https://github.com/CumulusNetworks/cldemo-tacacs)
