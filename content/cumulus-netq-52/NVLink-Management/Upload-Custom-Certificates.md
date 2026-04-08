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

2. Upload the server (southbound) TLS certificate and its private key (both as PEM-encoded files) by making a POST request to the `v1/certificates/server` endpoint. The certificate must be signed by the same CA as the certificate you uploaded in the previous step.

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

Note that you cannot use the `force` parameter to replace a server certificate that has already been successfully uploaded. You must perform a fresh NetQ NVLink installation to replace a certificate.

3. After the certificates are uploaded successfully, {{<link title="NVLink Bringup/#bringup-examples-using-custom-certificates" text="perform a bringup">}}.