---
title: VMware vSphere ESXi
author: NVIDIA
weight: 40
product: Cumulus VX
version: '5.x'
---
This section describes how to install and set up Cumulus VX in VMWare vSphere to create the two leaf and one spine topology shown below.

{{% vx/intro %}}

<!-- vale off -->
These steps were tested with Cumulus VX 4.2, VMware vSphere (ESXi) 6.7.0, and VSphere web client (HTML5) version 6.7.0.30000.
<!-- vale on -->

## Create and Configure the VMs

The following procedure creates leaf01, leaf02, and spine01 and the network connections between them. This section assumes you have VMWare vSphere experience.

### Download Cumulus VX

Download the {{<exlink url="https://www.nvidia.com/en-us/networking/ethernet-switching/cumulus-vx/" text="OVA disk image for VMware">}}.

### Create the VMs

Follow these steps for each VM (leaf01, leaf02, and spine01):

1. From the vSphere web client, create a new folder under VMs and Templates.
2. Select the folder then click **Deploy OVF Template** from the **Actions** menu.
3. Select the Cumulus VX OVA image you downloaded, then click **Next**.
4. In the **Virtual machine name** field, enter `leaf01`, then click **Next**.

   {{<img src="/images/cumulus-vx/vsphere-add-name.png" width="400">}}

5. Select a compute source (ESXi host), then click **Next**.
6. The Cumulus VX image comes preconfigured, so there is no need for further setup. Click **Next** until you see the `Ready to Complete` dialog, then click **Finish**.

   You import and deploy the Cumulus VX OVA image as a VM. After the deployment process is complete, the VM appears in the list of VMs in the left pane.

   {{% notice note %}}
   The Cumulus VX OVA image defines the CPU, memory, and disk requirements. Cumulus VX requires at least 768MB of RAM and 6GB of disk space.

   CumulusVX versions 4.3 and later requires 2 vCPUs.

   {{% /notice %}}

7. Repeat the previous steps to create two additional VMs: `leaf02` and `spine01`.

### Create Network Connections

Create the network connections between leaf01, leaf02, and spine01.

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

      {{< img src="/images/cumulus-vx/vsphere-edit-icon.png" width="500" >}}

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

      {{% notice note %}}
Adapter 1 is a shared management interface. The examples above show it as disabled for simplicity.
{{% /notice %}}

3. Start the VMs and launch the Console for each VM.

## Log into the Switches

{{% vx/login %}}

## Basic Switch Configuration

{{% vx/basic-config %}}

## Verify Configuration

{{% vx/verify-config %}}

## Next Steps

{{% vx/next-steps %}}
