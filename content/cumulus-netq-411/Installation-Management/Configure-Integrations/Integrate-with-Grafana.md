---
title: Integrate NetQ with Grafana
author: NVIDIA
weight: 550
toc: 3
---
Switches collect statistics about the performance of their interfaces. The NetQ Agent on each switch collects these statistics every 15 seconds and then sends them to your NetQ appliance or virtual machine.

NetQ collects statistics for *physical* interfaces; it does not collect statistics for *virtual* interfaces, such as bonds, bridges, and VXLANs.

<!-- NetQ collects these statistics from two data sources: Net-Q and Net-Q-Ethtool. -->

NetQ displays:

- **Transmit** with *tx\_* prefix: bytes, carrier, colls, drop, errs, packets
- **Receive** with *rx\_* prefix: bytes, drop, errs, frame, multicast, packets

<!-- Net-Q-Ethtool displays:

- **Hardware Transmit** with *hw\_if\_out\_* prefix: octets, ucast_pckts, mcast_pkts, bcast_pkts, discards, errors, q_drops, non_q_drops, q_len, pause_pkt, pfc[0-7]_pkt, wred_drops, q[0-9]_wred_drops
- **Hardware Receive** with *hw\_if\_in\_* prefix: octets, ucast_pckts, mcast_pkts, bcast_pkts, discards, l3_drops, buffer_drops, acl_drops, errors, dot3_length_errors, dot3_frame_errors, pause_pkt, pfc[0-7]_pkt
- **Software Transmit** with *soft\_out\_* prefix: errors, drops, tx_fifo_full
- **Software Receive** with *soft\_in\_* prefix: errors, frame_errors, drops -->

You can use Grafana, an open source analytics and monitoring tool, to view these statistics. The fastest way to achieve this is by installing Grafana on an application server or locally per user, and then installing the NetQ plugin.  

{{%notice note%}}

If you do not have Grafana installed already, refer to {{<exlink url="https://grafana.com/" text="grafana.com">}} for instructions on installing and configuring the Grafana tool.

{{%/notice%}}

<!-- vale off -->
## Install NetQ Plugin for Grafana
<!-- vale on -->

Use the Grafana CLI to install the NetQ plugin. For more detail about this command, refer to the {{<exlink url="https://grafana.com/docs/grafana/latest/administration/cli/" text="Grafana CLI documentation">}}.

{{%notice info%}}

The Grafana plugin comes unsigned. Before you can install it, you need to update the `grafana.ini` file then restart the Grafana service:

1. Edit `/etc/grafana/grafana.ini` and add `allow_loading_unsigned_plugins = netq-dashboard` to the file.

       cumulus@netq-appliance:~$ sudo nano /etc/grafana/grafana.ini
       ...
       allow_loading_unsigned_plugins = netq-dashboard
       ...

1. Restart the Grafana service:

       cumulus@netq-appliance:~$ sudo systemctl restart grafana-server.service

{{%/notice%}}

Then install the plugin:

```
cumulus@netq-appliance:~$ grafana-cli --pluginUrl https://netq-grafana-dsrc.s3-us-west-2.amazonaws.com/NetQ-DSplugin-3.3.1-plus.zip plugins install netq-dashboard
installing netq-dashboard @
from: https://netq-grafana-dsrc.s3-us-west-2.amazonaws.com/NetQ-DSplugin-3.3.1-plus.zip
into: /usr/local/var/lib/grafana/plugins

✔ Installed netq-dashboard successfully
```

After installing the plugin, you must restart Grafana, following the steps specific to your implementation.

## Set Up the NetQ Data Source

Now that you have the plugin installed, you need to configure access to the NetQ data source.

1. Open the Grafana user interface and log in. Navigate to the Home Dashboard:

    {{<figure src="/images/netq/grafana-home-page-230.png" width="700" alt="Grafana Home Dashboard">}}

2. Click **Add data source** or {{<img src="/images/netq/grafana-config-icon.png" width="24" height="24">}} > *Data Sources*.

<!-- 4. Enter **Net-Q** or **Net-Q-Ethtool** in the search box. Alternately, scroll down to the **Other** category, and select one of these sources from there.

    {{<figure src="/images/netq/grafana-add-data-src-320.png" width="500">}} -->

3. Enter **Net-Q** in the search box. Alternately, scroll down to the **Other** category, and select it from there.

    {{<figure src="/images/netq/grafana-add-data-src-330.png" alt="" width="500">}}

<!-- 5. Enter *Net-Q* or *Net-Q-Ethtool* into the **Name** field. -->

4. Enter *Net-Q* into the **Name** field.

5. Enter the URL used to access the database:
    - Cloud: *https://plugin.prod.netq.nvidia.com*
    - On-premises: *http://\<hostname-or-ipaddr-of-netq-appl-or-vm\>/plugin*
    - Cumulus in the Cloud (CITC): *plugin.air.netq.nvidia.com*

<!-- 7. Select which statistics you want to view from the **Module** dropdown; either *procdevstats* or *ethtool*. -->

