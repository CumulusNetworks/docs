---
title: SSH for Remote Access
author: Cumulus Networks
weight: 267
aliases:
 - /display/CL35/SSH+for+Remote+Access
 - /pages/viewpage.action?pageId=8357332
pageID: 8357332
product: Cumulus Linux
version: '3.5'
imgData: cumulus-linux-35
siteSlug: cumulus-linux-35
---
Authentication keys can be generated for securely accessing a Cumulus
Linux switch with the ssh-keygen component of the Secure Shell (SSH)
protocol. Cumulus Linux uses the OpenSSH package to provide this
functionality. The section below covers how to generate a SSH key pair.

## <span>Generate an SSH Key Pair</span>

1.  Run the `ssh-keygen` command, and follow the prompts, to generate
    the key pair:
    
    {{%notice info%}}
    
    **Configure a Passwordless System**
    
    To configure a completely passwordless system, do not enter a
    passphrase when prompted in the following step.
    
    {{%/notice%}}
    
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

2.  Run the `ssh-copy-id` command, and follow the prompts, to copy the
    generated public key to the desired location:
    
        cumulus@leaf01:~$ ssh-copy-id -i /home/cumulus/.ssh/id_rsa.pub cumulus@leaf02
        The authenticity of host 'leaf02 (192.168.0.11)' can't be established.
        ECDSA key fingerprint is b1:ce:b7:6a:20:f4:06:3a:09:3c:d9:42:de:99:66:6e.
        Are you sure you want to continue connecting (yes/no)? yes
        /usr/bin/ssh-copy-id: INFO: attempting to log in with the new key(s), to filter out any that are already installed
        /usr/bin/ssh-copy-id: INFO: 1 key(s) remain to be installed -- if you are prompted now it is to install the new keys
        cumulus@leaf01's password:
         
        Number of key(s) added: 1
    
    {{%notice warning%}}
    
    `ssh-copy-id` will not work if the username on the remote switch is
    different to the local switch. To work around this issue, use the
    `scp` command instead:
    
        cumulus@leaf01:~$ scp .ssh/id_rsa.pub cumulus@leaf02:.ssh/authorized_keys
        Enter passphrase for key '/home/cumulus/.ssh/id_rsa':
        id_rsa.pub
    
    {{%/notice%}}

3.  Connect to the remote switch to confirm the authentication keys are
    in place:
    
        cumulus@leaf04:~$ ssh cumulus@leaf02
         
        Welcome to Cumulus VX (TM)
         
        Cumulus VX (TM) is a community supported virtual appliance designed for
        experiencing, testing and prototyping Cumulus Networks' latest technology.
        For any questions or technical support, visit our community site at:
        http://community.cumulusnetworks.com
         
        The registered trademark Linux (R) is used pursuant to a sublicense from LMI,
        the exclusive licensee of Linus Torvalds, owner of the mark on a world-wide
        basis.
        Last login: Thu Sep 29 16:56:54 2016

## <span>Related Information</span>

  - [Debian Documentation - Password-less logins with
    OpenSSH](http://www.debian-administration.org/articles/152)

  - [Wikipedia - Secure Shell
    (SSH)](http://en.wikipedia.org/wiki/Secure_Shell)

<article id="html-search-results" class="ht-content" style="display: none;">

</article>

<footer id="ht-footer">

</footer>
