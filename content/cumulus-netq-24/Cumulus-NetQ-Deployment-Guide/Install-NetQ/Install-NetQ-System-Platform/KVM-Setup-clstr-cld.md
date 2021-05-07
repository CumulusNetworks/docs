---
title: Set Up Your KVM Virtual Machine for a Cloud Server Cluster
author: Cumulus Networks
weight: 75
toc: 5
bookhidden: true
---
First configure the VM on the master node, and then configure the VM on each worker node.

Follow these steps to setup and configure your VM on a cluster of servers in a cloud deployment:

1. Verify that your master node meets the VM requirements.

    {{<netq-install/vm-reqs deployment="cloud" hypervisor="kvm">}}

2. Confirm that the needed ports are open for communications.

    {{<netq-install/port-reqs server="cluster">}}

3. Download the NetQ Platform image.

    {{<netq-install/kvm-platform-image deployment="cloud" version="2.4.1">}}

4. Setup and configure your VM.

    {{<netq-install/vm-setup hypervisor="kvm" deployment="cloud" version="2.4.1">}}

5. Verify the master node is ready for installation. Fix any errors indicated before installing the NetQ software.

    {{<netq-install/verify-cmd deployment="cloud">}}

6. Run the Bootstrap CLI. Be sure to replace the *eth0* interface used in this example with the interface on the server used to listen for NetQ Agents.

    {{<netq-install/bootstrap server="single" version="2.4.1" platform="vm" deployment="cloud">}}

7. Verify that your first worker node meets the VM requirements, as described in Step 1.

8. Confirm that the needed ports are open for communications, as described in Step 2.

9. Open your hypervisor and setup the VM in the same manner as for the master node.

    {{<notice note>}}
Make a note of the private IP address you assign to the worker node. It is needed for later installation steps.
    {{</notice>}}

10. Verify the worker node is ready for installation. Fix any errors indicated before installing the NetQ software.

    {{<netq-install/verify-cmd deployment="cloud">}}

11. Run the Bootstrap CLI on the worker node.

    {{<netq-install/bootstrap server="cluster" version="2.4.1" platform="vm" deployment="cloud">}}

12. Repeat Steps 7 through 11 for each additional worker node you want in your cluster.

The final step is to install and activate the Cumulus NetQ software. You can do this using the Admin UI or the CLI.

Click the installation and activation method you want to use to complete installation:

- {{<link title="Install NetQ Using the Admin UI" text="Use the Admin UI">}} (recommended)
- {{<link title="Install NetQ Using the CLI" text="Use the CLI">}}
