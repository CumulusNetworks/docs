---
title: Access the NetQ UI
author: Cumulus Networks
weight: 240
toc: 4
---
Logging in to the NetQ UI is as easy as opening any web page.

To log in to the UI:

1. Open a new Internet browser window or tab.
2. Enter the following URL into the Address bar for the NetQ On-premises Appliance or VM, or the NetQ Cloud Appliance or VM:  
    - On-premises: *https://\<hostname-or-ipaddress\>:443*  
    - Cloud: *https://netq.cumulusnetworks.com*

    {{< figure src="/images/netq/access-ui-login-screen-310.png" width="600" >}}

3. Login.

    Default usernames and passwords for UI access:  
    - NetQ On-premises: *admin, admin*
    - NetQ Cloud: Use credentials provided by Cumulus via email titled *Welcome to Cumulus NetQ\!*

    {{<notice tip>}}
For cloud deployments, after three failed attempts to log in, the user is locked out for 15 minutes.
    {{</notice>}}

{{< tabs "TabID24" >}}

{{< tab "First Time Log In" >}}

1. Enter your username.

2. Enter your password.

3. Click **Login**.

4. Change your password.

    Enter a new password with a minimum of eight characters, including at least one uppercase letter, one lowercase letter, one special character, and one number.

5. Enter the new password again to confirm it.

6. Click **Sign In**.

7. Read the Terms of Use.

8. Click the checkbox at the end and click **Accept**.

    The default Cumulus Workbench opens, with your username shown in the upper right corner of the application.

    {{< figure src="/images/netq/access-ui-cumulus-wb-300.png" width="700" >}}

{{< /tab >}}

{{< tab "Log In After First Time" >}}

1. Enter your username.

2. Enter your password.

    The user-specified home workbench is displayed. If a home workbench is not specified, then the Cumulus Default workbench is displayed.

    {{<notice tip>}}
Any workbench can be set as the home workbench. Click <img src="https://icons.cumulusnetworks.com/17-Users/19-Natural-Close%20Up-Single%20User-Man/single-man-circle.svg" height="18" width="18"/> (User Settings), click <strong>Profiles and Preferences</strong>, then on the Workbenches card click to the left of the workbench name you want to be your home workbench.
    {{</notice>}}

{{< /tab >}}

{{< /tabs >}}

To log out of the UI:

1. Click <img src="https://icons.cumulusnetworks.com/17-Users/19-Natural-Close%20Up-Single%20User-Man/single-man-circle.svg" height="18" width="18"/> at the top right of the application.

2. Select **Log Out**.  

    {{<figure src="/images/netq/access-ui-logout-230.png" width="150">}}
