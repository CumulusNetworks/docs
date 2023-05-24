---
title: SNMP Server
author: Cumulus Networks
weight: 730

type: nojsscroll
---
<style>
h { color: RGB(118,185,0)}
</style>
{{%notice note%}}
The `nv unset` commands remove the configuration you set with the equivalent `nv set` commands. This guide only describes an `nv unset` command if it differs from the `nv set` command.
{{%/notice%}}

## <h>nv set service snmp-server</h>

Configures SNMP settings on the switch.

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set service snmp-server enable</h>

Turns the SNMP server on or off.

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv set service snmp-server enable on
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set service snmp-server listening-address \<listening-address-id\></h>

Configures the IP address on which the SNMP agent listens. You can set multiple IP addresses.

For security reasons, the listening address is the localhost by default so that the SNMP agent only responds to requests originating on the switch itself.

You can configure an IPv4 or an IPv6 address. To configure the `snmpd` daemon to listen on all interfaces for either IPv4 or IPv6 UDP port 161 SNMP requests, you can specify a value of `all`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<listening-address-id>` | The IP address on which the SNMP agent listens.|

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv set service snmp-server listening-address all
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set service snmp-server listening-address \<listening-address-id\> vrf \<vrf-name\></h>

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
cumulus@switch:~$ nv set service snmp-server listening-address localhost vrf default
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set service snmp-server mibs</h>

Configures the SNMP server MIBs. You can specify `cumulus-sensor-mib` or `cumulus-status-mib`.

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv set service snmp-server mibs cumulus-status-mib
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set service snmp-server readonly-community \<readonly-community-id\></h>

Configures the SNMP readonly community string for SNMP requests.

Cumulus Linux disables SNMP authentication for SNMPv1 and SNMPv2c by default. To enable authentication, provide a password (community string) for SNMPv1 or SNMPv2c environments so that the `snmpd` daemon can respond to requests. By default, this provides access to the full OID tree for such requests, regardless of their source. Cumulus Linux does not set a default password so `snmpd` does not respond to any requests that arrive unless you set the readonly community password.

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set service snmp-server readonly-community \<readonly-community-id\> access \<access-id\></h>

Configures the source IP address of the host or network to which you want to restrict requests.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<readonly-community-id>` | The SNMP readonly community string.|
| `<access-id>` | The IPv4 address of the host or network to which you want to restrict access.|

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv set service snmp-server readonly-community simplepassword access 192.168.200.10/24
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set service snmp-server readonly-community \<readonly-community-id\> access \<access-id\> oid \<oid\></h>

Configures the OID tree for which you want to restrict access.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<readonly-community-id>` | The SNMP readonly community string.|
| `<access-id>` | The IPv4 address of the host or network to which you want to restrict access.|
| `<oid>` | The OID tree that identifies an SNMP MIB object.|

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv set service snmp-server readonly-community simplepassword access 192.168.200.10/24 oid 1.3.6.1.2.1 
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set service snmp-server readonly-community \<readonly-community-id\> access \<access-id\> view \<view\></h>

Configures the view (the subset of the OID tree) to which you want to restrict viewing access.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<readonly-community-id>` | The SNMP readonly community string.|
| `<access-id>` | The IPv4 address of the host or network to which you want to restrict access.|
| `<view>` | The view (subset of the OID tree).|

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv set service snmp-server readonly-community simplepassword access 192.168.200.10/24 view mysystem
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set service snmp-server readonly-community-v6 \<readonly-community-id\></h>

Configures the SNMP readonly community string for SNMP requests for IPv6.

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set service snmp-server readonly-community-v6 \<readonly-community-id\> access \<access-id\></h>

Configures the source IPv6 address of the host or network to which you want to restrict requests.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<readonly-community-id>` | The SNMP readonly community string.|
| `<access-id>` | The IPv6 address of the host or network to which you want to restrict access.|

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv set service snmp-server readonly-community-v6 simplepassword access 2001:db8:1::100/32
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set service snmp-server readonly-community-v6 \<readonly-community-id\> access \<access-id\> oid \<oid\></h>

Configures the OID tree for which you want to restrict access for IPv6.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<readonly-community-id>` | The SNMP readonly community string.|
| `<access-id>` | The IPv6 address of the host or network to which you want to restrict access.|
| `<oid>` | The OID tree that identifies an SNMP MIB object.|

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv set service snmp-server readonly-community-v6 simplepassword access 2001:db8:1::100/32 oid 1.3.6.1.2.1
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set service snmp-server readonly-community-v6 \<readonly-community-id\> access \<access-id\> view \<value\></h>

