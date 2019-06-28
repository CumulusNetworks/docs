---
title: Installing FRRouting on the Host
author: Cumulus Networks
weight: 11
aliases:
 - /display/HOSTPACK/Installing+FRRouting+on+the+Host
 - /pages/viewpage.action?pageId=5868795
pageID: 5868795
product: Cumulus Host Pack
version: '1.0'
imgData: host-pack
siteSlug: host-pack
---
To use Host Pack to bring routing to your host servers, you must install
the FRRouting (FRR) package on those servers. FRRouting on the Host is
supported in the following environments:

  - Ubuntu 14.04-LTS, Trusty Tahr

  - Ubuntu 16.04-LTS, Xenial Xerus

  - Red Hat Enterprise Linux 7

  - CentOS 7

  - Docker containers

## <span>Install the FRR Package on a Bare Metal Server</span>

1.  If FRRouting is already installed on the host, you must uninstall
    that package before you install FRR.
    
      - **Ubuntu hosts:**
        
            root@host:~# dpkg -r frr
    
      - **RHEL 7 or CentOS 7 hosts:**
        
            root@host:~# rpm --erase frr

2.  Install the repository key.
    
      - **Ubuntu hosts:**
        
            root@host:~# wget -O- https://apps3.cumulusnetworks.com/setup/cumulus-apps-deb.pubkey | apt-key add -
    
      - **RHEL 7 or CentOS 7 hosts:**
        
            root@host:~# rpm --import https://apps3.cumulusnetworks.com/setup/cumulus-apps-rpm.pubkey

3.  Add the software repository. Copy and paste the command below to
    create a repo file to add the Cumulus Networks apps3 repository.
    
      - **Ubuntu hosts:**
        
            root@host:~# echo "deb [arch=amd64] https://apps3.cumulusnetworks.com/repos/deb $(lsb_release -cs) roh-3" >> /etc/apt/sources.list.d/cumulus-apps-deb-$(lsb_release -cs).list
    
      - **RHEL 7 or CentOS 7 hosts:**
        
            root@host:~# cat << EOT > /etc/yum.repos.d/cumulus-host-el.repo
            [cumulus-arch-roh-3]
            name=Cumulus roh packages
            baseurl=https://apps3.cumulusnetworks.com/repos/rpm/el/7/roh-3/x86_64/
            gpgcheck=1
            enabled=1
            EOT

4.  Install the FRRouting software.
    
      - **Ubuntu hosts:  
        **
        
            root@host:~# apt-get update && apt-get install frr
    
      - **RHEL 7 or CentOS 7 hosts:**
        
            root@host:~# yum install frr

5.  Create a `sysctl` text file, `/etc/sysctl.d/99frr_defaults.conf`,
    and populate it with the following content. The `sysctl` settings
    provided here makes routing perform better on the system.
    
        # /etc/sysctl.d/99frr_defaults.conf
        # Place this file at the location above and reload the device.
        # or run the sysctl -p /etc/sysctl.d/99frr_defaults.conf
          
        # Enables IPv4/IPv6 Routing
        net.ipv4.ip_forward = 1
        net.ipv6.conf.all.forwarding=1
         
        # Routing
        net.ipv6.route.max_size=131072
        net.ipv4.conf.all.ignore_routes_with_linkdown=1
        net.ipv6.conf.all.ignore_routes_with_linkdown=1
         
         
        # Best Settings for Peering w/ BGP Unnumbered
        #    and OSPF Neighbors
        net.ipv4.conf.all.rp_filter = 0
        net.ipv4.conf.default.rp_filter = 0
        net.ipv4.conf.lo.rp_filter = 0
        net.ipv4.conf.all.forwarding = 1
        net.ipv4.conf.default.forwarding = 1
        net.ipv4.conf.default.arp_announce = 2
        net.ipv4.conf.default.arp_notify = 1
        net.ipv4.conf.default.arp_ignore=1
        net.ipv4.conf.all.arp_announce = 2
        net.ipv4.conf.all.arp_notify = 1
        net.ipv4.conf.all.arp_ignore=1
        net.ipv4.icmp_errors_use_inbound_ifaddr=1
         
        # Miscellaneous Settings
         
        #   Keep ipv6 permanent addresses on an admin down
        net.ipv6.conf.all.keep_addr_on_down=1
         
        # igmp
        net.ipv4.igmp_max_memberships=1000
        net.ipv4.neigh.default.mcast_solicit = 10
         
        # MLD
        net.ipv6.mld_max_msf=512
         
        # Garbage Collection Settings for ARP and Neighbors
        net.ipv4.neigh.default.gc_thresh2=7168
        net.ipv4.neigh.default.gc_thresh3=8192
        net.ipv4.neigh.default.base_reachable_time_ms=14400000
        net.ipv6.neigh.default.gc_thresh2=3584
        net.ipv6.neigh.default.gc_thresh3=4096
        net.ipv6.neigh.default.base_reachable_time_ms=14400000
         
        # Use neigh information on selection of nexthop for multipath hops
        net.ipv4.fib_multipath_use_neigh=1
         
        # Allows Apps to Work with VRF
        net.ipv4.tcp_l3mdev_accept=1

