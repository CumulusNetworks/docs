---
title: NVLink Bringup
author: NVIDIA
weight: 300
toc: 4
---

After installing NetQ, perform a bringup to configure and register NetQ with a designated switch tray. This process enables NetQ to begin streaming telemetry and authorizes it to manage NVLink domains by establishing an mTLS-secured gRPC connection.

## Prerequisites

- Retrieve the {{<exlink url="https://docs.nvidia.com/networking/display/nvidianvosusermanualfornvlinkswitchesv25024282/sdn" text="SDN configuration profiles">}} from all switches included in the bringup procedure.
- Ensure you have configured a switch profile with the proper credentials. During the bringup process, you can specify a global switch profile for all switches or define individual profiles for each switch. Individual profiles take precedence over the global profile specified in the request body.


## NVLink Bringup Endpoints

### Switch Profile Endpoints

NetQ uses the following endpoints to manage switch credentials and access. The default value for both the username and the password is `admin`. You must specify at least one switch profile in the bringup request.

| Endpoint | Description |
| :-- | :-- |
| GET `/nmx/v1/switch-profiles` | Retrieve a list of switch profiles |
| POST `/nmx/v1/switch-profiles` | Create a new switch profile |
| GET `/nmx/v1/switch-profiles/{id}` | Retrieve a specific switch profile |
| DELETE `/nmx/v1/switch-profiles/{id}` | Delete a switch profile |
| PATCH `/nmx/v1/switch-profiles/{id}` | Update an existing switch profile |

### Bringup Endpoints

| Endpoint | Description |
| :-- | :-- |
| GET `/nmx/v1/bring-up` | Retrieve bring-up status with optional filters (pending, in progress, failed, completed) |
| POST `/nmx/v1/bring-up` | Initiate a new bring-up process for one or more switches |
| GET `/nmx/v1/bring-up/{id}` | Retrieve bring-up status for a specific operation |

## Bringup Examples

The following example performs a switch bringup by making a POST request to the `/v1/bring-up` endpoint. It defines the FM configuration profile, the switch profile ID, and list of switches included in the bringup:

```
curl -X 'POST' \
  'https://<NMX-Manager-API>/nmx/v1/bring-up' \
  -H 'accept: application/json' \
  -H 'Content-Type: multipart/form-data' \
  -F 'FmConfig=@<fm-config-file>' \
  -F 'ProfileID=<switch-profile-id>' \
  -F 'Switches={
  "Address": "<switch-IP-address-or-hostname>"
}'
```

This example is similar to the previous one, but defines both a global and individual profile ID. The individual profile ID overrides the global ID attribute:

```
curl -X 'POST' \
  'https://<NMX-Manager-API>/nmx/v1/bring-up' \
  -H 'accept: application/json' \
  -H 'Content-Type: multipart/form-data' \
  -F 'FmConfig=@<fm-config-file>' \
  -F 'ProfileID=' \
  -F 'Switches={
  "Address": "<switch-A-IP-address-or-hostname>"
}' \
  -F 'Switches={
  "Address": "<switch-B-IP-address-or-hostname>",
  "ProfileID": "<custom-switch-profile-id>"
}'
```

### Track the Progress

If all initial validations succeed, the API returns an `HTTP 202 Accepted` response with a JSON body containing a bringup operation ID. You can make a GET request to the `/v1/bring-up/` endpoint to track the progress of the bringup.

```
curl -X 'GET' \
  'https://<NMX-Manager-API>/nmx/v1/bring-up/682880baaf653727786b618f' \
  -H 'accept: application/json'
```

## Troubleshoot the Bringup Process

After the bringup process begins, it cannot be stopped. If the bringup operation fails, clean up the switch files and certificates and try again.

1. Establish an SSH connection to the switch.

2. Display the certificates configured on the switch:

```
nv show system security ca-certificate
nv show system security certificate
```

3. Delete the certificates associated with NMX-M or NetQ NVLink:

```
nv action delete system security certificate <certificate_name>
nv action delete system security ca-certificate <ca_certificate_name>
```

4. Remove the SDN configuration file and restore it to the default:

```
nv action delete sdn config apps nmx-controller type fm_config files fm_config.cfg
nv action reset sdn factory-default
```

5. Disable the cluster state:

```
nv set cluster state disabled
nv config apply
```

6. Remove the certificate and configuration files:

```
rm /tmp/cert.p12 /tmp/ca-cert.crt /tmp/fm_config.cfg
```