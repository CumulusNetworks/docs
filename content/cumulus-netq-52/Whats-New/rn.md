---
title: NVIDIA NetQ 5.2 Release Notes
author: Cumulus Networks
weight: 30
product: Cumulus NetQ
version: "5.2"
toc: 1
type: rn
pdfhidden: True
---
{{<rn_xls_link dir="cumulus-netq-52" >}}
## 5.2.1 Release Notes
### Open Issues in 5.2.1

|  Issue ID 	|   Description	|   Affects	|   Fixed |
|---	        |---	        |---	    |---	                |
| 4977619 | NetQ might fail to load in high-availability (HA) scale deployments when ECMP is enabled. To work around this issue, disable ECMP ingestion by updating the Kafka connector configuration:<ol><li>Create a backup of the current configuration:<br><code>kubectl get kafkaconnector cassandra-sink-group-1 -n netq-infra -o yaml > /tmp/cassandra-sink-group-1.backup.yaml</code></li><li>Capture the current Kafka connector values:<pre>OLD_KCQL=$(kubectl get kafkaconnector cassandra-sink-group-1 -n netq-infra -o jsonpath='{.spec.config.connect.cassandra.kcql}')<br>OLD_TOPICS=$(kubectl get kafkaconnector cassandra-sink-group-1 -n netq-infra -o jsonpath='{.spec.config.topics}')</pre></li><li>Remove ECMP-related entries from KCQL and topics:<pre>NEW_KCQL=$(echo "$OLD_KCQL" \| tr ';' '\n' \| grep -v -E 'INTO ecmp_info SELECT\|INTO ecmp_info_aggregate SELECT\|INTO ecmp_info_group_aggregate SELECT' \| paste -sd ';' -)<br>NEW_TOPICS=$(echo "$OLD_TOPICS" \| tr ',' '\n' \| grep -v -E '^netq_obj_ecmp_info$\|^netq_obj_ecmp_info_aggregate$\|^netq_obj_ecmp_info_group_aggregate$' \| paste -sd ',' -)</pre></li><li>Verify the changes before applying them:<pre>echo "=== KCQL ECMP entries remaining (should only show ecmp_hash + arEcmpInfo) ==="<br>echo "$NEW_KCQL" \| tr ';' '\n' \| grep -i ecmpecho "=== TOPICS ECMP entries remaining (should only show netq_obj_ecmp_hash) ==="<br>echo "$NEW_TOPICS" \| tr ',' '\n' \| grep -i ecmp<br>echo "Old KCQL: $(echo "$OLD_KCQL" \| tr ';' '\n' \| wc -l) / New: $(echo "$NEW_KCQL" \| tr ';' '\n' \| wc -l) (-3)"<br>echo "Old TOPICS: $(echo "$OLD_TOPICS" \| tr ',' '\n' \| wc -l) / New: $(echo "$NEW_TOPICS" \| tr ',' '\n' \| wc -l) (-3)"<br></pre></li><li>Apply the updated configuration:<br><code>kubectl patch kafkaconnector cassandra-sink-group-1 -n netq-infra --type=merge -p "$(jq -n --arg k "$NEW_KCQL" --arg t "$NEW_TOPICS" '{spec:{config:{"connect.cassandra.kcql":$k,"topics":$t&#125;&#125;&#125;')"</code></li></ol>To revert the changes, restore the backup with <code>kubectl apply -f /tmp/cassandra-sink-group-1.backup.yaml</code><br /> | 5.1.0-5.2.1 | |
| 4977342, 4889408 | The NetQ UI might not display a complete list of interfaces. To work around this issue, restart the NetQ agent or upgrade to the latest NetQ version. | 5.1.0-5.2.1 | |
| 4964170 | When you create a partition, the operation might fail with a BAD_PARAM error. To work around this issue, retry the operation until it is successful.  | 5.1.0-5.2.1 | |
| 4897897 | The NetQ NVLink API might fail to return a 400 error response when unsupported parameters are included in the API request. | 5.1.0-5.2.1 | |
| 4894672, 4896363 | NVOS upgrades on switches might fail if the image filename contains spaces or special characters. | 5.1.0-5.2.1 | |
| 4890084 | The NetQ CLI might not delete threshold-crossing alerts configured for ACL resources. To work around this issue, use the UI to delete the alerts. | 5.1.0-5.2.1 | |
| 4876932 | The NMX controller service might intermittently fail to switch to an alternate out-of-band (OOB) port when the primary registration port becomes unavailable. As a result, partition management operations might not function correctly on the secondary OOB port if the registered management port goes down. | 5.1.0-5.2.1 | |
| 4867933 | Threshold-crossing events created before version 5.1.0 may not display event values correctly after you upgrade NetQ. | 5.1.0-5.2.1 | |
| 4839716, 4844441 | You cannot perform lifecycle management operations immediately after backing up an HA scale cluster deployment. To work around this issue, wait several hours before initiating LCM operations. | 5.1.0-5.2.1 | |
| 4838526 | NMX controller and telemetry services might display a DOWN status if the primary out-of-band (OOB) management port is unavailable. | 5.1.0-5.2.1 | |
| 4830357 | When you try to filter images in the NetQ UI based on image type, NetQ might ignore the filter. | 5.1.0-5.2.1 | |
| 4794266 | Power sensor (PSU) events might show inconsistent sensor names. Additionally, NetQ might not generate PSU events reliably. | 5.1.0-5.2.1 | |
| 4784336 | The NetQ for NVLink deployment option is not supported in air-gapped environments. | 5.0.0-5.2.1 | |
| 4780773 | The NetQ for NVLink Swagger UI might incorrectly display 500 status placeholder text in example responses. | 5.0.0-5.2.1 | |
| 4687477 | When you run a validation against a group of devices with specific labels, NetQ ignores any pre-configured filters. | 5.0.0-5.2.1 | |
| 4681581 | The <code>netq bootstrap reset purge-db</code> command might take up to 60 minutes to complete on Base Command Manager scale deployments. | 5.0.0-5.2.1 | |
| 4399074 | When connecting a switch to NMX-T or NMX-C through the service registration workflow, use either the IP address or the hostname. Using both creates duplicate registrations, and the operation does not fail as expected. | 5.0.0-5.2.1 | |
| 4100882, 4119697 | When you attempt to export a file that is larger than 200MB, your browser might crash or otherwise prevent you from exporting the file. To work around this issue, use filters in the UI to decrease the size of the dataset that you intend to export. | 4.12.0-4.15.1, 5.0.0-5.2.1 | |

