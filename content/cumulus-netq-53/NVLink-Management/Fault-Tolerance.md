---
title: Fault Tolerance
author: NVIDIA
weight: 330
toc: 3
---

NetQ provides fault tolerance for NVLink domain management services (NMX-T and NMX-C) on GB200, GB300, and non-HA VR switches. When a management service becomes unavailable, NetQ automatically detects the failure and attempts recovery in the following order:

1. Failover to an alternate IP address: NetQ connects to the next available management IP address on the same switch.
2. Service restart: If no alternate IP address restores connectivity, NetQ stops and restarts the affected service, then verifies that it is healthy before resuming normal operation.

The service restart mechanism requires NetQ to authenticate to the switch using SSH credentials. To enable service restart, create a switch profile and attach it to either a switch node or a domain.

1. Create a switch profile:

```
curl -X 'POST' \
  'https://<ip_address>/nmx/v1/switch-profiles' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "Name": "<profile-name>",
  "Username": "<ssh-username>",
  "Password": "<ssh-password>"
}'
```

Note the `ID` value in the response; you'll need it in the next step.

2. Attach the profile to either a switch node or a domain:

Attach to a switch node:

```
curl -X 'PUT' \
  'https://<ip_address>/nmx/v1/switch-nodes/<switch-node-id>' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "ProfileID": "<switch-profile-id>"
}'
```

Attach to a domain (applies to all switch nodes in the domain):

```
curl -X 'PATCH' \
  'https://<ip_address>/nmx/v1/domains/<domain-id>' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "ProfileID": "<switch-profile-id>"
}'
```

## Disable Fault Tolerance

Fault tolerance is enabled by default for GB200, GB300, and non-HA VR switches and should be disabled for VR switches that are configured with HA. To disable the feature, set `service-failover-enabled` to `false` in `common.yaml`.