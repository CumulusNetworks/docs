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

In the simulation list, the **Organization** column shows the organization to which the simulation belongs.

{{<img src="/images/guides/nvidia-air/ManagingSim.png" alt="" width="800px">}}

<div style="margin-top: 20px;"></div>

To assign a simulation to an organization, click the **Edit** icon to open the **Edit Simulation** dialog. Select the organization from the **Organization** dropdown menu, then click **Submit**.

{{<img src="/images/guides/nvidia-air/EditSim.png" alt="" width="400px">}}

## Organizations and Images

_Public_ images are published for all users of NVIDIA Air, and simulations using public images can be assigned to any organization, or the organization can be left unassigned.

An Organization Administrator can upload a _private_ image for use in simulations assigned to the organization. Images in an organization can be _shared_ with individual users of NVIDIA Air outside of that organization for use in simulations.

### Requirements

Images uploaded to an organization have the following requirements:

- Private images in an organization that are not shared must be used in simulations that are assigned to the same organization.

- If you share an image with a user outside of an organization, it is no longer considered private and shared images must be used in simulations with an unassigned organization.

- A simulation can not include both private and shared images.

The following table summarizes the required organization assignment for simulations for each image type and combination used in a simulation:

| Images In Use | Organization Requirements |
| ------ | --------- |
| Public only | Simulations can be assigned to any or no organization | 
| Private only | Simulations must be assigned to the image organization |
| Shared only | Simulations must have an unassigned organization | 
| Private and Public | Simulations must be assigned to the image organization |
| Shared and Public | Simulations must have an unassigned organization |
| Private and Shared | Unsupported |

## Manage Organizations

If you are an Organization Administrator, you can create and manage organizations, and view details about each organization, such as the list of current members and their roles. You can also view resource utilization for all simulations in the organization.

To see the list of current organizations, click **Organization List** from the **Organizations** dropdown in the sidebar.

{{<img src="/images/guides/nvidia-air/OrgList.png" alt="organization list with options to create or delete an organization" width="800px">}}

<div style="margin-top: 20px;"></div>

On the Organizations page, you can create and delete organizations, and drill down to see details and manage a specific organization.

### Create an Organization

To create an organization, select **Create Organization**.

{{<img src="/images/guides/nvidia-air/AddOrg.png" alt="" width="600px">}}

<div style="margin-top: 20px;"></div>

Provide a name for the organization and the email address of each member you want to add. If you want a member to be an administrator, select the **Organization Admin** toggle.

### Delete an Organization

To delete an organization, select **Delete** from the actions menu. NVIDIA AIR prompts you to enter the name of the organization to confirm the deletion.

{{%notice info%}}
Deleting an organization also deletes all the simulations and resources assigned to it.
{{%/notice%}}

### View Details and Manage Members

To view details about each organization and to manage members, click the organization link in the **Organization** column on the Organizations page.

The organization details page provides several options.

{{<img src="/images/guides/nvidia-air/OrgDetails.png" alt="organizations dashboard with options to manage users and images">}}

<div style="margin-top: 20px;"></div>

- To view usage statistics for an organization, select **Usage**. You can see how many simulations are in the organization and how much CPU, memory, and disk storage the organization uses.
- To manage members select **Members**.
  - To add a new member, click **Add Member**, then provide the email address of the member you want to add. If you want the member to be an administrator, select the **Organization Admin** toggle.
  - To edit resource limits for a member such as CPU, memory, and storage and the number of simulations allowed, select **Edit Membership** from the actions menu.
  - To remove a member, select **Remove Member** from the actions menu.

    {{%notice note%}}
Removing a member from an organization also moves all their simulations out of the organization.
{{%/notice%}}

- To view information about a simulation image for an organization, such as the image size, when the image was created and who uploaded the image, click **Images**. To delete an image, select **Delete** from the actions menu.
