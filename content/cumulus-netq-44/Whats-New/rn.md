---
title: NVIDIA Cumulus NetQ 4.4 Release Notes
author: NVIDIA
weight: 30
product: Cumulus NetQ
version: "4.4"
toc: 1
type: rn
pdfhidden: True
---
{{<rn_xls_link dir="cumulus-netq-44" >}}
## 4.4.1 Release Notes
### Open Issues in 4.4.1

|  Issue ID 	|   Description	|   Affects	|   Fixed |
|---	        |---	        |---	    |---	                |
| 3739222 | The <code>opta-check</code> command does not properly validate if the required 16 CPU cores are present on the system for NetQ. The command only presents an error if there are fewer than 8 CPU cores detected. | 4.2.0-4.8.0 | 4.9.0-4.15.1|
| 3442456 | When an event notification is resolved or acknowledged, the NetQ UI might display a duplicate event with the original notification content and timestamp. | 4.2.0-4.6.0 | 4.7.0-4.15.1|
| 3438973 | When you install NetQ onto your VM, the installation fails with the following messages:<pre>05:57:33.023618: master-node-installer: Installed Debian ...	&#91; FAILED &#93;--------------------------------------ERROR: Failed to install the master node</pre>This is due to an expired key in the installation tarball. For assistance working around this issue, contact NVIDIA support. | 4.3.0-4.5.0 | 4.6.0-4.15.1|
| 3395385 | When you use NetQ LCM to upgrade a Cumulus Linux switch in an MLAG pair, the upgrade might fail. | 4.4.1-4.5.0 | 4.6.0-4.15.1|
| 3360627 | When the switch RoCE egress pool buffer limit is configured as unlimited, the maximum buffer usage for RoCE counters might display incorrect values in the NetQ UI. | 4.4.1-4.5.0 | 4.6.0-4.15.1|
| 3305144 | When you perform a <code>netq trace</code> between two hosts, the following message might be printed in the output even when the trace is successful:<pre>argument of type ‘NoneType’ is not iterable</pre> | 4.4.0-4.4.1 | 4.5.0-4.15.1|
| 3303284 | When you run the  <code>netq show opta-health</code> command, it might fail and produce the following error:<pre>ERROR: Expecting value: line 1 column 1 (char 0)</pre> | 4.3.0-4.4.1 | 4.5.0-4.15.1|
| 3290068 | When you back up NetQ data with the <code>backuprestore.sh</code> script, the operation fails with the following log messages:<pre>Failed to clear all earlier snapshot for keyspace:master. Exiting!command terminated with exit code 1Failed to execute /opt/backuprestore/createbackup.sh script on cassandra pod<br />Failed to proceed ahead with backup procedure. Exiting !</pre>Contact NVIDIA support for assistance performing a backup. | 4.4.0-4.4.1 | 4.5.0-4.15.1|
| 3266922 | When a NetQ agent sends your NetQ server or OPTA an unexpectedly large number for switch interface counters, <code>netq check</code> and <code>netq show</code> commands might fail with the following message:<pre>local variable ‘url’ referenced before assignment</pre> | 4.4.0-4.4.1 | 4.5.0-4.15.1|
| 3241664 | When you start the <code>netq-agent</code> service, the WJH service is enabled by default.  However, when you run the <code>netq config show agent wjh</code> command, the output might reflect the WJH service as disabled. | 4.4.0-4.4.1 | 4.5.0-4.15.1|
| 3179145 | The NetQ agent does not collect VLAN information from WJH data. This has been resolved, however when you upgrade to a NetQ version with the fix, historical WJH data will not be displayed in the UI. | 4.3.0-4.4.1 | 4.5.0-4.15.1|
| 3015875 | NetQ trace might report incomplete route information when there are multiple default routes in a VRF in the path between the source and destination. | 4.1.0-4.4.1 | 4.5.0-4.15.1|

### Fixed Issues in 4.4.1
|  Issue ID 	|   Description	|   Affects	|
|---	        |---	        |---	    |

## 4.4.0 Release Notes
### Open Issues in 4.4.0

