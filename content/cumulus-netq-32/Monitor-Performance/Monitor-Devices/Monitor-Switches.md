---
title: Monitor Switches
author: Cumulus Networks
weight: 830
toc: 4
---
With the NetQ UI, you can monitor individual switches separately from the network. You are able to view the status of services they are running, health of its various components, and connectivity performance. Being able to monitor switch component inventory aids in upgrade, compliance, and other planning tasks. Viewing individual switch health helps isolate performance issues.

## View the Overall Health of a Switch

When you want to monitor the health of a particular switch, open the small Switch card. It is unlikely that you would have this card open for every switch in your network at the same time, but it is useful for tracking selected switches that may have been problematic in the recent past or that you have recently installed. The card shows you alarm status and summary performance score and trend.

To view the summary:

1. Click <img src="https://icons.cumulusnetworks.com/44-Entertainment-Events-Hobbies/02-Card-Games/card-game-diamond.svg" height="18" width="18"/>, and select Device|Switches. A dialog box opens.

    {{< figure src="/images/netq/dev-switch-open-switch-card.png" width="250" >}}

2. Begin typing the hostname of the device you are interested in. Select it from the suggested matches when it appears.

    {{< figure src="/images/netq/dev-switch-type-dev-name.png" width="250" >}}

3. Select *small* to open the small size card.

    {{< figure src="/images/netq/dev-switch-choose-card-size.png" width="250" >}}

4. Click **Add**, or **Cancel** to exit the process.

    {{<figure src="/images/netq/dev-switch-small-card-230.png" width="200">}}

In this example, we see that the leaf01 switch has had very few alarms overall, but the number is trending upward, with a total count of 24 alarms currently.

## View Health Performance Metrics

When you are monitoring switches that have been problematic or are newly installed, you might want to view more than a summary. Instead, seeing key performance metrics can help you determine where issues might be occurring or how new devices are functioning in the network.

To view the key metrics, open the medium Switch card. The card shows you the overall switch health score and the scores for the key metrics that comprise that score. The key metric scores are based on the number of alarms attributed to the following activities on the switch:

- Network services, such as BGP, EVPN, MLAG, NTP, and so forth
- Scheduled traces
- Interface performance
- Platform performance

{{<figure src="/images/netq/dev-switch-medium-alarms-charts-231.png" width="420">}}

Also included on the card is the total alarm count for all of these metrics. You can view the key performance metrics as numerical scores or as line charts over time, by clicking **Charts** or **Alarms** at the top of the card.

## View Attributes of a Switch

For a quick look at the key attributes of a particular switch, open the large Switch card. Attributes are displayed as the default tab.

{{< figure src="/images/netq/dev-switch-large-attributes-tab-230.png" width="500" >}}

In this example, the items of interest might be the five interfaces that are down and what version of OS and NetQ Agent the switch is running.

## View Current Resource Utilization for a Switch

The NetQ GUI enables you to easily view the performance of various hardware components and the network tables. This enables you to determine whether a switch is reaching its maximum load and compare its performance with other switches.

To view the resource utilization on a particular switch:

1. Open the large Switch card.

2. Hover over the card and click <img src="https://icons.cumulusnetworks.com/06-Business-Products/12-Analytics/analytics-bars.svg" height="18" width="18"/>.

3. The card is divided into two sections, displaying hardware-related performance through a series of charts.

    {{<figure src="/images/netq/dev-switch-large-utilization-tab-230.png" width="500">}}

4. Look at the hardware performance charts. Are there any that are reaching critical usage levels?

5. Is usage high at a particular time of day?

6. Change the time period. Is the performance about the same? Better? Worse? The results can guide your decisions about upgrade options.

7. Open a different Switch card for a comparable switch. Is the performance similar?

## View Interface Statistics for a Switch

If you suspect that a particular switch is having performance problems, you might want to view the status of its interfaces. The statistics can also provide insight into interfaces that are more heavily loaded than others.

To view interface statistics:

1. Click <img src="https://icons.cumulusnetworks.com/03-Computers-Devices-Electronics/09-Hard-Drives/hard-drive-1.svg" width="18" height="18"/>.

2. Begin typing the name of the switch of interest, and select when it appears in the suggestions list.

3. Select the *Large* card size.

4. Click **Add**.

