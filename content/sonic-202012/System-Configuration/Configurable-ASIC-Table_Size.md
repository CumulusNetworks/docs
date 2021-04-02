---
title: Configurable ASIC Table Size
author: NVIDIA
weight: 399
product: SONiC
version: 202012
siteSlug: sonic
draft: true
---

ASIC's internal resources are limited and are shared between several hardware procedures. Due to this, a partitioning scheme for such resource  is expected in order to perform fine tuning for the applications. Such requirement can be done by configuring the ASIC's table size.

By adding or updating the macro definitions in `/usr/share/sonic/device/{platform name}/{sku name}/sai.profile`, the "fdb", "ip route", and "neighbor" table sizes can be updated based on the need.

To change the table size configuration:

1. Determine the desired table size and get it approved by Mellanox.
2. Update the file `/usr/share/sonic/device/{platform name}/{sku name}/sai.profile` on the switch with the approved table size.

   Example of the table size:
   - SAI_FDB_TABLE_SIZE=32768
   - SAI_IPV4_ROUTE_TABLE_SIZE=131072
   - SAI_IPV6_ROUTE_TABLE_SIZE=16384
   - SAI_IPV4_NEIGHBOR_TABLE_SIZE=16384
   - SAI_IPV6_NEIGHBOR_TABLE_SIZE=12288
3. Cold reboot the switch for the changes to take effect.

{{%notice info%}}

Setting incorrect table size may cause a failure at bootup. Changes to the table size must be reviewed by Mellanox personnel.

{{%/notice%}}
