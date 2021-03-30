---
title: Integrate NetQ with Your LDAP Server
author: Cumulus Networks
weight: 540
toc: 3
---
With this release and an administrator role, you are able to integrate the NetQ role-based access control (RBAC) with your lightweight directory access protocol (LDAP) server in on-premises deployments. NetQ maintains control over role-based permissions for the NetQ application. Currently there are two roles, admin and user. With the integration, user authentication is handled through LDAP and your directory service, such as Microsoft Active Directory, Kerberos, OpenLDAP, and Red Hat Directory Service. A copy of each user from LDAP is stored in the local NetQ database.

Integrating with an LDAP server does not prevent you from configuring local users (stored and managed in the NetQ database) as well.

Read Get Started to become familiar with LDAP configuration parameters, or skip to {{<link title="#Create an LDAP Configuration" text="Create an LDAP Configuration">}} if you are already an LDAP expert.

## Get Started

LDAP integration requires information about how to connect to your LDAP server, the type of authentication you plan to use, bind credentials, and, optionally, search attributes.

### Provide Your LDAP Server Information

To connect to your LDAP server, you need the URI and bind credentials. The URI identifies the location of the LDAP server. It is comprised of a  FQDN (fully qualified domain name) or IP address, and the port of the LDAP server where the LDAP client can connect. For example: myldap.mycompany.com or 192.168.10.2. Typically port 389 is used for connection over TCP or UDP. In production environments, a secure connection with SSL can be deployed. In this case, the port used is typically 636. Setting the **Enable SSL** toggle automatically sets the server port to 636.

### Specify Your Authentication Method

Two methods of user authentication are available: anonymous and basic.

- **Anonymous**: LDAP client does not require any authentication. The user can access all resources anonymously. This is not commonly used for production environments.
- **Basic**: (Also called Simple) LDAP client must provide a bind DN and password to authenticate the connection. When selected, the **Admin** credentials appear: Bind DN and Bind Password. The distinguished name (DN) is defined using a string of variables. Some common variables include:

    | Syntax | Description or Usage |
    | -------- | -------------------------- |
    | cn | Common name |
    | ou | Organizational unit or group |
    | dc | Domain name |
    | dc | Domain extension |
    
    - **Bind DN**: DN of user with administrator access to query the LDAP server; used for binding with the server. For example, `uid =admin,ou=ntwkops,dc=mycompany,dc=com`.
    - **Bind Password**: Password associated with Bind DN.

    The Bind DN and password are sent as clear text. Only users with these credentials are allowed to perform LDAP operations.

If you are unfamiliar with the configuration of your LDAP server, contact your administrator to ensure you select the appropriate authentication method and credentials.

### Define User Attributes

Two attributes are required to define a user entry in a directory:

- **Base DN**: Location in directory structure where search begins. For example, `dc=mycompany,dc=com`.
- **User ID**: Type of identifier used to specify an LDAP user. This can vary depending on the authentication service you are using. For example,  user ID (UID) or email address can be used with OpenLDAP, whereas sAMAccountName might be used with Active Directory.

Optionally, you can specify the first name, last name, and email address of the user.

### Set Search Attributes

While optional, specifying search scope indicates where to start and how deep a given user can search within the directory. The data to search for is specified in the search query.

Search scope options include:

- **Subtree**: Search for users from base, subordinates at any depth (default)
- **Base**: Search for users at the base level only; no subordinates
- **One Level**: Search for immediate children of user; not at base or for any descendants
- **Subordinate**: Search for subordinates at any depth of user; but not at base

A typical search query for users would be *{userIdAttribute}={userId}*.

Now that you are familiar with the various LDAP configuration parameters, you can configure the integration of your LDAP server with NetQ using the instructions in the next section.

## Create an LDAP Configuration

One LDAP server can be configured per bind DN (distinguished name). Once LDAP is configured, you can validate the connectivity (and configuration) and save the configuration.

To create an LDAP configuration:

1. Click <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/03-Menu/navigation-menu.svg" width="18" height="18"/>, then select *Management* under **Admin**.

2. Locate the LDAP Server Info card, and click **Configure LDAP**.

    {{<figure src="/images/netq/netq-mgmt-ldap-config-modal-231.png" width="500">}}

3. Fill out the LDAP Server Configuration form according to your particular configuration. Refer to {{<link title="#Overview" text="Overview">}} for details about the various parameters.

    **Note**: Items with an asterisk (*) are required. All others are optional.

