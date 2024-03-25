---
title: NVIDIA NetQ 4.4 Release Notes
author: Cumulus Networks
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
| <a name="3739222"></a> [3739222](#3739222) <a name="3739222"></a> <br /> | The <code>opta-check</code> command does not properly validate if the required 16 CPU cores are present on the system for NetQ. The command only presents an error if there are fewer than 8 CPU cores detected. | 4.2.0-4.8.0 | 4.9.0|
| <a name="3442456"></a> [3442456](#3442456) <a name="3442456"></a> <br /> | When an event notification is resolved or acknowledged, the NetQ UI might display a duplicate event with the original notification content and timestamp. | 4.2.0-4.6.0 | 4.7.0-4.9.0|
| <a name="3438973"></a> [3438973](#3438973) <a name="3438973"></a> <br /> | When you install NetQ onto your VM, the installation fails with the following messages:<pre>05:57:33.023618: master-node-installer: Installed Debian ...	&#91; FAILED &#93;--------------------------------------ERROR: Failed to install the master node</pre>This is due to an expired key in the installation tarball. For assistance working around this issue, contact NVIDIA support. | 4.3.0-4.5.0 | 4.6.0-4.9.0|
| <a name="3395385"></a> [3395385](#3395385) <a name="3395385"></a> <br /> | When you use NetQ LCM to upgrade a Cumulus Linux switch in an MLAG pair, the upgrade might fail. | 4.4.1-4.5.0 | 4.6.0-4.9.0|
| <a name="3360627"></a> [3360627](#3360627) <a name="3360627"></a> <br /> | When the switch RoCE egress pool buffer limit is configured as unlimited, the maximum buffer usage for RoCE counters might display incorrect values in the NetQ UI. | 4.4.1-4.5.0 | 4.6.0-4.9.0|
| <a name="3305144"></a> [3305144](#3305144) <a name="3305144"></a> <br /> | When you perform a <code>netq trace</code> between two hosts, the following message might be printed in the output even when the trace is successful:<pre>argument of type ‘NoneType’ is not iterable</pre> | 4.4.0-4.4.1 | 4.5.0-4.9.0|
| <a name="3303284"></a> [3303284](#3303284) <a name="3303284"></a> <br /> | When you run the  <code>netq show opta-health</code> command, it might fail and produce the following error:<pre>ERROR: Expecting value: line 1 column 1 (char 0)</pre> | 4.3.0-4.4.1 | 4.5.0-4.9.0|
| <a name="3290068"></a> [3290068](#3290068) <a name="3290068"></a> <br /> | When you back up NetQ data with the <code>backuprestore.sh</code> script, the operation fails with the following log messages:<pre>Failed to clear all earlier snapshot for keyspace:master. Exiting!command terminated with exit code 1Failed to execute /opt/backuprestore/createbackup.sh script on cassandra pod<br />Failed to proceed ahead with backup procedure. Exiting !</pre>Contact NVIDIA support for assistance performing a backup. | 4.4.0-4.4.1 | 4.5.0-4.9.0|
| <a name="3266922"></a> [3266922](#3266922) <a name="3266922"></a> <br /> | When a NetQ agent sends your NetQ server or OPTA an unexpectedly large number for switch interface counters, <code>netq check</code> and <code>netq show</code> commands might fail with the following message:<pre>local variable ‘url’ referenced before assignment</pre> | 4.4.0-4.4.1 | 4.5.0-4.9.0|
| <a name="3241664"></a> [3241664](#3241664) <a name="3241664"></a> <br /> | When you start the <code>netq-agent</code> service, the WJH service is enabled by default.  However, when you run the <code>netq config show agent wjh</code> command, the output might reflect the WJH service as disabled. | 4.4.0-4.4.1 | 4.5.0-4.9.0|
| <a name="3179145"></a> [3179145](#3179145) <a name="3179145"></a> <br /> | The NetQ agent does not collect VLAN information from WJH data. This has been resolved, however when you upgrade to a NetQ version with the fix, historical WJH data will not be displayed in the UI. | 4.3.0-4.4.1 | 4.5.0-4.9.0|
| <a name="3015875"></a> [3015875](#3015875) <a name="3015875"></a> <br /> | NetQ trace might report incomplete route information when there are multiple default routes in a VRF in the path between the source and destination. | 4.1.0-4.4.1 | 4.5.0-4.9.0|

### Fixed Issues in 4.4.1
|  Issue ID 	|   Description	|   Affects	|
|---	        |---	        |---	    |

## 4.4.0 Release Notes
### Open Issues in 4.4.0

|  Issue ID 	|   Description	|   Affects	|   Fixed |
|---	        |---	        |---	    |---	                |
| <a name="3739222"></a> [3739222](#3739222) <a name="3739222"></a> <br /> | The <code>opta-check</code> command does not properly validate if the required 16 CPU cores are present on the system for NetQ. The command only presents an error if there are fewer than 8 CPU cores detected. | 4.2.0-4.8.0 | 4.9.0|
| <a name="3442456"></a> [3442456](#3442456) <a name="3442456"></a> <br /> | When an event notification is resolved or acknowledged, the NetQ UI might display a duplicate event with the original notification content and timestamp. | 4.2.0-4.6.0 | 4.7.0-4.9.0|
| <a name="3438973"></a> [3438973](#3438973) <a name="3438973"></a> <br /> | When you install NetQ onto your VM, the installation fails with the following messages:<pre>05:57:33.023618: master-node-installer: Installed Debian ...	&#91; FAILED &#93;--------------------------------------ERROR: Failed to install the master node</pre>This is due to an expired key in the installation tarball. For assistance working around this issue, contact NVIDIA support. | 4.3.0-4.5.0 | 4.6.0-4.9.0|
| <a name="3305144"></a> [3305144](#3305144) <a name="3305144"></a> <br /> | When you perform a <code>netq trace</code> between two hosts, the following message might be printed in the output even when the trace is successful:<pre>argument of type ‘NoneType’ is not iterable</pre> | 4.4.0-4.4.1 | 4.5.0-4.9.0|
| <a name="3303284"></a> [3303284](#3303284) <a name="3303284"></a> <br /> | When you run the  <code>netq show opta-health</code> command, it might fail and produce the following error:<pre>ERROR: Expecting value: line 1 column 1 (char 0)</pre> | 4.3.0-4.4.1 | 4.5.0-4.9.0|
| <a name="3290068"></a> [3290068](#3290068) <a name="3290068"></a> <br /> | When you back up NetQ data with the <code>backuprestore.sh</code> script, the operation fails with the following log messages:<pre>Failed to clear all earlier snapshot for keyspace:master. Exiting!command terminated with exit code 1Failed to execute /opt/backuprestore/createbackup.sh script on cassandra pod<br />Failed to proceed ahead with backup procedure. Exiting !</pre>Contact NVIDIA support for assistance performing a backup. | 4.4.0-4.4.1 | 4.5.0-4.9.0|
| <a name="3266922"></a> [3266922](#3266922) <a name="3266922"></a> <br /> | When a NetQ agent sends your NetQ server or OPTA an unexpectedly large number for switch interface counters, <code>netq check</code> and <code>netq show</code> commands might fail with the following message:<pre>local variable ‘url’ referenced before assignment</pre> | 4.4.0-4.4.1 | 4.5.0-4.9.0|
| <a name="3241664"></a> [3241664](#3241664) <a name="3241664"></a> <br /> | When you start the <code>netq-agent</code> service, the WJH service is enabled by default.  However, when you run the <code>netq config show agent wjh</code> command, the output might reflect the WJH service as disabled. | 4.4.0-4.4.1 | 4.5.0-4.9.0|
| <a name="3179145"></a> [3179145](#3179145) <a name="3179145"></a> <br /> | The NetQ agent does not collect VLAN information from WJH data. This has been resolved, however when you upgrade to a NetQ version with the fix, historical WJH data will not be displayed in the UI. | 4.3.0-4.4.1 | 4.5.0-4.9.0|
| <a name="3015875"></a> [3015875](#3015875) <a name="3015875"></a> <br /> | NetQ trace might report incomplete route information when there are multiple default routes in a VRF in the path between the source and destination. | 4.1.0-4.4.1 | 4.5.0-4.9.0|

### Fixed Issues in 4.4.0
|  Issue ID 	|   Description	|   Affects	|
|---	        |---	        |---	    |
| <a name="3254224"></a> [3254224](#3254224) <a name="3254224"></a> <br /> | In a What Just Happened table, column titles might appear as long strings of text. To fix this issue, select the ‘reset columns’ icon at the upper-right corner of the application.  |  | |
| <a name="3244553"></a> [3244553](#3244553) <a name="3244553"></a> <br /> | The What Just Happened (WJH) feature does not work with the NetQ agent on SONiC switches. |  | |
| <a name="3226405"></a> [3226405](#3226405) <a name="3226405"></a> <br /> | TLS versions 1.0 and 1.1 are enabled for the OPTA API Gateway listening on TCP port 32708. Only TLS versions 1.2 and 1.3 should be enabled. | 4.3.0 | |
| <a name="3216161"></a> [3216161](#3216161) <a name="3216161"></a> <br /> | In an OPTA clustered environment, NetQ agents might appear as rotten after upgrading to NetQ 4.3.0. To work around this issue, configure the <code>spice: false</code> parameter in <code>/etc/netq/netq.yml</code>. | 4.3.0 | |
| <a name="3211317"></a> [3211317](#3211317) <a name="3211317"></a> <br /> | Upgrading Cumulus Linux with NetQ LCM fails when you upgrade a switch with the MLAG primary role. | 4.3.0 | |
| <a name="3205778"></a> [3205778](#3205778) <a name="3205778"></a> <br /> | In some high scale environments, NetQ agents might appear as rotten during high load. | 4.3.0 | |
| <a name="3203960"></a> [3203960](#3203960) <a name="3203960"></a> <br /> | When you add an LDAP user, the operation will fail and return an error: <code>Parameter error</code>. This has been resolved in NetQ 4.4.0 and later. If you configured LDAP authentication prior to NetQ 4.4.0, you must reconfigure LDAP after upgrading. |  | |
| <a name="3157803"></a> [3157803](#3157803) <a name="3157803"></a> <br /> | The <code>netq show</code> commands to view MACs, IP addresses, neighbors, and routes might show a higher value compared to the corresponding entries in the NetQ UI. The <code>netq show</code> commands display additional values from the NetQ server or OPTA in addition to monitored devices in the NetQ inventory. | 4.2.0-4.3.0 | |
| <a name="3141723"></a> [3141723](#3141723) <a name="3141723"></a> <br /> | When you edit a TCA rule, an error will prevent the rule from updating. To work around this problem, delete the existing rule and create a new one. |  | |
| <a name="3140425"></a> [3140425](#3140425) <a name="3140425"></a> <br /> | LCM NetQ install or upgrade will silently fail if a target switch's hostname is still set to the default (<code>cumulus</code> for Cumulus Linux or <code>sonic} for SONiC). |  | |
| <a name="3131311"></a> [3131311](#3131311) <a name="3131311"></a> <br /> | Sensor validation checks might still reflect a failure in NetQ after the sensor failure has recovered. | 4.2.0-4.3.0 | |
| <a name="3085064"></a> [3085064](#3085064) <a name="3085064"></a> <br /> | When you attempt to install NetQ on a device using LCM and configure the incorrect VRF, the installation will be reflected as successful but the switch will not be present in the inventory in the LCM UI. | 4.1.0-4.3.0 | |
| <a name="3053143"></a> [3053143](#3053143) <a name="3053143"></a> <br /> | The MLAG Session card might not show all MLAG events. | 4.2.0-4.3.0 | |
| <a name="2605545"></a> [2605545](#2605545) <a name="2605545"></a> <br /> | Sort functionality is disabled when the number of records exceeds 10,000 entries in a full-screen, tabular view.  | 4.3.0 | |

