---
title: NetQ CLI Changes
author: NVIDIA
weight: 20
toc: 4
---

A number of commands have changed in this release to accommodate the addition of new options or to simplify their syntax. Additionally, new commands have been added and others have been removed. A summary of those changes is provided here.

## New Commands

The following table summarizes the new commands available with this release.

| Command | Summary | Version |
| ------- | ------- | ------- |
| netq |  | 4.0.0 |

## Modified Commands

The following table summarizes the commands that have been changed with this release.

| Updated Command | Old Command | What Changed | Version |
| --------------- | ----------- | ------------ | ------- |
| netq | netq | Added | 4.0.0 |

netq config add agent opta-enable [true|false] – Allow the user to enable/disable OPTA (default true)
netq config add agent gnmi-enable [true|false] – Allow the user to enable/disable gNMI agent (default false)
netq config add agent gnmi-log-level [debug|info|warning|error] – Log verbosity for gNMI agent (default info)
netq config add agent gnmi-port <gnmi_port> - Allow the user to change gNMI port (default 9339)
