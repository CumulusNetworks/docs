---
title: Prepare Your Existing NetQ Appliances for a NetQ 3.2 Deployment
author: Cumulus Networks
weight: 235
toc: 5
---
This topic describes how to prepare a NetQ 2.4.x or earlier NetQ Appliance before installing NetQ 3.x. The steps are the same for both the on-premises and cloud appliances. The only difference is the software you download for each platform. On completion of the steps included here, you will be ready to perform a fresh installation of NetQ 3.x.

The preparation workflow is summarized in this figure:

{{<figure src="/images/netq/install-appl-prep-workflow-300.png" width="700">}}

To prepare your appliance:

1. Verify that your appliance is a supported hardware model.

    - NetQ On-premises Appliance: SuperMicro SYS-6019P-WTR ({{<exlink url="https://www.supermicro.com/manuals/superserver/1U/MNL-1943.pdf" text="user manual">}}, {{<exlink url="https://www.supermicro.com/QuickRefs/superserver/1U/QRG-1943.pdf" text="quick reference guide">}})
    - NetQ Cloud Appliance: SuperMicro SYS-E300-9D ({{<exlink url="https://www.supermicro.com/manuals/superserver/mini-itx/MNL-2094.pdf" text="user manual">}})

2. For on-premises solutions using the NetQ On-premises Appliance, optionally back up your NetQ data.

    1. Run the backup script to create a backup file in `/opt/<backup-directory>`.

        {{<notice note>}}
    Be sure to replace the <code>backup-directory</code> option with the name of the directory you want to use for the backup file. This location must be somewhere that is <em>off</em> of the appliance to avoid it being overwritten during these preparation steps.
        {{</notice>}}

        ```
        cumulus@<hostname>:~$ ./backuprestore.sh --backup --localdir /opt/<backup-directory>
        ```

    2. Verify the backup file has been created.

        ```
        cumulus@<hostname>:~$ cd /opt/<backup-directory>
        cumulus@<hostname>:~/opt/<backup-directory># ls
        netq_master_snapshot_2020-01-09_07_24_50_UTC.tar.gz
        ```

3. Install Ubuntu 18.04 LTS

    Follow the instructions {{<exlink url="https://www.fosslinux.com/6406/how-to-install-ubuntu-server-18-04-lts.htm" text="here">}} to install Ubuntu.

    Note these tips when installing:

    - Ignore the instructions for MAAS.
    - Ubuntu OS should be installed on the SSD disk. Select Micron SSD with ~900 GB at step#9 in the aforementioned instructions.

        {{<figure src="/images/netq/install-ubuntu-ssd-selection-240.png" width="700">}}

    - Set the default username to *cumulus* and password to *CumulusLinux!*.

        {{<figure src="/images/netq/install-ubuntu-set-creds-240.png" width="700">}}

    - When prompted, select *Install SSH server*.

4. Configure networking.

    Ubuntu uses Netplan for network configuration. You can give your appliance an IP address using DHCP or a static address.

    {{< tabs "TabID0" >}}
    
{{< tab "DHCP" >}}

- Create and/or edit the  */etc/netplan/01-ethernet.yaml* Netplan configuration file.

    ```
    # This file describes the network interfaces available on your system
    # For more information, see netplan(5).
    network:
        version: 2
        renderer: networkd
        ethernets:
            eno1:
                dhcp4: yes
    ```

- Apply the settings.

    ```
    $ sudo netplan apply
    ```

{{< /tab >}}

{{< tab "Static IP" >}}

- Create and/or edit the  */etc/netplan/01-ethernet.yaml* Netplan configuration file.

    In this example the interface, *eno1*, is given a static IP address of *192.168.1.222* with a gateway at *192.168.1.1* and DNS server at *8.8.8.8* and *8.8.4.4*.

    ```
    # This file describes the network interfaces available on your system
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
                    addresses: [8.8.8.8,8.8.4.4]
    ```

- Apply the settings.

    ```
    $ sudo netplan apply
    ```

{{< /tab >}}

{{< /tabs >}}

