---
title: Account Setup
author: NVIDIA
weight: 15
product: NVIDIA Air 2.0
---

NVIDIA Air uses {{<exlink url="https://docs.nvidia.com/ngc/latest/ngc-user-guide.html" text="NVIDIA NGC">}} for authentication and organization management.

## Prerequisites

To use Air, you need an NGC account and organization.

If you do not have an NGC account, go to {{<exlink url="https://ngc.nvidia.com/signin" text="ngc.nvidia.com">}} and follow the prompts to create an NVIDIA Cloud Account (NCA) and organization. For detailed instructions, refer to the {{<exlink url="https://docs.nvidia.com/ngc/latest/ngc-user-guide.html#ngc-org-owner-users" text="NGC User Guide">}}.

{{%notice note%}}
- **Individual orgs** are single-user only.
- **Enterprise orgs** support multiple users, teams, and role-based access. This plan is available to paying customers. Contact your NVIDIA sales representative for more information.



To add additional users to your organization, you need an enterprise org. For more information, see {{<exlink url="https://docs.nvidia.com/ngc/latest/ngc-user-guide.html#adding-ngc-users-to-an-org" text="Adding NGC Users to an Org">}}.
{{%/notice%}}

## Log In to Air

1. Go to {{<exlink url="https://air-ngc.nvidia.com" text="air-ngc.nvidia.com">}} and click **Login**.

{{<img src="/images/guides/nvidia-air-v2/air-landing.png" alt="NVIDIA Air landing page" width="800px">}}

2. Enter your business email address and click **Continue**.

{{<img src="/images/guides/nvidia-air-v2/ngc-login.png" alt="NGC login page" width="800px">}}

{{%notice note%}}
You must use a business email address. Personal email addresses (such as gmail.com) are not accepted. If your business email is not accepted and you think this is in error, contact {{<exlink url="mailto:air-support@nvidia.com" text="air-support@nvidia.com">}}.
{{%/notice%}}

3. Select the NGC organization you want to use with Air and click **Continue**.

{{<img src="/images/guides/nvidia-air-v2/ngc-org-select.png" alt="NGC organization selection" width="800px">}}

Air subscriptions and free trials are tied to your NGC organization, not individual users. If you belong to multiple organizations, select the one you want to use for Air simulations.

## Start a Free Trial

If your organization does not have an Air subscription, you may be eligible for a free trial. The trial includes:

| Resource | Individual Org |
|----------|----------------|
| Concurrent vCPUs | 60 |
| Concurrent memory | 60 GiB |
| Compute hours (credits) | 10,000 |
| Duration | 1 year |

Only NGC organization owners can start a free trial. If you are the org owner, Air prompts you to start the trial after you log in:

{{<img src="/images/guides/nvidia-air-v2/free-trial-offer.png" alt="Free trial offer for org owners" width="800px">}}

Click **Start Trial** to activate the free trial for your organization. If you are not the organization owner, contact your NGC organization admin to start the trial.

## Add a User and Assign Roles

To access NVIDIA Air, each user in your organization must have at least one of the following roles assigned at the organization level:

- **Air Org Admin**
- **Air User**

To add a new user to your organization, go to {{<exlink url="https://org.ngc.nvidia.com/users" text="org.ngc.nvidia.com/users">}} and click **Add a user**.

{{%notice warning%}}
Always add users through the NGC org management page linked above. Do not invite users through the NVIDIA Cloud Account (NCA) page. Users invited through NCA may not appear correctly in NGC, which prevents you from assigning roles.
{{%/notice%}}

To assign roles to an existing user:

1. Go to {{<exlink url="https://org.ngc.nvidia.com/users" text="org.ngc.nvidia.com/users">}}.
2. Find the user and edit their membership.
3. Under **Step 2: Assign Permissions to New User**, select **Organization** as the context for role assignment.
4. Under **NVIDIA Air**, select **Air Org Admin**, **Air User**, or both, then click **Add Role**.

{{<img src="/images/guides/nvidia-air-v2/assign-air-roles.png" alt="Assign Air roles to a user" width="600px">}}

## Troubleshooting

### Cannot Start Free Trial

Only NGC organization owners can start a free trial. If you see a prompt to contact your admin:

{{<img src="/images/guides/nvidia-air-v2/free-trial-contact-admin.png" alt="Contact admin to start free trial" width="800px">}}

Click **Contact Organization Admin** to send a request to your NGC organization owner.

### Missing Roles

If your organization has an Air subscription but you cannot access the platform:

{{<img src="/images/guides/nvidia-air-v2/subscription-no-roles.png" alt="Subscription exists but user lacks roles" width="800px">}}

Contact your NGC organization owner and direct them to [Add a User and Assign Roles](#add-a-user-and-assign-roles) to request the appropriate roles for Air access.
