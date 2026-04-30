---
title: NVIDIA NetQ 4.7 Release Notes
author: Cumulus Networks
weight: 30
product: Cumulus NetQ
version: "4.7"
toc: 1
type: rn
pdfhidden: True
---
{{<rn_xls_link dir="cumulus-netq-47" >}}
## 4.7.0 Release Notes
### Open Issues in 4.7.0

|  Issue ID 	|   Description	|   Affects	|   Fixed |
|---	        |---	        |---	    |---	                |
| 3819364 | When you attempt to delete a scheduled trace using the NetQ UI, the trace record is not deleted. | 4.7.0-4.9.0 | 4.10.0-4.15.1|
| 3739222 | The <code>opta-check</code> command does not properly validate if the required 16 CPU cores are present on the system for NetQ. The command only presents an error if there are fewer than 8 CPU cores detected. | 4.2.0-4.8.0 | 4.9.0-4.15.1|
| 3676723 | When you use the NetQ agent on a Cumulus Linux switch to export gNMI data and there is a period of inactivity in the gNMI stream, the NetQ agent service might stop. To recover from this issue, restart the service with the <code>netq config restart agent</code> command. | 4.7.0-4.8.0 | 4.9.0-4.15.1|
| 3575935 | When you upgrade to NetQ 4.7.0, configured premises names might get reset to the default name <code>OPID0</code>. | 4.7.0 | 4.8.0-4.15.1|
| 3575934 | When you upgrade to NetQ 4.7.0, the password for the <code>admin</code> user is reset to the default password. | 4.7.0 | 4.8.0-4.15.1|
| 3555031 | NetQ incorrectly reports a low health SSD event on SN5600 switches. To work around this issue, configure an event suppression rule for <code>ssdutil</code> messages from SN5600 switches in your network. | 4.7.0 | 4.8.0-4.15.1|
| 3549877 | NetQ cloud deployments might unexpectedly display validation results for checks that did not run on any nodes. | 4.6.0-4.8.0 | 4.9.0-4.15.1|
| 3530739 | Queue histogram data received from switches might encounter a delay before appearing in the NetQ UI. | 4.7.0 | 4.8.0-4.15.1|
| 3429528, 3588417 | EVPN and RoCE validation cards in the NetQ UI might not display data when Cumulus Linux switches are configured with high VNI scale. | 4.6.0-4.8.0 | 4.9.0-4.15.1|

### Fixed Issues in 4.7.0
|  Issue ID 	|   Description	|   Affects	|
|---	        |---	        |---	    |
| 3491935 | NetQ might generate continuous TCA events for the NetQ VM squashfs mounts when disk utilization TCA rules are configured for all hosts.   | 4.5.0-4.6.0 | |
| 3454057 | When you configure more than one TCA rule referencing the same TCA event type, adding additional TCA rules fails with the following message:<pre>Failed to add/update TCA http status_code: 409</pre> | 4.5.0-4.6.0 | |
| 3448057 | NetQ NTP validations will report time syncronization failures for switches running the NTP service in the default VRF. | 4.5.0-4.6.0 | |
| 3446351 | When you perform an apt upgrade from NetQ 4.5.0 to version 4.6.0, the <code>sudo apt upgrade</code> command fails with the following message: <pre>Setting up shim-signed (1.40.9+15.7-0ubuntu1) ..<br />mount: /var/lib/grub/esp: special device /dev/vda15 does not exist<br />dpkg: error processing package shim-signed (--configure):installed shim-signed package post-installation script subprocess returned error exit status 32Errors were encountered while processing:shim-signedE: Sub-process /usr/bin/dpkg returned an error code (1)</pre>To work around this issue, run the <code>sudo apt remove -y shim-signed grub-efi-amd64-bin --allow-remove-essential</code> command and rerun the <code>sudo apt upgrade</code> command. | 4.5.0-4.6.0 | |
| 3442456 | When an event notification is resolved or acknowledged, the NetQ UI might display a duplicate event with the original notification content and timestamp. | 4.2.0-4.6.0 | |
| 3436299 | RoCE validations might not display data in the NetQ UI and CLI for Cumulus Linux switches when the NVUE service is not running. This issue will resolve itself within 24 hours after the next full status update from the NetQ agent.  | 4.6.0 | |
| 3431386 | When you upgrade your NetQ VM from NetQ 4.5.0 to 4.6.0 using the <code>netq upgrade bundle</code> command, certain pods are not correctly retagged. To work around this issue, retag and restart the affected pods with the following commands for your deployment after upgrading:On-premises VMs:<pre>sudo docker tag localhost:5000/fluend-aggregator-opta:1.14.3 docker-registry:5000/fluend-aggregator-opta:1.14.3sudo docker push docker-registry:5000/fluend-aggregator-opta:1.14.3sudo kubectl get pods -n default\|grep -i fluend-aggregator-opta\|awk '{print $1}'\|xargs kubectl delete pod -n defaultsudo docker tag localhost:5000/cp-schema-registry:7.2.0 docker-registry:5000/cp-schema-registry:7.2.0sudo docker push docker-registry:5000/cp-schema-registry:7.2.0sudo kubectl get pods -n default\|grep -i cp-schema-registry\|awk '{print $1}'\|xargs kubectl delete pod -n defaultsudo docker tag localhost:5000/cp-kafka:7.2.0 docker-registry:5000/cp-kafka:7.2.0sudo docker push docker-registry:5000/cp-kafka:7.2.0sudo kubectl get pods -n default\|grep -i kafka-broker\|awk '{print $1}'\|xargs kubectl delete pod -n default</pre>Cloud VMs:<pre>sudo docker tag localhost:5000/fluend-aggregator-opta:1.14.3 docker-registry:5000/fluend-aggregator-opta:1.14.3sudo docker push docker-registry:5000/fluend-aggregator-opta:1.14.3sudo kubectl get pods -n default\|grep -i fluend-aggregator-opta\|awk '{print $1}'\|xargs kubectl delete pod -n default</pre> | 4.5.0-4.6.0 | |

