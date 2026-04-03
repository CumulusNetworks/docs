---
title: Cumulus Linux 5.17 Packages
author: Cumulus Networks
weight: -30
product: Cumulus Linux
version: "5.17"
toc: 1
pdfhidden: True
---
## 5.17 Packages

Cumulus Linux 5.17.0 contains the following core switch package versions:

| Package | Version | Description |
| --- | ----| ----------- |
| SDK (`sx-sdk-eth`) | 4.8.3972 | Switch SDK package. Legal Notices and 3rd Party Licenses: {{<exlink url="https://content.mellanox.com/Legal/3rdPartyUnifyNotice_SDK_sx_sdk_4_8_3000_4.8.3034.pdf" text="SDK 3rd Party Unify Notice">}}; {{<exlink url="https://content.mellanox.com/Legal/3rdPartyNotice_SDK_sx_sdk_4_8_3000_4.8.3034.pdf" text="SDK 3rd Party Notice">}}; {{<exlink url="https://content.mellanox.com/Legal/license_SDK_sx_sdk_4_8_3000_4.8.3034.pdf" text="SDK License">}} |
| MFT (`kernel-mft-dkms`) | 4.35.0.159 | Switch MFT package. Legal Notices and 3rd Party Licenses: {{<exlink url="https://content.mellanox.com/Legal/3rdPartyNotice_MFT_VMWARE_mft-4.34.1.pdf" text="MFT 3rd Party Notice">}}; {{<exlink url="https://content.mellanox.com/Legal/license_MFT_VMWARE_mft-4.34.1.pdf" text="MFT License">}} |
| Hardware management (`hw-management`) | 7.0060.0930 | Hardware management package|
| NVUE (`python3-nvue`) | 1.13.0.35 | NVUE core package |
| kernel (`linux-image`) | 6.1.123 | Linux kernel package |
| FRR | 10.0.3 | FRRouting package|
| Telemetry | 91.1.13.?? | Telemetry package |

To obtain a complete list of open source packages included in Cumulus Linux 5.17, see the downloads section on the {{<exlink url="https://enterprise-support.nvidia.com/s/" text="NVIDIA Enterprise support portal">}}.

<!-- The Spectrum-6 switch running Cumulus Linux 5.18 requires you to download and install the following components:

| Component | Version | Description |
| --- | ----| ----------- |
| BMC | ???? | Baseboard Management Controller |
| eRoT |???? | Embedded Root of Trust |

For package download and installation instructions, refer to {{<link url="BMC-and-eRoT" text="BMC and eRoT">}}.
-->