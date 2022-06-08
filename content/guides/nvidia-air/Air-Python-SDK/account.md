---
menu: main
product: AIR SDK
title: Account
---

# Table of Contents

* [air\_sdk.account](#air_sdk.account)
  * [Account](#air_sdk.account.Account)
  * [AccountApi](#air_sdk.account.AccountApi)
    * [get](#air_sdk.account.AccountApi.get)
    * [list](#air_sdk.account.AccountApi.list)

Account module

<a name="air_sdk.account.Account"></a>
## Account

Manage an Account
### json
Returns a JSON string representation of the account

### refresh
Syncs the account with all values returned by the API

<a name="air_sdk.account.AccountApi"></a>
## AccountApi

High-level interface for the Account API

<a name="air_sdk.account.AccountApi.get"></a>
### get

Get an existing account

**Arguments**:

- `account_id` _str_ - Account ID
- `kwargs` _dict, optional_ - All other optional keyword arguments are applied as query
  parameters/filters
  

**Returns**:

  [`Account`](/docs/account)
  

**Raises**:

  [`AirUnexpectedResposne`](/docs/exceptions) - API did not return a 200 OK
  or valid response JSON
  

**Example**:

```
>>> air.accounts.get('3dadd54d-583c-432e-9383-a2b0b1d7f551')
<Account mrobertson@nvidia.com 3dadd54d-583c-432e-9383-a2b0b1d7f551>
```

<a name="air_sdk.account.AccountApi.list"></a>
### list

List existing accounts

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
>>> air.accounts.list()
[<Account mrobertson@nvidia.com c51b49b6-94a7-4c93-950c-e7fa4883591>, <Account nmitchell@nvidia.com 3134711d-015e-49fb-a6ca-68248a8d4aff>]
```

