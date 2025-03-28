---
title: Set Up Your KVM Virtual Machine for a Single Remote Server
author: NVIDIA
weight: 226
toc: 5
bookhidden: true
---
Follow these steps to setup and configure your VM on a single server in a cloud deployment:

1. Verify that your system meets the VM requirements.

    {{<netq-install/vm-reqs deployment="cloud" hypervisor="kvm">}}

2. Confirm that the needed ports are open for communications.

    {{<netq-install/port-reqs server="single">}}

3. Download the NetQ images.

    {{<netq-install/kvm-platform-image deployment="cloud" version="4.2">}}

4. Setup and configure your VM.

    {{<netq-install/vm-setup hypervisor="kvm" deployment="cloud" version="4.2">}}

5. Log in to the VM and change the password.

    {{<netq-install/change-pswd>}}

6. Verify the platform is ready for installation. Fix any errors indicated before installing the NetQ software.

    {{<netq-install/verify-cmd deployment="cloud">}}

7. Change the hostname for the VM from the default value.

    {{<netq-install/set-hostname>}}

The final step is to install and activate the NetQ software using the CLI:

- {{<link title="Install NetQ Using the CLI" text="Use the CLI">}}
