---
title: Upgrade Cumulus Linux Using LCM
author: Cumulus Networks
weight: 580
toc: 4
---
LCM provides the ability to upgrade Cumulus Linux on one or more switches in your network through the NetQ UI or the NetQ CLI. Up to five upgrade jobs can be run simultaneously; however, a given switch can only be contained in one running job at a time.

{{<notice info>}}

Upgrades can be performed between Cumulus Linux 3.x releases, and between Cumulus Linux 4.x releases. <em>Lifecycle management does not support upgrades from Cumulus Linux 3.x to 4.x releases.</em>

{{</notice>}}

## Workflows for Cumulus Linux Upgrades Using LCM

When using the NetQ UI, the workflow is as follows:

{{<figure src="/images/netq/lcm-upgrade-workflow-300.png" width="700">}}

When using the NetQ CLI, the workflow is as follows:

<!-- insert workflow here -->

## Prepare

In preparation for Cumulus Linux upgrade on switches, first perform the following steps:

1. (CLI only) Verify network access to the relevant Cumulus Linux license file.

2. Upload the required Cumulus Linux images. Refer to {{<link title="Manage Cumulus Linux and NetQ Images" text="Manage Cumulus Linux and NetQ Images">}}.

3. (UI only) Optionally, specify a {{<link url="Image-Management/#specify-a-default-upgrade-version" text="default upgrade version">}}.

4. Verify the switches you want to manage are running NetQ Agent 2.4 or later. Refer to {{<link title="Manage Switches" text="Manage Switches">}}.

5. (UI only) Optionally, create a new NetQ {{<link url="Configuration-Management/#create-cumulus-netq-configuration-profiles" text="configuration profile">}}.

6. Configure {{<link title="Manage Switch Credentials" text="switch access credentials">}}.

7. Assign each switch a {{<link title="Role Management" text="role">}} (optional, but strongly recommended).

In the NetQ UI, your LCM dashboard should look similar to this after you have completed these steps:

{{<figure src="/images/netq/lcm-netq-upgrade-dashboard-post-prep-310.png" width="700">}}

## Perform a Cumulus Linux Upgrade

Upgrade Cumulus Linux on switches through either the NetQ UI or NetQ CLI:

{{< tabs "TabID43" >}}

{{< tab "NetQ UI" >}}

1. Click {{<img src="https://icons.cumulusnetworks.com/03-Computers-Devices-Electronics/09-Hard-Drives/hard-drive-1.svg" height="18" width="18">}} (Switches) in any workbench header, then select **Manage switches**.

2. Click **Manage** on the Switches card.

    {{<figure src="/images/netq/lcm-upgrade-switch-manage-button-300.png" width="700">}}

3. Select the switches you want to upgrade. If needed, use the filter to the narrow the listing and find these switches.

    {{<figure src="/images/netq/lcm-switch-mgmt-list-switches-selected-300.png" width="700">}}

4. Click {{<img src="https://icons.cumulusnetworks.com/05-Internet-Networks-Servers/06-Servers/server-upload.svg" height="18" width="18">}} (Upgrade Switches) above the table.

    From this point forward, the software walks you through the upgrade process, beginning with a review of the switches that you selected for upgrade.

    {{<figure src="/images/netq/lcm-upgrade-switches-review-switches-tab-300.png" width="500">}}

5. Give the upgrade job a name. This is required.

    {{<notice tip>}}
    For best presentation, Cumulus Networks recommends keeping the name to a maximum of 22 characters when possible. The name can contain spaces and special characters. If you choose to use longer names, use the distinguishing part of the name at the beginning.
    {{</notice>}}

