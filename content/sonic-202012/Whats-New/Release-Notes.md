---
title: Release Notes
author: NVIDIA
weight: 20
product: SONiC
version: 202012
siteSlug: sonic
type: rn
---

These are the release notes for SONiC software version 202012 on NVIDIA® Mellanox Spectrum®-based switches. However, these release notes are simply an upstream version of the pure SONiC release available on GitHub.

## Release Notes Update History

| Revision | Date | Description |
| -------- | ---- | ----------- |
| Rev 1.0 | April 20, 2021 | Initial release of these release notes. |

## SONiC General Support

### SONiC Versions

| Branch| Hash | Location |
| ----- | ---- | -------- |
| SONiC 202012 |  | https://github.com/Azure/sonic-buildimage/tree/202012  |

### Package Content

This release is based on the SONiC 202012 sonic-buildimage hash. It contains the following components:

| Switch Components | Version | Additional Information |
| ----------------- | ------- | ---------------------- |
| Mellanox Spectrum-3 Firmware | 30.2008.2416 | |
| Mellanox Spectrum-2 Firmware | 29.2008.2416 | |
| Mellanox Spectrum Firmware | 13.2008.2416 | |
| SDK | 4.4.2416 | SDK API can be found at: https://github.com/Mellanox/SwitchRouterSDK-interfaces |
| SAI | 1.18.1.0 | Mellanox SAI implementation can be found at: https://github.com/Mellanox/SAI-Implementation/tree/sonic2012 based on commit https://github.com/Mellanox/SAI-Implementation/commit/8dc2afd21ff6578cd0736b70aaa6ce5f1135265d |
| Mellanox Firmware Tools (MFT) | 4.16.0-105 | {{<exlink url="https://docs.mellanox.com/display/MFTv4160/Release+Notes" text="Release Notes">}}<br />{{<exlink url="https://docs.mellanox.com/display/MFTv4160/Introduction" text="User Manual">}} |

### Application Extensions

The following application extension was developed by Mellanox:

| Application Extension | Version | Additional Information |
| --------------------- | ------- | ---------------------- |
| What-Just-Happened | TBD | For further information, see {{<link url="What-Just-Happened">}}. |

## Issues Fixed in this Version

This section provides only a list of bugs fixed only by Mellanox in this version.

Additional bugs reported are handled by both Mellanox and the community as part of the 202012 release. For additional information, please refer to the {{<exlink url="https://github.com/Azure/sonic-buildimage/issues" text="Azure GitHub">}} site.

