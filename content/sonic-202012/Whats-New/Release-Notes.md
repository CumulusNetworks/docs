---
title: Release Notes
author: Cumulus Networks
weight: 20
product: SONiC
version: 202012
siteSlug: sonic
---

These are the release notes for SONiC software version 202012 on NVIDIA® Mellanox Spectrum®-based switches. However, these release notes are simply an upstream version of the pure SONiC release available on GitHub.

## Release Notes Update History

| Revision | Date | Description |
| -------- | ---- | ----------- |
| Rev 1.0 | May 1, 2021 | Initial release of these release notes. |

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
  <p><b>Keywords:</b>Spectrum-2, SN3800, Tx settings</p>
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
  <p><b>Keywords:</b>Driver, MTU</p>
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
  commands used to enable PFCWD do not work.<b></b></p>
  </td>
 </tr>
 <tr>
  <td>
  <p><strong>Keywords:</strong> PFCWD,
  CLI<b></b></p>
  </td>
 </tr>
 <tr>
  <td>
  <p><strong>Discovered in Version:</strong>
  SONiC 201911_MUR6<b></b></p>
  </td>
 </tr>
 <tr>
  <td>
  <p><strong>Fixed in Version: </strong>SONiC
  202012<b></b></p>
  </td>
 </tr>
 <tr>
  <td rowspan=4 valign=top >
  <p>2435816</p>
  </td>
  <td>
  <p><strong>Description:</strong> Interface
  PortChannel cannot get an assigned IP when 80 PortChannel RIF are defined.<b></b></p>
  </td>
 </tr>
 <tr>
  <td>
  <p><strong>Keywords:</strong> IP
  assignment, PortChannel, RIF<b></b></p>
  </td>
 </tr>
 <tr>
  <td>
  <p><strong>Discovered in Version:</strong>
  SONiC 201911_MUR6<b></b></p>
  </td>
 </tr>
 <tr>
  <td>
  <p><strong>Fixed in Version: </strong>SONiC
  202012<b></b></p>
  </td>
 </tr>
 <tr>
  <td rowspan=4 valign=top >
  <p>2447853</p>
  </td>
  <tdvalign=top>
  <p><b>Description:</b> What Just Happened consumes ~100&amp; CPU usage while not reading
  data.</p>
  </td>
 </tr>
 <tr>
  <tdvalign=top>
  <p><b>Keywords:</b> What-Just-Happened</p>
  </td>
 </tr>
 <tr>
  <tdvalign=top>
  <p><b>Discovered in Version: </b>SONiC 201911_MUR6</p>
  </td>
 </tr>
 <tr>
  <tdvalign=top>
  <p><b>Fixed in Version: </b>SONiC 202012</p>
  </td>
 </tr>
 <tr>
  <td rowspan=4 valign=top>
  <p>2367239</p>
  </td>
  <td valign=top>
  <p><b>Description:</b> snmpagent allocates (hardcoded)
  only 4 lanes for each transceiver. Therefore, the SNMP query returns the
  sensors of only the first 4 lanes of a QSFP-DD (400GbE) cable which has 8
  lanes. </p>
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
  <p><b>Description:</b> On occasion, when using Dell QSFP28
  copper cable in 40G (4x10G) split mode, the link goes down.</p>
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
  <p><b>Description:</b> The command 'config pfcwd start --action drop
  ports all detection-time 400 --restoration-time 400' fails due to invalid options: ports and detection-time</p>
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
  <p><b>Description:</b> When device is rebooted with locked
  Optical Transceivers in split mode, the firmware may get stuck.</p>
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
 <tr style='mso-yfti-irow:52'>
  <td rowspan=4 valign=top>
  <p>2355323</p>
  </td>
  <td valign=top>
  <p><b>Description:</b> When moving the port-status of two
  or more ingress ports up or down, congestion egress events will send events
  of threshold crossing without real reason, though the congestion histogram
  remains unaffected.</p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:53'>
  <td valign=top>
  <p><b>Keywords:</b> Telemetry</p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:54'>
  <td valign=top>
  <p><b>Discovered in Version:</b> SONiC
  201911_MUR6</p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:55'>
  <td valign=top>
  <p><b>Fixed in Version: </b>SONiC 202012</p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:56'>
  <td rowspan=4 valign=top>
  <p>2407915</p>
  </td>
  <td valign=top>
  <p><b>Description:</b> In Spectrum-3 while using Optic
  cable MFS1S50-H003E in Split 4x1 mode in PAM4, when one port is toggled, all
  other 3 ports go down.</p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:57'>
  <td valign=top>
  <p><b>Keywords:</b> Ethernet;Spectrum-3, PAM4, Optic
  Cables</p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:58'>
  <td valign=top>
  <p><b>Discovered in Version:</b> SONiC
  201911_MUR6</p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:59'>
  <td valign=top>
  <p><b>Fixed in Version: </b>SONiC 202012</p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:60'>
  <td rowspan=4 valign=top>
  <p>2405266</p>
  </td>
  <td valign=top>
  <p><b>Description:</b> On SN3800 systems, when the port is
  a member of a LAG, after a warmboot and port toggle on the peer-side, the
  port remains down. </p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:61'>
  <td valign=top>
  <p><b>Keywords:</b> Ethernet;Spectrum-3, DAC</p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:62'>
  <td valign=top>
  <p><b>Discovered in Version:</b> SONiC
  201911_MUR6</p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:63'>
  <td valign=top>
  <p><b>Fixed in Version: </b>SONiC 202012</p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:64'>
  <td rowspan=4 valign=top>
  <p>2176790</p>
  </td>
  <td valign=top>
  <p><b>Description:</b> On rare occasions packets loss may
  be experienced on SN3800 due to signal integrity issues.</p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:65'>
  <td valign=top>
  <p><b>Keywords:</b> Spectrum-2, SN3800, BER</p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:66'>
  <td valign=top>
  <p><b>Discovered in Version:</b> SONiC
  201911_MUR6</p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:67'>
  <td valign=top>
  <p><b>Fixed in Version: </b>SONiC 202012</p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:68'>
  <td rowspan=4 valign=top>
  <p>1883103</p>
  </td>
  <td valign=top>
  <p><b>Description:</b> When connecting SN3700 at 200GbE to
  Ixia K400, Ixia receives CRC errors.</p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:69'>
  <td valign=top>
  <p><b>Keywords:</b> Spectrum-2, SN3700, Ixia, CRC</p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:70'>
  <td valign=top>
  <p><b>Discovered in Version: </b>SONiC 201911_MUR6</p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:71'>
  <td valign=top>
  <p><b>Fixed in Version: </b>SONiC 202012</p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:72'>
  <td rowspan=4 valign=top>
  <p>2320854</p>
  </td>
  <td valign=top>
  <p><b>Description:</b> When working in 400GbE, deleting
  the headroom configuration (changing buffer size to zero) on the fly may cause
  continual packet drops.</p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:73'>
  <td valign=top>
  <p><b>Keywords:</b> Speed, 400GbE</p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:74'>
  <td valign=top>
  <p><b>Discovered in Version: </b>SONiC 201911_MUR6</p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:75'>
  <td valign=top>
  <p><b>Fixed in Version: </b>SONiC 202012</p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:76'>
  <td rowspan=4 valign=top>
  <p>2457801</p>
  </td>
  <td valign=top>
  <p><b>Description:</b> On Spectrum systems, 10GbE/1GbE
  Transceiver (FTLX8574D3BCV) stopped working after firmware upgrade. </p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:77'>
  <td valign=top>
  <p><b>Keywords:</b> Firmware Upgrade, Transceiver</p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:78'>
  <td valign=top>
  <p><b>Discovered in Version: </b>SONiC 201911_MUR6</p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:79'>
  <td valign=top>
  <p><b>Fixed in Version: </b>SONiC 202012</p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:80'>
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
 <tr style='mso-yfti-irow:81'>
  <td valign=top>
  <p><b>Keywords:</b> ISSU, Driver, Firmware Upgrade</p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:82'>
  <td valign=top>
  <p><b>Discovered in Version: </b>SONiC 201911_MUR6</p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:83'>
  <td valign=top>
  <p><b>Fixed in Version: </b>SONiC 202012</p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:84'>
  <td rowspan=4 valign=top>
  <p>2116499</p>
  </td>
  <td valign=top>
  <p><b>Description:</b> Everflow functionality does not work
  after warm reboot.</p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:85'>
  <td valign=top>
  <p><b>Keywords:</b> Everflow, warm reboot</p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:86'>
  <td valign=top>
  <p><b>Discovered in Version: </b>SONiC 201911</p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:87;mso-yfti-lastrow:yes'>
  <td valign=top>
  <p><b>Fixed in Version: </b>SONiC 202012</p>
  </td>
 </tr>
