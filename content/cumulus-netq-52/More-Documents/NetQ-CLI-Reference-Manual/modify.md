---
title: modify
author: NVIDIA
weight: 1105
toc: 3
right_toc_levels: 1
pdfhidden: true
type: nojsscroll
---
<!-- vale NVIDIA.HeadingTitles = NO -->
<!-- vale off -->
## netq modify otlp endpoint
<!-- vale on -->

Use this command to change the OTel endpoint of your time-series database (TSDB).

### Syntax

```
netq modify otlp endpoint tsdb-name <text-tsdb-endpoint> 
    [tsdb-url <text-tsdb-endpoint-url>] 
    [export true | export false] 
    [security-mode <text-mode>]
    [whitelist_enabled true | whitelist_enabled false]
```

### Required Arguments

| Argument | Value | Description |
| ---- | ---- | ---- |
| tsdb-name | \<text-tsdb-endpoint\> | Specify the name of your TSDB |

### Options

| Option | Value | Description |
| ---- | ---- | ---- |
| tsdb-url | \<text-tsdb-endpoint-url\> | Specify the URL of your TSDB |
| export | true, false | Begin exporting data immediately (true) or not (false) |
| security-mode | \<text-mode\> | Set the security mode to `tls` (for TLS) or `insecure` |
| whitelist_enabled | true, false | Enables (true) or disables (false) OTLP whitelist on the TSDB|

### Related Commands

- `netq set oltp endpoint`
- `netq show oltp endpoints`

