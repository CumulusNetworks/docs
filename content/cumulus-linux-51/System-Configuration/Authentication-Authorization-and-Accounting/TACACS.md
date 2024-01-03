---
title: TACACS
author: NVIDIA
weight: 180
toc: 4
---
Cumulus Linux implements TACACS+ client AAA (Accounting, Authentication, and Authorization) in a transparent way with minimal configuration. The client implements the TACACS+ protocol as described in {{<exlink url="https://tools.ietf.org/html/draft-grant-tacacs-02" text="this IETF document">}}. There is no need to create accounts or directories on the switch. Accounting records go to all configured TACACS+ servers by default. Using per-command authorization requires additional setup on the switch.

## Supported Features

- Authentication using PAM; includes `login`, `ssh`, `sudo` and `su`
- Runs over the eth0 management interface
- Ability to run in the {{<link url="Management-VRF" text="management VRF">}}
- TACACS+ privilege 15 users can run any command with sudo using the `/etc/sudoers.d/tacplus` file that the `libtacplus-map1` package installs
- Up to seven TACACS+ servers

## Install the TACACS+ Client Packages

You can install the TACACS+ packages even if the switch is not connected to the internet; the packages are in the `cumulus-local-apt-archive` repository in the {{<link url="Adding-and-Updating-Packages#add-packages-from-the-cumulus-linux-local-archive" text="Cumulus Linux image">}}.

To install all required packages, run these commands:

```
cumulus@switch:~$ sudo -E apt-get update
cumulus@switch:~$ sudo -E apt-get install tacplus-client
```

## Configure the TACACS+ Client

{{%notice note%}}

After you configure TACACS+ settings, you must restart both `nvued.service` and `nginx-authenticator.service`:

```
cumulus@switch:~$ sudo systemctl restart nvued.service
cumulus@switch:~$ sudo systemctl restart nginx-authenticator.service
```

{{%/notice%}}

After installing TACACS+, edit the `/etc/tacplus_servers` file to add at least one server and one shared secret (key). You can specify the server and secret parameters in any order anywhere in the file. Whitespace (spaces or tabs) are not allowed. For example, if your TACACS+ server IP address is `192.168.0.30` and your shared secret is `tacacskey`, add these parameters to the `/etc/tacplus_servers` file:

```
secret=tacacskey
server=192.168.0.30
```

Cumulus Linux supports a maximum of seven TACACS+ servers. To specify multiple servers, add one per line to the `/etc/tacplus_servers` file.

Connections establish in the order that this file lists. In most cases, you do not need to change any other parameters. You can add parameters the packages use to this file, which affects all the TACACS+ client software. For example, the timeout value for NSS lookups is 5 seconds by default in the `/etc/tacplus_nss.conf` file, whereas the timeout value for other packages is 10 seconds in the `/etc/tacplus_servers` file. The timeout value applies to each connection to the TACACS+ servers. (If you configure authorization per command, the timeout occurs for *each* command.) There are several connections to the server per login attempt from PAM, as well as two or more through NSS. Therefore, with the default timeout values, a TACACS+ server that is not reachable can delay logins by a minute or more for each unreachable server. If you must list unreachable TACACS+ servers, place them at the end of the server list and consider reducing the timeout values.

When you add or remove TACACS+ servers, you must restart `auditd` (with the `systemctl restart auditd` command) or you must send a signal (with `killall -HUP audisp-tacplus`) before `audisp-tacplus` rereads the configuration to see the changed server list.

You can also configure the IP address used as the source IP address when communicating with the TACACS+ server. See {{<link url="#tacacs-configuration-parameters" text="TACACS Configuration Parameters">}} below for the full list of TACACS+ parameters.

Following is the complete list of the TACACS+ client configuration files, and their use.