</table>

## Known Issues

For the community limitations, please refer to the {{<exlink url="https://github.com/Azure/sonic-buildimage/issues" text="Azure GitHub">}} site.

<table>
 <thead>
  <tr>
   <td valign=top>
   <p><b>RM #</b></p>
   </td>
   <td valign=top >
   <p align=center style='text-align:center;'><b>Issue</b></p>
   </td>
  </tr>
 <tr>
  <td rowspan=4 valign=top>
  <p>2446581</p>
  </td>
  <td>
  <p><strong>Description:</strong> An
  error is logged when a MAC address that already exists on the FDB is learned
  from a different port.<b></b></p>
  </td>
 </tr>
 <tr>
  <td>
  <p><strong>Workaround:</strong> N/A<b
 ></b></p>
  </td>
 </tr>
 <tr>
  <td>
  <p><strong>Keywords:</strong> MAC
  learning, FDB<b></b></p>
  </td>
 </tr>
 <tr>
  <td>
  <p><strong>Discovered in Version:</strong>
  SONiC 202012<b></b></p>
  </td>
 </tr>
 <tr>
  <td rowspan=4 valign=top>
  <p>2393635</p>
  </td>
  <td>
  <p><strong>Description:</strong> Warm-reboot
  fails in case of corrupted /host/warm-reboot/issu-bank.txt file and the
  switch is in an inconsistent state afterwards.<b></b></p>
  </td>
 </tr>
 <tr>
  <td>
  <p><strong>Workaround:</strong> Follow
  the instructions printed in <code>/var/log/syslog</code>, or run the CLI command <code>"warm-reboot
  -v"</code> and then perform a cold reboot.<b
 ></b></p>
  </td>
 </tr>
 <tr>
  <td>
  <p><strong>Keywords:</strong> ISSU<b
 ></b></p>
  </td>
 </tr>
 <tr>
  <td>
  <p><strong>Discovered in Version:</strong>
  SONiC 202012<b></b></p>
  </td>
 </tr>
 <tr>
  <td rowspan=4 valign=top>
  <p>2571738</p>
  </td>
  <td valign=top>
  <p><b>Description:</b> When configuring seed=0, hash distribution
  is not optimal.<b></b></p>
  </td>
 </tr>
 <tr>
  <td valign=top>
  <p><b>Workaround:</b> Avoid seed=0 configuration.<b
 ></b></p>
  </td>
 </tr>
 <tr>
  <td valign=top>
  <p><b>Keywords:</b> LAG, HASH<b></b></p>
  </td>
 </tr>
 <tr>
  <td valign=top>
  <p><b>Discovered in Version:</b> SONiC 202012<b
 ></b></p>
  </td>
 </tr>
 <tr>
  <td rowspan=4 valign=top>
  <p>-</p>
  </td>
  <td valign=top>
  <p><b>Description:</b> Dynamic port
  break out is not supported.</p>
  <p><b>Note:</b> All issues related to this capability are
  reported on github and are being handled by the community owner.</p>
  </td>
 </tr>
 <tr>
  <td valign=top>
  <p><b>Workaround:</b> N/A<b></b></p>
  </td>
 </tr>
 <tr>
  <td valign=top>
  <p><b>Keywords:</b> port breakout<b></b></p>
  </td>
 </tr>
 <tr>
  <td valign=top>
  <p><b>Discovered in Version:</b> SONiC 202012<b
 ></b></p>
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
  <p><b>Workaround:</b> N/A<b></b></p>
  </td>
 </tr>
 <tr>
  <td valign=top>
  <p><b>Keywords:</b> sflow<b></b></p>
  </td>
 </tr>
 <tr>
  <td valign=top>
  <p><b>Discovered in Version:</b> SONiC 202012<b
 ></b></p>
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
  <p><b>Keywords:</b> Ethernet;Spectrum-3, DAC</p>
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
  <p>2404336</p>
  
  </td>
  <td valign=top>
  <p><b>Description:</b> On very rare occasion, when
  connecting DR4 PAM4 transceiver to 100GbE DR1 NRZ, low BER may be
  experienced.</p>
  </td>
 </tr>
 <tr>
  <td valign=top>
  <p><b>Workaround:</b> N/A</p>
  </td>
 </tr>
 <tr>
  <td valign=top>
  <p><b>Keywords:</b> Ethernet;Spectrum-3, DR4</p>
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
  <p><b>Description:</b> Fastboot command may fail if the port-channel
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
  negotiation" drop reason is shown as "Other reason -"</p>
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
  <p><b>Description:</b> On SN3800 systems, Layer-1 state
  change counter currently does not function properly. We do not recommend
  using it. </p>
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
 <tr style='mso-yfti-irow:52'>
  <td rowspan=4 valign=top>
  <p>2074787</p>
  </td>
  <td valign=top>
  <p><b>Description:</b> The "show mac" command fails to
  show learnt MAC if a VLAN member is added in tagged mode.</p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:53'>
  <td valign=top>
  <p><b>Workaround:</b> N/A</p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:54'>
  <td valign=top>
  <p><b>Keywords:</b> FDB</p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:55'>
  <td valign=top>
  <p><b>Discovered in Version:</b> SONiC
  201911_MUR6</p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:56'>
  <td rowspan=4 valign=top>
  <p>2099346</p>
  </td>
  <td valign=top>
  <p><b>Description:</b> aclshow utility output does not
  display counters for Control plane ACLs.</p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:57'>
  <td valign=top>
  <p><b>Workaround:</b> Run: "sudo iptables -L -v -n" to display the counters fields also for the control plane ACLs. </p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:58'>
  <td valign=top>
  <p><b>Keywords:</b> aclshow control plane ACLs</p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:59'>
  <td valign=top>
  <p><b>Discovered in Version:</b> SONiC 201911_MUR6</p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:60'>
  <td rowspan=4 valign=top>
