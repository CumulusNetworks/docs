---
title: Upgrade NetQ Software on Your Server
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
This document describes the steps required to upgrade the NetQ Software (versions 2.0.x, 2.1.x, and 2.2.0) installed and running on your own server hardware to NetQ version 2.2.1.

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

| Hardware Component | Minimum On-site Requirement | Minimum Cloud Requirement |
| ---- | ---- | ---- |
| Processor | Eight (8) virtual CPUs | Four (4) virtual CPUs |
| Memory  | 64 GB RAM  | 8 GB RAM |
| Local disk storage | 256 GB SSD (**Note**: This *must* be an SSD; use of other storage options can lead to system instability and are not supported.) | 32 GB (SSD not required) |
| Network interface speed | 1 Gb NIC | 1 Gb NIC |

You must also open the following ports on your hardware to use the NetQ
    software:

| Port  | Deployment Type   | Software Component Access |
| ----- | ----------------- | ------------------------- |
| 31980 | On-site and cloud | NetQ Server             |
| 32708 | On-site           | API Gateway               |
| 32666 | On-site           | Web-based User Interface  |

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
- Ubuntu 16.04 or Ubuntu 18.04 (NetQ 2.2.2 and later)
- Red Hat<sup>®</sup> Enterprise Linux (RHEL) 7.1
- CentOS 7

## Upgrade Cumulus NetQ for an On-premises Deployment

