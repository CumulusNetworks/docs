---
title: Overview
author: NVIDIA
weight: 5
product: Cumulus VX
version: 5.x
---
This section provides an overview of Cumulus VX and lists supported hypervisors.

## Cumulus VX

Cumulus VX is a virtual appliance that helps you become familiar with NVIDIA networking technology, and provides a platform for you to prototype network operations and develop custom applications before you deploy into a production environment. Without the need for a bare metal switch or specialized hardware, Cumulus VX runs on all popular hypervisors, making traditional networking protocols such as BGP and MLAG, NVIDIA-specific technologies such as ONIE, and Prescriptive Topology Manager (PTM) available for testing and configuration.

Cumulus VX is a virtual machine (VM) on a standard x86 environment. The VM is the same Cumulus Linux operating system supported on NVIDIA ethernet switches and contains the same software features but in a VM format. Cumulus VX provides full data plane functionality through the Linux kernel, as well as layer 2 VLAN, VXLAN bridging, and VXLAN routing capabilities.

{{%notice note%}}
<!-- vale off -->
Cumulus VX is designed for testing and not data plane performance. Cumulus VX is not intended to act as a cloud virtual router. No testing or integration has been done with software packet acceleration integrations like SR-IOV or DPDK.
<!-- vale on -->
{{%/notice%}}

{{< img src="/images/cumulus-vx/cumulus-vx.png" width="800" >}}

## NVIDIA AIR

As an alternative to Cumulus VX, which requires a hypervisor (or hypervisor and orchestrator), you can use
{{<exlink url="https://www.nvidia.com/en-us/networking/ethernet-switching/air/" text="NVIDIA AIR">}}, which is a free, personal, virtual data center network that provides a low-effort way to see NVIDIA networking technology in action. Your virtual data center consists of two racks with two dual-homed servers connected with a leaf-spine network. This is a good way to try out Cumulus Linux if you have platform or disk limitations.

## Supported Hypervisors

Cumulus VX works with these supported hypervisors:

- KVM-QEMU
- KVM-QEMU and Vagrant
- VirtualBox
- VirtualBox and GNS3
- VirtualBox and Vagrant
- VMware Fusion, Workstation, and vSphere ESXi

{{%notice note%}}
Cumulus VX works with VMware Fusion, Workstation, and vSphere ESXi; however, this document provides setup instructions for VMware vSphere ESXi only.
{{%/notice%}}

## Cumulus VX Compared with Cumulus Linux

The VM is the same Cumulus Linux operating system supported on NVIDIA Ethernet switches and contains all the same software features but in a VM format. Cumulus VX provides full data plane functionality through the Linux kernel, as well as layer 2 VLANs and both VXLAN bridging and VXLAN routing capabilities. Due to hardware specific implementations, Cumulus VX does not support certain features.

Cumulus VX supports all software functions like BGP, spanning-tree, and SNMP, as well as any automation tooling and third-party packages.

| Cumulus VX | Cumulus Linux |
| -----------| ------------- |
| {{< img src="/images/cumulus-vx/cumulus-vx.png" width="450" >}}| {{< img src="/images/cumulus-vx/cumulus-linux.png" width="450" >}}|

## Unsupported Features in a VX

Due to hardware specific implementations, virtual environments do **not** support certain Cumulus Linux features.

