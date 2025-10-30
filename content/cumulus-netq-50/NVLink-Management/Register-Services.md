---
title: Register Services
author: NVIDIA
weight: 325
toc: 3
---

NetQ must register with the NMX-T and NMX-C services to begin receiving network telemetry and control data. Communication between these services is secured using certificate-based mTLS encryption. These certificates are automatically created during the installation process, but you must configure them on the switch trays hosting NMX-C and NMX-T.

## Generate Certificates

1. Use SSH to log in to the master node of your NetQ NVLink deployment. This is the node you used during the initial installation.

```
ssh nvidia@<IP_Address>
```

2. Run the `opt/netq-admin/nvl/scripts/reate-certificate.sh` script as the root user. When prompted, provide a certificate name (typically the switch’s hostname or IP address):

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

3. Copy the `example-ca.crt` and `example-tls.p12` files to the switch tray. Replace the filenames with the actual names of the files. Use the {{<exlink url="https://docs.nvidia.com/networking/display/nvidianvosusermanualfornvlinkswitchesv25022225/cluster+manager+commands" text="NVOS cluster manager commands">}} to apply the certificates to both NMX-C and NMX-T.

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

