---
title: Monitor Network Inventory
author: Cumulus Networks
weight: 820
toc: 4
---
With NetQ, a network administrator can monitor both the switch hardware and its operating system for misconfigurations or misbehaving services. Refer to {{<link title="Monitor Devices">}} for related commands and cards.

## View a Summary of Your Network Inventory

All of the devices in your network can be viewed from either the NetQ CLI or NetQ UI.

{{< tabs "TabID15" >}}

{{< tab "NetQ CLI" >}}

To view a list of devices in your network, run:

```
netq show inventory brief
```

This example shows that we have four spine switches, three leaf switches, two border switches, two firewall switches, seven hosts (servers), and an out-of-band management server in this network.

```
cumulus@switch:~$ netq show inventory brief
Matching inventory records:
Hostname          Switch               OS              CPU      ASIC            Ports
----------------- -------------------- --------------- -------- --------------- -----------------------------------
border01          VX                   CL              x86_64   VX              N/A
border02          VX                   CL              x86_64   VX              N/A
fw1               VX                   CL              x86_64   VX              N/A
fw2               VX                   CL              x86_64   VX              N/A
leaf01            VX                   CL              x86_64   VX              N/A
leaf02            VX                   CL              x86_64   VX              N/A
leaf03            VX                   CL              x86_64   VX              N/A
oob-mgmt-server   N/A                  Ubuntu          x86_64   N/A             N/A
server01          N/A                  Ubuntu          x86_64   N/A             N/A
server02          N/A                  Ubuntu          x86_64   N/A             N/A
server03          N/A                  Ubuntu          x86_64   N/A             N/A
server04          N/A                  Ubuntu          x86_64   N/A             N/A
server05          N/A                  Ubuntu          x86_64   N/A             N/A
server06          N/A                  Ubuntu          x86_64   N/A             N/A
server07          N/A                  Ubuntu          x86_64   N/A             N/A
spine01           VX                   CL              x86_64   VX              N/A
spine02           VX                   CL              x86_64   VX              N/A
spine03           VX                   CL              x86_64   VX              N/A
spine04           VX                   CL              x86_64   VX              N/A
```

{{< /tab >}}

{{< tab "NetQ UI" >}}

### View the Number of Each Device Type in Your Network

You can view the number of switches and hosts deployed in your network. As you grow your network this can be useful for validating that devices have been added as scheduled.

To view the quantity of devices in your network, open the small Devices Inventory card.

{{< figure src="/images/netq/inventory-devices-small-240.png" width="200" >}}

### View All Switches

You can view all stored attributes for all switches in your network. To view all switch details, open the full screen Devices Inventory card and click the **All Switches** tab in the navigation panel.

{{< figure src="/images/netq/inventory-devices-fullscr-allswitches-tab-241.png" width="700" >}}

To return to your workbench, click <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/close.svg" height="14" width="14"/> in the top right corner of the card.

### View All Hosts

You can view all stored attributes for all hosts in your network. To view all hosts details, open the full screen Devices Inventory card and click the **All Hosts** tab in the navigation panel.

{{< figure src="/images/netq/inventory-devices-fullscr-allhosts-tab-241.png" width="700" >}}

To return to your workbench, click <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/close.svg" height="14" width="14"/> in the top right corner of the card.

{{< /tab >}}

{{< /tabs >}}

## View Switch Components

Switch component inventory can be viewed from either the NetQ CLI or NetQ UI.

{{< tabs "TabID95" >}}

{{< tab "NetQ CLI" >}}

To view switch components, run:

```
netq show inventory brief
```

This example shows the operating systems (Cumulus Linux and Ubuntu), CPU architecture (all x86_64), ASIC (virtual), and ports (none, since virtual) for each device in the network. You can manually count the number of each of these, or export to a spreadsheet tool to sort and filter the list.

```
cumulus@switch:~$ netq show inventory brief
Matching inventory records:
Hostname          Switch               OS              CPU      ASIC            Ports
----------------- -------------------- --------------- -------- --------------- -----------------------------------
border01          VX                   CL              x86_64   VX              N/A
border02          VX                   CL              x86_64   VX              N/A
fw1               VX                   CL              x86_64   VX              N/A
fw2               VX                   CL              x86_64   VX              N/A
leaf01            VX                   CL              x86_64   VX              N/A
leaf02            VX                   CL              x86_64   VX              N/A
leaf03            VX                   CL              x86_64   VX              N/A
oob-mgmt-server   N/A                  Ubuntu          x86_64   N/A             N/A
server01          N/A                  Ubuntu          x86_64   N/A             N/A
server02          N/A                  Ubuntu          x86_64   N/A             N/A
server03          N/A                  Ubuntu          x86_64   N/A             N/A
server04          N/A                  Ubuntu          x86_64   N/A             N/A
server05          N/A                  Ubuntu          x86_64   N/A             N/A
server06          N/A                  Ubuntu          x86_64   N/A             N/A
server07          N/A                  Ubuntu          x86_64   N/A             N/A
spine01           VX                   CL              x86_64   VX              N/A
spine02           VX                   CL              x86_64   VX              N/A
spine03           VX                   CL              x86_64   VX              N/A
spine04           VX                   CL              x86_64   VX              N/A
```

{{< /tab >}}

{{< tab "NetQ UI" >}}

To view switch components:

1. Locate the Inventory|Devices card on your workbench.

2. Hover of the card, and switch to the large size card using the size picker.

    By default the Switches tab is shown displaying the total number of switches, ASIC vendors, OS versions, license status, NetQ Agent versions, and specific platforms deployed on all of your switches.

    {{< figure src="/images/netq/inventory-devices-large-switches-tab-230.png" width="500" >}}

You can hover over any of the segments in a component distribution chart to highlight a specific type of the given component. When you *hover*, a tooltip appears displaying:

- the name or value of the component type, such as the version number or status
- the total number of switches with that type of component deployed compared to the total number of switches
- percentage of this type with respect to all component types.  

    {{< figure src="/images/netq/inventory-devices-large-switches-tab-component-highlight-230.png" width="650" >}}

Additionally, sympathetic highlighting is used to show the related component types relevant to the highlighted segment and the number of unique component types associated with this type (shown in blue here).

{{< /tab >}}

{{< /tabs >}}

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

{{< /tab >}}

{{< /tabs >}}

## View Which Operating Systems Are Running on Your Network Devices

You can view the distribution of operating systems running on your switches and hosts. This is useful for verifying which versions of the OS are deployed and for upgrade planning. It also provides a view into the relative dependence on a given OS in your network.

To view the OS distribution, open the medium Devices Inventory card if it is not already on your workbench.

{{< figure src="/images/netq/inventory-devices-medium-230.png" width="200" >}}
