---
title: User Accounts
author: NVIDIA
weight: 150
toc: 4
---
By default, Cumulus Linux has two user accounts: *cumulus* and *root*.

The *cumulus* account:

- Uses the default password `cumulus`. You must change the default password when you log into Cumulus Linux for the first time.
- Is a user account in the *sudo* group with sudo privileges.
- Can log in to the system through all the usual channels, such as console and {{<link url="SSH-for-Remote-Access" text="SSH">}}.
- Includes permissions to run NVUE `nv show`, `nv set`, `nv unset`, and `nv apply` commands.

The *root* account:

- Has the default password disabled by default and prevents you from using SSH, telnet, FTP, and so on, to log in to the switch.
- Has the standard Linux root user access to everything on the switch.

## Add a New User Account

You can add additional user accounts as needed.
- You control local user account access to NVUE commands by changing the group membership (role) for a user. Like the *cumulus* account, these accounts must be in the `sudo` group or include the NVUE `system-admin` role to {{<link url="Using-sudo-to-Delegate-Privileges" text="execute privileged commands">}}.
- You can set a plain text password or a hashed password for the local user account. To access the switch without a password, you need to {{<link url="Single-User-Mode-Password-Recovery" text="boot into single user mode">}}.
- You can provide a full name for the local user account (optional).

### Default Roles

Cumulus Linux provides the following default roles:

{{< tabs "TabID32 ">}}
{{< tab "NVUE ">}}

| <div style="width:200px">Role | Permissions |
|--------- |---------- |
| `system-admin` | Allows the user to use `sudo` to run commands as the privileged user, run `nv show` commands, run `nv set` and `nv unset` commands to stage configuration changes, and run `nv apply` commands to apply configuration changes. |
| `nvue-admin` | Allows the user to run `nv show` commands, run `nv set` and `nv unset` commands to stage configuration changes, and run `nv apply` commands to apply configuration changes. |
| `nvue-monitor` | Allows the user to run `nv show` commands only.|

{{< /tab >}}
{{< tab "Linux ">}}

| <div style="width:200px">Role | Permissions |
|--------- |---------- |
| `sudo` | Allows the user to use `sudo` to run commands as the privileged user. |
| `nvshow` | Allows the user to run `nv show` commands only. |
| `nvset`  | Allows the user to run `nv show` commands, and run `nv set` and `nv unset` commands to stage configuration changes. |
| `nvapply` | Allows the user to run `nv show` commands, run `nv set` and `nv unset` commands to stage configuration changes, and run `nv apply` commands to apply configuration changes. |

{{< /tab >}}
{{< /tabs >}}

To add a new user account and assign the user a default role:

{{< tabs "TabID58 ">}}
{{< tab "NVUE Commands ">}}

The following example:
- Creates a new user account called `admin2` and sets the role to `system-admin`.
- Sets a plain text password. NVUE hashes the plain text password and stores the value as a hashed password. To set a hashed password, see {{<link url="#hashed-passwords" text="Hashed Passwords">}}, below.
- Adds the full name `FIRST LAST`. If the full name includes more than one name, either separate the names with a hyphen (`FIRST-LAST`) or enclose the full name in quotes (`"FIRST LAST"`).

```
cumulus@switch:~$ nv set system aaa user admin2 role system-admin
cumulus@switch:~$ nv set system aaa user admin2 password
Enter new password:
Confirm password:
cumulus@switch:~$ nv set system aaa user admin2 full-name "FIRST LAST"
cumulus@switch:~$ nv config apply
```

You can run the `nv set system aaa user <user> password <plain-text-password>` command to specify the plain text password inline. This command bypasses the `Enter new password` and `Confirm password` prompts but displays the plain text password as you type it.

{{%notice note%}}
If you are an NVUE-managed user, you can update your own password with the Linux `passwd` command.
{{%/notice%}}

