---
title: Micro-Updates
author: NVIDIA
weight: 61
toc: 3
---
The Cumulus Linux micro update framework delivers small, targeted, reversible package fixes, such as a critical bug or CVE, to a running switch without requiring a full image upgrade.

You can install a critical fix within your own maintenance window and back it out without a full image upgrade.

Micro updates only contain changed packages and complement rather than replace the standard release; NVIDIA rolls every micro update into a subsequent release.

You can roll back and return to the base image, not a previously-running micro update. If a package is running an earlier micro update version when you install a later micro update, removing the later update restores the base-image version, not the earlier micro update.

{{%notice note%}}
- Upgrading system packages after you install a micro update might overwrite the micro update fixes; the switch warns you before proceeding.
- A failed micro update install rolls back all touched packages automatically to the base version so that the switch is not left in a half-installed state.
{{%/notice%}}


## Install a Micro Update

To download a micro update, run the `nv action fetch system packages archive <url>` command. The micro update infrastructure supports HTTPS, SCP, FTP, and SFTP.

```
cumulus@switch:~$ nv action fetch system packages archive http://path/micro-update.deb
Action executing ...
Fetching file ...
Action executing ...
File has been successfully fetched
...
Action succeeded
```

The `nv action fetch system packages archive <url>` command uses the management VRF by default as the URL is often only reachable over the management VRF. To use a different VRF, use the optional VRF parameter (`nv action fetch system packages archive <url> vrf <vrf-id>`).

To install the micro update, run the `nv action install system packages archive <archive-id>` command. The install command validates, then replaces the targeted packages with their fixed versions. The fixed package versions become the running package versions.

The `<archive-id>` is the archive identifier (for example, rm0002). To show the archive identifier, run the `nv show system packages archive`​ command after you download the micro update. The `Archive` column shows the archive identifier.

{{%notice note%}}
- A micro update targets a specific base image version and platform; the validation process checks both and does not install the micro update if there is a mismatch.
- Installing and uninstalling a micro update might restart affected services. Before you install or uninstall a micro update, check the `impact` field in the `nv show system packages archive <archive-id>` command output to understand the expected impact.
{{%/notice%}}

```
cumulus@switch:~$ nv action install system packages archive rm0002
The operation will install the archive.
Type [y] to install the archive.
Type [N] to abort.

Do you want to continue? [y/N] y
Action executing ...
...
The following packages will be upgraded:
  ptmd switchd switchd-halmlx
...
Action succeeded
```

You run the `nv action install system packages archive <archive-id>` command with the following options:
- `force` runs the command without the prompts to continue.
- `dry-run` runs only the validate step but does not install the micro update.
- `allow-incompatible` bypasses any validate-check failure. 

{{%notice warning%}}
Use the `allow-incompatible` option with caution as it overrides the compatibility checks and forces the installation; NVIDIA cannot guarantee that the system will work as expected after installation.
{{%/notice%}}

## Uninstall a Micro Update

To uninstall a micro update and restore the pre-fix (base image) version as the running version, run the `nv action uninstall system packages archive <archive-id>` command.

{{%notice note%}}
Installing and uninstalling a micro update might restart any affected services. The `impact` field in the `nv show system packages archive <archive-id>` command output shows the affected services. 
{{%/notice%}}

```
cumulus@switch:~$ nv action uninstall system packages archive rm0002
The operation will uninstall the archive.
Type [y] to uninstall the archive.
Type [N] to abort.

Do you want to continue? [y/N] y
Action executing ...
...
The following packages will be DOWNGRADED:
  ptmd switchd switchd-halmlx
...
Action succeeded
```

To delete a micro update from the switch, run the `nv action delete system packages archive <archive-id>` command. You must uninstall the micro update before you can delete it.

```
cumulus@switch:~$ nv action delete system packages archive rm0002
The operation will delete the archive.
Type [y] to delete the archive.
Type [N] to abort.

Do you want to continue? [y/N] y
Action executing ...
...
The following packages will be REMOVED:
  cl-micro-update-rm0002*
...
```

## Show Micro Update Information

To show the micro update staged archives, each with a summary and status, run the `nv show system packages archive` command. The status is `installed`, `not-installed`, `partially-installed`, `failed`, or `operation-in-progress`.

```
cumulus@switch:~$ nv show system packages archive
No Data
```

To show information about a specific micro update, such as a summary, description, impact, installation time, failure reason, and its installed status, run the `nv show system packages archive <archive-id>` command:

```
cumulus@switch:~$ nv show system packages archive rm0002
              operational
------------  ----------------------------------------------------------------------------
summary       Add startup diagnostic log markers to switchd and ptmd.
description   Updates switchd and ptmd to each emit an additional informational log line
              at daemon startup, used to confirm micro-update delivery on the switch. No
              forwarding, protocol, or configuration behaviour is changed.
status        installed
impact        Installing swaps switchd and ptmd to the fixed versions and restarts both
              services. The switchd restart causes a brief forwarding/data-plane
              disruption of a few seconds, and ptmd re-establishes its LLDP/BFD
              adjacencies; no reboot is required. Uninstall restores the original versions
              with the same brief restarts.
installed-at  2026-07-27T18:35:24Z
```

The `nv show system version` command shows if the switch has a micro update installed.

```
cumulus@switch:~$ nv show system version
                 operational
---------------  ----------------------------
onie             2021.05-5.3.0008-115200
kernel           6.1.0-cl-1-amd64
base-os          Debian GNU/Linux 12.14
product-release  5.18.0
image
  build-id       5.18.0.0025
  build-date     Tue Jul 21 11:06:05 UTC 2026
micro-updated    yes
```

{{%notice note%}}
- The `micro-updated`​ field in `nv show system version` command output shows only after you install a micro update. If there is no installed micro update, the command output omits this field.
- The `cat /etc/image-release` command output shows `MICRO_UPDATED=yes` when the switch includes an installed micro update. When there is no installed micro update, this field is absent.
{{%/notice%}}
