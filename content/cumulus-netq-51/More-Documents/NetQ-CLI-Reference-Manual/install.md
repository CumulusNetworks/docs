---
title: install
author: NVIDIA
weight: 1104
toc: 3
right_toc_levels: 1
pdfhidden: true
type: nojsscroll
---

Refer to the {{<link title="Install the NetQ System" text="installation page for your deployment model">}} for step-by-step instructions.

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
nvidia@switch:~$ netq install cluster activate-job config-key ju8Kl4IhZ3cucHJvZDEubmV0cPk3vW11bHVzbmV0d29ya3MuY29cB3ag
```

### Related Commands

- ```netq install cluster full```

- - -
<!-- not supported for 4.9
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

None

- - -

-->
## netq install cluster bundle

Installs the NetQ software for an on-premises HA scale cluster deployment. Run this command on your *master* node, specifying the cluster configuration JSON file you created with the `netq install cluster config generate` command.

### Syntax

```
netq install cluster bundle
    <text-bundle-url>
    <text-cluster-config>
    [restore <text-backup-file>]
```

### Required Arguments

| Argument | Value | Description |
| ---- | ---- | ---- |
| bundle | \<text-bundle-url\> | Install the NetQ software bundle at this location; you must specify a full path |
| NA | \<text-cluster-config\> | Specify the cluster configuration JSON file  |

### Options

| Option | Value | Description |
| ---- | ---- | ---- |
| restore | \<text-backup-file\> | |

### Sample Usage

```
nvidia@<hostname>:~$ netq install cluster bundle /mnt/installables/NetQ-5.1.0.tgz /tmp/cluster-install-config.json restore /home/nvidia/combined_backup_20241211111316.tar
```

### Related Commands

- `netq install cluster config generate`
- - -
## netq install cluster combined bundle

Installs the NetQ software for an on-premises HA scale cluster deployment in Ethernet + NVLink combined mode.

### Syntax

```
netq install cluster combined bundle <text-bundle-url> <text-cluster-config> 
    [ignore-pre-checks] 
    [restore <text-backup-file>] 
    [validate-only]
```
### Required Arguments

| Argument | Value | Description |
| ---- | ---- | ---- |
| bundle | \<text-bundle-url\> | Install the NetQ software bundle at this location; you must specify a full path |
| NA | \<text-cluster-config\> | Installs NetQ per the JSON configuration file parameters that were specified using the `netq install combined config generate` command. |

### Options

| Option | Value | Description |
| ---- | ---- | ---- |
| ignore-pre-checks | N/A | Ignores the pre-check process that ensures the installation will complete successfully (not recommended)|
| restore | \<text-backup-file\> | Specify the path where the backup .tar file resides |
| validate-only | NA | Runs the pre-checks, but does not proceed with the installation |

### Sample Usage

```
nvidia@<hostname>:~$ netq install cluster combined bundle /mnt/installables/NetQ-5.1.0.tgz /tmp/combined-cluster-config.json
```
- - -
## netq install cluster config generate

Run this command on your *master* node to generate a JSON template that you can use to specify your VM's cluster configuration attributes as part of the high-availability scale cluster deployment.

### Syntax

```
netq install cluster config generate 
    [<text-config-json-file>]
```
### Required Arguments

None

### Options

| Option | Value | Description |
| ---- | ---- | ---- |
| NA | \<text-config-json-file\> | Generate the file at this location; you must specify a full path |

### Sample Usage

```
nvidia@netq-server:~$ netq install cluster config generate
2024-10-28 17:29:53.260462: master-node-installer: Writing cluster installation configuration template file @ /tmp/cluster-install-config.json
```

### Related Commands

- `netq install cluster bundle`

- - -

## netq install cluster config generate workers

For a 5-node scale cluster, run this command on your master node to generate a cluster configuration JSON file with 2 additional `worker-nodes` objects.

### Syntax

```
netq install cluster config generate workers
    <text-cluster-nworkers> 
    [<text-config-json-file>]
