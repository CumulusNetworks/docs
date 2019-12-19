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

    - **For standalone server in on-premises or cloud deployments**, run the following command on your NetQ platform server or NetQ Appliance:

        ```
        cumulus@<hostname>:~$ netq install standalone full interface eth0 bundle /mnt/installables/NetQ-2.4.0.tgz config-key EhVuZXasJ6HBvaW50LWdhdGV3YXkYsagD
        ```

    - **For a server cluster in on-premises or cloud deployments**, run the following command on your master node, using the IP addresses of your worker nodes:

        ```
        cumulus@<hostname>:~$ netq install cluster full interface eth0 bundle /mnt/installables/NetQ-2.4.0.tgz config-key Rh8e4p7xLWVuZHBvaW50LWdhdGV3YXkYsagD workers <worker-1-ip> <worker-2-ip>
        ```
