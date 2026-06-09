---
title: System Snapshots
author: NVIDIA
weight: 297
toc: 3
---
Cumulus Linux provides commands to manage system configuration snapshots. You can configure the switch to take snapshots after every successful `nv config apply` command and schedule the switch to take weekly snapshots.

The switch stores all configuration snapshots in the `/var/lib/config-backup/auto-snapshots` directory, enforcing an internal storage capacity limit by automatically pruning old backups. The snapshot names are in the format `config_backup-YYYYMMDD-HHMMSS_cumulus`; for example, `config_backup-2026-05-19-11.54.59_cumulus`.

You can restore a configuration snapshot on the switch.

## Enable Automatic Snapshot Collection

To enable automatic snapshot collection, run the `nv action system config backup state enabled` command:

```
cumulus@switch:~$ nv action system config backup state enabled
```

When enabled, the switch takes automatic snapshots after every successful `nv config apply` command and stores the snapshots in the `/var/lib/config-backup/auto-snapshots/applied` directory.

To disable automatic snapshot collection, run the `nv action system config backup state disabled` command. When disabled, the switch does not create any new snapshots.

## Schedule Weekly Snapshots

To schedule weekly snapshot collection, edit the `` file and update the `` option:

The switch stores the snapshots in the `/var/lib/config-backup/auto-snapshots/weekly` directory.

```
cumulus@switch:~$ 
```

## Storage Capacity Limit

The switch enforces an internal storage capacity limit of 512 MB for each directory (`/var/lib/config-backup/auto-snapshots/weekly` and `/var/lib/config-backup/auto-snapshots/applied`). When the directory reaches above 512 MB, the switch deletes the oldest snapshots automatically and logs the deleted snapshots.

## Restore a Snapshot

To restore a configuration snapshot, run the 

```
cumulus@switch:~$ 
cumulus@switch:~$
```