|  Issue ID 	|   Description	|   Affects	|   Fixed |
|---	        |---	        |---	    |---	                |
| 3739222 | The <code>opta-check</code> command does not properly validate if the required 16 CPU cores are present on the system for NetQ. The command only presents an error if there are fewer than 8 CPU cores detected. | 4.2.0-4.8.0 | 4.9.0-4.15.1|
| 3442456 | When an event notification is resolved or acknowledged, the NetQ UI might display a duplicate event with the original notification content and timestamp. | 4.2.0-4.6.0 | 4.7.0-4.15.1|
| 3438973 | When you install NetQ onto your VM, the installation fails with the following messages:<pre>05:57:33.023618: master-node-installer: Installed Debian ...	&#91; FAILED &#93;--------------------------------------ERROR: Failed to install the master node</pre>This is due to an expired key in the installation tarball. For assistance working around this issue, contact NVIDIA support. | 4.3.0-4.5.0 | 4.6.0-4.15.1|
| 3305144 | When you perform a <code>netq trace</code> between two hosts, the following message might be printed in the output even when the trace is successful:<pre>argument of type ‘NoneType’ is not iterable</pre> | 4.4.0-4.4.1 | 4.5.0-4.15.1|
| 3303284 | When you run the  <code>netq show opta-health</code> command, it might fail and produce the following error:<pre>ERROR: Expecting value: line 1 column 1 (char 0)</pre> | 4.3.0-4.4.1 | 4.5.0-4.15.1|
| 3290068 | When you back up NetQ data with the <code>backuprestore.sh</code> script, the operation fails with the following log messages:<pre>Failed to clear all earlier snapshot for keyspace:master. Exiting!command terminated with exit code 1Failed to execute /opt/backuprestore/createbackup.sh script on cassandra pod<br />Failed to proceed ahead with backup procedure. Exiting !</pre>Contact NVIDIA support for assistance performing a backup. | 4.4.0-4.4.1 | 4.5.0-4.15.1|
| 3266922 | When a NetQ agent sends your NetQ server or OPTA an unexpectedly large number for switch interface counters, <code>netq check</code> and <code>netq show</code> commands might fail with the following message:<pre>local variable ‘url’ referenced before assignment</pre> | 4.4.0-4.4.1 | 4.5.0-4.15.1|
| 3241664 | When you start the <code>netq-agent</code> service, the WJH service is enabled by default.  However, when you run the <code>netq config show agent wjh</code> command, the output might reflect the WJH service as disabled. | 4.4.0-4.4.1 | 4.5.0-4.15.1|
| 3179145 | The NetQ agent does not collect VLAN information from WJH data. This has been resolved, however when you upgrade to a NetQ version with the fix, historical WJH data will not be displayed in the UI. | 4.3.0-4.4.1 | 4.5.0-4.15.1|
| 3015875 | NetQ trace might report incomplete route information when there are multiple default routes in a VRF in the path between the source and destination. | 4.1.0-4.4.1 | 4.5.0-4.15.1|

### Fixed Issues in 4.4.0
|  Issue ID 	|   Description	|   Affects	|
|---	        |---	        |---	    |
| 3254224 | In a What Just Happened table, column titles might appear as long strings of text. To fix this issue, select the ‘reset columns’ icon at the upper-right corner of the application.  |  | |
| 3244553 | The What Just Happened (WJH) feature does not work with the NetQ agent on SONiC switches. |  | |
| 3226405 | TLS versions 1.0 and 1.1 are enabled for the OPTA API Gateway listening on TCP port 32708. Only TLS versions 1.2 and 1.3 should be enabled. | 4.3.0 | |
| 3216161 | In an OPTA clustered environment, NetQ agents might appear as rotten after upgrading to NetQ 4.3.0. To work around this issue, configure the <code>spice: false</code> parameter in <code>/etc/netq/netq.yml</code>. | 4.3.0 | |
| 3211317 | Upgrading Cumulus Linux with NetQ LCM fails when you upgrade a switch with the MLAG primary role. | 4.3.0 | |
| 3205778 | In some high scale environments, NetQ agents might appear as rotten during high load. | 4.3.0 | |
| 3203960 | When you add an LDAP user, the operation will fail and return an error: <code>Parameter error</code>. This has been resolved in NetQ 4.4.0 and later. If you configured LDAP authentication prior to NetQ 4.4.0, you must reconfigure LDAP after upgrading. |  | |
| 3157803 | The <code>netq show</code> commands to view MACs, IP addresses, neighbors, and routes might show a higher value compared to the corresponding entries in the NetQ UI. The <code>netq show</code> commands display additional values from the NetQ server or OPTA in addition to monitored devices in the NetQ inventory. | 4.2.0-4.3.0 | |
| 3141723 | When you edit a TCA rule, an error will prevent the rule from updating. To work around this problem, delete the existing rule and create a new one. |  | |
| 3140425 | LCM NetQ install or upgrade will silently fail if a target switch's hostname is still set to the default (<code>cumulus</code> for Cumulus Linux or <code>sonic} for SONiC). |  | |
| 3131311, 3234182 | Sensor validation checks might still reflect a failure in NetQ after the sensor failure has recovered. | 4.2.0-4.3.0 | |
| 3085064, 2838027, 2551494 | When you attempt to install NetQ on a device using LCM and configure the incorrect VRF, the installation will be reflected as successful but the switch will not be present in the inventory in the LCM UI. | 4.1.0-4.3.0 | |
| 3053143 | The MLAG Session card might not show all MLAG events. | 4.2.0-4.3.0 | |
| 2605545 | Sort functionality is disabled when the number of records exceeds 10,000 entries in a full-screen, tabular view.  | 4.3.0 | |

