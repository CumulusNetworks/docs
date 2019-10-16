---
title: Upgrade NetQ Software on Your Cloud Server
author: Cumulus Networks
weight: 127
aliases:
 - /display/NETQ/Upgrade+from+NetQ+2.0\/2.1+to+NetQ+2.2.x
 - /pages/viewpage.action?pageId=12321007
pageID: 12321007
product: Cumulus NetQ
version: 2.3
imgData: cumulus-netq
siteSlug: cumulus-netq
---
This document describes the steps required to upgrade the NetQ Software (versions 2.0 through 2.2) installed and running on your NetQ cloud server to NetQ version 2.3.

{{%notice info%}}

Cumulus Networks recommends upgrading NetQ only during a network
maintenance window.

{{%/notice%}}

{{%notice note%}}

Events generated during the upgrade process will not be available in the
database. Once the upgrade process is complete, the NetQ Agents resynchronize with
the current state of the Host or Cumulus Linux switch with the NetQ
Server.

{{%/notice%}}

## Prerequisites

Before you begin the upgrade process, please note the following:

  - The minimum supported Cumulus Linux version for NetQ 2.3.x is 3.3.2.
  - You must upgrade your NetQ Agents as well as the NetQ Platform.
  - You can upgrade to NetQ 2.3.x without upgrading Cumulus Linux.
  - The NetQ installer pod `netq-installer` should be up in either the
    *Containercreating* or *Running* state. The `netq-installer` pod
    state could also be *ContainerCreating*, in which case the host is
    initializing with the SSH keys.

### Hardware Requirements

Cumulus NetQ software is supported on a variety of hardware.

{{%notice info%}}

Confirm that your hardware meets these *minimum* requirements to upgrade the VM.

{{%/notice%}}

The NetQ software requires a server with the following:

| Hardware Component | Minimum Requirement |
| ------------------ | ------------------- |
| Processor | Four (4) virtual CPUs |
| Memory  | 8 GB RAM |
| Local disk storage | 32 GB (SSD not required) |
| Network interface speed | 1 Gb NIC |

You must also open port 31980 on your hardware to use the NetQ
    software.

### NetQ Platform HyperVisor Requirements

The NetQ Platform can be installed as a Virtual Machine (VM) using one
    of the following hypervisors:

- VMware ESXi™ 6.5 for servers running Cumulus Linux, CentOS, Ubuntu
        and RedHat operating systems.
- KVM/QCOW (QEMU Copy on Write) image for servers running CentOS,
        Ubuntu and RedHat operating systems.

### NetQ Agent Operating System Requirements

NetQ 2.2 Agents are supported on the following switch and host operating
    systems:

- Cumulus Linux 3.3.2 and later
- Ubuntu 16.04 (NetQ 2.x.x and later)
- Ubuntu 18.04 (NetQ 2.2.2 and later)
- Red Hat<sup>®</sup> Enterprise Linux (RHEL) 7.1
- CentOS 7

## Perform an In-place Upgrade of Cumulus NetQ

