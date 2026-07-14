---
title: import
author: NVIDIA
weight: 1103
toc: 3
right_toc_levels: 1
pdfhidden: true
type: nojsscroll
---

## netq import otlp ca-cert

Imports the CA certificate of your time-series database.

### Syntax

```
netq import otlp ca-cert <text-ca-cert-b64> 
```

### Required Arguments

| Argument | Value | Description |
| ---- | ---- | ---- |
| ca-cert | \<text-ca-cert-b64\> | base64 output  |

### Options

None

### Related Commands

- `netq export otlp ca-cert`
- - -

## netq import otlp ca-key

Imports the CA key of your time-series database.

### Syntax

```
netq import otlp ca-key <text-ca-key-b64> 
```

### Required Arguments

| Argument | Value | Description |
| ---- | ---- | ---- |
| ca-key | \<text-ca-cert-b64\> | base64 output  |

### Options

None

### Related Commands

- `netq export otlp ca-key`
- - -
<!--
## netq import otlp keypair


### Syntax

```
netq import otlp keypair 
    ca-cert <text-ca-cert-file-path> 
    ca-key <text-ca-key-file-path> 
```

### Required Arguments

| Argument | Value | Description |
| ---- | ---- | ---- |
| ca-cert | \<text-ca-cert-file-path\> | Full path to CA certificate  |
| ca-key | \<text-ca-key-file-path\> | Full path to CA key  |

### Options

None

### Related Commands

- `netq export otlp ca-key`

-->