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
| <a name="NETQ-6673"></a> [NETQ-6673](#NETQ-6673) <a name="NETQ-6673"></a> | Infra: NetQ VM installation fails if the designated disk size is greater than 2TB. To work around this issue, specify the disk for cloud deployments to be between 256GB and 2TB SSD, and for on-premises deployments to be between 32 GB and 2TB. | 2.4.0-3.1.0 | 3.2.0-3.3.0|
| <a name="NETQ-5833"></a> [NETQ-5833](#NETQ-5833) <a name="NETQ-5833"></a> | Switch upgrade of Cumulus Linux in the lifecycle management feature fails when attempted by a user with a standard or sudo user role and custom password credentials. To work around this issue, upgrades should be performed by users with root or sudo user role and an SSH key. Optionally, upgrade using a root user role with custom password.  | 3.0.0 | 3.1.0-3.3.0|
| <a name="NETQ-5808"></a> [NETQ-5808](#NETQ-5808) <a name="NETQ-5808"></a> | When upgrading to NetQ 3.0.0, if you are using NetQ Agent 2.3.1 or earlier and have MLAG configured, the MLAG service becomes unresponsive. To resolve this issue, upgrade your NetQ Agents to version 3.0.0. | 3.0.0 | 3.1.0-3.3.0|
| <a name="NETQ-5774"></a> [NETQ-5774](#NETQ-5774) <a name="NETQ-5774"></a> | When installing NetQ on switches running in Cumulus Linux 3.7.x  with management VRF configured, the CLI and Agent server are configured as follows:<br /><pre>netq config add cli server \<ipaddr\> vrf mgmt<br />netq config restart cli<br /><br />netq config add agent server \<ipaddr\> vrf mgmt<br />netq config restart agent<br /></pre><br />This results in `netqd` running in both default and management VRF and the NetQ Agent running in default VRF. In this scenario, the NetQ Agent status is not reported correctly to the management VRF. To workaround this issue: If you have management VRF configured, run the following commands:<br /><pre>systemctl stop netqd.service<br />systemctl disable netqd.service<br />systemctl enable netqd&#64;mgmt.service<br />systemctl restart netqd&#64;mgmt.service<br /></pre><br />If you have default VRF configured, run the following commands:<br /><pre>systemctl stop netqd&#64;mgmt.service<br />systemctl disable netqd&#64;mgmt.service<br />systemctl enable netqd.service<br />systemctl restart netqd.service<br /></pre><br /> | 3.0.0 | 3.1.0-3.3.0|
| <a name="NETQ-5768"></a> [NETQ-5768](#NETQ-5768) <a name="NETQ-5768"></a> | When multiple premises are deployed and Cumulus Linux upgrades have been performed on switches using the lifecycle management feature, the Upgrade History card displays history for all premises rather than only those for the selected premises. | 3.0.0 | 3.1.0-3.3.0|
| <a name="NETQ-5752"></a> [NETQ-5752](#NETQ-5752) <a name="NETQ-5752"></a> | Performing an upgrade using the lifecycle management feature fails intermittently when SSH key switch access authorization is used. To work around this issue, use basic authentication or retry an upgrade job that uses SSH key authorization. | 3.0.0 | 3.1.0-3.3.0|
| <a name="NETQ-5737"></a> [NETQ-5737](#NETQ-5737) <a name="NETQ-5737"></a> | UI: Warnings might appear during the post-upgrade phase for a Cumulus Linux switch upgrade job. They are caused by services that have not yet been restored by the time the job is complete. Cumulus Networks recommend waiting five minutes, creating a network snapshot, then comparing that to the pre-upgrade snapshot. If the comparison shows no differences for the services, the warnings can be ignored. If there are differences, then troubleshooting the relevant service(s) is recommended. | 3.0.0-3.3.0 | |
| <a name="NETQ-5591"></a> [NETQ-5591](#NETQ-5591) <a name="NETQ-5591"></a> | UI: The lifecycle management feature does not present general alarm or info events; however, errors related to the upgrade process are reported within the NetQ UI. | 3.0.0-3.1.0 | 3.2.0-3.3.0|
| <a name="NETQ-5571"></a> [NETQ-5571](#NETQ-5571) <a name="NETQ-5571"></a> | UI: The legend and segment colors on Switches and Upgrade History card graphs sometimes do not match. These cards appear on the lifecycle management dashboard (Manage Switch Assets view). Hover over graph to view the correct values. | 3.0.0-3.3.0 | |
| <a name="NETQ-5529"></a> [NETQ-5529](#NETQ-5529) <a name="NETQ-5529"></a> | UI: Snapshot comparison cards may not render correctly after navigating away from a workbench and then returning to it. If you are viewing the Snapshot comparison card(s) on a custom workbench, refresh the page to reload the data. If you are viewing it on the Cumulus Default workbench, after refreshing the page you must recreate the comparison(s). | 2.4.0-3.2.1 | 3.3.0|
| <a name="NETQ-4927"></a> [NETQ-4927](#NETQ-4927) <a name="NETQ-4927"></a> | Admin UI: If the Master Installation phase fails during NetQ installation, refreshing the page causes the error log to be lost. On failure, download the error log, then run `netq bootstrap reset` followed by `netq bootstrap master interface` on the node before restarting the installation process. | 2.4.1-3.0.0 | 3.1.0-3.3.0|
| <a name="NETQ-3451"></a> [NETQ-3451](#NETQ-3451) <a name="NETQ-3451"></a> | UI: If either the peer_hostname or the peer_asn is invalid, the full screen BGP Service card does not provide the ability to open cards for a selected BGP session. | 2.3.0-2.4.1, 3.0.0-3.3.0 | |

### Fixed Issues in 3.0.0
|  Issue ID 	|   Description	|   Affects	|
|---	        |---	        |---	    |
| <a name="NETQ-5182"></a> [NETQ-5182](#NETQ-5182) | When a switch or host reports its memory size in GB rather than MB, the NetQ Agent cannot parse the information and thus fails to register with the NetQ server. Contact customer support if you run into this issue. | 2.4.0-2.4.1 | |

