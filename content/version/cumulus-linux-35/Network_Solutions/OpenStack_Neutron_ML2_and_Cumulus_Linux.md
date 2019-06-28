---
title: OpenStack Neutron ML2 and Cumulus Linux
author: Cumulus Networks
weight: 239
aliases:
 - /display/CL35/OpenStack+Neutron+ML2+and+Cumulus+Linux
 - /pages/viewpage.action?pageId=8357769
pageID: 8357769
product: Cumulus Linux
version: '3.5'
imgData: cumulus-linux-35
siteSlug: cumulus-linux-35
---
The Modular Layer 2 (ML2) plugin is a framework that allows OpenStack
Networking to utilize a variety of non-vendor-specific layer 2
networking technologies. The ML2 framework simplifies adding support for
new layer 2 networking technologies, requiring much less initial and
ongoing effort — specifically, it enables dynamic provisioning of
VLAN/VXLAN on switches in OpenStack environment instead of manually
provisioning L2 connectivity for each VM.

The plugin supports configuration caching. The cached configuration is
replayed back to the Cumulus Linux switch from Cumulus ML2 mechanism
driver when a switch or process restart is detected.

In order to deploy [OpenStack
ML2](https://wiki.openstack.org/wiki/Neutron/ML2) in a network with
Cumulus Linux switches, you need the following:

  - A REST API, which is installed in Cumulus Linux.

  - The Cumulus Networks Modular Layer 2 (ML2) mechanism driver for
    OpenStack, which you install on the OpenStack Neutron controller
    node. It's available as a Python package from upstream.

{{% imgOld 0 %}}

## <span>Configuring the REST API</span>

1.  Configure the relevant settings in `/etc/restapi.conf`:
    
        [ML2]
        #local_bind = 10.40.10.122
        #service_node = 10.40.10.1
         
        # Add the list of inter switch links that
        # need to have the vlan included on it by default
        # Not needed if doing Hierarchical port binding
        #trunk_interfaces = uplink

2.  Restart the REST API service for the configuration changes to take
    effect:
    
        cumulus@switch:~$ sudo systemctl restart restserver

Additional REST API calls have been added to support the configuration
of bridge using the bridge name instead of network ID.

## <span>Installing and Configuring the Cumulus Networks Modular Layer 2 Mechanism Driver</span>

You need to install the Cumulus Networks ML2 mechanism driver on your
Neutron host, which is available upstream:

    root@neutron:~# git clone https://github.com/CumulusNetworks/networking-cumulus.git
    root@neutron:~# cd networking-cumulus
    root@neutron:~# python setup.py install
    root@neutron:~# neutron-db-manage upgrade head

Then configure the host to use the ML2 driver:

    root@neutron:~# openstack-config --set /etc/neutron/plugins/ml2/ml2_conf.ini mechanism_drivers linuxbridge,cumulus

Finally, list the Cumulus Linux switches to configure. Edit
`/etc/neutron/plugins/ml2/ml2_conf.ini` in a text editor and add the IP
addresses of the Cumulus Linux switches to the `switches` line. For
example:

    [ml2_cumulus]
    switches="192.168.10.10,192.168.20.20"

The ML2 mechanism driver contains the following configurable parameters.
You configure them in the `/etc/neutron/plugins/ml2/ml2_conf.ini` file.

  - `switches` — The list of Cumulus Linux switches connected to the
    Neutron host. Specify a list of IP addresses.

  - `scheme` — The scheme (for example, HTTP) for the base URL for the
    ML2 API.

  - `protocol_port` — The protocol port for the bast URL for the ML2
    API. The default value is *8000*.

  - `sync_time` — A periodic time interval for polling the Cumulus Linux
    switch. The default value is *30* seconds.

  - `spf_enable` — Enables/disables SPF for the bridge. The default
    value is *False*.

  - `new_bridge` — Enables/disables [VLAN-aware bridge
    mode](/version/cumulus-linux-35/Layer_1_and_2/Ethernet_Bridging_-_VLANs/VLAN-aware_Bridge_Mode_for_Large-scale_Layer_2_Environments)
    for the bridge configuration. The default value is *False*, so a
    traditional mode bridge is created.

## <span>Demo</span>

A demo involving OpenStack with Cumulus Linux is available in the
[Cumulus Networks knowledge
base](https://support.cumulusnetworks.com/hc/en-us/articles/226174767).
It demonstrates dynamic provisioning of VLANs using a virtual simulation
of two Cumulus VX leaf switches and two CentOS 7 (RDO Project) servers;
collectively they comprise an OpenStack environment.
