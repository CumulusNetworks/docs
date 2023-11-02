---
title: Upgrade Cumulus Linux
author: NVIDIA
weight: 680
toc: 4
---

 Lifecycle management (LCM) lets you upgrade Cumulus Linux on one or more switches in your network via the NetQ UI or the CLI. You can run up to five upgrade jobs simultaneously; however, a given switch can only appear in one running job at a time.

You can upgrade Cumulus Linux from:
- Cumulus Linux 4.3.0 and 4.3.1 (Broadcom switches)
- Cumulus Linux 5.0.0 and above (Spectrum switches)

You can upgrade switches running Cumulus Linux 5.0.0 or later that are managed with flat configuration files or with NVUE.

{{<notice warning>}}
When you upgrade a switch that has not been configured using NVUE, LCM backs up and restores flat file configurations in Cumulus Linux. After you upgrade a switch that has been managed with flat files and subsequently run NVUE configuration commands, NVUE will overwrite the configuration restored by NetQ LCM. See {{<exlink url="https://docs.nvidia.com/networking-ethernet-software/cumulus-linux/Installation-Management/Upgrading-Cumulus-Linux/" text="Upgrading Cumulus Linux">}} for additional information.
{{</notice>}}
## Prepare for a Cumulus Linux Upgrade

If the NetQ Agent is already installed on the switches you'd like to upgrade, follow the steps below. If the NetQ Agent is *not* installed on the switches you'd like to upgrade, run a {{<link title="Upgrade Cumulus Linux/#Upgrade-Cumulus-Linux-on-Switches-Without NetQ-Agent-Installed" text="switch discovery">}}, then proceed with the upgrade.

Before you upgrade, make sure you have the appropriate files and credentials:

{{<tabs "TabID34" >}}

{{<tab "Preparation Steps">}}

1. Upload the {{<link title="NetQ and Network OS Images/#upload-upgrade-images" text="Cumulus Linux upgrade images">}}.

2. (Optional) Specify a {{<link title="NetQ and Network OS Images/#specify-a-default-upgrade-version" text="default upgrade version">}}.

3. Verify or add {{<link title="Credentials and Profiles" text="switch access credentials">}}.

4. (Optional) Assign a {{<link  title="Switch Management/#assign-roles-to-switches" text="role">}} to each switch.

{{</tab>}}

{{</tabs>}}

## Upgrade Cumulus Linux

After you complete the preparation steps, upgrade Cumulus Linux:

{{<tabs "TabID51" >}}

{{<tab "NetQ UI" >}}

1. Click {{<img src="/images/netq/devices.svg" height="18" width="18">}} **Devices** in any workbench header, then select **Manage switches**.

2. Locate the Switches card and click **Manage**.

3. Select the switches you want to upgrade.

4. Click {{<img src="/images/netq/cl-upgrade-icon-blk.png" height="14" width="18">}} **Upgrade OS** above the table.

    Follow the steps in the UI. Create a name for the upgrade and review the switches that you selected to upgrade:

    {{<figure src="/images/netq/upgrade-switches-450.png" alt="screen displaying 2 switches selected for upgrading" width="550">}}

If you accidentally included a switch that you do *not* want to upgrade, hover over the switch information card and click {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/23-Delete/bin-1.svg" height="18" width="18">}} **Delete** to remove it from the upgrade.
   
If the role is incorrect or missing, click {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/22-Edit/pencil-1.svg" height="18" width="18">}} **Edit**, then select a role for that switch from the dropdown. Click {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/23-Delete/delete-2.svg" height="18" width="18">}} **Cancel** to discard the change.

7. Click **Next**.

8. Select either a {{<link title="NetQ and Network OS Images/#specify-a-default-upgrade-version" text="default image">}} or custom version.

9. Verify or add {{<link title="Credentials and Profiles" text="switch access credentials">}}.

10. Click **Next**.

11. Verify the upgrade job options.

    By default, NetQ performs a roll back to the original Cumulus Linux version on any server which fails to upgrade. It also takes network snapshots before and after the upgrade.

    You can exclude selected services and protocols from the snapshots by clicking them. Node and services must be included.

    {{<figure src="/images/netq/upgrade-switch-options-450.png" width="500">}}

12. Click **Next**.

13. NetQ performs several checks to eliminate preventable problems during the upgrade process. When all of the pre-checks pass, click **Preview**.

14. NetQ directs you to a screen where you can review the upgrade. After reviewing, select **Start upgrade** and confirm.

{{</tab>}}

{{<tab "NetQ CLI" >}}

Perform the upgrade using the `netq lcm upgrade cl-image` command, providing a name for the upgrade job, the Cumulus Linux and NetQ version, and a comma-separated list of the hostname(s) to be upgraded:

```
cumulus@switch:~$ netq lcm upgrade cl-image job-name upgrade-470 cl-version 5.5.0 netq-version 4.7.0 hostnames spine01,spine02
```

### Create a Network Snapshot

You can also generate a network snapshot before and after the upgrade by adding the `run-snapshot-before-after` option to the command:

```
cumulus@switch:~$ netq lcm upgrade cl-image job-name upgrade-470 cl-version 5.5.0 netq-version 4.7.0 hostnames spine01,spine02,leaf01,leaf02 order spine,leaf run-snapshot-before-after
```

### Restore upon an Upgrade Failure

(Recommended) You can restore the previous version of Cumulus Linux if the upgrade job fails by adding the `run-restore-on-failure` option to the command.

```
cumulus@switch:~$ netq lcm upgrade cl-image name upgrade-540 cl-version 5.4.0 netq-version 4.7.0 hostnames spine01,spine02,leaf01,leaf02 order spine,leaf run-restore-on-failure
```

{{</tab>}}

