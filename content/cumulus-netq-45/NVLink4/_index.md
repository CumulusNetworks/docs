---
title: NVLink4
author: NVIDIA
weight: 1090
---

This section describes the NetQ integration with NVLink4. This integration supports the following:


 - {{<exlink url="https://nvlink4-netq.d1pzhbszsr62xj.amplifyapp.com/networking-ethernet-software/cumulus-netq-45/api/index.html" text="API reference">}}: access a Swagger instance to view NVLink4 API options.
 - {{<link title="Fluentd Reference" text="Fluentd message reference">}}: view NVLink4 example messages in JSON format for Fluentd collectors.

You can also manage NVLink4 devices and NVOS upgrades via the NetQ UI:

- {{<link title="Domain Management" text="Domain management">}}: create and manage multiple NVLink4 domains. After you create and configure a domain, run Global Fabric Manager (GFM), then collect telemetry data which can be visualized in the UI.
- {{<link title="NVLink4 Inventory" text="Inventory management">}}: manage your inventory of NVLink4 switches and GPU nodes, and view statistics and data for each device.
- {{<link title="NVOS Images" text="NVOS image management">}}: check for missing images and upload NVOS images.
- {{<link title="Upgrade NVOS with LCM" text="NVOS upgrades">}}: upgrade NVLink4 switches and GPU nodes to the latest NVOS version.
 

 Each GPU node and NVSwitch has a designated telemetry agent embedded in NVOS. This agent fetches telemetry data and streams it to a Fluentd data collector that integrates with NetQ and/or a third-party client. 
 
 Additionally, NetQ maintains GFM processes with high availability. If the GFM process stops unexpectedly, NetQ quickly and automatically remediates issues.

 To get started, {{<link title="Deployment Guide" text="install NetQ">}}.

 Refer to the {{<link title="NVLink4 Glossary" text="glossary">}} for additional reference materials.