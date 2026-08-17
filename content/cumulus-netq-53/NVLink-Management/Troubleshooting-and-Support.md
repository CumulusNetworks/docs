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
| GET `/v1/support-packages` | Retrieve a list of support packages, including package metadata |
| POST `/v1/support-packages` | Initiate log collection from individual switches or from switches in a given domain |
| GET `/v1/support-packages/{id}` | Download the `tar.gz` support package |
| DELETE `/v1/support-packages/{id}` | Delete support package |

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


## Admin Endpoints for NMX-M Services

Each NetQ NVLink (NMX-M) microservice listens on a second HTTP address, `admin-addr`, used for health checks, Prometheus metrics, runtime logging, and configuration inspection during troubleshooting. This interface is separate from the NetQ NVLink REST API.

Use these endpoints when troubleshooting a specific NMX-M service on the NetQ cluster, typically under NVIDIA support guidance, or when you need evidence for a support case:

- Raise log verbosity temporarily (`/log-level`) without restarting a pod
- Confirm the process admin listener is up (`/live`)
- Capture the service’s effective config for a support case (`/config_dump`)

From a NetQ cluster node with Kubernetes access, port-forward to the service pod’s admin port. Ports differ by service (see the service ConfigMap `admin-addr`; commonly in the `90xx` range). Admin endpoints are not exposed through the NetQ VIP and are intended for cluster operators and NVIDIA support.

{{%notice infonopad%}}
- These endpoints require **no authentication**. Restrict access to trusted cluster operators.
- <code>GET /config_dump</code> returns the service’s runtime configuration. The response may include credentials and other sensitive data. Handle the output as confidential and share it only with NVIDIA support when requested.
{{%/notice%}}

| Endpoint | Method | Description |
|---|---|---|
| `/live` | GET | Returns `200` and `OK` if the process HTTP admin server is up |
| `/ready` | GET | Not implemented — returns `501` |
| `/metrics` | GET | Prometheus metrics |
| `/log-level` | GET | Current log level (JSON), e.g. `{"level":"info"}` |
| `/log-level` | PUT | Change log level at runtime (no restart). JSON body: `{"level":"debug"}` (also `info`, `warn`, `error`) |
| `/config_dump` | GET | Full service configuration as JSON |

The following example shows this operation. Replace `<pod>`, `<admin-port>`, and namespace as appropriate; the namespace is typically `netq-nvl`:

```
kubectl port-forward -n netq-nvl pod/<pod> 19081:<admin-port>

curl -sS http://127.0.0.1:19081/live

curl -sS http://127.0.0.1:19081/ready          # expect HTTP 501

curl -sS http://127.0.0.1:19081/log-level

curl -sS -X PUT -H "Content-Type: application/json" \
  -d '{"level":"debug"}' http://127.0.0.1:19081/log-level

curl -sS -X PUT -H "Content-Type: application/json" \
  -d '{"level":"info"}' http://127.0.0.1:19081/log-level   # restore

curl -sS http://127.0.0.1:19081/config_dump

curl -sS http://127.0.0.1:19081/metrics | head
```

To find the `<admin-port>` for a service:

```
kubectl get cm -n netq-nvl <service>-service-config -o yaml | grep admin-addr
```