<table>
  <tr>
   <th valign=top>RM #</th>
   <th valign=top>Issue</th>
  </tr>
 <tr>
  <td rowspan=4 valign=top>
  <p>2045019</p>
  </td>
  <td valign=top>
  <p><b>Description:</b> Removing a VLAN which still has a member
  port results in failure, although no error indication is provided in the CLI.</p>
  </td>
 </tr>
 <tr>
  <td valign=top>
  <p><b>Keywords:</b> VLAN</p>
  </td>
 </tr>
 <tr>
  <td valign=top>
  <p><b>Discovered in Version: </b>SONiC 201911</p>
  </td>
 </tr>
 <tr>
  <td valign=top>
  <p><strong>Fixed in Version: </strong>SONiC
  202012</p>
  </td>
 </tr>
 <tr>
  <td rowspan=4 valign=top>
  <p>2071829</p>
  </td>
  <td valign=top>
  <p><b>Description:</b> The validation of the <code>config portchannel member add</code> command is missing when adding a port that has already been a member of another portchannel interface.</p>
  </td>
 </tr>
 <tr>
  <td valign=top>
  <p><b>Keywords:</b> portchannel</p>
  </td>
 </tr>
 <tr>
  <td valign=top>
  <p><b>Discovered in Version: </b>SONiC 201911</p>
  </td>
 </tr>
 <tr>
  <td valign=top>
  <p><strong>Fixed in Version: </strong>SONiC
  202012</p>
  </td>
 </tr>
 <tr>
  <td rowspan=4 valign=top>
  <p>2198406</p>
  </td>
  <td valign=top>
  <p><b>Description:</b> In rare cases, high pre-FEC is
  experienced on MMA1B00-C100D optic cables (post-FEC is clean).</p>
  </td>
 </tr>
 <tr>
  <td valign=top>
  <p><b>Keywords:</b> SN4600C, Cables</p>
  </td>
 </tr>
 <tr>
  <td valign=top>
  <p><b>Discovered in Version: </b>SONiC 201911_MUR3</p>
  </td>
 </tr>
 <tr>
  <td valign=top>
  <p><strong>Fixed in Version: </strong>SONiC
  202012</p>
  </td>
 </tr>
 <tr>
  <td rowspan=4 valign=top>
  <p>2229399</p>
  </td>
  <td valign=top>
  <p><b>Description:</b> Tx settings of the line card in SN3800 fail eye measurement.</p>
  </td>
 </tr>
 <tr>
  <td valign=top>
  <p><b>Keywords:</b> Spectrum-2, SN3800, Tx settings</p>
  </td>
 </tr>
 <tr>
  <td valign=top>
  <p><b>Discovered in Version:</b> SONiC
  201911_MUR5</p>
  </td>
 </tr>
 <tr>
  <td valign=top>
  <p><strong>Fixed in Version: </strong>SONiC 202012</p>
  </td>
 </tr>
 <tr>
  <td rowspan=4 valign=top>
  <p>2135522</p>
  </td>
  <td valign=top>
  <p><b>Description:</b> When sending a control packet that is larger than the port MTU, the control-sending queue will get stuck.</p>
  </td>
 </tr>
 <tr>
  <td valign=top>
  <p><b>Keywords:</b> Driver, MTU</p>
  </td>
 </tr>
 <tr>
  <td valign=top>
  <p><b>Discovered in Version:</b> SONiC
  201911_MUR5</p>
  </td>
 </tr>
 <tr>
  <td valign=top>
  <p><strong>Fixed in Version: </strong>SONiC
  202012</p>
  </td>
 </tr>
 <tr>
  <td rowspan=4 valign=top >
  <p>2407901</p>
  </td>
  <td>
  <p><strong>Description:</strong>CLI
  commands used to enable PFCWD do not work.</p>
  </td>
 </tr>
 <tr>
  <td>
  <p><strong>Keywords:</strong> PFCWD,
  CLI</p>
  </td>
 </tr>
 <tr>
  <td>
  <p><strong>Discovered in Version:</strong>
  SONiC 201911_MUR6</p>
  </td>
 </tr>
 <tr>
  <td>
  <p><strong>Fixed in Version: </strong>SONiC
  202012</p>
  </td>
 </tr>
 <tr>
  <td rowspan=4 valign=top >
  <p>2435816</p>
  </td>
  <td>
  <p><strong>Description:</strong> Interface
  PortChannel cannot get an assigned IP when 80 PortChannel RIF are defined.</p>
  </td>
 </tr>
 <tr>
  <td>
  <p><strong>Keywords:</strong> IP
  assignment, PortChannel, RIF</p>
  </td>
 </tr>
 <tr>
  <td>
  <p><strong>Discovered in Version:</strong>
  SONiC 201911_MUR6</p>
  </td>
 </tr>
 <tr>
  <td>
  <p><strong>Fixed in Version: </strong>SONiC
  202012</p>
  </td>
 </tr>
 <tr>
  <td rowspan=4 valign=top >
  <p>2447853</p>
  </td>
  <td>
  <p><b>Description:</b> What Just Happened consumes almost 100% CPU usage while not reading
  data.</p>
  </td>
 </tr>
 <tr>
  <td>
  <p><b>Keywords:</b> What-Just-Happened</p>
  </td>
 </tr>
 <tr>
  <td>
  <p><b>Discovered in Version: </b>SONiC 201911_MUR6</p>
  </td>
 </tr>
 <tr>
  <td>
  <p><b>Fixed in Version: </b>SONiC 202012</p>
  </td>
 </tr>
 <tr>
  <td rowspan=4 valign=top>
  <p>2367239</p>
  </td>
  <td valign=top>
  <p><b>Description:</b> <code>snmpagent</code> allocates (hardcoded) only 4 lanes for each transceiver. Therefore, the SNMP query returns the sensors of only the first 4 lanes of a QSFP-DD (400GbE) cable which has 8 lanes. </p>
  </td>
 </tr>
 <tr>
  <td valign=top>
  <p><b>Keywords:</b> SNMP MIB</p>
  </td>
 </tr>
 <tr>
  <td valign=top>
  <p><b>Discovered in Version:</b> SONiC
  201911_MUR6</p>
  </td>
 </tr>
 <tr>
  <td valign=top>
  <p><b>Fixed in Version: </b>SONiC 202012</p>
  </td>
 </tr>
 <tr>
  <td rowspan=4 valign=top>
  <p>2384299</p>
  </td>
  <td valign=top>
  <p><b>Description:</b> On occasion, when using Dell QSFP28 copper cable in 40G (4x10G) split mode, the link goes down.</p>
  </td>
 </tr>
 <tr>
  <td valign=top>
  <p><b>Keywords:</b> SN4700, Cables, Split</p>
  </td>
 </tr>
 <tr>
  <td valign=top>
  <p><b>Discovered in Version:</b> SONiC
  201911_MUR6</p>
  </td>
 </tr>
 <tr>
  <td valign=top>
  <p><b>Fixed in Version: </b>SONiC 202012</p>
  </td>
 </tr>
 <tr>
  <td rowspan=4 valign=top>
  <p>2407901</p>
  </td>
  <td valign=top>
  <p><b>Description:</b> The command <code>config pfcwd start --action drop ports all detection-time 400 --restoration-time 400</code> fails due to invalid options: ports and detection-time.</p>
  </td>
 </tr>
 <tr>
  <td valign=top>
  <p><b>Keywords:</b> PFCWD</p>
  </td>
 </tr>
 <tr>
  <td valign=top>
  <p><b>Discovered in Version:</b> SONiC
  201911_MUR6</p>
  </td>
 </tr>
 <tr>
  <td valign=top>
  <p><b>Fixed in Version: </b>SONiC 202012</p>
  </td>
 </tr>
 <tr>
  <td rowspan=4 valign=top>
  <p>2409755</p>
  </td>
  <td valign=top>
  <p><b>Description:</b> On rare cases, when reading the
  wrong critical thermal thresholds of a transceiver may lead to software
  thermal shutdown resulting in system restart. </p>
  </td>
 </tr>
 <tr>
  <td valign=top>
  <p><b>Keywords:</b> ISSU</p>
  </td>
 </tr>
 <tr>
  <td valign=top>
  <p><b>Discovered in Version:</b> SONiC
  201911_MUR6</p>
  </td>
 </tr>
 <tr>
  <td valign=top>
  <p><b>Fixed in Version: </b>SONiC 202012</p>
  </td>
 </tr>
 <tr>
  <td rowspan=4 valign=top>
  <p>2431486</p>
  </td>
  <td valign=top>
  <p><b>Description:</b> When a switch is rebooted with locked optical transceivers in split mode, the firmware may get stuck.</p>
  </td>
 </tr>
 <tr>
  <td valign=top>
  <p><b>Keywords:</b> Optical Transceivers, Split Mode</p>
  </td>
 </tr>
 <tr>
  <td valign=top>
  <p><b>Discovered in Version:</b> SONiC
  201911_MUR6</p>
  </td>
 </tr>
 <tr>
  <td valign=top>
  <p><b>Fixed in Version: </b>SONiC 202012</p>
  </td>
 </tr>
 <tr>
  <td rowspan=4 valign=top>
  <p>2355323</p>
  </td>
  <td valign=top>
  <p><b>Description:</b> When moving the port-status of two
  or more ingress ports up or down, congestion egress events send events
  of threshold crossing without an actual reason, though the congestion histogram
  remains unaffected.</p>
  </td>
 </tr>
 <tr>
  <td valign=top>
  <p><b>Keywords:</b> Telemetry</p>
  </td>
 </tr>
 <tr>
  <td valign=top>
  <p><b>Discovered in Version:</b> SONiC
  201911_MUR6</p>
  </td>
 </tr>
 <tr>
  <td valign=top>
  <p><b>Fixed in Version: </b>SONiC 202012</p>
  </td>
 </tr>
 <tr>
  <td rowspan=4 valign=top>
  <p>2407915</p>
  </td>
  <td valign=top>
  <p><b>Description:</b> In Spectrum-3 while using optical cable MFS1S50-H003E in split 4x1 mode in PAM4, when one port is toggled, all three other ports go down.</p>
  </td>
 </tr>
 <tr>
  <td valign=top>
  <p><b>Keywords:</b> Ethernet, Spectrum-3, PAM4, Optic
  Cables</p>
  </td>
 </tr>
 <tr>
  <td valign=top>
  <p><b>Discovered in Version:</b> SONiC
  201911_MUR6</p>
  </td>
 </tr>
 <tr>
  <td valign=top>
  <p><b>Fixed in Version: </b>SONiC 202012</p>
  </td>
 </tr>
 <tr>
  <td rowspan=4 valign=top>
  <p>2405266</p>
  </td>
  <td valign=top>
  <p><b>Description:</b> On SN3800 systems, when the port is
  a member of a LAG, after a warm boot and port toggle on the peer-side, the
  port remains down. </p>
  </td>
 </tr>
 <tr>
  <td valign=top>
  <p><b>Keywords:</b> Ethernet, Spectrum-3, DAC</p>
  </td>
 </tr>
 <tr>
  <td valign=top>
  <p><b>Discovered in Version:</b> SONiC
  201911_MUR6</p>
  </td>
 </tr>
 <tr>
  <td valign=top>
  <p><b>Fixed in Version: </b>SONiC 202012</p>
  </td>
 </tr>
 <tr>
  <td rowspan=4 valign=top>
  <p>2176790</p>
  </td>
  <td valign=top>
  <p><b>Description:</b> On rare occasions packets loss may
  be experienced on SN3800 due to signal integrity issues.</p>
  </td>
 </tr>
 <tr>
  <td valign=top>
  <p><b>Keywords:</b> Spectrum-2, SN3800, BER</p>
  </td>
 </tr>
 <tr>
  <td valign=top>
  <p><b>Discovered in Version:</b> SONiC
  201911_MUR6</p>
  </td>
 </tr>
 <tr>
  <td valign=top>
  <p><b>Fixed in Version: </b>SONiC 202012</p>
  </td>
 </tr>
 <tr>
  <td rowspan=4 valign=top>
  <p>1883103</p>
  </td>
  <td valign=top>
  <p><b>Description:</b> When connecting SN3700 at 200GbE to
  Ixia K400, Ixia receives CRC errors.</p>
  </td>
 </tr>
 <tr>
  <td valign=top>
  <p><b>Keywords:</b> Spectrum-2, SN3700, Ixia, CRC</p>
  </td>
 </tr>
 <tr>
  <td valign=top>
  <p><b>Discovered in Version: </b>SONiC 201911_MUR6</p>
  </td>
 </tr>
 <tr>
  <td valign=top>
  <p><b>Fixed in Version: </b>SONiC 202012</p>
  </td>
 </tr>
 <tr>
  <td rowspan=4 valign=top>
  <p>2320854</p>
  </td>
  <td valign=top>
  <p><b>Description:</b> When working in 400GbE, deleting
  the headroom configuration (changing buffer size to zero) on the fly may cause
  continual packet drops.</p>
  </td>
 </tr>
 <tr>
  <td valign=top>
  <p><b>Keywords:</b> Speed, 400GbE</p>
  </td>
 </tr>
 <tr>
  <td valign=top>
  <p><b>Discovered in Version: </b>SONiC 201911_MUR6</p>
  </td>
 </tr>
 <tr>
  <td valign=top>
  <p><b>Fixed in Version: </b>SONiC 202012</p>
  </td>
 </tr>
 <tr>
  <td rowspan=4 valign=top>
  <p>2457801</p>
  </td>
  <td valign=top>
  <p><b>Description:</b> On Spectrum systems, 10GbE/1GbE
  Transceiver (FTLX8574D3BCV) stopped working after firmware upgrade. </p>
  </td>
 </tr>
 <tr>
  <td valign=top>
  <p><b>Keywords:</b> Firmware Upgrade, Transceiver</p>
  </td>
 </tr>
 <tr>
  <td valign=top>
  <p><b>Discovered in Version: </b>SONiC 201911_MUR6</p>
  </td>
 </tr>
 <tr>
  <td valign=top>
  <p><b>Fixed in Version: </b>SONiC 202012</p>
  </td>
 </tr>
 <tr>
  <td rowspan=4 valign=top>
  <p>2432630</p>
  </td>
  <td valign=top>
  <p><b>Description:</b> When the hardware-management driver
  tries to get the ASIC temperature from the firmware during a firmware
  upgrade, a random value appears outside of the temperature threshold, causing
  system thermal shutdown.</p>
  </td>
 </tr>
 <tr>
  <td valign=top>
  <p><b>Keywords:</b> ISSU, Driver, Firmware Upgrade</p>
  </td>
 </tr>
 <tr>
  <td valign=top>
  <p><b>Discovered in Version: </b>SONiC 201911_MUR6</p>
  </td>
 </tr>
 <tr>
  <td valign=top>
  <p><b>Fixed in Version: </b>SONiC 202012</p>
  </td>
 </tr>
 <tr>
  <td rowspan=4 valign=top>
  <p>2116499</p>
  </td>
  <td valign=top>
  <p><b>Description:</b> Everflow functionality does not work
  after warm reboot.</p>
  </td>
 </tr>
 <tr>
  <td valign=top>
  <p><b>Keywords:</b> Everflow, warm reboot</p>
  </td>
 </tr>
 <tr>
  <td valign=top>
  <p><b>Discovered in Version: </b>SONiC 201911</p>
  </td>
 </tr>
 <tr>
  <td valign=top>
  <p><b>Fixed in Version: </b>SONiC 202012</p>
  </td>
 </tr>
