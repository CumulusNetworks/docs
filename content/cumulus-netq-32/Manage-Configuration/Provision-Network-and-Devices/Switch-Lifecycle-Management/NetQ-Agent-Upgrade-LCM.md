---
title: Upgrade Cumulus NetQ Agent Using LCM
author: Cumulus Networks
weight: 670
toc: 4
---
The lifecycle management (LCM) feature enables you to upgrade to Cumulus NetQ 3.2.0 on switches with an existing NetQ Agent 2.4.x, 3.0.0, or 3.1.0 release using the NetQ UI. You can upgrade only the NetQ Agent or upgrade both the NetQ Agent and the NetQ CLI at the same time. Up to five jobs can be run simultaneously; however, a given switch can only be contained in one running job at a time.

The upgrade workflow includes the following steps:

{{<figure src="/images/netq/lcm-netq-upgrade-workflow-310.png" width="600">}}

{{<notice info>}}

Upgrades can be performed from NetQ Agents of 2.4.x, 3.0.0, and 3.1.0 releases to the NetQ 3.2.0 release. <em>Lifecycle management does not support upgrades from NetQ 2.3.1 or earlier releases; you must perform a new installation in these cases.</em> Refer to {{<link title="Install NetQ Agents">}}.

{{</notice>}}

## Prepare for a Cumulus NetQ Agent Upgrade

Prepare for NetQ Agent upgrade on switches as follows:

{{< tabs "TabID23" >}}

{{< tab "NetQ UI" >}}

