---
title: What's New
author: NVIDIA
weight: 10
product: SONiC
version: 202012
siteSlug: sonic
---

This topic provides a list of changes and new features in SONiC version 202012, including NVIDIA Spectrum-specific enhancements and fixes.

| Feature/Change | Description |
| -------------- | ----------- |
| SN3420 modules | Added support for Finisar 1G 10km module (FTLF1318P3BTL) on SN3420 systems. |
| SN3420 modules | Added support for Finisar 1GBase-T 1G 100m module (FCLF8522P2BTL) on SN3420 systems. |
| SN3700, SN4700 cables | Added support for the following HDR OPNs on SN3700, SN4700 systems at rates of 200GbE:<br /><ul><li>MCP1650-HxxxEyy (copper cable)</li><li>MCP7H50-HxxxRyy (copper splitter cable)</li><li>MMA1T00-HS (transceiver)</li><li>MFS1S00-HxxxE (AOC)</li><li>MFS1S50-HxxxE (AOC splitter cable)</li></ul> |
| SN4600C ports | Added support for up to 5W on ports 49 to 64 on SN4600C system. |
| Policy-based hashing | Added support for *policy-based hashing* static configurations. For further information, see {{<link url="Equal-Cost-Multipathing-ECMP/#policy-based-hashing" text="Policy-based Hashing">}}. |
| Shared headroom | Added support for *shared headroom*. This capability is enabled for non-default SKUs, however, it can be enabled on any SKU based upon request. For further information, see {{<link url="QoS-and-Buffers/#shared-headroom-pool" text="Shared Headroom Pool">}}. |
| Warm reboot| {{<link url="Warm-Reboot">}} is now tested with different topologies and not just with the community T0 configuration. |
| Fast reboot | {{<link url="Fast-Reboot">}} is now tested with different topologies and not just with the community T0 configuration. |
| Fast reboot | {{<link url="Fast-Reboot">}} is supported on NVIDIA Spectrum-3 switch platforms. |
| System health and LED management | Added support for {{<link url="System-Health-and-LEDs" text="system health monitoring and LED management">}}. |
| Bug fixes | See <a href="Release-Notes/#issues-fixed-in-this-version">Issues Fixed in this Version</a>. |
<!-- | Physical entity MIB | Added support for physical entity MIB. |
| Proxy ARP | Added support for Proxy ARP not just for VNET use case. | -->

## Customer-affecting Changes

| Feature/Change | Description |
| -------------- | ----------- |
| What Just Happened | Various What Just Happened (WJH) commands have been changed to contain the `poll` option. For example, `show what-just-happened poll --aggregate`. For further information, see section {{<link url="What-Just-Happened">}}. |
| Platform FW utility | `fwutil` command version 2.0.0.0 is now available. For further information, see {{<link url="Platform-Firmware-Components">}}. |
<!-- | PSU Status | New command output for ‘show platform psustatus’. It now has additional 2 columns which are currently has no valuable information on Nvidia switches. New JSON format is available . | -->

## Release Notes

To see the list of known issues and issues that have been fixed, read the {{<link url="Release-Notes">}}.

## Supported Port Speeds

The following tables show supported port speeds for select switches with NVIDIA Spectrum ASICs.

### NVIDIA Spectrum-3 SN4700 Supported Port Speeds

