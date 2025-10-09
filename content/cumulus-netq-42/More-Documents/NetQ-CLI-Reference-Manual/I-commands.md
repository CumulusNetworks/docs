---
title: I through K Commands
author: NVIDIA
weight: 1104
toc: 3
right_toc_levels: 1
pdfhidden: true
---

This topic includes all commands that begin with `netq i*`, `netq j*`, and `netq k*`.

**About Installation Commands**

You can install NetQ with a single command or you can perform the individual steps using multiple commands. Generally, using the single command option is *strongly recommended*. However, the individual commands can be useful for troubleshooting the installation process when it fails. You might need to {{<exlink url="https://support.mellanox.com/s/contact-support-page" text="create a support ticket">}} to take full advantage of the individual commands.

You can use these commands only after bootstrapping the physical server or VM. Refer to {{<link title="A and B Commands/#netq-bootstrap" text="netq bootstrap">}}.

{{<figure src="/images/netq/cliref-install-onprem-single-server-330.png" width="500" caption="On-premises single server">}}

{{<figure src="/images/netq/cliref-install-onprem-server-cluster-330.png" width="600" caption="On-premises server cluster">}}

{{<figure src="/images/netq/cliref-install-cloud-remote-330.png" width="250" caption="Cloud/remote">}}

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

### Command History

A release appears here if there were changes to the command; otherwise it is not listed.

| Release | Description |
| ---- | ---- |
| 2.4.0 | Introduced |

### Sample Usage

<!-- Add output/results -->
```
cumulus@switch:~$ netq install cluster activate-job config-key ju8Kl4IhZ3cucHJvZDEubmV0cPk3vW11bHVzbmV0d29ya3MuY29cB3ag
```

### Related Commands

- netq install cluster infra-job
- netq install cluster init-job
- netq install cluster install-job
- netq install cluster join-workers
- netq install cluster full

- - -

## netq install cluster full

Installs the NetQ Platform software on the servers (NetQ On-premises Appliances or VMs) in an on-premises, server cluster deployment, all with a single command. You must have the hostname or IP address of the master node and two worker nodes, and the NetQ software bundle to run the command.

Obtain the software release bundle from the {{<exlink url="http://support.mellanox.com/s/" text="My Mellanox support">}} page.

### Syntax

```
netq install cluster full
    (interface <text-opta-ifname>|ip-addr <text-ip-addr>)
    bundle <text-bundle-url>
    [config-key <text-opta-key>]
    workers <text-worker-01> <text-worker-02>
```

### Required Arguments

| Argument | Value | Description |
| ---- | ---- | ---- |
| full | NA | Install a server cluster, running all initialization and configuration commands automatically |
| interface | \<text-opta-ifname\> | Install a server cluster with a master node using this interface to communicate with the NetQ Agents on the worker nodes |
| ip-addr | \<text-ip-addr\> | Install a server cluster with a master node with this IP address to communicate with the NetQ Agents on the worker nodes |
| bundle | \<text-bundle-url\> | Install the NetQ software bundle at this location; you must specify a full path |
| workers | \<text-worker-01\> \<text-worker-02\> | Install the worker nodes with these IP addresses |

### Options

| Option | Value | Description |
| ---- | ---- | ---- |
| conifg-key | \<text-opta-key\> | Use this unique key to install the server cluster |

### Command History

A release appears here if there were changes to the command; otherwise it is not listed.

| Release | Description |
| ---- | ---- |
| 2.4.1 | Added `ip-addr` argument |
| 2.4.0 | Added `cluster` and `full` arguments. Removed `download`, `file`, and `force` options. |
| 2.2.2 | Added `download` options |
| Before 2.2.1 | Introduced |

### Sample Usage

<!-- Add output/results -->
```
cumulus@<hostname>:~$ netq install cluster full interface eth0 bundle /mnt/installables/NetQ-4.0.0.tgz workers 10.20.10.25 10.20.10.45
```

### Related Commands

- netq install cluster activate-job
- netq install cluster infra-job
- netq install cluster init-job
- netq install cluster install-job
- netq install cluster join-workers

