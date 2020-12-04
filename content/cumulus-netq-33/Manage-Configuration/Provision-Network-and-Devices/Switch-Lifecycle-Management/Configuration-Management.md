---
title: Manage Switch Configurations
author: NVIDIA
weight: 660
toc: 4
---
You can use the NetQ UI to configure switches using one or more switch configurations. To enable consistent application of configurations, switch configurations can contain network templates for SNMP, NTP, and user accounts, and configuration profiles for interfaces and NetQ Agents.

If you intend to use network templates or configuration profiles, the recommended workflow is as follows:

{{<figure src="/images/netq/lcm-switch-config-workflow-320.png" width="400">}}

## Manage Network Templates

Network templates provide administrators the option to create switch configuration profiles that can be applied to multiple switches. They can help reduce inconsistencies with switch configuration and speed the process of initial configuration and upgrades. No default templates are provided.

### View Network Templates

You can view existing templates using the Network Templates card.

1. Open the lifecycle management (Manage Switch Assets) dashboard.

2. Click **Configuration Management**.

3. Locate the Network Templates card.

    {{<figure src="/images/netq/lcm-ntwk-template-medium-320.png" width="200">}}

4. Click **Manage** to view the list of existing switch templates.

### Create Network Templates

No default templates are provided on installation of NetQ. This enables you to create configurations that match your specifications.

To create a network template:

1. Open the lifecycle management (Manage Switch Assets) dashboard.

2. Click **Configuration Management**.

3. Click **Add** on the Network Templates card.

    {{<figure src="/images/netq/lcm-ntwk-template-create-new-320.png" width="700">}}

