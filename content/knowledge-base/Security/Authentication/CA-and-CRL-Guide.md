---
title: CA and CRL Guide
author: NVIDIA
weight: 414
toc: 3
---
## Generate Root CA Certificates

Customers often have multiple Root CA certificates and create bundles of CA certificates. NVIDIA applications support CA bundles in most cases. With multiple Root CA certificates, it is crucial to name them for easy identification.

## CN and Filename Naming Schema

With STATE_NAME and NUMBER. Choose any naming schema you are comfortable with.

Format: ROOT_CA_<STATE_NAME>_<NUMBER>
Examples:

```
ROOT_CA_CALIFORNIA_00
ROOT_CA_CALIFORNIA_01
ROOT_CA_TEXAS_00
ROOT_CA_FLORIDA_00
```

Use common names to:
- Prevent confusion between different CAs on the system.
- Facilitate tracking of which CA issued which certificates.
- Avoid potential name collisions in certificate chains and in OpenSSL.
- Aid in quick identification during troubleshooting.

## Match the CA Filename with the CN Name

For example, if `CN=ROOT_CA_CALIFORNIA_00`, use the file name `ROOT_CA_CALIFORNIA_00.crt/key`.

The benefits include:
- Providing a clear mapping between certificate files and their identity.
- Reducing the chances of using incorrect certificates by mistake.
- Easier debugging.

{{%notice note%}}
Never generate two CA certificates with the same CN as OpenSSL might:
- Override one CA with the other.
- Fail to differentiate between certificates with the same CN.
- Use an incorrect public key for verification.
{{%/notice%}}

## OpenSSL Commands to Generate Root CA Certificates

The following openssl command examples show you how to generate root CA certificates:

```
# Generate Root CA Private Key
openssl genrsa -out ROOT_CA_CALIFORNIA_00.key 4096

# Generate Root CA Certificate
openssl req -x509 -new -key ROOT_CA_CALIFORNIA_00.key -sha256 -days 3650 -out ROOT_CA_CALIFORNIA_00.crt -subj "/C=US/ST=California/L=Santa Clara/O=NVIDIA/OU=NVIDIA Test CA/CN=ROOT_CA_CALIFORNIA_00"
 
# Verify Root CA Certificate
openssl x509 -in ROOT_CA_CALIFORNIA_00.crt -text -noout
```

Root CA certificates sign as many client certificates as needed.

## Create a CA Bundle

To generate a CA bundle:

```
cat ROOT_CA_CALIFORNIA_01.crt ROOT_CA_TEXAS_01.crt ROOT_CA_FLORIDA_01.crt > CA_BUNDLE_[Meaningful_Name].crt
```

## Generate Client Certificates

Client certificates provide client identity to servers ONLY when mTLS is enabled.

{{%notice note%}}
Use well-known definitions while discussing client certificates. The client has to use its certificate only after the server enables mTLS and sends a certificate request TLS record to the client.
{{%/notice%}}

Without mTLS, the client certificate has no purpose.

### CN and Filename Naming Schema

Format: CLIENT_<CLIENT_NUMBER/NAME>_<ROOT_CA_NAME>

The examples below use city for client name.

```
CLIENT_SAN_FRANCISCO_ROOT_CA_CALIFORNIA_01
CLIENT_AUSTIN_ROOT_CA_TEXAS_01
CLIENT_ORLANDO_ROOT_CA_FLORIDA_01
```

Using common names (CN) with Root CAs:
- Ensures each client certificate is uniquely identifiable.
- Ensures the CA certificate is known by the client CN name.
- Aids in quick identification during troubleshooting.
- Saves execution of many openssl commands.

### Matching Client Certificate Filenames with CN Names

For example, if `CN=CLIENT_SAN_FRANCISCO_ROOT_CA_CALIFORNIA_01`, use the filename `CLIENT_SAN_FRANCISCO_ROOT_CA_CALIFORNIA_01.crt/key`.

### OpenSSL Commands to Generate Client Certificates

