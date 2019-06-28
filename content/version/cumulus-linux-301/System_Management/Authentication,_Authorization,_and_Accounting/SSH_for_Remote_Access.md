---
title: SSH for Remote Access
author: Cumulus Networks
weight: 217
aliases:
 - /display/CL30/SSH+for+Remote+Access
 - /pages/viewpage.action?pageId=5118211
pageID: 5118211
product: Cumulus Linux
version: '3.0'
imgData: cumulus-linux-301
siteSlug: cumulus-linux-301
---
You use [SSH](http://en.wikipedia.org/wiki/Secure_Shell) to securely
access a Cumulus Linux switch remotely.

{{%notice note%}}

By default, you cannot use the root account to SSH to a Cumulus Linux
switch unless you [generate an SSH
key](User_Accounts.html#src-5118212_UserAccounts-ssh_key) or [set a
password](User_Accounts.html#src-5118212_UserAccounts-root_passwd) for
the account.

{{%/notice%}}

## <span>Access Using Passkey (Basic Setup)</span>

Cumulus Linux uses the openSSH package to provide SSH functionality. The
standard mechanisms of generating passwordless access just applies. The
example below has the *cumulus* user on a machine called
*management-station* connecting to a switch called *cumulus-switch1*.

First, on *management-station*, generate the SSH keys:

    cumulus@management-station:~$ ssh-keygen
       Generating public/private rsa key pair.
       Enter file in which to save the key (/home/cumulus/.ssh/id_rsa):
       Enter passphrase (empty for no passphrase):
       Enter same passphrase again:
       Your identification has been saved in /home/cumulus/.ssh/id_rsa.
       Your public key has been saved in /home/cumulus/.ssh/id_rsa.pub.
       The key fingerprint is:
       8c:47:6e:00:fb:13:b5:07:b4:1e:9d:f4:49:0a:77:a9 cumulus@management-station
       The key's randomart image is:
       +--[ RSA 2048]----+
       |    .  .= o o.   |
       |     o . O *..   |
       |    . o = =.o    |
       |     . O oE      |
       |      + S        |
       |       +         |
       |                 |
       |                 |
       |                 |
       +-----------------+

Next, append the public key in `~/.ssh/id_rsa.pub` into
`~/.ssh/authorized_keys` in the target user's home directory:

    cumulus@management-station:~$ scp .ssh/id_rsa.pub cumulus@cumulus-switch1:.ssh/authorized_keys
        Enter passphrase for key '/home/cumulus/.ssh/id_rsa':
        id_rsa.pub

### <span>Completely Passwordless System</span>

When generating the passphrase and its associated keys, as in the first
step above, do not enter a passphrase. Follow all the other
instructions.

## <span>Useful Links</span>

  - <http://www.debian-administration.org/articles/152>