| <div style="width:250px">Filename | Description |
|----------|-------------|
| `/etc/tacplus_servers` | The primary file that requires configuration after installation. All packages with `include=/etc/tacplus_servers` parameters use this file. Typically, this file contains the shared secrets; make sure that the Linux file mode is 600. |
| `/etc/nsswitch.conf` | When the `libnss_tacplus` package installs, this file configures tacplus lookups through `libnss_tacplus`. If you replace this file by automation, you need to add tacplus as the first lookup method for the *passwd* database line. |
| `/etc/tacplus_nss.conf` |Sets the basic parameters for `libnss_tacplus`. The file includes a debug variable for debugging NSS lookups separately from other client packages. |
| `/usr/share/pam-configs/tacplus` | The configuration file for `pam-auth-update` to generate the files in the next row. The file uses these configurations at `login`, by `su`, and by `ssh`. |
| `/etc/pam.d/common-*` | The `/etc/pam.d/common-*` files update for `tacplus` authentication. The files update with `pam-auth-update`, when you install or remove `libpam-tacplus`. |
| `/etc/sudoers.d/tacplus` | Allows TACACS+ privilege level 15 users to run commands with `sudo`. The file includes an example (commented out) of how to enable privilege level 15 TACACS users to use `sudo` without a password and provides an example of how to enable all TACACS users to run specific commands with sudo. Only edit this file with the `visudo -f /etc/sudoers.d/tacplus` command. |
| `/etc/audisp/plugins.d/audisp-tacplus.conf` | The `audisp` plugin configuration file. You do not need to modify this file. |
| `/etc/audisp/audisp-tac_plus.conf` | The TACACS+ server configuration file for accounting. You do not need to modify this file. You can use this configuration file when you only want to debug TACACS+ accounting issues, not all TACACS+ users. |
| `/etc/audit/rules.d/audisp-tacplus.rules` | The `auditd` rules for TACACS+ accounting. The `augenrules` command uses all rule files to generate the rules file (described below). |
| `/etc/audit/audit.rules`|The audit rules file that generate when you install `auditd`. |

{{%notice warning%}}

You can edit the `/etc/pam.d/common-*` files manually. However, if you run `pam-auth-update` again after making the changes, the update fails. Only configure `/usr/share/pam-configs/tacplus`, then run `pam-auth-update`.

{{%/notice%}}

## TACACS+ Authentication (login)

PAM modules and an updated version of the `libpam-tacplus` package configure authentication initially. When you install the package, the `pam-auth-update` command updates the PAM configuration in `/etc/pam.d`. If you make changes to your PAM configuration, you need to integrate these changes. If you also use LDAP with the `libpam-ldap` package, you need to edit the PAM configuration with the LDAP and TACACS ordering you prefer. The `libpam-tacplus` package ignore rules and the values in `success=2` require adjustments to ignore LDAP rules.

The TACACS+ privilege attribute `priv_lvl` determines the privilege level for the user that the TACACS+ server returns during the user authorization exchange. The client accepts the attribute in either the mandatory or optional forms and also accepts `priv-lvl` as the attribute name. The attribute value must be a numeric string in the range 0 to 15, with 15 the most privileged level.

{{%notice note%}}

By default, TACACS+ users at privilege levels other than 15 cannot run `sudo` commands and can only run commands with standard Linux user permissions.

{{%/notice%}}

### TACACS+ Client Sequencing

Due to SSH and login processing mechanisms, Cumulus Linux needs to know the following at the beginning of the AAA sequence:

- Whether the user is a valid TACACS+ user
- The user privilege level

For non-local users (users not in the local password file) you need to send a TACACS+ authorization request as the first communication with the TACACS+ server, before authentication and before the user logging in requests a password.

You need to configure certain TACACS+ servers to allow authorization requests before authentication. Contact your TACACS+ server vendor for information.

## Local Fallback Authentication

You can configure the switch to allow local fallback authentication for a user when the TACACS servers are unreachable, do not include the user for authentication, or have the user in the exclude user list.

To allow local fallback authentication for a user, add a local privileged user account on the switch with the same username as a TACACS user. A local user is always active even when the TACACS service is not running.

To configure local fallback authentication:

1. Edit the `/etc/nsswitch.conf` file to remove the keyword `tacplus` from the line starting with `passwd`. (You need to add the keyword back in step 3.)

    The following example shows the `/etc/nsswitch.conf` file with no `tacplus` keyword in the line starting with `passwd`.

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

2. To enable the local privileged user to run `sudo` and NVUE commands, run the `adduser` commands shown below. In the example commands, the TACACS account name is tacadmin.

    {{%notice note%}}

The first `adduser` command prompts for information and a password. You can skip most of the requested information by pressing ENTER.

