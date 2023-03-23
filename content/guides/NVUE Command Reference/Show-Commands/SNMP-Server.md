---
title: SNMP Server
author: Cumulus Networks
weight: 360
product: Cumulus Linux
type: nojsscroll
---
## nv show service snmp-server

Shows global SNMP server configuration on the switch, such as the listening addresses, trap link down and up check frequency, and the list of users.

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv show service snmp-server
```

- - -

## nv show service snmp-server listening-address

Shows the SNMP server listening address configured on the switch.

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
cumulus@switch:~$ nv show service snmp-server listening-address localhost
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
cumulus@switch:~$ nv show service snmp-server username testuserauth auth-md5 myauthmd5password encrypt-des
```

- - -

## nv show service snmp-server username \<username-id>\ auth-md5 \<auth-id>\ encrypt-des \<encrypt-id>\

Shows information about the specified SNMP server username and MD5 password and the AES or DES encryption password.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<username-id>` | The username for authentication.|
| `<auth-id>` | The MD5 password.|
| `<encrypt-id>` | The DES encryption password.|

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv show service snmp-server username testuserauth auth-md5 myauthmd5password encrypt-des myencryptsecret
```

- - -

## nv show service snmp-server username \<username-id>\ auth-md5 \<auth-id>\ encrypt-aes

Shows information about the specified SNMP server username and MD5 password that also includes an AES encryption password to encrypt the contents of the request and response packets.

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

## nv show service snmp-server username \<username-id>\ auth-md5 \<auth-id>\ encrypt-aes \<encrypt-id>\

Shows information about the specified SNMP server username and MD5 password and the AES encryption password.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<username-id>` | The username for authentication.|
| `<auth-id>` | The MD5 password.|
| `<encrypt-id>` | The AES encryption password.|

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

Shows information about the specified SNMP server username and SHA authentication password.

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

Shows information about the specified SNMP server username and SHA authentication password that also includes an AES or DES encryption password to encrypt the contents of the request and response packets.

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

Shows information about the SNMP server username with the SHA authentication password and AES or DES encryption password.

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

## nv show service snmp-server username \<username-id>\ auth-sha \<auth-id>\ encrypt-aes

Shows information about the specified SNMP server username and SHA authentication password that also includes an AES encryption password to encrypt the contents of the request and response packets.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<username-id>` | The username for authentication.|
| `<auth-id>` | The SHA authentication password.|

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv show service snmp-server username limiteduser1 auth-sha SHApassword1 encrypt-aes
```

- - -

## nv show service snmp-server username \<username-id>\ auth-sha \<auth-id>\ encrypt-aes \<encrypt-id>\

Shows information about the SNMP server username with the SHA authentication password and AES encryption password.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<username-id>` | The username for authentication.|
| `<auth-id>` | The SHA authentication password.|
| `<encrypt-id>` | The AES encryption password.|

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv show service snmp-server username limiteduser1 auth-sha SHApassword1 encrypt-aes myencryptsecret
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

Shows the configured SNMP server view names. SNMP views are named groups of MIB objects that you can associate with user accounts to allow limited access to view and modify SNMP statistics and system configuration.

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv show service snmp-server viewname
```

- - -

## nv show service snmp-server viewname \<viewname-id>\

Shows information about the specified SNMP server view name.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
|`<viewname-id` | The SNMP server view name. |

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv show service snmp-server viewname cumulusOnly
```

- - -

## nv show service snmp-server readonly-community

Shows the SNMP server readonly community strings.

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv show service snmp-server readonly-community 
```

- - -

## nv show service snmp-server readonly-community \<readonly-community-id>\

Shows information about the specified SNMP server readonly community string.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
|`<readonly-community-id>` | The readonly community string. |

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv show service snmp-server readonly-community simplepassword
```

- - -

## nv show service snmp-server readonly-community \<readonly-community-id>\ access

