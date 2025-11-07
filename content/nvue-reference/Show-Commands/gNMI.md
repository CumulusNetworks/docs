---
title: gNMI
author: Cumulus Networks
weight: 180

type: nojsscroll
---
<style>
h { color: RGB(118,185,0)}
</style>
<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system gnmi-server</h>

Shows the gNMI server configuration.

### Version History

Introduced in Cumulus Linux 5.13.0

### Example

```
cumulus@switch:~$ nv show system gnmi-server
                                  operational  applied    
--------------------------------  -----------  -----------
state                             disabled     enabled    
certificate                       self-signed  self-signed
port                              9339         9339       
[listening-address]               10.1.1.100   10.1.1.100 
[listening-address]               localhost    localhost  
mtls                                                      
  ca-certificate                  CACERT       CACERT     
version                                                   
status                                                    
  total-active-subscriptions      0                       
  received-subscription-requests  0                       
  rejected-subscriptions          0                       
  received-capabilities-requests  0                       
  [client]
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system gnmi-server listening-address</h>

Shows the external gNMI REST API listening addresses.

### Version History

Introduced in Cumulus Linux 5.13.0

### Example

```
cumulus@switch:~$ nv show system gnmi-server listening-address
----------
10.1.1.100
localhost
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system gnmi-server listening-address <listening-address-id></h>

Shows information about the specified gNMI server listening address.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<listening-address-id>` | The listening address. |

### Version History

Introduced in Cumulus Linux 5.13.0

### Example

```
cumulus@switch:~$ nv show system gnmi-server listening-address 10.1.1.100
No Data
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system gnmi-server mtls</h>

Shows mTLS information.

### Version History

Introduced in Cumulus Linux 5.13.0

### Example

```
cumulus@switch:~$ nv show system gnmi-server mtls
               operational  applied
--------------  -----------  -------
ca-certificate  CACERT       CACERT
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system gnmi-server status</h>

Shows gNMI server information such as the total number of active subscriptions, the number of received subscription requests, rejected subscriptions, and the number of received capabilities requests.

### Version History

Introduced in Cumulus Linux 5.13.0

### Example

```
cumulus@switch:~$ nv show system gnmi-server status
                                operational
------------------------------  -----------
total-active-subscriptions      0          
received-subscription-requests  0          
rejected-subscriptions          0          
received-capabilities-requests  0
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system gnmi-server status client</h>

Shows the gNMI server client status information.

### Version History

Introduced in Cumulus Linux 5.13.0

### Example

```
cumulus@switch:~$ nv show system gnmi-server status client
No Data
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system gnmi-server status client <client-address-id></h>

Shows status information for the specified gNMI server client.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<client-address-id>` | The client listening address. |

### Version History

Introduced in Cumulus Linux 5.13.0

### Example

```
cumulus@switch:~$ nv show system gnmi-server status client 10.1.1.10
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system gnmi-server status gnoi-rpc</h>

Shows the number of gNOI RPCs received on the switch.

### Version History

Introduced in Cumulus Linux 5.15.0

### Example

```
cumulus@switch:~$ nv show system gnmi-server status gnoi-rpc
gnoi-rpc-name failed-rpc-requests received-rpc-requests
------------- ------------------- ---------------------
File.Get      0                   4
File.Put      0                   1
File.Remove   0                   1
File.Stat     0                   46
OS.Install    0                   1
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system grpc-tunnel</h>

Shows the gRCP-tunnel servers configured on the switch.

### Version History

Introduced in Cumulus Linux 5.13.0

### Example

```
cumulus@switch:~$ nv show system grpc-tunnel
          operational  applied
--------  -----------  -------
[server]  SERVER1      SERVER1
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system grpc-tunnel server</h>

Shows gRCP-tunnel server configuration.

### Version History

Introduced in Cumulus Linux 5.13.0

### Example

```
cumulus@switch:~$ nv show system grpc-tunnel server
         Address    ca-certificate  Certificate  Port  Retry Interval  State     status.connection.established  status.connection.register  status.connection.tunnel  status.local-address  status.local-port  status.remote-address  status.remote-port  Target Name  Target Type
-------  ---------  --------------  -----------  ----  --------------  --------  -----------------------------  --------------------------  ------------------------  --------------------  -----------------  ---------------------  ------------------  -----------  -----------
SERVER1  10.1.1.10  CERT1                        443   30              disabled  1970-01-01T00:00:00Z           no                          no                        None                  0                  None                   0                   TARGET1      gnmi-gnoi 
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system grpc-tunnel server <server-name-id></h>

Shows configuration and status information for the specified gRCP-tunnel server.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<server-name-id>` | The gRCP-tunnel server ID. |

### Version History

Introduced in Cumulus Linux 5.13.0

### Example

```
cumulus@switch:~$ nv show system grpc-tunnel server SERVER1
                operational           applied  
---------------  --------------------  ---------
state            disabled              enabled  
target-name      TARGET1               TARGET1  
address          10.1.1.10             10.1.1.10
port             443                   443      
ca-certificate   CERT1                 CERT1    
target-type      gnmi-gnoi             gnmi-gnoi
retry-interval   30                    30       
status                                          
  local-port     0                              
  remote-port    0                              
  connection                                    
    established  1970-01-01T00:00:00Z           
    register     no                             
    tunnel       no 
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system grpc-tunnel server <server-name-id> status</h>

Shows status information for the specified gRCP-tunnel server.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<server-name-id>` | The gRCP-tunnel server ID. |

### Version History

Introduced in Cumulus Linux 5.13.0

### Example

```
cumulus@switch:~$ nv show system grpc-tunnel server SERVER1 status
               operational         
-------------  --------------------
local-port     0                   
remote-port    0                   
connection                         
  established  1970-01-01T00:00:00Z
  register     no                  
  tunnel       no
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system grpc-tunnel server <server-name-id> status connection</h>

Shows the connection status for the specified gRCP-tunnel server.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<server-name-id>` | The gRCP-tunnel server ID. |

### Version History

Introduced in Cumulus Linux 5.13.0

### Example

```
cumulus@switch:~$ nv show system grpc-tunnel server SERVER1 status connection
             operational         
-----------  --------------------
established  1970-01-01T00:00:00Z
register     no                  
tunnel       no
```
