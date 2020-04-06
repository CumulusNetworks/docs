---
title: Install NetQ Using the CLI
author: Cumulus Networks
weight: 100
aliases:
 - /display/NETQ/Install+NetQ
 - /pages/viewpage.action?pageId=12320951
pageID: 12320951
toc: 5
---
You can now install the NetQ software using the NetQ CLI.

{{<notice info>}}
This is the final set of steps for installing NetQ. If you have not already performed the installation preparation steps, go to {{<link title="Install NetQ Platform v2">}} before continuing here.
{{</notice>}}

To install NetQ:

1. Log in to your NetQ platform server, NetQ Appliance, NetQ Cloud Appliance or the master node of your cluster.

2. Install the software.

    <details><summary>For On-premises, Single Server Deployment</summary>

    Run the following command on your NetQ platform server or NetQ Appliance:

    ```
    cumulus@<hostname>:~$ netq install standalone full interface eth0 bundle /mnt/installables/NetQ-2.4.1.tgz
    ```

    {{<notice tip>}}
You can specify the IP address instead of the interface name here: use <code>ip-addr &lt;IP address&gt;</code> in place of <code>interface eth0</code> above.
    {{</notice>}}
    </details>
    <details><summary>For On-premises, Server Cluster Deployment</summary>

    Run the following commands on your *master* node, using the IP addresses of your worker nodes:

    ```
    cumulus@<hostname>:~$ netq install cluster full interface eth0 bundle /mnt/installables/NetQ-2.4.1.tgz workers <worker-1-ip> <worker-2-ip>
    ```

    {{<notice tip>}}
You can specify the IP address instead of the interface name here: use <code>ip-addr &lt;IP address&gt;</code> in place of <code>interface eth0</code> above.
    {{</notice>}}
    </details>
    <details><summary>For Cloud, Single Server Deployment</summary>

    Run the following command on your NetQ Cloud Appliance with the `config-key` sent by Cumulus Networks in an email titled "A new site has been added to your Cumulus NetQ account."

    ```
    cumulus@<hostname>:~$ netq install opta standalone full interface eth0 bundle /mnt/installables/NetQ-2.4.1-opta.tgz config-key <your-config-key-from-email> proxy-host <proxy-hostname> proxy-port <proxy-port>
    ```

    {{<notice tip>}}
You can specify the IP address instead of the interface name here: use <code>ip-addr &lt;IP address&gt;</code> in place of <code>interface eth0</code> above.
    {{</notice>}}
    </details>
    <details><summary>For Cloud, Server Cluster Deployment</summary>
    
    Run the following commands on your *master* NetQ Cloud Appliance with the `config-key` sent by Cumulus Networks in an email titled "A new site has been added to your Cumulus NetQ account."

    ```
    cumulus@<hostname>:~$ netq install opta cluster full interface eth0 bundle /mnt/installables/NetQ-2.4.1-opta.tgz config-key <your-config-key-from-email> workers <worker-1-ip> <worker-2-ip> proxy-host <proxy-hostname> proxy-port <proxy-port>
    ```

    {{<notice tip>}}
You can specify the IP address instead of the interface name here: use <code>ip-addr &lt;IP address&gt;</code> in place of <code>interface eth0</code> above.
    {{</notice>}}
    </details>
