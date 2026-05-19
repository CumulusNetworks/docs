---
title: DNS
author: Cumulus Networks
weight: 160

type: nojsscroll
---
<style>
h { color: RGB(118,185,0)}
</style>

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show service dns</h>

Shows <span class="a-tooltip">[DNS](## "Domain Name Service")</span> information.

{{%notice note%}}
In Cumulus Linux 5.15 and later, this command is `nv show system dns`.
{{%/notice%}}

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show service dns
          operational   
--------  ------------- 
domain    simulation                     
[server]  192.168.200.1                  
[search]  simulation
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show service dns \<vrf-id\></h>

Shows <span class="a-tooltip">[DNS](## "Domain Name Service")</span> configuration settings for the specified VRF.

{{%notice note%}}
Cumulus Linux 5.15 and later no longer supports this command.
{{%/notice%}}

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show service dns default
          operational  applied   
--------  -----------  ----------
[search]               nvidia.com
[server]               192.0.2.44
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show service dns \<vrf-id\> server</h>

Shows the remote DNS servers.

{{%notice note%}}
In Cumulus Linux 5.15 and later, this command is `nv show system dns server`.
{{%/notice%}}

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show service dns default server
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show service dns \<vrf-id\> server \<dns-server-id\></h>

Shows information about the specified remote DNS server.

{{%notice note%}}
In Cumulus Linux 5.15 and later, this command is `nv show system dns server <dns-server-id>`.
{{%/notice%}}

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<dns-server-id>` | The IPv4 or IPv6 address of a DNS server. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show service dns default server 192.0.2.44
     operational
---  -----------
vrf  mgmt 
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system dns</h>

Shows <span class="a-tooltip">[DNS](## "Domain Name Service")</span> information.

{{%notice note%}}
In Cumulus Linux 5.14 and earlier, this command is `nv show service dns`.
{{%/notice%}}

### Version History

Introduced in Cumulus Linux 5.15.0

### Example

```
cumulus@switch:~$ nv show system dns
          operational   
--------  ------------- 
domain    simulation                     
[server]  192.168.200.1                  
[search]  simulation
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system dns server</h>

Shows the remote DNS servers.

{{%notice note%}}
In Cumulus Linux 5.14 and earlier, this command is `nv show service dns <vrf-id> server`.
{{%/notice%}}

### Version History

Introduced in Cumulus Linux 5.15.0

### Example

```
cumulus@switch:~$ nv show system dns server
DNS Server     priority  VRF 
-------------  --------  ----
192.168.200.1            mgmt
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system dns server \<dns-server-id\></h>

Shows information about the specified remote DNS server.

{{%notice note%}}
In Cumulus Linux 5.14 and earlier, this command is `nv show service dns <vrf-id> server <dns-server-id>`.
{{%/notice%}}

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<dns-server-id>` | The IPv4 or IPv6 address of a DNS server. |

### Version History

Introduced in Cumulus Linux 5.15.0

### Example

```
cumulus@switch:~$ nv show system dns server 192.0.2.44
     operational
---  -----------
vrf  mgmt 
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system dns search</h>

Shows the DNS search IDs and priorities.

### Version History

Introduced in Cumulus Linux 5.15.0

### Example

```
cumulus@switch:~$ nv show system dns search
DNS Search id  priority
-------------  --------
simulation 
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system dns search \<dns-search-id\></h>

Shows the information about the DNS search ID.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<dns-search-id>` | The DNS search ID. |

### Version History

Introduced in Cumulus Linux 5.15.0

### Example

```
cumulus@switch:~$ nv show system dns search simulation
no data 
```