Shows the SNMP server readonly community string access settings.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
|`<readonly-community-id>` | The readonly community string. |

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv show service snmp-server readonly-community simplepassword access
```

- - -

## nv show service snmp-server readonly-community \<readonly-community-id>\ access \<access-id>\

Shows the SNMP server readonly community string access settings for the specified subnet.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
|`<readonly-community-id>` | The readonly community string. |
|`<access-id>` | The subnet. |

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv show service snmp-server readonly-community simplepassword access 192.168.200.10/24
```

- - -

## nv show service snmp-server readonly-community-v6

Shows the IPv6 SNMP server readonly community strings.

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv show service snmp-server readonly-community-v6
```

- - -

## nv show service snmp-server readonly-community-v6 \<readonly-community-id>\

Shows information about the specified IPv6 SNMP server readonly community string.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
|`<readonly-community-id>` | The IPv6 readonly community string. |

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv show service snmp-server readonly-community-v6 showitall
```

- - -

## nv show service snmp-server readonly-community-v6 \<readonly-community-id>\ access

Shows the IPv6 SNMP server readonly community string access settings.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
|`<readonly-community-id>` | The IPv6 readonly community string. |

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv show service snmp-server readonly-community-v6 showitall access
```

- - -

## nv show service snmp-server readonly-community-v6 \<readonly-community-id>\ access \<access-id>\

Shows the IPv6 SNMP server readonly community string access settings for the specified subnet.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
|`<readonly-community-id>` | The readonly community string. |
|`<access-id>` | The IPv6 subnet. |

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv show service snmp-server readonly-community-v6 showitall access 2001:db8::1/128
```

- - -

## nv show service snmp-server trap-link-down

Shows the SNMP traps for the interface link down status.

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv show service snmp-server trap-link-down
```

- - -

## nv show service snmp-server trap-link-up

Shows SNMP traps for the interface link up status.

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv show service snmp-server trap-link-up
```

- - -

## nv show service snmp-server trap-snmp-auth-failures

Shows SNMP traps for SNMP authentication failures.

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv show service snmp-server trap-snmp-auth-failures
```

- - -

## nv show service snmp-server trap-cpu-load-average

Shows the SNMP traps generated when the CPU load average exceeds a certain threshold.

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv show service snmp-server trap-cpu-load-average
```

- - -

## nv show service snmp-server trap-cpu-load-average one-minute

Shows the SNMP traps generated when the CPU load average the one-minute threshold.

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv show service snmp-server trap-cpu-load-average one-minute
```

- - -

## nv show service snmp-server trap-cpu-load-average one-minute \<one-minute-id>\

Shows the SNMP traps generated when the CPU load average the one-minute interval exceeds a certain percentage.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<one-minute-id>` | The one minute load average threshold ID.|

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv show service snmp-server trap-cpu-load-average one-minute 12
```

- - -

## nv show service snmp-server trap-cpu-load-average one-minute \<one-minute-id>\ five-minute

Shows the SNMP traps generated when the CPU load average for the one minute interval exceeds a certain percentage and reaches the five-minute interval.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<one-minute-id>` | The one minute load average threshold ID.|

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv show service snmp-server trap-cpu-load-average one-minute 102 five-minute
```

- - -

## nv show service snmp-server trap-cpu-load-average one-minute \<one-minute-id>\ five-minute \<five-minute-id>\

Shows the SNMP traps generated when the CPU load average for the one minute interval and the five minute interval exceed a certain percentage.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<one-minute-id>` | The one-minute load average threshold.|
| `<five-minute-id>` | The five-minute load average threshold.|

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv show service snmp-server trap-cpu-load-average one-minute 12 five-minute 10
```

- - -

## nv show service snmp-server trap-cpu-load-average one-minute \<one-minute-id>\ five-minute \<five-minute-id>\ fifteen-minute

Shows the SNMP traps generated when the CPU load average for the one minute interval and the five minute interval exceed a certain percentage and reaches the fifteen-minute interval.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<one-minute-id>` | The one-minute load average threshold.|
| `<five-minute-id>` | The five-minute load average threshold.|

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv show service snmp-server trap-cpu-load-average one-minute 102 five-minute 501 fifteen-minute
```

- - -

## nv show service snmp-server trap-cpu-load-average one-minute \<one-minute-id>\ five-minute \<five-minute-id>\ fifteen-minute \<fifteen-minute-id>\

Shows the SNMP traps generated when the CPU load average for the one-minute interval, the five-minute interval, and the fifteen-minute interval exceed a certain percentage.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<one-minute-id>` | The one-minute load average threshold.|
| `<five-minute-id>` | The five-minute load average threshold.|
| `<fifteen-minute-id>` | The fifteen-minute load average threshold.|

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv show service snmp-server trap-cpu-load-average one-minute 102 five-minute 501 fifteen-minute 1501
```

- - -

## nv show service snmp-server trap-destination

Shows the SNMP trap destinations.

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv show service snmp-server trap-destination
```

