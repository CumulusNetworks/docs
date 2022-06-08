---
menu: main
product: AIR SDK
title: Login
---

# Table of Contents

* [air\_sdk.login](#air_sdk.login)
  * [Login](#air_sdk.login.Login)
  * [LoginApi](#air_sdk.login.LoginApi)
    * [get](#air_sdk.login.LoginApi.get)
    * [list](#air_sdk.login.LoginApi.list)

Login module

<a name="air_sdk.login.Login"></a>
## Login

View login information

### json
Returns a JSON string representation of the login info

### refresh
Syncs the login info with all values returned by the API

<a name="air_sdk.login.LoginApi"></a>
## LoginApi

High-level interface for the Login API

<a name="air_sdk.login.LoginApi.get"></a>
### get

Get login information or start an OAuth request. This is equivalent to `login.list()`.

**Arguments**:

- `kwargs` _dict, optional_ - All other optional keyword arguments are applied as query
  parameters/filters
  

**Returns**:

  [`Login`](/docs/login)
  

**Raises**:

  [`AirUnexpectedResposne`](/docs/exceptions) - API did not return a 200 OK
  or valid response JSON
  

**Example**:

```
>>> air.login.get()
<Login>
```

<a name="air_sdk.login.LoginApi.list"></a>
### list

Get login information or start an OAuth request. This is equivalent to `login.get()`.

**Arguments**:

- `kwargs` _dict, optional_ - All other optional keyword arguments are applied as query
  parameters/filters
  

**Returns**:

  [`Login`](/docs/login)
  

**Raises**:

  [`AirUnexpectedResposne`](/docs/exceptions) - API did not return a 200 OK
  or valid response JSON
  

**Example**:

```
>>> air.login.get()
<Login>
```

