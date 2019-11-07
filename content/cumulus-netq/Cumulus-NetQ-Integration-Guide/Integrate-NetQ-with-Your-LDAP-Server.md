---
title: Integrate NetQ with Your LDAP Server
author: Cumulus Networks
weight: 201
aliases:
product: Cumulus NetQ
version: 2.3
imgData: cumulus-netq
---
With this release and an administrator role, you are able to integrate the NetQ role-based access control (RBAC) with your lightweight directory access protocol (LDAP) server in on-premises deployments. NetQ maintains control over role-based permissions for the NetQ application. Currently there are two roles, admin and user. With the integration, user authentication is handled through LDAP and your directory service, such as Microsoft Active Directory, Kerberos, OpenLDAP, and Red Hat Directory Service. A copy of each user from LDAP is stored in the local NetQ database.

Integrating with an LDAP server does not prevent you from configuring local users (stored and managed in the NetQ database) as well.

Read the Overview to become familiar with LDAP configuration parameters, or skip to [Create an LDAP Configuration](#create-an-ldap-configuration) if you are already an LDAP expert.

## Overview

LDAP integration requires information about how to connect to your LDAP server, the type of authentication you plan to use, bind credentials, and, optionally, search attributes.

### Provide Your LDAP Server Information

To connect to your LDAP server, you need the URI and bind credentials. The URI identifies the location of the LDAP server. It is comprised of a  FQDN (fully qualified domain name) or IP address, and the port of the LDAP server where the LDAP client can connect. For example: ldaps://myldap.mycompany.com or ldap://192.168.10.2. Typically port 389 is used for connection over TCP or UDP. In production environments, a secure connection with SSL or TLS is typically deployed. In this case,  the port used is typically 636.

### Specify Your Authentication Method

Three methods of user authentication are available:

- **Anonymous**: LDAP client does not require any authentication. The user can access all resources anonymously. This is not commonly used for production environments.
- **Basic**: (Also called Simple) LDAP client must provide a bind user and password to authenticate the connection. For NetQ, the bind user is the Admin distinguished name (DN) and password is the Admin password. It is sent as clear text. Only users with these credentials are allowed to perform LDAP operations.
- **SASL**: Not implemented. Please select an alternate method.

If you are unfamiliar with the configuration of your LDAP server, contact your administrator to ensure you select the appropriate authentication method and credentials.

### Define User Attributes

Three attributes are required to define a user entry in a directory. The DNs are defined using a string of variables. Some common variables include:

- ou=\<organization-or-group\>, 
- dc=\<domain-name\>, 
- dc=\<domain-extension\>
- cn=\<common-name\>

- **Bind DN**: DN used for binding with the LDAP server. For NetQ, the bind DN is based on the User ID plus other variables that you specify. The Bind DN=`{userIdAttribute}={userId},ou=ntwkops,dc=mycompany,dc=com`, where{userIdAttribute} should be replaced with the value specified in User ID field. For example, uid={userId},ou=ntwkops,dc=mycompany,dc=com.
- **User ID**: Type of identifier used to specify an LDAP user. This can vary depending on the authentication service you are using. For example,  user ID (UID) or email address  could be used with OpenLDAP, whereas sAMAccountName might be used with Active Directory.  For example, 
    - If the User ID type is `UID`, then the {user-id} in the Bind DN could accept jsmith, janed, or user.man
    - If the User ID type is `email`, then the {user-id} in the Bind DN could accept jsmith,dc=mycompany,dc=com
    - If the User ID type is `sAMAccountName`, than the {user-id} in the Bind DN could accept clientA
- **Base DN**: Location in directory structure where search begins. For example, `dc=mycompany,dc=com`

Optionally you can also specify the user's first name, last name, and email address.

### Set Search Attributes

While optional, specifying search scope indicates where to start and how deep a given user can search within the directory. The data to search for is specified in the search query.

Search scope options include:

- **None**: Not implemented. Please select an alternate scope.
- **Base**: Search for users at the base level only; no subordinates
- **One Level**: Search for immediate children of user; not at base or for any descendants
- **Subtree**: Search for users from base, subordinates at any depth
- **Subordinate**: Search for subordinates at any depth of user; but not at base

A typical search query for users would be `{userIdAttribute}={userId}`.

Now that you are familiar with the various LDAP configuration parameters, you can configure the integration of your LDAP server with NetQ using the instructions in the next section.

## Create an LDAP Configuration

One LDAP server can be configured per bind DN (distinguished name). Once LDAP is configured, you can validate the connectivity (and configuration) and save the configuration. 

To create an LDAP configuration:

1. Click <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/03-Menu/navigation-menu.svg", width="18", height="18"/>, then select *Management* under **Admin**.

2. Locate the LDAP Server Info card, and click **Configure LDAP**.

    {{<figure src="/images/netq/netq-mgmt-ldap-config-modal-230.png" width="500">}}

3. Fill out the LDAP Server Configuration form according to your particular configuration. Refer to [Overview](#overview) for details about the various parameters.

    **Note**: Items with an asterisk (*) are required. All others are optional.

4. Click **Save** to complete the configuration, or click **Cancel** to discard the configuration.

{{%notice info%}}
LDAP config cannot be changed once configured. If you need to change the configuration, you must delete the current LDAP configuration and create a new one. Note that if you change the LDAP server configuration, all users created against that LDAP server remain in the NetQ database and continue to be visible, but are no longer viable. You must manually delete those users if you do not want to see them.
{{%/notice%}}

## Example LDAP Configurations

A variety of example configurations are provided here.

### Scenario 1:  Anonymous Authentication, User ID=email, Base Search

| Parameter | Value |
| ------------- |  ------ |
| Host Server URL | ldap://ldap1.mycompany.com |
| Host Server Port | 389 |
| Authentication | Anonymous |
| Bind DN | {userIdAttribute}={userId},dc=mycompany,dc=com |
| Base DN | dc=mycompany,dc=com |
| User ID | email |
| Search Scope | Base |
| Search Query | {userIdAttribute}={userId} |

### Scenario 2: Basic authentication, Network Operator Users, One Level Search

| Parameter | Value |
| ------------- |  ------ |
| Host Server URL | ldaps://ldap1.mycompany.com |
| Host Server Port | 636 |
| Authentication | Basic |
| Admin DN | cn=cumulusnq,ou=netops |
| Admin Password | nqldap! |
| Bind DN | {userIdAttribute}={userId},ou=netops,dc=mycompany,dc=com |
| Base DN | dc=mycompany,dc=com |
| User ID | UID |
| Search Scope | One Level |
| Search Query | {userIdAttribute}={userId} |

### Scenario 3: SASL Authentication, Network Administrator Users, Subtree Search, OpenLDAP service

| Parameter | Value |
| ------------- |  ------ |
| Host Server URL | ldaps://192.168.10.2 |
| Host Server Port | 636 |
| Authentication | SASL |
| Admin DN | cn=cumulus,ou=netadmin |
| Admin Password | 1dap*netq |
| Bind DN | {userIdAttribute}={userId},ou=netadmin,dc=mycompany,dc=com |
| Base DN | dc=mycompany, dc=net |
| User ID | UID |
| Search Scope | Subtree |
| Search Query | userIdAttribute}={userId} |

### Scenario 4: SASL Authentication, Network Administrator Users, Subtree Search, Active Directory service

| Parameter | Value |
| ------------- |  ------ |
| Host Server URL | ldaps://192.168.10.2 |
| Host Server Port | 636 |
| Authentication | SASL |
| Admin DN | cn=cumulusnq,ou=netadmin |
| Admin Password | nq&4mAd! |
| Bind DN | {userId}@mycompany.com |
| Base DN | dc=mycompany, dc=net |
| User ID | sAMAccountName |
| Search Scope | Subtree |
| Search Query | {userIdAttribute}={userId} |


## Add LDAP Users to NetQ

1. Click <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/03-Menu/navigation-menu.svg", width="18", height="18"/>, then select *Management* under **Admin**.

2. Locate the User Accounts card, and click **Manage**.

3. On the User Accounts tab, click **Add User**.

    {{<figure src="/images/netq/netq-mgmt-user-acct-add-new-user-modal-230.png" width="250">}}

4. Select **LDAP User**.

5. Enter the user's ID.

6. Enter your administrator password. 

7. Click **Search**.

8. If the user is found, the email address, first and last name fields are automatically filled in on the Add New User form. If searching is not enabled on the LDAP server, you must enter the information manually.

    {{<figure src="/images/netq/netq-mgmt-user-acct-ldap-search-result-230.png" width="300">}}

    {{%notice tip%}}
If the fields are not automatically filled in, and searching is enabled on the LDAP server, you might require changes to the mapping file.
    {{%/notice%}}

9. Select the role for this user, *admin* or *user*, in the **User Type** dropdown.

10. Enter your admin password, and click **Save**, or click **Cancel** to discard the user account.

    {{<figure src="/images/netq/netq-mgmt-user-acct-fullscr-added-user-230.png" width="700">}}

    {{%notice tip%}}

LDAP user passwords are not stored in the NetQ database and are always authenticated against LDAP.

    {{%/notice%}}

11. Repeat these steps to add additional LDAP users.

## Remove LDAP Users from NetQ

You can remove LDAP users in the same manner as local users.

1. Click <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/03-Menu/navigation-menu.svg", width="18", height="18"/>, then select *Management* under **Admin**.

2. Locate the User Accounts card, and click **Manage**.

3. Select the user or users you want to remove.

4. Click <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/23-Delete/bin-1.svg", width="18", height="18"/> in the Edit menu.

{{%notice tip%}}
If an LDAP user is deleted in LDAP it is not automatically deleted from NetQ; however, the login credentials for these LDAP users stop working immediately.
{{%/notice%}}