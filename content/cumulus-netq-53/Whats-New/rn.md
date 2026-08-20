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
| 4867933 | Threshold-crossing events created before version 5.1.0 may not display event values correctly after you upgrade NetQ. | 5.1.0-5.3.0 | |
| 4687477 | When you run a validation against a group of devices with specific labels, NetQ ignores any pre-configured filters. | 5.0.0-5.3.0 | |
| 4681581 | The <code>netq bootstrap reset purge-db</code> command might take up to 60 minutes to complete on Base Command Manager scale deployments. | 5.0.0-5.3.0 | |
| 4399074 | When connecting a switch to NMX-T or NMX-C through the service registration workflow, use either the IP address or the hostname. Using both creates duplicate registrations, and the operation does not fail as expected. | 5.0.0-5.3.0 | |
| 4100882, 4119697 | When you attempt to export a file that is larger than 200MB, your browser might crash or otherwise prevent you from exporting the file. To work around this issue, use filters in the UI to decrease the size of the dataset that you intend to export. | 4.12.0-4.15.1, 5.0.0-5.16.5 | |

### Fixed Issues in 5.3.0
|  Issue ID 	|   Description	|   Affects	|
|---	        |---	        |---	    |

