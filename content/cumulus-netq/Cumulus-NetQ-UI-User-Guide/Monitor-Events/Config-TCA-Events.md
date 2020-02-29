---
title: Configure Threshold-based Events
author: Cumulus Networks
weight: 326
aliases:
 - /display/NETQ/Monitor+Events
 - /pages/viewpage.action?pageId=12321771
pageID: 12321771

toc: 4
---
NetQ supports a set of events that are triggered by crossing a user-defined threshold. These events allow detection and prevention of network failures for selected interface, utilization,  sensor, forwarding, and ACL events.

A notification configuration must contain one rule. Each rule must contain a scope and a threshold.

## Supported Events

The following events are supported:

| Category | Event ID | Description |
| ----------- | ---------- | -------------- |
| Interface Statistics | TCA_RXBROADCAST_UPPER  |  rx_broadcast bytes per second on a given switch or host is greater than maximum threshold |
| Interface Statistics | TCA_RXBYTES_UPPER |  rx_bytes per second on a given switch or host is greater than maximum threshold |
| Interface Statistics | TCA_RXMULTICAST_UPPER |  rx_multicast per second on a given switch or host is greater than maximum threshold |
| Interface Statistics | TCA_TXBROADCAST_UPPER |  tx_broadcast bytes per second on a given switch or host is greater than maximum threshold |
| Interface Statistics | TCA_TXBYTES_UPPER     |  tx_bytes per second on a given switch or host is greater than maximum threshold |
| Interface Statistics | TCA_TXMULTICAST_UPPER |  tx_multicast bytes per second on a given switch or host is greater than maximum threshold |
| Resource Utilization | TCA_CPU_UTILIZATION_UPPER | CPU utilization (%) on a given switch or host is greater than maximum threshold |
| Resource Utilization | TCA_DISK_UTILIZATION_UPPER  |  Disk utilization (%) on a given switch or host is greater than maximum threshold |
| Resource Utilization | TCA_MEMORY_UTILIZATION_UPPER  |  Memory utilization (%) on a given switch or host is greater than maximum threshold |
| Sensors | TCA_SENSOR_FAN_UPPER  |  Switch sensor reported fan speed on a given switch or host is greater than maximum threshold |
| Sensors | TCA_SENSOR_POWER_UPPER|  Switch sensor reported power (Watts) on a given switch or host is greater than maximum threshold |
| Sensors | TCA_SENSOR_TEMPERATURE_UPPER  |  Switch sensor reported temperature (&deg;C) on a given switch or host is greater than maximum threshold |
| Sensors | TCA_SENSOR_VOLTAGE_UPPER  |  Switch sensor reported voltage (Volts) on a given switch or host is greater than maximum threshold |
| Forwarding Resources | TCA_TCAM_TOTAL_ROUTE_ENTRIES_UPPER | Number of routes on a given switch or host is greater than maximum threshold |
| Forwarding Resources | TCA_TCAM_TOTAL_MCAST_ROUTES_UPPER | Number of multicast routes on a given switch or host is greater than maximum threshold |
| Forwarding Resources | TCA_TCAM_MAC_ENTRIES_UPPER | Number of MAC addresses on a given switch or host is greater than maximum threshold |
| Forwarding Resources | TCA_TCAM_IPV4_ROUTE_UPPER | Number of IPv4 routes on a given switch or host is greater than maximum threshold |
| Forwarding Resources | TCA_TCAM_IPV4_HOST_UPPER | Number of IPv4 hosts on a given switch or host is greater than maximum threshold |
| Forwarding Resources | TCA_TCAM_IPV6_ROUTE_UPPER | Number of IPv6 hosts on a given switch or host is greater than maximum threshold |
| Forwarding Resources | TCA_TCAM_IPV6_HOST_UPPER | Number of IPv6 hosts on a given switch or host is greater than maximum threshold |
| Forwarding Resources | TCA_TCAM_ECMP_NEXTHOPS_UPPER | Number of equal cost multi-path (ECMP) next hop entries on a given switch or host is greater than maximum threshold |
| ACL Resources | TCA_TCAM_IN_ACL_V4_FILTER_UPPER | Number of ingress ACL filters for IPv4 addresses on a given switch or host is greater than maximum threshold |
| ACL Resources | TCA_TCAM_EG_ACL_V4_FILTER_UPPER | Number of egress ACL filters for IPv4 addresses on a given switch or host is greater than maximum threshold |
| ACL Resources | TCA_TCAM_IN_ACL_V4_MANGLE_UPPER | Number of ingress ACL mangles for IPv4 addresses on a given switch or host is greater than maximum threshold |
| ACL Resources | TCA_TCAM_EG_ACL_V4_MANGLE_UPPER | Number of egress ACL mangles for IPv4 addresses on a given switch or host is greater than maximum threshold |
| ACL Resources | TCA_TCAM_IN_ACL_V6_FILTER_UPPER | Number of ingress ACL filters for IPv6 addresses on a given switch or host is greater than maximum threshold |
| ACL Resources | TCA_TCAM_EG_ACL_V6_FILTER_UPPER | Number of egress ACL filters for IPv6 addresses on a given switch or host is greater than maximum threshold |
| ACL Resources | TCA_TCAM_IN_ACL_V6_MANGLE_UPPER | Number of ingress ACL mangles for IPv6 addresses on a given switch or host is greater than maximum threshold |
| ACL Resources | TCA_TCAM_EG_ACL_V6_MANGLE_UPPER | Number of egress ACL mangles for IPv6 addresses on a given switch or host is greater than maximum threshold |
| ACL Resources | TCA_TCAM_IN_ACL_8021x_FILTER_UPPER | Number of ingress ACL 802.1 filters on a given switch or host is greater than maximum threshold |
| ACL Resources | TCA_TCAM_ACL_L4_PORT_CHECKERS_UPPER | Number of ACL port range checkers on a given switch or host is greater than maximum threshold |
| ACL Resources | TCA_TCAM_ACL_REGIONS_UPPER | Number of ACL regions on a given switch or host is greater than maximum threshold |
| ACL Resources | TCA_TCAM_IN_ACL_MIRROR_UPPER | Number of ingress ACL mirrors on a given switch or host is greater than maximum threshold |
| ACL Resources | TCA_TCAM_ACL_18B_RULES_UPPER | Number of ACL 18B rules on a given switch or host is greater than maximum threshold |
| ACL Resources | TCA_TCAM_ACL_32B_RULES_UPPER | Number of ACL 32B rules on a given switch or host is greater than maximum threshold |
| ACL Resources | TCA_TCAM_ACL_54B_RULES_UPPER | Number of ACL 54B rules on a given switch or host is greater than maximum threshold |
| ACL Resources | TCA_TCAM_IN_PBR_V4_FILTER_UPPER | Number of ingress policy-based routing (PBR) filters for IPv4 addresses on a given switch or host is greater than maximum threshold |
| ACL Resources | TCA_TCAM_IN_PBR_V6_FILTER_UPPER | Number of ingress policy-based routing (PBR) filters for IPv6 addresses on a given switch or host is greater than maximum threshold |

