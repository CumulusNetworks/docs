---
title: NetQ CLI Changes
author: NVIDIA
weight: 20
toc: 4
---

## New Commands

The following table summarizes the new commands available with this release.

| Command | Summary | Version |
| ------- | ------- | ------- |
| netq install cluster master-init | Initialize cluster master installation. | 4.2.0 |
| netq install cluster worker-init | Initialize cluster worker installation. | 4.2.0 |
| netq show status | Display installation status. | 4.2.0 |
| netq config add cli proxy | Adds a new proxy server to the CLI configuration. | 4.2.0 |
| netq check roce | Validation for RoCE. | 4.2.0 |
| netq show unit-tests roce | Display validation checks for RoCE. | 4.2.0 |
| netq config [start\|stop\|status\|restart] opta<br>netq config add opta config-key<br>netq config add opta proxy-host<br>netq config del opta proxy-host | On-switch OPTA configuration commands. | 4.2.0 |

## Modified Commands

The following table summarizes the commands that have changed with this release.
<!-- vale off -->
| Updated Command | What Changed | Version |
| --------------- | ------------ | ------- |
| netq config del cli  | Added `proxy` option to remove a proxy server from the CLI configuration. | 4.2.0 |
| netq trace | Added `debug` option to netq trace. | 4.2.0 |
<!-- vale on -->
