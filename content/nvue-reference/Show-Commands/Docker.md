---
title: Docker
author: Cumulus Networks
weight: 165

type: nojsscroll
---
<style>
h { color: RGB(118,185,0)}
</style>

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system docker</h>

Shows information about Docker in Cumulus Linux.

### Version History

Introduced in Cumulus Linux 5.15.0

### Example

```
cumulus@switch:~$ nv show system docker
       operational  applied
-----  -----------  -------
vrf    mgmt         mgmt   
state  enabled      enabled

Docker Containers
====================
    Container Name      Image                            Container ID  Status               Ports  Summary
    ------------------  -------------------------------  ------------  -------------------  -----  -------             
    what-just-happened  docker-wjh:latest                f834edf7fd3c  Up 6 days 
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system docker container</h>

Shows all containers and their status, including stopped containers.

### Version History

Introduced in Cumulus Linux 5.15.0

### Example

```
cumulus@switch:~$ nv show system docker container
Container Name      Image                            Container ID  Status               Ports  Summary
------------------  -------------------------------  ------------  -------------------  -----  -------
repo                cumulus-linux-apt-mirror:5.15.0  container1  Up 6 days (healthy)                
what-just-happened  docker-wjh:latest                container2  Up 7 days
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system docker container \<container-id\></h>

Shows details for a specific container.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<container-id>` | The container name. |

### Version History

Introduced in Cumulus Linux 5.15.0

### Example

```
cumulus@switch:~$ nv show system docker container repo
               operational                    
-------------  -------------------------------
id             f834edf7fd3c                   
status         Up 6 days (healthy)            
image-name     cumulus-linux-apt-mirror:5.15.0
port                                          
stats                                         
  cpu          0.00%                          
  mem-usage    8.105MiB                       
  mem-limit    15.02GiB                       
  mem-percent  0.05%                          
  net-io       0B / 0B                        
  block-io     160kB / 41kB                   
  pids         9
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system docker container \<container-id\> stats</h>

Shows statistics for a specific container.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<container-id>` | The container name or hexadecimal string. |

### Version History

Introduced in Cumulus Linux 5.15.0

### Example

```
cumulus@switch:~$ nv show system docker container repo stats 
             operational 
-----------  ------------
cpu          0.00%       
mem-usage    8.102MiB    
mem-limit    15.02GiB    
mem-percent  0.05%       
net-io       0B / 0B     
block-io     160kB / 41kB
pids         9
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system docker container stats</h>

Shows statistics for all containers.

### Version History

Introduced in Cumulus Linux 5.13.0

### Example

```
cumulus@switch:~$ nv show system docker container stats
Container Name      CPU%   MEM USAGE  MEM LIMIT  MEM%   NET I/O  BLOCK I/O       PIDS
------------------  -----  ---------  ---------  -----  -------  --------------  ----
repo                0.00%  8.102MiB   15.02GiB   0.05%  0B / 0B  160kB / 41kB    9   
what-just-happened  0.05%  81.96MiB   15.02GiB   0.53%  0B / 0B  496kB / 16.4kB  9
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system docker engine</h>

Shows docker engine configuration.

### Version History

Introduced in Cumulus Linux 5.13.0

### Example

```
cumulus@switch:~$ nv show system docker engine
                operational                                                                                    
--------------  -----------------------------------------------------------------------------------------------
client                                                                                                         
  name          Docker Engine - Community                                                                      
  version       28.5.1                                                                                         
  context       default                                                                                        
server                                                                                                         
  containers    2                                                                                              
  running       2                                                                                              
  paused        0                                                                                              
  stopped       0                                                                                              
plugins                                                                                                        
  volume        ['local']                                                                                      
  network       ['bridge', 'host', 'ipvlan', 'macvlan', 'null', 'overlay']                                     
  log           ['awslogs', 'fluentd', 'gcplogs', 'gelf', 'journald', 'json-file', 'local', 'splunk', 'syslog']
images          2                                                                                              
server-version  28.5.1                                                                                         
id              ae4be5b9-6806-435d-80cb-5e4548a9c11a                                                           
init-binary     docker-init                                                                                    
data-root       /docker                                                                                        
debug-mode      False                                                                                          
log-level       json-file
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system docker image</h>

Shows the docker images present on the switch.

### Version History

Introduced in Cumulus Linux 5.13.0

### Example

```
cumulus@switch:~$ nv show system docker image
Image Id      Image Name                Tag     Size    Date                           Summary
------------  ------------------------  ------  ------  -----------------------------  -------
283e2bf92e80  docker-wjh                latest  716MB   2025-10-29 21:47:09 -0400 EDT         
d839322a5483  cumulus-linux-apt-mirror  5.15.0  3.47GB  2025-10-30 02:35:30 -0400 EDT 
```