</table>

## Known Issues

For community-discovered limitations, please refer to the {{<exlink url="https://github.com/Azure/sonic-buildimage/issues" text="Azure GitHub">}} site.

<table>
 <thead>
  <tr>
   <th>
   <p><b>RM #</b></p>
   </th>
   <th>
   <p align=center style='text-align:center;'><b>Issue</b></p>
   </th>
  </tr>
 <tr>
  <td rowspan=4 valign=top>
  <p>2446581</p>
  </td>
  <td>
  <p><strong>Description:</strong> An
  error is logged when a MAC address that already exists on the FDB is learned
  from a different port.</p>
  </td>
 </tr>
 <tr>
  <td>
  <p><strong>Workaround:</strong> N/A</p>
  </td>
 </tr>
 <tr>
  <td>
  <p><strong>Keywords:</strong> MAC
  learning, FDB</p>
  </td>
 </tr>
 <tr>
  <td>
  <p><strong>Discovered in Version:</strong>
  SONiC 202012</p>
  </td>
 </tr>
 <tr>
  <td rowspan=4 valign=top>
  <p>2393635</p>
  </td>
  <td>
  <p><strong>Description:</strong> Warm reboot fails in case of corrupted <code>/host/warm-reboot/issu-bank.txt</code> file and the switch is in an inconsistent state afterwards.</p>
  </td>
 </tr>
 <tr>
  <td>
  <p><strong>Workaround:</strong> Follow the instructions printed in <code>/var/log/syslog</code>, or run the CLI command <code>warm-reboot -v</code> and then perform a cold reboot.</p>
  </td>
 </tr>
 <tr>
  <td>
  <p><strong>Keywords:</strong> ISSU</p>
  </td>
 </tr>
 <tr>
  <td>
  <p><strong>Discovered in Version:</strong>
  SONiC 202012</p>
  </td>
 </tr>
 <tr>
  <td rowspan=4 valign=top>
  <p>2571738</p>
  </td>
  <td valign=top>
  <p><b>Description:</b> When configuring seed=0, hash distribution
  is not optimal.</p>
  </td>
 </tr>
 <tr>
  <td valign=top>
  <p><b>Workaround:</b> Avoid seed=0 configuration.</p>
  </td>
 </tr>
 <tr>
  <td valign=top>
  <p><b>Keywords:</b> LAG, HASH</p>
  </td>
 </tr>
 <tr>
  <td valign=top>
  <p><b>Discovered in Version:</b> SONiC 202012</p>
  </td>
 </tr>
 <tr>
  <td rowspan=4 valign=top>
  <p>-</p>
  </td>
  <td valign=top>
  <p><b>Description:</b> Dynamic port breakout is not supported.</p>
  <p><b>Note:</b> All issues related to this feature are reported on GitHub and are being handled by the community owner.</p>
  </td>
 </tr>
 <tr>
  <td valign=top>
  <p><b>Workaround:</b> N/A</p>
  </td>
 </tr>
 <tr>
  <td valign=top>
  <p><b>Keywords:</b> port breakout</p>
  </td>
 </tr>
 <tr>
  <td valign=top>
  <p><b>Discovered in Version:</b> SONiC 202012</p>
  </td>
 </tr>
 <tr>
  <td rowspan=4 valign=top>
  <p><o:p> </o:p></p>
  </td>
  <td valign=top>
  <p><b>Description:</b> sFLow is not supported on NVIDIA switches.</p>
  </td>
 </tr>
 <tr>
  <td valign=top>
  <p><b>Workaround:</b> N/A</p>
  </td>
 </tr>
 <tr>
  <td valign=top>
  <p><b>Keywords:</b> sflow</p>
  </td>
 </tr>
 <tr>
  <td valign=top>
  <p><b>Discovered in Version:</b> SONiC 202012</p>
  </td>
 </tr>
 <tr>
  <td rowspan=4 valign=top>
  <p>2413409</p>
  </td>
  <td valign=top>
  <p><b>Description:</b> BER may be experienced when using
  5m DAC cables between SN4700 and SN2700 in 100GbE speed. </p>
  </td>
 </tr>
 <tr>
  <td valign=top>
  <p><b>Workaround:</b> N/A</p>
  </td>
 </tr>
 <tr>
  <td valign=top>
  <p><b>Keywords:</b> Ethernet, Spectrum-3, DAC</p>
  </td>
 </tr>
 <tr>
  <td valign=top>
  <p><b>Discovered in Version:</b> SONiC 201911_MUR6</p>
  </td>
 </tr>
 <tr>
  <td rowspan=4 valign=top>
  <p>2404336</p>
  
  </td>
  <td valign=top>
  <p><b>Description:</b> On very rare occasions, when connecting a DR4 PAM4 transceiver to a 100GbE DR1 NRZ, low BER may be experienced.</p>
  </td>
 </tr>
 <tr>
  <td valign=top>
  <p><b>Workaround:</b> N/A</p>
  </td>
 </tr>
 <tr>
  <td valign=top>
  <p><b>Keywords:</b> Ethernet, Spectrum-3, DR4</p>
  </td>
 </tr>
 <tr>
  <td valign=top>
  <p><b>Discovered in Version:</b> SONiC
  201911_MUR6</p>
  </td>
 </tr>
 <tr>
  <td rowspan=4 valign=top>
2322812
  </td>
  <td valign=top>
  <p><b>Description:</b> The interface name in unavailable
  if the port configuration is removed while using split configuration.</p>
  </td>
 </tr>
 <tr>
  <td valign=top>
  <p><b>Workaround:</b> N/A</p>
  </td>
 </tr>
 <tr>
  <td valign=top>
  <p><b>Keywords:</b> SNMP</p>
  </td>
 </tr>
 <tr>
  <td valign=top>
  <p><b>Discovered in Version:</b> SONiC
  201911_MUR6</p>
  </td>
 </tr>
 <tr>
  <td rowspan=4 valign=top>
  <p>2350845</p>
  </td>
  <td valign=top>
  <p><b>Description:</b> The <code>fast-reboot</code> command may fail if the portchannel
  is part of the VLAN.</p>
  </td>
 </tr>
 <tr>
  <td valign=top>
  <p><b>Workaround:</b> N/A</p>
  </td>
 </tr>
 <tr>
  <td valign=top>
  <p><b>Keywords:</b> Fastboot, VLAN</p>
  </td>
 </tr>
 <tr>
  <td valign=top>
  <p><b>Discovered in Version:</b> SONiC
  201911_MUR6</p>
  </td>
 </tr>
 <tr>
  <td rowspan=4 valign=top>
  <p>2393983</p>
  </td>
  <td valign=top>
  <p><b>Description:</b> CLI command <code>show priority-group watermark</code> returns zero value even if the headroom is occupied.</p>
  </td>
 </tr>
 <tr>
  <td valign=top>
  <p><b>Workaround:</b> N/A</p>
  </td>
 </tr>
 <tr>
  <td valign=top>
  <p><b>Keywords:</b> Headroom, Watermark</p>
  </td>
 </tr>
 <tr>
  <td valign=top>
  <p><b>Discovered in Version:</b> SONiC
  201911_MUR6</p>
  </td>
 </tr>
 <tr>
  <td rowspan=4 valign=top>
  <p>2395745</p>
  </td>
  <td valign=top>
  <p><b>Description:</b> COLORZ modules (IN-Q2AY2-41 , IN-Q2AY2-27) link up
  time increased to 85 seconds.</p>
  </td>
 </tr>
 <tr>
  <td valign=top>
  <p><b>Workaround:</b> N/A</p>
  </td>
 </tr>
 <tr>
  <td valign=top>
  <p><b>Keywords:</b> Modules, COLORZ</p>
  </td>
 </tr>
 <tr>
  <td valign=top>
  <p><b>Discovered in Version:</b> SONiC
  201911_MUR6</p>
  </td>
 </tr>
 <tr>
  <td rowspan=4 valign=top>
  <p>2373739</p>
  </td>
  <td valign=top>
  <p><b>Description:</b> On SN3800 systems, "Auto
  negotiation" drop reason is shown as "Other reason -".</p>
  </td>
 </tr>
 <tr>
  <td valign=top>
  <p><b>Workaround:</b> N/A</p>
  </td>
 </tr>
 <tr>
  <td valign=top>
  <p><b>Keywords:</b> What Just Happened, Auto
  negotiation</p>
  </td>
 </tr>
 <tr>
  <td valign=top>
  <p><b>Discovered in Version:</b> SONiC
  201911_MUR6</p>
  </td>
 </tr>
 <tr>
  <td rowspan=4 valign=top>
  <p>2373693</p>
  </td>
  <td valign=top>
  <p><b>Description:</b> On SN3800 systems, the layer 1 state change counter currently does not function properly. We do not recommend using it. </p>
  </td>
 </tr>
 <tr>
  <td valign=top>
  <p><b>Workaround:</b> N/A</p>
  </td>
 </tr>
 <tr>
  <td valign=top>
  <p><b>Keywords:</b> What Just Happened, State change
  counts</p>
  </td>
 </tr>
 <tr>
  <td valign=top>
  <p><b>Discovered in Version:</b> SONiC
  201911_MUR6</p>
  </td>
 </tr>
 <tr>
  <td rowspan=4 valign=top>
  <p>2074787</p>
  </td>
  <td valign=top>
  <p><b>Description:</b> The <code>show mac</code> command fails to show a learned MAC if a VLAN member is added in tagged mode.</p>
  </td>
 </tr>
 <tr>
  <td valign=top>
  <p><b>Workaround:</b> N/A</p>
  </td>
 </tr>
 <tr>
  <td valign=top>
  <p><b>Keywords:</b> FDB</p>
  </td>
 </tr>
 <tr>
  <td valign=top>
  <p><b>Discovered in Version:</b> SONiC
  201911_MUR6</p>
  </td>
 </tr>
 <tr>
  <td rowspan=4 valign=top>
  <p>2099346</p>
  </td>
  <td valign=top>
  <p><b>Description:</b> The <code>aclshow</code> utility output does not display counters for control plane ACLs.</p>
  </td>
 </tr>
 <tr>
  <td valign=top>
  <p><b>Workaround:</b> Run <code>sudo iptables -L -v -n</code> to display the counter fields for the control plane ACLs. </p>
  </td>
 </tr>
 <tr>
  <td valign=top>
  <p><b>Keywords:</b> aclshow control plane ACLs</p>
  </td>
 </tr>
 <tr>
  <td valign=top>
  <p><b>Discovered in Version:</b> SONiC 201911_MUR6</p>
  </td>
 </tr>
 <tr>
  <td rowspan=4 valign=top>
