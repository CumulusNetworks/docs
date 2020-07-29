---
title: VirtualBox
author: Cumulus Networks
weight: 15
---
This section describes how to install and set up Cumulus VX in VirtualBox to create the two leaf and one spine topology shown below.

{{% vx/intro %}}

These steps were tested with VirtualBox version 6.1.12 on macOS version 10.14.6.

## Create and Configure the VMs

The following procedure creates leaf01, leaf02, and spine01 and the network connections between them. This section assumes a basic level of VirtualBox experience.

### Download and Install the Software

1. Download and install {{<exlink url="https://www.virtualbox.org/wiki/Downloads" text="VirtualBox">}}.

2. Download the {{<exlink url="https://cumulusnetworks.com/products/cumulus-vx/download/" text="OVA VirtualBox image">}}.

### Create the VMs

{{% vx/virtualbox-steps %}}

### Create Network Connections

Configure the network adapter settings for leaf01, leaf02, and spine01 to create point-to-point connections.

{{%notice note%}}

Make sure that the VM is powered off.

{{%/notice%}}

1. In the VirtualBox Manager window, select leaf01.

2. Click **Settings**, then click **Network**.

3. Click **Adapter 2**.

4. Make sure the **Enable Network Adapter** check box is selected.

5. From the **Attached to** list, select **Internal Network**.  

6. In the **Name** field, enter a name for the internal network, then click **OK**. The example below uses `intnet-1`.

   {{< img src="/images/cumulus-vx/adapterSettings.png" width="400" >}}

7. Repeat the steps 1 through 6 for leaf02 and spine01. Use the internal network names and the connections shown in the illustration and table below.

   The internal network name for an adapter on a VM must match the internal network name on the corresponding network adapter on the VM to which it connects. For example, in the two leaf and one spine topology, Adapter 2 (swp1) on leaf01 is connected to Adapter 2 (swp1) on spine01; the name (intnet-1) must be the same for Adapter 2 on both VMs.

{{< figure src = "/images/cumulus-vx/VX-Connections.png" >}}

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

## Log into the Switches

{{% vx/login %}}

## Basic Switch Configuration

{{% vx/basic-config %}}

## Verify Configuration

{{% vx/verify-config %}}

## Next Steps

{{% vx/next-steps %}}
