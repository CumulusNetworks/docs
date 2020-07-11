---
title: Single User Mode - Password Recovery
author: Cumulus Networks
weight: 920
toc: 3
---
Use single user mode to assist in troubleshooting system boot issues or for password recovery.

To enter single user mode:

1. Boot the switch, then as soon as you see the GRUB menu, use the arrow keys to select **Advanced options for Cumulus Linux GNU/Linux**.

    ```
                    GNU GRUB  version 2.02+dfsg1-20

    +----------------------------------------------------------------------------+
    |*Cumulus Linux GNU/Linux                                                    |
    | Advanced options for Cumulus Linux GNU/Linux                               |
    | ONIE                                                                       |
    |                                                                            |
    +----------------------------------------------------------------------------+
    ```

2. Select **Cumulus Linux GNU/Linux, with Linux 4.19.0-cl-1-amd64 (recovery mode)**.

    ```
                    GNU GRUB  version 2.02+dfsg1-20

    +----------------------------------------------------------------------------+
    | Cumulus Linux GNU/Linux, with Linux 4.19.0-cl-1-amd64                       |
    |*Cumulus Linux GNU/Linux, with Linux 4.19.0-cl-1-amd64 (recovery mode)       |
    |                                                                            |
    +----------------------------------------------------------------------------+  
    ```

4. Press ctrl-d to reboot.
5. After the system reboots, set a new **root** password. The root user provides complete control over the switch.

    ```
    root@switch:~# passwd
    Enter new UNIX password:
    Retype new UNIX password:
    passwd: password updated successfully
    ```

    You can take this opportunity to reset the password for the *cumulus* account.

    ```
    root@switch:~# passwd cumulus
    Enter new UNIX password:
    Retype new UNIX password:
    passwd: password updated successfully
    ```

6. Sync the `/etc` directory, then reboot the system:

    ```
    root@switch:~# sync
    root@switch:~# reboot -f
    Restarting the system.
    ```
