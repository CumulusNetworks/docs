---
title: LDAP
author: Cumulus Networks
weight: 585

type: nojsscroll
---
<style>
h { color: RGB(118,185,0)}
</style>
{{%notice note%}}
The `nv unset` commands remove the configuration you set with the equivalent `nv set` commands. This guide only describes an `nv unset` command if it differs from the `nv set` command.
{{%/notice%}}

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system aaa ldap base-dn</h>

Configures the LDAP search base for the common maps (passwd and group).

When an LDAP client requests information about a resource, the client must connect and bind to the server, then perform one or more resource queries depending on the lookup. All search queries to the LDAP server use the configured search base, filter, and the desired entry (uid=myuser). If the LDAP directory is large, this search takes a long time. Define a more specific search base for the common maps (passwd and group).

### Version History

Introduced in Cumulus Linux 5.11.0

### Example

```
cumulus@switch:~$ nv set system aaa ldap base-dn ou=support,dc=rtp,dc=example,dc=test
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system aaa ldap bind-dn</h>

Configures the Authenticated (Simple) BIND credentials. The BIND credentials are optional; if you do not specify the credentials, the switch assumes an anonymous bind. To use SASL (Simple Authentication and Security Layer) BIND, which provides authentication services using other mechanisms such as Kerberos, contact your LDAP server administrator for authentication information.

### Version History

Introduced in Cumulus Linux 5.11.0

### Example

```
cumulus@switch:~$ nv set system aaa ldap bind-dn CN=cumulus-admin,CN=Users,DC=rtp,DC=example,DC=test
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system aaa ldap hostname \<hostname-id\></h>

Configures the host name or IP address of the LDAP server from which you want to import users. If you use multiple LDAP servers, you can also set a priority for each server.

{{%notice note%}}
In Cumulus Linux 5.12 and later, this command is `nv set system aaa ldap server <server-id>`.
{{%/notice%}}

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<hostname-id>` |  The LDAP server ID. |

### Version History

Introduced in Cumulus Linux 5.11.0

### Example

```
cumulus@switch:~$ nv set system aaa ldap hostname ldapserver1
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system aaa ldap hostname \<hostname-id\> priority</h>

Configures the priority when using multiple LDAP servers. You can specify a value between 1 and 8.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<hostname-id>` |  The host name or IP address of the LDAP server. |

### Version History

Introduced in Cumulus Linux 5.11.0

### Example

```
cumulus@switch:~$ nv set system aaa ldap hostname ldapserver2 priority 2
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system aaa ldap server \<server-id\></h>

Configures the host name or IP address of the LDAP server from which you want to import users. If you use multiple LDAP servers, you can also set a priority for each server.

{{%notice note%}}
In Cumulus Linux 5.11 and earlier, this command is `nv set system aaa ldap hostname <hostname-id>`.
{{%/notice%}}

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<server-id>` |  The LDAP server ID. |

### Version History

Introduced in Cumulus Linux 5.12.0

### Example

```
cumulus@switch:~$ nv set system aaa ldap server ldapserver1
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system aaa ldap server \<server-id\> priority</h>

Configures the priority when using multiple LDAP servers. You can specify a value between 1 and 8.

{{%notice note%}}
In Cumulus Linux 5.11 and earlier, this command is `nv set system aaa ldap hostname <hostname-id> priority`.
{{%/notice%}}

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<server-id>` |  The host name or IP address of the LDAP server. |

### Version History

Introduced in Cumulus Linux 5.12.0

### Example

```
cumulus@switch:~$ nv set system aaa ldap server ldapserver2 priority 2
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system aaa ldap port</h>

Configures the port number of the LDAP server if you are using a non-default port. The default port number for LDAP is TCP and UDP port 389.

### Version History

Introduced in Cumulus Linux 5.11.0

### Example

```
cumulus@switch:~$ nv set system aaa ldap port 388
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system aaa ldap referrals</h>

Enables or disables LDAP referrals, which allow a directory tree to be partitioned and distributed between multiple LDAP servers.

### Version History

Introduced in Cumulus Linux 5.11.0

### Example

```
cumulus@switch:~$ nv set system aaa ldap referrals enabled
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system aaa ldap secret</h>

