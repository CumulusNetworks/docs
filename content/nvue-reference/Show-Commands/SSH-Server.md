---
title: SSH Server
author: Cumulus Networks
weight: 365
type: nojsscroll
---
<style>
h { color: RGB(118,185,0)}
</style>
<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system ssh-server</h>

Shows SSH server configuration on the switch.

### Version History

Introduced in Cumulus Linux 5.6.0

### Example

```
cumulus@switch:~$ nv show system ssh-server
                             applied          
---------------------------  -----------------
authentication-retries       6                
inactive-timeout             0                
login-timeout                120              
max-sessions-per-connection  10               
permit-root-login            prohibit-password
state                        enabled          
max-unauthenticated                           
  session-count              100              
  throttle-percent           30               
  throttle-start             10  
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system ssh-server max-unauthenticated</h>

Shows the number of unauthenticated SSH sessions allowed before throttling starts, the starting percentage of connections to reject above the throttle start count before reaching the session count limit, and the maximum number of unauthenticated SSH sessions allowed.

### Version History

Introduced in Cumulus Linux 5.6.0

### Example

```
cumulus@switch:~$ nv show system ssh-server max-unauthenticated
                  applied
----------------  -------
session-count     100    
throttle-percent  30     
throttle-start    10 
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system ssh-server vrf</h>

Shows the VRFs that allow SSH sessions.

### Version History

Introduced in Cumulus Linux 5.6.0

### Example

```
cumulus@switch:~$ nv show system ssh-server vrf
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system ssh-server vrf \<vrf-id\></h>

Shows SSH session information for a specific VRF.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |  The VRF name.|

### Version History

Introduced in Cumulus Linux 5.6.0

### Example

```
cumulus@switch:~$ nv show system ssh-server vrf RED
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system ssh-server allow-users</h>

Shows the users that are allowed to establish an SSH session.

### Version History

Introduced in Cumulus Linux 5.6.0

### Example

```
cumulus@switch:~$ nv show system ssh-server allow-users
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system ssh-server allow-users \<user-id\></h>

Shows session information for a specific user allowed to establish an SSH session.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<user-id>` |  The user account name.|

### Version History

Introduced in Cumulus Linux 5.6.0

### Example

```
cumulus@switch:~$ nv show system ssh-server allow-users user1
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system ssh-server deny-users</h>

Shows the users that are **not** allowed to establish an SSH session.

### Version History

Introduced in Cumulus Linux 5.6.0

### Example

```
cumulus@switch:~$ nv show system ssh-server deny-users
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system ssh-server deny-users \<user-id\></h>

Shows information for a specific user **not** allowed to establish an SSH session.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<user-id>` |  The user account name.|

### Version History

Introduced in Cumulus Linux 5.6.0

### Example

```
cumulus@switch:~$ nv show system ssh-server deny-users user3
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system ssh-server port</h>

Shows TCP port numbers that listen for incoming SSH sessions.

### Version History

Introduced in Cumulus Linux 5.6.0

### Example

```
cumulus@switch:~$ nv show system ssh-server port
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system ssh-server port \<port-id\></h>

Shows information about a TCP port number that listens for incoming SSH sessions.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<port-id>` |  The port number.|

### Version History

Introduced in Cumulus Linux 5.6.0

### Example

```
cumulus@switch:~$ nv show system ssh-server port 443
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system ssh-server active-sessions</h>

Shows the current number of active SSH sessions on the switch.

### Version History

Introduced in Cumulus Linux 5.6.0

### Example

```
cumulus@switch:~$ nv show system ssh-server active-sessions
Peer Address:Port    Local Address:Port      State
-------------------  ----------------------  -----
192.168.200.1:46528  192.168.200.11%mgmt:22  ESTAB
```