```
### Required Arguments

| Argument | Value | Description |
| ---- | ---- | ---- |
| workers | \<text-cluster-nworkers\> | Adds *n* number of `worker-nodes` objects. For 5-node clusters, this value should be 2.|

### Options

| Option | Value | Description |
| ---- | ---- | ---- |
| NA | \<text-config-json-file\> | Generate the file at this location; you must specify a full path |

### Sample Usage

```
nvidia@netq-server:~$ netq install cluster config generate workers 2
2024-10-28 17:29:53.260462: master-node-installer: Writing cluster installation configuration template file @ /tmp/cluster-install-config.json
```
### Related Commands

- `netq install cluster bundle`

- - -
## netq install cluster full

Installs the NetQ software for an on-premises, server cluster deployment. Run this command on your *master* node. You must have the hostname or IP address of the master node, two worker nodes, virtual IP address, and the NetQ software bundle to run the command.

Obtain the software release bundle from the {{<exlink url="https://nvid.nvidia.com/" text="NVIDIA Application Hub">}}.

### Syntax

```
netq install cluster full
    (interface <text-opta-ifname>|ip-addr <text-ip-addr> [<text-ipv6-addr>])
    bundle <text-bundle-url>
    [config-key <text-opta-key>]
    [pod-ip-range <text-pod-ip-range>]
    [service-ip-range <text-service-ip-range>]
    workers <text-worker-01> <text-worker-02>
    [workers-ipv6 <text-worker-ipv6-01> <text-worker-ipv6-02>] 
    cluster-vip <text-cluster-vip> 
    [ipv6]
    [s3-access-key <text-s3-access-key> s3-secret-key <text-s3-secret-key>]
    [restore <text-backup-file>]
```

### Required Arguments

| Argument | Value | Description |
| ---- | ---- | ---- |
| interface | \<text-opta-ifname\> | Install a server cluster with a master node using this interface to communicate with the NetQ agents on the worker nodes |
| ip-addr | \<text-ip-addr\>,\<text-ipv6-addr\>  | Install a server cluster with a master node with this IPv4 or IPv6 address to communicate with the NetQ agents on the worker nodes |
| bundle | \<text-bundle-url\> | Install the NetQ software bundle at this location; you must specify a full path |
| workers | \<text-worker-01\> \<text-worker-02\> | Install the worker nodes with these IPv4 addresses |
| cluster-vip | \<text-cluster-vip\> | Specify a virtual IP address from the same subnet used for your master and worker nodes |

### Options

| Option | Value | Description |
| ---- | ---- | ---- |
| config-key | \<text-opta-key\> | Use this unique key to install the server cluster |
| pod-ip-range | \<text-pod-ip-range\> | Specify a range of IP addresses for the pod |
| service-ip-range | \<text-service-ip-range\> | Specify a range of IP addresses for the service |
| workers-ipv6 | \<text-worker-ipv6-01\> \<text-worker-ipv6-02\> | Install the worker nodes with these IPv6 addresses |
| s3-access-key | \<text-s3-access-key\> | AWS S3 access key ID |
| s3-secret-key| \<text-s3-secret-key\>| AWS S3 secret key ID |
| restore | \<text-backup-file\> | Specify the path where the backup .tar file resides |

### Sample Usage

```
nvidia@<hostname>:~$ netq install cluster full interface eth0 bundle /mnt/installables/NetQ-5.1.0.tgz workers 10.20.10.25 10.20.10.45 cluster-vip 10.20.10.254
```

### Related Commands

- `netq install cluster activate-job`

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
nvidia@<hostname>:~$ netq install cluster master-init
    Please run the following command on all worker nodes:
    netq install cluster worker-init c3NoLXJzYSBBQUFBQjNOemFDMXljMkVBQUFBREFRQUJBQUFCQVFDM2NjTTZPdVVUWWJ5c2Q3NlJ4SHdseHBsOHQ4N2VMRWVGR05LSWFWVnVNcy94OEE4RFNMQVhKOHVKRjVLUXBnVjdKM2lnMGJpL2hDMVhmSVVjU3l3ZmhvVDVZM3dQN1oySVZVT29ZTi8vR1lOek5nVlNocWZQMDNDRW0xNnNmSzVvUWRQTzQzRFhxQ3NjbndIT3dwZmhRYy9MWTU1a
```
### Related Commands

- `netq install cluster worker-init`

- - -
## netq install cluster worker add

Adds additional worker nodes to an existing HA scale cluster. Use this command to generate a JSON configuration template referencing the number of additional worker nodes you want to add. See the {{<link title="Set Up Your Virtual Machine for an On-premises HA Scale Cluster/#add-additional-worker-nodes" text="scale cluster deployment guide">}} for more information.

### Syntax

```
netq install cluster worker add <text-cluster-config>
    [restore <text-backup-file>]
```
### Required Arguments

| Argument | Value | Description |
| ---- | ---- | ---- |
| NA | \<text-cluster-config\> | Specify the cluster configuration JSON file |

