---
title: Micro-Update
author: NVIDIA
weight: 61
toc: 3
---
The Cumulus Linux Micro-Update Framework delivers small, targeted, reversible package fixes, such as a critical bug or CVE, to a running switch without requiring a full image upgrade.

You can schedule a critical fix on your own maintenance window and back it out without a full image upgrade.

The micro update only contains changed packages and complements rather than replaces the standard release; every micro-update fix is also rolled into a subsequent release.

You can roll back to return to the base image, not a previously-running micro-update. If a package is running an earlier micro update version when a later micro update is installed, removing the later one restores the base-image version, not the earlier micro-update.

## Install a Micro Update

To download and stage the micro update, run the `nv action fetch system packages archive <url>` command. The fix stays inactive until you run the `nv action install system packages archive <id>` command.

```
cumulus@switch:~$ nv action fetch system packages archive 
```

To activate the fix, run the `nv action install system packages archive <id>` command. The activate command validates, then swaps the targeted packages to their fixed versions. The fixed package versions become the running package versions.

```
cumulus@switch:~$ nv action install system packages archive <id>
```

You run the `nv action install system packages archive <id>` command with the following options:
- `force` runs the command without the prompts to continue.
- `dry-run` runs only the validate step and applies nothing.
- `allow-incompatible` bypasses any validate-check failure.

## Uninstall a Micro Update

To uninstall the system packages archive and restore the pre-fix package versions to inactive, run the `nv action uninstall system packages archive <id>` command.

```
cumulus@switch:~$ nv action uninstall system packages archive <id>
```

To delete the micro update from the swich, run the `nv action delete system packages archive <id>` command:

```
cumulus@switch:~$ nv action delete system packages archive <id>
```

## Show Micro Update Information

To show the micro update staged archives, each with a summary and status, run the `nv show system packages archive` command. The status is `installed`, `not-installed`, `partially-installed`, `failed`, or `operation-in-progress`.

```
cumulus@switch:~$ nv show system packages archive
```

To show information about a specific micro update, such as a summary, description, impact, supported-with, installation time, failure-reason, and its applied status, run the `nv show system packages archive <id>` command:

```
cumulus@switch:~$ nv show system packages archive <id>

```

The `nv show system version` command shows if the switch has a micro update installed and activated.

```
cumulus@switch:~$ nv show system version
                 operational
---------------  ----------------------------
onie             2023.11-5.3.0011-115200
kernel           6.1.0-cl-1-amd64
base-os          Debian GNU/Linux 12.13
product-release  5.17.0
image
  build-id       5.17.0.0033
  build-date     Thu May 14 05:50:32 UTC 2026
micro-updated    yes 
```
