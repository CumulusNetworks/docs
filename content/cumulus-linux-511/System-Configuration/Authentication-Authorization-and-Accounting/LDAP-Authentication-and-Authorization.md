---
title: LDAP Authentication and Authorization
author: NVIDIA
weight: 170
toc: 4
---
Cumulus Linux uses Pluggable Authentication Modules (PAM) and Name Service Switch (NSS) for user authentication. NSS enables PAM to use LDAP to provide user authentication, group mapping, and information for other services on the system.
- NSS specifies the order of the information sources that resolve names for each service. Using NSS with authentication and authorization provides the order and location for user lookup and group mapping on the system.
- PAM handles the interaction between the user and the system, providing login handling, session setup, authentication of users, and authorization of user actions.

## Configure LDAP Server Settings

You can configure LDAP server settings with NVUE commands or by editing configuration files.

{{%notice note%}}
To configure LDAP authentication on Linux, you can use `libnss-ldap`, `libnss-ldapd`, or `libnss-sss`. This document describes `libnss-ldapd` only. From internal testing, this library works best with Cumulus Linux and is the easiest to configure, automate, and troubleshoot.
{{%/notice%}}

### Connection

Configure the following connection settings:
- The host name or IP address of the LDAP server from which you want to import users.
- The port number of the LDAP server if you are using a non-default port. The default port numbers are TCP and UDP port 389 for LDAP and port 636 for LDAPS. In production environments, use the LDAPS protocol so that all communications are secure.
- Authenticated (Simple) BIND credentials. The BIND credentials are optional; if you do not specify the credentials, the switch assumes an anonymous bind. To use SASL (Simple Authentication and Security Layer) BIND, which provides authentication services using other mechanisms such as Kerberos, contact your LDAP server administrator for authentication information.

The following example configures the LDAP server and port, and the BIND credentials.

{{< tabs "TabID32 ">}}
{{< tab "NVUE Commands ">}}

```
cumulus@switch:~$ nv set system aaa ldap hostname ldapserver1
cumulus@switch:~$ nv set system aaa ldap port 388
cumulus@switch:~$ nv set system aaa ldap bind-dn CN=cumulus-admin,CN=Users,DC=rtp,DC=example,DC=test
cumulus@switch:~$ nv set system aaa ldap secret 1Q2w3e4r!
cumulus@switch:~$ nv config apply
```

{{< /tab >}}
{{< tab "Linux Commands ">}}

Edit the `/etc/nslcd.conf` file to set the URI and BIND credentials, then uncomment the lines:

```
cumulus@switch:~$ sudo nano /etc/nslcd.conf
...
# The location at which the LDAP server(s) should be reachable.
uri ldaps://ldapserver1:8443/
#uripriority 1
...
# The DN to bind with for normal lookups.
binddn CN=cumulus admin,CN=Users,DC=rtp,DC=example,DC=test
bindpw 1Q2w3e4r!
...
```

{{< /tab >}}
{{< /tabs >}}

### Search Function

When an LDAP client requests information about a resource, the client must connect and bind to the server, then perform one or more resource queries depending on the lookup. All search queries to the LDAP server use the configured search *base*, *filter*, and the desired entry (*uid=myuser*). If the LDAP directory is large, this search takes a long time. Define a more specific search base for the common *maps* (*passwd* and *group*).

{{< tabs "TabID68 ">}}
{{< tab "NVUE Commands ">}}

```
cumulus@switch:~$ nv set system aaa ldap base-dn ou=support,dc=rtp,dc=example,dc=test
cumulus@switch:~$ nv config apply
```

{{< /tab >}}
{{< tab "Linux Commands ">}}

Edit the `/etc/nslcd.conf` file to add the search base:

```
cumulus@switch:~$ sudo nano /etc/nslcd.conf
...
# The search base that will be used for all queries.
base ou=support,dc=rtp,dc=example,dc=test
```

{{< /tab >}}
{{< /tabs >}}

### Search Scope

You can set the search scope to one level to limit the level of the search to users directly under the base DN or to subtree to search for users in all branches under the base DN. The default setting is subtree.

To set the search scope to one level:

{{< tabs "TabID97 ">}}
{{< tab "NVUE Commands ">}}

```
cumulus@switch:~$ nv set system aaa ldap scope one-level
cumulus@switch:~$ nv config apply
```

To set the search scope back to the default setting (subtree):

```
cumulus@switch:~$ nv set system aaa ldap scope subtree
cumulus@switch:~$ nv config apply
```

{{< /tab >}}
{{< tab "Linux Commands ">}}

Edit the `/etc/nslcd.conf` file to set the `scope` option to `one`.

```
cumulus@switch:~$ sudo nano /etc/nslcd.conf
...
# The search scope.
scope one
...
```

To set the search scope back to the default setting (subtree), set the `scope` option to `sub`:

{{< /tab >}}
{{< /tabs >}}

### Search Filters

To limit the search scope when authenticating users, use search filters to specify criteria when searching for objects within the directory.

{{< tabs "TabID134 ">}}
{{< tab "NVUE Commands ">}}

```
cumulus@switch:~$ nv set system aaa ldap filter passwd cumulus
cumulus@switch:~$ nv set system aaa ldap filter group 1234
cumulus@switch:~$ nv set system aaa ldap filter shadow
cumulus@switch:~$ nv config apply
```

{{< /tab >}}
{{< tab "Linux Commands ">}}

Edit the `/etc/nslcd.conf` file to set the `filter passwd`, `filter group`, or `filter shadow` options.

```
cumulus@switch:~$ sudo nano /etc/nslcd.conf
...
# filters and maps
filter passwd cumulus
filter group 1234
filter shadow abcd
...
```