{{</tabs>}}

### Pre-check Failures

If one or more of the pre-checks fail, resolve the related issue and start the upgrade again. In the NetQ UI these failures appear on the Upgrade Preview page. In the NetQ CLI, it appears in the form of error messages in the `netq lcm show upgrade-jobs cl-image` command output.

### Analyze Results

After starting the upgrade you can monitor the progress in the NetQ UI. Successful upgrades are indicated by a green {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/check-circle-1.svg" height="16" width="18">}}. Failed upgrades display error messages indicating the cause of failure.

To view the progress of current upgrade jobs and the history of previous upgrade jobs using the CLI, run `netq lcm show upgrade-jobs cl-image`.

To see details of a particular upgrade job, run `netq lcm show status job-ID`.

To see only Cumulus Linux upgrade jobs, run `netq lcm show status cl-image job-ID`.

Upon successful upgrade, you can:

- {{<link title="#interpreting-the-comparison-data" text="Compare network snapshots">}} taken before and after the upgrade.

- Download details about the upgrade in a JSON-formatted file, by clicking **Download report**.
### Post-check Failures

A successful upgrade can still have post-check warnings. For example, you updated the OS, but not all services are fully up and running after the upgrade. If one or more of the post-checks fail, warning messages appear in the Post-Upgrade Tasks section of the preview. Click the warning category to view the detailed messages.
## Upgrade Cumulus Linux on Switches Without NetQ Agent Installed

To upgrade Cumulus Linux on switches without NetQ installed, create a switch discovery. The discovery searches your network for all Cumulus Linux switches (with and without NetQ currently installed) and determines the versions of Cumulus Linux and NetQ installed. These results are then used to install or upgrade Cumulus Linux and NetQ on all discovered switches in a single procedure rather than in two steps. You can run up to five jobs simultaneously; however, a given switch can only appear in one running job at a time.

To discover switches running Cumulus Linux and upgrade Cumulus Linux and NetQ on those switches:

{{<tabs "Discover switches" >}}

{{<tab "NetQ UI" >}}

1. Click {{<img src="/images/netq/devices.svg" height="18" width="18">}} **Devices** in the workbench header, then click **Manage switches**.

2. On the Switches card, click **Discover**.

3. Enter a name for the scan.

    {{<figure src="/images/netq/discover-switches-profile-450.png" width="500">}}

4. Choose whether you want to look for switches by entering IP address ranges or import switches using a comma-separated values (CSV) file.

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

3. Add additional ranges as needed. Click {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/43-Remove-Add/subtract-circle.svg" height="18" width="18">}} to remove a range.

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

5. Select an access profile from the dropdown menu. If you use Netq-Default you will see a message requesting that you {{<link title="Credentials and Profiles" text= "create or update your credentials">}}.

6. Click **Next**.

    When the network discovery is complete, NetQ presents the number of Cumulus Linux switches it found. Each switch can be in one of the following categories:

    - **Discovered without NetQ**: Switches found without NetQ installed
    - **Discovered with NetQ**: Switches found with some version of NetQ installed
    - **Discovered but Rotten**: Switches found that are unreachable
    - **Incorrect Credentials**: Switches found that are unreachable because the provided access credentials do not match those for the switches
    - **OS not Supported**: Switches found that are running a Cumulus Linux version not supported by LCM upgrades
    - **Not Discovered**: IP addresses which did not have an associated Cumulus Linux switch

    If the discovery process does not find any switches for a particular category, then it does not display that category.

7. Select which switches you want to upgrade from each category by clicking the checkbox on each switch card. Then click **Next**.

    {{<figure src="/images/netq/switch-discovery-selected-450.png" width="500">}}

8. Accept the default NetQ version or click **Custom** and select an alternate version.

9. By default, the NetQ Agent and CLI are upgraded on the selected switches. If you *do not* want to upgrade the NetQ CLI, click **Advanced** and change the selection to **No**.

10. Click **Next**.

11. NetQ performs several checks to eliminate preventable problems during the upgrade process. When all of the pre-checks pass, select **Install**.

    After starting the upgrade you can monitor the progress from the preview page or the Upgrade History page.

{{</tab>}}

{{<tab "NetQ CLI" >}}

Use the {{<link title="lcm/#netq-lcm-discover" text="netq lcm discover">}} command, specifying a single IP address, a range of IP addresses where your switches are located in the network, or a CSV file containing the IP address.

You must also specify the access profile ID, which you can obtain with the `netq lcm show credentials` command.

       cumulus@switch:~$ netq lcm discover ip-range 10.0.1.12 profile_id credential_profile_3eddab251bddea9653df7cd1be0fc123c5d7a42f818b68134e42858e54a9c289
       NetQ Discovery Started with job id: job_scan_4f3873b0-5526-11eb-97a2-5b3ed2e556db

When the network discovery is complete, NetQ presents the number of Cumulus Linux switches it has found. The output displays their discovery status, which can be one of the following:

- **Discovered without NetQ**: Switches found without NetQ installed
- **Discovered with NetQ**: Switches found with some version of NetQ installed
- **Discovered but Rotten**: Switches found that are unreachable
- **Incorrect Credentials**: Switches found that are unreachable because the provided access credentials do not match those for the switches
- **OS not Supported**: Switches found that are running Cumulus Linux version not supported by the LCM upgrade feature
- **NOT\_FOUND**: IP addresses which did not have an associated Cumulus Linux switch

After you determine which switches you need to upgrade, run the upgrade process as described {{<link url="#perform-a-cumulus-linux-upgrade" text="above">}}.

Note that if you previously ran a switch discovery, you can display its results with `netq lcm show discovery-job`:

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

{{</tab>}}

{{</tabs>}}