To configure a <span class="a-tooltip">[SPIFFE](## "Secure Production Identity Framework for Everyone")</span> ID for the user account instead of a password, run the `nv set system aaa user cumulus spiffe-id <id>` command.

{{< /tab >}}
{{< tab "Linux Commands ">}}

The following example:
- Creates a new user account called `admin2`, creates a home directory for the user, and adds the full name `First Last`.
- Securely sets the password for the user with `passwd`.
- Sets the group membership (role) to `sudo` and `nvapply` (permissions to use `sudo`, `nv show`, `nv set`, and `nv apply`).

```
cumulus@switch:~$ sudo useradd admin2 -m -c "First Last"
cumulus@switch:~$ sudo passwd admin2
Enter new UNIX password:
Retype new UNIX password:
passwd: password updated successfully
cumulus@switch:~$ sudo adduser admin2 sudo
cumulus@switch:~$ sudo adduser admin2 nvapply
```

{{%notice note%}}
- When you run Linux commands to add a new user, you must create a home directory for the user with the `-m` option. NVUE commands create a home directory automatically.
- If you run Linux commands to configure a user password with five or fewer characters, Cumulus Linux logs the message `BAD PASSWORD: The password is shorter than 6 characters`. If you disable password security, this is only a warning and the password is set. If you enable password security, the short password is not set.
{{%/notice%}}

{{< /tab >}}
{{< /tabs >}}

{{%notice note%}}
When you change the role for a user, Cumulus Linux terminates their session (including the SSH session) and they have to reauthenticate. For example, if you change the role for a user from `nvue-admin` to `nvue-monitor`, if the user tries to run `nv set` commands from an active session, their session disconnects and they have to reauthenticate.
{{%/notice%}}

{{%notice note%}}
Only the following user accounts can create, modify, and delete other `system-admin` accounts:
- NVUE-managed users with the `system-admin` role.
- The root user.
- Non NVUE-managed users that are in the `sudo` group.
{{%/notice%}}

You can also create custom roles and assign a custom role to a user. See {{<link url="Role-Based-Access-Control" text="Role-based Access Control">}}.

### Hashed Passwords

Instead of a plain text password, you can provide a hashed password for a local user.

You must specify the hashed password in Linux `crypt` format; the password must be a minimum of 15 to 20 characters long and must include special characters, digits, lowercase alphabetic letters, and more. Typically, the password format is set to `$id$salt$hashed`, where `$id` is the hashing algorithm. In GNU or Linux:
  - `$1$` is MD5
  - `$2a$` is Blowfish
  - `$2y$` is Blowfish
  - `$5$` is SHA-256
  - `$6$` is SHA-512
  
To generate a hashed password on the switch, you can either run a `python3` command or install and use the `mkpasswd` utility:

{{< tabs "TabID102 ">}}
{{< tab "python3 Command ">}}

Run the following command on the switch or Linux host. When prompted, enter the plain text password you want to hash:

```
cumulus@switch:~$ python3 -c "import crypt; import getpass; print(crypt.crypt(getpass.getpass(), salt=crypt.METHOD_SHA512))"                    
Password:                                                                                                                                                                 
$6$MIDE.sdxwxuAMGHd$XFXSpHV4NRJymUpeCKz.SYEMUfGGEtLbcqK0fBw3d96ZzegP3sw6ppl5Atx9xLS3UHLLTWS/BOwjkeBJJaRx10
```

{{< /tab >}}
{{< tab "mkpasswd Utility ">}}

1. Install the `mkpasswd` utility on the switch or Linux host:

  ```
  cumulus@switch:~$ sudo -E apt-get update
  cumulus@switch:~$ sudo -E apt-get install whois
  ```

2. To generate a hashed password for SHA-512, SHA256, or MD5 encryption, run the following command. When prompted, enter the plain text password you want to hash:

   SHA-512 encryption:

   ```
   cumulus@switch:~$ mkpasswd -m SHA-512
   Password:
   $6$bQcjKuWgKC0vdwT5$.ZlRgmS44geDH/HsCIttldsaxJ7Y/NidicXwR0FarwXq74uA/yJHxQXGHZwNviY/cG412i7Grzl6Wk8mStJwD0
   ```

   SHA256 encryption:

   ```                          
   cumulus@switch:~$ mkpasswd -m SHA-256
   Password:
   $5$SJsPU8bjl2F$.fzRpTGxwGw82RDdFPwhIermSSh6g2ZCYzPeNpeDrgC
   ```

   MD5 encryption:

   ```
   cumulus@switch:~$ mkpasswd -m MD5
   Password:
   $1$/ETjhZMJ$P73qhBZEYP20mKnRkhBol0
   ```

{{< /tab >}}
{{< /tabs >}}

To set the hashed password for the local user:

{{< tabs "TabID152 ">}}
{{< tab "NVUE Commands ">}}

Run the `nv set system aaa user <username> hashed-password <password>` command:

```
cumulus@switch:~$ nv set system aaa user admin2 hashed-password '$1$/ETjhZMJ$P73qhBZEYP20mKnRkhBol0'
cumulus@switch:~$ nv config apply
```

{{< /tab >}}
{{< tab "Linux Commands ">}}

```
cumulus@switch:~$ sudo useradd admin2 -c "First Last" -p '$1$/ETjhZMJ$P73qhBZEYP20mKnRkhBol0'
```

{{< /tab >}}
{{< /tabs >}}

{{%notice note%}}
Hashed password strings contain characters, such as `$`, that have a special meaning in the Linux shell; you must enclose the hashed password in single quotes (').
{{%/notice%}}

## Delete a User Account

To delete a user account:

{{< tabs "TabID104 ">}}
{{< tab "NVUE Commands ">}}

Run the `nv unset system aaa user <user>` command. The following example deletes the user account called `admin2`.

```
cumulus@switch:~$ nv unset system aaa user admin2
cumulus@switch:~$ nv config apply
```

{{< /tab >}}
{{< tab "Linux Commands ">}}

Run the `sudo userdel <user>` command. The following example deletes the user account called `admin2`.

```
cumulus@switch:~$ sudo userdel admin2
```

{{< /tab >}}
{{< /tabs >}}

## Disconnect User Account Active Terminals

To disconnect all active terminals for a user account, run the `nv action disconnect system aaa user <user-account>` command.

```
cumulus@switch:~$ nv action disconnect system aaa user admin3
```

## Show User Accounts

To show the user accounts configured on the system, run the NVUE `nv show system aaa` command or the linux `sudo cat /etc/passwd` command.

```
cumulus@switch:~$ nv show system aaa user
Username          Full-name                           Role     enable  Summary
----------------  ----------------------------------  -------  ------  -------
_apt                                                  Unknown  system         
_lldpd                                                Unknown  system         
backup            backup                              Unknown  system         
bin               bin                                 Unknown  system         
cumulus           cumulus,,,                          Unknown  on             
daemon            daemon                              Unknown  system         
dnsmasq           dnsmasq,,,                          Unknown  system         
frr               Frr routing suite,,,                Unknown  system         
games             games                               Unknown  system         
gnats             Gnats Bug-Reporting System (admin)  Unknown  system         
irc               ircd                                Unknown  system         
list              Mailing List Manager                Unknown  system         
lp                lp                                  Unknown  system         
mail              mail                                Unknown  system         
man               man                                 Unknown  system         
messagebus                                            Unknown  system         
news              news                                Unknown  system         
nobody            nobody                              Unknown  off            
ntp                                                   Unknown  system         
nvue              NVIDIA User Experience              Unknown  system         
proxy             proxy                               Unknown  system         
root              root                                Unknown  system         
snmp                                                  Unknown  system         
sshd                                                  Unknown  system         
sync              sync                                Unknown  system         
sys               sys                                 Unknown  system         
systemd-coredump  systemd Core Dumper                 Unknown  system         
systemd-network   systemd Network Management,,,       Unknown  system         
systemd-resolve   systemd Resolver,,,                 Unknown  system         
systemd-timesync  systemd Time Synchronization,,,     Unknown  system         
user1                                                 OSPF     on             
user2                                                 IFMgr    on             
uucp              uucp                                Unknown  system         
uuidd                                                 Unknown  system
```

To show information about a specific user account, run the NVUE `nv show system aaa user <user>` command:

```
cumulus@switch:~$ nv show system aaa user cumulus
                    operational  applied
------------------  -----------  -------
role                Unknown             
full-name           cumulus,,,          
hashed-password     *                   
ssh                                     
  [authorized-key]                      
state               enabled       enabled 
```

## Enable the root User

The root user does not have a password and cannot log into a switch using SSH. This default account behavior is consistent with Debian.

### Enable Console Access

To log into the switch using root from the console, you must set the password for the root account: 

```
cumulus@switch:~$ sudo passwd root
Enter new password:
...
```

### Enable SSH Access

To log into the switch using root with SSH, either:
- Install an SSH authorized key; refer to {{<link url="SSH-for-Remote-Access#install-an-authorized-ssh-key" text="Install an Authorized SSH Key">}}.
- Follow these steps to set a password and enable password authentication for root in `sshd`:
  
  1. Run the following command:
     ```
     cumulus@switch:~$ sudo passwd root 
     ```

  2. In the `/etc/ssh/sshd_config` file, change the `PermitRootLogin` setting from `without-password` to `yes`:

     ```
     cumulus@switch:~$ sudo nano /etc/ssh/sshd_config
     ...
     # Authentication: 
     LoginGraceTime 120 
     PermitRootLogin yes 
     StrictModes yes
     ...
     ```

  3. Restart the `ssh` service:

     ```
     cumulus@switch:~$ sudo systemctl reload ssh.service
     ```

## Password Security

A user password is the key credential that verifies the user accessing the switch and acts as the first line of defense to secure the switch. The complexity of the password, replacement capabilities, and change frequency define the security level of the first perimeter of the switch. To further improve and harden the switch, Cumulus Linux enables a password security option that enforces password policies that apply to all users on the switch; user passwords must include at least one lowercase character, one uppercase character, one digit, one special character, and cannot be usernames. In addition, passwords must be a minimum of eight characters long, expire in 365 days, and provide a warning 15 days before expiration.

You can change these password security policies; see {{<link url="User-Accounts/#configure-password-policies" text="Configure Password Policies">}} below.

### Disable Password Security

The password security option is on by default. To disable password security, run the `nv set system security password-hardening state disabled` command:

```
cumulus@switch:~$ nv set system security password-hardening state disabled
cumulus@switch:~$ nv config apply
```

To reenable password security, run the `nv set system security password-hardening state enabled` command.

### Configure Password Policies

The following table describes the password policies that Cumulus Linux provides and shows the default settings when password security is on. You can change these settings with NVUE commands.

| Policy |  Description  | Default Setting |
|-----   |-------------- | ----------------|
| Lowercase | Passwords must include at least one lowercase character. You can specify `enabled` or `disabled`.| `enabled` |
| Uppercase | Passwords must include at least one uppercase character. You can specify `enabled` or `disabled`.  | `enabled` |
| Digits | Passwords must include at least one digit. You can specify `enabled` or `disabled`.| `enabled` |
| Special characters | Passwords must include at least one special character. You can specify `enabled` or `disabled`. | `enabled` |
| Password length |The minimum password length. You can specify a value between 6 and 32 characters. | 8 characters |
| Expiration in days | The duration in days after which passwords expire. You can set a value between 1 and 365 days.| 180 days|
| Password expiration warning | The number of days before a password expires to send a warning. You can set a value between 1 and 30 days.| 15 days|
| Prevent usernames as passwords | Passwords cannot be usernames. You can specify `enabled` or `disabled`.| `enabled` |
| Password reuse| The number of times you can reuse the same password. You can set a value between 1 and 100.|  10|

The following example commands disable enforcement of lowercase and uppercase characters, digits, and special characters:

```
cumulus@switch:~$ nv set system security password-hardening lower-class disabled
cumulus@switch:~$ nv set system security password-hardening upper-class disabled
cumulus@switch:~$ nv set system security password-hardening digits-class disabled
cumulus@switch:~$ nv set system security password-hardening special-class disabled
```

{{%notice note%}}
Special characters include ` ~ ! @ # $ % ^ & * ( ) - _ + = | [ { } ] ; : ' , < . > / ? and white space.
{{%/notice%}}

The following example commands set the minimum password length to 10 characters, the password expiration to 30 days, and the expiration warning to 5 days before expiration.

```
cumulus@switch:~$ nv set system security password-hardening len-min 10
cumulus@switch:~$ nv set system security password-hardening expiration 30
cumulus@switch:~$ nv set system security password-hardening expiration-warning 5
```

The following example commands allow usernames as passwords and sets the number of times you can reuse a password to 20:

```
cumulus@switch:~$ nv set system security password-hardening reject-user-passw-match disabled
cumulus@switch:~$ nv set system security password-hardening history-cnt 20
```

### Show Password Policies

To show the currently configured password policies, run the `nv show system security password-hardening` command:

```
cumulus@switch:~$ nv show system security password-hardening
                         operational  applied 
-----------------------  -----------  --------
state                    enabled      enabled 
reject-user-passw-match  disabled     disabled
lower-class              enabled      enabled 
upper-class              enabled      enabled 
digits-class             disabled     disabled
special-class            disabled     disabled
expiration-warning       15           15      
expiration               180          180     
history-cnt              20           20      
len-min                  8            8
```

## Related Information

- {{<exlink url="https://man7.org/linux/man-pages/man3/crypt.3.html" text="crypt man page">}}
- {{<exlink url="https://www.cyberciti.biz/faq/understanding-etcshadow-file/" text="Understanding /etc/shadow file format on Linux">}}