### Define a Scope

A scope is used to filter the events generated by a given rule. Scope values are set on a per TCA rule basis. All rules can be filtered on Hostname. Some rules can also be filtered by other parameters, as shown in this

| Category | Event ID | Scope Parameters |
| ------------ | ---------- | -------------- |
| Interface Statistics | TCA_RXBROADCAST_UPPER  | Hostname, Interface |
| Interface Statistics | TCA_RXBYTES_UPPER | Hostname, Interface |
| Interface Statistics | TCA_RXMULTICAST_UPPER | Hostname, Interface |
| Interface Statistics | TCA_TXBROADCAST_UPPER | Hostname, Interface |
| Interface Statistics | TCA_TXBYTES_UPPER | Hostname, Interface |
| Interface Statistics | TCA_TXMULTICAST_UPPER | Hostname, Interface |
| Resource Utilization | TCA_CPU_UTILIZATION_UPPER | Hostname |
| Resource Utilization | TCA_DISK_UTILIZATION_UPPER  | Hostname |
| Resource Utilization | TCA_MEMORY_UTILIZATION_UPPER  | Hostname |
| Sensors | TCA_SENSOR_FAN_UPPER  | Hostname, Sensor Name |
| Sensors | TCA_SENSOR_POWER_UPPER| Hostname, Sensor Name |
| Sensors | TCA_SENSOR_TEMPERATURE_UPPER  | Hostname, Sensor Name |
| Sensors | TCA_SENSOR_VOLTAGE_UPPER  | Hostname, Sensor Name |
| Forwarding Resources | TCA_TCAM_TOTAL_ROUTE_ENTRIES_UPPER | Hostname |
| Forwarding Resources | TCA_TCAM_TOTAL_MCAST_ROUTES_UPPER | Hostname |
| Forwarding Resources | TCA_TCAM_MAC_ENTRIES_UPPER | Hostname |
| Forwarding Resources | TCA_TCAM_ECMP_NEXTHOPS_UPPER | Hostname |
| Forwarding Resources | TCA_TCAM_IPV4_ROUTE_UPPER | Hostname |
| Forwarding Resources | TCA_TCAM_IPV4_HOST_UPPER | Hostname |
| Forwarding Resources | TCA_TCAM_IPV6_ROUTE_UPPER | Hostname |
| Forwarding Resources | TCA_TCAM_IPV6_HOST_UPPER | Hostname |
| ACL Resources | TCA_TCAM_IN_ACL_V4_FILTER_UPPER | Hostname |
| ACL Resources | TCA_TCAM_EG_ACL_V4_FILTER_UPPER | Hostname |
| ACL Resources | TCA_TCAM_IN_ACL_V4_MANGLE_UPPER | Hostname |
| ACL Resources | TCA_TCAM_EG_ACL_V4_MANGLE_UPPER | Hostname |
| ACL Resources | TCA_TCAM_IN_ACL_V6_FILTER_UPPER | Hostname |
| ACL Resources | TCA_TCAM_EG_ACL_V6_FILTER_UPPER | Hostname |
| ACL Resources | TCA_TCAM_IN_ACL_V6_MANGLE_UPPER | Hostname |
| ACL Resources | TCA_TCAM_EG_ACL_V6_MANGLE_UPPER | Hostname |
| ACL Resources | TCA_TCAM_IN_ACL_8021x_FILTER_UPPER | Hostname |
| ACL Resources | TCA_TCAM_ACL_L4_PORT_CHECKERS_UPPER | Hostname |
| ACL Resources | TCA_TCAM_ACL_REGIONS_UPPER | Hostname |
| ACL Resources | TCA_TCAM_IN_ACL_MIRROR_UPPER | Hostname |
| ACL Resources | TCA_TCAM_ACL_18B_RULES_UPPER | Hostname |
| ACL Resources | TCA_TCAM_ACL_32B_RULES_UPPER | Hostname |
| ACL Resources | TCA_TCAM_ACL_54B_RULES_UPPER | Hostname |
| ACL Resources | TCA_TCAM_IN_PBR_V4_FILTER_UPPER | Hostname |
| ACL Resources | TCA_TCAM_IN_PBR_V6_FILTER_UPPER | Hostname |

