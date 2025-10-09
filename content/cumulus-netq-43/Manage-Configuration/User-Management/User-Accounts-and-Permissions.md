---
title: User Accounts and Permissions
author: NVIDIA
weight: 500
toc: 2
---
Sign in to NetQ as an admin to view and manage users' accounts. If you are a user and would like to set individual preferences, visit {{<link title="Set User Preferences" text="Set User Preferences">}}.

## NetQ Management Workbench

Navigate to the NetQ Management dashboard to complete the tasks outlined in this section. To get there, expand the menu <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/03-Menu/navigation-menu.svg" height="18" width="18"/> on the NetQ dashboard and select **Management**.

{{<figure src="/images/netq/netq-mgmt-wb-cloud-330.png" width="700"caption="Cloud NetQ Management Dashboard">}}

### Add a User Account

This section outlines the steps to add a local user. To add an LDAP user, refer to {{<link title="LDAP Authentication" text="LDAP Authentication">}}.

To add a new account:

1. On the User Accounts card, select **Manage** to open a table listing all user accounts.

2. Above the table, select {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/43-Remove-Add/add-circle.svg" alt="add" height="18" width="18">}} to add a user.

    {{< figure src="/images/netq/add-new-user-modal-221.png" width="250" >}}

3. Enter the fields and select **Save**.

    {{%notice note%}}
Be especially careful entering the email address as you *cannot* change it once you save the account. If you save a mistyped email address, you must delete the account and create a new one.
    {{%/notice%}}

### Edit a User Account

As an admin, you can:
+ edit a user's first or last name
+ reset a user's password
+ change a user's access type (user or admin)

You cannot edit a user’s email address, because this is the identifier the system uses for authentication. If you need to change an email address, delete the user and create a new one.

To edit an account:

1. On the User Accounts card, select **Manage** to open a table listing all user accounts.

2. Select the user whose account you'd like to edit. Above the table, click <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/22-Edit/pencil-1.svg" alt="edit" height="18" width="18"/> to edit the user's account information.

    {{< figure src="/images/netq/edit-user-modal-221.png" width="250" >}}


### Delete a User Account

To delete one or more user accounts:

1. On the User Accounts card, select **Manage** to open a table listing all user accounts.

2. Select one or more accounts. Above the table, click <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/23-Delete/bin-1.svg" alt="delete" height="18" width="18"/> to delete the selected account(s).

### View User Activity

Administrators can view user activity in the activity log.

To view the log, expand the <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/03-Menu/navigation-menu.svg" alt="menu" height="18" width="18"/> menu on the NetQ dashboard and select **Management**. Under **Admin** select **Activity Log** to open a table listing user activity. Use the controls above the table to filter or export the data.

{{<figure src="/images/netq/main-menu-ntwk-activity-log-320.png" width="700" >}}


### Manage Login Policies

Administrators can configure a session expiration time and the number of times users can refresh before requiring users to log in again to NetQ.

To configure these login policies:

1. On the Login Management card, select **Manage**.

2. Select how long a user can be logged in before logging in again.

 {{<figure src="/images/netq/netq-mgmt-login-mgmt-config-modal-330.png" width="400" >}}

3. Click **Update** to save the changes.

    The Login Management card shows the configuration.

    {{<figure src="/images/netq/netq-mgmt-login-mgmt-card-configd-330.png" width="200" >}}


