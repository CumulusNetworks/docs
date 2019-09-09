---
title: Upgrade NetQ Software on Your NetQ Appliance
author: Cumulus Networks
weight: 127
aliases:
 - /display/NETQ/Upgrade+the+NetQ+Appliance
 - /pages/viewpage.action?pageId=12321037
pageID: 12321037
product: Cumulus NetQ
version: 2.2
imgData: cumulus-netq-22
siteSlug: cumulus-netq-22
---
This document describes the steps required to upgrade the NetQ Software (versions 2.1.0 through 2.2.1) installed and running on your NetQ or NetQ Cloud Appliances to NetQ version 2.2.2.

{{%notice info%}}

Cumulus Networks recommends only upgrading NetQ during a network
maintenance window.

{{%/notice%}}

{{%notice note%}}

Events generated during the upgrade process will not be available in the
database. Once the upgrade process is complete, the NetQ Agents resynchronize with
the current state of the Host or Cumulus Linux switch with the NetQ or NetQ Cloud
Appliance.

{{%/notice%}}

## Prerequisites

Before you begin the upgrade process, please note the following:

  - Cumulus recommends upgrading your NetQ Agents to obtain the latest
    features and bug fixes, but it is not required.
  - The NetQ installer pod `netq-installer` should be up in either the
    *Containercreating* or *Running* state. The `netq-installer` pod
    state could also be *ContainerCreating*, in which case the host is
    initializing with the SSH keys.

## Perform an In-place Upgrade of Cumulus NetQ

