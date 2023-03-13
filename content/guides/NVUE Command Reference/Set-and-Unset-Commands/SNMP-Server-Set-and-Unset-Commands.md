---
title: SNMP Server Set and Unset Commands
author: Cumulus Networks
weight: 710
product: Cumulus Linux
type: nojsscroll
---
{{%notice note%}}
The `nv unset` commands remove the configuration you set with the equivalent `nv set` commands. This guide only describes an `nv unset` command if it differs from the `nv set` command.
{{%/notice%}}

## nv set service snmp-server

Configures SNMP settings on the switch.

- - -

## nv set service snmp-server listening-address \<listening-address-id\>

Configures the IP address on which the SNMP agent listens. You can set multiple IP addresses.

For security reasons, the listening address is the localhost by default so that the SNMP agent only responds to requests originating on the switch itself.

You can configure an IPv4, IPv6 address, or to configure the `snmpd` daemon to listen on all interfaces for either IPv4 or IPv6 UDP port 161 SNMP requests, you can specify a value of `all`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<listening-address-id>` | The IP address on which the SNMP agent listens.|

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set service snmp-server listening-address all
```

- - -

## nv set service snmp-server listening-address \<listening-address-id\> vrf \<vrf-name\>

Configures the VRF for the SNMP listening address.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<listening-address-id>` | The IP address on which the SNMP agent listens.|
| `<vrf-name>` | The VRF for the specified IP address.|

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set service snmp-server listening-address localhost vrf default
```

- - -

## nv set service snmp-server username \<username-id\>

Configures the SNMPv3 username for authentication.

NVIDIA recommends you use an SNMPv3 username and password instead of the read-only community; SNMPv3 does not expose the password in the `GetRequest` and `GetResponse` packets and can also encrypt packet contents. You can configure multiple usernames for different user roles with different levels of access to various MIBs.

{{%notice note%}}
The default snmpd.conf file contains the default user _snmptrapusernameX. You cannot use this username for authentication. SNMP traps require this username.
{{%/notice%}}

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<username-id>` | The SNMP username for authentication.|

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set service snmp-server username testuser1
```

- - -

## nv set service snmp-server username \<username-id\> auth-none

Configures the SNMP username to not require a password for authentication.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<username-id>` | The SNMP username for authentication.|

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set service snmp-server username testuser1 auth-none
```

- - -

## nv set service snmp-server username \<username-id\> auth-none oid \<oid\>

Configures SNMP to restrict a user with no password authentication to a particular OID tree.
The OID can be either a string of decimal numbers separated by periods or a unique text string that identifies an SNMP MIB object. The MIBs that Cumulus Linux includes are in the `/usr/share/snmp/mibs/` directory. If the MIB you want to use does not install by default, you can install it with the latest Debian `snmp-mibs-downloader` package.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<username-id>` | The SNMP username for authentication.|
| `<oid>` | The OID tree that identifies an SNMP MIB object.|

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set service snmp-server username testuser1 auth-none oid 1.3.6.1.2.1
```

- - -

## nv set service snmp-server username \<username-id\> auth-none view \<view\>

Configures MIB tree exposure restriction. You can define a view for an SNMPv3 username or community password, and a host from a restricted subnet. In doing so, any SNMP request with that username and password must have a source IP address within the configured subnet.

You can define a specific view multiple times and fine tune to provide or restrict access using the included or excluded command to specify branches of certain MIB trees.

By default, the `snmpd.conf` file contains many views within the `systemonly` view.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<username-id>` | The SNMP username for authentication.|
| `<view>` | The SNMP view (subnet).|

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set service snmp-server username testuser1 auth-none auth-none view cumulusOnly
```

- - -

## nv set service snmp-server username \<username-id\> auth-md5 \<auth-id\>

Configures MD5 authentication for the specified SNMP user.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<username-id>` | The SNMP username for authentication.|
| `<auth-id>` | The MD5 authentication password.|

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set service snmp-server username testuser1 auth-md5 myauthmd5password
```

- - -

## nv set service snmp-server username \<username-id\> auth-md5 \<auth-id\> encrypt-des \<encrypt-id\>