```
# Generate Client Private Key
openssl genrsa -out CLIENT_SAN_FRANCISCO_ROOT_CA_CALIFORNIA_01.key 2048
 
# Generate Client Certificate Signing Request (CSR)
openssl req -new -key CLIENT_SAN_FRANCISCO_ROOT_CA_CALIFORNIA_01.key -out CLIENT_SAN_FRANCISCO_ROOT_CA_CALIFORNIA_01.csr -subj "/C=US/ST=California/L=Santa Clara/O=Client Organization/OU=Client Department/CN=CLIENT_SAN_FRANCISCO_ROOT_CA_CALIFORNIA_01"
 
# Sign Client Certificate with CA
openssl x509 -req -in CLIENT_SAN_FRANCISCO_ROOT_CA_CALIFORNIA_01.csr -CA ROOT_CA_CALIFORNIA_01.crt -CAkey ROOT_CA_CALIFORNIA_01.key -CAcreateserial -out CLIENT_SAN_FRANCISCO_ROOT_CA_CALIFORNIA_01.crt -days 365 -sha256
 
# Verify Client Certificate
openssl x509 -in CLIENT_SAN_FRANCISCO_ROOT_CA_CALIFORNIA_01.crt -text -noout
```

## Generate Server Certificates

Server certificates provide server identification. A client verifies the server certificate during the TLS handshake unless the client decides to skip the verification.

{{%notice note%}}
Use well-known definitions while discussing server certificates. The server always has to use its certificate for the TLS handshake. The server certificate is sent to client in the server hello TLS record irrespective of mTLS or TLS. The client can skip server certificate verification.
{{%/notice%}}

### CN and Filename Naming Schema

Format: Considering the clients such as curl, browser, gnmic tries to resolve the server certificate CN name against domain name, server certificate CN name can be chosen as per the application.

For example, if the server in on a Cumulus switch, the server certificate CN name can be the switch_hostname_application_name.

Both client and server can be signed with same Root CA certificate. But it is recommended to use different Root CA to sign clients and server certificates.

For example:

```
ROOT_CA_CALIFORNIA_00 (all *_00) only will be used to sign server certificate.
ROOT_CA_CALIFORNIA_(01-N) can be used to sign client certificate.
```

### Match the Server Certificate Filename with the CN Name

For example, if `CN=CUMULUS_DC_TOR_15_gnmi`, use the filename `CUMULUS_DC_TOR_15_gnmi.crt/key`.

```
OpenSSL Commands to generate Server Certificate
# Generate Server Private Key
openssl genrsa -out CUMULUS_DC_TOR_15_gnmi.key 2048
 
# Generate Server Certificate Signing Request (CSR)
openssl req -new -key CUMULUS_DC_TOR_15_gnmi.key -out CUMULUS_DC_TOR_15_gnmi.csr -subj "/C=US/ST=California/L=Santa Clara/O=Server Organization/OU=Server Department/CN=CUMULUS_DC_TOR_15_gnmi"
 
# Sign Server Certificate with CA
openssl x509 -req -in CUMULUS_DC_TOR_15_gnmi.csr -CA ROOT_CA_CALIFORNIA_00.crt -CAkey ROOT_CA_CALIFORNIA_00.key -CAcreateserial -out CUMULUS_DC_TOR_15_gnmi.crt -days 365 -sha256
 
# Verify Server Certificate
openssl x509 -in CUMULUS_DC_TOR_15_gnmi.crt -text -noout
```

## Deploy the Certificate

### For TLS Handshake

For TLS handshake, the client needs:
- The CA certificate that signed the server certificate. If we follow our example given above and best practices, then ROOT_CA_CALIFORNIA_00.CRT should be copied on client.
Server:

For TLS handshake, server needs:

the server certificate and private key. As per our example given above, CUMULUS_DC_TOR_15_gnmi.crt/key should be copied on server.

### For mTLS Handshake

For mTLS handshake, client needs:

the CA certificate which has signed the server certificate.
the client certificate and private key.
If we follow our example given above and best practices, then ROOT_CA_CALIFORNIA_00.CRT and CLIENT_SAN_FRANCISCO_ROOT_CA_CALIFORNIA_01.crt/key should be copied on client.

For mTLS handshake, server needs:

the server certificate and private key.
the CA certificate which has signed the client certificate.

If we follow our example given above and best practices, then CUMULUS_DC_TOR_15_gnmi.crt/key and ROOT_CA_CALIFORNIA_01.CRT should be copied on server.

Note:

ROOT_CA_CALIFORNIA_00.CRT is used to sign server certificate and is copied on client.
ROOT_CA_CALIFORNIA_01.CRT is used to sign client certificate and is copied on server.

### Import Certificates and CRLs

Cumulus Linux provides a way to import Certificates and CRLs onto the switch using action import.