{{%/notice%}}

    ```
    cumulus@switch:~$ sudo adduser --ingroup tacacs tacadmin
    cumulus@switch:~$ sudo adduser tacadmin nvset
    cumulus@switch:~$ sudo adduser tacadmin nvapply
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

4. Restart the `nvued` service and the `nginx-authenticator` service with the following commands:

    ```
    cumulus@switch:~$ sudo systemctl restart nvued.service
    cumulus@switch:~$ sudo systemctl restart nginx-authenticator.service
    ```

## TACACS+ Accounting

TACACS+ accounting uses the `audisp` module, with an additional plugin for `auditd`/`audisp`. The plugin maps the auid in the accounting record to a TACACS login, which it bases on the `auid` and `sessionid`. The `audisp` module requires `libnss_tacplus` and uses the `libtacplus_map.so` library interfaces as part of the modified `libpam_tacplus` package.

Communication with the TACACS+ servers occurs with the `libsimple-tacact1` library, through `dlopen()`. A maximum of 240 bytes of command name and arguments send in the accounting record, due to the TACACS+ field length limitation of 255 bytes.

{{%notice note%}}

All Linux commands result in an accounting record, including login commands and sub-processes of other commands. This can generate a lot of accounting records.

{{%/notice%}}

Configure the IP address and encryption key of the server in the `/etc/tacplus_servers` file. Minimal configuration to `auditd` and `audisp` is necessary to enable the audit records needed for accounting. These records install as part of the package.

`audisp-tacplus` installs the audit rules for command accounting. When you configure a {{<link url="Management-VRF" text="management VRF">}}, you must add the *vrf* parameter and signal the `audisp-tacplus` process to reread the configuration. The example below shows that the management VRF name is *mgmt*. You can add the *vrf* parameter to either the `/etc/tacplus_servers` file or the `/etc/audisp/audisp-tac_plus.conf` file.

```
vrf=mgmt
```

After editing the configuration file, send the **HUP** signal `killall -HUP audisp-tacplus` to notify the accounting process to reread the file.

{{%notice note%}}

All `sudo` commands run by TACACS+ users generate accounting records against the original TACACS+ login name.

{{%/notice%}}

For more information, refer to the `audisp.8` and `auditd.8` man pages.

<!--## Configure NVUE for TACACS+ Users

When you install or upgrade TACACS+ packages, the installation and update process maps user accounts automatically and adds all *tacacs0* through *tacacs15* users to the *nvshow* group.

If you want any TACACS+ users to execute NVUE commands and restart services with NVUE, you need to add those users to the `/etc/nvue-auth.yaml` file. Add the *tacacs15* user and, depending upon your policies, other users (*tacacs1* through *tacacs14*).

To allow a TACACS+ user access to the nv show commands, add the *tacacs* group to the `read-only access` section of the `/etc/nvue-auth.yaml` file.

{{%notice warning%}}

Do not add the *tacacs* group to the `full read/write access` section of the `/etc/nvue-auth.yaml` file; any user can log into the switch as the root user.

{{%/notice%}}

To add the users, edit the `/etc/nvue-auth.yaml` file:

```
cumulus@switch:~$ sudo nano /etc/nvue-auth.yaml
...
  - reason: full read/write access
    action: allow
    match-request:
      path: '*'
      method: '*'
    match-user:
      name: cumulus
      group:
        - nvapply
        - nvset
  - reason: read-only access
    action: allow
    match-request:
      path: '*'
      method: GET
    match-user:
      group: nvshow
