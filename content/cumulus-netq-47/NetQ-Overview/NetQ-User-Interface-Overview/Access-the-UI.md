---
title: Access the NetQ UI
author: NVIDIA
weight: 100
toc: 4
---
This page describes how to log in and out of NetQ.

## Log In to NetQ

1. Open a new Chrome or Firefox browser window or tab.
2. Enter the following URL into the address bar:  
    - NetQ on-premises appliance or VM: *https://\<hostname-or-ipaddress\>*  
    - NetQ cloud appliance or VM: *https://netq.nvidia.com*

    {{<figure src="/images/netq/splash-470.png" alt="NetQ login screen" width="700">}}

3. Log in.

    The following are the default usernames and passwords for UI access:  
    - NetQ on-premises: *admin, admin*
    - NetQ Cloud: Use the credentials you created during setup. You should receive an email from NVIDIA titled *NetQ Access Link.*
<!-- vale on -->

{{<tabs "login">}}

{{<tab "First-time Login for Cloud">}}

Enter your username and password to log in. You can also log in with SSO if your company has enabled it.

**Username and Password**

1. Locate the email you received from NVIDIA titled *NetQ Access Link*. Select **Create Password**.

2. Enter a new password, then enter it again to confirm it.

4. Log in using your email address and new password.

5. Accept the Terms of Use after reading them.

    The default workbench opens, with your username and premises shown in the top-right corner of NetQ.

**SSO**

1. Follow the steps above until you reach the NetQ login screen.

2. Select **Sign up for SSO** and enter your organization's name. 

{{</tab>}}

{{<tab "First-time Login for On-premises">}}

1. Enter your username and password.

3. Create a new password and enter the new password again to confirm it.

5. Click **Update and Accept** after reading the Terms of Use.

    The default workbench opens, with your username shown in the top-right corner of NetQ.

{{</tab>}}

{{<tab "Subsequent Logins">}}

1. Enter your username.

2. Enter your password.

    The user-specified home workbench is displayed. If a home workbench is not specified, then the default workbench is displayed.

    {{<notice tip>}}
Any workbench can be set as the home workbench. Select <img src="https://icons.cumulusnetworks.com/17-Users/19-Natural-Close%20Up-Single%20User-Man/single-man-circle.svg" height="18" width="18"/> <strong>User Settings</strong> > <strong>Profiles and Preferences</strong>, then on the Workbenches card select the workbench you'd like to designate as your home workbench.
    {{</notice>}}

{{</tab>}}

{{</tabs>}}

## Log Out of NetQ

1. Select  <img src="https://icons.cumulusnetworks.com/17-Users/19-Natural-Close%20Up-Single%20User-Man/single-man-circle.svg" alt="profile" height="18" width="18"/> **User Settings** in the top-right corner of NetQ.

2. Select **Log Out**.  

## Related Information
- {{<link title="Set User Preferences" text="Set User Preferences">}}
- {{<link title="Add and Manage Accounts" text="Add and Manage Accounts">}}
