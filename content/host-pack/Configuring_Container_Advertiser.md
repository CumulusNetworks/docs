---
title: Configuring Container Advertiser
author: Cumulus Networks
weight: 21
aliases:
 - /display/HOSTPACK/Configuring+Container+Advertiser
 - /pages/viewpage.action?pageId=7110691
pageID: 7110691
product: Cumulus Host Pack
version: '1.0'
imgData: host-pack
siteSlug: host-pack
---
Container Advertiser and FRRouting (FRR) work together on the host to
advertise containers into the routed fabric.

## <span>Container Advertiser Architecture</span>

As Docker creates and destroys containers, the Container Advertiser
listens to the docker-engine API events stream. When a container
creation event is detected, a corresponding /32 host route is created in
table 30 of the Linux kernel routing tables. Similarly, when a container
destruction event is detected, the corresponding /32 host route is
removed.

Once the route is created, FRR sees the newly added route in the kernel
routing table and redistributes the route into BGP or OSPF depending
upon which [routing protocol you
enabled](/host-pack/Configuring_FRRouting_on_the_Host). This demo uses
BGP unnumbered as the routing protocol. Using BGP unnumbered in this
scenario means that no IPv4 addresses need to be configured on the
uplinks from the server.

{{% imgOld 0 %}}

### <span>Redistribute the Container Routing Table into FRRouting</span>

The following sample configuration — stored in the `/etc/frr/frr.conf`
file — demonstrates how you can advertise containers using FRRouting.

    frr defaults datacenter
    ip import-table 30
    username cumulus nopassword
    !
    service integrated-vtysh-config
    !
    log syslog informational
    !
    interface eth1
     ipv6 nd ra-interval 10
     no ipv6 nd suppress-ra
    !
    interface eth2
     ipv6 nd ra-interval 10
     no ipv6 nd suppress-ra
    !
    router bgp 65000
     bgp bestpath as-path multipath-relax
     neighbor eth1 interface remote-as external
     neighbor eth2 interface remote-as external
     !
     address-family ipv4 unicast
      redistribute table 30
     exit-address-family
    !
    line vty
    !

### <span>Supported Docker Network Driver Types</span>

When using Docker, containers can be attached to custom user-created
networks, as in the example network created below.

    user@host:~$ docker network create --driver=bridge --subnet 172.18.0.0/24 --gateway 172.18.0.254 \
    --opt  'com.docker.network.bridge.name=docker-newnet' \
    --opt  'com.docker.network.bridge.enable_icc=true' \
    --opt  'com.docker.network.bridge.enable_ip_masquerade=false' \
    new_network

Container Advertiser only advertises IP addresses from containers that
are on Docker bridges with NAT disabled, as shown in the example above.

Container Advertiser only supports the advertisement of containers
attached to networks created with one of two drivers: *bridge* and
*macvlan*.

## <span>Run Container Advertiser</span>

The container advertiser can be used on the host, just like any other
container.

1.  **Optional:** Pull the Container Advertiser image from the Cumulus
    Networks hub. If you don't pull the image here, it will be done in
    the next step for you automatically.
    
        user@host:~$ curl -X GET  https://hub.cumulusnetworks.com/v2/_catalog
    
    Click to see the output ...
    
        user@host:~$ sudo docker pull hub.cumulusnetworks.com/chp-crohdad:latest
        latest: Pulling from chp-roh
        ae79f2514705: Pull complete 
        5ad56d5fc149: Pull complete 
        170e558760e8: Pull complete 
        395460e233f5: Pull complete 
        6f01dc62e444: Pull complete 
        f417f88fae3f: Pull complete 
        e8c477c3664b: Pull complete 
        53ab13163b7a: Pull complete 
        16ea638db969: Pull complete 
        266b626a7906: Pull complete 
        385fd54db587: Pull complete 
        cba74222fa7e: Pull complete 
        6b7f7e0b8547: Pull complete 
        fa063c8b0c0a: Pull complete 
        Digest: sha256:557168b6728aa44305f7d1099769acc98e246c64369ebe59fb53bac23aa40dfb
        Status: Downloaded newer image for hub.cumulusnetworks.com/chp-crohdad:latest

