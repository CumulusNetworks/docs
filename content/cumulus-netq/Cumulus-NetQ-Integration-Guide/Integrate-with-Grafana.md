---
title: Integrate NetQ with Grafana
author: Cumulus Networks
weight: 202
aliases:
 - /display/NETQ141/Collect+Interface+Statistics
 - /pages/viewpage.action?pageId=10453499
pageID: 10453499
product: Cumulus NetQ
version: 2.3
imgData: cumulus-netq-23
siteSlug: cumulus-netq-23
---
Switches collect statistics about the performance of their interfaces.
The NetQ Agent on each switch collects these statistics every 15 seconds and then sends them to your NetQ
Server or Appliance.

NetQ only collects statistics for physical interfaces; it does not
collect statistics for virtual (non-physical) interfaces, such as bonds, bridges,
and VXLANs. Specifically, the NetQ Agent collects the following
interface statistics:

  - **Transmit**: tx\_bytes, tx\_carrier, tx\_colls, tx\_drop, tx\_errs,
    tx\_packets

  - **Receive**: rx\_bytes, rx\_drop, rx\_errs, rx\_frame,
    rx\_multicast, rx\_packets

You can use [Grafana](https://grafana.com/), an open source analytics and monitoring tool, to view the interface statistics collected by the NetQ Agents. The fastest way to achieve this is by installing Grafana on an application server or locally per user, and then importing the prepared NetQ dashboard.

## Install NetQ Plug-in for Grafana

The first step is to install the NetQ plug-in on your NetQ server or appliance. There are three ways to install the plug-in:

- **Docker File**: Add the commands in your existing Dockerfile
    ```
    # grafana docker file
    FROM grafana/grafana:6.2.2
    RUN grafana-cli --pluginUrl https://netq-grafana-dsrc.s3-us-west-2.amazonaws.com/dist.zip plugins install netq-dashboard
    ```
- **Grafana Docker Image**: Download and run the plug-in in your Grafana Docker container
    ```
    $ docker run -d -p 3000:3000 --name=grafana -e "GF_INSTALL_PLUGINS=https://netq-grafana-dsrc.s3-us-west-2.amazonaws.com/dist.zip;netq-dashboard" grafana/grafana
    ```
- **Grafana CLI**: Run a command in the Grafana CLI within your Grafana service
    ```
    grafana-cli --pluginUrl https://netq-grafana-dsrc.s3-us-west-2.amazonaws.com/dist.zip plugins install netq-dashboard
    ```
    Then restart Grafana.
    
    {{%notice info%}}
    The Grafana GUI is accessed through port 3000 by default. If you are
    running Grafana on a simulation server, you may need to modify
    forwarding rules in IPtables to allow access to port 3000.
    {{%/notice%}}

## Configure the Net-Q Data Source

## Create a Hostname Variable

## View the Interface Statistics

The quickest way to view the interface statistics for your Cumulus Linux network is to make use of the pre-configured dashboard installed with the plug-in. Once you are familiar with that dashboard, you may want to create a new dashboard or add new panels to the NetQ dashboard.

1.  Open the Grafana user interface:
    - Remote access: Enter **\<NetQ-Server-or-Appliance-IPaddr\>:3000** in a web browser address field.
    - Local access:  Enter **localhost:3000** in a web browser address field.

2.  Log in with a user name of *admin* and a password of *admin*.
    
    {{<figure src="/images/netq/grafana-login-230.png" width="400">}}
    
    The Home Dashboard appears.

3.  Select the *final-proc-dashboard* from the left panel.

4. Select the hostname from the variable list at the top left of the charts to see the statistics for that switch or host.

5. Review the statistics, looking for peaks and valleys, unusual patterns, and so forth.

6. Explore the data more by modifying the data view in one of several ways using the dashboard tool set:

    {{<figure src="/images/netq/grafana-dashboard-tools-230.png" width="600">}}
    
    - Select a different time period for the data by clicking the forward or back arrows. The default time range is dependent on the width of your browser window.
    - Zoom in on the dashboard by clicking the magnifying glass.
    - Manually refresh the dashboard data, or set an automatic refresh rate for the dashboard from the down arrow.
    - Add a new variable by clicking the cog wheel, then selecting Variables
    - Add additional panels
    - Click any chart title to edit or remove it from the dashboard

## Resolve Issues

If you are experiencing issues with the configuration or behavior of the
interface statistic collection feature, you can check log files on the
Telemetry Server and the individual nodes.

On the Telemetry Server, you can:

  - Verify that the InfluxDB is up and running (see example below)

  - Review relevant log files
    
      - `/var/log/cts/cts-influxdb.log`
    
      - `/var/log/netq-stats-pushd.log`

On each node, check the NetQ Agent log file `/var/log/netq-agent.log`.

### Example: Verifying InfluxDB Status</span>

1.  Validate the database is up.
    
        cumulus@ts:~$ sudo docker ps
        CONTAINER ID     IMAGE           COMMAND                   CREATED       STATUS      PORTS  NAMES
        dacbf4f234e9     cumulus-netq    "/tini -g -- /usr/sb…"    2 hours ago   Up 2 hours         netq_netq_1
        9cfd1e768be4     redis           "docker-entrypoint.s…"    2 hours ago   Up 2 hours         netq_redis_snt1_1
        5ad5e17a0089     redis           "docker-entrypoint.s…"    2 hours ago   Up 2 hours         netq_redis_master_1
        9bb544d9bb1b     influxdb        "/entrypoint.sh infl…"    2 hours ago   Up 2 hours         netq_influxdb_1
        77a7478bb6dc     cumulus-tsgui   "/portainer"              2 hours ago   Up 2 hours         netq_tsgui_1

2.  Validate the statistics being collected on which nodes and
    interfaces.
    
        cumulus@ts:~$ sudo docker exec -it 9bb544d9bb1b /bin/bash
        bash-4.3# influx -precision rfc3339
        Connected to http://localhost:8086 version 1.3.6
        InfluxDB shell version: 1.3.6
        > SHOW FIELD KEYS ON "netq"
        name: procnetdev
        fieldKey    fieldType
        --------    ---------
        rxBytes     integer
        rxDrop      integer
        rxErrs      integer
        rxFrame     integer
        rxMulticast integer
        rxPackets   integer
        txBytes     integer
        txCarrier   integer
        txColls     integer
        txDrop      integer
        txErrs      integer
        txPackets   integer
         
        > SHOW SERIES
        key
        ...
        downsampled_stats
        procnetdev,hostname=spine01,interface=eth0
        procnetdev,hostname=spine01,interface=lo
        procnetdev,hostname=spine01,interface=mgmt
        procnetdev,hostname=spine01,interface=swp1
        procnetdev,hostname=spine01,interface=swp2
        procnetdev,hostname=spine01,interface=swp3
        procnetdev,hostname=spine01,interface=swp31
        procnetdev,hostname=spine01,interface=swp32
        procnetdev,hostname=spine01,interface=swp4
        procnetdev,hostname=spine01,interface=vagrant
        procnetdev,hostname=spine02,interface=eth0
        procnetdev,hostname=spine02,interface=lo
        procnetdev,hostname=spine02,interface=mgmt
        procnetdev,hostname=spine02,interface=swp1
        procnetdev,hostname=spine02,interface=swp2
        procnetdev,hostname=spine02,interface=swp3
        procnetdev,hostname=spine02,interface=swp31
        procnetdev,hostname=spine02,interface=swp32
        procnetdev,hostname=spine02,interface=swp4
        procnetdev,hostname=spine02,interface=vagrant
        ...