Configures the DES encryption password for MD5 authentication for the specified SNMP user to encrypt the contents of the request and response packets.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<username-id>` | The SNMP username for authentication.|
| `<auth-id>` | The MD5 authentication password.|
| `<encrypt-id>` | The DES encryption password.|

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set service snmp-server username testuser1 auth-md5 myauthmd5password encrypt-des myencryptsecret
```

- - -

## nv set service snmp-server username \<username-id\> auth-md5 \<auth-id\> encrypt-des \<encrypt-id\> oid \<oid\>

Configures the setting to restrict a user with a specific DES authentication password and encryption password to a particular OID tree. The OID can be either a string of decimal numbers separated by periods or a unique text string that identifies an SNMP MIB object. The MIBs that Cumulus Linux includes are in the `/usr/share/snmp/mibs/` directory. If the MIB you want to use does not install by default, you can install it with the latest Debian snmp-mibs-downloader package.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<username-id>` | The SNMP username for authentication.|
| `<auth-id>` | The MD5 authentication password.|
| `<encrypt-id>` | The DES encryption password.|
| `<oid>` | The OID tree that identifies an SNMP MIB object.|

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set service snmp-server username testuser1 auth-md5 myauthmd5password encrypt-des myencryptsecret oid 1.3.6.1.2.1.1
```

- - -

## nv set service snmp-server username \<username-id\> auth-md5 \<auth-id\> encrypt-des \<encrypt-id\> view \<view\>

Configures the setting to restrict a user with a specific DES authentication password and encryption password to a defined view. Any SNMP request with that username and password must have a source IP address within the configured subnet.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<username-id>` | The SNMP username for authentication.|
| `<auth-id>` | The MD5 authentication password.|
| `<encrypt-id>` | The DES encryption password.|
| `<view>` | The SNMP view (subnet).|

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set service snmp-server username testuser1 auth-md5 myauthmd5password encrypt-des myencryptsecret view cumulusOnly
```

- - -

## nv set service snmp-server username \<username-id\> auth-md5 \<auth-id\> encrypt-aes \<encrypt-id\>

Configures the AES encryption password for MD5 authentication for the specified SNMP user to encrypt the contents of the request and response packets.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<username-id>` | The SNMP username for authentication.|
| `<auth-id>` | The MD5 authentication password.|
| `<encrypt-id>` | The AES encryption password.|

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set service snmp-server username testuser1 auth-md5 myauthmd5password encrypt-aes myencryptsecret
```

- - -

## nv set service snmp-server username \<username-id\> auth-md5 \<auth-id\> encrypt-aes \<encrypt-id\> oid \<oid\>

Configures the setting to restrict a user with a specific authentication password and AES encryption password to a particular OID tree. The OID can be either a string of decimal numbers separated by periods or a unique text string that identifies an SNMP MIB object. The MIBs that Cumulus Linux includes are in the `/usr/share/snmp/mibs/` directory. If the MIB you want to use does not install by default, you can install it with the latest Debian `snmp-mibs-downloader` package.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<username-id>` | The SNMP username for authentication.|
| `<auth-id>` | The MD5 authentication password.|
| `<encrypt-id>` | The AES encryption password.|
| `<oid>` | The OID tree that identifies an SNMP MIB object.|

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set service snmp-server username testuser1 auth-md5 myauthmd5password encrypt-aes myencryptsecret oid 1.3.6.1.2.1.1
```

- - -

## nv set service snmp-server username \<username-id\> auth-md5 \<auth-id\> encrypt-aes \<encrypt-id\> view \<value\>

Configures the setting to restrict a user with a specific AES authentication password and encryption password to a defined view. Any SNMP request with that username and password must have a source IP address within the configured subnet.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<username-id>` | The SNMP username for authentication.|
| `<auth-id>` | The MD5 authentication password.|
| `<encrypt-id>` | The AES encryption password.|
| `<view>` | The SNMP view (subnet).|

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set service snmp-server username testuser1 auth-md5 myauthmd5password encrypt-aes myencryptsecret view cumulusOnly
```

- - -

## nv set service snmp-server username \<username-id\> auth-md5 \<auth-id\> oid \<oid\>