2382746
  </td>
  <td valign=top>
  <p><b>Description:</b> What Just Happened does not report
  dropped packet that their dropped reason is:  <i>"Unicast destination IP but multicast destination MAC"</i>.<br>
  To receive this drop reason, you can use the customer WJH XML configuration
  file, and set the severity of it from ‘Invalid’ to any other severity.</p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:61'>
  <td valign=top>
  <p><b>Workaround:</b> N/A</p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:62'>
  <td valign=top>
  <p><b>Keywords:</b> What Just Happened, dropped packets</p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:63'>
  <td valign=top>
  <p><b>Discovered in Version:</b> SONiC
  201911_MUR6</p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:64'>
  <td rowspan=4 valign=top>
  <p>2376634</p>
  </td>
  <td valign=top>
  <p><b>Description:</b> Warmboot on NVIDIA Spectrum-3 is
  not supported if using SONiC 201911_MUR5 <b>(HASH:</b>
  c453381aecfda14c276dcc7f8d357a034feb84b4) and below to reboot or upgrade
  to 201911_MUR6.</p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:65'>
  <td valign=top>
  <p><b>Workaround:</b> N/A</p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:66'>
  <td valign=top>
  <p><b>Keywords:</b> Warmboot, NVIDIA Spectrum-3</p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:67'>
  <td valign=top>
  <p><b>Discovered in Version:</b> SONiC
  201911_MUR6</p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:68'>
  <td rowspan=4 valign=top>
