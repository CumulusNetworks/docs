---
title: Custom Topology
author: NVIDIA
weight: 40
version: "1.0"
---

NVIDIA Air fully supports the creation of custom topologies. This feature augments the pre-built demo infrastructure.

To access the custom topologies click on the `Create your own` card in the `Create a Simulation` menu:

{{<img src="/images/guides/nvidia-air/BuildaTopology.png" width="800px">}}

Alternatively, go directly by following this link:  {{<exlink url="https://air.nvidia.com/build" text="air.nvidia.com/build">}}.

## Custom Topology Landing Page

The custom topology landing page is a blank canvas that you can use to design any network.

{{<img src="/images/guides/nvidia-air/CustomTopology.png" width="800px">}}

### Canvas Overview

The left panel for custom topologies contains the supported nodes used for creating the custom topology:

- Cumulus VX switches
- Ubuntu servers
- SONiC switches
- Generic nodes

{{<img src="/images/guides/nvidia-air/CustomTopology_LeftPanel.png" width="150px">}}

The toolbar at the top manages the topology. Clicking the default name **My Topology Project** provides additional management options.

{{<img src="/images/guides/nvidia-air/CustomTopology_Management.png" width="500px">}}

- **Open Build**: Uploads a JSON-structured custom topology build. This is not the same as importing a `topology.dot` GraphViz format document. The JSON format structure is unique to the custom topology builder tool.
- **Save Build**: Exports a JSON-structured custom topology that represents the canvas. This exported JSON file is designed to be read in only by the custom topology builder application. While you can open and edit it in a text editor, it should only be interpreted by the custom topology builder application.
- **Export Build**: Exports the topology as a GraphViz format `topology.dot` file. This file can be imported into the Air simulation platform to launch a custom topology.
- **Download SVG**: Downloads an image in SVG format that defines your topology.
- **Rename Project**: Renames the project from the default of *My Topology Project*.
- **New Project**: Creates a new project.

### Add Nodes

To add a node, drag and drop it from the left panel.

{{<img src="/images/guides/nvidia-air/CustomTopology_AddingNodes.png" width="800px">}}

### Edit Nodes

Once a node has been added, you can edit it as needed. Click the node to select it and configure it using the options in the right panel.

{{<img src="/images/guides/nvidia-air/CustomTopology_EditingNodes.png" width="800px">}}

- **Name**: The hostname of the node.
- **OS**: The operating system version on the node. The supported OS versions are in a drop down list.

  {{<img src="/images/guides/nvidia-air/CustomTopology_NodeOS.png" width="800px">}}

- **Memory**: The amount of RAM on the node. The default is 1GB.
- **CPU**: The number of CPUs allocated to the node. The default is 1 CPU.
- **Role**: This is an advanced feature to define the role of the node to affect boot order. You typically don't have to assign a role.

  {{<img src="/images/guides/nvidia-air/CustomTopology_Role.png" width="800px">}}

- **Ports**: Add, rename and edit port location and information for the diagram.

### Connect Nodes

To connect two nodes together, click a port on one node and drag it to the port on the other node. This draws a line between the two ports to show the connection.

{{<img src="/images/guides/nvidia-air/CustomTopology_Link.png" width="800px">}}

### ZTP Script

A custom ZTP script can be included as part of the network design. This ZTP script will be copied, exactly as pasted into the text box, onto the `oob-mgmt-server` during simulation creation. Any network node making a ZTP request on the OOB management  network will have access to this ZTP script through a DHCP server and WWW server running on the `oob-mgmt-server`.

To upload a ZTP script, click the ZTP script button in the top right of the canvas:

{{<img src="/images/guides/nvidia-air/ZTP.png" width="500px">}}

This will open up a popup window to put in the ZTP script. The popup window will already be populated with a default script. The default script is designed as a guide to implement common ZTP features on Cumulus Linux, including:

* Disable password expirey
* Make `cumulus` user passwordless sudo
* Download SSH keys for key based SSH

{{<img src="/images/guides/nvidia-air/ZTPPopup.png" width="800px">}}

Once a ZTP script is applied, the ZTP button will change colors from grey to green, indicating that ZTP is now active on your `oob-mgmt-server`.

{{<img src="/images/guides/nvidia-air/ZTPActive.png" width="500px">}}

## Build a Custom Topology

To build a custom topology, choose one of these two options:

- Start a simulation directly from the topology builder
- Export the topology files and upload them directly into Air

{{<img src="/images/guides/nvidia-air/StartSimulation.png" width="500px">}}

### Start a Simulation Directly

To start a simulation directly from the topology builder, click the `Start Simulation` button. This automatically launches the simulation and redirects to the Air landing page. The topology and the diagram are automatically linked to your simulation, so no additional work is required.

### Export a Custom Topology

To export a custom topology, first download the requisite files. Click `Export` in the top right button.

This exports two files for download:

- `topology.dot` - Network definition in GraphViz format
- `topology.svg` - Network diagram in Scalable Vector Graphics format

You can upload both files file into Air via the `Create Simulation` workflow. First, click the `Upload Topology` card:

{{<img src="/images/guides/nvidia-air/UploadTopology1.png" width="400px">}}

Then upload the `topology.dot` and `topology.svg` files to the proper locations (drag the `topology.dot` file onto the **Drop a topology file here...** card and the `topology.svg` file onto the **Drop a diagram here...** card):

{{<img src="/images/guides/nvidia-air/UploadTopology2.png" width="400px">}}

## NetQ Integration

You can include NetQ with any simulation. To do this, drag the `node` icon into the canvas and change the `OS` field to a NetQ version.

{{<img src="/images/guides/nvidia-air/NetqCustomTopo.png" width="225px">}}

No additional connectivity is required to get NetQ functionality. The only requirement is the existence of a NetQ node. As long as the NetQ node is defined in the simulation, the platform automatically creates the NetQ agents and does the registration.
