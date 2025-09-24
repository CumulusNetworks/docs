---
title: gNMI
author: Cumulus Networks
weight: 567

type: nojsscroll
---
<style>
h { color: RGB(118,185,0)}
</style>
{{%notice note%}}
The `nv unset` commands remove the configuration you set with the equivalent `nv set` commands. This guide only describes an `nv unset` command if it differs from the `nv set` command.
{{%/notice%}}

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system gnmi-server mtls ca-certificate \<ca-cert-id\></h>

Sets the CA certificate you want to use to validate the client during mTLS.

## Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<ca-cert-id>` |  The CA-certificate ID. |

### Version History

Introduced in Cumulus Linux 5.13.0

### Example

```
cumulus@switch:~$ nv set system gnmi-server mtls ca-certificate CERT
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system gnmi-server mtls crl \<crl\></h>

Sets the <span class="a-tooltip">[CRL](## "Certificate Revocation List")</span> you want to use to validate the client during mTLS.

## Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<crl>` |  The Certificate Revocation List. |

### Version History

Introduced in Cumulus Linux 5.13.0

### Example

```
cumulus@switch:~$ nv set system gnmi-server mtls crl abcdefghijklmnop
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system gnmi-server certificate \<cert-id\></h>

Binds the certificate to the gNMI server when you configure the gRPC tunnel client package.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<cert-id>` |  The certificate ID. |

### Version History

Introduced in Cumulus Linux 5.13.0

### Example

```
cumulus@switch:~$ nv set system gnmi-server certificate CERT1
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system gnmi-server listening-address \<address\></h>

Sets the listening address for the gNMI server.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<address>` |  The gNMI server listening address. |

### Version History

Introduced in Cumulus Linux 5.13.0

### Example

```
cumulus@switch:~$ nv set system gnmi-server listening-address localhost
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system gnmi-server port \<port-id\></h>

Sets the gNMI server listening port.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<port-id>` |  The port number. |

### Version History

Introduced in Cumulus Linux 5.13.0

### Example

```
cumulus@switch:~$ nv set system gnmi-server port 9339
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system gnmi-server state</h>

Enables and disables the gNMI server. You can specify `enabled` or `disabled`.

### Version History

Introduced in Cumulus Linux 5.13.0

### Example

```
cumulus@switch:~$ nv set system gnmi-server state enabled
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system grpc-tunnel server \<server-id\> address \<address\></h>

Configures the IP address of the gRPC tunnel server to which you want to connect.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<server-id>` |  The gRPC tunnel server ID. |
| `<address>` |  The IP address or hostname of the gRPC tunnel server. |

### Version History

Introduced in Cumulus Linux 5.13.0

### Example

```
cumulus@switch:~$ nv set system grpc-tunnel server SERVER1 address 10.1.1.10 
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system grpc-tunnel server \<server\> ca-certificate \<ca-cert-id\></h>

Sets the CA certificate you want to use for the gRPC tunnel server.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<server-id>` |  The gRPC tunnel server ID. |
| `<ca-cert-id>` |  The CA-certificate ID for the gRPC tunnel server. |

### Version History

Introduced in Cumulus Linux 5.13.0

### Example

```
cumulus@switch:~$ nv set system grpc-tunnel server SERVER1 ca-certificate CERT1
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system grpc-tunnel server \<server\> certificate self-signed</h>

Configures the self-signed certificate you want to use for the gRPC tunnel server.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<server-id>` |  The gRPC tunnel server ID. |

### Version History

Introduced in Cumulus Linux 5.13.0

### Example

```
cumulus@switch:~$ nv set system grpc-tunnel server SERVER1 certificate self-signed
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system grpc-tunnel server \<server\> port</h>

Configures the port number for the gRPC tunnel server to which you want to connect.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<server-id>` |  The gRPC tunnel server ID. |
| `<port>` |  The gRPC tunnel server port. |

### Version History

Introduced in Cumulus Linux 5.13.0

### Example

```
cumulus@switch:~$ nv set system grpc-tunnel server SERVER1 port 443
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system grpc-tunnel server \<server\> retry-interval</h>

Configures the retry interval for grpc tunnel. You can specify a value between 10 and 300, The default value is 30.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<server-id>` |  The gRPC tunnel server ID. |

### Version History

Introduced in Cumulus Linux 5.13.0

### Example

```
cumulus@switch:~$ nv set system grpc-tunnel server SERVER1 retry-interval 20
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system grpc-tunnel server \<server\> target-name \<target-name\></h>

Configures the target name for the gRPC tunnel server to which you want to connect.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<server-id>` |  The gRPC tunnel server ID. |
| `<target-name>` |  The gRPC tunnel server target name. |

### Version History

Introduced in Cumulus Linux 5.13.0

### Example

```
cumulus@switch:~$ nv set system grpc-tunnel server SERVER1 target-name TARGET1
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system grpc-tunnel server \<server\> target-type \<target-type\></h>

Configures the target type for the gRPC tunnel server to which you want to connect.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<server-id>` |  The gRPC tunnel server ID. |
| `<target-type>` |  The gRPC tunnel server target type. |

### Version History

Introduced in Cumulus Linux 5.13.0

### Example

```
cumulus@switch:~$ nv set system grpc-tunnel server SERVER1 target-type gnmi-gnoi
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system grpc-tunnel server \<server\> state</h>

Enables and disables the gRPC tunnel server.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<server-id>` |  The gRPC tunnel server ID. |

### Version History

Introduced in Cumulus Linux 5.13.0

### Example

```
cumulus@switch:~$ nv set system grpc-tunnel server SERVER1 state enabled
```
