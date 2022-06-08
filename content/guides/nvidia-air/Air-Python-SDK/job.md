---
menu: main
product: AIR SDK
title: Job
---

# Table of Contents

* [air\_sdk.job](#air_sdk.job)
  * [Job](#air_sdk.job.Job)
  * [JobApi](#air_sdk.job.JobApi)
    * [get](#air_sdk.job.JobApi.get)
    * [list](#air_sdk.job.JobApi.list)

Job module

<a name="air_sdk.job.Job"></a>
## Job

Manage a Job

### json
Returns a JSON string representation of the job

### refresh
Syncs the job with all values returned by the API

### update
Update the job with the provided data

**Arguments**:

- `kwargs` _dict, optional_ - All optional keyword arguments are applied as key/value
  pairs in the request's JSON payload

<a name="air_sdk.job.JobApi"></a>
## JobApi

High-level interface for the Job API

<a name="air_sdk.job.JobApi.get"></a>
### get

Get an existing job

**Arguments**:

- `job_id` _str_ - Job ID
- `kwargs` _dict, optional_ - All other optional keyword arguments are applied as query
  parameters/filters
  

**Returns**:

  [`Job`](/docs/job)
  

**Raises**:

  [`AirUnexpectedResposne`](/docs/exceptions) - API did not return a 200 OK
  or valid response JSON
  

**Example**:

```
>>> air.jobs.get('3dadd54d-583c-432e-9383-a2b0b1d7f551')
<Job START 3dadd54d-583c-432e-9383-a2b0b1d7f551>
```

<a name="air_sdk.job.JobApi.list"></a>
### list

List existing jobs

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
>>> air.jobs.list()
[<Job START c51b49b6-94a7-4c93-950c-e7fa4883591>, <Job STOP 3134711d-015e-49fb-a6ca-68248a8d4aff>]
```

