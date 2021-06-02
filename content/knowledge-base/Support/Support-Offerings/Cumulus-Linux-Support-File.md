---
title: Cumulus Linux Support File
author: Cumulus Networks
weight: 707
toc: 4
---

Cumulus Linux generates support files called `cl-support` whenever issues are detected. 

This file is used to aid in troubleshooting customer issues. The Cumulus Networks global support staff often requests customers to provide this file when they open support tickets. 

The `cl-support` file is located in the `/var/support` directory and is named `cl_support_xxx.txz`.

There are three ways `cl-support` is generated:

- If `switchd` or any other process generates a core file (located in `/var/support/core`), then the `cl-support` file is generated.
- After the first failure of one of the following monitored services since the switch was rebooted or power cycled:
    - clagd
    - frr
    - openvswitch-vtep
    - portwd
    - ptmd
    - rdnbrd
    - switchd
    - vxrd
    - vxsnd
- A `cl-support` file can be triggered by issuing the `cl-support` command.

  {{%notice info%}}
  
You should only run this command at the direction of a  member of the Cumulus Networks support staff.

{{%/notice%}}

If you need to copy the `cl-support` file off of the switch to a remote host for collection, use `scp`:

    cumulus@switch:~$ scp /var/support/ username@myserver:/path/
