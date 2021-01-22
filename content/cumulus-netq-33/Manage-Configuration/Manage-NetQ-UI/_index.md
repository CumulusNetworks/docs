---
title: Manage the NetQ UI
author: NVIDIA
weight: 600
toc: 2
---
As an administrator, you can manage access to and various application-wide settings for the NetQ UI from a single location.

Individual users have the ability to set preferences specific to their workspaces. This information is covered separately. Refer to {{<link title="Set User Preferences">}}.

## NetQ Management Workbench

The NetQ Management workbench is accessed from the main menu. For the user(s) responsible for maintaining the application, this is a good place to start each day.

To open the workbench, click <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/03-Menu/navigation-menu.svg" height="18" width="18"/>, and select *Management* under the **Admin** column.

{{<figure src="/images/netq/netq-mgmt-wb-onprem-300.png" width="700">}}

{{<notice note>}}
For cloud deployments, the LDAP Server Info card is not available. Refer to {{<link url="Integrate-NetQ-with-Your-LDAP-Server" text="Integrate NetQ with Your LDAP server">}} for details.
{{</notice>}}

## Manage User Accounts

From the NetQ Management workbench, you can view the number of users with accounts in the system. As an administrator, you can also add, modify, and delete user accounts using the User Accounts card.

### Add New User Account

For each user that monitors at least one aspect of your data center
network, a user account is needed. Adding a local user is described here. Refer to {{<link url="Integrate-NetQ-with-Your-LDAP-Server" text="Integrate NetQ with Your LDAP server">}} for instructions for adding LDAP users.

To add a new user account:

1. Click **Manage** on the User Accounts card to open the **User Accounts** tab.

2. Click **Add User**.

    {{< figure src="/images/netq/add-new-user-modal-221.png" width="250" >}}

3. Enter the user's email address, along with their first and last name.

    {{%notice note%}}
Be especially careful entering the email address as you *cannot* change it once you save the account. If you save a mistyped email address, you must delete the account and create a new one.
    {{%/notice%}}

4. Select the user type: *Admin* or *User*.

5. Enter your password in the **Admin Password** field (only users with administrative permissions can add users).

6. Create a password for the user.

    1. Enter a password for the user.
    2. Re-enter the user password. If you do not enter a matching password, it will be underlined in red.

7. Click **Save** to create the user account, or **Cancel** to discard the user account.

    {{<figure src="/images/netq/netq-mgmt-user-accts-tab-241.png" width="700">}}

    By default the User Accounts table is sorted by *Role*.

8. Repeat these steps to add all of your users.

### Edit a User Name

If a user's first or last name was incorrectly entered, you can fix them easily.

To change a user name:

1. Click **Manage** on the User Accounts card to open the **User Accounts** tab.

2. Click the checkbox next to the account you want to edit.

3. Click <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/22-Edit/pencil-1.svg" height="18" width="18"/> above the account list.

4. Modify the first and/or last name as needed.

5. Enter your admin password.

    {{< figure src="/images/netq/edit-user-modal-221.png" width="250" >}}

6. Click **Save** to commit the changes or **Cancel** to discard them.

### Change a User's Password

Should a user forget his password or for security reasons, you can change a password for a particular user account.

To change a password:

1. Click **Manage** on the User Accounts card to open the **User Accounts** tab.

2. Click the checkbox next to the account you want to edit.

3. Click <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/22-Edit/pencil-1.svg" height="18" width="18"/> above the account list.

4. Click **Reset Password**.

5. Enter your admin password.

    {{< figure src="/images/netq/change-user-password-221.png" width="250" >}}

6. Enter a new password for the user.

7. Re-enter the user password. *Tip: If the password you enter does not match, Save is gray (not activated).*

8. Click **Save** to commit the change, or **Cancel** to discard the change.

### Change a User's Access Permissions

If a particular user has only standard user permissions and they need administrator permissions to perform their job (or the opposite, they have administrator permissions, but only need user permissions), you can modify their access rights.

