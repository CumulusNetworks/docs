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

## netq install cluster

    cluster          :  Install in clustering mode
    opta             :  Only show opta nodes
    patch            :  Patch packaged as a tgz tarball
    standalone       :  Install in non-cluster mode
    update-settings  :  Update admin environment variables

    netq install cluster full (interface <text-opta-ifname>|ip-addr <text-ip-addr>) bundle <text-bundle-url> [config-key <text-opta-key>] workers <text-worker-01> <text-worker-02>

## netq install opta

netq install opta standalone full (interface <text-opta-ifname>|ip-addr <text-ip-addr>) bundle <text-bundle-url> config-key <text-opta-key> [proxy-host <text-proxy-host> proxy-port <text-proxy-port>]
    netq install opta cluster full (interface <text-opta-ifname>|ip-addr <text-ip-addr>) bundle <text-bundle-url> config-key <text-opta-key> workers <text-worker-01> <text-worker-02> [proxy-host <text-proxy-host> proxy-port <text-proxy-port>]

## netq install standalone

netq install standalone full (interface <text-opta-ifname>|ip-addr <text-ip-addr>) bundle <text-bundle-url> [config-key <text-opta-key>]

## 