---
title: NVIDIA NetQ 4.3 Release Notes
author: NVIDIA
weight: 30
product: Cumulus NetQ
version: "4.3"
toc: 1
type: rn
pdfhidden: True
---
{{<rn_xls_link dir="cumulus-netq-43" >}}
## 4.3.0 Release Notes
### Open Issues in 4.3.0

|  Issue ID 	|   Description	|   Affects	|   Fixed |
|---	        |---	        |---	    |---	                |
| <a name="3226405"></a> [3226405](#3226405) <a name="3226405"></a> <br /> | TLS versions 1.0 and 1.1 are enabled for the OPTA API Gateway listening on TCP port 32708. Only TLS versions 1.2 and 1.3 should be enabled. | 4.3.0 | |
| <a name="3216161"></a> [3216161](#3216161) <a name="3216161"></a> <br /> | In an OPTA clustered environment, NetQ agents might appear as rotten after upgrading to NetQ 4.3.0. To work around this issue, configure the <code>spice: false</code> parameter in <code>/etc/netq/netq.yml</code>. | 4.3.0 | |
| <a name="3211317"></a> [3211317](#3211317) <a name="3211317"></a> <br /> | Upgrading Cumulus Linux with NetQ LCM fails when you upgrade a switch with the MLAG primary role. | 4.3.0 | |
| <a name="3205778"></a> [3205778](#3205778) <a name="3205778"></a> <br /> | In some high scale environments, NetQ agents might appear as rotten during high load. | 4.3.0 | |
| <a name="3157803"></a> [3157803](#3157803) <a name="3157803"></a> <br /> | The <code>netq show</code> commands to view MACs, IP addresses, neighbors, and routes might show a higher value compared to the corresponding entries in the NetQ UI. The <code>netq show</code> commands display additional values from the NetQ server or OPTA in addition to monitored devices in the NetQ inventory. | 4.2.0-4.3.0 | |
| <a name="3131311"></a> [3131311](#3131311) <a name="3131311"></a> <br /> | Sensor validation checks might still reflect a failure in NetQ after the sensor failure has recovered. | 4.2.0-4.3.0 | |
| <a name="3085064"></a> [3085064](#3085064) <a name="3085064"></a> <br /> | When you attempt to install NetQ on a device using LCM and configure the incorrect VRF, the installation will be reflected as successful but the switch will not be present in the inventory in the LCM UI. | 4.1.0-4.3.0 | |
| <a name="3053143"></a> [3053143](#3053143) <a name="3053143"></a> <br /> | The MLAG Session card might not show all MLAG events. | 4.2.0-4.3.0 | |
| <a name="3043146"></a> [3043146](#3043146) <a name="3043146"></a> <br /> | After you upgrade from NetQ 4.1 to NetQ 4.2, some streaming validation checks might erroneously report failures when services are running properly. This condition will resolve itself within 24 hours of the upgrade.  | 4.2.0-4.3.0 | |
| <a name="3015875"></a> [3015875](#3015875) <a name="3015875"></a> <br /> | NetQ trace might report incomplete route information when there are multiple default routes in a VRF in the path between the source and destination. | 4.1.0-4.3.0 | |
| <a name="2885312"></a> [2885312](#2885312) <a name="2885312"></a> <br /> | EVPN Validation Type 2 checks might show false Duplicate MAC events for MAC addresses that are not duplicated. An example of this is shown below:<br />  <pre>EVPN Type 2 Test details:<br />  Hostname          Peer Name         Peer Hostname     Reason                                        Last Changed<br />  ----------------- ----------------- ----------------- --------------------------------------------- -------------------------<br />  torc-11           -                 -                 Duplicate Mac 00:02:00:00:00:55 VLAN 1249 at  Sun Dec  5 18:26:14 2021<br />                                                        torc-21:vx-282 and torc-11:peerlink-3<br />  </pre> | 4.1.0-4.3.0 | |
| <a name="2872288"></a> [2872288](#2872288) <a name="2872288"></a> <br /> | When a NetQ agent sends messages with validation check data, there might be a delay of up to 120 seconds before the new data is displayed in streaming validation checks. | 4.2.0-4.3.0 | |
| <a name="2605545"></a> [2605545](#2605545) <a name="2605545"></a> <br /> | Sort functionality is disabled when the number of records exceeds 10,000 entries in a full-screen, tabular view.  | 4.3.0 | |

### Fixed Issues in 4.3.0
|  Issue ID 	|   Description	|   Affects	|
|---	        |---	        |---	    |
| <a name="3136898"></a> [3136898](#3136898) <a name="3136898"></a> <br /> | On switches running Cumulus Linux 5.2.0 and NetQ agent 4.2.0 or earlier, NetQ commands might fail and errors are logged to <code>/var/log/netq-agent.log</code>. To work around this issue, use NetQ agent version 4.3.0. | 4.2.0 | |
| <a name="3085017"></a> [3085017](#3085017) <a name="3085017"></a> <br /> | When you hover over a device with WJH events in the flow analysis graph, the number of WJH packet drops in the event summary might display 0 drops. This is because the device did not detect any WJH events on the selected path. To view the WJH events, select different paths to display any WJH events for that device. | 4.2.0 | |
| <a name="3047149"></a> [3047149](#3047149) <a name="3047149"></a> <br /> | When you reboot the OPTA, the NetQ validation summary might show an incorrect number of validations. This condition will resolve itself within an hour of the reboot. | 4.2.0 | |
| <a name="2817749"></a> [2817749](#2817749) <a name="2817749"></a> <br /> | If you configure an event suppression rule with <code>is_active false</code>, the event will no longer be displayed with the <code>netq show events-config</code> command. | 4.0.1-4.2.0 | |

