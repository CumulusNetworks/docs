---
title: Upgrade NetQ Agent
author: NVIDIA
weight: 670
toc: 4
---

Lifecycle management lets you upgrade to the latest agent version on switches with an existing NetQ Agent. You can upgrade only the NetQ Agent or both the NetQ Agent and NetQ CLI simultaneously. You can run up to five jobs at the same time; however, a given switch can only appear in one running job at a time.

## Prepare for a NetQ Agent Upgrade

Before you upgrade, make sure you have the appropriate files and credentials:

{{<tabs "TabID23" >}}

{{<tab "NetQ UI" >}}

1. Upload the {{<link title="NetQ and Network OS Images/#upload-upgrade-images" text="upgrade images">}}.

2. (Optional) Specify a {{<link title="NetQ and Network OS Images/#specify-a-default-upgrade-version" text="default upgrade version">}}.

3. Verify or add {{<link title="Credentials and Profiles" text="switch access credentials">}}.

{{</tab>}}

{{<tab "NetQ CLI" >}}

1. Verify or add {{<link title="Credentials and Profiles" text="switch access credentials">}}.

2. Configure {{<link title="Credentials and Profiles/#role-management" text="switch roles">}} to determine the order in which the switches get upgraded.

3. Upload the {{<link title="NetQ and Network OS Images/#upload-upgrade-images" text="Cumulus Linux upgrade images">}}.

{{</tab>}}

{{</tabs>}}

## Perform a NetQ Agent Upgrade

After you complete the preparation steps, upgrade the NetQ Agents:

{{<tabs "TabID61" >}}

{{<tab "NetQ UI" >}}

1. From the LCM dashboard, select the **Switch management** tab. Locate the Switches card and click **Manage**.

2. Select the switches you want to upgrade.

3. Click {{<img src="/images/netq/netq-upgrade-icon-blk.png" height="18" width="18">}} **Upgrade NetQ** above the table and follow the steps in the UI.

4. Verify that the number of switches selected for upgrade matches your expectation.

5. Enter a name for the upgrade job. The name can contain a maximum of 22 characters (including spaces).

6. Review each switch:

    - Is the configuration profile the one you want to apply? If not, click **Change config**, then select an alternate profile to apply to all selected switches.

<div style="padding-left: 18px;">

{{<notice tip>}}

You can apply <em>different</em> profiles to switches in a <em>single</em> upgrade job by selecting a subset of switches then choosing a different profile. You can also change the profile on a per-switch basis by clicking the current profile link and selecting an alternate one.

{{<img src="/images/netq/lcm-netq-upgrade-select-alternate-profile-320.png" alt="dialog displaying two profiles that can be applied to both multiple and individual switches" width="450">}}

{{</notice>}}

</div>

7. Review the summary indicating the number of switches and the configuration profile to be used. If either is incorrect, click **Back** and review your selections.

8. Select the version of NetQ Agent for upgrade. If you have designated a default version, keep the **Default** selection. Otherwise, select an alternate version by clicking **Custom** and selecting it from the list.

<div style="padding-left: 18px;">
{{<notice note>}}
By default, the NetQ Agent and CLI are upgraded on the selected switches. If you <em>do not</em> want to upgrade the NetQ CLI, click <strong>Advanced</strong> and change the selection to <strong>No</strong>.
{{</notice>}}
</div>

9. NetQ performs several checks to eliminate preventable problems during the upgrade process. When all of the pre-checks pass, click <strong>Upgrade</strong> to initiate the upgrade.

{{</tab>}}

{{<tab "NetQ CLI" >}}

To upgrade the NetQ Agent on one or more switches, run:

```
netq lcm upgrade netq-image 
    job-name <text-job-name> 
    [netq-version <text-netq-version>] 
    [upgrade-cli True | upgrade-cli False] 
    hostnames <text-switch-hostnames> 
    [config_profile <text-config-profile>]
```

The following example creates a NetQ Agent upgrade job called *upgrade-cl530-nq470*. It upgrades the *spine01* and *spine02* switches with NetQ Agents version 4.7.0.

```
cumulus@switch:~$ netq lcm upgrade netq-image job-name upgrade-cl530-nq470 netq-version 4.7.0 hostnames spine01,spine02
```

<!-- You can assign an order for which switches to upgrade based on the switch roles defined above. For example, to upgrade the spines before the leafs, add the `order ROLE1,ROLE2` option to the command:

    cumulus@switch:~$ netq lcm upgrade name upgrade-3712 image-id cl_image_69ce56d15b7958de5bb8371e9c4bf2fc9131da9a57b13853e2a60ca109238b22 hostnames spine01,spine02,leaf01,leaf02 order spine,leaf

If the switches have not been assigned a role, then do not use the `order` option. So in this example, if switches spine01 and spine02 have not been assigned the _spine_ role, then do not specify the `order spine` option. -->

{{</tab>}}

{{</tabs>}}

## Analyze the NetQ Agent Upgrade Results

