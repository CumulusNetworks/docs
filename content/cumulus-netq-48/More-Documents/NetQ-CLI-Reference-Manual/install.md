---
title: install
author: NVIDIA
weight: 1104
toc: 3
right_toc_levels: 1
pdfhidden: true
type: nojsscroll
---

You can install NetQ with a single command or you can perform the individual steps using multiple commands. Generally, using the single command option is *strongly recommended*. However, the individual commands can be useful for troubleshooting the installation process when it fails.

You can use these commands only after bootstrapping the physical server or VM. Refer to {{<link title="bootstrap" text="netq bootstrap">}}.

<!--

{{<figure src="/images/netq/cliref-install-onprem-single-server-330.png" width="500" caption="On-premises single server">}}

{{<figure src="/images/netq/cliref-install-onprem-server-cluster-330.png" width="600" caption="On-premises server cluster">}}

{{<figure src="/images/netq/cliref-install-cloud-remote-330.png" width="250" caption="Cloud/remote">}}

-->

- - -

## netq install cluster activate-job

Activates a NetQ instance after an initial server cluster (master and two worker nodes) is configured and installed. Activation requires a configuration key that can be obtained from support.

Alternately, use {{<link title="#netq-install-cluster-full" text="netq install cluster full">}} to perform this and all other steps of a NetQ installation with a single command.

### Syntax

```
netq install cluster activate-job
    config-key <text-opta-key>
```

### Required Arguments

| Argument | Value | Description |
| ---- | ---- | ---- |
| activate-job | NA | Activate NetQ instance |
| config-key | \<text-opta-key\> | Use this unique key to activate NetQ |

### Options

None

### Sample Usage

```
cumulus@switch:~$ netq install cluster activate-job config-key ju8Kl4IhZ3cucHJvZDEubmV0cPk3vW11bHVzbmV0d29ya3MuY29cB3ag
```

### Related Commands

- ```netq install cluster join-workers```
- ```netq install cluster full```

- - -

## netq install cluster add-worker

Add additional nodes to your server cluster in an on-premises deployment.

### Syntax

```
netq install cluster 
    add-worker <text-worker-01>
```
### Required Arguments

| Argument | Value | Description |
| ---- | ---- | ---- |
| add-worker | \<text-worker-01\> | Install the worker nodes with these IP addresses |

### Options

None

### Related Commands

- `netq install opta cluster add-worker`

- - -
## netq install cluster full

Installs the NetQ Platform software on the servers in an on-premises, server cluster deployment. You must have the hostname or IP address of the master node and two worker nodes, and the NetQ software bundle to run the command.

Obtain the software release bundle from the {{<exlink url="https://nvid.nvidia.com/" text="NVIDIA Application Hub">}}.

### Syntax

```
netq install cluster full
    (interface <text-opta-ifname>|ip-addr <text-ip-addr> [<text-ipv6-addr>])
    bundle <text-bundle-url>
    [config-key <text-opta-key>]
    [pod-ip-range <text-pod-ip-range>]
    workers <text-worker-01> <text-worker-02>
    [workers-ipv6 <text-worker-ipv6-01> <text-worker-ipv6-02>] 
    [ipv6]
    [cluster-vip <text-cluster-vip>] 
    [s3-access-key <text-s3-access-key> s3-secret-key <text-s3-secret-key>]
```

### Required Arguments

| Argument | Value | Description |
| ---- | ---- | ---- |
| full | NA | Install a server cluster, running all initialization and configuration commands automatically |
| interface | \<text-opta-ifname\> | Install a server cluster with a master node using this interface to communicate with the NetQ Agents on the worker nodes |
| ip-addr | \<text-ip-addr\> | Install a server cluster with a master node with this IPv4 address to communicate with the NetQ Agents on the worker nodes |
| bundle | \<text-bundle-url\> | Install the NetQ software bundle at this location; you must specify a full path |
| workers | \<text-worker-01\> \<text-worker-02\> | Install the worker nodes with these IPv4 addresses |

### Options