Scopes are displayed as regular expressions in the rule card.

| Scope | Display in Card | Result |
| ------- | ------------------- | ------- |
| All devices | hostname = * | Show events for all devices |
| All interfaces | ifname = * | Show events for all devices and all interfaces |
| All sensors | s_name = * | Show events for all devices and all sensors |
| Particular device | hostname = leaf01 | Show events for *leaf01* switch |
| Particular interfaces | ifname = swp14 | Show events for *swp14* interface |
| Particular sensors | s_name = fan2 | Show events for the *fan2* fan |
| Set of devices | hostname ^ leaf | Show events for switches having names starting with *leaf* |
| Set of interfaces | ifname ^ swp | Show events for interfaces having names starting with *swp* |
| Set of sensors | s_name ^ fan | Show events for sensors having names starting with *fan* |

When a rule is filtered by more than one parameter, each is displayed on the card. Leaving a value blank for a parameter defaults to all; all hostnames, interfaces, or sensors.

### Create a TCA Rule

Now that you know which events are supported and how to set the scope, you can create a basic rule to deliver one of the TCA events to a notification channel.

To create a TCA rule:

1. Click <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/03-Menu/navigation-menu.svg" height="18" width="18"/> to open the Main Menu.

    {{<figure src="/images/netq/main-menu-tca-selected-241.png" width="600">}}

