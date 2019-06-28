---
title: Using Cumulus VX with VMware
author: Cumulus Networks
weight: 11
aliases:
 - /display/VX30/Using+Cumulus+VX+with+VMware
 - /pages/viewpage.action?pageId=5126605
pageID: 5126605
product: Cumulus VX
version: '3.0'
imgData: cumulus-vx-30
siteSlug: cumulus-vx-30
---
The Cumulus VX OVA image is compatible with these hypervisor platforms
provided by VMware:

  - VMware vSphere ESXi (type-I server hypervisor)

  - VMware Fusion (for Mac users)

  - VMware Workstation (for Windows/Linux users)

No matter which VMware hypervisor you use, you use the same Cumulus VX
OVA image. Once you [install the
hypervisor](https://my.vmware.com/web/vmware/downloads) and [download
the VMware-specific OVA
image](https://cumulusnetworks.com/cumulus-vx/download/), you will
import it into the hypervisor, then clone it a few times to create a
two-leaf/two-spine virtual network.

The resulting configuration contains four VMs:

  - Two spine VMs, which represent two spine (aggregation layer)
    switches on the network

  - Two leaf VMs, which represent two leaf (access layer) switches on
    the network

{{% imgOld 0 %}}
