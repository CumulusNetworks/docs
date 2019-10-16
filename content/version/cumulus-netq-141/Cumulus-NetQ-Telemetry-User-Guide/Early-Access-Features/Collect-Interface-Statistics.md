---
title: Collect Interface Statistics
author: Cumulus Networks
weight: 111
aliases:
 - /display/NETQ141/Collect+Interface+Statistics
 - /pages/viewpage.action?pageId=10453499
pageID: 10453499
product: Cumulus NetQ
version: 1.4.1
imgData: cumulus-netq-141
siteSlug: cumulus-netq-141
---
Switches collect statistics about the performance of their interfaces.
The NetQ Agent on each switch collects these statistics every 15 seconds
by reading `/proc/net/dev`, and then sending them to the NetQ Telemetry
Server where it is stored in its InfluxDB in `procnetdev`. The Telemetry
Server `netq-stats-pushd` service manages the receipt and storage of the
statistics.

Only statistics for physical interfaces are collected; NetQ does not
collect statistics for non-physical interfaces, such as bonds, bridges,
and VXLANs. Specifically, the NetQ Agent collects the following
interface statistics:

  - **Transmit**: tx\_bytes, tx\_carrier, tx\_colls, tx\_drop, tx\_errs,
    tx\_packets
  - **Receive**: rx\_bytes, rx\_drop, rx\_errs, rx\_frame,
    rx\_multicast, rx\_packets

Currently, these statistics are available for view in third-party
analytic tools.

{{%notice note%}}