2. Click *Threshold Crossing Rules* under **Notifications**.

3. Click <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/43-Remove-Add/add-circle.svg" height="18" width="18"/> to add a rule.

    The Create TCA Rule dialog opens. Three steps create the rule.

    {{<figure src="/images/netq/tca-create-rule-details-tab-241.png" width="500">}}

    Note that you can move forward and backward until you are satisfied with your rule definition.

4. On the **Enter Details** step, enter a name for your rule, choose your TCA event type, and assign a severity.

    **Note**: The rule name has a maximum of 20 characters (including spaces).

5. Click **Next**.

6. On the **Choose Event** step, select the attribute to measure against.

    {{<figure src="/images/netq/tca-create-rule-event-tab-241.png" width="500">}}

    **Note**: The attributes presented depend on the event type chosen in the *Enter Details* step. This example shows the attributes available when *Resource Utilization* was selected.

7. Click **Next**.

8. On the **Set Threshold** step, enter a threshold value.

    If you stop there and click **Finish**, the event is triggered for all monitored devices in the network.

    {{<figure src="/images/netq/tca-create-rule-threshold-tab-241.png" width="500">}}

    If you want to restrict the rule to a particular device, toggle the scope filter and enter a hostname or other parameter values. Then click **Finish**.

    {{<figure src="/images/netq/tca-create-rule-apply-toggle-241.png" width="450">}}

This example shows two rules. The rule on the left triggers an informational event when switch *leaf01* exceeds the maximum CPU utilization of 87%. The rule on the right triggers a critical event when any device exceeds the maximum CPU utilization of 93%. Note that the cards indicate both rules are currently Active.

{{<figure src="/images/netq/tca-create-rule-examples-241.png" width="420">}}

## View All TCA Rules

You can view all of the threshold-crossing event rules you have created by clicking <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/03-Menu/navigation-menu.svg" height="18" width="18"/> and then selecting *Threshold Crossing Rules* under **Notifications**.

## Modify TCA Rules

You can modify the threshold value and scope of any existing rules.

To edit a rule:

1. Click <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/03-Menu/navigation-menu.svg" height="18" width="18"/> to open the Main Menu.

2. Click *Threshold Crossing Rules* under **Notifications**.

3. Locate the rule you want to modify and hover over the card.

4. Click <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/22-Edit/pencil-1.svg" height="18" width="18"/>.

    {{<figure src="/images/netq/tca-edit-rule-241.png" width="200">}}

5. Modify the rule or the scope.

    {{<figure src="/images/netq/tca-edit-rule-example-241.png" width="500">}}

6. Click **Update Rule**.

{{%notice tip%}}
If you want to modify the rule name or severity after creating the rule, you must delete the rule and recreate it.
{{%/notice%}}

## Manage TCA Rules

Once you have created a bunch of rules, you might have the need to manage them; suppress a rule, disable a rule, or delete a rule.

### Rule States

The TCA rules have three possible states:

- **Active**: Rule is operating, delivering events. This would be the normal operating state.
- **Suppressed**: Rule is disabled until a designated date and time. When that time occurs, the rule is automatically re-enabled. This state is useful during troubleshooting or maintenance of a switch when you do not want erroneous events being generated.
- **Disabled**: Rule is disabled until a user manually re-enables it. This state is useful when you are unclear when you want the rule to be re-enabled. This is not the same as deleting the rule.

### Suppress a Rule

To suppress a rule for a designated amount of time, you must change the state of the rule.

To suppress a rule:

1. Click <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/03-Menu/navigation-menu.svg" height="18" width="18"/> to open the Main Menu.

2. Click *Threshold Crossing Rules* under **Notifications**.

3. Locate the rule you want to suppress.

4. Click **Disable**.

    {{<figure src="/images/netq/tca-suppress-rule-241.png" width="300">}}

5. Click in the **Date/Time** field to set when you want the rule to be automatically re-enabled.

