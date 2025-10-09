---
title: NVLink4 Overview
author: NVIDIA
weight: 1150
toc: 3
bookhidden: true
---

This section describes the NetQ integration with NVLink4. This integration supports the following:


 - {{<link title="NVLink4 Domain Management" text="Domain management">}}: create and manage multiple NVLink4 domains. After you create and configure a domain, run Global Fabric Manager (GFM) to collect telemetry data which can be visualized in the UI.
 - {{<link title="NVLink4 Inventory Management" text="Inventory management">}}: manage your inventory of NVLink4 switches and GPU nodes, and view statistics and data for each device.
 - {{<exlink url="https://docs.nvidia.com/networking-ethernet-software/cumulus-netq-43/api/index.html" text="API reference">}}: access a Swagger instance to view NVLink4 API options.
  - {{<link title="NVLink4 Fluentd Reference" text="Fluentd message reference">}}: example NVLink4 messages in JSON format for fluentd collectors.

 Each GPU node and NVSwitch has a designated telemetry agent embedded in NVOS. This agent fetches telemetry data and streams it to a Fluentd data collector that integrates with NetQ or a third-party client. 
 
 Additionally, NetQ maintains GFM processes with high availability. If the GFM process stops unexpectedly, NetQ quickly and automatically remediates issues.

 To get started, {{<link title="NVLink4 Installation Management" text="install NetQ">}}.

 Refer to the {{<link title="NVLink4 Glossary" text="glossary">}} for additional reference materials.