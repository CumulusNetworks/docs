---
title: Single User Mode - Boot Recovery
author: Cumulus Networks
weight: 103
aliases:
 - /display/RMP31/Single+User+Mode+-+Boot+Recovery
 - /pages/viewpage.action?pageId=5122762
pageID: 5122762
product: Cumulus RMP
version: 3.1.2
imgData: cumulus-rmp-312
siteSlug: cumulus-rmp-312
---
Use single user mode to assist in troubleshooting system boot issues or
for password recovery.

## <span>Entering Single User Mode</span>

1.  Boot the switch, as soon as you see the GRUB menu.
    
    ``` 
                           GNU GRUB  version 2.02~beta2-22+deb8u1
     
     +----------------------------------------------------------------------------+
     |*Cumulus RMP GNU/Linux                                                      | 
     | Advanced options for Cumulus RMP GNU/Linux                                 |
     | ONIE                                                                       |
     |                                                                            |
     +----------------------------------------------------------------------------+     
    ```

2.  Use the ^ and v arrow keys to select **Advanced options for Cumulus
    RMP GNU/Linux**. A menu similar to the following should appear:
    
    ``` 
                           GNU GRUB  version 2.02~beta2-22+deb8u1
     
     +----------------------------------------------------------------------------+
     | Cumulus RMP GNU/Linux, with Linux 4.1.0-cl-1-amd64                         | 
     | Cumulus RMP GNU/Linux, with Linux 4.1.0-cl-1-amd64 (sysvinit)              |
     |*Cumulus RMP GNU/Linux, with Linux 4.1.0-cl-1-amd64 (recovery mode)         |
     |                                                                            |
     +----------------------------------------------------------------------------+    
    ```

3.  Select **Cumulus RMP GNU/Linux, with Linux 4.1.0-cl-1-amd64
    (recovery mode)**.

4.  Press ctrl-x to reboot.

5.  After the system reboots, set a new password.
    
        # passwd
        Enter new UNIX password: 
        Retype new UNIX password: 
        passwd: password updated successfully

6.  Reboot the system:
    
        # sync
        # reboot -f
        Restarting the system.
