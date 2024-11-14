---
title: Quick Start
author: NVIDIA
weight: 20
product: NVIDIA Air
---

This quick start provides the basics so that you can get started with the NVIDIA Air network simulation platform.

## Supported Browsers

The following browsers are fully supported:

- Google Chrome 120 or later
- Mozilla Firefox 121 or later

The following browsers are supported on a best-effort basis:

- Microsoft Edge 
- Safari

## Login

To log in, go to [air.nvidia.com](https://air.nvidia.com/). Enter your business email address, then click **Next.** A valid business email address is required to access NVIDIA Air. If you do not have an account, create a new one.

{{<img src="/images/guides/nvidia-air/Login.png" alt="" width="800px">}}

{{%notice note%}}
If your email address is not accepted as a valid business email address and you believe this to be incorrect, please contact us at [air-support@nvidia.com](mailto:air-support@nvidia.com)
{{%/notice%}}

## Simulations
When you log into Air, you will first see your list of current simulations in your account. 

### Create a Simulation
You can create new simulations in several different ways. NVIDIA Air provides multiple means of creating your own topologies from scratch, and also provides a [Demo Marketplace](https://air.nvidia.com/demos) for fully preconfigured simulations.

To create a new sim, click the **Create Simulation** button from the [Simulations homepage](https://air.nvidia.com/simulations). Then follow the below instructions depending on what kind of topology you want to build:

- To learn about custom topologies and creating sims with Air's built-in drag-and-drop editor, visit [Custom Topology](https://docs.nvidia.com/networking-ethernet-software/nvidia-air/Custom-Topology/).

- To learn about preconfigured, ready out-of-box simulations, visit [Pre-Built Demos](https://docs.nvidia.com/networking-ethernet-software/nvidia-air/Pre-Built-Demos).

### Navigate your Sim
After you create a simulation, you can power them on/off, [edit](#edit-simulations) various aspects of it, [share it with others](#sharing-simulations), and delete it with the **Actions** {{<img src="/images/guides/nvidia-air/ActionsButton.png" alt="">}} button on each sim.

{{<img src="/images/guides/nvidia-air/SimulationsActionHighlight.png" alt="">}}

Click on a simulation to view it. 

You can click the **Topology**, **Nodes** and **Links** tabs for different views. 

The ticking timer represents when your sim will automatically sleep, or be **stored**. You can add more time by clicking the **Actions button {{<img src="/images/guides/nvidia-air/ActionsButton.png" alt="">}} > Add Time**.

Click on a node to view its **Node Properties**.

{{<img src="/images/guides/nvidia-air/NodesTopology.png" alt="">}}

If your simulation contains a **Simulation Guide**, you can reopen a closed guide by clicking **Workspace > Simulation Guide**.

{{<img src="/images/guides/nvidia-air/WorkspaceSimGuide.png" alt="">}}

### Node Consoles
Double click on any node to connect to its console from the **Topology** tab. 

Click the {{<img src="/images/guides/nvidia-air/LoginCredsButton.png" alt=""  width="32px" >}} icon to view its login credentials. 
 
Click the {{<img src="/images/guides/nvidia-air/PopoutButton.png" alt=""  width="32px" >}} button to open the console in its own window.

{{<img src="/images/guides/nvidia-air/Console.png" alt=""  width="800px" >}}

### Services
Enable services to create an external connection with your sim. This allows for more integration with your sim, such as using a preferred SSH client to access your sim, running Grafana, or setting up SNMP polling.

To add a new service to your sim:
1. From within a simulation, click **Services > New Services**.

{{<img src="/images/guides/nvidia-air/ServicesDropdown.png" alt=""  width="450px" >}}

2. **Service Name**: Name for your service. Handy for running multiple instances of the same service on different interfaces or ports.
3. **Interface**: Where the connection terminates. Typically `eth0` on the `oob-mgmt-server`.
4. **Service Type**: Type of service.
   - NVIDIA Air creates a hyperlink to the URL automatically in the Services panel for _SSH_, _HTTP_ or _HTTPS_ services. For _Other_ services, any port can be used, but Air will not generate a hyperlink. The hyperlink provides a quick way to copy and paste the service if your browser supports it.
5. **Service Port**: Internal port where service terminates.
6. Click **Create**.

{{<img src="/images/guides/nvidia-air/ServicesAdd.png" alt=""  width="450px" >}}

Click **Services > Enable SSH** to enable SSH into the `oob-mgmt-server` immediately. Use this to leverage your preferred local SSH client. Only available when the [OOB network](https://docs.nvidia.com/networking-ethernet-software/Custom-Topology/#oob-management-network) is enabled. SSH password authentication is disabled on the `oob-mgmt-server` by default. To use SSH password authentication, you must upload SSH keys to your user profile; see [SSH Keys](#api-tokens--ssh-keys) below.

Click **Services > Services List** to view existing services enabled on the sim. Here you can also view important access information such as the port and external host to connect with.

{{<img src="/images/guides/nvidia-air/ServicesList.png" alt="">}}

### Rebuilding & Resetting Nodes
From within a sim, single click on a node to view its **Node Properties**. Click **Advanced Properties > Actions** to **Rebuild** or **Reset** the node.

- **Rebuild**: Restores the node to its original or default configuration. If the node was created from a demo, or other snapshot, it will revert to that configuration had you just launched a copy.
- **Reset**: Performs a hard reboot to the node.

{{<img src="/images/guides/nvidia-air/RebuildReset.png" alt=""  width="450px" >}}

You can also rebuild the entire simulation with **Workspace > Rebuild All Nodes**.

### Edit Simulations
From within a sim, click **Workspace > Edit Simulation** to edit various aspects of your sim.

- **Name**: Edit the sim name. Simulations can have duplicate names, as they each have a unique ID under the hood.
- **Organization**: Assign an Organization. You can read more about Organizations [here](https://docs.nvidia.com/networking-ethernet-software/nvidia-air/Organizations). This will assign this exact simulation to the Organization, _not a copy_. This means each user with appropriate permissions will have access to this exact sim.

- **Sleep date**: When the simulation will be automatically put to sleep. This means the state of the sim is saved and resources are freed for your account. Nodes are _not_ powered off.
- **Expiration date**: When the simulation will be automatically deleted.

You can also edit your sim from the **Simulations homepage > Actions {{<img src="/images/guides/nvidia-air/ActionsButton.png" alt="">}} > Edit Simulation**.

{{<img src="/images/guides/nvidia-air/EditSim.png" alt=""  width="500px" >}}

## API Tokens & SSH Keys
Click your username in the top right and click **Settings** to view your API tokens and SSH keys.

You can also navigate to [air.nvidia.com/settings](https://air.nvidia.com/settings).

### API Tokens

API tokens allow you to execute authenticated activities using the NVIDIA Air API or SDK.

To generate an API token:

1. **Name** your API token.
2. Set an **Expiration Date**.
3. Click **Create**.
4. Save your token somewhere safe. You will not be able to view it again.

{{<img src="/images/guides/nvidia-air/APIToken.png" alt="" width="1000px">}}

### SSH Keys
SSH keys must be added here when you wish to enable the SSH service on simulations. They are automatically added to the `oob-mgmt-server`.

To add an SSH key:

1. **Name** your SSH key.
2. Copy your **Public Key** into the textbox.
3. Click **Add**.

You can revoke/delete both API tokens and SSH keys if you no longer need them, or they are believed to be compromised.

{{<img src="/images/guides/nvidia-air/SSHKey.png" alt="" width="1000px">}}

## Sharing Simulations
Sharing a simulation with another user is a common use case in Air. 

To share a sim: 

1. From within a simulation, click **Workspace > Manage Users** to share this exact sim, _not a copy_, with any other user.  
2.	Enter their email address. You can enter multiple addresses.
3.	Toggle whether they only have **Read Only** access. This means they will not be able to make any modifications to the simulation in Air, such as deleting it or placing it in an Organization. The user can ##still access consoles## and modify the simulation directly that way.
4.	Click **Add User**.
   
The user(s) will now see the simulation in their [Simulations](https://air.nvidia.com/simulations) list to access. The user will not receive any notification they were given access to the sim. 

{{<img src="/images/guides/nvidia-air/ManageUsers.png" alt="" width="600px">}}

You can also share simulations via Organizations. Read more about them [here](https://docs.nvidia.com/networking-ethernet-software/nvidia-air/Organizations). 

## Resource Budgets
The number of simulation resources a user can consume is limited for each user's account. For an account using a valid business email, a user is granted the following limits:

- 60 vCPUs
- 90GB memory
- 650GB storage
- 4 running simulations

NVIDIA users are granted the following limits:

- 100 vCPUs
- 100GB memory
- 1TB storage
- 5 running simulations

Individual user account resources are great for running demos and smaller simulations but to run larger simulations it is best to use [Organizations](https://docs.nvidia.com/networking-ethernet-software/nvidia-air/Organizations).
Organizations have a much higher resource budget than an individual user account. The default resource budget for an organization is:

- 300 vCPUs
- 300GB memory
- 3TB storage
- 10GB Image Storage
- 15 running simulations

The budgets for organizations can be adjusted based on the needs of that organization. If a resource budget for an organization needs to be expanded, contact the Air Support team via the option to "Report An Issue" from air.nvidia.com.

## Other Notes

- Using [Cumulus Linux in a Virtual Environment](https://docs.nvidia.com/networking-ethernet-software/cumulus-linux/Cumulus-Linux-in-a-Virtual-Environment/)
