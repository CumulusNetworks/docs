---
title: NMX-M API User Guide
author: NVIDIA
weight: 1005
toc: 3
---

The NMX-M API is organized around {{<exlink url="https://en.wikipedia.org/wiki/REST" text="REST">}} and conforms with {{<exlink url="https://spec.openapis.org/oas/v3.0.3" text="OpenAPI Specification v3.0.3">}}. The API provides access to resources and functionalities <!--which ones?--> through a set of defined endpoints. Each endpoint has its own schema, which includes the payload, parameters, and the expected request/response formats.

<!--update these links-->
- {{<exlink url="https://docs.nvidia.com/networking-ethernet-software/nmx-api-8513100/" text="NMX-M REST API in Swagger">}}
- {{<exlink url="https://docs.nvidia.com/networking-ethernet-software/nmx-api-8513100/openapi.yaml" text="View the full object model">}}

This guide provides an overview of the NMX-M API framework, including the basics of using Swagger UI 2.0 or `bash` plus `curl` to view and test the APIs. Descriptions of each endpoint and model parameter are in individual API JSON files.

## Authentication

The NMX-M API uses {{<exlink url="https://developer.konghq.com/plugins/basic-auth/" text="Kong Basic Auth">}} for API access. During the installation process, NetQ creates two users that are authorized to interact with the API: `ro-user` and `rw-user`. The `ro-user` is authorized to perform read-only operations, which correspond to GET requests. The `rw-user` is authorized to access all API endpoints, including GET, POST, PUT, DELETE, and PATCH requests. <!--what about admin, admin?-->

{{< expand "Read-only example using cURL" >}}
```
curl -X 'GET' \ 
  'https://<ip_address>/nmx/v1/compute-nodes' \ 
  -u ro-user:ro-password 
```
{{< /expand >}}

{{< expand "Read-write example using cURL" >}}
```
curl -X 'PUT' \ 
  'https://<ip_address>/nmx/v1/compute-nodes/<id>' \ 
  -H 'accept: application/json' \ 
  -H 'Content-Type: application/json' \ 
  -u rw-user:rw-password \ 
  -d '{ 
  "Description": "Some New Description", 
  "Name": "Some New Name" 
}
```
{{< /expand >}}

### API Responses

An NMX-M API response comprises a status code, any relevant error codes (if unsuccessful), and the collected data (if successful). NMX-M uses conventional HTTP response codes to indicate the success or failure of an API request:

| Code | Name | Description | Action |
| ---- | ---- | ----| ---- |
| 200 | Success | Request was successfully processed. | Review response. |
| 400  | Bad Request | Invalid input was detected in request. | Check the syntax of your request and make sure it matches the schema. |
| 401  | Unauthorized | Authentication has failed or credentials were not provided. | Provide or verify your credentials, or request access from your administrator. |
| 403  | Forbidden | Request was valid, but user might not have the needed permissions. | Verify your credentials or request an account from your administrator. |
| 404  | Not Found | Requested resource could not be found. | Try the request again after a period of time or verify status of resource. |
| 409  | Conflict | Request cannot be processed due to conflict in current state of the resource. | Verify status of resource and remove conflict. |
| 500  | Internal Server Error | Unexpected condition has occurred. | Perform general troubleshooting and try the request again. |
| 503  | Service Unavailable | The service being requested is currently unavailable. | Verify the status of the NetQ Platform or appliance, and the associated service. |