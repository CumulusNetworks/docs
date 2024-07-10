---
title: LDAP Authentication and Authorization
author: NVIDIA
weight: 170
toc: 4
---
Cumulus Linux uses Pluggable Authentication Modules (PAM) and Name Service Switch (NSS) for user authentication. NSS enables PAM to use LDAP to provide user authentication, group mapping, and information for other services on the system.
- NSS specifies the order of the information sources that resolve names for each service. Using NSS with authentication and authorization provides the order and location for user lookup and group mapping on the system.
- PAM handles the interaction between the user and the system, providing login handling, session setup, authentication of users, and authorization of user actions.

{{%notice note%}}
To configure LDAP authentication on Linux, you can use `libnss-ldap`, `libnss-ldapd`, or `libnss-sss`. This chapter describes `libnss-ldapd` only. From internal testing, this library works best with Cumulus Linux and is the easiest to configure, automate, and troubleshoot.
{{%/notice%}}

## Install libnss-ldapd

The `libldap-2.4-2` and `libldap-common` LDAP packages are already installed on the Cumulus Linux image; however you need to install these additional packages to use LDAP authentication:

- `libnss-ldapd`
- `libpam-ldapd`
- `ldap-utils`

To install the additional packages, run the following command:

```
cumulus@switch:~$ sudo apt-get install libnss-ldapd libpam-ldapd ldap-utils nslcd
```

You can also install these packages even if the switch does not connect to the internet, as they are in the `cumulus-local-apt-archive` repository that is {{<link url="Adding-and-Updating-Packages#add-packages-from-the-cumulus-linux-local-archive" text="embedded">}} in the Cumulus Linux image.

Follow the interactive prompts to specify the LDAP URI, search base distinguished name (DN), and services that must have LDAP lookups enabled. You need to select at least the `passwd`, `group`, and `shadow` services (press space to select a service). When done, select OK. This creates a basic LDAP configuration using anonymous bind and initiates user search under the base DN specified.

After the dialog closes, the install process prints information similar to the following:

```
/etc/nsswitch.conf: enable LDAP lookups for group
/etc/nsswitch.conf: enable LDAP lookups for passwd
/etc/nsswitch.conf: enable LDAP lookups for shadow
```

After the installation is complete, the *name service caching daemon* (`nslcd`) runs. This service handles all the LDAP protocol interactions and caches information that returns from the LDAP server. `nslcd` appends `ldap` to the `/etc/nsswitch.conf` file, as well as the secondary information source for *passwd*, *group*, and *shadow*. `nslcd` references the local files (`/etc/passwd`, `/etc/groups` and `/etc/shadow`) first, as specified by the `compat` source.

```
passwd: compat ldap
group: compat ldap
shadow: compat ldap
```

{{%notice warning%}}
Keep `compat` as the first source in NSS for *passwd*, *group*, and *shadow*. This prevents you from getting locked out of the system.
{{%/notice%}}

Entering incorrect information during the installation process produces configuration errors. You can correct the information after installation by editing certain configuration files.

- Edit the `/etc/nslcd.conf` file to update the LDAP URI and search base DN (see {{<link url="#update-the-nslcdconf-file" text="Update the nslcd.conf File">}}, below).
- Edit the `/etc/nssswitch.conf` file to update the service selections.

Be sure to restart `nvued.service` after editing the files.

```
cumulus@switch:~$ sudo systemctl restart nvued.service
```

{{< expand "Alternative Installation Method Using debconf-utils "  >}}

Instead of running the installer and following the interactive prompts, as described above, you can pre-seed the installer parameters using `debconf-utils`.