Configures the view (the subset of the OID tree) to which you want to restrict viewing access for IPv6.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<readonly-community-id>` | The SNMP readonly community string.|
| `<access-id>` | The IPv6 address of the host or network to which you want to restrict access.|
| `<view>` | The view (subset of the OID tree).|

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv set service snmp-server readonly-community-v6 simplepassword access 2001:db8:1::100/32 view mysystem
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set service snmp-server system-contact \<value\></h>

Configures the username and email address of the contact person for this managed node.

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv set service snmp-server system-contact myemail@example.com
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set service snmp-server system-location</h>

Configures the system physical location for the node in the SNMPv2-MIB system table.

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv set service snmp-server system-location my-private-bunker
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set service snmp-server system-name</h>

Configures a name for the managed node. Typically, this is the fully qualified domain name of the node.

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv set service snmp-server system-name CumulusBox-1,543,567
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set service snmp-server trap-cpu-load-average</h>

Configures the switch to generate SNMP trap notifications for CPU load average thresholds. 

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv set service snmp-server trap-cpu-load-average
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set service snmp-server trap-cpu-load-average one-minute \<one-minute-id\></h>

Configures SNMP to generate a trap when the one-minute interval reaches a specific threshold. You can only use integers or floating point numbers.

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv set service snmp-server trap-cpu-load-average one-minute 5
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set service snmp-server trap-cpu-load-average one-minute \<one-minute-id\> five-minute \<five-minute-id\></h>

Configures SNMP to generate a trap when the one-minute or the five-minute intervals reach a specific threshold. You can only use integers or floating point numbers.

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv set service snmp-server trap-cpu-load-average one-minute 12 five-minute 10
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set service snmp-server trap-cpu-load-average one-minute \<one-minute-id\> five-minute \<five-minute-id\> fifteen-minute \<fifteen-minute-id\></h>

Configures SNMP to generate a trap when the one-minute, the five-minute, or fifteen-minute intervals reach a specific threshold. You can only use integers or floating point numbers.

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv set service snmp-server trap-cpu-load-average one-minute 12 five-minute 10 fifteen-minute 5
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set service snmp-server trap-link-down</h>

Configures the switch to generate notifications when the operational status of the link changes to down.

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv set service snmp-server trap-link-down
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set service snmp-server trap-link-down check-frequency</h>

Configures how often in seconds to check if the link is down to trigger notifications when the operational status of the link changes. You can specify a value between 5 and 300.

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv set service snmp-server trap-link-down check-frequency 10
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set service snmp-server trap-link-up</h>

Configures the switch to generate notifications when the operational status of the link changes to up.

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv set service snmp-server trap-link-up
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set service snmp-server trap-link-up check-frequency</h>

Configures how often in seconds to check if the link is up to trigger notifications when the operational status of the link changes. You can specify a value between 5 and 300.

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv set service snmp-server trap-link-up check-frequency 10
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set service snmp-server trap-destination \<trap-destination-id\></h>

Configures the trap receiver IP address for SNMPv1 and SNMPv2c traps. For SNMP versions 1 and 2c, you must set at least one SNMP trap destination IP address; multiple destinations can exist. Removing all settings disables SNMP traps. The default version is SNMPv2c. You must include a VRF name with the IP address to force traps to send in a non-default VRF table.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<trap-destination-id>` | The IP address of the trap receiver IP address for SNMPv1 and SNMPv2c traps.|

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv set service snmp-server trap-destination localhost
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set service snmp-server trap-destination \<trap-destination-id\> community-password \<community-password-id\></h>

Configures the trap receiver IP address for SNMPv1 and SNMPv2c traps and the community password.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<trap-destination-id>` | The IP address of the SNMP trap destination or `localhost`.|
| `<community-password-id>` | The community password.|

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv set service snmp-server trap-destination localhost community-password mynotsosecretpassword
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set service snmp-server trap-destination \<trap-destination-id\> community-password \<community-password-id\> version</h>

Configures the trap receiver IP address for SNMPv1 and SNMPv2c traps, the community password, and the SNMP version (1 or 2c). The default version is SNMPv2c.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<trap-destination-id>` | The IP address of the SNMP trap destination or `localhost`.|
| `<community-password-id>` | The community password.|

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv set service snmp-server trap-destination localhost community-password mynotsosecretpassword version 1
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set service snmp-server trap-destination \<trap-destination-id\> username \<username-id\></h>

Configures the SNMP trap receiver IP address and SNMP username.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<trap-destination-id>` | The IP address of the SNMP trap destination or `localhost`.|
| `<username-id>` | The SNMP username.|

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv set service snmp-server trap-destination localhost username myv3user
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set service snmp-server trap-destination \<trap-destination-id\> username \<username-id\> auth-md5 \<auth-id\></h>

Configures the SNMP trap receiver IP address, and the SNMP username and MD5 authentication password.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<trap-destination-id>` | The IP address of the SNMP trap destination or `localhost`.|
| `<username-id>` | The SNMP username.|
| `<auth-id>` | The MD5 authentication password.|

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv set service snmp-server trap-destination localhost username myv3user auth-md5 myauthmd5password 
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set service snmp-server trap-destination \<trap-destination-id\> username \<username-id\> auth-md5 \<auth-id\> engine-id \<engine-id\> inform</h>

Configures the trap receiver IP address and VRF for SNMPv1 and SNMPv2c traps, the SNMP username and the MD5 authentication password, and the engine ID.

The SNMP trap receiving daemon must have usernames, authentication passwords, and encryption passwords created with its own EngineID. You must configure this trap server EngineID in the switch `snmpd` daemon sending the trap and inform messages.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<trap-destination-id>` | The IP address of the SNMP trap destination or `localhost`.|
| `<username-id>` | The SNMP username.|
| `<auth-id>` | The MD5 authentication password.|
| `<engine-id>` | The engine ID.|

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv set service snmp-server trap-destination localhost username myv3user auth-md5 myauthmd5password engine-id 0x80001f888070939b14a514da5a00000000 inform
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set service snmp-server trap-destination \<trap-destination-id\> username \<username-id\> auth-md5 \<auth-id\> encrypt-des \<encrypt-id\></h>

Configures the SNMP trap receiver IP address, and the SNMP username and MD5 authentication password, and the DES encryption password.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<trap-destination-id>` | The IP address of the SNMP trap destination or `localhost`.|
| `<username-id>` | The SNMP username.|
| `<auth-id>` | The MD5 authentication password.|
| `<encrypt-id>` | The DES encryption password.|

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv set service snmp-server trap-destination localhost username myv3user auth-md5 myauthmd5password encrypt-des mydessecret2 
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set service snmp-server trap-destination \<trap-destination-id\> username \<username-id\> auth-md5 \<auth-id\> encrypt-des \<encrypt-id\> engine-id \<engine-id\> inform</h>

