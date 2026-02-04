---
title: Troubleshooting and Support
author: NVIDIA
weight: 1005
toc: 3
---

## Generate a Support File on the Server Cluster

The `opta-support` command generates information for troubleshooting issues with NetQ. It provides information about the NetQ server configuration and runtime statistics. 

```
nvidia@server:~$ sudo opta-support
Please send /var/support/opta_support_server_2025119_165552.txz to Nvidia support.
```

## Generate Support Files on NVOS Switches

Use the REST API to generate technical support files on NVOS switches. Alternately, you can generate files directly on the switch by following the instructions in the {{<exlink url="https://docs.nvidia.com/networking/display/nvidianvosusermanualfornvlinkswitchesv25024282/technical+support" text="NVOS user manual">}}.

Use the following endpoints to list, download, and optionally delete the `tar.gz` support file.

| Endpoint | Description |
| :-- | :-- |
| GET `/nmx/v1/support-packages` | Retrieve a list of support packages, including package metadata |
| POST `/nmx/v1/support-packages` | Initiate log collection from individual switches or from switches in a given domain |
| GET `/nmx/v1/support-packages/{id}` | Download the `tar.gz` support package |
| DELETE `/nmx/v1/support-packages/{id}` | Delete support package |

You can specify a `ProfileID` within the request body to authenticate switch access credentials. If you omit the `ProfileID`, NetQ uses the default profile for authentication.

The following example initiates the log collection by making a POST request to the `/v1/support-packages` endpoint, specifying the individual IP addresses for the switches. The response returns an operation ID, which you can use to query the status of the request:
```
POST /nmx/v1/support-packages
Content-Type: application/json
 
{
  "ProfileID": "profile-id-name"
  "Switches": [
    { "Address": "192.0.2.10" },
    { "Address": "192.0.2.12" }
  ]
}
```
The following example is similar to the one above, but uses the `DomainID` parameter that includes switches associated with a particular domain.

```
POST /nmx/v1/support-packages
Content-Type: application/json
 
{
  "Domains": [
    { "551137c2f9e1fac808a5f572" },
    { "551137c2f9e1fac808a5f573" }
  ]
}
```

To list the support packages, make a GET request to the `/v1/support-packages` endpoint. The response returns the file metadata:

```
GET /nmx/v1/support-packages
```

Example response:
```
{
  {
    "fileID": "521137c2f9e1fac808a5f572",
    "filename": "support-logs-2025-10-31.tar.gz",
    "size": 1048576,
    "uploadDate": "2025-10-31T12:34:56Z",
    "switchAddress": "192.0.2.10"
  }
}
```

Download the support files by making a GET request to the `/v1/support-packages/{id}` endpoint. It may take several minutes for the response to return the `tar.gz` support file.