<table>
  <tr>
   <th rowspan=2 valign=top>Speed [GbE]
   </th>
   <th rowspan=2 valign=top>Auto-neg
   </th>
   <th colspan=3 valign=top>Force
   </th>
   <th rowspan=2 valign=top>Cable / Modules
   </th>
   <th rowspan=2 valign=top>Cable Length [m]
   </th>
 </tr>
 <tr>
   <th valign=top>RS FEC
  </th>
  <th valign=top>FC FEC
  </th>
  <th valign=top>NO FEC
  </th>
 </tr>
 <tr>
  <td rowspan=2 valign=top>
  <p>400</p>
  </td>
  <td rowspan=2 valign=top>
  <p>&#9989;</p>
  </td>
  <td rowspan=2 valign=top>
  <p>&#9989;</p>
  <p>&nbsp;</p>
  </td>
  <td rowspan=2 valign=top>
  <p>&#10008;</p>
  </td>
  <td rowspan=2 valign=top>
  <p>&#10008;</p>
  </td>
  <td valign=top>
  <p>Optics</p>
  </td>
  <td valign=top>
  <p>Up to 5</p>
  </td>
 </tr>
 <tr>
  <td valign=top>
  <p>Copper</p>
  </td>
  <td valign=top>
  <p>Up to 2.5</p>
  </td>
 </tr>
 <tr>
  <td rowspan=2 valign=top>
  <p>200/<br>
  100 2x/<br>
  50 1x (PAM4)</p>
  </td>
  <td rowspan=2 valign=top>
  <p>&#9989;</p>
  <p>&nbsp;</p>
  </td>
  <td rowspan=2 valign=top>
  <p>&#9989;</p>
  <p>&nbsp;</p>
  </td>
  <td rowspan=2 valign=top>
  <p>&#10008;</p>
  </td>
  <td rowspan=2 valign=top>
  <p>&#10008;</p>
  </td>
  <td valign=top>
  <p>Optic</p>
  </td>
  <td valign=top>
  <p>Up to 5</p>
  </td>
 </tr>
 <tr>
  <td valign=top>
  <p>Copper</p>
  </td>
  <td valign=top>
  <p>Up to 2.5</p>
  </td>
 </tr>
 <tr>
  <td rowspan=2 valign=top>
  <p>100 (NRZ)</p>
  </td>
  <td rowspan=2 valign=top>
  <p>&#9989;</p>
  <p>&nbsp;</p>
  </td>
  <td rowspan=2 valign=top>
  <p>&#9989;</p>
  <p>&nbsp;</p>
  </td>
  <td rowspan=2 valign=top>
  <p>&#10008;</p>
  <p>&nbsp;</p>
  </td>
  <td rowspan=2 valign=top>
  <p>&#9989;</p>
  </td>
  <td valign=top>
  <p>Optic</p>
  </td>
  <td valign=top>
  <p>Up to 100</p>
  </td>
 </tr>
 <tr>
  <td valign=top>
  <p>Copper</p>
  </td>
  <td valign=top>
  <p>Up to 5</p>
  </td>
 </tr>
 <tr>
  <td rowspan=2 valign=top>
  <p>25/50 (NRZ)</p>
  </td>
  <td rowspan=2 valign=top>
  <p>&#9989;</p>
  <p>&nbsp;</p>
  </td>
  <td rowspan=2 valign=top>
  <p>&#9989;</p>
  <p>&nbsp;</p>
  </td>
  <td rowspan=2 valign=top>
  <p>&#9989;</p>
  </td>
  <td rowspan=2 valign=top>
  <p>&#9989;</p>
  <p>&nbsp;</p>
  </td>
  <td valign=top>
  <p>Optic</p>
  </td>
  <td valign=top>
  <p>Up to 100</p>
  </td>
 </tr>
 <tr>
  <td valign=top>
  <p>Copper</p>
  </td>
  <td valign=top>
  <p>Up to 5</p>
  </td>
 </tr>
 <tr>
  <td rowspan=2 valign=top>
  <p>10/40</p>
  </td>
  <td rowspan=2 valign=top>
  <p>&#9989;</p>
  </td>
  <td rowspan=2 valign=top>
  <p>&#10008;</p>
  </td>
  <td rowspan=2 valign=top>
  <p>&#9989;</p>
  </td>
  <td rowspan=2 valign=top>
  <p>&#9989;</p>
  </td>
  <td valign=top>
  <p>Optic</p>
  </td>
  <td valign=top>
  <p>Up to 100</p>
  </td>
 </tr>
 <tr>
  <td valign=top>
  <p>Copper</p>
  </td>
  <td valign=top>
  <p>Up to 5</p>
  </td>
 </tr>
 <tr>
  <td valign=top>
  <p>1</p>
  </td>
  <td valign=top>
  <p>&#9989;</p>
  </td>
  <td valign=top>
  <p>&#10008;</p>
  </td>
  <td valign=top>
  <p>&#10008;</p>
  </td>
  <td valign=top>
  <p>&#9989;</p>
  </td>
  <td valign=top>
  <p>Optic/Copper</p>
  </td>
  <td valign=top>
  <p>Up to 5</p>
  </td>
 </tr>