Configures the trap receiver IP address and VRF for SNMPv1 and SNMPv2c traps, the SNMP username and the MD5 authentication password, the DES encryption password, and the engine ID.

The SNMP trap receiving daemon must have usernames, authentication passwords, and encryption passwords created with its own EngineID. You must configure this trap server EngineID in the switch `snmpd` daemon sending the trap and inform messages.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<trap-destination-id>` | The IP address of the SNMP trap destination or `localhost`.|
| `<username-id>` | The SNMP username.|
| `<auth-id>` | The MD5 authentication password.|
| `<encrypt-id>` | The DES encryption password.|
| `<engine-id>` | The engine ID.|

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv set service snmp-server trap-destination localhost username myv3user auth-md5 myauthmd5password encrypt-des mydessecret2 engine-id 0x80001f888070939b14a514da5a00000000 inform
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set service snmp-server trap-destination \<trap-destination-id\> username \<username-id\> auth-md5 \<auth-id\> encrypt-aes \<encrypt-id\></h>

Configures the SNMP trap receiver IP address, and the SNMP username and MD5 authentication password, and the AES encryption password.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<trap-destination-id>` | The IP address of the SNMP trap destination or `localhost`.|
| `<username-id>` | The SNMP username.|
| `<auth-id>` | The MD5 authentication password.|
| `<encrypt-id>` | The AES encryption password.|

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv set service snmp-server trap-destination localhost username myv3user auth-md5 myauthmd5password encrypt-aes myaessecret2 
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set service snmp-server trap-destination \<trap-destination-id\> username \<username-id\> auth-md5 \<auth-id\> encrypt-aes \<encrypt-id\> engine-id \<engine-id\> inform</h>

Configures the trap receiver IP address and VRF for SNMPv1 and SNMPv2c traps, the SNMP username and the MD5 authentication password, the AES encryption password, and the engine ID.

The SNMP trap receiving daemon must have usernames, authentication passwords, and encryption passwords created with its own EngineID. You must configure this trap server EngineID in the switch `snmpd` daemon sending the trap and inform messages.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<trap-destination-id>` | The IP address of the SNMP trap destination or `localhost`.|
| `<username-id>` | The SNMP username.|
| `<auth-id>` | The MD5 authentication password.|
| `<encrypt-id>` | The AES encryption password.|
| `<engine-id>` | The engine ID.|

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv set service snmp-server trap-destination localhost username myv3user auth-md5 myauthmd5password encrypt-aes myaessecret2 engine-id 0x80001f888070939b14a514da5a00000000 inform
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set service snmp-server trap-destination \<trap-destination-id\> username \<username-id\> auth-sha \<auth-id\></h>

Configures the SNMP trap receiver IP address, and the SNMP username and SHA authentication password.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<trap-destination-id>` | The IP address of the SNMP trap destination or `localhost`.|
| `<username-id>` | The SNMP username.|
| `<auth-id>` | The SHA authentication password.|

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv set service snmp-server trap-destination localhost username myv3user auth-sha SHApassword1
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set service snmp-server trap-destination \<trap-destination-id\> username \<username-id\> auth-sha \<auth-id\> engine-id \<engine-id\> inform</h>

Configures the trap receiver IP address and VRF for SNMPv1 and SNMPv2c traps, the SNMP username and the SHA authentication password, and the engine ID.

The SNMP trap receiving daemon must have usernames, authentication passwords, and encryption passwords created with its own EngineID. You must configure this trap server EngineID in the switch `snmpd` daemon sending the trap and inform messages.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<trap-destination-id>` | The IP address of the SNMP trap destination or `localhost`.|
| `<username-id>` | The SNMP username.|
| `<auth-id>` | The SHA authentication password.|
| `<engine-id>` | The engine ID.|

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv set service snmp-server trap-destination localhost username myv3user auth-sha SHApassword1 engine-id 0x80001f888070939b14a514da5a00000000 inform
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set service snmp-server trap-destination \<trap-destination-id\> username \<username-id\> auth-sha \<auth-id\> encrypt-des \<encrypt-id\></h>

Configures the trap receiver IP address and VRF for SNMPv1 and SNMPv2c traps, the SNMP username and the SHA authentication password, and the DES encryption password.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<trap-destination-id>` | The IP address of the SNMP trap destination or `localhost`.|
| `<username-id>` | The SNMP username.|
| `<auth-id>` | The SHA authentication password.|
| `<encrypt-id>` | The DES encryption password.|

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv set service snmp-server trap-destination localhost username myv3user auth-sha SHApassword1 encrypt-des myencryptsecret
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set service snmp-server trap-destination \<trap-destination-id\> username \<username-id\> auth-sha \<auth-id\> encrypt-des \<encrypt-id\> engine-id \<engine-id\> inform</h>

Configures the trap receiver IP address and VRF for SNMPv1 and SNMPv2c traps, the SNMP username and the SHA authentication password, the DES encryption password, and the engine ID.

