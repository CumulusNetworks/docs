---
title: Set Up Your VMware Virtual Machine for a Single On-premises Server
author: NVIDIA
weight: 221
toc: 5
bookhidden: true
---
Follow these steps to setup and configure your VM on a single server in an on-premises deployment:

1. Verify that your system meets the VM requirements.

    {{<netq-install/vm-reqs deployment="onprem" hypervisor="vmware">}}

2. Confirm that the needed ports are open for communications.

    {{<netq-install/port-reqs server="single">}}

3. Download the NetQ Platform image.

    {{<netq-install/vmw-platform-image deployment="onprem" version="4.1">}}

4. Setup and configure your VM.

    {{<netq-install/vm-setup hypervisor="vmware" deployment="onprem" version="4.0">}}

5. Log in to the VM and change the password.

    {{<netq-install/change-pswd>}}

6. Verify the platform is ready for installation. Fix any errors indicated before installing the NetQ software.

    {{<netq-install/verify-cmd deployment="onprem">}}

7. Change the hostname for the VM from the default value.

    {{<netq-install/set-hostname>}}

8. Run the Bootstrap CLI. Be sure to replace the *eth0* interface used in this example with the interface on the server used to listen for NetQ Agents.

    {{<netq-install/bootstrap version="4.1" server="single" platform="vm" deployment="onprem">}}

9. Consider the following for container environments, and make adjustments as needed.

    {{<netq-install/container version="4.1">}}

The final step is to install and activate the NetQ software. You can do this using the Admin UI or the CLI.

Click the installation and activation method you want to use to complete installation:

- {{<link title="Install NetQ Using the Admin UI" text="Use the Admin UI">}} (recommended)
- {{<link title="Install NetQ Using the CLI" text="Use the CLI">}}
