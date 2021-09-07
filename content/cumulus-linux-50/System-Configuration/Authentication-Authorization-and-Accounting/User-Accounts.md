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
- Along with the cumulus group, has both show and edit rights for NCLU.

The *root* account:

- Has the default password disabled by default
- Has the standard Linux root user access to everything on the switch
- The disabled password prevents you from using SSH, telnet, FTP, and so on, to log in to the switch.

You can add additional user accounts as needed. Like the *cumulus* account, these accounts must use `sudo` to {{<link url="Using-sudo-to-Delegate-Privileges" text="execute privileged commands">}}; be sure to include them in the *sudo* group. For example:

```
cumulus@switch:~$ sudo adduser NEWUSERNAME sudo
```

To access the switch without a password, you need to {{<link url="Single-User-Mode-Password-Recovery" text="boot into a single shell/user mode">}}.

<!--WHAT HAPPENS FOR NVUE? - You can add and configure user accounts in Cumulus Linux with read-only or edit permissions for NCLU. For more information, see Configure User Accounts.-->

## Enable Remote Access for the root User

The root user does not have a password and cannot log into a switch using SSH. This default account behavior is consistent with Debian. To connect to a switch using the root account, you can do one of the
following:

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
<!-- vale off -->
3. At the prompt, enter a file in which to save the key (/root/.ssh/id\_rsa)*.* Press Enter to use the home directory of the root user or provide a different destination.
<!-- vale on -->
4. At the prompt, enter a passphrase (empty for no passphrase). This is optional but it does provide an extra layer of security.
5. The public key is now located in `/root/.ssh/id_rsa.pub`. The private key (identification) is now located in `/root/.ssh/id_rsa`.
6. Copy the public key to the switch. SSH to the switch as the cumulus user, then run:

    ```
    cumulus@switch:~$ sudo mkdir -p /root/.ssh
    cumulus@switch:~$ echo <SSH public key string> | sudo tee -a /root/.ssh/authorized_keys
    ```

### Set the root User Password

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
