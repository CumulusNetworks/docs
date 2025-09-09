---
title: Set Up Your Virtual Machine for an On-premises HA Scale Cluster
author: NVIDIA
weight: 227
toc: 5
bookhidden: true
---
Follow these steps to set up and configure your VM on a cluster of servers in an on-premises deployment. First configure the VM on the master node, and then configure the VM on each additional node. NVIDIA recommends installing the virtual machines on different servers to increase redundancy in the event of a hardware failure. 

{{%notice note%}}
NetQ 4.15.0 supports a 3-node HA scale cluster consisting of 1 master and 2 additional high-availability (HA) nodes or a 5-node cluster consisting of 1 master, 2 HA nodes, and 2 worker nodes.
{{%/notice%}}
- - -

## System Requirements

Verify that *each node* in your cluster meets the VM requirements.

| Resource | Minimum Requirements |
| :--- | :--- |
| Processor | 48 virtual CPUs |
| Memory | 512GB RAM |
| Local disk storage | 3.2TB SSD with minimum disk IOPS of 1000 for a standard 4kb block size<br> (Note: This must be an SSD; other storage options can lead to system instability and are not supported.)|
| Network interface speed | 10 Gbps NIC |
| Hypervisor | KVM/QCOW (QEMU Copy on Write) image for servers running Ubuntu;<br> VMware ESXi™ 6.5 or later (OVA image) for servers running Cumulus Linux or Ubuntu | 

## Port Requirements

Confirm that the required ports are open for communications.

| Port or Protocol Number | Protocol | Component Access |
| --- | --- | --- |
|4	|IP Protocol|	Calico networking (IP-in-IP Protocol)|
|22	|TCP|	SSH|
|80	|TCP|	nginx|
|179	|TCP|	Calico networking (BGP)|
|443	|TCP|	NetQ UI|
|2379	|TCP|	etcd datastore|
|4789	|UDP|	Calico networking (VxLAN)|
|5000	|TCP|	Docker registry|
|6443	|TCP|	kube-apiserver|
|30001	|TCP|	DPU communication|
|31980	|TCP|	NetQ Agent communication|
|31982	|TCP|	NetQ Agent SSL communication|
|32708	|TCP|	API Gateway|

Additionally, for internal cluster communication, you must open these ports:

| Port or Protocol Number | Protocol | Component Access |
| --- | --- | --- |
|8080|	TCP|	Admin API|
|5000|	TCP|	Docker registry|
|6443|	TCP|	Kubernetes API server|
|10250|	TCP|	kubelet health probe|
|2379|	TCP|	etcd|
|2380|	TCP|	etcd|
|7072|	TCP|	Kafka JMX monitoring|
|9092|	TCP|	Kafka client|
|7071|	TCP|	Cassandra JMX monitoring|
|7000|	TCP|	Cassandra cluster communication|
|9042|	TCP|	Cassandra client|
|7073|	TCP|	Zookeeper JMX monitoring|
|2888|	TCP|	Zookeeper cluster communication|
|3888|	TCP|	Zookeeper cluster communication|
|2181|	TCP|	Zookeeper client|
|36443|	TCP|	Kubernetes control plane|

## Installation and Configuration

1. Download the NetQ image.

    a. Log in to your {{<exlink url="https://nvid.nvidia.com/" text="NVIDIA Application Hub">}} account.<br>
    b. Select **NVIDIA Licensing Portal**.<br>
    c. Select **Software Downloads** from the menu.<br>
    d. Click **Product Family** and select **NetQ**.<br>
    e. For deployments using KVM, download the **NetQ SW 4.15.0 KVM Scale** image. For deployments using VMware, download the **NetQ SW 4.15.0 VMware Scale** image<br>
    f. If prompted, read the license agreement and proceed with the download.<br>

{{%notice note%}}
NVIDIA employees can download NetQ directly from the {{<exlink url="http://ui.licensing.nvidia.com/" text="NVIDIA Licensing Portal">}}.
{{%/notice%}}

