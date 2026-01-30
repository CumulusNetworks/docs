---
title: NVIDIA NetQ 4.13 Release Notes
author: Cumulus Networks
weight: 30
product: Cumulus NetQ
version: "4.13"
toc: 1
type: rn
pdfhidden: True
---
{{<rn_xls_link dir="cumulus-netq-413" >}}
## 4.13.0 Release Notes
### Open Issues in 4.13.0

|  Issue ID 	|   Description	|   Affects	|   Fixed |
|---	        |---	        |---	    |---	                |
| <a name="4612457"></a> [4612457](#4612457) <a name="4612457"></a> <br /> | The process monitoring dashboard may display inaccurate CPU utilization values for the NetQ agent. | 4.11.0-4.15.1 | 5.0.0|
| <a name="4466349"></a> [4466349](#4466349) <a name="4466349"></a> <br /> | When you upgrade an HA cluster deployment from a version that is not part of the supported upgrade path, the upgrade might fail and the UI might not load due to expired control plane certificates on the worker nodes.<br><br>To check whether the certificates have expired, run <code>sudo su</code> followed by <code>kubeadm certs check-expiration</code>. If the output displays a date in the past, your certificates are expired. To update the certificates, run <code>kubeadm certs renew all</code> on each worker node in the cluster. Next, restart the <a href="https://kubernetes.io/docs/concepts/overview/components/#control-plane-components/">control plane components</a> with <code>crictl stop CONTAINER_ID</code>, followed by <code>systemctl restart kubelet</code>. | 4.8.0-4.14.0 | 4.15.0-4.15.1|
| <a name="4371014"></a> [4371014](#4371014) <a name="4371014"></a> <br /> | In the full-screen switch card, the interface charts display incorrect values for transmit (Tx) and receive (Rx) byte rates. The actual values are slightly higher than the displayed values. | 4.12.0-4.13.0 | 4.14.0-4.15.1|
| <a name="4360421"></a> [4360421](#4360421) <a name="4360421"></a> <br /> | When you back up your data from a prior NetQ release and restore it after installing NetQ 4.13.0, any switches that were in a rotten state are missing from the NetQ inventory after the upgrade. To work around this issue, decommission any rotten switches before you upgrade and reconnect the agents after the upgrade is complete. | 4.13.0 | 4.14.0-4.15.1|
| <a name="4360420"></a> [4360420](#4360420) <a name="4360420"></a> <br /> | When you upgrade to 4.13, network snapshots taken prior to upgrading are not restored. | 4.13.0 | 4.14.0-4.15.1|
| <a name="4310939"></a> [4310939](#4310939) <a name="4310939"></a> <br /> | When a switch becomes rotten or is connected to a different NetQ server without decommissioning it first, the link health view dashboard displays outdated counter values. To work around this issue, wait for NetQ to update and display accurate counter values. | 4.13.0-4.14.0 | 4.15.0-4.15.1|
| <a name="4309191"></a> [4309191](#4309191) <a name="4309191"></a> <br /> | In cloud deployments, lifecycle management operations such as device discovery or switch decommissioning might time out and ultimately fail. To work around this issue, restart the LCM executor on the OPTA VM with <code>lcm_pod='kubectl get pod \| grep -m1 lcm \| awk ‘{print $1}’'; kubectl delete pod $lcm_pod</code>. | 4.13.0-4.14.0 | 4.15.0-4.15.1|
| <a name="4280023"></a> [4280023](#4280023) <a name="4280023"></a> <br /> | After backing up and restoring your NetQ data, any modifications to default suppression rules will be lost. | 4.12.0-4.13.0 | 4.14.0-4.15.1|
| <a name="4261089"></a> [4261089](#4261089) <a name="4261089"></a> <br /> | When you upgrade a cloud deployment, some switches might not appear in the search field or list of hostnames. To work around this issue, decommission the switches, then restart the agent on each switch with the <code> sudo netq config restart agent </code> command. | 4.13.0 | 4.14.0-4.15.1|
| <a name="4248942"></a> [4248942](#4248942) <a name="4248942"></a> <br /> | When you assign a role to a switch, NetQ might take up to five minutes to reflect the new or updated role in the queue histogram fabric overview page. | 4.13.0-4.14.0 | 4.15.0-4.15.1|
| <a name="4236491"></a> [4236491](#4236491) <a name="4236491"></a> <br /> | When you click within a comparison view chart in link health view, the link utilization values in the side menu might differ from the values displayed in the comparison view chart. The values in the comparison chart are aggregated ever hour, whereas the values in the side menu reflect the most recent data.  | 4.13.0 | 4.14.0-4.15.1|
| <a name="4131550"></a> [4131550](#4131550) <a name="4131550"></a> <br /> | When you run a topology validation, the full-screen topology validation view might not display the latest results. To work around this issue, refresh the page. | 4.12.0-4.15.1 | |
| <a name="4100882"></a> [4100882](#4100882) <a name="4100882"></a> <br /> | When you attempt to export a file that is larger than 200MB, your browser might crash or otherwise prevent you from exporting the file. To work around this issue, use filters in the UI to decrease the size of the dataset that you intend to export. | 4.12.0-4.15.1, 5.0.0 | |
| <a name="3993538"></a> [3993538](#3993538) <a name="3993538"></a> <br /> | When you re-position a card on your workbench and then manually refresh the workbench, NetQ might reposition the cards. | 4.11.0-4.15.1 | 5.0.0|
| <a name="3800434"></a> [3800434](#3800434) <a name="3800434"></a> <br /> | When you upgrade NetQ from a version prior to 4.9.0, What Just Happened data that was collected before the upgrade is no longer present. | 4.9.0-4.15.1 | |
| <a name="3772274"></a> [3772274](#3772274) <a name="3772274"></a> <br /> | After you upgrade NetQ, data from snapshots taken prior to the NetQ upgrade will contain unreliable data and should not be compared to any snapshots taken after the upgrade. In cluster deployments, snapshots from prior NetQ versions will not be visible in the UI. | 4.9.0-4.15.1 | |
| <a name="3769936"></a> [3769936](#3769936) <a name="3769936"></a> <br /> | When there is a NetQ interface validation failure for admin state mismatch, the validation failure might clear unexpectedly while one side of the link is still administratively down. | 4.9.0-4.13.0 | 4.14.0-4.15.1|
| <a name="3613811"></a> [3613811](#3613811) <a name="3613811"></a> <br /> | LCM operations using in-band management are unsupported on switches that use eth0 connected to an out-of-band network. To work around this issue, configure NetQ to use out-of-band management in the <code>mgmt</code> VRF on Cumulus Linux switches when interface eth0 is in use. | 4.8.0-4.15.1 | |

### Fixed Issues in 4.13.0
|  Issue ID 	|   Description	|   Affects	|
|---	        |---	        |---	    |
| <a name="4181296"></a> [4181296](#4181296) <a name="4181296"></a> <br /> | NetQ might become unresponsive when someone with a non-admin (user) role attempts to create or clone workbenches, add cards to a workbench, create validations, or run a flow analysis. | 4.11.0-4.12.0 | |
| <a name="4162383"></a> [4162383](#4162383) <a name="4162383"></a> <br /> | When you upgrade a NetQ VM with devices in the inventory that have been rotten for 7 or more days, NetQ's global search field might fail to return results for individual devices. To work around this issue, decommission rotten devices and ensure they are running the appropriate NetQ agent version. | 4.12.0 | |
| <a name="4157785"></a> [4157785](#4157785) <a name="4157785"></a> <br /> | When you add a new switch to the NetQ inventory, the NetQ UI might not display interface statistics or interface validation data for the new switch for up to one hour.<br>To work around this issue, adjust the poll period to 60 seconds on the new switch with the <code>netq config add agent command service-key ports poll-period 60</code> command. When interface data is displayed in the NetQ UI, change it back to the default value of 3600 with the <code>netq config add agent command service-key ports poll-period 3600</code> command. | 4.12.0 | |
| <a name="4155900"></a> [4155900](#4155900) <a name="4155900"></a> <br /> | When a fan’s sensor state is “high”, NetQ correctly displays the count information on the sensor health card. When the card is expanded to the detailed view, fans with a “high” sensor state will not be included among the fans with problematic states. | 4.12.0 | |
| <a name="4124724"></a> [4124724](#4124724) <a name="4124724"></a> <br /> | External notifications for DPU RoCE threshold-crossing events are not supported. To work around this issue, use the UI or CLI to view DPU RoCE threshold-crossing events. | 4.12.0 | |