- - -

## nv show service snmp-server trap-destination \<trap-destination-id>\

Shows information about the specified SNMP trap destination.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
|`<trap-destination-id>` | The SNMP trap destination IP address or hostname. |

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv show service snmp-server trap-destination localhost
```

- - -

## nv show service snmp-server trap-destination \<trap-destination-id>\ community-password

Shows the community password for the SNMP trap destination.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
|`<trap-destination-id>` | The SNMP trap destination IP address or hostname. |

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv show service snmp-server trap-destination localhost community-password
```

- - -

## nv show service snmp-server trap-destination \<trap-destination-id>\ community-password \<community-password-id>\

Shows information about the specified community password for the SNMP trap destination.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
|`<trap-destination-id>` | The SNMP trap destination IP address or hostname. |
|`<community-password-id>` | The community password. |

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv show service snmp-server trap-destination localhost community-password mymanagementvrfpassword
```

- - -

## nv show service snmp-server trap-destination \<trap-destination-id>\ vrf

Shows the SNMP server trap destinations configured for all VRFs.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
|`<trap-destination-id>` | The SNMP trap destination IP address or hostname. |

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv show service snmp-server trap-destination localhost vrf
```

- - -

## nv show service snmp-server trap-destination \<trap-destination-id>\ vrf \<vrf-name>\

Shows the SNMP server trap destinations configured for the specified VRF.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
|`<trap-destination-id>` | The SNMP trap destination IP address or hostname. |
|`<vrf-name>` | The VRF name. |

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv show service snmp-server trap-destination localhost vrf BLUE
```

- - -

## nv show service snmp-server trap-destination \<trap-destination-id>\ vrf \<vrf-name>\ community-password

Shows the community password for the SNMP server trap destinations configured for the specified VRF.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
|`<trap-destination-id>` | The SNMP trap destination IP address or hostname. |
|`<vrf-name>` | The VRF name. |

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv show service snmp-server trap-destination localhost vrf BLUE community-password
```

- - -

## nv show service snmp-server trap-destination \<trap-destination-id>\ vrf \<vrf-name>\ community-password \<community-password-id>\

Shows the community password settings for the SNMP server trap destinations configured for the specified VRF.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
|`<trap-destination-id>` | The SNMP trap destination IP address or hostname. |
|`<vrf-name>` | The VRF name. |
|`<community-password-id>` | The community password. |

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv show service snmp-server trap-destination localhost vrf BLUE community-password mynotsosecretpassword
```

- - -

## nv show service snmp-server trap-destination \<trap-destination-id>\ vrf \<vrf-name>\ username

Shows the usernames for the SNMP trap destination in the specified VRF.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
|`<trap-destination-id>` | The SNMP trap destination IP address or hostname. |
|`<vrf-name>` | The VRF name. |

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv show service snmp-server trap-destination localhost vrf BLUE username
```

- - -

## nv show service snmp-server trap-destination \<trap-destination-id>\ vrf \<vrf-name>\ username \<username-id>\