An in-place upgrade is recommended for upgrades from Cumulus NetQ 2.2.1 or 2.2.2. If you are upgrading from NetQ 2.2.0 or earlier, a [disk image upgrade](#perform-a-disk-image-upgrade-of-Cumulus-NetQ) is recommended.

### In-place Upgrade Workflow
Upgrading NetQ involves backing up your data, downloading and installing the new version of NetQ software, restoring your NetQ data, and upgrading and configuring the NetQ Agents.

{{< figure src="/images/netq/upgrade-wkflow-in-place-cloud-cust-hw-222.png" width="600" >}}

### Download the NetQ Software

To upgrade the NetQ software on your own hardware using a VM image:

1.  **IMPORTANT**: Confirm that your server hardware meets the
    requirements set out [above](#hardware-requirements).

2.  On the [Cumulus Downloads](https://cumulusnetworks.com/downloads/) page, select *NetQ* from the **Product** list box.

3.  Click *2.3* from the **Version** list box, and then select
  *2.3.0* from the submenu.

4.  Optionally, select the hypervisor you wish to use (*VMware (Cloud)* or *KVM (Cloud)*) from the
  **Hypervisor/Platform** list box.

     {{< figure src="/images/netq/netq-23-download-options-230.png" width="500" >}}

     {{%notice note%}}

For customers with VMware/ESXi OVA deployments, Cumulus Networks recommends deploying a fresh installation of NetQ 2.2.2, rather than performing the upgrade from 2.1.x or 2.2.0, to take advantage of the performance improvements available with the new vmxnet3 and Paravirtualization SCSI drivers.

        {{%/notice%}}

5.  Scroll down to review the images that match your selection
  criteria.

      {{< figure src="/images/netq/netq-23-vm-cloud-upgrade-230.png" width="400" >}}

6.  Click **Upgrade** for the relevant version, being careful to
  select the correct deployment version.

### Install and Configure the CLI

You must upgrade the CLI to make use of the modified upgrade command. Additionally, the access and secret keys generated for previous releases must be changed. NetQ now uses symmetric keys instead of the asymmetric keys.

1. Verify your `/etc/apt/sources.list` file has the repository reference for Cumulus NetQ.  

  ```
  cumulus@switch:~$ sudo nano /etc/apt/sources.list
  ...
  deb http://apps3.cumulusnetworks.com/repos/deb CumulusLinux-3 netq-2.3
  ...
  ```

2. Update the local `apt` repository, then install the NetQ apps package on the switch.

  ```
  cumulus@switch:~$ sudo apt-get update
  cumulus@switch:~$ sudo apt-get install netq-apps
  ```  

3. Generate new access and secret keys for users.

    1. Open the NetQ UI.

    2. Click <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/03-Menu/navigation-menu.svg", width="18", height="18"/>, then select *Management* in the **Admin** column.

        {{< figure src="/images/netq/main-menu-mgmt-selected.png" width="400">}}

    3. Click **Manage** on the User Accounts card.

    4. Select a user and click **Delete AuthKeys** in the Edit menu.

        {{< figure src="/images/netq/delete-auth-keys-230.png" width="700">}}

    5. Select the user again and click **Generate AuthKeys**.

    6. Copy these keys to a safe place.

        {{%notice info%}}
The secret key is only shown once. If you don't copy these, you will need to regenerate them and reconfigure CLI access.

In version 2.2.1 and later, if you created a keys file, you can add these keys to that file.
        {{%/notice%}}

4. Repeat these steps for all other users who should have CLI access.

5. Configure the CLI server, using the IP address of your NetQ server, the keys you just generated, and the name of the premises (if you have more than one).

```
cumulus@switch:~$ netq config add cli server 192.168.1.254 access-key <user-access-key> secret-key <user-secret-key> premises <premises-name> port 443
Successfully logged into NetQ cloud at 192.168.1.254 port 443

cumulus@switch:~$ netq config restart cli
Restarting NetQ CLI... Success!
```

### Run the Upgrade Command

1. Use the `netq upgrade opta` command to install the VM you downloaded above.

```
cumulus@switch:~$ netq upgrade opta tarball NetQ-2.3.0-opta.tgz
```

2. Verify the release has been updated successfully.

```
cumulus@switch:~$ cat /etc/app-release
APPLIANCE_VERSION=2.3.0
APPLIANCE_MANIFEST_HASH=a7c3cda
```

{{%notice info%}}

If you have changed the IP Address or hostname of the NetQ server, you need to
re-register this address or hostname with the Kubernetes containers before you can
continue.

1.  Reset all Kubernetes administrative settings. Run the command twice
    to make sure all directories and files have been reset.

    ```
    cumulus@switch:~$ sudo kubeadm reset -f  
    cumulus@switch:~$ sudo kubeadm reset -f
    ```

2.  Remove the Kubernetes configuration.  
    ```
    cumulus@switch:~$ sudo rm /home/cumulus/.kube/config
    ```

3.  Reset the NetQ Platform install daemon.  
    ```
    cumulus@switch:~$ sudo systemctl reset-failed
    ```

4.  Reset the Kubernetes service.  
    ```
    cumulus@switch:~$ sudo systemctl restart cts-kubectl-config
    ```  
    **Note**: Allow 15 minutes for the prompt to return.

{{%/notice%}}

### Verify the Operation of NetQ on Your Server

1. Run the `netq show opta-health` command to verify all applications are operating properly. Please allow 10-15 minutes for all applications to come up and report their status.

```
cumulus@<netq-platform-hostname>:~$ netq show opta-health
OPTA is healthy
```         

      {{%notice note%}}

If the results do not indicate the server is healthy after 30 minutes, open a [support ticket](https://cumulusnetworks.com/support/file-a-ticket/) and attach the output of the `opta-support` command.

      {{%/notice%}}

2.  Verify that NTP is configured and running. NTP operation is critical to proper operation of NetQ. Refer to [Setting Date and Time](/cumulus-linux/System-Configuration/Setting-Date-and-Time/) in the *Cumulus Linux User Guide* for details and instructions.

3.  Continue the NetQ upgrade by upgrading the NetQ Agent on each switch or host you want to monitor. Refer to [Install the NetQ Agent and CLI on Switches](../../Install-NetQ-Agents-and-CLI-on-Switches) for instructions.

## Perform a Disk Image Upgrade of Cumulus NetQ

A disk image upgrade is recommended for upgrades from Cumulus NetQ 2.2.0 or earlier. An [in-place upgrade](#perform-an-in-place-upgrade-of-Cumulus-NetQ) is recommended for upgrades from NetQ 2.2.1 or 2.2.2.

### Disk Image Upgrade Workflow
Upgrading NetQ involves backing up your data, downloading and installing the new version of NetQ software, restoring your NetQ data, and upgrading and configuring the NetQ Agents.

{{< figure src="/images/netq/upgrade-wkflow-disk-img-cloud-cust-hw-222.png" width="600" >}}

Please follow the instructions in the following topics in this order:

1. [Backup Your NetQ Data](../../Backup-and-Restore-NetQ/Backup-NetQ/)

2. [Download and Install the New Software](../../Install-NetQ/Install-NetQ-Software-on-Your-Server/)

3. [Restore Your NetQ Data](../../Backup-and-Restore-NetQ/Restore-NetQ/)

4. [Install and Configure NetQ Agent and CLI on Switches and Hosts](../../Install-NetQ/Install-NetQ-Agents-and-CLI-on-Switches)
