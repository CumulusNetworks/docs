---
title: Single User Mode - Boot Recovery
author: Cumulus Networks
weight: 153
aliases:
 - /display/CL25ESR/Single+User+Mode+-+Boot+Recovery
 - /pages/viewpage.action?pageId=5115975
pageID: 5115975
product: Cumulus Linux
version: 2.5.12 ESR
imgData: cumulus-linux-2512-esr
siteSlug: cumulus-linux-2512-esr
---
Use single user mode to assist in troubleshooting system boot issues or
for password recovery. Entering single user mode is
[platform-specific](http://cumulusnetworks.com/hcl/), so follow the
appropriate steps for your x86, ARM or PowerPC switch.

## <span>Entering Single User Mode on an x86 Switch</span>

1.  Boot the switch, as soon as you see the GRUB menu, use the ^ and v
    arrow keys to select the boot entry you wish to modify, then press
    *e* to edit the entry. Be careful to select the correct image slot,
    so that the password change is applied correctly to the slot you
    desire. The active slot is the first selected image when the GRUB
    menu appears.
    
    ``` 
                           GNU GRUB  version 1.99-27+deb7u2
    
     +--------------------------------------------------------------------------+
     |Cumulus Linux 2.5.5-4cd66d9-201512071810-build - slot 1                   | 
     |Cumulus Linux 2.5.5-4cd66d9-201512071810-build - slot 1 (recovery mode)   |
     |Cumulus Linux 2.5.3-c4e83ad-201506011818-build - slot 2                   |
     |Cumulus Linux 2.5.3-c4e83ad-201506011818-build - slot 2 (recovery mode)   |
     |ONIE                                                                      |
     |                                                                          |
     |                                                                          |
     |                                                                          |
     |                                                                          |
     |                                                                          |
     |                                                                          |
     |                                                                          | 
     +--------------------------------------------------------------------------+
    
          Use the ^ and v keys to select which entry is highlighted.      
          Press enter to boot the selected OS, 'e' to edit the commands      
          before booting or 'c' for a command-line.      
    ```

2.  After pressing *e*, a menu similar to the following should appear:
    
    ``` 
                          GNU GRUB  version 1.99-27+deb7u2
    
     +--------------------------------------------------------------------------+
     | setparams 'Cumulus Linux 2.5.5-4cd66d9-201512071810-build - slot 1'      | 
     |                                                                          |
     | insmod gzio                                                              |
     | insmod part_gpt                                                          |
     | insmod ext2                                                              |
     | set root='(hd0,gpt4)'                                                    |
     | search --no-floppy --fs-uuid --set=root 23ea9c70-6d9f-414e-a26a-c501608\ |
     | d3c3a                                                                    |
     | echo 'Loading Linux  ...'                                                |
     | linux /cl-vmlinuz-3.2.68-6-slot-1 root=UUID=07197d9c-7dd7-407a-8cbc-4ff\ |
     | 1084b6337 console=ttyS1,115200n8 cl_platform=dell_s3000_c2338 quiet act\ |
     | ive=1                                                                    |v
     +--------------------------------------------------------------------------+
    
          Minimum Emacs-like screen editing is supported. TAB lists      
          completions. Press Ctrl-x or F10 to boot, Ctrl-c or F2 for      
          a command-line or ESC to discard edits and return to the GRUB menu.
    ```

3.  Scroll down to the line that starts with "linux" and add
    *init=/bin/bash* to the end of the line. This allows the system to
    boot into single user mode.
    
    ``` 
                           GNU GRUB  version 1.99-27+deb7u2
    
     +--------------------------------------------------------------------------+
     |                                                                          |^
     | insmod gzio                                                              |
     | insmod part_gpt                                                          |
     | insmod ext2                                                              |
     | set root='(hd0,gpt4)'                                                    |
     | search --no-floppy --fs-uuid --set=root 23ea9c70-6d9f-414e-a26a-c501608\ |
     | d3c3a                                                                    |
     | echo 'Loading Linux  ...'                                                |
     | linux /cl-vmlinuz-3.2.68-6-slot-1 root=UUID=07197d9c-7dd7-407a-8cbc-4ff\ |
     | 1084b6337 console=ttyS1,115200n8 cl_platform=dell_s3000_c2338 quiet act\ |
     | ive=1 init=/bin/bash                                                     |
     | echo 'Loading initial ramdisk ...'                                       |v
     +--------------------------------------------------------------------------+
    
          Minimum Emacs-like screen editing is supported. TAB lists      
          completions. Press Ctrl-x or F10 to boot, Ctrl-c or F2 for      
          a command-line or ESC to discard edits and return to the GRUB menu.
    ```

4.  Press ctrl-x to reboot.

5.  After the system reboots, re-mount the partition as read/write and
    set a new password.
    
        # mount -o remount,rw /
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

## <span>Entering Single User Mode on a PowerPC Switch</span>

1.  From the console, boot the switch, interrupting the U-Boot countdown
    to enter the U-Boot prompt. Enter the following:
    
        => setenv lbootargs init=/bin/bash  
        => boot

2.  After the system boots, the shell command prompt appears. Set the
    root password:
    
        # passwd  
        Enter new UNIX password:  
        Retype new UNIX password:  
        passwd: password updated successfully

3.  Reboot the system.
    
        cumulus@switch:~$ sudo sync
        cumulus@switch:~$ sudo reboot -f  
        Restarting the system.

## <span>Entering Single User Mode on an ARM Switch</span>

1.  From the console, boot the switch, interrupting the U-Boot countdown
    to enter the U-Boot prompt. Enter the following:
    
        => setenv bootargs single  
        => boot

2.  After the system boots, the shell command prompt appears. In this
    mode, you can change the root password or test a boot service that
    is hanging the boot process.
    
        Welcome to rescu
        root@cumulus:~# passwd
        Enter new UNIX password: 
        Retype new UNIX password: 
        passwd: password updated successfully

3.  Reboot the system.
    
        root@cumulus:~# sync
        root@cumulus:~# reboot -f  
        Restarting the system.
