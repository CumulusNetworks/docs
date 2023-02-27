---
title: Validate Overall Network Health
author: NVIDIA
weight: 1010
toc: 3
---

The Validation Summary card in the NetQ UI lets you view the overall health of your network at a glance, giving you a high-level understanding of how well your network is operating. Successful validation results determine overall network health shown in this card.

## View Key Metrics of Network Health

Overall network health in the NetQ UI is a calculated average of several key health metrics: system, network services, and interface health.

**System health** represents the NetQ Agent and sensor health validations. In all cases, validation is performed on the agents. If you are monitoring platform sensors, the validation checks include these as well.

**Network service health** represents the individual network protocol and services validations. In all cases, validation is performed on NTP. If you are running BGP, EVPN, MLAG, OSPF, or VXLAN protocols the validation checks include these as well.

**Interface health** represents the interfaces, VLAN, and link MTU validations.

To view network health metrics:

1. Open or locate the medium Validation Summary card on your workbench.

2. Each metric displays a distribution of the validation results for each category. Hover over the individual categories to view detailed metrics for specific validation checks.  

   In this example, system health is good, but network services and interface health display validation failures:

    {{<figure src="/images/netq/updated-validation-summary-card.png" alt="medium validation summary card displaying high-level health metrics" width="200">}}

## View Detailed Network Health

To view details about your network's health, open or locate the large Validation Summary card on your workbench.

{{<tabs "View System Health">}}

{{<tab "System Health">}}

By default, the **System health tab** is displayed. 

   {{<figure src="/images/netq/validation-summary-l3-sys-health-42.png" width="500">}}

   The health of agents and sensors is represented on the left side of the card. Hover over the chart for each type of validation to see detailed results. The right side of the card displays devices with failures related to agents and sensors.

{{</tab>}}

{{<tab "Network Services Health">}}

Click the **Network service health** tab.

   {{<figure src="/images/netq/validation-summary-l3-net-health-42.png" width="500">}}

   The health of each network protocol or service is represented on the left side of the card. Hover over the chart for each type of validation to see detailed results. The right side of the card displays devices with failures related to these protocols and services.

{{</tab>}}

{{<tab "Interface Health">}}

Click the **Interface health** tab.

   {{<figure src="/images/netq/validation-summary-l3-int-health-42.png" width="500">}}

   The health of interfaces, VLANs, and link MTUs is represented on the left side of the card. Hover over the chart for each type of validation to see detailed results. The right side of the card displays devices with failures related to interfaces, VLANs, and link MTUs.

{{</tab>}}

{{</tabs>}}

### View Devices with the Most Issues

To view devices with the most issues, select **Most failures** from the filter above the table on the right.

{{<figure src="/images/netq/validation-summary-most-failures-42.png" alt="filter displaying two hostnames with multiple failures" width="300">}}

Devices with the most issues are listed at the top. To further investigate critical devices, click on the hostname to open the device card, or use the Events card and filter on the indicated switches.

### View Devices with Recent Issues

To view devices with recent issues, select **Recent failures** from the filter above the table on the right. The devices with the most-recent failures are listed at the top. To further investigate critical devices, click on the hostname to open the device card, or use the Events card and filter on the indicated switches.

### Filter Results by Service

You can focus the data in the table on the right by unselecting one or more services. Select the checkbox next to the service you want to remove from the data. In this example, we have unchecked MTU.

{{<figure src="/images/netq/validation-summary-l3-int-health-uncheck-mtu-42.png" alt="medicum card displaying interface health" width="500">}}

Unselecting the service temporarily removes the data related to that service from the table.

### View Details of a Particular Service

From the relevant tab (System Health, Network Service Health, or Interface Health) on the large Validation Summary card, you can select a chart to open a full-screen view of the validation data for that service.

The following example shows the EVPN chart:

{{<figure src="/images/netq/full-screen-evpn-validation.png" alt="EVPN validation data" width="900">}}

## View All Network Protocol and Service Validation Results

The Validation Summary card workflow lets you view all of the results of all validations run on the network protocols and services during a designated time period.

To view all the validation results:

1. Open or locate the full-screen Validation Summary card on your workbench.

2. Look for patterns in the data. For example, when did nodes, sessions, links, ports, or devices start failing validation? Was it at a specific time? Was it when you starting running the service on more nodes? Did sessions fail, but nodes were fine?

    {{<figure src="/images/netq/validation-summary-l4-failed-42.png" alt="fullscreen validation summary card displaying BGP metrics" width="900">}}

Where to go next depends on what data you see, but a few options include:

- Look for matching event information for the failure points in a given protocol or service.
- When you find failures in one protocol, compare with higher level protocols to see if they fail at a similar time (or vice versa with supporting services).
- Export the data for use in another analytics tool, by clicking {{<img src="https://icons.cumulusnetworks.com/05-Internet-Networks-Servers/08-Upload-Download/download-bottom.svg" alt="download" height="18" width="18">}} and providing a name for the data file.