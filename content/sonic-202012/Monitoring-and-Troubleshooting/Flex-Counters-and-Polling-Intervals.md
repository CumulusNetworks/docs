---
title: Flex Counters and Polling Intervals
author: Cumulus Networks
weight: 660
product: SONiC
version: 201911_MUR5
siteSlug: sonic
---

Flex Counters are responsible for polling counters from SAI and storing them in the DB. All the counters are split into Flex Counter Groups based on the object type they are related to (port, queue, etc) and in some cases other factors.

Currently these are the Flex Counter Groups:

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

## Aggregated Bridge Drops Counters

Aggregate Bridge Drops counters per interface are now available via Key/Value setting in the SAI XML, as the `show interface counters` CLI command displays port counters only.

If enabled, the bridge counters are aggregated with the port counters, and the default SONiC L2 traps behavior is changed to keep either standard trap or drop. This prevents drops for L2 traps to be part of the ingress general counter. If disabled, the bridge counters are not aggregated with the port counters, and L2 traps behavior is: trap->trap soft discard, drop->soft discard.

### Enabling Aggregated Bridge Counters

To enable Aggregated Bridge Counters:

1. Edit the SKU SAI profile or create a new SKU.

   An SKU SAI profile can be found on a DUT in the following location: /usr/share/sonic/device/{platform name}/{sku name}/sai.profile,

   For example, the SAI profile for ACS-MSN2700 SKU can be found in /usr/share/sonic/device/x86_64-mlnx_msn2700-r0/ACS-MSN2700/sai.profile,
2. Enable the feature by adding/editing the following Key/Value:

       SAI_AGGREGATE_BRIDGE_DROPS=1
3. Perform a config reload or software reboot for changes to take effect.

## Command Line User Interface

Show running counters configuration

| counterpoll show | Description |
| ----------------- | ----------- |
| counterpoll show | counterpoll [OPTIONS] COMMAND [ARGS]... |
| Options | -?, -h, --help: Show this message and exit. |
| Commands | show: Show the counter configuration<br />port: Port counter commands<br />rif: RIF counter commands<br />queue: Queue counter commands |
| Example | <pre>admin@sonic:~$ counterpoll --help<br />Usage: counterpoll [OPTIONS] COMMAND [ARGS]...<br />  SONiC Static Counter Poll configurations<br />Options:<br />  --help  Show this message and exit.<br />Commands:<br />port       Queue counter commands<br />queue      Queue counter commands<br />rif        RIF counter commands<br />show       Show the counter configuration<br />watermark  Watermark counter commands</pre> |

Enable or disable port counters

| counterpoll port | Description |
| ----------------- | ----------- |
| counterpoll port --help | counterpoll [OPTIONS] COMMAND [ARGS]... |
| Options | -?, -h, --help	Show this message and exit. |
| Commands | show: Show the counter configuration<br />port: Port counter commands<br />rif: RIF counter commands<br />queue: Queue counter commands |
| Example | <pre>admin@sonic:~$ counterpoll port enable<br />counterpoll port disable</pre> |

Change counter polling interval for port group to 10 seconds

| counterpoll port interval | Description |
| ------------------------- | ----------- |
| counterpoll port interval --help | counterpoll port interval [OPTIONS] POLL_INTERVAL |
| Options | -?, -h, --help: Show this message and exit. |
| Example | <pre>admin@sonic:~$  counterpoll port interval 10000</pre> |
