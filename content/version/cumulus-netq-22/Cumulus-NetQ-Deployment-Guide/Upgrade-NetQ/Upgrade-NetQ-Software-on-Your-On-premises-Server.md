---
title: Upgrade NetQ Software on Your On-premises Server
author: Cumulus Networks
weight: 125
aliases:
 - /display/NETQ/Upgrade+from+NetQ+2.0\/2.1+to+NetQ+2.2.x
 - /pages/viewpage.action?pageId=12321007
pageID: 12321007
product: Cumulus NetQ
version: 2.2
imgData: cumulus-netq-22
siteSlug: cumulus-netq-22
---
This document describes the steps required to upgrade the NetQ Software (versions 2.0.0 through 2.2.1) installed and running on your own server hardware to NetQ version 2.2.2.

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

  - The minimum supported Cumulus Linux version for NetQ 2.2.x is 3.3.2.
  - You must upgrade your NetQ Agents as well as the NetQ Platform.
  - You can upgrade to NetQ 2.2.x without upgrading Cumulus Linux.
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
| Processor          | Eight (8) virtual CPUs |
| Memory             | 64 GB RAM |
| Local disk storage | 256 GB SSD (**Note**: This *must* be an SSD; use of other storage options can lead to system instability and are not supported.) |
| Network interface speed | 1 Gb NIC |

You must also open the following ports on your hardware to use the NetQ
    software:

| Port  | Software Component Access |
| ----- | ------------------------- |
| 31980 | NetQ Server               |
| 32708 | API Gateway               |
| 32666 | Web-based User Interface  |

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
- Ubuntu 16.04 (NetQ 2.x.x)
- Ubuntu 18.04 (NetQ 2.2.2 and later)
- Red Hat<sup>®</sup> Enterprise Linux (RHEL) 7.1
- CentOS 7

## Perform an In-place Upgrade of Cumulus NetQ

