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
- You can set a plain text password or a hashed password for the local user account. To access the switch without a password, you need to {{<link url="Single-User-Mode-Password-Recovery" text="boot into a single shell/user mode">}}.
- You can provide a full name for the local user account (optional).

{{< tabs "TabID30 ">}}
{{< tab "NVUE Commands ">}}

Use the following roles to set the permissions for local user accounts.

| <div style="width:200px">Role | Permissions |
|--------- |---------- |
| `system-admin` | Allows the user to use `sudo` to run commands as the privileged user, run `nv show` commands, run `nv set` and `nv unset` commands to stage configuration changes, and run `nv apply` commands to apply configuration changes. |
| `nvue-admin` | Allows the user to run `nv show` commands, run `nv set` and `nv unset` commands to stage configuration changes, and run `nv apply` commands to apply configuration changes. |
| `nvue-monitor` | Allows the user to run `nv show` commands only.|

The following example:
- Creates a new user account called `admin2` and sets the role to `system-admin` (permissions for `sudo`, `nv show`, `nv set` and `nvunset`, and `nv apply`).
- Sets a plain text password. NVUE hashes the plain text password and stores the value as a hashed password. To set a hashed password, see {{<link url="#hashed-passwords" text="Hashed Passwords">}}, below.
- Adds the full name `FIRST LAST`. If the full name includes more than one name, either separate the names with a hyphon (`FIRST-LAST`) or enclose the full name in quotes (`"FIRST LAST"`).

```
cumulus@switch:~$ nv set system aaa user admin2 role system-admin
cumulus@switch:~$ nv set system aaa user admin2 password
Enter new password:
Confirm password:
cumulus@switch:~$ nv set system aaa user admin2 full-name "FIRST LAST"
cumulus@switch:~$ nv config apply
```

You can also run the `nv set system aaa user <user> password <plain-text-password>` command to specify the plain text password inline. This command bypasses the `Enter new password` and `Confirm password` prompts but displays the plain text password as you type it.

{{%notice note%}}
The NVUE API does not support configuring a plain text password; if you use the NVUE API instead of the CLI, NVUE only stores hashed passwords.
{{%/notice%}}

{{< /tab >}}
{{< tab "Linux Commands ">}}

Use the following groups to set permissions for local user accounts. To add users to these groups, use the `useradd(8)` or `usermod(8)` commands:

| Group | Permissions |
|--------- |---------- |
| `sudo` | Allows the user to use `sudo` to run commands as the privileged user. |
| `nvshow` | Allows the user to run `nv show` commands only. |
| `nvset`  | Allows the user to run `nv show` commands, and run `nv set` and `nv unset` commands to stage configuration changes. |
| `nvapply` | Allows the user to run `nv show` commands, run `nv set` and `nv unset` commands to stage configuration changes, and run `nv apply` commands to apply configuration changes. |

The following example:
- Creates a new user account called `admin2`, adds the full name `First Last`, and sets the password to `CumulusLinux!`
- Sets the group membership to `sudo` and `nvapply` (permissions to use `sudo`, `nv show`, `nv set`, and `nv apply`).

```
cumulus@switch:~$ sudo useradd admin2 -c "First Last" -p CumulusLinux!
cumulus@switch:~$ sudo adduser admin2 sudo
cumulus@switch:~$ sudo adduser admin2 nvapply
```

{{< /tab >}}
{{< /tabs >}}

{{%notice note%}}
Only the following user accounts can create, modify, and delete other `system-admin` accounts:
- NVUE-managed users with the `system-admin` role.
- The root user.
- Non NVUE-managed users that are in the `sudo` group.
{{%/notice%}}

### Hashed Passwords

Instead of a plain text password, you can provide a hashed password for a local user.

You must specify the hashed password in Linux `crypt` format; the password must be a minimum of 15 to 20 characters long and must include special characters, digits, lower case alphabetic letters, and more. Typically, the password format is set to `$id$salt$hashed`, where `$id` is the hashing algorithm. In GNU or Linux:
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

## Show User Accounts

To show the user accounts configured on the system, run the NVUE `nv show system aaa` command or the linux `sudo cat /etc/passwd` command.

```
cumulus@switch:~$ nv show system aaa
Username          Full-name                           Role          enable
----------------  ----------------------------------  ------------  ------
Debian-snmp                                           Unknown       system
_apt                                                  Unknown       system
_lldpd                                                Unknown       system
admin2            FIRST LAST                          system-admin  on    
...
```

To show information about a specific user account, run the run the NVUE `nv show system aaa user <user>` command:

```
cumulus@switch:~$ nv show system aaa user admin2
                 operational   applied     
---------------  ------------  ------------
full-name        FIRST LAST    FIRST LAST  
hashed-password  *             *           
role             system-admin  system-admin
enable           on            on  
```

## Enable Remote Access for a root User

The root user does not have a password and cannot log into a switch using SSH. This default account behavior is consistent with Debian. To connect to a switch using the root account, you can do one of the following:

- Generate an SSH key
- Set a password

### Generate an SSH Key for the root Account

1. In a terminal on your host system (not the switch), check to see if a key already exists:

    ```
    root@host:~# ls -al ~/.ssh/
    ```

    The name of the key is similar to `id_dsa.pub`, `id_rsa.pub`, or `id_ecdsa.pub`.

2. If a key does not exist, generate a new one by first creating the RSA key pair:

    ```
    root@host:~# ssh-keygen -t rsa
    ```

3. At the prompt, enter a file in which to save the key (`/root/.ssh/id_rsa`). Press Enter to use the home directory of the root user or provide a different destination.

4. At the prompt, enter a passphrase (empty for no passphrase). This is optional but it does provide an extra layer of security.

   The public key is now located in `/root/.ssh/id_rsa.pub`. The private key (identification) is now located in `/root/.ssh/id_rsa`.

5. Copy the public key to the switch. SSH to the switch as the cumulus user, then run:

    ```
    cumulus@switch:~$ sudo mkdir -p /root/.ssh
    cumulus@switch:~$ echo <SSH public key string> | sudo tee -a /root/.ssh/authorized_keys
    ```

### Set the root User Password

{{< tabs "TabID81 ">}}
{{< tab "NVUE Commands ">}}

```
cumulus@switch:~$ nv set system aaa user root password
Enter new password:
...
cumulus@switch:~$ nv config apply
```

{{< /tab >}}
{{< tab "Linux Commands ">}}

1. Run the following command:

    ```
    cumulus@switch:~$ sudo passwd root
    Enter new password:
    ...
    ```

2. Change the `PermitRootLogin` setting in the `/etc/ssh/sshd_config` file from *without-password* to *yes*.

    ``` 
    cumulus@switch:~$ sudo nano /etc/ssh/sshd_config
    ...
    # Authentication:
    LoginGraceTime 120
    PermitRootLogin yes
    StrictModes yes
    ...  
    ```

3. Restart the `ssh` service:

    ```
    cumulus@switch:~$ sudo systemctl reload ssh.service
    ```

{{< /tab >}}
{{< /tabs >}}

## Related Information

- {{<exlink url="https://man7.org/linux/man-pages/man3/crypt.3.html" text="crypt man page">}}
- {{<exlink url="https://www.cyberciti.biz/faq/understanding-etcshadow-file/" text="Understanding /etc/shadow file format on Linux">}}
