---
title: Patches
author: NVIDIA
weight: 61
toc: 3
---
The Cumulus Linux patch framework delivers small, targeted, reversible package fixes, such as a critical bug or CVE, to a running switch without requiring a full image upgrade.

You can install a critical fix within your own maintenance window and back it out without a full image upgrade.

Patches only contain changed packages and complement rather than replace the standard release; NVIDIA rolls every patch into a subsequent release.

When you install a patch over an existing one, the two form a chain. Uninstalling a patch returns the switch to the patch underneath it rather than to the base image, and you step back through a chain one patch at a time. Only a patch with nothing installed over it returns the switch to the base image.

{{%notice note%}}
- Upgrading system packages after you install a patch might overwrite the patch fixes; the switch warns you before proceeding.
- A failed patch install rolls back all touched packages automatically so that the switch is not left in a half-installed state. The switch returns to the patch it was already running, or to the base image if it was not running a patch.
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
- `allow-incompatible` bypasses the compatibility, baseline, and coverage validate-check failures.
- `accept-rollback-to-base` installs the patch when the patch it supersedes is no longer on the switch.

{{%notice warning%}}
Use the `allow-incompatible` option with caution as it overrides the compatibility checks and forces the installation; NVIDIA cannot guarantee that the system will work as expected after installation.
{{%/notice%}}

{{%notice warning%}}
Use the `accept-rollback-to-base` option with caution. When you install a patch this way, uninstalling it later returns the affected packages to their base-image versions instead of to the patch underneath, so the fix that patch carried is lost. The `allow-incompatible` option does not override this check.
{{%/notice%}}

The switch refuses to install a patch in the following cases:
- The patch does not carry every package that the patch already installed carries. Uninstalling the new patch later leaves those packages behind.
- The patch that this patch supersedes is no longer on the switch. To install anyway, use the `accept-rollback-to-base` option.
- The root filesystem does not have room for the packages the patch installs. The switch also refuses to fetch a patch without room to unpack it.

{{%notice note%}}
Neither the `force` option nor the `allow-incompatible` option overrides a disk space refusal. To free space, run the `nv action prune system packages archive` command, then try again. Refer to {{<link url="#reclaim-patch-space" text="Reclaim Patch Space">}}.
{{%/notice%}}

## Uninstall a Patch

To uninstall a patch, run the `nv action uninstall system packages archive <archive-id>` command. The switch removes the patch, restores the patch installed underneath it, and makes the result take effect as a single operation. Where no patch is underneath, the affected packages return to their base-image versions.

{{%notice note%}}
- You can only uninstall the patch on top of a chain. If another patch is installed over it, the switch refuses the command and names the patch you must remove first.
- To reach an earlier patch, uninstall the patches above it one at a time. You cannot step directly to an arbitrary earlier patch.
- Uninstalling a patch does not remove it from the switch; you can install it again or step back to it later. Refer to {{<link url="#reclaim-patch-space" text="Reclaim Patch Space">}}.
- If the patch underneath is no longer on the switch, the affected packages return to their base-image versions and the fix that patch carries does not restore.
- If the patch takes effect by rebooting the switch, the switch reboots once for the whole operation, not once for each patch.
{{%/notice%}}

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

To delete a patch from the switch, run the `nv action delete system packages archive <archive-id>` command. You must uninstall the patch before you can delete it. The switch also refuses to delete a patch on which a chain still depends, which includes every patch underneath the one in effect. To remove those patches, refer to {{<link url="#reclaim-patch-space" text="Reclaim Patch Space">}}.

```
cumulus@switch:~$ nv action delete system packages archive rm1234567
The operation will delete the archive.
Type [y] to delete the archive.
Type [N] to abort.
Do you want to continue? [y/N] y
Action executing ...
...
```

## Reclaim Patch Space

The switch keeps every patch you install, including patches you uninstall and patches that a later patch supersedes. Retaining them is what lets you step back through a chain; patches accumulate on the root filesystem until you reclaim the space.

<!-- REVIEW: the prune command, its confirmation prompt and the accept-rollback-to-base
     option are drafted from the spec's CLI tables. The spec is revision 1.0 dated
     2026-09-02 and marks the confirmation wording as not final, and the prompt it shows
     ("Are you sure? [y/N]:") does not match the "The operation will ... Type [y] ..."
     style every other example on this page uses. Capture all of it on a candidate build.
     Delete this comment before publishing. -->

To reclaim the space, run the `nv action prune system packages archive` command. For each chain, the switch keeps the patch on top and the patch immediately beneath it, and removes the rest. The command acts on every chain on the switch and takes no archive identifier.

```
cumulus@switch:~$ nv action prune system packages archive
Are you sure? [y/N]: y
Action executing ...
True
Action succeeded
```

Add the `force` option to run the command without the prompt to continue.

{{%notice warning%}}
The `nv action prune system packages archive` command removes patches from the switch permanently. After it runs, each chain can step back only one patch. Running it is the only thing that reduces how far back you can go.
{{%/notice%}}

The switch never reclaims this space on its own.

## Show Patch Information

To show the staged patch archives, each with a summary and status, run the `nv show system packages archive` command. The status is `installed`, `not-installed`, `partially-installed`, `failed`, or `operation-in-progress`.

{{%notice note%}}
A patch that a later patch supersedes shows a status of `not-installed` because the packages it fixes are running the versions of the later patch. The patch is still on the switch and uninstalling the later patch restores it.
{{%/notice%}}

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

The `installed-at` field shows when the patch became the running version of its packages. If you uninstall a later patch and the switch restores this one, `installed-at` shows the time of that step back rather than the time you first installed the patch.

The `nv show system version` command shows if the switch has a patch installed.

```
cumulus@switch:~$ nv show system version
                 operational
---------------  ----------------------------
onie             2021.05-5.3.0008-115200
kernel           6.1.0-cl-1-amd64
base-os          Debian GNU/Linux 12.14
product-release  5.19.0
image
  build-id       5.19.0.0025
  build-date     Tue Jul 21 11:06:05 UTC 2026
patched          yes
```

{{%notice note%}}
- The `patch`​ field in `nv show system version` command output shows only after you install a patch. If there is no installed patch, the command output omits this field.
- The `cat /etc/image-release` command output shows `PATCHED=yes` when the switch includes an installed patch. When there is no installed patch, this field is absent.
{{%/notice%}}
