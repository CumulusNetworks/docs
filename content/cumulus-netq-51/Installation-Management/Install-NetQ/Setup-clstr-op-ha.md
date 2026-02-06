---
title: Set Up Your Virtual Machine for an On-premises HA Server Cluster
author: NVIDIA
weight: 227
toc: 5
bookhidden: true
---
Follow these steps to set up and configure your VM on a cluster of servers in an on-premises deployment. First configure the VM on the master node, and then configure the VM on *each* worker node. NVIDIA recommends installing the virtual machines on different physical servers to increase redundancy in the event of a hardware failure. 

- - -

## System Requirements

Verify that each node in your cluster---the master node and two worker nodes---meets the VM requirements.

| Resource | Minimum Requirements |
| :--- | :--- |
| Processor | 16 virtual CPUs |
| Memory | 64 GB RAM |
| Local disk storage | 500 GB SSD with minimum disk IOPS of 1000 for a standard 4kb block size<br> (Note: This must be an SSD; other storage options can lead to system instability and are not supported.)|
| Network interface speed | 1 Gb NIC |
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
|30008	|TCP|	gRPC OTLP export |
|30009	|TCP|	HTTPS OTLP export|
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
|54321|	TCP|	OPTA communication|

{{< /expand >}}


## Installation and Configuration

1. Download the NetQ image.

    a. Log in to your {{<exlink url="https://nvid.nvidia.com/" text="NVIDIA Application Hub">}} account.<br>
    b. Select **NVIDIA Licensing Portal**.<br>
    c. Select **Software Downloads** from the menu.<br>
    d. In the search field above the table, enter **NetQ**.<br>
    e. For deployments using KVM, download the **NetQ SW 5.1.0 KVM** image. For deployments using VMware, download the **NetQ SW 5.1.0 VMware** image<br>
    f. If prompted, read the license agreement and proceed with the download.<br>

{{%notice note%}}
NVIDIA employees can download NetQ directly from the {{<exlink url="http://ui.licensing.nvidia.com/" text="NVIDIA Licensing Portal">}}.
{{%/notice%}}

2. Open your hypervisor and configure your VM. You can use the following examples for reference or use your own hypervisor instructions.

{{<netq-install/vm-setup hypervisor="kvm" deployment="onprem" version="5.1">}}
{{<netq-install/vm-setup hypervisor="vmware" deployment="onprem" version="5.1">}}

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
nvidia@hostname:~$ sudo opta-check
```

5. Change the hostname for the VM from the default value.

The default hostname for the NetQ virtual machines is *ubuntu*. Change the hostname to fit your naming conventions while meeting Internet and Kubernetes naming standards.

{{<notice tip>}}
Kubernetes requires hostnames to be composed of a sequence of labels concatenated with dots. For example, “en.wikipedia.org” is a hostname. Each label must be from 1 to 63 characters long. The entire hostname, including the delimiting dots, has a maximum of 253 ASCII characters.<br>
<br>
The Internet standards (RFCs) for protocols specify that labels may contain only the ASCII letters a through z (in lower case), the digits 0 through 9, and the hyphen-minus character ('-').
{{</notice>}}

Use the following command:

```
nvidia@hostname:~$ sudo hostnamectl set-hostname NEW_HOSTNAME
```

6. Open your hypervisor and set up the VM in the same manner as for the master node.

    {{<notice note>}}
Make a note of the private IP address you assign to the worker node. You will need it to complete the installation.
    {{</notice>}}

7. Verify that the worker node is ready for installation. Fix any errors indicated before installing the NetQ software.

<!--double check this command-->
```
nvidia@hostname:~$ sudo opta-check
```

8. Repeat steps 6 and 7 for each additional worker node in your cluster.

9. Install and activate the NetQ software using the CLI.

Run the following command on your *master* node to initialize the cluster. Copy the output of the command to use on your worker nodes:

```
nvidia@<hostname>:~$ netq install cluster master-init
    Please run the following command on all worker nodes:
    netq install cluster worker-init c3NoLXJzYSBBQUFBQjNOemFDMXljMkVBQUFBREFRQUJBQUFCQVFDM2NjTTZPdVM3dQN9MWTU1a
