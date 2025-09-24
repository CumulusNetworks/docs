---
title: LDAP Authentication and Authorization
author: NVIDIA
weight: 170
toc: 4
---
<!-- vale off -->
Cumulus Linux uses Pluggable Authentication Modules (PAM) and Name Service Switch (NSS) for user authentication. NSS enables PAM to use LDAP to provide user authentication, group mapping, and information for other services on the system.
<!-- vale on -->
- NSS specifies the order of the information sources that resolve names for each service. Using NSS with authentication and authorization provides the order and location for user lookup and group mapping on the system.
- PAM handles the interaction between the user and the system, providing login handling, session setup, authentication of users, and authorization of user actions.

NVUE manages LDAP authentication with PAM and NSS.

{{%notice note%}}
- LDAP authentication is sensitive to network delay. For optimal performance, NVIDIA recommends a round trip time of 10ms or less between LDAP clients and the LDAP server. If latency is between 10-50ms, NVIDIA recommends changing the [authentication order](#set-the-authentication-order) to prioritize local authentication before LDAP. For connections exceeding 50ms of latency, authentication might experience unacceptable delays; consider alternative authentication methods.
{{%/notice%}}

## Configure LDAP Server Settings

You can configure LDAP server settings with NVUE commands or by editing Linux configuration files.

{{%notice note%}}
If you edit Linux configuration files instead of using NVUE, you must:
- Configure PAM to use LDAP with the `sudo pam-auth-update --enable ldap` command.
- Restart NVUE with the `sudo systemctl restart nvued.service` command after editing the `/etc/nslcd.conf` file or the `/etc/nsswitch.conf` file.
{{%/notice%}}

### Connection

Configure the following connection settings:
- The hostname or IP address of the LDAP server from which you want to import users. If you use multiple LDAP servers, you can also set a priority for each server.
- The port number of the LDAP server if you are using a non-default port. The default port number for LDAP is TCP and UDP port 389.
- Authenticated (Simple) BIND credentials. The BIND credentials are optional; if you do not specify the credentials, the switch assumes an anonymous bind. To use SASL (Simple Authentication and Security Layer) BIND, which provides authentication services using other mechanisms such as Kerberos, contact your LDAP server administrator for authentication information.

The following example configures the LDAP server and port, and the BIND credentials.

{{< tabs "TabID32 ">}}
{{< tab "NVUE Commands ">}}

```
cumulus@switch:~$ nv set system aaa ldap server ldapserver1
cumulus@switch:~$ nv set system aaa ldap port 388
cumulus@switch:~$ nv set system aaa ldap bind-dn CN=cumulus-admin,CN=Users,DC=rtp,DC=example,DC=test
cumulus@switch:~$ nv set system aaa ldap secret 1Q2w3e4r!
cumulus@switch:~$ nv config apply
```

The following example sets the priority to 2 for ldapserver2 when using multiple LDAP servers:

```
cumulus@switch:~$ nv set system aaa ldap server ldapserver2 priority 2
```

{{< /tab >}}
{{< tab "Linux Commands ">}}

Edit the `/etc/nslcd.conf` file to set the URI and BIND credentials, then uncomment the lines:

```
cumulus@switch:~$ sudo nano /etc/nslcd.conf
...
# The location at which the LDAP server(s) should be reachable.
uri ldaps://ldapserver1:388/
#uripriority 1
...
# The DN to bind with for normal lookups.
binddn CN=cumulus admin,CN=Users,DC=rtp,DC=example,DC=test
bindpw 1Q2w3e4r!
...
```

{{< /tab >}}
{{< /tabs >}}

{{%notice note%}}
Cumulus Linux does not support LDAP with IPv6 and SSL or Start TLS. To use IPv6 with SSL or Start TLS, you must set the hostname of the LDAP server instead of the IPv6 address with the `nv set system aaa ldap server <hostname>` command.

If no DNS record exists for the IP address, first create a local entry in the `/etc/hosts` file with an NVUE snippet, then set the LDAP server hostname:

```
cumulus@switch:~$ sudo nano hosts-add.yaml
- set:
    system:
      config:
        snippet:
          hosts_local_entry:         # unique name
            file: "/etc/hosts"
            content: |
              ffd:fdfd:10:37:20:56:e1b:34 ldap.server.local
```

```
cumulus@switch:~$ nv config patch /path/to/hosts-add.yaml
cumulus@switch:~$ nv config apply
cumulus@switch:~$ nv set system aaa ldap server ldap.server.local
```

{{%/notice%}}

### Set the Authentication Order

To prioritize the order in which Cumulus Linux attempts different authentication methods to verify user access to the switch, you set the authentication order. By default, Cumulus Linux verifies users according to their local passwords.

If you set the authentication order to start with LDAP, but the LDAP servers do not have the user in the directory or does not respond, Cumulus Linux tries local password authentication.

To set the authentication order to start with LDAP before local authentication:

{{< tabs "TabID262 ">}}
{{< tab "NVUE Commands ">}}

```
cumulus@switch:~$ nv set system aaa authentication-order 1 ldap
cumulus@switch:~$ nv config apply
```

To set the authentication order to start with local authentication before querying LDAP:

```
cumulus@switch:~$ nv set system aaa authentication-order 1 local
cumulus@switch:~$ nv set system aaa authentication-order 2 ldap
cumulus@switch:~$ nv config apply
```

{{< /tab >}}
{{< tab "Linux Commands ">}}

Edit the `/etc/nsswitch.conf` file and add `ldap` before `files` for the `passwd` and `group` options to attempt LDAP authentication first, or configure `files` first to prioritize local authentication:

```
cumulus@switch:~$ sudo nano /etc/nsswitch.conf
...
passwd:         ldap files
group:          ldap files
shadow:         files
gshadow:        files

hosts:          files dns
networks:       files

protocols:      db files
services:       db files
ethers:         db files
rpc:            db files
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

NVUE does not provide commands to limit the search scope.
<!--
```
cumulus@switch:~$ nv set system aaa ldap filter passwd cumulus
cumulus@switch:~$ nv set system aaa ldap filter group cn
cumulus@switch:~$ nv set system aaa ldap filter shadow 1234
cumulus@switch:~$ nv config apply
```
-->
{{< /tab >}}
{{< tab "Linux Commands ">}}

Edit the `/etc/nslcd.conf` file to set the `filter passwd`, `filter group`, or `filter shadow` options.

```
cumulus@switch:~$ sudo nano /etc/nslcd.conf
...
# filters and maps
filter passwd cumulus
filter group cn
filter shadow 1234
...
```

{{< /tab >}}
{{< /tabs >}}

### Attribute Mapping

The *map* configuration allows you to override the attributes pushed from LDAP. To override an attribute for a given *map*, specify the attribute name and the new value.

{{< tabs "TabID166 ">}}
{{< tab "NVUE Commands ">}}

NVUE does not provide commands for attribute mapping.
<!--
```
cumulus@switch:~$ nv set system aaa ldap map passwd homedirectory /home/$sAMAccountName
cumulus@switch:~$ nv set system aaa ldap map passwd userpassword cumulus
cumulus@switch:~$ nv set system aaa ldap map group cn sAMAccountName
cumulus@switch:~$ nv set system aaa ldap map group gidnumber objectSid:S-1-5-21-1391733952-3059161487-1245441232
cumulus@switch:~$ nv config apply
```
-->
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

Edit the `/etc/etc/nslcd.conf` file to change the `ldap_version`.

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
- SSL mode. You can specify, `none`, `ssl`, or `start-tls`.
- SL port.
- SSL certificate validation.
- SSL cipher suites. You can specify TLS1.2, TLS1.3, TLS-CIPHERS, or all.
- SSL <span class="a-tooltip">[CRL](## "Certificate Revocation List")</span> check.

{{%notice note%}}
To use IPv6 with SSL or Start TLS, you must set the hostname of the LDAP server instead of the IPv6 address with the `nv set system aaa ldap server <hostname>` command. See {{<link url="#configure-ldap-server-settings" text="Configure LDAP Server Settings">}}.
{{%/notice%}}

The following example sets the SSL mode to SSL, the port to 8443, enables the SSL certificate checker, sets the SSL cipher suites to TLS1.3 and the Certificate Revocation List to /etc/ssl/certs/rtp-example-ca.crt.

{{< tabs "TabID270 ">}}
{{< tab "NVUE Commands ">}}

```
cumulus@switch:~$ nv set system aaa ldap ssl mode ssl
cumulus@switch:~$ nv set system aaa ldap ssl port 8443
cumulus@switch:~$ nv set system aaa ldap ssl cert-verify enabled 
cumulus@switch:~$ nv set system aaa ldap ssl tls-ciphers TLS1.3
cumulus@switch:~$ nv set system aaa ldap ssl crl-file /etc/ssl/certs/rtp-example-ca.crt
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

LDAP referrals allow you to partition a directory tree and distribute it between multiple LDAP servers.

To enable LDAP referral:

{{< tabs "TabID309 ">}}
{{< tab "NVUE Commands ">}}

```
cumulus@switch:~$ nv set system aaa ldap referrals enabled
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
- `nv show system aaa ldap server` shows the configured LDAP servers and their priorities.
- `nv show system aaa ldap server <server-id>` shows the priority for the specified LDAP server.
- `nv show system aaa ldap ssl` shows the LDAP SSL configuration settings.

The following example shows all the LDAP configuration settings:

```
cumulus@switch:~$ nv show system aaa ldap
                operational                                          applied                                            
--------------  ---------------------------------------------------  ---------------------------------------------------
bind-dn         CN=cumulus-admin,CN=Users,DC=rtp,DC=example,DC=test  CN=cumulus-admin,CN=Users,DC=rtp,DC=example,DC=test
base-dn         ou=users,dc=example,dc=com                           ou=users,dc=example,dc=com                         
referrals       yes                                                  off                                                
scope           sub                                                  subtree                                            
port            389                                                  388                                                
timeout-bind    5                                                    5                                                  
timeout-search  5                                                    5                                                  
secret          $nvsec$4fb719e24167246947d4f746f58696fc              $nvsec$4fb719e24167246947d4f746f58696fc            
version         3                                                    3                                                  
vrf             default                                              mgmt                                               
[server]        ldapserver1                                          ldapserver1                                        
ssl                                                                                                                     
  mode          ssl                                                  ssl                                                
  port          8443                                                 8443                                               
  cert-verify   enabled                                              enabled                                            
  tls-ciphers   TLS1.3                                               TLS1.3                                             
  crl-file      /etc/ssl/certs/rtp-example-ca.crt                    /etc/ssl/certs/rtp-example-ca.crt
...
```

The following example shows the configured LDAP servers and their priorities:

```
cumulus@switch:~$ nv show system aaa ldap server
Hostname     Priority
-----------  --------
ldapserver1  1
ldapserver2  2     
```

The following example shows the SSL configuration settings:

```
cumulus@switch:~$ nv show system aaa ldap ssl
             operational                        applied                          
-----------  ---------------------------------  ---------------------------------
mode         ssl                                ssl                              
port         8443                               8443                             
cert-verify  enabled                            enabled                          
tls-ciphers  TLS1.3                             TLS1.3                           
crl-file     /etc/ssl/certs/rtp-example-ca.crt  /etc/ssl/certs/rtp-example-ca.crt
```
<!--
The following example shows the search map group configuration settings:

```
cumulus@switch:~$ nv show system aaa ldap map group
           operational                                          applied                                            
---------  ---------------------------------------------------  ---------------------------------------------------
cn         sAMAccountName                                       sAMAccountName                                     
memberuid                                                                                                          
gidnumber  objectSid:S-1-5-21-1391733952-3059161487-1245441232  objectSid:S-1-5-21-1391733952-3059161487-1245441232
```
-->
## Configure LDAP Authorization

Linux uses the *sudo* command to allow non-administrator users (such as the default *cumulus* user account) to perform privileged operations. To control the users that can use sudo, define a series of rules in the `/etc/sudoers` file and files in the `/etc/sudoers.d/` directory. The rules apply to groups but you can also define specific users. You can add sudo rules using the group names from LDAP. For example, if a group of users are in the group *netadmin*, you can add a rule to give those users sudo privileges. Refer to the sudoers manual (`man sudoers`) for a complete usage description. The following shows an example in the `/etc/sudoers` file:

```
# The basic structure of a user specification is "who where = (as_whom) what ".
%sudo ALL=(ALL:ALL) ALL
%netadmin ALL=(ALL:ALL) ALL
```

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

The `getent` command retrieves all records found with NSS for a given map. It can also retrieve a specific entry under that map. You can perform tests with the `passwd`, `group`, `shadow`, or any other map in the `/etc/nslcd.conf` file. The output from this command formats according to the map requested. For the  `passwd` service, the structure of the output is the same as the entries in `/etc/passwd`. The group map outputs the same structure as `/etc/group`.

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

## Related Information

- {{<exlink url="https://wiki.debian.org/LDAP/NSS" text="Debian - configuring LDAP authentication">}}
- {{<exlink url="https://wiki.debian.org/LDAP/PAM" text="Debian - configuring PAM to use LDAP">}}
