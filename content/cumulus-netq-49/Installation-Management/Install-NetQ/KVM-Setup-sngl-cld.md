---
title: Set Up Your KVM Virtual Machine for a Single Cloud Server
author: NVIDIA
weight: 226
toc: 5
bookhidden: true
---
Follow these steps to set up and configure your VM on a single server in a cloud deployment:

1. Verify that your system meets the VM requirements.

    {{<netq-install/vm-reqs deployment="cloud" hypervisor="kvm">}}

2. Confirm that the required ports are open for communications. 

    {{<netq-install/port-reqs deployment="cloud" server="single">}}

3. Download the NetQ image.

    {{<netq-install/kvm-platform-image deployment="cloud" version="4.9">}}

4. Set up and configure your VM.

    {{<netq-install/vm-setup hypervisor="kvm" deployment="cloud" version="4.9">}}

5. Log in to the VM and change the password.

    {{<netq-install/change-pswd>}}

6. Verify the platform is ready for installation. Fix any errors indicated before installing the NetQ software.

    {{<netq-install/verify-cmd deployment="cloud">}}

7. Change the hostname for the VM from the default value.

    {{<netq-install/set-hostname>}}

8. Install and activate the NetQ software using the CLI:

{{<netq-install/install-with-cli version="4.9" deployment="cloud-single">}}

After NetQ is installed, you can {{<link title="Access the NetQ UI" text="log in to NetQ">}} from your browser.