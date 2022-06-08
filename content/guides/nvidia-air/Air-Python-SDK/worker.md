---
menu: main
product: AIR SDK
title: Worker
---

# Table of Contents

* [air\_sdk.worker](#air_sdk.worker)
  * [Worker](#air_sdk.worker.Worker)
    * [set\_available](#air_sdk.worker.Worker.set_available)
  * [WorkerApi](#air_sdk.worker.WorkerApi)
    * [get](#air_sdk.worker.WorkerApi.get)
    * [list](#air_sdk.worker.WorkerApi.list)
    * [create](#air_sdk.worker.WorkerApi.create)

Worker module

<a name="air_sdk.worker.Worker"></a>
## Worker

Manage a Worker

### json
Returns a JSON string representation of the worker

### refresh
Syncs the worker with all values returned by the API

### update
Update the worker with the provided data

**Arguments**:

- `kwargs` _dict, optional_ - All optional keyword arguments are applied as key/value
  pairs in the request's JSON payload

<a name="air_sdk.worker.Worker.set_available"></a>
### set\_available

Sets a worker's `available` value in AIR

**Arguments**:

  available (bool)

<a name="air_sdk.worker.WorkerApi"></a>
## WorkerApi

High-level interface for the Worker API

<a name="air_sdk.worker.WorkerApi.get"></a>
### get

Get an existing worker

**Arguments**:

- `worker_id` _str_ - Worker ID
- `kwargs` _dict, optional_ - All other optional keyword arguments are applied as query
  parameters/filters
  

**Returns**:

  [`Worker`](/docs/worker)
  

**Raises**:

  [`AirUnexpectedResposne`](/docs/exceptions) - API did not return a 200 OK
  or valid response JSON
  

**Example**:

```
>>> air.workers.get('3dadd54d-583c-432e-9383-a2b0b1d7f551')
<Worker worker01 3dadd54d-583c-432e-9383-a2b0b1d7f551>
```

<a name="air_sdk.worker.WorkerApi.list"></a>
### list

List existing workers

**Arguments**:

- `kwargs` _dict, optional_ - All other optional keyword arguments are applied as query
  parameters/filters
  

**Returns**:

  list
  

**Raises**:

  [`AirUnexpectedResposne`](/docs/exceptions) - API did not return a 200 OK
  or valid response JSON
  

**Example**:

```
>>> air.workers.list()
[<Worker worker01 c51b49b6-94a7-4c93-950c-e7fa4883591>, <Worker worker02 3134711d-015e-49fb-a6ca-68248a8d4aff>]
```

<a name="air_sdk.worker.WorkerApi.create"></a>
### create

Create a new worker

**Arguments**:

- `cpu` _int_ - Number of vCPUs the worker can support
- `memory` _int_ - Amount of memory (in MB) a worker can support
- `storage` _int_ - Amount of storage (in GB) a worker can support
- `ip_address` _str_ - Internal IP address
- `port_range` _str_ - Range of ports available on the worker
- `username` _str_ - Worker username for API access
- `password` _str_ - Worker password for API access
- `kwargs` _dict, optional_ - All other optional keyword arguments are applied as key/value
  pairs in the request's JSON payload
  

**Returns**:

  [`Worker`](/docs/worker)
  

**Raises**:

  [`AirUnexpectedResposne`](/docs/exceptions) - API did not return a 200 OK
  or valid response JSON
  

**Example**:

```
>>> air.workers.create(cpu=100, memory=200000, storage=1000, ip_address='10.1.1.1', port_range='10000-30000', username='worker01', password='secret')
<Worker my_sim 01298e0c-4ef1-43ec-9675-93160eb29d9f>
```

