---
title: VirtualBox
author: Cumulus Networks
weight: 15
---
To use Cumulus VX with VirtualBox, you need to perform the following configuration:

- Create the VMs
- Create connections between the VMs
- Test the connections
- Configure OSPF and FRRouting

## Create VMs with VirtualBox

The following procedure describes how to create a VM in VirtualBox for each switch in the example topology (Leaf01, Leaf02, and Spine01). This section assumes a basic level of VirtualBox experience.

1. Download and install VirtualBox. Refer to the {{<exlink url="https://www.virtualbox.org/wiki/Downloads" text="VirtualBox documentation">}}.

2. Download the OVA disk image for use with VirtualBox from the {{<exlink url="https://cumulusnetworks.com/products/cumulus-vx/download/" text="Cumulus Networks website">}}.

3. Open VirtualBox and click **File \> Import Appliance**.

4. Browse for the downloaded VirtualBox image, click the **Open** button, then click **Continue**.

5. Review the Appliance settings. Change the name of the VM to `Leaf01`, then click **Import** to begin the import process.  

   {{< img src = "/images/cumulus-vx/VirtualBox-review.png" >}}

6. Right click the created `Leaf01` VM, then select **Clone**.

7. Change the name of the VM to `Leaf02`, then click **Continue**.

8. Select **Full Clone** and click **Clone**.

9. Repeat steps 6-8 for Spine01:

## Create Connections Between VMs

To use the network topology you configured above, you need to configure the network adapter settings for each VM to create point-to-point connections. The following example shows how to create point-to-point connections between each VM in VirtualBox.

{{%notice note%}}

Make sure that the VM is powered off.

{{%/notice%}}

Follow these steps for each VM:

1. In the VirtualBox Manager window, select the VM.

2. Click **Settings**, then click **Network**.

3. Click **Adapter 2**.

4. Click the **Enable Network Adapter** check box.

5. From the **Attached to** list, select **Internal Network**.  

    {{< img src = "/images/cumulus-vx/adapterSettings.png" >}}

6. In the **Name** field, type a name for the internal network, then click **OK**.

   The internal network name must match the internal network name on the corresponding network adapter on the VM to be connected to this VM. For example, in the two-leaf and one spine topology, Adapter 2 (swp1) on Leaf01 is connected to Adapter 2 (swp1) on Spine01; the name must be the same for Adapter 2 on both VMs. Use the internal network names and the connections shown in the illustration and table below.

7. Click **Adapter 3** and repeat steps 4 thru 6. Use the internal network names and the connections shown in the illustration and table below.

{{< img src = "/images/cumulus-vx/mapping.png" >}}

| Switch    | swp      | VirtualBox Interface | VirtualBox Network Type | Name     |
| --------- | ----     | -------------------- | ----------------------- | -------- |
| Leaf01    |          | Adapter 1            | NAT                     |          |
|           | swp51    | Adapter 2            | Internal                | Intnet-1 |
| Leaf02    |          | Adapter 1            | NAT                     |          |
|           | swp51    | Adapter 2            | Internal                | Intnet-2 |
| Spine01   |          | Adapter 1            | NAT                     |          |
|           | swp1     | Adapter 2            | Internal                | Intnet-1 |
|           | swp2     | Adapter 3            | Internal                | Intnet-2 |

You can also add a VM to one or more internal virtual networks in VirtualBox by cloning the VM. However, consider the following if you prefer to clone VMs:

{{%notice note%}}

- To set up configurations quickly across multiple nodes, configure the settings for the original VM, then clone it using **Machine \> Clone**. For example, if a management VM is being created for the new topology, set the `eth0` port to be on a virtual network that the management VM is on. When you clone the new VM, the port will be duplicated, creating an out-of-band (OOB) network.
- When you clone the VM, save the new VM on disk storage by referring to the original disk image, instead of copying it to the new VM.
- Always reset MAC addresses on the virtual NICs, unless a critical reason not to exists.

{{%/notice%}}

## Test Network Connections

{{% vx-test-connections %}}

## Configure OSPF and FRRouting

{{% vx-conf-routing %}}

## Next Steps