6.  Load the new `sysctl` file.
    
        root@host:~# sysctl -p /etc/sysctl.d/99frr_defaults.conf
    
    {{%notice note%}}
    
    Depending on your kernel version and configuration, certain
    variables might not exist and show "No such file or directory"
    errors. This is expected and can be ignored.
    
    {{%/notice%}}

7.  Enable the daemons you intend to use (such as `bgpd`, `ospfd` or
    `ospf6d`). For more information, see [Configuring FRRouting on the
    Host](/host-pack/Configuring_FRRouting_on_the_Host).

8.  Start the FRR service.

<!-- end list -->

  - **Ubuntu 14.04 hosts:**
    
        root@host:~# service frr restart

  - **Ubuntu 16.04, RHEL 7 or CentOS 7 hosts:**
    
        root@host:~# systemctl start frr.service

## <span id="src-5868795_InstallingFRRoutingontheHost-container" class="confluence-anchor-link"></span><span>Start the Cumulus Host Pack FRR Docker Container</span>

{{%notice note%}}

Before you can use the Cumulus Host Pack FRR Docker container, you must
[install Docker](/host-pack/Installing_Docker).

{{%/notice%}}

{{%notice note%}}

If you install FRR inside a container, NetQ cannot retrieve any
FRR-related data from the container.

{{%/notice%}}

The following steps were done on an Ubuntu 16.04 host.

1.  **Optional:** Pull the FRR container image from the Cumulus Networks
    hub. If you do not pull the image here, it will be done for you
    automatically in the next step.
    
        root@host:/etc/apt/sources.list.d# docker pull hub.cumulusnetworks.com/chp-roh:latest
    
    Click to see the output ...
    
        latest: Pulling from hub.cumulusnetworks.com/chp-roh:latest
        5ba4f30e5bea: Pull complete 
        9d7d19c9dc56: Pull complete 
        ac6ad7efd0f9: Pull complete 
        e7491a747824: Pull complete 
        a3ed95caeb02: Pull complete 
        a2e15afd186f: Pull complete 
        c79a17f1dd48: Pull complete 
        b9ce745e3bfd: Pull complete 
        871c6c942d89: Pull complete 
        0295811cd443: Pull complete 
        6aaf3dc92cbd: Pull complete 
        e6e55669dd82: Pull complete 
        e3a986b5efb0: Pull complete 
        dd11dcae39d1: Pull complete 
        2feeda2bf3a6: Pull complete 
        Digest: sha256:dcabf5df4f631719a709bf84f1536d91ebd2d0c115f97b55090c9afaefac5657
        Status: Downloaded newer image for hub.cumulusnetworks.com/chp-roh:latest

2.  Create the container.
    
    1.  Create the container in privileged mode, naming it *FRR*. The
        container ID gets returned even if you specify a name, as you
        can see in the example below.
        
            root@host:/root# docker run -t -d --net=host --privileged --restart unless-stopped --name FRR hub.cumulusnetworks.com/chp-roh:latest cf0daeb70ceaf32d15b3fd27f80a355b3e88b178f7d7d53840c395d93e568a73
        
        {{%notice note%}}
        
        The container must run in privileged mode to interact with the
        kernel routing table.
        
        {{%/notice%}}
    
    2.  **Optional:** To create the container using a custom `frr.conf`
        configuration or with daemons other than BGP enabled, run the
        container while mounting files as volumes, as shown below.
        
            root@host:/etc/apt/sources.list.d# docker run -t -d --net=host --privileged --restart unless-stopped --name FRR \
                -v /root/frr.conf:/etc/frr/frr.conf \
                -v /root/daemons:/etc/frr/daemons \
                hub.cumulusnetworks.com/chp-roh:latest

3.  Validate the container.
    
    1.  Check all containers on the system.
        
            root@host:/root# docker ps -a
             
            CONTAINER ID        IMAGE                                    COMMAND             CREATED             STATUS                      PORTS               NAMES
            cf0daeb70cea        hub.cumulusnetworks.com/chp-roh:latest   "/bin/bash"         2 minutes ago       Up 2 minutes                                    FRR
        
        {{%notice tip%}}
        
        Running `docker ps` (without the `-a` option) only shows active
        ("up") containers on the system; the `-a` option shows all
        containers.
        
        {{%/notice%}}
    
    2.  Check the configuration on the container.
        
            root@host:/root# docker exec -i -t FRR /usr/bin/vtysh
            Hello, this is FRR (version 0.99.23.1+cl3u2).
            Copyright 1996-2005 Kunihiro Ishiguro, et al.
            host# show run
            Building configuration...
            Current configuration:
            !
            username cumulus nopassword
            !
            service integrated-vtysh-config
            !
            interface docker0
             ipv6 nd suppress-ra
             link-detect
            !
            interface lo
             link-detect
            !
            interface veth0c6e8a7
             link-detect
            !
            ip forwarding
            !
            line vty
            !
            end
            host#

## <span>Configure FRR</span>

Once you have finished installing FRR on your servers or in your
containers, you are ready to [configure
FRR](/host-pack/Configuring_FRRouting_on_the_Host).