{{< /tab >}}
{{< /tabs >}}

### Attribute Mapping

The *map* configuration allows you to override the attributes pushed from LDAP. To override an attribute for a given *map*, specify the attribute name and the new value.

{{< tabs "TabID166 ">}}
{{< tab "NVUE Commands ">}}

```
cumulus@switch:~$ nv set system aaa ldap map passwd homedirectory /home/$sAMAccountName
cumulus@switch:~$ nv set system aaa ldap map passwd userpassword cumulus
cumulus@switch:~$ nv set system aaa ldap map group cn sAMAccountName
cumulus@switch:~$ nv set system aaa ldap map group gidnumber objectSid:S-1-5-21-1391733952-3059161487-1245441232
cumulus@switch:~$ nv config apply
```

{{< /tab >}}
{{< tab "Linux Commands ">}}

Edit the `/etc/nslcd.conf` file to set the `map passwd` and `map group` options..

```
cumulus@switch:~$ sudo nano /etc/nslcd.conf
...
# filters and maps
...
map passwd homedirectory /home/$sAMAccountName
map passwd userpassword cumulus
map group cn sAMAccountName
map group gidnumber objectSid:S-1-5-21-1391733952-3059161487-1245441232
...
```

{{< /tab >}}
{{< /tabs >}}

### LDAP Version

Cumulus Linux uses LDAP version 3 by default. If you need to change the LDAP version to 2:

{{< tabs "TabID201 ">}}
{{< tab "NVUE Commands ">}}

```
cumulus@switch:~$ nv set system aaa ldap version 2
cumulus@switch:~$ nv config apply
```

{{< /tab >}}
{{< tab "Linux Commands ">}}

Edit the `/etc/nsswitch.conf` file to change the `ldap_version`.

```
cumulus@switch:~$ sudo nano /etc/nslcd.conf
...
# The LDAP protocol version to use.
ldap_version 2
...
```

{{< /tab >}}
{{< /tabs >}}

### LDAP Timeouts

Cumulus Linux provides two timeout settings:
- The bind timeout sets the number of seconds before the BIND operation times out. The default setting is 5 seconds.
- The search timeout sets the number of seconds before the search times out. The default setting is 5 seconds.

The following example sets both the BIND session timeout and the search timeout to 60 seconds.

{{< tabs "TabID233 ">}}
{{< tab "NVUE Commands ">}}

```
cumulus@switch:~$ nv set system aaa ldap timeout-bind 60
cumulus@switch:~$ nv set system aaa ldap timeout-search 60
cumulus@switch:~$ nv config apply
```

{{< /tab >}}
{{< tab "Linux Commands ">}}

Edit the `/etc/nslcd.conf` file to change the `bind_timelimit` option and the `timelimit` option.

```
cumulus@switch:~$ sudo nano /etc/nslcd.conf
...
bind_timelimit 60
timelimit 60
...
```

{{< /tab >}}
{{< /tabs >}}

### SSL Options

