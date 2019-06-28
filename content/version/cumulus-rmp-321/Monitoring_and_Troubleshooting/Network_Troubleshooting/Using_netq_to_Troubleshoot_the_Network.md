---
title: Using netq to Troubleshoot the Network
author: Cumulus Networks
weight: 213
aliases:
 - /display/RMP321/Using+netq+to+Troubleshoot+the+Network
 - /pages/viewpage.action?pageId=5127565
pageID: 5127565
product: Cumulus RMP
version: 3.2.1
imgData: cumulus-rmp-321
siteSlug: cumulus-rmp-321
---
{{%notice warning%}}

**Early Access Feature**

`netq` is an [early access
feature](https://support.cumulusnetworks.com/hc/en-us/articles/202933878)
in Cumulus RMP 3.2. Before you can install `netq`, you must enable the
Early Access repository. For more information about the Cumulus Linux
repository, read [this knowledge base
article](https://support.cumulusnetworks.com/hc/en-us/articles/217422127).

{{%/notice%}}

`netq` is a tool for troubleshooting the whole network fabric. Instead
of using other tools to troubleshoot node by node, `netq` aggregates
data from across all the nodes in a network, so you can query and
diagnose issues affecting the whole network, analyze outages or discover
why two or more switches cannot communicate. `netq` can return a wealth
of data about your network for both layer 2 and the layer 3 IP fabric,
including:

  - Interface history

  - MLAG checks

  - Anycast IP validation

  - Interface address history

  - IP neighbor history

  - MTU validation of traceroutes

  - Route history

  - Route origin validation

`netq` provides the ability to see the output of commands on other
switches, even if a switch is currently unavailable. You can even see
the command history so you can go back in time before the issue arouse
to debug it.

Because `netq` is a Linux application, it's easy to automate with tools
like Ansible, Puppet or Chef.

## <span>Components</span>

`netq` has three primary components:

  - `netq-agent`: The back end Python agent installed on every Cumulus
    RMP switch in the network; the agent pushes out data to a central
    server (a `redis` server, see below) periodically and when specific
    ` netlink  `events occur. The `redis` server processes the queries
    and sends back a response to the switch. The agent listens for these
    events:
    
      - address (IPv4 and IPv6)
    
      - route (IPv4 and IPv6)
    
      - link
    
      - bridge fdb
    
      - IP neighbor

  - `netq`: The command line interface to the `netq-agent`. You can use
    the `netq` CLI on every Cumulus RMP switch as well as the `redis`
    server.

  - `redis` server: The database/key-value store where all network
    information sent from `netq-agents` running on Cumulus RMP switches
    is collected and aggregated. The server runs ` redis  `version
    2.8.17-1.

{{% imgOld 0 %}}

## <span>Feature Limitations</span>

`netq` is an [early access
feature](https://support.cumulusnetworks.com/hc/en-us/articles/202933878).
As such, the following features are limited or unavailable at this time,
and should be available in a future release of Cumulus RMP:

  - You can check BGP health only at this time; reporting OSPF health
    should follow in the near future.

  - You cannot determine the origin of static routes.

  - Interoperability with [management
    VRF](/version/cumulus-rmp-321/Routing/Management_VRF) is not
    supported.

  - Clustering the `redis` server for high availability has not been
    tested.

  - `netq` has been tested with up to 20 nodes in a fabric, with 8k
    routes and MAC addresses per node.

If you are interested in trying out this or any other early access
feature, contact your Cumulus Networks account representative to let us
know you are testing it.

## <span>Installing netq</span>

To install the `netq` package — `cumulus-netq` — on a switch, follow the
instructions below. The `cumulus-netq` package contains `netq` and the
`netq-agent`. Cumulus Networks recommends you install the `netq-agent`
on every Cumulus RMP switch in the network; you can also install it on
the redis server.

1.  Open the `/etc/apt/sources.list` file in a text editor.

2.  Uncomment the early access repository lines and save the file:
    
        deb http://repo3.cumulusnetworks.com/repo CumulusLinux-3-early-access cumulus
        deb-src http://repo3.cumulusnetworks.com/repo CumulusLinux-3-early-access cumulus

3.  Run the following commands in a terminal to install the
    `cumulus-netq` package:
    
        cumulus@switch:~$ sudo apt-get update
        cumulus@switch:~$ sudo apt-get install cumulus-netq

### <span>Installing redis Server</span>

Cumulus Networks recommends you install the `redis` server on its own
server or VM. Ideally, you should run the `redis` server on a separate,
powerful server for maximum usability and performance — Cumulus Networks
recommends a system with a quad core CPU, 16GB of RAM (with 8GB for
`redis` itself) and 512GB of storage.

You need to download and install two packages:

  - The [`redis-server`
    package](https://packages.debian.org/jessie/database/redis-server),
    version 2.8.17-1.

  - The [`redis-tools`
    package](https://packages.debian.org/jessie/redis-tools), version
    2.8.17-1.

Use `apt-get` to install the packages:

    root@redis-server:~# apt-get update
    root@redis-server:~# apt-get install redis-server redis-tools

After you install these packages, connect the server over the management
network to ensure network connectivity even if the in-band network is
unavailable. Note its IP address, as you need to specify it when you
configure `netq`.

{{%notice note%}}

If you want to run the `netq` CLI on the redis server, you need to
install the `cumulus-netq` package on the server. You'll need to update
your sources.list file to include the [Cumulus Linux
repository](https://support.cumulusnetworks.com/hc/en-us/articles/217422127).
The install the package, following the instructions in the [Cumulus
Linux 3.2 release
notes](https://cumulusnetworks.zendesk.com/hc/en-us/articles/232013208).
The `cumulus-netq` package contains the `netq` client, which contains
the CLI.

{{%/notice%}}

{{%notice note%}}

You cannot specify a port number for the `redis` server at this time.

{{%/notice%}}

Once you install the redis server, you must configure it before you can
configure netq on the switch.

## <span>Configuring the redis Server</span>

Depending upon the operating system of the redis server host, you may
need to modify its configuration before it can start monitoring the
network. Check the `/etc/redis/redis.conf` file and verify that the
server is listening to external-facing ports, and not the localhost.

1.  Edit `/etc/redis/redis.conf`:
    
        root@redis-server:~# vi /etc/redis/redis.conf

2.  If the bind line links to localhost (127.0.0.1), change it to the IP
    address of one or more external ports, such as eth0:
    
        bind 192.0.2.240

3.  Restart the `redis-server` service. For example, on a Debian host,
    run:
    
        root@redis-server:~# systemctl restart redis-server

## <span>Configuring netq</span>

Once you install the `netq` packages and configure the redis server, you
need to configure `netq` to monitor your network.

1.  To ensure useful output, ensure that
    [NTP](/version/cumulus-rmp-321/System_Configuration/Setting_Date_and_Time)
    is running.

2.  Specify the IP address of the `redis` server. For example:
    
        cumulus@switch:~$ sudo netq add server 198.51.100.1

3.  Start the `netq` agent.
    
        cumulus@switch:~$ sudo netq agent start
    
    {{%notice note%}}
    
    If you see the following error, it means you haven't added the redis
    server or the server wasn't configured:
    
        cumulus@switch:~$ sudo netq agent start
        Error: Please specify IP address of DB server
    
    {{%/notice%}}

The `netq` configuration is stored in the following files:

  - `/etc/netq/netq-agent.conf`: Contains basic agent configuration,
    including the `redis` server IP address.

  - `/etc/netq/netq-agent-commands.json`: Contains key-value pairs of
    commands whose outputs are pushed along with the key to be
    associated, periodicity of push and so forth.

  - `/etc/netq/netq-agent-running.json`: Log of the actual commands that
    are being pushed to the agent, as determined when the agent starts,
    as well as the `redis` server IP address and more.

## <span>Using netq</span>

`netq` has a number of options to use with the command to return various
kinds of data about your network — press the *Tab* key at any time to
reveal the options available to a given part of the command. Running
`netq` on its own reveals all the options, with a brief explanation for
each one:

    cumulus@switch:~$ netq <TAB>
    add : Update configuration
    agent : Netq agent
    health : Show liveness and status of agent/bgp/mlag in fabric
    help : Show usage info
    resolve : Annotate input with names and interesting info
    server : IP address of DB server
    show : Show fabric-wide info
    view : Show output of pre-defined commands on specific node

### <span>Checking the Health of the Network</span>

It's best to start with ` netq check agents  `to see the status of every
network node, based on the whether the agent missed receiving any
heartbeats sent from the node. A node's status can be one of the
following:

  - **Fresh:** The agent is running fine, no heartbeats were missed.

  - **Stale:** The agent missed one heartbeat, which is not unusual.

  - **Rotten:** The agent missed five consecutive heartbeats.

<!-- end list -->

    cumulus@switch:~$ sudo netq check agents
     
    Node Name  Connect Time  Time Since Connect       Status
    ---------- ------------- ------------------------ --------
    leaf-1     2016-08-23    03:59:00 15 seconds ago  Fresh
    leaf-2     2016-08-23    03:59:00 14 seconds ago  Fresh
    leaf-3     2016-08-23    03:58:59 16 seconds ago  Fresh
    leaf-4     2016-08-23    03:58:55 20 seconds ago  Fresh
    leaf-5     2016-08-23    03:58:59 16 seconds ago  Fresh
    leaf-6     2016-08-23    03:58:59 15 seconds ago  Fresh
    leaf-7     2016-08-23    03:58:59 16 seconds ago  Fresh
    leaf-8     2016-08-23    03:58:58 16 seconds ago  Fresh
    leaf-9     2016-08-23    03:58:56 19 seconds ago  Fresh
    spine-1    2016-08-23    03:58:59 16 seconds ago  Fresh
    spine-2    2016-08-23    03:58:58 17 seconds ago  Fresh
    spine-3    2016-08-23    03:58:55 19 seconds ago  Fresh
    spine-4    2016-08-23    03:58:56 19 seconds ago  Fresh

You can also check the health of BGP and MLAG in the network:

    cumulus@switch:~$ netq check bgp
    No BGP sessions in failed state
     
     
    cumulus@switch:~$ netq check clag
    Failed Node          Reason
    -------------------- ------------------------------------------------------------
    leaf-9               Peer Connectivity failed
    None

### <span>Using netq show</span>

The `netq show` command can return information regarding the network
fabric overall, including:

  - Interface IP and MAC addresses across all nodes in the fabric.

  - Interfaces across all nodes in the fabric.

  - IPv4 and IPv6-related information.

  - LLDP-based neighbor information.

  - MAC address information, with VLANs if present, across the fabric.

The `netq show` command takes the following options:

    cumulus@switch:~$ sudo netq show [addresses | info | interfaces | ip | ipv6 | lldp | macs]

To see MAC address information for switch leaf-1, you would run:

    cumulus@switch:~$ netq show macs leaf-1
    List of nodes containing MAC *
    MAC               VLAN   Node Name   Egress Port   Update Time
    ----------------- ------ ----------- ------------- --------------
    00:00:5e:00:01:01  0     leaf-1      bridge        33 minutes ago
    00:00:5e:00:01:01  0     leaf-1      bridge.20     33 minutes ago
    00:00:5e:00:01:01  20    leaf-1      bridge        33 minutes ago
    08:00:27:51:3f:c2  0     leaf-1      bond-swp6     33 minutes ago
    08:00:27:51:3f:c2  20    leaf-1      bridge        33 minutes ago
    08:00:27:7f:06:83  0     leaf-1      peer-link     33 minutes ago
    08:00:27:9d:9d:2d  0     leaf-1      bond-swp5     33 minutes ago

You can filter the output to a given interface on a switch, in this case
a bridge on leaf-1 named *bridge*:

    vagrant@spine-1:~$ netq show macs leaf-1 bridge
    List of nodes containing MAC *
    MAC               VLAN   Node Name   Egress Port   Update Time
    ----------------- ------ ----------- ------------- --------------
    00:00:5e:00:01:01  0     leaf-1      bridge        33 minutes ago
    00:00:5e:00:01:01  20    leaf-1      bridge        33 minutes ago
    08:00:27:51:3f:c2  20    leaf-1      bridge        33 minutes ago

To see the route information, run:

    cumulus@switch:~$ netq show ip routes 10.1.20.1
    Route info about prefix 10.1.20.1 on host *
    Origin Table IP               Node             Nexthops                  Update Time
    ------ ----- ---------------- ---------------- ------------------------- ----------------
    0      254   10.1.20.0/24     leaf-3           169.254.0.1: swp4,        38 minutes ago
                                                   169.254.0.1: swp1,
                                                   169.254.0.1: swp2,
                                                   169.254.0.1: swp3
    0      254   10.1.20.0/24     leaf-4           169.254.0.1: swp4,        38 minutes ago
                                                   169.254.0.1: swp1,
                                                   169.254.0.1: swp3,
                                                   169.254.0.1: swp2
    0      254   10.1.20.0/24     leaf-5           169.254.0.1: swp4,        38 minutes ago
                                                   169.254.0.1: swp3,
                                                   169.254.0.1: swp1,
                                                   169.254.0.1: swp2
    0      254   10.1.20.0/24     leaf-6           169.254.0.1: swp4,        38 minutes ago
                                                   169.254.0.1: swp3,
                                                   169.254.0.1: swp2,
                                                   169.254.0.1: swp1
    0      254   10.1.20.0/24     leaf-7           169.254.0.1: swp4,        38 minutes ago
                                                   169.254.0.1: swp1,
                                                   169.254.0.1: swp3,
                                                   169.254.0.1: swp2
    0      254   10.1.20.0/24     leaf-8           169.254.0.1: swp4,        38 minutes ago
                                                   169.254.0.1: swp1,
                                                   169.254.0.1: swp3,
                                                   169.254.0.1: swp2
    0      254   10.1.20.0/24    leaf-9            169.254.0.1: swp4,        38 minutes ago
                                                   169.254.0.1: swp3,
                                                   169.254.0.1: swp1,
                                                   169.254.0.1: swp2
    0      254   10.1.20.0/24    spine-1           169.254.0.1: swp2,        38 minutes ago
                                                   169.254.0.1: swp1
    0      254   10.1.20.0/24    spine-2           169.254.0.1: swp1,        38 minutes ago
                                                   169.254.0.1: swp2
    0      254   10.1.20.0/24    spine-3           169.254.0.1: swp1,        38 minutes ago
                                                   169.254.0.1: swp2
    0      254   10.1.20.0/24    spine-4           169.254.0.1: swp1,        38 minutes ago
                                                   169.254.0.1: swp2
    1      254   10.1.20.0/24    leaf-2            Local                     38 minutes ago
    1      255   10.1.20.1/32    leaf-1            Local                     38 minutes ago

### <span>Using netq view</span>

The `netq view` command provides information about a specific node in
the network. The available options are:

    cumulus@switch:~$ netq view leaf-1 <TAB>
    addr : addr
    bgp : bgp
    clagctl : clagctl
    config : config
    counters : counters
    ifquery : ifquery
    link : link
    lldp : lldp
    meminfo : meminfo
    mstpctl : mstpctl
    uptime : uptime

For example, to see the BGP summary for switch leaf-5, run:

    cumulus@switch:~$ netq view leaf-5 bgp summary
    Output retrieved from 6 seconds ago
    BGP router identifier 192.0.2.10, local AS number 64517 vrf-id 0
    BGP table version 27
    RIB entries 33, using 3960 bytes of memory
    Peers 4, using 65 KiB of memory
    Peer groups 1, using 56 bytes of memory
     
    Neighbor V AS MsgRcvd MsgSent TblVer InQ OutQ Up/Down State/PfxRcd
    spine-1(swp1) 4 65000 169503 169504 0 0 0 5d21h17m 12
    spine-2(swp2) 4 65000 169505 169508 0 0 0 5d21h17m 12
    spine-3(swp3) 4 65000 169505 169508 0 0 0 5d21h17m 12
    spine-4(swp4) 4 65000 169504 169512 0 0 0 5d21h17m 12
     
     
    Total number of neighbors 4

## <span>Monitoring the redis Server</span>

You can use the `redis-cli info` command to determine how much memory is
consumed by the `redis` server, how many connections there are, and so
forth.

Two recommended commands to use are ` redis-cli info  `and ` redis-cli
ping  `.

{{%notice note%}}

To use the [`redis` CLI](http://redis.io/topics/rediscli), you need to
[install](https://packages.debian.org/jessie/redis-tools) `redis-tools`.

{{%/notice%}}

### <span>Specifying a Different redis Server</span>

If you need to change the IP address of the `redis` server, run `netq
add server` again, specifying the IP address of the new server, then
restart the `netq` agent. For example:

    cumulus@switch:~$ sudo netq add 198.51.100.10
    cumulus@switch:~$ sudo netq agent restart

Note that you need to specify this for every switch that you're
monitoring with `netq`. Cumulus Networks recommends you use an
automation tool like Ansible or Puppet to quickly update the server
across all switches.

## <span>Troubleshooting netq</span>

`netq` agent logs to `/var/log/netq-agent.log`. The logs are logrotated.

To ensure that the `netq` agent is running, run:

    cumulus@switch:~$ sudo netq agent status
    Running...