5. Update the Ubuntu repository.

    1. Reference and update the local apt repository.

        ```
        root@ubuntu:~# wget -O- https://apps3.cumulusnetworks.com/setup/cumulus-apps-deb.pubkey | apt-key add -
        ```

    2. Add the Ubuntu 18.04 repository.

        Create the file `/etc/apt/sources.list.d/cumulus-host-ubuntu-bionic.list` and add
    the following line:

        ```
        root@ubuntu:~# vi /etc/apt/sources.list.d/cumulus-apps-deb-bionic.list
        ...
        deb [arch=amd64] https://apps3.cumulusnetworks.com/repos/deb bionic netq-latest
        ...
        ```

        {{<notice note>}}
The use of <code>netq-latest</code> in this example means that a <code>get</code> to the repository always retrieves the latest version of NetQ, even in the case where a major version update has been made. If you want to keep the repository on a specific version - such as <code>netq-3.1</code> - use that instead.
        {{</notice>}}

6. Install Python.

    Run the following commands:

    ```
    root@ubuntu:~# apt-get update
    root@ubuntu:~# apt-get install python python2.7 python-apt python3-lib2to3 python3-distutils
    ```

7. Obtain the latest NetQ Agent and CLI package.

    Run the following commands:

    ```
    root@ubuntu:~# apt-get update
    root@ubuntu:~# apt-get install netq-agent netq-apps
    ```

8. Download the bootstrap and NetQ installation tarballs.

    Download the software from the {{<exlink url="https://support.mellanox.com/s/" text="MyMellanox downloads page">}} page.

    1. Select *NetQ* from the **Product** list.

    2. Select *3.2* from the **Version** list, and then select *3.2.1* from the submenu.

        {{<figure src="/images/netq/netq-32-bootstrap-download-321.png" width="500" >}}

    3. Select *Bootstrap* from the **Hypervisor/Platform** list.
        Note that the bootstrap file is the same for both appliances.

        {{<figure src="/images/netq/netq-321-download-bootstrap.png" width="200" >}}

    4. Scroll down and click **Download**.

    5. Select *Appliance* for the NetQ On-premises Appliance or *Appliance (Cloud)* for the NetQ Cloud Appliance from the **Hypervisor/Platform** list.

        Make sure you select the right install choice based on whether you are preparing the on-premises or cloud version of the appliance.

        {{<figure src="/images/netq/netq-32-appliance-onpremcld-dwnld-321.png" width="410" >}}

    6. Scroll down and click **Download**.

    7. Copy these two files, *netq-bootstrap-3.2.1.tgz* and either *NetQ-3.2.1.tgz* (on-premises) or *NetQ-3.2.1-opta.tgz* (cloud), to the */mnt/installables/* directory on the appliance.

    8. Verify that the needed files are present and of the correct release. This example shows on-premises files. The only difference for cloud files is that it should list *NetQ-3.2.1-opta.tgz* instead of *NetQ-3.2.1.tgz*.

        ```
        cumulus@<hostname>:~$ dpkg -l | grep netq
        ii  netq-agent   3.2.1-ub18.04u31~1603789872.6f62fad_amd64   Cumulus NetQ Telemetry Agent for Ubuntu
        ii  netq-apps    3.2.1-ub18.04u31~1603789872.6f62fad_amd64   Cumulus NetQ Fabric Validation Application for Ubuntu

        cumulus@<hostname>:~$ cd /mnt/installables/
        cumulus@<hostname>:/mnt/installables$ ls
        NetQ-3.2.1.tgz  netq-bootstrap-3.2.1.tgz
        ```

    9. Run the following commands.

        ```
        sudo systemctl disable apt-{daily,daily-upgrade}.{service,timer}
        sudo systemctl stop apt-{daily,daily-upgrade}.{service,timer}
        sudo systemctl disable motd-news.{service,timer}
        sudo systemctl stop motd-news.{service,timer}
        ```

9. Run the Bootstrap CLI.

    Run the bootstrap CLI on your appliance. Be sure to replace the *eth0* interface used in this example with the interface or IP address on the appliance used to listen for NetQ Agents.

    {{<netq-install/bootstrap server="single" version="3.2.1">}}

{{<notice note>}}
If you are creating a server cluster, you need to prepare each of those appliances as well. Repeat these steps if you are using a previously deployed appliance or refer to {{<link title="Install the NetQ System">}} for a new appliance.
{{</notice>}}

You are now ready to install the NetQ Software. Refer to {{<link title="Install NetQ Using the Admin UI">}} (recommended) or {{<link title="Install NetQ Using the CLI">}}.