2329793
  </td>
  <td valign=top>
  <p><b>Description:</b> Modifying shared buffer during
  traffic might create undefined behavior and in rare cases will lead to
  packets stuck in the ASIC that will require ASIC reset to recover.</p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:69'>
  <td valign=top>
  <p><b>Workaround:</b> Stop traffic before configuring Shared Headroom.</p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:70'>
  <td valign=top>
  <p><b>Keywords:</b> Shared Headroom</p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:71'>
  <td valign=top>
  <p><b>Discovered in Version:</b> SONiC
  201911_MUR6</p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:72'>
  <td rowspan=4 valign=top>
  <p>2329924</p>
  </td>
  <td valign=top>
  <p><b>Description:</b> When connecting SN4700 with Cisco
  3432C using 400GbE, link does not rise in the corner port when using auto-negotiation.</p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:73'>
  <td valign=top>
  <p><b>Workaround:</b> N/A</p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:74'>
  <td valign=top>
  <p><b>Keywords:</b> SN4700, Link, 400GbE</p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:75'>
  <td valign=top>
  <p><b>Discovered in Version:</b> SONiC
  201911_MUR6</p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:76'>
  <td rowspan=4 valign=top>2355190
  </td>
  <td valign=top>
  <p><b>Description:</b> Warm-reboot with an ACL rule that
  has action set to mirror session is currently not supported.</p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:77'>
  <td valign=top>
  <p><b>Workaround:</b> N/A</p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:78'>
  <td valign=top>
  <p><b>Keywords:</b> Warm-reboot, ACL</p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:79'>
  <td valign=top>
  <p><b>Discovered in Version:</b> SONiC
  201911_MUR5</p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:80'>
  <td rowspan=4 valign=top>
  <p>2360012</p>
  </td>
  <td valign=top>
  <p><b>Description:</b> Warm-reboot fails if PFCWD is
  enabled on the port which its operational/admin status is down.</p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:81'>
  <td valign=top>
  <p><b>Workaround:</b> Do not enable PFCWD on ports that their operational/admin
  status is down.</p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:82'>
  <td valign=top>
  <p><b>Keywords:</b> Warm-reboot, PFCWD</p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:83'>
  <td valign=top>
  <p><b>Discovered in Version:</b> SONiC
  201911_MUR5</p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:84'>
  <td rowspan=4 valign=top>2272238
  </td>
  <td valign=top>
  <p><b>Description: </b>Connecting DR4 to DR1 using 100GbE may
  cause link flap.</p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:85'>
  <td valign=top>
  <p><b>Workaround:</b> N/A</p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:86'>
  <td valign=top>
  <p><b>Keywords:</b> Spectrum-3, Link</p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:87'>
  <td valign=top>
  <p><b>Discovered in Version:</b> SONiC
  201911_MUR5</p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:88'>
  <td rowspan=4 valign=top>2257265
  </td>
  <td valign=top>
  <p><b>Description:</b> In SN4600 system, the odd ports are
  not activated while using Split-4 mode.</p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:89'>
  <td valign=top>
  <p><b>Workaround:</b> N/A</p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:90'>
  <td valign=top>
  <p><b>Keywords:</b> Spectrum-3, SN4600, Split, Ports</p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:91'>
  <td valign=top>
  <p><b>Discovered in Version:</b> SONiC
  201911_MUR5</p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:92'>
  <td rowspan=4 valign=top>
  <p>2245426</p>
  </td>
  <td valign=top>
  <p><b>Description: </b>In the SN4600 system, the link does not
  rise when using LUX42604CO module at 40GbE after toggle.</p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:93'>
  <td valign=top>
  <p><b>Workaround:</b> N/A</p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:94'>
  <td valign=top>
  <p><b>Keywords:</b> Spectrum-3, SN4600C, Cables</p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:95'>
  <td valign=top>
  <p><b>Discovered in Version:</b> SONiC
  201911_MUR5</p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:96'>
  <td rowspan=4 valign=top>
  <p>2245816</p>
  </td>
  <td valign=top>
  <p><b>Description:</b> Splitting with Optical cables may
  not work in SN4600.</p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:97'>
  <td valign=top>
  <p><b>Workaround:</b> N/A</p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:98'>
  <td valign=top>
  <p><b>Keywords:</b> Spectrum-3, SN4600, Cables, Ports</p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:99'>
  <td valign=top>
  <p><b>Discovered in Version:</b> SONiC
  201911_MUR5</p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:100'>
  <td rowspan=4 valign=top>
  <p>2310453</p>
  </td>
  <td valign=top>
  <p><b>Description:</b> BGP running configuration is not
  reflected in the frr.conf file.</p>
  <p><b>Note:</b> As the BGP configuration is not
  present in the techsupport file, the user must take it separately.</p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:101'>
  <td valign=top>
  <p><b>Workaround:</b> Use the "show running bgp" or the vtysh
  -c "show run" commands to see the BGP running
  configuration. </p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:102'>
  <td valign=top>
  <p><b>Keywords:</b> BGP, frr.conf file</p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:103'>
  <td valign=top>
  <p><b>Discovered in Version:</b> SONiC
  201911_MUR4</p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:104'>
  <td rowspan=4 valign=top>2036710
  </td>
  <td valign=top>
  <p><b>Description:</b> A wrong MTU size is displayed in
  ICMP (type 3, code 4) when fragmentation is needed only for the VLAN
  interface.</p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:105'>
  <td valign=top>
  <p><b>Workaround:</b> N/A</p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:106'>
  <td valign=top>
  <p><b>Keywords:</b> MTU, VLAN, ICMP</p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:107'>
  <td valign=top>
  <p><b>Discovered in Version:</b> SONiC
  201911_MUR4</p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:108'>
  <td rowspan=4 valign=top>
  <p>-</p>
  </td>
  <td valign=top>
  <p><b>Description:</b> 10G BaseT modules are not supported
  on SN3800.</p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:109'>
  <td valign=top>
  <p><b>Workaround: </b>N/A</p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:110'>
  <td valign=top>
  <p><b>Keywords:</b> SN3800, 10G BaseT modules</p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:111'>
  <td valign=top>
  <p><b>Discovered in Version: </b>SONiC 201911_MUR3</p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:112'>
  <td rowspan=4 valign=top>
  <p>2053350</p>
  </td>
  <td valign=top>
  <p><b>Description:</b> In SN3800 system, when the link
  goes down on the partner side, the "link down counter" increases by
  two.</p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:113'>
  <td valign=top>
  <p><b>Workaround: </b>N/A</p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:114'>
  <td valign=top>
  <p><b>Keywords:</b> SN3800, Link</p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:115'>
  <td valign=top>
  <p><b>Discovered in Version: </b>SONiC 201911_MUR3</p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:116'>
  <td rowspan=4 valign=top>
  <p>2180871/2148429</p>
  </td>
  <td valign=top>
  <p><b>Description:</b> Symbol counter may show the wrong
  indication.</p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:117'>
  <td valign=top>
  <p><b>Workaround: </b>N/A</p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:118'>
  <td valign=top>
  <p><b>Keywords:</b> SN3800, Counters </p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:119'>
  <td valign=top>
  <p><b>Discovered in Version: </b>SONiC 201911_MUR3</p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:120'>
  <td rowspan=4 valign=top>
  <p>2231118</p>
  </td>
  <td valign=top>
  <p><b>Description:</b> On rare occasion, when connecting <i>DR4 to </i><b>NVIDIA Spectrum-3 systems on both sides</b>, toggling form both sides
  may cause the link to not rise.</p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:121'>
  <td valign=top>
  <p><b>Workaround: </b>N/A</p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:122'>
  <td valign=top>
  <p><b>Keywords:</b> Port Toggle</p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:123'>
  <td valign=top>
  <p><b>Discovered in Version: </b>SONiC 201911_MUR3</p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:124'>
  <td rowspan=4 valign=top>
  <p>2162540</p>
  </td>
  <td valign=top>
  <p><b>Description:</b> MPLS is not supported for ISSU,
  therefore MPLS configuration will not hold 0 hit traffic during ISSU.</p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:125'>
  <td valign=top>
  <p><b>Workaround: </b>N/A</p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:126'>
  <td valign=top>
  <p><b>Keywords:</b> ISSU</p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:127'>
  <td valign=top>
  <p><b>Discovered in Version: </b>SONiC 201911_MUR3</p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:128'>
  <td rowspan=4 valign=top>
  <p>1835086</p>
  </td>
  <td valign=top>
  <p><b>Description:</b> In re-configuration phase of the
  ISSU, ports' admin state cannot be changed to DOWN until
  "sx_api_issu_end_set()" is called.</p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:129'>
  <td valign=top>
  <p><b>Workaround: </b>N/A</p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:130'>
  <td valign=top>
  <p><b>Keywords:</b> ISSU</p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:131'>
  <td valign=top>
  <p><b>Discovered in Version: </b>SONiC 201911_MUR3</p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:132'>
  <td rowspan=4 valign=top>
  <p>2190769</p>
  </td>
  <td valign=top>
  <p><b>Description:</b> Incoming ARP and NDP requests
  trigger the RIF RX_ERR counter.</p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:133'>
  <td valign=top>
  <p><b>Workaround: </b>N/A</p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:134'>
  <td valign=top>
  <p><b>Keywords:</b> ARP</p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:135'>
  <td valign=top>
  <p><b>Discovered in Version: </b>SONiC 201911_MUR3</p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:136'>
  <td rowspan=4 valign=top>
  <p>2200131</p>
  </td>
  <td valign=top>
  <p><b>Description: </b>When resetting the SFP, the following
  error message is print out to the error log.</p>
  <p><i>" Receive PMPE error event on module 0: status 3 error type
  0".</i></p>
  <p>This can be safely ignored as it does not
  impact the functionality, SFP reset still works as usual.</p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:137'>
  <td valign=top>
  <p><b>Workaround: </b>N/A</p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:138'>
  <td valign=top>
  <p><b>Keywords:</b> SFP</p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:139'>
  <td valign=top>
  <p><b>Discovered in Version: </b>SONiC 201911_MUR2</p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:140'>
  <td rowspan=4 valign=top>
  
  </td>
  <td valign=top>
  <p><b>Description:</b> SAI does not support disabling
  Auto-Negotiation in SONiC.</p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:141'>
  <td valign=top>
  <p><b>Workaround: </b>N/A</p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:142'>
  <td valign=top>
  <p><b>Keywords:</b> Auto-Negotiation</p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:143'>
  <td valign=top>
  <p><b>Discovered in Version: </b>SONiC 201911_MUR1</p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:144'>
  <td rowspan=4 valign=top>
  <p>2102645</p>
  </td>
  <td valign=top>
  <p><b>Description:</b> Adding a tagged VLAN on a port while an
  FDB learning process is running on the same port, may result in a failure to
  read the FDB entry when running the "show mac" command.</p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:145'>
  <td valign=top>
  <p><b>Workaround: </b>N/A</p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:146'>
  <td valign=top>
  <p><b>Keywords:</b> FDB</p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:147'>
  <td valign=top>
  <p><b>Discovered in Version: </b>SONiC 201911_MUR1</p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:148'>
  <td rowspan=4 valign=top>
  <p>2078420</p>
  </td>
  <td valign=top>
  <p><b>Description:</b> The "show mac' command fails if
  running it while the MACs are being flushed from the FDB.</p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:149'>
  <td valign=top>
  <p><b>Workaround: </b>N/A</p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:150'>
  <td valign=top>
  <p><b>Keywords:</b> FDB</p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:151'>
  <td valign=top>
  <p><b>Discovered in Version: </b>SONiC 201911_MUR1</p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:152'>
  <td rowspan=4 valign=top>
  <p>2074787</p>
  </td>
  <td valign=top>
  <p><b>Description:</b> The "show mac" command fails
  to show any learnt MAC if a VLAN member is added when in tagged mode.</p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:153'>
  <td valign=top>
  <p><b>Workaround: </b>N/A</p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:154'>
  <td valign=top>
  <p><b>Keywords:</b> FDB</p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:155'>
  <td valign=top>
  <p><b>Discovered in Version: </b>SONiC 201911_MUR1</p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:156'>
  <td rowspan=4 valign=top>
  
  </td>
  <td valign=top>
  <p><b>Description:</b> Port spit to 8 is not supported on
  NVIDIA Spectrum-2 and NVIDIA Spectrum-3 switch systems.</p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:157'>
  <td valign=top>
  <p><b>Workaround: </b>N/A</p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:158'>
  <td valign=top>
  <p><b>Keywords:</b> port-split</p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:159'>
  <td valign=top>
  <p><b>Discovered in Version: </b>SONiC 201911_MUR1</p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:160'>
  <td rowspan=4 valign=top>
  
  </td>
  <td valign=top>
  <p><b>Description:</b> fastboot is not supported on NVIDIA
  Spectrum-2 switch systems.</p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:161'>
  <td valign=top>
  <p><b>Workaround: </b>N/A</p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:162'>
  <td valign=top>
  <p><b>Keywords:</b> fastboot</p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:163'>
  <td valign=top>
  <p><b>Discovered in Version: </b>SONiC 201911_MUR1</p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:164'>
  <td rowspan=4 valign=top>
  
  </td>
  <td valign=top>
  <p><b>Description:</b> The MTU of the network device created by
  the SDK and the MTU of the switch port are not synchronized.</p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:165'>
  <td valign=top>
  <p><b>Workaround:</b> Configure the network device MTU to be 4
  bytes smaller than the port MTU.</p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:166'>
  <td valign=top>
  <p><b>Keywords:</b> MTU</p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:167'>
  <td valign=top>
  <p><b>Discovered in Version: </b>SONiC 201911_MUR1</p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:168'>
  <td rowspan=4 valign=top>
  <p>2239785</p>
  </td>
  <td valign=top>
  <p><b>Description:</b> ‘ethtool’ does not support parsed
  QSFP-DD cable EEPROM content.</p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:169'>
  <td valign=top>
  <p><b>Workaround: </b>Run 'show interface transceiver eeprom &lt;interface-name&gt;
  to see the right content.</p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:170'>
  <td valign=top>
  <p><b>Keywords:</b> ethtool</p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:171'>
  <td valign=top>
  <p><b>Discovered in Version: </b>SONiC 201911</p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:172'>
  <td rowspan=4 valign=top>
  <p>2239867</p>
  </td>
  <td valign=top>
  <p><b>Description:</b> 400GbE cables (CMIS) and
  transceivers' EEPROM is missing Pages Support.</p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:173'>
  <td valign=top>
  <p><b>Workaround: </b>N/A</p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:174'>
  <td valign=top>
  <p><b>Keywords:</b> Cables</p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:175'>
  <td valign=top>
  <p><b>Discovered in Version: </b>SONiC 201911</p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:176'>
  <td rowspan=4 valign=top>
  <p>2116493</p>
  </td>
  <td valign=top>
  <p><b>Description: </b>Command "pfcwd show stats"
  returns wrong (zeroid) counters when a lossless priority is moved to an
  operational state after being in stormed state.</p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:177'>
  <td valign=top>
  <p><b>Workaround: </b>N/A</p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:178'>
  <td valign=top>
  <p><b>Keywords:</b> PFCWD</p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:179'>
  <td valign=top>
  <p><b>Discovered in Version: </b>SONiC 201911</p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:180'>
  <td rowspan=4 valign=top>
