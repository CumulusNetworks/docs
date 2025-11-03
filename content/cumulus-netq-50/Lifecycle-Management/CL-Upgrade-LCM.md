---
title: Upgrade Cumulus Linux
author: NVIDIA
weight: 680
toc: 4
---

Lifecycle management (LCM) lets you upgrade Cumulus Linux on one or more switches in your network with the NetQ UI or the CLI. You do this by scheduling 'upgrade jobs' which upgrade Cumulus Linux on your switches. Each job can upgrade CL on up to 50 switches. NetQ upgrades the switches 5 at a time until all switches in the upgrade job are upgraded. You can schedule up to 5 upgrade jobs to run simultaneously.

For deployments running Cumulus Linux versions:

- 5.6.0 to 5.8.0: you can upgrade up to Cumulus Linux version 5.9 or later if your environment is running NetQ 4.10.1 or later. If you are running an earlier NetQ version, you must {{<link title="Upgrade NetQ Agent" text="upgrade NetQ">}} before you upgrade Cumulus Linux.
- 5.0.1 to 5.7.0: you can upgrade up to Cumulus Linux version 5.8.


To upgrade to Cumulus Linux 5.9 or later:

1. Ensure your switches are configured with NVUE. 
2. {{<exlink url="https://docs.nvidia.com/networking-ethernet-software/cumulus-linux/Quick-Start-Guide/#configure-the-hostname" text="Configure the switches' hostnames">}} with NVUE. 
3. Save all configurations with the `nv config save` command.

{{%notice warning%}}
When you upgrade a switch that has not been configured using NVUE (which is only supported for upgrades to Cumulus Linux versions 5.8 and earlier), LCM backs up and restores flat file configurations in Cumulus Linux. After you upgrade a switch that has been managed with flat files and subsequently run NVUE configuration commands, NVUE will overwrite the configuration restored by NetQ LCM. See {{<exlink url="https://docs.nvidia.com/networking-ethernet-software/cumulus-linux/Installation-Management/Upgrading-Cumulus-Linux/" text="Upgrading Cumulus Linux">}} and {{<exlink url="https://docs.nvidia.com/networking-ethernet-software/cumulus-linux/System-Configuration/NVIDIA-User-Experience-NVUE/NVUE-CLI/#" text="System Configuration with the NVUE CLI">}} for additional information.
{{%/notice%}}

{{<notice note>}}
During the Cumulus Linux upgrade process, NetQ does not upgrade or reinstall packages that are not part of the Cumulus Linux image. For example, if you installed node_exporter packages on a switch, you must reinstall these packages after the upgrade is complete.
{{</notice>}}
## Prepare for a Cumulus Linux Upgrade

Before you upgrade, make sure you have the appropriate files and credentials:

{{<tabs "TabID34" >}}

{{<tab "Preparation Steps">}}

1. Upload the {{<link title="NetQ and Network OS Images/#upload-upgrade-images" text="Cumulus Linux upgrade images">}}.

{{<notice note>}}
If you are upgrading to Cumulus Linux 5.9 or later and select the option to roll back to a previous Cumulus Linux version (for unsuccessful upgrade attempts), you must upload a total of four netq-apps and netq-agents packages to NetQ. Cumulus Linux 5.9 or later packages include <b>cld12</b>. Prior versions of Cumulus Linux include <b>cl4u</b>.<br><br> For example, you must upload the following packages for amd64 architecture:

- netq-agent_5.0.0-<b>cl4u</b>53~1753783478.2a97c1dde_amd64.deb
- netq-apps_5.0.0-<b>cl4u</b>53~1753783478.2a97c1dde_amd64.deb
- netq-agent_5.0.0-<b>cld12u</b>53~1753783414.2a97c1dde_amd64.deb
- netq-apps_5.0.0-<b>cld12u</b>53~1753783414.2a97c1dde_amd64.deb
{{</notice>}}

2. (Optional) Specify a {{<link title="NetQ and Network OS Images/#specify-a-default-upgrade-version" text="default upgrade version">}}.

3. Verify or add {{<link title="Credentials and Profiles" text="switch access credentials">}}.

4. (Optional) {{<link title="Switch Management/#assign-roles-to-switches" text="Assign a role">}} to each switch to identify switch dependencies and avoid potential upgrade issues.

{{</tab>}}

{{</tabs>}}

## Upgrade Cumulus Linux

If the NetQ Agent is already installed on the switches you'd like to upgrade, follow the steps below. If the NetQ Agent is *not* installed on the switches you'd like to upgrade, run a {{<link title="Switch Management/#switch-discovery" text="switch discovery">}} to find all Cumulus Linux switches with and without NetQ currently installed and perform the CL upgrade as part of the discovery workflow.