An in-place upgrade is recommended for upgrades from Cumulus NetQ 2.2.1. If you are upgrading from NetQ 2.2.0 or earlier, a [disk image upgrade](#perform-a-disk-image-upgrade-of-cumulus-netq) is recommended.

### In-place Upgrade Workflow
Upgrading NetQ in place involves downloading and installing the new version of NetQ applications, and upgrading and configuring the NetQ Agents. While optional, upgrading the CLI is recommended.

{{<figure src="/images/netq/upgrade-wkflow-on-prem-in-place-cust-hw-222.png" width="600">}}

### Download the NetQ Virtual Machine Upgrade Image

The first step in upgrading your on-premises NetQ Server is to obtain the VM upgrade image:

1.  **IMPORTANT**: Confirm that your server hardware meets the
    requirements set out [above](#hardware-requirements).

2.  On the [Cumulus Downloads](https://cumulusnetworks.com/downloads/) page, select *NetQ* from the **Product** list box.
3.  Click *2.2* from the **Version** list box, and then select *2.2.2* from the submenu.
4.  Optionally, select the hypervisor you wish to use (*VMware* or *KVM*) from the
  **Hypervisor/Platform** list box.

     {{< figure src="/images/netq/NetQ-22-Download-Options-222.png" width="500" >}}

     {{%notice note%}}

For customers with VMware/ESXi OVA deployments, Cumulus Networks recommends deploying a fresh installation of NetQ 2.2.2, rather than performing the upgrade from 2.1.x or 2.2.0, to take advantage of the performance improvements available with the new vmxnet3 and Paravirtualization SCSI drivers. Customers with on-premises deployments must backup their NetQ data prior to the fresh installation to retain their data, and then follow the installation with a restoration. Follow the instructions in [Backup and Restore NetQ](../../Backup-and-Restore-NetQ/) and [Install NetQ Software on Your Server](../../Install-NetQ/Install-NetQ-Software-on-Your-Server/).

        {{%/notice%}}

4.  Scroll down to review the images that match your selection criteria.

      {{< figure src="/images/netq/netq-22-vm-upgrade-222.png" width="400" >}}

5.  Click **Upgrade** for the relevant version, being careful to
  select the correct deployment version.

### Run the Installation Script

You must first store the downloaded file in a location where the installation script can find it, export the installer script from the tgz file, and configure SSH access (if this is the first time you have upgraded this server).

1.  From a terminal window, log in to the NetQ Server using your login
    credentials. This example uses the default *cumulus/CumulusLinux\!*
    credentials.

        <computer>:~<username>$ ssh cumulus@netq-platform
        cumulus@netq-platform's password: 
        cumulus@netq-platform:~$ 

2.  Change to the root user.

        cumulus@netq-platform:~$ sudo -i
        [sudo] password for cumulus:
        root@netq-platform:~#

3.  Create an *installables* subdirectory in the mount directory.

        root@netq-platform:~# mkdir -p /mnt/installables/

4.  Copy the upgrade image file, `NetQ-2.2.2.tgz`, into your new directory.

        root@netq-platform:~# cd /mnt/installables/
        root@netq-platform:/mnt/installables# cp /home/usr/dir/NetQ-2.2.2.tgz ./ 

5.  Export the installer script.

        root@netq-platform:/mnt/installables# tar -xvf NetQ-2.2.2.tgz ./netq-install.sh

6.  Verify the contents of the directory. You should have the image file
    and the `netq-install.sh` script.

        root@netq-platform:/mnt/installables# ls -l
        total 9607744
        -rw-r--r-- 1 cumulus cumulus 5911383922 Aug 28 11:13 NetQ-2.2.2.tgz
        -rwxr-xr-x 1 \_lldpd \_lldpd 4309 Aug 28 10:34 netq-install.sh
        root@netq-platform:/mnt/installables#

7.  Configure SSH access.

    {{%notice note%}}

If you perform the upgrade more than once, you can skip this step
    after performing it once. If you have an existing SSH key, skip to step 7c.

    {{%/notice%}}

    1.  Generate the SSH key to enable you to run the script.

        {{%notice note%}}

Leave the passphrase blank to simplify running the script.

        {{%/notice%}}

            root@netq-platform:/mnt/installables# ssh-keygen -t rsa -b 4096
            Generating public/private rsa key pair.
            Enter file in which to save the key (/root/.ssh/id_rsa):
            Created directory '/root/.ssh'.
            Enter passphrase (empty for no passphrase):
            Enter same passphrase again:
            Your identification has been saved in /root/.ssh/id_rsa.
            Your public key has been saved in /root/.ssh/id_rsa.pub.

    2.  Copy the key to the `authorized_keys` directory.

            root@netq-platform:/mnt/installables# cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys
            root@netq-platform:/mnt/installables# chmod 0600 ~/.ssh/authorized_keys
            root@netq-platform:/mnt/installables#

    3.  Associate the key with the installer.

```
root@netq-platform:/mnt/installables/# ./netq-install.sh --usekey ~/.ssh/id_rsa
[Tue Aug 27 04:50:07 2019] - File /root/.ssh/id_rsa exists on system...
[Tue Aug 27 04:50:08 2019] - checking the presence of existing installer-ssh-keys
[Tue Aug 27 04:50:08 2019] - Able to find existence of secret key ..
[Tue Aug 27 04:50:08 2019] - Re-generating the newer installer-ssh-keys ...
[Tue Aug 27 04:50:08 2019] - Successfully created newer installer-ssh-keys ...
[Tue Aug 27 04:50:08 2019] - Re-generating the older instaler-ssh-keys ...
[Tue Aug 27 04:50:08 2019] - Successfully created older instaler-ssh-keys ...
[Tue Aug 27 04:50:08 2019] - Validating the status of netq-installer-deploy pod ...
[Tue Aug 27 04:50:08 2019] - Able to find netq-installer-deploy pod: netq-installer-deploy-56dc64b6f9-bk2lj
[Tue Aug 27 04:50:08 2019] - Terminating the netq-installer-deploy pod: netq-installer-deploy-56dc64b6f9-bk2lj
[Tue Aug 27 04:50:09 2019] - Successfully terminated netq-installer-deploy pod: netq-installer-deploy-56dc64b6f9-bk2lj ...
[Tue Aug 27 04:50:09 2019] - Checking the Status of netq-installer ....
[Tue Aug 27 04:50:09 2019] - The netq-installer is up and running ...
```

8.  Run the installation script to upgrade the NetQ software.

```
root@netq-platform:/mnt/installables# ./netq-install.sh  --installbundle  /mnt/installables/NetQ-2.2.2.tgz --updateapps
[Tue Aug 27 04:51:29 2019] - Updating the netq-installer ...
[Tue Aug 27 04:51:29 2019] - Able to execute the command for updating netq-installer ...
[Tue Aug 27 04:51:29 2019] - Checking initialization of netq-installer update ...
[Tue Aug 27 04:51:29 2019] - Update of netq-installer is in progress ...
******************************************0
[Tue Aug 27 05:05:30 2019] - Validating the update of netq installer....

...

[Tue Aug 27 05:07:47 2019] - Checking the Status of netq-installer ....
[Tue Aug 27 05:07:47 2019] - The netq-installer is up and running ...
[Tue Aug 27 05:07:47 2019] - Able to execute the command for netq apps updates ...
[Tue Aug 27 05:07:47 2019] - Checking initialization of apps update ...
[Tue Aug 27 05:07:52 2019] - netq apps update is in progress ...
****************************************************0
[Tue Aug 27 05:54:54 2019] - Successfully updated netq apps ....
[Tue Aug 27 05:54:54 2019] - Updating the release informatio on system...
[Tue Aug 27 05:54:54 2019] - Successfully finished netq apps update procedure.
[Tue Aug 27 05:54:54 2019] - Refer logs:/var/log/netq/netq_upgrade.log for more details !
root@netq-platform:/mnt/installables#
```

    {{%notice note%}}

Please allow about an hour for the upgrade to complete.

    {{%/notice%}}

9. Verify the release has been updated successfully.

```
root@netq-platform:/mnt/installables# cat /etc/app-release
APPLIANCE_VERSION=2.2.2
APPLIANCE_MANIFEST_HASH=a7f3cda
```

{{%notice info%}}

If you have changed the IP Address or hostname of the NetQ Platform, you need to
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

### Install and Configure the CLI

While optional, it is useful to have the updated CLI running on your server.

1. Verify your `/etc/apt/sources.list` file has the repository reference for Cumulus NetQ.  

   ```
   cumulus@switch:~$ sudo nano /etc/apt/sources.list
   ...
   deb http://apps3.cumulusnetworks.com/repos/deb CumulusLinux-3 netq-2.2
   ...
   ```

2. Update the local `apt` repository, then install the NetQ apps package on the switch.

   ```
   cumulus@switch:~$ sudo apt-get update
   cumulus@switch:~$ sudo apt-get install netq-apps
   ```

3. Configure the CLI server, using the IP address of your NetQ server.

   ```
   cumulus@switch:~$ netq config add cli server 192.168.1.254
   cumulus@switch:~$ netq config restart cli
   ```

### Verify the Operation of NetQ on Your Server

1. Run the `netq show opta-health` command to verify all applications are operating properly. Please allow 10-15 minutes for all applications to come up and report their status.

```
cumulus@<netq-platform-hostname>:~$ netq show opta-health
   Application                    Status    Health    Kafka Stream    Git Hash    Timestamp
   -----------------------------  --------  --------  --------------  ----------  ------------------------
   netq-app-macfdb                UP        true      up              14b42e6     Mon Jun  3 20:20:35 2019
   netq-app-interface             UP        true                      0fe11c6     Mon Jun  3 20:20:34 2019
   netq-app-vlan                  UP        true                      4daed85     Mon Jun  3 20:20:35 2019
   netq-app-sensors               UP        true      up              f37272c     Mon Jun  3 20:20:34 2019
   netq-app-topology              UP        true                      3f4a887     Mon Jun  3 20:20:34 2019
   kafka-broker                   UP                                              Mon Jun  3 20:20:35 2019
   netq-app-mstpinfo              UP        true      up              ef5565d     Mon Jun  3 20:20:35 2019
   netq-app-address               UP        true      up              7e0d03d     Mon Jun  3 20:20:35 2019
   netq-gui                       UP                                              Mon Jun  3 20:20:35 2019
   netq-app-kube                  UP        true      up              fbcaa9d     Mon Jun  3 20:20:34 2019
   netq-app-link                  UP        true      up              6c2b21a     Mon Jun  3 20:20:35 2019
   netq-app-ptm                   UP        true      up              7162771     Mon Jun  3 20:20:34 2019
   netq-opta                      UP        true                                  Mon Jun  3 20:20:34 2019
   netq-app-clagsession           UP        true      up              356dda9     Mon Jun  3 20:20:34 2019
   netq-endpoint-gateway          UP        true                      295e9ed     Mon Jun  3 20:20:34 2019
   netq-app-ospf                  UP        true      up              e0e2ab0     Mon Jun  3 20:20:34 2019
   netq-app-lldp                  UP        true      up              90582de     Mon Jun  3 20:20:35 2019
   netq-app-inventory             UP        true      up              bbf9938     Mon Jun  3 20:20:34 2019
   netq-app-tracecheck-scheduler  UP        true                      5484c68     Mon Jun  3 20:20:34 2019
   netq-app-infra                 UP        true      up              13f9e7c     Mon Jun  3 20:20:34 2019
   kafka-connect                  UP                                              Mon Jun  3 20:20:35 2019
   netq-app-search                UP        true      up              e47aaba     Mon Jun  3 20:20:34 2019
   netq-app-procdevstats          UP        true      up              b8e280e     Mon Jun  3 20:20:34 2019
   netq-app-vxlan                 UP        true      up              123c577     Mon Jun  3 20:20:34 2019
   zookeeper                      UP                                              Mon Jun  3 20:20:35 2019
   netq-app-resource-util         UP        true      up              41dfb07     Mon Jun  3 20:20:34 2019
   netq-app-evpn                  UP        true      up              05a4003     Mon Jun  3 20:20:34 2019
   netq-api-gateway               UP        true                      c40231a     Mon Jun  3 20:20:34 2019
   netq-app-port                  UP        true      up              4592b70     Mon Jun  3 20:20:35 2019
   netq-app-macs                  UP        true                      dd6cd96     Mon Jun  3 20:20:35 2019
   netq-app-notifier              UP        true      up              da57b69     Mon Jun  3 20:20:35 2019
   netq-app-events                UP        true      up              8f7b4d9     Mon Jun  3 20:20:34 2019
   netq-app-services              UP        true      up              5094f4a     Mon Jun  3 20:20:34 2019
   cassandra                      UP                                              Mon Jun  3 20:20:35 2019
   netq-app-configdiff            UP        true      up              3be2ef1     Mon Jun  3 20:20:34 2019
   netq-app-neighbor              UP        true      up              9ebe479     Mon Jun  3 20:20:35 2019
   netq-app-bgp                   UP        true      up              e68f7a8     Mon Jun  3 20:20:35 2019
   schema-registry                UP                                              Mon Jun  3 20:20:35 2019
   netq-app-lnv                   UP        true      up              a9ca80a     Mon Jun  3 20:20:34 2019
   netq-app-healthdashboard       UP        true                      eea044c     Mon Jun  3 20:20:34 2019
   netq-app-ntp                   UP        true      up              651c86f     Mon Jun  3 20:20:35 2019
   netq-app-customermgmt          UP        true                      7250354     Mon Jun  3 20:20:34 2019
   netq-app-node                  UP        true      up              f676c9a     Mon Jun  3 20:20:34 2019
   netq-app-route                 UP        true      up              6e31f98     Mon Jun  3 20:20:35 2019
```
      {{%notice note%}}

If any of the applications or services display Status as DOWN after 30 minutes, open a [support ticket](https://cumulusnetworks.com/support/file-a-ticket/) and  attach the output of the `opta-support` command.

      {{%/notice%}}

2.  Verify that NTP is configured and running. NTP operation is critical to proper operation of NetQ. Refer to [Setting Date and Time](/cumulus-linux/System-Configuration/Setting-Date-and-Time/) in the *Cumulus Linux User Guide* for details and instructions.

3.  Continue the NetQ upgrade by upgrading the NetQ Agent on each switch or host you want to monitor. Refer to [Upgrade the NetQ Agents and CLI on Your Switches and Hosts](#upgrade-the-netq-agents-and-cli-on-your-switches-and-hosts) for instructions.

## Perform a Disk Image Upgrade of Cumulus NetQ

A disk image upgrade is recommended for upgrades from Cumulus NetQ 2.2.0 and earlier. If you are upgrading from NetQ 2.2.1, an [in-place upgrade](#perform-an-in-place-upgrade-of-cumulus-netq) is sufficient.

### Disk Image Upgrade Workflow

Upgrading NetQ using a disk image involves backing up your NetQ data, downloading and installing the new version of NetQ software, restoring your data, and configuring the NetQ Agents. While optional, upgrading the CLI is recommended.

{{< figure src="/images/netq/upgrade-wkflow-on-prem-disk-img-cust-hw-222.png" width="700" >}}

Please follow the instructions in the following topics in this order:

1. [Backup Your NetQ Data](../../Backup-and-Restore-NetQ/Backup-NetQ/)
2. [Download and Install the New Software](../../Install-NetQ/Install-NetQ-Software-on-Your-Server/)
3. [Restore Your NetQ Data](../../Backup-and-Restore-NetQ/Restore-NetQ/)
4. [Install and Configure NetQ Agent and CLI on Switches and Hosts](../../Install-NetQ/Install-NetQ-Software-on-Your-Server/#install-and-configure-the-netq-agent-and-cli-access)