- - -

<!-- vale off -->
## netq install cluster init-job
<!-- vale on -->

Verifies master node (NetQ On-premises Appliance or VM) resources, extracts NetQ packages, configures Kubernetes, node services and Docker registry, and install the Cassandra database in preparation for NetQ installation and activation in a server cluster deployment.

Alternately, use {{<link title="#netq-install-cluster-full" text="netq install cluster full">}} to perform this and all other steps of a NetQ installation with a single command.

### Syntax

```
netq install cluster init-job
```

### Required Arguments

| Argument | Value | Description |
| ---- | ---- | ---- |
| init-job | NA | Run the initialization jobs |

### Options

None

### Command History

A release appears here if there were changes to the command; otherwise it is not listed.

| Release | Description |
| ---- | ---- |
| 2.4.0 | Introduced |

### Sample Usage

<!-- Add output/results -->
```
cumulus@<hostname>:~$ netq install cluster init-job
```

### Related Commands

- netq install cluster activate-job
- netq install cluster infra-job
- netq install cluster install-job
- netq install cluster join-workers
- netq install cluster full

- - -

<!-- vale off -->
## netq install cluster join-workers
<!-- vale on -->

After initiating a NetQ installation, this command configures the first two worker nodes (NetQ On-premises Appliances or VMs) in a server cluster deployment.

Alternately, use {{<link title="#netq-install-cluster-full" text="netq install cluster full">}} to perform this and all other steps of a NetQ installation with a single command.

Refer to {{<link title="Post Installation Configuration Options#add-more-nodes-to-your-server-cluster" text="Post Installation Configuration Options">}} to add additional worker nodes after NetQ has been completely installed.

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

### Command History

A release appears here if there were changes to the command; otherwise it is not listed.

| Release | Description |
| ---- | ---- |
| 2.4.0 | Introduced |

### Sample Usage

<!-- Add output/results -->
```
cumulus@<hostname>:~$ netq install cluster join-workers 192.168.10.23 192.168.10.25
```

### Related Commands

- netq install cluster activate-job
- netq install cluster infra-job
- netq install cluster init-job
- netq install cluster install-job
- netq install cluster full

- - -

<!-- vale off -->
## netq install cluster infra-job
<!-- vale on -->

After initialization and configuring the worker nodes, this command installs the Kafka service and operators to aid in installation of the NetQ software.

Alternately, use {{<link title="#netq-install-cluster-full" text="netq install cluster full">}} (on-premises) or {{<link title="#netq-install-opta-cluster" text="netq install opta cluster">}} (remote/cloud) to perform this and all other steps of a NetQ installation with a single command.

### Syntax

```
netq install cluster infra-job
```

### Required Arguments

| Argument | Value | Description |
| ---- | ---- | ---- |
| infra-job | NA | Adds infrastructure aids to support installation |

### Options

None

### Command History

A release appears here if there were changes to the command; otherwise it is not listed.

| Release | Description |
| ---- | ---- |
| 2.4.0 | Introduced |

### Sample Usage

<!-- Add output/results -->
```
cumulus@<hostname>:~$ netq install cluster infra-job
```

### Related Commands

- netq install cluster activate-job
- netq install cluster init-job
- netq install cluster install-job
- netq install cluster join-workers
- netq install cluster full

- - -

<!-- vale off -->
## netq install cluster install-job
<!-- vale on -->

After you prepare and configure all the infrastructure, this command installs the NetQ software using the NetQ installation file that you previously downloaded and stored.

Obtain the software release bundle from the {{<exlink url="http://support.mellanox.com/s/" text="My Mellanox support">}} page.

Alternately, use {{<link title="#netq-install-cluster-full" text="netq install cluster full">}} (on-premises) or {{<link title="#netq-install-opta-cluster" text="netq install opta cluster">}} (remote/cloud) to perform this and all other steps of a NetQ installation with a single command.

### Syntax

```
netq install cluster install-job
    bundle <text-bundle-url>
```

### Required Arguments

