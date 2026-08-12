---
title: Patches
author: NVIDIA
weight: 61
toc: 3
---
The Cumulus Linux patch framework delivers small, targeted, reversible package fixes, such as a critical bug or CVE, to a running switch without requiring a full image upgrade.

You can install a critical fix within your own maintenance window and back it out without a full image upgrade.

Patches only contain changed packages and complement rather than replace the standard release; NVIDIA rolls every patch into a subsequent release.

You can roll back and return to the base image, not a previously-running patch. If a package is running an earlier patch version when you install a later patch, removing the later patch restores the base-image version, not the earlier patch.

{{%notice note%}}
- Upgrading system packages after you install a patch might overwrite the patch fixes; the switch warns you before proceeding.
- A failed patch install rolls back all touched packages automatically to the base version so that the switch is not left in a half-installed state.
- Installing and uninstalling a patch might restart affected services or reboot the system. Before you install or uninstall a patch, check the `impact` field in the `nv show system packages archive <archive-id>` command output to understand the expected impact.
{{%/notice%}}

## Install a Patch

To download a patch, run the `nv action fetch system packages archive <url>` command. The patch infrastructure supports HTTPS, SCP, FTP, and SFTP.

```
cumulus@switch:~$ nv action fetch system packages archive http://path/patch.deb
Action executing ...
Fetching file ...
Action executing ...
File has been successfully fetched
...
Action succeeded
```

The `nv action fetch system packages archive <url>` command uses the management VRF by default as the URL is often only reachable over the management VRF. To use a different VRF, use the optional VRF parameter (`nv action fetch system packages archive <url> vrf <vrf-id>`).

To install a patch, run the `nv action install system packages archive <archive-id>` command. The install command validates, then replaces the targeted packages with their fixed versions. The fixed package versions become the running package versions.

The `<archive-id>` is the archive identifier (for example, rm1234567). To show the archive identifier, run the `nv show system packages archive`​ command after you download the patch. The `Archive` column shows the archive identifier.

{{%notice note%}}
A patch targets a specific base image version and platform; the validation process checks both and does not install the patch if there is a mismatch.
{{%/notice%}}

```
cumulus@switch:~$ nv action install system packages archive rm1234567
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

You can run the `nv action install system packages archive <archive-id>` command with the following options:
- `force` runs the command without the prompts to continue.
- `dry-run` runs only the validate step but does not install the patch.
- `allow-incompatible` bypasses any validate-check failure. 

{{%notice warning%}}
Use the `allow-incompatible` option with caution as it overrides the compatibility checks and forces the installation; NVIDIA cannot guarantee that the system will work as expected after installation.
{{%/notice%}}

## Uninstall a Patch

To uninstall a patch and restore the pre-fix (base image) version as the running version, run the `nv action uninstall system packages archive <archive-id>` command.

```
cumulus@switch:~$ nv action uninstall system packages archive rm1234567
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

To delete a patch from the switch, run the `nv action delete system packages archive <archive-id>` command. You must uninstall the patch before you can delete it.

```
cumulus@switch:~$ nv action delete system packages archive rm1234567
The operation will delete the archive.
Type [y] to delete the archive.
Type [N] to abort.
Do you want to continue? [y/N] y
Action executing ...
...
```

## Show Patch Information

To show the staged patch archives, each with a summary and status, run the `nv show system packages archive` command. The status is `installed`, `not-installed`, `partially-installed`, `failed`, or `operation-in-progress`.

```
cumulus@switch:~$ nv show system packages archive
Archive    summary                                                  status
---------  -------------------------------------------------------  ---------
rm1234567  Add startup diagnostic log markers to switchd and ptmd.  installed
```

To show information about a specific patch, such as a summary, description, impact, installation time, failure reason, and its installed status, run the `nv show system packages archive <archive-id>` command:

```
cumulus@switch:~$ nv show system packages archive rm1234567
              operational
------------  ----------------------------------------------------------------------------
summary       Add startup diagnostic log markers to switchd and ptmd.
description   Updates switchd and ptmd to each emit an additional informational log line
              at daemon startup, used to confirm patch delivery on the switch. No
              forwarding, protocol, or configuration behaviour is changed.
status        installed
impact        Installing swaps switchd and ptmd to the fixed versions and restarts both
              services. The switchd restart causes a brief forwarding/data-plane
              disruption of a few seconds, and ptmd re-establishes its LLDP/BFD
              adjacencies; no reboot is required. Uninstall restores the original versions
              with the same brief restarts.
installed-at  2026-07-27T18:35:24Z
```

The `nv show system version` command shows if the switch has a patch installed.

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
patched          yes
```

{{%notice note%}}
- The `patch`​ field in `nv show system version` command output shows only after you install a patch. If there is no installed patch, the command output omits this field.
- The `cat /etc/image-release` command output shows `PATCHED=yes` when the switch includes an installed patch. When there is no installed patch, this field is absent.
{{%/notice%}}
