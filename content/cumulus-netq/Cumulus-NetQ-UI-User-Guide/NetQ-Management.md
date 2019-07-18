---
title: NetQ Management
author: Cumulus Networks
weight: 91
aliases:
 - /display/NETQ22/NetQ-Management
 - /pages/viewpage.action?pageId=12321950
pageID: 12321950
product: Cumulus NetQ
version: 2.2.0
imgData: cumulus-netq-22
siteSlug: cumulus-netq-22
---
As an administrator, you can manage access to and various
application-wide settings for the NetQ UI from a single location.

Individual users have the ability to set preferences specific to their
workspaces. This information is covered separately. Refer to
[User Settings](/cumulus-netq/Cumulus-NetQ-UI-User-Guide/NetQ-User-Interface-Overview).

## <span>NetQ Management Workbench</span>

The NetQ Management workbench is accessed from the main menu and from
the header of an open workbench. For the user or users responsible for
maintaining the application, this is a good place to start each day.

To open the workbench, click {{% imgOld 0 %}}, and select **Management** under the **Admin** column.

{{% imgOld 1 %}}

## <span>Manage User Accounts</span>

From the NetQ Management workbench, you can view the number of users
with accounts in the system. As an administrator, you can also add,
modify, and delete user accounts using the User Accounts card.

### <span id="src-12321950_safe-id-TmV0UU1hbmFnZW1lbnQtI0FkZFVzckFjdA" class="confluence-anchor-link"></span><span>Add New User Account</span>

For each user that monitors at least one aspect of your data center
network, a user account is needed.

To add a new user account:

1.  Click **Manage** on the User Accounts card.
2.  Click the **User Accounts** tab.
3.  Click **Add User**.

    {{% imgOld 2 %}}

4.  Enter the user's email address, along with their first and last
    name.

    {{%notice note%}}

Be especially careful entering the email address as you *cannot*
    change it once you save the account. If you save a mistyped email
    address, you must delete the account and create a new one.

    {{%/notice%}}

5.  Select the user type: *Admin* or *User*.
6.  Enter your password in the **Admin Password** field (only users with
    administrative permissions can add users).

7.  Create a password for the user.

    1.  Enter a password for the user.
    2.  Re-enter the user password. If you do not enter a matching
        password, it will be underlined in red.

8.  Click **Save** to create the user account, or **Cancel** to discard
    the user account.  

    By default the User Accounts table is sorted by *User ID*. Change
    the sort by clicking in any of the headers.  

    {{% imgOld 3 %}}

    {{%notice note%}}

There is only the *admin* role at this time. Any user account you
    create will have administrator permissions.

    {{%/notice%}}

9.  Repeat these steps to add all of your users.

### <span>Edit a User Name</span>

If a user's first or last name was incorrectly entered, you can fix them
easily.

To change a user name:

1.  Click **Manage** on the User Accounts card.
2.  Click the **User Accounts** tab.
3.  Hover over the account you want to change, and click the checkbox
    next to it.
4.  In the Edit menu that appears at the bottom of the window, click {{% imgOld 5 %}}.
5.  Modify the first and/or last name as needed.
6.  Enter your admin password.

    {{% imgOld 6 %}}

7.  Click **Save** to commit the changes or **Cancel** to discard them.

### <span>Change a User's Password</span>

Should a user forget his password or for security reasons, you can
change a password for a particular user account.

To change a password:

1.  Click **Manage** on the User Accounts card.
2.  Click the **User Accounts** tab.
3.  Hover over the account you want to change, and click the checkbox
    next to it.
4.  In the Edit menu that appears at the bottom of the window, click {{% imgOld 7 %}}.
5.  Click **Reset Password**.
6.  Enter your admin password.

    {{% imgOld 8 %}}

7.  Enter a new password for the user.
8.  Re-enter the user password. If the password you enter does not
    match, the Save is gray (not activated).
9.  Click **Save** to commit the change, or **Cancel** to discard the
    change.

### <span>Change a User's Access Permissions</span>

If a particular user has only standard user permissions and they need
administrator permissions to perform their job (or the opposite, they
have administrator permissions, but only need user permissions), you can
modify their access rights.

To change access permissions:

1.  Click **Manage** on the User Accounts card.
2.  Click the **User Accounts** tab.
3.  Hover over the account you want to change, and click the checkbox
    next to it.
4.  In the Edit menu that appears at the bottom of the window, click {{% imgOld 9 %}}.
5.  Select the appropriate user type from the dropdown list.

    {{% imgOld 10 %}}

6.  Enter your admin password.
7.  Click **Save** to commit the change, or **Cancel** to discard the
    change.

