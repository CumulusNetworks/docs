---
title: Install NetQ Using the CLI
author: Cumulus Networks
weight: 411
aliases:
 - /display/NETQ/Install+NetQ
 - /pages/viewpage.action?pageId=12320951
pageID: 12320951
product: Cumulus NetQ
version: 2.4
imgData: cumulus-netq
siteSlug: cumulus-netq
---
After you have validated the prerequisites and performed the preparation steps, you can now install the NetQ software using the CLI.

To install NetQ:

1. Log in to your NetQ platform server, NetQ Appliance, NetQ Cloud Appliance or the master node of your cluster.

2. Install the software using your configuration key.

    - **For standalone server**, run the following command on your NetQ platform server or NetQ Appliance:
        ```
        cumulus@<hostname>:~$ netq install standalone full interface eth0 bundle /mnt/installables/NetQ-2.4.0.tgz
        ```
    - **For cloud deployments**, run the following command on your NetQ Cloud Appliance with the config-key sent by Cumulus Networks in an email titled "A new site has been added to your Cumulus NetQ account".

        ```
        cumulus@<hostname>:~$ netq install standalone full interface eth0 bundle /mnt/installables/NetQ-2.4.0.tgz config-key <your-config-key-from-email>
        ```

    - **For a server cluster in on-premises**, run the following command on your master node, using the IP addresses of your worker nodes: 
        ```
        cumulus@<hostname>:~$ netq install cluster full interface eth0 bundle /mnt/installables/NetQ-2.4.0.tgz workers <worker-1-ip> <worker-2-ip>
        ```
    
    - **For a server cluster in cloud deployments**, run the following command on your master node, using the IP addresses of your worker nodes: Config-key is sent by Cumulus Networks in an email titled "A new site has been added to your Cumulus NetQ account".

        ```
        cumulus@<hostname>:~$ netq install cluster full interface eth0 bundle /mnt/installables/NetQ-2.4.0.tgz config-key <your-config-key-from-email> workers <worker-1-ip> <worker-2-ip>
        ```
