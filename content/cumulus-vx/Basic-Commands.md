---
title: Basic Commands
author: Cumulus Networks
weight: 60
product: Cumulus VX
version: '3.7'
toc: 1
---
This section shows some basic commands you can try to get started with Cumulus Linux.

## Basic Show Commands

To obtain information about a switch, run the `net show system` command:

```
cumulus@switch:~$ net show system
Cumulus VX
Cumulus Linux 3.5.0
Build: Cumulus Linux 3.5.0
Uptime: 4:29:09.270000
```

To show every available interface that is physically UP, run the `net show interface` command:

```
cumulus@switch:~$ net show interface
        Name    Master    Speed    MTU    Mode           Remote Host       Remote Port    Summary
-----  ------  --------  -------  -----  -------------  ----------------  -------------  -------------------------------------
UP     lo                N/A      65536  Loopback                                        IP: 127.0.0.1/8, 10.2.1.1/32, ::1/128
UP     eth0              1G       1500   Mgmt                                            IP: 10.0.2.15/24(DHCP)
UP     swp1              1G       1500   Interface/L3   CumulusVX-spine1  swp1           IP: 10.2.1.1/32
UP     swp2              1G       1500   Interface/L3   CumulusVX-spine2  swp1           IP: 10.2.1.1/32
UP     swp3              1G       1500   Interface/L3                                    IP: 10.4.1.1/24
ADMDN  swp4              N/A      1500   NotConfigured
ADMDN  swp5              N/A      1500   NotConfigured
ADMDN  swp6              N/A      1500   NotConfigured
ADMDN  swp7              N/A      1500   NotConfigured
```

To show topology verification, run the `net show lldp` command.

The example output below shows the two-leaf and one spine topology from Leaf01, where local port **swp1** is connected to remote port **swp1** on **Spine01**.

```
cumulus@switch:~$ net show lldp
LocalPort    Speed    Mode          RemotePort    RemoteHost        Summary
-----------  -------  ------------  ------------  ----------------  ---------------
swp1         1G       Interface/L3  swp1          CumulusVX-spine1  IP: 10.2.1.1/32
```

## Change the Hostname

To change the hostname, run the `net add hostname` command. This command updates both the `/etc/hostname` and `/etc/hosts` files.

```
cumulus@switch:~$ net add hostname <hostname>
```

## Install a Binary Image with ONIE

Cumulus VX images include the GRUB boot loader and {{<exlink url="(http://onie.org/" text="Open Network Install Environment (ONIE)">}} preinstalled. You can install Cumulus Linux on switch hardware using a binary image. You can test this process by installing a Cumulus VX binary image with ONIE in a virtual environment.

1. After booting the VM, reboot into ONIE Rescue mode using one of two methods:
   - Select ONIE Rescue mode on next reboot and reboot the VM with the `sudo onie-select -rf && sudo reboot` command.
   - Reboot and during the first 5 seconds on the GRUB menu, change the boot image to `ONIE`, then select `ONIE Rescue Mode` using the GRUB menu.

2. To install Cumulus VX, run the following command:

   ```
   cumulus@switch:~$ onie-nos-install <URL to cumulus-linux-vx-amd64.bin>
   ```

During the ONIE boot sequence, ONIE attempts to start DHCP and timeout on every configured interface. If the VM has numerous configured interfaces, this can take a while to complete.

After the installation process is complete, GRUB redirects you to the installed Cumulus VX instance.

## Related Information

- {{<exlink url="https://docs.cumulusnetworks.com/cumulus-linux-41" text="Cumulus Linux documentation">}}
- {{<exlink url="https://support.cumulusnetworks.com/hc/en-us/" text="Cumulus Networks knowledge base">}}
- {{<exlink url="https://pypi.python.org/pypi/ansible" text="Ansible 1.7 or newer">}}
