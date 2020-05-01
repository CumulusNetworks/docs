---
title: Cumulus NetQ 3.0 Release Notes
author: Cumulus Networks
weight: 652
product: Cumulus NetQ
version: "3.0"
toc: 1
type: rn
pdfhidden: True
---
<a href="/cumulus-netq-30/rn.xls"><img src="/images/xls_icon.png" height="20px" width="20px" alt="Download 3.0 Release Notes xls" /></a>&nbsp;&nbsp;&nbsp;&nbsp;<a href="/cumulus-netq-30/rn.xls">Download all 3.0 release notes as .xls</a>
## 3.0.0 Release Notes
### Open issues in 3.0.0

|  Issue ID 	|   Description	|   Affects	|   Fixed |
|---	        |---	        |---	    |---	                |
| <a name="NETQ-5768"></a> [NETQ-5768](#NETQ-5768) <a name="NETQ-5768"></a> | When multiple premises are deployed and Cumulus Linux upgrades have been performed on switches using the lifecycle management feature, the Upgrade History card displays history for all premises rather than only those for the selected premises. | 3.0.0 | |
| <a name="NETQ-5752"></a> [NETQ-5752](#NETQ-5752) <a name="NETQ-5752"></a> | Performing an upgrade using the lifecycle management feature fails intermittently when SSH key switch access authorization is used. To work around this issue, use basic authentication or retry an upgrade job that uses SSH key authorization. | 3.0.0 | |
| <a name="NETQ-5737"></a> [NETQ-5737](#NETQ-5737) <a name="NETQ-5737"></a> | Warnings might appear during the post-upgrade phase for a Cumulus Linux switch upgrade job. They are caused by services that have not yet been restored by the time the job is complete. Cumulus Networks recommend waiting five minutes, creating a network snapshot, then comparing that to the pre-upgrade snapshot. If the comparison shows no differences for the services, the warnings can be ignored. If there are differences, then troubleshooting the relevant service(s) is recommended. | 3.0.0 | |
| <a name="NETQ-5571"></a> [NETQ-5571](#NETQ-5571) <a name="NETQ-5571"></a> | The legend and segment colors on Switches and Upgrade History card graphs sometimes do not match. These cards appear on the lifecycle management dashboard (Manage Switch Assets view). Hover over graph to view the correct values. | 3.0.0 | |
| <a name="NETQ-5529"></a> [NETQ-5529](#NETQ-5529) <a name="NETQ-5529"></a> | Snapshot comparison cards may not render correctly after navigating away from a workbench and then returning to it. If you are viewing the Snapshot comparison card(s) on a custom workbench, refresh the page to reload the data. If you are viewing it on the Cumulus Default workbench, after refreshing the page you must recreate the comparison(s). | 2.4.0, 3.0.0 | |

### Fixed issues in 3.0.0
|  Issue ID 	|   Description	|   Affects	|
|---	        |---	        |---	    |
| <a name="NETQ-5182"></a> [NETQ-5182](#NETQ-5182) | When a switch or host reports its memory size in GB rather than MB, the NetQ Agent cannot parse the information and thus fails to register with the NetQ server. Contact customer support if you run into this issue. | 2.4.0 | |

