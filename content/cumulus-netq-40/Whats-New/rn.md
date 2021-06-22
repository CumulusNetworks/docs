---
title: NVIDIA Cumulus NetQ 4.0 Release Notes
author: NVIDIA
weight: 30
product: Cumulus NetQ
version: "4.0"
toc: 1
type: rn
pdfhidden: True
---
<a href="/cumulus-netq-40/rn.xls"> {{<rn_icon alt="Download 4.0 Release Notes xls" >}}</a>&nbsp;&nbsp;&nbsp;&nbsp;<a href="/cumulus-netq-40/rn.xls">Download all 4.0 release notes as .xls</a>

## 4.0 Release Notes

### Open Issues in 4.0.0

|  Issue ID 	|   Description	|   Affects	|   Fixed |
|---	        |---	        |---	    |---	                |
| <a name="NETQ-3451"></a> [NETQ-3451](#NETQ-3451) <a name="NETQ-3451"></a> <br /> | UI: If either the peer_hostname or the peer_asn is invalid, the full screen BGP Service card does not provide the ability to open cards for a selected BGP session. | 2.3.0-2.4.1, 3.0.0-3.3.1, 4.0.0 | |
| <a name="2549649"></a> [2549649](#2549649) <a name="2549649"></a> <br />NETQ-5737 | NetQ UI: Warnings might appear during the post-upgrade phase for a Cumulus Linux switch upgrade job. They are caused by services that have not yet been restored by the time the job is complete. Cumulus Networks recommend waiting five minutes, creating a network snapshot, then comparing that to the pre-upgrade snapshot. If the comparison shows no differences for the services, the warnings can be ignored. If there are differences, then troubleshooting the relevant service(s) is recommended. | 3.0.0-3.3.1, 4.0.0 | |
| <a name="2551545"></a> [2551545](#2551545) <a name="2551545"></a> <br />NETQ-6640 | Infra: Rarely, after a node is restarted, Kubernetes pods do not synchronize properly and the output of <code>netq show opta-health</code> shows failures. Node operation is not functionally impacted. You can safely remove the failures by running <code>kubectl get pods \| grep MatchNodeSelector \| cut \-f1 \-d' ' \| xargs kubectl delete pod</code>. To work around the issue, do not label nodes using the API. Instead label nodes through local configuration using <code>kubelet flag "--node-labels"</code>. | 3.1.0-3.3.1, 4.0.0 | |
| <a name="2555197"></a> [2555197](#2555197) <a name="2555197"></a> <br />NETQ-7966 | NetQ CLI: Occasionally, when a command response contains a large number of objects to be displayed the NetQ CLI does not display all results in the console. When this occurs, view all results using the <code>json</code> format option. | 3.3.0-3.3.1, 4.0.0 | |
| <a name="2555854"></a> [2555854](#2555854) <a name="2555854"></a> <br />NETQ-8245 | NetQ Agent: If a NetQ Agent is downgraded to the 3.0.0 version from any higher release, the default commands file present in the _/etc/netq/commands/_ also needs to be updated to prevent the NetQ Agent from becoming rotten. | 3.0.0-3.3.1, 4.0.0 | |
| <a name="2556339"></a> [2556339](#2556339) <a name="2556339"></a> <br />NETQ-8452 | Multiple CLI commands execution simultaneously fails | 3.3.0-3.3.1, 4.0.0 | |
| <a name="2661988"></a> [2661988](#2661988) <a name="2661988"></a> | Rerunning a validation in the UI or the CLI can return the same error if the query includes special characters, such as **+** or **:**. | 4.0.0 | |
| <a name="2663274"></a> [2663274](#2663274) <a name="2663274"></a> | You cannot set a validation filter for sensor validations. | 4.0.0 | |
| <a name="2663534"></a> [2663534](#2663534) <a name="2663534"></a> | Validation check filtering is only applied to errors in validation results and is not applied to warnings in validation results. | 4.0.0 | |
| <a name="2690469"></a> [2690469](#2690469) <a name="2690469"></a> | While upgrading an on-premises deployment from version 2.4.x to 3.x.y then to 4.x, the upgrade fails during the NetQ application stage.<br /><br />To work around this issue, run the following command on the NetQ telemetry server, then start the upgrade again:<br /><pre>netq install opta activate-job config-key EhVuZXRxLWVuZHBvaW50LWdhdGV3YXkYsagDIiw3T2sweW9kR3Y4Wk9sTHU3MkwrQTRjNkhhQkU3bVpBNVlZVjEvWWgyZGJBPQ==</pre> | 4.0.0 | |

### Fixed Issues in 4.0.0

|  Issue ID 	|   Description	|   Affects	|
|---	        |---	        |---	    |
| <a name="2549319"></a> [2549319](#2549319) <a name="2549319"></a> <br />NETQ-5571 | NetQ UI: The legend and segment colors on Switches and Upgrade History card graphs sometimes do not match. These cards appear on the lifecycle management dashboard (Manage Switch Assets view). Hover over graph to view the correct values. | 3.0.0-3.3.1 |
| <a name="2553453"></a> [2553453](#2553453) <a name="2553453"></a> <br />NETQ-7318 | The <code>netqd</code> daemon logs a traceback to _/var/log/netqd.log_ when the OPTA server is unreachable and <code>netq show</code> commands are run. | 3.1.0-3.3.1 |
| <a name="2611898"></a> [2611898](#2611898) <a name="2611898"></a> | Fixed an issue where deleting a snapshot does not remove the snapshot card from the workbench. However, the workbench might refresh before the deleted snapshot’s card is removed. During the refresh, you may notice a brief flashing. This is expected behavior and you can safely ignore the flashing. | 4.0.0 |
