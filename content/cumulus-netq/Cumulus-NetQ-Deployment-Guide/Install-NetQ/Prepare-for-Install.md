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

## Prepare a NetQ Appliance

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

If your network runs DHCP, you can configure Cumulus NetQ and Cumulus Linux over the network. If DHCP is not enabled, then you configure the appliance using the console cable provided.

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

Continue with the preparation steps in the next section.

## Preparation Steps

Follow the steps below based on the type of deployment and server arrangement you intend to install.

### On-premises Deployment, Standalone Server

To prepare your standalone NetQ platform for an on-premises deployment:

1. Download the installer program (`netq-bootstrap-2.4.0.tgz`) and the NetQ installation tarball (`NetQ-2.4.0.tgz`) from the [Cumulus Downloads](https://cumulusnetworks.com/downloads/) page.
    1. Select *NetQ* from the **Product** list box.
    2. Select *2.4* from the **Version** list box, and then select
        *2.4.0* from the submenu.
    3. Select *Bootstrap* from the **Hypervisor/Platform** list box.
    4. Scroll down to review the images that match your selection
        criteria, and click **Download** for the on-premises version.
    5. Select the hypervisor you want to use (*VMware* or *KVM*) from the **Hypervisor/Platform** list box.
    6. Scroll down to review the images that match your selection
        criteria, and click **Download** for the standalone image.
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

    {{%notice note%}}
If this fails for any reason, you can run `netq bootstrap reset` and then try again.
    {{%/notice%}}

### Cloud Deployment, Standalone Server

To prepare your standalone NetQ platform for a cloud deployment:

1. Download the installer program (`netq-bootstrap-2.4.0.tgz`) and the NetQ installation tarball (`NetQ-2.4.0-opta.tgz`) from the [Cumulus Downloads](https://cumulusnetworks.com/downloads/) page.
    1. Select *NetQ* from the **Product** list box.
    2. Select *2.4* from the **Version** list box, and then select
        *2.4.0* from the submenu.
    3. Select *Bootstrap* from the **Hypervisor/Platform** list box.
    4. Scroll down to review the images that match your selection
        criteria, and click **Download** for the cloud version.
    5. Select the hypervisor you want to use (*VMware* or *KVM*) from the **Hypervisor/Platform** list box.
    6. Scroll down to review the images that match your selection
        criteria, and click **Download** for the standalone image.
2. Copy these files to the */mnt/installables/* directory on your server.
3. Run the installer program on your NetQ platform server.

    ```
    cumulus@<hostname>:~$ netq bootstrap master interface eth0 tarball /mnt/installables/netq-bootstrap-2.4.0.tgz
    ```
    Allow about five minutes for this to complete.

    {{%notice note%}}
If this fails for any reason, you can run `netq bootstrap reset` and then try again.
    {{%/notice%}}

4. While this runs, locate your `config-key` provided by Cumulus Networks in an email titled *A new site has been added to your Cumulus NetQ account*. If you have lost it, submit a [support request](https://support.cumulusnetworks.com/hc/en-us/requests/new) to have it sent to you again.

### On-premises Deployment,  Server Cluster

To prepare your NetQ server cluster for an on-premises deployment:

1. Download the installer program (`netq-bootstrap-2.4.0.tgz`) and the NetQ installation tarball (`NetQ-2.4.0.tgz`) from the [Cumulus Downloads](https://cumulusnetworks.com/downloads/) page.
    1. Select *NetQ* from the **Product** list box.
    2. Select *2.4* from the **Version** list box, and then select
        *2.4.0* from the submenu.
    3. Select *Bootstrap* from the **Hypervisor/Platform** list box.
    4. Scroll down to review the images that match your selection
        criteria, and click **Download** for the on-premises version.
    5. Select the hypervisor you want to use (*VMware* or *KVM*) from the **Hypervisor/Platform** list box.
    6. Scroll down to review the images that match your selection
        criteria, and click **Download** for the cluster image.
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
5. Run the installer program on each of your two worker nodes, using the IP address of your master node.

    ```
    cumulus@<server>:~$ netq bootstrap worker tarball /mnt/installables/netq-bootstrap-2.4.0.tgz master-ip <master-ip>
    ```
    
    Allow about five minutes for this to complete.

    {{%notice tip%}}
If either of these steps fail for any reason, you can run `netq bootstrap reset` on the relevant node and then try again.
    {{%/notice%}}

6. Make a note of the private IP addresses for your master and worker nodes.

### Cloud  Deployment,  Server Cluster

To prepare your NetQ server cluster:

1. Download the installer program (`netq-bootstrap-2.4.0.tgz`) and the NetQ installation tarball (`NetQ-2.4.0-opta.tgz`) from the [Cumulus Downloads](https://cumulusnetworks.com/downloads/) page.
    1. Select *NetQ* from the **Product** list box.
    2. Select *2.4* from the **Version** list box, and then select
        *2.4.0* from the submenu.
    3. Select *Bootstrap* from the **Hypervisor/Platform** list box.
    4. Scroll down to review the images that match your selection
        criteria, and click **Download** for the cloud version.
    5. Select the hypervisor you want to use (*VMware* or *KVM*) from the **Hypervisor/Platform** list box.
    6. Scroll down to review the images that match your selection
        criteria, and click **Download** for the cluster image.
2. Copy these files to the */mnt/installables/* directory on your master and worker nodes.
3. Run the installer program on your master node.

    ```
    cumulus@<hostname>:~$ netq bootstrap master interface eth0 tarball /mnt/installables/netq-bootstrap-2.4.0.tgz
    ```

    Allow about five minutes for this to complete,  and only then continue to the next step.
4. Run the installer program on your two worker nodes, using the IP address of your master node.

    ```
    cumulus@<hostname>:~$ netq bootstrap worker tarball /mnt/installables/netq-bootstrap-2.4.0.tgz master-ip <master-ip>
    ```

    Allow about five minutes for this to complete.

    {{%notice note%}}
If either of these steps fail for any reason, you can run `netq bootstrap reset` on the relevant node and then try again.
    {{%/notice%}}

5. While this is running:

    -  Locate the `config-key` provided by Cumulus Networks in an email titled *A new site has been added to your Cumulus NetQ account*. If you have lost it, submit a [support request](https://support.cumulusnetworks.com/hc/en-us/requests/new) to have it sent to you again.
    -  Make a note of the private IP addresses for your master and worker nodes.

You are now ready to use the Admin UI (preferred) or NetQ CLI to complete the installation.
