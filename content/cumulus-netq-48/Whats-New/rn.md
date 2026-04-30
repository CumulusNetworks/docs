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
| 4466349 | When you upgrade an HA cluster deployment from a version that is not part of the supported upgrade path, the upgrade might fail and the UI might not load due to expired control plane certificates on the worker nodes.<br><br>To check whether the certificates have expired, run <code>sudo su</code> followed by <code>kubeadm certs check-expiration</code>. If the output displays a date in the past, your certificates are expired. To update the certificates, run <code>kubeadm certs renew all</code> on each worker node in the cluster. Next, restart the <a href="https://kubernetes.io/docs/concepts/overview/components/#control-plane-components/">control plane components</a> with <code>crictl stop CONTAINER_ID</code>, followed by <code>systemctl restart kubelet</code>. | 4.8.0-4.14.0 | 4.15.0-4.15.1|
| 3819364 | When you attempt to delete a scheduled trace using the NetQ UI, the trace record is not deleted. | 4.7.0-4.9.0 | 4.10.0-4.15.1|
| 3782784 | After performing a new NetQ cluster installation, some MLAG and EVPN NetQ validations might incorrectly report errors. To work around this issue, run the <code>netq check mlag legacy</code> and <code>netq check evpn legacy</code> commands instead of running a default streaming check.  | 4.8.0 | 4.9.0-4.15.1|
| 3781503, 3775625 | When you upgrade a Cumulus Linux switch running the nslcd service with NetQ LCM, the <code>nslcd</code> service fails to start after the upgrade. To work around this issue, manually back up your <code>nslcd</code> configuration and restore it after the upgrade. | 4.8.0 | 4.9.0-4.15.1|
| 3761602 |  NetQ does not display queue histogram data for switches running Cumulus Linux 5.8.0 and NetQ agent version 4.8.0. To work around this issue, upgrade the NetQ agent package to 4.9.0. | 4.8.0 | 4.9.0-4.15.1|
| 3739222 | The <code>opta-check</code> command does not properly validate if the required 16 CPU cores are present on the system for NetQ. The command only presents an error if there are fewer than 8 CPU cores detected. | 4.2.0-4.8.0 | 4.9.0-4.15.1|
| 3738840 | When you upgrade a Cumulus Linux switch configured for TACACS authentication using NetQ LCM, the switch's TACACS configuration is not restored after upgrade. | 4.8.0-4.9.0 | 4.10.0-4.15.1|
| 3688985 | After upgrading a NetQ VM with LDAP authentication configured, adding a new LDAP user to NetQ fails with the error message "LDAP not enabled." | 4.8.0 | 4.9.0-4.15.1|
| 3676723 | When you use the NetQ agent on a Cumulus Linux switch to export gNMI data and there is a period of inactivity in the gNMI stream, the NetQ agent service might stop. To recover from this issue, restart the service with the <code>netq config restart agent</code> command. | 4.7.0-4.8.0 | 4.9.0-4.15.1|
| 3670180 | The medium Validation Summary card might incorrectly display a failure or lack of data for the latest time interval. To work around this issue, expand the card to the largest view for an accurate representation of validation results. | 4.8.0 | 4.9.0-4.15.1|
| 3650422 | The OPTA-on-switch service does not send agent data when the NetQ CLI is not configured. To work around this issue, configure the NetQ CLI on the switch. | 4.8.0 | 4.9.0-4.15.1|
| 3644644 | When you perform an LCM upgrade of Cumulus Linux on a switch using the <code>netq lcm upgrade cl-image</code> CLI command, an error message of <code>NetQ cloud token invalid</code> is displayed though the upgrade completes successfully. This issue is not encountered when using the NetQ LCM UI to perform the upgrade. | 4.8.0 | 4.9.0-4.15.1|
| 3634648 | The topology graph might show unexpected connections when devices in the topology do not have LLDP adjacencies. | 4.8.0 | 4.9.0-4.15.1|
| 3632378 | After you upgrade your on-premises NetQ VM from version 4.7.0 to 4.8.0, NIC telemetry using the Prometheus adapter is not collected. To work around this issue, run the following commands on your NetQ VM:<pre>sudo kubectl set image deployment/netq-prom-adapter netq-prom-adapter=docker-registry:5000/netq-prom-adapter:4.8.0<br>sudo kubectl set image deployment/netq-prom-adapter prometheus=docker-registry:5000/prometheus-v2.41.0:4.8.0</pre> | 4.8.0 | 4.9.0-4.15.1|
| 3613811 | LCM operations using in-band management are unsupported on switches that use eth0 connected to an out-of-band network. To work around this issue, configure NetQ to use out-of-band management in the <code>mgmt</code> VRF on Cumulus Linux switches when interface eth0 is in use. | 4.8.0-4.15.1 | |
| 3549877 | NetQ cloud deployments might unexpectedly display validation results for checks that did not run on any nodes. | 4.6.0-4.8.0 | 4.9.0-4.15.1|
| 3429528, 3588417 | EVPN and RoCE validation cards in the NetQ UI might not display data when Cumulus Linux switches are configured with high VNI scale. | 4.6.0-4.8.0 | 4.9.0-4.15.1|

### Fixed Issues in 4.8.0
|  Issue ID 	|   Description	|   Affects	|
|---	        |---	        |---	    |
| 3575935 | When you upgrade to NetQ 4.7.0, configured premises names might get reset to the default name <code>OPID0</code>. | 4.7.0 | |
| 3575934 | When you upgrade to NetQ 4.7.0, the password for the <code>admin</code> user is reset to the default password. | 4.7.0 | |
| 3555031 | NetQ incorrectly reports a low health SSD event on SN5600 switches. To work around this issue, configure an event suppression rule for <code>ssdutil</code> messages from SN5600 switches in your network. | 4.7.0 | |
| 3530739 | Queue histogram data received from switches might encounter a delay before appearing in the NetQ UI. | 4.7.0 | |

