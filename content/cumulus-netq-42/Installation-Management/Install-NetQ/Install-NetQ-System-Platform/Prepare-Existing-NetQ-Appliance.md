---
title: Prepare Your Existing NetQ Appliances for a NetQ 4.2 Deployment
author: NVIDIA
weight: 235
toc: 5
---

This topic describes how to prepare a NetQ 3.3.x or earlier NetQ Appliance before installing NetQ {{<version>}}. The steps are the same for both the on-premises and cloud appliances. The only difference is the software you download for each platform. After you complete the steps included here, you are ready to perform a fresh installation of NetQ {{<version>}}.

The figure below summarizes the preparation workflow:

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

    2. Verify the backup file creation was successful.

        ```
        cumulus@<hostname>:~$ cd /opt/<backup-directory>
        cumulus@<hostname>:~/opt/<backup-directory># ls
        netq_master_snapshot_2021-01-13_07_24_50_UTC.tar.gz
        ```

3. Install Ubuntu 18.04 LTS

    Follow the instructions {{<exlink url="https://www.fosslinux.com/6406/how-to-install-ubuntu-server-18-04-lts.htm" text="here">}} to install Ubuntu.

    Note these tips when installing:

    - Ignore the instructions for MAAS.
    - You should install the Ubuntu OS on the SSD disk. Select Micron SSD with ~900 GB at step #9 in the {{<exlink url="https://www.fosslinux.com/6406/how-to-install-ubuntu-server-18-04-lts.htm" text="Ubuntu instructions">}}.

        {{<figure src="/images/netq/install-ubuntu-ssd-selection-240.png" width="700">}}

    - Set the default username to *cumulus* and password to *CumulusLinux!*.

        {{<figure src="/images/netq/install-ubuntu-set-creds-240.png" width="700">}}

    - When prompted, select *Install SSH server*.

4. Configure networking.

    Ubuntu uses Netplan for network configuration. You can give your appliance an IP address using DHCP or a static address.

    {{<tabs "TabID0" >}}
    
{{<tab "DHCP" >}}

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

{{</tab>}}

{{<tab "Static IP" >}}

- Create and/or edit the  */etc/netplan/01-ethernet.yaml* Netplan configuration file.

    In this example the interface, *eno1*, has a static IP address of *192.168.1.222* with a gateway at *192.168.1.1* and DNS server at *8.8.8.8* and *8.8.4.4*.

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

{{</tab>}}

{{</tabs>}}

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
The use of <code>netq-latest</code> in this example means that a <code>get</code> to the repository always retrieves the latest version of NetQ; this applies even for major version updates. If you want to keep the repository on a specific version &mdash; such as <code>netq-4.2</code> &mdash; use that instead.
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

8. Download NetQ installation tarball.

    1. On the {{<exlink url="http://support.mellanox.com/s/" text="My Mellanox support">}} page, log in to your account. If needed create a new account and then log in.

        {{<figure src="/images/netq/mymellanox-login-320.png" width="500">}}

        Your username is based on your Email address. For example, user1@domain.com.mlnx.

    2. Open the **Downloads** menu.

    3. Click **Software**.

    4. Open the **Cumulus Software** option.

        {{<figure src="/images/netq/mymellanox-cumulus-software-download-320.png" width="500">}}

    5. Click **All downloads** next to **NVIDIA NetQ**.

    6. Select *4.2.0* from the **NetQ Version** dropdown.

    7. Select *KVM* from the **Hypervisor** dropdown.

    8. Click **Show Download**.

        {{<figure src="/images/netq/mymellanox-netq-download-kvm-331.png" width="500">}}

    9. Verify this is the correct image, then click **Download**.

    10. Copy either *NetQ-4.2.0.tgz* (on-premises) or *NetQ-4.2.0-opta.tgz* (cloud), to the */mnt/installables/* directory on the appliance.

    11. Verify that the needed files are present and of the correct release. This example shows on-premises files. The only difference for cloud files is that it should list *NetQ-4.2.0-opta.tgz* instead of *NetQ-4.2.0.tgz*.

        ```
        cumulus@<hostname>:~$ dpkg -l | grep netq
        ii  netq-agent   4.2.0-ub18.04u38~1652817271.25f4ac0_amd64   NVIDIA NetQ Telemetry Agent for Ubuntu
        ii  netq-apps    4.2.0-ub18.04u38~1652817271.25f4ac0_amd64   NVIDIA NetQ Fabric Validation Application for Ubuntu

        cumulus@<hostname>:~$ cd /mnt/installables/
        cumulus@<hostname>:/mnt/installables$ ls
        NetQ-4.2.0.tgz
        ```

    12. Run the following commands.

        ```
        sudo systemctl disable apt-{daily,daily-upgrade}.{service,timer}
        sudo systemctl stop apt-{daily,daily-upgrade}.{service,timer}
        sudo systemctl disable motd-news.{service,timer}
        sudo systemctl stop motd-news.{service,timer}
        ```

9. You are now ready to install the NetQ Software. Refer to {{<link title="Install NetQ Using the CLI">}}.