The SNMP trap receiving daemon must have usernames, authentication passwords, and encryption passwords created with its own EngineID. You must configure this trap server EngineID in the switch `snmpd` daemon sending the trap and inform messages.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<trap-destination-id>` | The IP address of the SNMP trap destination or `localhost`.|
| `<username-id>` | The SNMP username.|
| `<auth-id>` | The SHA authentication password.|
| `<encrypt-id>` | The DES encryption password.|
| `<engine-id>` | The engine ID.|

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv set service snmp-server trap-destination localhost username myv3user auth-sha SHApassword1 encrypt-des myencryptsecret engine-id 0x80001f888070939b14a514da5a00000000 inform
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set service snmp-server trap-destination \<trap-destination-id\> username \<username-id\> auth-sha \<auth-id\> encrypt-aes \<encrypt-id\></h>

Configures the trap receiver IP address and VRF for SNMPv1 and SNMPv2c traps, the SNMP username and the SHA authentication password, and the AES encryption password.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<trap-destination-id>` | The IP address of the SNMP trap destination or `localhost`.|
| `<username-id>` | The SNMP username.|
| `<auth-id>` | The SHA authentication password.|
| `<encrypt-id>` | The AES encryption password.|

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv set service snmp-server trap-destination localhost username myv3user auth-sha SHApassword1 encrypt-aes myencryptsecret
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set service snmp-server trap-destination \<trap-destination-id\> username \<username-id\> auth-sha \<auth-id\> encrypt-aes \<encrypt-id\> engine-id \<engine-id\> inform</h>

Configures the trap receiver IP address and VRF for SNMPv1 and SNMPv2c traps, the SNMP username and the SHA authentication password, the AES encryption password, and the engine ID.

The SNMP trap receiving daemon must have usernames, authentication passwords, and encryption passwords created with its own EngineID. You must configure this trap server EngineID in the switch `snmpd` daemon sending the trap and inform messages.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<trap-destination-id>` | The IP address of the SNMP trap destination or `localhost`.|
| `<username-id>` | The SNMP username.|
| `<auth-id>` | The SHA authentication password.|
| `<encrypt-id>` | The AES encryption password.|
| `<engine-id>` | The engine ID.|

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv set service snmp-server trap-destination localhost username myv3user auth-sha SHApassword1 encrypt-aes myencryptsecret engine-id 0x80001f888070939b14a514da5a00000000 inform
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set service snmp-server trap-destination \<trap-destination-id\> vrf \<vrf-name\></h>

Configures the trap receiver IP address and VRF for SNMPv1 and SNMPv2c traps. For SNMP versions 1 and 2c, you must set at least one SNMP trap destination IP address; multiple destinations can exist. Removing all settings disables SNMP traps. The default version is SNMPv2c. You must include a VRF name with the IP address to force traps to send in a non-default VRF table.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<trap-destination-id>` | The IP address of the trap receiver IP address for SNMPv1 and SNMPv2c traps.|
| `<vrf-name>` | The VRF name.|

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv set service snmp-server trap-destination localhost vrf RED
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set service snmp-server trap-destination \<trap-destination-id\> vrf \<vrf-name\> community-password \<community-password-id\></h>

Configures the trap receiver IP address and VRF for SNMPv1 and SNMPv2c traps, and the community password.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<trap-destination-id>` | The IP address of the SNMP trap destination or `localhost`.|
| `<vrf-name>` | The VRF name.|
| `<community-password-id>` | The community password.|

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv set service snmp-server trap-destination localhost vrf RED community-password mynotsosecretpassword
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set service snmp-server trap-destination \<trap-destination-id\> vrf \<vrf-name\> community-password \<community-password-id\> version</h>

Configures the trap receiver IP address and VRF for SNMPv1 and SNMPv2c traps, the community password, and the SNMP version (1 or 2c). The default version is 2c.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<trap-destination-id>` | The IP address of the SNMP trap destination or `localhost`.|
| `<vrf-name>` | The VRF name.|
| `<community-password-id>` | The community password.|

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv set service snmp-server trap-destination localhost vrf RED community-password mynotsosecretpassword version 1
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set service snmp-server trap-destination \<trap-destination-id\> vrf \<vrf-name\> username \<username-id\></h>

Configures the trap receiver IP address and VRF for SNMPv1 and SNMPv2c traps, and the SNMP username.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<trap-destination-id>` | The IP address of the SNMP trap destination or `localhost`.|
| `<vrf-name>` | The VRF name.|
| `<username-id>` | The SNMP username.|

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv set service snmp-server trap-destination localhost vrf RED username myv3user
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set service snmp-server trap-destination \<trap-destination-id\> vrf \<vrf-name\> username \<username-id\> auth-md5 \<auth-id\></h>

Configures the trap receiver IP address and VRF for SNMPv1 and SNMPv2c traps, the SNMP username and the MD5 authentication password.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<trap-destination-id>` | The IP address of the SNMP trap destination or `localhost`.|
| `<vrf-name>` | The VRF name.|
| `<username-id>` | The SNMP username.|
| `<auth-id>` | The MD5 authentication password.|

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv set service snmp-server trap-destination localhost vrf RED username myv3user auth-md5 myauthmd5password 
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set service snmp-server trap-destination \<trap-destination-id\> vrf \<vrf-name\> username \<username-id\> auth-md5 \<auth-id\> engine-id \<engine-id\> inform</h>

Configures the trap receiver IP address and VRF for SNMPv1 and SNMPv2c traps, the SNMP username and the MD5 authentication password, and the trap server Engine ID.