2. Open your hypervisor and configure your VM. You can use the following examples for reference or use your own hypervisor instructions.

 {{<netq-install/vm-setup hypervisor="kvm" deployment="onprem-scale-cluster" version="4.15">}}

 {{<netq-install/vm-setup hypervisor="vmware" version="4.15">}}

3. Log in to the VM and change the password.

Use the default credentials to log in the first time:

- Username: nvidia
- Password: nvidia

```
$ ssh nvidia@<ipaddr>
Warning: Permanently added '<ipaddr>' (ECDSA) to the list of known hosts.
Ubuntu 24.04 LTS
nvidia@<ipaddr>'s password:
You are required to change your password immediately (root enforced)
System information as of Thu Dec  3 21:35:42 UTC 2024
System load:  0.09              Processes:           120
Usage of /:   8.1% of 61.86GB   Users logged in:     0
Memory usage: 5%                IP address for eth0: <ipaddr>
Swap usage:   0%
WARNING: Your password has expired.
You must change your password now and login again!
Changing password for nvidia.
(current) UNIX password: nvidia
Enter new UNIX password:
Retype new UNIX password:
passwd: password updated successfully
Connection to <ipaddr> closed.
```
Log in again with your new password.

```
$ ssh nvidia@<ipaddr>
Warning: Permanently added '<ipaddr>' (ECDSA) to the list of known hosts.
Ubuntu 24.04 LTS
nvidia@<ipaddr>'s password:
  System information as of Thu Dec  3 21:35:59 UTC 2024
  System load:  0.07              Processes:           121
  Usage of /:   8.1% of 61.86GB   Users logged in:     0
  Memory usage: 5%                IP address for eth0: <ipaddr>
  Swap usage:   0%
Last login: Thu Dec  3 21:35:43 2024 from <local-ipaddr>
nvidia@ubuntu:~$
```
4. Verify that the master node is ready for installation. Fix any errors before installing the NetQ software.

```
nvidia@hostname:~$ sudo opta-check-scale
```

5. Change the hostname for the VM from the default value.

The default hostname for the NetQ virtual machines is *ubuntu*. Change the hostname to fit your naming conventions while meeting Internet and Kubernetes naming standards.

{{<notice tip>}}
Kubernetes requires hostnames to be composed of a sequence of labels concatenated with dots. For example, “en.wikipedia.org” is a hostname. Each label must be from 1 to 63 characters long. The entire hostname, including the delimiting dots, has a maximum of 253 ASCII characters.<br>
<br>
The Internet standards (RFCs) for protocols specify that labels may contain only the ASCII letters a through z (in lower case), the digits 0 through 9, and the hyphen-minus character ('-').
{{</notice>}}

Set the new hostname using the following command. Replace `NEW_HOSTNAME` with the name you chose.

```
nvidia@hostname:~$ sudo hostnamectl set-hostname NEW_HOSTNAME
```
Add the same `NEW_HOSTNAME` value to **/etc/hosts** on your VM for the localhost entry. For example:

```
127.0.0.1 localhost NEW_HOSTNAME
```

6. Open your hypervisor and set up the VM for the additional nodes in the same manner as for the master node.

7. Run the following command on each node to verify that the node is ready for a NetQ software installation. Fix any errors indicated before installing the software.

```
nvidia@hostname:~$ sudo opta-check scale
```

8. Install and activate the NetQ software using the CLI.

Run the following command on your *master* node to initialize the cluster. Copy the output of the command which includes the SSH key. You will use it in the next step.

```
nvidia@<hostname>:~$ netq install cluster master-init
    Please run the following command on all worker nodes:
    netq install cluster worker-init c3NoLXJzYSBBQUFBQjNOemFDMXljMkVBQUFBREFRQUJBQUFCQVFDM2NjTTZPdVM3dQN9MWTU1a
```
9. Run the `netq install cluster worker-init <ssh-key>` command on each non-master node.

10. Create a JSON template using the installation command for your deployment model.

{{< tabs "Tab179 ">}}

{{< tab "3-Node Cluster">}}

For a 3-node cluster, run the `netq install cluster config generate` command on your master node to generate a template for the cluster configuration JSON file:

