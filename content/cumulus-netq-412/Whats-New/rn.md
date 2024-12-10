---
title: NVIDIA NetQ 4.12 Release Notes
author: Cumulus Networks
weight: 30
product: Cumulus NetQ
version: "4.12"
toc: 1
type: rn
pdfhidden: True
---
{{<rn_xls_link dir="cumulus-netq-412" >}}
## 4.12.0 Release Notes
### Open Issues in 4.12.0

|  Issue ID 	|   Description	|   Affects	|   Fixed |
|---	        |---	        |---	    |---	                |
| <a name="4181296"></a> [4181296](#4181296) <a name="4181296"></a> <br /> | NetQ might become unresponsive when someone with a non-admin (user) role attempts to create or clone workbenches, add cards to a workbench, create validations, or run a flow analysis. | 4.11.0-4.12.0 | |
| <a name="4160704"></a> [4160704](#4160704) <a name="4160704"></a> <br /> | In large-scale environments, NetQ might take up to a minute to display the results of the BGP validation in the UI and the <code>netq check bgp</code> command using the CLI. | 4.12.0 | |
| <a name="4157785"></a> [4157785](#4157785) <a name="4157785"></a> <br /> | When you add a new switch to the NetQ inventory, the NetQ UI might not display interface statistics or interface validation data for the new switch for up to one hour<br /><br>To work around this issue, adjust the poll period to 60 seconds on the new switch with the <code>netq config add agent command service-key ports poll-period 60</code> command. When interface data is displayed in the NetQ UI, change it back to the default value of 3600 with the <code>netq config add agent command service-key ports poll-period 3600</code> command<br /> | 4.12.0 | |
| <a name="4155900"></a> [4155900](#4155900) <a name="4155900"></a> <br /> | When a fan’s sensor state is “high”, NetQ correctly displays the count information on the sensor health card. When the card is expanded to the detailed view, fans with a “high” sensor state will not be included among the fans with problematic states. | 4.12.0 | |
| <a name="4131550"></a> [4131550](#4131550) <a name="4131550"></a> <br /> | When you run a topology validation, the full-screen topology validation view might not display the latest results. To work around this issue, refresh the page. | 4.12.0 | |
| <a name="3985598"></a> [3985598](#3985598) <a name="3985598"></a> <br /> | When you configure multiple threshold-crossing events for the same TCA event ID on the same device, NetQ will only display one TCA event for each hostname per TCA event ID, even if both thresholds are crossed or status events are triggered.   | 4.11.0-4.12.0 | |
| <a name="3800434"></a> [3800434](#3800434) <a name="3800434"></a> <br /> | When you upgrade NetQ from a version prior to 4.9.0, What Just Happened data that was collected before the upgrade is no longer present. | 4.9.0-4.12.0 | |
| <a name="3772274"></a> [3772274](#3772274) <a name="3772274"></a> <br /> | After you upgrade NetQ, data from snapshots taken prior to the NetQ upgrade will contain unreliable data and should not be compared to any snapshots taken after the upgrade. In cluster deployments, snapshots from prior NetQ versions will not be visible in the UI. | 4.9.0-4.12.0 | |
| <a name="3771279"></a> [3771279](#3771279) <a name="3771279"></a> <br /> | When an interface speed is changed in the network, NetQ might not reflect the new speed until up to an hour after the change. | 4.11.0-4.12.0 | |
| <a name="3769936"></a> [3769936](#3769936) <a name="3769936"></a> <br /> | When there is a NetQ interface validation failure for admin state mismatch, the validation failure might clear unexpectedly while one side of the link is still administratively down. | 4.9.0-4.12.0 | |
| <a name="3752422"></a> [3752422](#3752422) <a name="3752422"></a> <br /> | When you run a NetQ trace and specify MAC addresses for the source and destination, NetQ displays the message “No valid path to destination” and does not display trace data. | 4.9.0-4.12.0 | |
| <a name="3613811"></a> [3613811](#3613811) <a name="3613811"></a> <br /> | LCM operations using in-band management are unsupported on switches that use eth0 connected to an out-of-band network. To work around this issue, configure NetQ to use out-of-band management in the <code>mgmt</code> VRF on Cumulus Linux switches when interface eth0 is in use. | 4.8.0-4.12.0 | |

### Fixed Issues in 4.12.0
|  Issue ID 	|   Description	|   Affects	|
|---	        |---	        |---	    |
| <a name="4001098"></a> [4001098](#4001098) <a name="4001098"></a> <br /> | When you use NetQ LCM to upgrade a Cumulus Linux switch from version 5.9 to 5.10, and if the upgrade fails, NetQ rolls back to version 5.9 and reverts the <code>cumulus</code> user password to the default password. After rollback, reconfigure the password with the <code>nv set system aaa user cumulus password \<password\></code> command.   | 4.11.0 | |
| <a name="4000939"></a> [4000939](#4000939) <a name="4000939"></a> <br /> | When you upgrade a NetQ VM with devices in the inventory that have been rotten for 7 or more days, NetQ inventory cards in the UI and table output might show inconsistent results and might not display the rotten devices. To work around this issue, decommission the rotten device and ensure it's running the appropriate NetQ agent version. | 4.11.0 | |
| <a name="3995266"></a> [3995266](#3995266) <a name="3995266"></a> <br /> | When you use NetQ LCM to upgrade a Cumulus Linux switch with NTP configured using NVUE in a VRF that is not <code>mgmt</code>, the upgrade fails to complete. To work around this issue, first unset the NTP configuration with the <code>nv unset service ntp</code> and <code>nv config apply</code> commands, and reconfigure NTP after the upgrade completes. | 4.11.0 | |
| <a name="3981655"></a> [3981655](#3981655) <a name="3981655"></a> <br /> | When you upgrade your NetQ VM, some devices in the NetQ inventory might appear as rotten. To work around this issue, restart NetQ agents on devices or upgrade them to the latest agent version after the NetQ VM upgrade is completed. | 4.11.0 | |
| <a name="3858210"></a> [3858210](#3858210) <a name="3858210"></a> <br /> | When you upgrade your NetQ VM, DPUs in the inventory are not shown. To work around this issue, restart the DTS container on the DPUs in your network. | 4.10.0-4.11.0 | |
| <a name="3854467"></a> [3854467](#3854467) <a name="3854467"></a> <br /> | When a single NetQ cluster VM is offline, the NetQ kafka-connect pods are brought down on other cluster nodes, preventing NetQ data from collecting data. To work around this issue, bring all cluster nodes back into service. | 4.10.0-4.11.0 | |

