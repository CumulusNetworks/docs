---
title: Set Up Your VMware Virtual Machine for a Single On-premises Server
author: NVIDIA
weight: 221
toc: 5
bookhidden: true
---
Follow these steps to set up and configure your VM on a single server in an on-premises deployment:

1. Verify that your system meets the VM requirements.

    {{<netq-install/vm-reqs deployment="onprem" hypervisor="vmware" version="4.2.0">}}

2. Confirm that the required ports are open for communications.

    {{<netq-install/port-reqs server="single">}}

3. Download the NetQ Platform image.

    {{<netq-install/vmw-platform-image deployment="onprem" version="4.10">}}

4. Set up and configure your VM.

    {{<netq-install/vm-setup hypervisor="vmware" deployment="onprem" version="4.10">}}

5. Log in to the VM and change the password.

    {{<netq-install/change-pswd>}}

6. Verify the platform is ready for installation. Fix any errors indicated before installing the NetQ software.

    {{<netq-install/verify-cmd deployment="onprem">}}

7. Change the hostname for the VM from the default value.

    {{<netq-install/set-hostname>}}

8. Install and activate the NetQ software using the CLI:

    {{<netq-install/install-with-cli version="4.10" deployment="onprem-single">}}

After NetQ is installed, you can {{<link title="Access the NetQ UI" text="log in to NetQ">}} from your browser.