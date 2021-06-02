---
title: Warm Reboot
author: NVIDIA
weight: 240
product: SONiC
version: 202012
siteSlug: sonic
---

Warm reboot enables you to restart and upgrade the SONiC OS without impacting the data plane. In SONiC 201911 and later versions, due to the advantages provided by the NVIDIA Mellanox Spectrum ASICs, warm reboot can achieve 0% packet loss during SONiC upgrades (including the SDK and firmware) and warm reboots.

Control plane downtime requirements as well as scaling requirements are the same as in {{<link url="Fast-Reboot">}}.

{{%notice info%}}

Warm reboot is designed and maintained for the T0 topology only.

{{%/notice%}}

To check if warm reboot is enabled:

```
admin@switch:~$ show platform mlnx issu
ISSU is disabled
```

If warm reboot is not enabled although it is supported by your platform, edit the SAI profile to enable it manually.

1. Open the `/usr/share/sonic/device/{platform name}/{sku name}/sai_{platform}.xml` file in a text editor. For example:

       admin@switch:~$ sudo vi /usr/share/sonic/device/x86_64-mlnx_msn2700-r0/ACS-MSN2700/sai_2700.xml
1. Set `issu-enabled` to _1_:

       <issu-enabled>1</issu-enabled>
1. Reboot the switch for changes to take effect:

       admin@switch:~$ sudo reboot 
1. Verify warm reboot is enabled:

       admin@sonic:~$ show platform mlnx issu
       ISSU is enabled
