---
title: Post Installation Configuration Options
author: Cumulus Networks
weight: 710
toc: 3
---

This topic describes how to configure deployment options that can only be performed after installation or upgrade of NetQ is complete.

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
cumulus@<hostname>:~$ netq install standalone activate-job config-key <text-opta-key>
```

{{< /tab >}}

{{< /tabs >}}

## Add More Nodes to Your Server Cluster

Installation of NetQ with a server cluster sets up the master and two worker nodes. To expand your cluster to include up to a total of nine worker nodes, use the Admin UI.

{{<notice note>}}
Adding additional worker nodes increases availability, but does not increase scalability at this time. A maximum of 1000 nodes is supported regardless of the number of worker nodes in your cluster.
{{</notice>}}

To add more worker nodes:

1. Prepare the nodes. Refer to the relevant server cluster instructions in {{<link title="Install the NetQ System">}}.

2. Open the Admin UI by entering *https://\<master-hostname-or-ipaddress\>:8443* in your browser address field.

    This opens the Health dashboard for NetQ.

3. Click **Cluster** to view your current configuration.

    {{<figure src="/images/netq/adminui-cluster-tab-241.png" width="700" caption="On-premises deployment">}}

    This opens the Cluster dashboard, with the details about each node in the cluster.

4. Click **Add Worker Node**.

5. Enter the *private* IP address of the node you want to add.

6. Click **Add**.

    Monitor the progress of the three jobs by clicking <img src="https://icons.cumulusnetworks.com/52-Arrows-Diagrams/01-Arrows/arrow-circle-down.svg" height="18" width="18"/> next to the jobs.

    On completion, a card for the new node is added to the Cluster dashboard.

    If the addition fails for any reason, download the log file by clicking <img src="https://icons.cumulusnetworks.com/05-Internet-Networks-Servers/08-Upload-Download/download-bottom.svg" height="18" width="18"/>, run `netq bootstrap reset` on this new worker node, and then try again.

7. Repeat this process to add more worker nodes as needed.