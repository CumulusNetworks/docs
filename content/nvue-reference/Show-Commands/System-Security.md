---
title: System Security
author: Cumulus Networks
weight: 410

type: nojsscroll
---
<style>
h { color: RGB(118,185,0)}
</style>

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system security</h>

Shows security settings on the switch.

### Version History

Introduced in Cumulus Linux 5.9.0

### Example

```
cumulus@switch:~$ nv show system security
                           operational  applied
-------------------------  -----------  -------
fips
  mode                     enabled      enabled
password-hardening
  state                    enabled      enabled
  reject-user-passw-match  enabled      enabled
  lower-class              enabled      enabled
  upper-class              enabled      enabled
  digits-class             enabled      enabled
  special-class            enabled      enabled
  expiration-warning       15           15
  expiration               180          180
  history-cnt              10           10
  len-min                  8            8
encryption
  db
    state                               enabled
...
```

{{%notice note%}}
Cumulus Linux 5.16.0 introduce FIPS mode. If you are running Cumulus Linux 5.15 or earlier, the `nv show system security` command output does not show FIPS mode configuration.
{{%/notice%}}

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system security ca-certificate</h>

Shows all the CA certificates on the switch.

### Version History

Introduced in Cumulus Linux 5.7.0

### Example

```
cumulus@switch:~$ nv show system security ca-certificate
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system security ca-certificate \<cert-id\></h>

Shows brief information about a specific CA certificate.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<cert-id>` |  The CA certificate name. |

### Version History

Introduced in Cumulus Linux 5.7.0

### Example

```
cumulus@switch:~$ nv show system security ca-certificate cert-1
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system security ca-certificate \<cert-id\> dump</h>

Shows detailed information about a specific CA certificate.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<cert-id>` |  The CA certificate name. |

### Version History

Introduced in Cumulus Linux 5.7.0

### Example

```
cumulus@switch:~$ nv show system security ca-certificate cert-1 dump
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system security certificate</h>

Shows all the entity certificates on the switch.

### Version History

Introduced in Cumulus Linux 5.7.0

### Example

```
cumulus@switch:~$ nv show system security certificate
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system security certificate \<cert-id\></h>

Shows brief information about a specific entity certificate.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<cert-id>` |  The certificate name. |

### Version History

Introduced in Cumulus Linux 5.7.0

### Example

```
cumulus@switch:~$ nv show system security certificate cert-2
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system security certificate \<cert-id\> dump</h>

Shows detailed information about a specific entity certificate.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<cert-id>` |  The certificate name. |

### Version History

Introduced in Cumulus Linux 5.7.0

### Example

```
cumulus@switch:~$ nv show system security certificate cet2 dump
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system security certificate \<cert-id\> installed</h>

Shows the applications that are using a specific entity certificate.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<cert-id>` |  The certificate name. |

### Version History

Introduced in Cumulus Linux 5.7.0

### Example

```
cumulus@switch:~$ nv show system security certificate cert-2 installed
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system security encryption</h>

Shows if NVUE password encryption is enabled, By default, NVUE encrypts passwords, such as the RADIUS secret, TACACS secret, BGP peer password, OSPF MD5 key, and SNMP strings in the startup.yaml file.

### Version History

Introduced in Cumulus Linux 5.10.0

### Example

```
cumulus@switch:~$ nv show system security encryption
         operational  applied
-------  -----------  -------
db                           
  state               enabled
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system security encryption db</h>

Shows if NVUE password encryption is enabled, By default, NVUE encrypts passwords, such as the RADIUS secret, TACACS secret, BGP peer password, OSPF MD5 key, and SNMP strings in the startup.yaml file.

### Version History

Introduced in Cumulus Linux 5.10.0

### Example

```
cumulus@switch:~$ nv show system security encryption db
       operational  applied
-----  -----------  -------
state  enabled      enabled
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system security fips</h>

Shows if FIPS mode is enabled. FIPS are standards for federal computer systems developed by the U.S. government and published by the National Institute of Standards and Technology (NIST).

When you enable FIPS mode, the switch enforces FIPS 140-2 and 140-3 compliant cryptographic operations, making it suitable for high-security and regulated environments.

The default FIPS mode is `disabled`.

### Version History

Introduced in Cumulus Linux 5.16.0

### Example

```
cumulus@switch:~$ nv show system security fips
                           operational  applied
-------------------------  -----------  -------
mode                       enabled      enabled
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system security password-hardening</h>

Shows the currently configured password policies for the switch.

### Version History

Introduced in Cumulus Linux 5.9.0

### Example

```
cumulus@switch:~$ nv show system security password-hardening
                         operational  applied 
-----------------------  -----------  --------
state                    enabled      enabled 
reject-user-passw-match  disabled     disabled
lower-class              enabled      enabled 
upper-class              enabled      enabled 
digits-class             disabled     disabled
special-class            disabled     disabled
expiration-warning       15           15      
expiration               180          180     
history-cnt              20           20      
len-min                  8            8
```
