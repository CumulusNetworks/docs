---
title: Upgrade NetQ Virtual Machines
author: NVIDIA
weight: 410
toc: 4
---

This page describes how to upgrade your NetQ virtual machines. Note that the upgrade instructions vary depending on NetQ version you’re currently running.

For deployments running:

- 4.8.0, 4.7.0, 4.6.0, or 4.5.0: upgrade directly to NetQ 4.9.0 by following the steps on this page
- 4.4.1, 4.4.0, or 4.3.0: {{<link title="Back Up and Restore NetQ" text="back up your data">}}, then perform a {{<link title="Install the NetQ System" text="new installation of NetQ 4.9.0">}}
- 4.2.0 or earlier: upgrade incrementally {{<exlink url="https://docs.nvidia.com/networking-ethernet-software/cumulus-netq-43/Installation-Management/Upgrade-NetQ/Upgrade-System/" text="to version 4.3.0">}}. Then {{<link title="Back Up and Restore NetQ" text="back up your NetQ data">}} and perform a {{<link title="Install the NetQ System" text="new installation of NetQ 4.9.0">}}

During the upgrade process, NetQ will be temporarily unavailable.

{{%notice infonopad%}}
NetQ 4.9 does not support on-premises, cluster deployments.
{{%/notice%}}

## Before You Upgrade

1. Verify that the admin app is running with the `netq show status` command.

2. Verify that Kubernetes is running with the `kubectl get pods` command.

    If either of these commands display errors, you will not be able to upgrade NetQ. Reset the NetQ server with the `netq bootstrap reset keep-db` command and perform a fresh installation of the tarball with the appropriate {{<link title="install" text="netq install">}} command for your deployment type.

3. {{<link title="Back Up and Restore NetQ" text="Back up your NetQ data">}}. This is an optional step for on-premises deployments. NVIDIA automatically creates backups for NetQ cloud deployments.

## Update NetQ Debian Packages

1. Update `/etc/apt/sources.list.d/cumulus-netq.list` to netq-4.9:

    ```
    cat /etc/apt/sources.list.d/cumulus-netq.list
    deb [arch=amd64] https://apps3.cumulusnetworks.com/repos/deb focal netq-4.9
    ```

2. Update the NetQ `debian` packages. In cluster deployments, update the packages on the master and all worker nodes.

    ```
    cumulus@<hostname>:~$ sudo apt-get update
    Get:1 https://apps3.cumulusnetworks.com/repos/deb focal InRelease [13.8 kB]
    Get:2 https://apps3.cumulusnetworks.com/repos/deb focal/netq-4.9 amd64 Packages [758 B]
    Hit:3 http://archive.ubuntu.com/ubuntu focal InRelease
    Get:4 http://security.ubuntu.com/ubuntu focal-security InRelease [88.7 kB]
    Get:5 http://archive.ubuntu.com/ubuntu focal-updates InRelease [88.7 kB]
    ...
    Reading package lists... Done
    ```

    ```
    cumulus@<hostname>:~$ sudo apt-get install -y netq-agent netq-apps
    Reading package lists... Done
    Building dependency tree
    Reading state information... Done
    ...
    The following NEW packages will be installed:
    netq-agent netq-apps
    ...
    Fetched 39.8 MB in 3s (13.5 MB/s)
    ...
    Unpacking netq-agent (4.9.0-ub20.04u45~1706973134.d2ce145e5) ...
    ...
    Unpacking netq-apps (4.9.0-ub20.04u45~1706973134.d2ce145e5) ...
    Setting up netq-apps (4.9.0-ub20.04u45~1706973134.d2ce145e5) ...
    Setting up netq-agent (4.9.0-ub20.04u45~1706973134.d2ce145e5) ...
    Processing triggers for rsyslog (8.32.0-1ubuntu4) ...
    Processing triggers for man-db (2.8.3-2ubuntu0.1) ...
    ```


## Download the Upgrade Software

1. Download the upgrade tarball.

    {{<netq-install/upgrade-image version="4.9">}}

2. Copy the tarball to the `/mnt/installables/` directory on your NetQ VM.

## Run the Upgrade

{{%notice note%}}

Perform the following steps using the `cumulus` user account.

{{%/notice%}}
### Pre-installation Checks

Verify the following items before upgrading NetQ.

1. Confirm your VM is configured with 16 vCPUs. If your VM is configured with fewer than 16 vCPUs, power off your VM, reconfigure your hypervisor to allocate 16 vCPUs, then power the VM on before proceeding. For cluster deployments, verify these requirements on each node in the cluster.

