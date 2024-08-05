---
title: NVIDIA NetQ 4.11 Release Notes
author: Cumulus Networks
weight: 30
product: Cumulus NetQ
version: "4.11"
toc: 1
type: rn
pdfhidden: True
---
{{<rn_xls_link dir="cumulus-netq-411" >}}
## 4.11.0 Release Notes
### Open Issues in 4.11.0

|  Issue ID 	|   Description	|   Affects	|   Fixed |
|---	        |---	        |---	    |---	                |
| <a name="4004830"></a> [4004830](#4004830) <a name="4004830"></a> <br /> | When you attempt to reset your password from the login page, NetQ might display an error that your token is either invalid or expired. To work around this issue, either clear your cache or open the reset link contained in the email you received in an incognito window and reset your password from there. | 4.11.0 | |
| <a name="4001098"></a> [4001098](#4001098) <a name="4001098"></a> <br /> | When you use NetQ LCM to upgrade a Cumulus Linux switch from version 5.9 to 5.10, and if the upgrade fails, NetQ rolls back to version 5.9 and reverts the <code>cumulus</code> user password to the default password. After rollback, reconfigure the password with the <code>nv set system aaa user cumulus password \<password\></code> command.   | 4.11.0 | |
| <a name="3995266"></a> [3995266](#3995266) <a name="3995266"></a> <br /> | When you use NetQ LCM to upgrade a Cumulus Linux switch with NTP configured using NVUE in a VRF that is not <code>mgmt</code>, the upgrade fails to complete. To work around this issue, first unset the NTP configuration with the <code>nv unset service ntp</code> and <code>nv config apply</code> commands, and reconfigure NTP after the upgrade completes. | 4.11.0 | |
| <a name="3993243"></a> [3993243](#3993243) <a name="3993243"></a> <br /> | When you upgrade your NetQ VM, RoCE validation data might not contain all RoCE-enabled switches in your network. This condition will clear within 24 hours of the NetQ upgrade.  | 4.10.0-4.11.0 | |
| <a name="3985598"></a> [3985598](#3985598) <a name="3985598"></a> <br /> | When you configure multiple threshold-crossing events for the same TCA event ID on the same device, NetQ will only display one TCA event for each hostname per TCA event ID, even if both thresholds are crossed or status events are triggered.   | 4.11.0 | |
| <a name="3983871"></a> [3983871](#3983871) <a name="3983871"></a> <br /> | When you run the <code>netq install</code> command on a VM with an IP address configured that overlaps the NetQ pod or service IP subnets 10.244.0.0/16 or 10.96.0.0/16, the install prechecks will fail but subsequent attempts to run <code>netq install</code> will fail even after changing the VM IP address to not conflict with these subnets. To work around this issue, run the <code>netq bootstrap reset purge-db</code> command and rerun the <code>netq install</code> command. | 4.11.0 | |
| <a name="3981655"></a> [3981655](#3981655) <a name="3981655"></a> <br /> | When you upgrade your NetQ VM, some devices in the NetQ inventory might appear as rotten. To work around this issue, restart NetQ agents on devices or upgrade them to the latest agent version after the NetQ VM upgrade is completed. | 4.11.0 | |
| <a name="3854467"></a> [3854467](#3854467) <a name="3854467"></a> <br /> | When a single NetQ cluster VM is offline, the NetQ kafka-connect pods are brought down on other cluster nodes, preventing NetQ data from collecting data. To work around this issue, bring all cluster nodes back into service. | 4.10.0-4.11.0 | |
| <a name="3847280"></a> [3847280](#3847280) <a name="3847280"></a> <br /> | The <code>netq-opta</code> package fails to install on Cumulus Linux 5.9.0. On-switch OPTA is not supported on Cumulus Linux 5.9.0. | 4.10.0-4.11.0 | |
| <a name="3800434"></a> [3800434](#3800434) <a name="3800434"></a> <br /> | When you upgrade NetQ from a version prior to 4.9.0, What Just Happened data that was collected before the upgrade is no longer present. | 4.9.0-4.11.0 | |
| <a name="3772274"></a> [3772274](#3772274) <a name="3772274"></a> <br /> | After you upgrade NetQ, data from snapshots taken prior to the NetQ upgrade will contain unreliable data and should not be compared to any snapshots taken after the upgrade. In cluster deployments, snapshots from prior NetQ versions will not be visible in the UI. | 4.9.0-4.11.0 | |
| <a name="3771279"></a> [3771279](#3771279) <a name="3771279"></a> <br /> | When an interface speed is changed in the network, NetQ might not reflect the new speed until up to an hour after the change. | 4.11.0 | |
| <a name="3769936"></a> [3769936](#3769936) <a name="3769936"></a> <br /> | When there is a NetQ interface validation failure for admin state mismatch, the validation failure might clear unexpectedly while one side of the link is still administratively down. | 4.9.0-4.11.0 | |
| <a name="3752422"></a> [3752422](#3752422) <a name="3752422"></a> <br /> | When you run a NetQ trace and specify MAC addresses for the source and destination, NetQ displays the message “No valid path to destination” and does not display trace data. | 4.9.0-4.11.0 | |
| <a name="3613811"></a> [3613811](#3613811) <a name="3613811"></a> <br /> | LCM operations using in-band management are unsupported on switches that use eth0 connected to an out-of-band network. To work around this issue, configure NetQ to use out-of-band management in the <code>mgmt</code> VRF on Cumulus Linux switches when interface eth0 is in use. | 4.8.0-4.11.0 | |

### Fixed Issues in 4.11.0
|  Issue ID 	|   Description	|   Affects	|
|---	        |---	        |---	    |
| <a name="4011713"></a> [4011713](#4011713) <a name="4011713"></a> <br /> | When you run a duplicate address validation, NetQ might report a validation failure indicating 127.0.1.1 is duplicated on Cumulus Linux 5.10.0 switches. To suppress this validation failure, run the <code>netq add check-filter  check_filter_id addr_1 check_name addr test_name IPV4_Duplicate_Address scope '&#91;{"Prefix": "127.0.1.1"}&#93;'</code> CLI command, or use the NetQ UI to add duplicate address filter for address 127.0.1.1.  |  | |
| <a name="3948198"></a> [3948198](#3948198) <a name="3948198"></a> <br /> | When you upgrade a Cumulus Linux switch configured with NVUE using NetQ LCM, the upgrade might fail due to NVUE configuration validation if the NVUE object model was changed between the current and new Cumulus Linux version. When this failure occurs, NetQ is unable to rollback to the prior configuration and the switch remains running the default Cumulus Linux configuration.  | 4.10.1 | |
| <a name="3863195"></a> [3863195](#3863195) <a name="3863195"></a> <br /> | When you perform an LCM switch discovery on a Cumulus Linux 5.9.0 switch in your network that was already added in the NetQ inventory on a prior Cumulus Linux version, the switch will appear as Rotten in the NetQ UI. To work around this issue, decommission the switch first,and run LCM discovery again after the switch is upgraded. | 4.10.0-4.10.1 | |
| <a name="3851922"></a> [3851922](#3851922) <a name="3851922"></a> <br /> | After you run an LCM switch discovery in a NetQ cluster environment, NetQ CLI commands on switches might fail with the message <code>Failed to process command</code>. | 4.10.0-4.10.1 | |
| <a name="3721754"></a> [3721754](#3721754) <a name="3721754"></a> <br /> | After you decommission a switch, the switch's interfaces are still displayed in the NetQ UI in the Interfaces view. | 4.9.0-4.10.1 | |

