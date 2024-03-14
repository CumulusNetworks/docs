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
| <a name="3819364"></a> [3819364](#3819364) <a name="3819364"></a> <br /> | When you attempt to delete a scheduled trace using the NetQ UI, the trace record is not deleted. | 4.7.0-4.8.0 | |
| <a name="3782784"></a> [3782784](#3782784) <a name="3782784"></a> <br /> | After performing a new NetQ cluster installation, some MLAG and EVPN NetQ validations might incorrectly report errors. To work around this issue, run the <code>netq check mlag legacy</code> and <code>netq check evpn legacy</code> commands instead of running a default streaming check.  | 4.8.0 | |
| <a name="3781503"></a> [3781503](#3781503) <a name="3781503"></a> <br /> | When you upgrade a Cumulus Linux switch running the nslcd service with NetQ LCM, the <code>nslcd</code> service fails to start after the upgrade. To work around this issue, manually back up your <code>nslcd</code> configuration and restore it after the upgrade. | 4.8.0 | |
| <a name="3761602"></a> [3761602](#3761602) <a name="3761602"></a> <br /> |  NetQ does not display queue histogram data for switches running Cumulus Linux 5.8.0 and NetQ agent version 4.8.0. To work around this issue, upgrade the NetQ agent package to 4.9.0. | 4.8.0 | |
| <a name="3739222"></a> [3739222](#3739222) <a name="3739222"></a> <br /> | The <code>opta-check</code> command does not properly validate if the required 16 CPU cores are present on the system for NetQ. The command only presents an error if there are fewer than 8 CPU cores detected. | 4.2.0-4.8.0 | |
| <a name="3738840"></a> [3738840](#3738840) <a name="3738840"></a> <br /> | When you upgrade a Cumulus Linux switch configured for TACACS authentication using NetQ LCM, the switch's TACACS configuration is not restored after upgrade. | 4.8.0 | |
| <a name="3688985"></a> [3688985](#3688985) <a name="3688985"></a> <br /> | After upgrading a NetQ VM with LDAP authentication configured, adding a new LDAP user to NetQ fails with the error message "LDAP not enabled." | 4.8.0 | |
| <a name="3676723"></a> [3676723](#3676723) <a name="3676723"></a> <br /> | When you use the NetQ agent on a Cumulus Linux switch to export gNMI data and there is a period of inactivity in the gNMI stream, the NetQ agent service might stop. To recover from this issue, restart the service with the <code>netq config restart agent</code> command. | 4.7.0-4.8.0 | |
| <a name="3670180"></a> [3670180](#3670180) <a name="3670180"></a> <br /> | The medium Validation Summary card might incorrectly display a failure or lack of data for the latest time interval. To work around this issue, expand the card to the largest view for an accurate representation of validation results. | 4.8.0 | |
| <a name="3656965"></a> [3656965](#3656965) <a name="3656965"></a> <br /> | After you upgrade NetQ and try to decommission a switch, the decommission might fail with the message "Timeout encountered while processing." | 4.8.0 | |
| <a name="3650422"></a> [3650422](#3650422) <a name="3650422"></a> <br /> | The OPTA-on-switch service does not send agent data when the NetQ CLI is not configured. To work around this issue, configure the NetQ CLI on the switch. | 4.8.0 | |
| <a name="3644644"></a> [3644644](#3644644) <a name="3644644"></a> <br /> | When you perform an LCM upgrade of Cumulus Linux on a switch using the <code>netq lcm upgrade cl-image</code> CLI command, an error message of <code>NetQ cloud token invalid</code> is displayed though the upgrade completes successfully. This issue is not encountered when using the NetQ LCM UI to perform the upgrade. | 4.8.0 | |
| <a name="3634648"></a> [3634648](#3634648) <a name="3634648"></a> <br /> | The topology graph might show unexpected connections when devices in the topology do not have LLDP adjacencies. | 4.8.0 | |
| <a name="3633458"></a> [3633458](#3633458) <a name="3633458"></a> <br /> | The legacy topology diagram might categorize devices into tiers incorrectly. To work around this issue, use the updated topology diagram by selecting Topology Beta in the latest version of the NetQ UI. | 4.7.0-4.8.0 | |
| <a name="3632378"></a> [3632378](#3632378) <a name="3632378"></a> <br /> | After you upgrade your on-premises NetQ VM from version 4.7.0 to 4.8.0, NIC telemetry using the Prometheus adapter is not collected. To work around this issue, run the following commands on your NetQ VM:<pre>sudo kubectl set image deployment/netq-prom-adapter netq-prom-adapter=docker-registry:5000/netq-prom-adapter:4.8.0<br>sudo kubectl set image deployment/netq-prom-adapter prometheus=docker-registry:5000/prometheus-v2.41.0:4.8.0</pre> | 4.8.0 | |
| <a name="3613811"></a> [3613811](#3613811) <a name="3613811"></a> <br /> | LCM operations using in-band management are unsupported on switches that use eth0 connected to an out-of-band network. To work around this issue, configure NetQ to use out-of-band management in the <code>mgmt</code> VRF on Cumulus Linux switches when interface eth0 is in use. | 4.8.0 | |
| <a name="3549877"></a> [3549877](#3549877) <a name="3549877"></a> <br /> | NetQ cloud deployments might unexpectedly display validation results for checks that did not run on any nodes. | 4.6.0-4.8.0 | |
| <a name="3429528"></a> [3429528](#3429528) <a name="3429528"></a> <br /> | EVPN and RoCE validation cards in the NetQ UI might not display data when Cumulus Linux switches are configured with high VNI scale. | 4.6.0-4.8.0 | |
| <a name="2885312"></a> [2885312](#2885312) <a name="2885312"></a> <br /> | EVPN Validation Type 2 checks might show false Duplicate MAC events for MAC addresses that are not duplicated. An example of this is shown below:<br />  <pre>EVPN Type 2 Test details:<br />  Hostname          Peer Name         Peer Hostname     Reason                                        Last Changed<br />  ----------------- ----------------- ----------------- --------------------------------------------- -------------------------<br />  torc-11           -                 -                 Duplicate Mac 00:02:00:00:00:55 VLAN 1249 at  Sun Dec  5 18:26:14 2021<br />                                                        torc-21:vx-282 and torc-11:peerlink-3<br />  </pre> | 4.1.0-4.8.0 | |

### Fixed Issues in 4.8.0
|  Issue ID 	|   Description	|   Affects	|
|---	        |---	        |---	    |
| <a name="3575935"></a> [3575935](#3575935) <a name="3575935"></a> <br /> | When you upgrade to NetQ 4.7.0, configured premises names might get reset to the default name <code>OPID0</code>. | 4.7.0 | |
| <a name="3575934"></a> [3575934](#3575934) <a name="3575934"></a> <br /> | When you upgrade to NetQ 4.7.0, the password for the <code>admin</code> user is reset to the default password. | 4.7.0 | |
| <a name="3555031"></a> [3555031](#3555031) <a name="3555031"></a> <br /> | NetQ incorrectly reports a low health SSD event on SN5600 switches. To work around this issue, configure an event suppression rule for <code>ssdutil</code> messages from SN5600 switches in your network. | 4.7.0 | |
| <a name="3530739"></a> [3530739](#3530739) <a name="3530739"></a> <br /> | Queue histogram data received from switches might encounter a delay before appearing in the NetQ UI. | 4.7.0 | |