</td>
  <td valign=top>
  <p><b>Description: </b>Port ether stats/in/out packets 4K-9K
  counters count only packets 4K-8K.</p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:181'>
  <td valign=top>
  <p><b>Workaround: </b>N/A</p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:182'>
  <td valign=top>
  <p><b>Keywords:</b> Port counters</p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:183'>
  <td valign=top>
  <p><b>Discovered in Version: </b>SONiC 201911</p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:184'>
  <td rowspan=4 valign=top>
</td>
  <td valign=top>
  <p><b>Description: </b>ACL table can only be a member of a
  single sequential ACL group.</p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:185'>
  <td valign=top>
  <p><b>Workaround:</b> Create a table per sequential group.</p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:186'>
  <td valign=top>
  <p><b>Keywords: </b>ACL</p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:187'>
  <td valign=top>
  <p><b>Discovered in Version: </b>SONiC 201911</p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:188'>
  <td rowspan=4 valign=top>
</td>
  <td valign=top>
  <p><b>Description: </b>When using SAI_ACL_IP_TYPE_ANY, it is necessary
  to set at least one other field, as internally no key is used to match ANY
  value, and at least one key should be set for every rule.</p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:189'>
  <td valign=top>
  <p><b>Workaround:</b> Use additional field in the rule.</p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:190'>
  <td valign=top>
  <p><b>Keywords: </b>ACL</p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:191'>
  <td valign=top>
  <p><b>Discovered in Version: </b>SONiC 201911</p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:192'>
  <td rowspan=4 valign=top>
 </td>
  <td valign=top>
  <p><b>Description: </b>ACL SAI_ACL_ENTRY_ATTR_ACTION_MIRROR_INGRESS is not supported at Egress stage.</p>
  <p><b>Note:</b> An exception, for SAI_ACL_BIND_POINT_TYPE_ROUTER_INTERFACE at Egress stage, only SAI_ACL_ENTRY_ATTR_ACTION_MIRROR_INGRESS can be used.</p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:193'>
  <td valign=top>
  <p><b>Workaround: </b>N/A</p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:194'>
  <td valign=top>
  <p><b>Keywords: </b>ACL, Mirroring/SPAN</p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:195'>
  <td valign=top>
  <p><b>Discovered in Version: </b>SONiC 201911</p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:196'>
  <td rowspan=4 valign=top>
  </td>
  <td valign=top>
  <p><b>Description:</b> In the current DSCP mode, the DSCP value
  and the ECN mode are shared between the same type of tunnels.</p>
  <p>By changing the DSCP mode, the DSCP value
  and the ECN mode will affect all the tunnels of the same type. Tunnels are
  considered ‘the same type’ if both the following conditions are met:</p>
  <p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
  SAI_TUNNEL_ATTR_TYPE has the same
  value</p>
  <p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
  Tunnel direction has the same value.
  Direction has 3 types: encap, decap and symmetry</p>
  <p>o&nbsp;&nbsp; <b
 >Encap:</b> no decap
  attributes (start with SAI_TUNNEL_ATTR_ENCAP_) are configured during tunnel
  creation</p>
  <p>o&nbsp;&nbsp; <b
 >Decap:</b> no encap
  attributes (start with SAI_TUNNEL_ATTR_DECAP_) are configured during tunnel
  creation</p>
  <p>o&nbsp;&nbsp; <b
 >Symmetry:</b> Both encap and decap attributes are configured during tunnel creation</p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:197'>
  <td valign=top>
  <p><b>Workaround: </b>Use the same values for all tunnels of
  same type.</p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:198'>
  <td valign=top>
  <p><b>Keywords: </b>Tunnels</p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:199'>
  <td valign=top>
  <p><b>Discovered in Version: </b>SONiC 201911</p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:200'>
  <td rowspan=4 valign=top>