2382746
  </td>
  <td valign=top>
  <p><b>Description:</b> What Just Happened does not report a dropped packet when its dropped reason is <em>Unicast destination IP but multicast destination MAC</em>.</p><p>
  To receive this drop reason, you can use the customer WJH XML configuration
  file, and set the severity of it from ‘Invalid’ to any other severity.</p>
  </td>
 </tr>
 <tr>
  <td valign=top>
  <p><b>Workaround:</b> N/A</p>
  </td>
 </tr>
 <tr>
  <td valign=top>
  <p><b>Keywords:</b> What Just Happened, dropped packets</p>
  </td>
 </tr>
 <tr>
  <td valign=top>
  <p><b>Discovered in Version:</b> SONiC
  201911_MUR6</p>
  </td>
 </tr>
 <tr>
  <td rowspan=4 valign=top>
  <p>2376634</p>
  </td>
  <td valign=top>
  <p><b>Description:</b> Warm reboot on NVIDIA Spectrum-3 is not supported if using SONiC 201911_MUR5 <b>(HASH:</b>
  c453381aecfda14c276dcc7f8d357a034feb84b4) and below to reboot or upgrade to 201911_MUR6.</p>
  </td>
 </tr>
 <tr>
  <td valign=top>
  <p><b>Workaround:</b> N/A</p>
  </td>
 </tr>
 <tr>
  <td valign=top>
  <p><b>Keywords:</b> Warmboot, NVIDIA Spectrum-3</p>
  </td>
 </tr>
 <tr>
  <td valign=top>
  <p><b>Discovered in Version:</b> SONiC
  201911_MUR6</p>
  </td>
 </tr>
 <tr>
  <td rowspan=4 valign=top>
