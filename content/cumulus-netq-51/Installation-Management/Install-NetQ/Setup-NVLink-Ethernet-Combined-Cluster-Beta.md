---
title: Install NetQ for Ethernet and NVLink (Beta)
author: NVIDIA
weight: 227
toc: 5
bookhidden: true
---
Follow these steps to set up and configure your VMs in a cluster of servers. First configure the VM on the master node, and then configure the VM on each additional node. NVIDIA recommends installing the virtual machines on different servers to increase redundancy in the event of a hardware failure.
{{<notice info>}}
This deployment type is currently in beta and will require a fresh installation upon subsequent NetQ releases.
{{</notice>}}
## System Requirements

This deployment model requires a cluster comprising a minimum of three nodes. Verify that *each node* in your cluster meets the VM requirements:

| Resource | Minimum Requirements |
| :--- | :--- |
| Processor | 48 virtual CPUs |
| Memory | 512GB RAM |
| Local disk storage | 3.2TB NVMe |
| Network interface speed | 10 Gbps NIC |
| Hypervisor | KVM/QCOW (QEMU Copy on Write) image for servers running Ubuntu 24.04;<br> VMware ESXi™ 6.5 or later (OVA image) for servers running Cumulus Linux or Ubuntu 24.04| 

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
|30008	|TCP|	gRPC OTLP receiver|
|30009	|TCP|	HTTPS OTLP receiver|
|31980	|TCP|	NetQ Agent communication|
|31982	|TCP|	NetQ Agent SSL communication|
|32710	|TCP|	API Gateway|

{{< expand "Internal communication ports" >}}


Additionally, for internal cluster communication, you must open these ports:

| Port or Protocol Number | Protocol | Component Access |
| --- | --- | --- |
|2181|	TCP|	Zookeeper client|
|2379|	TCP|	etcd|
|2380|	TCP|	etcd|
|2888|	TCP|	Zookeeper cluster communication|
|3888|	TCP|	Zookeeper cluster communication|
|5000|	TCP|	Docker registry|
|6443|	TCP|	Kubernetes API server|
|7000|	TCP|	Cassandra cluster communication|
|7071|	TCP|	Cassandra JMX monitoring|
|7072|	TCP|	Kafka JMX monitoring|
|7073|	TCP|	Zookeeper JMX monitoring|
|8080|	TCP|	Admin API|
|9042|	TCP|	Cassandra client|
|9092|	TCP|	Kafka client|
|10250|	TCP|	kubelet health probe|
|36443|	TCP|	Kubernetes control plane|

{{< /expand >}}

## Installation and Configuration

1. Download the NetQ image.

    a. Log in to your {{<exlink url="https://nvid.nvidia.com/" text="NVIDIA Application Hub">}} account.<br>
    b. Select **NVIDIA Licensing Portal**.<br>
    c. Select **Software Downloads** from the menu.<br>
    d. In the search field above the table, enter **NetQ**.<br>
    e. For deployments using KVM, download the **NetQ SW 5.1.0 KVM Scale** image. For deployments using VMware, download the **NetQ SW 5.1.0 VMware Scale** image<br>
    f. If prompted, read the license agreement and proceed with the download.<br>

{{%notice note%}}
NVIDIA employees can download NetQ directly from the {{<exlink url="http://ui.licensing.nvidia.com/" text="NVIDIA Licensing Portal">}}.
{{%/notice%}}

2. Open your hypervisor and configure your VM. You can use the following examples for reference or use your own hypervisor instructions.

 {{<netq-install/vm-setup hypervisor="kvm" deployment="onprem-scale-cluster" version="5.1">}}

 {{<netq-install/vm-setup hypervisor="vmware" version="5.1">}}

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
6. Open your hypervisor and set up the VM for the additional nodes in the same manner as for the master node.

7. Run the following command on each node to verify that the node is ready for a NetQ software installation. Fix any errors indicated before installing the software.

