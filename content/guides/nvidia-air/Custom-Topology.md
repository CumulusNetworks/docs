---
title: Custom Topology
weight: 40
version: "1.0"
draft: true
---

NVIDIA Air has full support to launching custom topologies. This feature augments the pre-build demo infrastructure.

To access the custom topologies, go to the link https://air.nvidia.com/build

## Custom Topology Landing Page

The custom topology landing page is a blank canvas that can be used to design any network.

{{<img src="/images/guides/nvidia-air/CustomTopology.png" >}}

### Canvas Overview

The left panel for custom topology is where the supported nodes are located.

{{<img src="/images/guides/nvidia-air/CustomTopology_LeftPanel.png" >}}

The top panel manages the topology. Clicking on the default name `My Topology Project` provides additional management options.

{{<img src="/images/guides/nvidia-air/CustomTopology_Management.png" >}}

* Open Build - Lets a user input a JSON structured custom topology build. Note, this is not the same as importing in a topology.dot GraphViz format document. The JSON format structure is unique to the custom topology builder tool.
* Save Build - Lets a user export a JSON structured custom topology as per the canvas. This exported JSON file is designed to be read in only by the custom topology builder application. It can be opened and edited by a text editor, but is meant to be interpretted by the custom topology builder application.
* Export Build - Lets a user export the topology as a GraphViz format topology.dot file. This file can be imported into the Air simulation platform to launch a custom topology.
* Download SVG - Lets the user download an image in SVG format that defines their topology.
* Rename Project - Renames the project from the default of `My Topology Project` to user preference.
* New Project - Creates a new project.

### Adding Nodes

Nodes can be added to the custom by dragging and dropping from the left panel. 

{{<img src="/images/guides/nvidia-air/CustomTopology_AddingNodes.png" >}}

### Editing Nodes

Once a node has been added, it can be edited for function.

{{<img src="/images/guides/nvidia-air/CustomTopology_EditingNodes.png" >}}

* Name - The hostname of the node.
* OS - The version of the node. The OS versions available are in a drop down of pre-selected supported versions.

{{<img src="/images/guides/nvidia-air/CustomTopology_NodeOS.png" >}}

* Memory - The memory of the node. The default is 1Gb.
* CPU - The number of CPUs allocated to the node. The default is 1 CPU.
* Role - This is an advanced feature to define the role of the node to affect bootup order. This is not necessary to be populated in most cases.

{{<img src="/images/guides/nvidia-air/CustomTopology_Role.png" >}}

* Ports - Add, rename and edit port location and information for the diagram.

### Connecting Nodes

To connect two nodes together, use your mouse to click and drag the two ports that should be connected. This willd raw a line between the two ports.

{{<img src="/images/guides/nvidia-air/CustomTopology_Link.png" >}}

## Exporting a Custom Topology

To export a custom topology, click on the `Export` button referenced in {{<link text="Canvas Overview" title="### Canvas Overview" >}}. This lets you report the topology on the canvas as a GraphViz format.

{{<img src="/images/guides/nvidia-air/CustomTopology_Export.png" >}}

### Building a Custom Topology

To build a custom topology, reach out to your local NVIDIA Solutions Architect as they can take the exported topology.dot file and get it loaded into Air. If you don't know who you're local Solutions Architect is, contact NVIDIA Air Support.com for assistance by clicking `Report an issue`.

{{<img src="/images/guides/nvidia-air/ReportAnIssue.png" >}}
