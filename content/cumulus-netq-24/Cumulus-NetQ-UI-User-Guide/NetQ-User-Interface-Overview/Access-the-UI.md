---
title: Access the NetQ UI
author: Cumulus Networks
weight: 240
toc: 4
---
Logging in to the NetQ UI is as easy as opening any web page.

To log in to the UI:

1.  Open a new Internet browser window or tab.
2.  Enter the following URL into the Address bar for the on-site NetQ Platform/NetQ Appliance or the NetQ Cloud Appliance:  
    - On-premises: *https://\<hostname-or-ipaddress\>:443*  
    - Cloud: *https://netq.cumulusnetworks.com*

    {{< figure src="/images/netq/access-ui-login-screen-230.png" width="700" >}}

3.  Enter your username and then your password:  
    - NetQ Platform: *admin, admin* by default  
    - NetQ Appliance: *cumulus, CumulusLinux\!* by default  
    - NetQ Cloud Appliance: Use credentials provided by Cumulus via email titled *Welcome to Cumulus NetQ\!* and accept the terms of use.

    {{< figure src="/images/netq/access-ui-cumulus-wb-241.png" width="700" >}}

    On your first login, the default Cumulus Workbench opens, with your username shown in the upper right corner of the application. The NetQ Cloud UI has a **Premises** list in the application header, but is otherwise the same. On future logins, the last workbench that you were viewing is displayed.

To log out of the UI:

1.  Click the user icon at the top right of the application.

2.  Select **Log Out**.  

    {{< figure src="/images/netq/access-ui-logout-230.png" width="150" >}}
