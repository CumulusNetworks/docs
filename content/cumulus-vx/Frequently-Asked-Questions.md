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

Cumulus VX is available as a free download on the {{<exlink url="https://www.nvidia.com/en-us/networking/ethernet-switching/cumulus-vx/download/" text="NVIDIA Networking portal">}}. You must create an account and log in to download a Cumulus VX image.

### Which Hypervisors does Cumulus VX support?

Cumulus VX supports the KVM-QEMU hypervisor only.

### What is the support policy for Cumulus VX?

The support policy for Cumulus VX depends on whether you are a customer or non-customer. See {{<link url="Overview#support-policy" text="Support Policy">}}.

### What is the difference between Cumulus VX and Cumulus Linux?

The intent of Cumulus VX is for simulation, testing, and training. Cumulus Linux is the software running directly on NVIDIA switches. Cumulus VX is not a production-ready virtual switch or router. See {{<link url="Overview#Cumulus-vx-compared-with-cumulus-linux" text="Cumulus VX Compared with Cumulus Linux">}}.

### What is the difference between Cumulus VX and Cumulus AIR?

Cumulus VX is a free virtual appliance with the Cumulus Linux operating system. You can install Cumulus VX on the KVM-QEMU hypervisor. {{<exlink url="https://www.nvidia.com/en-us/networking/ethernet-switching/air/" text="NVIDIA Air">}} is a cloud hosted, network simulation platform that behaves exactly like a real world production environment. You use NVIDIA Air to create a digital twin of your IT infrastructure.

<!-- vale off -->
### I have platform and disk limitations for Cumulus VX, how do I try Cumulus Linux?
<!-- vale on -->

Try {{<exlink url="https://www.nvidia.com/en-us/networking/ethernet-switching/air/" text="NVIDIA Air">}}, which is a free, personal, virtual data center network that provides a low-effort way to see NVIDIA Networking technology in action. This is a good way to try out Cumulus Linux if you have platform or disk limitations.

<!-- vale off -->
### How do I log in to the Cumulus VX switches?
<!-- vale on -->

- For Cumulus VX 4.1.1 and earlier, log in to each switch with the `cumulus` account and default password `CumulusLinux!`. You are **not** prompted to change the default password.
- For Cumulus VX 4.2 and later, log in to each switch with the `cumulus` account and default password `cumulus`. When you log in for the first time, the OS prompts you to change the default password.

### Why do I see the error br0: received package on swp1 with own address as source address?

If you intend to bridge the switch ports in the VM, place each switch port in the bridge in its own virtual network on the host. Otherwise, you might see this error:

```
br0: received package on swp1 with own address as source address
```
