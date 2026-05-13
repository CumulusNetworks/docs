---
title: NVIDIA NetQ 5.0 Release Notes
author: Cumulus Networks
weight: 30
product: Cumulus NetQ
version: "5.0"
toc: 1
type: rn
pdfhidden: True
---
{{<rn_xls_link dir="cumulus-netq-50" >}}
## 5.0.1 Release Notes
### Open Issues in 5.0.1

|  Issue ID 	|   Description	|   Affects	|   Fixed |
|---	        |---	        |---	    |---	                |
| 4786996 | To use lifecycle management in NMC or BCM environments, you must edit the master node IP address in the configuration manager to match the cluster’s head node IP address. Use the <code>kubectl edit cm -n netq-eth netq-master-node-ip</code> command to edit the configuration. In the configuration file, change the <code>data/master_node</code> field to the cluster’s head node IP address.  | 5.0.0-5.0.1 | 5.1.0|
| 4693161 | In cluster and scale cluster deployments, the snapshot comparison feature may time out when comparing MAC addresses. | 5.0.0-5.0.1 | 5.1.0|
| 4689932 | Node reservation for NetQ is not supported in shared multi-node clusters. To work around this issue, deploy NetQ in a dedicated single-node or three-node cluster first, and then scale the deployment by adding nodes for other applications. | 5.0.0-5.0.1 | 5.1.0|
| 4687477 | When you run a validation against a group of devices with specific labels, NetQ ignores any pre-configured filters. | 5.0.0-5.1.0 | |
| 4687241 | The activity log in the UI might display multiple entries with “unknown” or “anonymous” usernames.  | 5.0.0-5.0.1 | 5.1.0|
| 4683830 | The Cable Validation Tool might fail to load in the NetQ UI. To work around this issue,  log out of NetQ and then log back in. | 5.0.0-5.0.1 | 5.1.0|
| 4681581 | The <code>netq bootstrap reset purge-db</code> command might take up to 60 minutes to complete on Base Command Manager scale deployments. | 5.0.0-5.1.0 | |
| 4668341 | When you a create an LDAP server configuration, the NetQ UI incorrectly allows you to modify the default server ports. Only the standard ports (389 for insecure and 636 for secure) are permitted. | 5.0.0-5.0.1 | 5.1.0|
| 4667571 | NetQ might return inconsistent results when queries use the regular expression wildcard. | 5.0.0-5.0.1 | 5.1.0|
| 4637749 | When the master node is down,  the <code>netq show status</code> command might report an incorrect status. | 5.0.0-5.0.1 | 5.1.0|
| 4573427 | The link health view utilization chart might display incorrect values for the top 5 links when multiple links share the same value. | 5.0.0-5.0.1 | 5.1.0|
| 4527529 | When there is a high volume of concurrent API requests to NetQ, some requests may fail. | 4.15.0-5.0.1 | 5.1.0|
| 4399074 | When connecting a switch to NMX-T or NMX-C through the service registration workflow, use either the IP address or the hostname. Using both creates duplicate registrations, and the operation does not fail as expected. | 5.0.0-5.1.0 | |
| 4100882 | When you attempt to export a file that is larger than 200MB, your browser might crash or otherwise prevent you from exporting the file. To work around this issue, use filters in the UI to decrease the size of the dataset that you intend to export. | 4.12.0-4.15.1, 5.0.0-5.1.0 | |

### Fixed Issues in 5.0.1
|  Issue ID 	|   Description	|   Affects	|
|---	        |---	        |---	    |
| 4784336 | The NetQ for NVLink deployment option is not supported in air-gapped environments. | 5.0.0 | |

## 5.0.0 Release Notes
### Open Issues in 5.0.0

