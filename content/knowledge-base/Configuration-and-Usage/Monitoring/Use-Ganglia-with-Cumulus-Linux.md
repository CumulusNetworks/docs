---
title: Use Ganglia with Cumulus Linux
author: Cumulus Networks
weight: 376
toc: 4
---

{{<exlink url="http://ganglia.sourceforge.net/" text="Ganglia">}}, a BSD-licensed open-source project, is a scalable distributed monitoring system for high-performance computing systems such as clusters and grids.According to the {{<exlink url="http://ganglia.sourceforge.net/" text="official Ganglia website">}}, the implementation is robust, has been ported to an extensive set of operating systems and processor architectures, and is currently in use on thousands of clusters around the world. Ganglia has been used to link clusters across university campuses and around the world and can scale to handle clusters with 2000 nodes.

Since Cumulus Linux is Linux, Ganglia also works great to monitor switches as well as servers. This article provides setup instructions for using Ganglia on Cumulus Linux.

## Requirements

- A {{<exlink url="https://cumulusnetworks.com/hcl" text="Cumulus Linux switch">}}
- A host running {{<exlink url="http://httpd.apache.org/" text="apache">}} on the same network. For the example shown we used Debian wheezy.
- Access to the {{<exlink url="http://repo3.cumulusnetworks.com/repo/pool/" text="Cumulus Linux repo">}} from the network where the host and switch reside.

## Set Up the Host

1.  The host, where the Web front end will reside for collection, must have three parts installed:

    - `ganglia-monitor`, also known as `gmond` (Ganglia monitoring daemon)
    - `gmetad`, which stands for Ganglia meta daemon
    - `ganglia-webfrontend`, which contains the PHP-based real-time dynamic Web pages

    All three are described on {{<exlink url="https://en.wikipedia.org/wiki/Ganglia_(software)" text="Wikipedia">}} and in {{<exlink url="http://sourceforge.net/apps/trac/ganglia/wiki/ganglia_quick_start" text="the Ganglia documentation">}}.

2.  Install these components on the host:

        user@webserver$ sudo apt-get install ganglia-monitor gmetad ganglia-webfrontend

3.  If you are unfamiliar with `apache`, the host needs to have the `/etc/ganglia-webfrontend/apache.conf` copied to `/etc/apache2/sites-enabled/` to enable the Ganglia Web front end, which defaults to http://\<the-host-ip\>/ganglia where \<the-host-ip\> is the IP of the host used, like http://10.0.1.1/ganglia.

4.  Configure the data sources. In this case, we are configuring the Cumulus Linux switch and the local host (Web server). On Debian wheezy, this file is located at `/etc/ganglia/gmetad.conf`.

        data_source "server" localhost server.lab.test 10.0.1.1
        data_source "sw1" sw1.lab.test 10.0.1.11

5.  Cumulus Linux supports both multicast and unicast traffic with Ganglia. We are going to configure unicast rather than the default multicast because many environments do not want multicast. This is a personal preference and has no bearing on the output provided by Ganglia. First, edit `/etc/ganglia/gmond.conf` and set the `send_metadata_interval`. In this example we use 30 seconds.

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

6.  Set up the cluster. This information must match between the host and the nodes it is listening to. The example below uses RDU, which stands for Raleigh, Durham (two amazing cities in central North Carolina). Continue editing `/etc/ganglia/gmond.conf`.
    
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

9.  At this point you should start seeing server statistics show up in Ganglia by viewing them at http://\<the-host-ip\>/ganglia. It is simply seeing its own data. As you can see in this example, we sometimes interchange DNS and IP, making sure DNS is set up or only utilize the reachable IPs.

## Set Up the Switch

1.  The switch, or node, where we want to monitor traffic must have just one package installed:

    - `ganglia-monitor`, also known as `gmond` (Ganglia monitoring daemon)

2.  `gmond` has been added to the Cumulus Linux repo. Install `ganglia-monitor` by running:

        cumulus@switch$ sudo apt-get install ganglia-monitor

3.  As with the host (Web server), we are going to configure unicast for this example. First set up the `send_metadata_interval` by editing `/etc/ganglia/gmond.conf`. In this example we use 30 seconds.

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

4.  Set up the cluster; edit `/etc/ganglia/gmond.conf`. This information must match between the switch and the host configured above. In our example we used RDU.

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

7.  After a minute the PHP front end on the host (server) will start getting enough data to see in the graphs. They will look like the following:

    - First select sw1 and pick a metric like CPU speed.  

      {{<img src="/images/knowledge-base/ganglia-choose-host.png">}}

    - It opens up the following:

    {{<img src="/images/knowledge-base/ganglia-sw1.png">}}

