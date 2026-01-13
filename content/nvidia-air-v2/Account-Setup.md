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
- **Enterprise orgs** support multiple users, teams, and role-based access.

To add other users to your organization, you need an enterprise org. For more information, see {{<exlink url="https://docs.nvidia.com/ngc/latest/ngc-user-guide.html#adding-ngc-users-to-an-org" text="Adding NGC Users to an Org">}}.
{{%/notice%}}

## Log In to Air

1. Go to {{<exlink url="https://air-ngc.nvidia.com" text="air-ngc.nvidia.com">}} and click **Login**.

{{<img src="/images/guides/nvidia-air-v2/air-landing.png" alt="NVIDIA Air landing page" width="800px">}}

2. Enter your business email address and click **Continue**.

{{<img src="/images/guides/nvidia-air-v2/ngc-login.png" alt="NGC login page" width="800px">}}

{{%notice note%}}
You must use a business email address. Personal email addresses (such as gmail.com) are not accepted. If your business email is not accepted and you think this is an error, contact {{<exlink url="mailto:air-support@nvidia.com" text="air-support@nvidia.com">}}.
{{%/notice%}}

3. Select the NGC organization you want to use with Air and click **Continue**.

{{<img src="/images/guides/nvidia-air-v2/ngc-org-select.png" alt="NGC organization selection" width="800px">}}

Air subscriptions and free trials are tied to your NGC organization, not individual users. If you belong to multiple organizations, select the one you want to use for Air simulations.

## Start a Free Trial

If your organization does not have an Air subscription, you may be eligible for a free trial. The trial includes:

| Resource | Enterprise Org | Individual Org |
|----------|----------------|----------------|
| Concurrent vCPUs | 300 | 60 |
| Concurrent memory | 300 GiB | 60 GiB |
| Compute hours | 50,000 | 10,000 |
| Duration | 1 year | 1 year |

Only NGC organization owners can start a free trial. If you are the org owner, Air prompts you to start the trial after you log in:

{{<img src="/images/guides/nvidia-air-v2/free-trial-offer.png" alt="Free trial offer for org owners" width="800px">}}

Click **Start Trial** to activate the free trial for your organization.

{{<img src="/images/guides/nvidia-air-v2/free-trial-success.png" alt="Free trial successfully created" width="800px">}}

If you are not the organization owner, contact your NGC organization admin to start the trial.

## Troubleshooting

### Cannot Start Free Trial

Only NGC organization owners can start a free trial. If you see a prompt to contact your admin:

{{<img src="/images/guides/nvidia-air-v2/free-trial-contact-admin.png" alt="Contact admin to start free trial" width="800px">}}

Click **Contact Organization Admin** to send a request to your NGC organization owner.

### Missing Roles

If your organization has an Air subscription but you cannot access the platform:

{{<img src="/images/guides/nvidia-air-v2/subscription-no-roles.png" alt="Subscription exists but user lacks roles" width="800px">}}

Contact your NGC organization owner to request the appropriate roles for Air access.
