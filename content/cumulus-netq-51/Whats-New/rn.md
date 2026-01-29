---
title: NVIDIA NetQ 5.1 Release Notes
author: Cumulus Networks
weight: 30
product: Cumulus NetQ
version: "5.1"
toc: 1
type: rn
pdfhidden: True
---
{{<rn_xls_link dir="cumulus-netq-50" >}}
## 5.0.1 Release Notes
### Open Issues in 5.0.1

|  Issue ID 	|   Description	|   Affects	|   Fixed |
|---	        |---	        |---	    |---	                |
| <a name="4786996"></a> [4786996](#4786996) <a name="4786996"></a> <br /> | To use lifecycle management in NMC or BCM environments, you must edit the master node IP address in the configuration manager to match the cluster’s head node IP address. Use the <code>kubectl edit cm -n netq-eth netq-master-node-ip</code> command to edit the configuration. In the configuration file, change the <code>data/master_node</code> field to the cluster’s head node IP address.  | 5.0.0-5.0.1 | |
| <a name="4687477"></a> [4687477](#4687477) <a name="4687477"></a> <br /> | When you run a validation against a group of devices with specific labels, NetQ ignores any pre-configured filters. | 5.0.0-5.0.1 | |
| <a name="4687241"></a> [4687241](#4687241) <a name="4687241"></a> <br /> | The activity log in the UI might display multiple entries with “unknown” or “anonymous” usernames.  | 5.0.0-5.0.1 | |
| <a name="4683830"></a> [4683830](#4683830) <a name="4683830"></a> <br /> | The Cable Validation Tool might fail to load in the NetQ UI. To work around this issue,  log out of NetQ and then log back in. | 5.0.0-5.0.1 | |
| <a name="4681581"></a> [4681581](#4681581) <a name="4681581"></a> <br /> | The <code>netq bootstrap reset purge-db</code> command might take up to 60 minutes to complete on Base Command Manager scale deployments. | 5.0.0-5.0.1 | |
| <a name="4668341"></a> [4668341](#4668341) <a name="4668341"></a> <br /> | When you a create an LDAP server configuration, the NetQ UI incorrectly allows you to modify the default server ports. Only the standard ports (389 for insecure and 636 for secure) are permitted. | 5.0.0-5.0.1 | |
| <a name="4573427"></a> [4573427](#4573427) <a name="4573427"></a> <br /> | The link health view utilization chart might display incorrect values for the top 5 links when multiple links share the same value. | 5.0.0-5.0.1 | |
| <a name="4399074"></a> [4399074](#4399074) <a name="4399074"></a> <br /> | When connecting a switch to NMX-T or NMX-C through the service registration workflow, use either the IP address or the hostname. Using both creates duplicate registrations, and the operation does not fail as expected. | 5.0.0-5.0.1 | |
| <a name="4100882"></a> [4100882](#4100882) <a name="4100882"></a> <br /> | When you attempt to export a file that is larger than 200MB, your browser might crash or otherwise prevent you from exporting the file. To work around this issue, use filters in the UI to decrease the size of the dataset that you intend to export. | 4.12.0-4.15.1, 5.0.0-5.0.1 | |

### Fixed Issues in 5.0.1
|  Issue ID 	|   Description	|   Affects	|
|---	        |---	        |---	    |
| <a name="4784336"></a> [4784336](#4784336) <a name="4784336"></a> <br /> | The NetQ for NVLink deployment option is not supported in air-gapped environments. | 5.0.0 | |

## 5.0.0 Release Notes
### Open Issues in 5.0.0

|  Issue ID 	|   Description	|   Affects	|   Fixed |
|---	        |---	        |---	    |---	                |
| <a name="4786996"></a> [4786996](#4786996) <a name="4786996"></a> <br /> | To use lifecycle management in NMC or BCM environments, you must edit the master node IP address in the configuration manager to match the cluster’s head node IP address. Use the <code>kubectl edit cm -n netq-eth netq-master-node-ip</code> command to edit the configuration. In the configuration file, change the <code>data/master_node</code> field to the cluster’s head node IP address.  | 5.0.0 | |
| <a name="4784336"></a> [4784336](#4784336) <a name="4784336"></a> <br /> | The NetQ for NVLink deployment option is not supported in air-gapped environments. | 5.0.0 | |
| <a name="4687477"></a> [4687477](#4687477) <a name="4687477"></a> <br /> | When you run a validation against a group of devices with specific labels, NetQ ignores any pre-configured filters. | 5.0.0 | |
| <a name="4687241"></a> [4687241](#4687241) <a name="4687241"></a> <br /> | The activity log in the UI might display multiple entries with “unknown” or “anonymous” usernames.  | 5.0.0 | |
| <a name="4683830"></a> [4683830](#4683830) <a name="4683830"></a> <br /> | The Cable Validation Tool might fail to load in the NetQ UI. To work around this issue,  log out of NetQ and then log back in. | 5.0.0 | |
| <a name="4681581"></a> [4681581](#4681581) <a name="4681581"></a> <br /> | The <code>netq bootstrap reset purge-db</code> command might take up to 60 minutes to complete on Base Command Manager scale deployments. | 5.0.0 | |
| <a name="4668341"></a> [4668341](#4668341) <a name="4668341"></a> <br /> | When you a create an LDAP server configuration, the NetQ UI incorrectly allows you to modify the default server ports. Only the standard ports (389 for insecure and 636 for secure) are permitted. | 5.0.0 | |
| <a name="4573427"></a> [4573427](#4573427) <a name="4573427"></a> <br /> | The link health view utilization chart might display incorrect values for the top 5 links when multiple links share the same value. | 5.0.0 | |
| <a name="4399074"></a> [4399074](#4399074) <a name="4399074"></a> <br /> | When connecting a switch to NMX-T or NMX-C through the service registration workflow, use either the IP address or the hostname. Using both creates duplicate registrations, and the operation does not fail as expected. | 5.0.0 | |
| <a name="4100882"></a> [4100882](#4100882) <a name="4100882"></a> <br /> | When you attempt to export a file that is larger than 200MB, your browser might crash or otherwise prevent you from exporting the file. To work around this issue, use filters in the UI to decrease the size of the dataset that you intend to export. | 4.12.0-4.15.1, 5.0.0 | |

### Fixed Issues in 5.0.0
|  Issue ID 	|   Description	|   Affects	|
|---	        |---	        |---	    |
| <a name="4521037"></a> [4521037](#4521037) <a name="4521037"></a> <br /> | The PTP violations summary in the UI might not render properly. To work around this issue, refresh the page in your browser. | 4.15.0-4.15.1 | |
| <a name="3993538"></a> [3993538](#3993538) <a name="3993538"></a> <br /> | When you re-position a card on your workbench and then manually refresh the workbench, NetQ might reposition the cards. | 4.11.0-4.15.1 | |