```
nvidia@hostname:~$ sudo opta-check-scale
```

8. Install and activate the NetQ software using the CLI.

Run the following command on your *master node* to initialize the cluster. Copy the output of the command which includes the SSH key. You will use it in the next step. 

```
nvidia@<hostname>:~$ netq install cluster master-init
    Please run the following command on all worker nodes:
    netq install cluster worker-init c3NoLXJzYSBBQUFBQjNOemFDMXljMkVBQUFBREFRQUJBQUFCQVFDM2NjTTZPdVM3dQN9MWTU1a
```
9. Run the `netq install cluster worker-init <ssh-key>` command on each non-master node.

10. Create a JSON template using the installation command for your deployment model. Run `netq install combined config generate` on your master node to generate a template for the cluster configuration JSON file. This command creates a template with three nodes by default. To change the number of nodes, specify the number in the command itself. For example, `netq install combined config generate nodes 6` creates a JSON template with fields for six nodes.

```
nvidia@netq-server:~$ netq install combined config generate
2025-10-28 17:29:53.260462: master-node-installer: Writing cluster installation configuration template file @ /tmp/combined-cluster-config.json
```

11. Edit the cluster configuration JSON file with the values for each attribute.

{{< tabs "Tab188 ">}}

{{< tab "Default JSON Template">}}

The `netq install combined config generate` command creates a JSON template for a three-node cluster.

```
nvidia@netq-server:~$ vim /tmp/combined-cluster-config.json
{
        "version": "v3.0",
        "interface": "<INPUT>",
        "cluster-vip": "<INPUT>",
        "master-ip": "<INPUT>",
        "is-ipv6": "<INPUT>",
        "ha-nodes": [
                {
                        "ip": "<INPUT>
                        "description": "Control Plane Node 1"
                },
                {
                        "ip": "<INPUT>"
                        "description": "Control Plane Node 2"
                }
                ],
        "shared-cluster-install": "<INPUT>"
        "storage-path": "/var/lib/longhorn"
        "alertmanager_webhook_url": "<INPUT>"

}
```

| Attribute | Description |
|----- | ----------- |
| `version` | The version of the JSON template. For NetQ 5.1, specify "v3.0". |
| `interface` | The local network interface on your master node used for NetQ connectivity. |
| `cluster-vip` | The cluster virtual IP address must be an unused IP address allocated from the same subnet assigned to the default interface for your server nodes. |
| `master-ip` | The IP address of the primary master node in your cluster. |
| `is-ipv6` | Set the value to `true` if your network connectivity and node address assignments are IPv6. Set the value to `false` for IPv4. |
| `ha-nodes`, `ip` | The IP addresses of the two high-availability control plane nodes in your cluster. |
| `shared-cluster-install` | Set the value to `true` if Kubernetes was already installed (for example, as part of a Base Command Manager deployment) or `false` to install Kubernetes. |
| `alertmanager_webhook_url` | Enter the URL of the Alertmanager webhook. You can add multiple URLs as a comma-separated list. Note that you must manually add this line to the JSON template to receive NVLink alerts. |

{{< /tab >}}
{{< tab "Completed JSON Example">}}

The following example uses the `netq install combined config generate nodes 6` command to create a JSON template for a six-node cluster.

``` 
nvidia@netq-server:~$ vim /tmp/combined-cluster-config.json 
{
        "version": "v3.0",
        "interface": "eth0",
        "cluster-vip": "10.176.235.101",
        "master-ip": "10.176.235.51",
        "is-ipv6": false,
        "ha-nodes": [
                {
                        "ip": "10.176.235.52"
                        "description": "Control Plane Node 1"
                },
                {
                        "ip": "10.176.235.53"
                        "description": "Control Plane Node 2"
                },
                ],
        "shared-cluster-install": false,
        "storage-path": "/var/lib/longhorn",
        "alertmanager_webhook_url": "",
        "worker-nodes": [
                {
                        "ip": "10.176.235.54",
                        "description": "Worker Node 1"
                },
                {
                        "ip": "10.176.235.55",
                        "description": "Worker Node 2"
                },
                {
                        "ip": "10.176.235.56",
                        "description": "Worker Node 3"
                }
        ]
}

```