2. Check if there is sufficient disk space:

```
cumulus@<hostname>:~$ df -h /
Filesystem      Size  Used Avail Use% Mounted on
/dev/sda1       248G   70G  179G  28% /
cumulus@netq-appliance:~$
```
NVIDIA recommends proceeding with the installation only if the `Use%` is less than 70%. You can delete previous software tarballs in the `/mnt/installables/` directory to regain some space. If you cannot decrease disk usage to under 70%, contact the NVIDIA support team.

3. Run the `netq show opta-health` command and check that all pods are in the `READY` state. If the pods are in a state other than `READY`, contact the NVIDIA support team.

4. Confirm that the NetQ CLI is {{<link url="Install-NetQ-CLI/#configure-the-netq-cli" text="properly configured">}}. The `netq show agents` command should complete successfully and display agent status.

5. Ensure that the required ports are open {{<link title="Install the NetQ System" text="according to your deployment model">}}.

{{%notice note%}}

If you are upgrading a cluster deployment to NetQ 4.9.0, you must open TCP port 36443 for Kubernetes control plane operations.

{{%/notice%}}

### Upgrade Using the NetQ CLI

1. Run the appropriate commands for your deployment type:

{{<tabs "tabID142">}}

{{<tab "On-premises Deployments">}}

{{<tabs "On-prem standalone or cluster">}}

{{<tab "Standalone">}}

```
cumulus@<hostname>:~$ netq upgrade bundle /mnt/installables/NetQ-4.9.0.tgz
```

{{%notice info%}}
If this step fails for any reason, run the <code>netq bootstrap reset keep-db</code> command and perform a fresh installation of the tarball with the {{<link title="install/#netq-install-standalone-full" text="netq install standalone full">}} command.
{{%/notice%}}
{{</tab>}}

{{<tab "Cluster">}}

NetQ 4.9 does not support on-premises, cluster deployments.
{{</tab>}}

{{</tabs>}}

{{</tab>}}

{{<tab "Cloud Deployments">}}

{{<tabs "Cloud standalone or cluster">}}

{{<tab "Standalone">}}

```
cumulus@<hostname>:~$ netq upgrade bundle /mnt/installables/NetQ-4.9.0-opta.tgz
```
{{%notice info%}}
If this step fails for any reason, run the <code>netq bootstrap reset keep-db</code> command and perform a fresh installation of the tarball with the {{<link title="install/#netq-install-opta-standalone-full" text="netq install opta standalone full">}} command.
{{%/notice%}}

{{</tab>}}

{{<tab "Cluster">}}

Run the `netq upgrade` command, specifying the current version's tarball and your cluster's virtual IP address. The virtual IP address must be allocated from the same subnet used for your master and worker nodes.

```
cumulus@<hostname>:~$ netq upgrade bundle /mnt/installables/NetQ-4.9.0-opta.tgz cluster-vip <vip-ip>
```
{{%notice info%}}
If this step fails for any reason, run the <code>netq bootstrap reset keep-db</code> command and perform a fresh installation of the tarball with the {{<link title="install/#netq-install-opta-cluster-full" text="netq install opta cluster full">}} command.
{{%/notice%}}

{{</tab>}}

{{</tabs>}}

{{</tab>}}

{{</tabs>}}

2. Confirm the upgrade was successful:

{{<tabs "TabID230" >}}

{{<tab "On-premises VM" >}}

    ```
    cumulus@<hostname>:~$ cat /etc/app-release
    BOOTSTRAP_VERSION=4.9.0
    APPLIANCE_MANIFEST_HASH=8869b5423dfcc441ea56a3c89e680b1b2ad61f6887edccb11676bac893073beb
    APPLIANCE_VERSION=4.9.0
    APPLIANCE_NAME=NetQ On-premises Appliance
    ```
{{</tab>}}

{{<tab "Cloud VM" >}}


    ```
    cumulus@<hostname>:~$ cat /etc/app-release
    BOOTSTRAP_VERSION=4.9.0
    APPLIANCE_MANIFEST_HASH=271f5943ffae42f758fef09bafeb37a63d996bd6e41bf7aeeb3a4d33232f05de
    APPLIANCE_VERSION=4.9.0
    APPLIANCE_NAME=NetQ Cloud Appliance
    ```
{{</tab>}}

{{</tabs>}}

## Next Steps

- {{<link title="Upgrade NetQ Agents">}}