---
title: TACACS
author: NVIDIA
weight: 180
toc: 4
---
Cumulus Linux implements TACACS+ client <span style="background-color:#F5F5DC">[AAA](## "Accounting, Authentication, and Authorization")</span> in a transparent way with minimal configuration. The client implements the TACACS+ protocol as described in {{<exlink url="https://tools.ietf.org/html/draft-grant-tacacs-02" text="this IETF document">}}. There is no need to create accounts or directories on the switch. Accounting records go to all configured TACACS+ servers by default. Using per-command authorization requires additional setup on the switch.

TACACS+ in Cumulus Linux:
- Uses PAM authentication and includes `login`, `ssh`, `sudo` and `su`.
- Allows users with privilege level 15 to run any command with sudo.
- Allows users with privilege level 15 to run NVUE `nv set`, `nv unset`, and `nv apply` commands in addition to `nv show` commands. TACACS+ users with a lower privilege level can only execute `nv show` commands.
- Supports up to seven TACACS+ servers. Be sure to configure your TACACS+ servers in addition to the TACACS+ client. Refer to your TACACS+ server documentation.

## Install the TACACS+ Client Packages

{{%notice note%}}
You must install the TACACS+ client packages to use TACACS+. If you do not install the TACACS+ packages, you see the following message when you try to enable TACACS+ with the NVUE `nv set system aaa tacacs enable on` command:

```
'tacplus-client' package needs to be installed to enable tacacs
```

{{%/notice%}}

You can install the TACACS+ packages even if the switch is not connected to the internet; the packages are in the `cumulus-local-apt-archive` repository in the {{<link url="Adding-and-Updating-Packages#add-packages-from-the-cumulus-linux-local-archive" text="Cumulus Linux image">}}.

To install all required packages, run these commands:

```
cumulus@switch:~$ sudo -E apt-get update
cumulus@switch:~$ sudo -E apt-get install tacplus-client
```

## Required TACACS+ Client Configuration

After you install the required TACACS+ packages, configure the following required settings on the switch (the TACACS+ client).
- Set the IP address or hostname of at least one TACACS+ server.
- Set the secret (key) shared between the TACACS+ server and client.
- Set the VRF you want to use to communicate with the TACACS+ server. This is typically the management VRF (`mgmt`), which is the default VRF on the switch.

If you use NVUE commands to configure TACACS+, you must also set the priority for the authentication order for local and TACACS+ users, and enable TACACS+.

{{%notice note%}}

After you change TACACS+ settings, you must restart both `nvued.service` and `nginx-authenticator.service`:

```
cumulus@switch:~$ sudo systemctl restart nvued.service
cumulus@switch:~$ sudo systemctl restart nginx-authenticator.service
```

{{%/notice%}}

{{< tabs "TabID31 ">}}
{{< tab "NVUE Commands ">}}

NVUE commands require you to specify the priority for each TACACS+ server. You must set a priority even if you only specify one server.

The following example commands set:
- The TACACS+ server priority to 5.
- The IP address of the server to 192.168.0.30.
- The secret to `mytacac$key`.
  {{%notice note%}}
  If you include special characters in the password (such as $), you must enclose the password in single quotes (').
  {{%/notice%}}
- The VRF to `mgmt`.
- The authentication order so that TACACS+ authentication has priority over local (the lower number has priority).
- TACACS+ to enabled.

```
cumulus@switch:~$ nv set system aaa tacacs server 5 host 192.168.0.30
cumulus@switch:~$ nv set system aaa tacacs server 5 secret 'mytacac$key'
cumulus@switch:~$ nv set system aaa tacacs vrf mgmt 
cumulus@switch:~$ nv set system aaa authentication-order 5 tacacs
cumulus@switch:~$ nv set system aaa authentication-order 10 local
cumulus@switch:~$ nv set system aaa tacacs enable on
cumulus@switch:~$ nv config apply
```

If you want the server to use IPv6, you must add the `nv set system aaa tacacs server <priority> prefer-ip-version 6` command:

```
cumulus@switch:~$ nv set system aaa tacacs server 5 host server5
cumulus@switch:~$ nv set system aaa tacacs server 5 prefer-ip-version 6
...
```

If you configure more than one TACACS+ server, you need to set the priority for each server. If the switch cannot establish a connection with the server that has the highest priority, it tries to establish a connection with the next highest priority server. The server with the lower number has the higher prioritity. In the example below, server 192.168.0.30 with a priority value of 5 has a higher priority than server 192.168.1.30, which has a priority value of 10.

```
cumulus@switch:~$ nv set system aaa tacacs server 5 host 192.168.0.30
cumulus@switch:~$ nv set system aaa tacacs server 5 secret 'mytacac$key' 
cumulus@switch:~$ nv set system aaa tacacs server 10 host 192.168.1.30
cumulus@switch:~$ nv set system aaa tacacs server 10 secret 'mytacac$key2'
cumulus@switch:~$ nv config apply
```

{{< /tab >}}
{{< tab "Linux Commands ">}}

1. Edit the `/etc/tacplus_servers` file to add at least one server and one shared secret (key). You can specify the server and secret parameters in any order anywhere in the file. Whitespace (spaces or tabs) are not allowed. For example, if your TACACS+ server IP address is `192.168.0.30` and your shared secret is `tacacskey`, add these parameters to the `/etc/tacplus_servers` file:

   ```
   cumulus@switch:~$ sudo nano /etc/tacplus_servers
   secret=mytacac$key
   server=192.168.0.30
   ```

   Cumulus Linux supports a maximum of seven TACACS+ servers. To specify multiple servers, add one per line to the `/etc/tacplus_servers` file. Connections establish in the order in the file.

   ```
   cumulus@switch:~$ sudo nano /etc/tacplus_servers
   secret=mytacac$key
   server=192.168.0.30
   secret=mytacac$key2
   server=192.168.1.30
   ```

   If you want the server to use IPv6, you must add the `prefer_ip_version=6` parameter in the `/etc/tacplus_servers` file:

   ```
   cumulus@switch:~$ sudo nano /etc/tacplus_servers
   secret=mytacac$key
   server=server5
   prefer_ip_version=ipv6 
   secret=mytacac$key2
   server=server6
   prefer_ip_version=ipv6 
   ```

2. Uncomment the `vrf=mgmt` line:

   ```
   # If the management network is in a vrf, set this variable to the vrf name.
   # This would usually be "mgmt"
   # When this variable is set, the connection to the TACACS+ accounting servers
   # will be made through the named vrf.
   vrf=mgmt
   ```

3. Restart `auditd`:

   ```
   cumulus@switch:~$ sudo systemctl restart auditd
   ```

{{< /tab >}}
{{< /tabs >}}

## Optional TACACS+ Configuration

You can configure the following optional TACACS+ settings:
- The port to use for communication between the TACACS+ server and client. By default, Cumulus Linux uses IP port 49.
- The TACACS timeout value, which is the number of seconds to wait for a response from the TACACS+ server before trying the next TACACS+ server. You can specify a value between 0 and 60. The default is 5 seconds.
- The source IP address to use when communicating with the TACACS+ server so that the server can identify the client switch. You must specify an IPv4 address, which must be valid for the interface you use. This source IP address is typically the loopback address on the switch.
<!-- vale off -->
- The TACACS+ authentication type. You can specify <span style="background-color:#F5F5DC">[PAP](## "Password Authentication Protocol")</span> to send clear text between the user and the server, <span style="background-color:#F5F5DC">[CHAP](## "Challenge Handshake Authentication Protocol")</span> to establish a <span style="background-color:#F5F5DC">[PPP](## "Point-to-Point Protocol")</span> connection between the user and the server, or login. The default is PAP.
<!-- vale on -->
- The users you do not want to send to the TACACS+ server for authentication; for example, local user accounts that exist on the switch, such as the cumulus user.
- A separate home directory for each TACACS+ user when the TACACS+ user first logs in. By default, the switch uses the home directory in the mapping accounts in `/etc/passwd`. If the home directory does not exist, the `mkhomedir_helper` program creates it. This option does not apply to accounts with restricted shells (users mapped to a TACACS privilege level that has enforced per-command authorization).

<!-- - The output debugging information level through syslog(3) to use for troubleshooting. You can specify a value between 0 and 2. The default is 0. A value of 1 enables debug logging. A value of 2 increases the verbosity of some debug logs.

  {{%notice note%}}
  Do not leave debugging enabled on a production switch after you complete troubleshooting.
  {{%/notice%}}
-->
{{< tabs "TabID111 ">}}
{{< tab "NVUE Commands ">}}

The following example commands set the timeout to 10 seconds and the TACACS+ server port to 32:

```
cumulus@switch:~$ nv set system aaa tacacs timeout 10
cumulus@switch:~$ nv set system aaa tacacs server 5 port 32
cumulus@switch:~$ nv config apply
```

The following example commands set the source IP address to 10.10.10.1 and the authentication type to CHAP:

```
cumulus@switch:~$ nv set system aaa tacacs source-ip 10.10.10.1
cumulus@switch:~$ nv set system aaa tacacs authentication mode chap
cumulus@switch:~$ nv config apply
```

The following example commands exclude the user `USER1` from going to the TACACS+ server for authentication and enables Cumulus Linux to create a separate home directory for each TACACS+ user when the TACACS+ user first logs in:

```
cumulus@switch:~$ nv set system aaa tacacs exclude-user USER1
cumulus@switch:~$ nv set system aaa tacacs authentication per-user-homedir on
cumulus@switch:~$ nv config apply
```

{{< /tab >}}
{{< tab "Linux Commands ">}}

- To set the server port (use the format `server:port`), source IP address, authentication type, and enable Cumulus Linux to create a separate home directory for each TACACS+ user, edit the `/etc/tacplus_servers` file, then restart `auditd`.
- To set the timeout and the usernames to exclude from TACACS+ authentication, edit the `/etc/tacplus_nss.conf` file (you do not need to restart `auditd`).

The following example sets the server port to 32, the authentication type to CHAP, the source IP address to 10.10.10.1, and enables Cumulus Linux to create a separate home directory for each TACACS+ user when the TACACS+ user first logs in:

```
cumulus@switch:~$ sudo nano /etc/tacplus_servers
...
secret=mytacac$key
server=192.168.0.30:32
...
# Sets the IPv4 address used as the source IP address when communicating with
# the TACACS+ server.  IPv6 addresses are not supported, nor are hostnames.
# The address must work when passsed to the bind() system call, that is, it must
# be valid for the interface being used.
source_ip=10.10.10.1
...
# If user_homedir=1, then tacacs users will be set to have a home directory
# based on their login name, rather than the mapped tacacsN home directory.
# mkhomedir_helper is used to create the directory if it does not exist (similar
# to use of pam_mkhomedir.so). This flag is ignored for users with restricted
# shells, e.g., users mapped to a tacacs privilege level that has enforced
# per-command authorization (see the tacplus-restrict man page).
user_homedir=1
...
login=chap
```

```
cumulus@switch:~$ sudo systemctl restart auditd
```

The following example sets the timeout to 10 seconds and excludes the user `USER1` from going to the TACACS+ server for authentication:

```
cumulus@switch:~$ sudo nano /etc/tacplus_nss.conf
...
# The connection timeout for an NSS library should be short, since it is
# invoked for many programs and daemons, and a failure is usually not
# catastrophic.  Not set or set to a negative value disables use of poll().
# This follows the include of tacplus_servers, so it can override any
# timeout value set in that file.
# It's important to have this set in this file, even if the same value
# as in tacplus_servers, since tacplus_servers should not be readable
# by users other than root.
timeout=10
...
# This is a comma separated list of usernames that are never sent to
# a tacacs server, they cause an early not found return.
#
# "*" is not a wild card.  While it's not a legal username, it turns out
# that during pathname completion, bash can do an NSS lookup on "*"
# To avoid server round trip delays, or worse, unreachable server delays
# on filename completion, we include "*" in the exclusion list.
exclude_users=root,daemon,nobody,cron,radius_user,radius_priv_user,sshd,cumulus,quagga,frr,snmp,www-data,ntp,man,_lldpd,USER1,*
```

Cumulus Linux supports the following additional Linux parameters in the `etc/tacplus_nss.conf` file. Currently, there are no equivalent NUVE commands.

| Linux Parameter | Description |
| --------------- | ----------- |
| `include` | Configures a supplemental configuration file to avoid duplicating configuration information. You can include up to eight additional configuration files. For example: `include=/myfile/myname`. |
| `min_uid` | Configures the minimum user ID that the NSS plugin can look up. 0 specifies that the plugin never looks up uid 0 (root). Do not specify a value greater than the local TACACS+ user IDs (0 through 15). |

{{< /tab >}}
{{< /tabs >}}

## TACACS+ Accounting

When you install the TACACS+ packages and configure the basic TACACS+ settings (set the server and shared secret), accounting is on and there is no additional configuration required.

TACACS+ accounting uses the `audisp` module, with an additional plugin for `auditd` and `audisp`. The plugin maps the `auid` in the accounting record to a TACACS login, which it bases on the `auid` and `sessionid`. The `audisp` module requires `libnss_tacplus` and uses the `libtacplus_map.so` library interfaces as part of the modified `libpam_tacplus` package.

Communication with the TACACS+ servers occurs with the `libsimple-tacact1` library, through `dlopen()`. A maximum of 240 bytes of command name and arguments send in the accounting record, due to the TACACS+ field length limitation of 255 bytes.

{{%notice note%}}
- All `sudo` commands run by TACACS+ users generate accounting records against the original TACACS+ login name.
- All Linux and NVUE commands result in an accounting record, including login commands and sub-processes of other commands. This can generate a lot of accounting records.
{{%/notice%}}

By default, Cumulus Linux sends accounting records to all servers. You can change this setting to send accounting records to the server that is first to respond:

{{< tabs "TabID248 ">}}
{{< tab "NVUE Commands ">}}

```
cumulus@switch:~$ nv set system aaa tacacs accounting send-records first-response
cumulus@switch:~$ nv config apply
```

To reset to the default configuration (send accounting records to all servers), run the `nv set system aaa tacacs accounting send-records all` command.

{{< /tab >}}
{{< tab "Linux Commands ">}}

1. Edit the `/etc/audisp/audisp-tac_plus.conf` file and change the `acct_all` parameter to 0:

   ```
   cumulus@switch:~$ sudo nano /etc/audisp/audisp-tac_plus.conf
   ...
   acct_all=0
   ```

2. Restart `auditd`:

   ```
   cumulus@switch:~$ sudo systemctl restart auditd
   ```

To reset to the default configuration (send accounting records to all servers), change the value of `acct_all` to 1 (`acct_all=1`).

{{< /tab >}}
{{< /tabs >}}

To disable TACACS+ accounting:

{{< tabs "TabID306 ">}}
{{< tab "NVUE Commands ">}}

```
cumulus@switch:~$ nv set system aaa tacacs accounting enable off
cumulus@switch:~$ nv config apply
```

{{< /tab >}}
{{< tab "Linux Commands ">}}

1. Edit the `/etc/audisp/plugins.d/audisp-tacplus.conf` file and change the `active` parameter to `no`:

   ```
   cumulus@switch:~$ sudo nano /etc/audisp/plugins.d/audisp-tacplus.conf
   ...
   # default to enabling tacacs accounting; change to no to disable
   active = no
   ```

2. Restart `auditd`:

   ```
   cumulus@switch:~$ sudo systemctl restart auditd
   ```

{{< /tab >}}
{{< /tabs >}}

## Local Fallback Authentication

If a site wants to allow local fallback authentication for a user when none of the TACACS servers are reachable, you can add a privileged user account as a local account on the switch.

{{%notice note%}}
NVUE does not provide commands to configure local fallback authentication.
{{%/notice%}}

To configure local fallback authentication:

1. Edit the `/etc/nsswitch.conf` file to remove the keyword `tacplus` from the line starting with `passwd`. (You need to add the keyword back in step 3.)

    The following example shows the `/etc/nsswitch.conf` file with no `tacplus` keyword in the line starting with `passwd`.

    ```
    cumulus@switch:~$ sudo vi /etc/nsswitch.conf
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

4. Restart the `nvued` service with the following command:

    ```
    cumulus@switch:~$ sudo systemctl restart nvued
    ```
<!-- vale off -->
## TACACS+ Per-command Authorization

TACACS+ per-command authorization lets you configure the commands that TACACS+ users at different privilege levels can run.

{{%notice note%}}
To reach the TACACS+ server through the default VRF, you must specify the egress interface you use in the default VRF. Either run the NVUE `nv set system aaa tacacs vrf <interface>` command (for example, `nv set system aaa tacacs vrf swp51`) or set the `vrf=<interface>` option in the `/etc/tacplus_servers` file (for example, `vrf=swp51`).
{{%/notice%}}

<!-- vale on -->

The following command allows TACACS+ users at privilege level 0 to run the `nv` and `ip` commands (if authorized by the TACACS+ server):

{{< tabs "TabID392 ">}}
{{< tab "NVUE Commands ">}}

```
cumulus@switch:~$ nv set system aaa tacacs authorization 0 command ip 
cumulus@switch:~$ nv set system aaa tacacs authorization 0 command nv
cumulus@switch:~$ nv config apply
```

To show the per-command authorization settings, run the `nv show system aaa tacacs authorization` command:

```
cumulus@switch:~$ nv show system aaa tacacs authorization
Privilege Level  role          command
---------------  ------------  -------
0                nvue-monitor  ip     
                               nv  
```

{{< /tab >}}
{{< tab "Linux Commands ">}}

```
tacuser0@switch:~$ sudo tacplus-restrict -i -u tacacs0 -a ip nv
```

The `tacplus-auth` command handles authorization for each command. To make this an enforced authorization, change the TACACS+ log in to use a restricted shell, with a very limited executable search path. Otherwise, the user can bypass the authorization. The `tacplus-restrict` utility simplifies setting up the restricted environment.

The following table provides the `tacplus-restrict` command options:

| Option | Description |
|------- |------------ |
| `-i` | Initializes the environment. You only need to issue this option one time per username. |
| `-a` | You can invoke the utility with the `-a` option as often as you like. For each command in the `-a` list, the utility creates a symbolic link from `tacplus-auth` to the relative portion of the command name in the local bin subdirectory. You also need to enable these commands on the TACACS+ server (refer to your TACACS+ server documentation). It is common for the server to allow some options to a command, but not others. |
| `-f` | Re-initializes the environment. If you need to restart, run the `-f` option with `-i` to force re-initialization; otherwise, the utility ignores repeated use of `-i`.<br>During initialization:<br>- The user shell changes to `/bin/rbash`.<br>- The utility saves any existing dot files. |

After running this command, examine the `tacacs0` directory::

```
cumulus@switch:~$ sudo ls -lR ~tacacs0
total 12
lrwxrwxrwx 1 root root 22 Nov 21 22:07 ip -> /usr/sbin/tacplus-auth
lrwxrwxrwx 1 root root 22 Nov 21 22:07 nv -> /usr/sbin/tacplus-auth
```

Except for shell built-ins, privilege level 0 TACACS users can only run the `ip` and `nv` commands.

If you add commands with the `-a` option by mistake, you can remove them. The example below removes the `nv` command:

```
cumulus@switch:~$ sudo rm ~tacacs0/bin/nv
```

To remove all commands:

```
cumulus@switch:~$ sudo rm ~tacacs0/bin/*
```

{{< /tab >}}
{{< /tabs >}}

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

### Show TACACS+ Configuration

Run the following commands to show TACACS+ configuration:

- To show all TACACS+ configuration (NVUE hides server secret keys), run the `nv show aaa tacacs` command.
- To show TACACS+ authentication configuration , run the `nv show system aaa tacacs authentication` command.
- To show TACACS+ accounting configuration , run the `nv show system aaa tacacs accounting` command.
- To show TACACS+ server configuration, run the `nv show system aaa tacacs server` command.
- To show TACACS+ server priority configuration, run the `nv show system aaa tacacs server <priority-id>` command.
- To show the list of users excluded from TACACS+ server authentication, run the `nv show system aaa tacacs exclude-user` command.

The following example command shows all TACACS+ configuration:

```
cumulus@switch:~$ nv show system aaa tacacs
                    applied
------------------  -------
enable              off    
debug-level         0      
timeout             5      
vrf                 mgmt   
accounting                 
  enable            off    
authentication             
  mode              pap    
  per-user-homedir  off    
[server]            5      
[server]            10 
```

The following command shows the list of users excluded from TACACS+ server authentication:

```
cumulus@switch:~$ nv show system aaa tacacs exclude-user
          applied
--------  -------
username  USER1  
```

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

If TACACS+ is not working correctly, you can use debugging. Add the `debug=1` parameter to the `/etc/tacplus_servers` and `/etc/tacplus_nss.conf` files; see the Linux Commands under {{<link url="#optional-tacacs-configuration" text="Optional TACACS+ Configuration">}} above. You can also add `debug=1` to individual `pam_tacplus` lines in `/etc/pam.d/common*`.

All log messages are in `/var/log/syslog`.

### Incorrect Shared Key

The TACACS client on the switch and the TACACS server must have the same shared secret key. If this key is incorrect, the following message prints to `syslog`:

```
2017-09-05T19:57:00.356520+00:00 leaf01 sshd[3176]: nss_tacplus: TACACS+ server 192.168.0.254:49 read failed with protocol error (incorrect shared secret?) user cumulus
```
<!-- vale off -->
### Debug Issues with Per-command Authorization
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

### TACACS+ Package Descriptions

Cumulus Linux uses the following packages for TACACS.

| <div style="width:280px">Package | Description|
|--------|---------|
| `audisp-tacplus` | Uses auditing data from `auditd` to send accounting records to the TACACS+ server and starts as part of `auditd`. |
| `libtac2` | Provides basic TACACS+ server utility and communication routines. |
| `libnss-tacplus` | Provides an interface between `libc` username lookups, the mapping functions, and the TACACS+ server. |
| `tacplus-auth` | Includes the `tacplus-restrict` setup utility, which enables you to perform per-command TACACS+ authorization. Per-command authorization is not the default. |
| `libpam-tacplus` | Provides a modified version of the standard Debian package. |
| `libtacplus-map1` | Provides mapping between local and TACACS+ users on the server. The package:</br>- Sets the immutable `sessionid` and auditing UID to ensure that you can track the original user through multiple processes and privilege changes.</br>- Sets the auditing `loginuid` as immutable.</br>- Creates and maintains a status database in `/run/tacacs_client_map` to manage and lookup mappings. |
| `libsimple-tacacct1` | Provides an interface for programs to send accounting records to the TACACS+ server. `audisp-tacplus` uses this package. |
| `libtac2-bin` | Provides the `tacc` testing program and TACACS+ man page. |

### TACACS+ Client Configuration Files

The following table describes the TACACS+ client configuration files that Cumulus Linux uses.

| <div style="width:250px">Filename | Description |
|----------|-------------|
| `/etc/tacplus_servers` | The primary file that requires configuration after installation. All packages with `include=/etc/tacplus_servers` parameters use this file. Typically, this file contains the shared secrets; make sure that the Linux file mode is 600. |
| `/etc/nsswitch.conf` | When the `libnss_tacplus` package installs, this file configures tacplus lookups through `libnss_tacplus`. If you replace this file by automation, you need to add tacplus as the first lookup method for the *passwd* database line. |
| `/etc/tacplus_nss.conf` |Sets the basic parameters for `libnss_tacplus`. The file includes a debug variable for debugging NSS lookups separately from other client packages. |
| `/usr/share/pam-configs/tacplus` | The configuration file for `pam-auth-update` to generate the files in the next row. The file uses these configurations at `login`, by `su`, and by `ssh`. |
| `/etc/pam.d/common-*` | The `/etc/pam.d/common-*` files update for `tacplus` authentication. The files update with `pam-auth-update` when you install or remove `libpam-tacplus`. |
| `/etc/sudoers.d/tacplus` | Allows TACACS+ privilege level 15 users to run commands with `sudo`. The file includes an example (commented out) of how to enable privilege level 15 TACACS users to use `sudo` without a password and provides an example of how to enable all TACACS users to run specific commands with sudo. Only edit this file with the `visudo -f /etc/sudoers.d/tacplus` command. |
| `/etc/audisp/plugins.d/audisp-tacplus.conf` | The `audisp` plugin configuration file. You do not need to modify this file. |
| `/etc/audisp/audisp-tac_plus.conf` | The TACACS+ server configuration file for accounting. You do not need to modify this file. You can use this configuration file when you only want to debug TACACS+ accounting issues, not all TACACS+ users. |
| `/etc/audit/rules.d/audisp-tacplus.rules` | The `auditd` rules for TACACS+ accounting. The `augenrules` command uses all rule files to generate the rules file.
| `/etc/audit/audit.rules`|The audit rules file that generate when you install `auditd`. |

## Considerations

<!--### TACACS+ Client Is only Supported through the Management Interface

The TACACS+ client is only supported through the management interface on the switch: eth0, eth1, or the VRF management interface. The TACACS+ client is not supported through bonds, switch virtual interfaces (SVIs), or switch port interfaces (swp).-->

### Multiple TACACS+ Users

If two or more TACACS+ users log in simultaneously with the same privilege level, while the accounting records are correct, a lookup on either name matches both users, while a UID lookup only returns the user that logs in first.

As a result, any processes that either user runs apply to both and all files either user creates apply to the first name matched. This is similar to adding two local users to the password file with the same UID and GID and is an inherent limitation of using the UID for the base user from the password file.

{{%notice note%}}
The current algorithm returns the first name matching the UID from the mapping file; either the first or the second user that logs in.
{{%/notice%}}

To work around this issue, you can use the switch audit log or the TACACS server accounting logs to determine which processes and files each user creates.

- For commands that do not execute other commands (for example, changes to configurations in an editor or actions with tools like `clagctl` and vtysh), there is no additional accounting.
- Per-command authorization is at the most basic level (Cumulus Linux uses standard Linux user permissions for the local TACACS users and only privilege level 15 users can run `sudo` commands by default).

The Linux `auditd` system does not always generate audit events for processes when terminated with a signal (with the `kill` system call or internal errors such as SIGSEGV). As a result, processes that exit on a signal that you do not handle, generate a STOP accounting record.

### Issues with the deluser Command

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

### TACACS+ and PAM

PAM modules and an updated version of the `libpam-tacplus` package configure authentication initially. When you install the package, the `pam-auth-update` command updates the PAM configuration in `/etc/pam.d`. If you make changes to your PAM configuration, you need to integrate these changes. If you also use LDAP with the `libpam-ldap` package, you need to edit the PAM configuration with the LDAP and TACACS ordering you prefer. The `libpam-tacplus` package ignore rules and the values in `success=2` require adjustments to ignore LDAP rules.

The TACACS+ privilege attribute `priv_lvl` determines the privilege level for the user that the TACACS+ server returns during the user authorization exchange. The client accepts the attribute in either the mandatory or optional forms and also accepts `priv-lvl` as the attribute name. The attribute value must be a numeric string in the range 0 to 15, with 15 the most privileged level.

{{%notice note%}}
By default, TACACS+ users at privilege levels other than 15 cannot run `sudo` commands and can only run commands with standard Linux user permissions.
{{%/notice%}}

{{%notice warning%}}
You can edit the `/etc/pam.d/common-*` files manually. However, if you run `pam-auth-update` again after making the changes, the update fails. Only configure `/usr/share/pam-configs/tacplus`, then run `pam-auth-update`.
{{%/notice%}}

### NSS Plugin

With `pam_tacplus`, TACACS+ authenticated users can log in without a local account on the system using the NSS plugin that comes with the `tacplus_nss` package. The plugin uses the mapped `tacplus` information if the user is not in the local password file, provides the `getpwnam()` and `getpwuid()`entry points, and uses the TACACS+ authentication functions.

The plugin asks the TACACS+ server if it knows the user, and then for relevant attributes to determine the privilege level of the user. When you install the `libnss_tacplus` package, `nsswitch.conf` changes to set `tacplus` as the first lookup method for `passwd`. If you change the order, lookups return the local accounts, such as `tacacs0`

If TACACS+ server does not find the user, it uses the `libtacplus.so` exported functions to do a mapped lookup. The privilege level appends to `tacacs` and the lookup searches for the name in the local password file. For example, privilege level 15 searches for the tacacs15 user. If the TACACS+ server finds the user, it adds information for the user in the password structure.

If the TACACS+ server does not find the user, it decrements the privilege level and checks again until it reaches privilege level 0 (user `tacacs0`). This allows you to use only the two local users `tacacs0` and `tacacs15`, for minimal configuration.

### TACACS+ Client Sequencing

Cumulus Linux requires the following information at the beginning of the AAA sequence:

- Whether the user is a valid TACACS+ user
- The user privilege level

For non-local users (users not in the local password file) you need to send a TACACS+ authorization request as the first communication with the TACACS+ server, before authentication and before the user logging in requests a password.

You need to configure certain TACACS+ servers to allow authorization requests before authentication. Contact your TACACS+ server vendor for information.

### Multiple Servers with Different User Accounts

If you configure multiple TACACS+ servers that have different user accounts:
- TACACS+ *authentication* allows for fall through; if the first reachable server does not authenticate the user, the client tries the second server, and so on.
- TACACS *authorization* does not fall through. If the first reachable server returns an *unauthorized* result, the command is unauthorized and the client does not try the next server.
