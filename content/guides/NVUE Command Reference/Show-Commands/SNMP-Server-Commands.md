---
title: SNMP Server Commands
author: Cumulus Networks
weight: 300
product: Cumulus Linux
type: nojsscroll
---
## nv show service snmp-server

Shows SNMP server configuration on the switch.

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv show service snmp-server
```

- - -

## nv show service snmp-server listening-address

Shows the SNMP server listening address configuration on the switch.

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv show service snmp-server listening-address
```

- - -

## nv show service snmp-server listening-address \<listening-address-id>\

Shows information about the specified SNMP server listening address.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<listening-address-id>` | The SNMP server listening address. By default, this is the localhost so that the SNMP agent only responds to requests originating on the switch itself.|

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv show service snmp-server listening-address 192.168.200.11
```

- - -

## nv show service snmp-server username

Shows the SNMP server username configured on the switch.

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv show service snmp-server username
```

- - -

## nv show service snmp-server username \<username-id>\

Shows information about the specified SNMP server username.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<username-id>` | The username for authentication.|

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv show service snmp-server username testusernoauth
```

- - -

## nv show service snmp-server username \<username-id>\ auth-none

Shows information about the specified SNMP server username with no authentication password.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<username-id>` | The username for authentication.|

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv show service snmp-server username testusernoauth auth-none
```

- - -

## nv show service snmp-server username \<username-id>\ auth-md5

Shows information about the specified SNMP server username with an MD5 password.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<username-id>` | The username for authentication.|

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv show service snmp-server username testuserauth auth-md5
```

- - -

## nv show service snmp-server username \<username-id>\ auth-md5 \<auth-id>\

Shows information about the specified SNMP server username and MD5 password.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<username-id>` | The username for authentication.|
| `<auth-id>` | The MD5 password.|

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv show nv show service snmp-server username testuserauth auth-md5 myauthmd5password
```

- - -

## nv show service snmp-server username \<username-id>\ auth-md5 \<auth-id>\ encrypt-des

Shows information about the specified SNMP server username and MD5 password that also includes an AES or DES encryption password to encrypt the contents of the request and response packets.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<username-id>` | The username for authentication.|
| `<auth-id>` | The MD5 password.|

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv show service snmp-server username testuserauth auth-md5 myauthmd5password encrypt-aes
```

- - -

## nv show service snmp-server username \<username-id>\ auth-md5 \<auth-id>\ encrypt-des \<encrypt-id>\

Shows information about the specified SNMP server username with the specified MD5 password and the specified AES or DES encryption password.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<username-id>` | The username for authentication.|
| `<auth-id>` | The MD5 password.|
| `<encrypt-id>` | The AES or DES encryption password.|

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv show service snmp-server username testuserauth auth-md5 myauthmd5password encrypt-aes myencryptsecret
```

- - -

## nv show service snmp-server username \<username-id>\ auth-sha

Shows information about the specified SNMP server username with an SHA authentication password.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<username-id>` | The username for authentication.|

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv show service snmp-server username limiteduser1 auth-sha
```

- - -

## nv show service snmp-server username \<username-id>\ auth-sha \<auth-id>\

Shows information about the specified SNMP server username with the specified SHA authentication password.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<username-id>` | The username for authentication.|
| `<auth-id>` | The SHA authentication password.|

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv show service snmp-server username limiteduser1 auth-sha SHApassword1
```

- - -

## nv show service snmp-server username \<username-id>\ auth-sha \<auth-id>\ encrypt-des

Shows information about the specified SNMP server username with the specified SHA authentication password that also includes an AES or DES encryption password to encrypt the contents of the request and response packets.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<username-id>` | The username for authentication.|
| `<auth-id>` | The SHA authentication password.|

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv show service snmp-server username limiteduser1 auth-sha SHApassword1 encrypt-des
```

- - -

## nv show service snmp-server username \<username-id>\ auth-sha \<auth-id>\ encrypt-des \<encrypt-id>\

Shows information about the specified SNMP server username with the specified SHA authentication password and specified AES or DES encryption password.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<username-id>` | The username for authentication.|
| `<auth-id>` | The SHA authentication password.|
| `<encrypt-id>` | The AES or DES encryption password.|

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv show service snmp-server username limiteduser1 auth-sha SHApassword1 encrypt-des myencryptsecret
```

- - -

## nv show service snmp-server mibs

Shows the SNMP MIBS.

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv show service snmp-server mibs
```

- - -

## nv show service snmp-server viewname

