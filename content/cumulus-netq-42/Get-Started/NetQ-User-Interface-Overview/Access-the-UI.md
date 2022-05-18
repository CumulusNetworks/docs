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
    - NetQ Cloud Appliance or VM: *https://netq.cumulusnetworks.com*

    {{< figure src="/images/netq/access-ui-login-screen-400.png" alt="NetQ login screen" width="700" >}}

3. Sign in.

    The following are the default usernames and passwords for UI access:  
    - NetQ On-premises: *admin, admin*
    - NetQ Cloud: Use the credentials you created during setup. You should receive an email from NVIDIA titled *NetQ Access Link.*
<!-- vale on -->

{{<tabs "login">}}

{{<tab "First Time Log In—On Premises">}}

1. Enter your username.

2. Enter your password.

3. Enter a new password.

4. Enter the new password again to confirm it.

5. Click **Update and Accept** after reading the Terms of Use.

    The default NetQ Workbench opens, with your username shown in the upper right corner of the application.

    {{<figure src="/images/netq/access-ui-cumulus-wb-400.png" alt="" width="700">}}

{{</tab>}}

{{<tab "First Time Log In—NetQ Cloud">}}

1. Locate the email you received from NVIDIA titled *NetQ Access Link*. Select **Create Password**.

2. Enter a new password. Then enter it again to confirm it.

4. Log in using your email address and new password.

5. Accept the Terms of Use after reading them.

    The default NetQ Workbench opens, with your username and premise shown in the upper right corner of the application.

    {{<figure src="/images/netq/new-premise-username.png" alt="username and premises information in the UI header" width="300">}}

    You can view your configuration key used during OPTA installation by selecting the premise and choosing **Manage Premises**.
{{</tab>}}

{{<tab "Log In After First Time">}}

1. Enter your username.

2. Enter your password.

    The user-specified home workbench is displayed. If a home workbench is not specified, then the Cumulus Default workbench is displayed.

    {{<notice tip>}}
Any workbench can be set as the home workbench. Click <img src="https://icons.cumulusnetworks.com/17-Users/19-Natural-Close%20Up-Single%20User-Man/single-man-circle.svg" height="18" width="18"/> (User Settings), click <strong>Profiles and Preferences</strong>, then on the Workbenches card click to the left of the workbench name you want to be your home workbench.
    {{</notice>}}

{{</tab>}}

{{</tabs>}}

## Reset a Forgotten Password

To reset a password for cloud deployments:

1. Enter *https://netq.cumulusnetworks.com* in your browser to open the login page.

2. Click **Forgot Password?** and enter an email address. Look for a message with the subject *NetQ Password Reset Link* from *netq-sre@cumulusnetworks.com*.  

3. Click on the link in the email and follow the instructions to create a new password. 

## Log Out of NetQ

To log out of the NetQ UI:

1. Click <img src="https://icons.cumulusnetworks.com/17-Users/19-Natural-Close%20Up-Single%20User-Man/single-man-circle.svg" height="18" width="18"/> at the top right of the application.

2. Select **Log Out**.  

    {{<figure src="/images/netq/access-ui-logout-230.png" width="150">}}
