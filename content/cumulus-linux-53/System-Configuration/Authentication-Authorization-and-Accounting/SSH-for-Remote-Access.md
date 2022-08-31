---
title: SSH for Remote Access
author: NVIDIA
weight: 140
toc: 4
---
You can generate authentication keys to access a Cumulus Linux switch securely with the `ssh-keygen` component of the Secure Shell (SSH) protocol. Cumulus Linux uses the OpenSSH package to provide this functionality. This section describes how to generate an SSH key pair.

## Generate an SSH Key Pair

1. To generate the SSH key pair, run the `ssh-keygen` command and follow the prompts:

    {{%notice info%}}
To configure the system without a password, do not enter a passphrase when prompted in the following step.
{{%/notice%}}

    ```
    cumulus@leaf01:~$ ssh-keygen
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

2. To copy the generated public key to the desired location, run the `ssh-copy-id` command and follow the prompts:

    ```
    cumulus@leaf01:~$ ssh-copy-id -i /home/cumulus/.ssh/id_rsa.pub cumulus@leaf02
    The authenticity of host 'leaf02 (192.168.0.11)' can't be established.
    ECDSA key fingerprint is b1:ce:b7:6a:20:f4:06:3a:09:3c:d9:42:de:99:66:6e.
    Are you sure you want to continue connecting (yes/no)? yes
    /usr/bin/ssh-copy-id: INFO: attempting to log in with the new key(s), to filter out any that are already installed
    /usr/bin/ssh-copy-id: INFO: 1 key(s) remain to be installed -- if you are prompted now it is to install the new keys
    cumulus@leaf01's password:

    Number of key(s) added: 1
    ```

   `ssh-copy-id` does not work if the username on the remote switch is different from the username on the local switch. To work around this issue, use the `scp` command instead:

    ```
    cumulus@leaf01:~$ scp .ssh/id_rsa.pub cumulus@leaf02:.ssh/authorized_keys
    Enter passphrase for key '/home/cumulus/.ssh/id_rsa':
    id_rsa.pub
    ```

3. Connect to the remote switch to confirm that the authentication keys are in place:

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

## Related Information

{{<exlink url="https://debian-administration.org/article/152/Password-less_logins_with_OpenSSH" text="Debian Documentation - Password-less logins with OpenSSH">}}
