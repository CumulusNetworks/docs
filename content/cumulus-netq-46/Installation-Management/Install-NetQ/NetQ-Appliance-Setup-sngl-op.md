---
title: Install the NetQ On-premises Appliance
author: NVIDIA
weight: 229
toc: 5
bookhidden: true
---
This topic describes how to prepare your single, NetQ On-premises Appliance for installation of the NetQ Platform software.

Each system shipped to you contains:

- Your NVIDIA NetQ On-premises Appliance (a Supermicro 6019P-WTR server)
- Hardware accessories, such as power cables and rack mounting gear (note that network cables and optics ship separately)
- Information regarding your order

For more detail about hardware specifications (including LED layouts and FRUs like the power supply or fans, and accessories like included cables) or safety and environmental information, refer to the {{<exlink url="https://www.supermicro.com/manuals/superserver/1U/MNL-1943.pdf" text="user manual">}} and {{<exlink url="https://www.supermicro.com/QuickRefs/superserver/1U/QRG-1943.pdf" text="quick reference guide">}}.

#### Install the Appliance

{{<netq-install/appliance-setup deployment="onprem">}}

#### Configure the Password, Hostname, and IP Address

Change the password and specify the hostname and IP address for the appliance before installing the NetQ software.

1. Log in to the appliance using the default login credentials:

    - **Username**: cumulus
    - **Password**: cumulus

2. Change the password using the `passwd` command:

    ```
    cumulus@hostname:~$ passwd
    Changing password for cumulus.
    (current) UNIX password: cumulus
    Enter new UNIX password:
    Retype new UNIX password:
    passwd: password updated successfully
    ```

3. The default hostname for the NetQ On-premises Appliance is *netq-appliance*. Change the hostname to fit your naming conventions while meeting Internet and Kubernetes naming standards.

    Kubernetes requires that hostnames comprise a sequence of labels concatenated with dots. For example, *en.wikipedia.org* is a hostname. Each label must be from 1 to 63 characters long. The entire hostname, including the delimiting dots, has a maximum of 253 ASCII characters.

    The Internet standards (RFCs) for protocols specify that labels can  contain only the ASCII letters a through z (in lower case), the digits 0 through 9, and the hyphen-minus character ('-').

    Use the following command:

    ```
    cumulus@hostname:~$ sudo hostnamectl set-hostname NEW_HOSTNAME
    ```

4. Identify the IP address.

    The appliance contains two Ethernet ports. It uses port *eno1* for out-of-band management. This is where NetQ Agents should send the telemetry data collected from your monitored switches and hosts. By default, eno1 uses DHCPv4 to get its IP address. You can view the assigned IP address using the following command:

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

#### Verify NetQ Software and Appliance Readiness

Now that the appliance is up and running, verify that the software is available and the appliance is ready for installation.

1. Verify that the needed packages are present and of the correct release, version {{<version>}} and update 38.

    {{<netq-install/verify-pkgs version="4.6" platform="appliance">}}

2. Verify the installation images are present and of the correct release, version {{<version>}}.

    {{<netq-install/verify-image deployment="onprem" version="4.6">}}

3. Verify the appliance is ready for installation. Fix any errors indicated before installing the NetQ software.

    {{<netq-install/verify-cmd deployment="onprem">}}

4. The final step is to install and activate the NetQ software using the CLI:

{{<netq-install/install-with-cli version="4.6" deployment="onprem-single">}}

After NetQ is installed, you can {{<link title="Access the NetQ UI" text="log in to NetQ">}} from your browser.