{{<tabs "TabID51" >}}

{{<tab "NetQ UI" >}}

1. Expand the {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/03-Menu/navigation-menu.svg" alt="" width="18" height="18">}} **Menu**, then select **Manage switches**. 

2. From the **Switch management** tab, locate the Switches card and click **Manage**.

3. Select the switches you want to upgrade.

4. Click {{<img src="/images/netq/cl-upgrade-icon-blk.png" height="14" width="18">}} **Upgrade OS** above the table.

    Follow the steps in the UI. Enter a name for the upgrade and review the switches that you selected to upgrade:

    {{<figure src="/images/netq/upgrade-switches-450.png" alt="screen displaying 2 switches selected for upgrading" width="550">}}

If you accidentally included a switch that you do *not* want to upgrade, hover over the switch information card and click {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/23-Delete/bin-1.svg" alt="" height="18" width="18">}} **Delete** to remove it from the upgrade.
   
5. Click **Next**.

6. Specify which Cumulus Linux version NetQ should use during the upgrade. If you previously uploaded NetQ images, you can also upgrade NetQ at this time.

7. Verify or add {{<link title="Credentials and Profiles" text="switch access credentials">}}.

8. Click **Next**.

9. Verify the upgrade job options.

{{%notice note%}}
By default, NetQ performs a roll back to the original Cumulus Linux version on any server which fails to upgrade. For single-server and cluster deployments, NetQ takes network snapshots before and after the upgrade. This option is unavailable in scale cluster deployments.
{{%/notice%}}

You can exclude selected services and protocols from the snapshots by clicking them. Node and services must be included.

    {{<figure src="/images/netq/upgrade-switch-options-450.png" width="500">}}

10. Click **Next**.

11. NetQ performs several checks to eliminate preventable problems during the upgrade process. When all of the pre-checks pass, click **Preview**.

12. NetQ directs you to a screen where you can review the upgrade. After reviewing, select **Start upgrade** and confirm.

{{</tab>}}

{{<tab "NetQ CLI" >}}

Perform the upgrade using the {{<link title="lcm/#netq-lcm-upgrade-cl-image" text="netq lcm upgrade cl-image">}} command, providing a name for the upgrade job, the Cumulus Linux and NetQ version, and a comma-separated list of the hostname(s) to be upgraded:

```
nvidia@switch:~$ netq lcm upgrade cl-image job-name upgrade-example cl-version 5.15.0 netq-version 5.0.0 hostnames spine01,spine02
```

### Create a Network Snapshot

You can also generate a network snapshot before and after the upgrade by adding the `run-snapshot-before-after` option to the command:

```
nvidia@switch:~$ netq lcm upgrade cl-image job-name upgrade-example cl-version 5.15.0 netq-version 5.0.0 hostnames spine01,spine02,leaf01,leaf02 order spine,leaf run-snapshot-before-after
```

### Restore upon an Upgrade Failure

(Recommended) You can restore the previous version of Cumulus Linux if the upgrade job fails by adding the `run-restore-on-failure` option to the command.

```
nvidia@switch:~$ netq lcm upgrade cl-image name upgrade-example cl-version 5.15.0 netq-version 5.0.0 hostnames spine01,spine02,leaf01,leaf02 order spine,leaf run-restore-on-failure
```

{{</tab>}}

{{</tabs>}}

### Pre-check Failures

If one or more of the pre-checks fail, resolve the related issue and start the upgrade again. In the NetQ UI these failures appear on the Upgrade Preview page. In the NetQ CLI, it appears in the form of error messages in the `netq lcm show upgrade-jobs cl-image` command output.

### Analyze Results

After starting the upgrade you can monitor the progress in the NetQ UI. Successful upgrades are indicated by a green check {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/check-circle-1.svg" alt="" height="16" width="18">}}. Failed upgrades display error messages indicating the cause of failure.

 - To view the progress of current upgrade jobs and the history of previous upgrade jobs using the CLI, run `netq lcm show upgrade-jobs cl-image`.
 - To see details of a particular upgrade job, run `netq lcm show status job-ID`.
 - To see only Cumulus Linux upgrade jobs, run `netq lcm show status cl-image job-ID`.

Upon successful upgrade, you can:

- {{<link title="Network Snapshots" text="Compare network snapshots">}} taken before and after the upgrade.

- Download details about the upgrade in a JSON-formatted file, by clicking **Download report**.
### Post-check Failures

A successful upgrade can still have post-check warnings. For example, you updated the OS, but not all services are fully up and running after the upgrade. If one or more of the post-checks fail, warning messages appear in the Post-Upgrade Tasks section of the preview. Click the warning category to view the detailed messages.
