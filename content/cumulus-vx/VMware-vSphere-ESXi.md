---
title: VMware vSphere ESXi
author: Cumulus Networks
weight: 30
---
This section describes how to install and set up Cumulus VX in VMWare vSphere to create the two leaf and one spine topology shown below.

{{% vx/intro %}}

These steps were tested with VMware vSphere (ESXi) 6.7.0 and VSphere web client (HTML5) version 6.7.0.30000.

## Create and Configure the VMs

The following procedure creates leaf01, leaf02, and spine01 and the network connections between them. This section assumes you have a basic level of VMWare vSphere experience.

### Download Cumulus VX

Download the {{<exlink url="https://cumulusnetworks.com/products/cumulus-vx/download/" text="OVA disk image for VMware">}}.

### Create the VMs

1. From the vSphere web client, create a new folder under VMs and Templates. Select the folder then click **Deploy OVF Template** from the **Actions** menu.
2. Select the Cumulus VX OVA image you downloaded, then click **Next**.
3. In the **Virtual machine name** field, enter `leaf01`, then click **Next**.

   {{< img src="/images/cumulus-vx/vsphere-add-name.png" width="300" >}}

4. Select a compute source (ESXi host), then click **Next**.

5. The Cumulus VX image is preconfigured, so no more setup options are required. Click **Next** until you see the `Ready to Complete` dialog, then click **Finish**.

   The Cumulus VX OVA image is imported and deployed as a VM. After the deployment process is complete, the VM appears in the list of VMs in the left pane.

6. Repeat the previous steps to create two additional VMs: `leaf02` and `spine01`.

### Create Network Connections

1. Create four virtual machine port groups:

   1. Under **Hosts and clusters**, select the ESXi host, then select **Add Networking** from the **Actions** menu.

   2. Select **Virtual Machine Port Group for a Standard Switch**, then click **Next**.

      {{< img src="/images/cumulus-vx/vsphere-add-network.png" width="500" >}}

   3. Select **New standard switch**, then click **Next**.

   4. In the **Create a Standard Switch** dialog, click **Next**, then click **OK** when the Physical Network Adapters warning displays.

   5. In the **Network Label** field, enter `intnet-1`, click **Next**, then click **Finish**.

   6. Repeat the previous steps to create **three** additional port groups: `intnet-2`, `intnet-3`, and `intnet-4`.

2. Configure the virtual hardware for each VM (leaf01, leaf02, and spine01):

   1. Under **VMs and Templates**, select the VM in the left pane, then click the **Edit Settings** icon.

   2. Under **Virtual Hardware**, configure the network adapters as shown below, then click **OK**.

      {{< figure src = "/images/cumulus-vx/VX-Connections.png" >}}

      {{< tabs "TabID55 ">}}

{{< tab "leaf01 ">}}

{{< img src="/images/cumulus-vx/vsphere-network-leaf01.png" width="600" >}}

{{< /tab >}}

{{< tab "leaf02 ">}}

{{< img src="/images/cumulus-vx/vsphere-network-leaf02.png" width="600" >}}

{{< /tab >}}

{{< tab "spine01 ">}}

{{< img src="/images/cumulus-vx/vsphere-network-spine01.png" width="600" >}}

{{< /tab >}}

{{< /tabs >}}

3. Start the VMS and launch the Console for each VM.

## Log into the Switches

{{% vx/login %}}

## Basic Switch Configuration

{{% vx/basic-config %}}

## Verify Configuration

{{% vx/verify-config-vsphere %}}

## Next Steps

{{% vx/next-steps %}}
