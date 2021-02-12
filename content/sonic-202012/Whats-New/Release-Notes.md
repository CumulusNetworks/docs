---
title: Release Notes
author: Cumulus Networks
weight: 20
product: SONiC
version: 4.0
siteSlug: sonic
---

## Release Notes Update History

| Revision | Date | Description |
| -------- | ---- | ----------- |
| Rev 7.0 | October 06, 2020 | Initial release of this Release Notes version. This version introduces Changes and New Features and Bug Fixes. |

## Overview

SONiC is an open source network operating system based on Linux that runs on switches from multiple vendors and ASICs. SONiC offers a full-suite of network functionality, like BGP and RDMA, that has been production-hardened in the data centers of some of the largest cloud-service providers. It offers teams the flexibility to create the network solutions they need while leveraging the collective strength of a large ecosystem and community.

These are the release notes for SONiC software on NVIDIA® Mellanox Spectrum® based switches.

## Changes and New Features

This section provides only a list of Changes and New Features in this version. For a list of old releases, please see Changes and New Features History.

| Feature/Change | Description |
| -------------- | ----------- |
|  | Rev. SONiC 201911_MUR5 |

### Customer-Affecting Changes

| Feature/Change | Description |
| -------------- | ----------- |
|  | Rev. SONiC 201911_MUR5 |

## SONiC General Support

###	Supported Switch Systems

This software supports the switch systems listed below.

| Part Number | System Description |
| ----------- | ------------------ |
| SN2010 | Mellanox Spectrum based 100GbE, Open Ethernet switch, 18 SFP+ and 4 QSFP28 ports, 2 AC power supplies, x86 quad core, short depth |
| SN2100 | Mellanox Spectrum based 100GbE, Open Ethernet switch, 16 QSFP28 ports, short depth, Rangeley CPU |
| SN2410 | Mellanox Spectrum based 25GbE/100GbE, Open Ethernet switch, 48 SFP28 ports, 8 QSFP28 ports, x86 dual core, short depth |
| SN2700 | Mellanox Spectrum based 100GbE, Open Ethernet switch, 32 QSFP28 ports, x86 CPU, standard depth |
| SN3420 | Mellanox Spectrum-2 based 25GbE/100GbE 1U Open Ethernet switch, 48 SFP28 ports and 12 QSFP28 ports, x86 CPU, Standard depth |
| SN3700 | Mellanox Spectrum-2 based 200GbE Open Ethernet switch, 32 QSFP56 ports, x86 CPU, standard depth |
| SN3700C | Mellanox Spectrum-2 based 100GbE Open Ethernet switch, 32 QSFP28 ports, x86 CPU, standard depth |
| SN3800 | Mellanox Spectrum-2 based 100GbE Open Ethernet switch, 64 QSFP28 ports, x86 CPU, standard depth |
| SN4600C | Mellanox Spectrum-3 based 100GbE 2U Open Ethernet Switch, 64 QSFP56 ports, 2 Power Supplies (AC), standard depth |
| SN4700 | Mellanox Spectrum-3 based 400GbE, 1U Open Ethernet switch, 32xQSFP-DD ports, x86 CPU, standard depth |

###	SONiC Versions

| Branch| Hash | Location |
| ----- | ---- | -------- |
| SONiC 201911_MUR4 | bea968bb2be64c739ed0bae7cfdcc40eccf6988b | https://github.com/Azure/sonic-buildimage/tree/201911 |

###	Package Content

This release is based on SONiC 201911_MUR3 sonic-buildimage hash. It contains the following components:

| Switch Components | Version | Additional Information |
| ----------------- | ------- | ---------------------- |
| Mellanox Spectrum-3 Firmware | 30.2008.1910 | |
| Mellanox Spectrum-2 Firmware | 29.2008.1910 | |
| Mellanox Spectrum Firmware | 13.2008.1910	| |
| SDK | 4.4.1910 | SDK API can be found at: https://github.com/Mellanox/SwitchRouterSDK-interfaces |
| SAI | 1.17.3 | Mellanox SAI implementation can be found at: https://github.com/Mellanox/SAI-Implementation/tree/sonic1910 |
| Mellanox Firmware Tools (MFT) | 4.15.0-104 | {{<exlink url="https://docs.mellanox.com/display/MFTv4150/Release+Notes" text="Release Notes">}}<br />{{<exlink url="https://docs.mellanox.com/display/MFTv4150/Introduction" text="User Manual">}} |

### Application Extensions

The following are the Mellanox Application Extensions:

| Application Extensions | Version | Additional Information |
| ---------------------- | ------- | ---------------------- |
| What-Just-Happened | what-just-happened/what-just-happened-201911_1.3.0_amd64.deb | For further information see section "What Just Happened" in the User Manual.<br />**Note:** This version is aligned with SDK v4.4.1910 as well as enabling what-just-happen integration with hardware clock. |

## Bug Fixes in this Version

This section provides only a list of bugs fixed by Mellanox only in this version. For a list of old fixes, please see Bug Fixes History.

Additional bugs reported are handled by both Mellanox and the community as part of the 201911_MUR4 release. For additional information, please refer to github.

| Item # | RM # | Issue |
| ------ | ---- | ----- |
| 1. | | **Description:**<br />**Keywords:**<br />**Discovered in Version:** SONiC 201911_MUR4<br />**Fixed in Version:** SONiC 201911_MUR5 |

## Known Issues

For the community limitations, please refer to: https://github.com/Azure/sonic-buildimage/issues.

| Item # | RM # | Issue |
| ------ | ---- | ----- |
| 1. | 2315799 | **Description:** When running the "show pfc counters" (or "ptfcstat") command, the output displays incorrect PFC counters values. Values can be shown even when no PFC frames are sent or when PFC frames are sent, and all counters are equal to "0".<br />**Workaround:** Use the SDK debug scripts in "syncd" docker container to check the PFC counters. For example: "docker exec -it syncd sx_api_port_counter_dump_all.py".<br />**Keywords:** PFC counters<br />**Discovered in Version:** SONiC 201911_MUR4 |
| 2. | 2310453 | **Description:** BGP running configuration is not reflected in the frr.conf file.<br />**Note:** As the BGP configuration is not present in the techsupport file, the user must take it separately.<br />**Workaround:** Use the "show running bgp" or the vtysh -c "show run" commands to see the BGP running configuration.<br />**Keywords:** BGP, frr.conf file<br />**Discovered in Version:** SONiC 201911_MUR4 |
| 3. | 2036710 | **Description:** A wrong MTU size is displayed in ICMP (type 3, code 4) when fragmentation is needed only for the VLAN interface.<br />**Workaround:** N/A<br />**Keywords:** MTU, VLAN, ICMP<br />**Discovered in Version:** SONiC 201911_MUR4 |
| 4. | 2299515 | **Description:** The 'config reload -y' commands do not function properly and fail sporadically.<br />**Workaround:** N/A<br />**Keywords:** SONiC config reload commands<br />**Discovered in Version:** SONiC 201911_MUR4 |
| ... | ... | ... |

## Supported Port Speeds

### Mellanox Spectrum®-3 SN4700 Supported Port Speeds