6. From the **Module** dropdown, select *procdevstats*.

7. Enter your credentials (the ones used to log in).

8. For NetQ cloud deployments only, if you have more than one premises configured, you can select the premises you want to view, as follows:

    - If you leave the **Premises** field blank, the first premises name is selected by default.
    - If you enter a premises name, that premises is selected for viewing.
    - If multiple premises are configured with the same name, then the first listed premises is displayed.
<div style="margin-top: 20px;"></div>

9. Select **Save & Test**.

## Create Your NetQ Dashboard

After you configure the data source, you can create a customizable dashboard with transmit and receive statistics.

### Create a Dashboard

1. Click {{<img src="/images/netq/grafana-create-dashbd-icon.png" width="24" height="24">}} to open a blank dashboard.

2. Click {{<img src="/images/netq/grafana-config-icon.png" width="24" height="24">}} (Dashboard Settings) at the top of the dashboard.

### Add Variables

1. Click **Variables**.

    {{<figure src="/images/netq/grafana-add-hostname-variable-331.png" width="600">}}

2. In the **Name** field, enter *hostname*.

3. In the **Label** field, enter *hostname*.

<!-- 4. Select *Net-Q* or *Net-Q-Ethtool* from the **Data source** list. -->

4. From the **Data source** list, select *Net-Q*.

5. From the **Refresh** list, select *On Dashboard Load*.

6. In the **Query** field, enter *hostname*.

7. Click **Add**.

    You should see a preview at the bottom of the hostname values.

8. Click **Variables** to add another variable for the interface name.

    {{<figure src="/images/netq/grafana-add-ifname-variable-331.png" alt="" width="600">}}

9. In the **Name** field, enter *ifname*.

10. In the **Label** field, enter *ifname*.

<!-- 11. Select *Net-Q* or *Net-Q-Ethtool* from the **Data source** list. -->

11. From the **Data source** list, select *Net-Q*.

12. From the **Refresh** list, select *On Dashboard Load*.

13. In the **Query** field, enter *ifname*.

14. Click **Add**.

    You should see a preview at the bottom of the ifname values.

15. Click **Variables** to add a variable for metrics.

    {{<figure src="/images/netq/grafana-add-metrics-variable-331.png" alt="" width="600">}}

16. In the **Name** field, enter *metrics*.

17. In the **Label** field, enter *metrics*.

<!-- 18. Select *Net-Q* or *Net-Q-Ethtool* from the **Data source** list. -->

18. From the **Data source** list, select *Net-Q*.

19. From the **Refresh** list, select *On Dashboard Load*.

20. In the **Query** field, enter *metrics*.

21. Click **Add**.

    You should see a preview at the bottom of the metrics values.

### Add Charts

1. Now that the variables are defined, click {{<img src="/images/netq/grafana-back-button-230.png" width="24" height="24">}} to return to the new dashboard.

2. Click **Add Query**.

    {{<figure src="/images/netq/grafana-create-chart-230.png" alt="" width="600">}}

<!-- 3. Select *Net-Q* or *Net-Q-Ethtool* from the **Query** source list. -->

3. From the **Query** source list, select *Net-Q*.

4. Select the interface statistic you want to view from the **Metric** list.

5. Click the **General** icon.

    {{<figure src="/images/netq/grafana-create-chart-general-settings-230.png" alt="" width="600">}}

6. From the **Repeat** list, select *hostname*.

7. Set any other parameters around how to display the data.

8. Return to the dashboard.

9. Select one or more hostnames from the **hostname** list.

    {{<figure src="/images/netq/grafana-create-chart-select-hostname-331.png" alt="" width="600">}}

10. Select one or more interface names from the **ifname** list.

    {{<figure src="/images/netq/grafana-create-chart-select-ifname-331.png" alt="" width="600">}}

11. Select one or more metrics to display for these hostnames and interfaces from the **metrics** list.

    {{<figure src="/images/netq/grafana-create-chart-select-metrics-331.png" width="600">}}

The following example shows a dashboard with two hostnames, two interfaces, and one metric selected. The more values you select from the variable options, the more charts appear on your dashboard.

{{<figure src="/images/netq/grafana-netq-dashboard-331.png" alt="Grafana dashboard displaying metrics" width="600">}}

## Analyze the Data

After you have configured the dashboard, you can start analyzing the data. You can explore the data by modifying the viewing parameters in one of several ways using the dashboard tool set:

{{<figure src="/images/netq/grafana-dashboard-tools-230.png" alt="" width="600">}}

- Select a different time period for the data by clicking the forward or back arrows. The default time range is dependent on the width of your browser window.
- Zoom in on the dashboard by clicking the magnifying glass.
- Manually refresh the dashboard data, or set an automatic refresh rate for the dashboard from the down arrow.
- Add additional panels.
- Click any chart title to edit or remove it from the dashboard.
- Rename the dashboard by clicking the cog wheel and entering the new name.
