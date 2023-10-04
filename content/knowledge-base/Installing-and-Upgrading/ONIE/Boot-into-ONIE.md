---
title: Boot into ONIE
author: NVIDIA
weight: 271
toc: 4
---

## Issue
<!-- vale off -->
I already have Cumulus Linux running but I want to boot back into {{<exlink url="https://opencomputeproject.github.io/onie/" text="ONIE">}} for troubleshooting/installation issues.
<!-- vale on -->
You use ONIE (the Open Network Install Environment) to [install Cumulus Linux]({{<ref "/cumulus-linux-43/Quick-Start-Guide" >}}) on open networking switches.

## Environment

- Cumulus Linux, all versions

## Resolution

1. Log in to your switch via the [console]({{<ref "/cumulus-linux-43/Quick-Start-Guide/#serial-console-management" >}}).

1. Reboot the switch:

       cumulus@switch~:# sudo reboot

1. Press any key when you see the following prompt:

       Hit any key to stop autoboot:  0

1. **ARM switches only:** The switch now boots into U-Boot.  

       switch-> version
        
       U-Boot 2013.01.01-g1f891da (Sep 23 2013 - 18:31:29)
       ONIE 1.6.5
       powerpc-linux-gcc (GCC) 4.7.2
       GNU ld (GNU Binutils) 2.22
       switch->
       switch->

   To boot into ONIE install mode, type the following commands:

       -> setenv onie_boot_reason install
       -> run bootcmd

   {{%notice note%}}
Install mode automatically starts trying to install a switch binary (like Cumulus Linux). If it keeps booting into Cumulus Linux and you just want to get to the ONIE prompt, use rescue mode instead:

    -> setenv onie_boot_reason rescue
    -> run bootcmd
{{%/notice%}}

1. Select _ONIE_ from the GRUB menu, then press _Enter_ to access the ONIE console.

                               GNU GRUB  version 2.02-cl3u3
       +----------------------------------------------------------------------------+
       | Cumulus Linux GNU/Linux                                                    | 
       | Advanced options for Cumulus Linux GNU/Linux                               |
       | Load a read-only snapshot                                                  |
       |*ONIE                                                                       |
       | ACCTON-DIAG                                                                |
       |                                                                            |
       |                                                                            |
       |                                                                            |
       |                                                                            |
       |                                                                            |
       |                                                                            |
       |                                                                            | 
       +----------------------------------------------------------------------------+
            Use the ^ and v keys to select which entry is highlighted.          
            Press enter to boot the selected OS, `e' to edit the commands       
            before booting or `c' for a command-line.                           
         The highlighted entry will be executed automatically in 4s.   

1. Select the ONIE mode to use then press _Enter_.

                                 GNU GRUB  version 2.02~beta3
       +----------------------------------------------------------------------------+
       | ONIE: Install OS                                                           |
       |*ONIE: Rescue                                                               |
       | ONIE: Uninstall OS                                                         |
       | ONIE: Update ONIE                                                          |
       | ONIE: Embed ONIE                                                           |
       | ACCTON-DIAG                                                                |
       |                                                                            |
       |                                                                            |
       |                                                                            |
       |                                                                            |
       |                                                                            |
       |                                                                            |
       +----------------------------------------------------------------------------+
            Use the ^ and v keys to select which entry is highlighted.          
            Press enter to boot the selected OS, `e' to edit the commands       
            before booting or `c' for a command-line.                           
        The highlighted entry will be executed automatically in 1s.                 

1. The ONIE prompt appears.

       ONIE:/ #