<table border=1 cellspacing=0 cellpadding=0 width="100%"
 style='width:100.0%;border-collapse:collapse;border:none'>
  <tr>
   <td rowspan=2 valign=top style='border:solid #DDDDDD 1.0pt;background:#cbd4e0;
   padding:1.5pt 1.5pt 1.0pt 1.5pt'>
   <p class=CellHeading><b>Speed [GbE]</b></p>
   </td>
   <td rowspan=2 valign=top style='border:solid #DDDDDD 1.0pt;border-left:none;
   background:#cbd4e0;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
   <p class=CellHeading><b>AutoNeg</b></p>
   </td>
   <td colspan=3 valign=top style='border:solid #DDDDDD 1.0pt;border-left:none;
   background:#cbd4e0;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
   <p class=CellHeading><b>Force</b></p>
   </td>
   <td rowspan=2 valign=top style='border:solid #DDDDDD 1.0pt;border-left:none;
   background:#cbd4e0;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
   <p class=CellHeading><b>Cable / Modules</b></p>
   </td>
   <td rowspan=2 valign=top style='border:solid #DDDDDD 1.0pt;border-left:none;
   background:#cbd4e0;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
   <p class=CellHeading><b>Cable Length [m]</b></p>
   </td>
 </tr>
 <tr>
   <td valign=top style='border-top:none;border-left:none;border-bottom:solid #DDDDDD 1.0pt;
  border-right:solid #DDDDDD 1.0pt;background:#cbd4e0;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p class=CellHeading>RS FEC</p>
  </td>
  <td valign=top style='border-top:none;border-left:none;border-bottom:solid #DDDDDD 1.0pt;
  border-right:solid #DDDDDD 1.0pt;background:#cbd4e0;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p class=CellHeading>FC FEC</p>
  </td>
  <td valign=top style='border-top:none;border-left:none;border-bottom:solid #DDDDDD 1.0pt;
  border-right:solid #DDDDDD 1.0pt;background:#cbd4e0;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p class=CellHeading>NO FEC</p>
  </td>
 </tr>
 </thead>
 <tr>
  <td rowspan=2 valign=top style='border:solid #DDDDDD 1.0pt;border-top:none;
  padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p class=MsoNormal><span style='font-size:10.0pt'>400</span></p>
  </td>
  <td rowspan=2 valign=top style='border-top:none;border-left:none;border-bottom:
  solid #DDDDDD 1.0pt;border-right:solid #DDDDDD 1.0pt;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p class=MsoNormal>&#9989;</p>
  </td>
  <td rowspan=2 valign=top style='border-top:none;border-left:none;border-bottom:
  solid #DDDDDD 1.0pt;border-right:solid #DDDDDD 1.0pt;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p class=MsoNormal>&#9989;</p>
  <p class=MsoNormal><span style='font-size:10.0pt'>&nbsp;</span></p>
  </td>
  <td rowspan=2 valign=top style='border-top:none;border-left:none;border-bottom:
  solid #DDDDDD 1.0pt;border-right:solid #DDDDDD 1.0pt;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p class=MsoNormal>&#10008;</p>
  </td>
  <td rowspan=2 valign=top style='border-top:none;border-left:none;border-bottom:
  solid #DDDDDD 1.0pt;border-right:solid #DDDDDD 1.0pt;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p class=MsoNormal>&#10008;</p>
  </td>
  <td valign=top style='border-top:none;border-left:none;border-bottom:solid #DDDDDD 1.0pt;
  border-right:solid #DDDDDD 1.0pt;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p class=MsoNormal><span style='font-size:10.0pt'>Optics</span></p>
  </td>
  <td valign=top style='border-top:none;border-left:none;border-bottom:solid #DDDDDD 1.0pt;
  border-right:solid #DDDDDD 1.0pt;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p class=MsoNormal><span style='font-size:10.0pt'>Up to 5</span></p>
  </td>
 </tr>
 <tr>
  <td valign=top style='border-top:none;border-left:none;border-bottom:solid #DDDDDD 1.0pt;
  border-right:solid #DDDDDD 1.0pt;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p class=MsoNormal><span style='font-size:10.0pt'>Copper</span></p>
  </td>
  <td valign=top style='border-top:none;border-left:none;border-bottom:solid #DDDDDD 1.0pt;
  border-right:solid #DDDDDD 1.0pt;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p class=MsoNormal><span style='font-size:10.0pt'>Up to 2.5</span></p>
  </td>
 </tr>
 <tr>
  <td rowspan=2 valign=top style='border:solid #DDDDDD 1.0pt;border-top:none;
  padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p class=MsoNormal><span style='font-size:10.0pt'>200/<br>
  100 2x/<br>
  50 1x (PAM4)</span></p>
  </td>
  <td rowspan=2 valign=top style='border-top:none;border-left:none;border-bottom:
  solid #DDDDDD 1.0pt;border-right:solid #DDDDDD 1.0pt;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p class=MsoNormal>&#9989;</p>
  <p class=MsoNormal><span style='font-size:10.0pt'>&nbsp;</span></p>
  </td>
  <td rowspan=2 valign=top style='border-top:none;border-left:none;border-bottom:
  solid #DDDDDD 1.0pt;border-right:solid #DDDDDD 1.0pt;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p class=MsoNormal>&#9989;</p>
  <p class=MsoNormal><span style='font-size:10.0pt'>&nbsp;</span></p>
  </td>
  <td rowspan=2 valign=top style='border-top:none;border-left:none;border-bottom:
  solid #DDDDDD 1.0pt;border-right:solid #DDDDDD 1.0pt;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p class=MsoNormal>&#10008;</p>
  </td>
  <td rowspan=2 valign=top style='border-top:none;border-left:none;border-bottom:
  solid #DDDDDD 1.0pt;border-right:solid #DDDDDD 1.0pt;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p class=MsoNormal>&#10008;</p>
  </td>
  <td valign=top style='border-top:none;border-left:none;border-bottom:solid #DDDDDD 1.0pt;
  border-right:solid #DDDDDD 1.0pt;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p class=MsoNormal><span style='font-size:10.0pt'>Optic</span></p>
  </td>
  <td valign=top style='border-top:none;border-left:none;border-bottom:solid #DDDDDD 1.0pt;
  border-right:solid #DDDDDD 1.0pt;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p class=MsoNormal><span style='font-size:10.0pt'>Up to 5</span></p>
  </td>
 </tr>
 <tr>
  <td valign=top style='border-top:none;border-left:none;border-bottom:solid #DDDDDD 1.0pt;
  border-right:solid #DDDDDD 1.0pt;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p class=MsoNormal><span style='font-size:10.0pt'>Copper</span></p>
  </td>
  <td valign=top style='border-top:none;border-left:none;border-bottom:solid #DDDDDD 1.0pt;
  border-right:solid #DDDDDD 1.0pt;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p class=MsoNormal><span style='font-size:10.0pt'>Up to 2.5</span></p>
  </td>
 </tr>
 <tr>
  <td rowspan=2 valign=top style='border:solid #DDDDDD 1.0pt;border-top:none;
  padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p class=MsoNormal><span style='font-size:10.0pt'>100 (NRZ)</span></p>
  </td>
  <td rowspan=2 valign=top style='border-top:none;border-left:none;border-bottom:
  solid #DDDDDD 1.0pt;border-right:solid #DDDDDD 1.0pt;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p class=MsoNormal>&#9989;</p>
  <p class=MsoNormal><span style='font-size:10.0pt'>&nbsp;</span></p>
  </td>
  <td rowspan=2 valign=top style='border-top:none;border-left:none;border-bottom:
  solid #DDDDDD 1.0pt;border-right:solid #DDDDDD 1.0pt;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p class=MsoNormal>&#9989;</p>
  <p class=MsoNormal><span style='font-size:10.0pt'>&nbsp;</span></p>
  </td>
  <td rowspan=2 valign=top style='border-top:none;border-left:none;border-bottom:
  solid #DDDDDD 1.0pt;border-right:solid #DDDDDD 1.0pt;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p class=MsoNormal>&#10008;</p>
  <p class=MsoNormal><span style='font-size:10.0pt'>&nbsp;</span></p>
  </td>
  <td rowspan=2 valign=top style='border-top:none;border-left:none;border-bottom:
  solid #DDDDDD 1.0pt;border-right:solid #DDDDDD 1.0pt;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p class=MsoNormal>&#9989;</p>
  </td>
  <td valign=top style='border-top:none;border-left:none;border-bottom:solid #DDDDDD 1.0pt;
  border-right:solid #DDDDDD 1.0pt;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p class=MsoNormal><span style='font-size:10.0pt'>Optic</span></p>
  </td>
  <td valign=top style='border-top:none;border-left:none;border-bottom:solid #DDDDDD 1.0pt;
  border-right:solid #DDDDDD 1.0pt;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p class=MsoNormal><span style='font-size:10.0pt'>Up to 100</span></p>
  </td>
 </tr>
 <tr>
  <td valign=top style='border-top:none;border-left:none;border-bottom:solid #DDDDDD 1.0pt;
  border-right:solid #DDDDDD 1.0pt;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p class=MsoNormal><span style='font-size:10.0pt'>Copper</span></p>
  </td>
  <td valign=top style='border-top:none;border-left:none;border-bottom:solid #DDDDDD 1.0pt;
  border-right:solid #DDDDDD 1.0pt;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p class=MsoNormal><span style='font-size:10.0pt'>Up to 5</span></p>
  </td>
 </tr>
 <tr>
  <td rowspan=2 valign=top style='border:solid #DDDDDD 1.0pt;border-top:none;
  padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p class=MsoNormal><span style='font-size:10.0pt'>25/50 (NRZ)</span></p>
  </td>
  <td rowspan=2 valign=top style='border-top:none;border-left:none;border-bottom:
  solid #DDDDDD 1.0pt;border-right:solid #DDDDDD 1.0pt;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p class=MsoNormal>&#9989;</p>
  <p class=MsoNormal><span style='font-size:10.0pt'>&nbsp;</span></p>
  </td>
  <td rowspan=2 valign=top style='border-top:none;border-left:none;border-bottom:
  solid #DDDDDD 1.0pt;border-right:solid #DDDDDD 1.0pt;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p class=MsoNormal>&#9989;</p>
  <p class=MsoNormal><span style='font-size:10.0pt'>&nbsp;</span></p>
  </td>
  <td rowspan=2 valign=top style='border-top:none;border-left:none;border-bottom:
  solid #DDDDDD 1.0pt;border-right:solid #DDDDDD 1.0pt;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p class=MsoNormal>&#9989;</p>
  </td>
  <td rowspan=2 valign=top style='border-top:none;border-left:none;border-bottom:
  solid #DDDDDD 1.0pt;border-right:solid #DDDDDD 1.0pt;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p class=MsoNormal>&#9989;</p>
  <p class=MsoNormal><span style='font-size:10.0pt'>&nbsp;</span></p>
  </td>
  <td valign=top style='border-top:none;border-left:none;border-bottom:solid #DDDDDD 1.0pt;
  border-right:solid #DDDDDD 1.0pt;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p class=MsoNormal><span style='font-size:10.0pt'>Optic</span></p>
  </td>
  <td valign=top style='border-top:none;border-left:none;border-bottom:solid #DDDDDD 1.0pt;
  border-right:solid #DDDDDD 1.0pt;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p class=MsoNormal><span style='font-size:10.0pt'>Up to 100</span></p>
  </td>
 </tr>
 <tr>
  <td valign=top style='border-top:none;border-left:none;border-bottom:solid #DDDDDD 1.0pt;
  border-right:solid #DDDDDD 1.0pt;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p class=MsoNormal><span style='font-size:10.0pt'>Copper</span></p>
  </td>
  <td valign=top style='border-top:none;border-left:none;border-bottom:solid #DDDDDD 1.0pt;
  border-right:solid #DDDDDD 1.0pt;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p class=MsoNormal><span style='font-size:10.0pt'>Up to 5</span></p>
  </td>
 </tr>
 <tr>
  <td rowspan=2 valign=top style='border:solid #DDDDDD 1.0pt;border-top:none;
  padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p class=MsoNormal><span style='font-size:10.0pt'>10/40</span></p>
  </td>
  <td rowspan=2 valign=top style='border-top:none;border-left:none;border-bottom:
  solid #DDDDDD 1.0pt;border-right:solid #DDDDDD 1.0pt;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p class=MsoNormal>&#9989;</p>
  </td>
  <td rowspan=2 valign=top style='border-top:none;border-left:none;border-bottom:
  solid #DDDDDD 1.0pt;border-right:solid #DDDDDD 1.0pt;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p class=MsoNormal>&#10008;</p>
  </td>
  <td rowspan=2 valign=top style='border-top:none;border-left:none;border-bottom:
  solid #DDDDDD 1.0pt;border-right:solid #DDDDDD 1.0pt;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p class=MsoNormal>&#9989;</p>
  </td>
  <td rowspan=2 valign=top style='border-top:none;border-left:none;border-bottom:
  solid #DDDDDD 1.0pt;border-right:solid #DDDDDD 1.0pt;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p class=MsoNormal>&#9989;</p>
  </td>
  <td valign=top style='border-top:none;border-left:none;border-bottom:solid #DDDDDD 1.0pt;
  border-right:solid #DDDDDD 1.0pt;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p class=MsoNormal><span style='font-size:10.0pt'>Optic</span></p>
  </td>
  <td valign=top style='border-top:none;border-left:none;border-bottom:solid #DDDDDD 1.0pt;
  border-right:solid #DDDDDD 1.0pt;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p class=MsoNormal><span style='font-size:10.0pt'>Up to 100</span></p>
  </td>
 </tr>
 <tr>
  <td valign=top style='border-top:none;border-left:none;border-bottom:solid #DDDDDD 1.0pt;
  border-right:solid #DDDDDD 1.0pt;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p class=MsoNormal><span style='font-size:10.0pt'>Copper</span></p>
  </td>
  <td valign=top style='border-top:none;border-left:none;border-bottom:solid #DDDDDD 1.0pt;
  border-right:solid #DDDDDD 1.0pt;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p class=MsoNormal><span style='font-size:10.0pt'>Up to 5</span></p>
  </td>
 </tr>
 <tr>
  <td valign=top style='border:solid #DDDDDD 1.0pt;border-top:none;padding:
  1.5pt 1.5pt 1.0pt 1.5pt'>
  <p class=MsoNormal><span style='font-size:10.0pt'>1</span></p>
  </td>
  <td valign=top style='border-top:none;border-left:none;border-bottom:solid #DDDDDD 1.0pt;
  border-right:solid #DDDDDD 1.0pt;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p class=MsoNormal>&#9989;</p>
  </td>
  <td valign=top style='border-top:none;border-left:none;border-bottom:solid #DDDDDD 1.0pt;
  border-right:solid #DDDDDD 1.0pt;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p class=MsoNormal>&#10008;</p>
  </td>
  <td valign=top style='border-top:none;border-left:none;border-bottom:solid #DDDDDD 1.0pt;
  border-right:solid #DDDDDD 1.0pt;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p class=MsoNormal>&#10008;</p>
  </td>
  <td valign=top style='border-top:none;border-left:none;border-bottom:solid #DDDDDD 1.0pt;
  border-right:solid #DDDDDD 1.0pt;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p class=MsoNormal>&#9989;</p>
  </td>
  <td valign=top style='border-top:none;border-left:none;border-bottom:solid #DDDDDD 1.0pt;
  border-right:solid #DDDDDD 1.0pt;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p class=MsoNormal><span style='font-size:10.0pt'>Optic/Copper</span></p>
  </td>
  <td valign=top style='border-top:none;border-left:none;border-bottom:solid #DDDDDD 1.0pt;
  border-right:solid #DDDDDD 1.0pt;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p class=MsoNormal><span style='font-size:10.0pt'>Up to 5</span></p>
  </td>
 </tr>
</table>

### Mellanox Spectrum®-3 SN4600C Supported Port Speeds