| Attribute | Description |
|----- | ----------- |
| `version` | The version of the JSON template. For NetQ 5.1, specify "v3.0". |
| `interface` | The local network interface on your master node used for NetQ connectivity. |
| `cluster-vip` | The cluster virtual IP address must be an unused IP address allocated from the same subnet assigned to the default interface for your server nodes. |
| `master-ip` | The IP address of the primary master node in your cluster. |
| `is-ipv6` | Set the value to `true` if your network connectivity and node address assignments are IPv6. Set the value to `false` for IPv4. |
| `ha-nodes`, `ip` | The IP addresses of the two high-availability control plane nodes in your cluster. |
| `shared-cluster-install` | Set the value to `true` if Kubernetes was already installed (for example, as part of a Base Command Manager deployment) or `false` to install Kubernetes. |
| `alertmanager_webhook_url` | Enter the URL of the Alertmanager webhook. You can add multiple URLs as a comma-separated list. Note that you must manually add this line to the JSON template to receive NVLink alerts. |
| `worker-nodes`, `ip` | The IP addresses of the worker nodes in your cluster. |

{{< /tab >}}
{{< /tabs >}}

12.  Run the installation command on your master node using the JSON configuration file that you created in the previous step.

{{< tabs "TabID268">}}
{{< tab "New Install">}}

```
nvidia@<hostname>:~$ netq install cluster combined bundle /mnt/installables/NetQ-5.1.0.tgz /tmp/combined-cluster-config.json
```
<div class=“notices tip”><p>If this step fails for any reason, run <code>netq bootstrap reset</code> and then try again.</p></div>

{{< /tab >}}
{{< /tabs >}}


## Verify Installation Status

To view the status of the installation, use the `netq show status [verbose]` command. The following example shows a successful 3-node installation:

```
State: Active
    NetQ Live State: Active
    Installation Status: FINISHED
    Version: 5.1.0
    Installer Version: 5.1.0
    Installation Type: Cluster
    Installation Mode: Combined
    Activation Key: EhVuZXRxLWVuZHBvaW50LWdhdGV3YXkYsagDIixPSUJCOHBPWUFnWXI2dGlGY2hTRzExR2E5aSt6ZnpjOUvpVVTaDdpZEhFPQ==
    Master SSH Public Key: c3NoLXJzYSBBQUFBQjNOemFDMXljMkVBQUFBREFRQUJBQUFCZ1FDNW9iVXB6RkczNkRC
    Is Cloud: False
    
    Kubernetes Cluster Nodes Status:
    IP Address      Hostname       Role    NodeStatus    Virtual IP
    ------------    -----------    ------  ------------  ------------
    10.176.235.53   10.176.235.53  Worker  Ready         10.176.235.56
    10.176.235.52   10.176.235.52  Worker  Ready         10.176.235.55
    10.176.235.51   10.176.235.51  Master  Ready         10.176.235.54
    
    In Summary, Live state of the NetQ is... Active
```
Run the `netq show opta-health` command to verify that all applications are operating properly. Allow at least 15 minutes for all applications to come up and report their status.

{{%notice note%}}
If any of the applications or services display a DOWN status after 30 minutes, open a support ticket and attach the output of the `opta-support` command.
{{%/notice%}}

## Next Steps

After NetQ is installed, you can {{<link title="Access the NetQ UI" text="log in to NetQ">}} from your browser using the virtual cluster IP address. 

To access NVLink data, {{<link title="NVLink Bringup" text="perform a system bringup">}} to connect to telemetry and controller services.