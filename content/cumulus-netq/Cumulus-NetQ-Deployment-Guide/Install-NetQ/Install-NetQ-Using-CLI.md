---
title: Install NetQ Using the CLI
author: Cumulus Networks
weight: 110
aliases:
 - /display/NETQ/Install+NetQ
 - /pages/viewpage.action?pageId=12320951
pageID: 12320951
product: Cumulus NetQ
version: 2.4
imgData: cumulus-netq
siteSlug: cumulus-netq
toc: 4
---
After you have validated the prerequisites and performed the preparation steps, you can now install the NetQ software using the CLI.

{{%notice info%}}
You must perform the preparation steps before installing the NetQ software. Go to [Prepare for NetQ On-premises Installation](../Prepare-NetQ-Onprem/) or [Prepare for NetQ Cloud Installation](../Prepare-NetQ-Cloud/) if you have not yet completed these preparation steps.
{{%/notice%}}

To install NetQ:

1. Log in to your NetQ platform server, NetQ Appliance, NetQ Cloud Appliance or the master node of your cluster.

2. Install the software.

    - **For On-premises Solution, Single Server**
        
        Run the following command on your NetQ platform server or NetQ Appliance:

        ```
        cumulus@<hostname>:~$ netq install standalone full interface eth0 bundle /mnt/installables/NetQ-2.4.0.tgz
        ```
        
    - **For On-premises Solution, Server Cluster**
    
        Run the following commands on your *master* node, using the IP addresses of your worker nodes:

        ```        
        cumulus@<hostname>:~$ netq install cluster full interface eth0 bundle /mnt/installables/NetQ-2.4.0.tgz workers <worker-1-ip> <worker-2-ip>
        ```
        
    - **For Cloud Solution, Single Server**
    
        Run the following command on your NetQ Cloud Appliance with the `config-key` sent by Cumulus Networks in an email titled "A new site has been added to your Cumulus NetQ account."

        ```
        cumulus@<hostname>:~$ netq install opta standalone full interface eth0 bundle /mnt/installables/NetQ-2.4.0-opta.tgz config-key <your-config-key-from-email>
        ```
    - **For Cloud Solution, Server Cluster**
    
        Run the following commands on your *master* NetQ Cloud Appliance with the `config-key` sent by Cumulus Networks in an email titled "A new site has been added to your Cumulus NetQ account."

        ```
        cumulus@<hostname>:~$ netq install opta cluster full interface eth0 bundle /mnt/installables/NetQ-2.4.0-opta.tgz config-key <your-config-key-from-email> workers <worker-1-ip> <worker-2-ip>
        ```
