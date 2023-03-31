---
title: Deployment Guide
author: NVIDIA
weight: 1000
toc: 3

---

## System Requirements and Installation

Follow the installation instructions for the NetQ on-premises deployment with a server cluster arrangement. This arrangement requires 3 worker nodes. Each node requires the following:

{{<netq-install/vm-reqs deployment="onprem" hypervisor="kvm" version="4.2.0">}}

After ensuring you have the minimum system resource requirements, follow the installation instructions for either a {{<link title="Set Up Your KVM Virtual Machine for an On-premises Server Cluster" text="KVM hypervisor">}} or {{<link title="Set Up Your VMware Virtual Machine for an On-premises Server Cluster" text="VMware hypervisor">}}.

After you complete the installation, log in to NetQ and {{<link title="Access the NVLink4 UI" text="follow the steps to access NVLink4 features">}} via the UI.