---
title: Monitor Network Inventory
author: Cumulus Networks
weight: 820
toc: 4
---
With NetQ, a network administrator can monitor both the switch hardware and its operating system for misconfigurations or misbehaving services. The Devices Inventory card workflow provides a view into the switches and hosts installed in your network and their various hardware and software components. The workflow contains a small card with a count of each device type in your network, a medium card displaying the operating systems running on each set of devices, large cards with component information statistics, and full-screen cards displaying tables with attributes of all switches and all hosts in your network.

For monitoring inventory and performance on a switch-by-switch basis, refer to {{<link title="Monitor Switches">}}.

## View the Number of Each Device Type in Your Network

You can view the number of switches and hosts deployed in your network. As you grow your network this can be useful for validating that devices have been added as scheduled.

To view the quantity of devices in your network, open the small Devices Inventory card.

{{< figure src="/images/netq/inventory-devices-small-230.png" width="200" >}}

## View Which Operating Systems Are Running on Your Network Devices

You can view the distribution of operating systems running on your switches and hosts. This is useful for verifying which versions of the OS are deployed and for upgrade planning. It also provides a view into the relative dependence on a given OS in your network.

To view the OS distribution, open the medium Devices Inventory card if it is not already on your workbench.

{{< figure src="/images/netq/inventory-devices-medium-230.png" width="200" >}}

## View Switch Components

To view switch components, open the large Devices Inventory card. By default the Switches tab is shown displaying the total number of switches, ASIC vendor, OS versions, license status, NetQ Agent versions, and specific platforms deployed on all of your switches.

{{< figure src="/images/netq/inventory-devices-large-switches-tab-230.png" width="500" >}}

### Highlight a Selected Component Type

You can hover over any of the segments in a component distribution chart to highlight a specific type of the given component. When you *hover*, a tooltip appears displaying:

- the name or value of the component type, such as the version number or status
- the total number of switches with that type of component deployed compared to the total number of switches
- percentage of this type with respect to all component types.  

    {{< figure src="/images/netq/inventory-devices-large-switches-tab-component-highlight-230.png" width="650" >}}

Additionally, sympathetic highlighting is used to show the related component types relevant to the highlighted segment and the number of unique component types associated with this type (shown in blue here).

### Focus on a Selected Component Type

To dig deeper on a particular component type, you can filter the card data by that type. In this procedure, the result of filtering on the OS is shown.

To view component type data:

1. Click a segment of the component distribution charts.

    {{< figure src="/images/netq/inventory-devices-large-switches-tab-component-filter.png" width="300" >}}

2. Select the first option from the popup, *Filter* \<*component name*\>. The card data is filtered to show only the components associated with selected component type. A filter tag appears next to the total number of switches indicating the filter criteria.

    {{< figure src="/images/netq/inventory-devices-large-switches-tab-component-filter-os-230.png" width="250" >}}

3.  Hover over the segments to view the related components.

    {{< figure src="/images/netq/inventory-devices-large-switches-tab-component-highlight2-230.png" width="500" >}}

4.  To return to the full complement of components, click the <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/close.svg" height="14" width="14"/> in the filter tag.

### Navigate to the Switch Inventory Workflow

While the Device Inventory cards provide a network-wide view, you may want to see more detail about your switch inventory. This can be found in the Switches Inventory card workflow. To open that workflow, click the **Switch Inventory** button at the top right of the Switches card.

{{< figure src="/images/netq/inventory-devices-large-switches-tab-switch-inv-button-230.png" width="500" >}}

## View All Switches

You can view all stored attributes for all switches in your network. To view all switch details, open the full screen Devices Inventory card and click the **All Switches** tab in the navigation panel.

{{< figure src="/images/netq/inventory-devices-fullscr-allswitches-tab-241.png" width="700" >}}

To return to your workbench, click <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/close.svg" height="14" width="14"/> in the top right corner of the card.

## View All Hosts

You can view all stored attributes for all hosts in your network. To view all hosts details, open the full screen Devices Inventory card and click the **All Hosts** tab in the navigation panel.

{{< figure src="/images/netq/inventory-devices-fullscr-allhosts-tab-241.png" width="700" >}}

To return to your workbench, click <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/close.svg" height="14" width="14"/> in the top right corner of the card.
