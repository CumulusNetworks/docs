---
title: Preparation for NetQ Appliance Upgrade
author: Cumulus Networks
weight: 133
aliases:
 - /display/NETQ/Install+NetQ
 - /pages/viewpage.action?pageId=12320951
product: Cumulus NetQ
version: 2.4
imgData: cumulus-netq
siteSlug: cumulus-netq
---
This topic describes how to prepare a NetQ 2.3.x or earlier NetQ Appliance before installing NetQ 2.4.0. The steps are the same for both the on-premises and cloud appliances. The only difference is the software you download for each platform. On completion of the steps included here, you will be ready to perform a fresh installation of NetQ 2.4.0.

To prepare your appliance:

1. Log in to your appliance.

2. Verify that your appliance is one of the following:
    - NetQ Appliance: SuperMicro SYS-6019P-WTR ([user manual](https://www.supermicro.com/manuals/superserver/1U/MNL-1943.pdf), [quick reference guide](https://www.supermicro.com/QuickRefs/superserver/1U/QRG-1943.pdf))
    - NetQ Cloud Appliance: SuperMicro SYS-E300-9D ([user manual](https://www.supermicro.com/manuals/superserver/mini-itx/MNL-2094.pdf))

3. Remove/uninstall xxx software  ???

4. Install Ubuntu 18.04 LTS. Use the instructions [here](https://www.fosslinux.com/6406/how-to-install-ubuntu-server-18-04-lts.htm).

    Note these tips:
    - Ignore the instructions for MAAS.
    - Ubuntu OS should be installed on the SSD disk. Select Micron SSD with ~900 GB at step#9 in the aforementioned instructions.
        {{<figure src="/images/netq/install-ubuntu-ssd-selection-240.png" width="700">}}
    - Set the default username to *cumulus* and password to *CumulusLinux!* while installing Ubuntu 18.04.
        {{<figure src="/images/netq/install-ubuntu-set-creds-240.png" width="700">}}
    - When prompted, select *Install SSH server*.

5. Configure Netplan. 
    Ubuntu uses Netplan for network configuration. You can give your appliance an IP address using DHCP or a static address. 
    
    To configure an IP address allocation using DHCP:

    - Create and/or edit the  */etc/netplan/01-ethernet.yaml* Netplan configuration file.

```
# This file describes the network interfaces available on your system
...
# For more information, see netplan(5).
network:
    version: 2
    renderer: networkd
    ethernets:
        eno1:
            dhcp4: yes
... 
```

    - Apply the settings.

```
$ sudo netplan apply
```

    To configure a static IP address:

    - Create and/or edit the  */etc/netplan/01-ethernet.yaml* Netplan configuration file.

```
# This file describes the network interfaces available on your system
...
# For more information, see netplan(5).
network:
    version: 2
    renderer: networkd
    ethernets:
        eno1:
            dhcp4: no
            addresses: [192.168.1.222/24]
            gateway4: 192.168.1.1
            nameservers:
                addresses: [8.8.8.8,8.8.4.4
...
```

        In this example the interface, eno1, is given a static IP address of 192.168.1.222 with a gateway at 192.168.1.1 and DNS server at 8.8.8.8 and 8.8.4.4.

    - Apply the settings.
        
```
$ sudo netplan apply
```

6. Retrieve the Ubuntu repository. The instructions are the same for either appliance.

    1. Reference and update the local apt repository.

        ```
        root@ubuntu:~# wget -O- https://apps3.cumulusnetworks.com/setup/cumulus-apps-deb.pubkey | apt-key add -
        ```

    2. Add the Ubuntu repository, by creating the file */etc/apt/sources.list.d/cumulus-host-ubuntu-bionic.list* and adding the following line:

        ```
        root@ubuntu:~# vi /etc/apt/sources.list.d/cumulus-apps-deb-bionic.list
        ...
        deb [arch=amd64] https://apps3.cumulusnetworks.com/repos/deb bionic netq-latest
        ...
        ```
7. Install Python.

    ```
    root@ubuntu:~# apt-get update
    root@ubuntu:~# apt-get install python python-2.7 python-apt
    ```

8. Obtain the latest NetQ Agent and CLI package.

    ```
    root@ubuntu:~# apt-get update
    root@ubuntu:~# apt-get install cumulus-netq
    ```

9. Download the installer program and the NetQ installation tarball from the [Cumulus Downloads](https://cumulusnetworks.com/downloads/) page.

    1. Select *NetQ* from the **Product** list.

    2. Select *2.4* from the **Version** list, and then select *2.4.0* from the submenu.

    3. Select *Bootstrap* from the **Platform/Appliance** list. 
        Note that the bootstrap file is the same for both appliances.

    4. Scroll down and click **Download**.

    5. Select *Appliance* for the NetQ Appliance or *Appliance (Cloud)* for the NetQ Cloud Appliance from the **Platform/Appliance** list.

        Make sure you select the right install choice based on whether you are preparing the on-premises or cloud version of the appliance.

    6. Scroll down and click **Download**.

    7. Copy these two files to the */mnt/installables/* directory on the appliance.

    8. Run the following commands.

        ```
        sudo systemctl disable apt-{daily,daily-upgrade}.{service,timer}
        sudo systemctl stop apt-{daily,daily-upgrade}.{service,timer}
        sudo systemctl disable motd-news.{service,timer}
        sudo systemctl stop motd-news.{service,timer}
        ```
10. Run the installer program on your appliance.

    ```
    cumulus@<appliance-name>:~$ netq bootstrap master interface eth0 tarball /mnt/installables/netq-bootstrap-2.4.0.tgz
    ```

    Allow about five minutes for this to complete.

{{%notice note%}}
If you are creating a server cluster, you need to prepare each of those appliances as well. Repeat these steps if you are using a previously deployed appliance or refer to [Prepare Your Cumulus NetQ Appliance](../../Install-NetQ/Prepare-NetQ-Onprem/) for a new appliance.
{{%/notice%}}

You are now ready to install the NetQ Software. Refer to [Install NetQ Using the AdminUI](../../Install-NetQ/Install-NetQ-Using-AdminUI/).