<table border=1 cellspacing=0 cellpadding=0 width="100%"
 style='width:100.0%;border-collapse:collapse;border:none'>
  <tr>
   <td rowspan=2 valign=top style='border:solid #DDDDDD 1.0pt;background:#cbd4e0;
   padding:1.5pt 1.5pt 1.0pt 1.5pt'>
   <p class=CellHeading><b>Speed [GbE]</b></p>
   </td>
   <td rowspan=2 valign=top style='border:solid #DDDDDD 1.0pt;border-left:none;
   background:#cbd4e0;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
   <p class=CellHeading><b>AutoNeg</b></p>
   </td>
   <td colspan=3 valign=top style='border:solid #DDDDDD 1.0pt;border-left:none;
   background:#cbd4e0;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
   <p class=CellHeading><b>Force</b></p>
   </td>
   <td rowspan=2 valign=top style='border:solid #DDDDDD 1.0pt;border-left:none;
   background:#cbd4e0;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
   <p class=CellHeading><b>Cable / Modules</b></p>
   </td>
   <td rowspan=2 valign=top style='border:solid #DDDDDD 1.0pt;border-left:none;
   background:#cbd4e0;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
   <p class=CellHeading><b>Cable Length [m]</b></p>
   </td>
 </tr>
 <tr>
   <td valign=top style='border-top:none;border-left:none;border-bottom:solid #DDDDDD 1.0pt;
  border-right:solid #DDDDDD 1.0pt;background:#cbd4e0;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p class=CellHeading>RS FEC</p>
  </td>
  <td valign=top style='border-top:none;border-left:none;border-bottom:solid #DDDDDD 1.0pt;
  border-right:solid #DDDDDD 1.0pt;background:#cbd4e0;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p class=CellHeading>FC FEC</p>
  </td>
  <td valign=top style='border-top:none;border-left:none;border-bottom:solid #DDDDDD 1.0pt;
  border-right:solid #DDDDDD 1.0pt;background:#cbd4e0;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p class=CellHeading>NO FEC</p>
  </td>
 </tr>
 </thead>
 <tr>
  <td rowspan=2 valign=top style='border:solid #DDDDDD 1.0pt;border-top:none;
  padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p class=MsoNormal><span style='font-size:10.0pt'>100 (NRZ)</span></p>
  </td>
  <td rowspan=2 valign=top style='border-top:none;border-left:none;border-bottom:
  solid #DDDDDD 1.0pt;border-right:solid #DDDDDD 1.0pt;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p class=MsoNormal>&#9989;</p>
  <p class=MsoNormal><span style='font-size:10.0pt'>&nbsp;</span></p>
  </td>
  <td rowspan=2 valign=top style='border-top:none;border-left:none;border-bottom:
  solid #DDDDDD 1.0pt;border-right:solid #DDDDDD 1.0pt;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p class=MsoNormal>&#9989;</p>
  <p class=MsoNormal><span style='font-size:10.0pt'>&nbsp;</span></p>
  </td>
  <td rowspan=2 valign=top style='border-top:none;border-left:none;border-bottom:
  solid #DDDDDD 1.0pt;border-right:solid #DDDDDD 1.0pt;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p class=MsoNormal>&#10008;</p>
  <p class=MsoNormal><span style='font-size:10.0pt'>&nbsp;</span></p>
  </td>
  <td rowspan=2 valign=top style='border-top:none;border-left:none;border-bottom:
  solid #DDDDDD 1.0pt;border-right:solid #DDDDDD 1.0pt;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p class=MsoNormal>&#9989;</p>
  </td>
  <td valign=top style='border-top:none;border-left:none;border-bottom:solid #DDDDDD 1.0pt;
  border-right:solid #DDDDDD 1.0pt;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p class=MsoNormal><span style='font-size:10.0pt'>Optic</span></p>
  </td>
  <td valign=top style='border-top:none;border-left:none;border-bottom:solid #DDDDDD 1.0pt;
  border-right:solid #DDDDDD 1.0pt;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p class=MsoNormal><span style='font-size:10.0pt'>Up to 100</span></p>
  </td>
 </tr>
 <tr>
  <td valign=top style='border-top:none;border-left:none;border-bottom:solid #DDDDDD 1.0pt;
  border-right:solid #DDDDDD 1.0pt;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p class=MsoNormal><span style='font-size:10.0pt'>Copper</span></p>
  </td>
  <td valign=top style='border-top:none;border-left:none;border-bottom:solid #DDDDDD 1.0pt;
  border-right:solid #DDDDDD 1.0pt;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p class=MsoNormal><span style='font-size:10.0pt'>Up to 3</span></p>
  </td>
 </tr>
 <tr>
  <td rowspan=2 valign=top style='border:solid #DDDDDD 1.0pt;border-top:none;
  padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p class=MsoNormal><span style='font-size:10.0pt'>25/50 (NRZ)</span></p>
  </td>
  <td rowspan=2 valign=top style='border-top:none;border-left:none;border-bottom:
  solid #DDDDDD 1.0pt;border-right:solid #DDDDDD 1.0pt;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p class=MsoNormal>&#9989;</p>
  <p class=MsoNormal><span style='font-size:10.0pt'>&nbsp;</span></p>
  </td>
  <td rowspan=2 valign=top style='border-top:none;border-left:none;border-bottom:
  solid #DDDDDD 1.0pt;border-right:solid #DDDDDD 1.0pt;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p class=MsoNormal>&#9989;</p>
  <p class=MsoNormal><span style='font-size:10.0pt'>&nbsp;</span></p>
  </td>
  <td rowspan=2 valign=top style='border-top:none;border-left:none;border-bottom:
  solid #DDDDDD 1.0pt;border-right:solid #DDDDDD 1.0pt;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p class=MsoNormal>&#9989;</p>
  </td>
  <td rowspan=2 valign=top style='border-top:none;border-left:none;border-bottom:
  solid #DDDDDD 1.0pt;border-right:solid #DDDDDD 1.0pt;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p class=MsoNormal>&#9989;</p>
  <p class=MsoNormal><span style='font-size:10.0pt'>&nbsp;</span></p>
  </td>
  <td valign=top style='border-top:none;border-left:none;border-bottom:solid #DDDDDD 1.0pt;
  border-right:solid #DDDDDD 1.0pt;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p class=MsoNormal><span style='font-size:10.0pt'>Optic</span></p>
  </td>
  <td valign=top style='border-top:none;border-left:none;border-bottom:solid #DDDDDD 1.0pt;
  border-right:solid #DDDDDD 1.0pt;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p class=MsoNormal><span style='font-size:10.0pt'>Up to 100</span></p>
  </td>
 </tr>
 <tr>
  <td valign=top style='border-top:none;border-left:none;border-bottom:solid #DDDDDD 1.0pt;
  border-right:solid #DDDDDD 1.0pt;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p class=MsoNormal><span style='font-size:10.0pt'>Copper</span></p>
  </td>
  <td valign=top style='border-top:none;border-left:none;border-bottom:solid #DDDDDD 1.0pt;
  border-right:solid #DDDDDD 1.0pt;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p class=MsoNormal><span style='font-size:10.0pt'>Up to 5</span></p>
  </td>
 </tr>
 <tr>
  <td rowspan=2 valign=top style='border:solid #DDDDDD 1.0pt;border-top:none;
  padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p class=MsoNormal><span style='font-size:10.0pt'>10/40</span></p>
  </td>
  <td rowspan=2 valign=top style='border-top:none;border-left:none;border-bottom:
  solid #DDDDDD 1.0pt;border-right:solid #DDDDDD 1.0pt;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p class=MsoNormal>&#9989;</p>
  </td>
  <td rowspan=2 valign=top style='border-top:none;border-left:none;border-bottom:
  solid #DDDDDD 1.0pt;border-right:solid #DDDDDD 1.0pt;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p class=MsoNormal>&#10008;</p>
  </td>
  <td rowspan=2 valign=top style='border-top:none;border-left:none;border-bottom:
  solid #DDDDDD 1.0pt;border-right:solid #DDDDDD 1.0pt;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p class=MsoNormal>&#9989;</p>
  </td>
  <td rowspan=2 valign=top style='border-top:none;border-left:none;border-bottom:
  solid #DDDDDD 1.0pt;border-right:solid #DDDDDD 1.0pt;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p class=MsoNormal>&#9989;</p>
  </td>
  <td valign=top style='border-top:none;border-left:none;border-bottom:solid #DDDDDD 1.0pt;
  border-right:solid #DDDDDD 1.0pt;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p class=MsoNormal><span style='font-size:10.0pt'>Optic</span></p>
  </td>
  <td valign=top style='border-top:none;border-left:none;border-bottom:solid #DDDDDD 1.0pt;
  border-right:solid #DDDDDD 1.0pt;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p class=MsoNormal><span style='font-size:10.0pt'>Up to 100</span></p>
  </td>
 </tr>
 <tr>
  <td valign=top style='border-top:none;border-left:none;border-bottom:solid #DDDDDD 1.0pt;
  border-right:solid #DDDDDD 1.0pt;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p class=MsoNormal><span style='font-size:10.0pt'>Copper</span></p>
  </td>
  <td valign=top style='border-top:none;border-left:none;border-bottom:solid #DDDDDD 1.0pt;
  border-right:solid #DDDDDD 1.0pt;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p class=MsoNormal><span style='font-size:10.0pt'>Up to 3</span></p>
  </td>
 </tr>
 <tr>
  <td valign=top style='border:solid #DDDDDD 1.0pt;border-top:none;padding:
  1.5pt 1.5pt 1.0pt 1.5pt'>
  <p class=MsoNormal><span style='font-size:10.0pt'>1</span></p>
  </td>
  <td valign=top style='border-top:none;border-left:none;border-bottom:solid #DDDDDD 1.0pt;
  border-right:solid #DDDDDD 1.0pt;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p class=MsoNormal>&#9989;</p>
  </td>
  <td valign=top style='border-top:none;border-left:none;border-bottom:solid #DDDDDD 1.0pt;
  border-right:solid #DDDDDD 1.0pt;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p class=MsoNormal>&#10008;</p>
  </td>
  <td valign=top style='border-top:none;border-left:none;border-bottom:solid #DDDDDD 1.0pt;
  border-right:solid #DDDDDD 1.0pt;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p class=MsoNormal>&#10008;</p>
  </td>
  <td valign=top style='border-top:none;border-left:none;border-bottom:solid #DDDDDD 1.0pt;
  border-right:solid #DDDDDD 1.0pt;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p class=MsoNormal>&#9989;</p>
  </td>
  <td valign=top style='border-top:none;border-left:none;border-bottom:solid #DDDDDD 1.0pt;
  border-right:solid #DDDDDD 1.0pt;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p class=MsoNormal><span style='font-size:10.0pt'>Optic/Copper</span></p>
  </td>
  <td valign=top style='border-top:none;border-left:none;border-bottom:solid #DDDDDD 1.0pt;
  border-right:solid #DDDDDD 1.0pt;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p class=MsoNormal><span style='font-size:10.0pt'>Up to 5</span></p>
  </td>
 </tr>
</table>

### Mellanox Spectrum®-2 SN3800 Series Supported Port Speeds

