---
title: User Accounts
author: Cumulus Networks
weight: 217
aliases:
 - /display/CL25ESR/User+Accounts
 - /pages/viewpage.action?pageId=5115902
pageID: 5115902
product: Cumulus Linux
version: 2.5.12 ESR
imgData: cumulus-linux-2512-esr
siteSlug: cumulus-linux-2512-esr
---
By default, Cumulus Linux has two user accounts: *cumulus* and *root*.

The *cumulus* account:

  - 
    
    <div id="src-5115902_indexterm-A462AF86BE7C4D2CE05BD6109EBFE723">
    
    Default password is *CumulusLinux\!*
    
    </div>

  - Is a user account in the *sudo* group with sudo privileges

  - User can log in to the system via all the usual channels like
    console and
    [SSH](/version/cumulus-linux-2512-esr/System_Management/Authentication_Authorization_and_Accounting/SSH_for_Remote_Access)

The *root* account:

  - Default password is disabled by default

  - Has the standard Linux root user access to everything on the switch

  - Disabled password prohibits login to the switch by SSH, telnet, FTP,
    and so forth

For best security, you should change the default password (using the
`passwd` command) before you configure Cumulus Linux on the switch.

You can enable a valid password for the root account using the `sudo
passwd root` command and can install an SSH key for the root account if
needed. Enabling a password for the root account allows the root user to
log in directly to the switch. The Cumulus Linux default root account
behavior is consistent with Debian.

You can add more user accounts as needed. Like the *cumulus* account,
these accounts must use `sudo` to [execute privileged
commands](/version/cumulus-linux-2512-esr/System_Management/Authentication_Authorization_and_Accounting/Using_sudo_to_Delegate_Privileges),
so be sure to include them in the *sudo* group.

To access the switch without any password requires booting into a single
shell/user mode. [Here are the
instructions](/version/cumulus-linux-2512-esr/Monitoring_and_Troubleshooting/Single_User_Mode_-_Boot_Recovery)
on how to do this using PowerPC and x86 switches.
