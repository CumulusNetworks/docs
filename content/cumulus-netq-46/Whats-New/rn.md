---
title: NVIDIA NetQ 4.6 Release Notes
author: Cumulus Networks
weight: 30
product: Cumulus NetQ
version: "4.6"
toc: 1
type: rn
pdfhidden: True
---
{{<rn_xls_link dir="cumulus-netq-46" >}}
## 4.6.0 Release Notes
### Open Issues in 4.6.0

|  Issue ID 	|   Description	|   Affects	|   Fixed |
|---	        |---	        |---	    |---	                |
| <a name="3739222"></a> [3739222](#3739222) <a name="3739222"></a> <br /> | The <code>opta-check</code> command does not properly validate if the required 16 CPU cores are present on the system for NetQ. The command only presents an error if there are fewer than 8 CPU cores detected. | 4.2.0-4.8.0 | 4.9.0-4.13.0|
| <a name="3549877"></a> [3549877](#3549877) <a name="3549877"></a> <br /> | NetQ cloud deployments might unexpectedly display validation results for checks that did not run on any nodes. | 4.6.0-4.8.0 | 4.9.0-4.13.0|
| <a name="3491935"></a> [3491935](#3491935) <a name="3491935"></a> <br /> | NetQ might generate continuous TCA events for the NetQ VM squashfs mounts when disk utilization TCA rules are configured for all hosts.   | 4.5.0-4.6.0 | 4.7.0-4.13.0|
| <a name="3454057"></a> [3454057](#3454057) <a name="3454057"></a> <br /> | When you configure more than one TCA rule referencing the same TCA event type, adding additional TCA rules fails with the following message:<pre>Failed to add/update TCA http status_code: 409</pre> | 4.5.0-4.6.0 | 4.7.0-4.13.0|
| <a name="3448057"></a> [3448057](#3448057) <a name="3448057"></a> <br /> | NetQ NTP validations will report time syncronization failures for switches running the NTP service in the default VRF. | 4.5.0-4.6.0 | 4.7.0-4.13.0|
| <a name="3446351"></a> [3446351](#3446351) <a name="3446351"></a> <br /> | When you perform an apt upgrade from NetQ 4.5.0 to version 4.6.0, the <code>sudo apt upgrade</code> command fails with the following message: <pre>Setting up shim-signed (1.40.9+15.7-0ubuntu1) ..<br />mount: /var/lib/grub/esp: special device /dev/vda15 does not exist<br />dpkg: error processing package shim-signed (--configure):installed shim-signed package post-installation script subprocess returned error exit status 32Errors were encountered while processing:shim-signedE: Sub-process /usr/bin/dpkg returned an error code (1)</pre>To work around this issue, run the <code>sudo apt remove -y shim-signed grub-efi-amd64-bin --allow-remove-essential</code> command and rerun the <code>sudo apt upgrade</code> command. | 4.5.0-4.6.0 | 4.7.0-4.13.0|
| <a name="3442456"></a> [3442456](#3442456) <a name="3442456"></a> <br /> | When an event notification is resolved or acknowledged, the NetQ UI might display a duplicate event with the original notification content and timestamp. | 4.2.0-4.6.0 | 4.7.0-4.13.0|
| <a name="3436299"></a> [3436299](#3436299) <a name="3436299"></a> <br /> | RoCE validations might not display data in the NetQ UI and CLI for Cumulus Linux switches when the NVUE service is not running. This issue will resolve itself within 24 hours after the next full status update from the NetQ agent.  | 4.6.0 | 4.7.0-4.13.0|
| <a name="3431386"></a> [3431386](#3431386) <a name="3431386"></a> <br /> | When you upgrade your NetQ VM from NetQ 4.5.0 to 4.6.0 using the <code>netq upgrade bundle</code> command, certain pods are not correctly retagged. To work around this issue, retag and restart the affected pods with the following commands for your deployment after upgrading:On-premises VMs:<pre>sudo docker tag localhost:5000/fluend-aggregator-opta:1.14.3 docker-registry:5000/fluend-aggregator-opta:1.14.3sudo docker push docker-registry:5000/fluend-aggregator-opta:1.14.3sudo kubectl get pods -n default\|grep -i fluend-aggregator-opta\|awk '{print $1}'\|xargs kubectl delete pod -n defaultsudo docker tag localhost:5000/cp-schema-registry:7.2.0 docker-registry:5000/cp-schema-registry:7.2.0sudo docker push docker-registry:5000/cp-schema-registry:7.2.0sudo kubectl get pods -n default\|grep -i cp-schema-registry\|awk '{print $1}'\|xargs kubectl delete pod -n defaultsudo docker tag localhost:5000/cp-kafka:7.2.0 docker-registry:5000/cp-kafka:7.2.0sudo docker push docker-registry:5000/cp-kafka:7.2.0sudo kubectl get pods -n default\|grep -i kafka-broker\|awk '{print $1}'\|xargs kubectl delete pod -n default</pre>Cloud VMs:<pre>sudo docker tag localhost:5000/fluend-aggregator-opta:1.14.3 docker-registry:5000/fluend-aggregator-opta:1.14.3sudo docker push docker-registry:5000/fluend-aggregator-opta:1.14.3sudo kubectl get pods -n default\|grep -i fluend-aggregator-opta\|awk '{print $1}'\|xargs kubectl delete pod -n default</pre> | 4.5.0-4.6.0 | 4.7.0-4.13.0|
| <a name="3429528"></a> [3429528](#3429528) <a name="3429528"></a> <br /> | EVPN and RoCE validation cards in the NetQ UI might not display data when Cumulus Linux switches are configured with high VNI scale. | 4.6.0-4.8.0 | 4.9.0-4.13.0|

### Fixed Issues in 4.6.0
|  Issue ID 	|   Description	|   Affects	|
|---	        |---	        |---	    |
| <a name="3438973"></a> [3438973](#3438973) <a name="3438973"></a> <br /> | When you install NetQ onto your VM, the installation fails with the following messages:<pre>05:57:33.023618: master-node-installer: Installed Debian ...	&#91; FAILED &#93;--------------------------------------ERROR: Failed to install the master node</pre>This is due to an expired key in the installation tarball. For assistance working around this issue, contact NVIDIA support. | 4.3.0-4.5.0 | |
| <a name="3395385"></a> [3395385](#3395385) <a name="3395385"></a> <br /> | When you use NetQ LCM to upgrade a Cumulus Linux switch in an MLAG pair, the upgrade might fail. | 4.4.1-4.5.0 | |
| <a name="3367267"></a> [3367267](#3367267) <a name="3367267"></a> <br /> | When you upgrade a switch with NetQ LCM using the <code>root</code> user, the upgrade fails with the following message: <pre> Destination /home/root does not exist. </pre> To work around this issue, perform the upgrade using a different user account. | 4.5.0 | |
| <a name="3362224"></a> [3362224](#3362224) <a name="3362224"></a> <br /> | When you configure a new access profile with SSH authentication using the CLI, the command fails with the following log message:<pre>Expecting value: line 1 column 1 (char 0) </pre>To work around this issue, use the NetQ UI to configure the access profile. | 4.5.0 | |
| <a name="3360627"></a> [3360627](#3360627) <a name="3360627"></a> <br /> | When the switch RoCE egress pool buffer limit is configured as unlimited, the maximum buffer usage for RoCE counters might display incorrect values in the NetQ UI. | 4.4.1-4.5.0 | |

