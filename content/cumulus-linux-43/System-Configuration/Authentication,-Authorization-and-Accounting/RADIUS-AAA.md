---
title: RADIUS AAA
author: Cumulus Networks
weight: 190
toc: 4
---
Cumulus Networks offers add-on packages that enable {{<exlink url="https://en.wikipedia.org/wiki/RADIUS" text="RADIUS">}} users to log in to Cumulus Linux switches in a transparent way with minimal configuration. There is no need to create accounts or directories on the switch. Authentication is handled with PAM and includes login, `ssh`, `sudo` and `su`.

## Install the RADIUS Packages

You can install the RADIUS packages even if the switch is not connected to the internet, as they are contained in the `cumulus-local-apt-archive` repository that is {{<link url="Adding-and-Updating-Packages#add-packages-from-the-cumulus-linux-local-archive" text="embedded">}} in the Cumulus Linux image.

To install the RADIUS packages:

```
cumulus@switch:~$ sudo apt-get update
cumulus@switch:~$ sudo apt-get install libnss-mapuser libpam-radius-auth
```

After installation is complete, either reboot the switch or run the `sudo systemctl restart netd` command.

The `libpam-radius-auth` package supplied with the Cumulus Linux RADIUS client is a newer version than the one in {{<exlink url="https://packages.debian.org/buster/libpam-radius-auth" text="Debian Buster">}}. This package contains support for IPv6, the `src_ip` option described below, as well as a number of bug fixes and minor features. The package also includes VRF support, provides man pages describing the PAM and RADIUS configuration, and sets the `SUDO_PROMPT` environment variable to the login name for RADIUS mapping support.

The `libnss-mapuser` package is specific to Cumulus Linux and supports the `getgrent`, `getgrnam` and `getgrgid` library interfaces. These interfaces add logged in RADIUS users to the group member list for groups that contain the `mapped_user` (`radius_user`) if the RADIUS account is unprivileged, and add privileged RADIUS users to the group member list for groups that contain the `mapped_priv_user` (`radius_priv_user`) during the group lookups.

During package installation:

- The PAM configuration is modified automatically using `pam-auth-update (8)`, and the NSS configuration file `/etc/nsswitch.conf` is modified to add the *mapuser* and *mapuid* plugins. If you remove or purge the packages, these files are modified to remove the configuration for these plugins.
- The `radius_shell` package is added, which installs the `/sbin/radius_shell` and `setcap cap_setuid` program used as the login shell for RADIUS accounts. The package adjusts the `UID` when needed, then runs the bash shell with the same arguments. When installed, the package changes the shell of the RADIUS accounts to `/sbin//radius_shell`, and to `/bin/shell` if the package is removed. This package is required for privileged RADIUS users to be enabled. It is not required for regular RADIUS client use.
- The `radius_user` account is added to the `netshow` group and the `radius_priv_user` account to the `netedit` and `sudo` groups. This change enables all RADUS logins to run NCLU `net show` commands and all privileged RADIUS users to also run `net add`, `net del`, and `net commit` commands, and to use `sudo`.

## Configure the RADIUS Client

To configure the RADIUS client, edit the `/etc/pam_radius_auth.conf` file:

1. Add the hostname or IP address of at least one RADIUS server (such as a *{{<exlink url="http://freeradius.org/" text="freeradius">}}* server on Linux), and the shared secret used to authenticate and encrypt communication with each server.

    {{%notice tip%}}

The hostname of the switch must be resolvable to an IP address, which, in general, is fixed in DNS. If for some reason you cannot find the hostname in DNS, you can add the hostname to the `/etc/hosts` file manually. However, this can cause problems since the IP address is usually assigned by DHCP, which can change at any time.

{{%/notice%}}

    Multiple server configuration lines are verified in the order listed. Other than memory, there is no limit to the number of RADIUS servers you can use.
    
    The server port number or name is optional. The system looks up the port in the `/etc/services` file. However, you can override the ports in the `/etc/pam_radius_auth.conf` file.

2. If the server is slow or latencies are high, change the `timeout` setting. The setting defaults to 3 seconds.
3. If you want to use a specific interface to reach the RADIUS server, specify the `src_ip` option. You can specify the hostname of the interface, an IPv4, or an IPv6 address. If you specify the `src_ip` option, you must also specify the `timeout` option.
4. Set the `vrf-name` field. This is typically set to *mgmt* if you are using a {{<link url="Management-VRF" text="management VRF">}}. You cannot specify more than one VRF.

