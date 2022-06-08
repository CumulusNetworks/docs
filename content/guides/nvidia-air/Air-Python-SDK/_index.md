---
menu: main
product: AIR SDK
title: Air Python SDK
weight: 999
---

# cumulus_air_sdk

This project provides a Python SDK for interacting with the NVIDIA Air API (https://air.nvidia.com/api/).

[Click here for the full documentation](https://cumulus-consulting.gitlab.io/air/cumulus_air_sdk/docs/)

## Prerequisite

The SDK requires python 3.7 or later. The safest way to install the SDK is to set up a virtual environment in python3.7:

```
apt-get install python3.7
```

```
python3.7 -m pip install virtualenv
```

```
python3.7 -m virtualenv venv37
```

```
. venv37/bin/activate
```

## Installation

To install the SDK, use pip. Either command will work below based on context.

If using the modernized python3 method:

```
python3.7 -m pip install git+https://gitlab.com/cumulus-consulting/air/cumulus_air_sdk.git
```

If using the pip3 method:

```
pip3 install git+https://gitlab.com/cumulus-consulting/air/cumulus_air_sdk.git
```


## Usage

```
>>> from air_sdk import AirApi
>>> air = AirApi(username='<user>', password='<password>')
```

## Authentication Options

Using the API requires the use of either an API token, a username/password, or a bearer token.

### API token

To use an API token, one must first be generated. The easiest way to do this is via the [Air UI](https://air.nvidia.com/settings/api-tokens).

Once a token is generated:

```
>>> air = AirApi(username='<username>', password='<api_token>')
```

### Username/Password

To use a username/password, an administrator of NVIDIA Air must provision a service account. Once the administrator provides the username and password:

```
>>> air = AirApi(username='<username>', password='<password>')
```

### Bearer token

Generally, it's recommended to use an [API Token](#api-token) over a bearer token. However, a bearer token might be used for testing or quick-and-dirty operations that might not need a long term API token. To use a bearer token, the calling user must have a nvidia.com account and have previously approved access for NVIDIA Air. Once a token is obtained:

```
>>> air = AirApi(bearer_token='<bearer_token>')
```

### Interacting with the API

The SDK provides various helper methods for interacting with the API. For example:

```
>>> air.simulations.list()
[<Simulation sim1 c51b49b6-94a7-4c93-950c-e7fa4883591>, <Simulation sim2 3134711d-015e-49fb-a6ca-68248a8d4aff>]
>>> sim1 = air.simulations.get('c51b49b6-94a7-4c93-950c-e7fa4883591')
>>> sim1.title = 'My Sim'
>>> sim1.store()
```

## Developing

Contributions to the SDK are very welcome. All code must pass linting and unit testing before it will be merged.

### Requirements

```
pip3 install -r requirements-dev.txt
```

### Linting

```
pylint **/*.py
```

### Unit testing

```
./unit_test.sh
```

### Generating docs

```
pydoc-markdown
```