| Argument | Value | Description |
| ---- | ---- | ---- |
| install-job | NA | Install the NetQ software |
| bundle | \<text-bundle-url\> | Install the `NetQ-x.y.z.tgz` installation file at this location; you must specify a full path |

### Options

None

### Command History

A release appears here if there were changes to the command; otherwise it is not listed.

| Release | Description |
| ---- | ---- |
| 2.4.0 | Introduced |

### Sample Usage

<!-- Add output/results -->
```
cumulus@<hostname>:~$ netq install cluster install-job bundle /mnt/installables/NetQ-4.0.0.tgz
```

### Related Commands

- netq install cluster activate-job
- netq install cluster infra-job
- netq install cluster init-job
- netq install cluster join-workers
- netq install cluster full

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

### Command History

A release appears here if there were changes to the command; otherwise it is not listed.

| Release | Description |
| ---- | ---- |
| 2.4.1 | Introduced |

### Sample Usage

<!-- Add output/results -->
```
cumulus@switch:~$ netq install opta activate-job config-key ju8Kl4IhZ3cucHJvZDEubmV0cPk3vW11bHV9f3lk0d29ya3MuY29cB3ag
```

### Related Commands

- netq install opta cluster
- netq install opta standalone

- - -

## netq install opta cluster

Installs the NetQ Collector software on a master node and two worker nodes. For cloud deployments, it installs the software on the NetQ Cloud Appliance or VM. For a multi-site on-premises deployment, it installs the software on one or two secondary servers at the external premises. You must have the hostname, IP address, or interface of the servers, the NetQ software bundle, and configuration key to run the command. You can also configure a proxy.

Obtain the software release bundle from the {{<exlink url="http://support.mellanox.com/s/" text="My Mellanox support">}} page.

Obtain the config-key as follows:

<!-- vale off -->
- Cloud: Locate and retrieve key from email titled *A new site has been added to your NVIDIA NetQ account* (sent to your NetQ administrator)
- Remote: Follow the instructions in {{<link title="Manage the NetQ UI/#configure-multiple-premises" text="Configure Multiple Premises">}}
<!-- vale on -->

### Syntax

```
netq install opta cluster full
    (interface <text-opta-ifname>|ip-addr <text-ip-addr>)
    bundle<text-bundle-url>
    config-key <text-opta-key>
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
| proxy-host | \<text-proxy-host\> | Use the proxy server with this hostname or IP address instead of directly connecting to the NetQ Cloud Appliance or VM; you must also specify a port |
| proxy-port | \<text-proxy-port\> | Use this port on the proxy server instead of directly connecting to the NetQ Cloud Appliance or VM; you must also specify a proxy host |

### Command History

A release appears here if there were changes to the command; otherwise it is not listed.

| Release | Description |
| ---- | ---- |
| 2.4.1 | Added `ip-addr` argument, `proxy-host` and `proxy-port` options |
| 2.4.0 | Added `cluster` and `full` arguments. Removed `download`, `file`, and `force` options. |
| 2.2.2 | Added `download` options |
| Before 2.2.1 | Introduced |

### Sample Usage

<!-- Add output/results -->
```
cumulus@<hostname>:~$ netq install opta cluster full interface en01 bundle /mnt/installables/NetQ-4.0.0.tgz config-key CI39fo5CZ3cucHJvZDEubmV0cS5jdW11bHVzbmVp6z8ma3MuY29tGLsD workers 10.20.10.25 10.20.10.45
```

### Related Commands

- netq install opta activate-job

- - -

## netq install opta standalone

Installs the NetQ Collector software on a single cloud server (NetQ Cloud Appliance or VM) with a single command. You must have the hostname, IP address, or interface of the server, the NetQ software bundle, and configuration key to run the command. You can also configure a proxy.

Obtain the software release bundle from the {{<exlink url="http://support.mellanox.com/s/" text="My Mellanox support">}} page.

<!-- vale off -->
Obtain the config-key from the email sent to your NetQ administrator titled *A new site has been added to your NVIDIA NetQ account*.
<!-- vale on -->

### Syntax

```
netq install opta standalone full
    (interface <text-opta-ifname>|ip-addr <text-ip-addr>)
    bundle <text-bundle-url>
    config-key <text-opta-key>
    [proxy-host <text-proxy-host> proxy-port<text-proxy-port>]
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
| proxy-host | \<text-proxy-host\> | Use the proxy server with this hostname or IP address instead of directly connecting to the NetQ Cloud Appliance or VM; you must also specify a port |
| proxy-port | \<text-proxy-port\> | Use this port on the proxy server instead of directly connecting to the NetQ Cloud Appliance or VM; you must also specify a proxy host |