| Feature | Supported in a Virtual Environment |
| -----------------------------------------------------| ------------|
|{{<exlink url="https://docs.nvidia.com/networking-ethernet-software/cumulus-linux/System-Configuration/Netfilter-ACLs" text="ACL configuration ">}}|<font color="red">No</font> |
|{{<exlink url="https://docs.nvidia.com/networking-ethernet-software/cumulus-linux/System-Configuration/In-Service-System-Upgrade-ISSU" text="In Service System Upgrade - ISSU ">}}| <font color="red">No</font> |
|{{<exlink url="https://docs.nvidia.com/networking-ethernet-software/cumulus-linux/System-Configuration/Date-and-Time/Precision-Time-Protocol-PTP" text="Precision Time Protocol - PTP">}}| <font color="red">No</font> |
|{{<exlink url="https://docs.nvidia.com/networking-ethernet-software/cumulus-linux/Layer-1-and-Switch-Ports/Port-Security" text="Port Security">}}| <font color="red">No</font> |
|{{<exlink url="https://docs.nvidia.com/networking-ethernet-software/cumulus-linux/Monitoring-and-Troubleshooting/Network-Troubleshooting/SPAN-and-ERSPAN" text="SPAN and ERSPAN">}}| <font color="red">No</font> |
|{{<exlink url="https://docs.nvidia.com/networking-ethernet-software/cumulus-linux/Monitoring-and-Troubleshooting/Monitoring-System-Hardware/#sensors-command" text="Temperature and sensor outputs">}}| Artificial temperature and sensor outputs for simulation. You can control and test monitoring tools using these artificial sensors.|
|{{<exlink url="https://docs.nvidia.com/networking-ethernet-software/cumulus-linux/Layer-1-and-Switch-Ports/Quality-of-Service/#mark-and-remark-traffic" text="QoS Packet marking and remarking">}}| <font color="red">No</font> |
|{{<exlink url="https://docs.nvidia.com/networking-ethernet-software/cumulus-linux/Layer-1-and-Switch-Ports/Quality-of-Service" text="QoS buffer management and buffer monitoring">}}| <font color="red">No</font> |
|{{<exlink url="https://docs.nvidia.com/networking-ethernet-software/cumulus-linux/Layer-1-and-Switch-Ports/Quality-of-Service/#policing-and-shaping" text="QoS shaping ">}}| <font color="red">No</font> |
|{{<exlink url="https://docs.nvidia.com/networking-ethernet-software/cumulus-linux/Monitoring-and-Troubleshooting/Network-Troubleshooting/Mellanox-WJH" text="What Just Happened (WJH)">}}| <font color="red">No</font> |
|{{<exlink url="https://docs.nvidia.com/networking-ethernet-software/cumulus-linux/Layer-3/Network-Address-Translation-NAT" text="Network Address Translation (NAT)">}}| <font color="red">No</font> |
|{{<exlink url="https://docs.nvidia.com/networking-ethernet-software/cumulus-linux/Layer-3/Routing/Equal-Cost-Multipath-Load-Sharing-Hardware-ECMP/#adaptive-routing" text="Adaptive Routing" >}}| <font color="red">No</font> |
|{{<exlink url="https://docs.nvidia.com/networking-ethernet-software/cumulus-linux/Layer-2/Storm-Control" text="Storm control ">}}|<font color="red">No</font>|

## Support Policy

As a Cumulus Linux customer, you can receive formal NVIDIA support for Cumulus VX to:

- Test and stage network topologies before deploying to production.
- Analyze, troubleshoot, and correct issues with configurations and software bugs in Cumulus VX that might also apply to Cumulus Linux running on physical devices.
- Analyze, troubleshoot, and correct issues with Cumulus VX if behaving differently than physical devices. This does not apply in scenarios where it is not possible to emulate physical hardware with virtualization.

NVIDIA does *not* provide support for:

- Cumulus VX used in a production environment.
- Virtualization environments, including installation, setup, and configuration.
- Automation tool playbooks, including creation and troubleshooting.
- Performance or scalability issues related to network traffic running through Cumulus VX instances.

For non-customers, Cumulus VX remains a community-supported product, with no formal support obligations from NVIDIA.

## Related Information

- {{<exlink url="https://docs.nvidia.com/networking-ethernet-software/cumulus-linux" text="Cumulus Linux documentation">}}
- {{<exlink url="https://www.nvidia.com/en-us/networking/ethernet-switching/cumulus-vx/" text="Cumulus VX downloads">}}
- {{<exlink url="https://www.vmware.com/support/pubs/" text="VMware documentation">}}
- {{<exlink url="https://www.virtualbox.org/wiki/Documentation" text="VirtualBox documentation">}}
- {{<exlink url="http://www.linux-kvm.org/page/Documents" text="KVM documentation">}}
- {{<exlink url="https://www.vagrantup.com/docs" text="Vagrant documentation">}}
- {{<exlink url="https://www.gns3.com/software" text="GNS3 documentation">}}
- {{<exlink url="https://www.nvidia.com/en-us/networking/ethernet-switching/air/" text="NVIDIA AIR">}}
- {{<exlink url="https://www.nvidia.com/en-us/networking/linux-on-demand/" text="Cumulus Linux on demand">}}
