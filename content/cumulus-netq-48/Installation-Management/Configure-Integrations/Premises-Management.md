---
title: Configure Premises
author: NVIDIA
weight: 500
toc: 2
---

The NetQ management dashboard lets you configure a single NetQ UI and CLI for monitoring data from multiple premises. This means you do not need to log in to each premises individually to view the data.
## Configure Multiple Premises

There are two ways to implement a multi-site, on-premises deployment: (1) as a full deployment at the primary premises and each of the external premises or (2) as a full deployment at the primary premises with smaller deployments at the secondary premises. 

<div class="notices note"><p>The primary premises is called OPID0 by default in the UI. </p></div>

### Full NetQ Deployment at Each Premises

In this implementation, there is a NetQ appliance or VM running the NetQ software with a database. Each premises operates independently as an external premises, with its own NetQ UI and CLI. The NetQ appliance or VM at one of the deployments acts as the primary premises. A list of external premises is stored with the primary deployment.

{{<figure src="/images/netq/appmgmt-multisite-onprem-fulldeploy-330.png" alt="" width="600">}}

To configure a single UI to monitor multiple premises:

1. From the UI of the primary premises (OPID0), select the **Premises** {{<img src="/images/netq/Down.svg" width="14">}} dropdown in the top-right corner of the screen. 

2. Select **Manage premises**, then select the **External premises** tab.

3. Select **Add external premises**.

    {{<figure src="/images/netq/external-premises-490.png" alt="" width="900">}}

4. Enter the IP address for the external server, your username, and password. The username and password are the same credentials used to log in to the UI for the external server. Select **Next**

    {{<figure src="/images/netq/external-premises-credentials.png" alt="dialog prompting the user to enter the external server's IP and credentials" width="350">}}

5. Select the premises you want to connect, then click **Finish**.

    {{<figure src="/images/netq/additional-external-premises.png" alt="dialog displaying two premises" width="350">}}

You can also reduce the number of premises that can be displayed in the UI by hovering over a deployment and selecting {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/23-Delete/bin-1.svg" height="18" width="18">}} **Delete**.

To view the premises you just added, return to the home workbench and select the **Premises** {{<img src="/images/netq/Down.svg" width="14">}} dropdown in the top-right corner of the screen. Alternately, run the {{<link title="config/#netq-config-show-cli-premises" text="netq config show cli premises">}} command.


### Full NetQ Deployment at Primary Premises and Smaller Deployments at Secondary Premises

In this implementation, there is a NetQ appliance or VM at one of the deployments acting as the primary premises for the other deployments. The primary premises runs the NetQ software (including the NetQ UI and CLI) and houses the database. All other deployments are secondary premises; they run the NetQ cloud software and send their data to the primary premises for storage and processing. A list of these secondary premises is stored with the primary deployment.

{{<figure src="/images/netq/appmgmt-multisite-onprem-mixeddeploy-330.png" alt="" width="500">}}

After the multiple premises are configured, you can view this list of premises in the NetQ UI at the primary premises, change the name of premises on the list, and delete premises from the list.

In this deployment model, the data is stored and can be viewed only from the NetQ UI at the primary premises.

<div class="notices note"><p>The primary NetQ premises must be installed and operational before the secondary premises can be added. </p></div>

To create and add secondary premises:

1. In the workbench header, select the **Premises** {{<img src="/images/netq/Down.svg" width="14">}} dropdown.

2. Click **Manage premises**. Your primary premises (OPID0) is shown by default.

3. Click {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/43-Remove-Add/add-circle.svg" height="18" width="18">}} **Add premises**.

{{<figure src="/images/netq/create-new-premises.png" alt="" width="350">}}

4. Enter the name of a secondary premises you'd like to add, then click **Done**.

5. From the confirmation dialog, select **View config key**.

{{<figure src="/images/netq/premises-view-config-key.png" alt="" width="350">}}

6. Click the copy icon, then save the key to a safe place, or click **e-mail** to send it to yourself or others. Then click **Confirm activation**.

{{<figure src="/images/netq/new-premises-config-key.png" alt="dialog displaying configuration key with options to copy or share the key" width="650">}}

To view the premises you just added, return to the home workbench and select the **Premises** {{<img src="/images/netq/Down.svg" width="14">}} dropdown at the top-right corner of the screen. Alternately, run the {{<link title="config/#netq-config-show-cli-premises" text="netq config show cli premises">}} command.

## Rename a Premises

To rename an existing premises:

1. In the workbench header, select the **Premises** {{<img src="/images/netq/Down.svg" width="14">}} dropdown, then **Manage premises**.

1. Select a premises to rename, then click {{<img src="/images/old_doc_images/pencil-2.png" width="16">}} **Edit**.

1. Enter the new name for the premises, then click **Done**.

4. (Optional) {{<link title="Install NetQ CLI/#configure-the-netq-cli" text="Reconfigure the NetQ CLI">}} by generating new AuthKeys. You must complete this step after renaming a premises for the CLI to be functional.

## Related Information

- {{<link title="Focus Your Monitoring Using Workbenches" text="Focus Your Monitoring Using Workbenches">}}

<!--Need to find new place for this

## System Server Information

To view the physical server or VM configuration:

1. Click {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/03-Menu/navigation-menu.svg" height="18" width="18" alt="Main Menu">}} Menu.

2. Under **Admin**, select **Management**.

3. Locate the System Server Info card:

    {{<figure src="/images/netq/system-server-info-card.png" alt="system server info card displaying appliance version, IP address, OS version, and NetQ version" width="500">}}

    If no data is present on this card, it is likely that the NetQ Agent on your server or VM is not running properly, or the underlying streaming services are impaired.

-->