1. Run `apt-get install debconf-utils` and create the pre-seeded parameters using `debconf-set-selections`. Provide the appropriate answers.
2. Run `debconf-show <pkg>` to check the settings. Here is an example of how to pre-seed answers to the installer questions using `debconf-set-selections`:

   ```
   root# debconf-set-selections <<'zzzEndOfFilezzz'

   # LDAP database user. Leave blank will be populated later!

   nslcd nslcd/ldap-binddn  string

   # LDAP user password. Leave blank!
   nslcd nslcd/ldap-bindpw   password

   # LDAP server search base:
   nslcd nslcd/ldap-base string  ou=support,dc=rtp,dc=example,dc=test

   # LDAP server URI. Using ldap over ssl.
   nslcd nslcd/ldap-uris string  ldaps://myadserver.rtp.example.test

   # New to 0.9. restart cron, exim and others libraries without asking
   nslcd libraries/restart-without-asking: boolean true

   # LDAP authentication to use:
   # Choices: none, simple, SASL
   # Using simple because its easy to configure. Security comes by using LDAP over SSL
   # keep /etc/nslcd.conf 'rw' to root for basic security of bindDN password
   nslcd nslcd/ldap-auth-type    select  simple

   # Don't set starttls to true
   nslcd nslcd/ldap-starttls     boolean false

   # Check server's SSL certificate:
   # Choices: never, allow, try, demand
   nslcd nslcd/ldap-reqcert      select  never

   # Choices: Ccreds credential caching - password saving, Unix authentication, LDAP Authentication , Create home directory on first time login, Ccreds credential caching - password checking
   # This is where "mkhomedir" pam config is activated that allows automatic creation of home directory
   libpam-runtime        libpam-runtime/profiles multiselect     ccreds-save, unix, ldap, mkhomedir , ccreds-check

   # for internal use; can be preseeded
   man-db        man-db/auto-update      boolean true

   # Name services to configure:
   # Choices: aliases, ethers, group, hosts, netgroup, networks, passwd, protocols, rpc, services,  shadow
   libnss-ldapd  libnss-ldapd/nsswitch   multiselect     group, passwd, shadow
   libnss-ldapd  libnss-ldapd/clean_nsswitch     boolean false

   ## define platform specific libnss-ldapd debconf questions/answers. 
   ## For demo used amd64.
   libnss-ldapd:amd64    libnss-ldapd/nsswitch   multiselect     group, passwd, shadow
   libnss-ldapd:amd64    libnss-ldapd/clean_nsswitch     boolean false
   # libnss-ldapd:powerpc   libnss-ldapd/nsswitch   multiselect     group, passwd, shadow
   # libnss-ldapd:powerpc    libnss-ldapd/clean_nsswitch     boolean false
   ```

{{< /expand >}}

## Configure LDAP Server Settings

After installation, update the main configuration file (`/etc/nslcd.conf`) to accommodate the expected LDAP server settings.

This section documents some of the more important options that relate to security and queries. For details on all the available configuration options, read the {{<exlink url="http://linux.die.net/man/5/nslcd.conf" text="nslcd.conf man page">}}.

{{%notice note%}}
After first editing the `/etc/nslcd.conf` file or enabling LDAP in the `/etc/nsswitch.conf` file, you must restart `netd` with the `sudo systemctl restart netd` command. If you disable LDAP, you need to restart the `netd` service.
{{%/notice%}}

### Connection

The LDAP client starts a session by connecting to the LDAP server on TCP and UDP port 389 or on port 636 for LDAPS. Depending on the configuration, this connection establishes without authentication (anonymous bind); otherwise, the client must provide a bind user and password. The variables you use to define the connection to the LDAP server are the URI and bind credentials.

The URI is mandatory and specifies the LDAP server location using the FQDN or IP address. The URI also designates whether to use `ldap://` for clear text transport, or `ldaps://` for SSL/TLS encrypted transport. You can also specify an alternate port in the URI. In production environments, use the LDAPS protocol so that all communications are secure.

After the connection to the server is complete, the BIND operation authenticates the session. The BIND credentials are optional; if you do not specify the credentials, the switch assumes an anonymous bind. Configure authenticated (Simple) BIND by specifying the user (`binddn`) and password (`bindpw`) in the configuration. Another option is to use SASL (Simple Authentication and Security Layer) BIND, which provides authentication services using other mechanisms, like Kerberos. Contact your LDAP server administrator for this information as it depends on the configuration of the LDAP server and the credentials for the client device.

{{< tabs "TabID145 ">}}
{{< tab "NVUE Commands ">}}

```
cumulus@switch:~$ nv set system aaa ldap uri ldaps://ldap.example.com priority 1
cumulus@switch:~$ nv set system aaa ldap bind-dn cn=CLswitch,dc=example,dc=com
cumulus@switch:~$ nv set system aaa ldap bind-password CuMuLuS
cumulus@switch:~$ nv config apply
```

{{< /tab >}}
{{< tab "Linux Commands ">}}

Edit the `/etc/nslcd.conf` file to add the URI and BIND credentials:

