---
title: Cumulus Linux Support File
author: NVIDIA
weight: 707
toc: 4
---

Cumulus Linux generates support files called `cl-support` whenever it detects issues.

This file aids in troubleshooting customer issues. The NVIDIA Enterprise Support team often requests customers to provide this file when they open support tickets.

The `cl-support` command names the file `cl_support_xxx.txz` and writes it to the `/var/support` directory.

You can generate `cl-support` in one of three ways:

- If `switchd` or any other process generates a core file (located in `/var/support/core`), then Cumulus Linux generates the `cl-support` file.
- After the first failure of one of the following monitored services after a switch reboot or power cycling:
    - clagd
    - frr
    - openvswitch-vtep
    - portwd
    - ptmd
    - rdnbrd
    - switchd
    - vxrd
    - vxsnd
- You can trigger creation of a `cl-support` file by running the `cl-support` command.

  {{%notice info%}}
  
You should only run this command at the direction of a member of the NVIDIA support staff.

{{%/notice%}}

If you need to copy the `cl-support` file off of the switch to a remote host for collection, use `scp`:

    cumulus@switch:~$ scp /var/support/ username@myserver:/path/
