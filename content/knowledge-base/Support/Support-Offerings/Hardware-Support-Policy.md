---
title: Hardware Support Policy
author: Cumulus Networks
weight: 706
toc: 4
---

Cumulus Linux is only supported when running on hardware listed on the Cumulus Linux {{<exlink url="https://cumulusnetworks.com/support/hcl/" text="hardware compatibility list (HCL)">}}. The HCL is the definitive source for supported platforms. Hardware platforms do get added to the HCL over time.

In the event that a hardware platform is removed from the HCL, it will be supported until the end of the {{<link url="Cumulus-NetQ-Release-Versioning-and-Support-Policy" text="extended support release (ESR)">}} cycle for the version when the switch was removed. For example, if we remove a switch from the HCL when Cumulus Linux 3.3.1 is the current version, Cumulus will support that switch until the end of the 3.y ESR cycle.

Cumulus Networks support may determine, in the course of problem analysis, that an issue is related to hardware. In this case, Cumulus Networks support will work with the hardware vendor to further analyze the issue and provide a solution in a timely fashion. In the course of analysis, it may be deemed necessary to RMA the system. The Cumulus Networks customer support team can assist customers with the hardware partner and the customer's channel partner to perform the RMA as appropriate. Once the hardware is replaced, Cumulus Networks support will work with the customer to restore service.

## When a Manufacturer Stops Selling a Switch

In the event that a manufacturer stops selling a switch model (End of Sale, or EoS), Cumulus Networks will continue to support that switch until the end of the {{<link url="Cumulus-NetQ-Release-Versioning-and-Support-Policy" text="extended support release (ESR)">}} cycle for the version when the EoS was announced. For example, if a manufacturer stops selling a switch when Cumulus Linux 3.3.1 is the current version, Cumulus will support that switch until the end of the 3.y ESR cycle.