2329793
  </td>
  <td valign=top>
  <p><b>Description:</b> Modifying a shared buffer during
  traffic might create undefined behavior and in rare cases leads to
  packets stuck in the ASIC that require an ASIC reset to recover.</p>
  </td>
 </tr>
 <tr>
  <td valign=top>
  <p><b>Workaround:</b> Stop traffic before configuring shared headroom.</p>
  </td>
 </tr>
 <tr>
  <td valign=top>
  <p><b>Keywords:</b> Shared Headroom</p>
  </td>
 </tr>
 <tr>
  <td valign=top>
  <p><b>Discovered in Version:</b> SONiC
  201911_MUR6</p>
  </td>
 </tr>
 <tr>
  <td rowspan=4 valign=top>
  <p>2329924</p>
  </td>
  <td valign=top>
  <p><b>Description:</b> When connecting a SN4700 switch to a Cisco 3432C using 400GbE, the link does not rise in the corner port when using auto-negotiation.</p>
  </td>
 </tr>
 <tr>
  <td valign=top>
  <p><b>Workaround:</b> N/A</p>
  </td>
 </tr>
 <tr>
  <td valign=top>
  <p><b>Keywords:</b> SN4700, Link, 400GbE</p>
  </td>
 </tr>
 <tr>
  <td valign=top>
  <p><b>Discovered in Version:</b> SONiC
  201911_MUR6</p>
  </td>
 </tr>
 <tr>
  <td rowspan=4 valign=top>
  <p>2360012</p>
  </td>
  <td valign=top>
  <p><b>Description:</b> Warm reboot fails if PFCWD is enabled on the port when its operational/admin status is down.</p>
  </td>
 </tr>
 <tr>
  <td valign=top>
  <p><b>Workaround:</b> Do not enable PFCWD on ports when their operational/admin status is down.</p>
  </td>
 </tr>
 <tr>
  <td valign=top>
  <p><b>Keywords:</b> Warm-reboot, PFCWD</p>
  </td>
 </tr>
 <tr>
  <td valign=top>
  <p><b>Discovered in Version:</b> SONiC
  201911_MUR5</p>
  </td>
 </tr>
 <tr>
  <td rowspan=4 valign=top>2257265
  </td>
  <td valign=top>
  <p><b>Description:</b> On an SN4600 switch, the odd ports are not activated while using split-4 mode.</p>
  </td>
 </tr>
 <tr>
  <td valign=top>
  <p><b>Workaround:</b> N/A</p>
  </td>
 </tr>
 <tr>
  <td valign=top>
  <p><b>Keywords:</b> Spectrum-3, SN4600, Split, Ports</p>
  </td>
 </tr>
 <tr>
  <td valign=top>
  <p><b>Discovered in Version:</b> SONiC
  201911_MUR5</p>
  </td>
 </tr>
 <tr>
  <td rowspan=4 valign=top>
  <p>2245426</p>
  </td>
  <td valign=top>
  <p><b>Description: </b>On an SN4600 switch, the link does not rise when using LUX42604CO module at 40GbE after toggle.</p>
  </td>
 </tr>
 <tr>
  <td valign=top>
  <p><b>Workaround:</b> N/A</p>
  </td>
 </tr>
 <tr>
  <td valign=top>
  <p><b>Keywords:</b> Spectrum-3, SN4600C, Cables</p>
  </td>
 </tr>
 <tr>
  <td valign=top>
  <p><b>Discovered in Version:</b> SONiC
  201911_MUR5</p>
  </td>
 </tr>
 <tr>
  <td rowspan=4 valign=top>
  <p>2245816</p>
  </td>
  <td valign=top>
  <p><b>Description:</b> Splitting with optical cables may not work on an SN4600 switch.</p>
  </td>
 </tr>
 <tr>
  <td valign=top>
  <p><b>Workaround:</b> N/A</p>
  </td>
 </tr>
 <tr>
  <td valign=top>
  <p><b>Keywords:</b> Spectrum-3, SN4600, Cables, Ports</p>
  </td>
 </tr>
 <tr>
  <td valign=top>
  <p><b>Discovered in Version:</b> SONiC
  201911_MUR5</p>
  </td>
 </tr>
 <tr>
  <td rowspan=4 valign=top>
  <p>2310453</p>
  </td>
  <td valign=top>
  <p><b>Description:</b> The BGP running configuration is not reflected in the <code>frr.conf</code> file.</p>
  <p><b>Note:</b> As the BGP configuration is not present in the techsupport file, you must submit it separately.</p>
  </td>
 </tr>
 <tr>
  <td valign=top>
  <p><b>Workaround:</b> Use the <code>show running bgp</code> or the <code>vtysh
  -c "show run"</code> commands to see the BGP running configuration. </p>
  </td>
 </tr>
 <tr>
  <td valign=top>
  <p><b>Keywords:</b> BGP, frr.conf file</p>
  </td>
 </tr>
 <tr>
  <td valign=top>
  <p><b>Discovered in Version:</b> SONiC
  201911_MUR4</p>
  </td>
 </tr>
 <tr>
  <td rowspan=4 valign=top>2036710
  </td>
  <td valign=top>
  <p><b>Description:</b> A wrong MTU size is displayed in
  ICMP (type 3, code 4) when fragmentation is needed only for the VLAN
  interface.</p>
  </td>
 </tr>
 <tr>
  <td valign=top>
  <p><b>Workaround:</b> N/A</p>
  </td>
 </tr>
 <tr>
  <td valign=top>
  <p><b>Keywords:</b> MTU, VLAN, ICMP</p>
  </td>
 </tr>
 <tr>
  <td valign=top>
  <p><b>Discovered in Version:</b> SONiC
  201911_MUR4</p>
  </td>
 </tr>
 <tr>
  <td rowspan=4 valign=top>
  <p>-</p>
  </td>
  <td valign=top>
  <p><b>Description:</b> 10G BaseT modules are not supported
  on the SN3800 switch.</p>
  </td>
 </tr>
 <tr>
  <td valign=top>
  <p><b>Workaround: </b>N/A</p>
  </td>
 </tr>
 <tr>
  <td valign=top>
  <p><b>Keywords:</b> SN3800, 10G BaseT modules</p>
  </td>
 </tr>
 <tr>
  <td valign=top>
  <p><b>Discovered in Version: </b>SONiC 201911_MUR3</p>
  </td>
 </tr>
 <tr>
  <td rowspan=4 valign=top>
  <p>2053350</p>
  </td>
  <td valign=top>
  <p><b>Description:</b> In SN3800 system, when the link goes down on the partner side, the link down counter increases by 2.</p>
  </td>
 </tr>
 <tr>
  <td valign=top>
  <p><b>Workaround: </b>N/A</p>
  </td>
 </tr>
 <tr>
  <td valign=top>
  <p><b>Keywords:</b> SN3800, Link</p>
  </td>
 </tr>
 <tr>
  <td valign=top>
  <p><b>Discovered in Version: </b>SONiC 201911_MUR3</p>
  </td>
 </tr>
 <tr>
  <td rowspan=4 valign=top>
  <p>2180871/2148429</p>
  </td>
  <td valign=top>
  <p><b>Description:</b> Symbol counter may show the wrong
  indication.</p>
  </td>
 </tr>
 <tr>
  <td valign=top>
  <p><b>Workaround: </b>N/A</p>
  </td>
 </tr>
 <tr>
  <td valign=top>
  <p><b>Keywords:</b> SN3800, Counters </p>
  </td>
 </tr>
 <tr>
  <td valign=top>
  <p><b>Discovered in Version: </b>SONiC 201911_MUR3</p>
  </td>
 </tr>
 <tr>
  <td rowspan=4 valign=top>
  <p>2231118</p>
  </td>
  <td valign=top>
  <p><b>Description:</b> On rare occasions, when connecting a DR4 to NVIDIA Spectrum-3 systems on both sides, toggling on both sides may cause the link to not rise.</p>
  </td>
 </tr>
 <tr>
  <td valign=top>
  <p><b>Workaround: </b>N/A</p>
  </td>
 </tr>
 <tr>
  <td valign=top>
  <p><b>Keywords:</b> Port Toggle</p>
  </td>
 </tr>
 <tr>
  <td valign=top>
  <p><b>Discovered in Version: </b>SONiC 201911_MUR3</p>
  </td>
 </tr>
 <tr>
  <td rowspan=4 valign=top>
  <p>2162540</p>
  </td>
  <td valign=top>
  <p><b>Description:</b> MPLS is not supported for ISSU. Therefore, an MPLS configuration does not hold 0 hit traffic during ISSU.</p>
  </td>
 </tr>
 <tr>
  <td valign=top>
  <p><b>Workaround: </b>N/A</p>
  </td>
 </tr>
 <tr>
  <td valign=top>
  <p><b>Keywords:</b> ISSU</p>
  </td>
 </tr>
 <tr>
  <td valign=top>
  <p><b>Discovered in Version: </b>SONiC 201911_MUR3</p>
  </td>
 </tr>
 <tr>
  <td rowspan=4 valign=top>
  <p>1835086</p>
  </td>
  <td valign=top>
  <p><b>Description:</b> During the re-configuration phase of the ISSU, a port's admin state cannot be changed to DOWN until <code>sx_api_issu_end_set()</code> is called.</p>
  </td>
 </tr>
 <tr>
  <td valign=top>
  <p><b>Workaround: </b>N/A</p>
  </td>
 </tr>
 <tr>
  <td valign=top>
  <p><b>Keywords:</b> ISSU</p>
  </td>
 </tr>
 <tr>
  <td valign=top>
  <p><b>Discovered in Version: </b>SONiC 201911_MUR3</p>
  </td>
 </tr>
 <tr>
  <td rowspan=4 valign=top>
  <p>2190769</p>
  </td>
  <td valign=top>
  <p><b>Description:</b> Incoming ARP and NDP requests
  trigger the RIF RX_ERR counter.</p>
  </td>
 </tr>
 <tr>
  <td valign=top>
  <p><b>Workaround: </b>N/A</p>
  </td>
 </tr>
 <tr>
  <td valign=top>
  <p><b>Keywords:</b> ARP</p>
  </td>
 </tr>
 <tr>
  <td valign=top>
  <p><b>Discovered in Version: </b>SONiC 201911_MUR3</p>
  </td>
 </tr>
 <tr>
  <td rowspan=4 valign=top>
  <p>2200131</p>
  </td>
  <td valign=top>
  <p><b>Description: </b>When resetting the SFP, the following
  error message is printed out to the error log.</p>
  <p><i>" Receive PMPE error event on module 0: status 3 error type
  0".</i></p>
  <p>This can be safely ignored as it does not impact functionality; SFP reset still works as usual.</p>
  </td>
 </tr>
 <tr>
  <td valign=top>
  <p><b>Workaround: </b>N/A</p>
  </td>
 </tr>
 <tr>
  <td valign=top>
  <p><b>Keywords:</b> SFP</p>
  </td>
 </tr>
 <tr>
  <td valign=top>
  <p><b>Discovered in Version: </b>SONiC 201911_MUR2</p>
  </td>
 </tr>
 <tr>
  <td rowspan=4 valign=top>
  
  </td>
  <td valign=top>
  <p><b>Description:</b> SAI does not support disabling auto-negotiation in SONiC.</p>
  </td>
 </tr>
 <tr>
  <td valign=top>
  <p><b>Workaround: </b>N/A</p>
  </td>
 </tr>
 <tr>
  <td valign=top>
  <p><b>Keywords:</b> Auto-Negotiation</p>
  </td>
 </tr>
 <tr>
  <td valign=top>
  <p><b>Discovered in Version: </b>SONiC 201911_MUR1</p>
  </td>
 </tr>
 <tr>
  <td rowspan=4 valign=top>
  <p>2102645</p>
  </td>
  <td valign=top>
  <p><b>Description:</b> Adding a tagged VLAN on a port while an
  FDB learning process is running on the same port may result in a failure to
  read the FDB entry when running the <code>show mac</code> command.</p>
  </td>
 </tr>
 <tr>
  <td valign=top>
  <p><b>Workaround: </b>N/A</p>
  </td>
 </tr>
 <tr>
  <td valign=top>
  <p><b>Keywords:</b> FDB</p>
  </td>
 </tr>
 <tr>
  <td valign=top>
  <p><b>Discovered in Version: </b>SONiC 201911_MUR1</p>
  </td>
 </tr>
 <tr>
  <td rowspan=4 valign=top>
  <p>2078420</p>
  </td>
  <td valign=top>
  <p><b>Description:</b> The <code>show mac</code> command fails if it is run while the MACs are being flushed from the FDB.</p>
  </td>
 </tr>
 <tr>
  <td valign=top>
  <p><b>Workaround: </b>N/A</p>
  </td>
 </tr>
 <tr>
  <td valign=top>
  <p><b>Keywords:</b> FDB</p>
  </td>
 </tr>
 <tr>
  <td valign=top>
  <p><b>Discovered in Version: </b>SONiC 201911_MUR1</p>
  </td>
 </tr>
 <tr>
  <td rowspan=4 valign=top>
  <p>2074787</p>
  </td>
  <td valign=top>
  <p><b>Description:</b> The <code>show mac</code> command fails to show any learned MAC if a VLAN member is added when in tagged mode.</p>
  </td>
 </tr>
 <tr>
  <td valign=top>
  <p><b>Workaround: </b>N/A</p>
  </td>
 </tr>
 <tr>
  <td valign=top>
  <p><b>Keywords:</b> FDB</p>
  </td>
 </tr>
 <tr>
  <td valign=top>
  <p><b>Discovered in Version: </b>SONiC 201911_MUR1</p>
  </td>
 </tr>
 <tr>
  <td rowspan=4 valign=top>
  
  </td>
  <td valign=top>
  <p><b>Description:</b> Port split to 8 is not supported on NVIDIA Spectrum-2 and NVIDIA Spectrum-3 switches.</p>
  </td>
 </tr>
 <tr>
  <td valign=top>
  <p><b>Workaround: </b>N/A</p>
  </td>
 </tr>
 <tr>
  <td valign=top>
  <p><b>Keywords:</b> port-split</p>
  </td>
 </tr>
 <tr>
  <td valign=top>
  <p><b>Discovered in Version: </b>SONiC 201911_MUR1</p>
  </td>
 </tr>
 <tr>
  <td rowspan=4 valign=top>
  
  </td>
  <td valign=top>
  <p><b>Description:</b> Fast reboot is not supported on NVIDIA Spectrum-2 switches.</p>
  </td>
 </tr>
 <tr>
  <td valign=top>
  <p><b>Workaround: </b>N/A</p>
  </td>
 </tr>
 <tr>
  <td valign=top>
  <p><b>Keywords:</b> fast-reboot</p>
  </td>
 </tr>
 <tr>
  <td valign=top>
  <p><b>Discovered in Version: </b>SONiC 201911_MUR1</p>
  </td>
 </tr>
 <tr>
  <td rowspan=4 valign=top>
  
  </td>
  <td valign=top>
  <p><b>Description:</b> The MTU of a network device created by the SDK and the MTU of the switch port are not synchronized.</p>
  </td>
 </tr>
 <tr>
  <td valign=top>
  <p><b>Workaround:</b> Configure the network device MTU to be 4
  bytes smaller than the port MTU.</p>
  </td>
 </tr>
 <tr>
  <td valign=top>
  <p><b>Keywords:</b> MTU</p>
  </td>
 </tr>
 <tr>
  <td valign=top>
  <p><b>Discovered in Version: </b>SONiC 201911_MUR1</p>
  </td>
 </tr>
 <tr>
  <td rowspan=4 valign=top>
  <p>2239785</p>
  </td>
  <td valign=top>
  <p><b>Description:</b> <code>ethtool</code> does not support parsed QSFP-DD cable EEPROM content.</p>
  </td>
 </tr>
 <tr>
  <td valign=top>
  <p><b>Workaround: </b>Run <code>show interface transceiver eeprom &lt;interface-name&gt;</code>
  to see the right content.</p>
  </td>
 </tr>
 <tr>
  <td valign=top>
  <p><b>Keywords:</b> ethtool</p>
  </td>
 </tr>
 <tr>
  <td valign=top>
  <p><b>Discovered in Version: </b>SONiC 201911</p>
  </td>
 </tr>
 <tr>
  <td rowspan=4 valign=top>
  <p>2239867</p>
  </td>
  <td valign=top>
  <p><b>Description:</b> 400GbE cables (CMIS) and transceiver EEPROMs are missing page support.</p>
  </td>
 </tr>
 <tr>
  <td valign=top>
  <p><b>Workaround: </b>N/A</p>
  </td>
 </tr>
 <tr>
  <td valign=top>
  <p><b>Keywords:</b> Cables</p>
  </td>
 </tr>
 <tr>
  <td valign=top>
  <p><b>Discovered in Version: </b>SONiC 201911</p>
  </td>
 </tr>
 <tr>
  <td rowspan=4 valign=top>
  <p>2116493</p>
  </td>
  <td valign=top>
  <p><b>Description: </b>The <code>pfcwd show stats</code> command returns wrong (zeroid) counters when a lossless priority is moved to an operational state after being in stormed state.</p>
  </td>
 </tr>
 <tr>
  <td valign=top>
  <p><b>Workaround: </b>N/A</p>
  </td>
 </tr>
 <tr>
  <td valign=top>
  <p><b>Keywords:</b> PFCWD</p>
  </td>
 </tr>
 <tr>
  <td valign=top>
  <p><b>Discovered in Version: </b>SONiC 201911</p>
  </td>
 </tr>
 <tr>
  <td rowspan=4 valign=top>