1. Click {{<img src="https://icons.cumulusnetworks.com/03-Computers-Devices-Electronics/09-Hard-Drives/hard-drive-1.svg" height="18" width="18">}} (Switches) in the workbench header, then click **Manage switches**, or click {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/03-Menu/navigation-menu.svg" height="18" width="18" alt="Main Menu">}} (Main Menu) and select **Manage Switches**.

2. Add the {{<link title="Manage Cumulus Linux and NetQ Images/#upload-upgrade-images" text="upgrade images">}}.

3. Optionally, specify a {{<link title="Manage Cumulus Linux and NetQ Images/#specify-a-default-upgrade-version" text="default upgrade version">}}.

4. Verify or add {{<link title="Manage Switch Credentials/#specify-switch-credentials" text="switch access credentials">}}.

5. Optionally, create a new {{<link title="Manage Switch Configurations/#create-cumulus-netq-configuration-profiles" text="switch configuration profile">}}.

Your LCM dashboard should look similar to this after you have completed the above steps:

{{<figure src="/images/netq/lcm-netq-upgrade-dashboard-post-prep-320.png" width="600">}}

{{< /tab >}}

{{< tab "NetQ CLI" >}}

1. Verify or add {{<link title="Manage Switch Credentials/#specify-switch-credentials" text="switch access credentials">}}.

2. Configure {{<link title="Manage Switch Credentials/#role-management" text="switch roles">}} to determine the order in which the switches get upgraded.

3. Upload the {{<link title="Manage Cumulus Linux and NetQ Images/#upload-upgrade-images" text="Cumulus Linux install images">}}.

{{< /tab >}}

{{< /tabs >}}

## Perform a Cumulus NetQ Agent Upgrade

You can upgrade Cumulus NetQ Agents on switches as follows:

{{< tabs "TabID61" >}}

{{< tab "NetQ UI" >}}

1. Click **Manage** on the Switches card.

2. Select the individual switches (or click {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/check-circle-1.svg" height="16" width="18">}} to select all switches) with older NetQ releases that you want to upgrade. If needed, use the filter to narrow the listing and find the relevant switches.

3. Click {{<img src="/images/netq/netq-upgrade-icon-blk.png" height="18" width="18">}} (Upgrade NetQ) above the table.

    From this point forward, the software walks you through the upgrade process, beginning with a review of the switches that you selected for upgrade.

    {{<figure src="/images/netq/lcm-netq-upgrade-review-switches-tab-320.png" width="500">}}

4. Verify that the number of switches selected for upgrade matches your expectation.

5. Enter a name for the upgrade job. The name can contain a maximum of 22 characters (including spaces).

6. Review each switch:

    - Is the NetQ Agent version between 2.4.0 and 3.1.1? If not, this switch can only be upgraded through the {{<link title="Upgrade Cumulus Linux Using LCM/#upgrade-cumulus-linux-on-switches-without-netq-agent-installed" text="switch discovery">}} process.
    - Is the configuration profile the one you want to apply? If not, click **Change config**, then select an alternate profile to apply to all selected switches.

<div style="padding-left: 18px;">

{{<notice tip>}}

You can apply <em>different</em> profiles to switches in a <em>single</em> upgrade job by selecting a subset of switches (click checkbox for each switch) and then choosing a different profile. You can also change the profile on a per switch basis by clicking the current profile link and selecting an alternate one.

{{<img src="/images/netq/lcm-netq-upgrade-select-alternate-profile-320.png" width="450">}}

{{</notice>}}

Scroll down to view all selected switches or use **Search** to find a particular switch of interest.
</div>

7. After you are satisfied with the included switches, click **Next**.

8. Review the summary indicating the number of switches and the configuration profile to be used. If either is incorrect, click **Back** and review your selections.

    {{<figure src="/images/netq/lcm-netq-upgrade-select-version-tab-320.png" width="500">}}

9. Select the version of NetQ Agent for upgrade. If you have designated a default version, keep the **Default** selection. Otherwise, select an alternate version by clicking **Custom** and selecting it from the list.

<div style="padding-left: 18px;">
{{<notice note>}}
By default, the NetQ Agent and CLI are upgraded on the selected switches. If you <em>do not</em> want to upgrade the NetQ CLI, click <strong>Advanced</strong> and change the selection to <strong>No</strong>.
{{</notice>}}
</div>

10. Click **Next**.

11. Several checks are performed to eliminate preventable problems during the upgrade process.

    {{<figure src="/images/netq/lcm-netq-upgrade-precheck-tab-320.png" width="500">}}

<div style="padding-left: 18px;">These checks verify the following when applicable:
<ul>
<li>Selected switches are not currently scheduled for, or in the middle of, a Cumulus Linux or NetQ Agent upgrade</li>
<li>Selected version of NetQ Agent is a valid upgrade path</li>
<li>All mandatory parameters have valid values, including MLAG configurations</li>
<li>All switches are reachable</li>
<li>The order to upgrade the switches, based on roles and configurations</li>
</ul>
<p>If any of the pre-checks fail, review the error messages and take appropriate action.</p>
<p>If all of the pre-checks pass, click <strong>Upgrade</strong> to initiate the upgrade job.</p>
</div>

12. Watch the progress of the upgrade job.

    {{<figure src="/images/netq/lcm-netq-upgrade-inprogress-320.png" width="700">}}

<div style="padding-left: 18px;">You can watch the detailed progress for a given switch by clicking {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/03-Menu/navigation-menu-vertical.svg" height="14" width="14">}}.</div>

    {{<figure src="/images/netq/lcm-netq-upgrade-details-popup-320.png" width="700">}}

13. Click {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/close.svg" height="14" width="14">}} to return to Switches listing.

    For the switches you upgraded, you can verify the version is correctly listed in the **NetQ_Version** column. Click {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/close.svg" height="14" width="14">}} to return to the lifecycle management dashboard.

    The NetQ Install and Upgrade History card is now visible and shows the status of this upgrade job.

    {{<figure src="/images/netq/lcm-netq-upgrade-success-history-card-320.png" width="200">}}

{{< /tab >}}

{{< tab "NetQ CLI" >}}

To upgrade the NetQ Agent on one or more switches, run:

```
netq lcm upgrade name <text-job-name> cl-version <text-cumulus-linux-version> netq-version <text-netq-version> hostnames <text-switch-hostnames> [run-restore-on-failure] [run-before-after]
```

This example creates a NetQ Agent upgrade job called *upgrade-cl410-nq320*. It upgrades the *spine01* and *spine02* switches with NetQ Agents version 3.2.0.

```
cumulus@switch:~$ netq lcm upgrade name upgrade-cl410-nq320 cl-version 4.1.0 netq-version 3.2.0 hostnames spine01,spine02
```

<!-- You can assign an order for which switches to upgrade based on the switch roles defined above. For example, to upgrade the spines before the leafs, add the `order ROLE1,ROLE2` option to the command:

    cumulus@switch:~$ netq lcm upgrade name upgrade-3712 image-id cl_image_69ce56d15b7958de5bb8371e9c4bf2fc9131da9a57b13853e2a60ca109238b22 license LICENSE hostnames spine01,spine02,leaf01,leaf02 order spine,leaf

If the switches have not been assigned a role, then do not use the `order` option. So in this example, if switches spine01 and spine02 have not been assigned the _spine_ role, then do not specify the `order spine` option. -->

Including the `run-restore-on-failure` option restores the switch(es) with their earlier version of NetQ Agent should the upgrade fail. The `run-before-after` option generates a network snapshot before upgrade begins and another when it is completed. The snapshots are visible in the NetQ UI.

{{< /tab >}}

{{< /tabs >}}

## Analyze the NetQ Agent Upgrade Results

After starting the upgrade you can monitor the progress in the NetQ UI. Progress can be monitored from the preview page or the Upgrade History page.

From the preview page, a green circle with rotating arrows is shown on each switch as it is working. Alternately, you can close the detail of the job and see a summary of all current and past upgrade jobs on the NetQ Install and Upgrade History page. The job started most recently is shown at the top, and the data is refreshed periodically.

{{<notice tip>}}
If you are disconnected while the job is in progress, it may appear as if nothing is happening. Try closing (click {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/close.svg" height="14" width="14">}}) and reopening your view (click {{<img src="https://icons.cumulusnetworks.com/52-Arrows-Diagrams/01-Arrows/arrow-right-1.svg" height="18" width="18">}}), or refreshing the page.
{{</notice>}}

### Monitor the NetQ Agent Upgrade Job

Several viewing options are available for monitoring the upgrade job.

- Monitor the job with full details open:

    {{<figure src="/images/netq/lcm-netq-upgrade-inprogress-320.png" width="700">}}

- Monitor the job with only summary information in the NetQ Install and Upgrade History page. Open this view by clicking {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/close.svg" height="14" width="14">}} in the full details view; useful when you have multiple jobs running simultaneously.

    {{<figure src="/images/netq/lcm-netq-upgrade-history-summ-view-320.png" width="700">}}

    When multiple jobs are running, scroll down or use the filters above the jobs to find the jobs of interest:

    - **Time Range**: Enter a range of time in which the upgrade job was created, then click **Done**.
    - **All switches**: Search for or select individual switches from the list, then click **Done**.
    - **All switch types**: Search for or select individual switch series, then click **Done**.
    - **All users**: Search for or select individual users who created an upgrade job, then click **Done**.
    - **All filters**: Display all filters at once to apply multiple filters at once. Additional filter options are included here. Click **Done** when satisfied with your filter criteria.

    By default, filters show *all* of that items of the given filter type until it is restricted by these settings.

- Monitor the job through the NetQ Install and Upgrade History card on the LCM dashboard. Click {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/close.svg" height="14" width="14">}} twice to return to the LCM dashboard.

    {{<figure src="/images/netq/lcm-netq-upgrade-history-card-inprogress-310.png" width="200">}}

### Sample Successful NetQ Agent Upgrade

This example shows that all four of the selected switches were upgraded successfully. You can see the results in the Switches list as well.

{{<figure src="/images/netq/lcm-netq-upgrade-example-success-310.png" width="700">}}

### Sample Failed NetQ Agent Upgrade

This example shows that an error has occurred trying to upgrade two of the four switches in a job. The error indicates that the access permissions for the switches are invalid. In this case, you need to modify the {{<link title="Manage Switch Inventory and Roles/#modify-switch-credentials" text="switch access credentials">}} and then create a new upgrade job.

{{<figure src="/images/netq/lcm-netq-upgrade-example-failure-310.png" width="700">}}

If you were watching this job from the LCM dashboard view, click **View** on the NetQ Install and Upgrade History card to return to the detailed view to resolve any issues that occurred.

<!--CLI

To view the progress of upgrade jobs, run:

```
netq lcm show upgrade-jobs [json]
netq lcm show status <text-lcm-job-id> [json]
```

You can view the progress of one upgrade job at a time. To do so, you first need the job identifier and then you can view the status of that job.

This example shows all upgrade jobs that are currently running or have completed, and then shows the status of the job with a job identifier of xxx.

```
cumulus@switch:~$ netq lcm show upgrade-jobs
xxx

cumulus@switch:~$ netq lcm show status xxx
xxx
```
-->

### Reasons for NetQ Agent Upgrade Failure

Upgrades can fail at any of the stages of the process, including when backing up data, upgrading the Cumulus NetQ software, and restoring the data. Failures can also occur when attempting to connect to a switch or perform a particular task on the switch.

Some of the common reasons for upgrade failures and the errors they present:

| Reason | Error Message |
| --- | --- |
| Switch is not reachable via SSH | Data could not be sent to remote host "192.168.0.15". Make sure this host can be reached over ssh: ssh: connect to host 192.168.0.15 port 22: No route to host |
| Switch is reachable, but user-provided credentials are invalid | Invalid/incorrect username/password. Skipping remaining 2 retries to prevent account lockout: Warning: Permanently added '\<hostname-ipaddr\>' to the list of known hosts. Permission denied, please try again. |
| Switch is reachable, but a valid Cumulus Linux license is not installed | 1587866683.880463 2020-04-26 02:04:43 license.c:336 CRIT No license file. No license installed! |
| Upgrade task could not be run | Failure message depends on the why the task could not be run. For example: /etc/network/interfaces: No such file or directory |
| Upgrade task failed | Failed at- \<task that failed\>. For example: Failed at- MLAG check for the peerLink interface status |
| Retry failed after five attempts | FAILED In all retries to process the LCM Job |