</td>
  <td valign=top>
  <p><b>Description: </b>In case the WRED profile
  has WRED and ECN mark enabled for at least one color, the enabled colors for
  WRED and ECN must be the same (For example, cannot have SAI_WRED_ATTR_GREEN_ENABLE=true and SAI_WRED_ATTR_ECN_MARK_MODE=SAI_ECN_MARK_MODE_YELLOW)</p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:201'>
  <td valign=top>
  <p><b>Workaround:</b> Use the same enabled colors for WRED and
  ECN.</p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:202'>
  <td valign=top>
  <p><b>Keywords: </b>WRED, ECN, QoS<b> </b></p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:203'>
  <td valign=top>
  <p><b>Discovered in Version: </b>SONiC 201911</p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:204'>
  <td rowspan=4 valign=top>
 </td>
  <td valign=top>
  <p><b>Description: </b>Clear queue stats for specific counters
  always clears all available counters.</p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:205'>
  <td valign=top>
  <p><b>Workaround: </b>N/A</p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:206'>
  <td valign=top>
  <p><b>Keywords: </b>Queues, Buffers</p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:207'>
  <td valign=top>
  <p><b>Discovered in Version: </b>SONiC 201911</p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:208'>
  <td rowspan=4 valign=top>
   </td>
  <td valign=top>
  <p><b>Description:</b> When using 3 mirror sessions, it is impossible to edit a session.</p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:209'>
  <td valign=top>
  <p><b>Workaround:</b> Remove the session and re-create it with
  the required new values.</p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:210'>
  <td valign=top>
  <p><b>Keywords: </b>Mirroring (or SPAN)</p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:211'>
  <td valign=top>
  <p><b>Discovered in Version: </b>SONiC 201911</p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:212'>
  <td rowspan=4 valign=top>
 </td>
  <td valign=top>
  <p><b>Description: </b>Switch Prio (SAI TC) &lt;-&gt; IEEE PFC
  is a global property, therefore when setting different PFC-&gt;PG on
  different ports, the last value set overrides the rest.</p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:213'>
  <td valign=top>
  <p><b>Workaround: </b>Set the same map on all the ports</p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:214'>
  <td valign=top>
  <p><b>Keywords: </b>QoS maps</p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:215'>
  <td valign=top>
  <p><b>Discovered in Version: </b>SONiC 201911</p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:216'>
  <td rowspan=4 valign=top>
  </td>
  <td valign=top>
  <p><b>Description: </b>Debug counters do not work correctly with
  WJH, and vice-versa, as the 2 features configurations conflict.</p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:217'>
  <td valign=top>
  <p><b>Workaround:</b></p>
  <p> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
  Delete all debug counters before using
  WJH</p>
  <p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
  Stop WJH before creating debug counters</p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:218'>
  <td valign=top>
  <p><b>Keywords: </b>Debug counters, WJH</p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:219'>
  <td valign=top>
  <p><b>Discovered in Version: </b>SONiC 201911</p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:220'>
  <td rowspan=4 valign=top>