</td>
  <td valign=top>
  <p><b>Description: </b>Port ether stats/in/out packets 4K-9K
  counters count only packets 4K-8K.</p>
  </td>
 </tr>
 <tr>
  <td valign=top>
  <p><b>Workaround: </b>N/A</p>
  </td>
 </tr>
 <tr>
  <td valign=top>
  <p><b>Keywords:</b> Port counters</p>
  </td>
 </tr>
 <tr>
  <td valign=top>
  <p><b>Discovered in Version: </b>SONiC 201911</p>
  </td>
 </tr>
 <tr>
  <td rowspan=4 valign=top>
</td>
  <td valign=top>
  <p><b>Description: </b>ACL table can only be a member of a
  single sequential ACL group.</p>
  </td>
 </tr>
 <tr>
  <td valign=top>
  <p><b>Workaround:</b> Create a table per sequential group.</p>
  </td>
 </tr>
 <tr>
  <td valign=top>
  <p><b>Keywords: </b>ACL</p>
  </td>
 </tr>
 <tr>
  <td valign=top>
  <p><b>Discovered in Version: </b>SONiC 201911</p>
  </td>
 </tr>
 <tr>
  <td rowspan=4 valign=top>
</td>
  <td valign=top>
  <p><b>Description: </b>When using <code>SAI_ACL_IP_TYPE_ANY</code>, it is necessary
  to set at least one other field, as internally no key is used to match ANY
  value, and at least one key should be set for every rule.</p>
  </td>
 </tr>
 <tr>
  <td valign=top>
  <p><b>Workaround:</b> Use the additional field in the rule.</p>
  </td>
 </tr>
 <tr>
  <td valign=top>
  <p><b>Keywords: </b>ACL</p>
  </td>
 </tr>
 <tr>
  <td valign=top>
  <p><b>Discovered in Version: </b>SONiC 201911</p>
  </td>
 </tr>
 <tr>
  <td rowspan=4 valign=top>
 </td>
  <td valign=top>
  <p><b>Description:</b> <code>ACL SAI_ACL_ENTRY_ATTR_ACTION_MIRROR_INGRESS</code> is not supported at egress stage.</p>
  <p><b>Note:</b> An exception exists for <code>SAI_ACL_BIND_POINT_TYPE_ROUTER_INTERFACE</code> at egress stage, when only <code>SAI_ACL_ENTRY_ATTR_ACTION_MIRROR_INGRESS</code> can be used.</p>
  </td>
 </tr>
 <tr>
  <td valign=top>
  <p><b>Workaround: </b>N/A</p>
  </td>
 </tr>
 <tr>
  <td valign=top>
  <p><b>Keywords: </b>ACL, Mirroring/SPAN</p>
  </td>
 </tr>
 <tr>
  <td valign=top>
  <p><b>Discovered in Version: </b>SONiC 201911</p>
  </td>
 </tr>
 <tr>
  <td rowspan=4 valign=top>
  </td>
  <td valign=top>
  <p><b>Description:</b> In the current DSCP mode, the DSCP value
  and the ECN mode are shared between the same type of tunnels.</p>
  <p>By changing the DSCP mode, the DSCP value
  and the ECN mode will affect all the tunnels of the same type. Tunnels are
  considered ‘the same type’ if both the following conditions are met:</p>
  <ul>
  <li><code>SAI_TUNNEL_ATTR_TYPE</code> has the same value</li>
  <li>Tunnel direction has the same value. Direction has 3 types: encap, decap and symmetry.
  <ul>
  <li><b>Encap:</b> No decap attributes (which start with <code>SAI_TUNNEL_ATTR_ENCAP_</code>) are configured during tunnel creation.</li>
  <li><b>Decap:</b> No encap attributes (which start with <code>SAI_TUNNEL_ATTR_DECAP_</code>) are configured during tunnel creation.</li>
  <li><b>Symmetry:</b> Both encap and decap attributes are configured during tunnel creation.</li>
  </ul>
   </li>
   </ul>
  </td>
 </tr>
 <tr>
  <td valign=top>
  <p><b>Workaround: </b>Use the same values for all tunnels of same type.</p>
  </td>
 </tr>
  <tr>
  <td valign=top>
  <p><b>Keywords: </b>Tunnels</p>
  </td>
 </tr>
 <tr>
  <td valign=top>
  <p><b>Discovered in Version: </b>SONiC 201911</p>
  </td>
 </tr>
 <tr>
  <td rowspan=4 valign=top>
