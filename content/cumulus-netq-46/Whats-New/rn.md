---
title: NVIDIA NetQ 4.6 Release Notes
author: Cumulus Networks
weight: 30
product: Cumulus NetQ
version: "4.6"
toc: 1
type: rn
pdfhidden: True
---
{{<rn_xls_link dir="cumulus-netq-46" >}}
## 4.6.0 Release Notes
### Open Issues in 4.6.0

|  Issue ID 	|   Description	|   Affects	|   Fixed |
|---	        |---	        |---	    |---	                |
| <a name="3355892"></a> [3355892](#3355892) <a name="3355892"></a> <br /> | When you use NetQ LCM to upgrade a switch from a Cumulus Linux 5 release to a later version and have not saved your NVUE configuration with the <code>nv config save</code> command, the NetQ UI will present the following warning:<br /><pre>There are unsaved changes in the NVUE config file on switch <hostname>. Consider saving the changes before upgrading.<br /></pre> | 4.6.0 | |
| <a name="3429528"></a> [3429528](#3429528) <a name="3429528"></a> <br /> | EVPN and RoCE validation cards in the NetQ UI might not display data when Cumulus Linux switches are configured with high VNI scale.  | 4.6.0 | |
| <a name="3435373"></a> [3435373](#3435373) <a name="3435373"></a> <br /> | If your NetQ on-premises VM is not configured with at least 16 vCPUs, upgrades from NetQ 4.5.0 to 4.6.0 using the <code>netq upgrade bundle</code> command fail with the following message: <pre>Job upgrade failed or timed out<br /></pre>To work around this issue, reconfigure your VM to use 16 vCPUs before upgrading. | 4.5.0-4.6.0 | |
| <a name="3436299"></a> [3436299](#3436299) <a name="3436299"></a> <br /> | RoCE validations might not display data in the NetQ UI and CLI for Cumulus Linux switches when the NVUE service is not running. This issue will resolve itself within 24 hours after the next full status update from the NetQ agent.  | 4.6.0 | |
| <a name="2885312"></a> [2885312](#2885312) <a name="2885312"></a> <br /> | EVPN Validation Type 2 checks might show false Duplicate MAC events for MAC addresses that are not duplicated. An example of this is shown below:<br />  <pre>EVPN Type 2 Test details:<br />  Hostname          Peer Name         Peer Hostname     Reason                                        Last Changed<br />  ----------------- ----------------- ----------------- --------------------------------------------- -------------------------<br />  torc-11           -                 -                 Duplicate Mac 00:02:00:00:00:55 VLAN 1249 at  Sun Dec  5 18:26:14 2021<br />                                                        torc-21:vx-282 and torc-11:peerlink-3<br />  </pre> | 4.1.0-4.6.0 | |

### Fixed Issues in 4.6.0
|  Issue ID 	|   Description	|   Affects	|
|---	        |---	        |---	    |
| <a name="3438973"></a> [3438973](#3438973) <a name="3438973"></a> <br /> | When you install NetQ onto your VM, the installation fails with the following messages:<pre>05:57:33.023618: master-node-installer: Installed Debian ...	&#91; FAILED &#93;--------------------------------------ERROR: Failed to install the master node</pre>This is due to an expired key in the installation tarball. For assistance working around this issue, contact NVIDIA support. | 4.3.0-4.5.0 | |
| <a name="3395385"></a> [3395385](#3395385) <a name="3395385"></a> <br /> | When you use NetQ LCM to upgrade a Cumulus Linux switch in an MLAG pair, the upgrade might fail. | 4.4.1-4.5.0 | |
| <a name="3367267"></a> [3367267](#3367267) <a name="3367267"></a> <br /> | When you upgrade a switch with NetQ LCM using the <code>root</code> user, the upgrade fails with the following message: <pre> Destination /home/root does not exist. </pre> To work around this issue, perform the upgrade using a different user account. | 4.5.0 | |
| <a name="3362224"></a> [3362224](#3362224) <a name="3362224"></a> <br /> | When you configure a new access profile with SSH authentication using the CLI, the command fails with the following log message:<pre>Expecting value: line 1 column 1 (char 0) </pre>To work around this issue, use the NetQ UI to configure the access profile. | 4.5.0 | |
| <a name="3360627"></a> [3360627](#3360627) <a name="3360627"></a> <br /> | When the switch RoCE egress pool buffer limit is configured as unlimited, the maximum buffer usage for RoCE counters might display incorrect values in the NetQ UI. | 4.4.1-4.5.0 | |

