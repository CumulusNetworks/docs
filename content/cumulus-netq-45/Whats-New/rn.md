---
title: NVIDIA NetQ 4.5 Release Notes
author: Cumulus Networks
weight: 30
product: Cumulus NetQ
version: "4.5"
toc: 1
type: rn
pdfhidden: True
---
{{<rn_xls_link dir="cumulus-netq-45" >}}
## 4.5.0 Release Notes
### Open Issues in 4.5.0

|  Issue ID 	|   Description	|   Affects	|   Fixed |
|---	        |---	        |---	    |---	                |
| <a name="3362224"></a> [3362224](#3362224) <a name="3362224"></a> <br /> | When you configure a new access profile with SSH authentication using the CLI, the command fails with the following log message:<pre>Expecting value: line 1 column 1 (char 0) </pre>To work around this issue, use the NetQ UI to configure the access profile. | 4.5.0 | |
| <a name="3226405"></a> [3226405](#3226405) <a name="3226405"></a> <br /> | TLS versions 1.0 and 1.1 are enabled for the OPTA API Gateway listening on TCP port 32708. Only TLS versions 1.2 and 1.3 should be enabled. | 4.3.0-4.5.0 | |
| <a name="3216161"></a> [3216161](#3216161) <a name="3216161"></a> <br /> | In an OPTA clustered environment, NetQ agents might appear as rotten after upgrading to NetQ 4.3.0. To work around this issue, configure the <code>spice: false</code> parameter in <code>/etc/netq/netq.yml</code>. | 4.3.0-4.5.0 | |
| <a name="3211317"></a> [3211317](#3211317) <a name="3211317"></a> <br /> | Upgrading Cumulus Linux with NetQ LCM fails when you upgrade a switch with the MLAG primary role. | 4.3.0-4.5.0 | |
| <a name="3205778"></a> [3205778](#3205778) <a name="3205778"></a> <br /> | In some high scale environments, NetQ agents might appear as rotten during high load. | 4.3.0-4.5.0 | |
| <a name="3157803"></a> [3157803](#3157803) <a name="3157803"></a> <br /> | The <code>netq show</code> commands to view MACs, IP addresses, neighbors, and routes might show a higher value compared to the corresponding entries in the NetQ UI. The <code>netq show</code> commands display additional values from the NetQ server or OPTA in addition to monitored devices in the NetQ inventory. | 4.2.0-4.5.0 | |
| <a name="3131311"></a> [3131311](#3131311) <a name="3131311"></a> <br /> | Sensor validation checks might still reflect a failure in NetQ after the sensor failure has recovered. | 4.2.0-4.5.0 | |
| <a name="3085064"></a> [3085064](#3085064) <a name="3085064"></a> <br /> | When you attempt to install NetQ on a device using LCM and configure the incorrect VRF, the installation will be reflected as successful but the switch will not be present in the inventory in the LCM UI. | 4.1.0-4.5.0 | |
| <a name="3053143"></a> [3053143](#3053143) <a name="3053143"></a> <br /> | The MLAG Session card might not show all MLAG events. | 4.2.0-4.5.0 | |
| <a name="2885312"></a> [2885312](#2885312) <a name="2885312"></a> <br /> | EVPN Validation Type 2 checks might show false Duplicate MAC events for MAC addresses that are not duplicated. An example of this is shown below:<br />  <pre>EVPN Type 2 Test details:<br />  Hostname          Peer Name         Peer Hostname     Reason                                        Last Changed<br />  ----------------- ----------------- ----------------- --------------------------------------------- -------------------------<br />  torc-11           -                 -                 Duplicate Mac 00:02:00:00:00:55 VLAN 1249 at  Sun Dec  5 18:26:14 2021<br />                                                        torc-21:vx-282 and torc-11:peerlink-3<br />  </pre> | 4.1.0-4.5.0 | |
| <a name="2872288"></a> [2872288](#2872288) <a name="2872288"></a> <br /> | When a NetQ agent sends messages with validation check data, there might be a delay of up to 120 seconds before the new data is displayed in streaming validation checks. | 4.2.0-4.5.0 | |
| <a name="2605545"></a> [2605545](#2605545) <a name="2605545"></a> <br /> | Sort functionality is disabled when the number of records exceeds 10,000 entries in a full-screen, tabular view.  | 4.3.0-4.5.0 | |

### Fixed Issues in 4.5.0
|  Issue ID 	|   Description	|   Affects	|
|---	        |---	        |---	    |
| <a name="3305144"></a> [3305144](#3305144) <a name="3305144"></a> <br /> | When you perform a <code>netq trace</code> between two hosts, the following message might be printed in the output even when the trace is successful:<pre>argument of type ‘NoneType’ is not iterable</pre> |  | |
| <a name="3303284"></a> [3303284](#3303284) <a name="3303284"></a> <br /> | When you run the  <code>netq show opta-health</code> command, it might fail and produce the following error:<pre>ERROR: Expecting value: line 1 column 1 (char 0)</pre> | 4.3.0-4.4.0 | |
| <a name="3290068"></a> [3290068](#3290068) <a name="3290068"></a> <br /> | When you back up NetQ data with the <code>backuprestore.sh</code> script, the operation fails with the following log messages:<pre>Failed to clear all earlier snapshot for keyspace:master. Exiting!command terminated with exit code 1Failed to execute /opt/backuprestore/createbackup.sh script on cassandra pod<br />Failed to proceed ahead with backup procedure. Exiting !</pre>Contact NVIDIA support for assistance performing a backup. |  | |
| <a name="3266922"></a> [3266922](#3266922) <a name="3266922"></a> <br /> | When a NetQ agent sends your NetQ server or OPTA an unexpectedly large number for switch interface counters, <code>netq check</code> and <code>netq show</code> commands might fail with the following message:<pre>local variable ‘url’ referenced before assignment</pre> |  | |
| <a name="3241664"></a> [3241664](#3241664) <a name="3241664"></a> <br /> | When you start the <code>netq-agent</code> service, the WJH service is enabled by default.  However, when you run the <code>netq config show agent wjh</code> command, the output might reflect the WJH service as disabled. |  | |
| <a name="3231404"></a> [3231404](#3231404) <a name="3231404"></a> <br /> | When you attempt to reinstall NetQ on a server with an existing NetQ installation using the <code>netq install &#91;opta&#93;</code> command, the installation fails with the following messages:<pre>master-node-installer: Plugged in release bundle ...    &#91; FAILED &#93;--------------------------------------ERROR: Failed to install the master nodeCommand '&#91;'/usr/bin/dpkg', '-i', ''&#93;' returned non-zero exit status 2<br /></pre>To work around this issue, run the <code>netq bootstrap reset</code> command before attempting to reinstall NetQ on your existing server. |  | |
| <a name="3179145"></a> [3179145](#3179145) <a name="3179145"></a> <br /> | The NetQ agent does not collect VLAN information from WJH data. This has been resolved, however when you upgrade to a NetQ version with the fix, historical WJH data will not be displayed in the UI. | 4.3.0-4.4.0 | |
| <a name="3015875"></a> [3015875](#3015875) <a name="3015875"></a> <br /> | NetQ trace might report incomplete route information when there are multiple default routes in a VRF in the path between the source and destination. | 4.1.0-4.4.0 | |

