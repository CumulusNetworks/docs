---
title: Deploy NetQ as an On-premises Installation
author: Cumulus Networks
weight: 
aliases:
 - /display/NETQ/Install+NetQ
 - /pages/viewpage.action?pageId=12320951
pageID: 12320951
toc: 5
bookhidden: false
---
## Prepare for Installation

Perform the following steps to prepare your system for installation of the NetQ software.

1. Verify that your system meets the {{<link url="onprem-vm-reqs" text="VM requirements">}}.

2. Confirm that the needed {{<link url="sglsvr-open-ports" text="ports">}} are open for communications.

3. {{<link url="X" text="Download the NetQ Platform image">}}.

4. {{<link url="x" text="Configure Your KVM VM">}}

5. Verify the platform is ready for installation. Fix any errors indicated before installing the NetQ software.

    ```
    cumulus@<hostname>:~$ sudo opta-check
    ```
    
5. Run the Bootstrap CLI on the platform *for the interface you defined above* (eth0 or eth1 for example). This example uses the eth0 interface.

    ```
    cumulus@<hostname>:~$ netq bootstrap master interface eth0 tarball /mnt/installables/netq-bootstrap-2.4.1.tgz
    ```

    Allow about five minutes for this to complete,  and only then continue to the next step.

    {{%notice tip%}}
If this step fails for any reason, you can run `netq bootstrap reset` and then try again.
    {{%/notice%}}

{{<link url="x" text="x">}}