### Options

| Option | Value | Description |
| ---- | ---- | ---- |
| restore | \<text-backup-file\> | Specify the path where the backup .tar file resides |

### Related Commands

- `netq install cluster config generate`

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
## netq install combined config generate

Creates the JSON configuration template for the NetQ for Ethernet and NVLink combined mode in an HA scale cluster environment. Several versions of this command are available depending on how many nodes are in your deployment.

### Syntax

The default `netq install combined config generate` command creates a JSON configuration template for a three-node cluster. If your deployment model uses more than three nodes, specify the number using the `nodes` argument.
<!--asking shyamala what this does
netq install combined config generate workers <text-num-nodes> 
    [<text-config-json-file>]
-->
```
netq install combined config generate 
    [<text-config-json-file>]

netq install combined config generate nodes <text-num-nodes>  
    [<text-config-json-file>] 
```

### Required Arguments

| Argument | Value | Description |
| ---- | ---- | ---- |
| nodes| \<text-num-nodes\> | Specify the number of worker node objects in the JSON configuration template |

### Options

| Option | Value | Description |
| ---- | ---- | ---- |
| NA | \<text-num-nodes\> | Specify the full path for the JSON configuration file template |

### Related Commands

- `netq install cluster combined bundle`

- - -

## netq install nvl bundle

Installs {{<link title="Install NetQ NVLink" text="NetQ NVLink">}} using the JSON configuration file generated by the `netq install nvl config generate` command.

### Syntax

```
netq install nvl bundle <text-bundle-url> 
    kong-rw-password <text-kong-rw-password> 
    kong-ro-password <text-kong-ro-password> 
    <text-cluster-config>
    [ignore-pre-checks]
```

### Required Arguments

| Argument | Value | Description |
| ---- | ---- | ---- |
| bundle | \<text-bundle-url\> | Specify the full path to the NetQ tarball |
| kong-rw-password | \<text-kong-rw-password\> | Sets the Kong read-write password (8 character minimum)|
| kong-ro-password | \<text-kong-ro-password\> | Sets the Kong read-only password (8 character minimum) |
| NA| \<text-cluster-config\> | Specify the full path to the JSON configuration file |

### Options

| Option | Value | Description |
| ---- | ---- | ---- |
| ignore-pre-checks | NA | Skips pre-checks (not recommended)|

### Related Commands

- `netq install nvl config generate`

- - -

## netq install nvl config

Generates a JSON template with placeholder values. You will use this file to install NetQ NVLink using the `netq install nvl bundle` command.

### Syntax

```
netq install nvl config generate [<text-config-json-file>]
```

### Required Arguments

None

### Options

| Option | Value | Description |
| ---- | ---- | ---- |
| NA | \<text-config-json-file\>  | Specify the path where the JSON template is generated. If left unspecified, the template is located at `/tmp/nvl-cluster-config.json` |

### Related Commands

- `netq install nvl bundle`

- - -

<!-- vale off -->
## netq install opta activate-job

Activates the NetQ software after you configure and install an initial server or server cluster. Activation requires a configuration key that you can obtain from an email titled *A new site has been added to your NVIDIA NetQ account* (sent to your NetQ administrator).
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
nvidia@switch:~$ netq install opta activate-job config-key ju8Kl4IhZ3cucHJvZDEubmV0cPk3vW11bHV9f3lk0d29ya3MuY29cB3ag
```

### Related Commands

- ```netq install opta standalone```

- - -

## netq install opta standalone full

Installs the NetQ software on a single cloud server (VM). You must have the hostname, IP address (or interface of the server), the NetQ software bundle, and configuration key to run the command. You can also configure a proxy.

Obtain the software release bundle from the {{<exlink url="https://nvid.nvidia.com/" text="NVIDIA Application Hub">}}.

Obtain the config-key from the email sent to your NetQ administrator titled *A new site has been added to your NVIDIA NetQ account*. You can also obtain the configuration key through the NetQ UI in the {{<link title="Configure Premises" text="premises management configuration">}}.

### Syntax

```
netq install opta standalone full
    (interface <text-opta-ifname>|ip-addr <text-ip-addr>)
    bundle <text-bundle-url>
    config-key <text-opta-key>
    [pod-ip-range <text-pod-ip-range>]
    [service-ip-range <text-service-ip-range>]
    [proxy-host <text-proxy-host> proxy-port<text-proxy-port>]
    [s3-access-key <text-s3-access-key> s3-secret-key <text-s3-secret-key>]
    [restore <text-backup-file>]