To change access permissions:

1. Click **Manage** on the User Accounts card to open the **User Accounts** tab.

2. Click the checkbox next to the account you want to edit.

3. Click <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/22-Edit/pencil-1.svg" height="18" width="18"/> above the account list.

4. Select the appropriate user type from the dropdown list.

    {{< figure src="/images/netq/change-user-permissions-221.png" width="250" >}}

5. Enter your admin password.

6. Click **Save** to commit the change, or **Cancel** to discard the change.

### Correct a Mistyped User ID (Email Address)

You cannot edit a user's email address, because this is the identifier the system uses for authentication. If you need to change an email address, you must create a new one for this user. Refer to {{<link title="#Add New User Account" text="Add New User Account">}}. You should delete the incorrect user account. Select the user account, and click <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/23-Delete/bin-1.svg" height="18" width="18"/>.

### Export a List of User Accounts

You can export user account information at any time using the User Accounts tab.

To export information for one or more user accounts:

1. Click **Manage** on the User Accounts card to open the **User Accounts** tab.

2. Select one or more accounts that you want to export by clicking the checkbox next to them. Alternately select all accounts by clicking <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/check-circle-1.svg" height="18" width="18"/>.

3. Click <img src="https://icons.cumulusnetworks.com/05-Internet-Networks-Servers/08-Upload-Download/upload-bottom.svg" height="18" width="18"/> to export the selected user accounts.

### Delete a User Account

NetQ application administrators should remove user accounts associated with users that are no longer using the application.

To delete one or more user accounts:

1. Click **Manage** on the User Accounts card to open the **User Accounts** tab.

2. Select one or more accounts that you want to remove by clicking the checkbox next to them.

3. Click <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/23-Delete/bin-1.svg" height="18" width="18"/> to remove the accounts.

## Manage User Login Policies

NetQ application administrators can configure a session expiration time and the number of times users can refresh before requiring users to re-login to the NetQ application.

To configure these login policies:

1. Click <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/03-Menu/navigation-menu.svg" height="18" width="18"/> (main menu), and select **Management** under the **Admin** column.

2. Locate the Login Management card.

3. Click **Manage**.

    {{<figure src="/images/netq/netq-mgmt-login-mgmt-config-modal-320.png" width="400" >}}

4. Select how long a user may be logged in before logging in again; 30 minutes, 1, 3, 5, or 8 hours.

    Default for on-premises deployments is 6 hours. Default for cloud deployments is 30 minutes.

5. Indicate the number of times (between 1 and 100) the application can be refreshed before the user must log in again. Default is unspecified.

6. Enter your admin password.

7. Click **Update** to save the changes, or click **Cancel** to discard them.

    The Login Management card shows the configuration.

    {{<figure src="/images/netq/netq-mgmt-login-mgmt-card-configd-320.png" width="200" >}}

## Monitor User Activity

NetQ application administrators can audit user activity in the application using the Activity Log.

To view the log, click <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/03-Menu/navigation-menu.svg" height="18" width="18"/> (main menu), then click **Activity Log** under the **Admin** column.

{{<figure src="/images/netq/main-menu-ntwk-activity-log-320.png" width="700" >}}

