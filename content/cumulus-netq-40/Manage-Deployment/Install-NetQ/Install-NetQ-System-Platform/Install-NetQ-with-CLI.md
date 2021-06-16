---
title: Install NetQ Using the CLI
author: NVIDIA
weight: 250
toc: 5
---
You can now install the NetQ software using the NetQ CLI.

{{<notice info>}}
This is the final set of steps for installing NetQ. If you have not already performed the installation preparation steps, go to {{<link title="Install the NetQ System">}} before continuing here.
{{</notice>}}

## Install the NetQ System

To install NetQ, log in to your NetQ platform server, NetQ Appliance, NetQ Cloud Appliance or the master node of your cluster.

Then, to install the software, choose the tab for the type of deployment:

{{<tabs "TabID0" >}}

{{<tab "On-premises, Single Server Deployment" >}}

Run the following command on your NetQ platform server or NetQ Appliance:

```
cumulus@hostname:~$ netq install standalone full interface eth0 bundle /mnt/installables/NetQ-4.0.0.tgz
```

{{</tab>}}

{{<tab "On-premises, Server Cluster Deployment" >}}

Run the following commands on your *master* node, using the IP addresses of your worker nodes:

```
cumulus@<hostname>:~$ netq install cluster full interface eth0 bundle /mnt/installables/NetQ-4.0.0.tgz workers <worker-1-ip> <worker-2-ip>
```

{{</tab>}}

{{</tabs>}}

{{<notice tip>}}
You can specify the IP address instead of the interface name here: use <code>ip-addr &lt;IP address&gt;</code> in place of <code>interface &lt;ifname&gt;</code> above.
{{</notice>}}

Run the `netq show opta-health` command to verify all applications are operating properly. Please allow 10-15 minutes for all applications to come up and report their status.

```
cumulus@hostname:~$ netq show opta-health
Application                                            Status    Namespace      Restarts    Timestamp
-----------------------------------------------------  --------  -------------  ----------  ------------------------
cassandra-rc-0-w7h4z                                   READY     default        0           Fri Apr 10 16:08:38 2020
cp-schema-registry-deploy-6bf5cbc8cc-vwcsx             READY     default        0           Fri Apr 10 16:08:38 2020
kafka-broker-rc-0-p9r2l                                READY     default        0           Fri Apr 10 16:08:38 2020
kafka-connect-deploy-7799bcb7b4-xdm5l                  READY     default        0           Fri Apr 10 16:08:38 2020
netq-api-gateway-deploy-55996ff7c8-w4hrs               READY     default        0           Fri Apr 10 16:08:38 2020
netq-app-address-deploy-66776ccc67-phpqk               READY     default        0           Fri Apr 10 16:08:38 2020
netq-app-admin-oob-mgmt-server                         READY     default        0           Fri Apr 10 16:08:38 2020
netq-app-bgp-deploy-7dd4c9d45b-j9bfr                   READY     default        0           Fri Apr 10 16:08:38 2020
netq-app-clagsession-deploy-69564895b4-qhcpr           READY     default        0           Fri Apr 10 16:08:38 2020
netq-app-configdiff-deploy-ff54c4cc4-7rz66             READY     default        0           Fri Apr 10 16:08:38 2020
...
```

{{<notice note>}}
If any of the applications or services display Status as DOWN after 30 minutes, open a support ticket and attach the output of the <code>opta-support</code> command.
{{</notice>}}

## Install the OPTA Server

To install the OPTA server, choose the tab for the type of deployment:

{{<tabs "TabID01" >}}

{{<tab "Cloud, Single Server Deployment" >}}

Run the following command on your NetQ Cloud Appliance with the `config-key` sent by NVIDIA in an email titled <!-- vale off -->*"A new site has been added to your NVIDIA Cumulus NetQ account."*<!-- vale on -->

```
cumulus@<hostname>:~$ netq install opta standalone full interface eth0 bundle /mnt/installables/NetQ-4.0.0-opta.tgz config-key <your-config-key-from-email> proxy-host <proxy-hostname> proxy-port <proxy-port>
```

{{</tab>}}

{{<tab "Cloud, Server Cluster Deployment" >}}

Run the following commands on your *master* NetQ Cloud Appliance with the `config-key` sent by NVIDIA in an email titled <!-- vale off -->*"A new site has been added to your NVIDIA Cumulus NetQ account."*<!-- vale on -->

```
cumulus@<hostname>:~$ netq install opta cluster full interface eth0 bundle /mnt/installables/NetQ-4.0.0-opta.tgz config-key <your-config-key-from-email> workers <worker-1-ip> <worker-2-ip> proxy-host <proxy-hostname> proxy-port <proxy-port>
```

{{</tab>}}

{{</tabs>}}

{{<notice tip>}}
You can specify the IP address instead of the interface name here: use <code>ip-addr &lt;IP address&gt;</code> in place of <code>interface eth0</code> above.
{{</notice>}}

Run the `netq show opta-health` command to verify all applications are operating properly.

```
cumulus@hostname:~$ netq show opta-health
OPTA is healthy
```