4. Click **Save** to complete the configuration, or click **Cancel** to discard the configuration.

{{%notice info%}}
LDAP config cannot be changed once configured. If you need to change the configuration, you must delete the current LDAP configuration and create a new one. Note that if you change the LDAP server configuration, all users created against that LDAP server remain in the NetQ database and continue to be visible, but are no longer viable. You must manually delete those users if you do not want to see them.
{{%/notice%}}

## Example LDAP Configurations

A variety of example configurations are provided here. Scenarios 1-3 are based on using an OpenLDAP or similar authentication service. Scenario 4 is based on using the Active Directory service for authentication.

### Scenario 1: Base Configuration

In this scenario, we are configuring the LDAP server with anonymous authentication, a User ID based on an email address, and a search scope of base.

| Parameter | Value |
| ------------- |  ------ |
| Host Server URL | ldap1.mycompany.com |
| Host Server Port | 389 |
| Authentication | Anonymous |
| Base DN | dc=mycompany,dc=com |
| User ID | email |
| Search Scope | Base |
| Search Query | {userIdAttribute}={userId} |

### Scenario 2: Basic Authentication and Subset of Users

In this scenario, we are configuring the LDAP server with basic authentication, for access only by the persons in the network operators group, and a limited search scope.

| Parameter | Value |
| ------------- |  ------ |
| Host Server URL | ldap1.mycompany.com |
| Host Server Port | 389 |
| Authentication | Basic |
| Admin Bind DN | uid =admin,ou=netops,dc=mycompany,dc=com |
| Admin Bind Password | nqldap! |
| Base DN | dc=mycompany,dc=com |
| User ID | UID |
| Search Scope | One Level |
| Search Query | {userIdAttribute}={userId} |

### Scenario 3: Scenario 2 with Widest Search Capability

In this scenario, we are configuring the LDAP server with basic authentication, for access only by the persons in the network administrators group, and an unlimited search scope.

| Parameter | Value |
| ------------- |  ------ |
| Host Server URL | 192.168.10.2 |
| Host Server Port | 389 |
| Authentication | Basic |
| Admin Bind DN | uid =admin,ou=netadmin,dc=mycompany,dc=com |
| Admin Bind Password | 1dap*netq |
| Base DN | dc=mycompany, dc=net |
| User ID | UID |
| Search Scope | Subtree |
| Search Query | userIdAttribute}={userId} |

### Scenario 4: Scenario 3 with Active Directory Service

In this scenario, we are configuring the LDAP server with basic authentication, for access only by the persons in the given Active Directory group, and an unlimited search scope.

| Parameter | Value |
| ------------- | ------ |
| Host Server URL | 192.168.10.2 |
| Host Server Port | 389 |
| Authentication | Basic |
| Admin Bind DN | cn=netq,ou=45,dc=mycompany,dc=com |
| Admin Bind Password | nq&4mAd! |
| Base DN | dc=mycompany, dc=net |
| User ID | sAMAccountName |
| Search Scope | Subtree |
| Search Query | {userIdAttribute}={userId} |

## Add LDAP Users to NetQ

1. Click <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/03-Menu/navigation-menu.svg" width="18" height="18"/>, then select *Management* under **Admin**.

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

9. Select the NetQ user role for this user, *admin* or *user*, in the **User Type** dropdown.

10. Enter your admin password, and click **Save**, or click **Cancel** to discard the user account.

    {{<figure src="/images/netq/netq-mgmt-user-acct-fullscr-added-user-230.png" width="700">}}

    {{%notice tip%}}

LDAP user passwords are not stored in the NetQ database and are always authenticated against LDAP.

    {{%/notice%}}

11. Repeat these steps to add additional LDAP users.

## Remove LDAP Users from NetQ

You can remove LDAP users in the same manner as local users.

1. Click <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/03-Menu/navigation-menu.svg" width="18" height="18"/>, then select *Management* under **Admin**.

2. Locate the User Accounts card, and click **Manage**.

3. Select the user or users you want to remove.

4. Click <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/23-Delete/bin-1.svg" width="18" height="18"/> in the Edit menu.

{{%notice tip%}}
If an LDAP user is deleted in LDAP it is not automatically deleted from NetQ; however, the login credentials for these LDAP users stop working immediately.
{{%/notice%}}
