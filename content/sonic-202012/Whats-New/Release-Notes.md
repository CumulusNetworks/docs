---
title: Release Notes
author: Cumulus Networks
weight: 20
product: SONiC
version: 201911_MUR5
siteSlug: sonic
---

## Release Notes Update History

| Revision | Date | Description |
| -------- | ---- | ----------- |
| Rev 1.0 | May 1, 2021 | Initial release of these release notes. |

## Overview

SONiC is an open source network operating system based on Linux that runs on switches from multiple vendors and ASICs. SONiC offers a full suite of network functionality, like BGP and RDMA, that has been production-hardened in the data centers of some of the largest cloud-service providers. It offers teams the flexibility to create the network solutions they need while leveraging the collective strength of a large ecosystem and community.

<!-- These are the release notes for SONiC software on NVIDIA® Mellanox Spectrum® based switches. -->

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

## Bugs Fixed in this Version

This section provides only a list of bugs fixed by Mellanox only in this version. For a list of old fixes, please see Bug Fix History.

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
   <p><b>Speed [GbE]</b></p>
   </td>
   <td rowspan=2 valign=top style='border:solid #DDDDDD 1.0pt;border-left:none;
   background:#cbd4e0;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
   <p><b>AutoNeg</b></p>
   </td>
   <td colspan=3 valign=top style='border:solid #DDDDDD 1.0pt;border-left:none;
   background:#cbd4e0;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
   <p><b>Force</b></p>
   </td>
   <td rowspan=2 valign=top style='border:solid #DDDDDD 1.0pt;border-left:none;
   background:#cbd4e0;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
   <p><b>Cable / Modules</b></p>
   </td>
   <td rowspan=2 valign=top style='border:solid #DDDDDD 1.0pt;border-left:none;
   background:#cbd4e0;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
   <p><b>Cable Length [m]</b></p>
   </td>
 </tr>
 <tr>
   <td valign=top style='border-top:none;border-left:none;border-bottom:solid #DDDDDD 1.0pt;
  border-right:solid #DDDDDD 1.0pt;background:#cbd4e0;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p>RS FEC</p>
  </td>
  <td valign=top style='border-top:none;border-left:none;border-bottom:solid #DDDDDD 1.0pt;
  border-right:solid #DDDDDD 1.0pt;background:#cbd4e0;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p>FC FEC</p>
  </td>
  <td valign=top style='border-top:none;border-left:none;border-bottom:solid #DDDDDD 1.0pt;
  border-right:solid #DDDDDD 1.0pt;background:#cbd4e0;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p>NO FEC</p>
  </td>
 </tr>
 </thead>
 <tr>
  <td rowspan=2 valign=top style='border:solid #DDDDDD 1.0pt;border-top:none;
  padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p>400</p>
  </td>
  <td rowspan=2 valign=top style='border-top:none;border-left:none;border-bottom:
  solid #DDDDDD 1.0pt;border-right:solid #DDDDDD 1.0pt;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p>&#9989;</p>
  </td>
  <td rowspan=2 valign=top style='border-top:none;border-left:none;border-bottom:
  solid #DDDDDD 1.0pt;border-right:solid #DDDDDD 1.0pt;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p>&#9989;</p>
  <p>&nbsp;</p>
  </td>
  <td rowspan=2 valign=top style='border-top:none;border-left:none;border-bottom:
  solid #DDDDDD 1.0pt;border-right:solid #DDDDDD 1.0pt;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p>&#10008;</p>
  </td>
  <td rowspan=2 valign=top style='border-top:none;border-left:none;border-bottom:
  solid #DDDDDD 1.0pt;border-right:solid #DDDDDD 1.0pt;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p>&#10008;</p>
  </td>
  <td valign=top style='border-top:none;border-left:none;border-bottom:solid #DDDDDD 1.0pt;
  border-right:solid #DDDDDD 1.0pt;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p>Optics</p>
  </td>
  <td valign=top style='border-top:none;border-left:none;border-bottom:solid #DDDDDD 1.0pt;
  border-right:solid #DDDDDD 1.0pt;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p>Up to 5</p>
  </td>
 </tr>
 <tr>
  <td valign=top style='border-top:none;border-left:none;border-bottom:solid #DDDDDD 1.0pt;
  border-right:solid #DDDDDD 1.0pt;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p>Copper</p>
  </td>
  <td valign=top style='border-top:none;border-left:none;border-bottom:solid #DDDDDD 1.0pt;
  border-right:solid #DDDDDD 1.0pt;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p>Up to 2.5</p>
  </td>
 </tr>
 <tr>
  <td rowspan=2 valign=top style='border:solid #DDDDDD 1.0pt;border-top:none;
  padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p>200/<br>
  100 2x/<br>
  50 1x (PAM4)</p>
  </td>
  <td rowspan=2 valign=top style='border-top:none;border-left:none;border-bottom:
  solid #DDDDDD 1.0pt;border-right:solid #DDDDDD 1.0pt;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p>&#9989;</p>
  <p>&nbsp;</p>
  </td>
  <td rowspan=2 valign=top style='border-top:none;border-left:none;border-bottom:
  solid #DDDDDD 1.0pt;border-right:solid #DDDDDD 1.0pt;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p>&#9989;</p>
  <p>&nbsp;</p>
  </td>
  <td rowspan=2 valign=top style='border-top:none;border-left:none;border-bottom:
  solid #DDDDDD 1.0pt;border-right:solid #DDDDDD 1.0pt;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p>&#10008;</p>
  </td>
  <td rowspan=2 valign=top style='border-top:none;border-left:none;border-bottom:
  solid #DDDDDD 1.0pt;border-right:solid #DDDDDD 1.0pt;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p>&#10008;</p>
  </td>
  <td valign=top style='border-top:none;border-left:none;border-bottom:solid #DDDDDD 1.0pt;
  border-right:solid #DDDDDD 1.0pt;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p>Optic</p>
  </td>
  <td valign=top style='border-top:none;border-left:none;border-bottom:solid #DDDDDD 1.0pt;
  border-right:solid #DDDDDD 1.0pt;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p>Up to 5</p>
  </td>
 </tr>
 <tr>
  <td valign=top style='border-top:none;border-left:none;border-bottom:solid #DDDDDD 1.0pt;
  border-right:solid #DDDDDD 1.0pt;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p>Copper</p>
  </td>
  <td valign=top style='border-top:none;border-left:none;border-bottom:solid #DDDDDD 1.0pt;
  border-right:solid #DDDDDD 1.0pt;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p>Up to 2.5</p>
  </td>
 </tr>
 <tr>
  <td rowspan=2 valign=top style='border:solid #DDDDDD 1.0pt;border-top:none;
  padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p>100 (NRZ)</p>
  </td>
  <td rowspan=2 valign=top style='border-top:none;border-left:none;border-bottom:
  solid #DDDDDD 1.0pt;border-right:solid #DDDDDD 1.0pt;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p>&#9989;</p>
  <p>&nbsp;</p>
  </td>
  <td rowspan=2 valign=top style='border-top:none;border-left:none;border-bottom:
  solid #DDDDDD 1.0pt;border-right:solid #DDDDDD 1.0pt;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p>&#9989;</p>
  <p>&nbsp;</p>
  </td>
  <td rowspan=2 valign=top style='border-top:none;border-left:none;border-bottom:
  solid #DDDDDD 1.0pt;border-right:solid #DDDDDD 1.0pt;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p>&#10008;</p>
  <p>&nbsp;</p>
  </td>
  <td rowspan=2 valign=top style='border-top:none;border-left:none;border-bottom:
  solid #DDDDDD 1.0pt;border-right:solid #DDDDDD 1.0pt;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p>&#9989;</p>
  </td>
  <td valign=top style='border-top:none;border-left:none;border-bottom:solid #DDDDDD 1.0pt;
  border-right:solid #DDDDDD 1.0pt;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p>Optic</p>
  </td>
  <td valign=top style='border-top:none;border-left:none;border-bottom:solid #DDDDDD 1.0pt;
  border-right:solid #DDDDDD 1.0pt;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p>Up to 100</p>
  </td>
 </tr>
 <tr>
  <td valign=top style='border-top:none;border-left:none;border-bottom:solid #DDDDDD 1.0pt;
  border-right:solid #DDDDDD 1.0pt;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p>Copper</p>
  </td>
  <td valign=top style='border-top:none;border-left:none;border-bottom:solid #DDDDDD 1.0pt;
  border-right:solid #DDDDDD 1.0pt;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p>Up to 5</p>
  </td>
 </tr>
 <tr>
  <td rowspan=2 valign=top style='border:solid #DDDDDD 1.0pt;border-top:none;
  padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p>25/50 (NRZ)</p>
  </td>
  <td rowspan=2 valign=top style='border-top:none;border-left:none;border-bottom:
  solid #DDDDDD 1.0pt;border-right:solid #DDDDDD 1.0pt;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p>&#9989;</p>
  <p>&nbsp;</p>
  </td>
  <td rowspan=2 valign=top style='border-top:none;border-left:none;border-bottom:
  solid #DDDDDD 1.0pt;border-right:solid #DDDDDD 1.0pt;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p>&#9989;</p>
  <p>&nbsp;</p>
  </td>
  <td rowspan=2 valign=top style='border-top:none;border-left:none;border-bottom:
  solid #DDDDDD 1.0pt;border-right:solid #DDDDDD 1.0pt;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p>&#9989;</p>
  </td>
  <td rowspan=2 valign=top style='border-top:none;border-left:none;border-bottom:
  solid #DDDDDD 1.0pt;border-right:solid #DDDDDD 1.0pt;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p>&#9989;</p>
  <p>&nbsp;</p>
  </td>
  <td valign=top style='border-top:none;border-left:none;border-bottom:solid #DDDDDD 1.0pt;
  border-right:solid #DDDDDD 1.0pt;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p>Optic</p>
  </td>
  <td valign=top style='border-top:none;border-left:none;border-bottom:solid #DDDDDD 1.0pt;
  border-right:solid #DDDDDD 1.0pt;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p>Up to 100</p>
  </td>
 </tr>
 <tr>
  <td valign=top style='border-top:none;border-left:none;border-bottom:solid #DDDDDD 1.0pt;
  border-right:solid #DDDDDD 1.0pt;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p>Copper</p>
  </td>
  <td valign=top style='border-top:none;border-left:none;border-bottom:solid #DDDDDD 1.0pt;
  border-right:solid #DDDDDD 1.0pt;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p>Up to 5</p>
  </td>
 </tr>
 <tr>
  <td rowspan=2 valign=top style='border:solid #DDDDDD 1.0pt;border-top:none;
  padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p>10/40</p>
  </td>
  <td rowspan=2 valign=top style='border-top:none;border-left:none;border-bottom:
  solid #DDDDDD 1.0pt;border-right:solid #DDDDDD 1.0pt;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p>&#9989;</p>
  </td>
  <td rowspan=2 valign=top style='border-top:none;border-left:none;border-bottom:
  solid #DDDDDD 1.0pt;border-right:solid #DDDDDD 1.0pt;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p>&#10008;</p>
  </td>
  <td rowspan=2 valign=top style='border-top:none;border-left:none;border-bottom:
  solid #DDDDDD 1.0pt;border-right:solid #DDDDDD 1.0pt;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p>&#9989;</p>
  </td>
  <td rowspan=2 valign=top style='border-top:none;border-left:none;border-bottom:
  solid #DDDDDD 1.0pt;border-right:solid #DDDDDD 1.0pt;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p>&#9989;</p>
  </td>
  <td valign=top style='border-top:none;border-left:none;border-bottom:solid #DDDDDD 1.0pt;
  border-right:solid #DDDDDD 1.0pt;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p>Optic</p>
  </td>
  <td valign=top style='border-top:none;border-left:none;border-bottom:solid #DDDDDD 1.0pt;
  border-right:solid #DDDDDD 1.0pt;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p>Up to 100</p>
  </td>
 </tr>
 <tr>
  <td valign=top style='border-top:none;border-left:none;border-bottom:solid #DDDDDD 1.0pt;
  border-right:solid #DDDDDD 1.0pt;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p>Copper</p>
  </td>
  <td valign=top style='border-top:none;border-left:none;border-bottom:solid #DDDDDD 1.0pt;
  border-right:solid #DDDDDD 1.0pt;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p>Up to 5</p>
  </td>
 </tr>
 <tr>
  <td valign=top style='border:solid #DDDDDD 1.0pt;border-top:none;padding:
  1.5pt 1.5pt 1.0pt 1.5pt'>
  <p>1</p>
  </td>
  <td valign=top style='border-top:none;border-left:none;border-bottom:solid #DDDDDD 1.0pt;
  border-right:solid #DDDDDD 1.0pt;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p>&#9989;</p>
  </td>
  <td valign=top style='border-top:none;border-left:none;border-bottom:solid #DDDDDD 1.0pt;
  border-right:solid #DDDDDD 1.0pt;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p>&#10008;</p>
  </td>
  <td valign=top style='border-top:none;border-left:none;border-bottom:solid #DDDDDD 1.0pt;
  border-right:solid #DDDDDD 1.0pt;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p>&#10008;</p>
  </td>
  <td valign=top style='border-top:none;border-left:none;border-bottom:solid #DDDDDD 1.0pt;
  border-right:solid #DDDDDD 1.0pt;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p>&#9989;</p>
  </td>
  <td valign=top style='border-top:none;border-left:none;border-bottom:solid #DDDDDD 1.0pt;
  border-right:solid #DDDDDD 1.0pt;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p>Optic/Copper</p>
  </td>
  <td valign=top style='border-top:none;border-left:none;border-bottom:solid #DDDDDD 1.0pt;
  border-right:solid #DDDDDD 1.0pt;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p>Up to 5</p>
  </td>
 </tr>
