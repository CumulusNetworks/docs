---
title: VirtualBox
author: Cumulus Networks
weight: 15
---
This section describes how to download Cumulus VX and create a VM in VirtualBox for each switch in the two-leaf and one spine topology shown below.

{{% vx-intro %}}

These steps were tested with VirtualBox version 6.1.12 on macOS version 10.14.6.

## Create the VMs

The following procedure describes how to create a VM in VirtualBox for each switch in the example topology (Leaf01, Leaf02, and Spine01). This section assumes a basic level of VirtualBox experience.

1. Download and install VirtualBox. Refer to the {{<exlink url="https://www.virtualbox.org/wiki/Downloads" text="VirtualBox documentation">}}.

2. From the {{<exlink url="https://cumulusnetworks.com/products/cumulus-vx/download/" text="Cumulus Networks website">}}, download the OVA disk image to run Cumulus VX within VirtualBox.

3. Open the VirtualBox application and select **Import Appliance** from the **File** menu.

4. Browse for the OVA disk image you installed in the previous step, click the **Open** button, then click **Continue**.

5. In the Appliance settings, change the name of the VM to `Leaf01`, then click **Import** to begin the import process.  

   {{< figure src="/images/cumulus-vx/VirtualBox-review.png" width="500" >}}

6. In the VirtualBox Manager window, right click the `Leaf01` VM, then select **Clone**.

7. Change the name of the VM to `Leaf02`, then click **Continue**.

8. Select **Full Clone** and click **Clone**.

9. Repeat steps 6 through 8 to create `Spine01`.

## Create Connections Between VMs

Configure the network adapter settings for Leaf01, Leaf02, and Spine01 to create point-to-point connections.

{{%notice note%}}

Make sure that the VM is powered off.

{{%/notice%}}

1. In the VirtualBox Manager window, select Leaf01.

2. Click **Settings**, then click **Network**.

3. Click **Adapter 2**.

4. Make sure the **Enable Network Adapter** check box is selected.

5. From the **Attached to** list, select **Internal Network**.  

6. In the **Name** field, enter a name for the internal network, then click **OK**. The example below uses `intnet-1`.

   {{< figure src="/images/cumulus-vx/adapterSettings.png" width="400" >}}

7. Repeat the steps 1 through 6 for Leaf02 and Spine01. Use the internal network names and the connections shown in the illustration and table below.

   The internal network name for an adapter on a VM must match the internal network name on the corresponding network adapter on the VM to which it connects. For example, in the two-leaf and one spine topology, Adapter 2 (swp1) on Leaf01 is connected to Adapter 2 (swp1) on Spine01; the name (intnet-1) must be the same for Adapter 2 on both VMs.

{{< figure src = "/images/cumulus-vx/VX-Connections.png" >}}

| Switch    | swp      | VirtualBox Interface | VirtualBox Network Type | Internal Network Name |
| --------- | ----     | -------------------- | ----------------------- | --------------------- |
|Leaf01     |          | Adapter 1            | NAT                     |                       |
|           | swp1     | Adapter 2            | Internal                | intnet-1              |
|           | swp2     | Adapter 3            | Internal                | intnet-3              |
|           | swp3     | Adapter 4            | Internal                | intnet-4              |
|Leaf02     |          | Adapter 1            | NAT                     |                       |
|           | swp1     | Adapter 2            | Internal                | intnet-2              |
|           | swp2     | Adapter 3            | Internal                | intnet-3              |
|           | swp3     | Adapter 4            | Internal                | intnet-4              |
|Spine01    |          | Adapter 1            | NAT                     |                       |
|           | swp1     | Adapter 2            | Internal                | intnet-1              |
|           | swp2     | Adapter 3            | Internal                | intnet-2              |

## Basic Switch Configuration

{{% vx-basic-config %}}

## Next Steps

{{% vx-next-steps %}}