2.  Start the container.
    
    1.  Create the container in privileged mode, naming the container
        *crohdad*.
        
            user@host:~$ docker run -t -d --net=host --privileged --restart unless-stopped \
                 -v /var/run/docker.sock:/var/run/docker.sock \
                 -v /etc/iproute2/rt_tables:/etc/iproute2/rt_tables \
                 -v /dev/log:/dev/log \
                --name crohdad hub.cumulusnetworks.com/chp-crohdad:latest
        
        {{%notice note%}}
        
        The container must run in privileged mode to interact with the
        Linux kernel to create the new routing table (table 30 by
        default) and populate /32 host routes into that table.
        
        {{%/notice%}}

3.  Validate the container is running.
    
    1.  Check all containers on the system.
        
            user@host:~$ docker ps -a
            CONTAINER ID        IMAGE                                        COMMAND                  CREATED             STATUS              PORTS               NAMES
            dcfbe94e9502        hub.cumulusnetworks.com/chp-crohdad:latest   "/usr/bin/crohdad_..."   25 seconds ago      Up 24 seconds                           crohdad
        
        {{%notice note%}}
        
        Running `docker ps` (without the `-a` option) only shows active
        ("up") containers on the system; the `-a` option shows all
        containers.
        
        {{%/notice%}}
    
    2.  View logs from the container.
        
            user@host:~$ docker logs crohdad
            RUNNING CRoHDAd: /root/crohdad.py  &
            ################################################
            #                                              #
            #     Cumulus Routing On the Host              #
            #       Docker Advertisement Daemon            #
            #             --cRoHDAd--                      #
            #         originally written by Eric Pulvino   #
            #                                              #
            ################################################
             STARTING UP.
                *Adding All Host Routes to Table 30*
                  Run "ip route show table 30" to see routes.
                Flushing any pre-existing routes from table 30.
             
              Auto-Detecting existing containers and adding host routes...
              Listening for Container Activity...
             
            [hit enter key to exit] or run 'docker stop <container>'

## <span>Container Advertiser Options</span>

The container advertiser has a number of different options that can be
specified. By default it starts with no additional options defined. To
see all available options <span style="color: #000000;"> run the
following command: </span>

    user@host:~$ docker run -it --name=crohdad hub.cumulusnetworks.com/chp-crohdad:latest -h

### <span>Write Events to the Host syslog</span>

Container Advertiser attempts to write events to the host `syslog` by
default if the `/dev/log` file is available inside the container.

To disable this functionality use the `-l` flag.

    user@host:~$ docker run -t -d --net=host --privileged \
         -v /var/run/docker.sock:/var/run/docker.sock \
         -v /etc/iproute2/rt_tables:/etc/iproute2/rt_tables \
        --name crohdad hub.cumulusnetworks.com/chp-crohdad:latest -l

{{%notice note%}}

When using the `-l` flag, the volume mount for the `/dev/log` file is
not required.

{{%/notice%}}

### <span>Control Container Advertisement by Subnet</span>

Container Advertiser can be restricted to only advertise containers that
are created/destroyed within specific subnets. By default, all subnets
are advertised.

Subnet advertisements can be restricted using one or more "-s" flags.

    user@host:~$ docker run -t -d --net=host --privileged --restart unless-stopped  \
         -v /var/run/docker.sock:/var/run/docker.sock \
         -v /etc/iproute2/rt_tables:/etc/iproute2/rt_tables \
        --name crohdad hub.cumulusnetworks.com/chp-crohdad:latest -s 172.18.0.0/24 -s 172.19.0.0/24

In the example above, only containers that are created and associated to
IP addresses in the following ranges 172.18.0.0/24 and 172.19.0.0/24
will be advertised.

### <span>View All Supported Options</span>

Run the container with the `-h` flag which displays the help options.

    user@host:~$ docker run -it --name=crohdad hub.cumulusnetworks.com/chp-crohdad:latest -h

