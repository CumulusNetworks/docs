---
title: FIPS
author: NVIDIA
weight: 192
toc: 4
---
<span class="a-tooltip">[FIPS](## "Federal Information Processing Standards")</span> are standards for federal computer systems and information developed by the U.S. government and published by the National Institute of Standards and Technology (NIST).

## Configure FIPS Mode

To enable FIPS mode on the switch, run the `nv set system security fips mode enabled` command:

```
cumulus@switch:~$ nv set system security fips mode enabled
cumulus@switch:~$ nv config apply
```

To disable FIPS mode, run the `nv set system security fips mode disabled` command. You can also run the `nv unset system security fips` command to restore FIPS to the default mode, which is `disabled`.

## Show FIPS Configuration

To show if FIPS mode is configured, run the `nv show system security fips` command:

```
cumulus@switch:~$ nv show system security fips
                           operational  applied
-------------------------  -----------  -------
mode                       enabled      enabled
```

The `nv show system security` command shows if FIPS mode is enabled in addition to other security options.

```
cumulus@switch:~$ nv show system security
                           operational  applied
-------------------------  -----------  -------
fips
  mode                     enabled      enabled
password-hardening
  state                    enabled      enabled
  reject-user-passw-match  enabled      enabled
  lower-class              enabled      enabled
  upper-class              enabled      enabled
  digits-class             enabled      enabled
  special-class            enabled      enabled
  expiration-warning       15           15
  expiration               180          180
  history-cnt              10           10
  len-min                  8            8
encryption
  db
    state                               enabled
```