### Command History

A release appears here if there were changes to the command; otherwise it is not listed.

| Release | Description |
| ---- | ---- |
| 2.4.0 | Introduced |

### Sample Usage

<!-- Add output/results -->
```
cumulus@<hostname>:~$ netq install opta standalone full interface en01 bundle /mnt/installables/NetQ-4.0.0.tgz config-key CI39fo5CZ3cucHJvZDEubmV0cS5jdW11bHVzbmVp6z8ma3MuY29tGLsD
```

### Related Commands

- netq install opta activate-job

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

### Command History

A release appears here if there were changes to the command; otherwise it is not listed.

| Release | Description |
| ---- | ---- |
| 2.4.1 | Introduced |

### Sample Usage

<!-- Add output/results -->
```
cumulus@<hostname>:~$ netq install patch /mnt/installables/NetQ-4.0.0-patch.tgz
```

### Related Commands

- netq upgrade

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

### Command History

A release appears here if there were changes to the command; otherwise it is not listed.

| Release | Description |
| ---- | ---- |
| 2.4.1 | Replaced `netq update opta config-key` |
| 2.4.0 | Introduced |

### Sample Usage

<!-- Add output/results -->
```
cumulus@switch:~$ netq install standalone activate-job config-key ju8Kl4IhZ3cucHJvZDEubmV0cPk3vW11bHVzbmV0d29ya3MuY29cB3ag
```

### Related Commands

- netq install standalone infra-job
- netq install standalone init-job
- netq install standalone install-job
- netq install standalone full

- - -

## netq install standalone full

Installs the NetQ Platform software on the NetQ On-premises Appliance or VM in an on-premises, single server deployment, all with a single command. You must have the hostname or IP address of the server, and the NetQ software bundle to run the command. A configuration key is optional.

Obtain the software release bundle from the {{<exlink url="http://support.mellanox.com/s/" text="My Mellanox support">}} page.

### Syntax

```
netq install standalone full
    (interface <text-opta-ifname>|ip-addr <text-ip-addr>)
    bundle <text-bundle-url>
    [config-key <text-opta-key>]
```

### Required Arguments

| Argument | Value | Description |
| ---- | ---- | ---- |
| full | NA | Install a server with NetQ software, running all initialization and configuration commands automatically |
| interface | \<text-opta-ifname\> | Install NetQ on the server with this interface as the communication interface for the NetQ Agents on the monitored switches and hosts |
| ip-addr | \<text-ip-addr\> | Install NetQ on the server with this IP address to communicate with the NetQ Agents on the monitored switches and hosts |
| bundle | \<text-bundle-url\> | Install the NetQ software bundle at this location; you must specify a full path |

### Options

| Option | Value | Description |
| ---- | ---- | ---- |
| conifg-key | \<text-opta-key\> | Use this unique key to activate the software |

### Command History

A release appears here if there were changes to the command; otherwise it is not listed.

| Release | Description |
| ---- | ---- |
| 2.4.1 | Added `ip-addr` argument |
| 2.4.0 | Added `standalone` and `full` arguments. Removed `download`, `file`, and `force` options. |
| 2.2.2 | Added `download` options |
| Before 2.2.1 | Introduced |

### Sample Usage

<!-- Add output/results -->
```
cumulus@<hostname>:~$ netq install standalone full interface eth0 bundle /mnt/installables/NetQ-4.0.0.tgz
```

### Related Commands

- netq install standalone activate-job
- netq install standalone infra-job
- netq install standalone init-job
- netq install standalone install-job

