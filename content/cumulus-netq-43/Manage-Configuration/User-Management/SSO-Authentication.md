---
title: SSO Authentication
author: NVIDIA
weight: 550
toc: 3
---

You can integrate your NetQ Cloud deployment with a Microsoft Azure Active Directory (AD) or Google Cloud authentication server to support single sign-on (SSO) to NetQ. NetQ supports integration with SAML (Security Assertion Markup Language), OAuth (Open Authorization), and multi-factor authentication (MFA). Only one SSO configuration can be configured at a time.

## Add SSO Configuration and User Accounts

To integrate your authentication server:

1. Expand the menu {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/03-Menu/navigation-menu.svg" height="18" width="18" alt="Main Menu">}} on the NetQ dashboard.

2. Under **Admin**, select **Management**. Locate the SSO Configuration card and select **Manage**.

    {{<figure src="/images/netq/netq-mgmt-sso-card-330.png" alt="" width="200">}}

3. Select either **SAML** or **OpenID** (which uses OAuth with OpenID Connect)

4. Specify the parameters:

    {{<tabs "TabID468" >}}

{{<tab "OAuth+OpenID Connect" >}}

You need several pieces of data from your Microsoft Azure or Google account and authentication server to complete the integration.

{{<figure src="/images/netq/add-sso-openid.png" alt="sso configuration card with open id configuration" width="600">}}

**SSO Organization** is the name your users will enter to log in with SSO. You can configure login from here and specify the access type (either user or admin).

**Name** is a unique name for the SSO configuration.

**Client ID** is the identifier for your resource server.

**Client Secret** is the secret key for your resource server.

**Authorization Endpoint** is the URL of the authorization application.

**Token Endpoint** is the URL of the authorization token.

After you enter the fields, select **Add**.

    {{<figure src="/images/netq/sso-url-41.png" width="600">}}

As indicated, copy the redirect URL *https://api.netq.cumulusnetworks.com/netq/auth/v1/sso-callback* into your OpenID Connect configuration.

  Select **Test** to verify you are sent to the correct place and can log in. If it is not working, you are logged out. Check your specification and retest the configuration until it is working properly.

Select **Close**. The card reflects the configuration.

    {{<figure src="/images/netq/netq-mgmt-sso-oauth-config-disabled-330.png" alt="sso config card displaying an open id configuration with a disabled status" width="200">}}

To require users to log in using this SSO configuration, select **change** under the current Disabled status and confirm. The card reflects that SSO is enabled.

    {{<figure src="/images/netq/netq-mgmt-sso-oauth-config-enabled-330.png" alt="sso configuration card with enabled status" width="200">}}

{{</tab>}}

{{<tab "SAML" >}}

You need several pieces of data from your Microsoft Azure or Google account and authentication server to complete the integration.

{{<figure src="/images/netq/add-sso-saml.png" alt="sso configuration card with SAML configuration" width="600">}}

**SSO Organization** is the name your users will enter to log in with SSO. You can configure login from here and specify the access type (either user or admin).

**Name** is a unique name for the SSO configuration.

**Login URL** is the URL for the authorization server login page.

**Identity Provider Identifier** is the name of the authorization server.

**Service Provider Identifier**  is the name of the application server.

**Email Claim Key** is an optional field. When left blank, the user email address is captured.

After you enter the fields, select **Add**.

    {{<figure src="/images/netq/netq-mgmt-sso-success-330.png" width="600">}}

As indicated, copy the redirect URL *https://api.netq.cumulusnetworks.com/netq/auth/v1/sso-callback* into your identity provider configuration.

Select **Test** to verify you are sent to the right place and can log in. If it is not working, you are logged out. Check your specification and retest the configuration until it is working properly.

Select **Close**. The card reflects the configuration.

    {{<figure src="/images/netq/netq-mgmt-sso-saml-config-disabled-330.png" alt="sso config card displaying a SAML configuration with a disabled status" width="200">}}

To require users to log in using this SSO configuration, select **change** under the current Disabled status and confirm. The card reflects that SSO is enabled.

Select **Submit** to enable the configuration. The SSO card reflects this new status.

    {{<figure src="/images/netq/netq-mgmt-sso-saml-config-enabled-330.png" width="200">}}

{{</tab>}}

    {{</tabs>}}

## Modify Configuration

You can change the specifications for SSO integration with your authentication server at any time, including changing to an alternate SSO type, disabling the existing configuration, or reconfiguring the current configuration.

### Change SSO Type

To choose a different SSO type:

1. Expand the menu {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/03-Menu/navigation-menu.svg" height="18" width="18" alt="Main Menu">}} on the NetQ dashboard.

2. Under **Admin**, select **Management**.

3. Locate the SSO Config card and click **Disable**, then **Yes**.

4. Click **Manage** then select the desired SSO type and complete the form.

8. Copy the redirect URL on the success dialog into your identity provider configuration.

9. Click **Test** to verify proper login operation. Modify your specification and retest the configuration until it is working properly.

10. Click **Update**.

### Disable SSO Configuration

To disable the existing SSO configuration:

1. Expand the menu {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/03-Menu/navigation-menu.svg" height="18" width="18" alt="Main Menu">}} on the NetQ dashboard.

2. Under **Admin**, select **Management**.

3. Locate the SSO Config card.

4. Click **Disable**.

5. Click **Yes** to disable the configuration, or **Cancel** to keep it enabled.