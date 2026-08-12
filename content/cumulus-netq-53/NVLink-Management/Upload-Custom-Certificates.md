---
title: Upload Custom Certificates
author: NVIDIA
weight: 260
toc: 4
---

NetQ NVLink supports two types of certificates: self-signed or custom. Self-signed certificates are auto-generated during the NetQ NVLink installation process and require no further action. If you specified a custom certificate in the JSON template during the initial installation, follow the steps on this page to upload the certificates. 

## Prerequisites

- The JSON configuration file used to {{<link title="Install NetQ NVLink" text="install NetQ NVLink">}} must have the `cert-mode` attribute set to `user-cert`.
- You must have the following certificates. Make sure the certificates are valid and not expired.
    - A CA certificate (PEM-encoded) from your certificate authority.
    - A server TLS certificate and its corresponding private key (both PEM-encoded), signed by the same CA.
    - A PKCS#12 (.p12) certificate bundle for your switches, signed by the same CA. The .p12 file must not be password-protected.

## Upload the Certificates using the API

1. Upload your CA public certificate as a PEM-encoded file by making a POST request to the `/v1/certificates/ca` endpoint:

```
curl -X 'POST' \
  'https://<ip-address>/nmx/v1/certificates/ca' \
  -H 'accept: application/json' \
  -H 'Content-Type: multipart/form-data' \
  -F 'certificate=@<path-to-ca-cert.pem>'
```

A successful upload returns HTTP 200 OK with the CA certificate metadata:

```
{
  "type": "ca",
  "subject": "CN=My Organization CA",
  "issuer": "CN=My Organization CA",
  "serialNumber": "1a2b3c",
  "notBefore": "2025-01-01T00:00:00Z",
  "notAfter": "2030-01-01T00:00:00Z",
  "fingerprint": "sha256-hex-string",
  "keyAlgorithm": "RSA-4096"
}
```

2. Upload the server (southbound) TLS certificate and its private key (both as PEM-encoded files) by making a POST request to the `/v1/certificates/server` endpoint. The certificate must be signed by the same CA as the certificate you uploaded in the previous step.

```
curl -X 'POST' \
  'https://<ip-address>/nmx/v1/certificates/server' \
  -H 'accept: application/json' \
  -H 'Content-Type: multipart/form-data' \
  -F 'certificate=@<path-to-server-cert.pem>' \
  -F 'privateKey=@<path-to-server-key.pem>'
```

If the operation was successful, the API returns an operation ID which you can use to track the status of the upload. If the initial upload fails at any point, you can retry with the `force` query parameter. Setting `force=true` cleans up the metadata from the previous attempt and proceeds with a fresh upload:

```
curl -X 'POST' \
  'https://<ip-address>/nmx/v1/certificates/server?force=true' \
  -H 'accept: application/json' \
  -H 'Content-Type: multipart/form-data' \
  -F 'certificate=@<path-to-server-cert.pem>' \
  -F 'privateKey=@<path-to-server-key.pem>
```

Note that you cannot use the `force` parameter to replace a server certificate that has already been successfully uploaded. You must rotate certificates to replace them.

3. After the certificates are uploaded successfully, {{<link title="NVLink Bringup/#bringup-examples-using-custom-certificates" text="perform a bringup">}}.

## Rotate Certificates

Certificate rotation lets you replace CA, server, or switch P12 certificates in-place without reinstalling NetQ NVLink. Rotate certificates before they expire or when a certificate or key is compromised.

NetQ automatically monitors your certificates and raises a warning 30 days before expiry, escalating to critical once expired. By default, NetQ checks every 6 hours; both the interval and threshold are configurable, and alerts are delivered to your configured webhook receiver. See {{<link title="Manage Alerts/#certificate-expiration" text="Manage Alerts">}}.
### Rotation Prerequisites

The CA and server certificates must already be uploaded before you can rotate them. See {{<link title="#Upload the Certificates using the API" text="Upload the Certificates using the API">}}.

You also need the following valid, unexpired replacement certificates:

- A PEM-encoded CA certificate from your certificate authority
- A PEM-encoded server TLS certificate and its private key, signed by the same CA
- A PKCS#12 (`.p12`) bundle for your switches, signed by the same CA, without password protection

Before rotating certificates, set NetQ NVLink to maintenance mode, as described in the next section.

When you rotate the certificates, enter the same credentials (username) that you used during the {{<link title="NVLink Bringup" text="bringup process">}}.

### Maintenance Mode

Maintenance mode is a low-noise state you enable while performing disruptive operations such as certificate rotation. While on, NetQ NVLink suppresses fault-tolerance recovery and some internal processes so your work does not trigger alerts or automatic recovery actions.

