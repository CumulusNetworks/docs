---
title: GNS3 and VirtualBox
author: Cumulus Networks
weight: 40
---

This section describes how to install and set up Cumulus VX within GNS3 and VirtualBox to create the two leaf and one spine topology shown below.

{{% vx/intro %}}

These steps were tested with VirtualBox version 6.1.12 and GNS3 version 2.2.11 on macOS version 10.14.6.

## Create VMs and Network Connections

The following procedure creates leaf01, leaf02, and spine01 and the network connections between them. This section assumes a basic level of GN3, VirtualBox, and Linux experience.

### Download the Software

1. Download and install {{<exlink url="https://www.virtualbox.org" text="VirtualBox">}}.
2. Download the {{<exlink url="https://cumulusnetworks.com/cumulus-vx/download/" text="VirtualBox OVA image">}}.
3. Download and install {{<exlink url="https://www.gns3.com/software" text="GNS3">}}.

### Create the VMs in VirtualBox

{{% vx/virtualbox-steps %}}

### Configure GNS3

1. Open the GNS3 application an create a new project.

2. From the **Preferences** menu, select **GNS3**. Then, from the left pane of the Preferences dialog, select **VirtualBox**.
3. In the **Path to VBoxManage** field, enter the location where VBoxManage is installed. For example: `/usr/bin/VBoxManage`.
4. From the left pane, select **VirtualBox VMs**, then click **New**. The **VM list** shows the VirtualBox VMs you set up earlier.

    {{< figure src = "/images/cumulus-vx/VX_GNS3_new_VBox_VM.png" >}}

5. From the **VM list**, select leaf01, then click **Finish**. The VM you selected appears in the center pane. Repeat this step for leaf02 and spine01.

6. Enable GNS3 to work with the network interfaces of the VirtualBox VMs:

   1. In the center pane, select leaf01 then click **Edit**.

   2. In the VirtualBox VM configuration dialog, click the **Network** tab.

      {{< img src="/images/cumulus-vx/VX_GNS3_VBox_VM_nwconfig.png" width="300" >}}

   3. Increase the number of **Adapters** to *4*.
   4. From the **Type** dropdown, select *Paravirtualized Network*.
   5. Select **Allow GNS3 to use any configured VirtualBox adapter**.
   6. Click **OK** to save your settings and close the dialog.
   7. Repeat these steps for leaf02 and spine01, then click **OK** to close the Preferences dialog.

### Create Network Connections

Create the network connections between leaf01, leaf02, and spine01, then start the switches.

From the GNS3 Management Console, drag leaf01, leaf02, and spine01 to the console. Select the cable icon from the left pane, then connect the leafs and spine by selecting the network interfaces. `e1` in GNS3 corresponds to `swp1` in Cumulus VX, `e2` corresponds to `swp2`, and so on.

{{< img src="/images/cumulus-vx/gns3-network-connections.png" width="500" >}}

## Log into the Switches

{{% vx/login %}}

## Basic Switch Configuration

{{% vx/basic-config %}}

## Verify Configuration

{{% vx/verify-config %}}

## Next Steps

{{% vx/next-steps %}}
