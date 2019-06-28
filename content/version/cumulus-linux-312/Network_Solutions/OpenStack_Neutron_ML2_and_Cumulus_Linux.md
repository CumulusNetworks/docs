---
title: OpenStack Neutron ML2 and Cumulus Linux
author: Cumulus Networks
weight: 201
aliases:
 - /display/CL31/OpenStack+Neutron+ML2+and+Cumulus+Linux
 - /pages/viewpage.action?pageId=5122188
pageID: 5122188
product: Cumulus Linux
version: 3.1.2
imgData: cumulus-linux-312
siteSlug: cumulus-linux-312
---
{{%notice warning%}}

**Early Access Feature**

The REST API component is an [early access
feature](https://support.cumulusnetworks.com/hc/en-us/articles/202933878)
in Cumulus Linux 3.1. Before you can install the API, you must enable
the Early Access repository. For more information about the Cumulus
Linux repository, read [this knowledge base
article](https://support.cumulusnetworks.com/hc/en-us/articles/217422127).

{{%/notice%}}

In order to deploy [OpenStack
ML2](https://wiki.openstack.org/wiki/Neutron/ML2) in a network with
Cumulus Linux switches, you need to install two packages:

  - A REST API, which you install on your Cumulus Linux switches. It is
    in the Cumulus Linux [early
    access](https://support.cumulusnetworks.com/hc/en-us/articles/202933878)
    repository.

  - The Cumulus Networks Modular Layer 2 (ML2) mechanism driver for
    OpenStack, which you install on the OpenStack Neutron controller
    node. It's available as Debian DEB and Red Hat RPM packages in the
    Cumulus Networks [GitHub
    repository](https://github.com/CumulusNetworks/cumulus-ml2/tree/master/images).

{{% imgOld 0 %}}

## <span>Installing and Configuring the REST API</span>

To install the `python-falcon` and `python-cumulus-restapi` packages,
follow the instructions in the [Cumulus Linux 3.1 release
notes](https://support.cumulusnetworks.com/hc/en-us/articles/224473608#ea).

Then configure the relevant settings in `/etc/restapi.conf`:

    [ML2]
    #local_bind = 10.40.10.122
    #service_node = 10.40.10.1
     
    # Add the list of inter switch links that
    # need to have the vlan included on it by default
    # Not needed if doing Hierarchical port binding
    #trunk_interfaces = uplink 
     
    #For persistency across reboots use "net" command
    #use_net = True

In order for the bridge configurations to persist across reboots on the
Cumulus Linux switch, you need to uncomment the `use_net` setting in
`restapi.conf` and install the [`net` command line
interface](/version/cumulus-linux-312/Configuring_and_Managing_Network_Interfaces/Network_Command_Line_Utility).

Restart the REST API service for the configuration changes to take
effect:

    cumulus@switch:~$ sudo systemctl restart restserver

## <span>Installing and Configuring the Cumulus Networks Modular Layer 2 Mechanism Driver</span>

You need to install the Cumulus Networks ML2 mechanism driver on your
Neutron host. Download the Debian .deb or Red Hat RPM image from the
Cumulus Networks [GitHub
repository](https://github.com/CumulusNetworks/cumulus-ml2/tree/master/images).

  - To install the Debian image, run
    
        root@neutron:~# dpkg –i cumulus-ml2-driver_1.0.0-cl3eau1_all.deb

  - To install the RPM image, run:
    
        root@neutron:~# rpm -ivh cumulus-ml2-driver-1.0.0.dev8-1.noarch.rpm

Then configure the host to use the ML2 driver:

    root@neutron:~# openstack-config --set /etc/neutron/plugins/ml2/ml2_cumulus.ini mechanism_drivers linuxbridge,cumulus

Finally, list the Cumulus Linux switches to configure. Edit
`/etc/neutron/plugins/ml2/ml2_cumulus.ini` in a text editor and add the
IP addresses of the Cumulus Linux switches to the `switches` line. For
example:

    [ml2_cumulus]
    switches="192.168.10.10,192.168.20.20"

## <span>Demo</span>

A demo involving OpenStack with Cumulus Linux is available in the
[Cumulus Networks knowledge
base](https://support.cumulusnetworks.com/hc/en-us/articles/226174767).
It demonstrates dynamic provisioning of VLANs using a virtual simulation
of two Cumulus VX leaf switches and two CentOS 7 (RDO Project) servers;
collectively they comprise an OpenStack environment.