Click to see example output...

    user@host:~$ docker run -it --name=crohdad hub.cumulusnetworks.com/chp-crohdad:latest -h
    RUNNING CRoHDAd: /root/crohdad.py -h &
    usage: crohdad.py [-h] [-d] [-f] [-l] [-t TABLE_NUMBER] [-n] [-s SUBNETS] [-v]
     
    Cumulus Routing on the Host Docker Advertisement Daemon (CRoHDAD) -- A Daemon
    to advertise Docker container IP addresses into Routing Fabrics running with
    Quagga/FRR.
     
    optional arguments:
      -h, --help            show this help message and exit
      -d, --debug           enables verbose logging output.
      -f, --no-flush-routes
                            disables table flush of existing host-routes at
                            startup.
      -l, --log-to-syslog-off
                            disable logging to syslog.
      -t TABLE_NUMBER, --table_number TABLE_NUMBER
                            route table number to add/remove host routes (see:
                            /etc/iproute2/rt_tables). Default is 30
      -n, --no-add-on-start
                            automatically detects existing containers and adds
                            their host routes upon initial script start-up.
      -s SUBNETS, --subnets SUBNETS
                            Allows the user to specify the acceptable container
                            subnets which can be advertised via CRoHDAD when seen
                            on containers. Defaults to advertising everything.
                            example ./crohdad.py --subnets 172.19.0.0/24 --subnets
                            172.17.0.0/24
      -v, --version         Using this option displays the version of CRoHDAd and
                            exits.
     
     
    [hit enter key to exit] or run 'docker stop <container>'

## <span>Deploy the Container Advertiser with Ansible</span>

Below is a task for an Ansible playbook that you can use to deploy the
Container Advertiser.

    - name: Deploy Container Advertiser
      docker_container:
        name: crohdad
        privileged: true
        interactive: true
        network_mode: host
        restart_policy: unless-stopped
        tty: true
        recreate: yes
        image: hub.cumulusnetworks.com/chp-crohdad:latest
        volumes:
          - "/var/run/docker.sock:/var/run/docker.sock"
          - "/etc/iproute2/rt_tables:/etc/iproute2/rt_tables"
          - "/dev/log:/dev/log"

{{%notice note%}}

Ansible v2.1 or greater is required to use the `docker_container`
module.

{{%/notice%}}

## <span>Start the Container Advertiser Automatically when the System Boots</span>

This configuration automatically restarts the container if it dies at
any point using standard systemd constructs.

1.  Create the `systemd` unit file
    `/etc/systemd/system/container-advertiser.service` and populate the
    file with the following content.
    
        [Unit]
        Description=Container Advertiser
        After=docker.service network-online.target
        Requires=docker.service
         
        [Service]
        Restart=always
        TimeoutStartSec=0
         
        #One ExecStart/ExecStop line to prevent hitting bugs in certain systemd versions
        ExecStart=/bin/sh -c '/usr/bin/docker rm -f crohdad; \
        /usr/bin/docker pull hub.cumulusnetworks.com/chp-crohdad:latest; \
        /usr/bin/docker run -t --net=host --privileged \
        -v /var/run/docker.sock:/var/run/docker.sock \
        -v /etc/iproute2/rt_tables:/etc/iproute2/rt_tables \
        -v /dev/log:/dev/log \
        --name crohdad hub.cumulusnetworks.com/chp-crohdad:latest'
         
        ExecStop=-/bin/sh -c '/usr/bin/docker stop crohdad; \
        /usr/bin/docker rm -f crohdad'
         
        [Install]
        WantedBy=multi-user.target

2.  Set the container to start at boot time by enabling the
    `container-advertiser` service.
    
        root@host:# systemctl enable container-advertiser.service

3.  **Optional:** Start the Container Advertiser.
    
        root@host:# systemctl start container-advertiser.service

## <span>Further Example Configurations</span>

To see a Vagrant-based demo of the Container Advertiser in action, visit
the [Cumulus Networks GitHub
repository](https://github.com/CumulusNetworks/cldemo-roh-dad).
