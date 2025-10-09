---
title: Access the NetQ UI
author: NVIDIA
weight: 100
toc: 4
---
This page describes how to sign in and out of NetQ, and how to reset your password.

## Log In to NetQ

To log in to the UI:

<!-- vale off -->
1. Open a new Chrome browser window or tab.
2. Enter the following URL into the address bar:  
    - NetQ On-premises Appliance or VM: *https://\<hostname-or-ipaddress\>:443*  
    - NetQ Cloud Appliance or VM: *https://netq.nvidia.com*

    {{< figure src="/images/netq/access-ui-login-screen-400.png" alt="NetQ login screen" width="700" >}}

3. Sign in.

    The following are the default usernames and passwords for UI access:  
    - NetQ On-premises: *admin, admin*
    - NetQ Cloud: Use the credentials you created during setup. You should receive an email from NVIDIA titled *NetQ Access Link.*
<!-- vale on -->

{{<tabs "login">}}

{{<tab "First Time Log In—NetQ Cloud">}}

Use your username and password to log in. You can also log in with SSO if your company has enabled it.

**Username and Password**

1. Locate the email you received from NVIDIA titled *NetQ Access Link*. Select **Create Password**.

2. Enter a new password. Then enter it again to confirm it.

4. Log in using your email address and new password.

5. Accept the Terms of Use after reading them.

    The default NetQ Workbench opens, with your username and premise shown in the upper right corner of the application.

    {{<figure src="/images/netq/new-premise-username.png" alt="username and premises information in the UI header" width="300">}}

**SSO**

1. Follow the steps above until you reach the NetQ login screen.

2. Select **Sign up for SSO** and enter your organization's name. 

{{</tab>}}

{{<tab "First Time Log In—On Premises">}}

1. Enter your username and password.

3. Create a new password and enter the new password again to confirm it.

5. Click **Update and Accept** after reading the Terms of Use.

    The default NetQ Workbench opens, with your username shown in the upper right corner of the application.

    {{<figure src="/images/netq/access-ui-cumulus-wb-400.png" alt="" width="700">}}

{{</tab>}}

{{<tab "Log In After First Time">}}

1. Enter your username.

2. Enter your password.

    The user-specified home workbench is displayed. If a home workbench is not specified, then the default workbench is displayed.

    {{<notice tip>}}
Any workbench can be set as the home workbench. Click <img src="https://icons.cumulusnetworks.com/17-Users/19-Natural-Close%20Up-Single%20User-Man/single-man-circle.svg" height="18" width="18"/> (User Settings), click <strong>Profiles and Preferences</strong>, then on the Workbenches card click to the left of the workbench name you want to be your home workbench.
    {{</notice>}}

{{</tab>}}

{{</tabs>}}

## Reset a Password

{{<tabs "resetpassword">}}

{{<tab "On Premises">}}

To reset the password for the `admin` account to the default password:

1. Run the following command on the command line of your on-premises appliance:

```
kubectl exec $(kubectl get pod -oname -l app=cassandra) -- cqlsh -e "INSERT INTO master.user(id,  cust_id,  first_name,  last_name,  password,     access_key,  role,  email,  is_ldap_user,  is_active,  terms_of_use_accepted,  enable_alarm_notifications,  default_workbench,  preferences,  creation_time,  last_login,  reset_password)     VALUES(  'admin',  0,  'Admin',  '',  '009413d86fd42592e0910bb2146815deaceaadf3a4667b728463c4bc170a6511',     null, 'admin',  null,  false,  true,  true,  true,  { workspace_id : 'DEFAULT', workbench_id : 'DEFAULT' },  '{}',  toUnixTimestamp(now()),  toUnixTimestamp(now()),  true )"
```

2. Log in to your NetQ UI with the default username and password of *admin/admin*. After logging in, you will be prompted to change the password. 

{{</tab>}}

{{<tab "NetQ Cloud">}}

To reset a password for cloud deployments:

1. Enter *https://netq.nvidia.com* in your browser to open the login page.

2. Click **Forgot Password?** and enter an email address. Look for a message with the subject *NetQ Password Reset Link* from *netq-sre@cumulusnetworks.com*.  

3. Select the link in the email and follow the instructions to create a new password. 

{{</tab>}}

{{</tabs>}}
## Log Out of NetQ

To log out of the NetQ UI:

1. Select  <img src="https://icons.cumulusnetworks.com/17-Users/19-Natural-Close%20Up-Single%20User-Man/single-man-circle.svg" alt="profile" height="18" width="18"/> at the top right of the application.

2. Select **Log Out**.  

    {{<figure src="/images/netq/access-ui-logout-230.png" width="150">}}