Shows the configured SNMP server view names.

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv show service snmp-server viewname
```

- - -

## nv show service snmp-server viewname \<viewname-id>\

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
|`<viewname-id` | The SNMP server view name. |
### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv show service snmp-server viewname ??
```

- - -

## nv show service snmp-server readonly-community

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv show service snmp-server readonly-community
```

- - -

## nv show service snmp-server readonly-community \<readonly-community-id>\

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv show service snmp-server readonly-community ??
```

- - -

## nv show service snmp-server readonly-community \<readonly-community-id>\ access

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv show service snmp-server readonly-community ?? access
```

- - -

## nv show service snmp-server readonly-community \<readonly-community-id>\ access \<access-id>\


### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv show service snmp-server readonly-community ?? access ??
```

- - -

## nv show service snmp-server readonly-community-v6


### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv show service snmp-server readonly-community-v6
```

- - -

## nv show service snmp-server readonly-community-v6 \<readonly-community-id>\

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv show service snmp-server readonly-community-v6 ????
```

- - -

## nv show service snmp-server readonly-community-v6 \<readonly-community-id>\ access

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv show service snmp-server readonly-community-v6 ???? access
```

- - -

## nv show service snmp-server readonly-community-v6 \<readonly-community-id>\ access \<access-id>\

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv show service snmp-server readonly-community-v6 ???? access ??
```

- - -

## nv show service snmp-server trap-link-down

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv show service snmp-server trap-link-down
```

- - -

## nv show service snmp-server trap-link-up

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv show service snmp-server trap-link-up
```

- - -

## nv show service snmp-server trap-snmp-auth-failures

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv show service snmp-server trap-snmp-auth-failures
```

- - -

## nv show service snmp-server trap-cpu-load-average

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv show
```

- - -

## nv show service snmp-server trap-cpu-load-average one-minute

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv show
```

- - -

## nv show service snmp-server trap-cpu-load-average one-minute \<one-minute-id>\

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv show
```

- - -

## nv show service snmp-server trap-cpu-load-average one-minute \<one-minute-id>\ five-minute

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv show
```

- - -

## nv show service snmp-server trap-cpu-load-average one-minute \<one-minute-id>\ five-minute \<five-minute-id>\

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv show
```

- - -

## nv show service snmp-server trap-cpu-load-average one-minute \<one-minute-id>\ five-minute \<five-minute-id>\ fifteen-minute

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv show
```

- - -

## nv show service snmp-server trap-cpu-load-average one-minute \<one-minute-id>\ five-minute \<five-minute-id>\ fifteen-minute \<fifteen-minute-id>\

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv show
```

- - -

## nv show service snmp-server trap-destination

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv show
```

- - -

## nv show service snmp-server trap-destination \<trap-destination-id>\

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv show
```

- - -

## nv show service snmp-server trap-destination \<trap-destination-id>\ community-password

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv show
```

- - -

## nv show service snmp-server trap-destination \<trap-destination-id>\ community-password \<community-password-id>\

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv show
```

- - -

## nv show service snmp-server trap-destination \<trap-destination-id>\ vrf

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv show
```

- - -

## nv show service snmp-server trap-destination \<trap-destination-id>\ vrf \<vrf-name>\

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv show
```

- - -

## nv show service snmp-server trap-destination \<trap-destination-id>\ vrf \<vrf-name>\ community-password

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv show
```

- - -

## nv show service snmp-server trap-destination \<trap-destination-id>\ vrf \<vrf-name>\ community-password \<community-password-id>\

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv show
```

- - -

## nv show service snmp-server trap-destination \<trap-destination-id>\ vrf \<vrf-name>\ username

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv show
```

- - -

## nv show service snmp-server trap-destination \<trap-destination-id>\ vrf \<vrf-name>\ username \<username-id>\

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv show
```

- - -

## nv show service snmp-server trap-destination \<trap-destination-id>\ vrf \<vrf-name>\ username \<username-id>\ auth-md5

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv show
```

- - -

## nv show service snmp-server trap-destination \<trap-destination-id>\ vrf \<vrf-name>\ username \<username-id>\ auth-md5 \<auth-id>\

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv show
```

- - -

## nv show service snmp-server trap-destination \<trap-destination-id>\ vrf \<vrf-name>\ username \<username-id>\ auth-md5 \<auth-id>\ engine-id

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv show
```

- - -

## nv show service snmp-server trap-destination \<trap-destination-id>\ vrf \<vrf-name>\ username \<username-id>\ auth-md5 \<auth-id>\ engine-id \<engine-id>\

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv show
```

- - -