</td>
  <td valign=top>
  <p><b>Description:</b> A specific drop reason can only exist in
  a single debug counter.</p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:221'>
  <td valign=top>
  <p><b>Workaround: </b>N/A</p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:222'>
  <td valign=top>
  <p><b>Keywords: </b>Debug counters</p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:223'>
  <td valign=top>
  <p><b>Discovered in Version: </b>SONiC 201911</p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:224'>
  <td rowspan=4 valign=top>
  <p>2137421</p>
  </td>
  <td valign=top>
  <p><b>Description: </b>In SN3800 system, when working in split
  mode, it is not possible to configure the first port to 50GbE while
  configuring the second port to either 25GbE or 10GbE.</p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:225'>
  <td valign=top>
  <p><b>Workaround: </b>N/A</p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:226'>
  <td valign=top>
  <p><b>Keywords:</b> SN3800</p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:227'>
  <td valign=top>
  <p><b>Discovered in Version: </b>SONiC 201911</p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:228'>
  <td rowspan=4 valign=top>
  <p>1973766</p>
  </td>
  <td valign=top>
  <p><b>Description: </b>Splitting a port to 4 is not supported in
  SN3800 switch systems.</p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:229'>
  <td valign=top>
  <p><b>Workaround: </b>N/A</p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:230'>
  <td valign=top>
  <p><b>Keywords:</b> SN3800, split port</p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:231'>
  <td valign=top>
  <p><b>Discovered in Version: </b>SONiC 201911</p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:232'>
  <td rowspan=4 valign=top>
  </td>
  <td valign=top>
  <p><b>Description: </b>On SN3800 switch system, traffic maybe
  dropped due to high BER in link on very rare occasions.</p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:233'>
  <td valign=top>
  <p><b>Workaround: </b>N/A</p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:234'>
  <td valign=top>
  <p><b>Keywords: </b>SN3800, Cables, Speeds, BER</p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:235'>
  <td valign=top>
  <p><b>Discovered in Version: </b>SONiC 201911</p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:236'>
  <td rowspan=4 valign=top>
 </td>
  <td valign=top>
  <p><b>Description: </b>SN3800 system does not interoperate with Cisco Nexus 9K C9236C or C9364.
  Link up takes long and connection is not guaranteed.</p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:237'>
  <td valign=top>
  <p><b>Workaround: </b>N/A</p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:238'>
  <td valign=top>
  <p><b>Keywords:</b> SN3800, link up</p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:239'>
  <td valign=top>
  <p><b>Discovered in Version: </b>SONiC 201911</p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:240'>
  <td rowspan=4 valign=top>
