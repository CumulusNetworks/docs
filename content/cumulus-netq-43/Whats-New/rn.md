---
title: NVIDIA Cumulus NetQ 4.3 Release Notes
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
| 3739222 | The <code>opta-check</code> command does not properly validate if the required 16 CPU cores are present on the system for NetQ. The command only presents an error if there are fewer than 8 CPU cores detected. | 4.2.0-4.8.0 | 4.9.0-4.15.1|
| 3442456 | When an event notification is resolved or acknowledged, the NetQ UI might display a duplicate event with the original notification content and timestamp. | 4.2.0-4.6.0 | 4.7.0-4.15.1|
| 3438973 | When you install NetQ onto your VM, the installation fails with the following messages:<pre>05:57:33.023618: master-node-installer: Installed Debian ...	&#91; FAILED &#93;--------------------------------------ERROR: Failed to install the master node</pre>This is due to an expired key in the installation tarball. For assistance working around this issue, contact NVIDIA support. | 4.3.0-4.5.0 | 4.6.0-4.15.1|
| 3303284 | When you run the  <code>netq show opta-health</code> command, it might fail and produce the following error:<pre>ERROR: Expecting value: line 1 column 1 (char 0)</pre> | 4.3.0-4.4.1 | 4.5.0-4.15.1|
| 3226405 | TLS versions 1.0 and 1.1 are enabled for the OPTA API Gateway listening on TCP port 32708. Only TLS versions 1.2 and 1.3 should be enabled. | 4.3.0 | 4.4.0-4.15.1|
| 3216161 | In an OPTA clustered environment, NetQ agents might appear as rotten after upgrading to NetQ 4.3.0. To work around this issue, configure the <code>spice: false</code> parameter in <code>/etc/netq/netq.yml</code>. | 4.3.0 | 4.4.0-4.15.1|
| 3211317 | Upgrading Cumulus Linux with NetQ LCM fails when you upgrade a switch with the MLAG primary role. | 4.3.0 | 4.4.0-4.15.1|
| 3205778 | In some high scale environments, NetQ agents might appear as rotten during high load. | 4.3.0 | 4.4.0-4.15.1|
| 3179145 | The NetQ agent does not collect VLAN information from WJH data. This has been resolved, however when you upgrade to a NetQ version with the fix, historical WJH data will not be displayed in the UI. | 4.3.0-4.4.1 | 4.5.0-4.15.1|
| 3157803 | The <code>netq show</code> commands to view MACs, IP addresses, neighbors, and routes might show a higher value compared to the corresponding entries in the NetQ UI. The <code>netq show</code> commands display additional values from the NetQ server or OPTA in addition to monitored devices in the NetQ inventory. | 4.2.0-4.3.0 | 4.4.0-4.15.1|
| 3131311, 3234182 | Sensor validation checks might still reflect a failure in NetQ after the sensor failure has recovered. | 4.2.0-4.3.0 | 4.4.0-4.15.1|
| 3085064, 2838027, 2551494 | When you attempt to install NetQ on a device using LCM and configure the incorrect VRF, the installation will be reflected as successful but the switch will not be present in the inventory in the LCM UI. | 4.1.0-4.3.0 | 4.4.0-4.15.1|
| 3053143 | The MLAG Session card might not show all MLAG events. | 4.2.0-4.3.0 | 4.4.0-4.15.1|
| 3015875 | NetQ trace might report incomplete route information when there are multiple default routes in a VRF in the path between the source and destination. | 4.1.0-4.4.1 | 4.5.0-4.15.1|
| 2605545 | Sort functionality is disabled when the number of records exceeds 10,000 entries in a full-screen, tabular view.  | 4.3.0 | 4.4.0-4.15.1|

### Fixed Issues in 4.3.0
|  Issue ID 	|   Description	|   Affects	|
|---	        |---	        |---	    |
| 3136898 | On switches running Cumulus Linux 5.2.0 and NetQ agent 4.2.0 or earlier, NetQ commands might fail and errors are logged to <code>/var/log/netq-agent.log</code>. To work around this issue, use NetQ agent version 4.3.0. | 4.2.0 | |
| 3085017 | When you hover over a device with WJH events in the flow analysis graph, the number of WJH packet drops in the event summary might display 0 drops. This is because the device did not detect any WJH events on the selected path. To view the WJH events, select different paths to display any WJH events for that device. | 4.2.0 | |
| 3047149 | When you reboot the OPTA, the NetQ validation summary might show an incorrect number of validations. This condition will resolve itself within an hour of the reboot. | 4.2.0 | |
| 2817749 | If you configure an event suppression rule with <code>is_active false</code>, the event will no longer be displayed with the <code>netq show events-config</code> command. | 4.0.1-4.2.0 | |

