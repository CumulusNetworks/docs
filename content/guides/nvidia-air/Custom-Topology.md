---
title: Custom Topology
author: NVIDIA
weight: 40
version: "1.0"
---

NVIDIA Air fully supports the creation of custom topologies. This feature augments the pre-built demo infrastructure.

To access the custom topologies, go to {{<exlink url="https://air.nvidia.com/build" text="air.nvidia.com/build">}}.

## Custom Topology Landing Page

The custom topology landing page is a blank canvas that you can use to design any network.

{{<img src="/images/guides/nvidia-air/CustomTopology.png" width="800px">}}

### Canvas Overview

The left panel for custom topologies contains the supported nodes used for creating the custom topology:

- Cumulus VX switches
- Ubuntu servers
- SONiC switches
- Generic nodes

{{<img src="/images/guides/nvidia-air/CustomTopology_LeftPanel.png" >}}

The toolbar at the top manages the topology. Clicking the default name **My Topology Project** provides additional management options.

{{<img src="/images/guides/nvidia-air/CustomTopology_Management.png" >}}

- **Open Build**: Uploads a JSON-structured custom topology build. This is not the same as importing a `topology.dot` GraphViz format document. The JSON format structure is unique to the custom topology builder tool.
- **Save Build**: Exports a JSON-structured custom topology that represents the canvas. This exported JSON file is designed to be read in only by the custom topology builder application. While you can open and edit it in a text editor, it should only be interpreted by the custom topology builder application.
- **Export Build**: Exports the topology as a GraphViz format `topology.dot` file. This file can be imported into the Air simulation platform to launch a custom topology.
- **Download SVG**: Downloads an image in SVG format that defines your topology.
- **Rename Project**: Renames the project from the default of *My Topology Project*.
- **New Project**: Creates a new project.

### Add Nodes

To add a node, drag and drop it from the left panel.

{{<img src="/images/guides/nvidia-air/CustomTopology_AddingNodes.png" width="1000px">}}

### Edit Nodes

Once a node has been added, you can edit it as needed. Click the node to select it and configure it using the options in the right panel.

{{<img src="/images/guides/nvidia-air/CustomTopology_EditingNodes.png" width="1000px">}}

- **Name**: The hostname of the node.
- **OS**: The operating system version on the node. The supported OS versions are in a drop down list.

  {{<img src="/images/guides/nvidia-air/CustomTopology_NodeOS.png" width="1000px">}}

- **Memory**: The amount of RAM on the node. The default is 1GB.
- **CPU**: The number of CPUs allocated to the node. The default is 1 CPU.
- **Role**: This is an advanced feature to define the role of the node to affect boot order. You typically don't have to assign a role.

  {{<img src="/images/guides/nvidia-air/CustomTopology_Role.png" width="1000px">}}

- **Ports**: Add, rename and edit port location and information for the diagram.

### Connect Nodes

To connect two nodes together, click a port on one node and drag it to the port on the other node. This draws a line between the two ports to show the connection.

{{<img src="/images/guides/nvidia-air/CustomTopology_Link.png" width="1000px">}}

## Export a Custom Topology

To export a custom topology, click **Export Build** in the drop down referenced in {{<link text="Canvas Overview" title="#canvas-overview">}} above. This exports the custom topology in a GraphViz format so you can import it into the Air simulation platform to create a new custom topology.

{{<img src="/images/guides/nvidia-air/CustomTopology_Export.png" width="1000px">}}

### Build a Custom Topology

To build a custom topology, reach out to your local NVIDIA Solutions Architect to take the exported `topology.dot` file and load it into Air. If you don't know who your local Solutions Architect is, contact NVIDIA Air Support for assistance by clicking **Report an issue** on the landing page for your Air simulation.

{{<img src="/images/guides/nvidia-air/ReportAnIssue.png">}}
