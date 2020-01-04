---
title: Prepare for Installation
author: Cumulus Networks
weight: 409
aliases:
 - /display/NETQ/Install+NetQ
 - /pages/viewpage.action?pageId=12320951
pageID: 12320951
product: Cumulus NetQ
version: 2.4
imgData: cumulus-netq
siteSlug: cumulus-netq
---
Whether you are using a single server or cluster of servers to create an on-premises or cloud deployment, there are some preparation steps to complete before using the Admin UI or the NetQ CLI to complete the installation.

If you are using one of the NetQ appliances, you must first prepare these before performing these preparation steps. If you are using your own hardware, you can skip to [Preparation Steps](#preparation-steps).

{{%notice info%}}
A fresh server or appliance is recommended for NetQ installation. Alternately, you can create a new VM or re-image an existing server with Ubuntu as the base operating system. Be sure to back up any NetQ data beforehand if you choose this alternative.
{{%/notice%}}

## Prepare Your NetQ Appliance

Inside the box that was shipped to you, you'll find:

- Your Cumulus NetQ Appliance (a Supermicro 6019P-WTR server) or your Cumulus NetQ Cloud Appliance (a Supermicro SuperServer E300-9D)
- Hardware accessories, such as power cables and rack mounting gear (note that network cables and optics ship separately)
- Information regarding your order

For more detail about hardware specifications (including LED layouts and FRUs like the power supply or fans, and accessories like included cables) or safety and environmental information, refer to:

- NetQ Appliance:  [user manual](https://www.supermicro.com/manuals/superserver/1U/MNL-1943.pdf) and [quick reference guide](https://www.supermicro.com/QuickRefs/superserver/1U/QRG-1943.pdf)
- NetQ Cloud Appliance:  [user manual](https://www.supermicro.com/manuals/superserver/mini-itx/MNL-2094.pdf)

### Install the Appliance

After you unbox the appliance:

1. Mount the appliance in the rack.
2. Connect it to power following the procedures described in your appliance's user manual.
3. Connect the Ethernet cable to the 1G management port (eth0).
4. Power on the appliance.

   {{< figure src="/images/netq/netq-appliance-port-connections.png" width="700" caption="NetQ Appliance connections">}}

   {{< figure src="/images/netq/netq-cloud-appl-port-connections.png" width="475" caption="NetQ Cloud Appliance connections">}}

If your network runs DHCP, you can configure Cumulus NetQ over the network. If DHCP is not enabled, then you configure the appliance using the console cable provided.

### Configure the Password, Hostname and IP Address

Change the password using the `passwd` command:

```
$ passwd 
Changing password for <user>.
(current) UNIX password: 
Enter new UNIX password: 
Retype new UNIX password: 
passwd: password updated successfully
```

By default, DHCP is used to acquire the hostname and IP address. However, you can manually specify the hostname with the following command:

```
sudo hostnamectl set-hostname <newHostNameHere>
```

You can also configure these items using the Ubuntu Netplan configuration tool. For example, to set your network interface *eth0* to a static IP address of *192.168.1.222* with gateway *192.168.1.1* and DNS server as *8.8.8.8* and *8.8.4.4*:

1. Edit the */etc/netplan/01-eth0.yaml* Netplan configuration file:

    ```
    # This file describes the network interfaces available on your system
    ...
    # For more information, see netplan(5).
    network:
    version: 2
    renderer: networkd
    ethernets:
        eth0:
        dhcp4: no
        addresses: [192.168.1.222/24]
        gateway4: 192.168.1.1
        nameservers:
        addresses: [8.8.8.8,8.8.4.4]
    ...
    ```

2. Apply the settings.

```
$ sudo netplan apply
```

Continue with the steps in [Download the Installer Program and NetQ Installation Tarball](#download-the-installer-program-and-netq-installation-tarball).

## Prepare Your Own Server

If you are using your own hardware server, you must first install Ubuntu OS 18.04 and then install and configure your VM.

### Install Ubuntu

The NetQ software runs on the Ubuntu OS, version 18.04. Log in to server and install Ubuntu 18.04.3 LTS by following the instructions [here](https://www.fosslinux.com/6406/how-to-install-ubuntu-server-18-04-lts.htm).

### Install and Configure a VM

To install and configure a VM on your own hardware:

1.  **IMPORTANT**: Confirm that your server hardware meets the
    requirements identified in the [Prerequites](../Prerequisites/#hardware-requirements).
2.  Download the NetQ Platform image.

    1.  On the [Cumulus Downloads](https://cumulusnetworks.com/downloads/) page, select *NetQ* from the **Product** list.

    2.  Click *2.4* from the **Version** list, and then select
        *2.4.0* from the submenu.

    3.  Optionally, select the hypervisor you wish to use (*VMware*, *VMware (Cloud)*, *KVM*, or *KVM (Cloud)*) from the **Hypervisor/Platform** list.

        {{< figure src="/images/netq/netq-24-download-options-240.png" width="500" >}}

    4.  Scroll down to review the images that match your selection
        criteria, and click **Download** for the image you want.

        {{< figure src="/images/netq/netq-24-vm-dwnld-240.png" width="700" >}}

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
$ sha256sum ./Downloads/cumulus-netq-server-2.4.0-ts-amd64-qemu.qcow2
$ 6fff5f2ac62930799b4e8cc7811abb6840b247e2c9e76ea9ccba03f991f42424  ./Downloads/cumulus-netq-server-2.4.0-ts-amd64-qemu.qcow2
```

      2. Copy the QCOW2 image to a directory where you want to run it.

        {{%notice tip%}} 
Copy, instead of moving, the original QCOW2 image that was downloaded to avoid re-downloading it again later should you need to perform this process again.
        {{%/notice%}}

```
$ sudo mkdir /vms
$ sudo cp ./Downloads/cumulus-netq-server-2.4.0-ts-amd64-qemu.qcow2 /vms/ts.qcow2
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

      5.  From the Console of the VM, check to see which IP address Eth0 has obtained via DHCP, or alternatively set a static IP address by editing the */etc/netplan/01-eth0.yaml* Netplan configuration file:

        ```
        # This file describes the network interfaces available on your system
        ...
        # For more information, see netplan(5).
        network:
        version: 2
        renderer: networkd
        ethernets:
            eth0:
            dhcp4: no
            addresses: [192.168.1.222/24]
            gateway4: 192.168.1.1
            nameservers:
            addresses: [8.8.8.8,8.8.4.4]
        ...
        ```
        
        Apply the settings.

        ```
        $ sudo netplan apply
        ```

    Continue with the steps in the next section.
      </details>

## Download the Installer Program and NetQ Installation Tarball

Follow the steps below based on the type of deployment and server arrangement you intend to install.

### On-premises Deployment, Standalone Server

To prepare your standalone NetQ platform for an on-premises deployment:

1. For NetQ appliances, download the installer program (`netq-bootstrap-2.4.0.tgz`) and the NetQ installation tarball (`NetQ-2.4.0.tgz`) from the [Cumulus Downloads](https://cumulusnetworks.com/downloads/) page.
    {{%notice note%}}
If you have installed a VM on your own server, skip to Step 3.
    {{%/notice%}}
    1. Select *NetQ* from the **Product** list.
    2. Select *2.4* from the **Version** list, and then select
        *2.4.0* from the submenu.
    3. Select *Bootstrap* from the **Hypervisor/Platform** list.
    4. Scroll down and click **Download**.
    5. Select *Install*  from the  **Hypervisor/Platform** list.
    6. Scroll down and click **Download**.
2. Copy the files to the */mnt/installables/* directory on your server.
3. Optionally back up your NetQ data.
    This example shows how to backup NetQ 2.3.1 data. Be sure to substitute the `backup-directory` option with the full path to your local backup directory.
    
    ```
    cumulus@<server>:~$ ./backuprestore.sh --backup --localdir /opt/<backup-directory>
    ```

    Refer to [Back Up Your NetQ Data](../../Cumulus-NetQ-Deployment-Guide/Backup-and-Restore-NetQ/Backup-NetQ/) for more detail about this command.
4. Run the installer program on your NetQ platform server.

    ```
    cumulus@<hostname>:~$ netq bootstrap master interface eth0 tarball /mnt/installables/netq-bootstrap-2.4.0.tgz
    ```
    Allow about five minutes for this to complete.

    {{%notice tip%}}
If this fails for any reason, you can run `netq bootstrap reset` and then try again.
    {{%/notice%}}

5. Verify the server is ready for installation. Fix any errors indicated before installing the NetQ software.

    ```
    cumulus@<hostname>:~$ sudo opta-check
    ```

### Cloud Deployment, Standalone Server

To prepare your standalone NetQ platform for a cloud deployment:

1. Download the installer program (`netq-bootstrap-2.4.0.tgz`) and the NetQ installation tarball (`NetQ-2.4.0-opta.tgz`) from the [Cumulus Downloads](https://cumulusnetworks.com/downloads/) page.
    {{%notice note%}}
If you have installed a VM on your own server, skip to Step 3.
    {{%/notice%}}
    1. Select *NetQ* from the **Product** list.
    2. Select *2.4* from the **Version** list, and then select
        *2.4.0* from the submenu.
    3. Select *Bootstrap* from the **Hypervisor/Platform** list.
    4. Scroll down and click **Download**.
    5. Select *Install (Cloud)* from the **Hypervisor/Platform** list.
    6. Scroll down and click **Download**.
2. Copy these files to the */mnt/installables/* directory on your server.
3. Run the installer program on your NetQ platform server.

    ```
    cumulus@<hostname>:~$ netq bootstrap master interface eth0 tarball /mnt/installables/netq-bootstrap-2.4.0.tgz
    ```
    Allow about five minutes for this to complete.

    {{%notice tip%}}
If this fails for any reason, you can run `netq bootstrap reset` and then try again.
    {{%/notice%}}

5. Verify the server is ready for installation. Fix any errors indicated before installing the NetQ software.

    ```
    cumulus@<hostname>:~$ sudo opta-check-cloud
    ```
    
4. While this runs, locate your `config-key` provided by Cumulus Networks in an email titled *A new site has been added to your Cumulus NetQ account*. If you have lost it, submit a [support request](https://support.cumulusnetworks.com/hc/en-us/requests/new) to have it sent to you again.

### On-premises Deployment,  Server Cluster

To prepare your NetQ server cluster for an on-premises deployment:

1. Download the installer program (`netq-bootstrap-2.4.0.tgz`) and the NetQ installation tarball (`NetQ-2.4.0.tgz`) from the [Cumulus Downloads](https://cumulusnetworks.com/downloads/) page.
    {{%notice note%}}
If you have installed a VM on your own server, skip to Step 3.
    {{%/notice%}}
    1. Select *NetQ* from the **Product** list.
    2. Select *2.4* from the **Version** list, and then select
        *2.4.0* from the submenu.
    3. Select *Bootstrap* from the **Hypervisor/Platform** list.
    4. Scroll down click **Download**.
    5. Select *Install* from the **Hypervisor/Platform** list.
    6. Scroll down and click **Download**.
2. Copy these files to the */mnt/installables/* directory on your master and worker nodes.
3. Optionally back up your NetQ data.
    
    This example shows how to backup NetQ 2.3.1 data. Be sure to substitute the `backup-directory` option with the full path to your local backup directory.
    
    ```
    cumulus@<hostname>:~$ ./backuprestore.sh --backup --localdir /opt/<backup-directory>
    ```

    Refer to [Back Up Your NetQ Data](../../Cumulus-NetQ-Deployment-Guide/Backup-and-Restore-NetQ/Backup-NetQ/) for more detail about this command.
4. Run the installer program on your master node.

    ```
    cumulus@<hostname>:~$ netq bootstrap master interface eth0 tarball /mnt/installables/netq-bootstrap-2.4.0.tgz
    ```
    Allow about five minutes for this to complete,  and only then continue to the next step.

    {{%notice tip%}}
If this step fails for any reason, you can run `netq bootstrap reset` and then try again.
    {{%/notice%}}

5. Verify the server is ready for installation. Fix any errors indicated before installing the NetQ software.

    ```
    cumulus@<hostname>:~$ sudo opta-check
    ```

6. Run the installer program on each of your two worker nodes, using the IP address of your master node.

    ```
    cumulus@<server>:~$ netq bootstrap worker tarball /mnt/installables/netq-bootstrap-2.4.0.tgz master-ip <master-ip>
    ```
    
    Allow about five minutes for this to complete.

    {{%notice tip%}}
If this step fails for any reason, you can run `netq bootstrap reset` on the relevant node and then try again.
    {{%/notice%}}

6. Make a note of the private IP addresses for your master and worker nodes.

### Cloud  Deployment,  Server Cluster

To prepare your NetQ server cluster:

1. Download the installer program (`netq-bootstrap-2.4.0.tgz`) and the NetQ installation tarball (`NetQ-2.4.0-opta.tgz`) from the [Cumulus Downloads](https://cumulusnetworks.com/downloads/) page.
    {{%notice note%}}
If you have installed a VM on your own server, skip to Step 3.
    {{%/notice%}}
    1. Select *NetQ* from the **Product** list.
    2. Select *2.4* from the **Version** list, and then select
        *2.4.0* from the submenu.
    3. Select *Bootstrap* from the **Hypervisor/Platform** list.
    4. Scroll down and click **Download**.
    5. Select *Install (Cloud)* from the **Hypervisor/Platform** list.
    6. Scroll down and click **Download**.
2. Copy these files to the */mnt/installables/* directory on your master and worker nodes.
3. Run the installer program on your master node.

    ```
    cumulus@<hostname>:~$ netq bootstrap master interface eth0 tarball /mnt/installables/netq-bootstrap-2.4.0.tgz
    ```

    Allow about five minutes for this to complete,  and only then continue to the next step.

    {{%notice tip%}}
If this step fails for any reason, you can run `netq bootstrap reset` and then try again.
    {{%/notice%}}

4. Run the installer program on your two worker nodes, using the IP address of your master node.

    ```
    cumulus@<hostname>:~$ netq bootstrap worker tarball /mnt/installables/netq-bootstrap-2.4.0.tgz master-ip <master-ip>
    ```

    Allow about five minutes for this to complete.

    {{%notice tip%}}
If either of these steps fail for any reason, you can run `netq bootstrap reset` on the relevant node and then try again.
    {{%/notice%}}

5. While this is running:

    -  Locate the `config-key` provided by Cumulus Networks in an email titled *A new site has been added to your Cumulus NetQ account*. If you have lost it, submit a [support request](https://support.cumulusnetworks.com/hc/en-us/requests/new) to have it sent to you again.
    -  Make a note of the private IP addresses for your master and worker nodes.

You are now ready to use the Admin UI (preferred) or NetQ CLI to complete the installation.
