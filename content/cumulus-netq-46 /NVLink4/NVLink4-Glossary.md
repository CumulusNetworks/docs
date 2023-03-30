---
title: NVLink4 Glossary
author: NVIDIA
weight: 1165
toc: 3

---

## NVLink4 Terminology and Acronyms

The following table lists terms and acronyms used throughout the NVLink4 user documentation.

|Term|Definition|
|--- |--- |
|Access NVLink|An NVLink between a GPU and an NVSwitch|
|Computer node|A server system with DGXA100 baseboard|
|FM|Fabric Manager|
|GFM|Global Fabric Manager. There is one GFM per NVLink domain (cluster).|
|L1 NVSwitch|First-level NVSwitch. For example, the NVSwitches on compute nodes.|
|L2 NVSwitch|Second-level NVSwitch. The NVSwitches in the NVLink Rack Switch are L2.|
|LFM|Local Fabric Manager. Runs on each compute node to manage NVSwitches. Only the GFM directly communicates with LFMs.|
|NVLink domain/cluster|A set of nodes that can communicate over NVLink|
|NVOS|NVIDIA Networking OS, formerly known as MLNX-OS|
|OSFP Port/NVLink|Octal Small Form Factor Pluggable based NVLink ports attached to NVIDIA GPU baseboard|
|Rack switch node|A rack switch with 2 NVSwitch devices with multiple OSFP ports|
|Trunk NVLink|An NVLink between 2 NVSwitch devices|

For more information, refer to the {{<exlink url="https://docs.nvidia.com/datacenter/tesla/pdf/fabric-manager-user-guide.pdf" text="Fabric Manager User Guide">}}.