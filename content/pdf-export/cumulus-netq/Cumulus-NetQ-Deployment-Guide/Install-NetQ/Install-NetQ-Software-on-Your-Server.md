---
title: Install NetQ Software on Your Server
author: Cumulus Networks
weight: 409
aliases:
 - /display/NETQ/Install+NetQ
 - /pages/viewpage.action?pageId=12320951
pageID: 12320951
product: Cumulus NetQ
version: 2.2
imgData: cumulus-netq-22
siteSlug: cumulus-netq-22
---

The installation instructions in this topic describe how to install the Cumulus NetQ software onto your server for either an on-premises or in-cloud deployment. There are three key steps:

1. Verify your server meets the hardware and software requirements.
2. Load the software onto the switch.
3. Load the NetQ Agent onto the switches and hosts you want to monitor.

If you are upgrading from a prior version of NetQ, refer to [Upgrade NetQ](/cumulus-netq/Cumulus-NetQ-Deployment-Guide/Upgrade-NetQ/)
    instead.

## Prerequisites

### Hardware Requirements

Cumulus NetQ software is supported on a variety of hardware.

{{%notice info%}}

You must meet these *minimum* hardware requirements to install the VM
and have it run properly.

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
| 31980 | On-site and cloud | NetQ Platform             |
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
- Ubuntu 16.04
- Red Hat<sup>®</sup> Enterprise Linux (RHEL) 7.1
- CentOS 7

### NetQ Application Support

The NetQ CLI, UI, and RESTful API are supported on NetQ 2.1.0 and later.
NetQ 1.4 and earlier applications are not supported in NetQ 2.x.

### Install Workflow

Installation of NetQ involves installing the NetQ software, and
installing and configuring the NetQ Agents. Additional steps are needed
to [Integrate NetQ with Event Notification Applications](/cumulus-netq/Cumulus-NetQ-Deployment-Guide/Integration-Guide/Integrate-with-Notification-Applications).
This flow chart shows the required steps to install and setup
NetQ to start validating your network, and the optional steps of
integrating with event notification applications and monitoring hosts.

{{<figure src="https://dkahegywkrw3e.cloudfront.net/images/netq/install-wkflow-cust-hw.png">}}

## Install the NetQ Platform

The first step of the install process is to install the NetQ software
onto your hardware (NetQ Platform).

The NetQ software is comprised of the following components:

  - **NetQ applications**: network monitoring and analytics
    functionality
  - **NetQ CLI**: command line user interface for monitoring network and
    administering NetQ through a terminal session
  - **NetQ UI**: graphical interface for monitoring network and
    administering NetQ
  - **NetQ API**: Restful application programming interface for
    accessing NetQ data and integrating with third-party tools
  - **NetQ notifier**: application used to send event notifications to
    third-party notification tools

{{%notice tip%}}

