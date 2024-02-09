---
title: Switch Management
author: NVIDIA
weight: 630
toc: 4
---

Lifecycle management displays an inventory of switches that are available for software installation or upgrade through NetQ. From the inventory list, you can assign access profiles and roles to switches, and select switches for software installation and upgrades. You can also decommission switches, which removes them from the NetQ database.

{{%notice note%}}
If you manage a switch using an in-band network interface, {{<link url="Lifecycle-Management/#lcm-support-for-in-band-management" text="additional configurations">}} are required for LCM operations.
{{%/notice%}}

## View the LCM Switch Inventory

{{<tabs "TabID13" >}}

{{<tab "NetQ UI" >}}

Expand the {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/03-Menu/navigation-menu.svg" width="18" height="18">}} **Menu**, then select **Manage switches**. From the LCM dashboard, select the **Switch management** tab. The Switches card displays the number of switches that NetQ discovered and the network OS versions that are running on those switches:

{{<figure src="/images/netq/lcm-switches-490.png" alt="switches card displaying 525 discovered switches" width="200" height="330">}}

To view a table of all discovered switches and their attributes, select **Manage** on the Switches card.

{{<notice tip>}}
If you have more than one network OS version running on your switches, you can click a version segment on the Switches card chart to open a list of switches filtered by that version.
{{</notice>}}

{{</tab>}}

{{<tab "NetQ CLI" >}}

To view a list of all switches discovered by lifecycle management, run:

```
netq lcm show switches
    [cl-version <text-cumulus-linux-version>]
    [netq-version <text-netq-version>]
    [json]
```
Use the `version` options to display switches with a given OS version. For additional details, refer to the {{<link title="lcm/#netq-lcm-show-switches" text="command line reference">}}.

{{</tab>}}

{{</tabs>}}

The table of switches is the starting point for network OS upgrades or NetQ installations and upgrades. If the switches you want to upgrade are not present in the list, you can:

- Verify the missing switches are reachable using `ping`
- Run a [switch discovery](#switch-discovery), which locates all switches running Cumulus Linux in your network's fabric
- {{<link title="Install NetQ Agents" text="Install NetQ Agents on the switch">}}
- Verify the NetQ Agent is fresh and running version 4.1.0 or later for switches that already have the agent installed (click {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/03-Menu/navigation-menu.svg" height="18" width="18" alt="Main Menu">}} **Menu**, then click **Agents** or run `netq show agents`)
- {{<link title="Upgrade NetQ Agents" text="Upgrade NetQ Agents">}} (if needed)

## Switch Discovery

A switch discovery searches your network for all Cumulus Linux switches (with and without NetQ currently installed) and determines the versions of Cumulus Linux and NetQ installed. These results can be used to install or upgrade Cumulus Linux and NetQ on all discovered switches in a single procedure.

To discover switches running Cumulus Linux:

{{<tabs "Discover switches" >}}

{{<tab "NetQ UI" >}}

1. Click {{<img src="/images/netq/devices.svg" height="18" width="18">}} **Devices** in the workbench header, then click **Manage switches**.

2. On the Switches card, click **Discover**.

3. Enter a name for the scan.

    {{<figure src="/images/netq/discover-switches-profile-450.png" width="500" height="550">}}

4. Choose whether you want to look for switches by entering IP address ranges or import switches using a comma-separated values (CSV) file.

    {{<tabs "TabID314" >}}

{{<tab "IP Address Range" >}}

If you do not have a switch listing, then you can manually add the address ranges where your switches are located in the network. This has the advantage of catching switches that might have been missed in a file.

{{<notice tip>}}
A maximum of 50 addresses can be included in an address range. If necessary, break the range into smaller ranges.
{{</notice>}}

To discover switches using address ranges:

1. Enter an IP address range in the **IP Range** field.

    Ranges can be contiguous, for example *192.168.0.24-64*, or non-contiguous, for example *192.168.0.24-64,128-190,235*, but they must be contained within a single subnet.

2. Optionally, enter another IP address range (in a different subnet) by clicking {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/43-Remove-Add/add-circle.svg" height="18" width="18">}}.

    For example, *198.51.100.0-128* or *198.51.100.0-128,190,200-253*.

3. Add additional ranges as needed. Click {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/43-Remove-Add/subtract-circle.svg" height="18" width="18">}} to remove a range.

If you decide to use a CSV file instead, the ranges you entered will remain if you return to using IP ranges again.

{{</tab>}}

{{<tab "CSV Import" >}}

To import switches through a CSV file:

1. Click **Browse**.

2. Select the CSV file containing the list of switches.

    The CSV file must include a header containing *hostname*, *ip*, and *port*. They can be in any order you like, but the data must match that order. For example, a CSV file that represents the Cumulus reference topology could look like this:

    {{<figure src="/images/netq/lcm-import-switches-310.png" width="200" height="275">}}

<div style="padding-left: 18px;">or this:</div>

    {{<figure src="/images/netq/lcm-import-switches-2-310.png" width="200" height="275">}}

<div style="padding-left: 18px;">
{{<notice note>}}
You must have an IP address in your file, but the hostname is optional. If the port is blank, NetQ uses switch port 22 by default.
{{</notice>}}
</div>

Click **Remove** if you decide to use a different file or want to use IP address ranges instead. If you entered ranges before selecting the CSV file option, they remain.

{{</tab>}}

    {{</tabs>}}

5. Select an access profile from the dropdown menu. If you use Netq-Default you will see a message requesting that you {{<link title="Credentials and Profiles" text= "create or update your credentials">}}.

6. Click **Next**.

    When the network discovery is complete, NetQ presents the number of Cumulus Linux switches it found. Each switch can be in one of the following categories:

    - **Discovered without NetQ**: Switches found without NetQ installed
    - **Discovered with NetQ**: Switches found with some version of NetQ installed
    - **Discovered but Rotten**: Switches found that are unreachable
    - **Incorrect Credentials**: Switches found that are unreachable because the provided access credentials do not match those for the switches
    - **OS not Supported**: Switches found that are running a Cumulus Linux version not supported by LCM upgrades
    - **Not Discovered**: IP addresses which did not have an associated Cumulus Linux switch

    If the discovery process does not find any switches for a particular category, then it does not display that category.

{{</tab>}}

{{<tab "NetQ CLI" >}}

Use the {{<link title="lcm/#netq-lcm-discover" text="netq lcm discover">}} command, specifying a single IP address, a range of IP addresses where your switches are located in the network, or a CSV file containing the IP address.

You must also specify the access profile ID, which you can obtain with the `netq lcm show credentials` command.

       cumulus@switch:~$ netq lcm discover ip-range 10.0.1.12 profile_id credential_profile_3eddab251bddea9653df7cd1be0fc123c5d7a42f818b68134e42858e54a9c289
       NetQ Discovery Started with job id: job_scan_4f3873b0-5526-11eb-97a2-5b3ed2e556db

When the network discovery is complete, NetQ presents the number of Cumulus Linux switches it has found. The output displays their discovery status, which can be one of the following:

- **Discovered without NetQ**: Switches found without NetQ installed
- **Discovered with NetQ**: Switches found with some version of NetQ installed
- **Discovered but Rotten**: Switches found that are unreachable
- **Incorrect Credentials**: Switches found that are unreachable because the provided access credentials do not match those for the switches
- **OS not Supported**: Switches found that are running Cumulus Linux version not supported by the LCM upgrade feature
- **NOT\_FOUND**: IP addresses which did not have an associated Cumulus Linux switch

Note that if you previously ran a switch discovery, you can display its results with `netq lcm show discovery-job`:

```
cumulus@switch:~$ netq lcm show discovery-job job_scan_921f0a40-5440-11eb-97a2-5b3ed2e556db
Scan COMPLETED

Summary
-------
Start Time: 2021-01-11 19:09:47.441000
End Time: 2021-01-11 19:09:59.890000
Total IPs: 1
Completed IPs: 1
Discovered without NetQ: 0
Discovered with NetQ: 0
Incorrect Credentials: 0
OS Not Supported: 0
Not Discovered: 1


Hostname          IP Address                MAC Address        CPU      CL Version  NetQ Version  Config Profile               Discovery Status Upgrade Status
----------------- ------------------------- ------------------ -------- ----------- ------------- ---------------------------- ---------------- --------------
N/A               10.0.1.12                 N/A                N/A      N/A         N/A           []                           NOT_FOUND        NOT_UPGRADING
cumulus@switch:~$ 
```

{{</tab>}}

{{</tabs>}}

## Attach an Access Profile to a Switch

NetQ uses access profiles to store user authentications credentials. After {{<link title="Credentials and Profiles" text="creating an access profile">}} from your credentials, you can attach a profile to one or multiple switches.

{{<tabs "TabID85" >}}

{{<tab "NetQ UI" >}}

1. Expand the <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/03-Menu/navigation-menu.svg" height="18" width="18"/> **Menu** and select **Manage switches**. On the Switches card, select **Manage**.

2. The table displays a list of switches. The **Access type** column specifies whether the type of authentication is basic or SSH. The **Profile name** column displays the access profile that is assigned to the switch.

Select the switches to which you'd like to assign access profiles, then select {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/04-Login-Logout/login-key-1.svg" height="18" width="18">}} **Manage access profile** above the table: 

{{<figure src="/images/netq/manage-access-profile-450.png" alt="" width="500" height="375">}}

3. Select the profile from the list, then click **Apply**. If the profile you want to use isn't listed, select **Add new profile** and {{<link title="Credentials and Profiles/#create-access-profiles" text="follow the steps to create an access profile">}}.

4. Select **Ok** on the confirmation dialog. The updated access profiles are now reflected in the **Profile name** column.


{{</tab>}}

{{<tab "NetQ CLI" >}}

The command syntax to attach a profile to a switch is:

```
netq lcm attach credentials 
    profile_id <text-switch-profile-id> 
    hostnames <text-switch-hostnames>
```

1. Run `netq lcm show credentials` to display a list of access profiles. Note the profile ID that you'd like to assign to a switch.

2. Run `netq lcm show switches` to display a list of switches. Note the hostname of the switch(es) you'd like to attach a profile to.

3. Next, attach the credentials to the switch:

```
netq lcm attach credentials profile_id credential_profile_3eddab251bddea9653df7cd1be0fc123c5d7a42f818b68134e42858e54a9c289 hostnames tor-1,tor-2
Attached profile to switch(es).
```

4. Run `netq lcm show switches` and verify the change in the credential profile column.

{{</tab>}}

{{</tabs>}}

## Reassign or Detach an Access Profile

Detaching a profile from a switch restores it to the default access profile, Netq-Default.

{{<tabs "TabID110" >}}

{{<tab "NetQ UI" >}}

1. On the Switches card, click **Manage**.

2. From the table of switches, locate the switch whose access profile you'd like to manage. Hover over the access type column and select **Manage access**:

{{<figure src="/images/netq/detach-manage-access-450.png" alt="" width="500" height="270">}}

3. To assign a different access profile to the switch, select it from the list. To detach the access profile, select <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/23-Delete/bin-1.svg" width="18" height="18"/> **Detach**.

{{<figure src="/images/netq/manage-access-profile-spine-450.png" alt="" width="500" height="450">}}

After you detach the profile from the switch, NetQ reassigns it to the Netq-Default profile.

{{</tab>}}

{{<tab "NetQ CLI" >}}

The syntax for the detach command is `netq lcm detach credentials hostname <text-switch-hostname>`.

1. To obtain a list of hostnames, run `netq lcm show switches`.

2. Detach the access profile and specify the hostname. The following example detaches spine-1 from its assigned access profile:

```
cumulus@switch:~$ netq lcm detach credentials hostname spine-1
Detached profile from switch.
```

3. Run `netq lcm show switches` and verify the change in the credential profile column.

{{</tab>}}

{{</tabs>}}

## Role Management

You can assign switches one of four roles: superspine, spine, leaf, and exit.

Switch roles identify switch dependencies and determine the order in which switches are upgraded. The upgrade process begins with switches assigned the superspine role, then continues with the spine switches, leaf switches, exit switches, and finally, switches with no role assigned. Upgrades for all switches with a given role must be successful before the upgrade proceeds to the switches with the closest dependent role.

Role assignment is optional, but recommended. Assigning roles can prevent switches from becoming unreachable due to dependencies between switches or single attachments. Additionally, when you deploy MLAG pairs, assigned roles avoid upgrade conflicts.

### Assign Roles to Switches

{{<tabs "TabID136" >}}

{{<tab "NetQ UI" >}}

1. On the Switches card, click **Manage**.

2. Select one switch or multiple switches to assign to the same role.

3. Above the table, select {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/58-Tags-Bookmarks/tags.svg" height="18" width="18" alt="Assign Role">}} **Assign role**.

4. Select the role (superspine, leaf, spine, or exit) that applies to the selected switch(es).

5. Click **Assign**.

    Note that the **Role** column is updated with the role assigned to the selected switch(es). To return to the full list of switches, click **All**.

    {{<figure src="/images/netq/role-column-450.png" alt="table displaying role column with updated role assignments" width="700" height="300">}}

6. Continue selecting switches and assigning roles until most or all switches have roles assigned.

{{</tab>}}

{{<tab "NetQ CLI" >}}

To add a role to one or more switches, run:

```
netq lcm add role (superspine | spine | leaf | exit) switches <text-switch-hostnames>
```

For a single switch, run:

```
netq lcm add role leaf switches leaf01
```

To assign multiple switches to the same role, separate the hostnames with commas (no spaces). This example configures *leaf01* through *leaf04* switches with the leaf role:

```
netq lcm add role leaf switches leaf01,leaf02,leaf03,leaf04
```
To view all switch roles, run:

```
netq lcm show switches [version <text-cumulus-linux-version>] [json]
```
<!-- vale off -->
Use the `version` option to only show switches with a given network OS version, X.Y.Z.
<!-- vale on -->
The **Role** column displays assigned roles:

```
cumulus@switch:~$ netq lcm show switches
Hostname          Role       IP Address                MAC Address        CPU      CL Version           NetQ Version             Last Changed
----------------- ---------- ------------------------- ------------------ -------- -------------------- ------------------------ -------------------------
leaf01            leaf       192.168.200.11            44:38:39:00:01:7A  x86_64   4.1.0                3.2.0-cl4u30~1601410518. Wed Sep 30 21:55:37 2020
                                                                                                        104fb9ed
spine04           spine      192.168.200.24            44:38:39:00:01:6C  x86_64   4.1.0                3.2.0-cl4u30~1601410518. Tue Sep 29 21:25:16 2020
                                                                                                        104fb9ed
leaf03            leaf       192.168.200.13            44:38:39:00:01:84  x86_64   4.1.0                3.2.0-cl4u30~1601410518. Wed Sep 30 21:55:56 2020
                                                                                                        104fb9ed
leaf04            leaf       192.168.200.14            44:38:39:00:01:8A  x86_64   4.1.0                3.2.0-cl4u30~1601410518. Wed Sep 30 21:55:07 2020
                                                                                                        104fb9ed
border02                     192.168.200.64            44:38:39:00:01:7C  x86_64   4.1.0                3.2.0-cl4u30~1601410518. Wed Sep 30 21:56:49 2020
                                                                                                        104fb9ed
border01                     192.168.200.63            44:38:39:00:01:74  x86_64   4.1.0                3.2.0-cl4u30~1601410518. Wed Sep 30 21:56:37 2020
                                                                                                        104fb9ed
fw2                          192.168.200.62            44:38:39:00:01:8E  x86_64   4.1.0                3.2.0-cl4u30~1601410518. Tue Sep 29 21:24:58 2020
                                                                                                        104fb9ed
spine01           spine      192.168.200.21            44:38:39:00:01:82  x86_64   4.1.0                3.2.0-cl4u30~1601410518. Tue Sep 29 21:25:07 2020
                                                                                                        104fb9ed
spine02           spine      192.168.200.22            44:38:39:00:01:92  x86_64   4.1.0                3.2.0-cl4u30~1601410518. Tue Sep 29 21:25:08 2020
                                                                                                        104fb9ed
spine03           spine      192.168.200.23            44:38:39:00:01:70  x86_64   4.1.0                3.2.0-cl4u30~1601410518. Tue Sep 29 21:25:16 2020
                                                                                                        104fb9ed
fw1                          192.168.200.61            44:38:39:00:01:8C  x86_64   4.1.0                3.2.0-cl4u30~1601410518. Tue Sep 29 21:24:58 2020
                                                                                                        104fb9ed
leaf02            leaf       192.168.200.12            44:38:39:00:01:78  x86_64   4.1.0                3.2.0-cl4u30~1601410518. Wed Sep 30 21:55:53 2020
                                                                                                        104fb9ed
```
{{</tab>}}

{{</tabs>}}

### Reassign Roles to Switches

{{<tabs "TabID222" >}}

{{<tab "NetQ UI" >}}

1. On the Switches card, click **Manage**.

2. Select the switches with the incorrect role from the list.

3. Click {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/58-Tags-Bookmarks/tags.svg" height="18" width="18" alt="Assign Role">}} **Assign role**.

4. Select the correct role. To leave a switch unassigned, select **No Role**. 

5. Click **Assign**.

{{</tab>}}

{{<tab "NetQ CLI" >}}

You use the same command to both assign a role and change a role.

For a single switch, run:

```
netq lcm add role exit switches border01
```

To assign multiple switches to the same role, separate the hostnames with commas (no spaces). For example:

```
cumulus@switch:~$ netq lcm add role exit switches border01,border02
```

{{</tab>}}

{{</tabs>}}

## Host a ZTP Script with NetQ

You can host a {{<exlink url="https://docs.nvidia.com/networking-ethernet-software/cumulus-linux/Installation-Management/Zero-Touch-Provisioning-ZTP/" text="Zero Touch Provisioning (ZTP) script">}} on your NetQ VM to provision switches running Cumulus Linux. To host a ZTP script, copy the script to your NetQ server and reference the path you copied to in the `netq lcm add ztp-script` CLI command: 

```
cumulus@netq-server:~$ netq lcm add ztp-script /home/cumulus/ztp.sh
ZTP script ztp.sh uploaded successfully and can be downloaded from http://10.10.10.10/lcm/asset/ztp.sh
cumulus@netq-server:~$ 
```

The output of the command will provide the URL to use in the DHCP server option 239 configuration to instruct switches to retrieve the script. If you would like to use your NetQ VM as a DHCP server, you can use the {{<exlink url="https://kea.readthedocs.io/en/latest/arm/intro.html" text="Kea DHCP server package">}}, which is installed by default.

To list scripts that are currently added to NetQ along with their download URLs and script identification numbers, use the `netq lcm show ztp-scripts` command. You can remove ZTP scripts from NetQ with the `netq lcm del ztp-script <text-ztp-script-id>` command. 

```
cumulus@netq-server:~$ netq lcm show ztp-scripts json
[
    {
        "scriptId": "file_e96b2807bdb2c77c89334d03952097dd2224a25df68a6e91d6ab19fc9c265974",
        "scriptName": "ztp1.sh",
        "generatedDownloadUrl": http://10.10.10.10/lcm/asset/ztp.sh
    }
]

cumulus@netq-server:~$ netq lcm del ztp-script file_e96b2807bdb2c77c89334d03952097dd2224a25df68a6e91d6ab19fc9c265974
ZTP script ztp1.sh successfully deleted 
```
## Decommission a Switch with LCM

Decommissioning the switch or host removes information about the switch or host from the NetQ database. When the NetQ Agent restarts at a later date, it sends a connection request back to the database, so NetQ can monitor the switch or host again.

{{<tabs "TabID22" >}}

{{<tab "NetQ UI" >}}

1. From the LCM dashboard, navigate to the **Switch management** tab.

2. On the Switches card, select **Manage**.

3. Select the devices to decommission, then select **Decommission switch** above the table:

{{<figure src="/images/netq/decom-switch-box-450.png" alt="" width="600" height="175">}}

If you attempt to decommission a switch that is assigned a default, unmodified access profile, the process will fail. {{<link title="Credentials and Profiles" text="Create a unique access profile">}} (or update the default with unique credentials), then {{<link title="Switch Management/#attach-a-profile-to-a-switch" text="attach the profile">}} to the switch you want to decommission.

4. Confirm the devices you want to decommission.

5. Wait for the decommission process to complete, then select **Done**.

{{</tab>}}

{{<tab "NetQ CLI" >}}

To decommission a switch or host:

1. On the given switch or host, stop and disable the NetQ Agent service:

    ```
    cumulus@switch:~$ sudo systemctl stop netq-agent
    cumulus@switch:~$ sudo systemctl disable netq-agent
    ```

2. On the NetQ appliance or VM, decommission the switch or host:

    ```
    cumulus@netq-appliance:~$ netq decommission <hostname-to-decommission>
    ```
{{</tab>}}

{{</tabs>}}