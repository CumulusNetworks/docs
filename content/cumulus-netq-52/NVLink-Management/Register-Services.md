---
title: Register Services
author: NVIDIA
weight: 325
toc: 3
---

NetQ must register with the NMX-T and NMX-C services to begin receiving network telemetry and control data. Communication between these services is secured using certificate-based mTLS encryption. 

These certificates are automatically created during the installation process, but you must configure them on the switch trays hosting NMX-C and NMX-T. Alternately, you can provide your own certificates.

{{<notice tip>}}
You can also perform the steps outlined on this page using the <code>/v1/switch-profiles</code> endpoint. Refer to {{<link url="NVLink-Bringup" text="NVLink Bringup">}} for more information.
{{</notice>}}

## Secure Devices with Certificates

You can configure NetQ NVLink devices to use either NetQ NVLink's self-signed certificate or your own certificates. If you are using your own certificates, upload the CA certificate first, followed by the server certificate, and finally the switch certificate.

{{<tabs "certificate-options" >}}

{{<tab "Self-signed certificates" >}}

1. Use SSH to log in to the master node of your NetQ NVLink deployment. This is the node you used during the initial installation.

```
ssh nvidia@<IP_Address>
```

2. Run the `/opt/netq-admin/nvl/scripts/create-certificate.sh` script as the root user. When prompted, provide a certificate name (typically the switch’s hostname or IP address):

```
nvidia@ubuntu:~$ su
root@ubuntu:/home/nvidia# /opt/netq-admin/nvl/scripts/create-certificate.sh example
certificate.cert-manager.io/example-certificate created
Certificate is ready after 10 seconds.
Extracting secret data to local files...
Files created:
-rw-r--r-- 1 root root 1094 May 29 11:57 example-ca.crt
-rw-r--r-- 1 root root 1424 May 29 11:57 example-tls.crt
-rw-r--r-- 1 root root 3243 May 29 11:57 example-tls.key
-rw------- 1 root root 3907 May 29 11:57 example-tls.p12
Done.
```

3. Copy the `.crt` and `.p12` files to the switch tray. Use the {{<exlink url=“https://docs.nvidia.com/networking/display/nvidianvosusermanualfornvlinkswitchesv25022225/cluster+manager+commands” text="NVOS cluster manager commands">}} to apply the certificates to both NMX-C and NMX-T.

{{</tab>}}

{{<tab "User-provided certificates" >}}

{{<tabs "user-provided-certs">}}

{{<tab "CA certificates" >}}

1. Ensure that you do not already have a certificate installed by making a GET request to the `/v1/certificates/` endpoint.

2. Upload your certificates by making a POST request to the `/v1/certificates/ca` endpoint. In the request body, specify the file. The certificate must be in PEM format and end in `.crt`. If successful, the response body includes metadata about the certificate including its expiration date.

{{</tab >}}

{{<tab "Server certificates" >}}

1. Ensure that you do not already have a server certificate installed by making a GET request to the `/v1/certificates/` endpoint.

1. Upload your certificates by making a POST request to the `/v1/certificates/server` endpoint. In the request body, specify the `.crt` and `.key` files. If successful, the response body includes metadata about the certificate including its expiration date.

{{</tab >}}

{{<tab "Switch certificates" >}}

1. Ensure that you do not already have a switch certificate installed by making a GET request to the `/v1/certificates/` endpoint.

1. Upload your certificates by making a POST request to the `/v1/certificates/switch` endpoint. In the request body, specify the `.p12` file. If successful, the response body includes metadata about the certificate including its expiration date.

1. Perform an {{<link url="NVLink-Bringup" text="NVLink Bringup">}} by making a POST request to the `/v1/bring-up/` endpoint, and specify the switch `.p12` file in the request body.

{{</tab>}}

{{</tabs>}}

{{</tab>}}

{{</tabs>}}

## Register Services

Register the services by making a POST request to the `v1/services` endpoint.

{{<tabs "TabID42" >}}

{{<tab "cURL Example" >}}

```
curl --request POST \
  --url https://<ip_address>/nmx/v1/services \
  --header 'Authorization: Basic cnctdXNlcjpOdmlkaWExMg==' \
  --header 'Content-Type: application/json' \
  --data '{
  "Name": "Registration,
  "Description": "Example registration to controller",
  "ServiceType": "CONTROLLER",
  "ServiceConnectionInformation": {
    "Address": "10.188.47.166",
    "PortNumber": 9370
  }
}'
```

{{</tab>}}

{{</tabs>}}

## Check the Status of a Registered Service

To retrieve the status of all registered services, make a GET request to the `v1/services` endpoint.

{{<tabs "TabID70" >}}

{{<tab "cURL Example" >}}
```
curl --request GET \
  --url https://<ip_address>/nmx/v1/services \
  --header 'Authorization: Basic cnctdXNlcpOdmlkaWExMg=='
```

{{</tab>}}

{{</tabs>}}

You can add a filter to the response to retrieve either telemetry or controller services exclusively:

{{<tabs "TabID85" >}}

{{<tab "cURL Example" >}}
```
curl --request GET \
  --url https://<ip_address>/nmx/v1/services \TELEMETRY&offset=0&limit=1' \\
  --header 'Authorization: Basic cnctdXNlcpOdmlkaWExMg=='
```

{{</tab>}}

{{</tabs>}}

## Remove a Registered Service

NetQ NVLink includes a failover mechanism that transfers services to a secondary IP address in case the primary IP address is unavailable. Before you can remove a registered service, you must disable the failover feature.

1. Run the following command to view the NetQ NVLink configuration file:

```
kubectl edit cm -n netq-nvl common-config
```

2. Locate the `feature-flags` section. Change the `service-failover-enabled` value from `true` to `false`.

3. Make a `DELETE` request to the `v1/services` endpoint.