Example:

```
vagrant@cumulus:mgmt:/vagrant$ nv action import system security --help
usage:
  nv [options] action import system security ca-certificate
  nv [options] action import system security certificate
  nv [options] action import system security crl
 
Description:
  security        Security features
 
Attributes:
  ca-certificate  A collection of CA/RA/Root X.509 certificates.
  certificate     A collection of X.509 certificates.
  crl             A collection of X.509 Certificate Revocation Lists (CRLs).
```

## Request with TLS Handshake

Example of client request\Configuration with TLS Handshake

```
$curl --cacert ROOT_CA_CALIFORNIA_00.crt https://<server-address>/endpoint
$gnmic --tls-ca ROOT_CA_CALIFORNIA_00.crt --path ....
```

Note: ROOT_CA_CALIFORNIA_00.crt is used to sign server certificate, which must be set as ca-certificate on client.

### List of TLS Clients used in Cumulus Switch:

#### gRPC Tunnel Client

Config:

```
nv [options] set system grpc-tunnel server <server-name-id> [ca-certificate ...]
nv set system grpc-tunnel server server_sfo ROOT_CA_CALIFORNIA_00.crt
```

#### Linux Commands

Linux commands such as `wget` also use CA certificates at `/etc/ssl/certs/ca-certificates.crt`
while downloading a file from the HTTPS server.

{{%notice note%}}
If a client decides to skip server certificate verification, it does not need a CA certificate and all requests are allowed to proceed. A request works even without a CA certificate configuration on the switch.
{{%/notice%}}

### Server Configuration with TLS Handshake

The server must always specify its certificate and private key.

The following commands show the server certificate configuration on the switch:

```
cumulus@switch:~$ nv set system gnmi-server certificate <arg>
cumulus@switch:~$ nv set system api certificate <arg>
```

## Request with mTLS Handshake

### Client Request Configuration with mTLS Handshake

The client must also specify its certificate and private key during the mTLS handshake.

{{%notice note%}}
mTLS is enabled only by the server.
{{%/notice%}}

```
$curl --cacert ROOT_CA_CALIFORNIA_00.crt --cert CLIENT_SAN_FRANCISCO_ROOT_CA_CALIFORNIA_01.crt --key CLIENT_SAN_FRANCISCO_ROOT_CA_CALIFORNIA_01.key https://<server-address>/endpoint

$gnmic --tls-ca ROOT_CA_CALIFORNIA_00.crt --tls-cert CLIENT_SAN_FRANCISCO_ROOT_CA_CALIFORNIA_01.crt --tls-key CLIENT_SAN_FRANCISCO_ROOT_CA_CALIFORNIA_01.key --path ....
```

Config of TLS Clients used in Cumulus Switch to specify certificates for mTLS Handshake:

```
nv [options] set system grpc-tunnel server <server-name-id> [certificate ...]
```

Note: Client may specify client certificate and private key in configuration\request even when mTLS is not enabled by server. But in that case, client certificate will not play any role.

### Example of server configuration with mTLS Handshake

Server controls mTLS configuration by either specifying CA certificates or by other knobs.

Example for Cumulus Switch:

```
nv [options] set system gnmi-server mtls ca-certificate <arg>
nv set system gnmi-server mtls ca-certificate ROOT_CA_CALIFORNIA_01.crt

nv [options] set system api mtls ca-certificate <arg>
nv set system api mtls ca-certificate ROOT_CA_CALIFORNIA_01.crt
```

Note: ROOT_CA_CALIFORNIA_01.crt is used to sign client certificate, which must be set as ca-certificate on server.

#### CA Bundle on the Switch

Instead of single CA certificate, CA bundle can be used on Cumulus Switch.

```
nv [options] set system gnmi-server mtls ca-certificate <arg>
nv set system gnmi-server mtls ca-certificate CA_BUNDLE_[Meaningful_Name].crt
```

## Packet Exchange with the TLS or mTLS Handshake

Figure: PACKET EXCHANGE WHILE TLS {mTLS shown in Light Blue}

Note: multiple TLS record are exchanged in single PACKET to keep initiation of session faster and shorter.

## Intermediate CA (ICA)

In most customer environments, intermediate certificates signs client certificates. And Root CA certificate signs intermediate certificates.

For Example: Customer may have