The collection of interface statistics is an [early access
feature](https://support.cumulusnetworks.com/hc/en-us/articles/202933878)
in Cumulus NetQ 1.3 and later.

{{%/notice%}}

## Configure Interface Statistic Collection

InfluxDB is installed in its own container by default on the Telemetry
Server. The `netq-stats-pushd` service is also installed by default, but
must be enabled. You also need to enable statistics collection on every
node for which you want to gather statistics.

To set up interface statistic collection:

1.  Enable and start the `netq-stats-pushd` service on the Telemetry
    Server.

        cumulus@ts:~$ sudo systemctl enable netq-stats-pushd.service
        cumulus@ts:~$ sudo systemctl start netq-stats-pushd.service

2.  Verify the service is running.

        cumulus@ts:~$ sudo systemctl status netq-stats-pushd.service
        ● netq-stats-pushd.service - NetQ Stats Storage daemon
           Loaded: loaded (/lib/systemd/system/netq-stats-pushd.service; enabled)
           Active: active (running) since Mon 2017-11-27 00:51:09 UTC; 6s ago
         Main PID: 30550 (netq-stats-push)

3.  On every node you want to monitor: log in to each node, configure
    the NetQ Agent to collect the statistics, and then restart the
    agent.

        cumulus@ts:~$ ssh spine01
        cumulus@spine01:~$ netq config add agent stats
        cumulus@spine01:~$ netq config restart agent

    {{%notice tip%}}

Optionally, you can automate the configuration and restart of each
node using an IT automation tool, such as Ansible.

    {{%/notice%}}

As each NetQ Agent is restarted, the `netq-stats-pushd` service starts
collecting interface statistics and the agent pushes them to the
database on the Telemetry Server.

## View Interface Statistics in Grafana

You can use the open platform [Grafana](https://grafana.com/) analytics
and monitoring tool to view the interface statistics collected by the
NetQ Agents. This is accomplished by installing the tool on the
Telemetry Server and then configuring the tool to access the NetQ
InfluxDB.

To set up Grafana to view NetQ interface statistics:

1.  Using a text editor of your choice, add the repository for Grafana.

        cumulus@ts:~$ sudo vi /etc/apt/sources.list
        [sudo] password for cumulus:**********
         
        ...
        deb https://packagecloud.io/grafana/stable/debian/ jessie main
        ...

2.  Install the package cloud key.

        cumulus@ts:~$ curl https://packagecloud.io/gpg.key | sudo apt-key add -

3.  Install, start, and enable the package.

        cumulus@ts:~$ sudo apt-get update
        cumulus@ts:~$ sudo apt-get install grafana
        cumulus@ts:~$ sudo systemctl daemon-reload
        cumulus@ts:~$ sudo systemctl start grafana-server
        cumulus@ts:~$ sudo systemctl enable grafana-server

4.  Verify Grafana is running.

        cumulus@ts:~$ sudo systemctl status grafana-server
        ● grafana-server.service - Grafana instance
           Loaded: loaded (/usr/lib/systemd/system/grafana-server.service; disabled)
           Active: active (running) since Mon 2018-06-18 20:14:38 UTC; 7s ago
             Docs: http://docs.grafana.org
        Main PID: 5755 (grafana-server)
          CGroup: /system.slice/grafana-server.service
                  └─5755 /usr/sbin/grafana-server --config=/etc/grafana/grafana.ini --pidfile=/var/...

    {{%notice note%}}

The Grafana GUI is accessed through port 3000 by default. If you are
running Grafana on a simulation server, you may need to modify
forwarding rules in IPtables to allow access to port 3000.

    {{%/notice%}}

5.  Open Grafana.

    1.  In a web browser, enter the
        <*Telemetry_Server_IPaddress:* 3000> in the address field.

    2.  Log in with a user name of *admin* and a password of *admin*.

        {{% imgOld 0 %}}

        The Home Dashboard appears.

6.  Create a data source.

    1.  Click **Configuration** (<img src="/images/netq/grafana-config-icon.png" width="16"/>) \> **Data Sources**.

    2.  Click **Add data source**.

    3.  Enter a name for the data source, for example *NetQ IF Stats* or
        *cumulus-netq.*

    4.  Select *InfluxDB* from the **Type** list box.

    5.  Verify the URL references port 8086.

    6.  In **InfluxDB Details**, enter *netq* for the **Database**.

    7.  Enter *admin* for the **User** and *CumulusNetQ\!* for the
        **Password**.

        {{% imgOld 2 %}}

    8.  Click **Save & Test**.  
        A **Data source is working** confirmation appears when your
        configuration is good. If a **Network Error: Bad Request(400)**
        appears, your configuration needs to be modified. Check your
        configuration and click **Save & Test** again.

    9.  Click **Data Sources** to view the data source in a card.

        {{% imgOld 3 %}}

7.  Create a Dashboard.

    1.  Click Create (<img src="/images/netq/grafana-create-dashbd-icon.png" width="16"/>) \> Dashboard.

    2.  Select a panel type to add to the Dashboard.  
        You can add as many panels to your dashboard as you want, pick
        one to start with and then add others as desired. In our
        example, a Graph panel is selected.

        {{% imgOld 5 %}}

    3.  Click **Panel Title** \> **Edit** to open the edit option tabs.

        {{% imgOld 6 %}}

    4.  Click through each tab entering the relevant information.

        {{%notice note%}}

When creating queries in the **Metrics** tab, in FROM select *procnetdev* to access the receive and transmit statistics for display. In WHERE, click <img src="/images/netq/grafana-create-dashbd-icon.png" width="16"/>, select *hostname* to specify a particular host. In SELECT, choose a statistic to display. And so forth.

        {{%/notice%}}

    5.  When you have added all of the desired panels, click the **New
        dashboard** title, enter a name for the dashboard, and click
        **Save**.

    6.  Click <img src="/images/netq/grafana-save-dashbd-icon.png" width="16"/> to save the Dashboard itself.

You now have a customized view of the NetQ interface statistics. You can
add and remove panels at any time.

### Add Common Interface Statistics to Dashboard

There are many options for displaying the statistics in Grafana. Two
examples are provided here.

#### Example: Add Dropped Packets Panels

When you are monitoring your network, it is useful to see the total
number of packets that are being dropped by various interfaces and
whether that number is increasing or decreasing. This example creates
one panel to display the number of dropped packets on selected leaf01
interfaces and another panel to display the trend for these interfaces.

To add a total number of dropped packets panel:

1.  Open Grafana on the Telemetry Server.

2.  Open your dashboard (Cumulus Statistics in this example).

3.  Click <img src="/images/netq/grafana-add-new-panel-icon.png" width="24"/> to add a new panel.

4.  Select **Singlestat**.

5.  Click **Panel Title** \> **Edit**.

6.  On the **Metrics** tab, select the Data Source (*NetQ IF Stats* in
    this example).

7.  Click **Add Query**.

8.  Fill out query:

    1.  In FROM, select *procnetdev*

    2.  In WHERE, click <img src="/images/netq/grafana-create-dashbd-icon.png" width="16"/> \> select **hostname** \> select *leaf01* **** \> click <img src="/images/netq/grafana-create-dashbd-icon.png" width="16"/> \> select **interface** \> select *swp1*

    3.  In SELECT, select **rxDrop**

9.  On the **General** tab, enter a **Title** for the panel.

10. On the **Options** tab, under **Value** \> Stat, select *Total*.

11. Optionally on the **Options** tab, increase the font size and add
    thresholds.

12. Click <img src="/images/netq/grafana-close-options-icon.png" width="16"/> to close the edit options.

13. Click <img src="/images/netq/grafana-save-dashbd-icon.png" width="16"/> to save the dashboard.

    {{% imgOld 14 %}}

14. Add a comment regarding the change you made, and click **Save**.

    {{% imgOld 15 %}}

    You can now drag and drop the panels to modify their placement, or
    drag the bottom right corner of a given panel to resize it.

To add a trend view of dropped packets to your dashboard:

1.  Open Grafana on the Telemetry Server.

2.  Open your dashboard (Cumulus Statistics in this example).

3.  Click <img src="/images/netq/grafana-add-new-panel-icon.png" width="24"/> to add a new panel.

4.  Select **Graph**.

5.  Click **Panel Title** \> **Edit**.

6.  On the **Metrics** tab, select the Data Source (*NetQ IF Stats* in
    this example).

7.  Click **Add Query**.

8.  Fill out query:

    1.  In FROM, select *procnetdev*

    2.  In WHERE, click <img src="/images/netq/grafana-create-dashbd-icon.png" width="16"/> \> select **hostname** \> select *leaf01* **** \> click <img src="/images/netq/grafana-create-dashbd-icon.png" width="16"/> \> select **interface** \> select *swp1*

    3.  In SELECT, select **rxDrop**

9.  On the **General** tab, enter a **Title** for the panel.

10. Optionally on the **Time range** tab \> **Override relative time**
    \> 72h to view rolling results for the last 72 hours.

11. Click <img src="/images/netq/grafana-close-options-icon.png" width="16"/> to close the edit options.

    {{% imgOld 20 %}}

12. Click <img src="/images/netq/grafana-save-dashbd-icon.png" width="16"/> to save the dashboard.

    {{% imgOld 22 %}}

#### Example: Add Received Bytes Panel

The following example shows the Received Bytes on spine01 for all
interfaces over time.

To add trend view of received bytes to the dashboard:

1.  Open Grafana on the Telemetry Server.

2.  Open your dashboard (Cumulus Statistics in this example).

3.  Click <img src="/images/netq/grafana-add-new-panel-icon.png" width="24"/> to add a new panel.

4.  Select **Graph**.

5.  Click **Panel Title** \> **Edit**.

6.  On the **Metrics** tab, select the Data Source (*NetQ IF Stats* in
    this example).

7.  Click **Add Query**.

8.  Fill out query:

    1.  In FROM, select *procnetdev*

    2.  In WHERE, click <img src="/images/netq/grafana-create-dashbd-icon.png" width="16"/> \> select **hostname** \> select *spine01*

    3.  In SELECT, select **rxBytes**

9.  On the **General** tab, enter a **Title** for the panel.

10. Optionally specify other graph criteria using the other tabs.

11. Click <img src="/images/netq/grafana-close-options-icon.png" width="16"/> to close the edit options.

    {{% imgOld 26 %}}

12. Click <img src="/images/netq/grafana-save-dashbd-icon.png" width="16"/> to save the dashboard.

    {{% imgOld 28 %}}

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

### Example: Verifying InfluxDB Status

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

## Disable Interface Statistics Collection

If you no longer wish to collect interface statistics, you can disable
the feature.

{{%notice tip%}}

Disabling this feature does not purge the data already collected from
the database.

{{%/notice%}}

To disable interface statistics collection:

1.  For each node, disable the feature and restart the NetQ Agent.

        cumulus@switch:~$ netq config del stats
        cumulus@switch:~$ netq config restart agent

    {{%notice note%}}

You must restart the NetQ Agent after you disable statistics collection.

    {{%/notice%}}

2.  Once all nodes have stopped pushing statistics, stop and disable the
    `netq-stats-pushd` service on the Telemetry Server.

        cumulus@ts:~$ sudo systemctl stop netq-stats-pushd.service
        cumulus@ts:~$ sudo systemctl disable netq-stats-pushd.service

<article id="html-search-results" class="ht-content" style="display: none;">

</article>

<footer id="ht-footer">

</footer>
