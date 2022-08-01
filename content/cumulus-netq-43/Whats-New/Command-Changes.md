---
title: NetQ CLI Changes
author: NVIDIA
weight: 20
toc: 4
---
## Modified Commands

The following table summarizes the commands that have changed with this release.
<!-- vale off -->
| Updated Command | What Changed | Version |
| --------------- | ------------ | ------- |
| netq [hostname] show events  | Added `level critical` to show critical events. | 4.3.0 |
| netq lcm upgrade [cl-image] <br> netq lcm upgrade netq-image | Changed `name <text-job-name>` to `job-name <text-job-name>`. | 4.3.0 |
| netq install standalone full <br> netq install cluster full <br> netq install opta standalone full <br> netq install opta cluster full | Added `pod-ip-range <text-pod-ip-range>` option to specify a range of IP addresses for the pod. | 4.3.0 |
<!-- vale on -->
