---
title: Access the NetQ UI
author: NVIDIA
weight: 100
toc: 4
---
The NetQ UI is a web-based application. Logging in and logging out are simple and quick. Users working with a cloud deployment of NetQ can reset forgotten passwords.

## Log In to NetQ

To log in to the UI:

<!-- vale off -->
1. Open a new Chrome browser window or tab.
2. Enter the following URL into the address bar:  
    - NetQ On-premises Appliance or VM: *https://\<hostname-or-ipaddress\>:443*  
    - NetQ Cloud Appliance or VM: *https://netq.cumulusnetworks.com*

    {{< figure src="/images/netq/access-ui-login-screen-400.png" width="700" >}}

3. Sign in.

    Default usernames and passwords for UI access:  
    - NetQ On-premises: *admin, admin*
    - NetQ Cloud: Use credentials created during setup. You should receive an email from NVIDIA titled *NetQ Access Link.*
<!-- vale on -->

{{<tabs "login">}}

{{<tab "First Time Log In - On Premises">}}

1. Enter your username.

2. Enter your password.

3. Enter a new password.

4. Enter the new password again to confirm it.

5. Click **Update and Accept** after reading the Terms of Use.

    The default NetQ Workbench opens, with your username shown in the upper right corner of the application.

    {{<figure src="/images/netq/access-ui-cumulus-wb-400.png" width="700">}}

{{</tab>}}

{{<tab "First Time Log In - NetQ Cloud">}}

1. Select **Create Password** from the email received from NVIDIA titled *NetQ Access Link."

2. Enter a new password.

3. Enter the new password again to confirm it.

4. Log in using your email address and created password.

5. Click to agree and accept the Terms of Use after reading them.

    The default NetQ Workbench opens, with your username and premise shown in the upper right corner of the application.

    {{<figure src="/images/netq/new-premise-username.png" width="300">}}

6. Click on the premise and select **Activate Wizard**

    {{<figure src="/images/netq/activate-premise.png" width="400">}}

7. Click through the activation wizard and follow the instructions to obtain the activation key used during installation through the {{<link title="Install NetQ Using the Admin UI#install-netq" text="Admin UI.">}}

{{<figure src="/images/netq/activation-wizard-admin-login.png" width="1000">}}

{{<figure src="/images/netq/activation-wizard-key.png" width="1000">}}

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

For cloud deployments, you can reset your password if it has been forgotten.

To reset a password:

1. Enter *https://netq.cumulusnetworks.com* in your browser to open the login page.

    {{<figure src="/images/netq/access-ui-cld-login-320.png" width="250">}} <!-- UPDATE ME! -->

2. Click **Forgot Password?**

3. Enter an email address where you want instructions to be sent for resetting the password.

4. Click **Send Reset Email**, or click **Cancel** to return to login page.

    {{<figure src="/images/netq/access-ui-reset-email-sent-320.png" width="250">}}

5. Log in to the email account where you sent the reset message. Look for a message with a subject of *NetQ Password Reset Link* from *netq-sre@cumulusnetworks.com*.

6. Click on the link provided to open the Reset Password dialog.

    {{<figure src="/images/netq/access-ui-reset-forgotten-pswd-320.png" width="250">}}

7. Enter a new password.

8. Enter the new password again to confirm it.

9. Click **Reset**.

    A confirmation message is shown on successful reset.

    {{<figure src="/images/netq/access-ui-reset-pswd-success-320.png" width="250">}}

10. Click **Login** to access NetQ with your username and new password.

## Log Out of NetQ

To log out of the NetQ UI:

1. Click <img src="https://icons.cumulusnetworks.com/17-Users/19-Natural-Close%20Up-Single%20User-Man/single-man-circle.svg" height="18" width="18"/> at the top right of the application.

2. Select **Log Out**.  

    {{<figure src="/images/netq/access-ui-logout-230.png" width="150">}}
