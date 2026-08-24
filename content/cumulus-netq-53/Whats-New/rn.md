---
title: NVIDIA NetQ 5.3 Release Notes
author: Cumulus Networks
weight: 30
product: Cumulus NetQ
version: "5.3"
toc: 1
type: rn
pdfhidden: True
---
{{<rn_xls_link dir="cumulus-netq-53" >}}
## 5.3.0 Release Notes
### Open Issues in 5.3.0

|  Issue ID 	|   Description	|   Affects	|   Fixed |
|---	        |---	        |---	    |---	                |
| 4965251 | When BlueField DPUs are in the default, embedded mode, the output of the <code>netq check roce</code> command might produce duplicate entries for the same device (one for the host and one for the DPU). This issue can also affect the calculations for the RoCE Mode Consistency and DSCP Classification tests. Additionally, the <code>netq show roce-config host</code> command might display DPU interfaces alongside host interfaces. This issue does not affect DPUs that are configured in separated mode. | 5.2.1-5.3.0 | |
| 4867933 | Threshold-crossing events created before version 5.1.0 may not display event values correctly after you upgrade NetQ. | 5.1.0-5.3.0 | |
| 4687477 | When you run a validation against a group of devices with specific labels, NetQ ignores any pre-configured filters. | 5.0.0-5.3.0 | |
| 4681581 | The <code>netq bootstrap reset purge-db</code> command might take up to 60 minutes to complete on Base Command Manager scale deployments. | 5.0.0-5.3.0 | |
| 4399074 | When connecting a switch to NMX-T or NMX-C through the service registration workflow, use either the IP address or the hostname. Using both creates duplicate registrations, and the operation does not fail as expected. | 5.0.0-5.3.0 | |
| 4100882, 4119697 | When you attempt to export a file that is larger than 200MB, your browser might crash or otherwise prevent you from exporting the file. To work around this issue, use filters in the UI to decrease the size of the dataset that you intend to export. | 4.12.0-4.15.1, 5.0.0-5.3.0 | |

### Fixed Issues in 5.3.0
|  Issue ID 	|   Description	|   Affects	|
|---	        |---	        |---	    |
| 5073537 | After uninstalling a NetQ cluster, the cluster VIP address is not released from the network interface. On a subsequent reinstall, the installer detects the VIP as still reachable and exits with the error <code>cluster-vip address <ip> is reachable. Please provide non reachable IP address</code>, even though the cluster is no longer running<br />This issue affects deployments that use a VLAN interface (for example, <code>bond0.100</code>) rather than the management IP for the cluster VIP. It does not affect first-time installs, but blocks every uninstall-reinstall cycle until the VIP is manually removed<br />To work around this issue, manually remove the VIP from the interface before reinstalling with <code>sudo ip addr del <cluster-vip>/<prefix-length> dev <interface></code> | 5.2.1  | |
| 4989796 | When you send a POST request to <code>nmx/v1/support-packages</code> with a tech-support bundle larger than 1 MB, the operation fails. |  | |
| 4986372 | After installing NetQ for Ethernet and NVLink, the UI might fail to load and display the message <code>No route matched with those values.</code>. To work around this issue, restart the Kong-CP and Kong-DP deployments with <code>kubectl rollout restart deployment -n netq-infra kong-cp-kongsleep 300</code>, followed by <code>kubectl rollout restart deployment -n netq-infra kong-dp-kong</code><br /><br>If the issue persists, run <code>cd /tmp/netq-infra/kube-config/build/data-infra</code>, followed by <code>kubectl apply -f deck-sync-job.yaml</code>. | 5.2.1 | |
| 4943571 | After you register NVLink services, it might take up to an hour for the scheduler service to run and return data. | 5.2.1 | |
| 4854663 | When specifying a cluster VIP on an invalid or incorrect subnet, the installer displays an error indicating that <code>master_ip</code> should be different than <code>cluster_ip</code> without indicating which IP address is invalid. | 5.1.0-5.2.1 | |
| 4682275 | NVLink cluster installations do not validate that each node has a unique hostname. If two nodes share a common hostname, NetQ does not flag the issue after the installation completes. | 5.0.0-5.2.1 | |
| 4389662 | When a cluster installation fails a cluster VIP validation check, the installer generates an opta-support archive and prompts you to send it to NVIDIA support instead of prompting you to fix the initial error. | 4.15.0-5.2.1 | |
| 4122430 | When the master node is unreachable, a worker node might report the output of <code>netq show status</code> as <code>Not Installed</code> instead of indicating that the cluster was degraded. | 4.12.0-5.2.1 | |

