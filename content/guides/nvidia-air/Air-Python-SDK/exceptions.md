---
menu: main
product: AIR SDK
title: Exceptions
---

# Table of Contents

* [air\_sdk.exceptions](#air_sdk.exceptions)
  * [AirError](#air_sdk.exceptions.AirError)
  * [AirAuthorizationError](#air_sdk.exceptions.AirAuthorizationError)
  * [AirUnexpectedResponse](#air_sdk.exceptions.AirUnexpectedResponse)
  * [AirForbiddenError](#air_sdk.exceptions.AirForbiddenError)
  * [AirObjectDeleted](#air_sdk.exceptions.AirObjectDeleted)

Custom exceptions for the AIR SDK

<a name="air_sdk.exceptions.AirError"></a>
## AirError

Base exception class. All custom exceptions should inherit from this class.

<a name="air_sdk.exceptions.AirAuthorizationError"></a>
## AirAuthorizationError

Raised when authorization with the API fails.

<a name="air_sdk.exceptions.AirUnexpectedResponse"></a>
## AirUnexpectedResponse

Raised when the API returns an unexpected response.

<a name="air_sdk.exceptions.AirForbiddenError"></a>
## AirForbiddenError

Raised when an API call returns a 403 Forbidden error

<a name="air_sdk.exceptions.AirObjectDeleted"></a>
## AirObjectDeleted

Raised when accessing a previously instantiated object that has since been deleted

