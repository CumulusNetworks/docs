---
title: Prerequisites
author: Cumulus Networks
weight: 408
aliases:
 - /display/NETQ/Install+NetQ
 - /pages/viewpage.action?pageId=12320951
pageID: 12320951
product: Cumulus NetQ
version: 2.4
imgData: cumulus-netq
siteSlug: cumulus-netq
---
This topic describes the hardware and software requirements for installation of the Cumulus NetQ software on your own hardware.

## Hardware Requirements

Cumulus NetQ software is supported on a variety of hardware.

{{%notice info%}}

A fresh server or appliance is recommended for NetQ installation. Alternately, you can create a new VM or re-image an existing server with Ubuntu as the base operating system. Be sure to back up any NetQ data beforehand if you choose this alternative.

Servers must meet these *minimum* hardware requirements to install the VM and have it run properly.

{{%/notice%}}

The NetQ software requires a server with the following:

<table>
<colgroup>
<col style="width: 30%" />
<col style="width: 30%" />
<col style="width: 40%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Hardware Component</p></th>
<th><p>Minimum Cloud Requirement</p></th>
<th><p>Minimum On-premises Requirement</p></th>
</tr>
</thead>
<tbody>
<tr class="even">
<td>Processor</td>
<td>Four (4) virtual CPUs</td>
<td>Eight (8) virtual CPUs</td>
</tr>
<tr class="odd">
<td>Memory</td>
<td>8 GB RAM</td>
<td>64 GB RAM</td>
</tr>
<tr class="even">
<td>Local disk storage</td>
<td>32 GB <br>(SSD not required)</td>
<td>256 GB SSD <br>(<strong>Note</strong>: This <em>must</em> be an SSD; use of other storage options can lead to system instability and are not supported.)</td>
</tr>
<tr class="odd">
<td>Network interface speed</td>
<td>1 Gb NIC</td>
<td>1 Gb NIC</td>
</tr>
</tbody>
</table>

You must also open the following ports on your NetQ Platform server or your  cluster servers:

For external connections:

| Port  |  Protocol | Component Access |
| ------: |  :-----: | ----- |
| 8443 |  TCP | Admin UI |
| 443 | TCP | NetQ UI |
| 31980 | TCP | NetQ Agent communication |
| 32708 | TCP | API Gateway |
| 22 | TCP | SSH |

For internal cluster communication:

| Port  |  Protocol | Component Access |
| ------: |  :-----: | ----- |
| 8080 | TCP | Admin API |
| 5000 | TCP | Docker registry |
| 8472 | UDP | Flannel port for VXLAN |
| 6443 | TCP | Kubernetes API server |
| 10250 | TCP | kubelet health probe |
| 2379 | TCP | etcd |
| 2380 | TCP | etcd |
| 7072 | TCP | Kafka JMX monitoring |
| 9092 | TCP | Kafka client |
| 7071 | TCP | Cassandra JMX monitoring |
| 7000 | TCP | Cassandra cluster communication |
| 9042 | TCP | Cassandra client |
| 7073 | TCP | Zookeeper JMX |
| 2888 | TCP | Zookeeper cluster communication |
| 3888 | TCP | Zookeeper cluster communication |
| 2181 | TCP | Zookeeper client |

{{%notice tip%}}
Port 32666 is no longer used for the NetQ UI.
{{%/notice%}}

### NetQ Platform HyperVisor Requirements

The NetQ Platform can be installed as a Virtual Machine (VM) using one
of the following hypervisors:

- VMware ESXi™ 6.5 for servers running Cumulus Linux, CentOS, Ubuntu
    and RedHat operating systems.
- KVM/QCOW (QEMU Copy on Write) image for servers running CentOS,
    Ubuntu and RedHat operating systems.

### NetQ Agent Operating System Requirements

NetQ 2.4 Agents are supported on the following switch and host operating
systems:

- Cumulus Linux 3.3.2 and later
- Ubuntu 16.04
- Ubuntu 18.04 (NetQ 2.2.2 and later)
- Red Hat Enterprise Linux (RHEL) 7.1
- CentOS 7

### NetQ Application Support

The NetQ CLI, UI, and RESTful API are supported on NetQ 2.1.0 and later.
NetQ 1.4 and earlier applications are not supported in NetQ 2.x.