</td>
  <td valign=top>
  <p><b>Description:</b> 1GbE is currently not implemented on
  SN3800 system.</p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:241'>
  <td valign=top>
  <p><b>Workaround: </b>N/A</p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:242'>
  <td valign=top>
  <p><b>Keywords:</b> SN3800</p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:243'>
  <td valign=top>
  <p><b>Discovered in Version: </b>SONiC 201911</p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:244'>
  <td rowspan=4 valign=top>
  <p>2061691</p>
   </td>
  <td valign=top>
  <p><b>Description: </b>VLAN1 cannot be used by the user as it is
  reserved for SONiC internal purposes only. The usable VLAN ID for users
  starts as of VLAN2.</p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:245'>
  <td valign=top>
  <p><b>Workaround: </b>N/A</p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:246'>
  <td valign=top>
  <p><b>Keywords:</b> VLAN</p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:247'>
  <td valign=top>
  <p><b>Discovered in Version: </b>SONiC 201911</p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:248'>
  <td rowspan=4 valign=top>
  <p>1940359</td>
  <td valign=top>
  <p><b>Description: </b>On MSN2010 switch systems, if a system
  reboot is triggered using the "sudo reboot" command, the
  following wrong reboot cause is provided to the user "Hardware - Other (Reset caused
  by hotswap or halt)" instead of "reset_sw_reset”.</p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:249'>
  <td valign=top>
  <p><b>Workaround: </b>N/A</p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:250'>
  <td valign=top>
  <p><b>Keywords:</b> System reboot, MSN2010</p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:251'>
  <td valign=top>
  <p><b>Discovered in Version: </b>SONiC 201911</p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:252'>
  <td rowspan=4 valign=top>
  <p>2054684</p>
 </td>
  <td valign=top>
  <p><b>Description: </b>IPv6 L3 ACL table is not supported on
  NVIDIA Spectrum based switches.</p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:253'>
  <td valign=top>
  <p><b>Workaround: </b>N/A</p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:254'>
  <td valign=top>
  <p><b>Keywords:</b> IPv6 L3 ACL table</p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:255'>
  <td valign=top>
  <p><b>Discovered in Version: </b>SONiC 201911</p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:256'>
  <td rowspan=4 valign=top>  
  </td>
  <td valign=top>
  <p><b>Description:</b> When ISSU is enabled per SKU, hardware
  resources are reduced to half (routes, neighbors, ACLs).</p>
  <p>To check if ISSU is enabled for a
  specific SKU run:</p>
  <p>admin@arc-switch1004:~$
  show platform mlnx issu<br>
  ISSU is enabled<br>
  admin@arc-switch1004:~$</p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:257'>
  <td valign=top>
  <p><b>Workaround: </b>N/A</p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:258'>
  <td valign=top>
  <p><b>Keywords:</b> ISSU</p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:259'>
  <td valign=top>
  <p><b>Discovered in Version:</b> SONiC 201811</p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:260'>
  <td rowspan=4 valign=top>
  </td>
  <td valign=top>
  <p>Description:</b> The command `show interface counters` shows RX_BPS, RX_UTIL, TX_BPS, TX_UTIL as ‘N/A’ until `sonic-clear counters` is issued. The reason is a limitation in counter implementation by
  one of the vendors.</p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:261'>
  <td valign=top>
  <p><b>Workaround:</b> Run `sonic-clear counters` after every
  switch reboot/init. The pps/bps rates and port utilization should be
  available then.</p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:262'>
  <td valign=top>
  <p><b>Keywords:</b> Counters</p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:263'>
  <td valign=top>
  <p><b>Discovered in Version: </b>SONiC 201811</p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:264'>
  <td rowspan=4 valign=top>
  </td>
  <td valign=top>
  <p><b>Description:</b> ARP refreshing is only function on a
  VLAN interface.</p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:265'>
  <td valign=top>
  <p><b>Workaround: </b>N/A</p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:266'>
  <td valign=top>
  <p><b>Keywords:</b> ARP</p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:267'>
  <td valign=top>
  <p><b>Discovered in Version: </b>SONiC 201811</p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:268'>
  <td rowspan=4 valign=top>
  </td>
  <td valign=top>
  <p><b>Description:</b> Warm boot and fast boot are not
  supported on SN2010 switch systems.</p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:269'>
  <td valign=top>
  <p><b>Workaround: </b>N/A</p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:270'>
  <td valign=top>
  <p><b>Keywords: </b>Warm boot</p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:271'>
  <td valign=top>
  <p><b>Discovered in Version: </b>SONiC 201811</p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:272'>
  <td rowspan=4 valign=top>
  <p>1945337</p>
  </td>
  <td valign=top>
  <p><b>Description: </b>PFCWD does not detect PFC storm for lossy
  priority on a port that ASYM-PFC is enabled.</p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:273'>
  <td valign=top>
  <p><b>Workaround: </b>N/A</p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:274'>
  <td valign=top>
  <p><b>Keywords: </b>PFCWD</p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:275'>
  <td valign=top>
  <p><b>Discovered in Version: </b>SONiC 201811</p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:276'>
  <td rowspan=4 valign=top>
  </td>
  <td valign=top>
  <p><b>Description: </b>Bit Error Rate Monitoring (BER) is not
  supported on 10GbaseT modules.</p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:277'>
  <td valign=top>
  <p><b>Workaround: </b>N/A</p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:278'>
  <td valign=top>
  <p><b>Keywords: </b>BER, 10GbaseT modules</p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:279'>
  <td valign=top>
  <p><b>Discovered in Version: </b>SONiC 201811</p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:280'>
  <td rowspan=4 valign=top>
  </td>
  <td valign=top>
  <p><b>Description: </b>Rx LOS is not supported when both sides
  of the link are of type BaseT.</p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:281'>
  <td valign=top>
  <p><b>Workaround: </b>N/A</p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:282'>
  <td valign=top>
  <p><b>Keywords: </b>Rx LOS, BaseT modules</p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:283'>
  <td valign=top>
  <p><b>Discovered in Version: </b>SONiC 201811</p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:284'>
  <td rowspan=4 valign=top>
  </td>
  <td valign=top>
  <p><b>Description: </b>When configuring shared buffers, the
  software does not verify that Xon &lt; Xoff &lt; buffer size.</p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:285'>
  <td valign=top>
  <p><b>Workaround: </b>Please make sure to meet these
  requirements during configuration.</p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:286'>
  <td valign=top>
  <p><b>Keywords: </b>Shared Buffers</p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:287'>
  <td valign=top>
  <p><b>Discovered in Version: </b>SONiC 201811</p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:288'>
  <td rowspan=4 valign=top>
  </td>
  <td valign=top>
  <p><b>Description: </b>The minimum reserved buffer space for
  egress traffic is 1.</p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:289'>
  <td valign=top>
  <p><b>Workaround: </b>N/A</p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:290'>
  <td valign=top>
  <p><b>Keywords: </b>Shared Buffers</p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:291'>
  <td valign=top>
  <p><b>Discovered in Version: </b>SONiC 201811</p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:292'>
  <td rowspan=4 valign=top>
  </td>
  <td valign=top>
  <p><b>Description: </b>Mapping of switch priority 7 to a non-default
  Priority Group (PG) is not permitted and causes an unexpected behavior.</p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:293'>
  <td valign=top>
  <p><b>Workaround: </b>N/A</p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:294'>
  <td valign=top>
  <p><b>Keywords: </b>Switch Priority, Priority Group (PG)</p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:295'>
  <td valign=top>
  <p><b>Discovered in Version: </b>SONiC 201811</p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:296'>
  <td rowspan=4 valign=top>
  
  </td>
  <td valign=top>
  <p><b>Description: </b>Toggling port speed from 1GbE to other
  speeds may block 1GbE traffic.</p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:297'>
  <td valign=top>
  <p><b>Workaround: </b>N/A</p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:298'>
  <td valign=top>
  <p><b>Keywords: </b>Port toggling</p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:299'>
  <td valign=top>
  <p><b>Discovered in Version: </b>SONiC 201811</p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:300'>
  <td rowspan=4 valign=top>
   </td>
  <td valign=top>
  <p><b>Description: </b>In some configuration cases, Priority
  Flow Control does not perform as expected.</p>
  <p>Only one of the following maps can have
  "none" default value:</p>
  <p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
  TC_TO_QUEUE_MAP</p>
  <p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
  MAP_PFC_PRIORITY_TO_QUEUE</p>
  <p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
  TC_TO_PRIORITY_GROUP_MAP</p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:301'>
  <td valign=top>
  <p><b>Workaround:</b> A single instance of
  TC_TO_PRIORITY_GROUP_MAP should be applied on all interfaces.</p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:302'>
  <td valign=top>
  <p><b>Keywords:</b> QoS mapping</p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:303'>
  <td valign=top>
  <p><b>Discovered in Version: </b>SONiC 201811</p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:304'>
  <td rowspan=4 valign=top>
  <p>849302</p>
  </td>
  <td valign=top>
  <p><b>Description: </b>Traffic is not divided up correctly under
  congestion if working with Strict priority.</p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:305'>
  <td valign=top>
  <p><b>Workaround: </b>N/A</p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:306'>
  <td valign=top>
  <p><b>Keywords: </b>Congestion, port priority</p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:307;mso-yfti-lastrow:yes'>
  <td valign=top>
  <p><b>Discovered in Version: </b>SONiC 201811</p>
  </td>
 </tr>
</table>