The SNMP trap receiving daemon must have usernames, authentication passwords, and encryption passwords created with its own EngineID. You must configure this trap server EngineID in the switch `snmpd` daemon sending the trap and inform messages.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<trap-destination-id>` | The IP address of the SNMP trap destination or `localhost`.|
| `<vrf-name>` | The VRF name.|
| `<username-id>` | The SNMP username.|
| `<auth-id>` | The MD5 authentication password.|
| `<engine-id>` | The trap server engine ID.|

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv set service snmp-server trap-destination localhost vrf RED username myv3user auth-md5 myauthmd5passwor engine-id  0x80001f888070939b14a514da5a00000000 inform
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set service snmp-server trap-destination \<trap-destination-id\> vrf \<vrf-name\> username \<username-id\> auth-md5 \<auth-id\> encrypt-des \<encrypt-id\></h>

Configures the trap receiver IP address and VRF for SNMPv1 and SNMPv2c traps, the SNMP username and MD5 authentication password, and the DES encryption password.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<trap-destination-id>` | The IP address of the SNMP trap destination or `localhost`.|
| `<vrf-name>` | The VRF name.|
| `<username-id>` | The SNMP username.|
| `<auth-id>` | The MD5 authentication password.|
| `<encrypt-id>` | The DES encryption password.|

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv set service snmp-server trap-destination localhost vrf RED username myv3user auth-md5 myauthmd5password encrypt-des user3encryption
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set service snmp-server trap-destination \<trap-destination-id\> vrf \<vrf-name\> username \<username-id\> auth-md5 \<auth-id\> encrypt-des \<encrypt-id\> engine-id \<engine-id\> inform</h>

Configures the trap receiver IP address and VRF for SNMPv1 and SNMPv2c traps, the SNMP username and MD5 authentication password, the DES encryption password, and the trap server engine ID.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<trap-destination-id>` | The IP address of the SNMP trap destination or `localhost`.|
| `<vrf-name>` | The VRF name.|
| `<username-id>` | The SNMP username.|
| `<auth-id>` | The MD5 authentication password.|
| `<encrypt-id>` | The DES encryption password.|
| `<engine-id>` | The engine ID.|

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv set service snmp-server trap-destination localhost vrf RED username myv3user auth-md5 myauthmd5passwor encrypt-des user3encryption engine-id 0x80001f888070939b14a514da5a00000000 inform
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set service snmp-server trap-destination \<trap-destination-id\> vrf \<vrf-name\> username \<username-id\> auth-md5 \<auth-id\> encrypt-aes \<encrypt-id\></h>

Configures the trap receiver IP address and VRF for SNMPv1 and SNMPv2c traps, the SNMP username and MD5 authentication password, and the AES encryption password.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<trap-destination-id>` | The IP address of the SNMP trap destination or `localhost`.|
| `<vrf-name>` | The VRF name.|
| `<username-id>` | The SNMP username.|
| `<auth-id>` | The MD5 authentication password.|
| `<encrypt-id>` | The AES encryption password.|

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv set service snmp-server trap-destination localhost vrf RED username myv3user auth-md5 myauthmd5passwor encrypt-aes myaessecret2
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set service snmp-server trap-destination \<trap-destination-id\> vrf \<vrf-name\> username \<username-id\> auth-md5 \<auth-id\> encrypt-aes \<encrypt-id\> engine-id \<engine-id\> inform</h>

Configures the trap receiver IP address and VRF for SNMPv1 and SNMPv2c traps, the SNMP username and MD5 authentication password, the AES encryption password, and the trap server engine ID.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<trap-destination-id>` | The IP address of the SNMP trap destination or `localhost`.|
| `<vrf-name>` | The VRF name.|
| `<username-id>` | The SNMP username.|
| `<auth-id>` | The MD5 authentication password.|
| `<encrypt-id>` | The AES encryption password.|
| `<engine-id>` | The engine ID.|

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv set service snmp-server trap-destination localhost vrf RED username myv3user auth-md5 myauthmd5password encrypt-aes user3encryption engine-id 0x80001f888070939b14a514da5a00000000 inform
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set service snmp-server trap-destination \<trap-destination-id\> vrf \<vrf-name\> username \<username-id\> auth-sha \<auth-id\></h>

Configures the trap receiver IP address and VRF for SNMPv1 and SNMPv2c traps, the SNMP username and the SHA authentication password.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<trap-destination-id>` | The IP address of the SNMP trap destination or `localhost`.|
| `<vrf-name>` | The VRF name.|
| `<username-id>` | The SNMP username.|
| `<auth-id>` | The SHA authentication password.|

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv set service snmp-server trap-destination localhost vrf RED username myv3user auth-sha SHApassword1
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set service snmp-server trap-destination \<trap-destination-id\> vrf \<vrf-name\> username \<username-id\> auth-sha \<auth-id\> engine-id \<engine-id\> inform</h>

Configures the trap receiver IP address and VRF for SNMPv1 and SNMPv2c traps, the SNMP username and the SHA authentication password, and the engine ID.

