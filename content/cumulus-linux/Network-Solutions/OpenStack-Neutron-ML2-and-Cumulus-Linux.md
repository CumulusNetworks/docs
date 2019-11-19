---
title: OpenStack Neutron ML2 and Cumulus Linux
author: Cumulus Networks
weight: 253
aliases:
 - /display/DOCS/OpenStack+Neutron+ML2+and+Cumulus+Linux
 - /pages/viewpage.action?pageId=8366713
product: Cumulus Linux
version: '4.0'
---
The Modular Layer 2 (ML2) plugin is a framework that allows OpenStack Networking to use a variety of non-vendor-specific layer 2 networking technologies. The ML2 framework simplifies adding support for new layer 2 networking technologies and enables dynamic provisioning of VLAN/VXLAN on switches in an OpenStack environment instead of manually provisioning layer 2 connectivity for each VM.

The plugin supports configuration caching. The cached configuration is replayed back to the Cumulus Linux switch from the Cumulus ML2 mechanism driver when a switch or process restart is detected.

To deploy [OpenStack ML2](https://wiki.openstack.org/wiki/Neutron/ML2) in a network with Cumulus Linux switches, you need the following:

- A REST API, which is installed with Cumulus Linux.
- The Cumulus Networks Modular Layer 2 (ML2) mechanism driver for OpenStack, which you install on the OpenStack Neutron controller node. The driver is available as a Python package from upstream.
- The OpenStack Queens release.

{{< img src = "/images/cumulus-linux/network-solutions-ml2-driver-arch.png" >}}

## Configure the REST API

1. Configure the relevant settings in the `/etc/restapi.conf` file:

```
[ML2]
#local_bind = 10.40.10.122
#service_node = 10.40.10.1

# Add the list of inter switch links that
# need to have the vlan included on it by default
# Not needed if doing Hierarchical port binding
#trunk_interfaces = uplink
```

2. Restart the REST API service for the configuration changes to take effect:

```
cumulus@switch:~$ sudo systemctl restart restserver
```

Additional REST API calls have been added to support bridge configuration using the bridge name instead of network ID.

## Install and Configure the ML2 Driver

1. Install the Cumulus Networks ML2 mechanism driver on your Neutron host, which is available upstream:

```
root@neutron:~# git clone https://github.com/CumulusNetworks/networking-cumulus.git
root@neutron:~# cd networking-cumulus
root@neutron:~# python setup.py install
root@neutron:~# neutron-db-manage upgrade head
```

2. Configure the host to use the ML2 driver:

```
root@neutron:~# openstack-config --set /etc/neutron/plugins/ml2/ml2_conf.ini mechanism_drivers linuxbridge,cumulus
```

3. List the Cumulus Linux switches to configure. Edit the `/etc/neutron/plugins/ml2/ml2_conf.ini` file and add the IP addresses of the Cumulus Linux switches to the `switches` line. For example:

```
[ml2_cumulus]
switches="192.168.10.10,192.168.20.20"
```

The ML2 mechanism driver includes the following parameters, which you can configure in the `/etc/neutron/plugins/ml2/ml2_conf.ini` file.

| Parameter | Description |
|-----------| ------------|
| `switches` | The list of Cumulus Linux switches connected to the Neutron host. Specify a list of IP addresses. |
| `scheme` | The scheme for the base URL for the ML2 API. For example, HTTP. |
| `protocol_port` | The protocol port for the bast URL for the ML2 API. The default value is *8000*. |
| `sync_time` | A periodic time interval for polling the Cumulus Linux switch. The default value is *30* seconds.|
| `spf_enable` | Enables and disables SPF for the bridge. The default value is *False*.|
|`new_bridge` | Enables and disables [VLAN-aware bridge mode](../../Layer-2/Ethernet-Bridging-VLANs/VLAN-aware-Bridge-Mode/) for the bridge configuration. The default value is *False*, so a traditional mode bridge is created. |

## OpenStack with Cumulus in the Cloud

OpenStack Neutron is available as a preconfigured option with [Cumulus in the
Cloud](https://cumulusnetworks.com/products/cumulus-in-the-cloud/). Add the ML2 driver, described above.
