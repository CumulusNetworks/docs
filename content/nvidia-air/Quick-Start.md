---
title: Quick Start
author: NVIDIA
weight: 20
product: NVIDIA Air
---

This quick start provides the basics so that you can get started with the NVIDIA Air network simulation platform.

## Supported Browsers

The following browsers are fully supported:

- Google Chrome 91 or later
- Mozilla Firefox 89 or later

The following browsers are supported on a best-effort basis:

- Microsoft Edge 
- Safari

## Login

NVIDIA Air uses the same credentials as the NVIDIA developer forums for account access. To log in, go to {{<exlink url="https://air.nvidia.com" text="air.nvidia.com">}}. Enter the email address you use for the forums or the one you intend to use to sign up, then click **Get Started**:

{{<img src="/images/guides/nvidia-air/Login.png" alt="" width="800px">}}

The page redirects you to the NVIDIA forums login page. Either click the **Create account** link to sign up or enter your password to log in with an existing account:

{{<img src="/images/guides/nvidia-air/LoginForums.png" alt="" width="800px">}}

## Landing Page

After you log in, the NVIDIA Air landing page opens:

{{<img src="/images/guides/nvidia-air/LandingPagewithCallouts.png" alt="" width="800px">}}

<div style="margin-top: 20px;"></div>

- The **Sidebar** provides links to create simulations, configure organizations and settings, and view documentation.
<!--{{<img src="/images/guides/nvidia-air/SideBar.png">}}-->
- The **Search simulations** field lets you filter your simulations based on a text match, if you have more than one simulation.
<!--{{<img src="/images/guides/nvidia-air/SearchSimulation.png">}}-->
- The **Search filter** lets you filter your list of simulations based on organization, if you belong to multiple organizations.
<!--{{<img src="/images/guides/nvidia-air/OrganizationDropdown.png" width="250px">}}-->
- The **Build a Simulation** button lets you build a new simulation. This button appears only if you have no simulations. NVIDIA Air provides {{<link title="Pre-built Demos">}} to help you get started.<!--{{<img src="/images/guides/nvidia-air/BuildSim.png" width="300px">}}-->

   When you select **Build a Simulation**, a new window opens displaying different ways to create a simulation.

   {{<img src="/images/guides/nvidia-air/Catalog.png" alt="options to build a simulation from a pre-defined topology, a custom topology, or from the demo marketplace" width="800px">}}

## Simulation Views

Every simulation has a basic view and an advanced view.

### Basic View

The basic view of the simulation provides a graphical view of the topology.

{{<img src="/images/guides/nvidia-air/BasicView.png" alt="" width="800px">}}

<div style="margin-top: 20px;"></div>

Select a node in the topology to open a console and connect to that node:

{{<img src="/images/guides/nvidia-air/Console.png" alt="" width="500px">}}

### Advanced View

The advanced view has four different panes:

{{<img src="/images/guides/nvidia-air/AdvancedView.png" alt="" width="800px">}}

- **Guided Tour** provides a detailed description of the simulation, complete with step-by-step instructions on running the demo infrastructure.
- **Console** provides console connection to the simulation.
- **Nodes** lists the nodes in the topology; see {{<link url="#nodes" text="Nodes">}} below.
- **Services** provides optional services, such as SSH; see {{<link url="#services" text="Services">}} below.

#### Nodes

Use the **Nodes** pane in the advanced view to see the status, number of CPUs, and amount of memory for each node. Click the **Actions** dropdown for a node and select:
  - **Rebuild** to restore the node to its default configuration.
  - **Reset** to issue a hard reset to the node.
  - **View Console** to connect to the node from a console.

#### Services

