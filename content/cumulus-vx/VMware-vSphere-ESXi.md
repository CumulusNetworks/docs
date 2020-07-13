---
title: VMware vSphere ESXi
author: Cumulus Networks
weight: 20
toc: 2
---

To use Cumulus VX with VMWare vSphere, you need to perform the following configuration:

- Create the VMs
- Create connections between the VMs
- Test the connections
- Configure OSPF and FRRouting

## Create VMs with VMWare vSphere

The following procedure describes how to create a VM in VMWare vSphere for each switch in the example topology (Leaf01, Leaf02, and Spine01). This section assumes a basic level of VMWare vSphere experience.

1. Download and install the VMWare vSphere ESXi hypervisor. Refer to the {{<exlink url="http://www.vmware.com/products/vsphere.html" text="VMWare vSphere documentation">}}.

2. Download the OVA disk image for use with VMware from the {{<exlink url="https://cumulusnetworks.com/products/cumulus-vx/download/" text="Cumulus Networks website">}}.

3. Download the VMware OVFtools utility from the {{<exlink url="https://my.vmware.com/web/vmware/details?productId=352&downloadGroup=OVFTOOL350" text="VMware downloads page">}} and install it on the client. You can view installation instructions on the VMware website.

4. Connect the vSphere client to the vSphere ESXi server using the IP address and user credentials of the ESXi server.

5. In the vSphere client window, click **File > Deploy OVF Template** to open the import window.

6. Select **Browse**, locate the Cumulus VX OVA file, then click **Next** to continue.

7. Review the template details, then click **Next**.

8. In the text box, edit the name of the VM to `Leaf01`, then click **Next**.

    {{< img src = "/images/cumulus-vx/VX_esxi_deploy3_name.png" >}}

9. As the Cumulus VX image is preconfigured, no more set up options are required. Click **Next** through the next few windows until you see the `Ready to Complete` window:

    {{< img src = "/images/cumulus-vx/VX_esxi_deploy4_ready.png" >}}

10. If you want the VM to start immediately after the import process is complete, select the `Power on after deployment` option, then click **Finish**.

   The Cumulus VX OVA image is imported into vSphere ESXi and deployed as a VM. The length of the import process depends on the system configuration. You can view the progress in the `Recent Tasks` pane at the bottom of the client window. After the deployment process is complete, the newly created VM appears in the list of VMs in the left pane.

   {{< img src = "/images/cumulus-vx/VX_esxi_deploy5_deploying.png" >}}

11. Repeat the previous steps to create two additional VMs: `Leaf02` and `Spine01`.

{{%notice note%}}

You might encounter an issue if the wrong storage interface type is selected (SATA or IDE). For example this log message indicates the filesystem cannot be found. Configure ESXi to use the SATA controller.

```
Info: Fetching http://192.168.100.1/onie-installer-cumulus_vx ...
ONIE: Executing installer: http://192.168.100.1/onie-installer-cumulus_vx
Verifying image checksum ...OK.
Preparing image archive ... OK.
Verifying image compatibility ...OK.
Verifying system ram ...OK.
Setting up installer ...Failure: Unable to find storage device for file system with label 'ONIE-BOOT'
Info: Check the output of 'blkid'.
```

{{%/notice%}}

## Create Connections Between VMs

Add section here

## Test the Network Connections

After you restart the VMs, ping across VMs to test the connections.

Run the following commands from leaf01 to ping Leaf02 and Spine01:

```
cumulus@Cumulusleaf01:~$ ping 10.2.1.2

cumulus@leaf01:~$ ping 10.2.1.3
```

## Configure OSPF and FRRouting

   ADD shortcode
