---
title: set
author: NVIDIA
weight: 1105
toc: 3
right_toc_levels: 1
pdfhidden: true
type: nojsscroll
---
<!-- vale NVIDIA.HeadingTitles = NO -->
<!-- vale off -->
## netq set otlp endpoint-ca-cert
<!-- vale on -->
Sets the CA certificate of your time-series database; used together with the `netq add otlp endpoint` command.

### Syntax

```
netq set otlp endpoint-ca-cert 
    tsdb-name <text-tsdb-endpoint> 
    ca-cert <text-path-to-ca-crt>
```

### Required Arguments

| Argument | Value | Description |
| ---- | ---- | ---- |
| tsdb-name | \<text-tsdb-endpoint\> | Specify the name of your TSDB |
| ca-cert | \<text-path-to-ca-crt\> | Specify the path to the CA certificate|

### Options

None

### Related Commands

- `netq add otlp endpoint`

- - -

## netq set otlp security-mode

Sets the OTLP security mode.

### Syntax

```
netq set otlp security-mode <text-mode>
```

### Required Arguments

| Argument | Value | Description |
| ---- | ---- | ---- |
| security-mode | \<text-mode\> |  Enable TLS (`tls`) or disable (`insecure`) the OTLP security mode |

### Options

None

### Related Commands

None

- - -

## netq set otlp tls-cert

Configures the server certificate (`server.crt`) and server key (`server.key`) on the NetQ server.

### Syntax

```
netq set otlp tls-cert 
    server-crt <text-path-to-server-crt> 
    server-key <text-path-to-server-key>
```

### Required Arguments

| Argument | Value | Description |
| ---- | ---- | ---- |
| server-crt | \<text-path-to-server-crt\> | Specify path to the server certificate |
| server-key | \<text-path-to-server-key\> | Specify path to the server key |

### Options

None

### Related Commands

None

- - -
<!--
## netq set otlp whitelist

Use this command to add and update the whitelist ConfigMap for an external time-series database. Executing the command automatically triggers a rolling restart of the OTLP pods and will not cause downtime. You can view the contents of the whitelist using the `netq show whitelist custom` command.

### Syntax

```
netq set otlp 
    whitelist file <path-to-yaml-file> 
    tsdb-name <tsdb-name>
```

### Required Arguments

| Argument | Value | Description |
| ---- | ---- | ---- |
| whitelist file | \<path-to-yaml-file\> | Specify the path to the YAML file |
| tsdb-name | \<tsdb-name\> | Specify the name of the time-series database |

### Options

None

### Sample Usage

```
netq set otlp whitelist file /home/nvidia/custom.yaml tsdb-name external-vm
```

### Related Commands

- `netq show otlp whitelist`

-->