---
title: Manage Alerts
author: NVIDIA
weight: 850
toc: 4
---

NetQ continuously gathers metrics from telemetry services. When specific thresholds defined by alert rules are exceeded, the system generates events and sends them to the webhook URL that was {{<link title="Install the NetQ System" text="configured during the initial installation">}}. Some alerts detail exact events, such as a port-down occurrence, while others highlight trends, like deteriorating port health. 

All triggering conditions are preconfigured and cannot be modified.

## Ongoing Port Validation

The *port status* alert is triggered by a group of events that affect port operation. These alerts are based on deviations in a group of metrics---if any metric exceeds two standard deviations from the average, an alert is raised. The alert includes the port ID, domain, node ID, and port number.

| Alert Type | Alert Group | Alert Name(s) | Severity |
| :-- | :-- | :-- | :-- |
| Ongoing Port Validation | `ongoing_port_validation` | `OngoingPortValidation` | warning |


## Anomaly Detection

For each new metric value, NetQ analyzes historical data over a predefined time period using a statistical model. If the value deviates significantly from the expected range (beyond two standard deviations), the system triggers an alert.

| Alert Type | Alert Group | Alert Name(s) | Severity |
| :-- | :-- | :-- | :-- |
| Port Congestion Warning | `port_metrics_deviation` | `PortCongestion` | warning |
| Physical Layer Retransmission Warning | `port_metrics_deviation` | `PhysicalLayerRetransmission` | warning |
| Port Degradation Warning | `port_metrics_deviation` | `PortDegradationHistogram1`, `PortDegradationHistogram2`, `PortDegradationHistogram3`, `PortDegradationBER`, `PortDegradationLinkErrors` | warning |
| Packet Discard Warning | `port_metrics_deviation` | `PacketDiscard` | warning |

## License Expiration

NetQ broadcasts alerts when your {{<link title="Manage Licenses" text="NetQ for NVLink license">}} is expired or about to expire. To enable or disable these alerts refer to {{<link title="Manage Licenses/#manage-license-alerts" text="manage license alerts">}}.

| Alert Type | Alert Group | Alert Name(s) | Severity |
| :-- | :-- | :-- | :-- |
| Expires Soon | `licensing` | `LicenseValidation` | warning |
| Expired | `licensing` | `LicenseValidation` | critical |

<!--
## Certificate Expiration
-->

## Leak Sensor Notifications

| Alert Type | Alert Group | Alert Name(s) | Severity |
| :-- | :-- | :-- | :-- |
| Redfish event alert on a switch or GPU | `webhook-gateway` | `RedfishEventNotification` | warning/critical |
| Redfish connection status update on a switch or GPU | `oob-connectivity` | `RedfishStatusNotification` | warning/critical |


## Update the Webhook Receiver URL

You can update the webhook URL at any time after installation.

1. Create a `webhook.yaml` file that specifies the new alerts webhook receiver URL(s). You can provide a single URL or a comma-separated list of URLs.

2. Run the following script as the root user:
```
/opt/netq-admin/nvl/scripts/alerts-webhook-url-config.sh
```

3. NetQ prompts you to choose one of four options: 

- Update webhook receiver URLs
- Retrieve webhook receiver URLs and their statuses
- Clear webhook receiver URLs
- Exit

4. If you chose the first option, NetQ will automatically redeploy and apply the updated URL settings.
