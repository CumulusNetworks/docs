---
title: Frequently Asked Questions
author: Cumulus Networks
weight: 50
---

### From where do I download Cumulus VX images?

Cumulus VX is available as a free download on the {{<exlink url="https://cumulusnetworks.com/products/cumulus-vx/download/" text="Cumulus Networks website">}}. You must create an account and log in to download a Cumulus VX image. Images are available for all supported hypervisors.

### Which Hypervisors does Cumulus VX support?

For a list of the supported hypervisors and orchestrators, see {{<link url="Overview" text="supported hypervisors">}}.

### What's the support policy for Cumulus VX?

The support policy for Cumulus VX depends on whether you are a customer or non-customer. See {{<link url="Overview#support-policy" text="Support Policy">}}.

### What's the difference between Cumulus VX and Cumulus Linux?

Cumulus VX is intended for simulation, testing, and training. Cumulus Linux is the software running directly on NVIDIA switches. Cumulus VX is not a production-ready virtual switch or router. See {{<link url="Overview#Cumulus-vx-compared-with-cumulus-linux" text="Cumulus VX Compared with Cumulus Linux">}}.

### I have platform and disk limitations for Cumulus VX, how do I try Cumulus Linux?

Try {{<exlink url="https://cumulusnetworks.com/products/cumulus-in-the-cloud/" text="Cumulus in the Cloud">}}, which is a free, personal, virtual data center network that provides a low-effort way to see Cumulus Networks technology in action. This is a good way to try out Cumulus Linux if you have platform or disk limitations.

### How do I log into the Cumulus VX switches?

- For Cumulus VX 4.1.1 and earlier, log into each switch with the `cumulus` account and default password `CumulusLinux!`. You are **not** prompted to change the default password.

- For Cumulus VX 4.2 and later, log into each switch with the `cumulus` account and default password `cumulus`. When you log in for the first time, you are prompted to change the default password.

<p>For more information on the required password change, see the <a href="https://docs.cumulusnetworks.com/cumulus-linux/Quick-Start-Guide/#login-credentials">Cumulus Linux documentation</a>.</p>

### Why do I see the failure: Unable to find storage device for file system with label 'ONIE-BOOT'?

In VMware vSphere, you might see this failure if the wrong storage interface type is selected (SATA or IDE). For example this log message indicates the filesystem cannot be found.

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

### Why do I see the error "br0: received package on swp1 with own address as source address"?

If you intend to bridge the switch ports in the VM, place each switch port in the bridge in its own virtual network on the host. Otherwise, you might see this error:

```
br0: received package on swp1 with own address as source address
```

### How do I redirect the grub menu and the kernel output to the serial console?

To provide easier access in video-focused hypervisors (such as VirtualBox), Cumulus VX is configured by default to redirect the grub menu and the kernel output to the video console.

Follow these steps to send both the grub menu and the kernel output back to the serial console.

{{< tabs "TabID01 ">}}

{{< tab "If the VM has not been booted ">}}

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

### Why do I see a the error "net could not connect to netd" when I try to run NCLU commands?

Based on the underlying CPU resources, it might take some time for the NCLU service to start after you boot the switch. If you issue an NCLU command before the NCLU service starts, you see the message:

```
ERROR: net could not connect to netd
```

Either wait a bit longer for the NCLU service to start or run the command `sudo sytemctl start netd`.

{{<notice note>}}

If you start Cumulus VX with less than the required 768MB of RAM, the NCLU service might fail to start.

{{</notice>}}

### When using VirtualBox, why is the bond down?

With VirtualBox and VirtualBox with Vagrant, when you create a bond (aggregate multiple network interfaces (slaves) into a single logical bonded interface), you need to make sure that *promiscuous mode* is set to `on` for each interface in the bond. You set promiscuous mode in the `/etc/network/interface` file on the switch.

The following example shows that swp2 and swp3 is configured as a bond.

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
