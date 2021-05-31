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
| <a name="2661988"></a> [2661988](#2661988) <a name="2661988"></a> | Rerunning a validation in the UI or the CLI can return the same error if the query includes special characters, such as **+** or **:**. | 4.0.0 | |
| <a name="2663534"></a> [2663534](#2663534) <a name="2663534"></a> | Validation check filtering is only applied to errors in validation results and is not applied to warnings in validation results. | 4.0.0 | |
| <a name="2663274"></a> [2663274](#2663274) <a name="2663274"></a> | You cannot set a validation filter for sensor validations. | 4.0.0 | |

### Fixed Issues in 4.0.0

|  Issue ID 	|   Description	|   Affects	|
|---	        |---	        |---	    |
| <a name="2549319"></a> [2549319](#2549319) <a name="2549319"></a> <br />NETQ-5571 | NetQ UI: The legend and segment colors on Switches and Upgrade History card graphs sometimes do not match. These cards appear on the lifecycle management dashboard (Manage Switch Assets view). Hover over graph to view the correct values. | 3.0.0-3.3.1 |
| <a name="2553453"></a> [2553453](#2553453) <a name="2553453"></a> <br />NETQ-7318 | The <code>netqd</code> daemon logs a traceback to _/var/log/netqd.log_ when the OPTA server is unreachable and <code>netq show</code> commands are run. | 3.1.0-3.3.1 |
| <a name="2611898"></a> [2611898](#2611898) <a name="2611898"></a> | Fixed an issue where deleting a snapshot does not remove the snapshot card from the workbench. However, the workbench might refresh before the deleted snapshot’s card is removed. During the refresh, you may notice a brief flashing. This is expected behavior and you can safely ignore the flashing. | 4.0.0 |