Shows configuration settings for the SNMP trap destination username in the specified VRF.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
|`<trap-destination-id>` | The SNMP trap destination IP address or hostname. |
|`<vrf-name>` | The VRF name. |
|`<username-id>` | The username. |

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv show service snmp-server trap-destination localhost vrf BLUE username myv3user
```

- - -

## nv show service snmp-server trap-destination \<trap-destination-id>\ vrf \<vrf-name>\ username \<username-id>\ auth-md5

Shows SNMP trap destination MD5 authentications for the specified VRF.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
|`<trap-destination-id>` | The SNMP trap destination IP address or hostname. |
|`<vrf-name>` | The VRF name. |
|`<username-id>` | The username. |

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv show service snmp-server trap-destination localhost vrf BLUE username myv3user auth-md5
```

- - -

## nv show service snmp-server trap-destination \<trap-destination-id>\ vrf \<vrf-name>\ username \<username-id>\ auth-md5 \<auth-id>\

Shows information for the SNMP trap destination MD5 authentication for the specified VRF.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
|`<trap-destination-id>` | The SNMP trap destination IP address or hostname. |
|`<vrf-name>` | The VRF name. |
|`<username-id>` | The username. |
|`<auth-id>` | The MD5 password. |

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv show service snmp-server trap-destination localhost vrf BLUE username myv3user auth-md5 md5password2
```

- - -

## nv show service snmp-server trap-destination \<trap-destination-id>\ vrf \<vrf-name>\ username \<username-id>\ auth-md5 \<auth-id>\ engine-id

Shows the engine IDs for the SNMP trap destination username and password for the specified VRF.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
|`<trap-destination-id>` | The SNMP trap destination IP address or hostname. |
|`<vrf-name>` | The VRF name. |
|`<username-id>` | The username. |
|`<auth-id>` | The MD5 password. |

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv show service snmp-server trap-destination localhost vrf BLUE username myv3user auth-md5 md5password2 engine-id
```

- - -

## nv show service snmp-server trap-destination \<trap-destination-id>\ vrf \<vrf-name>\ username \<username-id>\ auth-md5 \<auth-id>\ engine-id \<engine-id>\

Shows information for the specified engine ID associated with the SNMP trap destination username and MD5 password for the specified VRF.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
|`<trap-destination-id>` | The SNMP trap destination IP address or hostname. |
|`<vrf-name>` | The VRF name. |
|`<username-id>` | The username. |
|`<auth-id>` | The MD5 password. |
|`<engine-id>` | The engine ID. |

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv show service snmp-server trap-destination localhost vrf BLUE username myv3user auth-md5 md5password2 engine-id 0x80001f888070939b14a514da5a00000000
```

- - -

## nv show service snmp-server trap-destination \<trap-destination-id>\ vrf \<vrf-name>\ username \<username-id>\ auth-md5 \<auth-id>\ encrypt-des

Shows the DES encryptions for MD5 authentication for the SNMP trap destination username and MD5 password.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<trap-destination-id>` | The SNMP trap destination IP address or hostname. |
|`<vrf-name>` | The VRF name. |
|`<username-id>` | The username. |
|`<auth-id>` | The MD5 password. |

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv show service snmp-server trap-destination localhost vrf BLUE username myv3user auth-md5 md5password2 encrypt-des
```

- - -

## nv show service snmp-server trap-destination \<trap-destination-id>\ vrf \<vrf-name>\ username \<username-id>\ auth-md5 \<auth-id>\ encrypt-des \<encrypt-id>\

Shows information about the DES encryption for MD5 authentication for the SNMP trap destination username and MD5 password.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<trap-destination-id>` | The SNMP trap destination IP address or hostname. |
|`<vrf-name>` | The VRF name. |
|`<username-id>` | The username. |
|`<auth-id>` | The MD5 password. |
|`<encrypt-id>` | The DES encryption ID for MD5 authentication. |

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv show service snmp-server trap-destination localhost vrf BLUE username myv3user auth-md5 md5password2 encrypt-des myaessecret2
```

- - -

## nv show service snmp-server trap-destination \<trap-destination-id>\ vrf \<vrf-name>\ username \<username-id>\ auth-md5 \<auth-id>\ encrypt-des \<encrypt-id>\ engine-id

Shows the engine ID for the DES encryption for MD5 authentication for the SNMP trap destination username and MD5 password.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| --------- | -------------- |
| `<trap-destination-id>` | The SNMP trap destination IP address or hostname. |
|`<vrf-name>` | The VRF name. |
|`<username-id>` | The username. |
|`<auth-id>` | The MD5 password. |
|`<encrypt-id>` | The DES encryption ID for MD5 authentication. |

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv show service snmp-server trap-destination localhost vrf BLUE username myv3user auth-md5 md5password2 encrypt-des myaessecret2 engine-id
```