### Fixed Issues in 5.2.1
|  Issue ID 	|   Description	|   Affects	|
|---	        |---	        |---	    |

## 5.2.0 Release Notes
### Open Issues in 5.2.0

|  Issue ID 	|   Description	|   Affects	|   Fixed |
|---	        |---	        |---	    |---	                |
| 4965251 | When BlueField DPUs are in the default, embedded mode, the output of the <code>netq check roce</code> command might produce duplicate entries for the same device (one for the host and one for the DPU). This issue can also affect the calculations for the RoCE Mode Consistency and DSCP Classification tests. Additionally, the <code>netq show roce-config host</code> command might display DPU interfaces alongside host interfaces. This issue does not affect DPUs that are configured in separated mode. | 5.2.0 | |
| 4867933 | Threshold-crossing events created before version 5.1.0 may not display event values correctly after you upgrade NetQ. | 5.1.0-5.2.0 | |
| 4784336 | The NetQ for NVLink deployment option is not supported in air-gapped environments. | 5.0.0-5.2.0 | |
| 4687477 | When you run a validation against a group of devices with specific labels, NetQ ignores any pre-configured filters. | 5.0.0-5.2.0 | |
| 4681581 | The <code>netq bootstrap reset purge-db</code> command might take up to 60 minutes to complete on Base Command Manager scale deployments. | 5.0.0-5.2.0 | |
| 4399074 | When connecting a switch to NMX-T or NMX-C through the service registration workflow, use either the IP address or the hostname. Using both creates duplicate registrations, and the operation does not fail as expected. | 5.0.0-5.2.0 | |
| 4100882, 4119697 | When you attempt to export a file that is larger than 200MB, your browser might crash or otherwise prevent you from exporting the file. To work around this issue, use filters in the UI to decrease the size of the dataset that you intend to export. | 4.12.0-4.15.1, 5.0.0-5.2.0 | |