```

After you save and exit the `/etc/nvue-auth.yaml` file, restart the `nvued` service. Run:

```
cumulus@switch:~$ sudo systemctl restart nvued
``` -->
<!-- vale off -->
## TACACS+ Per-command Authorization

The `tacplus-auth` command handles authorization for each command. To make this an enforced authorization, change the TACACS+ login to use a restricted shell, with a very limited executable search path. Otherwise, the user can bypass the authorization. The `tacplus-restrict` utility simplifies setting up the restricted environment. The example below initializes the environment for the *tacacs0* user account. This is the account for TACACS+ users at privilege level `0`.
<!-- vale on -->
```
tacuser0@switch:~$ sudo tacplus-restrict -i -u tacacs0 -a command1 command2 command3
```

The following table provides the command options:

| Option | Description |
|------- |------------ |
| `-i` | Initializes the environment. You only need to issue this option one time per username. |
| `-a` | You can invoke the utility with the `-a` option as often as you like. For each command in the `-a` list, the utility creates a symbolic link from `tacplus-auth` to the relative portion of the command name in the local bin subdirectory. You also need to enable these commands on the TACACS+ server (refer to the TACACS+ server documentation). It is common for the server to allow some options to a command, but not others. |
| `-f` | Re-initializes the environment. If you need to restart, issue the `-f` option with `-i` to force re-initialization; otherwise, the utility ignores repeated use of `-i`.<br>As part of the initialization:<br>- The user shell changes to `/bin/rbash`.<br>- The utility saves any existing dot files. |

For example, if you want to allow the user to be able to run the `nv` and `ip` commands (if authorized by the TACACS+ server):

```
cumulus@switch:~$ sudo tacplus-restrict -i -u tacacs0 -a ip nv
```

After running this command, examine the `tacacs0` directory::

```
cumulus@switch:~$ sudo ls -lR ~tacacs0
total 12
lrwxrwxrwx 1 root root 22 Nov 21 22:07 ip -> /usr/sbin/tacplus-auth
lrwxrwxrwx 1 root root 22 Nov 21 22:07 nv -> /usr/sbin/tacplus-auth
```

Other than shell built-ins, privilege level 0 TACACS users can only run the `ip` and `nv` commands.

If add commands with the `-a` option by mistake, you can remove them. The example below removes the `nv` command:

```
cumulus@switch:~$ sudo rm ~tacacs0/bin/nv
```

You can remove all commands:

```
cumulus@switch:~$ sudo rm ~tacacs0/bin/*
```

For more information on `tacplus-auth` and `tacplus-restrict`, run the `man` command.

```
cumulus@switch:~$ man tacplus-auth tacplus-restrict
```

## NSS Plugin

With `pam_tacplus`, TACACS+ authenticated users can log in without a local account on the system using the NSS plugin that comes with the `tacplus_nss` package. The plugin uses the mapped `tacplus` information if the user is not in the local password file, provides the `getpwnam()` and `getpwuid()`entry points, and uses the TACACS+ authentication functions.

The plugin asks the TACACS+ server if it knows the user, and then for relevant attributes to determine the privilege level of the user. When you install the `libnss_tacplus` package, `nsswitch.conf` changes to set `tacplus` as the first lookup method for `passwd`. If you change the order, lookups return the local accounts, such as `tacacs0`

If TACACS+ server does not find the user, it uses the `libtacplus.so` exported functions to do a mapped lookup. The privilege level appends to `tacacs` and the lookup searches for the name in the local password file. For example, privilege level 15 searches for the tacacs15 user. If the TACACS+ server finds the user, it adds information for the user in the password structure.

If the TACACS+ server does not find the user, it decrements the privilege level and checks again until it reaches privilege level 0 (user `tacacs0`). This allows you to use only the two local users `tacacs0` and `tacacs15`, for minimal configuration.

## TACACS Configuration Parameters

The recognized configuration options are the same as the `libpam_tacplus` command line arguments; however, Cumulus Linux does not support all `pam_tacplus` options. For a description of the configuration parameters, refer to the `tacplus_servers.5` man page, which is part of the `libpam-tacplus` package.

The table below describes the configuration options available:

| Configuration Option | Description |
|--------------------- |------------ |
| debug | The output debugging information through syslog(3).<br>**Note**: Debugging is heavy, including passwords. Do not leave debugging enabled on a production switch after you have completed troubleshooting. |
| secret=STRING | The secret key to encrypt and decrypt packets sent to and received from the server.<br>You can specify the secret key more than one time in any order. <br>Only use this parameter in files such as /etc/tacplus_servers that are not world readable. |
| server=hostname<br>server=ip-address | Adds a TACACS+ server to the servers list. Cumulus Linux queries servers in turn until it finds a match or no servers remain in the list. You can provide an IP address with a port number, preceded by a colon (:). The default port is 49.<br>**Note**: When sending accounting records, the record sends to all servers in the list if `acct_all=1`, which is the default. |
| source_ip=ipv4-address | Sets the IP address as the source IP address when communicating with the TACACS+ server. You must specify an IPv4 address. You cannot use IPv6 addresses and hostnames. The address must be valid for the interface you use. |
| timeout=seconds | TACACS+ servers communication timeout.<br>This parameter defaults to 10 seconds in the /etc/tacplus_servers file, but defaults to 5 seconds in the /etc/tacplus_nss.conf file. |
| include=/file/name | A supplemental configuration file to avoid duplicating configuration information. You can include up to 8 more configuration files. |
| min_uid=value | The minimum user ID that the NSS plugin looks up. 0 specifies that the plugin never looks up uid 0 (root). Do not specify a value greater than the local TACACS+ user IDs (0 through 15). |
| exclude_users=user1,user2,| A comma-separated list of usernames in the `tacplus_nss.conf` file that the NSS plugin never looks up. You cannot use * (asterisk) as a wild card in the list. While it is not a legal username, bash can look up this asterisk as a username during pathname completion, so it is in this list as a username string.<br>**Note**: Do not remove the cumulus user from the `exclude_users` list; doing so can make it impossible to log in as the cumulus user, which is the primary administrative account in Cumulus Linux. If you do remove the cumulus user, add some other local fallback user that does not rely on TACACS but is a member of sudo and NVUE read/write groups, so that these accounts can run sudo and NVUE commands. |
| login=string | TACACS+ authentication service (pap, chap, or login).<br>The default value is pap.|
|user_homedir=1|This option is off by default. When you enable this option, Cumulus Linux creates a separate home directory for each TACACS+ user when the TACACS+ user first logs in. By default, the switch uses the home directory in the mapping accounts in `/etc/passwd` (`/home/tacacs0` through `/home/tacacs15`). If the home directory does not exist, the `mkhomedir_helper` program creates it, in the same way as `pam_mkhomedir`.<br>This option does not apply for accounts with restricted shells when you enable per-command authorization. |
| acct_all=1 | Configuration option for audisp_tacplus and pam_tacplus sending accounting records to all supplied servers (1), or the first server to respond (0).<br>The default value is 1. |
| timeout=seconds | Sets the timeout in seconds for connections to each TACACS+ server.<br>The default is 10 seconds for all lookups. NSS lookups use a 5 second timeout. |
| vrf=vrf-name | If the management network is in a VRF, set this variable to the VRF name. This is typically `mgmt`. When you set this variable, the connection to the TACACS+ accounting servers establishes through the named VRF. |
| service | TACACS+ accounting and authorization service. Examples include shell, pap, raccess, ppp, and slip.<br>The default value is shell. |
| protocol | TACACS+ protocol field. This option is user dependent. PAM uses the SSH protocol. |

## Remove the TACACS+ Client Packages

To remove all the TACACS+ client packages, use the following commands:

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

You can use the `getent` command to determine if you configured TACACS+ correctly and if the local password is in the configuration files. In the example commands below, the cumulus user represents the local user, while cumulusTAC represents the TACACS user.

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

If TACACS is not working correctly, debug the following configuration files by adding the *debug=1* parameter to one or more of these files:

- `/etc/tacplus_servers`
- `/etc/tacplus_nss.conf`

{{%notice note%}}

You can also add `debug=1` to individual pam_tacplus lines in `/etc/pam.d/common*`.

{{%/notice%}}

All log messages are in `/var/log/syslog`.

#### Incorrect Shared Key

The TACACS client on the switch and the TACACS server must have the same shared secret key. If this key is incorrect, the following message prints to `syslog`:

```
2017-09-05T19:57:00.356520+00:00 leaf01 sshd[3176]: nss_tacplus: TACACS+ server 192.168.0.254:49 read failed with protocol error (incorrect shared secret?) user cumulus
```
<!-- vale off -->
### Issues with Per-command Authorization
<!-- vale on -->
To debug TACACS user command authorization, have the TACACS+ user enter the following command at a shell prompt, then try the command again:

```
tacuser0@switch:~$ export TACACSAUTHDEBUG=1
```

When you enable debugging, the command authorization conversation with the TACACS+ server shows additional information.

To disable debugging:

```
tacuser0@switch:~$ export -n TACACSAUTHDEBUG
```

### Debug Issues with Accounting Records

If you add or delete TACACS+ servers from the configuration files, make sure you notify the `audisp` plugin with this command:

```
cumulus@switch:~$ sudo killall -HUP audisp-tacplus
```

If accounting records do not send, add *debug=1* to the `/etc/audisp/audisp-tac_plus.conf` file, then run the command above to notify the plugin. Ask the TACACS+ user to run a command and examine the end of `/var/log/syslog` for messages from the plugin. You can also check the auditing log file `/var/log/audit audit.log` to be sure the auditing records exist. If the auditing records do not exist, restart the audit daemon with:

```
cumulus@switch:~$ sudo systemctl restart auditd.service
```

### TACACS Component Software Descriptions

Cumulus Linux uses the following packages for TACACS.

| Package Name| Description|
|--------|---------|
| audisp-tacplus\_1.0.0-1-cl3u3 | This package uses auditing data from `auditd` to send accounting records to the TACACS+ server and starts as part of `auditd`. |
| libtac2\_1.4.0-cl3u2 | Basic TACACS+ server utility and communications routines. |
| libnss-tacplus\_1.0.1-cl3u3 | Provides an interface between `libc` username lookups, the mapping functions, and the TACACS+ server. |
| tacplus-auth-1.0.0-cl3u1 | Includes the `tacplus-restrict` setup utility, which enables you to perform per-command TACACS+ authorization. Per-command authorization is not the default. |
| libpam-tacplus\_1.4.0-1-cl3u2 | A modified version of the standard Debian package. |
| libtacplus-map1\_1.0.0-cl3u2 | The mapping functionality between local and TACACS+ users on the server. Sets the immutable `sessionid` and auditing UID to ensure that you can track the original user through multiple processes and privilege changes. Sets the auditing `loginuid` as immutable. Creates and maintains a status database in `/run/tacacs_client_map` to manage and lookup mappings. |
| libsimple-tacacct1\_1.0.0-cl3u2 | Provides an interface for programs to send accounting records to the TACACS+ server. `audisp-tacplus` uses this package. |
| libtac2-bin\_1.4.0-cl3u2 | Provides the `tacc` testing program and TACACS+ man page. |

## Considerations

### TACACS+ Client Is only Supported through the Management Interface

The TACACS+ client is only supported through the management interface on the switch: eth0, eth1, or the VRF management interface. The TACACS+ client is not supported through bonds, switch virtual interfaces (SVIs), or switch port interfaces (swp).

### Multiple TACACS+ Users

If two or more TACACS+ users log in simultaneously with the same privilege level, while the accounting records are correct, a lookup on either name matches both users, while a UID lookup only returns the user that logs in first.

This means that any processes that either user runs apply to both, and all files either user creates apply to the first name matched. This is similar to adding two local users to the password file with the same UID and GID, and is an inherent limitation of using the UID for the base user from the password file.

{{%notice note%}}

The current algorithm returns the first name matching the UID from the mapping file; either the first or the second user that logs in.

{{%/notice%}}

To work around this issue, you can use the switch audit log or the TACACS server accounting logs to determine which processes and files each user creates.

- For commands that do not execute other commands (for example, changes to configurations in an editor or actions with tools like `clagctl` and vtysh), there is no additional accounting.
- Per-command authorization is at the most basic level (Cumulus Linux uses standard Linux user permissions for the local TACACS users and only privilege level 15 users can run `sudo` commands by default).

The Linux `auditd` system does not always generate audit events for processes when terminated with a signal (with the `kill` system call or internal errors such as SIGSEGV). As a result, processes that exit on a signal that you do not handle, generate a STOP accounting record.

### Issues with deluser Command

TACACS+ and other non-local users that run the `deluser` command with the `--remove-home` option see the following error:

```
tacuser0@switch: deluser --remove-home USERNAME
userdel: cannot remove entry 'USERNAME' from /etc/passwd
/usr/sbin/deluser: `/usr/sbin/userdel USERNAME' returned error code 1. Exiting
```

The command does remove the home directory. The user can still log in on that account but does not have a valid home directory. This is a known upstream issue with the `deluser` command for all non-local users.

Only use the `--remove-home` option with the `user_homedir=1` configuration command.

### Both TACACS+ and RADIUS AAA Clients

When you install both the TACACS+ and the RADIUS AAA client, Cumulus Linux does not attempt RADIUS login. As a workaround, do not install both the TACACS+ and the RADIUS AAA client on the same switch.