An in-place upgrade is recommended for upgrades from Cumulus NetQ 2.2.1. If you are upgrading from NetQ 2.2.0 or earlier, a [disk image upgrade](#perform-a-disk-image-upgrade-of-cumulus-netq) is recommended.

### In-place Upgrade Workflow
Upgrading NetQ in place involves downloading and installing the new version of NetQ applications, and upgrading and configuring the NetQ Agents. While optional, upgrading the CLI is recommended.

{{< figure src="/images/netq/upgrade-wkflow-on-prem-in-place-nqappl-222.png" width="600" >}}

### Download Appliance Upgrade Image

The first step in upgrading your NetQ Appliance is to obtain the appliance upgrade image:

1.  On the [Cumulus Downloads](https://cumulusnetworks.com/downloads/) page, select *NetQ* from the **Product** list box.

2.  Click *2.2* from the **Version** list box, and then select
  *2.2.2* from the submenu.

3.  From the **Hypervisor/Platform** list box, select *Appliance*.

      {{< figure src="/images/netq/NetQ-22-Download-Options-222.png" width="500" >}}

4.  Click **Upgrade**.

      {{< figure src="/images/netq/netq-22-nqappl-upgrade-222.png" width="200" >}}

### Run the Installation Script

You must first store the downloaded file in a location where the installation script can find it, export the installer script from the tgz file, and configure SSH access (if this is the first time you have upgraded this server).

1.  From a terminal window, log in to the appliance using your
login credentials. This example uses the default
*cumulus/CumulusLinux\!* credentials, on a NetQ Appliance.

        <computer>:~<username>$ ssh cumulus@netq-appliance
        cumulus@netq-appliance's password: 
        cumulus@netq-appliance:~$ 

2.  Change to the root user.

        cumulus@netq-appliance:~$ sudo -i
        [sudo] password for cumulus:
        root@netq-appliance:~#

3.  Copy the upgrade package (`NetQ-2.2.2.tgz`) into your new directory.

        root@netq-appliance:~# cd /mnt/installables/
        root@netq-appliance:/mnt/installables# cp /home/usr/dir/NetQ-2.2.2.tgz ./ 

4.  Export the installer script.

        root@netq-appliance:/mnt/installables# tar -xvf NetQ-2.2.2.tgz ./netq-install.sh

5.  Verify the contents of the directory. You should have the package
    and the `netq-install.sh` script.
```
        root@netq-appliance:/mnt/installables# ls -l
        total 9607744
        -rw-r--r-- 1 cumulus cumulus 5911383922 Jul 23 11:13 NetQ-2.2.2.tgz
        -rwxr-xr-x 1 _lldpd _lldpd 4309 Jul 23 10:34 netq-install.sh
        root@netq-appliance:/mnt/installables#
```
6.  Configure SSH access.

    {{%notice note%}}

If you perform the upgrade more than once, you can skip this step after performing it once. If you have an existing SSH key, skip to step 6c.

    {{%/notice%}}

    1.  Generate the SSH key to enable you to run the script.

        {{%notice note%}}

Leave the passphrase blank to simplify running the script.

        {{%/notice%}}

            root@netq-appliance:/mnt/installables# ssh-keygen -t rsa -b 4096
            Generating public/private rsa key pair.
            Enter file in which to save the key (/root/.ssh/id_rsa):
            Created directory '/root/.ssh'.
            Enter passphrase (empty for no passphrase):
            Enter same passphrase again:
            Your identification has been saved in /root/.ssh/id_rsa.
            Your public key has been saved in /root/.ssh/id_rsa.pub.

    2.  Copy the key to the `authorized_keys` directory.

            root@netq-appliance:/mnt/installables# cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys
            root@netq-appliance:/mnt/installables# chmod 0600 ~/.ssh/authorized_keys
            root@netq-appliance:/mnt/installables#

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

7.  Run the installation script to upgrade the NetQ software.

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

8. Verify the release has been updated successfully.

```
root@netq-platform:/mnt/installables# cat /etc/app-release
APPLIANCE_VERSION=2.2.2
APPLIANCE_MANIFEST_HASH=a7f3cda
```
{{%notice info%}}

If you have changed the IP Address or hostname of your appliance, you need to
re-register this address with the Kubernetes containers before you can
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

Now that the core software is updated, you must update the CLI.

1. Edit the `/etc/apt/sources.list` file to add the repository for Cumulus NetQ.  

   ```
   cumulus@switch:~$ sudo nano /etc/apt/sources.list
   ...
   deb http://apps3.cumulusnetworks.com/repos/deb CumulusLinux-3 netq-2.2
   ...
   ```

2. Update the local `apt` repository, then install the NetQ apps  package on the switch.

   ```
   cumulus@switch:~$ sudo apt-get update
   cumulus@switch:~$ sudo apt-get install netq-apps
   ```

3. Configure the CLI server, using the IP address assigned to your CLI server.

   ```
   cumulus@switch:~$ netq config add cli server 192.168.1.254
   cumulus@switch:~$ netq config restart cli
   ```

### Verify the Operation of NetQ on Your Appliance

1. Run the `netq show opta-health` command to verify all applications are
    operating properly. Please allow 10-15 minutes for all applications to come up and report their status.

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

3.  Continue the NetQ upgrade by loading the NetQ Agent on each switch or host you want to monitor. Refer to [Upgrade the NetQ Agents and CLI on Your Switches and Hosts](#upgrade-the-netq-agents-and-cli-on-your-switches-and-hosts) for instructions.

## Perform a Disk Image Upgrade of Cumulus NetQ

A disk image upgrade is recommended for upgrades from Cumulus NetQ 2.2.0 and earlier. If you are upgrading from NetQ 2.2.1, an [in-place upgrade](#perform-an-in-place-upgrade-of-cumulus-netq) is sufficient.

### Disk Image Upgrade Workflow

Upgrading NetQ using a disk image involves backing up your NetQ data, downloading and installing the new version of NetQ software, restoring your data, and configuring the NetQ Agents. While optional, upgrading the CLI is recommended.

{{< figure src="/images/netq/upgrade-wkflow-disk-img-on-prem-nqappl-222.png" width="700" >}}

### Backup Your NetQ Data

If you want to retain the data you have already collected with an earlier version of Cumulus NetQ, you need to backup that data as follows:

Run the provided backup script to create a backup file in `/opt/<backup-directory>` being sure to replace the `backup-directory` option with the name of the directory you want to use for the backup file.
 ```
 cumulus@<netq-appliance>:~$ ./backuprestore.sh --backup --localdir /opt/<backup-directory>
 ```
The file is named `netq_master_snapshot_<timestamp>.tar.gz`. For more detail about the script and the back up process, refer to [Backup NetQ](../../Backup-and-Restore-NetQ/Backup-NetQ).

### Download the NetQ Software Image

The next step is to obtain the new image.

1.  On the [Cumulus Downloads](https://cumulusnetworks.com/downloads/) page, select *NetQ* from the **Product** list box.

2.  Click *2.2* from the **Version** list box, and then select
  *2.2.2* from the submenu.

3.  From the **Hypervisor/Platform** list box, select *Appliance*.

      {{< figure src="/images/netq/NetQ-22-Download-Options-222.png" width="500" >}}

4.  Click **Download**.

      {{< figure src="/images/netq/netq-22-nqappl-dwnld-222.png" width="200" >}}

### Install the Image Using ONIE

ONIE is an open source project (equivalent to PXE on servers) that enables the installation of network operating systems (NOS) on a bare metal switch. Use the `onie-install -a -i <image-location>` command to install the image from the web or local file.

- This example installs the image from a web server, then reboots the appliance.

```
cumulus@netq-platform:~$ sudo onie-install -a -i http://10.0.1.251/cumulus-netq-server-2.2.2-ts-amd64.bin && sudo reboot
```

- This example installs the image from a local file, then reboots the appliance.

```
cumulus@netq-platform:~$ sudo onie-install -a -i /home/<local-directory>/<path>/cumulus-netq-server-2.2.2-ts-amd64.bin && sudo reboot
```

### Restore Your NetQ Data

Restore the configuration files to the new release. Run the restore script being sure to replace the `backup-directory` option with the name of the directory where the backup file resides.

 ```
 cumulus@<netq-platform/netq-appliance>:~$ ./backuprestore.sh --restore --localdir /opt/<backup-directory>
 ```

This uses the `netq_master_snapshot_<timestamp>.tar.gz` file to restore your data. For more detail about the script and the restoration process, refer to [Restore NetQ](../../Backup-and-Restore-NetQ/Restore-NetQ).

### Verify the Operation of NetQ on Your Appliance

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

3.  Continue the NetQ upgrade by upgrading the NetQ Agent on each switch or host you want to monitor. Refer to the next section for instructions.

## Upgrade the NetQ Agents and CLI on Your Switches and Hosts

The NetQ Agent should be upgraded on each of the existing nodes you want
to monitor. The node can be a:

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

###  Upgrade NetQ Agent on a Cumulus Linux Switch

A simple process ugprades the NetQ Agent on a Cumulus switch.

1.  Edit the `/etc/apt/sources.list` file to add the repository for Cumulus NetQ.
    **Note** that NetQ has a separate repository from Cumulus Linux.  

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

```
cumulus@netq-appliance:~$ cat /etc/app-release
APPLIANCE_VERSION=2.2.2
APPLIANCE_MANIFEST_HASH=a7f3cda

cumulus@netq-appliance:~$ dpkg -l | grep netq
ii  cumulus-netq                      2.2.2-cl3u17~155734b432.a60ec9a    all          This meta-package provides installation of Cumulus NetQ packages.
ii  netq-agent                        2.2.2-cl3u17~1559c81411.2bba220    amd64        Cumulus NetQ Telemetry Agent for Cumulus Linux
ii  netq-apps                         2.2.2-cl3u17~15596814a1.2bba220    amd64        Cumulus NetQ Fabric Validation Application for Cumulus Linux
```

4.  Restart `rsyslog` so log files are sent to the correct destination.

        cumulus@switch:~$ sudo systemctl restart rsyslog.service

5.  Configure the NetQ Agent to send telemetry data to the NetQ Platform.

      {{%notice info%}}

If you intend to use VRF, skip to [Configure the Agent to Use            VRF](#configure-the-agent-to-use-a-vrf-interface). If you intend to specify a port for communication, skip to [Configure the Agent to Communicate over a Specific Port](#configure-the-agent-to-communicate-over-a-specific-port).

      {{%/notice%}}

      In this example, the IP address for the agent server is *192.168.1.254*.

         cumulus@switch:~$ netq config add agent server 192.168.1.254
         cumulus@switch:~$ netq config restart agent

      This command updates the configuration in the `/etc/netq/netq.yml` file.

6.  Optionally, configure the updated CLI on this switch by providing the IP address of your CLI server. (The updated CLI was installed in Step 3.)

      In this example, the IP address for the CLI server is *192.168.1.254*.

   ```
   user@ubuntu:~# netq config add cli server 192.168.1.254
   user@ubuntu:~# netq config restart cli
   ```

7.  Repeat these steps for each Cumulus switch, or use an automation
            tool to install and configure the NetQ Agent on multiple Cumulus Linux switches.

### Upgrade NetQ Agent on an Ubuntu Server

To install the NetQ Agent on an Ubuntu server:

1.  Reference and update the local `apt` repository.

      ```
      root@ubuntu:~# wget -O- https://apps3.cumulusnetworks.com/setup/cumulus-apps-deb.pubkey | apt-key add -
      ```

2.  Verify or add the relevant Ubuntu repository:

    <details><summary>Ubuntu 16.04</summary>
    Create the file
    `/etc/apt/sources.list.d/cumulus-host-ubuntu-xenial.list` and add
    the following line (if not already present):

        root@ubuntu:~# vi /etc/apt/sources.list.d/cumulus-apps-deb-xenial.list
        ...
        deb [arch=amd64] https://apps3.cumulusnetworks.com/repos/deb xenial netq-latest
        ...
    </details>
    <details><summary>Ubuntu 18.04</summary>
    Create the file
    `/etc/apt/sources.list.d/cumulus-host-ubuntu-bionic.list` and add
    the following line:

        root@ubuntu:~# vi /etc/apt/sources.list.d/cumulus-apps-deb-bionic.list
        ...
        deb [arch=amd64] https://apps3.cumulusnetworks.com/repos/deb bionic netq-latest
        ...
    </details>

      {{%notice note%}}

The use of `netq-latest` in these examples means that a `get` to the
            repository always retrieves the latest version of NetQ, even in the
            case where a major version update has been made. If you want to keep
            the repository on a specific version — such as `netq-2.2` — use that
            instead.

      {{%/notice%}}

3.  Install the meta package on the server.

         root@ubuntu:~# apt-get update
         root@ubuntu:~# apt-get install cumulus-netq

4.  Verify the upgrade.

```
root@ubuntu:~$ dpkg -l | grep netq
         ii  cumulus-netq                      2.2.2-cl3u17~155d3c5432.a60ec9a    all          This meta-package provides installation of Cumulus NetQ packages.
         ii  netq-agent                        2.2.2-cl3u17~1559c814b1.2bba220    amd64        Cumulus NetQ Telemetry Agent for Cumulus Linux
         ii  netq-apps                         2.2.2-cl3u17~1559c814b1.2bba220    amd64        Cumulus NetQ Fabric Validation Application for Cumulus Linux
```

5.  Configure the NetQ Agent to send telemetry data to the NetQ Platform.

      {{%notice info%}}

If you intend to use VRF, skip to [Configure the Agent to Use VRF](#configure-the-agent-to-use-a-vrf-interface). If you intend to specify a port for communication, skip to [Configure the Agent to Communicate over a Specific    Port](#configure-the-agent-to-communicate-over-a-specific-port).

      {{%/notice%}}

      In this example, the IP address for the agent server is *192.168.1.254*.

      ```
      user@ubuntu:~# netq config add agent server 192.168.1.254
      Updated agent server 192.168.1.254 vrf default. Please restart netq-agent (netq config restart agent).
      user@ubuntu:~# netq config restart agent
      ```
      This command updates the configuration in the `/etc/netq/netq.yml` file.

6.  Optionally, configure the updated CLI on this switch by providing the IP address of your CLI server. (The updated CLI was installed in Step 3.)

         ```
         user@ubuntu:~# netq config add cli server 192.168.1.254
         Updated cli server 192.168.1.254 vrf default. Please restart netqd (netq config restart cli).
         user@ubuntu:~# netq config restart cli
         ```

7.  Repeat these steps for each switch/host running Ubuntu, or use an
            automation tool to install and configure the NetQ Agent on multiple hosts.

### Upgrade NetQ Agent on a Red Hat or CentOS Server

To upgrade the NetQ Agent on a Red Hat or CentOS server:

1.  Reference and update the local `yum` repository.

         root@rhel7:~# rpm --import https://apps3.cumulusnetworks.com/setup/cumulus-apps-rpm.pubkey
         root@rhel7:~# wget -O- https://apps3.cumulusnetworks.com/setup/cumulus-apps-rpm-el7.repo > /etc/yum.repos.d/cumulus-host-el.repo

2.  Edit `/etc/yum.repos.d/cumulus-host-el.repo` to set the `enabled=1` flag for the two NetQ repositories.

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

         root@rhel7:~$ yum list installed | grep netq
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

6.  Optionally, configure the updated CLI on this switch by providing the IP address of your CLI server. (The updated CLI was installed in Step 3.)

         ```
         root@rhel7:~# netq config add cli server 192.168.1.254
         Updated cli server 192.168.1.254 vrf default. Please restart netqd (netq config restart cli).
         root@rhel7:~# netq config restart cli
         ```

7.  Repeat these steps for each host running Red Hat or CentOS, or use an  automation tool to install and configure the NetQ Agent on multiple hosts.

## Configure Optional NetQ Agent Settings

Once the NetQ Agents have been installed on the network nodes you want
to monitor, the NetQ Agents must be configured to obtain useful and
relevant data. The code examples shown in this section illustrate how to
configure the NetQ Agent on a Cumulus switch, but it is exactly the same
for the other type of nodes. If you have already configured these
settings, you do not need to do so again.

  - [Configuring the Agent to Use a
    VRF](http://docs.cumulusnetworks.com#AgentVRF)
  - [Configuring the Agent to Communicate over a Specific
    Port](http://docs.cumulusnetworks.com#port)

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

## Upgrade Tips

After you have upgraded NetQ, if you find that some issues remain,
review these commonly encountered scenarios. If NetQ is still not
operating as expected, please open a [support
ticket](https://cumulusnetworks.com/support/file-a-ticket/) with a
detailed description of your issues.

### No IP Address Assigned to the NetQ Appliance on Boot

A user did not configure an IP address when the system was first booted.
Later the user assigned an IP address to eth0, but the NetQ appliance
does not appear to be functioning.

You must reset  the install daemon and restart the Kubernetes service.
Follow these steps:

1.  Reset the NetQ Appliance install daemon.

        cumulus@switch:~$ sudo systemctl reset-failed

2.  Restart the Kubernetes service.

        cumulus@switch:~$ sudo systemctl restart cts-kubectl-config