You must enable maintenance mode before rotating certificates. Maintenance mode is a system setting named `maintenance.state`, with a value of `on` or `off` (default `off`). You manage it through the settings API. Rotation requests are rejected when it is off.

- Enable maintenance mode.
- Disable maintenance mode when rotation is complete so monitoring and fault-tolerance recovery resume.
- Certificate *upload* (initial install) requires maintenance mode to be off.

{{%notice note%}}
The maintenance-mode check applies when a rotation request is submitted. Disabling maintenance mode while a rotation is already in progress does not interrupt it.
{{%/notice%}}


#### Check the Current State

Send a GET request to `/v1/settings/maintenance.state`:

```
curl -X 'GET' \
  'https://<ip-address>/nmx/v1/settings/maintenance.state' \
  -H 'accept: application/json'
```

A successful request returns `HTTP 200 OK` with the setting:

```
{
  "Name": "maintenance.state",
  "Value": "off",
  "Description": "Maintenance mode state. When enabled, low-noise mode suppresses fault-tolerance and certificate expiration monitoring during certificate rotation.",
  "CreatedAt": "2026-01-15T10:00:00Z",
  "UpdatedAt": "2026-01-15T10:00:00Z"
}
```

#### Enable Maintenance Mode

Send a PATCH request to `/v1/settings` with the setting name and a value of `on`:

```
curl -X 'PATCH' \
  'https://<ip-address>/nmx/v1/settings' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{"Name":"maintenance.state","Value":"on"}'
```

A successful request returns `HTTP 200 OK` with the updated setting.

#### Disable Maintenance Mode

Send the same PATCH request with a value of `off`:

```
curl -X 'PATCH' \
  'https://<ip-address>/nmx/v1/settings' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{"Name":"maintenance.state","Value":"off"}'
```

A successful request returns `HTTP 200 OK` with the updated setting.

### Rotate the CA Certificate

CA rotation is synchronous. Send a PUT request to `/v1/certificates/ca` with the new CA certificate:

```
curl -X 'PUT' \
  'https://<ip-address>/nmx/v1/certificates/ca' \
  -H 'accept: application/json' \
  -H 'Content-Type: multipart/form-data' \
  -F 'certificate=@<path-to-ca-cert.pem>'
```

A successful rotation returns `HTTP 200 OK` with the new certificate metadata.

### Rotate the Server Certificate

Send a PUT request to `/v1/certificates/server` with the new certificate and private key. The certificate must be signed by the current CA:

```
curl -X 'PUT' \
  'https://<ip-address>/nmx/v1/certificates/server' \
  -H 'accept: application/json' \
  -H 'Content-Type: multipart/form-data' \
  -F 'certificate=@<path-to-server-cert.pem>' \
  -F 'privateKey=@<path-to-server-key.pem>'
```

A successful request returns `HTTP 202 Accepted` with an operation ID for tracking status.

By default, the new certificate is staged and services pick it up on their next reconnection. To activate it immediately and force managed services to reconnect, add `Reconnect=true`:

```
curl -X 'PUT' \
  'https://<ip-address>/nmx/v1/certificates/server?Reconnect=true' \
  -H 'accept: application/json' \
  -H 'Content-Type: multipart/form-data' \
  -F 'certificate=@<path-to-server-cert.pem>' \
  -F 'privateKey=@<path-to-server-key.pem>'
```

### Rotate Switch Certificates

Send a PUT request to `/v1/certificates/switches` with the new `.p12` bundle and one or more switches. The bundle must be signed by the current CA:

```
curl -X 'PUT' \
  'https://<ip-address>/nmx/v1/certificates/switches' \
  -H 'accept: application/json' \
  -H 'Content-Type: multipart/form-data' \
  -F 'CertP12=@<path-to-switch-bundle.p12>' \
  -F 'Switches={"Address":"10.1.1.1"}' \
  -F 'Switches={"Address":"10.1.1.2"}'
```

Each `Switches` entry takes an `Address` field containing the switch management IP or hostname, which must match a managed switch. To apply a switch profile, add a global `ProfileID` field, or set `ProfileID` per switch to override the global value:

```
  -F 'ProfileID=551137c2f9e1fac808a5f572' \
  -F 'Switches={"Address":"10.1.1.1"}' \
  -F 'Switches={"Address":"10.1.1.2","ProfileID":"661248d3a0f2gbd919b6g683"}'
```

A successful request returns `HTTP 202 Accepted ` with an operation ID. To apply different `.p12` bundles to different switches, submit separate requests. If rotation fails for a switch, you can resubmit the request for that switch.

### Track Progress

The server and switch rotations run asynchronously. Poll `GET /v1/operations/{id}` with the returned operation ID to check progress:

```
curl -X 'GET' \
  'https://<ip-address>/nmx/v1/operations/551137c2f9e1fac808a5f572' \
  -H 'accept: application/json'
```