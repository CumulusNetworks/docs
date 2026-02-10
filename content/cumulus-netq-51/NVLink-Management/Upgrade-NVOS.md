---
title: Upgrade NVOS
author: NVIDIA
weight: 850
toc: 4
---

Use the REST API to upgrade NVOS on your switches. First, create a switch profile, then upload the NVOS image and track the progress of the upgrade.

## Requirements

- Download the NVOS image from the {{<exlink url="https://enterprise-support.nvidia.com/s/" text="NVIDIA Enterprise Support Portal">}}.
- Only the admin or read-write user (`rw-user`) can perform the steps in this section.

## Upgrade NVOS 

You can upgrade NVOS at either the switch-level or domain-level. Switch-level operations are prioritized before domain-level operations.

{{<tabs "TabID129" >}}
{{<tab "Switch-level upgrade"  >}}

1. Authenticate your credentials by {{<link title="NVLink Bringup/#switch-profile-endpoints" text="creating a switch profile">}}. Make a POST request to the `/v1/switch-profiles` endpoint that contains your username and password. Copy the `ProfileID` from the response body.

2. Upload the NVOS image by making a POST request to the `/v1/images` endpoint. After the image is successfully uploaded, the response body returns an `ImageID`.

3. Make a POST request to the `/v1/upgrade-switch` endpoint; select **switch-based upgrade** and include the `ProfileID` and `ImageID` from the previous steps, in addition to the IP addresses of the switches you want to upgrade.

4. If all initial validations succeed, the API returns an `HTTP 202 Accepted` response with a JSON body containing an operation ID. You can make a GET request to the `/v1/operations/` endpoint to track the progress of the upgrade.

{{</tab>}}
{{<tab "Domain-level upgrade" >}}

1. Authenticate your credentials by {{<link title="NVLink Bringup/#switch-profile-endpoints" text="creating a switch profile">}}. Make a POST request to the `/v1/switch-profiles` endpoint that contains your username and password. Copy the `ProfileID` from the response body.

2. Upload the NVOS image by making a POST request to the `/v1/images` endpoint. After the image is successfully uploaded, the response body returns an `ImageID`.

2. Make a PATCH request to the `/v1/domains/{id}` endpoint to create an association between the profile ID from the first step and a given domain. The response body returns a `DomainID`.

3. Make a POST request to the `/v1/upgrade-switch` endpoint; select **domain-based upgrade** and include the `DomainID` and `ImageID` from the previous steps.

4. If all initial validations succeed, the API returns an `HTTP 202 Accepted` response with a JSON body containing an operation ID. You can make a GET request to the `/v1/operations/` endpoint to track the progress of the upgrade.

{{</tab >}}
{{</tabs>}}