```

### Required Arguments

| Argument | Value | Description |
| ---- | ---- | ---- |
| interface | \<text-opta-ifname\> | Install NetQ on the server with this interface as the communication interface for the NetQ agents on the monitored switches and hosts |
| ip-addr | \<text-ip-addr\> | Install NetQ on the server with this IP address to communicate with the NetQ agents on the monitored switches and hosts |
| bundle | \<text-bundle-url\> | Install the NetQ software bundle at this location; you must specify a full path |
| config-key | \<text-opta-key\> | Use this unique key to activate the software |

### Options

| Option | Value | Description |
| ---- | ---- | ---- |
| pod-ip-range | \<text-pod-ip-range\> | Specify a range of IP addresses for the pod |
| service-ip-range | \<text-service-ip-range\> | Specify a range of IP addresses for the service |
| proxy-host | \<text-proxy-host\> | Use the proxy server with this hostname or IP address instead of directly connecting to the VM; you must also specify a port |
| proxy-port | \<text-proxy-port\> | Use this port on the proxy server instead of directly connecting to the VM; you must also specify a proxy host |
| s3-access-key | \<text-s3-access-key\> | AWS S3 access key ID |
| s3-secret-key| \<text-s3-secret-key\>| AWS S3 secret key ID |
| restore | \<text-backup-file\> | Specify the path where the backup .tar file resides |


### Sample Usage

```
nvidia@<hostname>:~$ netq install opta standalone full interface en01 bundle /mnt/installables/NetQ-5.1.0.tgz config-key CI39fo5CZ3cucHJvZDEubmV0cS5jdW11bHVzbmVp6z8ma3MuY29tGLsD
```

### Related Commands

- ```netq install opta activate-job```

- - -

## netq install patch

Installs a focused software fix using a compressed file package (rather than a full installation or upgrade). Run this command on the NetQ server or VM.

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
nvidia@<hostname>:~$ netq install patch /mnt/installables/NetQ-4.0.0-patch.tgz
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
nvidia@switch:~$ netq install standalone activate-job config-key ju8Kl4IhZ3cucHJvZDEubmV0cPk3vW11bHVzbmV0d29ya3MuY29cB3ag
```

### Related Commands

- ```netq install standalone full```

- - -

## netq install standalone full

Installs the NetQ software on the NetQ VM in an on-premises, single server deployment. You must have the hostname or IP address of the server, and the NetQ software bundle to run the command. A configuration key is optional.

Obtain the software release bundle from the {{<exlink url="https://nvid.nvidia.com/" text="NVIDIA Application Hub">}}.

### Syntax

```
netq install standalone full 
    (interface <text-opta-ifname>|ip-addr <text-ip-addr> [<text-ipv6-addr>]) 
    bundle <text-bundle-url> 
    [ipv6] 
    [config-key <text-opta-key>]
    [pod-ip-range <text-pod-ip-range>]
    [service-ip-range <text-service-ip-range>]
    [s3-access-key <text-s3-access-key> s3-secret-key <text-s3-secret-key>]
    [restore <text-backup-file>]
```
### Required Arguments

| Argument | Value | Description |
| ---- | ---- | ---- |
| interface | \<text-opta-ifname\> | Install NetQ on the server with this interface as the communication interface for the NetQ agents on the monitored switches and hosts |
| ip-addr | \<text-ip-addr\>,\<text-ipv6-addr\>  | Install NetQ on the server with this IPv4 or IPv6 address to communicate with the NetQ agents on the monitored switches and hosts |
| bundle | \<text-bundle-url\> | Install the NetQ software bundle at this location; you must specify a full path |

### Options

| Option | Value | Description |
| ---- | ---- | ---- |
| ipv6 | NA | Install NetQ using an IPv6 address |
| config-key | \<text-opta-key\> | Use this unique key to activate the software |
| pod-ip-range | \<text-pod-ip-range\> | Specify a range of IP addresses for the pod |
| service-ip-range | \<text-service-ip-range\> | Specify a range of IP addresses for the service |
| s3-access-key | \<text-s3-access-key\> | AWS S3 access key ID |
| s3-secret-key| \<text-s3-secret-key\>| AWS S3 secret key ID |
| restore | \<text-backup-file\> | Specify the path where the backup .tar file resides |

### Sample Usage

```
nvidia@<hostname>:~$ netq install standalone full interface eth0 bundle /mnt/installables/NetQ-5.1.0.tgz
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