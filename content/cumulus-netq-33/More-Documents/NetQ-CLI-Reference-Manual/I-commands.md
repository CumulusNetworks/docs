---
title: I through K Commands
author: NVIDIA
weight: 1104
toc: 3
right_toc_levels: 1
pdfhidden: true
draft: true
---

This topic includes all commands that begin with `netq i*`, `netq j*`, and `netq k*`.

## netq install cluster activate-job

Activates a NetQ instance after an initial on-premises server cluster (master and two worker nodes) is configured.

### Syntax

```
netq install cluster activate-job
    config-key <text-opta-key>
```

## netq install cluster full

netq install cluster full (interface <text-opta-ifname>|ip-addr <text-ip-addr>) bundle<text-bundle-url> [config-key <text-opta-key>] workers <text-worker-01> <text-worker-02>

## netq install cluster init-job

netq install cluster init-job

## netq install cluster join-workers

netq install cluster join-workers <text-worker-01> [<text-worker-02>]

## netq install cluster infra-job

netq install cluster infra-job

## netq install cluster install-job

netq install cluster install-job bundle <text-bundle-url>

## netq install opta activate-job

netq install opta activate-job config-key <text-opta-key>netq install patch <text-tarball-name>

## netq install opta cluster

netq install opta cluster full (interface <text-opta-ifname>|ip-addr <text-ip-addr>) bundle<text-bundle-url> config-key <text-opta-key> workers <text-worker-01> <text-worker-02>[proxy-host <text-proxy-host> proxy-port <text-proxy-port>]

## netq install opta standalone

netq install opta standalone full (interface <text-opta-ifname>|ip-addr <text-ip-addr>)bundle <text-bundle-url> config-key <text-opta-key> [proxy-host <text-proxy-host> proxy-port<text-proxy-port>]

## netq install standalone activate-job

netq install standalone activate-job config-key <text-opta-key>

## netq install standalone full

netq install standalone full (interface <text-opta-ifname>|ip-addr <text-ip-addr>) bundle <text-bundle-url> [config-key <text-opta-key>]

## netq install standalone infra-job

netq install standalone infra-job

## netq install standalone init-job

netq install standalone init-job

## netq install standalone install-job

netq install standalone install-job bundle <text-bundle-url>

## netq install update-settings

netq install update-settings <text-key> <text-value>
