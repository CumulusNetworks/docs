---
title: Next Steps
author: Cumulus Networks
weight: 60
product: Cumulus VX
version: '3.7'
toc: 1
---
This section provides some additional configuration specific to Cumulus VX and shows some basic commands you can try to get started with Cumulus Linux.

## Send Output to the Serial Console

To provide easier access in video-focused hypervisors (such as VirtualBox), Cumulus VX is configured to redirect the grub menu and the kernel output to the video console. To send both the grub menu and the kernel output back to the serial console, follow these steps:

{{< tabs "TabID01 ">}}

{{< tab "If the VM is not booted ">}}

1. Interrupt the boot process at the GRUB prompt.

2. Modify the Linux command line directly, removing all references to the console entries:

   **Original Version**:

   {{< img src = "/images/cumulus-vx/grub1.png" >}}

   **Configured Version**:

   {{< img src = "/images/cumulus-vx/grub1.png" >}}

   The example images above are for the ONIE-RESCUE entry, not the standard boot entry. The configuration process is the same for both entries.

3. Start the VM.

{{< /tab >}}

{{< tab "If the VM is already running ">}}

1. Run the following commands as the sudo user:

    ```
    cumulus@switch:~$ sed -i 's/^#//' /etc/default/grub.d/00-installer-defaults.cfg
    cumulus@switch:~$ sed -r -i '/^GRUB_CMDLINE_LINUX=/ s/(console=ttyS0,115200n8) (console=tty0)/\2 \1/' /etc/default/grub
    cumulus@switch:~$ update-grub
    ```

2. Restart the VM to implement the change.

    {{< /tab >}}

    {{< /tabs >}}

## Basic Commands

After you configure the Cumulus VX instances and perform the configuration above, use the {{<exlink url="https://docs.cumulusnetworks.com/cumulus-linux" text="Cumulus Linux documentation suite">}} to configure and test features, and fine tune the network topology.

Use the following basic commands to get started. You can run the commands on each VM to see system information and interface and LLDP details, and to change the hostname of the switch.

To obtain information about the switch, run the `net show system` command:

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

The example output below shows the two-leaf, two-spine Cumulus VX network topology from CumulusVX-leaf1, where local port **swp1** is connected to remote port **swp1** on **CumulusVX-spine1** and local port **swp2** is connected to remote port **swp1** on **CumulusVX-spine2**.

```
cumulus@switch:~$ net show lldp
LocalPort    Speed    Mode          RemotePort    RemoteHost        Summary
-----------  -------  ------------  ------------  ----------------  ---------------
swp1         1G       Interface/L3  swp1          CumulusVX-spine1  IP: 10.2.1.1/32
swp2         1G       Interface/L3  swp1          CumulusVX-spine2  IP: 10.2.1.1/32
```

To change the hostname, run the `net add hostname` command. This command updates both the `/etc/hostname` and `/etc/hosts` files.

```
cumulus@switch:~$ net add hostname <hostname>
```

## Related Information

- {{<exlink url="https://docs.cumulusnetworks.com/cumulus-linux-41" text="Cumulus Linux documentation">}}
- {{<exlink url="https://support.cumulusnetworks.com/hc/en-us/" text="Cumulus Networks knowledge base">}}


Cumulus VX images now include the GRUB boot loader and {{<exlink url="(http://onie.org/" text="Open Network Install Environment (ONIE)">}} preinstalled. You can install Cumulus Linux on switch hardware using a binary image. You can test this process by installing a Cumulus VX binary image with ONIE in a virtual environment.

{{%notice note%}}

Installation via ONIE is supported in Cumulus VX 3.x and later.

{{%/notice%}}

This section assumes that you have downloaded and installed a hypervisor, {{<exlink url="https://cumulusnetworks.com/products/cumulus-vx/download/" text="downloaded the Cumulus VX binary image" >}}, and configured the VM.

1. After booting the VM, reboot into ONIE Rescue mode using one of two methods:
   - Select ONIE Rescue mode on next reboot and reboot the VM with the `cumulus@switch:$ sudo onie-select -rf && sudo reboot` command.
   - Reboot and during the first 5 seconds on the GRUB menu, change the boot image to `ONIE`, then select `ONIE Rescue Mode` using the GRUB menu.

2. To install Cumulus VX, run the following command:

   ```
   cumulus@switch:~$ onie-nos-install <URL to cumulus-linux-vx-amd64.bin>
   ```

   Refer to {{<exlink url="https://docs.cumulusnetworks.com/cumulus-linux/Installation-Management/Installing-a-New-Cumulus-Linux-Image" text="Installing a New Cumulus Linux Image">}} or the
   {{<exlink url="https://github.com/opencomputeproject/onie/wiki/Quick-Start-Guide" text="ONIE Quick Start Guide">}} for more specific instructions.

During the ONIE boot sequence, ONIE attempts to start DHCP and timeout on every configured interface. If the VM has numerous configured interfaces, this can take a while to complete.

After the installation process is complete, GRUB redirects you to the installed Cumulus VX instance.



Cumulus Networks provides several preconfigured demos to run with Vagrant using Ansible to configure the VMs. To run these demos, download and install {{<exlink url="https://pypi.python.org/pypi/ansible" text="Ansible 1.7 or newer">}}.