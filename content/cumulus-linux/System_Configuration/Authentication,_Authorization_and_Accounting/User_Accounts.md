---
title: User Accounts
author: Cumulus Networks
weight: 275
aliases:
 - /display/DOCS/User+Accounts
 - /pages/viewpage.action?pageId=8362553
pageID: 8362553
product: Cumulus Linux
version: 3.7.7
imgData: cumulus-linux
siteSlug: cumulus-linux
---
By default, Cumulus Linux has two user accounts: *cumulus* and *root*.

The *cumulus* account:

  - 
    
    <div id="src-8362553_indexterm-50F8B57828989BFCD3F7B3B095E560B0">
    
    Uses the default password *CumulusLinux\!*
    
    </div>

  - Is a user account in the *sudo* group with sudo privileges.

  - Can log in to the system through all the usual channels, such as
    console and
    [SSH](/cumulus-linux/System_Configuration/Authentication_Authorization_and_Accounting/SSH_for_Remote_Access).

  - Along with the cumulus group, has both show and edit rights for
    [NCLU](/cumulus-linux/System_Configuration/Network_Command_Line_Utility_-_NCLU).

The *root* account:

  - Has the default password disabled by default.

  - Has the standard Linux root user access to everything on the switch.

  - Disabled password prohibits login to the switch by SSH, telnet, FTP,
    and so on.

For optimal security, change the default password with the `passwd`
command before you configure Cumulus Linux on the switch.

You can add additional user accounts as needed. Like the *cumulus*
account, these accounts must use `sudo` to [execute privileged
commands](/cumulus-linux/System_Configuration/Authentication_Authorization_and_Accounting/Using_sudo_to_Delegate_Privileges);
be sure to include them in the *sudo* group.

To access the switch without a password, you need to [boot into a single
shell/user
mode](/cumulus-linux/Monitoring_and_Troubleshooting/Single_User_Mode_-_Boot_Recovery).

You can add and configure user accounts in Cumulus Linux with read-only
or edit permissions for NCLU. For more information, see [Configure User
Accounts](Network_Command_Line_Utility_-_NCLU.html#src-8362580_NetworkCommandLineUtility-NCLU-configure-user-accounts).

## <span>Enable Remote Access for the root User</span>

The root user does not have a password and cannot log into a switch
using SSH. This default account behavior is consistent with Debian. To
connect to a switch using the root account, you can do one of the
following:

  - Generate an SSH key

  - Set a password

### <span id="src-8362553_UserAccounts-ssh_key" class="confluence-anchor-link"></span><span>Generate an SSH Key for the root Account</span>

1.  In a terminal on your host system (not the switch), check to see if
    a key already exists:
    
        root@host:~# ls -al ~/.ssh/
    
    The key is named something like `id_dsa.pub`, `id_rsa.pub` or
    `id_ecdsa.pub`.

2.  If a key does not exist, generate a new one by first creating the
    RSA key pair:
    
        root@host:~# ssh-keygen -t rsa

3.  You are prompted to enter a file in which to save the key
    (/root/.ssh/id\_rsa)*.* Press Enter to use the home directory of the
    root user or provide a different destination.

4.  You are prompted to enter a passphrase (empty for no passphrase).
    This is optional but it does provide an extra layer of security.

5.  The public key is now located in `/root/.ssh/id_rsa.pub`. The
    private key (identification) is now located in `/root/.ssh/id_rsa`.

6.  Copy the public key to the switch. SSH to the switch as the cumulus
    user, then run:
    
        cumulus@switch:~$ sudo mkdir -p /root/.ssh
        cumulus@switch:~$ echo <SSH public key string> | sudo tee -a /root/.ssh/authorized_keys

### <span id="src-8362553_UserAccounts-root_passwd" class="confluence-anchor-link"></span><span>Set the root User Password</span>

1.  Run the following command:
    
        cumulus@switch:~$ sudo passwd root

2.  Change the `PermitRootLogin` setting in the `/etc/ssh/sshd_config`
    file from *without-password* to *yes*.
    
    ``` 
    cumulus@switch:~$ sudo nano /etc/ssh/sshd_config
     
    ... 
          
    # Authentication:
    LoginGraceTime 120
    PermitRootLogin yes
    StrictModes yes
          
    ...  
    ```

3.  Restart the `ssh` service:
    
        cumulus@switch:~$ sudo systemctl reload ssh.service