- - -

## nv show service snmp-server trap-destination \<trap-destination-id>\ vrf \<vrf-name>\ username \<username-id>\ auth-md5 \<auth-id>\ encrypt-des \<encrypt-id>\ engine-id \<engine-id>\

Shows information about the engine ID for DES encryption for MD5 authentication for the SNMP trap destination username and MD5 password.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<trap-destination-id>` | The SNMP trap destination IP address or hostname. |
|`<vrf-name>` | The VRF name. |
|`<username-id>` | The username. |
|`<auth-id>` | The MD5 password. |
|`<encrypt-id>` | The DES encryption ID for MD5 authentication. |
|`<engine-id>` | The engine ID. |

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv show service snmp-server trap-destination localhost vrf BLUE username myv3user auth-md5 md5password2 encrypt-des myaessecret2 engine-id 0x80001f888070939b14a514da5a00000000
```

- - -

## nv show service snmp-server trap-destination \<trap-destination-id>\ vrf \<vrf-name>\ username \<username-id>\ auth-sha

Shows the SHA authentications for the user specified for the SNMP trap destination.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<trap-destination-id>` | The SNMP trap destination IP address or hostname. |
|`<vrf-name>` | The VRF name. |
|`<username-id>` | The username. |

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv show service snmp-server trap-destination localhost vrf BLUE username myv3user auth-sha
```

- - -

## nv show service snmp-server trap-destination \<trap-destination-id>\ vrf \<vrf-name>\ username \<username-id>\ auth-sha \<auth-id>\

Shows information about the specified SHA authentication for the user specified for the SNMP trap destination.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<trap-destination-id>` | The SNMP trap destination IP address or hostname. |
|`<vrf-name>` | The VRF name. |
|`<username-id>` | The username. |
|`<auth-id>` | The SHA authentication password. |

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv show service snmp-server trap-destination localhost vrf BLUE username myv3user auth-sha SHApassword1
```

- - -

## nv show service snmp-server trap-destination \<trap-destination-id>\ vrf \<vrf-name>\ username \<username-id>\ auth-sha \<auth-id>\ engine-id

Shows the engine IDs for the SNMP trap destination username and SHA password.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<trap-destination-id>` | The SNMP trap destination IP address or hostname. |
|`<vrf-name>` | The VRF name. |
|`<username-id>` | The username. |
|`<auth-id>` | The SHA authentication password. |

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv show service snmp-server trap-destination localhost vrf BLUE username myv3user auth-sha SHApassword1 engine-id
```

- - -

## nv show service snmp-server trap-destination \<trap-destination-id>\ vrf \<vrf-name>\ username \<username-id>\ auth-sha \<auth-id>\ engine-id \<engine-id>\

Shows information about the engine ID for the SNMP trap destination username and SHA password.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<trap-destination-id>` | The SNMP trap destination IP address or hostname. |
|`<vrf-name>` | The VRF name. |
|`<username-id>` | The username. |
|`<auth-id>` | The SHA authentication password. |
|`<engine-id>` | The engine ID. |

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv show service snmp-server trap-destination localhost vrf BLUE username myv3user auth-sha SHApassword1 engine-id 0x80001f888070939b14a514da5a00000000
```

- - -

## nv show service snmp-server trap-destination \<trap-destination-id>\ vrf \<vrf-name>\ username \<username-id>\ auth-sha \<auth-id>\ encrypt-des