<table border=1 cellspacing=0 cellpadding=0 width="100%"
 style='width:100.0%;border-collapse:collapse;border:none'>
  <tr>
   <td rowspan=2 valign=top style='border:solid #DDDDDD 1.0pt;background:#cbd4e0;
   padding:1.5pt 1.5pt 1.0pt 1.5pt'>
   <p class=CellHeading><b>Speed [GbE]</b></p>
   </td>
   <td rowspan=2 valign=top style='border:solid #DDDDDD 1.0pt;border-left:none;
   background:#cbd4e0;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
   <p class=CellHeading><b>AutoNeg</b></p>
   </td>
   <td colspan=3 valign=top style='border:solid #DDDDDD 1.0pt;border-left:none;
   background:#cbd4e0;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
   <p class=CellHeading><b>Force</b></p>
   </td>
   <td rowspan=2 valign=top style='border:solid #DDDDDD 1.0pt;border-left:none;
   background:#cbd4e0;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
   <p class=CellHeading><b>Cable / Modules</b></p>
   </td>
   <td rowspan=2 valign=top style='border:solid #DDDDDD 1.0pt;border-left:none;
   background:#cbd4e0;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
   <p class=CellHeading><b>Cable Length [m]</b></p>
   </td>
   <td rowspan=2 valign=top style='border:solid #DDDDDD 1.0pt;border-left:none;
   background:#cbd4e0;padding:1.5pt 1.5pt 1.0pt 1.5pt'><b>Comments</b></td>
 </tr>
 <tr>
   <td valign=top style='border-top:none;border-left:none;border-bottom:solid #DDDDDD 1.0pt;
  border-right:solid #DDDDDD 1.0pt;background:#cbd4e0;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p class=CellHeading>RS FEC</p>
  </td>
  <td valign=top style='border-top:none;border-left:none;border-bottom:solid #DDDDDD 1.0pt;
  border-right:solid #DDDDDD 1.0pt;background:#cbd4e0;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p class=CellHeading>FC FEC</p>
  </td>
  <td valign=top style='border-top:none;border-left:none;border-bottom:solid #DDDDDD 1.0pt;
  border-right:solid #DDDDDD 1.0pt;background:#cbd4e0;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p class=CellHeading>NO FEC</p>
  </td>
 </tr>
 </thead>
 <tr>
  <td rowspan=2 valign=top style='border:solid #DDDDDD 1.0pt;border-top:none;
  padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p class=MsoNormal><span style='font-size:10.0pt'>100 (NRZ)</span></p>
  </td>
  <td rowspan=2 valign=top style='border-top:none;border-left:none;border-bottom:
  solid #DDDDDD 1.0pt;border-right:solid #DDDDDD 1.0pt;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p class=MsoNormal>&#10008;</p>
  <p class=MsoNormal><span style='font-size:10.0pt'>&nbsp;</span></p>
  </td>
  <td rowspan=2 valign=top style='border-top:none;border-left:none;border-bottom:
  solid #DDDDDD 1.0pt;border-right:solid #DDDDDD 1.0pt;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p class=MsoNormal>&#9989;</p>
  <p class=MsoNormal><span style='font-size:10.0pt'>&nbsp;</span></p>
  </td>
  <td rowspan=2 valign=top style='border-top:none;border-left:none;border-bottom:
  solid #DDDDDD 1.0pt;border-right:solid #DDDDDD 1.0pt;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p class=MsoNormal>&#10008;</p>
  <p class=MsoNormal><span style='font-size:10.0pt'>&nbsp;</span></p>
  </td>
  <td rowspan=2 valign=top style='border-top:none;border-left:none;border-bottom:
  solid #DDDDDD 1.0pt;border-right:solid #DDDDDD 1.0pt;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p class=MsoNormal>&#9989;</p>
  </td>
  <td valign=top style='border-top:none;border-left:none;border-bottom:solid #DDDDDD 1.0pt;
  border-right:solid #DDDDDD 1.0pt;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p class=MsoNormal><span style='font-size:10.0pt'>Optic</span></p>
  </td>
  <td valign=top style='border-top:none;border-left:none;border-bottom:solid #DDDDDD 1.0pt;
  border-right:solid #DDDDDD 1.0pt;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p class=MsoNormal><span style='font-size:10.0pt'>Up to 30</span></p>
  </td>
  <td rowspan=2 valign=top style='border:solid #DDDDDD 1.0pt;border-top:none;
  padding:1.5pt 1.5pt 1.0pt 1.5pt'>N/A</td>
 </tr>
 <tr>
  <td valign=top style='border-top:none;border-left:none;border-bottom:solid #DDDDDD 1.0pt;
  border-right:solid #DDDDDD 1.0pt;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p class=MsoNormal><span style='font-size:10.0pt'>Copper</span></p>
  </td>
  <td valign=top style='border-top:none;border-left:none;border-bottom:solid #DDDDDD 1.0pt;
  border-right:solid #DDDDDD 1.0pt;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p class=MsoNormal><span style='font-size:10.0pt'>Up to 5</span></p>
  </td>
 </tr>
 <tr>
  <td rowspan=2 valign=top style='border:solid #DDDDDD 1.0pt;border-top:none;
  padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p class=MsoNormal><span style='font-size:10.0pt'>25/50 (NRZ)</span></p>
  </td>
  <td rowspan=2 valign=top style='border-top:none;border-left:none;border-bottom:
  solid #DDDDDD 1.0pt;border-right:solid #DDDDDD 1.0pt;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p class=MsoNormal>&#10008;</p>
  <p class=MsoNormal><span style='font-size:10.0pt'>&nbsp;</span></p>
  </td>
  <td rowspan=2 valign=top style='border-top:none;border-left:none;border-bottom:
  solid #DDDDDD 1.0pt;border-right:solid #DDDDDD 1.0pt;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p class=MsoNormal>&#9989;</p>
  <p class=MsoNormal><span style='font-size:10.0pt'>&nbsp;</span></p>
  </td>
  <td rowspan=2 valign=top style='border-top:none;border-left:none;border-bottom:
  solid #DDDDDD 1.0pt;border-right:solid #DDDDDD 1.0pt;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p class=MsoNormal>&#9989;</p>
  </td>
  <td rowspan=2 valign=top style='border-top:none;border-left:none;border-bottom:
  solid #DDDDDD 1.0pt;border-right:solid #DDDDDD 1.0pt;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p class=MsoNormal>&#9989;</p>
  <p class=MsoNormal><span style='font-size:10.0pt'>&nbsp;</span></p>
  </td>
  <td valign=top style='border-top:none;border-left:none;border-bottom:solid #DDDDDD 1.0pt;
  border-right:solid #DDDDDD 1.0pt;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p class=MsoNormal><span style='font-size:10.0pt'>Optic</span></p>
  </td>
  <td valign=top style='border-top:none;border-left:none;border-bottom:solid #DDDDDD 1.0pt;
  border-right:solid #DDDDDD 1.0pt;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p class=MsoNormal><span style='font-size:10.0pt'>Up to 30</span></p>
  </td>
  <td rowspan=2 valign=top style='border:solid #DDDDDD 1.0pt;border-top:none;
  padding:1.5pt 1.5pt 1.0pt 1.5pt'>N/A</td>
 </tr>
 <tr>
  <td valign=top style='border-top:none;border-left:none;border-bottom:solid #DDDDDD 1.0pt;
  border-right:solid #DDDDDD 1.0pt;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p class=MsoNormal><span style='font-size:10.0pt'>Copper</span></p>
  </td>
  <td valign=top style='border-top:none;border-left:none;border-bottom:solid #DDDDDD 1.0pt;
  border-right:solid #DDDDDD 1.0pt;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p class=MsoNormal><span style='font-size:10.0pt'>Up to 5</span></p>
  </td>
 </tr>
 <tr>
  <td rowspan=2 valign=top style='border:solid #DDDDDD 1.0pt;border-top:none;
  padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p class=MsoNormal><span style='font-size:10.0pt'>10/40</span></p>
  </td>
  <td rowspan=2 valign=top style='border-top:none;border-left:none;border-bottom:
  solid #DDDDDD 1.0pt;border-right:solid #DDDDDD 1.0pt;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p class=MsoNormal>&#10008;</p>
  </td>
  <td rowspan=2 valign=top style='border-top:none;border-left:none;border-bottom:
  solid #DDDDDD 1.0pt;border-right:solid #DDDDDD 1.0pt;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p class=MsoNormal>&#10008;</p>
  </td>
  <td rowspan=2 valign=top style='border-top:none;border-left:none;border-bottom:
  solid #DDDDDD 1.0pt;border-right:solid #DDDDDD 1.0pt;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p class=MsoNormal>&#10008;</p>
  </td>
  <td rowspan=2 valign=top style='border-top:none;border-left:none;border-bottom:
  solid #DDDDDD 1.0pt;border-right:solid #DDDDDD 1.0pt;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p class=MsoNormal>&#9989;</p>
  </td>
  <td valign=top style='border-top:none;border-left:none;border-bottom:solid #DDDDDD 1.0pt;
  border-right:solid #DDDDDD 1.0pt;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p class=MsoNormal><span style='font-size:10.0pt'>Optic</span></p>
  </td>
  <td valign=top style='border-top:none;border-left:none;border-bottom:solid #DDDDDD 1.0pt;
  border-right:solid #DDDDDD 1.0pt;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p class=MsoNormal><span style='font-size:10.0pt'>Up to 30</span></p>
  </td>
  <td rowspan=2 valign=top style='border:solid #DDDDDD 1.0pt;border-top:none;
  padding:1.5pt 1.5pt 1.0pt 1.5pt'>10GBASE-T modules are not supported</td>
 </tr>
 <tr>
  <td valign=top style='border-top:none;border-left:none;border-bottom:solid #DDDDDD 1.0pt;
  border-right:solid #DDDDDD 1.0pt;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p class=MsoNormal><span style='font-size:10.0pt'>Copper</span></p>
  </td>
  <td valign=top style='border-top:none;border-left:none;border-bottom:solid #DDDDDD 1.0pt;
  border-right:solid #DDDDDD 1.0pt;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p class=MsoNormal><span style='font-size:10.0pt'>Up to 3</span></p>
  </td>
 </tr>
</table>

...

## Changes and New Features History

