---
title: NetQ NVLink API User Guide
author: NVIDIA
weight: 350
toc: 3
---

The NetQ NVLink API is organized around {{<exlink url="https://en.wikipedia.org/wiki/REST" text="REST">}} and conforms with {{<exlink url="https://spec.openapis.org/oas/v3.0.3" text="OpenAPI Specification v3.0.3">}}. The API provides access to resources and functionalities through a set of defined endpoints. Each endpoint has its own schema, which includes the payload, parameters, and the expected request/response formats.

- {{<exlink url="http://docs.nvidia.com/networking-ethernet-software/netq-nvlink-api-510/" text="REST API in Swagger">}}
- {{<exlink url="https://docs.nvidia.com/networking-ethernet-software/netq-nvlink-api-510/openapi.yaml" text="View the full object model">}}

## Authentication

The API uses {{<exlink url="https://developer.konghq.com/plugins/basic-auth/" text="Kong Basic Auth">}} for API access. The default username and passwords vary according to your deployment:

- NVLink-only deployment: during the installation process, NetQ creates two users that are authorized to interact with the API: `ro-user` and `rw-user`. The `ro-user` is authorized to perform read-only operations, which correspond to GET requests. The `rw-user` is authorized to access all API endpoints, including GET, POST, PUT, DELETE, and PATCH requests.

- Ethernet and NVLink combined deployment: during the installation process, NetQ creates the default username and password, *admin*, *admin*. Upon {{<link title="Access the NetQ UI" text="initial login">}}, the NetQ UI will prompt you to change the default values. The admin has read-write access and can {{<link title="Add and Manage Accounts" text="create additional accounts">}}. The username, password, and access level are specified during the account creation process.

## Asynchronous Operations

Some REST API calls involve asynchronous, long-running tasks. When one of these APIs is invoked, it immediately returns a `202 Accepted` response. This indicates that the request has been received and is being processed, but the operation is not yet complete. Each `202` response includes:

- A JSON body with an `operationID` (for example, `"operationId": "551137c2f9e1fac808a5f572"`)
- A location header that points to the operations API endpoint at `/nmx/v1/operations/<op-id>`

If the operation eventually creates a new resource (for example, a service), querying the operation once its status is completed returns a response containing a location header pointing to the new resource endpoint (for example, `/nmx/v1/services/<created-service-id>`).

## API Responses

The NetQ NVLink API uses conventional HTTP response codes to indicate the success or failure of an API request:

| Code | Name | Description |
| ---- | ---- | ----|
| 200 | Success | Request was successfully processed. |
| 400  | Bad Request | Invalid input was detected in request. |
| 401  | Unauthorized | Authentication has failed or credentials were not provided. |
| 403  | Forbidden | Request was valid, but user might not have the necessary permissions. |
| 404  | Not Found | Requested resource could not be found. |
| 409  | Conflict | Request cannot be processed due to conflict in current state of the resource. |
| 500  | Internal Server Error | Unexpected condition has occurred. |
| 503  | Service Unavailable | The service being requested is currently unavailable. |

## Limitations

The NetQ NVLink REST API contains fields that use the numeric `uint64` format. Because tools like Swagger have limited JSON parsing capabilities, they cannot handle these large values correctly. This issue arises because Swagger relies on the native JavaScript `JSON.parse` method, which cannot accurately interpret 64-bit integers.

To address this limitation, pre-process any JSON data containing `uint64` values before handling it in browser-based applications:

```
const preprocessed = jsonAsString.replace(/:\s*(\d{16,})/g, ': "$1"');
const result = JSON.parse(preprocessed, (key, value) => typeof value === 'string' && /:\s*(\d{16,})/g.test(value) ? BigInt(value) : value)
```

Responses from certain endpoints can be very large, which may result in slow loading, unresponsiveness, or even browser freezes. This limitation stems from browser and JavaScript processing constraints. For handling large-scale data, use dedicated tools such as Insomnia, Postman, or the command line.

Additionally, complex schemas with deeply nested structures can cause rendering issues.