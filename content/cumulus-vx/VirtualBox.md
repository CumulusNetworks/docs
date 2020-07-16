---
title: VirtualBox
author: Cumulus Networks
weight: 15
---
To use Cumulus VX with VirtualBox, perform the following configuration:

- Create the VMs
- Create connections between the VMs
- Test the network connections

The following steps were tested with VirtualBox-6.0.24.

## Create the VMs

The following procedure describes how to create a VM in VirtualBox for each switch in the example topology (Leaf01, Leaf02, and Spine01). This section assumes a basic level of VirtualBox experience.

1. Download and install VirtualBox. Refer to the {{<exlink url="https://www.virtualbox.org/wiki/Downloads" text="VirtualBox documentation">}}.

2. From the {{<exlink url="https://cumulusnetworks.com/products/cumulus-vx/download/" text="Cumulus Networks website">}}, download the OVA disk image to run Cumulus VX within VirtualBox.

3. Open the VirtualBox application and select **Import Appliance** from the **File** menu.

4. Browse for the OVA disk image you installed in the previous step, click the **Open** button, then click **Continue**.

5. In the Appliance settings, change the name of the VM to `Leaf01`, then click **Import** to begin the import process.  

   {{< img src = "/images/cumulus-vx/VirtualBox-review.png" >}}

6. In the VirtualBox Manager window, right click the created `Leaf01` VM, then select **Clone**.

7. Change the name of the VM to `Leaf02`, then click **Continue**.

8. Select **Full Clone** and click **Clone**.

9. Repeat steps 6 through 8 to create `Spine01`.

## Create Connections Between VMs

Configure the network adapter settings for Leaf01, Leaf02, and Spine01 to create point-to-point connections.

{{%notice note%}}

Make sure that the VM is powered off.

{{%/notice%}}

Follow these steps for each VM (Leaf01, Leaf02, and Spine01):

1. In the VirtualBox Manager window, select Leaf01.

2. Click **Settings**, then click **Network**.

3. Click **Adapter 2**.

4. Make sure the **Enable Network Adapter** check box is selected.

5. From the **Attached to** list, select **Internal Network**.  

6. In the **Name** field, enter a name for the internal network, then click **OK**. The example below uses `intnet-1`.

   The internal network name must match the internal network name on the corresponding network adapter on the VM to be connected to this VM. For example, in the two-leaf and one spine topology, Adapter 2 (swp1) on Leaf01 is connected to Adapter 2 (swp1) on Spine01; the name must be the same for Adapter 2 on both VMs. Use the internal network names and the connections shown in the illustration and table below.

   {{< img src = "/images/cumulus-vx/adapterSettings.png" >}}

7. Repeat steps 2 through 6 for Leaf02 and Spine02 using the internal network names and the connections shown in the illustration and table below.

{{< img src = "/images/cumulus-vx/VX-Connections.png" >}}

| Switch    | swp      | VirtualBox Interface | VirtualBox Network Type | Name     |
| --------- | ----     | -------------------- | ----------------------- | -------- |
| Leaf01    |          | Adapter 1            | NAT                     |          |
|           | swp1     | Adapter 2            | Internal                | intnet-1 |
| Leaf02    |          | Adapter 1            | NAT                     |          |
|           | swp1    |  Adapter 2            | Internal                | intnet-2 |
| Spine01   |          | Adapter 1            | NAT                     |          |
|           | swp1     | Adapter 2            | Internal                | intnet-1 |
|           | swp2     | Adapter 3            | Internal                | intnet-2 |

{{%notice note%}}

You can also add a VM to one or more internal virtual networks in VirtualBox by cloning the VM. However, consider the following if you prefer to clone VMs:

- To set up configurations quickly across multiple nodes, configure the settings for the original VM, then clone it using **Machine \> Clone**. For example, if a management VM is being created for the new topology, set the `eth0` port to be on a virtual network that the management VM is on. When you clone the new VM, the port will be duplicated, creating an out-of-band (OOB) network.
- When you clone the VM, save the new VM on disk storage by referring to the original disk image, instead of copying it to the new VM.
- Always reset MAC addresses on the virtual NICs, unless a critical reason not to exists.

{{%/notice%}}

## Basic Switch Configuration

After you have created the three VMs, log into Leaf01, Leaf02, and Spine 01 with the `cumulus` account and default password `CumulusLinux!` and then perform the following basic configuration:

- Change the hostname
- Bring up swp1 and swp2
- Check the connections

### Change the Hostname

Run the following command on each VM:

```
net add hostname <name>
net commit
```

### Bring up the Interfaces

Run the following command to bring up swp1 and swp2 on each VM:

   ```
   net add interface swp1, swp2
   net commit
   ```




## Next Steps
