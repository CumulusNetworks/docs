---
title: SNMP Server
author: Cumulus Networks
weight: 360
type: nojsscroll
---
<style>
h { color: RGB(118,185,0)}
</style>
<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show service snmp-server</h>

Shows global SNMP server configuration on the switch, such as the listening addresses, trap link down and up check frequency, and the list of users.

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv show service snmp-server
                     applied                
-------------------  -----------------------
[listening-address]  10.10.10.10            
[listening-address]  192.168.200.11         
[listening-address]  localhost              
[listening-address]  localhost-v6           
system-contact       myemail@example.com    
system-location      my-private-bunker      
enable               on                     
trap-link-down                              
  check-frequency    10                     
trap-link-up                                
  check-frequency    15                     
                     enable                 
                     listening-address      
                     readonly-community     
                     readonly-community-v6  
                     system-contact         
                     system-location        
                     system-name            
                     trap-cpu-load-average  
                     trap-destination       
                     trap-link-down         
                     trap-link-up           
                     trap-snmp-auth-failures
                     username               
                     viewname               
[username]           limiteduser1           
[username]           testuserauth           
[username]           testusernoauth         
system-name          CumulusBox-1,543,567
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show service snmp-server listening-address</h>

Shows the SNMP server listening address configured on the switch.

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv show service snmp-server listening-address
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show service snmp-server listening-address \<listening-address-id\></h>

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

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show service snmp-server username</h>

Shows the SNMP server username configured on the switch.

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv show service snmp-server username
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show service snmp-server username \<username-id\></h>

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
           applied          
----------  -----------------
[auth-md5]  myauthmd5password
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show service snmp-server username \<username-id\> auth-none</h>

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

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show service snmp-server username \<username-id\> auth-md5</h>

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

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show service snmp-server username \<username-id\> auth-md5 \<auth-id\></h>

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

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show service snmp-server username \<username-id\> auth-md5 \<auth-id\> encrypt-des</h>

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

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show service snmp-server username \<username-id\> auth-md5 \<auth-id\> encrypt-des \<encrypt-id\></h>

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

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show service snmp-server username \<username-id\> auth-md5 \<auth-id\> encrypt-aes</h>

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

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show service snmp-server username \<username-id\> auth-md5 \<auth-id\> encrypt-aes \<encrypt-id\></h>

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

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show service snmp-server username \<username-id\> auth-sha</h>

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

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show service snmp-server username \<username-id\> auth-sha \<auth-id\></h>

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

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show service snmp-server username \<username-id\> auth-sha \<auth-id\> encrypt-des</h>

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

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show service snmp-server username \<username-id\> auth-sha \<auth-id\> encrypt-des \<encrypt-id\></h>

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

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show service snmp-server username \<username-id\> auth-sha \<auth-id\> encrypt-aes</h>

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

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show service snmp-server username \<username-id\> auth-sha \<auth-id\> encrypt-aes \<encrypt-id\></h>

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

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show service snmp-server mibs</h>

Shows the SNMP MIBS.

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv show service snmp-server mibs
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show service snmp-server viewname</h>

Shows the configured SNMP server view names. SNMP views are groups of MIB objects that you can associate with user accounts to allow limited access to view and modify SNMP statistics and system configuration.

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv show service snmp-server viewname
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show service snmp-server viewname \<viewname-id\></h>

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

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show service snmp-server readonly-community</h>

Shows the SNMP server readonly community strings.

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv show service snmp-server readonly-community 
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show service snmp-server readonly-community \<readonly-community-id\></h>

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

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show service snmp-server readonly-community \<readonly-community-id\> access</h>

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

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show service snmp-server readonly-community \<readonly-community-id\> access \<access-id\></h>

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

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show service snmp-server readonly-community-v6</h>

Shows the IPv6 SNMP server readonly community strings.

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv show service snmp-server readonly-community-v6
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show service snmp-server readonly-community-v6 \<readonly-community-id\></h>

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

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show service snmp-server readonly-community-v6 \<readonly-community-id\> access</h>

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

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show service snmp-server readonly-community-v6 \<readonly-community-id\> access \<access-id\></h>

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

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show service snmp-server trap-link-down</h>

Shows the SNMP traps for the interface link down status.

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv show service snmp-server trap-link-down
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show service snmp-server trap-link-up</h>

