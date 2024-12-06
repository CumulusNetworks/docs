---
title: Organizations
author: NVIDIA
weight: 50
product: NVIDIA Air
---
{{%notice note%}}
The information on this page reflects the workflows for the new Air UI. The legacy UI is being deprecated. {{<link title="Organizations (Legacy)" text="View documentation for the legacy UI">}}
{{%/notice%}}

NVIDIA Air supports collaboration so that you can share simulations with your colleagues in an organization. When you share a simulation with an organization, each member can edit and view the simulation. To join an organization, contact your organization administrator or your NVIDIA sales team. If you do not know who your organization administrator is, reach out to air-support@nvidia.com.

## Assign Simulations to an Organization

Make sure you are a member of an organization before attempting to assign a simulation to it.

1. From [Simulations](https://air.nvidia.com/simulations), click **Actions {{<img src="/images/guides/nvidia-air/ActionsButton.png" alt="">}} > Edit Simulation**.
2. Select an organization.

{{<img src="/images/guides/nvidia-air/EditSim.png" alt="" width="400px">}}

3. (Optional) Choose a date when the simulation expires and is automatically deleted.
<br>
<br>
Each user with appropriate permissions will now have access to this _exact_ simulation (and not a clone of the simulation). It will appear in their list of available simulations.

{{<img src="/images/guides/nvidia-air/SimulationOrganization.png" alt="" >}}

## Create an Organization

To create an organization, navigate to [air.nvidia.com/organizations](https://air.nvidia.com/organizations).

1. Click **Create Organization**.
2. Give the organization a name.
3. Enter the email addresses of the users you wish to add to the organization. You can select the **Admin** toggle to grant users additional privileges, such as adding additional users.
4. When you are finished adding users, click **Create**. 

{{<img src="/images/guides/nvidia-air/CreateOrganization.png" alt="">}}

## Manage an Organization

Admins can add or remove members, delete or rename organizations, view resource utilization data, and manage [images](#organization-images) for the organization.

{{<img src="/images/guides/nvidia-air/OrganizationMembers.png" alt="">}}

{{%notice info%}}
When you delete an organization, you also delete all the simulations and resources assigned to it. When you remove a member from an organization, their simulations are also removed from the organization.
{{%/notice%}}

## Organization Images

_Public_ images are published for all users of NVIDIA Air, and simulations using public images can be assigned to any organization, or the organization can be left unassigned.

An organization administrator can upload a _private_ image for use in simulations assigned to the organization. Images in an organization can be shared with individual users of NVIDIA Air outside of a particular organization for use in their own simulations.

### Requirements

Images uploaded to an organization have the following requirements:

- Private images in an organization that are not shared must be used in simulations that are assigned to the same organization.
- If you share an image with a user outside of an organization, it is no longer considered private and shared images must be used in simulations with an unassigned organization.
- A simulation can not include both private and shared images.

The following table summarizes the required organization assignment for simulations for each image type and combination used in a simulation:

| Images in Use | Organization Requirements |
| ------ | --------- |
| Public only | Simulations can be assigned to any or no organization | 
| Private only | Simulations must be assigned to the image organization |
| Shared only | Simulations must have an unassigned organization | 
| Private and public | Simulations must be assigned to the image organization |
| Shared and public | Simulations must have an unassigned organization |
| Private and shared | Unsupported |


- To view information about a simulation image for an organization, such as the image size, when the image was created and who uploaded the image, click **Images**. To delete an image, select **Delete** from the actions menu.
