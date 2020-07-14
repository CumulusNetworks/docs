---
title: GNS3 and VirtualBox
author: Cumulus Networks
weight: 40
---

INTRO

## Create VMs with GNS3 and VirtualBox

{{%notice note%}}

GNS3 overwrites the interface names that are configured in VirtualBox. If you want to use the VMs in VirtualBox and GNS3, consider cloning them first.

{{%/notice%}}

To run your virtual network under GNS3:

1. Download and install {{<exlink url="https://www.virtualbox.org" text="VirtualBox">}}.
2. Download the {{<exlink url="https://cumulusnetworks.com/cumulus-vx/download/" text="VirtualBox OVA image">}} and import all the VMs that you want to run in GNS3 into VirtualBox.
3. Download and install {{<exlink url="https://www.gns3.com/software" text="GNS3">}}.
4. Start GNS3.
5. Select **GNS3** \> **Preferences**. From the left pane of the Preferences dialog, select **VirtualBox**.
6. In the **Path to VBoxManage** field, enter the location where VBoxManage is installed. For example: `/usr/bin/VBoxManage`.
7. From the left pane, select **VirtualBox VMs**, then click **New**. The **VM list** shows the VirtualBox VMs you set up earlier.

    {{< img src = "/images/cumulus-vx/VX_GNS3_new_VBox_VM.png" >}}

8. From the **VM list**, select the VM that you want to run in GNS3, then click **Finish**. The VM you selected appears in the center pane. Repeat this step for every VM in the topology that you want to run in GNS3. For the example topology above, the VMs are: Cumulus spine01, Cumulus spine02, Cumulus leaf01 and Cumulus leaf02.

    {{< img src = "/images/cumulus-vx/VX_GNS3_VBox_VMs.png" >}}

9. Enable GNS3 to work with the network interfaces of the VirtualBox VMs. Configure the network settings for each VM using the GNS3 interface:

   1. Select a VM in the center pane, then click **Edit**.

   2. In the VirtualBox VM configuration dialog, click the **Network** tab.

      {{< img src = "/images/cumulus-vx/VX_GNS3_VBox_VM_nwconfig.png" >}}

   3. Increase the number of **Adapters** to *4*.
   4. Select the **Type** to be *Paravirtualized Network*.
   5. Select **Allow GNS3 to use any configured VirtualBox adapter**.
   6. Click **OK** to save your settings and close the dialog. GNS3 overwrites the interface names that are configured in VirtualBox; If you want to use the VM in VirtualBox, you might want to consider cloning them first.

10. To connect VMs, select the cable icon from the left pane, then select the VMs to connect directly. To do this, select which network interface you want connected for each VM. e1 in GNS3 corresponds to swp1 in Cumulus VX, e2 to swp2, and so on.

   {{< tabs "TabID01 ">}}

{{< tab "Spine01 ">}}

e1<->e1 Cumulus Leaf01  
e2<->e1 Cumulus Leaf02

{{< /tab >}}

{{< tab "Cumulus Leaf01 ">}}

e1<->e1 Cumulus Spine01  
e3<->e0 PC1 (VPCS)

{{< /tab >}}

{{< tab "Cumulus Leaf02 ">}}

e1<->e2 Cumulus spine01  
e3<->e0 PC2 (VPCS)

{{< /tab >}}

{{< /tabs >}}

   You can also drag and drop virtual PCs (VPCS) and connect them to the Cumulus VX switch. To open a console to a virtual PC, right click on the VPCS icon and select **Console**. In the console, configure the IP address and default gateway for the VPCS (for example: `ip 10.4.1.101/25 10.4.1.1`).

## Test the Network Connections

After you restart the VMs, ping across VMs to test the connections. Run the following commands from leaf01:

   ```
   cumulus@Cumulusleaf01:~$ ping 10.2.1.2

   cumulus@leaf01:~$ ping 10.2.1.3
   ```

## Configure OSPF and FRRouting

ADD SHORTCODE
