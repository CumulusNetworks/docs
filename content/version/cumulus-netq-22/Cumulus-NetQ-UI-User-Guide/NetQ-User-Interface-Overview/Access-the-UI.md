---
title: Access the NetQ UI
author: Cumulus Networks
weight: 501
pageID: 12321856
product: Cumulus NetQ
version: 2.2
imgData: cumulus-netq-22
siteSlug: cumulus-netq-22
---
Logging in to the NetQ UI is as easy as opening any web page.

To log in to the UI:

1.  Open a new Internet browser window or tab.
2.  Enter the following URL into the Address bar for the on-site NetQ Platform/NetQ Appliance or the NetQ Cloud Appliance:  
    - On-premises: *http://\<netq-platform/appliance-ipaddress\>:32666*  
    - Cloud: *http//netq.cumulusnetworks.com*

    {{% imgOld 0 %}}

3.  Select your language of choice (English or Spanish) from the dropdown at the top of the window.

    {{% imgOld 1 %}}

4.  Enter your username and then your password:  
    - NetQ Platform: *admin, admin* by default  
    - NetQ Appliance: *cumulus, CumulusLinux\!* by default  
    - NetQ Cloud Appliance: Use credentials provided by Cumulus via email titled *Welcome to Cumulus NetQ\!* and accept the terms of use.

      {{< figure src="/images/netq/cumulus-wb-default.png" width="700" >}}

    On your first login, the default Cumulus Workbench opens, with your username shown in the upper right corner of the application. The NetQ Cloud UI has a **Premises** list in the application header, but is otherwise the same. On future logins, the last workbench that you were viewing is displayed.

To log out of the UI:

1.  Click the user icon at the top right of the application.

2.  Select **Log Out**.  

    {{% imgOld 3 %}}