</table>

### Mellanox Spectrum®-3 SN4600C Supported Port Speeds

<table border=1 cellspacing=0 cellpadding=0 width="100%"
 style='width:100.0%;border-collapse:collapse;border:none'>
  <tr>
   <td rowspan=2 valign=top style='border:solid #DDDDDD 1.0pt;background:#cbd4e0;
   padding:1.5pt 1.5pt 1.0pt 1.5pt'>
   <p><b>Speed [GbE]</b></p>
   </td>
   <td rowspan=2 valign=top style='border:solid #DDDDDD 1.0pt;border-left:none;
   background:#cbd4e0;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
   <p><b>AutoNeg</b></p>
   </td>
   <td colspan=3 valign=top style='border:solid #DDDDDD 1.0pt;border-left:none;
   background:#cbd4e0;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
   <p><b>Force</b></p>
   </td>
   <td rowspan=2 valign=top style='border:solid #DDDDDD 1.0pt;border-left:none;
   background:#cbd4e0;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
   <p><b>Cable / Modules</b></p>
   </td>
   <td rowspan=2 valign=top style='border:solid #DDDDDD 1.0pt;border-left:none;
   background:#cbd4e0;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
   <p><b>Cable Length [m]</b></p>
   </td>
 </tr>
 <tr>
   <td valign=top style='border-top:none;border-left:none;border-bottom:solid #DDDDDD 1.0pt;
  border-right:solid #DDDDDD 1.0pt;background:#cbd4e0;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p>RS FEC</p>
  </td>
  <td valign=top style='border-top:none;border-left:none;border-bottom:solid #DDDDDD 1.0pt;
  border-right:solid #DDDDDD 1.0pt;background:#cbd4e0;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p>FC FEC</p>
  </td>
  <td valign=top style='border-top:none;border-left:none;border-bottom:solid #DDDDDD 1.0pt;
  border-right:solid #DDDDDD 1.0pt;background:#cbd4e0;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p>NO FEC</p>
  </td>
 </tr>
 </thead>
 <tr>
  <td rowspan=2 valign=top style='border:solid #DDDDDD 1.0pt;border-top:none;
  padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p>100 (NRZ)</p>
  </td>
  <td rowspan=2 valign=top style='border-top:none;border-left:none;border-bottom:
  solid #DDDDDD 1.0pt;border-right:solid #DDDDDD 1.0pt;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p>&#9989;</p>
  <p>&nbsp;</p>
  </td>
  <td rowspan=2 valign=top style='border-top:none;border-left:none;border-bottom:
  solid #DDDDDD 1.0pt;border-right:solid #DDDDDD 1.0pt;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p>&#9989;</p>
  <p>&nbsp;</p>
  </td>
  <td rowspan=2 valign=top style='border-top:none;border-left:none;border-bottom:
  solid #DDDDDD 1.0pt;border-right:solid #DDDDDD 1.0pt;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p>&#10008;</p>
  <p>&nbsp;</p>
  </td>
  <td rowspan=2 valign=top style='border-top:none;border-left:none;border-bottom:
  solid #DDDDDD 1.0pt;border-right:solid #DDDDDD 1.0pt;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p>&#9989;</p>
  </td>
  <td valign=top style='border-top:none;border-left:none;border-bottom:solid #DDDDDD 1.0pt;
  border-right:solid #DDDDDD 1.0pt;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p>Optic</p>
  </td>
  <td valign=top style='border-top:none;border-left:none;border-bottom:solid #DDDDDD 1.0pt;
  border-right:solid #DDDDDD 1.0pt;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p>Up to 100</p>
  </td>
 </tr>
 <tr>
  <td valign=top style='border-top:none;border-left:none;border-bottom:solid #DDDDDD 1.0pt;
  border-right:solid #DDDDDD 1.0pt;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p>Copper</p>
  </td>
  <td valign=top style='border-top:none;border-left:none;border-bottom:solid #DDDDDD 1.0pt;
  border-right:solid #DDDDDD 1.0pt;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p>Up to 3</p>
  </td>
 </tr>
 <tr>
  <td rowspan=2 valign=top style='border:solid #DDDDDD 1.0pt;border-top:none;
  padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p>25/50 (NRZ)</p>
  </td>
  <td rowspan=2 valign=top style='border-top:none;border-left:none;border-bottom:
  solid #DDDDDD 1.0pt;border-right:solid #DDDDDD 1.0pt;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p>&#9989;</p>
  <p>&nbsp;</p>
  </td>
  <td rowspan=2 valign=top style='border-top:none;border-left:none;border-bottom:
  solid #DDDDDD 1.0pt;border-right:solid #DDDDDD 1.0pt;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p>&#9989;</p>
  <p>&nbsp;</p>
  </td>
  <td rowspan=2 valign=top style='border-top:none;border-left:none;border-bottom:
  solid #DDDDDD 1.0pt;border-right:solid #DDDDDD 1.0pt;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p>&#9989;</p>
  </td>
  <td rowspan=2 valign=top style='border-top:none;border-left:none;border-bottom:
  solid #DDDDDD 1.0pt;border-right:solid #DDDDDD 1.0pt;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p>&#9989;</p>
  <p>&nbsp;</p>
  </td>
  <td valign=top style='border-top:none;border-left:none;border-bottom:solid #DDDDDD 1.0pt;
  border-right:solid #DDDDDD 1.0pt;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p>Optic</p>
  </td>
  <td valign=top style='border-top:none;border-left:none;border-bottom:solid #DDDDDD 1.0pt;
  border-right:solid #DDDDDD 1.0pt;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p>Up to 100</p>
  </td>
 </tr>
 <tr>
  <td valign=top style='border-top:none;border-left:none;border-bottom:solid #DDDDDD 1.0pt;
  border-right:solid #DDDDDD 1.0pt;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p>Copper</p>
  </td>
  <td valign=top style='border-top:none;border-left:none;border-bottom:solid #DDDDDD 1.0pt;
  border-right:solid #DDDDDD 1.0pt;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p>Up to 5</p>
  </td>
 </tr>
 <tr>
  <td rowspan=2 valign=top style='border:solid #DDDDDD 1.0pt;border-top:none;
  padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p>10/40</p>
  </td>
  <td rowspan=2 valign=top style='border-top:none;border-left:none;border-bottom:
  solid #DDDDDD 1.0pt;border-right:solid #DDDDDD 1.0pt;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p>&#9989;</p>
  </td>
  <td rowspan=2 valign=top style='border-top:none;border-left:none;border-bottom:
  solid #DDDDDD 1.0pt;border-right:solid #DDDDDD 1.0pt;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p>&#10008;</p>
  </td>
  <td rowspan=2 valign=top style='border-top:none;border-left:none;border-bottom:
  solid #DDDDDD 1.0pt;border-right:solid #DDDDDD 1.0pt;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p>&#9989;</p>
  </td>
  <td rowspan=2 valign=top style='border-top:none;border-left:none;border-bottom:
  solid #DDDDDD 1.0pt;border-right:solid #DDDDDD 1.0pt;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p>&#9989;</p>
  </td>
  <td valign=top style='border-top:none;border-left:none;border-bottom:solid #DDDDDD 1.0pt;
  border-right:solid #DDDDDD 1.0pt;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p>Optic</p>
  </td>
  <td valign=top style='border-top:none;border-left:none;border-bottom:solid #DDDDDD 1.0pt;
  border-right:solid #DDDDDD 1.0pt;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p>Up to 100</p>
  </td>
 </tr>
 <tr>
  <td valign=top style='border-top:none;border-left:none;border-bottom:solid #DDDDDD 1.0pt;
  border-right:solid #DDDDDD 1.0pt;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p>Copper</p>
  </td>
  <td valign=top style='border-top:none;border-left:none;border-bottom:solid #DDDDDD 1.0pt;
  border-right:solid #DDDDDD 1.0pt;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p>Up to 3</p>
  </td>
 </tr>
 <tr>
  <td valign=top style='border:solid #DDDDDD 1.0pt;border-top:none;padding:
  1.5pt 1.5pt 1.0pt 1.5pt'>
  <p>1</p>
  </td>
  <td valign=top style='border-top:none;border-left:none;border-bottom:solid #DDDDDD 1.0pt;
  border-right:solid #DDDDDD 1.0pt;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p>&#9989;</p>
  </td>
  <td valign=top style='border-top:none;border-left:none;border-bottom:solid #DDDDDD 1.0pt;
  border-right:solid #DDDDDD 1.0pt;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p>&#10008;</p>
  </td>
  <td valign=top style='border-top:none;border-left:none;border-bottom:solid #DDDDDD 1.0pt;
  border-right:solid #DDDDDD 1.0pt;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p>&#10008;</p>
  </td>
  <td valign=top style='border-top:none;border-left:none;border-bottom:solid #DDDDDD 1.0pt;
  border-right:solid #DDDDDD 1.0pt;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p>&#9989;</p>
  </td>
  <td valign=top style='border-top:none;border-left:none;border-bottom:solid #DDDDDD 1.0pt;
  border-right:solid #DDDDDD 1.0pt;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p>Optic/Copper</p>
  </td>
  <td valign=top style='border-top:none;border-left:none;border-bottom:solid #DDDDDD 1.0pt;
  border-right:solid #DDDDDD 1.0pt;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p>Up to 5</p>
  </td>
 </tr>
