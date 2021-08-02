---
title: Quick Start
author: NVIDIA
weight: 20
version: "1.0"
---

This quick start provides an easy way to get started with the NVIDIA Air simulation platform.

## Log into NVIDIA Air

NVIDIA Air uses the same credentials as the NVIDIA developer forums for account access. When the login page appears, enter your email address (the one you already use for the forums or the one you intend to use to sign up) in the box and click **Get Started**:

{{<img src="/images/guides/nvidia-air/Login.png" width="800px">}}

The page redirects to the NVIDIA forums login page. Click the **Create Account** link to sign up or enter your password to log in with an existing account:

{{<img src="/images/guides/nvidia-air/LoginForums.png" width="800px">}}

## NVIDIA Air Landing Page

After you log in, the NVIDIA Air landing page appears:

{{<img src="/images/guides/nvidia-air/LandingPage.png" width="800px">}}

The landing page offers the following options:

- **Organizations**: If you have custom simulations, the `Organizations` dropdown shows the different organizations to which each simulation belongs. This is typically only visible if you are working directly with an NVIDIA Solutions Architect to set up a custom topology.

  {{<img src="/images/guides/nvidia-air/OrganizationDropdown.png" width="250px">}}

- **Search Simulations**: If you have more than one simulation, the search box can help filter your simulations based on a text match.

  {{<img src="/images/guides/nvidia-air/SearchSimulation.png">}}

- **Build a Simulation**: If you have no simulations, click the **Build a Simulation** button in the middle of the screen. The details of the demos are described in {{<link title="Pre-built Demos">}}.

  {{<img src="/images/guides/nvidia-air/BuildSim.png" width="300px">}}

  This launches a new window from where you can choose one of the pre-built demos from the list.

  {{<img src="/images/guides/nvidia-air/BuildSim_Demos.png" width="800px">}}

- **Sidebar**: The sidebar to the left has a **Create a Simulation** link to create new simulations, links to the current Cumulus Linux and NetQ user guides and a link to [self-paced labs](https://www.nvidia.com/en-us/networking/linux-on-demand/).

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
3. **Nodes**: The list of the nodes in the topology.
4. **Services**: Optional services you can add, such as SSH.

#### Services 

The services pane provides the option for creating an external connection into the simulation. Example use cases for this include:

* Accessing the simulation environment using your local preferred SSH client
* Running Grafana on the `oob-mgmt-server` and accessing the Grafana GUI externally
* Setting up SNMP polling from your local laptop into the simulation environment

To set up a service click the `+ Add Service` button.

{{<img src="/images/guides/nvidia-air/ServicesPanel.png" width="400px">}}

The following popup will present giving four options:

{{<img src="/images/guides/nvidia-air/ServicesCreate.png" width="400px">}}

* **Service Name:** The name of the service. This can be any free form text field.
* **Interface:** The interface inside the simulation environment that will terminate the connection. This is most commonly the `eth0` interface of the `oob-mgmt-server`.
* **Service Type:** If the field is SSH, HTTP or HTTPS, a hyper link to the URL will automatically be created in the Services panel. If set to Other, any port can be selected, but no hyperlink will be created. The hyperlink has no functional difference other than providing users a quick way to copy and paste the service.
* **Service Port:** This is the internal port where the service will terminate.

After selecting this and submitting, the service will be created. In the below example, a service was created for TCP port 1022. The external port would be 24886, so connecting to this service would require connecting to worker06.air.nvidia.com on TCP port 24886, which would forward and redirect to the oob-mgmt-server on TCP port 1022.

{{<img src="/images/guides/nvidia-air/ServicesCreated.png" width="400px">}}

The `Enable SSH` button auto populates the `Services` panel with an SSH session. It is a short cut to enable inbound SSH to the `oob-mgmt-server` so that the user can leverage their local preferred SSH client. Be aware, that SSH password authentication is disabled on the `oob-mgmt-server` by default. So to use this functionality upload SSH keys to your user profile. More information about uploading SSH keys to the user profile is in the section labelled `User Settings`.

## Manage a Simulation

From the Air landing page, you can manage simulations. There are three options for each public simulation:

- **Power On/Off**: Wakes the simulation up or puts it to sleep.
- **Rebuild**: Resets the simulation to its initial configuration. This is useful if you've made many changes to the simulation and it is no longer in a desireable state.
- **Delete**: Deletes the simulation.

{{<img src="/images/guides/nvidia-air/ManagingSim.png" width="800px">}}

## User Settings

In the top right there is a gear icon which opens up user options.

{{<img src="/images/guides/nvidia-air/UserSettingsGear.png" width="200px">}}

Clicking the gear will open up `User Settings` where SSH keys can be uploaded. These SSH keys are automatically uploaded to the `oob-mgmt-server` when a simulation is created as to allow password-less authentication when SSH is enabled.

{{<img src="/images/guides/nvidia-air/UserSSHKeys.png" width="800px">}}
