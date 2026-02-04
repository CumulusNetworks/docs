---
title: API
author: Cumulus Networks
weight: 515

type: nojsscroll
---
<style>
h { color: RGB(118,185,0)}
</style>
{{%notice note%}}
The `nv unset` commands remove the configuration you set with the equivalent `nv set` commands. This guide only describes an `nv unset` command if it differs from the `nv set` command.
{{%/notice%}}

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system api certificate \<certificate-string\></h>

Configures the X.509 certificate to be used with the API end-point.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `certificate-string` | The certificate string. |

### Version History

Introduced in Cumulus Linux 5.8.0

### Example

```
cumulus@switch:~$ nv set system api certificate <string>
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system api compression gzip</h>

Enables and disables compression of HTTP responses for client requests with the Content-Encoding: gzip header to reduce data size and improve performance. When accessing the API over slow network connections or retrieving large datasets, response times can be significant.

HTTP response compression is disabled by default.

### Version History

Introduced in Cumulus Linux 5.16.0

### Example

```
cumulus@switch:~$ nv set system api compression gzip
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system api listening-address \<listening-address-id\></h>

Configures the NVUE REST API listening address; you can specify an IPv4 address or localhost. If you do not specify a listening address, NGINX listens on all addresses for the target port.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `listening-address-id` | The IP address of the API listening address, or localhost. |

### Version History

Introduced in Cumulus Linux 5.6.0

### Example

```
cumulus@switch:~$ nv set system api listening-address localhost
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system api mtls ca-certificate \<certificate-string\></h>

Configures the certificate for client validation during Mutual TLS (mTLS) authentication.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `certificate-string` | The certificate string. |

### Version History

Introduced in Cumulus Linux 5.8.0

### Example

```
cumulus@switch:~$ nv set system api mtls ca-certificate <string>
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system api port</h>

Configures the NVUE REST API port. You can set a value between 1 and 65535. If you do not set a port, Cumulus Linux uses the default port 8765.

### Version History

Introduced in Cumulus Linux 5.6.0

### Example

```
cumulus@switch:~$ nv set system api port 8888
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system api state</h>

Enables or disables the NVUE REST API. The default setting is `enabled`.

{{%notice note%}}
To use the NVUE REST API in Cumulus Linux 5.6, you must change the password for the cumulus user; otherwise you see 403 responses when you run commands.
{{%/notice%}}

### Version History

Introduced in Cumulus Linux 5.6.0

### Example

```
cumulus@switch:~$ nv set system api state enabled
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system api token-expiration</h>

Configures the JWT-based authentication token expiration time in minutes. You can set a value between 0 and 10080 minutes. The default value is 60 minutes. If set the expiration time to 0, Cumulus Linux does not issue a token and all previously issued tokens do not work.

### Version History

Introduced in Cumulus Linux 5.14.0

### Example

```
cumulus@switch:~$ nv set system api token-expiration 1000
```