</table>

### Mellanox Spectrum®-2 SN3800 Series Supported Port Speeds

<table border=1 cellspacing=0 cellpadding=0 width="100%"
 style='width:100.0%;border-collapse:collapse;border:none'>
  <tr>
   <td rowspan=2 valign=top style='border:solid #DDDDDD 1.0pt;background:#cbd4e0;
   padding:1.5pt 1.5pt 1.0pt 1.5pt'>
   <p><b>Speed [GbE]</b></p>
   </td>
   <td rowspan=2 valign=top style='border:solid #DDDDDD 1.0pt;border-left:none;
   background:#cbd4e0;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
   <p><b>AutoNeg</b></p>
   </td>
   <td colspan=3 valign=top style='border:solid #DDDDDD 1.0pt;border-left:none;
   background:#cbd4e0;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
   <p><b>Force</b></p>
   </td>
   <td rowspan=2 valign=top style='border:solid #DDDDDD 1.0pt;border-left:none;
   background:#cbd4e0;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
   <p><b>Cable / Modules</b></p>
   </td>
   <td rowspan=2 valign=top style='border:solid #DDDDDD 1.0pt;border-left:none;
   background:#cbd4e0;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
   <p><b>Cable Length [m]</b></p>
   </td>
   <td rowspan=2 valign=top style='border:solid #DDDDDD 1.0pt;border-left:none;
   background:#cbd4e0;padding:1.5pt 1.5pt 1.0pt 1.5pt'><b>Comments</b></td>
 </tr>
 <tr>
   <td valign=top style='border-top:none;border-left:none;border-bottom:solid #DDDDDD 1.0pt;
  border-right:solid #DDDDDD 1.0pt;background:#cbd4e0;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p>RS FEC</p>
  </td>
  <td valign=top style='border-top:none;border-left:none;border-bottom:solid #DDDDDD 1.0pt;
  border-right:solid #DDDDDD 1.0pt;background:#cbd4e0;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p>FC FEC</p>
  </td>
  <td valign=top style='border-top:none;border-left:none;border-bottom:solid #DDDDDD 1.0pt;
  border-right:solid #DDDDDD 1.0pt;background:#cbd4e0;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p>NO FEC</p>
  </td>
 </tr>
 </thead>
 <tr>
  <td rowspan=2 valign=top style='border:solid #DDDDDD 1.0pt;border-top:none;
  padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p>100 (NRZ)</p>
  </td>
  <td rowspan=2 valign=top style='border-top:none;border-left:none;border-bottom:
  solid #DDDDDD 1.0pt;border-right:solid #DDDDDD 1.0pt;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p>&#10008;</p>
  <p>&nbsp;</p>
  </td>
  <td rowspan=2 valign=top style='border-top:none;border-left:none;border-bottom:
  solid #DDDDDD 1.0pt;border-right:solid #DDDDDD 1.0pt;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p>&#9989;</p>
  <p>&nbsp;</p>
  </td>
  <td rowspan=2 valign=top style='border-top:none;border-left:none;border-bottom:
  solid #DDDDDD 1.0pt;border-right:solid #DDDDDD 1.0pt;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p>&#10008;</p>
  <p>&nbsp;</p>
  </td>
  <td rowspan=2 valign=top style='border-top:none;border-left:none;border-bottom:
  solid #DDDDDD 1.0pt;border-right:solid #DDDDDD 1.0pt;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p>&#9989;</p>
  </td>
  <td valign=top style='border-top:none;border-left:none;border-bottom:solid #DDDDDD 1.0pt;
  border-right:solid #DDDDDD 1.0pt;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p>Optic</p>
  </td>
  <td valign=top style='border-top:none;border-left:none;border-bottom:solid #DDDDDD 1.0pt;
  border-right:solid #DDDDDD 1.0pt;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p>Up to 30</p>
  </td>
  <td rowspan=2 valign=top style='border:solid #DDDDDD 1.0pt;border-top:none;
  padding:1.5pt 1.5pt 1.0pt 1.5pt'>N/A</td>
 </tr>
 <tr>
  <td valign=top style='border-top:none;border-left:none;border-bottom:solid #DDDDDD 1.0pt;
  border-right:solid #DDDDDD 1.0pt;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p>Copper</p>
  </td>
  <td valign=top style='border-top:none;border-left:none;border-bottom:solid #DDDDDD 1.0pt;
  border-right:solid #DDDDDD 1.0pt;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p>Up to 5</p>
  </td>
 </tr>
 <tr>
  <td rowspan=2 valign=top style='border:solid #DDDDDD 1.0pt;border-top:none;
  padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p>25/50 (NRZ)</p>
  </td>
  <td rowspan=2 valign=top style='border-top:none;border-left:none;border-bottom:
  solid #DDDDDD 1.0pt;border-right:solid #DDDDDD 1.0pt;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p>&#10008;</p>
  <p>&nbsp;</p>
  </td>
  <td rowspan=2 valign=top style='border-top:none;border-left:none;border-bottom:
  solid #DDDDDD 1.0pt;border-right:solid #DDDDDD 1.0pt;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p>&#9989;</p>
  <p>&nbsp;</p>
  </td>
  <td rowspan=2 valign=top style='border-top:none;border-left:none;border-bottom:
  solid #DDDDDD 1.0pt;border-right:solid #DDDDDD 1.0pt;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p>&#9989;</p>
  </td>
  <td rowspan=2 valign=top style='border-top:none;border-left:none;border-bottom:
  solid #DDDDDD 1.0pt;border-right:solid #DDDDDD 1.0pt;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p>&#9989;</p>
  <p>&nbsp;</p>
  </td>
  <td valign=top style='border-top:none;border-left:none;border-bottom:solid #DDDDDD 1.0pt;
  border-right:solid #DDDDDD 1.0pt;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p>Optic</p>
  </td>
  <td valign=top style='border-top:none;border-left:none;border-bottom:solid #DDDDDD 1.0pt;
  border-right:solid #DDDDDD 1.0pt;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p>Up to 30</p>
  </td>
  <td rowspan=2 valign=top style='border:solid #DDDDDD 1.0pt;border-top:none;
  padding:1.5pt 1.5pt 1.0pt 1.5pt'>N/A</td>
 </tr>
 <tr>
  <td valign=top style='border-top:none;border-left:none;border-bottom:solid #DDDDDD 1.0pt;
  border-right:solid #DDDDDD 1.0pt;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p>Copper</p>
  </td>
  <td valign=top style='border-top:none;border-left:none;border-bottom:solid #DDDDDD 1.0pt;
  border-right:solid #DDDDDD 1.0pt;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p>Up to 5</p>
  </td>
 </tr>
 <tr>
  <td rowspan=2 valign=top style='border:solid #DDDDDD 1.0pt;border-top:none;
  padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p>10/40</p>
  </td>
  <td rowspan=2 valign=top style='border-top:none;border-left:none;border-bottom:
  solid #DDDDDD 1.0pt;border-right:solid #DDDDDD 1.0pt;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p>&#10008;</p>
  </td>
  <td rowspan=2 valign=top style='border-top:none;border-left:none;border-bottom:
  solid #DDDDDD 1.0pt;border-right:solid #DDDDDD 1.0pt;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p>&#10008;</p>
  </td>
  <td rowspan=2 valign=top style='border-top:none;border-left:none;border-bottom:
  solid #DDDDDD 1.0pt;border-right:solid #DDDDDD 1.0pt;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p>&#10008;</p>
  </td>
  <td rowspan=2 valign=top style='border-top:none;border-left:none;border-bottom:
  solid #DDDDDD 1.0pt;border-right:solid #DDDDDD 1.0pt;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p>&#9989;</p>
  </td>
  <td valign=top style='border-top:none;border-left:none;border-bottom:solid #DDDDDD 1.0pt;
  border-right:solid #DDDDDD 1.0pt;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p>Optic</p>
  </td>
  <td valign=top style='border-top:none;border-left:none;border-bottom:solid #DDDDDD 1.0pt;
  border-right:solid #DDDDDD 1.0pt;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p>Up to 30</p>
  </td>
  <td rowspan=2 valign=top style='border:solid #DDDDDD 1.0pt;border-top:none;
  padding:1.5pt 1.5pt 1.0pt 1.5pt'>10GBASE-T modules are not supported</td>
 </tr>
 <tr>
  <td valign=top style='border-top:none;border-left:none;border-bottom:solid #DDDDDD 1.0pt;
  border-right:solid #DDDDDD 1.0pt;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p>Copper</p>
  </td>
  <td valign=top style='border-top:none;border-left:none;border-bottom:solid #DDDDDD 1.0pt;
  border-right:solid #DDDDDD 1.0pt;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p>Up to 3</p>
  </td>
 </tr>
