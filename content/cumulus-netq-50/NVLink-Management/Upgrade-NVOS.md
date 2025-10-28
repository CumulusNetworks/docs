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

1. Authenticate your credentials by {{<link title="NVLink Bringup/#switch-profile-endpoints" text="creating a switch profile">}}. Make a POST request to the `/v1/switch-profiles` endpoint that contains your username and password. Copy the `ProfileID` from the response body. You will use it in a later step.

2. Upload the NVOS image by making a POST request to the `/v1/images` endpoint. After the image is successfully uploaded, the response body returns an `ImageID`. Copy the ID. You will use it in the next step.

3. Make a POST request to the `/v1/upgrade-switch` endpoint; include the `ProfileID` and `ImageID` from the previous steps, in addition to the IP addresses of the switches you want to upgrade.

4. If all initial validations succeed, the API returns an `HTTP 202 Accepted` response with a JSON body containing an operation ID. You can make a GET request to the `/v1/operations/` endpoint to track the progress of the upgrade.