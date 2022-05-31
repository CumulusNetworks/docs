---
title: Understanding the Cumulus Linux License
author: Cumulus Networks
weight: 611
toc: 4
---

The Cumulus Linux license has a simple format. Managing your license keys is very easy, as you can use the same license file for all your licensed Cumulus Linux switches.

In addition, there is no need to replace the license file when you renew or purchase additional licenses.

From a technical standpoint, the license changed as follows:

- Increased messaging volume, which displays on screen when you log into the switch; Cumulus Linux writes the messages to `syslog`.
- New messaging when `switchd` detects a missing or invalid license.  

The license format looks like this:

    user@company.com|thequickbrownfoxjumpsoverthelazydog312

You manage your licenses in the {{<exlink url="NVIDIA Enterprise supoport portal" text="NVIDIA Enterprise supoport portal">}}.

To verify that you installed your license, run the `cl-license` command.

    cumulus@switch:~$ cl-license
    user@example.com|$ampleL1cen$et3xt

For more information on the use of `cl-license`, refer to the [Quick Start Guide]({{<ref "/cumulus-linux-43/Quick-Start-Guide" >}}).

To check the version of Cumulus Linux you are running, {{<link url="Verify-Software-and-Hardware-Version-Information" text="read this article">}}.
