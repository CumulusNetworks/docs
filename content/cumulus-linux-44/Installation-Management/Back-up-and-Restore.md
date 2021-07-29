---
title: Back up and Restore
author: NVIDIA
weight: 70
toc: 3
---
You can back up the current configuration on a switch and restore the configuration on the **same switch** or on another Cumulus Linux switch of the **same type and release**. The backup is a compressed tar file that includes all configuration files installed by Debian packages and marked as configuration files. In addition, the backup contains files in the `/etc` directory that are not installed by a Debian package but are modified when you install a new image or enable/disable certain services (such as the Cumulus license file).

Cumulus Linux automatically creates a backup of the configuration files on the switch after you install the Cumulus Linux image, in case you want to return to the initial switch configuration. NCLU automatically
creates a backup of the configuration files when you run the `net commit` command and restores a previous configuration when you run the `net rollback` command.

{{%notice note%}}
NVUE does not use backup and restore. See {{<link url="NVIDIA-User-Experience-NVUE" text="NVIDIA User Experience - NVUE">}} for information about backing up and restoring NVUE configuration files.
{{%/notice%}}

## Back up Configuration Files

To back up the current configuration files on the switch, run the `config-backup` command:

```
cumulus@switch:~$ sudo config-backup
```

If you run this command without any options, Cumulus Linux creates a backup of the current configuration and stores the backup file in the `/var/lib/config-backup/backups` directory. The filename includes the date and time you run the backup, and the switch name; for example, `config_backup-2019-04-23-21.30.47_leaf01`. You can restore the backup with the `config-restore` command, described below.

The switch can store up to 30 *non-permanent* backup files (a maximum of 25 MB of disc space) in addition to the permanent backup files (see the `-p` option below). When this limit is reached, Cumulus Linux keeps the oldest and the newest backup files, then starts removing the second oldest file up to the second newest file.

{{%notice note%}}

Cumulus Linux recommends you copy the backup file off the switch after backup is complete.

{{%/notice%}}

The `config-backup` command includes the following options:

|Option|Description|
|--- |--- |
|`-h`|Displays this list of command options.|
|`-d`|Enables debugging output, which shows status messages during the backup process.|
|`-D <description>`|Adds a description, which is shown in the archive file list when you run the `config-restore -l` command.|
|`-p`|Adds -perm to the end of the backup filename to mark it as permanent. For example, `config_backup-2019-04-23-21.30.47_leaf01-perm`. Be careful when using this option. Permanent backup files are not removed.|
|`-q`|Runs the command in quiet mode. No status messages are shown, only errors.|
|`-t <type>`|Specifies the type of configuration, which is shown in the archive file list when you run the `config-restore -l` command. You can provide any short text. For example, you can specify `pre`, `post`, or `pre-restore`.|
|`-v`|Enables verbose mode to show messages during the backup process.|
|`-X <pattern>`|Excludes certain files that match a specified pattern. For example, to exclude all backup files ending with a tilde (~), use the `-X .*~$` option.|
<!-- vale off -->
### config-backup Command Examples
<!-- vale on -->
The following command example creates a backup file in debugging mode and provides the description `myconfig`, which shows in the backup archive list.

```
cumulus@switch:~$ sudo config-backup -d -D myconfig 
```

The following command example creates a backup file in quiet mode and excludes files that end in a tilde (\~).

```
cumulus@switch:~$ sudo config-backup -q -X .*~$
```

The following command example creates a backup file in verbose mode and marks the file as permanent.

```
cumulus@switch:~$ sudo config-backup -pv
```

## Restore Backup Files

You can restore a backup to the same switch or to a different switch. When restoring to a different switch, the switch must be of the **same type and release**. For example, you can restore a backup from a Broadcom Trident3 switch to a Broadcom Trident3 switch; however, you cannot restore a backup from a Broadcom Trident3 switch to an NVIDIA Spectrum or to a Broadcom Tomahawk2 switch.

To restore a backup file, run the `config-restore` command with a specific filename (`-b <filename>`), file number (`-n <number>`), *or* the `-N` option, which restores the most recent backup file.

You can run the `config-restore -l` command to list the archived backup files by filename and number (see {{<link url="#config-restore-command-examples" text="config-restore Command Examples">}} below).

```
cumulus@switch:~$ sudo config-restore -b config_backup-2019-04-23-21.30.47_leaf01
cumulus@switch:~$ sudo config-restore -n 10
cumulus@switch:~$ sudo config-restore -N
```

After the backup file is restored successfully, you are prompted to restart any affected services or reboot the switch if necessary.

Cumulus Linux reports any issues encountered during restore and prompts you to continue or stop.

{{%notice note%}}

- The `config-restore` command *requires* a filename, file number, or the most recent file option (`-N`).
- You can only run one `config-backup` or `config-restore` command instance at the same time.

{{%/notice%}}

The `config-restore` command includes the following options:

|Option|Description|
|--- |--- |
|`-h`|Displays this list of command options.|
| `-a <directory>`|Restores the backup to the directory specified.|
| `-B`| Runs *no* backup before restoring the configuration. If you do *not* specify this option, Cumulus Linux runs a backup to save the current configuration before the restore so that you can do a rollback if needed.|
| `-b <filename>`| Specifies the name of the backup file you want to restore (shown by `-l`).|
| `-D`| Shows the differences between the current configuration and the configuration in the backup file.|
| `-d`| Displays debugging output, which provides status messages during the restore process.|
| `-f`| Forces the restore; does not prompt for confirmations.|
| `-F <filename>`| Shows differences for only this file (used with -D).|
| `-i`| Displays information about the current backup file.|
| `-L`| Lists the configuration files in the backup file.|
| `-l`| Lists all backup files archived on the switch and includes the file number, type, and description.|
| `-N`| Restores the newest (most recent) backup file.|
| `-n <number>`| Specifies the backup file by number (shown by `-l`).|
| `-q`|Runs the command in quiet mode. No status messages are displayed, only errors.|
| `-T`| Runs the command in test mode; does not restore the configuration but shows what would be restored.|
| `-v`| Enables verbose mode to display status messages during restore.|
<!-- vale off -->
### config-restore Command Examples
<!-- vale on -->
The following command example lists the backup files available on the switch. The list includes the file number (\#), type, description, and filename. Type is the text specified with the `config-backup -t` option.

```
cumulus@switch:~$ sudo config-restore -l
# Type       Description               Name
1 Initial    First system boot         config_backup-2019-04-23-00.42.11_cumulus-perm
2 Initial    First system boot         config_backup-2019-04-23-00.47.43_cumulus-perm
3 Initial    First system boot         config_backup-2019-04-23-18.12.26_cumulus-perm
4 pre nclu "net commit" (user cumulus) config_backup-2019-04-23-19.55.13_leaf01
5 post-4     nclu "net commit" (user cumulus)   config_backup-2019-04-23-19.55.26_leaf01
6            config_backup-2019-04-23-21.20.41_leaf01
7            config_backup-2019-04-23-21.30.47_leaf01-perm
...
```

The following command example runs in verbose mode to restore the backup file `config_backup-2019-04-23-21.30.47_leaf01`.

```
cumulus@switch:~$ sudo config-restore -v -b config_backup-2019-04-23-21.30.47_leaf01
```

The following command example runs test mode to restore the most recent backup file (no configuration is actually restored).

```
cumulus@switch:~$ sudo config-restore -T -N
```

The following command example lists the files in the most recent backup file.

```
cumulus@switch:~$ sudo config-restore -L -N
```
