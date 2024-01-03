---
title: TACACS
author: NVIDIA
weight: 180
toc: 4
---
Cumulus Linux implements TACACS+ client AAA (Accounting, Authentication, and Authorization) in a transparent way with minimal configuration. The client implements the TACACS+ protocol as described in {{<exlink url="https://tools.ietf.org/html/draft-grant-tacacs-02" text="this IETF document">}}. There is no need to create accounts or directories on the switch. Accounting records are sent to all configured TACACS+ servers by default. Use of per-command authorization requires additional setup on the switch.

## Supported Features

- Authentication using PAM; includes `login`, `ssh`, `sudo` and `su`
- Runs over the eth0 management interface
- Ability to run in the {{<link url="Management-VRF" text="management VRF">}}
- TACACS+ privilege 15 users can run any command with sudo using the `/etc/sudoers.d/tacplus` file that is installed by the `libtacplus-map1` package
- Up to seven TACACS+ servers

## Install the TACACS+ Client Packages

You can install the TACACS+ packages even if the switch is not connected to the internet, as they are contained in the `cumulus-local-apt-archive` repository that is {{<link url="Adding-and-Updating-Packages#add-packages-from-the-cumulus-linux-local-archive" text="embedded">}} in the Cumulus Linux disk image.

To install all required packages, run these commands:

```
cumulus@switch:~$ sudo -E apt-get update
cumulus@switch:~$ sudo -E apt-get install tacplus-client
```

## Configure the TACACS+ Client

After installing TACACS+, edit the `/etc/tacplus_servers` file to add at least one server and one shared secret (key). You can specify the server and secret parameters in any order anywhere in the file. Whitespace (spaces or tabs) are not allowed. For example, if your TACACS+ server IP address is `192.168.0.30` and your shared secret is `tacacskey`, add these parameters to the `/etc/tacplus_servers` file:

```
secret=tacacskey
server=192.168.0.30
```

Cumulus Linux supports a maximum of seven TACACS+ servers. To specify multiple servers, add one per line to the `/etc/tacplus_servers` file.

Connections are made in the order in which they are listed in this file. In most cases, you do not need to change any other parameters. You can add parameters used by any of the packages to this file, which affects all the TACACS+ client software. For example, the timeout value for NSS lookups (see description below) is set to 5 seconds by default in the `/etc/tacplus_nss.conf` file, whereas the timeout value for other packages is 10 seconds and is set in the `/etc/tacplus_servers` file. The timeout value is per connection to the TACACS+ servers. (If authorization is configured per command, the timeout occurs for *each* command.) There are several (typically four) connections to the server per login attempt from PAM, as well as two or more through NSS. Therefore, with the default timeout values, a TACACS+ server that is not reachable can delay logins by a minute or more per unreachable server. If you must list unreachable TACACS+ servers, place them at the end of the server list and consider reducing the timeout values.

When you add or remove TACACS+ servers, you must restart `auditd` (with the `systemctl restart auditd` command) or you must send a signal (with `killall -HUP audisp-tacplus`) before `audisp-tacplus` rereads the configuration to see the changed server list.

You can also configure the IP address used as the source IP address when communicating with the TACACS+ server. See {{<link url="#tacacs-configuration-parameters" text="TACACS Configuration Parameters">}} below for the full list of TACACS+ parameters.

Following is the complete list of the TACACS+ client configuration files, and their use.