<table class=ScrollTableNormal border=1 cellspacing=0 cellpadding=0 width="100%"
 style='border-collapse:collapse;border:none'>
 <thead>
  <tr>
   <td width=186 valign=top style='width:139.25pt;border:solid #DDDDDD 1.0pt;
   background:#cbd4e0;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
   <p class=CellHeading align=center style='text-align:center'><b>Category</b></p>
   </td>
   <td width=423 valign=top style='width:317.45pt;border:solid #DDDDDD 1.0pt;
   border-left:none;background:#cbd4e0;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
   <p class=CellHeading align=center style='text-align:center'><b>Description</b></p>
   </td>
  </tr>
 </thead>
 <tr>
  <td width=609 colspan=2 valign=top style='width:456.7pt;border:solid #DDDDDD 1.0pt;
  border-top:none;background:#cbd4e0;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p class=CellHeading align=center style='text-align:center'>Rev. SONiC
  201911_MUR3</p>
  </td>
 </tr>
 <tr>
  <td width=186 valign=top style='width:139.25pt;border:solid #DDDDDD 1.0pt;
  border-top:none;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p class=MsoNormal><b><span style='font-size:10.0pt'>Switch Systems</span></b></p>
  </td>
  <td width=423 valign=top style='width:317.45pt;border-top:none;border-left:
  none;border-bottom:solid #DDDDDD 1.0pt;border-right:solid #DDDDDD 1.0pt;
  padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p class=MsoNormal><span style='font-size:10.0pt'>NVIDIA Mellanox Spectrum-3
  (SN4600C) and NVIDIA Mellanox Spectrum-2 (SN3420) Ethernet switch platforms
  are now at GA Level.</span></p>
  </td>
 </tr>
 <tr>
  <td width=186 valign=top style='width:139.25pt;border:solid #DDDDDD 1.0pt;
  border-top:none;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p class=MsoNormal><b><span style='font-size:10.0pt'>Buffers</span></b></p>
  </td>
  <td width=423 valign=top style='width:317.45pt;border-top:none;border-left:
  none;border-bottom:solid #DDDDDD 1.0pt;border-right:solid #DDDDDD 1.0pt;
  padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p class=MsoNormal><span style='font-size:10.0pt'>Aligned all platforms to
  recent headroom calculation for both T0 and T1.<br>
  <b>Note:</b> Upgrading to this version will not automatically update the
  numbers. In order to have them applied, you should run the &quot;config
  load_minigraph&quot; command.</span></p>
  </td>
 </tr>
 <tr>
  <td width=186 valign=top style='width:139.25pt;border:solid #DDDDDD 1.0pt;
  border-top:none;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p class=MsoNormal><b><span style='font-size:10.0pt'>What-Just-Happened</span></b></p>
  </td>
  <td width=423 valign=top style='width:317.45pt;border-top:none;border-left:
  none;border-bottom:solid #DDDDDD 1.0pt;border-right:solid #DDDDDD 1.0pt;
  padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p class=MsoNormal><span style='font-size:10.0pt'>Added sample window
  information for all aggregated show commands.</span></p>
  </td>
 </tr>
 <tr>
  <td width=186 valign=top style='width:139.25pt;border:solid #DDDDDD 1.0pt;
  border-top:none;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p class=MsoNormal><b><span style='font-size:10.0pt'>Warm-boot</span></b></p>
  </td>
  <td width=423 valign=top style='width:317.45pt;border-top:none;border-left:
  none;border-bottom:solid #DDDDDD 1.0pt;border-right:solid #DDDDDD 1.0pt;
  padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p class=MsoNormal><span style='font-size:10.0pt'>Added support for warm-boot
  capability for&nbsp;SN4700 and SN4600C switch systems.&nbsp;</span></p>
  </td>
 </tr>
 <tr>
  <td width=186 valign=top style='width:139.25pt;border:solid #DDDDDD 1.0pt;
  border-top:none;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p class=MsoNormal><b><span style='font-size:10.0pt'>Cables</span></b></p>
  </td>
  <td width=423 valign=top style='width:317.45pt;border-top:none;border-left:
  none;border-bottom:solid #DDDDDD 1.0pt;border-right:solid #DDDDDD 1.0pt;
  padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p class=MsoNormal><span style='font-size:10.0pt'>Added support for QSFP-DD
  module in SN4700 switch systems used for all &quot;show&quot; commands and
  SFP monitoring.</span></p>
  </td>
 </tr>
 <tr>
  <td width=186 valign=top style='width:139.25pt;border:solid #DDDDDD 1.0pt;
  border-top:none;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p class=MsoNormal><b><span style='font-size:10.0pt'>Build</span></b></p>
  </td>
  <td width=423 valign=top style='width:317.45pt;border-top:none;border-left:
  none;border-bottom:solid #DDDDDD 1.0pt;border-right:solid #DDDDDD 1.0pt;
  padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p class=MsoNormal><span style='font-size:10.0pt'>Added DKMS build support
  for Mellanox MFT and SDK.</span></p>
  </td>
 </tr>
 <tr>
  <td width=186 valign=top style='width:139.25pt;border:solid #DDDDDD 1.0pt;
  border-top:none;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p class=MsoNormal><b><span style='font-size:10.0pt'>Customer-Affecting
  Changes</span></b></p>
  </td>
  <td width=423 valign=top style='width:317.45pt;border-top:none;border-left:
  none;border-bottom:solid #DDDDDD 1.0pt;border-right:solid #DDDDDD 1.0pt;
  padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p class=MsoNormal><span style='font-size:10.0pt'>See&nbsp;</span><a
  href="#scroll-bookmark-21"><span style='font-size:10.0pt'>Customer-Affecting
  Changes</span></a><span style='font-size:10.0pt'>.</span></p>
  </td>
 </tr>
 <tr>
  <td width=609 colspan=2 valign=top style='width:456.7pt;border:solid #DDDDDD 1.0pt;
  border-top:none;background:#cbd4e0;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p class=CellHeading align=center style='text-align:center'>Rev. SONiC
  201911_MUR2</p>
  </td>
 </tr>
 <tr>
  <td width=186 valign=top style='width:139.25pt;border:solid #DDDDDD 1.0pt;
  border-top:none;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p class=MsoNormal><b><span style='font-size:10.0pt'>Proxy-ARP</span></b></p>
  </td>
  <td width=423 valign=top style='width:317.45pt;border-top:none;border-left:
  none;border-bottom:solid #DDDDDD 1.0pt;border-right:solid #DDDDDD 1.0pt;
  padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p class=MsoNormal><span style='font-size:10.0pt'>The Proxy ARP distributes
  traffic through multiple gateways by balancing load based on source and
  destination IP addresses.</span></p>
  <p class=MsoNormal><span style='font-size:10.0pt'>For further information,
  see</span><a
  href="https://github.com/Azure/SONiC/blob/master/doc/arp/Proxy%20Arp.md"><span
  style='font-size:10.0pt'>https://github.com/Azure/SONiC/blob/master/doc/arp/Proxy%20Arp.md</span></a></p>
  </td>
 </tr>
 <tr>
  <td width=186 valign=top style='width:139.25pt;border:solid #DDDDDD 1.0pt;
  border-top:none;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p class=MsoNormal><b><span style='font-size:10.0pt'>Thermal Control</span></b></p>
  </td>
  <td width=423 valign=top style='width:317.45pt;border-top:none;border-left:
  none;border-bottom:solid #DDDDDD 1.0pt;border-right:solid #DDDDDD 1.0pt;
  padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p class=MsoNormal><span style='font-size:10.0pt'>The Thermal Control keeps
  the switch at a proper temperature by using cooling devices.</span></p>
  <p class=MsoNormal><span style='font-size:10.0pt'>For further information,
  see</span></p>
  <p class=MsoNormal><a
  href="https://github.com/Azure/SONiC/blob/master/doc/pmon/sonic_thermal_control_test_plan.md"><span
  style='font-size:10.0pt'>https://github.com/Azure/SONiC/blob/master/doc/pmon/sonic_thermal_control_test_plan.md</span></a></p>
  </td>
 </tr>
 <tr>
  <td width=186 valign=top style='width:139.25pt;border:solid #DDDDDD 1.0pt;
  border-top:none;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p class=MsoNormal><b><span style='font-size:10.0pt'>What-Just-Happened</span></b></p>
  </td>
  <td width=423 valign=top style='width:317.45pt;border-top:none;border-left:
  none;border-bottom:solid #DDDDDD 1.0pt;border-right:solid #DDDDDD 1.0pt;
  padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p class=MsoNormal><span style='font-size:10.0pt'>The What-Just-Happened
  feature provides the ability to retain the last packets that were dropped
  from the switch with complete packet headers and the actual drop reason. This
  enhances the ability to debug network problems, identify affected flows, and
  decrease time-to-repair.</span></p>
  <p class=MsoNormal><span style='font-size:10.0pt'>Once enabled, the user can
  debug L2, l3 and Tunnel drop packets with raw and aggregated information.</span></p>
  <p class=MsoNormal><span style='font-size:10.0pt'>The features should be
  downloaded and installed on top of a SONiC release via DPKT. Please contact
  Mellanox Support to get this package.</span></p>
  </td>
 </tr>
 <tr>
  <td width=609 colspan=2 valign=top style='width:456.7pt;border:solid #DDDDDD 1.0pt;
  border-top:none;background:#cbd4e0;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p class=CellHeading align=center style='text-align:center'>Rev. SONiC
  201911_MUR1</p>
  </td>
 </tr>
 <tr>
  <td width=186 valign=top style='width:139.25pt;border:solid #DDDDDD 1.0pt;
  border-top:none;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p class=MsoNormal><b><span style='font-size:10.0pt'>Switch Systems</span></b></p>
  </td>
  <td width=423 valign=top style='width:317.45pt;border-top:none;border-left:
  none;border-bottom:solid #DDDDDD 1.0pt;border-right:solid #DDDDDD 1.0pt;
  padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p class=MsoNormal><span style='font-size:10.0pt'>Added support for Mellanox
  Spectrum-2 (SN3420) and Mellanox Spectrum-3 (SN4700 and SN4600C) Ethernet
  switch platforms at Engineering Sample Level.</span></p>
  </td>
 </tr>
 <tr>
  <td width=186 valign=top style='width:139.25pt;border:solid #DDDDDD 1.0pt;
  border-top:none;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p class=MsoNormal><b><span style='font-size:10.0pt'>PAM4 Link Speeds when
  Using 400GbE/200GbE</span></b></p>
  </td>
  <td width=423 valign=top style='width:317.45pt;border-top:none;border-left:
  none;border-bottom:solid #DDDDDD 1.0pt;border-right:solid #DDDDDD 1.0pt;
  padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p class=MsoNormal><span style='font-size:10.0pt'>The following are the
  minimal software/firmware versions that support PAM4 link speeds when
  connected using Mellanox-to-Mellanox and Mellanox-to-3rd party devices:</span></p>
  <p class=MsoNormal style='margin-left:.25in;text-indent:-.25in'><span
  style='font-size:10.0pt;font-family:Symbol'>·<span style='font:7.0pt "Times New Roman"'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
  </span></span><span style='font-size:10.0pt'>Mellanox Onyx: 3.9.0900</span></p>
  <p class=MsoNormal style='margin-left:.25in;text-indent:-.25in'><span
  style='font-size:10.0pt;font-family:Symbol'>·<span style='font:7.0pt "Times New Roman"'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
  </span></span><span style='font-size:10.0pt'>ConnectX-6/ConnectX-6 Dx:
  20/22.27.2008*</span></p>
  <p class=MsoNormal><b><span style='font-size:10.0pt'>*Note:</span></b><span
  style='font-size:10.0pt'> NICs with this firmware version support
  Mellanox-to-Mellanox connectivity with PAM4 link speeds.</span></p>
  </td>
 </tr>
 <tr>
  <td width=186 valign=top style='width:139.25pt;border:solid #DDDDDD 1.0pt;
  border-top:none;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p class=MsoNormal><b><span style='font-size:10.0pt'>Link Speed</span></b></p>
  </td>
  <td width=423 valign=top style='width:317.45pt;border-top:none;border-left:
  none;border-bottom:solid #DDDDDD 1.0pt;border-right:solid #DDDDDD 1.0pt;
  padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p class=MsoNormal><span style='font-size:10.0pt'>200GbE speed rate is at GA
  level when connecting Mellanox to Mellanox cables.</span></p>
  </td>
 </tr>
 <tr>
  <td width=186 valign=top style='width:139.25pt;border:solid #DDDDDD 1.0pt;
  border-top:none;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p class=MsoNormal><b><span style='font-size:10.0pt'>Link Speed</span></b></p>
  </td>
  <td width=423 valign=top style='width:317.45pt;border-top:none;border-left:
  none;border-bottom:solid #DDDDDD 1.0pt;border-right:solid #DDDDDD 1.0pt;
  padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p class=MsoNormal><span style='font-size:10.0pt'>200GbE speed rate is at
  Engineering Sample Level when connecting Mellanox to 3<sup>rd</sup> party
  cables.</span></p>
  </td>
 </tr>
 <tr>
  <td width=186 valign=top style='width:139.25pt;border:solid #DDDDDD 1.0pt;
  border-top:none;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p class=MsoNormal><b><span style='font-size:10.0pt'>Link Speed</span></b></p>
  </td>
  <td width=423 valign=top style='width:317.45pt;border-top:none;border-left:
  none;border-bottom:solid #DDDDDD 1.0pt;border-right:solid #DDDDDD 1.0pt;
  padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p class=MsoNormal><span style='font-size:10.0pt'>400GbE speed rate is at
  Engineering Sample Level.</span></p>
  </td>
 </tr>
 <tr>
  <td width=186 valign=top style='width:139.25pt;border:solid #DDDDDD 1.0pt;
  border-top:none;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p class=MsoNormal><b><span style='font-size:10.0pt'>ZTP</span></b></p>
  </td>
  <td width=423 valign=top style='width:317.45pt;border-top:none;border-left:
  none;border-bottom:solid #DDDDDD 1.0pt;border-right:solid #DDDDDD 1.0pt;
  padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p class=MsoNormal><span style='font-size:10.0pt'>Out-of-band management is
  now functional. &nbsp;</span></p>
  </td>
 </tr>
 <tr>
  <td width=609 colspan=2 valign=top style='width:456.7pt;border:solid #DDDDDD 1.0pt;
  border-top:none;background:#cbd4e0;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p class=CellHeading align=center style='text-align:center'>Rev. SONiC 201911</p>
  </td>
 </tr>
 <tr>
  <td width=186 valign=top style='width:139.25pt;border:solid #DDDDDD 1.0pt;
  border-top:none;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p class=MsoNormal><b><span style='font-size:10.0pt'>Switch Systems</span></b></p>
  </td>
  <td width=423 valign=top style='width:317.45pt;border-top:none;border-left:
  none;border-bottom:solid #DDDDDD 1.0pt;border-right:solid #DDDDDD 1.0pt;
  padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p class=MsoNormal><span style='font-size:10.0pt'>Added support for Mellanox
  Spectrum-2 Ethernet switch platforms (SN3700, SN3700C and SN3800).</span></p>
  </td>
 </tr>
 <tr>
  <td width=186 valign=top style='width:139.25pt;border:solid #DDDDDD 1.0pt;
  border-top:none;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p class=MsoNormal><b><span style='font-size:10.0pt'>Zero Time Warm-boot</span></b></p>
  </td>
  <td width=423 valign=top style='width:317.45pt;border-top:none;border-left:
  none;border-bottom:solid #DDDDDD 1.0pt;border-right:solid #DDDDDD 1.0pt;
  padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p class=MsoNormal><span style='font-size:10.0pt'>No data disruption for
  Mellanox Spectrum and Spectrum-2 Ethernet switch platforms.</span></p>
  </td>
 </tr>
 <tr>
  <td width=186 valign=top style='width:139.25pt;border:solid #DDDDDD 1.0pt;
  border-top:none;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p class=MsoNormal><b><span style='font-size:10.0pt'>Warm-boot for Spectrum-2</span></b></p>
  </td>
  <td width=423 valign=top style='width:317.45pt;border-top:none;border-left:
  none;border-bottom:solid #DDDDDD 1.0pt;border-right:solid #DDDDDD 1.0pt;
  padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p class=MsoNormal><span style='font-size:10.0pt'>Added support for warm-boot
  for Spectrum-2 Ethernet switch platforms.</span></p>
  </td>
 </tr>
 <tr>
  <td width=186 valign=top style='width:139.25pt;border:solid #DDDDDD 1.0pt;
  border-top:none;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p class=MsoNormal><b><span style='font-size:10.0pt'>Zero Touch Provisioning
  (ZTP)</span></b></p>
  </td>
  <td width=423 valign=top style='width:317.45pt;border-top:none;border-left:
  none;border-bottom:solid #DDDDDD 1.0pt;border-right:solid #DDDDDD 1.0pt;
  padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p class=MsoNormal><span style='font-size:10.0pt'>Zero Touch Provisioning
  (ZTP) service can be used by users to configure a fleet of switches using
  common configuration templates. Switches booting from factory default state
  should be able to communicate with remote provisioning server and download relevant
  configuration files and scripts to kick start more complex configuration
  steps. ZTP service takes user input in JSON format.</span></p>
  <p class=MsoNormal><b><span style='font-size:10.0pt'>Notes:</span></b></p>
  <p class=CellBullet><span style='font-size:9.0pt;font-family:Symbol;
  color:#76B900'>·<span style='font:7.0pt "Times New Roman"'>&nbsp; </span></span>This
  capability is disabled by default and needs to be enabled upon compilation.</p>
  <p class=CellBullet><span style='font-size:9.0pt;font-family:Symbol;
  color:#76B900'>·<span style='font:7.0pt "Times New Roman"'>&nbsp; </span></span>This
  capability is not tested on any Mellanox platforms.</p>
  <p class=MsoNormal><span style='font-size:10.0pt'>For further information,
  see </span><a href="https://github.com/Azure/SONiC/blob/master/doc/ztp/ztp.md"><span
  style='font-size:10.0pt'>https://github.com/Azure/SONiC/blob/master/doc/ztp/ztp.md</span></a></p>
  </td>
 </tr>
 <tr>
  <td width=186 valign=top style='width:139.25pt;border:solid #DDDDDD 1.0pt;
  border-top:none;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p class=MsoNormal><b><span style='font-size:10.0pt'>FRR</span></b></p>
  </td>
  <td width=423 valign=top style='width:317.45pt;border-top:none;border-left:
  none;border-bottom:solid #DDDDDD 1.0pt;border-right:solid #DDDDDD 1.0pt;
  padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p class=MsoNormal><span style='font-size:10.0pt'>Becomes the default routing
  protocol.</span></p>
  </td>
 </tr>
 <tr>
  <td width=186 valign=top style='width:139.25pt;border:solid #DDDDDD 1.0pt;
  border-top:none;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p class=MsoNormal><b><span style='font-size:10.0pt'>VXLAN VNET</span></b></p>
  </td>
  <td width=423 valign=top style='width:317.45pt;border-top:none;border-left:
  none;border-bottom:solid #DDDDDD 1.0pt;border-right:solid #DDDDDD 1.0pt;
  padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p class=MsoNormal><span style='font-size:10.0pt'>Supported VNET scale
  numbers:</span></p>
  <p class=CellBullet><span style='font-size:9.0pt;font-family:Symbol;
  color:#76B900'>·<span style='font:7.0pt "Times New Roman"'>&nbsp; </span></span>Mellanox
  Spectrum</p>
  <p class=CellBullet style='margin-left:1.0in;text-indent:-.25in'><span
  style='font-family:"Courier New"'>o<span style='font:7.0pt "Times New Roman"'>&nbsp;&nbsp;
  </span></span>VNETs: 32</p>
  <p class=CellBullet style='margin-left:1.0in;text-indent:-.25in'><span
  style='font-family:"Courier New"'>o<span style='font:7.0pt "Times New Roman"'>&nbsp;&nbsp;
  </span></span>VNET interfaces: 32</p>
  <p class=CellBullet style='margin-left:1.0in;text-indent:-.25in'><span
  style='font-family:"Courier New"'>o<span style='font:7.0pt "Times New Roman"'>&nbsp;&nbsp;
  </span></span>VNET routes: 3000</p>
  <p class=CellBullet style='margin-left:1.0in;text-indent:-.25in'><span
  style='font-family:"Courier New"'>o<span style='font:7.0pt "Times New Roman"'>&nbsp;&nbsp;
  </span></span>VNET endpoints: 512</p>
  <p class=CellBullet><span style='font-size:9.0pt;font-family:Symbol;
  color:#76B900'>·<span style='font:7.0pt "Times New Roman"'>&nbsp; </span></span>Mellanox
  Spectrum-2</p>
  <p class=MsoNormal style='margin-left:1.0in;text-indent:-.25in'><span
  style='font-size:10.0pt;font-family:"Courier New"'>o<span style='font:7.0pt "Times New Roman"'>&nbsp;&nbsp;
  </span></span><span style='font-size:10.0pt'>VNETs: 32</span></p>
  <p class=MsoNormal style='margin-left:1.0in;text-indent:-.25in'><span
  style='font-size:10.0pt;font-family:"Courier New"'>o<span style='font:7.0pt "Times New Roman"'>&nbsp;&nbsp;
  </span></span><span style='font-size:10.0pt'>VNET interfaces: 32</span></p>
  <p class=MsoNormal style='margin-left:1.0in;text-indent:-.25in'><span
  style='font-size:10.0pt;font-family:"Courier New"'>o<span style='font:7.0pt "Times New Roman"'>&nbsp;&nbsp;
  </span></span><span style='font-size:10.0pt'>VNET routes: 40000</span></p>
  <p class=MsoNormal style='margin-left:1.0in;text-indent:-.25in'><span
  style='font-size:10.0pt;font-family:"Courier New"'>o<span style='font:7.0pt "Times New Roman"'>&nbsp;&nbsp;
  </span></span><span style='font-size:10.0pt'>VNET endpoints: 4000</span></p>
  <p class=MsoNormal><span style='font-size:10.0pt'>For further information,
  see </span><a
  href="https://github.com/Azure/SONiC/blob/master/doc/vxlan/Vxlan_hld.md"><span
  style='font-size:10.0pt'>https://github.com/Azure/SONiC/blob/master/doc/vxlan/Vxlan_hld.md</span></a></p>
  </td>
 </tr>
 <tr>
  <td width=186 valign=top style='width:139.25pt;border:solid #DDDDDD 1.0pt;
  border-top:none;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p class=MsoNormal><b><span style='font-size:10.0pt'>CLI Commands: BIOS and
  CPLD Updates</span></b></p>
  </td>
  <td width=423 valign=top style='width:317.45pt;border-top:none;border-left:
  none;border-bottom:solid #DDDDDD 1.0pt;border-right:solid #DDDDDD 1.0pt;
  padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p class=MsoNormal><span style='font-size:10.0pt'>For further information,
  see </span><a
  href="https://github.com/Azure/sonic-utilities/blob/master/doc/Command-Reference.md#platform-component-firmware"><span
  style='font-size:10.0pt'>https://github.com/Azure/sonic-utilities/blob/master/doc/Command-Reference.md#platform-component-firmware</span></a></p>
  </td>
 </tr>
 <tr>
  <td width=186 valign=top style='width:139.25pt;border:solid #DDDDDD 1.0pt;
  border-top:none;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p class=MsoNormal><b><span style='font-size:10.0pt'>Configurable Drop
  Counters</span></b></p>
  </td>
  <td width=423 valign=top style='width:317.45pt;border-top:none;border-left:
  none;border-bottom:solid #DDDDDD 1.0pt;border-right:solid #DDDDDD 1.0pt;
  padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p class=MsoNormal><span style='font-size:10.0pt'>For further information,
  see </span><a
  href="https://github.com/Azure/sonic-utilities/blob/master/doc/Command-Reference.md#drop-counters"><span
  style='font-size:10.0pt'>https://github.com/Azure/sonic-utilities/blob/master/doc/Command-Reference.md#drop-counters</span></a></p>
  </td>
 </tr>
 <tr>
  <td width=186 valign=top style='width:139.25pt;border:solid #DDDDDD 1.0pt;
  border-top:none;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p class=MsoNormal><b><span style='font-size:10.0pt'>Management VRF<br>
  <br>
  </span></b></p>
  </td>
  <td width=423 valign=top style='width:317.45pt;border-top:none;border-left:
  none;border-bottom:solid #DDDDDD 1.0pt;border-right:solid #DDDDDD 1.0pt;
  padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p class=MsoNormal><span style='font-size:10.0pt'>For further information,
  see </span><a
  href="https://github.com/Azure/sonic-utilities/blob/master/doc/Command-Reference.md#management-vrf"><span
  style='font-size:10.0pt'>https://github.com/Azure/sonic-utilities/blob/master/doc/Command-Reference.md#management-vrf</span></a></p>
  </td>
 </tr>
 <tr>
  <td width=186 valign=top style='width:139.25pt;border:solid #DDDDDD 1.0pt;
  border-top:none;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p class=MsoNormal><b><span style='font-size:10.0pt'>SSD Health</span></b></p>
  </td>
  <td width=423 valign=top style='width:317.45pt;border-top:none;border-left:
  none;border-bottom:solid #DDDDDD 1.0pt;border-right:solid #DDDDDD 1.0pt;
  padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p class=MsoNormal><span style='font-size:10.0pt'>Displays switch’s SSD
  health parameter.</span></p>
  <p class=MsoNormal><span style='font-size:10.0pt'>For further information,
  see </span><a
  href="https://github.com/Azure/sonic-utilities/blob/master/doc/Command-Reference.md#show-hardware-platform"><span
  style='font-size:10.0pt'>https://github.com/Azure/sonic-utilities/blob/master/doc/Command-Reference.md#show-hardware-platform</span></a></p>
  </td>
 </tr>
 <tr>
  <td width=186 valign=top style='width:139.25pt;border:solid #DDDDDD 1.0pt;
  border-top:none;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p class=MsoNormal><b><span style='font-size:10.0pt'>Egress Mirroring and ACL
  Action Support check via SAI</span></b></p>
  </td>
  <td width=423 valign=top style='width:317.45pt;border-top:none;border-left:
  none;border-bottom:solid #DDDDDD 1.0pt;border-right:solid #DDDDDD 1.0pt;
  padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p class=MsoNormal><span style='font-size:10.0pt'>For further information,
  see </span><a
  href="https://github.com/Azure/sonic-utilities/blob/master/doc/Command-Reference.md#acl"><span
  style='font-size:10.0pt'>https://github.com/Azure/sonic-utilities/blob/master/doc/Command-Reference.md#acl</span></a></p>
  </td>
 </tr>
 <tr>
  <td width=186 valign=top style='width:139.25pt;border:solid #DDDDDD 1.0pt;
  border-top:none;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p class=MsoNormal><b><span style='font-size:10.0pt'>CPLD Update Time<br>
  <br>
  </span></b></p>
  </td>
  <td width=423 valign=top style='width:317.45pt;border-top:none;border-left:
  none;border-bottom:solid #DDDDDD 1.0pt;border-right:solid #DDDDDD 1.0pt;
  padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p class=MsoNormal><span style='font-size:10.0pt'>Reduced the CPLD update
  time to less than 10 min.</span></p>
  </td>
 </tr>
 <tr>
  <td width=186 valign=top style='width:139.25pt;border:solid #DDDDDD 1.0pt;
  border-top:none;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p class=MsoNormal><b><span style='font-size:10.0pt'>PSU Monitoring</span></b></p>
  </td>
  <td width=423 valign=top style='width:317.45pt;border-top:none;border-left:
  none;border-bottom:solid #DDDDDD 1.0pt;border-right:solid #DDDDDD 1.0pt;
  padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p class=MsoNormal><span style='font-size:10.0pt'>New PSU daemon (psud) added
  to collect PSU running status to DB.</span></p>
  <p class=MsoNormal><span style='font-size:10.0pt'>For further information,
  see </span><a
  href="https://github.com/Azure/SONiC/blob/master/doc/pmon/pmon-enhancement-design.md"><span
  style='font-size:10.0pt'>https://github.com/Azure/SONiC/blob/master/doc/pmon/pmon-enhancement-design.md</span></a></p>
  </td>
 </tr>
 <tr>
  <td width=186 valign=top style='width:139.25pt;border:solid #DDDDDD 1.0pt;
  border-top:none;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p class=MsoNormal><b><span style='font-size:10.0pt'>System EEPROM Monitoring<br>
  <br>
  </span></b></p>
  </td>
  <td width=423 valign=top style='width:317.45pt;border-top:none;border-left:
  none;border-bottom:solid #DDDDDD 1.0pt;border-right:solid #DDDDDD 1.0pt;
  padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p class=MsoNormal><span style='font-size:10.0pt'>New system EEPROM daemon
  added to fetch system EEPROM content to DB.</span></p>
  </td>
 </tr>
 <tr>
  <td width=186 valign=top style='width:139.25pt;border:solid #DDDDDD 1.0pt;
  border-top:none;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p class=MsoNormal><b><span style='font-size:10.0pt'>Configurable Daemon
  Launching in pmon</span></b></p>
  </td>
  <td width=423 valign=top style='width:317.45pt;border-top:none;border-left:
  none;border-bottom:solid #DDDDDD 1.0pt;border-right:solid #DDDDDD 1.0pt;
  padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p class=MsoNormal><span style='font-size:10.0pt'>User can control the
  launching of the daemons in pmon by editing the configuration file.</span></p>
  <p class=MsoNormal><span style='font-size:10.0pt'>For further information,
  see </span><a
  href="https://github.com/Azure/SONiC/blob/master/doc/pmon/pmon-enhancement-design.md#4-pmon-daemons-dynamically-loading"><span
  style='font-size:10.0pt'>https://github.com/Azure/SONiC/blob/master/doc/pmon/pmon-enhancement-design.md#4-pmon-daemons-dynamically-loading</span></a></p>
  </td>
 </tr>
 <tr>
  <td width=186 valign=top style='width:139.25pt;border:solid #DDDDDD 1.0pt;
  border-top:none;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p class=MsoNormal><b><span style='font-size:10.0pt'>New Platform API Support</span></b></p>
  </td>
  <td width=423 valign=top style='width:317.45pt;border-top:none;border-left:
  none;border-bottom:solid #DDDDDD 1.0pt;border-right:solid #DDDDDD 1.0pt;
  padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p class=MsoNormal><span style='font-size:10.0pt'>New Platform API is
  designed to replace the old device plugins to fetch platform device
  information.</span></p>
  <p class=MsoNormal><span style='font-size:10.0pt'>The following Platform API
  were added:</span></p>
  <p class=MsoNormal style='margin-left:.25in;text-indent:-.25in'><span
  style='font-size:10.0pt;font-family:Symbol'>·<span style='font:7.0pt "Times New Roman"'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
  </span></span><span style='font-size:10.0pt'>FAN platform API</span></p>
  <p class=MsoNormal style='margin-left:.25in;text-indent:-.25in'><span
  style='font-size:10.0pt;font-family:Symbol'>·<span style='font:7.0pt "Times New Roman"'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
  </span></span><span style='font-size:10.0pt'>PSU platform API</span></p>
  <p class=MsoNormal style='margin-left:.25in;text-indent:-.25in'><span
  style='font-size:10.0pt;font-family:Symbol'>·<span style='font:7.0pt "Times New Roman"'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
  </span></span><span style='font-size:10.0pt'>SFP platform API</span></p>
  <p class=MsoNormal style='margin-left:.25in;text-indent:-.25in'><span
  style='font-size:10.0pt;font-family:Symbol'>·<span style='font:7.0pt "Times New Roman"'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
  </span></span><span style='font-size:10.0pt'>Thermal platform API</span></p>
  <p class=MsoNormal style='margin-left:.25in;text-indent:-.25in'><span
  style='font-size:10.0pt;font-family:Symbol'>·<span style='font:7.0pt "Times New Roman"'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
  </span></span><span style='font-size:10.0pt'>Watchdog platform API</span></p>
  <p class=MsoNormal style='margin-left:.25in;text-indent:-.25in'><span
  style='font-size:10.0pt;font-family:Symbol'>·<span style='font:7.0pt "Times New Roman"'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
  </span></span><span style='font-size:10.0pt'>EEPROM platform API</span></p>
  <p class=MsoNormal style='margin-left:.25in;text-indent:-.25in'><span
  style='font-size:10.0pt;font-family:Symbol'>·<span style='font:7.0pt "Times New Roman"'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
  </span></span><span style='font-size:10.0pt'>CPLD and BIOS platform API</span></p>
  <p class=MsoNormal><span style='font-size:10.0pt'>For further information,
  see </span><a
  href="https://github.com/Azure/SONiC/blob/master/doc/platform_api/new_platform_api.md"><span
  style='font-size:10.0pt'>https://github.com/Azure/SONiC/blob/master/doc/platform_api/new_platform_api.md</span></a></p>
  </td>
 </tr>
 <tr>
  <td width=609 colspan=2 valign=top style='width:456.7pt;border:solid #DDDDDD 1.0pt;
  border-top:none;background:#cbd4e0;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p class=CellHeading align=center style='text-align:center'>Rev. SONiC 201811</p>
  </td>
 </tr>
 <tr>
  <td width=609 colspan=2 valign=top style='width:456.7pt;border:solid #DDDDDD 1.0pt;
  border-top:none;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p class=MsoNormal><span style='font-size:10.0pt'>For the complete list of
  commands that are supported in SONiC 201811, see </span><a
  href="https://github.com/Azure/sonic-utilities/blob/201911/doc/Command-Reference.md"><span
  style='font-size:10.0pt'>https://github.com/Azure/sonic-utilities/blob/201911/doc/Command-Reference.md</span></a><span
  style='font-size:10.0pt'>.</span></p>
  <p class=MsoNormal><span style='font-size:10.0pt'>Please note that as the
  Command Reference Guide is not part of 201811 branch (it was added at a later
  stage). any differences in the software behavior between 201911 and 201811
  should be specified by the Author.</span></p>
  </td>
 </tr>
 <tr>
  <td width=186 valign=top style='width:139.25pt;border:solid #DDDDDD 1.0pt;
  border-top:none;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p class=MsoNormal><b><span style='font-size:10.0pt'>MAC Address Aging</span></b></p>
  </td>
  <td width=423 valign=top style='width:317.45pt;border-top:none;border-left:
  none;border-bottom:solid #DDDDDD 1.0pt;border-right:solid #DDDDDD 1.0pt;
  padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p class=MsoNormal><span style='font-size:10.0pt'>The MAC address aging time
  can be changed by updating the &quot;orchagent&quot; configuration file.</span></p>
  </td>
 </tr>
 <tr>
  <td width=186 valign=top style='width:139.25pt;border:solid #DDDDDD 1.0pt;
  border-top:none;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p class=MsoNormal><b><span style='font-size:10.0pt'>Critical Resource
  Monitoring</span></b></p>
  </td>
  <td width=423 valign=top style='width:317.45pt;border-top:none;border-left:
  none;border-bottom:solid #DDDDDD 1.0pt;border-right:solid #DDDDDD 1.0pt;
  padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p class=MsoNormal><span style='font-size:10.0pt'>Critical Resource
  Monitoring (CRM) monitors ASIC resources' utilization by polling SAI
  attributes.</span></p>
  <p class=MsoNormal><span style='font-size:10.0pt'>For further information,
  see </span><a
  href="https://github.com/Azure/SONiC/wiki/Critical-Resource-Monitoring-High-Level-Design"><span
  style='font-size:10.0pt'>https://github.com/Azure/SONiC/wiki/Critical-Resource-Monitoring-High-Level-Design</span></a></p>
  </td>
 </tr>
 <tr>
  <td width=186 valign=top style='width:139.25pt;border:solid #DDDDDD 1.0pt;
  border-top:none;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p class=MsoNormal><b><span style='font-size:10.0pt'>PFC Watchdog</span></b></p>
  </td>
  <td width=423 valign=top style='width:317.45pt;border-top:none;border-left:
  none;border-bottom:solid #DDDDDD 1.0pt;border-right:solid #DDDDDD 1.0pt;
  padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p class=MsoNormal><span style='font-size:10.0pt'>PFC watchdog is designed to
  detect and mitigate PFC storm received for each port. PFC pause frames is
  used in lossless Ethernet to pause the link partner from sending packets.
  Such back-pressure mechanism could propagate to the whole network and cause
  the network stop forwarding traffic. PFC watchdog is to detect abnormal back-
  pressure caused by receiving excessive PFC pause frames, and mitigate such
  situation by disable PFC caused pause temporarily. PFC watchdog has three
  function blocks, i.e. detection, mitigation and restoration.</span></p>
  <p class=MsoNormal><span style='font-size:10.0pt'>For further information,
  see </span><a href="https://github.com/Azure/SONiC/wiki/PFC-Watchdog-Design"><span
  style='font-size:10.0pt'>https://github.com/Azure/SONiC/wiki/PFC-Watchdog-Design</span></a></p>
  </td>
 </tr>
 <tr>
  <td width=186 valign=top style='width:139.25pt;border:solid #DDDDDD 1.0pt;
  border-top:none;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p class=MsoNormal><b><span style='font-size:10.0pt'>IPv6 ACL</span></b></p>
  </td>
  <td width=423 valign=top style='width:317.45pt;border-top:none;border-left:
  none;border-bottom:solid #DDDDDD 1.0pt;border-right:solid #DDDDDD 1.0pt;
  padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p class=MsoNormal><span style='font-size:10.0pt'>Extends the ACL IPv4
  support within IPv6.</span></p>
  <p class=MsoNormal><span style='font-size:10.0pt'>For further information,
  see </span><a
  href="https://github.com/Azure/SONiC/blob/gh-pages/doc/ACL-enhancements-on-SONIC.docx"><span
  style='font-size:10.0pt'>https://github.com/Azure/SONiC/blob/gh-pages/doc/ACL-enhancements-on-SONIC.docx</span></a></p>
  </td>
 </tr>
 <tr>
  <td width=186 valign=top style='width:139.25pt;border:solid #DDDDDD 1.0pt;
  border-top:none;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p class=MsoNormal><b><span style='font-size:10.0pt'>BGP Neighbors</span></b></p>
  <p class=MsoNormal><b><span style='font-size:10.0pt'>(neighbor-down
  fib-accelerate)</span></b></p>
  </td>
  <td width=423 valign=top style='width:317.45pt;border-top:none;border-left:
  none;border-bottom:solid #DDDDDD 1.0pt;border-right:solid #DDDDDD 1.0pt;
  padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p class=MsoNormal><span style='font-size:10.0pt'>BGP neighbors performance
  improvements.</span></p>
  </td>
 </tr>
 <tr>
  <td width=186 valign=top style='width:139.25pt;border:solid #DDDDDD 1.0pt;
  border-top:none;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p class=MsoNormal><b><span style='font-size:10.0pt'>gRPC for Telemetry</span></b></p>
  </td>
  <td width=423 valign=top style='width:317.45pt;border-top:none;border-left:
  none;border-bottom:solid #DDDDDD 1.0pt;border-right:solid #DDDDDD 1.0pt;
  padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p class=MsoNormal><span style='font-size:10.0pt'>Implementation of gRPC for
  Telemetry data collection.</span></p>
  <p class=MsoNormal><span style='font-size:10.0pt'>For further information,
  see </span><a
  href="https://github.com/Azure/sonic-telemetry/blob/master/doc/grpc_telemetry.md"><span
  style='font-size:10.0pt'>https://github.com/Azure/sonic-telemetry/blob/master/doc/grpc_telemetry.md</span></a></p>
  </td>
 </tr>
 <tr>
  <td width=186 valign=top style='width:139.25pt;border:solid #DDDDDD 1.0pt;
  border-top:none;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p class=MsoNormal><b><span style='font-size:10.0pt'>Transceiver Sensors
  Monitoring</span></b></p>
  </td>
  <td width=423 valign=top style='width:317.45pt;border-top:none;border-left:
  none;border-bottom:solid #DDDDDD 1.0pt;border-right:solid #DDDDDD 1.0pt;
  padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p class=MsoNormal><span style='font-size:10.0pt'>Transceiver Sensors
  monitoring uses Xcvrd that is designed to fetch the transceiver and DOM
  sensor information from the eeprom, and then update the state DB with this
  information.</span></p>
  <p class=MsoNormal><span style='font-size:10.0pt'>For further information,
  see </span><a
  href="https://github.com/Azure/SONiC/blob/master/doc/xrcvd/transceiver-monitor-hld.md"><span
  style='font-size:10.0pt'>https://github.com/Azure/SONiC/blob/master/doc/xrcvd/transceiver-monitor-hld.md</span></a></p>
  </td>
 </tr>
 <tr>
  <td width=186 valign=top style='width:139.25pt;border:solid #DDDDDD 1.0pt;
  border-top:none;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p class=MsoNormal><b><span style='font-size:10.0pt'>Asymmetric Priority Flow
  Control (PFC)</span></b></p>
  </td>
  <td width=423 valign=top style='width:317.45pt;border-top:none;border-left:
  none;border-bottom:solid #DDDDDD 1.0pt;border-right:solid #DDDDDD 1.0pt;
  padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p class=MsoNormal><span style='font-size:10.0pt'>Extends default PFC
  functionality in order to add possibility for configuring different behavior
  for receiving and transmitting PFC pause frames.</span></p>
  <p class=MsoNormal><span style='font-size:10.0pt'>For further information,
  see </span><a
  href="https://github.com/Azure/SONiC/wiki/Asymmetric-PFC-High-Level-Design"><span
  style='font-size:10.0pt'>https://github.com/Azure/SONiC/wiki/Asymmetric-PFC-High-Level-Design</span></a></p>
  </td>
 </tr>
 <tr>
  <td width=186 valign=top style='width:139.25pt;border:solid #DDDDDD 1.0pt;
  border-top:none;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p class=MsoNormal><b><span style='font-size:10.0pt'>Routing Stack Graceful
  Restart</span></b></p>
  </td>
  <td width=423 valign=top style='width:317.45pt;border-top:none;border-left:
  none;border-bottom:solid #DDDDDD 1.0pt;border-right:solid #DDDDDD 1.0pt;
  padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p class=MsoNormal><span style='font-size:10.0pt'>Gracefully restarts the
  Routing Stack (BGP) as part of the warm-boot functionality. This allows a BGP
  speaker to express its ability to preserve forwarding state during BGP
  restart.</span></p>
  <p class=MsoNormal><span style='font-size:10.0pt'>For further information,
  see </span><a
  href="https://github.com/Azure/SONiC/blob/dcac72377f23521a394694214678ea4450f6f70a/doc/routing-warm-reboot/"><span
  style='font-size:10.0pt'>https://github.com/Azure/SONiC/blob/dcac72377f23521a394694214678ea4450f6f70a/doc/routing-warm-reboot/</span></a><span
  style='font-size:10.0pt'> </span><a
  href="http://Routing_Warm_Reboot.md#4-bgp-graceful-restart-overview"><span
  style='font-size:10.0pt'>Routing_Warm_Reboot.md#4-bgp-graceful-restart-overview</span></a></p>
  </td>
 </tr>
 <tr>
  <td width=186 valign=top style='width:139.25pt;border:solid #DDDDDD 1.0pt;
  border-top:none;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p class=MsoNormal><b><span style='font-size:10.0pt'>Incremental Config (IP,
  LAG, Port admin)</span></b></p>
  </td>
  <td width=423 valign=top style='width:317.45pt;border-top:none;border-left:
  none;border-bottom:solid #DDDDDD 1.0pt;border-right:solid #DDDDDD 1.0pt;
  padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p class=MsoNormal><span style='font-size:10.0pt'>Enhances Command Line
  Interface to allow run-time configuration of the different items.</span></p>
  <p class=MsoNormal><span style='font-size:10.0pt'>For more information, see </span><a
  href="https://github.com/Azure/sonic-utilities/blob/master/doc/Command-Reference.md"><span
  style='font-size:10.0pt'>https://github.com/Azure/sonic-utilities/blob/master/doc/Command-Reference.md</span></a></p>
  </td>
 </tr>
 <tr>
  <td width=186 valign=top style='width:139.25pt;border:solid #DDDDDD 1.0pt;
  border-top:none;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p class=MsoNormal><b><span style='font-size:10.0pt'>IP-in-IP v6</span></b></p>
  </td>
  <td width=423 valign=top style='width:317.45pt;border-top:none;border-left:
  none;border-bottom:solid #DDDDDD 1.0pt;border-right:solid #DDDDDD 1.0pt;
  padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p class=MsoNormal><span style='font-size:10.0pt'>Extends IP-in-IP support
  with IPv6 and all 4 combinations of IPv4 and IPv6.</span></p>
  </td>
 </tr>
 <tr>
  <td width=186 valign=top style='width:139.25pt;border:solid #DDDDDD 1.0pt;
  border-top:none;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p class=MsoNormal><b><span style='font-size:10.0pt'>PFC Watermark Counters</span></b></p>
  </td>
  <td width=423 valign=top style='width:317.45pt;border-top:none;border-left:
  none;border-bottom:solid #DDDDDD 1.0pt;border-right:solid #DDDDDD 1.0pt;
  padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p class=MsoNormal><span style='font-size:10.0pt'>PFC Watermark counters are
  now available in both CLI and gRPC. A periodic read is performed via the
  Telemetry Agent, and on demand via the CLI for debug purposes.</span></p>
  <p class=MsoNormal><span style='font-size:10.0pt'>For further information,
  see </span><a
  href="https://github.com/Azure/SONiC/blob/master/doc/buffer-watermark/watermarks_HLD.md"><span
  style='font-size:10.0pt'>https://github.com/Azure/SONiC/blob/master/doc/buffer-watermark/watermarks_HLD.md</span></a></p>
  </td>
 </tr>
 <tr>
  <td width=186 valign=top style='width:139.25pt;border:solid #DDDDDD 1.0pt;
  border-top:none;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p class=MsoNormal><b><span style='font-size:10.0pt'>SONiC Warm Reboot</span></b></p>
  </td>
  <td width=423 valign=top style='width:317.45pt;border-top:none;border-left:
  none;border-bottom:solid #DDDDDD 1.0pt;border-right:solid #DDDDDD 1.0pt;
  padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p class=MsoNormal><span style='font-size:10.0pt'>Restarts and upgrades SONiC
  software without impacting the data plane. This process takes &lt; 1 second.</span></p>
  <p class=MsoNormal><span style='font-size:10.0pt'>For further information,
  see </span><a
  href="https://github.com/Azure/SONiC/blob/master/doc/warm-reboot/SONiC_Warmboot.md"><span
  style='font-size:10.0pt'>https://github.com/Azure/SONiC/blob/master/doc/warm-reboot/SONiC_Warmboot.md</span></a></p>
  </td>
 </tr>
 <tr>
  <td width=186 valign=top style='width:139.25pt;border:solid #DDDDDD 1.0pt;
  border-top:none;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p class=MsoNormal><b><span style='font-size:10.0pt'>Configurable ASIC Table
  Sizes</span></b></p>
  </td>
  <td width=423 valign=top style='width:317.45pt;border-top:none;border-left:
  none;border-bottom:solid #DDDDDD 1.0pt;border-right:solid #DDDDDD 1.0pt;
  padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p class=MsoNormal><span style='font-size:10.0pt'>By adding or updating the
  macro definitions in </span><span style='font-size:10.0pt;font-family:Consolas;
  color:black'>/usr/share/sonic/device/{platform name}/{sku name}/sai.profile</span><span
  style='font-size:10.0pt'>, the </span><span style='font-size:10.0pt;
  font-family:Consolas;color:black'>&quot;fdb&quot;</span><span
  style='font-size:10.0pt'>, </span><span style='font-size:10.0pt;font-family:
  Consolas;color:black'>&quot;ip route&quot;</span><span style='font-size:10.0pt'>,
  and </span><span style='font-size:10.0pt;font-family:Consolas;color:black'>&quot;neighbor&quot;</span><span
  style='font-size:10.0pt'> table sizes could be updated based on the need.</span></p>
  <p class=MsoNormal style='margin-left:.25in;text-indent:-.25in'><span
  style='font-size:10.0pt;font-family:Symbol'>·<span style='font:7.0pt "Times New Roman"'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
  </span></span><span style='font-size:10.0pt'>SAI_FDB_TABLE_SIZE=32768</span></p>
  <p class=MsoNormal style='margin-left:.25in;text-indent:-.25in'><span
  style='font-size:10.0pt;font-family:Symbol'>·<span style='font:7.0pt "Times New Roman"'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
  </span></span><span style='font-size:10.0pt'>SAI_IPV4_ROUTE_TABLE_SIZE=131072</span></p>
  <p class=MsoNormal style='margin-left:.25in;text-indent:-.25in'><span
  style='font-size:10.0pt;font-family:Symbol'>·<span style='font:7.0pt "Times New Roman"'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
  </span></span><span style='font-size:10.0pt'>SAI_IPV6_ROUTE_TABLE_SIZE=16384</span></p>
  <p class=MsoNormal style='margin-left:.25in;text-indent:-.25in'><span
  style='font-size:10.0pt;font-family:Symbol'>·<span style='font:7.0pt "Times New Roman"'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
  </span></span><span style='font-size:10.0pt'>SAI_IPV4_NEIGHBOR_TABLE_SIZE=16384</span></p>
  <p class=MsoNormal style='margin-left:.25in;text-indent:-.25in'><span
  style='font-size:10.0pt;font-family:Symbol'>·<span style='font:7.0pt "Times New Roman"'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
  </span></span><span style='font-size:10.0pt'>SAI_IPV6_NEIGHBOR_TABLE_SIZE=12288</span></p>
  <p class=MsoNormal><b><span style='font-size:10.0pt'>Note:</span></b><span
  style='font-size:10.0pt'> Please contact Mellanox before updating the default
  sizes in the table.</span></p>
  </td>
 </tr>
