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
You can take this opportunity to reset the password for the *cumulus* account. If you manage the switch by editing configuration files manually, run the following command:

       root@switch:~# passwd cumulus
       Enter new UNIX password:
       Retype new UNIX password:
       passwd: password updated successfully

If you manage the switch configuration with NVUE commands, you cannot use single user mode to reset the cumulus account password. Log into the switch as the root user and change the cumulus account password (or any NVUE-managed user account passwords) with the `nv set system aaa user <user-id> password <value>` command.

In Cumulus Linux 5.9 and later, user passwords must include at least one lowercase character, one uppercase character, one digit, one special character, and cannot be usernames. In addition, passwords must be a minimum of eight characters long, expire in 365 days, and provide a warning 15 days before expiration. For more information about the password security policy, refer to {{<link url="User-Accounts/#password-security" text="Password Security">}}.

{{%/notice%}}

4. Sync the `/etc` directory, then reboot the system:

       root@switch:~# sync
       root@switch:~# reboot -f
       Restarting the system.
