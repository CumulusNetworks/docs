---
title: Secure Mount Directory Encryption
author: NVIDIA
weight: 280
toc: 3
---

To protect sensitive data at rest, you can configure secure mount directory encryption on the switch with a USB device. Cumulus Linux uses the `gocryptfs` application to create and manage an encrypted view of your files.

### Enable and Manage Encryption

To enable secure mount directory encryption or change the existing encryption password, make sure the USB device is plugged in, then run the `nv action enable system security encryption folder-encrypt password <password>` command. The switch restarts after you run the command.

```
cumulus@switch:~$ nv action enable system security encryption folder-encrypt password MYPASSWORD
```

- The first time you enable secure mount directory encryption, the switch starts a background process to copy and encrypt all data in the managed directories.
- If you have already enabled secure mount directory encryption, the switch rotates the encryption and updates the stored key on the configured USB device, replacing the old one.

To disable secure mount directory encryption, run the `nv action disable system security encryption folder-encrypt` command. The switch restarts after you run the command.

### Configure Directories for Encryption

When you enable secure mount directory encryption, the switch encrypts the `/var/log`, `/var/home`, and `/var/lib` directories. To configure the absolute path to other directories you want to encrypt, run the `nv set system security encryption folder-encrypt encrypted_folder <path_to_new_folder>` command:

```
cumulus@switch:~$ nv set system security encryption folder-encrypt encrypted_folder /my_user/my_data
```

{{%notice info%}}
- For encryption changes to take effect, you must reboot the switch.
- The USB device containing the key must remain plugged in at all times for the switch to function. If you unplug the USB, the system becomes inaccessible.
- You cannot encrypt the `/boot`, `/etc`, `/dev`, and `/usr` directories.
{{%/notice%}}
