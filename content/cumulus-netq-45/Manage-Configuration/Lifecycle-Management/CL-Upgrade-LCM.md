---
title: Upgrade Cumulus Linux Using LCM
author: NVIDIA
weight: 680
toc: 4
---

LCM lets you upgrade Cumulus Linux on one or more switches in your network via the NetQ UI or the CLI. You can run up to five upgrade jobs simultaneously; however, a given switch can only appear in one running job at a time. Upgrading Cumulus Linux on a switch typically takes around 45 minutes.

You can upgrade Cumulus Linux from:

- 3.7.12 to later versions of Cumulus Linux 3
- 3.7.12 or later to 4.2.0 or later versions of Cumulus Linux 4
- 4.0 to later versions of Cumulus Linux 4
- 4.4.0 or later to Cumulus Linux 5 releases
- 5.0.0 or later to 5.1.0 or later versions of Cumulus Linux 5

{{<notice warning>}}
When upgrading to Cumulus Linux 5.0.0 or later, LCM backs up and restores flat file configurations in Cumulus Linux. After you upgrade to Cumulus Linux 5, running NVUE configuration commands replaces any configuration restored by NetQ LCM. See {{<exlink url="https://docs.nvidia.com/networking-ethernet-software/cumulus-linux/Installation-Management/Upgrading-Cumulus-Linux/" text="Upgrading Cumulus Linux">}} for additional information.
{{</notice>}}

{{<notice info>}}
When NVUE is enabled, LCM supports upgrades from Cumulus Linux 5.0.0 to later versions of Cumulus Linux 5. Upgrading from earlier versions of Cumulus Linux is not supported when NVUE is enabled. 
{{</notice>}}
## How to Upgrade Cumulus Linux Using LCM

If the NetQ Agent is already installed on the switches you'd like to upgrade, follow the steps below.

If the NetQ Agent is *not* installed on the switches you'd like to upgrade, run a {{<link title="Upgrade Cumulus Linux Using LCM/#Upgrade-Cumulus-Linux-on-Switches-Without NetQ-Agent-Installed" text="switch discovery">}}, then proceed with the upgrade.

## Upgrade Cumulus Linux on Switches With NetQ Agent Installed
### Prepare for a Cumulus Linux Upgrade

Before you upgrade, make sure you have the appropriate files and credentials:

{{<tabs "TabID42" >}}

{{<tab "NetQ UI" >}}

1. Click {{<img src="/images/netq/devices.svg" height="18" width="18">}} Devices in the workbench header, then click **Manage switches**.

2. Upload the {{<link title="NetQ and Network OS Images/#upload-upgrade-images" text="Cumulus Linux upgrade images">}}.

3. (Optional) Specify a {{<link title="NetQ and Network OS Images/#specify-a-default-upgrade-version" text="default upgrade version">}}.

4. Verify or add {{<link title="Switch Credentials" text="switch access credentials">}}.

5. (Optional) Assign a {{<link  title="Switch Credentials/#assign-switch-roles" text="role">}} to each switch.

{{</tab>}}

{{<tab "NetQ CLI" >}}

1. Create a discovery job to locate Cumulus Linux switches on the network. Use the `netq lcm discover` command, specifying a single IP address, a range of IP addresses where your switches are located in the network, or a CSV file containing the IP address, and optionally, the hostname and port for each switch on the network. If the port is blank, NetQ uses switch port 22 by default. They can be in any order you like, but the data must match that order.

       cumulus@switch:~$ netq lcm discover ip-range 10.0.1.12 
       NetQ Discovery Started with job id: job_scan_4f3873b0-5526-11eb-97a2-5b3ed2e556db

2. Upload the {{<link title="NetQ and Network OS Images/#upload-upgrade-images" text="Cumulus Linux upgrade images">}}. 

3. Verify or add {{<link title="Switch Credentials" text="switch access credentials">}}.

4. (Optional) Assign a {{<link title="Switch Credentials/#assign-switch-roles" text="role">}} to each switch.

{{</tab>}}

{{</tabs>}}

### Perform a Cumulus Linux Upgrade

After you complete the preparation steps, upgrade Cumulus Linux:

{{<tabs "TabID51" >}}

{{<tab "NetQ UI" >}}

1. Click {{<img src="/images/netq/devices.svg" height="18" width="18">}} Devices in any workbench header, then select **Manage switches**.

2. Locate the Switches card and click **Manage**.

3. Select the switches you want to upgrade. You can filter by role or sort by column heading to narrow down the list.

4. Click {{<img src="/images/netq/cl-upgrade-icon-blk.png" height="14" width="18">}} (Upgrade OS) above the table.

    From this point forward, the software walks you through the upgrade process, beginning with a review of the switches that you selected for upgrade.

    {{<figure src="/images/netq/lcm-upgrade-switches-review-switches-tab-320.png" alt="screen displaying 4 switches selected for upgrading" width="500">}}