A root CA for all LABs and Data Centers in California.
Intermediate CAs for different data centers in California or for different services i.e. INTERMEDIATE_CA_SAN_FRANCISCO or INTERMEDIATE_CA_TELEMETRY.
It is utmost important to use Intermediate CA in our testing environment to simulate real customer environment.

### CN and Filename Naming Schema

Format: INTERMEDIATE_CA_<CITY\SERVICE_NAME>_<ROOT_CA_NAME>

Example:

```
INTERMEDIATE_CA_SAN_FRANCISCO_ROOT_CA_CALIFORNIA_01
INTERMEDIATE_CA_TELEMETRY_ROOT_CA_CALIFORNIA_01
```

### Matching Intermediate Certificate Filename with the CN Name

Example: If CN=INTERMEDIATE_CA_SAN_FRANCISCO_ROOT_CA_CALIFORNIA_01, the filename should be INTERMEDIATE_CA_SAN_FRANCISCO_ROOT_CA_CALIFORNIA_01.crt/key.

### OpenSSL Commands to generate Intermediate Certificates

```
# Generate Intermediate CA Private Key
openssl genrsa -out INTERMEDIATE_CA_SAN_FRANCISCO_ROOT_CA_CALIFORNIA_01.key 2048
 
# Generate Intermediate CA Certificate Signing Request (CSR)
openssl req -new -key INTERMEDIATE_CA_SAN_FRANCISCO_ROOT_CA_CALIFORNIA_01.key -out INTERMEDIATE_CA_SAN_FRANCISCO_ROOT_CA_CALIFORNIA_01.csr -subj "/C=US/ST=California/L=Santa Clara/O=Intermediate CA Organization/OU=Intermediate CA Department/CN=INTERMEDIATE_CA_SAN_FRANCISCO_ROOT_CA_CALIFORNIA_01"
 
# Sign Intermediate CA Certificate with Root CA
openssl x509 -req -in INTERMEDIATE_CA_SAN_FRANCISCO_ROOT_CA_CALIFORNIA_01.csr -CA ROOT_CA_CALIFORNIA_01.crt -CAkey ROOT_CA_CALIFORNIA_01.key -CAcreateserial -out INTERMEDIATE_CA_SAN_FRANCISCO_ROOT_CA_CALIFORNIA_01.crt -days 365 -sha256
 
# Verify Intermediate CA Certificate
openssl x509 -in INTERMEDIATE_CA_SAN_FRANCISCO_ROOT_CA_CALIFORNIA_01.crt -text -noout
```

### CN and Filename Naming Schema for Client signed by ICA:
Format: CLIENT_<CLIENT_NUMBER/NAME>_<INTERMEDIATE_CA_NAME>

Example:

CLIENT_SAN_FRANCISCO_INTERMEDIATE_CA_SAN_FRANCISCO

#### Matching Client Certificate Filename with CN Name

Example: If CN=CLIENT_SAN_FRANCISCO_INTERMEDIATE_CA_SAN_FRANCISCO, the filename should be CLIENT_SAN_FRANCISCO_INTERMEDIATE_CA_SAN_FRANCISCO.crt/key.

## Client Certificate Chains

Client certificate chains are supplied in request to server when intermediate CA is used to sign client certificate and when mTLS is enabled by server.

Client certificate chain is a sequence of certificates starting from client certificate with intermediate CA certificate.

cat CLIENT_SAN_FRANCISCO_ROOT_CA_CALIFORNIA_01.crt INTERMEDIATE_CA_SAN_FRANCISCO_ROOT_CA_CALIFORNIA_01.crt  > CLIENT_SAN_FRANCISCO_chain.crt

### Using client certificate chain in curl or gnmic:

```
curl --cacert ROOT_CA_CALIFORNIA_00.crt --cert CLIENT_SAN_FRANCISCO_chain.crt --key CLIENT_SAN_FRANCISCO_INTERMEDIATE_CA_SAN_FRANCISCO.key https://<server-address>/endpoint
```

Note: Key for client certificate is CLIENT_SAN_FRANCISCO_INTERMEDIATE_CA_SAN_FRANCISCO.key.

### Certificate Revocation List (CRL)

Certificate Revocation List (CRL) is a list of certificates that have been revoked by a Certificate Authority (CA).

### CN and Filename Naming Schema

Format: CRL_<ROOT_CA_NAME>

Example:

CRL_ROOT_CA_CALIFORNIA_00

### Matching CRL Filename with CN Name