```
cumulus@switch:~$ sudo nano /etc/nslcd.conf
...
# The location at which the LDAP server(s) should be reachable.
uri ldaps://ldap.example.com
# The DN to bind with for normal lookups.
binddn cn=CLswitch,ou=infra,dc=example,dc=com
bindpw CuMuLuS
```

{{< /tab >}}
{{< /tabs >}}

### Search Function

When an LDAP client requests information about a resource, it must connect and bind to the server. Then, it performs one or more resource queries depending on the lookup. All search queries to the LDAP server use the configured search *base*, *filter*, and the desired entry (*uid=myuser*). If the LDAP directory is large, this search takes a long time. Define a more specific search base for the common *maps* (*passwd* and *group*).

{{< tabs "TabID176 ">}}
{{< tab "NVUE Commands ">}}

```
cumulus@switch:~$ nv set system aaa ldap base-dn dc=example,dc=com
cumulus@switch:~$ nv config apply
```

{{< /tab >}}
{{< tab "Linux Commands ">}}

Edit the `/etc/nsswitch.conf` file to add the search base:

```
cumulus@switch:~$ sudo nano /etc/nsswitch.conf
...
# The search base that will be used for all queries.
base dc=example,dc=com
# Mapped search bases to speed up common queries.
base passwd ou=people,dc=example,dc=com
base group ou=groups,dc=example,dc=com
```

{{< /tab >}}
{{< /tabs >}}

### Search Scope

You can configure the search scope to one level or the subtree.

{{< tabs "TabID206 ">}}
{{< tab "NVUE Commands ">}}

To set the search scope to one level:

```
cumulus@switch:~$ nv set system aaa ldap scope one-level
cumulus@switch:~$ nv config apply
```

To set the search scope to subtree:

```
cumulus@switch:~$ nv set system aaa ldap scope subtree
cumulus@switch:~$ nv config apply
```

{{< /tab >}}
{{< tab "Linux Commands ">}}

Edit the `/etc/nsswitch.conf` file to set the `scope` option to either `one` or `sub` and uncomment the line.

```
cumulus@switch:~$ sudo nano /etc/nslcd.conf
...
# The search scope.
scope one
...
```

{{< /tab >}}
{{< /tabs >}}

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

### LDAP Version

Cumulus Linux uses LDAP version 3 by default. If you need to change the LDAP version to 2:

{{< tabs "TabID265 ">}}
{{< tab "NVUE Commands ">}}

```
cumulus@switch:~$ nv set system aaa ldap version 2
cumulus@switch:~$ nv config apply
```

{{< /tab >}}
{{< tab "Linux Commands ">}}

Edit the `/etc/nsswitch.conf` file to change the `ldap_version` option and uncomment the line.

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
- The bind timeout sets the number of seconds before the BIND operation times out.
- The search timeout sets the number of seconds before the search times out.

{{< tabs "TabID295 ">}}
{{< tab "NVUE Commands ">}}

The following example sets both the BIND session timeout and the search timeout to 60 seconds:

```
cumulus@switch:~$ nv set system aaa ldap timeout-bind 60
cumulus@switch:~$ nv set system aaa ldap timeout-search 60
cumulus@switch:~$ nv config apply
```

{{< /tab >}}
{{< tab "Linux Commands ">}}

Edit the `/etc/nsswitch.conf` file to add the `bind_timelimit` option and the `timelimit` option.

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

{{< tabs "TabID324 ">}}
{{< tab "NVUE Commands ">}}

```
cumulus@switch:~$ nv set system aaa ldap ssl mode
cumulus@switch:~$ nv set system aaa ldap ssl port
cumulus@switch:~$ nv set system aaa ldap ssl cert-verify
cumulus@switch:~$ nv set system aaa ldap ssl ca-list
cumulus@switch:~$ nv set system aaa ldap ssl ciphers
cumulus@switch:~$ nv set system aaa ldap ssl crl-check
cumulus@switch:~$ nv config apply
```

{{< /tab >}}
{{< tab "Linux Commands ">}}

Edit the `/etc/nsswitch.conf` file to

```
cumulus@switch:~$ sudo nano /etc/nslcd.conf
...
# SSL options
ssl on
tls_reqcert try
tls_cacertfile /etc/ssl/certs/rtp-example-ca.crt
...
```

{{< /tab >}}
{{< /tabs >}}

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

Here is an example configuration using Cumulus Linux.

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
