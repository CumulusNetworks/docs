---
title: RADIUS AAA
author: NVIDIA
weight: 190
toc: 4
---
Cumulus Linux provides add-on packages to enable <span class="a-tooltip">[RADIUS](## "Remote Authentication Dial-In User Service")</span> users to log into the switch transparently with minimal configuration. There is no need to create accounts or directories on the switch. Authentication uses PAM and includes login, `ssh`, `sudo` and `su`.

## Install the RADIUS Packages

{{%notice note%}}
NVUE automatically installs the RADIUS AAA packages; you do **not** have to install the packages if you use NVUE commands to configure RADIUS AAA.
{{%/notice%}}

If you use Linux commands to configure RADIUS AAA, you must install the RADIUS `libnss-mapuser` and `libpam-radius-auth` packages before you start configuration. The packages are in the `cumulus-local-apt-archive` repository, which is {{<link url="Adding-and-Updating-Packages#add-packages-from-the-cumulus-linux-local-archive" text="embedded">}} in the Cumulus Linux image. You can install the packages even when the switch is not connected to the internet.

To install the RADIUS packages:

```
cumulus@switch:~$ sudo apt-get update
cumulus@switch:~$ sudo apt-get install libnss-mapuser libpam-radius-auth
```

{{%notice note%}}
When installing the `libpam-radius-auth` package, Cumulus Linux prompts you to either overwrite the local files with those from the package or to keep the local files. The default option is to keep the local files, which does not allow RADIUS to operate as expected. To install the `libpam-radius-auth` package and overwrite the local files, run the following command:

```
cumulus@switch:~$ sudo apt-get -y -o Dpkg::Options::=--force-confnew install libnss-mapuser libpam-radius-auth
```

If you install the `libpam-radius-auth` package without overwriting the local files, you must either remove and reinstall the package with the `sudo apt-get -y -o Dpkg::Options::=--force-confnew install libnss-mapuser libpam-radius-auth` command, or overwrite the local files without removing or reinstalling the package with the `sudo pam-auth-update –force` command.
{{%/notice%}}

After installation completes, either reboot the switch or run the `sudo systemctl restart nvued` command.

The `nvshow` group includes the `radius_user` account, and the `nvset` and `nvapply` groups. The `sudo` groups include the `radius_priv_user` account. This enables all RADIUS logins to run NVUE `nv show` commands and all privileged RADIUS users to also run `nv set`, `nv unset`, and `nv apply` commands, and to use `sudo`.

## Required RADIUS Client Configuration

After you install the required RADIUS packages, configure the following required settings on the switch (the RADIUS client):
- Set the IP address or hostname of at least one RADIUS server. You can specify a port for the server (optional). The default port number is 1812.
- Set the secret key shared between the RADIUS server and client. If you include special characters in the key (such as $), you must enclose the key in single quotes (').
- If you use NVUE commands to configure RADIUS, you must also:
  - Set the priority at which Cumulus Linux contacts a RADIUS server for load balancing. You can set a value between 1 and 100. The lower value is the higher priority.
  - Set the priority for the authentication order for local and RADIUS users. You can set a value between 1 and 100. The lower value is the higher priority.

{{%notice note%}}
After you configure any RADIUS settings with NVUE and you run `nv config apply`, you must restart the NVUE service with the `sudo systemctl restart nvued.service` command.
{{%/notice%}}

{{< tabs "TabID41 ">}}
{{< tab "NVUE Commands ">}}

The following example commands set:
- The IP address of the RADIUS server to 192.168.0.254 and the port to 42.
- The secret to `'myradius$key'`.
- The priority at which Cumulus Linux contacts the RADIUS server to 10.
- The authentication order to 10 so that RADIUS authentication has priority over local.

```
cumulus@switch:~$ nv set system aaa radius server 192.168.0.254 port 42
cumulus@switch:~$ nv set system aaa radius server 192.168.0.254 secret 'myradius$key'
cumulus@switch:~$ nv set system aaa radius server 192.168.0.254 priority 10
cumulus@switch:~$ nv set system aaa authentication-order 10 radius
cumulus@switch:~$ nv set system aaa authentication-order 20 local
cumulus@switch:~$ nv config apply
```

{{< /tab >}}
{{< tab "Linux Commands ">}}

Edit the `/etc/pam_radius_auth.conf` file to specify the hostname or IP address of at least one RADIUS server, and the shared secret you want to use to authenticate and encrypt communication with each server.

```
...
mapped_priv_user   radius_priv_user

# server[:port]    shared_secret   timeout (secs)  src_ip
192.168.0.254:42   myradius$key       3
...
```

You must be able to resolve the hostname of the switch to an IP address. If you cannot find the hostname in DNS, you can add the hostname to the `/etc/hosts` file manually. Be aware that adding the hostname to the `/etc/hosts` file manually can cause problems because DHCP assigns the IP address, which can change at any time.

Cumulus Linux verifies multiple server configuration lines in the order listed. Other than memory, there is no limit to the number of RADIUS servers you can use.

The server port number is optional. The system looks up the port in the `/etc/services` file. However, you can override the ports in the `/etc/pam_radius_auth.conf` file.

{{< /tab >}}
{{< /tabs >}}

## Optional RADIUS Configuration

You can configure the following global RADIUS settings and server specific settings.

{{< tabs "TabID34 ">}}
{{< tab "NVUE Commands ">}}

| Setting | Description |
| ------ | ----------- |
| `vrf` | The global VRF you want to use to communicate with a RADIUS server. This is typically the management VRF (`mgmt`), which is the default VRF on the switch. If you use multiple RADIUS servers, you can specify a different VRF for each server. |
| `privilege-level` | The minimum privilege level that determines if users can configure the switch with NVUE commands and sudo, or have read-only rights. The default privilege level is 15, which provides full administrator access. This is a global option only; you cannot set the minimum privilege level for specific RADIUS servers.|
| `retransmit` | The maximum number of retransmission attempts allowed for requests when a RADIUS authentication request times out. This is a global option only; you cannot set the number of retransmission attempts for specific RADIUS servers.|
| `timeout` | The timeout value when a server is slow or latencies are high. You can set a value between 1 and 60. The default timeout is 3 seconds. If you configure multiple RADIUS servers, you can set a global timeout for all servers. |
| `source-ipv4`</br>`source-ipv6`| A specific interface to reach all RADIUS servers. To configure the source IP address for a specific RADIUS server, use the `source-ip` option.|
| `debug` | The debug option for troubleshooting. The debugging messages write to `/var/log/syslog`. When the RADIUS client is working correctly, you can disable the debug option. You enable the debug option globally for all the servers.|
| `require-message-authenticator` | Requires authentication packets to have the Message-Authenticator attribute; the switch discards as Access-Reject all packets that do not have the Message-Authenticator attribute.|

The following example configures global RADIUS settings:

```
cumulus@switch:~$ nv set system aaa radius vrf mgmt
cumulus@switch:~$ nv set system aaa radius privilege-level 10
cumulus@switch:~$ nv set system aaa radius retransmit 8
cumulus@switch:~$ nv set system aaa radius timeout 10
cumulus@switch:~$ nv set system aaa radius source-ipv4 192.168.1.10
cumulus@switch:~$ nv set system aaa radius debug enable
cumulus@switch:~$ nv set system aaa radius require-message-authenticator enabled 
cumulus@switch:~$ nv config apply
```

The following example configures RADIUS settings for a specific RADIUS server:

```
cumulus@switch:~$ nv set system aaa radius server 192.168.0.254 source-ip 192.168.1.10
cumulus@switch:~$ nv set system aaa radius server 192.168.0.254 vrf RED
cumulus@switch:~$ nv set system aaa radius server 192.168.0.254 timeout 10
cumulus@switch:~$ nv config apply
```

{{< /tab >}}
{{< tab "Linux Commands ">}}

| Setting | Description |
| ------ | ----------- |
| `vrf` | The VRF you want to use to communicate with the RADIUS server. This is typically the management VRF (`mgmt`), which is the default VRF on the switch. If you use multiple RADIUS servers, you can specify a different VRF for each server. |
| `privilege-level` | Determines the privilege level for the user on the switch.|
| `timeout` | The timeout value when a server is slow or latencies are high. You can set a value between 1 and 60. The default timeout is 3 seconds. If you configure multiple RADIUS servers, you can set a global timeout for all servers. |
| `src_ip`| A specific IPv4 or IPv6 interface to reach the RADIUS server. If you configure multiple RADIUS servers, you can configure a specific interface to reach all RADIUS servers. |
| `debug` | The debug option for troubleshooting. The debugging messages write to `/var/log/syslog`. When the RADIUS client is working correctly, you can disable the debug option. If you configure multiple RADIUS servers, you can enable the debug option globally for all the servers.|

Edit the `/etc/pam_radius_auth.conf` file.
<!-- vale off -->
```
...
# Set the minimum privilege level in VSA attribute shell:privilege-level=VALUE
# default is 15, range is 0-15.
privilege-level 10
#
#  Uncomment to enable debugging, can be used instead of altering pam files
debug
#
# Account for privileged radius user mapping.  If you change it here,  you need
# to change /etc/nss_mapuser.conf as well
mapped_priv_user radius_priv_user

# server[:port]        shared_secret       timeout (secs)    vrf-name    src_ip
192.168.0.254:42       myradius$key        10                mgmt        192.168.1.10        

```
<!-- vale on -->
{{< /tab >}}
{{< /tabs >}}

{{%notice note%}}
The value of the VSA (Vendor Specific Attribute) `shell:priv-lvl` determines the privilege level for the user on the switch. If the attribute does not return, the user does not have privileges. The following shows an example using the `freeradius` server for a fully privileged user.

```
Service-Type = Administrative-User,
Cisco-AVPair = "shell:roles=network-administrator",
Cisco-AVPair += "shell:priv-lvl=15"
```

The VSA vendor name (Cisco-AVPair in the example above) can have any content. The RADIUS client only checks for the string `shell:priv-lvl`.
{{%/notice%}}

## Enable Login without Local Accounts

{{%notice note%}}
NVUE does not provide commands to enable login without local accounts.
{{%/notice%}}

LDAP is not commonly used with switches and adding accounts locally is cumbersome, Cumulus Linux includes a mapping capability with the `libnss-mapuser` package.

Mapping uses two NSS (Name Service Switch) plugins, one for account name, and one for UID lookup. The installation process configures these accounts automatically in the `/etc/nsswitch.conf` file and removes them when you delete the package. See the `nss_mapuser (8)` man page for the full description of this plugin.
<!-- vale off -->
A username is mapped at login to a fixed account specified in the configuration file, with the fields of the fixed account used as a template for the user that is logging in.
<!-- vale on -->
For example, if you look up the name `dave` and the fixed account in the configuration file is `radius\_user`, and that entry in `/etc/passwd` is:

```
radius_user:x:1017:1002:radius user:/home/radius_user:/bin/bash
```

then the matching line that returns when you run `getent passwd dave` is:

```
cumulus@switch:~$ getent passwd dave
dave:x:1017:1002:dave mapped user:/home/dave:/bin/bash
```

The login process creates the home directory `/home/dave` if it does not already exist and populates it with the standard skeleton files by the `mkhomedir_helper` command.

The configuration file `/etc/nss_mapuser.conf` configures the plugins. The file includes the mapped account name, which is `radius_user` by default. You can change the mapped account name by editing the file. The `nss_mapuser (5)` man page describes the configuration file.

A flat file mapping derives from the session number assigned during login, which persists across `su` and `sudo`. Cumulus Linux removes the mapping at logout.

## Local Fallback Authentication

If a site wants to allow local fallback authentication for a user when none of the RADIUS servers are reachable, you can add a privileged user account as a local account on the switch.

To configure an account for local fallback authentication:

1. Add a local user account with the desired role and permissions as described in {{<link url="User-Accounts#add-a-new-user-account" text="Add a New User Account">}}.

2. To ensure the local user account password authenticates the user only when none of the RADIUS servers are reachable, configure the {{<link url="RADIUS-AAA#required-radius-client-configuration" text="authentication order">}} so that RADIUS has a preferred priority over local authentication:

{{< tabs "TabID211 ">}}
{{< tab "NVUE Commands ">}}
```
cumulus@switch:~$ nv set system aaa authentication-order 10 radius
cumulus@switch:~$ nv set system aaa authentication-order 20 local
```

{{< /tab >}}
{{< tab "Linux Commands ">}}

Configure the `passwd` line in the `/etc/nsswitch.conf` file to place `files` after `mapuid` in the authentication order:

```
cumulus@switch:~$ vi /etc/nsswitch.conf 

# /etc/nsswitch.conf
#
# Example configuration of GNU Name Service Switch functionality.
# If you have the `glibc-doc-reference' and `info' packages installed, try:
# `info libc "Name Service Switch"' for information about this file.

passwd:         mapuid files mapname
group:          mapname files
shadow:         files
gshadow:        files

hosts:          files dns
networks:       files

protocols:      db files
services:       db files
ethers:         db files
rpc:            db files

netgroup:       nis
```

{{< /tab >}}
{{< /tabs >}}

{{%notice note%}}
- If you configure the authentication order to prefer local authentication before RADIUS, login falls back to RADIUS only if the user is not configured locally.
- If you configure the same account on the switch locally and on your RADIUS server, you must configure the local user account before attempting authentication with RADIUS for the user; otherwise, local account creation fails.
{{%/notice%}}

## RADIUS User Command Accounting

RADIUS user command accounting lets you log every command that a RADIUS user runs and send the commands to RADIUS servers for auditing. Audit logs are a requirement for compliance standards, such as PCI and HIPPA.

You must configure the RADIUS servers to accept packets from clients and have a dictionary entry for `NV-Command-String`.

{{%notice note%}}
When you enable or change accounting settings, NVUE disconnects currently logged in RADIUS users.
{{%/notice%}}

### Enable RADIUS Accounting

To enable RADIUS user command accounting:

```
cumulus@switch:~$ nv set system aaa radius accounting state enabled
cumulus@switch:~$ nv config apply
```

To disable RADIUS user command accounting, run the `nv set system aaa radius accounting state disabled` command.

The `/var/log/radius-cmd-acct.log` file contains the local copy of the logs, which match the logs that the server receives.

If you do not receive any accounting packets, check the `/var/log/radius-send-cmd.log` file.

To see if RADIUS user command accounting is `on`, run the `nv show system aaa radius` command.

### Send Accounting Records to First Response

By default, Cumulus Linux sends accounting records to all servers. You can change this setting to send accounting records to the server that is first to respond. If the first available server does not respond, Cumulus Linux continues trying down the list of servers (by priority) until one is reachable. If none of the servers are reachable, there is a 30 second timeout, after which Cumulus Linux retries the servers. After 10 failed retries, the switch drops the packet.

```
cumulus@switch:~$ nv set system aaa radius accounting send-records first-response
cumulus@switch:~$ nv config apply
```

To reset to the default configuration (send accounting records to all servers), run the `nv set system aaa radius accounting send-records all` command. If none of the servers respond, there is a 30 second timeout, after which Cumulus Linux retries the servers. After 10 failed retries, the switch drops the packet.

## Verify RADIUS Client Configuration

To verify the RADIUS client configuration, log in as a non-privileged user and run the `nv set interface` command.

In this example, the `ops` user is not a privileged RADIUS user so the `ops` user cannot add an interface.

```
ops@leaf01:~$ nv set interface swp1
ERROR: User ops does not have permission to make networking changes.
```

In this example, the `admin` user is a privileged RADIUS user (with privilege level 15) so is able to add interface swp1.

```
admin@leaf01:~$ nv set interface swp1
admin@leaf01:~$ nv apply
```

## Show RADIUS Configuration

To show global RADIUS configuration, run the `nv show system aaa radius` command:

```
cumulus@switch:~$ nv show system aaa radius
                 operational    applied        
---------------  -------------  ------------- 
vrf              mgmt           mgmt          
debug            disabled       disabled      
privilege-level                 15            
retransmit       0              0             
port                            1812          
timeout                         3             
accounting       enabled        enabled       
[server]         192.168.0.254  192.168.0.254 
```

To show all RADIUS configured servers, run the `nv show system aaa radius server` command:

```
cumulus@switch:~$ nv show system aaa radius server
Hostname       Port  Priority  Password  source-ip     Timeout
-------------  ----  --------  --------  ------------  -------
192.168.0.254  42    1         *         192.168.1.10  10
```

To show configuration for a specific RADIUS server, run the `nv show system aaa radius server <server>` command:

```
cumulus@switch:~$ nv show system aaa radius server 192.168.0.254
           operational   applied     
---------  ------------  ------------
port       42            42          
timeout    10            10          
secret     *             *           
priority   1             10          
```
<!-- NOT IN 5.14 - TO ADD FOR 5.15 MAYBE
## Show and Clear RADIUS Counters

To show statistics for a specific RADIUS server, such as the number of authorization requests, accepted, rejected, timed out and retried access requests, and authorization connection errors and bad responses, run the `nv show system aaa radius server <server> counters` command:

```
cumulus@switch:~$ nv show system aaa radius server 192.168.0.254 counters
                         operational  applied
-----------------------  -----------  -------
auth-requests            28                  
access-accepts           0                   
access-rejects           0                   
timeout-access-requests  28                  
retried-auth-requests    0                   
auth-connection-errors   28                  
auth-bad-responses       0            90
```

To clear all the counters for a RADIUS server, run the `nv action clear system aaa radius counters` command:

```
cumulus@switch:~$ nv action clear system aaa radius counters
RADIUS counters cleared.
Action succeeded
```
-->
## Remove RADIUS Client Packages

Remove the RADIUS packages with the following command:

```
cumulus@switch:~$ sudo apt-get remove libnss-mapuser libpam-radius-auth
```

When you remove the packages, Cumulus Linux deletes the plugins from the `/etc/nsswitch.conf` file and from the PAM files.

To remove all configuration files for these packages, run:

```
cumulus@switch:~$ sudo apt-get purge libnss-mapuser libpam-radius-auth
```

{{%notice note%}}
Cumulus Linux does not remove the RADIUS fixed account from the `/etc/passwd` or `/etc/group` file or the home directories. They remain in case of modifications to the account or files in the home directories.
{{%/notice%}}

To remove the home directories of the RADIUS users, obtain the list by running the following command:

```
cumulus@switch:~$ sudo ls -l /home | grep radius
```

For all users listed, except the `radius_user`, run the following command to remove the home directories:

```
cumulus@switch:~$ sudo deluser --remove-home USERNAME
```

`USERNAME` is the account name (the home directory relative portion). This command gives the following warning because the user is not listed in the `/etc/passwd` file.

```
userdel: cannot remove entry 'USERNAME' from /etc/passwd
/usr/sbin/deluser: `/usr/sbin/userdel USERNAME' returned error code 1. Exiting.
```

After you remove all the RADIUS users, run the command to remove the fixed account. If there are changes to the account in the `/etc/nss_mapuser.conf` file, use that account name instead of `radius_user`.

```
cumulus@switch:~$ sudo deluser --remove-home radius_user
cumulus@switch:~$ sudo deluser --remove-home radius_priv_user
cumulus@switch:~$ sudo delgroup radius_users
```

## Considerations

- If two or more RADIUS users log in simultaneously, a UID lookup only returns the user that logs in first. Any process that either user runs applies to both, and all files that either user creates apply to the first name matched. This process is similar to adding two local users to the password file with the same UID and GID, and is an inherent limitation of using the UID for the fixed user from the password file. The current algorithm returns the first name matching the UID from the mapping file, which is either the first or second user that logs in.
- When you install both the TACACS+ and the RADIUS AAA client, Cumulus Linux does not attempt the RADIUS login. As a workaround, do not install both the TACACS+ and the RADIUS AAA client on the same switch.
- When the RADIUS server is reachable outside of the management VRF, such as the default VRF, you might see the following error message when you try to run `sudo`:

  ```
  2008-10-31T07:06:36.191359+00:00 SW01 sudo: pam_radius_auth(sudo:auth): Bind for server 10.1.1.25 failed: Cannot assign requested address
  2008-10-31T07:06:36.192307+00:00 sw01 sudo: pam_radius_auth(sudo:auth): No valid server found in configuration file /etc/pam_radius_auth.conf
  ```

   The error occurs because `sudo` tries to authenticate to the RADIUS server through the management VRF. Before you run `sudo`, you must set the shell to the correct VRF:

   ```
   cumulus@switch:~$ vrf exec default bash
   cumulus@switch:~$ sudo 
   ```