The SNMP trap receiving daemon must have usernames, authentication passwords, and encryption passwords created with its own EngineID. You must configure this trap server EngineID in the switch `snmpd` daemon sending the trap and inform messages.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<trap-destination-id>` | The IP address of the SNMP trap destination or `localhost`.|
| `<vrf-name>` | The VRF name.|
| `<username-id>` | The SNMP username.|
| `<auth-id>` | The SHA authentication password.|
| `<engine-id>` | The trap server engine ID.|

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv set service snmp-server trap-destination localhost vrf RED username myv3user auth-sha SHApassword1 engine-id 0x80001f888070939b14a514da5a00000000 inform
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set service snmp-server trap-destination \<trap-destination-id\> vrf \<vrf-name\> username \<username-id\> auth-sha \<auth-id\> encrypt-des \<encrypt-id\></h>

Configures the trap receiver IP address and VRF for SNMPv1 and SNMPv2c traps, the SNMP username and the SHA authentication password, and the DES encryption password.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<trap-destination-id>` | The IP address of the SNMP trap destination or `localhost`.|
| `<vrf-name>` | The VRF name.|
| `<username-id>` | The SNMP username.|
| `<auth-id>` | The SHA authentication password.|
| `<encrypt-id>` | The DES encryption password.|

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv set service snmp-server trap-destination localhost vrf RED username myv3user auth-sha SHApassword1 encrypt-des mydessecret2
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set service snmp-server trap-destination \<trap-destination-id\> vrf \<vrf-name\> username \<username-id\> auth-sha \<auth-id\> encrypt-des \<encrypt-id\> engine-id \<engine-id\> inform</h>

Configures the trap receiver IP address and VRF for SNMPv1 and SNMPv2c traps, the SNMP username and the SHA authentication password, the DES encryption password, and the engine ID.

The SNMP trap receiving daemon must have usernames, authentication passwords, and encryption passwords created with its own EngineID. You must configure this trap server EngineID in the switch `snmpd` daemon sending the trap and inform messages.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<trap-destination-id>` | The IP address of the SNMP trap destination or `localhost`.|
| `<vrf-name>` | The VRF name.|
| `<username-id>` | The SNMP username.|
| `<auth-id>` | The SHA authentication password.|
| `<encrypt-id>` | The DES encryption password.|
| `<engine-id>` | The engine ID.|

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv set service snmp-server trap-destination localhost vrf RED username myv3user auth-sha SHApassword1 encrypt-des mydessecret2 engine-id 0x80001f888070939b14a514da5a00000000 inform
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set service snmp-server trap-destination \<trap-destination-id\> vrf \<vrf-name\> username \<username-id\> auth-sha \<auth-id\> encrypt-aes \<encrypt-id\></h>

Configures the trap receiver IP address and VRF for SNMPv1 and SNMPv2c traps, the SNMP username and the SHA authentication password, and the AES encryption password.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<trap-destination-id>` | The IP address of the SNMP trap destination or `localhost`.|
| `<vrf-name>` | The VRF name.|
| `<username-id>` | The SNMP username.|
| `<auth-id>` | The SHA authentication password.|
| `<encrypt-id>` | The AES encryption password.|

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv set service snmp-server trap-destination localhost vrf RED username myv3user auth-sha SHApassword1 encrypt-aes myaessecret1
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set service snmp-server trap-destination \<trap-destination-id\> vrf \<vrf-name\> username \<username-id\> auth-sha \<auth-id\> encrypt-aes \<encrypt-id\> engine-id \<engine-id\> inform</h>

Configures the SNMP trap receiver IP address and VRF for SNMPv1 and SNMPv2c traps, the SNMP username and the SHA authentication password, the AES encryption password, and the engine ID.

The SNMP trap receiving daemon must have usernames, authentication passwords, and encryption passwords created with its own EngineID. You must configure this trap server EngineID in the switch `snmpd` daemon sending the trap and inform messages.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<trap-destination-id>` | The IP address of the SNMP trap destination or `localhost`.|
| `<vrf-name>` | The VRF name.|
| `<username-id>` | The SNMP username.|
| `<auth-id>` | The SHA authentication password.|
| `<encrypt-id>` | The AES encryption password.|
| `<engine-id>` | The engine ID.|

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv set service snmp-server trap-destination localhost vrf RED username myv3user auth-sha SHApassword1 encrypt-aes myaessecret1 engine-id 0x80001f888070939b14a514da5a00000000 inform
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set service snmp-server trap-snmp-auth-failures</h>

Configures the switch to generate SNMP trap notifications for every SNMP authentication failure.

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv set service snmp-server trap-snmp-auth-failures
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set service snmp-server username \<username-id\></h>

Configures the SNMPv3 username for authentication.

NVIDIA recommends you use an SNMPv3 username and password instead of the readonly community; SNMPv3 does not expose the password in the `GetRequest` and `GetResponse` packets and can also encrypt packet contents. You can configure multiple usernames for different user roles with different levels of access to various MIBs.

{{%notice note%}}
The default snmpd.conf file contains the default `user _snmptrapusernameX`. You cannot use this username for authentication. SNMP traps require this username.
{{%/notice%}}

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<username-id>` | The SNMP username for authentication.|

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv set service snmp-server username testuser1
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set service snmp-server username \<username-id\> auth-md5 \<auth-id\></h>

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
cumulus@switch:~$ nv set service snmp-server username testuser1 auth-md5 myauthmd5password
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set service snmp-server username \<username-id\> auth-md5 \<auth-id\> encrypt-des \<encrypt-id\></h>

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
cumulus@switch:~$ nv set service snmp-server username testuser1 auth-md5 myauthmd5password encrypt-des myencryptsecret
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set service snmp-server username \<username-id\> auth-md5 \<auth-id\> encrypt-des \<encrypt-id\> oid \<oid\></h>

