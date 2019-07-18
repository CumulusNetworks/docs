---
title: LDAP Authentication and Authorization
author: Cumulus Networks
weight: 261
aliases:
 - /display/CL321/LDAP+Authentication+and+Authorization
 - /pages/viewpage.action?pageId=5126754
pageID: 5126754
product: Cumulus Linux
version: 3.2.1
imgData: cumulus-linux-321
siteSlug: cumulus-linux-321
---
<details>

Cumulus Linux uses Pluggable Authentication Modules (PAM) and Name
Service Switch (NSS) for user authentication.

NSS specifies the order of information sources used to resolve names for
each service. Using this with authentication and authorization, it
provides the order and location used for user lookup and group mapping
on the system. PAM handles the interaction between the user and the
system, providing login handling, session setup, authentication of users
and authorization of a user actions.

NSS enables PAM to use LDAP for providing user authentication, group
mapping and information for other services on the system.

## <span>Configuring LDAP Authentication</span>

There are 3 common ways of configuring LDAP authentication on Linux:

  - libnss-ldap

  - libnss-ldapd

  - libnss-sss

This chapter covers using `libnss-ldapd` only. From internal testing,
this library worked best with Cumulus Linux and was the easiest to
configure, automate and troubleshoot.

## <span>Installing libnss-ldapd</span>

The `libpam-ldapd` package depends on `nslcd`, so to install
`libnss-ldapd`, `libpam-ldapd` and `ldap-utils`, you must run:

    cumulus@switch:~$ sudo apt-get install libnss-ldapd libpam-ldapd ldap-utils nslcd

This brings up an interactive prompt asking questions about the LDAP
URI, search base distinguished name (DN) and services that should have
LDAP lookups enabled. This creates a very basic LDAP configuration,
using anonymous bind, and initiating the search for a user under the
base DN specified.

{{%notice note%}}

Alternatively, these parameters can be pre-seeded using the
`debconf-utils`. To use this method, run `apt-get install debconf-utils`
and create the pre-seeded parameters using `debconf-set-selections` with
the appropriate answers. Run `debconf-show <pkg>` to check the settings.
Here is an [example of how to preseed answers to the installer questions
using `debconf-set-selections`](attachments_5126753_1_kb_debconf.txt) .

{{%/notice%}}

Once the install is complete, the *name service LDAP caching daemon*
(`nslcd`) will be running. This is the service that handles all of the
LDAP protocol interactions, and caches the information returned from the
LDAP server. In `/etc/nsswitch.conf`, ` ldap  `has been appended and is
the secondary information source for *passwd*, *group* and *shadow*. The
local files (`/etc/passwd`, `/etc/groups` and `/etc/shadow`) are used
first, as specified by the `compat` source.

    passwd: compat ldap
    group: compat ldap
    shadow: compat ldap

{{%notice warning%}}

You are strongly advised to keep `compat` as the first source in NSS for
*passwd*, *group* and *shadow*. This prevents you from getting locked
out of the system.

{{%/notice%}}

## <span>Configuring nslcd.conf</span>

