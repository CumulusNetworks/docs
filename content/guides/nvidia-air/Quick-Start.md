---
title: Quick Start
author: NVIDIA
weight: 20
product: NVIDIA Air
---

This quick start provides the basics so that you can get started with the NVIDIA Air network simulation platform.

## Login

NVIDIA Air uses the same credentials as the NVIDIA developer forums for account access. When the login page opens, enter the email address you use for the forums or the one you intend to use to sign up, then click **GET STARTED**:

{{<img src="/images/guides/nvidia-air/Login.png" width="800px">}}

The page redirects you to the NVIDIA forums login page. Either click the **Create account** link to sign up or enter your password to log in with an existing account:

{{<img src="/images/guides/nvidia-air/LoginForums.png" width="800px">}}

## Landing Page

After you log in, the NVIDIA Air landing page opens:

{{<img src="/images/guides/nvidia-air/LandingPagewithCallouts.png" width="800px">}}

The landing page provides the following options:
- **Sidebar**: Provides links to create simulations, configure organizations and settings, and view documentation.
<!--{{<img src="/images/guides/nvidia-air/SideBar.png">}}-->
- **Filter Organizations**: If you belong to multiple organizations, you can filter your list of simulations based on organization.
<!--{{<img src="/images/guides/nvidia-air/OrganizationDropdown.png" width="250px">}}-->
- **Search Simulations**: If you have more than one simulation, you can filter your simulations based on a text match.
<!--{{<img src="/images/guides/nvidia-air/SearchSimulation.png">}}-->
- **Build a Simulation**: If you have no simulations, click the **BUILD A SIMULATION** button. NVIDIA Air provides {{<link title="Pre-built Demos">}} to help you get started.<!--{{<img src="/images/guides/nvidia-air/BuildSim.png" width="300px">}}-->

   A new window opens so that you can choose from different ways to build a simulation.

   {{<img src="/images/guides/nvidia-air/Catalog.png" width="800px">}}

## Simulation Views

Every simulation has a basic view and an advanced view.

### Basic View

The basic view of the simulation provides a graphical view of the topology.

{{<img src="/images/guides/nvidia-air/BasicView.png" width="800px">}}

Click a node in the topology to open a console and connect to that node:

{{<img src="/images/guides/nvidia-air/Console.png" width="800px">}}

### Advanced View

The advanced view has four different panes:

{{<img src="/images/guides/nvidia-air/AdvancedView.png" width="800px">}}

- **Guided Tour** provides a detailed description of the simulation, complete with step-by-step instructions on running the demo infrastructure.
- **Console** provides console connection to the simulation.
- **Nodes** lists the nodes in the topology; see {{<link url="#nodes" text="Nodes">}} below.
- **Services** provides optional services, such as SSH; see {{<link url="#services" text="Services">}} below.

#### Nodes

The nodes list in the advanced view shows the status, number of CPUs, and amount of memory for each node. Click the **Actions** dropdown for a node and select:
  - **Rebuild** to restore the node to its default configuration.
  - **Reset** to issue a hard reset to the node.
  - **View Console** to connect to the node from a console.

#### Services

Use the Services pane in the advanced view to create an external connection into the simulation. You can access the simulation environment using your local preferred SSH client, run Grafana on the [oob-mgmt-server](## "Out-of-band Management Server") and access the Grafana GUI externally, or set up SNMP polling from your local laptop into the simulation environment.

To set up a service:
1. Click the **+ Add Service** button to open the Service dialog:

  {{<img src="/images/guides/nvidia-air/ServicesCreate.png" width="400px">}}

2. In the **Service Name** field, enter the name of the service. This is a free form text field.
3. In the **Interface** dropdown, select the name of the interface in the simulation where the connection terminates. This is typically the eth0interface on the oob-mgmt-server.
4. In the **Service Type** dropdown, select the type of service you want to create. If you select *SSH*, *HTTP* or *HTTPS*, NVIDIA Air creates a hyperlink to the URL automatically in the Services panel. If you select *Other*, you can select any port, but there is no hyperlink. The hyperlink provides a quick way to copy and paste the service.
5. In the **Service Port** field, specify the internal port where the service terminates.
6. Click **Submit** to create the service.
<!-- vale off -->
The example below shows the creation of a service for TCP port 1022. The external port is 24886. Connecting to this service requires connecting to worker06.air.nvidia.com on TCP port 24886, which forwards and redirects to the oob-mgmt-server on TCP port 1022.
<!-- vale on -->

{{<img src="/images/guides/nvidia-air/ServicesCreated.png" width="400px">}}

<!-- vale off -->
The **ENABLE SSH** button populates the Services panel with an SSH session, which provides a shortcut to enable inbound SSH to the oob-mgmt-server. Use this shortcut to leverage your preferred local SSH client. SSH password authentication is disabled on the oob-mgmt-server by default. To use SSH password authentication, you must upload SSH keys to your user profile; see {{<link url="#user-settings" text="User Settings">}} below.
<!-- vale on -->

## Log into Virtual Machines

Use the operating system default credentials to log into your virtual machines. Some operating systems require you to change your password after the first successful login.

{{< tabs "TabID112 ">}}
{{< tab "oob-mgmt-server ">}}

Username: `ubuntu`

Password: `nvidia`

{{< /tab >}}
{{< tab "oob-mgmt-switch ">}}

Username: `cumulus`

Password: `cumulus`

{{< /tab >}}
{{< tab "NVIDIA Cumulus Linux ">}}

{{< tabs "TabID127 ">}}
{{< tab "Release 4.2 and later ">}}

Username: `cumulus`

Password: `cumulus`

{{< /tab >}}
{{< tab "Release 4.1 and earlier ">}}

Username: `cumulus`

Password: `CumulusLinux!`

{{< /tab >}}
{{< /tabs >}}

{{< /tab >}}
{{< tab "NVIDIA Cumulus NetQ ">}}

Username: `cumulus`

Password: `cumulus`

{{< /tab >}}
{{< tab "SONiC ">}}

Username: `admin`

Password: `YourPaSsWoRd`

{{< /tab >}}
{{< tab "Ubuntu ">}}

Username: `ubuntu`

Password: `nvidia`

{{< /tab >}}
{{< /tabs >}}

## Manage a Simulation

From the NVIDIA Air landing page, you can manage your simulations.

{{<img src="/images/guides/nvidia-air/ManagingSimwithCallouts.png" width="800px">}}

 Each public simulation has three options:
- **Power On or Off** wakes the simulation up or puts it to sleep.
- **Edit** lets you change the simulation name and organization, and set the simulation to never expire or sleep.
- **Delete** removes the simulation.

## User Settings

The **SETTINGS** dropdown in the sidebar provides options to:

- Generate API tokens
- Upload SSH keys

### API Tokens

You can use API tokens to execute authenticated activities using the NVIDIA Air API or SDK.

{{<img src="/images/guides/nvidia-air/UserAPITokenTab.png" width="200px">}}

To generate a token, enter the required information in the fields and click **Create**.

{{<img src="/images/guides/nvidia-air/UserAPITokenCreate.png" width="300px">}}

This generates a token that you can use to access the API and SDK.

{{<img src="/images/guides/nvidia-air/UserAPITokenGenerated.png" width="600px">}}

### SSH Keys

The **SSH Keys** tab is where you can upload your public SSH key.

{{<img src="/images/guides/nvidia-air/UserSSHKeysTab.png" width="200px">}}

The SSH keys upload automatically to the oob-mgmt-server. Creating a simulation and enabling SSH allows for passwordless authentication.

{{<img src="/images/guides/nvidia-air/UserSSHKeys.png" width="800px">}}