```
nvidia@netq-server:~$ netq install cluster config generate
2024-10-28 17:29:53.260462: master-node-installer: Writing cluster installation configuration template file @ /tmp/cluster-install-config.json
```
{{< /tab >}}
{{< tab "5-Node Cluster">}}
For a 5-node cluster, run the `netq install cluster config generate workers 2` command on your master node to generate a cluster configuration JSON file with 2 additional `worker-nodes` objects:

```
nvidia@netq-server:~$ netq install cluster config generate workers 2
2024-10-28 17:29:53.260462: master-node-installer: Writing cluster installation configuration template file @ /tmp/cluster-install-config.json
```

{{< /tab >}}
{{< /tabs >}}

11. Edit the cluster configuration JSON file with the values for each attribute.

{{< tabs "Tab188 ">}}

{{< tab "Default JSON Template">}}

The following example includes the `worker-nodes` objects for a 5-node deployment. The JSON template for the 3-node deployment will not include `worker-nodes`.  

``` 
nvidia@netq-server:~$ vim /tmp/cluster-install-config.json 
{
        "version": "v2.0",
        "interface": "<INPUT>",
        "cluster-vip": "<INPUT>",
        "master-ip": "<INPUT>",
        "is-ipv6": false,
        "ha-nodes": [
                {
                        "ip": "<INPUT>"
                },
                {
                        "ip": "<INPUT>"
                }
        ]
        "worker-nodes": [
                {
                        "ip": "<INPUT>"
                },
                {
                        "ip": "<INPUT>"
                }
        ]
}
```



| Attribute | Description |
|----- | ----------- |
| `interface` | The local network interface on your master node used for NetQ connectivity. |
| `cluster-vip` | The cluster virtual IP address must be an unused IP address allocated from the same subnet assigned to the default interface for your master and worker nodes. |
| `master-ip` | The IP address assigned to the interface on your master node used for NetQ connectivity. |
| `is-ipv6` | Set the value to `true` if your network connectivity and node address assignments are IPv6. |
| `ha-nodes` | The IP addresses of the two HA nodes in your cluster. |
| `worker-nodes` | The IP addresses of the two worker nodes (for 5-node deployments). |

{{%notice note%}}

NetQ uses the 10.244.0.0/16 (`pod-ip-range`) and 10.96.0.0/16 (`service-ip-range`) networks for internal communication by default. If you are using these networks, you must override each range by specifying new subnets for these parameters in the cluster configuration JSON file:

```
nvidia@netq-server:~$ vim /tmp/cluster-install-config.json 
{
        "version": "v2.0",
        "interface": "eth0",
        "cluster-vip": "10.176.235.101",
        "master-ip": "10.176.235.50",
        "is-ipv6": false,
        "pod-ip-range": "192.168.0.1/32",
	"service-ip-range": "172.168.0.1/32",
        "ha-nodes": [
                {
                        "ip": "10.176.235.51"
                },
                {
                        "ip": "10.176.235.52"
                }
        ]
}
```

{{%/notice%}}

{{< /tab >}}
{{< tab "Completed JSON Example ">}}

The following example configures a 3-node cluster installation with the master IP of 10.176.235.50, and the HA nodes 10.176.235.51 and 10.176.235.52: 
``` 
nvidia@netq-server:~$ vim /tmp/cluster-install-config.json 
{
        "version": "v2.0",
        "interface": "eth0",
        "cluster-vip": "10.176.235.101",
        "master-ip": "10.176.235.50",
        "is-ipv6": false,
        "ha-nodes": [
                {
                        "ip": "10.176.235.51"
                },
                {
                        "ip": "10.176.235.52"
                }
        ]
}
```
The following example configures a 5-node cluster installation with a master node, two HA nodes, and two worker nodes:

