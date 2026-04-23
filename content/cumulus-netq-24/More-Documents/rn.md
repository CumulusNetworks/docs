---
title: NVIDIA Cumulus NetQ 2.4 Release Notes
author: NVIDIA
weight: 30
product: Cumulus NetQ
version: "2.4"
toc: 1
type: rn
pdfhidden: True
---
{{<rn_xls_link dir="cumulus-netq-24" >}}
## 2.4.1 Release Notes
### Open Issues in 2.4.1

|  Issue ID 	|   Description	|   Affects	|   Fixed |
|---	        |---	        |---	    |---	                |
| 2551641 | Infra: NetQ VM installation fails if the designated disk size is greater than 2TB. To work around this issue, specify the disk for cloud deployments to be between 256GB and 2TB SSD, and for on-premises deployments to be between 32 GB and 2TB. | 2.4.0-3.1.1 | 3.2.0-3.3.1|
| 2549246, 2549315, 2549518, 2549315 | NetQ UI: Snapshot comparison cards may not render correctly after navigating away from a workbench and then returning to it. If you are viewing the Snapshot comparison card(s) on a custom workbench, refresh the page to reload the data. If you are viewing it on the Cumulus Default workbench, after refreshing the page you must recreate the comparison(s). | 2.4.0-3.2.1 | 3.3.0-3.3.1|
| 2548560 | When a switch or host reports its memory size in GB rather than MB, the NetQ Agent cannot parse the information and thus fails to register with the NetQ server. Contact customer support if you run into this issue. | 2.4.0-2.4.1 | 3.0.0-3.3.1|
| 2547642 | Admin UI: If the Master Installation phase fails during NetQ installation, refreshing the page causes the error log to be lost. On failure, download the error log, then run <code>netq bootstrap reset</code> followed by <code>netq bootstrap master interface</code> on the node before restarting the installation process. | 2.4.1-3.0.1 | 3.1.0-3.3.1|

### Fixed Issues in 2.4.1
|  Issue ID 	|   Description	|   Affects	|
|---	        |---	        |---	    |
| 2546397 | NetQ Admin UI: When installing NetQ with the Admin UI, the job status is presented to show progress. However, when an error is encountered while running individual tasks, the UI may feel unresponsive. Please wait for at least 15 minutes to receive a response. | 2.4.0 | |
| 2545685 | NetQ UI: On medium- and large-sized Scheduled Trace cards, the destination field does not accept IPv6 addresses. They are reported as invalid destination IP addresses. The source field on these cards accepts IPv6 addresses. | 2.3.1-2.4.0 | |
| 2545119 | NetQ UI and CLI: EVPN failure details do not appear in the full screen EVPN Service card or when running 'netq show validation results type evpn' in the NetQ CLI, even though the EVPN failure is seen on validation. | 2.3.1-2.4.0 | |

