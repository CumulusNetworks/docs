---
title: Using the watch Command
author: NVIDIA
weight: 378
toc: 4
---

The `watch` command allows you to continuously run any Linux command in fullscreen. It also allows for changing the timing between the command runs as well as highlighting the differences between each run.

## Parameters

Use the `-n` option to set the interval in seconds between each running of the command. (`-n0` sets the interval to .1 seconds, which is the fastest available refresh rate; the default interval is 2 seconds and the longest interval is 4294 seconds).

Use the `--differences` option to highlight the changes between command runs.

## Examples
<!-- vale off -->
### cl-rctl ip route
<!-- vale on -->
This command displays the Cumulus Linux routing table.

    watch -n0 --differences sudo cl-rctl ip route

{{<img src="/images/knowledge-base/watch-command-cl-rctl_ip_route.gif" alt="watch command for cl-rctl ip route">}}

### ip -s link show up

This command displays interface packet counters.

    watch -n0 --differences sudo ip -s link show up

{{<img src="/images/knowledge-base/watch-command-ip-s_link_show_up.gif" alt="watch command for ip dash s link show">}}