```
nvidia@netq-server:~$ vim /tmp/cluster-install-config.json 
{
        "version": "v2.0",
        "interface": "eth0",
        "cluster-vip": "10.176.235.101",
        "master-ip": "10.176.235.50",
        "is-ipv6": false,
        "ha-nodes": [
                {
                        "ip": "10.176.235.51"
                },
                {
                        "ip": "10.176.235.52"
                }
        ]
        "worker-nodes": [
                {
                        "ip": "10.176.235.53"
                },
                {
                        "ip": "10.176.235.54"
                }
        ]
}
```

| Attribute | Description |
|----- | ----------- |
| `interface` | The local network interface on your master node used for NetQ connectivity. |
| `cluster-vip` | The cluster virtual IP address must be an unused IP address allocated from the same subnet assigned to the default interface for your master and worker nodes. |
| `master-ip` | The IP address assigned to the interface on your master node used for NetQ connectivity. |
| `is-ipv6` | Set the value to `true` if your network connectivity and node address assignments are IPv6. |
| `ha-nodes` | The IP addresses of the two HA nodes in your cluster. |
| `worker-nodes` | The IP addresses of the two worker nodes (for 5-node deployments). |

{{< /tab >}}
{{< /tabs >}}


12. Run the installation command on your master node. Follow the steps under _Restore Data and New Install_ if you have a {{<link title="Back Up and Restore NetQ" text="backup data tarball">}} from a previous NetQ installation to restore.

{{< tabs "TabID41 ">}}
{{< tab "New Install">}}

Run the following command on your master node, using the JSON configuration file created in step 11:

```
nvidia@<hostname>:~$ netq install cluster bundle /mnt/installables/NetQ-4.15.0.tgz /tmp/cluster-install-config.json
```

<div class="notices tip"><p>If this step fails for any reason, run <code>netq bootstrap reset</code> and then try again.</p></div>


{{< /tab >}}
{{< tab "Restore Data and New Install">}}

1. Add the `config-key` parameter to the JSON template from step 11 using the key created during the {{<link title="Back Up and Restore NetQ" text="backup process">}}. Edit the file with values for each attribute.

```
nvidia@netq-server:~$ vim /tmp/cluster-install-config.json 
{
        "version": "v2.0",
        "config-key": "<INPUT>",
        "interface": "<INPUT>",
        "cluster-vip": "<INPUT>",
        "master-ip": "<INPUT>",
        "is-ipv6": false,
        "ha-nodes":
                {
                        "ip": "<INPUT>"
                },
                {
                        "ip": "<INPUT>"
                }
}
```

2. Run the following command on your master node, using the JSON configuration file from the previous step. Include the restore option referencing the path where the backup file resides:

```
nvidia@<hostname>:~$ netq install cluster bundle /mnt/installables/NetQ-4.15.0.tgz /tmp/cluster-install-config.json restore /home/cumulus/combined_backup_20241211111316.tar
```

<div class="notices tip"><p><ul><li>If this step fails for any reason, run <code>netq bootstrap reset</code> and then try again.</li><li>If you restore NetQ data to a server with an IP address that is different from the one used to back up the data, you must <a href="https://docs.nvidia.com/networking-ethernet-software/cumulus-netq/Installation-Management/Install-NetQ/Install-NetQ-Agents/#configure-netq-agents">reconfigure the agents</a> on each switch as a final step.</li></ul></p></div>

{{< /tab >}}
{{< /tabs >}}


## Verify Installation Status

To view the status of the installation, use the `netq show status [verbose]` command. The following example shows a successful 3-node installation:

```
State: Active
    NetQ Live State: Active
    Installation Status: FINISHED
    Version: 4.15.0
    Installer Version: 4.15.0
    Installation Type: Cluster
    Activation Key: EhVuZXRxLWVuZHBvaW50LWdhdGV3YXkYsagDIixPSUJCOHBPWUFnWXI2dGlGY2hTRzExR2E5aSt6ZnpjOUvpVVTaDdpZEhFPQ==
    Master SSH Public Key: c3NoLXJzYSBBQUFBQjNOemFDMXljMkVBQUFBREFRQUJBQUFCZ1FDNW9iVXB6RkczNkRC
    Is Cloud: False
    
    Kubernetes Cluster Nodes Status:
    IP Address    Hostname     Role    NodeStatus    Virtual IP
    ------------  -----------  ------  ------------  ------------
    10.213.7.52   10.213.7.52  Worker  Ready         10.213.7.53
    10.213.7.51   10.213.7.51  Worker  Ready         10.213.7.53
    10.213.7.49   10.213.7.49  Master  Ready         10.213.7.53
    
    In Summary, Live state of the NetQ is... Active
```
Run the `netq show opta-health` command to verify that all applications are operating properly. Allow at least 15 minutes for all applications to come up and report their status.