Configures SNMP to restrict a specific user with the specified password to a particular OID tree.
The OID can be either a string of decimal numbers separated by periods or a unique text string that identifies an SNMP MIB object. The MIBs that Cumulus Linux includes are in the `/usr/share/snmp/mibs/` directory. If the MIB you want to use does not install by default, you can install it with the latest Debian `snmp-mibs-downloader` package.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<username-id>` | The SNMP username for authentication.|
| `<auth-id>` | The SNMP username for authentication.|
| `<oid>` | The OID tree that identifies an SNMP MIB object.|

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set service snmp-server username testuser1 auth-md5 myauthmd5password oid 1.3.6.1.2.1
```

- - -

## nv set service snmp-server username \<username-id\> auth-md5 \<auth-id\> view \<value\>

Configures MIB tree exposure restriction. You can define a view for an SNMPv3 username or community password, and a host from a restricted subnet. In doing so, any SNMP request with that username and password must have a source IP address within the configured subnet.

You can define a specific view multiple times and fine tune to provide or restrict access using the included or excluded command to specify branches of certain MIB trees.

By default, the `snmpd.conf` file contains many views within the `systemonly` view.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<username-id>` | The SNMP username for authentication.|
| `<auth-id>` | The SNMP username for authentication.|
| `<view>` | The SNMP view (subnet).|

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set service snmp-server username testuser1 auth-md5 myauthmd5password view cumulusOnly
```

- - -

## nv set service snmp-server username \<username-id\> auth-sha \<auth-id\>

- - -

## nv set service snmp-server username \<username-id\> auth-sha \<auth-id\> encrypt-des \<encrypt-id\>

- - -

## nv set service snmp-server username \<username-id\> auth-sha \<auth-id\> encrypt-des \<encrypt-id\> oid \<oid\>

- - -

## nv set service snmp-server username \<username-id\> auth-sha \<auth-id\> encrypt-des \<encrypt-id\> view \<value\>

- - -

## nv set service snmp-server username \<username-id\> auth-sha \<auth-id\> encrypt-aes \<encrypt-id\>

- - -

## nv set service snmp-server username \<username-id\> auth-sha \<auth-id\> encrypt-aes \<encrypt-id\> oid \<oid\>

- - -

## nv set service snmp-server username \<username-id\> auth-sha \<auth-id\> encrypt-aes \<encrypt-id\> view \<value\>

- - -

## nv set service snmp-server username \<username-id\> auth-sha \<auth-id\> oid \<oid\>

- - -

## nv set service snmp-server username \<username-id\> auth-sha \<auth-id\> view \<value\>

- - -

## nv set service snmp-server mibs (cumulus-sensor-mib|cumulus-status-mib)

- - -

## nv set service snmp-server viewname \<viewname-id\>

- - -

## nv set service snmp-server viewname \<viewname-id\> excluded \<snmp-branch\>

- - -

## nv set service snmp-server viewname \<viewname-id\> included \<snmp-branch\>

- - -

## nv set service snmp-server readonly-community \<readonly-community-id\>

- - -

## nv set service snmp-server readonly-community \<readonly-community-id\> access \<access-id\>

- - -

## nv set service snmp-server readonly-community \<readonly-community-id\> access \<access-id\> oid \<oid\>

- - -

## nv set service snmp-server readonly-community \<readonly-community-id\> access \<access-id\> view \<value\>

- - -

## nv set service snmp-server readonly-community-v6 \<readonly-community-id\>

- - -

## nv set service snmp-server readonly-community-v6 \<readonly-community-id\> access \<access-id\>

- - -

## nv set service snmp-server readonly-community-v6 \<readonly-community-id\> access \<access-id\> oid \<oid\>

- - -

## nv set service snmp-server readonly-community-v6 \<readonly-community-id\> access \<access-id\> view \<value\>

- - -

## nv set service snmp-server trap-link-down

- - -

## nv set service snmp-server trap-link-down check-frequency 5-300

- - -

## nv set service snmp-server trap-link-up

- - -

## nv set service snmp-server trap-link-up check-frequency 5-300

- - -

## nv set service snmp-server trap-snmp-auth-failures

- - -

## nv set service snmp-server trap-cpu-load-average

- - -

## nv set service snmp-server trap-cpu-load-average one-minute \<one-minute-id\>

- - -

## nv set service snmp-server trap-cpu-load-average one-minute \<one-minute-id\> five-minute \<five-minute-id\>

- - -

