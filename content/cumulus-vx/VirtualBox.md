---
title: VirtualBox
author: Cumulus Networks
weight: 15
---
This section describes how to install and set up Cumulus VX in VirtualBox to create the two leaf and one spine topology shown below.

{{% vx/intro %}}

These steps were tested with VirtualBox version 6.1.12 on macOS version 10.14.6.

## Create and Configure the VMs

The following procedure creates leaf01, leaf02, and spine01 and the network connections between them. This section assumes you have a basic level of VirtualBox experience.

### Download and Install the Software

1. Download and install {{<exlink url="https://www.virtualbox.org/wiki/Downloads" text="VirtualBox">}}.

2. Download the {{<exlink url="https://cumulusnetworks.com/products/cumulus-vx/download/" text="OVA VirtualBox image">}}.

### Create the VMs

{{% vx/virtualbox-steps %}}

### Create Network Connections

Configure the network adapter settings for leaf01, leaf02, and spine01 to create point-to-point connections, as shown below.

{{< figure src = "/images/cumulus-vx/VX-Connections.png" >}}

Follow these steps for each VM (leaf01, leaf02, and spine01):

1. In the VirtualBox Manager window, select the VM.

2. Click **Settings**, then click **Network**.

3. Configure the **Adapters** as shown in the table below, then click **OK**.

   For each adapter, make sure the **Enable Network Adapter** check box is selected. For Adapter 2, 3, and 4, make sure  **Internal Network** is selected in the **Attached to** dropdown.

   | Switch    | swp      | VirtualBox Interface | VirtualBox Network Type | Internal Network Name |
   | --------- | ----     | -------------------- | ----------------------- | --------------------- |
   |leaf01     |          | Adapter 1            | NAT                     |                       |
   |           | swp1     | Adapter 2            | Internal                | intnet-1              |
   |           | swp2     | Adapter 3            | Internal                | intnet-3              |
   |           | swp3     | Adapter 4            | Internal                | intnet-4              |
   |leaf02     |          | Adapter 1            | NAT                     |                       |
   |           | swp1     | Adapter 2            | Internal                | intnet-2              |
   |           | swp2     | Adapter 3            | Internal                | intnet-3              |
   |           | swp3     | Adapter 4            | Internal                | intnet-4              |
   |spine01    |          | Adapter 1            | NAT                     |                       |
   |           | swp1     | Adapter 2            | Internal                | intnet-1              |
   |           | swp2     | Adapter 3            | Internal                | intnet-2              |

4. Start the VMs.

## Log into the Switches

{{% vx/login %}}

## Basic Switch Configuration

{{% vx/basic-config %}}

## Verify Configuration

{{% vx/verify-config %}}

## Next Steps

{{% vx/next-steps %}}
