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
- You control local user account access to NVUE commands by changing the group membership (role) for a user. Like the *cumulus* account, these accounts must use `sudo` to {{<link url="Using-sudo-to-Delegate-Privileges" text="execute privileged commands">}}; be sure to include them in the *sudo* group.
- You can set a normal password or a hashed password for the local user account. To access the switch without a password, you need to {{<link url="Single-User-Mode-Password-Recovery" text="boot into a single shell/user mode">}}.
- You can provide a full name for the local user account (optional).

{{< tabs "TabID30 ">}}
{{< tab "NVUE Commands ">}}

Use the following roles to set the permissions for local user accounts.

| <div style="width:200px">Role | Permissions |
|--------- |---------- |
| `system-admin` | Allows the user to use `sudo` to run commands as the privileged user, run `nv show` commands, run `nv set` and `nv unset` commands to stage configuration changes, and run `nv apply` commands to apply configuration changes. |
| `nvue-admin` | Allows the user to run `nv show` commands, run `nv set` and `nv unset` commands to stage configuration changes, and run `nv apply` commands to apply configuration changes. |
| `nvue-monitor` | Allows the user to run `nv show` commands only.|

{{%notice note%}}
Only user accounts with the `system-admin` role can create, modify, and delete other `system-admin` accounts.
{{%/notice%}}

The following example:
- Creates a new user account called `admin2` and sets the role to `system-admin` (permissions for `sudo`, `nv show`, `nv set`, and `nv apply`).
- Adds the full name `FIRST LAST`. If the full name includes more than one name, either separate the names with a hyphon (FIRST-LAST) or enclose the full name in quotes ("FIRST LAST").
- Sets the password to CumulusLinux!

```
cumulus@switch:~$ nv set system aaa user admin2 role system-admin
cumulus@switch:~$ nv set system aaa user admin2 password CumulusLinux!
cumulus@switch:~$ nv set system aaa user admin2 full-name "FIRST LAST"
cumulus@switch:~$ nv config apply
```

To set a hashed password for the local user, run the `nv set system aaa user <username> hashed-password <hashed-password>` command.

To set an SSH authorized key for a user, run the `nv set system aaa user <username> ssh authorized-key <value>` command.

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
- Creates a new user account called `admin2`, adds the full name `First Last`, and sets the password to CumulusLinux!
- Sets the group membership to `sudo` and `nvapply` (permissions to use `sudo`, `nv show`, `nv set`, and `nv apply`).

```
cumulus@switch:~$ sudo useradd admin2 -c "First Last" -p CumulusLinux!
cumulus@switch:~$ sudo adduser admin2 sudo
cumulus@switch:~$ sudo adduser admin2 nvapply
```

{{< /tab >}}
{{< /tabs >}}

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
cumulus@switch:~$ nv show system aaa user
```

To show information about a specific user account, run the run the NVUE `nv show system aaa user <user>` command:

```
cumulus@switch:~$ nv show system aaa user admin2
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
cumulus@switch:~$ nv config apply
```

{{< /tab >}}
{{< tab "Linux Commands ">}}

1. Run the following command:

    ```
    cumulus@switch:~$ sudo passwd root
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