Shows SNMP traps for the interface link up status.

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv show service snmp-server trap-link-up
                 applied
---------------  -------
check-frequency  15
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show service snmp-server trap-snmp-auth-failures</h>

Shows SNMP traps for SNMP authentication failures.

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv show service snmp-server trap-snmp-auth-failures
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show service snmp-server trap-cpu-load-average</h>

Shows the SNMP traps generated when the CPU load average exceeds a certain threshold.

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv show service snmp-server trap-cpu-load-average
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show service snmp-server trap-cpu-load-average one-minute</h>

Shows the SNMP traps generated when the CPU load average exceeds the one-minute threshold.

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv show service snmp-server trap-cpu-load-average one-minute
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show service snmp-server trap-cpu-load-average one-minute \<one-minute-id\></h>

Shows the SNMP traps generated when the CPU load average for the one-minute interval exceeds a certain percentage.

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

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show service snmp-server trap-cpu-load-average one-minute \<one-minute-id\> five-minute</h>

Shows the SNMP traps generated when the CPU load average for the one-minute interval exceeds a certain percentage and reaches the five-minute interval.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<one-minute-id>` | The one-minute load average threshold ID.|

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv show service snmp-server trap-cpu-load-average one-minute 102 five-minute
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show service snmp-server trap-cpu-load-average one-minute \<one-minute-id\> five-minute \<five-minute-id\></h>

Shows the SNMP traps generated when the CPU load average for the one-minute interval and the five-minute interval exceed a certain percentage.

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

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show service snmp-server trap-cpu-load-average one-minute \<one-minute-id\> five-minute \<five-minute-id\> fifteen-minute</h>

Shows the SNMP traps generated when the CPU load average for the one-minute interval and the five-minute interval exceed a certain percentage and reaches the fifteen-minute interval.

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

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show service snmp-server trap-cpu-load-average one-minute \<one-minute-id\> five-minute \<five-minute-id\> fifteen-minute \<fifteen-minute-id\></h>

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

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show service snmp-server trap-destination</h>

Shows the SNMP trap destinations.

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv show service snmp-server trap-destination
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show service snmp-server trap-destination \<trap-destination-id\></h>

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

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show service snmp-server trap-destination \<trap-destination-id\> community-password</h>

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

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show service snmp-server trap-destination \<trap-destination-id\> community-password \<community-password-id\></h>

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

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show service snmp-server trap-destination \<trap-destination-id\> vrf</h>

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

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show service snmp-server trap-destination \<trap-destination-id\> vrf \<vrf-name\></h>

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

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show service snmp-server trap-destination \<trap-destination-id\> vrf \<vrf-name\> community-password</h>

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

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show service snmp-server trap-destination \<trap-destination-id\> vrf \<vrf-name\> community-password \<community-password-id\></h>

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

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show service snmp-server trap-destination \<trap-destination-id\> vrf \<vrf-name\> username</h>

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

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show service snmp-server trap-destination \<trap-destination-id\> vrf \<vrf-name\> username \<username-id\></h>

Shows configuration settings for the SNMP trap destination username for the specified VRF.

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

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show service snmp-server trap-destination \<trap-destination-id\> vrf \<vrf-name\> username \<username-id\> auth-md5</h>

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

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show service snmp-server trap-destination \<trap-destination-id\> vrf \<vrf-name\> username \<username-id\> auth-md5 \<auth-id\></h>

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

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show service snmp-server trap-destination \<trap-destination-id\> vrf \<vrf-name\> username \<username-id\> auth-md5 \<auth-id\> engine-id</h>

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

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show service snmp-server trap-destination \<trap-destination-id\> vrf \<vrf-name\> username \<username-id\> auth-md5 \<auth-id\> engine-id \<engine-id\></h>

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

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show service snmp-server trap-destination \<trap-destination-id\> vrf \<vrf-name\> username \<username-id\> auth-md5 \<auth-id\> encrypt-des</h>

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

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show service snmp-server trap-destination \<trap-destination-id\> vrf \<vrf-name\> username \<username-id\> auth-md5 \<auth-id\> encrypt-des \<encrypt-id\></h>

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

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show service snmp-server trap-destination \<trap-destination-id\> vrf \<vrf-name\> username \<username-id\> auth-md5 \<auth-id\> encrypt-des \<encrypt-id\> engine-id</h>

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

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show service snmp-server trap-destination \<trap-destination-id\> vrf \<vrf-name\> username \<username-id\> auth-md5 \<auth-id\> encrypt-des \<encrypt-id\> engine-id \<engine-id\></h>

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

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show service snmp-server trap-destination \<trap-destination-id\> vrf \<vrf-name\> username \<username-id\> auth-sha</h>

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

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show service snmp-server trap-destination \<trap-destination-id\> vrf \<vrf-name\> username \<username-id\> auth-sha \<auth-id\></h>

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

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show service snmp-server trap-destination \<trap-destination-id\> vrf \<vrf-name\> username \<username-id\> auth-sha \<auth-id\> engine-id</h>

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

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show service snmp-server trap-destination \<trap-destination-id\> vrf \<vrf-name\> username \<username-id\> auth-sha \<auth-id\> engine-id \<engine-id\></h>

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

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show service snmp-server trap-destination \<trap-destination-id\> vrf \<vrf-name\> username \<username-id\> auth-sha \<auth-id\> encrypt-des</h>

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

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show service snmp-server trap-destination \<trap-destination-id\> vrf \<vrf-name\> username \<username-id\> auth-sha \<auth-id\> encrypt-des \<encrypt-id\></h>

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

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show service snmp-server trap-destination \<trap-destination-id\> vrf \<vrf-name\> username \<username-id\> auth-sha \<auth-id\> encrypt-des \<encrypt-id\> engine-id</h>

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

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show service snmp-server trap-destination \<trap-destination-id\> vrf \<vrf-name\> username \<username-id\> auth-sha \<auth-id\> encrypt-des \<encrypt-id\> engine-id \<engine-id\></h>

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

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show service snmp-server trap-destination \<trap-destination-id\> username</h>

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

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show service snmp-server trap-destination \<trap-destination-id\> username \<username-id\></h>

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

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show service snmp-server trap-destination \<trap-destination-id\> username \<username-id\> auth-md5</h>

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

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show service snmp-server trap-destination \<trap-destination-id\> username \<username-id\> auth-md5 \<auth-id\></h>

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

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show service snmp-server trap-destination \<trap-destination-id\> username \<username-id\> auth-md5 \<auth-id\> engine-id</h>

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

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show service snmp-server trap-destination \<trap-destination-id\> username \<username-id\> auth-md5 \<auth-id\> engine-id \<engine-id\></h>

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

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show service snmp-server trap-destination \<trap-destination-id\> username \<username-id\> auth-md5 \<auth-id\> encrypt-des</h>

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

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show service snmp-server trap-destination \<trap-destination-id\> username \<username-id\> auth-md5 \<auth-id\> encrypt-des \<encrypt-id\></h>

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

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show service snmp-server trap-destination \<trap-destination-id\> username \<username-id\> auth-md5 \<auth-id\> encrypt-des \<encrypt-id\> engine-id</h>

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

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show service snmp-server trap-destination \<trap-destination-id\> username \<username-id\> auth-md5 \<auth-id\> encrypt-des \<encrypt-id\> engine-id \<engine-id\></h>

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

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show service snmp-server trap-destination \<trap-destination-id\> username \<username-id\> auth-sha</h>

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

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show service snmp-server trap-destination \<trap-destination-id\> username \<username-id\> auth-sha \<auth-id\></h>

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

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show service snmp-server trap-destination \<trap-destination-id\> username \<username-id\> auth-sha \<auth-id\> engine-id</h>

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

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show service snmp-server trap-destination \<trap-destination-id\> username \<username-id\> auth-sha \<auth-id\> engine-id \<engine-id\></h>

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

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show service snmp-server trap-destination \<trap-destination-id\> username \<username-id\> auth-sha \<auth-id\> encrypt-des</h>

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

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show service snmp-server trap-destination \<trap-destination-id\> username \<username-id\> auth-sha \<auth-id\> encrypt-des \<encrypt-id\></h>

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

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show service snmp-server trap-destination \<trap-destination-id\> username \<username-id\> auth-sha \<auth-id\> encrypt-des \<encrypt-id\> engine-id</h>

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

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show service snmp-server trap-destination \<trap-destination-id\> username \<username-id\> auth-sha \<auth-id\> encrypt-des \<encrypt-id\> engine-id \<engine-id\></h>

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
