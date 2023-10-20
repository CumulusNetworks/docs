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

1. Select the NVL4 icon in the header, then select **Add domain**.

2. Fill out the fields in UI, starting with the GFM configuration:

{{<figure src="/images/netq/domain-first-480.png" alt="wizard prompting user to configure GFM" width="550">}}

The **Domain name** is the name that will appear in the inventory list.

The **log level** can be set to critical, error, warning, info, or none.

The **GFM timeout** is the length of time that the GFM node will wait for Local Fabric Managers (LFMs) to boot on all nodes. Setting this field to **Wait forever -1** (recommended) instructs the node to wait indefinitely, preventing timeout issues. You can also enter a custom value in this field (in seconds).

**Fabric manager mode** lists supported physical and virtualization models. For more information, refer to the {{<exlink url="https://docs.nvidia.com/datacenter/tesla/pdf/fabric-manager-user-guide.pdf" text="Fabric Manager User Guide">}}.

When switched on, the **Create all nodes partition** toggle creates a single, default partition.

3. Select **Next**.

4. The next screen prompts you to upload a topology file. For GFM to run, the topology file must reflect how the network is wired. The same topology file is frequently reused for multiple domains. If a topology file was previously used to create a domain, you will be able to select it from this screen. 

5. Select **Next**.

6. The subsequent screen prompts you to upload your fabric node configuration. This is a text file listing the IP addresses for the nodes (GPU nodes and NVL4 switches) that comprise the domain. Select **Next**.

7. The final screen displays a summary of the domain's parameters. In addition to the summary, you can toggle GFM to run after creating the domain. If you are not ready to start GFM, you can save the configuration and start it later.

8. After reviewing the summary, select **Finish**. NetQ adds the domain to a list of all NVLink4 domains:

{{<figure src="/images/netq/nvl4-test-domain-480.png" alt="" width="1150">}}

From the list of NVLink4 domains, you can view and manage multiple domains. Per domain, you can view the:

- Domain's name
- Time a domain was created
- Last time the domain was updated
- Name of the user who created the domain
- GFM status (starting, stopping, up, down, or failed)
- Total number of nodes (GPU nodes and NVL4 switches), including their health status (healthy or unhealthy)

You can also perform the following actions:

- Generate GFM logs by selecting the **Fetch** button. You can download the logs or view them in the file manager. <!--link to file manager section-->
- Stop and start GFM by selecting the stop and play buttons. When you stop GFM, monitoring operations are gradually shut down and the telemetry agent stops.
- Review a domain's configuration, the devices associated with a domain, and any topology misconfigurations detected by NetQ by selecting the **View details** button:

<!-- insert pic from functioning setup-->
 - The Configuration tab displays the parameters of the domain; 
 - The Devices tab displays a full list of devices, including their IP address, the device health (healthy or unhealthy), LFM status, and other details. Many of the status columns include icons that reveal timestamps and additional information when you hover over them with your mouse. The timestamps update every 60 seconds.
 <!-- insert pic from functioning setup-->
 {{<figure src="/images/netq/nvlink4-unhealthy.png" alt="devices summary for selected domain, including timestamp for an unhealthy device" width="1050">}}
 - The Connections tab displays differences that NetQ detected between the actual topology and the expected topology.
 <!-- insert pic from functioning setup-->

## Edit a Domain

To edit a domain, you must first stop the GFM by selecting the stop button. After GFM stops, select the {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/03-Menu/navigation-menu-vertical.svg" height="14" width="14">}} **three-dot menu**, then select **Edit**. Note that this menu only appears when GFM is not running.
## Delete a Domain

To delete a domain, you must first stop the GFM by selecting the stop button. After GFM stops, select the {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/03-Menu/navigation-menu-vertical.svg" height="14" width="14">}} **three-dot menu**, then select **Delete**. You cannot delete a topology file that is in use by a domain.
