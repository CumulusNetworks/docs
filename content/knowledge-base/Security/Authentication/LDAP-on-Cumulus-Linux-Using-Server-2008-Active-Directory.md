---
title: LDAP on Cumulus Linux Using Server 2008 Active Directory
author: NVIDIA
weight: 411
toc: 3
---

This article provides an example of how to set up LDAP authentication and authorization on Cumulus Linux using Active Directory. It applies to any Debian Wheezy-based server or switch.

The method described in the article applies ONLY to Windows Server 2008. This method does not work as well with Windows Server 2012.

## Prerequisites

- Windows 2008 Active Directory
- Cumulus Linux 2.x

## Active Directory Setup

- **Base DN:** CN=Cumulus Admin, DC=RTP, DC=Example, DC=test
- **Base OU:** OU=Support, DC=RTP, DC=Example, DC=Test
- **Users and Groups:** This example has three users that can access a Cumulus Linux switch. Two are in the senior network engineer group, one in the junior engineering group. The last user, *Mark Smith*, does not have access to the switches because he is not a member of the *cumuluslnxadm* group.

{{<img src="/images/knowledge-base/LDAP-Server-2008-layout_of_users_on_ad.png" width="600" alt="group layout of users">}}

*AD group layout of users*

{{<img src="/images/knowledge-base/LDAP-Server-2008-adsi_edit_landscape.jpg" width="600" alt="layout of users and groups in AD schema">}}

*Layout of users and groups in AD schema*

## Goals

- Configure LDAP authentication without changing the default AD schema.
- Support nested groups. The following should work:  
  {{<img src="/images/knowledge-base/LDAP-Server-2008-nested_group_diagram.png" width="500" alt="nested group diagram">}}
- User directories are automatically created the first time an authorized user logs into the switch.
- Senior network admins via `sudo` can run any command on the switch.
- Junior network admins can:  
  - Log in and access any non-privileged command.
  - Run `sudo lldpctl` without prompting for a password. `lldpctl` is an important network troubleshooting tool, but requires root access.
  - Use all `ip` commands (*iproute2 commands*).
  - Not access *FRR* via `vtysh` or non-modal CLI like `cl-ospf`.

## Configure Cumulus Linux

1. Update PAM to support automatic creation of directories (optional).

   This information is from {{<exlink url="https://wiki.debian.org/LDAP/PAM" text="the Debian wiki">}}. The alternative is to set the `homeDirectory` attribute for users in AD to */home/cumulus*, and all users map to the predefined user account.

   Create the following file `/usr/share/pam-configs/mkhomedir`:

       Name: Create home directory during login
       Default: yes
       Priority: 900
       Session-Type: Additional
       Session:
               required        pam_mkhomedir.so umask=0022 skel=/etc/skel

2. Add Debian backports to apt sources list (optional).

   You need `libnss-ldapd` version 0.9 and higher for nested group support. For Wheezy, *and thus Cumulus Linux 2.x*, include {{<exlink url="http://backports.debian.org/Instructions/" text="Debian Wheezy backports to the apt sources list">}}.

3. Seed `debconf` with appropriate values (*recommended*).

   Seeding `debconf` is helpful because it adds most of the important configuration values in the various applications and prevents the apps from asking questions during the installation.

   While it is possible to execute `apt-get` in non-interactive mode, you need to change most of the necessary configuration later.

   {{%notice note%}}

For `libnss-ldapd`, there are CPU architecture-specific questions to answer.

