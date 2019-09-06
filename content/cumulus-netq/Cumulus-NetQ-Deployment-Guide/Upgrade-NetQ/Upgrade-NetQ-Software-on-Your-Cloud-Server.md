---
title: Upgrade NetQ Software on Your Cloud Server
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
This document describes the steps required to upgrade the NetQ Software (versions 2.0.0 through 2.2.0) installed and running on your NetQ cloud server to NetQ version 2.2.2.

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
- Ubuntu 16.04 or Ubuntu 18.04 (NetQ 2.2.2 and later)
- Red Hat<sup>®</sup> Enterprise Linux (RHEL) 7.1
- CentOS 7

## Perform an In-place Upgrade of Cumulus NetQ

An in-place upgrade is recommended for upgrades from Cumulus NetQ 2.2.1. If you are upgrading from NetQ 2.2.0 or earlier, a [disk image upgrade](#perform-a-disk-image-upgrade-of-Cumulus-NetQ) is recommended.

### In-place Upgrade Workflow
Upgrading NetQ involves backing up your data, downloading and installing the new version of NetQ software, restoring your NetQ data, and upgrading and configuring the NetQ Agents.

{{< figure src="/images/netq/upgrade-wkflow-in-place-cloud-cust-hw-222.png" width="600" >}}

### Download the NetQ Software

To upgrade the NetQ software on your own hardware using a VM image:

1.  **IMPORTANT**: Confirm that your server hardware meets the
    requirements set out [above](#hardware-requirements).

2.  On the [Cumulus Downloads](https://cumulusnetworks.com/downloads/) page, select *NetQ* from the **Product** list box.

3.  Click *2.2* from the **Version** list box, and then select
  *2.2.2* from the submenu.

4.  Optionally, select the hypervisor you wish to use (*VMware (Cloud)* or *KVM (Cloud)*) from the
  **Hypervisor/Platform** list box.

     {{< figure src="/images/netq/NetQ-22-Download-Options-222.png" width="500" >}}

     {{%notice note%}}

For customers with VMware/ESXi OVA deployments, Cumulus Networks recommends deploying a fresh installation of NetQ 2.2.2, rather than performing the upgrade from 2.1.x or 2.2.0, to take advantage of the performance improvements available with the new vmxnet3 and Paravirtualization SCSI drivers.

        {{%/notice%}}

5.  Scroll down to review the images that match your selection
  criteria.

      {{< figure src="/images/netq/netq-22-vm-cloud-upgrade-222.png" width="400" >}}

6.  Click **Upgrade** for the relevant version, being careful to
  select the correct deployment version.

### Install and Configure the CLI

You must upgrade the CLI to make use of the modified upgrade command.

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
### Run the Upgrade Command

1. Use the `netq upgrade opta` command to install the VM you downloaded above.

```
cumulus@switch:~$ netq upgrade opta tarball NetQ-2.2.2-opta.tgz
```

2. Verify the release has been updated successfully.

```
cumulus@switch:~$ cat /etc/app-release
APPLIANCE_VERSION=2.2.2
APPLIANCE_MANIFEST_HASH=a7f3cda
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

3.  Continue the NetQ upgrade by upgrading the NetQ Agent on each switch or host you want to monitor. Refer to [Upgrade the NetQ Agents and CLI](#upgrade-the-netq-agents-and-cli) for instructions.

## Perform a Disk Image Upgrade of Cumulus NetQ

A disk image upgrade is recommended for upgrades from Cumulus NetQ 2.2.0 or earlier. An [in-place upgrade](#perform-an-in-place-upgrade-of-Cumulus-NetQ) is recommended for upgrades from NetQ 2.2.1.

### Disk Image Upgrade Workflow
Upgrading NetQ involves backing up your data, downloading and installing the new version of NetQ software, restoring your NetQ data, and upgrading and configuring the NetQ Agents.

{{< figure src="/images/netq/upgrade-wkflow-disk-img-cust-hw-cloud-222.png" width="600" >}}

### Download NetQ Virtual Machine Image

1.  **IMPORTANT**: Confirm that your server hardware meets the
    requirements set out [here](#hardware-requirements).

2.  On the [Cumulus Downloads](https://cumulusnetworks.com/downloads/) page, select
        *NetQ* from the **Product** list box.

4.  Click *2.2* from the **Version** list box, and then select *2.2.2* from the submenu.

5.  Optionally, select the hypervisor you wish to use (*VMware (Cloud)* or *KVM (Cloud)*) from the
  **Hypervisor/Platform** list box.

     {{< figure src="/images/netq/NetQ-22-Download-Options-222.png" width="500" >}}

6.  Scroll down to review the images that match your selection criteria, and click **Download** for the image you want.

       {{< figure src="/images/netq/netq-22-vm-dwnld-222.png" width="750" >}}

### Deploy VM Image

Open your hypervisor and set up your VM. You can use these examples for reference or use your own hypervisor instructions.

 <details><summary>VMware example</summary>

   This example shows the VM setup process using an OVA file with VMware
   ESXi.

   1.  Enter the address of the hardware in your browser.
   2.  Log in to VMware using credentials with root access.  

      {{< figure src="/images/netq/vmw-main-page.png" width="650" >}}

   3.  Click **Create/Register VM** at the top of the right pane.

      {{< figure src="/images/netq/vmw-menu-create-register.png" width="650" >}}

   4.  Select **Deploy a virtual machine from an OVF or OVA file**, and
       click **Next**.  

      {{< figure src="/images/netq/vmw-deploy-vm-from-ova.png" width="700" >}}

   5.  Provide a name for the VM, for example *Cumulus NetQ*.

   6.  Drag and drop the NetQ Platform image file you downloaded in Step 1
       above.

      {{< figure src="/images/netq/vmw-name-the-vm.png" width="700" >}}

   7.  Click **Next**.

   8.  Select the storage type and data store for the image to use, then
       click **Next**. In this example, only one is available.

       {{< figure src="/images/netq/vmw-select-storage.png" width="700" >}}

   9. Accept the default deployment options or modify them according to
       your network needs. Click **Next** when you are finished.

       {{< figure src="/images/netq/vmw-default-deploy-options.png" width="700" >}}

   10. Review the configuration summary. Click **Back** to change any of
       the settings, or click **Finish** to continue with the creation of
       the VM.

       {{< figure src="/images/netq/vmw-review-before-create.png" width="700" >}}

       The progress of the request is shown in the Recent Tasks window at
       the bottom of the application. This may take some time, so continue
       with your other work until the upload finishes.

   11. Once completed, view the full details of the VM and hardware.

       {{< figure src="/images/netq/vmw-deploy-results.png" width="700" >}}

</details>
<details><summary>KVM example</summary>

This example shows the VM setup process for a system with Libvirt and
KVM/QEMU installed.

1.  Confirm that the SHA256 checksum matches the one posted on the
    Cumulus Downloads website to ensure the image download has not been
    corrupted.

        $ sha256sum ./Downloads/cumulus-netq-server-2.2.0-ts-amd64-qemu.qcow2
        $ 6fff5f2ac62930799b4e8cc7811abb6840b247e2c9e76ea9ccba03f991f42424  ./Downloads/cumulus-netq-server-2.2.0-ts-amd64-qemu.qcow2

2.  Copy the QCOW2 image to a directory where you want to run it.

    {{%notice tip%}}

Copy, instead of moving, the original QCOW2 image that
    was downloaded to avoid re-downloading it again later
    should you need to perform this process again.

    {{%/notice%}}

        $ sudo mkdir /vms
        $ sudo cp ./Downloads/cumulus-netq-server-2.2.0-ts-amd64-qemu.qcow2 /vms/ts.qcow2

3.  Create the VM.

    For a Direct VM, where the VM uses a MACVLAN interface to sit on the
    host interface for its connectivity:

        $ virt-install --name=netq_ts --vcpus=8 --memory=65536 --os-type=linux --os-variant=debian7 \
         --disk path=/vms/ts.qcow2,format=qcow2,bus=virtio,cache=none \
         --network=type=direct,source=eth0,model=virtio --import --noautoconsole

    {{%notice note%}}

Replace the disk path value with the location where the QCOW2 image
    is to reside. Replace network model value (eth0 in the above
    example) with the name of the interface where the VM is connected to
    the external network.

    {{%/notice%}}

    Or, for a Bridged VM, where the VM attaches to a bridge which has
    already been setup to allow for external access:

        $ virt-install --name=netq_ts --vcpus=8 --memory=65536 --os-type=linux --os-variant=debian7 \
         --disk path=/vms/ts.qcow2,format=qcow2,bus=virtio,cache=none \
         --network=bridge=br0,model=virtio --import --noautoconsole

    {{%notice note%}}

Replace network bridge value (br0 in the above example) with the
    name of the (pre-existing) bridge interface where the VM is
    connected to the external network.

    {{%/notice%}}

4.  Watch the boot process in another terminal window.

        $ virsh console netq_ts

5.  From the Console of the VM, check to see which IP address Eth0 has
    obtained via DHCP, or alternatively set a static IP address with
    NCLU on the NetQ Appliance or Platform VM.

        $ ip addr show eth0
        $ net add interface eth0 ip address 10.0.0.1
        $ net commit
</details>

{{%notice info%}}

If you have changed the IP address or hostname of the NetQ Platform, you need to
re-register this address or hostname with the Kubernetes containers before you can
continue.

1.  Reset all Kubernetes administrative settings. Run the command twice
    to make sure all directories and files have been reset.
    ```
    cumulus@netq-platform:~$ sudo kubeadm reset -f
    ```  
2.  Remove the Kubernetes configuration.

    ```
    cumulus@netq-platform:~$ sudo rm /home/cumulus/.kube/config
    ```

3.  Reset the NetQ Platform install daemon.  

    ```
    cumulus@netq-platform:~$ sudo systemctl reset-failed
    ```  

4.  Reset the Kubernetes service.  

    ```
    cumulus@netq-platform:~$ sudo systemctl restart cts-kubectl-config
    ```  
    **Note**: Allow 15 minutes for the prompt to return.

5.  Reboot the VM.  
    **Note**: Allow 5-10 minutes for the VM to boot.

{{%/notice%}}

### Install and Configure the CLI

The CLI communicates through the API gateway in the NetQ Cloud. To access and configure the CLI on your NetQ Cloud server you will need your username and password to access the NetQ UI to generate an access-key and secret-key. Your credentials and NetQ Cloud addresses were provided by Cumulus Networks via an email titled *Welcome to Cumulus NetQ!*

To configure CLI access:

1. In your Internet browser, enter **netq.cumulusnetworks.com** into the address field to open the NetQ UI login page.

2. Enter your username and password.

3. From the Main Menu, select *Management* in the **Admin** column.

      {{< figure src="/images/netq/main-menu-mgmt-selected.png" width="400">}}

4. Click **Manage** on the User Accounts card.
5. Select your user and click **Generate AuthKeys**.

      {{< figure src="/images/netq/generate-auth-keys.png" width="700">}}

6. Copy these keys to a safe place.

      {{%notice info%}}
The secret key is only shown once. If you don't copy these, you will need to regenerate them and reconfigure CLI access.

In version 2.2.1 and later, you can save these keys to a YAML file for easy reference, and to avoid having to type or copy the key values. You can store this file wherever you like, name it *credentials.yml*, and make sure it has the following format:
```
access-key: <user-access-key-value-here>
secret-key: <user-secret-key-value-here>
```
      {{%/notice%}}

7. Configure access to the CLI:
   - In NetQ 2.2.x, run the following commands. Replace the key values with your generated keys.
   ```
   cumulus@netq-platform:~$ netq config add cli server api.netq.cumulusnetworks.com access-key <text-access-key> secret-key <text-secret-key> port 443
   Successfully logged into NetQ cloud at api.netq.cumulusnetworks.com:443
   Updated cli server api.netq.cumulusnetworks.com vrf default port 443. Please restart netqd (netq config restart cli)

   cumulus@netq-platform:~$ netq config restart cli
   Restarting NetQ CLI... Success!
   ```
   - In NetQ 2.2.1 or later, if you have created a *credentials.yml* file as noted in the previous step, run the following commands. Be sure to include the **full path** the to file.
   ```
   cumulus@netq-platform:~$ netq config add cli server api.netq.cumulusnetworks.com cli-keys-file /full-path/credentials.yml port 443
   Successfully logged into NetQ cloud at api.netq.cumulusnetworks.com:443
   Updated cli server api.netq.cumulusnetworks.com vrf default port 443. Please restart netqd (netq config restart cli)

   cumulus@netq-platform:~$ netq config restart cli
   Restarting NetQ CLI... Success!
   ```

### Download and Install NetQ Cloud Software

1. Create the file /etc/apt/sources.list.d/cumulus_netq.list and add the following lines:

```
deb http://apps3.cumulusnetworks.com/repos/deb CumulusLinux-3 netq-2.2
```

2. Download the latest netq-apps package from this repository.

```
cumulus@netq-platform:~$ sudo apt-get update
cumulus@netq-platform:~$ sudo apt-get install netq-apps
```

3. Download and install the software.

```
cumulus@netq-platform:~$ netq upgrade opta tarball download 2.2.2
2019-08-29 21:25:58.343212: opta-installer: Upgrading OPTA
2019-08-29 21:26:17.549618: opta-installer: Extracting tarball /mnt/installables/NetQ-2.2.2-opta.tgz
2019-08-29 21:26:38.427990: opta-installer: Checking for configkey
2019-08-29 21:26:38.991100: opta-installer: Upgrading netq-installer pod
2019-08-29 21:30:45.981703: opta-installer: Upgrading netq-opta pod
2019-08-29 21:35:47.161308: opta-installer: Validating upgrade
------------------------------
Successfully upgraded the opta
```

4. Confirm the upgrade was successful.

```
cumulus@netq-platform:~$ cat /etc/app-release
APPLIANCE_VERSION=2.2.2
APPLIANCE_MANIFEST_HASH=a7f3cda
APPLIANCE_NAME="NetQ Cloud Appliance"

cumulus@netq-platform:~$ dpkg -l | egrep "netq-agent|netq-apps"
ii  netq-agent                        2.2.2-cl3u20~1566948619.810054e      amd64        Cumulus NetQ Telemetry Agent for Cumulus Linux
ii  netq-apps                         2.2.2-cl3u20~1566948619.810054e      amd64        Cumulus NetQ Fabric Validation Application for Cumulus Linux
```

6. Verify all applications and services are operating properly.
   ```
   cumulus@netq-platform:~$ netq show opta-health
   OPTA is healthy
   ```
       {{%notice note%}}

If the results do not indicate the server is healthy after 30 minutes, open a [support ticket](https://cumulusnetworks.com/support/file-a-ticket/) and attach the output of the `opta-support` command.

         {{%/notice%}}

## Upgrade the NetQ Agents and CLI

The NetQ Agent should be upgraded on each of the existing nodes you want to monitor to be sure you have the latest features and fixes. The node can be a:

  - Switch running Cumulus Linux version 3.3.2 or later
  - Server running Red Hat RHEL 7.1, Ubuntu 16.04, Ubuntu 18.04 (NetQ 2.2.2 and later), or CentOS 7
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
        ii  cumulus-netq                      2.2.2-cl3u20~155d365432.a60ec9a    all          This meta-package provides installation of Cumulus NetQ packages.
        ii  netq-agent                        2.2.2-cl3u20~1539681411.2bba220    amd64        Cumulus NetQ Telemetry Agent for Cumulus Linux
        ii  netq-apps                         2.2.2-cl3u20~1539681411.2bba220    amd64        Cumulus NetQ Fabric Validation Application for Cumulus Linux

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

6.  Optionally, configure the switch or host to run the NetQ CLI.

      *For switches* **with** *Internet access:*

      - In NetQ 2.2.x, run the following commands. Replace the key values with your generated keys.

   ```
   cumulus@switch:~$ netq config add cli server api.netq.cumulusnetworks.com access-key <text-access-key> secret-key <text-secret-key> port 443
   Successfully logged into NetQ cloud at api.netq.cumulusnetworks.com:443
   Updated cli server api.netq.cumulusnetworks.com vrf default port 443. Please restart netqd (netq config restart cli)

   cumulus@switch:~$ netq config restart cli
   Restarting NetQ CLI... Success!
   ```

      - In NetQ 2.2.1 and later, if you have created a `credentials.yml` file during step 6 of [Install and Configure the CLI](#install-and-configure-the-cli), run the following commands. Be sure to include the **full path** to the file.

   ```
   cumulus@switch:~$ netq config add cli server api.netq.cumulusnetworks.com cli-keys-file /full-path/credentials.yml port 443
   Successfully logged into NetQ cloud at api.netq.cumulusnetworks.com:443
   Updated cli server api.netq.cumulusnetworks.com vrf default port 443. Please restart netqd (netq config restart cli)

   cumulus@switch:~$ netq config restart cli
   Restarting NetQ CLI... Success!
   ```

      *For switches* **without** *Internet access:*

      A CLI proxy is part of the NetQ Cloud image with NetQ 2.2.2 and later. If your switches and hosts do not have access to the Internet, you can use the proxy on the NetQ Cloud server to manage CLI access on your nodes. To make use of the proxy, you must point each switch or host to the NetQ Cloud server. Run the following commands, using the IP address of your NetQ Cloud server:

   ```
   cumulus@switch:~$ netq config add cli server <netq-cloud-server-ip-addr>
   Updated cli server <netq-cloud-server-ip-addr> vrf default port 443. Please restart netqd (netq config restart cli)

   cumulus@switch:~$ netq config restart cli
   Restarting NetQ CLI... Success!
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
    root@ubuntu:~# netq config add agent server 192.168.1.254
    Updated agent server 192.168.1.254 vrf default. Please restart netq-agent (netq config restart agent).
    root@ubuntu:~# netq config restart agent
    ```
    This command updates the configuration in the `/etc/netq/netq.yml`
    file.

6.  Optionally, configure the switch or host to run the NetQ CLI.

       *For switches* **with** *Internet access:*

       - In NetQ 2.2.x, run the following commands. Replace the key values with your generated keys.

    ```
    root@ubuntu:~# netq config add cli server api.netq.cumulusnetworks.com access-key <text-access-key> secret-key <text-secret-key> port 443
    Successfully logged into NetQ cloud at api.netq.cumulusnetworks.com:443
    Updated cli server api.netq.cumulusnetworks.com vrf default port 443. Please restart netqd (netq config restart cli)

    root@ubuntu:~# netq config restart cli
    Restarting NetQ CLI... Success!
    ```

       - In NetQ 2.2.1 and later, if you have created a `credentials.yml` file as noted in during step 6 of [Install and Configure the CLI](#install-and-configure-the-cli), run the following commands. Be sure to include the **full path** the to file.

    ```
    root@ubuntu:~# netq config add cli server api.netq.cumulusnetworks.com cli-keys-file /full-path/credentials.yml port 443
    Successfully logged into NetQ cloud at api.netq.cumulusnetworks.com:443
    Updated cli server api.netq.cumulusnetworks.com vrf default port 443. Please restart netqd (netq config restart cli)

    root@ubuntu:~# netq config restart cli
    Restarting NetQ CLI... Success!
    ```

       *For switches* **without** *Internet access:*

       A CLI proxy is part of the NetQ Cloud image with NetQ 2.2.2 and later. If your switches and hosts do not have access to the Internet, you can use the proxy on the NetQ Cloud server to manage CLI access on your nodes. To make use of the proxy, you must point each switch or host to the NetQ Cloud server. Run the following commands, using the IP address of your NetQ Cloud server:

    ```
    root@ubuntu:~# netq config add cli server <netq-cloud-server-ip-addr>
    Updated cli server <netq-cloud-server-ip-addr> vrf default port 443. Please restart netqd (netq config restart cli)

    root@ubuntu:~# netq config restart cli
    Restarting NetQ CLI... Success!
    ```

7.  Repeat these steps for each switch/host running Ubuntu, or use an
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

6.  Optionally, configure the switch or host to run the NetQ CLI.

      *For switches* **with** *Internet access:*

      - In NetQ 2.2.x, run the following commands. Replace the key values with your generated keys.

   ```
   root@rhel7:~# netq config add cli server api.netq.cumulusnetworks.com access-key <text-access-key> secret-key <text-secret-key> port 443
   Successfully logged into NetQ cloud at api.netq.cumulusnetworks.com:443
   Updated cli server api.netq.cumulusnetworks.com vrf default port 443. Please restart netqd (netq config restart cli)

   root@rhel7:~# netq config restart cli
   Restarting NetQ CLI... Success!
   ```

      - In NetQ 2.2.1 and later, if you have created a `credentials.yml` file as noted in during step 6 of [Install and Configure the CLI](#install-and-configure-the-cli), run the following commands. Be sure to include the **full path** the to file.

   ```
   root@rhel7:~# netq config add cli server api.netq.cumulusnetworks.com cli-keys-file /full-path/credentials.yml port 443
   Successfully logged into NetQ cloud at api.netq.cumulusnetworks.com:443
   Updated cli server api.netq.cumulusnetworks.com vrf default port 443. Please restart netqd (netq config restart cli)

   root@rhel7:~# netq config restart cli
   Restarting NetQ CLI... Success!
   ```

      *For switches* **without** *Internet access:*

      A CLI proxy is part of the NetQ Cloud image with NetQ 2.2.2 and later. If your switches and hosts do not have access to the Internet, you can use the proxy on the NetQ Cloud server to manage CLI access on your nodes. To make use of the proxy, you must point each switch or host to the NetQ Cloud server. Run the following commands, using the IP address of your NetQ Cloud server:

   ```
   root@rhel7:~# netq config add cli server <netq-cloud-server-ip-addr>
   Updated cli server <netq-cloud-server-ip-addr> vrf default port 443. Please restart netqd (netq config restart cli)

   root@rhel7:~# netq config restart cli
   Restarting NetQ CLI... Success!
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
