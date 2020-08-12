---
title: Frequently Asked Questions
author: Cumulus Networks
weight: 50
---

### From where do I download Cumulus VX images?

You can download Cumulus VX images for all supported platforms from the {{<exlink url="https://cumulusnetworks.com/products/cumulus-vx/download/" text="Cumulus VX Download">}} page.

### Which Hypervisors does Cumulus VX support?

For a list of the supported hypervisors and orchestrators, see {{<link url="Overview" text="supported platforms">}}.

### What's the support policy for Cumulus VX?

The support policy for Cumulus VX depends on whether you are a customer or non-customer. See {{<link url="Overview#support-policy" text="Support Policy">}}.

### What's the difference between Cumulus VX and Cumulus Linux?

Cumulus VX is not a production-ready virtual switch or router. See {{<link url="Overview#Cumulus-vx-compared-with-cumulus-linux" text="Cumulus VX Compared with Cumulus Linux">}}.

### How do I log into the Cumulus VX switches?

- For Cumulus VX 4.2 and later, log into each switch with the `cumulus` account and default password `cumulus`. When you log in for the first time, you are prompted to change the default password.

- For Cumulus VX 4.1.1 and earlier, log into each switch with the `cumulus` account and default password `CumulusLinux!`. You are **not** prompted to change the default password.

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

### Why do I see the error br0: received package on swp1 with own address as source address?

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

### I have platform and disk limitations for Cumulus VX, how do I try Cumulus Linux?

Try {{<exlink url="https://cumulusnetworks.com/products/cumulus-in-the-cloud/" text="Cumulus in the Cloud">}}, which is a free, personal, virtual data center network that provides a low-effort way to see Cumulus Networks technology in action. This is a good way to try out Cumulus Linux if you have platform or disk limitations.
