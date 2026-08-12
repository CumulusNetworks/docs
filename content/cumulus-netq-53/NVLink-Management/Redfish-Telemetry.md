---
title: Sensor Events and Notifications
author: NVIDIA
weight: 850
toc: 4
---

The {{<exlink url="https://en.wikipedia.org/wiki/Redfish_(specification)" text="Redfish">}} REST endpoints detect and report leak events in liquid-cooling equipment using the Redfish Baseboard Management Controller (BMC). NetQ NVLink connects to the {{<exlink url="https://docs.nvidia.com/networking/display/nvidiaswitchbmcusermanualv8800020956/overview" text="BMCs on NVIDIA switches">}} and GPU compute nodes using their Redfish-compatible REST APIs.

{{%notice note%}}
NetQ NVLink supports leakage sensor events exclusively; events from other sensor URIs are ignored.
{{%/notice%}}

## Register a BMC Redfish Endpoint

To begin monitoring leak events for a switch, register the designated Redfish endpoint of the BMC assigned to that switch:

1. {{<link title="NVLink Bringup/#switch-profile-endpoints" text="Create a switch profile">}}. Make a POST request to the `/v1/switch-profiles` endpoint using the {{<exlink url="https://docs.nvidia.com/networking/display/nvidiaswitchbmcusermanualv8800020956/getting+started#src-3832573619_GettingStarted-LoginCredentials" text="BMC username and password">}}. Copy the `ProfileID` from the response body.

2. Make a POST request to the `/v1/redfish` endpoint using the `ProfileID` from the previous step. You can either specify a global profile ID or an individual profile ID for each endpoint. Note that individual profile IDs override global profile IDs for any given endpoint. You can optionally specify a port or use the default value (443).

3. If all initial validations succeed, the API returns an `HTTP 202 Accepted` response with a JSON body containing an operation ID. You can make a GET request to the `/v1/operations` endpoint to track the progress of the registration.

After the endpoint is successfully registered, the `status` field changes from `pending` to `active`. NetQ NVLink establishes an HTTPS mTLS connection and subscribes to the {{<link title="Manage Alerts/#leak-sensor-notifications" text="BMC Redfish events">}}. You can send GET request to `/v1/redfish` to list all registered endpoints. 

## Example

The following example shows a leak event on a switch:

```
{
  "labels": {
    "alertname": "RedfishEventNotification",
    "job":       "webhook-gateway",
    "endpoint":  "6836d33b-0001-0000-0000-000000000001",
    "uid":       "42",
    "device":    "switch",
    "sensor":    "LeakageDetectors",
    "uri":       "/redfish/v1/Chassis/1U/ThermalSubsystem/LeakDetection/LeakDetectors/leakage_aggr"
  },
  "annotations": {
    "summary":     "Redfish LeakageDetectors alert on switch UID 42",
    "description": "LeakageDetectors sensor alert for Redfish Endpoint 6836d33b-0001-0000-0000-000000000001 on switch 42 at /redfish/v1/Chassis/1U/ThermalSubsystem/LeakDetection/LeakDetectors/leakage_aggr: Leak detected at cooling manifold",
    "event_type":  "Alert",
    "message":     "Leak detected at cooling manifold",
    "uuid":        "c0a80100-0000-0000-0000-000000000042"
  },
  "startsAt": "2026-04-07T10:00:00Z"
}
```