```
10. Run the `netq install cluster worker-init <ssh-key>` command on each of your worker nodes.

11. Run the installation command on your NetQ server. Follow the steps under _Restore Data and New Install_ if you have a {{<link title="Back Up and Restore NetQ" text="backup data tarball">}} from a previous NetQ installation to restore.

{{< tabs "TabID41 ">}}
{{< tab "New Install">}}

Run the following commands on your master node, using the IP addresses of your worker nodes and the HA cluster virtual IP address (VIP):

{{<notice info>}}
The HA cluster virtual IP must be:
    <li>An unused IP address allocated from the same subnet assigned to the default interface for your master and worker nodes. The default interface is the interface used in the <code>netq install</code> <a href="https://docs.nvidia.com/networking-ethernet-software/cumulus-netq/More-Documents/NetQ-CLI-Reference-Manual/install/#netq-install-cluster-full">command</a>.</li>
    <li>A different IP address than the primary IP assigned to the default interface.</li>
{{</notice>}}

```
nvidia@<hostname>:~$ netq install cluster full interface eth0 bundle /mnt/installables/NetQ-5.1.0.tgz workers <worker-1-ip> <worker-2-ip> cluster-vip <vip-ip>
```
<div class="notices note"><p></p><p>NetQ uses the 10.244.0.0/16 (<code>pod-ip-range</code>) and 10.96.0.0/16 (<code>service-ip-range</code>) networks for internal communication by default. If you are using these networks, you must override each range by specifying new subnets for these parameters in the install command:</p>
    <pre><div class=“copy-code-img”></div>nvidia@hostname:~$ netq install cluster full interface eth0 bundle /mnt/installables/NetQ-5.1.0.tgz pod-ip-range &lt;pod-ip-range&gt; service-ip-range &lt;service-ip-range&gt; workers &lt;worker-1-ip&gt; &lt;worker-2-ip&gt;&nbsp;&nbsp;</pre><p>You can specify the IP address of the server instead of the interface name using the <code>ip-addr &lt;ip-address&gt;</code> argument:</p>
    <pre><div class="copy-code-img"></div>nvidia@hostname:~$ netq install cluster full ip-addr &lt;ip-address&gt; bundle /mnt/installables/NetQ-5.1.0.tgz workers &lt;worker-1-ip&gt; &lt;worker-2-ip&gt;</pre><p>If you change the server IP address or hostname after installing NetQ, you must reset the server with the <code>netq bootstrap reset keep-db</code> command and rerun the install command.</p>
    <p></p></div>

<div class="notices tip"><p>If this step fails for any reason, run <code>netq bootstrap reset</code> and then try again.</p></div>

{{< /tab >}}
{{< tab "Restore Data and New Install">}}

Restore your data with the backup file you created during a backup using the `restore` option with the `netq install` command. The `restore` option copies the data from the backup file to the database, decompresses it, verifies the restoration, and starts all necessary services. 

Run the installation command on your master node, using the IP addresses of your worker nodes, the HA cluster virtual IP address (VIP), and referencing the path where the backup file resides.

{{<notice info>}}
The HA cluster virtual IP must be:
    <li>An unused IP address allocated from the same subnet assigned to the default interface for your master and worker nodes. The default interface is the interface used in the <code>netq install</code> <a href="https://docs.nvidia.com/networking-ethernet-software/cumulus-netq/More-Documents/NetQ-CLI-Reference-Manual/install/#netq-install-cluster-full">command</a>.</li>
    <li>A different IP address than the primary IP assigned to the default interface.</li>
{{</notice>}}

```
nvidia@netq-server:~$ netq install cluster full interface eth0 bundle /mnt/installables/NetQ-5.1.0.tgz workers 10.188.44.219 10.188.45.164 cluster-vip 10.188.45.169 restore /home/nvidia/combined_backup_20241211111316.tar
```

<div class="notices note"><p></p><p>NetQ uses the 10.244.0.0/16 (<code>pod-ip-range</code>) and 10.96.0.0/16 (<code>service-ip-range</code>) networks for internal communication by default. If you are using these networks, you must override each range by specifying new subnets for these parameters in the install command:</p>
    <pre><div class="copy-code-img"></div>nvidia@hostname:~$ netq install cluster full interface eth0 bundle /mnt/installables/NetQ-5.1.0.tgz workers &lt;worker-1-ip&gt; &lt;worker-2-ip&gt; pod-ip-range &lt;pod-ip-range&gt; service-ip-range &lt;service-ip-range&gt; restore /home/nvidia/combined_backup_20241211111316.tar</pre><p>You can specify the IP address of the server instead of the interface name using the <code>ip-addr &lt;ip-address&gt;</code> argument:</p>
    <pre><div class="copy-code-img"></div>nvidia@hostname:~$ netq install cluster full ip-addr &lt;ip-address&gt; bundle /mnt/installables/NetQ-5.1.0.tgz workers &lt;worker-1-ip&gt; &lt;worker-2-ip&gt; restore /home/nvidia/combined_backup_20241211111316.tar</pre><p>If you change the server IP address or hostname after installing NetQ, you must reset the server with the <code>netq bootstrap reset keep-db</code> command and rerun the install command.</p>
    <p></p></div>

<div class="notices tip"><p><ul><li>If this step fails for any reason, run <code>netq bootstrap reset</code> and then try again.</li><li>If you restore NetQ data to a server with an IP address that is different from the one used to back up the data, you must <a href="https://docs.nvidia.com/networking-ethernet-software/cumulus-netq/Installation-Management/Install-NetQ/Install-NetQ-Agents/#configure-netq-agents">reconfigure the agents</a> on each switch as a final step.</li></ul></p></div>
{{< /tab >}}
{{< /tabs >}}


## Verify Installation Status

To view the status of the installation, use the `netq show status [verbose]` command. The following example shows a successful on-premises installation:

```
State: Active
    NetQ Live State: Active
    Installation Status: FINISHED
    Version: 5.1.0
    Installer Version: 5.1.0
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

{{%notice note%}}
If any of the applications or services display a DOWN status after 30 minutes, open a support ticket and attach the output of the `opta-support` command.
{{%/notice%}}
After NetQ is installed, you can {{<link title="Access the NetQ UI" text="log in to NetQ">}} from your browser.
