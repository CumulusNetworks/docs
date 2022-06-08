---
menu: main
product: AIR SDK
title: Image
---

# Table of Contents

* [air\_sdk.image](#air_sdk.image)
  * [Image](#air_sdk.image.Image)
    * [upload](#air_sdk.image.Image.upload)
  * [ImageApi](#air_sdk.image.ImageApi)
    * [get](#air_sdk.image.ImageApi.get)
    * [list](#air_sdk.image.ImageApi.list)
    * [create](#air_sdk.image.ImageApi.create)

Image module

<a name="air_sdk.image.Image"></a>
## Image

Manage an Image

### delete
Delete the image. Once successful, the object should no longer be used and will raise
[`AirDeletedObject`](/docs/exceptions) when referenced.

**Raises**:

  [`AirUnexpectedResposne`](/docs/exceptions) - Delete failed
  
  ### json
  Returns a JSON string representation of the image
  
  ### refresh
  Syncs the image with all values returned by the API
  
  ### update
  Update the image with the provided data
  

**Arguments**:

- `kwargs` _dict, optional_ - All optional keyword arguments are applied as key/value
  pairs in the request's JSON payload

<a name="air_sdk.image.Image.upload"></a>
### upload

Upload an image file

**Arguments**:

- `filename` _str_ - Absolute path to the local image
  

**Raises**:

  [`AirUnexpectedResposne`](/docs/exceptions) - Upload failed

<a name="air_sdk.image.ImageApi"></a>
## ImageApi

High-level interface for the Image API

<a name="air_sdk.image.ImageApi.get"></a>
### get

Get an existing image

**Arguments**:

- `image_id` _str_ - Image ID
- `kwargs` _dict, optional_ - All other optional keyword arguments are applied as query
  parameters/filters
  

**Returns**:

  [`Image`](/docs/image)
  

**Raises**:

  [`AirUnexpectedResposne`](/docs/exceptions) - API did not return a 200 OK
  or valid response JSON
  

**Example**:

```
>>> air.images.get('3dadd54d-583c-432e-9383-a2b0b1d7f551')
<Image cumulus-vx-4.2.1 3dadd54d-583c-432e-9383-a2b0b1d7f551>
```

<a name="air_sdk.image.ImageApi.list"></a>
### list

List existing images

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
>>> air.images.list()
[<Image cumulus-vx-4.2.1 c51b49b6-94a7-4c93-950c-e7fa4883591>, <Image generic/ubuntu18.04 3134711d-015e-49fb-a6ca-68248a8d4aff>]
```

<a name="air_sdk.image.ImageApi.create"></a>
### create

Create a new image

**Arguments**:

- `name` _str_ - Image name
- `organization` _str | `Organization`_ - `Organization` or ID
- `filename` _str, optional_ - Absolute path to the local file which should be uploaded
- `kwargs` _dict, optional_ - All other optional keyword arguments are applied as key/value
  pairs in the request's JSON payload
  

**Returns**:

  [`Image`](/docs/image)
  

**Raises**:

  [`AirUnexpectedResposne`](/docs/exceptions) - API did not return a 200 OK
  or valid response JSON
  

**Example**:

```
>>> air.images.create(name='my_image', filename='/tmp/my_image.qcow2', agent_enabled=False)
<Image my_image 01298e0c-4ef1-43ec-9675-93160eb29d9f>
```

