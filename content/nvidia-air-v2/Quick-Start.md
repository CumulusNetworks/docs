---
title: Quick Start
author: NVIDIA
weight: 20
product: NVIDIA Air 2.0
---

## Supported Browsers

NVIDIA Air fully supports the following browsers:
- Google Chrome 120 or later
- Mozilla Firefox 121 or later

NVIDIA Air supports the following browsers on a best-effort basis:
- Microsoft Edge
- Safari

## Log in to Air

Go to {{<exlink url="https://air-ngc.nvidia.com" text="air-ngc.nvidia.com">}} and click **Login**. Air uses NGC for authentication—sign in with your business email and select your NGC organization.

For first-time setup, free trials, and troubleshooting access issues, see {{<link title="Account Setup">}}.

## Network Simulations

After you log in, Air displays a list of simulations associated with your account.

### Create a Simulation

To create a simulation, you can either:
- Build a custom topology; see [Custom Topology](https://docs.nvidia.com/networking-ethernet-software/nvidia-air/Custom-Topology/).
- Load a pre-configured demo from the [Demo Marketplace](https://air-ngc.nvidia.com/demos) and customize it; see [Pre-Built Demos](https://docs.nvidia.com/networking-ethernet-software/nvidia-air/Pre-Built-Demos).

### Navigate Simulations

To interact with your simulation, select the **Topology** tab. This tab provides a variety of options, including options to start and stop the simulation, share it with other users, export it as a JSON file, and ways to access additional features.

{{<img src="/images/guides/nvidia-air-v2/SimulationActions.png" alt="">}}

For detailed information about simulation states, checkpoints, and history, see {{<link title="Simulation Management">}}.

### Nodes and Consoles

Select a node to open a side panel that displays the node's properties, including its operating system, number of CPUs, memory and storage capacities, and connectors.

{{<img src="/images/guides/nvidia-air-v2/NodesTopology.png" alt="">}}
<br>
<br>
Double-click any node to connect to its console.

{{<img src="/images/guides/nvidia-air-v2/Console.png" alt="example console with login prompt"  width="800px" >}}

### Services

Enable services to create external connections to your simulation to support integrations: for example, you can use your preferred SSH client to access the `oob-mgmt-server`, run and access web applications such as Grafana or Kibana, or configure SNMP polling.

To add a new service to your simulation:

1. In a loaded simulation, select the **Services** tab, then click **+ New Service**.

{{<img src="/images/guides/nvidia-air-v2/ServicesDropdown.png" alt="" >}}

2. Enter the following information to create a service:
- **Service Name** is the name for your service. After you name a service, you can choose to run multiple instances of the same service on different interfaces or ports.
- **Interface** is where the connection terminates; typically `eth0` on the `oob-mgmt-server`.
- **Service Type** is the service type. NVIDIA Air creates a hyperlink to the URL automatically in the services panel for _SSH_, _HTTP_, or _HTTPS_ services. For _Other_ services, you can use any port, but Air does not generate a hyperlink. The hyperlink provides a convenient way to copy and paste the service if your browser supports it.
- **Service Port** is the internal port where the service terminates. 

Click **Create**.

Air displays the information needed to access the service you created.

{{<img src="/images/guides/nvidia-air-v2/ServicesList.png" alt="">}}
<br>
<br>
To enable SSH in the `oob-mgmt-server`, click **Enable SSH**. This option is only available when the out-of-band network is enabled. SSH password authentication is disabled on the `oob-mgmt-server` by default. To use SSH password authentication, you must upload SSH keys to your user profile; for more information, see [SSH Keys](#ssh-keys).

### Rebuild and Reset Nodes

Rebuilding a node restores the node to its original or default configuration. If you create the node from a demo or other snapshot, rebuilding it reverts the node to its original configuration. Resetting a node performs a hard reboot to the node.

From a loaded simulation, click the hamburger menu on a node to view rebuild and reset options.

{{<img src="/images/guides/nvidia-air-v2/RebuildReset.png" alt=""  width="450px" >}}
<br>
<br>
You can also rebuild all nodes in a simulation simultaneously by clicking the {{<img src="/images/guides/nvidia-air-v2/RebuildAllNodes.png" alt="" width="22px" >}} **Rebuild All Nodes** button in the **Topology** tab.

### Edit Simulations

You can edit important attributes of a simulation with the {{<img src="/images/guides/nvidia-air-v2/Edit.png" alt="" width="22px" >}} **Edit** button in the **Topology** tab.
- **Simulation Name** is the simulation name. Simulations can share the same name. Air assigns a unique identifier to each simulation to differentiate between each one.
- **Sleep date** is when the simulation goes into sleep mode automatically; Air saves the state of the simulation and stores it to free up account resources.

{{<img src="/images/guides/nvidia-air-v2/EditSim.png" alt="" width="400px">}}

## API Authentication

To authenticate with the NVIDIA Air API, use NGC API keys. For detailed information about generating and using API keys, see {{<link title="API Authentication">}}.

## SSH Keys

To view your SSH keys, click your username in the UI and select **Settings**. To enable the SSH service on simulations, you must add SSH keys to your authentication settings. Any SSH keys that you add are included automatically in your simulation's list of authorized keys under the `oob-mgmt-server`.

To add an SSH key, fill in the **Name** and **Public Key** fields, then select **Add**.

{{<img src="/images/guides/nvidia-air-v2/SSHKey.png" alt="" width="1000px">}}
<br>
<br>
You can delete SSH keys if you no longer need them, or if they become compromised.

## Resource Budgets

The number of simulation resources allotted to a user is tied to the user's account. For an account using a valid business email, Air allocates the following resource budget:
- 60 vCPUs
- 90 GB memory
- 650 GB storage
- 4 running simulations

NGC organizations have the largest resource budgets and can accommodate large simulations. The default resource budget for an organization is:
- 300 vCPUs
- 300 GB memory
- 3 TB storage
- 10 GB image storage
- 15 running simulations

If you need to expand the resources for an organization beyond the default resource budget, contact the Air Support team at [air-support@nvidia.com](mailto:air-support@nvidia.com).

## Related Information

- [Cumulus Linux in a Virtual Environment](https://docs.nvidia.com/networking-ethernet-software/cumulus-linux/Cumulus-Linux-in-a-Virtual-Environment/)