6. Verify that the switches you selected are included, and that they have the correct IP address and roles assigned.

    - If you accidentally included a switch that you do NOT want to upgrade, hover over the switch information card and click {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/23-Delete/bin-1.svg" height="18" width="18">}} to remove it from the upgrade job.
    - If the role is incorrect or missing, click {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/22-Edit/pencil-1.svg" height="18" width="18">}} to select a role for that switch, then click {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/check-circle-1.svg" height="18" width="18">}}. Click {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/23-Delete/delete-2.svg" height="18" width="18">}} to discard a role change.

    In this example, some of the selected switches do not have roles assigned.

    {{<figure src="/images/netq/lcm-upgrade-switches-review-switches-missing-roles-300.png" width="500">}}
    
7. When you are satisfied that the list of switches is accurate for the job, click **Next**.

8. Verify that you want to use the default Cumulus Linux version for this upgrade job. If not, click **Custom** and select an alternate image from the list.

    {{<figure src="/images/netq/lcm-upgrade-switches-describe-tab-300.png" width="500" caption="Default CL Version Selected">}}{{<figure src="/images/netq/lcm-upgrade-switches-describe-tab-custom-version-300.png" width="500" caption="Custom CL Version Selected">}}

9. Note that the switch access authentication method, *Using global access credentials*, indicates you have chosen either basic authentication with a username and password or SSH key-based authentication for all of your switches. Authentication on a per switch basis is not currently available.

10. Click **Next**.

11. Verify the upgrade job options.

    By default, NetQ takes a network snapshot before the upgrade and then one after the upgrade is complete. It also performs a roll back to the original Cumulus Linux version on any server which fails to upgrade.

    While these options provide a smoother upgrade process and are highly recommended, you have the option to disable these options by clicking **No** next to one or both options.

    {{<figure src="/images/netq/lcm-upgrade-switches-options-tab-300.png" width="500">}}

12. Click **Next**.

13. After the pre-checks have completed successfully, click **Preview**.

    {{<figure src="/images/netq/lcm-upgrade-switches-precheck-tab-success-300.png" width="500">}}

    If one or more of the pre-checks fail, resolve the related issue and start the upgrade again. Expand the following dropdown to view common failures, their causes and corrective actions.

    {{< expand "Pre-check Failure Messages"  >}}

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
<th>Pre-check</th>
<th>Message</th>
<th>Type</th>
<th>Description</th>
<th>Corrective Action</th>
</tr>
</thead>
<tbody>
<tr>
<td>(1) Switch Order</td>
<td>&lt;hostname1&gt; switch cannot be upgraded without isolating &lt;hostname2&gt;, &lt;hostname3&gt; which are connected neighbors. Unable to upgrade</td>
<td>Warning</td>
<td>Hostname2 and hostname3 switches will be isolated during upgrade, making them unreachable. These switches are skipped if you continue with the upgrade.</td>
<td>Reconfigure hostname2 and hostname 3 switches to have redundant connections, or continue with upgrade knowing that you will lose connectivity with these switches during the upgrade process.</td>
</tr>
<tr>
<td>(2) Version Compatibility</td>
<td>Unable to upgrade &lt;hostname&gt; with CL version &lt;3.y.z&gt; to &lt;4.y.z&gt;</td>
<td>Error</td>
<td>LCM only supports CL 3.x to 3.x and CL 4.x to 4.x upgrades</td>
<td>Perform a fresh install of CL 4.x</td>
</tr>
<tr>
<td></td>
<td>Image not uploaded for the combination: CL Version - &lt;x.y.z&gt;, Asic Vendor - &lt;Mellanox | Broadcom&gt;, CPU Arch - &lt;x86 | ARM &gt;</td>
<td>Error</td>
<td>The specified Cumulus Linux image is not available in the LCM repository</td>
<td>Upload missing image. Refer to {{<link title="#Upload Images" text="Upload Images">}}.</td>
</tr>
<tr>
<td></td>
<td>Restoration image not uploaded for the combination: CL Version - &lt;x.y.z&gt;, Asic Vendor - &lt;Mellanox | Broadcom&gt;, CPU Arch - &lt;x86 | ARM &gt;</td>
<td>Error</td>
<td>The specified Cumulus Linux image needed to restore the switch back to its original version if the upgrade fails is not available in the LCM repository. This applies only when the "Roll back on upgrade failure" job option is selected.</td>
<td>Upload missing image. Refer to {{<link title="#Upload Images" text="Upload Images">}}.</td>
</tr>
<tr>
<td></td>
<td>NetQ Agent and NetQ CLI Debian packages are not present for combination: CL Version - &lt;x.y.z&gt;, CPU Arch - &lt;x86 | ARM &gt;</td>
<td>Error</td>
<td>The specified NetQ packages are not installed on the switch.</td>
<td>Upload missing packages. Refer to {{<link title="Install NetQ Agents" text="Install NetQ Agents">}} and {{<link title="Install NetQ CLI" text="Install NetQ CLI">}}.</td>
</tr>
<tr>
<td></td>
<td>Restoration NetQ Agent and NetQ CLI Debian packages are not present for combination: CL Version - &lt;x.y.z&gt;, CPU Arch - &lt;x86 | ARM &gt;</td>
<td>Error</td>
<td>The specified NetQ packages are not installed on the switch.</td>
<td>Install missing packages. Refer to {{<link title="Install NetQ Agents" text="Install NetQ Agents">}} and {{<link title="Install NetQ CLI" text="Install NetQ CLI">}}.</td>
</tr>
<tr>
<td></td>
<td>CL version to be upgraded to and current version on switch &lt;hostname&gt; are the same.</td>
<td>Warning</td>
<td>Switch is already operating the desired upgrade CL version. No upgrade is required.</td>
<td>Choose an alternate CL version for upgrade or remove switch from upgrade job.</td>
</tr>
<tr>
<td>(3) Switch Connectivity</td>
<td>Global credentials are not specified</td>
<td>Error</td>
<td>Switch access credentials are required to perform a CL upgrade, and they have not been specified.</td>
<td>Specify access credentials. Refer to {{<link title="#Specify Switch Credentials" text="Specify Switch Credentials">}}.</td>
</tr>
<tr>
<td></td>
<td>Switch is not in NetQ inventory: &lt;hostname&gt;</td>
<td>Error</td>
<td>LCM cannot upgrade a switch that is not in its inventory.</td>
<td><p>Verify you have the correct hostname or IP address for the switch. </p> <p>Verify the switch has NetQ Agent 2.4.0 or later installed: click {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/03-Menu/navigation-menu.svg" height="18" width="18" alt="Main Menu">}}, then click <strong>Agents</strong> in the <strong>Network</strong> section, view <strong>Version</strong> column. Upgrade NetQ Agents if needed. Refer to {{<link title="Upgrade NetQ Agents">}}.</p></td>
</tr>
<tr>
<td></td>
<td>Switch &lt;hostname&gt; is rotten. Cannot select for upgrade.</td>
<td>Error</td>
<td>LCM must be able to communicate with the switch to upgrade it.</td>
<td>Troubleshoot the connectivity issue and retry upgrade when the switch is fresh.</td>
</tr>
<tr>
<td></td>
<td>Total number of jobs &lt;running jobs count&gt; exceeded Max jobs supported 50</td>
<td>Error</td>
<td>LCM can support a total of 50 upgrade jobs running simultaneously.</td>
<td>Wait for the total number of simultaneous upgrade jobs to drop below 50.</td>
</tr>
<tr>
<td></td>
<td>Switch &lt;hostname&gt; is already being upgraded. Cannot initiate another upgrade.</td>
<td>Error</td>
<td>Switch is already a part of another running upgrade job.</td>
<td>Remove switch from current job or wait until the competing job has completed.</td>
</tr>
<tr>
<td></td>
<td>Backup failed in previous upgrade attempt for switch &lt;hostname&gt;.</td>
<td>Warning</td>
<td>LCM was unable to back up switch during a previously failed upgrade attempt.</td>
<td>You may want to back up switch manually prior to upgrade if you want to restore the switch after upgrade. Refer to [add link here].</td>
</tr>
<tr>
<td></td>
<td>Restore failed in previous upgrade attempt for switch &lt;hostname&gt;.</td>
<td>Warning</td>
<td>LCM was unable to restore switch after a previously failed upgrade attempt.</td>
<td>You may need to restore switch manually after upgrade. Refer to [add link here].</td>
</tr>
<tr>
<td></td>
<td>Upgrade failed in previous attempt for switch &lt;hostname&gt;.</td>
<td>Warning</td>
<td>LCM was unable to upgrade switch during last attempt.</td>
<td></td>
</tr>
<tr>
<td>(4) MLAG Configuration</td>
<td>hostname:&lt;hostname&gt;,reason:&lt;MLAG error message&gt;</td>
<td>Error</td>
<td>An error in an MLAG configuration has been detected. For example: Backup IP 10.10.10.1 does not belong to peer.</td>
<td>Review the MLAG configuration on the identified switch. Refer to {{<exlink url="https://docs.cumulusnetworks.com/cumulus-linux-41/Layer-2/Multi-Chassis-Link-Aggregation-MLAG/" text="Multi-Chassis Link Aggregation-MLAG">}}. Make any needed changes.</td>
</tr>
<tr>
<td></td>
<td>MLAG configuration checks timed out</td>
<td>Error</td>
<td>One or more switches stopped responding to the MLAG checks.</td>
<td></td>
</tr>
<tr>
<td></td>
<td>MLAG configuration checks failed</td>
<td>Error</td>
<td>One or more switches failed the MLAG checks.</td>
<td></td>
</tr>
<tr>
<td></td>
<td>For switch &lt;hostname&gt;, the MLAG switch with Role: secondary and ClagSysmac: &lt;MAC address&gt; does not exist.</td>
<td>Error</td>
<td>Identified switch is the primary in an MLAG pair, but the defined secondary switch is not in NetQ inventory.</td>
<td>Verify the switch has NetQ Agent 2.4.0 or later installed: click {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/03-Menu/navigation-menu.svg" height="18" width="18" alt="Main Menu">}}, then click <strong>Agents</strong> in the <strong>Network</strong> section, view <strong>Version</strong> column. Upgrade NetQ Agent if needed. Refer to {{<link title="Upgrade NetQ Agents">}}. Add the missing peer switch to NetQ inventory.</td>
</tr>
</tbody>
</table>

{{< /expand >}}

14. Review the job preview.

    - When all of your switches have roles assigned, this view displays the chosen job options (top center), the pre-checks status (top right and left in Pre-Upgrade Tasks), the order in which the switches are planned for upgrade (center; upgrade starts from the left), and the post-upgrade tasks status (right).

        {{<figure src="/images/netq/lcm-upgrade-switches-preview-job-300.png" width="700" caption="Roles assigned">}}

    - When none of your switches have roles assigned, this view displays the chosen job options (top center), the pre-checks status (top right and left in Pre-Upgrade Tasks), a list of switches planned for upgrade (center), and the post-upgrade tasks status (right).

        {{<figure src="/images/netq/lcm-upgrade-switches-preview-job-noroles-300.png" width="700" caption="No roles assigned">}}

    - When some of your switches have roles assigned, any switches without roles are upgraded last and are grouped under the label *Stage1*.

        {{<figure src="/images/netq/lcm-upgrade-switches-preview-job-someroles-300.png" width="700" caption="Some roles assigned">}}

15. When you are happy with the job specifications, click **Start Upgrade**.

{{< /tab >}}

{{< tab "NetQ CLI" >}}

1. Get the Cumulus Linux install image ID. Determine the image ID intended to upgrade the switches and copy it.

       cumulus@switch:~$ netq lcm show images
       ID                        Name            CL Version           CPU      ASIC            Last Changed
       ------------------------- --------------- -------------------- -------- --------------- -------------------------
       cl_image_69ce56d15b7958de cumulus-linux-3 3.7.12               x86_64   VX              Fri Apr 24 15:20:02 2020
       5bb8371e9c4bf2fc9131da9a5 .7.12-vx-amd64.
       7b13853e2a60ca109238b22   bin
       cl_image_1187bd949568aba7 cumulus-linux-3 3.7.11               x86_64   VX              Fri Apr 24 14:55:13 2020
       eff1b37b1dec394cb832ceb4d .7.11-vx-amd64.
       94e234d9a1f62deb279c405   bin

1. Perform the upgrade:

       cumulus@switch:~$ netq lcm upgrade name upgrade-3712 cl-version 3.7.12 netq-version 3.1.0 hostnames spine01,spine02 order spine

You can assign an order for which switches to upgrade based on the switch roles defined above. For example, to upgrade the spines before the leafs, add the `order ROLE1,ROLE2` option to the command:

    cumulus@switch:~$ netq lcm upgrade name upgrade-3712 cl-version 3.7.12 netq-version 3.1.0 hostnames spine01,spine02,leaf01,leaf02 order spine,leaf

If the switches have not been assigned a role, then do not use the `order` option. So in this example, if switches spine01 and spine02 have not been assigned the _spine_ role, then do not specify the `order spine` option.

You can decide to run LCM before and after the upgrade by adding the `run-before-after` option to the command:

    cumulus@switch:~$ netq lcm upgrade name upgrade-3712 cl-version 3.7.12 netq-version 3.1.0 hostnames spine01,spine02,leaf01,leaf02 order spine,leaf run-before-after

You can decide to restore LCM when a failure occurs by adding the `run-restore-on-failure` option to the command:

    cumulus@switch:~$ netq lcm upgrade name upgrade-3712 cl-version 3.7.12 netq-version 3.1.0 hostnames spine01,spine02,leaf01,leaf02 order spine,leaf run-restore-on-failure

{{< /tab >}}

{{< /tabs >}}

### Analyze Results

After starting the upgrade you can monitor the progress from the preview page or the Upgrade History page.

From the preview page, a green circle with rotating arrows is shown above each step as it is working. Alternately, you can close the detail of the job and see a summary of all current and past upgrade jobs on the Upgrade History page. The job started most recently is shown at the bottom, and the data is refreshed every minute.

{{<notice tip>}}
If you are disconnected while the job is in progress, it may appear as if nothing is happening. Try closing (click {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/close.svg" height="14" width="14">}}) and reopening your view (click {{<img src="https://icons.cumulusnetworks.com/52-Arrows-Diagrams/01-Arrows/arrow-right-1.svg" height="18" width="18">}}), or refreshing the page.
{{</notice>}}

#### Monitoring the Upgrade

Several viewing options are available for monitoring the upgrade job.

- Monitor the job with full details open:

    {{<figure src="/images/netq/lcm-upgrade-switches-job-upgrading-300.png" width="700">}}

- Monitor the job with summary information only in the Upgrade History page. Open this view by clicking {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/close.svg" height="14" width="14">}} in the full details view:

    {{<figure src="/images/netq/lcm-upgrade-switches-upg-history-upgrading-summary-300.png" width="700">}}

    This view is refreshed automatically. Click {{<img src="https://icons.cumulusnetworks.com/52-Arrows-Diagrams/01-Arrows/arrow-down-1.svg" height="18" width="18">}} to view what stage the job is in.

    {{<figure src="/images/netq/lcm-upgrade-switches-upg-history-stage-view-300.png" width="700">}}

    Click {{<img src="https://icons.cumulusnetworks.com/52-Arrows-Diagrams/01-Arrows/arrow-right-1.svg" height="18" width="18">}} to view the detailed view.

After either a successful or failed upgrade attempt has been performed, a new Upgrade History card appears on your LCM dashboard.

{{<figure src="/images/netq/lcm-upgrade-history-card-300.png" width="200">}}

Click **View** to return to the Upgrade History page as needed.

#### Sample Successful Upgrade

On successful completion, you can:

- Compare the network snapshots taken before and after the upgrade.

    {{<figure src="/images/netq/lcm-upgrade-switches-success-detail-300.png" width="700">}}

    Click **Compare Snapshots** in the detail view.

    {{<figure src="/images/netq/lcm-upgrade-switches-compare-snapshots-300.png" width="700">}}

    Refer to {{<link title="#interpreting-the-comparison-data" text="Interpreting the Comparison Data">}} for information about analyzing these results.

- Download details about the upgrade in the form of a JSON-formatted file, by clicking **Download Report**.

- View the changes on the Switches card of the LCM dashboard.

    Click {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/03-Menu/navigation-menu.svg" height="18" width="18" alt="Main Menu">}}, then **Upgrade Switches**.

    {{<figure src="/images/netq/lcm-switches-card-after-upgrade-300.png" width="200">}}

    In our example, all switches have been upgraded to Cumulus Linux 3.7.12.

Upgrades can be considered successful and still have post-check warnings. For example, the OS has been updated, but not all services are fully up and running after the upgrade. If one or more of the post-checks fail, warning messages are provided in the Post-Upgrade Tasks section of the preview. Click on the warning category to view the detailed messages.

<!-- Expand the following dropdown to view common failures, their causes and corrective actions.

{{< expand "Post-check Failure Messages"  >}}

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
<td>Wait for up to x more minutes to see if the specified services come up. If they do not, xxx.</td>
</tr>
<tr>
<td>Switch Connectivity</td>
<td>Service &lt;service-name&gt; is missing on Host &lt;hostname&gt; for &lt;VRF default|VRF mgmt&gt;.</td>
<td>Warning</td>
<td>A given service is not yet running on the upgraded host. For example: Service ntp is missing on Host Leaf01 for VRF default.</td>
<td>Wait for up to x more minutes to see if the specified services come up. If they do not, xxx.</td>
</tr>
</tbody>
</table>

{{< /expand >}}-->

#### Sample Failed Upgrade

If an upgrade job fails for any reason, you can view the associated error(s):

1. From the Upgrade History dashboard, find the job of interest.

    {{<figure src="/images/netq/lcm-upgrade-switches-upg-history-fail-summary-300.png" width="700">}}

2. Click {{<img src="https://icons.cumulusnetworks.com/52-Arrows-Diagrams/01-Arrows/arrow-down-1.svg" height="18" width="18">}}.

3. Click {{<img src="https://icons.cumulusnetworks.com/52-Arrows-Diagrams/01-Arrows/arrow-right-1.svg" height="18" width="18">}}.

    {{<figure src="/images/netq/lcm-upgrade-switches-upgrade-error-open-300.png" width="700">}}

    Note in this example, all of the pre-upgrade tasks were successful, but backup failed on the spine switches.

4. Double-click on an error to view a more detailed error message.

    This example, shows that the upgrade failure was due to bad switch access credentials. You would need to fix those and then create a new upgrade job.

    {{<figure src="/images/netq/lcm-upgrade-switches-upgrade-error-message-300.png" width="700">}}

#### Reasons for Upgrade Failure

Upgrades can fail at any of the stages of the process, including when backing up data, upgrading the Cumulus Linux software, and restoring the data. Failures can occur when attempting to connect to a switch or perform a particular task on the switch.

Some of the common reasons for upgrade failures and the errors they present:

| Reason | Error Message |
| --- | --- |
| Switch is not reachable via SSH | Data could not be sent to remote host "192.168.0.15". Make sure this host can be reached over ssh: ssh: connect to host 192.168.0.15 port 22: No route to host |
| Switch is reachable, but user-provided credentials are invalid | Invalid/incorrect username/password. Skipping remaining 2 retries to prevent account lockout: Warning: Permanently added '\<hostname-ipaddr\>' to the list of known hosts. Permission denied, please try again. |
| Switch is reachable, but a valid Cumulus Linux license is not installed | 1587866683.880463 2020-04-26 02:04:43 license.c:336 CRIT No license file. No license installed! |
| Upgrade task could not be run | Failure message depends on the why the task could not be run. For example: /etc/network/interfaces: No such file or directory |
| Upgrade task failed | Failed at- \<task that failed\>. For example: Failed at- MLAG check for the peerLink interface status |
| Retry failed after five attempts | FAILED In all retries to process the LCM Job |
