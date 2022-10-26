---
title: Validate Overall Network Health
author: NVIDIA
weight: 1010
toc: 3
---

The Validation Summary card in the NetQ UI lets you view the overall health of your network at a glance, giving you a high-level understanding of how well your network is operating. Successful validation results determine overall network health shown in this card.

## View Network Health Summary

You can view a very simple summary of your network health including the distribution of validation check results across your network.

To view this summary:

1. Open or locate the Validation Summary card on your workbench.

2. Change to the small card using the card size picker.

    {{<figure src="/images/netq/validation-summary-l1-42.png" width="200">}}

    In this example, all validation checks are successful.
## View Key Metrics of Network Health

Overall network health in the NetQ UI is a calculated average of several key health metrics: interface, system, and network services health.

To view these key metrics:

1. Open or locate the Validation Summary card on your workbench.

2. Change to the medium card if needed.

    Each metric is shown with a distribution of the validation results for each category. Hover over the individual categories to view detailed metrics for specific validation checks.

    {{<figure src="/images/netq/validation-summary-l2-net-svcs-fail-42.png" width="200">}}

    In this example, the health of each of the interface and system health are good, but network service health shows some validation failures. You might choose to dig further if it does improve. Refer to the following section for additional details.

## View Network Health

Network health is divided into three categories: 

- System health
- Network service health
- Interface health

System health represents the NetQ Agent and sensor health validations. In all cases, validation is performed on the agents. If you are monitoring platform sensors, the validation checks include these as well.

Network services health represents the individual network protocol and services validations. In all cases, validation is performed on NTP. If you are running BGP, EVPN, MLAG, OSPF, or VXLAN protocols the validation checks include these as well. You can view the overall health of network services from the medium Validation Summary card and information about individual services from the **Network service health** tab on the large Validation Summary card.

Interface health represents the interfaces, VLAN, and link MTU validations. You can view the overall health of interfaces from the medium Validation Summary card and information about each component from the Interface Health tab on the large Validation Summary card.

To view details about your network's health:

1. Open or locate the Validation Summary card on your workbench.

2. Change to the large card using the card size picker.

{{<tabs "View System Health">}}

{{<tab "System Health">}}

3. By default, the **System health tab** is displayed. 

   {{<figure src="/images/netq/validation-summary-l3-sys-health-42.png" width="500">}}

   The health of agents and sensors is represented on the left side of the card. Hover over the chart for each type of validation to see detailed results. The right side of the card provides a listing of devices with failures related to agents and sensors.

{{</tab>}}

{{<tab "Network Services Health">}}

3. Click the **Network service health** tab.

   {{<figure src="/images/netq/validation-summary-l3-net-health-42.png" width="500">}}

   The health of each network protocol or service is represented on the left side of the card. Hover over the chart for each type of validation to see detailed results. The right side of the card provides a listing of devices with failures related to these protocols and services.

{{</tab>}}

{{<tab "Interface Health">}}

3. Click the **Interface health** tab.

   {{<figure src="/images/netq/validation-summary-l3-int-health-42.png" width="500">}}

   The health of interfaces, VLANs, and link MTUs is represented on the left side of the card. Hover over the chart for each type of validation to see detailed results. The right side of the card provides a listing of devices with failures related to interfaces, VLANs, and link MTUs.

{{</tab>}}

{{</tabs>}}

### View Devices with the Most Issues

It is useful to know which devices are experiencing the most issues with their system services, network services, or interfaces in general, as this can help focus troubleshooting efforts toward selected devices versus the service itself.

To view devices with the most issues, select **Most failures** from the filter above the table on the right.

{{<figure src="/images/netq/validation-summary-most-failures-42.png" width="300">}}

Devices with the most issues are listed at the top. Scroll down to view those with fewer issues. To further investigate critical devices, click on the hostname to open the device card, or use the Events card and filter on the indicated switches.

### View Devices with Recent Issues

To view devices with recent issues, select **Recent failures** from the filter above the table on the right. The devices with the most-recent failures are listed at the top. To further investigate critical devices, click on the hostname to open the device card, or use the Events card and filter on the indicated switches.

### Filter Results by Service

You can focus the data in the table on the right by unselecting one or more services. Click the checkbox next to the service you want to remove from the data. In this example, we have unchecked MTU.

{{<figure src="/images/netq/validation-summary-l3-int-health-uncheck-mtu-42.png" width="500">}}

This removes the checkbox next to the associated chart and grays out the title of the chart, temporarily removing the data related to that service from the table. Add it back by hovering over the chart and clicking the checkbox that appears.

### View Details of a Particular Service

From the relevant tab (System Health, Network Service Health, or Interface Health) on the large Validation Summary card, you can click on a chart to take you to the full-screen validation data for that service.

This example shows the results of clicking on the EVPN chart.

{{<figure src="/images/netq/validation-summary-failed-validation-expanded-42.png" width="700">}}

## View All Network Protocol and Service Validation Results

The Validation Summary card workflow enables you to view all of the results of all validations run on the network protocols and services during the designated time period.

To view all the validation results:

1. Open or locate the Validation Summary card on your workbench.

2. Change to the large card using the card size picker.

3. Click *\<network protocol or service name\>* tab in the navigation panel.

4. Look for patterns in the data. For example, when did nodes, sessions, links, ports, or devices start failing validation? Was it at a specific time? Was it when you starting running the service on more nodes? Did sessions fail, but nodes were fine?

    {{<figure src="/images/netq/validation-summary-l4-failed-42.png" width="700">}}

Where to go next depends on what data you see, but a few options include:

- Look for matching event information for the failure points in a given protocol or service.
- When you find failures in one protocol, compare with higher level protocols to see if they fail at a similar time (or vice versa with supporting services).
- Export the data for use in another analytics tool, by clicking {{<img src="https://icons.cumulusnetworks.com/05-Internet-Networks-Servers/08-Upload-Download/download-bottom.svg" height="18" width="18">}} and providing a name for the data file.
