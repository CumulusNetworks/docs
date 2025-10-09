---
title: Configuration Updates
author: Cumulus Networks
weight: 172
toc: 3
---

After installation or upgrade of NetQ is complete, there are a few additional configuration tasks that might be required.

## Add More Nodes to Your Server Cluster

Installation of NetQ with a server cluster sets up the master and two worker nodes. To expand your cluster to include up to a total of nine worker nodes, use the Admin UI.

To add more worker nodes:

1. Prepare the nodes. Refer to the relevant server cluster instructions in {{<link title="Install NetQ System Platform" text="Install NetQ System Platform">}}.

2. Open the Admin UI by entering *https://\<master-hostname-or-ipaddress\>:8443* in your browser address field.

    This opens the Health dashboard for NetQ.

2. Click **Cluster** to view your current configuration.

    {{<figure src="/images/netq/adminui-cluster-tab-241.png" width="700" caption="On-premises deployment">}}

    This opens the Cluster dashboard, with the details about each node in the cluster.

3. Click **Add Worker Node**.

4. Enter the *private* IP address of the node you want to add.

5. Click **Add**.

    Monitor the progress of the three jobs by clicking <img src="https://icons.cumulusnetworks.com/52-Arrows-Diagrams/01-Arrows/arrow-circle-down.svg" height="18" width="18"/> next to the jobs.

    On completion, a card for the new node is added to the Cluster dashboard.

    If the addition fails for any reason, download the log file by clicking <img src="https://icons.cumulusnetworks.com/05-Internet-Networks-Servers/08-Upload-Download/download-bottom.svg" height="18" width="18"/>, run `netq bootstrap reset` on this new worker node, and then try again.

6. Repeat this process to add more worker nodes as needed.

## Update Your Cloud Activation Key

The cloud activation key is the one used to access the Cloud services, not the authorization keys used for configuring the CLI. It is provided by Cumulus Networks when your premises is set up. It is called the *config-key*.

There are occasions where you might want to update your cloud service activation key. For example, if you mistyped the key during installation and now your existing key does not work, or you received a new key for your premises from Cumulus Networks.

Update the activation key using the Admin UI or NetQ CLI:

{{< tabs "TabID50" >}}

{{< tab "Admin UI" >}}

1. Open the Admin UI by entering *https://\<master-hostname-or-ipaddress\>:8443* in your browser address field.

2. Click **Settings**.

3. Click **Activation**.

4. Click **Edit**.

5. Enter your new configuration key in the designated text box.

6. Click **Apply**.

{{< /tab >}}

{{< tab "NetQ CLI" >}}

Run the following command on your standalone or master NetQ Cloud Appliance or VM replacing `text-opta-key` with your new key.

```
cumulus@<hostname>:~$ netq install [standalone|cluster] activate-job config-key <text-opta-key>
```

{{< /tab >}}

{{< /tabs >}}