</td>
  <td valign=top>
  <p><b>Description: </b>In case the WRED profile
  has WRED and ECN mark enabled for at least one color, the enabled colors for
  WRED and ECN must be the same. For example, you cannot have <code>SAI_WRED_ATTR_GREEN_ENABLE=true</code> and <code>SAI_WRED_ATTR_ECN_MARK_MODE=SAI_ECN_MARK_MODE_YELLOW</code>.</p>
  </td>
 </tr>
 <tr>
  <td valign=top>
  <p><b>Workaround:</b> Use the same enabled colors for WRED and ECN.</p>
  </td>
 </tr>
 <tr>
  <td valign=top>
  <p><b>Keywords: </b>WRED, ECN, QoS<b> </b></p>
  </td>
 </tr>
 <tr>
  <td valign=top>
  <p><b>Discovered in Version: </b>SONiC 201911</p>
  </td>
 </tr>
 <tr>
  <td rowspan=4 valign=top>
 </td>
  <td valign=top>
  <p><b>Description: </b>Clear queue stats for specific counters
  always clears all available counters.</p>
  </td>
 </tr>
 <tr>
  <td valign=top>
  <p><b>Workaround: </b>N/A</p>
  </td>
 </tr>
 <tr>
  <td valign=top>
  <p><b>Keywords: </b>Queues, Buffers</p>
  </td>
 </tr>
 <tr>
  <td valign=top>
  <p><b>Discovered in Version: </b>SONiC 201911</p>
  </td>
 </tr>
 <tr>
  <td rowspan=4 valign=top>
   </td>
  <td valign=top>
  <p><b>Description:</b> Mirror session cannot be edited if the maximum supported mirror sessions was already configured.</p>
  <p>The maximum supported mirror sessions for NVIDIA Spectrum ASICs is 3.</p>
<p>The maximum supported mirror sessions for NVIDIA Spectrum-2 and Spectrum-3 ASICs is 8.</p>
  </td>
 </tr>
 <tr>
  <td valign=top>
  <p><b>Workaround:</b> Remove the session and recreate it with the required new values.</p>
  </td>
 </tr>
 <tr>
  <td valign=top>
  <p><b>Keywords: </b>Mirroring (or SPAN)</p>
  </td>
 </tr>
 <tr>
  <td valign=top>
  <p><b>Discovered in Version: </b>SONiC 201911</p>
  </td>
 </tr>
 <tr>
  <td rowspan=4 valign=top>
 </td>
  <td valign=top>
  <p><b>Description: </b>Switch Prio (SAI TC) &lt;-&gt; IEEE PFC is a global property. Thus, when setting different PFC-&gt;PG on different ports, the last value set overrides the rest.</p>
  </td>
 </tr>
 <tr>
  <td valign=top>
  <p><b>Workaround: </b>Set the same map on all the ports</p>
  </td>
 </tr>
 <tr>
  <td valign=top>
  <p><b>Keywords: </b>QoS maps</p>
  </td>
 </tr>
 <tr>
  <td valign=top>
  <p><b>Discovered in Version: </b>SONiC 201911</p>
  </td>
 </tr>
 <tr>
  <td rowspan=4 valign=top>
  </td>
  <td valign=top>
  <p><b>Description: </b>Debug counters do not work correctly with
  WJH, and vice-versa, as the configurationss for the two features conflict.</p>
  </td>
 </tr>
 <tr>
  <td valign=top>
  <p><b>Workaround:</b></p>
  <ul>
  <li>Delete all debug counters before using WJH</li>
  <li>Stop WJH before creating debug counters</li>
  </ul>
  </td>
 </tr>
 <tr>
  <td valign=top>
  <p><b>Keywords: </b>Debug counters, WJH</p>
  </td>
 </tr>
 <tr>
  <td valign=top>
  <p><b>Discovered in Version: </b>SONiC 201911</p>
  </td>
 </tr>
 <tr>
  <td rowspan=4 valign=top>
</td>
  <td valign=top>
  <p><b>Description:</b> A specific drop reason can only exist in
  a single debug counter.</p>
  </td>
 </tr>
 <tr>
  <td valign=top>
  <p><b>Workaround: </b>N/A</p>
  </td>
 </tr>
 <tr>
  <td valign=top>
  <p><b>Keywords: </b>Debug counters</p>
  </td>
 </tr>
 <tr>
  <td valign=top>
  <p><b>Discovered in Version: </b>SONiC 201911</p>
  </td>
 </tr>
 <tr>
  <td rowspan=4 valign=top>
  <p>2137421</p>
  </td>
  <td valign=top>
  <p><b>Description: </b>On an SN3800 switch, when working in split mode, you cannot configure the first port to 50GbE while configuring the second port to either 25GbE or 10GbE.</p>
  </td>
 </tr>
 <tr>
  <td valign=top>
  <p><b>Workaround: </b>N/A</p>
  </td>
 </tr>
 <tr>
  <td valign=top>
  <p><b>Keywords:</b> SN3800</p>
  </td>
 </tr>
 <tr>
  <td valign=top>
  <p><b>Discovered in Version: </b>SONiC 201911</p>
  </td>
 </tr>
 <tr>
  <td rowspan=4 valign=top>
  <p>1973766</p>
  </td>
  <td valign=top>
  <p><b>Description: </b>Splitting a port into 4 breakouts is not supported on SN3800 switches.</p>
  </td>
 </tr>
 <tr>
  <td valign=top>
  <p><b>Workaround: </b>N/A</p>
  </td>
 </tr>
 <tr>
  <td valign=top>
  <p><b>Keywords:</b> SN3800, split port</p>
  </td>
 </tr>
 <tr>
  <td valign=top>
  <p><b>Discovered in Version: </b>SONiC 201911</p>
  </td>
 </tr>
 <tr>
  <td rowspan=4 valign=top>
  </td>
  <td valign=top>
  <p><b>Description: </b>On very rare occasions on SN3800 switches, traffic may get dropped due to high BER in the link.</p>
  </td>
 </tr>
 <tr>
  <td valign=top>
  <p><b>Workaround: </b>N/A</p>
  </td>
 </tr>
 <tr>
  <td valign=top>
  <p><b>Keywords: </b>SN3800, Cables, Speeds, BER</p>
  </td>
 </tr>
 <tr>
  <td valign=top>
  <p><b>Discovered in Version: </b>SONiC 201911</p>
  </td>
 </tr>
 <tr>
  <td rowspan=4 valign=top>
