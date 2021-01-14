---
title: NVIDIA NetQ 3.3 Release Notes
author: NVIDIA/NVIDIA
weight: 30
product: Cumulus NetQ
version: "3.3"
toc: 1
type: rn
pdfhidden: True
---
<a href="/cumulus-netq-33/rn.xls"><img src="/images/xls_icon.png" height="20px" width="20px" alt="Download 3.3 Release Notes xls" /></a>&nbsp;&nbsp;&nbsp;&nbsp;<a href="/cumulus-netq-33/rn.xls">Download all 3.3 release notes as .xls</a>
## 3.3.0 Release Notes
### Open issues in 3.3.0

|  Issue ID 	|   Description	|   Affects	|   Fixed |
|---	        |---	        |---	    |---	                |
| <a name="NETQ-6640"></a> [NETQ-6640](#NETQ-6640) <a name="NETQ-6640"></a> | Infra: Rarely, after a node is restarted, Kubernetes pods do not synchronize properly and the output of `netq show opta-health` shows failures. Node operation is not functionally impacted. You can safely remove the failures by running `kubectl get pods \| grep MatchNodeSelector \| cut &#45;f1 &#45;d' ' \| xargs kubectl delete pod`. To work around the issue, do not label nodes using the API. Instead label nodes through local configuration using `kubelet flag "--node-labels"`. | 3.1.0-3.3.0 | |
| <a name="NETQ-5737"></a> [NETQ-5737](#NETQ-5737) <a name="NETQ-5737"></a> | UI: Warnings might appear during the post-upgrade phase for a Cumulus Linux switch upgrade job. They are caused by services that have not yet been restored by the time the job is complete. Cumulus Networks recommend waiting five minutes, creating a network snapshot, then comparing that to the pre-upgrade snapshot. If the comparison shows no differences for the services, the warnings can be ignored. If there are differences, then troubleshooting the relevant service(s) is recommended. | 3.0.0-3.3.0 | |
| <a name="NETQ-5571"></a> [NETQ-5571](#NETQ-5571) <a name="NETQ-5571"></a> | UI: The legend and segment colors on Switches and Upgrade History card graphs sometimes do not match. These cards appear on the lifecycle management dashboard (Manage Switch Assets view). Hover over graph to view the correct values. | 3.0.0-3.3.0 | |
| <a name="NETQ-3451"></a> [NETQ-3451](#NETQ-3451) <a name="NETQ-3451"></a> | UI: If either the peer_hostname or the peer_asn is invalid, the full screen BGP Service card does not provide the ability to open cards for a selected BGP session. | 2.3.0-2.4.1, 3.0.0-3.3.0 | |

### Fixed Issues in 3.3.0
|  Issue ID 	|   Description	|   Affects	|
|---	        |---	        |---	    |
| <a name="NETQ-5529"></a> [NETQ-5529](#NETQ-5529) | UI: Snapshot comparison cards may not render correctly after navigating away from a workbench and then returning to it. If you are viewing the Snapshot comparison card(s) on a custom workbench, refresh the page to reload the data. If you are viewing it on the Cumulus Default workbench, after refreshing the page you must recreate the comparison(s). | 2.4.0-3.2.1 | |

