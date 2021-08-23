---
title: Validate Overall Network Health
author: NVIDIA
weight: 1010
toc: 3
---

The Network Health card in the NetQ UI lets you view the overall health of your network at a glance, giving you a high-level understanding of how well your network is operating. Successful validation results determine overall network health shown in this card.

## View Network Health Summary

You can view a very simple summary of your network health, including the percentage of successful validation results, a trend indicator, and a distribution of the validation results.

To view this summary:

1. Open or locate the Network Health card on your workbench.

2. Change to the small card using the card size picker.

    {{<figure src="/images/netq/ntwk-hlth-small-230.png" width="200">}}

    In this example, the overall health is relatively good, but improving compared to recent status. Refer to the next section for viewing the key health metrics.

## View Key Metrics of Network Health

Overall network health in the NetQ UI is a calculated average of several key health metrics: System, Network Services, and Interface health.

To view these key metrics:

1. Open or locate the Network Health card on your workbench.

2. Change to the medium card if needed.

    Each metric is shown with percentage of successful validations, a trend indicator, and a distribution of the validation results.

    {{<figure src="/images/netq/ntwk-hlth-medium-230.png" width="200">}}

    In this example, the health of each of the system and network services are good, but interface health is on the lower side. While it is improving, you might choose to dig further if it does not continue to improve. Refer to the following section for additional details.

## View Network Health

Network health is divided into three categories: 

- System health
- Network service health
- Interface health

System health is a calculated average of the NetQ Agent and sensor health metrics. In all cases, validation is performed on the agents. If you are monitoring platform sensors, the calculation includes these as well.

Network services health is a calculated average of the individual network protocol and services health metrics. In all cases, validation is performed on NTP. If you are running BGP, EVPN, MLAG, OSPF, or VXLAN protocols the calculation includes these as well. You can view the overall health of network services from the medium Network Health card and information about individual services from the Network Service Health tab on the large Network Health card.

Interface health is a calculated average of the interfaces, VLAN, and link MTU health metrics. You can view the overall health of interfaces from the medium Interface Health card and information about each component from the Interface Health tab on the large Interface Health card.

To view details about your network's health:

1. Open or locate the Network Health card on your workbench.

2. Change to the large card using the card size picker.

{{<tabs "View System Health">}}

{{<tab "System Health">}}

3. By default, the System Health tab is displayed. If it is not, hover over the card and click {{<img src="https://icons.cumulusnetworks.com/04-Programing-Apps-Websites/12-Apps/app-window-heart.svg" height="18" width="18">}}.

   {{<figure src="/images/netq/ntwk-hlth-large-sys-hlth-tab-4.0.0.png" width="500">}}

   The health of each system protocol or service is represented on the left side of the card by a distribution of the health score, a trend indicator, and a percentage of successful results. The right side of the card provides a listing of devices with failures related to agents and sensors.

{{</tab>}}

{{<tab "Network Services Health">}}

3. Hover over the card and click {{<img src="https://icons.cumulusnetworks.com/05-Internet-Networks-Servers/01-Worldwide-Web/network-heart.svg" height="18" width="18">}}.

   {{<figure src="/images/netq/ntwk-hlth-large-ntwk-hlth-tab-241.png" width="500">}}

   The health of each network protocol or service is represented on the left side of the card by a distribution of the health score, a trend indicator, and a percentage of successful results. The right side of the card provides a listing of devices with failures related to these protocols and services.

{{</tab>}}

{{<tab "Interface Health">}}

3. Hover over the card and click {{<img src="/images/netq/ntwk-health-if-health-icon.png" height="20" width="20">}}.

   {{<figure src="/images/netq/ntwk-hlth-large-if-hlth-tab-320.png" width="500">}}

   The health of each interface protocol or service is represented on the left side of the card by a distribution of the health score, a trend indicator, and a percentage of successful results. The right side of the card provides a listing of devices with failures related to interfaces, VLANs, and link MTUs.

{{</tab>}}

{{</tabs>}}

### View Devices with the Most Issues

It is useful to know which devices are experiencing the most issues with their system services, network services, or interfaces in general, as this can help focus troubleshooting efforts toward selected devices versus the service itself.

To view devices with the most issues, select **Most Failures** from the filter above the table on the right.

{{<figure src="/images/netq/ntwk-health-large-table-options-222.png" width="300">}}

Devices with the highest number of issues are listed at the top. Scroll down to view those with fewer issues. To further investigate the critical devices, open the Switch card or the Events|Alarms and Events|Info cards and filter on the indicated switches.

### View Devices with Recent Issues

It is useful to know which devices are experiencing the most issues with their with their system services, network services, or interfaces right now, as this can help focus troubleshooting efforts toward devices current issues.

To view devices with recent issues, select **Recent Failures** from the filter above the table on the right. Devices with the highest number of issues are listed at the top. Scroll down to view those with fewer issues. To further investigate the critical devices, open the Switch card or the Event cards and filter on the indicated switches.

### Filter Results by Service

You can focus the data in the table on the right, by unselecting one or more services. Click the *checkbox* next to the service you want to remove from the data. In this example, we have unchecked MTU.

{{<figure src="/images/netq/ntwk-hlth-large-filter-if-hlth-in-tbl-241.png" width="500">}}

This removes the checkbox next to the associated chart and grays out the title of the chart, temporarily removing the data related to that service from the table. Add it back by hovering over the chart and clicking the checkbox that appears.

### View Details of a Particular Service

From the relevant tab (System Health, Network Service Health, or Interface Health) on the large Network Health card, you can click on a chart to take you to the full-screen card pre-focused on that service data.

This example shows the results of clicking on the Agent chart.

{{<figure src="/images/netq/ntwk-hlth-fullscr-prefilter-agents-320.png" width="700">}}

## View All Network Protocol and Service Validation Results

The Network Health card workflow enables you to view all of the results
of all validations run on the network protocols and services during the
designated time period.

To view all the validation results:

1. Open or locate the Network Health card on your workbench.

2. Change to the large card using the card size picker.

3. Click *\<network protocol or service name\>* tab in the navigation panel.

4. Look for patterns in the data. For example, when did nodes, sessions, links, ports, or devices start failing validation? Was it at a specific time? Was it when you starting running the service on more nodes? Did sessions fail, but nodes were fine?

    {{<figure src="/images/netq/ntwk-hlth-fullscr-bgp-tab-241.png" width="700">}}

Where to go next depends on what data you see, but a few options include:

- Look for matching event information for the failure points in a given protocol or service.
- When you find failures in one protocol, compare with higher level protocols to see if they fail at a similar time (or vice versa with supporting services).
- Export the data for use in another analytics tool, by clicking {{<img src="https://icons.cumulusnetworks.com/05-Internet-Networks-Servers/08-Upload-Download/download-bottom.svg" height="18" width="18">}} and providing a name for the data file.