</table>

...

## Changes and New Features History

<table border=1 cellspacing=0 cellpadding=0 width="100%"
 style='border-collapse:collapse;border:none'>
 <thead>
  <tr>
   <td width=186 valign=top style='width:139.25pt;border:solid #DDDDDD 1.0pt;
   background:#cbd4e0;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
   <p align=center style='text-align:center'><b>Category</b></p>
   </td>
   <td width=423 valign=top style='width:317.45pt;border:solid #DDDDDD 1.0pt;
   border-left:none;background:#cbd4e0;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
   <p align=center style='text-align:center'><b>Description</b></p>
   </td>
  </tr>
 </thead>
 <tr>
  <td width=609 colspan=2 valign=top style='width:456.7pt;border:solid #DDDDDD 1.0pt;
  border-top:none;background:#cbd4e0;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p align=center style='text-align:center'>Rev. SONiC
  201911_MUR3</p>
  </td>
 </tr>
 <tr>
  <td width=186 valign=top style='width:139.25pt;border:solid #DDDDDD 1.0pt;
  border-top:none;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p><b>Switch Systems</b></p>
  </td>
  <td width=423 valign=top style='width:317.45pt;border-top:none;border-left:
  none;border-bottom:solid #DDDDDD 1.0pt;border-right:solid #DDDDDD 1.0pt;
  padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p>NVIDIA Mellanox Spectrum-3
  (SN4600C) and NVIDIA Mellanox Spectrum-2 (SN3420) Ethernet switch platforms
  are now at GA Level.</p>
  </td>
 </tr>
 <tr>
  <td width=186 valign=top style='width:139.25pt;border:solid #DDDDDD 1.0pt;
  border-top:none;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p><b>Buffers</b></p>
  </td>
  <td width=423 valign=top style='width:317.45pt;border-top:none;border-left:
  none;border-bottom:solid #DDDDDD 1.0pt;border-right:solid #DDDDDD 1.0pt;
  padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p>Aligned all platforms to
  recent headroom calculation for both T0 and T1.<br>
  <b>Note:</b> Upgrading to this version will not automatically update the
  numbers. In order to have them applied, you should run the &quot;config
  load_minigraph&quot; command.</p>
  </td>
 </tr>
 <tr>
  <td width=186 valign=top style='width:139.25pt;border:solid #DDDDDD 1.0pt;
  border-top:none;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p><b>What-Just-Happened</b></p>
  </td>
  <td width=423 valign=top style='width:317.45pt;border-top:none;border-left:
  none;border-bottom:solid #DDDDDD 1.0pt;border-right:solid #DDDDDD 1.0pt;
  padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p>Added sample window
  information for all aggregated show commands.</p>
  </td>
 </tr>
 <tr>
  <td width=186 valign=top style='width:139.25pt;border:solid #DDDDDD 1.0pt;
  border-top:none;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p><b>Warm-boot</b></p>
  </td>
  <td width=423 valign=top style='width:317.45pt;border-top:none;border-left:
  none;border-bottom:solid #DDDDDD 1.0pt;border-right:solid #DDDDDD 1.0pt;
  padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p>Added support for warm-boot
  capability for&nbsp;SN4700 and SN4600C switch systems.&nbsp;</p>
  </td>
 </tr>
 <tr>
  <td width=186 valign=top style='width:139.25pt;border:solid #DDDDDD 1.0pt;
  border-top:none;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p><b>Cables</b></p>
  </td>
  <td width=423 valign=top style='width:317.45pt;border-top:none;border-left:
  none;border-bottom:solid #DDDDDD 1.0pt;border-right:solid #DDDDDD 1.0pt;
  padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p>Added support for QSFP-DD
  module in SN4700 switch systems used for all &quot;show&quot; commands and
  SFP monitoring.</p>
  </td>
 </tr>
 <tr>
  <td width=186 valign=top style='width:139.25pt;border:solid #DDDDDD 1.0pt;
  border-top:none;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p><b>Build</b></p>
  </td>
  <td width=423 valign=top style='width:317.45pt;border-top:none;border-left:
  none;border-bottom:solid #DDDDDD 1.0pt;border-right:solid #DDDDDD 1.0pt;
  padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p>Added DKMS build support
  for Mellanox MFT and SDK.</p>
  </td>
 </tr>
 <tr>
  <td width=186 valign=top style='width:139.25pt;border:solid #DDDDDD 1.0pt;
  border-top:none;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p><b>Customer-Affecting
  Changes</b></p>
  </td>
  <td width=423 valign=top style='width:317.45pt;border-top:none;border-left:
  none;border-bottom:solid #DDDDDD 1.0pt;border-right:solid #DDDDDD 1.0pt;
  padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p>See&nbsp;<a
  href="#scroll-bookmark-21">Customer-Affecting
  Changes</a>.</p>
  </td>
 </tr>
 <tr>
  <td width=609 colspan=2 valign=top style='width:456.7pt;border:solid #DDDDDD 1.0pt;
  border-top:none;background:#cbd4e0;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p align=center style='text-align:center'>Rev. SONiC
  201911_MUR2</p>
  </td>
 </tr>
 <tr>
  <td width=186 valign=top style='width:139.25pt;border:solid #DDDDDD 1.0pt;
  border-top:none;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p><b>Proxy-ARP</b></p>
  </td>
  <td width=423 valign=top style='width:317.45pt;border-top:none;border-left:
  none;border-bottom:solid #DDDDDD 1.0pt;border-right:solid #DDDDDD 1.0pt;
  padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p>The Proxy ARP distributes
  traffic through multiple gateways by balancing load based on source and
  destination IP addresses.</p>
  <p>For further information,
  see<a
  href="https://github.com/Azure/SONiC/blob/master/doc/arp/Proxy%20Arp.md">https://github.com/Azure/SONiC/blob/master/doc/arp/Proxy%20Arp.md</a></p>
  </td>
 </tr>
 <tr>
  <td width=186 valign=top style='width:139.25pt;border:solid #DDDDDD 1.0pt;
  border-top:none;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p><b>Thermal Control</b></p>
  </td>
  <td width=423 valign=top style='width:317.45pt;border-top:none;border-left:
  none;border-bottom:solid #DDDDDD 1.0pt;border-right:solid #DDDDDD 1.0pt;
  padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p>The Thermal Control keeps
  the switch at a proper temperature by using cooling devices.</p>
  <p>For further information,
  see</p>
  <p><a
  href="https://github.com/Azure/SONiC/blob/master/doc/pmon/sonic_thermal_control_test_plan.md">https://github.com/Azure/SONiC/blob/master/doc/pmon/sonic_thermal_control_test_plan.md</a></p>
  </td>
 </tr>
 <tr>
  <td width=186 valign=top style='width:139.25pt;border:solid #DDDDDD 1.0pt;
  border-top:none;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p><b>What-Just-Happened</b></p>
  </td>
  <td width=423 valign=top style='width:317.45pt;border-top:none;border-left:
  none;border-bottom:solid #DDDDDD 1.0pt;border-right:solid #DDDDDD 1.0pt;
  padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p>The What-Just-Happened
  feature provides the ability to retain the last packets that were dropped
  from the switch with complete packet headers and the actual drop reason. This
  enhances the ability to debug network problems, identify affected flows, and
  decrease time-to-repair.</p>
  <p>Once enabled, the user can
  debug L2, l3 and Tunnel drop packets with raw and aggregated information.</p>
  <p>The features should be
  downloaded and installed on top of a SONiC release via DPKT. Please contact
  Mellanox Support to get this package.</p>
  </td>
 </tr>
 <tr>
  <td width=609 colspan=2 valign=top style='width:456.7pt;border:solid #DDDDDD 1.0pt;
  border-top:none;background:#cbd4e0;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p align=center style='text-align:center'>Rev. SONiC
  201911_MUR1</p>
  </td>
 </tr>
 <tr>
  <td width=186 valign=top style='width:139.25pt;border:solid #DDDDDD 1.0pt;
  border-top:none;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p><b>Switch Systems</b></p>
  </td>
  <td width=423 valign=top style='width:317.45pt;border-top:none;border-left:
  none;border-bottom:solid #DDDDDD 1.0pt;border-right:solid #DDDDDD 1.0pt;
  padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p>Added support for Mellanox
  Spectrum-2 (SN3420) and Mellanox Spectrum-3 (SN4700 and SN4600C) Ethernet
  switch platforms at Engineering Sample Level.</p>
  </td>
 </tr>
 <tr>
  <td width=186 valign=top style='width:139.25pt;border:solid #DDDDDD 1.0pt;
  border-top:none;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p><b>PAM4 Link Speeds when
  Using 400GbE/200GbE</b></p>
  </td>
  <td width=423 valign=top style='width:317.45pt;border-top:none;border-left:
  none;border-bottom:solid #DDDDDD 1.0pt;border-right:solid #DDDDDD 1.0pt;
  padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p>The following are the
  minimal software/firmware versions that support PAM4 link speeds when
  connected using Mellanox-to-Mellanox and Mellanox-to-3rd party devices:</p>
  <p style='margin-left:.25in;text-indent:-.25in'>·&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
  Mellanox Onyx: 3.9.0900</p>
  <p style='margin-left:.25in;text-indent:-.25in'>·&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
  ConnectX-6/ConnectX-6 Dx:
  20/22.27.2008*</p>
  <p><b>*Note:</b> NICs with this firmware version support
  Mellanox-to-Mellanox connectivity with PAM4 link speeds.</p>
  </td>
 </tr>
 <tr>
  <td width=186 valign=top style='width:139.25pt;border:solid #DDDDDD 1.0pt;
  border-top:none;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p><b>Link Speed</b></p>
  </td>
  <td width=423 valign=top style='width:317.45pt;border-top:none;border-left:
  none;border-bottom:solid #DDDDDD 1.0pt;border-right:solid #DDDDDD 1.0pt;
  padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p>200GbE speed rate is at GA
  level when connecting Mellanox to Mellanox cables.</p>
  </td>
 </tr>
 <tr>
  <td width=186 valign=top style='width:139.25pt;border:solid #DDDDDD 1.0pt;
  border-top:none;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p><b>Link Speed</b></p>
  </td>
  <td width=423 valign=top style='width:317.45pt;border-top:none;border-left:
  none;border-bottom:solid #DDDDDD 1.0pt;border-right:solid #DDDDDD 1.0pt;
  padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p>200GbE speed rate is at
  Engineering Sample Level when connecting Mellanox to 3<sup>rd</sup> party
  cables.</p>
  </td>
 </tr>
 <tr>
  <td width=186 valign=top style='width:139.25pt;border:solid #DDDDDD 1.0pt;
  border-top:none;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p><b>Link Speed</b></p>
  </td>
  <td width=423 valign=top style='width:317.45pt;border-top:none;border-left:
  none;border-bottom:solid #DDDDDD 1.0pt;border-right:solid #DDDDDD 1.0pt;
  padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p>400GbE speed rate is at
  Engineering Sample Level.</p>
  </td>
 </tr>
 <tr>
  <td width=186 valign=top style='width:139.25pt;border:solid #DDDDDD 1.0pt;
  border-top:none;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p><b>ZTP</b></p>
  </td>
  <td width=423 valign=top style='width:317.45pt;border-top:none;border-left:
  none;border-bottom:solid #DDDDDD 1.0pt;border-right:solid #DDDDDD 1.0pt;
  padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p>Out-of-band management is
  now functional. &nbsp;</p>
  </td>
 </tr>
 <tr>
  <td width=609 colspan=2 valign=top style='width:456.7pt;border:solid #DDDDDD 1.0pt;
  border-top:none;background:#cbd4e0;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p align=center style='text-align:center'>Rev. SONiC 201911</p>
  </td>
 </tr>
 <tr>
  <td width=186 valign=top style='width:139.25pt;border:solid #DDDDDD 1.0pt;
  border-top:none;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p><b>Switch Systems</b></p>
  </td>
  <td width=423 valign=top style='width:317.45pt;border-top:none;border-left:
  none;border-bottom:solid #DDDDDD 1.0pt;border-right:solid #DDDDDD 1.0pt;
  padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p>Added support for Mellanox
  Spectrum-2 Ethernet switch platforms (SN3700, SN3700C and SN3800).</p>
  </td>
 </tr>
 <tr>
  <td width=186 valign=top style='width:139.25pt;border:solid #DDDDDD 1.0pt;
  border-top:none;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p><b>Zero Time Warm-boot</b></p>
  </td>
  <td width=423 valign=top style='width:317.45pt;border-top:none;border-left:
  none;border-bottom:solid #DDDDDD 1.0pt;border-right:solid #DDDDDD 1.0pt;
  padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p>No data disruption for
  Mellanox Spectrum and Spectrum-2 Ethernet switch platforms.</p>
  </td>
 </tr>
 <tr>
  <td width=186 valign=top style='width:139.25pt;border:solid #DDDDDD 1.0pt;
  border-top:none;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p><b>Warm-boot for Spectrum-2</b></p>
  </td>
  <td width=423 valign=top style='width:317.45pt;border-top:none;border-left:
  none;border-bottom:solid #DDDDDD 1.0pt;border-right:solid #DDDDDD 1.0pt;
  padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p>Added support for warm-boot
  for Spectrum-2 Ethernet switch platforms.</p>
  </td>
 </tr>
 <tr>
  <td width=186 valign=top style='width:139.25pt;border:solid #DDDDDD 1.0pt;
  border-top:none;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p><b>Zero Touch Provisioning
  (ZTP)</b></p>
  </td>
  <td width=423 valign=top style='width:317.45pt;border-top:none;border-left:
  none;border-bottom:solid #DDDDDD 1.0pt;border-right:solid #DDDDDD 1.0pt;
  padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p>Zero Touch Provisioning
  (ZTP) service can be used by users to configure a fleet of switches using
  common configuration templates. Switches booting from factory default state
  should be able to communicate with remote provisioning server and download relevant
  configuration files and scripts to kick start more complex configuration
  steps. ZTP service takes user input in JSON format.</p>
  <p><b>Notes:</b></p>
  <p>·&nbsp; This
  capability is disabled by default and needs to be enabled upon compilation.</p>
  <p>·&nbsp; This
  capability is not tested on any Mellanox platforms.</p>
  <p>For further information,
  see <a href="https://github.com/Azure/SONiC/blob/master/doc/ztp/ztp.md">https://github.com/Azure/SONiC/blob/master/doc/ztp/ztp.md</a></p>
  </td>
 </tr>
 <tr>
  <td width=186 valign=top style='width:139.25pt;border:solid #DDDDDD 1.0pt;
  border-top:none;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p><b>FRR</b></p>
  </td>
  <td width=423 valign=top style='width:317.45pt;border-top:none;border-left:
  none;border-bottom:solid #DDDDDD 1.0pt;border-right:solid #DDDDDD 1.0pt;
  padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p>Becomes the default routing
  protocol.</p>
  </td>
 </tr>
 <tr>
  <td width=186 valign=top style='width:139.25pt;border:solid #DDDDDD 1.0pt;
  border-top:none;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p><b>VXLAN VNET</b></p>
  </td>
  <td width=423 valign=top style='width:317.45pt;border-top:none;border-left:
  none;border-bottom:solid #DDDDDD 1.0pt;border-right:solid #DDDDDD 1.0pt;
  padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p>Supported VNET scale
  numbers:</p>
  <p>·&nbsp; Mellanox
  Spectrum</p>
  <p style='margin-left:1.0in;text-indent:-.25in'>o&nbsp;&nbsp;
  VNETs: 32</p>
  <p style='margin-left:1.0in;text-indent:-.25in'>o&nbsp;&nbsp;
  VNET interfaces: 32</p>
  <p style='margin-left:1.0in;text-indent:-.25in'>o&nbsp;&nbsp;
  VNET routes: 3000</p>
  <p style='margin-left:1.0in;text-indent:-.25in'>o&nbsp;&nbsp;
  VNET endpoints: 512</p>
  <p>·&nbsp; Mellanox
  Spectrum-2</p>
  <p style='margin-left:1.0in;text-indent:-.25in'>o&nbsp;&nbsp;
  VNETs: 32</p>
  <p style='margin-left:1.0in;text-indent:-.25in'>o&nbsp;&nbsp;
  VNET interfaces: 32</p>
  <p style='margin-left:1.0in;text-indent:-.25in'>o&nbsp;&nbsp;
  VNET routes: 40000</p>
  <p style='margin-left:1.0in;text-indent:-.25in'>o&nbsp;&nbsp;
  VNET endpoints: 4000</p>
  <p>For further information,
  see <a
  href="https://github.com/Azure/SONiC/blob/master/doc/vxlan/Vxlan_hld.md">https://github.com/Azure/SONiC/blob/master/doc/vxlan/Vxlan_hld.md</a></p>
  </td>
 </tr>
 <tr>
  <td width=186 valign=top style='width:139.25pt;border:solid #DDDDDD 1.0pt;
  border-top:none;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p><b>CLI Commands: BIOS and
  CPLD Updates</b></p>
  </td>
  <td width=423 valign=top style='width:317.45pt;border-top:none;border-left:
  none;border-bottom:solid #DDDDDD 1.0pt;border-right:solid #DDDDDD 1.0pt;
  padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p>For further information,
  see <a
  href="https://github.com/Azure/sonic-utilities/blob/master/doc/Command-Reference.md#platform-component-firmware">https://github.com/Azure/sonic-utilities/blob/master/doc/Command-Reference.md#platform-component-firmware</a></p>
  </td>
 </tr>
 <tr>
  <td width=186 valign=top style='width:139.25pt;border:solid #DDDDDD 1.0pt;
  border-top:none;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p><b>Configurable Drop
  Counters</b></p>
  </td>
  <td width=423 valign=top style='width:317.45pt;border-top:none;border-left:
  none;border-bottom:solid #DDDDDD 1.0pt;border-right:solid #DDDDDD 1.0pt;
  padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p>For further information,
  see <a
  href="https://github.com/Azure/sonic-utilities/blob/master/doc/Command-Reference.md#drop-counters">https://github.com/Azure/sonic-utilities/blob/master/doc/Command-Reference.md#drop-counters</a></p>
  </td>
 </tr>
 <tr>
  <td width=186 valign=top style='width:139.25pt;border:solid #DDDDDD 1.0pt;
  border-top:none;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p><b>Management VRF<br>
  <br>
  </b></p>
  </td>
  <td width=423 valign=top style='width:317.45pt;border-top:none;border-left:
  none;border-bottom:solid #DDDDDD 1.0pt;border-right:solid #DDDDDD 1.0pt;
  padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p>For further information,
  see <a
  href="https://github.com/Azure/sonic-utilities/blob/master/doc/Command-Reference.md#management-vrf">https://github.com/Azure/sonic-utilities/blob/master/doc/Command-Reference.md#management-vrf</a></p>
  </td>
 </tr>
 <tr>
  <td width=186 valign=top style='width:139.25pt;border:solid #DDDDDD 1.0pt;
  border-top:none;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p><b>SSD Health</b></p>
  </td>
  <td width=423 valign=top style='width:317.45pt;border-top:none;border-left:
  none;border-bottom:solid #DDDDDD 1.0pt;border-right:solid #DDDDDD 1.0pt;
  padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p>Displays switch’s SSD
  health parameter.</p>
  <p>For further information,
  see <a
  href="https://github.com/Azure/sonic-utilities/blob/master/doc/Command-Reference.md#show-hardware-platform">https://github.com/Azure/sonic-utilities/blob/master/doc/Command-Reference.md#show-hardware-platform</a></p>
  </td>
 </tr>
 <tr>
  <td width=186 valign=top style='width:139.25pt;border:solid #DDDDDD 1.0pt;
  border-top:none;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p><b>Egress Mirroring and ACL
  Action Support check via SAI</b></p>
  </td>
  <td width=423 valign=top style='width:317.45pt;border-top:none;border-left:
  none;border-bottom:solid #DDDDDD 1.0pt;border-right:solid #DDDDDD 1.0pt;
  padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p>For further information,
  see <a
  href="https://github.com/Azure/sonic-utilities/blob/master/doc/Command-Reference.md#acl">https://github.com/Azure/sonic-utilities/blob/master/doc/Command-Reference.md#acl</a></p>
  </td>
 </tr>
 <tr>
  <td width=186 valign=top style='width:139.25pt;border:solid #DDDDDD 1.0pt;
  border-top:none;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p><b>CPLD Update Time<br>
  <br>
  </b></p>
  </td>
  <td width=423 valign=top style='width:317.45pt;border-top:none;border-left:
  none;border-bottom:solid #DDDDDD 1.0pt;border-right:solid #DDDDDD 1.0pt;
  padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p>Reduced the CPLD update
  time to less than 10 min.</p>
  </td>
 </tr>
 <tr>
  <td width=186 valign=top style='width:139.25pt;border:solid #DDDDDD 1.0pt;
  border-top:none;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p><b>PSU Monitoring</b></p>
  </td>
  <td width=423 valign=top style='width:317.45pt;border-top:none;border-left:
  none;border-bottom:solid #DDDDDD 1.0pt;border-right:solid #DDDDDD 1.0pt;
  padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p>New PSU daemon (psud) added
  to collect PSU running status to DB.</p>
  <p>For further information,
  see <a
  href="https://github.com/Azure/SONiC/blob/master/doc/pmon/pmon-enhancement-design.md">https://github.com/Azure/SONiC/blob/master/doc/pmon/pmon-enhancement-design.md</a></p>
  </td>
 </tr>
 <tr>
  <td width=186 valign=top style='width:139.25pt;border:solid #DDDDDD 1.0pt;
  border-top:none;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p><b>System EEPROM Monitoring<br>
  <br>
  </b></p>
  </td>
  <td width=423 valign=top style='width:317.45pt;border-top:none;border-left:
  none;border-bottom:solid #DDDDDD 1.0pt;border-right:solid #DDDDDD 1.0pt;
  padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p>New system EEPROM daemon
  added to fetch system EEPROM content to DB.</p>
  </td>
 </tr>
 <tr>
  <td width=186 valign=top style='width:139.25pt;border:solid #DDDDDD 1.0pt;
  border-top:none;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p><b>Configurable Daemon
  Launching in pmon</b></p>
  </td>
  <td width=423 valign=top style='width:317.45pt;border-top:none;border-left:
  none;border-bottom:solid #DDDDDD 1.0pt;border-right:solid #DDDDDD 1.0pt;
  padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p>User can control the
  launching of the daemons in pmon by editing the configuration file.</p>
  <p>For further information,
  see <a
  href="https://github.com/Azure/SONiC/blob/master/doc/pmon/pmon-enhancement-design.md#4-pmon-daemons-dynamically-loading">https://github.com/Azure/SONiC/blob/master/doc/pmon/pmon-enhancement-design.md#4-pmon-daemons-dynamically-loading</a></p>
  </td>
 </tr>
 <tr>
  <td width=186 valign=top style='width:139.25pt;border:solid #DDDDDD 1.0pt;
  border-top:none;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p><b>New Platform API Support</b></p>
  </td>
  <td width=423 valign=top style='width:317.45pt;border-top:none;border-left:
  none;border-bottom:solid #DDDDDD 1.0pt;border-right:solid #DDDDDD 1.0pt;
  padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p>New Platform API is
  designed to replace the old device plugins to fetch platform device
  information.</p>
  <p>The following Platform API
  were added:</p>
  <p style='margin-left:.25in;text-indent:-.25in'>·&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
  FAN platform API</p>
  <p style='margin-left:.25in;text-indent:-.25in'>·&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
  PSU platform API</p>
  <p style='margin-left:.25in;text-indent:-.25in'>·&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
  SFP platform API</p>
  <p style='margin-left:.25in;text-indent:-.25in'>·&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
  Thermal platform API</p>
  <p style='margin-left:.25in;text-indent:-.25in'>·&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
  Watchdog platform API</p>
  <p style='margin-left:.25in;text-indent:-.25in'>·&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
  EEPROM platform API</p>
  <p style='margin-left:.25in;text-indent:-.25in'>·&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
  CPLD and BIOS platform API</p>
  <p>For further information, see <a
  href="https://github.com/Azure/SONiC/blob/master/doc/platform_api/new_platform_api.md">https://github.com/Azure/SONiC/blob/master/doc/platform_api/new_platform_api.md</a></p>
  </td>
 </tr>
 <tr>
  <td width=609 colspan=2 valign=top style='width:456.7pt;border:solid #DDDDDD 1.0pt;
  border-top:none;background:#cbd4e0;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p align=center style='text-align:center'>Rev. SONiC 201811</p>
  </td>
 </tr>
 <tr>
  <td width=609 colspan=2 valign=top style='width:456.7pt;border:solid #DDDDDD 1.0pt;
  border-top:none;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p>For the complete list of
  commands that are supported in SONiC 201811, see <a
  href="https://github.com/Azure/sonic-utilities/blob/201911/doc/Command-Reference.md">https://github.com/Azure/sonic-utilities/blob/201911/doc/Command-Reference.md</a>.</p>
  <p>Please note that as the Command Reference Guide is not part of 201811 branch (it was added at a later stage). Any differences in the software behavior between 201911 and 201811 should be specified by the Author.</p>
  </td>
 </tr>
 <tr>
  <td width=186 valign=top style='width:139.25pt;border:solid #DDDDDD 1.0pt;
  border-top:none;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p><b>MAC Address Aging</b></p>
  </td>
  <td width=423 valign=top style='width:317.45pt;border-top:none;border-left:
  none;border-bottom:solid #DDDDDD 1.0pt;border-right:solid #DDDDDD 1.0pt;
  padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p>The MAC address aging time
  can be changed by updating the &quot;orchagent&quot; configuration file.</p>
  </td>
 </tr>
 <tr>
  <td width=186 valign=top style='width:139.25pt;border:solid #DDDDDD 1.0pt;
  border-top:none;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p><b>Critical Resource
  Monitoring</b></p>
  </td>
  <td width=423 valign=top style='width:317.45pt;border-top:none;border-left:
  none;border-bottom:solid #DDDDDD 1.0pt;border-right:solid #DDDDDD 1.0pt;
  padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p>Critical Resource
  Monitoring (CRM) monitors ASIC resources' utilization by polling SAI
  attributes.</p>
  <p>For further information, see <a
  href="https://github.com/Azure/SONiC/wiki/Critical-Resource-Monitoring-High-Level-Design">https://github.com/Azure/SONiC/wiki/Critical-Resource-Monitoring-High-Level-Design</a>.</p>
  </td>
 </tr>
 <tr>
  <td width=186 valign=top style='width:139.25pt;border:solid #DDDDDD 1.0pt;
  border-top:none;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p><b>PFC Watchdog</b></p>
  </td>
  <td width=423 valign=top style='width:317.45pt;border-top:none;border-left:
  none;border-bottom:solid #DDDDDD 1.0pt;border-right:solid #DDDDDD 1.0pt;
  padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p>PFC watchdog is designed to
  detect and mitigate PFC storm received for each port. PFC pause frames is
  used in lossless Ethernet to pause the link partner from sending packets.
  Such back-pressure mechanism could propagate to the whole network and cause
  the network stop forwarding traffic. PFC watchdog is to detect abnormal back-
  pressure caused by receiving excessive PFC pause frames, and mitigate such
  situation by disable PFC caused pause temporarily. PFC watchdog has three
  function blocks, i.e. detection, mitigation and restoration.</p>
  <p>For further information,
  see <a href="https://github.com/Azure/SONiC/wiki/PFC-Watchdog-Design">https://github.com/Azure/SONiC/wiki/PFC-Watchdog-Design</a></p>
  </td>
 </tr>
 <tr>
  <td width=186 valign=top style='width:139.25pt;border:solid #DDDDDD 1.0pt;
  border-top:none;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p><b>IPv6 ACL</b></p>
  </td>
  <td width=423 valign=top style='width:317.45pt;border-top:none;border-left:
  none;border-bottom:solid #DDDDDD 1.0pt;border-right:solid #DDDDDD 1.0pt;
  padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p>Extends the ACL IPv4
  support within IPv6.</p>
  <p>For further information,
  see <a
  href="https://github.com/Azure/SONiC/blob/gh-pages/doc/ACL-enhancements-on-SONIC.docx">https://github.com/Azure/SONiC/blob/gh-pages/doc/ACL-enhancements-on-SONIC.docx</a></p>
  </td>
 </tr>
 <tr>
  <td width=186 valign=top style='width:139.25pt;border:solid #DDDDDD 1.0pt;
  border-top:none;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p><b>BGP Neighbors</b></p>
  <p><b>(neighbor-down
  fib-accelerate)</b></p>
  </td>
  <td width=423 valign=top style='width:317.45pt;border-top:none;border-left:
  none;border-bottom:solid #DDDDDD 1.0pt;border-right:solid #DDDDDD 1.0pt;
  padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p>BGP neighbors performance
  improvements.</p>
  </td>
 </tr>
 <tr>
  <td width=186 valign=top style='width:139.25pt;border:solid #DDDDDD 1.0pt;
  border-top:none;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p><b>gRPC for Telemetry</b></p>
  </td>
  <td width=423 valign=top style='width:317.45pt;border-top:none;border-left:
  none;border-bottom:solid #DDDDDD 1.0pt;border-right:solid #DDDDDD 1.0pt;
  padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p>Implementation of gRPC for
  Telemetry data collection.</p>
  <p>For further information,
  see <a
  href="https://github.com/Azure/sonic-telemetry/blob/master/doc/grpc_telemetry.md">https://github.com/Azure/sonic-telemetry/blob/master/doc/grpc_telemetry.md</a></p>
  </td>
 </tr>
 <tr>
  <td width=186 valign=top style='width:139.25pt;border:solid #DDDDDD 1.0pt;
  border-top:none;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p><b>Transceiver Sensors
  Monitoring</b></p>
  </td>
  <td width=423 valign=top style='width:317.45pt;border-top:none;border-left:
  none;border-bottom:solid #DDDDDD 1.0pt;border-right:solid #DDDDDD 1.0pt;
  padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p>Transceiver Sensors
  monitoring uses Xcvrd that is designed to fetch the transceiver and DOM
  sensor information from the eeprom, and then update the state DB with this
  information.</p>
  <p>For further information,
  see <a
  href="https://github.com/Azure/SONiC/blob/master/doc/xrcvd/transceiver-monitor-hld.md">https://github.com/Azure/SONiC/blob/master/doc/xrcvd/transceiver-monitor-hld.md</a></p>
  </td>
 </tr>
 <tr>
  <td width=186 valign=top style='width:139.25pt;border:solid #DDDDDD 1.0pt;
  border-top:none;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p><b>Asymmetric Priority Flow
  Control (PFC)</b></p>
  </td>
  <td width=423 valign=top style='width:317.45pt;border-top:none;border-left:
  none;border-bottom:solid #DDDDDD 1.0pt;border-right:solid #DDDDDD 1.0pt;
  padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p>Extends default PFC
  functionality in order to add possibility for configuring different behavior
  for receiving and transmitting PFC pause frames.</p>
  <p>For further information,
  see <a
  href="https://github.com/Azure/SONiC/wiki/Asymmetric-PFC-High-Level-Design">https://github.com/Azure/SONiC/wiki/Asymmetric-PFC-High-Level-Design</a></p>
  </td>
 </tr>
 <tr>
  <td width=186 valign=top style='width:139.25pt;border:solid #DDDDDD 1.0pt;
  border-top:none;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p><b>Routing Stack Graceful
  Restart</b></p>
  </td>
  <td width=423 valign=top style='width:317.45pt;border-top:none;border-left:
  none;border-bottom:solid #DDDDDD 1.0pt;border-right:solid #DDDDDD 1.0pt;
  padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p>Gracefully restarts the
  Routing Stack (BGP) as part of the warm-boot functionality. This allows a BGP
  speaker to express its ability to preserve forwarding state during BGP
  restart.</p>
  <p>For further information,
  see <a
  href="https://github.com/Azure/SONiC/blob/dcac72377f23521a394694214678ea4450f6f70a/doc/routing-warm-reboot/">https://github.com/Azure/SONiC/blob/dcac72377f23521a394694214678ea4450f6f70a/doc/routing-warm-reboot/</a> <a
  href="http://Routing_Warm_Reboot.md#4-bgp-graceful-restart-overview">Routing_Warm_Reboot.md#4-bgp-graceful-restart-overview</a></p>
  </td>
 </tr>
 <tr>
  <td width=186 valign=top style='width:139.25pt;border:solid #DDDDDD 1.0pt;
  border-top:none;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p><b>Incremental Config (IP,
  LAG, Port admin)</b></p>
  </td>
  <td width=423 valign=top style='width:317.45pt;border-top:none;border-left:
  none;border-bottom:solid #DDDDDD 1.0pt;border-right:solid #DDDDDD 1.0pt;
  padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p>Enhances Command Line
  Interface to allow run-time configuration of the different items.</p>
  <p>For more information, see <a
  href="https://github.com/Azure/sonic-utilities/blob/master/doc/Command-Reference.md">https://github.com/Azure/sonic-utilities/blob/master/doc/Command-Reference.md</a></p>
  </td>
 </tr>
 <tr>
  <td width=186 valign=top style='width:139.25pt;border:solid #DDDDDD 1.0pt;
  border-top:none;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p><b>IP-in-IP v6</b></p>
  </td>
  <td width=423 valign=top style='width:317.45pt;border-top:none;border-left:
  none;border-bottom:solid #DDDDDD 1.0pt;border-right:solid #DDDDDD 1.0pt;
  padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p>Extends IP-in-IP support
  with IPv6 and all 4 combinations of IPv4 and IPv6.</p>
  </td>
 </tr>
 <tr>
  <td width=186 valign=top style='width:139.25pt;border:solid #DDDDDD 1.0pt;
  border-top:none;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p><b>PFC Watermark Counters</b></p>
  </td>
  <td width=423 valign=top style='width:317.45pt;border-top:none;border-left:
  none;border-bottom:solid #DDDDDD 1.0pt;border-right:solid #DDDDDD 1.0pt;
  padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p>PFC Watermark counters are
  now available in both CLI and gRPC. A periodic read is performed via the
  Telemetry Agent, and on demand via the CLI for debug purposes.</p>
  <p>For further information,
  see <a
  href="https://github.com/Azure/SONiC/blob/master/doc/buffer-watermark/watermarks_HLD.md">https://github.com/Azure/SONiC/blob/master/doc/buffer-watermark/watermarks_HLD.md</a></p>
  </td>
 </tr>
 <tr>
  <td width=186 valign=top style='width:139.25pt;border:solid #DDDDDD 1.0pt;
  border-top:none;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p><b>SONiC Warm Reboot</b></p>
  </td>
  <td width=423 valign=top style='width:317.45pt;border-top:none;border-left:
  none;border-bottom:solid #DDDDDD 1.0pt;border-right:solid #DDDDDD 1.0pt;
  padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p>Restarts and upgrades SONiC
  software without impacting the data plane. This process takes &lt; 1 second.</p>
  <p>For further information,
  see <a
  href="https://github.com/Azure/SONiC/blob/master/doc/warm-reboot/SONiC_Warmboot.md">https://github.com/Azure/SONiC/blob/master/doc/warm-reboot/SONiC_Warmboot.md</a></p>
  </td>
 </tr>
 <tr>
  <td width=186 valign=top style='width:139.25pt;border:solid #DDDDDD 1.0pt;
  border-top:none;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p><b>Configurable ASIC Table
  Sizes</b></p>
  </td>
  <td width=423 valign=top style='width:317.45pt;border-top:none;border-left:
  none;border-bottom:solid #DDDDDD 1.0pt;border-right:solid #DDDDDD 1.0pt;
  padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p>By adding or updating the
  macro definitions in /usr/share/sonic/device/{platform name}/{sku name}/sai.profile, the &quot;fdb&quot;, &quot;ip route&quot;,
  and &quot;neighbor&quot; table sizes could be updated based on the need.</p>
  <p style='margin-left:.25in;text-indent:-.25in'>·&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
  SAI_FDB_TABLE_SIZE=32768</p>
  <p style='margin-left:.25in;text-indent:-.25in'>·&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
  SAI_IPV4_ROUTE_TABLE_SIZE=131072</p>
  <p style='margin-left:.25in;text-indent:-.25in'>·&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
  SAI_IPV6_ROUTE_TABLE_SIZE=16384</p>
  <p style='margin-left:.25in;text-indent:-.25in'>·&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
  SAI_IPV4_NEIGHBOR_TABLE_SIZE=16384</p>
  <p style='margin-left:.25in;text-indent:-.25in'>·&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
  SAI_IPV6_NEIGHBOR_TABLE_SIZE=12288</p>
  <p><b>Note:</b> Please contact Mellanox before updating the default sizes in the table.</p>
  </td>
 </tr>