Example: If CN=CRL_ROOT_CA_CALIFORNIA_00, the filename should be CRL_ROOT_CA_CALIFORNIA_00.pem.

### OpenSSL Commands to generate CRL

Assume ROOT_CA_CALIFORNIA_01 has signed 10 client certificates. And now, 3 client certificates should be revoked.

#### Create index.txt, crlnumber and openssl.cnf

- CRL_NUMBER is a random number.
- Choose directory for index.txt, crlnumber and openssl.cnf.
- ROOT_CA_CALIFORNIA_01.crt and ROOT_CA_CALIFORNIA_01.key should be in the directory.
- Choose default_days and default_crl_days.

```
$touch index.txt
 
$echo <CRL_NUMBER> > crlnumber
 
$cat <<EOF > openssl.cnf
[ ca ]
default_ca = CA_default
 
[ CA_default ]
dir             = .
database        = $dir/index.txt
certificate     = ./ROOT_CA_CALIFORNIA_01.crt
private_key     = ./ROOT_CA_CALIFORNIA_01.key
crlnumber       = $dir/crlnumber
default_days    = 365
default_crl_days = 30
```

#### Revoke Client Certificates

```
openssl ca -config openssl.cnf -revoke CLIENT_SAN_FRANCISCO_ROOT_CA_CALIFORNIA_01.crt
openssl ca -config openssl.cnf -revoke CLIENT_SACRAMENTO_ROOT_CA_CALIFORNIA_01.crt
openssl ca -config openssl.cnf -revoke CLIENT_LOS_ANGELES_ROOT_CA_CALIFORNIA_01.crt
```

{{%notice note%}}
In most cases, CA issues a CRL file with `No Certificate revoked`, in which case the `openssl ... -revoke` command is skipped.
{{%/notice%}}

#### Generate the CRL

```
cumulus@switch:~$ openssl ca -config openssl.cnf -gencrl -out CRL_ROOT_CA_CALIFORNIA_01.pem
```

### Verify the CRL

```
cumulus@switch:~$ openssl crl -in CRL_ROOT_CA_CALIFORNIA_01.pem -text -noout
```

To create a CRL bundle file, concatenate multiple CRL files of different Root CAs.

```
cumulus@switch:~$ cat CRL_ROOT_CA_CALIFORNIA_01.pem CRL_ROOT_CA_TEXAS_01.pem CRL_ROOT_CA_FLORIDA_01.pem > CRL_BUNDLE_CALIFORNIA_TEXAS_FLORIDA.pem
```

## Deploy CRL on server

For Cumulus Switch, you can deploy the CRL with the nv action import command:

```
cumulus@switch:~$ nv action import system security crl <crl-file>
```

### Bind the CRL with a server or client

{{%notice note%}}
Both the server and client can use the CRL.
{{%/notice%}}

```
cumulus@switch:~$ nv set system gnmi-server mtls crl <crl-file>
cumulus@switch:~$ nv set system api mtls crl <crl-file>

# TBD, in future, grpc-tunnel server will support crl.
nv [options] set system grpc-tunnel server <server-name-id> [crl ...]
```

## CRL Processing

### CRL Processing for Client Certificate on the Server

After a server has an active CRL configuration, the client request is processed as shown below.

{{%notice note%}}
For the server, both the CA certificate and the CRL are used only if mTLS is enabled. They are used to verify the client certificate.
{{%/notice%}}

- Say client certificate is CLIENT_SAN_FRANCISCO_ROOT_CA_CALIFORNIA_01.crt
- CRL for ROOT_CA_CALIFORNIA_01 i.e content of ROOT_CA_CALIFORNIA_01.pem, must exist in CRL file(bundle or individual) bound to server. CRL file may have No revoked certificates, but it must exist.
Error: {unable to get certificate CRL} will be returned if CRL file does not exist.
- CRL of ROOT_CA_CALIFORNIA_01 must be valid as per current time.
Error: {CRL has expired} will be returned if CRL is expired.
- Certificates must not be on the revoked certificates list for request to succeed.
Error: {certificate revoked} will be returned if certificate is revoked.

### CRL Processing for Server Certificate on the Client

CRL processing is similar to client certificate processing performed by server.

{{%notice note%}}
- The client uses the CRL to verify the server certificate (during TLS handshake).
- The server uses the CRL to verify the client certificate (during mTLS handshake).
{{%/notice%}}
