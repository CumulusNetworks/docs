---
title: Premises Management
author: NVIDIA
weight: 500
toc: 2
---

Managing premises involves renaming existing premises or creating multiple premises.
## Configure Multiple Premises

The NetQ Management dashboard lets you configure a single NetQ UI and CLI for monitoring data from multiple premises. This mean you do not need to log in to each premises to view the data.

There are two ways to implement a multi-site, on-premises deployment: either as a full deployment at each premises or as a full deployment at the primary site with a smaller deployment at secondary sites.

**Full NetQ Deployment at Each Premises**<br/>
  In this implementation, there is a NetQ appliance or VM running the NetQ Platform software with a database. Each premises operates independently, with its own NetQ UI and CLI. The NetQ appliance or VM at one of the deployments acts as the primary premises for the premises in the other deployments. A list of these secondary premises is stored with the primary deployment.

{{<figure src="/images/netq/appmgmt-multisite-onprem-fulldeploy-330.png" width="500">}}

**Full NetQ Deployment at Primary Site and Smaller Deployment at Secondary Sites**<br/>
In this implementation, there is a NetQ appliance or VM at one of the deployments acting as the primary premises for the premises in the other deployments. The primary premises runs the NetQ Platform software (including the NetQ UI and CLI) and houses the database. All other deployments are secondary premises; they run the NetQ Controller software and send their data to the primary premises for storage and processing. A list of these secondary premises is stored with the primary deployment.

{{<figure src="/images/netq/appmgmt-multisite-onprem-mixeddeploy-330.png" width="500">}}

After the multiple premises are configured, you can view this list of premises in the NetQ UI at the primary premises, change the name of premises on the list, and delete premises from the list.

To configure secondary premises so that you can view their data using the primary site NetQ UI, follow the instructions for the relevant deployment type of the *secondary* premises.

{{<tabs "Multiple Premises">}}

{{<tab "NetQ Platform">}}

In this deployment model, each NetQ deployment can be installed separately. The data is stored and can be viewed from the NetQ UI at each premises.

To configure a these premises so that their data can be viewed from one premises:

1. On the workbench, under **Premises**, click {{<img src="/images/netq/Down.svg" width="14">}}.

2. Select **Manage Premises**, then **External Premises**.

    {{<figure src="/images/netq/premises-card-external-prems-tab-330.png" width="700">}}

3. Select **Add External Premises**.

    {{<figure src="/images/netq/premises-card-add-external-prems-330.png" width="350">}}

4. Enter the IP address for the API gateway on the NetQ appliance or VM for one of the secondary premises.

5. Enter the access credentials for this host then click **Next**.

6. Select the premises you want to connect then click **Finish**.

    {{<figure src="/images/netq/premises-card-select-external-prems-330.png" width="350">}}

7. Add additional secondary premises by clicking {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/43-Remove-Add/add-circle.svg" height="18" width="18">}}.

{{</tab>}}

{{<tab "NetQ Collector">}}

In this deployment model, the data is stored and can be viewed only from the NetQ UI at the primary premises.

<div class="notices note"><p>The primary NetQ premises must be installed before the secondary premises can be added. For the secondary premises, create the premises here, then install them.</p></div>

1. On the workbench, under **Premises**, click {{<img src="/images/netq/Down.svg" width="14">}}.

2. Click **Manage Premises**. Your primary premises (*OPID0*) is shown by default.

3. Click {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/43-Remove-Add/add-circle.svg" height="18" width="18">}} (Add Premises).

   {{<figure src="/images/netq/premises-create-prem-330.png" width="300">}}

4. Enter the name of one of the secondary premises you want to add, then click **Done**.

   {{<figure src="/images/netq/premises-card-premises-tab-list-330.png" width="700">}}

5. Select the premises you just created.

6. Click {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/04-Login-Logout/login-key-1.svg" height="18" width="18">}} to generate a configuration key.

   {{<figure src="/images/netq/premises-card-premises-tab-generate-key-330.png" width="400">}}

7. Click **Copy** and save the key to a safe place, or click **e-mail** to send it to yourself or other administrator as appropriate. Then click **Done**

{{</tab>}}

{{</tabs>}}

## Rename a Premises

To rename an existing premises:

1. On the workbench, under **Premises**, click {{<img src="/images/netq/Down.svg" width="14">}}, then **Manage Premises**.

1. To rename an external premises, click **External Premises**.

1. On the right side of the screen, select a premises to rename, then click {{<img src="/images/old_doc_images/pencil-2.png" width="16">}}.

1. Enter the new name for the premises, then click **Done**.

   {{<figure src="/images/netq/premises-rename-4.0.0.png" width="400">}}

## System Server Information

To view the physical server or VM configuration:

1. Click menu {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/03-Menu/navigation-menu.svg" height="18" width="18" alt="Main Menu">}}.

2. Under **Admin**, select **Management**.

3. Locate the System Server Info card.

    {{<figure src="/images/netq/netq-mgmt-sys-server-info-card-300.png" width="500">}}

    If no data is present on this card, it is likely that the NetQ Agent on your server or VM is not running properly or the underlying streaming services are impaired.
