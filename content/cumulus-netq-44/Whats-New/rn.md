---
title: NVIDIA NetQ 4.4 Release Notes
author: NVIDIA
weight: 30
product: Cumulus NetQ
version: "4.4"
toc: 1
type: rn
pdfhidden: True
---
{{<rn_xls_link dir="cumulus-netq-44" >}}
## 4.3.0 Release Notes
### Open Issues in 4.3.0

|  Issue ID 	|   Description	|   Affects	|   Fixed |
|---	        |---	        |---	    |---	                |
| <a name="3053143"></a> [3053143](#3053143) <a name="3053143"></a> <br /> | The MLAG Session card might not show all MLAG events. | 4.2.0-4.3.0 | |
| <a name="3043146"></a> [3043146](#3043146) <a name="3043146"></a> <br /> | After you upgrade from NetQ 4.1 to NetQ 4.2, some streaming validation checks might erroneously report failures when services are running properly. This condition will resolve itself within 24 hours of the upgrade.  | 4.2.0-4.3.0 | |
| <a name="3015875"></a> [3015875](#3015875) <a name="3015875"></a> <br /> | NetQ trace might report incomplete route information when there are multiple default routes in a VRF in the path between the source and destination. | 4.1.0-4.3.0 | |
| <a name="2885312"></a> [2885312](#2885312) <a name="2885312"></a> <br /> | EVPN Validation Type 2 checks might show false Duplicate MAC events for MAC addresses that are not duplicated. An example of this is shown below:<br />  <pre>EVPN Type 2 Test details:<br />  Hostname          Peer Name         Peer Hostname     Reason                                        Last Changed<br />  ----------------- ----------------- ----------------- --------------------------------------------- -------------------------<br />  torc-11           -                 -                 Duplicate Mac 00:02:00:00:00:55 VLAN 1249 at  Sun Dec  5 18:26:14 2021<br />                                                        torc-21:vx-282 and torc-11:peerlink-3<br />  </pre> | 4.1.0-4.3.0 | |
| <a name="2872288"></a> [2872288](#2872288) <a name="2872288"></a> <br /> | When a NetQ agent sends messages with validation check data, there might be a delay of up to 120 seconds before the new data is displayed in streaming validation checks. | 4.2.0-4.3.0 | |
| <a name="2663534"></a> [2663534](#2663534) <a name="2663534"></a> <br /> | Validation check filtering is only applied to errors in validation results and is not applied to warnings in validation results. | 4.0.0-4.3.0 | |
| <a name="2555854"></a> [2555854](#2555854) <a name="2555854"></a> <br />NETQ-8245 | NetQ Agent: If a NetQ Agent is downgraded to the 3.0.0 version from any higher release, the default commands file present in the _/etc/netq/commands/_ also needs to be updated to prevent the NetQ Agent from becoming rotten. | 3.0.0-3.3.1, 4.0.0-4.3.0 | |
| <a name="2549649"></a> [2549649](#2549649) <a name="2549649"></a> <br />NETQ-5737 | NetQ UI: Warnings might appear during the post-upgrade phase for a Cumulus Linux switch upgrade job. They are caused by services that have not yet been restored by the time the job is complete. Cumulus Networks recommend waiting five minutes, creating a network snapshot, then comparing that to the pre-upgrade snapshot. If the comparison shows no differences for the services, the warnings can be ignored. If there are differences, then troubleshooting the relevant service(s) is recommended. | 3.0.0-3.3.1, 4.0.0-4.3.0 | |

### Fixed Issues in 4.3.0
|  Issue ID 	|   Description	|   Affects	|
|---	        |---	        |---	    |
| <a name="3085017"></a> [3085017](#3085017) <a name="3085017"></a> <br /> | When you hover over a device with WJH events in the flow analysis graph, the number of WJH packet drops in the event summary might display 0 drops. This is because the device did not detect any WJH events on the selected path. To view the WJH events, select different paths to display any WJH events for that device. | 4.2.0 | |
| <a name="3047149"></a> [3047149](#3047149) <a name="3047149"></a> <br /> | When you reboot the OPTA, the NetQ validation summary might show an incorrect number of validations. This condition will resolve itself within an hour of the reboot. | 4.2.0 | |
| <a name="2817749"></a> [2817749](#2817749) <a name="2817749"></a> <br /> | If you configure an event suppression rule with <code>is_active false</code>, the event will no longer be displayed with the <code>netq show events-config</code> command. | 4.0.1-4.2.0 | |