Click {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/15-Filter/filter-1.svg" height="18" width="18">}} to filter the log by username, action, resource, and time period.

Click {{<img src="https://icons.cumulusnetworks.com/05-Internet-Networks-Servers/08-Upload-Download/upload-bottom.svg" width="18" height="18">}} to export the log a page at a time.

## Manage Scheduled Traces

From the NetQ Management workbench, you can view the number of traces scheduled to run in the system. A set of default traces are provided with the NetQ GUI. As an administrator, you can run one or more scheduled traces, add new scheduled traces, and edit or delete existing traces.

### Add a Scheduled Trace

You can create a scheduled trace to provide regular status about a particularly important connection between a pair of devices in your network or for temporary troubleshooting.

To add a trace:

1. Click **Manage** on the Scheduled Traces card to open the **Scheduled Traces** tab.

2. Click **Add Trace** to open the large New Trace Request card.

    {{<figure src="/images/netq/trace-request-large-222.png" width="500">}}

3. Enter source and destination addresses.

    {{%notice note%}}
For layer 2 traces, the source must be a hostname and the destination must be a MAC address. For layer 3 traces, the source can be a hostname or IP address, and the destination must be an IP address.
    {{%/notice%}}

4. Specify a VLAN for a layer 2 trace or (optionally) a VRF for a layer 3 trace.

5. Set the schedule for the trace, by selecting how often to run the trace and when to start it the first time.

6. Click **Save As New** to add the trace. You are prompted to enter a name for the trace in the **Name** field.  

    If you want to run the new trace right away for a baseline, select the trace you just added from the dropdown list, and click **Run Now**.

### Delete a Scheduled Trace

If you do not want to run a given scheduled trace any longer, you can remove it.

To delete a scheduled trace:

1. Click **Manage** on the Scheduled Trace card to open the **Scheduled Traces** tab.

2. Select at least one trace by clicking on the checkbox next to the trace.

3. Click <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/23-Delete/bin-1.svg" height="16" width="16"/>.

### Export a Scheduled Trace

You can export a scheduled trace configuration at any time using the Scheduled Traces tab.

To export one or more scheduled trace configurations:

1. Click **Manage** on the Scheduled Trace card to open the **Scheduled Traces** tab.

2. Select one or more traces by clicking on the checkbox next to the trace. Alternately, click <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/check-circle-1.svg" height="18" width="18"/> to select all traces.

3. Click <img src="https://icons.cumulusnetworks.com/05-Internet-Networks-Servers/08-Upload-Download/upload-bottom.svg" height="18" width="18"/> to export the selected traces.

## Manage Scheduled Validations

From the NetQ Management workbench, you can view the total number of validations scheduled to run in the system. A set of default scheduled validations are provided and pre-configured with the NetQ UI. These are not included in the total count. As an administrator, you can view and export the configurations for all scheduled validations, or add a new validation.

### View Scheduled Validation Configurations

You can view the configuration of a scheduled validation at any time. This can be useful when you are trying to determine if the validation request needs to be modified to produce a slightly different set of results (editing or cloning) or if it would be best to create a new one.

To view the configurations:

1. Click **Manage** on the Scheduled Validations card to open the **Scheduled Validations** tab.

2. Click <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/close.svg" height="14" width="14"/> in the top right to return to your NetQ Management cards.

### Add a Scheduled Validation

You can add a scheduled validation at any time using the Scheduled Validations tab.

To add a scheduled validation:

1. Click **Manage** on the Scheduled Validations card to open the **Scheduled Validations** tab.

2. Click **Add Validation** to open the large Validation Request card.

    {{<figure src="/images/netq/valid-request-large-222.png" width="500">}}

4.  Configure the request. Refer to {{<link title="Validate Network Protocol and Service Operations">}} for details.

### Delete Scheduled Validations

You can remove a scheduled validation that you created (one of the 15 allowed) at any time. You cannot remove the default scheduled validations included with NetQ.

To remove a scheduled validation:

1. Click **Manage** on the Scheduled Validations card to open the **Scheduled Validations** tab.

2. Select one or more validations that you want to delete.

3. Click <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/23-Delete/bin-1.svg" height="16" width="16"/> above the validations list.

### Export Scheduled Validation Configurations

You can export one or more scheduled validation configurations at any time using the Scheduled Validations tab.

To export a scheduled validation:

1. Click **Manage** on the Scheduled Validations card to open the **Scheduled Validations** tab.

2. Select one or more validations by clicking the checkbox next to the validation. Alternately, click <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/check-circle-1.svg" height="18" width="18"/> to select all validations.

3. Click <img src="https://icons.cumulusnetworks.com/05-Internet-Networks-Servers/08-Upload-Download/upload-bottom.svg" height="18" width="18"/> to export selected validations.

    {{<figure src="/images/netq/netq-mgmt-sched-valid-tab-export-241.png" width="700">}}

## Manage Threshold Crossing Rules

NetQ supports a set of events that are triggered by crossing a user-defined threshold, called TCA events. These events allow detection and prevention of network failures for selected ACL resources, digital optics, forwarding resources, interface errors and statistics, link flaps, resource utilization, sensor and WJH events. A complete list of supported events can be found in the {{<link title="TCA Event Messages Reference">}}.

Instructions for managing these rules can be found in {{<link title="Configure Threshold-Based Event Notifications/#manage-threshold-based-event-notifications" text="Manage Threshold-based Event Notifications">}}.

## Manage Notification Channels

NetQ supports Slack, PagerDuty, and syslog notification channels for reporting system and threshold-based events. You can access channel configuration in one of two ways:

- Click **Manage** on the Channels card

    {{<figure src="/images/netq/netq-mgmt-channels-card-320.png" width="200">}}

- Click <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/03-Menu/navigation-menu.svg" height="18" width="18"/>, and then click **Channels** in the **Notifications** column

    {{<figure src="/images/netq/main-menu-channels-selected-300.png" width="600">}}

In either case, the Channels view is opened.

{{<figure src="/images/netq/channels-none-created-300.png" width="700">}}

Determine the type of channel you want to add and follow the instructions for the selected type in {{<link title="Configure System Event Notifications">}}. Refer to {{<link title="Configure System Event Notifications/#remove-an-event-notification-channel" text="Remove a Channel">}} to remove a channel you no longer need.

## Configure Multiple Premises

The NetQ Management dashboard provides the ability to configure a single NetQ UI and  CLI for monitoring data from multiple external premises in addition to your local premises.

A complete NetQ deployment is required at each premises. The NetQ appliance or VM of one of the deployments acts as the primary (similar to a proxy) for the premises in the other deployments. A list of these external premises is stored with the primary deployment. After the multiple premises are configured, you can view this list of external premises, change the name of premises on the list, and delete premises from the list.

{{<figure src="/images/netq/appmgmt-multisite-onprem-300.png" width="500">}}

To configure monitoring of external premises:

1. Sign in to primary NetQ Appliance or VM.

2. In the NetQ UI, click {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/03-Menu/navigation-menu.svg" height="18" width="18" alt="Main Menu">}}.

3. Select *Management* from the **Admin** column.

4. Locate the External Premises card.

    {{<figure src="/images/netq/premises-card-300.png" width="200">}}

5. Click **Manage**.

6. Click <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/43-Remove-Add/add-circle.svg" height="18" width="18"/> to open the Add Premises dialog.

    {{<figure src="/images/netq/premises-add-300.png" width="300">}}

7. Specify an external premises.

    - Enter an IP address for the API gateway on the external NetQ Appliance or VM in the Hostname field (required)
    - Enter the access credentials

8. Click **Next**.

9. Select from the available premises associated with this deployment by clicking on their names.

10. Click **Finish**.

11. Add more external premises by repeating Steps 6-10.

## System Server Information

You can easily view the configuration of the physical server or VM from the NetQ Management dashboard. 

To view the server information:

1. Click {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/03-Menu/navigation-menu.svg" height="18" width="18" alt="Main Menu">}}.

2. Select *Management* from the **Admin** column.

3. Locate the System Server Info card.

    {{<figure src="/images/netq/netq-mgmt-sys-server-info-card-300.png" width="500">}}

    If no data is present on this card, it is likely that the NetQ Agent on your server or VM is not running properly or the underlying streaming services are impaired.

## Integrate with Your LDAP Server

For on-premises deployments you can integrate your LDAP server with NetQ to provide access to NetQ using LDAP user accounts instead of ,or in addition to, the NetQ user accounts. Refer to {{<link title="Integrate NetQ with Your LDAP Server">}} for more detail.
