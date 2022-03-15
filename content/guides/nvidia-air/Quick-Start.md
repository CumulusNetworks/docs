---
title: Quick Start
author: NVIDIA
weight: 20
product: NVIDIA Air
---

This quick start provides an easy way to get started with the NVIDIA Air simulation platform.

## Log into NVIDIA Air

NVIDIA Air uses the same credentials as the NVIDIA developer forums for account access. When the login page appears, enter your email address (the one you already use for the forums or the one you intend to use to sign up) in the entry field and click **Get Started**:

{{<img src="/images/guides/nvidia-air/Login.png" width="800px">}}

The page redirects to the NVIDIA forums login page. Click the **Create Account** link to sign up or enter your password to log in with an existing account:

{{<img src="/images/guides/nvidia-air/LoginForums.png" width="800px">}}

## NVIDIA Air Landing Page

After you log in, the NVIDIA Air landing page appears:

{{<img src="/images/guides/nvidia-air/LandingPage.png" width="800px">}}

The landing page offers the following options:

- **Filter Organizations**: If you belong to multiple organizations, the filter icon allows you to filter your list of simulations to only those in the chosen organization(s).

  {{<img src="/images/guides/nvidia-air/OrganizationDropdown.png" width="250px">}}

- **Search Simulations**: If you have more than one simulation, the search field can help filter your simulations based on a text match.

  {{<img src="/images/guides/nvidia-air/SearchSimulation.png">}}

- **Build a Simulation**: If you have no simulations, click the **Build a Simulation** button in the middle of the screen. You can read details of the demos in {{<link title="Pre-built Demos">}}.

  {{<img src="/images/guides/nvidia-air/BuildSim.png" width="300px">}}

  This launches a new window from where you can choose from different ways to build a simulation.

  {{<img src="/images/guides/nvidia-air/Catalog.png" width="800px">}}

- **Sidebar**: The sidebar to the left has a **Create a Simulation** link to create new simulations, links to relevant documentation, and other helpful options.

{{<img src="/images/guides/nvidia-air/SideBar.png">}}

## Simulation Views

Every simulation has a basic view and an advanced view, which provides more options.

### Basic View

The basic view of the simulation provides a graphical view of the simulation's topology.

{{<img src="/images/guides/nvidia-air/BasicView.png" width="800px">}}

Click a node in the topology to launch a console to connect to that node:

{{<img src="/images/guides/nvidia-air/Console.png" width="800px">}}

### Advanced View

The advanced view has 4 different panes:

{{<img src="/images/guides/nvidia-air/AdvancedView.png" width="800px">}}

1. **Guided Tour**: A detailed description of the simulation, complete with step-by-step instructions on running the demo infrastructure.
2. **Console**: The console connection to the simulation.
3. **Nodes**: The list of the nodes in the topology. The list shows the status, number of CPUs and amount of memory for each node. You can take the following actions for each node:
   - **Rebuild**: To restore the node to its default configuration.
   - **Reset**: To issue a hard reset to the node.
   - **View Console**: To connect to the node via a console.
4. **Services**: Optional services you can add, such as SSH. See {{<link url="#services" text="Services">}} below.

#### Services

The Services pane provides the ability to create an external connection into the simulation. Example use cases for this include:

- Accessing the simulation environment using your local preferred SSH client.
- Running Grafana on the oob-mgmt-server and accessing the Grafana GUI externally.
- Setting up SNMP polling from your local laptop into the simulation environment.

To set up a service click the **+ Add Service** button.

{{<img src="/images/guides/nvidia-air/ServicesPanel.png" width="400px">}}

The Create Service dialog appears:

{{<img src="/images/guides/nvidia-air/ServicesCreate.png" width="400px">}}

1. In the **Service Name** field, enter the name of the service. This is a free form text field.
1. In the **Interface** dropdown, select the name of the interface in the simulation where the connection terminates. This is most commonly the eth0 interface on the oob-mgmt-server.
1. In the **Service Type** dropdown, select the type of service you are creating. If you select *SSH*, *HTTP* or *HTTPS*, a hyperlink to the URL is automatically created in the Services panel. If you select *Other*, you can select any port, but no hyperlink gets created. The hyperlink has no functional difference other than providing users a quick way to copy and paste the service.
1. In the **Service Port** field, specify the internal port where the service terminates.
1. Click **Submit** to create the service.

<!-- vale off -->
The example below shows the creation of a service for TCP port 1022. The external port is 24886, so connecting to this service requires connecting to worker06.air.nvidia.com on TCP port 24886, which would forward and redirect to the oob-mgmt-server on TCP port 1022.
<!-- vale on -->

{{<img src="/images/guides/nvidia-air/ServicesCreated.png" width="400px">}}

<!-- vale off -->
The **Enable SSH** button automatically populates the Services panel with an SSH session. It is a shortcut to enable inbound SSH to the oob-mgmt-server so that you can leverage your preferred local SSH client. Note that SSH password authentication is disabled on the oob-mgmt-server by default, so you must upload SSH keys to your user profile so you can use this feature. More information about uploading SSH keys to the user profile is in {{<link url="#user-settings" text="User Settings">}} below.
<!-- vale on -->

## Logging into Virtual Machines

Use the operating system's default credentials to log into your virtual machine(s). Note that some operating systems may require you to change your password after the first successful login.

- **Out-of-band management server (oob-mgmt-server)**
    - Username: `ubuntu`
    - Password: `nvidia`
- **Out-of-band management switch (oob-mgmt-switch)**
    - Username: `cumulus`
    - Password: `cumulus`
- **NVIDIA Cumulus Linux** (version 4.2 and higher)
    - Username: `cumulus`
    - Password: `cumulus`
- **NVIDIA Cumulus Linux** (version 4.1 and lower)
    - Username: `cumulus`
    - Password: `CumulusLinux!`
- **NVIDIA Cumulus NetQ**
    - Username: `cumulus`
    - Password: `cumulus`
- **SONiC**
    - Username: `admin`
    - Password: `YourPaSsWoRd`
- **Ubuntu**
    - Username: `ubuntu`
    - Password: `nvidia`

## Manage a Simulation

From the Air landing page, you can manage simulations. There are three options for each public simulation:

- **Power On/Off**: Wakes the simulation up or puts it to sleep.
- **Rebuild**: Resets the simulation to its initial configuration. This is useful if you've made many changes to the simulation and it is no longer in a desireable state.
- **Delete**: Deletes the simulation.

{{<img src="/images/guides/nvidia-air/ManagingSim.png" width="800px">}}

## User Settings

The `Settings` section of the sidebar allows you to:

- Generate API tokens
- Upload SSH keys

### API Tokens

You can use API tokens to execute authenticated activities using the Air API/SDK.

{{<img src="/images/guides/nvidia-air/UserAPITokenTab.png" width="200px">}}

To generate a token, enter the requisite data into the field and click **Create**.

{{<img src="/images/guides/nvidia-air/UserAPITokenCreate.png" width="300px">}}

This generates a token that you can use to access the API and SDK.

{{<img src="/images/guides/nvidia-air/UserAPITokenGenerated.png" width="600px">}}

### SSH Keys

The **SSH Keys** tab is where you can upload your public SSH key.

{{<img src="/images/guides/nvidia-air/UserSSHKeysTab.png" width="200px">}}

These SSH keys are automatically uploaded to the oob-mgmt-server. Creating a simulation and enabling SSH allows for passwordless authentication.

{{<img src="/images/guides/nvidia-air/UserSSHKeys.png" width="800px">}}
