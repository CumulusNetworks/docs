---
title: Set Up Your VMware Virtual Machine for an On-premises HA Server Cluster
author: NVIDIA
weight: 223
toc: 5
bookhidden: true
---
First configure the VM on the master node, and then configure the VM on each worker node.

Follow these steps to set up and configure your VM cluster for an on-premises deployment:

1. Verify that each node in your cluster---the master node and two worker nodes---meets the VM requirements.

    {{<netq-install/vm-reqs deployment="onprem" hypervisor="vmware" version="4.2.0">}}

2. Confirm that the required ports are open for communications.

    {{<netq-install/port-reqs server="cluster">}}

3. Download the NetQ Platform image.

    {{<netq-install/vmw-platform-image deployment="onprem" version="4.10">}}

4. Set up and configure your VM.

    {{<netq-install/vm-setup hypervisor="vmware" deployment="onprem" version="4.10">}}

5. Log in to the VM and change the password.

    {{<netq-install/change-pswd>}}

6. Verify the master node is ready for installation. Fix any errors indicated before installing the NetQ software.

    {{<netq-install/verify-cmd deployment="onprem">}}

7. Change the hostname for the VM from the default value.

    {{<netq-install/set-hostname>}}

8. Verify that your first worker node meets the VM requirements, as described in step 1.

9. Confirm that the required ports are open for communications, as described in step 2.

10. Open your hypervisor and set up the VM in the same manner as the master node.

    {{<notice note>}}
Make a note of the private IP address you assign to the worker node. You need it for later installation steps.
    {{</notice>}}

11. Verify the worker node is ready for installation. Fix any errors indicated before installing the NetQ software.

    {{<netq-install/verify-cmd deployment="cloud">}}

12. Repeat steps 8 through 11 for each additional worker node in your cluster.

13. Install and activate the NetQ software using the CLI:

{{<netq-install/install-with-cli version="4.10" deployment="onprem-cluster-ha">}}

After NetQ is installed, you can {{<link title="Access the NetQ UI" text="log in to NetQ">}} from your browser.