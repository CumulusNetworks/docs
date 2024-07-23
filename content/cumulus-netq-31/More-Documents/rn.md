---
title: Cumulus NetQ 3.1 Release Notes
author: Cumulus Networks
weight: 652
product: Cumulus NetQ
version: "3.1"
toc: 1
type: rn
pdfhidden: True
---
{{<rn_xls_link dir="cumulus-netq-31" >}}
## 3.1.0 Release Notes
### Open Issues in 3.1.0

|  Issue ID 	|   Description	|   Affects	|   Fixed |
|---	        |---	        |---	    |---	                |
| <a name="2893000"></a> [2893000](#2893000) <a name="2893000"></a> <br /> | CVE-2021-44228: Apache Log4j2 <=2.14.1 JNDI features used in configuration, log messages, and parameters do not protect against attacker controlled LDAP and other JNDI related endpoints. | 2.4.0-4.0.1 | 4.1.0-4.10.1|
| <a name="2553453"></a> [2553453](#2553453) <a name="2553453"></a> <br />NETQ-7318 | The <code>netqd</code> daemon logs a traceback to _/var/log/netqd.log_ when the OPTA server is unreachable and <code>netq show</code> commands are run. | 3.1.0-3.3.1 | 4.0.0-4.10.1|
| <a name="2551790"></a> [2551790](#2551790) <a name="2551790"></a> <br />NETQ-6732 | CLI: Upgrade to NetQ 3.1.0 using the CLI fails due to an authentication issue. To work around this issue, run the <code>netq bootstrap master upgrade</code> command as usual, then use the Admin UI to complete the upgrade at _https://\<netq-appl-vm-hostname-or-ipaddr\>:8443_. | 3.1.0-3.1.1 | 3.2.0-3.3.1|
| <a name="2551641"></a> [2551641](#2551641) <a name="2551641"></a> <br />NETQ-6673 | Infra: NetQ VM installation fails if the designated disk size is greater than 2TB. To work around this issue, specify the disk for cloud deployments to be between 256GB and 2TB SSD, and for on-premises deployments to be between 32 GB and 2TB. | 2.4.0-3.1.1 | 3.2.0-3.3.1|
| <a name="2551569"></a> [2551569](#2551569) <a name="2551569"></a> <br />NETQ-6650 | CLI: When a proxy server is configured for NetQ Cloud access and lifecycle management (LCM) is enabled, the associated LCM CLI commands fail due to incorrect port specification. To work around this issue, configure the NetQ Collector to connect directly to NetQ Cloud without a proxy. | 3.1.0-3.1.1 | 3.2.0-3.3.1|
| <a name="2549344"></a> [2549344](#2549344) <a name="2549344"></a> <br />NETQ-5591 | UI: The lifecycle management feature does not present general alarm or info events; however, errors related to the upgrade process are reported within the NetQ UI. | 3.0.0-3.1.1 | 3.2.0-3.3.1|
| <a name="2549319"></a> [2549319](#2549319) <a name="2549319"></a> <br />NETQ-5571 | NetQ UI: The legend and segment colors on Switches and Upgrade History card graphs sometimes do not match. These cards appear on the lifecycle management dashboard (Manage Switch Assets view). Hover over graph to view the correct values. | 3.0.0-3.3.1 | 4.0.0-4.10.1|
| <a name="2549246"></a> [2549246](#2549246) <a name="2549246"></a> <br />NETQ-5529 | NetQ UI: Snapshot comparison cards may not render correctly after navigating away from a workbench and then returning to it. If you are viewing the Snapshot comparison card(s) on a custom workbench, refresh the page to reload the data. If you are viewing it on the Cumulus Default workbench, after refreshing the page you must recreate the comparison(s). | 2.4.0-3.2.1 | 3.3.0-3.3.1|

### Fixed Issues in 3.1.0
|  Issue ID 	|   Description	|   Affects	|
|---	        |---	        |---	    |
| <a name="2549842"></a> [2549842](#2549842) <a name="2549842"></a> <br />NETQ-5833 | Switch upgrade of Cumulus Linux in the lifecycle management feature fails when attempted by a user with a standard or sudo user role and custom password credentials. To work around this issue, upgrades should be performed by users with root or sudo user role and an SSH key. Optionally, upgrade using a root user role with custom password.  | 3.0.0-3.0.1 | |
| <a name="2549787"></a> [2549787](#2549787) <a name="2549787"></a> <br />NETQ-5808 | When upgrading to NetQ 3.0.0, if you are using NetQ Agent 2.3.1 or earlier and have MLAG configured, the MLAG service becomes unresponsive. To resolve this issue, upgrade your NetQ Agents to version 3.0.0. | 3.0.0-3.0.1 | |
| <a name="2549721"></a> [2549721](#2549721) <a name="2549721"></a> <br />NETQ-5774 | When installing NetQ on switches running in Cumulus Linux 3.7.x  with management VRF configured, the CLI and Agent server are configured as follows:<pre>netq config add cli server \<ipaddr\> vrf mgmtnetq config restart clinetq config add agent server \<ipaddr\> vrf mgmtnetq config restart agent</pre>This results in <code>netqd</code> running in both default and management VRF and the NetQ Agent running in default VRF. In this scenario, the NetQ Agent status is not reported correctly to the management VRF. To workaround this issue: If you have management VRF configured, run the following commands:<pre>systemctl stop netqd.servicesystemctl disable netqd.servicesystemctl enable netqd&#64;mgmt.servicesystemctl restart netqd&#64;mgmt.service</pre>If you have default VRF configured, run the following commands:<pre>systemctl stop netqd&#64;mgmt.servicesystemctl disable netqd&#64;mgmt.servicesystemctl enable netqd.servicesystemctl restart netqd.service</pre> | 3.0.0-3.0.1 | |
| <a name="2549704"></a> [2549704](#2549704) <a name="2549704"></a> <br />NETQ-5768 | When multiple premises are deployed and Cumulus Linux upgrades have been performed on switches using the lifecycle management feature, the Upgrade History card displays history for all premises rather than only those for the selected premises. | 3.0.0-3.0.1 | |
| <a name="2549682"></a> [2549682](#2549682) <a name="2549682"></a> <br />NETQ-5752 | Performing an upgrade using the lifecycle management feature fails intermittently when SSH key switch access authorization is used. To work around this issue, use basic authentication or retry an upgrade job that uses SSH key authorization. | 3.0.0-3.0.1 | |
| <a name="2547642"></a> [2547642](#2547642) <a name="2547642"></a> <br />NETQ-4927 | Admin UI: If the Master Installation phase fails during NetQ installation, refreshing the page causes the error log to be lost. On failure, download the error log, then run <code>netq bootstrap reset</code> followed by <code>netq bootstrap master interface</code> on the node before restarting the installation process. | 2.4.1-3.0.1 | |

