---
title: OpenStack Neutron ML2 and Cumulus Linux
author: NVIDIA
weight: 255
pageID: 8362989
---
The Modular Layer 2 (ML2) plugin is a framework that allows OpenStack
Networking to utilize a variety of non-vendor-specific layer 2
networking technologies. The ML2 framework simplifies adding support for
new layer 2 networking technologies, requiring much less initial and
ongoing effort - specifically, it enables dynamic provisioning of
VLAN/VXLAN on switches in OpenStack environment instead of manually
provisioning L2 connectivity for each VM.

The plugin supports configuration caching. The cached configuration is
replayed back to the Cumulus Linux switch from Cumulus ML2 mechanism
driver when a switch or process restart is detected.

In order to deploy {{<exlink url="https://wiki.openstack.org/wiki/Neutron/ML2" text="OpenStack ML2">}}
in a network with Cumulus Linux switches, you need the following:

- A REST API, which is installed in Cumulus Linux.
- The Modular Layer 2 (ML2) mechanism driver for OpenStack, which you install on the OpenStack Neutron controller node. It's available as a Python package from upstream.
- The OpenStack Queens release.

{{< img src = "/images/cumulus-linux/network-solutions-ml2-driver-arch.png" >}}

## Configure the REST API

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

## Install and Configure the Modular Layer 2 Mechanism Driver

You need to install the ML2 mechanism driver on your
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

  - `switches` - The list of Cumulus Linux switches connected to the
    Neutron host. Specify a list of IP addresses.
  - `scheme` - The scheme (for example, HTTP) for the base URL for the
    ML2 API.
  - `protocol_port` - The protocol port for the bast URL for the ML2
    API. The default value is *8000*.
  - `sync_time` - A periodic time interval for polling the Cumulus Linux
    switch. The default value is *30* seconds.
  - `spf_enable` - Enables/disables SPF for the bridge. The default
    value is *False*.
  - `new_bridge` - Enables/disables {{<link url="VLAN-aware-Bridge-Mode" text="VLAN-aware bridge mode">}}
    for the bridge configuration. The default value is *False*, so a
    traditional mode bridge is created.

## Try OpenStack with Cumulus in the Cloud

OpenStack Neutron is available as a preconfigured option with
{{<exlink url="https://www.nvidia.com/en-us/networking/network-simulation/" text="Cumulus in the Cloud">}}.
You just need to add the ML2 driver, as per the
{{<link url="#install-and-configure-the-cumulus-networks-modular-layer-2-mechanism-driver" text="instructions above">}}.