</table>

### NVIDIA Spectrum-3 SN4600C Supported Port Speeds

<table>
  <tr>
   <th rowspan=2 valign=top>Speed [GbE]
   </th>
   <th rowspan=2 valign=top>Auto-neg
   </th>
   <th colspan=3 valign=top>Force
   </th>
   <th rowspan=2 valign=top>Cable / Modules
   </th>
   <th rowspan=2 valign=top>Cable Length [m]
   </th>
 </tr>
 <tr>
   <th valign=top>RS FEC
  </th>
  <th valign=top>FC FEC
  </th>
  <th valign=top>NO FEC
  </th>
 </tr>
 <tr>
  <td rowspan=2 valign=top>
  <p>100 (NRZ)</p>
  </td>
  <td rowspan=2 valign=top>
  <p>&#9989;</p>
  <p>&nbsp;</p>
  </td>
  <td rowspan=2 valign=top>
  <p>&#9989;</p>
  <p>&nbsp;</p>
  </td>
  <td rowspan=2 valign=top>
  <p>&#10008;</p>
  <p>&nbsp;</p>
  </td>
  <td rowspan=2 valign=top>
  <p>&#9989;</p>
  </td>
  <td valign=top>
  <p>Optic</p>
  </td>
  <td valign=top>
  <p>Up to 100</p>
  </td>
 </tr>
 <tr>
  <td valign=top>
  <p>Copper</p>
  </td>
  <td valign=top>
  <p>Up to 3</p>
  </td>
 </tr>
 <tr>
  <td rowspan=2 valign=top>
  <p>25/50 (NRZ)</p>
  </td>
  <td rowspan=2 valign=top>
  <p>&#9989;</p>
  <p>&nbsp;</p>
  </td>
  <td rowspan=2 valign=top>
  <p>&#9989;</p>
  <p>&nbsp;</p>
  </td>
  <td rowspan=2 valign=top>
  <p>&#9989;</p>
  </td>
  <td rowspan=2 valign=top>
  <p>&#9989;</p>
  <p>&nbsp;</p>
  </td>
  <td valign=top>
  <p>Optic</p>
  </td>
  <td valign=top>
  <p>Up to 100</p>
  </td>
 </tr>
 <tr>
  <td valign=top>
  <p>Copper</p>
  </td>
  <td valign=top>
  <p>Up to 5</p>
  </td>
 </tr>
 <tr>
  <td rowspan=2 valign=top>
  <p>10/40</p>
  </td>
  <td rowspan=2 valign=top>
  <p>&#9989;</p>
  </td>
  <td rowspan=2 valign=top>
  <p>&#10008;</p>
  </td>
  <td rowspan=2 valign=top>
  <p>&#9989;</p>
  </td>
  <td rowspan=2 valign=top>
  <p>&#9989;</p>
  </td>
  <td valign=top>
  <p>Optic</p>
  </td>
  <td valign=top>
  <p>Up to 100</p>
  </td>
 </tr>
 <tr>
  <td valign=top>
  <p>Copper</p>
  </td>
  <td valign=top>
  <p>Up to 3</p>
  </td>
 </tr>
 <tr>
  <td valign=top>
  <p>1</p>
  </td>
  <td valign=top>
  <p>&#9989;</p>
  </td>
  <td valign=top>
  <p>&#10008;</p>
  </td>
  <td valign=top>
  <p>&#10008;</p>
  </td>
  <td valign=top>
  <p>&#9989;</p>
  </td>
  <td valign=top>
  <p>Optic/Copper</p>
  </td>
  <td valign=top>
  <p>Up to 5</p>
  </td>
 </tr>
</table>

### NVIDIA Spectrum-2 SN3800 Series Supported Port Speeds