You need to update the main configuration file (`/etc/nslcd.conf`) after
installation to accommodate the expected LDAP server settings. The
[nslcd.conf man page](http://linux.die.net/man/5/nslcd.conf) details all
the available configuration options. Some of the more important options
are related to security and how the queries are handled.

### <span>Connection</span>

The LDAP client starts a session by connecting to the LDAP server, by
default, on TCP and UDP port 389, or on port 636 for LDAPS. Depending on
the configuration, this connection may be unauthenticated (anonymous
bind); otherwise, the client must provide a bind user and password. The
variables used to define the connection to the LDAP server are the URI
and bind credentials.

The URI is mandatory, and specifies the LDAP server location using the
FQDN or IP address. It also designates whether to use ldap:// for clear
text transport, or ldaps:// for SSL/TLS encrypted transport. Optionally,
an alternate port may also be specified in the URI. Typically, in
production environments, it is best to utilize the LDAPS protocol.
Otherwise all communications are clear text and not secure.

After the connection to the server is complete, the BIND operation
authenticates the session. The BIND credentials are optional, and if not
specified, an anonymous bind is assumed. This is typically not allowed
in most production environments. Configure authenticated (Simple) BIND
by specifying the user (*binddn*) and password (*bindpw*) in the
configuration. Another option is to use SASL (Simple Authentication and
Security Layer) BIND, which provides authentication services using other
mechanisms, like Kerberos. Contact your LDAP server administrator for
this information since it depends on the configuration of the LDAP
server and what credentials are created for the client device.

    # The location at which the LDAP server(s) should be reachable.
    uri ldaps://ldap.example.com
    # The DN to bind with for normal lookups.
    binddn cn=CLswitch,ou=infra,dc=example,dc=com
    bindpw CuMuLuS

### <span>Search Function</span>

When an LDAP client requests information about a resource, it must
connect and bind to the server. Then it performs one or more resource
queries depending on what it is looking up. All search queries sent to
the LDAP server are created using the configured search *base*,
*filter*, and the desired entry (*uid=myuser*) being searched for. If
the LDAP directory is large, this search may take a significant amount
of time. It is a good idea to define a more specific search base for the
common *maps* (*passwd* and *group*).

    # The search base that will be used for all queries.
    base dc=example,dc=com
    # Mapped search bases to speed up common queries.
    base passwd ou=people,dc=example,dc=com
    base group ou=groups,dc=example,dc=com

### <span>Search Filters</span>

It is also common to use search filters to specify criteria used when
searching for objects within the directory. This is used to limit the
search scope when authenticating users. The default filters applied are:

    filter passwd (objectClass=posixAccount)
    filter group (objectClass=posixGroup) 

### <span>Attribute Mapping</span>

The *map* configuration allows for overriding the attributes pushed from
LDAP. To override an attribute for a given *map*\*, specify the
attribute name and the new value. One example of how this is useful is
ensuring the shell is *bash* and the home directory is `/home/cumulus`:

    map    passwd homeDirectory "/home/cumulus"
    map    passwd shell "/bin/bash"

{{%notice note%}}

\*In LDAP, the ***map*** refers to one of the supported maps specified
in the manpage for `nslcd.conf` (such as *passwd* or *group*).

{{%/notice%}}

### <span>Example Configuration</span>

Here is an [example
configuration ](attachments_5126755_1_nslcd.conf)using Cumulus Linux.

## <span>Troubleshooting</span>

### <span>Using nslcd Debug Mode</span>

When setting up LDAP authentication for the first time, Cumulus Networks
recommends you turn off this service using `systemctl stop
nslcd.service` and run it in debug mode. Debug mode works whether you
are using LDAP over SSL (port 636) or an unencrypted LDAP connection
(port 389).

    cumulus@switch:~$ sudo systemctl stop nslcd.service
    cumulus@switch:~$ sudo nslcd -d

Once you enable debug mode, run the following command to test LDAP
queries:

    cumulus@switch:~$ sudo getent myuser

If LDAP is configured correctly, the following messages appear after you
run the `getent` command:

    nslcd: DEBUG: accept() failed (ignored): Resource temporarily unavailable
    nslcd: [8e1f29] DEBUG: connection from pid=11766 uid=0 gid=0
    nslcd: [8e1f29] <passwd(all)> DEBUG: myldap_search(base="dc=example,dc=com", filter="(objectClass=posixAccount)")
    nslcd: [8e1f29] <passwd(all)> DEBUG: ldap_result(): uid=myuser,ou=people,dc=example,dc=com
    nslcd: [8e1f29] <passwd(all)> DEBUG: ldap_result(): ... 152 more results
    nslcd: [8e1f29] <passwd(all)> DEBUG: ldap_result(): end of results (162 total)

In the output above, *\<passwd(all)\>* indicates that the entire
directory structure was queried.

A specific user can be queried using the command:

    cumulus@switch:~$ sudo getent passwd myuser

You can replace *myuser* with any username on the switch. The following
debug output indicates that user *myuser* exists:

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

Notice how the `<passwd="myuser">` shows that the specific *myuser* user
was queried.

### <span>Common Problems</span>

#### <span>SSL/TLS</span>

  - The FQDN of the LDAP server URI does not match the FQDN in the
    CA-signed server certificate exactly.

  - `nslcd` cannot read the SSL certificate, and will report a
    "Permission denied" error in the debug during server connection
    negotiation. Check the permission on each directory in the path of
    the root SSL certificate. Ensure that it is readable by the `nslcd`
    user.

#### <span>NSCD</span>

  - If the `nscd cache` daemon is also enabled and you make some changes
    to the user from LDAP, you may want to clear the cache using the
    commands:
    
        nscd --invalidate = passwd 
        nscd --invalidate = group

  - The `nscd` package works with `nslcd` to cache name entries returned
    from the LDAP server. This may cause authentication failures. To
    work around these issues:
    
    1.  Disable `nscd` by running:
        
            cumulus@switch:~$ sudo nscd -K
    
    2.  Restart the `nslcd` service:
        
            cumulus@switch:~$ sudo systemctl restart nslcd.service
    
    3.  Try the authentication again.

#### <span>LDAP</span>

  - The search filter returns wrong results. Check for typos in the
    search filter. Use `ldapsearch` to test your filter.

  - Optionally, configure the basic LDAP connection and search
    parameters in `/etc/ldap/ldap.conf`.
    
        # ldapsearch -D 'cn=CLadmin' -w 'CuMuLuS' "(&(ObjectClass=inetOrgUser)(uid=myuser))"

  - When a local username also exists in the LDAP database, the order of
    the information sources in `/etc/nsswitch` can be updated to query
    LDAP before the local user database. This is generally not
    recommended. For example, the configuration below ensures that LDAP
    is queried before the local database.
    
        # /etc/nsswitch.conf
        passwd:         ldap compat

## <span>Configuring LDAP Authorization</span>

Linux uses the *sudo* command to allow non-administrator users — like
the default *cumulus* user account — to perform privileged operations.
To control the users authorized to use sudo, the `/etc/sudoers` file and
files located in the `/etc/sudoers.d/` directory have a series of rules
defined. Typically, the rules are based on groups, but can also be
defined for specific users. Therefore, sudo rules can be added using the
group names from LDAP. For example, if a group of users were associated
with the group *netadmin*, a rule can be added to give those users sudo
privileges. Refer to the sudoers manual (`man sudoers`) for a complete
usage description. Here's an illustration of this in `/etc/sudoers`:

    # The basic structure of a user specification is “who where = (as_whom) what”.
    %sudo ALL=(ALL:ALL) ALL
    %netadmin ALL=(ALL:ALL) ALL

## <span>Active Directory Configuration</span>

Active Directory (AD) is a fully featured LDAP-based NIS server created
by Microsoft. It offers unique features that classic OpenLDAP servers
lack. Therefore, it can be more complicated to configure on the client
and each version of AD is a little different in how it works with
Linux-based LDAP clients. Some more advanced configuration examples,
from testing LDAP clients on Cumulus Linux with Active Directory
(AD/LDAP), are available in our [knowledge
base](https://support.cumulusnetworks.com/hc/en-us/articles/204383797).

## <span>LDAP Verification Tools</span>

Typically, password and group information is retrieved from LDAP and
cached by the LDAP client daemon. To test the LDAP interaction, these
command line tools can be used to trigger an LDAP query from the device.
This helps to create the best filters and verify the information sent
back from the LDAP server.

### <span>Identifying a User with the id Command</span>

The `id` command performs a username lookup by following the lookup
information sources in NSS for the *passwd* service. This simply returns
the user ID, group ID and the group list retrieved from the information
source. In the following example, the user *cumulus* is locally defined
in `/etc/passwd`, and *myuser* is on LDAP. The NSS configuration has the
passwd map configured with the sources `compat ldap`:

    cumulus@switch:~$ id cumulus
    uid=1000(cumulus) gid=1000(cumulus) groups=1000(cumulus),24(cdrom),25(floppy),27(sudo),29(audio),30(dip),44(video),46(plugdev)
    cumulus@switch:~$ id myuser 
    uid=1230(myuser) gid=3000(Development) groups=3000(Development),500(Employees),27(sudo)

### <span>Using getent</span>

The `getent` command retrieves all records found via NSS for a given
map. It can also get a specific entry under that map. Tests can be done
with the passwd, group, shadow or any other map configured in
`/etc/nsswitch.conf`. The output from this command is formatted
according to the map requested. Thus, for the passwd service, the
structure of the output is the same as the entries in `/etc/passwd`. The
same can be said for the group map will output the same as `/etc/group`.
In this example, looking up a specific user in the passwd map, the user
*cumulus* is locally defined in `/etc/passwd`, and *myuser* is only in
LDAP.

    cumulus@switch:~$ getent passwd cumulus
    cumulus:x:1000:1000::/home/cumulus:/bin/bash
    cumulus@switch:~$ getent passwd myuser 
    myuser:x:1230:3000:My Test User:/home/myuser:/bin/bash

In the next example, looking up a specific group in the group service,
the group *cumulus* is locally defined in `/etc/groups`, and *netadmin*
is on LDAP.

    cumulus@switch:~$ getent group cumulus
    cumulus:x:1000:
    cumulus@switch:~$ getent group netadmin
    netadmin:*:502:larry,moe,curly,shemp

Running the command `getent passwd` or `getent group` without a specific
request, returns **all** local and LDAP entries for the *passwd* and
*group* maps, respectively.

### <span>Using LDAP search</span>

The `ldapsearch` command performs LDAP operations directly on the LDAP
server. This does not interact with NSS. This command helps display what
the LDAP daemon process is receiving back from the server. The command
has many options. The simplest uses anonymous bind to the host and
specifies the search DN and what attribute to lookup.

    cumulus@switch:~$ ldapsearch -H ldap://ldap.example.com -b dc=example,dc=com -x uid=myuser

<summary>Click to expand the command output ... </summary>

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

### <span>LDAP Browsers</span>

There are some GUI LDAP clients that help to work with LDAP servers.
These are free tools to help graphically show the structure of the LDAP
database.

  - [Apache Directory Studio](http://directory.apache.org/studio/)

  - [LDAPManager](http://ldapmanager.sourceforge.net/)

## <span>Related Information</span>

  - [Debian - configuring LDAP
    authentication](https://wiki.debian.org/LDAP/NSS)

  - [Debian - configuring PAM to use
    LDAP](https://wiki.debian.org/LDAP/PAM)

  - [GitHub - Arthur de Jong nslcd.conf
    file](https://raw.githubusercontent.com/arthurdejong/nss-pam-ldapd/master/nslcd.conf)

  - [Debian backports](http://backports.debian.org/Instructions/)

<article id="html-search-results" class="ht-content" style="display: none;">

</article>

<footer id="ht-footer">

</footer>

</details>