4. Click {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/43-Remove-Add/add-circle.svg" height="18" width="18">}} Create New.

    {{<figure src="/images/netq/lcm-ntwk-template-forms-snmp-320.png" width="700">}}

5. Decide which aspects of configuration you want included in this template: SNMP, NTP, and/or User accounts.

    {{<notice tip>}}

You can specify your template in any order, but to complete the configuration, you must open the User form to click <strong>Save and Finish</strong>.

    {{</notice>}}

6. Configure the template using the following instructions.

{{< tabs "TabID51" >}}

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
        | Load(1 min) | Threshold CPU load must cross within a minute to trigger a trap |
        | Trap link down frequency | Toggle on to set the frequency at which to collect link down trap information. Default value is 60 seconds. |
        | Trap link up frequency | Toggle on to set the frequency at which to collect link up trap information. Default value is 60 seconds.  |
        | IQuery Secname | Security name for SNMP query |
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

    1. Click {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/43-Remove-Add/add-circle.svg" height="18" width="18">}} **Advanced**.

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

    2. Provide a description of the user.

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

6. Once you have finished the template configuration, you are returned to the network templates library.

    This shows the new template you created and which forms have been included in the template. You may only have one or two of the forms in a given template.

    {{<figure src="/images/netq/lcm-ntwk-template-library-320.png" width="700">}}

### Modify Network Templates

For each template that you have created, you can edit, clone, or discard it altogether.

#### Edit a Network Template

You can change a switch configuration template at any time. The process is similar to creating the template.

To edit a network template:

1. Enter template edit mode in one of two ways:

    - Hover over the template , then click {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/22-Edit/pencil-1.svg" height="18" width="18">}} (edit).

        {{<figure src="/images/netq/lcm-ntwk-template-edit-320.png" width="200">}}

    - Click {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/03-Menu/navigation-menu-horizontal.svg" height="18" width="18">}}, then select *Edit*.

        {{<figure src="/images/netq/lcm-ntwk-template-edit-menu-320.png" width="200">}}

2. Modify the parameters of the SNMP, NTP, or User forms in the same manner as when you created the template.

3. Click **User**, then **Save and Finish**.

#### Clone a Network Template

You can take advantage of a template that is significantly similar to another template that you want to create by cloning an existing template. This can save significant time and reduce errors.

To clone a network template:

1. Enter template clone mode in one of two ways:

    - Hover over the template , then click {{<img src="https://icons.cumulusnetworks.com/12-Design/07-Layers/layers-front.svg" height="18" width="18">}} (clone).

        {{<figure src="/images/netq/lcm-ntwk-template-clone-320.png" width="200">}}

    - Click {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/03-Menu/navigation-menu-horizontal.svg" height="18" width="18">}}, then select *Clone*.

        {{<figure src="/images/netq/lcm-ntwk-template-edit-menu-320.png" width="200">}}

2. Modify the parameters of the SNMP, NTP, or User forms in the same manner as when you created the template to create the new template.

3. Click **User**, then **Save and Finish**.

    The newly cloned template is now visible on the template library.

#### Delete a Network Template

You can remove a template when it is no longer needed.

To delete a network template, do one of the following:

- Hover over the template , then click {{<img src="https://icons.cumulusnetworks.com/12-Design/07-Layers/layers-front.svg" height="18" width="18">}} (delete).

    {{<figure src="/images/netq/lcm-ntwk-template-delete-320.png" width="200">}}

- Click {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/03-Menu/navigation-menu-horizontal.svg" height="18" width="18">}}, then select *Delete*.

    {{<figure src="/images/netq/lcm-ntwk-template-edit-menu-320.png" width="200">}}

The template is no longer visible in the network templates library.

## Manage NetQ Configuration Profiles

You can set up a configuration profile to indicate how you want NetQ configured when it is installed or upgraded on your Cumulus Linux switches.

The default configuration profile, *NetQ default config*, is set up to run in the management VRF and provide info level logging. Both WJH and CPU Limiting are disabled.

You can view, add, and remove NetQ configuration profiles at any time.

### View NetQ Configuration Profiles

To view existing profiles:

1. Click <img src="https://icons.cumulusnetworks.com/03-Computers-Devices-Electronics/09-Hard-Drives/hard-drive-1.svg" height="18" width="18"/> (Switches) in the workbench header, then click **Manage switches**, or click {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/03-Menu/navigation-menu.svg" height="18" width="18" alt="Main Menu">}} (Main Menu) and select **Manage Switches**.

2. Click **Configuration Management**.

3. Click **Manage** on the NetQ Configurations card.

    Note that the initial value on first installation of NetQ shows one profile. This is the default profile provided with NetQ.

    {{<figure src="/images/netq/lcm-netq-config-card-on-install-310.png" width="200">}}

4. Review the profiles.

    {{<figure src="/images/netq/lcm-netq-config-profiles-list-310.png" width="550">}}

### Create NetQ Configuration Profiles

You can specify four options when creating NetQ configuration profiles:

- Basic: Assign a VRF and enable or disable what just happened (WJH) feature
- Advanced: Set logging level and  enable or disable CPU limit feature

To create a profile:

1. Click <img src="https://icons.cumulusnetworks.com/03-Computers-Devices-Electronics/09-Hard-Drives/hard-drive-1.svg" height="18" width="18"/> (Switches) in the workbench header, then click **Manage switches**, or click {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/03-Menu/navigation-menu.svg" height="18" width="18" alt="Main Menu">}} (Main Menu) and select **Manage Switches**.

2. Click **Configuration Management**.

3. Click **Manage** on the NetQ Configurations card.

4. Click {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/43-Remove-Add/add-circle.svg" height="18" width="18" alt="Add Config Profile">}} (Add Config) above the listing.

    {{<figure src="/images/netq/lcm-netq-config-profile-create-310.png" width="450">}}

5. Enter a name for the profile. This is required.

6. If you do not want NetQ Agent to run in the management VRF, select either *Default* or *Custom*. The Custom option lets you enter the name of a user-defined VRF.

7. Optionally enable WJH.

    Refer to {{<link title="Configure and Monitor What Just Happened Metrics/#view-what-just-happened-metrics" text="WJH">}} for information about this feature. *WJH is only available on Mellanox switches.*

8. To set a logging level, click **Advanced**, then choose the desired level.

    {{<figure src="/images/netq/lcm-netq-config-profile-log-level-310.png" width="450">}}

9. Optionally set a CPU usage limit for the NetQ Agent. Click **Enable** and drag the dot to the desired limit. Refer to this {{<exlink url="https://support.cumulusnetworks.com/hc/en-us/articles/360046925373-NetQ-Agent-CPU-Utilization-on-Cumulus-Linux-Switches" text="Knowledge Base article">}} for information about this feature.

10. Click **Add** to complete the configuration or **Close** to discard the configuration.

    This example shows the addition of a profile with the CPU limit set to 75 percent.

    {{<figure src="/images/netq/lcm-netq-config-profile-added-310.png" width="550">}}

### Remove NetQ Configuration Profiles

To remove a NetQ configuration profile:

1. Click <img src="https://icons.cumulusnetworks.com/03-Computers-Devices-Electronics/09-Hard-Drives/hard-drive-1.svg" height="18" width="18"/> (Switches) in the workbench header, then click **Manage switches**, or click {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/03-Menu/navigation-menu.svg" height="18" width="18" alt="Main Menu">}} (Main Menu) and select **Manage Switches**.

2. Click **Configuration Management**.

3. Click **Manage** on the NetQ Configurations card.

4. Select the profile(s) you want to remove and click {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/23-Delete/bin-1.svg" width="18" height="18">}} (Delete).

## Manage Switch Configuration

To ease the consistent configuration of your switches, NetQ enables you to create and manage multiple switch configuration profiles. Each configuration can contain Cumulus Linux- and NetQ Agent-related settings. These can then be applied to a group of switches at once.

You can view, create, and modify switch configuration profiles and their assignments at any time using the Switch Configurations card.

### View Switch Configuration Profiles

You can view existing switch configuration profiles using the Switch Configurations card.

1. Open the lifecycle management (Manage Switch Assets) dashboard.

2. Click **Configuration Management**.

3. Locate the Switch Configurations card.

    {{<figure src="/images/netq/lcm-switch-config-medium-card-320.png" width="200">}}

4. Click **Manage** to view the list of existing switch templates.

### Create Switch Configuration Profiles

No default configurations are provided on installation of NetQ. This enables you to create configurations that match your specifications.

To create a switch configuration profile:

1. Open the lifecycle management (Manage Switch Assets) dashboard.

2. Click **Configuration Management**.

3. Click **Add** on the Switch Configurations card.

    {{<figure src="/images/netq/lcm-switch-config-add-320.png" width="200">}}

4. Enter a name for the configuration. This is required and must be a maximum of 22 characters, including spaces.

5. Decide which aspects of configuration you want included in this template: Cumulus Linux, NetQ Agent, VLANs, MLAG, and/or interfaces.

6. Specify the settings for each using the following instructions.

{{< tabs "TabID383" >}}

{{< tab "CL Configuration" >}}

Three configuration options are available for the Cumulus Linux configuration portion of the switch configuration profile. Note that two of those are required.

1. Enter the management interface (VLAN ID) to be used for communications with the switches with this profile assigned. Commonly this is either *eth0* or *eth1*.

2. Select the type of switch that will have this configuration assigned from the **Choose Switch type** dropdown. Currently this includes Mellanox SN series of switches.

3. If you want to include network settings in this configuration, click **View/Add**.

    This opens the Network Template forms. You can select an existing network template to pre-populate the parameters already specified in that template, or you can start from scratch to create a different set of network settings.

    {{<figure src="/images/netq/lcm-switch-config-ntwk-template-config-320.png" width="700">}}

<div style="padding-left: 18px;"><em>To use an existing network template as a starting point:</em>

1. Select the template from the dropdown.

2. If you have selected a network template that has any SNMP parameters specified, you must specify the additional required parameters, then click **Continue** or click **NTP**.

3. If the selected network template has any NTP parameters specified, you must specify the additional required parameters, then click **Continue** or click **User**.

4. If the selected network template has any User parameters specified, you must specify the additional required parameters, then click **Done**.

5. If you think this Cumulus Linux configuration is one that you will use regularly, you can make it a template. Enter a name for the configuration and click **Yes**.

    {{<figure src="/images/netq/lcm-switch-config-save-as-template-dialog-320.png" width="200">}}

</div>

<div style="padding-left: 18px;"><em>To create a new set of network settings:</em>

1. Select the SNMP, NTP, or User forms to specify parameters for this configuration. Note that selected parameters are required on each form, noted by red asterisks (*). Refer to {{<link title="Manage Switch Configurations/#create-network-templates" text="Create Network Templates">}} for a description of the fields.

2. When you have completed the network settings, click **Done**.

    If you are not on the User form, you need to go to that tab for the **Done** option to appear.

In either case, if you change your mind about including network settings, click {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/remove-circle.svg" height="18" width="18">}} to exit the form.

</div>

Click one of the following:
<ul>
<li><strong>Reset</strong> to clear your entries and start again</li>
<li><strong>Save and Continue</strong> to configure additional switch configuration parameters</li>
<li><strong>Save and Deploy</strong> if the switch configuration is now complete</li>
</ul>

{{< /tab >}}

{{< tab "NetQ Agent" >}}

1. Click **NetQ Agent Configuration**.

    {{<figure src="/images/netq/lcm-switch-config-nqagent-config-320.png" width="700">}}

2. Select an existing NetQ Configuration profile or create a custom one.

    <em>To use an existing network template as a starting point:</em>

    - Select the configuration profile from the dropdown.

    - Modify any of the parameters as needed.

    <em>To create a new configuration profile:</em>

    - Select values as appropriate for your situation. Refer to {{<link title="Manage Switch Configurations/#create-cumulus-netq-configuration-profiles" text="Create NetQ Configuration Profiles">}} for descriptions of these parameters.

3. Click one of the following:

    - **Reset** to clear your entries and start again
    - **Save and Continue** to configure additional switch configuration parameters
    - **Save and Deploy** if the switch configuration is now complete

{{< /tab >}}

{{< tab "VLAN Management" >}}

1. Click **VLAN management**.

2. Click {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/43-Remove-Add/add-circle.svg" height="18" width="18">}} to add one or more VLANs to the switch configuration.

3. Enter a name for the VLAN when creating a single VLAN or enter a prefix (combined with the VLAN ID) for multiple VLANs.

4. Enter a single VLAN ID (1-4096) or a range of IDs. When entering multiple IDs, separate them by commas and do not use spaces. For example, you can enter them:

    - One at a time: 25,26,27,28,85,86,87,88,89,112
    - As a single range: 25-28 or 85-89
    - As a set of ranges and individual IDs: 25-28,85-89 or 25-28,85-89,112

5. Click **Create**.

    The VLAN/s are displayed in the VLAN list. Once VLANs are in the list, they can be exported, modified, removed, and duplicated using the menu above the list. Simply select one, all, or filter for a subset of VLANs, then click the relevant menu icon.

6. Click one of the following:

    - **Reset** to clear your entries and start again
    - **Save and Continue** to configure additional switch configuration parameters
    - **Save and Deploy** if the switch configuration is now complete

{{< /tab >}}

{{< tab "MLAG" >}}

MLAG is disabled by default. If you want to include MLAG in the switch configuration, you must enable it.

1. Click **Enable**.

2. Select the VLAN over which MLAG traffic is communicated. If you have created a VLAN profile....If you have not yet created a VLAN profile, refer to xxx and then return here.

3. Enter the priority of ???

4. Designate which ports are to be used, including ingress and egress ports.

5. Click one of the following:

    - **Reset** to clear your entries and start again or remove the specifications
    - **Save and Continue** to configure additional switch configuration parameters
    - **Save and Deploy** if the switch configuration is now complete

{{< /tab >}}

{{< tab "Interface Profile" >}}

Every interface requires at least one interface profile.  An interface profile must contain a bond, SVI, sub-interface, and port. You can create (up to x or as many desired???) profiles. (or is this profiles in profiles???)

### Add Bond Profiles

The information needed to define a bond profile is collected into two categories: details and attributes. Begin your definition with the bond details as these items are all required.

1. Click **Interface profile**.

2. Click {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/43-Remove-Add/add-circle.svg" height="18" width="18">}} to add a new bond profile.

3. Enter a unique name for the bond profile.

4. Click on the type of bond this profile is to support; either layer 2 (**L2**) or layer 3 (**L3**).

5. Enter the supported MTU for this bond profile.

6. Select the mode this profile is to support: either **lacp** or **balance-xor**.

    Choosing the LACP (link aggregation control protocol) allows for redundancy by load-balancing traffic across all available links. Choosing balance-xor balances traffic load by spreading outgoing packets between the available Ethernet interfaces.

    If you select LACP, then you must enable LACP and indicate the rate to expect PDUs at the switch; **fast**&ndash;every second, or **slow**&ndash;every 30 seconds. Click on the appropriate choices.

7. Click **Bond attributes**.

8. Select a private VLAN ID (pvid) for communication from the dropdown.

9. Optionally assign one or more tagged VLANs to support traffic from more than one VLAN on a port.

10. Indicated whether this bond profile is to support multi-homing (connections to more than one network) (**True**) or to only a single network (**False**).

11. Review your specification, clicking **Back** to review the details and **Next** to return to the attributes.

12. When you are satisfied with the bond profile specification, click **Create**.

    The bond profiles are displayed in the Bond list. Once bonds are in the list, they can be exported, modified, removed, and duplicated using the menu above the list. Simply select one, all, or filter for a subset of bonds, then click the relevant menu icon.

13. Click one of the following:

    - **Reset** to clear your entries and start again
    - **Save and Continue** to configure additional interface profile components
    - **Save and Deploy** if your interface profile and the switch configuration is now completed

### Add SVI Profiles

(why include???)

1. Click **SVI**.

2. Click {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/43-Remove-Add/add-circle.svg" height="18" width="18">}} to add a new SVI profile.

3. Enter a unique name for the SVI profile.

4. Enter the supported MTU for this SVI profile.

5. Select a VRF profile from the dropdown. (where is this created???)

6. Enable VRR if desired.

7. Click **Create**.

    (how are the ipv4 and ipv6 addresses populated???)

    The SVI profiles are displayed in the SVI list. Once SVIs are in the list, they can be exported, modified, removed, and duplicated using the menu above the list. Simply select one, all, or filter for a subset of SVIs, then click the relevant menu icon.

8. Click one of the following:

    - **Reset** to clear your entries and start again
    - **Save and Continue** to configure additional interface profile components
    - **Save and Deploy** if your interface profile and the switch configuration is now completed

### Add Sub-interfaces Profiles

(why include???)

1. Click **Subinterface**.

2. Click {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/43-Remove-Add/add-circle.svg" height="18" width="18">}} to add a new sub-interface profile.

3. Enter a unique name for the subinterface profile.

4. Enter the supported MTU for this subinterface profile.

5. Select a VRF profile from the dropdown. (where is this created???)

6. Click **Create**.

    The subinterface profiles are displayed in the subinterface list. Once subinterfaces are in the list, they can be exported, modified, removed, and duplicated using the menu above the list. Simply select one, all, or filter for a subset of subinterfaces, then click the relevant menu icon.

7. Click one of the following:

    - **Reset** to clear your entries and start again
    - **Save and Continue** to configure additional interface profile components
    - **Save and Deploy** if your interface profile and the switch configuration is now completed

### Add Port Profiles

The information needed to define a port is collected into two categories: details and attributes.

1. Click **Port**.

2. Click {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/43-Remove-Add/add-circle.svg" height="18" width="18">}} to add a new port profile.

3. Enter a unique name for the port profile.

4. Click on the type of port this profile is to support; either layer 2 (**L2**) or layer 3 (**L3**).

5. Optionally enable forward error correction (FEC); click **True**. (what is default value here???)

6. Optionally enable auto-negotiation of link speeds; click **True**.

7. Optionally specify the whether to support transmit and receive on this port (**full**) or either transmit or receive on this port (**half**).

8. Optionally select port speed from the dropdown.

9. Optionally enter the supported MTU for this bond profile.

10. Click **Bond attributes**.

11. Select a private VLAN ID (pvid) for communication from the dropdown.

12. Optionally assign one or more tagged VLANs to support traffic from more than one VLAN on a port.

13. When you are satisfied with the bond profile specification, click **Create**.

    The port profiles are displayed in the Port list. Once ports are in the list, they can be exported, modified, removed, and duplicated using the menu above the list. Simply select one, all, or filter for a subset of ports, then click the relevant menu icon.

14. Click one of the following:

    - **Reset** to clear your entries and start again
    - **Save and Continue** to configure additional interface profile components
    - **Save and Deploy** if your interface profile and the switch configuration is now completed

{{< /tab >}}

{{< tab "Interfaces" >}}

intro

### Add Bonds

intro/which parameters required?

1. Click **Interfaces**.

2. Click **Bond management**.

3. Click {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/43-Remove-Add/add-circle.svg" height="18" width="18">}} to add a new bond.

4. Enter a unique name for the bond.

5. Optionally enter an alias for the bond. Format???

6. Select an interface profile from the dropdown. If you have not yet created one, refer to (Interface profile tab > Bond submenu. how to link to tab???)

7. Assign the ports included in this bond. Format???

8. When you are satisfied with the bond specification, click **Create**.

    The bonds are displayed in the Bond list. Once bonds are in the list, they can be exported, modified, removed, and duplicated using the menu above the list. Simply select one, all, or filter for a subset of bonds, then click the relevant menu icon.

    (when select bond a, get an error, was there a step i missed to set these per instance variables???)

9. Click one of the following:

    - **Reset** to clear your entries and start again
    - **Save and Continue** to configure additional interface profile components
    - **Save and Deploy** if your interface profile and the switch configuration is now completed

### Add SVIs

(why include???)

1. Click **SVI Management**.

2. Click {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/43-Remove-Add/add-circle.svg" height="18" width="18">}} to add a new SVI.

3. Enter a unique name for the SVI.

4. Select a VLAN profile to apply to this SVI.

5. Enter the supported MTU for this SVI.

6. Select an interface profile to apply to this SVI.

7. Click **Create**.

    The SVIs are displayed in the SVI list. Once SVIs are in the list, they can be exported, modified, removed, and duplicated using the menu above the list. Simply select one, all, or filter for a subset of SVIs, then click the relevant menu icon.

8. Click one of the following:

    - **Reset** to clear your entries and start again
    - **Save and Continue** to configure additional interface parameters
    - **Save and Deploy** if your interfaces and the switch configuration is now completed

### Add Sub-interfaces

(why include???)

1. Click **Subinterface management**.

2. Click {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/43-Remove-Add/add-circle.svg" height="18" width="18">}} to add a new sub-interface.

3. Enter a unique name for the subinterface.

4. Select a VLAN profile to apply to this subinterface.

5. Enter the supported MTU for this subinterface.

6. Select a parent interface from the dropdown.

7. Select an interface profile to apply to this subinterface.

8. Click **Create**.

    The subinterface are displayed in the subinterface list. Once subinterfaces are in the list, they can be exported, modified, removed, and duplicated using the menu above the list. Simply select one, all, or filter for a subset of subinterfaces, then click the relevant menu icon.

9. Click one of the following:

    - **Reset** to clear your entries and start again
    - **Save and Continue** to configure additional interface parameters
    - **Save and Deploy** if your interfaces and the switch configuration is now completed

### Add Ports

This tab describes all of the ports on the identified switch. The port name and bond are provided by default (based on the switch type??? and xxx???). For each port, you must define the speed and assign an interface profile. Optionally you can configure ports to be split to support xxx???. Any caveats related to port configuration on the specified type of switch are listed under the port listing.

1. Click **Port management**.

2. Accept or change the port names.

3. Verify the port speeds. For any port that should be other than 100 G, select either 50 G or 40 G.

4. If you want to break out selected ports, choose the split value from the dropdown.

5. Select a bond to apply to each port.

6. Select an interface profile for each port.

<div class="notices tip"><p>For values that apply to all ports, select all ports and then select or enter the value.</p></div>

7. When you are satisfied with the interfaces specification, click one of the following:

    - **Reset** to clear your entries and start again
    - **Save and Continue** to configure additional switch configuration parameters
    - **Save and Deploy** if your port configuration and the switch configuration is now completed

{{< /tab >}}

{{< tab "Switches" >}}

The final step is to assign the switch configuration that you have just created to one or more switches.

To assign the configuration:

1. Click **Switches**.

    A few items to note on this tab:
    - Above the switches (left), the number of switches that can be assigned and the number of switches that have already been assigned
    - Above the switches (right), management tools to help find the switches you want to assign with this configuration, including select all, clear, filter, and search.

    {{<figure src="/images/netq/lcm-switch-config-switch-assign-320.png" width="700">}}

2. Select the switches to be assigned this configuration.

    In this example, we searched for all leaf switches, then clicked select all.

    {{<figure src="/images/netq/lcm-switch-config-switch-selection-320.png" width="700">}}

3. Click **Save and Finish**.

4. To run the job to apply the configuration, you first have the option to change the hostnames of the selected switches.

    Either change the hostnames and then click **Continue** or just click **Continue** without changing the hostnames.

5. Enter a name for the job (maximum of 22 characters including spaces), then click **Continue**.

    This opens the monitoring page for the assignment jobs, similar to the upgrade jobs. The job title bar indicates the name of the switch configuration being applied and the number of switches that to be assigned with the configuration. (After you have mulitple switch configurations created, you might have more than one configuration being applied in a single job.) Each switch element indicates its hostname, IP address, installed Cumulus Linux and NetQ versions, a note indicating this is a new assignment, the switch configuration being applied, and a menu that provides the detailed steps being executed. The last is useful when the assignment fails as any errors are included in this popup.

    {{<figure src="/images/netq/lcm-switch-config-assign-job-success-320.png" width="700">}}

    {{<figure src="/images/netq/lcm-switch-config-assign-job-status-popup-320.png" width="300">}}

6. Click {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/close.svg" height="14" width="14">}} to return to the switch configuration page where you can either create another configuration and apply it. If you are finished assigning switch configurations to switches, click {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/43-Remove-Add/remove-circle.svg" height="18" width="18">}} to return to the lifecycle management dashboard.

7. When you return the dashboard, your Switch Configurations card shows the new configurations and the Config Assignment History card appears that shows a summary status of all configuration assignment jobs attempted.

    {{<figure src="/images/netq/lcm-switch-config-post-assign-config-hist-320.png" width="420">}}

8. Click **View** on the Config Assignment History card to open the details of all assignment jobs. Refer to {{<link title="Manage Switch Configurations/#view-switch-configuration-history">}} for more detail about this card.

{{< /tab >}}

{{< /tabs >}}

### Edit a Switch Configuration

You can edit a switch configuration at any time. After you have made changes to the configuration, you can apply it to the same set of switches or modify the switches using the configuration as part of the editing process.

To edit a switch configuration:

1. Locate the Switch Configurations card on the lifecycle management dashboard.

2. Click **Manage**.

3. Locate the configuration you want to edit. Scroll down or filter the listing to help find the configuration when there are multiple configurations.

4. Click {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/03-Menu/navigation-menu-horizontal.svg" height="18" width="18">}}, then select *Edit*.

5. Follow the instructions in {{<link title="Manage Switch Configurations/#create-switch-configuration-profiles" text="Create Switch Configuration Profiles">}}, starting at Step 5, to make any required edits.

### Clone a Switch Configuration

You can clone a switch configuration assignment job at any time.

To clone an assignment job:

1. Locate the Switch Configurations card on the lifecycle management dashboard.

2. Click **Manage**.

3. Locate the configuration you want to clone. Scroll down or filter the listing to help find the configuration when there are multiple configurations.

4. Click {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/03-Menu/navigation-menu-horizontal.svg" height="18" width="18">}}, then select *Clone*.

5. Click {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/03-Menu/navigation-menu-horizontal.svg" height="18" width="18">}}, then select *Edit*.

6. Change the Configuration Name.

7. Follow the instructions in {{<link title="Manage Switch Configurations/#create-switch-configuration-profiles" text="Create Switch Configuration Profiles">}}, starting at Step 5, to make any required edits.

### Remove a Switch Configuration

You can remove a switch configuration at any time; however if there are switches with the given configuration assigned, you must first assign an alternate configuration to those switches.

To remove a switch configuration:

1. Locate the Switch Configurations card on the lifecycle management dashboard.

2. Click **Manage**.

3. Locate the configuration you want to remove. Scroll down or filter the listing to help find the configuration when there are multiple configurations.

4. Click {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/03-Menu/navigation-menu-horizontal.svg" height="18" width="18">}}, then select *Delete*.

    - If any switches are assigned to this configuration, an error message appears. Assign a different switch configuration to the relevant switches and repeat the removal steps.

        {{<figure src="/images/netq/lcm-switch-config-del-config-error-320.png" width="300">}}

    - Otherwise, confirm the removal by clicking **Yes**.

        {{<figure src="/images/netq/lcm-switch-config-del-config-confirmation-320.png" width="300">}}

### Assign Existing Switch Configuration Profiles

You can assign existing switch configurations to one or more switches at any time. You can also change the switch configuration already assigned to a switch.

If you need to create a new switch configuration, follow the instructions in {{<link title="Manage Switch Configurations/#create-switch-configuration-profiles" text="Create Switch Configuration Profiles">}}.

#### Add an Assignment

As new switches are added to your network, you might want to use a switch configuration to speed the process and make sure it matches the configuration of similarly designated switches.

To assign an existing switch configuration to switches:

1. Locate the Switch Configurations card on the lifecycle management dashboard.

2. Click **Manage**.

    {{<figure src="/images/netq/lcm-switch-config-manage-320.png" width="700">}}

3. Locate the configuration you want to assign.

    Scroll down or filter the listing by:
    - **Time Range**: Enter a range of time in which the switch configuration was created, then click **Done**.
    - **All switches**: Search for or select individual switches from the list, then click **Done**.
    - **All switch types**: Search for or select individual switch series, then click **Done**.
    - **All users**: Search for or select individual users who created a switch configuration, then click **Done**.
    - **All filters**: Display all filters at once to apply multiple filters at once. Additional filter options are included here. Click **Done** when satisfied with your filter criteria.

    By default, filters show *all* of that items of the given filter type until it is restricted by these settings.

4. Click **Select switches** in the switch configuration summary.

    {{<figure src="/images/netq/lcm-switch-config-manage-select-switches-320.png" width="700">}}

5. Select the switches that you want to assign to the switch configuration.

    Scroll down or use the **select all**, **clear**, filter , and **Search** options to help find the switches of interest. You can filter by role, Cumulus Linux version, or NetQ version. The badge on the filter icon indicates the number of filters applied. Colors on filter options are only used to distinguish between options. No other indication is intended.

    In this example, we have one role defined, and we have selected that role.

    {{<figure src="/images/netq/lcm-switch-config-manage-select-switches-filter-320.png" width="300">}}

    The result is two switches. Note that only the switches that meet the criteria and have no switch configuration assigned are shown. In this example, there are two additional switches with the spine role, but they already have a switch configuration assigned to them. Click on the link above the list to view those switches.

    Continue narrowing the list of switches until all or most of the switches are visible.

6. Hover over the switches and click {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/43-Remove-Add/add-circle.svg" height="18" width="18">}} or click **select all**.

    {{<figure src="/images/netq/lcm-switch-config-manage-selected-switches-320.png" width="700">}}

7. Click **Done**.

8. To run the job to apply the configuration, you first have the option to change the hostnames of the selected switches.

    Either change the hostnames and then click **Continue** or just click **Continue** without changing the hostnames.

9. If you have additional switches that you want to assign a different switch configuration, follow Steps 3-7 for each switch configuration.

    If you do this, multiple assignment configurations are listed in the bottom area of the page. They all become part of a single assignment job.

10. When you have all the assignments configured, click **Start Assignment** to start the job.

    {{<figure src="/images/netq/lcm-switch-config-manage-start-assign-320.png" width="700">}}

11. Enter a name for the job (maximum of 22 characters including spaces), then click **Continue**.

    {{<figure src="/images/netq/lcm-switch-config-manage-job-name-320.png" width="275">}}

12. Watch the progress or click {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/close.svg" height="14" width="14">}} to return to the switch configuration page where you can either create another configuration and apply it. If you are finished assigning switch configurations to switches, click {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/43-Remove-Add/remove-circle.svg" height="18" width="18">}} to return to the lifecycle management dashboard.

    The Config Assignment History card is updated to include the status of the job you just ran.

#### Change the Configuration Assignment on a Switch

You can change the switch configuration assignment at any time. For example you might have a switch that is starting to experience reduced performance, so you want to run What Just Happened on it to see if there is a particular problem area. You can reassign this switch to a new configuration with WJH enabled on the NetQ Agent while you test it. Then you can change it back to its original assignment.

To change the configuration assignment on a switch:

1. Locate the Switch Configurations card on the lifecycle management dashboard.

2. Click **Manage**.

    {{<figure src="/images/netq/lcm-switch-config-manage-320.png" width="700">}}

3. Locate the configuration you want to assign. Scroll down or filter the listing to help find the configuration when there are multiple configurations.

4. Click **Select switches** in the switch configuration summary.

    {{<figure src="/images/netq/lcm-switch-config-manage-select-switches-320.png" width="700">}}

5. Select the switches that you want to assign to the switch configuration.

    Scroll down or use the **select all**, **clear**, filter , and **Search** options to help find the switch(es) of interest.

6. Hover over the switches and click {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/43-Remove-Add/add-circle.svg" height="18" width="18">}} or click **select all**.

7. Click **Done**.

8. Click **Start Assignment**.

9. Watch the progress.

    On completion, each switch shows the previous assignment and the newly applied configuration assignment.

    {{<figure src="/images/netq/lcm-switch-config-manage-assign-changed-320.png" width="700">}}

10. Click {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/close.svg" height="14" width="14">}} to return to the switch configuration page where you can either create another configuration and apply it. If you are finished assigning switch configurations to switches, click {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/43-Remove-Add/remove-circle.svg" height="18" width="18">}} to return to the lifecycle management dashboard.

    The Config Assignment History card is updated to include the status of the job you just ran.

<!-- #### Remove Assignment

You can remove a switch configuration assignment on a switch at any time. 

To remove an assignment:

1. Locate the Switch Configurations card on the lifecycle management dashboard.

2. Click **Manage**.

3. Locate the configuration you want to assign. Scroll down or filter the listing to help find the configuration when there are multiple configurations.

4. Click **Select switches** in the switch configuration summary.

5.  -->

### View Switch Configuration History

You can view a history of switch configuration assignments using the Config Assignment History card.

To view a summary, locate the Config Assignment History card on the lifecycle management dashboard.

{{<figure src="/images/netq/lcm-config-assign-history-card-320.png" width="200">}}

To view details of the assignment jobs, click **View**.

{{<figure src="/images/netq/lcm-config-assign-history-job-listing-320.png" width="700">}}

Above the jobs, a number of filters are provided to help you find a particular job. To the right of those is a status summary of all jobs. Click <img src="https://icons.cumulusnetworks.com/52-Arrows-Diagrams/01-Arrows/arrow-right-1.svg" height="14" width="14"/> in the job listing to see the details of that job. Click {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/close.svg" height="14" width="14">}} to return to the lifecycle management dashboard.