- - -

<!-- vale off -->
## netq install standalone infra-job
<!-- vale on -->

After initialization, this command installs kafka and operators to aid in installation of software.

Alternately, use {{<link title="#netq-install-standalone-full" text="netq install standalone full">}} to perform this and all other steps of a NetQ installation with a single command.

### Syntax

```
netq install standalone infra-job
```

### Required Arguments

| Argument | Value | Description |
| ---- | ---- | ---- |
| infra-job | NA | Install helper aids for software installation |

### Options

None

### Command History

A release appears here if there were changes to the command; otherwise it is not listed.

| Release | Description |
| ---- | ---- |
| 2.4.0 | Introduced |

### Sample Usage

<!-- Add output/results -->
```
cumulus@<hostname>:~$ netq install standalone infra-job
```

### Related Commands

- netq install standalone activate-job
- netq install standalone init-job
- netq install standalone install-job
- netq install standalone full

- - -

<!-- vale off -->
## netq install standalone init-job
<!-- vale on -->

Verifies NetQ On-premises Appliance or VM resources, extracts NetQ packages, configures Kubernetes, node services and Docker registry, and install the Cassandra database in preparation for NetQ installation and activation in a single server, on-premises deployment.

Alternately, use {{<link title="#netq-install-standalone-full" text="netq install standalone full">}} to perform this and all other steps of a NetQ installation with a single command.

### Syntax

```
netq install standalone init-job
```

### Required Arguments

| Argument | Value | Description |
| ---- | ---- | ---- |
| init-job | NA | Run the initialization jobs |

### Options

None

### Command History

A release appears here if there were changes to the command; otherwise it is not listed.

| Release | Description |
| ---- | ---- |
| 2.4.0 | Introduced |

### Sample Usage

<!-- Add output/results -->
```
cumulus@<hostname>:~$ netq install standalone init-job
```

### Related Commands

- netq install standalone activate-job
- netq install standalone infra-job
- netq install standalone install-job
- netq install standalone full

- - -

<!-- vale off -->
## netq install standalone install-job
<!-- vale on -->

After you prepare and configure all the infrastructure, this command installs the NetQ Platform software on the NetQ On-premises Appliance or VM using the NetQ installation file that you previously downloaded and stored.

Obtain the software release bundle from the {{<exlink url="http://support.mellanox.com/s/" text="My Mellanox support">}} page.

Alternately, use {{<link title="#netq-install-standalone-full" text="netq install standalone full">}} to perform this and all other steps of a NetQ installation with a single command.

### Syntax

```
netq install standalone install-job
    bundle <text-bundle-url>
```

### Required Arguments

| Argument | Value | Description |
| ---- | ---- | ---- |
| install-job | NA | Install the NetQ software |
| bundle | \<text-bundle-url\> | Install the `NetQ-x.y.z.tgz` installation file at this location; you must specify the full path |

### Options

None

### Command History

A release appears here if there were changes to the command; otherwise it is not listed.

| Release | Description |
| ---- | ---- |
| 2.4.0 | Introduced |

### Sample Usage

<!-- Add output/results -->
```
cumulus@<hostname>:~$ netq install standalone install-job bundle /mnt/installables/NetQ-4.0.0.tgz
```

### Related Commands

- netq install standalone activate-job
- netq install standalone infra-job
- netq install standalone init-job
- netq install standalone full

- - -

<!-- vale off -->
## netq install update-settings
<!-- vale on -->

Overrides system variables after encountering issues during installation. File a {{<exlink url="https://support.mellanox.com/s/contact-support-page" text="support ticket">}} with the NVIDIA Enterprise Support team before using this command. They can provide the key/value pair needed to resolve your issue.

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

### Command History

A release appears here if there were changes to the command; otherwise it is not listed.

| Release | Description |
| ---- | ---- |
| 3.1.0 | Introduced |

### Sample Usage

Change timeout for tasks

```
cumulus@<hostname>:~$ netq install update-settings DEFAULT_TASK_TIMEOUT_IN_MILLIS 3000000
```

### Related Commands

None

- - -