### Fixed Issues in 5.2.0
|  Issue ID 	|   Description	|   Affects	|
|---	        |---	        |---	    |
| 4977619 | NetQ might fail to load in high-availability (HA) scale deployments when ECMP is enabled. To work around this issue, disable ECMP ingestion by updating the Kafka connector configuration:<ol><li>Create a backup of the current configuration:<br><code>kubectl get kafkaconnector cassandra-sink-group-1 -n netq-infra -o yaml > /tmp/cassandra-sink-group-1.backup.yaml</code></li><li>Capture the current Kafka connector values:<pre>OLD_KCQL=$(kubectl get kafkaconnector cassandra-sink-group-1 -n netq-infra -o jsonpath='{.spec.config.connect.cassandra.kcql}')<br>OLD_TOPICS=$(kubectl get kafkaconnector cassandra-sink-group-1 -n netq-infra -o jsonpath='{.spec.config.topics}')</pre></li><li>Remove ECMP-related entries from KCQL and topics:<pre>NEW_KCQL=$(echo "$OLD_KCQL" \| tr ';' '\n' \| grep -v -E 'INTO ecmp_info SELECT\|INTO ecmp_info_aggregate SELECT\|INTO ecmp_info_group_aggregate SELECT' \| paste -sd ';' -)<br>NEW_TOPICS=$(echo "$OLD_TOPICS" \| tr ',' '\n' \| grep -v -E '^netq_obj_ecmp_info$\|^netq_obj_ecmp_info_aggregate$\|^netq_obj_ecmp_info_group_aggregate$' \| paste -sd ',' -)</pre></li><li>Verify the changes before applying them:<pre>echo "=== KCQL ECMP entries remaining (should only show ecmp_hash + arEcmpInfo) ==="<br>echo "$NEW_KCQL" \| tr ';' '\n' \| grep -i ecmpecho "=== TOPICS ECMP entries remaining (should only show netq_obj_ecmp_hash) ==="<br>echo "$NEW_TOPICS" \| tr ',' '\n' \| grep -i ecmp<br>echo "Old KCQL: $(echo "$OLD_KCQL" \| tr ';' '\n' \| wc -l) / New: $(echo "$NEW_KCQL" \| tr ';' '\n' \| wc -l) (-3)"<br>echo "Old TOPICS: $(echo "$OLD_TOPICS" \| tr ',' '\n' \| wc -l) / New: $(echo "$NEW_TOPICS" \| tr ',' '\n' \| wc -l) (-3)"<br></pre></li><li>Apply the updated configuration:<br><code>kubectl patch kafkaconnector cassandra-sink-group-1 -n netq-infra --type=merge -p "$(jq -n --arg k "$NEW_KCQL" --arg t "$NEW_TOPICS" '{spec:{config:{"connect.cassandra.kcql":$k,"topics":$t&#125;&#125;&#125;')"</code></li></ol>To revert the changes, restore the backup with <code>kubectl apply -f /tmp/cassandra-sink-group-1.backup.yaml</code><br /> | 5.1.0 | |
| 4977342, 4889408 | The NetQ UI might not display a complete list of interfaces. To work around this issue, restart the NetQ agent or upgrade to the latest NetQ version. | 5.1.0 | |
| 4964170 | When you create a partition, the operation might fail with a BAD_PARAM error. To work around this issue, retry the operation until it is successful.  | 5.1.0 | |
| 4897897 | The NetQ NVLink API might fail to return a 400 error response when unsupported parameters are included in the API request. | 5.1.0 | |
| 4894672, 4896363 | NVOS upgrades on switches might fail if the image filename contains spaces or special characters. | 5.1.0 | |
| 4890084 | The NetQ CLI might not delete threshold-crossing alerts configured for ACL resources. To work around this issue, use the UI to delete the alerts. | 5.1.0 | |
| 4876932 | The NMX controller service might intermittently fail to switch to an alternate out-of-band (OOB) port when the primary registration port becomes unavailable. As a result, partition management operations might not function correctly on the secondary OOB port if the registered management port goes down. | 5.1.0 | |
| 4839716, 4844441 | You cannot perform lifecycle management operations immediately after backing up an HA scale cluster deployment. To work around this issue, wait several hours before initiating LCM operations. | 5.1.0 | |
| 4838526 | NMX controller and telemetry services might display a DOWN status if the primary out-of-band (OOB) management port is unavailable. | 5.1.0 | |
| 4830357 | When you try to filter images in the NetQ UI based on image type, NetQ might ignore the filter. | 5.1.0 | |
| 4794266 | Power sensor (PSU) events might show inconsistent sensor names. Additionally, NetQ might not generate PSU events reliably. | 5.1.0 | |
| 4780773 | The NetQ for NVLink Swagger UI might incorrectly display 500 status placeholder text in example responses. | 5.0.0-5.1.0 | |