8.  You can now use all of Ganglia's features the same as someone would on servers.

## Multiple Interfaces Module

Ganglia was originally meant for hosts (servers) so originally most applications only used 1-2 interfaces. However, with Cumulus Linux, multiple front panel ports that show up as swp1-\>swpMAX where MAX is the last front panel port. Some users will want to see not aggregate packet counts for the box but packet counts per-interface to watch utilization. Fortunately there is already an open source module that is easy to add to Ganglia called {{<exlink url="https://github.com/ganglia/gmond_python_modules/tree/master/network/iface/python_modules" text="multi\_interface">}}.

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

We can also see that while swp10-13 do not have any traffic running across them, unlike swp45, which has traffic running. And of course Ganglia allows us to zoom in to get more statistics with their Web interface.

{{<img src="/images/knowledge-base/ganglia-swp45.png">}}

## See Also

- {{<exlink url="https://github.com/ganglia/gmond_python_modules/tree/master/network/iface/python_modules" text="Ganglia multi_interface module">}}
- {{<link url="Set-up-a-Basic-Ansible-Lab/">}}

<!-- 
## Comments

- 
    
    <div id="comment_204032787">
    
    <div class="comment-avatar">
    
    ![Avatar](https://secure.gravatar.com/avatar/d83a3dc2148554274e009a06f095f9ab?default=https%3A%2F%2Fassets.zendesk.com%2Fhc%2Fassets%2Fdefault_avatar.png&r=g)
    
    </div>
    
    <div class="comment-container">
    
    **Gabriel Stoicea** <span class="comment-published">December 18,
    2014 14:04</span>
    
    <div class="comment-body markdown">
    
    Concerning "Multiple Interfaces Module" the above recipe is not
    complete.
    
    When I tried to enable multi\_interface.py following the above
    recipe didn't worked out. Finally I discovered the solution.  
    You have to do in addition before:  
    \- Add the following lines inside module section in
    “/etc/ganglia/gmond.conf” config file:
    
    cumulus@cumulus-atlas-test$ sudo vi /etc/ganglia/gmond.conf  
    module {  
    name = "python\_module"  
    path = "/usr/lib/ganglia/modpython.so"  
    params = "/usr/lib/ganglia/python\_modules/"  
    }
    
    - Also add the following line at the end of
        “/etc/ganglia/gmond.conf” config file:
    
    include ('/etc/ganglia/conf.d/\*.pyconf')
    
    After that you can follow the above recipe for multi\_interface.  
    In the end please restart gmond:
    
    cumulus@cumulus-atlas-test$ sudo service ganglia-monitor restart
    
    That's all.
    
    Cheers,  
    Gabriel
    
    </div>
    
    <span class="comment-actions"> <span class="dropdown">
    <span class="dropdown-toggle" data-aria-label="Comment actions" data-aria-haspopup="true">Comment
    actions</span> <span class="dropdown-menu" data-role="menu">
    /span> </span>
    </span>
    
    </div>
    
    </div>

- 
    
    <div id="comment_202709248">
    
    <div class="comment-avatar">
    
    ![Avatar](https://support.cumulusnetworks.com/system/photos/0001/1962/5696/Sean2.jpg)
    
    </div>
    
    <div class="comment-container">
    
    **Sean Cavanaugh** <span class="comment-published">December 18, 2014
    14:07</span>
    
    <div class="comment-body markdown">
    
    Gabriel, really appreciate you taking the time to add the comment to
    help others that might get stuck, this is awesome\!
    
    </div>
    
    <span class="comment-actions"> <span class="dropdown">
    <span class="dropdown-toggle" data-aria-label="Comment actions" data-aria-haspopup="true">Comment
    actions</span> <span class="dropdown-menu" data-role="menu">
    </span> </span>
    </span>
    
    </div>
    
    </div>

- 
    
    <div id="comment_202709268">
    
    <div class="comment-avatar">
    
    ![Avatar](https://secure.gravatar.com/avatar/d83a3dc2148554274e009a06f095f9ab?default=https%3A%2F%2Fassets.zendesk.com%2Fhc%2Fassets%2Fdefault_avatar.png&r=g)
    
    </div>
    
    <div class="comment-container">
    
    **Gabriel Stoicea** <span class="comment-published">December 18,
    2014 14:12</span>
    
    <div class="comment-body markdown">
    
    Some correction:
    
    In "name" must be an underscore between python and module and also
    other underscore in "params" between python and modules.  
    When I submitted the above comment the underscore sign disappeared.
    
    Thanks.  
    Best regards,  
    Gabriel
    
    </div> -->
