---
title: Install NetQ Using the Admin UI
author: Cumulus Networks
weight: 95
toc: 5
---
You can now install the NetQ software using the Admin UI.

{{<notice info>}}
This is the final set of steps for installing NetQ. If you have not already performed the installation preparation steps, go to {{<link title="Install NetQ System Platform">}} before continuing here.
{{</notice>}}

To install NetQ:

1. Log in to your NetQ On-premises Appliance, NetQ Cloud Appliance, the master node of your cluster, or VM.

    In your browser address field, enter *https://\<hostname-or-ipaddr\>:8443*.

2. Enter your username. Default is *admin*.

3. Enter your password. Default is *admin*.

4. Click **Sign In**.

    A Welcome screen is presented on first login and on subsequent logins the NetQ Health dashboard is displayed.

    {{<figure src="/images/netq/adminui-main-page-241.png" width="700">}}

5. Step through the UI.

    Having made your installation choices during the preparation steps, you can quickly select the correct path through the UI.

    1. Select your deployment type.

        Choose which type of deployment model you want to use. Both options provide secure access to data and features useful for monitoring and troubleshooting your network.

        {{<figure src="/images/netq/adminui-deploy-type-240.png" width="700">}}

    2. Select your install method.

        Choose between restoring data from a previous version of NetQ or performing a fresh installation.

        **Fresh Install**: Continue with Step c.

        {{<figure src="/images/netq/adminui-install-netq-240.png" width="700">}}

        **Maintain Existing Data** (on-premises only): If you have created a backup of your NetQ data, choose this option.

        {{<notice info>}}
If you are moving from a standalone to a server cluster arrangement, you can only restore your data one time. After the data has been converted to the cluster schema, it cannot be returned to the single server format.
        {{</notice>}}

        {{<figure src="/images/netq/adminui-restore-db-240.png" width="700">}}

    3. Select your server arrangement.

        Select whether you want to deploy your infrastructure as a single stand-alone server or as a cluster of servers. One master and two worker nodes are supported for the cluster deployment.

        {{<figure src="/images/netq/adminui-server-arrange-240.png" width="700" caption="Select arrangement">}}

        If you select a server cluster, use the private IP addresses that you used when setting up the worker nodes to add those nodes.

        {{<figure src="/images/netq/adminui-cluster-config-240.png" width="700" caption="Add worker nodes to a server cluster">}}

    4. Install NetQ software.

        You install the NetQ software using the installation files (`NetQ-3.1.0-tgz` for on-premises deployments or `NetQ-3.1.0-opta.tgz` for cloud deployments)  that you downloaded and stored previously.

        Enter the appropriate filename in the field provided.

    5. Activate NetQ.

        This final step activates the software and enables you to view the health of your NetQ system. For cloud deployments, you must enter your configuration key.

        {{<figure src="/images/netq/adminui-activate-netq-onprem-240.png" width="700" caption="On-premises activation">}}

        {{<figure src="/images/netq/adminui-activate-netq-cloud-240.png" width="700" caption="Cloud activation">}}

    6. View the system health.

        When the installation and activation is complete, the NetQ System Health dashboard is visible for tracking the status of key components in the system. Single server deployments display two cards, one for the server, and one for Kubernetes pods. Server cluster deployments display additional cards, including one each for the Cassandra database, Kafka, and Zookeeper services.

        {{<figure src="/images/netq/adminui-health-db-onprem-300.png" width="700" caption="On-premises deployment">}}
