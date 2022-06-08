---
menu: main
product: AIR SDK
title: API Token
---

# Table of Contents

* [air\_sdk.api\_token](#air_sdk.api_token)
  * [Token](#air_sdk.api_token.Token)
  * [TokenApi](#air_sdk.api_token.TokenApi)
    * [list](#air_sdk.api_token.TokenApi.list)
    * [create](#air_sdk.api_token.TokenApi.create)
    * [delete](#air_sdk.api_token.TokenApi.delete)

SSH Key module

<a name="air_sdk.api_token.Token"></a>
## Token

Manage an API Token

<a name="air_sdk.api_token.TokenApi"></a>
## TokenApi

High-level interface for the Token API

<a name="air_sdk.api_token.TokenApi.list"></a>
### list

List existing tokens

**Arguments**:

- `kwargs` _dict, optional_ - All other optional keyword arguments are applied as query
  parameters/filters
  

**Returns**:

  list
  

**Raises**:

  [`AirUnexpectedResponse`](/docs/exceptions) - API did not return a 200 OK
  or valid response JSON
  

**Example**:

```
>>> air.api_tokens.list()
[<Token mytoken c51b49b6-94a7-4c93-950c-e7fa4883591>, <Token test_token 3134711d-015e-49fb-a6ca-68248a8d4aff>]
```

<a name="air_sdk.api_token.TokenApi.create"></a>
### create

Add a new api token to your account

**Arguments**:

- `name` _str_ - Descriptive name for the public key
- `kwargs` _dict, optional_ - All other optional keyword arguments are applied as key/value
  pairs in the request's JSON payload
  

**Returns**:

  [`Token`](/docs/token)
  

**Raises**:

  [`AirUnexpectedResposne`](/docs/exceptions) - API did not return a 200 OK
  or valid response JSON
  

**Example**:

```
>>> air.api_tokens.create(name='my_api_token')
<Token my_api_token 01298e0c-4ef1-43ec-9675-93160eb29d9f>
```

<a name="air_sdk.api_token.TokenApi.delete"></a>
### delete

Delete the token

**Arguments**:

- `kwargs` _dict, optional_ - All other optional keyword arguments are applied as query
  parameters/filters
  

**Returns**:

  string
  

**Raises**:

  [`AirUnexpectedResposne`](/docs/exceptions) - Received an unexpected response 
  from the Cumulus AIR API (404): {"detail":"Not found."}
  

**Example**:

```
>>> air.api_tokens.delete()
'SUCCESS'
```

