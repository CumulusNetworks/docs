---
title: Update Cloud Activation Key
author: NVIDIA
weight: 395
toc: 3
---

NVIDIA provides a cloud activation key when you set up your premises. You use the cloud activation key (called the *config-key*) to access the cloud services. Note that these authorization keys are different from the ones you use to configure the CLI. 

On occasion, you might want to update your cloud service activation key---for example, if you mistyped the key during installation and now your existing key does not work, or you received a new key for your premises from NVIDIA.

Update the activation key using the NetQ CLI:

{{<tabs "Cloud Key">}}

{{<tab "NetQ CLI">}}

Run the following command on your master NetQ VM replacing `text-opta-key` with your new key.

```
cumulus@<hostname>:~$ netq install standalone activate-job config-key <text-opta-key>
```

{{</tab>}}

{{</tabs>}}