|  Issue ID 	|   Description	|   Affects	|   Fixed |
|---	        |---	        |---	    |---	                |
| 4786996 | To use lifecycle management in NMC or BCM environments, you must edit the master node IP address in the configuration manager to match the cluster’s head node IP address. Use the <code>kubectl edit cm -n netq-eth netq-master-node-ip</code> command to edit the configuration. In the configuration file, change the <code>data/master_node</code> field to the cluster’s head node IP address.  | 5.0.0 | 5.1.0|
| 4784336 | The NetQ for NVLink deployment option is not supported in air-gapped environments. | 5.0.0-5.1.0 | |
| 4780773 | The NetQ for NVLink Swagger UI might incorrectly display 500 status placeholder text in example responses. | 5.0.0-5.1.0 | |
| 4693161 | In cluster and scale cluster deployments, the snapshot comparison feature may time out when comparing MAC addresses. | 5.0.0 | 5.1.0|
| 4689932, 4702436 | Node reservation for NetQ is not supported in shared multi-node clusters. To work around this issue, deploy NetQ in a dedicated single-node or three-node cluster first, and then scale the deployment by adding nodes for other applications. | 5.0.0 | 5.1.0|
| 4687477 | When you run a validation against a group of devices with specific labels, NetQ ignores any pre-configured filters. | 5.0.0-5.1.0 | |
| 4687241 | The activity log in the UI might display multiple entries with “unknown” or “anonymous” usernames.  | 5.0.0 | 5.1.0|
| 4683830 | The Cable Validation Tool might fail to load in the NetQ UI. To work around this issue,  log out of NetQ and then log back in. | 5.0.0 | 5.1.0|
| 4681581 | The <code>netq bootstrap reset purge-db</code> command might take up to 60 minutes to complete on Base Command Manager scale deployments. | 5.0.0-5.1.0 | |
| 4668341 | When you a create an LDAP server configuration, the NetQ UI incorrectly allows you to modify the default server ports. Only the standard ports (389 for insecure and 636 for secure) are permitted. | 5.0.0 | 5.1.0|
| 4667571 | NetQ might return inconsistent results when queries use the regular expression wildcard. | 5.0.0 | 5.1.0|
| 4637749 | When the master node is down,  the <code>netq show status</code> command might report an incorrect status. | 5.0.0 | 5.1.0|
| 4573427 | The link health view utilization chart might display incorrect values for the top 5 links when multiple links share the same value. | 5.0.0 | 5.1.0|
| 4527529 | When there is a high volume of concurrent API requests to NetQ, some requests may fail. | 4.15.0-5.0.0 | 5.1.0|
| 4399074 | When connecting a switch to NMX-T or NMX-C through the service registration workflow, use either the IP address or the hostname. Using both creates duplicate registrations, and the operation does not fail as expected. | 5.0.0-5.1.0 | |
| 4100882, 4119697 | When you attempt to export a file that is larger than 200MB, your browser might crash or otherwise prevent you from exporting the file. To work around this issue, use filters in the UI to decrease the size of the dataset that you intend to export. | 4.12.0-4.15.1, 5.0.0-5.1.0 | |

### Fixed Issues in 5.0.0
|  Issue ID 	|   Description	|   Affects	|
|---	        |---	        |---	    |
| 4621868 | NetQ might generate event notifications for BGP reset time changes even when no actual changes have occurred. | 4.14.0-4.15.1 | |
| 4612457 | The process monitoring dashboard may display inaccurate CPU utilization values for the NetQ agent. | 4.11.0-4.15.1 | |
| 4606694 | Switch discovery through the lifecycle management UI does not work for switch IP addresses whose last octet is 0 or 255. To work around this issue, manually add these switches to NetQ by configuring the switch to point to the OPTA IP address. | 4.15.0-4.15.1 | |
| 4572526, 4572527 | NetQ for NVLink deployments might fail in air-gapped environments. |  | |
| 4537675 | The NetQ UI might not display pagination controls for large tables with multiple entries. | 4.14.0-4.15.1 | |
| 4532058, 4526493 | When you run a validation for a past date, NetQ might display incorrect values for session counts and active links. | 4.15.0-4.15.1 | |
| 4521037 | The PTP violations summary in the UI might not render properly. To work around this issue, refresh the page in your browser. | 4.15.0-4.15.1 | |
| 4023716, 4022819, 4282514 | NetQ might display duplicate validations results. | 4.11.0-4.15.1 | |
| 3993538, 4379389 | When you re-position a card on your workbench and then manually refresh the workbench, NetQ might reposition the cards. | 4.11.0-4.15.1 | |