| Option | Value | Description |
| ---- | ---- | ---- |
| NA | \<text-ipv6-addr\> | Install a server cluster with a master node with this IPv6 address to communicate with the NetQ Agents on the worker nodes |
| conifg-key | \<text-opta-key\> | Use this unique key to install the server cluster |
| pod-ip-range | \<text-pod-ip-range\> | Specify a range of IP addresses for the pod |
| workers-ipv6 | \<text-worker-ipv6-01\> \<text-worker-ipv6-02\> | Install the worker nodes with these IPv6 addresses |
| ipv6 | NA | Include this option for IPv6 installations |
| cluster-vip | \<text-vip\> | Specify a virtual IP address from the same subnet used for your master and worker nodes. |
| s3-access-key | \<text-s3-access-key\> | AWS S3 access key ID |
| s3-secret-key| \<text-s3-secret-key\>| AWS S3 secret key ID |


### Sample Usage

```
cumulus@<hostname>:~$ netq install cluster full interface eth0 bundle /mnt/installables/NetQ-4.8.0.tgz workers 10.20.10.25 10.20.10.45
```

### Related Commands

- `netq install cluster activate-job`
- `netq install cluster join-workers`

- - -
<!-- vale off -->
## netq install cluster join-workers
<!-- vale on -->

After initiating a NetQ installation, this command configures the first two worker nodes (NetQ on-premises appliances or VMs) in a server cluster deployment.

Alternately, use {{<link title="#netq-install-cluster-full" text="netq install cluster full">}} to perform this and all other steps of a NetQ installation with a single command.

### Syntax

```
netq install cluster join-workers
    <text-worker-01>
    [<text-worker-02>]
```

### Required Arguments

| Argument | Value | Description |
| ---- | ---- | ---- |
| join-workers | NA | Identify at least one worker node for the server cluster |
| NA | \<text-worker-node-01\> | IP address of server to configure as the first worker node in this server cluster |

### Options

| Option | Value | Description |
| ---- | ---- | ---- |
| NA | \<text-worker-node-02\> | IP address of server to configure as the second worker node in this server cluster |

### Sample Usage

```
cumulus@<hostname>:~$ netq install cluster join-workers 192.168.10.23 192.168.10.25
```

### Related Commands

- ```netq install cluster activate-job```
- ```netq install cluster full```

- - -
## netq install cluster master-init

After adding worker nodes to your cluster, run this command on your master node to initialize the cluster.

### Syntax

```
netq install cluster master-init
```
### Required Arguments

| Argument | Value | Description |
| ---- | ---- | ---- |
| master-init | NA | Initialize the cluster master node |

### Options

None

### Sample Usage

```
cumulus@<hostname>:~$ netq install cluster master-init
    Please run the following command on all worker nodes:
    netq install cluster worker-init c3NoLXJzYSBBQUFBQjNOemFDMXljMkVBQUFBREFRQUJBQUFCQVFDM2NjTTZPdVVUWWJ5c2Q3NlJ4SHdseHBsOHQ4N2VMRWVGR05LSWFWVnVNcy94OEE4RFNMQVhKOHVKRjVLUXBnVjdKM2lnMGJpL2hDMVhmSVVjU3l3ZmhvVDVZM3dQN1oySVZVT29ZTi8vR1lOek5nVlNocWZQMDNDRW0xNnNmSzVvUWRQTzQzRFhxQ3NjbndIT3dwZmhRYy9MWTU1a
```
### Related Commands

- `netq install cluster worker-init`

- - -

## netq install cluster worker-init

After initializing the cluster on the master node, run this command on each worker node.

### Syntax

```
netq install cluster worker-init 
    <text-ssh-key>
```
### Required Arguments

| Argument | Value | Description |
| ---- | ---- | ---- |
| worker-init| NA | Initialize cluster worker node |
| NA| \<text-ssh-key\> | Public SSH key |

### Options

None

### Related Commands

- `netq install cluster master-init`

- - -
<!-- vale off -->
## netq install opta activate-job

