---
title: Install NetQ Using the Admin UI
author: NVIDIA
weight: 240
toc: 5
---
You can install the NetQ software using the Admin UI, which you use for either a default basic installation or an advanced installation.

{{%notice info%}}
This is the final set of steps for installing NetQ. If you have not already performed the installation preparation steps, go to {{<link title="Install the NetQ System">}} before continuing here.
{{%/notice%}}

## Install NetQ

To install NetQ:

1. Log in to your NetQ On-premises Appliance, NetQ Cloud Appliance, the master node of your cluster, or VM.

    In your browser address field, enter *https://\<hostname-or-ipaddr\>:8443*.

    {{<figure src="/images/netq/adminui-login-page-320.png" width="600">}}

2. Enter your NetQ credentials to enter the application.

    The default username is *admin* and the default password in *admin*.

    {{<figure src="/images/netq/adminui-welcome-330.png" width="600">}}

3. Click **Begin Installation**.

4. Choose an installation type: basic or advanced.

    {{<figure src="/images/netq/adminui-install-type-330.png" width="600">}}

    Read the descriptions carefully to be sure to select the correct type. Then follow these instructions based on your selection.

    {{<tabs "TabID33" >}}

{{<tab "Basic" >}}

1. Select **Basic Install**, then click <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/50-Navigate/navigation-right-circle-1_1.svg" height="18" width="18"/>.

    {{<figure src="/images/netq/adminui-install-type-basic-330.png" width="600">}}

2. Select a deployment type.

    Choose which type of deployment model you want to use. Both options provide secure access to data and features useful for monitoring and troubleshooting your network.

    {{<figure src="/images/netq/adminui-deploy-type-330.png" width="600">}}

3. Install the NetQ software according to your deployment type.

    {{<tabs "TabID49" >}}

{{<tab "Self-hosted DB" >}}

- Enter or upload the NetQ 4.0.0 tarball.

    {{<figure src="/images/netq/adminui-install-onprem-basic-330.png" width="600">}}

- Click <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/50-Navigate/navigation-right-circle-1_1.svg" height="18" width="18"/> once you are ready to install.

    NOTE: You cannot stop the installation once it has begun.

{{</tab>}}

{{<tab "Remote-hosted DB" >}}

- Enter or upload the NetQ 4.0.0 tarball.

- Enter your configuration key.

    {{<figure src="/images/netq/adminui-install-cloud-basic-330.png" width="600">}}

- Click <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/50-Navigate/navigation-right-circle-1_1.svg" height="18" width="18"/>.

    NOTE: You cannot stop the installation once it has begun.

{{</tab>}}

{{</tabs>}}

4. Monitor the progress of the installation job. Click **Details** for a job to see more granular progress.

    {{<figure src="/images/netq/adminui-install-onprem-basic-inprogress-details-330.png" width="600">}}

### Installation Results

If the installation succeeds, you are directed to the Health page of the Admin UI. Refer to {{<link title="Install NetQ Using the Admin UI/#view-netq-system-health" text="View NetQ System Health">}}.

If the installation fails, a failure indication is given.

{{<figure src="/images/netq/adminui-install-basic-failure-330.png" width="600">}}

1. Click <img src="https://icons.cumulusnetworks.com/05-Internet-Networks-Servers/08-Upload-Download/download-bottom.svg" height="18" width="18"/> to download a json file with a description why the installation failed.

2. Can the error can be resolved by moving to the advanced configuration flow?

    - **No**: close the Admin UI, resolve the error, run `netq boostrap reset` and `netq bootstrap master` commands, then reopen the Admin UI to start installation again.
    - **Yes**: click {{<img src="/images/netq/adminui-install-advanced-icon-320.png" height="18" width="18" >}} to be taken to the advanced installation flow and retry the failed task. Refer to the **Advanced** tab for instructions.

{{</tab>}}

{{<tab "Advanced" >}}

1. Select **Advanced Install**, then click <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/50-Navigate/navigation-right-circle-1_1.svg" height="18" width="18"/>.

    {{<figure src="/images/netq/adminui-install-type-advanced-330.png" width="600">}}

2. Select your deployment type.

    Choose the deployment model you want to use. Both options provide secure access to data and features useful for monitoring and troubleshooting your network.

    {{<figure src="/images/netq/adminui-deploy-type-advanced-330.png" width="600">}}

3. Monitor the initialization of the master node. When complete, click <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/50-Navigate/navigation-right-circle-1_1.svg" height="18" width="18"/>.

    {{<figure src="/images/netq/adminui-init-master-onprem-advanced-330.png" width="600" caption="Self-hosted, on-premises deployment">}}

    {{<figure src="/images/netq/adminui-init-master-cloud-advanced-330.png" width="600" caption="Remote-hosted, multi-site or cloud deployment">}}

4. For on-premises (self-hosted) deployments only, select your install method. For cloud deployments, skip to Step 5.

    Choose between restoring data from a previous version of NetQ or performing a fresh installation.

<div style="padding-left: 18px;">
{{<notice info>}}
If you are moving from a standalone to a server cluster arrangement, you can only restore your data one time. After the data has been converted to the cluster schema, it cannot be returned to the single server format.
{{</notice>}}
</div>

    {{<figure src="/images/netq/adminui-install-method-advanced-330.png" width="600">}}

