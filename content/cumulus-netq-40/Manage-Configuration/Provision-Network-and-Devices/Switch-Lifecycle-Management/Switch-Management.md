---
title: Manage Switch Inventory and Roles
author: NVIDIA
weight: 650
toc: 4
---
On initial installation, the lifecycle management feature provides an inventory of switches that have been automatically discovered by NetQ and are available for software installation or upgrade through NetQ. This includes all switches running Cumulus Linux 3.6 or later, SONiC 202012 or later, and NetQ Agent 2.4 or later in your network. You assign network roles to switches and select switches for software installation and upgrade from this inventory listing.

## View the LCM Switch Inventory

The switch inventory can be viewed from the NetQ UI and the NetQ CLI.

{{<tabs "TabID13" >}}

{{<tab "NetQ UI" >}}

A count of the switches NetQ was able to discover and the network OS versions that are running on those switches is available from the LCM dashboard.

{{<figure src="/images/netq/lcm-switches-card-with-labels-320.png" width="400">}}

To view a list of all switches known to lifecycle management, click **Manage** on the Switches card.

{{<figure src="/images/netq/lcm-switch-mgmt-list-330.png" width="700">}}

Review the list:
- Sort the list by any column; hover over column title and click to toggle between ascending and descending order
- Filter the list: click {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/15-Filter/filter-1.svg" height="18" width="18" alt="Filter Switch List">}} and enter parameter value of interest

{{<notice tip>}}
If you have more than one network OS version running on your switches, you can click a version segment on the Switches card graph to open a list of switches pre-filtered by that version.
{{</notice>}}

{{</tab>}}

{{<tab "NetQ CLI" >}}

To view a list of all switches known to lifecycle management, run:

```
netq lcm show switches [version <text-cumulus-linux-version>] [json]
```
<!-- vale off -->
Use the `version` option to only show switches with a given network OS version, X.Y.Z.
<!-- vale on -->
This example shows all switches known by lifecycle management.

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

This listing is the starting point for network OS upgrades or NetQ installations and upgrades. If the switches you want to upgrade are not present in the list, you can:

- Work with the list you have and add them later
- Verify the missing switches are reachable using `ping`
- Verify the NetQ Agent is fresh and version 2.4.0 or later for switches that already have the agent installed (click {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/03-Menu/navigation-menu.svg" height="18" width="18" alt="Main Menu">}}, then click **Agents** or run `netq show agents`)
- Install NetQ on the switch (refer to {{<link url="#use-switch-discovery-to-install-and-upgrade-netq" text="Install NetQ">}})
- Upgrade any NetQ Agents if needed (refer to {{<link title="Upgrade NetQ Agents">}} for instructions)

## Role Management

Four pre-defined switch roles are available based on the Clos architecture: Superspine, Spine, Leaf, and Exit. With this release, you cannot create your own roles.

Switch roles are used to:

- Identify switch dependencies and determine the order in which switches are upgraded
- Determine when to stop the process if a failure is encountered

When roles are assigned, the upgrade process begins with switches having the superspine role, then continues with the spine switches, leaf switches, exit switches, and finally switches with no role assigned. All switches with a given role must be successfully upgraded before the switches with the closest dependent role can be upgraded.

For example, a group of seven switches are selected for upgrade. Three are spine switches and four are leaf switches. After all the spine switches are successfully upgraded, then the leaf switches are upgraded. If one of the spine switches were to fail the upgrade, the other two spine switches are upgraded, but the upgrade process stops after that, leaving the leaf switches untouched, and the upgrade job fails.

When only some of the selected switches have roles assigned in an upgrade job, the switches with roles are upgraded first and then all the switches with no roles assigned are upgraded.

While role assignment is optional, using roles can prevent switches from becoming unreachable due to dependencies between switches or single attachments. And when MLAG pairs are deployed, switch roles avoid upgrade conflicts. For these reasons, NVIDIA highly recommends assigning roles to all your switches.

### Assign Switch Roles

Roles can be assigned to one or more switches using the NetQ UI or the NetQ CLI.

{{<tabs "TabID99" >}}

{{<tab "NetQ UI" >}}

1. Open the LCM dashboard.

2. On the Switches card, click **Manage**.

3. Select one switch or multiple switches that should be assigned to the same role.

4. Click {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/58-Tags-Bookmarks/tags.svg" height="18" width="18" alt="Assign Role">}}.

5. Select the role that applies to the selected switch(es).

    {{<figure src="/images/netq/lcm-role-assign-role-selection-320.png" width="300">}}

6. Click **Assign**.

    Note that the **Role** column is updated with the role assigned to the selected switch(es). To return to the full list of switches, click **All**.

    {{<figure src="/images/netq/lcm-switches-listing-role-assigned-320.png" width="700">}}

7. Continue selecting switches and assigning roles until most or all switches have roles assigned.

A bonus of assigning roles to switches is that you can then filter the list of switches by their roles by clicking the appropriate tab.

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

For multiple switches to be assigned the same role, separate the hostnames with commas (no spaces). This example configures *leaf01* through *leaf04* switches with the leaf role:

```
netq lcm add role leaf switches leaf01,leaf02,leaf03,leaf04
```

{{</tab>}}

{{</tabs>}}

### View Switch Roles

You can view the roles assigned to the switches in the LCM inventory at any time.

{{<tabs "TabID151" >}}

{{<tab "NetQ UI" >}}

1. Open the LCM dashboard.

2. On the Switches card, click **Manage**.

    The assigned role is displayed in the **Role** column of the listing.

    {{<figure src="/images/netq/lcm-switch-mgmt-list-300.png" width="700">}}

{{</tab>}}

{{<tab "NetQ CLI" >}}

To view all switch roles, run:

```
netq lcm show switches [version <text-cumulus-linux-version>] [json]
```
<!-- vale off -->
Use the `version` option to only show switches with a given network OS version, X.Y.Z.
<!-- vale on -->
This example shows the role of all switches in the **Role** column of the listing.

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

### Change the Role of a Switch

If you accidentally assign an incorrect role to a switch, it can easily be changed to the correct role.

To change a switch role:

{{<tabs "TabID179" >}}

{{<tab "NetQ UI" >}}

1. Open the LCM dashboard.

2. On the Switches card, click **Manage**.

3. Select the switches with the incorrect role from the list.

4. Click {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/58-Tags-Bookmarks/tags.svg" height="18" width="18" alt="Assign Role">}}.

5. Select the correct role. (Note that you can select **No Role** here as well to remove the role from the switches.)

6. Click **Assign**.

{{</tab>}}

{{<tab "NetQ CLI" >}}

You use the same command to assign a role as you use to change the role.

For a single switch, run:

```
netq lcm add role exit switches border01
```

For multiple switches to be assigned the same role, separate the hostnames with commas (no spaces). For example:

```
cumulus@switch:~$ netq lcm add role exit switches border01,border02
```

{{</tab>}}

{{</tabs>}}

## Export List of Switches

Using the Switch Management feature you can export a listing of all or a selected set of switches.

To export the switch listing:

{{<tabs "TabID223" >}}

{{<tab "NetQ UI" >}}

1. Open the LCM dashboard.

2. On the Switches card, click **Manage**.

3. Select one or more switches, filtering as needed, or select all switches (click <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/check-circle-1.svg" height="18" width="18"/>).

4. Click <img src="https://icons.cumulusnetworks.com/05-Internet-Networks-Servers/08-Upload-Download/upload-bottom.svg" height="18" width="18"/>.

5. Choose the export file type and click **Export**.

    {{<figure src="/images/netq/export-data-dialog-300.png" width="250">}}

{{</tab>}}

{{<tab "NetQ CLI" >}}

Use the `json` option with the `netq lcm show switches` command to output a list of all switches in the LCM repository. Alternately, output only switches running a particular network OS version by including the `version` option.

```
cumulus@switch:~$ netq lcm show switches json

cumulus@switch:~$ netq lcm show switches version 3.7.11 json
```

{{</tab>}}

{{</tabs>}}
