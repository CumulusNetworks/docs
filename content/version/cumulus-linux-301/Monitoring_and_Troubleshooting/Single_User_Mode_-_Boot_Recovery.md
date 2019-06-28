---
title: Single User Mode - Boot Recovery
author: Cumulus Networks
weight: 163
aliases:
 - /display/CL30/Single+User+Mode+-+Boot+Recovery
 - /pages/viewpage.action?pageId=5118243
pageID: 5118243
product: Cumulus Linux
version: '3.0'
imgData: cumulus-linux-301
siteSlug: cumulus-linux-301
---
Use single user mode to assist in troubleshooting system boot issues or
for password recovery. Entering single user mode is
[platform-specific](http://cumulusnetworks.com/hcl/), so follow the
appropriate steps for your x86 or ARM switch.

## <span>Entering Single User Mode on an x86 Switch</span>

1.  Boot the switch, as soon as you see the GRUB menu.
    
    ``` 
                           GNU GRUB  version 2.02~beta2-22+deb8u1
    
     +----------------------------------------------------------------------------+
     |*Cumulus Linux GNU/Linux                                                    | 
     | Advanced options for Cumulus Linux GNU/Linux                               |
     | ONIE                                                                       |
     |                                                                            |
     +----------------------------------------------------------------------------+     
    ```

2.  Use the ^ and v arrow keys to select **Advanced options for Cumulus
    Linux GNU/Linux**. A menu similar to the following should appear:
    
    ``` 
                           GNU GRUB  version 2.02~beta2-22+deb8u1
    
     +----------------------------------------------------------------------------+
     | Cumulus Linux GNU/Linux, with Linux 4.1.0-cl-1-amd64                       | 
     | Cumulus Linux GNU/Linux, with Linux 4.1.0-cl-1-amd64 (sysvinit)            |
     |*Cumulus Linux GNU/Linux, with Linux 4.1.0-cl-1-amd64 (recovery mode)       |
     |                                                                            |
     +----------------------------------------------------------------------------+    
    ```

3.  Select **Cumulus Linux GNU/Linux, with Linux 4.1.0-cl-1-amd64
    (recovery mode)**.

4.  Press ctrl-x to reboot.

5.  After the system reboots, set a new password.
    
        # passwd
        Enter new UNIX password: 
        Retype new UNIX password: 
        passwd: password updated successfully

6.  Reboot the system:
    
    ``` 
    # sync
    # reboot -f
    Restarting the system.    
    ```

## <span>Entering Single User Mode on an ARM Switch</span>

1.  From the console, boot the switch, interrupting the U-Boot countdown
    to enter the U-Boot prompt. Enter the following:
    
        => setenv lbootargs init=/bin/bash  
        => boot

2.  After the system boots, the shell command prompt appears. In this
    mode, you can change the root password or test a boot service that
    is hanging the boot process.
    
        # passwd
        Enter new UNIX password: 
        Retype new UNIX password: 
              passwd: password updated successfully

3.  Reboot the system.
    
        cumulus@switch:~$ sudo sync
        cumulus@switch:~$ sudo reboot -f  
        Restarting the system.