The configuration file includes the `mapped_priv_user` field that sets the account used for privileged RADIUS users and the `priv-lvl` field that sets the minimum value for the privilege level to be considered a privileged login (the default value is 15). If you edit these fields, make sure the values match those set in the `/etc/nss_mapuser.conf` file.

The following example provides a sample `/etc/pam_radius_auth.conf` file configuration:

```
mapped_priv_user   radius_priv_user
# server[:port]    shared_secret   timeout (secs)  src_ip
192.168.0.254      secretkey
other-server       othersecret     3               192.168.1.10
# when mgmt vrf is in use
vrf-name mgmt
```

{{%notice tip%}}

If this is the first time you are configuring the RADIUS client, uncomment the `debug` line to help with troubleshooting. The debugging messages are written to `/var/log/syslog`. When the RADIUS client is working correctly, comment out the `debug` line.

{{%/notice%}}

As an optional step, you can set PAM configuration keywords by editing the `/usr/share/pam-configs/radius` file. After you edit the file, you must run the `pam-auth-update --package` command. PAM configuration keywords are described in the `pam_radius_auth (8)` man page.

{{%notice note%}}

The privilege level for the user on the switch is determined by the value of the VSA (Vendor Specific Attribute)  `shell:priv-lvl`. If the attribute is not returned, the user is unprivileged. The following shows an example using the freeradius server for a fully-privileged user.

```
Service-Type = Administrative-User,
Cisco-AVPair = "shell:roles=network-administrator",
Cisco-AVPair += "shell:priv-lvl=15"
```

The VSA vendor name (Cisco-AVPair in the example above) can have any content. The RADIUS client only checks for the string `shell:priv-lvl`.

{{%/notice%}}

## Enable Login without Local Accounts

Because LDAP is not commonly used with switches and adding accounts locally is cumbersome, Cumulus Linux includes a mapping capability with the `libnss-mapuser` package.

Mapping is done using two NSS (Name Service Switch) plugins, one for account name, and one for UID lookup. These accounts are configured automatically in `/etc/nsswitch.conf` during installation and are removed when the package is removed. See the `nss_mapuser (8)` man page for the full description of this plugin.

A username is mapped at login to a fixed account specified in the configuration file, with the fields of the fixed account used as a template for the user that is logging in.

For example, if the name being looked up is *dave* and the fixed account in the configuration file is *radius\_user*, and that entry in `/etc/passwd` is:

```
radius_user:x:1017:1002:radius user:/home/radius_user:/bin/bash
```

then the matching line returned by running `getent passwd dave` is:

```
cumulus@switch:~$ getent passwd dave
dave:x:1017:1002:dave mapped user:/home/dave:/bin/bash
```

The home directory `/home/dave` is created during the login process if it does not already exist and is populated with the standard skeleton files by the `mkhomedir_helper` command.

The configuration file `/etc/nss_mapuser.conf` is used to configure the plugins. The file includes the mapped account name, which is `radius_user` by default. You can change the mapped account name by editing the file. The `nss_mapuser (5)` man page describes the configuration file.

A flat file mapping is done based on the session number assigned during login, which persists across `su` and `sudo`. The mapping is removed at logout.

## Local Fallback Authentication

If a site wants to allow local fallback authentication for a user when none of the RADIUS servers can be reached you can add a privileged user account as a local account on the switch. The local account must have the same unique identifier as the privileged user and the shell must be the same.

To configure local fallback authentication:

1. Add a local privileged user account. For example, if the `radius_priv_user` account in the `/etc/passwd` file is `radius_priv_user:x:1002:1001::/home/radius_priv_user:/sbin/radius_shell`, run the following command to add a local privileged user account named johnadmin:

    ```
    cumulus@switch:~$ sudo useradd -u 1002 -g 1001 -o -s /sbin/radius_shell johnadmin
    ```

2. To enable the local privileged user to run `sudo` and NCLU commands, run the following commands:

    ```
    cumulus@switch:~$ sudo adduser johnadmin netedit
    cumulus@switch:~$ sudo adduser johnadmin sudo
    cumulus@switch:~$ sudo systemctl restart netd
    ```

