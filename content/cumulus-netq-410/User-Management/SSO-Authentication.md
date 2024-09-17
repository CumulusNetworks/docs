---
title: SSO Authentication
author: NVIDIA
weight: 550
toc: 3
---

You can integrate your NetQ Cloud deployment with a Microsoft Azure Active Directory (AD) or Google Cloud authentication server to support single sign-on (SSO) to NetQ. NetQ supports integration with SAML (Security Assertion Markup Language), OAuth (Open Authorization), and multi-factor authentication (MFA). Only one SSO configuration can be configured at a time.

You can create local accounts with default access roles by enabling SSO. After enabling SSO, users logging in for the first time can {{<link title="Access the NetQ UI" text="sign up for SSO">}} through the NetQ login screen or with a link provided by an admin.

## Add SSO Configuration and Accounts

To integrate your authentication server:

1. Expand the {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/03-Menu/navigation-menu.svg" height="18" width="18" alt="Main Menu">}} **Menu** and select **Management**.

2. Locate the SSO Configuration card and select **Manage**.

3. Select either **SAML** or **OpenID** (which uses OAuth with OpenID Connect).

4. Specify the parameters:

    {{<tabs "TabID468" >}}

{{<tab "OAuth+OpenID Connect" >}}

You need several pieces of data from your Microsoft Azure or Google account and authentication server to complete the integration.

{{<figure src="/images/netq/add-sso-openid.png" alt="sso configuration card with open id configuration" width="600">}}

**SSO Organization** is typically a company's name or a department. The name entered in this field will appear in the SSO signup URL.

**Role** (either user or admin) is automatically assigned when the account is initalized via SSO login.

**Name** is a unique name for the SSO configuration.

**Client ID** is the identifier for your resource server.

**Client Secret** is the secret key for your resource server.

**Authorization Endpoint** is the URL of the authorization application.

**Token Endpoint** is the URL of the authorization token.

After you enter the fields, select **Add**.

As indicated, copy the redirect URI (https://api.netq.nvidia.com/netq/auth/v1/sso-callback) into your OpenID Connect configuration.

    {{<figure src="/images/netq/sso-updated-domain.png" alt="" width="600">}}

  Select **Test** to verify the configuration and ensure that you can log in. If it is not working, you are logged out. Check your specification and retest the configuration until it is working properly.

Select **Close**. The card reflects the configuration:

     {{<figure src="/images/netq/sso-status-disabled.png" alt="sso config card displaying an Open ID configuration with a disabled status" width="200">}}

To require users to log in using this SSO configuration, select **Change** under the "Disabled" status and confirm. The card updates to reflect that SSO is enabled.

After an admin has configured and enabled SSO, users logging in for the first time can {{<link title="Access the NetQ UI" text="sign up for SSO">}}. 

Admins can also provide users with an SSO signup URL: *https://netq.nvidia.com/signup?organization=SSO_Organization*

The SSO organization you entered during the configuration will replace *SSO_Organization* in the URL.

{{</tab>}}

{{<tab "SAML" >}}

You need several pieces of data from your Microsoft Azure or Google account and authentication server to complete the integration.

{{<figure src="/images/netq/add-sso-saml.png" alt="sso configuration card with SAML configuration" width="600">}}

**SSO Organization** is typically a company's name or a department. The name entered in this field will appear in the SSO signup URL.

**Role** (either user or admin) is automatically assigned when the account is initialized via SSO login.

**Name** is a unique name for the SSO configuration.

**Login URL** is the URL for the authorization server login page.

**Identity Provider Identifier** is the name of the authorization server.

**Service Provider Identifier** is the name of the application server.

**Email Claim Key** is an optional field. When left blank, the email address is captured.

After you enter the fields, select **Add**.

As indicated, copy the redirect URI (https://api.netq.nvidia.com/netq/auth/v1/sso-callback) into your OpenID Connect configuration.

    {{<figure src="/images/netq/sso-updated-domain.png" alt="" width="600">}}

Select **Test** to verify the configuration and ensure that you can log in. If it is not working, you are logged out. Check your specification and retest the configuration until it is working properly.

Select **Close**. The card reflects the configuration:

    {{<figure src="/images/netq/sso-status-disabled.png" alt="sso config card displaying a SAML configuration with a disabled status" width="200">}}

To require users to log in using this SSO configuration, select **Change** under the "Disabled" status and confirm. The card updates to reflect that SSO is enabled.

Select **Submit** to enable the configuration. The SSO card reflects the "enabled" status.

After an admin has configured and enabled SSO, users logging in for the first time can {{<link title="Access the NetQ UI" text="sign up for SSO">}}.

Admins can also provide users with an SSO signup URL: *https://netq.nvidia.com/signup?organization=SSO_Organization*

The SSO organization you entered during the configuration will replace *SSO_Organization* in the URL.

{{</tab>}}

    {{</tabs>}}

## Modify Configuration

You can change the specifications for SSO integration with your authentication server at any time, including changing to an alternate SSO type, disabling the existing configuration, or reconfiguring SSO. 

### Change SSO Type

From the SSO Configuration card:

1. Select **Disable**, then **Yes**.

2. Select **Manage** then select the desired SSO type and complete the form.

3. Copy the redirect URL on the success dialog into your identity provider configuration.

4. Select **Test** to verify that the login is working. Modify your specification and retest the configuration until it is working properly.

5. Select **Update**.

### Disable SSO Configuration

From the SSO Configuration card:

1. Select **Disable**.

2. Select **Yes** to disable the configuration, or **Cancel** to keep it enabled.