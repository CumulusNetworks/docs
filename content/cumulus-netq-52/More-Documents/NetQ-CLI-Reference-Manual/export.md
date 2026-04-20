---
title: export
author: NVIDIA
weight: 1103
toc: 3
right_toc_levels: 1
pdfhidden: true
type: nojsscroll
---

## netq export otlp ca-cert
<
Exports the CA certificate of your time-series database.

### Syntax

```
netq export otlp ca-cert 
    [dump | save <text-path-to-ca-cert-save-file>]
```

### Options

| Option | Value | Description |
| ---- | ---- | ---- |
| NA | dump, save | Display the certificate as a dump file or save the certificate to the specified path |

### Options

None

### Related Commands

- `netq import otlp ca-cert`
- - -

## netq export otlp ca-key

Exports the CA certificate key of your time-series database.

### Syntax

```
netq export otlp ca-key 
    [dump | save <text-path-to-ca-key-save-file>] 
```

### Options

| Option | Value | Description |
| ---- | ---- | ---- |
| NA | dump, save | Display the key as a dump file or save the key to the specified path |

### Options

None

### Related Commands

- `netq import otlp ca-key`
- - -