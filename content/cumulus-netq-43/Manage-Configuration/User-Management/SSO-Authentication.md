---
title: SSO Authentication
author: NVIDIA
weight: 550
toc: 3
---

## Integrate with Your Microsoft Azure or Google Cloud for SSO

You can integrate your NetQ Cloud deployment with a Microsoft Azure Active Directory (AD) or Google Cloud authentication server to support single sign-on (SSO) to NetQ. NetQ supports integration with SAML (Security Assertion Markup Language) or OAuth (Open Authorization). Multi-factor authentication (MFA) is also supported. Only one SSO configuration can be configured at a time. You must enable the configuration for the configuration to take effect.

### Configure Support

To integrate your authentication server:

1. Click {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/03-Menu/navigation-menu.svg" height="18" width="18" alt="Main Menu">}}.

2. Select *Management* from the **Admin** column.

3. Locate the SSO Config card.

    {{<figure src="/images/netq/netq-mgmt-sso-card-330.png" width="200">}}

4. Click **Manage**.

5. Click the type of SSO to be integrated:

    - **Open ID**: Choose this option to integrate using OAuth with OpenID Connect
    - **SAML**: Choose this option to integrate using SAML

6. Specify the required parameters.

    You need several pieces of data from your Microsoft Azure or Google account and authentication server to complete the integration. Open your account for easy cut and paste of this data into the NetQ form.

    {{<tabs "TabID468" >}}

{{<tab "OAuth+OpenID Connect" >}}

{{<figure src="/images/netq/netq-mgmt-add-sso-oauth-330.png" width="600">}}

1. Enter your administrator password. This is required when creating a new configuration.

2. Enter a unique name for the SSO configuration.

3. Copy the identifier for your Resource Server into the **Client ID** field.

4. Copy the secret key for your Resource Server into the **Client Secret** field.

5. Copy the URL of the authorization application into the **Authorization Endpoint** field.

6. Copy the URL of the authorization token into the **Token Endpoint** field.

    This example shows a Microsoft Azure AD integration.

    {{<figure src="/images/netq/netq-mgmt-add-sso-oauth-msazure-330.png" width="600">}}

7. Click **Add**.

    {{<figure src="/images/netq/sso-url-41.png" width="600">}}

8. As indicated, copy the redirect URL *https://api.netq.cumulusnetworks.com/netq/auth/v1/sso-callback* into your OpenID Connect configuration.

9. Click **Test** to verify you are sent to the right place and can login. If it is not working, you are logged out. Check your specification and retest the configuration until it is working properly.

10. Click **Close**. The SSO Config card reflects the configuration.

    {{<figure src="/images/netq/netq-mgmt-sso-oauth-config-disabled-330.png" width="200">}}

11. To require users to log in to NetQ using this SSO configuration, click **change** under the current Disabled status.

12. Enter your administrator password.

13. Click **Submit** to enable the configuration. The SSO card reflects this new status.

    {{<figure src="/images/netq/netq-mgmt-sso-oauth-config-enabled-330.png" width="200">}}

{{</tab>}}

{{<tab "SAML" >}}

{{<figure src="/images/netq/netq-mgmt-add-sso-saml-330.png" width="600">}}

1. Enter your administrator password.

2. Enter a unique name for the SSO configuration.

3. Copy the URL for the authorization server login page into the **Login URL** field.

4. Copy the name of the authorization server into the **Identity Provider Identifier** field.

5. Copy the name of the application server into the **Service Provider Identifier** field.

6. Optionally, copy a claim into the **Email Claim Key** field. When left blank, the user email address is captured.

    This example shows a Google Cloud integration.

    {{<figure src="/images/netq/netq-mgmt-add-sso-saml-google-330.png" width="600">}}

7. Click **Add**.

    {{<figure src="/images/netq/netq-mgmt-sso-success-330.png" width="600">}}

8. As indicated, copy the redirect URL *https://api.netq.cumulusnetworks.com/netq/auth/v1/sso-callback* into your identity provider configuration.

9. Click **Test** to verify you are sent to the right place and can login. If it is not working, you are logged out. Check your specification and retest the configuration until it is working properly.

10. Click **Close**. The SSO Config card reflects the configuration.

    {{<figure src="/images/netq/netq-mgmt-sso-saml-config-disabled-330.png" width="200">}}

11. To require users to log in to NetQ using this SSO configuration, click **change** under the current Disabled status.

12. Enter your administrator password.

13. Click **Submit** to enable the configuration. The SSO card reflects this new status.

    {{<figure src="/images/netq/netq-mgmt-sso-saml-config-enabled-330.png" width="200">}}

{{</tab>}}

    {{</tabs>}}

### Modify Integrations

You can change the specifications for SSO integration with your authentication server at any time, including changing to an alternate SSO type, disabling the existing configuration, or reconfiguring the current configuration.

#### Change SSO Type

To choose a different SSO type:

1. Click {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/03-Menu/navigation-menu.svg" height="18" width="18" alt="Main Menu">}}.

2. Select *Management* from the **Admin** column.

3. Locate the SSO Config card.

4. Click **Disable**.

5. Click **Yes**.

6. Click **Manage**.

7. Select the desired SSO type and complete the form with the relevant data for that SSO type.

8. copy the redirect URL on the success dialog into your identity provider configuration.

9. Click **Test** to verify proper login operation. Modify your specification and retest the configuration until it is working properly.

10. Click **Update**.

#### Disable SSO Configuration

To disable the existing SSO configuration:

1. Click {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/03-Menu/navigation-menu.svg" height="18" width="18" alt="Main Menu">}}.

2. Select *Management* from the **Admin** column.

3. Locate the SSO Config card.

4. Click **Disable**.

5. Click **Yes** to disable the configuration, or **Cancel** to keep it enabled.

#### Edit the SSO Configuration

To edit the existing SSO configuration:

1. Click {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/03-Menu/navigation-menu.svg" height="18" width="18" alt="Main Menu">}}.

2. Select *Management* from the **Admin** column.

3. Locate the SSO Config card.

4. Modify any of the fields as needed.

5. Click **Test** to verify proper login operation. Modify your specification and retest the configuration until it is working properly.

6. Click **Update**.