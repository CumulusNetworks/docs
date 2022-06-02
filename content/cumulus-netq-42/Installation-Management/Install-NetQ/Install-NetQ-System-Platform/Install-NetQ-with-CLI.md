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
cumulus@hostname:~$ netq install standalone full interface eth0 bundle /mnt/installables/NetQ-4.2.0.tgz
```

{{<notice note>}}
You can specify the IP address instead of the interface name here: use <code>ip-addr &lt;IP address&gt;</code> in place of <code>interface &lt;ifname&gt;</code> above.

If you have changed the IP address or hostname of the NetQ On-premises VM after this step, you need to re-register this address with NetQ as follows:

Reset the VM, indicating whether you want to purge any NetQ DB data or keep it.

<pre>cumulus@hostname:~$ netq bootstrap reset [purge-db|keep-db]</pre>

Re-run the install CLI on the appliance. This example uses interface eno1. Replace this with your updated IP address, hostname or interface using the interface or ip-addr option.
<pre>cumulus@hostname:~$ netq install standalone full interface eno1 bundle /mnt/installables/NetQ-4.2.0.tgz</pre>

{{</notice>}}

{{<notice tip>}}
If this step fails for any reason, you can run <code>netq bootstrap reset</code> and then try again.
{{</notice>}}

{{</tab>}}

{{<tab "On-premises, Server Cluster Deployment" >}}

Run the following command on your *master* node to initialize the cluster. Copy the output of the command to use on your worker nodes:

```
cumulus@<hostname>:~$ netq install cluster master-init
Please run the following command on all worker nodes:
netq install cluster worker-init c3NoLXJzYSBBQUFBQjNOemFDMXljMkVBQUFBREFRQUJBQUFCQVFDM2NjTTZPdVVUWWJ5c2Q3NlJ4SHdseHBsOHQ4N2VMRWVGR05LSWFWVnVNcy94OEE4RFNMQVhKOHVKRjVLUXBnVjdKM2lnMGJpL2hDMVhmSVVjU3l3ZmhvVDVZM3dQN1oySVZVT29ZTi8vR1lOek5nVlNocWZQMDNDRW0xNnNmSzVvUWRQTzQzRFhxQ3NjbndIT3dwZmhRYy9MWTU1a
```

Run the `netq install cluster worker-init <ssh-key>` on each of your worker nodes.

Run the following commands on your *master* node, using the IP addresses of your worker nodes:

```
cumulus@<hostname>:~$ netq install cluster full interface eth0 bundle /mnt/installables/NetQ-4.2.0.tgz workers <worker-1-ip> <worker-2-ip>
```

{{<notice note>}}
You can specify the IP address instead of the interface name here: use <code>ip-addr &lt;IP address&gt;</code> in place of <code>interface &lt;ifname&gt;</code> above.<br>

If you have changed the IP address or hostname of the NetQ On-premises VM after this step, you need to re-register this address with NetQ as follows:

Reset the VM, indicating whether you want to purge any NetQ DB data or keep it.

<pre>cumulus@hostname:~$ netq bootstrap reset [purge-db|keep-db]</pre>

Re-run the install CLI on the appliance. This example uses interface eno1. Replace this with your updated IP address, hostname or interface using the interface or ip-addr option.
<pre>cumulus@hostname:~$ netq install standalone full interface eno1 bundle /mnt/installables/NetQ-4.2.0.tgz</pre>

{{</notice>}}

{{<notice tip>}}
If this step fails for any reason, you can run <code>netq bootstrap reset</code> and then try again.
{{</notice>}}

{{</tab>}}

{{</tabs>}}

## Install the OPTA Server

To install the OPTA server, choose the tab for the type of deployment:

{{<tabs "TabID01" >}}

{{<tab "Cloud, Single Server Deployment" >}}

<!-- vale off -->
Run the following command on your NetQ Cloud Appliance with the `config-key` obtained from the email you received from NVIDIA titled _NetQ Access Link_. You can also obtain the configuration key through the NetQ UI in the premise management configuration. For more information, see {{<link title="Access the NetQ UI#log-in-to-netq" text="First Time Log In - NetQ Cloud">}}.
<!-- vale on -->

```
cumulus@<hostname>:~$ netq install opta standalone full interface eth0 bundle /mnt/installables/NetQ-4.2.0-opta.tgz config-key <your-config-key> [proxy-host <proxy-hostname> proxy-port <proxy-port>]
```

{{<notice note>}}
You can specify the IP address instead of the interface name here: use <code>ip-addr &lt;IP address&gt;</code> in place of <code>interface &lt;ifname&gt;</code> above.

If you have changed the IP address or hostname of the NetQ OPTA after this step, you need to re-register this address with NetQ as follows:

Reset the VM:

<pre>cumulus@hostname:~$ netq bootstrap reset</pre>

Re-run the install CLI on the appliance. This example uses interface eno1. Replace this with your updated IP address, hostname or interface using the interface or ip-addr option.
<pre>cumulus@hostname:~$ netq install opta standalone full interface eno1 bundle /mnt/installables/NetQ-4.2.0-opta.tgz config-key <your-config-key> [proxy-host <proxy-hostname> proxy-port <proxy-port>]</pre>
{{</notice>}}

{{<notice tip>}}
If this step fails for any reason, you can run <code>netq bootstrap reset</code> and then try again.
{{</notice>}}

Consider the following for container environments, and make adjustments as needed.

{{<netq-install/container version="4.2">}}

{{</tab>}}

{{<tab "Cloud, Server Cluster Deployment" >}}

Run the following command on your *master* node to initialize the cluster. Copy the output of the command to use on your worker nodes:

```
cumulus@<hostname>:~$ netq install cluster master-init
Please run the following command on all worker nodes:
netq install cluster worker-init c3NoLXJzYSBBQUFBQjNOemFDMXljMkVBQUFBREFRQUJBQUFCQVFDM2NjTTZPdVVUWWJ5c2Q3NlJ4SHdseHBsOHQ4N2VMRWVGR05LSWFWVnVNcy94OEE4RFNMQVhKOHVKRjVLUXBnVjdKM2lnMGJpL2hDMVhmSVVjU3l3ZmhvVDVZM3dQN1oySVZVT29ZTi8vR1lOek5nVlNocWZQMDNDRW0xNnNmSzVvUWRQTzQzRFhxQ3NjbndIT3dwZmhRYy9MWTU1a
```

Run the `netq install cluster worker-init <ssh-key>` on each of your worker nodes.

<!-- vale off -->
Run the following command on your NetQ Cloud Appliance with the `config-key` obtained from the email you received from NVIDIA titled _NetQ Access Link_. You can also obtain the configuration key through the NetQ UI in the premise management configuration. For more information, see {{<link title="Access the NetQ UI#log-in-to-netq" text="First Time Log In - NetQ Cloud">}}.
<!-- vale on -->

```
cumulus@<hostname>:~$ netq install opta cluster full interface eth0 bundle /mnt/installables/NetQ-4.2.0-opta.tgz config-key <your-config-key> workers <worker-1-ip> <worker-2-ip> [proxy-host <proxy-hostname> proxy-port <proxy-port>]
```

{{<notice note>}}
You can specify the IP address instead of the interface name here: use <code>ip-addr &lt;IP address&gt;</code> in place of <code>interface &lt;ifname&gt;</code> above.

If you have changed the IP address or hostname of the NetQ OPTA after this step, you need to re-register this address with NetQ as follows:

Reset the VM:

<pre>cumulus@hostname:~$ netq bootstrap reset</pre>

Re-run the install CLI on the appliance. This example uses interface eth0. Replace this with your updated IP address, hostname or interface using the interface or ip-addr option.
<pre>cumulus@hostname:~$ netq install opta standalone full interface eth0 bundle /mnt/installables/NetQ-4.2.0-opta.tgz config-key <your-config-key> [proxy-host <proxy-hostname> proxy-port <proxy-port>]</pre>
{{</notice>}}

{{<notice tip>}}
If this step fails for any reason, you can run <code>netq bootstrap reset</code> and then try again.
{{</notice>}}

Consider the following for container environments, and make adjustments as needed.

{{<netq-install/container version="4.2">}}

{{</tab>}}

{{</tabs>}}

Run the `netq show opta-health` command to verify all applications are operating properly.

```
cumulus@hostname:~$ netq show opta-health
OPTA is healthy
```

## Verify Installation Status

To view the status of the installation, use the `netq show status [verbose]` command. The following example shows a successful on-premise installation:

```$ netq show status
State: Active
Version: 4.2.0
Installer Version: 4.2.0
Installation Type: Standalone
Activation Key: PKrgipMGEhVuZXRxLWVuZHBvaW50LWdhdGV3YXkYsagDIixUQmFLTUhzZU80RUdTL3pOT01uQ2lnRnrrUhTbXNPUGRXdnUwTVo5SEpBPTIHZGVmYXVsdDoHbmV0cWRldgz=
Master SSH Public Key: a3NoLXJzYSBBQUFBQjNOemFDMXljMkVBQUFBREFRQUJBQUFCQVFEazliekZDblJUajkvQVhOZ0hteXByTzZIb3Y2cVZBWFdsNVNtKzVrTXo3dmMrcFNZTGlOdWl1bEhZeUZZVDhSNmU3bFdqS3NrSE10bzArNFJsQVd6cnRvbVVzLzlLMzQ4M3pUMjVZQXpIU2N1ZVhBSE1TdTZHZ0JyUkpXYUpTNjJ2RTkzcHBDVjBxWWJvUFo3aGpCY3ozb0VVWnRsU1lqQlZVdjhsVjBNN3JEWW52TXNGSURWLzJ2eks3K0x2N01XTG5aT054S09hdWZKZnVOT0R4YjFLbk1mN0JWK3hURUpLWW1mbTY1ckoyS1ArOEtFUllrr5TkF3bFVRTUdmT3daVHF2RWNoZnpQajMwQ29CWDZZMzVST2hDNmhVVnN5OEkwdjVSV0tCbktrWk81MWlMSDAyZUpJbXJHUGdQa2s1SzhJdGRrQXZISVlTZ0RwRlpRb3Igcm9vdEBucXRzLTEwLTE4OC00NC0xNDc=
Is Cloud: False

Cluster Status:
IP Address     Hostname       Role    Status
-------------  -------------  ------  --------
10.188.44.147  10.188.44.147  Role    Ready

NetQ... Active
```

Run the `netq show opta-health` command to verify all applications are operating properly. Allow 10-15 minutes for all applications to come up and report their status.

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