<table>
  <tr>
   <th rowspan=2 valign=top>Speed [GbE]
   </th>
   <th rowspan=2 valign=top>Auto-neg
   </th>
   <th colspan=3 valign=top>Force
   </th>
   <th rowspan=2 valign=top>Cable / Modules
   </th>
   <th rowspan=2 valign=top>Cable Length [m]
   </th>
   <th rowspan=2 valign=top>Comments</th>
 </tr>
 <tr>
   <th valign=top>RS FEC
  </th>
  <th valign=top>FC FEC
  </th>
  <th valign=top>NO FEC
  </th>
 </tr>
 <tr>
  <td rowspan=2 valign=top>
  <p>100 (NRZ)</p>
  </td>
  <td rowspan=2 valign=top>
  <p>&#10008;</p>
  <p>&nbsp;</p>
  </td>
  <td rowspan=2 valign=top>
  <p>&#9989;</p>
  <p>&nbsp;</p>
  </td>
  <td rowspan=2 valign=top>
  <p>&#10008;</p>
  <p>&nbsp;</p>
  </td>
  <td rowspan=2 valign=top>
  <p>&#9989;</p>
  </td>
  <td valign=top>
  <p>Optic</p>
  </td>
  <td valign=top>
  <p>Up to 30</p>
  </td>
  <td rowspan=2 valign=top>N/A</td>
 </tr>
 <tr>
  <td valign=top>
  <p>Copper</p>
  </td>
  <td valign=top>
  <p>Up to 5</p>
  </td>
 </tr>
 <tr>
  <td rowspan=2 valign=top>
  <p>25/50 (NRZ)</p>
  </td>
  <td rowspan=2 valign=top>
  <p>&#10008;</p>
  <p>&nbsp;</p>
  </td>
  <td rowspan=2 valign=top>
  <p>&#9989;</p>
  <p>&nbsp;</p>
  </td>
  <td rowspan=2 valign=top>
  <p>&#9989;</p>
  </td>
  <td rowspan=2 valign=top>
  <p>&#9989;</p>
  <p>&nbsp;</p>
  </td>
  <td valign=top>
  <p>Optic</p>
  </td>
  <td valign=top>
  <p>Up to 30</p>
  </td>
  <td rowspan=2 valign=top>N/A</td>
 </tr>
 <tr>
  <td valign=top>
  <p>Copper</p>
  </td>
  <td valign=top>
  <p>Up to 5</p>
  </td>
 </tr>
 <tr>
  <td rowspan=2 valign=top>
  <p>10/40</p>
  </td>
  <td rowspan=2 valign=top>
  <p>&#10008;</p>
  </td>
  <td rowspan=2 valign=top>
  <p>&#10008;</p>
  </td>
  <td rowspan=2 valign=top>
  <p>&#10008;</p>
  </td>
  <td rowspan=2 valign=top>
  <p>&#9989;</p>
  </td>
  <td valign=top>
  <p>Optic</p>
  </td>
  <td valign=top>
  <p>Up to 30</p>
  </td>
  <td rowspan=2 valign=top>10GBASE-T modules are not supported</td>
 </tr>
 <tr>
  <td valign=top>
  <p>Copper</p>
  </td>
  <td valign=top>
  <p>Up to 3</p>
  </td>
 </tr>
</table>

### NVIDIA Spectrum-2 SN3700 Supported Port Speeds

