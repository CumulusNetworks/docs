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
{{<rn_xls_link dir="cumulus-netq-51" >}}
## 5.1.0 Release Notes
### Open Issues in 5.1.0

|  Issue ID 	|   Description	|   Affects	|   Fixed |
|---	        |---	        |---	    |---	                |
| 4977619 | NetQ might fail to load in high-availability (HA) scale deployments when ECMP is enabled. To work around this issue, disable ECMP ingestion by updating the Kafka connector configuration:<ol><li>Create a backup of the current configuration:<br><code>kubectl get kafkaconnector cassandra-sink-group-1 -n netq-infra -o yaml > /tmp/cassandra-sink-group-1.backup.yaml</code></li><li>Capture the current Kafka connector values:<pre>OLD_KCQL=$(kubectl get kafkaconnector cassandra-sink-group-1 -n netq-infra -o jsonpath='{.spec.config.connect.cassandra.kcql}')<br>OLD_TOPICS=$(kubectl get kafkaconnector cassandra-sink-group-1 -n netq-infra -o jsonpath='{.spec.config.topics}')</pre></li><li>Remove ECMP-related entries from KCQL and topics:<pre>NEW_KCQL=$(echo "$OLD_KCQL" \| tr ';' '\n' \| grep -v -E 'INTO ecmp_info SELECT\|INTO ecmp_info_aggregate SELECT\|INTO ecmp_info_group_aggregate SELECT' \| paste -sd ';' -)<br>NEW_TOPICS=$(echo "$OLD_TOPICS" \| tr ',' '\n' \| grep -v -E '^netq_obj_ecmp_info$\|^netq_obj_ecmp_info_aggregate$\|^netq_obj_ecmp_info_group_aggregate$' \| paste -sd ',' -)</pre></li><li>Verify the changes before applying them:<pre>echo "=== KCQL ECMP entries remaining (should only show ecmp_hash + arEcmpInfo) ==="<br>echo "$NEW_KCQL" \| tr ';' '\n' \| grep -i ecmpecho "=== TOPICS ECMP entries remaining (should only show netq_obj_ecmp_hash) ==="<br>echo "$NEW_TOPICS" \| tr ',' '\n' \| grep -i ecmp<br>echo "Old KCQL: $(echo "$OLD_KCQL" \| tr ';' '\n' \| wc -l) / New: $(echo "$NEW_KCQL" \| tr ';' '\n' \| wc -l) (-3)"<br>echo "Old TOPICS: $(echo "$OLD_TOPICS" \| tr ',' '\n' \| wc -l) / New: $(echo "$NEW_TOPICS" \| tr ',' '\n' \| wc -l) (-3)"<br></pre></li><li>Apply the updated configuration:<br><code>kubectl patch kafkaconnector cassandra-sink-group-1 -n netq-infra --type=merge -p "$(jq -n --arg k "$NEW_KCQL" --arg t "$NEW_TOPICS" '{spec:{config:{"connect.cassandra.kcql":$k,"topics":$t&#125;&#125;&#125;')"</code></li></ol>To revert the changes, restore the backup with <code>kubectl apply -f /tmp/cassandra-sink-group-1.backup.yaml</code><br /> | 5.1.0 | |
| 4867933 | Threshold-crossing events created before version 5.1.0 may not display event values correctly after you upgrade NetQ. | 5.1.0 | |
| 4854041 | When you upgrade a NetQ for NVLink and Ethernet deployment using the data backup and restoration workflow, NetQ does not preserve NVLink data. | 5.1.0 | |
| 4839716 | You cannot perform lifecycle management operations immediately after backing up an HA scale cluster deployment. To work around this issue, wait several hours before initiating LCM operations. | 5.1.0 | |
| 4794266 | Power sensor (PSU) events might show inconsistent sensor names. Additionally, NetQ might not generate PSU events reliably. | 5.1.0 | |
| 4784336 | The NetQ for NVLink deployment option is not supported in air-gapped environments. | 5.0.0-5.1.0 | |
| 4687477 | When you run a validation against a group of devices with specific labels, NetQ ignores any pre-configured filters. | 5.0.0-5.1.0 | |
| 4681581 | The <code>netq bootstrap reset purge-db</code> command might take up to 60 minutes to complete on Base Command Manager scale deployments. | 5.0.0-5.1.0 | |
| 4399074 | When connecting a switch to NMX-T or NMX-C through the service registration workflow, use either the IP address or the hostname. Using both creates duplicate registrations, and the operation does not fail as expected. | 5.0.0-5.1.0 | |
| 4100882 | When you attempt to export a file that is larger than 200MB, your browser might crash or otherwise prevent you from exporting the file. To work around this issue, use filters in the UI to decrease the size of the dataset that you intend to export. | 4.12.0-4.15.1, 5.0.0-5.1.0 | |

### Fixed Issues in 5.1.0
|  Issue ID 	|   Description	|   Affects	|
|---	        |---	        |---	    |
| 4786996 | To use lifecycle management in NMC or BCM environments, you must edit the master node IP address in the configuration manager to match the cluster’s head node IP address. Use the <code>kubectl edit cm -n netq-eth netq-master-node-ip</code> command to edit the configuration. In the configuration file, change the <code>data/master_node</code> field to the cluster’s head node IP address.  | 5.0.0 | |
| 4693161 | In cluster and scale cluster deployments, the snapshot comparison feature may time out when comparing MAC addresses. | 5.0.0 | |
| 4689932 | Node reservation for NetQ is not supported in shared multi-node clusters. To work around this issue, deploy NetQ in a dedicated single-node or three-node cluster first, and then scale the deployment by adding nodes for other applications. | 5.0.0 | |
| 4687241 | The activity log in the UI might display multiple entries with “unknown” or “anonymous” usernames.  | 5.0.0 | |
| 4683830 | The Cable Validation Tool might fail to load in the NetQ UI. To work around this issue,  log out of NetQ and then log back in. | 5.0.0 | |
| 4668341 | When you a create an LDAP server configuration, the NetQ UI incorrectly allows you to modify the default server ports. Only the standard ports (389 for insecure and 636 for secure) are permitted. | 5.0.0 | |
| 4667571 | NetQ might return inconsistent results when queries use the regular expression wildcard. | 5.0.0 | |
| 4637749 | When the master node is down,  the <code>netq show status</code> command might report an incorrect status. | 5.0.0 | |
| 4573427 | The link health view utilization chart might display incorrect values for the top 5 links when multiple links share the same value. | 5.0.0 | |
| 4527529 | When there is a high volume of concurrent API requests to NetQ, some requests may fail. | 4.15.0-5.0.0 | |