Shows the DES encryptions for the SNMP trap destination username and SHA password.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<trap-destination-id>` | The SNMP trap destination IP address or hostname. |
|`<vrf-name>` | The VRF name. |
|`<username-id>` | The username. |
|`<auth-id>` | The SHA authentication password. |

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv show service snmp-server trap-destination localhost vrf BLUE username myv3user auth-sha SHApassword1 encrypt-des
```

- - -

## nv show service snmp-server trap-destination \<trap-destination-id>\ vrf \<vrf-name>\ username \<username-id>\ auth-sha \<auth-id>\ encrypt-des \<encrypt-id>\

Shows information about the DES encryption for SHA authentication for the SNMP trap destination username and SHA password.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<trap-destination-id>` | The SNMP trap destination IP address or hostname. |
|`<vrf-name>` | The VRF name. |
|`<username-id>` | The username. |
|`<auth-id>` | The SHA password. |
|`<encrypt-id>` | The DES encryption ID for SHA authentication. |

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv show service snmp-server trap-destination localhost vrf BLUE username myv3user auth-sha SHApassword1 encrypt-des user666encryption
```

- - -

## nv show service snmp-server trap-destination \<trap-destination-id>\ vrf \<vrf-name>\ username \<username-id>\ auth-sha \<auth-id>\ encrypt-des \<encrypt-id>\ engine-id

Shows the engine ID for the DES encryption for SHA authentication for the SNMP trap destination username and SHA password.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<trap-destination-id>` | The SNMP trap destination IP address or hostname. |
|`<vrf-name>` | The VRF name. |
|`<username-id>` | The username. |
|`<auth-id>` | The SHA password. |
|`<encrypt-id>` | The DES encryption ID for SHA authentication. |

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv show service snmp-server trap-destination localhost vrf BLUE username user666password encrypt-aes user666encryption engine-id
```

- - -

## nv show service snmp-server trap-destination \<trap-destination-id>\ vrf \<vrf-name>\ username \<username-id>\ auth-sha \<auth-id>\ encrypt-des \<encrypt-id>\ engine-id \<engine-id>\

Shows information for the engine ID for the DES encryption for SHA authentication for the SNMP trap destination username and SHA password.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<trap-destination-id>` | The SNMP trap destination IP address or hostname. |
|`<vrf-name>` | The VRF name. |
|`<username-id>` | The username. |
|`<auth-id>` | The SHA password. |
|`<encrypt-id>` | The DES encryption ID for SHA authentication. |
|`<engine-id>` | The engine ID. |

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv show service snmp-server trap-destination localhost vrf BLUE username user666password encrypt-aes user666encryption engine-id 0x80001f888070939b14a514da5a00000000
```

- - -

## nv show service snmp-server trap-destination \<trap-destination-id>\ username

Shows the list of usernames for the SNMP trap destination.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<trap-destination-id>` | The SNMP trap destination IP address or hostname. |
|`<username-id>` | The username. |

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv show service snmp-server trap-destination localhost 
```

- - -

## nv show service snmp-server trap-destination \<trap-destination-id>\ username \<username-id>\

Shows information about the specified username for the SNMP trap destination.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<trap-destination-id>` | The SNMP trap destination IP address or hostname. |
|`<username-id>` | The username. |

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv show service snmp-server trap-destination localhost username user1
```

- - -

## nv show service snmp-server trap-destination \<trap-destination-id>\ username \<username-id>\ auth-md5

Shows the MD5 password for the specified username for the SNMP trap destination.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<trap-destination-id>` | The SNMP trap destination IP address or hostname. |
|`<username-id>` | The username. |

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv show service snmp-server trap-destination localhost username user1 auth-md5
```

- - -

## nv show service snmp-server trap-destination \<trap-destination-id>\ username \<username-id>\ auth-md5 \<auth-id>\

Shows information about the specified username and MD5 password for the SNMP trap destination.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<trap-destination-id>` | The SNMP trap destination IP address or hostname. |
|`<username-id>` | The username. |
|`<auth-id>` | The MD5 password. |

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv show service snmp-server trap-destination localhost username user1 auth-md5 user1password
```

