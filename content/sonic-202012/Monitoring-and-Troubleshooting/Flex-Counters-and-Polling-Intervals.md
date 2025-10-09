---
title: Flex Counters and Polling Intervals
author: NVIDIA
weight: 660
product: SONiC
version: 202012
siteSlug: sonic
---

*Flex counters* are responsible for polling counters from SAI and storing them in the database. All the counters are split into *flex counter groups* based on the object type they are related to (such as port or queue) and in some cases other factors.

This table lists the flex counter groups:

| Name | Default polling interval, ms | Comment |
| ---- | ---------------------------- | ------- |
| QUEUE_STAT | 10000 | Queue counters |
| PORT_STAT | 1000 | Port counters |
| PORT_BUFFER_DROP | 60000 | Port Buffer counters |
| RIF_STAT | 1000 | Router interface counters |
| QUEUE_WATERMARK_STAT | 10000 | Queue watermarks |
| PG_WATERMARK_STAT | 10000 | Priority group watermarks |
| BUFFER_POOL_WATERMARK_STAT | 10000 | Buffer pool watermarks |
| PFC_WD | 100 | Used for PFC watchdog feature, not configurable via CLI |

## Aggregated Bridge Drop Counters

*Aggregate bridge drop counters* per interface are available via a key/value setting in the SAI XML, as the `show interface counters` CLI command displays port counters only.

When enabled, the bridge counters are aggregated with the port counters, and the default SONiC L2 traps behavior is changed to keep either a standard trap or drop. This prevents drops for L2 traps to be part of the ingress general counter.

When disabled, the bridge counters are not aggregated with the port counters, and L2 traps behave as follows:

- A trap becomes a trap soft discard.
- A drop becomes a soft discard.

### Enable Aggregated Bridge Counters

To enable aggregated bridge counters:

1. Edit the SKU SAI profile or create a new SKU.

   A SKU SAI profile can be found on a DUT in `/usr/share/sonic/device/{platform name}/{sku name}/sai.profile`.

   For example, the SAI profile for ACS-MSN2700 SKU can be found in `/usr/share/sonic/device/x86_64-mlnx_msn2700-r0/ACS-MSN2700/sai.profile`.
2. Enable the feature by adding/editing the following key/value:

       SAI_AGGREGATE_BRIDGE_DROPS=1
3. Reload the configuration or reboot the switch for the changes to take effect.

## counterpoll CLI

The `counterpoll` command provides tools to enable and disable a counter query as well as set its interval.

To show the running counters, their intervals and whether or not they are enabled, run `counterpoll show`:

```
admin@leaf01:~$ counterpoll show
Type                        Interval (in ms)    Status
--------------------------  ------------------  --------
QUEUE_STAT                  default (10000)     enable
PORT_STAT                   default (1000)      enable
PORT_BUFFER_DROP            default (60000)     enable
QUEUE_WATERMARK_STAT        default (10000)     enable
PG_WATERMARK_STAT           default (10000)     enable
BUFFER_POOL_WATERMARK_STAT  default (10000)     enable
```

You can specify one of the following options with the `counterpoll` command to configure that counter query.

| counterpoll Option | Description |
| ----------------- | ----------- |
| port | Port counter commands. |
| port_buffer_drop | Port buffer drop counter commands. |
| rif | RIF counter commands. |
| queue | Queue counter commands. |
| watermark | Watermark counter commands. |

### Disable a Counter Query

All the counter queries are enabled by default.

To disable the RIF query, for example, run:

    admin@switch:~$ counterpoll rif disable

To enable the RIF query again, run:

    admin@switch:~$ counterpoll rif enable

### Set Polling Intervals

All the counter queries have default polling intervals specified in milliseconds.

To change the counter polling interval for the port counter to 10 seconds, run:

    admin@switch:~$ counterpoll port interval 10000