Configures the LDAP secret.

### Version History

Introduced in Cumulus Linux 5.11.0

### Example

```
cumulus@switch:~$ nv set system aaa ldap secret 1Q2w3e4r!
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system aaa ldap ssl ca-list</h>

Configures the SSL CA certificate list.

{{%notice note%}}
Cumulus Linux 5.12 and later does not provide this command.
{{%/notice%}}

### Version History

Introduced in Cumulus Linux 5.11.0

### Example

```
cumulus@switch:~$ nv set system aaa ldap ssl ca-list none
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system aaa ldap ssl cert-verify</h>

Enables SSL certificate validation.

### Version History

Introduced in Cumulus Linux 5.12.0

### Example

```
cumulus@switch:~$ nv set system aaa ldap ssl cert-verify enabled 
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system aaa ldap ssl crl-check</h>

Configures the SSL CRL (Certificate Revocation List) check.

{{%notice note%}}
In Cumulus Linux 5.12 and later, this command is `nv set system aaa ldap ssl crl-file`.
{{%/notice%}}

### Version History

Introduced in Cumulus Linux 5.11.0

### Example

```
cumulus@switch:~$ nv set system aaa ldap ssl crl-check /etc/ssl/certs/rtp-example-ca.crt
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system aaa ldap ssl crl-file</h>

Configures the SSL CRL (Certificate Revocation List) check.

{{%notice note%}}
In Cumulus Linux 5.11 and earlier, this command is `nv set system aaa ldap ssl crl-check`.
{{%/notice%}}

### Version History

Introduced in Cumulus Linux 5.12.0

### Example

```
cumulus@switch:~$ nv set system aaa ldap ssl crl-file /etc/ssl/certs/rtp-example-ca.crt
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system aaa ldap ssl mode</h>

Configures the LDAP SSL mode. You can specify `none`, `ssl`, or `start-tls`.

### Version History

Introduced in Cumulus Linux 5.11.0

### Example

```
cumulus@switch:~$ nv set system aaa ldap ssl mode ssl
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system aaa ldap ssl port</h>

Configures the LDAP SSL port.

### Version History

Introduced in Cumulus Linux 5.11.0

### Example

```
cumulus@switch:~$ nv set system aaa ldap ssl port 8443
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system aaa ldap scope</h>

Configures the search scope to one level to limit the level of the search to users directly under the base DN or to subtree to search for users in all branches under the base DN. The default setting is subtree.

### Version History

Introduced in Cumulus Linux 5.12.0

### Example

```
cumulus@switch:~$ nv set system aaa ldap scope one-level
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system aaa ldap ssl tls-ciphers</h>

Configures the SSL cipher suites. You can specify `TLS1.2`, `TLS1.3`, or `all`.

### Version History

Introduced in Cumulus Linux 5.11.0

### Example

```
cumulus@switch:~$ nv set system aaa ldap ssl tls-ciphers TLS1.3
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system aaa ldap timeout-bind</h>

Configures the number of seconds before the BIND operation times out. You can specify a value between 1 and 60. The default setting is 5 seconds.

### Version History

Introduced in Cumulus Linux 5.11.0

### Example

```
cumulus@switch:~$ nv set system aaa ldap timeout-bind 60
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system aaa ldap timeout-search</h>

Configures the number of seconds before the search times out. You can specify a value between 1 and 60. The default setting is 5 seconds.

### Version History

Introduced in Cumulus Linux 5.11.0

### Example

```
cumulus@switch:~$ nv set system aaa ldap timeout-search 60
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system aaa ldap version</h>

Configures the LDAP version. You can specify version 2 or 3. Cumulus Linux uses LDAP version 3 by default.

### Version History

Introduced in Cumulus Linux 5.11.0

### Example

```
cumulus@switch:~$ nv set system aaa ldap version 2
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system aaa ldap vrf</h>

Configures the LDAP VRF.

### Version History

Introduced in Cumulus Linux 5.11.0

### Example

```
cumulus@switch:~$ nv set system aaa ldap vrf mgmt
```
