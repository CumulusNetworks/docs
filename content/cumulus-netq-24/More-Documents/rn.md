---
title: Cumulus NetQ 2.4 Release Notes
author: Cumulus Networks
weight: 635
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
| <a name="2893000"></a> [2893000](#2893000) <a name="2893000"></a> <br /> | CVE-2021-44228: Apache Log4j2 <=2.14.1 JNDI features used in configuration, log messages, and parameters do not protect against attacker controlled LDAP and other JNDI related endpoints. | 2.4.0-4.0.1 | 4.1.0-4.7.0|
| <a name="2551641"></a> [2551641](#2551641) <a name="2551641"></a> <br />NETQ-6673 | Infra: NetQ VM installation fails if the designated disk size is greater than 2TB. To work around this issue, specify the disk for cloud deployments to be between 256GB and 2TB SSD, and for on-premises deployments to be between 32 GB and 2TB. | 2.4.0-3.1.1 | 3.2.0-3.3.1|
| <a name="2549246"></a> [2549246](#2549246) <a name="2549246"></a> <br />NETQ-5529 | NetQ UI: Snapshot comparison cards may not render correctly after navigating away from a workbench and then returning to it. If you are viewing the Snapshot comparison card(s) on a custom workbench, refresh the page to reload the data. If you are viewing it on the Cumulus Default workbench, after refreshing the page you must recreate the comparison(s). | 2.4.0-3.2.1 | 3.3.0-3.3.1|
| <a name="2548560"></a> [2548560](#2548560) <a name="2548560"></a> <br />NETQ-5182 | When a switch or host reports its memory size in GB rather than MB, the NetQ Agent cannot parse the information and thus fails to register with the NetQ server. Contact customer support if you run into this issue. | 2.4.0-2.4.1 | 3.0.0-3.3.1|
| <a name="2547642"></a> [2547642](#2547642) <a name="2547642"></a> <br />NETQ-4927 | Admin UI: If the Master Installation phase fails during NetQ installation, refreshing the page causes the error log to be lost. On failure, download the error log, then run <code>netq bootstrap reset</code> followed by <code>netq bootstrap master interface</code> on the node before restarting the installation process. | 2.4.1-3.0.1 | 3.1.0-3.3.1|

### Fixed Issues in 2.4.1
|  Issue ID 	|   Description	|   Affects	|
|---	        |---	        |---	    |
| <a name="2546397"></a> [2546397](#2546397) <a name="2546397"></a> <br />NETQ-4419 | NetQ Admin UI: When installing NetQ with the Admin UI, the job status is presented to show progress. However, when an error is encountered while running individual tasks, the UI may feel unresponsive. Please wait for at least 15 minutes to receive a response. | 2.4.0 | |
| <a name="2545685"></a> [2545685](#2545685) <a name="2545685"></a> <br />NETQ-4113 | NetQ UI: On medium- and large-sized Scheduled Trace cards, the destination field does not accept IPv6 addresses. They are reported as invalid destination IP addresses. The source field on these cards accepts IPv6 addresses. | 2.3.1-2.4.0 | |
| <a name="2545119"></a> [2545119](#2545119) <a name="2545119"></a> <br />NETQ-3916 | NetQ UI and CLI: EVPN failure details do not appear in the full screen EVPN Service card or when running 'netq show validation results type evpn' in the NetQ CLI, even though the EVPN failure is seen on validation. | 2.3.1-2.4.0 | |

## 2.4.0 Release Notes
### Open Issues in 2.4.0

|  Issue ID 	|   Description	|   Affects	|   Fixed |
|---	        |---	        |---	    |---	                |
| <a name="2893000"></a> [2893000](#2893000) <a name="2893000"></a> <br /> | CVE-2021-44228: Apache Log4j2 <=2.14.1 JNDI features used in configuration, log messages, and parameters do not protect against attacker controlled LDAP and other JNDI related endpoints. | 2.4.0-4.0.1 | 4.1.0-4.7.0|
| <a name="2551641"></a> [2551641](#2551641) <a name="2551641"></a> <br />NETQ-6673 | Infra: NetQ VM installation fails if the designated disk size is greater than 2TB. To work around this issue, specify the disk for cloud deployments to be between 256GB and 2TB SSD, and for on-premises deployments to be between 32 GB and 2TB. | 2.4.0-3.1.1 | 3.2.0-3.3.1|
| <a name="2549246"></a> [2549246](#2549246) <a name="2549246"></a> <br />NETQ-5529 | NetQ UI: Snapshot comparison cards may not render correctly after navigating away from a workbench and then returning to it. If you are viewing the Snapshot comparison card(s) on a custom workbench, refresh the page to reload the data. If you are viewing it on the Cumulus Default workbench, after refreshing the page you must recreate the comparison(s). | 2.4.0-3.2.1 | 3.3.0-3.3.1|
| <a name="2548560"></a> [2548560](#2548560) <a name="2548560"></a> <br />NETQ-5182 | When a switch or host reports its memory size in GB rather than MB, the NetQ Agent cannot parse the information and thus fails to register with the NetQ server. Contact customer support if you run into this issue. | 2.4.0-2.4.1 | 3.0.0-3.3.1|
| <a name="2546397"></a> [2546397](#2546397) <a name="2546397"></a> <br />NETQ-4419 | NetQ Admin UI: When installing NetQ with the Admin UI, the job status is presented to show progress. However, when an error is encountered while running individual tasks, the UI may feel unresponsive. Please wait for at least 15 minutes to receive a response. | 2.4.0 | 2.4.1|
| <a name="2545685"></a> [2545685](#2545685) <a name="2545685"></a> <br />NETQ-4113 | NetQ UI: On medium- and large-sized Scheduled Trace cards, the destination field does not accept IPv6 addresses. They are reported as invalid destination IP addresses. The source field on these cards accepts IPv6 addresses. | 2.3.1-2.4.0 | 2.4.1|
| <a name="2545119"></a> [2545119](#2545119) <a name="2545119"></a> <br />NETQ-3916 | NetQ UI and CLI: EVPN failure details do not appear in the full screen EVPN Service card or when running 'netq show validation results type evpn' in the NetQ CLI, even though the EVPN failure is seen on validation. | 2.3.1-2.4.0 | 2.4.1|

### Fixed Issues in 2.4.0
|  Issue ID 	|   Description	|   Affects	|
|---	        |---	        |---	    |
| <a name="2545622"></a> [2545622](#2545622) <a name="2545622"></a> <br />NETQ-4100 | NetQ UI: This only applies to the NetQ 2.3.1 UI installed on the NetQ Server or NetQ Appliance in on-premises deployments. Cloud deployments are not impacted by this bug. Trace results are not shown after running an on-demand or scheduled trace request in the NetQ UI. The medium Trace Result cards are blank whether the trace was successful or not. The full-screen Trace Result card and the NetQ CLI show the results correctly<br />To work around this issue, apply the update to your existing 2.3.1 build as follows:* Download the update tarball<br />If your server or appliance has internet access, use <code>wget</code> to perform the download. Be sure to use your download directory in place of _/home/cumulus_ indicated in this example<br /><pre>cumulus&#64;opta:~$ wget http://netq-shared.s3-us-west-2.amazonaws.com/NetQ-2.3.1.1.tgz -O /home/cumulus/NetQ-2.3.1.1.tgz</pre>If your server or appliance is air-gapped, first download the tarball and then, as a root user, copy it to the appropriate directory on your server or appliance<br /><pre>root&#64;opta:~# cd /mnt/swinstalls/root&#64;opta:/mnt/swinstalls# cp /home/cumulus/NetQ-2.3.1.1.tgz ./ </pre>* Extract the script<br /><pre>cumulus&#64;opta:~$ tar -xvzf /home/cumulus/NetQ-2.3.1.1.tgz update-app.sh</pre>* Run the script. On completion, a new GUI container will be running and the card will display the trace result<br /><pre>cumulus&#64;opta:~$ ./update-app.sh /home/cumulus/NetQ-2.3.1.1.tgzLoading the new appe9b2c1648ab5: Loading layer &#91;==================================================>&#93;  2.048kB/2.048kBe7acfa3378f4: Loading layer &#91;==================================================>&#93;  20.59MB/20.59MB..<br />Loaded image: 498186410471.dkr.ecr.us-west-2.amazonaws.com/netq-gui:2.3.1Restarting the app with new imagedeployment.extensions/netq-gui-deploy scaledSleeping for 15 secondsConfirming the app is running with new imageFound the container running with new image<br /></pre>* Close and reopen the NetQ UI to run the new image. *Note*: You may need to press Cmd+Shift+R to fully clear the cache on the Chrome browser. |  | |
| <a name="2545549"></a> [2545549](#2545549) <a name="2545549"></a> <br />NETQ-4080 | When you upgrade both the NetQ Agent and the NetQ Apps in on-premises deployments, a temporary increase in event messages is seen. They are the result of collecting package information from the NetQ Agent on each monitored node. This only happens on initial upgrade and there is no functional impact to the operation of the NetQ software. | 2.3.1 | |
| <a name="2545296"></a> [2545296](#2545296) <a name="2545296"></a> <br />NETQ-3993 | NetQ UI: When a warning occurs during a VXLAN validation, the small, medium, and large VXLAN Scheduled Validation Result cards incorrectly display the text of the warning instead of the Failed icon and text. | 2.3.1 | |
| <a name="2545113"></a> [2545113](#2545113) <a name="2545113"></a> <br />NETQ-3915 | NetQ UI: When troubleshooting a user may wish to disable auto-refresh so that the data is not changed in the middle of analysis. If auto-refresh causes any state loss on the card of interest, pause the auto-refresh feature by clicking the Refresh icon in the workbench header. When finished with the analysis, re-enable the auto-refresh feature by clicking the Refresh icon again to ensure the card data is always the most recent available. | 2.3.1 | |
| <a name="2543333"></a> [2543333](#2543333) <a name="2543333"></a> <br />NETQ-3255 | NetQ UI: Trace configuration information is not captured until the trace has been run at least once, leaving the large Trace Result card blank. The schedule information remains missing even after the trace has been run. | 2.2.2-2.3.1 | |