3. Edit the `/etc/passwd` file to move the local user line before to the `radius_priv_user` line:

    ```
    cumulus@switch:~$ sudo vi /etc/passwd
    ...
    johnadmin:x:1002:1001::/home/johnadmin:/sbin/radius_shell
    radius_priv_user:x:1002:1001::/home/radius_priv_user:/sbin/radius_shell
    ```

4. To set the local password for the local user, run the following command:

    ```
    cumulus@switch:~$ sudo passwd johnadmin
    ```

## Verify RADIUS Client Configuration

To verify that the RADIUS client is configured correctly, log in as a non-privileged user and run a `net add interface` command.

In this example, the `ops` user is not a privileged RADIUS user so they cannot add an interface.

```
ops@leaf01:~$ net add interface swp1
ERROR: User ops does not have permission to make networking changes.
```

In this example, the `admin` user is a privileged RADIUS user (with privilege level 15) so is able to add interface swp1.

```
admin@leaf01:~$ net add interface swp1
admin@leaf01:~$ net pending
--- /etc/network/interfaces    2018-04-06 14:49:33.099331830 +0000
+++ /var/run/nclu/iface/interfaces.tmp    2018-04-06 16:01:16.057639999 +0000
@@ -3,10 +3,13 @@

  source /etc/network/interfaces.d/*.intf

  # The loopback network interface
  auto lo
  iface lo inet loopback

  # The primary network interface
  auto eth0
  iface eth0 inet dhcp
+
+auto swp1
iface swp1
...
```

## Remove RADIUS Client Packages

Remove the RADIUS packages with the following command:

```
cumulus@switch:~$ sudo apt-get remove libnss-mapuser libpam-radius-auth
```

When you remove the packages, the plugins are removed from the `/etc/nsswitch.conf` file and from the PAM files.

To remove all configuration files for these packages, run:

```
cumulus@switch:~$ sudo apt-get purge libnss-mapuser libpam-radius-auth
```

{{%notice note%}}

The RADIUS fixed account is not removed from the `/etc/passwd` or `/etc/group` file and the home directories are not removed. They remain in case there are modifications to the account or files in the home directories.

{{%/notice%}}

To remove the home directories of the RADIUS users, first get the list by running:

```
cumulus@switch:~$ sudo ls -l /home | grep radius
```

For all users listed, except the *radius\_user*, run this command to remove the home directories:

```
cumulus@switch:~$ sudo deluser --remove-home USERNAME
```

where USERNAME is the account name (the home directory relative portion). This command gives the following warning because the user is not listed in the `/etc/passwd` file.

```
userdel: cannot remove entry 'USERNAME' from /etc/passwd
/usr/sbin/deluser: `/usr/sbin/userdel USERNAME' returned error code 1. Exiting.
```

After removing all the RADIUS users, run the command to remove the fixed account. If the account has been changed in the `/etc/nss_mapuser.conf` file, use that account name instead of *radius\_user*.

```
cumulus@switch:~$ sudo deluser --remove-home radius_user
cumulus@switch:~$ sudo deluser --remove-home radius_priv_user
cumulus@switch:~$ sudo delgroup radius_users
```

## Considerations

- If two or more RADIUS users are logged in simultaneously, a UID lookup only returns the user that logged in first. Any processes run by either user get attributed to both, and all files created by either user get attributed to the first name matched. This is similar to adding two local users to the password file with the same UID and GID, and is an inherent limitation of using the UID for the fixed user from the password file. The current algorithm returns the first name matching the UID from the mapping file; this might be the first or second user that logged in.
- When you have both the TACACS+ and the RADIUS AAA client installed, RADIUS login is not attempted. As a workaround, do not install both the TACACS+ and the RADIUS AAA client on the same switch.

## Related Information

- {{<link url="TACACS+" text="TACACS+ client">}}
- {{<exlink url="https://github.com/CumulusNetworks/cldemo-radius" text="Cumulus Networks RADIUS demo on GitHub">}}
- {{<exlink url="https://github.com/CumulusNetworks/cldemo-tacacs" text="Cumulus Network TACACS demo on GitHub">}}
