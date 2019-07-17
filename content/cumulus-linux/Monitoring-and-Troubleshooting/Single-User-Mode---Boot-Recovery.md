---
title: Single User Mode - Boot Recovery
author: Cumulus Networks
weight: 2159
aliases:
 - /display/CL3740/Single-User-Mode---Boot-Recovery
 - /pages/viewpage.action?pageId=83626066327
pageID: 83626066327
product: Cumulus Linux
version: 3.7.7'4.0'
imgData: cumulus-linux-37740
siteSlug: cumulus-linux-37740
---
Use single user mode to assist in troubleshooting system boot issues or
for password recovery. To enter single user mode, follow the steps
below.

1.  Boot the switch as soon as you see the GRUB menu.
    
    ``` 
                           GNU GRUB  version 2.02-cl3u3
     
     +----------------------------------------------------------------------------+
     |*Cumulus Linux GNU/Linux                                                    | 
     | Advanced options for Cumulus Linux GNU/Linux                               |
     | ONIE                                                                       |
     |                                                                            |
     +----------------------------------------------------------------------------+     
    ```

2.  Use the ^ and v arrow keys to select **Advanced options for Cumulus
    Linux GNU/Linux**. A menu similar to the following should appears:
    
    ``` 
                           GNU GRUB  version 2.02-cl3u3
     
     +----------------------------------------------------------------------------+
     | Cumulus Linux GNU/Linux, with Linux 4.1.0-cl-7-amd64                       | 
     |*Cumulus Linux GNU/Linux, with Linux 4.1.0-cl-7-amd64 (recovery mode)       |
     |                                                                            |
     +----------------------------------------------------------------------------+  
    ```

3.  Select **Cumulus Linux GNU/Linux, with Linux 4.1.0-cl-71-amd64
    (recovery mode)**.

4.  Press ctrl-x to reboot.

5.  After the system reboots, set a new **root** password. This is
    useful since the root user provides complete control over the
    switch, and providing a new password now helps in case the current
    password has been forgotten, which is a common problem.
    
        root@switch:~# passwd
        Enter new UNIX password: 
        Retype new UNIX password: 
        passwd: password updated successfully
    
    {{%notice tip%}}
    
    You may want to take this opportunity to reset the password for the
    *cumulus* account as well.
    
        root@switch:~# passwd cumulus
        Enter new UNIX password: 
        Retype new UNIX password: 
        passwd: password updated successfully
    
    {{%/notice%}}

6.  Sync the `/etc` directory using `btrfs`, then reboot the system:
    
        root@switch:~# btrfs filesystem sync /etc
        root@switch:~# reboot -f
        Restarting the system. 

<article id="html-search-results" class="ht-content" style="display: none;">

</article>

<footer id="ht-footer">

</footer>
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTU5NjQ1OTc5NF19
-->