<table>
  <tr>
   <th rowspan=2 valign=top>Speed [GbE]
   </th>
   <th rowspan=2 valign=top>Auto-neg
   </th>
   <th colspan=3 valign=top>Force
   </th>
   <th rowspan=2 valign=top>Cable / Modules
   </th>
   <th rowspan=2 valign=top>Cable Length [m]
   </th>
 </tr>
 <tr>
   <th valign=top>RS FEC
  </th>
  <th valign=top>FC FEC
  </th>
  <th valign=top>NO FEC
  </th>
 </tr>
 <tr>
  <td rowspan=3 valign=top>
  <p>200/<br>
  100 2x/<br>
  50 1x (PAM4)**</p>
  </td>
  <td rowspan=3 valign=top>
  <p>&#9989;</p>
  <p>&nbsp;</p>
  </td>
  <td rowspan=3 valign=top>
  <p>&#9989;</p>
  <p>&nbsp;</p>
  </td>
  <td rowspan=3 valign=top>
  <p>&#10008;</p>
  </td>
  <td rowspan=3 valign=top>
  <p>&#10008;</p>
  </td>
  <td valign=top>
  <p>Optic</p>
  </td>
  <td valign=top>
  <p>Up to 30</p>
  </td>
 </tr>
 <tr>
  <td valign=top>
  <p>AOM*</p>
  </td>
  <td valign=top>
  <p>Up to 100</p>
  </td>
 </tr>
 <tr>
  <td valign=top>
  <p>Copper</p>
  </td>
  <td valign=top>
  <p>Up to 2</p>
  </td>
 </tr>
 <tr>
  <td rowspan=3 valign=top>
  <p>100 (NRZ)</p>
  </td>
  <td rowspan=3 valign=top>
  <p>&#9989;</p>
  <p>&nbsp;</p>
  </td>
  <td rowspan=3 valign=top>
  <p>&#9989;</p>
  <p>&nbsp;</p>
  </td>
  <td rowspan=3 valign=top>
  <p>&#10008;</p>
  <p>&nbsp;</p>
  </td>
  <td rowspan=3 valign=top>
  <p>&#9989;</p>
  </td>
  <td valign=top>
  <p>Optic</p>
  </td>
  <td valign=top>
  <p>Up to 100</p>
  </td>
 </tr>
 <tr>
  <td valign=top>
  <p>AOM*</p>
  </td>
  <td valign=top>
  <p>Up to 80km</p>
  </td>
 </tr>
 <tr>
  <td valign=top>
  <p>Copper</p>
  </td>
  <td valign=top>
  <p>Up to 5</p>
  </td>
 </tr>
 <tr>
  <td rowspan=3 valign=top>
  <p>25/50 (NRZ)</p>
  </td>
  <td rowspan=3 valign=top>
  <p>&#9989;</p>
  <p>&nbsp;</p>
  </td>
  <td rowspan=3 valign=top>
  <p>&#9989;</p>
  <p>&nbsp;</p>
  </td>
  <td rowspan=3 valign=top>
  <p>&#9989;</p>
  </td>
  <td rowspan=3 valign=top>
  <p>&#9989;</p>
  <p>&nbsp;</p>
  </td>
  <td valign=top>
  <p>Optic</p>
  </td>
  <td valign=top>
  <p>Up to 100</p>
  </td>
 </tr>
 <tr>
  <td valign=top>
  <p>AOM*</p>
  </td>
  <td valign=top>
  <p>Up to 10km</p>
  </td>
 </tr>
 <tr>
  <td valign=top>
  <p>Copper</p>
  </td>
  <td valign=top>
  <p>Up to 5</p>
  </td>
 </tr>
 <tr>
  <td rowspan=3 valign=top>
  <p>10/40</p>
  </td>
  <td rowspan=3 valign=top>
  <p>&#9989;</p>
  </td>
  <td rowspan=3 valign=top>
  <p>&#10008;</p>
  </td>
  <td rowspan=3 valign=top>
  <p>&#9989;</p>
  </td>
  <td rowspan=3 valign=top>
  <p>&#9989;</p>
  </td>
  <td valign=top>
  <p>Optic</p>
  </td>
  <td valign=top>
  <p>Up to 100</p>
  </td>
 </tr>
 <tr>
  <td valign=top>
  <p>AOM*</p>
  </td>
  <td valign=top>
  <p>Up to 10km</p>
  </td>
 </tr>
 <tr>
  <td valign=top>
  <p>Copper</p>
  </td>
  <td valign=top>
  <p>Up to 5</p>
  </td>
 </tr>
 <tr>
  <td rowspan=3 valign=top>
  <p>1</p>
  </td>
  <td rowspan=3 valign=top>
  <p>&#9989;</p>
  </td>
  <td rowspan=3 valign=top>
  <p>&#10008;</p>
  </td>
  <td rowspan=3 valign=top>
  <p>&#10008;</p>
  </td>
  <td rowspan=3 valign=top>
  <p>&#9989;</p>
  </td>
  <td valign=top>
  <p>Optic</p>
  </td>
  <td valign=top>
  <p>Up to 100</p>
  </td>
  </tr>
  <tr>
  <td valign=top>
  <p>AOM*</p>
  </td>
  <td valign=top>
  <p>Up to 80km</p>
  </td>
 </tr>
 <tr>
  <td valign=top>
  <p>Copper</p>
  </td>
  <td valign=top>
  <p>Up to 5</p>
  </td>
 </tr>
 </table>