6. Click **Disable**.

    {{<figure src="/images/netq/tca-suppress-rule-example-241.png" width="200">}}

    Note the changes in the card:

    - The state is now marked as *Inactive*,  but remains green
    - The date and time that the rule will be enabled is noted in the **Suppressed** field
    - The **Disable** option has changed to **Disable Forever**. Refer to [Disable a Rule](#disable-a-rule) for information about this change.

### Disable a Rule

To disable a rule until you want to manually re-enable it, you must change the state of the rule.

To disable a rule that is currently active:

1. Click <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/03-Menu/navigation-menu.svg" height="18" width="18"/> to open the Main Menu.

2. Click *Threshold Crossing Rules* under **Notifications**.

3. Locate the rule you want to disable.

4. Click **Disable**.

5. Leave the **Date/Time** field blank.

6. Click **Disable**.

    {{<figure src="/images/netq/tca-disable-rule-example-241.png" width="200">}}

    Note the changes in the card:

    - The state is now marked as *Inactive* and is red
    - The rule definition is grayed out
    - The **Disable** option has changed to **Enable** to reactivate the rule when you are ready

To disable a rule that is currently suppressed:

1. Click <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/03-Menu/navigation-menu.svg" height="18" width="18"/> to open the Main Menu.

2. Click *Threshold Crossing Rules* under **Notifications**.

3. Locate the rule you want to disable.

4. Click **Disable Forever**.

    Note the changes in the card:

    - The state is now marked as *Inactive* and is red
    - The rule definition is grayed out
    - The **Disable** option has changed to **Enable** to reactivate the rule when you are ready

### Delete a Rule

You might find that you no longer want to received event notifications for a particular TCA event. In that case, you can either disable the event if you think you may want to receive them again or delete the rule altogether. Refer to [Disable a Rule](#disable-a-rule) in the first case. Follow the instructions here to remove the rule. The rule can be in any of the three states.

To delete a rule:

1. Click <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/03-Menu/navigation-menu.svg" height="18" width="18"/> to open the Main Menu.

2. Click *Threshold Crossing Rules* under **Notifications**.

3. Locate the rule you want to remove and hover over the card.

4. Click <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/23-Delete/bin-1.svg" height="18" width="18"/>.

{{<figure src="/images/netq/tca-delete-rule-241.png" width="200">}}

### Resolve Scope Conflicts

There may be occasions where the scope defined by multiple rules for a given TCA event may overlap each other. In such cases, the TCA rule with the most specific scope that is still true is used to generate the event.

To clarify this, consider this example. Three events have occurred:

- First event on switch *leaf01*, interface *swp1*
- Second event on switch *leaf01*, interface *swp3*
- Third event on switch *spine01*, interface *swp1*

NetQ attempts to match the TCA event against hostname and interface name with three TCA rules with different scopes:

- Scope 1 send events for the *swp1* interface on switch *leaf01* (very specific)
- Scope 2 send events for all interfaces on switches that start with *leaf* (moderately specific)
- Scope 3 send events for all switches and interfaces (very broad)

The result is:

- For the first event, NetQ applies the scope from rule 1 because it matches scope 1 exactly
- For the second event, NetQ applies the scope from rule 2 because it does not match scope 1, but does match scope 2
- For the third event, NetQ applies the scope from rule 3 because it does not match either scope 1 or scope 2

In summary:

| Input Event | Scope Parameters | Rule 1, Scope 1 | Rule 2, Scope 2 | Rule 3, Scope 3 | Scope Applied |
| --- | --- | --- | --- | --- | --- |
| leaf01, swp1 | Hostname, Interface | hostname=leaf01, ifname=swp1 | hostname ^ leaf, ifname=\* | hostname=\*, ifname=\* | Scope 1 |
| leaf01, swp3 | Hostname, Interface | hostname=leaf01, ifname=swp1 | hostname ^ leaf, ifname=\* | hostname=\*, ifname=\* | Scope 2 |
| spine01, swp1 | Hostname, Interface | hostname=leaf01, ifname=swp1 | hostname ^ leaf, ifname=\* | hostname=\*, ifname=\* | Scope 3 |
