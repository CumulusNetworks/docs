---
title: Use Ganglia with Cumulus Linux
author: NVIDIA
weight: 376
toc: 4
---

{{<exlink url="http://ganglia.sourceforge.net/" text="Ganglia">}}, a BSD-licensed open-source project, is a scalable distributed monitoring system for high-performance computing systems such as clusters and grids. According to the {{<exlink url="http://ganglia.sourceforge.net/" text="official Ganglia website">}}, the implementation is robust, is compatible with an extensive set of operating systems and processor architectures, and is currently in use on thousands of clusters around the world. You can use Ganglia to link clusters across university campuses and around the world and can scale to handle clusters with 2000 nodes.

Because Cumulus Linux is Linux, Ganglia also works great to monitor switches as well as servers. This article provides setup instructions for using Ganglia on Cumulus Linux.

## Requirements

- A {{<exlink url="https://www.nvidia.com/en-us/networking/ethernet-switching/hardware-compatibility-list/" text="Cumulus Linux switch">}}
- A host running {{<exlink url="http://httpd.apache.org/" text="apache">}} on the same network. The example here uses Debian wheezy.
- Access to the {{<exlink url="http://repo3.cumulusnetworks.com/repo/pool/" text="Cumulus Linux repo">}} from the network where the host and switch reside.

## Set Up the Host

1.  The host, where the web front end is going to reside for collection, must have three parts installed:

    - `ganglia-monitor`, also known as `gmond` (Ganglia monitoring daemon)
    - `gmetad`, which stands for Ganglia meta daemon
    - `ganglia-webfrontend`, which contains the PHP-based real-time dynamic Web pages

    You can learn more about these parts in {{<exlink url="https://en.wikipedia.org/wiki/Ganglia_(software)" text="Wikipedia">}} and in {{<exlink url="http://sourceforge.net/apps/trac/ganglia/wiki/ganglia_quick_start" text="the Ganglia documentation">}}.

2.  Install these components on the host:

        user@webserver$ sudo apt-get install ganglia-monitor gmetad ganglia-webfrontend

3.  If you are unfamiliar with `apache`, the host needs to have the `/etc/ganglia-webfrontend/apache.conf` copied to `/etc/apache2/sites-enabled/` to enable the Ganglia Web front end, which defaults to http://\<the-host-ip\>/ganglia where \<the-host-ip\> is the IP of the host used, like http://10.0.1.1/ganglia.

4.  Configure the data sources. In this case, you are configuring the Cumulus Linux switch and the local host (Web server). On Debian wheezy, you can find this file at `/etc/ganglia/gmetad.conf`.

        data_source "server" localhost server.lab.test 10.0.1.1
        data_source "sw1" sw1.lab.test 10.0.1.11

5.  Cumulus Linux supports both multicast and unicast traffic with Ganglia. You are going to configure unicast rather than the default multicast because many environments do not want multicast. This is a personal preference and has no bearing on the output provided by Ganglia. First, edit `/etc/ganglia/gmond.conf` and set the `send_metadata_interval`. This example uses 30 seconds.

        globals {
          daemonize = yes
          setuid = yes
          user = ganglia
          debug_level = 0
          max_udp_msg_len = 1472
          mute = no
          deaf = no
          host_dmax = 0 /*secs */
          cleanup_threshold = 300 /*secs */
          gexec = no
          send_metadata_interval = 30
        }

6.  Set up the cluster. This information must match between the host and the nodes it is listening to. The example below uses RDU, which stands for Raleigh and Durham (two cities in central North Carolina). Continue editing `/etc/ganglia/gmond.conf`.
    
        cluster {
          name = "RDU"
          owner = "RDU"
          latlong = "unspecified"
          url = "unspecified"
        }

7.  Set up the recieve and send channels with `udp` (again, configuring `/etc/ganglia/gmond.conf`). Make them match the following:
    
        udp_send_channel {
          host = server.lab.test
          port = 8649
        }
        udp_recv_channel {
          port = 8649
        }

8.  Restart `gmond` and `gmetad`.

        cumulus@switch$ sudo service ganglia-monitor restart
        cumulus@switch$ sudo service gmetad restart

9.  At this point you should start seeing server statistics show up in Ganglia by viewing them at *http://\<the-host-ip\>/ganglia*. It is just seeing its own data. This example sometimes interchanges DNS and IP, making sure DNS is set up or only utilizing the reachable IPs.

## Set Up the Switch

1.  The switch, or node, where you want to monitor traffic must have just one package installed:

    - `ganglia-monitor`, also known as `gmond` (Ganglia monitoring daemon)

