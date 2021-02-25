---
title: I through K Commands
author: NVIDIA
weight: 1104
toc: 3
right_toc_levels: 1
pdfhidden: true
draft: true
---

This topic includes all commands that begin with `netq i*`, `netq j*`, and `netq k*`.

NetQ installation can be performed with a single command or you can perform the individual steps using multiple commands. Generally, using a single command is recommended. However, the individual commands can be useful for troubleshooting the installation process.

{{<figure src="/images/netq/cliref-install-onprem-single-server-330.png" width="500" caption="On-premises single server">}}

{{<figure src="/images/netq/cliref-install-onprem-server-cluster-330.png" width="600" caption="On-premises server cluster">}}

{{<figure src="/images/netq/cliref-install-cloud-remote-330.png" width="250" caption="Cloud/remote">}}

## netq install cluster activate-job

Activates a NetQ instance after an initial server cluster (master and two worker nodes) is configured. Activation requires a configuration key. For cloud deployments, this can be found in an email titled "*A new site has been added to your Cumulus NetQ account*". For multi-site on-premises deployments, you must generate the key from the NetQ UI as described in the {{<link title="Manage the NetQ UI/#configure-multiple-premises" text="NetQ user guide">}}.

Alternately, use the `netq install cluster full` (on-premises) `netq install opta cluster` (remote/cloud) command to perform this and all other steps of a NetQ installation with a single command.

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

A release is included if there were changes to the command, otherwise it is not listed.

| Release | Description |
| ---- | ---- |
| 2.4.0 | Introduced |

### Sample Usage

<!-- Add output/results??? -->
```
cumulus@switch:~$ netq install cluster activate-job config-key ju8Kl4IhZ3cucHJvZDEubmV0cPk3vW11bHVzbmV0d29ya3MuY29cB3ag
```

### Related Commands

- netq install cluster infra-job
- netq install cluster init-job
- netq install cluster install-job
- netq install cluster join-workers
- netq install cluster full
- netq install opta cluster

- - -

## netq install cluster full

Installs a NetQ instance for an on-premises, server cluster deployment in a single command. You must have the hostname or IP address of the master node and two worker nodes, and the NetQ software bundle to run the command. A configuration key is optional ???

Obtain the software release bundle from the {{<exlink url="https://cumulusnetworks.com/downloads/#product=NetQ" text="Cumulus Downloads">}} page or {{<exlink url="http://support.mellanox.com/s/" text="My Mellanox support">}} page.

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
| bundle | \<text-bundle-url\> | Install the NetQ software bundle at this location; a full path is required |
| workers | \<text-worker-01\> \<text-worker-02\> | Install the worker nodes with these hostnames or IP addresses |

### Options

| Option | Value | Description |
| ---- | ---- | ---- |
| conifg-key | \<text-opta-key\> | Use this unique key to install the server cluster |

### Command History

A release is included if there were changes to the command, otherwise it is not listed.

| Release | Description |
| ---- | ---- |
| 2.4.0 | Introduced |

### Sample Usage

<!-- Add output/results??? -->
```
cumulus@<hostname>:~$ netq install cluster full interface eth0 bundle /mnt/installables/NetQ-3.3.1.tgz workers 10.20.10.25 10.20.10.45
```

### Related Commands

- netq install cluster infra-job
- netq install cluster init-job
- netq install cluster install-job
- netq install cluster join-workers
- netq install cluster full
- netq install opta cluster

- - -

## netq install cluster init-job

Verifies master node resources, extracts NetQ packages, configures Kubernetes, node services and Docker registry in preparation for NetQ installation and activation in a server cluster deployment.

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

A release is included if there were changes to the command, otherwise it is not listed.

| Release | Description |
| ---- | ---- |
| 2.4.0 | Introduced |

### Sample Usage

<!-- Add output/results??? -->
```
cumulus@<hostname>:~$ netq install cluster init-job
```

### Related Commands

- netq install cluster activate-job
- netq install cluster infra-job
- netq install cluster install-job
- netq install cluster join-workers
- netq install cluster full
- netq install opta cluster

- - -

## netq install cluster join-workers

netq install cluster join-workers <text-worker-01> [<text-worker-02>]

## netq install cluster infra-job

netq install cluster infra-job

## netq install cluster install-job

netq install cluster install-job bundle <text-bundle-url>

## netq install opta activate-job

netq install opta activate-job config-key <text-opta-key>

## netq install opta cluster

netq install opta cluster full (interface <text-opta-ifname>|ip-addr <text-ip-addr>) bundle<text-bundle-url> config-key <text-opta-key> workers <text-worker-01> <text-worker-02>[proxy-host <text-proxy-host> proxy-port <text-proxy-port>]

## netq install opta standalone

netq install opta standalone full (interface <text-opta-ifname>|ip-addr <text-ip-addr>)bundle <text-bundle-url> config-key <text-opta-key> [proxy-host <text-proxy-host> proxy-port<text-proxy-port>]

## netq install patch

netq install patch <text-tarball-name>

## netq install standalone activate-job

netq install standalone activate-job config-key <text-opta-key>

## netq install standalone full

netq install standalone full (interface <text-opta-ifname>|ip-addr <text-ip-addr>) bundle <text-bundle-url> [config-key <text-opta-key>]

## netq install standalone infra-job

netq install standalone infra-job

## netq install standalone init-job

netq install standalone init-job

## netq install standalone install-job

netq install standalone install-job bundle <text-bundle-url>

## netq install update-settings

netq install update-settings <text-key> <text-value>

3.1.0 intro
