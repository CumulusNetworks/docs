---
title: Organizations
author: NVIDIA
weight: 50
product: NVIDIA Air
---
NVIDIA Air supports collaboration so that you can share simulations with your colleagues in an Organization. To join an Organization, contact your Organization Administrator or your NVIDIA sales team. 

If you do not know who your Organization Administrator is, reach out to air-support@nvidia.com.

## Assign Simulations to an Organization

To assign a simulation to an Organization:
1. From the [Simulations](https://air.nvidia.com/simulations) homepage, click **Actions {{<img src="/images/guides/nvidia-air/ActionsButton.png" alt="">}} > Edit Simulation** for the sim you wish to assign to an Organization.
2. Assign an Organization. You can only assign an Organization for which you are already a member of.

{{<img src="/images/guides/nvidia-air/EditSim.png" alt="" width="400px">}}

Each user with appropriate permissions will now have access to this _exact_ sim. It will appear in their list of available simulations.

{{<img src="/images/guides/nvidia-air/SimulationOrganization.png" alt="" >}}

## Create an Organization

To create an Organization:
1. Navigate to [air.nvidia.com/organizations](https://air.nvidia.com/organizations).
2. Click Create **Organization**.
3. Give the Organization a **Name**.
4. Enter the email address of a user you wish to add to the Organization.
5. Mark if the user is an **Admin** or not. This will grant admin capabilities for managing the Organization, such as adding more users.
6. Click **Add User**.
7. Add more emails as necessary.
8. Click **Create**. 

{{<img src="/images/guides/nvidia-air/CreateOrganization.png" alt="">}}

## Manage an Organization

You can view, add and remove assigned members, simulations and [images](#organization-images) for the Organization. You can also view utilized resources.

{{<img src="/images/guides/nvidia-air/OrganizationMembers.png" alt="">}}

Rename or delete an Organization with the **Actions {{<img src="/images/guides/nvidia-air/ActionsButton.png" alt="">}} button**.

{{%notice info%}}
Deleting an Organization also deletes all the simulations and resources assigned to it. Removing a member from an Organization also moves all their simulations out of the Organization.
{{%/notice%}}


## Organization Images

_Public_ images are published for all users of NVIDIA Air, and simulations using public images can be assigned to any Organization, or the Organization can be left unassigned.

An Organization Administrator can upload a _private_ image for use in simulations assigned to the Organization. Images in an Organization can be _shared_ with individual users of NVIDIA Air outside of that Organization for use in simulations.

### Requirements

Images uploaded to an Organization have the following requirements:

- Private images in an Organization that are not shared must be used in simulations that are assigned to the same Organization.

- If you share an image with a user outside of an Organization, it is no longer considered private and shared images must be used in simulations with an unassigned Organization.

- A simulation can not include both private and shared images.

The following table summarizes the required Organization assignment for simulations for each image type and combination used in a simulation:

| Images In Use | Organization Requirements |
| ------ | --------- |
| Public only | Simulations can be assigned to any or no Organization | 
| Private only | Simulations must be assigned to the image Organization |
| Shared only | Simulations must have an unassigned Organization | 
| Private and Public | Simulations must be assigned to the image Organization |
| Shared and Public | Simulations must have an unassigned Organization |
| Private and Shared | Unsupported |


- To view information about a simulation image for an Organization, such as the image size, when the image was created and who uploaded the image, click **Images**. To delete an image, select **Delete** from the actions menu.
