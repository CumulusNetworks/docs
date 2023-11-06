---
title: NVIDIA NetQ 4.8 Release Notes
author: Cumulus Networks
weight: 30
product: Cumulus NetQ
version: "4.8"
toc: 1
type: rn
pdfhidden: True
---
{{<rn_xls_link dir="cumulus-netq-48" >}}
## 4.8.0 Release Notes
### Open Issues in 4.8.0

|  Issue ID 	|   Description	|   Affects	|   Fixed |
|---	        |---	        |---	    |---	                |
| <a name="3435373"></a> [3435373](#3435373) <a name="3435373"></a> <br /> | If your NetQ on-premises VM is not configured with at least 16 vCPUs, upgrades from NetQ 4.5.0 to 4.6.0 using the <code>netq upgrade bundle</code> command fail with the following message: <pre>Job upgrade failed or timed out<br /></pre>To work around this issue, reconfigure your VM to use 16 vCPUs before upgrading. | 4.5.0-4.8.0 | |
| <a name="3429528"></a> [3429528](#3429528) <a name="3429528"></a> <br /> | EVPN and RoCE validation cards in the NetQ UI might not display data when Cumulus Linux switches are configured with high VNI scale. | 4.6.0-4.8.0 | |
| <a name="2885312"></a> [2885312](#2885312) <a name="2885312"></a> <br /> | EVPN Validation Type 2 checks might show false Duplicate MAC events for MAC addresses that are not duplicated. An example of this is shown below:<br />  <pre>EVPN Type 2 Test details:<br />  Hostname          Peer Name         Peer Hostname     Reason                                        Last Changed<br />  ----------------- ----------------- ----------------- --------------------------------------------- -------------------------<br />  torc-11           -                 -                 Duplicate Mac 00:02:00:00:00:55 VLAN 1249 at  Sun Dec  5 18:26:14 2021<br />                                                        torc-21:vx-282 and torc-11:peerlink-3<br />  </pre> | 4.1.0-4.8.0 | |

### Fixed Issues in 4.8.0
|  Issue ID 	|   Description	|   Affects	|
|---	        |---	        |---	    |
| <a name="3555031"></a> [3555031](#3555031) <a name="3555031"></a> <br /> | NetQ incorrectly reports a low health SSD event on SN5600 switches. To work around this issue, configure an event suppression rule for <code>ssdutil</code> messages from SN5600 switches in your network. | 4.7.0 | |
| <a name="3530739"></a> [3530739](#3530739) <a name="3530739"></a> <br /> | Queue histogram data received from switches might encounter a delay before appearing in the NetQ UI. | 4.7.0 | |

