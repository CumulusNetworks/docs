---
title: Install NetQ Software on Your Server
author: Cumulus Networks
weight: 409
aliases:
 - /display/NETQ/Install+NetQ
 - /pages/viewpage.action?pageId=12320951
pageID: 12320951
product: Cumulus NetQ
version: 2.3
imgData: cumulus-netq
siteSlug: cumulus-netq
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
| 31980 | On-premises and cloud | NetQ Platform             |
| 32708 | On-premises           | API Gateway               |
| 32666 | On-premises           | Web-based User Interface  |

### NetQ Platform HyperVisor Requirements

The NetQ Platform can be installed as a Virtual Machine (VM) using one
of the following hypervisors:

- VMware ESXi™ 6.5 for servers running Cumulus Linux, CentOS, Ubuntu
    and RedHat operating systems.
- KVM/QCOW (QEMU Copy on Write) image for servers running CentOS,
    Ubuntu and RedHat operating systems.

### NetQ Agent Operating System Requirements

NetQ 2.3 Agents are supported on the following switch and host operating
systems:

- Cumulus Linux 3.3.2 and later
- Ubuntu 16.04
- Ubuntu 18.04 (NetQ 2.2.2 and later)
- Red Hat<sup>®</sup> Enterprise Linux (RHEL) 7.1
- CentOS 7

### NetQ Application Support

The NetQ CLI, UI, and RESTful API are supported on NetQ 2.1.0 and later.
NetQ 1.4 and earlier applications are not supported in NetQ 2.x.

### Install Workflow

Installation of NetQ involves installing the NetQ software, and
installing and configuring the NetQ Agents. Additional steps are needed
to [Integrate NetQ with Event Notification Applications](../../../Cumulus-NetQ-Integration-Guide/Integrate-NetQ-with-Notification-Applications).
This flow chart shows the required steps to install and setup
NetQ to start validating your network, and the optional steps of
integrating with event notification applications and monitoring hosts.

{{<figure src="/images/netq/install-wkflow-on-prem-cust-hw-222.png">}}

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

