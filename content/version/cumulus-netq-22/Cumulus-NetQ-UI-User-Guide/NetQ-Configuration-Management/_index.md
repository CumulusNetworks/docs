---
title: NetQ Management
author: Cumulus Networks
weight: 91
pageID: 12321950
product: Cumulus NetQ
version: 2.2
imgData: cumulus-netq-22
siteSlug: cumulus-netq-22
---
As an administrator, you can manage access to and various
application-wide settings for the Cumulus NetQ UI from a single location.

Individual users have the ability to set preferences specific to their
workspaces. This information is covered separately. Refer to
[Set User Preferences](../NetQ-User-Interface-Overview/Set-User-Preferences).

## NetQ Management Workbench

The NetQ Management workbench is accessed from the main menu. For the user(s) responsible for maintaining the application, this is a good place to start each day.

To open the workbench, click <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/03-Menu/navigation-menu.svg", height="18", width="18"/>, and select **Management** under the **Admin** column.

{{<figure src="https://dkahegywkrw3e.cloudfront.net/images/netq/netq-mgmt-wb-222.png" width="700">}}

## Manage User Accounts

From the NetQ Management workbench, you can view the number of users
with accounts in the system. As an administrator, you can also add,
modify, and delete user accounts using the User Accounts card.

### Add New User Account

For each user that monitors at least one aspect of your data center
network, a user account is needed.

To add a new user account:

1.  Click **Manage** on the User Accounts card, to open the **User Accounts** tab.
2.  Click **Add User**.

    {{< figure src="https://dkahegywkrw3e.cloudfront.net/images/netq/add-new-user-modal-221.png" width="250" >}}

3.  Enter the user's email address, along with their first and last
    name.

    {{%notice note%}}

Be especially careful entering the email address as you *cannot*
    change it once you save the account. If you save a mistyped email
    address, you must delete the account and create a new one.

    {{%/notice%}}

4.  Select the user type: *Admin* or *User*.
5.  Enter your password in the **Admin Password** field (only users with
    administrative permissions can add users).

6.  Create a password for the user.

    1.  Enter a password for the user.
    2.  Re-enter the user password. If you do not enter a matching
        password, it will be underlined in red.

7.  Click **Save** to create the user account, or **Cancel** to discard
    the user account.  

    {{<figure src="https://dkahegywkrw3e.cloudfront.net/images/netq/netq-mgmt-user-accts-tab-222.png" width="700">}}

    By default the User Accounts table is sorted by *Role*. Change
    the sort by clicking in any of the headers, then click <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/35-Text-Options/arrange-letter.svg", height="18", width="18"/>.  

8.  Repeat these steps to add all of your users.

### Edit a User Name

If a user's first or last name was incorrectly entered, you can fix them
easily.

To change a user name:

1.  Click **Manage** on the User Accounts card to open the **User Accounts** tab.
2.  Select the account you want to change by clicking the checkbox next to it.
3.  In the Edit menu that appears at the bottom of the window, click <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/22-Edit/pencil-1.svg", height="18", width="18"/>.
4.  Modify the first and/or last name as needed.
5.  Enter your admin password.

    {{< figure src="https://dkahegywkrw3e.cloudfront.net/images/netq/edit-user-modal-221.png" width="250" >}}

6.  Click **Save** to commit the changes or **Cancel** to discard them.

### Change a User's Password

Should a user forget his password or for security reasons, you can
change a password for a particular user account.

To change a password:

1.  Click **Manage** on the User Accounts card to open the **User Accounts** tab.
2.  Select the account you want to change by clicking the checkbox next to it.
3.  In the Edit menu that appears at the bottom of the window, click click <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/22-Edit/pencil-1.svg", height="18", width="18"/>.
4.  Click **Reset Password**.
5.  Enter your admin password.

    {{< figure src="https://dkahegywkrw3e.cloudfront.net/images/netq/change-user-password-221.png" width="250" >}}

6.  Enter a new password for the user.
7.  Re-enter the user password.

      {{%notice tip%}}
If the password you enter does not match, **Save** is not activated, and you cannot save the change.
      {{%/notice%}}

8.  Click **Save** to commit the change, or **Cancel** to discard the
    change.

### Change a User's Access Permissions

If a particular user has only standard user permissions and they need
administrator permissions to perform their job (or the opposite, they
have administrator permissions, but only need user permissions), you can
modify their access rights.

To change access permissions:

1.  Click **Manage** on the User Accounts card to open the **User Accounts** tab.
2.  Select the account you want to change by clicking the checkbox next to it.
3.  In the Edit menu that appears at the bottom of the window, click <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/22-Edit/pencil-1.svg", height="18", width="18"/>.
4.  Enter your admin password.
5.  Select the appropriate user type from the dropdown list.

    {{< figure src="https://dkahegywkrw3e.cloudfront.net/images/netq/change-user-permissions-221.png" width="250" >}}

6.  Click **Save** to commit the change, or **Cancel** to discard the
    change.

### Correct a Mistyped User ID (Email Address)

