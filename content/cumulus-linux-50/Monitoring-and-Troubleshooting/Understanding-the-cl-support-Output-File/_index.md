---
title: Understanding the cl-support Output File
author: NVIDIA
weight: 1050
toc: 3
---
The `cl-support` script generates a compressed archive file of useful information for troubleshooting. The system either creates the archive file automatically or you can create the archive file manually.

## Automatic cl-support File

The system creates the `cl-support` archive file automatically for the following reasons:

- When there is a {{<exlink url="http://linux.die.net/man/5/core" text="core file dump">}} of any application (not specific to Cumulus Linux, but something all Linux distributions support), located in `/var/support/core`.
- After the first failure of one of several monitored services since the switch was rebooted or power cycled.

## Manual cl-support File

To create the `cl-support` archive file manually, run the `cl-support` command:

```
cumulus@switch:~$ sudo cl-support
```

If the Cumulus Linux support team requests that you submit the output from `cl-support` to help with the investigation of issues you might experience with Cumulus Linux and you need to include security-sensitive information, such as the `sudoers` file, use the `-s` option:

```
cumulus@switch:~$ sudo cl-support -s
```

{{%notice note%}}

On ARM switches, the cl-support FRR module might time out even when FRR is not running. To disable the timeout, run the `cl-support` command with the `-M` option; for example:

```
cumulus@switch:~$ sudo cl-support -M
```

{{%/notice%}}

For information on the directories included in the `cl-support` archive, see:

- {{<link url="Troubleshooting-the-etc-Directory">}}. The `/etc` directory contains the largest number of files; however, log files might be significantly larger in file size.
- {{<link url="Troubleshooting-Log-Files">}}. This guide highlights the most important log files to inspect. Keep in mind, `cl-support` includes all of the log files.