```
nvidia@hostname:~$ netq show opta-health
    Application                                            Status    Namespace      Restarts    Timestamp
    -----------------------------------------------------  --------  -------------  ----------  ------------------------
    cassandra-rc-0-w7h4z                                   READY     default        0           Fri Apr 10 16:08:38 2024
    cp-schema-registry-deploy-6bf5cbc8cc-vwcsx             READY     default        0           Fri Apr 10 16:08:38 2024
    kafka-broker-rc-0-p9r2l                                READY     default        0           Fri Apr 10 16:08:38 2024
    kafka-connect-deploy-7799bcb7b4-xdm5l                  READY     default        0           Fri Apr 10 16:08:38 2024
    netq-api-gateway-deploy-55996ff7c8-w4hrs               READY     default        0           Fri Apr 10 16:08:38 2024
    netq-app-address-deploy-66776ccc67-phpqk               READY     default        0           Fri Apr 10 16:08:38 2024
    netq-app-admin-oob-mgmt-server                         READY     default        0           Fri Apr 10 16:08:38 2024
    netq-app-bgp-deploy-7dd4c9d45b-j9bfr                   READY     default        0           Fri Apr 10 16:08:38 2024
    netq-app-clagsession-deploy-69564895b4-qhcpr           READY     default        0           Fri Apr 10 16:08:38 2024
    netq-app-configdiff-deploy-ff54c4cc4-7rz66             READY     default        0           Fri Apr 10 16:08:38 2024
    ...
```
{{%notice note%}}
If any of the applications or services display a DOWN status after 30 minutes, open a support ticket and attach the output of the `opta-support` command.
{{%/notice%}}
After NetQ is installed, you can {{<link title="Access the NetQ UI" text="log in to NetQ">}} from your browser.

## Add Additional Worker Nodes

When the number of devices in your network grows, you can add additional nodes to your cluster deployment so that NetQ remains operational and can accommodate the additional devices. Refer to the {{<link title="Before You Install/#installation-overview" text="Installation Overview">}} for device support information.

To add additional worker nodes to an existing HA scale cluster, generate a JSON configuration template referencing the number of additional worker nodes you want to add. For example, to expand a 3-node cluster to a 5-node cluster, run the `netq install cluster config generate workers 2` command to generate the JSON configuration template, `/tmp/cluster-install-config.json`:

```
nvidia@netq-server:~$ cat /tmp/cluster-install-config.json
{
        "version": "v2.0",
        "interface": "<INPUT>",
        "cluster-vip": "<INPUT>",
        "master-ip": "<INPUT>",
        "is-ipv6": false,
        "ha-nodes": [
                {
                        "ip": "<INPUT>"
                },
                {
                        "ip": "<INPUT>"
                }
        ],
        "worker-nodes": [
                {
                        "ip": "<INPUT>"
                },
                {
                        "ip": "<INPUT>"
                }
        ]
}
```

Edit this file and configure the parameters, including the existing nodes in your cluster and the new worker IP addresses.

```
{
        "version": "v2.0",
        "interface": "eth0",
        "cluster-vip": "10.176.235.101",
        "master-ip": "10.176.235.50",
        "is-ipv6": false,
        "ha-nodes": [
                {
                        "ip": "10.176.235.51"
                },
                {
                        "ip": "10.176.235.52"
                }
        ]
        "worker-nodes": [
                {
                        "ip": "10.176.235.53"
                },
                {
                        "ip": "10.176.235.54"
                }
        ]
}
```

Install the new workers using the `netq install cluster worker add /tmp/cluster-install-config.json` command.



