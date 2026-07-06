---
title: Maintenance Mode
author: NVIDIA
weight: 260
toc: 4
---

Maintenance mode is a low-noise state you enable while performing disruptive operations such as certificate rotation. While on, NetQ NVLink suppresses fault-tolerance recovery and some internal processes so your work does not trigger alerts or automatic recovery actions.

Maintenance mode is a system setting named `maintenance.state`, with a value of `on` or `off` (default `off`). You manage it through the settings API.

## Check the Current State

Send a GET request to `/v1/settings/maintenance.state`:

```
curl -X 'GET' \
  'https://<ip-address>/nmx/v1/settings/maintenance.state' \
  -H 'accept: application/json'
```

A successful request returns `HTTP 200 OK` with the setting:

```
{
  "Name": "maintenance.state",
  "Value": "off",
  "Description": "Maintenance mode state. When enabled, low-noise mode suppresses fault-tolerance and certificate expiration monitoring during certificate rotation.",
  "CreatedAt": "2026-01-15T10:00:00Z",
  "UpdatedAt": "2026-01-15T10:00:00Z"
}
```

## Enable Maintenance Mode

Send a PATCH request to `/v1/settings` with the setting name and a value of `on`:

```
curl -X 'PATCH' \
  'https://<ip-address>/nmx/v1/settings' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{"Name":"maintenance.state","Value":"on"}'
```

A successful request returns `HTTP 200 OK` with the updated setting.

## Disable Maintenance Mode

Send the same PATCH request with a value of `off`:

```
curl -X 'PATCH' \
  'https://<ip-address>/nmx/v1/settings' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{"Name":"maintenance.state","Value":"off"}'
```

A successful request returns `HTTP 200 OK` with the updated setting.