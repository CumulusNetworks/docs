---
title: Integrate NetQ with Your LDAP Server
author: Cumulus Networks
weight: 201
aliases:
product: Cumulus NetQ
version: 2.3
imgData: cumulus-netq-23
---
With this release and an administrator role, you are able to integrate the NetQ role-based access control (RBAC) with your lightweight directory access protocol (LDAP) server in on-premises deployments. NetQ maintains control over role-based permissions, but LDAP is used for authentication of the users. A copy of each user from LDAP is stored in the local NetQ database.

Configuring an LDAP server does not prevent you from configuring local users (stored and managed in the NetQ database) as well.

## Create an LDAP Configuration

One LDAP server can be configured per admin user account. Once LDAP is configured, you can validate the connectivity (and configuration) and save the configuration.

1. Click <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/03-Menu/navigation-menu.svg", width="18", height="18"/>, then select *Management* under **Admin**.

2. Locate the LDAP Server Info card, and click **Configure LDAP**.

    {{<figure src="/images/netq/netq-mgmt-ldap-config-modal-230.png" width="500">}}

3. Obtain and enter the following information about your LDAP server:

    | Parameter | Description |
    | --------- | ----------- |
    | Server    | <ul><li><strong>Host\*</strong>: URL of the LDAP server</li><li><strong>Server Port\*</strong>: Name of the port on which to communicate with the LDAP server</li><li><strong>Authentication\*</strong>: Select from <ul><li><em>Anonymous</em>: LDAP client does not require authentication</li><li><em>Basic</em>: LDAP client sends the username as an LDAP distinguished name along with a password as clear text to the LDAP server. Also called Simple authentication.</li><li><em>SASL</em>: LDAP client and server negotiate an authentication mechanism</li></ul></ul> |
    | User Attributes | <ul><li><strong>Bind DN\*</strong>: Username (Distinguished Name) used for search queries</li><li><strong>Base DN\*</strong>: Base of the subtree, where in directory structure search query begins</li><li><strong>User ID\*</strong>: Type of identifier used to specify an LDAP user</li><li><strong>First Name</strong>: Given name of LDAP user</li><li><strong>Last Name</strong>: Surname of LDAP user</li><li><strong>Email</strong>: Electronic mail address for LDAP user</li></ul> |
    | Search Attributes | <ul><li><strong>Search Scope</strong>: Specifies the portion of the target subtree used in a search query. Select from <ul><li><em>None</em>: No search allowed for user on this LDAP server</li><li><em>Base</em>: Search for users at the base level only; no subordinates</li><li><em>One Level</em>: Search for immediate children of user; not at base or for any descendants</li><li><em>Subtree</em>: Search for users from base, subordinates at any depth</li><li><em>Subordinate</em>: Search for subordinates at any depth of user; but not at base</li></ul><li><strong>Search Query</strong>: Actual search query</li></ul> |

    **Note**: Items with an asterisk (*) are required. All others are optional.

4. Click **Save** to complete the configuration, or click **Cancel** to discard the configuration.

{{%notice info%}}
LDAP config cannot be changed once configured. If you need to change the configuration, you must delete the current LDAP configuration and create a new one. Note that if you change the LDAP server configuration, all users created against that LDAP server remain in the NetQ database and continue to be visible, but are no longer be viable. You must manually delete those users if you do not want to see them.
{{%/notice%}}

## Add LDAP Users to NetQ

1. Click <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/03-Menu/navigation-menu.svg", width="18", height="18"/>, then select *Management* under **Admin**.

2. Locate the User Accounts card, and click **Manage**.

3. On the User Accounts tab, click **Add User**.

4. Enter the user's email address.

5. Select/click/check  LDAP 

6. Click Search.

7. If the user is found, the email address, first and last name fields are automatically filled in on the  Add New User form. If searching is not enabled on the LDAP server, you must enter the information manually.

    {{%notice tip%}}
If the fields are not automatically filled in, and searching is enabled on the LDAP server, you might require changes to the mapping file. Refer to xxx for details.
    {{%/notice%}}

8. Select the role for this user, *admin* or *user*, in the **User Type** dropdown.

9. Enter your admin password, and click **Validate**.

10. When the user is validated, click **Save** to add the user account, or click **Cancel** to discard the user account.

    {{%notice tip%}}
LDAP user passwords are not stored in the NetQ database and are always authenticated against LDAP.
    {{%/notice%}}

10. Repeat these steps to add additional LDAP users.


-----
7. If the user is deleted in LDAP it doesn't get automatically deleted in NetQ however, the login for such user stops working immediately 