Activates the NetQ Collector software after you configure and install an initial server or server cluster (master and two worker nodes). Activation requires a configuration key that you can obtain from an email titled *A new site has been added to your NVIDIA NetQ account* (sent to your NetQ administrator).
<!-- vale on -->

### Syntax

```
netq install opta activate-job
    config-key <text-opta-key>
```

### Required Arguments

| Argument | Value | Description |
| ---- | ---- | ---- |
| activate-job | NA | Activate NetQ collector software |
| config-key | \<text-opta-key\> | Use this unique key to activate NetQ |

### Options

None

### Sample Usage

```
cumulus@switch:~$ netq install opta activate-job config-key ju8Kl4IhZ3cucHJvZDEubmV0cPk3vW11bHV9f3lk0d29ya3MuY29cB3ag
```

### Related Commands

- ```netq install opta cluster```
- ```netq install opta standalone```

- - -

## netq install opta cluster

Installs the NetQ Collector software on a master node and two worker nodes. For cloud deployments, it installs the software on the VM. For a multi-site on-premises deployment, it installs the software on one or two secondary servers at the external premises. You must have the hostname, IP address, or interface of the servers, the NetQ software bundle, and configuration key to run the command. You can also configure a proxy.

Obtain the software release bundle from the {{<exlink url="https://nvid.nvidia.com/" text="NVIDIA Application Hub">}}.

Obtain the config-key as follows:

<!-- vale off -->
- Cloud: Locate and retrieve key from email titled *A new site has been added to your NVIDIA NetQ account* (sent to your NetQ administrator)
- Remote: Follow the instructions in {{<link title="Configure Premises" text="Configure Multiple Premises">}}
<!-- vale on -->

### Syntax

```
netq install opta cluster full
    (interface <text-opta-ifname>|ip-addr <text-ip-addr>)
    bundle <text-bundle-url>
    config-key <text-opta-key>
    [pod-ip-range <text-pod-ip-range>]
    workers <text-worker-01> <text-worker-02>
    [proxy-host <text-proxy-host> proxy-port <text-proxy-port>]
```

### Required Arguments

| Argument | Value | Description |
| ---- | ---- | ---- |
| full | NA | Install a server with NetQ Collector software, running all initialization and configuration commands automatically |
| interface | \<text-opta-ifname\> | Install a server cluster with a master node using this interface to communicate with the NetQ Agents on the worker nodes |
| ip-addr | \<text-ip-addr\> | Install a server cluster with a master node with this IP address to communicate with the NetQ Agents on the worker nodes |
| bundle | \<text-bundle-url\> | Install the NetQ software bundle at this location; you must specify a full path |
| workers | \<text-worker-01\> \<text-worker-02\> | Install the worker nodes with these IP addresses |
| conifg-key | \<text-opta-key\> | Use this unique key to activate the software |

### Options

| Option | Value | Description |
| ---- | ---- | ---- |
| proxy-host | \<text-proxy-host\> | Use the proxy server with this hostname or IP address instead of directly connecting to the VM; you must also specify a port |
| proxy-port | \<text-proxy-port\> | Use this port on the proxy server instead of directly connecting to the VM; you must also specify a proxy host |
| pod-ip-range | \<text-pod-ip-range\> | Specify a range of IP addresses for the pod |

### Sample Usage

<!-- Add output/results -->
```
cumulus@<hostname>:~$ netq install opta cluster full interface en01 bundle /mnt/installables/NetQ-4.0.0.tgz config-key CI39fo5CZ3cucHJvZDEubmV0cS5jdW11bHVzbmVp6z8ma3MuY29tGLsD workers 10.20.10.25 10.20.10.45
```

### Related Commands

- ```netq install opta activate-job```

- - -

## install opta cluster add-worker

Add additional nodes to your server cluster in a cloud deployment.

### Syntax

```
 netq install opta cluster 
    add-worker <text-worker-01>
 ```
### Required Arguments

