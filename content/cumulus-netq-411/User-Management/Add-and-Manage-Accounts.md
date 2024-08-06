---
title: Add and Manage Accounts
author: NVIDIA
weight: 500
toc: 2
---
Sign in to NetQ as an admin to view and manage accounts. If you want to change individual preferences, visit {{<link title="Set User Preferences" text="Set User Preferences">}}.

Navigate to the NetQ management dashboard to complete the tasks outlined in this section. To get there, expand the <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/03-Menu/navigation-menu.svg" height="18" width="18"/> **Menu** on the NetQ dashboard and select **Management**.

## Add an Account

This section outlines the steps to add a local user account. To add an LDAP account, refer to {{<link title="LDAP Authentication" text="LDAP Authentication">}}.

To create a new account:

1. On the User Accounts card, select **Manage** to open a table listing all accounts.

2. Above the table, select {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/43-Remove-Add/add-circle.svg" alt="add" height="18" width="18">}} **Add** to add an account.

    {{<img src="/images/netq/add-user-470.png" alt="" width="250">}}
    <div style="margin-top: 20px;"></div>

3. Enter the fields and select **Save**.

    {{%notice note%}}
Be especially careful entering the email address; you *cannot* change it once you save the account. If you save a mistyped email address, you must delete the account and create a new one.
    {{%/notice%}}

## Edit an Account

As an admin, you can:
+ Edit the first or last name associated with an account
+ Reset an account's password
+ Change an account's role (user or admin)

You cannot edit the email address associated with an account, because this is the identifier the system uses for authentication. If you need to change an email address, delete the account and create a new one.

To edit an account:

1. On the User Accounts card, select **Manage** to open a table listing all accounts.

2. Select the account you'd like to edit. Above the table, click <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/22-Edit/pencil-1.svg" alt="edit" height="18" width="18"/>  **Edit** to edit the account's information.

## Reset an Admin Password

If your account is assigned an admin role, reset your password by restoring the default password, then changing the password:

{{<tabs "resetpassword">}}

{{<tab "On-Premises">}}

1. Run the following command on your on-premises server's CLI:

```
kubectl exec $(kubectl get pod -oname -l app=cassandra) -- cqlsh -e "INSERT INTO master.user(id,  cust_id,  first_name,  last_name,  password,     access_key,  role,  email,  is_ldap_user,  is_active,  terms_of_use_accepted,  enable_alarm_notifications,  default_workbench,  preferences,  creation_time,  last_login,  reset_password)     VALUES(  'admin',  0,  'Admin',  '',  '009413d86fd42592e0910bb2146815deaceaadf3a4667b728463c4bc170a6511',     null, 'admin',  null,  false,  true,  true,  true,  { workspace_id : 'DEFAULT', workbench_id : 'DEFAULT' },  '{}',  toUnixTimestamp(now()),  toUnixTimestamp(now()),  true )"
```

2. Log in to the NetQ UI with the default username and password: *admin, admin*. After logging in, you will be prompted to change the password. 

{{</tab>}}

{{<tab "NetQ cloud">}}

To reset a password for cloud deployments:

1. Enter *https://netq.nvidia.com* in your browser to open the login page.

2. Click **Forgot Password?** and enter an email address. Look for a message with the subject *NetQ Password Reset Link* from *netq-sre@cumulusnetworks.com*.  

3. Select the link in the email and follow the instructions to create a new password. 

{{</tab>}}

{{</tabs>}}


## Delete an Account

To delete one or more accounts:

1. On the User Accounts card, select **Manage** to open a table listing all accounts.

2. Select one or more accounts. Above the table, click <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/23-Delete/bin-1.svg" alt="delete" height="18" width="18"/> **Delete** to delete the selected account(s).

## View Account Activity

Administrators can view account activity in the activity log. To get there, expand the <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/03-Menu/navigation-menu.svg" alt="menu" height="18" width="18"/> **Menu** and select **Activity log**. Use the controls above the table to filter or export the data.

## Manage Login Policies

Administrators can configure a session expiration time and the number of times users can refresh before requiring them to log in again to NetQ.

To configure these login policies:

1. On the Login Management card, select **Manage**.

2. Select how long an account can be logged in before requiring a user to log in again:

    {{<figure src="/images/netq/login-management-470.png" alt="" width="450" >}}

3. Click **Update** to save the changes.

    The Login Management card reflects the updated configuration.


