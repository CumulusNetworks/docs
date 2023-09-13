---
title: Single User Mode - Password Recovery
author: NVIDIA
weight: 1200
toc: 3
---
{{%notice warning%}}
In Cumulus Linux 5.6, you can't reset the root password by booting into Cumulus Linux single-user recovery mode. To work around this issue, reset the cumulus or root user password as follows:

1. Use `df /` to determine which device is mounted on `/`. If you cannot access the switch but another switch with the same hardware is available, use `df /` on that switch to find the device.
2. Reboot the switch.
3. In the GRUB menu, select `ONIE`, then in the GRUB ONIE menu, select `ONIE Rescue`.
4. When prompted, press enter.
5. Mount the device in step 1 with the `mount $DEVICE /mnt` command.

   If you did not determine the mount point in step 1, you can use the `df` command to determine which devices to try; for example, if `/mnt/onie-boot` is on `/dev/sda2`, try `mount /dev/sda4 /mnt`. If this is the correct device, `ls /mnt` shows a root file system and `ls /mnt/etc/shadow` shows a file.

6. Run `chroot /mnt`, then run `passwd cumulus` or `passwd root`.
7. Exit, then reboot.

To avoid using the above workaround and to ensure that the Cumulus Linux single-user recovery mode boots, you can do the following **before** you upgrade to Cumulus Linux 5.6.

1. Change directories to `/lib/systemd/system`.

   ```
   cumulus@switch:~$ cd /lib/systemd/system
   ```

2. Remove the symlink `rescue.service`

   ```
   cumulus@switch:~$ sudo rm rescue.service
   ```

3. Rename `rescue.service.cumulus` to `rescue.service`:

   ```
   cumulus@switch:~$ sudo cp rescue.service.cumulus rescue.service
   ```

{{%/notice%}}

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

You can take this opportunity to reset the password for the *cumulus* account.

       root@switch:~# passwd cumulus
       Enter new UNIX password:
       Retype new UNIX password:
       passwd: password updated successfully

{{%/notice%}}

4. Sync the `/etc` directory, then reboot the system:

       root@switch:~# sync
       root@switch:~# reboot -f
       Restarting the system.