5. Hover over the card and click <img src="https://icons.cumulusnetworks.com/05-Internet-Networks-Servers/07-Data-Transfer/data-transfer-square-diagonal.svg" width="18" height="18"/> to open the Interface Stats tab.

    {{<figure src="/images/netq/dev-switch-large-interfaces-tab-230.png" width="500">}}

6. Select an interface from the list, scrolling down until you find it. By default the interfaces are sorted by Name, but you may find it easier to sort by the highest transmit or receive utilization using the filter above the list.

7. The charts update according to your selection. Scroll up and down to view the individual statistics.

What you view next depends on what you see, but a couple of possibilities include:

- Open the full screen card to view details about all of the IP addresses, MAC addresses, and interfaces on the switch.
- Open another switch card to compare performance on a similar interface.

## View All Addresses for a Switch

It can be useful to view all of the configured addresses that this switch is using. You can view all IP addresses or all MAC addresses using the full screen Switch card.

To view all IP addresses:

1. Open the full screen Switch card. Click **IP addresses**.

    {{<figure src="/images/netq/dev-switch-fullscr-ipaddr-tab-241.png" width="700">}}

    By default **All** IP addresses are selected. Click **IPv6** or **IPv4** above the table to view only those IP addresses.

2. Review the addresses for any anomalies, to obtain prefix information, determine if it is an IPv4 or IPv6 address, and so forth.

3. To return to the workbench, click <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/close.svg" height="14" width="14"/> in the top right corner.

To view all MAC addresses:

1. Open the full screen Switch card and click **MAC Addresses**.

    {{<figure src="/images/netq/dev-switch-fullscr-macaddr-tab-241.png" width="700">}}

2. Review the addresses for any anomalies, to see the associated egress port, associated VLANs, and so forth.

3. To return to the workbench, click <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/close.svg" height="14" width="14"/> in the top right corner.

## View All Interfaces on a Switch

You can view all of the configured interfaces on a switch in one place making it easier to see inconsistencies in the configuration, quickly see when changes were made, and the operational status.

To view all interfaces:

1. Open the full-screen Switch card and click **All Interfaces**.

    {{<figure src="/images/netq/dev-switch-fullscr-interfaces-tab-241.png" width="700">}}

2. Look for interfaces that are down, shown in the **State** column.

3. Look for recent changes to the interfaces, shown in the **Last Changed** column.

4. View details about each interface, shown in the **Details** column.

5. Verify they are of the correct kind for their intended function, shown in the **Type** column.

6. Verify the correct VRF interface is assigned to an interface, shown in the **VRF** column.

7. To return to the workbench, click <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/close.svg" height="14" width="14"/> in the top right corner.

## View All Software Packages on a Switch

You can view all of the software installed on a given switch to quickly validate versions and total software installed.

To view all software packages:

1. Open the full-screen Switch card and click **Installed Packages**.

    {{<figure src="/images/netq/dev-switch-fullscr-pkgs-tab-241.png" width="700">}}

2. Look for packages of interest and their version and status. Sort by a particular parameter by clicking <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/15-Filter/filter-1.svg" height="18" width="18"/>.

    {{<figure src="/images/netq/dev-switch-fullscr-filter-by-pkgname-241.png" width="300">}}

3. Optionally, export the list by selecting all or specific packages, then clicking <img src="https://icons.cumulusnetworks.com/05-Internet-Networks-Servers/08-Upload-Download/upload-bottom.svg" height="18" width="18"/>.

## View Disk Storage After BTRFS Allocation

Customers running Cumulus Linux 3.x which uses the BTRFS (b-tree file system) might experience issues with disk space management. This is a known problem of BTRFS because it does not perform periodic garbage collection, or rebalancing. If left unattended, these errors can make it impossible to rebalance the partitions on the disk. To avoid this issue, Cumulus Networks recommends rebalancing the BTRFS partitions in a preemptive manner, but only when absolutely needed to avoid reduction in the lifetime of the disk. By tracking the state of the disk space usage, users can determine when rebalancing should be performed. For details about when a rebalance is recommended, refer to {{<exlink url="https://support.cumulusnetworks.com/hc/en-us/articles/360037394933-When-to-Rebalance-BTRFS-Partitions" text="When to Rebalance BTRFS Partitions">}}.

To view the disk state:

1. Open the full-screen Switch card for a switch of interest:

     - Type the switch name in the Search box, then use the card size picker to open the full-screen card, or 
     - Click <img src="https://icons.cumulusnetworks.com/03-Computers-Devices-Electronics/09-Hard-Drives/hard-drive-1.svg" height="24" width="24"/> (Switches) and enter the switch name and select the full-screen card size.

