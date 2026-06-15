---
title: Automatic Configuration Backup
author: NVIDIA
weight: 82
toc: 3
---

Cumulus Linux provides an automatic configuration backup feature that takes snapshots each time the `nv config apply` command runs successfully. The switch also takes a snapshot weekly to ensure that at least one valid weekly snapshot is available, subject to disk space and backup success.

The switch stores the snapshots in the `/var/lib/nvue/backup/applied` directory and the weekly snapshots in the `/var/lib/nvue/backup/weekly/` directory. When you reach the maximum storage limit of 512 MiB, the switch deletes the oldest snapshots and logs the deleted snapshots.

{{%notice note%}}
- Root owns the snapshot directories; you can view the directories only if you have root privileges.
- The snapshots contain potentially sensitive configuration details such as certificates, interface IDs and routing configuration, services and IP addresses.
- If the `nv config apply` command fails verification, exits on warning prompts, or rolls back due to a `--confirm` timeout, the automatic configuration backup does not run.
{{%/notice%}}

## Enable Automatic Configuration Backup

Automatic configuration backup is disabled by default. To enable automatic configuration backup, run the `nv system config backup state enabled` command:

```
cumulus@switch:~$ nv set system config backup state enabled
cumulus@switch:~$ nv config apply
```

To disable automatic configuration backup, run the `nv system config backup state disabled` command.

## Restore a Snapshot

To restore a snapshot, identify the snapshot you want to restore by inspecting the `/var/lib/nvue/backup/applied/` directory or the `/var/lib/nvue/backup/weekly/` directory, then run the `nv action system config backup restore <snapshot-id>` command.

```
cumulus@switch:~$ nv action system config backup restore /var/lib/nvue/backup/weekly/weekly-20260320-121030
```

The configuration restore process triggers a controlled reboot so that all relevant services and daemons restart with the restored configuration.

## Backup and Restore Errors

If the backup or restore fails, you see errors.

### Configuration Backup Errors

If the automatic configuration backup results in failure, the `nv config apply` command completes; however, you cannot retry the configuration backup with the same `nv config apply` command.

If the weekly automatic configuration backup results in failure, the error is recorded in the logs and the next scheduled run proceeds normally. To view the logs, run the `journalctl -u nvue-config-backup-weekly.service` command.

If the automatic configuration backup reports insufficient space, the switch deletes the oldest snapshots. If the there is still a failure, the switch logs the error and skips the snapshot.

### Configuration Restore Errors

If you encounter an error when restoring a snapshot, inspect the logs and attempt to restore another snapshot.
