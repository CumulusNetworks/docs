---
title: All Switches Installed from the Same Cumulus Linux 4.0.0 and 4.1.0 Image Have the Same SSH Host Keys
author: NVIDIA
weight: 454
toc: 4
---

## Issue

Due to a packaging error, all switches installed from the same Cumulus Linux image have the same SSH host keys. This affects switches originally installed with Cumulus Linux 4.0.0 and 4.1.0 from a disk image only (including those that were upgraded by `apt` to a later release).

As a result, this issue allows an attacker to more easily bypass remote host verification when a user connects by SSH to what is believed to be a previously used remote host but is really the attacker's host. For example, this issue can be exploited by a spoofing or man-in-the-middle attack.

## Environment

- Switches originally installed with Cumulus Linux 4.0.0 and 4.1.0 from a disk image only, including those that were upgraded by `apt` to a later release

## Resolution

To resolve this issue, generate new SSH host keys for any switch that has Cumulus Linux 4.0.0 or 4.1.0 installed on it:

    cumulus@switch:~$ sudo rm /etc/ssh/ssh_host*
    cumulus@switch:~$ sudo dpkg-reconfigure openssh-server
    cumulus@switch:~$ sudo systemctl restart ssh

After generating new SSH host keys, SSH clients that have previously logged into that switch will see a warning that the switch's SSH host key changed; this is expected behavior. Be sure to inform anyone who may log in to the switch that you generated new SSH host keys. These users must log in to the affected switches with their SSH clients, where they will be given instructions on how to remove the old SSH host keys from the known hosts files to avoid a spoofing or man-in-the-middle attack directed at their SSH clients.

## Notes

- This issue is fixed in Cumulus Linux 4.1.1. However, Cumulus Networks recommends you generate new SSH host keys as this is the most reliable solution.
- If you upgrade from Cumulus Linux 4.0.0 or 4.1.0 to version 4.1.1 or later using `apt-get` and you didn't generate new SSH host keys, you will need to generate new SSH host keys after the upgrade.
- If you perform a fresh install of Cumulus Linux 4.1.1 or later using a disk image, you will lose your existing local configuration.