Configures the setting to restrict a user with a specific MD5 authentication password and DES encryption password to a particular OID tree. The OID can be either a string of decimal numbers separated by periods or a unique text string that identifies an SNMP MIB object. The MIBs that Cumulus Linux includes are in the `/usr/share/snmp/mibs/` directory. If the MIB you want to use does not install by default, you can install it with the latest Debian snmp-mibs-downloader package.

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
cumulus@switch:~$ nv set service snmp-server username testuser1 auth-md5 myauthmd5password encrypt-des myencryptsecret oid 1.3.6.1.2.1.1
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set service snmp-server username \<username-id\> auth-md5 \<auth-id\> encrypt-des \<encrypt-id\> view \<view\></h>

Configures the setting to restrict a user with a specific MD5 authentication password and DES encryption password to a defined view (subnet). Any SNMP request with that username and password must have a source IP address within the configured subnet.

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
cumulus@switch:~$ nv set service snmp-server username testuser1 auth-md5 myauthmd5password encrypt-des myencryptsecret view cumulusOnly
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set service snmp-server username \<username-id\> auth-md5 \<auth-id\> encrypt-aes \<encrypt-id\></h>

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
cumulus@switch:~$ nv set service snmp-server username testuser1 auth-md5 myauthmd5password encrypt-aes myencryptsecret
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set service snmp-server username \<username-id\> auth-md5 \<auth-id\> encrypt-aes \<encrypt-id\> oid \<oid\></h>

Configures the setting to restrict a user with a specific MD5 authentication password and AES encryption password to a particular OID tree. The OID can be either a string of decimal numbers separated by periods or a unique text string that identifies an SNMP MIB object. The MIBs that Cumulus Linux includes are in the `/usr/share/snmp/mibs/` directory. If the MIB you want to use does not install by default, you can install it with the latest Debian `snmp-mibs-downloader` package.

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
cumulus@switch:~$ nv set service snmp-server username testuser1 auth-md5 myauthmd5password encrypt-aes myencryptsecret oid 1.3.6.1.2.1.1
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set service snmp-server username \<username-id\> auth-md5 \<auth-id\> encrypt-aes \<encrypt-id\> view \<value\></h>

Configures the setting to restrict a user with a specific MD5 authentication password and AES encryption password to a defined view. Any SNMP request with that username and password must have a source IP address within the configured subnet.

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
cumulus@switch:~$ nv set service snmp-server username testuser1 auth-md5 myauthmd5password encrypt-aes myencryptsecret view cumulusOnly
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set service snmp-server username \<username-id\> auth-md5 \<auth-id\> oid \<oid\></h>

Configures SNMP to restrict a specific user with the specified password to a particular OID tree.
The OID can be either a string of decimal numbers separated by periods or a unique text string that identifies an SNMP MIB object. The MIBs that Cumulus Linux includes are in the `/usr/share/snmp/mibs/` directory. If the MIB you want to use does not install by default, you can install it with the latest Debian `snmp-mibs-downloader` package.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<username-id>` | The SNMP username for authentication.|
| `<auth-id>` | The MD5 authentication password.|
| `<oid>` | The OID tree that identifies an SNMP MIB object.|

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv set service snmp-server username testuser1 auth-md5 myauthmd5password oid 1.3.6.1.2.1
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set service snmp-server username \<username-id\> auth-md5 \<auth-id\> view \<value\></h>

Configures SNMP to restrict a specific user with the specified MD5 password to a view so that any SNMP request with that username and password must have a source IP address within the configured subnet.

You can define a specific view multiple times and fine tune to provide or restrict access using the included or excluded command to specify branches of certain MIB trees.

By default, the `snmpd.conf` file contains many views within the `systemonly` view.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<username-id>` | The SNMP username for authentication.|
| `<auth-id>` | The MD5 authentication password.|
| `<view>` | The SNMP view (subnet).|

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv set service snmp-server username testuser1 auth-md5 myauthmd5password view cumulusOnly
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set service snmp-server username \<username-id\> auth-none</h>

Configures the SNMP username to not require a password for authentication.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<username-id>` | The SNMP username for authentication.|

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv set service snmp-server username testuser1 auth-none
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set service snmp-server username \<username-id\> auth-none oid \<oid\></h>

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
cumulus@switch:~$ nv set service snmp-server username testuser1 auth-none oid 1.3.6.1.2.1
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set service snmp-server username \<username-id\> auth-none view \<view\></h>

Configures MIB tree exposure restriction. You can define a view for the SNMPv3 username and a host from a restricted subnet so that any SNMP request with that username must have a source IP address within the configured subnet.

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
cumulus@switch:~$ nv set service snmp-server username testuser1 auth-none view cumulusOnly
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set service snmp-server username \<username-id\> auth-sha \<auth-id\></h>

Configures SHA authentication for the specified SNMP user.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<username-id>` | The SNMP username for authentication.|
| `<auth-id>` | The SHA authentication password.|

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv set service snmp-server username testuser1 auth-sha SHApassword1
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set service snmp-server username \<username-id\> auth-sha \<auth-id\> encrypt-des \<encrypt-id\></h>

Configures the DES encryption password for SHA authentication for the specified SNMP user to encrypt the contents of the request and response packets.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<username-id>` | The SNMP username for authentication.|
| `<auth-id>` | The SHA authentication password.|
| `<encrypt-id>` | The DES encryption password.|

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv set service snmp-server username testuser1 auth-sha SHApassword1 encrypt-des myencryptsecret
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set service snmp-server username \<username-id\> auth-sha \<auth-id\> encrypt-des \<encrypt-id\> oid \<oid\></h>

Configures the setting to restrict a user with a specific SHA authentication password and DES encryption password to a particular OID tree. The OID can be either a string of decimal numbers separated by periods or a unique text string that identifies an SNMP MIB object. The MIBs that Cumulus Linux includes are in the `/usr/share/snmp/mibs/` directory. If the MIB you want to use does not install by default, you can install it with the latest Debian snmp-mibs-downloader package.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<username-id>` | The SNMP username for authentication.|
| `<auth-id>` | The SHA authentication password.|
| `<encrypt-id>` | The DES encryption password.|
| `<oid>` | The OID tree that identifies an SNMP MIB object.|

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv set service snmp-server username testuser1 auth-sha SHApassword1 encrypt-des myencryptsecret oid 1.3.6.1.2.1.1
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set service snmp-server username \<username-id\> auth-sha \<auth-id\> encrypt-des \<encrypt-id\> view \<value\></h>

