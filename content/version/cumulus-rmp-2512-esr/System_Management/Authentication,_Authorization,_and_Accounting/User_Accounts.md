---
title: User Accounts
author: Cumulus Networks
weight: 115
aliases:
 - /display/RMP25ESR/User+Accounts
 - /pages/viewpage.action?pageId=5116312
pageID: 5116312
product: Cumulus RMP
version: 2.5.12 ESR
imgData: cumulus-rmp-2512-esr
siteSlug: cumulus-rmp-2512-esr
---
By default, Cumulus RMP has two user accounts: *root* and *cumulus*.

The *cumulus* account:

  - Default password is *CumulusLinux\!*

  - Is a user account in the *sudo* group with sudo privileges

  - User can log in to the system via all the usual channels like
    console and
    [SSH](/version/cumulus-rmp-2512-esr/System_Management/Authentication_Authorization_and_Accounting/SSH_for_Remote_Access)

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
these accounts must use sudo to [execute privileged
commands](/version/cumulus-rmp-2512-esr/System_Management/Authentication_Authorization_and_Accounting/Using_sudo_to_Delegate_Privileges),
so be sure to include them in the *sudo* group.

To access the switch without any password requires booting into a single
shell/user mode. [Here are the
instructions](/version/cumulus-rmp-2512-esr/Monitoring_and_Troubleshooting/Single_User_Mode_-_Boot_Recovery)
on how to do this using PowerPC and x86 switches.