## nv set service snmp-server trap-cpu-load-average one-minute \<one-minute-id\> five-minute \<five-minute-id\> fifteen-minute \<fifteen-minute-id\>

- - -

## nv set service snmp-server trap-destination \<trap-destination-id\>

- - -

## nv set service snmp-server trap-destination \<trap-destination-id\> community-password \<community-password-id\>

- - -

## nv set service snmp-server trap-destination \<trap-destination-id\> community-password \<community-password-id\> version (1|2c)

- - -

## nv set service snmp-server trap-destination \<trap-destination-id\> vrf \<vrf-name\>

- - -

## nv set service snmp-server trap-destination \<trap-destination-id\> vrf \<vrf-name\> community-password \<community-password-id\>

- - -

## nv set service snmp-server trap-destination \<trap-destination-id\> vrf \<vrf-name\> community-password \<community-password-id\> version (1|2c)

- - -

## nv set service snmp-server trap-destination \<trap-destination-id\> vrf \<vrf-name\> username \<username-id\>

- - -

## nv set service snmp-server trap-destination \<trap-destination-id\> vrf \<vrf-name\> username \<username-id\> auth-md5 \<auth-id\>

- - -

## nv set service snmp-server trap-destination \<trap-destination-id\> vrf \<vrf-name\> username \<username-id\> auth-md5 \<auth-id\> engine-id \<engine-id\>

- - -

## nv set service snmp-server trap-destination \<trap-destination-id\> vrf \<vrf-name\> username \<username-id\> auth-md5 \<auth-id\> engine-id \<engine-id\> inform (on|off)

- - -

## nv set service snmp-server trap-destination \<trap-destination-id\> vrf \<vrf-name\> username \<username-id\> auth-md5 \<auth-id\> encrypt-des \<encrypt-id\>

- - -

## nv set service snmp-server trap-destination \<trap-destination-id\> vrf \<vrf-name\> username \<username-id\> auth-md5 \<auth-id\> encrypt-des \<encrypt-id\> engine-id \<engine-id\>

- - -

## nv set service snmp-server trap-destination \<trap-destination-id\> vrf \<vrf-name\> username \<username-id\> auth-md5 \<auth-id\> encrypt-des \<encrypt-id\> engine-id \<engine-id\> inform (on|off)

- - -

## nv set service snmp-server trap-destination \<trap-destination-id\> vrf \<vrf-name\> username \<username-id\> auth-md5 \<auth-id\> encrypt-aes \<encrypt-id\>

- - -

## nv set service snmp-server trap-destination \<trap-destination-id\> vrf \<vrf-name\> username \<username-id\> auth-md5 \<auth-id\> encrypt-aes \<encrypt-id\> engine-id \<engine-id\>

- - -

## nv set service snmp-server trap-destination \<trap-destination-id\> vrf \<vrf-name\> username \<username-id\> auth-md5 \<auth-id\> encrypt-aes \<encrypt-id\> engine-id \<engine-id\> inform (on|off)

- - -

## nv set service snmp-server trap-destination \<trap-destination-id\> vrf \<vrf-name\> username \<username-id\> auth-sha \<auth-id\>

- - -

## nv set service snmp-server trap-destination \<trap-destination-id\> vrf \<vrf-name\> username \<username-id\> auth-sha \<auth-id\> engine-id \<engine-id\>

- - -

## nv set service snmp-server trap-destination \<trap-destination-id\> vrf \<vrf-name\> username \<username-id\> auth-sha \<auth-id\> engine-id \<engine-id\> inform (on|off)

- - -

## nv set service snmp-server trap-destination \<trap-destination-id\> vrf \<vrf-name\> username \<username-id\> auth-sha \<auth-id\> encrypt-des \<encrypt-id\>

- - -

## nv set service snmp-server trap-destination \<trap-destination-id\> vrf \<vrf-name\> username \<username-id\> auth-sha \<auth-id\> encrypt-des \<encrypt-id\> engine-id \<engine-id\>

- - -

## nv set service snmp-server trap-destination \<trap-destination-id\> vrf \<vrf-name\> username \<username-id\> auth-sha \<auth-id\> encrypt-des \<encrypt-id\> engine-id \<engine-id\> inform (on|off)

- - -

## nv set service snmp-server trap-destination \<trap-destination-id\> vrf \<vrf-name\> username \<username-id\> auth-sha \<auth-id\> encrypt-aes \<encrypt-id\>