2. Click **BTRFS Utilization**.

    {{<figure src="/images/netq/dev-switch-fullscr-btrfs-util-tab-241.png" width="700">}}

3. Look for the **Rebalance Recommended** column.

    If the value in that column says *Yes*, then you are strongly encouraged to rebalance the BTRFS partitions. If it says *No*, then you can review the other values in the table to determine if you are getting close to needing a rebalance, and come back to view this table at a later time.

## View SSD Utilization

For NetQ servers and appliances that have 3ME3 solid state drives (SSDs) installed (primarily in on-premises deployments), you can view the utilization of the drive on-demand. An alarm is generated for drives that drop below 10% health, or have more than a two percent loss of health in 24 hours, indicating the need to rebalance the drive. Tracking SSD utiilization over time enables you to see any downward trend or instability of the drive before you receive an alarm.

To view SSD utilization:

1. Open the full screen Switch card and click **SSD Utilization**.

    {{<figure src="/images/netq/dev-switch-fullscr-ssd-tab-241.png" width="700">}}

2. View the average PE Cycles value for a given drive. Is it higher than usual?

3. View the Health value for a given drive. Is it lower than  usual? Less than 10%?

Consider adding the switch cards that are suspect to a workbench for easy tracking.

## View a Summary of Communication Status for All Switches

A communication status summary for all of your switches across the network is available from the small Switch Inventory card.

{{<figure src="/images/netq/inventory-switch-small-230.png" width="200">}}

In this example, we see all 13 switches have been heard from recently (they are fresh).

## View the Number of Types of Any Component Deployed

For each of the components monitored on a switch, NetQ displays the variety of those component by way of a count. For example, if you have three operating systems running on your switches, say Cumulus Linux, Ubuntu and RHEL, NetQ indicates a total unique count of three OSs. If you only use Cumulus Linux, then the count shows as one.

To view this count for all of the components on the switch:

1. Open the medium Switch Inventory card.

    {{<figure src="/images/netq/inventory-switch-medium-320.png" width="200">}}

2. Note the number in the **Unique** column for each component.

    In the above example, there are four different disk sizes deployed, four different OSs running, four different ASIC vendors and models deployed, and so forth.

3. Scroll down to see additional components.

By default, the data is shown for switches with a fresh communication status. You can choose to look at the data for switches in the rotten state instead. For example, if you wanted to see if there was any correlation to a version of OS to the switch having a rotten status, you could select **Rotten Switches** from the dropdown at the top of the card and see if they all use the same OS (count would be 1). It may not be the cause of the lack of communication, but you get the idea.

## View the Distribution of Any Component Deployed

NetQ monitors a number of switch components. For each component you can view the distribution of versions or models or vendors deployed across your network for that component.

To view the distribution:

1. Open the medium or large Switch Inventory card. Each component has a chart showing the distribution.  

    {{<figure src="/images/netq/inventory-switch-medium-230.png" width="200">}}

    OR

    {{<figure src="/images/netq/inventory-switch-large-summary-tab-230.png" width="500">}}

2. Hover over a segment of the chart to view the name, version, model or vendor and the number of switches that have been deployed. You can also see the percentage of all switches this total represents. On the large Switch Inventory card, hovering also highlights the related components for the selected component. This is shown in blue here.

    {{<figure src="/images/netq/inventory-switch-large-summary-tab-hover-os-230.png" width="500">}}

3. Point to additional segments on that component or other components to view their detail.

4. Scroll down to view additional components.

## View the Number of Switches with Invalid or Missing Licenses

It is important to know when you have switches that have invalid or missing Cumulus Linux licenses, as not all of the features are operational without a valid license. Simply open the medium or large Switch Inventory card, and hover over the License chart to see the count.

{{<figure src="/images/netq/inventory-switch-medium-hover-license-230.png" width="200">}}

To view which vendors and platforms have bad or missing licenses, open the large Switch Inventory card, and click {{<img src="/images/netq/platform-icon.png" height="18" width="18">}} to open the **Platform** tab. Hover over the License State bar chart to highlight the vendor and platforms with the various states.

To view *which* switches have invalid or missing licenses, either:

