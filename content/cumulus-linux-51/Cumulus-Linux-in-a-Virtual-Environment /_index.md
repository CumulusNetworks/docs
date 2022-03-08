---
title: Cumulus Linux in a Virtual Environment
author: NVIDIA
weight: 1600
toc: 2
---
Cumulus Linux in a virtual environment enables you to become familiar NVIDIA networking technology, learn and test Cumulus Linux in your own environment, and create a digital twin of your IT infrastructure to validate configurations, features, and automation code.

NVIDIA provides these virtual environments:
<!-- vale off -->
- **NVIDIA Air** is a cloud hosted platform that works exactly like a real world production deployment. NVIDIA AIR provides pre-built demos using the reference topology. You can also build your own reference topology and configurations. See [NVIDIA AIR]({{<ref "/nvidia-air" >}}).
<!-- vale on -->
- **Cumulus VX** is a free virtual appliance with the Cumulus Linux operating system. You can install Cumulus VX on a supported hypervisor and configure the VMs with the reference topology or create your own topology. See [NVIDIA Cumulus VX]({{<ref "/cumulus-vx" >}}).

Cumulus Linux in a virtual environment contains the same Cumulus Linux operating system as NVIDIA Ethernet switches and contains the same software features. You have the full data plane functionality through the Linux kernel, as well as layer 2 VLANs and both VXLAN bridging and VXLAN routing capabilities.

Due to hardware specific implementations, virtual environments do **not** support these Cumulus Linux features:
- {{<link url="Netfilter-ACLs" text="ACL configuration with the cl-acltool command ">}}
- {{<link url="Smart-System-Manager" >}}
- {{<link url="Precision-Time-Protocol-PTP" >}}
- {{<link url="Prescriptive-Topology-Manager-PTM" >}}
- {{<link url="Port-Security" >}}
- {{<link url="SPAN-and-ERSPAN" >}}
- {{<link url="Monitoring-System-Hardware/#sensors-command" text="Temperature and sensor outputs">}}
- {{<link url="Quality-of-Service/#mark-and-remark-traffic" text="Packet marking and remarking">}}
- {{<link url="Quality-of-Service" text="QoS buffer management and buffer monitoring">}}
- {{<link url="Quality-of-Service/#policing-and-shaping" text="QoS shaping ">}}
- {{<link title="What Just Happened (WJH)" >}}
- {{<link url="Network-Address-Translation-NAT" >}}
