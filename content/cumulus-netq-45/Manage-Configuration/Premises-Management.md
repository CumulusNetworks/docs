---
title: Premises Management
author: NVIDIA
weight: 500
toc: 2
---

## Configure Multiple Premises

The NetQ management dashboard lets you configure a single NetQ UI and CLI for monitoring data from multiple premises. This means you do not need to log in to each premises individually to view the data.

There are two ways to implement a multi-site, on-premises deployment: (1) as a full deployment at the primary premises and each of the external premises or (2) as a full deployment at the primary premises with smaller deployments at the secondary premises.

### Full NetQ Deployment at Each Premises

In this implementation, there is a NetQ appliance or VM running the NetQ Platform software with a database. Each premises operates independently as an external premises, with its own NetQ UI and CLI. The NetQ appliance or VM at one of the deployments acts as the primary premises. A list of external premises is stored with the primary deployment.

{{<figure src="/images/netq/appmgmt-multisite-onprem-fulldeploy-330.png" width="600">}}

To configure a single UI to monitor multiple premises:

1. From the UI of the primary premises, select the **Premises** <img src="/images/netq/Down.svg" width="14"> dropdown at the top-right corner of the screen. 

2. Select **Manage premises**, then select the **External premises** tab.

    {{<figure src="/images/netq/add-external-premises.png" width="900">}}

3. Select **Add external premises**.

    {{<figure src="/images/netq/external-premises-credentials.png" width="350">}}

4. Enter the IP address for the external server.

5. Enter the login credentials for the external server, then click **Next**.

6. Select the premises you want to connect, then click **Finish**.

    {{<figure src="/images/netq/additional-external-premises.png" width="350">}}

You can also reduce the number of premises that can be displayed in the UI by hovering over a deployment and selecting <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/23-Delete/bin-1.svg" height="18" width="18"/> Delete.

To view the premises you just added, return to the home workbench and select the **Premises** <img src="/images/netq/Down.svg" width="14"> dropdown at the top-right corner of the screen.


### Full NetQ Deployment at Primary Premises and Smaller Deployment at Secondary Premises

In this implementation, there is a NetQ appliance or VM at one of the deployments acting as the primary premises for the other deployments. The primary premises runs the NetQ software (including the NetQ UI and CLI) and houses the database. All other deployments are secondary premises; they run the NetQ Collector software and send their data to the primary premises for storage and processing. A list of these secondary premises is stored with the primary deployment.

{{<figure src="/images/netq/appmgmt-multisite-onprem-mixeddeploy-330.png" width="500">}}

After the multiple premises are configured, you can view this list of premises in the NetQ UI at the primary premises, change the name of premises on the list, and delete premises from the list.

In this deployment model, the data is stored and can be viewed only from the NetQ UI at the primary premises.

<div class="notices note"><p>The primary NetQ premises must be installed and operational before the secondary premises can be added. </p></div>

1. In the workbench header, select the **Premises** <img src="/images/netq/Down.svg" width="14"> dropdown.

2. Click **Manage premises**. Your primary premises (*OPID0*) is shown by default.

3. Click {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/43-Remove-Add/add-circle.svg" height="18" width="18">}} **Add premises**.

4. Enter the name of a secondary premises you'd like to add, then click **Done**.

5. From the table, select the premises you just created.

6. Click {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/04-Login-Logout/login-key-1.svg" height="18" width="18">}} to generate a configuration key.

7. Click **Copy** and save the key to a safe place, or click **e-mail** to send it to yourself or others. Then click **Done**

## Rename a Premises

To rename an existing premises:

1. In the workbench header, select the **Premises** <img src="/images/netq/Down.svg" width="14"> dropdown, then **Manage premises**.

1. Select a premises to rename, then click {{<img src="/images/old_doc_images/pencil-2.png" width="16">}} Edit.

1. Enter the new name for the premises, then click **Done**.

## System Server Information

To view the physical server or VM configuration:

1. Click <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/03-Menu/navigation-menu.svg" height="18" width="18" alt="Main Menu"> Menu.

2. Under **Admin**, select **Management**.

3. Locate the System Server Info card:

    {{<figure src="/images/netq/system-server-info-card.png" alt="system server info card displaying appliance version, IP address, OS version, and NetQ version" width="500">}}

    If no data is present on this card, it is likely that the NetQ Agent on your server or VM is not running properly or the underlying streaming services are impaired.