- - -

## nv show service snmp-server trap-destination \<trap-destination-id>\ username \<username-id>\ auth-md5 \<auth-id>\ engine-id

Shows the engine ID for the SNMP trap destination username and MD5 password.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<trap-destination-id>` | The SNMP trap destination IP address or hostname. |
|`<username-id>` | The username. |
|`<auth-id>` | The MD5 password. |

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv show service snmp-server trap-destination localhost username user1 auth-md5 user1password engine-id

```

- - -

## nv show service snmp-server trap-destination \<trap-destination-id>\ username \<username-id>\ auth-md5 \<auth-id>\ engine-id \<engine-id>\

Shows information for the engine ID for MD5 authentication for the SNMP trap destination username and MD5 password.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<trap-destination-id>` | The SNMP trap destination IP address or hostname. |
|`<username-id>` | The username. |
|`<auth-id>` | The MD5 password. |
|`<engine-id>` | The engine ID. |

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv show service snmp-server trap-destination localhost username user1 auth-md5 user1password engine-id 0x80001f888070939b14a514da5a00000000
```

- - -

## nv show service snmp-server trap-destination \<trap-destination-id>\ username \<username-id>\ auth-md5 \<auth-id>\ encrypt-des

Shows the DES encryption for MD5 authentication for the SNMP trap destination username and MD5 password.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<trap-destination-id>` | The SNMP trap destination IP address or hostname. |
|`<username-id>` | The username. |
|`<auth-id>` | The MD5 password. |

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv show service snmp-server trap-destination localhost username user3 auth-md5 user3password encrypt-des
```

- - -

## nv show service snmp-server trap-destination \<trap-destination-id>\ username \<username-id>\ auth-md5 \<auth-id>\ encrypt-des \<encrypt-id>\

Shows information about the DES encryption for MD5 authentication for the SNMP trap destination username and MD5 password.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<trap-destination-id>` | The SNMP trap destination IP address or hostname. |
|`<username-id>` | The username. |
|`<auth-id>` | The MD5 password. |
|`<encrypt-id>` | The DES encryption ID for MD5 authentication. |

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv show service snmp-server trap-destination localhost username user3 auth-md5 user3password encrypt-des user3encryption
```

- - -
## nv show service snmp-server trap-destination \<trap-destination-id>\ username \<username-id>\ auth-md5 \<auth-id>\ encrypt-des \<encrypt-id>\ engine-id

Shows the engine ID for DES encryption for MD5 authentication for the SNMP trap destination username and MD5 password.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<trap-destination-id>` | The SNMP trap destination IP address or hostname. |
|`<username-id>` | The username. |
|`<auth-id>` | The MD5 password. |
|`<encrypt-id>` | The DES encryption ID for MD5 authentication. |

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv show service snmp-server trap-destination localhost username user3 auth-md5 user3password encrypt-des user3encryption engine-id
```

- - -

## nv show service snmp-server trap-destination \<trap-destination-id>\ username \<username-id>\ auth-md5 \<auth-id>\ encrypt-des \<encrypt-id>\ engine-id \<engine-id>\

Shows information about the engine ID for DES encryption for MD5 authentication for the SNMP trap destination username and MD5 password.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<trap-destination-id>` | The SNMP trap destination IP address or hostname. |
|`<username-id>` | The username. |
|`<auth-id>` | The MD5 password. |
|`<encrypt-id>` | The DES encryption ID for MD5 authentication. |
|`<engine-id>` | The engine ID. |

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv show service snmp-server trap-destination localhost username user3 auth-md5 user3password encrypt-des user3encryption engine-id 0x80001f888070939b14a514da5a00000000
```

- - -

## nv show service snmp-server trap-destination \<trap-destination-id>\ username \<username-id>\ auth-sha

Shows the SHA authentications for the user specified for the SNMP trap destination.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<trap-destination-id>` | The SNMP trap destination IP address or hostname. |
|`<username-id>` | The username. |

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv show service snmp-server trap-destination localhost username limiteduser1 auth-sha
```

