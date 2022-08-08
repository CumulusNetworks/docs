---
title: NVLink4 Glossary
author: NVIDIA
weight: 1150
toc: 3
---

## NVLink4 Terminology and Acronyms

The following table covers some basic terms and acronyms used throughout the NVLink4 user documentation.

|Term|Definition|
|--- |--- |
|FM|Fabric Manager|
|Computer node|A server system with DGXA100 baseboard|
|Rack switch node|A rack switch with 2 NVSwitch devices with multiple OSFP ports|
|NVLink domain/cluster|A set of nodes that can communicate over NVLink|
|Access NVLink|An NVLink between a GPU an NVSwitch|
|Trunk NVLink|An NVLink between 2 NVSwitch devices|
|L1 NVSwitch|First-level NVSwitch. For example, the NVSwitches on compute nodes|
|L2 NVSwitch|Second-level NVSwitch. The NVSwitches in the NVLink Rack Switch are L2|
|GFM|Global Fabric Manager. There is one GFM per NVLink domain (cluster).|
|LFM|Local Fabric Manager. Runs on each compute node to manage NVSwitches. Only the GFM directly communicates with LFMs. |
|OSFP Port/NVLink|Octal Small Form Factor Pluggable based NVLink ports attached to NVIDIA GPU baseboard|
|NVOS|NVIDIA Networking OS, formerly known as MLNX-OS|