| <div style="width:250px">Filename | Description |
|----------|-------------|
| `/etc/tacplus_servers` | This is the primary file that requires configuration after installation. The file is used by all packages with `include=/etc/tacplus_servers` parameters in the other configuration files that are installed. Typically, this file contains the shared secrets; make sure that the Linux file mode is 600. |
| `/etc/nsswitch.conf` | When the `libnss_tacplus` package is installed, this file is configured to enable tacplus lookups via `libnss_tacplus`. If you replace this file by automation or other means, you need to add tacplus as the first lookup method for the *passwd* database line. |
| `/etc/tacplus_nss.conf` |This file sets the basic parameters for `libnss_tacplus`. It includes a debug variable for debugging NSS lookups separately from other client packages. |
| `/usr/share/pam-configs/tacplus` | This is the configuration file for `pam-auth-update` to generate the files in the next row. These configurations are used at `login`, by `su`, and by `ssh`. |
| `/etc/pam.d/common-*` | The `/etc/pam.d/common-*` files are updated for `tacplus` authentication. The files are updated with `pam-auth-update`, when `libpam-tacplus` is installed or removed. |
| `/etc/sudoers.d/tacplus` | This file allows TACACS+ privilege level 15 users to run commands with `sudo`. The file includes an example (commented out) of how to enable privilege level 15 TACACS users to use `sudo` without having to enter a password and provides an example of how to enable all TACACS users to run specific commands with sudo. Only edit this file with the `visudo -f /etc/sudoers.d/tacplus` command. |
| `/etc/audisp/plugins.d/audisp-tacplus.conf` | This is the `audisp` plugin configuration file. Typically, no modifications are required. |
| `/etc/audisp/audisp-tac_plus.conf` | This is the TACACS+ server configuration file for accounting. Typically, no modifications are required. You can use this configuration file when you only want to debug TACACS+ accounting issues, not all TACACS+ users. |
| `/etc/audit/rules.d/audisp-tacplus.rules` | The `auditd` rules for TACACS+ accounting. The `augenrules` command uses all rule files to generate the rules file (described below). |
| `/etc/audit/audit.rules`|This is the audit rules file generated when `auditd` is installed. |

{{%notice warning%}}

You can edit the `/etc/pam.d/common-*` files manually. However, if you run `pam-auth-update` again after making the changes, the update fails. Only perform configuration in `/usr/share/pam-configs/tacplus`, then run `pam-auth-update`.

{{%/notice%}}

## TACACS+ Authentication (login)

The initial authentication configuration is done through the PAM modules and an updated version of the `libpam-tacplus` package. When the package is installed, the PAM configuration is updated in `/etc/pam.d` with the `pam-auth-update` command. If you have made changes to your PAM configuration, you need to integrate these changes yourself. If you are also using LDAP with the `libpam-ldap` package, you might need to edit the PAM configuration to ensure the LDAP and TACACS ordering that you prefer. The `libpam-tacplus` are configured to skip over rules and the values in the `success=2` might require adjustments to skip over LDAP rules.

A user privilege level is determined by the TACACS+ privilege attribute `priv_lvl` for the user that is returned by the TACACS+ server during the user authorization exchange. The client accepts the attribute in either the mandatory or optional forms and also accepts `priv-lvl` as the attribute name. The attribute value must be a numeric string in the range 0 to 15, with 15 the most privileged level.

{{%notice note%}}

By default, TACACS+ users at privilege levels other than 15 are not allowed to run `sudo` commands and are limited to commands that can be run with standard Linux user permissions.

{{%/notice%}}

### TACACS+ Client Sequencing

Due to SSH and login processing mechanisms, Cumulus Linux needs to know the following very early in the AAA sequence:

- Whether the user is a valid TACACS+ user
- The user's privilege level

The only way to do this for non-local users &mdash; that is, users not present in the local password file &mdash; is to send a TACACS+ authorization request as the first communication with the TACACS+ server, prior to the authentication and before a password is requested from the user logging in.

Some TACACS+ servers need special configuration to allow authorization requests prior to authentication. Contact your TACACS+ server vendor for the proper configuration if your TACACS+ server does not allow the initial authorization request.

## Local Fallback Authentication

You can configure the switch to allow local fallback authentication for a user when the TACACS servers are unreachable, do not include the user for authentication, or have the user in the exclude user list.

To allow local fallback authentication for a user, add a local privileged user account on the switch with the same username as a TACACS user. A local user is always active even when the TACACS service is not running.

To configure local fallback authentication:

1. Edit the `/etc/nsswitch.conf` file to remove the keyword `tacplus` from the line starting with `passwd`. (You need to add the keyword back in step 3.)

    An example of the `/etc/nsswitch.conf` file with the keyword `tacplus` removed from the line starting with `passwd` is shown below.

    ```
    cumulus@switch:~$ sudo nano /etc/nsswitch.conf
    #
    # Example configuration of GNU Name Service Switch functionality.
    # If you have the `glibc-doc-reference' and `info' packages installed, try:
    # `info libc "Name Service Switch"' for information about this file.

    passwd:         files
    group:          tacplus files
    shadow:         files
    gshadow:        files
    ...
    ```

2. To enable the local privileged user to run `sudo` and NCLU commands, run the `adduser` commands shown below. In the example commands, the TACACS account name is tacadmin.

    {{%notice note%}}

The first `adduser` command prompts for information and a password. You can skip most of the requested information by pressing ENTER.

{{%/notice%}}

    ```
    cumulus@switch:~$ sudo adduser --ingroup tacacs tacadmin
    cumulus@switch:~$ sudo adduser tacadmin netedit
    cumulus@switch:~$ sudo adduser tacadmin sudo
    ```

3. Edit the `/etc/nsswitch.conf` file to add the keyword `tacplus` back to the line starting with `passwd` (the keyword you removed in the first step).

   ```
    cumulus@switch:~$ sudo nano /etc/nsswitch.conf
    #
    # Example configuration of GNU Name Service Switch functionality.
    # If you have the `glibc-doc-reference' and `info' packages installed, try:
    # `info libc "Name Service Switch"' for information about this file.
    passwd:         tacplus files
    group:          tacplus files
    shadow:         files
    gshadow:        files
    ...
    ```

4. Restart the `netd` service with the following command:

    ```
    cumulus@switch:~$ sudo systemctl restart netd
    ```

## TACACS+ Accounting

TACACS+ accounting is implemented with the `audisp` module, with an additional plugin for `auditd`/`audisp`. The plugin maps the auid in the accounting record to a TACACS login, based on the `auid` and `sessionid`. The `audisp` module requires `libnss_tacplus` and uses the `libtacplus_map.so` library interfaces as part of the modified `libpam_tacplus` package.

Communication with the TACACS+ servers is done with the `libsimple-tacact1` library, through `dlopen()`. A maximum of 240 bytes of command name and arguments are sent in the accounting record, due to the TACACS+ field length limitation of 255 bytes.

{{%notice note%}}

All Linux commands result in an accounting record, including commands run as part of the login process or as sub-processes of other commands. This can sometimes generate a large number of accounting records.

{{%/notice%}}

Configure the IP address and encryption key of the server in the `/etc/tacplus_servers` file. Minimal configuration to `auditd` and `audisp` is necessary to enable the audit records necessary for accounting. These records are installed as part of the package.

`audisp-tacplus` installs the audit rules for command accounting. Modifying the configuration files is not usually necessary. However, when a {{<link url="Management-VRF" text="management VRF">}} is configured, the accounting configuration does need special modification because the `auditd` service starts prior to networking. It is necessary to add the *vrf* parameter and to signal the `audisp-tacplus` process to reread the configuration. The example below shows that the management VRF is named *mgmt*. You can place the *vrf* parameter in either the `/etc/tacplus_servers` file or in the `/etc/audisp/audisp-tac_plus.conf` file.

```
vrf=mgmt
```

After editing the configuration file, send the **HUP** signal `killall -HUP audisp-tacplus` to notify the accounting process to reread the file.

{{%notice note%}}

All `sudo` commands run by TACACS+ users generate accounting records against the original TACACS+ login name.

{{%/notice%}}

For more information, refer to the `audisp.8` and `auditd.8` man pages.

## Configure NCLU for TACACS+ Users

When you install or upgrade TACACS+ packages, mapped user accounts are created automatically. All *tacacs0* through *tacacs15* users are added to the *netshow* group.

For any TACACS+ users to execute `net add`, `net del`, and `net commit` commands and to restart services with NCLU, you need to add those users to the `users_with_edit` variable in the `/etc/netd.conf` file. Add the *tacacs15* user and, depending upon your policies, other users (*tacacs1* through *tacacs14*) to this variable.

To give a TACACS+ user access to the show commands, add the *tacacs* group to the `groups_with_show` variable.

{{%notice warning%}}

Do not add the *tacacs* group to the `groups_with_edit` variable; this is dangerous and can potentially enable any user to log into the switch as the root user.

{{%/notice%}}

To add the users, edit the `/etc/netd.conf` file:

```
cumulus@switch:~$ sudo nano /etc/netd.conf
...
# Control which users/groups are allowed to run "add", "del",
# "clear", "abort", and "commit" commands.
users_with_edit = root, cumulus, tacacs15
groups_with_edit = netedit