</table>

### Customer-Affecting Changes

<table class=ScrollTableNormal border=1 cellspacing=0 cellpadding=0 width="100%"
 style='width:100.0%;border-collapse:collapse;border:none'>
 <thead>
  <tr>
   <td valign=top style='border:solid #DDDDDD 1.0pt;background:#cbd4e0;
   padding:1.5pt 1.5pt 1.0pt 1.5pt'>
   <p class=CellHeading align=center style='text-align:center'><b>Feature/Change</b></p>
   </td>
   <td valign=top style='border:solid #DDDDDD 1.0pt;border-left:none;
   background:#cbd4e0;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
   <p class=CellHeading align=center style='text-align:center'><b>Description</b></p>
   </td>
  </tr>
 </thead>
 <tr>
  <td colspan=2 valign=top style='border:solid #DDDDDD 1.0pt;border-top:none;
  background:#cbd4e0;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p class=CellHeading align=center style='text-align:center'>Rev. SONiC
  201911_MUR3</p>
  </td>
 </tr>
 <tr>
  <td valign=top style='border:solid #DDDDDD 1.0pt;border-top:none;padding:
  1.5pt 1.5pt 1.0pt 1.5pt'>
  <p class=MsoNormal><span style='font-size:10.0pt'>DHCP</span></p>
  </td>
  <td valign=top style='border-top:none;border-left:none;border-bottom:solid #DDDDDD 1.0pt;
  border-right:solid #DDDDDD 1.0pt;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p class=MsoNormal><span style='font-size:10.0pt'>DHCP trap can only be
  enabled on Top of Rack (ToR) Router. To enable it on a non-ToR Router, the
  user must change the default COPP trap configuration.</span></p>
  <p class=MsoNormal><span style='font-size:10.0pt'>For further information,
  see&nbsp;</span><a
  href="https://github.com/Azure/sonic-swss/blob/201911/doc/Configuration.md"><span
  style='font-size:10.0pt'>https://github.com/Azure/sonic-swss/blob/201911/doc/Configuration.md</span></a></p>
  </td>
 </tr>
 <tr>
  <td valign=top style='border:solid #DDDDDD 1.0pt;border-top:none;padding:
  1.5pt 1.5pt 1.0pt 1.5pt'>
  <p class=MsoNormal><span style='font-size:10.0pt'>CLI Commands:&nbsp;Features</span></p>
  </td>
  <td valign=top style='border-top:none;border-left:none;border-bottom:solid #DDDDDD 1.0pt;
  border-right:solid #DDDDDD 1.0pt;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p class=MsoNormal><span style='font-size:10.0pt'>The &quot;Feature&quot; CLI
  command has been changed.</span></p>
  <p class=MsoNormal style='margin-left:.25in;text-indent:-.25in'><span
  style='font-size:10.0pt;font-family:Symbol'>·<span style='font:7.0pt "Times New Roman"'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
  </span></span><span style='font-size:10.0pt'>To see all the available
  features command options, execute:<br>
  </span><span style='font-size:10.0pt;font-family:Consolas;color:black'>‘show
  feature status’</span></p>
  <p class=MsoNormal style='margin-left:.25in;text-indent:-.25in'><span
  style='font-size:10.0pt;font-family:Symbol'>·<span style='font:7.0pt "Times New Roman"'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
  </span></span><span style='font-size:10.0pt'>To change a feature state, execute:<br>
  </span><span style='font-size:10.0pt;font-family:Consolas;color:black'>‘config
  feature state &lt;feature_name&gt; &lt;enabled/disbaled&gt;’</span></p>
  <p class=MsoNormal><b><span style='font-size:10.0pt'>Note:</span></b><span
  style='font-size:10.0pt'> Feature CLI changes affect the way WJH is enabled
  as well as any other feature.</span></p>
  </td>
 </tr>
