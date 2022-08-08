---
title: NVLink4 Domain Management
author: NVIDIA
weight: 1150
toc: 3
---

This section describes how to create, edit, and delete NVLink4 domains. After you create and configure a domain, Global Fabric Manager (GFM) manages the domains while NetQ collects telemetry data that can be visualized in the UI.

## Requirements

To run GFM, each domain needs a configuration file, a topology file, and an IP file. You need to upload the topology and IP files during the domain creation process. The configuration file is created automatically after you have configured the domain.

## Create a Domain

Select the NVL4 icon in the header, then **Add domain**:

{{<figure src="/images/netq/netq-header-nvl4.png" width="750">}}

The first step configures the GFM:

{{<figure src="/images/netq/nvlink-gfm-config.png" width="750">}}

**Domain name** is the name you'd like to give your domain. This name will appear in the inventory list.

Choose a **log level** of critical, error, warning, info, or none.

**GFM timeout** is the length of time (in seconds) that the GFM node will wait for Local Fabric managers (LFMs) to boot up on all nodes. Setting this field to -1 (recommended) prevents timeout issues.

**Fabric manager mode** lists supported physical and virtualization models. For more information, refer to chapters 3 and 4 in the {{<exlink url="https://docs.nvidia.com/datacenter/tesla/pdf/fabric-manager-user-guide.pdf" text="Fabric Manager User Guide">}}

The next step prompts you to upload a topology file:

{{<figure src="/images/netq/nvl4-topology-file.png" width="550">}}

For GFM to run, the topology file must reflect how the network is wired. It is likely that the same topology file will be used for multiple domains. If a a topology file was previously used to create a domain, it will appear on this screen.

Next, upload a file of IP addresses:

{{<figure src="/images/netq/nvl4-ip-address-file.png" width="550">}}

This is a text file listing the IP addresses for the nodes (GPU nodes and NVL4 switches) that comprise the domain.

The final screen displays a summary of the domain's parameters. In addition to the summary, you can toggle GFM to run after creating the domain. If you are not ready to start GFM, you can save the configuration and start it later.

Enter your credentials to set the switch username and password. Note: If you are also using NetQ to manage ethernet switches, these credentials must match.

After you select **Finish**, NetQ adds the domain to a list of NVLink4 domains:

{{<figure src="/images/netq/nvl4-domain-list.png" width="950">}}

From the list of NVLink4 domains, you can view and manage multiple domains. Per domain, you can view:

- The domain's name
- Time a domain was created
- Name of the user who created the domain
- GFM status (starting, stopping, up, down, or failed)
- Total number of nodes (GPU nodes and NVL4 switches)
- Number of healthy, unhealthy, and undiscovered nodes. *Undiscovered* means that NetQ is not receiving telemetry data from the device.

You can also stop and start GFM by selecting (stop icon) or (play icon). Stopping GFM gradually shuts down monitoring operations and stops the telemetry agent.

Select **View details** to review the domain's configuration and associated devices:

{{<figure src="/images/netq/nvl4-view-details.png" width="950">}}

{{<figure src="/images/netq/nvl4-devices-list.png" width="950">}}

## Edit a domain

Select the three-dot menu (icon) to edit a domain's configuration. Note that if GFM is running, you must stop it before editing a domain. 

## Delete a domain

Select the three-dot menu (icon) and select **Delete**. You cannot delete a topology file if it is in use by a domain.