</table>

### Customer-Affecting Changes

<table border=1 cellspacing=0 cellpadding=0 width="100%"
 style='width:100.0%;border-collapse:collapse;border:none'>
 <thead>
  <tr>
   <td valign=top style='border:solid #DDDDDD 1.0pt;background:#cbd4e0;
   padding:1.5pt 1.5pt 1.0pt 1.5pt'>
   <p align=center style='text-align:center'><b>Feature/Change</b></p>
   </td>
   <td valign=top style='border:solid #DDDDDD 1.0pt;border-left:none;
   background:#cbd4e0;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
   <p align=center style='text-align:center'><b>Description</b></p>
   </td>
  </tr>
 </thead>
 <tr>
  <td colspan=2 valign=top style='border:solid #DDDDDD 1.0pt;border-top:none;
  background:#cbd4e0;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p align=center style='text-align:center'>Rev. SONiC
  201911_MUR3</p>
  </td>
 </tr>
 <tr>
  <td valign=top style='border:solid #DDDDDD 1.0pt;border-top:none;padding:
  1.5pt 1.5pt 1.0pt 1.5pt'>
  <p>DHCP</p>
  </td>
  <td valign=top style='border-top:none;border-left:none;border-bottom:solid #DDDDDD 1.0pt;
  border-right:solid #DDDDDD 1.0pt;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p>DHCP trap can only be
  enabled on Top of Rack (ToR) Router. To enable it on a non-ToR Router, the
  user must change the default COPP trap configuration.</p>
  <p>For further information,
  see&nbsp;<a
  href="https://github.com/Azure/sonic-swss/blob/201911/doc/Configuration.md">https://github.com/Azure/sonic-swss/blob/201911/doc/Configuration.md</a></p>
  </td>
 </tr>
 <tr>
  <td valign=top style='border:solid #DDDDDD 1.0pt;border-top:none;padding:
  1.5pt 1.5pt 1.0pt 1.5pt'>
  <p>CLI Commands: Features</p>
  </td>
  <td valign=top style='border-top:none;border-left:none;border-bottom:solid #DDDDDD 1.0pt;
  border-right:solid #DDDDDD 1.0pt;padding:1.5pt 1.5pt 1.0pt 1.5pt'>
  <p>The &quot;Feature&quot; CLI
  command has been changed.</p>
  <p style='margin-left:.25in;text-indent:-.25in'>·&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
  To see all the available
  features command options, execute:<br>
  ‘show feature status’</p>
  <p style='margin-left:.25in;text-indent:-.25in'>·&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
  To change a feature state, execute:<br>
  ‘config
  feature state &lt;feature_name&gt; &lt;enabled/disbaled&gt;’</p>
  <p><b>Note:</b> Feature CLI changes affect the way WJH is enabled
  as well as any other feature.</p>
  </td>
 </tr>
