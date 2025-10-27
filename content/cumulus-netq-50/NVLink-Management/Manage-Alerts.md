---
title: Manage Alerts
author: NVIDIA
weight: 850
toc: 4
---

NetQ continuously gathers metrics from telemetry services. When specific thresholds defined by alert rules are exceeded, the system generates events and sends them to the webhook URL that was {{<link title="Install the NetQ System" text="configured during the initial installation">}}. Some alerts detail exact events, such as a port-down occurrence, while others highlight trends, like deteriorating port health. 

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