{{%/notice%}}

       root# apt-get install debconf-utils

       root# debconf-set-selections <<'zzzEndOfFilezzz'

       # LDAP database user. Leave blank will be populated later!
       # This way of setting binddn and bindpw doesn't seem to work.
       # So have to manually do it. But interactive apt-get mode works.
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

       # Choices: Ccreds credential caching - password saving, Unix authentication, LDAP Authentication , Create  home directory on first time login, Ccreds credential caching - password checking
       # This is where "mkhomedir" pam config is activated that allows automatic creation of home directory
       libpam-runtime        libpam-runtime/profiles multiselect     ccreds-save, unix, ldap, mkhomedir , ccreds-check
    
       # for internal use; can be preseeded
       man-db        man-db/auto-update      boolean true
    
       # Name services to configure:
       # Choices: aliases, ethers, group, hosts, netgroup, networks, passwd, protocols, rpc, services,  shadow
       libnss-ldapd  libnss-ldapd/nsswitch   multiselect     group, passwd, shadow
       libnss-ldapd  libnss-ldapd/clean_nsswitch     boolean false
    
    
       zzzEndOfFilezzz

   Verify the `debconf` configuration:

       root# debconf-show nslcd
       * nslcd/ldap-bindpw: (password omitted)
         nslcd/restart-failed:
         nslcd/ldap-sasl-authcid:
         nslcd/restart-services:
         nslcd/ldap-sasl-realm:
       * nslcd/ldap-sasl-mech:
       * nslcd/ldap-starttls: false
       * nslcd/ldap-base:  ou=support,dc=rtp,dc=example,dc=test
         nslcd/ldap-sasl-krb5-ccname: /var/run/nslcd/nslcd.tkt
       * nslcd/ldap-auth-type: none
         nslcd/disable-screensaver:
       * libraries/restart-without-asking: true
       * nslcd/ldap-reqcert: never
         nslcd/ldap-cacertfile: /etc/ssl/certs/ca-certificates.crt
         nslcd/ldap-sasl-authzid:
       * nslcd/ldap-uris:  ldaps://myadserver.rtp.example.test
       * libraries/restart-without-asking:: true
         nslcd/ldap-sasl-secprops:
         nslcd/xdm-needs-restart:
       * nslcd/ldap-binddn:
    
       root# debconf-show libpam-runtime
         libpam-runtime/override: false
         libpam-runtime/profiles: mkhomedir, unix, ldap, capability, auditd
         libpam-runtime/title:
         libpam-runtime/conflicts:
         libpam-runtime/no_profiles_chosen:
    
       root# debconf-show man-db
       * man-db/auto-update: true
         man-db/install-setuid: false
    
       root# debconf-show libnss-ldapd
       * libnss-ldapd/nsswitch:     group, passwd, shadow
       * libnss-ldapd/clean_nsswitch: false

4. Install LDAP apps.

   `libnss-ldapd` from the Wheezy main repo does not support nested groups. Load the `libnss-ldapd` app from backports to get the latest available version.

   {{%notice note%}}

Do not install `libnss-ldap`. This is the **wrong** app, {{<exlink url="http://bugs.debian.org/cgi-bin/bugreport.cgi?bug=579647" text="and this explains why">}}.

{{%/notice%}}

       root# apt-get -t wheezy-backports install libnss-ldapd ldap-utils

5. Get the Active Directory Domain SID.

   Use the `dsquery` command on the Windows server to get the domain SID. For more information, read {{<exlink url="http://portal.sivarajan.com/2011/09/objectsid-and-active-directory.html" text="this good reference on Object SIDs">}}.

   {{<img src="/images/knowledge-base/LDAP-Server-2008-dsquery.png" alt="dsquery output">}}

6. Configure `nslcd.conf`.

   Update `/etc/nslcd.conf` with the following:

   - Specify the Bind DN path.
   - Specify the Bind DN password.
   - Configure LDAP search filter. The filter states that only users in the *cumuluslnxadm* group can log in. The search filter performs the nested group lookup.
   - Configure Unix to AD mappings.
   - Configure nested group support.

   Here is the `/etc/nslcd.conf` config with comments:

       # /etc/nslcd.conf
       # nslcd configuration file. See nslcd.conf(5)
       # for details.

       # The user and group nslcd should run as.
       uid nslcd
       gid nslcd

       # The location at which the LDAP server(s) should be reachable.
       # If planning to use secure LDAP, use fqdn that matches name 
       # in the server SSL cert sent during negotiation. Debugging 
       # nslcd will show this error if found
       uri ldap://myadserver.rtp.example.test

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
       # default tls setting of 'demand' requires CA public cert
       #  for AD server be defined in "tls_cacertfile"
       # use PEM format for CA cert, not DER format.
       tls_reqcert never
       #tls_cacertfile /etc/ssl/certs/ca-certificates.crt

       # The search scope.
       #scope sub

       # Add nested group support
       # Supported in nslcd 0.9 and higher.
       # default wheezy install of nslcd supports on 0.8. wheezy-backports has 0.9
       nss_nested_groups yes

       # Mappings for Active Directory
       # (replace the SIDs in the objectSid mappings with the value for your domain)
       # "dsquery * -filter (samaccountname=testuser1) -attr ObjectSID" 
       pagesize 1000
       referrals off
       idle_timelimit 1000

       # Do not allow uids lower than 100 to login (aka Administrator)
       # not needed as pam already has this support
       #  nss_min_uid 1000

       # This filter says to get all users who are part of the cumuluslnxadm group. Supports nested groups search filter.
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

