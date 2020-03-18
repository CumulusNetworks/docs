---
title: Setup Your VMware Virtual Machine
author: Cumulus Networks
weight:
aliases:
 - /display/NETQ/Install+NetQ
 - /pages/viewpage.action?pageId=12320951
pageID: 12320951
toc: 5

onprem: true
cluster: false
vm: true
kvm: true
---

Follow these steps to setup and configure your VM:

1. Verify that your system meets the VM requirements.

    {{<netq-install/vm-reqs>}}

2. Confirm that the needed ports are open for communications.

    {{<netq-install/port-reqs>}}

3. Download the NetQ Platform image.

    {{<netq-install/platform-image>}}

4. Setup and configure your VM.

    {{<netq-install/vm-setup hypervisor="kvm">}}

5. Verify the platform is ready for installation. Fix any errors indicated before installing the NetQ software.

    {{<netq-install/verify-cmd>}}

5. Run the Bootstrap CLI on the platform *for the interface you defined above* (eth0 or eth1 for example). This example uses the eth0 interface.

    ```
    cumulus@<hostname>:~$ netq bootstrap master interface eth0 tarball /mnt/installables/netq-bootstrap-2.4.1.tgz
    ```

    Allow about five minutes for this to complete,  and only then continue to the next step.

    {{%notice tip%}}
If this step fails for any reason, you can run `netq bootstrap reset` and then try again.
    {{%/notice%}}

You are now ready to install the Cumulus NetQ software.  Refer to {{<link title="Install NetQ Using the Admin UI">}} (recommended) or {{<link title="Install NetQ Using the CLI">}}.