Follow the instructions in this section to upgrade Cumulus NetQ software on your NetQ server that is deployed and managed on your premises. For cloud deployments, refer to [Upgrade Cumulus NetQ for a Cloud Deployment](#upgrade-cumulus-netq-for-a-cloud-deployment).

### On-Premises Upgrade Workflow
Upgrading NetQ involves backing up your data, downloading and installing the new version of NetQ software, restoring your NetQ data, and upgrading and configuring the NetQ Agents.

{{< figure src="/images/netq/upgrade-flow-cust-hw-on-prem-222.png" width="600" >}}

### Backup Your NetQ Data

If you want to save the data you have already collected with an earlier version of Cumulus NetQ, you need to backup that data as follows:

Run the provided backup script to create a backup file in `/opt/<backup-directory>` being sure to replace the `backup-directory` option with the name of the directory you want to use for the backup file.
   ```
   cumulus@<netq-platform/netq-platform>:~$ ./backuprestore.sh --backup --localdir /opt/<backup-directory>
   ```
The file is named `netq_master_snapshot_<timestamp>.tar.gz`. For more detail about the script and the back up process, refer to [Backup NetQ](../../Backup-and-Restore-NetQ/Backup-NetQ).

### Upgrade the NetQ Software

To upgrade the NetQ software on your own hardware using a VM image:

1.  **IMPORTANT**: Confirm that your server hardware meets the
    requirements set out [above](#hardware-requirements).

2.  Download the NetQ software VM upgrade image.
    1.  On the [Cumulus Downloads](https://cumulusnetworks.com/downloads/) page, select *NetQ* from the **Product** list box.
    2.  Click *2.2* from the **Version** list box, and then select
        *2.2.2* from the submenu.
    3.  Optionally, select the hypervisor you wish to use (*VMware* or *KVM*) from the
        **Hypervisor/Platform** list box.

        {{< figure src="/images/netq/NetQ-22-Download-Options-222.png" width="500" >}}

        {{%notice note%}}

For customers with VMware/ESXi OVA deployments, Cumulus Networks recommends deploying a fresh installation of NetQ 2.2.2, rather than performing the upgrade from 2.1.x or 2.2.0, to take advantage of the performance improvements available with the new vmxnet3 and Paravirtualization SCSI drivers. Customers with on-premises deployments must backup their NetQ data prior to the fresh installation to retain their data, and then follow the installation with a restoration. Follow the instructions in [Backup and Restore NetQ](/cumulus-netq/cumulus-netq-deployment-guide/backup-and-restore-netq) and [Install NetQ Software on Your Server](/cumulus-netq/cumulus-netq-deployment-guide/install-netq/#install-netq-software-on-your-server).

        {{%/notice%}}

    4.  Scroll down to review the images that match your selection
        criteria.

        {{< figure src="/images/netq/netq-22-vm-upgrade-222.png" width="400" >}}

    5.  Click **Upgrade** for the relevant version, being careful to
        select the correct deployment version.
3.  From a terminal window, log in to the NetQ Server using your login
    credentials. This example uses the default *cumulus/CumulusLinux\!*
    credentials.

        <computer>:~<username>$ ssh cumulus@netq-platform
        cumulus@netq-platform's password: 
        cumulus@netq-platform:~$ 

4.  Change to the root user.

        cumulus@netq-platform:~$ sudo -i
        [sudo] password for cumulus:
        root@netq-platform:~#

5.  Create an *installables* subdirectory in the mount directory.

        root@netq-platform:~# mkdir -p /mnt/installables/

6.  Copy the upgrade image file, `NetQ-2.2.2.tgz`, into your new directory.

        root@netq-platform:~# cd /mnt/installables/
        root@netq-platform:/mnt/installables# cp /home/usr/dir/NetQ-2.2.2.tgz ./ 

7.  Export the installer script.

        root@netq-platform:/mnt/installables# tar -xvf NetQ-2.2.2.tgz ./netq-install.sh

8.  Verify the contents of the directory. You should have the image file
    and the `netq-install.sh` script.

        root@netq-platform:/mnt/installables# ls -l
        total 9607744
        -rw-r--r-- 1 cumulus cumulus 5911383922 Aug 28 11:13 NetQ-2.2.2.tgz
        -rwxr-xr-x 1 \_lldpd \_lldpd 4309 Aug 28 10:34 netq-install.sh
        root@netq-platform:/mnt/installables#

9.  Configure SSH access.

    {{%notice note%}}

If you perform the upgrade more than once, you can skip this step
    after performing it once.

If you have an existing SSH key, skip to step 9c.

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

            root@netq-platform:/mnt/installables/# ./netq-install.sh --usekey ~/.ssh/id_rsa
            [Fri 30 Aug 2019 06:34:47 AM UTC] - This Script can only be invoked by user: root
            [Fri 30 Aug 2019 06:34:47 AM UTC] - The logged in user is root
            [Fri 30 Aug 2019 06:34:47 AM UTC] - Install directory /mnt/installables exists on system.
            [Fri 30 Aug 2019 06:34:47 AM UTC] - File /root/.ssh/id_rsa exists on system...
            [Fri 30 Aug 2019 06:34:47 AM UTC] - checking the presence of existing instaler-ssh-keys secret/instaler-ssh-keys created
            [Fri 30 Aug 2019 06:34:48 AM UTC] - Unable to find netq-installer up and running. Sleeping for 10 seconds ...
            [Fri 30 Aug 2019 06:34:58 AM UTC] - Unable to find netq-installer up and running. Sleeping for 10 seconds ...
            [Fri 30 Aug 2019 06:35:08 AM UTC] - Able to find the netq-installer up and running...

10.  Upgrade the NetQ software. This example shows an upgrade to version 2.2.2.

        root@netq-platform:/mnt/installables# ./netq-install.sh  --installbundle  /mnt/installables/NetQ-2.2.2.tgz --updateapps
        [Fri 30 Aug 2019 08:18:37 PM UTC] - File /mnt/installables/NetQ-2.2.2.tgz exists on system for updating netq-installer ...
        [Fri 30 Aug 2019 08:18:37 PM UTC] - Check the netq-installer is up and running to process requests ....
        [Fri 30 Aug 2019 08:18:37 PM UTC] - Checking the Status of netq-installer ....
        [Fri 30 Aug 2019 08:18:37 PM UTC] - The netq-installer is up and running ...
        [Fri 30 Aug 2019 08:18:37 PM UTC] - Updating the netq-installer ...
        [Fri 30 Aug 2019 08:18:37 PM UTC] - Able to execute the command for updating netq-installer ...
        [Fri 30 Aug 2019 08:18:37 PM UTC] - Checking initialization of netq-installer update ...
        [Fri 30 Aug 2019 08:18:37 PM UTC] - Update of netq-installer is in progress ...
        ******************************0
        [Fri 30 Aug 2019 08:28:39 PM UTC] - Successfully updated netq installer....
        0,/mnt/installables/NetQ-2.2.1.tgz
        [Fri 30 Aug 2019 08:28:39 PM UTC] - File /mnt/installables/NetQ-2.2.1.tgz exists on system for updating netq apps...
        [Fri 30 Aug 2019 08:28:39 PM UTC] - User selected to update netq-apps ...
        [Fri 30 Aug 2019 08:28:39 PM UTC] - Checking the Status of netq-installer ....
        [Fri 30 Aug 2019 08:28:41 PM UTC] - Unable to find netq-installer up and running. Sleeping for 10 seconds ...
        [Fri 30 Aug 2019 08:29:24 PM UTC] - The netq-installer is up and running ...
        [Fri 30 Aug 2019 08:29:24 PM UTC] - Able to execute the command for netq apps updates ...
        [Fri 30 Aug 2019 08:29:24 PM UTC] - Checking initialization of apps update ...
        [Fri 30 Aug 2019 08:29:29 PM UTC] - netq apps update is in progress ...
        ************************************************************************************************************************************    ******************************************************************************************************************************************************************************
        0
        [Fri 30 Aug 2019 09:20:31 PM UTC] - Successfully updated netq apps ....
        root@netq-platform:/mnt/installables#

    {{%notice note%}}

Please allow about an hour for the upgrade to complete.

    {{%/notice%}}

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

### Restore Your NetQ Data

If you backed up your NetQ data, you can now restore that data. Run the restore script being sure to replace the `backup-directory` option with the name of the directory where the backup file resides.
   ```
   cumulus@<netq-platform/netq-appliance>:~$ ./backuprestore.sh --restore --localdir /opt/<backup-directory>
   ```

This uses the `netq_master_snapshot_<timestamp>.tar.gz` file to restore your data. For more detail about the script and the restoration process, refer to [Restore NetQ](../../Backup-and-Restore-NetQ/Restore-NetQ).

### Update the CLI

Now that the core software is updated, you must update the CLI.

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

### Verify the On-premises Upgrade

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

3.  Continue the NetQ upgrade by upgrading the NetQ Agent on each switch or host you want to monitor. Refer to [Upgrade the NetQ Agents and CLI Access](#upgrade-the-netq-agents-and-cli-access) for instructions.

## Upgrade Cumulus NetQ for a Cloud Deployment

Follow the instructions in this section to upgrade Cumulus NetQ software on your NetQ server that is deployed and managed on your premises, but uses the NetQ Cloud Service applications and data storage. For on-premises deployments, refer to [Upgrade Cumulus NetQ for an On-premises Deployment](#upgrade-cumulus-netq-for-an-on-premises-deployment).

### Cloud Upgrade Workflow
Upgrading NetQ involves backing up your data, downloading and installing the new version of NetQ software, restoring your NetQ data, and upgrading and configuring the NetQ Agents.

{{< figure src="/images/netq/upgrade-flow-cust-hw-cloud-222.png" width="600" >}}
          ```
          cumulus@<netq-platform-hostname>:~$ netq show opta-health
          OPTA is healthy
          ```         

          {{%notice note%}}

    If the results do not indicate the server is healthy after 30 minutes, open a [support ticket](https://cumulusnetworks.com/support/file-a-ticket/) and attach the output of the `opta-support` command.

          {{%/notice%}}


## Upgrade the NetQ Agents and CLI Access

The NetQ Agent should be upgraded on each of the existing nodes you want to monitor to be sure you have the latest functionality and fixes. The node can be a:

  - Switch running Cumulus Linux version 3.3.2 or later
  - Server running Red Hat RHEL 7.1, Ubuntu 16.04 or CentOS 7
  - Linux virtual machine running any of the above Linux operating
    systems

To upgrade the NetQ Agent you need to install the OS-specific meta
package, `cumulus-netq`, on each switch. Optionally, you can install it
on hosts. The meta package contains the NetQ Agent, the NetQ command
line interface (CLI), and the NetQ library. The library contains modules
used by both the NetQ Agent and the CLI.

  - [Upgrade NetQ Agent on a Cumulus Linux Switch](#upgrade-netq-agent-on-a-cumulus-linux-switch)
  - [Upgrade NetQ Agent on an Ubuntu Server](#upgrade-netq-agent-on-an-ubuntu-server)
  - [Upgrade NetQ Agent on a Red Hat or CentOS Server](#upgrade-netq-agent-on-a-red-hat-or-centos-server)

{{%notice info%}}

If your network uses a proxy server for external connections, you should first
[configure a global proxy](/cumulus-linux/System-Configuration/Configuring-a-Global-Proxy/),
so `apt-get` can access the meta package on the Cumulus Networks repository.

{{%/notice%}}

### Upgrade NetQ Agent on a Cumulus Linux Switch

A simple process installs the NetQ Agent on a Cumulus switch.

1.  Edit the `/etc/apt/sources.list` file to add the repository for
    Cumulus NetQ. **Note** that NetQ has a separate repository from
    Cumulus Linux.

        cumulus@switch:~$ sudo nano /etc/apt/sources.list
        ...
        deb http://apps3.cumulusnetworks.com/repos/deb CumulusLinux-3 netq-2.2
        ...

    {{%notice tip%}}

The repository `deb http://apps3.cumulusnetworks.com/repos/deb
    CumulusLinux-3 netq-latest` can be used if you want to always
    retrieve the latest posted version of NetQ.

    {{%/notice%}}

2.  Update the local `apt` repository, then install the NetQ meta
    package on the switch.

        cumulus@switch:~$ sudo apt-get update
        cumulus@switch:~$ sudo apt-get install cumulus-netq

3.  Verify the upgrade.

        cumulus@switch:~$ dpkg -l | grep netq
        ii  cumulus-netq                      2.2.1-cl3u17~155d365432.a60ec9a    all          This meta-package provides installation of Cumulus NetQ packages.
        ii  netq-agent                        2.2.1-cl3u17~1539681411.2bba220    amd64        Cumulus NetQ Telemetry Agent for Cumulus Linux
        ii  netq-apps                         2.2.1-cl3u17~1539681411.2bba220    amd64        Cumulus NetQ Fabric Validation Application for Cumulus Linux

4.  Restart `rsyslog` so log files are sent to the correct destination.

        cumulus@switch:~$ sudo systemctl restart rsyslog.service

5.  Configure the NetQ Agent to send telemetry data to the NetQ Platform.

    {{%notice info%}}

If you intend to use VRF, skip to [Configure the Agent to Use
    VRF](#configure-the-agent-to-use-a-vrf-interface).
    If you intend to specify a port for communication, skip to
    [Configure the Agent to Communicate over a Specific
    Port](#configure-the-agent-to-communicate-over-a-specific-port).

    {{%/notice%}}

    In this example, the IP address for the agent server is *192.168.1.254*.

        cumulus@switch:~$ netq config add agent server 192.168.1.254
        cumulus@switch:~$ netq config restart agent

    This command updates the configuration in the `/etc/netq/netq.yml`
    file.

6.  If you have not already configured CLI access for this switch, you can do so at this time.

   - For on-premises deployment:

        ```
        cumulus@switch:~$ netq config add cli server 192.168.1.254
        cumulus@switch:~$ netq config restart cli
        ```

   - For in-cloud deployment:
      {{%notice info%}}

The switch or host must have access to the Internet to configure CLI access.

      {{%/notice%}}

         Be sure to replace the key values with your user credentials.

           ```
           cumulus@switch:~$ netq config add cli server api.netq.cumulusnetworks.com access-key <text-access-key> secret-key <text-secret-key> port 443
           cumulus@switch:~$ netq config restart cli
           ```
           or, if you have a *credentials.yml* file, be sure to use the full path to the file and the correct file name.
           ```
           cumulus@switch:~$ netq config add cli server api.netq.cumulusnetworks.com cli-keys-file /full-path/credentials.yml port 443
           cumulus@switch:~$ netq config restart cli
           ```

7.  Repeat these steps for each Cumulus switch, or use an automation
    tool to install and configure the NetQ Agent on multiple Cumulus Linux switches.

### Upgrade NetQ Agent on an Ubuntu Server

To install the NetQ Agent on an Ubuntu server:

1.  Reference and update the local `apt` repository.

        root@ubuntu:~# wget -O- https://apps3.cumulusnetworks.com/setup/cumulus-apps-deb.pubkey | apt-key add -

2.  In `/etc/apt/sources.list.d/cumulus-host-ubuntu-xenial.list`, verify
    the following repository is included:

        root@ubuntu:~# vi /etc/apt/sources.list.d/cumulus-apps-deb-xenial.list
        ...
        deb [arch=amd64] https://apps3.cumulusnetworks.com/repos/deb xenial netq-latest
        ...

    {{%notice note%}}

The use of `netq-latest` in this example means that a `get` to the
    repository always retrieves the latest version of NetQ, even in the
    case where a major version update has been made. If you want to keep
    the repository on a specific version — such as `netq-2.2` — use that
    instead.

    {{%/notice%}}

3.  Install the meta package on the server.

        root@ubuntu:~# apt-get update
        root@ubuntu:~# apt-get install cumulus-netq

4.  Verify the upgrade.

        root@ubuntu:~$ dpkg -l | grep netq
        ii  cumulus-netq                      2.2.1-cl3u17~155d345432.a60ec9a    all          This meta-package provides installation of Cumulus NetQ packages.
        ii  netq-agent                        2.2.1-cl3u17~1559c81411.2bba220    amd64        Cumulus NetQ Telemetry Agent for Cumulus Linux
        ii  netq-apps                         2.2.1-cl3u17~1559c81411.2bba220    amd64        Cumulus NetQ Fabric Validation Application for Cumulus Linux

5.  Configure the NetQ Agent to send telemetry data to the NetQ Platform.

    {{%notice info%}}

If you intend to use VRF, skip to [Configure the Agent to Use
    VRF](#configure-the-agent-to-use-a-vrf-interface).
    If you intend to specify a port for communication, skip to
    [Configure the Agent to Communicate over a Specific
    Port](#configure-the-agent-to-communicate-over-a-specific-port).

    {{%/notice%}}

    In this example, the IP address for the agent server is *192.168.1.254*.

    ```
    user@ubuntu:~# netq config add agent server 192.168.1.254
    Updated agent server 192.168.1.254 vrf default. Please restart netq-agent (netq config restart agent).
    user@ubuntu:~# netq config restart agent
    ```
    This command updates the configuration in the `/etc/netq/netq.yml`
    file.

6.  If you have not already configured CLI access for this hosts, you can do so at this time.

   - For on-premises deployment:

        ```
        user@ubuntu:~# netq config add cli server 192.168.1.254
        Updated cli server 192.168.1.254 vrf default. Please restart netqd (netq config restart cli).
        user@ubuntu:~# netq config restart cli
        ```

   - For in-cloud deployment:
      {{%notice info%}}

The switch or host must have access to the Internet to configure CLI access.

      {{%/notice%}}

         Be sure to replace the key values with your user credentials.

         ```
         user@ubuntu:~# netq config add cli server api.netq.cumulusnetworks.com access-key <text-access-key> secret-key <text-secret-key> port 443
         user@ubuntu:~# netq config restart cli
         ```
         or, if you have a *credentials.yml* file, be sure to use the full path to the file and the correct file name.
         ```
         user@ubuntu:~# netq config add cli server api.netq.cumulusnetworks.com cli-keys-file /full-path/credentials.yml port 443
         user@ubuntu:~# netq config restart cli
         ```

9.  Repeat these steps for each switch/host running Ubuntu, or use an
    automation tool to install and configure the NetQ Agent on multiple hosts.

### Upgrade NetQ Agent on a Red Hat or CentOS Server

To upgrade the NetQ Agent on a Red Hat or CentOS server:

1.  Reference and update the local `yum` repository.

        root@rhel7:~# rpm --import https://apps3.cumulusnetworks.com/setup/cumulus-apps-rpm.pubkey
        root@rhel7:~# wget -O- https://apps3.cumulusnetworks.com/setup/cumulus-apps-rpm-el7.repo > /etc/yum.repos.d/cumulus-host-el.repo

2.  Edit `/etc/yum.repos.d/cumulus-host-el.repo` to set the `enabled=1`
    flag for the two NetQ repositories.

        [cumulus@firewall-2 ~]$ cat /etc/yum.repos.d/cumulus-host-el.repo
        [cumulus-arch-netq-2.2]
        name=Cumulus netq packages
        baseurl=http://rohbuild03.mvlab.cumulusnetworks.com/dev/rpm/el/7/netq-latest/$basearch
        gpgcheck=1
        enabled=1

        [cumulus-noarch-netq-2.2]
        name=Cumulus netq architecture-independent packages
        baseurl=http://rohbuild03.mvlab.cumulusnetworks.com/dev/rpm/el/7/netq-latest/noarch
        gpgcheck=1
        enabled=1

        [cumulus-src-netq-2.2]
        name=Cumulus netq source packages
        baseurl=http://rohbuild03.mvlab.cumulusnetworks.com/dev/rpm/el/7/netq-latest/src
        gpgcheck=1
        enabled=1

3.  Update the NetQ meta packages on the server.

        root@rhel7:~# yum update cumulus-netq.x86_64

4.  Verify the upgrade.

        root@ubuntu:~$ yum list installed | grep netq
        ii  cumulus-netq                      2.2.1-cl3u17~15573c5432.a60ec9a    all          This meta-package provides installation of Cumulus NetQ packages.
        ii  netq-agent                        2.2.1-cl3u17~1559b81411.2bba220    amd64        Cumulus NetQ Telemetry Agent for Cumulus Linux
        ii  netq-apps                         2.2.1-cl3u17~1559b81411.2bba220    amd64        Cumulus NetQ Fabric Validation Application for Cumulus Linux

5.  Configure the NetQ Agent to send telemetry data to the NetQ Platform.

      {{%notice info%}}

If you intend to use VRF, skip to [Configure the Agent to Use VRF](#configure-the-agent-to-use-a-vrf-interface). If you intend to specify a port for communication, skip to [Configure the Agent to Communicate over a Specific Port](#configure-the-agent-to-communicate-over-a-specific-port).

      {{%/notice%}}

      In this example, the IP address for the agent server is *192.168.1.254*.

        root@rhel7:~# netq config add agent server 192.168.1.254
        Updated agent server 192.168.1.254 vrf default. Please restart netq-agent (netq config restart agent).
        root@rhel7:~# netq config restart agent

6.  If you have not already configured CLI access for this host, you can do so at this time.
   - For on-premises deployments:

      ```
      root@rhel7:~# netq config add cli server 192.168.1.254
      Updated cli server 192.168.1.254 vrf default. Please restart netqd (netq config restart cli).
      root@rhel7:~# netq config restart cli
      ```

   - For in-cloud deployment:
      {{%notice info%}}

The switch or host must have access to the Internet to configure CLI access.

      {{%/notice%}}

         Be sure to replace the key values with your user credentials.

         ```
         root@rhel7:~# netq config add cli server api.netq.cumulusnetworks.com access-key <text-access-key> secret-key <text-secret-key> port 443
         root@rhel7:~# netq config restart cli
         ```
         or, if you have a *credentials.yml* file, be sure to use the full path to the file and the correct file name.
         ```
         root@rhel7:~# netq config add cli server api.netq.cumulusnetworks.com cli-keys-file /full-path/credentials.yml port 443
         root@rhel7:~# netq config restart cli
         ```

9.  Repeat these steps for each host running Red Hat or CentOS, or use an
    automation tool to install and configure the NetQ Agent on multiple hosts.

## Configure Optional NetQ Agent Settings

Once the NetQ Agents have been installed on the network nodes you want
to monitor, the NetQ Agents must be configured to obtain useful and
relevant data. The code examples shown in this section illustrate how to
configure the NetQ Agent on a Cumulus switch, but it is exactly the same
for the other type of nodes. If you have already configured these
settings, you do not need to do so again.

  - [Configuring the Agent to Use a VRF](#configure-the-agent-to-use-a-vrf-interface)
  - [Configuring the Agent to Communicate over a Specific Port](#configure-the-agent-to-communicate-over-a-specific-port)

### Configure the Agent to Use a VRF Interface

While optional, Cumulus strongly recommends that you configure NetQ
Agents to communicate with the NetQ Platform only via a
[VRF](/cumulus-linux/Layer-3/Virtual-Routing-and-Forwarding-VRF/), including a
[management VRF](/cumulus-linux/Layer-3/Management-VRF/). To do so, you need to
specify the VRF name when configuring the NetQ Agent. For example, if
the management VRF is configured and you want the agent to communicate
with the NetQ Platform over it, configure the agent like this:

    cumulus@leaf01:~$ netq config add agent server 192.168.1.254 vrf mgmt
    cumulus@leaf01:~$ netq config add cli server 192.168.254 vrf mgmt

You then restart the agent:

    cumulus@leaf01:~$ netq config restart agent
    cumulus@leaf01:~$ netq config restart cli

### Configure the Agent to Communicate over a Specific Port

By default, NetQ uses port 8981 for communication between the NetQ
Platform and NetQ Agents. If you want the NetQ Agent to communicate with
the NetQ Platform via a different port, you need to specify the port
number when configuring the NetQ Agent like this:

    cumulus@switch:~$ netq config add agent server 192.168.1.254 port 7379

You then restart the agent:

    cumulus@leaf01:~$ netq config restart agent
