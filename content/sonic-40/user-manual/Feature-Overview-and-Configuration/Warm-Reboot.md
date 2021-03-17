---
title: Warm Reboot
author: Cumulus Networks
weight: 52
product: SONiC
version: 4.0
siteSlug: sonic
---

Warn reboot enables the user to restart and upgrade SONiC software without impacting the data plane. If using SONiC 201811 versions, sub second traffic loss may occur during the warm reboot. In SONiC 201911 versions, due to the advantages provided by the NVIDIA Mellanox Spectrum ASICs, warm reboot solution can achieve 0 packet loss during SONiC OS (including SDK/FW) upgrade and warm reboot.

Control plane downtime requirements as well as scaling requirements are the same as in Fast-Reboot.

{{% notice info%}}

Warn reboot is designed and maintained for T0 only.

{{%/notice%}}

To check if warm reboot is enabled:

```
root@sonic:~# show platform mlnx issu
ISSU is not enabled on this HWSKU
Warm reboot is not supported
```

If warm reboot is not enabled although it is supported by your platform, edit the SAI profile to enable it manually.

1. Open the `/usr/share/sonic/device/{platform name}/{sku name}/sai_{platform}.xml` file, (e.g. `/usr/share/sonic/device/x86_64-mlnx_msn2700-r0/ACS-MSN2700/sai_2700.xml`).
2. Set "issue-enabled" to _1_.

       <issu-enabled>1</issu-enabled>

For more configurations, please refer to this link: https://github.com/Azure/sonic-utilities/blob/201911/doc/Command-Refeence.md#warm-reboot
