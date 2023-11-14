---
title: NVLink4
author: NVIDIA
weight: 1090
---

With NetQ, you can monitor the performance of your NVLink devices, manage NVOS upgrades, create NVLink domains, and troubleshoot issues. This section describes the NetQ integration with NVLink4.

- {{<link title="NVLink Quick Start Guide" text="NVLink quick start guide">}}: log in to NetQ and access NVLink features in the UI
- {{<link title="Domain Management" text="Domain management">}}: create and manage multiple NVLink4 domains. After you create and configure a domain, run Global Fabric Manager and start collecting telemetry data which can be visualized in the UI.
- {{<link title="NVLink4 Events" text="NVLink events">}}: monitor your NVLink devices and GFM status for errors or downtime
- {{<link title="NVLink4 Inventory" text="NVLink inventory">}}: manage your inventory of NVLink L1 and L2 switches, and view statistics and data for each device
- {{<link title="NVOS Management" text="NVOS management">}}: upload NVOS images to NetQ, then upgrade NVLink4 switches to the latest NVOS version
- {{<link title="Debugging Files" text="Debugging files">}}: download system dumps and GFM logs for troubleshooting
- {{<link title="Edit GFM Variables" text="Edit GFM variables">}}: customize your Global Fabric Manager configuration with variables unavailable in the NetQ UI
- {{<link title="Fluentd Reference" text="Fluentd message reference">}}: view NVLink4 example messages in JSON format for Fluentd collectors
- {{<exlink url="https://docs.nvidia.com/networking-ethernet-software/cumulus-netq-48/api/" text="API reference">}}: access a Swagger instance to view NVLink4 API options
 
Each NVSwitch has a designated telemetry agent embedded in NVOS. This agent fetches telemetry data and streams it to a Fluentd data collector that integrates with NetQ or a third-party client. 
 
NetQ maintains GFM processes with high availability. If the GFM process stops unexpectedly, NetQ quickly and automatically remediates issues.

