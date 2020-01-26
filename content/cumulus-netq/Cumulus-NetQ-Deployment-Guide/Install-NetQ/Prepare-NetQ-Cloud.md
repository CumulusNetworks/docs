---
title: Prepare for NetQ Cloud Installation
author: Cumulus Networks
weight: 80
aliases:
 - /display/NETQ/Install+NetQ
 - /pages/viewpage.action?pageId=12320951
pageID: 12320951
product: Cumulus NetQ
version: 2.4
imgData: cumulus-netq
siteSlug: cumulus-netq
toc: 4
---
This topic describes the preparation steps needed before installing  NetQ in a cloud deployment.  Refer to [Prepare for NetQ On-premises Installation](../Prepare-NetQ-Onprem/) for preparations for on-premises deployments.

There are three key steps in the preparation for cloud installation:

1. Decide whether you want to install NetQ using:
    - a virtual machine (VM) on hardware that you provide, or
    - the Cumulus NetQ Cloud Appliance.

2. Review the general requirements and, if appropriate, the VM requirements.

3. Obtain the various software components and setup the VM or appliance.

## Requirements for VMs

If you choose to deploy NetQ on your own hardware, the following *minimum* hardware and software requirements must be met for the VM to operate correctly.

### NetQ Platform HyperVisor Requirements

The NetQ Platform can be installed as a Virtual Machine (VM) using one of the following hypervisors:

- VMware ESXi™ 6.5 (OVA image) for servers running Cumulus Linux, CentOS, Ubuntu and RedHat operating systems.
- KVM/QCOW (QEMU Copy on Write) image for servers running CentOS, Ubuntu and RedHat operating systems.

### Hardware Requirements

{{%notice info%}}

A fresh server is recommended for NetQ 2.4.0 installation. Alternately, you could create a new VM.

{{%/notice%}}

The NetQ Cloud Platform requires a server with the following:

<table>
<colgroup>
<col style="width: 40%" />
<col style="width: 60%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Hardware Component</p></th>
<th><p>Minimum Requirement</p></th>
</tr>
</thead>
<tbody>
<tr class="even">
<td>Processor</td>
<td>Four (4) virtual CPUs</td>
</tr>
<tr class="odd">
<td>Memory</td>
<td>8 GB RAM</td>
</tr>
<tr class="even">
<td>Local disk storage</td>
<td>32 GB</td>
</tr>
<tr class="odd">
<td>Network interface speed</td>
<td>1 Gb NIC</td>
</tr>
</tbody>
</table>

You must also open the following ports on your NetQ Cloud Platform (or platforms if you are planning to deploy a server cluster).

For external connections:

| Port  |  Protocol | Component Access |
| ------: |  :-----: | ----- |
| 8443 |  TCP | Admin UI |
| 443 | TCP | NetQ UI |
| 31980 | TCP | NetQ Agent communication |
| 32708 | TCP | API Gateway |
| 22 | TCP | SSH |

For internal cluster communication:

| Port  |  Protocol | Component Access |
| ------: |  :-----: | ----- |
| 8080 | TCP | Admin API |
| 5000 | TCP | Docker registry |
| 8472 | UDP | Flannel port for VXLAN |
| 6443 | TCP | Kubernetes API server |
| 10250 | TCP | kubelet health probe |
| 2379 | TCP | etcd |
| 2380 | TCP | etcd |
| 7072 | TCP | Kafka JMX monitoring |
| 9092 | TCP | Kafka client |
| 7071 | TCP | Cassandra JMX monitoring |
| 7000 | TCP | Cassandra cluster communication |
| 9042 | TCP | Cassandra client |
| 7073 | TCP | Zookeeper JMX |
| 2888 | TCP | Zookeeper cluster communication |
| 3888 | TCP | Zookeeper cluster communication |
| 2181 | TCP | Zookeeper client |

{{%notice tip%}}
Port 32666 is no longer used for the NetQ UI.
{{%/notice%}}

## Prepare Your NetQ Platform with KVM Hypervisor

