---
title: Configuring NetQ on the Host
author: Cumulus Networks
weight: 17
aliases:
 - /display/HOSTPACK/Configuring+NetQ+on+the+Host
 - /pages/viewpage.action?pageId=7110686
pageID: 7110686
product: Cumulus Host Pack
version: '1.0'
imgData: host-pack
siteSlug: host-pack
---
Once you [install the
NetQ packages](/host-pack/Installing_NetQ_on_the_Host) and configure
the NetQ Telemetry Server, you need to configure NetQ on each node
(Linux host) to monitor that node on your network.

1.  To ensure useful output, ensure that
    [NTP](/display/HOSTPACK/Setting+Date+and+Time) is running.

2.  On the host, after you install the NetQ metapackage, restart
    `rsyslog` so logs are sent to the correct destination:
    
        root@host:~# systemctl restart rsyslog

3.  **CentOS, RHEL or Ubuntu hosts only:** Enable and restart the
    `netqd` service:
    
        root@host:~# systemctl enable netqd ; sudo systemctl start netqd

4.  Link the host to the telemetry server you configured previously; in
    the following example, the IP address for the telemetry server host
    is *198.51.100.10*:
    
        root@host:~# netq config add server 198.51.100.10
    
    This command updated the configuration in the
    `/etc/cts/netq/netq.yml` file. It also enables the NetQ CLI.

5.  **Container hosts only:** Enable Docker by adding the following
    three lines to the `netq.yml` file on the container host:
    
        root@host:~# vi /etc/cts/netq/netq.yml
          
        ...
         
        docker:
          enable: true
          poll_period: 15

6.  Restart the `netq` services.
    
        root@host:~# netq config agent restart
    
    {{%notice note%}}
    
    If you see the following error, it means you haven't added the
    telemetry server or the server wasn't configured:
    
        Error: Please specify IP address of DB server
    
    {{%/notice%}}
