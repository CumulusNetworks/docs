---
title: NVLink4 Domain Management
author: NVIDIA
weight: 1150
toc: 3
bookhidden: true
---

This section describes how to create, edit, and delete NVLink4 domains. After you create and configure a domain, Global Fabric Manager (GFM) manages the domains while NetQ collects telemetry data that can be visualized in the UI.

## Requirements

To run GFM, each domain needs a configuration file, a topology file, and an IP address file. You need to upload the topology and IP address files during the domain creation process. The configuration file is created automatically after you have configured the domain.

## Create a Domain

Select the NVL4 icon in the header, then select **Add domain**:

{{<figure src="/images/netq/netq-header-nvl4.png" alt="" width="750">}}

Creating a domain is a 4-step process. The first step configures the GFM:

{{<figure src="/images/netq/nvlink-gfm-config.png" alt="wizard prompting user to configure GFM" width="750">}}

**Domain name** is the name that will appear in the inventory list.

The **log level** is critical, error, warning, info, or none.

**GFM timeout** is the length of time (in seconds) that the GFM node will wait for Local Fabric Managers (LFMs) to boot up on all nodes. Setting this field to -1 (recommended) prevents timeout issues.

**Fabric manager mode** lists supported physical and virtualization models. For more information, refer to chapters 3 and 4 in the {{<exlink url="https://docs.nvidia.com/datacenter/tesla/pdf/fabric-manager-user-guide.pdf" text="Fabric Manager User Guide">}}.

The next step prompts you to upload a topology file:

{{<figure src="/images/netq/nvl4-topology-file.png" alt="wizard prompting user to upload topology file" width="550">}}

For GFM to run, the topology file must reflect how the network is wired. The same topology file is frequently reused for multiple domains. If a topology file was previously used to create a domain, it will appear on this screen.

Next, upload a file of IP addresses:

{{<figure src="/images/netq/nvl4-ip-address-file.png" alt="wizard prompting user to upload file containing IP addresses" width="550">}}

This is a text file listing the IP addresses for the nodes (GPU nodes and NVL4 switches) that comprise the domain.

The final screen displays a summary of the domain's parameters. In addition to the summary, you can toggle GFM to run after creating the domain. If you are not ready to start GFM, you can save the configuration and start it later.

Enter your credentials to set the switch username and password. 

{{<notice info>}}
If you are also using NetQ to manage Ethernet switches, make sure the switch username and password match.
{{</notice>}}

After reviewing the summary, select **Finish**. NetQ adds the domain to a list of all NVLink4 domains:

{{<figure src="/images/netq/nvl4-domain-list.png" alt="list of three NVL4 domains, including the one created in the preceding steps" width="1050">}}

From the list of NVLink4 domains, you can view and manage multiple domains. Per domain, you can view:

- The domain's name
- Time a domain was created
- Name of the user who created the domain
- GFM status (starting, stopping, up, down, or failed)
- Total number of nodes (GPU nodes and NVL4 switches)
- Number of healthy, unhealthy, and undiscovered nodes. *Undiscovered* means that NetQ is not receiving telemetry data from the device.

You can also stop and start GFM by selecting the stop and play buttons. Stopping GFM gradually shuts down monitoring operations and stops the telemetry agent.

Select **View details** to review the domain's configuration and associated devices:

{{<figure src="/images/netq/nvl4-view-details.png" alt="configuration summary for a selected domain" width="1050">}}

{{<figure src="/images/netq/nvl4-devices-list.png" alt="devices summary for selected domain" width="1050">}}

## Edit a Domain

Select the three-dot menu {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/03-Menu/navigation-menu-vertical.svg" height="14" width="14">}} to edit a domain's configuration. Note that if GFM is running, you must stop it before editing a domain. 

## Delete a Domain

Select the three-dot menu {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/03-Menu/navigation-menu-vertical.svg" height="14" width="14">}}, then select **Delete**. You cannot delete a topology file that is in use by a domain.
