---
title: Cumulus Linux in a Virtual Environment
author: NVIDIA
weight: 1800
toc: 2
---
Cumulus Linux in a virtual environment enables you to become familiar NVIDIA networking technology, learn and test Cumulus Linux in your own environment, and create a digital twin of your IT infrastructure to validate configurations, features, and automation code.

## Virtual Environments

NVIDIA provides these virtual environments:
<!-- vale off -->
- **NVIDIA Air** is a cloud hosted platform that works exactly like a real world production deployment. NVIDIA AIR provides pre-built demos using the reference topology. You can also build your own reference topology and configurations. See {{<exlink url="https://docs.nvidia.com/networking-ethernet-software/nvidia-air/" text="NVIDIA Air User Guide">}}.
<!-- vale on -->
- **Cumulus VX** is a free virtual appliance with the Cumulus Linux operating system. You can install Cumulus VX on a supported hypervisor and configure the VMs with the reference topology or create your own topology. See {{<exlink url="https://docs.nvidia.com/networking-ethernet-software/cumulus-vx/" text="Cumulus VX">}}.

Cumulus Linux in a virtual environment contains the same Cumulus Linux operating system as NVIDIA Ethernet switches and contains the same software features. You have the full data plane functionality through the Linux kernel, as well as layer 2 VLANs and both VXLAN bridging and VXLAN routing capabilities.

## Unsupported Features in a Virtual Environment

Due to hardware specific implementations, virtual environments do **not** support certain Cumulus Linux features.

| Feature | Supported in a Virtual Environment |
| -----------------------------------------------------| ------------|
|{{<link url="Netfilter-ACLs" text="ACL configuration with the cl-acltool command ">}}|<font color="red">No</font> |
|{{<link url="In-Service-System-Upgrade-ISSU" >}}| <font color="red">No</font> |
|{{<link url="Precision-Time-Protocol-PTP" >}}| <font color="red">No</font> |
|{{<link url="Port-Security" >}}| <font color="red">No</font> |
|{{<link url="SPAN-and-ERSPAN" >}}| <font color="red">No</font> |
|{{<link url="Monitoring-System-Hardware/#sensors-command" text="Temperature and sensor outputs">}}| Artificial temperature and sensor outputs for simulation.|
|{{<link url="Quality-of-Service/#mark-and-remark-traffic" text="Packet marking and remarking">}}| <font color="red">No</font> |
|{{<link url="Quality-of-Service" text="QoS buffer management and buffer monitoring">}}| <font color="red">No</font> |
|{{<link url="Quality-of-Service/#policing-and-shaping" text="QoS shaping ">}}| <font color="red">No</font> |
|{{<link title="What Just Happened (WJH)" >}}| <font color="red">No</font> |
|{{<link url="Network-Address-Translation-NAT" >}}| <font color="red">No</font> |
|{{<link url="Equal-Cost-Multipath-Load-Sharing-Hardware-ECMP/#adaptive-routing" text="Adaptive Routing" >}}| <font color="red">No</font> |
|{{<link url="Storm-Control" text="Storm control ">}}|<font color="red">No</font>|

<!--
| Feature | In a Virtual Environment | In a Virtual Environment with Emulated ASIC |
| -----------------------------------------------------| ------------| --------------|
|{{<link url="Netfilter-ACLs" text="ACL configuration with the cl-acltool command ">}}|<font color="red">No</font> | <font color="green">yes</font>|
|{{<link url="In-Service-System-Upgrade-ISSU" >}}| <font color="red">No</font> | <font color="red">No</font> |
|{{<link url="Precision-Time-Protocol-PTP" >}}| <font color="red">No</font> | <font color="green">yes</font> |
|{{<link url="Port-Security" >}}| <font color="red">No</font> | <font color="green">yes</font> |
|{{<link url="SPAN-and-ERSPAN" >}}| <font color="red">No</font> | <font color="green">yes</font> |
|{{<link url="Monitoring-System-Hardware/#sensors-command" text="Temperature and sensor outputs">}}| <font color="red">No</font> | <font color="green">yes</font>|
|{{<link url="Quality-of-Service/#mark-and-remark-traffic" text="Packet marking and remarking">}}| <font color="red">No</font> | <font color="green">yes</font> |
|{{<link url="Quality-of-Service" text="QoS buffer management and buffer monitoring">}}| <font color="red">No</font> |<font color="red">No</font> |
|{{<link url="Quality-of-Service/#policing-and-shaping" text="QoS shaping ">}}| <font color="red">No</font> | <font color="red">No</font> |
|{{<link title="What Just Happened (WJH)" >}}| <font color="red">No</font> | <font color="green">yes</font> |
|{{<link url="Network-Address-Translation-NAT" >}}| <font color="red">No</font> | <font color="green">yes</font>|
|{{<link url="Equal-Cost-Multipath-Load-Sharing-Hardware-ECMP/#adaptive-routing" >}}| <font color="red">No</font> |
-->
