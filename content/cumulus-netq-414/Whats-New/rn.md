---
title: NVIDIA NetQ 4.14 Release Notes
author: Cumulus Networks
weight: 30
product: Cumulus NetQ
version: "4.14"
toc: 1
type: rn
pdfhidden: True
---
{{<rn_xls_link dir="cumulus-netq-414" >}}
## 4.14.0 Release Notes
### Open Issues in 4.14.0

|  Issue ID 	|   Description	|   Affects	|   Fixed |
|---	        |---	        |---	    |---	                |
| 4621868 | NetQ might generate event notifications for BGP reset time changes even when no actual changes have occurred. | 4.14.0-4.15.1 | 5.0.0-5.1.0|
| 4612457 | The process monitoring dashboard may display inaccurate CPU utilization values for the NetQ agent. | 4.11.0-4.15.1 | 5.0.0-5.1.0|
| 4537675 | The NetQ UI might not display pagination controls for large tables with multiple entries. | 4.14.0-4.15.1 | 5.0.0-5.1.0|
| 4466349 | When you upgrade an HA cluster deployment from a version that is not part of the supported upgrade path, the upgrade might fail and the UI might not load due to expired control plane certificates on the worker nodes.<br><br>To check whether the certificates have expired, run <code>sudo su</code> followed by <code>kubeadm certs check-expiration</code>. If the output displays a date in the past, your certificates are expired. To update the certificates, run <code>kubeadm certs renew all</code> on each worker node in the cluster. Next, restart the <a href="https://kubernetes.io/docs/concepts/overview/components/#control-plane-components/">control plane components</a> with <code>crictl stop CONTAINER_ID</code>, followed by <code>systemctl restart kubelet</code>. | 4.8.0-4.14.0 | 4.15.0-4.15.1|
| 4402969 | When you upgrade a cluster deployment from NetQ 4.13 to 4.14 using Base Command Manager (BCM), the operation might appear to fail with the error message <code>Warning: Ping to admin app failed. 10.141.0.1 Traceback (most recent call last): File “/usr/bin/netq”, line 404, in <module> rx_reply(sock, sys.argv) File “/usr/bin/netq”, line 126, in rx_reply rx_data = sock.recv(4096) BlockingIOError: &#91;Errno 11&#93; Resource temporarily unavailable</code>. You can ignore this message and wait for the upgrade to complete. To verify the actual NetQ version and upgrade status, run the <code>netq show status</code> command<br /> | 4.14.0 | 4.15.0-4.15.1|
| 4310939 | When a switch becomes rotten or is connected to a different NetQ server without decommissioning it first, the link health view dashboard displays outdated counter values. To work around this issue, wait for NetQ to update and display accurate counter values. | 4.13.0-4.14.0 | 4.15.0-4.15.1|
| 4309191, 4309888, 4343075, 4351684, 4411619, 4291885, 4493616 | In cloud deployments, lifecycle management operations such as device discovery or switch decommissioning might time out and ultimately fail. To work around this issue, restart the LCM executor on the OPTA VM with <code>lcm_pod='kubectl get pod \| grep -m1 lcm \| awk ‘{print $1}’'; kubectl delete pod $lcm_pod</code>. | 4.13.0-4.14.0 | 4.15.0-4.15.1|
| 4248942 | When you assign a role to a switch, NetQ might take up to five minutes to reflect the new or updated role in the queue histogram fabric overview page. | 4.13.0-4.14.0 | 4.15.0-4.15.1|
| 4131550 | When you run a topology validation, the full-screen topology validation view might not display the latest results. To work around this issue, refresh the page. | 4.12.0-4.15.1 | |
| 4100882, 4119697 | When you attempt to export a file that is larger than 200MB, your browser might crash or otherwise prevent you from exporting the file. To work around this issue, use filters in the UI to decrease the size of the dataset that you intend to export. | 4.12.0-4.15.1, 5.0.0-5.1.0 | |
| 4023716, 4022819, 4282514 | NetQ might display duplicate validations results. | 4.11.0-4.15.1 | 5.0.0-5.1.0|
| 3993538, 4379389 | When you re-position a card on your workbench and then manually refresh the workbench, NetQ might reposition the cards. | 4.11.0-4.15.1 | 5.0.0-5.1.0|
| 3800434 | When you upgrade NetQ from a version prior to 4.9.0, What Just Happened data that was collected before the upgrade is no longer present. | 4.9.0-4.15.1 | |
| 3772274 | After you upgrade NetQ, data from snapshots taken prior to the NetQ upgrade will contain unreliable data and should not be compared to any snapshots taken after the upgrade. In cluster deployments, snapshots from prior NetQ versions will not be visible in the UI. | 4.9.0-4.15.1 | |
| 3613811 | LCM operations using in-band management are unsupported on switches that use eth0 connected to an out-of-band network. To work around this issue, configure NetQ to use out-of-band management in the <code>mgmt</code> VRF on Cumulus Linux switches when interface eth0 is in use. | 4.8.0-4.15.1 | |

### Fixed Issues in 4.14.0
|  Issue ID 	|   Description	|   Affects	|
|---	        |---	        |---	    |
| 4371014 | In the full-screen switch card, the interface charts display incorrect values for transmit (Tx) and receive (Rx) byte rates. The actual values are slightly higher than the displayed values. | 4.12.0-4.13.0 | |
| 4360421 | When you back up your data from a prior NetQ release and restore it after installing NetQ 4.13.0, any switches that were in a rotten state are missing from the NetQ inventory after the upgrade. To work around this issue, decommission any rotten switches before you upgrade and reconnect the agents after the upgrade is complete. | 4.13.0 | |
| 4360420, 4316305 | When you upgrade to 4.13, network snapshots taken prior to upgrading are not restored. | 4.13.0 | |
| 4280023 | After backing up and restoring your NetQ data, any modifications to default suppression rules will be lost. | 4.12.0-4.13.0 | |
| 4261089, 4303877 | When you upgrade a cloud deployment, some switches might not appear in the search field or list of hostnames. To work around this issue, decommission the switches, then restart the agent on each switch with the <code> sudo netq config restart agent </code> command. | 4.13.0 | |
| 4236491 | When you click within a comparison view chart in link health view, the link utilization values in the side menu might differ from the values displayed in the comparison view chart. The values in the comparison chart are aggregated ever hour, whereas the values in the side menu reflect the most recent data.  | 4.13.0 | |
| 3769936, 3976289, 4122250 | When there is a NetQ interface validation failure for admin state mismatch, the validation failure might clear unexpectedly while one side of the link is still administratively down. | 4.9.0-4.13.0 | |