After starting the upgrade you can monitor the progress in the NetQ UI. Successful upgrades are indicated by a green {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/check-circle-1.svg" height="16" width="18">}}. Failed upgrades display error messages indicating the cause of failure.

To view the progress of upgrade jobs using the CLI, run:

```
netq lcm show upgrade-jobs netq-image [json]
netq lcm show status <text-lcm-job-id> [json]
```
{{<expand "Example netq lcm show upgrade-jobs">}}

You can view the progress of one upgrade job at a time. This requires the job identifier.

The following example shows all upgrade jobs that are currently running or have completed, and then shows the status of the job with a job identifier of job_netq_install_7152a03a8c63c906631c3fb340d8f51e70c3ab508d69f3fdf5032eebad118cc7.

```
cumulus@switch:~$ netq lcm show upgrade-jobs netq-image json
[
    {
        "jobId": "job_netq_install_7152a03a8c63c906631c3fb340d8f51e70c3ab508d69f3fdf5032eebad118cc7",
        "name": "Leaf01-02 to NetQ330",
        "netqVersion": "4.1.0",
        "overallStatus": "FAILED",
        "pre-checkStatus": "COMPLETED",
        "warnings": [],
        "errors": [],
        "startTime": 1611863290557.0
    }
]

cumulus@switch:~$ netq lcm show status netq-image job_netq_install_7152a03a8c63c906631c3fb340d8f51e70c3ab508d69f3fdf5032eebad118cc7
NetQ Upgrade FAILED

Upgrade Summary
---------------
Start Time: 2021-01-28 19:48:10.557000
End Time: 2021-01-28 19:48:17.972000
Upgrade CLI: True
NetQ Version: 4.1.0
Pre Check Status COMPLETED
Precheck Task switch_precheck COMPLETED
	Warnings: []
	Errors: []
Precheck Task version_precheck COMPLETED
	Warnings: []
	Errors: []
Precheck Task config_precheck COMPLETED
	Warnings: []
	Errors: []


Hostname          CL Version  NetQ Version  Prev NetQ Ver Config Profile               Status           Warnings         Errors       Start Time
                                            sion
----------------- ----------- ------------- ------------- ---------------------------- ---------------- ---------------- ------------ --------------------------
leaf01            4.2.1       4.1.0         3.2.1         ['NetQ default config']      FAILED           []               ["Unreachabl Thu Jan 28 19:48:10 2021
                                                                                                                         e at Invalid
                                                                                                                         /incorrect u
                                                                                                                         sername/pass
                                                                                                                         word. Skippi
                                                                                                                         ng remaining
                                                                                                                         10 retries t
                                                                                                                         o prevent ac
                                                                                                                         count lockou
                                                                                                                         t: Warning:
                                                                                                                         Permanently
                                                                                                                         added '192.1
                                                                                                                         68.200.11' (
                                                                                                                         ECDSA) to th
                                                                                                                         e list of kn
                                                                                                                         own hosts.\r
                                                                                                                         \nPermission
                                                                                                                         denied,
                                                                                                                         please try a
                                                                                                                         gain."]
leaf02            4.2.1       4.1.0         3.2.1         ['NetQ default config']      FAILED           []               ["Unreachabl Thu Jan 28 19:48:10 2021
                                                                                                                         e at Invalid
                                                                                                                         /incorrect u
                                                                                                                         sername/pass
                                                                                                                         word. Skippi
                                                                                                                         ng remaining
                                                                                                                         10 retries t
                                                                                                                         o prevent ac
                                                                                                                         count lockou
                                                                                                                         t: Warning:
                                                                                                                         Permanently
                                                                                                                         added '192.1
                                                                                                                         68.200.12' (
                                                                                                                         ECDSA) to th
                                                                                                                         e list of kn
                                                                                                                         own hosts.\r
                                                                                                                         \nPermission
                                                                                                                         denied,
                                                                                                                         please try a
                                                                                                                         gain."]
```
{{</expand>}}

<!--
### Reasons for NetQ Agent Upgrade Failure

Upgrades can fail at any stage of the process. The following table lists common reasons for upgrade failures:

| Reason | Error Message |
| --- | --- |
| Switch is not reachable via SSH | Data could not be sent to remote host "192.168.0.15." Make sure this host can be reached over ssh: ssh: connect to host 192.168.0.15 port 22: No route to host |
| Switch is reachable, but user-provided credentials are invalid | Invalid/incorrect username/password. Skipping remaining 2 retries to prevent account lockout: Warning: Permanently added '\<hostname-ipaddr\>' to the list of known hosts. Permission denied, please try again. |
| Upgrade task could not be run | Failure message depends on the why the task could not be run. For example: /etc/network/interfaces: No such file or directory |
| Upgrade task failed | Failed at- \<task that failed\>. For example: Failed at- MLAG check for the peerLink interface status |
| Retry failed after five attempts | FAILED In all retries to process the LCM Job |

-->