- - -

## nv set service snmp-server trap-destination \<trap-destination-id\> vrf \<vrf-name\> username \<username-id\> auth-sha \<auth-id\> encrypt-aes \<encrypt-id\> engine-id \<engine-id\>

- - -

## nv set service snmp-server trap-destination \<trap-destination-id\> vrf \<vrf-name\> username \<username-id\> auth-sha \<auth-id\> encrypt-aes \<encrypt-id\> engine-id \<engine-id\> inform (on|off)

- - -

## nv set service snmp-server trap-destination \<trap-destination-id\> username \<username-id\>

- - -

## nv set service snmp-server trap-destination \<trap-destination-id\> username \<username-id\> auth-md5 \<auth-id\>

- - -

## nv set service snmp-server trap-destination \<trap-destination-id\> username \<username-id\> auth-md5 \<auth-id\> engine-id \<engine-id\>

- - -

## nv set service snmp-server trap-destination \<trap-destination-id\> username \<username-id\> auth-md5 \<auth-id\> engine-id \<engine-id\> inform (on|off)

- - -

## nv set service snmp-server trap-destination \<trap-destination-id\> username \<username-id\> auth-md5 \<auth-id\> encrypt-des \<encrypt-id\>

- - -

## nv set service snmp-server trap-destination \<trap-destination-id\> username \<username-id\> auth-md5 \<auth-id\> encrypt-des \<encrypt-id\> engine-id \<engine-id\>

- - -

## nv set service snmp-server trap-destination \<trap-destination-id\> username \<username-id\> auth-md5 \<auth-id\> encrypt-des \<encrypt-id\> engine-id \<engine-id\> inform (on|off)

- - -

## nv set service snmp-server trap-destination \<trap-destination-id\> username \<username-id\> auth-md5 \<auth-id\> encrypt-aes \<encrypt-id\>

- - -

## nv set service snmp-server trap-destination \<trap-destination-id\> username \<username-id\> auth-md5 \<auth-id\> encrypt-aes \<encrypt-id\> engine-id \<engine-id\>

- - -

## nv set service snmp-server trap-destination \<trap-destination-id\> username \<username-id\> auth-md5 \<auth-id\> encrypt-aes \<encrypt-id\> engine-id \<engine-id\> inform (on|off)

- - -

## nv set service snmp-server trap-destination \<trap-destination-id\> username \<username-id\> auth-sha \<auth-id\>

- - -

## nv set service snmp-server trap-destination \<trap-destination-id\> username \<username-id\> auth-sha \<auth-id\> engine-id \<engine-id\>

- - -

## nv set service snmp-server trap-destination \<trap-destination-id\> username \<username-id\> auth-sha \<auth-id\> engine-id \<engine-id\> inform (on|off)

- - -

## nv set service snmp-server trap-destination \<trap-destination-id\> username \<username-id\> auth-sha \<auth-id\> encrypt-des \<encrypt-id\>

- - -

## nv set service snmp-server trap-destination \<trap-destination-id\> username \<username-id\> auth-sha \<auth-id\> encrypt-des \<encrypt-id\> engine-id \<engine-id\>

- - -

## nv set service snmp-server trap-destination \<trap-destination-id\> username \<username-id\> auth-sha \<auth-id\> encrypt-des \<encrypt-id\> engine-id \<engine-id\> inform (on|off)

- - -

## nv set service snmp-server trap-destination \<trap-destination-id\> username \<username-id\> auth-sha \<auth-id\> encrypt-aes \<encrypt-id\>

- - -

## nv set service snmp-server trap-destination \<trap-destination-id\> username \<username-id\> auth-sha \<auth-id\> encrypt-aes \<encrypt-id\> engine-id \<engine-id\>

- - -

## nv set service snmp-server trap-destination \<trap-destination-id\> username \<username-id\> auth-sha \<auth-id\> encrypt-aes \<encrypt-id\> engine-id \<engine-id\> inform (on|off)

- - -

## nv set service snmp-server enable (on|off)

- - -

## nv set service snmp-server system-contact \<value\>

- - -

## nv set service snmp-server system-location \<value\>

- - -

## nv set service snmp-server system-name \<value\>

- - -