## nv show service snmp-server trap-destination \<trap-destination-id>\ vrf \<vrf-name>\ username \<username-id>\ auth-md5 \<auth-id>\ encrypt-des

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv show
```

- - -

## nv show service snmp-server trap-destination \<trap-destination-id>\ vrf \<vrf-name>\ username \<username-id>\ auth-md5 \<auth-id>\ encrypt-des \<encrypt-id>\

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv show
```

- - -

## nv show service snmp-server trap-destination \<trap-destination-id>\ vrf \<vrf-name>\ username \<username-id>\ auth-md5 \<auth-id>\ encrypt-des \<encrypt-id>\ engine-id

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv show
```

- - -

## nv show service snmp-server trap-destination \<trap-destination-id>\ vrf \<vrf-name>\ username \<username-id>\ auth-md5 \<auth-id>\ encrypt-des \<encrypt-id>\ engine-id \<engine-id>\

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv show
```

- - -

## nv show service snmp-server trap-destination \<trap-destination-id>\ vrf \<vrf-name>\ username \<username-id>\ auth-md5 \<auth-id>\ encrypt-aes

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv show
```

- - -

## nv show service snmp-server trap-destination \<trap-destination-id>\ vrf \<vrf-name>\ username \<username-id>\ auth-md5 \<auth-id>\ encrypt-aes \<encrypt-id>\

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv show
```

- - -

## nv show service snmp-server trap-destination \<trap-destination-id>\ vrf \<vrf-name>\ username \<username-id>\ auth-md5 \<auth-id>\ encrypt-aes \<encrypt-id>\ engine-id

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv show
```

- - -

## nv show service snmp-server trap-destination \<trap-destination-id>\ vrf \<vrf-name>\ username \<username-id>\ auth-md5 \<auth-id>\ encrypt-aes \<encrypt-id>\ engine-id \<engine-id>\

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv show
```

- - -

## nv show service snmp-server trap-destination \<trap-destination-id>\ vrf \<vrf-name>\ username \<username-id>\ auth-sha

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv show
```

- - -

## nv show service snmp-server trap-destination \<trap-destination-id>\ vrf \<vrf-name>\ username \<username-id>\ auth-sha \<auth-id>\

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv show
```

- - -

## nv show service snmp-server trap-destination \<trap-destination-id>\ vrf \<vrf-name>\ username \<username-id>\ auth-sha \<auth-id>\ engine-id

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv show
```

- - -

## nv show service snmp-server trap-destination \<trap-destination-id>\ vrf \<vrf-name>\ username \<username-id>\ auth-sha \<auth-id>\ engine-id \<engine-id>\

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv show
```

- - -

## nv show service snmp-server trap-destination \<trap-destination-id>\ vrf \<vrf-name>\ username \<username-id>\ auth-sha \<auth-id>\ encrypt-des

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv show
```

- - -

## nv show service snmp-server trap-destination \<trap-destination-id>\ vrf \<vrf-name>\ username \<username-id>\ auth-sha \<auth-id>\ encrypt-des \<encrypt-id>\

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv show
```

- - -

## nv show service snmp-server trap-destination \<trap-destination-id>\ vrf \<vrf-name>\ username \<username-id>\ auth-sha \<auth-id>\ encrypt-des \<encrypt-id>\ engine-id

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv show
```

- - -

## nv show service snmp-server trap-destination \<trap-destination-id>\ vrf \<vrf-name>\ username \<username-id>\ auth-sha \<auth-id>\ encrypt-des \<encrypt-id>\ engine-id \<engine-id>\

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv show
```

- - -

## nv show service snmp-server trap-destination \<trap-destination-id>\ vrf \<vrf-name>\ username \<username-id>\ auth-sha \<auth-id>\ encrypt-aes

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv show
```

- - -

## nv show service snmp-server trap-destination \<trap-destination-id>\ vrf \<vrf-name>\ username \<username-id>\ auth-sha \<auth-id>\ encrypt-aes \<encrypt-id>\

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv show
```

- - -

## nv show service snmp-server trap-destination \<trap-destination-id>\ vrf \<vrf-name>\ username \<username-id>\ auth-sha \<auth-id>\ encrypt-aes \<encrypt-id>\ engine-id

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv show
```

- - -

## nv show service snmp-server trap-destination \<trap-destination-id>\ vrf \<vrf-name>\ username \<username-id>\ auth-sha \<auth-id>\ encrypt-aes \<encrypt-id>\ engine-id \<engine-id>\

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv show
```

- - -

## nv show service snmp-server trap-destination \<trap-destination-id>\ username

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv show
```

- - -

## nv show service snmp-server trap-destination \<trap-destination-id>\ username \<username-id>\

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv show
```

