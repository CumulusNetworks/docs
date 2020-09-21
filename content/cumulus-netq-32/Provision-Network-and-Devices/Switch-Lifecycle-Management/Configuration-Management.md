---
title: Manage Switch Configurations
author: Cumulus Networks
weight: 660
toc: 4
---
You can configure switches using one or more configurations. To enable consistent application of configurations, switch configurations can contain network templates for SNMP, NTP, and user accounts. You can also configure configuration profiles for Cumulus NetQ Agents.

Workflow for config switches

## Manage Network Templates

Network templates provide administrators the option to create switch configuration profiles that can be applied to multiple switches. They can help reduce inconsistencies with switch configuration and speed the process of initial configuration and upgrades. No default templates are provided.

### View Network Templates

You can view existing templates using the Network Templates card.

{{<figure src="/images/netq/lcm-ntwk-template-medium-320.png" width="200">}}

Click **Manage** to view the list of existing switch templates.

### Create Network Templates

No default templates are provided on installation of NetQ. This enables you to create configurations that match your specifications.

To create a network template:

1. Open the Manage Switch Assets dashboard.

2. Click **Add** on the Network Templates card.

3. Decide which aspects of configuration you want included in this template: SNMP, NTP, and/or User accounts.

4. Configure the template using the following instructions.

{{< tabs "TabID37" >}}

{{< tab "SNMP" >}}

SNMP provides a way to query, monitor, and manage your devices in addition to NetQ. (required fields???)

1. Provide a name for the template. The maximum number of characters allowed, including spaces, is 22.

2. Enter a comma-separated list of IP addresses of the SNMP Agents on the switches and hosts in your network.

3. Accept the management VRF or change to the default VRF.

4. Enter contact information for the SNMP system administrator (who will receive the SNMP alerts???), including an email address or phone number, their location, and name.

5. Optionally, restrict the recipients that should receive the SNMP alerts to those in the Read only Community or Read only Community6.

    1. Enter an email address (typically an alias for a group of operators).

    2. Indicate which messages should be sent: any = send all messages; ??? = ???

6. Optionally, specify specific traps to be included:

7. If you are using SNMP version 3, open the V3 support section.

{{< /tab >}}

{{< tab "NTP" >}}

{{< /tab >}}

{{< tab "User Accounts" >}}

{{< /tab >}}

### Modify Network Templates

### Delete Network Templates

## Manage Switch Configuration Profiles

### View Switch Configuration Profiles

### Create Switch Configuration Profiles

### Assign Switch Configuration Profiles

### Change Switch Configuration Profile Assignment

#### Modify Assignment

#### Remove Assignment

### View Switch Configuration History

## Manage NetQ Configuration Profiles

You can set up a configuration profile to indicate how you want NetQ configured when it is installed or upgraded on your Cumulus Linux switches.

The default configuration profile, *NetQ default config*, is set up to run in the management VRF and provide info level logging. Both WJH and CPU Limiting are disabled.

You can view, add, and remove NetQ configuration profiles at any time.

### View Cumulus NetQ Configuration Profiles

To view existing profiles:

1. Click <img src="https://icons.cumulusnetworks.com/03-Computers-Devices-Electronics/09-Hard-Drives/hard-drive-1.svg" height="18" width="18"/> (Switches) in the workbench header, then click **Manage switches**, or click {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/03-Menu/navigation-menu.svg" height="18" width="18" alt="Main Menu">}} (Main Menu) and select **Upgrade Switches**.

2. Click **Manage** on the NetQ Configurations card.

    Note that the initial value on first installation of NetQ shows one profile. This is the default profile provided with NetQ.

    {{<figure src="/images/netq/lcm-netq-config-card-on-install-310.png" width="200">}}

3. Review the profiles.

    {{<figure src="/images/netq/lcm-netq-config-profiles-list-310.png" width="550">}}

### Create Cumulus NetQ Configuration Profiles

You can specify four options when creating NetQ configuration profiles:

- Basic: VRF assignment and Logging level
- Advanced: CPU limit and what just happened (WJH)

To create a profile:

1. Click <img src="https://icons.cumulusnetworks.com/03-Computers-Devices-Electronics/09-Hard-Drives/hard-drive-1.svg" height="18" width="18"/> (Switches) in the workbench header, then click **Manage switches**, or click {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/03-Menu/navigation-menu.svg" height="18" width="18" alt="Main Menu">}} (Main Menu) and select **Upgrade Switches**.

2. Click **Manage** on the NetQ Configurations card.

3. Click {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/43-Remove-Add/add-circle.svg" height="18" width="18" alt="Add Config Profile">}} (Add Config).

    {{<figure src="/images/netq/lcm-netq-config-profile-create-310.png" width="450">}}

4. Enter a name for the profile.

5. If you do not want NetQ Agent to run in the management VRF, select either *Default* or *Custom*. The Custom option lets you enter the name of a user-defined VRF.

6. Optionally enable WJH.

    Refer to {{<link url="Monitor-Network-Elements/#view-what-just-happened" text="WJH">}} for information about this feature. *WJH is only available on Mellanox switches.*

7. To set a logging level, click **Advanced**, then choose the desired level.

    {{<figure src="/images/netq/lcm-netq-config-profile-log-level-310.png" width="450">}}

8. Optionally set a CPU usage limit for the NetQ Agent. Click **Enable** and drag the dot to the desired limit. Refer to this {{<exlink url="https://support.cumulusnetworks.com/hc/en-us/articles/360046925373-NetQ-Agent-CPU-Utilization-on-Cumulus-Linux-Switches" text="Knowledge Base article">}} for information about this feature.

9. Click **Add** to complete the configuration or **Close** to discard the configuration.

    This example shows the addition of a profile with the CPU limit set to 75 percent.

    {{<figure src="/images/netq/lcm-netq-config-profile-added-310.png" width="550">}}

### Remove Cumulus NetQ Configuration Profiles

To remove a NetQ configuration profile:

1. Click <img src="https://icons.cumulusnetworks.com/03-Computers-Devices-Electronics/09-Hard-Drives/hard-drive-1.svg" height="18" width="18"/> (Switches) in the workbench header, then click **Manage switches**, or click {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/03-Menu/navigation-menu.svg" height="18" width="18" alt="Main Menu">}} (Main Menu) and select **Upgrade Switches**.

2. Click **Manage** on the NetQ Configurations card.

3. Select the profile(s) you want to remove and click {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/23-Delete/bin-1.svg" width="18" height="18">}} (Delete).
