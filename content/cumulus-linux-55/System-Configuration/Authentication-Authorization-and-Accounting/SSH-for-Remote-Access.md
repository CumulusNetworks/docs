---
title: SSH for Remote Access
author: NVIDIA
weight: 140
toc: 4
---
Cumulus Linux uses the OpenSSH package to provide access to the system using the Secure Shell (SSH) protocol. With SSH, you can use key pairs instead of passwords to gain access to the system.

This section describes how to generate an SSH key pair on one system and install the key as an authorized key in another system.

## Generate an SSH Key Pair

To generate an SSH key pair, run the `ssh-keygen` command and follow the prompts.

{{%notice note%}}
To configure the system without a password, do not enter a passphrase when prompted in the following step.
{{%/notice%}}

```
cumulus@host01:~$ ssh-keygen 
Generating public/private rsa key pair. 
Enter file in which to save the key (/home/cumulus/.ssh/id_rsa): 
Enter passphrase (empty for no passphrase): 
Enter same passphrase again: 
Your identification has been saved in /home/cumulus/.ssh/id_rsa. 
Your public key has been saved in /home/cumulus/.ssh/id_rsa.pub. 
The key fingerprint is: 
5a:b4:16:a0:f9:14:6b:51:f6:f6:c0:76:1a:35:2b:bb cumulus@leaf04 
The key's randomart image is: 
+---[RSA 2048]----+ 
|      +.o   o    | 
|     o * o . o   | 
|    o + o O o    | 
|     + . = O     | 
|      . S o .    | 
|       +   .     | 
|      .   E      | 
|                 | 
|                 | 
+-----------------+ 
```

## Install an Authorized SSH Key

To install an authorized SSH key, you take the contents of an SSH public key and add it to the SSH authorized key file (`~/.ssh/authorized_keys`) of the user.

A public key is a text file with three space separated fields:

```
<type> <key string> <comment>
```

| Field | Description |
| ----- | ----------- |
| `<type>`  | The algorithm you want to use to hash the key. The algorithm can be `ecdsa-sha2-nistp256`, `ecdsa-sha2-nistp384`, `ecdsa-sha2-nistp521`, `ssh-dss`, `ssh-ed25519`, or `ssh-rsa` (the default value). |
| `<key string>` | A base64 format string for the key. |
| `<comment>` | A single word string. By default, this is the name of the system that generated the key. NVUE uses the `<comment>` field as the key name. |

The procedure to install an authorized SSH key is different based on whether the user is an NVUE managed user, a non-NVUE managed user, or the root user.

### NVUE Managed User

The following example adds an authorized key named `prod_key` to the user `admin2`. The content of the public key file is `ssh-rsa 1234 prod_key`.

```
cumulus@leaf01:~$ nv set system aaa user admin2 ssh authorized-key prod_key key XABDB3NzaC1yc2EAAAADAQABAAABgQCvjs/RFPhxLQMkckONg+1RE1PTIO2JQhzFN9TRg7ox7o0tfZ+IzSB99lr2dmmVe8FRWgxVjc...
cumulus@leaf01:~$ nv set system aaa user admin2 ssh authorized-key prod_key type ssh-rsa
cumulus@leaf01:~$ nv config apply
```
<!-- vale off -->
### Non-NVUE Managed User
<!-- vale on -->
The following example adds an authorized key file from the account `cumulus` on a host to the `cumulus` account on the switch:

1. To copy a previously generated public key to the desired location, run the `ssh-copy-id` command and follow the prompts:

   ```
   cumulus@host01:~$ ssh-copy-id -i /home/cumulus/.ssh/id_rsa.pub cumulus@leaf02
   The authenticity of host 'leaf02 (192.168.0.11)' can't be established.
   ECDSA key fingerprint is b1:ce:b7:6a:20:f4:06:3a:09:3c:d9:42:de:99:66:6e.
   Are you sure you want to continue connecting (yes/no)? yes
   /usr/bin/ssh-copy-id: INFO: attempting to log in with the new key(s), to filter out any that are already installed
   /usr/bin/ssh-copy-id: INFO: 1 key(s) remain to be installed -- if you are prompted now it is to install the new keys
   cumulus@leaf01's password:
   Number of key(s) added: 1
   ```

   The `ssh-copy-id` command does not work if the username on the remote switch is different from the username on the local switch. To work around this issue, use the `scp` command instead:

   ```
   cumulus@host01:~$ scp .ssh/id_rsa.pub cumulus@leaf02:.ssh/authorized_keys
   Enter passphrase for key '/home/cumulus/.ssh/id_rsa':
   id_rsa.pub
   ```

2. Connect to the remote switch to confirm that the authentication keys are in place:

   ```
   cumulus@leaf01:~$ ssh cumulus@leaf02
   Welcome to Cumulus VX (TM) 
   Cumulus VX (TM) is a community supported virtual appliance designed for
   experiencing, testing and prototyping the latest technology.
   For any questions or technical support, visit our community site at:
   http://community.cumulusnetworks.com 
   The registered trademark Linux (R) is used pursuant to a sublicense from LMI,
   the exclusive licensee of Linus Torvalds, owner of the mark on a world-wide basis. 
   Last login: Thu Sep 29 16:56:54 2016
   ```

### Root User

By default, the root account cannot use SSH to log in. To add an authorized SSH key to the root account:

1. Create an `.ssh` directory for the root user.

   ```
   cumulus@switch:~$ sudo mkdir -p /root/.ssh
   cumulus@switch:~$ sudo chmod 0700 /root/.ssh 
   ```

2. As a privileged user (such as the `cumulus` user), either `echo` the public key contents and redirect the contents to the authorized key file *or* copy the public key file to the switch, then copy it to the root account (with privilege escalation).

   To echo the public key contents and redirect the contents to the authorized key file:

   ```
   cumulus@switch:~$ echo "<SSH public key contents>" | sudo tee -a /root/.ssh/authorized_keys 
   cumulus@switch:~$ sudo chmod 0644 /root/.ssh/authorized_keys 
   ```

   To copy the public key file to the switch, then copy it to the root account:

   ```
   cumulus@switch:~$ sudo cp <SSH public key file> /root/.ssh/authorized_keys 
   cumulus@switch:~$ sudo chmod 0644 /root/.ssh/authorized_keys
   ```

## SSH and VRFs

The SSH service runs in the default VRF on the switch but listens on all interfaces in all VRFs. To limit SSH to listen on just one VRF, you need to bind the SSH service to that VRF.

The following example configures SSH to listen only on the management VRF:

```
cumulus@switch:~$ sudo systemctl stop ssh.service
cumulus@switch:~$ sudo systemctl disable ssh.service
cumulus@switch:~$ sudo systemctl start ssh@mgmt.service
cumulus@switch:~$ sudo systemctl enable ssh@mgmt.service
```

To configure SSH to listen to only one IP address or a subnet in a VRF, you need to bind the service to that VRF (as above), then set the `ListenAddress` parameter in the `/etc/ssh/sshd_config` file to the IP address or subnet in that VRF.

```
cumulus@switch:~$ sudo cat /etc/ssh/sshd_config
...

#Port 22
#AddressFamily any
ListenAddress 10.10.10.6
#ListenAddress ::
```

{{%notice note%}}
You can only run one SSH service on the switch at a time.
{{%/notice%}}
