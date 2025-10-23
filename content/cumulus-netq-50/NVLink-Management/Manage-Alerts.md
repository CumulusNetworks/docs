---
title: Manage Alerts
author: NVIDIA
weight: 850
toc: 4
---

NMX-M continuously gathers metrics from telemetry services. When specific thresholds defined by alert rules are exceeded, the system generates events and sends them to the webhook URL that was {{<link title="Install NetQ NVLink" text="configured during the initial installation">}}. Some alerts detail exact events, such as a port-down occurrence, while others highlight trends, like deteriorating port health. 

All triggering conditions are preconfigured and cannot be modified.

## Supported Rules

The *port status* alert is triggered by a group of events that affect port operation. These alerts are based on deviations in a group of metrics---if any metric exceeds two standard deviations from the average, an alert is raised. The alert includes the port ID, domain, node ID, and port number.

There are two types of alerts in this group---ongoing port validations and anomaly detection:

### Ongoing Port Validation
- Trigger condition: More than 3 errors of a specific metric are detected within a 24-hour window.
  - Behavior: The alert is sent continuously until the condition is resolved. This ensures that external systems receive the alert even if temporarily down.
  - Alert group: `ongoing_port_validation`
  - Alert name: `OngoingPortValidation`
  - Severity: `warning`

### Anomaly Detection

For each new metric value, NMX-M analyzes historical data over a predefined time period using a statistical model. If the value deviates significantly from the expected range (beyond two standard deviations), the system triggers an alert.  The following alerts are included:

- Port Congestion Warning
  - Alert group: `port_metrics_deviation`
  - Alert name: `PortCongestion`
  - Severity: `warning`

- Physical Layer Retransmission Warning
  - Alert group: `port_metrics_deviation`
  - Alert name: `PhysicalLayerRetransmission`
  - Severity: `warning`

- Port Degradation Warning
  - Alert group: `port_metrics_deviation`
  - Alert names:
    - `PortDegradationHistogram1`
    - `PortDegradationHistogram2`
    - `PortDegradationHistogram3`
    - `PortDegradationBER`
    - `PortDegradationLinkErrors`
  - Severity: `warning`

- Packet Discard Warning
  - Alert group: `port_metrics_deviation`
  - Alert name: `PacketDiscard`
  - Severity: `warning`



<!-- checking this with Ilia
## Update the Webhook Receiver URL

You can update the webhook URL at any time after installation.

To do so:

Create a webhook.yaml  file containing the new Alerts webhook receiver URL(s). You can provide a single URL or a comma-separated list. Example:
http://alert1.example.com:9093,http://alert2.example.com:9093/webhook
Run the following script under the root user:
/opt/nvidia/nmx/scripts/alerts-webhook-url-config.sh
When prompted, you'll see the following menu:
Choose an option:
1) Update webhook receiver URLs
2) Retrieve webhook receiver URLs and their statuses
3) Clear webhook receiver URLs
4) Exit
Enter your selection: ..
To view the current configuration, select option 2.

To update the webhook URLs, select option 1.

To clear the URLs, select option 3.

New webhook URLs will begin receiving notifications shortly after the system automatically redeploys the relevant components.
-->