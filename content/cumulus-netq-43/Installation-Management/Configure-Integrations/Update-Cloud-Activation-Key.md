---
title: Update Cloud Activation Key
author: NVIDIA
weight: 395
toc: 3
---

You use the cloud activation key (called the *config-key*) to access the cloud services, not the authorization keys you use for configuring the CLI. NVIDIA provides the key when you set up your premises.

On occasion, you might want to update your cloud service activation key. For example, if you mistyped the key during installation and now your existing key does not work, or you received a new key for your premises from NVIDIA.

Update the activation key using the NetQ CLI:

{{<tabs "Cloud Key">}}

{{<tab "NetQ CLI">}}

Run the following command on your standalone or master NetQ Cloud Appliance or VM replacing `text-opta-key` with your new key.

```
cumulus@<hostname>:~$ netq install standalone activate-job config-key <text-opta-key>
```

{{</tab>}}

{{</tabs>}}