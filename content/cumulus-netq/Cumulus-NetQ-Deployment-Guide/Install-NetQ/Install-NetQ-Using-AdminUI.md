---
title: Install NetQ Using the Admin UI
author: Cumulus Networks
weight: 410
aliases:
 - /display/NETQ/Install+NetQ
 - /pages/viewpage.action?pageId=12320951
pageID: 12320951
product: Cumulus NetQ
version: 2.4
imgData: cumulus-netq
siteSlug: cumulus-netq
---
After you have validated the prerequisites and performed the preparation steps, you can now install the NetQ software using the Admin UI.

To install NetQ:

1. Log in to your NetQ platform server, NetQ Appliance, NetQ Cloud Appliance or the master node of your cluster.

    In your browser address field, enter **https://**<*hostname-or-ipaddr*>**:8443**

    This opens the Admin UI.

    {{<figure src="/images/netq/adminui-main-page-240.png" width="700">}}

2. Step through the UI:

    1. Select your deployment type.

        The first step to install Cumulus NetQ is to choose which type of deployment model you want to use. If you are performing an upgrade, then select the deployment type you already have set up. Both options provide secure access to data and features useful for monitoring and troubleshooting your network.

        Select the on-premises deployment model if you want to host all required hardware and software at your location(s), and you have the in-house skill set to install, configure, and maintain it—including performing data backups, acquiring and maintaining hardware and software, and integration and license management. This model is commonly chosen when you do not want to provide any access to the Internet or you have a strong desire for control of the entire network.

        Select the cloud deployment model if you want to host only a small server on your premises and leave the details up to Cumulus Networks. In this deployment, the server connects to the NetQ Cloud service over selected ports. The NetQ application is hosted and data storage is provided in the cloud. Cumulus handles the backups and maintenance of the application and storage.

        {{<figure src="/images/netq/adminui-deploy-type-240.png" width="700">}}

    2. Select your install method.
    
        Choose between restoring data from a previous version of NetQ or performing a fresh installation.
        
        \> Restore NetQ data (on-premises only)

        If you have created a backup of your NetQ data in the preparation steps, you can restore your data when you reach this screen.

        {{%notice info%}}
If you are moving from a standalone to a server cluster arrangement, you can only restore your data one time. After the data has been converted to the cluster schema, it cannot be returned to the standalone server format.
        {{%/notice%}}

         {{<figure src="/images/netq/adminui-restore-db-240.png" width="700">}}

        \> Fresh Install

        See step 4.

    3. Select your server arrangement.

        Select whether you want to deploy your infrastructure as a single stand-alone server or as a cluster of servers. Choosing the Stand-alone configuration is simpler, but for on-premises deployments you need to anticipate the size and capabilities of this server to support your final deployment. Choosing the multiple server configuration is more complex, but it offers more scalability, high availability, and failover capabilities depending on the configuration. Both options support the installation of NetQ as a VM or disk image.

        Select the standalone single-server arrangements for smaller, simpler deployments. Be sure to consider the capabilities and resources needed on this server to support the size of your final deployment.

        Select the three-server cluster arrangement to obtain scalability, high availability, and/or failover for your network. With this release, you must have one master and two worker nodes.

        {{<figure src="/images/netq/adminui-server-arrange-240.png" width="700" caption="Select arrangement">}}

        {{<figure src="/images/netq/adminui-cluster-config-240.png" width="700" caption="Add worker nodes to a server cluster">}}
 
    4. Install NetQ software.
    
        After the hardware has been configured, you can install the NetQ software using the installation files (`NetQ-2.4.0-tgz` for on-premises deployments or `NetQ-2.4.0-opta.tgz` for cloud deployments)  that you downloaded during the preparation steps.

        {{<figure src="/images/netq/adminui-install-netq-240.png" width="700">}}

    5. Activate NetQ.

        This final step activates the software and enables you to view the health of your NetQ system. For cloud deployments, you must enter your configuration key.

        {{<figure src="/images/netq/adminui-activate-netq-onprem-240.png" width="700" caption="On-premises activation">}}

        {{<figure src="/images/netq/adminui-activate-netq-cloud-240.png" width="700" caption="Cloud activation">}}

    6. View the system health.

        When the installation and activation is complete, the NetQ System Health dashboard is visible for tracking the status of key components in the system. Standalone server deployments display two cards, one for the server, and one for Kubernetes pods. Server cluster deployments display additional cards, including one each for the Cassandra database, Kafka, and Zookeeper services.

        {{<figure src="/images/netq/adminui-health-db-cloud-240.png" width="700">}}
