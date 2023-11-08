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
| <a name="3649630"></a> [3649630](#3649630) <a name="3649630"></a> <br /> | LCM discovery might fail in a NetQ on-premises cluster deployment with the message <code>Error: Connection failure: ('The read operation timed out',)</code>. To validate this issue is occurring, run the <code>sudo kubectl get pods -o wide \| grep lcm-executor</code> command and confirm the lcm-executor pod is deployed on a worker node instead of the expected master node. To work around this issue: <br>1. Retrieve your worker node names:<pre>$ sudo kubectl get nodesNAME               STATUS   ROLES                  AGE   VERSIONmaster1  Ready    control-plane,master   18d   v1.27.2worker1  Ready    <none>    18d   v1.27.2worker2  Ready    <none>    18d   v1.27.2</pre>2. Disable pod scheduling on the worker nodes with the <code>sudo kubectl cordon <worker1-name> <worker2-name></code> command.<br><br>3. Verify pod scheduling is disabled on the worker nodes:<pre>NAME               STATUS   ROLES                  AGE   VERSIONmaster1  Ready    control-plane,master   18d   v1.27.2worker1  Ready,SchedulingDisabled    <none>    18d   v1.27.2worker2  Ready,SchedulingDisabled    <none>    18d   v1.27.2</pre>4. Delete the lcm-executor pod with the <code>delete pod netq-lcm-executor-deploy-<name></code> command, retrieving the full lcm-executor pod name from the output of <code>sudo kubectl get pods -o wide \| grep lcm-executor</code><br /><br>5. Verify the lcm-executor pod is now scheduled on the master node with the <code>sudo kubectl get pods -o wide \| grep lcm-executor</code> command<br /><br>6. Reenable scheduling on worker nodes with the <code>sudo kubectl cordon <worker1-name> <worker2-name></code> command<br /><br>7. Run your LCM discovery again. | 4.7.0-4.8.0 | |
| <a name="3644644"></a> [3644644](#3644644) <a name="3644644"></a> <br /> | When you perform an LCM upgrade of Cumulus Linux on a switch using the <code>netq lcm upgrade cl-image</code> CLI command, an error message of <code>NetQ cloud token invalid</code> is displayed though the upgrade completes successfully. This issue is not encountered when using the NetQ LCM UI to perform the upgrade. | 4.8.0 | |
| <a name="3633458"></a> [3633458](#3633458) <a name="3633458"></a> <br /> | The legacy topology diagram might categorize devices into tiers incorrectly. To work around this issue, use the updated topology diagram by selecting Topology Beta in the NetQ 4.8.0 UI. | 4.7.0-4.8.0 | |
| <a name="3632783"></a> [3632783](#3632783) <a name="3632783"></a> <br /> | LCM upgrades of Cumulus Linux fail when using an on-switch OPTA and in-band management. | 4.8.0 | |
| <a name="3632378"></a> [3632378](#3632378) <a name="3632378"></a> <br /> | After you upgrade your on-premises NetQ VM from version 4.7.0 to 4.8.0, NIC telemetry using the Prometheus adapter is not collected. To work around this issue, run the following commands on your NetQ VM:<pre>sudo kubectl set image deployment/netq-prom-adapter netq-prom-adapter=docker-registry:5000/netq-prom-adapter:4.8.0sudo kubectl set image deployment/netq-prom-adapter prometheus=docker-registry:5000/prometheus-v2.41.0:4.8.0</pre> | 4.8.0 | |
| <a name="3613811"></a> [3613811](#3613811) <a name="3613811"></a> <br /> | LCM operations using in-band management are unsupported on switches that use eth0 connected to an out-of-band network. To work around this issue, configure NetQ to use out-of-band management in the <code>mgmt</code> VRF on Cumulus Linux switches when interface eth0 is in use. | 4.8.0 | |
| <a name="3435373"></a> [3435373](#3435373) <a name="3435373"></a> <br /> | If your NetQ on-premises VM is not configured with at least 16 vCPUs, upgrades from NetQ 4.5.0 to 4.6.0 using the <code>netq upgrade bundle</code> command fail with the following message: <pre>Job upgrade failed or timed out<br /></pre>To work around this issue, reconfigure your VM to use 16 vCPUs before upgrading. | 4.5.0-4.8.0 | |
| <a name="3429528"></a> [3429528](#3429528) <a name="3429528"></a> <br /> | EVPN and RoCE validation cards in the NetQ UI might not display data when Cumulus Linux switches are configured with high VNI scale. | 4.6.0-4.8.0 | |
| <a name="2885312"></a> [2885312](#2885312) <a name="2885312"></a> <br /> | EVPN Validation Type 2 checks might show false Duplicate MAC events for MAC addresses that are not duplicated. An example of this is shown below:<br />  <pre>EVPN Type 2 Test details:<br />  Hostname          Peer Name         Peer Hostname     Reason                                        Last Changed<br />  ----------------- ----------------- ----------------- --------------------------------------------- -------------------------<br />  torc-11           -                 -                 Duplicate Mac 00:02:00:00:00:55 VLAN 1249 at  Sun Dec  5 18:26:14 2021<br />                                                        torc-21:vx-282 and torc-11:peerlink-3<br />  </pre> | 4.1.0-4.8.0 | |

### Fixed Issues in 4.8.0
|  Issue ID 	|   Description	|   Affects	|
|---	        |---	        |---	    |
| <a name="3575935"></a> [3575935](#3575935) <a name="3575935"></a> <br /> | When you upgrade to NetQ 4.7.0, configured premises names might get reset to the default name <code>OPID0</code>. | 4.7.0 | |
| <a name="3575934"></a> [3575934](#3575934) <a name="3575934"></a> <br /> | When you upgrade to NetQ 4.7.0, the password for the <code>admin</code> user is reset to the default password. | 4.7.0 | |
| <a name="3555031"></a> [3555031](#3555031) <a name="3555031"></a> <br /> | NetQ incorrectly reports a low health SSD event on SN5600 switches. To work around this issue, configure an event suppression rule for <code>ssdutil</code> messages from SN5600 switches in your network. | 4.7.0 | |
| <a name="3549877"></a> [3549877](#3549877) <a name="3549877"></a> <br /> | NetQ cloud deployments might unexpectedly display validation results for checks that did not run on any nodes. | 4.6.0-4.7.0 | |
| <a name="3530739"></a> [3530739](#3530739) <a name="3530739"></a> <br /> | Queue histogram data received from switches might encounter a delay before appearing in the NetQ UI. | 4.7.0 | |

