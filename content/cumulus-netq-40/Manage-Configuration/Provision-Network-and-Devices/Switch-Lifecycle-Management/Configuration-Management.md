---
title: Manage Switch Configurations
author: NVIDIA
weight: 660
toc: 4
---
You can use the NetQ UI to configure switches using one or more switch configurations. To enable consistent application of configurations, switch configurations can contain network templates for SNMP, NTP, and user accounts, VLAN and MLAG settings, and configuration profiles for interfaces and NetQ Agents.

If you intend to use network templates or configuration profiles, the recommended workflow is as follows:

{{<figure src="/images/netq/lcm-switch-config-workflow-320.png" width="400">}}

If you do not want to use the templates or profiles, simply skip to switch configuration.

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

    {{<figure src="/images/netq/lcm-ntwk-template-forms-general-tab-330.png" width="700">}}

4. Decide which aspects of configuration you want included in this template: SNMP, NTP, LLDP, and/or User accounts.
    {{<notice tip>}}

You can specify your template in any order, but to complete the configuration, you must open the <strong>User</strong> form to click <strong>Save and Finish</strong>.

    {{</notice>}}

5. Configure the template using the following instructions.

    {{<tabs "TabID51" >}}

{{<tab "General" >}}

1. Provide a name for the template. This field is required and can be a maximum of 22 characters, including spaces.

2. Accept the VRF selection of *Management*, or optionally change it to *Default*. Note that changing the VRF may cause some agents to become unresponsive.

3. Click **Save and Continue to SNMP** or select another tab.

{{</tab>}}

{{<tab "SNMP" >}}

SNMP provides a way to query, monitor, and manage your devices in addition to NetQ.

{{<figure src="/images/netq/lcm-ntwk-template-forms-snmp-tab-330.png" width="700">}}

To create a network template with SNMP parameters included:

1. Enter the IP addresses of the SNMP Agents on the switches and hosts in your network.

    You can enter individual IP addresses, a range of IP addresses, or select from the address categories provided (click {{<img src="/images/netq/Down.svg" width="14">}}).

    After adding one of these, you can create another set of addresses by clicking {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/43-Remove-Add/add-circle.svg" height="18" width="18">}}. Continue until you have entered all desired SNMP agent addresses.

2. Accept the management VRF or change to the default VRF.

3. Enter the SNMP username(s) of persons who have access to the SNMP server.

4. Enter contact information for the SNMP system administrator, including an email address or phone number, their location, and name.

5. Restrict the hosts that should accept SNMP packets:

    Click {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/43-Remove-Add/add-circle.svg" height="18" width="18">}} next to **Add Read only Community**.

    {{<figure src="/images/netq/lcm-ntwk-template-forms-snmp-rocomm-330.png" width="700">}}

<div style="padding-left: 18px;"><ul><li>Enter the name of an IPv4 or IPv6 community string.</li>

<li>Indicate which hosts should accept messages:<br>
Accept <em>any</em> to indicate all hosts are to accept messages (default), or enter the hostnames or IP addresses of the specific hosts that should accept messages.</li>

<li>Click {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/43-Remove-Add/add-circle.svg" height="18" width="18">}} to add additional community strings.</li></div>

6. Specify traps to be included:

    Click {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/43-Remove-Add/add-circle.svg" height="18" width="18">}} next to **Add traps**.

    {{<figure src="/images/netq/lcm-ntwk-template-forms-snmp-traps-330.png" width="700">}}

<div style="padding-left: 18px;"><ul><li>Specify the traps as follows:<br>
<table>
<thead>
<tr>
<th>Parameter</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>Load (1 min)</td>
<td>Threshold CPU load must cross within a minute to trigger a trap</td>
</tr>
<tr>
<td>Trap link down frequency</td>
<td>Toggle on to set the frequency at which to collect link down trap information. Default value is 60 seconds.</td>
</tr>
<tr>
<td>Trap link up frequency</td>
<td>Toggle on to set the frequency at which to collect link up trap information. Default value is 60 seconds.</td>
</tr>
<tr>
<td>IQuery Secname</td>
<td>Security name for SNMP query</td>
</tr>
<tr>
<td>Trap Destination IP</td>
<td>IPv4 or IPv6 address where the trap information is to be sent. This can be a local host or other valid location.</td>
</tr>
<tr>
<td>Community Password</td>
<td>Authorization password. Any valid string, where an exclamation mark (!) is the only allowed special character.</td>
</tr>
<tr>
<td>Version</td>
<td>SNMP version to use</td>
</tr>
</tbody>
</table>
</li></div>

7. If you are using SNMP version 3, specify relevant V3 support parameters:

    Click {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/43-Remove-Add/add-circle.svg" height="18" width="18">}} next to **Add V3 support**.

    {{<figure src="/images/netq/lcm-ntwk-template-forms-snmp-v3supp-330.png" width="700">}}

<div style="padding-left: 18px;"><ul>
<li>Toggle <strong>Authtrap enable</strong> to configure authentication for users accessing the SNMP server.</li>
<li>Select an authorization type.<br>
For either MDS or SHA, enter an authorization key and optionally specify AES or DES encryption.</li>
</ul></div>

8. Click **Save and Continue to NTP** or select another tab.

{{</tab>}}

{{<tab "NTP" >}}

Switches and hosts must be kept in time synchronization with the NetQ appliance or VM to ensure accurate data reporting. NTP is one protocol that can be used to synchronize the clocks of these devices. None of the parameters are required. Specify those which apply to your configuration.

To create a network template with NTP parameters included:

1. Click NTP.

    {{<figure src="/images/netq/lcm-ntwk-template-forms-ntp-330.png" width="700">}}

2. Enter the address of one or more of your NTP servers. Toggle to choose between Burst and IBurst to specify whether the server should send a burst of packets when the server is reachable or unreachable, respectively.

3. Specify either the Default or Management VRF for communication with the NTP server.

4. Enter the interfaces that the NTP server should listen to for synchronization. This can be a IP, broadcast, manycastclient, or reference clock address.

5. Select the timezone of the NTP server.

6. Specify advanced parameters:

    Click {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/43-Remove-Add/add-circle.svg" height="18" width="18">}} next to **Advanced**.

    {{<figure src="/images/netq/lcm-ntwk-template-forms-ntpadv-330.png" width="700">}}

<div style="padding-left: 18px;"><ul>
<li>Specify the location of a Drift file containing the frequency offset between the NTP server clock and the UTC clock. It is used to adjust the system clock frequency on every system or service start. Be sure that the location you enter can be written by the NTP daemon.</li>

<li>Enter an interface for the NTP server to ignore. Click {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/43-Remove-Add/add-circle.svg" height="18" width="18">}} to add more interfaces to be ignored.</li>

<li>Enter one or more interfaces from which the NTP server should drop all messages. Click {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/43-Remove-Add/add-circle.svg" height="18" width="18">}} to add more interfaces to be dropped.</li>

<li>Restrict query and configuration access to the NTP server.<br>
For each restriction, enter <strong>restrict</strong> followed by the value. Common values include:<br>
<table>
<thead>
<tr>
<th>Value</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>default</td>
<td>Block all queries except as explicitly indicated</td>
</tr>
<tr>
<td>kod (kiss-o-death)</td>
<td>block all, but time and statistics queries</td>
</tr>
<tr>
<td>nomodify</td>
<td>block changes to NTP configuration</td>
</tr>
<tr>
<td>notrap</td>
<td>block control message protocol traps</td>
</tr>
<tr>
<td>nopeer</td>
<td>block the creation of a peer</td>
</tr>
<tr>
<td>noquery</td>
<td>block NTP daemon queries, but allow time queries</td>
</tr>
</tbody>
</table>
Click {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/43-Remove-Add/add-circle.svg" height="18" width="18">}} to add more access control restrictions.</li>

<li>Restrict administrative control (host) access to the NTP server.<br>
Enter the IP address for a host or set of hosts, with or without a mask, followed by a restriction value (as described in step 5.) If no mask is provided, 255.255.255.255 is used. If *default* is specified for query/configuration access, entering the IP address and mask for a host or set of hosts in this field <em>allows</em> query access for these hosts (explicit indication).<br>
Click {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/43-Remove-Add/add-circle.svg" height="18" width="18">}} to add more administrative control restrictions.</li>
</ul></div>

7. Click **Save and Continue to LLDP** or select another tab.

{{</tab>}}

{{<tab "LLDP" >}}

LLDP advertises device identities, capabilities, and neighbors. The network template enables you to specify how often you want the advertisement to take place and how long those messages should remain alive on the network.

To create a network template with LLDP parameters included:

1. Click LLDP.

    {{<figure src="/images/netq/lcm-ntwk-template-forms-lldp-330.png" width="700">}}

2. Enter the interval, in seconds, that you want LLDP to transmit neighbor information and statistics.

3. Enter how many times the transmit interval you want for LLDP messages to live on the network.

4. Optionally, specify advanced features by clicking {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/43-Remove-Add/add-circle.svg" height="18" width="18">}} next to **Advanced**.

    {{<figure src="/images/netq/lcm-ntwk-template-forms-lldpadv-330.png" width="700">}}

<div style="padding-left: 18px;"><ul>
<li>Enable advertisement of IEEE 802.1Q TLV (type-length-value) structures, including port description, system name, description and capabilities, management address, and custom names. Mandatory TLVs include end of LLDPPDU, chassis ID, port ID, and time-to-live.</li>
<li>Enable advertisement of system capability codes for the nodes. For example:<br>
<table>
<thead>
<tr>
<th>Code</th>
<th>Capability</th>
</tr>
</thead>
<tbody>
<tr>
<td>B</td>
<td>Bridge (Switch)</td>
</tr>
<tr>
<td>C</td>
<td>DOCSIS Cable Device</td>
</tr>
<tr>
<td>O</td>
<td>Other</td>
</tr>
<tr>
<td>P</td>
<td>Repeater</td>
</tr>
<tr>
<td>R</td>
<td>Router</td>
</tr>
<tr>
<td>S</td>
<td>Station</td>
</tr>
<tr>
<td>T</td>
<td>Telephone</td>
</tr>
<tr>
<td>W</td>
<td>WLAN Access Point</td>
</tr>
</tbody>
</table>
</li>

<li>Enable advertisement of the IP address used for management of the nodes.
</ul></div>

5. Click **Save and Continue to User** or select another tab.

{{</tab>}}

{{<tab "User" >}}

Creating a User template controls who or what accounts can access the switch and what permissions they have with respect to the data found (read/write/execute). You can also control access using groups of users. No parameters are required. Specify parameters which apply to your specific configuration need.

To create a network template with user parameters included:

1. Click **User**.

    {{<figure src="/images/netq/lcm-ntwk-template-forms-user-330.png" width="700">}}

2. Enter the username and password for one or more users.

3. Provide a description of the users.

4. Toggle **Should Expire** to set the password to expire on a given date.

    The current date and time are automatically provided. Click in the field to modify this to the appropriate expiration date.

5. Specify advanced parameters:

    Click {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/43-Remove-Add/add-circle.svg" height="18" width="18">}} next to **Advanced**.

    {{<figure src="/images/netq/lcm-ntwk-template-forms-useradv-330.png" width="700">}}

<div style="padding-left: 18px;"><ul>
<li>If you <em>do not</em> want a home folder created for this user or account, toggle <strong>Create home folder</strong>.</li>
<li>Generate an SSH key pair for this user(s). Toggle <strong>Generate SSH key</strong>. When generation is selected, the key pair is stored in the <em>/home/&lt;user&gt;/.ssh</em> directory.</li>
<li>If you are looking to remove access for the user or account, toggle <strong>Delete user</strong>. If you <em>do not</em> want to remove the directories associated with this user or account at the same time, leave toggle as is (default, do not delete).</li>
<li>Identify this account as a system account. Toggle <strong>Is system account</strong>. System users have no expiration date assigned. Their IDs are selected from the SYS_UID_MIN-SYS_UID_MAX range.
<li>To specify additional access groups these users belongs to, enter the group names in the <strong>Groups</strong> field.<br>
Click {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/43-Remove-Add/add-circle.svg" height="18" width="18">}} to add additional groups.</li>
</ul></div>

6. Click **Save and Finish**.

{{</tab>}}

{{</tabs>}}

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

2. Modify the parameters of the various forms in the same manner as when you created the template.

3. Click **User**, then **Save and Finish**.

#### Clone a Network Template

You can take advantage of a template that is significantly similar to another template that you want to create by cloning an existing template. This can save significant time and reduce errors.

To clone a network template:

1. Enter template clone mode in one of two ways:

    - Hover over the template , then click {{<img src="https://icons.cumulusnetworks.com/12-Design/07-Layers/layers-front.svg" height="18" width="18">}} (clone).

        {{<figure src="/images/netq/lcm-ntwk-template-clone-320.png" width="200">}}

    - Click {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/03-Menu/navigation-menu-horizontal.svg" height="18" width="18">}}, then select *Clone*.

        {{<figure src="/images/netq/lcm-ntwk-template-edit-menu-320.png" width="200">}}

2. Enter a new name for this cloned template and click **Yes**. Or to discard the clone, click **No**.

    {{<figure src="/images/netq/lcm-ntwk-template-clone-modal-330.png" width="300">}}

3. Modify the parameters of the various forms in the same manner as when you created the template to create the new template.

4. Click **User**, then **Save and Finish**.

    The newly cloned template is now visible on the template library.

    {{<figure src="/images/netq/lcm-ntwk-template-library-withclone-330.png" width="500">}}

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

{{<tabs "View existing profiles" >}}

{{<tab "NetQ UI" >}}

1. Click <img src="https://icons.cumulusnetworks.com/03-Computers-Devices-Electronics/09-Hard-Drives/hard-drive-1.svg" height="18" width="18"/> (Switches) in the workbench header, then click **Manage switches**, or click {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/03-Menu/navigation-menu.svg" height="18" width="18" alt="Main Menu">}} (Main Menu) and select **Manage Switches**.

2. Click **Configuration Management**.

3. Click **Manage** on the NetQ Configurations card.

    Note that the initial value on first installation of NetQ shows one profile. This is the default profile provided with NetQ.

    {{<figure src="/images/netq/lcm-netq-config-card-on-install-310.png" width="200">}}

4. Review the profiles.

    {{<figure src="/images/netq/lcm-netq-config-profiles-list-310.png" width="550">}}

{{</tab>}}

{{<tab "NetQ CLI" >}}

Run the `netq lcm show netq-config` command:

```
cumulus@switch:~$ netq lcm show netq-config
ID                        Name            Default Profile                VRF             WJH       CPU Limit Log Level Last Changed
------------------------- --------------- ------------------------------ --------------- --------- --------- --------- -------------------------
config_profile_3289efda36 NetQ default co Yes                            mgmt            Disable   Disable   info      Tue Jan  5 05:25:31 2021
db4065d56f91ebbd34a523b45 nfig
944fbfd10c5d75f9134d42023
eb2b
config_profile_233c151302 CPU limit 75%   No                             mgmt            Disable   75%       info      Mon Jan 11 19:11:35 2021
eb8ee77d6c27fe2eaca51a9bf
2dfcbfd77d11ff0af92b807de
a0dd
```

{{</tab>}}

{{</tabs>}}

### Create NetQ Configuration Profiles

You can specify four options when creating NetQ configuration profiles:

- Basic: Assign a VRF, and enable or disable what just happened (WJH) feature
- Advanced: Set logging level, and enable or disable CPU limit feature

To create a profile:

1. Click <img src="https://icons.cumulusnetworks.com/03-Computers-Devices-Electronics/09-Hard-Drives/hard-drive-1.svg" height="18" width="18"/> (Switches) in the workbench header, then click **Manage switches**, or click {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/03-Menu/navigation-menu.svg" height="18" width="18" alt="Main Menu">}} (Main Menu) and select **Manage Switches**.

2. Click **Configuration Management**.

3. Click **Manage** on the NetQ Configurations card.

4. Click {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/43-Remove-Add/add-circle.svg" height="18" width="18" alt="Add Config Profile">}} (Add Config) above the listing.

    {{<figure src="/images/netq/lcm-netq-config-profile-create-330.png" width="400">}}

5. Enter a name for the profile. This is required.

6. If you do not want NetQ Agent to run in the management VRF, select either *Default* or *Custom*. The Custom option lets you enter the name of a user-defined VRF.

7. Optionally enable WJH.

    Refer to {{<link title="Configure and Monitor What Just Happened" text="What Just Happened">}} for information about configuring this feature, and to {{<link title="WJH Event Messages Reference" text="WJH Event Messages Reference">}} for a description of the drop reasons. *WJH is only available on Mellanox switches.*

    If you choose to enable WJH for this profile, you can use the default configuration which collects all statistics, or you can select **Customize** to select which categories and drop reasons you want collected. *This is an Early Access capability.* Click on each category and drop reason you do not want collected, then click **Done**. You can discard your changes (return to all categories and drop reasons) by clicking **Cancel**.

    {{<figure src="/images/netq/lcm-netq-config-profile-create-wjh-custom-330.png" width="400">}}

8. To set a logging level, click **Advanced**, then choose the desired level.

    {{<figure src="/images/netq/lcm-netq-config-profile-log-level-330.png" width="400">}}

9. Optionally set a CPU usage limit for the NetQ Agent. Click **Enable** and drag the dot to the desired limit.

    Refer to this [Knowledge Base article]({{<ref "knowledge-base/Configuration-and-Usage/Cumulus-NetQ/NetQ-Agent-CPU-Utilization-on-Cumulus-Linux-Switches">}}) for information about this feature.

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

To ease the consistent configuration of your switches, NetQ enables you to create and manage multiple switch configuration profiles. Each configuration can contain Cumulus Linux, NetQ Agent, and switch settings. These can then be applied to a group of switches at once.

You can view, create, and modify switch configuration profiles and their assignments at any time using the Switch Configurations card.

{{<notice info>}}
New switch configuration features introduced with release 3.3.0 are Early Access features and are provided in advance of general availability to enable customers to try them out and provide feedback. These features are bundled into the <code>netq-apps</code> package so there is no need to install a separate software package. The features are enabled by default and marked in the documentation here as Early Access.
{{</notice>}}

### View Switch Configuration Profiles

You can view existing switch configuration profiles using the Switch Configurations card.

1. Open the lifecycle management (Manage Switch Assets) dashboard.

    Click {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/03-Menu/navigation-menu.svg" width="18" height="18">}}, then select **Manage Switches**. Alternately, click {{<img src="https://icons.cumulusnetworks.com/05-Internet-Networks-Servers/06-Servers/server-upload.svg" width="18" height="18">}} in a workbench header.

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

4. You must begin with the Cumulus Linux option. Then you can decide which other aspects of configuration you want included in this template: NetQ Agent, VLANs, MLAG, and/or interfaces.

5. Specify the settings for each using the following instructions.

    {{<notice info>}}
The VLAN, MLAG, Interface profiles and Interfaces settings are provided as Early Access capabilities.
    {{</notice>}}

    {{<tabs "TabID383" >}}

{{<tab "CL Configuration" >}}

Four configuration items are available for the Cumulus Linux configuration portion of the switch configuration profile. Items with a red asterisk (*) are required.

{{<figure src="/images/netq/lcm-switch-config-cl-tab-330.png" width="700">}}

1. Enter a name for the configuration. The name can be a maximum of 22 characters, including spaces.

2. Enter the management interface (VLAN ID) to be used for communications with the switches with this profile assigned. Commonly this is either *eth0* or *eth1*.

3. Select the type of switch that will have this configuration assigned from the **Switch type** dropdown. Currently this includes Mellanox SN series of switches.

    {{<notice note>}}
Choose carefully as once this has been selected, it cannot be changed for the given switch configuration profile. You must create a new profile.
    {{</notice>}}

4. If you want to include network settings in this configuration, click **Add**.

    This opens the Network Template forms. You can select an existing network template to pre-populate the parameters already specified in that template, or you can start from scratch to create a different set of network settings.

    {{<figure src="/images/netq/lcm-switch-config-ntwk-template-config-330.png" width="700">}}

<div style="padding-left: 18px;"><em>To use an existing network template as a starting point:</em>

- Select the template from the dropdown.

- If you have selected a network template that has any SNMP parameters specified, verify those parameters and specify any additional required parameters, then click **Continue** or click **NTP**.

- If the selected network template has any NTP parameters specified, verify those parameters and specify any additional required parameters, then click **Continue** or click **LLDP**.

- If the selected network template has any LLDP parameters specified, verify those parameters, then click **Continue** or click **User**.

- If the selected network template has any User parameters specified, verify those parameters and specify any additional required parameters, then click **Done**.

- If you think this Cumulus Linux configuration is one that you will use regularly, you can make it a template. Enter a name for the configuration and click **Yes**.

    {{<figure src="/images/netq/lcm-switch-config-save-as-template-dialog-320.png" width="200">}}

</div>

<div style="padding-left: 18px;"><em>To create a new set of network settings:</em>

- Select the various forms to specify parameters for this configuration. Note that selected parameters are required on each form, noted by red asterisks (*). Refer to {{<link title="Manage Switch Configurations/#create-network-templates" text="Create Network Templates">}} for a description of the fields.

- When you have completed the network settings, click **Done**.

    If you are not on the User form, you need to go to that tab for the **Done** option to appear.

In either case, if you change your mind about including network settings, click {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/remove-circle.svg" height="18" width="18">}} to exit the form.

</div>

5. Click one of the following:

<div style="padding-left: 18px;"><ul><li><strong>Discard</strong> to clear your entries and start again</li>
    <li><strong>Save and go to NetQ Agent configuration</strong> to configure additional switch configuration parameters</li>
    <li><strong>Save and deploy on switches</strong> if the switch configuration is now complete</li>
    </ul></div>

{{</tab>}}

{{<tab "NetQ Agent" >}}

1. Click **NetQ Agent Configuration**.

    {{<figure src="/images/netq/lcm-switch-config-nqagent-config-330.png" width="700">}}

2. Select an existing NetQ Configuration profile or create a custom one.

    <em>To use an existing network template as a starting point:</em>

<div style="padding-left: 18px;"><ul><li>Select the configuration profile from the dropdown.</li>
<li>Modify any of the parameters as needed.</li></ul>

<em>To create a new configuration profile:</em>

<ul><li>Select values as appropriate for your situation. Refer to {{<link title="Manage Switch Configurations/#create-cumulus-netq-configuration-profiles" text="Create NetQ Configuration Profiles">}} for descriptions of these parameters.</li></ul></div>

3. Click one of the following:

<div style="padding-left: 18px;"><ul><li><strong>Discard</strong> to clear your entries and start again</li>
    <li><strong>Save and go to VLANs</strong> to configure additional switch configuration parameters</li>
    <li><strong>Save and deploy on switches</strong> if the switch configuration is now complete</li>
    </ul></div>

{{</tab>}}

{{<tab "VLANs" >}}

*This is an Early Access capability.*

1. Click **VLANs**.

2. Click **Add VLAN/s** if none are present, or click {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/43-Remove-Add/add-circle.svg" height="18" width="18">}} to add more VLANs to the switch configuration.

    {{<figure src="/images/netq/lcm-switch-config-add-vlans-330.png" width="400">}}

3. Enter a name for the VLAN when creating a single VLAN or enter a prefix (combined with the VLAN ID) for multiple VLANs.

4. Enter a single VLAN ID (1-4096) or a range of IDs. When entering multiple IDs, separate them by commas and do not use spaces. For example, you can enter them:

<div style="padding-left: 18px;"><ul><li>One at a time: 25,26,27,28,85,86,87,88,89,112</li>
<li>As a set of ranges and individual IDs: 25-28,85-89 or 25-28,85-89,112</li>
<li>As a single range: 25-28 or 85-89</li></ul></div>

5. Click **Create**.

    The VLAN/s are displayed in the VLAN list. Once VLANs are in the list, they can be exported, modified, removed, and duplicated using the menu above the list. Simply select one, all, or filter for a subset of VLANs, then click the relevant menu icon.

    {{<figure src="/images/netq/lcm-switch-config-vlans-330.png" width="700">}}

6. Click one of the following:

<div style="padding-left: 18px;"><ul><li><strong>Discard</strong> to clear your entries and start again</li>
    <li><strong>Save and go to MLAG</strong> to configure additional switch configuration parameters</li>
    <li><strong>Save and deploy on switches</strong> if the switch configuration is now complete</li>
    </ul></div>

{{</tab>}}

{{<tab "MLAG" >}}

MLAG is disabled by default. If you want to include MLAG in the switch configuration, you must enable it.

1. Click **Enable**.

    {{<figure src="/images/netq/lcm-switch-config-mlag-330.png" width="700">}}

2. Select the VLAN over which MLAG traffic is communicated. If you have created VLANs already, select the VLAN from the Management VLAN dropdown. If you have not yet created any VLANs, refer to VLAN tab and then return here.

3. Accept the default (180 seconds) or modify the amount of time `clagd` should wait to bring up the MLAG bonds and anycast IP addresses.

4. Specify the peerlink. Note items with a red asterisk  (*) are required.

<div style="padding-left: 18px;"><ul><li>Enter the supported MTU for this link</li>
    <li>Enter the minimum number of links to use. Add additional links to handle link failures of the peerlink bond itself.</li>
    <li>Select the private VLAN (PVID) from the dropdown. If you have not yet created any VLANs, refer to VLAN tab and then return here.</li>
    <li>Enter a tagged VLAN range to link switches.</li>
    <li>Designate which ports are to be used, including ingress and egress ports.</li>
    </ul></div>

5. Click one of the following:

<div style="padding-left: 18px;"><ul><li><strong>Discard</strong> to clear your entries and start again</li>
    <li><strong>Save and go to Interface profiles</strong> to configure additional switch configuration parameters</li>
    <li><strong>Save and deploy on switches</strong> if the switch configuration is now complete</li>
    </ul></div>

{{</tab>}}

{{<tab "Interface Profiles" >}}

*This is an Early Access capability.*

Every interface requires at least one interface profile. Specifically, a bond, SVI, sub-interface, or port interface require at least one corresponding interface profile.  For example, for a given bond interface, you must have at least one bond interface profile. For a given SVI, you must have at least one SVI interface profile. And so forth. Each of these can be configured independently. That is, configuring a bond interface and interface profile does not require you to configure any of the other SVI, sub-interface or port interface options.

Interface profiles are used to speed configuration of switches by configuring common capabilities of an interface component and then referencing that profile in the component specification.

### Add Bond Profiles

You can create a new bond profile or import an existing one to modify. Bond profiles are used to specify interfaces in the switch configuration.

*To create a new bond profile:*

1. Click **Interface profiles**.

2. Click **Create** if no profiles yet exist, or click {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/43-Remove-Add/add-circle.svg" height="18" width="18">}} to add another bond profile.

    {{<figure src="/images/netq/lcm-switch-config-ifprofs-add-bondprof-330.png" width="400">}}

3. Enter a unique name for the bond profile. Note that items with a red asterisk (*) are required.

4. Click on the type of bond this profile is to support; either layer 2 (**L2**) or layer 3 (**L3**).

5. Enter the supported MTU for this bond profile.

6. Enter the minimum number of links to use. Add additional links to handle link failures of the bond itself.

7. Select the mode this profile is to support: either **Lacp** or **Static**.

    Choosing **Lacp** (link aggregation control protocol) allows for redundancy by load-balancing traffic across all available links. Choosing **Static** provides no load balancing.

    If you select LACP, then you must also specify:
    
<div style="padding-left: 18px;"><ul><li>The LACP rate: how often to expect PDUs at the switch; <strong>Fast</strong>&ndash;every second, or <strong>Slow</strong>&ndash;every 30 seconds</li>
    <li>Whether to enable or disable LACP bypass: <strong>Enable</strong> allows a bond configured in 802.3ad mode to become active and forward traffic even when there is no LACP partner</li>
    </ul></div>

8. Enable or disable whether the bond must be dually connected. When enabled, you must specify the associated MLAG identifier.

9. Click **Next** to specify the bond attributes.

    {{<figure src="/images/netq/lcm-switch-config-ifprofs-bond-attr-330.png" width="400">}}

10. Select a private VLAN ID (pvid) from the dropdown for communication.

11. Assign one or more tagged VLANs to support traffic from more than one VLAN on a port.

<!-- 10. Indicated whether this bond profile is to support multi-homing (connections to more than one network) (**True**) or to only a single network (**False**). -->

12. Review your specification, clicking **Back** to review the bond details.

13. When you are satisfied with the bond profile specification, click **Create**.

    The bond profiles are displayed in the Bond list. Once bonds are in the list, they can be exported, modified, removed, and duplicated using the menu above the list. Simply select one, all, or filter for a subset of bonds, then click the relevant menu icon.

    {{<figure src="/images/netq/lcm-switch-config-ifprofs-bondprofs-330.png" width="700">}}

*To import an existing bond profile:*

1. Click **Interface profiles**.

2. Click **Import** if no profiles yet exist, or click {{<img src="https://icons.cumulusnetworks.com/16-Files-Folders/01-Common-Files/common-file-download.svg" height="18" width="18">}} to import a bond profile.

    {{<figure src="/images/netq/lcm-switch-config-ifprofs-import-bond-330.png" width="400">}}

3. Enter a name for this new bond profile.

4. Select a bond from the dropdown.

5. Click **Import**.

6. Select the profile from the list and click {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/22-Edit/pencil-1.svg" height="18" width="18">}} to edit it.

### Add SVI Profiles

You can create a new SVI profile or import an existing one to modify. SVI profiles are used to specify interfaces in the switch configuration.

*To create a new SVI profile:*

1. Click **Interface profiles**.

2. Click **SVI Profiles**.

3. Click **Create** if no profiles yet exist, or click {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/43-Remove-Add/add-circle.svg" height="18" width="18">}} to add a new SVI profile.

    {{<figure src="/images/netq/lcm-switch-config-ifprofs-add-sviprof-330.png" width="400">}}

4. Enter a unique name for the SVI profile.

5. Enter the supported MTU for this SVI profile.

6. Select a VRF profile from the dropdown, or enter the name of a VRF and click *Add VRF*.

7. Enable VRR if desired, and enter the associated MAC address.

8. Click **Create**.

    The SVI profiles are displayed in the SVI list. Once SVIs are in the list, they can be exported, modified, removed, and duplicated using the menu above the list. Simply select one, all, or filter for a subset of SVIs, then click the relevant menu icon.

    {{<figure src="/images/netq/lcm-switch-config-ifprofs-svis-330.png" width="700">}}

*To import an existing SVI profile:*

1. Click **Interface profiles**.

2. Click **SVI Profiles**.

3. Click **Import** if no profiles yet exist, or click {{<img src="https://icons.cumulusnetworks.com/16-Files-Folders/01-Common-Files/common-file-download.svg" height="18" width="18">}} to import an SVI profile.

    {{<figure src="/images/netq/lcm-switch-config-ifprofs-import-bond-330.png" width="400">}}

4. Enter a name for this new SVI profile.

5. Select an SVI from the dropdown.

6. Click **Import**.

7. Select the profile from the list and click {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/22-Edit/pencil-1.svg" height="18" width="18">}} to edit it.

### Add Sub-interfaces Profiles

You can create a new subinterface profile or import an existing one to modify. Subinterface profiles are used to specify interfaces in the switch configuration.

1. Click **Interface profiles**.

2. Click **Subinterface Profiles**.

3. Click **Create** if no profiles yet exist, or click {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/43-Remove-Add/add-circle.svg" height="18" width="18">}} to add a new sub-interface profile.

    {{<figure src="/images/netq/lcm-switch-config-ifprofs-add-subifprof-330.png" width="400">}}

4. Enter a unique name for the subinterface profile.

5. Enter the supported MTU for this subinterface profile.

6. Select a VRF profile from the dropdown, or enter the name of a VRF and click *Add VRF*.

7. Click **Create**.

    The subinterface profiles are displayed in the subinterface list. Once subinterfaces are in the list, they can be exported, modified, removed, and duplicated using the menu above the list. Simply select one, all, or filter for a subset of subinterfaces, then click the relevant menu icon.

    {{<figure src="/images/netq/lcm-switch-config-ifprofs-subifprofs-330.png" width="700">}}

*To import an existing subinterface profile:*

1. Click **Interface profiles**.

2. Click **Subinterface Profiles**.

3. Click **Import** if no profiles yet exist, or click {{<img src="https://icons.cumulusnetworks.com/16-Files-Folders/01-Common-Files/common-file-download.svg" height="18" width="18">}} to import a subinterface profile.

    {{<figure src="/images/netq/lcm-switch-config-ifprofs-import-subif-330.png" width="400">}}

4. Enter a name for this new subinterface profile.

5. Select a subinterface from the dropdown.

6. Click **Import**.

7. Select the profile from the list and click {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/22-Edit/pencil-1.svg" height="18" width="18">}} to edit it.

### Add Port Profiles

You can create a new port profile or import an existing one to modify. Port profiles are used to specify interfaces in the switch configuration.

1. Click **Interface profiles**.

2. Click **Port Profiles**.

3. Click **Create** if no profiles yet exist, or click {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/43-Remove-Add/add-circle.svg" height="18" width="18">}} to add a new port profile.

    {{<figure src="/images/netq/lcm-switch-config-ifprofs-add-portprof-330.png" width="400">}}

4. Enter a unique name for the port profile. Note that items with a red asterisk (*) are required.

5. Click on the type of port this profile is to support; either layer 2 (**L2**) or layer 3 (**L3**).

6. Enter the supported MTU for this port profile.

7. Enable or disable forward error correction (FEC).

8. Enable or disable auto-negotiation of link speeds.

9. Specify the whether to support transmit and receive on this port (**Full** duplex) or either transmit or receive on this port (**Half** duplex).

10. Specify the port speed from the dropdown. Choices are based on the switch type selected iin the CL configuration tab.

11. Click **Next** to specify port attributes.

    {{<figure src="/images/netq/lcm-switch-config-ifprofs-add-portprof-attr-330.png" width="400">}}

12. Select a private VLAN ID (pvid) for communication from the dropdown.

13. Assign one or more tagged VLANs to support traffic from more than one VLAN on a port.

14. Review your specification, clicking **Back** to review the bond details.

15. When you are satisfied with the port profile specification, click **Create**.

    The port profiles are displayed in the Port list. Once ports are in the list, they can be exported, modified, removed, and duplicated using the menu above the list. Simply select one, all, or filter for a subset of ports, then click the relevant menu icon.

    {{<figure src="/images/netq/lcm-switch-config-ifprofs-portprofs-330.png" width="700">}}

*To import an existing port profile:*

1. Click **Interface profiles**.

2. Click **Port Profiles**.

3. Click **Import** if no profiles yet exist, or click {{<img src="https://icons.cumulusnetworks.com/16-Files-Folders/01-Common-Files/common-file-download.svg" height="18" width="18">}} to import a port profile.

    {{<figure src="/images/netq/lcm-switch-config-ifprofs-import-portprof-330.png" width="400">}}

4. Enter a name for this new port profile.

5. Select a port profile from the dropdown.

6. Click **Import**.

7. Select the profile from the list and click {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/22-Edit/pencil-1.svg" height="18" width="18">}} to edit it.

8. Now that you have one complete interface profile defined, click one of the following:

<div style="padding-left: 18px;"><ul><li><strong>Discard</strong> to clear your entries and start again</li>
    <li><strong>Save and go to Interfaces</strong> to configure additional switch configuration parameters</li>
    <li><strong>Save and deploy on switches</strong> if the switch configuration is now complete</li>
    </ul></div>

{{</tab>}}

{{<tab "Interfaces" >}}

*This is an Early Access capability.*

Every interface requires at least one interface profile. Specifically, a bond, SVI, sub-interface, or port interface require at least one corresponding interface profile.  For example, for a given bond interface, you must have at least one bond interface profile. For a given SVI, you must have at least one SVI interface profile. And so forth. Each of these can be configured independently. That is, configuring a bond interface and interface profile does not require you to configure any of the other SVI, sub-interface or port interface options.

Interfaces identify how and where communication occurs.

### Add Bonds

Bonds indicate how switches are connected to each other. You must have at least one bond interface profile specified to configure a bond interface (return to the **Interface Profiles** tab and see *Add Bond Interface Profiles* if needed).

1. Click **Interfaces**.

2. Click **Create** if no bonds exist yet, or click {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/43-Remove-Add/add-circle.svg" height="18" width="18">}} to add a new bond.

    {{<figure src="/images/netq/lcm-switch-config-ifs-add-bond-330.png" width="400">}}

3. Enter a unique name for the bond.

4. Optionally enter an alias for the bond.

5. Select a bond profile from the dropdown. If you have not yet created one, follow the instructions in the Interface Profiles tab and then return here.

6. Assign the ports included in this bond. The port name is provided based on the switch type selection you made earlier. The port numbers are entered here.

7. When you are satisfied with the bond specification, click **Create**.

    The bonds are displayed in the Bond list. Once bonds are in the list, they can be exported, modified, removed, and duplicated using the menu above the list. Simply select one, all, or filter for a subset of bonds, then click the relevant menu icon.

    {{<figure src="/images/netq/lcm-switch-config-ifs-bonds-330.png" width="700">}}

8. Repeat these steps to add additional bonds as needed. Then continue to specifying SVIs.

### Add SVIs

Add SVIs (switch virtual interfaces) to your switch configuration when you need a virtual interface at layer 3 to a VLAN. You must have at least one SVI interface profile specified to configure an SVI interface (return to the **Interface Profiles** tab and see *Add SVI Interface Profiles* if needed).

1. Click **Interfaces**.

2. Click **SVIs**.

3. Click **Create** if no SVIs exist, or click {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/43-Remove-Add/add-circle.svg" height="18" width="18">}} to add a new SVI.

    {{<figure src="/images/netq/lcm-switch-config-ifs-add-svi-330.png" width="400">}}

4. Enter a unique name for the SVI.

5. Select a VLAN to apply to this SVI.

6. Select an SVI profile to apply to this SVI. If you have not yet created one, follow the instructions in the **Interface Profiles** tab and then return here.

7. When you are satisfied with your SVI specification, click **Create**.

    The SVIs are displayed in the SVI list. Once SVIs are in the list, they can be exported, modified, removed, and duplicated using the menu above the list. Simply select one, all, or filter for a subset of SVIs, then click the relevant menu icon.

    {{<figure src="/images/netq/lcm-switch-config-ifs-svis-330.png" width="700">}}

8. Repeat these steps to add additional SVIs as needed. Then continue to specifying subinterfaces.

### Add Subinterfaces

Add subinterface to your switch configuration when you want a VLAN associated with a given interface. You must have at least one subinterface interface profile specified to configure a bond interface (return to the **Interface Profiles** tab and see *Add Subinterface Profiles* if needed).

1. Click **Interfaces**.

2. Click **Subinterfaces**.

3. Click Create if no subinterfaces exist, or click {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/43-Remove-Add/add-circle.svg" height="18" width="18">}} to add a new subinterface.

    {{<figure src="/images/netq/lcm-switch-config-ifs-add-subif-330.png" width="400">}}

4. Enter a unique name for the subinterface in the format \<parent-interface-name:vlan-subinterface-id\>. For example, swp2:1.

5. Optionally enter an alias for this subinterface.

6. Select a VLAN to apply to this subinterface. This should match the name you specified in step 4.

7. Select a parent interface from the dropdown. This should match the name you specified in step 4.

8. Select a subinterface profile to apply to this subinterface.

9. When you are satisfied with your subinterface specification, click **Create**.

    The subinterfaces are displayed in the subinterface list. Once subinterfaces are in the list, they can be exported, modified, removed, and duplicated using the menu above the list. Simply select one, all, or filter for a subset of subinterfaces, then click the relevant menu icon.

    {{<figure src="/images/netq/lcm-switch-config-ifs-subifs-330.png" width="700">}}

10. Repeat these steps to add additional subinterfaces as needed. Then continue to specifying ports.

### Add Ports

This tab describes all of the ports on the identified switch type. The port name and bond are provided by default (based on your previous switch configuration entries). For each port, you must define the speed and assign an interface profile. Optionally you can configure ports to be split to support multiple interfaces. Any caveats related to port configuration on the specified type of switch are listed under the port listing.

You must have at least one port interface profile specified to configure a port interface (return to the **Interface Profiles** tab and see *Add Port Interface Profiles* if needed).

1. Click **Interfaces**.

2. Click **Ports**.

    {{<figure src="/images/netq/lcm-switch-config-ifs-ports-330.png" width="700">}}

3. For each port, verify the port speed. For any port that should be other than the default highlighted, click on the alternate speed choice.

4. If you want to break out selected ports, choose the split value from the dropdown.

    In the example above, swp1 has its speed set to 100 Gbps. On the Mellanox SN2700 switch being configured here, this port can then be broken into two 50 Gbps speed interfaces or four 25 Gbps speed interfaces. Some limitations on other ports may occur when you breakout a given port. In this case, if we were to choose a 4x breakout, swp2 would become unavailable and you would not be able to configure that port.

    {{<figure src="/images/netq/lcm-switch-config-ifs-ports-brkout-330.png" width="100">}}

5. If a port is missing a bond (all ports must have a bond), return to **Interfaces** > **Bonds** to assign it.

6. Assign an interface profile for each port by clicking on the *Select profile* link.

    Click L2 or L3 to view available port profiles. If you have not yet created one, follow the instructions in the **Interface Profiles** tab and then return here.

    Click on the port profile card to select it and return to the port list. If you accidentally select the wrong port profile, simply click on the profile name and reselect a different profile.

    {{<figure src="/images/netq/lcm-switch-config-ifs-ports-assignprof-330.png" width="400">}}

7. When you are satisfied with the port specification for all ports, click one of the following:

<div style="padding-left: 18px;"><ul><li><strong>Discard</strong> to clear your entries and start again.</li>
    <li><strong>Save and go to Switches</strong> to assign the switch configuration to switches now.</li>
    <li><strong>Save and deploy on switches</strong> to complete the switch configuration and go to your switch configurations listing. You can edit the configuration to assign it to switches at a later time.</li>
    </ul></div>

{{</tab>}}

{{</tabs>}}

### Assign Switch Configuration Profiles to Switches

After you have completed one or more switch configurations, you can assign them to one or more switches.

To assign a switch configuration:

1. Open the **Switches** tab in the switch configuration you want to assign:

    - If you have just completed creating a switch configuration and are still within the configuration page, simply click the **Switches** tab.

        {{<figure src="/images/netq/lcm-switch-config-switches-tab-highlight-330.png" width="700">}}

    - If you want to apply a previously saved configuration, click {{<img src="https://icons.cumulusnetworks.com/05-Internet-Networks-Servers/06-Servers/server-upload.svg" width="18" height="18">}} on a workbench header > click **Configuration Management** > click **Manage** on the Switch Configurations card > locate the desired configuration > click {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/03-Menu/navigation-menu-horizontal.svg" height="18" width="18">}} > select **Edit** > click the **Switches** tab.

        {{<figure src="/images/netq/lcm-switch-config-edit-switchconfig-330.png" width="700">}}

    In either case, you should land on the switch configuration page with the **Switches** tab open.

    {{<figure src="/images/netq/lcm-switch-config-switches-330.png" width="700">}}

<div style="padding-left: 18px;">A few items to note on this tab:
    <ul><li>Above the switches (left), the number of switches that can be assigned and the number of switches that have already been assigned a switch configuration</li>
        <li>Above the switches (right), management tools to help find the switches you want to assign with this configuration, including filter and search.</li>
    </ul></div>

2. Select the switches to be assigned this configuration. Each switch selected must have items specified that are particular to that switch. This can be done in one of two ways:

   - Select an individual switch by clicking on the switch card
   - Filter or search for switches and then click **Save and deploy on switches**

   Either way, a per-instance variables form appears for the selected or one of the selected switches.

   *This is an Early Access capability.*

    {{<figure src="/images/netq/lcm-switch-config-switches-variables-330.png" width="700">}}

3. Enter the required parameters for each switch using the following instructions.

    {{<tabs "TabID1086" >}}

{{<tab "General Changes" >}}

*This is an Early Access capability.*

1. Verify the IP address of the switch.

2. Optionally change the hostname of the switch.

3. Enter the loopback IP address for the switch.

4. Enter the System MAC address for the switch.

5. Enter the system ID for the switch.

6. Enter a priority for the switch in the format of an integer, where zero (0) is the lowest priority.

7. Enter a backup IP address for the switch in the event it becomes unreachable.

8. Enter a VXLAN anycast IP address for the switch.

9. Enter the name of a VRF for the switch.

    {{<figure src="/images/netq/lcm-switch-config-switches-variables-general-330.png" width="500">}}

10. Click **Continue to vrf details**, or click **Save and Exit** to come back later to finish the specification. If you choose to save and exit, click {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/14-Alerts/alert-circle.svg" height="18" width="18">}} on the switch card to return to the per instance variable definition pages.

{{</tab>}}

{{<tab "VRF" >}}

The VRF identified in **General Changes** is presented. Optionally add the associated IPv4 and IPv6 addresses for this VRF.

{{<figure src="/images/netq/lcm-switch-config-switches-variables-vrf-330.png" width="500">}}

Click **Continue to bond details**, or click **Save and Exit** to come back later to finish the specification. If you choose to save and exit, click {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/14-Alerts/alert-circle.svg" height="18" width="18">}} on the switch card to return to the per instance variable definition pages.

{{</tab>}}

{{<tab "Bond Changes" >}}

{{<img src="https://icons.cumulusnetworks.com/11-Content/01-Content-Creation/content-paper-edit.svg" height="36" width="36">}} This topic is in development.

{{</tab>}}

{{<tab "SVI Changes" >}}

The SVIs specified are presented. If no SVIs are defined and there should be, return to the Interface Profiles and Interfaces tabs to specify them.

Optionally add the associated IPv4 and IPv6 addresses this switch should use for these SVIs.

{{<figure src="/images/netq/lcm-switch-config-switches-variables-svi-330.png" width="500">}}

Click **Continue to subinterface details**, or click **Save and Exit** to come back later to finish the specification. If you choose to save and exit, click {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/14-Alerts/alert-circle.svg" height="18" width="18">}} on the switch card to return to the per instance variable definition pages.

{{</tab>}}

{{<tab "Subinterface Changes" >}}

The subinterfaces specified are presented. If no subinterfaces are defined and there should be, return to the Interface Profiles and Interfaces tabs to specify them.

Optionally add the associated IPv4 and IPv6 addresses this switch should use for these subinterfaces.

{{<figure src="/images/netq/lcm-switch-config-switches-variables-subif-330.png" width="500">}}

Click **Continue to port details**, or click **Save and Exit** to come back later to finish the specification. If you choose to save and exit, click {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/14-Alerts/alert-circle.svg" height="18" width="18">}} on the switch card to return to the per instance variable definition pages.

{{</tab>}}

{{<tab "Port Changes" >}}

{{<img src="https://icons.cumulusnetworks.com/11-Content/01-Content-Creation/content-paper-edit.svg" height="36" width="36">}} This topic is in development.

{{</tab>}}

{{</tabs>}}

4. Click **Save and Exit**.

5. To run the job to apply the configuration, click **Save and deploy on switches**.

6. Enter a name for the job (maximum of 22 characters including spaces). Verify the configuration name and number of switches you have selected to assign this configuration to. then click **Continue**.

    This opens the monitoring page for the assignment jobs, similar to the upgrade jobs. The job title bar indicates the name of the switch configuration being applied and the number of switches that to be assigned with the configuration. (After you have multiple switch configurations created, you might have more than one configuration being applied in a single job.) Each switch element indicates its hostname, IP address, installed Cumulus Linux and NetQ versions, a note indicating this is a new assignment, the switch configuration being applied, and a menu that provides the detailed steps being executed. The last is useful when the assignment fails as any errors are included in this popup.

    {{<figure src="/images/netq/lcm-switch-config-assign-job-success-320.png" width="700">}}

    {{<img src="/images/netq/lcm-switch-config-assign-job-status-popup-320.png" width="230">}} {{<img src="/images/netq/lcm-switch-config-assign-job-status-popup-fail-330.png" width="260">}}

6. Click {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/close.svg" height="14" width="14">}} to return to the switch configuration page where you can either create another configuration and apply it. If you are finished assigning switch configurations to switches, click {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/43-Remove-Add/remove-circle.svg" height="18" width="18">}} to return to the lifecycle management dashboard.

7. When you return the dashboard, your Switch Configurations card on the Configuration Management tab shows the new configurations, and the Config Assignment History card appears on the Job History tab that shows a summary status of all configuration assignment jobs attempted.

    {{<figure src="/images/netq/lcm-switch-config-post-assign-switchconfigs-330.png" width="700">}}
    
    {{<figure src="/images/netq/lcm-switch-config-post-assign-config-assign-330.png" width="400">}}

8. Click **View** on the Config Assignment History card to open the details of all assignment jobs. Refer to {{<link title="Manage Switch Configurations/#view-switch-configuration-history">}} for more detail about this card.

### Edit a Switch Configuration

You can edit a switch configuration at any time. After you have made changes to the configuration, you can apply it to the same set of switches or modify the switches using the configuration as part of the editing process.

To edit a switch configuration:

1. Locate the Switch Configurations card on the **Configuration Management** tab of the lifecycle management dashboard.

2. Click **Manage**.

3. Locate the configuration you want to edit. Scroll down or filter the listing to help find the configuration when there are multiple configurations.

4. Click {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/03-Menu/navigation-menu-horizontal.svg" height="18" width="18">}}, then select *Edit*.

5. Follow the instructions in {{<link title="Manage Switch Configurations/#create-switch-configuration-profiles" text="Create Switch Configuration Profiles">}}, starting at Step 5, to make any required edits.

### Clone a Switch Configuration

You can clone a switch configuration assignment job at any time.

To clone an assignment job:

1. Locate the Switch Configurations card on the **Configuration Management** tab of the lifecycle management dashboard.

2. Click **Manage**.

3. Locate the configuration you want to clone. Scroll down or filter the listing to help find the configuration when there are multiple configurations.

4. Click {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/03-Menu/navigation-menu-horizontal.svg" height="18" width="18">}}, then select *Clone*.

5. Click {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/03-Menu/navigation-menu-horizontal.svg" height="18" width="18">}}, then select *Edit*.

6. Change the Configuration Name.

7. Follow the instructions in {{<link title="Manage Switch Configurations/#create-switch-configuration-profiles" text="Create Switch Configuration Profiles">}}, starting at Step 5, to make any required edits.

### Remove a Switch Configuration

You can remove a switch configuration at any time; however if there are switches with the given configuration assigned, you must first assign an alternate configuration to those switches.

To remove a switch configuration:

1. Locate the Switch Configurations card on the **Configuration Management** tab of the lifecycle management dashboard.

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

1. Locate the Switch Configurations card on the **Configuration Management** tab of the lifecycle management dashboard.

2. Click **Manage**.

    {{<figure src="/images/netq/lcm-switch-config-manage-320.png" width="700">}}

3. Locate the configuration you want to assign.

    Scroll down or filter the listing by:
    - **Time Range**: Enter a range of time in which the switch configuration was created, then click **Done**.
    - **All switches**: Search for or select individual switches from the list, then click **Done**.
    - **All switch types**: Search for or select individual switch series, then click **Done**.
    - **All users**: Search for or select individual users who created a switch configuration, then click **Done**.
    - **All filters**: Display all filters at once to apply multiple filters at once. Additional filter options are included here. Click **Done** when satisfied with your filter criteria.

    By default, filters show *all* of the items of the given filter type until it is restricted by these settings.

4. Click **Select switches** in the switch configuration summary.

    {{<figure src="/images/netq/lcm-switch-config-manage-select-switches-320.png" width="700">}}

5. Select the switches that you want to assign to the switch configuration.

    Scroll down or use the filter and **Search** options to help find the switches of interest. You can filter by role, Cumulus Linux version, or NetQ version. The badge on the filter icon indicates the number of filters applied. Colors on filter options are only used to distinguish between options. No other indication is intended.

    In this example, we have three roles defined, and we have selected to filter on the spine role.

    {{<figure src="/images/netq/lcm-switch-config-manage-select-switches-filter-330.png" width="300">}}

    The result is four switches. Note that only the switches that meet the criteria and have no switch configuration assigned are shown. In this example, there are two additional switches with the spine role, but they already have a switch configuration assigned to them. Click on the link above the list to view those switches.

    Continue narrowing the list of switches until all or most of the switches are visible.

6. Click on each switch card to be given the switch configuration.

    When you select a card, if the per-switch variables have not already been specified, you must complete that first. Refer to {{<link title="#assign-switch-configuration-profiles-to-switches" text="Assign Switch Configuration Profiles to Switches">}} beginning at step 2, then return here. If a switch has an incomplete specification of the required variables, click {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/14-Alerts/alert-circle.svg" height="18" width="18">}} to enter the required information.

    {{<figure src="/images/netq/lcm-switch-config-manage-selected-switches-320.png" width="700">}}

7. Verify all of the switches are selected that you want applied with this configuration, then click **Done**.

8. If you have additional switches that you want to assign a different switch configuration, follow Steps 3-7 for each switch configuration.

    A job is created with each of the assignments configured. It is shown at the botton of the page. If you have multiple configuration assignments, they all become part of a single assignment job.

9. Click **Start Assignment** to start the job.

    This example shows only one switch configuration assignment.

    {{<figure src="/images/netq/lcm-switch-config-manage-start-assign-320.png" width="700">}}

10. Enter a name for the job (maximum of 22 characters including spaces), then click **Continue**.

    {{<figure src="/images/netq/lcm-switch-config-manage-job-name-320.png" width="275">}}

11. Watch the progress or click {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/close.svg" height="14" width="14">}} to return to the switch configuration page where you can either create another configuration and apply it. If you are finished assigning switch configurations to switches, click {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/43-Remove-Add/remove-circle.svg" height="18" width="18">}} to return to the lifecycle management dashboard.

    The Config Assignment History card on the **Job History** tab is updated to include the status of the job you just ran.

#### Change the Configuration Assignment on a Switch

You can change the switch configuration assignment at any time. For example you might have a switch that is starting to experience reduced performance, so you want to run What Just Happened on it to see if there is a particular problem area. You can reassign this switch to a new configuration with WJH enabled on the NetQ Agent while you test it. Then you can change it back to its original assignment.

To change the configuration assignment on a switch:

1. Locate the Switch Configurations card on the **Configuration Management** tab of the lifecycle management dashboard.

2. Click **Manage**.

    {{<figure src="/images/netq/lcm-switch-config-manage-320.png" width="700">}}

3. Locate the configuration you want to assign. Scroll down or filter the listing to help find the configuration when there are multiple configurations.

4. Click **Select switches** in the switch configuration summary.

    {{<figure src="/images/netq/lcm-switch-config-manage-select-switches-320.png" width="700">}}

5. Select the switches that you want to assign to the switch configuration.

    Scroll down or use the filter and **Search** options to help find the switch(es) of interest.

6. Click on each switch card to be given the switch configuration.

    When you select a card, if the per-switch variables have not already been specified, you must complete that first. Refer to {{<link title="#assign-switch-configuration-profiles-to-switches" text="Assign Switch Configuration Profiles to Switches">}} beginning at step 2, then return here. If a switch has an incomplete specification of the required variables, click {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/14-Alerts/alert-circle.svg" height="18" width="18">}} to enter the required information.

7. Click **Done**.

8. Click **Start Assignment**.

9. Watch the progress.

    On completion, each switch shows the previous assignment and the newly applied configuration assignment.

    {{<figure src="/images/netq/lcm-switch-config-manage-assign-changed-320.png" width="700">}}

10. Click {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/close.svg" height="14" width="14">}} to return to the switch configuration page where you can either create another configuration and apply it. If you are finished assigning switch configurations to switches, click {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/43-Remove-Add/remove-circle.svg" height="18" width="18">}} to return to the lifecycle management dashboard.

    The Config Assignment History card on the **Job History** tab is updated to include the status of the job you just ran.

### View Switch Configuration History

You can view a history of switch configuration assignments using the Config Assignment History card.

To view a summary, locate the Config Assignment History card on the lifecycle management dashboard.

{{<figure src="/images/netq/lcm-config-assign-history-card-320.png" width="200">}}

To view details of the assignment jobs, click **View**.

{{<figure src="/images/netq/lcm-config-assign-history-job-listing-320.png" width="700">}}

Above the jobs, a number of filters are provided to help you find a particular job. To the right of those is a status summary of all jobs. Click <img src="https://icons.cumulusnetworks.com/52-Arrows-Diagrams/01-Arrows/arrow-right-1.svg" height="14" width="14"/> in the job listing to see the details of that job. Click {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/close.svg" height="14" width="14">}} to return to the lifecycle management dashboard.
