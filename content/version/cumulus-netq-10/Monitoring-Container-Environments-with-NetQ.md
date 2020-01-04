---
title: Monitoring Container Environments with NetQ
author: Cumulus Networks
weight: 25
aliases:
 - /display/NETQ10/Monitoring+Container+Environments+with+NetQ
 - /pages/viewpage.action?pageId=6488224
pageID: 6488224
product: Cumulus NetQ
version: 1.0.0
imgData: cumulus-netq-10
siteSlug: cumulus-netq-10
---
The NetQ Agent monitors Docker containers the same way it monitors
[physical
servers](/version/cumulus-netq-10/Monitoring-Linux-Hosts-with-NetQ).
There is no special implementation. The NetQ Agent pulls Docker data
from the container as it would pull data from a Cumulus Linux switch or
Linux host.

NetQ monitors many aspects of containers on your network, including
their:

  - **Identity**: The NetQ agent tracks every container's IP and MAC
    address, name, image, and more. NetQ can locate containers across
    the fabric based on a container's name, image, IP or MAC address,
    and protocol and port pair.

  - **Port mapping on a network**: The NetQ agent tracks protocol and
    ports exposed by a container. NetQ can identify containers exposing
    a specific protocol and port pair on a network.

  - **Connectivity**: NetQ can provide information on network
    connectivity for a container, including adjacency, and can identify
    containers that can be affected by a top of rack switch.

## NetQ Container Support</span>

The NetQ Agent supports Docker version 1.13 (Jan 2017), 17.04.0-ce
(April 2017).

The NetQ Agent parses the following Docker events:

  - Image: pull and delete

  - Container: run, stop, start, restart, attach and detach

  - Network: create, connect, disconnect and destroy

Currently, the NetQ Agent does not support:

  - Monitoring Docker volume mount and unmount events

  - Plugin install and deletes

  - Third party network configuration through plugins like Calico

  - Docker Swarm service

### Telemetry Server Memory Requirement</span>