You cannot edit a user's email address, because this is the identifier
the system uses for authentication. If you need to change an email
address, you must create a new one for this user. Refer to [Add a New User Account](#add-new-user-account). You should delete the incorrect user account. Select the user account, and click **Delete** in the Edit menu.

### Export a List of User Accounts

You can export user account information at any time using the User
Accounts tab.

To export information for one or more user accounts:

1.  Click **Manage** on the User Accounts card to open the **User Accounts** tab.
2.  Select one or more accounts that you want to export by clicking the checkbox next to them.
3.  To export all user accounts, click **Select All** in the Edit menu and then click  **Export Selected**.

    {{<figure src="https://dkahegywkrw3e.cloudfront.net/images/netq/user-acct-edit-menu-export-222.png" width="600">}}

4.  To export specific user accounts, select only those accounts you
    want to export, and click **Export Selected** in the Edit menu.

### Delete a User Account

NetQ application administrators should remove user accounts associated with users that are no longer using the application.

To delete one or more user accounts:

1.  Click **Manage** on the User Accounts card to open the **User Accounts** tab.
2.  Select one or more accounts that you want to remove by clicking the checkbox next to them.
3.  Click <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/23-Delete/bin-1.svg", height="18", width="18"/> in the Edit menu to remove the accounts.

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

1.  Click **Manage** on the Scheduled Traces card to open the **Scheduled Traces** tab.
2.  Click **Add Trace** to open the large New Trace Request card.

    {{<figure src="https://dkahegywkrw3e.cloudfront.net/images/netq/trace-request-large-222.png" width="500">}}

3.  Enter source and destination addresses.

    {{%notice note%}}

For layer 2 traces, the source must be a hostname and the
    destination must be a MAC address. For layer 3 traces, the source
    can be a hostname or IP address, and the destination must be an IP
    address.

    {{%/notice%}}

4.  Specify a VLAN for a layer 2 trace or (optionally) a VRF for a layer
    3 trace.
5.  Set the schedule for the trace, by selecting how often to run the
    trace and when to start it the first time.
6.  Click **Save As New** to add the trace. You are prompted to enter a
    name for the trace in the **Name** field.  

    If you want to run the new trace right away for a baseline, select
    the trace you just added from the dropdown list, and click **Run
    Now**.

### Delete a Scheduled Trace

If you do not want to run a given scheduled trace any longer, you can remove it.

To delete a scheduled trace:

1.  Click **Manage** on the Scheduled Trace card to open the **Scheduled Traces** tab.
2.  Hover over and select at least one trace.
3.  Click <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/23-Delete/bin-1.svg", height="16", width="16"/>.

### Export a Scheduled Trace

You can export a scheduled trace configuration at any time using the
Scheduled Traces tab.

To export one or more scheduled trace configurations:

1.  Click **Manage** on the Scheduled Trace card to open the **Scheduled Traces** tab.
2.  Hover over and select at least one trace.
3.  To export all traces, click **Select All** and then **Export
    Selected**.

    {{% imgOld 13 %}}

4.  To export specific traces, select only those traces you want to
    export, and click **Export Selected**.

## Manage Scheduled Validations

From the NetQ Management workbench, you can view the total number of
validations scheduled to run in the system. A set of default scheduled
validations are provided and preconfigured with the NetQ UI. These are not included in the total count. As an administrator, you can view and export the configurations for all
scheduled validations, or add a new validation.

### View Scheduled Validation Configurations

You can view the configuration of a scheduled validation at any time.
This can be useful when you are trying to determine if the validation
request needs to be modified to produce a slightly different set of
results (editing or cloning) or if it would be best to create a new one.

To view the configurations:

1.  Click **Manage** on the Scheduled Validations card to open the **Scheduled Validations** tab.
2.  Click <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/close.svg", height="14", width="14"/> in the top right to return to your NetQ Management cards.

### Add a Scheduled Validation

You can add a scheduled validation at any time using the Scheduled
Validations tab.

To add a scheduled validation:

1.  Click **Manage** on the Scheduled Validations card.
2.  Click the **Scheduled Validations** tab.
3.  Click **Add Validation** to open the large Validation Request card.

    {{<figure src="https://dkahegywkrw3e.cloudfront.net/images/netq/valid-request-large-222.png" width="500">}}

4.  Configure the request. Refer to [Validate Network Protocol and Service Operations](../Monitor-Network-Performance/Validate-Network-Protocol-and-Service-Operations/) for details.

### Export Scheduled Validation Configurations

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

## View System Server Information

From the NetQ Management workbench, you can view information about the NetQ hardware server (your own or one of the Cumulus NetQ Appliances).

Locate the System Server Info card on the workbench. You may need to scroll down.

{{<figure src="https://dkahegywkrw3e.cloudfront.net/images/netq/netq-mgmt-sys-server-info-222.png" width="500">}}

The following data is available on this card:

| Parameter | Description |
| --------- | ----------- |
| Application Serial Number | Identifier of the Cumulus NetQ instance running on this server |
| Appliance Version | Version of the hardware; a VX value indicates a virtual server |
| CPU Core | Number of CPU cores on this server |
| IP | IP address associated with this server |
| Memory | Size of the RAM on this server |
| NetQ Version | Version of the Cumulus NetQ software running on this server |
| OS Version | Version of the operating system running on this server |
| Timestamp | Date and time this information was collected from the server |
