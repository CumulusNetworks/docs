---
title: Manage Switch Configurations
author: Cumulus Networks
weight: 660
toc: 4
---
You can use the NetQ UI to configure switches using one or more switch configurations. To enable consistent application of configurations, switch configurations can contain network templates for SNMP, NTP, and user accounts. You can also specify configuration profiles for Cumulus NetQ Agents.

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

    {{<figure src="/images/netq/lcm-ntwk-template-create-new-320.png" width="700">}}

3. Click {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/43-Remove-Add/add-circle.svg" height="18" width="18">}} Create New.

    {{<figure src="/images/netq/lcm-ntwk-template-forms-snmp-320.png" width="700">}}

4. Decide which aspects of configuration you want included in this template: SNMP, NTP, and/or User accounts.

5. Configure the template using the following instructions.

{{< tabs "TabID37" >}}

{{< tab "SNMP" >}}

SNMP provides a way to query, monitor, and manage your devices in addition to NetQ.

To create a network template with SNMP parameters included:

1. Provide a name for the template. This field is required and can be a maximum of 22 characters, including spaces.

    All other parameters are optional. Configure those as desired, and described here.

2. Enter a comma-separated list of IP addresses of the SNMP Agents on the switches and hosts in your network.

3. Accept the management VRF or change to the default VRF.

4. Enter contact information for the SNMP system administrator, including an email address or phone number, their location, and name.

5. Restrict the hosts that should accept SNMP packets:

    1. Click {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/43-Remove-Add/add-circle.svg" height="18" width="18">}}.

    2. Enter the name of an IPv4 or IPv6 community string.

    3. Indicate which hosts should accept messages:

        Accept *any* to indicate all hosts are to accept messages (default), or enter the hostnames or IP addresses of the specific hosts that should accept messages.

    4. Click {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/43-Remove-Add/add-circle.svg" height="18" width="18">}} to add additional community strings.

6. Specify traps to be included:

    1. Click {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/43-Remove-Add/add-circle.svg" height="18" width="18">}}.

    2. Specify the traps as follows:

        | Parameter | Description |
        | ---- | ---- |
        | Load(1 min) | Name of the xxx |
        | Trap link down frequency | Toggle on to set the frequency at which to collect link down trap information. Default value is 60 seconds. |
        | Trap link up frequency | Toggle on to set the frequency at which to collect link up trap information. Default value is 60 seconds.  |
        | IQuery Secname | xxx |
        | Trap Destination IP | IPv4 or IPv6 address where the trap information is to be sent. This can be a local host or other valid location. |
        | Community Password | Authorization password. Any valid string, where an exclamation mark (!) is the only allowed special character. |
        | Version | SNMP version to use |

7. If you are using SNMP version 3, specify relevant V3 support parameters:

    1. Enter the user name of someone who has full access to the SNMP server.

    2. Enter the user name of someone who has only read access to the SNMP server.

    3. Toggle **Authtrap** to enable authentication for users accessing the SNMP server.

    4. Select an authorization type.

        For either MDS or SHA, enter an authorization key and optionally specify AES or DES encryption.

8. Click **Save and Continue**.

{{< /tab >}}

{{< tab "NTP" >}}

Switches and hosts must be kept in time synchronization with the NetQ appliance or VM to ensure accurate data reporting. NTP is one protocol that can be used to synchronize the clocks of these devices. None of the parameters are required. Specify those which apply to your configuration.

To create a network template with NTP parameters included:

1. Click NTP.

    {{<figure src="/images/netq/lcm-ntwk-template-forms-ntp-320.png" width="700">}}

2. Enter the address of one or more of your NTP servers. Toggle to choose between Burst and IBurst to specify whether the server should send a burst of packets when the server is reachable or unreachable, respectively.

3. Specify either the Default or Management VRF for communication with the NTP server.

4. Enter the interfaces that the NTP server should listen to for synchronization. This can be a IP, broadcast, manycastclient, or reference clock address.

5. Enter the timezone of the NTP server.

6. Specify advanced parameters:

    1. Click {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/43-Remove-Add/add-circle.svg" height="18" width="18">}}.

    2. Specify the location of a Drift file containing the frequency offset between the NTP server clock and the UTC clock. It is used to adjust the system clock frequency on every system or service start. Be sure that the location you enter can be written by the NTP daemon.

    3. Enter an interface for the NTP server to ignore. Click {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/43-Remove-Add/add-circle.svg" height="18" width="18">}} to add more interfaces to be ignored.

    4. Enter one or more interfaces that xxx. Click {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/43-Remove-Add/add-circle.svg" height="18" width="18">}} to add more interfaces to be dropped.

    5. Restrict query/configuration access to the NTP server.

        Enter **restrict \<values\>**. Common values include:

        | Value | Description |
        | ---- | ---- |
        | default | Block all queries except as explicitly indicated |
        | kod (kiss-o-death) | block all, but time and statistics queries |
        | nomodify | block changes to NTP configuration |
        | notrap | block control message protocol traps |
        | nopeer | block the creation of a peer |
        | noquery | block NTP daemon queries, but allow time queries |

        Click {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/43-Remove-Add/add-circle.svg" height="18" width="18">}} to add more access control restrictions.

    6. Restrict administrative control (host) access to the NTP server.

        Enter the IP address for a host or set of hosts, with or without a mask, followed by a restriction value (as described in step 5.) If no mask is provided, 255.255.255.255 is used. If *default* is specified for query/configuration access, entering the IP address and mask for a host or set of hosts in this field *allows* query access for these hosts (explicit indication).

        Click {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/43-Remove-Add/add-circle.svg" height="18" width="18">}} to add more administrative control restrictions.

7. Click **Save and Continue**.

{{< /tab >}}

{{< tab "User" >}}

Creating a User template controls who or what accounts can access the switch and what permissions they have with respect to the data found (read/write/execute). You can also control access using groups of users. No parameters are required. Specify parameters which apply to your specific configuration need.

To create a network template with user parameters included:

1. Click **User**.

    {{<figure src="/images/netq/lcm-ntwk-template-forms-user-320.png" width="700">}}

2. For individual users or accounts:

    1. Enter a username and password for the individual or account.

    2. Provide a description of the user. (any char limits???)

    3. Toggle **Should Expire** to require changes to the password to expire on a given date.

        The current date and time are automatically provided to show the correct entry format. Modify this to the appropriate expiration date.

3. Specify advanced parameters:

    1. Click {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/43-Remove-Add/add-circle.svg" height="18" width="18">}}.

    2. If you do not want a home folder created for this user or account, toggle **Create home folder**.

    3. Generate an SSH key pair for this user or account. **Toggle Generate SSH key**. When generation is selected, the key pair are stored in the */home/\<user\>/.ssh* directory.

    4. If you are looking to remove access for the user or account, toggle **Delete user if present**. If you *do not* want to remove the directories associated with this user or account at the same time, toggle **Delete user directory**.

    5. Identify this account as a system account. Toggle **Is system account**.

    6. To specify a group this user or account belongs to, enter the group name in the **Groups** field. 

        Click {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/43-Remove-Add/add-circle.svg" height="18" width="18">}} to add additional groups.

4. Click **Save and Finish**.

{{< /tab >}}

{{< /tabs >}}

6. Once you have finished the template configuration, you are returned to the templates library.

    {{<figure src="/images/netq/lcm-ntwk-template-library-320.png" width="700">}}

### Modify Network Templates

For each template that you have created, you can edit, clone, or discard it altogether.

#### Edit a Network Template

Click xxx, then select xxx (edit). Edit enables you to modify....

#### Clone a Network Template

Click xxx, then select xxx (clone).

#### Delete a Network Template

Click xxx, then xxx (trash).

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