</table>

## Bug Fixes History

This section provides only a list of bugs fixed by Mellanox only. For additional bugs reported that are handled by both Mellanox and the community please refer to github. 

| Item # | RM # | Issue |
| ------ | ---- | ----- |
| 1. | 2082958 | **Description:** Applying an ACL rule with the REDIRECT_ACTION attribute fails with errors.<br />**Keywords:** ACL<br />**Discovered in Version:** SONiC 201911_MUR3<br />**Fixed in Version:** SONiC 201911_MUR4 |
| 2. | 2269143 | **Description:** In some cases, error may occur when using MCION query on a module with types "sfp_rx_los_soft_en" or "sfp_tx_fault_soft_en" that enable rx_los/tx_fault read from the memory map.<br />**Keywords:** Modules<br />**Discovered in Version:** SONiC 201911_MUR3<br />**Fixed in Version:** SONiC 201911_MUR4 |
| 3. | 2268678 | **Description:** MSTP state is not updated correctly for ports in certain VLAG scenarios.<br />**Keywords:** LAG<br />**Discovered in Version:** SONiC 201911_MUR3<br />**Fixed in Version:** SONiC 201911_MUR4 |
| 4. | 2036664 | **Description:** "show ip interface" shows the phantom PortChannel interface that was configured following a configuration reload of a non-saved configuration.<br />**Keywords:** Portchannel<br />**Discovered in Version:** SONiC 201911<br />**Fixed in Version:** SONiC 201911_MUR4 |
| ... | ... | ... |
