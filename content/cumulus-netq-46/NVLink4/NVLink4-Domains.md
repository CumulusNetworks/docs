---
title: Domain Management
author: NVIDIA
weight: 1100
toc: 3

---

This section describes how to create, edit, and delete NVLink4 domains. To collect telemetry data that can be visualized in the UI, create and configure a domain, then run Global Fabric Manager (GFM).

## Requirements

To run GFM, each domain needs a configuration file, a topology file, and an IP address file. You need to upload the topology and IP address files during the domain creation process. The configuration file is created automatically after you have configured the domain.

## Create a Domain

Select the NVL4 icon in the header, then select **Add domain**:

{{<figure src="/images/netq/nvl4-header-450.png" alt="" width="850">}}

Creating a domain is a 4-step process. The first step configures the GFM:

{{<figure src="/images/netq/nvl4-config-450.png" alt="wizard prompting user to configure GFM" width="550">}}

**Domain name** is the name that will appear in the inventory list.

The **log level** is critical, error, warning, info, or none.

**GFM timeout** is the length of time (in seconds) that the GFM node will wait for Local Fabric Managers (LFMs) to boot up on all nodes. Setting this field to -1 (recommended) prevents timeout issues.

**Fabric manager mode** lists supported physical and virtualization models. For more information, refer to chapters 3 and 4 in the {{<exlink url="https://docs.nvidia.com/datacenter/tesla/pdf/fabric-manager-user-guide.pdf" text="Fabric Manager User Guide">}}.

The **Create all nodes partition** toggle creates a single default partition when toggled on.

The next step prompts you to upload a topology file:

{{<figure src="/images/netq/nvl4-topology-file.png" alt="wizard prompting user to upload topology file" width="550">}}

For GFM to run, the topology file must reflect how the network is wired. The same topology file is frequently reused for multiple domains. If a topology file was previously used to create a domain, it will appear on this screen.

Next, upload your fabric node configuration. This is a text file listing the IP addresses for the nodes (GPU nodes and NVL4 switches) that comprise the domain.

{{<figure src="/images/netq/nvl4-ip-address-file.png" alt="wizard prompting user to upload file containing IP adressess" width="550">}}


The final screen displays a summary of the domain's parameters. In addition to the summary, you can toggle GFM to run after creating the domain. If you are not ready to start GFM, you can save the configuration and start it later.

After reviewing the summary, select **Finish**. NetQ adds the domain to a list of all NVLink4 domains:

{{<figure src="/images/netq/nvlink4-domains-list.png" alt="list of three NVL4 domains" width="1150">}}

From the list of NVLink4 domains, you can view and manage multiple domains. Per domain, you can view the:

- Domain's name
- Time a domain was created
- Last time the domain was updated
- Name of the user who created the domain
- GFM status (starting, stopping, up, down, or failed)
- Total number of nodes (GPU nodes and NVL4 switches)
- Number of healthy and unhealthy nodes

You can also stop and start GFM by selecting the stop and play buttons. Stopping GFM gradually shuts down monitoring operations and stops the telemetry agent.

Select **View details** to review the domain's configuration and associated devices:

{{<figure src="/images/netq/nvlink4-view-details.png" alt="configuration summary for a selected domain" width="700">}}

The Devices tab displays the device health (healthy or unhealthy) and the LFM status. Hover over unhealthy devices to view the time at which they were last healthy. The timestamp updates continuously at a polling frequency of 60 seconds:

{{<figure src="/images/netq/nvlink4-unhealthy.png" alt="devices summary for selected domain, including timestamp for an unhealthy device" width="1050">}}

## Edit a Domain

Select the three-dot menu {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/03-Menu/navigation-menu-vertical.svg" height="14" width="14">}} to edit a domain's configuration. This menu only appears when GFM is not running. You must stop GFM to edit the domain.

## Delete a Domain

Select the three-dot menu {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/03-Menu/navigation-menu-vertical.svg" height="14" width="14">}}, then select **Delete**. You cannot delete a topology file that is in use by a domain.
