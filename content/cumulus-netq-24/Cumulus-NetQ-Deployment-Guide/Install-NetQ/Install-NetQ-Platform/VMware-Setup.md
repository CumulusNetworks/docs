---
title: Set Up Your VMware Virtual Machine
author: Cumulus Networks
weight:
aliases:
 - /display/NETQ/Install+NetQ
 - /pages/viewpage.action?pageId=12320951
pageID: 12320951
toc: 5
bookhidden: true
---

Follow these steps to setup and configure your VM:

1. Verify that your system meets the VM requirements.

    {{<netq-install/vm-reqs deployment="onprem">}}

2. Confirm that the needed ports are open for communications.

    {{<netq-install/port-reqs server="single">}}

3. Download the NetQ Platform image.

    {{<netq-install/vmw-platform-image deployment="onprem">}}

4. Setup and configure your VM.

    {{<netq-install/vm-setup hypervisor="vmware">}}

5. Verify the platform is ready for installation. Fix any errors indicated before installing the NetQ software.

    {{<netq-install/verify-cmd deployment="onprem">}}

5. Run the Bootstrap CLI, specifying the interface on the platform *based on what you defined in your VM configuration*. This example uses the *eth0* interface.

    ```
    cumulus@<hostname>:~$ netq bootstrap master interface eth0 tarball /mnt/installables/netq-bootstrap-2.4.1.tgz
    ```

    Allow about five minutes for this to complete,  and only then continue to the next step.

    {{%notice tip%}}
If this step fails for any reason, you can run `netq bootstrap reset` and then try again.
    {{%/notice%}}

The final step is to install and activate the Cumulus NetQ software.  You can do this using the Admin UI or the CLI.

Click the installation and activation method to want to use to continue complete installation:

- {{<link title="Install NetQ Using the Admin UI" text="Use the Admin UI">}} (recommended)
- {{<link title="Install NetQ Using the CLI" text="Use the CLI">}}