2.  With `gmond` added to the Cumulus Linux repo, install `ganglia-monitor` by running:

        cumulus@switch$ sudo apt-get install ganglia-monitor

3.  As with the host (Web server), you are configuring unicast for this example. First set up the `send_metadata_interval` by editing `/etc/ganglia/gmond.conf`. This example uses 30 seconds.

        globals {
          daemonize = yes
          setuid = yes
          user = ganglia
          debug_level = 0
          max_udp_msg_len = 1472
          mute = no
          deaf = no
          host_dmax = 0 /*secs */
          cleanup_threshold = 300 /*secs */
          gexec = no
          send_metadata_interval = 30
        }

4.  Set up the cluster; edit `/etc/ganglia/gmond.conf`. This information must match between the switch and the host configured above. This example uses RDU.

        cluster {
          name = "RDU"
          owner = "RDU"
          latlong = "unspecified"
          url = "unspecified"
        }

5.  Set up the unicast send channels with `udp` by configuring `/etc/ganglia/gmond.conf` as follows:

        udp_send_channel {
          host = server.lab.test
          port = 8649
        }

6.  Restart the `gmond` process:

        cumulus@switch$ sudo service ganglia-monitor restart

7.  After a minute, the PHP front end on the host (server) starts getting enough data to see in the graphs. They look like the following:

    - First select sw1 and pick a metric like CPU speed.  

      {{<img src="/images/knowledge-base/ganglia-choose-host.png">}}

    - It opens up the following:

    {{<img src="/images/knowledge-base/ganglia-sw1.png">}}

8.  You can now use any Ganglia features just like you would on servers.

## Multiple Interfaces Module

Ganglia was originally meant for hosts (servers) so originally most applications only used 1-2 interfaces. However, with Cumulus Linux, multiple front panel ports that show up as swp1-\>swpMAX where MAX is the last front panel port. Some users might not want to see aggregate packet counts for the switch but packet counts per-interface to watch utilization. To do this, you can add an open source module to Ganglia called {{<exlink url="https://github.com/ganglia/gmond_python_modules/tree/master/network/iface/python_modules" text="multi\_interface">}}.

1.  Download {{<exlink url="https://github.com/ganglia/gmond_python_modules/tree/master/network/iface/python_modules" text="multi_interface.py">}}.

        cumulus@switch$ sudo wget https://raw.githubusercontent.com/ganglia/gmond_python_modules/master/network/multi_interface/python_modules/multi_interface.py .

2.  Put `multi_interface.py` into `/usr/lib/ganglia/python_modules/`.  

        cumulus@switch$ sudo mkdir -p /usr/lib/ganglia/python_modules/; mv multi_interface.py /usr/lib/ganglia/python_modules/

3.  Download {{<exlink url="https://github.com/ganglia/gmond_python_modules/tree/master/network/iface/conf.d" text="multi_interface.pyconf">}}.

        cumulus@switch$ sudo wget https://github.com/ganglia/gmond_python_modules/tree/master/network/iface/conf.d .

4.  Add the following lines to the module section in the `/etc/ganglia/gmond.conf` configuration file:

        cumulus@switch$ sudo vi /etc/ganglia/gmond.conf
        module {
        name = "python_module"
        path = "/usr/lib/ganglia/modpython.so"
        params = "/usr/lib/ganglia/python_modules/"
        }

    Also add the following line at the end of `/etc/ganglia/gmond.conf`:

        include ('/etc/ganglia/conf.d/*.pyconf')

5.  Put `multi_interface.pyconf` into `/etc/ganglia/conf.d/`.  

        cumulus@switch$ sudo mkdir -p /etc/ganglia/conf.d/; mv multi_interface.pyconf /etc/ganglia/conf.d/

6.  Restart `gmond`.

        cumulus@switch$ sudo service ganglia-monitor restart

7.  The display now has a multiple interfaces graphed for each swp as well as the management interface of eth0:

    {{<img src="/images/knowledge-base/ganglia-front_panel_ports.png">}}

You can also see that while swp10-13 do not have any traffic running across them, unlike swp45, which has traffic running. Ganglia also allows you to zoom in to get more statistics with their Web interface.

{{<img src="/images/knowledge-base/ganglia-swp45.png">}}

## See Also

- {{<exlink url="https://github.com/ganglia/gmond_python_modules/tree/master/network/iface/python_modules" text="Ganglia multi_interface module">}}
- {{<link url="Set-up-a-Basic-Ansible-Lab/">}}
