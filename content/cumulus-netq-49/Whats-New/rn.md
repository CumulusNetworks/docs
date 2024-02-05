---
title: NVIDIA NetQ 4.9 Release Notes
author: Cumulus Networks
weight: 30
product: Cumulus NetQ
version: "4.9"
toc: 1
type: rn
pdfhidden: True
---
{{<rn_xls_link dir="cumulus-netq-49" >}}
## 4.9.0 Release Notes
### Open Issues in 4.9.0

|  Issue ID 	|   Description	|   Affects	|   Fixed |
|---	        |---	        |---	    |---	                |
| <a name="3633458"></a> [3633458](#3633458) <a name="3633458"></a> <br /> | The legacy topology diagram might categorize devices into tiers incorrectly. To work around this issue, use the updated topology diagram by selecting Topology Beta in the NetQ 4.8.0 UI. | 4.7.0-4.9.0 | |
| <a name="3613811"></a> [3613811](#3613811) <a name="3613811"></a> <br /> | LCM operations using in-band management are unsupported on switches that use eth0 connected to an out-of-band network. To work around this issue, configure NetQ to use out-of-band management in the <code>mgmt</code> VRF on Cumulus Linux switches when interface eth0 is in use. | 4.8.0-4.9.0 | |
| <a name="2885312"></a> [2885312](#2885312) <a name="2885312"></a> <br /> | EVPN Validation Type 2 checks might show false Duplicate MAC events for MAC addresses that are not duplicated. An example of this is shown below:<br />  <pre>EVPN Type 2 Test details:<br />  Hostname          Peer Name         Peer Hostname     Reason                                        Last Changed<br />  ----------------- ----------------- ----------------- --------------------------------------------- -------------------------<br />  torc-11           -                 -                 Duplicate Mac 00:02:00:00:00:55 VLAN 1249 at  Sun Dec  5 18:26:14 2021<br />                                                        torc-21:vx-282 and torc-11:peerlink-3<br />  </pre> | 4.1.0-4.9.0 | |

### Fixed Issues in 4.9.0
|  Issue ID 	|   Description	|   Affects	|
|---	        |---	        |---	    |
| <a name="3644644"></a> [3644644](#3644644) <a name="3644644"></a> <br /> | When you perform an LCM upgrade of Cumulus Linux on a switch using the <code>netq lcm upgrade cl-image</code> CLI command, an error message of <code>NetQ cloud token invalid</code> is displayed though the upgrade completes successfully. This issue is not encountered when using the NetQ LCM UI to perform the upgrade. | 4.8.0 | |
| <a name="3634648"></a> [3634648](#3634648) <a name="3634648"></a> <br /> | The topology graph might show unexpected connections when devices in the topology do not have LLDP adjacencies. | 4.8.0 | |
| <a name="3632378"></a> [3632378](#3632378) <a name="3632378"></a> <br /> | After you upgrade your on-premises NetQ VM from version 4.7.0 to 4.8.0, NIC telemetry using the Prometheus adapter is not collected. To work around this issue, run the following commands on your NetQ VM:<pre>sudo kubectl set image deployment/netq-prom-adapter netq-prom-adapter=docker-registry:5000/netq-prom-adapter:4.8.0<br>sudo kubectl set image deployment/netq-prom-adapter prometheus=docker-registry:5000/prometheus-v2.41.0:4.8.0</pre> | 4.8.0 | |
| <a name="3549877"></a> [3549877](#3549877) <a name="3549877"></a> <br /> | NetQ cloud deployments might unexpectedly display validation results for checks that did not run on any nodes. | 4.6.0-4.8.0 | |
| <a name="3429528"></a> [3429528](#3429528) <a name="3429528"></a> <br /> | EVPN and RoCE validation cards in the NetQ UI might not display data when Cumulus Linux switches are configured with high VNI scale. | 4.6.0-4.8.0 | |