\* Link to supported AOM.<br />** 200GbE is only supported on SN3700 switches.

### NVIDIA Spectrum SN2000 Supported Port Speeds

<table>
  <tr>
   <th rowspan=2 valign=top>Speed [GbE]
   </th>
   <th rowspan=2 valign=top>Auto-neg
   </th>
   <th colspan=3 valign=top>Force
   </th>
   <th rowspan=2 valign=top>Cable / Modules
   </th>
   <th rowspan=2 valign=top>Cable Length [m]
   </th>
 </tr>
 <tr>
   <th valign=top>RS FEC
  </th>
  <th valign=top>FC FEC
  </th>
  <th valign=top>NO FEC
  </th>
 </tr>
 <tr>
  <td rowspan=3 valign=top>
  <p>100</p>
  </td>
  <td rowspan=3 valign=top>
  <p>&#9989;</p>
  </td>
  <td rowspan=3 valign=top>
  <p>&#9989;</p>
  </td>
  <td rowspan=3 valign=top>
  <p>&#9989;</p>
  </td>
  <td rowspan=3 valign=top>
  <p>&#9989;</p>
  </td>
  <td valign=top>
  <p>Optic</p>
  </td>
  <td valign=top>
  <p>Up to 100</p>
  </td>
 </tr>
 <tr>
  <td valign=top>
  <p>AOM*</p>
  </td>
  <td valign=top>
  <p>Up to 80km</p>
  </td>
 </tr>
 <tr>
  <td valign=top>
  <p>Copper</p>
  </td>
  <td valign=top>
  <p>Up to 5</p>
  </td>
 </tr>
 <tr>
  <td rowspan=3 valign=top>
  <p>25/50</p>
  </td>
  <td rowspan=3 valign=top>
  <p>&#9989;</p>
  </td>
  <td rowspan=3 valign=top>
  <p>&#9989;</p>
  </td>
  <td rowspan=3 valign=top>
  <p>&#9989;</p>
  </td>
  <td rowspan=3 valign=top>
  <p>&#9989;</p>
  </td>
  <td valign=top>
  <p>Optic</p>
  </td>
  <td valign=top>
  <p>Up to 100</p>
  </td>
 </tr>
 <tr>
  <td valign=top>
  <p>AOM*</p>
  </td>
  <td valign=top>
  <p>Up to 10km</p>
  </td>
 </tr>
 <tr>
  <td valign=top>
  <p>Copper</p>
  </td>
  <td valign=top>
  <p>Up to 5</p>
  </td>
 </tr>
 <tr>
  <td rowspan=3 valign=top>
  <p>10/40</p>
  </td>
  <td rowspan=3 valign=top>
  <p>&#9989;</p>
  </td>
  <td rowspan=3 valign=top>
  <p>&#10008;</p>
  </td>
  <td rowspan=3 valign=top>
  <p>&#9989;</p>
  </td>
  <td rowspan=3 valign=top>
  <p>&#9989;</p>
  </td>
  <td valign=top>
  <p>Optic</p>
  </td>
  <td valign=top>
  <p>Up to 100</p>
  </td>
 </tr>
 <tr>
  <td valign=top>
  <p>AOM*</p>
  </td>
  <td valign=top>
  <p>Up to 80km</p>
  </td>
 </tr>
 <tr>
  <td valign=top>
  <p>Copper</p>
  </td>
  <td valign=top>
  <p>Up to 5</p>
  </td>
 </tr>
 <tr>
  <td rowspan=2 valign=top>
  <p>1</p>
  </td>
  <td rowspan=2 valign=top>
  <p>&#9989;</p>
  </td>
  <td rowspan=2 valign=top>
  <p>&#10008;</p>
  </td>
  <td rowspan=2 valign=top>
  <p>&#10008;</p>
  </td>
  <td rowspan=2 valign=top>
  <p>&#9989;</p>
  </td>
  <td valign=top>
  <p>Optic</p>
  </td>
  <td valign=top>
  <p>Up to 100</p>
  </td>
  </tr>
  <tr>
  <td valign=top>
  <p>Copper</p>
  </td>
  <td valign=top>
  <p>Up to 5</p>
  </td>
 </tr>
 </table>

\* Link to supported AOM.