| Argument | Value | Description |
| ---- | ---- | ---- |
| add-worker | \<text-worker-01\> | Install the worker nodes with these IP addresses |

### Options

None

### Related Commands

- `netq install cluster add-worker`

- - -
## netq install opta standalone

Installs the NetQ Collector software on a single cloud server (VM) with a single command. You must have the hostname, IP address, or interface of the server, the NetQ software bundle, and configuration key to run the command. You can also configure a proxy.

Obtain the software release bundle from the {{<exlink url="https://nvid.nvidia.com/" text="NVIDIA Application Hub">}}.

<!-- vale off -->
Obtain the config-key from the email sent to your NetQ administrator titled *A new site has been added to your NVIDIA NetQ account*.
<!-- vale on -->

### Syntax

```
netq install opta standalone full
    (interface <text-opta-ifname>|ip-addr <text-ip-addr>)
    bundle <text-bundle-url>
    config-key <text-opta-key>
    [pod-ip-range <text-pod-ip-range>]
    [proxy-host <text-proxy-host> proxy-port<text-proxy-port>]
    [s3-access-key <text-s3-access-key> s3-secret-key <text-s3-secret-key>]
```

### Required Arguments

| Argument | Value | Description |
| ---- | ---- | ---- |
| full | NA | Install a server with NetQ Collector software, running all initialization and configuration commands automatically |
| interface | \<text-opta-ifname\> | Install NetQ on the server with this interface as the communication interface for the NetQ Agents on the monitored switches and hosts |
| ip-addr | \<text-ip-addr\> | Install NetQ on the server with this IP address to communicate with the NetQ Agents on the monitored switches and hosts |
| bundle | \<text-bundle-url\> | Install the NetQ software bundle at this location; you must specify a full path |
| conifg-key | \<text-opta-key\> | Use this unique key to activate the software |

### Options

| Option | Value | Description |
| ---- | ---- | ---- |
| proxy-host | \<text-proxy-host\> | Use the proxy server with this hostname or IP address instead of directly connecting to the VM; you must also specify a port |
| proxy-port | \<text-proxy-port\> | Use this port on the proxy server instead of directly connecting to the VM; you must also specify a proxy host |
| pod-ip-range | \<text-pod-ip-range\> | Specify a range of IP addresses for the pod |
| s3-access-key | \<text-s3-access-key\> | AWS S3 access key ID |
| s3-secret-key| \<text-s3-secret-key\>| AWS S3 secret key ID |

### Sample Usage

```
cumulus@<hostname>:~$ netq install opta standalone full interface en01 bundle /mnt/installables/NetQ-4.0.0.tgz config-key CI39fo5CZ3cucHJvZDEubmV0cS5jdW11bHVzbmVp6z8ma3MuY29tGLsD
```

### Related Commands

- ```netq install opta activate-job```

- - -

## netq install patch

Installs a focused software fix using a compressed file package (rather than a full installation or upgrade). Run this command on the NetQ appliance or VM as appropriate.

### Syntax

```
netq install patch
    <text-tarball-name>
```

### Required Arguments

| Argument | Value | Description |
| ---- | ---- | ---- |
| NA | \<text-tarball-name\> | Install the software patch contained in the tarball at this location; you must specify a full path |

### Options

None

### Sample Usage

```
cumulus@<hostname>:~$ netq install patch /mnt/installables/NetQ-4.0.0-patch.tgz
```

### Related Commands

- ```netq upgrade```

- - -

<!-- vale off -->
## netq install standalone activate-job
<!-- vale on -->

Activates a NetQ instance after you install the software. Activation requires a configuration key that you can obtain from support.

Alternately, use {{<link title="#netq-install-standalone-full" text="netq install standalone full">}} to perform this and all other steps of a NetQ installation with a single command.

### Syntax

```
netq install standalone activate-job
    config-key <text-opta-key>
```

### Required Arguments

| Argument | Value | Description |
| ---- | ---- | ---- |
| activate-job | NA | Activate NetQ instance |
| config-key | \<text-opta-key\> | Use this unique key to activate NetQ |