### <span>Correct a Mistyped User ID (Email Address)</span>

You cannot edit a user's email address, because this is the identifier
the system uses for authentication. If you need to change an email
address, you must create a new one for this user. Refer to [Add a New
User Account](#src-12321950_NetQManagement-AddUsrAct). You should delete
the incorrect user account. Select the user account, and click
**Delete** in the Edit menu.

### <span>Export a List of User Accounts</span>

You can export user account information at any time using the User
Accounts tab.

To export information for one or more user accounts:

1.  Click **Manage** on the User Accounts card.
2.  Click the **User Accounts** tab.
3.  Hover over and select at least one user account.
4.  To export all user accounts, click **Select All** and then **Export
    Selected**.

    {{% imgOld 11 %}}

5.  To export specific user accounts, select only those accounts you
    want to export, and click **Export Selected**.

## <span>Manage Scheduled Traces</span>

From the NetQ Management workbench, you can view the number of traces
scheduled to run in the system. A set of default traces are provided
with the NetQ GUI. As an administrator, you can run one or more
scheduled traces, add new scheduled traces, and edit or delete existing
traces.

### <span>Add a Scheduled Trace</span>

You can create a scheduled trace to provide regular status about a
particularly important connection between a pair of devices in your
network or for temporary troubleshooting.

To add a trace:

1.  Click **Manage** on the Scheduled Traces card.
2.  Click the **Scheduled Traces** tab.
3.  Click **Add Trace** to open the large New Trace Request card.

    {{% imgOld 12 %}}

4.  Enter source and destination addresses.

    {{%notice note%}}

For layer 2 traces, the source must be a hostname and the
    destination must be a MAC address. For layer 3 traces, the source
    can be a hostname or IP address, and the destination must be an IP
    address.

    {{%/notice%}}

5.  Specify a VLAN for a layer 2 trace or (optionally) a VRF for a layer
    3 trace.
6.  Set the schedule for the trace, by selecting how often to run the
    trace and when to start it the first time.
7.  Click **Save As New** to add the trace. You are prompted to enter a
    name for the trace in the **Name** field.  

    If you want to run the new trace right away for a baseline, select
    the trace you just added from the dropdown list, and click **Run
    Now**.

### <span>Export a Scheduled Trace</span>

You can export a scheduled trace configuration at any time using the
Scheduled Traces tab.

To export one or more scheduled trace configurations:

1.  Click **Manage** on the Scheduled Trace card.
2.  Click the **Scheduled Traces** tab.
3.  Hover over and select at least one trace.
4.  To export all validations, click **Select All** and then **Export
    Selected**.

    {{% imgOld 13 %}}

5.  To export specific traces, select only those traces you want to
    export, and click **Export Selected**.

## <span>Manage Scheduled Validations</span>

From the NetQ Management workbench, you can view the total number of
validations scheduled to run in the system. A set of default scheduled
validations are provided and preconfigured with the NetQ UI. As an
administrator, you can view and export the configurations for all
scheduled validations, or add a new validation.

### <span>View Scheduled Validation Configurations</span>

You can view the configuration of a scheduled validation at any time.
This can be useful when you are trying to determine if the validation
request needs to be modified to produce a slightly different set of
results (editing or cloning) or if it would be best to create a new one.

To view the configurations:

1.  Click **Manage** on the Scheduled Validations card.
2.  Click the **Scheduled Validations** tab.
3.  Click {{% imgOld 14 %}} in the top right to return to your NetQ Management cards.

### <span>Export Scheduled Validation Configurations</span>

You can export one or more scheduled validation configurations at any
time using the Scheduled Validations tab.

To export a scheduled validation:

1.  Click **Manage** on the Scheduled Validations card.
2.  Click the **Scheduled Validations** tab.
3.  Hover over and select at least one validation.
4.  To export all validations, click **Select All** and then **Export
    Selected**.

    {{% imgOld 15 %}}

5.  To export specific validations, select only those validations you
    want to export, and click **Export Selected**.

### <span>Add a Scheduled Validation</span>

You can add a scheduled validation at any time using the Scheduled
Validations tab.

To add a scheduled validation:

1.  Click **Manage** on the Scheduled Validations card.
2.  Click the **Scheduled Validations** tab.
3.  Click **Add Validation** to open the large Validation Request card.

    {{% imgOld 16 %}}

4.  Configure the request. Refer to [Validate Network Protocol and Service Operations](/cumulus-netq/Cumulus-NetQ-UI-User-Guide/Monitor-the-Network/Validate-Network-Protocol-and-Service-Operations) for details.

<article id="html-search-results" class="ht-content" style="display: none;">

</article>

<footer id="ht-footer">

</footer>