<div style="padding-left: 18px;">
<ul>
<li><strong>Fresh Install</strong>: Continue with Step 5.</li>
<li><strong>Maintain Existing Data</strong> (on-premises only): If you have created a backup of your NetQ data, choose this option. Enter the restoration filename in the field provided and click <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/50-Navigate/navigation-right-circle-1_1.svg" height="18" width="18"/> or upload it.</li>
</ul>

    {{<figure src="/images/netq/adminui-restore-db-advanced-330.png" width="600">}}

</div>

5. Select your server arrangement.

    Select whether you want to deploy your infrastructure as a single stand-alone server or as a cluster of servers.

    {{<figure src="/images/netq/adminui-server-arrange-advanced-330.png" width="600">}}

{{<tabs "TabID137" >}}

{{<tab "Single Server" >}}

Monitor the master configuration. When complete click <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/50-Navigate/navigation-right-circle-1_1.svg" height="18" width="18"/>.

{{<figure src="/images/netq/adminui-master-config-advanced-330.png" width="600">}}

{{</tab>}}

{{<tab "Server Cluster" >}}

Use the private IP addresses that you assigned to the nodes being used as worker nodes to add the worker nodes to the server cluster.

{{<figure src="/images/netq/adminui-cluster-config-330.png" width="600">}}

Click **Add Worker Node**. Enter the unique private IP address for the first worker node. It cannot be the same as the master node or other worker nodes. Click **Add**.

{{<figure src="/images/netq/adminui-cluster-config-add-worker-320.png" width="400">}}

Monitor the progress. When complete click <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/50-Navigate/navigation-right-circle-1_1.svg" height="18" width="18"/>.

{{<figure src="/images/netq/adminui-cluster-config-add-worker-inprocess-320.png" width="400">}}

Repeat these steps for the second worker node.

Click **Create Cluster**. When complete click <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/50-Navigate/navigation-right-circle-1_1.svg" height="18" width="18"/>.

If either of the add worker jobs fail, an indication is given. For example, the IP address provided for the worker node was unreachable. You can see this by clicking <img src="https://icons.cumulusnetworks.com/05-Internet-Networks-Servers/08-Upload-Download/download-bottom.svg" height="18" width="18"/> to open the error file.

{{<figure src="/images/netq/adminui-cluster-config-add-worker-failure-320.png" width="400">}}

{{<figure src="/images/netq/adminui-cluster-config-add-worker-error-file-320.png" width="400">}}

Refer to {{<link title="Post Installation Configuration Options/#add-more-nodes-to-your-server-cluster" text="Add More Nodes to Your Server Cluster">}} to add additional worker nodes *after* NetQ installation is complete.

{{</tab>}}

{{</tabs>}}

6. Install the NetQ software.

    You install the NetQ software using the installation files (`NetQ-4.0.0-tgz` for on-premises deployments or `NetQ-4.0.0-opta.tgz` for cloud deployments) that you downloaded and stored previously.

    *For on-premises*: Accept the path and filename suggested, or modify these to reflect where you stored your installation file, then click <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/50-Navigate/navigation-right-circle-1_1.svg" height="18" width="18"/>. Alternately, upload the file.

    {{<figure src="/images/netq/adminui-install-onprem-advanced-330.png" width="600">}}

<div style="padding-left: 18px;">

<em>For cloud</em>: Accept the path and filename suggested, or modify these to reflect where you stored your installation file. Enter your configuration key. Then click <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/50-Navigate/navigation-right-circle-1_1.svg" height="18" width="18"/>.

{{<figure src="/images/netq/adminui-install-cloud-advanced-330.png" width="600">}}

If the installation fails, a failure indication is given. For example:

{{<figure src="/images/netq/adminui-install-advanced-failure-320.png" width="600">}}

Click <img src="https://icons.cumulusnetworks.com/05-Internet-Networks-Servers/08-Upload-Download/download-bottom.svg" height="18" width="18"/> to download an error file in JSON format, or click <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/50-Navigate/navigation-left-circle-1_1.svg" height="18" width="18"/> to return to the previous step.

</div>

7. Activate NetQ.

    This final step activates the software and enables you to view the health of your NetQ system. For remote deployments, you must enter your configuration key.

    {{<figure src="/images/netq/adminui-activate-netq-onprem-240.png" width="700" caption="Self-hosted activation">}}

    {{<figure src="/images/netq/adminui-activate-netq-cloud-240.png" width="700" caption="Remote-hosted activation">}}

{{</tab>}}

{{</tabs>}}

## View NetQ System Health

When the installation and activation is complete, the NetQ System Health dashboard is visible for tracking the status of key components in the system. The cards displayed represent the deployment chosen:

| Server Arrangement | Deployment Type | Node Card/s | Pod Card | Kafka Card | Zookeeper Card | Cassandra Card |
| ---- | ---- | ---- | :----: | :----: | :----: | :----: |
| Standalone server | On-premises | Master | Yes | Yes | Yes | Yes |
| Standalone server | Cloud | Master | Yes | No | No | No |
| Server cluster | On-premises | Master, 2+ Workers | Yes | Yes | Yes | Yes |
| Server cluster | Cloud | Master, 2+ Workers | Yes | No | No | No |

{{<figure src="/images/netq/adminui-health-standalone-onprem-320.png" width="700" caption="Self-hosted, on-premises deployment">}}

{{<figure src="/images/netq/adminui-health-standalone-cloud-330.png" width="700" caption="Remote-hosted, mulit-site or cloud, deployment">}}

If you have deployed an on-premises solution, you can add a custom signed certificate. Refer to {{<link title="Post Installation Configuration Options/#install-a-custom-signed-certificate" text="Install a Certificate">}} for instructions.

Click **Open NetQ** to enter the NetQ UI application.