- - -

## nv show service snmp-server trap-destination \<trap-destination-id>\ username \<username-id>\ auth-md5

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv show
```

- - -

## nv show service snmp-server trap-destination \<trap-destination-id>\ username \<username-id>\ auth-md5 \<auth-id>\

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv show
```

- - -

## nv show service snmp-server trap-destination \<trap-destination-id>\ username \<username-id>\ auth-md5 \<auth-id>\ engine-id

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv show
```

- - -

## nv show service snmp-server trap-destination \<trap-destination-id>\ username \<username-id>\ auth-md5 \<auth-id>\ engine-id \<engine-id>\

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv show
```

- - -

## nv show service snmp-server trap-destination \<trap-destination-id>\ username \<username-id>\ auth-md5 \<auth-id>\ encrypt-des

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv show
```

- - -

## nv show service snmp-server trap-destination \<trap-destination-id>\ username \<username-id>\ auth-md5 \<auth-id>\ encrypt-des \<encrypt-id>\

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv show
```

- - -
## nv show service snmp-server trap-destination \<trap-destination-id>\ username \<username-id>\ auth-md5 \<auth-id>\ encrypt-des \<encrypt-id>\ engine-id

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv show
```

- - -

## nv show service snmp-server trap-destination \<trap-destination-id>\ username \<username-id>\ auth-md5 \<auth-id>\ encrypt-des \<encrypt-id>\ engine-id \<engine-id>\

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv show
```

- - -

## nv show service snmp-server trap-destination \<trap-destination-id>\ username \<username-id>\ auth-md5 \<auth-id>\ encrypt-aes

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv show
```

- - -

## nv show service snmp-server trap-destination \<trap-destination-id>\ username \<username-id>\ auth-md5 \<auth-id>\ encrypt-aes \<encrypt-id>\

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv show
```

- - -

## nv show service snmp-server trap-destination \<trap-destination-id>\ username \<username-id>\ auth-md5 \<auth-id>\ encrypt-aes \<encrypt-id>\ engine-id

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv show
```

- - -

## nv show service snmp-server trap-destination \<trap-destination-id>\ username \<username-id>\ auth-md5 \<auth-id>\ encrypt-aes \<encrypt-id>\ engine-id \<engine-id>\

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv show
```

- - -

## nv show service snmp-server trap-destination \<trap-destination-id>\ username \<username-id>\ auth-sha

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv show
```

- - -

## nv show service snmp-server trap-destination \<trap-destination-id>\ username \<username-id>\ auth-sha \<auth-id>\

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv show
```

- - -

## nv show service snmp-server trap-destination \<trap-destination-id>\ username \<username-id>\ auth-sha \<auth-id>\ engine-id

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv show
```

- - -

## nv show service snmp-server trap-destination \<trap-destination-id>\ username \<username-id>\ auth-sha \<auth-id>\ engine-id \<engine-id>\

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv show
```

- - -

## nv show service snmp-server trap-destination \<trap-destination-id>\ username \<username-id>\ auth-sha \<auth-id>\ encrypt-des

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv show
```

- - -

## nv show service snmp-server trap-destination \<trap-destination-id>\ username \<username-id>\ auth-sha \<auth-id>\ encrypt-des \<encrypt-id>\

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv show
```

- - -

## nv show service snmp-server trap-destination \<trap-destination-id>\ username \<username-id>\ auth-sha \<auth-id>\ encrypt-des \<encrypt-id>\ engine-id

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv show
```

- - -

## nv show service snmp-server trap-destination \<trap-destination-id>\ username \<username-id>\ auth-sha \<auth-id>\ encrypt-des \<encrypt-id>\ engine-id \<engine-id>\

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv show
```

- - -

## nv show service snmp-server trap-destination \<trap-destination-id>\ username \<username-id>\ auth-sha \<auth-id>\ encrypt-aes

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv show
```

- - -

## nv show service snmp-server trap-destination \<trap-destination-id>\ username \<username-id>\ auth-sha \<auth-id>\ encrypt-aes \<encrypt-id>\

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv show
```

- - -

## nv show service snmp-server trap-destination \<trap-destination-id>\ username \<username-id>\ auth-sha \<auth-id>\ encrypt-aes \<encrypt-id>\ engine-id

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv show
```

- - -

## nv show service snmp-server trap-destination \<trap-destination-id>\ username \<username-id>\ auth-sha \<auth-id>\ encrypt-aes \<encrypt-id>\ engine-id \<engine-id>\