### Options

None

### Sample Usage

<!-- Add output/results -->
```
cumulus@switch:~$ netq install standalone activate-job config-key ju8Kl4IhZ3cucHJvZDEubmV0cPk3vW11bHVzbmV0d29ya3MuY29cB3ag
```

### Related Commands

- ```netq install standalone full```

- - -

## netq install standalone full

Installs the NetQ Platform software on the NetQ On-premises Appliance or VM in an on-premises, single server deployment, all with a single command. You must have the hostname or IP address of the server, and the NetQ software bundle to run the command. A configuration key is optional.

Obtain the software release bundle from the {{<exlink url="https://nvid.nvidia.com/" text="NVIDIA Application Hub">}}.

### Syntax

```
netq install standalone full 
    (interface <text-opta-ifname>|ip-addr <text-ip-addr> [<text-ipv6-addr>]) 
    bundle <text-bundle-url> 
    [ipv6] 
    [config-key <text-opta-key>]
    [pod-ip-range <text-pod-ip-range>]
    [s3-access-key <text-s3-access-key> s3-secret-key <text-s3-secret-key>]
```
### Required Arguments

| Argument | Value | Description |
| ---- | ---- | ---- |
| full | NA | Install a server with NetQ software, running all initialization and configuration commands automatically |
| interface | \<text-opta-ifname\> | Install NetQ on the server with this interface as the communication interface for the NetQ Agents on the monitored switches and hosts |
| ip-addr | \<text-ip-addr\>,\<text-ipv6-addr\>  | Install NetQ on the server with this IPv4 or IPv6 address to communicate with the NetQ Agents on the monitored switches and hosts |
| bundle | \<text-bundle-url\> | Install the NetQ software bundle at this location; you must specify a full path |

### Options

| Option | Value | Description |
| ---- | ---- | ---- |
| ipv6 | NA | Install NetQ using an IPv6 address |
| conifg-key | \<text-opta-key\> | Use this unique key to activate the software |
| pod-ip-range | \<text-pod-ip-range\> | Specify a range of IP addresses for the pod |
| s3-access-key | \<text-s3-access-key\> | AWS S3 access key ID |
| s3-secret-key| \<text-s3-secret-key\>| AWS S3 secret key ID |

### Sample Usage

```
cumulus@<hostname>:~$ netq install standalone full interface eth0 bundle /mnt/installables/NetQ-4.7.0.tgz
```

### Related Commands

- `netq install standalone activate-job`

- - -
## netq install update-opta-ssl-setting

Replace or update the TSL/SSL settings on OPTA for agent-OPTA connection.

### Syntax

```
netq install update-opta-ssl-setting 
    ssl-cert <text-ssl-cert-file> 
    ssl-key <text-ssl-key-file>
```
### Required Arguments

| Argument | Value | Description |
| ---- | ---- | ---- |
| update-opta-ssl-setting | NA | Update the TLS/SSL settings on OPTA for agent-opta connection |
| ssl-cert | \<text-ssl-cert-filel\> | TLS/SSL certificate file absolute path |
| ssl-key | \<text-ssl-key-filel\> | TLS/SSL private key file absolute path |

### Options

None

### Related Commands

None

- - -

## netq install update-settings


Overrides system variables after encountering issues during installation. File a {{<exlink url="https://enterprise-support.nvidia.com/" text="support ticket">}} with the NVIDIA Enterprise Support team before using this command. They can provide the key/value pair needed to resolve your issue.

### Syntax

```
netq install update-settings
    <text-key>
    <text-value>
```

### Required Arguments

| Argument | Value | Description |
| ---- | ---- | ---- |
| NA | \<text-key\> | Update the environment variable with this name |
| NA | \<text-value\> | Update the specified environment variable with this value |

### Options

None

### Sample Usage

Change timeout for tasks

```
cumulus@<hostname>:~$ netq install update-settings DEFAULT_TASK_TIMEOUT_IN_MILLIS 3000000
```

### Related Commands

None