</td>
  <td valign=top>
  <p><b>Description:</b> 1GbE is currently not implemented on SN3800 switches.</p>
  </td>
 </tr>
 <tr>
  <td valign=top>
  <p><b>Workaround: </b>N/A</p>
  </td>
 </tr>
 <tr>
  <td valign=top>
  <p><b>Keywords:</b> SN3800</p>
  </td>
 </tr>
 <tr>
  <td valign=top>
  <p><b>Discovered in Version: </b>SONiC 201911</p>
  </td>
 </tr>
 <tr>
  <td rowspan=4 valign=top>
  <p>2061691</p>
   </td>
  <td valign=top>
  <p><b>Description: </b>You cannot use VLAN1 as it is reserved for SONiC internal purposes only. The usable VLAN ID for users starts at <em>VLAN2</em>.</p>
  </td>
 </tr>
 <tr>
  <td valign=top>
  <p><b>Workaround: </b>N/A</p>
  </td>
 </tr>
 <tr>
  <td valign=top>
  <p><b>Keywords:</b> VLAN</p>
  </td>
 </tr>
 <tr>
  <td valign=top>
  <p><b>Discovered in Version: </b>SONiC 201911</p>
  </td>
 </tr>
 <tr>
  <td rowspan=4 valign=top>
  <p>1940359</td>
  <td valign=top>
  <p><b>Description:</b> On MSN2010 switches, if a system reboot is triggered using the <code>sudo reboot</code> command, the following wrong reboot cause is displayed: <em>Hardware - Other (Reset caused
  by hotswap or halt)</em> instead of "reset_sw_reset”.</p>
  </td>
 </tr>
 <tr>
  <td valign=top>
  <p><b>Workaround: </b>N/A</p>
  </td>
 </tr>
 <tr>
  <td valign=top>
  <p><b>Keywords:</b> System reboot, MSN2010</p>
  </td>
 </tr>
 <tr>
  <td valign=top>
  <p><b>Discovered in Version: </b>SONiC 201911</p>
  </td>
 </tr>
 <tr>
  <td rowspan=4 valign=top>
  <p>2054684</p>
 </td>
  <td valign=top>
  <p><b>Description: </b>The IPv6 layer 3 ACL table is not supported on
  NVIDIA Spectrum-based switches.</p>
  </td>
 </tr>
 <tr>
  <td valign=top>
  <p><b>Workaround: </b>N/A</p>
  </td>
 </tr>
 <tr>
  <td valign=top>
  <p><b>Keywords:</b> IPv6 L3 ACL table</p>
  </td>
 </tr>
 <tr>
  <td valign=top>
  <p><b>Discovered in Version: </b>SONiC 201911</p>
  </td>
 </tr>
 <tr>
  <td rowspan=4 valign=top>  
  </td>
  <td valign=top>
  <p><b>Description:</b> When ISSU is enabled for a SKU, hardware
  resources are reduced to half (routes, neighbors, ACLs).</p>
  <p>To check if ISSU is enabled for a specific SKU, run:</p>
  <pre>admin@sonic:~$ show platform mlnx issu
  ISSU is enabled
  admin@arc-switch1004:~$</pre>
  </td>
 </tr>
 <tr>
  <td valign=top>
  <p><b>Workaround: </b>N/A</p>
  </td>
 </tr>
 <tr>
  <td valign=top>
  <p><b>Keywords:</b> ISSU</p>
  </td>
 </tr>
 <tr>
  <td valign=top>
  <p><b>Discovered in Version:</b> SONiC 201811</p>
  </td>
 </tr>
 <tr>
  <td rowspan=4 valign=top>
  </td>
  <td valign=top>
  <p>Description:</b> The command <code>show interface counters</code> shows RX_BPS, RX_UTIL, TX_BPS, TX_UTIL as <em>N/A</em> until you run <code>sonic-clear counters</code>. The reason is a limitation in counter implementation by
  a vendor.</p>
  </td>
 </tr>
 <tr>
  <td valign=top>
  <p><b>Workaround:</b> Run <code>sonic-clear counters</code> after every switch reboot/init. The pps/bps rates and port utilization should be available then.</p>
  </td>
 </tr>
 <tr>
  <td valign=top>
  <p><b>Keywords:</b> Counters</p>
  </td>
 </tr>
 <tr>
  <td valign=top>
  <p><b>Discovered in Version: </b>SONiC 201811</p>
  </td>
 </tr>
 <tr>
  <td rowspan=4 valign=top>
  </td>
  <td valign=top>
  <p><b>Description:</b> ARP refreshing only functions on a VLAN interface.</p>
  </td>
 </tr>
 <tr>
  <td valign=top>
  <p><b>Workaround: </b>N/A</p>
  </td>
 </tr>
 <tr>
  <td valign=top>
  <p><b>Keywords:</b> ARP</p>
  </td>
 </tr>
 <tr>
  <td valign=top>
  <p><b>Discovered in Version: </b>SONiC 201811</p>
  </td>
 </tr>
 <tr>
  <td rowspan=4 valign=top>
  </td>
  <td valign=top>
  <p><b>Description:</b> Warm reboot and fast reboot are not
  supported on SN2010 switches.</p>
  </td>
 </tr>
 <tr>
  <td valign=top>
  <p><b>Workaround: </b>N/A</p>
  </td>
 </tr>
 <tr>
  <td valign=top>
  <p><b>Keywords: </b>Warm reboot, fast reboot</p>
  </td>
 </tr>
 <tr>
  <td valign=top>
  <p><b>Discovered in Version: </b>SONiC 201811</p>
  </td>
 </tr>
 <tr>
  <td rowspan=4 valign=top>
  <p>1945337</p>
  </td>
  <td valign=top>
  <p><b>Description: </b>PFCWD does not detect PFC storm for lossy
  priority on a port that has ASYM-PFC is enabled.</p>
  </td>
 </tr>
 <tr>
  <td valign=top>
  <p><b>Workaround: </b>N/A</p>
  </td>
 </tr>
 <tr>
  <td valign=top>
  <p><b>Keywords: </b>PFCWD</p>
  </td>
 </tr>
 <tr>
  <td valign=top>
  <p><b>Discovered in Version: </b>SONiC 201811</p>
  </td>
 </tr>
 <tr>
  <td rowspan=4 valign=top>
  </td>
  <td valign=top>
  <p><b>Description: </b>Bit Error Rate monitoring (BER) is not supported on 10GbaseT modules.</p>
  </td>
 </tr>
 <tr>
  <td valign=top>
  <p><b>Workaround: </b>N/A</p>
  </td>
 </tr>
 <tr>
  <td valign=top>
  <p><b>Keywords: </b>BER, 10GbaseT modules</p>
  </td>
 </tr>
 <tr>
  <td valign=top>
  <p><b>Discovered in Version: </b>SONiC 201811</p>
  </td>
 </tr>
 <tr>
  <td rowspan=4 valign=top>
  </td>
  <td valign=top>
  <p><b>Description: </b>Rx LOS is not supported when both sides
  of the link are of type BaseT.</p>
  </td>
 </tr>
 <tr>
  <td valign=top>
  <p><b>Workaround: </b>N/A</p>
  </td>
 </tr>
 <tr>
  <td valign=top>
  <p><b>Keywords: </b>Rx LOS, BaseT modules</p>
  </td>
 </tr>
 <tr>
  <td valign=top>
  <p><b>Discovered in Version: </b>SONiC 201811</p>
  </td>
 </tr>
 <tr>
  <td rowspan=4 valign=top>
  </td>
  <td valign=top>
  <p><b>Description: </b>When configuring shared buffers, the
  software does not verify that Xon &lt; Xoff &lt; buffer size.</p>
  </td>
 </tr>
 <tr>
  <td valign=top>
  <p><b>Workaround: </b>Make sure to meet these
  requirements during configuration.</p>
  </td>
 </tr>
 <tr>
  <td valign=top>
  <p><b>Keywords: </b>Shared Buffers</p>
  </td>
 </tr>
 <tr>
  <td valign=top>
  <p><b>Discovered in Version: </b>SONiC 201811</p>
  </td>
 </tr>
 <tr>
  <td rowspan=4 valign=top>
  </td>
  <td valign=top>
  <p><b>Description: </b>The minimum reserved buffer space for
  egress traffic is 1.</p>
  </td>
 </tr>
 <tr>
  <td valign=top>
  <p><b>Workaround: </b>N/A</p>
  </td>
 </tr>
 <tr>
  <td valign=top>
  <p><b>Keywords: </b>Shared Buffers</p>
  </td>
 </tr>
 <tr>
  <td valign=top>
  <p><b>Discovered in Version: </b>SONiC 201811</p>
  </td>
 </tr>
 <tr>
  <td rowspan=4 valign=top>
  </td>
  <td valign=top>
  <p><b>Description: </b>Mapping of switch priority 7 to a non-default
  Priority Group (PG) is not permitted and causes unexpected behavior.</p>
  </td>
 </tr>
 <tr>
  <td valign=top>
  <p><b>Workaround: </b>N/A</p>
  </td>
 </tr>
 <tr>
  <td valign=top>
  <p><b>Keywords: </b>Switch Priority, Priority Group (PG)</p>
  </td>
 </tr>
 <tr>
  <td valign=top>
  <p><b>Discovered in Version: </b>SONiC 201811</p>
  </td>
 </tr>
 <tr>
  <td rowspan=4 valign=top>
  
  </td>
  <td valign=top>
  <p><b>Description: </b>Toggling port speed from 1GbE to other
  speeds may block 1GbE traffic.</p>
  </td>
 </tr>
 <tr>
  <td valign=top>
  <p><b>Workaround: </b>N/A</p>
  </td>
 </tr>
 <tr>
  <td valign=top>
  <p><b>Keywords: </b>Port toggling</p>
  </td>
 </tr>
 <tr>
  <td valign=top>
  <p><b>Discovered in Version: </b>SONiC 201811</p>
  </td>
 </tr>
 <tr>
  <td rowspan=4 valign=top>
   </td>
  <td valign=top>
  <p><b>Description: </b>In some configuration cases, Priority
  Flow Control does not perform as expected.</p>
  <p>Only one of the following maps can have <em>none</em> as the default value:</p>
  <ul>
  <li><code>TC_TO_QUEUE_MAP</code></li>
  <li><code>MAP_PFC_PRIORITY_TO_QUEUE</code></li>
  <li><code>TC_TO_PRIORITY_GROUP_MAP</code></li>
  </ul>
  </td>
 </tr>
 <tr>
  <td valign=top>
  <p><b>Workaround:</b> A single instance of
  <code>TC_TO_PRIORITY_GROUP_MAP</code> should be applied on all interfaces.</p>
  </td>
 </tr>
 <tr>
  <td valign=top>
  <p><b>Keywords:</b> QoS mapping</p>
  </td>
 </tr>
 <tr>
  <td valign=top>
  <p><b>Discovered in Version: </b>SONiC 201811</p>
  </td>
 </tr>
 <tr>
  <td rowspan=4 valign=top>
  <p>849302</p>
  </td>
  <td valign=top>
  <p><b>Description: </b>Traffic is not divided up correctly under
  congestion if working with Strict priority.</p>
  </td>
 </tr>
 <tr>
  <td valign=top>
  <p><b>Workaround: </b>N/A</p>
  </td>
 </tr>
 <tr>
  <td valign=top>
  <p><b>Keywords: </b>Congestion, port priority</p>
  </td>
 </tr>
 <tr>
  <td valign=top>
  <p><b>Discovered in Version: </b>SONiC 201811</p>
  </td>
 </tr>
</table>