6. Verify that the switches you selected are included, and that they have the correct IP address and roles assigned.

If you accidentally included a switch that you do NOT want to upgrade, hover over the switch information card and click {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/23-Delete/bin-1.svg" height="18" width="18">}} to remove it from the upgrade job.
   

        {{<figure src="/images/netq/lcm-upgrade-switches-review-switches-modify-switch-320.png" alt="switch assigned a spine roll with dropdown to change role" width="500">}}

If the role is incorrect or missing, click {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/22-Edit/pencil-1.svg" height="18" width="18">}}, then select a role for that switch from the dropdown. Click {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/23-Delete/delete-2.svg" height="18" width="18">}} to discard a role change:

        {{<figure src="/images/netq/lcm-upgrade-switches-review-switches-edit-roles-320.png" width="150">}}

7. When you are satisfied that the list of switches is accurate for the job, click **Next**.

8. Verify that you want to use the default Cumulus Linux or NetQ version for this upgrade job. If not, click **Custom** and select an alternate image from the list.

    {{<figure src="/images/netq/lcm-upgrade-switches-describe-tab-320.png" width="500" caption="Default CL Version Selected">}}{{<figure src="/images/netq/lcm-upgrade-switches-describe-tab-custom-version-320.png" width="400" caption="Custom CL Version Selected">}}

9. Note that the switch access authentication method, *Using global access credentials*, indicates you have chosen either basic authentication with a username and password or SSH key-based authentication for all of your switches. Authentication on a per switch basis is not currently available.

10. Click **Next**.

11. Verify the upgrade job options.

    By default, NetQ takes a network snapshot before the upgrade and then one after the upgrade is complete. It also performs a roll back to the original Cumulus Linux version on any server which fails to upgrade.

    You can exclude selected services and protocols from the snapshots. By default, node and services are included, but you can deselect any of the other items. Click on one to remove it; click again to include it. This is helpful when you are not running a particular protocol, or you have concerns about the amount of time it will take to run the snapshot. Note that removing services or protocols from the job might produce non-equivalent results compared with prior snapshots.

    While these options provide a smoother upgrade process and are highly recommended, you have the option to disable these options by clicking **No** next to one or both options.

    {{<figure src="/images/netq/lcm-upgrade-switches-options-tab-320.png" width="500">}}

12. Click **Next**.

13. After the pre-checks have completed successfully, click **Preview**. If there are failures, refer to {{<link url="#Pre-check Failures" text="Pre-check Failures">}}.

    These checks verify the following:

    - Selected switches are not currently scheduled for, or in the middle of, a Cumulus Linux or NetQ Agent upgrade
    - Selected versions of Cumulus Linux and NetQ Agent are valid upgrade paths
    - All mandatory parameters have valid values, including MLAG configurations
    - All switches are reachable
    - The order to upgrade the switches, based on roles and configurations

    {{<figure src="/images/netq/lcm-upgrade-switches-precheck-tab-success-320.png" width="500">}}

14. Review the job preview.

    When all of your switches have roles assigned, this view displays the chosen job options (top center), the pre-checks status (top right and left in Pre-Upgrade Tasks), the order in which the switches are planned for upgrade (center; upgrade starts from the left), and the post-upgrade tasks status (right).

    {{<figure src="/images/netq/lcm-upgrade-switches-preview-job-320.png" width="700" caption="Roles assigned">}}

<div style="padding-left: 18px;">When none of your switches have roles assigned <em>or</em> they are all of the same role, this view displays the chosen job options (top center), the pre-checks status (top right and left in Pre-Upgrade Tasks), a list of switches planned for upgrade (center), and the post-upgrade tasks status (right).</div>

    {{<figure src="/images/netq/lcm-upgrade-switches-preview-single-roll-320.png" width="700" caption="All roles the same">}}

<div style="padding-left: 18px;">When some of your switches have roles assigned, any switches without roles get upgraded last and get grouped under the label <em>Stage1</em>.</div>

    {{<figure src="/images/netq/lcm-upgrade-switches-preview-job-someroles-310.png" width="700" caption="Some roles assigned">}}

15. When you are happy with the job specifications, click **Start Upgrade**.

16. Click **Yes** to confirm that you want to continue with the upgrade, or click **Cancel** to discard the upgrade job.

    {{<figure src="/images/netq/lcm-upgrade-switches-confirm-dialog-320.png" width="200">}}

{{</tab>}}

{{<tab "NetQ CLI" >}}

Perform the upgrade using the `netq lcm upgrade cl-image` command, providing a name for the upgrade job, the Cumulus Linux and NetQ version, and a comma-separated list of the hostname(s) to be upgraded:

```
cumulus@switch:~$ netq lcm upgrade cl-image job-name upgrade-cl430 cl-version 4.3.0 netq-version 4.4.0 hostnames spine01,spine02
```

#### Network Snapshot Creation

You can also generate a network snapshot before and after the upgrade by adding the `run-snapshot-before-after` option to the command:

```
cumulus@switch:~$ netq lcm upgrade cl-image name upgrade-430 cl-version 4.3.0 netq-version 4.4.0 hostnames spine01,spine02,leaf01,leaf02 order spine,leaf run-snapshot-before-after
```

#### Restore on an Upgrade Failure

You can have LCM restore the previous version of Cumulus Linux if the upgrade job fails by adding the `run-restore-on-failure` option to the command. This is highly recommended.

```
cumulus@switch:~$ netq lcm upgrade cl-image name upgrade-430 cl-version 4.3.0 netq-version 4.4.0 hostnames spine01,spine02,leaf01,leaf02 order spine,leaf run-restore-on-failure
```

{{</tab>}}

{{</tabs>}}

### Pre-check Failures

If one or more of the pre-checks fail, resolve the related issue and start the upgrade again. In the NetQ UI these failures appear on the Upgrade Preview page. In the NetQ CLI, it appears in the form of error messages in the `netq lcm show upgrade-jobs cl-image` command output.

{{<expand "Pre-check failure messages">}}