# Control which users/groups are allowed to run "show" commands
users_with_show = root, cumulus
groups_with_show = netshow, netedit, tacacs
...
```

After you save and exit the `netd.conf` file, restart the `netd` service. Run:

```
cumulus@switch:~$ sudo systemctl restart netd
```

## TACACS+ Per-command Authorization

The `tacplus-auth` command handles the per-command authorization. To make this an enforced authorization, you must change the TACACS+ login to use a restricted shell, with a very limited executable search path. Otherwise, the user can bypass the authorization. The `tacplus-restrict` utility simplifies the setup of the restricted environment. The example below initializes the environment for the *tacacs0* user account. This is the account used for TACACS+ users at privilege level `0`.

```
tacuser0@switch:~$ sudo tacplus-restrict -i -u tacacs0 -a command1 command2 ... commandN
```

If the user/command combination is not authorized by the TACACS+ server, a message similar to the following displays:

```
tacuser0@switch:~$ net show version
net not authorized by TACACS+ with given arguments, not executing
```

The following table provides the command options:

| Option | Description |
|------- |------------ |
| `-i` | Initializes the environment. You only need to issue this option once per username. |
| `-a` | You can invoke the utility with the -a option as many times as desired. For each command in the -a list, a symbolic link is created from tacplus-auth to the relative portion of the command name in the local bin subdirectory. You also need to enable these commands on the TACACS+ server (refer to the TACACS+ server documentation). It is common to have the server allow some options to a command, but not others. |
| `-f` | Re-initializes the environment. If you need to restart, issue the -f option with -i to force the re-initialization; otherwise, repeated use of -i is ignored.<br>As part of the initialization:<br>- The user's shell is changed to /bin/rbash.<br>- Any existing dot files are saved.<br>- A limited environment is set up that does not allow general command execution, but instead allows only commands from the user's local bin subdirectory. |

For example, if you want to allow the user to be able to run the `net` and `ip` commands (if authorized by the TACACS+ server), use the command:

```
cumulus@switch:~$ sudo tacplus-restrict -i -u tacacs0 -a ip net
```

After running this command, examine the `tacacs0` directory::

```
cumulus@switch:~$ sudo ls -lR ~tacacs0
total 12
lrwxrwxrwx 1 root root 22 Nov 21 22:07 ip -> /usr/sbin/tacplus-auth
lrwxrwxrwx 1 root root 22 Nov 21 22:07 net -> /usr/sbin/tacplus-auth
```

Other than shell built-ins, the only two commands the privilege level 0 TACACS users can run are the `ip` and `net` commands.

If you mistakenly add potential commands with the `-a` option, you can remove them. The example below shows how to remove the `net` command:

```
cumulus@switch:~$ sudo rm ~tacacs0/bin/net
```

You can remove all commands as follows:

```
cumulus@switch:~$ sudo rm ~tacacs0/bin/*
```

Use the `man` command on the switch for more information on `tacplus-auth` and `tacplus-restrict`.

```
cumulus@switch:~$ man tacplus-auth tacplus-restrict
```

## NSS Plugin

When used with `pam_tacplus`, TACACS+ authenticated users can log in without a local account on the system using the NSS plugin that comes with the `tacplus_nss` package. The plugin uses the mapped `tacplus` information if the user is not found in the local password file, provides the `getpwnam()` and `getpwuid()`entry point,s and uses the TACACS+ authentication functions.

The plugin asks the TACACS+ server if the user is known, and then for relevant attributes to determine the privilege level of the user. When the `libnss_tacplus` package is installed, `nsswitch.conf` is modified to set `tacplus` as the first lookup method for `passwd`. If the order is changed, lookups return the local accounts, such as `tacacs0`

If the user is not found, a mapped lookup is performed using the `libtacplus.so` exported functions. The privilege level is appended to `tacacs` and the lookup searches for the name in the local password file. For example, privilege level 15 searches for the tacacs15 user. If the user is found, the password structure is filled in with information for the user.

If the user is not found, the privilege level is decremented and checked again until privilege level 0 (user `tacacs0`) is reached. This allows use of only the two local users `tacacs0` and `tacacs15`, if minimal configuration is desired.

## TACACS Configuration Parameters

The recognized configuration options are the same as the `libpam_tacplus` command line arguments; however, not all `pam_tacplus` options are supported. These configuration parameters are documented in the `tacplus_servers.5` man page, which is part of the `libpam-tacplus` package.

The table below describes the configuration options available:

| Configuration Option | Description |
|--------------------- |------------ |
| debug | The output debugging information through syslog(3).<br>**Note**: Debugging is heavy, including passwords. Do not leave debugging enabled on a production switch after you have completed troubleshooting. |
| secret=STRING | The secret key used to encrypt and decrypt packets sent to and received from the server.<br>You can specify the secret key more than once in any order with respect to the server= parameter. When fewer secret= parameters are specified, the last secret given is used for the remaining servers.<br>Only use this parameter in files such as /etc/tacplus_servers that are not world readable. |
| server=hostname<br>server=ip-address | Adds a TACACS+ server to the servers list. Servers are queried in turn until a match is found, or no servers remain in the list. Can be specified up to 7 times. An IP address can be optionally followed by a port number, preceded by a ":". The default port is 49.<br>**Note**: When sending accounting records, the record is sent to all servers in the list if acct_all=1, which is the default. |
| source_ip=ipv4-address | Sets the IP address used as the source IP address when communicating with the TACACS+ server. You must specify an IPv4 address. IPv6 addresses and hostnames are not supported. The address must must be valid for the interface being used. |
| timeout=seconds | TACACS+ server(s) communication timeout.<br>This parameter defaults to 10 seconds in the /etc/tacplus_servers file, but defaults to 5 seconds in the /etc/tacplus_nss.conf file. |
| include=/file/name | A supplemental configuration file to avoid duplicating configuration information. You can include up to 8 more configuration files. |
| min_uid=value | The minimum user ID that the NSS plugin looks up. Setting it to 0 means uid 0 (root) is never looked up, which is desirable for performance reasons. The value should not be greater than the local TACACS+ user IDs (0 through 15), to ensure they can be looked up. |
| exclude_users=user1,user2,... | A comma-separated list of usernames that are never looked up by the NSS plugin, set in the tacplus_nss.conf file. You cannot use * (asterisk) as a wild card in the list. While it's not a legal username, bash may lookup this as a user name during pathname completion, so it is included in this list as a username string.<br>**Note**: Do not remove the cumulus user from the exclude_users list; doing so can make it impossible to log in as the cumulus user, which is the primary administrative account in Cumulus Linux. If you do remove the cumulus user, add some other local fallback user that does not rely on TACACS but is a member of sudo and netedit groups, so that these accounts can run sudo and NCLU commands. |
| login=string | TACACS+ authentication service (pap, chap, or login).<br>The default value is pap.|
|user_homedir=1|This is not enabled by default. When enabled, a separate home directory for each TACACS+ user is created when the TACACS+ user first logs in. By default, the home directory in the mapping accounts in /etc/passwd (/home/tacacs0 ... /home/tacacs15) is used. If the home directory does not exist, it is created with the mkhomedir_helper program, in the same way as pam_mkhomedir.<br>This option is not honored for accounts with restricted shells when per-command authorization is enabled. |
| acct_all=1 | Configuration option for audisp_tacplus and pam_tacplus sending accounting records to all supplied servers (1), or the first server to respond (0).<br>The default value is 1. |
| timeout=seconds | Sets the timeout in seconds for connections to each TACACS+ server.<br>The default is 10 seconds for all lookups except that NSS lookups use a 5 second timeout. |
| vrf=vrf-name | If the management network is in a VRF, set this variable to the VRF name. This is typically mgmt. When this variable is set, the connection to the TACACS+ accounting servers is made through the named VRF. |
| service | TACACS+ accounting and authorization service. Examples include shell, pap, raccess, ppp, and slip.<br>The default value is shell. |
| protocol | TACACS+ protocol field. This option is use dependent. PAM uses the SSH protocol. |

## Remove the TACACS+ Client Packages

To remove all of the TACACS+ client packages, use the following commands:

```
cumulus@switch:~$ sudo -E apt-get remove tacplus-client
cumulus@switch:~$ sudo -E apt-get autoremove
```

To remove the TACACS+ client configuration files as well as the packages (recommended), use this command:

```
cumulus@switch:~$ sudo -E apt-get autoremove --purge
```

## Troubleshooting

### Basic Server Connectivity or NSS Issues

You can use the `getent` command to determine if TACACS+ is configured correctly and if the local password is stored in the configuration files. In the example commands below, the cumulus user represents the local user, while cumulusTAC represents the TACACS user.

To look up the username within all NSS methods:

```
cumulus@switch:~$ sudo getent passwd cumulusTAC
cumulusTAC:x:1016:1001:TACACS+ mapped user at privilege level 15,,,:/home/tacacs15:/bin/bash
```

To look up the user within the local database only:

```
cumulus@switch:~$ sudo getent -s compat passwd cumulus
cumulus:x:1000:1000:cumulus,,,:/home/cumulus:/bin/bash
```

To look up the user within the TACACS+ database only:

```
cumulus@switch:~$ sudo getent -s tacplus passwd cumulusTAC
cumulusTAC:x:1016:1001:TACACS+ mapped user at privilege level 15,,,:/home/tacacs15:/bin/bash
```

If TACACS does not appear to be working correctly, debug the following configuration files by adding the *debug=1* parameter to one or more of these files:

- `/etc/tacplus_servers`
- `/etc/tacplus_nss.conf`

{{%notice note%}}

You can also add `debug=1` to individual pam_tacplus lines in `/etc/pam.d/common*`.

{{%/notice%}}

All log messages are stored in `/var/log/syslog`.

#### Incorrect Shared Key

The TACACS client on the switch and the TACACS server should have the same shared secret key. If this key is incorrect, the following message is printed to `syslog`:

```
2017-09-05T19:57:00.356520+00:00 leaf01 sshd[3176]: nss_tacplus: TACACS+ server 192.168.0.254:49 read failed with protocol error (incorrect shared secret?) user cumulus
```

### Issues with Per-command Authorization

To debug TACACS user command authorization, have the TACACS+ user enter
the following command at a shell prompt, then try the command again:

```
tacuser0@switch:~$ export TACACSAUTHDEBUG=1
```

When this debugging is enabled, additional information is shown for the command authorization conversation with the TACACS+ server:

```
tacuser0@switch:~$ net pending
tacplus-auth: found matching command (/usr/bin/net) request authorization
tacplus-auth: error connecting to 10.0.3.195:49 to request authorization for net: Transport endpoint is not connected
tacplus-auth: cmd not authorized (16)
tacplus-auth: net not authorized from 192.168.3.189:49
net not authorized by TACACS+ with given arguments, not executing
```

```
tacuser0@switch:~$ net show version
tacplus-auth: found matching command (/usr/bin/net) request authorization
tacplus-auth: error connecting to 10.0.3.195:49 to request authorization for net: Transport endpoint is not connected
tacplus-auth: 192.168.3.189:49 authorized command net
tacplus-auth: net authorized, executing
DISTRIB_ID="Cumulus Linux"
DISTRIB_RELEASE=4.1.0
DISTRIB_DESCRIPTION="Cumulus Linux 4.1.0"
```

To disable debugging:

```
tacuser0@switch:~$ export -n TACACSAUTHDEBUG
```

### Debug Issues with Accounting Records

If you have added or deleted TACACS+ servers from the configuration files, make sure you notify the `audisp` plugin with this command:

```
cumulus@switch:~$ sudo killall -HUP audisp-tacplus
```

If accounting records are still not being sent, add *debug=1* to the `/etc/audisp/audisp-tac_plus.conf` file, then issue the command above to notify the plugin. Ask the TACACS+ user to run a command and examine the end of `/var/log/syslog` for messages from the plugin. You can also check the auditing log file `/var/log/audit audit.log` to be sure the auditing records are being written. If they are not, restart the audit daemon with:

```
cumulus@switch:~$ sudo systemctl restart auditd.service
```

### TACACS Component Software Descriptions

The following table describes the different pieces of software involved with delivering TACACS.

| Package Name| Description|
|--------|---------|
| audisp-tacplus\_1.0.0-1-cl3u3 | This package uses auditing data from `auditd` to send accounting records to the TACACS+ server and is started as part of `auditd`. |
| libtac2\_1.4.0-cl3u2 | Basic TACACS+ server utility and communications routines. |
| libnss-tacplus\_1.0.1-cl3u3 | Provides an interface between `libc` username lookups, the mapping functions, and the TACACS+ server. |
| tacplus-auth-1.0.0-cl3u1 | This package includes the `tacplus-restrict` setup utility, which enables you to perform per-command TACACS+ authorization. Per-command authorization is not done by default. |
| libpam-tacplus\_1.4.0-1-cl3u2 | A modified version of the standard Debian package. |
| libtacplus-map1\_1.0.0-cl3u2 | The mapping functionality between local and TACACS+ users on the server. Sets the immutable `sessionid` and auditing UID to ensure the original user can be tracked through multiple processes and privilege changes. Sets the auditing `loginuid` as immutable if supported. Creates and maintains a status database in `/run/tacacs_client_map` to manage and lookup mappings. |
| libsimple-tacacct1\_1.0.0-cl3u2 | Provides an interface for programs to send accounting records to the TACACS+ server. Used by `audisp-tacplus`. |
| libtac2-bin\_1.4.0-cl3u2 | Provides the `tacc` testing program and TACACS+ man page. |

## Limitations

### TACACS+ Client Is only Supported through the Management Interface

The TACACS+ client is only supported through the management interface on the switch: eth0, eth1, or the VRF management interface. The TACACS+ client is not supported through bonds, switch virtual interfaces (SVIs), or switch port interfaces (swp).

### Multiple TACACS+ Users

If two or more TACACS+ users are logged in simultaneously with the same privilege level, while the accounting records are maintained correctly, a lookup on either name will match both users, while a UID lookup will only return the user that logged in first.

This means that any processes run by either user will be attributed to both, and all files created by either user will be attributed to the first name matched. This is similar to adding two local users to the password file with the same UID and GID, and is an inherent limitation of using the UID for the base user from the password file.

{{%notice note%}}

The current algorithm returns the first name matching the UID from the mapping file; this can be the first or the second user that logged in.

{{%/notice%}}

To work around this issue, you can use the switch audit log or the TACACS server accounting logs to determine which processes and files are created by each user.

- For commands that do not execute other commands (for example, changes to configurations in an editor, or actions with tools like `clagctl` and `vtysh`), no additional accounting is done.
- Per-command authorization is implemented at the most basic level (commands are permitted or denied based on the standard Linux user permissions for the local TACACS users and only privilege level 15 users can run `sudo` commands by default).

The Linux `auditd` system does not always generate audit events for processes when terminated with a signal (with the `kill` system call or internal errors such as SIGSEGV). As a result, processes that exit on a signal that is not caught and handled, might not generate a STOP accounting record.

### Issues with deluser Command

TACACS+ and other non-local users that run the `deluser` command with the `--remove-home` option will see an error about not finding the user in `/etc/passwd`:

```
tacuser0@switch: deluser --remove-home USERNAME
userdel: cannot remove entry 'USERNAME' from /etc/passwd
/usr/sbin/deluser: `/usr/sbin/userdel USERNAME' returned error code 1. Exiting
```

However, the command does remove the home directory. The user can still log in on that account, but will not have a valid home directory. This is a known upstream issue with the `deluser` command for all non-local users.

Only use the `--remove-home` option when the `user_homedir=1` configuration command is in use.

## When Both TACACS+ and RADIUS AAA Clients are Installed

When you have both the TACACS+ and the RADIUS AAA client installed, RADIUS login is not attempted. As a workaround, do not install both the TACACS+ and the RADIUS AAA client on the same switch.