7. Enable Secure LDAP (optional).

   - Copy the LDAP CA certificate (in PEM format) to the directory, specified in the nslcd.conf `tls_cacertfile` option, on the client device. Ensure the file specified matches the filename copied.
   - Set the `tls_reqcert` option to `demand`.
   - Change the URI to use `ldaps://`.

8. Confirm that LDAP authentication works.

   - Restart the `nscd` service using `service nscd restart` to clear the cache. This can cache a mistake and then you can spend hours troubleshooting a problem that does not exist. Or, clear the `nscd` cache for `passwd` and `group` using the commands:

         root# nscd --invalidate=group
         root# nscd --invalidate=passwd

   - Run `nslcd` in debug mode.

         root# service nslcd stop
         root# nslcd -d

   - When it works, it should output as follows: *user list*: The UID and GIDs are the last 4 digits of the user's AD object SID. Notice that "Mark Smith" the support manager is not there. This is because the user is not part of the `cumuluslnxadm` group.

          root# getent passwd
          root:x:0:0:root:/root:/bin/bash
          daemon:x:1:1:daemon:/usr/sbin:/bin/sh
          ...
          ..........
          _lldpd:x:105:107::/var/run/lldpd:/bin/false
          joechen:*:1121:1121:Joe Chen:/home/joechen:/bin/bash
          marydiho:*:1124:1124:Mary Diho:/home/marydiho:/bin/bash
          obidia:*:1128:1128:Obi Dia:/home/obidia:/bin/bash

      *group list*: GIDs of each user should be present. Because you enabled nested group support, all nested groups get mapped to the right users.

          root# getent group
          ..
          .....
          ssh:x:105:
          nslcd:x:106
          _lldpd:x:107:
          joechen:*:1121:
          marydiho:*:1124:
          marksmith:*:1125:
          obidia:*:1128:
          jnrnetworkadm:*:1118:obidia
          cumuluslnxadm:*:1120:obidia,marydiho,joechen
          snrnetworkadm:*:1126:marydiho,joechen

9. Set up command authorization (*optional*).

   To do authorization with `nslcd`, creating entries on the client device matches against the LDAP information cached. To accomplish this, you must install the `sudo-ldap` package from the Wheezy repo.

   In this example, you create the following authorizations:

   - Senior engineers can run any privileged and non-privileged command.
   - Junior engineers can run `lldpctl` without a password. By default, `lldpctl` requires root access.

   Add two files to the `/etc/sudoers.d` directory, one for senior engineers and the other for junior engineers. You can configure this in the `/etc/sudoers` file, but this keeps things modular.

   `/etc/sudoers.d/snrnetworkadm`:

       # allow any senior engineer root privilege after they type their password
       %snrnetworkadm ALL=(ALL) ALL

   `/etc/sudoers.d/jnrnetworkadm`:

       Cmnd_Alias LLDP_CMDS = /usr/sbin/lldpctl

       # allow any junior network engineer to run lldpctl without root permission
       %jnrnetworkadm ALL=(ALL) NOPASSWD: LLDP_CMDS

## Automate It with Ansible

An Ansible Playbook is available on {{<exlink url="https://github.com/CumulusNetworks/ansible-role-activedirectory-auth-client" text="GitHub">}} that automates the configuration shown in this article.
