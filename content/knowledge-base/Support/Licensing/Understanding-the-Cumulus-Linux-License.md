---
title: Understanding the Cumulus Linux License
author: Cumulus Networks
weight: 611
toc: 4
---

The Cumulus Linux license has a simple format. Managing your license keys is very easy, as you can use the same license file for all your licensed Cumulus Linux switches.

In addition, there is no need to replace the license file when you renew or purchase additional licenses.

From a technical standpoint, the license has changed as follows:

- Increased messaging volume, which is displayed on screen when you log into the switch, and is written to `syslog`.
- New messaging when `switchd` detects a missing or invalid license.  

The license format looks like this:

    user@company.com|thequickbrownfoxjumpsoverthelazydog312

You manage your licenses in the MyMellanox {{<exlink url="https://support.mellanox.com/s/login/" text="customer portal">}}.

To verify that your license is installed, run the `cl-license` command.

    cumulus@switch:~$ cl-license
    user@example.com|$ampleL1cen$et3xt

For more information on the use of `cl-license`, please refer to the
{{<kb_link url="cumulus-linux-43/Quick-Start-Guide/" text="Quick Start Guide">}}.

To check the version of Cumulus Linux you are running, {{<link url="Verify-Software-and-Hardware-Version-Information" text="read this article">}}.
