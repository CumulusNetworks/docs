---
title: Integrate NetQ with Grafana
author: Cumulus Networks
weight: 202
toc: 3
---
Switches collect statistics about the performance of their interfaces. The NetQ Agent on each switch collects these statistics every 15 seconds and then sends them to your NetQ Server or Appliance.

NetQ only collects statistics for physical interfaces; it does not collect statistics for virtual (non-physical) interfaces, such as bonds, bridges, and VXLANs. Specifically, the NetQ Agent collects the following interface statistics:

  - **Transmit**: tx\_bytes, tx\_carrier, tx\_colls, tx\_drop, tx\_errs,
    tx\_packets

  - **Receive**: rx\_bytes, rx\_drop, rx\_errs, rx\_frame,
    rx\_multicast, rx\_packets

You can use Grafana version 6.x, an open source analytics and monitoring tool, to view these statistics. The fastest way to achieve this is by installing Grafana on an application server or locally per user, and then installing the NetQ plugin containing the prepared NetQ dashboard.  

{{%notice note%}}

If you do not have Grafana installed already, refer to {{<exlink url="https://grafana.com/" text="grafana.com">}} for instructions on installing and configuring the Grafana tool.

{{%/notice%}}

## Install NetQ Plugin for Grafana

Use the Grafana CLI to install the NetQ plugin. For more detail about this command, refer to the {{<exlink url="https://grafana.com/docs/grafana/latest/administration/cli/" text="Grafana CLI documentation">}}.

```
grafana-cli --pluginUrl https://netq-grafana-dsrc.s3-us-west-2.amazonaws.com/dist.zip plugins install netq-dashboard
installing netq-dashboard @ 
from: https://netq-grafana-dsrc.s3-us-west-2.amazonaws.com/dist.zip
into: /usr/local/var/lib/grafana/plugins

✔ Installed netq-dashboard successfully

Restart grafana after installing plugins . <service grafana-server restart>
```

## Set Up the NetQ Data Source

Now that you have the plugin installed, you need to configure access to the NetQ data source.

1. Open the Grafana user interface.

2. Log in using your application credentials.

    {{<figure src="/images/netq/grafana-login-230.png" width="400">}}

    The Home Dashboard appears.

    {{<figure src="/images/netq/grafana-home-page-230.png" width="700">}}

3. Click **Add data source** or {{<img src="/images/netq/grafana-config-icon.png" width="24" height="24">}} > *Data Sources*.

4. Enter **Net-Q** in the search box or scroll down to the **Other** category, and select *Net-Q* from there.

    {{<figure src="/images/netq/grafana-add-data-src-230.png" width="500">}}

5. Enter *Net-Q* into the **Name** field.

6. Enter the URL used to access the database:
    - Cloud: *api.netq.cumulusnetworks.com*
    - On-premises: *\<hostname-or-ipaddr-of-netq-appl-or-vm\>/api*
    - Cumulus in the Cloud (CITC): *air.netq.cumulusnetworks.com*

7. Enter your credentials (the ones used to login)

8. For cloud deployments only, if you have more than one premises configured, you can select the premises you want to view, as follows:

    - If you leave the **Premises** field blank, the first premises name is selected by default
    - If you enter a premises name, that premises is selected for viewing

        *Note*: If multiple premises are configured with the same name, then the first premises of that name is selected for viewing

9. Click **Save & Test**

    {{<figure src="/images/netq/grafana-netq-dashboard-230.png" width="700">}}

## Create Your NetQ Dashboard

With the data source configured, you can create a dashboard with the transmit and receive statistics of interest to you.

To create your dashboard:

1. Click {{<img src="/images/netq/grafana-create-dashbd-icon.png" width="24" height="24">}} to open a blank dashboard.

2. Click {{<img src="/images/netq/grafana-config-icon.png" width="24" height="24">}} (Dashboard Settings) at the top of the dashboard.

3. Click **Variables**.

    {{<figure src="/images/netq/grafana-add-hostname-variable-230.png" width="600">}}

4. Enter *hostname* into the **Name** field.

5. Enter *Hostname* into the **Label** field.

6. Select *Net-Q* from the **Data source** list.

7. Enter *hostname* into the **Query** field.

8. Click **Add**.

    You should see a preview at the bottom of the hostname values.

9. Click {{<img src="/images/netq/grafana-back-button-230.png" width="24" height="24">}} to return to the new dashboard.

10. Click **Add Query**.

    {{<figure src="/images/netq/grafana-create-chart-230.png" width="600">}}

11. Select *Net-Q* from the **Query** source list.

12. Select the interface statistic you want to view from the **Metric** list.

13. Click the **General** icon.

    {{<figure src="/images/netq/grafana-create-chart-general-settings-230.png" width="600">}}

14. Select *hostname* from the **Repeat** list.

15. Set any other parameters around how to display the data.

16. Return to the dashboard.

17. Add additional panels with other metrics to complete your dashboard.

## Analyze the Data

Once you have your dashboard configured, you can start analyzing the data.

For reference, this example shows a dashboard with all of the available statistics.

{{<figure src="/images/netq/grafana-netq-dashboard-230.png" width="700">}}

1. Select the hostname from the variable list at the top left of the charts to see the statistics for that switch or host.

    {{<figure src="/images/netq/grafana-variable-list-230.png" width="200">}}

2. Review the statistics, looking for peaks and valleys, unusual patterns, and so forth.

3. Explore the data more by modifying the data view in one of several ways using the dashboard tool set:

    {{<figure src="/images/netq/grafana-dashboard-tools-230.png" width="600">}}
    
    - Select a different time period for the data by clicking the forward or back arrows. The default time range is dependent on the width of your browser window.
    - Zoom in on the dashboard by clicking the magnifying glass.
    - Manually refresh the dashboard data, or set an automatic refresh rate for the dashboard from the down arrow.
    - Add a new variable by clicking the cog wheel, then selecting Variables
    - Add additional panels
    - Click any chart title to edit or remove it from the dashboard
    - Rename the dashboard by clicking the cog wheel and entering the new name