</table>

## Bug Fix History

This section provides a list of bugs fixed by Mellanox only. For additional bugs reported that are handled by both Mellanox and the community, please refer to GitHub.

| Item # | RM # | Issue |
| ------ | ---- | ----- |
| 1. | 2082958 | **Description:** Applying an ACL rule with the REDIRECT_ACTION attribute fails with errors.<br />**Keywords:** ACL<br />**Discovered in Version:** SONiC 201911_MUR3<br />**Fixed in Version:** SONiC 201911_MUR4 |
| 2. | 2269143 | **Description:** In some cases, error may occur when using MCION query on a module with types "sfp_rx_los_soft_en" or "sfp_tx_fault_soft_en" that enable rx_los/tx_fault read from the memory map.<br />**Keywords:** Modules<br />**Discovered in Version:** SONiC 201911_MUR3<br />**Fixed in Version:** SONiC 201911_MUR4 |
| 3. | 2268678 | **Description:** MSTP state is not updated correctly for ports in certain VLAG scenarios.<br />**Keywords:** LAG<br />**Discovered in Version:** SONiC 201911_MUR3<br />**Fixed in Version:** SONiC 201911_MUR4 |
| 4. | 2036664 | **Description:** "show ip interface" shows the phantom PortChannel interface that was configured following a configuration reload of a non-saved configuration.<br />**Keywords:** Portchannel<br />**Discovered in Version:** SONiC 201911<br />**Fixed in Version:** SONiC 201911_MUR4 |
| ... | ... | ... |