Follow the preparation instructions below, based on whether you intend to deploy a single server platform or a three-server cluster.

### KVM Single-Server Arrangement

To prepare your single-server NetQ Platform:

1.  **IMPORTANT**: Confirm that your server hardware meets the
    requirements identified in [Hardware Requirements](#hardware-requirements).
2.  Download the NetQ Platform image.

    1.  On the [Cumulus Downloads](https://cumulusnetworks.com/downloads/) page, select *NetQ* from the **Product** list.

    2.  Click *2.4* from the **Version** list, and then select
        *2.4.0* from the submenu.

    3.  Select *KVM (Cloud)* from the **Hypervisor/Platform** list.

        {{< figure src="/images/netq/netq-24-download-options-240b.png" width="500" >}}

    4.  Scroll down to view the image, and click **Download**.

        {{< figure src="/images/netq/netq-24-vm-dwnld-kvmcld-240.png" width="200" >}}

3.  Open your hypervisor and set up your VM.  
    You can use this example for reference or use your own hypervisor instructions. 
    
    <details><summary>KVM Example</summary>
    This example shows the VM setup process for a system with Libvirt and KVM/QEMU installed.

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

          For a Direct VM, where the VM uses a MACVLAN interface to sit on the host interface for its connectivity:

            $ virt-install --name=netq_ts --vcpus=8 --memory=65536 --os-type=linux --os-variant=debian7 --disk path=/vms/ts.qcow2,format=qcow2,bus=virtio,cache=none --network=type=direct,source=eth0,model=virtio -import --noautoconsole

          {{%notice note%}}
Replace the disk path value with the location where the QCOW2 image is to reside. Replace network model value (eth0 in the above example) with the name of the interface where the VM is connected to the external network.
          {{%/notice%}}

          Or, for a Bridged VM, where the VM attaches to a bridge which has already been setup to allow for external access:

            $ virt-install --name=netq_ts --vcpus=8 --memory=65536 --os-type=linux --os-variant=debian7 --disk path=/vms/ts.qcow2,format=qcow2,bus=virtio,cache=none --network=bridge=br0,model=virtio --import --noautoconsole

          {{%notice note%}}
Replace network bridge value (br0 in the above example) with the   name of the (pre-existing) bridge interface where the VM is        connected to the external network.
          {{%/notice%}}

      4.  Watch the boot process in another terminal window.

            $ virsh console netq_ts

      5.  From the Console of the VM, check to see which IP address Eth0 has obtained via DHCP, or alternatively set a static IP address by viewing the */etc/netplan/01-ethernet.yaml* Netplan configuration file:

        ```
        # This file describes the network interfaces available on your system
        # For more information, see netplan(5).
        network:
            version: 2
            renderer: networkd
            ethernets:
                eno0:
                    dhcp4: no
                    addresses: [192.168.1.222/24]
                    gateway4: 192.168.1.1
                    nameservers:
                        addresses: [8.8.8.8,8.8.4.4]
        ```

        This example show that the IP address is a static address. If this is desired, exit the file without changes. If you wanted the IP address to be determined by DHCP, edit the file as follows:

        ```
        network:
            version: 2
            renderer: networkd
            ethernets:
                eno0:
                    dhcp4: yes
        ```

        Apply the settings.

        ```
        $ sudo netplan apply
        ```

    </details>

4. Verify the platform is ready for installation. Fix any errors indicated before installing the NetQ software.

    ```
    cumulus@<hostname>:~$ sudo opta-check-cloud
    ```
    
5. Run the Bootstrap CLI on the platform for the interface you defined above (eth0 or eth1 for example). This example uses the eth0 interface.

    ```
    cumulus@<hostname>:~$ netq bootstrap master interface eth0 tarball /mnt/installables/netq-bootstrap-2.4.0.tgz
    ```

    Allow about five minutes for this to complete,  and only then continue to the next step.

    {{%notice tip%}}
If this step fails for any reason, you can run `netq bootstrap reset` and then try again.
    {{%/notice%}}

You are now ready to install the Cumulus NetQ software.  Refer to [Install NetQ Using the Admin UI](../Install-NetQ-Using-AdminUI/).

### KVM Three-Server Cluster

To prepare the NetQ Platform using a three-server cluster:

1. Copy the file you downloaded for the single server to the other two servers.

2. On each additional server, open your hypervisor and setup the VM in the same manner as for the single server.

    {{%notice note%}}
Make a note of the private IP addresses you assign to the master and two worker nodes. They are needed for the installation steps.
    {{%/notice%}}

3. Verify the platform is ready for installation. Fix any errors indicated before installing the NetQ software.

    ```
    cumulus@<hostname>:~$ sudo opta-check-cloud
    ```

4. Run the Bootstrap CLI on each worker node for the interface you defined above (eth0 or eth1 for example). This example uses the eth0 interface.

    ```
    cumulus@<hostname>:~$ netq bootstrap worker interface eth0 tarball /mnt/installables/netq-bootstrap-2.4.0.tgz
    ```

    Allow about five minutes for this to complete,  and only then continue to the next step.

    {{%notice tip%}}
If this step fails for any reason, you can run `netq bootstrap reset` and then try again.
    {{%/notice%}}

You are now ready to install the Cumulus NetQ software.  Refer to [Install NetQ Using the Admin UI](../Install-NetQ-Using-AdminUI/).

## Prepare Your NetQ Platform with VMware Hypervisor

Follow the preparation instructions below, based on whether you intend to deploy a single server platform or a three-server cluster.

### VMware Single-Server Arrangement

To prepare your single-server NetQ Platform:

1.  **IMPORTANT**: Confirm that your server hardware meets the
    requirements identified in [Hardware Requirements](#hardware-requirements).
2.  Download the NetQ Platform image.

    1.  On the [Cumulus Downloads](https://cumulusnetworks.com/downloads/) page, select *NetQ* from the **Product** list.

    2.  Click *2.4* from the **Version** list, and then select
        *2.4.0* from the submenu.

    3.  Select *VMware (Cloud)* from the **Hypervisor/Platform** list.

        {{< figure src="/images/netq/netq-24-download-options-240b.png" width="500" >}}

    4.  Scroll down to view the image, and click **Download**.

        {{< figure src="/images/netq/netq-24-vm-dwnld-vmwarecld-240.png" width="200" >}}

3.  Open your hypervisor and set up your VM.  
    You can use this examples for reference or use your own hypervisor instructions. 
    
    <details><summary>VMware Example</summary>
    This example shows the VM setup process using an OVA file with VMware ESXi.

      1. Enter the address of the hardware in your browser.

      2. Log in to VMware using credentials with root access.  

          {{< figure src="/images/netq/vmw-main-page.png" width="700" >}}

      3. Click **Storage** in the Navigator to verify you have an SSD installed.  

          {{< figure src="/images/netq/vmw-verify-storage.png" width="700" >}}

      4. Click **Create/Register VM** at the top of the right pane.

          {{< figure src="/images/netq/vmw-menu-create-register.png" width="700" >}}

      5. Select **Deploy a virtual machine from an OVF or OVA file**, and
          click **Next**.  

          {{< figure src="/images/netq/vmw-deploy-vm-from-ova.png" width="700" >}}

      6. Provide a name for the VM, for example *Cumulus NetQ*.

      7. Drag and drop the NetQ Platform image file you downloaded in Step 2 above.

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

          The progress of the request is shown in the Recent Tasks window at the bottom of the application. This may take some time, so continue with your other work until the upload finishes.

      12. Once completed, view the full details of the VM and hardware.

          {{< figure src="/images/netq/vmw-deploy-results.png" width="700" >}}

    </details>

4. Verify the platform is ready for installation. Fix any errors indicated before installing the NetQ software.

    ```
    cumulus@<hostname>:~$ sudo opta-check-cloud
    ```

5. Run the Bootstrap CLI on the platform for the interface you defined above (eth0 or eth1 for example). This example uses the eth0 interface..

    ```
    cumulus@<hostname>:~$ netq bootstrap master interface eth0 tarball /mnt/installables/netq-bootstrap-2.4.0.tgz
    ```

    Allow about five minutes for this to complete,  and only then continue to the next step.

    {{%notice tip%}}
If this step fails for any reason, you can run `netq bootstrap reset` and then try again.
    {{%/notice%}}

You are now ready to install the Cumulus NetQ software.  Refer to [Install NetQ Using the Admin UI](../Install-NetQ-Using-AdminUI/).

### VMware Three-Server Cluster

To prepare the NetQ Platform using a three-server cluster:

1. Copy the file you downloaded for the single server to the other two servers.

2. On each additional server, open your hypervisor and setup the VM in the same manner as for the single server.

    {{%notice note%}}
Make a note of the private IP addresses you assign to the master and two worker nodes. They are needed for the installation steps.
    {{%/notice%}}

3. Verify the platform is ready for installation. Fix any errors indicated before installing the NetQ software.

    ```
    cumulus@<hostname>:~$ sudo opta-check-cloud
    ```

4. Run the Bootstrap CLI on each worker node for the interface you defined above (eth0 or eth1 for example). This example uses the eth0 interface.

    ```
    cumulus@<hostname>:~$ netq bootstrap worker interface eth0 tarball /mnt/installables/netq-bootstrap-2.4.0.tgz
    ```

    Allow about five minutes for this to complete,  and only then continue to the next step.

    {{%notice tip%}}
If this step fails for any reason, you can run `netq bootstrap reset` and then try again.
    {{%/notice%}}

You are now ready to install the Cumulus NetQ software.  Refer to [Install NetQ Using the Admin UI](../Install-NetQ-Using-AdminUI/).

## Prepare Your Cumulus NetQ Cloud Appliance

Follow the preparation instructions below, based on whether you intend to deploy a single server platform or a three-server cluster.

### Single NetQ Cloud Appliance

To prepare your single NetQ Appliance:

Inside the box that was shipped to you, you'll find:

- Your Cumulus NetQ Cloud Appliance (a Supermicro SuperServer E300-9D)
- Hardware accessories, such as power cables and rack mounting gear (note that network cables and optics ship separately)
- Information regarding your order

If you're looking for hardware specifications (including LED layouts and FRUs like the power supply or fans and accessories like included cables) or safety and environmental information, check out the appliance's [user manual](https://www.supermicro.com/manuals/superserver/mini-itx/MNL-2094.pdf).

#### Install the Appliance

After you unbox the appliance:

1. Mount the appliance in the rack.
2. Connect it to power following the procedures described in your appliance's user manual.
3. Connect the Ethernet cable to the 1G management port (eth0).
4. Power on the appliance.

   {{< figure src="/images/netq/netq-appliance-port-connections.png" width="700" caption="NetQ Appliance connections">}}

If your network runs DHCP, you can configure Cumulus NetQ over the network. If DHCP is not enabled, then you configure the appliance using the console cable provided.

#### Configure the Password, Hostname and IP Address

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

1. Edit the */etc/netplan/01-ethernet.yaml* Netplan configuration file:

    ```
    # This file describes the network interfaces available on your system
    # For more information, see netplan(5).
    network:
        version: 2
        renderer: networkd
        ethernets:
            eno0:
                dhcp4: no
                addresses: [192.168.1.222/24]
                gateway4: 192.168.1.1
                nameservers:
                    addresses: [8.8.8.8,8.8.4.4]
    ```

2. Apply the settings.

```
$ sudo netplan apply
```

#### Download the NetQ Software

Now that the appliance is up and running, download the software for installation.

To download the NetQ Cloud Appliance image and installer program:

1.  On the [Cumulus Downloads](https://cumulusnetworks.com/downloads/) page, select *NetQ* from the **Product** list.

2.  Click *2.4* from the **Version** list, and then select
    *2.4.0* from the submenu.

3.  Select *Bootstrap* from the **Hypervisor/Platform** list.

    {{< figure src="/images/netq/netq-24-download-options-240b.png" width="500" >}}

4.  Scroll down and click **Download**.

    {{< figure src="/images/netq/netq-24-bootstrap-dwnld-240.png" width="200" >}}

5. Select *Appliance (Cloud)* from the **Hypervisor/Platform** list.

6. Scroll down and click **Download**.

    {{< figure src="/images/netq/netq-24-appliancecld-dwnld-240.png" width="200" >}}

7. Copy these two files, *netq-bootstrap-2.4.0.tgz* and *NetQ-2.4.0-opta.tgz*, to the */mnt/installables/* directory on the appliance.

8. Verify that the needed files are present and of the correct release.

    ```
    cumulus@<hostname>:~$ dpkg -l | grep netq
    ii  netq-agent   2.4.0-ub18.04u24~1577405296.fcf3c28 amd64   Cumulus NetQ Telemetry Agent for Ubuntu
ii  netq-apps    2.4.0-ub18.04u24~1577405296.fcf3c28 amd64   Cumulus NetQ Fabric Validation Application for Ubuntu

    cumulus@<hostname>:~$ cd /mnt/installables/
    cumulus@<hostname>:/mnt/installables$ ls
    NetQ-2.4.0-opta.tgz  netq-bootstrap-2.4.0.tgz
    ```

9. Run the following commands.

```
sudo systemctl disable apt-{daily,daily-upgrade}.{service,timer}
sudo systemctl stop apt-{daily,daily-upgrade}.{service,timer}
sudo systemctl disable motd-news.{service,timer}
sudo systemctl stop motd-news.{service,timer}
```

10. Verify the appliance is ready for installation. Fix any errors indicated before installing the NetQ software.

    ```
    cumulus@<hostname>:~$ sudo opta-check-cloud
    ```
    
11. Run the Bootstrap CLI on the appliance for the interface you defined above (eth0 or eth1 for example). This example uses the eth0 interface..

    ```
    cumulus@<hostname>:~$ netq bootstrap master interface eth0 tarball /mnt/installables/netq-bootstrap-2.4.0.tgz
    ```

    Allow about five minutes for this to complete,  and only then continue to the next step.

    {{%notice tip%}}
If this step fails for any reason, you can run `netq bootstrap reset` and then try again.
    {{%/notice%}}

You are now ready to install the Cumulus NetQ software.  Refer to [Install NetQ Using the Admin UI](../Install-NetQ-Using-AdminUI/).

### Three-Appliance Cluster

To prepare a three-appliance cluster:

1. Install the second NetQ Cloud Appliance using the same steps as a single NetQ Appliance.

2. Configure the IP address, hostname, and password using the same steps as a single NetQ Appliance.
    {{%notice note%}}
Make a note of the private IP addresses you assign to the master and two worker nodes. They are needed for the installation steps.
    {{%/notice%}}

3. Copy the *netq-bootstrap-2.4.0.tgz* and *NetQ-2.4.0-opta.tgz* files downloaded for the single NetQ Appliance to this second NetQ Appliance and verify the correct files are present.

4. Run the `systemctl` commands.

5. Verify the platform is ready for installation. Fix any errors indicated before installing the NetQ software.

    ```
    cumulus@<hostname>:~$ sudo opta-check-cloud
    ```
    
6. Run the Bootstrap CLI on the appliance for the interface you defined above (eth0 or eth1 for example). This example uses the eth0 interface.

    ```
    cumulus@<hostname>:~$ netq bootstrap worker interface eth0 tarball /mnt/installables/netq-bootstrap-2.4.0.tgz
    ```

    Allow about five minutes for this to complete,  and only then continue to the next step.

    {{%notice tip%}}
If this step fails for any reason, you can run `netq bootstrap reset` and then try again.
    {{%/notice%}}

7. Repeat these steps for the third NetQ Appliance.

You are now ready to install the Cumulus NetQ software.  Refer to [Install NetQ Using the Admin UI](../Install-NetQ-Using-AdminUI/).
