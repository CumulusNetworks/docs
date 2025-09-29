---
title: Cable Validations
author: NVIDIA
weight: 1105
toc: 3
---

Launch the cable validation tool from within NetQ to validate layer 1 physical links and connections in your clustered network environments. The tool can detect a range of network cabling issues, including: 

- Miswired or incorrectly connected cables within clusters.
- Missing or disconnected links between network nodes.
- Redundant cables or extra links that do not match the expected network topology.
- Faulty or damaged cables that disrupt connectivity and cluster health.

{{%notice note%}}
The cable validation tool is a standalone tool that you can launch from the NetQ UI. All users work from a single instance of the tool. Refer to the <a href="https://docs.nvidia.com/networking/display/cablevalidationtool160/" target="_blank">Cable Validation Tool User Guide</a> for: 

- A comprehensive <a href="https://docs.nvidia.com/networking/display/cablevalidationtool160/introduction#src-4183397448_Introduction-SymptomsandRemediation" target="_blank">list of cabling issues</a> that the tool can detect.
- An <a href="https://docs.nvidia.com/networking/display/cablevalidationtool160/introduction#src-4183397448_Introduction-SymptomsandRemediation" target="_blank">overview of the UI</a>.
- Instructions for running <a href="https://docs.nvidia.com/networking/display/cablevalidationtool160/topology+files" target="_blank">topology validations</a>.
{{%/notice%}}

## Requirements and Support

| Fabric Size | CPU Requirements | Memory | Disk Space (Minimum) | Disk Space (Recommended) |
| :--------- | --------- | ----------- |  ----------- |  ----------- |
| Up to 1,000 nodes | 4-core server | 4 GB | 20 GB | 50 GB |
| 1,000-5,000 nodes | 8-core server | 16 GB | 40 GB | 120 GB |
| 5,000-10,000 nodes | 16-core server | 32 GB | 80 GB | 160 GB |

If your network comprises more than 10,000 nodes, contact NVIDIA support for assistance.

### Operating Systems

The cable validation tool is compatible with Spectrum-X and NVLink fabrics running Cumulus Linux or NVOS, respectively.

### Port Requirements
The cable validation tool uses port 8251 for communication. Follow the instructions to {{<exlink url="https://docs.nvidia.com/networking/display/cablevalidationtool160/open+agent+port" text="open port 8251">}} before using the cable validator.

### Switch Configurations
Configure each switch...TBD

### User Roles

All users work from a single instance of the tool. 
- Is CVT only available to users with the admin role?

## Access the Cable Validation

{{<tabs "45">}}

{{<tab "NetQ UI">}}

1. Expand the {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/03-Menu/navigation-menu.svg" height="18" width="18">}} Menu. From the **Tools** section, select **Cable Validation**.

2. If prompted, log in with your NetQ username and password, then follow the instructions in the UI to launch the tool.

When you are finished using the tool, it's a good idea to shut it down to free up resources. To do this, navigate to **System Admin** in the side navigation. From the **Services** tab, select **Stop Bringup**.

{{</tab>}}

{{</tabs>}}