Cumulus Networks recommends you install the NetQ software on a server
that is part of an out-of-band management network to ensure it can
monitor in-band network issues without being affected itself. You should
run the software on a separate, powerful server to ensure proper
operation and for maximum usability and performance. Refer to [Hardware
Requirements](#hardware-requirements) for specifics.

{{%/notice%}}

To install the NetQ software onto your own hardware using a VM
image:

1.  **IMPORTANT**: Confirm that your server hardware meets the
    requirements set out [here](#hardware-requirements).
2.  Download the NetQ Platform image.

    1.  On the [Cumulus Downloads](https://cumulusnetworks.com/downloads/) page, select
        *NetQ* from the **Product** list box.

    2.  Click *2.2* from the **Version** list box, and then select
        *2.2.x* from the submenu.

    3.  Optionally, select the hypervisor you wish to use (*VMware,
        VMware (Cloud),* *KVM (Cloud)*, or *KVM*) from the
        **Hypervisor/Platform** list box.

        {{< figure src="https://dkahegywkrw3e.cloudfront.net/images/netq/NetQ-22-Download-Options-v2.png" width="500" >}}

        {{%notice note%}}

If you are installing the on-premises solution, select either *VMware* or *KVM*. If you are installing the in-cloud solution, select either *VMware (Cloud)* or *KVM (Cloud)*.
        {{%/notice%}}

    4.  Scroll down to review the images that match your selection
        criteria, and click **Download** for the image you want.

        {{< figure src="https://dkahegywkrw3e.cloudfront.net/images/netq/netq-22-vm-dwnld.png" width="750" >}}

3.  Open your hypervisor and set up your VM.  
    You can use these examples for reference or use your own hypervisor
    instructions.

    <details><summary><span style="color:teal">VMware example</span></summary>

      This example shows the VM setup process using an OVA file with VMware
      ESXi.

      1.  Enter the address of the hardware in your browser.
      2.  Log in to VMware using credentials with root access.  

          {{% imgOld 3 %}}

      3.  For an on-site NetQ Platform deployment, click **Storage** in the
          Navigator to verify you have an SSD installed.  

          {{% imgOld 4 %}}

      4.  Click **Create/Register VM** at the top of the right pane.

          {{% imgOld 5 %}}

      5.  Select **Deploy a virtual machine from and OVF or OVA file**, and
          click **Next**.  

          {{% imgOld 6 %}}

      6.  Provide a name for the VM, for example *Cumulus NetQ*.
      7.  Drag and drop the NetQ Platform image file you downloaded in Step 1
          above.
      8.  Click **Next**.

          {{% imgOld 7 %}}

      9.  Select the storage type and data store for the image to use, then
          click **Next**. In this example, only one is available.

          {{% imgOld 8 %}}

      10. Accept the default deployment options or modify them according to
          your network needs. Click **Next** when you are finished.

          {{% imgOld 9 %}}

      11. Review the configuration summary. Click **Back** to change any of
          the settings, or click **Finish** to continue with the creation of
          the VM.

          {{% imgOld 10 %}}

          The progress of the request is shown in the Recent Tasks window at
          the bottom of the application. This may take some time, so continue
          with your other work until the upload finishes.

      12. Once completed, view the full details of the VM and hardware.

          {{% imgOld 11 %}}

   </details>
   <details><summary><span style="color:teal">KVM example</span></summary>

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

If you have changed the IP address of the NetQ Platform, you need to
re-register this address with the Kubernetes containers before you can
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
    *Note*: Allow 15 minutes for the prompt to return.

5.  Reboot the VM.  
    *Note*: Allow 5-10 minutes for the VM to boot.

{{%/notice%}}

If you are installing an on-premises solution, continue with the steps here. If you are installing the in-cloud solution, skip to [Additional In-cloud Solution Installation Steps](#additional-in-cloud-solution-installation-steps).

### Verify On-Premises Installation

1.  Verify you can access the NetQ CLI.

    1.  From a terminal window, log in to the NetQ Platform using the
        default credentials (*cumulus/CumulusLinux\!*).

            <computer>:~<username>$ ssh cumulus@<netq-platform-ipaddress>
            Warning: Permanently added '<netq-platform-hostname>,192.168.1.254' (ECDSA) to the list of known hosts.
            cumulus@<netq-platform-hostname>'s password: <enter CumulusLinux! here>
             
            Welcome to Cumulus (R) Linux (R)
             
            For support and online technical documentation, visit
            http://www.cumulusnetworks.com/support
             
            The registered trademark Linux (R) is used pursuant to a sublicense from LMI,
            the exclusive licensee of Linus Torvalds, owner of the mark on a world-wide
            basis.
             
            cumulus@<netq-platform-hostname>:~$ 

    2.  Run the following command to verify all applications are
        operating properly. *Note*: Please allow 10-15 minutes for
        all applications to come up and report their status.

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
             
            cumulus@<netq-platform-hostname>:~$

        {{%notice note%}}

If any of the applications or services display status as DOWN after 30 minutes,
open a [support ticket](https://cumulusnetworks.com/support/file-a-ticket/) and
attach the output of the `opta-support` command.

        {{%/notice%}}

2.  Verify that NTP is configured and running. NTP operation is critical
    to proper operation of NetQ. Refer to [Setting Date and Time](/cumulus-linux/System-Configuration/Setting-Date-and-Time/) in the *Cumulus Linux User Guide* for details and instructions.

      {{%notice tip%}}

If you are still experiencing issues with your installation, confirm that your DNS server is properly configured.

      {{%/notice%}}

You are almost done. The NetQ server installation is complete. The final step is to install NetQ Agents on each of the switches and hosts you want monitored. Go to [Install the NetQ Agent](#install-the-netq-agent) for these instructions.

## Additional In-cloud Solution Installation Steps

With the in-cloud solution, the VM you downloaded only contains the core NetQ software. You must also download the additional cloud components and configure CLI access on the NetQ server (and any switches or hosts).

### Download Cloud Components

To obtain the additional cloud components:

1. Download the second image.

    1. On the [Cumulus Downloads](https://cumulusnetworks.com/downloads/) page, select
        *NetQ* from the **Product** list box.

    2. Click *2.2* from the **Version** list box, and then select *2.2.x* from the submenu.

    3. Optionally, select *Appliance (Cloud)* from the **Hypervisor/Platform** list box.

         {{< figure src="https://dkahegywkrw3e.cloudfront.net/images/netq/NetQ-22-Download-Options.png" >}}

    4. Click the **Upgrade** button.

         {{< figure src="https://dkahegywkrw3e.cloudfront.net/images/netq/NetQ-Cloud-Appl-SW-Dwnld-v2.png" width="250">}}

2. Log in to the NetQ server.
3. Copy the downloaded file into the `/mnt/installables/` directory. Be sure to use the correct file name, with appropriate version.

   ```
   cumulus@netq-server:~$ sudo cp /home/usr/dir/NetQ-2.2.1-opta.tgz /mnt/installables/
   ```

4. Identify the IP address and interface where NetQ Agents should send the telemetry data collected from your monitored switches and hosts.
   - Using dynamic address (DHCP): run the `net show interface eth0` command.
   - Using static address: assign the address by running `net show interface <eth0|eth1> address <IP-address>`, then review and commit the assignment using `net pending` and then `net commit`.
5. Install the downloaded software.
      <details><summary><span style="color:teal">NetQ v2.2.0</span></summary>

      ```
      cumulus@netq-appliance:~$ netq install opta interface eth0 tarball NetQ-2.2.0-opta.tgz key "CNKaDBIjZ3buZhV2Mi5uZXRxZGV2LmN1bXVsdXNuZXw3b3Jrcy5jb20YuwM="
      opta-installer: Resetting OPTA
      opta-installer: Checking for installer directory
      opta-installer: Checking minimum RAM requirements
      opta-installer: Checking for minimum CPU requirements
      opta-installer: Checking for Python 2.7
      opta-installer: Checking for Kubernetes v1.11.5
      opta-installer: Checking for Docker /usr/bin/docker
      ...
      Successfully installed the opta
      ```

      </details>
      <details><summary><span style="color:teal">NetQ v2.2.1</span></summary>

      ```
      cumulus@netq-appliance:~$ netq install opta interface eth0 tarball NetQ-2.2.1-opta.tgz config-key "CNKaDBIjZ3buZhV2Mi5uZXRxZGV2LmN1bXVsdXNuZXw3b3Jrcy5jb20YuwM="
      opta-installer: Resetting OPTA
      opta-installer: Checking for installer directory
      opta-installer: Checking minimum RAM requirements
      opta-installer: Checking for minimum CPU requirements
      opta-installer: Checking for Python 2.7
      opta-installer: Checking for Kubernetes v1.11.5
      opta-installer: Checking for Docker /usr/bin/docker
      ...
      Successfully installed the opta
      ```

      </details>

      {{%notice note%}}

You can optionally override selected default installation parameters using the `file <text-config-file>` option. By default, the data directory is `/mnt`, the Kubernetes pods are assigned to network addresses in the 10.244.0.0/16 range, the node name is *cumulus.netq*, and the scratch directory is `/tmp`. The override file must be in YAML format and written as shown in this example:

```
data-dir: /usr/share
pod-network-dir: 10.1.1.0/16
node-name: company-name.netq
scratch-dir: /tmp/netq
```

The `text-config-file` value is then the full path to the YAML file; for example `/home/username/overwrite-default.yml`.

      {{%/notice%}}


6. Verify all applications and services are operating properly.
   ```
   cumulus@<netq-appliance-hostname>:~$ netq show opta-health
   OPTA is healthy
   ```

### Configure CLI Access

The CLI communicates through the API gateway in the NetQ Cloud. To access and configure the CLI on your NetQ Cloud server you will need your username and password to access the NetQ UI to generate an access-key and secret-key. Your credentials and NetQ Cloud addresses were provided by Cumulus Networks via an email titled *Welcome to Cumulus NetQ!*

To configure CLI access:

1. In your Internet browser, enter **netq.cumulusnetworks.com** into the address field to open the NetQ UI login page.

2. Enter your username and password.

3. From the Main Menu, select *Management* in the **Admin column**.

      {{< figure src="https://dkahegywkrw3e.cloudfront.net/images/netq/main-menu-mgmt-selected.png" width="400">}}

4. Click **Manage** on the User Accounts card.
5. Select your user and click **Generate AuthKeys**.

      {{< figure src="https://dkahegywkrw3e.cloudfront.net/images/netq/generate-auth-keys.png" width="700">}}

6. Copy these keys to a safe place.

      {{%notice info%}}
The secret key is only shown once. If you don't copy these, you will need to regenerate them and reconfigure CLI access.

In version 2.2.1, you can save these keys to a YAML file for easy reference, and to avoid having to type or copy the key values. You can store this file wherever you like, give it a name, such as, *credentials.yml*, and make sure it has the following format:
```
access-key: <user-access-key-value-here>
secret-key: <user-secret-key-value-here>
```
      {{%/notice%}}

7. Configure access to the CLI:
   - In NetQ 2.2.x, run the following commands. Replace the key values with your generated keys.
   ```
   cumulus@netq-appliance:~$ netq config add cli server api.netq.cumulusnetworks.com access-key <text-access-key> secret-key <text-secret-key> port 443
   Successfully logged into NetQ cloud at api.netq.cumulusnetworks.com:443
   Updated cli server api.netq.cumulusnetworks.com vrf default port 443. Please restart netqd (netq config restart cli)

   cumulus@netq-appliance:~$ netq config restart cli
   Restarting NetQ CLI... Success!
   ```
   - In NetQ 2.2.1, if you have created a *credentials.yml* file as noted in the previous step, run the following commands. Be sure to include the full path the to file.
   ```
   cumulus@netq-appliance:~$ netq config add cli server api.netq.cumulusnetworks.com cli-keys-file /full-path/credentials.yml port 443
   Successfully logged into NetQ cloud at api.netq.cumulusnetworks.com:443
   Updated cli server api.netq.cumulusnetworks.com vrf default port 443. Please restart netqd (netq config restart cli)

   cumulus@netq-appliance:~$ netq config restart cli
   Restarting NetQ CLI... Success!
   ```

With your NetQ cloud server now set up and configured, you are ready to install the NetQ Agent on each switch and host you want to monitor with NetQ. Follow the instructions in the next section for details.

## Install the NetQ Agent

Whether using the NetQ Appliance or your own hardware, the NetQ Agent
must be installed on each node you want to monitor. The node can be a:

  - Switch running Cumulus Linux version 3.3.2 or later
  - Server running Red Hat RHEL 7.1, Ubuntu 16.04 or CentOS 7
  - Linux virtual machine running any of the above Linux operating
    systems

To install the NetQ Agent you need to install the OS-specific meta
package, `cumulus-netq`, on each switch. Optionally, you can install it
on hosts. The meta package contains the NetQ Agent, the NetQ command
line interface (CLI), and the NetQ library. The library contains modules
used by both the NetQ Agent and the CLI.

Instructions for installing the meta package on each node type are
included here:

  - [Install NetQ Agent on a Cumulus Linux Switch](#install-netq-agent-on-a-cumulus-linux-switch)
  - [Install NetQ Agent on an Ubuntu Server](#install-netq-on-an-ubuntu-server)
  - [Install NetQ Agent on a Red Hat or CentOS Server](#install-netq-on-a-red-hat-or-centos-server)

{{%notice note%}}

If your network uses a proxy server for external connections, you should
first [configure a global proxy](/cumulus-linux/System-Configuration/Configuring-a-Global-Proxy/)
so `apt-get` can access the meta package on the Cumulus Networks repository.

{{%/notice%}}

### Install NetQ Agent on a Cumulus Linux Switch

A simple process installs the NetQ Agent on a Cumulus switch.

1.  Edit the `/etc/apt/sources.list` file to add the repository for
    Cumulus NetQ. ***Note*** that NetQ has a separate repository from
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

3.  Verify that [NTP](/cumulus-linux/System-Configuration/Setting-Date-and-Time/)
    is running on the host node. Nodes must be in time synchronization with the
    NetQ Platform to enable useful statistical analysis.

        cumulus@switch:~$ sudo systemctl status ntp
        [sudo] password for cumulus:
        ● ntp.service - LSB: Start NTP daemon
           Loaded: loaded (/etc/init.d/ntp; bad; vendor preset: enabled)
           Active: active (running) since Fri 2018-06-01 13:49:11 EDT; 2 weeks 6 days ago
             Docs: man:systemd-sysv-generator(8)
           CGroup: /system.slice/ntp.service
                   └─2873 /usr/sbin/ntpd -p /var/run/ntpd.pid -g -c /var/lib/ntp/ntp.conf.dhcp -u 109:114

4.  Restart `rsyslog` so log files are sent to the correct destination.

        cumulus@switch:~$ sudo systemctl restart rsyslog.service

5.  Configure the NetQ Agent to send telemetry data to the NetQ Platform.  

    {{%notice info%}}

If you intend to use VRF, skip to [Configure the Agent to Use VRF](#configure-the-agent-to-use-a-vrf). If you intend to specify a port for communication, skip to [Configure the Agent to Communicate over a Specific Port](#configure-the-agent-to-communicate-over-a-specific-port).

    {{%/notice%}}

    In this example, the IP address for the NetQ hardware is
    *192.168.1.254*.

        cumulus@switch:~$ netq config add agent server 192.168.1.254
        cumulus@switch:~$ netq config restart agent

6.  Optionally, configure the switch or host to run the NetQ CLI.
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

7. Repeat these steps for each Cumulus switch, or use an automation tool to
install NetQ Agent on multiple Cumulus Linux switches.

### Install NetQ Agent on an Ubuntu Server

Before you install the NetQ Agent on an Ubuntu server, make sure the
following packages are installed and running these minimum versions:

  - iproute 1:4.3.0-1ubuntu3.16.04.1 all
  - iproute2 4.3.0-1ubuntu3 amd64
  - lldpd 0.7.19-1 amd64
  - ntp 1:4.2.8p4+dfsg-3ubuntu5.6 amd64

    {{%notice info%}}

Make sure you are running lldp**d**, not lldp**ad**. Ubuntu does not include `lldpd` by default, which is required for the installation.

To install this package, run the following commands:

```
root@ubuntu:~# apt-get update
root@ubuntu:~# apt-get install lldpd
root@ubuntu:~# systemctl enable lldpd.service
root@ubuntu:~# systemctl start lldpd.service
```
    {{%/notice%}}

To install the NetQ Agent on an Ubuntu server:

1.  Reference and update the local `apt` repository.

        root@ubuntu:~# wget -O- https://apps3.cumulusnetworks.com/setup/cumulus-apps-deb.pubkey | apt-key add -

2.  Create the file
    `/etc/apt/sources.list.d/cumulus-host-ubuntu-xenial.list` and add
    the following lines:

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

3.  Install NTP on the server, if not already installed.

        root@ubuntu:~# sudo apt-get install ntp

4.  Configure the NTP server.

    1.  Open the `/etc/ntp.conf` file in your text editor of choice.

    2.  Under the Server section, specify the NTP server IP address or
        hostname.

5.  Enable and start the NTP service.

        root@ubuntu:~# sudo systemctl enable ntp.service
        root@ubuntu:~# sudo systemctl start ntp.service

6.  Verify NTP is operating correctly. Look for an asterisk (\*) or a
    plus sign (+) that indicates the clock is synchronized.

        root@ubuntu:~# ntpq -pn
             remote           refid      st t when poll reach   delay   offset  jitter
        ==============================================================================
        +173.255.206.154 132.163.96.3     2 u   86  128  377   41.354    2.834   0.602
        +12.167.151.2    198.148.79.209   3 u  103  128  377   13.395   -4.025   0.198
         2a00:7600::41   .STEP.          16 u    - 1024    0    0.000    0.000   0.000
        \*129.250.35.250  249.224.99.213   2 u  101  128  377   14.588   -0.299   0.243

7.  Install the meta package on the server.

        root@ubuntu:~# apt-get update
        root@ubuntu:~# apt-get install cumulus-netq

8.  Configure the NetQ Agent to send telemetry data to the NetQ
    Platform, NetQ Appliance, or NetQ Cloud Appliance.  

    {{%notice info%}}

If you intend to use VRF, skip to [Configure the Agent to Use VRF](#configure-the-agent-to-use-a-vrf). If you intend to specify a port for communication, skip to [Configure the Agent to Communicate over a Specific Port](#configure-the-agent-to-communicate-over-a-specific-port).

    {{%/notice%}}

    In this example, the IP address for the NetQ hardware is
    *192.168.1.254*.

        root@ubuntu:~# netq config add agent server 192.168.1.254
        Updated agent server 192.168.1.254 vrf default. Please restart netq-agent (netq config restart agent).
        root@ubuntu:~# netq config restart agent

9.  Optionally, configure the switch or host to run the NetQ CLI.

      - For on-premises deployment:

            root@ubuntu:~# netq config add cli server 192.168.1.254
            Updated cli server 192.168.1.254 vrf default. Please restart netqd (netq config restart cli).
            root@ubuntu:~# netq config restart cli

      - For in-cloud deployment:
         {{%notice info%}}

The switch or host must have access to the Internet to configure CLI access.

         {{%/notice%}}

         Be sure to replace the key values with your user credentials.

         ```
         root@ubuntu:~# netq config add cli server api.netq.cumulusnetworks.com access-key <text-access-key> secret-key <text-secret-key> port 443
         root@ubuntu:~# netq config restart cli
         ```
         or, if you have a *credentials.yml* file, be sure to use the full path to the file and correct file name.
         ```
         root@ubuntu:~$ netq config add cli server api.netq.cumulusnetworks.com cli-keys-file /full-path/credentials.yml port 443
         root@ubuntu:~$ netq config restart cli
         ```

10. Repeat these steps for all of your hosts running Ubuntu, or use an
    automation tool to streamline the process.

### Install NetQ Agent on a Red Hat or CentOS Server

Before you install the NetQ Agent on a Red Hat or CentOS server, make
sure the following packages are installed and running these minimum
versions:

  - iproute-3.10.0-54.el7\_2.1.x86\_64
  - lldpd-0.9.7-5.el7.x86\_64

    {{%notice info%}}

Make sure you are running lldp**d**, not lldp**ad**. CentOS does not include `lldpd` by default, nor does it include `wget`, which is required for the installation.

To install this package, run the following commands:

```
root@rhel7:~# yum -y install epel-release
root@rhel7:~# yum -y install lldpd
root@rhel7:~# systemctl enable lldpd.service
root@rhel7:~# systemctl start lldpd.service
root@rhel7:~# yum install wget
```
    {{%/notice%}}

  - ntp-4.2.6p5-25.el7.centos.2.x86\_64
  - ntpdate-4.2.6p5-25.el7.centos.2.x86\_64

To install the NetQ Agent on a Red Hat or CentOS server:

1.  Reference and update the local `yum` repository.

        root@rhel7:~# rpm --import https://apps3.cumulusnetworks.com/setup/cumulus-apps-rpm.pubkey
        root@rhel7:~# wget -O- https://apps3.cumulusnetworks.com/setup/cumulus-apps-rpm-el7.repo > /etc/yum.repos.d/cumulus-host-el.repo

2.  Edit `/etc/yum.repos.d/cumulus-host-el.repo` to set the `enabled=1`
    flag for the two NetQ repositories.

        root@rhel7:~# vi /etc/yum.repos.d/cumulus-host-el.repo
        ...
        [cumulus-arch-netq-2.2]
        name=Cumulus netq packages
        baseurl=https://apps3.cumulusnetworks.com/repos/rpm/el/7/netq-2.2/$basearch
        gpgcheck=1
        enabled=1
        [cumulus-noarch-netq-2.2]
        name=Cumulus netq architecture-independent packages
        baseurl=https://apps3.cumulusnetworks.com/repos/rpm/el/7/netq-2.2/noarch
        gpgcheck=1
        enabled=1
        ...

3.  Install NTP on the server.

        root@rhel7:~# yum install ntp

4.  Configure the NTP server.

    1.  Open the `/etc/ntp.conf` file in your text editor of choice.
    2.  Under the Server section, specify the NTP server IP address or
        hostname.

5.  Enable and start the NTP service.

        root@rhel7:~# sudo systemctl enable ntpd.service
        root@rhel7:~# sudo systemctl start ntpd.service

6.  Verify NTP is operating correctly. Look for an asterisk (\*) or a
    plus sign (+) that indicates the clock is synchronized.

        root@rhel7:~# ntpq -pn
             remote           refid      st t when poll reach   delay   offset  jitter
        ==============================================================================
        +173.255.206.154 132.163.96.3     2 u   86  128  377   41.354    2.834   0.602
        +12.167.151.2    198.148.79.209   3 u  103  128  377   13.395   -4.025   0.198
         2a00:7600::41   .STEP.          16 u    - 1024    0    0.000    0.000   0.000
        \*129.250.35.250  249.224.99.213   2 u  101  128  377   14.588   -0.299   0.243

7.  Install the Bash completion and NetQ meta packages on the server.

        root@rhel7:~# yum -y install bash-completion
        root@rhel7:~# yum install cumulus-netq

8.  Configure the NetQ Agent to send telemetry data to the NetQ
    Platform, NetQ Appliance, or NetQ Cloud Appliance.  

    {{%notice info%}}
If you intend to use VRF, skip to [Configure the Agent to Use VRF](#configure-the-agent-to-use-a-vrf). If you intend to specify a port for communication, skip to [Configure the Agent to Communicate over a Specific Port](#configure-the-agent-to-communicate-over-a-specific-port).
    {{%/notice%}}

    In this example, the IP address for the NetQ hardware is
    *192.168.1.254*.

        root@rhel7:~# netq config add agent server 192.168.1.254
        Updated agent server 192.168.1.254 vrf default. Please restart netq-agent (netq config restart agent).
        root@rhel7:~# netq config restart agent

9.  Optionally, configure the switch or host to run the NetQ CLI.

    1.  For on-premises deployment:

         ```
         root@rhel7:~# netq config add cli server 192.168.1.254
         Updated cli server 192.168.1.254 vrf default. Please restart netqd (netq config restart cli).
         root@rhel7:~# netq config restart cli
         ```

    2.  For in-cloud deployment:

         {{%notice info%}}

The switch or host must have access to the Internet to configure CLI access.

         {{%/notice%}}

         Be sure to replace the key values with your user credentials.
         ```
         root@rhel7:~# netq config add cli server api.netq.cumulusnetworks.com access-key <text-access-key> secret-key <text-secret-key> port 443
         root@rhel7:~# netq config restart cli
         ```
         or, if you created a *credentials.yml* file, be sure to use the full path to the file and correct file name.

         ```
         root@rhel7:~# netq config add cli server api.netq.cumulusnetworks.com cli-keys-file /full-path/credentials.yml port 443
         root@rhel7:~# netq config restart cli
         ```

10. Repeat these steps for all of your hosts running Ubuntu, or use an
    automation tool to streamline the process.

## Configure Optional NetQ Agent Settings

Once the NetQ Agents have been installed on the network nodes you want
to monitor, the NetQ Agents must be configured to obtain useful and
relevant data. The code examples shown in this section illustrate how to
configure the NetQ Agent on a Cumulus switch, but it is exactly the same
for the other type of nodes. Depending on your deployment, follow the
relevant additional instructions after the basic configuration steps:

  - [Configuring the Agent to Use a VRF](#configure-the-agent-to-use-a-vrf)
  - [Configuring the Agent to Communicate over a Specific Port](#configure-the-agent-to-communicate-over-a-specific-port)

### Configure the Agent to Use a VRF

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

By default, NetQ uses port 31980 for communication between the NetQ
Platform and NetQ Agents. If you want the NetQ Agent to communicate with
the NetQ Platform via a different port, you need to specify the port
number when configuring the NetQ Agent like this:

    cumulus@leaf01:~$ netq config add agent server 192.168.1.254 port 7379

You then restart the agent:

    cumulus@leaf01:~$ netq config restart agent

## Integrate with Event Notification Tools

If you want to proactively monitor events in your network, you can
integrate NetQ with the PagerDuty or Slack notification tools. To do so
you need to configure both the notification application itself to
receive the messages, and NetQ with what messages to send and where to
send them. Refer to [Integrate NetQ with Event Notification Applications](/cumulus-netq/Cumulus-NetQ-Integration-Guide/integrate-netq-with-notification-applications)
to use the CLI for configuration.

## Set Up Security

When you set up and configured your
Cumulus Linux switches, you likely configured a number of the security
features available. Cumulus recommends the same security measures be
followed for the NetQ Platform in the out-of-band-network. Refer to the
[Securing Cumulus Linux white paper](https://cumulusnetworks.com/learn/web-scale-networking-resources/white-papers/securing-cumulus-linux/) for details.

Your Cumulus Linux switches have a number
of ports open by default. A few additional ports must be opened to run
the NetQ software (refer to [Default Open Ports in Cumulus Linux and NetQ](https://support.cumulusnetworks.com/hc/en-us/articles/228281808-Default-Open-Ports-in-Cumulus-Linux-and-NetQ) article).
