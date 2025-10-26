---
title: Install NetQ for NVLink
author: NVIDIA
weight: 250
toc: 4
---

NetQ deployment options vary, depending on whether you want to use NetQ to monitor Ethernet, NVLink, or both NVLink and Ethernet. Refer to {{<link title="Before You Install" text="Before You Install">}} for more information about the various NetQ deployments.

## System Requirements

NetQ for NVLink requires a 3-node cluster with the following system requirements. Each node in the cluster must meet the VM requirements:

| Resource | Minimum Requirements |
| :--- | :--- |
| Processor | 48 virtual CPUs |
| Memory | 512GB RAM |
| Local disk storage | 3.2TB NVMe |
| Network interface speed | 10 Gbps NIC |
| Hypervisor | KVM/QCOW (QEMU Copy on Write) image for servers running Ubuntu;<br> VMware ESXi™ 6.5 or later (OVA image) for servers running Cumulus Linux or Ubuntu 24.04 |

## Next Steps

- For new deployments, refer to {{<link title="Install the NetQ System" text="Install NetQ">}}.
- To upgrade your existing NMX-M deployment, {{<link title="NVLink Bringup" text="perform a system bringup">}}to connect to NMX-C and NMX-T.