You can configure the following SSL options:
- The SSL mode.
- The SSL port.
- The SSL certificate checker.
- The SSL CA certificate file.
- The SSL cipher suites. You can specify TLS1.2, TLS1.3, TLS-CIPHERS, or all.
- The SSL <span class="a-tooltip">[CRL](## "Certificate Revocation List")</span> checker.

The following example sets the SSL mode to SSL, the port to 8443, enables the SSL certificate checker, sets the CA certificate list to none, the SSL cipher suites to TLS1.3 and the Certificate Revocation List to abc.

{{< tabs "TabID270 ">}}
{{< tab "NVUE Commands ">}}

```
cumulus@switch:~$ nv set system aaa ldap ssl mode ssl
cumulus@switch:~$ nv set system aaa ldap ssl port 8443
cumulus@switch:~$ nv set system aaa ldap ssl cert-verify enabled
cumulus@switch:~$ nv set system aaa ldap ssl ca-list none
cumulus@switch:~$ nv set system aaa ldap ssl tls-ciphers TLS1.3
cumulus@switch:~$ nv set system aaa ldap ssl crl-check /etc/ssl/certs/rtp-example-ca.crt
cumulus@switch:~$ nv config apply
```

{{< /tab >}}
{{< tab "Linux Commands ">}}

Edit the `/etc/nslcd.conf` file to set the SSL options.

```
cumulus@switch:~$ sudo nano /etc/nslcd.conf
...
# SSL options
ssl on
tls_reqcert try
tls_ciphers NORMAL:-VERS-ALL:+VERS-TLS1.3
tls_crlcheck all
tls_crlfile /etc/ssl/certs/rtp-example-ca.crt
...
```

{{< /tab >}}
{{< /tabs >}}

### LDAP Referrals

LDAP referrals allow a directory tree to be partitioned and distributed between multiple LDAP servers.

To configure LDAP referrals:

{{< tabs "TabID309 ">}}
{{< tab "NVUE Commands ">}}

```
cumulus@switch:~$ nv set system aaa ldap referrals ldapserver2,ldapserver3
cumulus@switch:~$ nv config apply
```

{{< /tab >}}
{{< tab "Linux Commands ">}}

Edit the `/etc/nslcd.conf` file to set the referrals option.

```
cumulus@switch:~$ sudo nano /etc/nslcd.conf
...
referrals yes
...
```

{{< /tab >}}
{{< /tabs >}}

### Show LDAP Settings

To show the LDAP configuration settings on the switch, run the following commands:
- `nv show system aaa ldap` shows all the LDAP configuration settings. 
- `nv show system aaa ldap hostname` shows the hostnames of the LDAP servers and their priorities.
- `nv show system aaa ldap hostname <hostname>` shows the priority for the specified hostname.
- `nv show system aaa ldap ssl` shows the LDAP SSL configuration settings.
- `nv show system aaa ldap map` shows the attribute mapping settings. You can show the group, password or shadow mappings with the `nv show system aaa ldap map group`, `nv show system aaa ldap map passwd`, and `nv show system aaa ldap map shadow` commands.
- `nv show system aaa ldap filter` shows the search filter settings.

The following example shows all the LDAP configuration settings:

```
cumulus@switch:~$ nv show system aaa ldap
                      operational                                          applied                                            
--------------------  ---------------------------------------------------  ---------------------------------------------------
vrf                   default                                              mgmt                                               
bind-dn               CN=cumulus-admin,CN=Users,DC=rtp,DC=example,DC=test  CN=cumulus-admin,CN=Users,DC=rtp,DC=example,DC=test
base-dn               ou=support,dc=rtp,dc=example,dc=test                 ou=support,dc=rtp,dc=example,dc=test               
referrals             yes                                                  off                                                
scope                 one                                                  one-level                                          
port                  389                                                  389                                                
timeout-bind          5                                                    5                                                  
timeout-search        5                                                    5                                                  
secret                *                                                    *                                                  
version               3                                                    3                                                  
[hostname]            ldapserver1                                          ldapserver1                                        
ssl                                                                                                                           
  mode                none                                                 none                                               
  port                389                                                  636                                                
  cert-verify         enabled                                              enabled                                            
  ca-list             default                                              default                                            
  tls-ciphers         all                                                  all                                                
  crl-check           none                                                 none                                               
filter                                                                                                                        
  passwd              cumulus                                              cumulus                                            
  group               1234                                                 1234                                               
  shadow              abc                                                  abc                                                
map                                                                                                                           
  passwd                                                                                                                      
    uid                                                                                                                       
    uidnumber                                                                                                                 
    gidnumber                                                                                                                 
    userpassword      cumulus                                              cumulus                                            
    homedirectory     /home/                                               /home/                                             
    gecos                                                                                                                     
  shadow                                                                                                                      
    uid                                                                                                                       
    shadowlastchange                                                                                                          
  group                                                                                                                       
    cn                sAMAccountName                                       sAMAccountName                                     
    memberuid                                                                                                                 
    gidnumber         objectSid:S-1-5-21-1391733952-3059161487-1245441232  objectSid:S-1-5-21-1391733952-3059161487-1245441232
```

The following example shows the SSL configuration settings:

```
cumulus@switch:~$ nv show system aaa ldap ssl
             operational  applied
-----------  -----------  -------
mode         none         none   
port         389          636    
cert-verify  enabled      enabled
ca-list      default      default
tls-ciphers  all          all    
crl-check    none         none
```

The following example shows the search map group configuration settings:

```
cumulus@switch:~$ nv show system aaa ldap map group
           operational                                          applied                                            
---------  ---------------------------------------------------  ---------------------------------------------------
cn         sAMAccountName                                       sAMAccountName                                     
memberuid                                                                                                          
gidnumber  objectSid:S-1-5-21-1391733952-3059161487-1245441232  objectSid:S-1-5-21-1391733952-3059161487-1245441232

```

## Create Home Directory on Login

If you want to use unique home directories, run the `sudo pam-auth-update` command and select `Create home directory on login` in the PAM configuration dialog (press the space bar to select the option). Select OK, then press Enter to save the update and close the dialog.

```
cumulus@switch:~$ sudo pam-auth-update
```

{{< img src = "/images/cumulus-linux/authentication-pam-update.png" >}}

The home directory for any user that logs in (using LDAP or not) populates with the standard dotfiles from `/etc/skel`.

{{%notice note%}}
When `nslcd` starts, an error message similar to the following (where 5816 is the `nslcd` PID) sometimes appears:

```
nslcd[5816]: unable to dlopen /usr/lib/x86_64-linux-gnu/sasl2/libsasldb.so: libdb-5.3.so: cannot open
shared object file: No such file or directory
```

You can ignore this message. The `libdb` package and resulting log messages from `nslcd` do not cause any issues when you use LDAP as a client for login and authentication.
{{%/notice%}}


## Configure LDAP Authorization

Linux uses the *sudo* command to allow non-administrator users (such as the default *cumulus* user account) to perform privileged operations. To control the users that can use sudo, define a series of rules in the `/etc/sudoers` file and files in the `/etc/sudoers.d/` directory. The rules apply to groups but you can also define specific users. You can add sudo rules using the group names from LDAP. For example, if a group of users are in the group *netadmin*, you can add a rule to give those users sudo privileges. Refer to the sudoers manual (`man sudoers`) for a complete usage description. The following shows an example in the `/etc/sudoers` file:

```
# The basic structure of a user specification is "who where = (as_whom) what ".
%sudo ALL=(ALL:ALL) ALL
%netadmin ALL=(ALL:ALL) ALL
```

## Active Directory Configuration

Active Directory (AD) is a fully featured LDAP-based NIS server created by Microsoft. It offers unique features that classic OpenLDAP servers do not have. AD can be more complicated to configure on the client and each version works a little differently with Linux-based LDAP clients. Some more advanced configuration examples, from testing LDAP clients on Cumulus Linux with Active Directory (AD/LDAP), are available in the [knowledge base]({{<ref "/knowledge-base/Security/Authentication/LDAP-on-Cumulus-Linux-Using-Server-2008-Active-Directory" >}}).

## LDAP Verification Tools

The LDAP client daemon retrieves and caches password and group information from LDAP. To verify the LDAP interaction, use these command-line tools to trigger an LDAP query from the device.

### Identify a User with the id Command

The `id` command performs a username lookup by following the lookup information sources in NSS for the *passwd* service. This returns the user ID, group ID and the group list retrieved from the information source. In the following example, the user *cumulus* is locally defined in `/etc/passwd`, and *myuser* is on LDAP. The NSS configuration has the `passwd` map configured with the sources `compat ldap`:

```
cumulus@switch:~$ id cumulus
uid=1000(cumulus) gid=1000(cumulus) groups=1000(cumulus),24(cdrom),25(floppy),27(sudo),29(audio),30(dip),44(video),46(plugdev)
cumulus@switch:~$ id myuser
uid=1230(myuser) gid=3000(Development) groups=3000(Development),500(Employees),27(sudo)
```

### getent

The `getent` command retrieves all records found with NSS for a given map. It can also retrieve a specific entry under that map. You can perform tests with the `passwd`, `group`, `shadow`, or any other map in the `/etc/nsswitch.conf` file. The output from this command formats according to the map requested. For the  `passwd` service, the structure of the output is the same as the entries in `/etc/passwd`. The group map outputs the same structure as `/etc/group`.

In this example, looking up a specific user in the `passwd` map, the user *cumulus* is locally defined in `/etc/passwd`, and *myuser* is only in LDAP.

```
cumulus@switch:~$ getent passwd cumulus
cumulus:x:1000:1000::/home/cumulus:/bin/bash
cumulus@switch:~$ getent passwd myuser
myuser:x:1230:3000:My Test User:/home/myuser:/bin/bash
```

In the next example, looking up a specific group in the group service, the group *cumulus* is locally defined in `/etc/groups`, and *netadmin* is on LDAP.

```
cumulus@switch:~$ getent group cumulus
cumulus:x:1000:
cumulus@switch:~$ getent group netadmin
netadmin:*:502:larry,moe,curly,shemp
```

Running the command `getent passwd` or `getent group` without a specific request returns **all** local and LDAP entries for the *passwd* and *group* maps.

### LDAP search

The `ldapsearch` command performs LDAP operations directly on the LDAP server. This does not interact with NSS. This command displays the information that the LDAP daemon process receives back from the server. The command has several options. The simplest option uses anonymous bind to the host and specifies the search DN and the attribute to look up.

```
cumulus@switch:~$ ldapsearch -H ldap://ldap.example.com -b dc=example,dc=com -x uid=myuser
```

{{< expand "Click to expand the command output "  >}}

```
# extended LDIF
#
# LDAPv3
# base <dc=example,dc=com> with scope subtree
# filter: uid=myuser
# requesting: ALL
#
# myuser, people, example.com
dn: uid=myuser,ou=people,dc=example,dc=com
cn: My User
displayName: My User
gecos: myuser
gidNumber: 3000
givenName: My
homeDirectory: /home/myuser
initials: MU
loginShell: /bin/bash
mail: myuser@example.com
objectClass: inetOrgPerson
objectClass: posixAccount
objectClass: shadowAccount
objectClass: top
shadowExpire: -1
shadowFlag: 0
shadowMax: 999999
shadowMin: 8
shadowWarning: 7
sn: User
uid: myuser
uidNumber: 1234

# search result
search: 2
result: 0 Success

# numResponses: 2
# numEntries: 1
```

{{< /expand >}}

### LDAP Browsers

The GUI LDAP clients are free tools that show the structure of the LDAP database graphically.

- {{<exlink url="http://directory.apache.org/studio/" text="Apache Directory Studio">}}
- {{<exlink url="http://ldapmanager.sourceforge.net/" text="LDAPManager">}}

## Troubleshooting

### nslcd Debug Mode

When setting up LDAP authentication for the first time, turn off the `nslcd` service using the `systemctl stop nslcd.service` command (or the `systemctl stop nslcd@mgmt.service` if you are running the service in a management VRF) and run it in debug mode. Debug mode works whether you are using LDAP over SSL (port 636) or an unencrypted LDAP connection (port 389).

```
cumulus@switch:~$ sudo systemctl stop nslcd.service
cumulus@switch:~$ sudo nslcd -d
```

After you enable debug mode, run the following command to test LDAP queries:

```
cumulus@switch:~$ getent passwd
```

If you configure LDAP correctly, the following messages appear after you run the `getent` command:

```
nslcd: DEBUG: accept() failed (ignored): Resource temporarily unavailable
nslcd: [8e1f29] DEBUG: connection from pid=11766 uid=0 gid=0
nslcd: [8e1f29] <passwd(all)> DEBUG: myldap_search(base="dc=example,dc=com", filter="(objectClass=posixAccount)")
nslcd: [8e1f29] <passwd(all)> DEBUG: ldap_result(): uid=myuser,ou=people,dc=example,dc=com
nslcd: [8e1f29] <passwd(all)> DEBUG: ldap_result(): ... 152 more results
nslcd: [8e1f29] <passwd(all)> DEBUG: ldap_result(): end of results (162 total)
```

In the example output above, `<passwd(all)>` shows a query of the entire directory structure.

You can query a specific user with the following command:

```
cumulus@switch:~$ getent passwd myuser
```

You can replace `myuser` with any username on the switch. The following debug output indicates that user `myuser` exists:

```
nslcd: DEBUG: add_uri(ldap://10.50.21.101)
nslcd: version 0.8.10 starting
nslcd: DEBUG: unlink() of /var/run/nslcd/socket failed (ignored): No such file or directory
nslcd: DEBUG: setgroups(0,NULL) done
nslcd: DEBUG: setgid(110) done
nslcd: DEBUG: setuid(107) done
nslcd: accepting connections
nslcd: DEBUG: accept() failed (ignored): Resource temporarily unavailable
nslcd: [8b4567] DEBUG: connection from pid=11369 uid=0 gid=0
nslcd: [8b4567] <passwd="myuser"> DEBUG: myldap_search(base="dc=cumulusnetworks,dc=com", filter="(&(objectClass=posixAccount)(uid=myuser))")
nslcd: [8b4567] <passwd="myuser"> DEBUG: ldap_initialize(ldap://<ip_address>)
nslcd: [8b4567] <passwd="myuser"> DEBUG: ldap_set_rebind_proc()
nslcd: [8b4567] <passwd="myuser"> DEBUG: ldap_set_option(LDAP_OPT_PROTOCOL_VERSION,3)
nslcd: [8b4567] <passwd="myuser"> DEBUG: ldap_set_option(LDAP_OPT_DEREF,0)
nslcd: [8b4567] <passwd="myuser"> DEBUG: ldap_set_option(LDAP_OPT_TIMELIMIT,0)
nslcd: [8b4567] <passwd="myuser"> DEBUG: ldap_set_option(LDAP_OPT_TIMEOUT,0)
nslcd: [8b4567] <passwd="myuser"> DEBUG: ldap_set_option(LDAP_OPT_NETWORK_TIMEOUT,0)
nslcd: [8b4567] <passwd="myuser"> DEBUG: ldap_set_option(LDAP_OPT_REFERRALS,LDAP_OPT_ON)
nslcd: [8b4567] <passwd="myuser"> DEBUG: ldap_set_option(LDAP_OPT_RESTART,LDAP_OPT_ON)
nslcd: [8b4567] <passwd="myuser"> DEBUG: ldap_simple_bind_s(NULL,NULL) (uri="ldap://<ip_address>")
nslcd: [8b4567] <passwd="myuser"> DEBUG: ldap_result(): end of results (0 total)
```

### SSL/TLS

- The FQDN of the LDAP server URI does not match the FQDN in the CA-signed server certificate.
- `nslcd` cannot read the SSL certificate and reports a *Permission denied* error during server connection negotiation. Check the permission on each directory in the path of the root SSL certificate. Ensure that it is readable by the `nslcd` user.

### NSCD

If you enable the `nscd cache` daemon then make changes to the user from LDAP, you can clear the cache using the following commands:

```
nscd --invalidate = passwd
nscd --invalidate = group
```

The `nscd` package works with `nslcd` to cache name entries returned from the LDAP server, which can cause authentication failures. To work around these issues, disable `nscd`, restart the `nslcd` service, then retry authentication:

```
cumulus@switch:~$ sudo nscd -K
cumulus@switch:~$ sudo systemctl restart nslcd.service
```

{{%notice note%}}
If you are running the `nslcd` service in the management VRF, you must use the `systemctl restart nslcd@mgmt.service` command instead of the `systemctl restart nslcd.service` command; for example:

```
cumulus@switch:~$ sudo nscd -K
cumulus@switch:~$ sudo systemctl restart nslcd@mgmt.service
```
{{%/notice%}}

### LDAP

If the search filter returns incorrect results, check for typographical errors in the search filter. Use `ldapsearch` to test your filter or configure the basic LDAP connection and search parameters in the `/etc/ldap/ldap.conf` file.

```
# ldapsearch -D 'cn=CLadmin' -w 'CuMuLuS' "(&(ObjectClass=inetOrgUser)(uid=myuser))"
```

## Related Information

- {{<exlink url="https://wiki.debian.org/LDAP/NSS" text="Debian - configuring LDAP authentication">}}
- {{<exlink url="https://wiki.debian.org/LDAP/PAM" text="Debian - configuring PAM to use LDAP">}}
- {{<exlink url="https://raw.githubusercontent.com/arthurdejong/nss-pam-ldapd/master/nslcd.conf" text="GitHub - Arthur de Jong nslcd.conf file">}}
- {{<exlink url="http://backports.debian.org/Instructions/" text="Debian backports">}}

<!--
## Update the nslcd.conf File

After installation, update the main configuration file (`/etc/nslcd.conf`) to accommodate the expected LDAP server settings.

This section documents some of the more important options that relate to security and queries. For details on all the available configuration options, read the {{<exlink url="http://linux.die.net/man/5/nslcd.conf" text="nslcd.conf man page">}}.

{{%notice note%}}
After first editing the `/etc/nslcd.conf` file and/or enabling LDAP in the `/etc/nsswitch.conf` file, you must restart `netd` with the `sudo systemctl restart netd` command. If you disable LDAP, you need to restart the `netd` service.
{{%/notice%}}

### Connection

The LDAP client starts a session by connecting to the LDAP server on TCP and UDP port 389 or on port 636 for LDAPS. Depending on the configuration, this connection establishes without authentication (anonymous bind); otherwise, the client must provide a bind user and password. The variables you use to define the connection to the LDAP server are the URI and bind credentials.

The URI is mandatory and specifies the LDAP server location using the FQDN or IP address. The URI also designates whether to use `ldap://` for clear text transport, or `ldaps://` for SSL/TLS encrypted transport. You can also specify an alternate port in the URI. In production environments, use the LDAPS protocol so that all communications are secure.

After the connection to the server is complete, the BIND operation authenticates the session. The BIND credentials are optional; if you do not specify the credentials, the switch assumes an anonymous bind. Configure authenticated (Simple) BIND by specifying the user (`binddn`) and password (`bindpw`) in the configuration. Another option is to use SASL (Simple Authentication and Security Layer) BIND, which provides authentication services using other mechanisms, like Kerberos. Contact your LDAP server administrator for this information as it depends on the configuration of the LDAP server and the credentials for the client device.

```
# The location at which the LDAP server(s) should be reachable.
uri ldaps://ldap.example.com
# The DN to bind with for normal lookups.
binddn cn=CLswitch,ou=infra,dc=example,dc=com
bindpw CuMuLuS
```

### Search Function

When an LDAP client requests information about a resource, it must connect and bind to the server. Then, it performs one or more resource queries depending on the lookup. All search queries to the LDAP server use the configured search *base*, *filter*, and the desired entry (*uid=myuser*). If the LDAP directory is large, this search takes a long time. Define a more specific search base for the common *maps* (*passwd* and *group*).

```
# The search base that will be used for all queries.
base dc=example,dc=com
# Mapped search bases to speed up common queries.
base passwd ou=people,dc=example,dc=com
base group ou=groups,dc=example,dc=com
```

### Search Filters

To limit the search scope when authenticating users, use search filters to specify criteria when searching for objects within the directory. The default filters applied are:

```
filter passwd (objectClass=posixAccount)
filter group (objectClass=posixGroup)
```

### Attribute Mapping

The *map* configuration allows you to override the attributes pushed from LDAP. To override an attribute for a given *map*, specify the attribute name and the new value. This is useful to ensure that the shell is *bash* and the home directory is `/home/cumulus`:

```
map    passwd homeDirectory "/home/cumulus"
map    passwd shell "/bin/bash"
```

{{%notice note%}}
In LDAP, the ***map*** refers to one of the supported maps specified in the `manpage` for `nslcd.conf` (such as *passwd* or *group*).
{{%/notice%}}

### Create Home Directory on Login

If you want to use unique home directories, run the `sudo pam-auth-update` command and select `Create home directory on login` in the PAM configuration dialog (press the space bar to select the option). Select OK, then press Enter to save the update and close the dialog.

```
cumulus@switch:~$ sudo pam-auth-update
```

{{< img src = "/images/cumulus-linux/authentication-pam-update.png" >}}

The home directory for any user that logs in (using LDAP or not) populates with the standard dotfiles from `/etc/skel`.

{{%notice note%}}
When `nslcd` starts, an error message similar to the following (where 5816 is the `nslcd` PID) sometimes appears:

```
nslcd[5816]: unable to dlopen /usr/lib/x86_64-linux-gnu/sasl2/libsasldb.so: libdb-5.3.so: cannot open
shared object file: No such file or directory
```

You can ignore this message. The `libdb` package and resulting log messages from `nslcd` do not cause any issues when you use LDAP as a client for login and authentication.
{{%/notice%}}

### Example Configuration

The following is an example configuration using Cumulus Linux.

```
# /etc/nslcd.conf
# nslcd configuration file. See nslcd.conf(5)
# for details.

# The user and group nslcd should run as.
uid nslcd
gid nslcd

# The location at which the LDAP server(s) should be reachable.
uri ldaps://myadserver.rtp.example.test

# The search base that will be used for all queries.
base ou=support,dc=rtp,dc=example,dc=test

# The LDAP protocol version to use.
#ldap_version 3

# The DN to bind with for normal lookups.
# defconf-set-selections doesn't seem to set this. so have to manually set this.
binddn CN=cumulus admin,CN=Users,DC=rtp,DC=example,DC=test
bindpw 1Q2w3e4r!

# The DN used for password modifications by root.
#rootpwmoddn cn=admin,dc=example,dc=com

# SSL options
#ssl off (default)
# Not good does not prevent man in the middle attacks
#tls_reqcert demand(default)
tls_cacertfile /etc/ssl/certs/rtp-example-ca.crt

# The search scope.
#scope sub

# Add nested group support
# Supported in nslcd 0.9 and higher.
# default wheezy install of nslcd supports on 0.8. wheezy-backports has 0.9
nss_nested_groups yes

# Mappings for Active Directory
# (replace the SIDs in the objectSid mappings with the value for your domain)
# "dsquery * -filter (samaccountname=testuser1) -attr ObjectSID" where cn == 'testuser1'
pagesize 1000
referrals off
idle_timelimit 1000

# Do not allow uids lower than 100 to login (aka Administrator)
# not needed as pam already has this support
# nss_min_uid 1000

# This filter says to get all users who are part of the cumuluslnxadm group. Supports nested groups.
# Example, mary is part of the snrnetworkadm group which is part of cumuluslnxadm group
# Ref: http://msdn.microsoft.com/en-us/library/aa746475%28VS.85%29.aspx (LDAP_MATCHING_RULE_IN_CHAIN)
filter passwd (&(Objectclass=user)(!(objectClass=computer))(memberOf:1.2.840.113556.1.4.1941:=cn=cumuluslnxadm,ou=groups,ou=support,dc=rtp,dc=example,dc=test))
map    passwd uid           sAMAccountName
map    passwd uidNumber     objectSid:S-1-5-21-1391733952-3059161487-1245441232
map    passwd gidNumber     objectSid:S-1-5-21-1391733952-3059161487-1245441232
map    passwd homeDirectory "/home/$sAMAccountName"
map    passwd gecos         displayName
map    passwd loginShell    "/bin/bash"

# Filter for any AD group or user in the baseDN. the reason for filtering for the
# user to make sure group listing for user files don't say '<user> <gid>'. instead will say '<user> <user>'
# So for cosmetic reasons..nothing more.
filter group (&(|(objectClass=group)(Objectclass=user))(!(objectClass=computer)))
map    group gidNumber     objectSid:S-1-5-21-1391733952-3059161487-1245441232
map    group cn            sAMAccountName
```

## Configure LDAP Authorization

Linux uses the *sudo* command to allow non-administrator users (such as the default *cumulus* user account) to perform privileged operations. To control the users that can use sudo, define a series of rules in the `/etc/sudoers` file and files in the `/etc/sudoers.d/` directory. The rules apply to groups but you can also define specific users. You can add sudo rules using the group names from LDAP. For example, if a group of users are in the group *netadmin*, you can add a rule to give those users sudo privileges. Refer to the sudoers manual (`man sudoers`) for a complete usage description. The following shows an example in the `/etc/sudoers` file:

```
# The basic structure of a user specification is "who where = (as_whom) what ".
%sudo ALL=(ALL:ALL) ALL
%netadmin ALL=(ALL:ALL) ALL
```

## Active Directory Configuration

Active Directory (AD) is a fully featured LDAP-based NIS server create by Microsoft. It offers unique features that classic OpenLDAP servers do not have. AD can be more complicated to configure on the client and each version works a little differently with Linux-based LDAP clients. Some more advanced configuration examples, from testing LDAP clients on Cumulus Linux with Active Directory (AD/LDAP), are available in the [knowledge base]({{<ref "/knowledge-base/Security/Authentication/LDAP-on-Cumulus-Linux-Using-Server-2008-Active-Directory" >}}).

## LDAP Verification Tools

The LDAP client daemon retrieves and caches password and group information from LDAP. To verify the LDAP interaction, use these command-line tools to trigger an LDAP query from the device.

### Identify a User with the id Command

The `id` command performs a username lookup by following the lookup information sources in NSS for the *passwd* service. This returns the user ID, group ID and the group list retrieved from the information source. In the following example, the user *cumulus* is locally defined in `/etc/passwd`, and *myuser* is on LDAP. The NSS configuration has the `passwd` map configured with the sources `compat ldap`:

```
cumulus@switch:~$ id cumulus
uid=1000(cumulus) gid=1000(cumulus) groups=1000(cumulus),24(cdrom),25(floppy),27(sudo),29(audio),30(dip),44(video),46(plugdev)
cumulus@switch:~$ id myuser
uid=1230(myuser) gid=3000(Development) groups=3000(Development),500(Employees),27(sudo)
```

### getent

The `getent` command retrieves all records found with NSS for a given map. It can also retrieve a specific entry under that map. You can perform tests with the `passwd`, `group`, `shadow`, or any other map in the `/etc/nsswitch.conf` file. The output from this command formats according to the map requested. For the  `passwd` service, the structure of the output is the same as the entries in `/etc/passwd`. The group map outputs the same structure as `/etc/group`.

In this example, looking up a specific user in the `passwd` map, the user *cumulus* is locally defined in `/etc/passwd`, and *myuser* is only in LDAP.

```
cumulus@switch:~$ getent passwd cumulus
cumulus:x:1000:1000::/home/cumulus:/bin/bash
cumulus@switch:~$ getent passwd myuser
myuser:x:1230:3000:My Test User:/home/myuser:/bin/bash
```

In the next example, looking up a specific group in the group service, the group *cumulus* is locally defined in `/etc/groups`, and *netadmin* is on LDAP.

```
cumulus@switch:~$ getent group cumulus
cumulus:x:1000:
cumulus@switch:~$ getent group netadmin
netadmin:*:502:larry,moe,curly,shemp
```

Running the command `getent passwd` or `getent group` without a specific request returns **all** local and LDAP entries for the *passwd* and *group* maps.

### LDAP search

The `ldapsearch` command performs LDAP operations directly on the LDAP server. This does not interact with NSS. This command displays the information that the LDAP daemon process receives back from the server. The command has several options. The simplest option uses anonymous bind to the host and specifies the search DN and the attribute to look up.

```
cumulus@switch:~$ ldapsearch -H ldap://ldap.example.com -b dc=example,dc=com -x uid=myuser
```

{{< expand "Click to expand the command output "  >}}

```
# extended LDIF
#
# LDAPv3
# base <dc=example,dc=com> with scope subtree
# filter: uid=myuser
# requesting: ALL
#
# myuser, people, example.com
dn: uid=myuser,ou=people,dc=example,dc=com
cn: My User
displayName: My User
gecos: myuser
gidNumber: 3000
givenName: My
homeDirectory: /home/myuser
initials: MU
loginShell: /bin/bash
mail: myuser@example.com
objectClass: inetOrgPerson
objectClass: posixAccount
objectClass: shadowAccount
objectClass: top
shadowExpire: -1
shadowFlag: 0
shadowMax: 999999
shadowMin: 8
shadowWarning: 7
sn: User
uid: myuser
uidNumber: 1234

# search result
search: 2
result: 0 Success

# numResponses: 2
# numEntries: 1
```

{{< /expand >}}

### LDAP Browsers

The GUI LDAP clients are free tools that show the structure of the LDAP database graphically.

- {{<exlink url="http://directory.apache.org/studio/" text="Apache Directory Studio">}}
- {{<exlink url="http://ldapmanager.sourceforge.net/" text="LDAPManager">}}

## Troubleshooting

### nslcd Debug Mode

When setting up LDAP authentication for the first time, turn off the `nslcd` service using the `systemctl stop nslcd.service` command (or the `systemctl stop nslcd@mgmt.service` if you are running the service in a management VRF) and run it in debug mode. Debug mode works whether you are using LDAP over SSL (port 636) or an unencrypted LDAP connection (port 389).

```
cumulus@switch:~$ sudo systemctl stop nslcd.service
cumulus@switch:~$ sudo nslcd -d
```

After you enable debug mode, run the following command to test LDAP queries:

```
cumulus@switch:~$ getent passwd
```

If you configure LDAP correctly, the following messages appear after you run the `getent` command:

```
nslcd: DEBUG: accept() failed (ignored): Resource temporarily unavailable
nslcd: [8e1f29] DEBUG: connection from pid=11766 uid=0 gid=0
nslcd: [8e1f29] <passwd(all)> DEBUG: myldap_search(base="dc=example,dc=com", filter="(objectClass=posixAccount)")
nslcd: [8e1f29] <passwd(all)> DEBUG: ldap_result(): uid=myuser,ou=people,dc=example,dc=com
nslcd: [8e1f29] <passwd(all)> DEBUG: ldap_result(): ... 152 more results
nslcd: [8e1f29] <passwd(all)> DEBUG: ldap_result(): end of results (162 total)
```

In the example output above, `<passwd(all)>` shows a query of the entire directory structure.

You can query a specific user with the following command:

```
cumulus@switch:~$ getent passwd myuser
```

You can replace `myuser` with any username on the switch. The following debug output indicates that user `myuser` exists:

```
nslcd: DEBUG: add_uri(ldap://10.50.21.101)
nslcd: version 0.8.10 starting
nslcd: DEBUG: unlink() of /var/run/nslcd/socket failed (ignored): No such file or directory
nslcd: DEBUG: setgroups(0,NULL) done
nslcd: DEBUG: setgid(110) done
nslcd: DEBUG: setuid(107) done
nslcd: accepting connections
nslcd: DEBUG: accept() failed (ignored): Resource temporarily unavailable
nslcd: [8b4567] DEBUG: connection from pid=11369 uid=0 gid=0
nslcd: [8b4567] <passwd="myuser"> DEBUG: myldap_search(base="dc=cumulusnetworks,dc=com", filter="(&(objectClass=posixAccount)(uid=myuser))")
nslcd: [8b4567] <passwd="myuser"> DEBUG: ldap_initialize(ldap://<ip_address>)
nslcd: [8b4567] <passwd="myuser"> DEBUG: ldap_set_rebind_proc()
nslcd: [8b4567] <passwd="myuser"> DEBUG: ldap_set_option(LDAP_OPT_PROTOCOL_VERSION,3)
nslcd: [8b4567] <passwd="myuser"> DEBUG: ldap_set_option(LDAP_OPT_DEREF,0)
nslcd: [8b4567] <passwd="myuser"> DEBUG: ldap_set_option(LDAP_OPT_TIMELIMIT,0)
nslcd: [8b4567] <passwd="myuser"> DEBUG: ldap_set_option(LDAP_OPT_TIMEOUT,0)
nslcd: [8b4567] <passwd="myuser"> DEBUG: ldap_set_option(LDAP_OPT_NETWORK_TIMEOUT,0)
nslcd: [8b4567] <passwd="myuser"> DEBUG: ldap_set_option(LDAP_OPT_REFERRALS,LDAP_OPT_ON)
nslcd: [8b4567] <passwd="myuser"> DEBUG: ldap_set_option(LDAP_OPT_RESTART,LDAP_OPT_ON)
nslcd: [8b4567] <passwd="myuser"> DEBUG: ldap_simple_bind_s(NULL,NULL) (uri="ldap://<ip_address>")
nslcd: [8b4567] <passwd="myuser"> DEBUG: ldap_result(): end of results (0 total)
```

### Common Problems

#### SSL/TLS

- The FQDN of the LDAP server URI does not match the FQDN in the CA-signed server certificate.
- `nslcd` cannot read the SSL certificate and reports a *Permission denied* error in the debug during server connection negotiation. Check the permission on each directory in the path of the root SSL certificate. Ensure that it is readable by the `nslcd` user.

#### NSCD

- If the `nscd cache` daemon is also enabled and you make some changes to the user from LDAP, you can clear the cache using the following commands:

   ```
   nscd --invalidate = passwd
   nscd --invalidate = group
   ```

- The `nscd` package works with `nslcd` to cache name entries returned from the LDAP server. This sometimes causes authentication failures. To work around these issues, disable `nscd`, restart the `nslcd` service, then retry authentication:

   ```
   cumulus@switch:~$ sudo nscd -K
   cumulus@switch:~$ sudo systemctl restart nslcd.service
   ```

{{%notice note%}}
If you are running the `nslcd` service in a management VRF, you need to run the `systemctl restart nslcd@mgmt.service` command instead of the `systemctl restart nslcd.service` command. For example:

```
cumulus@switch:~$ sudo nscd -K
cumulus@switch:~$ sudo systemctl restart nslcd@mgmt.service
```
{{%/notice%}}

#### LDAP

- The search filter returns incorrect results. Check for typos in the search filter. Use `ldapsearch` to test your filter.
- Optionally, configure the basic LDAP connection and search parameters in `/etc/ldap/ldap.conf`.

   ```
   # ldapsearch -D 'cn=CLadmin' -w 'CuMuLuS' "(&(ObjectClass=inetOrgUser)(uid=myuser))"
   ```

## Related Information

- {{<exlink url="https://wiki.debian.org/LDAP/NSS" text="Debian - configuring LDAP authentication">}}
- {{<exlink url="https://wiki.debian.org/LDAP/PAM" text="Debian - configuring PAM to use LDAP">}}
- {{<exlink url="https://raw.githubusercontent.com/arthurdejong/nss-pam-ldapd/master/nslcd.conf" text="GitHub - Arthur de Jong nslcd.conf file">}}
- {{<exlink url="http://backports.debian.org/Instructions/" text="Debian backports">}}
-->