Use the **Services** pane in the advanced view to create an external connection into the simulation. You can access the simulation environment using your local preferred SSH client, run Grafana on the [oob-mgmt-server](## "Out-of-band Management Server") and access the Grafana GUI externally, or set up SNMP polling from your local laptop into the simulation environment.

<!-- vale off -->
- **Enable SSH** populates the services panel with an SSH session, which provides a shortcut to enable inbound SSH to the oob-mgmt-server. Use this shortcut to leverage your preferred local SSH client. SSH password authentication is disabled on the oob-mgmt-server by default. To use SSH password authentication, you must upload SSH keys to your user profile; see {{<link url="#user-settings" text="User Settings">}} below.
<!-- vale on -->
- **Add Service** opens the Create Service dialog so you can add a service:

  {{<img src="/images/guides/nvidia-air/ServicesCreate.png" alt="" width="400px">}}

  1. In the **Service Name** field, enter the name of the service.
  2. From the **Interface** dropdown, select the name of the interface in the simulation where the connection terminates. This is typically the eth0 interface on the oob-mgmt-server.
  3. From the **Service Type** dropdown, select the type of service you want to create. If you select *SSH*, *HTTP* or *HTTPS*, NVIDIA Air creates a hyperlink to the URL automatically in the Services panel. If you select *Other*, you can select any port, but there is no hyperlink. The hyperlink provides a quick way to copy and paste the service.
  4. In the **Service Port** field, specify the internal port where the service terminates.
  5. Click **Submit** to create the service.
<!-- vale off -->

The example below shows a service for TCP port 1022. The external port is 24886. Connecting to this service requires connecting to worker06.air.nvidia.com on TCP port 24886, which forwards and redirects to the oob-mgmt-server on TCP port 1022.
<!-- vale on -->

{{<img src="/images/guides/nvidia-air/ServicesCreated.png" alt="" width="400px">}}

<div style="margin-top: 20px;"></div>

## Log in to Virtual Machines

To log in to your virtual machines, use the operating system default credentials. Some operating systems require you to change your password after the first successful login.

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
{{< tab "NVIDIA NetQ ">}}

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

{{<img src="/images/guides/nvidia-air/ManagingSimwithCallouts.png" alt="" width="900px">}}

<div style="margin-top: 20px;"></div>

 Each public simulation has three options:
- **Power On or Off** wakes the simulation up or puts it to sleep.
- **Edit** lets you change the simulation name and organization.
- **Delete** removes the simulation.

## User Settings

The **Settings** menu in the sidebar provides options to generate API tokens and upload SSH keys.

{{<img src="/images/guides/nvidia-air/UserAPITokenTab.png" alt="" width="200px">}}

### API Tokens

From the **Settings** section, select **API Tokens** to generate an authentication token which allows you to execute authenticated activities using the NVIDIA Air API or SDK.

In the API Tokens window, provide a name and expiration date (optional) for the token, then click **Create**.

{{<img src="/images/guides/nvidia-air/UserAPITokenCreate.png" alt="" width="300px">}}

<div style="margin-top: 20px;"></div>

NVIDIA Air generates a token that you can use to access the API and SDK.

{{<img src="/images/guides/nvidia-air/UserAPITokenGenerated.png" alt="" width="600px">}}

### SSH Keys

From the **Settings** section, select **SSH Keys** to upload your public SSH key. Creating a simulation and enabling SSH allows for passwordless authentication.

In the SSH keys window, provide a name and enter your public key, then click **Add**.

{{<img src="/images/guides/nvidia-air/UserSSHKeys.png" alt="" width="800px">}}

<div style="margin-top: 20px;"></div>

The SSH keys upload automatically to the oob-mgmt-server.

## Resource Budgets

The number of simulation resources a user can consume is limited based on the user's account. For an account using a company email, a user is granted the following limits:

- 60 vCPUs
- 90GB memory
- 650GB storage
- 4 running simulations

For an account using a non-company email, a user is granted the following limits:

- 30 vCPUs
- 55GB memory
- 350GB storage
- 1 running simulation

NVIDIA users are granted the following limits:

- 100 vCPUs
- 100GB memory
- 1TB storage
- 5 running simulations

Individual user account resources are great for running demos and smaller simulations but to run larger simulations it is best to use {{<link title="Organizations">}}.
Organizations have a much higher resource budget than an individual user account. The default resource budget for an organization is:

- 300 vCPUs
- 300GB memory
- 3TB storage
- 10GB Image Storage
- 15 running simulations

The budgets for organizations can be adjusted based on the needs of that organization. If a resource budget for an organization needs to be expanded, contact the Air Support team via the option to "Report An Issue" from air.nvidia.com.

## Other Notes

- Using {{<exlink url="https://docs.nvidia.com/networking-ethernet-software/cumulus-linux/Cumulus-Linux-in-a-Virtual-Environment/" text="Cumulus Linux in a Virtual Environment">}}
