---
title: Frequently Asked Questions
author: NVIDIA
weight: 50
product: Cumulus VX
version: '5.x'
---

<!-- vale off -->
### From where do I download Cumulus VX images?
<!-- vale on -->

Cumulus VX is available as a free download on the {{<exlink url="https://www.nvidia.com/en-us/networking/ethernet-switching/cumulus-vx/download/" text="NVIDIA Networking portal">}}. You must create an account and log in to download a Cumulus VX image. Images are available for all supported hypervisors.

### Which Hypervisors does Cumulus VX support?

For a list of the supported hypervisors and orchestrators, see {{<link url="Overview#supported-hypervisors" text="supported hypervisors">}}.

### What is the support policy for Cumulus VX?

The support policy for Cumulus VX depends on whether you are a customer or non-customer. See {{<link url="Overview#support-policy" text="Support Policy">}}.

### What is the difference between Cumulus VX and Cumulus Linux?

The intent of Cumulus VX is for simulation, testing, and training. Cumulus Linux is the software running directly on NVIDIA switches. Cumulus VX is not a production-ready virtual switch or router. See {{<link url="Overview#Cumulus-vx-compared-with-cumulus-linux" text="Cumulus VX Compared with Cumulus Linux">}}.

### What is the difference between Cumulus VX and Cumulus AIR?

Cumulus VX is a free virtual appliance with the Cumulus Linux operating system. You can install Cumulus VX on a supported hypervisor and configure the VMs with the reference topology or create your own topology. {{<exlink url="https://www.nvidia.com/en-us/networking/ethernet-switching/air/" text="NVIDIA Air">}} is a cloud hosted, network simulation platform that behaves exactly like a real world production environment. You use NVIDIA Air to create a digital twin of your IT infrastructure.

<!-- vale off -->
### I have platform and disk limitations for Cumulus VX, how do I try Cumulus Linux?
<!-- vale on -->

Try {{<exlink url="https://www.nvidia.com/en-us/networking/ethernet-switching/air/" text="NVIDIA Air">}}, which is a free, personal, virtual data center network that provides a low-effort way to see NVIDIA Networking technology in action. This is a good way to try out Cumulus Linux if you have platform or disk limitations.

<!-- vale off -->
### How do I log in to the Cumulus VX switches?
<!-- vale on -->

- For Cumulus VX 4.1.1 and earlier, log in to each switch with the `cumulus` account and default password `CumulusLinux!`. You are **not** prompted to change the default password.
- For Cumulus VX 4.2 and later, log in to each switch with the `cumulus` account and default password `cumulus`. When you log in for the first time, the OS prompts you to change the default password.

For more information on the required password change, see the {{<exlink url="https://docs.nvidia.com/networking-ethernet-software/cumulus-linux/Quick-Start-Guide/" text="Cumulus Linux documentation">}}.

<!-- vale off -->
### Why do I see the failure: Unable to find storage device for file system with label *ONIE-BOOT*?
<!-- vale on -->

In VMware vSphere, you might see this failure if you select the wrong storage interface type (SATA or IDE). For example this log message indicates vSphere cannot find the filesystem.

```
Info: Fetching http://192.168.100.1/onie-installer-cumulus_vx ...
ONIE: Executing installer: http://192.168.100.1/onie-installer-cumulus_vx
Verifying image checksum ...OK.
Preparing image archive ... OK.
Verifying image compatibility ...OK.
Verifying system ram ...OK.
Setting up installer ...Failure: Unable to find storage device for file system with label 'ONIE-BOOT'
Info: Check the output of 'blkid'.
```

Configure VMware vSphere to use the SATA controller.

<!-- vale off -->
### Why do I see the error br0: received package on swp1 with own address as source address?
<!-- vale on -->

If you intend to bridge the switch ports in the VM, place each switch port in the bridge in its own virtual network on the host. Otherwise, you might see this error:

```
br0: received package on swp1 with own address as source address
```

<!-- vale off -->
### How do I redirect the GRUB menu and the kernel output to the serial console?
<!-- vale on -->

To provide easier access in video-focused hypervisors (such as VirtualBox), the default Cumulus VX configuration redirects the GRUB menu and the kernel output to the video console.

Follow these steps to send both the GRUB menu and the kernel output back to the serial console.

{{< tabs "TabID01 ">}}

{{< tab "If the VM did not boot ">}}

1. Interrupt the boot process at the GRUB prompt.
2. Modify the Linux command line directly, removing all references to the console entries.
3. Start the VM.

{{< /tab >}}

{{< tab "If the VM is already running ">}}

1. Run the following commands as the sudo user:

   ```
   cumulus@switch:~$ sudo sed -i 's/^#//' /etc/default/grub.d/00-installer-defaults.cfg
   cumulus@switch:~$ sudo sed -r -i '/^GRUB_CMDLINE_LINUX=/ s/(console=ttyS0,115200n8) (console=tty0)/\2 \1/' /etc/default/grub
   cumulus@switch:~$ sudo update-grub
   ```

2. Restart the VM.

{{< /tab >}}

{{< /tabs >}}

<!-- vale off -->
### Why do I see a the error: net could not connect to netd when I try to run NCLU commands?
<!-- vale on -->

Based on the underlying CPU resources, it might take some time for the NCLU service to start after you boot the switch. If you issue an NCLU command before the NCLU service starts, you see the message:

```
ERROR: net could not connect to netd
```

Either wait a bit longer for the NCLU service to start or run the command `sudo sytemctl start netd`.

{{%notice note%}}
If you start Cumulus VX with less than the required 768MB of RAM, the NCLU service might fail to start.
{{%/notice%}}

<!-- vale off -->
### When using VirtualBox or VirtualBox with Vagrant, why is the bond I create down?
<!-- vale on -->

With VirtualBox or VirtualBox with Vagrant, when you create a bond, make sure to set *promiscuous mode* to `on` for each interface:

1. For VirtualBox, make sure to set all adapters (except Adapter 1) to **Promiscuous Mode: Allow All** under network settings in the VirtualBox Manager. See {{<link url="VirtualBox#create-network-connections" text="VirtualBox">}}.

   For VirtualBox and Vagrant, make sure the `Vagrantfile` contains the promiscuous mode setting for all interfaces. See the example Vagrantfile in {{<link url="VirtualBox-and-Vagrant#create-vms-and-network-connections" text="VirtualBox and Vagrant">}}.
3. On each switch, set promiscuous mode for all interfaces in the `/etc/network/interface` file. For example:

   ```
   auto swp2
   iface swp2
       #required for traffic to flow on Bonds in Vbox VMs
       post-up ip link set $IFACE promisc on

   auto swp3
   iface swp3
       #required for traffic to flow on Bonds in Vbox VMs
       post-up ip link set $IFACE promisc on
   ```

### Cumulus VX does not boot on Nutanix AHV

When using Nutanix AHV as a hypervisor, during the boot process of Cumulus VX, you see the following error:

```
 Gave up waiting for root file system device. Common problems:
  - Boot args (cat /proc/cmdline)b302-e5056ce95126
     - Check rootdelay= (did the system wait long enough?)
  - Missing modules (cat /proc/modules; ls /dev)
ALERT! UUID=92d167d9-116d-4290-8552-5ce3c50bd4a8 does not exist. Dropping to a shell!

BusyBox v1.30.1 (Debian 1:1.30.1-4) built-in shell (ash)
Enter 'help' for a list of built-in commands.

(initramfs)
```

Using the AHV default `SCSI` disk type instead of `SATA` causes this issue. Change the disk type under the VM details to SATA and restart the Cumulus VX VM.
