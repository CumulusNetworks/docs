---
title: Quick Start
author: NVIDIA
weight: 20
product: NVIDIA Air
---

## Supported Browsers

The following browsers are fully supported:

- Google Chrome 120 or later
- Mozilla Firefox 121 or later

The following browsers are supported on a best-effort basis:

- Microsoft Edge 
- Safari

## Log in to Air

To log in, go to [air.nvidia.com](https://air.nvidia.com/). Enter your business email address, then click **Next**. <!--include air inside login path?-->

{{<img src="/images/guides/nvidia-air/Login.png" alt="" width="800px">}}

{{%notice note%}}
If your email address is not accepted as a valid business email address and you think this is an error, contact [air-support@nvidia.com](mailto:air-support@nvidia.com)
{{%/notice%}}

## Network Simulations

After you log in, Air displays a list of simulations associated with your account.

### Create a Simulation

There are two main ways to create simulations: you can either build a custom topology from scratch or load a pre-configured demo from the [Demo Marketplace](https://air.nvidia.com/demos) and customize it as you'd like.

- To learn how to create custom topologies and simulations using Air's drag-and-drop editor, see [Custom Topology](https://docs.nvidia.com/networking-ethernet-software/nvidia-air/Custom-Topology/).
- To learn about pre-configured simulations that you can clone and customize, see [Pre-Built Demos](https://docs.nvidia.com/networking-ethernet-software/nvidia-air/Pre-Built-Demos).

### Navigate Simulations

After you create a simulation, you can power it on or off, edit it, share it with others, or delete it by selecting the simulation's **Actions** {{<img src="/images/guides/nvidia-air/ActionsButton.png" alt="">}} menu.

{{<img src="/images/guides/nvidia-air/SimulationsActionHighlight.png" alt="action menu displaying options to stop, edit, or delete the simulation">}}
<br>

Select a simulation's name to load the simulation. You can choose between the **Topology**, **Nodes**, or **Links** tabs to view the simulation as a topology, a list of nodes, or a list of links, respectively. 

The timer displays when your simulation will automatically sleep, or enter a stored status to conserve system resources. You can extend the amount of time that your simulation is active by selecting the timer's three-dot menu, then clicking **Add Time**. You can also reposition the timer by dragging it to a different part of the screen.

Select a node to open a side panel which displays the node's properties, including its operating system, number of CPUs, memory and storage capacities, and connectors.

{{<img src="/images/guides/nvidia-air/NodesTopology.png" alt="">}}
<br>
<br>
Simulations from the Demo Marketplace typically include a simulation guide that appears when you first load the simulation. If you close the guide, you can access it again by navigating to the **Topology** tab. From the top of the dashboard, select **Workspace > Simulation Guide**.

### Node Consoles

Double-click any node to connect to its console.

Click the {{<img src="/images/guides/nvidia-air/LoginCredsButton.png" alt="information"  width="32px" >}} icon to view its login credentials. 
 
Click the {{<img src="/images/guides/nvidia-air/PopoutButton.png" alt="pop-out"  width="32px" >}} button to open the console in its own window.

{{<img src="/images/guides/nvidia-air/Console.png" alt="example console with login prompt"  width="800px" >}}

### Services

You can enable services to create external connections to your simulation. By enabling services, you can allow for integrations, such as using a preferred SSH client to access your simulation, running Grafana, or setting up SNMP polling.

To add a new service to your simulation:

1. Load the simulation, then select **Services > New Service**.

{{<img src="/images/guides/nvidia-air/ServicesDropdown.png" alt=""  width="450px" >}}

Enter the fields to create a service.

- **Service Name**: Name for your service. After you name a service, you can choose to run multiple instances of the same service on different interfaces or ports.
- **Interface**: Where the connection terminates. Typically `eth0` on the `oob-mgmt-server`.
- **Service Type**: Type of service. NVIDIA Air creates a hyperlink to the URL automatically in the services panel for _SSH_, _HTTP_, or _HTTPS_ services. For _Other_ services, any port can be used, but Air will not generate a hyperlink. The hyperlink provides a convenient way to copy and paste the service if your browser supports it.
- **Service Port**: Internal port where the service terminates.

2. Click **Create**.

{{<img src="/images/guides/nvidia-air/ServicesAdd.png" alt=""  width="450px" >}}
<br>
<br>
To enable SSH into the `oob-mgmt-server`, click **Services > Enable SSH**. Note that this option is only available when the out-of-band network is enabled. SSH password authentication is disabled on the `oob-mgmt-server` by default. To use SSH password authentication, you must upload SSH keys to your user profile; for more information, see [SSH Keys](#ssh-keys).

To view existing services enabled on the simulation, click **Services > Services List**. From here, you can also view access information such as the external port and host connections.

{{<img src="/images/guides/nvidia-air/ServicesList.png" alt="">}}

### Rebuild and Reset Nodes

Rebuilding a node restores the node to its original or default configuration. If the node was created from a demo or other snapshot, rebuilding it will revert the node to its original configuration. Resetting a node performs a hard reboot to the node.

From a loaded simulation, select a node to view its node properties. Click **Advanced Options > Actions** to rebuild or reset the node.

{{<img src="/images/guides/nvidia-air/RebuildReset.png" alt=""  width="450px" >}}
<br>
<br>
You can also rebuild all nodes in a simulation simultaneously by selecting **Workspace > Rebuild All Nodes**.

### Edit Simulations

From a simulation, click **Workspace > Edit Simulation** to edit any of the following attributes:

- **Name**: Edit the simulation's name. Simulations can share the same name. Air assigns a unique identifier to each simulation to differentiate between them.
- **Organization**: Assign the simulation to an organization. This will assign this exact simulation to an organization. The simulation that is assigned to the organization is not a copy or clone of the simulation. This means that each user with appropriate permissions will have access to the simulation and may edit it. For more information, refer to [Organizations](https://docs.nvidia.com/networking-ethernet-software/nvidia-air/Organizations). 
- **Sleep date**: When the simulation will be automatically put to sleep. This means the state of the simulation is saved but stored to free up account resources.
- **Expiration date**: When the simulation will be automatically deleted.

You can also edit your simulation from the **Simulations** page by selecting **Actions {{<img src="/images/guides/nvidia-air/ActionsButton.png" alt="">}} > Edit Simulation**.

{{<img src="/images/guides/nvidia-air/EditSim.png" alt=""  width="500px" >}}

### Share Simulations

Sharing a simulation allows other users to view and interact with a simulation. When sharing a simulation, you can choose to give users read-only access, which means they cannot modify the simulation (for example, by deleting it or assigning it to an organization). Note that users with read-only access have access to node consoles, where they can run commands to modify the simulation. To share a simulation with a group of users, see [Organizations](https://docs.nvidia.com/networking-ethernet-software/nvidia-air/Organizations).

To share a simulation: 

1. Load the simulation you want to share. Then click **Workspace > Manage Users**.
2.	Enter the email addresses for the users with whom you would like to share the simulation.
3.	Select whether to give the users read-only access.
4.	Click **Add User**.
5.	Click **Close** when finished.

{{<img src="/images/guides/nvidia-air/ManageUsers.png" alt="" width="600px">}}
<br>
<br>
Users will see the simulation listed in their [Simulations](https://air.nvidia.com/simulations) list. The user will not receive any notification that they were given access to the simulation. <!--why not if they entered their email?--> 

## API Tokens

API tokens allow you to execute authenticated activities using the NVIDIA Air API or SDK. Click your username in the UI and select **Settings** to view your API tokens.

To generate an API token, enter the **Name** and **Expiration Date** fields, then click **Create**. Save your token somewhere safe. You will not be able to view it again.

{{<img src="/images/guides/nvidia-air/APIToken.png" alt="" width="1000px">}}

## SSH Keys

Click your username in the UI and select **Settings** to view your SSH keys. To enable the SSH service on simulations, you must add SSH keys to your authentication settings. Any SSH keys that you add are automatically included in your simulation's list of authorized keys under the `oob-mgmt-server`.

To add an SSH key, enter the **Name** and **Public Key** fields, then select **Add**.

{{<img src="/images/guides/nvidia-air/SSHKey.png" alt="" width="1000px">}}
<br>
<br>
You can revoke or delete both API tokens and SSH keys if you no longer need them, or if they become compromised.

## Resource Budgets

The number of simulation resources a user is allotted is tied to the user's account. For an account using a valid business email, a user is granted the following limits:

- 60 vCPUs
- 90 GB memory
- 650 GB storage
- 4 running simulations

NVIDIA employees are granted the following limits:

- 100 vCPUs
- 100 GB memory
- 1 TB storage
- 5 running simulations

[Organizations](https://docs.nvidia.com/networking-ethernet-software/nvidia-air/Organizations) have the largest resource budgets and can accommodate large simulations. The default resource budget for an organization is:

- 300 vCPUs
- 300 GB memory
- 3 TB storage
- 10 GB image storage
- 15 running simulations

If you need to expand an organization's resources beyond the default resource budget, contact the Air Support team at [air-support@nvidia.com](mailto:air-support@nvidia.com).

## Related Information

- [Cumulus Linux in a Virtual Environment](https://docs.nvidia.com/networking-ethernet-software/cumulus-linux/Cumulus-Linux-in-a-Virtual-Environment/)
