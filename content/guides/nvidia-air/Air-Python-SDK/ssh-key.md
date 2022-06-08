---
menu: main
product: AIR SDK
title: SSH Key
---

# Table of Contents

* [air\_sdk.ssh\_key](#air_sdk.ssh_key)
  * [SSHKey](#air_sdk.ssh_key.SSHKey)
  * [SSHKeyApi](#air_sdk.ssh_key.SSHKeyApi)
    * [list](#air_sdk.ssh_key.SSHKeyApi.list)
    * [create](#air_sdk.ssh_key.SSHKeyApi.create)

SSH Key module

<a name="air_sdk.ssh_key.SSHKey"></a>
## SSHKey

Manage a SSH Key

### delete
Delete the key. Once successful, the object should no longer be used and will raise
[`AirDeletedObject`](/docs/exceptions) when referenced.

**Raises**:

  [`AirUnexpectedResposne`](/docs/exceptions) - Delete failed
  
  ### json
  Returns a JSON string representation of the key
  
  ### refresh
  Syncs the key with all values returned by the API

<a name="air_sdk.ssh_key.SSHKeyApi"></a>
## SSHKeyApi

High-level interface for the SSHKey API

<a name="air_sdk.ssh_key.SSHKeyApi.list"></a>
### list

List existing keys

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
>>> air.ssh_keys.list()
[<SSHKey mykey c51b49b6-94a7-4c93-950c-e7fa4883591>, <SSHKey test_key 3134711d-015e-49fb-a6ca-68248a8d4aff>]
```

<a name="air_sdk.ssh_key.SSHKeyApi.create"></a>
### create

Add a new public key to your account

**Arguments**:

- `name` _str_ - Descriptive name for the public key
- `public_key` _str_ - Public key
- `kwargs` _dict, optional_ - All other optional keyword arguments are applied as key/value
  pairs in the request's JSON payload
  

**Returns**:

  [`SSHKey`](/docs/sshkey)
  

**Raises**:

  [`AirUnexpectedResposne`](/docs/exceptions) - API did not return a 200 OK
  or valid response JSON
  

**Example**:

```
>>> air.ssh_keys.create(name='my_pub_key', public_key='<key_string>')
<SSHKey my_pub_key 01298e0c-4ef1-43ec-9675-93160eb29d9f>
```

