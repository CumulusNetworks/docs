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
| ca-cert | \<text-path-to-ca-crt\> | |

### Options

None

### Related Commands

None

- - -

## netq set otlp security-mode

### Syntax

```
netq set otlp security-mode <text-mode>
```

### Required Arguments

| Argument | Value | Description |
| ---- | ---- | ---- |
| security-mode | \<text-mode\> |  |

### Options

None

### Related Commands

None

- - -

## netq set otlp tls-cert

### Syntax

```
netq set otlp tls-cert 
    server-crt <text-path-to-server-crt> 
    server-key <text-path-to-server-key>
```

### Required Arguments

| Argument | Value | Description |
| ---- | ---- | ---- |
| server-crt | \<text-path-to-server-crt\> | |
| server-key | \<text-path-to-server-key\> | |