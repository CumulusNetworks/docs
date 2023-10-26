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

This section outlines the steps to create a new domain using the UI. Advanced users can manually adjust GFM variables (beyond what is presented in the UI) by creating a new domain as outlined below, then following the {{<link title="Edit GFM Variables" text="steps to edit GFM configuration variables">}}. 

1. Select the {{<link title="NVLink Quick Start Guide/#access-nvlink4" text="NVL4 icon in the header">}}, then select **Add domain**.

2. Fill out the fields in the UI, starting with configuring the GFM:

{{<figure src="/images/netq/domain-first-480.png" alt="wizard prompting user to configure GFM" width="550">}}

- **Domain name** is the name that will appear in the inventory list.
- **Log level** can be set to critical, error, warning, info, or none.
- **GFM timeout** is the length of time that the GFM node will wait for Local Fabric Managers (LFMs) to boot on all nodes. Set this field to **Wait forever -1** (recommended) to instruct the node to wait indefinitely, which prevents timeout issues. You can also enter a custom value (in seconds) in this field.
- **Fabric manager mode** lists supported physical and virtualization models. For more information, refer to the {{<exlink url="https://docs.nvidia.com/datacenter/tesla/pdf/fabric-manager-user-guide.pdf" text="Fabric Manager User Guide">}}.

When toggled on, the **Create all nodes partition** switch creates a single, default partition.

3. Select **Next**.

4. The next screen prompts you to upload a topology file. For GFM to run, the topology file must reflect how the network is wired. The same topology file is frequently reused for multiple domains. If a topology file was previously used to create a domain, you will be able to select it from this screen. NetQ supports both IPv4 and IPv6 addresses.

5. Select **Next**.

6. The subsequent screen prompts you to upload your fabric node configuration. This is a text file listing the IP addresses for the nodes (NVLink switches) that comprise the domain. 

7. Select **Next**.

8. The final screen displays a summary of the domain's parameters. In addition to the summary, you can choose to start GFM after creating the domain. If you are not ready to start GFM or if you are planning to {{<link title="Edit GFM Variables" text="edit the GFM variables">}}, you can save the configuration and start it later.

9. After reviewing the summary, select **Finish**. NetQ adds the domain to a list of all NVLink4 domains:

{{<figure src="/images/netq/nvl4-test-domain-480.png" alt="" width="1150">}}

From the list of NVLink4 domains, you can view and manage multiple domains. Per domain, you can view the:

- Domain's name
- Time a domain was created
- Last time the domain was updated
- Name of the user who created the domain
- GFM status (starting, stopping, up, down, or failed). In the event of a 'failed' status, NetQ will also display the number of times it attempted to restart GFM via a 'GFM recovery' counter.
- Differences in the expected versus actual topology, indicated by a topology icon <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/41-Hierachy-Organization/hierarchy.svg" height="18" width="18"/> that you can select to view the differences
- Total number of nodes, including their health status (healthy or unhealthy)

You can also perform the following actions:

- Generate GFM logs by selecting the **Fetch** button. You can view a list of logs and download them by selecting the {{<link title="Debugging Files" text="file manager">}}.
- Stop and start GFM by selecting the stop and play buttons. When you stop GFM, monitoring operations are gradually shut down and the telemetry agent stops.
- Review a domain's configuration, the devices associated with a domain, and any topology misconfigurations detected by NetQ by selecting the **View details** button.

 ## View Additional Domain Information

 When you select the **View details** button on a given domain, you gain access to granular information about the domain's configuration:
<!-- insert pic from functioning setup-->
 - The Configuration tab displays the domain's configuration information.
 - The Devices tab displays a full list of devices, including their respective IP addresses, hostnames, LFM status, the device health (healthy or unhealthy), and other details. Many of the status columns include timestamp details (updated every 60 seconds) that you can access by hovering your mouse over the clock icon. The LED indicator column features a toggle that can be switched on to illuminate the blue locator UID LED on the switch. This is helpful for finding a particular switch in a data center full of switches.
 {{<figure src="/images/netq/nvlink-devices-480.png" alt="devices summary for selected domain" width="1050">}}
 - The Connections tab displays differences that NetQ detected between the actual network topology and the expected network topology. NetQ groups and displays missing, unexpected, or inactive optical connections for NVLink L1 and L2 switches. If NetQ does not detect connection anomalies, this screen will not contain data.
<!--{{<figure src="/images/netq/connections-diff-nvlink-480.png" alt="" width="1050">}}-->

## Edit a Domain

To edit a domain, you must first stop the GFM by selecting the stop button. After GFM stops, select the {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/03-Menu/navigation-menu-vertical.svg" height="14" width="14">}} **three-dot menu**, then select **Edit**. Note that this menu only appears when GFM is not running. To manually adjust and configure a broader range GFM variables that are unavailable in the NetQ UI, refer to {{<link title="Edit GFM Variables">}}.

## Delete a Domain

To delete a domain, you must first stop the GFM by selecting the stop button. After GFM stops, select the {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/03-Menu/navigation-menu-vertical.svg" height="14" width="14">}} **three-dot menu**, then select **Delete**. You cannot delete a topology file that is in use by a domain.