<!-- vale off -->
| Pre-check | Message | Type | Description | Corrective Action |
| --------- | ------- | ---- | ----------- | ----------------- |
| (1) Switch Order | &lt;hostname1&gt; switch cannot be upgraded without isolating &lt;hostname2&gt;, &lt;hostname3&gt; which are connected neighbors. Unable to upgrade | Warning | Switches hostname2 and hostname3 get isolated during an upgrade, making them unreachable. These switches are skipped if you continue with the upgrade. | Reconfigure hostname2 and hostname3 to have redundant connections, or continue with upgrade knowing that connectivity is lost with these switches during the upgrade process. |
| (2) Version Compatibility | Unable to upgrade &lt;hostname&gt; with CL version &lt;#&gt; to &lt;#&gt; | Error | LCM only supports the following Cumulus Linux upgrades:<br/><ul><li>3.7.12 to later versions of Cumulus Linux 3</li><li>3.7.12 or later to 4.2.0 or later versions of Cumulus Linux 4</li><li>4.0 to later versions of Cumulus Linux 4</li><li>4.4.0 or later to Cumulus Linux 5.0 releases</li><li>5.0.0 or later to Cumulus Linux 5.1 releases</li></ul> | Perform a fresh install of CL. |
|  | Image not uploaded for the combination: CL Version - &lt;x.y.z&gt;, Asic Vendor - &lt;NVIDIA \| Broadcom&gt;, CPU Arch - &lt;x86 \| ARM &gt; | Error | The specified Cumulus Linux image is not available in the LCM repository | Upload missing image. Refer to {{<link title="#Upload Images" text="Upload Images">}}. |
|  | Restoration image not uploaded for the combination: CL Version - &lt;x.y.z&gt;, Asic Vendor - &lt;Mellanox \| Broadcom&gt;, CPU Arch - &lt;x86 \| ARM &gt; | Error | The specified Cumulus Linux image needed to restore the switch back to its original version if the upgrade fails is not available in the LCM repository. This applies only when the "Roll back on upgrade failure" job option is selected. | Upload missing image. Refer to {{<link title="#Upload Images" text="Upload Images">}}. |
|  | NetQ Agent and NetQ CLI Debian packages are not present for combination: CL Version - &lt;x.y.z&gt;, CPU Arch - &lt;x86 \| ARM &gt; | Error | The specified NetQ packages are not installed on the switch. | Upload missing packages. Refer to {{<link title="Install NetQ Agents" text="Install NetQ Agents">}} and {{<link title="Install NetQ CLI" text="Install NetQ CLI">}}. |
|  |  | Restoration NetQ Agent and NetQ CLI Debian packages are not present for combination: CL Version - &lt;x.y.z&gt;, CPU Arch - &lt;x86 \| ARM &gt; | Error | The specified NetQ packages are not installed on the switch. | Install missing packages. Refer to {{<link title="Install NetQ Agents" text="Install NetQ Agents">}} and {{<link title="Install NetQ CLI" text="Install NetQ CLI">}}. |
|  | CL version to be upgraded to and current version on switch &lt;hostname&gt; are the same. | Warning | Switch is already operating the desired upgrade CL version. No upgrade is required. | Choose an alternate CL version for upgrade or remove switch from upgrade job. |
| (3) Switch Connectivity | Global credentials are not specified | Error | Switch access credentials are required to perform a CL upgrade, and they have not been specified. | Specify access credentials. Refer to {{<link title="#Specify Switch Credentials" text="Specify Switch Credentials">}}. |
|  | Switch is not in NetQ inventory: &lt;hostname&gt; | Error | LCM cannot upgrade a switch that is not in its inventory. | Verify you have the correct hostname or IP address for the switch.<br/><br/>Verify the switch has NetQ Agent 4.1.0 or later installed: click {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/03-Menu/navigation-menu.svg" height="18" width="18" alt="Main Menu">}}, then click <strong>Agents</strong> in the <strong>Network</strong> section, view <strong>Version</strong> column. Upgrade NetQ Agents if needed. Refer to {{<link title="Upgrade NetQ Agents">}}. |
|  | Switch &lt;hostname&gt; is rotten. Cannot select for upgrade. | Error | LCM must be able to communicate with the switch to upgrade it. | Troubleshoot the connectivity issue and retry upgrade when the switch is fresh. |
|  | Total number of jobs &lt;running jobs count&gt; exceeded Max jobs supported 50 | Error | LCM can support a total of 50 upgrade jobs running simultaneously. | Wait for the total number of simultaneous upgrade jobs to drop below 50. |
|  | Switch &lt;hostname&gt; is already being upgraded. Cannot initiate another upgrade. | Error | Switch is already a part of another running upgrade job. | Remove switch from current job or wait until the competing job has completed. |
|  | Backup failed in previous upgrade attempt for switch &lt;hostname&gt;. | Warning | LCM was unable to back up switch during a previously failed upgrade attempt. | You could back up the switch manually prior to upgrade if you want to restore the switch after upgrade. Refer to {{<link title="Back Up and Restore NetQ">}}. |
|  | Restore failed in previous upgrade attempt for switch &lt;hostname&gt;. | Warning | LCM was unable to restore switch after a previously failed upgrade attempt. | You might need to restore the switch manually after upgrade. Refer to {{<link title="Back Up and Restore NetQ">}}. |
|  | Upgrade failed in previous attempt for switch &lt;hostname&gt;. | Warning | LCM was unable to upgrade switch during last attempt. |  |
| (4) MLAG Configuration | hostname:&lt;hostname&gt;,reason:&lt;MLAG error message&gt; | Error | An error in an MLAG configuration has been detected. For example: Backup IP 10.10.10.1 does not belong to peer. | Review the MLAG configuration on the identified switch. Refer to [Multi-Chassis Link Aggregation - MLAG]({{<ref "cumulus-linux-44/Layer-2/Multi-Chassis-Link-Aggregation-MLAG">}}). Make any needed changes. |
|  | MLAG configuration checks timed out | Error | One or more switches stopped responding to the MLAG checks. |  |
|  | MLAG configuration checks failed | Error | One or more switches failed the MLAG checks. |  |
|  | For switch &lt;hostname&gt;, the MLAG switch with Role: secondary and ClagSysmac: &lt;MAC address&gt; does not exist. | Error | Identified switch is the primary in an MLAG pair, but the defined secondary switch is not in NetQ inventory. | Verify the switch has NetQ Agent 4.1.0 or later installed: click {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/03-Menu/navigation-menu.svg" height="18" width="18" alt="Main Menu">}}, then click <strong>Agents</strong> in the <strong>Network</strong> section, view <strong>Version</strong> column. Upgrade NetQ Agent if needed. Refer to {{<link title="Upgrade NetQ Agents">}}. Add the missing peer switch to NetQ inventory. |
<!-- vale on -->

{{</expand>}}

### Analyze Results

After starting the upgrade you can monitor the progress of your upgrade job and the final results. While the views are different, essentially the same information is available from either the NetQ UI or the NetQ CLI.

{{<tabs "TabID334">}}

{{<tab "NetQ UI">}}

You can track the progress of your upgrade job from the Preview page or the Upgrade History page of the NetQ UI.

{{<notice tip>}}

If you get disconnected while the job is in progress, it might appear as if nothing is happening. Try closing (click {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/close.svg" height="14" width="14">}}) and reopening your view (click {{<img src="https://icons.cumulusnetworks.com/52-Arrows-Diagrams/01-Arrows/arrow-right-1.svg" height="18" width="18">}}), or refreshing the page.

{{</notice>}}

Several viewing options are available for monitoring the upgrade job.

- Monitor the job with full details open on the Preview page:

    {{<figure src="/images/netq/lcm-upgrade-switches-job-upgrading-320.png" width="700" caption="Single role">}}

    {{<figure src="/images/netq/lcm-upgrade-switches-job-upgrading-2-310.png" width="700" caption="Multiple roles and some without roles">}}

<div style="padding-left: 18px;">Each switch goes through a number of steps. To view these steps, click <strong>Details</strong> and scroll down as needed. Click <img src="https://icons.cumulusnetworks.com/52-Arrows-Diagrams/01-Arrows/arrow-up-1.svg" height="18" width="18"/> collapse the step detail. Click <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/close.svg" height="14" width="14"/> to close the detail popup.</div>

- Monitor the job with summary information only in the CL Upgrade History page. Open this view by clicking {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/close.svg" height="14" width="14">}} in the full details view:

    {{<figure src="/images/netq/lcm-upgrade-switches-upg-history-upgrading-summary-320.png" width="700">}}

<div style="padding-left: 18px;">This view is refreshed automatically. Click {{<img src="https://icons.cumulusnetworks.com/52-Arrows-Diagrams/01-Arrows/arrow-down-1.svg" height="18" width="18">}} to view what stage the job is in.</div>

    {{<figure src="/images/netq/lcm-upgrade-switches-upg-history-stage-view-320.png" width="700">}}

<div style="padding-left: 18px;">Click {{<img src="https://icons.cumulusnetworks.com/52-Arrows-Diagrams/01-Arrows/arrow-right-1.svg" height="18" width="18">}} to view the detailed view.</div>

- Monitor the job through the CL Upgrade History card in the **Job History** tab. Click {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/close.svg" height="14" width="14">}} twice to return to the LCM dashboard. As you perform more upgrades the graph displays the success and failure of each job.

    {{<figure src="/images/netq/lcm-cl-upgrade-history-card-inprogress-310.png" width="450">}}

<div style="padding-left: 18px;">Click <strong>View</strong> to return to the Upgrade History page as needed.</div>

### Sample Successful Upgrade

On successful completion, you can:

- Compare the network snapshots taken before and after the upgrade.

    {{<figure src="/images/netq/lcm-upgrade-switches-success-detail-300.png" width="700">}}

<div style="padding-left: 18px;">Click <strong>Compare Snapshots</strong> in the detail view.</div>

    {{<figure src="/images/netq/lcm-upgrade-switches-compare-snapshots-300.png" width="700">}}

<div style="padding-left: 18px;">Refer to {{<link title="#interpreting-the-comparison-data" text="Interpreting the Comparison Data">}} for information about analyzing these results.</div>

- Download details about the upgrade in the form of a JSON-formatted file, by clicking **Download Report**.

- View the changes on the Switches card of the LCM dashboard.

    Click {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/03-Menu/navigation-menu.svg" height="18" width="18" alt="Main Menu">}} Menu, then **Upgrade Switches**.

    {{<figure src="/images/netq/lcm-switches-card-after-upgrade-300.png" width="200">}}

<div style="padding-left: 18px;">In our example, all switches have been upgraded to Cumulus Linux 3.7.12.</div>

### Sample Failed Upgrade

If an upgrade job fails for any reason, you can view the associated error(s):

1. From the CL Upgrade History dashboard, find the job of interest.

    {{<figure src="/images/netq/lcm-upgrade-switches-upg-history-upgrading-summary-320.png" width="700">}}

2. Click {{<img src="https://icons.cumulusnetworks.com/52-Arrows-Diagrams/01-Arrows/arrow-down-1.svg" height="18" width="18">}}.

3. Click {{<img src="https://icons.cumulusnetworks.com/52-Arrows-Diagrams/01-Arrows/arrow-right-1.svg" height="18" width="18">}}.

    {{<figure src="/images/netq/lcm-upgrade-switches-upgrade-error-open-320.png" width="700">}}

<div style="padding-left: 18px;">Note in this example, all of the pre-upgrade tasks were successful, but backup failed on the spine switches.</div>

4. To view what step in the upgrade process failed, click {{<img src="https://icons.cumulusnetworks.com/52-Arrows-Diagrams/01-Arrows/arrow-down-1.svg" height="18" width="18">}} and scroll down. Click {{<img src="https://icons.cumulusnetworks.com/52-Arrows-Diagrams/01-Arrows/arrow-up-1.svg" height="18" width="18">}} to close the step list.

    {{<figure src="/images/netq/lcm-upgrade-switches-upgrade-error-step-320.png" width="200">}}

5. To view details about the errors, either double-click the failed step or click <strong>Details</strong> and scroll down as needed. Click <img src="https://icons.cumulusnetworks.com/52-Arrows-Diagrams/01-Arrows/arrow-up-1.svg" height="18" width="18"/> collapse the step detail. Click <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/close.svg" height="14" width="14"/> to close the detail popup.

    {{<figure src="/images/netq/lcm-upgrade-switches-upgrade-error-message-320.png" width="700">}}

{{</tab>}}

{{<tab "NetQ CLI" >}}

To see the progress of current upgrade jobs and the history of previous upgrade jobs, run `netq lcm show upgrade-jobs cl-image`:

```
cumulus@switch:~$ netq lcm show upgrade-jobs cl-image
Job ID       Name            CL Version           Pre-Check Status                 Warnings         Errors       Start Time
------------ --------------- -------------------- -------------------------------- ---------------- ------------ --------------------
job_cl_upgra Leafs upgr to C 4.2.0                COMPLETED                                                      Fri Sep 25 17:16:10
de_ff9c35bc4 L410                                                                                                2020
950e92cf49ac
bb7eb4fc6e3b
7feca7d82960
570548454c50
cd05802
job_cl_upgra Spines to 4.2.0 4.2.0                COMPLETED                                                      Fri Sep 25 16:37:08
de_9b60d3a1f                                                                                                     2020
dd3987f787c7
69fd92f2eef1
c33f56707f65
4a5dfc82e633
dc3b860
job_upgrade_ 3.7.12 Upgrade  3.7.12               WARNING                                                        Fri Apr 24 20:27:47
fda24660-866                                                                                                     2020
9-11ea-bda5-
ad48ae2cfafb
job_upgrade_ DataCenter      3.7.12               WARNING                                                        Mon Apr 27 17:44:36
81749650-88a                                                                                                     2020
e-11ea-bda5-
ad48ae2cfafb
job_upgrade_ Upgrade to CL3. 3.7.12               COMPLETED                                                      Fri Apr 24 17:56:59
4564c160-865 7.12                                                                                                2020
3-11ea-bda5-
ad48ae2cfafb
```

To see details of a particular upgrade job, run `netq lcm show status job-ID`:

```
cumulus@switch:~$ netq lcm show status job_upgrade_fda24660-8669-11ea-bda5-ad48ae2cfafb
Hostname    CL Version    Backup Status    Backup Start Time         Restore Status    Restore Start Time        Upgrade Status    Upgrade Start Time
----------  ------------  ---------------  ------------------------  ----------------  ------------------------  ----------------  ------------------------
spine02     4.1.0         FAILED           Fri Sep 25 16:37:40 2020  SKIPPED_ON_FAILURE  N/A                   SKIPPED_ON_FAILURE  N/A
spine03     4.1.0         FAILED           Fri Sep 25 16:37:40 2020  SKIPPED_ON_FAILURE  N/A                   SKIPPED_ON_FAILURE  N/A
spine04     4.1.0         FAILED           Fri Sep 25 16:37:40 2020  SKIPPED_ON_FAILURE  N/A                   SKIPPED_ON_FAILURE  N/A
spine01     4.1.0         FAILED           Fri Sep 25 16:40:26 2020  SKIPPED_ON_FAILURE  N/A                   SKIPPED_ON_FAILURE  N/A
```

To see only Cumulus Linux upgrade jobs, run `netq lcm show status cl-image job-ID`.

{{</tab>}}

{{</tabs>}}

### Post-check Failures

A successful upgrade can still have post-check warnings. For example, you updated the OS, but not all services are fully up and running after the upgrade. If one or more of the post-checks fail, warning messages appear in the Post-Upgrade Tasks section of the preview. Click the warning category to view the detailed messages.

{{< expand "Post-check failure messages"  >}}

<table>
<colgroup>
<col style="width: 10%" />
<col style="width: 24%" />
<col style="width: 10%" />
<col style="width: 23%" />
<col style="width: 23%" />
</colgroup>
<thead>
<tr>
<th>Post-check</th>
<th>Message</th>
<th>Type</th>
<th>Description</th>
<th>Corrective Action</th>
</tr>
</thead>
<tbody>
<tr>
<td>Health of Services</td>
<td>Service &lt;service-name&gt; is missing on Host &lt;hostname&gt; for &lt;VRF default|VRF mgmt&gt;.</td>
<td>Warning</td>
<td>A given service is not yet running on the upgraded host. For example: Service ntp is missing on Host Leaf01 for VRF default.</td>
<td>Wait for up to x more minutes to see if the specified services come up.</td>
</tr>
<tr>
<td>Switch Connectivity</td>
<td>Service &lt;service-name&gt; is missing on Host &lt;hostname&gt; for &lt;VRF default|VRF mgmt&gt;.</td>
<td>Warning</td>
<td>A given service is not yet running on the upgraded host. For example: Service ntp is missing on Host Leaf01 for VRF default.</td>
<td>Wait for up to x more minutes to see if the specified services come up.</td>
</tr>
</tbody>
</table>

{{< /expand >}}

### Reasons for Upgrade Job Failure

Upgrades can fail at any of the stages of the process. The following table lists common reasons for upgrade failures:

<!-- vale off -->
| Reason | Error Message |
| --- | --- |
| Switch is not reachable via SSH | Data could not be sent to remote host "192.168.0.15." Make sure this host can be reached over ssh: ssh: connect to host 192.168.0.15 port 22: No route to host |
| Switch is reachable, but user-provided credentials are invalid | Invalid/incorrect username/password. Skipping remaining 2 retries to prevent account lockout: Warning: Permanently added '\<hostname-ipaddr\>' to the list of known hosts. Permission denied, please try again. |
| Upgrade task could not be run | Failure message depends on the why the task could not be run. For example: `/etc/network/interfaces`: No such file or directory |
| Upgrade task failed | Failed at- \<task that failed\>. For example: Failed at- MLAG check for the peerLink interface status |
| Retry failed after five attempts | FAILED In all retries to process the LCM Job |
<!-- vale on -->

## Upgrade Cumulus Linux on Switches Without NetQ Agent Installed

When you want to update Cumulus Linux on switches without NetQ installed, use the switch discovery feature. The feature browses your network to find all Cumulus Linux switches (with and without NetQ currently installed) and determines the versions of Cumulus Linux and NetQ installed. These results are then used to install or upgrade Cumulus Linux and NetQ on all discovered switches in a single procedure rather than in two steps. You can run up to five jobs simultaneously; however, a given switch can only appear in one running job at a time.

To discover switches running Cumulus Linux and upgrade Cumulus Linux and NetQ on them:

{{<tabs "Discover switches" >}}

{{<tab "NetQ UI" >}}


1. Click {{<img src="/images/netq/devices.svg" height="18" width="18">}} Devices in the workbench header, then click **Manage switches**.

2. On the Switches card, click **Discover**.

3. Enter a name for the scan.

    {{<figure src="/images/netq/lcm-discover-search-switches-tab-310.png" width="500">}}

4. Choose whether you want to look for switches by entering IP address ranges OR import switches using a comma-separated values (CSV) file.

    {{<tabs "TabID314" >}}

{{<tab "IP Address Range" >}}

If you do not have a switch listing, then you can manually add the address ranges where your switches are located in the network. This has the advantage of catching switches that might have been missed in a file.

{{<notice tip>}}
A maximum of 50 addresses can be included in an address range. If necessary, break the range into smaller ranges.
{{</notice>}}

To discover switches using address ranges:

1. Enter an IP address range in the **IP Range** field.

    Ranges can be contiguous, for example *192.168.0.24-64*, or non-contiguous, for example *192.168.0.24-64,128-190,235*, but they must be contained within a single subnet.

2. Optionally, enter another IP address range (in a different subnet) by clicking {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/43-Remove-Add/add-circle.svg" height="18" width="18">}}.

    For example, *198.51.100.0-128* or *198.51.100.0-128,190,200-253*.

3. Add additional ranges as needed. Click {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/43-Remove-Add/subtract-circle.svg" height="18" width="18">}} to remove a range if needed.

If you decide to use a CSV file instead, the ranges you entered will remain if you return to using IP ranges again.

{{</tab>}}

{{<tab "CSV Import" >}}

To import switches through a CSV file:

1. Click **Browse**.

2. Select the CSV file containing the list of switches.

    The CSV file must include a header containing *hostname*, *ip*, and *port*. They can be in any order you like, but the data must match that order. For example, a CSV file that represents the Cumulus reference topology could look like this:

    {{<figure src="/images/netq/lcm-import-switches-310.png" width="200">}}

<div style="padding-left: 18px;">or this:</div>

    {{<figure src="/images/netq/lcm-import-switches-2-310.png" width="200">}}

<div style="padding-left: 18px;">
{{<notice note>}}
You must have an IP address in your file, but the hostname is optional. If the port is blank, NetQ uses switch port 22 by default.
{{</notice>}}
</div>

Click **Remove** if you decide to use a different file or want to use IP address ranges instead. If you entered ranges before selecting the CSV file option, they remain.

{{</tab>}}

    {{</tabs>}}

5. Note that you can use the switch access credentials defined in {{<link title="Switch Credentials">}} to access these switches. If you have issues accessing the switches, you might need to update your credentials.

6. Click **Next**.

    When the network discovery is complete, NetQ presents the number of Cumulus Linux switches it found. Each switch can be in one of the following categories:

    - **Discovered without NetQ**: Switches found without NetQ installed
    - **Discovered with NetQ**: Switches found with some version of NetQ installed
    - **Discovered but Rotten**: Switches found that are unreachable
    - **Incorrect Credentials**: Switches found that cannot are unreachable because the provided access credentials do not match those for the switches
    - **OS not Supported**: Switches found that are running Cumulus Linux version not supported by the LCM upgrade feature
    - **Not Discovered**: IP addresses which did not have an associated Cumulus Linux switch

    If the discovery process does not find any switches for a particular category, then it does not display that category.

    {{<figure src="/images/netq/lcm-discover-select-switches-tab-310.png" width="500">}}

7. Select which switches you want to upgrade from each category by clicking the checkbox on each switch card.

    {{<figure src="/images/netq/lcm-discover-select-switches-tab-chosen-switches-310.png" width="500">}}

8. Click **Next**.

9. Verify the number of switches identified for upgrade and the configuration profile to be applied is correct.

10. Accept the default NetQ version or click **Custom** and select an alternate version.

11. By default, the NetQ Agent and CLI are upgraded on the selected switches. If you *do not* want to upgrade the NetQ CLI, click **Advanced** and change the selection to **No**.

12. Click **Next**.

13. Several checks are performed to eliminate preventable problems during the install process.

    {{<figure src="/images/netq/lcm-netq-upgrade-precheck-tab-310.png" width="500">}}

   These checks verify the following:

   - Selected switches are not currently scheduled for, or in the middle of, a Cumulus Linux or NetQ Agent upgrade
   - Selected versions of Cumulus Linux and NetQ Agent are valid upgrade paths
   - All mandatory parameters have valid values, including MLAG configurations
   - All switches are reachable
   - The order to upgrade the switches, based on roles and configurations

   If any of the pre-checks fail, review the error messages and take appropriate action.

   If all of the pre-checks pass, click **Install** to initiate the job.

14. Monitor the job progress.

    After starting the upgrade you can monitor the progress from the preview page or the Upgrade History page.

    From the preview page, a green circle with rotating arrows is shown on each switch as it is working. Alternately, you can close the detail of the job and see a summary of all current and past upgrade jobs on the NetQ Install and Upgrade History page. The job started most recently is shown at the top, and the data is refreshed periodically.

    {{<notice tip>}}
If you are disconnected while the job is in progress, it might appear as if nothing is happening. Try closing (click {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/close.svg" height="14" width="14">}}) and reopening your view (click {{<img src="https://icons.cumulusnetworks.com/52-Arrows-Diagrams/01-Arrows/arrow-right-1.svg" height="18" width="18">}}), or refreshing the page.
    {{</notice>}}

   Several viewing options are available for monitoring the upgrade job.

   - Monitor the job with full details open:

        {{<figure src="/images/netq/lcm-discover-netq-upgrade-inprogress-310.png" width="700">}}

   - Monitor the job with only summary information in the NetQ Install and Upgrade History page. Open this view by clicking {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/close.svg" height="14" width="14">}} in the full details view; useful when you have multiple jobs running simultaneously

        {{<figure src="/images/netq/lcm-netq-upgrade-history-summ-view-310.png" width="700">}}

   - Monitor the job through the NetQ Install and Upgrade History card on the LCM dashboard. Click {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/close.svg" height="14" width="14">}} twice to return to the LCM dashboard.

        {{<figure src="/images/netq/lcm-netq-upgrade-history-card-inprogress-310.png" width="200">}}

15. Investigate any failures and create new jobs to reattempt the upgrade.

{{</tab>}}

{{<tab "NetQ CLI" >}}

If you previously ran a {{<link url="#prepare-for-upgrade" text="discovery job">}}, you can show the results of that job by running the `netq lcm show discovery-job` command.

```
cumulus@switch:~$ netq lcm show discovery-job job_scan_921f0a40-5440-11eb-97a2-5b3ed2e556db
Scan COMPLETED

Summary
-------
Start Time: 2021-01-11 19:09:47.441000
End Time: 2021-01-11 19:09:59.890000
Total IPs: 1
Completed IPs: 1
Discovered without NetQ: 0
Discovered with NetQ: 0
Incorrect Credentials: 0
OS Not Supported: 0
Not Discovered: 1


Hostname          IP Address                MAC Address        CPU      CL Version  NetQ Version  Config Profile               Discovery Status Upgrade Status
----------------- ------------------------- ------------------ -------- ----------- ------------- ---------------------------- ---------------- --------------
N/A               10.0.1.12                 N/A                N/A      N/A         N/A           []                           NOT_FOUND        NOT_UPGRADING
cumulus@switch:~$ 
```

When the network discovery is complete, NetQ presents the number of Cumulus Linux switches it has found. The output displays their discovery status, which can be one of the following:

- **Discovered without NetQ**: Switches found without NetQ installed
- **Discovered with NetQ**: Switches found with some version of NetQ installed
- **Discovered but Rotten**: Switches found that are unreachable
- **Incorrect Credentials**: Switches found that are unreachable because the provided access credentials do not match those for the switches
- **OS not Supported**: Switches found that are running Cumulus Linux version not supported by the LCM upgrade feature
- **NOT\_FOUND**: IP addresses which did not have an associated Cumulus Linux switch

After you determine which switches you need to upgrade, run the upgrade process as described {{<link url="#perform-a-cumulus-linux-upgrade" text="above">}}.

{{</tab>}}

{{</tabs>}}