- - -

## nv show service snmp-server trap-destination \<trap-destination-id>\ username \<username-id>\ auth-sha \<auth-id>\

Shows information about the specified SHA authentication for the user specified for the SNMP trap destination.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<trap-destination-id>` | The SNMP trap destination IP address or hostname. |
|`<username-id>` | The username. |
|`<auth-id>` | The SHA password. |

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv show service snmp-server trap-destination localhost username limiteduser1 auth-sha SHApassword1
```

- - -

## nv show service snmp-server trap-destination \<trap-destination-id>\ username \<username-id>\ auth-sha \<auth-id>\ engine-id

Shows the engine IDs for the SNMP trap destination username and SHA password.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<trap-destination-id>` | The SNMP trap destination IP address or hostname. |
|`<username-id>` | The username. |
|`<auth-id>` | The SHA password. |

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv show service snmp-server trap-destination localhost username limiteduser1 auth-sha SHApassword1 engine-id
```

- - -

## nv show service snmp-server trap-destination \<trap-destination-id>\ username \<username-id>\ auth-sha \<auth-id>\ engine-id \<engine-id>\

Shows information about the engine ID for the SNMP trap destination username and SHA password.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<trap-destination-id>` | The SNMP trap destination IP address or hostname. |
|`<username-id>` | The username. |
|`<auth-id>` | The SHA password. |
|`<engine-id>` | The engine ID. |

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv show service snmp-server trap-destination localhost username limiteduser1 auth-sha SHApassword1 engine-id 0x80001f888070939b14a514da5a00000000
```

- - -

## nv show service snmp-server trap-destination \<trap-destination-id>\ username \<username-id>\ auth-sha \<auth-id>\ encrypt-des

Shows the DES encryptions for the SNMP trap destination username and SHA password.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<trap-destination-id>` | The SNMP trap destination IP address or hostname. |
|`<username-id>` | The username. |
|`<auth-id>` | The SHA password. |

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv show service snmp-server trap-destination localhost username user666 auth-sha user666password encrypt-aes
```

- - -

## nv show service snmp-server trap-destination \<trap-destination-id>\ username \<username-id>\ auth-sha \<auth-id>\ encrypt-des \<encrypt-id>\

Shows information about the DES encryptions for the SNMP trap destination username and SHA password.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<trap-destination-id>` | The SNMP trap destination IP address or hostname. |
|`<username-id>` | The username. |
|`<auth-id>` | The SHA password. |
|`<encrypt-id>` | The DES encryption ID for SHA authentication. |

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv show service snmp-server trap-destination localhost username user666 auth-sha user666password encrypt-aes user666encryption
```

- - -

## nv show service snmp-server trap-destination \<trap-destination-id>\ username \<username-id>\ auth-sha \<auth-id>\ encrypt-des \<encrypt-id>\ engine-id

Shows the engine IDs for the DES encryptions for the SNMP trap destination username and SHA password.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<trap-destination-id>` | The SNMP trap destination IP address or hostname. |
|`<username-id>` | The username. |
|`<auth-id>` | The SHA password. |
|`<encrypt-id>` | The DES encryption ID for SHA authentication. |

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv show service snmp-server trap-destination localhost username user666 auth-sha user666password encrypt-aes user666encryption engine-id
```

- - -

## nv show service snmp-server trap-destination \<trap-destination-id>\ username \<username-id>\ auth-sha \<auth-id>\ encrypt-des \<encrypt-id>\ engine-id \<engine-id>\

Shows information about the engine ID for the DES encryptions for the SNMP trap destination username and SHA password.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<trap-destination-id>` | The SNMP trap destination IP address or hostname. |
|`<username-id>` | The username. |
|`<auth-id>` | The SHA password. |
|`<encrypt-id>` | The DES encryption ID for SHA authentication. |
|`<engine-id>` | The engine ID. |

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv show service snmp-server trap-destination localhost username user666 auth-sha user666password encrypt-aes user666encryption engine-id 0x80001f888070939b14a514da5a00000000
```

- - -
