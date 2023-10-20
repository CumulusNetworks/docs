---
title: Switch Management
author: NVIDIA
weight: 630
toc: 4
---

Lifecycle management displays an inventory of switches that are available for software installation or upgrade through NetQ. From the inventory list, you can assign access profiles and roles to switches, and select switches for software installation and upgrades. You can also decommission switches, which removes them from the NetQ database.

{{%notice note%}}
If you manage a switch using an in-band network interface, {{<link url="Lifecycle-Management/#lcm-support-and-in-band-management" text="additional configuration">}} is required for LCM operations.
{{%/notice%}}

## View the LCM Switch Inventory

{{<tabs "TabID13" >}}

{{<tab "NetQ UI" >}}

From the LCM dashboard, select the **Switch management** tab. The Switches card displays the number of switches that NetQ discovered and the network OS versions that are running on those switches:

{{<figure src="/images/netq/lcm-dashboard-switches-450.png" alt="switches card displaying 15 discovered switches with Cumulus Linux version 4.4.4" width="400">}}

To view a table of all discovered switches and their attributes, select **Manage** on the Switches card.

{{<notice tip>}}
If you have more than one network OS version running on your switches, you can click a version segment on the Switches card graph to open a list of switches pre-filtered by that version.
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

This list is the starting point for network OS upgrades or NetQ installations and upgrades. If the switches you want to upgrade are not present in the list, you can:

- Verify the missing switches are reachable using `ping`
- Run a {{<link title="Upgrade Cumulus Linux/#upgrade-cumulus-linux-on-switches-without-netq-agent-installed" text="switch discovery">}}, which locates all switches running Cumulus Linux in your network's fabric
- {{<link title="Install NetQ Agents" text="Install NetQ on the switch">}}
- Verify the NetQ Agent is fresh and running version 4.1.0 or later for switches that already have the agent installed (click {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/03-Menu/navigation-menu.svg" height="18" width="18" alt="Main Menu">}} **Menu**, then click **Agents** or run `netq show agents`)
- {{<link title="Upgrade NetQ Agents" text="Upgrade NetQ Agents">}} (if needed)

## Attach an Access Profile to a Switch

After creating {{<link title="Credentials and Profiles" text="access profiles">}} from your credentials, you can attach a profile to one or more switches.

{{<tabs "TabID85" >}}

{{<tab "NetQ UI" >}}

1. Expand the <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/03-Menu/navigation-menu.svg" height="18" width="18"/> **Menu** and select **Manage switches**. On the Switches card, select **Manage**.

2. The table displays a list of switches. The **Access type** column specifies whether the type of authentication is basic or SSH. The **Profile name** column displays the access profile that is assigned to the switch.

Select the switches you'd like to assign access profiles, then select {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/04-Login-Logout/login-key-1.svg" height="18" width="18">}} **Manage access profile** above the table: 

{{<figure src="/images/netq/manage-access-profile-450.png" alt="" width="500">}}

3. Select the profile from the list, then click **Done**.

If the profile you want to use isn't listed, select **Add new profile** and {{<link title="Credentials and Profiles/#create-access-profiles" text="follow the steps to create an access profile">}}.

4. Select **Ok** on the confirmation dialog. The updated access profiles are now reflected in the **Profile name** column:

{{<figure src="/images/netq/updated-access-profile-450.png" alt="" width="500">}}

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

2. The table displays a list of switches. In the profile name column, locate the access profile. Hover over the access type column and select **Manage access**:

{{<figure src="/images/netq/detach-manage-access-450.png" alt="" width="500">}}

3. To assign a different access profile to the switch, select it from the list. To detach the access profile, select <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/23-Delete/bin-1.svg" width="18" height="18"/> **Detach**.

{{<figure src="/images/netq/manage-access-profile-spine-450.png" alt="" width="500">}}

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

    {{<figure src="/images/netq/role-column-450.png" alt="table displaying role column with updated role assignments" width="700">}}

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

## Decommission a Switch with LCM

Decommissioning the switch or host removes information about the switch or host from the NetQ database. When the NetQ Agent restarts at a later date, it sends a connection request back to the database, so NetQ can monitor the switch or host again.

{{<tabs "TabID22" >}}

{{<tab "NetQ UI" >}}

1. From the LCM dashboard, navigate to the **Switch management** tab.

2. On the Switches card, select **Manage**.

3. Select the devices to decommission, then select **Decommission switch** above the table:

{{<figure src="/images/netq/decom-switch-box-450.png" alt="" width="600">}}

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