Configures the setting to restrict a user with a specific SHA authentication password and DES encryption password to a defined view (subnet). Any SNMP request with that username and password must have a source IP address within the configured subnet.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<username-id>` | The SNMP username for authentication.|
| `<auth-id>` | The SHA authentication password.|
| `<encrypt-id>` | The DES encryption password.|
| `<view>` | The SNMP view (subnet).|

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv set service snmp-server username testuser1 auth-sha SHApassword1 encrypt-des myencryptsecret view cumulusOnly
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set service snmp-server username \<username-id\> auth-sha \<auth-id\> encrypt-aes \<encrypt-id\></h>

Configures the AES encryption password for SHA authentication for the specified SNMP user to encrypt the contents of the request and response packets.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<username-id>` | The SNMP username for authentication.|
| `<auth-id>` | The SHA authentication password.|
| `<encrypt-id>` | The AES encryption password.|

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv set service snmp-server username testuser1 auth-sha SHApassword1 encrypt-aes myencryptsecret
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set service snmp-server username \<username-id\> auth-sha \<auth-id\> encrypt-aes \<encrypt-id\> oid \<oid\></h>

Configures SNMP to restrict a user with a specific SHA authentication password and AES encryption password to a particular OID tree. The OID can be either a string of decimal numbers separated by periods or a unique text string that identifies an SNMP MIB object. The MIBs that Cumulus Linux includes are in the `/usr/share/snmp/mibs/` directory. If the MIB you want to use does not install by default, you can install it with the latest Debian `snmp-mibs-downloader` package.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<username-id>` | The SNMP username for authentication.|
| `<auth-id>` | The SHA authentication password.|
| `<encrypt-id>` | The AES encryption password.|
| `<oid>` | The OID tree that identifies an SNMP MIB object.|

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv set service snmp-server username testuser1 auth-sha SHApassword1 encrypt-aes myencryptsecret oid 1.3.6.1.2.1.1
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set service snmp-server username \<username-id\> auth-sha \<auth-id\> encrypt-aes \<encrypt-id\> view \<value\></h>

Configures SNMP to restrict a user with a specific SHA authentication password and AES encryption password to a defined view (subnet). Any SNMP request with that username and password must have a source IP address within the configured subnet.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<username-id>` | The SNMP username for authentication.|
| `<auth-id>` | The SHA authentication password.|
| `<encrypt-id>` | The AES encryption password.|
| `<view>` | The SNMP view (subnet).|

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv set service snmp-server username testuser1 auth-sha SHApassword1 encrypt-aes myencryptsecret view cumulusOnly
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set service snmp-server username \<username-id\> auth-sha \<auth-id\> oid \<oid\></h>

Configures SNMP to restrict a specific user with the specified SHA authentication password to a particular OID tree.
The OID can be either a string of decimal numbers separated by periods or a unique text string that identifies an SNMP MIB object. The MIBs that Cumulus Linux includes are in the `/usr/share/snmp/mibs/` directory. If the MIB you want to use does not install by default, you can install it with the latest Debian `snmp-mibs-downloader` package.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<username-id>` | The SNMP username for authentication.|
| `<auth-id>` | The SHA authentication password.|
| `<oid>` | The OID tree that identifies an SNMP MIB object.|

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv set service snmp-server username testuser1 auth-sha SHApassword1 oid 1.3.6.1.2.1
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set service snmp-server username \<username-id\> auth-sha \<auth-id\> view \<value\></h>

Configures SNMP to restrict a specific user with the specified SHA authentication password to a particular SNMP view (subnet) so that any SNMP request with that username and SHA authentication password must have a source IP address within the configured subnet.

You can define a specific view multiple times and fine tune to provide or restrict access using the included or excluded command to specify branches of certain MIB trees.

By default, the `snmpd.conf` file contains many views within the `systemonly` view.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<username-id>` | The SNMP username for authentication.|
| `<auth-id>` | The SHA authentication password.|
| `<view>` | The SNMP view (subnet).|

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv set service snmp-server username testuser1 auth-sha SHApassword1 view cumulusOnly
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set service snmp-server viewname \<viewname-id\></h>

Configures the view names that restrict MIB tree exposure.

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set service snmp-server viewname \<viewname-id\> excluded \<snmp-branch\></h>

Configures the SNMP tree branches to exclude.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<viewname-id>` | The SNMP view (subnet) name.|
| `<snmp-branch>` | SNMP tree branch to exclude.|

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv set service snmp-server viewname cumulusOnly excluded .1.3.6.1.4.1.40310
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set service snmp-server viewname \<viewname-id\> included \<snmp-branch\></h>

Configures the SNMP tree branches to include.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<viewname-id>` | The SNMP view (subnet) name.|
| `<snmp-branch>` | SNMP tree branch to include.|

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv set service snmp-server viewname cumulusOnly included .1.3.6.1.4.1.40310.2
```
