---
title: Install the NetQ Appliance Cluster
author: Cumulus Networks
weight: 82
toc: 5
bookhidden: true
---
To prepare your on-premises NetQ Appliances:

Inside each box that was shipped to you, you'll find:

- A Cumulus NetQ Appliance (a Supermicro 6019P-WTR server)
- Hardware accessories, such as power cables and rack mounting gear (note that network cables and optics ship separately)
- Information regarding your order

For more detail about hardware specifications (including LED layouts and FRUs like the power supply or fans, and accessories like included cables) or safety and environmental information, refer to the {{<exlink url="https://www.supermicro.com/manuals/superserver/1U/MNL-1943.pdf" text="user manual">}} and {{<exlink url="https://www.supermicro.com/QuickRefs/superserver/1U/QRG-1943.pdf" text="quick reference guide">}}.

#### Install Each Appliance

{{<netq-install/appliance-setup deployment="onprem">}}

#### Configure the Password, Hostname and IP Address

For each appliance, change the password using the `passwd` command:

```
cumulus@hostname:~$ passwd
Changing password for <user>.
(current) UNIX password:
Enter new UNIX password:
Retype new UNIX password:
passwd: password updated successfully
```

By default, DHCP is used to acquire the hostname and IP address. However, you can manually specify the hostname with the following command:

```
cumulus@hostname:~$ sudo hostnamectl set-hostname <newHostNameHere>
```

You can also configure these items using the Ubuntu Netplan configuration tool. For example, to set your network interface *eth0* to a static IP address of *192.168.1.222* with gateway *192.168.1.1* and DNS server as *8.8.8.8* and *8.8.4.4*:

Edit the */etc/netplan/01-ethernet.yaml* Netplan configuration file.

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

Apply the settings.

```
cumulus@hostname:~$ sudo netplan apply
```

{{%notice info%}}
If you have changed the IP address or hostname of the NetQ Appliance, you need to re-register this address with NetQ.

1. Reset the appliance, indicating whether you want to purge any NetQ DB data or keep it.

    ```
    cumulus@hostname:~$ netq bootstrap reset [purge-db|keep-db]
    ```

2. Run the Bootstrap CLI on the appliance. This example uses interface *eth0*. Replace this with your updated IP address, hostname or interface using the `interface <text-opta-ifname>` or `ip-addr <text-ip-addr>` option.

    {{<netq-install/bootstrap server="single" version="2.4.1">}}

{{%/notice%}}

#### Verify NetQ Software and Appliance Readiness

Now that the appliances are up and running, verify that the software is available and each appliance is ready for installation.

1. On the master node, verify that the needed packages are present and of the correct release, version 2.4.1 and update 26 or later.

    {{<netq-install/verify-pkgs version="2.4.1">}}

2. Verify the installation images are present and of the correct release, version 2.4.1.

    {{<netq-install/verify-image deployment="onprem" version="2.4.1">}}

3. Run the following commands to prevent daily upgrades and Message of the Day news.

    ```
    cumulus@hostname:~$ sudo systemctl disable apt-{daily,daily-upgrade}.{service,timer}
    cumulus@hostname:~$ sudo systemctl stop apt-{daily,daily-upgrade}.{service,timer}
    cumulus@hostname:~$ sudo systemctl disable motd-news.{service,timer}
    cumulus@hostname:~$ sudo systemctl stop motd-news.{service,timer}
    ```

4. Verify the master node is ready for installation. Fix any errors indicated before installing the NetQ software.

    {{<netq-install/verify-cmd deployment="onprem">}}

5. Run the Bootstrap CLI. Be sure to replace the *eth0* interface used in this example with the interface on the server used to listen for NetQ Agents.

    {{<netq-install/bootstrap server="single" version="2.4.1">}}

6. On your first worker node, verify that the needed packages are present and of the correct release, version 2.4.1 and update 26 or later.

    {{<netq-install/verify-pkgs version="2.4.1">}}

7. Configure the IP address, hostname, and password using the same steps as as for the master node. Refer to {{<link title="#NetQ-Appliance-Setup-clstr-op" text="Configure the Password, Hostname and IP Address">}}.
    {{<notice note>}}
Make a note of the private IP addresses you assign to the master and worker nodes. They are needed for the installation steps.
    {{</notice>}}

8. Copy the *netq-bootstrap-2.4.1.tgz* and *NetQ-2.4.1.tgz* files,  downloaded for the master NetQ Appliance, to the */mnt/installables/* directory on the worker NetQ Appliance.

9. Run the following `systemctl` commands to disable automatic daily upgrades and Message of the Day news.

    ```
    cumulus@hostname:~$ sudo systemctl disable apt-{daily,daily-upgrade}.{service,timer}
    cumulus@hostname:~$ sudo systemctl stop apt-{daily,daily-upgrade}.{service,timer}
    cumulus@hostname:~$ sudo systemctl disable motd-news.{service,timer}
    cumulus@hostname:~$ sudo systemctl stop motd-news.{service,timer}
    ```

10. Verify that the needed files are present and of the correct release.

    {{<netq-install/verify-image deployment="onprem" version="2.4.1">}}

11. Verify the platform is ready for installation. Fix any errors indicated before installing the NetQ software.

    ```
    cumulus@<hostname>:~$ sudo opta-check
    ```

12. Run the Bootstrap CLI on the appliance *for the interface you defined above* (eth0 or eth1 for example). This example uses the *eth0* interface.

    {{<netq-install/bootstrap server="cluster" version="2.4.1">}}

13. Repeat Steps 6-12 for each additional worker NetQ Appliance.

The final step is to install and activate the Cumulus NetQ software.  You can do this using the Admin UI or the CLI.

Click the installation and activation method you want to use to complete installation:

- {{<link title="Install NetQ Using the Admin UI" text="Use the Admin UI">}} (recommended)
- {{<link title="Install NetQ Using the CLI" text="Use the CLI">}}