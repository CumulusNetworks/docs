---
title: Cumulus Linux in a Virtual Environment
author: NVIDIA
weight: 1600
toc: 2
---
You can run Cumulus Linux in a virtual environment to create a digital twin of your IT infrastructure and validate configurations, features, and automation code.

- Install Cumulus VX on a supported hypervisor to configure VMs with the reference topology or create your own topology with the topology converter. After you successfully install and configure the VMs, you can run Cumulus Linux configuration commands. See [NVIDIA Cumulus VX]({{<ref "/cumulus-vx" >}}).
- Run a simulation in NVIDIA Air; a cloud hosted platform that is accessible to anyone and works exactly like a real world production deployment. NVIDIA AIR provides pre-built demos using the reference topology. You can also build your own reference topology and configurations. See [NVIDIA AIR]({{<ref "/nvidia-air" >}}).

Virtual environments do not support the following Cumulus Linux features:
- {{<link url="Netfilter-ACLs" >}}
- {{<link url="Smart-System-Manager" >}}
- {{<link url="Precision-Time-Protocol-PTP" >}}
- {{<link url="Prescriptive-Topology-Manager-PTM" >}}
- {{<link url="Port-Security" >}}
- {{<link url="SPAN-and-ERSPAN" >}}
