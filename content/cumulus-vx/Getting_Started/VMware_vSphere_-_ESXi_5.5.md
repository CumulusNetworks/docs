---
title: VMware vSphere - ESXi 5.5
author: Cumulus Networks
weight: 37
aliases:
 - /display/VX/VMware+vSphere+-+ESXi+5.5
 - /pages/viewpage.action?pageId=5126689
pageID: 5126689
product: Cumulus VX
version: 3.4.0
imgData: cumulus-vx
siteSlug: cumulus-vx
---
The following sections describe how to import and set up a
two-leaf/two-spine Cumulus VX topology with VMware vSphere.

{{%notice note%}}

These sections assume a basic level of VMware vSphere experience. For
detailed instructions, refer to the [VMware vSphere
documentation](https://pubs.vmware.com/vsphere-55/index.jsp).

{{%/notice%}}

## <span>Create a Cumulus VX VM with VMware vSphere - ESXi 5.5</span>

{{%notice note%}}

This section assumes that you have downloaded the Cumulus VX disk image
for VMware hypervisors and that the VMware vSphere is installed. For
more download locations and steps, refer to the [Getting
Started](/cumulus-vx/Getting_Started/) page.

{{%/notice%}}

{{%notice note%}}

This configuration was tested using vSphere ESXi 5.5 and a Windows
vSphere client; however, the VM is configured to support ESXi 4.0 and
higher.

{{%/notice%}}

1.  Download the VMware OVFtools utility from the [VMware downloads
    page](https://my.vmware.com/web/vmware/details?productId=352&downloadGroup=OVFTOOL350)
    and install it on the client. You can view installation instructions
    on the VMware website.

2.  Connect the vSphere client to the vSphere ESXi server using the IP
    address and user credentials of the ESXi server.

3.  In the vSphere client window, click **File \> Deploy OVF Template**
    to open the import window.

4.  Select **Browse**, locate the Cumulus VX OVA file, then click
    **Next** to continue.

5.  Review the template details, then click **Next**.

6.  In the text box, edit the name of the VM to `CumulusVX-leaf1`, then
    click **Next**.
    
    {{% imgOld 0 %}}

7.  As the Cumulus VX image is preconfigured, no more set up options are
    required. Click **Next** through the next few windows until you see
    the `Ready to Complete` window:
    
    {{% imgOld 1 %}}

8.  If you want the VM to start immediately after the import process is
    complete, select the `Power on after deployment` option, then click
    **Finish**.

The Cumulus VX OVA image is imported into vSphere ESXi and deployed as a
VM. The length of the import process depends on the system
configuration. You can view the progress in the `Recent Tasks` pane at
the bottom of the client window. After the deployment process is
complete, the newly created VM appears in the list of VMs in the left
pane.

{{% imgOld 2 %}}

## <span>Next Steps</span>

{{%notice note%}}

This section assumes that you are configuring a two-leaf/two-spine
network topology, that you have completed the steps in [Create a Cumulus
VX VM with VMware vSphere - ESXi
5.5](#src-5126689_VMwarevSphere-ESXi5.5-CreateaCumulusVXVirtualMachinewithVMwarevSphere-ESXi5.5)
above, and that you now have a VM called `CumulusVX-leaf1`.

{{%/notice%}}

1.  The two-leaf/two-spine network topology requires you to create four
    VMs. Repeat the steps outlined in [Create a Cumulus VX VM with
    VMware vSphere - ESXi
    5.5](#src-5126689_VMwarevSphere-ESXi5.5-CreateaCumulusVXVirtualMachinewithVMwarevSphere-ESXi5.5)
    to create three additional VMs, replacing the name `CumulusVX-leaf1`
    with:
    
      - `CumulusVX-leaf2`
    
      - `CumulusVX-spine1`
    
      - `CumulusVX-spine2`

2.  After you have created all four VMs, follow the steps detailed in
    [Create a Two-Leaf, Two-Spine
    Topology](/cumulus-vx/Create_a_Two-Leaf_Two-Spine_Topology) to
    configure the network interfaces and routing.
