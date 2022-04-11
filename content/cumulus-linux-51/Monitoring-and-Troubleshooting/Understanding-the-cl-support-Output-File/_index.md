---
title: Understanding the cl-support Output File
author: NVIDIA
weight: 1050
toc: 3
---
The `cl-support` script generates a compressed archive file of useful information for troubleshooting. The system either creates the archive file automatically or you can create the archive file manually.
<!-- vale off -->
## Automatic cl-support File
<!-- vale on -->
The system creates the `cl-support` archive file automatically for the following reasons:

- When there is a {{<exlink url="http://linux.die.net/man/5/core" text="core dump file">}} for any application (not specific to Cumulus Linux, but something all Linux distributions support), located in `/var/support/core`.
- When one of the monitored services fails for the first time after you reboot or power cycle the switch.
<!-- vale off -->
## Manual cl-support File
<!-- vale on -->
To create the `cl-support` archive file manually, run the `cl-support` command:

```
cumulus@switch:~$ sudo cl-support
```

If the Cumulus Linux support team requests that you submit the output from `cl-support` to investigate issues you experience and you need to include security-sensitive information, such as the `sudoers` file, use the `-s` option:

```
cumulus@switch:~$ sudo cl-support -s
```

For information on the directories included in the `cl-support` archive, see:
- {{<link url="Troubleshooting-the-etc-Directory">}}. The `/etc` directory contains the largest number of files.
- {{<link url="Troubleshooting-Log-Files">}}. This guide highlights the most important log files to inspect. Keep in mind, `cl-support` includes all log files.
