---
title: Hardware Support Policy
author: NVIDIA
weight: 706
toc: 4
---

NVIDIA supports Cumulus Linux only when running on hardware listed on the Cumulus Linux {{<exlink url="www.nvidia.com/en-us/networking/ethernet-switching/hardware-compatibility-list/" text="hardware compatibility list (HCL)">}}. The HCL is the definitive source for supported platforms. NVIDIA does add hardware platforms to the HCL over time.

If NVIDIA removes a hardware platform from the HCL, NVIDIA provides support until the end of the {{<link url="Cumulus-Linux-Release-Versioning-and-Support-Policy" text="extended support release (ESR)">}} cycle for the version when it removed the switch. For example, if NVIDIA removed a switch from the HCL when Cumulus Linux 3.3.1 is the current version, NVIDIA provides support for that switch until the end of the 3.y ESR cycle.

NVIDIA support might determine, in the course of problem analysis, that an issue is hardware related. In this case, NVIDIA support works with the hardware vendor to further analyze the issue and provide a solution as quickly as possible. In the course of analysis, it might be necessary to RMA the system. The NVIDIA customer support team can assist customers with the hardware partner and the customer's channel partner to perform the RMA as appropriate. After the partner replaces the hardware, NVIDIA support works with the customer to restore service.

## When a Manufacturer Stops Selling a Switch

If a manufacturer stops selling a switch model (End of Sale, or EoS), NVIDIA provides support for that switch until the end of the {{<link url="Cumulus-Linux-Release-Versioning-and-Support-Policy" text="extended support release (ESR)">}} cycle for the version when the vendor announced the EoS. For example, if a manufacturer stops selling a switch when Cumulus Linux 3.3.1 is the current version, NVIDIA provides support that switch until the end of the 3.y ESR cycle.
