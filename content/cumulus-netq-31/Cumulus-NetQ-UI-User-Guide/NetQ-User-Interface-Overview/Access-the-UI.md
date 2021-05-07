---
title: Access the NetQ UI
author: Cumulus Networks
weight: 240
toc: 4
---
The NetQ UI is a web-based application. Logging in and logging out are simple and quick.

To log in to the UI:

1. Open a new Internet browser window or tab.
2. Enter the following URL into the Address bar for the NetQ On-premises Appliance or VM, or the NetQ Cloud Appliance or VM:  
    - On-premises: *https://\<hostname-or-ipaddress\>:443*  
    - Cloud: *https://netq.cumulusnetworks.com*

    {{<figure src="/images/netq/access-ui-login-screen-310.png" width="600" >}}

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

    *Passwords must contain a minimum of eight characters, including at least one uppercase letter, one lowercase letter, one special character, and one number.* If you do not enter a strong enough password, you are reminded of these requirements.

    The following error message appears if you enter incorrect credentials:

    {{<figure src="/images/netq/access-ui-cred-error-310.png" width="250">}}

3. Click **Login**.

    This opens the Reset Password dialog.

    {{<figure src="/images/netq/access-ui-reset-pswd-310.png" width="250">}}

4. Enter your current password.

5. Enter a new password.

6. Enter the new password again to confirm it.

7. Click **Reset**.

    This opens the Terms of Use notice.

     {{<figure src="/images/netq/access-ui-terms-310.png" width="350">}}

8. Read the Terms of Use.

9. Click the checkbox and click **Accept**.

    The default Cumulus Workbench opens, with your username shown in the upper right corner of the application.

    {{<figure src="/images/netq/access-ui-cumulus-wb-310.png" width="700">}}

{{< /tab >}}

{{< tab "Log In After First Time" >}}

1. Enter your username.

2. Enter your password.

3. Click **Login**.

    The user-specified home workbench is displayed. If a home workbench is not specified, then the default Cumulus Workbench is displayed.

    {{<notice tip>}}
Any workbench can be set as the home workbench. Click <img src="https://icons.cumulusnetworks.com/17-Users/19-Natural-Close%20Up-Single%20User-Man/single-man-circle.svg" height="18" width="18"/> (User Settings), click <strong>Profiles and Preferences</strong>, then on the Workbenches card click to the left of the workbench name you want to be your home workbench.
    {{</notice>}}

{{< /tab >}}

{{< /tabs >}}

To log out of the UI:

1. Click <img src="https://icons.cumulusnetworks.com/17-Users/19-Natural-Close%20Up-Single%20User-Man/single-man-circle.svg" height="18" width="18"/> at the top right of the application.

2. Select **Log Out**.  

    {{<figure src="/images/netq/access-ui-logout-230.png" width="150">}}
