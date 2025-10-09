---
title: Install a NetQ Cloud Appliance Cluster
author: Cumulus Networks
weight: 83
toc: 5
bookhidden: true
---
This topic describes how to prepare your cluster of NetQ Cloud Appliances for installation of the NetQ Collector software.

Inside each box that was shipped to you, you'll find:

- A Cumulus NetQ Cloud Appliance (a Supermicro SuperServer E300-9D)
- Hardware accessories, such as power cables and rack mounting gear (note that network cables and optics ship separately)
- Information regarding your order

For more detail about hardware specifications (including LED layouts and FRUs like the power supply or fans and accessories like included cables) or safety and environmental information, refer to the {{<exlink url="https://www.supermicro.com/manuals/superserver/mini-itx/MNL-2094.pdf" text="user manual">}}.

#### Install Each Appliance

{{<netq-install/appliance-setup deployment="cloud">}}

#### Configure the Password, Hostname and IP Address

Change the password and specify the hostname and IP address for each appliance before installing the NetQ software.

1. Log in to the appliance that will be your master node using the default login credentials:

    - **Username**: cumulus
    - **Password**: CumulusLinux!

2. Change the password using the `passwd` command:

    ```
    cumulus@hostname:~$ passwd
    Changing password for <user>.
    (current) UNIX password:
    Enter new UNIX password:
    Retype new UNIX password:
    passwd: password updated successfully
    ```

3. The default hostname for the NetQ Cloud Appliance is *netq-appliance*. Change the hostname to fit your naming conventions while meeting Internet and Kubernetes naming standards.

    Kubernetes requires that hostnames are composed of a sequence of labels concatenated with dots. For example, “en.wikipedia.org” is a hostname. Each label must be from 1 to 63 characters long. The entire hostname, including the delimiting dots, has a maximum of 253 ASCII characters.

    The Internet standards (RFCs) for protocols specify that labels may contain only the ASCII letters a through z (in lower case), the digits 0 through 9, and the hyphen-minus character ('-').

    Use the following command:

    ```
    cumulus@hostname:~$ sudo hostnamectl set-hostname NEW_HOSTNAME
    ```

4. Identify the IP address.

    The appliance contains two Ethernet ports. Port *eno1*, is dedicated for out-of-band management. This is where NetQ Agents should send the telemetry data collected from your monitored switches and hosts. By default, eno1 uses DHCPv4 to get its IP address. You can view the assigned IP address using the following command:

    ```
    cumulus@hostname:~$ ip -4 -brief addr show eno1
    eno1             UP             10.20.16.248/24
    ```

    Alternately, you can configure the interface with a static IP address by editing the */etc/netplan/01-ethernet.yaml* Ubuntu Netplan configuration file.

    For example, to set your network interface *eno1* to a static IP address of *192.168.1.222* with gateway *192.168.1.1* and DNS server as *8.8.8.8* and *8.8.4.4*:

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

    Apply the settings.

    ```
    cumulus@hostname:~$ sudo netplan apply
    ```

5. Repeat these steps for each of the worker node appliances.

#### Verify NetQ Software and Appliance Readiness

Now that the appliances are up and running, verify that the software is available and each appliance is ready for installation.

1. On the master NetQ Cloud Appliance, verify that the needed packages are present and of the correct release, version 3.1.0 and update 28 or later.

    {{<netq-install/verify-pkgs version="3.1.0" platform="appliance">}}

2. Verify the installation images are present and of the correct release, version 3.1.0.

    {{<netq-install/verify-image deployment="cloud" version="3.1.0">}}

3. Verify the master NetQ Cloud Appliance is ready for installation. Fix any errors indicated before installing the NetQ software.

    {{<netq-install/verify-cmd deployment="cloud">}}

4. Run the Bootstrap CLI. Be sure to replace the *eno1* interface used in this example with the interface or IP address on the appliance used to listen for NetQ Agents.

    {{<netq-install/bootstrap server="single" version="3.1.0" platform="appliance" deployment="cloud">}}

5. On one of your worker NetQ Cloud Appliances, verify that the needed packages are present and of the correct release, version 3.1.0 and update 28 or later.

    {{<netq-install/verify-pkgs version="3.1.0" platform="appliance">}}

6. Configure the IP address, hostname, and password using the same steps as as for the master node. Refer to {{<link url="#configure-the-password-hostname-and-ip-address" text="Configure the Password, Hostname, and IP Address">}}.

    {{<notice note>}}
Make a note of the private IP addresses you assign to the master and worker nodes. They are needed for later installation steps.
    {{</notice>}}

7. Verify that the needed packages are present and of the correct release, version 3.1.0 and update 28 or later.

    {{<netq-install/verify-pkgs version="3.1.0" platform="appliance">}}

8. Verify that the needed files are present and of the correct release.

    {{<netq-install/verify-image deployment="cloud" version="3.1.0">}}

9. Verify the appliance is ready for installation. Fix any errors indicated before installing the NetQ software.

    {{<netq-install/verify-cmd deployment="cloud">}}

10. Run the Bootstrap CLI on the worker node.

    {{<netq-install/bootstrap server="cluster" version="3.1.0" deployment="cloud" platform="appliance">}}

11. Repeat Steps 5-10 for each additional worker NetQ Cloud Appliance.

The final step is to install and activate the Cumulus NetQ software on each appliance in your cluster.  You can do this using the Admin UI or the CLI.

Click the installation and activation method you want to use to complete installation:

- {{<link title="Install NetQ Using the Admin UI" text="Use the Admin UI">}} (recommended)
- {{<link title="Install NetQ Using the CLI" text="Use the CLI">}}