- Hover over the large Switch Inventory card and click {{<img src="/images/netq/platform-icon.png" height="18" width="18">}} to open the **Platform** tab. Above the Licenses State or the Vendor chart, click **Show All**.
      {{< figure src="/images/netq/inventory-switch-large-platform-tab.png" width="500" >}}
- Open the full screen Switch Inventory card. Then sort the **All Switches** tab data table by the **License State** column to locate the switches with bad or missing licenses.
      {{< figure src="/images/netq/inventory-switch-fullscr-show-all-tab-license-highlight.png" width="700" >}}

## View the Most Commonly Deployed ASIC

It can be useful to know the quantity and ratio of many components deployed in your network to determine the scope of upgrade tasks, balance vendor reliance, or for detailed troubleshooting. You can view the most commonly deployed components in generally the same way. Some components have additional details contained in large card tabs.

To view the most commonly deployed ASIC, for example:

1. Open the medium or large Switch Inventory card.

2. Hover over the *largest* segment in the ASIC chart. The tooltip that appears shows you the number of switches with the given ASIC and the percentage of your entire switch population with this ASIC.  

    {{<figure src="/images/netq/inventory-switch-medium-asic-highlight-230.png" width="200">}}

    Click on any other component in a similar fashion to see the most common type of that component.

3. If you opened the medium Switch Inventory card, switch to the large card.

4. Hover over the card, and click <img src="https://icons.cumulusnetworks.com/03-Computers-Devices-Electronics/08-Microprocessor-Chips/computer-chip-core-1.svg" height="18" width="18"/> to open the **ASIC** tab. Here you can more easily view the various vendors and platforms based on the ASIC deployed.

5. *Hover* over the **Vendor** pie chart to highlight which platforms are supported by the vendor and vice versa; hover over the **Model** pie chart to see which vendor supports that platform. Moving your cursor off of the charts removes the highlight.

    {{<figure src="/images/netq/inventory-switch-large-asic-tab-vendor-highlight-230.png" width="500">}}

6. *Click* on a segment of the **Vendor** pie chart to drill down and see only that Vendor and its supported models. A filter tag is placed at the top of the charts.

    {{<figure src="/images/netq/inventory-switch-large-asic-tab-vendor-selected-230.png" width="500">}}

7. To return to the complete view of vendors and platforms, click <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/close.svg" height="14" width="14"/> on the filter tag.

## View the Number of Switches with a Particular NetQ Agent

It is recommended that when you upgrade NetQ that you also upgrade the NetQ Agents. You can determine if you have covered all of your agents using the medium or large Switch Inventory card. To view the NetQ Agent distribution by version:

1. Open the medium Switch Inventory card.

2. View the number in the **Unique** column next to Agent.

    {{<figure src="/images/netq/inventory-switch-medium-agent-highlight-320.png" width="200">}}

3. If the number is greater than one, you have multiple NetQ Agent versions deployed.

4. If you have multiple versions, hover over the Agent chart to view the count of switches using each version.

5. For more detail, switch to the large Switch Inventory card.

6. Hover over the card and click <img src="https://icons.cumulusnetworks.com/03-Computers-Devices-Electronics/12-CD-Rom/cd.svg" height="20" width="20"/> to open the **Software** tab.  

    {{<figure src="/images/netq/inventory-switch-large-software-tab-230.png" width="500">}}

7. Hover over the chart on the right to view the number of switches using the various versions of the NetQ Agent.

8. Hover over the Operating System chart to see which NetQ Agent versions are being run on each OS.  

    {{<figure src="/images/netq/inventory-switch-large-software-tab-os-highlight-230.png" width="500">}}

9. Click either chart to focus on a particular OS or agent version.

10. To return to the full view, click <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/close.svg" height="14" width="14"/> in the filter tag.

11. Filter the data on the card by switches that are having trouble communicating, by selecting *Rotten Switches* from the dropdown above the charts.

## View a List of All Data for a Specific Component

When the small, medium and large Switch Inventory cards do not provide either enough information or are not organized in a fashion that provides the information you need, open the full screen Switch Inventory card. Select the component tab of interest and filter and sort as desired. Export the data to a third-party tool, by clicking <img src="https://icons.cumulusnetworks.com/05-Internet-Networks-Servers/08-Upload-Download/upload-bottom.svg" height="18" width="18"/>.

{{<figure src="/images/netq/inventory-switch-fullscr-show-all-tab-241.png" width="700">}}
