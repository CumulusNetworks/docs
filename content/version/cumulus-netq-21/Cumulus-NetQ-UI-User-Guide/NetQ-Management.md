---
title: NetQ Management
author: Cumulus Networks
weight: 57
aliases:
 - /display/NETQ21/NetQ+Management
 - /pages/viewpage.action?pageId=10465518
pageID: 10465518
product: Cumulus NetQ
version: '2.1'
imgData: cumulus-netq-21
siteSlug: cumulus-netq-21
---
As an administrator, you can manage access to and various
application-wide settings for the NetQ UI as well as view information
about the system server, all from a single workbench.

Individual users have the ability to set preferences specific to their
workspaces. This information is covered separately. Refer to [User Settings](/version/cumulus-netq-21/Cumulus-NetQ-UI-User-Guide/NetQ-User-Interface-Overview/User-Settings).

## NetQ Management Workbench

The NetQ Management workbench is accessed from the main menu and from
the header of an open workbench. For the user or users responsible for
maintaining the application, this is a good place to start each day.

To open the workbench, click {{% imgOld 0 %}},  and select **Management** under the **Admin** column.

{{% imgOld 1 %}}

## Manage User Accounts

From the NetQ Management workbench, you can view the number of users
with accounts in the system. As an administrator, you can also add,
modify, and delete user accounts using the User Account card.

### Add New User Account

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
change it once you save the account.
    
    {{%/notice%}}

5.  Enter your password in the Admin Password field (only users with
    administrative permissions can add users).

6.  Create a password for the user.
    
    1.  Enter a password for the user.
    
    2.  Re-enter the user password. If you do not enter a matching
        password, it will be underlined in red.

7.  Click **Save** to create the user account, or **Cancel** to discard
    the user account.  
    By default the User Accounts table is sorted by *User ID*. Change
    the sort by clicking in any of the headers.  
    
    {{% imgOld 3 %}}
    
    {{%notice info%}}
    
There is only the *admin* role at this time. Any user account you
create will have administrator permissions.
    
    {{%/notice%}}

8.  Repeat these steps to add all of your users.

### Correct a Mis-spelled Name

If you have mistyped a user's first or last name, you can modify it from
the User Accounts tab.

To edit the name on a user account:

1.  Click **Manage** on the User Accounts card.

2.  Click the **User Accounts** tab.

3.  Hover over the account you want to change, and click the checkbox
    next to it.

4.  In the Edit menu that appears at the bottom of the window, click <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/22-Edit/pencil-2.svg", height="18", width="18"/>.

5.  Modify the first and/or last name as needed.

6.  Enter your admin password.
    
    {{% imgOld 5 %}}

7.  Click **Save** to commit the changes or **Cancel** to discard them.

### Change a User's Password

Should a user forget his password or for security reasons, you can
change a password for a particular user account.

To change a password:

1.  Click **Manage** on the User Accounts card.

2.  Click the **User Accounts** tab.

3.  Hover over the account you want to change, and click the checkbox
    next to it.

4.  In the Edit menu that appears at the bottom of the window, click <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/22-Edit/pencil-2.svg", height="18", width="18"/>.

5.  Enter your admin password.

6.  Click **Reset** **Password**.
    
    {{% imgOld 7 %}}

7.  Enter a new password for the user.

8.  Re-enter the user password. If the password you enter does not
    match, a red line appears underneath it.

9.  Click **Save** to commit the change, or **Cancel** to discard the
    change.

### Correct a Mis-typed User ID (Email Address)

You cannot edit a user's email address, because this is the identifier
the system uses for authentication. If you need to change an email
address, you must create a new one for this user. Refer to [Add New
User Account](#add-new-user-account). The old account
remains.

### Export a List of User Accounts

You can export user account information at any time using the User
Accounts tab.

To export information for one or more user accounts:

1.  Click **Manage** on the User Accounts card.

2.  Click the **User Accounts** tab.

3.  Hover over and select at least one user account.

4.  To export all user accounts, click **Select All** and then **Export
    Selected**.

5.  To export specific user accounts, select only those accounts you
    want to export, and click **Export Selected**.

## Manage Scheduled Traces

From the NetQ Management workbench, you can view the number of traces
scheduled to run in the system. A set of default traces are provided
with the NetQ GUI. As an administrator, you can run one or more
scheduled traces, add new scheduled traces, and edit or delete existing
traces.

### Add a Scheduled Trace

You can create a scheduled trace to provide regular status about a
particularly important connection between a pair of devices in your
network or for temporary troubleshooting.

To add a trace:

1.  Click **Manage** on the Scheduled Traces card.

2.  Click the **Scheduled Traces** tab.

3.  Click **Add Trace** to open the large New Trace Request card.
    
    {{% imgOld 8 %}}

4.  Enter source and destination addresses.
    
    {{%notice info%}}
    
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
    If you want to run the new trace right away for a baseline, open the
    small Trace Request card. Select the trace you just added, and click
    **GO**.

### Export a Scheduled Trace

You can export a scheduled trace configuration at any time using the
Scheduled Traces tab.

To export one or more scheduled trace configurations:

1.  Click **Manage** on the Scheduled Trace card.

2.  Click the **Scheduled Traces** tab.

3.  Hover over and select at least one trace.

4.  To export all validations, click **Select All** and then **Export
    Selected**.

5.  To export specific traces, select only those traces you want to
    export, and click **Export Selected**.

## Manage Scheduled Validations

From the NetQ Management workbench, you can view the total number of
validations scheduled to run in the system. A set of default scheduled
validations are provided and pre-configured with the NetQ UI. As an
administrator, you can view and export the configurations for all
scheduled validations, or add a new validation.

### View Scheduled Validation Configurations

You can view the configuration of a scheduled validation at any time.
This can be useful when you are trying to determine if the validation
request needs to be modified to produce a slightly different set of
results (editing or cloning) or if it would be best to create a new one.

To view the configurations:

1.  Click **Manage** on the Scheduled Validations card.

2.  Click the **Scheduled Validations** tab.

3.  Click <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/close.svg", height="18", width="18"/> in the top right to return to your NetQ Management cards.

### Export Scheduled Validation Configurations

You can export one or more scheduled validation configurations at any
time using the Scheduled Validations tab.

To export a scheduled validation:

1.  Click **Manage** on the Scheduled Validations card.

2.  Click the **Scheduled Validations** tab.

3.  Hover over and select at least one validation.

4.  To export all validations, click **Select All** and then **Export
    Selected**.

5.  To export specific validations, select only those validations you
    want to export, and click **Export Selected**.

### Add a Scheduled Validation

You can add a scheduled validation at any time using the Scheduled
Validations tab.

To add a scheduled validation:

1.  Click **Manage** on the Scheduled Validations card.

2.  Click the **Scheduled Validations** tab.

3.  Click **Add Validation**.  
    This opens the large Validation Request card.

4.  Configure the request. Refer to [Validate Network Protocol and
    Service Operations](../Monitor-the-Network/Validate-Network-Protocol-and-Service-Operations)
    for details.
