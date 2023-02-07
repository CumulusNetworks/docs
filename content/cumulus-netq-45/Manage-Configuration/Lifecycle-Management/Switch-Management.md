---
title: Switch Management
author: NVIDIA
weight: 650
toc: 4
---

Upon installation, lifecycle management displays an inventory of switches that are available for software installation or upgrade through NetQ. This includes all switches running Cumulus Linux 3.7.12 or later, SONiC 202012 and 202106, and NetQ Agent 4.1.0 or later in your network. From this list, you can assign access profiles and roles to switches, and select switches for software installation and upgrades.

## View the LCM Switch Inventory

{{<tabs "TabID13" >}}

{{<tab "NetQ UI" >}}

From the LCM dashboard, select the **Switch management** tab. The Switches card displays the number of switches that NetQ discovered and the network OS versions that are running on those switches:

{{<figure src="/images/netq/lcm-dashboard-switches-450.png" alt="switches card displaying 14 discovered switches with Cumulus Linux version 4.4.4" width="400">}}

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
Use the `version` options to display switches with a given OS version, X.Y.Z.

For additional details, refer to the {{<link title="lcm/#netq-lcm-show-switches" text="command line reference">}}.

{{</tab>}}

{{</tabs>}}

This list is the starting point for network OS upgrades or NetQ installations and upgrades. If the switches you want to upgrade are not present in the list, you can:

- Verify the missing switches are reachable using `ping`
- Verify the NetQ Agent is fresh and version 4.1.0 or later for switches that already have the agent installed (click {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/03-Menu/navigation-menu.svg" height="18" width="18" alt="Main Menu">}} Menu, then click **Agents** or run `netq show agents`)
- {{<link title="Install NetQ Agents" text="Install NetQ on the switch">}}
- {{<link title="Upgrade NetQ Agents" text="Upgrade NetQ Agents">}} (if needed)

## Assign a Profile to a Switch

After creating {{<link title="Credentials and Profiles" text="access profiles">}} from your credentials, you can assign profiles to individual switches.

{{<tabs "TabID85" >}}

{{<tab "NetQ UI" >}}

1. On the Switches card, select **Manage**.

2. The table displays a list of switches. The **Access type** column specifies whether the type of authentication is basic or SSH. The **Profile name** column displays the access profile that is assigned to the switch.

Select the switches you'd like to assign access profiles, then select {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/04-Login-Logout/login-key-1.svg" height="18" width="18">}} **Manage access profile** above the table: 

{{<figure src="/images/netq/manage-access-profile-450.png" alt="" width="500">}}

3. Select the profile from the list, then click **Done**.

If the profile you'd like to use isn't listed, select **Add new profile** and {{<link title="Credentials and Profiles/#create-access-profiles" text="follow the steps to create an access profile">}}.

4. Select **Ok** on the confirmation dialog. The updated access profiles are now reflected in the **Profile name** column:

{{<figure src="/images/netq/updated-access-profile-450.png" alt="" width="500">}}

{{</tab>}}

{{<tab "NetQ CLI" >}}

{{</tab>}}

{{</tabs>}}

## Role Management

You can assign switches one of four roles: superspine, spine, leaf, and exit.

Switch roles identify switch dependencies and determine the order in which switches are upgraded. The upgrade process begins with switches assigned the superspine role, then continues with the spine switches, leaf switches, exit switches, and finally, switches with no role assigned. Upgrades for all switches with a given role must be successful before the upgrade process for switches with the closest dependent role can begin.

Role assignment is optional, but recommended. Using roles can prevent switches from becoming unreachable due to dependencies between switches or single attachments. Additionally, when you deploy MLAG pairs, assigned roles avoid upgrade conflicts.

### Assign Roles to Switches

{{<tabs "TabID99" >}}

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

{{<tabs "TabID179" >}}

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