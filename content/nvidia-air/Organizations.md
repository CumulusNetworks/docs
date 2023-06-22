---
title: Organizations
author: NVIDIA
weight: 50
product: NVIDIA Air
---
<!-- vale off -->
NVIDIA Air supports collaboration so that you can share simulations with your colleagues in an organization. To join an organization, contact your Organization Administrator or your NVIDIA sales team. If you do not know who your Organization Administrator is, reach out to air-support@nvidia.com.
<!-- vale on -->
## Assign an Organization to Your Simulation

You can assign each simulation to an organization in which you are a member. All members of the organization can view all assigned simulations.

In the simulation list, the **ORGANIZATION** column shows the organization to which the simulation belongs.

{{<img src="/images/guides/nvidia-air/ManagingSim.png" width="800px">}}

<div style="margin-top: 20px;"></div>

To assign a simulation to an organization, click the **Edit** icon to open the **EDIT SIMULATION** dialog. Select the organization from the **ORGANIZATION** dropdown menu, then click **Submit**.

{{<img src="/images/guides/nvidia-air/EditSim.png" width="400px">}}

## Manage Organizations

If you are an Organization Administrator, you can create and manage organizations, and view details about each organization, such as the list of current members and their roles. You can also view resource utilization for all simulations in the organization.

To see the list of current organizations, click **Organization List** from the **ORGANIZATIONS** dropdown in the sidebar.

{{<img src="/images/guides/nvidia-air/OrgList.png" width="800px">}}

<div style="margin-top: 20px;"></div>

On the Organizations page, you can create and delete organizations, and drill down to see details and manage a specifc organization.

### Create an Organization

To create an organization, click the **Create Organization** button to open the Create Organization dialog.

{{<img src="/images/guides/nvidia-air/AddOrg.png" width="600px">}}

<div style="margin-top: 20px;"></div>

Provide a name for the organization and the email address of each member you want to add. If you want a member to be an administrator, click **ORGANIZATION ADMIN** so that the toggle switch turns green.

### Delete an Organization

To delete an organization, select **Delete** from the actions menu. NVIDIA AIR prompts you to enter the name of the organization to confirm the deletion.

{{%notice info%}}
Deleting an organization also deletes all the simulations and resources assigned to it.
{{%/notice%}}

### View Details and Manage Members

To view details about each organization and to manage members, click the organization link in the **Organization** column on the Organizations page.

The organization details page provides several options.

{{<img src="/images/guides/nvidia-air/OrgDetails.png">}}

<div style="margin-top: 20px;"></div>

- To view usage statistics for an organization, click the **Usage** link. You can see how many simulations are in the organization and how much CPU, memory, and disk storage the organization uses.
- To manage members click the **Members** link.
  - To add a new member, click the **Add Member** button. In the Add Members dialog, provide the email address of the member you want to add. If you want the member to be an administrator, click **ORGANIZATION ADMIN** so that the toggle switch turns green.
  - To edit resource limits for a member such as CPU, memory, and storage and the number of simulations allowed, select **Edit Membership** from the actions menu.
  - To remove a member, select **Remove Member** from the actions menu.

    {{%notice note%}}
Removing a member from an organization also moves all their simulations out of the organization.
{{%/notice%}}

- To view information about a simulation image for an organization, such as the image size, when the image was created and who uploaded the image, click the **Images** link. To delete an image, select **Delete** from the actions menu.
