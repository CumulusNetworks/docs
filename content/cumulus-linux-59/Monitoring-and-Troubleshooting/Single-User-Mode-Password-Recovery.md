---
title: Single User Mode - Password Recovery
author: NVIDIA
weight: 1200
toc: 3
---
Use single user mode to assist in troubleshooting system boot issues or for password recovery.

To enter single user mode:

1. Boot the switch, then as soon as you see the GRUB menu, use the arrow keys to select **Advanced options for Cumulus Linux GNU/Linux**.

   {{%notice info%}}
**Before** the GRUB menu appears, the switch goes through the boot cycle. Do **not** interrupt this autoboot process when you see the following lines; wait until you see the GRUB menu.

```
...
USB0:  Bringing USB2 host out of reset...
Net:   eth-0
SF:    MX25L6405D with page size 4 KiB, total 8 MiB
Hit any key to stop autoboot:  2
```
{{%/notice%}}

                    GNU GRUB  version 2.02+dfsg1-20

       +----------------------------------------------------------------------------+
       |*Cumulus Linux GNU/Linux                                                    |
       | Advanced options for Cumulus Linux GNU/Linux                               |
       | ONIE                                                                       |
       |                                                                            |
       +----------------------------------------------------------------------------+

2. Select **Cumulus Linux GNU/Linux, with Linux 4.19.0-cl-1-amd64 (recovery mode)**.

                    GNU GRUB  version 2.02+dfsg1-20

       +----------------------------------------------------------------------------+
       | Cumulus Linux GNU/Linux, with Linux 4.19.0-cl-1-amd64                       |
       |*Cumulus Linux GNU/Linux, with Linux 4.19.0-cl-1-amd64 (recovery mode)       |
       |                                                                            |
       +----------------------------------------------------------------------------+  

3. After the system reboots, set a new **root** password. The root user provides complete control over the switch.

       root@switch:~# passwd
       Enter new UNIX password:
       Retype new UNIX password:
       passwd: password updated successfully

   {{%notice tip%}}
You can also take this opportunity to reset the password for the *cumulus* account or other user accounts. You can set the user account password to expire upon the next login with the `passwd <user-account> --expire` command. Or to change the password for a user account, run the `passwd <user-account>` command. For information about user accounts, refer to {{<link url="User-Accounts" text="User Accounts">}}.

The following example changes the password for the *cumulus* user:

       root@switch:~# passwd cumulus
       Enter new UNIX password:
       Retype new UNIX password:
       passwd: password updated successfully

If you manage the switch configuration with NVUE commands, you must also change the password for the *cumulus* user in the `/etc/nvue.d/startup.yaml` configuration file. Obtain the new password's SHA hash with the following command:

```
root@switch:~# /usr/bin/grep cumulus /etc/shadow | /usr/bin/cut -d ":" -f 2
$y$j9T$Iytj2XM4L1RUT82vS6gge1$APrp2ETA6tsxOVDzNkq3Li478VgZIexe3ToFDYBqb/.
```

Use the output of the command to edit the `/etc/nvue.d/startup.yaml` file

```
root@switch:~# nano /etc/nvue.d/startup.yaml

 system:
      aaa:
        user:
          cumulus:
            hashed-password: $y$j9T$Iytj2XM4L1RUT82vS6gge1$APrp2ETA6tsxOVDzNkq3Li478VgZIexe3ToFDYBqb/.
            role: system-admin
```

In Cumulus Linux 5.9 and later, user passwords must include at least one lowercase character, one uppercase character, one digit, one special character, and cannot be usernames. In addition, passwords must be a minimum of eight characters long, expire in 365 days, and provide a warning 15 days before expiration. For more information about the password security policy, refer to {{<link url="User-Accounts/#password-security" text="Password Security">}}.

{{%/notice%}}

4. Sync the `/etc` directory, then reboot the system:

       root@switch:~# sync
       root@switch:~# reboot -f
       Restarting the system.
