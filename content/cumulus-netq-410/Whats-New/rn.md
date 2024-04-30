---
title: NVIDIA NetQ 4.10 Release Notes
author: Cumulus Networks
weight: 30
product: Cumulus NetQ
version: "4.10"
toc: 1
type: rn
pdfhidden: True
---
{{<rn_xls_link dir="cumulus-netq-410" >}}
## 4.10.0 Release Notes
### Open Issues in 4.10.0

|  Issue ID 	|   Description	|   Affects	|   Fixed |
|---	        |---	        |---	    |---	                |
| <a name="3866340"></a> [3866340](#3866340) <a name="3866340"></a> <br /> | When NetQ validates BGP neighbors in your network, numbered BGP neighbors pass validation with mismatched values configured. | 4.10.0 | |
| <a name="3863195"></a> [3863195](#3863195) <a name="3863195"></a> <br /> | When you perform an LCM switch discovery on a Cumulus Linux 5.9.0 switch in your network that was already added in the NetQ inventory on a prior Cumulus Linux version, the switch will appear as Rotten in the NetQ UI. To work around this issue, decommission the switch first,and run LCM discovery again after the switch is upgraded. | 4.10.0 | |
| <a name="3854467"></a> [3854467](#3854467) <a name="3854467"></a> <br /> | When the NetQ master node in a cluster is down, the NetQ kafka-connect pods might crash on other cluster nodes, preventing data collection. To work around this issue, bring the master node back into service. | 4.10.0 | |
| <a name="3851922"></a> [3851922](#3851922) <a name="3851922"></a> <br /> | After you run an LCM switch discovery in a NetQ cluster environment, NetQ CLI commands on switches might fail with the message <code>Failed to process command</code>. | 4.10.0 | |
| <a name="3847280"></a> [3847280](#3847280) <a name="3847280"></a> <br /> | The <code>netq-opta</code> package fails to install on Cumulus Linux 5.9.0. On-switch OPTA is not supported on Cumulus Linux 5.9.0. | 4.10.0 | |
| <a name="3814701"></a> [3814701](#3814701) <a name="3814701"></a> <br /> | After you upgrade NetQ, devices that were in a rotten state before the upgrade might not appear in the UI or CLI after the upgrade. To work around this issue, decommission rotten devices before performing the upgrade. | 4.9.0-4.10.0 | |
| <a name="3800434"></a> [3800434](#3800434) <a name="3800434"></a> <br /> | When you upgrade NetQ from a version prior to 4.9.0, What Just Happened data that was collected before the upgrade is no longer present. | 4.9.0-4.10.0 | |
| <a name="3798677"></a> [3798677](#3798677) <a name="3798677"></a> <br /> | In a NetQ cluster environment, if your master node goes offline and is restored, subsequent NetQ validations for MLAG and EVPN might unexpectedly indicate failures. To work around this issue, either restart NetQ agents on devices in the inventory or wait up to 24 hours for the issue to clear. | 4.9.0-4.10.0 | |
| <a name="3787946"></a> [3787946](#3787946) <a name="3787946"></a> <br /> | When you install a NetQ cluster deployment on a subnet with other NetQ clusters or other devices using VRRP, there might be connectivity loss to the cluster virtual IP (VIP). The VIP is established using the VRRP protocol, and during cluster installation a virtual router ID (VRID) is selected. If another device on the subnet running VRRP selects the same VRID, connectivity issues may occur. To work around this issue, avoid multiple VRRP speakers on the subnet, or ensure the VRID used on all VRRP devices is unique. To validate the VRID used by NetQ, check the assigned <code>virtual_router_id</code> value in <code>/mnt/keepalived/keepalived.conf</code>. | 4.9.0-4.10.0 | |
| <a name="3772274"></a> [3772274](#3772274) <a name="3772274"></a> <br /> | After you upgrade NetQ, data from snapshots taken prior to the NetQ upgrade will contain unreliable data and should not be compared to any snapshots taken after the upgrade. In cluster deployments, snapshots from prior NetQ versions will not be visible in the UI. | 4.9.0-4.10.0 | |
| <a name="3769936"></a> [3769936](#3769936) <a name="3769936"></a> <br /> | When there is a NetQ interface validation failure for admin state mismatch, the validation failure might clear unexpectedly while one side of the link is still administratively down. | 4.9.0-4.10.0 | |
| <a name="3752422"></a> [3752422](#3752422) <a name="3752422"></a> <br /> | When you run a NetQ trace and specify MAC addresses for the source and destination, NetQ displays the message “No valid path to destination” and does not display trace data. | 4.9.0-4.10.0 | |
| <a name="3721754"></a> [3721754](#3721754) <a name="3721754"></a> <br /> | After you decommission a switch, the switch's interfaces are still displayed in the NetQ UI in the Interfaces view. | 4.9.0-4.10.0 | |
| <a name="3613811"></a> [3613811](#3613811) <a name="3613811"></a> <br /> | LCM operations using in-band management are unsupported on switches that use eth0 connected to an out-of-band network. To work around this issue, configure NetQ to use out-of-band management in the <code>mgmt</code> VRF on Cumulus Linux switches when interface eth0 is in use. | 4.8.0-4.10.0 | |

### Fixed Issues in 4.10.0
|  Issue ID 	|   Description	|   Affects	|
|---	        |---	        |---	    |
| <a name="3824873"></a> [3824873](#3824873) <a name="3824873"></a> <br /> | When you upgrade an on-premises NetQ deployment, the upgrade might fail with the following message:<pre>master-node-installer: Upgrading NetQ Appliance with tarball : /mnt/installables/NetQ-4.9.0.tgz<br>master-node-installer: Migrating H2 db list index out of range.</pre>To work around this issue, re-run the <code>netq upgrade</code> command.  | 4.9.0 | |
| <a name="3820671"></a> [3820671](#3820671) <a name="3820671"></a> <br /> | When you upgrade NetQ cluster deployments with DPUs in the device inventory, the DPUs might not be visible in the NetQ UI after the upgrade. To work around this issue, restart the DTS container on the DPUs in your network. | 4.9.0 | |
| <a name="3819688"></a> [3819688](#3819688) <a name="3819688"></a> <br /> | When you upgrade NetQ cluster deployments, the configured LCM credential profile assigned to switches in the inventory is reset to the default access profile. To work around this issue, reconfigure the correct access profile on switches before managing them with LCM after the upgrade.  | 4.9.0 | |
| <a name="3819364"></a> [3819364](#3819364) <a name="3819364"></a> <br /> | When you attempt to delete a scheduled trace using the NetQ UI, the trace record is not deleted. | 4.7.0-4.9.0 | |
| <a name="3813819"></a> [3813819](#3813819) <a name="3813819"></a> <br /> | When you perform a switch discovery by specifying an IP range, an error message is displayed if switches included in the range have different credentials. To work around this issue, batch switches based on their credentials and run a switch discovery for each batch. | 4.9.0 | |
| <a name="3813078"></a> [3813078](#3813078) <a name="3813078"></a> <br /> | When you perform a NetQ upgrade, the upgrade might fail with the following error message:<pre>Command '&#91;'kubectl', 'version --client'&#93;' returned non-zero exit status 1.</pre>To work around this issue, run the <code>netq bootstrap reset keep-db</code> command and then reinstall NetQ using the <code>netq install</code> <a href="https://docs.nvidia.com/networking-ethernet-software/cumulus-netq/More-Documents/NetQ-CLI-Reference-Manual/install/">command for your deployment.</a> | 4.9.0 | |
| <a name="3808200"></a> [3808200](#3808200) <a name="3808200"></a> <br /> | When you perform a <code>netq bootstrap reset</code> on a NetQ cluster VM and perform a fresh install with the <code>netq install</code> command, the install might fail with the following error:<pre> master-node-installer: Running sanity check on cluster_vip: 10.10.10.10 Virtual IP 10.10.10.10 is already used</pre>To work around this issue, run the <code>netq install</code> command again. | 4.9.0 | |
| <a name="3773879"></a> [3773879](#3773879) <a name="3773879"></a> <br /> | When you upgrade a switch running Cumulus Linux using NetQ LCM, any configuration files in <code>/etc/cumulus/switchd.d</code> for adaptive routing or other features are not restored after the upgrade. To work around this issue, manually back up these files and restore them after the upgrade. | 4.9.0 | |
| <a name="3771124"></a> [3771124](#3771124) <a name="3771124"></a> <br /> | When you reconfigure a VNI to map to a different VRF or remove and recreate a VNI in the same VRF, NetQ EVPN validations might incorrectly indicate a failure for the VRF consistency test. | 4.9.0 | |
| <a name="3760442"></a> [3760442](#3760442) <a name="3760442"></a> <br /> | When you export events from NetQ to a CSV file, the timestamp of the exported events does not match the timestamp reported in the NetQ UI based on the user profile's time zone setting. | 4.9.0 | |
| <a name="3755207"></a> [3755207](#3755207) <a name="3755207"></a> <br /> | When you export digital optics table data from NetQ, some fields might be visible in the UI that are not exported to CSV or JSON files. | 4.9.0 | |
| <a name="3738840"></a> [3738840](#3738840) <a name="3738840"></a> <br /> | When you upgrade a Cumulus Linux switch configured for TACACS authentication using NetQ LCM, the switch's TACACS configuration is not restored after upgrade. | 4.8.0-4.9.0 | |