## Install Cumulus NetQ for an On-premises Deployment
Follow the instructions in this section to install Cumulus NetQ software onto a server that is to be deployed and managed on your premises. For cloud deployments, refer to [Install Cumulus NetQ for a Cloud Deployment](#install-cumulus-netq-for-a-cloud-deployment).

### On-Premises Install Workflow

Installation of NetQ involves installing the NetQ software, and
installing and configuring the NetQ Agents. Additional steps are needed
to [Integrate NetQ with Notification Applications](../../../Cumulus-NetQ-Integration-Guide/Integrate-NetQ-with-Notification-Applications).

{{<figure src="/images/netq/install-flow-cust-hw-on-prem-nq222.png" width="600" >}}

### Install the NetQ Software

To install the NetQ software onto your own hardware using a VM image:

1.  **IMPORTANT**: Confirm that your server hardware meets the
    requirements set out [here](#hardware-requirements).
2.  Download the NetQ Platform image.

    1.  On the [Cumulus Downloads](https://cumulusnetworks.com/downloads/) page, select
        *NetQ* from the **Product** list box.

    2.  Click *2.3* from the **Version** list box, and then select
        *2.3.x* from the submenu.

    3.  Optionally, select the hypervisor you wish to use (*VMware* or *KVM*) from the
        **Hypervisor/Platform** list box.

        {{< figure src="/images/netq/netq-23-download-options-230.png" width="500" >}}

    4.  Scroll down to review the images that match your selection
        criteria, and click **Download** for the image you want.

        {{< figure src="/images/netq/netq-23-vm-dwnld-230.png" width="400" >}}

3.  Open your hypervisor and set up your VM.  
    You can use these examples for reference or use your own hypervisor
    instructions.

    <details><summary>VMware example</summary>

      This example shows the VM setup process using an OVA file with VMware
      ESXi.

      1. Enter the address of the hardware in your browser.

      2. Log in to VMware using credentials with root access.  

          {{< figure src="/images/netq/vmw-main-page.png" width="700" >}}

      3. For an on-site NetQ Platform deployment, click **Storage** in the
          Navigator to verify you have an SSD installed.  

          {{< figure src="/images/netq/vmw-verify-storage.png" width="700" >}}

      4. Click **Create/Register VM** at the top of the right pane.

          {{< figure src="/images/netq/vmw-menu-create-register.png" width="700" >}}

      5. Select **Deploy a virtual machine from and OVF or OVA file**, and
          click **Next**.  

          {{< figure src="/images/netq/vmw-deploy-vm-from-ova.png" width="700" >}}

      6. Provide a name for the VM, for example *Cumulus NetQ*.

      7. Drag and drop the NetQ Platform image file you downloaded in Step 1 above.
      8. Click **Next**.

          {{< figure src="/images/netq/vmw-name-the-vm.png" width="700" >}}

      9. Select the storage type and data store for the image to use, then
          click **Next**. In this example, only one is available.

          {{< figure src="/images/netq/vmw-select-storage.png" width="700" >}}

      10. Accept the default deployment options or modify them according to
          your network needs. Click **Next** when you are finished.

          {{< figure src="/images/netq/vmw-default-deploy-options.png" width="700" >}}

      11. Review the configuration summary. Click **Back** to change any of
          the settings, or click **Finish** to continue with the creation of
          the VM.

          {{< figure src="/images/netq/vmw-review-before-create.png" width="700" >}}

          The progress of the request is shown in the Recent Tasks window at
          the bottom of the application. This may take some time, so continue
          with your other work until the upload finishes.

      12. Once completed, view the full details of the VM and hardware.

          {{< figure src="/images/netq/vmw-deploy-results.png" width="700" >}}

    </details>

    <details><summary>KVM example</summary>

      This example shows the VM setup process for a system with Libvirt and
      KVM/QEMU installed.

      1. Confirm that the SHA256 checksum matches the one posted on the Cumulus Downloads website to ensure the image download has not been corrupted.

```
$ sha256sum ./Downloads/cumulus-netq-server-2.3.0-ts-amd64-qemu.qcow2
$ 6fff5f2ac62930799b4e8cc7811abb6840b247e2c9e76ea9ccba03f991f42424  ./Downloads/cumulus-netq-server-2.2.0-ts-amd64-qemu.qcow2
```

      2. Copy the QCOW2 image to a directory where you want to run it.

        {{%notice tip%}} 
Copy, instead of moving, the original QCOW2 image that was downloaded to avoid re-downloading it again later should you need to perform this process again.
        {{%/notice%}}

```
$ sudo mkdir /vms
$ sudo cp ./Downloads/cumulus-netq-server-2.3.0-ts-amd64-qemu.qcow2 /vms/ts.qcow2
```

      3. Create the VM.

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

If you have changed the IP address or hostname of the NetQ server, you need to
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
    **Note**: Allow 15 minutes for the prompt to return.

{{%/notice%}}

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
        operating properly.

            cumulus@<netq-platform-hostname>:~$ netq show opta-health
            Application                    Status    Health    Kafka Stream    Git Hash    Timestamp
            -----------------------------  --------  --------  --------------  ----------  ------------------------
            netq-app-macfdb                UP        true      up              14b42e6     Mon Jun  3 20:20:35 2019
            netq-app-interface             UP        true                      0fe11c6     Mon Jun  3 20:20:34 2019
            netq-app-vlan                  UP        true                      4daed85     Mon Jun  3 20:20:35 2019
            netq-app-sensors               UP        true      up              f37272c     Mon Jun  3 20:20:34 2019

            ...

            netq-app-ntp                   UP        true      up              651c86f     Mon Jun  3 20:20:35 2019
            netq-app-customermgmt          UP        true                      7250354     Mon Jun  3 20:20:34 2019
            netq-app-node                  UP        true      up              f676c9a     Mon Jun  3 20:20:34 2019
            netq-app-route                 UP        true      up              6e31f98     Mon Jun  3 20:20:35 2019
             
            cumulus@<netq-platform-hostname>:~$

        {{%notice note%}}

Please allow 10-15 minutes for all applications to come up and report their status. If any of the applications or services display status as DOWN after 30 minutes, open a [support ticket](https://cumulusnetworks.com/support/file-a-ticket/) and attach the output of the `opta-support` command.

        {{%/notice%}}

2.  Verify that NTP is configured and running. NTP operation is critical
    to proper operation of NetQ. Refer to [Setting Date and Time](/cumulus-linux/System-Configuration/Setting-Date-and-Time/) in the *Cumulus Linux User Guide* for details and instructions.

      {{%notice tip%}}

If you are still experiencing issues with your installation, confirm that your DNS server is properly configured.

      {{%/notice%}}

You are almost done. The NetQ server installation is complete. The final step is to install NetQ Agents on each of the switches and hosts you want monitored. Go to [Install the NetQ Agent and CLI on Switches](../Install-NetQ-Agents-and-CLI-on-Switches) for these instructions.

## Install Cumulus NetQ for a Cloud Deployment

Follow the instructions in this section to install Cumulus NetQ software onto a server that is to be installed and managed on your premises, but that accesses the Cumulus NetQ Cloud for application and data storage. For on-premises deployments, refer to [Install Cumulus NetQ for an On-premises Deployment](#install-cumulus-netq-for-an-on-premises-deployment).

### Cloud Deployment Install Workflow

Installation of NetQ involves installing the NetQ software, and
installing and configuring the NetQ Agents. Additional steps are needed
to [Integrate NetQ with Notification Applications](../../../Cumulus-NetQ-Integration-Guide/Integrate-NetQ-with-Notification-Applications).

{{<figure src="/images/netq/install-flow-cust-hw-cloud-nq222.png" width="600" >}}

### Download NetQ Virtual Machine

To install the NetQ VM image onto your own hardware:

1.  **IMPORTANT**: Confirm that your server hardware meets the
    requirements set out [here](#hardware-requirements).
2.  Download the NetQ Platform image.

    1.  On the [Cumulus Downloads](https://cumulusnetworks.com/downloads/) page, select
        *NetQ* from the **Product** list box.

    2.  Click *2.3* from the **Version** list box, and then select
        *2.3.x* from the submenu.

    3.  Optionally, select the hypervisor you wish to use (*VMware (Cloud)* or *KVM (Cloud)*) from the
        **Hypervisor/Platform** list box.

        {{< figure src="/images/netq/netq-23-download-options-230.png" width="500" >}}

    4.  Scroll down to review the images that match your selection
        criteria, and click **Download** for the image you want.

        {{< figure src="/images/netq/netq-23-vm-cloud-dwnld-230.png" width="400" >}}

3.  Open your hypervisor and set up your VM.  
    You can use these examples for reference or use your own hypervisor
    instructions.

    <details><summary>VMware example</summary>

    This example shows the VM setup process using an OVA file with VMware
    ESXi.

    1. Enter the address of the hardware in your browser.

    2. Log in to VMware using credentials with root access.  

        {{< figure src="/images/netq/vmw-main-page.png" width="700" >}}

    3. Click **Create/Register VM** at the top of the right pane.

        {{< figure src="/images/netq/vmw-menu-create-register.png" width="700" >}}

    4. Select **Deploy a virtual machine from and OVF or OVA file**, and
        click **Next**.  

        {{< figure src="/images/netq/vmw-deploy-vm-from-ova.png" width="700" >}}

    5. Provide a name for the VM, for example *Cumulus NetQ*.

    6. Drag and drop the NetQ Platform image file you downloaded in Step 1 above.

    7. Click **Next**.

        {{< figure src="/images/netq/vmw-name-the-vm.png" width="700" >}}

    8. Select the storage type and data store for the image to use, then
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

            $ sha256sum ./Downloads/cumulus-netq-server-2.3.0-ts-amd64-qemu.qcow2
            $ 6fff5f2ac62930799b4e8cc7811abb6840b247e2c9e76ea9ccba03f991f42424  ./Downloads/cumulus-netq-server-2.3.0-ts-amd64-qemu.qcow2

    2.  Copy the QCOW2 image to a directory where you want to run it.

        {{%notice tip%}}

Copy, instead of moving, the original QCOW2 image that was downloaded to avoid re-downloading it again later should you need to perform this process again.

        {{%/notice%}}

            $ sudo mkdir /vms
            $ sudo cp ./Downloads/cumulus-netq-server-2.3.0-ts-amd64-qemu.qcow2 /vms/ts.qcow2

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

If you have changed the IP address or hostname of the NetQ server, you need to
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
    **Note**: Allow 15 minutes for the prompt to return.

{{%/notice%}}

### Download and Install NetQ Cloud Components

Download and install the tarball file.

The `config-key` was provided to you by Cumulus Networks via an email titled *A new site has been added to your Cumulus NetQ account*. If you have lost it, submit a [support request](https://support.cumulusnetworks.com/hc/en-us/requests/new) to have it sent to you again.

**Note**: Be sure to replace the interface and key values with values appropriate for your configuration. This example uses eth0 and a sample key.

```
cumulus@netq-platform:~$ netq install opta interface eth0 tarball download config-key "CNKaDBIjZ3buZhV2Mi5uZXRxZGV2LmN1bXVsdXNuZXw3b3Jrcy5jb20YuwM="
```

{{%notice info%}}

If you changed the IP address or interface of the appliance to something other than what it was assigned previously, you must inform NetQ of the change.

If you changed the IP address, but kept the interface the same (for example, eth0), re-run the `netq install opta interface` command using your config-key:

```
cumulus@netq-platform:~$ netq install opta interface eth0 tarball NetQ-2.3.x-opta.tgz config-key "CNKaDBIjZ3buZhV2Mi5uZXRxZGV2LmN1bXVsdXNuZXw3b3Jrcy5jb20YuwM="
```

If you changed the interface (for example, eth0 to eth1), run the `netq install opta interface` command with the new interface and your config-key:

```
cumulus@netq-platform:~$ netq install opta interface eth1 tarball NetQ-2.2.x-opta.tgz config-key "CNKaDBIjZ3buZhV2Mi5uZXRxZGV2LmN1bXVsdXNuZXw3b3Jrcy5jb20YuwM="
```

{{%/notice%}}

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

### Verify Cloud Installation

Now that your appliance is installed and configured, you can verify that all applications and services are operating properly.

```
cumulus@netq-platform:~$ netq show opta-health
OPTA is healthy
```

### Configure CLI Access on Appliance

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
The secret key is only shown once. If you do not copy these, you will need to regenerate them and reconfigure CLI access.

In version 2.2.1 and later, you can save these keys to a YAML file for easy reference, and to avoid having to type or copy the key values. You can:

- store the file wherever you like, for example in */home/cumulus/* or */etc/netq*
- name the file whatever you like, for example *credentials.yml*, *creds.yml*, or *keys.yml*

BUT, the file must have the following format:

```
access-key: <user-access-key-value-here>
secret-key: <user-secret-key-value-here>
```

      {{%/notice%}}

7. Configure access to the CLI:
   - In NetQ 2.3.x, run the following commands. Replace the key values with your generated keys.
   ```
   cumulus@netq-platform:~$ netq config add cli server api.netq.cumulusnetworks.com access-key <text-access-key> secret-key <text-secret-key> premises <text-premises-name> port 443
   Successfully logged into NetQ cloud at api.netq.cumulusnetworks.com:443
   Updated cli server api.netq.cumulusnetworks.com vrf default port 443. Please restart netqd (netq config restart cli)

   cumulus@netq-platform:~$ netq config restart cli
   Restarting NetQ CLI... Success!
   ```
   - In NetQ 2.2.1 and later, if you have created a keys file as noted in the previous step, run the following commands. Be sure to include the *full path* the to file.
   ```
   cumulus@netq-platform:~$ netq config add cli server api.netq.cumulusnetworks.com cli-keys-file /full-path/credentials.yml port 443
   Successfully logged into NetQ cloud at api.netq.cumulusnetworks.com:443
   Updated cli server api.netq.cumulusnetworks.com vrf default port 443. Please restart netqd (netq config restart cli)

   cumulus@netq-platform:~$ netq config restart cli
   Restarting NetQ CLI... Success!
   ```

With your NetQ cloud server set up and configured, you are ready to install the NetQ Agent on each switch and host you want to monitor with NetQ. Follow the instructions in [Install the NetQ Agent and CLI on Switches](../Install-NetQ-Agents-and-CLI-on-Switches) for details.

## Integrate with Event Notification Tools

If you want to proactively monitor events in your network, you can
integrate NetQ with the PagerDuty or Slack notification tools. To do so
you need to configure both the notification application itself to
receive the messages, and NetQ with what messages to send and where to
send them. Refer to [Integrate NetQ with Notification Applications](../../../Cumulus-NetQ-Integration-Guide/Integrate-NetQ-with-Notification-Applications/)
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