Due to the higher memory requirements to run containers, Cumulus
Networks recommends you run the NetQ Telemetry Server on a host with at
least 32G RAM. For more information, read the [Performing Network
Diagnostics](Performing-Network-Diagnostics.html#src-6488212_PerformingNetworkDiagnostics-matrix)
chapter.

## <span id="src-6488224_MonitoringContainerEnvironmentswithNetQ-enable" class="confluence-anchor-link"></span>Configuring the Container Host</span>

In order for NetQ to be able to monitor the containers on a host, you
need to do three things:

  - Configure the host to point to the telemetry server by its IP
    address

  - Enable Docker in the NetQ configuration file

  - Restart the agent

See the section on [configuring the NetQ agent on a
node](Getting-Started-with-NetQ.html#src-6488202_GettingStartedwithNetQ-nodeconfig)
for details. In the following example `/etc/netq/netq.yml` file on the
server, the last three lines enable Docker:

    cumulus@server01:~$ sudo vi /etc/netq/netq.yml
    # See /usr/share/doc/netq/examples for full configuration file
    backend:
      port: 6379
      server: 192.168.0.10
      vrf: default
    user-commands:
    - commands:
      - command: /bin/cat /etc/network/interfaces
        key: config-interfaces
        period: '60'
      - command: /bin/cat /etc/ntp.conf
        key: config-ntp
        period: '60'
      service: misc
    - commands:
      - command:
        - /usr/bin/vtysh
        - -c
        - show running-config
        key: config-quagga
        period: '60'
      service: zebra
    view-commands:
    - commands:
      - command: /bin/cat /etc/network/interfaces
        key: config-interfaces
        period: '60'
      - command: /bin/cat /etc/ntp.conf
        key: config-ntp
        period: '60'
      service: misc
    - commands:
      - command:
        - /usr/bin/vtysh
        - -c
        - show running-config
        key: config-quagga
        period: '60'
      service: zebra
     
    docker:
      enable: true
      poll_period: 15

## Starting and Stopping Containers</span>

If you need to start or stop a single container on a host, use the
`docker-compose` command. In the example below, the container is called
*netq\_cont\_a*:

    cumulus@server01:~$ sudo docker-compose -f /appliance/cfg/docker/netq-base-compose.yml -p netq_cont_a stop netq-notifier
    cumulus@server01:~$ sudo docker-compose -f /appliance/cfg/docker/netq-base-compose.yml -p netq_cont_a start netq-notifier

## Showing Container Summary Information</span>

To see a high level view of the network, including the number of
containers installed and running on the network, run `netq show docker
summary`:

    cumulus@server01:~$ netq show docker summary 
    Node        Version       Installed    Running    Images  Swarm Cluster    Networks
    ----------  ----------  -----------  ---------  --------  ---------------  ----------
    exit01      17.03.1-ce           26         26         1                   3
    exit02      17.03.1-ce            1          0         3                   3
    server01    17.03.1-ce            0          0         0                   3
    server02    17.03.1-ce            0          0         0                   3
    server03    17.03.1-ce            0          0         0                   3
    server04    17.03.1-ce            0          0         0                   3
    server01    17.03.1-ce           13         13         1                   3
    server02    17.03.1-ce            0          0         0                   3

## Identifying Containers on the Network</span>

To view the different container networks and the containers in them, run
`netq show docker network`:

    cumulus@server01:~$ netq show docker network
    Network Name     Node       subnet          gateway         ipv6      ip masq. encrypted
    ---------------- ---------- --------------- --------------- --------- -------- ---------
    bridge           exit01     172.17.0.0/16                   Disabled  True     False
    bridge           exit02     172.17.0.0/16                   Disabled  True     False
    bridge           server01   172.17.0.0/16                   Disabled  True     False
    bridge           server02   172.17.0.0/16                   Disabled  True     False
    bridge           server03   172.17.0.0/16                   Disabled  True     False
    bridge           server04   172.17.0.0/16                   Disabled  True     False
    bridge           server01   172.17.0.0/16                   Disabled  True     False
    bridge           server02   172.17.0.0/16                   Disabled  True     False
    bridge           server03   172.17.0.0/16                   Disabled  True     False
    bridge           server04   172.17.0.0/16                   Disabled  True     False
    host             exit01                                     Disabled  False    False
    host             exit02                                     Disabled  False    False
    host             server01                                   Disabled  False    False
    host             server02                                   Disabled  False    False
    host             server03                                   Disabled  False    False
    host             server04                                   Disabled  False    False
    host             server01                                   Disabled  False    False
    host             server02                                   Disabled  False    False
    host             server03                                   Disabled  False    False
    host             server04                                   Disabled  False    False
    none             exit01                                     Disabled  False    False
    none             exit02                                     Disabled  False    False
    none             server01                                   Disabled  False    False
    none             server02                                   Disabled  False    False
    none             server03                                   Disabled  False    False
    none             server04                                   Disabled  False    False
    none             server01                                   Disabled  False    False
    none             server02                                   Disabled  False    False
    none             server03                                   Disabled  False    False
    none             server04                                   Disabled  False    False

To view all the hosts using a specific container network driver, use
`netq show docker network driver NAME`. Use the `brief` keyword for a
shorter summary. Docker supports many network drivers.

    cumulus@server01:~$ netq show docker network driver bridge brief 
    Network Name     Node       Driver    subnet          gateway         ipv6      ip masq. encrypted Containers
    ---------------- ---------- --------- --------------- --------------- --------- -------- --------- -------------------------
    bridge           exit01     bridge    172.17.0.0/16                   Disabled  True     False     Name:netcat-8085 IPv4:172
                                                                                                       .17.0.7/16,
                                                                                                       Name:netcat-8082 IPv4:172
                                                                                                       .17.0.4/16,
                                                                                                       Name:netcat-8083 IPv4:172
                                                                                                       .17.0.5/16,
                                                                                                       Name:netcat-8089 IPv4:172
                                                                                                       .17.0.11/16,
                                                                                                       Name:netcat-8081 IPv4:172
                                                                                                       .17.0.3/16,
                                                                                                       Name:netcat-8084 IPv4:172
                                                                                                       .17.0.6/16,
                                                                                                       Name:netcat-8090 IPv4:172
                                                                                                       .17.0.12/16,
                                                                                                       Name:netcat-8080 IPv4:172
                                                                                                       .17.0.2/16,
                                                                                                       Name:netcat-8091 IPv4:172
                                                                                                       .17.0.13/16,
                                                                                                       Name:netcat-8092 IPv4:172
                                                                                                       .17.0.14/16,
                                                                                                       Name:netcat-8088 IPv4:172
                                                                                                       .17.0.10/16,
                                                                                                       Name:netcat-8087 IPv4:172
                                                                                                       .17.0.9/16,
                                                                                                       Name:netcat-8086 IPv4:172
                                                                                                       .17.0.8/16
    bridge           exit02     bridge    172.17.0.0/16                   Disabled  True     False
    bridge           server01   bridge    172.17.0.0/16                   Disabled  True     False
    bridge           server02   bridge    172.17.0.0/16                   Disabled  True     False
    bridge           server03   bridge    172.17.0.0/16                   Disabled  True     False
    bridge           server04   bridge    172.17.0.0/16                   Disabled  True     False
    bridge           server01   bridge    172.17.0.0/16                   Disabled  True     False     Name:netcat-8082 IPv4:172
                                                                                                       .17.0.4/16,
                                                                                                       Name:netcat-8085 IPv4:172
                                                                                                       .17.0.7/16,
                                                                                                       Name:netcat-8083 IPv4:172
                                                                                                       .17.0.5/16,
                                                                                                       Name:netcat-8086 IPv4:172
                                                                                                       .17.0.8/16,
                                                                                                       Name:netcat-8089 IPv4:172
                                                                                                       .17.0.11/16,
                                                                                                       Name:netcat-8084 IPv4:172
                                                                                                       .17.0.6/16,
                                                                                                       Name:netcat-8092 IPv4:172
                                                                                                       .17.0.14/16,
                                                                                                       Name:netcat-8087 IPv4:172
                                                                                                       .17.0.9/16,
                                                                                                       Name:netcat-8080 IPv4:172
                                                                                                       .17.0.2/16,
                                                                                                       Name:netcat-8081 IPv4:172
                                                                                                       .17.0.3/16,
                                                                                                       Name:netcat-8090 IPv4:172
                                                                                                       .17.0.12/16,
                                                                                                       Name:netcat-8091 IPv4:172
                                                                                                       .17.0.13/16,
                                                                                                       Name:netcat-8088 IPv4:172
                                                                                                       .17.0.10/16
    bridge           server02   bridge    172.17.0.0/16                   Disabled  True     False
    bridge           server03   bridge    172.17.0.0/16                   Disabled  True     False
    bridge           server04   bridge    172.17.0.0/16                   Disabled  True     False

To see all the containers on a given container network, run the
following command, where the container network is named *host*:

    cumulus@server01:~$ netq show docker container network host 
    Name                 Node       IP                IP Masq. Network        Service Name    Up time
    -------------------- ---------- ----------------- -------- -------------- --------------- ---------------
    netcat-9080          exit01     45.0.0.17/26,     False    host                           0:29:42
                                    27.0.0.3/32,
                                    192.168.0.15/24
    netcat-9081          exit01     45.0.0.17/26,     False    host                           0:29:41
                                    27.0.0.3/32,
                                    192.168.0.15/24
    netcat-9082          exit01     45.0.0.17/26,     False    host                           0:29:42
                                    27.0.0.3/32,
                                    192.168.0.15/24
    netcat-9083          exit01     45.0.0.17/26,     False    host                           0:29:39
                                    27.0.0.3/32,
                                    192.168.0.15/24
    netcat-9084          exit01     45.0.0.17/26,     False    host                           0:29:40
                                    27.0.0.3/32,
                                    192.168.0.15/24
    netcat-9085          exit01     45.0.0.17/26,     False    host                           0:29:40
                                    27.0.0.3/32,
                                    192.168.0.15/24
    netcat-9086          exit01     45.0.0.17/26,     False    host                           0:29:39
                                    27.0.0.3/32,
                                    192.168.0.15/24
    netcat-9087          exit01     45.0.0.17/26,     False    host                           0:29:38
                                    27.0.0.3/32,
                                    192.168.0.15/24
    netcat-9088          exit01     45.0.0.17/26,     False    host                           0:29:37
                                    27.0.0.3/32,
                                    192.168.0.15/24
    netcat-9089          exit01     45.0.0.17/26,     False    host                           0:29:38
                                    27.0.0.3/32,
                                    192.168.0.15/24
    netcat-9090          exit01     45.0.0.17/26,     False    host                           0:29:36
                                    27.0.0.3/32,
                                    192.168.0.15/24
    netcat-9091          exit01     45.0.0.17/26,     False    host                           0:29:37
                                    27.0.0.3/32,
                                    192.168.0.15/24
    netcat-9092          exit01     45.0.0.17/26,     False    host                           0:29:38
                                    27.0.0.3/32,
                                    192.168.0.15/24

## Showing Container Adjacency</span>

NetQ can list all the containers running on hosts adjacent to a top of
rack switch. This helps in analyzing what impact the ToR switch can have
on an application

To identify all the containers that may have been launched on hosts that
are adjacent to a given node, run `netq NODE show docker container
adjacent`:

    cumulus@leaf01:~$ netq leaf01 show docker container adjacent
    Interface            Peer Node  Peer Interface        Container Name       IP                   Network    Service Name
    -------------------- ---------- --------------------- -------------------- -------------------- ---------- ---------------
    swp6:VlanA-1         server01   mac:00:02:00:00:00:27 netcat-9090                               host
    swp6:VlanA-1         server01   mac:00:02:00:00:00:27 netcat-9082                               host
    swp6:VlanA-1         server01   mac:00:02:00:00:00:27 netcat-9091                               host
    swp6:VlanA-1         server01   mac:00:02:00:00:00:27 netcat-9086                               host
    swp6:VlanA-1         server01   mac:00:02:00:00:00:27 netcat-9081                               host
    swp6:VlanA-1         server01   mac:00:02:00:00:00:27 netcat-9083                               host
    swp6:VlanA-1         server01   mac:00:02:00:00:00:27 netcat-9087                               host
    swp6:VlanA-1         server01   mac:00:02:00:00:00:27 netcat-9088                               host
    swp6:VlanA-1         server01   mac:00:02:00:00:00:27 netcat-9085                               host
    swp6:VlanA-1         server01   mac:00:02:00:00:00:27 netcat-9080                               host
    swp6:VlanA-1         server01   mac:00:02:00:00:00:27 netcat-9084                               host
    swp6:VlanA-1         server01   mac:00:02:00:00:00:27 netcat-9089                               host
    swp6:VlanA-1         server01   mac:00:02:00:00:00:27 netcat-9092                               host
    swp7:VlanA-1         server02   mac:00:02:00:00:00:2a netcat-8089          172.17.0.11          bridge
    swp7:VlanA-1         server02   mac:00:02:00:00:00:2a netcat-8084          172.17.0.6           bridge
    swp7:VlanA-1         server02   mac:00:02:00:00:00:2a netcat-8092          172.17.0.14          bridge
    swp7:VlanA-1         server02   mac:00:02:00:00:00:2a netcat-8083          172.17.0.5           bridge
    swp7:VlanA-1         server02   mac:00:02:00:00:00:2a netcat-8085          172.17.0.7           bridge
    swp7:VlanA-1         server02   mac:00:02:00:00:00:2a netcat-8081          172.17.0.3           bridge
    swp7:VlanA-1         server02   mac:00:02:00:00:00:2a netcat-8080          172.17.0.2           bridge
    swp7:VlanA-1         server02   mac:00:02:00:00:00:2a netcat-8086          172.17.0.8           bridge
    swp7:VlanA-1         server02   mac:00:02:00:00:00:2a netcat-8088          172.17.0.10          bridge
    swp7:VlanA-1         server02   mac:00:02:00:00:00:2a netcat-8082          172.17.0.4           bridge
    swp7:VlanA-1         server02   mac:00:02:00:00:00:2a netcat-8091          172.17.0.13          bridge
    swp7:VlanA-1         server02   mac:00:02:00:00:00:2a netcat-8090          172.17.0.12          bridge
    swp7:VlanA-1         server02   mac:00:02:00:00:00:2a netcat-8087          172.17.0.9           bridge
    swp8:VlanA-1         server03   mac:00:02:00:00:00:2d netcat-8091          172.17.0.13          bridge
    swp8:VlanA-1         server03   mac:00:02:00:00:00:2d netcat-8083          172.17.0.5           bridge
    swp8:VlanA-1         server03   mac:00:02:00:00:00:2d netcat-8087          172.17.0.9           bridge
    swp8:VlanA-1         server03   mac:00:02:00:00:00:2d netcat-8082          172.17.0.4           bridge
    swp8:VlanA-1         server03   mac:00:02:00:00:00:2d netcat-8080          172.17.0.2           bridge
    swp8:VlanA-1         server03   mac:00:02:00:00:00:2d netcat-8092          172.17.0.14          bridge
    swp8:VlanA-1         server03   mac:00:02:00:00:00:2d netcat-8086          172.17.0.8           bridge
    swp8:VlanA-1         server03   mac:00:02:00:00:00:2d netcat-8084          172.17.0.6           bridge
    swp8:VlanA-1         server03   mac:00:02:00:00:00:2d netcat-8088          172.17.0.10          bridge
    swp8:VlanA-1         server03   mac:00:02:00:00:00:2d netcat-8090          172.17.0.12          bridge
    swp8:VlanA-1         server03   mac:00:02:00:00:00:2d netcat-8085          172.17.0.7           bridge
    swp8:VlanA-1         server03   mac:00:02:00:00:00:2d netcat-8089          172.17.0.11          bridge
    swp8:VlanA-1         server03   mac:00:02:00:00:00:2d netcat-8081          172.17.0.3           bridge

You can filter this output for a given interface:

    cumulus@leaf01:~$ netq leaf01 show docker container adjacent interfaces swp6
    Interface            Peer Node  Peer Interface        Container Name       IP                   Network    Service Name
    -------------------- ---------- --------------------- -------------------- -------------------- ---------- ---------------
    swp6:VlanA-1         server01   mac:00:02:00:00:00:27 netcat-9090                               host
    swp6:VlanA-1         server01   mac:00:02:00:00:00:27 netcat-9082                               host
    swp6:VlanA-1         server01   mac:00:02:00:00:00:27 netcat-9091                               host
    swp6:VlanA-1         server01   mac:00:02:00:00:00:27 netcat-9086                               host
    swp6:VlanA-1         server01   mac:00:02:00:00:00:27 netcat-9081                               host
    swp6:VlanA-1         server01   mac:00:02:00:00:00:27 netcat-9083                               host
    swp6:VlanA-1         server01   mac:00:02:00:00:00:27 netcat-9087                               host
    swp6:VlanA-1         server01   mac:00:02:00:00:00:27 netcat-9088                               host
    swp6:VlanA-1         server01   mac:00:02:00:00:00:27 netcat-9085                               host
    swp6:VlanA-1         server01   mac:00:02:00:00:00:27 netcat-9080                               host
    swp6:VlanA-1         server01   mac:00:02:00:00:00:27 netcat-9084                               host
    swp6:VlanA-1         server01   mac:00:02:00:00:00:27 netcat-9089                               host                                7
    swp6:VlanA-1         server01   mac:00:02:00:00:00:27 netcat-9092                               host

And you can go back in time to check adjacency around a given moment:

    cumulus@leaf01:~$ netq leaf01 show docker container adjacent around 1h
    Interface            Peer Node  Peer Interface        Container Name       IP                   Network    Service Name
    -------------------- ---------- --------------------- -------------------- -------------------- ---------- ---------------
    swp6:VlanA-1         server01   mac:00:02:00:00:00:27 netcat-9090                               host
    swp6:VlanA-1         server01   mac:00:02:00:00:00:27 netcat-9082                               host
    swp6:VlanA-1         server01   mac:00:02:00:00:00:27 netcat-9091                               host
    swp6:VlanA-1         server01   mac:00:02:00:00:00:27 netcat-9086                               host
    swp6:VlanA-1         server01   mac:00:02:00:00:00:27 netcat-9081                               host
    swp6:VlanA-1         server01   mac:00:02:00:00:00:27 netcat-9083                               host
    swp6:VlanA-1         server01   mac:00:02:00:00:00:27 netcat-9087                               host
    swp6:VlanA-1         server01   mac:00:02:00:00:00:27 netcat-9088                               host
    swp6:VlanA-1         server01   mac:00:02:00:00:00:27 netcat-9085                               host
    swp6:VlanA-1         server01   mac:00:02:00:00:00:27 netcat-9080                               host
    swp6:VlanA-1         server01   mac:00:02:00:00:00:27 netcat-9084                               host
    swp6:VlanA-1         server01   mac:00:02:00:00:00:27 netcat-9089                               host
    swp6:VlanA-1         server01   mac:00:02:00:00:00:27 netcat-9092                               host
    swp7:VlanA-1         server02   mac:00:02:00:00:00:2a netcat-8089          172.17.0.11          bridge
    swp7:VlanA-1         server02   mac:00:02:00:00:00:2a netcat-8084          172.17.0.6           bridge
    swp7:VlanA-1         server02   mac:00:02:00:00:00:2a netcat-8092          172.17.0.14          bridge
    swp7:VlanA-1         server02   mac:00:02:00:00:00:2a netcat-8083          172.17.0.5           bridge
    swp7:VlanA-1         server02   mac:00:02:00:00:00:2a netcat-8085          172.17.0.7           bridge
    swp7:VlanA-1         server02   mac:00:02:00:00:00:2a netcat-8081          172.17.0.3           bridge
    swp7:VlanA-1         server02   mac:00:02:00:00:00:2a netcat-8080          172.17.0.2           bridge
    swp7:VlanA-1         server02   mac:00:02:00:00:00:2a netcat-8086          172.17.0.8           bridge
    swp7:VlanA-1         server02   mac:00:02:00:00:00:2a netcat-8088          172.17.0.10          bridge
    swp7:VlanA-1         server02   mac:00:02:00:00:00:2a netcat-8082          172.17.0.4           bridge
    swp7:VlanA-1         server02   mac:00:02:00:00:00:2a netcat-8091          172.17.0.13          bridge
    swp7:VlanA-1         server02   mac:00:02:00:00:00:2a netcat-8090          172.17.0.12          bridge
    swp7:VlanA-1         server02   mac:00:02:00:00:00:2a netcat-8087          172.17.0.9           bridge
    swp8:VlanA-1         server03   mac:00:02:00:00:00:2d netcat-8091          172.17.0.13          bridge
    swp8:VlanA-1         server03   mac:00:02:00:00:00:2d netcat-8083          172.17.0.5           bridge
    swp8:VlanA-1         server03   mac:00:02:00:00:00:2d netcat-8087          172.17.0.9           bridge
    swp8:VlanA-1         server03   mac:00:02:00:00:00:2d netcat-8082          172.17.0.4           bridge
    swp8:VlanA-1         server03   mac:00:02:00:00:00:2d netcat-8080          172.17.0.2           bridge
    swp8:VlanA-1         server03   mac:00:02:00:00:00:2d netcat-8092          172.17.0.14          bridge
    swp8:VlanA-1         server03   mac:00:02:00:00:00:2d netcat-8086          172.17.0.8           bridge
    swp8:VlanA-1         server03   mac:00:02:00:00:00:2d netcat-8084          172.17.0.6           bridge
    swp8:VlanA-1         server03   mac:00:02:00:00:00:2d netcat-8088          172.17.0.10          bridge
    swp8:VlanA-1         server03   mac:00:02:00:00:00:2d netcat-8090          172.17.0.12          bridge
    swp8:VlanA-1         server03   mac:00:02:00:00:00:2d netcat-8085          172.17.0.7           bridge
    swp8:VlanA-1         server03   mac:00:02:00:00:00:2d netcat-8089          172.17.0.11          bridge
    swp8:VlanA-1         server03   mac:00:02:00:00:00:2d netcat-8081          172.17.0.3           bridge

## Showing Container-specific Information</span>

You can see information about a given container by running `netq show
docker container name NAME`:

    cumulus@server01:~$ netq show docker container name netcat-9092
    Name                 Node       IP                IP Masq. Network        Service Name    Up time
    -------------------- ---------- ----------------- -------- -------------- --------------- ---------------
    netcat-9092          exit01     45.0.0.17/26,     False    host                           0:34:15
                                    27.0.0.3/32,
                                    192.168.0.15/24

## Showing Containers with a Specific Image</span>

To search for all the containers on the network with a specific Docker
image, run `netq show docker container image IMAGE_NAME`:

    cumulus@server01:~$ netq show docker container image chilcano/netcat:jessie 
    Name                 Node       IP                IP Masq. Network        Service Name    Up time
    -------------------- ---------- ----------------- -------- -------------- --------------- ---------------
    netcat-8080          exit01     172.17.0.2        True     bridge                         0:32:09
    netcat-8080          server01   172.17.0.2        True     bridge                         0:23:11
    netcat-8081          exit01     172.17.0.3        True     bridge                         0:32:07
    netcat-8081          server01   172.17.0.3        True     bridge                         0:23:10
    netcat-8082          exit01     172.17.0.4        True     bridge                         0:32:08
    netcat-8082          server01   172.17.0.4        True     bridge                         0:23:08
    netcat-8083          exit01     172.17.0.5        True     bridge                         0:32:07
    netcat-8083          server01   172.17.0.5        True     bridge                         0:23:07
    netcat-8084          exit01     172.17.0.6        True     bridge                         0:32:07
    netcat-8084          server01   172.17.0.6        True     bridge                         0:23:09
    netcat-8085          exit01     172.17.0.7        True     bridge                         0:32:05
    netcat-8085          server01   172.17.0.7        True     bridge                         0:23:06
    netcat-8086          exit01     172.17.0.8        True     bridge                         0:32:06
    netcat-8086          server01   172.17.0.8        True     bridge                         0:23:06
    netcat-8087          exit01     172.17.0.9        True     bridge                         0:32:05
    netcat-8087          server01   172.17.0.9        True     bridge                         0:23:06
    netcat-8088          exit01     172.17.0.10       True     bridge                         0:32:04
    netcat-8088          server01   172.17.0.10       True     bridge                         0:23:06
    netcat-8089          exit01     172.17.0.11       True     bridge                         0:32:02
    netcat-8089          server01   172.17.0.11       True     bridge                         0:23:03
    netcat-8090          exit01     172.17.0.12       True     bridge                         0:32:01
    netcat-8090          server01   172.17.0.12       True     bridge                         0:23:05
    netcat-8091          exit01     172.17.0.13       True     bridge                         0:32:03
    netcat-8091          server01   172.17.0.13       True     bridge                         0:23:04
    netcat-8092          exit01     172.17.0.14       True     bridge                         0:31:59
    netcat-8092          server01   172.17.0.14       True     bridge                         0:23:03
    netcat-9080          exit01     45.0.0.17/26,     False    host                           0:31:51
                                    27.0.0.3/32,
                                    192.168.0.15/24
    netcat-9081          exit01     45.0.0.17/26,     False    host                           0:31:51
                                    27.0.0.3/32,
                                    192.168.0.15/24
    netcat-9082          exit01     45.0.0.17/26,     False    host                           0:31:52
                                    27.0.0.3/32,
                                    192.168.0.15/24
    netcat-9083          exit01     45.0.0.17/26,     False    host                           0:31:49
                                    27.0.0.3/32,
                                    192.168.0.15/24
    netcat-9084          exit01     45.0.0.17/26,     False    host                           0:31:50
                                    27.0.0.3/32,
                                    192.168.0.15/24
    netcat-9085          exit01     45.0.0.17/26,     False    host                           0:31:50
                                    27.0.0.3/32,
                                    192.168.0.15/24
    netcat-9086          exit01     45.0.0.17/26,     False    host                           0:31:48
                                    27.0.0.3/32,
                                    192.168.0.15/24
    netcat-9087          exit01     45.0.0.17/26,     False    host                           0:31:48
                                    27.0.0.3/32,
                                    192.168.0.15/24
    netcat-9088          exit01     45.0.0.17/26,     False    host                           0:31:47
                                    27.0.0.3/32,
                                    192.168.0.15/24
    netcat-9089          exit01     45.0.0.17/26,     False    host                           0:31:48
                                    27.0.0.3/32,
                                    192.168.0.15/24
    netcat-9090          exit01     45.0.0.17/26,     False    host                           0:31:46
                                    27.0.0.3/32,
                                    192.168.0.15/24
    netcat-9091          exit01     45.0.0.17/26,     False    host                           0:31:47
                                    27.0.0.3/32,
                                    192.168.0.15/24
    netcat-9092          exit01     45.0.0.17/26,     False    host                           0:31:47
                                    27.0.0.3/32,
                                    192.168.0.15/24

## Showing Container Connectivity</span>

To determine how a particular container is attached to a network, run
`netq HOST show docker container network NAME connectivity`. The output
tells you what host it's launched on, adjacent nodes, adjacent ports.

    cumulus@leaf01:~$ netq server01 show docker container network host connectivity 
    Name            Swarm Service Cont IP         Network    Node       Port                 Peer Node  Peer Port
    --------------- ------------- --------------- ---------- ---------- -------------------- ---------- --------------------
    netcat-9080                                   host       server01   swp2:NetQBond-1      noc-pr     swp21:NetQBond-19
    netcat-9080                                   host       server01   swp3:NetQBond-1      noc-se     swp21:NetQBond-19
    netcat-9080                                   host       server01   swp1:swp1            tor-1      Local Node tor-1 and
                                                                                                        Ports swp6 <==> Remo
                                                                                                        te  Node/s hosts-11
                                                                                                        and Ports swp1
    netcat-9081                                   host       server01   swp2:NetQBond-1      noc-pr     swp21:NetQBond-19
    netcat-9081                                   host       server01   swp3:NetQBond-1      noc-se     swp21:NetQBond-19
    netcat-9081                                   host       server01   swp1:swp1            tor-1      Local Node tor-1 and
                                                                                                        Ports swp6 <==> Remo
                                                                                                        te  Node/s hosts-11
                                                                                                        and Ports swp1
    netcat-9082                                   host       server01   swp2:NetQBond-1      noc-pr     swp21:NetQBond-19
    netcat-9082                                   host       server01   swp3:NetQBond-1      noc-se     swp21:NetQBond-19
    netcat-9082                                   host       server01   swp1:swp1            tor-1      Local Node tor-1 and
                                                                                                        Ports swp6 <==> Remo
                                                                                                        te  Node/s hosts-11
                                                                                                        and Ports swp1
    netcat-9083                                   host       server01   swp2:NetQBond-1      noc-pr     swp21:NetQBond-19
    netcat-9083                                   host       server01   swp3:NetQBond-1      noc-se     swp21:NetQBond-19
    netcat-9083                                   host       server01   swp1:swp1            tor-1      Local Node tor-1 and
                                                                                                        Ports swp6 <==> Remo
                                                                                                        te  Node/s hosts-11
                                                                                                        and Ports swp1
    netcat-9084                                   host       server01   swp2:NetQBond-1      noc-pr     swp21:NetQBond-19
    netcat-9084                                   host       server01   swp3:NetQBond-1      noc-se     swp21:NetQBond-19
    netcat-9084                                   host       server01   swp1:swp1            tor-1      Local Node tor-1 and
                                                                                                        Ports swp6 <==> Remo
                                                                                                        te  Node/s hosts-11
                                                                                                        and Ports swp1
    netcat-9085                                   host       server01   swp2:NetQBond-1      noc-pr     swp21:NetQBond-19
    netcat-9085                                   host       server01   swp3:NetQBond-1      noc-se     swp21:NetQBond-19
    netcat-9085                                   host       server01   swp1:swp1            tor-1      Local Node tor-1 and
                                                                                                        Ports swp6 <==> Remo
                                                                                                        te  Node/s hosts-11
                                                                                                        and Ports swp1
    netcat-9086                                   host       server01   swp2:NetQBond-1      noc-pr     swp21:NetQBond-19
    netcat-9086                                   host       server01   swp3:NetQBond-1      noc-se     swp21:NetQBond-19
    netcat-9086                                   host       server01   swp1:swp1            tor-1      Local Node tor-1 and
                                                                                                        Ports swp6 <==> Remo
                                                                                                        te  Node/s hosts-11
                                                                                                        and Ports swp1
    netcat-9087                                   host       server01   swp2:NetQBond-1      noc-pr     swp21:NetQBond-19
    netcat-9087                                   host       server01   swp3:NetQBond-1      noc-se     swp21:NetQBond-19
    netcat-9087                                   host       server01   swp1:swp1            tor-1      Local Node tor-1 and
                                                                                                        Ports swp6 <==> Remo
                                                                                                        te  Node/s hosts-11
                                                                                                        and Ports swp1
    netcat-9088                                   host       server01   swp2:NetQBond-1      noc-pr     swp21:NetQBond-19
    netcat-9088                                   host       server01   swp3:NetQBond-1      noc-se     swp21:NetQBond-19
    netcat-9088                                   host       server01   swp1:swp1            tor-1      Local Node tor-1 and
                                                                                                        Ports swp6 <==> Remo
                                                                                                        te  Node/s hosts-11
                                                                                                        and Ports swp1
    netcat-9089                                   host       server01   swp2:NetQBond-1      noc-pr     swp21:NetQBond-19
    netcat-9089                                   host       server01   swp3:NetQBond-1      noc-se     swp21:NetQBond-19
    netcat-9089                                   host       server01   swp1:swp1            tor-1      Local Node tor-1 and
                                                                                                        Ports swp6 <==> Remo
                                                                                                        te  Node/s hosts-11
                                                                                                        and Ports swp1
    netcat-9090                                   host       server01   swp2:NetQBond-1      noc-pr     swp21:NetQBond-19
    netcat-9090                                   host       server01   swp3:NetQBond-1      noc-se     swp21:NetQBond-19
    netcat-9090                                   host       server01   swp1:swp1            tor-1      Local Node tor-1 and
                                                                                                        Ports swp6 <==> Remo
                                                                                                        te  Node/s hosts-11
                                                                                                        and Ports swp1
    netcat-9091                                   host       server01   swp2:NetQBond-1      noc-pr     swp21:NetQBond-19
    netcat-9091                                   host       server01   swp3:NetQBond-1      noc-se     swp21:NetQBond-19
    netcat-9091                                   host       server01   swp1:swp1            tor-1      Local Node tor-1 and
                                                                                                        Ports swp6 <==> Remo
                                                                                                        te  Node/s hosts-11
                                                                                                        and Ports swp1
    netcat-9092                                   host       server01   swp2:NetQBond-1      noc-pr     swp21:NetQBond-19
    netcat-9092                                   host       server01   swp3:NetQBond-1      noc-se     swp21:NetQBond-19
    netcat-9092                                   host       server01   swp1:swp1            tor-1      Local Node tor-1 and
                                                                                                        Ports swp6 <==> Remo
                                                                                                        te  Node/s hosts-11
                                                                                                        and Ports swp1

## Checking Network Traffic over a Given Protocol</span>

You can include the protocol when you observe a given flow of traffic on
the network and want to identify which container sent or received
traffic using that protocol from a given port.

    cumulus@tor-1:mgmt-vrf:~$ netq hosts-11 show docker container 6.0.1.5 tcp 
    Container Name       Node       Proto  Port     Cont IP           Network        Host IP               Host Port
    -------------------- ---------- ------ -------- ----------------- -------------- --------------------- ------------
    netcat-9080          server01   tcp    9192                       host           6.0.1.5/26:swp1.1004  9192
    netcat-9080          server01   tcp    8182                       host           6.0.1.5/26:swp1.1004  8182
    netcat-9081          server01   tcp    9192                       host           6.0.1.5/26:swp1.1004  9192
    netcat-9081          server01   tcp    8182                       host           6.0.1.5/26:swp1.1004  8182
    netcat-9082          server01   tcp    8182                       host           6.0.1.5/26:swp1.1004  8182
    netcat-9082          server01   tcp    9192                       host           6.0.1.5/26:swp1.1004  9192
    netcat-9083          server01   tcp    8182                       host           6.0.1.5/26:swp1.1004  8182
    netcat-9083          server01   tcp    9192                       host           6.0.1.5/26:swp1.1004  9192
    netcat-9084          server01   tcp    9192                       host           6.0.1.5/26:swp1.1004  9192
    netcat-9084          server01   tcp    8182                       host           6.0.1.5/26:swp1.1004  8182
    netcat-9085          server01   tcp    8182                       host           6.0.1.5/26:swp1.1004  8182
    netcat-9085          server01   tcp    9192                       host           6.0.1.5/26:swp1.1004  9192
    netcat-9086          server01   tcp    9192                       host           6.0.1.5/26:swp1.1004  9192
    netcat-9086          server01   tcp    8182                       host           6.0.1.5/26:swp1.1004  8182
    netcat-9087          server01   tcp    9192                       host           6.0.1.5/26:swp1.1004  9192
    netcat-9087          server01   tcp    8182                       host           6.0.1.5/26:swp1.1004  8182
    netcat-9088          server01   tcp    9192                       host           6.0.1.5/26:swp1.1004  9192
    netcat-9088          server01   tcp    8182                       host           6.0.1.5/26:swp1.1004  8182
    netcat-9089          server01   tcp    8182                       host           6.0.1.5/26:swp1.1004  8182
    netcat-9089          server01   tcp    9192                       host           6.0.1.5/26:swp1.1004  9192
    netcat-9090          server01   tcp    8182                       host           6.0.1.5/26:swp1.1004  8182
    netcat-9090          server01   tcp    9192                       host           6.0.1.5/26:swp1.1004  9192
    netcat-9091          server01   tcp    9192                       host           6.0.1.5/26:swp1.1004  9192
    netcat-9091          server01   tcp    8182                       host           6.0.1.5/26:swp1.1004  8182
    netcat-9092          server01   tcp    9192                       host           6.0.1.5/26:swp1.1004  9192
    netcat-9092          server01   tcp    8182                       host           6.0.1.5/26:swp1.1004  8182
